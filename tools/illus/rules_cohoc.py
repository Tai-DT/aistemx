"""Luật gán hình cho họ **cơ học**.

Mỗi luật là một **bảng tra theo id đầy đủ**, không phải một phép so chuỗi con.
Lí do: chuỗi con trong lĩnh vực này bắt nhầm cực kỳ dễ và cực kỳ khó thấy —
``luc`` trúng ``luc-day-ac-si-met`` lẫn ``ai-luc-electron``; ``song`` trúng
``song-song`` (hai đường thẳng song song) và ``nguyen-li-song-anh``; ``dao-dong``
trúng cả dao động phân tử trong hoá lượng tử, nơi hình con lắc lò xo là sai
hoàn toàn. Bảng id thì mỗi dòng đã được đọc tận nơi công thức trước khi thêm.

Cái giá phải trả là luật không tự nới sang công thức mới thêm vào kho sau này.
Đổi lại là không có hình sai — mà một hình sai thì người học không có cách nào
phát hiện, nên đây là đánh đổi đúng chiều.

Phạm vi: các chủ đề ``Động học``, ``Động lực học``, ``Dao động điều hoà``,
``Sóng cơ``, ``Cơ học chất điểm`` (vật lí THPT/đại học), cùng ba chủ đề cơ học
THCS ``Chuyển động``, ``Lực``, ``Cơ năng`` — cùng một bộ hình dùng lại được.
"""

from __future__ import annotations

from typing import Callable, Optional

# Cùng chữ ký với matcher.py — khai lại tại chỗ để module đứng một mình được.
Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]

#: (generator, params, ghi chú) tra theo id công thức.
Bang = dict[str, tuple[dict, str]]


def _tra(bang: Bang, generator: str) -> Rule:
    """Dựng một luật từ bảng id → tham số. Trả bản sao params để bảng bất biến."""

    def luat(f: dict) -> Optional[Match]:
        got = bang.get(f.get("id", ""))
        if got is None:
            return None
        params, ghi_chu = got
        return generator, dict(params), ghi_chu

    return luat


# --------------------------------------------------------------------------
# Đồ thị chuyển động
# --------------------------------------------------------------------------
_XT: Bang = {
    "physics.thpt.dong-hoc.phuong-trinh-chuyen-dong-thang-deu": (
        {"x0": 2, "v": 1.6, "tmax": 6, "slope": True},
        "đồ thị x-t của chuyển động thẳng đều, độ dốc = v"),
    "physics.thpt.dong-hoc.do-doc-do-thi-do-dich-chuyen-thoi-gian": (
        {"x0": 1, "v": 1.8, "tmax": 6, "slope": True},
        "độ dốc đồ thị d-t chính là vận tốc"),
    "physics.thpt.dong-hoc.do-dich-chuyen": (
        {"x0": 2, "v": 1.5, "tmax": 5, "delta": True},
        "độ dịch chuyển d = x₂ − x₁ đọc trên đồ thị x-t"),
    "physics.thpt.dong-hoc.van-toc-trung-binh": (
        {"x0": 1, "v": 0, "tmax": 6, "chord": True, "slope_label": "v",
         "points": [[0, 1], [2, 4], [4, 5], [6, 9]]},
        "vận tốc trung bình = độ dốc dây cung"),
    "physics.thpt.dong-hoc.toc-do-trung-binh": (
        {"tmax": 6, "chord": True, "slope_label": "v", "ylabel": "s (m)",
         "points": [[0, 0], [2, 3], [4, 4], [6, 9]]},
        "tốc độ trung bình = quãng đường chia thời gian"),
    "physics.thpt.dong-hoc.van-toc-tuc-thoi": (
        {"x0": 0, "v": 1.0, "a": 1.2, "tmax": 5, "tangent": 3.0},
        "vận tốc tức thời = độ dốc tiếp tuyến của đồ thị x-t"),
    "physics.thcs.chuyen-dong.quang-duong": (
        {"x0": 0, "v": 2, "tmax": 6, "slope": True, "ylabel": "s (m)"},
        "đồ thị quãng đường - thời gian, s = v·t"),
    "physics.thcs.chuyen-dong.toc-do": (
        {"x0": 0, "v": 2, "tmax": 6, "slope": True, "ylabel": "s (m)"},
        "tốc độ = độ dốc đồ thị s-t"),
    "physics.thcs.chuyen-dong.thoi-gian": (
        {"x0": 0, "v": 2, "tmax": 6, "slope": True, "ylabel": "s (m)"},
        "thời gian đọc từ đồ thị s-t"),
    "physics.thcs.chuyen-dong.toc-do-trung-binh": (
        {"tmax": 6, "chord": True, "ylabel": "s (m)",
         "points": [[0, 0], [2, 3], [4, 4], [6, 9]]},
        "tốc độ trung bình của cả hành trình"),
    "physics.thcs.chuyen-dong.toc-do-trung-binh-hai-giai-doan": (
        {"tmax": 6, "chord": True, "ylabel": "s (m)",
         "points": [[0, 0], [1.5, 4], [6, 8]]},
        "hai giai đoạn cùng quãng đường, khác tốc độ"),
}

