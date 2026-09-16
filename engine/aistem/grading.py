"""Chấm bài và chẩn đoán lỗ hổng kiến thức.

Chấm ở đây không chỉ trả đúng/sai. Với mỗi câu sai, hệ thống nói được **sai ở
đâu** (kho đã ghi sẵn `why_wrong` cho từng phương án nhiễu), **thiếu kỹ năng
gì** (trường `skills`), và **học lại ở đâu** (đi ngược đồ thị công thức → bài
giảng). Đó là phần biến một bộ chấm thành một bộ dạy.

Bốn cách chấm, chọn theo dạng bài:

* `trac-nghiem` — so khoá phương án, kèm lời giải thích vì sao phương án đã
  chọn lại sai.
* `dien-so` — so giá trị theo dung sai, tự quy đổi đơn vị: `980 cm/s^2` và
  `9,8 m/s^2` là cùng một đáp án.
* `tu-luan` — so **tương đương biểu thức** bằng CAS, nên `\\frac{1}{2}`,
  `0.5` và `2^{-1}` đều được chấp nhận như nhau.
* còn lại — so văn bản đã chuẩn hoá không dấu.
"""

from __future__ import annotations

import re
import sqlite3
from collections import Counter, defaultdict
from typing import Any

from . import progress, quantities, skills
from .cas import compare_with_units, equivalent, numbers_match, parse_unit, to_sympy
from .config import settings
from .models import (
    DiagnosisRequest,
    DiagnosisResult,
    GradeRequest,
    GradeResult,
    Hit,
    PartResult,
    Problem,
    SkillStat,
)
from .store.db import load_record, load_records
from .store.search import lessons_for_formulas, problems_by_skill
from .textnorm import extract_number, fold

_CHOICE_RE = re.compile(r"\b([A-E])\b")


def _load_problem(conn: sqlite3.Connection, problem_id: str) -> Problem:
    record = load_record(conn, "problem", problem_id)
    if record is None:
        raise KeyError(f"Không có bài tập nào mang id {problem_id!r} trong kho.")
    return Problem.model_validate(record)


def _normalize_choice(answer: str) -> str | None:
    """Rút khoá phương án từ câu trả lời: 'B', 'b', 'đáp án B', 'chọn B.' đều ra 'B'."""
    match = _CHOICE_RE.search((answer or "").upper())
    return match.group(1) if match else None


def _grade_choice(problem: Problem, student: str) -> GradeResult:
    chosen = _normalize_choice(student)
    expected = _normalize_choice(problem.answer) or problem.answer.strip().upper()
    if chosen is None:
        return GradeResult(
            correct=False, verdict="khong-cham-duoc", method="choice",
            expected=expected, received=student,
            detail="Không nhận ra phương án nào trong câu trả lời (cần một chữ cái A-E).",
        )
    if chosen == expected:
        return GradeResult(
            correct=True, verdict="dung", method="choice", score=1.0,
            expected=expected, received=chosen, detail="Chọn đúng phương án.",
        )

    why = next(
        (c.why_wrong for c in problem.choices if c.key == chosen and c.why_wrong), ""
    )
    return GradeResult(
        correct=False, verdict="sai", method="choice",
        expected=expected, received=chosen,
        detail=f"Đáp án đúng là {expected}.",
        why_wrong=why or "Kho chưa ghi lí do cho phương án này.",
    )


#: Lệch trong khoảng này thì gần như chắc chắn là làm tròn quá sớm ở bước trung
#: gian chứ không phải sai phương pháp — đáng cho nửa điểm và một lời nhắc, chứ
#: không đáng gạch sai. Ngoài khoảng này thì sai lệch quá lớn để đổ cho làm tròn.
_NEAR_MISS_CEILING = 0.05


def _is_near_miss(expected: float | None, got: float | None, tolerance: float) -> bool:
    if expected is None or got is None:
        return False
    within, _ = numbers_match(expected, got, max(tolerance * 10, _NEAR_MISS_CEILING))
    return within


