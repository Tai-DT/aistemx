"""Đòn bẩy L3 — mở tầm parser cho ký pháp độ và ký hiệu có mũ trang trí.

Bộ test này chia làm hai nửa, và nửa sau mới là nửa quan trọng:

* nửa **dịch đúng** — `\\cos 60^{\\circ}` phải ra 0,5 chứ không phải cos(60 rad);
* nửa **không kết tội bừa** — mọi biến thể nhập nhằng của `^\\circ` (độ Celsius,
  trạng thái chuẩn trong Hoá, phép hợp hàm) phải tiếp tục trả "chưa kết luận".

Nới một danh sách chặn là việc dễ gây báo oan nhất, nên mỗi ký pháp được mở ra
đều phải kèm một test khẳng định hàng rào tương ứng vẫn đứng.
"""

from __future__ import annotations

import pytest

from aistem.cas import check_steps, evaluate_latex, latex_equivalent, to_sympy
from aistem.textnorm import clean_latex, normalise_degrees


def _status(latex: str, explain: str = "") -> str:
    return check_steps([{"latex": latex, "explain": explain}])[0].status


# --------------------------------------------------------------------------- #
# Ký pháp độ — dịch đúng
# --------------------------------------------------------------------------- #


class TestDegreesTranslate:
    @pytest.mark.parametrize(
        ("latex", "value"),
        [
            (r"\cos 60^{\circ}", 0.5),
            (r"\sin 30^{\circ}", 0.5),
            (r"\cos 30^{\circ}", 0.8660254),
            (r"\tan 45^{\circ}", 1.0),
            (r"\cos^{2}30^{\circ}", 0.75),
            (r"180^{\circ} - 60^{\circ}", 2.0943951),  # 120° tính bằng radian
            (r"14{,}48^{\circ}", 0.2527),               # dấu phẩy thập phân Việt Nam
        ],
    )
    def test_degree_becomes_radian(self, latex: str, value: float) -> None:
        assert evaluate_latex(latex) == pytest.approx(value, rel=1e-4)

    def test_degree_step_is_verified(self) -> None:
        """`25\\cos 30^{\\circ} = 21{,}65` là số học đúng và phải kiểm được."""
        assert _status(r"v_{0x} = 25\cos 30^{\circ} = 21{,}65") == "verified"

    def test_arcsin_returns_radian_matching_degree_answer(self) -> None:
        """Vế trái ra radian, vế phải ghi bằng độ — quy đổi rồi mới so được."""
        assert _status(r"\theta = \arcsin 0{,}25 = 14{,}48^{\circ}") == "verified"

    def test_degree_arithmetic_chain(self) -> None:
        assert _status(r"\alpha = 90^{\circ} - 30^{\circ} = 60^{\circ}") == "verified"

    def test_wrong_degree_arithmetic_is_refuted(self) -> None:
        """Mở tầm parser mà không bắt được lỗi thật thì mở làm gì."""
        assert _status(r"\alpha = 90^{\circ} - 30^{\circ} = 70^{\circ}") == "refuted"

    def test_ignoring_degrees_would_have_been_silently_wrong(self) -> None:
        """Vì sao phải quy đổi: bỏ mũ tròn thì cos(30) là 30 radian, lệch 5 lần."""
        assert evaluate_latex(r"\cos 30") == pytest.approx(0.15425, rel=1e-3)
        assert evaluate_latex(r"\cos 30^{\circ}") == pytest.approx(0.86603, rel=1e-3)


# --------------------------------------------------------------------------- #
# Ký pháp độ — các biến thể nhập nhằng phải vẫn "chưa kết luận"
# --------------------------------------------------------------------------- #


class TestDegreesStayBlocked:
    @pytest.mark.parametrize(
        "latex",
        [
            r"t = 294 - 273 = 21^{\circ}\text{C}",
            r"T_{2} - T_{1} = 33 - 18 = 15\ ^{\circ}C",
            r"t = 42{,}5\ ^\circ\text{C}",
            r"T_{m} = 60{,}0 - 6{,}2 = 53{,}8\ ^{\circ}\mathrm{C}",
        ],
    )
    def test_celsius_is_not_an_angle(self, latex: str) -> None:
        """`21^{\\circ}C` là nhiệt độ; quy sang radian thì sai nghĩa hoàn toàn."""
        assert normalise_degrees(latex) == latex
        assert _status(latex) != "refuted"

    @pytest.mark.parametrize(
        "latex",
        [
            r"\Delta H_{f}^{\circ} = -393{,}5 - 285{,}8",
            r"\Delta G^{\circ} = \Delta H^{\circ} - T\Delta S^{\circ}",
            r"E^\circ_{pin} = 0{,}34 - (-0{,}76) = 1{,}10",
            r"K^{\circ} = 4{,}43",
        ],
    )
    def test_standard_state_is_not_an_angle(self, latex: str) -> None:
        """Mũ tròn dán vào TÊN đại lượng là trạng thái chuẩn trong Hoá."""
        assert normalise_degrees(latex) == latex
        assert _status(latex) != "refuted"

    def test_function_composition_stays_unsupported(self) -> None:
        """`f \\circ g` là phép hợp hàm, không phải phép nhân."""
        assert normalise_degrees(r"(f \circ g)(x) = f(g(x))") == r"(f \circ g)(x) = f(g(x))"
        assert _status(r"h = f \circ g") != "refuted"

    def test_subscript_digit_before_circ_is_not_an_angle(self) -> None:
        """`H_2^{\\circ}` — chữ số ấy là chỉ số dưới, không phải số đo góc."""
        assert normalise_degrees(r"\Delta H_2^{\circ} = 0") == r"\Delta H_2^{\circ} = 0"

    def test_carbocation_degree_class_is_not_refuted(self) -> None:
        """`3^{\\circ} > 2^{\\circ}` là bậc carbocation — không đủ căn cứ kết tội."""
        assert _status(r"\text{độ bền carbocation}: 3^{\circ} > 2^{\circ} > 1^{\circ}") != "refuted"


