"""Trục kiểm chứng hoá học: cân bằng nguyên tử và khối lượng mol.

Module này là chỗ duy nhất trong hệ thống dám kết tội một cách tất định — một
phương trình lệch nguyên tử là sai theo định luật bảo toàn khối lượng, không có
ngữ cảnh nào cứu được. Chính vì thế **quá nửa bộ test dưới đây khẳng định hệ
thống KHÔNG kết luận gì**: rủi ro thật của nó không nằm ở phép đếm nguyên tử mà
ở chỗ nhận nhầm một bước Toán hay Sinh thành phản ứng hoá học.
"""

from __future__ import annotations

from fractions import Fraction

from aistem.cas import check_steps, verify_answer
from aistem.cas.chemistry import (
    check_equation,
    check_molar_mass,
    molar_mass,
    parse_formula,
    parse_side,
)


def _atoms(formula: str) -> dict[str, int] | None:
    parsed = parse_formula(formula)
    return dict(parsed[0]) if parsed else None


def _charge(formula: str) -> int | None:
    parsed = parse_formula(formula)
    return parsed[1] if parsed else None


class TestDocCongThuc:
    def test_cong_thuc_co_ban(self) -> None:
        assert _atoms("H_2SO_4") == {"H": 2, "S": 1, "O": 4}
        assert _atoms(r"\mathrm{NaOH}") == {"Na": 1, "O": 1, "H": 1}

    def test_ngoac_long_va_he_so_nhom(self) -> None:
        assert _atoms("Ca(OH)_2") == {"Ca": 1, "O": 2, "H": 2}
        assert _atoms("Fe_2(SO_4)_3") == {"Fe": 2, "S": 3, "O": 12}
        assert _atoms("K_3[Fe(CN)_6]") == {"K": 3, "Fe": 1, "C": 6, "N": 6}

    def test_chi_so_viet_tran_va_viet_ngoac(self) -> None:
        # Kho dùng cả `H_2O`, `H_{2}O` lẫn `H2O`; ba lối phải cho cùng kết quả.
        assert _atoms("H_2O") == _atoms("H_{2}O") == _atoms("H2O")

    def test_ion_mang_dien_tich(self) -> None:
        assert _charge("SO_4^{2-}") == -2
        assert _charge(r"\mathrm{Fe^{3+}}") == 3
        assert _charge("OH^{-}") == -1
        assert _charge(r"[\mathrm{Ag(NH_3)_2}]^{+}") == 1

    def test_ky_hieu_hai_chu_khong_bi_xe_doi(self) -> None:
        # `Cl` phải đọc là clo, không phải cacbon rồi chữ `l` vô nghĩa.
        assert _atoms("NaCl") == {"Na": 1, "Cl": 1}
        assert _atoms("CoCl_2") == {"Co": 1, "Cl": 2}

    def test_khong_doc_duoc_thi_tra_none_chu_khong_doan(self) -> None:
        assert parse_formula("Xyzzy") is None
        assert parse_formula(r"(-CH_2-CH_2-)_n") is None   # chỉ số là ẩn
        assert parse_formula("") is None

    def test_he_so_phan_so_trong_ban_phan_ung(self) -> None:
        parsed = parse_side(r"\tfrac{1}{2}\mathrm{O_2}")
        assert parsed is not None
        assert parsed[0]["O"] == Fraction(1)


