"""Đòn bẩy L4 — nguyên tử mờ cho áp dụng hàm, và theo dõi định nghĩa hàm.

Bộ test này chia làm hai nửa, và nửa thứ hai mới là nửa quan trọng:

* nửa đầu kiểm rằng những khâu **thuần số** nằm chung dòng với một lời gọi hàm
  không còn bị vứt oan;
* nửa sau kiểm rằng hệ thống **không kết tội** ở những chỗ nó không đủ căn cứ —
  hàm cho theo từng khoảng, hàm đệ quy, ký pháp thay cận, và cả chỗ mơ hồ giữa
  "áp dụng hàm" với "phép nhân".
"""

from __future__ import annotations

import pytest

from aistem.cas import check_steps, verify_answer
from aistem.cas.funcalls import FunctionScope


def statuses(steps: list[dict]) -> list[str]:
    return [c.status for c in check_steps(steps)]


class TestNguyenTuMo:
    """`P(X = 4)`, `f(1)`, `\\operatorname{Var}(X)` thành nguyên tử giữ chỗ."""

    def test_khau_thuan_so_van_kiem_duoc(self) -> None:
        """Trước đây cả bước bị vứt chỉ vì có `P(X = 4)` ở vế đầu."""
        checks = check_steps(
            [{"explain": "tính giá trị",
              "latex": r"P(X = 4) = 0{,}343 \times 0{,}3 = 0{,}1029"}]
        )
        assert checks[0].status == "verified"

    def test_phuong_sai_qua_operatorname(self) -> None:
        checks = check_steps(
            [{"explain": "công thức phương sai",
              "latex": r"\operatorname{Var}(X) = E(X^{2}) - (E(X))^{2}"
                       r" = 3{,}7 - 1{,}7^{2} = 3{,}7 - 2{,}89 = 0{,}81"}]
        )
        assert checks[0].status == "verified"

    def test_cung_loi_goi_ra_cung_nguyen_tu(self) -> None:
        """`P(X=4)` và `P(X = 4)` là một; `P(X=4)` và `P(X=5)` là hai."""
        scope = FunctionScope()
        first = scope.rewrite(r"P(X=4)")
        again = scope.rewrite(r"P(X = 4)")
        other = scope.rewrite(r"P(X=5)")
        assert first == again
        assert first != other

    def test_khong_xac_nhan_bua_hai_xac_suat_khac_nhau(self) -> None:
        """Bẫy cũ: parser rụng mất đối số nên `P(X > 68)` và `P(Z > 1,481)`
        cùng thành ký hiệu `P`, rồi CAS reo lên "trùng khớp về cấu trúc"."""
        checks = check_steps(
            [{"explain": "chuẩn hoá",
              "latex": r"P(X > 68) = P(Z > 1{,}481)"}]
        )
        assert checks[0].status == "inconclusive"

    def test_ten_danh_rieng_cua_sympy_khong_thanh_so(self) -> None:
        """`N(2)`, `S(40)` là số hạt và diện tích, không phải hàm dựng sẵn."""
        assert check_steps([{"latex": r"N(2) = 162{,}5 + 85 + 12{,}5 = 260"}])[0].status == (
            "verified"
        )
        assert check_steps(
            [{"latex": r"S(40) = 1600 + \frac{128000}{40} = 1600 + 3200 = 4800"}]
        )[0].status == "verified"

    def test_loi_so_hoc_that_van_bi_bat(self) -> None:
        """Nới cho đúng dễ nới quá tay: khâu thuần số sai vẫn phải bị bác bỏ."""
        checks = check_steps([{"latex": r"f(1) = 1 - 6 + 9 + 1 = 7"}])
        assert checks[0].status == "refuted"


class TestKhongKetToiKhiMoHo:
    """Những chỗ hệ thống phải trả "chưa kết luận" thay vì đoán."""

    def test_nhan_that_trong_vat_li_khong_bi_ket_toi(self) -> None:
        """`x(t+1)` có thể là phép nhân thật — không đủ căn cứ nói gì cả."""
        checks = check_steps([{"latex": r"x(t+1) = xt + x"}])
        assert checks[0].status != "refuted"

    def test_loi_goi_ham_khong_bao_gio_tham_gia_ket_toi(self) -> None:
        """Vế còn nguyên tử mờ thì mọi phán quyết phải dừng ở "chưa kết luận"."""
        checks = check_steps([{"latex": r"P(X = 4) = 0{,}5"},
                              {"latex": r"P(X = 4) = 0{,}9"}])
        assert "refuted" not in [c.status for c in checks]

    def test_ky_phap_thay_can_khong_ket_toi(self) -> None:
        """`\\left. t^{2} \\right|_{0}^{1}` bị parser nuốt sạch phần sau dấu gạch
        và trả về đúng số `1`. So với nó là kết tội một lời giải đúng."""
        checks = check_steps(
            [{"latex": r"x(1) = 1 + \int_{0}^{1} 2t\,dt"
                       r" = 1 + \left.t^{2}\right|_{0}^{1} = 1 + 1 = 2"}]
        )
        assert checks[0].status == "verified"  # khâu `1 + 1 = 2` vẫn kiểm được
        assert checks[0].status != "refuted"

    def test_gia_tri_tuyet_doi_khong_bi_nham_la_ky_phap_thay_can(self) -> None:
        """`|z_1|^2` parser đọc đúng thành `Abs(z_1)**2`, đừng vứt nó đi."""
        checks = check_steps([{"latex": r"|z_1|^2 = 2^2 + 3^2 = 13"}])
        assert checks[0].status == "verified"


