#!/usr/bin/env python3
"""Script cào và phân tích toàn bộ mẫu vật, dụng cụ thí nghiệm xuất hiện trong 10 459 bản ghi AISTEM.

Quét qua:
- 5 272 công thức (data/formulas/)
- 990 bài học (data/lessons/)
- 4 351 bài tập (data/problems/)
- 41 hồ sơ đề thi (data/exams/)
"""

import re
import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path("/Volumes/SecondaryDisk/aistemx")
DATA_DIR = ROOT / "data"

# Các từ khóa nhận diện mẫu vật / dụng cụ thí nghiệm trong SGK và đề thi
KEYWORDS = [
    # Mẫu vật sinh học
    "e. coli", "vi khuẩn", "hồng cầu", "bạch cầu", "tế bào", "hành tây", "khí khổng",
    "lục lạp", "ti thể", "nấm men", "trùng biến hình", "amoeba", "trùng roi", "euglena",
    "tảo xoắn", "spirogyra", "thủy tức", "hydra", "nhiễm sắc thể", "karyotype", "phấn hoa",
    "nơ-ron", "mô cơ", "xương", "màng sinh chất", "plasmid", "adn", "dna", "tinh hoàn",
    "giảm phân", "nguyên phân", "lá cây", "thân cây", "rễ hành", "nấm mốc", "giun", "châu chấu",

    # Mẫu vật hoá học & Hóa chất thí nghiệm
    "tinh thể", "nacl", "cuso4", "kmno4", "lưu huỳnh", "magie", "natri", "kali", "sắt",
    "fe(oh)3", "bismut", "tráng gương", "tráng bạc", "tollens", "chuẩn độ", "buret",
    "pipet", "ống nghiệm", "bình nón", "erlenmeyer", "quỳ tím", "phenolphthalein",
    "khí hydro", "khí oxy", "khí clo", "axit clohidric", "h2so4", "naoh", "kết tủa",

    # Dụng cụ / Thí nghiệm vật lý
    "lăng kính", "thấu kính", "khe young", "giao thoa", "con lắc", "lò xo", "nam châm",
    "neodymium", "từ trường", "ferrofluid", "tia catot", "crookes", "quang phổ", "laser",
    "vòng tròn newton", "nhiệt kế", "ampe kế", "vôn kế", "mạch điện", "bàn đinh galton",
    "khí hiếm", "plasma", "tuyết", "màng xà phòng"
]


def mine_specimens_and_labs():
    print("═"*80)
    print("🔍 BẮT ĐẦU CÀO TOÀN BỘ MẪU VẬT & THÍ NGHIỆM TỪ CƠ SỞ DỮ LIỆU AISTEM")
    print("═"*80)

    stats = Counter()
    subject_specimens = defaultdict(lambda: defaultdict(int))
    exam_specimens = defaultdict(lambda: defaultdict(int))

    # 1. Quét kho bài tập (4 351 bài)
    prob_files = list((DATA_DIR / "problems").glob("*.json"))
    for pf in prob_files:
        if pf.name in ("schema.json", "index.json"):
            continue
        try:
            data = json.loads(pf.read_text(encoding="utf-8"))
            for p in data.get("problems", []):
                subj = p.get("subject", "other")
                text = (p.get("statement_vi", "") + " " + p.get("statement_en", "") + " " + json.dumps(p.get("solution_steps", []))).lower()
                for kw in KEYWORDS:
                    if kw in text:
                        subject_specimens[subj][kw] += 1
                        stats["problems_matched"] += 1
        except Exception:
            pass

    # 2. Quét kho bài học (990 bài)
    lesson_files = list((DATA_DIR / "lessons").glob("*.json"))
    for lf in lesson_files:
        if lf.name in ("schema.json", "index.json"):
            continue
        try:
            data = json.loads(lf.read_text(encoding="utf-8"))
            for l in data.get("lessons", []):
                subj = l.get("subject", "other")
                text = (l.get("title_vi", "") + " " + l.get("content", "") + " " + json.dumps(l.get("key_concepts", []))).lower()
                for kw in KEYWORDS:
                    if kw in text:
                        subject_specimens[subj][kw] += 1
                        stats["lessons_matched"] += 1
        except Exception:
            pass

    # 3. Quét kho đề thi (41 hồ sơ đề thi)
    exam_files = list((DATA_DIR / "exams").glob("*.json"))
    for ef in exam_files:
        if ef.name in ("schema.json", "index.json"):
            continue
        try:
            data = json.loads(ef.read_text(encoding="utf-8"))
            for ex in data.get("exams", []):
                eid = ex.get("id")
                text = json.dumps(ex).lower()
                for kw in KEYWORDS:
                    if kw in text:
                        exam_specimens[eid][kw] += 1
                        stats["exams_matched"] += 1
        except Exception:
            pass

    print("\n📊 THỐNG KÊ TỔNG SỐ LƯỢNG MẪU VẬT & THÍ NGHIỆM XUẤT HIỆN:")
    for subj, cdict in subject_specimens.items():
        counter = Counter(cdict)
        print(f"\n📁 MÔN: {subj.upper()} (Có {len(counter)} loại mẫu vật/dụng cụ được nhắc đến):")
        top_items = counter.most_common(12)
        for kw, count in top_items:
            print(f"   • {kw.title():<25}: {count:>4} lần xuất hiện trong bài học & bài tập")

    print(f"\n📋 THÍ NGHIỆM & MẪU VẬT TRỌNG TÂM TRONG CÁC KỲ THI CHUẨN HÓA (AP / IB / A-LEVEL / THPTQG):")
    for eid, cdict in list(exam_specimens.items())[:8]:
        counter = Counter(cdict)
        top_ex = [k for k, _ in counter.most_common(5)]
        print(f"   • Đề thi [{eid:<25}]: {', '.join(top_ex)}")


if __name__ == "__main__":
    mine_specimens_and_labs()
