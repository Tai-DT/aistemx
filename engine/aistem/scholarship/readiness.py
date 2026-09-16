"""Mô-đun đánh giá năng lực hồ sơ săn học bổng STEM (Profile Readiness Assessment).

Đánh giá định lượng 4 trụ cột cốt lõi (0 - 100 điểm):
1. Academic Excellence (0 - 25 điểm): GPA, SAT/ACT, IELTS/TOEFL, AP/IB.
2. STEM Competitions & Research (0 - 25 điểm): Giải quốc gia, Olympic quốc tế, AMC/AIME, ISEF, bài báo nghiên cứu.
3. Spike Profile & Extracurriculars (0 - 25 điểm): Độ sâu chuyên môn vượt trội, lãnh đạo, sản phẩm kỹ thuật/dự án cộng đồng có tác động đo lường được.
4. Essays, Storytelling & LORs (0 - 25 điểm): Chiều sâu tư duy, tính chân thực, bản lĩnh vượt khó và thư giới thiệu.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional


def assess_profile_readiness(profile: Dict[str, Any]) -> Dict[str, Any]:
    """Đánh giá toàn diện hồ sơ học bổng STEM và xuất phân tích khoảng cách (Gap Analysis)."""
    strengths: List[str] = []
    gaps: List[Dict[str, str]] = []

    # -------------------------------------------------------------
    # 1. Trụ cột 1: Academic Excellence (Tối đa 25 điểm)
    # -------------------------------------------------------------
    academic_score = 0.0
    academic_details: List[str] = []

    # GPA (tối đa 8 điểm)
    gpa = float(profile.get("gpa", 0.0))
    # Hỗ trợ cả thang 4.0 và thang 10.0
    gpa_normalized = gpa / 4.0 * 10.0 if gpa <= 4.0 and gpa > 0 else gpa
    if gpa_normalized >= 9.5:
        academic_score += 8.0
        academic_details.append(f"GPA xuất sắc ({gpa}/10): +8.0 đ")
        strengths.append(f"GPA {gpa} thuộc top 1-2% toàn khóa học.")
    elif gpa_normalized >= 9.0:
        academic_score += 6.5
        academic_details.append(f"GPA giỏi ({gpa}/10): +6.5 đ")
        strengths.append(f"GPA {gpa} đáp ứng phần lớn các đại học top 30-50.")
    elif gpa_normalized >= 8.5:
        academic_score += 5.0
        academic_details.append(f"GPA khá tốt ({gpa}/10): +5.0 đ")
        gaps.append({
            "pillar": "Academic",
            "issue": f"GPA {gpa} ở mức khá nhưng chưa tối ưu cho học bổng toàn phần Ivy/Top 20.",
            "recommendation": "Duy trì và kéo điểm các môn STEM (Toán, Lý, Tin, Hóa) kỳ tới đạt trên 9.2 để nâng cao học bạ."
        })
    elif gpa_normalized > 0:
        academic_score += 3.0
        academic_details.append(f"GPA trung bình ({gpa}/10): +3.0 đ")
        gaps.append({
            "pillar": "Academic",
            "issue": f"GPA {gpa} dưới ngưỡng an toàn 8.5 cho học bổng quốc tế cạnh tranh.",
            "recommendation": "Tập trung cải thiện điểm số môn trọng tâm và bù đắp bằng điểm SAT/chứng chỉ AP thật cao."
        })
    else:
        gaps.append({
            "pillar": "Academic",
            "issue": "Chưa cung cấp điểm GPA THPT/Đại học.",
            "recommendation": "Bổ sung điểm GPA để hệ thống tính toán chính xác."
        })

    # Chuẩn hóa SAT (tối đa 9 điểm)
    sat = int(profile.get("sat", 0) or 0)
    act = int(profile.get("act", 0) or 0)
    if act > 0 and sat == 0:
        # Chuyển đổi ACT xấp xỉ sang SAT
        if act >= 35:
            sat = 1550
        elif act >= 33:
            sat = 1480
        elif act >= 30:
            sat = 1380
        else:
            sat = 1250

    if sat >= 1530:
        academic_score += 9.0
        academic_details.append(f"SAT tinh hoa ({sat}/1600): +9.0 đ")
        strengths.append(f"Điểm chuẩn hóa SAT {sat} đạt chuẩn Ivy League và MIT Need-Blind.")
    elif sat >= 1480:
        academic_score += 7.5
        academic_details.append(f"SAT rất tốt ({sat}/1600): +7.5 đ")
        strengths.append(f"SAT {sat} cạnh tranh mạnh cho Top 20-50 Mỹ và ASEAN NUS/NTU.")
    elif sat >= 1400:
        academic_score += 5.5
        academic_details.append(f"SAT khá ({sat}/1600): +5.5 đ")
        gaps.append({
            "pillar": "Academic",
            "issue": f"Điểm SAT {sat} chưa đủ bứt phá ở nhánh trường Need-Blind / Full-Ride.",
            "recommendation": "Luyện thi nâng điểm Digital SAT Math lên tiệm cận 780-800 để tối ưu hóa hồ sơ STEM."
        })
    elif sat > 0:
        academic_score += 3.5
        academic_details.append(f"SAT cơ bản ({sat}/1600): +3.5 đ")
        gaps.append({
            "pillar": "Academic",
            "issue": f"SAT {sat} dưới mức trung bình của học bổng cạnh tranh.",
            "recommendation": "Cần kế hoạch ôn luyện 3-6 tháng hoặc cân nhắc chính sách Test-Optional."
        })
    else:
        gaps.append({
            "pillar": "Academic",
            "issue": "Chưa có chứng chỉ chuẩn hóa SAT / ACT.",
            "recommendation": "Thi Digital SAT (mục tiêu >= 1480 cho STEM) hoặc nhắm các trường chấp nhận Test-Optional."
        })

    # Tiếng Anh: IELTS / TOEFL / Duolingo (tối đa 4 điểm)
    ielts = float(profile.get("ielts", 0.0) or 0.0)
    toefl = int(profile.get("toefl", 0) or 0)
    if toefl > 0 and ielts == 0.0:
        if toefl >= 110:
            ielts = 8.0
        elif toefl >= 100:
            ielts = 7.5
        elif toefl >= 90:
            ielts = 7.0
        else:
            ielts = 6.0

    if ielts >= 8.0:
        academic_score += 4.0
        academic_details.append(f"IELTS xuất sắc ({ielts}): +4.0 đ")
        strengths.append(f"Năng lực ngoại ngữ IELTS {ielts} đáp ứng 100% mọi đại học hàng đầu thế giới.")
    elif ielts >= 7.5:
        academic_score += 3.5
        academic_details.append(f"IELTS rất tốt ({ielts}): +3.5 đ")
    elif ielts >= 7.0:
        academic_score += 2.5
        academic_details.append(f"IELTS đạt chuẩn ({ielts}): +2.5 đ")
    elif ielts >= 6.5:
        academic_score += 1.5
        academic_details.append(f"IELTS cơ bản ({ielts}): +1.5 đ")
        gaps.append({
            "pillar": "Academic",
            "issue": f"IELTS {ielts} chỉ ở mức điều kiện tối thiểu, dễ bị trừ điểm cạnh tranh phỏng vấn.",
            "recommendation": "Nâng điểm IELTS lên tối thiểu 7.5 (đặc biệt là kỹ năng Speaking & Writing)."
        })
    else:
        gaps.append({
            "pillar": "Academic",
            "issue": "Chưa có chứng chỉ IELTS / TOEFL.",
            "recommendation": "Đăng ký thi IELTS học thuật sớm để hoàn thiện hồ sơ xét tuyển."
        })

    # AP / IB / Các môn nâng cao (tối đa 4 điểm)
    ap_count = int(profile.get("ap_count", 0) or 0)
    has_ib = bool(profile.get("has_ib", False))
    if ap_count >= 4 or has_ib:
        academic_score += 4.0
        academic_details.append(f"Chương trình nâng cao (AP: {ap_count} môn / IB Diploma): +4.0 đ")
        strengths.append("Có nền tảng môn học nâng cao AP/IB thể hiện tinh thần sẵn sàng đón nhận thử thách.")
    elif ap_count >= 2:
        academic_score += 2.5
        academic_details.append(f"AP cơ bản ({ap_count} môn): +2.5 đ")
    elif ap_count == 1:
        academic_score += 1.0
        academic_details.append("1 môn AP: +1.0 đ")
    else:
        gaps.append({
            "pillar": "Academic",
            "issue": "Chưa có môn nâng cao AP (Advanced Placement) hoặc bằng IB.",
            "recommendation": "Tự học hoặc thi chứng chỉ AP Calculus BC, AP Physics C hoặc AP Computer Science A để gia tăng tính cạnh tranh."
        })

    academic_score = min(academic_score, 25.0)

    # -------------------------------------------------------------
    # 2. Trụ cột 2: STEM Competitions & Research (Tối đa 25 điểm)
    # -------------------------------------------------------------
    stem_score = 0.0
    stem_details: List[str] = []

    competitions: List[Dict[str, Any]] = profile.get("competitions", [])
    research_papers: List[Dict[str, Any]] = profile.get("research_papers", [])

    # Đánh giá các giải thưởng
    has_intl_olympiad = False
    has_national_prize = False
    has_amc_aime = False
    has_isef = False
    has_robotics = False

    for comp in competitions:
        level = comp.get("level", "").lower()
        prize = comp.get("prize", "").lower()
        name = comp.get("name", "").lower()

        if "quoc te" in level or "international" in level or "olympic" in name or "imo" in name or "ipho" in name or "icho" in name or "ioi" in name or "ibo" in name:
            has_intl_olympiad = True
        if "quoc gia" in level or "national" in level or "hsgqg" in name:
            has_national_prize = True
        if "aime" in name or "amc" in name:
            has_amc_aime = True
        if "isef" in name or "khoa hoc ky thuat" in name or "viisef" in name:
            has_isef = True
        if "robotics" in name or "vex" in name or "first" in name:
            has_robotics = True

    if has_intl_olympiad:
        stem_score += 16.0
        stem_details.append("Huy chương / Đại diện Olympic Khoa học Quốc tế (IMO/IPhO/IChO/IOI/IBO): +16.0 đ")
        strengths.append("Sở hữu thành tích Olympic Khoa học Quốc tế - bảo chứng năng lực trí tuệ hàng đầu thế giới.")
    elif has_national_prize:
        stem_score += 12.0
        stem_details.append("Giải Học sinh Giỏi Quốc gia / Vòng chọn đội tuyển Quốc tế: +12.0 đ")
        strengths.append("Đạt giải Học sinh Giỏi Quốc gia môn STEM, khẳng định vị thế top đầu cả nước.")
    elif has_amc_aime:
        stem_score += 8.0
        stem_details.append("Chứng nhận AMC Top 5% / Vòng AIME Hoa Kỳ: +8.0 đ")
        strengths.append("Đạt chuẩn AIME/AMC được công nhận rộng rãi bởi hội đồng tuyển sinh MIT, Caltech, Stanford.")
    elif competitions:
        stem_score += 5.0
        stem_details.append("Giải thưởng cấp Tỉnh / Thành phố hoặc cuộc thi học thuật mở rộng: +5.0 đ")

    if has_isef:
        stem_score += 6.0
        stem_details.append("Giải thưởng Khoa học Kỹ thuật ISEF / ViISEF Quốc gia: +6.0 đ")
        strengths.append("Dự án ISEF thể hiện năng lực nghiên cứu ứng dụng và tư duy khoa học thực nghiệm.")

    if has_robotics:
        stem_score += 4.0
        stem_details.append("Giải đấu Kỹ thuật / Robotics (VEX / FIRST): +4.0 đ")

    # Đánh giá bài báo nghiên cứu khoa học
    paper_count = len(research_papers)
    if paper_count >= 2:
        stem_score += 7.0
        stem_details.append(f"{paper_count} bài báo khoa học / Preprints: +7.0 đ")
        strengths.append(f"Công bố {paper_count} công trình nghiên cứu khoa học, vượt trội so với ứng viên cùng lứa tuổi.")
    elif paper_count == 1:
        stem_score += 4.5
        stem_details.append("1 bài báo / công trình nghiên cứu khoa học có mentor: +4.5 đ")
        strengths.append("Có kinh nghiệm nghiên cứu khoa học thực thụ cùng giảng viên/chuyên gia.")
    else:
        if not has_isef:
            gaps.append({
                "pillar": "STEM Competitions & Research",
                "issue": "Thiếu các công trình nghiên cứu khoa học độc lập hoặc dự án ISEF.",
                "recommendation": "Xây dựng 1 dự án nghiên cứu khoa học dưới sự cố vấn của thầy cô/mentor và gửi tham gia các cuộc thi KHKT hoặc tạp chí học sinh."
            })

    if not competitions:
        gaps.append({
            "pillar": "STEM Competitions & Research",
            "issue": "Chưa tham gia các kỳ thi chuyên môn Toán/STEM chuẩn mực.",
            "recommendation": "Đăng ký thử sức với kỳ thi AMC 10/12 (Toán) hoặc cuộc thi lập trình quốc tế (USACO/ICPC)."
        })

    stem_score = min(stem_score, 25.0)

    # -------------------------------------------------------------
    # 3. Trụ cột 3: Spike Profile & Extracurriculars (Tối đa 25 điểm)
    # -------------------------------------------------------------
    spike_score = 0.0
    spike_details: List[str] = []

    activities: List[Dict[str, Any]] = profile.get("activities", [])
    spike_domain = profile.get("spike_domain", "").strip()

    has_spike = bool(spike_domain)
    has_founder_role = False
    has_tech_product = False
    has_measurable_impact = False

    for act in activities:
        role = act.get("role", "").lower()
        desc = act.get("description", "").lower()
        impact = str(act.get("impact", "")).lower()

        if any(w in role for w in ["founder", "chu tich", "truong ban", "leader", "captain", "sang lap"]):
            has_founder_role = True
        if any(w in desc or w in impact for w in ["github", "app", "website", "san pham", "sang che", "patent", "open-source"]):
            has_tech_product = True
        if any(c.isdigit() for c in impact) and any(w in impact for w in ["usd", "vnd", "hoc sinh", "nguoi dung", "users", "luot tai", "quyen gop", "hoc vien"]):
            has_measurable_impact = True

    if has_spike:
        spike_score += 8.0
        spike_details.append(f"Định vị mũi nhọn (Spike Domain: '{spike_domain}'): +8.0 đ")
        strengths.append(f"Hồ sơ có mũi nhọn rõ ràng ({spike_domain}), tránh bẫy 'toàn diện nhưng mờ nhạt'.")
    else:
        gaps.append({
            "pillar": "Spike Profile & Extracurriculars",
            "issue": "Hồ sơ chưa xác định được mũi nhọn duy nhất (Spike Profile).",
            "recommendation": "Tập trung xoay quanh một chủ đề hạt nhân (ví dụ: 'Ứng dụng AI chẩn đoán bệnh võng mạc' thay vì tham gia nhiều CLB dàn trải)."
        })

    if has_founder_role:
        spike_score += 6.0
        spike_details.append("Vai trò Lãnh đạo / Sáng lập tổ chức STEM: +6.0 đ")
        strengths.append("Thể hiện năng lực lãnh đạo thực tế qua vai trò sáng lập và dẫn dắt đội ngũ.")
    else:
        spike_score += 3.0
        spike_details.append("Thành viên tích cực trong hoạt động ngoại khóa: +3.0 đ")
        gaps.append({
            "pillar": "Spike Profile & Extracurriculars",
            "issue": "Chưa có vai trò thủ lĩnh hoặc sáng lập dự án mang dấu ấn cá nhân.",
            "recommendation": "Khởi xướng một sáng kiến/dự án nhỏ giải quyết vấn đề thực tế trong trường học hoặc địa phương."
        })

    if has_tech_product:
        spike_score += 6.0
        spike_details.append("Sản phẩm kỹ thuật / Mã nguồn mở có người dùng: +6.0 đ")
        strengths.append("Có sản phẩm công nghệ thực tiễn, chứng minh khả năng chuyển hóa kiến thức thành hành động.")
    elif len(activities) >= 2 or any("clb" in a.get("description", "").lower() or "dự án" in a.get("description", "").lower() or "câu lạc bộ" in a.get("description", "").lower() for a in activities):
        spike_score += 4.0
        spike_details.append("Dự án quy mô lớn / Câu lạc bộ mở rộng: +4.0 đ")
    else:
        gaps.append({
            "pillar": "Spike Profile & Extracurriculars",
            "issue": "Thiếu các sản phẩm kỹ thuật, phần mềm hoặc nguyên mẫu thử nghiệm (Portfolio/Github).",
            "recommendation": "Xây dựng dự án Github hoặc nguyên mẫu thiết bị mẫu (Prototype) minh họa cho hồ sơ."
        })

    if has_measurable_impact:
        spike_score += 5.0
        spike_details.append("Tác động cộng đồng đo lường được bằng số liệu thực tế: +5.0 đ")
        strengths.append("Hoạt động ngoại khóa có số liệu tác động cụ thể, tạo sức thuyết phục vượt trội cho hội đồng tuyển sinh.")
    else:
        spike_score += 2.0
        gaps.append({
            "pillar": "Spike Profile & Extracurriculars",
            "issue": "Mô tả hoạt động ngoại khóa chưa có số liệu định lượng (Quantifiable Impact).",
            "recommendation": "Viết lại phần hoạt động bằng số liệu đo lường (số người thụ hưởng, kinh phí gây quỹ, số giờ đào tạo)."
        })

    spike_score = min(spike_score, 25.0)

    # -------------------------------------------------------------
    # 4. Trụ cột 4: Essays, Storytelling & LORs (Tối đa 25 điểm)
    # -------------------------------------------------------------
    essays_score = 0.0
    essays_details: List[str] = []

    essay_status = profile.get("essay_status", "not_started").lower()
    has_counselor_lor = bool(profile.get("has_counselor_lor", False))
    has_stem_teacher_lor = bool(profile.get("has_stem_teacher_lor", False))
    has_research_mentor_lor = bool(profile.get("has_research_mentor_lor", False))

    if essay_status in ["completed", "polished", "ready"]:
        essays_score += 12.0
        essays_details.append("Bài luận chính & Luận phụ đã hoàn thiện: +12.0 đ")
        strengths.append("Bài luận cá nhân đã được trau chuốt, sẵn sàng cho các kỳ nộp đơn sớm (ED/EA).")
    elif essay_status in ["drafting", "in_progress", "dang_viet"]:
        essays_score += 7.0
        essays_details.append("Bài luận đang trong giai đoạn viết nháp/sửa bản thảo: +7.0 đ")
    else:
        essays_score += 2.0
        gaps.append({
            "pillar": "Essays & LORs",
            "issue": "Chưa bắt đầu viết bài luận cá nhân (Common App / Scholarship Essay).",
            "recommendation": "Lên dàn ý bài luận chính xoay quanh bước ngoặt tư duy hoặc thất bại đã biến thành bài học đắt giá."
        })

    lor_score = 0.0
    if has_research_mentor_lor:
        lor_score += 5.0
        essays_details.append("Thư giới thiệu từ Giáo sư / Mentor nghiên cứu khoa học: +5.0 đ")
        strengths.append("Có thư giới thiệu từ nhà khoa học/giáo sư chứng nhận năng lực nghiên cứu độc lập.")
    if has_stem_teacher_lor:
        lor_score += 4.0
        essays_details.append("Thư giới thiệu từ Giáo viên bộ môn STEM (Toán/Lý/Tin): +4.0 đ")
    else:
        gaps.append({
            "pillar": "Essays & LORs",
            "issue": "Chưa chốt giáo viên viết thư giới thiệu môn STEM.",
            "recommendation": "Kết nối sớm với thầy cô dạy Toán/Khoa học hiểu rõ sự nỗ lực và tính tò mò của bạn."
        })

    if has_counselor_lor:
        lor_score += 4.0
        essays_details.append("Thư đánh giá từ Cố vấn học tập (Counselor Recommendation): +4.0 đ")
    else:
        lor_score += 2.0

    essays_score += min(lor_score, 13.0)
    essays_score = min(essays_score, 25.0)

    # -------------------------------------------------------------
    # Tổng kết & Xếp hạng Hồ sơ
    # -------------------------------------------------------------
    total_score = round(academic_score + stem_score + spike_score + essays_score, 1)

    if total_score >= 85.0:
        tier = "Elite Tier (Cạnh tranh Ivy League, MIT, Stanford, NUS/NTU Full-Ride)"
        readiness_label = "Sẵn sàng chinh phục học bổng toàn phần tinh hoa toàn cầu"
    elif total_score >= 70.0:
        tier = "Strong Tier (Ứng viên sáng giá Top 20-50 Thế giới, KAIST, MEXT, VinUni Toàn phần)"
        readiness_label = "Hồ sơ rất mạnh, cần tối ưu hóa bài luận và chiến lược nộp đơn"
    elif total_score >= 50.0:
        tier = "Competitive Tier (Học bổng 50-100% Học phí, Đại học công lập chất lượng cao)"
        readiness_label = "Nền tảng tốt, cần tăng tốc bồi đắp các mũi nhọn còn thiếu"
    else:
        tier = "Developing Tier (Giai đoạn xây dựng nền tảng học thuật & ngoại khóa)"
        readiness_label = "Cần lộ trình 1-2 năm tích lũy điểm số và thành tích chuyên sâu"

    return {
        "overall_score": total_score,
        "max_score": 100.0,
        "tier": tier,
        "readiness_label": readiness_label,
        "pillars": {
            "academic": {
                "name": "Năng lực Học thuật & Điểm chuẩn hóa",
                "score": round(academic_score, 1),
                "max": 25.0,
                "percentage": round(academic_score / 25.0 * 100, 1),
                "details": academic_details
            },
            "stem_awards": {
                "name": "Giải thưởng & Nghiên cứu STEM",
                "score": round(stem_score, 1),
                "max": 25.0,
                "percentage": round(stem_score / 25.0 * 100, 1),
                "details": stem_details
            },
            "spike_profile": {
                "name": "Hồ sơ Mũi nhọn & Hoạt động Ngoại khóa",
                "score": round(spike_score, 1),
                "max": 25.0,
                "percentage": round(spike_score / 25.0 * 100, 1),
                "details": spike_details
            },
            "essays_lors": {
                "name": "Bài luận, Khát vọng & Thư giới thiệu",
                "score": round(essays_score, 1),
                "max": 25.0,
                "percentage": round(essays_score / 25.0 * 100, 1),
                "details": essays_details
            }
        },
        "strengths": strengths,
        "gap_analysis": gaps
    }