_VT: Bang = {
    "physics.thpt.dong-hoc.van-toc-chuyen-dong-bien-doi-deu": (
        {"v0": 2, "a": 1.5, "tmax": 6, "slope": True},
        "đồ thị v-t, độ dốc = gia tốc"),
    "physics.thpt.dong-hoc.gia-toc-trung-binh": (
        {"v0": 2, "a": 1.5, "tmax": 6, "slope": True},
        "gia tốc trung bình = Δv/Δt trên đồ thị v-t"),
    "physics.thpt.dong-hoc.dien-tich-do-thi-van-toc-thoi-gian": (
        {"v0": 2, "a": 1.2, "tmax": 6, "area": True},
        "độ dịch chuyển = diện tích dưới đồ thị v-t"),
    "physics.thpt.dong-hoc.quang-duong-chuyen-dong-bien-doi-deu": (
        {"v0": 2, "a": 1.2, "tmax": 6, "area": True},
        "d = v₀t + ½at² là diện tích hình thang dưới đồ thị v-t"),
    "physics.thpt.dong-hoc.he-thuc-doc-lap-thoi-gian": (
        {"v0": 2, "a": 1.2, "tmax": 6, "area": True},
        "v² − v₀² = 2ad, với d là diện tích dưới đồ thị v-t"),
    "physics.thpt.dong-hoc.quang-duong-chuyen-dong-thang-deu": (
        {"v0": 3, "a": 0, "tmax": 6, "area": True, "area_label": "s"},
        "s = v·t là diện tích hình chữ nhật dưới đồ thị v-t"),
    "physics.thpt.dong-hoc.van-toc-trung-binh-bien-doi-deu": (
        {"v0": 2, "a": 1.2, "tmax": 6, "mean": True},
        "v_tb = (v₀ + v)/2 của chuyển động biến đổi đều"),
    "physics.thpt.dong-hoc.quang-duong-trong-giay-thu-n": (
        {"v0": 1, "a": 1.4, "tmax": 6, "strip": [3, 4], "area_label": "s"},
        "quãng đường trong giây thứ n là dải hẹp dưới đồ thị v-t"),
    "physics.thpt.dong-hoc.roi-tu-do-van-toc": (
        {"v0": 0, "a": 9.8, "tmax": 3, "slope": True, "slope_label": "g"},
        "v = gt: đồ thị v-t của rơi tự do"),
}

_TRIO: Bang = {
    "physics.thpt.dong-hoc.phuong-trinh-toa-do-chuyen-dong-bien-doi-deu": (
        {"x0": 0, "v0": 1, "a": 1.2, "tmax": 5},
        "x-t parabol, v-t đường thẳng, a-t hằng số"),
}

