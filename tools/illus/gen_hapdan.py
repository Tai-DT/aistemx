"""Generator SVG cho Trường hấp dẫn & Chuyển động thiên thể Kepler (Vật lí THPT / AP / IB).

Bao gồm:
- kepler_orbit: Định luật I (quỹ đạo elip, cận điểm, viễn điểm), định luật II (quét diện tích bằng nhau), định luật III (T²/a³).
- gravitational_field: Định luật vạn vật hấp dẫn F = G·m₁m₂/r², quỹ đạo vệ tinh quanh Trái Đất v = √(GM/r), thế năng hấp dẫn.
"""

from __future__ import annotations

import math
from typing import Callable

from .svgkit import Canvas, _n

Params = dict


def build_kepler_orbit(p: Params) -> str:
    """Định luật Kepler về chuyển động thiên thể."""
    w, h = 480.0, 320.0
    mode = str(p.get("mode", "kepler2"))
    cv = Canvas(w, h, title="Định luật Kepler về quỹ đạo hành tinh",
                desc="Chuyển động của hành tinh trên quỹ đạo elip quanh Mặt Trời.")

    ox, oy = w / 2 - 20, h / 2
    a, b = 160.0, 100.0
    c = math.sqrt(a * a - b * b)  # Tiêu cự c ≈ 124.9

    # Mặt Trời ở tiêu điểm F1
    sun_x, sun_y = ox - c * 0.75, oy  # Vẽ với độ lệch tiêu điểm vừa phải cho dễ nhìn
    # Giữ tỷ lệ elip
    cv.path(f"M {ox-a} {oy} A {a} {b} 0 1 0 {ox+a} {oy} A {a} {b} 0 1 0 {ox-a} {oy}",
            cls="curve", extra=' stroke-dasharray="6 4" stroke-width="2"')

    # Mặt Trời
    cv.circle(sun_x, sun_y, 14.0, cls="accent-d", extra=' fill-opacity="1"')
    cv.text(sun_x, sun_y + 26, "Mặt Trời (Tiêu điểm)", cls="lbl-sm", anchor="middle")

    if mode == "kepler1":
        # Định luật I Kepler: Quỹ đạo elip, Cận điểm P và Viễn điểm A
        cv.text(w / 2, 35, "Định luật I Kepler: Quỹ đạo Elip", cls="lbl", anchor="middle", extra=' font-size="16px"')
        cv.text(w / 2, 60, "Mặt Trời nằm tại một trong hai tiêu điểm của hình elip", cls="lbl-sm", anchor="middle")

        # Trục lớn nối Aphelion và Perihelion
        cv.line(ox - a, oy, ox + a, oy, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        # Cận điểm P (Perihelion)
        px, py = ox - a, oy
        cv.dot(px, py, 4.0, cls="accent-b")
        cv.text(px - 10, py - 10, "Cận điểm P", cls="lbl-sm")
        cv.text(px - 10, py + 18, "(Gần nhất, v_max)", cls="lbl-sm")

        # Viễn điểm A (Aphelion)
        ax, ay = ox + a, oy
        cv.dot(ax, ay, 4.0, cls="accent-a")
        cv.text(ax + 6, ay - 10, "Viễn điểm A", cls="lbl-sm")
        cv.text(ax + 6, ay + 18, "(Xa nhất, v_min)", cls="lbl-sm")

        # Bán trục lớn a
        cv.line(ox, oy - 25, ox + a, oy - 25, cls="accent-c", extra=' stroke-width="1.8"')
        cv.arrow(ox + 20, oy - 25, ox, oy - 25, cls="accent-c", head=5)
        cv.arrow(ox + a - 20, oy - 25, ox + a, oy - 25, cls="accent-c", head=5)
        cv.text(ox + a / 2, oy - 32, "Bán trục lớn a", cls="lbl-sm", anchor="middle")

    elif mode == "kepler3":
        # Định luật III Kepler: T²/a³ = const
        cv.text(w / 2, 35, "T² / a³ = 4π² / (G·M) = hằng số", cls="lbl", anchor="middle", extra=' font-size="18px"')
        cv.text(w / 2, 60, "Tỉ số giữa bình phương chu kì và lập phương bán trục lớn là như nhau", cls="lbl-sm", anchor="middle")

        # Quỹ đạo tròn/elip so sánh 2 hành tinh
        a2, b2 = a * 0.55, b * 0.55
        cv.path(f"M {ox-a2} {oy} A {a2} {b2} 0 1 0 {ox+a2} {oy} A {a2} {b2} 0 1 0 {ox-a2} {oy}",
                cls="accent-c", extra=' fill="none" stroke-width="1.8" stroke-dasharray="4 3"')
        cv.text(ox + a2 + 8, oy - 10, "Hành tinh 1 (T₁, a₁)", cls="lbl-sm")
        cv.text(ox + a + 8, oy - 10, "Hành tinh 2 (T₂, a₂)", cls="lbl-sm")

        cv.text(w / 2, h - 25, "T₁² / a₁³ = T₂² / a₂³", cls="lbl", anchor="middle", extra=' font-size="16px"')

    else:
        # Định luật II Kepler: Định luật diện tích (quét diện tích bằng nhau)
        cv.text(w / 2, 35, "Định luật II Kepler: dA/dt = L/(2m) = const", cls="lbl", anchor="middle", extra=' font-size="16px"')
        cv.text(w / 2, 60, "Bán kính vectơ quét những diện tích bằng nhau trong các khoảng thời gian bằng nhau", cls="lbl-sm", anchor="middle")

        # Rẻ quạt 1: Gần Mặt Trời (r nhỏ, cung quét lớn)
        # Điểm cận nhật: góc từ 160° đến 200°
        p1_ang1, p1_ang2 = math.radians(150), math.radians(210)
        p1_x1, p1_y1 = ox + a * math.cos(p1_ang1), oy + b * math.sin(p1_ang1)
        p1_x2, p1_y2 = ox + a * math.cos(p1_ang2), oy + b * math.sin(p1_ang2)

        # Rẻ quạt gần Mặt Trời (S1)
        cv.path(f"M {sun_x} {sun_y} L {p1_x1} {p1_y1} A {a} {b} 0 0 1 {p1_x2} {p1_y2} Z",
                cls="fill-b", extra=' fill-opacity="0.35"')
        cv.line(sun_x, sun_y, p1_x1, p1_y1, cls="ink-thin")
        cv.line(sun_x, sun_y, p1_x2, p1_y2, cls="ink-thin")
        cv.text((sun_x + p1_x1 + p1_x2) / 3 - 10, oy, "ΔS₁", cls="lbl", extra=' font-weight="bold"')
        cv.text(p1_x1 - 10, oy - 45, "v₁ lớn (nhanh)", cls="lbl-sm", anchor="end")

        # Rẻ quạt 2: Xa Mặt Trời (r lớn, cung quét nhỏ)
        # Điểm viễn nhật: góc từ -20° đến 20°
        p2_ang1, p2_ang2 = math.radians(-18), math.radians(18)
        p2_x1, p2_y1 = ox + a * math.cos(p2_ang1), oy + b * math.sin(p2_ang1)
        p2_x2, p2_y2 = ox + a * math.cos(p2_ang2), oy + b * math.sin(p2_ang2)

        # Rẻ quạt xa Mặt Trời (S2)
        cv.path(f"M {sun_x} {sun_y} L {p2_x1} {p2_y1} A {a} {b} 0 0 1 {p2_x2} {p2_y2} Z",
                cls="fill-a", extra=' fill-opacity="0.35"')
        cv.line(sun_x, sun_y, p2_x1, p2_y1, cls="ink-thin")
        cv.line(sun_x, sun_y, p2_x2, p2_y2, cls="ink-thin")
        cv.text((sun_x + p2_x1 + p2_x2) / 3 + 20, oy, "ΔS₂", cls="lbl", extra=' font-weight="bold"')
        cv.text(p2_x2 + 8, oy + 30, "v₂ bé (chậm)", cls="lbl-sm")

        # Nhãn kết luận
        cv.text(w / 2, h - 20, "Trong cùng thời gian Δt: ΔS₁ = ΔS₂", cls="lbl", anchor="middle")

    return cv.render()


def build_gravitational_field(p: Params) -> str:
    """Định luật vạn vật hấp dẫn và chuyển động vệ tinh."""
    w, h = 480.0, 320.0
    mode = str(p.get("mode", "newton_law"))
    cv = Canvas(w, h, title="Trường hấp dẫn và định luật vạn vật hấp dẫn",
                desc="Tương tác hấp dẫn giữa hai vật F = G·m₁m₂/r².")

    if mode == "satellite":
        # Vệ tinh quay quanh Trái Đất trên quỹ đạo tròn
        cv.text(w / 2, 35, "v = √(G·M / r)   và   v_thoát = √(2G·M / r)",
                cls="lbl", anchor="middle", extra=' font-size="16px"')
        cv.text(w / 2, 60, "Lực hấp dẫn đóng vai trò lực hướng tâm: F_hd = F_ht", cls="lbl-sm", anchor="middle")

        cx, cy = 180.0, 185.0
        # Quả địa cầu
        cv.circle(cx, cy, 45.0, cls="accent-a", extra=' fill-opacity="0.3"')
        cv.text(cx, cy + 4, "Trái Đất (M)", cls="lbl-sm", anchor="middle")

        # Quỹ đạo tròn bán kính r
        r_orb = 105.0
        cv.circle(cx, cy, r_orb, cls="accent-c", extra=' fill="none" stroke-dasharray="5 4" stroke-width="1.8"')

        # Vệ tinh tại vị trí góc 45°
        ang = math.radians(-45)
        sat_x, sat_y = cx + r_orb * math.cos(ang), cy + r_orb * math.sin(ang)
        cv.rect(sat_x - 6, sat_y - 6, 12, 12, cls="ink")
        # Tấm pin mặt trời
        cv.line(sat_x - 14, sat_y, sat_x + 14, sat_y, cls="accent-a", extra=' stroke-width="3"')
        cv.text(sat_x + 14, sat_y - 8, "Vệ tinh (m)", cls="lbl-sm")

        # Vectơ vận tốc tiếp tuyến v
        tan_x, tan_y = -math.sin(ang) * 55, math.cos(ang) * 55
        cv.arrow(sat_x, sat_y, sat_x + tan_x, sat_y + tan_y, cls="accent-c", head=7)
        cv.text(sat_x + tan_x + 6, sat_y + tan_y, "v⃗", cls="lbl")

        # Lực hấp dẫn F_hd hướng về tâm Trái Đất
        rad_x, rad_y = -math.cos(ang) * 50, -math.sin(ang) * 50
        cv.arrow(sat_x, sat_y, sat_x + rad_x, sat_y + rad_y, cls="accent-b", head=7)
        cv.text(sat_x + rad_x - 14, sat_y + rad_y + 12, "F⃗_hd", cls="lbl")

        # Bán kính quỹ đạo r = R + h
        cv.line(cx, cy, cx - r_orb, cy, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.line(cx, cy, cx, cy - r_orb, cls="accent-b", extra=' stroke-width="1.8"')
        cv.arrow(cx, cy - 25, cx, cy, cls="accent-b", head=5)
        cv.arrow(cx, cy - r_orb + 25, cx, cy - r_orb, cls="accent-b", head=5)
        cv.text(cx - 10, cy - r_orb / 2, "r = R + h", cls="lbl-sm", anchor="end")

        # Cơ năng vệ tinh
        cv.text(w - 20, 160, "W = -G·Mm / (2r)", cls="lbl", anchor="end")
        cv.text(w - 20, 185, "Thế năng W_t = -G·Mm/r", cls="lbl-sm", anchor="end")
        cv.text(w - 20, 210, "Động năng W_d = G·Mm/(2r)", cls="lbl-sm", anchor="end")

    else:
        # Định luật vạn vật hấp dẫn giữa hai vật m1, m2
        cv.text(w / 2, 40, "F = G · (m₁ · m₂) / r²", cls="lbl", anchor="middle", extra=' font-size="20px"')
        cv.text(w / 2, 68, "Hai vật hút nhau bằng cặp lực trực đối: F⃗₁₂ = -F⃗₂₁", cls="lbl-sm", anchor="middle")

        # Vật 1 (m1)
        x1, y1, r1 = 110.0, 185.0, 32.0
        cv.circle(x1, y1, r1, cls="accent-a", extra=' fill-opacity="0.3" stroke-width="2"')
        cv.dot(x1, y1, 4.0, cls="accent-a")
        cv.text(x1, y1 + 5, "m₁", cls="lbl", anchor="middle")

        # Vật 2 (m2)
        x2, y2, r2 = 360.0, 185.0, 24.0
        cv.circle(x2, y2, r2, cls="accent-c", extra=' fill-opacity="0.3" stroke-width="2"')
        cv.dot(x2, y2, 4.0, cls="accent-c")
        cv.text(x2, y2 + 5, "m₂", cls="lbl", anchor="middle")

        # Khoảng cách r giữa 2 tâm
        cv.line(x1, y1 + 55, x2, y2 + 55, cls="ink", extra=' stroke-width="1.8"')
        cv.arrow(x1 + 30, y1 + 55, x1, y1 + 55, cls="ink", head=6)
        cv.arrow(x2 - 30, y2 + 55, x2, y2 + 55, cls="ink", head=6)
        cv.line(x1, y1, x1, y1 + 65, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.line(x2, y2, x2, y2 + 65, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.text((x1 + x2) / 2, y1 + 48, "r (Khoảng cách giữa hai tâm)", cls="lbl-sm", anchor="middle")

        # Lực hấp dẫn F12 (m1 bị hút về phía m2)
        cv.arrow(x1, y1, x1 + 65, y1, cls="accent-b", head=8)
        cv.text(x1 + 68, y1 - 10, "F⃗₁₂", cls="lbl")

        # Lực hấp dẫn F21 (m2 bị hút về phía m1)
        cv.arrow(x2, y2, x2 - 65, y2, cls="accent-b", head=8)
        cv.text(x2 - 80, y2 - 10, "F⃗₂₁", cls="lbl")

        # Hằng số hấp dẫn G
        cv.text(w / 2, h - 20, "G ≈ 6,674 × 10⁻¹¹ N·m²/kg²", cls="lbl-sm", anchor="middle")

    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "kepler_orbit": build_kepler_orbit,
    "gravitational_field": build_gravitational_field,
}
