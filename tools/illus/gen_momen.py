"""Generator SVG cho Cân bằng vật rắn & Mômen lực (Vật lí 10).

Bao gồm:
- torque_moment: Mômen lực M = F·d, cánh tay đòn d ⊥ giá của lực, ngẫu lực M = F·d.
- lever_balance: Đòn bẩy quanh điểm tựa O (F₁d₁ = F₂d₂), hợp hai lực song song cùng/ngược chiều.
- equilibrium_3forces: Cân bằng 3 lực đồng quy và tam giác lực khép kín, điều kiện mặt chân đế.
"""

from __future__ import annotations

import math
from typing import Callable

from .svgkit import Canvas, _n

Params = dict


def build_torque_moment(p: Params) -> str:
    """Mômen lực M = F·d và ngẫu lực."""
    w, h = 460.0, 320.0
    mode = str(p.get("mode", "single"))
    cv = Canvas(w, h, title="Mômen lực và cánh tay đòn",
                desc="Mômen lực đối với trục quay M = F·d.")

    if mode == "couple":
        # Ngẫu lực: hai lực song song ngược chiều cùng độ lớn
        cv.text(w / 2, 40, "M = F · d", cls="lbl", anchor="middle", extra=' font-size="18px"')
        cv.text(w / 2, 65, "Mômen ngẫu lực (d: khoảng cách giữa hai giá của lực)", cls="lbl-sm", anchor="middle")

        # Vật hình thanh đòn quay quanh tâm O
        cx, cy = w / 2, 190.0
        r = 110.0
        cv.circle(cx, cy, 5.0, cls="accent-a")
        cv.text(cx, cy + 20, "O (Trục quay)", cls="lbl-sm", anchor="middle")

        # Thanh quay nghiêng góc 30°
        ang = math.radians(30)
        x1, y1 = cx - r * math.cos(ang), cy + r * math.sin(ang)
        x2, y2 = cx + r * math.cos(ang), cy - r * math.sin(ang)
        cv.line(x1, y1, x2, y2, cls="ink", extra=' stroke-width="6" stroke-linecap="round"')

        # Lực F1 hướng lên tại A(x1, y1)
        cv.arrow(x1, y1, x1, y1 - 80, cls="accent-b", head=8)
        cv.text(x1 - 10, y1 - 85, "F⃗₁", cls="lbl")

        # Lực F2 hướng xuống tại B(x2, y2)
        cv.arrow(x2, y2, x2, y2 + 80, cls="accent-b", head=8)
        cv.text(x2 + 10, y2 + 85, "F⃗₂", cls="lbl")

        # Khoảng cách d giữa hai giá của lực
        cv.line(x1, 100, x1, 260, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.line(x2, 100, x2, 260, cls="ink-thin", extra=' stroke-dasharray="3 3"')
        cv.line(x1, 220, x2, 220, cls="accent-c", extra=' stroke-width="1.8"')
        cv.arrow(x1 + 30, 220, x1, 220, cls="accent-c", head=6)
        cv.arrow(x2 - 30, 220, x2, 220, cls="accent-c", head=6)
        cv.text(cx, 214, "d", cls="lbl", anchor="middle")

        # Vòng cung quay mômen
        cv.path(f"M {cx+35} {cy-15} A 40 40 0 0 0 {cx-35} {cy+15}", cls="accent-a", extra=' fill="none" stroke-width="2"')

    else:
        # Mômen của một lực M = F·d
        cv.text(w - 20, 40, "M = F · d", cls="lbl", anchor="end", extra=' font-size="18px"')
        cv.text(w - 20, 65, "d = OA · sin α (Cánh tay đòn)", cls="lbl-sm", anchor="end")

        # Trục quay O
        ox, oy = 110.0, 220.0
        cv.circle(ox, oy, 6.0, cls="accent-a")
        cv.text(ox - 14, oy + 18, "O", cls="lbl")
        cv.text(ox - 30, oy + 32, "Trục quay", cls="lbl-sm")

        # Vật quay (thanh đòn OA)
        ax, ay = ox + 190.0, oy - 60.0
        cv.line(ox, oy, ax, ay, cls="ink", extra=' stroke-width="6" stroke-linecap="round"')
        cv.dot(ax, ay, 4.0, cls="accent-a")
        cv.text(ax + 8, ay - 6, "A (Điểm đặt lực)", cls="lbl-sm")

        # Lực F đặt tại A nghiêng góc
        fx, fy = ax + 50.0, ay - 90.0
        cv.arrow(ax, ay, fx, fy, cls="accent-b", head=8)
        cv.text(fx + 6, fy - 6, "F⃗", cls="lbl")

        # Giá của lực (đường thẳng mang vectơ F kéo dài nét đứt)
        # Hệ số góc của F: (fy - ay) / (fx - ax) = -90 / 50 = -1.8
        cv.line(ax - 70, ay + 126, fx + 25, fy - 45, cls="ink-thin", extra=' stroke-dasharray="4 3"')
        cv.text(ax - 75, ay + 140, "Giá của lực", cls="lbl-sm")

        # Hạ đường vuông góc OH từ trục O xuống giá của lực
        # Vector giá lực: u = (50, -90), norm = sqrt(2500 + 8100) = sqrt(10600) ≈ 102.96
        # Điểm A: (ax, ay). Điểm H trên đường thẳng A + t*u sao cho (H - O) . u = 0
        ux, uy = 50.0, -90.0
        u_len = math.hypot(ux, uy)
        vx, vy = ux / u_len, uy / u_len
        # toạ độ O relative to A: dx = ox - ax, dy = oy - ay
        dx, dy = ox - ax, oy - ay
        t = dx * vx + dy * vy
        hx, hy = ax + t * vx, ay + t * vy

        cv.line(ox, oy, hx, hy, cls="accent-c", extra=' stroke-width="2.2"')
        cv.dot(hx, hy, 3.5, cls="accent-c")
        cv.right_angle(hx, hy, ox, oy, ax, ay, size=10)

        cv.text(hx - 12, hy + 14, "H", cls="lbl")
        cv.text((ox + hx) / 2 - 14, (oy + hy) / 2 - 8, "d", cls="lbl", extra=' font-weight="bold"')

        # Chiều quay của mômen lực (vòng cung mũi tên)
        cv.path(f"M {ox+50} {oy-20} A 55 55 0 0 0 {ox+20} {oy-55}", cls="accent-d", extra=' fill="none" stroke-width="2"')
        cv.arrow(ox + 22, oy - 50, ox + 18, oy - 56, cls="accent-d", head=5)

    return cv.render()


def build_lever_balance(p: Params) -> str:
    """Đòn bẩy và hợp hai lực song song."""
    w, h = 460.0, 320.0
    mode = str(p.get("mode", "lever"))
    cv = Canvas(w, h, title="Quy tắc đòn bẩy và hợp lực",
                desc="Điều kiện cân bằng đòn bẩy F₁·d₁ = F₂·d₂.")

    if mode == "parallel_forces":
        # Hợp hai lực song song cùng chiều
        cv.text(w / 2, 40, "F⃗ = F⃗₁ + F⃗₂   (F = F₁ + F₂)", cls="lbl", anchor="middle", extra=' font-size="16px"')
        cv.text(w / 2, 65, "F₁ · d₁ = F₂ · d₂   (Chia trong theo tỉ lệ nghịch)", cls="lbl-sm", anchor="middle")

        # Thanh AB
        ax, bx, y0 = 80.0, 380.0, 160.0
        # Điểm O đặt hợp lực F
        ox = ax + (bx - ax) * 0.65  # O gần B hơn nếu F2 > F1
        cv.line(ax, y0, bx, y0, cls="ink", extra=' stroke-width="5" stroke-linecap="round"')

        # Lực F1 tại A
        cv.arrow(ax, y0, ax, y0 + 70, cls="accent-a", head=8)
        cv.text(ax - 10, y0 + 85, "F⃗₁", cls="lbl")

        # Lực F2 tại B
        cv.arrow(bx, y0, bx, y0 + 110, cls="accent-a", head=8)
        cv.text(bx + 8, y0 + 120, "F⃗₂", cls="lbl")

        # Hợp lực F tại O
        cv.arrow(ox, y0, ox, y0 + 145, cls="accent-b", head=9)
        cv.text(ox + 8, y0 + 155, "F⃗ = F⃗₁ + F⃗₂", cls="lbl", extra=' font-weight="bold"')

        # Điểm A, B, O
        cv.dot(ax, y0, 3.5, cls="ink")
        cv.dot(bx, y0, 3.5, cls="ink")
        cv.dot(ox, y0, 4.0, cls="accent-b")
        cv.text(ax, y0 - 10, "A", cls="lbl-sm", anchor="middle")
        cv.text(bx, y0 - 10, "B", cls="lbl-sm", anchor="middle")
        cv.text(ox, y0 - 10, "O", cls="lbl-sm", anchor="middle")

        # Khoảng cách d1, d2
        cv.line(ax, y0 - 25, ox, y0 - 25, cls="accent-c", extra=' stroke-width="1.8"')
        cv.line(ox, y0 - 25, bx, y0 - 25, cls="accent-d", extra=' stroke-width="1.8"')
        cv.text((ax + ox) / 2, y0 - 30, "d₁", cls="lbl", anchor="middle")
        cv.text((ox + bx) / 2, y0 - 30, "d₂", cls="lbl", anchor="middle")

    else:
        # Đòn bẩy quay quanh điểm tựa O
        cv.text(w / 2, 35, "F₁ · d₁ = F₂ · d₂   hay   F₁ / F₂ = d₂ / d₁",
                cls="lbl", anchor="middle", extra=' font-size="16px"')
        cv.text(w / 2, 60, "Quy tắc mômen lực cho đòn bẩy", cls="lbl-sm", anchor="middle")

        # Điểm tựa O (tam giác đỡ)
        ox, oy = 210.0, 180.0
        cv.polygon([(ox, oy), (ox - 18, oy + 32), (ox + 18, oy + 32)], cls="fill-a")
        cv.polyline([(ox, oy), (ox - 18, oy + 32), (ox + 18, oy + 32), (ox, oy)], cls="ink")
        cv.circle(ox, oy, 4.0, cls="accent-a")
        cv.text(ox, oy + 46, "Điểm tựa O", cls="lbl-sm", anchor="middle")

        # Thanh đòn AB nằm ngang
        ax, bx = 70.0, 390.0
        cv.line(ax, oy, bx, oy, cls="ink", extra=' stroke-width="6" stroke-linecap="round"')
        cv.dot(ax, oy, 4.0, cls="accent-a")
        cv.dot(bx, oy, 4.0, cls="accent-a")
        cv.text(ax - 10, oy - 12, "A", cls="lbl")
        cv.text(bx + 8, oy - 12, "B", cls="lbl")

        # Lực F1 hướng xuống tại A
        cv.arrow(ax, oy, ax, oy + 90, cls="accent-b", head=8)
        cv.text(ax - 12, oy + 105, "F⃗₁ (Tải)", cls="lbl-sm")

        # Lực F2 hướng xuống tại B
        cv.arrow(bx, oy, bx, oy + 70, cls="accent-c", head=8)
        cv.text(bx - 10, oy + 85, "F⃗₂ (Lực tác dụng)", cls="lbl-sm")

        # Kích thước d1 (OA) và d2 (OB)
        cv.line(ax, oy - 25, ox, oy - 25, cls="accent-b", extra=' stroke-width="1.8"')
        cv.line(ox, oy - 25, bx, oy - 25, cls="accent-c", extra=' stroke-width="1.8"')
        cv.arrow(ax + 20, oy - 25, ax, oy - 25, cls="accent-b", head=5)
        cv.arrow(ox - 20, oy - 25, ox, oy - 25, cls="accent-b", head=5)
        cv.arrow(ox + 20, oy - 25, ox, oy - 25, cls="accent-c", head=5)
        cv.arrow(bx - 20, oy - 25, bx, oy - 25, cls="accent-c", head=5)

        cv.text((ax + ox) / 2, oy - 32, "d₁", cls="lbl", anchor="middle")
        cv.text((ox + bx) / 2, oy - 32, "d₂", cls="lbl", anchor="middle")

        # Nhãn lợi về lực khi d2 > d1
        cv.text(w / 2, h - 20, "Nếu d₂ > d₁ thì F₂ < F₁ (Được lợi về lực)", cls="lbl-sm", anchor="middle")

    return cv.render()


def build_equilibrium_3forces(p: Params) -> str:
    """Cân bằng của vật rắn dưới tác dụng của ba lực không song song."""
    w, h = 460.0, 320.0
    cv = Canvas(w, h, title="Cân bằng ba lực không song song",
                desc="Ba lực đồng phẳng và đồng quy: F₁ + F₂ + F₃ = 0.")

    # Tiêu đề công thức
    cv.text(w / 2, 35, "F⃗₁ + F⃗₂ + F⃗₃ = 0⃗", cls="lbl", anchor="middle", extra=' font-size="18px"')
    cv.text(w / 2, 60, "Ba lực không song song phải đồng phẳng và đồng quy", cls="lbl-sm", anchor="middle")

    # Vật rắn bất kỳ (đa giác bo cong)
    body_pts = [
        (100.0, 150.0), (140.0, 100.0), (240.0, 110.0),
        (280.0, 180.0), (250.0, 250.0), (130.0, 230.0)
    ]
    cv.polygon(body_pts, cls="fill-a")
    cv.polyline(body_pts + [body_pts[0]], cls="ink")

    # Điểm đồng quy O
    ox, oy = 190.0, 175.0
    cv.dot(ox, oy, 3.5, cls="accent-a")
    cv.text(ox + 8, oy + 4, "O (Điểm đồng quy)", cls="lbl-sm")

    # Ba lực xuất phát từ 3 điểm trên vật A1, A2, A3
    # Lực 1: hướng sang trái chếch lên
    f1_ang = math.radians(160)
    # Lực 2: hướng sang phải chếch lên
    f2_ang = math.radians(35)
    # Lực 3: hướng thẳng xuống cân bằng: F3 = -(F1 + F2)
    f1_mag, f2_mag = 70.0, 75.0
    f1x, f1y = f1_mag * math.cos(f1_ang), f1_mag * math.sin(f1_ang)
    f2x, f2y = f2_mag * math.cos(f2_ang), f2_mag * math.sin(f2_ang)
    f3x, f3y = -(f1x + f2x), -(f1y + f2y)

    # Điểm đặt lực
    p1 = (ox + 35 * math.cos(f1_ang), oy + 35 * math.sin(f1_ang))
    p2 = (ox + 40 * math.cos(f2_ang), oy + 40 * math.sin(f2_ang))
    p3 = (ox + 30 * (f3x / math.hypot(f3x, f3y)), oy + 30 * (f3y / math.hypot(f3x, f3y)))

    # Giá của lực nét đứt hội tụ về O
    cv.line(ox, oy, p1[0], p1[1], cls="ink-thin", extra=' stroke-dasharray="3 3"')
    cv.line(ox, oy, p2[0], p2[1], cls="ink-thin", extra=' stroke-dasharray="3 3"')
    cv.line(ox, oy, p3[0], p3[1], cls="ink-thin", extra=' stroke-dasharray="3 3"')

    # Vẽ 3 vectơ lực
    cv.arrow(p1[0], p1[1], p1[0] + f1x, p1[1] + f1y, cls="accent-b", head=7)
    cv.arrow(p2[0], p2[1], p2[0] + f2x, p2[1] + f2y, cls="accent-b", head=7)
    cv.arrow(p3[0], p3[1], p3[0] + f3x, p3[1] + f3y, cls="accent-b", head=7)

    cv.text(p1[0] + f1x - 12, p1[1] + f1y, "F⃗₁", cls="lbl")
    cv.text(p2[0] + f2x + 6, p2[1] + f2y - 4, "F⃗₂", cls="lbl")
    cv.text(p3[0] + f3x + 6, p3[1] + f3y + 16, "F⃗₃", cls="lbl")

    # Tam giác lực ở góc phải
    tx, ty = 360.0, 220.0
    cv.arrow(tx, ty, tx + f1x * 0.7, ty + f1y * 0.7, cls="accent-c", head=5)
    t1x, t1y = tx + f1x * 0.7, ty + f1y * 0.7
    cv.arrow(t1x, t1y, t1x + f2x * 0.7, t1y + f2y * 0.7, cls="accent-c", head=5)
    t2x, t2y = t1x + f2x * 0.7, t1y + f2y * 0.7
    cv.arrow(t2x, t2y, tx, ty, cls="accent-c", head=5)
    cv.text(tx - 20, ty - 50, "Tam giác lực khép kín", cls="lbl-sm")

    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "torque_moment": build_torque_moment,
    "lever_balance": build_lever_balance,
    "equilibrium_3forces": build_equilibrium_3forces,
}
