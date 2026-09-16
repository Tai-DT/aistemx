"""Bộ giải phương trình vi phân thường (ODEs) chính xác cao bằng Runge-Kutta 4 (RK4).

Hỗ trợ các hệ động lực kinh điển trong STEM:
- Con lắc đơn phi tuyến (Nonlinear Pendulum)
- Hệ hỗn loạn Lorenz Attractor
- Dao động điều hòa có cản & lực cưỡng bức (Damped & Forced Harmonic Oscillator)
- Chuyển động trường hấp dẫn 2-vật & 3-vật (Keplerian orbits)
"""
from __future__ import annotations

import math
from typing import Callable, Sequence, Any


def rk4_step(
    f: Callable[[float, list[float]], Sequence[float]],
    t: float,
    y: list[float],
    dt: float,
) -> list[float]:
    """Một bước tích phân Runge-Kutta bậc 4 (RK4) cho hệ vi phân dy/dt = f(t, y).
    
    Sai số cục bộ O(dt^5), sai số toàn cục O(dt^4).
    """
    n = len(y)
    
    # k1 = f(t, y)
    k1 = [float(v) for v in f(t, y)]
    
    # k2 = f(t + dt/2, y + dt/2 * k1)
    y_k2 = [y[i] + 0.5 * dt * k1[i] for i in range(n)]
    k2 = [float(v) for v in f(t + 0.5 * dt, y_k2)]
    
    # k3 = f(t + dt/2, y + dt/2 * k2)
    y_k3 = [y[i] + 0.5 * dt * k2[i] for i in range(n)]
    k3 = [float(v) for v in f(t + 0.5 * dt, y_k3)]
    
    # k4 = f(t + dt, y + dt * k3)
    y_k4 = [y[i] + dt * k3[i] for i in range(n)]
    k4 = [float(v) for v in f(t + dt, y_k4)]
    
    # y_{n+1} = y_n + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    return [
        y[i] + (dt / 6.0) * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i])
        for i in range(n)
    ]


def simulate_rk4_trajectory(
    f: Callable[[float, list[float]], Sequence[float]],
    t0: float,
    y0: list[float],
    dt: float,
    steps: int,
) -> dict[str, list[Any]]:
    """Tích phân hệ vi phân qua nhiều bước thời gian."""
    t_list = [t0]
    trajectory = [[float(v) for v in y0]]
    
    curr_t = t0
    curr_y = [float(v) for v in y0]
    
    for _ in range(steps):
        curr_y = rk4_step(f, curr_t, curr_y, dt)
        curr_t += dt
        t_list.append(round(curr_t, 6))
        trajectory.append([round(v, 6) for v in curr_y])
        
    return {
        "time": t_list,
        "trajectory": trajectory,
        "final_state": trajectory[-1],
    }


def simulate_nonlinear_pendulum(
    theta0: float,
    omega0: float = 0.0,
    g: float = 9.81,
    length: float = 1.0,
    damping: float = 0.05,
    dt: float = 0.02,
    steps: int = 500,
) -> dict[str, Any]:
    """Mô phỏng con lắc đơn phi tuyến: d^2(theta)/dt^2 + (g/L)*sin(theta) + damping*omega = 0.
    
    y = [theta, omega]
    d(theta)/dt = omega
    d(omega)/dt = -(g/L)*sin(theta) - damping*omega
    """
    def deriv(_t: float, y: list[float]) -> list[float]:
        theta, omega = y[0], y[1]
        d_theta = omega
        d_omega = -(g / length) * math.sin(theta) - damping * omega
        return [d_theta, d_omega]

    sim = simulate_rk4_trajectory(deriv, 0.0, [theta0, omega0], dt, steps)
    
    # Tính cơ năng: E = E_kin + E_pot = 0.5*m*(L*omega)^2 + m*g*L*(1 - cos(theta)) với m=1kg
    energies = []
    for state in sim["trajectory"]:
        th, om = state[0], state[1]
        e_kin = 0.5 * (length * om) ** 2
        e_pot = g * length * (1.0 - math.cos(th))
        energies.append(round(e_kin + e_pot, 4))

    return {
        "system": "nonlinear_pendulum",
        "parameters": {"g": g, "length": length, "damping": damping, "dt": dt, "steps": steps},
        "time": sim["time"],
        "theta": [s[0] for s in sim["trajectory"]],
        "omega": [s[1] for s in sim["trajectory"]],
        "energy": energies,
        "conserved": damping == 0.0,
    }


def simulate_lorenz_attractor(
    sigma: float = 10.0,
    rho: float = 28.0,
    beta: float = 8.0 / 3.0,
    x0: float = 0.1,
    y0: float = 0.0,
    z0: float = 0.0,
    dt: float = 0.01,
    steps: int = 2000,
) -> dict[str, Any]:
    """Mô phỏng hệ hấp dẫn hỗn loạn Lorenz (Butterfly Effect).
    
    dx/dt = sigma*(y - x)
    dy/dt = x*(rho - z) - y
    dz/dt = x*y - beta*z
    """
    def deriv(_t: float, state: list[float]) -> list[float]:
        x, y, z = state[0], state[1], state[2]
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        return [dx, dy, dz]

    sim = simulate_rk4_trajectory(deriv, 0.0, [x0, y0, z0], dt, steps)
    
    points_3d = []
    for s in sim["trajectory"]:
        points_3d.append({"x": s[0], "y": s[1], "z": s[2]})
        
    return {
        "system": "lorenz_attractor",
        "parameters": {"sigma": sigma, "rho": rho, "beta": beta, "dt": dt, "steps": steps},
        "points": points_3d,
        "final_state": {"x": sim["final_state"][0], "y": sim["final_state"][1], "z": sim["final_state"][2]},
    }


def simulate_kepler_orbit(
    mu: float = 398600.4418,  # GM Trái Đất (km^3/s^2) hoặc chuẩn hóa = 1.0
    r0: tuple[float, float] = (7000.0, 0.0),  # Vị trí ban đầu (x, y) km
    v0: tuple[float, float] = (0.0, 7.546),    # Vận tốc ban đầu (vx, vy) km/s
    dt: float = 10.0,
    steps: int = 600,
) -> dict[str, Any]:
    """Mô phỏng chuyển động 2 vật Keplerian trong trường hấp dẫn Newton."""
    def deriv(_t: float, state: list[float]) -> list[float]:
        x, y, vx, vy = state
        r = math.hypot(x, y)
        if r < 1e-6:
            r = 1e-6
        ax = -mu * x / (r ** 3)
        ay = -mu * y / (r ** 3)
        return [vx, vy, ax, ay]

    sim = simulate_rk4_trajectory(deriv, 0.0, [r0[0], r0[1], v0[0], v0[1]], dt, steps)
    orbit = [{"x": s[0], "y": s[1], "vx": s[2], "vy": s[3]} for s in sim["trajectory"]]
    
    return {
        "system": "kepler_orbit",
        "parameters": {"mu": mu, "dt": dt, "steps": steps},
        "orbit": orbit,
    }
