"""Luật gán generator cho 3 đường conic (Elip, Hypebol, Parabol).

Khớp chính xác từng định danh công thức thuộc chủ đề `math.thpt.oxy-conic.*`.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


def r_conic_ellipse(f: dict) -> Optional[Match]:
    if _tail(f, "oxy-conic.elip-pt-chinh-tac"):
        return "conic_ellipse", {}, "phương trình chính tắc của elip x²/a² + y²/b² = 1"
    if _tail(f, "oxy-conic.elip-dinh-truc"):
        return "conic_ellipse", {"show_m": False}, "các đỉnh và độ dài hai trục của elip"
    if _tail(f, "oxy-conic.elip-tieu-cu"):
        return "conic_ellipse", {"show_m": False}, "tiêu điểm và tiêu cự của elip: c² = a² − b²"
    if _tail(f, "oxy-conic.elip-tam-sai"):
        return "conic_ellipse", {}, "tâm sai của elip e = c/a (0 < e < 1)"
    if _tail(f, "oxy-conic.elip-ban-kinh-qua-tieu"):
        return "conic_ellipse", {"show_m": True}, "bán kính qua tiêu MF₁ = a + ex, MF₂ = a − ex"
    if _tail(f, "oxy-conic.elip-duong-chuan"):
        return "conic_ellipse", {"show_directrix": True}, "đường chuẩn của elip x = ±a/e"
    if _tail(f, "oxy-conic.elip-dien-tich"):
        return "conic_ellipse", {"show_area": True, "show_m": False}, "diện tích hình elip S = π·a·b"
    if _tail(f, "oxy-conic.dinh-nghia-conic-theo-duong-chuan"):
        return "conic_ellipse", {"show_directrix": True}, "định nghĩa chung conic: MF/d(M,Δ) = e"
    return None


def r_conic_hyperbola(f: dict) -> Optional[Match]:
    if _tail(f, "oxy-conic.hypebol-pt-chinh-tac"):
        return "conic_hyperbola", {}, "phương trình chính tắc của hypebol x²/a² − y²/b² = 1"
    if _tail(f, "oxy-conic.hypebol-tiem-can"):
        return "conic_hyperbola", {"show_asymptotes": True, "show_m": False}, "đường tiệm cận của hypebol y = ±(b/a)x"
    if _tail(f, "oxy-conic.hypebol-tieu-cu"):
        return "conic_hyperbola", {"show_m": False}, "tiêu điểm và tiêu cự của hypebol: c² = a² + b²"
    if _tail(f, "oxy-conic.hypebol-tam-sai"):
        return "conic_hyperbola", {}, "tâm sai của hypebol e = c/a > 1"
    if _tail(f, "oxy-conic.hypebol-ban-kinh-qua-tieu"):
        return "conic_hyperbola", {"show_m": True}, "bán kính qua tiêu của hypebol |MF₁ − MF₂| = 2a"
    if _tail(f, "oxy-conic.hypebol-duong-chuan"):
        return "conic_hyperbola", {"show_directrix": True}, "đường chuẩn của hypebol x = ±a/e"
    return None


def r_conic_parabola(f: dict) -> Optional[Match]:
    if _tail(f, "oxy-conic.parabol-pt-chinh-tac"):
        return "conic_parabola", {}, "phương trình chính tắc của parabol y² = 2px"
    if _tail(f, "oxy-conic.parabol-tieu-diem"):
        return "conic_parabola", {}, "tiêu điểm parabol F(p/2; 0)"
    if _tail(f, "oxy-conic.parabol-duong-chuan"):
        return "conic_parabola", {}, "đường chuẩn parabol Δ: x = −p/2"
    if _tail(f, "oxy-conic.parabol-tieu-diem-duong-chuan"):
        return "conic_parabola", {}, "tiêu điểm F(p/2; 0) và đường chuẩn Δ: x = −p/2"
    if _tail(f, "oxy-conic.parabol-ban-kinh-qua-tieu"):
        return "conic_parabola", {"show_point_m": True}, "bán kính qua tiêu của parabol MF = x + p/2"
    if _tail(f, "oxy-conic.parabol-tam-sai"):
        return "conic_parabola", {}, "tâm sai của parabol e = 1"
    return None


RULES: list[Rule] = [
    r_conic_ellipse,
    r_conic_hyperbola,
    r_conic_parabola,
]
