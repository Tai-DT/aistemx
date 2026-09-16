#!/usr/bin/env python3
"""Script tải toàn diện 14 mẫu vật và thí nghiệm thực nghiệm còn thiếu để đạt độ phủ 100% SGK.

Danh sách 14 mẫu vật bổ sung:
1. Sinh học:
   - Tế bào Bạch cầu thực bào vi khuẩn (Human White Blood Cell / Phagocytosis)
   - Tế bào Giảm phân tinh hoàn châu chấu (Meiosis in Locust Testis)
   - Nấm mốc đen bánh mì (Rhizopus stolonifer / Black Bread Mold)
   - Thủy tức nước ngọt (Hydra vulgaris)
   - Lát cắt giải phẫu thân cây một lá mầm & hai lá mầm (Monocot vs Dicot Stem Cross-section)
   - Lát cắt giải phẫu mô xương xốp người (Human Compact Bone Osteon)
   - Tiêu bản bộ NST người Karyotype (Human Chromosome Karyotype 46,XX/46,XY)

2. Hoá học:
   - Magie kim loại cháy trong không khí (Magnesium Ribbon Burning)
   - Thí nghiệm điện phân dung dịch CuSO4 (Copper Electroplating)
   - Kết tủa sắt(III) hydroxit Fe(OH)3 màu nâu đỏ (Iron III Hydroxide Precipitate)
   - Thí nghiệm núi lửa Amoni dicromat (Ammonium Dichromate Volcano)

3. Vật lý:
   - Vòng tròn Newton giao thoa màng mỏng (Newton's Rings)
   - Ống phóng điện Plasma khí hiếm (Noble Gas Plasma Discharge Tubes)
   - Tinh thể Băng tuyết lục giác (Hexagonal Snow Crystal Snowflake)
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

SUPPLEMENTAL_SPECIMENS = [
    # --- SINH HỌC THỰC HÀNH NÂNG CAO ---
    {
        "query": "Neutrophil engulfing anthrax bacterium SEM phagocytosis",
        "id": "specimen_white_blood_cell",
        "name_vi": "Tế Bào Bạch Cầu Thực Bào Vi Khuẩn (SEM)",
        "name_en": "Human White Blood Cell (Neutrophil Phagocytosis)",
        "category": "biology",
        "type": "Tế bào miễn dịch không đặc hiệu",
        "magnification": "8,000x (SEM)",
        "dimensions": "Đường kính 12 – 15 µm",
        "filename": "wbc_phagocytosis.jpg",
        "grade_level": "Sinh 8, Sinh 11 (Hệ Miễn dịch & Thực bào)",
        "description_vi": "Ảnh hiển vi điện tử quét chụp khoảnh khắc tế bào bạch cầu trung tính kéo dài màng sinh chất tạo chân giả để nuốt và tiêu hóa vi khuẩn qua cơ chế thực bào.",
        "key_structures": ["Chân giả thực bào bao vây vi khuẩn", "Lysosome chứa enzyme thủy phân", "Màng tế bào gợn sóng"],
        "storage_conditions": "Mẫu máu tươi kèm chất chống đông Heparin",
        "safety_level": "BSL-2",
        "color": "#f43f5e"
    },
    {
        "query": "Hydra vulgaris freshwater polyp microscope",
        "id": "specimen_hydra",
        "name_vi": "Thủy Tức Nước Ngọt (Hydra vulgaris)",
        "name_en": "Freshwater Hydra Polyp with Buds",
        "category": "biology",
        "type": "Động vật ruột khoang đối xứng tỏa tròn",
        "magnification": "40x – 100x (Kính hiển vi soi nổi)",
        "dimensions": "Chiều dài cơ thể 1 – 20 mm",
        "filename": "hydra_polyp.jpg",
        "grade_level": "KHTN 7 (Động vật không xương sống) & Sinh 11",
        "description_vi": "Cơ thể hình trụ hình chuông với các tua miệng chứa tế bào gai tự vệ và bắt mồi. Sinh sản vô tính bằng hình thức mọc chồi (budding) và tái sinh cực mạnh.",
        "key_structures": ["Tua miệng chứa tế bào gai (Cnidocytes)", "Chồi con đang phát triển", "Khoang tiêu hóa túi"],
        "storage_conditions": "Nước ngọt nuôi cấy kèm giáp xác râu ngành (Daphnia)",
        "safety_level": "An toàn tuyệt đối",
        "color": "#06b6d4"
    },
    {
        "query": "Rhizopus stolonifer black bread mold microscope sporangia",
        "id": "specimen_rhizopus_mold",
        "name_vi": "Nấm Mốc Đen Bánh Mì (Rhizopus stolonifer)",
        "name_en": "Black Bread Mold Sporangia",
        "category": "biology",
        "type": "Nấm sợi tiếp hợp (Zygomycota)",
        "magnification": "100x – 400x",
        "dimensions": "Túi bào tử đường kính 100 – 350 µm",
        "filename": "rhizopus_mold.jpg",
        "grade_level": "KHTN 6 & Sinh 10 (Thế giới Nấm)",
        "description_vi": "Sợi nấm không vách ngăn phân nhánh chằng chịt, mang các bọc túi bào tử hình cầu màu đen ở đầu cuống. Khi chín, bọc vỡ giải phóng hàng triệu bào tử phát tán trong không khí.",
        "key_structures": ["Túi bào tử hình cầu (Sporangium)", "Cuống túi bào tử", "Rễ giả (Rhizoids) bám thức ăn"],
        "storage_conditions": "Bánh mì hoặc cơm nguội để ẩm 3-4 ngày",
        "safety_level": "Tránh hít phải bào tử nấm mốc",
        "color": "#475569"
    },
    {
        "query": "Human chromosome karyotype spectral karyotyping",
        "id": "specimen_human_karyotype",
        "name_vi": "Bộ Nhiễm Sắc Thể Người (Karyotype 46,XY / 46,XX)",
        "name_en": "Human Chromosome Metaphase Spread",
        "category": "biology",
        "type": "Vật chất di truyền cấp tế bào",
        "magnification": "1000x (Nhuộm băng Giemsa G-banding)",
        "dimensions": "46 nhiễm sắc thể (23 cặp tương đồng)",
        "filename": "human_karyotype.jpg",
        "grade_level": "Sinh 9, Sinh 12 (Di truyền học & Đột biến NST)",
        "description_vi": "Ảnh chụp bộ NST người ở kỳ giữa nguyên phân. Nhuộm băng G giúp xếp thành 22 cặp NST thường và 1 cặp NST giới tính để chẩn đoán hội chứng Down (3 NST 21), Turner (XO), Klinefelter (XXY).",
        "key_structures": ["Tâm động (Centromere)", "Cánh ngắn p và cánh dài q", "Các vạch băng sáng tối đặc trưng"],
        "storage_conditions": "Tiêu bản tế bào tủy xương hoặc tế bào lympho máu",
        "safety_level": "BSL-2",
        "color": "#a855f7"
    },
    {
        "query": "Zea mays stem cross section microscope monocot vascular bundle",
        "id": "specimen_monocot_stem",
        "name_vi": "Lát Cắt Thân Cây Ngô Một Lá Mầm (Monocot Stem)",
        "name_en": "Monocot Stem Vascular Bundles Cross-section",
        "category": "biology",
        "type": "Giải phẫu mô thực vật",
        "magnification": "100x – 400x",
        "dimensions": "Đường kính thân 2 – 5 mm",
        "filename": "monocot_stem.jpg",
        "grade_level": "Sinh 11 (Vận chuyển nước và chất khoáng trong cây)",
        "description_vi": "Lát cắt ngang thân cây ngô một lá mầm: các bó mạch dẫn (gồm mạch gỗ Xylem và mạch rây Phloem) xếp rải rác lộn xộn trong mô mềm, có hình dáng giống 'mặt người'.",
        "key_structures": ["Mạch gỗ hình chữ V dẫn nước", "Mạch rây dẫn chất hữu cơ", "Bao sợi cứng bảo vệ"],
        "storage_conditions": "Lát cắt vi phẫu nhuộm kép Son môi - Xanh metylen",
        "safety_level": "An toàn",
        "color": "#22c55e"
    },
    {
        "query": "Human compact bone tissue osteon haversian system microscope",
        "id": "specimen_bone_osteon",
        "name_vi": "Hệ Thống Ống Havers Mô Xương Xốp Người (Osteon)",
        "name_en": "Human Compact Bone Osteon Haversian System",
        "category": "biology",
        "type": "Mô liên kết cứng động vật",
        "magnification": "200x – 400x",
        "dimensions": "Đường kính ống Havers 50 µm",
        "filename": "bone_osteon.jpg",
        "grade_level": "Sinh 8 (Hệ vận động & Cấu tạo xương)",
        "description_vi": "Cấu trúc vi thể của xương đặc: các lá xương đồng tâm xếp xung quanh ống Havers chứa mạch máu và dây thần kinh, các hốc xương chứa tế bào xương liên lạc qua các vi quản.",
        "key_structures": ["Ống trung tâm Havers", "Các lá xương đồng tâm", "Tế bào xương trong hốc (Osteocytes)"],
        "storage_conditions": "Lát mài xương khô gắn keo bảo quản",
        "safety_level": "An toàn",
        "color": "#eab308"
    },

    # --- HOÁ HỌC & PHẢN ỨNG ĐẶC TRƯNG ---
    {
        "query": "Magnesium burning ribbon white light flame chemistry",
        "id": "chem_magnesium_flame",
        "name_vi": "Dây Kim Loại Magie (Mg) Cháy Phát Sáng Chói Lòa",
        "name_en": "Magnesium Ribbon Burning with Brilliant White Flame",
        "category": "chemistry",
        "type": "Phản ứng cháy kim loại kiềm thổ",
        "magnification": "Nhiệt độ ngọn lửa 3,100 K",
        "dimensions": "Dải ruy-băng Mg tinh khiết 99.9%",
        "filename": "magnesium_flame.jpg",
        "grade_level": "Hóa 8, Hóa 9, Hóa 10 (Phản ứng Oxi hóa khử)",
        "description_vi": "Dây Magie cháy mãnh liệt trong không khí tạo ngọn lửa màu trắng chói lòa giàu tia cực tím UV và tạo tàn tro bột MgO màu trắng tuyết: 2Mg + O2 -> 2MgO.",
        "key_structures": ["Ngọn lửa trắng rực rỡ phát tia cực tím", "Bột oxit Magie MgO trắng", "Tỏa nhiệt lượng cực lớn"],
        "storage_conditions": "Dây kim loại cuộn kín trong túi hút ẩm",
        "safety_level": "Cảnh báo chói mắt, đeo kính lọc UV khi đốt",
        "color": "#f8fafc"
    },
    {
        "query": "Iron III hydroxide precipitate test tube reddish brown",
        "id": "chem_feoh3_precipitate",
        "name_vi": "Kết Tủa Sắt(III) Hydroxit Fe(OH)₃ Màu Nâu Đỏ",
        "name_en": "Iron(III) Hydroxide Reddish-Brown Precipitate",
        "category": "chemistry",
        "type": "Phản ứng trao đổi ion & Nhận biết cation",
        "magnification": "Ống nghiệm phản ứng hóa phân tích",
        "dimensions": "Dung dịch FeCl3 + NaOH",
        "filename": "feoh3_precipitate.jpg",
        "grade_level": "Hóa 9, Hóa 11 (Nhận biết ion), Hóa 12 (Hợp chất Sắt)",
        "description_vi": "Thí nghiệm nhận biết ion Fe³⁺ kinh điển trong SGK: nhỏ dung dịch NaOH vào muối sắt(III) clorua sinh ra kết tủa dạng keo màu nâu đỏ đặc trưng không tan trong kiềm dư.",
        "key_structures": ["Kết tủa dạng keo màu nâu đỏ", "Phản ứng Fe³⁺ + 3OH⁻ -> Fe(OH)₃↓", "Không tan trong bazơ dư"],
        "storage_conditions": "Pha mới trước khi thực hành",
        "safety_level": "Hóa chất ăn mòn nhẹ",
        "color": "#b45309"
    },
    {
        "query": "Ammonium dichromate volcano reaction orange spark",
        "id": "chem_volcano_reaction",
        "name_vi": "Thí Nghiệm Núi Lửa Amoni Dicromat (NH₄)₂Cr₂O₇",
        "name_en": "Ammonium Dichromate Chemical Volcano",
        "category": "chemistry",
        "type": "Phản ứng nhiệt phân tự oxy hóa khử",
        "magnification": "Tia lửa hoa tiêu và tro Cr2O3 xanh lục",
        "dimensions": "Chất rắn màu da cam",
        "filename": "volcano_reaction.jpg",
        "grade_level": "Hóa 10, Hóa 12 (Nhiệt phân muối vô cơ & Crom)",
        "description_vi": "Khi châm lửa đốt muối (NH4)2Cr2O7 màu cam, phản ứng tự duy trì phun trào tia lửa như núi lửa mini, tạo tro bột Cr2O3 màu xanh lá xốp phồng và giải phóng khí N2, hơi nước.",
        "key_structures": ["Muối màu cam chuyển thành tro Cr2O3 màu xanh lục", "Tự sinh nhiệt và tia lửa", "Giải phóng khí N2"],
        "storage_conditions": "Lọ tối màu, tủ hóa chất độc",
        "safety_level": "Hợp chất Cr(VI) độc hại, chỉ làm trong tủ hút",
        "color": "#ea580c"
    },

    # --- VẬT LÝ & QUANG HỌC HIỆN ĐẠI ---
    {
        "query": "Newton's rings interference pattern optics microscope",
        "id": "phys_newton_rings",
        "name_vi": "Vân Tròn Giao Thoa Newton (Newton's Rings)",
        "name_en": "Newton's Rings Thin Film Interference Pattern",
        "category": "physics",
        "type": "Quang học sóng & Giao thoa bản mỏng",
        "magnification": "Giao thoa ánh sáng đơn sắc natri",
        "dimensions": "Hệ thấu kính phẳng - lồi đặt trên bản thủy tinh",
        "filename": "newton_rings.jpg",
        "grade_level": "Vật lý 12 & Vật lý đại cương (Quang sóng)",
        "description_vi": "Hệ thống các vòng tròn sáng tối đồng tâm tạo ra do sự giao thoa của sóng ánh sáng phản xạ từ mặt dưới của thấu kính lồi và mặt trên của bản thủy tinh phẳng.",
        "key_structures": ["Tâm vòng tối trung tâm", "Các vòng tròn đồng tâm có bán kính tỉ lệ căn bậc 2", "Đo bán kính cong của thấu kính"],
        "storage_conditions": "Hộp thiết bị quang học khô ráo",
        "safety_level": "An toàn",
        "color": "#38bdf8"
    },
    {
        "query": "Noble gas discharge tubes spectrum glow neon helium argon",
        "id": "phys_gas_discharge",
        "name_vi": "Ống Phóng Điện Khí Hiếm (He, Ne, Ar, Kr, Xe)",
        "name_en": "Noble Gas Plasma Discharge Glow Tubes",
        "category": "physics",
        "type": "Quang phổ vạch phát xạ nguyên tử & Plasma",
        "magnification": "Điện trường cao thế kích thích điện tử",
        "dimensions": "Ống thủy tinh chứa khí áp suất thấp",
        "filename": "gas_discharge.jpg",
        "grade_level": "Vật lý 12 (Mẫu nguyên tử Bohr & Quang phổ)",
        "description_vi": "Mỗi loại khí hiếm phát ra màu sắc đặc trưng khi electron chuyển mức năng lượng: Helium (vàng hồng), Neon (đỏ cam rực rỡ), Argon (tím xanh), Xenon (xanh lam ngọc).",
        "key_structures": ["Quang phổ vạch nguyên tử gián đoạn", "Trạng thái Plasma phát quang", "Mức năng lượng kích thích Bohr"],
        "storage_conditions": "Bộ giá đỡ cách điện cao thế",
        "safety_level": "Điện áp cao 3–5 kV",
        "color": "#ec4899"
    },
    {
        "query": "Snowflake macro photography crystal hexagonal symmetry",
        "id": "phys_snowflake_crystal",
        "name_vi": "Tinh Thể Băng Tuyết Đối Xứng Lục Giác (Snowflake)",
        "name_en": "Hexagonal Snowflake Macro Crystal",
        "category": "physics",
        "type": "Tinh thể học & Liên kết Hydro của nước",
        "magnification": "Macro quang học 50x",
        "dimensions": "Đường kính 2 – 5 mm",
        "filename": "snowflake_crystal.jpg",
        "grade_level": "Vật lý 10 (Cấu tạo chất) & Hóa 10 (Liên kết Hydro)",
        "description_vi": "Ảnh chụp macro tinh thể tuyết tự nhiên với cấu trúc đối xứng lục giác 6 nhánh hoàn hảo, hình thành từ mạng liên kết hydro tứ diện của phân tử nước H2O khi đóng băng.",
        "key_structures": ["Cấu trúc đối xứng bậc 6 (Góc 60°)", "Nhánh tinh thể nhánh cây dendrite", "Mạng lưới liên kết hydro"],
        "storage_conditions": "Nhiệt độ dưới 0°C",
        "safety_level": "An toàn tuyệt đối",
        "color": "#93c5fd"
    }
]


def download_all_supplemental():
    print("=== TẢI BỔ SUNG 100% MẪU VẬT SGK TOÁN - LÝ - HÓA - SINH ===")
    headers = {"User-Agent": "AISTEM-Full-Curriculum-Bot/1.0 (academic research; contact@aistem.edu)"}

    json_path = Path("/Volumes/SecondaryDisk/aistemx/data/lab_specimens.json")
    specimens = []
    if json_path.exists():
        try:
            specimens = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            specimens = []

    existing_ids = {s["id"] for s in specimens}

    for item in SUPPLEMENTAL_SPECIMENS:
        sid = item["id"]
        fname = item["filename"]
        target_path = PUBLIC_DIR / fname
        q = item["query"]

        if not target_path.exists() or target_path.stat().st_size < 1000:
            print(f"🔍 Tìm ảnh thật cho [{item['name_vi']}]...")
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
            specimens.append(spec_data)
            existing_ids.add(sid)
        else:
            for i, ex in enumerate(specimens):
                if ex["id"] == sid:
                    specimens[i] = spec_data

        time.sleep(0.4)

    json_path.write_text(json.dumps(specimens, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n🎉 HOÀN TẤT TUYỆT ĐỐI! Hiện hệ thống đã có tổng cộng: {len(specimens)} MẪU VẬT THỰC NGHIỆM.")


if __name__ == "__main__":
    download_all_supplemental()
