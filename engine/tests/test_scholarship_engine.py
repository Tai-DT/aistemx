"""Bộ kiểm thử đơn vị toàn diện cho Hệ thống Học bổng AISTEM (Scholarship Engine)."""
from __future__ import annotations

import pytest
from pathlib import Path

from aistem.scholarship import (
    assess_profile_readiness,
    load_scholarships,
    calculate_match,
    match_scholarships,
    get_all_questions,
    get_question_by_id,
    evaluate_star_response,
)


class TestReadinessAssessment:
    """Kiểm tra mô-đun đánh giá năng lực hồ sơ (4 trụ cột & Gap Analysis)."""

    def test_elite_profile_reaches_elite_tier(self) -> None:
        profile = {
            "gpa": 9.8,
            "sat": 1560,
            "ielts": 8.5,
            "ap_count": 5,
            "competitions": [
                {"name": "IMO 2025", "level": "quoc te", "prize": "Huy chương Bạc"},
                {"name": "ViISEF Quốc gia", "level": "quoc gia", "prize": "Giải Nhất"}
            ],
            "research_papers": [
                {"title": "Deep Learning for Solar Flare Forecasting", "venue": "IEEE Student"}
            ],
            "spike_domain": "Trí tuệ nhân tạo và Vật lý Thiên văn",
            "activities": [
                {"role": "Founder & Captain", "description": "Câu lạc bộ Thiên văn mở rộng", "impact": "5,000 học sinh và 10,000 USD quỹ tài trợ"}
            ],
            "essay_status": "polished",
            "has_counselor_lor": True,
            "has_stem_teacher_lor": True,
            "has_research_mentor_lor": True,
        }

        result = assess_profile_readiness(profile)
        assert result["overall_score"] >= 85.0
        assert "Elite Tier" in result["tier"]
        assert len(result["strengths"]) >= 4
        assert result["pillars"]["academic"]["score"] >= 23.0
        assert result["pillars"]["stem_awards"]["score"] >= 20.0
        assert result["pillars"]["spike_profile"]["score"] >= 20.0
        assert result["pillars"]["essays_lors"]["score"] >= 20.0

    def test_developing_profile_produces_actionable_gaps(self) -> None:
        profile = {
            "gpa": 7.8,
            "sat": 0,
            "ielts": 6.0,
            "ap_count": 0,
            "competitions": [],
            "research_papers": [],
            "spike_domain": "",
            "activities": [
                {"role": "Member", "description": "Tham gia CLB Tình nguyện", "impact": "Tham gia tích cực"}
            ],
            "essay_status": "not_started",
            "has_counselor_lor": False,
            "has_stem_teacher_lor": False,
            "has_research_mentor_lor": False,
        }

        result = assess_profile_readiness(profile)
        assert result["overall_score"] < 50.0
        assert "Developing Tier" in result["tier"]
        # Phải có các khuyến nghị cụ thể
        gaps = result["gap_analysis"]
        assert len(gaps) >= 4
        pillars_in_gaps = {g["pillar"] for g in gaps}
        assert "Academic" in pillars_in_gaps
        assert "STEM Competitions & Research" in pillars_in_gaps
        assert "Spike Profile & Extracurriculars" in pillars_in_gaps
        assert "Essays & LORs" in pillars_in_gaps

    def test_handles_empty_or_edge_case_inputs(self) -> None:
        result = assess_profile_readiness({})
        assert 0.0 <= result["overall_score"] <= 100.0
        assert result["max_score"] == 100.0
        assert isinstance(result["gap_analysis"], list)


