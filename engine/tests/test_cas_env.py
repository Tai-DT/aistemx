"""Đòn bẩy L1 — môi trường ký hiệu mang theo giữa các bước.

Cùng tinh thần với `tests/test_cas.py`: phần lớn test ở đây không đo "bắt được
bao nhiêu", mà giữ cho hệ thống **không kết tội ở những chỗ nó không đủ căn
cứ**. Mỗi hàng rào chống báo oan trong `cas/env.py` có đúng một test canh nó.

Chạy:
    PYTHONPATH=<thư-mục-này> pytest test_lever.py -q
"""

from __future__ import annotations

import sympy as sp

from aistem.cas import check_steps, verify_answer
from aistem.cas.env import SymbolEnv
from aistem.textnorm import split_relations


def _statuses(steps: list[dict]) -> list[str]:
    return [c.status for c in check_steps(steps)]


def _step(latex: str, explain: str = "") -> dict:
    return {"explain": explain, "latex": latex}


class TestMoiTruongXacNhanThem:
    def test_thay_rang_buoc_tu_buoc_truoc(self) -> None:
        """Khâu `\\sqrt{g/R} = \\sqrt{9,80/0,200}` kiểm được khi đã biết g và R."""
        steps = [
            _step(r"g = 9{,}80 \quad ; \quad R = 0{,}200"),
            _step(r"\omega_{c} = \sqrt{\frac{g}{R}} = \sqrt{\frac{9{,}80}{0{,}200}}"),
        ]
        assert _statuses(steps)[1] == "verified"

    def test_khong_co_moi_truong_thi_van_la_chua_ket_luan(self) -> None:
        """Không có bước nào đặt g, R thì phải giữ nguyên câu trả lời cũ."""
        steps = [
            _step(r"\omega_{c} = \sqrt{\frac{g}{R}} = \sqrt{\frac{9{,}80}{0{,}200}}")
        ]
        assert _statuses(steps)[0] == "inconclusive"

    def test_rang_buoc_chi_di_theo_chieu_xuoi(self) -> None:
        """Ràng buộc đặt ở bước SAU không được dùng để phán về bước TRƯỚC."""
        steps = [
            _step(r"y = \frac{a}{2} = \frac{6}{2} = 3"),
            _step(r"a = 6"),
        ]
        # Bước 0 chỉ có khâu `6/2 = 3` là kiểm được; khâu `a/2 = 6/2` thì chưa,
        # vì lúc ấy `a` chưa được đặt. Không được sập vào "refuted" ở đâu cả.
        assert _statuses(steps)[0] in {"verified", "inconclusive"}
        assert "refuted" not in _statuses(steps)

    def test_ngu_canh_ngoai_truyen_vao_duoc(self) -> None:
        """`given` cho phép nạp dữ kiện đề bài mà không phá tương thích ngược."""
        steps = [_step(r"F = m a = 2 \times 3")]
        assert _statuses(steps)[0] == "inconclusive"
        assert check_steps(steps, given={"m": 2.0, "a": 3.0})[0].status == "verified"


