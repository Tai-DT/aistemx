"""Nạp bốn kho JSON của AISTEM vào SQLite.

Đọc thẳng từ các file lát cắt (`data/<kho>/**/*.json`) chứ không đọc
`index.json` — file dẫn xuất có thể cũ hơn dữ liệu nguồn. Các file dẫn xuất
(`index.json`, `corpus.jsonl`, `usage.json`, `schema.json`) đều bị bỏ qua.
"""

from __future__ import annotations

import json
import sqlite3
import time
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .. import skills as skills_module
from ..config import settings
from ..models import RecordKind
from ..textnorm import fold, search_blob
from . import illustrations as illustrations_store
from .db import init_schema, session, set_meta, stats

DERIVED_FILES = {"index.json", "corpus.jsonl", "usage.json", "schema.json"}

#: kho -> (thư mục, khoá chứa mảng bản ghi)
SOURCES: dict[RecordKind, tuple[str, str]] = {
    RecordKind.FORMULA: ("formulas", "formulas"),
    RecordKind.LESSON: ("lessons", "lessons"),
    RecordKind.PROBLEM: ("problems", "problems"),
    RecordKind.EXAM: ("exams", "exams"),
}

#: kho -> [(trường chứa danh sách id, tên quan hệ, kho đích)]
LINKS: dict[RecordKind, list[tuple[str, str, RecordKind]]] = {
    RecordKind.FORMULA: [("related", "related", RecordKind.FORMULA)],
    RecordKind.LESSON: [
        ("formulas", "uses_formula", RecordKind.FORMULA),
        ("prerequisites", "prerequisite", RecordKind.LESSON),
    ],
    RecordKind.PROBLEM: [("formulas_used", "uses_formula", RecordKind.FORMULA)],
    RecordKind.EXAM: [("formulas_must_memorize", "must_memorize", RecordKind.FORMULA)],
}


@dataclass
class BuildReport:
    counts: dict[str, int] = field(default_factory=dict)
    edges: int = 0
    skills: int = 0
    illustrations: int = 0
    files: int = 0
    dangling_edges: list[str] = field(default_factory=list)
    elapsed_s: float = 0.0

    def as_dict(self) -> dict[str, Any]:
        return {
            "counts": self.counts,
            "total": sum(self.counts.values()),
            "edges": self.edges,
            "skills": self.skills,
            "illustrations": self.illustrations,
            "files": self.files,
            "dangling_edges": len(self.dangling_edges),
            "dangling_sample": self.dangling_edges[:10],
            "elapsed_s": round(self.elapsed_s, 2),
        }


def slice_files(directory: Path) -> list[Path]:
    """Mọi file JSON lát cắt trong một kho, quét đệ quy, bỏ file dẫn xuất."""
    if not directory.is_dir():
        return []
    return sorted(
        p for p in directory.rglob("*.json") if p.name not in DERIVED_FILES and p.is_file()
    )


def _iter_records(path: Path, array_key: str) -> Iterable[dict[str, Any]]:
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Không đọc được {path}: {exc}") from exc
    if isinstance(doc, list):
        records = doc
    elif isinstance(doc, dict):
        records = doc.get(array_key) or []
    else:
        records = []
    for rec in records:
        if isinstance(rec, dict) and rec.get("id"):
            yield rec


def _title_of(kind: RecordKind, rec: dict[str, Any]) -> str:
    if kind is RecordKind.FORMULA:
        return rec.get("name_vi") or rec.get("name_en") or rec["id"]
    if kind is RecordKind.LESSON:
        return rec.get("title_vi") or rec.get("title_en") or rec["id"]
    if kind is RecordKind.PROBLEM:
        return (rec.get("statement_vi") or rec.get("statement_en") or rec["id"])[:180]
    return rec.get("name") or rec["id"]


