"""Tầng ảnh raster (AI) cho các công thức khó vẽ bằng SVG.

SVG deterministic hợp với hình hình học/đồ thị; nhưng nhiều công thức có "vật thật" đi
kèm — con lắc, bình điện phân, lá cây quang hợp, phân bào — thì ảnh minh hoạ (AI sinh)
trực quan hơn. Module này: (1) danh sách ứng viên đã tuyển + mô tả cảnh, (2) sinh prompt
chuẩn để đưa vào model text-to-image.

Nguyên tắc prompt cho hình STEM:
  * cùng một "style suffix" cho cả bộ → nhìn đồng bộ;
  * KHÔNG để chữ/nhãn (model sinh chữ sai) → cảnh mô tả bằng hình, negative chặn text;
  * seed suy ra từ id → sinh lại tái lập được.

Engine thuần Python, không phụ thuộc backend. Việc gọi model nằm ở tools/gen_raster.py.
"""

from __future__ import annotations

import zlib

# Kiểu ảnh chung — giữ bộ ảnh đồng bộ, sạch, không chữ.
STYLE = ("clean modern educational science illustration, textbook diagram style, "
         "soft studio lighting, minimalist, plain white background, subtle shadows, "
         "clear composition, high detail, no text")
NEGATIVE = ("text, words, letters, labels, captions, numbers, watermark, signature, logo, "
            "blurry, low quality, jpeg artifacts, cluttered, deformed, extra limbs, ugly")
DEFAULT_MODEL = "@cf/black-forest-labs/flux-1-schnell"

# Ứng viên đã tuyển: mỗi mục là công thức + mô tả cảnh (tiếng Anh, tránh chữ trong ảnh).
CANDIDATES: list[dict] = [
    {"id": "physics.thpt.dao-dong-dieu-hoa.con-lac-don-chu-ki",
     "scene": "a simple pendulum: a small metal ball hanging from a thin string fixed to a "
              "horizontal support, swinging in an arc, motion arc shown as a faint dotted curve"},
    {"id": "physics.thpt.cam-ung-dien-tu.dinh-luat-faraday-cam-ung",
     "scene": "a bar magnet moving into a cylindrical copper wire coil connected to a galvanometer, "
              "magnetic field lines around the magnet, sense of motion"},
    {"id": "physics.thcs.quang-hoc.cong-thuc-thau-kinh",
     "scene": "a glass convex converging lens on an optical bench, an upright arrow object on the "
              "left and light rays passing through the lens converging to an inverted image on the right"},
    {"id": "physics.dai-hoc.nhiet-hoc.phuong-trinh-trang-thai-khi-li-tuong",
     "scene": "a transparent cylinder with a movable piston compressing an ideal gas shown as many "
              "small bouncing particles inside, thermometer feel, clean lab render"},
    {"id": "physics.thpt.dong-luc-hoc.dinh-luat-van-vat-hap-dan",
     "scene": "two spherical planets of different size in space attracting each other, a faint force "
              "arrow between their centers, starfield far background, dramatic lighting"},
    {"id": "physics.thpt.intl-hap-dan.kepler-dinh-luat-i",
     "scene": "a planet orbiting a bright star along a clear elliptical path, the star at one focus of "
              "the ellipse, orbit drawn as a smooth glowing ring, space background"},
    {"id": "chemistry.thpt.dien-hoa.dinh-luat-faraday",
     "scene": "an electrolysis apparatus: a glass beaker with blue electrolyte solution, two metal "
              "electrodes dipped in, wires going to a battery, gas bubbles rising on an electrode"},
    {"id": "biology.thcs.chuyen-hoa-thuc-vat.phuong-trinh-quang-hop",
     "scene": "photosynthesis in a green leaf under sunlight: sun rays hitting the leaf, water and "
              "carbon dioxide flowing in, oxygen bubbles and glucose forming, cross-section of a chloroplast"},
    {"id": "biology.dai-hoc.dong-hoc-enzyme.phuong-trinh-michaelis-menten",
     "scene": "enzyme and substrate lock-and-key model: a colorful enzyme protein with an active site "
              "pocket binding a small matching substrate molecule, 3d biochemistry render"},
    {"id": "biology.thpt.nhan-doi-adn.so-lien-ket-hidro-bi-pha-vo",
     "scene": "a DNA replication fork: a double helix unzipping into two strands with the twisted "
              "ladder structure and complementary bases, glossy 3d molecular render"},
    {"id": "biology.thpt.phan-bao.so-te-bao-con-sau-nguyen-phan",
     "scene": "stages of mitosis cell division shown as a row of round cells: chromosomes condensing, "
              "aligning at the middle, separating to poles, and one cell splitting into two"},
]


def seed_for(formula_id: str) -> int:
    """Seed ổn định suy từ id (để sinh lại ra ảnh gần như nhau)."""
    return zlib.crc32(formula_id.encode("utf-8")) & 0x7FFFFFFF


def build_prompt(candidate: dict, formula: dict | None = None,
                 model: str = DEFAULT_MODEL, width: int = 1024, height: int = 1024) -> dict:
    """Sinh bản ghi prompt đầy đủ cho một ứng viên."""
    scene = candidate["scene"]
    prompt = f"{scene}. {STYLE}."
    return {
        "formula_id": candidate["id"],
        "name_vi": (formula or {}).get("name_vi", ""),
        "subject": candidate["id"].split(".")[0],
        "model": model,
        "prompt": prompt,
        "negative_prompt": NEGATIVE,
        "width": width,
        "height": height,
        "seed": seed_for(candidate["id"]),
        "scene": scene,
    }