class TestHangRaoChongBaoOan:
    def test_gan_lai_khong_bao_gio_thanh_ket_toi(self) -> None:
        """`x = 7` sau khi `x = 5` là gán lại hợp lệ, không phải mâu thuẫn."""
        steps = [_step("x = 5"), _step("x = 7"), _step(r"y = 2x = 14")]
        assert "refuted" not in _statuses(steps)

    def test_ky_hieu_dung_lai_bi_vo_hieu(self) -> None:
        """Ký hiệu mang hai giá trị khác nhau thì môi trường thôi tin nó."""
        env = SymbolEnv()
        env.record(["t", "2"], "t = 2")
        assert env.value("t") == 2.0
        env.record(["t", "9"], "t = 9")
        assert env.value("t") is None, "gán lại giá trị khác ⇒ ràng buộc phải chết"

    def test_ve_dang_duoc_dinh_nghia_khong_bi_thay(self) -> None:
        """Không được thay ràng buộc cũ vào chính ký hiệu mà bước này đang gán."""
        env = SymbolEnv({"x": 5.0})
        x, seven = sp.Symbol("x"), sp.Integer(7)
        assert env.reconcile(x, seven, exclude={"x"}) is None
        assert env.reconcile(x, seven) is not None  # không chặn thì mới thay

    def test_thay_xong_ma_lech_thi_chi_neu_ra_chu_khong_ket_toi(self) -> None:
        """Mặc định an toàn: môi trường chỉ được tạo ra xác nhận, không tạo kết tội.

        `a` ở bước 2 mang nghĩa khác hẳn `a` ở bước 0 (đúng kiểu bài nhiều phần),
        nên thay vào thì hai vế lệch — nhưng lời giải không hề sai.
        """
        steps = [
            _step("a = 3"),
            _step(r"S = a b = 40", explain="phần (b): a là cạnh của hình khác"),
        ]
        checks = check_steps(steps)
        assert checks[1].status != "refuted"

    def test_ky_hieu_doi_mu_khong_duoc_gom_chung_voi_ky_hieu_tran(self) -> None:
        """`\\bar{d}` và `d` rơi về cùng một Symbol sau khi gọt LaTeX — cấm thu."""
        env = SymbolEnv()
        raw = r"\bar{d} = 2{,}4083"
        env.record(split_relations(raw)[0], raw)
        assert env.value("d") is None

    def test_loi_sai_that_van_bi_bat(self) -> None:
        """Nới cho đúng không được nới luôn cho sai."""
        assert _statuses([_step("x = 2 + 2 = 5")]) == ["refuted"]


class TestDauXapXi:
    def test_doc_duoc_gia_tri_sau_dau_xap_xi(self) -> None:
        parts, ops = split_relations(r"SE = \frac{1{,}9014}{\sqrt{12}} \approx 0{,}54889")
        assert parts == ["SE", r"\frac{1.9014}{\sqrt{12}}", "0.54889"]
        assert ops == ["=", "≈"]

    def test_khau_xap_xi_duoc_xac_nhan(self) -> None:
        assert _statuses([_step(r"t = \frac{2{,}4083}{0{,}54889} \approx 4{,}388")]) == [
            "verified"
        ]

    def test_khau_xap_xi_khong_bao_gio_ket_toi(self) -> None:
        """`\\sin x \\approx x` là xấp xỉ có chủ ý, không phải lỗi số học."""
        assert _statuses([_step(r"\sin x \approx x")]) == ["inconclusive"]
        assert _statuses([_step(r"(1+x)^{20} \approx 1 + 20x")]) == ["inconclusive"]

    def test_van_bat_loi_o_khau_dang_thuc_ben_canh_khau_xap_xi(self) -> None:
        """Dấu `≈` che cho khâu của nó, không che cho cả dòng."""
        assert _statuses([_step(r"2 + 2 = 5 \approx 5{,}0")]) == ["refuted"]

    def test_gia_tri_sau_dau_xap_xi_vao_duoc_ket_luan_dap_so(self) -> None:
        result = verify_answer(
            answer="0,5489",
            answer_numeric=0.5489,
            steps=[_step(r"SE = \frac{1{,}9014}{\sqrt{12}} \approx 0{,}54889")],
        )
        assert result.answer_status == "verified"


class TestGachThayCan:
    def test_khong_ket_toi_khi_gap_gach_thay_can(self) -> None:
        """Parser đánh rơi `\\left. ... \\right|_{a}^{b}`; đọc bừa là kết tội oan."""
        steps = [
            _step(
                r"S = \frac{1}{18}\cdot\frac{2}{3}\left.u^{3/2}\right|_{4}^{13}"
                r" = \frac{13\sqrt{13} - 8}{27} \approx 1.4397"
            )
        ]
        # Vế có gạch thay cận bị loại **riêng nó**, nên khâu
        # `\frac{13\sqrt{13} - 8}{27} \approx 1.4397` bên cạnh vẫn kiểm được —
        # điều quan trọng là con số parser đọc nhầm không bao giờ được đem ra
        # kết tội.
        assert _statuses(steps) != ["refuted"]

    def test_tri_tuyet_doi_van_kiem_duoc(self) -> None:
        """Chỉ gạch đứng CÓ chỉ số dưới mới là gạch thay cận."""
        assert _statuses([_step(r"|{-3}| + |4| = 7")]) != ["inconclusive"]
