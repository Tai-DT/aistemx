"""Generator SVG cho 3 đường conic trong hình học toạ độ Oxy: Elip, Hypebol, Parabol.

Mọi toạ độ và tiêu cự được tính chuẩn xác theo công thức hình học giải tích:
- Elip: x²/a² + y²/b² = 1 (a > b > 0, c² = a² − b², e = c/a < 1)
- Hypebol: x²/a² − y²/b² = 1 (c² = a² + b², tiệm cận y = ±(b/a)x, e = c/a > 1)
- Parabol: y² = 2px (tiêu điểm F(p/2; 0), đường chuẩn Δ: x = −p/2)
"""

from __future__ import annotations

import math
from typing import Callable

from .svgkit import Canvas, _n

Params = dict


def _f(val, default: float) -> float:
    try:
        v = float(val)
        return v if math.isfinite(v) else default
    except (TypeError, ValueError):
        return default


def build_conic_ellipse(p: Params) -> str:
    """Đồ thị Elip chính tắc x²/a² + y²/b² = 1 với tiêu điểm, các đỉnh, bán kính qua tiêu."""
    a = max(_f(p.get("a", 140), 140.0), 50.0)
    b = max(_f(p.get("b", 85), 85.0), 30.0)
    if b >= a:
        b = a * 0.65
    c = math.sqrt(a * a - b * b)

    show_foci = bool(p.get("show_foci", True))
    show_vertices = bool(p.get("show_vertices", True))
    show_directrix = bool(p.get("show_directrix", False))
    show_m = bool(p.get("show_m", True))
    show_area = bool(p.get("show_area", False))

    w, h = 480.0, 320.0
    ox, oy = w / 2.0, h / 2.0

    cv = Canvas(w, h, title="Đường Elip chính tắc",
                desc=f"Elip có phương trình x²/{int(a)}² + y²/{int(b)}² = 1 với hai tiêu điểm F₁, F₂ và bốn đỉnh A₁, A₂, B₁, B₂.")

    # Trục toạ độ
    cv.arrow(30, oy, w - 25, oy, cls="axis", head=7)
    cv.arrow(ox, h - 25, ox, 25, cls="axis", head=7)
    cv.text(w - 28, oy - 9, "x", cls="lbl-sm", anchor="end")
    cv.text(ox + 9, 32, "y", cls="lbl-sm")
    cv.text(ox - 8, oy + 16, "O", cls="lbl", anchor="end")

    # Đường chuẩn x = -a²/c và x = a²/c nếu cần
    if show_directrix and c > 0:
        d_val = (a * a) / c
        if d_val < ox - 40:
            cv.line(ox - d_val, 35, ox - d_val, h - 35, cls="accent-c", extra=' stroke-dasharray="4 3"')
            cv.line(ox + d_val, 35, ox + d_val, h - 35, cls="accent-c", extra=' stroke-dasharray="4 3"')
            cv.text(ox - d_val - 4, 45, "Δ₁: x = -a²/c", cls="lbl-sm", anchor="end")
            cv.text(ox + d_val + 4, 45, "Δ₂: x = a²/c", cls="lbl-sm", anchor="start")

    # Đường Elip
    pts = []
    for deg in range(361):
        rad = math.radians(deg)
        pts.append((ox + a * math.cos(rad), oy - b * math.sin(rad)))

    if show_area:
        cv.polygon(pts, cls="fill-a")
        cv.text(ox, oy - 20, "S = π·a·b", cls="lbl", anchor="middle")

    cv.polyline(pts, cls="curve")

    # Tiêu điểm F₁(-c; 0), F₂(c; 0)
    if show_foci:
        cv.dot(ox - c, oy, r=3.4, cls="accent-b")
        cv.dot(ox + c, oy, r=3.4, cls="accent-b")
        cv.text(ox - c, oy + 18, "F₁(-c;0)", cls="lbl-sm", anchor="middle")
        cv.text(ox + c, oy + 18, "F₂(c;0)", cls="lbl-sm", anchor="middle")

    # Các đỉnh
    if show_vertices:
        cv.dot(ox - a, oy, r=2.8, cls="ink")
        cv.dot(ox + a, oy, r=2.8, cls="ink")
        cv.dot(ox, oy - b, r=2.8, cls="ink")
        cv.dot(ox, oy + b, r=2.8, cls="ink")
        cv.text(ox - a - 4, oy - 8, "A₁(-a;0)", cls="lbl-sm", anchor="end")
        cv.text(ox + a + 4, oy - 8, "A₂(a;0)", cls="lbl-sm", anchor="start")
        cv.text(ox - 8, oy - b - 7, "B₂(0;b)", cls="lbl-sm", anchor="end")
        cv.text(ox - 8, oy + b + 15, "B₁(0;-b)", cls="lbl-sm", anchor="end")

    # Điểm M và các bán kính qua tiêu MF₁, MF₂
    if show_m and show_foci:
        ang_m = math.radians(52.0)
        mx, my = ox + a * math.cos(ang_m), oy - b * math.sin(ang_m)
        cv.line(ox - c, oy, mx, my, cls="accent-b", extra=' stroke-dasharray="4 3"')
        cv.line(ox + c, oy, mx, my, cls="accent-b", extra=' stroke-dasharray="4 3"')
        cv.dot(mx, my, r=3.6, cls="accent-a")
        cv.text(mx + 7, my - 6, "M(x;y)", cls="lbl")
        cv.text((ox - c + mx) / 2.0 - 8, (oy + my) / 2.0 - 6, "MF₁", cls="lbl-sm")
        cv.text((ox + c + mx) / 2.0 + 8, (oy + my) / 2.0 - 6, "MF₂", cls="lbl-sm")
        cv.text(ox, h - 10, "MF₁ + MF₂ = 2a  (c² = a² − b²)", cls="lbl-sm", anchor="middle")

    return cv.render()