class TestScholarshipMatcher:
    """Kiểm tra mô-đun khớp nối học bổng và phân loại Reach/Target/Safety."""

    def test_loads_scholarships_data(self) -> None:
        scholarships = load_scholarships()
        assert len(scholarships) >= 20
        # Đảm bảo mỗi học bổng có đủ các trường trọng yếu
        for s in scholarships:
            assert s["id"].startswith("sch.")
            assert s["name"]
            assert s["country"]
            assert s["coverage"] in ["full-ride", "full-tuition", "partial", "living-stipend"]

    def test_matcher_categorizes_into_reach_target_safety(self) -> None:
        profile = {
            "gpa": 9.2,
            "sat": 1490,
            "ielts": 7.5,
            "ap_count": 3,
            "intended_major": "khoa-hoc-may-tinh",
            "preferred_countries": ["Hoa Kỳ", "Singapore", "Việt Nam"],
            "competitions": [
                {"name": "AMC 12", "level": "quoc te", "prize": "AIME Qualifier"}
            ],
            "spike_domain": "Khoa học Dữ liệu",
            "activities": [
                {"role": "Leader", "description": "Dự án phân tích dữ liệu rác thải", "impact": "1,200 người dùng website"}
            ],
            "essay_status": "in_progress",
            "has_stem_teacher_lor": True,
        }

        matched = match_scholarships(profile)
        stats = matched["statistics"]
        assert stats["total_evaluated"] >= 20
        assert stats["reach_count"] > 0
        assert stats["target_count"] > 0
        # Tất cả các kết quả đều có match_score hợp lệ
        for item in matched["all_matches"]:
            assert 10.0 <= item["match_score"] <= 99.0
            assert item["category"] in ["reach", "target", "safety"]
            assert isinstance(item["fit_reasons"], list)

    def test_single_match_calculation(self) -> None:
        scholarship = {
            "id": "sch.test-uni",
            "name": "Test University STEM Merit Award",
            "country": "Hoa Kỳ",
            "provider": "Test University",
            "coverage": "full-tuition",
            "gpa_min": 9.0,
            "sat_min": 1450,
            "ielts_min": 7.0,
            "target_majors": ["stem", "khoa-hoc-may-tinh"],
            "tags": ["merit-based", "usa"],
        }
        profile = {
            "gpa": 9.3,
            "sat": 1480,
            "ielts": 7.5,
            "intended_major": "khoa-hoc-may-tinh",
            "preferred_countries": ["Hoa Kỳ"],
        }
        readiness = assess_profile_readiness(profile)
        res = calculate_match(profile, scholarship, readiness)
        assert res["match_score"] >= 75.0
        assert res["category"] in ["target", "safety"]
        assert any("GPA" in r for r in res["fit_reasons"])


class TestInterviewSimulator:
    """Kiểm tra mô phỏng phỏng vấn & chấm điểm phản xạ STAR."""

    def test_question_bank_retrieval(self) -> None:
        questions = get_all_questions()
        assert len(questions) >= 6
        for q in questions:
            assert q["id"].startswith("q_")
            assert q["category"]
            assert q["question_vi"]
            assert len(q["key_objectives"]) >= 2
            assert "sample_star_outline" in q

        q_first = get_question_by_id(questions[0]["id"])
        assert q_first is not None
        assert q_first["id"] == questions[0]["id"]

    def test_star_evaluation_with_short_answer(self) -> None:
        res = evaluate_star_response("q_research_deep", "Tôi thích làm AI vì nó hay.")
        assert res["word_count"] < 20
        assert res["total_star_score"] < 60.0
        assert any("quá ngắn" in fb.lower() for fb in res["feedback"])

    def test_star_evaluation_with_rich_response(self) -> None:
        rich_answer = (
            "Khi tham gia kỳ thi KHKT ViISEF năm lớp 11, tôi nhận thấy nhiều người cao tuổi "
            "tại quê hương gặp khó khăn khi phát hiện sớm bệnh thoái hóa điểm vàng võng mạc. "
            "Nhiệm vụ và thách thức lớn nhất của tôi là phải xây dựng một mô hình thị giác máy tính "
            "có thể phân tích ảnh đáy mắt với độ chính xác cao nhưng dung lượng siêu nhẹ dưới 25MB để chạy được trên điện thoại bình dân. "
            "Tôi đã trực tiếp lập trình mạng nơ-ron tích chập sử dụng framework PyTorch, áp dụng kỹ thuật pruning và quantization "
            "để tinh gọn trọng số, đồng thời thử nghiệm tối ưu siêu tham số qua 50 epochs trên tập dữ liệu mở. "
            "Kết quả đạt được là mô hình có độ chính xác 94.8%, giảm thời gian suy luận xuống chỉ còn 0.4 giây mỗi bức ảnh. "
            "Dự án đã được ứng dụng thử nghiệm cho hơn 300 bệnh nhân tại trạm y tế địa phương và đạt giải Nhì KHKT cấp quốc gia. "
            "Bài học lớn nhất mà tôi chiêm nghiệm được là công nghệ STEM chỉ thực sự có hồn khi nó giải quyết được nỗi đau thực tế của con người."
        )
        res = evaluate_star_response("q_research_deep", rich_answer)
        assert res["word_count"] >= 100
        assert res["total_star_score"] >= 80.0
        assert res["star_components"]["situation"]["score"] >= 20.0
        assert res["star_components"]["task"]["score"] >= 20.0
        assert res["star_components"]["action"]["score"] >= 20.0
        assert res["star_components"]["result"]["score"] >= 20.0
        assert "Elite" in res["star_rating"]
