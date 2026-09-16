"""Đòn bẩy L2 — tách chuỗi theo `≈` và kiểm bất đẳng thức.

Một nửa số test ở đây khẳng định hệ thống **xác nhận thêm được**; nửa còn lại
khẳng định nó **vẫn im lặng** ở đúng những chỗ nó không đủ căn cứ. Nửa sau mới
là nửa quan trọng: mỗi trường hợp trong đó là một lời giải đúng thật trong kho
mà cách tách chuỗi mới suýt kết tội.

Chạy:
    PYTHONPATH=<thư-mục-này> pytest test_lever.py -q
"""

from __future__ import annotations

import pytest

from aistem.cas.verify import check_steps
from aistem.textnorm import split_relations, starts_with_relation


def _status(latex: str, explain: str = "") -> tuple[str, str]:
    check = check_steps([{"latex": latex, "explain": explain}])[0]
    return check.status, check.detail or ""


class TestSplitRelations:
    def test_keeps_each_relation_with_its_own_link(self) -> None:
        """`a ≤ b ≈ c < d` là bốn vế nối bằng ba quan hệ khác nhau."""
        parts, ops = split_relations(r"\left|R\right| \le \frac{1}{1320} \approx 0.00076 < 0.001")
        assert parts == ["|R|", r"\frac{1}{1320}", "0.00076", "0.001"]
        assert ops == ["<=", "≈", "<"]

    @pytest.mark.parametrize(
        ("latex", "ops"),
        [
            (r"a \leq b", ["<="]),
            (r"a \leqslant b", ["<="]),
            (r"a \geq b", [">="]),
            (r"a \ne b", ["!="]),
            (r"a \gg b", ["≫"]),
            (r"a \simeq b", ["≈"]),
        ],
    )
    def test_reads_every_spelling_of_a_relation(self, latex: str, ops: list[str]) -> None:
        assert split_relations(latex)[1] == ops

    def test_left_is_not_read_as_le(self) -> None:
        """`\\left(` mở đầu bằng đúng hai chữ của `\\le` — tách theo nó thì hỏng cả dòng."""
        parts, ops = split_relations(r"\left( x + 1 \right) = 3")
        assert ops == ["="]
        assert parts[0].strip() == "( x + 1 )"

    def test_relations_inside_brackets_are_left_alone(self) -> None:
        """`P(T_{16} > 3{,}451)` là một đối số, không phải một mắt xích."""
        parts, ops = split_relations(r"p = 2P(T_{16} > 3{,}451) \approx 0{,}0033 < 0{,}05")
        assert ops == ["=", "≈", "<"]
        assert "T_{16} > 3.451" in parts[1]

    def test_leading_relation_keeps_its_empty_slot(self) -> None:
        """Bước nối tiếp phải giữ chỗ trống để nơi gọi biết mà nối vào bước trước."""
        assert split_relations(r"= \frac{x+3}{x-2}") == (["", r"\frac{x+3}{x-2}"], ["="])

    def test_starts_with_relation_reads_the_raw_string(self) -> None:
        assert starts_with_relation(r"\approx 4{,}39")
        assert not starts_with_relation(r"\text{can duoi} = 29")


class TestApproxChain:
    def test_confirms_a_rounded_value(self) -> None:
        status, detail = _status(r"t = \frac{2{,}4083 - 0}{0{,}54889} \approx 4{,}388")
        assert status == "verified"
        assert "4.388" in detail

    def test_confirms_through_pi(self) -> None:
        assert _status(r"S = \pi r^{2} = 4\pi \approx 12.5664")[0] == "verified"

    def test_approximation_that_drops_a_term_is_not_convicted(self) -> None:
        """`≈` cho phép bỏ số hạng: hai vế lệch nhau ở đó là cố ý."""
        status, _ = _status(r"\frac{2pq}{q^{2}} \approx \frac{2}{q}")
        assert status != "refuted"

    def test_distribution_approximation_is_not_convicted(self) -> None:
        status, _ = _status(r"\bar{X}_n \approx \mathcal{N}(\mu, \sigma^{2}/n)")
        assert status != "refuted"

    def test_a_wrong_approximation_is_reported_as_unknown_not_refuted(self) -> None:
        """Kết tội theo `≈` là vô nghĩa — lệch bao nhiêu thì gọi là sai?"""
        status, detail = _status(r"\frac{1}{2} \approx 0{,}9")
        assert status != "refuted"
        assert "không đủ căn cứ kết tội" in detail


