"""Cổng an toàn của bộ đọc, và bốn cơ chế báo oan tìm được khi soi lại kho.

Cả bốn đều là **lỗi im lặng**: hệ thống không ném lỗi nào, nó chỉ bình thản kết
luận sai. Ba trong bốn được tìm ra bằng cách đọc tay từng bước mà `aistem audit`
báo là "bị bác bỏ" rồi hỏi ngược lại: kho sai thật, hay ta báo oan? Cả bốn lần
đều là ta báo oan.
"""

from __future__ import annotations

import sympy as sp

from aistem.cas import check_steps, equivalent, to_sympy
from aistem.cas.verify import _cancellation_floor, _constant_value, _sample_compare
from aistem.textnorm import clean_latex


class TestCongAnToan:
    """Parser nhận một tiền tố hợp lệ rồi vứt phần đuôi, không ném lỗi nào."""

    def test_ngoac_rong_khong_duoc_nuot_mat_ve_sau(self) -> None:
        # `4 ( ) + 1` từng trả về đúng `4`, và bước `4 + 1 = 5` của kho bị bác bỏ.
        # `doit()` vì parser trả `Add(1, 4)` chưa rút gọn.
        assert to_sympy(r"4 ( ) + 1").doit() == 5

    def test_toan_tu_cut_thi_tra_none(self) -> None:
        # `1 + 2 + \text{ghi chú}` gọt xong còn `1 + 2 +`, parser lặng lẽ trả 3.
        assert to_sympy(r"1 + 2 + \text{ghi chu}") is None

    def test_hai_so_dinh_nhau_la_nhap_nhang(self) -> None:
        # `5 \quad 7` là hai mệnh đề rời; ghép lại thành 57 là bịa.
        assert to_sympy(r"5 \quad 7") is None

    def test_phan_nhom_hang_nghin_van_doc_duoc(self) -> None:
        # Nhưng `12\,000` thì đúng là mười hai nghìn, không được chặn nhầm.
        assert to_sympy(r"12\,000") == 12000
        assert to_sympy(r"1\,234\,567") == 1234567

    def test_lenh_latex_khong_hieu_thi_khong_bia_thanh_ky_hieu(self) -> None:
        assert to_sympy(r"2 + 3 \mathrm{C{=}O}") is None
        assert to_sympy(r"2x + 3 \mathbb{Z}") is None
        assert to_sympy(r"7 + \unknowncmd 9") is None

    def test_chu_cai_hy_lap_van_la_ky_hieu_hop_le(self) -> None:
        assert to_sympy(r"3 \alpha") is not None
        assert to_sympy(r"2 \pi") is not None
        assert to_sympy(r"\sin^2 x + \cos^2 x") is not None

    def test_chu_thich_trong_ngoac_bi_go_chu_khong_lam_hong_phep_tinh(self) -> None:
        # `4 (vòng thơm) + 1 (nhóm C=O) = 5` — hai ngoặc là nhãn, không phải nhân.
        assert clean_latex(r"4\ (\text{vòng thơm}) + 1\ (\text{nhóm CO})") == "4 + 1"


class TestLeibniz:
    """`dh/dt` phải giữ nghĩa "chưa biết", không được rút về 0."""

    def test_dao_ham_leibniz_khong_rut_ve_khong(self) -> None:
        expr = to_sympy(r"\frac{dh}{dt}")
        assert expr is not None and expr.doit() != 0

    def test_buoc_that_trong_kho_khong_con_bi_bac_bo(self) -> None:
        # prob.math.ap-calculus.0016 bước 5 — trước đây bị bác bỏ "-2 ≠ 0".
        latex = r"-2 = \frac{\pi (4)^{2}}{4}\cdot\frac{dh}{dt} = 4\pi\frac{dh}{dt}"
        check = check_steps([{"latex": latex}])[0]
        assert check.status != "refuted"

    def test_dao_ham_that_van_tinh_duoc(self) -> None:
        expr = to_sympy(r"\frac{d}{dx}\left(x^2\right)")
        assert expr is not None and expr.doit() == 2 * sp.Symbol("x")