class TestTheoDoiDinhNghiaHam:
    def test_dinh_nghia_roi_thay_so(self) -> None:
        checks = check_steps([{"latex": r"D(x) = x^{2} + \left(x^{2} - 3\right)^{2}"},
                              {"latex": r"D(0) = 9"}])
        assert checks[1].status == "verified"

    def test_dao_ham_la_mot_cai_ten_khac(self) -> None:
        """`f'(x) = 3x^2 - 2` KHÔNG định nghĩa `f`. Lẫn hai cái là kết tội oan
        mọi bước tính `f` ở sau."""
        checks = check_steps([{"latex": r"f'(x) = 3x^{2} - 2"},
                              {"latex": r"f'(2) = 10"},
                              {"latex": r"f(2) = 5"}])
        assert checks[1].status == "verified"
        assert checks[2].status != "refuted"

    def test_ham_cho_theo_tung_khoang_bi_bo_han(self) -> None:
        """Một tên, hai công thức: không cách nào biết bước đang xét thuộc nhánh
        nào, nên cấm thế số hẳn."""
        checks = check_steps([{"latex": r"f(x) = 3x - 1"},
                              {"latex": r"f(x) = x^{2}"},
                              {"latex": r"f(2) = 4"}])
        assert checks[2].status == "inconclusive"

    def test_ham_de_quy_khong_duoc_thu(self) -> None:
        """`f(f(n)) = 3n` là phương trình hàm, không phải định nghĩa."""
        checks = check_steps([{"latex": r"f(f(n)) = 3n"},
                              {"latex": r"f(1) = 2"},
                              {"latex": r"f(2) = 3"}])
        assert "refuted" not in [c.status for c in checks]

    def test_ham_phu_thuoc_ham_khac_khong_duoc_thu(self) -> None:
        """`f(t) = u(t-2)(t-2)`: `u` là hàm bậc thang chưa biết."""
        checks = check_steps([{"latex": r"f(t) = u(t - 2)(t - 2)"},
                              {"latex": r"f(5) = 1 \cdot (5 - 2) = 3"}])
        assert checks[1].status == "verified"  # nhờ khâu `1 \cdot (5-2) = 3`
        assert checks[0].status != "refuted"

    def test_bien_co_khong_phai_bien_so(self) -> None:
        """`P(A) = 0,5` trông y hệt một định nghĩa hàm hằng. Nhận nhầm thì
        `P(B) = 0,5` được "xác nhận" trong khi chẳng có căn cứ nào."""
        checks = check_steps([{"latex": r"P(A) = 0{,}5"},
                              {"latex": r"P(B) = 0{,}5"}])
        assert checks[1].status == "inconclusive"

    def test_the_dinh_nghia_khong_bao_gio_ket_toi(self) -> None:
        """Định nghĩa có thể chỉ đúng trên một miền. Xác nhận thì được, kết tội
        thì không đủ tư cách."""
        checks = check_steps([{"latex": r"f(x) = x^{2} + 1"},
                              {"latex": r"f(5) = 30"}])
        assert checks[1].status == "inconclusive"

    def test_tham_so_chua_biet_thi_khong_phai_dinh_nghia(self) -> None:
        checks = check_steps([{"latex": r"P(t) = \frac{L}{1 + Ae^{-kt}}"},
                              {"latex": r"P(0) = 500"}])
        assert checks[1].status != "refuted"


class TestDapSoVanChatTay:
    def test_khong_ket_toi_dap_so_chi_vi_doc_them_duoc_buoc(self) -> None:
        """Kiểm thêm được bước không được phép biến thành kết tội đáp số."""
        result = verify_answer(
            answer="0,1029", answer_numeric=0.1029,
            steps=[{"explain": "hình học", "latex": r"P(X = 4) = (1-p)^{3}p"},
                   {"explain": "tính", "latex": r"P(X = 4) = 0{,}343 \times 0{,}3 = 0{,}1029"}],
        )
        assert result.answer_status == "verified"
        assert result.steps_refuted == 0

    def test_bai_ham_de_quy_khong_bi_ket_toi(self) -> None:
        result = verify_answer(
            answer="3888", answer_numeric=3888,
            steps=[
                {"latex": r"f(1)=2,\qquad f(2)=f\left(f(1)\right)=3\cdot 1=3"},
                {"latex": r"3^{6}=729,\qquad 2\cdot 3^{6}=1458,\qquad 3^{7}=2187"},
                {"latex": r"f(2025)=3\left(2025-729\right)=3\cdot 1296=3888"},
            ],
        )
        assert result.steps_refuted == 0
        assert result.answer_status == "verified"


class TestNganSachThoiGian:
    def test_khong_lam_cham_them(self) -> None:
        """Nguyên tử mờ không ép được về số; vòng thay số phải bỏ cuộc ngay chứ
        không quay đủ 24 lượt cho mỗi khâu."""
        import time

        steps = [{"latex": rf"P(X = {i}) = {i} + 1 = {i + 1}"} for i in range(12)]
        started = time.perf_counter()
        result = verify_answer(answer="12", steps=steps, budget=20.0)
        assert time.perf_counter() - started < 10
        assert result.steps_refuted == 0


@pytest.mark.parametrize(
    "latex",
    [
        r"\sin(2x) = 2\sin x\cos x",
        r"\min(3) = 3",
        r"\Phi(1{,}5) = 0{,}9332",
    ],
)
def test_ham_dung_san_khong_bi_nham_la_ap_dung_ham(latex: str) -> None:
    """Chỉ chữ cái ĐỨNG RIÊNG mới được coi là tên hàm: `\\sin`, `\\min`, `\\Phi`
    là lệnh LaTeX, cắt lấy chữ cái cuối của chúng là đọc bậy."""
    scope = FunctionScope()
    assert "\\Xi" not in scope.rewrite(latex)
