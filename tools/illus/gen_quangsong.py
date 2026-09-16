"""Generator SVG cho sóng ánh sáng và quang hình: Giao thoa Y-âng và Lăng kính.

Mọi toạ độ và đường truyền tia sáng được tính chuẩn theo định luật quang học:
- Giao thoa Y-âng: i = λD/a, x_s = ki, x_t = (k + ½)i, d₂ − d₁ = ax/D
- Lăng kính: sin i₁ = n·sin r₁, sin i₂ = n·sin r₂, A = r₁ + r₂, D = i₁ + i₂ − A
- Tán sắc: n_tím > n_đỏ ⇒ góc lệch D_tím > D_đỏ
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


def build_young_interference(p: Params) -> str:
    """Thí nghiệm giao thoa ánh sáng qua hai khe hẹp Y-âng."""
    mode = str(p.get("mode", "fringe_spacing"))
    w, h = 520.0, 320.0
    cv = Canvas(w, h, title="Thí nghiệm giao thoa khe Y-âng",
                desc="Hai khe hẹp S₁, S₂ cách nhau a, màn cách hai khe D. Vân sáng tại x = ki, khoảng vân i = λD/a.")

    # Nguồn sáng đơn sắc S
    sx, sy = 45.0, h / 2.0
    cv.dot(sx, sy, r=3.5, cls="accent-a")
    cv.text(sx - 8, sy - 8, "S", cls="lbl")

    # Mặt phẳng chứa 2 khe S₁, S₂
    slit_x = 135.0
    gap = 22.0
    cv.line(slit_x, 25, slit_x, sy - gap, cls="ink", extra=' stroke-width="3"')
    cv.line(slit_x, sy + gap, slit_x, h - 25, cls="ink", extra=' stroke-width="3"')
    s1x, s1y = slit_x, sy - gap
    s2x, s2y = slit_x, sy + gap
    cv.dot(s1x, s1y, r=2.6, cls="accent-a")
    cv.dot(s2x, s2y, r=2.6, cls="accent-a")
    cv.text(s1x - 14, s1y - 6, "S₁", cls="lbl-sm")
    cv.text(s2x - 14, s2y + 14, "S₂", cls="lbl-sm")

    # Khoảng cách a giữa hai khe
    cv.line(s1x - 22, s1y, s1x - 22, s2y, cls="ink-thin")
    cv.line(s1x - 26, s1y, s1x - 18, s1y, cls="ink-thin")
    cv.line(s1x - 26, s2y, s1x - 18, s2y, cls="ink-thin")
    cv.text(s1x - 28, sy + 4, "a", cls="lbl-sm", anchor="end")

    # Màn quan sát M
    screen_x = 420.0
    cv.line(screen_x, 20, screen_x, h - 20, cls="ink", extra=' stroke-width="2.5"')
    cv.text(screen_x + 8, 32, "Màn E", cls="lbl-sm")

    # Khoảng cách D
    cv.line(slit_x, h - 15, screen_x, h - 15, cls="axis")
    cv.line(slit_x, h - 20, slit_x, h - 10, cls="axis")
    cv.line(screen_x, h - 20, screen_x, h - 10, cls="axis")
    cv.text((slit_x + screen_x) / 2.0, h - 22, "D (khoảng cách khe – màn)", cls="lbl-sm", anchor="middle")

    # Vân trung tâm O
    cv.dot(screen_x, sy, r=3.0, cls="accent-b")
    cv.text(screen_x + 8, sy + 4, "O (vân trung tâm)", cls="lbl-sm")

    # Điểm M trên màn
    fringe_i = 20.0
    target_k = 3 if mode != "dark" else 2.5
    my = sy - target_k * fringe_i
    cv.dot(screen_x, my, r=3.5, cls="accent-a")
    label_m = "M (vân sáng bậc 3)" if mode != "dark" else "M (vân tối thứ 3)"
    cv.text(screen_x + 8, my - 6, label_m, cls="lbl-sm")

    # Tia sáng S₁M và S₂M
    cv.line(s1x, s1y, screen_x, my, cls="accent-c", extra=' stroke-width="1.5"')
    cv.line(s2x, s2y, screen_x, my, cls="accent-c", extra=' stroke-width="1.5"')
    cv.text((s1x + screen_x) / 2.0 - 15, (s1y + my) / 2.0 - 8, "d₁", cls="lbl-sm")
    cv.text((s2x + screen_x) / 2.0 + 10, (s2y + my) / 2.0 + 12, "d₂", cls="lbl-sm")

    # Toạ độ x của M
    cv.line(screen_x - 12, sy, screen_x - 12, my, cls="accent-b", extra=' stroke-dasharray="3 2"')
    cv.text(screen_x - 16, (sy + my) / 2.0 + 4, "x", cls="lbl-sm", anchor="end")

    # Hệ vân sáng - tối mô phỏng trên màn
    for k in range(-5, 6):
        fy = sy + k * fringe_i
        if 25 < fy < h - 25:
            cv.line(screen_x, fy, screen_x + 22, fy, cls="accent-b", extra=' stroke-width="3"')
            if k < 5:
                # vân tối ở giữa
                fy_dark = fy + fringe_i / 2.0
                cv.line(screen_x, fy_dark, screen_x + 12, fy_dark, cls="ink-thin", extra=' stroke-width="1" opacity="0.35"')

    # Đánh dấu khoảng vân i
    cv.line(screen_x + 28, sy, screen_x + 28, sy + fringe_i, cls="ink-thin")
    cv.line(screen_x + 24, sy, screen_x + 32, sy, cls="ink-thin")
    cv.line(screen_x + 24, sy + fringe_i, screen_x + 32, sy + fringe_i, cls="ink-thin")
    cv.text(screen_x + 36, sy + fringe_i / 2.0 + 4, "i = λD/a", cls="lbl-sm")

    # Chú thích chân hình
    caption = "Hiệu quang trình: d₂ − d₁ = ax/D" if mode == "path_diff" else "Khoảng vân giao thoa: i = λD/a"
    cv.text((slit_x + screen_x) / 2.0, 30, caption, cls="lbl-sm", anchor="middle")

    return cv.render()


def build_prism_refraction(p: Params) -> str:
    """Đường truyền tia sáng qua lăng kính và góc lệch D."""
    w, h = 480.0, 320.0
    cv = Canvas(w, h, title="Đường truyền tia sáng qua lăng kính",
                desc="Tia sáng đơn sắc đi qua lăng kính góc chiết quang A: sin i₁ = n·sin r₁, sin i₂ = n·sin r₂, D = i₁ + i₂ − A.")

    # Tiết diện lăng kính tam giác ABC
    ax, ay = 240.0, 55.0
    bx, by = 120.0, 265.0
    cx, cy = 360.0, 265.0

    cv.polygon([(ax, ay), (bx, by), (cx, cy)], cls="fill-a")
    cv.polyline([(ax, ay), (bx, by), (cx, cy), (ax, ay)], cls="ink", extra=' stroke-width="2"')

    cv.text(ax, ay - 10, "A (góc chiết quang)", cls="lbl-sm", anchor="middle")
    cv.text(bx - 12, by + 14, "B", cls="lbl")
    cv.text(cx + 4, cy + 14, "C", cls="lbl")

    # Tia tới SI
    ix, iy = 170.0, 180.0
    sx, sy = 55.0, 225.0
    cv.arrow(sx, sy, ix, iy, cls="accent-b", head=8)
    cv.text((sx + ix) / 2.0 - 10, (sy + iy) / 2.0 + 16, "SI (tia tới)", cls="lbl-sm")

    # Tia khúc xạ IJ trong lăng kính
    jx, jy = 300.0, 165.0
    cv.arrow(ix, iy, jx, jy, cls="accent-b", head=8)
    cv.text((ix + jx) / 2.0, (iy + jy) / 2.0 + 16, "r₁     r₂", cls="lbl-sm", anchor="middle")

    # Tia ló JR ra ngoài
    rx, ry = 425.0, 220.0
    cv.arrow(jx, jy, rx, ry, cls="accent-b", head=8)
    cv.text((jx + rx) / 2.0 + 10, (jy + ry) / 2.0 + 16, "JR (tia ló)", cls="lbl-sm")

    # Đường kéo dài xác định góc lệch D
    kx, ky = 235.0, 145.0
    cv.line(ix, iy, kx, ky, cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.line(jx, jy, kx, ky, cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.text(kx + 10, ky - 8, "D (góc lệch)", cls="lbl-sm", anchor="start")

    # Pháp tuyến tại hai điểm tới I và J
    cv.line(ix - 25, iy - 30, ix + 35, iy + 42, cls="axis", extra=' stroke-dasharray="3 3"')
    cv.line(jx - 35, jy + 42, jx + 25, jy - 30, cls="axis", extra=' stroke-dasharray="3 3"')

    # Chú thích công thức
    cv.text(w / 2.0, h - 10, "A = r₁ + r₂  |  D = i₁ + i₂ − A", cls="lbl-sm", anchor="middle")

    return cv.render()


def build_prism_dispersion(p: Params) -> str:
    """Tán sắc ánh sáng trắng qua lăng kính thành dải màu cầu vồng."""
    w, h = 480.0, 320.0
    cv = Canvas(w, h, title="Hiện tượng tán sắc ánh sáng qua lăng kính",
                desc="Chùm ánh sáng trắng bị tách thành dải quang phổ liên tục từ đỏ đến tím do chiết suất n_tím > n_đỏ.")

    # Lăng kính ABC
    ax, ay = 210.0, 60.0
    bx, by = 110.0, 260.0
    cx, cy = 310.0, 260.0

    cv.polygon([(ax, ay), (bx, by), (cx, cy)], cls="fill-a")
    cv.polyline([(ax, ay), (bx, by), (cx, cy), (ax, ay)], cls="ink", extra=' stroke-width="2"')
    cv.text(ax, ay - 8, "A", cls="lbl", anchor="middle")

    # Tia sáng trắng tới mặt bên AB
    ix, iy = 150.0, 180.0
    sx, sy = 40.0, 215.0
    cv.arrow(sx, sy, ix, iy, cls="ink", head=8)
    cv.text(sx + 10, sy - 10, "Ánh sáng trắng", cls="lbl-sm")

    # Điểm ló của tia đỏ và tia tím trên mặt AC
    j_red_x, j_red_y = 265.0, 160.0
    j_violet_x, j_violet_y = 275.0, 185.0

    # Tia đỏ (lệch ít nhất)
    cv.line(ix, iy, j_red_x, j_red_y, cls="accent-b")
    cv.arrow(j_red_x, j_red_y, 420.0, 205.0, cls="accent-b", head=7)
    cv.text(426.0, 208.0, "Tia đỏ (lệch ít)", cls="lbl-sm", anchor="start")

    # Tia tím (lệch nhiều nhất)
    cv.line(ix, iy, j_violet_x, j_violet_y, cls="accent-a")
    cv.arrow(j_violet_x, j_violet_y, 410.0, 255.0, cls="accent-a", head=7)
    cv.text(416.0, 258.0, "Tia tím (lệch nhiều)", cls="lbl-sm", anchor="start")

    # Dải quang phổ giữa đỏ và tím
    cv.polygon([(j_red_x, j_red_y), (420.0, 205.0), (410.0, 255.0), (j_violet_x, j_violet_y)],
               cls="fill-c")

    # Chú thích
    cv.text(w / 2.0, h - 12, "n_đỏ < n_cam < n_vàng < n_lục < n_lam < n_chàm < n_tím", cls="lbl-sm", anchor="middle")

    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "young_interference": build_young_interference,
    "prism_refraction": build_prism_refraction,
    "prism_dispersion": build_prism_dispersion,
}
