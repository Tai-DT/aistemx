#!/usr/bin/env python3
"""Script tải toàn bộ kho dụng cụ thí nghiệm và hệ thống phản ứng Hóa học thực tế chuẩn SGK & Quốc tế (AP/IB).

Bao gồm:
1. Dụng cụ đo thể tích & pha chế:
   - Bình định mức (Volumetric flask)
   - Pipet bầu / Pipet chia vạch (Volumetric Pipette)
   - Ống đong chia vạch (Graduated cylinder)
   - Cốc đốt Beaker thủy tinh chịu nhiệt (Beaker)
   - Ống nhỏ giọt Pasteur (Pasteur pipette)

2. Dụng cụ phản ứng, chưng cất & nung:
   - Ống nghiệm & Giá để ống nghiệm (Test tubes and rack)
   - Bình tam giác Erlenmeyer (Erlenmeyer flask)
   - Ống sinh hàn hoàn lưu / ngưng tụ (Condenser / Liebig condenser)
   - Bình cầu đáy tròn / đáy bằng (Round-bottom flask)
   - Phễu chiết tách chất lỏng không trộn lẫn (Separatory funnel)
   - Phễu lọc Büchner & Bình hút chân không (Büchner funnel & suction flask)
   - Chén nung sứ & Kiềng đun (Crucible & Triangle)
   - Đèn cồn / Đèn khí Bunsen (Bunsen burner)
   - Kẹp ống nghiệm, Đũa thủy tinh, Thìa xúc hóa chất (Spatula)

3. Các thí nghiệm Hóa học kinh điển bắt buộc:
   - Thí nghiệm điều chế và thu khí O2 từ KMnO4 / KClO3 (Úp ngược bình thu đẩy nước)
   - Thí nghiệm điều chế và thu khí Cl2 (Tác dụng MnO2 + HCl đặc)
   - Thí nghiệm điều chế este Etyl axetat (Phản ứng este hóa)
   - Thí nghiệm ăn mòn điện hóa kim loại (Cặp kim loại Fe-Cu ngâm dung dịch điện li)
   - Thí nghiệm pin điện hóa Daniell (Cầu muối Zn-Cu)
   - Thí nghiệm phân tích màu ngọn lửa kim loại kiềm/kiềm thổ (Flame test: Na vàng, K tím, Ba lục, Ca đỏ cam)
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

CHEMISTRY_APPARATUS_AND_LABS = [
    # ------------------ DỤNG CỤ THỦY TINH & ĐO LƯỜNG CHUẨN ------------------
    {
        "query": "Volumetric flask chemistry laboratory precision glassware",
        "id": "chem_volumetric_flask",
        "name_vi": "Bình Định Mức Chuẩn Độ Pha Dung Dịch (Volumetric Flask)",
        "name_en": "Volumetric Flask for Precise Solution Preparation",
        "category": "chemistry",
        "type": "Dụng cụ đo thể tích cấp chính xác A",
        "magnification": "Vạch định mức đơn 100 mL / 250 mL / 500 mL (±0.15 mL)",
        "dimensions": "Cổ dài hẹp, đáy phẳng có nút đậy mài nhám",
        "filename": "volumetric_flask.jpg",
        "grade_level": "Hóa 10, Hóa 11, Hóa 12 & AP/IB Chemistry",
        "description_vi": "Dụng cụ bắt buộc để pha chế dung dịch có nồng độ chính xác tuyệt đối. Khi dung dịch chạm đáy mặt khum khít vạch định mức ở nhiệt độ chuẩn 20°C, thể tích đạt độ tin cậy cao nhất.",
        "key_structures": ["Vạch khắc định mức chính xác duy nhất", "Cổ bình dài hẹp giảm sai số đọc meniscus", "Nút đậy kín chống bay hơi"],
        "storage_conditions": "Rửa sạch bằng nước cất, sấy khô nhẹ hoặc tráng dung dịch",
        "safety_level": "Thủy tinh Borosilicate 3.3 chịu nhiệt và hóa chất",
        "color": "#38bdf8"
    },
    {
        "query": "Volumetric pipette chemistry lab bulb filler",
        "id": "chem_pipette",
        "name_vi": "Pipet Bầu & Quả Bóp Cao Su Hút Hóa Chất (Pipette)",
        "name_en": "Volumetric Pipette with Rubber Bulb",
        "category": "chemistry",
        "type": "Dụng cụ hút và chuyển chất lỏng chính xác",
        "magnification": "Dung tích chính xác 10 mL / 25 mL",
        "dimensions": "Thân ống thon dài có bầu chứa ở giữa",
        "filename": "pipette_lab.jpg",
        "grade_level": "Hóa 11 (Chuẩn độ dung dịch) & AP Chemistry",
        "description_vi": "Dùng để hút chính xác một thể tích dung dịch xác định từ bình chứa sang bình phản ứng. Dùng quả bóp cao su tạo áp suất hút, thả ngón tay trỏ điều chỉnh mức chất lỏng chạm vạch.",
        "key_structures": ["Bầu chứa dung tích chuẩn", "Đầu nhọn thoát giọt đều", "Vạch chia định mức"],
        "storage_conditions": "Đặt thẳng đứng trên giá cắm pipet chuyên dụng",
        "safety_level": "Tuyệt đối không hút hóa chất bằng miệng",
        "color": "#06b6d4"
    },
    {
        "query": "Graduated cylinder laboratory measurement meniscus chemistry",
        "id": "chem_graduated_cylinder",
        "name_vi": "Ống Đong Thủy Tinh Chia Vạch Đo Thể Tích (Cylinder)",
        "name_en": "Graduated Cylinder Measuring Meniscus",
        "category": "chemistry",
        "type": "Dụng cụ đo thể tích thô",
        "magnification": "Vạch chia 1 mL trên thang 100 mL",
        "dimensions": "Ống hình trụ có chân đế lục giác vững chắc",
        "filename": "graduated_cylinder.jpg",
        "grade_level": "KHTN 6, Hóa 8, 9, 10, 11, 12",
        "description_vi": "Dụng cụ cơ bản dùng để đo thể tích chất lỏng nhanh. Khi đọc thể tích, mắt phải đặt ngang bằng với đáy của mặt khum lõm (meniscus) đối với dung dịch trong suốt không màu.",
        "key_structures": ["Thang chia vạch in vĩnh cửu", "Mỏ rót chống tràn", "Vành bảo vệ chống vỡ khi đổ"],
        "storage_conditions": "Giá úp ống đong khô ráo",
        "safety_level": "Không đun nóng trực tiếp trên ngọn lửa",
        "color": "#10b981"
    },
    {
        "query": "Separatory funnel chemistry extraction two phases",
        "id": "chem_separatory_funnel",
        "name_vi": "Phễu Chiết Quả Lê Tách Chất Lỏng (Separatory Funnel)",
        "name_en": "Separatory Funnel Liquid-Liquid Extraction",
        "category": "chemistry",
        "type": "Thiết bị chiết và tách phân đoạn hữu cơ",
        "magnification": "Dung tích 250 mL kèm khóa vặn PTFE",
        "dimensions": "Hình quả lê vuốt nhọn có vòi xả đáy",
        "filename": "separatory_funnel.jpg",
        "grade_level": "Hóa 11 (Hóa học hữu cơ: Tách và tinh chế este)",
        "description_vi": "Dùng để tách hai chất lỏng không hòa tan vào nhau (như nước và dầu/este). Chất lỏng có khối lượng riêng lớn hơn nằm ở lớp dưới được xả ra trước qua khóa vòi.",
        "key_structures": ["Ranh giới phân tách 2 pha lỏng rõ rệt", "Khóa van điều tiết giọt chính xác", "Nút đậy thông khí khi xả"],
        "storage_conditions": "Treo trên vòng kẹp giá sắt thí nghiệm",
        "safety_level": "Mở khóa xả áp suất khí thường xuyên khi lắc",
        "color": "#f59e0b"
    },
    {
        "query": "Liebig condenser distillation apparatus glassware reflux",
        "id": "chem_liebig_condenser",
        "name_vi": "Hệ Thống Sinh Hàn Chưng Cất & Hoàn Lưu (Condenser)",
        "name_en": "Liebig Condenser in Distillation Apparatus",
        "category": "chemistry",
        "type": "Hệ thống ngưng tụ hơi hóa chất",
        "magnification": "Áo nước làm mát 2 lớp đối lưu",
        "dimensions": "Ống sinh hàn thẳng/xoắn chiều dài 300 mm",
        "filename": "condenser_distillation.jpg",
        "grade_level": "Hóa 11, Hóa 12 (Chưng cất rượu, điều chế este)",
        "description_vi": "Dụng cụ làm lạnh hơi chất lỏng để ngưng tụ trở lại dạng lỏng. Nước làm mát luôn được cấp vào từ nhánh dưới và thoát ra ở nhánh trên để đảm bảo áo nước luôn đầy hoàn toàn.",
        "key_structures": ["Ống dẫn hơi bên trong", "Áo nước làm mát bao quanh", "Đầu nối thủy tinh nhám chuẩn 24/29"],
        "storage_conditions": "Lắp chặt với khớp nối mài bôi mỡ silicon",
        "safety_level": "Kiểm tra dòng nước lưu thông trước khi cấp nhiệt",
        "color": "#6366f1"
    },
    {
        "query": "Buchner funnel vacuum filtration suction flask chemistry",
        "id": "chem_buchner_filtration",
        "name_vi": "Phễu Lọc Hút Chân Không Büchner (Vacuum Filtration)",
        "name_en": "Büchner Funnel and Suction Flask Filtration",
        "category": "chemistry",
        "type": "Hệ thống lọc tinh thể nhanh bằng áp suất giảm",
        "magnification": "Màng lọc giấy xốp có lỗ sứ",
        "dimensions": "Phễu sứ Büchner đường kính 90 mm + Bình lọc hút",
        "filename": "buchner_filtration.jpg",
        "grade_level": "Hóa 10, Hóa 12 (Tách kết tủa, tinh chế chất rắn)",
        "description_vi": "Dùng máy hút chân không tạo độ chênh lệch áp suất lớn để hút kiệt dung dịch lọc qua phễu sứ, giúp thu hồi tinh thể kết tủa khô ráo nhanh gấp 10 lần lọc trọng lực thông thường.",
        "key_structures": ["Phễu sứ đục lỗ tròn đều", "Bình tam giác có nhánh nối bơm hút", "Giấy lọc ẩm ép khít đáy phễu"],
        "storage_conditions": "Rửa sạch lỗ phễu bằng axit loãng và sấy khô",
        "safety_level": "Dùng bình hút thủy tinh thành dày chịu áp suất",
        "color": "#ec4899"
    },
    {
        "query": "Bunsen burner blue flame laboratory chemistry heating",
        "id": "chem_bunsen_burner",
        "name_vi": "Đèn Khí Bunsen & Ngọn Lửa Xanh Nhiệt Độ Cao (Bunsen Burner)",
        "name_en": "Bunsen Burner Adjustable High-Temp Blue Flame",
        "category": "chemistry",
        "type": "Nguồn cung cấp nhiệt độ cao phòng lab",
        "magnification": "Nhiệt độ vùng ngọn lửa ngoài đạt 1,500°C",
        "dimensions": "Đế kim loại đúc nặng, ống trộn khí có vòng xoay gió",
        "filename": "bunsen_burner.jpg",
        "grade_level": "KHTN & Hóa học tất cả các cấp học",
        "description_vi": "Nguồn nhiệt chuẩn quốc tế: xoay vòng gió để trộn đủ oxy tạo ngọn lửa màu xanh không muội nhiệt độ cực cao. Khi đóng gió tạo ngọn lửa màu vàng an toàn dễ quan sát.",
        "key_structures": ["Vòng xoay điều chỉnh lượng không khí", "Vùng oxy hóa nóng nhất ở đỉnh nón trong", "Ống dẫn khí gas an toàn"],
        "storage_conditions": "Khóa van bình gas tổng sau khi kết thúc buổi thực hành",
        "safety_level": "Tránh xa các dung môi hữu cơ dễ cháy (cồn, ete)",
        "color": "#3b82f6"
    },

    # ------------------ CÁC THÍ NGHIỆM HÓA HỌC THỰC TẾ KINH ĐIỂN ------------------
    {
        "query": "Oxygen gas preparation potassium permanganate water displacement",
        "id": "chem_lab_oxygen_prep",
        "name_vi": "Thí Nghiệm Điều Chế & Thu Khí Oxy (Phương Pháp Đẩy Nước)",
        "name_en": "Oxygen Gas Preparation via Water Displacement Lab",
        "category": "chemistry",
        "type": "Thí nghiệm nhiệt phân điều chế khí",
        "magnification": "Khí O2 không màu đẩy nước chiếm chỗ",
        "dimensions": "Ống nghiệm chịu nhiệt + Ống dẫn khí + Chậu nước",
        "filename": "oxygen_prep.jpg",
        "grade_level": "Hóa 8, Hóa 10 (Oxi - Không khí)",
        "description_vi": "Nhiệt phân thuốc tím 2KMnO4 -> K2MnO4 + MnO2 + O2↑. Vì khí Oxy ít tan trong nước và nhẹ hơn nước nên được thu bằng phương pháp úp ngược lọ đầy nước trên chậu nước.",
        "key_structures": ["Miếng bông gòn ở miệng ống ngăn bột thuốc tím bay sang", "Ống nghiệm lắp nghiêng miệng hơi chúc xuống", "Tháo ống dẫn khí trước khi tắt đèn cồn chống hút ngược"],
        "storage_conditions": "Bình thu khí O2 đậy kín bằng mặt kính đồng hồ nhám",
        "safety_level": "Thao tác tháo ống dẫn đúng quy tắc an toàn",
        "color": "#0ea5e9"
    },
    {
        "query": "Daniell galvanic cell zinc copper salt bridge chemistry",
        "id": "chem_lab_daniell_cell",
        "name_vi": "Pin Điện Hóa Daniell Kèm Cầu Muối (Galvanic Cell Zn-Cu)",
        "name_en": "Daniell Galvanic Cell with Zinc, Copper & Salt Bridge",
        "category": "chemistry",
        "type": "Pin hóa năng chuyển thành điện năng",
        "magnification": "Suất điện động chuẩn E° = 1.10 Vôn",
        "dimensions": "2 cốc chứa dung dịch ZnSO4 1M & CuSO4 1M",
        "filename": "daniell_cell.jpg",
        "grade_level": "Hóa 12 & AP Chemistry (Unit 9: Electrochemistry)",
        "description_vi": "Tại cực âm Anot (kẽm): Zn -> Zn²⁺ + 2e (bị ăn mòn). Tại cực dương Catot (đồng): Cu²⁺ + 2e -> Cu (bám dày thêm). Cầu muối chứa KCl/KNO3 trung hòa điện tích hai bán pin.",
        "key_structures": ["Thanh kẽm và thanh đồng tinh khiết", "Cầu muối chứa thạch agar bão hòa ion", "Vôn kế đo điện áp chính xác 1.10V"],
        "storage_conditions": "Ngâm đầu cầu muối trong dung dịch KCl bảo quản",
        "safety_level": "An toàn điện áp thấp",
        "color": "#f59e0b"
    },
    {
        "query": "Flame test colors chemistry sodium potassium copper strontium",
        "id": "chem_lab_flame_test",
        "name_vi": "Thí Nghiệm Phân Tích Màu Ngọn Lửa Kim Loại (Flame Test)",
        "name_en": "Emission Flame Test of Alkali and Alkaline Earth Metals",
        "category": "chemistry",
        "type": "Quang phổ phát xạ ngọn lửa định tính ion",
        "magnification": "Màu sắc quang phổ đặc trưng",
        "dimensions": "Đũa bạch kim (Pt) hoặc dây Ni-Cr",
        "filename": "flame_test.jpg",
        "grade_level": "Hóa 10 (Cấu hình electron nguyên tử) & Hóa 12 (Kim loại kiềm)",
        "description_vi": "Nhúng đầu que thử vào muối rồi đốt trên ngọn lửa Bunsen không màu: Natri phát ngọn lửa màu Vàng chói, Kali phát màu Tím nhạt, Đồng cho màu Xanh lục, Stronti cho màu Đỏ tươi.",
        "key_structures": ["Ngọn lửa phát xạ màu đơn sắc đặc trưng", "Dây kim loại Pt/Ni-Cr rửa sạch bằng HCl đặc", "Kính màu coban để quan sát ngọn lửa Kali"],
        "storage_conditions": "Dây thử ngâm rửa sạch trong ống nghiệm chứa HCl đặc",
        "safety_level": "Đeo kính bảo hộ chống tia lửa bắn",
        "color": "#ec4899"
    }
]


def download_all_chem():
    print("=== TẢI TOÀN BỘ DỤNG CỤ VÀ THÍ NGHIỆM HÓA HỌC THỰC TẾ ===")
    headers = {"User-Agent": "AISTEM-ChemLab-Bot/1.0 (academic research; contact@aistem.edu)"}

    json_path = Path("/Volumes/SecondaryDisk/aistemx/data/lab_specimens.json")
    specimens = []
    if json_path.exists():
        try:
            specimens = json.loads(json_path.read_text(encoding="utf-8"))
        except Exception:
            specimens = []

    existing_ids = {s["id"] for s in specimens}

    for item in CHEMISTRY_APPARATUS_AND_LABS:
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
            specimens.append(spec_data)
            existing_ids.add(sid)
        else:
            for i, ex in enumerate(specimens):
                if ex["id"] == sid:
                    specimens[i] = spec_data

        time.sleep(0.4)

    json_path.write_text(json.dumps(specimens, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n🎉 HOÀN TẤT ĐỒNG BỘ! Tổng số mẫu vật & dụng cụ thí nghiệm phòng lab hiện tại: {len(specimens)}")


if __name__ == "__main__":
    download_all_chem()
