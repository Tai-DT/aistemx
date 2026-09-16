"""Unit tests cho module math_core."""
import math
import pytest

try:
    from aistem.math_core.ode import (
        rk4_step,
        simulate_nonlinear_pendulum,
        simulate_lorenz_attractor,
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
    )
    from aistem.math_core.geometry import (
        evaluate_cubic_bezier,
        intersect_lines,
        intersect_two_circles,
        convex_hull_2d,
    )
except ImportError:
    from engine.aistem.math_core.ode import (
        rk4_step,
        simulate_nonlinear_pendulum,
        simulate_lorenz_attractor,
    )
    from engine.aistem.math_core.fourier import (
        fourier_series_wave,
        cooley_tukey_fft,
        compute_dft_epicycles,
    )
    from engine.aistem.math_core.linear_algebra import (
        matrix_2x2_properties,
        power_iteration_dominant_eigen,
        svd_2x2,
    )
    from engine.aistem.math_core.calculus import (
        newton_raphson_solve,
        bisection_solve,
        simpson_integrate,
        gauss_legendre_3pt,
        central_difference_derivative,
    )
    from engine.aistem.math_core.stochastics import (
        simulate_galton_board,
        monte_carlo_pi,
    )
    from engine.aistem.math_core.geometry import (
        evaluate_cubic_bezier,
        intersect_lines,
        intersect_two_circles,
        convex_hull_2d,
    )


def test_rk4_pendulum_conservation():
    sim = simulate_nonlinear_pendulum(theta0=0.5, omega0=0.0, damping=0.0, dt=0.01, steps=200)
    assert sim["conserved"] is True
    energies = sim["energy"]
    e_start = energies[0]
    e_end = energies[-1]
    assert abs(e_end - e_start) / e_start < 0.005


def test_lorenz_attractor():
    sim = simulate_lorenz_attractor(steps=100)
    assert len(sim["points"]) == 101
    assert "x" in sim["points"][0] and "z" in sim["points"][0]


def test_fourier_wave_and_fft():
    fw = fourier_series_wave(wave_type="square", harmonics=5, points=100)
    assert len(fw["signal"]) == 100
    assert len(fw["spectrum"]) == 5
    assert fw["spectrum"][1]["amplitude"] == 0.0

    data = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
    res = cooley_tukey_fft(data)
    assert len(res) == 8
    assert abs(res[0] - 4.0) < 1e-6


def test_matrix_properties_and_eigen():
    props = matrix_2x2_properties(2.0, 0.0, 0.0, 3.0)
    assert props["determinant"] == 6.0
    assert props["trace"] == 5.0
    assert 3.0 in props["eigenvalues"] and 2.0 in props["eigenvalues"]

    svd = svd_2x2(3.0, 0.0, 0.0, 4.0)
    assert svd["rank"] == 2
    assert 4.0 in svd["singular_values"] and 3.0 in svd["singular_values"]


def test_calculus_solvers():
    res = newton_raphson_solve(lambda x: x**2 - 4.0, lambda x: 2.0 * x, x0=3.0)
    assert res["converged"] is True
    assert abs(res["root"] - 2.0) < 1e-5

    simpson = simpson_integrate(lambda x: x**2, 0.0, 3.0, n=20)
    assert abs(simpson["integral"] - 9.0) < 1e-5

    gauss = gauss_legendre_3pt(lambda x: x**4, 0.0, 1.0)
    assert abs(gauss - 0.2) < 1e-6


def test_stochastics():
    galton = simulate_galton_board(num_balls=500, rows=10)
    assert len(galton["bins"]) == 11
    assert sum(galton["bins"]) == 500

    mc = monte_carlo_pi(num_samples=1000)
    assert 2.7 < mc["pi_estimate"] < 3.6


def test_geometry():
    bez = evaluate_cubic_bezier((0, 0), (1, 2), (2, 2), (3, 0), num_points=20)
    assert len(bez["curve"]) == 20

    res = intersect_two_circles((0.0, 0.0, 5.0), (6.0, 0.0, 5.0))
    assert res["intersects"] is True
    assert res["count"] == 2
    pts = res["points"]
    y_coords = {round(p["y"], 1) for p in pts}
    assert 4.0 in y_coords and -4.0 in y_coords