def _body_of(kind: RecordKind, rec: dict[str, Any]) -> str:
    """Chuỗi đưa vào FTS — chọn đúng các trường mang nghĩa tra cứu."""
    if kind is RecordKind.FORMULA:
        return search_blob(
            rec.get("name_vi"), rec.get("name_en"), rec.get("topic"), rec.get("subtopic"),
            rec.get("latex"), rec.get("vars"), rec.get("units"), rec.get("conditions"),
            rec.get("note"), rec.get("tags"),
        )
    if kind is RecordKind.LESSON:
        concepts = [
            f"{c.get('term_vi', '')} {c.get('term_en', '')} {c.get('definition', '')}"
            for c in rec.get("key_concepts", [])
            if isinstance(c, dict)
        ]
        return search_blob(
            rec.get("title_vi"), rec.get("title_en"), rec.get("unit"),
            rec.get("objectives"), concepts, rec.get("tags"),
            (rec.get("content") or "")[:4000],
        )
    if kind is RecordKind.PROBLEM:
        steps = [s.get("explain", "") for s in rec.get("solution_steps", []) if isinstance(s, dict)]
        return search_blob(
            rec.get("statement_vi"), rec.get("statement_en"), rec.get("topic"),
            rec.get("skills"), rec.get("tags"), steps[:6],
        )
    return search_blob(
        rec.get("name"), rec.get("provider"), rec.get("overview"),
        rec.get("tags"), rec.get("strategies"), rec.get("common_traps"),
    )


def _norm_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return list(value)
    return [value]