def _rounding_note(expected: float, error: float | None) -> str:
    gap = f"lệch {error:.2%} " if error is not None else ""
    return (
        f"Gần đúng: {gap}so với {expected:.10g}. "
        "Thường là do làm tròn quá sớm ở bước trung gian."
    )


def _is_prose_unit(unit: str) -> bool:
    """Đơn vị là mô tả bằng lời chứ không phải đơn vị đo?

    Kho có những "đơn vị" như `liên kết peptide`, `mắt xích`, `nhiễm sắc thể`.
    Chúng là danh từ đếm được, không có thứ nguyên để kiểm — và quan trọng hơn,
    câu trả lời đi kèm thường là một câu chứ không phải một con số.
    """
    text = (unit or "").strip()
    if not text:
        return False
    return " " in text and parse_unit(text) is None


def _grade_numeric(problem: Problem, student: str) -> GradeResult:
    tolerance = quantities.relative_tolerance(
        problem.tolerance, problem.answer_numeric, settings.default_tolerance
    )
    # Kho ghi đáp án ở hai chỗ: `answer_numeric` (máy đọc) và `answer` (người
    # đọc). Chúng có thể lệch nhau vì làm tròn — `0,046875` với `3/64 ≈ 0,0469`.
    # Khớp với bản nào cũng phải tính là đúng: chính kho công bố cả hai.
    candidates = [
        value
        for value in (problem.answer_numeric, extract_number(problem.answer))
        if value is not None
    ]
    if not candidates:
        return _grade_text(problem, student)

    if _is_prose_unit(problem.answer_unit or ""):
        return _grade_text(problem, student)

    unit = problem.answer_unit or ""
    if unit:
        # Thử từng ứng viên qua đúng đường quy đổi đơn vị. Không được chọn ứng
        # viên trước rồi mới quy đổi: đáp án `≈ 2,0 nF` có `answer_numeric` là
        # 2e-9 F, nên con số hiển thị (2,0) chỉ đúng khi đọc kèm tiền tố nano.
        for candidate in candidates:
            ok, detail = compare_with_units(student, candidate, unit, tolerance)
            if ok:
                return GradeResult(
                    correct=True, verdict="dung", method="numeric", score=1.0,
                    expected=problem.answer, received=student, detail=detail,
                )
        expected_value = candidates[0]
        _, detail = compare_with_units(student, expected_value, unit, tolerance)
        # Đúng số nhưng sai/thiếu đơn vị là một loại sai riêng, đáng được nói rõ.
        value = extract_number(student)
        matched = any(numbers_match(c, value, tolerance)[0] for c in candidates)
        _, error = numbers_match(expected_value, value, tolerance)
        if matched:
            return GradeResult(
                correct=False, verdict="sai-don-vi", method="numeric", score=0.5,
                expected=problem.answer, received=student, relative_error=error,
                detail="Giá trị số đúng nhưng đơn vị chưa đúng. " + detail,
            )
        if _is_near_miss(expected_value, value, tolerance):
            return GradeResult(
                correct=False, verdict="gan-dung", method="numeric", score=0.5,
                expected=problem.answer, received=student, relative_error=error,
                detail=_rounding_note(expected_value, error),
            )
        return GradeResult(
            correct=False, verdict="sai", method="numeric",
            expected=problem.answer, received=student, relative_error=error, detail=detail,
        )

    expected_value = candidates[0]
    value = extract_number(student)
    if value is None:
        return GradeResult(
            correct=False, verdict="khong-cham-duoc", method="numeric",
            expected=problem.answer, received=student,
            detail="Không tìm thấy giá trị số nào trong câu trả lời.",
        )
    ok = any(numbers_match(c, value, tolerance)[0] for c in candidates)
    _, error = numbers_match(expected_value, value, tolerance)
    if ok:
        return GradeResult(
            correct=True, verdict="dung", method="numeric", score=1.0,
            expected=problem.answer, received=student, relative_error=error,
            detail=f"Khớp {expected_value:.10g} trong dung sai {tolerance:g}.",
        )
    if _is_near_miss(expected_value, value, tolerance):
        return GradeResult(
            correct=False, verdict="gan-dung", method="numeric", score=0.5,
            expected=problem.answer, received=student, relative_error=error,
            detail=_rounding_note(expected_value, error),
        )
    return GradeResult(
        correct=False, verdict="sai", method="numeric",
        expected=problem.answer, received=student, relative_error=error,
        detail=f"Đáp án đúng là {problem.answer}.",
    )


