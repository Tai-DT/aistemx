"""Pipeline xử lí một bài toán, từ đề vào tới lời giải đã kiểm chứng.

    đọc đề  →  phân loại  →  truy xuất kho  →  giải  →  kiểm chứng CAS  →  gợi ý

Điểm cốt lõi nằm ở chặng áp chót. Mô hình ngôn ngữ viết lời giải, nhưng nó
không phải trọng tài cho chính nó: SymPy tính lại đáp số và từng bước biến đổi
một cách độc lập, rồi hệ thống hạ mức tin cậy và ghi cảnh báo theo đúng những
gì kiểm chứng được. Người học luôn nhìn thấy hệ thống chắc tới đâu.
"""

from __future__ import annotations

import sqlite3
import time
from typing import Any

from .. import llm
from ..cas import verify_answer
from ..config import settings
from ..models import (
    Classification,
    Hit,
    SolutionStep,
    SolveRequest,
    SolveResponse,
    Verification,
)
from ..store import illustrations as illustration_store
from ..store.search import lessons_for_formulas, problems_by_skill
from ..textnorm import extract_number
from . import ingest, retrieve
from .classify import classify as classify_problem

SOLVE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "required": ["answer", "solution_steps", "formulas_used", "confidence"],
    "properties": {
        "answer": {
            "type": "string",
            "description": (
                "Đáp án cuối cùng, gọn. Với bài điền số thì ghi giá trị kèm đơn vị; "
                "với trắc nghiệm thì ghi khoá phương án."
            ),
        },
        "answer_numeric": {
            "type": "number",
            "description": "Giá trị số của đáp án nếu có, để hệ thống chấm tự động",
        },
        "answer_unit": {"type": "string", "description": "Đơn vị SI dạng ASCII, ví dụ m/s^2"},
        "solution_steps": {
            "type": "array",
            "minItems": 1,
            "description": "Lời giải từng bước, mỗi bước một phép biến đổi",
            "items": {
                "type": "object",
                "required": ["explain"],
                "properties": {
                    "explain": {
                        "type": "string",
                        "description": (
                            "Nói rõ LÀM GÌ và TẠI SAO lại làm thế. Đây là phần dạy học, "
                            "không phải phần trình bày biến đổi."
                        ),
                    },
                    "latex": {
                        "type": "string",
                        "description": (
                            "Biểu thức của bước, LaTeX thuần không bọc $. Viết đủ hai vế "
                            "của một đẳng thức trong cùng một bước để hệ thống kiểm chứng "
                            "lại được. Dùng dấu chấm thập phân, không dùng dấu phẩy."
                        ),
                    },
                },
            },
        },
        "formulas_used": {
            "type": "array",
            "items": {"type": "string"},
            "description": "id các công thức trong kho đã dùng. Chỉ được lấy id có thật.",
        },
        "hints": {
            "type": "array",
            "items": {"type": "string"},
            "description": "2-3 gợi ý mở dần, từ nhẹ tới nặng, không lộ đáp án ngay",
        },
        "common_mistakes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Lỗi học sinh hay mắc ở dạng bài này",
        },
        "confidence": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "description": "Mức tự tin vào lời giải. Thấp khi đề thiếu dữ kiện hoặc mơ hồ.",
        },
        "warnings": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Chỗ đề mâu thuẫn, thiếu dữ kiện, hoặc giả thiết bạn phải tự thêm",
        },
    },
}

SOLVE_SYSTEM = """Bạn là giáo viên Toán - Lí - Hoá - Sinh giải bài cho hệ thống AISTEM.

Nguyên tắc bắt buộc:
1. Chỉ dùng công thức có trong phần ngữ cảnh được cung cấp, và ghi đúng id của
   chúng vào formulas_used. Không bịa id. Nếu kho thiếu công thức cần thiết,
   vẫn giải nhưng để formulas_used rỗng và nói rõ trong warnings.
2. Mỗi bước phải viết được thành một đẳng thức đầy đủ hai vế trong trường latex,
   vì hệ thống sẽ dùng SymPy tính lại từng bước để kiểm chứng bạn.
   Viết `x = 3 + 4 = 7`, đừng viết chỉ `= 7`.
3. Trong latex dùng dấu chấm thập phân (3.14), không dùng dấu phẩy.
4. Trường explain là phần dạy học: nói vì sao chọn cách đó, vì sao bước này hợp lệ.
   Người đọc là học sinh đang không hiểu, không phải người chấm bài.
5. Giữ đủ chữ số trong tính toán trung gian, chỉ làm tròn ở đáp án cuối.
6. Nếu đề thiếu dữ kiện hoặc mâu thuẫn: nói thẳng trong warnings và hạ confidence.
   Không tự bịa thêm số liệu để bài ra kết quả đẹp.

Trả lời bằng tiếng Việt."""


