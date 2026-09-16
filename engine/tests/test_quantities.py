"""Tách và chấm đáp án nhiều đại lượng."""

from __future__ import annotations

from aistem.grading import grade_problem
from aistem.models import Problem
from aistem.quantities import align, is_multi_numeric, parse_quantities


class TestParsing:
    def test_splits_on_semicolons(self) -> None:
        quantities = parse_quantities("Vmax = 50 μmol·phút⁻¹; Km = 4,0 mM")
        assert [q.label for q in quantities] == ["Vmax", "Km"]
        assert quantities[1].value == 4.0

    def test_value_comes_after_the_last_equals(self) -> None:
        """`quang hợp gộp = 4,0 + 2,0 = 6,0` — kết quả nằm ở cuối."""
        quantity = parse_quantities("tổng = 4,0 + 2,0 = 6,0")[0]
        assert quantity.label == "tổng"
        assert quantity.value == 6.0

    def test_trailing_parenthetical_is_dropped(self) -> None:
        assert parse_quantities("198 phút (3,3 giờ)")[0].value == 198.0

    def test_item_markers_are_stripped(self) -> None:
        quantities = parse_quantities("(a) 0,80 V; (b) 0,050 C")
        assert [q.value for q in quantities] == [0.80, 0.050]

    def test_thousands_separated_by_space(self) -> None:
        """`12 000` là mười hai nghìn, không phải 12."""
        assert parse_quantities("MSY = 12 000")[0].value == 12000.0


class TestMultiNumericDetection:
    def test_clean_quantities_qualify(self) -> None:
        assert is_multi_numeric("Vmax = 50 μmol/phút; Km = 4,0 mM")
        assert is_multi_numeric("(a) 0,80 V; (b) 0,050 C")

    def test_prose_with_numbers_does_not_qualify(self) -> None:
        """Có số không có nghĩa là chấm máy được."""
        assert not is_multi_numeric(
            "a) Ψ tế bào = -5,0 bar. b) Nước đi từ dung dịch (-3,0 bar) vào tế bào"
        )

    def test_comparisons_do_not_qualify(self) -> None:
        assert not is_multi_numeric("s_p^2 = 9,04; SE ≈ 1,227; t ≈ 2,851 với df = 22 > 2,074")

    def test_single_quantity_does_not_qualify(self) -> None:
        assert not is_multi_numeric("9,8 m/s^2")


class TestAlignment:
    def test_matches_by_label_not_position(self) -> None:
        """Trả lời không đúng thứ tự đề hỏi không phải là sai."""
        expected = parse_quantities("Vmax = 50; Km = 4,0")
        received = parse_quantities("Km = 4,0; Vmax = 50")
        for want, got in align(expected, received):
            assert got is not None and want.label == got.label


class TestGrading:
    def _problem(self, answer: str) -> Problem:
        return Problem(
            id="t", subject="biology", level="dai-hoc", type="dien-so",
            answer=answer, tolerance=0.02,
        )

    def test_all_parts_right(self) -> None:
        problem = self._problem("Vmax = 50 μmol·phút⁻¹; Km = 4,0 mM")
        result = grade_problem(problem, "Vmax = 50 μmol·phút⁻¹; Km = 4,0 mM")
        assert result.correct and result.score == 1.0
        assert len(result.parts) == 2

    def test_order_does_not_matter(self) -> None:
        problem = self._problem("Vmax = 50 μmol·phút⁻¹; Km = 4,0 mM")
        assert grade_problem(problem, "Km = 4,0 mM; Vmax = 50 μmol·phút⁻¹").correct

    def test_partial_credit_names_the_wrong_part(self) -> None:
        problem = self._problem("Vmax = 50 μmol·phút⁻¹; Km = 4,0 mM")
        result = grade_problem(problem, "Vmax = 50 μmol·phút⁻¹; Km = 9,0 mM")
        assert result.verdict == "dung-mot-phan"
        assert result.score == 0.5
        assert "Km" in result.detail
        assert [p.correct for p in result.parts] == [True, False]

    def test_missing_part_is_reported(self) -> None:
        problem = self._problem("Vmax = 50; Km = 4,0")
        result = grade_problem(problem, "Vmax = 50")
        assert result.verdict == "dung-mot-phan"
        assert any("thiếu" in p.detail for p in result.parts)

    def test_everything_wrong_is_wrong(self) -> None:
        problem = self._problem("Vmax = 50; Km = 4,0")
        result = grade_problem(problem, "Vmax = 12; Km = 3")
        assert result.verdict == "sai" and result.score == 0.0
