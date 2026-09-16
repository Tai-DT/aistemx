"""Những lỗ hổng do vòng phản biện tìm ra, sau khi tám đòn bẩy đã gộp.

Cả tám đòn bẩy đều tự đo trên lát cắt kho của riêng mình và đều báo "0 bước bị
bác bỏ mới". Vòng phản biện không đo lại độ phủ — nó **dựng đầu vào hiểm** rồi
hỏi ngược: chỗ nào hệ thống nói "đã kiểm" mà thật ra chưa kiểm gì? Gần như mọi
thứ nó tìm được đều thuộc loại ấy, chứ không phải báo oan.

Lí do các phép đo bỏ sót: mỗi lát cắt chỉ thấy phần kho mà đòn bẩy của nó chạm
tới, còn lỗi thì nằm ở **chỗ hai đòn bẩy gặp nhau** — hàng rào của cái này bịt
miệng kết luận của cái kia, và kho không có sẵn ca nào bày ra chuyện đó.
"""

from __future__ import annotations

import pytest

from aistem.cas import check_steps, verify_answer
from aistem.cas.chemistry import check_molar_mass, parse_formula
from aistem.cas.dimensions import check_dimension
from aistem.cas.funcalls import FunctionScope


def _status(latex: str) -> str:
    return check_steps([{"latex": latex}])[0].status


class TestMauThuanBiBitMiengKhongThanhXacNhan:
    """Một mắt xích lệch nhau mà bị hàng rào hạ xuống "chưa kết luận" thì cả
    bước phải dừng ở "chưa kết luận" — không được để mắt xích khác đóng dấu."""

    def test_dong_vua_co_mau_thuan_vua_co_khau_dung(self) -> None:
        # Vế `\text{m}`/`\text{mm}` khiến khâu đầu bị bịt miệng; khâu sau đúng.
        # Trước khi vá, cả bước hiện ra là "verified".
        latex = r"y = 3\ \text{m} = 7\ \text{mm} \quad ; \quad z = 2 + 2 = 4"
        assert _status(latex) != "verified"

    def test_quy_doi_don_vi_dung_van_duoc_xac_nhan(self) -> None:
        # Ngược lại: hàng rào GIẢI THÍCH được mâu thuẫn thành phép đổi đơn vị
        # khớp thì không còn gì treo lại, bước vẫn được xác nhận.
        assert _status(r"6\cdot 10^{-3}\ \text{m} = 6\ \text{mm}") == "verified"


class TestBatDangThucKhongDuocKhangDinhBua:
    def test_hai_so_sat_nhau_thi_khong_ket_luan_chieu(self) -> None:
        # `4 \ge 4{,}4` sai, nhưng dung sai suy từ chữ số viết ra của `4` là ±0,5
        # nên nó từng được "xác nhận" là đúng.
        assert _status(r"4 \ge 4{,}4") != "verified"

    def test_hai_so_phan_biet_duoc_thi_van_kiem_duoc(self) -> None:
        # Lệch 27% thì rõ ràng phân biệt được, dù `10^{-6}` chỉ viết một chữ số.
        assert _status(r"7{,}28 \times 10^{-7} \le 10^{-6}") == "verified"


class TestHoaHocKhongDoanMachCaMatXich:
    def test_phep_tinh_sai_ben_canh_phuong_trinh_van_bi_bat(self) -> None:
        latex = (
            r"2\mathrm{H_2} + \mathrm{O_2} \rightarrow 2\mathrm{H_2O}"
            r" :\ n = 5 \times 3 = 16"
        )
        assert _status(latex) == "refuted"

    def test_chu_thich_khong_co_phep_tinh_thi_khong_can_tro(self) -> None:
        latex = (
            r"\mathrm{Na} + \mathrm{H_2O} \to \mathrm{NaOH}"
            r" + \tfrac{1}{2}\mathrm{H_2}:\ n_{\mathrm{NaOH}} = 0{,}2"
        )
        assert _status(latex) == "verified"

    def test_muoi_ngam_nuoc_khong_bi_noi_lien_chi_so(self) -> None:
        # `CuSO_4 \cdot 5H_2O` từng bị xoá khoảng trắng thành `CuSO_45H_2O`,
        # và chỉ số đọc ra là 45.
        assert parse_formula(r"CuSO_4 \cdot 5H_2O") is None

    @pytest.mark.parametrize(
        "latex",
        [r"M_{C} = 12", r"M = 5{,}0", r"M_{\text{ròng rọc}} = 3{,}5"],
    )
    def test_khong_tra_bang_nguyen_tu_khoi_cho_ky_hieu_khong_phai_hoa_hoc(
        self, latex: str
    ) -> None:
        assert check_molar_mass(latex)[0] == "unknown"

    def test_ten_chat_that_thi_van_kiem_duoc(self) -> None:
        assert check_molar_mass(r"M_{\mathrm{H_2SO_4}} = 98")[0] == "balanced"


