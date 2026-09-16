"""Tầng minh hoạ: nạp và tra hình gắn với công thức.

Khác bốn kho kia, kho minh hoạ đọc từ `data/illustrations/index.json` chứ không
từ các file lát cắt — ở đây `index.json` **là** dữ liệu gốc, vì nó do
`tools/build_illustrations.py` ghép từ khai báo thủ công (`bindings.json`) với
kết quả của bộ tự khớp.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any

from ..config import settings
from ..models import Illustration

#: SVG có thể chứa mã chạy được. Kho này do công cụ của chính người dùng sinh
#: ra nên rủi ro thấp, nhưng API sẽ phục vụ lại nội dung ấy cho trình duyệt —
#: kiểm một lượt vẫn hơn là tin vào nguồn gốc.
_UNSAFE_MARKERS = ("<script", "javascript:", "<foreignobject", " onload=", " onerror=", " onclick=")


def source_file(corpus_root: Path | None = None) -> Path:
    root = Path(corpus_root or settings.corpus_root)
    return root / "data" / "illustrations" / "index.json"


def assets_dir(corpus_root: Path | None = None) -> Path:
    root = Path(corpus_root or settings.corpus_root)
    return (root / "data" / "illustrations").resolve()


def load(conn: sqlite3.Connection, corpus_root: Path | None = None) -> int:
    """Nạp kho minh hoạ vào bảng `illustrations`. Trả số bản ghi đã nạp."""
    path = source_file(corpus_root)
    if not path.is_file():
        return 0
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return 0

    rows: list[tuple] = []
    for item in document.get("illustrations", []):
        formula_id = item.get("formula_id")
        if not formula_id:
            continue
        raster = item.get("raster") or {}
        rows.append(
            (
                formula_id,
                item.get("kind", "2d-svg"),
                item.get("source", ""),
                item.get("generator", ""),
                item.get("caption_vi", ""),
                item.get("subject", ""),
                item.get("level", ""),
                item.get("topic", ""),
                item.get("title", ""),
                item.get("svg_path"),
                raster.get("path"),
                raster.get("width"),
                raster.get("height"),
                raster.get("status", ""),
                json.dumps(item, ensure_ascii=False),
            )
        )
    if rows:
        conn.executemany(
            "INSERT OR REPLACE INTO illustrations (formula_id, kind, source, generator,"
            " caption_vi, subject, level, topic, title, svg_path, raster_path,"
            " width, height, status, payload)"
            " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            rows,
        )
    return len(rows)


def _resolve(relative: str | None, corpus_root: Path | None = None) -> Path | None:
    """Đường dẫn tuyệt đối của một tệp minh hoạ, có chặn thoát thư mục.

    `svg_path` đến từ dữ liệu, và dữ liệu thì có thể sai hoặc bị sửa. Không
    kiểm thì một mục ghi `../../../etc/passwd` sẽ được API phục vụ ra ngoài.
    """
    if not relative:
        return None
    base = assets_dir(corpus_root)
    try:
        candidate = (base / relative).resolve()
        candidate.relative_to(base)
    except (ValueError, OSError):
        return None
    return candidate if candidate.is_file() else None


def read_svg(relative: str | None, corpus_root: Path | None = None) -> str | None:
    """Đọc nội dung SVG, trả None nếu thiếu tệp hoặc nội dung không an toàn."""
    path = _resolve(relative, corpus_root)
    if path is None or path.suffix.lower() != ".svg":
        return None
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return None
    lowered = content.lower()
    if any(marker in lowered for marker in _UNSAFE_MARKERS):
        return None
    return content


def _to_model(row: sqlite3.Row, *, with_svg: bool, corpus_root: Path | None) -> Illustration:
    return Illustration(
        formula_id=row["formula_id"],
        kind=row["kind"],
        source=row["source"],
        generator=row["generator"],
        caption_vi=row["caption_vi"],
        # Ba trục lọc đi kèm bản ghi để nơi hiển thị không phải mở lại kho công
        # thức chỉ để biết một hình thuộc môn nào. `Illustration` khai
        # `extra="allow"` nên chúng đi thẳng vào model mà không cần thêm trường.
        subject=row["subject"],
        level=row["level"],
        topic=row["topic"],
        title=row["title"],
        svg_path=row["svg_path"],
        raster_path=row["raster_path"],
        width=row["width"],
        height=row["height"],
        status=row["status"] or "",
        svg=read_svg(row["svg_path"], corpus_root) if with_svg else None,
    )


def get(
    conn: sqlite3.Connection,
    formula_id: str,
    *,
    with_svg: bool = True,
    corpus_root: Path | None = None,
) -> Illustration | None:
    row = conn.execute(
        "SELECT * FROM illustrations WHERE formula_id = ?", (formula_id,)
    ).fetchone()
    return None if row is None else _to_model(row, with_svg=with_svg, corpus_root=corpus_root)


def for_formulas(
    conn: sqlite3.Connection,
    formula_ids: list[str],
    *,
    with_svg: bool = False,
    limit: int = 4,
    corpus_root: Path | None = None,
) -> list[Illustration]:
    """Hình minh hoạ cho một loạt công thức, giữ nguyên thứ tự ưu tiên đầu vào.

    Bỏ qua các mục mới chỉ là chỗ dành sẵn (`status = placeholder`): hiện một ô
    trống cho người học còn tệ hơn không hiện gì.
    """
    if not formula_ids:
        return []
    placeholders = ",".join("?" * len(formula_ids))
    rows = {
        row["formula_id"]: row
        for row in conn.execute(
            f"SELECT * FROM illustrations WHERE formula_id IN ({placeholders})", formula_ids
        )
    }
    out: list[Illustration] = []
    for formula_id in formula_ids:
        row = rows.get(formula_id)
        if row is None:
            continue
        model = _to_model(row, with_svg=with_svg, corpus_root=corpus_root)
        if model.ready:
            out.append(model)
        if len(out) >= limit:
            break
    return out


def browse(
    conn: sqlite3.Connection,
    *,
    subject: str | None = None,
    level: str | None = None,
    topic: str | None = None,
    generator: str | None = None,
    query: str | None = None,
    limit: int = 60,
    with_svg: bool = False,
    corpus_root: Path | None = None,
) -> list[Illustration]:
    """Duyệt kho minh hoạ theo môn / cấp / chủ đề / generator.

    Bốn kho kia truy xuất từ công thức sang hình; hàm này đi thẳng vào kho hình,
    vì khi thư viện lớn lên thì câu hỏi thường gặp đổi chiều: "môn Lí bậc THPT
    đã có những hình gì" chứ không còn là "công thức này có hình không".
    """
    where: list[str] = ["status != 'placeholder'"]
    args: list[Any] = []
    for column, value in (
        ("subject", subject), ("level", level), ("topic", topic), ("generator", generator)
    ):
        if value:
            where.append(f"{column} = ?")
            args.append(value)
    if query:
        where.append(
            "(formula_id LIKE ? OR title LIKE ? OR topic LIKE ? OR caption_vi LIKE ?)"
        )
        args.extend([f"%{query}%"] * 4)
    args.append(max(1, limit))
    rows = conn.execute(
        f"SELECT * FROM illustrations WHERE {' AND '.join(where)}"
        " ORDER BY subject, level, formula_id LIMIT ?",
        args,
    )
    return [_to_model(r, with_svg=with_svg, corpus_root=corpus_root) for r in rows]


def facets(conn: sqlite3.Connection) -> dict[str, dict[str, int]]:
    """Các giá trị lọc đang có và số hình của mỗi giá trị."""
    out: dict[str, dict[str, int]] = {}
    for column in ("subject", "level", "generator"):
        out[column] = {
            row[column]: row["n"]
            for row in conn.execute(
                f"SELECT {column}, COUNT(*) AS n FROM illustrations"
                f" WHERE {column} != '' GROUP BY {column} ORDER BY n DESC"
            )
        }
    return out


def stats(conn: sqlite3.Connection) -> dict[str, Any]:
    total = conn.execute("SELECT COUNT(*) AS n FROM illustrations").fetchone()["n"]
    by_kind = {
        row["kind"]: row["n"]
        for row in conn.execute(
            "SELECT kind, COUNT(*) AS n FROM illustrations GROUP BY kind"
        )
    }
    placeholders = conn.execute(
        "SELECT COUNT(*) AS n FROM illustrations WHERE status = 'placeholder'"
    ).fetchone()["n"]
    return {"total": total, "by_kind": by_kind, "placeholders": placeholders}
