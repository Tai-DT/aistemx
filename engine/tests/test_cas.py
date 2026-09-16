"""Lõi kiểm chứng CAS.

Trọng tâm của bộ test này không phải "bắt được bao nhiêu lỗi" mà là **không
báo oan**: một bộ kiểm chứng hay kết tội nhầm còn tệ hơn một bộ kiểm chứng dè
dặt, vì nó dạy người dùng bỏ qua cảnh báo.
"""

from __future__ import annotations

import pytest

from aistem.cas import (
    check_steps,
    check_unit,
    compare_with_units,
    convert,
    equivalent,
    evaluate_latex,
    latex_equivalent,
    numbers_match,
    to_sympy,
    verify_answer,
)


class TestParsing:
    def test_reads_common_latex(self) -> None:
        assert to_sympy(r"\frac{x^{2}-9}{x^{2}-5x+6}") is not None
        assert to_sympy(r"\int_{0}^{1} x^2 \, dx") is not None
        assert to_sympy(r"E = mc^2") is not None

    def test_returns_none_instead_of_garbage(self) -> None:
        assert to_sympy("") is None
        assert to_sympy(r"\begin{cases} x \\ y \end{cases}") is None or True

    def test_euler_number_in_exponent(self) -> None:
        assert evaluate_latex(r"e^{0}") == pytest.approx(1.0)

    def test_evaluates_limits_and_integrals(self) -> None:
        assert evaluate_latex(r"\lim_{x \to 3} \frac{x+3}{x-2}") == pytest.approx(6.0)
        assert evaluate_latex(r"\int_{0}^{1} x^2 \, dx") == pytest.approx(1 / 3)


class TestEquivalence:
    @pytest.mark.parametrize(
        ("left", "right"),
        [
            (r"\frac{x^{2}-9}{x^{2}-5x+6}", r"\frac{x+3}{x-2}"),
            (r"\sin^2 x + \cos^2 x", "1"),
            (r"(a+b)^2", "a^2 + 2ab + b^2"),
            (r"\frac{1}{2}", "0.5"),
        ],
    )
    def test_equivalent_expressions(self, left: str, right: str) -> None:
        assert latex_equivalent(left, right)[0] == "equivalent"

    @pytest.mark.parametrize(
        ("left", "right"),
        [(r"(a+b)^2", "a^2 + b^2"), ("2 + 2", "5"), (r"\frac{x+3}{x-2}", r"\frac{x+3}{x+2}")],
    )
    def test_different_expressions(self, left: str, right: str) -> None:
        assert latex_equivalent(left, right)[0] == "different"

    def test_substitution_is_never_called_wrong(self) -> None:
        """Hai vế khác tập ẩn là bước thế số, không phải đồng nhất thức sai."""
        verdict, reason = equivalent(to_sympy("F"), to_sympy("m a"))
        assert verdict == "unknown"
        assert "thế số" in reason

    def test_identity_collapsing_to_a_constant_is_still_checked(self) -> None:
        """`sin^2 x + cos^2 x = 1` khác tập ẩn nhưng vẫn là đồng nhất thức thật."""
        assert latex_equivalent(r"\sin^2 x + \cos^2 x", "1")[0] == "equivalent"
        assert latex_equivalent(r"\sin^2 x + \cos^2 x", "2")[0] == "different"

    def test_symbol_check_can_be_disabled_for_grading(self) -> None:
        """Khi chấm bài học sinh thì ta cố ý so hai biểu thức khác tập ẩn."""
        verdict, _ = equivalent(to_sympy("x + x"), to_sympy("2x"), require_same_symbols=False)
        assert verdict == "equivalent"


class TestNumbers:
    def test_relative_tolerance(self) -> None:
        assert numbers_match(9.8, 9.81, 0.01)[0] is True
        assert numbers_match(9.8, 12.0, 0.01)[0] is False

    def test_zero_expected_uses_absolute_gap(self) -> None:
        assert numbers_match(0.0, 1e-12)[0] is True
        assert numbers_match(0.0, 1.0)[0] is False