class TestThangDo:
    """Ngưỡng "coi như bằng nhau" phải theo độ lớn của chính đại lượng."""

    def test_dai_luong_rat_nho_khong_bi_coi_la_hang_so(self) -> None:
        # `e·4,20·10⁻¹⁵` với `e` là điện tích nguyên tố: một ẩn thật, không phải hằng.
        assert _constant_value(sp.Symbol("e") * sp.Float("4.2e-15")) is None

    def test_hai_dai_luong_vi_mo_lech_nhau_thi_phai_thay_la_khac(self) -> None:
        x = sp.Symbol("x")
        assert _sample_compare(x * sp.Float("1e-20"), x * sp.Float("9e-20")) == "different"
        assert _sample_compare(x * sp.Float("6.626e-34"), x * sp.Float("3.0e-34")) == "different"

    def test_hai_dai_luong_vi_mo_bang_nhau_van_duoc_xac_nhan(self) -> None:
        x = sp.Symbol("x")
        assert _sample_compare(x * sp.Float("6.626e-34"), x * sp.Float("6.626e-34")) == "equivalent"

    def test_nhieu_con_lai_sau_phep_tru_van_duoc_coi_la_khong(self) -> None:
        x = sp.Symbol("x")
        zero = sp.expand((x + 1) ** 2) - x**2 - 2 * x - 1
        assert _sample_compare(zero, sp.Integer(0)) == "equivalent"

    def test_nguong_khong_suy_tu_do_lon_cac_so_hang(self) -> None:
        x = sp.Symbol("x")
        assert _cancellation_floor(x + sp.Integer(1), {x: sp.Float(2.0)}) > 0


class TestDoiDonVi:
    """Hai vế viết ở hai đơn vị khác nhau là phép đổi đơn vị, không phải lỗi."""

    def test_doi_don_vi_dung_thi_duoc_xac_nhan(self) -> None:
        for latex in (
            r"6\cdot 10^{-3}\ \text{m} = 6\ \text{mm}",
            r"a = 250\ \mu\mathrm{m} = 2{,}50\times 10^{-2}\ \mathrm{cm}",
            r"\Delta G = -2{,}192\times 10^{5}\ \mathrm{J/mol} = -219{,}2\ \mathrm{kJ/mol}",
            r"m = 5\ \mathrm{kg} = 5000\ \mathrm{g}",
        ):
            assert check_steps([{"latex": latex}])[0].status == "verified", latex

    def test_doi_don_vi_sai_thi_khong_ket_toi_ma_noi_chua_ket_luan(self) -> None:
        # Bất đối xứng: chưa đủ căn cứ để chắc đây là lỗi số học chứ không phải
        # một đơn vị chuyên ngành mà Pint hiểu nhầm.
        checks = check_steps([{"latex": r"x = 3\ \mathrm{m} = 7\ \mathrm{mm}"}])
        assert checks[0].status != "refuted"

    def test_don_vi_pint_khong_biet_thi_khong_ket_toi(self) -> None:
        assert check_steps(
            [{"latex": r"CO = 5400\ \mathrm{mL/phut} = 5{,}4\ \mathrm{L/phut}"}]
        )[0].status != "refuted"


class TestKhongNoiLongHangRaoCu:
    """Những chỗ vốn phải bị bác bỏ thì vẫn phải bị bác bỏ."""

    def test_loi_so_hoc_that_van_bi_bat(self) -> None:
        assert equivalent(to_sympy("2 + 2"), to_sympy("5"))[0] == "different"
        assert check_steps([{"latex": r"3 \times 4 = 11"}])[0].status == "refuted"

    def test_bien_doi_dai_so_sai_van_bi_bat(self) -> None:
        assert equivalent(to_sympy(r"(a+b)^2"), to_sympy("a^2 + b^2"))[0] == "different"