_ROI: Bang = {
    "physics.thpt.dong-hoc.roi-tu-do-quang-duong": (
        {"h": 45, "n": 4}, "h = ½gt²"),
    "physics.thpt.dong-hoc.roi-tu-do-thoi-gian-roi": (
        {"h": 45, "n": 4}, "thời gian rơi từ độ cao h"),
    "physics.thpt.dong-hoc.roi-tu-do-quang-duong-giay-thu-n": (
        {"h": 45, "n": 4}, "quãng đường các giây liên tiếp tỉ lệ 1 : 3 : 5 : 7"),
    "physics.thpt.dong-hoc.roi-tu-do-he-thuc-doc-lap": (
        {"h": 45, "n": 4}, "v² = 2gh"),
    "physics.thcs.co-nang.van-toc-roi-tu-do": (
        {"h": 45, "n": 4}, "v = √(2gh) khi rơi tự do"),
    "physics.thpt.dong-hoc.nem-thang-dung-do-cao-cuc-dai": (
        {"h": 45, "n": 3, "direction": "len"}, "độ cao cực đại khi ném thẳng đứng lên"),
    "physics.thpt.dong-hoc.nem-thang-dung-thoi-gian-len": (
        {"h": 45, "n": 3, "direction": "len"}, "thời gian lên tới điểm cao nhất"),
}

_NEM_NGANG: Bang = {
    "physics.thpt.dong-hoc.nem-ngang-phuong-trinh-chuyen-dong": (
        {"v0": 12, "H": 20}, "x = v₀t, y = ½gt²"),
    "physics.thpt.dong-hoc.nem-ngang-phuong-trinh-quy-dao": (
        {"v0": 12, "H": 20}, "quỹ đạo nửa parabol"),
    "physics.thpt.dong-hoc.nem-ngang-tam-xa": (
        {"v0": 12, "H": 20}, "tầm xa L của vật ném ngang"),
    "physics.thpt.dong-hoc.nem-ngang-thoi-gian-roi": (
        {"v0": 12, "H": 20}, "thời gian rơi chỉ phụ thuộc độ cao"),
    "physics.thpt.dong-hoc.nem-ngang-van-toc-cham-dat": (
        {"v0": 12, "H": 20}, "v = √(vₓ² + v_y²)"),
    "physics.thpt.dong-hoc.nem-ngang-goc-hop-phuong-ngang": (
        {"v0": 12, "H": 20}, "góc β giữa vận tốc và phương ngang"),
}

# ném xiên đã có generator `projectile` ở generators2d; matcher.py chỉ nhận 4 id,
# ba id dưới đây bị bỏ sót nên nhận thêm ở đây (KHÔNG đụng vào 4 id kia).
_NEM_XIEN: Bang = {
    "physics.thpt.dong-hoc.nem-xien-phuong-trinh-chuyen-dong": (
        {"v0": 22, "angle": 45}, "phương trình chuyển động của vật ném xiên"),
    "physics.thpt.dong-hoc.nem-xien-tam-cao": (
        {"v0": 22, "angle": 55}, "tầm cao của vật ném xiên"),
    "physics.thpt.dong-hoc.nem-xien-thoi-gian-bay": (
        {"v0": 22, "angle": 45}, "thời gian bay của vật ném xiên"),
}

_TRON: Bang = {
    "physics.thpt.dong-hoc.gia-toc-huong-tam": (
        {"center_label": "a_ht"}, "gia tốc hướng tâm hướng vào tâm quỹ đạo"),
    "physics.thpt.dong-luc-hoc.luc-huong-tam": (
        {"center_label": "F_ht"}, "lực hướng tâm hướng vào tâm quỹ đạo"),
    "physics.thpt.dong-hoc.lien-he-toc-do-dai-toc-do-goc": (
        {"show_a": False, "show_omega": True}, "v = ωr"),
    "physics.thpt.dong-hoc.toc-do-goc": (
        {"show_a": False, "show_omega": True}, "ω = Δφ/Δt"),
    "physics.thpt.dong-hoc.chu-ki-chuyen-dong-tron-deu": (
        {"show_a": False, "show_omega": True}, "chu kì của chuyển động tròn đều"),
    "physics.thpt.dong-hoc.tan-so-chuyen-dong-tron-deu": (
        {"show_a": False, "show_omega": True}, "tần số của chuyển động tròn đều"),
}