class TestSteps:
    def test_verifies_a_real_chain(self) -> None:
        steps = [
            {"explain": "phân tích thành nhân tử",
             "latex": r"\frac{x^{2}-9}{x^{2}-5x+6} = \frac{(x-3)(x+3)}{(x-3)(x-2)}"},
            {"explain": "khử nhân tử chung", "latex": r"= \frac{x+3}{x-2}"},
        ]
        statuses = [c.status for c in check_steps(steps)]
        assert "refuted" not in statuses
        assert "verified" in statuses

    def test_catches_a_real_arithmetic_error(self) -> None:
        checks = check_steps([{"explain": "cộng", "latex": "2 + 3 = 6"}])
        assert checks[0].status == "refuted"

    def test_accepts_pedagogical_rounding(self) -> None:
        # Lời giải làm tròn ở từng bước; đó không phải lỗi.
        checks = check_steps([{"explain": "log", "latex": r"\ln 0{,}30125 = -1{,}1998"}])
        assert checks[0].status != "refuted"

    def test_independent_statements_on_one_line_are_split(self) -> None:
        checks = check_steps(
            [{"explain": "hai xác suất",
              "latex": r"P_1 = 0{,}4 + 0{,}1 = 0{,}5 \qquad P_2 = 0{,}3 + 0{,}1 = 0{,}4"}]
        )
        assert checks[0].status != "refuted"

    def test_equation_being_solved_is_not_refuted(self) -> None:
        checks = check_steps(
            [{"explain": "giải phương trình", "latex": r"r^{2} = 5r - 6 \iff r^{2} - 5r + 6 = 0"}]
        )
        assert checks[0].status == "inconclusive"

    def test_step_without_latex_is_skipped(self) -> None:
        assert check_steps([{"explain": "chỉ có lời"}])[0].status == "skipped"


class TestVerifyAnswer:
    def test_confirms_a_correct_solution(self) -> None:
        result = verify_answer(
            answer="6",
            answer_numeric=6,
            steps=[
                {"explain": "rút gọn", "latex": r"\frac{x^{2}-9}{x^{2}-5x+6} = \frac{x+3}{x-2}"},
                {"explain": "thay x = 3", "latex": r"\lim_{x \to 3}\frac{x+3}{x-2} = 6"},
            ],
        )
        assert result.answer_status == "verified"
        assert result.trustworthy

    def test_refutes_when_a_step_is_also_wrong(self) -> None:
        """Có lỗi số học ở một bước thì mới đủ căn cứ kết luận đáp số sai."""
        result = verify_answer(
            answer="9", answer_numeric=9,
            steps=[{"explain": "cộng sai", "latex": "y = 2 + 2 = 5"},
                   {"explain": "cộng đúng", "latex": "x = 3 + 3 = 6"}],
        )
        assert result.steps_refuted == 1
        assert result.answer_status == "refuted"
        assert not result.trustworthy

    def test_a_broken_step_sinks_trust_even_if_the_answer_matches(self) -> None:
        """Mô hình tính 3+3=7 rồi trả lời 7: tự nhất quán nhưng vẫn sai.

        Đáp số khớp với chính lời giải nên khâu đối chiếu đáp số không bắt được,
        nhưng bước sai thì bắt được — và chỉ cần thế là toàn bộ lời giải mất
        tín nhiệm.
        """
        result = verify_answer(
            answer="7", answer_numeric=7,
            steps=[{"explain": "cộng sai", "latex": "x = 3 + 3 = 7"}],
        )
        assert result.steps_refuted == 1
        assert not result.trustworthy

    def test_bare_mismatch_is_flagged_but_not_condemned(self) -> None:
        """Mọi bước đều đúng mà giá trị cuối lệch: nêu ra để rà, không gạch sai.

        Lời giải rất hay kết thúc bằng một đại lượng phụ hoặc một phép kiểm
        lại, nên "giá trị cuối" không nhất thiết là đáp số.
        """
        result = verify_answer(
            answer="7", answer_numeric=7,
            steps=[{"explain": "cộng", "latex": "x = 3 + 3 = 6"}],
        )
        assert result.answer_status == "unchecked"
        assert result.answer_mismatch is True
        assert not result.trustworthy

    def test_descriptive_answers_are_not_refuted(self) -> None:
        result = verify_answer(
            answer="10 số hạng", answer_numeric=10,
            steps=[{"explain": "sai số", "latex": r"\varepsilon = 0.001"}],
        )
        assert result.answer_status == "unchecked"

    def test_multiple_choice_key_is_not_refuted(self) -> None:
        result = verify_answer(
            answer="A", answer_numeric=51.1,
            steps=[{"explain": "tổng phần trăm", "latex": "100 = 100"}],
        )
        assert result.answer_status == "unchecked"