class TestInequalityChain:
    @pytest.mark.parametrize(
        "latex",
        [
            r"n = 12 < 30",
            r"72 > 69{,}5",
            r"\left|R_{2}-R_{1}\right| = 5 < d = 12 < R_{1}+R_{2} = 15",
            r"p = 0{,}140 < d_{JC} = 0{,}1550 < d_{K2P} = 0{,}1581",
            r"\frac{e}{180 \cdot 12^{4}} \approx 7{,}28 \times 10^{-7} \le 10^{-6}",
        ],
    )
    def test_confirms_a_true_numeric_inequality(self, latex: str) -> None:
        assert _status(latex)[0] == "verified"

    def test_a_false_inequality_is_never_convicted(self) -> None:
        """Kho có bước liệt kê phản ví dụ: `n=2: 4>4 (sai)` là lời giải ĐÚNG."""
        status, detail = _status(r"4 > 9")
        assert status != "refuted"
        assert "không kết tội" in detail

    def test_a_bound_being_proved_is_not_convicted(self) -> None:
        status, _ = _status(r"\left|R_{3}\right| \le \frac{2(0.5)^{4}}{24}")
        assert status != "refuted"

    def test_two_numbers_too_close_give_no_direction(self) -> None:
        """0,1550 với 0,15501: chiều của `<` nằm dưới mức làm tròn của lời giải."""
        status, detail = _status(r"0{,}15500 < 0{,}15501")
        assert status != "verified"
        assert "sát nhau quá" in detail

    def test_symbolic_sides_stay_silent(self) -> None:
        assert _status(r"T_{\max}^{\text{doc}} < T_{\max}^{\text{hieu chinh}}")[0] != "verified"


class TestNoNewFalseAccusations:
    """Bốn lời giải ĐÚNG trong kho mà bản đầu của đòn bẩy này đã kết tội oan."""

    @pytest.mark.parametrize(
        "latex",
        [
            # quy đổi đơn vị: 5,5e-4 m và 0,55 mm là cùng một độ dài
            r"y = 5{,}5\times10^{-4}\ \text{m} = 0{,}55\ \text{mm}"
            r" < \frac{d}{2} = 6{,}0\ \text{mm}",
            r"h = \dfrac{2\cdot 0.073}{1000\cdot 9.8\cdot 2.0\times 10^{-4}}"
            r" \approx 0.0745\ \text{m} = 7.5\ \text{cm}",
            r"\Delta\nu \approx 2{,}80\times 10^{10}\ \text{Hz} = 28{,}0\ \text{GHz}",
        ],
    )
    def test_unit_conversion_is_not_an_arithmetic_error(self, latex: str) -> None:
        assert _status(latex)[0] != "refuted"

    def test_pi_read_as_a_free_symbol_never_convicts(self) -> None:
        """π/sin(π/3) = 2π/√3 là đẳng thức đúng; sai chỗ là ở cách đọc `\\pi`."""
        status, detail = _status(
            r"I\left(\dfrac{1}{3}\right) = \dfrac{\pi}{\sin\left(\pi/3\right)}"
            r" = \dfrac{2\pi}{\sqrt{3}} \approx 3.628"
        )
        assert status == "verified"
        assert "π" in detail

    def test_pi_as_a_statistical_proportion_is_not_convicted(self) -> None:
        """Trong Thống kê `\\pi` là tỉ lệ tổng thể — đọc thành 3,14 rồi kết tội là oan."""
        assert _status(r"\pi = 0{,}40")[0] != "refuted"

    def test_a_stripped_label_is_not_joined_to_the_previous_step(self) -> None:
        """`\\text{cận dưới} = 16+5+8` KHÔNG phải bước nối tiếp của `AB = 8`."""
        steps = [
            {"latex": r"AB = 8", "explain": ""},
            {"latex": r"\text{can duoi} = 16 + 5 + 8 = 29", "explain": ""},
        ]
        checks = check_steps(steps)
        assert checks[1].status == "verified"
        assert "8 ≠ 29" not in (checks[1].detail or "")

    def test_text_removed_from_the_middle_does_not_fabricate_a_comparison(self) -> None:
        """`V'(t) > 0 \\text{ khi } t < 4` còn lại `0 t` — không phải con số 0."""
        status, _ = _status(r"V'(t) > 0 \text{ khi } t < 4")
        assert status != "verified"


class TestStillCatchesRealErrors:
    """Các hàng rào mới không được làm hỏng việc bắt lỗi số học thật."""

    @pytest.mark.parametrize(
        "latex",
        [
            r"x = 2 + 2 = 5",
            r"E = \frac{U}{d} = \frac{12}{0{,}012} = 900",
            r"(a+b)^{2} = a^{2} + b^{2}",
        ],
    )
    def test_arithmetic_and_algebra_errors_are_still_refuted(self, latex: str) -> None:
        assert _status(latex)[0] == "refuted"

    def test_one_unit_on_the_line_still_allows_conviction(self) -> None:
        assert _status(r"E = \frac{12}{0{,}012} = 900\ \text{V/m}")[0] == "refuted"
