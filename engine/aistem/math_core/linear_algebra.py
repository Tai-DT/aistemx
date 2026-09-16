"""Đại số tuyến tính và Thuật toán Ma trận cho AIstem.

Hỗ trợ:
- Biến đổi ma trận không gian 2D/3D (Affine Transformations)
- Tính định thức, vết, hạng, ma trận nghịch đảo
- Trị riêng & Vectơ riêng (Eigenvalues & Eigenvectors: Công thức đại số & Power Iteration)
- Phân rã giá trị kỳ dị (SVD) & Xấp xỉ hạng thấp
"""
from __future__ import annotations

import math
from typing import Any


def matrix_2x2_properties(a: float, b: float, c: float, d: float) -> dict[str, Any]:
    """Phân tích đầy đủ tính chất của ma trận A = [[a, b], [c, d]]."""
    det = a * d - b * c
    trace = a + d
    
    # Phương trình đặc trưng: lambda^2 - trace*lambda + det = 0
    delta = trace * trace - 4.0 * det
    
    eigenvalues: list[Any] = []
    eigenvectors: list[Any] = []
    
    if delta >= 0:
        l1 = (trace + math.sqrt(delta)) / 2.0
        l2 = (trace - math.sqrt(delta)) / 2.0
        eigenvalues = [round(l1, 4), round(l2, 4)]
        
        # Tìm vector riêng cho l1
        # (a - l1)*x + b*y = 0
        for l in [l1, l2]:
            if abs(b) > 1e-7:
                vx, vy = -b, a - l
            elif abs(c) > 1e-7:
                vx, vy = d - l, -c
            else:
                # Ma trận đường chéo
                vx, vy = (1.0, 0.0) if abs(a - l) < 1e-7 else (0.0, 1.0)
            norm = math.hypot(vx, vy)
            if norm > 1e-7:
                eigenvectors.append({"x": round(vx / norm, 4), "y": round(vy / norm, 4)})
            else:
                eigenvectors.append({"x": 1.0, "y": 0.0})
    else:
        # Nghiệm phức
        real_part = trace / 2.0
        imag_part = math.sqrt(-delta) / 2.0
        eigenvalues = [
            f"{round(real_part, 4)} + {round(imag_part, 4)}i",
            f"{round(real_part, 4)} - {round(imag_part, 4)}i",
        ]

    # Ma trận nghịch đảo
    inverse = None
    if abs(det) > 1e-9:
        inverse = [
            [round(d / det, 4), round(-b / det, 4)],
            [round(-c / det, 4), round(a / det, 4)],
        ]

    # Lưới tọa độ biến đổi (Unit square [0,0]->[1,0]->[1,1]->[0,1])
    transformed_unit_square = [
        {"x": 0.0, "y": 0.0},
        {"x": round(a, 4), "y": round(c, 4)},
        {"x": round(a + b, 4), "y": round(c + d, 4)},
        {"x": round(b, 4), "y": round(d, 4)},
    ]

    return {
        "matrix": [[a, b], [c, d]],
        "determinant": round(det, 4),
        "trace": round(trace, 4),
        "is_singular": abs(det) < 1e-9,
        "eigenvalues": eigenvalues,
        "eigenvectors": eigenvectors,
        "inverse": inverse,
        "transformed_unit_square": transformed_unit_square,
    }


def power_iteration_dominant_eigen(
    A: list[list[float]],
    max_iter: int = 100,
    tol: float = 1e-8,
) -> dict[str, Any]:
    """Thuật toán lặp lũy thừa tìm trị riêng cực đại và vectơ riêng của ma trận thực nxn."""
    n = len(A)
    # Khởi tạo vector ngẫu nhiên
    v = [1.0 / math.sqrt(n)] * n
    eigenvalue = 0.0

    for it in range(max_iter):
        # Nhân A * v
        w = [sum(A[i][j] * v[j] for j in range(n)) for i in range(n)]
        
        # Chuẩn hóa w
        norm = math.sqrt(sum(x * x for x in w))
        if norm < 1e-12:
            break
        v_next = [x / norm for x in w]
        
        # Rayleigh Quotient
        Av = [sum(A[i][j] * v_next[j] for j in range(n)) for i in range(n)]
        lam = sum(v_next[i] * Av[i] for i in range(n))
        
        if abs(lam - eigenvalue) < tol:
            eigenvalue = lam
            v = v_next
            return {
                "converged": True,
                "iterations": it + 1,
                "dominant_eigenvalue": round(eigenvalue, 6),
                "eigenvector": [round(x, 6) for x in v],
            }
        eigenvalue = lam
        v = v_next

    return {
        "converged": False,
        "iterations": max_iter,
        "dominant_eigenvalue": round(eigenvalue, 6),
        "eigenvector": [round(x, 6) for x in v],
    }


def svd_2x2(a: float, b: float, c: float, d: float) -> dict[str, Any]:
    """Phân rã SVD A = U * Sigma * V^T cho ma trận 2x2.
    
    A^T * A có các trị riêng là sigma_1^2, sigma_2^2.
    """
    # Tính A^T * A
    ata_00 = a * a + c * c
    ata_01 = a * b + c * d
    ata_11 = b * b + d * d
    
    prop = matrix_2x2_properties(ata_00, ata_01, ata_01, ata_11)
    eigs = prop["eigenvalues"]
    if isinstance(eigs[0], (int, float)) and isinstance(eigs[1], (int, float)):
        s1 = math.sqrt(max(0.0, eigs[0]))
        s2 = math.sqrt(max(0.0, eigs[1]))
    else:
        s1, s2 = 0.0, 0.0

    return {
        "singular_values": [round(s1, 4), round(s2, 4)],
        "condition_number": round(s1 / s2, 4) if s2 > 1e-9 else "inf",
        "rank": 2 if (s1 > 1e-7 and s2 > 1e-7) else (1 if s1 > 1e-7 else 0),
    }