# --------------------------------------------------------------------------
# Sơ đồ lực
# --------------------------------------------------------------------------
_FBD_NGANG: Bang = {
    "physics.thpt.dong-luc-hoc.luc-ma-sat-truot": (
        {"keo": True, "ma_sat": True, "gia_toc": "ngang"}, "F_ms trượt = μ_t·N"),
    "physics.thpt.dong-luc-hoc.luc-ma-sat-lan": (
        {"keo": True, "ma_sat": True, "gia_toc": "ngang"}, "F_ms lăn = μ_l·N"),
    "physics.thpt.dong-luc-hoc.luc-ma-sat-nghi": (
        {"keo": True, "ma_sat": True}, "ma sát nghỉ cân bằng với ngoại lực"),
    "physics.thcs.luc.luc-ma-sat": (
        {"keo": True, "ma_sat": True}, "F_ms = μN"),
    "physics.thcs.luc.luc-ma-sat-nghi": (
        {"keo": True, "ma_sat": True}, "ma sát nghỉ bằng lực kéo khi vật đứng yên"),
    "physics.thpt.dong-luc-hoc.dinh-luat-ii-newton": (
        {"keo": True, "ma_sat": False, "gia_toc": "ngang", "nhan_keo": "F"},
        "hợp lực khác 0 sinh ra gia tốc cùng hướng"),
    "physics.thpt.dong-luc-hoc.dinh-luat-i-newton": (
        {"keo": False, "ma_sat": False}, "hợp lực bằng 0 → vận tốc không đổi"),
    "physics.thcs.luc.quan-tinh": (
        {"keo": False, "ma_sat": False}, "quán tính: hợp lực bằng 0"),
    "physics.thpt.dong-luc-hoc.trong-luong-bieu-kien": (
        {"keo": False, "ma_sat": False, "gia_toc": "len"},
        "trọng lượng biểu kiến trong thang máy có gia tốc"),
}

_FBD_NGHIENG: Bang = {
    "physics.thpt.dong-luc-hoc.mat-phang-nghieng-khong-ma-sat": (
        {"alpha": 30, "ma_sat": False}, "a = g·sin α khi không có ma sát"),
    "physics.thpt.dong-luc-hoc.mat-phang-nghieng-co-ma-sat": (
        {"alpha": 30, "ma_sat": True}, "a = g(sin α − μ·cos α)"),
    "physics.thpt.dong-luc-hoc.phan-luc-mat-phang-nghieng": (
        {"alpha": 32, "ma_sat": False}, "N = mg·cos α"),
    "physics.thpt.dong-luc-hoc.dieu-kien-nam-yen-mat-phang-nghieng": (
        {"alpha": 26, "ma_sat": True}, "vật nằm yên khi tan α ≤ μ"),
}

_FBD_TREO: Bang = {
    "physics.thpt.dong-luc-hoc.luc-cang-day": (
        {"gia_toc": "len"}, "T = m(g + a)"),
    "physics.thcs.luc.hai-luc-can-bang": (
        {"can_bang": True}, "hai lực cân bằng: T và P"),
    "physics.thcs.luc.dieu-kien-can-bang-vat": (
        {"can_bang": True}, "vật cân bằng khi hợp lực bằng 0"),
}

_HE_VAT: Bang = {
    "physics.thpt.dong-luc-hoc.he-vat-qua-rong-roc": (
        {"kind": "atwood"}, "máy Atwood"),
    "physics.thpt.dong-luc-hoc.he-vat-ban-va-vat-treo": (
        {"kind": "ban-treo", "ma_sat": True}, "vật trên bàn nối vật treo qua ròng rọc"),
    "physics.thpt.dong-luc-hoc.he-hai-vat-noi-day-tren-mat-ngang": (
        {"kind": "ngang", "ma_sat": True}, "hai vật nối dây, kéo trên mặt ngang"),
}


# --------------------------------------------------------------------------
# Dao động điều hoà
# --------------------------------------------------------------------------
_LO_XO_NGANG: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.con-lac-lo-xo-chu-ki": (
        {}, "con lắc lò xo nằm ngang"),
    "physics.thpt.dao-dong-dieu-hoa.luc-keo-ve": (
        {"x": -0.62}, "lực kéo về F = −kx luôn hướng về VTCB"),
}

