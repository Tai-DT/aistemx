"""Luật gán generator cho sóng ánh sáng và quang hình (Giao thoa Y-âng & Lăng kính).

Khớp chính xác từng định danh công thức thuộc chủ đề `physics.thpt.song-anh-sang.*`.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


def r_young_interference(f: dict) -> Optional[Match]:
    if _tail(f, "song-anh-sang.khoang-van",
             "song-anh-sang.khoang-cach-giua-hai-van",
             "song-anh-sang.so-van-tren-truong-giao-thoa",
             "song-anh-sang.giao-thoa-trong-moi-truong-chiet-suat",
             "song-anh-sang.be-rong-quang-pho-bac-k"):
        return "young_interference", {"mode": "fringe_spacing"}, "khoảng vân trong giao thoa Y-âng i = λD/a"
    if _tail(f, "song-anh-sang.vi-tri-van-sang",
             "song-anh-sang.buoc-song-cho-van-sang-tai-diem"):
        return "young_interference", {"mode": "bright"}, "vị trí vân sáng x_s = k·i"
    if _tail(f, "song-anh-sang.vi-tri-van-toi",
             "song-anh-sang.buoc-song-cho-van-toi-tai-diem"):
        return "young_interference", {"mode": "dark"}, "vị trí vân tối x_t = (k + ½)i"
    if _tail(f, "song-anh-sang.hieu-duong-di-y-ang"):
        return "young_interference", {"mode": "path_diff"}, "hiệu đường đi trong thí nghiệm Y-âng: d₂ − d₁ = ax/D"
    if _tail(f, "song-anh-sang.van-trung-hai-buc-xa"):
        return "young_interference", {"mode": "two_wavelengths"}, "vân sáng trùng nhau k₁λ₁ = k₂λ₂"
    return None


def r_prism_refraction(f: dict) -> Optional[Match]:
    if _tail(f, "song-anh-sang.cong-thuc-lang-kinh",
             "song-anh-sang.lang-kinh-goc-lech-cuc-tieu",
             "song-anh-sang.lang-kinh-goc-nho"):
        return "prism_refraction", {}, "đường truyền tia sáng qua lăng kính: A = r₁ + r₂, D = i₁ + i₂ − A"
    if _tail(f, "song-anh-sang.tan-sac-anh-sang",
             "song-anh-sang.goc-lech-do-tim-qua-lang-kinh"):
        return "prism_dispersion", {}, "hiện tượng tán sắc ánh sáng qua lăng kính: n_tím > n_đỏ"
    return None


RULES: list[Rule] = [
    r_young_interference,
    r_prism_refraction,
]