class TestHamChoTheoTungKhoang:
    def test_mot_nhanh_khong_duoc_dung_thay_ca_ham(self) -> None:
        steps = [
            {"latex": r"f(x) = \begin{cases} 3x-1 & x<0 \\ x^2 & x\ge 0\end{cases}"},
            {"latex": r"f(x) = 3x - 1"},
            {"latex": r"f(2) = 5"},
        ]
        assert [c.status for c in check_steps(steps)][-1] != "verified"

    def test_ham_mot_cong_thuc_van_the_duoc(self) -> None:
        steps = [{"latex": r"f(x) = x^{2}+1"}, {"latex": r"f(5) = 26"}]
        assert [c.status for c in check_steps(steps)][-1] == "verified"

    def test_dinh_nghia_khong_dung_duoc_thi_dau_doc_ten(self) -> None:
        scope = FunctionScope()
        scope.learn(r"f(x) = \begin{cases} 3x-1 & x<0 \\ x^2 & x\ge 0\end{cases}")
        scope.learn(r"f(x) = 3x - 1")
        assert "f" not in scope._definitions


class TestThuNguyenKhongXacNhanKhong:
    def test_khong_doc_duoc_don_vi_thi_khong_duoc_noi_la_so_thuan(self) -> None:
        answer = "Gamma ≈ 1,91e12 s^-1, tương ứng tau ≈ 5,24e-13 s"
        assert check_dimension(answer, "%")[0] == "unknown"

    def test_dap_an_so_thuan_that_thi_van_khop(self) -> None:
        assert check_dimension("0,75", "%")[0] == "consistent"


class TestBangXepHangKhongPhaiGoc:
    def test_bac_carbocation_khong_duoc_quy_sang_radian(self) -> None:
        # `3^{\circ} > 2^{\circ} > 1^{\circ}` là bậc carbocation trong Hoá hữu
        # cơ. Quy sang radian rồi "xác nhận" thứ tự là xác nhận một thứ tự
        # chính mình vừa bịa ra.
        assert _status(r"3^{\circ} > 2^{\circ} > 1^{\circ}") != "verified"

    def test_goc_that_van_kiem_duoc(self) -> None:
        assert _status(r"\theta = 180^{\circ} + 53{,}1^{\circ} = 233^{\circ}") == "verified"


class TestNoiThatVeDapSo:
    def test_khong_nhan_la_tinh_lai_khi_chi_doc_lai_con_so(self) -> None:
        """Vế sau dấu `≈` thường là con số người viết gõ sẵn, không phải kết quả
        CAS tính ra. Khớp với nó vẫn có giá trị — nó bắt được đáp án lệch với
        chính các bước — nhưng phải nói đúng là đã kiểm được cái gì."""
        result = verify_answer(
            answer="0,58", answer_numeric=0.58, steps=[{"latex": r"p \approx 0{,}58"}]
        )
        assert result.answer_status == "verified"
        assert "lời giải viết ra" in (result.answer_detail or "")

    def test_van_nhan_la_tinh_lai_khi_that_su_co_tinh(self) -> None:
        result = verify_answer(
            answer="0,5489",
            answer_numeric=0.5489,
            steps=[{"latex": r"SE = \frac{1{,}9014}{\sqrt{12}} \approx 0{,}54889"}],
        )
        assert result.answer_status == "verified"
        assert "CAS tính lại được" in (result.answer_detail or "")
