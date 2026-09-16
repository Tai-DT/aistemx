"""Test cho đòn bẩy L6 — kiểm thứ nguyên ba trạng thái.

Phần lớn test ở đây khẳng định hệ thống **không kết tội**. Đó là chủ ý: một bộ
kiểm đơn vị dễ viết cho có, và cái giá của nó không nằm ở chỗ bỏ sót mà ở chỗ
nói sai với người trả lời đúng. Nhóm cuối (`TestVanConBatDuocLoi`) giữ chiều
ngược lại để việc nới tay không âm thầm biến bộ kiểm thành đồ trang trí.
"""

from __future__ import annotations

import pytest

from aistem.cas import check_dimension, verify_answer
from aistem.cas.units import check_unit


class TestKhongDuThongTinThiKhongKetToi:
    """Thiếu dữ kiện phải ra "unknown" — đây là mặc định, không phải ngoại lệ."""

    def test_khoa_trac_nghiem_khong_phai_don_vi(self) -> None:
        """`A` là phương án trả lời, không phải ampe.

        Cùng một cái bẫy chữ-cái-bị-chiếm-chỗ với `F = ma` ở tầng SymPy: Pint
        đọc `A` thành ampe, `B` thành bel, `C` thành coulomb. Đây là nhóm báo
        oan lớn nhất đo được trên kho (16 bài).
        """
        for key in ("A", "B", "C", "D", "E"):
            status, _ = check_dimension(key, "%")
            assert status == "unknown"
        assert check_dimension("A", "m/s^2")[0] == "unknown"

    def test_don_vi_chuyen_nganh_pint_khong_biet(self) -> None:
        """`cM`, `bp`, `nat`, `cá thể` — không hiểu thì nói chưa kiểm được."""
        for unit in ("cM", "bp", "nat", "cá thể", "liên kết peptit", "nucleotide"):
            status, detail = check_dimension(f"12 {unit}", unit)
            assert status != "inconsistent", f"{unit!r} bị kết tội oan: {detail}"

    def test_dap_an_nhieu_dai_luong(self) -> None:
        """Kho khai một `answer_unit` cho cả cụm — không biết nó nói về cái nào."""
        status, _ = check_dimension("E_K ≈ -89,0 mV; E_Na ≈ +60,6 mV", "mV")
        assert status == "unknown"

    def test_nhieu_dai_luong_noi_bang_loi_van(self) -> None:
        """`Gamma ≈ ... s^-1, tương ứng tau ≈ ... s` — hai đại lượng, hai thứ nguyên.

        Không có dấu `;` nào để bám vào. Lấy bừa mẩu cuối thì đọc ra `s` trong
        khi kho khai `s⁻¹`, và một lời giải đúng bị gạch sai.
        """
        answer = "Gamma ≈ 1,91 x 10^12 s^-1, tương ứng thời gian sống tau ≈ 5,24 x 10^-13 s"
        status, detail = check_dimension(answer, "s⁻¹")
        assert status != "inconsistent", detail

    def test_dap_an_khong_kem_don_vi_la_loi_viet(self) -> None:
        """Kho ghi `answer='30'` với `answer_unit='%'`. Đó là lối viết, không phải lỗi.

        Khác hẳn `check_unit`: ở đó đang chấm bài học sinh nên "thiếu đơn vị" là
        nhận xét chính đáng, và test cũ giữ đúng hành vi ấy.
        """
        assert check_dimension("-0,8", "MPa")[0] == "unknown"
        assert check_unit("12", "m/s^2")[0] is False  # đường chấm bài: giữ nguyên

    def test_don_vi_kho_khong_mang_thu_nguyen(self) -> None:
        """`%` với một đáp án có đơn vị thật là cách ghi nhãn của kho, không phải lỗi."""
        status, _ = check_dimension("≈ -219 kJ/mol", "%")
        assert status == "unknown"


class TestVanXacNhanRongTay:
    """Xác nhận thì rộng tay — nới chống báo oan không được làm mất xác nhận đúng."""

    def test_khac_boi_so_van_hop_le(self) -> None:
        assert check_dimension("980 cm/s^2", "m/s^2")[0] == "consistent"

    def test_don_vi_tieng_viet(self) -> None:
        """Kho viết `L/phút`, `năm`; Pint chỉ biết tên tiếng Anh."""
        assert check_dimension("5,4 L/phút", "L/phút")[0] == "consistent"
        assert check_dimension("≈ 9,93 năm", "năm")[0] == "consistent"

    def test_mu_unicode(self) -> None:
        assert check_dimension("45 μmol·phút⁻¹", "μmol·phút⁻¹")[0] == "consistent"

    def test_ky_phap_khoa_hoc_chu_x_ascii(self) -> None:
        """`2.9 x 10^-3 mol/L` — chữ `x` thường, không phải `\\times`.

        Bộ tách đơn vị chung không nuốt dạng này, nên phần `x 10^-3` dính vào
        chuỗi đơn vị và một đáp án đúng bị báo sai. Đây là 1 trong 2 ca đang
        thực sự bị kết tội trên đường chạy thật trước khi sửa.
        """
        assert check_dimension("2.9 x 10^-3 mol/L", "mol/L")[0] == "consistent"

    def test_chuoi_quy_doi_don_vi(self) -> None:
        """`Wq = 0,4 giờ = 24 phút` là một chuỗi quy đổi, các mẩu cùng thứ nguyên.

        Cắt theo dấu `=` đầu tiên thì còn `giờ = 24 phút`, Pint nhân hai đơn vị
        với nhau ra thời gian **bậc hai** rồi báo sai một đáp án hoàn toàn đúng.
        """
        assert check_dimension("Wq = 0,4 giờ = 24 phút", "phút")[0] == "consistent"

    def test_so_thuan_voi_dai_luong_khong_thu_nguyen(self) -> None:
        assert check_dimension("70,4 %", "%")[0] == "consistent"


class TestVanConBatDuocLoi:
    """Chiều ngược lại: nới tay rồi thì còn bắt được lỗi thứ nguyên thật không?

    Đo trên kho: bẻ đơn vị của 187 đáp án vốn xác nhận được thì bắt 97,9%.
    """

    @pytest.mark.parametrize(
        ("answer", "unit"),
        [
            ("9,8 N", "m/s^2"),      # lực nhận nhầm thành gia tốc
            ("5,0 J", "W"),          # công nhận nhầm thành công suất
            ("3,0 m", "s"),          # quãng đường nhận nhầm thành thời gian
            ("2,0 kg", "N"),         # khối lượng nhận nhầm thành lực
        ],
    )
    def test_sai_thu_nguyen_that_thi_phai_bat(self, answer: str, unit: str) -> None:
        status, detail = check_dimension(answer, unit)
        assert status == "inconsistent", f"lọt lưới: {answer!r} vs {unit!r} -> {detail}"


class TestNoiVaoVerification:
    """Nối vào `Verification` phải tương thích ngược."""

    def test_khong_khai_don_vi_thi_khong_dung_toi(self) -> None:
        result = verify_answer(answer="6", steps=[{"latex": "2 + 4 = 6"}])
        assert result.unit_status == "unchecked"

    def test_unknown_hien_ra_thanh_unchecked(self) -> None:
        """Model chỉ có ba giá trị; `unknown` phải quy về `unchecked`."""
        result = verify_answer(
            answer="A", answer_numeric=51.1,
            steps=[{"explain": "tổng phần trăm", "latex": "100 = 100"}],
            expected_unit="%",
        )
        assert result.unit_status == "unchecked"
        assert result.answer_status != "refuted"