def _grade_symbolic(problem: Problem, student: str) -> GradeResult:
    """So hai biểu thức về mặt toán học, không so mặt chữ."""
    expected_expr = to_sympy(problem.answer)
    student_expr = to_sympy(student)
    if expected_expr is not None and student_expr is not None:
        verdict, detail = equivalent(expected_expr, student_expr, require_same_symbols=False)
        if verdict == "equivalent":
            return GradeResult(
                correct=True, verdict="dung", method="symbolic", score=1.0,
                expected=problem.answer, received=student,
                detail=f"Biểu thức tương đương với đáp án ({detail}).",
            )
        if verdict == "different":
            return GradeResult(
                correct=False, verdict="sai", method="symbolic",
                expected=problem.answer, received=student,
                detail=f"Biểu thức không tương đương với đáp án ({detail}).",
            )
    # CAS chịu thua thì thử số, rồi cuối cùng mới so chữ.
    if problem.answer_numeric is not None or extract_number(problem.answer) is not None:
        return _grade_numeric(problem, student)
    return _grade_text(problem, student)


def _grade_text(problem: Problem, student: str) -> GradeResult:
    expected = fold(problem.answer)
    received = fold(student)
    if not received:
        return GradeResult(
            correct=False, verdict="khong-cham-duoc", method="text",
            expected=problem.answer, received=student, detail="Câu trả lời rỗng.",
        )
    if expected and (expected == received or expected in received or received in expected):
        return GradeResult(
            correct=True, verdict="dung", method="text", score=1.0,
            expected=problem.answer, received=student, detail="Trùng khớp nội dung đáp án.",
        )
    return GradeResult(
        correct=False, verdict="khong-cham-duoc", method="text",
        expected=problem.answer, received=student,
        detail=(
            "Đây là câu tự luận cần người chấm: hệ thống chỉ so được mặt chữ, "
            "không kết luận đúng sai."
        ),
    )


#: Đáp án gồm nhiều ý: `a) … b) …`, hoặc nhiều mệnh đề ngăn bằng dấu chấm phẩy.
#: Ép cả chuỗi về một con số rồi so là chấm bừa — con số đầu tiên chỉ nói được
#: về ý đầu tiên, còn các ý sau thì hệ thống chưa hề đọc tới.
_ITEM_MARKER_RE = re.compile(r"(?:^|[.;]\s+|\s)[(\[]?([a-dạ-ỹ1-4])[)\].]\s+\S")


def _is_multi_quantity(answer: str) -> bool:
    text = (answer or "").strip()
    if len(_ITEM_MARKER_RE.findall(text)) >= 2:
        return True
    if not re.search(r";\s*\S|(?:^|\s)và\s+\S+\s*[=≈]", text):
        return False
    # Hai dấu `=` trở lên, hoặc có dấu `;` ngăn cách: đúng là nhiều đại lượng.
    return text.count("=") + text.count("≈") >= 2 or ";" in text


