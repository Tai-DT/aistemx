"""Luật khớp generator cho họ hình **điện - từ - quang - nhiệt - hạt nhân**.

Mọi luật ở đây khớp bằng **định danh đầy đủ**, không bằng chuỗi con. Lí do rất
cụ thể: kho này có hàng loạt id gần giống nhau mà nghĩa khác hẳn, và một luật
lỏng tay sẽ gán nhầm mà bảng thống kê vẫn đẹp —

* ``dien-hoc.noi-tiep-dien-tro`` (R nối tiếp) và ``dien-hoc.song-song-dien-tro``
  cùng chứa ``dien-tro``; khớp theo ``"dien-tro" in id`` là vẽ mạch nối tiếp
  cho công thức mạch song song.
* ``dien-xoay-chieu.mach-chi-chua-c`` chỉ có tụ điện, còn
  ``dien-xoay-chieu.tong-tro-rlc`` có đủ R, L, C; cùng thuộc chủ đề
  "Dòng điện xoay chiều" nhưng vẽ chung một sơ đồ là minh hoạ sai đề.
* ``quang-hoc.thau-kinh-hoi-tu-tao-anh`` và ``thau-kinh-phan-ki-tao-anh`` chỉ
  khác nhau một từ, mà ảnh dựng ra thì ngược hẳn (thật/ảo, ngược/cùng chiều).

Đổi lại, luật ở đây **không tự bắt được công thức mới** thêm vào kho sau này.
Đó là đánh đổi cố ý: thà bỏ sót và bổ sung tay còn hơn phủ nhầm.

Cùng chữ ký với ``matcher.py``: mỗi luật nhận dict công thức, trả
``(generator, params, ghi_chú)`` hoặc ``None``.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _lookup(f: dict, gen: str, table: dict[str, tuple[dict, str]]) -> Optional[Match]:
    """Tra id ĐẦY ĐỦ trong bảng; trả bản sao params để phía gọi sửa được tự do."""
    hit = table.get(f.get("id", ""))
    if hit is None:
        return None
    params, note = hit
    return gen, dict(params), note


# --------------------------------------------------------------------------
# Mạch điện một chiều
# --------------------------------------------------------------------------
_NOI_TIEP = {
    "physics.thcs.dien-hoc.noi-tiep-dien-tro": (
        {"resistors": ["R₁", "R₂", "R₃"], "caption": "R_tđ = R₁ + R₂ + R₃"},
        "điện trở tương đương đoạn mạch nối tiếp"),
    "physics.thcs.dien-hoc.noi-tiep-cuong-do": (
        {"resistors": ["R₁", "R₂"], "ammeter": True, "caption": "I = I₁ = I₂"},
        "dòng điện như nhau qua mọi điện trở nối tiếp"),
    "physics.thcs.dien-hoc.noi-tiep-hieu-dien-the": (
        {"resistors": ["R₁", "R₂"], "voltmeter": 0, "caption": "U = U₁ + U₂"},
        "hiệu điện thế cộng trên đoạn mạch nối tiếp"),
    "physics.thcs.dien-hoc.noi-tiep-ti-le": (
        {"resistors": ["R₁", "R₂"], "caption": "U₁ / U₂ = R₁ / R₂"},
        "tỉ lệ hiệu điện thế theo điện trở"),
    "physics.thpt.dong-dien-khong-doi.ghep-dien-tro-noi-tiep": (
        {"resistors": ["R₁", "R₂", "R₃"], "caption": "R = R₁ + R₂ + R₃"},
        "ghép điện trở nối tiếp"),
}

_DINH_LUAT_OM = {
    "physics.thcs.dien-hoc.dinh-luat-om": ("I = U / R", "định luật Ôm cho đoạn mạch"),
    "physics.thcs.dien-hoc.dien-tro-doan-mach": ("R = U / I", "điện trở đoạn mạch"),
    "physics.thcs.dien-hoc.hieu-dien-the-om": ("U = I · R", "hiệu điện thế hai đầu điện trở"),
    "physics.thpt.dong-dien-khong-doi.dinh-luat-om-doan-mach": (
        "I = U / R", "định luật Ôm cho đoạn mạch chỉ chứa R"),
}

_SONG_SONG = {
    "physics.thcs.dien-hoc.song-song-dien-tro": (
        {"resistors": ["R₁", "R₂", "R₃"], "caption": "1/R_tđ = 1/R₁ + 1/R₂ + 1/R₃"},
        "điện trở tương đương đoạn mạch song song"),
    "physics.thcs.dien-hoc.song-song-hai-dien-tro": (
        {"resistors": ["R₁", "R₂"], "caption": "R_tđ = R₁R₂ / (R₁ + R₂)"},
        "hai điện trở song song"),
    "physics.thcs.dien-hoc.song-song-cuong-do": (
        {"resistors": ["R₁", "R₂"], "caption": "I = I₁ + I₂"},
        "dòng mạch chính bằng tổng dòng các nhánh"),
    "physics.thcs.dien-hoc.song-song-hieu-dien-the": (
        {"resistors": ["R₁", "R₂"], "caption": "U = U₁ = U₂"},
        "các nhánh song song cùng hiệu điện thế"),
    "physics.thcs.dien-hoc.song-song-ti-le": (
        {"resistors": ["R₁", "R₂"], "caption": "I₁ / I₂ = R₂ / R₁"},
        "tỉ lệ cường độ dòng điện trong hai nhánh"),
    "physics.thcs.dien-hoc.song-song-n-dien-tro-giong-nhau": (
        {"resistors": ["r", "r", "r"], "caption": "R_tđ = r / n"},
        "n điện trở giống nhau mắc song song"),
    "physics.thpt.dong-dien-khong-doi.ghep-dien-tro-song-song": (
        {"resistors": ["R₁", "R₂", "R₃"], "caption": "1/R = 1/R₁ + 1/R₂ + 1/R₃"},
        "ghép điện trở song song"),
}

_TOAN_MACH = {
    "physics.thpt.dong-dien-khong-doi.dinh-luat-om-toan-mach": (
        "I = ξ / (R_N + r)", "định luật Ôm cho toàn mạch"),
    "physics.thpt.dong-dien-khong-doi.do-giam-the-mach-ngoai": (
        "U_N = ξ − I·r = I·R_N", "độ giảm thế trong nguồn"),
    "physics.thpt.dong-dien-khong-doi.hieu-suat-nguon-dien": (
        "H = U_N / ξ = R_N / (R_N + r)", "hiệu suất nguồn điện"),
    "physics.thpt.dong-dien-khong-doi.cong-suat-mach-ngoai-cuc-dai": (
        "P_N cực đại khi R_N = r", "công suất mạch ngoài cực đại"),
}


def r_mach_noi_tiep(f: dict) -> Optional[Match]:
    return _lookup(f, "circuit_series", _NOI_TIEP)


def r_dinh_luat_om(f: dict) -> Optional[Match]:
    """Ôm cho một điện trở: thêm ampe kế NỐI TIẾP và vôn kế SONG SONG với R.

    Sơ đồ đo là thứ giải thích vì sao I và U trong công thức lại đo được, nên
    nhóm này dùng mạch một điện trở kèm hai dụng cụ đo chứ không phải mạch trơn.
    """
    hit = _DINH_LUAT_OM.get(f.get("id", ""))
    if hit is None:
        return None
    caption, note = hit
    return "circuit_series", {"resistors": ["R"], "ammeter": True,
                              "voltmeter": 0, "caption": caption}, note


def r_mach_song_song(f: dict) -> Optional[Match]:
    return _lookup(f, "circuit_parallel", _SONG_SONG)


def r_toan_mach(f: dict) -> Optional[Match]:
    hit = _TOAN_MACH.get(f.get("id", ""))
    if hit is None:
        return None
    caption, note = hit
    return "circuit_emf", {"caption": caption}, note


# --------------------------------------------------------------------------
# Dòng điện xoay chiều
# --------------------------------------------------------------------------
_XOAY_CHIEU = {
    "physics.thpt.dien-xoay-chieu.mach-chi-chua-r": (
        {"elements": ["R"], "caption": "u cùng pha với i"}, "mạch chỉ chứa R"),
    "physics.thpt.dien-xoay-chieu.mach-chi-chua-l": (
        {"elements": ["L"], "caption": "u sớm pha π/2 so với i"}, "mạch chỉ chứa L"),
    "physics.thpt.dien-xoay-chieu.mach-chi-chua-c": (
        {"elements": ["C"], "caption": "u trễ pha π/2 so với i"}, "mạch chỉ chứa C"),
    "physics.thpt.dien-xoay-chieu.cam-khang": (
        {"elements": ["L"], "caption": "Z_L = ωL = 2πfL"}, "cảm kháng của cuộn cảm"),
    "physics.thpt.dien-xoay-chieu.dung-khang": (
        {"elements": ["C"], "caption": "Z_C = 1 / (ωC)"}, "dung kháng của tụ điện"),
    "physics.thpt.dien-xoay-chieu.dinh-luat-om-xoay-chieu": (
        {"elements": ["R", "L", "C"], "caption": "I = U / Z"},
        "định luật Ôm cho mạch RLC nối tiếp"),
}

_FRENEN = {
    "physics.thpt.dien-xoay-chieu.gian-do-vecto-dien-ap": (
        {}, "hệ thức điện áp trên giản đồ vectơ"),
    "physics.thpt.dien-xoay-chieu.do-lech-pha-rlc": (
        {}, "độ lệch pha giữa u và i"),
    "physics.thpt.dien-xoay-chieu.he-so-cong-suat": (
        {}, "hệ số công suất cos φ = U_R/U"),
    "physics.thpt.dien-xoay-chieu.tong-tro-rlc": (
        {"quantity": "Z"}, "tam giác tổng trở"),
    "physics.thpt.dien-xoay-chieu.cong-huong-dien": (
        {"resonance": True}, "cộng hưởng: Z_L = Z_C nên φ = 0"),
    "physics.thpt.dien-xoay-chieu.cong-suat-dien-xoay-chieu": (
        {}, "công suất P = UI·cos φ đọc từ giản đồ Fre-nen"),
}


def r_mach_xoay_chieu(f: dict) -> Optional[Match]:
    return _lookup(f, "circuit_rlc", _XOAY_CHIEU)


def r_gian_do_frenen(f: dict) -> Optional[Match]:
    return _lookup(f, "phasor_rlc", _FRENEN)


# --------------------------------------------------------------------------
# Điện trường - từ trường
# --------------------------------------------------------------------------
_DIEN_TICH_DIEM = {
    "physics.thpt.dien-tich-dien-truong.dien-truong-dien-tich-diem": (
        {"caption": "E = k|Q| / (ε·r²), hướng ra xa điện tích dương"},
        "cường độ điện trường của điện tích điểm"),
    # Cùng hình đường sức, nhưng công thức nói về ĐIỆN THẾ nên phải đổi cả chú
    # thích lẫn việc bật mặt đẳng thế; để nguyên "E = ..." là dán nhãn sai.
    "physics.thpt.dien-tich-dien-truong.dien-the-dien-tich-diem": (
        {"equipotential": True, "caption": "V = k·Q / (ε·r); mặt đẳng thế là các mặt cầu"},
        "điện thế và mặt đẳng thế quanh điện tích điểm"),
}

_COULOMB = {
    "physics.thpt.dien-tich-dien-truong.dinh-luat-coulomb-chan-khong": (
        {}, "định luật Cu-lông trong chân không"),
    "physics.thpt.dien-tich-dien-truong.dinh-luat-coulomb-dien-moi": (
        {}, "định luật Cu-lông trong điện môi"),
    "physics.dai-hoc.dien-truong.dinh-luat-coulomb-dang-vecto": (
        {}, "định luật Cu-lông dạng vectơ"),
}

_DIEN_TRUONG_DEU = {
    "physics.thpt.tinh-dien-gauss.dien-truong-hai-ban-song-song": (
        {"caption": "E = σ/ε₀ = U/d giữa hai bản tích điện trái dấu"},
        "điện trường giữa hai bản song song"),
    "physics.thpt.dien-tich-dien-truong.lien-he-e-u-d": (
        {}, "liên hệ E = U/d trong điện trường đều"),
    "physics.thpt.dien-tich-dien-truong.cong-cua-luc-dien": (
        {"charge": True, "caption": "A_MN = qEd, với d là hình chiếu đoạn dời lên đường sức"},
        "công của lực điện A = qEd"),
    "physics.thpt.dien-tich-dien-truong.gia-toc-dien-tich-trong-dien-truong-deu": (
        {"charge": True, "caption": "a = |q|E/m = |q|U/(md)"},
        "gia tốc của điện tích trong điện trường đều"),
    "physics.thpt.dien-tich-dien-truong.luc-dien-tac-dung-len-dien-tich": (
        {"charge": True, "caption": "F = qE — điện tích dương chịu lực cùng chiều đường sức"},
        "lực điện F = qE"),
    "physics.thpt.dien-tich-dien-truong.quy-dao-dien-tich-bay-vao-dien-truong": (
        {"trajectory": True, "caption": "y = |q|E·x² / (2mv₀²) — quỹ đạo là một nhánh parabol"},
        "quỹ đạo parabol của điện tích bay vào điện trường đều"),
    "physics.thpt.dien-tich-dien-truong.goc-lech-chum-tia-dien-tich": (
        {"trajectory": True, "caption": "tan α = |q|E·ℓ / (m·v₀²)"},
        "góc lệch của chùm hạt khi ra khỏi bản tụ"),
}

# Ba hình từ trường khác hẳn nhau về hình học, nên tách theo generator ngay ở bảng.
# Ba công thức bậc đại học tổng quát hơn hình vẽ (dây hữu hạn, điểm trên trục
# vòng dây, thêm cuộn toroid); ghi rõ trong ghi chú rằng hình chỉ minh hoạ
# TRƯỜNG HỢP RIÊNG được viết ngay trong công thức, để người biên tập biết mà
# không dùng hình này thay cho phần còn lại.
_TU_TRUONG = {
    "physics.thpt.tu-truong.cam-ung-tu-dong-dien-thang-dai": (
        "field_wire", {}, "từ trường của dòng điện thẳng dài"),
    "physics.dai-hoc.tu-truong.tu-truong-day-thang-dai": (
        "field_wire", {}, "hình vẽ trường hợp dây dài vô hạn của công thức"),
    "physics.thpt.tu-truong.cam-ung-tu-dong-dien-tron": (
        "field_loop", {}, "cảm ứng từ tại tâm dòng điện tròn"),
    "physics.dai-hoc.tu-truong.tu-truong-vong-day-tron": (
        "field_loop", {}, "hình vẽ trường hợp x = 0 (cảm ứng từ tại tâm vòng dây)"),
    "physics.thpt.tu-truong.cam-ung-tu-ong-day": (
        "field_solenoid", {}, "từ trường trong lòng ống dây"),
    "physics.dai-hoc.tu-truong.tu-truong-ong-day-va-toroid": (
        "field_solenoid", {}, "hình vẽ vế ống dây dài; vế toroid chưa có hình"),
}


def r_dien_truong_diem(f: dict) -> Optional[Match]:
    return _lookup(f, "field_point_charge", _DIEN_TICH_DIEM)


def r_luc_coulomb(f: dict) -> Optional[Match]:
    return _lookup(f, "coulomb_two_charges", _COULOMB)


def r_dien_truong_deu(f: dict) -> Optional[Match]:
    return _lookup(f, "field_parallel_plates", _DIEN_TRUONG_DEU)


def r_tu_truong(f: dict) -> Optional[Match]:
    hit = _TU_TRUONG.get(f.get("id", ""))
    if hit is None:
        return None
    gen, params, note = hit
    return gen, dict(params), note


# --------------------------------------------------------------------------
# Quang hình
# --------------------------------------------------------------------------
# d và f chọn sao cho mỗi công thức rơi vào đúng trường hợp mà nó nói tới:
# d > 2f (ảnh thật nhỏ hơn), f < d < 2f (ảnh thật lớn hơn), d < f (ảnh ảo),
# f < 0 (thấu kính phân kì).
_THAU_KINH = {
    "physics.thcs.quang-hoc.cong-thuc-thau-kinh": (
        {"f": 6, "d": 15}, "công thức thấu kính 1/f = 1/d + 1/d′"),
    "physics.thcs.quang-hoc.vi-tri-anh-qua-thau-kinh": (
        {"f": 6, "d": 15}, "vị trí ảnh d′ = df/(d − f)"),
    "physics.thcs.quang-hoc.so-phong-dai-thau-kinh": (
        {"f": 6, "d": 9}, "số phóng đại k = −d′/d"),
    "physics.thcs.quang-hoc.chieu-cao-anh": (
        {"f": 6, "d": 9}, "chiều cao ảnh h′ = |k|·h"),
    "physics.thcs.quang-hoc.khoang-cach-vat-anh": (
        {"f": 6, "d": 15}, "khoảng cách vật - ảnh"),
    "physics.thcs.quang-hoc.thau-kinh-hoi-tu-tao-anh": (
        {"f": 6, "d": 15}, "thấu kính hội tụ, d > 2f: ảnh thật ngược chiều nhỏ hơn"),
    "physics.thcs.quang-hoc.thau-kinh-phan-ki-tao-anh": (
        {"f": -6, "d": 10}, "thấu kính phân kì: luôn cho ảnh ảo cùng chiều nhỏ hơn"),
    "physics.thcs.quang-hoc.may-anh": (
        {"f": 6, "d": 18}, "máy ảnh: vật xa cho ảnh thật ngược chiều trên phim"),
    "physics.thcs.quang-hoc.do-tu-thau-kinh": (
        {"f": 6, "d": 15}, "độ tụ D = 1/f (hình chỉ ra tiêu điểm F, F′)"),
    "physics.thcs.quang-hoc.kinh-lup-so-boi-giac": (
        {"f": 6, "d": 4}, "kính lúp: vật trong tiêu cự, ảnh ảo cùng chiều lớn hơn"),
    "physics.thpt.quang-hinh-quoc-te.thau-kinh-quy-uoc-real-is-positive": (
        {"f": 6, "d": 15}, "công thức thấu kính mỏng, quy ước real-is-positive"),
    "physics.thpt.quang-hinh-quoc-te.thau-kinh-quy-uoc-cartesian": (
        {"f": 6, "d": 15}, "công thức thấu kính, quy ước Descartes"),
}

_PHAN_XA = {
    "physics.thcs.quang-hoc.dinh-luat-phan-xa-anh-sang": (
        {"i": 40}, "định luật phản xạ: i′ = i"),
    "physics.thcs.quang-hoc.goc-giua-tia-toi-va-tia-phan-xa": (
        {"i": 35}, "góc giữa tia tới và tia phản xạ bằng 2i"),
}

_KHUC_XA = {
    "physics.thcs.quang-hoc.dinh-luat-khuc-xa-snell": (
        {"n1": 1.0, "n2": 1.5, "i": 45}, "định luật khúc xạ n₁sin i = n₂sin r"),
    "physics.thpt.song-anh-sang.dinh-luat-khuc-xa": (
        {"n1": 1.0, "n2": 1.5, "i": 45}, "định luật khúc xạ ánh sáng"),
    "physics.thcs.quang-hoc.khuc-xa-anh-sang": (
        {"n1": 1.0, "n2": 1.33, "i": 45}, "không khí → nước: r < i"),
    "physics.thpt.song-anh-sang.phan-xa-toan-phan": (
        {"n1": 1.5, "n2": 1.0, "i": 50}, "i > i_gh: phản xạ toàn phần"),
}


def r_thau_kinh(f: dict) -> Optional[Match]:
    return _lookup(f, "lens_ray", _THAU_KINH)


def r_guong_phang(f: dict) -> Optional[Match]:
    if f.get("id") == "physics.thcs.quang-hoc.anh-qua-guong-phang":
        return "mirror_plane", {"d": 4}, "ảnh ảo đối xứng qua gương phẳng"
    return None


def r_phan_xa(f: dict) -> Optional[Match]:
    return _lookup(f, "reflection_law", _PHAN_XA)


def r_guong_cau(f: dict) -> Optional[Match]:
    if f.get("id") == "physics.thpt.quang-hinh-quoc-te.guong-cau-quy-uoc-quoc-te":
        return "mirror_spherical", {"f": 6, "so": 15}, "gương cầu lõm, vật ngoài tâm C"
    return None


def r_khuc_xa(f: dict) -> Optional[Match]:
    return _lookup(f, "refraction", _KHUC_XA)


# --------------------------------------------------------------------------
# Nhiệt học
# --------------------------------------------------------------------------
_PV = {
    "physics.thpt.chat-khi.dinh-luat-boyle": (
        {"process": "isothermal"}, "đẳng nhiệt: pV = const"),
    "physics.thpt.chat-khi.dinh-luat-charles": (
        {"process": "isobaric"}, "đẳng áp: V/T = const"),
    "physics.thpt.chat-khi.dinh-luat-gay-lussac": (
        {"process": "isochoric"}, "đẳng tích: p/T = const"),
    "physics.thpt.nhiet-dong-luc-hoc.qua-trinh-dang-nhiet": (
        {"process": "isothermal", "work": True}, "nguyên lí I cho quá trình đẳng nhiệt"),
    "physics.thpt.nhiet-dong-luc-hoc.qua-trinh-dang-ap": (
        {"process": "isobaric", "work": True}, "nguyên lí I cho quá trình đẳng áp"),
    "physics.thpt.nhiet-dong-luc-hoc.qua-trinh-dang-tich": (
        {"process": "isochoric"}, "đẳng tích: A = 0 nên ΔU = Q"),
    "physics.thpt.nhiet-dong-luc-hoc.qua-trinh-doan-nhiet": (
        {"process": "adiabatic"}, "nguyên lí I cho quá trình đoạn nhiệt"),
    "physics.thpt.nhiet-dong-luc-hoc.phuong-trinh-poisson": (
        {"process": "adiabatic"}, "phương trình Poisson pVᵞ = const"),
    "physics.dai-hoc.nhiet-hoc.qua-trinh-doan-nhiet-poisson": (
        {"process": "adiabatic"}, "quá trình đoạn nhiệt"),
    "physics.thpt.nhiet-dong-luc-hoc.cong-cua-khi-dang-ap": (
        {"process": "isobaric", "work": True}, "công của khí trong quá trình đẳng áp"),
    "physics.thpt.nhiet-dong-luc-hoc.cong-cua-khi-dang-nhiet": (
        {"process": "isothermal", "work": True}, "công của khí trong quá trình đẳng nhiệt"),
    # Công thức nói "quá trình bất kì"; hình buộc phải chọn một đường cụ thể,
    # nên chú thích phải nói rõ đó chỉ là ví dụ, không phải điều kiện.
    "physics.thpt.nhiet-dong-luc-hoc.cong-tong-quat-cua-khi": (
        {"process": "isothermal", "work": True,
         "caption": "A′ = diện tích dưới đường quá trình (ví dụ: một đường đẳng nhiệt)"},
        "công bằng diện tích dưới đường p-V"),
    "physics.thpt.nhiet-dong-luc-hoc.cong-trong-qua-trinh-doan-nhiet": (
        {"process": "adiabatic", "work": True}, "công của khí trong quá trình đoạn nhiệt"),
    "physics.dai-hoc.nhiet-hoc.cong-trong-cac-qua-trinh": (
        {"process": "all"}, "so sánh công của bốn quá trình cơ bản"),
    "physics.dai-hoc.nhiet-hoc.cong-trong-qua-trinh-doan-nhiet": (
        {"process": "adiabatic", "work": True}, "công trong quá trình đoạn nhiệt"),
    "physics.thpt.intl-nhiet-hoc.dien-tich-gian-do-pv": (
        {"process": "cycle"}, "công của chu trình bằng diện tích hình kín"),
    "physics.thpt.intl-nhiet-hoc.doan-nhiet-khi-don-nguyen-tu-ib": (
        {"process": "adiabatic", "gamma": 5 / 3}, "đoạn nhiệt khí đơn nguyên tử, γ = 5/3"),
    "physics.dai-hoc.nhiet-hoc.qua-trinh-da-bien": (
        {"process": "polytropic", "n": 1.2}, "quá trình đa biến pVⁿ = const"),
}

_CARNOT = {
    "physics.dai-hoc.nhiet-hoc.chu-trinh-carnot": ({}, "hiệu suất chu trình Carnot"),
    "physics.thpt.nhiet-dong-luc-hoc.hieu-suat-chu-trinh-carnot": (
        {}, "hiệu suất cực đại H = 1 − T₂/T₁"),
    "physics.thpt.nhiet-dong-luc-hoc.he-thuc-nhiet-luong-carnot": (
        {}, "hệ thức Q₁/T₁ = |Q₂|/T₂ của chu trình Carnot"),
    "physics.thpt.intl-nhiet-hoc.hieu-suat-carnot-ib": (
        {}, "giới hạn Carnot cho hiệu suất động cơ nhiệt"),
}

# Máy lạnh KHÔNG phải động cơ nhiệt vẽ ngược nhãn: cả ba dòng năng lượng đều
# đảo chiều, nên tách hẳn thành mode riêng.
_DONG_CO_NHIET = {
    "physics.thcs.nhiet-hoc.hieu-suat-dong-co-nhiet": ("engine", "hiệu suất động cơ nhiệt"),
    "physics.thpt.nhiet-dong-luc-hoc.hieu-suat-dong-co-nhiet": ("engine", "hiệu suất động cơ nhiệt"),
    "physics.dai-hoc.nhiet-hoc.hieu-suat-dong-co-nhiet": ("engine", "hiệu suất động cơ nhiệt"),
    "physics.thpt.intl-nhiet-hoc.hieu-suat-dong-co-nhiet-ib": ("engine", "hiệu suất động cơ nhiệt"),
    "physics.thpt.nhiet-dong-luc-hoc.hieu-nang-may-lanh": ("fridge", "hiệu năng máy lạnh"),
    "physics.thpt.nhiet-dong-luc-hoc.hieu-nang-bom-nhiet": ("fridge", "hiệu năng bơm nhiệt"),
    "physics.dai-hoc.nhiet-hoc.he-so-lam-lanh-va-bom-nhiet": (
        "fridge", "hệ số làm lạnh và hệ số bơm nhiệt"),
}


def r_gian_do_pv(f: dict) -> Optional[Match]:
    return _lookup(f, "pv_diagram", _PV)


def r_chu_trinh_carnot(f: dict) -> Optional[Match]:
    return _lookup(f, "carnot_cycle", _CARNOT)


def r_dong_co_nhiet(f: dict) -> Optional[Match]:
    hit = _DONG_CO_NHIET.get(f.get("id", ""))
    if hit is None:
        return None
    mode, note = hit
    return "heat_engine", {"mode": mode}, note


# --------------------------------------------------------------------------
# Hạt nhân
# --------------------------------------------------------------------------
# ``quantity`` đổi ký hiệu trên trục tung: N, m và H giảm theo cùng một quy luật
# nhưng dán nhãn "N/N₀" cạnh công thức độ phóng xạ là đổi tên đại lượng.
_PHONG_XA = {
    "physics.thpt.hat-nhan.dinh-luat-phong-xa-so-hat": (
        {"quantity": "N"}, "định luật phóng xạ theo số hạt nhân"),
    "physics.thpt.hat-nhan.dinh-luat-phong-xa-khoi-luong": (
        {"quantity": "m"}, "định luật phóng xạ theo khối lượng"),
    "physics.thpt.hat-nhan.do-phong-xa": (
        {"quantity": "H"}, "độ phóng xạ giảm theo cùng quy luật với N"),
    "physics.thpt.hat-nhan.hang-so-phong-xa": (
        {"quantity": "N"}, "hằng số phóng xạ λ = ln2 / T"),
    "physics.thpt.hat-nhan.xac-dinh-tuoi-co-vat": (
        {"quantity": "N"}, "xác định tuổi cổ vật từ tỉ số N₀/N"),
    "physics.thpt.hat-nhan.so-hat-nhan-da-phan-ra": (
        {"quantity": "N", "daughter": True},
        "số hạt nhân đã phân rã ΔN = N₀(1 − 2^(−t/T))"),
    "physics.thpt.hat-nhan.ti-le-hat-nhan-me-con": (
        {"quantity": "N", "daughter": True}, "tỉ lệ số hạt nhân con trên hạt nhân mẹ"),
}

_SO_DO_PHAN_RA = {
    "physics.thpt.hat-nhan.phong-xa-alpha": ({"kind": "alpha"}, "phóng xạ α: Z giảm 2, N giảm 2"),
    "physics.thpt.hat-nhan.phong-xa-beta-tru": ({"kind": "beta-"}, "phóng xạ β⁻: Z tăng 1, N giảm 1"),
    "physics.thpt.hat-nhan.phong-xa-beta-cong": ({"kind": "beta+"}, "phóng xạ β⁺: Z giảm 1, N tăng 1"),
    "physics.thpt.hat-nhan.phong-xa-gamma": ({"kind": "gamma"}, "phóng xạ γ: A và Z không đổi"),
}


def r_duong_phong_xa(f: dict) -> Optional[Match]:
    return _lookup(f, "decay_curve", _PHONG_XA)


def r_so_do_phan_ra(f: dict) -> Optional[Match]:
    return _lookup(f, "decay_scheme", _SO_DO_PHAN_RA)


RULES: list[Rule] = [
    r_mach_noi_tiep, r_dinh_luat_om, r_mach_song_song, r_toan_mach,
    r_mach_xoay_chieu, r_gian_do_frenen,
    r_dien_truong_diem, r_luc_coulomb, r_dien_truong_deu, r_tu_truong,
    r_thau_kinh, r_guong_phang, r_phan_xa, r_guong_cau, r_khuc_xa,
    r_gian_do_pv, r_chu_trinh_carnot, r_dong_co_nhiet,
    r_duong_phong_xa, r_so_do_phan_ra,
]
