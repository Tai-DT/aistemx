"""Gói xử lý nghiệp vụ Học bổng AISTEM (Scholarship Engine).

Bao gồm:
- readiness: Đánh giá hồ sơ theo 4 trụ cột, xếp hạng Tier & phân tích khoảng cách Gap Analysis
- matcher: Thuật toán đề xuất & phân bổ danh mục Reach / Target / Safety
- interview_simulator: Ngân hàng câu hỏi chuẩn hóa & Đánh giá phản xạ phương pháp STAR
"""
from __future__ import annotations

from .readiness import assess_profile_readiness
from .matcher import load_scholarships, calculate_match, match_scholarships
from .interview_simulator import (
    INTERVIEW_QUESTIONS,
    get_all_questions,
    get_question_by_id,
    evaluate_star_response,
)

__all__ = [
    "assess_profile_readiness",
    "load_scholarships",
    "calculate_match",
    "match_scholarships",
    "INTERVIEW_QUESTIONS",
    "get_all_questions",
    "get_question_by_id",
    "evaluate_star_response",
]