_LO_XO_DOC: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.con-lac-lo-xo-thang-dung": (
        {"bien_do": True}, "Δℓ₀ = mg/k của lò xo treo thẳng đứng"),
    "physics.thpt.dong-luc-hoc.lo-xo-treo-thang-dung": (
        {"bien_do": False, "luc": True}, "độ dãn ở vị trí cân bằng"),
    "physics.thpt.dao-dong-dieu-hoa.chieu-dai-lo-xo-dao-dong": (
        {"bien_do": True}, "ℓ_max, ℓ_min của lò xo khi dao động"),
    "physics.thpt.dao-dong-dieu-hoa.luc-dan-hoi-con-lac-lo-xo": (
        {"bien_do": True, "luc": True}, "lực đàn hồi cực đại, cực tiểu"),
    "physics.thpt.dong-luc-hoc.dinh-luat-hooke": (
        {"bien_do": False, "luc": True}, "F_đh = k·|Δℓ|"),
    "physics.thcs.luc.luc-dan-hoi-lo-xo": (
        {"bien_do": False, "luc": True}, "lực đàn hồi của lò xo"),
    "physics.thcs.luc.do-cung-lo-xo": (
        {"bien_do": False, "luc": True}, "độ cứng k = F_đh / |Δℓ|"),
    "physics.thcs.luc.chieu-dai-lo-xo": (
        {"bien_do": False, "luc": False}, "ℓ = ℓ₀ + Δℓ"),
}

_CON_LAC_DON: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.con-lac-don-chu-ki": (
        {"alpha": 32}, "chu kì con lắc đơn"),
    "physics.thpt.dao-dong-dieu-hoa.phuong-trinh-con-lac-don": (
        {"alpha": 32, "luc": False}, "li độ cong s = αℓ"),
    "physics.thpt.dao-dong-dieu-hoa.nang-luong-con-lac-don": (
        {"alpha": 44, "luc": False, "do_cao": True}, "W = mgℓ(1 − cos α₀)"),
    "physics.thpt.dao-dong-dieu-hoa.van-toc-con-lac-don": (
        {"alpha": 44, "luc": False, "do_cao": True}, "v = √(2gℓ(cos α − cos α₀))"),
    "physics.thpt.dao-dong-dieu-hoa.luc-cang-day-con-lac-don": (
        {"alpha": 36, "cang": True}, "lực căng dây con lắc đơn"),
}

_SHM_XT: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.phuong-trinh-li-do": (
        {"A": 4, "T": 2, "phi": 0}, "x = A·cos(ωt + φ)"),
    "physics.thpt.dao-dong-dieu-hoa.chu-ki-tan-so": (
        {"A": 4, "T": 2}, "chu kì đọc trên đồ thị li độ"),
    "physics.thpt.dao-dong-dieu-hoa.quang-duong-trong-mot-chu-ki": (
        {"A": 4, "T": 2, "note": "mỗi chu kì vật đi được 4A"},
        "quãng đường trong một chu kì bằng 4A"),
}

_SHM_TRIO: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.phuong-trinh-van-toc": (
        {"A": 4, "T": 2}, "v sớm pha π/2 so với x"),
    "physics.thpt.dao-dong-dieu-hoa.phuong-trinh-gia-toc": (
        {"A": 4, "T": 2}, "a ngược pha với x"),
    "physics.thpt.dao-dong-dieu-hoa.gia-tri-cuc-dai-v-a": (
        {"A": 4, "T": 2}, "v_max = ωA, a_max = ω²A"),
}

_SHM_ELIP: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.he-thuc-doc-lap-x-v": (
        {"mode": "x-v"}, "quỹ đạo pha (x, v) là elip nửa trục A và ωA"),
    "physics.thpt.dao-dong-dieu-hoa.he-thuc-doc-lap-v-a": (
        {"mode": "v-a"}, "quỹ đạo pha (v, a) là elip nửa trục ωA và ω²A"),
}

_PHA: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.quang-duong-lon-nhat-nho-nhat": (
        {"dphi": 100}, "S_max, S_min dựng trên vòng tròn pha"),
}

