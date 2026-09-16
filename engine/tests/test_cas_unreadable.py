"""Đòn bẩy L5 — những biểu thức CAS không đọc nổi.

Ba nhóm thay đổi, và với mỗi nhóm có cả test khẳng định hệ thống **không** kết
tội ở chỗ nó không đủ căn cứ. Đó mới là phần đắt tiền: một bộ kiểm chứng nói
"chưa biết" thì vô hại, nói "sai" nhầm thì người dùng bỏ qua mọi cảnh báo sau đó.
"""

from __future__ import annotations

import pytest

from aistem.cas.parse import to_sympy
from aistem.cas.verify import check_steps
from aistem.textnorm import clean_latex, split_equation, split_relations


def _status(latex: str, explain: str = "") -> str:
    return check_steps([{"latex": latex, "explain": explain}])[0].status


# --------------------------------------------------------------------------- #
# 1. `\text{...}` trong chỉ số dưới là TÊN ký hiệu, không phải chú thích
# --------------------------------------------------------------------------- #


def test_index_label_no_longer_kills_the_parser() -> None:
    """`U_{\\text{eff}}` phải còn lại một ký hiệu đọc được, không phải `U_{}`."""
    cleaned = clean_latex(r"U_{\text{eff}} = -mgR")
    assert "{ }" not in cleaned and "{}" not in cleaned
    assert to_sympy(r"U_{\text{eff}}") is not None


def test_index_label_is_one_atomic_symbol() -> None:
    """Nhãn phải thành MỘT ký hiệu nguyên khối, không phải tích các chữ cái.

    Parser đọc `n_{eff}` thành `n_{e*f*f}`. Tích thì có cấu trúc đại số, nên hai
    nhãn khác nghĩa mà trùng tập chữ cái sẽ so ra "khác nhau" và một bước đúng bị
    kết tội — đúng loại báo oan phải chặn từ gốc.
    """
    expr = to_sympy(r"n_{\text{cho vào}}")
    assert expr is not None
    assert len(expr.free_symbols) == 1


def test_index_labels_stay_distinct() -> None:
    """Hai nhãn khác nhau không được nhập làm một ký hiệu."""
    a = to_sympy(r"n_{\text{cho vào}}")
    b = to_sympy(r"n_{\text{dư}}")
    plain = to_sympy("n")
    assert a != b and a != plain and b != plain


def test_index_label_does_not_accuse_a_substitution_step() -> None:
    """Đọc được rồi vẫn phải im lặng: hai vế khác tập ẩn là bước thế số."""
    assert _status(r"n_{\text{đã phản ứng}} = n_{\text{cho vào}} - n_{\text{dư}}") == "inconclusive"


def test_superscript_label_left_alone() -> None:
    """Nhãn ở chỉ số TRÊN cố ý không xử lí.

    `K_M^{\\text{bk}}` là "K_M biểu kiến", không phải luỹ thừa. Mọi cách viết lại
    đều là phỏng đoán, mà nếu phỏng đoán thành `K_M` thì
    `\\frac{K_M^{bk}}{K_M} = 3` biến thành `1 = 3` — kết tội oan.
    """
    assert to_sympy(r"\frac{K_{M}^{\text{bk}}}{K_{M}} = 3") is None


def test_text_outside_an_index_is_still_dropped() -> None:
    """Bẫy cũ: `\\text` ngoài chỉ số là đơn vị/lời văn, và số mũ đi kèm phải bị nuốt."""
    assert clean_latex(r"m = 18\ \text{g/m}^3") == "m = 18"
    assert clean_latex(r"v = 5\ \text{m/s}^{2}") == "v = 5"


# --------------------------------------------------------------------------- #
# 2. Ký pháp Newton `\dot{x}`, `\ddot{x}`
# --------------------------------------------------------------------------- #


def test_newton_dot_is_readable() -> None:
    assert to_sympy(r"\ddot{\theta}") is not None
    assert to_sympy(r"\dot{x}") is not None


def test_newton_dot_is_not_the_same_symbol_as_the_variable() -> None:
    """Nhập `\\dot{x}` với `x` thì phương trình chuyển động thành đẳng thức sai hiển nhiên."""
    assert to_sympy(r"\dot{x}") != to_sympy("x")
    assert to_sympy(r"\ddot{x}") != to_sympy(r"\dot{x}")


def test_newton_dot_does_not_eat_the_ellipsis() -> None:
    """`\\dots` chứa đúng chữ `\\dot` — không chặn thì dấu chấm lửng thành ký hiệu bịa."""
    assert r"\dots" in clean_latex(r"a_1 + \dots + a_n")


# --------------------------------------------------------------------------- #
# 3. Dấu xấp xỉ
# --------------------------------------------------------------------------- #


def test_approx_is_not_parsed_as_a_free_symbol() -> None:
    """Trước đây `a \\approx b` ra `a*approx*b` — một biểu thức bịa, không lỗi nào ném ra."""
    for part in split_equation(r"0{,}50 + 1{,}645 \times 0{,}05 \approx 0{,}5822"):
        expr = to_sympy(part)
        assert expr is None or not any(
            str(s).startswith("approx") for s in expr.free_symbols
        )


def test_approx_splits_into_two_sides() -> None:
    assert split_relations(r"\frac{1}{3} \approx 0{,}33") == (
        [r"\frac{1}{3}", "0.33"],
        ["≈"],
    )
    assert split_relations(r"\frac{1}{2} \simeq 0{,}5")[1] == ["≈"]


def test_approx_link_can_still_confirm() -> None:
    assert _status(r"p = 0{,}50 + 1{,}645 \times 0{,}05 \approx 0{,}5822") == "verified"


def test_approx_link_never_accuses() -> None:
    """`\\frac{2}{3} \\approx 0{,}66` là lời giải ĐÚNG, chỉ làm tròn xuống.

    Chênh 1% vượt mọi ngưỡng làm tròn của bộ so số, nên nếu mắt xích xấp xỉ được
    quyền kết tội thì đây là một bản án oan.
    """
    assert _status(r"\frac{2}{3} \approx 0{,}66") == "inconclusive"
    assert _status(r"\pi \approx 3{,}1") == "inconclusive"


def test_equals_link_still_accuses() -> None:
    """Nới cho dấu xấp xỉ không được làm mềm dấu bằng."""
    assert _status("1 + 2 = 4") == "refuted"
    assert _status(r"\frac{1}{2} + \frac{1}{3} = \frac{2}{5}") == "refuted"


def test_approx_does_not_soften_a_neighbouring_equals() -> None:
    """Trong `a = b \\approx c`, mắt xích `a = b` vẫn giữ nguyên sức nặng."""
    assert _status(r"2 + 2 = 5 \approx 5{,}0") == "refuted"


@pytest.mark.parametrize(
    "latex",
    [
        r"\text{cạnh tranh}: \tfrac{1}{V_{\max}}",
        r"R_{f} = \frac{\text{quãng đường chất}}{\text{quãng đường dung môi}}",
        r"\left.\frac{dy}{dx}\right|_{(3;3)}",
        r"[\mathrm{H^{+}}]^{2} = K_{a}C",
    ],
)
def test_still_silent_where_there_is_no_ground(latex: str) -> None:
    """Những dạng L5 cố tình KHÔNG đụng tới vẫn phải là "chưa kết luận", không phải "sai"."""
    assert _status(latex) != "refuted"
