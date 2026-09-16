#!/usr/bin/env python3
"""Script tải ảnh kính hiển vi điện tử (SEM/TEM), ảnh quang học và dụng cụ thí nghiệm thực tế từ Wikimedia API."""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

PUBLIC_DIR = Path("/Volumes/SecondaryDisk/aistemx/frontend/public/real_specimens")
PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

# Danh sách bài báo & file Wikimedia chính thức
WIKI_FILES = [
    {
        "wiki_title": "File:Escherichia coli (SEM).jpg",
        "id": "specimen_ecoli",
        "name_vi": "Vi Khuẩn E. coli (Kính hiển vi điện tử quét SEM)",
        "name_en": "Escherichia coli Scanning Electron Micrograph",
        "category": "biology",
        "type": "Tế bào nhân sơ (Prokaryote)",
        "magnification": "10,000x (SEM)",
        "dimensions": "0.5 µm × 2.0 µm",
        "filename": "ecoli_sem.jpg",
        "description_vi": "Ảnh chụp kính hiển vi điện tử quét (SEM) phân giải cao của trực khuẩn E. coli. Quan sát rõ cấu trúc thành tế bào Gram âm và hình thái thể que.",
        "key_structures": ["Thành tế bào Peptidoglycan Gram âm", "Thể que vi khuẩn", "Vùng nhân ADN vòng đơn"],
        "storage_conditions": "Môi trường LB lỏng, bảo quản ở -80°C",
        "safety_level": "BSL-1 (Chủng phòng thí nghiệm)",
        "color": "#10b981"
    },
    {
        "wiki_title": "File:Red Blood Cell.jpg",
        "id": "specimen_human_rbc",
        "name_vi": "Tế Bào Hồng Cầu Người (SEM Micrograph)",
        "name_en": "Human Red Blood Cells",
        "category": "biology",
        "type": "Tế bào máu chuyên hóa",
        "magnification": "4,000x (SEM)",
        "dimensions": "Đường kính 7.5 µm, bề dày 2.0 µm",
        "filename": "human_rbc_sem.jpg",
        "description_vi": "Ảnh hiển vi điện tử quét chụp hình thái đĩa lõm 2 mặt của hồng cầu người. Cấu trúc lõm tăng tối đa diện tích tiếp xúc để trao đổi khí Oxy và CO2.",
        "key_structures": ["Dạng đĩa lõm 2 mặt biconcave", "Màng hồng cầu linh hoạt", "Phức hệ Hemoglobin chứa Fe²⁺"],
        "storage_conditions": "Dung dịch muối đẳng trương NaCl 0.9% hoặc 4°C",
        "safety_level": "BSL-2 (Mẫu máu người y tế)",
        "color": "#ef4444"
    },
    {
        "wiki_title": "File:Onion cells 2.jpg",
        "id": "specimen_onion_cell",
        "name_vi": "Tế Bào Biểu Bì Củ Hành Tây (Nhuộm màu 400x)",
        "name_en": "Onion Epidermal Cells Stained",
        "category": "biology",
        "type": "Tế bào thực vật (Plant Cell)",
        "magnification": "400x (Kính hiển vi quang học)",
        "dimensions": "200 µm × 70 µm",
        "filename": "onion_cells.jpg",
        "description_vi": "Ảnh chụp thị kính hiển vi quang học mẫu tế bào vảy hành tây. Ranh giới vách tế bào Cellulose xếp khít nhau như tổ ong, thấy rõ nhân tế bào hình tròn đậm màu.",
        "key_structures": ["Thành tế bào Cellulose cứng", "Nhân tế bào đậm màu", "Không bào trung tâm lớn"],
        "storage_conditions": "Lam kính tươi nhỏ giọt dung dịch Lugol",
        "safety_level": "An toàn tuyệt đối",
        "color": "#a855f7"
    },
    {
        "wiki_title": "File:Stomata under a microscope.jpg",
        "id": "specimen_stomata",
        "name_vi": "Khí Khổng & Lục Lạp Mặt Dưới Lá Cây",
        "name_en": "Leaf Stomata and Chloroplasts",
        "category": "biology",
        "type": "Cơ quan thoát hơi nước & Quang hợp",
        "magnification": "500x",
        "dimensions": "Khe mở 5–15 µm",
        "filename": "stomata_micrograph.jpg",
        "description_vi": "Ảnh hiển vi chụp cặp tế bào hình hạt đậu bao bọc lỗ khí khổng. Bên trong chứa nhiều hạt lục lạp xanh quang hợp.",
        "key_structures": ["Cặp tế bào bảo vệ hình hạt đậu", "Hạt lục lạp chứa chlorophyll", "Khe thoát khí khổng"],
        "storage_conditions": "Bóc biểu bì lá lẻ bạn / thài lài tía tươi",
        "safety_level": "An toàn",
        "color": "#22c55e"
    },
    {
        "wiki_title": "File:Copper(II) sulfate pentahydrate crystal.jpg",
        "id": "chem_cuso4_crystal",
        "name_vi": "Tinh Thể Đồng(II) Sunfat Ngậm Nước (CuSO₄·5H₂O)",
        "name_en": "Copper(II) Sulfate Pentahydrate Crystals",
        "category": "chemistry",
        "type": "Tinh thể khoáng vô cơ",
        "magnification": "Chụp Macro tinh thể quang học",
        "dimensions": "Hệ tinh thể tam tà đơn sắc",
        "filename": "cuso4_crystal.jpg",
        "description_vi": "Ảnh chụp macro tinh thể CuSO4·5H2O màu xanh lam sapphire nuôi cấy từ dung dịch bão hòa. Khi nung nóng mất nước chuyển thành bột CuSO4 khan màu trắng tinh.",
        "key_structures": ["Mặt phẳng tinh thể tam tà", "Màu xanh do ion [Cu(H2O)6]2+", "Dễ tan trong nước"],
        "storage_conditions": "Lọ thủy tinh nắp kín, tránh nơi khô nóng",
        "safety_level": "Gây kích ứng mắt, độc nếu nuốt phải",
        "color": "#38bdf8"
    },
    {
        "wiki_title": "File:Titration.jpg",
        "id": "chem_titration_apparatus",
        "name_vi": "Bộ Dụng Cụ Chuẩn Độ Axit - Bazơ & Buret",
        "name_en": "Laboratory Acid-Base Titration Setup",
        "category": "chemistry",
        "type": "Dụng cụ phân tích thể tích chuẩn",
        "magnification": "Thang đo chia vạch 0.1 mL",
        "dimensions": "Buret 50 mL kèm khóa PTFE, Bình tam giác Erlenmeyer",
        "filename": "titration_setup.jpg",
        "description_vi": "Ảnh chụp thực tế quá trình chuẩn độ axit clohiđric bằng dung dịch chuẩn NaOH với chỉ thị Phenolphthalein.",
        "key_structures": ["Buret thủy tinh borosilicate chia vạch", "Khóa buret chống rò rỉ", "Bình nón Erlenmeyer khuấy từ"],
        "storage_conditions": "Rửa sạch bằng nước cất, tráng bằng dung dịch cần đo",
        "safety_level": "Đeo kính bảo hộ, găng tay chống axit/kiềm",
        "color": "#ec4899"
    },
    {
        "wiki_title": "File:Bi-crystal.jpg",
        "id": "chem_bismuth_crystal",
        "name_vi": "Tinh Thể Kim Loại Bismut (Bi) Tinh Khiết",
        "name_en": "Synthetic Bismuth Hopper Crystal",
        "category": "chemistry",
        "type": "Kim loại chuyển tiếp cầu vồng",
        "magnification": "Chụp Macro quang học",
        "dimensions": "Cấu trúc bậc thang 99.99% Bi",
        "filename": "bismuth_crystal.jpg",
        "description_vi": "Ảnh chụp tinh thể Bismut với màng oxit bề mặt giao thoa ánh sáng tạo nên hiệu ứng màu sắc cầu vồng óng ánh.",
        "key_structures": ["Mạng tinh thể bậc thang hopper", "Lớp màng oxit giao thoa mỏng", "Kim loại nghịch từ"],
        "storage_conditions": "Nhiệt độ phòng, tránh va đập mạnh",
        "safety_level": "Kim loại nặng không độc hại",
        "color": "#f59e0b"
    },
    {
        "wiki_title": "File:Double slit pattern from green laser pointer.jpg",
        "id": "phys_double_slit_laser",
        "name_vi": "Hình Ảnh Thực Tế Giao Thoa Laser Khe Young",
        "name_en": "Laser Double Slit Diffraction Pattern",
        "category": "physics",
        "type": "Thí nghiệm giao thoa sóng ánh sáng",
        "magnification": "Quang ảnh thực nghiệm laser 532 nm",
        "dimensions": "Khoảng cách khe d = 0.25 mm",
        "filename": "double_slit_laser.jpg",
        "description_vi": "Ảnh chụp thực tế màn hứng vân giao thoa khi chiếu tia laser xanh qua 2 khe hẹp song song. Thấy rõ các vạch sáng tối xen kẽ.",
        "key_structures": ["Vân sáng trung tâm cực đại k=0", "Các vân tối xen kẽ đối xứng", "Vùng nhiễu xạ bao ngoài"],
        "storage_conditions": "Phòng tối quang học, tránh rung chấn",
        "safety_level": "Laser Class 2 (Không rọi vào mắt)",
        "color": "#10b981"
    },
    {
        "wiki_title": "File:Ferrofluid in magnetic field.jpg",
        "id": "phys_ferrofluid",
        "name_vi": "Nước Từ Ferrofluid Trong Từ Trường Nam Châm",
        "name_en": "Ferrofluid Spikes in Magnetic Field",
        "category": "physics",
        "type": "Chất lỏng từ tính nano",
        "magnification": "Gai từ trường chiều cao 5–15 mm",
        "dimensions": "Hạt nano Fe3O4 kích thước 10 nm",
        "filename": "ferrofluid_magnetic.jpg",
        "description_vi": "Ảnh chụp các gai nhọn tự tổ chức của chất lỏng từ tính (ferrofluid) khi đặt gần cực nam châm Neodymium.",
        "key_structures": ["Gai nhọn định hướng theo đường sức từ", "Huyền phù hạt nano từ tính", "Chất hoạt động bề mặt chống vón cục"],
        "storage_conditions": "Lọ thủy tinh chứa dung môi dầu khoáng",
        "safety_level": "Chất lỏng nhuộm đen da, khó rửa",
        "color": "#8b5cf6"
    }
]