# --------------------------------------------------------------------------- #
# Ký hiệu có mũ trang trí: `\bar{x}` KHÔNG được nhập làm một với `x`
# --------------------------------------------------------------------------- #


class TestDecorationsStayDistinct:
    @pytest.mark.parametrize(
        ("decorated", "plain"),
        [(r"\bar{x}", "x"), (r"\hat{p}", "p"), (r"\tilde{\nu}", r"\nu"), (r"\overline{B}", "B")],
    )
    def test_decorated_symbol_differs_from_bare_symbol(
        self, decorated: str, plain: str
    ) -> None:
        left, right = to_sympy(decorated), to_sympy(plain)
        assert left is not None and right is not None
        assert left != right, f"{decorated} bị đọc thành cùng ký hiệu với {plain}"

    def test_sample_mean_does_not_collapse_the_z_score(self) -> None:
        """`z = (x - \\bar{x})/s` từng bị đọc thành `z = (x - x)/s`, tức `z = 0`."""
        expr = to_sympy(r"\frac{x - \bar{x}}{s}")
        assert expr is not None
        assert expr != 0, "hiệu x - \\bar{x} bị triệt tiêu thành 0"
        assert len(expr.free_symbols) == 3, "x và \\bar{x} phải là hai ẩn khác nhau"

    def test_rank_identity_is_no_longer_a_self_made_tautology(self) -> None:
        """Bẫy tệ nhất: `rank A = rank \\bar{A}` từng thành `rank A = rank A`
        rồi được XÁC NHẬN — một lời xác nhận rỗng nội dung."""
        latex = r"\operatorname{rank} A = \operatorname{rank} \bar{A} = 1"
        assert _status(latex) != "verified"

    def test_subscript_after_decoration_is_absorbed(self) -> None:
        """`\\bar{p}_{1}` phải khác cả `p_{1}` lẫn `\\bar{p}`."""
        assert clean_latex(r"\bar{p}_{1}") == "p_{bar1}"
        assert to_sympy(r"\bar{p}_{1}") != to_sympy(r"p_{1}")
        assert to_sympy(r"\bar{p}_{1}") != to_sympy(r"\bar{p}")

    def test_vector_arrow_still_unwraps(self) -> None:
        """`\\vec{v}` vẫn là chính đại lượng ấy — không đổi tên, tránh mất xác nhận."""
        assert clean_latex(r"\vec{v} = 3") == "v = 3"


# --------------------------------------------------------------------------- #
# Hệ số nhị thức
# --------------------------------------------------------------------------- #


class TestBinomial:
    def test_binomial_is_read_exactly(self) -> None:
        assert evaluate_latex(r"\binom{8}{4}") == pytest.approx(70.0)

    def test_binomial_step_is_verified(self) -> None:
        assert _status(r"\binom{8}{4} = 70") == "verified"

    def test_wrong_binomial_is_refuted(self) -> None:
        assert _status(r"\binom{8}{4} = 71") == "refuted"

    def test_symbolic_binomial_identity(self) -> None:
        assert latex_equivalent(r"\binom{n}{k}", r"\binom{n}{n-k}")[0] != "different"


# --------------------------------------------------------------------------- #
# Hai hàng rào phải dựng thêm khi mở danh sách chặn
#
# Mở `^\circ` ra đồng nghĩa với việc đẩy hàng trăm bước mới vào bộ so sánh, nên
# hai lỗi vốn đang **nấp sau** danh sách chặn lập tức lộ ra. Cả hai đều từng bác
# bỏ một lời giải đúng.
# --------------------------------------------------------------------------- #


