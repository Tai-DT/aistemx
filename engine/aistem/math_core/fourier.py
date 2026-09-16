"""Phân tích Fourier và Biến đổi Fourier Nhanh (FFT) cho AIstem.

Hỗ trợ:
- Khai triển chuỗi Fourier hàm chuẩn (sóng vuông, tam giác, răng cưa, xung)
- Biến đổi Fourier Nhanh (Cooley-Tukey FFT O(N log N))
- Phân rã ngoại luân (Epicycles Decomposition) từ đường cong 2D bất kỳ
"""
from __future__ import annotations

import cmath
import math
from typing import Any, Sequence


def fourier_series_wave(
    wave_type: str = "square",
    harmonics: int = 7,
    points: int = 500,
    frequency: float = 1.0,
) -> dict[str, Any]:
    """Tính toán xấp xỉ chuỗi Fourier cho các dạng sóng cơ bản qua N họa tần."""
    omega = 2.0 * math.pi * frequency
    t_values = [i / (points - 1) for i in range(points)]
    wave_approx = []
    spectrum = []

    for n in range(1, harmonics + 1):
        amp = 0.0
        # Tính hệ số biên độ theo dạng sóng
        if wave_type == "square":
            # Sóng vuông: chỉ có họa tần lẻ (2k-1), biên độ = 4 / (pi * n)
            if n % 2 != 0:
                amp = 4.0 / (math.pi * n)
        elif wave_type == "sawtooth":
            # Sóng răng cưa: biên độ = 2 * (-1)^(n+1) / (pi * n)
            amp = 2.0 * ((-1) ** (n + 1)) / (math.pi * n)
        elif wave_type == "triangle":
            # Sóng tam giác: chỉ có họa tần lẻ, biên độ = 8 * (-1)^((n-1)/2) / (pi^2 * n^2)
            if n % 2 != 0:
                k = (n - 1) // 2
                amp = (8.0 * ((-1) ** k)) / ((math.pi * n) ** 2)
        elif wave_type == "pulse":
            # Sóng xung hẹp (duty cycle 25%)
            amp = (2.0 / (math.pi * n)) * math.sin(n * math.pi * 0.25)
        else:
            amp = 1.0 / n

        spectrum.append({"harmonic": n, "frequency": n * frequency, "amplitude": round(amp, 6)})

    # Tổng hợp sóng
    for t in t_values:
        val = 0.0
        for item in spectrum:
            n = item["harmonic"]
            amp = item["amplitude"]
            val += amp * math.sin(n * omega * t)
        wave_approx.append(round(val, 6))

    return {
        "wave_type": wave_type,
        "harmonics_count": harmonics,
        "time": t_values,
        "signal": wave_approx,
        "spectrum": spectrum,
    }


def cooley_tukey_fft(x: Sequence[complex]) -> list[complex]:
    """Biến đổi Fourier Nhanh Cooley-Tukey đệ quy O(N log N).
    
    Yêu cầu độ dài len(x) là lũy thừa của 2.
    """
    n = len(x)
    if n <= 1:
        return list(x)
    
    # Kiểm tra n có phải lũy thừa của 2 không
    if (n & (n - 1)) != 0:
        # Zero-padding tới lũy thừa của 2 gần nhất
        next_power = 1 << (n - 1).bit_length()
        padded = list(x) + [0j] * (next_power - n)
        return cooley_tukey_fft(padded)

    even = cooley_tukey_fft(x[0::2])
    odd = cooley_tukey_fft(x[1::2])

    t_factors = [cmath.exp(-2j * cmath.pi * k / n) * odd[k] for k in range(n // 2)]
    return (
        [even[k] + t_factors[k] for k in range(n // 2)]
        + [even[k] - t_factors[k] for k in range(n // 2)]
    )


def compute_dft_epicycles(points: list[tuple[float, float]]) -> list[dict[str, Any]]:
    """Phân rã đường cong 2D kín thành chuỗi các vòng tròn Epicycles.
    
    Mỗi phần tử epicycle chứa:
    - freq: tần số góc n
    - radius: bán kính vòng tròn |c_n|
    - phase: góc pha ban đầu arg(c_n)
    """
    N = len(points)
    if N == 0:
        return []

    # Chuyển (x, y) thành số phức z = x + i*y
    complex_points = [complex(p[0], p[1]) for p in points]
    epicycles = []

    for k in range(N):
        # Tính hệ số Fourier c_k
        c_k = 0j
        for n in range(N):
            phi = (2.0 * math.pi * k * n) / N
            c_k += complex_points[n] * cmath.exp(-1j * phi)
        c_k /= N

        radius = abs(c_k)
        phase = cmath.phase(c_k)
        epicycles.append({
            "freq": k,
            "radius": round(radius, 4),
            "phase": round(phase, 4),
            "re": round(c_k.real, 4),
            "im": round(c_k.imag, 4),
        })

    # Sắp xếp theo bán kính giảm dần để các vòng tròn lớn vẽ trước
    epicycles.sort(key=lambda item: item["radius"], reverse=True)
    return epicycles