_NANG_LUONG: Bang = {
    "physics.thpt.dao-dong-dieu-hoa.co-nang-dao-dong": (
        {"A": 4}, "cơ năng W = W_đ + W_t không đổi"),
    "physics.thpt.dao-dong-dieu-hoa.dong-nang-dao-dong": (
        {"A": 4}, "động năng theo li độ"),
    "physics.thpt.dao-dong-dieu-hoa.the-nang-dao-dong": (
        {"A": 4}, "thế năng theo li độ"),
    "physics.thpt.dao-dong-dieu-hoa.vi-tri-dong-nang-bang-n-lan-the-nang": (
        {"A": 4, "n": 1}, "vị trí W_đ = n·W_t"),
}


# --------------------------------------------------------------------------
# Sóng cơ
# --------------------------------------------------------------------------
_SONG: Bang = {
    "physics.thpt.song-co.buoc-song": (
        {}, "λ là khoảng cách hai đỉnh sóng liên tiếp"),
    "physics.thpt.song-co.phuong-trinh-song": (
        {}, "hình dạng sóng tại một thời điểm"),
    "physics.thpt.song-co.do-lech-pha-hai-diem": (
        {"two_points": True, "d": 0.75}, "Δφ = 2πd/λ giữa hai điểm"),
}

_SONG_DUNG: Bang = {
    "physics.thpt.song-co.song-dung-hai-dau-co-dinh": (
        {"k": 3, "free_end": False}, "ℓ = k·λ/2 khi hai đầu cố định"),
    "physics.thpt.song-co.song-dung-mot-dau-tu-do": (
        {"k": 2, "free_end": True}, "ℓ = (2k+1)·λ/4 khi một đầu tự do"),
    "physics.thpt.song-co.khoang-cach-nut-bung": (
        {"k": 3, "free_end": False}, "nút - nút là λ/2, nút - bụng là λ/4"),
    "physics.thpt.song-co.bien-do-song-dung": (
        {"k": 3, "free_end": False}, "biên độ điểm trên sóng dừng nằm giữa hai đường bao"),
    "physics.thpt.song-co.hoa-am-day-dan": (
        {"modes": 3, "free_end": False, "mark": False}, "các hoạ âm của dây hai đầu cố định"),
}

_GIAO_THOA: Bang = {
    "physics.thpt.song-co.dieu-kien-cuc-dai-giao-thoa-cung-pha": (
        {"show": "cuc-dai"}, "cực đại khi d₂ − d₁ = kλ"),
    "physics.thpt.song-co.dieu-kien-cuc-tieu-giao-thoa-cung-pha": (
        {"show": "cuc-tieu"}, "cực tiểu khi d₂ − d₁ = (k + ½)λ"),
    "physics.thpt.song-co.bien-do-giao-thoa": (
        {"show": "ca-hai"}, "biên độ tại M phụ thuộc hiệu đường đi"),
    "physics.thpt.song-co.phuong-trinh-giao-thoa-hai-nguon-cung-pha": (
        {"show": "ca-hai"}, "sóng tổng hợp tại M trong vùng giao thoa"),
    "physics.thpt.song-co.khoang-cach-hai-cuc-dai-lien-tiep": (
        {"show": "cuc-dai", "kmax": 3, "khoang_cach": True, "mark_M": False},
        "hai cực đại liên tiếp cách nhau λ/2"),
    "physics.thpt.song-co.so-cuc-dai-tren-doan-noi-hai-nguon": (
        {"show": "cuc-dai", "kmax": 3, "mark_M": False},
        "đếm số đường cực đại cắt đoạn S₁S₂"),
}

