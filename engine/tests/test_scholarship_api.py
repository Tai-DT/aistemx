"""Kiểm thử tích hợp cho REST APIs của Hệ thống Học bổng (/api/scholarships/*)."""
from __future__ import annotations

import pytest
from starlette.testclient import TestClient

from server import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_list_scholarships_endpoint(client: TestClient) -> None:
    res = client.get("/api/scholarships")
    assert res.status_code == 200
    data = res.json()
    assert data["total"] >= 20
    assert len(data["scholarships"]) >= 20


def test_list_scholarships_with_filters(client: TestClient) -> None:
    # Lọc theo quốc gia
    res = client.get("/api/scholarships", params={"country": "Hoa Kỳ"})
    assert res.status_code == 200
    usa_items = res.json()["scholarships"]
    assert len(usa_items) >= 4
    assert all("Hoa Kỳ" in s["country"] for s in usa_items)

    # Lọc theo coverage
    res = client.get("/api/scholarships", params={"coverage": "full-ride"})
    assert res.status_code == 200
    assert all(s["coverage"] == "full-ride" for s in res.json()["scholarships"])


def test_get_scholarship_detail(client: TestClient) -> None:
    res = client.get("/api/scholarships/sch.harvard-financial-aid")
    assert res.status_code == 200
    data = res.json()
    assert data["id"] == "sch.harvard-financial-aid"
    assert "Harvard" in data["name"]

    # 404 cho id không tồn tại
    res404 = client.get("/api/scholarships/sch.khong-ton-tai")
    assert res404.status_code == 404


def test_assess_profile_endpoint(client: TestClient) -> None:
    profile = {
        "gpa": 9.6,
        "sat": 1540,
        "ielts": 8.0,
        "ap_count": 4,
        "competitions": [
            {"name": "AMC 12", "level": "quoc te", "prize": "Distinction"}
        ],
        "spike_domain": "Khoa học Máy tính & Mật mã học",
        "essay_status": "polished",
        "has_stem_teacher_lor": True,
    }
    res = client.post("/api/scholarships/assess", json={"profile": profile})
    assert res.status_code == 200
    data = res.json()
    assert "overall_score" in data
    assert "pillars" in data
    assert data["overall_score"] >= 65.0


def test_match_profile_endpoint(client: TestClient) -> None:
    profile = {
        "gpa": 9.4,
        "sat": 1500,
        "ielts": 7.5,
        "intended_major": "khoa-hoc-may-tinh",
    }
    res = client.post("/api/scholarships/match", json={"profile": profile})
    assert res.status_code == 200
    data = res.json()
    assert "statistics" in data
    assert "categorized" in data
    assert "reach" in data["categorized"]
    assert "target" in data["categorized"]
    assert "safety" in data["categorized"]


def test_interview_questions_and_evaluate(client: TestClient) -> None:
    # 1. Lấy danh sách câu hỏi
    res = client.get("/api/scholarships/interview/questions")
    assert res.status_code == 200
    data = res.json()
    assert data["total"] >= 6
    assert len(data["questions"]) >= 6

    # 2. Đánh giá câu trả lời
    eval_res = client.post("/api/scholarships/interview/evaluate", json={
        "question_id": "q_motivation_fit",
        "answer": (
            "Khi tìm hiểu về trường, tôi đặc biệt ấn tượng với phòng lab Robotics của Giáo sư Smith. "
            "Thách thức trong dự án chế tạo xe tự hành trước đây của tôi là thuật toán SLAM bị trôi tín hiệu khi gặp vật cản gương. "
            "Tôi đã chủ động đọc các bài báo mới nhất của GS Smith trên IEEE về sensor fusion và tự viết lại thuật toán lọc Kalman mở rộng. "
            "Kết quả là sai số định vị giảm 65% trên mô hình thực nghiệm và xe đã hoàn thành trọn vẹn sa hình thi đấu. "
            "Tôi tin rằng môi trường nghiên cứu tại trường sẽ giúp tôi phát triển sâu hơn về tự hành thông minh."
        )
    })
    assert eval_res.status_code == 200
    eval_data = eval_res.json()
    assert eval_data["total_star_score"] >= 75.0
    assert "star_components" in eval_data
