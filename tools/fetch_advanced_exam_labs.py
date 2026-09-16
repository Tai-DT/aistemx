#!/usr/bin/env python3
"""Script kiểm tra và nạp 6 thiết bị/thí nghiệm thực tế chuyên sâu cuối cùng từ các kỳ thi AP/IB/Olympiad.

6 Thiết bị & Thí nghiệm bổ sung:
1. Sinh học:
   - Bản Gel Điện Di ADN (Agarose Gel Electrophoresis UV Transilluminator)
   - Thí nghiệm Thẩm thấu Khối Thạch Agar-Phenolphthalein (Agar Cube Diffusion Lab)
   - Ti thể dưới kính hiển vi điện tử truyền qua (Mitochondria TEM Micrograph)

2. Hoá học:
   - Máy Quang Phổ Hấp Thụ Phân Tử UV-Vis (Spectrophotometer & Cuvette)
   - Nhiệt lượng kế đo nhiệt phản ứng (Coffee Cup / Bomb Calorimeter)

3. Vật lý:
   - Dao Động Ký Điện Tử Khảo Sát Sóng & Mạch RLC (Digital Storage Oscilloscope CRT/LCD)
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

PUBLIC_DIR = Path("/Volumes/SecondaryDisk/aistemx/frontend/public/real_specimens")
PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

ADVANCED_EXAM_LABS = [
    {
        "query": "Agarose gel electrophoresis DNA bands UV illumination",
        "id": "specimen_gel_electrophoresis",
        "name_vi": "Bản Gel Điện Di ADN Dưới Ánh Sáng Tia Cực Tím UV",
        "name_en": "Agarose Gel Electrophoresis DNA Bands Under UV",
        "category": "biology",
        "type": "Công nghệ sinh học phân tử & Di truyền",
        "magnification": "Thang đo chuẩn DNA Ladder 100 bp – 10 kb",
        "dimensions": "Bản gel Agarose 1% nhuộm Ethidium Bromide",
        "filename": "gel_electrophoresis.jpg",
        "grade_level": "Sinh 12 & AP Biology (Unit 6: Gene Expression & Biotech)",
        "description_vi": "Thí nghiệm cốt lõi trong đề thi AP/IB/THPTQG: các đoạn ADN mang điện tích âm di chuyển về cực dương trong điện trường; đoạn ngắn chạy nhanh và xa hơn đoạn dài, phát quang màu cam dưới đèn UV.",
        "key_structures": ["Thang chuẩn kích thước DNA Ladder", "Các vạch băng ADN sắc nét", "Cực âm Catot và cực dương Anot"],
        "storage_conditions": "Bản gel đọc ngay sau khi chạy 45 phút ở 100V",
        "safety_level": "Đeo kính chống tia cực tím UV và găng tay",
        "color": "#a855f7"
    },
    {
        "query": "Agar cube diffusion phenolphthalein surface area volume lab",
        "id": "specimen_agar_diffusion",
        "name_vi": "Thí Nghiệm Khuếch Tán Thạch Agar-Phenolphthalein (Tỉ lệ S/V)",
        "name_en": "Agar Cube Diffusion Surface Area to Volume Ratio Lab",
        "category": "biology",
        "type": "Mô hình khuếch tán & Giới hạn kích thước tế bào",
        "magnification": "Mắt thường & Thước kẹp mm",
        "dimensions": "3 khối lập phương cạnh 1 cm, 2 cm, 3 cm",
        "filename": "agar_diffusion.jpg",
        "grade_level": "Sinh 10 & AP Biology (Unit 2: Cell Size & Diffusion Limits)",
        "description_vi": "Thí nghiệm kinh điển chứng minh vì sao tế bào không thể quá lớn: ngâm các khối thạch chứa phenolphthalein vào NaOH, khối nhỏ nhất (S/V lớn nhất) có tỉ lệ phần trăm thể tích khuếch tán thấu suốt cao nhất.",
        "key_structures": ["Màu hồng thâm nhập từ ngoài vào trong", "Vùng lõi chưa khuếch tán", "Bề dày khuếch tán đồng nhất"],
        "storage_conditions": "Bảo quản thạch trong tủ mát 4°C trước khi cắt",
        "safety_level": "Dung dịch kiềm NaOH 0.1M ăn mòn nhẹ",
        "color": "#ec4899"
    },
    {
        "query": "Mitochondrion transmission electron microscope TEM cristae",
        "id": "specimen_mitochondria_tem",
        "name_vi": "Ty Thể Dưới Kính Hiển Vi Điện Tử Truyền Qua (TEM)",
        "name_en": "Mitochondrion Ultrastructure TEM Micrograph",
        "category": "biology",
        "type": "Bào quan hô hấp tế bào & Sản sinh ATP",
        "magnification": "50,000x – 100,000x (TEM)",
        "dimensions": "0.5 – 1.0 µm × 2 – 7 µm",
        "filename": "mitochondria_tem.jpg",
        "grade_level": "Sinh 10 & AP Biology (Unit 3: Cellular Energetics)",
        "description_vi": "Ảnh hiển vi điện tử truyền qua (TEM) siêu cấu trúc ty thể: thấy rõ màng kép, màng trong gấp nếp thành các mào (*cristae*) chứa chuỗi truyền electron hô hấp và chất nền chứa ADN ty thể vòng.",
        "key_structures": ["Màng ngoài trơn nhẵn", "Màng trong gấp nếp cristae tăng diện tích", "Chất nền matrix chứa enzyme chu trình Krebs"],
        "storage_conditions": "Lát cắt siêu mỏng cố định OsO4",
        "safety_level": "An toàn",
        "color": "#f59e0b"
    },
    {
        "query": "UV Vis spectrophotometer cuvette chemistry lab beer lambert",
        "id": "chem_spectrophotometer",
        "name_vi": "Máy Quang Phổ Hấp Thụ UV-Vis & Cuvet Đo (Beer-Lambert)",
        "name_en": "UV-Vis Spectrophotometer and Cuvette Setup",
        "category": "chemistry",
        "type": "Thiết bị phân tích quang phổ định lượng",
        "magnification": "Đo độ hấp thụ quang A từ 0.001 đến 3.000",
        "dimensions": "Cuvet thạch anh quang trình b = 1.00 cm",
        "filename": "spectrophotometer.jpg",
        "grade_level": "Hóa 11, Hóa 12 & AP Chemistry (Topic 3.13 Beer-Lambert Law)",
        "description_vi": "Thiết bị đo nồng độ dung dịch màu dựa trên định luật Beer-Lambert: A = ε·b·c. Chiếu chùm sáng đơn sắc qua cuvet chứa mẫu để đo cường độ ánh sáng truyền qua.",
        "key_structures": ["Cuvet thạch anh trong suốt 4 mặt", "Nguồn phát đèn Deuterium/Tungsten", "Bộ đơn sắc lăng kính/cách tử"],
        "storage_conditions": "Lau sạch cuvet bằng giấy quang học chuyên dụng",
        "safety_level": "An toàn",
        "color": "#38bdf8"
    },
    {
        "query": "Bomb calorimeter chemistry experiment heat of combustion",
        "id": "chem_calorimeter",
        "name_vi": "Nhiệt Lượng Kế Đo Enthalpy Nhiệt Phản Ứng (Calorimeter)",
        "name_en": "Laboratory Calorimeter Heat of Reaction Setup",
        "category": "chemistry",
        "type": "Thiết bị nhiệt động học hóa học",
        "magnification": "Đo biến thiên nhiệt độ ΔT chính xác 0.01°C",
        "dimensions": "Bình cách nhiệt chân không kèm que khuấy & nhiệt kế",
        "filename": "calorimeter_setup.jpg",
        "grade_level": "Hóa 10 (Nhiệt hóa học) & AP Chemistry (Unit 6: Thermodynamics)",
        "description_vi": "Dụng cụ xác định biến thiên Enthalpy phản ứng: q = m·C·ΔT. Cách ly nhiệt hoàn toàn với môi trường để đo chính xác lượng nhiệt tỏa ra hoặc thu vào của phản ứng.",
        "key_structures": ["Vỏ xốp cách nhiệt kép", "Cảm biến nhiệt độ điện tử phân giải cao", "Cần khuấy đều dung dịch"],
        "storage_conditions": "Lau khô bảo quản nơi khô ráo",
        "safety_level": "Cẩn thận phản ứng tỏa nhiệt mạnh",
        "color": "#ef4444"
    },
    {
        "query": "Digital storage oscilloscope waveform electronics physics lab",
        "id": "phys_oscilloscope",
        "name_vi": "Dao Động Ký Điện Tử Khảo Sát Tín Hiệu Sóng (Oscilloscope)",
        "name_en": "Digital Storage Oscilloscope Displaying Waveforms",
        "category": "physics",
        "type": "Thiết bị đo lường điện tử & Sóng điện từ",
        "magnification": "Băng thông 100 MHz, lấy mẫu 1 GSa/s",
        "dimensions": "Màn hình hiển thị điện áp theo thời gian (V-t)",
        "filename": "oscilloscope.jpg",
        "grade_level": "Vật lý 12 & AP Physics (Dao động điều hòa, Mạch RLC & Sóng)",
        "description_vi": "Thiết bị đo lường vạn năng trong phòng lab: hiển thị dạng sóng điện xoay chiều hình sin, đo chu kỳ T, tần số f, biên độ điện áp đỉnh U0 và độ lệch pha giữa u và i trong mạch RLC.",
        "key_structures": ["Màn hình lưới đồ thị Graticule chia vạch", "Đầu dò que đo Probe 10X", "Kênh đo kép CH1 & CH2 so sánh lệch pha"],
        "storage_conditions": "Tránh ẩm ướt và từ trường mạnh",
        "safety_level": "Cách điện an toàn",
        "color": "#10b981"
    }
]


def download_advanced():
    print("=== TẢI 6 THIẾT BỊ VÀ MẪU VẬT KHOA HỌC CHUYÊN SÂU (AP/IB/OLYMPIAD) ===")
    headers = {"User-Agent": "AISTEM-Master-Lab/1.0 (academic research; contact@aistem.edu)"}

    json_path = Path("/Volumes/SecondaryDisk/aistemx/data/lab_specimens.json")
    specimens = []
    if json_path.exists():
        try:
            specimens = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            specimens = []

    existing_ids = {s["id"] for s in specimens}

    for item in ADVANCED_EXAM_LABS:
        sid = item["id"]
        fname = item["filename"]
        target_path = PUBLIC_DIR / fname
        q = item["query"]

        if not target_path.exists() or target_path.stat().st_size < 1000:
            print(f"🔍 Đang tải ảnh thật cho [{item['name_vi']}]...")
            api_url = f"https://commons.wikimedia.org/w/api.php?action=query&format=json&generator=search&gsrnamespace=6&gsrlimit=1&gsrsearch={urllib.parse.quote(q)}&prop=imageinfo&iiprop=url"
            try:
                req = urllib.request.Request(api_url, headers=headers)
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    pages = data.get("query", {}).get("pages", {})
                    real_url = None
                    for _, pdata in pages.items():
                        real_url = pdata["imageinfo"][0]["url"]
                        break

                if real_url:
                    print(f"  ⬇ Lưu ảnh: {fname}...")
                    img_req = urllib.request.Request(real_url, headers=headers)
                    with urllib.request.urlopen(img_req, timeout=25) as img_resp:
                        target_path.write_bytes(img_resp.read())
                        print(f"  ✓ Đã lưu: {fname} ({target_path.stat().st_size/1024:.1f} KB)")
            except Exception as e:
                print(f"  ❌ Lỗi tải {fname}: {e}")

        spec_data = dict(item)
        del spec_data["query"]
        del spec_data["filename"]
        spec_data["local_image"] = f"/real_specimens/{fname}"

        if sid not in existing_ids:
            specimens.append(spec_data)
            existing_ids.add(sid)
        else:
            for i, ex in enumerate(specimens):
                if ex["id"] == sid:
                    specimens[i] = spec_data

        time.sleep(0.4)

    json_path.write_text(json.dumps(specimens, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n🎉 HOÀN TẤT ĐỒNG BỘ 100%! Toàn hệ thống hiện có chính xác: {len(specimens)} MẪU VẬT & THIẾT BỊ PHÒNG LAB.")


if __name__ == "__main__":
    download_advanced()
