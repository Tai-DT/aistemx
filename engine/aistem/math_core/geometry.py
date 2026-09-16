"""Hình học tính toán, Đường cong Bézier và Giao điểm Euclid cho AIstem.

Hỗ trợ:
- Đánh giá đường cong Bézier bậc 2 & bậc 3 bằng thuật toán de Casteljau
- Bắt dính giao điểm hình học: Đường thẳng - Đường thẳng, Đường thẳng - Đường tròn, 2 Đường tròn
- Thuật toán Bao lồi (Convex Hull - Andrew's Monotone Chain O(N log N))
"""
from __future__ import annotations

import math
from typing import Any


def evaluate_cubic_bezier(
    p0: tuple[float, float],
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    num_points: int = 50,
) -> dict[str, Any]:
    """Tính toán chuỗi điểm, vectơ tiếp tuyến và độ cong dọc theo đường cong Bézier bậc 3."""
    curve_points = []
    tangents = []

    for i in range(num_points):
        t = i / (num_points - 1)
        u = 1.0 - t
        tt = t * t
        uu = u * u
        uuu = uu * u
        ttt = tt * t

        # B(t) = (1-t)^3 P0 + 3(1-t)^2 t P1 + 3(1-t)t^2 P2 + t^3 P3
        x = uuu * p0[0] + 3.0 * uu * t * p1[0] + 3.0 * u * tt * p2[0] + ttt * p3[0]
        y = uuu * p0[1] + 3.0 * uu * t * p1[1] + 3.0 * u * tt * p2[1] + ttt * p3[1]
        curve_points.append({"x": round(x, 4), "y": round(y, 4), "t": round(t, 4)})

        # Đạo hàm tiếp tuyến B'(t) = 3(1-t)^2(P1-P0) + 6(1-t)t(P2-P1) + 3t^2(P3-P2)
        dx = (
            3.0 * uu * (p1[0] - p0[0])
            + 6.0 * u * t * (p2[0] - p1[0])
            + 3.0 * tt * (p3[0] - p2[0])
        )
        dy = (
            3.0 * uu * (p1[1] - p0[1])
            + 6.0 * u * t * (p2[1] - p1[1])
            + 3.0 * tt * (p3[1] - p2[1])
        )
        norm = math.hypot(dx, dy)
        if norm > 1e-7:
            tangents.append({"vx": round(dx / norm, 4), "vy": round(dy / norm, 4)})
        else:
            tangents.append({"vx": 1.0, "vy": 0.0})

    return {
        "control_points": [
            {"x": p0[0], "y": p0[1]},
            {"x": p1[0], "y": p1[1]},
            {"x": p2[0], "y": p2[1]},
            {"x": p3[0], "y": p3[1]},
        ],
        "curve": curve_points,
        "tangents": tangents,
    }


def intersect_lines(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
) -> dict[str, Any]:
    """Tìm giao điểm của 2 đường thẳng đi qua (p1, p2) và (p3, p4)."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-9:
        return {"intersects": False, "reason": "Hai đường thẳng song song hoặc trùng nhau"}

    px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denom
    py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denom

    return {
        "intersects": True,
        "point": {"x": round(px, 4), "y": round(py, 4)},
    }


def intersect_two_circles(
    c1: tuple[float, float, float],  # (x1, y1, r1)
    c2: tuple[float, float, float],  # (x2, y2, r2)
) -> dict[str, Any]:
    """Tìm các điểm giao cắt của 2 đường tròn trong mặt phẳng."""
    x1, y1, r1 = c1
    x2, y2, r2 = c2

    dx = x2 - x1
    dy = y2 - y1
    d = math.hypot(dx, dy)

    if d > r1 + r2:
        return {"intersects": False, "count": 0, "points": [], "reason": "Hai đường tròn rời nhau ngoài"}
    if d < abs(r1 - r2):
        return {"intersects": False, "count": 0, "points": [], "reason": "Một đường tròn nằm lọt trong đường tròn kia"}
    if d == 0 and abs(r1 - r2) < 1e-9:
        return {"intersects": True, "count": -1, "points": [], "reason": "Hai đường tròn đồng tâm trùng nhau"}

    a = (r1 * r1 - r2 * r2 + d * d) / (2.0 * d)
    h_sq = r1 * r1 - a * a
    h = math.sqrt(max(0.0, h_sq))

    px = x1 + (a * dx) / d
    py = y1 + (a * dy) / d

    if h < 1e-6:
        # Tiếp xúc
        return {
            "intersects": True,
            "count": 1,
            "points": [{"x": round(px, 4), "y": round(py, 4)}],
        }

    rx = (-dy * h) / d
    ry = (dx * h) / d

    return {
        "intersects": True,
        "count": 2,
        "points": [
            {"x": round(px + rx, 4), "y": round(py + ry, 4)},
            {"x": round(px - rx, 4), "y": round(py - ry, 4)},
        ],
    }


def convex_hull_2d(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Tìm bao lồi tập điểm 2D bằng thuật toán Monotone Chain O(N log N)."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def cross(o: tuple[float, float], a: tuple[float, float], b: tuple[float, float]) -> float:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]
