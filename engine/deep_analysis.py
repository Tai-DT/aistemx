#!/usr/bin/env python3
"""Module Phân tích Sâu Hướng giải Bài toán & Chiến lược Tư duy Khoa học AISTEM."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parent.parent


def analyze_problem_solution(prob: dict, formula_repo: dict[str, dict]) -> dict:
    """Phân tích sâu hướng giải, bẫy thường gặp, chiến thuật và bài toán tương tự."""
    subject = prob.get("subject", "math")
    topic = prob.get("topic", "")
    difficulty = prob.get("difficulty", 2)
    formulas_used = prob.get("formulas_used", [])

    # Tra cứu chi tiết công thức liên kết
    f_info = []
    for fid in formulas_used:
        if fid in formula_repo:
            f = formula_repo[fid]
            f_info.append({
                "id": fid,
                "name": f.get("name_vi", ""),
                "latex": f.get("latex", ""),
                "conditions": f.get("conditions", "")
            })

    # Phân tích theo từng môn học
    if subject == "math":
        core_principle = "Quy đổi bài toán về dạng phương trình chuẩn tắc, khai thác đại lượng bất biến hoặc tính đối xứng của biểu thức."
        pitfalls = [
            "Bỏ quên điều kiện xác định của biến (nguyên dương, khác 0, mẫu số khác 0).",
            "Nhầm lẫn giữa chỉnh hợp (có phân biệt thứ tự) và tổ hợp (không phân biệt thứ tự).",
            "Sai sót khi khai căn bậc hai: quên xét nghiệm âm hoặc không loại nghiệm ngoại lai."
        ]
        tactics = "Phương pháp Đặt ẩn phụ / Quy nạp toán học / Đánh giá bất đẳng thức biên."
    elif subject == "physics":
        core_principle = "Áp dụng định luật bảo toàn (cơ năng, động lượng, điện tích) và phân tích lực theo các trục tọa độ trực giao."
        pitfalls = [
            "Không đổi đơn vị về hệ chuẩn SI (gam -> kg, cm -> m, phút -> giây).",
            "Nhầm lẫn dấu của công lực cản / gia tốc hãm phanh (dấu âm trong hệ trục).",
            "Bỏ qua lực ma sát nghỉ cực đại hoặc nhầm lẫn giữa điện trở trong và ngoài."
        ]
        tactics = "Phương pháp Tọa độ - Vectơ / Bảo toàn năng lượng / Khảo sát dao động điều hòa."
    elif subject == "chemistry":
        core_principle = "Bảo toàn nguyên tố, bảo toàn electron trong phản ứng oxi hóa - khử và cân bằng nhiệt động học Gibbs."
        pitfalls = [
            "Quên đổi đơn vị entropy ΔS từ J/(mol·K) sang kJ/(mol·K) khi nhân với nhiệt độ T.",
            "Nhầm lẫn giữa pH và nồng độ ion H+ (thang logarit cơ số 10).",
            "Tính sai tỉ lệ mol khi có chất phản ứng dư hoặc chất xúc tác."
        ]
        tactics = "Phương pháp Đường chéo nồng độ / Phương trình Gibbs - Helmholtz / Bảo toàn điện tích ion."
    else:  # biology
        core_principle = "Quy luật di truyền Mendel, cân bằng di truyền quần thể Hardy - Weinberg và cơ chế phân tử DNA."
        pitfalls = [
            "Nhầm lẫn giữa tần số alen (p, q) và tỉ lệ kiểu gen (p², 2pq, q²).",
            "Quên chia 2 tổng số nucleotide khi tính chiều dài mạch kép DNA.",
            "Không phân biệt giữa bệnh do gen lặn trên NST thường và gen lặn trên NST giới tính X."
        ]
        tactics = "Khung lưới Punnett / Sơ đồ phả hệ di truyền / Công thức cấu trúc DNA B-form."

    cognitive_steps = [
        {"phase": "1. Nhận diện & Chuẩn hóa", "desc": "Trích xuất các giả thiết đề bài, xác định đơn vị đo và đại lượng cần tìm."},
        {"phase": "2. Chọn Mô hình & Công thức", "desc": f"Áp dụng các định luật: {', '.join(f['name'] for f in f_info) or 'Mô hình chuẩn'}"},
        {"phase": "3. Thiết lập Phương trình", "desc": "Chuyển ngôn ngữ đề bài thành hệ thức toán học chính xác."},
        {"phase": "4. Giải & Kiểm định Biên", "desc": "Tính toán ra đáp số số học, đối chiếu với điều kiện thực tế và dung sai sai số."}
    ]

    return {
        "problem_id": prob.get("id"),
        "subject": subject,
        "topic": topic,
        "difficulty_rating": f"Cấp độ {difficulty}/5",
        "core_scientific_principle": core_principle,
        "optimal_tactics": tactics,
        "cognitive_blueprint": cognitive_steps,
        "common_pitfalls": pitfalls,
        "linked_formulas": f_info,
        "skills_required": prob.get("skills", []),
        "similar_tags": prob.get("tags", [])
    }