def _grade_multi(problem: Problem, student: str) -> GradeResult:
    """Chấm đáp án gồm nhiều đại lượng số, có điểm từng phần.

    Ghép theo nhãn nên thứ tự trả lời không quan trọng, và mỗi đại lượng được
    so bằng đúng bộ máy như bài một đáp số: quy đổi đơn vị, dung sai tương đối.
    """
    expected = quantities.parse_quantities(problem.answer)
    received = quantities.parse_quantities(student)

    parts: list[PartResult] = []
    for want, got in quantities.align(expected, received):
        if not want.looks_like_a_quantity:
            # Mẩu này là diễn giải bằng lời, không phải đại lượng. Máy không đọc
            # được nó, nên chỉ có đúng một cách kết luận trung thực: nếu người
            # học chép lại y hệt thì coi như khớp, còn khác đi thì nói rõ là
            # CHƯA CHẤM ĐƯỢC. Xếp nó vào ô "sai" là kết tội một thứ chưa ai chấm.
            same = got is not None and fold(want.body or want.raw) == fold(got.body or got.raw)
            parts.append(
                PartResult(
                    label=want.label,
                    correct=same,
                    status="dung" if same else "chua-cham-duoc",
                    expected=want.raw,
                    received=got.raw if got is not None else "",
                    detail=("trùng khớp nguyên văn" if same
                            else "phần này là diễn giải bằng lời, máy chưa chấm được"),
                )
            )
            continue
        if got is None or got.value is None:
            parts.append(
                PartResult(label=want.label, correct=False, status="sai", expected=want.raw,
                           received="", detail="thiếu đại lượng này trong câu trả lời")
            )
            continue
        # So bằng giá trị **đã tách sẵn**, không đọc lại từ chuỗi gốc: hai tầng
        # đọc số dùng hai quy ước khác nhau về dấu `=` nào là dấu chốt, và khi
        # chúng lệch nhau thì một đáp án đúng nguyên văn vẫn bị chấm sai.
        tolerance = quantities.relative_tolerance(
            problem.tolerance, want.value, settings.default_tolerance
        )
        if want.unit and got.unit and fold(want.unit) != fold(got.unit):
            ok, detail = compare_with_units(
                f"{got.value} {got.unit}", want.value, want.unit, tolerance
            )
        else:
            ok, error = numbers_match(want.value, got.value, tolerance)
            detail = (
                f"khớp {want.value:.10g} {want.unit}".strip() if ok
                else (f"lệch {error:.3g} so với {want.value:.10g}" if error is not None
                      else "không khớp")
            )
        parts.append(
            PartResult(label=want.label, correct=ok, status="dung" if ok else "sai",
                       expected=want.raw, received=got.raw, detail=detail)
        )

    right = sum(1 for part in parts if part.status == "dung")
    wrong_parts = [part for part in parts if part.status == "sai"]
    unchecked = [part for part in parts if part.status == "chua-cham-duoc"]
    total = len(parts) or 1
    if right == total:
        verdict, correct = "dung", True
        detail = f"Đúng cả {total} phần."
    elif not wrong_parts:
        # Mọi phần chấm được đều đúng, chỉ còn phần diễn giải chưa chấm. Đây
        # KHÔNG phải "sai một phần" — không có phần nào sai cả. Nói đúng như
        # vậy, và để người đọc tự đối chiếu nốt phần lời.
        verdict, correct = "dung-mot-phan", False
        names = ", ".join(part.label for part in unchecked)
        detail = (
            f"Đúng cả {right} phần chấm được. Còn {len(unchecked)} phần là diễn giải"
            f" bằng lời nên máy chưa chấm ({names}) — cần đọc lại bằng mắt."
        )
    elif right:
        verdict, correct = "dung-mot-phan", False
        wrong = ", ".join(part.label for part in wrong_parts)
        detail = f"Đúng {right}/{total} phần. Còn sai: {wrong}."
    else:
        verdict, correct = "sai", False
        detail = f"Không phần nào trong {total} khớp đáp án."

    return GradeResult(
        correct=correct, verdict=verdict, method="multi", score=round(right / total, 3),
        expected=problem.answer, received=student, detail=detail, parts=parts,
    )


#: Đáp án dạng bảng đúng/sai: `(a) Đúng; (b) Sai; (c) Đúng; (d) Sai`. Đây là
#: dạng "câu trắc nghiệm đúng - sai" của đề thi Việt Nam hiện hành, và nó chấm
#: được **tất định**: không có dung sai, không có cách viết nào khác.
_TRUTH_ITEM_RE = re.compile(
    r"[(\[]?\s*([a-dA-D1-4])\s*[)\].:]\s*(đúng|sai|dung|true|false|t|f|đ|s)\b",
    re.IGNORECASE,
)
_TRUE_WORDS = {"đúng", "dung", "true", "t", "đ"}


