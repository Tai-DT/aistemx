"""Luật gán generator cho Trường hấp dẫn & Định luật Kepler (Vật lí THPT / AP / IB).

Ánh xạ chuẩn xác các công thức vạn vật hấp dẫn, vệ tinh, thế năng hấp dẫn và 3 định luật Kepler
vào các generator trong `gen_hapdan.py`.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


def r_kepler(f: dict) -> Optional[Match]:
    """Các định luật Kepler về chuyển động thiên thể."""
    if _tail(f, "intl-hap-dan.kepler-dinh-luat-i"):
        return "kepler_orbit", {"mode": "kepler1"}, "định luật I Kepler: quỹ đạo elip quanh Mặt Trời tại một tiêu điểm"
    if _tail(f, "intl-hap-dan.kepler-dinh-luat-ii"):
        return "kepler_orbit", {"mode": "kepler2"}, "định luật II Kepler: bán kính vectơ quét diện tích bằng nhau trong cùng thời gian"
    if _tail(f, "intl-hap-dan.kepler-dinh-luat-iii"):
        return "kepler_orbit", {"mode": "kepler3"}, "định luật III Kepler: tỉ số T²/a³ là hằng số đối với mọi hành tinh"
    return None


def r_gravitational_field(f: dict) -> Optional[Match]:
    """Trường hấp dẫn, định luật vạn vật hấp dẫn và chuyển động vệ tinh."""
    if _tail(f, "dong-luc-hoc.dinh-luat-van-vat-hap-dan"):
        return "gravitational_field", {"mode": "newton_law"}, "định luật vạn vật hấp dẫn F = G·m₁m₂/r²"
    if _tail(f, "intl-hap-dan.cuong-do-truong-hap-dan"):
        return "gravitational_field", {"mode": "newton_law"}, "cường độ trường hấp dẫn g = G·M/r²"
    if _tail(f, "intl-hap-dan.the-nang-hap-dan-hai-vat-ib",
             "cong-nang-luong.the-nang-hap-dan-tong-quat"):
        return "gravitational_field", {"mode": "newton_law"}, "thế năng hấp dẫn W_t = -G·Mm/r"
    if _tail(f, "intl-hap-dan.the-hap-dan"):
        return "gravitational_field", {"mode": "newton_law"}, "thế hấp dẫn V = -G·M/r"
    if _tail(f, "intl-hap-dan.cong-di-chuyen-trong-truong-hap-dan"):
        return "gravitational_field", {"mode": "newton_law"}, "công dịch chuyển vật trong trường hấp dẫn"
    if _tail(f, "intl-hap-dan.lien-he-g-va-the-hap-dan"):
        return "gravitational_field", {"mode": "newton_law"}, "liên hệ giữa cường độ trường và gradient thế hấp dẫn g = -dV/dr"
    if _tail(f, "intl-hap-dan.co-nang-ve-tinh"):
        return "gravitational_field", {"mode": "satellite"}, "cơ năng toàn phần của vệ tinh trên quỹ đạo tròn W = -G·Mm/(2r)"
    if _tail(f, "intl-hap-dan.quy-dao-dia-tinh"):
        return "gravitational_field", {"mode": "satellite"}, "bán kính quỹ đạo vệ tinh địa tĩnh"
    if _tail(f, "intl-hap-dan.toc-do-quy-dao-ib"):
        return "gravitational_field", {"mode": "satellite"}, "tốc độ quỹ đạo tròn v = √(G·M/r)"
    if _tail(f, "intl-hap-dan.toc-do-thoat-ib"):
        return "gravitational_field", {"mode": "satellite"}, "tốc độ thoát khỏi trường hấp dẫn v = √(2G·M/r)"
    if _tail(f, "intl-hap-dan.truong-hap-dan-ben-trong-qua-cau"):
        return "gravitational_field", {"mode": "satellite"}, "cường độ trường hấp dẫn bên trong quả cầu đồng chất (định lí vỏ cầu)"
    return None


RULES: list[Rule] = [
    r_kepler,
    r_gravitational_field,
]
