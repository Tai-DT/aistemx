"""Chấm bài và chẩn đoán."""

from __future__ import annotations

import sqlite3

from aistem.grading import diagnose, grade, grade_problem
from aistem.models import DiagnosisRequest, GradeRequest, Problem


def _numeric_problem(**overrides) -> Problem:
    base = {
        "id": "test.numeric", "subject": "physics", "level": "thpt", "type": "dien-so",
        "answer": "9,8 m/s^2", "answer_numeric": 9.8, "answer_unit": "m/s^2",
        "tolerance": 0.01, "skills": ["đổi đơn vị"],
    }
    base.update(overrides)
    return Problem(**base)


class TestChoiceGrading:
    def test_accepts_various_phrasings(self, conn: sqlite3.Connection) -> None:
        problem = Problem(
            id="t", subject="math", level="thpt", type="trac-nghiem", answer="A",
            choices=[{"key": "A", "text": "6"}, {"key": "B", "text": "0", "why_wrong": "vì X"}],
        )
        for answer in ("A", "a", "chọn A", "đáp án là A."):
            assert grade_problem(problem, answer).correct

    def test_wrong_choice_explains_why(self, conn: sqlite3.Connection) -> None:
        problem = Problem(
            id="t", subject="math", level="thpt", type="trac-nghiem", answer="A",
            choices=[{"key": "A", "text": "6"}, {"key": "B", "text": "0", "why_wrong": "vì X"}],
        )
        result = grade_problem(problem, "B")
        assert not result.correct and result.why_wrong == "vì X"


class TestNumericGrading:
    def test_unit_conversion_counts_as_correct(self) -> None:
        assert grade_problem(_numeric_problem(), "980 cm/s^2").correct

    def test_right_number_wrong_unit_is_its_own_verdict(self) -> None:
        result = grade_problem(_numeric_problem(), "9.8 N")
        assert result.verdict == "sai-don-vi" and result.score == 0.5

    def test_near_miss_is_flagged_as_rounding(self) -> None:
        result = grade_problem(_numeric_problem(), "9.6 m/s^2")
        assert result.verdict == "gan-dung" and result.score == 0.5

    def test_clear_miss_is_wrong(self) -> None:
        assert grade_problem(_numeric_problem(), "2 m/s^2").verdict == "sai"

    def test_vietnamese_decimal_comma_accepted(self) -> None:
        assert grade_problem(_numeric_problem(), "9,8 m/s^2").correct


class TestSymbolicGrading:
    def test_any_equivalent_form_is_accepted(self) -> None:
        problem = Problem(
            id="t", subject="math", level="thpt", type="tu-luan", answer=r"\frac{x+3}{x-2}"
        )
        assert grade_problem(problem, r"\frac{x^2-9}{x^2-5x+6}").correct
        assert not grade_problem(problem, r"\frac{x+3}{x+2}").correct


class TestGradeAgainstCorpus:
    def test_grades_a_real_problem_and_suggests_next_steps(self, conn: sqlite3.Connection) -> None:
        result = grade(
            conn, GradeRequest(problem_id="prob.math.ap-calculus.0001", student_answer="B")
        )
        assert not result.correct
        assert result.why_wrong
        assert result.hints
        assert result.weak_skills
        assert result.next_steps

    def test_unknown_problem_id_raises(self, conn: sqlite3.Connection) -> None:
        import pytest

        with pytest.raises(KeyError):
            grade(conn, GradeRequest(problem_id="khong-ton-tai", student_answer="A"))

    def test_adhoc_grading_without_corpus(self, conn: sqlite3.Connection) -> None:
        result = grade(
            conn,
            GradeRequest(student_answer="3.14", expected_numeric=3.14159, tolerance=0.01),
        )
        assert result.correct


