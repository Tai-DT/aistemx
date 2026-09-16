"""AISTEM Mathematical Core Engine.

Gói giải thuật số học và giải tích chính xác cao cho STEM.
"""
from aistem.math_core.ode import (
    rk4_step,
    simulate_rk4_trajectory,
    simulate_nonlinear_pendulum,
    simulate_lorenz_attractor,
    simulate_kepler_orbit,
)
from aistem.math_core.fourier import (
    fourier_series_wave,
    cooley_tukey_fft,
    compute_dft_epicycles,
)
from aistem.math_core.linear_algebra import (
    matrix_2x2_properties,
    power_iteration_dominant_eigen,
    svd_2x2,
)
from aistem.math_core.calculus import (
    newton_raphson_solve,
    bisection_solve,
    simpson_integrate,
    gauss_legendre_3pt,
    central_difference_derivative,
)
from aistem.math_core.stochastics import (
    simulate_galton_board,
    monte_carlo_pi,
    random_walk_2d,
)
from aistem.math_core.geometry import (
    evaluate_cubic_bezier,
    intersect_lines,
    intersect_two_circles,
    convex_hull_2d,
)

__all__ = [
    "rk4_step",
    "simulate_rk4_trajectory",
    "simulate_nonlinear_pendulum",
    "simulate_lorenz_attractor",
    "simulate_kepler_orbit",
    "fourier_series_wave",
    "cooley_tukey_fft",
    "compute_dft_epicycles",
    "matrix_2x2_properties",
    "power_iteration_dominant_eigen",
    "svd_2x2",
    "newton_raphson_solve",
    "bisection_solve",
    "simpson_integrate",
    "gauss_legendre_3pt",
    "central_difference_derivative",
    "simulate_galton_board",
    "monte_carlo_pi",
    "random_walk_2d",
    "evaluate_cubic_bezier",
    "intersect_lines",
    "intersect_two_circles",
    "convex_hull_2d",
]