def build_database(
    corpus_root: Path | None = None,
    db_path: Path | None = None,
    *,
    verbose: bool = False,
) -> BuildReport:
    """Dựng lại toàn bộ cơ sở dữ liệu từ đầu.

    Tên hàm cố ý không phải `build`: gói `aistem.store` xuất lại hàm này, mà
    module chứa nó cũng tên `build`. Trùng tên thì `from ..store import build`
    lấy về hàm chứ không lấy module, và `build.ensure_built()` sẽ nổ ngay lúc
    khởi động — đúng loại lỗi chỉ lộ ra khi chạy thật.
    """
    started = time.perf_counter()
    root = Path(corpus_root or settings.corpus_root)
    data_dir = root / "data"
    if not data_dir.is_dir():
        raise FileNotFoundError(f"Không thấy thư mục dữ liệu: {data_dir}")

    report = BuildReport()
    target = Path(db_path or settings.database)
    for leftover in (target, target.with_suffix(target.suffix + "-wal"),
                     target.with_suffix(target.suffix + "-shm")):
        leftover.unlink(missing_ok=True)

    # id đã nạp, để phát hiện cạnh treo sau khi nạp xong toàn bộ
    known: dict[str, set[str]] = {k.value: set() for k in RecordKind}
    pending_edges: list[tuple[str, str, str, str, str]] = []

    with session(target) as conn:
        init_schema(conn)
        rowid = 0

        for kind, (folder, array_key) in SOURCES.items():
            directory = data_dir / folder
            files = slice_files(directory)
            report.files += len(files)
            loaded = 0

            for path in files:
                rel = str(path.relative_to(root))
                rows: list[tuple] = []
                fts_rows: list[tuple] = []
                skill_rows: list[tuple[str, str, str, str]] = []
                token_rows: list[tuple[str, str]] = []

                for rec in _iter_records(path, array_key):
                    rid = rec["id"]
                    if rid in known[kind.value]:
                        continue  # id trùng: giữ bản gặp trước, kho gốc đã validate là duy nhất
                    known[kind.value].add(rid)
                    rowid += 1
                    loaded += 1

                    title = _title_of(kind, rec)
                    topic = rec.get("topic") or rec.get("unit") or ""
                    body = _body_of(kind, rec)
                    rows.append(
                        (
                            rowid,
                            kind.value,
                            rid,
                            rec.get("subject", ""),
                            rec.get("level", ""),
                            topic,
                            title,
                            json.dumps(_norm_list(rec.get("grades")), ensure_ascii=False),
                            json.dumps(_norm_list(rec.get("curriculum")), ensure_ascii=False),
                            json.dumps(_norm_list(rec.get("tags")), ensure_ascii=False),
                            rec.get("difficulty"),
                            rec.get("type", ""),
                            rel,
                            json.dumps(rec, ensure_ascii=False),
                        )
                    )
                    fts_rows.append((rowid, title, topic, body, fold(f"{title} {topic} {body}")))

                    for source_field, rel_name, dst_kind in LINKS.get(kind, []):
                        for dst in _norm_list(rec.get(source_field)):
                            if isinstance(dst, str) and dst:
                                pending_edges.append(
                                    (kind.value, rid, rel_name, dst_kind.value, dst)
                                )

                    if kind is RecordKind.PROBLEM:
                        for skill in _norm_list(rec.get("skills")):
                            if isinstance(skill, str) and skill.strip():
                                name = skill.strip()
                                skill_rows.append(
                                    (rid, name, fold(name), skills_module.canonical(name))
                                )
                                token_rows.extend(
                                    (token, rid) for token in set(skills_module.tokens(name))
                                )

                if rows:
                    conn.executemany(
                        "INSERT INTO records (rowid, kind, rid, subject, level, topic, title,"
                        " grades, curriculum, tags, difficulty, ptype, source_file, payload)"
                        " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        rows,
                    )
                    conn.executemany(
                        "INSERT INTO records_fts (rowid, title, topic, body, folded)"
                        " VALUES (?,?,?,?,?)",
                        fts_rows,
                    )
                if skill_rows:
                    conn.executemany(
                        "INSERT OR IGNORE INTO problem_skills"
                        " (problem_id, skill, skill_fold, skill_key) VALUES (?,?,?,?)",
                        skill_rows,
                    )
                if token_rows:
                    conn.executemany(
                        "INSERT OR IGNORE INTO skill_tokens (token, problem_id) VALUES (?,?)",
                        token_rows,
                    )
                if verbose:
                    print(f"  {rel}: {len(rows)} bản ghi")

            report.counts[kind.value] = loaded

        # Cạnh: chỉ giữ cạnh trỏ tới bản ghi có thật, phần còn lại ghi vào báo cáo.
        good: list[tuple[str, str, str, str, str]] = []
        for src_kind, src_id, rel_name, dst_kind, dst_id in pending_edges:
            if dst_id in known[dst_kind]:
                good.append((src_kind, src_id, rel_name, dst_kind, dst_id))
            else:
                report.dangling_edges.append(f"{src_kind}:{src_id} -{rel_name}-> {dst_id}")
        conn.executemany(
            "INSERT OR IGNORE INTO edges (src_kind, src_id, rel, dst_kind, dst_id)"
            " VALUES (?,?,?,?,?)",
            good,
        )
        report.edges = len(good)
        report.skills = conn.execute(
            "SELECT COUNT(DISTINCT skill) AS n FROM problem_skills"
        ).fetchone()["n"]
        report.illustrations = illustrations_store.load(conn, root)

        set_meta(conn, "built_at", time.strftime("%Y-%m-%dT%H:%M:%S"))
        set_meta(conn, "corpus_root", str(root))
        set_meta(conn, "counts", report.counts)
        conn.execute("INSERT INTO records_fts(records_fts) VALUES ('optimize')")

    report.elapsed_s = time.perf_counter() - started
    return report


def database_stats(db_path: Path | None = None) -> dict[str, Any]:
    with session(db_path, readonly=True) as conn:
        return stats(conn)


def ensure_built(db_path: Path | None = None) -> Path:
    """Dựng DB nếu chưa có. Trả về đường dẫn file."""
    target = Path(db_path or settings.database)
    if not target.exists():
        build_database(db_path=target)
    return target


def _table_is_empty(conn: sqlite3.Connection, table: str) -> bool:
    return conn.execute(f"SELECT COUNT(*) AS n FROM {table}").fetchone()["n"] == 0