def _truth_table(text: str) -> dict[str, bool]:
    """`(a) Đúng; (b) Sai` -> {'a': True, 'b': False}. Rỗng nếu không phải dạng này."""
    table: dict[str, bool] = {}
    for label, word in _TRUTH_ITEM_RE.findall(text or ""):
        table[label.lower()] = fold(word) in {fold(w) for w in _TRUE_WORDS}
    return table


def _grade_truth_table(problem: Problem, student: str) -> GradeResult:
    """Chấm bảng đúng/sai theo từng ý.

    Ghép theo nhãn, nên thiếu một ý là thiếu chứ không phải sai — người học bỏ
    trống ý (c) không giống với người trả lời (c) ngược.
    """
    expected = _truth_table(problem.answer)
    received = _truth_table(student)

    parts: list[PartResult] = []
    for label in sorted(expected):
        want = expected[label]
        got = received.get(label)
        if got is None:
            parts.append(
                PartResult(label=label, correct=False, status="sai",
                           expected="Đúng" if want else "Sai", received="",
                           detail="thiếu ý này trong câu trả lời")
            )
            continue
        ok = got == want
        parts.append(
            PartResult(label=label, correct=ok, status="dung" if ok else "sai",
                       expected="Đúng" if want else "Sai",
                       received="Đúng" if got else "Sai",
                       detail="khớp" if ok else "ngược với đáp án")
        )

    right = sum(1 for part in parts if part.correct)
    total = len(parts) or 1
    if right == total:
        verdict, correct, detail = "dung", True, f"Đúng cả {total} ý."
    elif right:
        wrong = ", ".join(part.label for part in parts if not part.correct)
        verdict, correct = "dung-mot-phan", False
        detail = f"Đúng {right}/{total} ý. Còn sai: {wrong}."
    else:
        verdict, correct, detail = "sai", False, f"Không ý nào trong {total} khớp đáp án."

    return GradeResult(
        correct=correct, verdict=verdict, method="multi", score=round(right / total, 3),
        expected=problem.answer, received=student, detail=detail, parts=parts,
    )


def grade_problem(problem: Problem, student_answer: str) -> GradeResult:
    """Chấm một câu trả lời theo đúng dạng của bài."""
    student = (student_answer or "").strip()
    if problem.type == "trac-nghiem" and problem.choices:
        result = _grade_choice(problem, student)
    elif len(_truth_table(problem.answer)) >= 2:
        result = _grade_truth_table(problem, student)
    elif quantities.countable_quantities(problem.answer) >= 2:
        result = _grade_multi(problem, student)
    elif _is_multi_quantity(problem.answer) and quantities.countable_quantities(problem.answer):
        # Chỉ một mẩu chấm máy được, phần còn lại là lời. Vẫn hơn hẳn im lặng:
        # người học ít nhất biết con số của mình đúng hay sai, và được nói rõ
        # phần diễn giải chưa ai chấm.
        result = _grade_multi(problem, student)
    elif _is_multi_quantity(problem.answer):
        result = GradeResult(
            correct=False, verdict="khong-cham-duoc", method="none",
            expected=problem.answer, received=student,
            detail=(
                "Đáp án gồm nhiều ý bằng lời nên hệ thống không tự chấm được; "
                "cần người chấm đối chiếu từng phần."
            ),
        )
    elif problem.type == "dien-so" or problem.answer_numeric is not None:
        result = _grade_numeric(problem, student)
    elif problem.type == "tu-luan":
        result = _grade_symbolic(problem, student)
    else:
        result = _grade_text(problem, student)

    if not result.correct:
        result.weak_skills = list(problem.skills)
        result.hints = list(problem.hints)
    return result