class TestKhoiLuongMol:
    def test_tinh_dung_theo_bang_iupac(self) -> None:
        assert molar_mass("H_2O") == 18.015
        assert round(molar_mass("H_2SO_4"), 1) == 98.1

    def test_nhan_ca_hai_quy_uoc_lam_tron(self) -> None:
        # Sách giáo khoa Việt Nam dùng Cu = 64, O = 16 nên M(CuO) = 80; giá trị
        # IUPAC là 79,5. Cả hai đều phải được chấp nhận, nếu không thì mọi lời
        # giải viết theo sách giáo khoa bị kết tội hàng loạt.
        assert check_molar_mass(r"M_{\mathrm{CuO}} = 80")[0] == "balanced"
        assert check_molar_mass(r"M_{\mathrm{CuO}} = 79{,}5")[0] == "balanced"

    def test_bat_duoc_khoi_luong_mol_sai(self) -> None:
        verdict, detail = check_molar_mass(r"M_{\mathrm{H_2SO_4}} = 89")
        assert verdict == "unbalanced"
        assert "98" in detail

    def test_dau_phay_thap_phan_kieu_viet_nam(self) -> None:
        assert check_molar_mass(r"M_{\mathrm{NaCl}} = 58{,}5")[0] == "balanced"

    def test_khong_doi_chieu_khi_chua_du_can_cu(self) -> None:
        # Không biết chất nào thì không có gì để tra bảng.
        assert check_molar_mass(r"M = 98")[0] == "unknown"
        # Nhãn không phải công thức hoá học.
        assert check_molar_mass(r"M_{X} = 100")[0] == "unknown"

    def test_khong_vo_lay_con_so_giua_mot_phep_tinh(self) -> None:
        # `M_{AlCl_3} = 26,98 + 3 × 35,45 = 133,33` là chuỗi cộng. Nếu bộ kiểm
        # tóm lấy con số gần nhất thì nó đem 35,45 so với 133,33 rồi kết tội một
        # bước hoàn toàn đúng. Chuỗi tính như thế để lớp CAS thường lo.
        claim = r"M_{\mathrm{AlCl_3}} = 26{,}98 + 3 \times 35{,}45 = 133{,}33\ \mathrm{g/mol}"
        assert check_molar_mass(claim)[0] == "unknown"


class TestCanBang:
    def test_xac_nhan_phuong_trinh_can_bang(self) -> None:
        for latex in (
            r"2\mathrm{H_2} + \mathrm{O_2} \rightarrow 2\mathrm{H_2O}",
            r"2\mathrm{NaOH} + \mathrm{CO_2} \rightarrow \mathrm{Na_2CO_3} + \mathrm{H_2O}",
            r"3\mathrm{Cu} + 8\mathrm{HNO_3} \to"
            r" 3\mathrm{Cu(NO_3)_2} + 2\mathrm{NO} + 4\mathrm{H_2O}",
            r"2\mathrm{Al} + \mathrm{Fe_2O_3} \to \mathrm{Al_2O_3} + 2\mathrm{Fe}",
        ):
            assert check_equation(latex)[0] == "balanced", latex

    def test_ket_toi_phuong_trinh_lech_nguyen_tu(self) -> None:
        verdict, detail = check_equation(r"\mathrm{H_2} + \mathrm{O_2} \rightarrow \mathrm{H_2O}")
        assert verdict == "unbalanced"
        assert "O" in detail

    def test_ket_toi_he_so_sai(self) -> None:
        assert check_equation(
            r"\mathrm{Al} + 3\mathrm{HCl} \to \mathrm{AlCl_3} + \mathrm{H_2}"
        )[0] == "unbalanced"

    def test_phuong_trinh_ion_can_ca_dien_tich(self) -> None:
        assert check_equation(
            r"\mathrm{Ba^{2+}(aq)} + \mathrm{SO_4^{2-}(aq)} \rightarrow \mathrm{BaSO_4(s)}"
        )[0] == "balanced"
        assert check_equation(
            r"\mathrm{MnO_4^{-}} + 8\mathrm{H^{+}} + 5\mathrm{Fe^{2+}}"
            r" \rightarrow \mathrm{Mn^{2+}} + 5\mathrm{Fe^{3+}} + 4\mathrm{H_2O}"
        )[0] == "balanced"

    def test_ban_phan_ung_co_electron(self) -> None:
        assert check_equation(r"\mathrm{Zn} \rightarrow \mathrm{Zn^{2+}} + 2e^{-}")[0] == "balanced"
        # Lối viết trừ electron của kho Việt Nam.
        assert check_equation(r"\mathrm{Fe} - 2e^{-} \rightarrow \mathrm{Fe^{2+}}")[0] == "balanced"

    def test_he_so_phan_so(self) -> None:
        assert check_equation(
            r"\mathrm{Na} + \mathrm{H_2O} \to \mathrm{NaOH} + \tfrac{1}{2}\mathrm{H_2}"
        )[0] == "balanced"

    def test_trang_thai_chat_va_ket_tua_khong_tinh_vao_can_bang(self) -> None:
        assert check_equation(
            r"\mathrm{CaF_2(s)} \rightleftharpoons \mathrm{Ca^{2+}} + 2\mathrm{F^{-}}"
        )[0] == "balanced"

    def test_xuc_tac_tren_mui_ten_khong_tinh_vao_can_bang(self) -> None:
        assert check_equation(r"C_6H_6 + Br_2 \xrightarrow{Fe} C_6H_5Br + HBr")[0] == "balanced"


