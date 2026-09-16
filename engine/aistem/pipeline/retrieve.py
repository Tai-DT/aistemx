"""Bước truy xuất: gom đúng phần kho cần thiết cho một đề bài cụ thể.

Nguyên tắc: mô hình chỉ được giải dựa trên công thức có thật trong kho, và
mọi công thức đưa vào prompt đều kèm `id` để lời giải trích dẫn lại được. Nhờ
vậy lời giải bám đúng chương trình người học đang theo, và ta kiểm được nó
dùng công thức nào.
"""

from __future__ import annotations

import re
import sqlite3

from ..config import settings
from ..models import Classification, Formula, Hit, RecordKind, RetrievedContext
from ..store.search import Filters, lessons_for_formulas, search


def _filters_for(classification: Classification | None, kind: str, *, strict: bool) -> Filters:
    """Bộ lọc theo môn/cấp/hệ chương trình.

    `strict=False` chỉ giữ lại lọc theo môn: nếu siết cả cấp lẫn hệ mà kho
    không có gì khớp thì thà lấy công thức đúng môn còn hơn không lấy được gì.
    """
    if classification is None:
        return Filters(kinds=[kind])
    # Công thức thì chỉ lọc theo môn. Một công thức thuộc nhiều hệ chương trình
    # cùng lúc, và `curriculum` của nó chỉ ghi những hệ đã được gắn nhãn — siết
    # theo hệ ở đây sẽ loại đúng những công thức phổ thông nhất (đạo hàm của
    # tích, động năng) chỉ vì chúng không mang nhãn "ap".
    if kind == "formula":
        return Filters(kinds=[kind], subject=classification.subject or None)
    return Filters(
        kinds=[kind],
        subject=classification.subject or None,
        level=classification.level if strict else None,
        curriculum=(classification.curriculum[0] if classification.curriculum and strict else None),
    )


#: Câu hỏi của đề thường nằm ở mệnh đề cuối và mở đầu bằng một trong các từ này.
_ASK_RE = re.compile(
    r"(?:^|[.;?]\s*)((?:tính|tìm|xác định|cho biết|hỏi|chứng minh|giải|so sánh|"
    r"dự đoán|viết|lập|nêu|hãy)[^.;?]{4,180})",
    re.IGNORECASE,
)


def _focus(statement: str) -> str | None:
    """Rút mệnh đề hỏi ra khỏi đề bài.

    Phần đầu đề toàn dữ kiện riêng của bài — khối lượng, vận tốc, thể tích — và
    những từ ấy có mặt trong hàng trăm công thức. Mệnh đề hỏi mới là thứ nói
    đúng đại lượng cần tìm, nên nó đáng được tra riêng một lượt.
    """
    matches = _ASK_RE.findall(statement or "")
    if not matches:
        return None
    focus = max(matches, key=len).strip()
    return focus if len(focus) >= 8 and focus != statement.strip() else None


def _merge(primary: list[Hit], secondary: list[Hit], limit: int) -> list[Hit]:
    """Ghép hai bảng kết quả, ưu tiên bảng đầu, bỏ trùng."""
    seen: set[str] = set()
    merged: list[Hit] = []
    for hit in [*primary, *secondary]:
        if hit.id in seen:
            continue
        seen.add(hit.id)
        merged.append(hit)
        if len(merged) >= limit:
            break
    return merged


