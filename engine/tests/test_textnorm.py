"""Chuẩn hoá văn bản và LaTeX."""

from __future__ import annotations

import pytest

from aistem.textnorm import (
    clean_latex,
    extract_number,
    fold,
    slugify,
    split_equation,
    strip_annotations,
    strip_diacritics,
    strip_trailing_units,
)


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("Đạo hàm", "Dao ham"),
        ("Phương trình quang hợp", "Phuong trinh quang hop"),
        ("ĐỘNG NĂNG", "DONG NANG"),
        ("nồng độ mol", "nong do mol"),
    ],
)
def test_strip_diacritics(source: str, expected: str) -> None:
    assert strip_diacritics(source) == expected


def test_fold_is_case_and_space_insensitive() -> None:
    assert fold("  Đạo   HÀM  ") == "dao ham"


def test_decimal_comma_is_a_decimal_point() -> None:
    # 31,5% số bước giải trong kho viết số thập phân kiểu `0{,}0241`.
    assert clean_latex(r"\ln 0{,}30125") == r"\ln 0.30125"
    assert clean_latex(r"4{,}01 \times 10^{-3}") == r"4.01 * 10^{-3}"


def test_bare_comma_is_left_alone() -> None:
    # Trong kho, dấu phẩy trần là chỉ số dưới chứ không phải dấu thập phân.
    assert "1/2,1" in clean_latex(r"t_{1/2,1}")


def test_clean_latex_removes_presentation_only_commands() -> None:
    assert clean_latex(r"$\vec{F} = m\vec{a}$") == "F = ma"
    assert clean_latex(r"\left( x + 1 \right)") == "( x + 1 )"
    assert clean_latex(r"\dfrac{1}{2}") == r"\frac{1}{2}"


def test_trig_argument_gets_parenthesised() -> None:
    assert clean_latex(r"2\cos 6\theta") == r"2\cos(6\theta)"


def test_strip_annotations_drops_trailing_conditions() -> None:
    assert strip_annotations(r"\frac{x+3}{x-2} (x \neq 3)") == r"\frac{x+3}{x-2}"


def test_strip_trailing_units() -> None:
    assert strip_trailing_units(r"4.01 \times 10^{-3}\ \mathrm{s^{-1}}") == r"4.01 \times 10^{-3}"


def test_split_equation_splits_only_top_level_equals() -> None:
    assert split_equation("a = b = c") == ["a", "b", "c"]
    assert split_equation(r"x \neq 3") == ["x != 3"]


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("9,8 m/s^2", 9.8),
        ("3.14", 3.14),
        (r"4,00 x 10^-3 s^-1", 4e-3),
        (r"2{,}5 \times 10^{6}", 2.5e6),
        ("không có số", None),
    ],
)
def test_extract_number(source: str, expected: float | None) -> None:
    assert extract_number(source) == expected


def test_slugify() -> None:
    assert slugify("Đạo hàm của một tích") == "dao-ham-cua-mot-tich"


def test_leading_equals_is_split_off() -> None:
    """Bước nối tiếp mở đầu bằng `=` phải tách được vế.

    Đây là lối viết phổ biến nhất trong kho, và `"" in "<>!:"` cho True nên rất
    dễ vô tình chặn mất nhánh này.
    """
    assert split_equation(r"= \frac{x+3}{x-2}") == [r"\frac{x+3}{x-2}"]


def test_comparison_operators_are_not_split() -> None:
    assert split_equation(r"x \leq 3") == [r"x \leq 3"]
    assert split_equation("a >= b") == ["a >= b"]
    assert split_equation("a == b") == ["a == b"]


def test_unit_superscript_does_not_survive_its_unit() -> None:
    """`18\\ \\text{g/m}^3` là 18 g/m³, không phải 18³.

    Bỏ `\\text{g/m}` mà để lại `^3` thì CAS đọc thành 5832 — con số bị nhân lên
    324 lần mà không có lỗi nào ném ra.
    """
    assert clean_latex(r"m = 18\ \text{g/m}^3") == "m = 18"
    assert clean_latex(r"v = 5\ \text{m/s}^{2}") == "v = 5"
