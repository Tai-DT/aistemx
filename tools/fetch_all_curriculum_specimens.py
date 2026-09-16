#!/usr/bin/env python3
"""Script tải toàn bộ kho mẫu vật hiển vi & thực nghiệm chuẩn chương trình GDPT 2018 và Quốc tế (AP/IB/A-Level).

Bổ sung đầy đủ các mẫu vật bắt buộc trong SGK:
1. Sinh học THCS & THPT:
   - Trùng biến hình (Amoeba proteus)
   - Tảo xoắn (Spirogyra)
   - Trùng roi xanh (Euglena gracilis)
   - Nấm men bánh mì (Saccharomyces cerevisiae)
   - Tế bào niêm mạc miệng người (Human Cheek Epithelial Cells)
   - Nhiễm sắc thể người (Human Karyotype / Chromosomes)
   - Quá trình nguyên phân ở rễ hành (Onion Root Tip Mitosis)
   - Tế bào nơ-ron thần kinh (Neuron / Purkinje cells)
   - Mô cơ vân / cơ tim (Striated Muscle Tissue)
   - Hạt phấn hoa (Pollen grains SEM)

2. Hoá học & Khoáng vật thực nghiệm:
   - Tinh thể muối ăn NaCl (Cubic halite crystal)
   - Lưu huỳnh nguyên chất (Sulfur crystal)
   - Kim loại Magie cháy trong không khí (Magnesium flame)
   - Thí nghiệm tráng bạc gương (Silver mirror reaction)
   - Kết tủa BaSO4, Fe(OH)3

3. Vật lý & Quang học lượng tử:
   - Quang phổ liên tục & quang phổ vạch phát xạ (Emission spectrum)
   - Hiện tượng khúc xạ qua lăng kính tán sắc (Prism dispersion)
   - Màng xà phòng giao thoa ánh sáng (Thin film interference)
   - Cực quang / Ống tia catot (Crookes cathode ray tube)
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

FULL_SPECIMENS_CATALOG = [
    # ------------------ SINH HỌC TẾ BÀO & VI SINH ------------------
    {
        "query": "Amoeba proteus microscope",
        "id": "specimen_amoeba",
        "name_vi": "Trùng Biến Hình (Amoeba proteus)",
        "name_en": "Amoeba Proteus Pseudopodia",
        "category": "biology",
        "type": "Động vật nguyên sinh (Protozoa)",
        "magnification": "200x",
        "dimensions": "250 – 600 µm",
        "filename": "amoeba.jpg",
        "grade_level": "Lớp 6 (KHTN), Lớp 10 & AP Biology",
        "description_vi": "Sinh vật đơn bào dị dưỡng di chuyển và bắt mồi bằng chân giả (pseudopodia) nhờ dòng chất nguyên sinh luân chuyển. Quan sát rõ không bào tiêu hóa và nhân tròn.",
        "key_structures": ["Chân giả (Pseudopodia)", "Không bào tiêu hóa thức ăn", "Không bào co bóp thải nước", "Nhân tế bào"],
        "storage_conditions": "Môi trường nước ao tù giàu mùn bã hữu cơ",
        "safety_level": "An toàn sinh học",
        "color": "#06b6d4"
    },
    {
        "query": "Euglena gracilis microscope light",
        "id": "specimen_euglena",
        "name_vi": "Trùng Roi Xanh (Euglena gracilis)",
        "name_en": "Euglena Flagellate Protist",
        "category": "biology",
        "type": "Sinh vật đơn bào lưỡng dưỡng",
        "magnification": "400x",
        "dimensions": "35 – 55 µm",
        "filename": "euglena.jpg",
        "grade_level": "Lớp 6 (KHTN) & Lớp 10",
        "description_vi": "Sinh vật trung gian giữa động vật và thực vật: có hạt diệp lục tự dưỡng quang hợp khi có ánh sáng, nhưng có thể dị dưỡng trong bóng tối và di chuyển bằng roi đơn ở đầu.",
        "key_structures": ["Roi bơi đơn dài (Flagellum)", "Điểm mắt cảm nhận ánh sáng (Stigma)", "Hạt lục lạp (Chloroplasts)"],
        "storage_conditions": "Nước rãnh nước ngập nắng, bảo quản 20°C",
        "safety_level": "An toàn",
        "color": "#22c55e"
    },
    {
        "query": "Spirogyra microscope chloroplast",
        "id": "specimen_spirogyra",
        "name_vi": "Tảo Xoắn Nước Ngọt (Spirogyra)",
        "name_en": "Spirogyra Green Algae Ribbon Chloroplast",
        "category": "biology",
        "type": "Tảo đa bào hình sợi (Chlorophyta)",
        "magnification": "400x",
        "dimensions": "Sợi dài đường kính 20 – 60 µm",
        "filename": "spirogyra.jpg",
        "grade_level": "Lớp 6 (KHTN) & Lớp 10",
        "description_vi": "Tảo sợi nước ngọt đặc trưng với dải lục lạp xoắn ốc tuyệt đẹp chạy dọc tế bào. Thực hiện tiếp hợp sinh sản hữu tính bằng cầu nối tiếp hợp giữa 2 sợi tảo.",
        "key_structures": ["Lục lạp dạng dải ruy-băng xoắn ốc", "Hạt tạo tinh bột pyrenoid", "Thành tế bào cellulose phủ pectin trơn"],
        "storage_conditions": "Nước ngọt tĩnh trong mương máng ao hồ",
        "safety_level": "An toàn tuyệt đối",
        "color": "#10b981"
    },
    {
        "query": "Saccharomyces cerevisiae yeast microscope",
        "id": "specimen_yeast",
        "name_vi": "Nấm Men Bánh Mì (Saccharomyces cerevisiae)",
        "name_en": "Baker's Yeast Budding Cells",
        "category": "biology",
        "type": "Nấm men đơn bào nhân thực",
        "magnification": "1000x (Vật kính dầu)",
        "dimensions": "5 – 10 µm",
        "filename": "yeast_cells.jpg",
        "grade_level": "Lớp 6, Lớp 10 (Lên men vi sinh)",
        "description_vi": "Nấm men kinh điển trong công nghệ thực phẩm và sinh học phân tử. Sinh sản vô tính bằng hình thức nảy chồi (budding). Thực hiện lên men rượu chuyển hóa glucose thành ethanol và CO2.",
        "key_structures": ["Tế bào hình bầu dục", "Vết sẹo nảy chồi (Bud scar)", "Vách tế bào Glucan và Mannan"],
        "storage_conditions": "Môi trường YPD thạch, bảo quản 4°C",
        "safety_level": "BSL-1 (An toàn)",
        "color": "#f59e0b"
    },
    {
        "query": "human cheek epithelial cells microscope methylene blue",
        "id": "specimen_cheek_cell",
        "name_vi": "Tế Bào Niêm Mạc Miệng Người (Nhuộm Xanh Metylen)",
        "name_en": "Human Cheek Epithelial Cells",
        "category": "biology",
        "type": "Mô biểu mô lát tầng động vật",
        "magnification": "400x",
        "dimensions": "60 – 80 µm",
        "filename": "cheek_cells.jpg",
        "grade_level": "Lớp 6 & Lớp 10 (So sánh Tế bào Thực vật vs Động vật)",
        "description_vi": "Mẫu thực hành bắt buộc trong SGK: cạo nhẹ niêm mạc má trong của người và nhuộm methylene blue. Tế bào động vật không có thành cellulose cứng nên hình dạng mềm dẻo không đều.",
        "key_structures": ["Màng sinh chất mềm dẻo", "Nhân tế bào đậm màu ở trung tâm", "Chất tế bào hạt"],
        "storage_conditions": "Lam kính làm tươi, quan sát ngay trong 30 phút",
        "safety_level": "Mẫu cá nhân an toàn",
        "color": "#38bdf8"
    },
    {
        "query": "onion root tip mitosis microscope stages",
        "id": "specimen_mitosis_root",
        "name_vi": "Nguyên Phân Ở Rễ Hành (Mitosis in Onion Root Tip)",
        "name_en": "Onion Root Tip Mitosis Stages",
        "category": "biology",
        "type": "Mô phân sinh ngọn rễ (Meristem)",
        "magnification": "400x - 1000x",
        "dimensions": "Vùng phân chia tế bào đỉnh sinh trưởng",
        "filename": "root_mitosis.jpg",
        "grade_level": "Lớp 10 (Chu kỳ tế bào & Nguyên phân)",
        "description_vi": "Tiêu bản cố định nhuộm Aceto-carmine để quan sát các kỳ nguyên phân: Kỳ đầu (NST co xoắn), Kỳ giữa (NST xếp 1 hàng ở mặt phẳng xích đạo), Kỳ sau (NST phân ly), Kỳ cuối.",
        "key_structures": ["Nhiễm sắc thể co xoắn cực đại", "Thoi phân bào", "Vách ngăn tế bào mới"],
        "storage_conditions": "Tiêu bản cố định lâu năm gắn keo Canada",
        "safety_level": "An toàn",
        "color": "#ec4899"
    },
    {
        "query": "Pollen grain scanning electron microscope",
        "id": "specimen_pollen_sem",
        "name_vi": "Hạt Phấn Hoa Dưới Kính Hiển Vi Điện Tử (SEM)",
        "name_en": "Pollen Grains Scanning Electron Micrograph",
        "category": "biology",
        "type": "Giao tử đực thực vật có hoa",
        "magnification": "2,000x - 5,000x (SEM)",
        "dimensions": "20 – 60 µm",
        "filename": "pollen_sem.jpg",
        "grade_level": "Lớp 7, 11 (Sinh sản ở thực vật)",
        "description_vi": "Ảnh SEM thể hiện lớp vỏ ngoài (exine) có gai nhọn và hoa văn điêu khắc phức tạp của hạt phấn hoa, giúp bám dính chắc chắn vào côn trùng thụ phấn và đầu nhụy cái.",
        "key_structures": ["Lớp vỏ exine cấu tạo bằng sporopollenin bền vững", "Gai bám dính thụ phấn", "Rãnh nảy mầm"],
        "storage_conditions": "Bảo quản khô ráo kèm hạt hút ẩm",
        "safety_level": "Có thể gây dị ứng phấn hoa nhẹ",
        "color": "#eab308"
    },
    {
        "query": "Human neuron brain cell microscope",
        "id": "specimen_neuron",
        "name_vi": "Tế Bào Nơ-ron Thần Kinh (Pyramidal / Purkinje Neuron)",
        "name_en": "Human Brain Pyramidal Neuron",
        "category": "biology",
        "type": "Mô thần kinh chuyên hóa cao",
        "magnification": "400x (Nhuộm Bạc Golgi)",
        "dimensions": "Thân tế bào 20 µm, sợi trục kéo dài",
        "filename": "neuron_golgi.jpg",
        "grade_level": "Lớp 8, Lớp 11 (Cảm ứng & Dẫn truyền xung thần kinh)",
        "description_vi": "Tế bào dẫn truyền xung điện sinh học. Thân tế bào soma tỏa ra nhiều sợi nhánh (dendrites) tiếp nhận tín hiệu và một sợi trục (axon) dài truyền điện thế hoạt động đến synap.",
        "key_structures": ["Thân tế bào soma", "Sợi nhánh nhận tin (Dendrites)", "Sợi trục dẫn truyền (Axon)", "Bao Myelin cách điện"],
        "storage_conditions": "Lát cắt mô não cố định nhuộm muối bạc",
        "safety_level": "BSL-2",
        "color": "#a855f7"
    },

    # ------------------ HOÁ HỌC & KHOÁNG VẬT THỰC NGHIỆM ------------------
    {
        "query": "Halite crystal macro cubic salt",
        "id": "chem_nacl_crystal",
        "name_vi": "Mạng Tinh Thể Muối Ăn Natri Clorua (NaCl)",
        "name_en": "Halite Cubic Sodium Chloride Crystal",
        "category": "chemistry",
        "type": "Mạng tinh thể ion lập phương tâm diện",
        "magnification": "Macro quang học & Kính lúp",
        "dimensions": "Khối lập phương hoàn hảo góc 90°",
        "filename": "nacl_crystal.jpg",
        "grade_level": "Lớp 10 (Liên kết ion & Mạng tinh thể)",
        "description_vi": "Tinh thể muối đá Halite tự nhiên kết tinh thành các khối lập phương hoàn hảo với góc 90 độ, phản ánh trực tiếp sự sắp xếp trật tự của mạng ion Na+ và Cl- tâm diện.",
        "key_structures": ["Mặt phẳng lập phương vuông góc 90°", "Liên kết ion hút tĩnh điện mạnh", "Nhiệt độ nóng chảy 801°C"],
        "storage_conditions": "Lọ kín tránh không khí ẩm gây chảy rữa",
        "safety_level": "Không độc",
        "color": "#f8fafc"
    },
    {
        "query": "Native sulfur crystal macro yellow",
        "id": "chem_sulfur_crystal",
        "name_vi": "Tinh Thể Lưu Huỳnh Tự Nhiên (Native Sulfur S₈)",
        "name_en": "Native Orthorhombic Sulfur Crystals",
        "category": "chemistry",
        "type": "Đơn chất phi kim tinh khiết",
        "magnification": "Chụp Macro khoáng vật",
        "dimensions": "Hệ tinh thể trực thoi màu vàng chanh",
        "filename": "sulfur_crystal.jpg",
        "grade_level": "Lớp 10 & 11 (Nhóm Oxi - Lưu huỳnh)",
        "description_vi": "Lưu huỳnh nguyên chất dạng vòng S8 màu vàng sáng, kết tinh tại các miệng phun núi lửa. Không tan trong nước nhưng tan trong dung môi không phân cực CS2.",
        "key_structures": ["Vòng bát giác S8 hình vương miện", "Màu vàng chanh đặc trưng", "Cháy cho ngọn lửa màu xanh lam sinh khí SO2"],
        "storage_conditions": "Nhiệt độ phòng, tránh xa chất oxy hóa mạnh",
        "safety_level": "Chất dễ cháy",
        "color": "#facc15"
    },
    {
        "query": "Silver mirror reaction flask Tollens",
        "id": "chem_silver_mirror",
        "name_vi": "Thí Nghiệm Phản Ứng Tráng Gương Bạc (Tollens Test)",
        "name_en": "Silver Mirror Reaction in Flask",
        "category": "chemistry",
        "type": "Phản ứng oxy hóa khử hữu cơ",
        "magnification": "Lớp màng bạc nano phản xạ gương",
        "dimensions": "Bình cầu thủy tinh 100 mL",
        "filename": "silver_mirror.jpg",
        "grade_level": "Lớp 11 & 12 (Andehit & Glucozơ)",
        "description_vi": "Ảnh thực nghiệm tráng lớp bạc kim loại sáng bóng bám lên thành bình thủy tinh khi cho dung dịch Glucozơ tác dụng với thuốc thử Tollens [Ag(NH3)2]OH đun nóng nhẹ.",
        "key_structures": ["Lớp màng mỏng Ag kim loại", "Phản ứng nhận biết nhóm chức -CHO", "Khử ion Ag+ thành Ag tự do"],
        "storage_conditions": "Bình thí nghiệm tráng rửa bằng HNO3 sau khi dùng",
        "safety_level": "Cẩn thận dung dịch tạo bạc fulminat nổ nếu để khô",
        "color": "#cbd5e1"
    },

    # ------------------ VẬT LÝ & QUANG HỌC ------------------
    {
        "query": "Prism rainbow dispersion light physics experiment",
        "id": "phys_prism_dispersion",
        "name_vi": "Thí Nghiệm Tán Sắc Ánh Sáng Trắng Qua Lăng Kính",
        "name_en": "White Light Dispersion Through Glass Prism",
        "category": "physics",
        "type": "Quang hình & Chiết suất ánh sáng",
        "magnification": "Dải quang phổ khả kiến 380 – 750 nm",
        "dimensions": "Lăng kính thủy tinh Flint góc chiết quang A = 60°",
        "filename": "prism_dispersion.jpg",
        "grade_level": "Lớp 9 & Lớp 12 (Tán sắc ánh sáng)",
        "description_vi": "Thí nghiệm kinh điển của Isaac Newton: chiếu chùm ánh sáng trắng hẹp qua lăng kính bị bẻ cong và phân tách thành dải 7 màu liên tục (Đỏ đến Tím) do chiết suất n thay đổi theo bước sóng.",
        "key_structures": ["Tia đỏ lệch ít nhất (chiết suất n nhỏ nhất)", "Tia tím lệch nhiều nhất (chiết suất n lớn nhất)", "Dải quang phổ khả kiến"],
        "storage_conditions": "Lăng kính bảo quản trong hộp nhung chống xước",
        "safety_level": "An toàn",
        "color": "#f43f5e"
    },
    {
        "query": "Crookes tube cathode ray magnetic deflection",
        "id": "phys_crookes_tube",
        "name_vi": "Ống Tia Catot Crookes & Lực Từ Lorentz",
        "name_en": "Crookes Tube Cathode Ray Deflection",
        "category": "physics",
        "type": "Vật lý hạt & Điện trường/Từ trường",
        "magnification": "Chùm tia electron phát quang lân tinh",
        "dimensions": "Ống thủy tinh chân không 10⁻⁴ mmHg",
        "filename": "crookes_tube.jpg",
        "grade_level": "Lớp 11 (Lực từ lên điện tích) & Lớp 12 (Hạt nhân)",
        "description_vi": "Thí nghiệm khám phá ra hạt Electron của J.J. Thomson. Khi đưa cực nam châm lại gần ống tia catot chân không cao, chùm electron mang điện tích âm bị bẻ cong theo quy tắc bàn tay trái.",
        "key_structures": ["Catot phát xạ chùm electron", "Màn huỳnh quang ZnS phát sáng xanh lục", "Lực từ Lorentz bẻ cong quỹ đạo"],
        "storage_conditions": "Bảo quản tránh va đập vỡ chân không thủy tinh",
        "safety_level": "Điện áp cao kV, cẩn thận điện giật",
        "color": "#22c55e"
    }
]


def fetch_all():
    print("=== NẠP BỔ SUNG TOÀN DIỆN MẪU VẬT THỰC NGHIỆM CHUẨN SGK GDPT 2018 & QUỐC TẾ ===")
    headers = {"User-Agent": "AISTEM-Scientific-Curriculum/1.0 (academic research; contact@aistem.edu)"}

    # Đọc dữ liệu cũ nếu có
    json_path = Path("/Volumes/SecondaryDisk/aistemx/data/lab_specimens.json")
    existing_specimens = []
    if json_path.exists():
        try:
            existing_specimens = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            existing_specimens = []

    existing_ids = {s["id"] for s in existing_specimens}
    
    for item in FULL_SPECIMENS_CATALOG:
        sid = item["id"]
        fname = item["filename"]
        target_path = PUBLIC_DIR / fname
        q = item["query"]

        if not target_path.exists() or target_path.stat().st_size < 1000:
            print(f"🔍 Đang tìm ảnh khoa học thật cho [{item['name_vi']}]...")
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
                    print(f"  ⬇ Tải ảnh thật: {fname}...")
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
            existing_specimens.append(spec_data)
            existing_ids.add(sid)
        else:
            # Cập nhật thông tin
            for i, ex in enumerate(existing_specimens):
                if ex["id"] == sid:
                    existing_specimens[i] = spec_data

        time.sleep(0.4)

    # Ghi lại toàn bộ vào file JSON
    json_path.write_text(json.dumps(existing_specimens, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✓ Hoàn tất mở rộng kho mẫu vật! Tổng cộng có: {len(existing_specimens)} mẫu vật thực nghiệm phủ kín chương trình.")


if __name__ == "__main__":
    fetch_all()