class TestKhongKetToiKhiThieuCanCu:
    """Phần quan trọng nhất: những chỗ hệ thống PHẢI im lặng."""

    def test_mui_ten_gioi_han_cua_mon_toan(self) -> None:
        # `\to` là mũi tên giới hạn ở 104/211 bước có mũi tên trong kho.
        for latex in (
            r"\lim_{x \to 3} \frac{x^2-9}{x^2-5x+6}",
            r"n \to \infty",
            r"\bar{X} \xrightarrow{\ d\ } N\left(\mu, \frac{\sigma^{2}}{n}\right)",
            r"\left| \int_{a}^{b} f_{n} \right| \le (b-a) \longrightarrow 0",
        ):
            assert check_equation(latex)[0] == "unknown", latex

    def test_codon_mon_sinh_khong_phai_phan_ung(self) -> None:
        # `UUU \rightarrow UUC` là đột biến codon, nhưng U là urani và C là
        # cacbon nên nó đọc trót lọt thành hai "chất" rồi bị báo lệch nguyên tử.
        # Đây là báo oan thật đã bắt được khi quét kho, không phải giả định.
        assert check_equation(r"UUU \rightarrow UUC")[0] == "unknown"
        assert check_equation(r"UGG \rightarrow UGA")[0] == "unknown"

    def test_so_do_va_an_so_khong_phai_phan_ung(self) -> None:
        assert check_equation(r"X \rightarrow Y")[0] == "unknown"
        assert check_equation(r"AAbb \times aaBB \rightarrow F_{1}: AaBb")[0] == "unknown"
        assert check_equation(r"G_{1} \xrightarrow{\text{diem kiem soat}} S")[0] == "unknown"

    def test_chuoi_chuyen_hoa_nhieu_mui_ten(self) -> None:
        # Chu trình nitơ: một dãy chuyển hoá, không phải một phương trình để cân.
        assert check_equation(
            r"NO_{3}^{-} \rightarrow NO_{2}^{-} \rightarrow NO \rightarrow N_{2}"
        )[0] == "unknown"

    def test_nhan_mui_ten_mang_dau_la_manh_mat_them(self) -> None:
        # Phổ khối: `\xrightarrow{-CH_3}` nghĩa là mất mảnh CH₃, mảnh ấy ĐỔI cân
        # bằng nên không được coi là xúc tác rồi gỡ đi.
        assert check_equation(r"72 \xrightarrow{-\mathrm{CH_3}} 57")[0] == "unknown"

    def test_he_so_la_an_thi_khong_ket_luan(self) -> None:
        # Trùng hợp polymer: `n` chưa biết.
        assert check_equation(r"n\,CH_2=CH_2 \rightarrow (-CH_2-CH_2-)_n")[0] == "unknown"

    def test_co_chu_tieng_viet_thi_khong_ket_luan(self) -> None:
        assert check_equation(
            r"CH_3\text{-}C\equiv C\text{-}CH_3 + AgNO_3 \rightarrow \text{khong phan ung}"
        )[0] == "unknown"

    def test_chat_ngoai_bang_nguyen_to_thi_khong_ket_luan(self) -> None:
        # ATP / ADP / P_i không phải công thức phân tử.
        assert check_equation(
            r"N_{2} + 8H^{+} + 8e^{-} + 16\,ATP \rightarrow 2NH_{3} + 16\,ADP"
        )[0] == "unknown"

    def test_dien_tich_lech_thi_chua_ket_luan_chu_khong_ket_toi(self) -> None:
        # Kho ghi số oxi hoá ở mũ hệt như ghi điện tích ion, nên nguyên tử cân mà
        # điện tích lệch thì gần như luôn là lối viết chứ không phải lỗi.
        verdict, detail = check_equation(r"\mathrm{Fe^{2+}} \rightarrow \mathrm{Fe^{3+}}")
        assert verdict == "unknown"
        assert "điện tích" in detail


