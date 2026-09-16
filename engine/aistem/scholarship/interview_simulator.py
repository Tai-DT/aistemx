"""Mô phỏng phỏng vấn học bổng STEM & Chấm điểm phản xạ theo phương pháp STAR.

STAR Framework:
- Situation (Bối cảnh thực tế)
- Task (Thách thức & Nhiệm vụ cá nhân)
- Action (Hành động cụ thể, kỹ thuật đã áp dụng, tư duy độc lập)
- Result (Kết quả định lượng & Bài học chiêm nghiệm)
"""
from __future__ import annotations

import re
from typing import Any, Dict, List, Optional


INTERVIEW_QUESTIONS: List[Dict[str, Any]] = [
    {
        "id": "q_motivation_fit",
        "category": "motivation",
        "category_vi": "Động lực & Độ tương thích văn hóa",
        "question_vi": "Tại sao bạn quyết định theo đuổi ngành STEM tại trường/quỹ học bổng này thay vì những lựa chọn uy tín khác?",
        "question_en": "Why do you want to pursue your STEM degree at our university/scholarship foundation rather than other prestigious options?",
        "key_objectives": [
            "Kiểm tra mức độ tìm hiểu sâu sắc về giáo sư, phòng lab, văn hóa maker của trường",
            "Tránh câu trả lời sáo rỗng về ranking hay danh tiếng chung chung",
            "Thể hiện sự khớp nối giữa định hướng nghiên cứu cá nhân với thế mạnh nhà trường"
        ],
        "sample_star_outline": {
            "situation": "Đang nghiên cứu về thị giác máy tính và nhận thấy rào cản về tính toán biên.",
            "task": "Cần môi trường học thuật có lab chuyên sâu về TinyML và AI hardware.",
            "action": "Tìm hiểu các công trình của GS [Tên] tại trường, đối chiếu với dự án đã làm.",
            "result": "Lộ trình rõ ràng sẵn sàng tham gia nghiên cứu ngay từ năm nhất."
        },
        "red_flags": [
            "Chỉ khen trường nổi tiếng, ranking cao",
            "Không nêu được tên một giáo sư, dự án hay lab cụ thể nào của trường",
            "Sao chép câu trả lời áp dụng cho bất kỳ trường nào cũng được"
        ]
    },
    {
        "id": "q_research_deep",
        "category": "spike_research",
        "category_vi": "Chiều sâu nghiên cứu & Diễn giải khoa học",
        "question_vi": "Hãy giải thích đề tài nghiên cứu hoặc dự án kỹ thuật tâm đắc nhất của bạn cho một người không có chuyên môn hiểu được trong 2 phút.",
        "question_en": "Explain your proudest STEM research project to someone without a technical background in under 2 minutes.",
        "key_objectives": [
            "Đánh giá khả năng chuyển đổi khái niệm toán/kỹ thuật phức tạp thành ngôn ngữ trực quan",
            "Làm rõ vai trò then chốt của bản thân (không nói chung chung về team)",
            "Làm nổi bật giá trị thực tiễn đối với con người hoặc khoa học"
        ],
        "sample_star_outline": {
            "situation": "Bệnh nhân vùng sâu vùng xa khó tiếp cận chẩn đoán hình ảnh sớm.",
            "task": "Xây dựng thuật toán nén mô hình phân loại ảnh X-quang chạy trực tiếp trên smartphone.",
            "action": "Áp dụng kỹ thuật pruning và quantization để giảm kích thước model 70% mà độ chính xác giảm chưa tới 1.5%.",
            "result": "Thử nghiệm trên 500 ảnh bệnh án, tốc độ phản hồi 0.3s/ảnh không cần internet."
        },
        "red_flags": [
            "Lạm dụng thuật ngữ đao to búa lớn mà không có ẩn dụ dễ hiểu",
            "Chỉ nói về kết quả của cả nhóm mà không thấy đóng góp kỹ thuật cá nhân",
            "Không giải thích được tại sao bài toán đó quan trọng"
        ]
    },
    {
        "id": "q_failure_resilience",
        "category": "overcoming_failure",
        "category_vi": "Bản lĩnh vượt khó & Thất bại trong khoa học",
        "question_vi": "Kể về một lần thử nghiệm, thuật toán hoặc dự án STEM của bạn thất bại hoàn toàn. Bạn đã đối diện và hành động như thế nào?",
        "question_en": "Tell me about a time when your STEM experiment or engineering project failed completely. How did you handle the setback?",
        "key_objectives": [
            "Kiểm tra tính trung thực khoa học (Scientific Integrity)",
            "Khả năng phân tích nguyên nhân gốc rễ (Root-Cause Analysis) thay vì đổ lỗi hoàn cảnh",
            "Sức bền tâm lý (Grit) khi đối diện với bế tắc nghiên cứu"
        ],
        "sample_star_outline": {
            "situation": "Sau 3 tháng huấn luyện mô hình dự báo hạn mặn, mô hình overfitting nặng khi test thực tế.",
            "task": "Chỉ còn 3 tuần trước hạn nộp hội nghị khoa học, dữ liệu cũ không còn tin cậy.",
            "action": "Không sửa số liệu gian lận; tổ chức đo đạc lại cảm biến, bổ sung kỹ thuật Cross-Validation và dữ liệu lịch sử.",
            "result": "Dù không đạt kỷ lục độ chính xác nhưng hiểu sâu sắc về phân phối dữ liệu và viết bài phân tích lỗi được khen ngợi."
        },
        "red_flags": [
            "Kể về một 'thất bại giả vờ' (ví dụ: 'tôi quá cầu toàn')",
            "Đổ lỗi cho đồng đội, thầy cô hoặc thiết bị hỏng",
            "Không rút ra được bài học phương pháp luận nào"
        ]
    },
    {
        "id": "q_ethics_impact",
        "category": "ethics_impact",
        "category_vi": "Đạo đức khoa học & Trách nhiệm xã hội",
        "question_vi": "Nếu công nghệ bạn phát triển có nguy cơ bị lạm dụng hoặc tạo ra định kiến gây hại xã hội, bạn sẽ xử lý như thế nào?",
        "question_en": "If a technology you build carries the risk of societal bias or misuse, how would you address this ethical dilemma?",
        "key_objectives": [
            "Tư duy đạo đức công nghệ (AI Ethics / Responsible Engineering)",
            "Không chỉ nhìn vào hiệu năng kỹ thuật mà thấy được tác động xã hội",
            "Đề xuất giải pháp kiểm toán (audit), minh bạch thuật toán và an toàn dữ liệu"
        ],
        "sample_star_outline": {
            "situation": "Phát triển công cụ tự động sàng lọc hồ sơ cho CLB, phát hiện mô hình thiên lệch về trường chuyên lớp chọn.",
            "task": "Đảm bảo tính công bằng mà không làm suy giảm chất lượng ứng viên.",
            "action": "Ẩn các trường thông tin nhận diện (Blind Review), tái cân bằng dữ liệu huấn luyện và bổ sung đánh giá thủ công.",
            "result": "Tỷ lệ học sinh từ các trường thường trúng tuyển tăng 40% mà hiệu quả hoạt động vẫn xuất sắc."
        },
        "red_flags": [
            "Cho rằng 'kỹ sư chỉ lo kỹ thuật, đạo đức là chuyện của nhà quản lý'",
            "Xem nhẹ các nguy cơ xã hội hoặc tính thiên kiến của dữ liệu"
        ]
    },
    {
        "id": "q_teamwork_conflict",
        "category": "leadership_team",
        "category_vi": "Lãnh đạo & Hóa giải mâu thuẫn kỹ thuật",
        "question_vi": "Khi làm việc nhóm trong một dự án STEM và nảy sinh tranh cãi gay gắt về kiến trúc giải pháp, bạn đã hóa giải thế nào?",
        "question_en": "When working on a technical team and facing fierce disagreements over solution design, how did you resolve the conflict?",
        "key_objectives": [
            "Kỹ năng lắng nghe và tư duy ra quyết định dựa trên dữ liệu thực nghiệm (Data-Driven)",
            "Tinh thần đồng đội, tôn trọng sự khác biệt",
            "Không để bất đồng cá nhân cản trở tiến độ dự án"
        ],
        "sample_star_outline": {
            "situation": "Đội thi Robotics tranh cãi giữa cơ chế bắn bóng bằng bánh đà hay cánh tay cơ học.",
            "task": "Cần chốt phương án cơ khí trong vòng 48h để kịp gia công linh kiện.",
            "action": "Đề xuất làm mẫu thử nghiệm thu nhỏ (A/B testing) và lập ma trận đánh giá định lượng: tốc độ, độ ổn định, chi phí.",
            "result": "Dữ liệu đo đạc thực tế thuyết phục cả đội nhất trí chọn bánh đà, đạt giải Ba toàn quốc."
        },
        "red_flags": [
            "Áp đặt ý kiến cá nhân bằng quyền lực",
            "Nhượng bộ vô nguyên tắc để dĩ hòa vi quý mà bỏ qua chất lượng kỹ thuật"
        ]
    },
    {
        "id": "q_future_vision",
        "category": "future_vision",
        "category_vi": "Tầm nhìn dài hạn & Đóng góp cộng đồng",
        "question_vi": "Trong 5 - 10 năm tới sau khi tốt nghiệp, bạn dự định đóng góp gì cụ thể cho cộng đồng khoa học kỹ thuật tại Việt Nam hoặc thế giới?",
        "question_en": "Looking 5 to 10 years ahead, what concrete contributions do you envision making to the STEM community in Vietnam or globally?",
        "key_objectives": [
            "Khát vọng cống hiến lớn lao (Purpose & Community Giveback)",
            "Tính khả thi của mục tiêu nghề nghiệp (nghiên cứu hàn lâm, startup công nghệ, chính sách khoa học)",
            "Sự kết nối giữa học bổng hôm nay với giá trị kiến tạo ngày mai"
        ],
        "sample_star_outline": {
            "situation": "Việt Nam có nguồn nhân lực trẻ dồi dào nhưng thiếu hệ sinh thái bán dẫn và AI chip thiết kế sâu.",
            "task": "Xây dựng năng lực nghiên cứu vi mạch tích hợp cho thế hệ kỹ sư mới.",
            "action": "Học tập chuyên sâu về VLSI/Computer Architecture, kết nối với các giáo sư đầu ngành để mở workshop chuyển giao tri thức.",
            "result": "Mục tiêu thành lập trung tâm thiết kế chip mã nguồn mở phục vụ nông nghiệp thông minh tại ĐBSCL."
        },
        "red_flags": [
            "Mục tiêu hoàn toàn vị kỷ (chỉ nói về kiếm nhiều tiền, thăng chức nhanh)",
            "Kế hoạch viển vông, không có các bước chuẩn bị nền móng thực tế"
        ]
    }
]