def fetch_and_save():
    print("=== TẢI ẢNH MẪU VẬT HIỂN VI THẬT TỪ WIKIMEDIA COMMONS ===")
    headers = {
        "User-Agent": "AISTEM-Educational-Real-Specimens/1.0 (academic research; mailto:contact@aistem.edu)"
    }

    results = []
    for item in WIKI_FILES:
        title = item["wiki_title"]
        fname = item["filename"]
        target_file = PUBLIC_DIR / fname

        print(f"🔍 Đang truy vấn URL gốc cho: {item['name_vi']}...")
        api_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(title)}&prop=imageinfo&iiprop=url&format=json"

        try:
            req = urllib.request.Request(api_url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                pages = data.get("query", {}).get("pages", {})
                real_url = None
                for _, pdata in pages.items():
                    info_list = pdata.get("imageinfo", [])
                    if info_list:
                        real_url = info_list[0].get("url")
                        break

            if real_url:
                print(f"  ⬇ Đang tải file thật: {fname}...")
                img_req = urllib.request.Request(real_url, headers=headers)
                with urllib.request.urlopen(img_req, timeout=25) as img_resp:
                    target_file.write_bytes(img_resp.read())
                    print(f"  ✓ Đã lưu thành công: {fname} ({target_file.stat().st_size/1024:.1f} KB)")
            else:
                print(f"  ⚠ Không tìm thấy URL cho {title}")
        except Exception as e:
            print(f"  ❌ Lỗi tải {fname}: {e}")

        spec_item = dict(item)
        del spec_item["wiki_title"]
        del spec_item["filename"]
        spec_item["local_image"] = f"/real_specimens/{fname}"
        results.append(spec_item)
        time.sleep(0.5)

    # Lưu vào data/lab_specimens.json
    out_json = Path("/Volumes/SecondaryDisk/aistemx/data/lab_specimens.json")
    out_json.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✓ Hoàn tất nạp cơ sở dữ liệu mẫu vật & ảnh thực tế: {out_json}")


if __name__ == "__main__":
    fetch_and_save()
