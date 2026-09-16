from fastapi.testclient import TestClient
from server import app

client = TestClient(app)

def test_admin_login_success():
    res = client.post("/api/admin/login", json={"username": "admin@aistem.edu.vn", "password": "admin2026"})
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "ok"
    assert data["user"]["role"] == "admin"

def test_admin_login_failure():
    res = client.post("/api/admin/login", json={"username": "admin", "password": "wrong_password"})
    assert res.status_code == 401

def test_admin_overview_returns_metrics():
    res = client.get("/api/admin/overview")
    assert res.status_code == 200
    data = res.json()
    assert "total_learners" in data
    assert "total_attempts" in data
    assert "avg_accuracy" in data
    assert "difficult_problems" in data

def test_admin_list_learners():
    res = client.get("/api/admin/learners")
    assert res.status_code == 200
    data = res.json()
    assert "learners" in data
    assert len(data["learners"]) > 0

def test_admin_learner_detail():
    res = client.get("/api/admin/learners/hs_01_minhanh")
    assert res.status_code == 200
    data = res.json()
    assert data["learner"]["name"] == "Nguyễn Minh Anh"
    assert "subject_stats" in data
    assert "attempts_history" in data

def test_record_attempt():
    res = client.post("/api/practice/attempt", json={
        "learner": "hs_01_minhanh",
        "problem_id": "prob.biology.ext-khtn-thcs.0015",
        "answer": "B",
        "correct": True,
        "verdict": "correct"
    })
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_lessons_and_prerequisites():
    res = client.get("/api/lessons?page=1&page_size=5")
    assert res.status_code == 200
    data = res.json()
    assert "lessons" in data
    assert len(data["lessons"]) > 0
    lesson = data["lessons"][0]
    assert "prerequisites" in lesson
    assert "grades" in lesson

    detail_res = client.get(f"/api/lessons/{lesson['id']}")
    assert detail_res.status_code == 200
    detail = detail_res.json()
    assert "prerequisite_details" in detail
    assert "next_lessons" in detail


def test_roadmap_endpoint():
    res = client.post("/api/roadmap", json={"goal": "đạo hàm", "max_lessons": 5})
    assert res.status_code == 200
    data = res.json()
    assert data["goal"] == "đạo hàm"
    assert "milestones" in data
    assert len(data["milestones"]) > 0
    assert "sessions" in data
    assert data["total_minutes"] > 0