class TestDiagnosis:
    def test_reports_weak_skills_and_recommends(self, conn: sqlite3.Connection) -> None:
        result = diagnose(
            conn,
            DiagnosisRequest(
                answers={
                    "prob.math.ap-calculus.0001": "B",
                    "prob.math.ap-calculus.0006": "B",
                    "prob.math.ap-calculus.0007": "B",
                }
            ),
        )
        assert result.total == 3
        assert result.weak_skills
        assert result.recommended_lessons or result.recommended_problems
        assert "Đúng" in result.summary

    def test_unknown_ids_are_reported_not_crashed(self, conn: sqlite3.Connection) -> None:
        result = diagnose(conn, DiagnosisRequest(answers={"khong-ton-tai": "A"}))
        assert result.total == 0
        assert "không có trong kho" in result.summary


class TestSkillMatching:
    """Kho được soạn theo nhiều lát cắt độc lập nên cùng một kỹ năng có cả dạng
    chữ lẫn dạng slug. So khớp bằng chuỗi nguyên làm hai nửa kho không gợi ý
    được cho nhau: đo được 95% kỹ năng chỉ ra đúng một bài, tức tính năng luyện
    tập gần như vô dụng.
    """

    def test_slug_and_prose_spellings_are_the_same_skill(self) -> None:
        from aistem.skills import canonical

        assert canonical("phân tích đa thức thành nhân tử") == canonical(
            "phan-tich-da-thuc-thanh-nhan-tu"
        )
        assert canonical("Đổi đơn vị") == canonical("doi-don-vi")

    def test_leading_verbs_do_not_split_a_skill(self) -> None:
        from aistem.skills import canonical

        assert canonical("vận dụng công thức Nernst") == canonical("công thức Nernst")

    def test_display_prefers_the_readable_spelling(self) -> None:
        from aistem.skills import display_name

        assert display_name(["doi-don-vi", "đổi đơn vị"]) == "đổi đơn vị"

    def test_rare_tokens_outweigh_common_ones(self) -> None:
        from aistem.skills import SkillMatcher

        # "công thức" có ở khắp nơi, "Nernst" thì không.
        matcher = SkillMatcher({"cong": 900, "thuc": 900, "nernst": 4}, total=1000)
        assert matcher.similarity("công thức Nernst", "phương trình Nernst") > matcher.similarity(
            "công thức Nernst", "công thức Bernoulli"
        )

    def test_recommendation_actually_returns_problems(self, conn) -> None:
        from aistem.store import problems_by_skill

        for skill in ("đổi đơn vị", "doi-don-vi", "tính thế nước"):
            assert len(problems_by_skill(conn, [skill], limit=10)) >= 3

    def test_unrelated_skills_do_not_match(self, conn) -> None:
        from aistem.store import problems_by_skill

        hits = problems_by_skill(conn, ["quang hợp ở thực vật C4"], limit=10)
        assert all(hit.subject in {"biology", ""} for hit in hits)