class TestGhepVaoLuongKiemChung:
    def test_buoc_hoa_hoc_duoc_xac_nhan(self) -> None:
        checks = check_steps(
            [{"latex": r"2\mathrm{Al} + 6\mathrm{HCl} \to 2\mathrm{AlCl_3} + 3\mathrm{H_2}",
              "explain": "Viết phương trình phản ứng"}]
        )
        assert checks[0].status == "verified"
        assert "cân bằng" in (checks[0].detail or "")

    def test_chu_thich_sau_dau_hai_cham_khong_can_tro(self) -> None:
        checks = check_steps(
            [{"latex": r"\mathrm{Na} + \mathrm{H_2O} \to \mathrm{NaOH}"
                       r" + \tfrac{1}{2}\mathrm{H_2}:\ n_{\mathrm{NaOH}} = 0{,}2",
              "explain": ""}]
        )
        assert checks[0].status == "verified"

    def test_ket_toi_di_qua_duoc_hang_rao_lien_tu(self) -> None:
        # Bước Hoá gần như luôn có chữ "cân bằng"/"phản ứng" trong lời giải
        # thích, mà những chữ ấy nằm sẵn trong `_SOLVING_WORDS` và bình thường sẽ
        # hạ mọi kết luận "sai" xuống "chưa kết luận". Với phương trình phản ứng
        # thì hàng rào ấy không đúng: mũi tên khẳng định bảo toàn khối lượng, và
        # không câu chữ nào làm cho một phương trình lệch nguyên tử thành đúng.
        checks = check_steps(
            [{"latex": r"\mathrm{H_2} + \mathrm{O_2} \rightarrow \mathrm{H_2O}",
              "explain": "Cân bằng phương trình rồi suy ra số mol"}]
        )
        assert checks[0].status == "refuted"

    def test_buoc_toan_co_mui_ten_khong_bi_dong_cham(self) -> None:
        checks = check_steps(
            [{"latex": r"\lim_{x \to 3} \frac{x^{2}-9}{x-3} = 6", "explain": ""}]
        )
        assert checks[0].status != "refuted"

    def test_khong_bia_ket_luan_cho_buoc_sinh_hoc(self) -> None:
        checks = check_steps([{"latex": r"UUU \rightarrow UUC:\ Phe \rightarrow Phe",
                               "explain": "Đột biến đồng nghĩa"}])
        assert checks[0].status != "refuted"

    def test_dap_so_khong_bi_ket_toi_theo(self) -> None:
        # Xác nhận thêm một bước Hoá không được kéo theo kết luận gì về đáp số.
        result = verify_answer(
            answer="0,2 mol",
            answer_numeric=0.2,
            steps=[{"latex": r"2\mathrm{Al} + 6\mathrm{HCl} \to 2\mathrm{AlCl_3} + 3\mathrm{H_2}",
                    "explain": ""}],
        )
        assert result.answer_status != "refuted"
        assert result.steps_refuted == 0