class TestMisparseRail:
    def test_differential_d_does_not_swallow_the_cosine(self) -> None:
        """`F d\\cos 0^{\\circ}`: antlr coi `d` là dấu vi phân nên gộp `d\\cos`
        thành ẩn `dcos`, đối số rơi ra thành thừa số, cả tích thành 0."""
        assert to_sympy(r"F d\cos (0.0)") is None
        assert to_sympy(r"F d\cos 0") is None

    def test_work_formula_is_not_refuted(self) -> None:
        """Bước thật trong kho: `W = F d\\cos 0^{\\circ} = 15 × 4,0 = 60 J` đúng."""
        assert _status(r"W_{F} = F d\cos 0^{\circ} = 15 \times 4{,}0 = 60\ \text{J}") != "refuted"

    def test_ordinary_products_with_functions_still_parse(self) -> None:
        """Hàng rào không được bắt oan: chỉ `d` mới gây ra chuyện này."""
        assert to_sympy(r"a b\sin (0.5)") is not None
        assert to_sympy(r"x y\tan (0.5)") is not None

    def test_symbol_named_like_a_function_is_left_alone(self) -> None:
        """Không có `\\exp` trong nguồn thì ẩn tên `N_{exp}` chỉ là một cái tên."""
        assert to_sympy(r"N_{exp} + 1") is not None

    @pytest.mark.parametrize(
        "latex",
        [
            r"\sum_{k=0}^{6} \frac{(-1)^{k}}{k!} = \frac{265}{720}",
            r"B = \frac{\mu_{0}I}{4\pi R}\int_{0}^{\phi}d\phi' = \frac{\mu_{0}I\phi}{4\pi R}",
            r"\int_{0}^{1} x^2 \, dx = \frac{1}{3}",
        ],
    )
    def test_integrals_and_sums_survive_the_tuple_rail(self, latex: str) -> None:
        """`Integral`/`Sum` lưu cận bằng `Tuple`, nên rào "có Tuple là hỏng" quét
        cả cây sẽ giết sạch 285 bước tích phân và tổng của kho mà không bắt thêm
        lỗi nào. Rào phải soi đúng chỗ `Tuple` làm số hạng của phép toán."""
        assert _status(latex) == "verified"


class TestRoundedNumbersNeverFallThrough:
    def test_rounded_numbers_do_not_reach_the_1e_8_comparison(self) -> None:
        """`180° + 53,1° = 233°` lệch 0,04% — đúng chuẩn sư phạm.

        Khi `to_number` hết giờ (máy bận), luồng cũ rơi xuống `_sample_compare`
        vốn so ở ngưỡng 1e-8 và kết tội. Một lời bác bỏ chỉ hiện ra lúc quá tải
        là thứ không ai gỡ lại được, nên phải chặn hẳn.
        """
        import aistem.cas.verify as verify_module

        a = to_sympy("(3.141592653589793)+(0.9267698328089891)")
        b = to_sympy("(4.066617157146788)")
        assert verify_module.equivalent(a, b)[0] == "equivalent"

        original = verify_module.to_number
        verify_module.to_number = lambda expr: None
        try:
            assert verify_module.equivalent(a, b)[0] == "unknown"
        finally:
            verify_module.to_number = original

    def test_real_arithmetic_error_is_still_caught(self) -> None:
        """Nới ngưỡng cho làm tròn không được che lỗi số học thật."""
        assert _status(r"\theta = 180^{\circ} + 53{,}1^{\circ} = 200^{\circ}") == "refuted"


class TestDegreeDroppedMidChain:
    def test_chain_that_drops_the_degree_sign_is_not_refuted(self) -> None:
        """Bước thật trong kho (`prob.physics.olympiad.0041`):

            θ₁ = θ₀(l₀/l₁)^{3/4} = 6,0°·4^{3/4} = 6,0·2,8284 = 16,97°

        Số học đúng tuyệt đối — tác giả tính bằng độ suốt dòng. Nhưng vế có ký
        hiệu độ thì được quy sang radian, vế số trần thì không, nên hai vế lệch
        đúng 57,29578 lần. Kết tội ở đây là báo oan.
        """
        latex = (
            r"\theta_{1}=\theta_{0}\left(\frac{l_{0}}{l_{1}}\right)^{3/4}"
            r"=6{,}0^{\circ}\cdot 4^{3/4}=6{,}0\cdot 2{,}8284=16{,}97^{\circ}"
        )
        assert _status(latex) != "refuted"

    def test_ve_ghi_do_va_ve_viet_tran_thi_khong_ket_toi(self) -> None:
        """Trộn hai cách ghi trong một mắt xích thì không so thẳng được."""
        mixed = (
            r"\theta_{1}=6{,}0^{\circ}\cdot 4^{3/4}"
            r"=6{,}0\cdot 2{,}8284=16{,}97^{\circ}"
        )
        assert _status(mixed) != "refuted"

    def test_ca_chuoi_cung_ghi_do_thi_van_kiem_duoc(self) -> None:
        assert _status(r"\theta = 180^{\circ}+53{,}1^{\circ} = 233^{\circ}") == "verified"

    @pytest.mark.parametrize(
        "latex",
        [
            r"(2R,3S) \equiv (2S,3R)",
            r"343 \equiv 43 \pmod{100}",
            r"\frac{\partial L}{\partial \phi} = 0",
            r"\mathbf{Q} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}",
        ],
    )
    def test_ky_phap_van_nam_ngoai_tam_thi_khong_ket_toi(self, latex: str) -> None:
        """`\\equiv` mang ba nghĩa (đồng dư, đồng nhất, nối ba trong Hoá) nên
        chưa phân biệt được thì chưa mở."""
        assert _status(latex) != "refuted"