# Tổng hợp vectơ — dùng lại generator `vector_add` đã có ở generators2d.
_VECTO: Bang = {
    "physics.thpt.dong-luc-hoc.tong-hop-hai-luc-dong-quy": (
        {"ux": 3, "uy": 0.6, "vx": 1.1, "vy": 2.6,
         "label_u": "F₁", "label_v": "F₂", "label_w": "F"},
        "quy tắc hình bình hành cho hai lực đồng quy"),
    "physics.thpt.dong-hoc.cong-thuc-cong-van-toc": (
        {"ux": 3, "uy": 0.5, "vx": 1.0, "vy": 2.4,
         "label_u": "v₁₂", "label_v": "v₂₃", "label_w": "v₁₃"},
        "cộng vận tốc theo quy tắc hình bình hành"),
    "physics.thpt.dong-hoc.cong-van-toc-hop-goc": (
        {"ux": 3, "uy": 0.5, "vx": 1.0, "vy": 2.4,
         "label_u": "v₁₂", "label_v": "v₂₃", "label_w": "v₁₃"},
        "hai vận tốc hợp với nhau một góc"),
    "physics.thpt.dong-hoc.do-dich-chuyen-tong-hop": (
        {"ux": 3, "uy": 0, "vx": 0, "vy": 2.2,
         "label_u": "d₁", "label_v": "d₂", "label_w": "d"},
        "hai độ dịch chuyển vuông góc"),
    "physics.thpt.dao-dong-dieu-hoa.tong-hop-hai-dao-dong-bien-do": (
        {"ux": 3, "uy": 0, "vx": 1.4, "vy": 2.2,
         "label_u": "A₁", "label_v": "A₂", "label_w": "A"},
        "giản đồ Fre-nen: tổng hợp hai dao động điều hoà cùng phương"),
    "physics.thpt.dao-dong-dieu-hoa.tong-hop-hai-dao-dong-pha": (
        {"ux": 3, "uy": 0, "vx": 1.4, "vy": 2.2,
         "label_u": "A₁", "label_v": "A₂", "label_w": "A"},
        "pha ban đầu của dao động tổng hợp"),
    "physics.thpt.dao-dong-dieu-hoa.dieu-kien-bien-do-tong-hop": (
        {"ux": 3, "uy": 0, "vx": 1.4, "vy": 2.2,
         "label_u": "A₁", "label_v": "A₂", "label_w": "A"},
        "miền giá trị biên độ tổng hợp: |A₁ − A₂| ≤ A ≤ A₁ + A₂"),
}


r_do_thi_xt = _tra(_XT, "motion_xt")
r_do_thi_vt = _tra(_VT, "motion_vt")
r_do_thi_bo_ba = _tra(_TRIO, "motion_trio")
r_roi_tu_do = _tra(_ROI, "free_fall")
r_nem_ngang = _tra(_NEM_NGANG, "horizontal_throw")
r_nem_xien_bo_sung = _tra(_NEM_XIEN, "projectile")
r_tron_deu = _tra(_TRON, "circular_motion")
r_so_do_luc_ngang = _tra(_FBD_NGANG, "fbd_horizontal")
r_so_do_luc_nghieng = _tra(_FBD_NGHIENG, "fbd_incline")
r_so_do_luc_treo = _tra(_FBD_TREO, "fbd_hanging")
r_he_vat_noi_day = _tra(_HE_VAT, "connected_bodies")
r_lo_xo_ngang = _tra(_LO_XO_NGANG, "spring_horizontal")
r_lo_xo_doc = _tra(_LO_XO_DOC, "spring_vertical")
r_con_lac_don = _tra(_CON_LAC_DON, "simple_pendulum")
r_do_thi_li_do = _tra(_SHM_XT, "shm_xt")
r_do_thi_x_v_a = _tra(_SHM_TRIO, "shm_trio")
r_elip_pha = _tra(_SHM_ELIP, "shm_phase_ellipse")
r_vong_tron_pha = _tra(_PHA, "phasor_circle")
r_nang_luong_dao_dong = _tra(_NANG_LUONG, "shm_energy")
r_song_ngang = _tra(_SONG, "wave_snapshot")
r_song_dung = _tra(_SONG_DUNG, "standing_wave")
r_giao_thoa = _tra(_GIAO_THOA, "two_source_interference")
r_tong_hop_vecto = _tra(_VECTO, "vector_add")


RULES: list[Rule] = [
    r_do_thi_xt, r_do_thi_vt, r_do_thi_bo_ba,
    r_roi_tu_do, r_nem_ngang, r_nem_xien_bo_sung, r_tron_deu,
    r_so_do_luc_ngang, r_so_do_luc_nghieng, r_so_do_luc_treo, r_he_vat_noi_day,
    r_lo_xo_ngang, r_lo_xo_doc, r_con_lac_don,
    r_do_thi_li_do, r_do_thi_x_v_a, r_elip_pha, r_vong_tron_pha, r_nang_luong_dao_dong,
    r_song_ngang, r_song_dung, r_giao_thoa, r_tong_hop_vecto,
]
