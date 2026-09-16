"""Giải tích số: Tìm nghiệm phi tuyến, Tích phân và Đạo hàm cho AIstem.

Hỗ trợ:
- Tìm nghiệm: Newton-Raphson, Bisection Method
- Tích phân số: Simpson 1/3, Cầu phương Gauss-Legendre 3-điểm và 5-điểm
- Đạo hàm số: Sai phân hữu hạn trung tâm
"""
from __future__ import annotations

import math
from typing import Callable, Any


def newton_raphson_solve(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> dict[str, Any]:
    """Tìm nghiệm f(x) = 0 bằng phương pháp Newton-Raphson với lịch sử từng bước."""
    history = [{"step": 0, "x": round(x0, 6), "fx": round(f(x0), 6)}]
    x = x0
    
    for i in range(1, max_iter + 1):
        fx = f(x)
        if abs(fx) < tol:
            return {
                "converged": True,
                "root": round(x, 7),
                "iterations": i,
                "history": history,
            }
        dfx = df(x)
        if abs(dfx) < 1e-12:
            return {
                "converged": False,
                "error": "Đạo hàm xấp xỉ 0 (tiếp tuyến nằm ngang), không thể tiếp tục.",
                "last_x": round(x, 7),
                "history": history,
            }
        x_next = x - fx / dfx
        history.append({"step": i, "x": round(x_next, 6), "fx": round(f(x_next), 6)})
        if abs(x_next - x) < tol:
            return {
                "converged": True,
                "root": round(x_next, 7),
                "iterations": i,
                "history": history,
            }
        x = x_next

    return {
        "converged": False,
        "root": round(x, 7),
        "iterations": max_iter,
        "history": history,
    }


def bisection_solve(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-7,
    max_iter: int = 100,
) -> dict[str, Any]:
    """Tìm nghiệm bằng phương pháp chia đôi (Bisection) đảm bảo hội tụ nếu f(a)*f(b) < 0."""
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return {
            "converged": False,
            "error": f"f(a)={fa} và f(b)={fb} cùng dấu, không đảm bảo có nghiệm trong [a, b].",
        }

    history = []
    c = a
    for i in range(1, max_iter + 1):
        c = (a + b) / 2.0
        fc = f(c)
        history.append({"step": i, "a": round(a, 6), "b": round(b, 6), "mid": round(c, 6), "fc": round(fc, 6)})
        
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            return {
                "converged": True,
                "root": round(c, 7),
                "iterations": i,
                "history": history,
            }
        if f(a) * fc < 0:
            b = c
        else:
            a = c

    return {
        "converged": True,
        "root": round(c, 7),
        "iterations": max_iter,
        "history": history,
    }


def simpson_integrate(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int = 100,
) -> dict[str, Any]:
    """Tích phân số bằng công thức Simpson 1/3."""
    if n % 2 != 0:
        n += 1  # n phải là số chẵn
    h = (b - a) / n
    total = f(a) + f(b)
    
    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 1:
            total += 4.0 * f(x_i)
        else:
            total += 2.0 * f(x_i)
            
    res = (h / 3.0) * total
    return {
        "integral": round(res, 8),
        "intervals": n,
        "step_size": round(h, 6),
    }


def gauss_legendre_3pt(
    f: Callable[[float], float],
    a: float,
    b: float,
) -> float:
    """Cầu phương Gauss-Legendre 3-điểm (độ chính xác đại số bậc 5)."""
    t1 = -math.sqrt(3.0 / 5.0)
    t2 = 0.0
    t3 = math.sqrt(3.0 / 5.0)
    w1 = 5.0 / 9.0
    w2 = 8.0 / 9.0
    w3 = 5.0 / 9.0

    scale = (b - a) / 2.0
    shift = (a + b) / 2.0
    
    val = (
        w1 * f(scale * t1 + shift)
        + w2 * f(scale * t2 + shift)
        + w3 * f(scale * t3 + shift)
    )
    return scale * val


def central_difference_derivative(
    f: Callable[[float], float],
    x: float,
    h: float = 1e-5,
) -> dict[str, float]:
    """Tính đạo hàm cấp 1 và cấp 2 bằng sai phân trung tâm O(h^2)."""
    df = (f(x + h) - f(x - h)) / (2.0 * h)
    d2f = (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)
    return {
        "f_prime": round(df, 7),
        "f_double_prime": round(d2f, 7),
    }