def get_all_questions() -> List[Dict[str, Any]]:
    """Lấy danh sách tất cả các câu hỏi phỏng vấn học bổng chuẩn hóa."""
    return INTERVIEW_QUESTIONS


def get_question_by_id(question_id: str) -> Optional[Dict[str, Any]]:
    """Tìm câu hỏi theo mã định danh."""
    for q in INTERVIEW_QUESTIONS:
        if q["id"] == question_id:
            return q
    return None


def evaluate_star_response(question_id: str, answer_text: str) -> Dict[str, Any]:
    """Phân tích câu trả lời phỏng vấn theo phương pháp STAR và trả về điểm số, nhận xét chi tiết."""
    q_data = get_question_by_id(question_id)
    text = (answer_text or "").strip()
    words = text.split()
    word_count = len(words)

    feedback_items: List[str] = []
    star_scores: Dict[str, float] = {
        "situation": 0.0,
        "task": 0.0,
        "action": 0.0,
        "result": 0.0
    }
    star_notes: Dict[str, str] = {}

    text_lower = text.lower()

    # 1. Đánh giá độ dài & dung lượng
    if word_count < 50:
        feedback_items.append("Câu trả lời quá ngắn (dưới 50 từ). Bạn chưa cung cấp đủ dữ liệu để hội đồng đánh giá năng lực tư duy.")
    elif word_count < 120:
        feedback_items.append("Độ dài ở mức trung bình. Nên mở rộng phần Hành động kỹ thuật (Action) và Kết quả đo lường (Result).")
    elif word_count > 600:
        feedback_items.append("Câu trả lời hơi dài dòng (trên 600 từ). Khi phỏng vấn trực tiếp dễ làm hội đồng mất kiên nhẫn. Nên cô đọng lại khoảng 200-350 từ.")
    else:
        feedback_items.append(f"Độ dài lý tưởng ({word_count} từ), tương đương 2-3 phút nói gãy gọn.")

    # 2. Phát hiện Situation (Bối cảnh) - Tối đa 25 điểm
    situation_keywords = ["khi", "trong lúc", "dự án", "năm lớp", "năm ngoái", "tại cuộc thi", "bối cảnh", "thực trạng", "đề tài", "when", "during", "in high school", "project", "competition"]
    s_matched = any(kw in text_lower for kw in situation_keywords)
    if s_matched and word_count >= 60:
        star_scores["situation"] = 22.0
        star_notes["situation"] = "Đã nêu rõ thời điểm, hoàn cảnh và bối cảnh dự án."
    elif s_matched or word_count >= 40:
        star_scores["situation"] = 15.0
        star_notes["situation"] = "Có nhắc đến bối cảnh nhưng cần cụ thể hóa rõ hơn địa điểm hoặc tính cấp thiết của vấn đề."
    else:
        star_scores["situation"] = 8.0
        star_notes["situation"] = "Thiếu phần thiết lập bối cảnh (Situation), người nghe chưa rõ sự việc diễn ra khi nào, tại đâu."

    # 3. Phát hiện Task (Nhiệm vụ & Thách thức) - Tối đa 25 điểm
    task_keywords = ["nhiệm vụ", "thách thức", "khó khăn", "vấn đề", "mục tiêu", "bài toán", "cần phải", "áp lực", "challenge", "task", "objective", "problem", "goal"]
    t_matched = any(kw in text_lower for kw in task_keywords)
    if t_matched:
        star_scores["task"] = 23.0
        star_notes["task"] = "Làm nổi bật bài toán hóc búa cần giải quyết hoặc trách nhiệm cá nhân."
    elif word_count >= 80:
        star_scores["task"] = 16.0
        star_notes["task"] = "Có đề cập đến nhiệm vụ nhưng chưa nhấn mạnh rõ rào cản lớn nhất là gì."
    else:
        star_scores["task"] = 9.0
        star_notes["task"] = "Chưa làm rõ bài toán thách thức (Task) mà bạn phải gánh vác."

    # 4. Phát hiện Action (Hành động cụ thể & Tư duy cá nhân) - Tối đa 25 điểm
    action_keywords = ["tôi đã", "chúng tôi đã", "nghiên cứu", "thử nghiệm", "thuật toán", "lập trình", "thiết kế", "chế tạo", "phân tích", "tối ưu", "áp dụng", "i designed", "i implemented", "i analyzed", "i tested", "developed"]
    a_count = sum(1 for kw in action_keywords if kw in text_lower)
    has_personal_pronoun = "tôi" in text_lower or "em" in text_lower or "mình" in text_lower or " i " in (" " + text_lower + " ")

    if a_count >= 3 and has_personal_pronoun:
        star_scores["action"] = 25.0
        star_notes["action"] = "Rất xuất sắc! Nêu rõ hành động kỹ thuật chuyên sâu và khẳng định rõ nét vai trò cá nhân."
    elif a_count >= 1:
        star_scores["action"] = 18.0
        star_notes["action"] = "Có nêu giải pháp nhưng cần chi tiết hơn về mặt kỹ thuật/phương pháp luận và sử dụng nhiều đại từ 'Tôi' thay vì nói chung chung."
    else:
        star_scores["action"] = 10.0
        star_notes["action"] = "Hành động (Action) còn mờ nhạt, người nghe chưa thấy được bạn thực sự đã làm những gì."

    # 5. Phát hiện Result (Kết quả định lượng & Bài học) - Tối đa 25 điểm
    has_numbers = bool(re.search(r'\d+', text))
    result_keywords = ["kết quả", "đạt được", "giải thưởng", "tăng", "giảm", "bài học", "nhận ra", "trưởng thành", "chiêm nghiệm", "tác động", "result", "achieved", "improved", "learned", "impact"]
    r_count = sum(1 for kw in result_keywords if kw in text_lower)

    if has_numbers and r_count >= 2:
        star_scores["result"] = 24.0
        star_notes["result"] = "Tuyệt vời! Kết quả có số liệu đo lường định lượng và đúc kết được bài học phương pháp luận."
    elif has_numbers or r_count >= 1:
        star_scores["result"] = 17.0
        star_notes["result"] = "Đã có kết quả nhưng nên bổ sung thêm số liệu % hoặc con số cụ thể và bài học bản thân rút ra."
    else:
        star_scores["result"] = 8.0
        star_notes["result"] = "Thiếu kết quả định lượng (Result) và bài học chiêm nghiệm."

    # Tính điểm tổng STAR (thang 100)
    total_star_score = round(sum(star_scores.values()), 1)

    if total_star_score >= 85:
        star_rating = "Đạt chuẩn Phỏng vấn Tinh hoa (Elite Interviewee)"
        feedback_items.append("Phản xạ phỏng vấn rất thuyết phục, kết cấu mạch lạc đúng cấu trúc STAR chuẩn mực.")
    elif total_star_score >= 70:
        star_rating = "Khá Tốt (Strong Interviewee)"
        feedback_items.append("Trả lời rõ ý. Nên bổ sung thêm các số liệu định lượng (metrics) để tăng tính minh chứng.")
    elif total_star_score >= 50:
        star_rating = "Cần Trau Chuốt (Developing)"
        feedback_items.append("Cần tái cấu trúc câu trả lời: tập trung 60% thời lượng cho phần Action (hành động kỹ thuật của bạn) và Result (kết quả đo lường).")
    else:
        star_rating = "Chưa Đạt Chuẩn (Needs Restructuring)"
        feedback_items.append("Câu trả lời chưa theo cấu trúc STAR. Hãy viết nháp theo từng gạch đầu dòng S - T - A - R trước khi nói.")

    # Đưa ra gợi ý cải thiện theo câu hỏi cụ thể
    coaching_tips: List[str] = []
    if q_data:
        coaching_tips.extend(q_data.get("key_objectives", []))

    return {
        "question_id": question_id,
        "question_vi": q_data.get("question_vi") if q_data else "",
        "word_count": word_count,
        "total_star_score": total_star_score,
        "star_rating": star_rating,
        "star_components": {
            "situation": {
                "score": star_scores["situation"],
                "max": 25.0,
                "notes": star_notes["situation"]
            },
            "task": {
                "score": star_scores["task"],
                "max": 25.0,
                "notes": star_notes["task"]
            },
            "action": {
                "score": star_scores["action"],
                "max": 25.0,
                "notes": star_notes["action"]
            },
            "result": {
                "score": star_scores["result"],
                "max": 25.0,
                "notes": star_notes["result"]
            }
        },
        "feedback": feedback_items,
        "coaching_tips": coaching_tips,
        "sample_outline": q_data.get("sample_star_outline") if q_data else {}
    }
