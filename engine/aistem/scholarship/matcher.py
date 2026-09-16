"""Mô-đun khớp nối và đề xuất học bổng (Scholarship Matching Engine).

Phân loại học bổng theo 3 nhóm chiến lược:
- Reach (Vươn tầm / Cực kỳ cạnh tranh)
- Target (Mục tiêu cốt lõi / Vừa tầm)
- Safety (An toàn / Khả thi cao)
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    from aistem.scholarship.readiness import assess_profile_readiness
except ImportError:
    try:
        from engine.aistem.scholarship.readiness import assess_profile_readiness
    except ImportError:
        import sys
        ROOT = Path(__file__).resolve().parents[3]
        if str(ROOT) not in sys.path:
            sys.path.insert(0, str(ROOT))
        from engine.aistem.scholarship.readiness import assess_profile_readiness


DEFAULT_DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "scholarships" / "scholarships.json"


def load_scholarships(file_path: Optional[Path | str] = None) -> List[Dict[str, Any]]:
    """Tải danh sách học bổng từ cơ sở dữ liệu JSON."""
    path = Path(file_path) if file_path else DEFAULT_DATA_PATH
    if not path.exists():
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("scholarships", [])
    except Exception:
        return []


def calculate_match(profile: Dict[str, Any], scholarship: Dict[str, Any], readiness: Dict[str, Any]) -> Dict[str, Any]:
    """Tính toán điểm phù hợp (Match Score % từ 0 đến 100) giữa ứng viên và học bổng."""
    fit_reasons: List[str] = []
    warnings: List[str] = []

    # -------------------------------------------------------------
    # 1. Điểm học thuật (40%)
    # -------------------------------------------------------------
    academic_pts = 0.0

    # GPA so sánh (15 điểm)
    gpa = float(profile.get("gpa", 0.0) or 0.0)
    gpa_norm = gpa / 4.0 * 10.0 if gpa <= 4.0 and gpa > 0 else gpa
    sch_gpa = float(scholarship.get("gpa_min", 8.0))

    if gpa_norm >= sch_gpa:
        academic_pts += 15.0
        fit_reasons.append(f"GPA ({gpa:.2f}) đạt/vượt yêu cầu tối thiểu ({sch_gpa}).")
    elif gpa_norm >= sch_gpa - 0.4:
        academic_pts += 10.0
        warnings.append(f"GPA ({gpa:.2f}) tiệm cận mức yêu cầu ({sch_gpa}), cần thư giải trình hoặc các điểm mạnh khác bù đắp.")
    elif gpa_norm > 0:
        academic_pts += 5.0
        warnings.append(f"GPA ({gpa:.2f}) thấp hơn điều kiện tham chiếu ({sch_gpa}).")
    else:
        warnings.append("Chưa có thông tin GPA.")

    # SAT so sánh (15 điểm)
    sat = int(profile.get("sat", 0) or 0)
    sch_sat = int(scholarship.get("sat_min", 0) or 0)

    if sch_sat == 0:
        # Trường không bắt buộc SAT (châu Âu, Nhật, Úc, v.v.)
        academic_pts += 15.0
        fit_reasons.append("Học bổng không yêu cầu điểm SAT/ACT.")
    else:
        if sat >= sch_sat:
            academic_pts += 15.0
            fit_reasons.append(f"Điểm SAT ({sat}) thỏa mãn chuẩn tuyển chọn ({sch_sat}+).")
        elif sat >= sch_sat - 60:
            academic_pts += 10.0
            warnings.append(f"Điểm SAT ({sat}) hơi thấp hơn điểm khuyến nghị ({sch_sat}).")
        elif sat > 0:
            academic_pts += 4.0
            warnings.append(f"Điểm SAT ({sat}) cách biệt đáng kể so với ngưỡng ({sch_sat}).")
        else:
            warnings.append(f"Yêu cầu SAT tối thiểu {sch_sat}, ứng viên chưa có điểm SAT.")

    # IELTS so sánh (10 điểm)
    ielts = float(profile.get("ielts", 0.0) or 0.0)
    sch_ielts = float(scholarship.get("ielts_min", 6.5))

    if ielts >= sch_ielts:
        academic_pts += 10.0
        fit_reasons.append(f"Điểm IELTS ({ielts}) vượt chuẩn đầu vào ({sch_ielts}).")
    elif ielts >= sch_ielts - 0.5:
        academic_pts += 6.5
        warnings.append(f"IELTS ({ielts}) tiệm cận ngưỡng {sch_ielts}, nên nâng điểm để tăng tính cạnh tranh.")
    elif ielts > 0:
        academic_pts += 3.0
        warnings.append(f"IELTS ({ielts}) chưa đạt ngưỡng yêu cầu ({sch_ielts}).")
    else:
        warnings.append(f"Chưa có điểm tiếng Anh (yêu cầu IELTS >= {sch_ielts}).")

    academic_pts = min(academic_pts, 40.0)

    # -------------------------------------------------------------
    # 2. Ngành học định hướng (20%)
    # -------------------------------------------------------------
    major_pts = 0.0
    intended_major = str(profile.get("intended_major", "")).lower().strip()
    target_majors = [m.lower() for m in scholarship.get("target_majors", [])]

    if not intended_major or intended_major in ["tat-ca", "all", "general"]:
        major_pts = 20.0
        fit_reasons.append("Ngành học mục tiêu tương thích hoàn toàn.")
    elif "tat-ca" in target_majors or "stem" in target_majors:
        major_pts = 20.0
        fit_reasons.append(f"Ngành '{intended_major}' thuộc nhóm STEM trọng điểm của học bổng.")
    elif any(intended_major in m or m in intended_major for m in target_majors):
        major_pts = 20.0
        fit_reasons.append(f"Ngành học định hướng '{intended_major}' trùng khớp chính xác.")
    else:
        # Khác biệt ngành
        major_pts = 8.0
        warnings.append(f"Ngành '{intended_major}' không nằm trong nhóm ưu tiên hàng đầu của quỹ.")

    # -------------------------------------------------------------
    # 3. Năng lực Hồ sơ & Độ cạnh tranh (30%)
    # -------------------------------------------------------------
    overall_readiness = readiness.get("overall_score", 0.0)
    readiness_pts = 0.0

    tags = scholarship.get("tags", [])
    coverage = scholarship.get("coverage", "")
    is_elite = any(t in ["ivy-league", "oxbridge", "need-blind"] for t in tags) or coverage == "full-ride"

    if is_elite:
        # Yêu cầu hồ sơ rất cao
        if overall_readiness >= 80.0:
            readiness_pts = 30.0
            fit_reasons.append("Hồ sơ đạt đẳng cấp tinh hoa (Elite Tier), đủ sức cạnh tranh vòng xét chọn học bổng toàn phần.")
        elif overall_readiness >= 65.0:
            readiness_pts = 20.0
            warnings.append("Học bổng cực kỳ khốc liệt, hồ sơ ở mức khá mạnh nhưng cần bài luận và Spike đột phá.")
        else:
            readiness_pts = 10.0
            warnings.append("Học bổng có độ cạnh tranh toàn cầu cao hơn mức độ sẵn sàng hiện tại của hồ sơ.")
    else:
        # Học bổng vừa tầm hơn (merit-based, chính phủ, hỗ trợ học phí)
        if overall_readiness >= 65.0:
            readiness_pts = 30.0
            fit_reasons.append("Hồ sơ năng lực vượt trội so với mặt bằng ứng viên thông thường.")
        elif overall_readiness >= 50.0:
            readiness_pts = 24.0
            fit_reasons.append("Hồ sơ cơ bản đáp ứng các tiêu chuẩn cốt lõi.")
        else:
            readiness_pts = 14.0

    # -------------------------------------------------------------
    # 4. Quốc gia & Sở thích (10%)
    # -------------------------------------------------------------
    pref_pts = 0.0
    preferred_countries = [c.lower() for c in profile.get("preferred_countries", [])]
    sch_country = scholarship.get("country", "").lower()

    if not preferred_countries or any(sch_country in c or c in sch_country for c in preferred_countries):
        pref_pts = 10.0
        if preferred_countries:
            fit_reasons.append(f"Quốc gia ({scholarship.get('country')}) nằm trong danh sách ưu tiên.")
    else:
        pref_pts = 4.0

    total_match = round(academic_pts + major_pts + readiness_pts + pref_pts, 1)
    total_match = min(max(total_match, 10.0), 99.0)

    # -------------------------------------------------------------
    # Phân loại chiến lược (Strategy Category)
    # -------------------------------------------------------------
    # Các trường Ivy / MIT / Cambridge / Oxford / Need-Blind luôn xếp Reach trừ khi match cực cao
    is_super_selective = any(t in ["ivy-league", "oxbridge", "need-blind"] for t in tags)

    if is_super_selective:
        category = "reach"
        category_label = "Reach (Vươn tầm / Cạnh tranh cao cấp)"
    elif total_match >= 85.0:
        if coverage == "full-ride" and overall_readiness < 80.0:
            category = "target"
            category_label = "Target (Mục tiêu cốt lõi)"
        else:
            category = "safety"
            category_label = "Safety (Khả thi cao / An toàn)"
    elif total_match >= 70.0:
        category = "target"
        category_label = "Target (Mục tiêu cốt lõi)"
    else:
        category = "reach"
        category_label = "Reach (Vươn tầm / Cần nỗ lực lớn)"

    return {
        "scholarship_id": scholarship.get("id"),
        "scholarship_name": scholarship.get("name"),
        "country": scholarship.get("country"),
        "provider": scholarship.get("provider"),
        "coverage": scholarship.get("coverage"),
        "financial_value_usd": scholarship.get("financial_value_usd"),
        "match_score": total_match,
        "category": category,
        "category_label": category_label,
        "fit_reasons": fit_reasons,
        "warnings": warnings,
        "official_url": scholarship.get("official_url"),
        "deadlines": scholarship.get("deadlines", {})
    }


def match_scholarships(profile: Dict[str, Any], scholarships: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
    """Phân tích hồ sơ và trả về các nhóm học bổng Reach, Target, Safety cùng chỉ số phù hợp."""
    scholarships_list = scholarships if scholarships is not None else load_scholarships()
    readiness = assess_profile_readiness(profile)

    matched_items: List[Dict[str, Any]] = []
    for sch in scholarships_list:
        match_result = calculate_match(profile, sch, readiness)
        matched_items.append(match_result)

    # Sắp xếp theo match score giảm dần
    matched_items.sort(key=lambda x: x["match_score"], reverse=True)

    reach_list = [m for m in matched_items if m["category"] == "reach"]
    target_list = [m for m in matched_items if m["category"] == "target"]
    safety_list = [m for m in matched_items if m["category"] == "safety"]

    return {
        "profile_summary": {
            "overall_score": readiness["overall_score"],
            "tier": readiness["tier"],
            "readiness_label": readiness["readiness_label"]
        },
        "statistics": {
            "total_evaluated": len(matched_items),
            "reach_count": len(reach_list),
            "target_count": len(target_list),
            "safety_count": len(safety_list)
        },
        "categorized": {
            "reach": reach_list,
            "target": target_list,
            "safety": safety_list
        },
        "all_matches": matched_items
    }