def _prompt(statement: str, classification: Classification, context_block: str,
            reading: ingest.ReadResult) -> str:
    lines = [
        "### Đề bài",
        statement,
    ]
    if reading.given:
        lines += ["", "### Dữ kiện đã cho", *(f"- {g}" for g in reading.given)]
    if reading.asked:
        lines += ["", f"### Yêu cầu\n{reading.asked}"]
    if reading.choices:
        lines += [
            "",
            "### Các phương án",
            *(f"{c.get('key')}. {c.get('text')}" for c in reading.choices),
        ]
    lines += [
        "",
        "### Phân loại",
        f"Môn {classification.subject} · cấp {classification.level}"
        f" · chủ đề {classification.topic or '(chưa rõ)'}"
        f" · độ khó dự kiến {classification.difficulty}/5"
        + (f" · hệ {'/'.join(classification.curriculum)}" if classification.curriculum else ""),
        "",
        "### Ngữ cảnh từ kho AISTEM",
        context_block,
        "",
        "Hãy giải bài trên và trả kết quả theo đúng lược đồ.",
    ]
    return "\n".join(lines)


def _confidence(verification: Verification, model_confidence: float) -> str:
    """Gộp mức tự tin của mô hình với kết quả kiểm chứng độc lập.

    Kiểm chứng có quyền phủ quyết: mô hình tự tin đến mấy mà CAS bác bỏ đáp số
    thì mức tin cậy vẫn tụt xuống thấp.
    """
    if verification.answer_status == "refuted" or verification.steps_refuted:
        return "thap"
    if verification.answer_mismatch:
        return "thap"
    if verification.answer_status == "verified" and model_confidence >= 0.6:
        return "cao"
    if model_confidence >= 0.8 and verification.steps_verified > 0:
        return "cao"
    if model_confidence < 0.5:
        return "thap"
    return "trung-binh"


def _recommendations(
    conn: sqlite3.Connection, classification: Classification, formulas_used: list[str]
) -> list[Hit]:
    """Bài học và bài luyện đi kèm, để người học vá đúng chỗ vừa vấp."""
    out: list[Hit] = []
    if formulas_used:
        out.extend(lessons_for_formulas(conn, formulas_used, limit=3))
    if classification.skills:
        out.extend(
            problems_by_skill(
                conn,
                classification.skills,
                limit=4,
                difficulty_max=min(5, classification.difficulty + 1),
            )
        )
    seen: set[str] = set()
    unique = []
    for hit in out:
        if hit.id not in seen:
            seen.add(hit.id)
            unique.append(hit)
    return unique[:6]


