"""Integration tests cho các REST API toán học trong server.py."""
import pytest
from fastapi.testclient import TestClient

try:
    from server import app
except ImportError:
    from engine.server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_api_fourier(client):
    res = client.post("/api/math/simulate/fourier", json={"wave_type": "square", "harmonics": 5, "points": 50})
    assert res.status_code == 200
    data = res.json()
    assert "signal" in data
    assert len(data["spectrum"]) == 5


def test_api_pendulum(client):
    res = client.post("/api/math/simulate/rk4-pendulum", json={"theta0": 0.5, "steps": 50})
    assert res.status_code == 200
    data = res.json()
    assert len(data["theta"]) == 51
    assert "energy" in data


def test_api_matrix_2x2(client):
    res = client.post("/api/math/simulate/matrix-2x2", json={"a": 1.0, "b": 2.0, "c": 3.0, "d": 4.0})
    assert res.status_code == 200
    data = res.json()
    assert data["determinant"] == -2.0
    assert "svd" in data


def test_api_galton(client):
    res = client.post("/api/math/simulate/galton", json={"num_balls": 100, "rows": 8})
    assert res.status_code == 200
    data = res.json()
    assert len(data["bins"]) == 9
    assert sum(data["bins"]) == 100


def test_api_cas_solve(client):
    res = client.post("/api/math/cas/solve-equation", json={"equation": "2*x + 10 = 20", "variable": "x"})
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "5" in data["solutions"]


def test_api_cas_calculus(client):
    res = client.post("/api/math/cas/calculus", json={"operation": "diff", "expression": "cos(x)", "variable": "x"})
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert "-sin(x)" in data["result_str"]