class TestRealCorpusAnswers:
    """Bất biến quan trọng nhất của một bộ chấm: **nộp đúng đáp án mà kho công
    bố thì phải được chấm đúng**.

    Đo lần đầu trên toàn kho: 436/1258 bài (35%) bị chấm sai chính đáp án của
    mình — và tệ hơn là bộ chấm nói "sai" chứ không nói "không chấm được". Các
    ca dưới đây là từng nguyên nhân đã tìm ra.
    """

    def _numeric(self, answer, numeric, unit="", tolerance=0.01, ptype="dien-so"):
        return Problem(
            id="t", subject="chemistry", level="thpt", type=ptype,
            answer=answer, answer_numeric=numeric, answer_unit=unit, tolerance=tolerance,
        )

    def test_fraction_answers(self) -> None:
        assert grade_problem(self._numeric("27/64", 0.421875), "27/64").correct
        assert grade_problem(self._numeric("3/64 ≈ 0,0469", 0.046875), "3/64 ≈ 0,0469").correct

    def test_labelled_answers(self) -> None:
        """`Q10 ≈ 2,31` từng bị đọc thành 10 — con số trong tên ký hiệu."""
        assert grade_problem(self._numeric("Q10 ≈ 2,31", 2.31), "Q10 ≈ 2,31").correct
        assert grade_problem(self._numeric("d(X/H2) = 18,125", 18.125), "18,125").correct

    def test_labelled_answer_with_unit(self) -> None:
        assert grade_problem(self._numeric("a = 361 pm", 361.0, "pm"), "a = 361 pm").correct
        assert grade_problem(self._numeric("V = 300 mL", 300.0, "mL"), "300 mL").correct

    def test_unicode_superscript_scientific_notation(self) -> None:
        assert grade_problem(
            self._numeric("≈ 2,68 × 10³ bp", 2680.0, "bp"), "2,68 × 10³ bp"
        ).correct

    def test_vietnamese_dot_as_times_ten(self) -> None:
        """Sách giáo khoa Việt Nam viết `8,64.10^-3` cho 8,64 × 10⁻³."""
        assert grade_problem(
            self._numeric("k ≈ 8,64.10^-3 s^-1", 8.64e-3, "s^-1"), "8,64.10^-3 s^-1"
        ).correct

    def test_percent_is_not_a_dimensional_unit(self) -> None:
        assert grade_problem(self._numeric("≈ 34,0 %", 34.0, "%"), "34,0 %").correct
        assert grade_problem(self._numeric("2pq = 3,92 %", 3.92, "%"), "3,92%").correct

    def test_prefixed_unit_matches_base_unit_value(self) -> None:
        """`≈ 2,0 nF` đi với `answer_numeric = 2e-9` và `answer_unit = 'F'`."""
        assert grade_problem(self._numeric("≈ 2,0 nF", 2e-9, "F"), "≈ 2,0 nF").correct
        assert grade_problem(self._numeric("≈ 4,24 mm", 4.24e-3, "m"), "4,24 mm").correct

    def test_domain_units_pint_does_not_know(self) -> None:
        """`cM`, `bp` là đơn vị chuyên ngành. Không hiểu ≠ sai."""
        assert grade_problem(self._numeric("≈ 18,84 cM", 18.84, "cM"), "18,84 cM").correct

    def test_multi_quantity_answers_are_graded_per_part(self) -> None:
        """Đáp án nhiều đại lượng số chấm được từng phần, không còn bỏ qua."""
        problem = self._numeric("Vmax = 50 μmol/phút; Km = 4,0 mM", 4.0, "mM")
        result = grade_problem(problem, "Vmax = 50 μmol/phút; Km = 4,0 mM")
        assert result.correct
        assert result.method == "multi"
        assert len(result.parts) == 2

    def test_prose_answers_still_say_they_need_a_human(self) -> None:
        problem = self._numeric(
            "a) Ψ tế bào = -5,0 bar. b) Nước đi từ dung dịch (-3,0 bar) vào tế bào (-5,0 bar)",
            -5.0, "bar",
        )
        result = grade_problem(problem, "a) Ψ tế bào = -5,0 bar. b) Nước đi vào tế bào")
        assert result.verdict == "khong-cham-duoc"
        assert "cần người chấm" in result.detail

    def test_prose_units_fall_back_to_text(self) -> None:
        problem = Problem(
            id="t", subject="biology", level="thpt", type="tu-luan",
            answer="X có 4 mắt xích và 3 liên kết peptide",
            answer_unit="liên kết peptide",
        )
        result = grade_problem(problem, "X có 4 mắt xích và 3 liên kết peptide")
        assert result.correct or result.verdict == "khong-cham-duoc"

    def test_still_catches_genuinely_wrong_answers(self) -> None:
        """Nới cho đúng thì dễ nới quá tay — phải kiểm cả chiều ngược lại."""
        assert not grade_problem(self._numeric("≈ 34,0 %", 34.0, "%"), "12 %").correct
        assert not grade_problem(self._numeric("27/64", 0.421875), "1/2").correct
        assert not grade_problem(self._numeric("a = 361 pm", 361.0, "pm"), "a = 900 pm").correct
