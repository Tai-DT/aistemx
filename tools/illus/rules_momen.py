"""Luật gán generator cho Cân bằng vật rắn & Mômen lực (Vật lí 10).

Ánh xạ chuẩn xác các công thức mômen lực, đòn bẩy, ngẫu lực, hợp lực song song
và cân bằng ba lực vào các generator trong `gen_momen.py`.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


def r_torque_moment(f: dict) -> Optional[Match]:
    """Mômen lực và ngẫu lực."""
    if _tail(f, "can-bang-vat-ran.momen-luc"):
        return "torque_moment", {"mode": "single"}, "mômen lực M = F·d đối với trục quay"
    if _tail(f, "can-bang-vat-ran.ngau-luc"):
        return "torque_moment", {"mode": "couple"}, "mômen của ngẫu lực M = F·d"
    return None


def r_lever_balance(f: dict) -> Optional[Match]:
    """Đòn bẩy, quy tắc mômen và hợp lực song song."""
    if _tail(f, "can-bang-vat-ran.don-bay"):
        return "lever_balance", {"mode": "lever"}, "điều kiện cân bằng của đòn bẩy F₁d₁ = F₂d₂"
    if _tail(f, "can-bang-vat-ran.quy-tac-momen-luc"):
        return "lever_balance", {"mode": "lever"}, "quy tắc mômen lực: tổng mômen làm quay theo chiều kim đồng hồ bằng ngược chiều"
    if _tail(f, "can-bang-vat-ran.hop-luc-song-song-cung-chieu"):
        return "lever_balance", {"mode": "parallel_forces"}, "hợp hai lực song song cùng chiều F = F₁ + F₂, F₁d₁ = F₂d₂"
    if _tail(f, "can-bang-vat-ran.hop-luc-song-song-nguoc-chieu"):
        return "lever_balance", {"mode": "parallel_forces"}, "hợp hai lực song song ngược chiều F = |F₁ - F₂|, F₁d₁ = F₂d₂"
    if _tail(f, "can-bang-vat-ran.trong-tam-he-chat-diem"):
        return "lever_balance", {"mode": "parallel_forces"}, "tọa độ trọng tâm của hệ chất điểm theo quy tắc hợp lực song song"
    return None


def r_equilibrium_3forces(f: dict) -> Optional[Match]:
    """Cân bằng ba lực không song song và điều kiện cân bằng tổng quát."""
    if _tail(f, "can-bang-vat-ran.can-bang-ba-luc-khong-song-song"):
        return "equilibrium_3forces", {}, "cân bằng của vật rắn chịu tác dụng của ba lực không song song (đồng quy)"
    if _tail(f, "can-bang-vat-ran.dieu-kien-can-bang-chat-diem"):
        return "equilibrium_3forces", {}, "điều kiện cân bằng của chất điểm: tổng hợp lực bằng không"
    if _tail(f, "can-bang-vat-ran.dieu-kien-can-bang-tong-quat"):
        return "equilibrium_3forces", {}, "điều kiện cân bằng tổng quát của vật rắn: tổng lực bằng 0 và tổng mômen bằng 0"
    if _tail(f, "can-bang-vat-ran.dieu-kien-can-bang-mat-chan-de"):
        return "equilibrium_3forces", {}, "điều kiện cân bằng của vật có mặt chân đế: giá của trọng lực rơi vào mặt chân đế"
    return None


RULES: list[Rule] = [
    r_torque_moment,
    r_lever_balance,
    r_equilibrium_3forces,
]