def grade(conn: sqlite3.Connection, request: GradeRequest) -> GradeResult:
    """Chấm một câu, kèm gợi ý học tiếp khi sai."""
    if request.problem_id:
        problem = _load_problem(conn, request.problem_id)
    else:
        if request.expected_answer is None and request.expected_numeric is None:
            raise ValueError(
                "Chấm bài ngoài kho thì phải cung cấp expected_answer hoặc expected_numeric."
            )
        problem = Problem(
            id="adhoc",
            subject="",
            level="",
            type=request.problem_type or "dien-so",
            answer=request.expected_answer or "",
            answer_numeric=request.expected_numeric,
            tolerance=request.tolerance,
        )

    result = grade_problem(problem, request.student_answer)
    if request.tolerance is not None and result.method == "numeric" and not result.correct:
        problem.tolerance = request.tolerance
        result = grade_problem(problem, request.student_answer)

    if not result.correct:
        result.next_steps = _next_steps(conn, problem) if request.problem_id else []

    if request.problem_id:
        conn.execute(
            "INSERT INTO attempts (learner, problem_id, answer, correct, verdict)"
            " VALUES (?,?,?,?,?)",
            (request.learner, problem.id, request.student_answer,
             int(result.correct), result.verdict),
        )
        conn.commit()
        # Cập nhật luôn lịch ôn giãn cách. Ghi tiến độ mà không dùng tới thì
        # đúng bằng không ghi — đây là chỗ khép vòng lặp học.
        if problem.skills:
            progress.record_practice(
                conn,
                problem.skills,
                correct=result.correct,
                score=result.score,
                learner=request.learner,
            )
    return result


def _next_steps(conn: sqlite3.Connection, problem: Problem, limit: int = 5) -> list[Hit]:
    """Bài giảng dạy công thức vừa dùng, cộng bài luyện cùng kỹ năng nhưng dễ hơn."""
    steps: list[Hit] = []
    if problem.formulas_used:
        steps.extend(lessons_for_formulas(conn, problem.formulas_used, limit=2))
    if problem.skills:
        steps.extend(
            problems_by_skill(
                conn,
                problem.skills,
                limit=4,
                exclude=[problem.id],
                difficulty_max=max(1, (problem.difficulty or 3) - 1),
            )
        )
    seen: set[str] = set()
    unique: list[Hit] = []
    for hit in steps:
        if hit.id not in seen:
            seen.add(hit.id)
            unique.append(hit)
    return unique[:limit]


# --------------------------------------------------------------------------- #
# Chẩn đoán trên cả một loạt câu
# --------------------------------------------------------------------------- #


def diagnose(conn: sqlite3.Connection, request: DiagnosisRequest) -> DiagnosisResult:
    """Chấm cả loạt rồi chỉ ra kỹ năng nào đang yếu và nên học lại phần nào.

    Kỹ năng bị coi là yếu khi làm sai quá nửa số câu chạm tới nó — dùng tỉ lệ
    chứ không dùng số câu sai tuyệt đối, để một kỹ năng xuất hiện ở mười câu
    không tự động bị xếp yếu hơn kỹ năng chỉ xuất hiện ở một câu.
    """
    records = load_records(conn, "problem", list(request.answers.keys()))
    missing = [pid for pid in request.answers if pid not in records]

    per_problem: list[GradeResult] = []
    attempted: Counter = Counter()
    correct_by_skill: Counter = Counter()
    wrong_topics: Counter = Counter()
    wrong_formulas: list[str] = []
    solved_ids: list[str] = []
    # Gộp theo khoá chuẩn để "đổi đơn vị" và "doi-don-vi" không bị đếm thành hai
    # kỹ năng riêng; giữ lại các cách viết để chọn bản dễ đọc khi hiển thị.
    surface_forms: dict[str, list[str]] = {}

    for problem_id, answer in request.answers.items():
        record = records.get(problem_id)
        if record is None:
            continue
        problem = Problem.model_validate(record)
        result = grade_problem(problem, answer)
        per_problem.append(result)
        solved_ids.append(problem_id)

        for skill in problem.skills:
            key = skills.canonical(skill) or fold(skill)
            surface_forms.setdefault(key, []).append(skill)
            attempted[key] += 1
            if result.correct:
                correct_by_skill[key] += 1
        if not result.correct:
            if problem.topic:
                wrong_topics[problem.topic] += 1
            wrong_formulas.extend(problem.formulas_used)

    total = len(per_problem)
    correct = sum(1 for r in per_problem if r.correct)

    weak = [
        SkillStat(
            skill=skills.display_name(surface_forms[key]),
            attempted=count,
            correct=correct_by_skill[key],
        )
        for key, count in attempted.items()
        if correct_by_skill[key] / count < 0.5
    ]
    weak.sort(key=lambda s: (s.accuracy, -s.attempted))

    result = DiagnosisResult(
        total=total,
        correct=correct,
        accuracy=round(correct / total, 4) if total else 0.0,
        per_problem=per_problem,
        weak_skills=weak[: request.max_recommendations],
        weak_topics=[topic for topic, _ in wrong_topics.most_common(5)],
    )

    if wrong_formulas:
        result.recommended_lessons = lessons_for_formulas(
            conn, list(dict.fromkeys(wrong_formulas)), limit=5
        )
    if weak:
        result.recommended_problems = problems_by_skill(
            conn,
            [s.skill for s in weak[:6]],
            limit=request.max_recommendations,
            exclude=solved_ids,
        )

    result.summary = _summarize(result, missing)
    return result