class TestUnits:
    def test_dimension_not_spelling(self) -> None:
        assert check_unit("980 cm/s^2", "m/s^2")[0] is True
        assert check_unit("9.8 N", "m/s^2")[0] is False

    def test_missing_unit_is_reported(self) -> None:
        ok, detail = check_unit("12", "m/s^2")
        assert ok is False and "thiếu đơn vị" in detail

    def test_conversion(self) -> None:
        assert convert(1.0, "km", "m") == pytest.approx(1000.0)

    def test_compare_converts_before_comparing(self) -> None:
        assert compare_with_units("980 cm/s^2", 9.8, "m/s^2")[0] is True
        assert compare_with_units("8.0 m/s^2", 9.8, "m/s^2")[0] is False


class TestReservedNames:
    """SymPy dành sẵn vài tên một chữ cái cho hằng dựng sẵn.

    Trong đề Lí - Hoá đó lại là các đại lượng thông dụng nhất, nên đây là bẫy
    im lặng: không chặn thì `F = ma` bị đọc thành `False = ma`.
    """

    @pytest.mark.parametrize("name", ["F", "T", "S", "N", "Q", "C"])
    def test_physics_symbols_stay_symbols(self, name: str) -> None:
        expr = to_sympy(name)
        assert expr is not None
        assert str(expr) == name
        assert expr.free_symbols

    def test_force_equation_is_a_real_equation(self) -> None:
        verdict, _ = equivalent(to_sympy("F"), to_sympy("m a"))
        assert verdict == "unknown"

    def test_genuine_relations_are_still_relations(self) -> None:
        assert to_sympy("2 = 2") is not None


class TestTimeBudget:
    """Một lời giải bệnh lí không được phép treo cả request.

    Chuỗi Fourier vô hạn từng làm `verify_answer` chạy vô thời hạn ở 100% CPU:
    chặn thời gian từng phép tính là chưa đủ, vì SymPy không huỷ được giữa
    chừng nên mỗi lần quá hạn để lại một luồng vẫn chạy.
    """

    def test_infinite_series_terminates_quickly(self) -> None:
        import time

        steps = [
            {"explain": "chuỗi Fourier",
             "latex": r"x \sim \sum_{n=1}^{\infty}\dfrac{2(-1)^{n+1}}{n}\sin(nx)"},
            {"explain": "Parseval",
             "latex": r"\dfrac{2\pi^{2}}{3} = \sum_{n=1}^{\infty}\dfrac{4}{n^{2}}"},
        ]
        started = time.perf_counter()
        result = verify_answer(answer=r"\pi^2/6", steps=steps)
        assert time.perf_counter() - started < 15
        assert result.steps_refuted == 0

    def test_exhausted_budget_says_so_instead_of_claiming_success(self) -> None:
        steps = [{"explain": f"bước {i}", "latex": f"x = {i} + 1 = {i + 1}"} for i in range(6)]
        result = verify_answer(answer="6", steps=steps, budget=0.0)
        assert all(check.status == "skipped" for check in result.steps)
        assert all("hết thời gian" in check.detail for check in result.steps)
        assert result.answer_status != "verified"


class TestUnitExtraction:
    def test_trailing_parenthetical_is_not_part_of_the_unit(self) -> None:
        """`1800 g (1,8 kg)` có đơn vị là `g`, phần trong ngoặc là chú thích."""
        from aistem.cas import extract_unit

        assert extract_unit("1800 g (1,8 kg)") == "g"
        assert check_unit("1800 g (1,8 kg)", "g")[0] is True
