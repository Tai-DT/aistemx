"""Generator SVG cho Hình học toạ độ không gian Oxyz (Toán 12).

Bao gồm:
- oxyz_coords: Hệ trục Oxyz, toạ độ điểm M(x,y,z), hình chiếu lên các trục/mặt phẳng, vectơ đơn vị, trung điểm/trọng tâm.
- oxyz_vectors: Hai vectơ, góc giữa hai vectơ, tích có hướng n = [u, v], diện tích hình bình hành, tam giác, thể tích khối hộp.
- oxyz_plane: Mặt phẳng (P): Ax + By + Cz + D = 0, vectơ pháp tuyến n, khoảng cách từ điểm đến mặt phẳng, hai mặt phẳng song song, góc giữa hai mặt phẳng, mặt phẳng đoạn chắn, mặt phẳng trung trực.
- oxyz_line: Đường thẳng d qua M0 với VTCP u, góc giữa đường thẳng và mặt phẳng, góc giữa hai đường thẳng, khoảng cách điểm đến đường thẳng, khoảng cách hai đường chéo nhau, vị trí tương đối mặt cầu và đường thẳng.
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


def build_oxyz_coords(p: Params) -> str:
    """Hệ trục toạ độ không gian Oxyz và toạ độ điểm M(x, y, z)."""
    w, h = 460.0, 340.0
    ox, oy = 170.0, 220.0  # Gốc O

    mode = str(p.get("mode", "point"))
    cv = Canvas(w, h, title="Hệ toạ độ không gian Oxyz",
                desc="Hệ toạ độ Oxyz với 3 trục Ox, Oy, Oz đôi một vuông góc.")

    # Các trục toạ độ:
    # Oz: thẳng đứng lên
    # Oy: nằm ngang sang phải
    # Ox: xiên góc 135° (xuống trái) với hệ số co 0.7
    kx, ky, kz = 0.75, 1.0, 1.0
    ang_x = math.radians(135)
    cos_x, sin_x = math.cos(ang_x), math.sin(ang_x)  # cos < 0, sin > 0

    def to_2d(x: float, y: float, z: float) -> tuple[float, float]:
        # x: trục Ox (xiên xuống trái)
        # y: trục Oy (ngang phải)
        # z: trục Oz (thẳng đứng lên)
        px = ox + y * ky + x * kx * math.cos(math.radians(215))
        py = oy - z * kz - x * kx * math.sin(math.radians(215))
        return px, py

    # Vẽ các tia âm (nét đứt mờ)
    cv.line(ox, oy, ox, h - 25, cls="axis", extra=' stroke-dasharray="3 3" opacity="0.4"')
    cv.line(ox, oy, 30, oy, cls="axis", extra=' stroke-dasharray="3 3" opacity="0.4"')

    # Vẽ 3 trục chính
    # Oz
    cv.arrow(ox, oy, ox, 30, cls="axis", head=7)
    cv.text(ox + 12, 35, "z", cls="lbl-sm")
    # Oy
    cv.arrow(ox, oy, w - 30, oy, cls="axis", head=7)
    cv.text(w - 25, oy - 10, "y", cls="lbl-sm")
    # Ox
    x_end_x, x_end_y = to_2d(180, 0, 0)
    cv.arrow(ox, oy, x_end_x, x_end_y, cls="axis", head=7)
    cv.text(x_end_x - 12, x_end_y + 16, "x", cls="lbl-sm")

    cv.text(ox - 15, oy + 16, "O", cls="lbl")

    if mode == "unit_vectors":
        # i, j, k
        ix, iy = to_2d(50, 0, 0)
        jx, jy = to_2d(0, 50, 0)
        kx_pt, ky_pt = to_2d(0, 0, 50)
        cv.arrow(ox, oy, ix, iy, cls="accent-b", head=6)
        cv.arrow(ox, oy, jx, jy, cls="accent-c", head=6)
        cv.arrow(ox, oy, kx_pt, ky_pt, cls="accent-a", head=6)
        cv.text(ix - 14, iy + 6, "i⃗", cls="lbl")
        cv.text(jx + 2, jy - 8, "j⃗", cls="lbl")
        cv.text(kx_pt + 8, ky_pt + 6, "k⃗", cls="lbl")
        cv.text(w / 2, h - 20, "OM⃗ = x·i⃗ + y·j⃗ + z·k⃗", cls="lbl-sm", anchor="middle")

    elif mode == "midpoint_centroid":
        # Đoạn thẳng AB và trung điểm M
        ax, ay = to_2d(30, 40, 110)
        bx, by = to_2d(120, 160, 40)
        mx, my = (ax + bx) / 2.0, (ay + by) / 2.0
        cv.line(ax, ay, bx, by, cls="ink")
        cv.dot(ax, ay, 3.5, cls="accent-a")
        cv.dot(bx, by, 3.5, cls="accent-a")
        cv.dot(mx, my, 4.0, cls="accent-b")
        cv.text(ax - 10, ay - 8, "A(x_A, y_A, z_A)", cls="lbl-sm")
        cv.text(bx + 6, by + 12, "B(x_B, y_B, z_B)", cls="lbl-sm")
        cv.text(mx + 6, my - 8, "M (Trung điểm)", cls="lbl-sm")
        cv.text(w / 2, h - 18, "M = ((x_A+x_B)/2, (y_A+y_B)/2, (z_A+z_B)/2)", cls="lbl-sm", anchor="middle")

    else:
        # M(x0, y0, z0) với các đường gióng hình hộp chữ nhật
        x0, y0, z0 = 110.0, 150.0, 105.0
        mx, my = to_2d(x0, y0, z0)
        # Các hình chiếu:
        m_xy = to_2d(x0, y0, 0)
        m_x = to_2d(x0, 0, 0)
        m_y = to_2d(0, y0, 0)
        m_z = to_2d(0, 0, z0)
        m_xz = to_2d(x0, 0, z0)
        m_yz = to_2d(0, y0, z0)

        # Hộp gióng không gian (nét đứt)
        cv.line(ox, oy, m_x[0], m_x[1], cls="accent-a", extra=' stroke-dasharray="3 3"')
        cv.line(ox, oy, m_y[0], m_y[1], cls="accent-a", extra=' stroke-dasharray="3 3"')
        cv.line(m_x[0], m_x[1], m_xy[0], m_xy[1], cls="accent-a", extra=' stroke-dasharray="3 3"')
        cv.line(m_y[0], m_y[1], m_xy[0], m_xy[1], cls="accent-a", extra=' stroke-dasharray="3 3"')

        # Dóng lên M
        cv.line(m_xy[0], m_xy[1], mx, my, cls="accent-b", extra=' stroke-dasharray="4 3" stroke-width="1.8"')
        cv.line(m_z[0], m_z[1], m_yz[0], m_yz[1], cls="accent-a", extra=' stroke-dasharray="3 3"')
        cv.line(m_z[0], m_z[1], m_xz[0], m_xz[1], cls="accent-a", extra=' stroke-dasharray="3 3"')
        cv.line(m_xz[0], m_xz[1], mx, my, cls="accent-a", extra=' stroke-dasharray="3 3"')
        cv.line(m_yz[0], m_yz[1], mx, my, cls="accent-a", extra=' stroke-dasharray="3 3"')

        # Vectơ vị trí OM
        cv.arrow(ox, oy, mx, my, cls="accent-c", head=7)

        # Các điểm
        cv.dot(mx, my, 4.5, cls="accent-b")
        cv.dot(m_xy[0], m_xy[1], 3.0, cls="accent-a")
        cv.dot(m_x[0], m_x[1], 2.5, cls="accent-a")
        cv.dot(m_y[0], m_y[1], 2.5, cls="accent-a")
        cv.dot(m_z[0], m_z[1], 2.5, cls="accent-a")

        cv.text(mx + 8, my - 6, "M(x, y, z)", cls="lbl")
        cv.text(m_xy[0] + 6, m_xy[1] + 12, "M_xy(x, y, 0)", cls="lbl-sm")
        cv.text(m_x[0] - 8, m_x[1] + 14, "x", cls="lbl-sm")
        cv.text(m_y[0] + 4, m_y[1] + 14, "y", cls="lbl-sm")
        cv.text(m_z[0] - 14, m_z[1] + 4, "z", cls="lbl-sm")

        cv.text(w / 2, h - 15, "OM = √(x² + y² + z²)", cls="lbl-sm", anchor="middle")

    return cv.render()


def build_oxyz_vectors(p: Params) -> str:
    """Vectơ trong không gian: tích có hướng, tích vô hướng, diện tích, thể tích."""
    w, h = 460.0, 320.0
    mode = str(p.get("mode", "cross_product"))
    cv = Canvas(w, h, title="Vectơ trong không gian Oxyz",
                desc="Tích có hướng và ứng dụng hình học trong không gian Oxyz.")

    if mode == "box_volume":
        # Khối hộp dựng trên 3 vectơ u, v, w
        ox, oy = 90.0, 240.0
        # u: ngang chếch
        ux, uy = ox + 140, oy - 20
        # v: xiên vào trong
        vx, vy = ox + 80, oy - 70
        # u+v
        uvx, uvy = ux + (vx - ox), uy + (vy - oy)
        # w: thẳng đứng chếch lên
        wx, wy = ox + 15, oy - 120

        # Mặt đáy (u, v)
        cv.polygon([(ox, oy), (ux, uy), (uvx, uvy), (vx, vy)], cls="fill-a")
        # Khối hộp 3D
        top_pts = [(ox + (wx - ox), oy + (wy - oy)),
                   (ux + (wx - ox), uy + (wy - oy)),
                   (uvx + (wx - ox), uvy + (wy - oy)),
                   (vx + (wx - ox), vy + (wy - oy))]
        cv.polygon(top_pts, cls="fill-b")

        # Các cạnh bên và mặt bên
        cv.line(ox, oy, top_pts[0][0], top_pts[0][1], cls="ink")
        cv.line(ux, uy, top_pts[1][0], top_pts[1][1], cls="ink")
        cv.line(uvx, uvy, top_pts[2][0], top_pts[2][1], cls="ink")
        cv.line(vx, vy, top_pts[3][0], top_pts[3][1], cls="ink-thin", extra=' stroke-dasharray="3 3"')

        # Đáy nét khuất
        cv.line(ox, oy, vx, vy, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.line(vx, vy, uvx, uvy, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.line(ox, oy, ux, uy, cls="ink")
        cv.line(ux, uy, uvx, uvy, cls="ink")

        # Cạnh trên
        cv.polygon(top_pts, cls="fill-c")
        cv.polyline([top_pts[0], top_pts[1], top_pts[2], top_pts[3], top_pts[0]], cls="ink")

        # 3 vectơ chỉ thị
        cv.arrow(ox, oy, ux, uy, cls="accent-a", head=7)
        cv.arrow(ox, oy, vx, vy, cls="accent-a", head=7)
        cv.arrow(ox, oy, wx, wy, cls="accent-b", head=7)

        cv.text((ox + ux) / 2, (oy + uy) / 2 + 18, "u⃗", cls="lbl")
        cv.text((ox + vx) / 2 - 14, (oy + vy) / 2, "v⃗", cls="lbl")
        cv.text(wx - 16, (oy + wy) / 2, "w⃗", cls="lbl")

        cv.text(w / 2 + 50, 45, "V = |[u⃗, v⃗] · w⃗|", cls="lbl", extra=' font-size="16px"')
        cv.text(w / 2 + 50, 70, "Thể tích khối hộp dựng trên 3 vectơ", cls="lbl-sm")

    elif mode in ("parallelogram", "triangle"):
        # Hình bình hành hoặc tam giác dựng trên u, v
        ox, oy = 110.0, 220.0
        ux, uy = ox + 180, oy
        vx, vy = ox + 70, oy - 110
        cx, cy = ux + (vx - ox), uy + (vy - oy)

        if mode == "triangle":
            cv.polygon([(ox, oy), (ux, uy), (vx, vy)], cls="fill-a")
            cv.line(ux, uy, vx, vy, cls="ink", extra=' stroke-dasharray="4 3"')
            cv.text(w / 2 + 30, 60, "S_Δ = ½ |[u⃗, v⃗]|", cls="lbl", extra=' font-size="16px"')
            cv.text(w / 2 + 30, 85, "Diện tích tam giác trong không gian", cls="lbl-sm")
        else:
            cv.polygon([(ox, oy), (ux, uy), (cx, cy), (vx, vy)], cls="fill-a")
            cv.line(ux, uy, cx, cy, cls="ink-thin")
            cv.line(vx, vy, cx, cy, cls="ink-thin")
            cv.text(w / 2 + 30, 60, "S = |[u⃗, v⃗]|", cls="lbl", extra=' font-size="16px"')
            cv.text(w / 2 + 30, 85, "Diện tích hình bình hành trong không gian", cls="lbl-sm")

        cv.arrow(ox, oy, ux, uy, cls="accent-a", head=8)
        cv.arrow(ox, oy, vx, vy, cls="accent-a", head=8)
        cv.dot(ox, oy, 3.5, cls="accent-a")
        cv.text(ox - 15, oy + 5, "A", cls="lbl")
        cv.text(ux + 8, uy + 5, "B", cls="lbl")
        cv.text(vx - 5, vy - 10, "C", cls="lbl")
        cv.text((ox + ux) / 2, oy + 20, "u⃗ = AB⃗", cls="lbl-sm", anchor="middle")
        cv.text((ox + vx) / 2 - 25, (oy + vy) / 2, "v⃗ = AC⃗", cls="lbl-sm")

    elif mode == "dot_product":
        # Hai vectơ u, v và góc phi
        ox, oy = 140.0, 190.0
        ux, uy = ox + 160, oy - 20
        vx, vy = ox + 100, oy - 110

        cv.arrow(ox, oy, ux, uy, cls="accent-a", head=8)
        cv.arrow(ox, oy, vx, vy, cls="accent-a", head=8)
        cv.dot(ox, oy, 3.5, cls="accent-a")

        # Cung góc phi
        cv.path(f"M {ox+35} {oy-4} A 35 35 0 0 0 {ox+20} {oy-28}", cls="accent-b", extra=' fill="none" stroke-width="1.8"')
        cv.text(ox + 42, oy - 18, "φ", cls="lbl")

        cv.text(ux + 8, uy, "u⃗", cls="lbl")
        cv.text(vx + 4, vy - 8, "v⃗", cls="lbl")

        cv.text(w / 2, 45, "u⃗ · v⃗ = |u⃗|·|v⃗|·cos φ", cls="lbl", anchor="middle", extra=' font-size="16px"')
        cv.text(w / 2, 72, "cos φ = (u₁v₁ + u₂v₂ + u₃v₃) / (|u⃗|·|v⃗|)", cls="lbl-sm", anchor="middle")

    else:
        # Mặc định: Tích có hướng n = [u, v] vuông góc với cả u và v
        ox, oy = 160.0, 220.0
        ux, uy = ox + 160, oy - 20
        vx, vy = ox + 90, oy - 70
        # Vectơ n thẳng đứng lên
        nx, ny = ox, oy - 130

        # Mặt phẳng cơ sở chứa u và v
        p_corner1 = (ox - 40, oy + 10)
        p_corner2 = (ux + 40, uy + 10)
        p_corner3 = (ux + 40 + (vx - ox), uy - 70)
        p_corner4 = (ox - 40 + (vx - ox), oy - 80)
        cv.polygon([p_corner1, p_corner2, p_corner3, p_corner4], cls="fill-a")

        # Hai vectơ u, v
        cv.arrow(ox, oy, ux, uy, cls="accent-a", head=8)
        cv.arrow(ox, oy, vx, vy, cls="accent-a", head=8)

        # Vectơ n = [u, v]
        cv.arrow(ox, oy, nx, ny, cls="accent-b", head=8)

        # Ký hiệu góc vuông giữa n với u và n với v
        cv.right_angle(ox, oy, nx, ny, ux, uy, size=12)
        cv.right_angle(ox, oy, nx, ny, vx, vy, size=12)

        cv.text(ux + 10, uy + 5, "u⃗", cls="lbl")
        cv.text(vx + 8, vy - 4, "v⃗", cls="lbl")
        cv.text(nx + 10, ny + 10, "n⃗ = [u⃗, v⃗]", cls="lbl", extra=' font-weight="bold"')

        cv.text(w - 20, 50, "n⃗ ⊥ u⃗  và  n⃗ ⊥ v⃗", cls="lbl-sm", anchor="end")
        cv.text(w - 20, 75, "|[u⃗, v⃗]| = |u⃗|·|v⃗|·sin(u⃗, v⃗)", cls="lbl-sm", anchor="end")
        cv.text(w - 20, 100, "Quy tắc bàn tay phải", cls="lbl-sm", anchor="end")

    return cv.render()


def build_oxyz_plane(p: Params) -> str:
    """Mặt phẳng trong không gian Oxyz: VTPT, khoảng cách, góc, đoạn chắn."""
    w, h = 460.0, 320.0
    mode = str(p.get("mode", "general"))
    cv = Canvas(w, h, title="Mặt phẳng trong không gian Oxyz",
                desc="Phương trình tổng quát mặt phẳng và khoảng cách trong Oxyz.")

    if mode == "distance":
        # Mặt phẳng (P) và khoảng cách từ điểm M đến (P)
        p_pts = [(60.0, 240.0), (320.0, 240.0), (400.0, 150.0), (140.0, 150.0)]
        cv.polygon(p_pts, cls="fill-a")
        cv.polyline(p_pts + [p_pts[0]], cls="ink")
        cv.text(75, 230, "(P): Ax + By + Cz + D = 0", cls="lbl-sm")

        # Điểm M nằm ngoài (P)
        mx, my = 250.0, 50.0
        hx, hy = 250.0, 185.0  # Hình chiếu H trên (P)

        # Đoạn vuông góc MH
        cv.line(mx, my, hx, hy, cls="accent-b", extra=' stroke-width="2.2"')
        cv.dot(mx, my, 4.0, cls="accent-b")
        cv.dot(hx, hy, 3.5, cls="accent-a")

        # Góc vuông tại H
        cv.right_angle(hx, hy, mx, my, hx + 20, hy, size=10)

        cv.text(mx + 8, my, "M(x_M, y_M, z_M)", cls="lbl")
        cv.text(hx + 8, hy + 4, "H", cls="lbl")
        cv.text(mx - 10, (my + hy) / 2, "d(M, (P))", cls="lbl-sm", anchor="end")

        # Công thức
        cv.text(w - 15, 35, "d(M,(P)) = |Ax_M + By_M + Cz_M + D| / √(A² + B² + C²)",
                cls="lbl-sm", anchor="end", extra=' font-weight="bold"')

    elif mode == "intercept":
        # Phương trình mặt phẳng theo đoạn chắn x/a + y/b + z/c = 1
        ox, oy = 150.0, 210.0
        # 3 trục
        cv.arrow(ox, oy, ox, 30, cls="axis", head=7)
        cv.text(ox + 8, 35, "z", cls="lbl-sm")
        cv.arrow(ox, oy, w - 40, oy, cls="axis", head=7)
        cv.text(w - 35, oy - 8, "y", cls="lbl-sm")
        # Ox xiên
        kx, ky_end = ox - 90, oy + 70
        cv.arrow(ox, oy, kx, ky_end, cls="axis", head=7)
        cv.text(kx - 12, ky_end + 12, "x", cls="lbl-sm")
        cv.text(ox - 14, oy + 15, "O", cls="lbl")

        # 3 giao điểm A(a,0,0), B(0,b,0), C(0,0,c)
        ax, ay = ox - 55, oy + 42
        bx, by = ox + 180, oy
        cx, cy = ox, 65

        # Mặt phẳng tam giác ABC
        cv.polygon([(ax, ay), (bx, by), (cx, cy)], cls="fill-c")
        cv.line(ax, ay, bx, by, cls="accent-c", extra=' stroke-width="2"')
        cv.line(bx, by, cx, cy, cls="accent-c", extra=' stroke-width="2"')
        cv.line(cx, cy, ax, ay, cls="accent-c", extra=' stroke-width="2"')

        cv.dot(ax, ay, 3.5, cls="accent-b")
        cv.dot(bx, by, 3.5, cls="accent-b")
        cv.dot(cx, cy, 3.5, cls="accent-b")

        cv.text(ax - 8, ay + 16, "A(a,0,0)", cls="lbl-sm")
        cv.text(bx + 4, by + 16, "B(0,b,0)", cls="lbl-sm")
        cv.text(cx + 8, cy, "C(0,0,c)", cls="lbl-sm")

        cv.text(w / 2 + 40, 45, "x/a + y/b + z/c = 1", cls="lbl", extra=' font-size="16px"')
        cv.text(w / 2 + 40, 70, "Phương trình mặt phẳng đoạn chắn", cls="lbl-sm")

    elif mode == "parallel":
        # Hai mặt phẳng song song
        p1 = [(60.0, 260.0), (320.0, 260.0), (400.0, 180.0), (140.0, 180.0)]
        p2 = [(60.0, 160.0), (320.0, 160.0), (400.0, 80.0), (140.0, 80.0)]
        cv.polygon(p1, cls="fill-a")
        cv.polyline(p1 + [p1[0]], cls="ink")
        cv.polygon(p2, cls="fill-a")
        cv.polyline(p2 + [p2[0]], cls="ink")

        # Khoảng cách giữa 2 mặt phẳng
        hx1, hy1 = 230.0, 215.0
        hx2, hy2 = 230.0, 115.0
        cv.line(hx1, hy1, hx2, hy2, cls="accent-b", extra=' stroke-width="2"')
        cv.dot(hx1, hy1, 3.0, cls="accent-a")
        cv.dot(hx2, hy2, 3.0, cls="accent-a")
        cv.right_angle(hx1, hy1, hx2, hy2, hx1 + 18, hy1, size=8)
        cv.right_angle(hx2, hy2, hx1, hy1, hx2 + 18, hy2, size=8)

        cv.text(75, 250, "(P): Ax + By + Cz + D₁ = 0", cls="lbl-sm")
        cv.text(75, 150, "(Q): Ax + By + Cz + D₂ = 0", cls="lbl-sm")
        cv.text(hx1 + 8, (hy1 + hy2) / 2, "d((P),(Q))", cls="lbl-sm")

        cv.text(w - 15, 35, "d((P),(Q)) = |D₁ - D₂| / √(A² + B² + C²)", cls="lbl-sm", anchor="end", extra=' font-weight="bold"')

    elif mode == "angle":
        # Góc giữa hai mặt phẳng qua hai vectơ pháp tuyến
        cv.text(w / 2, 30, "cos φ = |n⃗₁ · n⃗₂| / (|n⃗₁| · |n⃗₂|)", cls="lbl", anchor="middle", extra=' font-size="16px"')
        # Hai mặt phẳng giao nhau
        cv.polygon([(50.0, 240.0), (280.0, 240.0), (380.0, 170.0), (150.0, 170.0)], cls="fill-a")
        cv.polyline([(50.0, 240.0), (280.0, 240.0), (380.0, 170.0), (150.0, 170.0), (50.0, 240.0)], cls="ink")

        # Mặt phẳng thứ hai cắt xiên
        cv.polygon([(110.0, 270.0), (340.0, 270.0), (300.0, 100.0), (70.0, 100.0)], cls="fill-b")
        cv.polyline([(110.0, 270.0), (340.0, 270.0), (300.0, 100.0), (70.0, 100.0), (110.0, 270.0)], cls="ink")

        # 2 pháp tuyến n1, n2 tại một điểm trên giao tuyến
        ix, iy = 210.0, 190.0
        cv.arrow(ix, iy, ix + 10, iy - 75, cls="accent-a", head=7)
        cv.arrow(ix, iy, ix - 65, iy - 45, cls="accent-b", head=7)
        cv.text(ix + 15, iy - 65, "n⃗₁", cls="lbl")
        cv.text(ix - 75, iy - 35, "n⃗₂", cls="lbl")
        cv.text(ix - 15, iy - 20, "φ", cls="lbl-sm")

    elif mode == "midplane":
        # Mặt phẳng trung trực của đoạn AB
        ax, ay = 140.0, 90.0
        bx, by = 300.0, 210.0
        mx, my = (ax + bx) / 2.0, (ay + by) / 2.0  # I

        # Mặt phẳng vuông góc với AB tại I
        p_pts = [(120.0, 260.0), (320.0, 210.0), (280.0, 60.0), (80.0, 110.0)]
        cv.polygon(p_pts, cls="fill-c")
        cv.polyline(p_pts + [p_pts[0]], cls="ink")

        # Đoạn AB đâm xuyên qua
        cv.line(ax, ay, mx, my, cls="accent-a", extra=' stroke-width="2"')
        cv.line(mx, my, bx, by, cls="accent-a", extra=' stroke-width="2"')
        cv.dot(ax, ay, 3.5, cls="accent-a")
        cv.dot(bx, by, 3.5, cls="accent-a")
        cv.dot(mx, my, 4.0, cls="accent-b")

        cv.text(ax - 10, ay - 6, "A", cls="lbl")
        cv.text(bx + 8, by + 8, "B", cls="lbl")
        cv.text(mx + 6, my - 8, "I (Trung điểm)", cls="lbl-sm")
        cv.text(w / 2, h - 20, "Mặt phẳng qua I và nhận AB⃗ làm VTPT", cls="lbl-sm", anchor="middle")

    else:
        # Mặt phẳng (P) tổng quát với điểm M0 và VTPT n
        p_pts = [(60.0, 240.0), (320.0, 240.0), (400.0, 150.0), (140.0, 150.0)]
        cv.polygon(p_pts, cls="fill-a")
        cv.polyline(p_pts + [p_pts[0]], cls="ink")

        m0x, m0y = 210.0, 195.0
        nx, ny = m0x, m0y - 110
        cv.arrow(m0x, m0y, nx, ny, cls="accent-b", head=8)
        cv.dot(m0x, m0y, 3.5, cls="accent-a")

        cv.right_angle(m0x, m0y, nx, ny, m0x + 25, m0y, size=12)

        cv.text(m0x + 8, m0y + 16, "M₀(x₀, y₀, z₀)", cls="lbl")
        cv.text(nx + 10, ny + 15, "n⃗ = (A, B, C)", cls="lbl", extra=' font-weight="bold"')
        cv.text(80, 225, "(P)", cls="lbl", extra=' font-size="16px"')

        cv.text(w / 2 + 50, 45, "A(x - x₀) + B(y - y₀) + C(z - z₀) = 0", cls="lbl-sm", anchor="middle")
        cv.text(w / 2 + 50, 70, "Phương trình tổng quát: Ax + By + Cz + D = 0", cls="lbl-sm", anchor="middle")

    return cv.render()


def build_oxyz_line(p: Params) -> str:
    """Đường thẳng trong không gian Oxyz: VTCP, góc đường-mặt, khoảng cách, hai đường chéo nhau."""
    w, h = 460.0, 320.0
    mode = str(p.get("mode", "param"))
    cv = Canvas(w, h, title="Đường thẳng trong không gian Oxyz",
                desc="Phương trình tham số, chính tắc và góc, khoảng cách của đường thẳng.")

    if mode == "line_plane_angle":
        # Góc giữa đường thẳng d và mặt phẳng (P)
        p_pts = [(50.0, 250.0), (320.0, 250.0), (400.0, 160.0), (130.0, 160.0)]
        cv.polygon(p_pts, cls="fill-a")
        cv.polyline(p_pts + [p_pts[0]], cls="ink")
        cv.text(70, 240, "(P)", cls="lbl")

        # Giao điểm A
        ax, ay = 180.0, 205.0
        cv.dot(ax, ay, 3.5, cls="accent-a")
        cv.text(ax - 14, ay + 6, "A", cls="lbl")

        # Hình chiếu d₁ trên (P)
        d_prime_x, d_prime_y = ax + 140, ay
        cv.line(ax, ay, d_prime_x, d_prime_y, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.text(d_prime_x + 8, d_prime_y, "d₁", cls="lbl-sm")

        # Đường thẳng d cắt xiên lên
        dx, dy = ax + 130, ay - 85
        cv.line(ax - 40, ay + 26, ax, ay, cls="accent-c", extra=' stroke-dasharray="3 3"')
        cv.line(ax, ay, dx + 30, dy - 20, cls="accent-c", extra=' stroke-width="2.2"')
        cv.text(dx + 35, dy - 20, "d", cls="lbl", extra=' font-weight="bold"')

        # Điểm M trên d và hình chiếu H trên (P)
        mx, my = ax + 90, ay - 60
        hx, hy = ax + 90, ay
        cv.line(mx, my, hx, hy, cls="accent-b", extra=' stroke-dasharray="3 3"')
        cv.dot(mx, my, 3.0, cls="accent-a")
        cv.dot(hx, hy, 3.0, cls="accent-a")
        cv.right_angle(hx, hy, mx, my, ax, ay, size=8)

        # Cung góc phi giữa d và d'
        cv.path(f"M {ax+30} {ay} A 30 30 0 0 0 {ax+26} {ay-15}", cls="accent-b", extra=' fill="none" stroke-width="1.8"')
        cv.text(ax + 36, ay - 8, "φ", cls="lbl")

        # VTPT n của mặt phẳng
        cv.arrow(ax, ay, ax, ay - 90, cls="accent-a", head=7)
        cv.text(ax + 8, ay - 80, "n⃗", cls="lbl")

        cv.text(w - 15, 40, "sin φ = |u⃗ · n⃗| / (|u⃗| · |n⃗|)", cls="lbl", anchor="end", extra=' font-size="16px"')
        cv.text(w - 15, 65, "Góc giữa đường thẳng và mặt phẳng (0 ≤ φ ≤ 90°)", cls="lbl-sm", anchor="end")

    elif mode == "skew_lines":
        # Khoảng cách giữa hai đường thẳng chéo nhau (đoạn vuông góc chung)
        # Đường d1
        cv.line(60, 80, 360, 110, cls="accent-a", extra=' stroke-width="2.2"')
        cv.text(370, 112, "Δ₁ (u⃗₁)", cls="lbl")
        # Đường d2 chéo phía dưới
        cv.line(100, 250, 380, 190, cls="accent-c", extra=' stroke-width="2.2"')
        cv.text(390, 192, "Δ₂ (u⃗₂)", cls="lbl")

        # Đoạn vuông góc chung MN
        m1x, m1y = 220.0, 96.0
        m2x, m2y = 220.0, 224.0
        cv.line(m1x, m1y, m2x, m2y, cls="accent-b", extra=' stroke-width="2.2"')
        cv.dot(m1x, m1y, 3.5, cls="accent-b")
        cv.dot(m2x, m2y, 3.5, cls="accent-b")

        cv.right_angle(m1x, m1y, m2x, m2y, m1x + 20, m1y + 2, size=9)
        cv.right_angle(m2x, m2y, m1x, m1y, m2x + 20, m2y - 4, size=9)

        cv.text(m1x - 10, m1y - 6, "M", cls="lbl")
        cv.text(m2x - 10, m2y + 14, "N", cls="lbl")
        cv.text(m1x + 8, (m1y + m2y) / 2, "d(Δ₁, Δ₂) = MN", cls="lbl-sm")

        cv.text(w / 2, 40, "d(Δ₁, Δ₂) = |[u⃗₁, u⃗₂] · M₁M₂⃗| / |[u⃗₁, u⃗₂]|", cls="lbl-sm", anchor="middle", extra=' font-weight="bold"')

    elif mode == "point_line_dist":
        # Khoảng cách từ điểm M đến đường thẳng Delta
        lx1, ly1 = 60.0, 200.0
        lx2, ly2 = 380.0, 200.0
        cv.line(lx1, ly1, lx2, ly2, cls="accent-a", extra=' stroke-width="2.2"')
        cv.text(390, 204, "Δ (M₀, u⃗)", cls="lbl")

        # M0 và u trên Delta
        m0x, m0y = 120.0, 200.0
        cv.dot(m0x, m0y, 3.0, cls="accent-a")
        cv.arrow(m0x, m0y, m0x + 60, m0y, cls="accent-c", head=7)
        cv.text(m0x, m0y + 18, "M₀", cls="lbl")
        cv.text(m0x + 30, m0y - 8, "u⃗", cls="lbl")

        # Điểm M và hình chiếu H
        mx, my = 260.0, 70.0
        hx, hy = 260.0, 200.0
        cv.line(mx, my, hx, hy, cls="accent-b", extra=' stroke-width="2"')
        cv.line(m0x, m0y, mx, my, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.dot(mx, my, 4.0, cls="accent-b")
        cv.dot(hx, hy, 3.0, cls="accent-a")
        cv.right_angle(hx, hy, mx, my, hx - 20, hy, size=10)

        cv.text(mx + 8, my, "M", cls="lbl")
        cv.text(hx + 6, hy + 18, "H", cls="lbl")
        cv.text(mx + 10, (my + hy) / 2, "d(M, Δ)", cls="lbl-sm")

        cv.text(w / 2, 35, "d(M, Δ) = |[M₀M⃗, u⃗]| / |u⃗|", cls="lbl", anchor="middle", extra=' font-size="16px"')

    elif mode == "two_lines_angle":
        # Góc giữa hai đường thẳng d1, d2
        ox, oy = 200.0, 160.0
        cv.line(ox - 140, oy + 50, ox + 140, oy - 50, cls="accent-a", extra=' stroke-width="2"')
        cv.line(ox - 120, oy - 60, ox + 120, oy + 60, cls="accent-c", extra=' stroke-width="2"')

        cv.arrow(ox, oy, ox + 70, oy - 25, cls="accent-a", head=7)
        cv.arrow(ox, oy, ox + 60, oy + 30, cls="accent-c", head=7)
        cv.text(ox + 80, oy - 30, "u⃗₁", cls="lbl")
        cv.text(ox + 70, oy + 40, "u⃗₂", cls="lbl")
        cv.text(ox + 35, oy + 4, "φ", cls="lbl")

        cv.text(w / 2, 40, "cos φ = |u⃗₁ · u⃗₂| / (|u⃗₁| · |u⃗₂|)", cls="lbl", anchor="middle", extra=' font-size="16px"')
        cv.text(w / 2, 65, "Góc giữa hai đường thẳng (0 ≤ φ ≤ 90°)", cls="lbl-sm", anchor="middle")

    elif mode == "sphere_line":
        # Vị trí tương đối mặt cầu và đường thẳng
        cx, cy, r = 180.0, 160.0, 65.0
        cv.circle(cx, cy, r, cls="accent-a", extra=' fill="none" stroke-width="2"')
        # Vĩ tuyến elip tạo chiều sâu 3D
        cv.path(f"M {cx-r} {cy} A {r} 22 0 0 0 {cx+r} {cy}", cls="ink-thin")
        cv.path(f"M {cx-r} {cy} A {r} 22 0 0 1 {cx+r} {cy}", cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.dot(cx, cy, 3.5, cls="accent-a")
        cv.text(cx - 8, cy - 8, "I", cls="lbl")

        # Đường thẳng d tiếp xúc (d = R) hoặc cắt
        dy = cy + r
        cv.line(50, dy, 380, dy, cls="accent-c", extra=' stroke-width="2"')
        cv.line(cx, cy, cx, dy, cls="accent-b", extra=' stroke-dasharray="3 3"')
        cv.dot(cx, dy, 3.5, cls="accent-b")
        cv.right_angle(cx, dy, cx, cy, cx + 20, dy, size=8)

        cv.text(cx + 8, (cy + dy) / 2, "d(I, Δ) = R", cls="lbl-sm")
        cv.text(cx + 8, dy + 18, "H (Tiếp điểm)", cls="lbl-sm")
        cv.text(390, dy + 4, "Δ (Tiếp tuyến)", cls="lbl-sm")
        cv.text(w / 2 + 30, 45, "d(I, Δ) = R: Tiếp xúc", cls="lbl-sm")
        cv.text(w / 2 + 30, 65, "d(I, Δ) < R: Cắt tại 2 điểm", cls="lbl-sm")
        cv.text(w / 2 + 30, 85, "d(I, Δ) > R: Không cắt", cls="lbl-sm")

    else:
        # Mặc định: Phương trình tham số / chính tắc của đường thẳng d
        lx1, ly1 = 60.0, 220.0
        lx2, ly2 = 390.0, 90.0
        cv.line(lx1, ly1, lx2, ly2, cls="accent-a", extra=' stroke-width="2.2"')

        m0x, m0y = 150.0, 185.0
        cv.dot(m0x, m0y, 4.0, cls="accent-b")
        cv.text(m0x - 10, m0y - 12, "M₀(x₀, y₀, z₀)", cls="lbl")

        # VTCP u xuất phát từ M0
        ux, uy = m0x + 90, m0y - 35
        cv.arrow(m0x, m0y, ux, uy, cls="accent-c", head=8)
        cv.text(ux + 8, uy, "u⃗ = (a, b, c)", cls="lbl", extra=' font-weight="bold"')

        cv.text(lx2 + 8, ly2, "d", cls="lbl", extra=' font-size="16px"')

        cv.text(w / 2 + 40, 40, "Tham số: x = x₀ + at, y = y₀ + bt, z = z₀ + ct", cls="lbl-sm", anchor="middle")
        cv.text(w / 2 + 40, 65, "Chính tắc: (x - x₀)/a = (y - y₀)/b = (z - z₀)/c", cls="lbl-sm", anchor="middle")

    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "oxyz_coords": build_oxyz_coords,
    "oxyz_vectors": build_oxyz_vectors,
    "oxyz_plane": build_oxyz_plane,
    "oxyz_line": build_oxyz_line,
}