def _summarize(result: DiagnosisResult, missing: list[str]) -> str:
    if result.total == 0:
        return "Không chấm được câu nào: các id gửi lên không có trong kho."
    lines = [
        f"Đúng {result.correct}/{result.total} câu ({result.accuracy:.0%})."
    ]
    if result.weak_skills:
        names = ", ".join(f"{s.skill} ({s.correct}/{s.attempted})" for s in result.weak_skills[:4])
        lines.append(f"Kỹ năng cần củng cố: {names}.")
    else:
        lines.append("Không có kỹ năng nào rơi xuống dưới mức một nửa.")
    if result.weak_topics:
        lines.append("Chủ đề sai nhiều nhất: " + ", ".join(result.weak_topics[:3]) + ".")
    if result.recommended_lessons:
        lines.append(f"Gợi ý {len(result.recommended_lessons)} bài giảng để học lại.")
    if missing:
        lines.append(f"Bỏ qua {len(missing)} id không có trong kho: {', '.join(missing[:3])}.")
    return " ".join(lines)


def skill_report(conn: sqlite3.Connection, learner: str = "local") -> dict[str, Any]:
    """Tổng hợp lịch sử làm bài đã ghi trong bảng `attempts`."""
    rows = conn.execute(
        "SELECT a.problem_id, a.correct FROM attempts a WHERE a.learner = ?", (learner,)
    ).fetchall()
    if not rows:
        return {"learner": learner, "attempts": 0, "skills": []}

    by_skill: dict[str, list[int]] = defaultdict(list)
    surface_forms: dict[str, list[str]] = defaultdict(list)
    problem_ids = list({row["problem_id"] for row in rows})
    placeholders = ",".join("?" * len(problem_ids))
    skill_rows = conn.execute(
        "SELECT problem_id, skill, skill_key FROM problem_skills"
        f" WHERE problem_id IN ({placeholders})",
        problem_ids,
    ).fetchall()
    skills_of: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for row in skill_rows:
        key = row["skill_key"] or fold(row["skill"])
        skills_of[row["problem_id"]].append((key, row["skill"]))
        surface_forms[key].append(row["skill"])

    for row in rows:
        for key, _ in skills_of.get(row["problem_id"], []):
            by_skill[key].append(row["correct"])

    summary = [
        {
            "skill": skills.display_name(surface_forms[key]),
            "attempted": len(results),
            "correct": sum(results),
            "accuracy": round(sum(results) / len(results), 3),
        }
        for key, results in by_skill.items()
    ]
    summary.sort(key=lambda s: (s["accuracy"], -s["attempted"]))
    return {"learner": learner, "attempts": len(rows), "skills": summary}
