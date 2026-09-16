"""Luật gán generator lượng giác, véc-tơ phẳng và số phức cho công thức.

Ánh xạ chuẩn xác từng công thức lượng giác, hình tam giác, véc-tơ và số phức
vào các generator vector 2D trong `gen_luonggiac.py`.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    """``id`` có kết thúc bằng ``.<tail>`` không (khớp trọn phần đuôi)."""
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


# --------------------------------------------------------------------------
# 1. Tỉ số lượng giác & Tam giác vuông
# --------------------------------------------------------------------------
def r_trig_right_triangle(f: dict) -> Optional[Match]:
    if _tail(f, "ti-so-luong-giac.sin-goc-nhon"):
        return "lg_tam_giac_vuong_abc", {"target": "sin"}, "sin góc nhọn: đối / huyền"
    if _tail(f, "ti-so-luong-giac.cos-goc-nhon"):
        return "lg_tam_giac_vuong_abc", {"target": "cos"}, "cos góc nhọn: kề / huyền"
    if _tail(f, "ti-so-luong-giac.tang-goc-nhon"):
        return "lg_tam_giac_vuong_abc", {"target": "tan"}, "tan góc nhọn: đối / kề"
    if _tail(f, "ti-so-luong-giac.cotang-goc-nhon"):
        return "lg_tam_giac_vuong_abc", {"target": "cot"}, "cot góc nhọn: kề / đối"
    if _tail(f, "ti-so-luong-giac.gia-tri-luong-giac-dac-biet"):
        return "lg_goc_dac_biet", {}, "tỉ số lượng giác các góc đặc biệt 30°, 45°, 60°"
    if _tail(f, "luong-giac.gia-tri-luong-giac-cung-dac-biet"):
        return "lg_gia_tri_dac_biet", {}, "toạ độ (cos; sin) các cung đặc biệt 0, π/6, π/4, π/3, π/2 trên đường tròn đơn vị"
    if _tail(f, "ti-so-luong-giac.he-thuc-canh-goc-theo-sin-cos",
             "ti-so-luong-giac.he-thuc-canh-goc-theo-tan-cot"):
        return "lg_he_thuc_tam_giac_vuong", {}, "hệ thức giữa cạnh và góc trong tam giác vuông"
    return None


# --------------------------------------------------------------------------
# 2. Đường tròn lượng giác & Cung góc
# --------------------------------------------------------------------------
def r_trig_circle(f: dict) -> Optional[Match]:
    if _tail(f, "luong-giac.dinh-nghia-tren-duong-tron",
             "luong-giac.gia-tri-luong-giac-goc-alpha",
             "ti-so-luong-giac.he-thuc-luong-giac-co-ban",
             "ti-so-luong-giac.tan-theo-sin-va-cos",
             "ti-so-luong-giac.tich-tan-va-cot"):
        return "lg_duong_tron_luong_giac", {}, "đường tròn lượng giác đơn vị"
    if _tail(f, "ti-so-luong-giac.hai-goc-phu-nhau",
             "luong-giac.cung-phu",
             "luong-giac.hai-goc-phu"):
        return "lg_cung_lien_ket", {"mode": "phu"}, "hai góc phụ nhau: sin(π/2 - α) = cos α"
    if _tail(f, "luong-giac.cung-bu", "luong-giac.hai-goc-bu"):
        return "lg_cung_lien_ket", {"mode": "bu"}, "hai góc bù nhau: sin(π - α) = sin α"
    if _tail(f, "luong-giac.cung-doi", "luong-giac.hai-goc-doi"):
        return "lg_cung_lien_ket", {"mode": "doi"}, "hai góc đối nhau: cos(-α) = cos α"
    if _tail(f, "luong-giac.cung-hon-kem-pi"):
        return "lg_cung_lien_ket", {"mode": "hon_pi"}, "hai góc hơn kém π: tan(α + π) = tan α"
    if _tail(f, "luong-giac.dau-gia-tri-luong-giac"):
        return "lg_dau_luong_giac", {}, "dấu của sin, cos, tan, cot theo bốn góc phần tư"
    if _tail(f, "goc-va-cung.do-dai-cung-tron"):
        return "lg_cung_quat", {}, "độ dài cung tròn l = R·α và diện tích hình quạt"
    return None


# --------------------------------------------------------------------------
# 3. Đồ thị hàm số lượng giác
# --------------------------------------------------------------------------
def r_trig_graphs(f: dict) -> Optional[Match]:
    if _tail(f, "ham-so-luong-giac.do-thi-ham-sin", "ham-so-luong-giac.ham-sin"):
        return "lg_do_thi_luong_giac", {"fn": "sin"}, "đồ thị hàm số y = sin x"
    if _tail(f, "ham-so-luong-giac.do-thi-ham-cos", "ham-so-luong-giac.ham-cos"):
        return "lg_do_thi_luong_giac", {"fn": "cos"}, "đồ thị hàm số y = cos x"
    if _tail(f, "ham-so-luong-giac.do-thi-ham-tan", "ham-so-luong-giac.ham-tan"):
        return "lg_do_thi_luong_giac", {"fn": "tan"}, "đồ thị hàm số y = tan x"
    if _tail(f, "luong-giac.chu-ki-ham-sin-cos"):
        return "lg_do_thi_luong_giac", {"fn": "sin"}, "chu kì và đồ thị hàm số sin/cos"
    if _tail(f, "luong-giac.chu-ki-ham-tan-cot"):
        return "lg_do_thi_luong_giac", {"fn": "tan"}, "chu kì và đồ thị hàm số tan/cot"
    if _tail(f, "luong-giac.tap-gia-tri-sin-cos"):
        return "lg_do_thi_luong_giac", {"fn": "cos"}, "tập giá trị [-1; 1] của hàm sin và cos"
    return None


# --------------------------------------------------------------------------
# 4. Toạ độ cực
# --------------------------------------------------------------------------
def r_polar_coords(f: dict) -> Optional[Match]:
    if _tail(f, "fm-toa-do-cuc.chuyen-doi-cuc-descartes",
             "fm-toa-do-cuc.duong-cong-cuc-co-ban"):
        return "lg_toa_do_cuc", {}, "chuyển đổi giữa toạ độ cực (r; θ) và Descartes (x; y)"
    if _tail(f, "fm-toa-do-cuc.duong-cardioid"):
        return "lg_duong_cong_cuc", {"curve": "cardioid"}, "đường cardioid trong toạ độ cực r = a(1 + cos θ)"
    if _tail(f, "fm-toa-do-cuc.hoa-hong-cuc"):
        return "lg_duong_cong_cuc", {"curve": "rose"}, "đường hoa hồng cực r = a·cos(nθ)"
    if _tail(f, "fm-toa-do-cuc.xoan-oc-archimedes"):
        return "lg_duong_cong_cuc", {"curve": "spiral"}, "đường xoắn ốc Archimedes r = a·θ"
    return None


# --------------------------------------------------------------------------
# 5. Vectơ phẳng
# --------------------------------------------------------------------------
def r_vectors(f: dict) -> Optional[Match]:
    if _tail(f, "vecto.quy-tac-ba-diem", "vecto.tong-hai-vecto"):
        return "vt_tong", {}, "quy tắc ba điểm cộng vectơ: AB + BC = AC"
    if _tail(f, "vecto.quy-tac-hinh-binh-hanh"):
        return "vt_tong", {"parallelogram": True}, "quy tắc hình bình hành: AB + AD = AC"
    if _tail(f, "vecto.quy-tac-tru", "vecto.hieu-hai-vecto"):
        return "vt_hieu", {}, "quy tắc trừ vectơ chung gốc: AB - AC = CB"
    if _tail(f, "vecto.tich-vecto-voi-mot-so", "vecto.vecto-doi"):
        return "vt_nhan_so", {}, "tích của vectơ với một số k·a"
    if _tail(f, "vecto.dieu-kien-cung-phuong",
             "vecto.ba-diem-thang-hang"):
        return "vt_thang_hang", {}, "điều kiện ba điểm thẳng hàng: AB = k·AC"
    if _tail(f, "vecto.tich-vo-huong",
             "vecto.goc-giua-hai-vecto",
             "vecto.dieu-kien-vuong-goc",
             "vecto.binh-phuong-vo-huong"):
        return "vt_tich_vo_huong", {}, "tích vô hướng: a·b = |a|·|b|·cos(a,b)"
    if _tail(f, "vecto.phan-tich-vecto"):
        return "vt_phan_tich", {}, "phân tích một vectơ theo hai vectơ không cùng phương"
    if _tail(f, "vecto.he-thuc-trung-diem",
             "vecto.trung-tuyen-vecto"):
        return "vt_diem_dac_biet", {"type": "midpoint"}, "hệ thức trung điểm: IA + IB = 0, 2·MI = MA + MB"
    if _tail(f, "vecto.he-thuc-trong-tam"):
        return "vt_diem_dac_biet", {"type": "centroid"}, "hệ thức trọng tâm: GA + GB + GC = 0"
    if _tail(f, "oxy-toa-do.do-dai-vecto"):
        return "vt_tich_vo_huong", {}, "độ dài vectơ trong mặt phẳng tọa độ"
    return None


# --------------------------------------------------------------------------
# 6. Số phức
# --------------------------------------------------------------------------
def r_complex_numbers(f: dict) -> Optional[Match]:
    if _tail(f, "so-phuc.bieu-dien-hinh-hoc",
             "so-phuc.dinh-nghia",
             "so-phuc.dang-dai-so",
             "so-phuc.modun-so-phuc",
             "so-phuc.modun-la-khoang-cach"):
        return "sp_diem_bieu_dien", {}, "biểu diễn hình học số phức z = a + bi trên mặt phẳng Argand"
    if _tail(f, "so-phuc.so-phuc-lien-hop",
             "so-phuc.tinh-chat-lien-hop"):
        return "sp_lien_hop", {}, "số phức liên hợp z và z̄ đối xứng qua trục thực"
    if _tail(f, "so-phuc.cong-tru-so-phuc",
             "so-phuc.bat-dang-thuc-modun",
             "so-phuc.phep-cong-so-phuc",
             "so-phuc.phep-tru-so-phuc"):
        return "sp_cong", {}, "phép cộng số phức theo quy tắc hình bình hành"
    if _tail(f, "so-phuc.dang-luong-giac",
             "so-phuc.nhan-chia-dang-luong-giac",
             "so-phuc.cong-thuc-moivre",
             "fm-so-phuc.nhan-la-quay-vi-tu",
             "so-phuc.nhan-quay"):
        return "sp_nhan_quay", {}, "nhân số phức và phép quay góc φ"
    if _tail(f, "so-phuc.luy-thua-don-vi-ao",
             "so-phuc.luy-thua-i"):
        return "sp_luy_thua_i", {}, "chu kỳ lũy thừa của đơn vị ảo i"
    if _tail(f, "so-phuc.can-bac-n-so-phuc",
             "fm-so-phuc.can-bac-n-cua-don-vi",
             "fm-so-phuc.can-bac-n-da-giac-deu",
             "so-phuc.can-bac-hai-so-phuc",
             "so-phuc.can-bac-n"):
        return "sp_can_bac_n", {}, "căn bậc n của số phức phân bố đều trên đường tròn"
    if _tail(f, "so-phuc.tap-hop-diem-duong-thang"):
        return "sp_quy_tich", {"kind": "trung-truc"}, "tập hợp điểm là đường trung trực"
    if _tail(f, "so-phuc.tap-hop-diem-duong-tron"):
        return "sp_quy_tich", {"kind": "duong-tron"}, "tập hợp điểm là đường tròn"
    if _tail(f, "fm-so-phuc.quy-tich-apollonius"):
        return "sp_quy_tich", {"kind": "apollonius"}, "quỹ tích đường tròn Apollonius"
    if _tail(f, "fm-so-phuc.quy-tich-cung-tron-arg"):
        return "sp_quy_tich", {"kind": "cung-tron"}, "quỹ tích cung tròn arg((z-a)/(z-b)) = θ"
    if _tail(f, "fm-so-phuc.quy-tich-elip-argand"):
        return "sp_quy_tich", {"kind": "elip"}, "quỹ tích elip |z-a| + |z-b| = const"
    if _tail(f, "fm-so-phuc.quy-tich-tia-arg"):
        return "sp_quy_tich", {"kind": "tia"}, "quỹ tích tia arg(z-a) = θ"
    return None


RULES: list[Rule] = [
    r_trig_right_triangle,
    r_trig_circle,
    r_trig_graphs,
    r_polar_coords,
    r_vectors,
    r_complex_numbers,
]
