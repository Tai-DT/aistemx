"""Xác suất, Quá trình Ngẫu nhiên và Mô phỏng Monte Carlo cho AIstem.

Hỗ trợ:
- Bảng Galton (Quincunx) & Định lý Giới hạn Trung tâm (CLT)
- Phương pháp Monte Carlo: Ước lượng số Pi, Tích phân đa chiều
- Bước đi ngẫu nhiên 2D/3D (Random Walk)
"""
from __future__ import annotations

import math
import random
from typing import Any


def simulate_galton_board(
    num_balls: int = 1000,
    rows: int = 16,
    prob_right: float = 0.5,
) -> dict[str, Any]:
    """Mô phỏng bảng Galton với num_balls viên bi rơi qua rows hàng đinh."""
    num_bins = rows + 1
    bins = [0] * num_bins
    sample_trajectories = []

    # Lưu vết đường rơi của 5 viên bi đầu tiên làm mẫu trực quan
    for i in range(num_balls):
        bin_idx = 0
        path = [0]
        for _ in range(rows):
            if random.random() < prob_right:
                bin_idx += 1
            path.append(bin_idx)
        bins[bin_idx] += 1
        if i < 5:
            sample_trajectories.append(path)

    # Tính phân phối chuẩn lý thuyết tương ứng: N(mu, sigma^2)
    mu = rows * prob_right
    sigma = math.sqrt(rows * prob_right * (1.0 - prob_right))
    
    theoretical_curve = []
    for k in range(num_bins):
        # f(x) = (1 / (sigma * sqrt(2*pi))) * exp(- (x - mu)^2 / (2*sigma^2))
        gauss = (1.0 / (sigma * math.sqrt(2.0 * math.pi))) * math.exp(-0.5 * ((k - mu) / sigma) ** 2)
        theoretical_curve.append(round(gauss * num_balls, 2))

    return {
        "parameters": {"num_balls": num_balls, "rows": rows, "p": prob_right},
        "bins": bins,
        "theoretical_gaussian": theoretical_curve,
        "mean": round(mu, 3),
        "std_dev": round(sigma, 3),
        "sample_trajectories": sample_trajectories,
    }


def monte_carlo_pi(num_samples: int = 10000) -> dict[str, Any]:
    """Ước lượng số Pi bằng cách thả điểm ngẫu nhiên vào hình vuông [-1, 1]x[-1, 1]."""
    inside_count = 0
    sample_points = []

    for i in range(num_samples):
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)
        is_inside = (x * x + y * y) <= 1.0
        if is_inside:
            inside_count += 1
        # Lưu 100 điểm đầu để vẽ minh họa
        if i < 100:
            sample_points.append({"x": round(x, 4), "y": round(y, 4), "inside": is_inside})

    pi_estimate = 4.0 * inside_count / num_samples
    error = abs(pi_estimate - math.pi)

    return {
        "samples": num_samples,
        "inside_count": inside_count,
        "pi_estimate": round(pi_estimate, 6),
        "actual_pi": round(math.pi, 6),
        "absolute_error": round(error, 6),
        "relative_error_pct": round((error / math.pi) * 100.0, 4),
        "sample_points": sample_points,
    }


def random_walk_2d(steps: int = 500) -> dict[str, Any]:
    """Mô phỏng bước đi ngẫu nhiên 2D (chuyển động Brown)."""
    trajectory = [{"x": 0.0, "y": 0.0}]
    x, y = 0.0, 0.0

    for _ in range(steps):
        angle = random.uniform(0.0, 2.0 * math.pi)
        x += math.cos(angle)
        y += math.sin(angle)
        trajectory.append({"x": round(x, 3), "y": round(y, 3)})

    end_distance = math.hypot(x, y)
    theoretical_distance = math.sqrt(steps)

    return {
        "steps": steps,
        "trajectory": trajectory,
        "end_distance": round(end_distance, 3),
        "theoretical_root_n": round(theoretical_distance, 3),
    }