def _search_with_fallback(
    conn: sqlite3.Connection,
    query: str,
    classification: Classification | None,
    kind: str,
    limit: int,
    *,
    include_record: bool = False,
) -> list[Hit]:
    hits = search(
        conn,
        query,
        filters=_filters_for(classification, kind, strict=True),
        limit=limit,
        include_record=include_record,
    )
    if len(hits) >= max(2, limit // 3):
        return hits
    relaxed = search(
        conn,
        query,
        filters=_filters_for(classification, kind, strict=False),
        limit=limit,
        include_record=include_record,
    )
    seen = {h.id for h in hits}
    return hits + [h for h in relaxed if h.id not in seen][: limit - len(hits)]


def gather(
    conn: sqlite3.Connection,
    statement: str,
    classification: Classification | None = None,
    *,
    formulas: int | None = None,
    lessons: int | None = None,
    problems: int | None = None,
) -> RetrievedContext:
    """Gom công thức, bài học, bài tập tương tự và hồ sơ đề thi liên quan."""
    query = statement.strip()
    context = RetrievedContext()
    formula_limit = formulas or settings.retrieve_formulas

    by_statement = _search_with_fallback(
        conn, query, classification, "formula", formula_limit, include_record=True
    )
    focus = _focus(query)
    if focus:
        by_focus = _search_with_fallback(
            conn, focus, classification, "formula",
            max(4, formula_limit // 2), include_record=True,
        )
        context.formulas = _merge(by_focus, by_statement, formula_limit)
    else:
        context.formulas = by_statement
    context.similar_problems = _search_with_fallback(
        conn, query, classification, "problem",
        problems or settings.retrieve_problems, include_record=True,
    )

    # Bài học lấy theo hai đường rồi gộp: bám từ khoá của đề, và bám các công
    # thức vừa tìm được. Đường thứ hai bắt được bài giảng đúng chỗ ngay cả khi
    # đề dùng từ ngữ khác hẳn tiêu đề bài.
    keyword_lessons = _search_with_fallback(
        conn, query, classification, "lesson", lessons or settings.retrieve_lessons
    )
    graph_lessons = lessons_for_formulas(
        conn, [h.id for h in context.formulas[:6]], limit=lessons or settings.retrieve_lessons
    )
    seen = {h.id for h in keyword_lessons}
    context.lessons = keyword_lessons + [h for h in graph_lessons if h.id not in seen]
    context.lessons = context.lessons[: (lessons or settings.retrieve_lessons) + 2]

    if classification and classification.curriculum:
        context.exams = search(
            conn,
            classification.curriculum[0],
            filters=Filters(kinds=["exam"], subject=classification.subject or None),
            limit=2,
        )
    return context


def formula_records(context: RetrievedContext) -> list[Formula]:
    """Đổi các hit công thức thành đối tượng `Formula` đầy đủ để dựng prompt."""
    out: list[Formula] = []
    for hit in context.formulas:
        if hit.kind is RecordKind.FORMULA and hit.record:
            try:
                out.append(Formula.model_validate(hit.record))
            except Exception:
                continue
    return out


def as_prompt_context(context: RetrievedContext) -> str:
    """Dựng khối ngữ cảnh đưa vào prompt.

    Công thức ghi đầy đủ vì mô hình phải dùng đúng dạng của kho. Bài tập tương
    tự chỉ ghi đề và đáp án — đủ để mô hình bắt chước cách trình bày và mức độ
    chi tiết, không đủ để nó chép lời giải.
    """
    blocks: list[str] = []

    formulas = formula_records(context)
    if formulas:
        blocks.append(
            "## Công thức có trong kho AISTEM (chỉ được dùng công thức ở đây, "
            "trích dẫn bằng đúng id)\n\n"
            + "\n\n".join(f.as_prompt_block() for f in formulas)
        )

    if context.similar_problems:
        lines = []
        for hit in context.similar_problems:
            record = hit.record or {}
            lines.append(
                f"[{hit.id}] (độ khó {record.get('difficulty', '?')}/5, {hit.topic})\n"
                f"  Đề: {(record.get('statement_vi') or '')[:300]}\n"
                f"  Đáp án: {record.get('answer', '')}"
            )
        blocks.append("## Bài tập tương tự trong kho (tham khảo mức độ và cách trình bày)\n\n"
                      + "\n\n".join(lines))

    if context.lessons:
        lines = [f"[{h.id}] {h.title} — {h.topic}" for h in context.lessons]
        blocks.append("## Bài học liên quan\n\n" + "\n".join(lines))

    return "\n\n".join(blocks) if blocks else "(Kho không trả về ngữ cảnh nào khớp với đề này.)"
