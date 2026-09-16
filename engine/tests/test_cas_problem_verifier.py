"""Kiểm thử pipeline kiểm định khoa học CAS cho bài toán (SymPy / Numerical / Symbolic)."""
from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from aistem.cas.problem_verifier import verify_problem_data
from aistem.store.postgres import get_postgres_connection
from server import app


def test_verify_problem_data_dien_so():
    # Bài toán điền số chuẩn
    problem = {
        "id": "test.prob.001",
        "type": "dien-so",
        "answer": "21,6 N",
        "answer_numeric": 21.6,
        "answer_unit": "N",
        "tolerance": 0.05,
        "solution_steps": [
            {
                "explain": "Định luật Coulomb",
                "latex": "F = 9\\cdot10^{9}\\cdot\\dfrac{4\\cdot10^{-6}\\cdot 6\\cdot10^{-6}}{0{,}1^{2}} = 21{,}6\\ \\text{N}"
            }
        ]
    }

    is_verified, status, details = verify_problem_data(problem)
    assert is_verified is True
    assert status == "verified"
    assert details["cas_value"] == 21.6
    assert details["trustworthy"] is True


def test_verify_problem_data_trac_nghiem():
    # Bài toán trắc nghiệm chọn A, B, C, D
    problem = {
        "id": "test.prob.002",
        "type": "trac-nghiem",
        "answer": "A",
        "choices": [
            {"key": "A", "text": "$2\\cdot10^{4}$ V/m"},
            {"key": "B", "text": "$3\\cdot10^{3}$ V/m", "why_wrong": "Quên bình phương"},
            {"key": "C", "text": "$5\\cdot10^{3}$ V/m", "why_wrong": "Nhầm khoảng cách"},
            {"key": "D", "text": "$4{,}5\\cdot10^{4}$ V/m", "why_wrong": "Sai số liệu"}
        ],
        "solution_steps": [
            {
                "explain": "Cường độ điện trường",
                "latex": "E = 9\\cdot10^9 \\cdot \\dfrac{5\\cdot10^{-8}}{0{,}15^2} = 20000\\ \\text{V/m}"
            }
        ]
    }

    is_verified, status, details = verify_problem_data(problem)
    assert is_verified is True
    assert status == "verified"
    assert details["cas_value"] == 20000.0


def test_verify_problem_data_refuted_wrong_answer():
    # Bài toán cố ý sai đáp số để kiểm tra khả năng phát hiện lỗi
    problem = {
        "id": "test.prob.wrong",
        "type": "dien-so",
        "answer": "999 N",
        "answer_numeric": 999.0,
        "solution_steps": [
            {
                "explain": "Tính lực",
                "latex": "F = 2\\cdot 10 = 20"
            }
        ]
    }

    is_verified, status, details = verify_problem_data(problem)
    assert is_verified is False
    assert status == "refuted" or details.get("answer_mismatch") is True


def test_api_verify_cas_endpoint():
    client = TestClient(app)
    resp = client.post("/api/problems/prob.physics.vn-thpt-physics-diendtu.0001/verify-cas")
    assert resp.status_code == 200
    data = resp.json()
    assert data["id"] == "prob.physics.vn-thpt-physics-diendtu.0001"
    assert data["cas_verified"] is True
    assert data["cas_status"] == "verified"
    assert data["cas_details"]["cas_value"] == 21.6
