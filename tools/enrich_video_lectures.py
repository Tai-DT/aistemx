#!/usr/bin/env python3
"""Script thu thập & tích hợp Video bài giảng phân tích và Mô phỏng tương tác thật vào AISTEM.

Nguồn video chuẩn học thuật:
- Khan Academy / 3Blue1Brown / MIT OpenCourseWare / CrashCourse / Periodic Videos
- PhET Interactive Simulations (University of Colorado Boulder)
- Manim Vector Visualizations
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LESSONS_DIR = ROOT / "data" / "lessons"

# Kho video bài giảng phân tích & thí nghiệm chuẩn khoa học
CURATED_MEDIA_MAP = {
    # TOÁN HỌC (Calculus, Linear Algebra, Geometry)
    "dao-ham": {
        "video_lectures": [
            {
                "title": "Bản chất trực quan của Đạo hàm (Essence of Calculus)",
                "url": "https://www.youtube.com/watch?v=WUvTyaaNkzM",
                "provider": "3Blue1Brown",
                "duration": "17:05",
                "language": "en/vi",
                "timestamps": [
                    {"time": "02:15", "label": "Ý nghĩa hình học của tiếp tuyến & hệ số góc"},
                    {"time": "07:30", "label": "Giới hạn vi phân dy/dx"},
                    {"time": "12:40", "label": "Quy tắc lũy thừa x^n"}
                ]
            },
            {
                "title": "Derivative Rules & Intuition",
                "url": "https://www.khanacademy.org/math/calculus-1/cs1-derivatives-definition-and-basic-rules",
                "provider": "Khan Academy",
                "duration": "14:20",
                "language": "en"
            }
        ],
        "animations": [
            {
                "title": "Tiếp tuyến di động trên đồ thị hàm số",
                "type": "geogebra",
                "url": "https://www.geogebra.org/m/Jm8Wv8vA",
                "description": "Kéo điểm tiếp xúc để quan sát sự thay đổi hệ số góc và giá trị đạo hàm tức thời f'(x)"
            }
        ]
    },
    "tich-phan": {
        "video_lectures": [
            {
                "title": "Tích phân và định lý cơ bản của Giải tích",
                "url": "https://www.youtube.com/watch?v=rfG8ce4nNh0",
                "provider": "3Blue1Brown",
                "duration": "20:45",
                "language": "en/vi"
            }
        ],
        "animations": [
            {
                "title": "Tổng Riemann và diện tích dưới đường cong",
                "type": "geogebra",
                "url": "https://www.geogebra.org/m/e4M5nsqH",
                "description": "Tăng số lượng hình chữ nhật N để thấy tổng Riemann tiệm cận về tích phân chính xác"
            }
        ]
    },

    # VẬT LÍ (Cơ học, Sóng, Điện từ)
    "con-lac": {
        "video_lectures": [
            {
                "title": "Mô phỏng và thực nghiệm Con lắc đơn & Con lắc lò xo",
                "url": "https://www.youtube.com/watch?v=yVkdfJ9PkRQ",
                "provider": "MIT OpenCourseWare (Walter Lewin)",
                "duration": "48:10",
                "language": "en"
            }
        ],
        "animations": [
            {
                "title": "PhET Con Lắc & Bảo Toàn Cơ Năng",
                "type": "phet",
                "url": "https://phet.colorado.edu/sims/html/pendulum-lab/latest/pendulum-lab_all.html",
                "description": "Khảo sát dao động điều hòa, vận tốc, gia tốc, thế năng và động năng theo thời gian thực"
            }
        ]
    },
    "giao-thoa": {
        "video_lectures": [
            {
                "title": "Thí nghiệm giao thoa khe Young ánh sáng laser thực tế",
                "url": "https://www.youtube.com/watch?v=Iuv6hY6zsd0",
                "provider": "Veritasium",
                "duration": "08:12",
                "language": "en"
            }
        ],
        "animations": [
            {
                "title": "PhET Giao thoa sóng và ánh sáng",
                "type": "phet",
                "url": "https://phet.colorado.edu/sims/html/wave-interference/latest/wave-interference_all.html",
                "description": "Mô phỏng sóng nước, sóng âm và sóng ánh sáng đi qua 2 khe hẹp"
            }
        ]
    },

    # HOÁ HỌC (Cấu tạo chất, Phản ứng, Chuẩn độ)
    "chuan-do": {
        "video_lectures": [
            {
                "title": "Thí nghiệm chuẩn độ Axit - Bazơ dùng chỉ thị Phenolphthalein",
                "url": "https://www.youtube.com/watch?v=8UiuE7Xx5l8",
                "provider": "Royal Society of Chemistry",
                "duration": "05:40",
                "language": "en"
            }
        ],
        "animations": [
            {
                "title": "Đường cong chuẩn độ pH tương tác",
                "type": "interactive",
                "url": "https://chemcollective.org/activities/simulations/titration",
                "description": "Mô phỏng giọt chuẩn độ burette và biểu đồ pH tương ứng"
            }
        ]
    },
    "benzen": {
        "video_lectures": [
            {
                "title": "Benzene Structure & Aromaticity Chemistry",
                "url": "https://www.youtube.com/watch?v=84_LgY3-4f0",
                "provider": "Professor Dave Explains",
                "duration": "09:30",
                "language": "en"
            }
        ],
        "animations": [
            {
                "title": "Mô hình không gian phân tử Benzen 3D",
                "type": "threejs",
                "url": "https://pubchem.ncbi.nlm.nih.gov/compound/241#section=3D-Conformer",
                "description": "Cấu trúc vòng thơm phẳng 6 cạnh đều với hệ electron pi giải tỏa"
            }
        ]
    },

    # SINH HỌC (Di truyền, ADN, Tế bào)
    "adn": {
        "video_lectures": [
            {
                "title": "Cơ chế nhân đôi ADN (DNA Replication 3D Animation)",
                "url": "https://www.youtube.com/watch?v=TNKWgcFPHqw",
                "provider": "HHMI BioInteractive",
                "duration": "04:25",
                "language": "en/vi",
                "timestamps": [
                    {"time": "00:40", "label": "Helicase tháo xoắn"},
                    {"time": "01:20", "label": "DNA Polymerase tổng hợp mạch dẫn đầu (Leading strand)"},
                    {"time": "02:35", "label": "Đoạn Okazaki trên mạch đi sau (Lagging strand)"}
                ]
            }
        ],
        "animations": [
            {
                "title": "Xoắn kép ADN tương tác 3D",
                "type": "threejs",
                "url": "https://www.rcsb.org/3d-view/1BNA",
                "description": "Tọa độ nguyên tử B-DNA từ Protein Data Bank (RCSB PDB 1BNA)"
            }
        ]
    }
}


def enrich_lessons():
    print("=== NẠP VIDEO BÀI GIẢNG PHÂN TÍCH & MÔ PHỎNG VÀO CÁC BÀI HỌC ===")
    total_matched = 0
    lesson_files = list(LESSONS_DIR.glob("*.json"))

    for fpath in sorted(lesson_files):
        if fpath.name in ("schema.json", "index.json"):
            continue
        data = json.loads(fpath.read_text(encoding="utf-8"))
        lessons = data.get("lessons", [])
        modified = False

        for lesson in lessons:
            lid = lesson.get("id", "")
            tags = lesson.get("tags", [])
            title = (lesson.get("title_vi", "") + " " + lesson.get("title_en", "")).lower()

            for key, media in CURATED_MEDIA_MAP.items():
                if key in lid or key in tags or key in title:
                    if "video_lectures" in media and "video_lectures" not in lesson:
                        lesson["video_lectures"] = media["video_lectures"]
                        modified = True
                        total_matched += 1
                    if "animations" in media and "animations" not in lesson:
                        lesson["animations"] = media["animations"]
                        modified = True

        if modified:
            fpath.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"  ✓ Đã cập nhật media cho: {fpath.name}")

    print(f"\n✓ Hoàn tất gắn video bài giảng và mô phỏng thực nghiệm vào hệ thống.")


if __name__ == "__main__":
    enrich_lessons()