def solve(conn: sqlite3.Connection, request: SolveRequest) -> SolveResponse:
    """Chạy trọn pipeline cho một đề bài."""
    started = time.perf_counter()
    model = settings.model_heavy if request.heavy else settings.model

    # 1. Đọc đề -----------------------------------------------------------------
    reading = ingest.read(
        request.statement,
        image_base64=request.image_base64,
        image_media_type=request.image_media_type,
        model=model,
    )

    # 2. Phân loại --------------------------------------------------------------
    classification = classify_problem(
        conn,
        reading.statement,
        hint_subject=request.subject,
        hint_level=request.level,
        hint_curriculum=request.curriculum,
        model=model,
    )

    # 3. Truy xuất kho ----------------------------------------------------------
    context = retrieve.gather(conn, reading.statement, classification)

    response = SolveResponse(
        statement=reading.statement,
        statement_latex=reading.statement_latex,
        classification=classification,
        context=context,
        model=model,
    )
    if reading.notes:
        response.warnings.append(f"Khi đọc đề: {reading.notes}")

    # 4. Giải -------------------------------------------------------------------
    if not llm.available():
        response.confidence = "thap"
        response.warnings.append(
            "Chưa cấu hình khoá API nên hệ thống không giải bài. Phần phân loại, "
            "truy xuất công thức và bài tương tự ở trên vẫn dùng được."
        )
        response.recommendations = _recommendations(conn, classification, [])
        response.context.illustrations = illustration_store.for_formulas(
            conn, [hit.id for hit in context.formulas[:6]], with_svg=True, limit=3
        )
        response.elapsed_ms = int((time.perf_counter() - started) * 1000)
        return response

    try:
        result = llm.structured(
            system=SOLVE_SYSTEM,
            prompt=_prompt(
                reading.statement, classification, retrieve.as_prompt_context(context), reading
            ),
            schema=SOLVE_SCHEMA,
            tool_name="giai_bai",
            tool_description="Trả về lời giải từng bước đã kiểm tra.",
            model=model,
        )
    except llm.LLMUnavailable as exc:
        response.confidence = "thap"
        response.warnings.append(str(exc))
        response.elapsed_ms = int((time.perf_counter() - started) * 1000)
        return response

    data = result.data
    response.answer = str(data.get("answer", "")).strip()
    response.answer_numeric = data.get("answer_numeric")
    response.answer_unit = data.get("answer_unit") or None
    response.solution_steps = [
        SolutionStep(explain=s.get("explain", ""), latex=s.get("latex") or None)
        for s in data.get("solution_steps", [])
        if isinstance(s, dict) and s.get("explain")
    ]
    response.warnings.extend(data.get("warnings") or [])

    if response.answer_numeric is None:
        response.answer_numeric = extract_number(response.answer)

    # Chỉ giữ lại id công thức có thật — mô hình vẫn có thể bịa id dù đã dặn.
    claimed = [str(f) for f in (data.get("formulas_used") or [])]
    response.formulas_used, invented = _keep_real_formulas(conn, claimed)
    if invented:
        response.warnings.append(
            "Bỏ qua id công thức không có trong kho: " + ", ".join(invented[:5])
        )

    # 5. Kiểm chứng độc lập bằng CAS -------------------------------------------
    if request.verify:
        response.verification = verify_answer(
            answer=response.answer,
            answer_numeric=response.answer_numeric,
            steps=[s.model_dump() for s in response.solution_steps],
            expected_unit=response.answer_unit,
        )
        if response.verification.answer_status == "refuted":
            response.warnings.append(
                "CAS bác bỏ đáp số: " + response.verification.answer_detail
            )
        elif response.verification.answer_mismatch:
            response.warnings.append(
                "Cần rà lại đáp số: " + response.verification.answer_detail
            )
        if response.verification.steps_refuted:
            bad = [s.index + 1 for s in response.verification.steps if s.status == "refuted"]
            response.warnings.append(
                f"CAS bác bỏ {len(bad)} bước biến đổi (bước {', '.join(map(str, bad))})"
            )
        if response.verification.unit_status == "inconsistent":
            response.warnings.append("Đơn vị đáp án: " + response.verification.unit_detail)

    response.confidence = _confidence(
        response.verification, float(data.get("confidence", 0.5))
    )

    # 6. Gợi ý học tiếp ---------------------------------------------------------
    response.recommendations = _recommendations(
        conn, classification, response.formulas_used
    )
    # Hình minh hoạ cho đúng công thức đã dùng; thiếu thì lấy theo công thức đã
    # truy xuất được. Với hình học và đồ thị, một hình nói được nhiều hơn cả
    # đoạn giải thích.
    response.context.illustrations = illustration_store.for_formulas(
        conn,
        response.formulas_used or [hit.id for hit in context.formulas[:6]],
        with_svg=True,
        limit=3,
    )
    if not request.show_steps:
        response.solution_steps = []

    response.elapsed_ms = int((time.perf_counter() - started) * 1000)
    return response


def _keep_real_formulas(
    conn: sqlite3.Connection, claimed: list[str]
) -> tuple[list[str], list[str]]:
    """Tách id công thức có thật khỏi id bịa."""
    if not claimed:
        return [], []
    placeholders = ",".join("?" * len(claimed))
    rows = conn.execute(
        f"SELECT rid FROM records WHERE kind = 'formula' AND rid IN ({placeholders})",
        claimed,
    ).fetchall()
    real = {row["rid"] for row in rows}
    return [c for c in claimed if c in real], [c for c in claimed if c not in real]
