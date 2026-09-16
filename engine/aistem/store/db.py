"""Kết nối SQLite và lược đồ bảng.

Toàn bộ kho AISTEM (6 931 bản ghi, ~20 MB JSON) nén gọn vào một file SQLite
duy nhất. Không cần server DB: đọc nhiều - ghi hiếm, FTS5 lo tìm kiếm toàn văn,
numpy lo phần vector nếu có nhúng.
"""

from __future__ import annotations

import json
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from ..config import settings

SCHEMA = """
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;
PRAGMA foreign_keys = ON;

-- Một bảng cho cả bốn kho: khác nhau ở cột `kind`, chi tiết nằm trong `payload`.
CREATE TABLE IF NOT EXISTS records (
    rowid       INTEGER PRIMARY KEY,
    kind        TEXT NOT NULL,          -- formula | lesson | problem | exam
    rid         TEXT NOT NULL,          -- id gốc trong kho
    subject     TEXT NOT NULL DEFAULT '',
    level       TEXT NOT NULL DEFAULT '',
    topic       TEXT NOT NULL DEFAULT '',
    title       TEXT NOT NULL DEFAULT '',
    grades      TEXT NOT NULL DEFAULT '[]',
    curriculum  TEXT NOT NULL DEFAULT '[]',
    tags        TEXT NOT NULL DEFAULT '[]',
    difficulty  INTEGER,
    ptype       TEXT NOT NULL DEFAULT '',
    source_file TEXT NOT NULL DEFAULT '',
    payload     TEXT NOT NULL,
    UNIQUE (kind, rid)
);

CREATE INDEX IF NOT EXISTS idx_records_kind_subject ON records (kind, subject);
CREATE INDEX IF NOT EXISTS idx_records_level        ON records (level);
CREATE INDEX IF NOT EXISTS idx_records_topic        ON records (topic);
CREATE INDEX IF NOT EXISTS idx_records_rid          ON records (rid);

-- Chỉ mục toàn văn. `folded` là bản không dấu do textnorm.fold() sinh:
-- tokenizer unicode61 gỡ được dấu thanh nhưng không đổi được 'đ' -> 'd'.
CREATE VIRTUAL TABLE IF NOT EXISTS records_fts USING fts5(
    title, topic, body, folded,
    tokenize = "unicode61 remove_diacritics 2"
);

-- Đồ thị nối các kho: formulas_used, prerequisites, related, formulas...
CREATE TABLE IF NOT EXISTS edges (
    src_kind TEXT NOT NULL,
    src_id   TEXT NOT NULL,
    rel      TEXT NOT NULL,
    dst_kind TEXT NOT NULL,
    dst_id   TEXT NOT NULL,
    PRIMARY KEY (src_kind, src_id, rel, dst_id)
) WITHOUT ROWID;

CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges (dst_kind, dst_id, rel);

-- Kỹ năng của từng bài tập — trục để chẩn đoán lỗ hổng kiến thức.
-- `skill_key` là khoá chuẩn hoá (token nội dung, sắp xếp): nó gộp được
-- "phân tích đa thức thành nhân tử" với "phan-tich-da-thuc-thanh-nhan-tu",
-- vốn là hai cách viết cùng tồn tại trong kho.
CREATE TABLE IF NOT EXISTS problem_skills (
    problem_id TEXT NOT NULL,
    skill      TEXT NOT NULL,
    skill_fold TEXT NOT NULL,
    skill_key  TEXT NOT NULL DEFAULT '',
    PRIMARY KEY (problem_id, skill)
) WITHOUT ROWID;

CREATE INDEX IF NOT EXISTS idx_skills_fold ON problem_skills (skill_fold);
CREATE INDEX IF NOT EXISTS idx_skills_key  ON problem_skills (skill_key);

-- Chỉ mục ngược token -> bài tập, để so khớp kỹ năng gần đúng khi hai cách
-- viết không trùng khít. `df` là số bài chứa token, dùng tính IDF.
CREATE TABLE IF NOT EXISTS skill_tokens (
    token      TEXT NOT NULL,
    problem_id TEXT NOT NULL,
    PRIMARY KEY (token, problem_id)
) WITHOUT ROWID;

CREATE INDEX IF NOT EXISTS idx_skill_tokens_problem ON skill_tokens (problem_id);

-- Hình minh hoạ, khoá theo công thức. Đây là phần đính kèm của công thức chứ
-- không phải một kho ngang hàng, nên để bảng riêng thay vì nhét vào `records`.
CREATE TABLE IF NOT EXISTS illustrations (
    formula_id  TEXT PRIMARY KEY,
    kind        TEXT NOT NULL DEFAULT '2d-svg',
    source      TEXT NOT NULL DEFAULT '',
    generator   TEXT NOT NULL DEFAULT '',
    caption_vi  TEXT NOT NULL DEFAULT '',
    subject     TEXT NOT NULL DEFAULT '',
    level       TEXT NOT NULL DEFAULT '',
    topic       TEXT NOT NULL DEFAULT '',
    title       TEXT NOT NULL DEFAULT '',
    svg_path    TEXT,
    raster_path TEXT,
    width       INTEGER,
    height      INTEGER,
    status      TEXT NOT NULL DEFAULT '',
    payload     TEXT NOT NULL
) WITHOUT ROWID;

CREATE INDEX IF NOT EXISTS idx_illustrations_kind ON illustrations (kind);
CREATE INDEX IF NOT EXISTS idx_illustrations_facets ON illustrations (subject, level);

-- Nhúng vector (tuỳ chọn). Không có thì hệ thống chạy thuần từ khoá.
CREATE TABLE IF NOT EXISTS embeddings (
    kind      TEXT NOT NULL,
    rid       TEXT NOT NULL,
    model     TEXT NOT NULL,
    dim       INTEGER NOT NULL,
    vector    BLOB NOT NULL,
    PRIMARY KEY (kind, rid)
) WITHOUT ROWID;

-- Nhật ký phiên làm bài, phục vụ chẩn đoán và lộ trình luyện tập.
CREATE TABLE IF NOT EXISTS attempts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    learner     TEXT NOT NULL DEFAULT 'local',
    problem_id  TEXT NOT NULL,
    answer      TEXT NOT NULL DEFAULT '',
    correct     INTEGER NOT NULL DEFAULT 0,
    verdict     TEXT NOT NULL DEFAULT '',
    created_at  TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_attempts_learner ON attempts (learner, created_at);
CREATE INDEX IF NOT EXISTS idx_attempts_problem ON attempts (learner, problem_id);

-- Bài học đã đọc xong. Tách khỏi `attempts` vì đọc xong một bài giảng và làm
-- đúng một bài tập là hai chuyện khác nhau: cái đầu là đã tiếp xúc, cái sau
-- mới là bằng chứng đã hiểu.
CREATE TABLE IF NOT EXISTS lesson_progress (
    learner      TEXT NOT NULL DEFAULT 'local',
    lesson_id    TEXT NOT NULL,
    status       TEXT NOT NULL DEFAULT 'done',   -- done | in-progress | skipped
    completed_at TEXT NOT NULL DEFAULT (datetime('now')),
    PRIMARY KEY (learner, lesson_id)
) WITHOUT ROWID;

-- Lịch ôn giãn cách, tính theo **kỹ năng** chứ không theo từng bài tập: người
-- học cần nhớ cách làm, không cần nhớ một đề cụ thể. Khoá là `skill_key` đã
-- chuẩn hoá nên hai cách viết của cùng một kỹ năng dùng chung một lịch.
CREATE TABLE IF NOT EXISTS skill_reviews (
    learner       TEXT NOT NULL DEFAULT 'local',
    skill_key     TEXT NOT NULL,
    skill_label   TEXT NOT NULL DEFAULT '',
    repetitions   INTEGER NOT NULL DEFAULT 0,
    ease          REAL NOT NULL DEFAULT 2.5,
    interval_days REAL NOT NULL DEFAULT 0,
    due_at        TEXT NOT NULL DEFAULT (datetime('now')),
    last_seen_at  TEXT NOT NULL DEFAULT (datetime('now')),
    lapses        INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (learner, skill_key)
) WITHOUT ROWID;

CREATE INDEX IF NOT EXISTS idx_reviews_due ON skill_reviews (learner, due_at);

CREATE TABLE IF NOT EXISTS meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
"""