def build_conic_hyperbola(p: Params) -> str:
    """Đồ thị Hypebol chính tắc x²/a² − y²/b² = 1 với tiệm cận và tiêu điểm."""
    a = max(_f(p.get("a", 72), 72.0), 30.0)
    b = max(_f(p.get("b", 56), 56.0), 25.0)
    c = math.sqrt(a * a + b * b)

    show_foci = bool(p.get("show_foci", True))
    show_asymptotes = bool(p.get("show_asymptotes", True))
    show_directrix = bool(p.get("show_directrix", False))
    show_m = bool(p.get("show_m", True))

    w, h = 480.0, 320.0
    ox, oy = w / 2.0, h / 2.0

    cv = Canvas(w, h, title="Đường Hypebol chính tắc",
                desc="Hypebol x²/a² − y²/b² = 1 với hai nhánh đối xứng qua Oy và hai đường tiệm cận y = ±(b/a)x.")

    # Trục toạ độ
    cv.arrow(25, oy, w - 20, oy, cls="axis", head=7)
    cv.arrow(ox, h - 25, ox, 25, cls="axis", head=7)
    cv.text(w - 24, oy - 9, "x", cls="lbl-sm", anchor="end")
    cv.text(ox + 9, 32, "y", cls="lbl-sm")
    cv.text(ox - 8, oy + 16, "O", cls="lbl", anchor="end")

    # Hai đường tiệm cận y = ±(b/a)x
    if show_asymptotes:
        slope = b / a
        x_span = min(ox - 35, 175.0)
        cv.line(ox - x_span, oy + slope * x_span, ox + x_span, oy - slope * x_span,
                cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.line(ox - x_span, oy - slope * x_span, ox + x_span, oy + slope * x_span,
                cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.text(ox + x_span - 8, oy - slope * x_span - 7, "y = (b/a)x", cls="lbl-sm", anchor="start")
        cv.text(ox + x_span - 8, oy + slope * x_span + 14, "y = -(b/a)x", cls="lbl-sm", anchor="start")

    # Nhánh phải của hypebol: x = a/cos(t), y = b*tan(t)
    pts_r = []
    for deg in range(-68, 69, 2):
        rad = math.radians(deg)
        x = a / math.cos(rad)
        y = b * math.tan(rad)
        if x < ox - 35:
            pts_r.append((ox + x, oy - y))

    if pts_r:
        cv.polyline(pts_r, cls="curve")
        # Nhánh trái đối xứng qua gốc O
        pts_l = [(2.0 * ox - px, py) for px, py in pts_r]
        cv.polyline(pts_l, cls="curve")

    # Đường chuẩn nếu cần
    if show_directrix and c > 0:
        d_val = (a * a) / c
        cv.line(ox - d_val, 35, ox - d_val, h - 35, cls="accent-c", extra=' stroke-dasharray="4 3"')
        cv.line(ox + d_val, 35, ox + d_val, h - 35, cls="accent-c", extra=' stroke-dasharray="4 3"')
        cv.text(ox - d_val - 4, 45, "Δ₁", cls="lbl-sm", anchor="end")
        cv.text(ox + d_val + 4, 45, "Δ₂", cls="lbl-sm", anchor="start")

    # Tiêu điểm F₁(-c; 0), F₂(c; 0)
    if show_foci:
        cv.dot(ox - c, oy, r=3.4, cls="accent-b")
        cv.dot(ox + c, oy, r=3.4, cls="accent-b")
        cv.text(ox - c, oy + 18, "F₁(-c;0)", cls="lbl-sm", anchor="middle")
        cv.text(ox + c, oy + 18, "F₂(c;0)", cls="lbl-sm", anchor="middle")

    # Các đỉnh A₁(-a; 0), A₂(a; 0)
    cv.dot(ox - a, oy, r=2.8, cls="ink")
    cv.dot(ox + a, oy, r=2.8, cls="ink")
    cv.text(ox - a - 4, oy - 8, "A₁(-a;0)", cls="lbl-sm", anchor="end")
    cv.text(ox + a + 4, oy - 8, "A₂(a;0)", cls="lbl-sm", anchor="start")

    # Điểm M trên nhánh phải
    if show_m and show_foci and pts_r:
        target_idx = len(pts_r) * 3 // 4
        mx, my = pts_r[target_idx]
        cv.line(ox - c, oy, mx, my, cls="accent-b", extra=' stroke-dasharray="4 3"')
        cv.line(ox + c, oy, mx, my, cls="accent-b", extra=' stroke-dasharray="4 3"')
        cv.dot(mx, my, r=3.6, cls="accent-a")
        cv.text(mx + 7, my - 6, "M(x;y)", cls="lbl")
        cv.text(ox, h - 10, "|MF₁ − MF₂| = 2a  (c² = a² + b²)", cls="lbl-sm", anchor="middle")

    return cv.render()


def build_conic_parabola(p: Params) -> str:
    """Đồ thị Parabol chính tắc y² = 2px với tiêu điểm F(p/2; 0) và đường chuẩn Δ: x = −p/2."""
    param_p = max(_f(p.get("p", 60), 60.0), 20.0)
    w, h = 480.0, 320.0
    ox, oy = 140.0, h / 2.0

    cv = Canvas(w, h, title="Đường Parabol chính tắc",
                desc=f"Parabol y² = 2px (p = {int(param_p)}) với tiêu điểm F(p/2; 0) và đường chuẩn Δ: x = −p/2.")

    # Trục toạ độ
    cv.arrow(30, oy, w - 25, oy, cls="axis", head=7)
    cv.arrow(ox, h - 25, ox, 25, cls="axis", head=7)
    cv.text(w - 28, oy - 9, "x", cls="lbl-sm", anchor="end")
    cv.text(ox + 9, 32, "y", cls="lbl-sm")
    cv.text(ox - 8, oy + 16, "O", cls="lbl", anchor="end")

    # Đường chuẩn Δ: x = -p/2
    dir_x = ox - param_p / 2.0
    cv.line(dir_x, 35, dir_x, h - 35, cls="accent-c", extra=' stroke-dasharray="4 3"')
    cv.text(dir_x - 6, 45, "Δ: x = -p/2", cls="lbl-sm", anchor="end")

    # Đồ thị Parabol x = y² / (2p)
    pts = []
    max_y = 125.0
    steps = int(max_y * 2)
    for i in range(-steps // 2, steps // 2 + 1):
        y_val = i * (2.0 * max_y / steps)
        x_val = (y_val * y_val) / (2.0 * param_p)
        if x_val < (w - ox - 35):
            pts.append((ox + x_val, oy - y_val))

    cv.polyline(pts, cls="curve")

    # Tiêu điểm F(p/2; 0)
    fx = ox + param_p / 2.0
    cv.dot(fx, oy, r=3.4, cls="accent-b")
    cv.text(fx + 4, oy + 18, "F(p/2;0)", cls="lbl-sm", anchor="start")

    # Điểm M(x; y) trên parabol
    target_y = 80.0
    target_x = (target_y * target_y) / (2.0 * param_p)
    mx, my = ox + target_x, oy - target_y
    cv.dot(mx, my, r=3.6, cls="accent-a")
    cv.text(mx + 7, my - 6, "M(x;y)", cls="lbl")

    # Đoạn MF và đoạn vuông góc MH tới đường chuẩn Δ
    cv.line(mx, my, fx, oy, cls="accent-b", extra=' stroke-dasharray="4 3"')
    cv.line(mx, my, dir_x, my, cls="accent-c", extra=' stroke-dasharray="4 3"')
    cv.dot(dir_x, my, r=2.6, cls="accent-c")
    cv.text(dir_x - 6, my + 4, "H", cls="lbl-sm", anchor="end")
    cv.right_angle(dir_x, my, dir_x, my - 20, mx, my, size=10)

    cv.text((mx + fx) / 2.0 + 8, (my + oy) / 2.0, "MF", cls="lbl-sm")
    cv.text((mx + dir_x) / 2.0, my - 6, "d(M,Δ)", cls="lbl-sm", anchor="middle")
    cv.text(ox + 80, h - 10, "MF = d(M, Δ) = x + p/2  (e = 1)", cls="lbl-sm", anchor="middle")

    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "conic_ellipse": build_conic_ellipse,
    "conic_hyperbola": build_conic_hyperbola,
    "conic_parabola": build_conic_parabola,
}
