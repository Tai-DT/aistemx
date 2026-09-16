"""Tự động gán generator 2D cho công thức (rule-based, ưu tiên độ chính xác).

Chỉ khớp khi tín hiệu chắc chắn (đoạn slug trong ``id`` — vốn là ASCII ổn định — hoặc
chữ ký LaTeX rõ ràng). Nhánh nào không chắc thì bỏ, nhường cho ``bindings.json`` thủ công.
Mỗi rule trả ``(generator, params, note)``. ``match_formula`` trả rule đầu tiên trúng.
"""

from __future__ import annotations

import re
from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _has(f: dict, *subs: str) -> bool:
    return any(s in f["id"] for s in subs)


def _latex_norm(f: dict) -> str:
    return re.sub(r"\s+", "", f.get("latex", ""))


# -- các rule (thứ tự = độ ưu tiên) ---------------------------------------
def r_pythagoras(f: dict) -> Optional[Match]:
    if _has(f, "he-thuc-luong.dinh-li-pytago"):
        return "right_triangle", {"b": 4, "c": 3, "pythagoras": True,
                                   "label_hyp": "a", "label_base": "b", "label_height": "c"}, "định lí Pytago"
    # khớp CHÍNH XÁC dạng thuần Pytago — tránh nuốt nhầm định lí cosin
    # (a² = b² + c² − 2bc·cosA) vốn có tiền tố y hệt.
    lx = _latex_norm(f)
    if lx in {"a^{2}=b^{2}+c^{2}", "a^2=b^2+c^2", "c^{2}=a^{2}+b^{2}", "c^2=a^2+b^2"}:
        return "right_triangle", {"b": 4, "c": 3, "pythagoras": True,
                                  "label_hyp": "a", "label_base": "b", "label_height": "c"}, "hệ thức Pytago"
    return None


def r_right_triangle_area(f: dict) -> Optional[Match]:
    if _has(f, "dien-tich-tam-giac-vuong"):
        return "right_triangle", {"b": 4, "c": 3, "label_hyp": "a", "label_base": "b", "label_height": "c"}, "S tam giác vuông"
    return None


def r_triangle_area(f: dict) -> Optional[Match]:
    if _has(f, "dien-tich.dien-tich-tam-giac") and "vuong" not in f["id"] and "deu" not in f["id"]:
        return "triangle", {"base": 6, "height": 4}, "S tam giác = ½·đáy·cao"
    return None


def r_circle(f: dict) -> Optional[Match]:
    if _has(f, "dien-tich-hinh-tron", "chu-vi-hinh-tron", "duong-tron.chu-vi", "duong-tron.dien-tich-hinh-tron"):
        return "circle", {"R": 3}, "đường tròn"
    if f["id"].endswith("hinh-hoc-phang.chu-vi-hinh-tron"):
        return "circle", {"R": 3}, "chu vi hình tròn"
    return None


def r_rectangle(f: dict) -> Optional[Match]:
    if _has(f, "dien-tich-hinh-chu-nhat", "chu-vi-hinh-chu-nhat"):
        return "rectangle", {"a": 5, "b": 3}, "hình chữ nhật"
    return None


def r_parallelogram(f: dict) -> Optional[Match]:
    if _has(f, "dien-tich-hinh-binh-hanh", "chu-vi-hinh-binh-hanh") and "oxyz" not in f["id"] and "oxy-" not in f["id"]:
        return "parallelogram", {"a": 5, "height": 3}, "hình bình hành"
    return None


def r_trapezoid(f: dict) -> Optional[Match]:
    if _has(f, "dien-tich-hinh-thang"):
        return "trapezoid", {"a": 6, "b": 3.4, "height": 3}, "hình thang"
    return None


def r_linear_graph(f: dict) -> Optional[Match]:
    if _has(f, "ham-so-bac-nhat.do-thi", "ham-so-bac-nhat.dinh-nghia"):
        return "function_plot", {"expr": "0.8*x+1", "xmin": -4, "xmax": 4, "label": "y = ax + b"}, "đồ thị hàm bậc nhất"
    return None


def r_parabola_graph(f: dict) -> Optional[Match]:
    if _has(f, "ham-so-bac-hai.do-thi-parabol"):
        return "function_plot", {"expr": "x^2", "xmin": -3, "xmax": 3, "label": "y = ax² + bx + c"}, "parabol"
    return None


def r_projectile(f: dict) -> Optional[Match]:
    if _has(f, "dong-hoc.nem-xien-phuong-trinh-quy-dao", "dong-hoc.nem-xien-do-cao-cuc-dai",
            "dong-hoc.nem-xien-tam-xa", "dong-hoc.nem-xien-goc-nem-toi-uu"):
        return "projectile", {"v0": 22, "angle": 45}, "ném xiên"
    return None


RULES: list[Rule] = [
    r_pythagoras, r_right_triangle_area, r_triangle_area, r_circle,
    r_rectangle, r_parallelogram, r_trapezoid,
    r_linear_graph, r_parabola_graph, r_projectile,
]


def match_formula(f: dict) -> Optional[Match]:
    for rule in RULES:
        m = rule(f)
        if m:
            return m
    return None