def connect(path: Path | None = None, *, readonly: bool = False) -> sqlite3.Connection:
    target = Path(path or settings.database)
    if readonly:
        if not target.exists():
            raise FileNotFoundError(
                f"Chưa có cơ sở dữ liệu tại {target}. Chạy `aistem db build` trước."
            )
        conn = sqlite3.connect(f"file:{target}?mode=ro", uri=True, check_same_thread=False)
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(target, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@contextmanager
def session(path: Path | None = None, *, readonly: bool = False) -> Iterator[sqlite3.Connection]:
    conn = connect(path, readonly=readonly)
    try:
        yield conn
        if not readonly:
            conn.commit()
    finally:
        conn.close()


def init_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA)


def get_meta(conn: sqlite3.Connection, key: str, default: Any = None) -> Any:
    row = conn.execute("SELECT value FROM meta WHERE key = ?", (key,)).fetchone()
    if row is None:
        return default
    try:
        return json.loads(row["value"])
    except json.JSONDecodeError:
        return row["value"]


def set_meta(conn: sqlite3.Connection, key: str, value: Any) -> None:
    conn.execute(
        "INSERT INTO meta (key, value) VALUES (?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (key, json.dumps(value, ensure_ascii=False)),
    )


def load_record(conn: sqlite3.Connection, kind: str, rid: str) -> dict[str, Any] | None:
    row = conn.execute(
        "SELECT payload FROM records WHERE kind = ? AND rid = ?", (kind, rid)
    ).fetchone()
    return json.loads(row["payload"]) if row else None


def load_records(conn: sqlite3.Connection, kind: str, rids: list[str]) -> dict[str, dict[str, Any]]:
    """Nạp nhiều bản ghi một lượt, tránh N+1 truy vấn."""
    if not rids:
        return {}
    out: dict[str, dict[str, Any]] = {}
    for i in range(0, len(rids), 500):  # SQLite giới hạn số tham số
        chunk = rids[i : i + 500]
        placeholders = ",".join("?" * len(chunk))
        rows = conn.execute(
            f"SELECT rid, payload FROM records WHERE kind = ? AND rid IN ({placeholders})",
            (kind, *chunk),
        ).fetchall()
        out.update({r["rid"]: json.loads(r["payload"]) for r in rows})
    return out


def stats(conn: sqlite3.Connection) -> dict[str, Any]:
    counts = {
        row["kind"]: row["n"]
        for row in conn.execute("SELECT kind, COUNT(*) AS n FROM records GROUP BY kind")
    }
    by_subject = [
        dict(row)
        for row in conn.execute(
            "SELECT kind, subject, COUNT(*) AS n FROM records "
            "GROUP BY kind, subject ORDER BY kind, n DESC"
        )
    ]
    return {
        "counts": counts,
        "total": sum(counts.values()),
        "by_subject": by_subject,
        "edges": conn.execute("SELECT COUNT(*) AS n FROM edges").fetchone()["n"],
        "skills": conn.execute(
            "SELECT COUNT(DISTINCT skill) AS n FROM problem_skills"
        ).fetchone()["n"],
        "embeddings": conn.execute("SELECT COUNT(*) AS n FROM embeddings").fetchone()["n"],
        "illustrations": conn.execute(
            "SELECT COUNT(*) AS n FROM illustrations"
        ).fetchone()["n"],
        "built_at": get_meta(conn, "built_at"),
        "corpus_root": get_meta(conn, "corpus_root"),
    }
