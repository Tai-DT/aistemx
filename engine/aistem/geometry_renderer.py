"""Bộ giải mã và vẽ hình học / sơ đồ toán lý hóa chuẩn xác 100% cho AISTEM X.

Tận dụng 193 Geometry & Diagram Engines chuyên sâu của hệ thống AISTEM để vẽ hình học
phẳng, hình không gian, đồ thị giải tích, vectơ và vật lý học đường chuẩn xác từng toạ độ.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from tools.illus.registry import all_generators, render as render_illus
except ImportError:
    render_illus = None
    all_generators = lambda: {}


def _clean_text(text: str) -> str:
    """Chuẩn hóa văn bản: chữ thường, chuẩn hóa khoảng trắng."""
    t = text.lower().strip()
    t = re.sub(r"[\s_]+", " ", t)
    return t


def match_geometry_intent(prompt: str) -> tuple[Optional[str], dict[str, Any]]:
    """Phân tích ý định vẽ hình và chọn Engine trong 193 Generators phù hợp nhất."""
    p = _clean_text(prompt)

    # 1. HÌNH HỌC KHÔNG GIAN 3D (Ưu tiên cao hơn hình phẳng để tránh nhầm lăng trụ tam giác -> tam giác)
    if any(k in p for k in ["tứ diện", "tu dien"]):
        return "tetrahedron3d", {}

    if any(k in p for k in ["chóp cụt", "chop cut"]):
        return "pyramid_frustum3d", {}

    if any(k in p for k in ["hình chóp", "hinh chop", "chóp s.abcd", "chóp s.abc", "khối chóp"]):
        return "pyramid3d", {}

    if any(k in p for k in ["lăng trụ", "lang tru", "khối lăng trụ"]):
        return "prism3d", {}

    if any(k in p for k in ["lập phương", "lap phuong", "khối lập phương"]):
        return "cube3d", {}

    if any(k in p for k in ["hình hộp", "hinh hop"]):
        return "box3d", {}

    if any(k in p for k in ["nón cụt", "non cut"]):
        return "cone_frustum3d", {}

    if any(k in p for k in ["hình nón", "hinh non", "khối nón", "mặt nón"]):
        return "cone3d", {}

    if any(k in p for k in ["hình trụ", "hinh tru", "khối trụ", "mặt trụ"]):
        return "cylinder3d", {}

    if any(k in p for k in ["mặt cầu", "mat cau", "hình cầu", "hinh cau", "khối cầu"]):
        return "sphere3d", {}

    # Hệ toạ độ Oxyz
    if any(k in p for k in ["oxyz", "không gian oxyz"]):
        if any(k in p for k in ["mặt phẳng", "mat phang"]):
            return "oxyz_plane", {}
        if any(k in p for k in ["đường thẳng", "duong thang"]):
            return "oxyz_line", {}
        if any(k in p for k in ["vectơ", "vector"]):
            return "oxyz_vectors", {}
        return "oxyz_coords", {}

    # 2. VẬT LÝ HỌC ĐƯỜNG (Ưu tiên trước đồ thị tổng quát)
    if any(k in p for k in ["con lắc đơn", "con lac don"]):
        return "simple_pendulum", {}

    if any(k in p for k in ["con lắc lò xo thẳng đứng", "lò xo thẳng đứng"]):
        return "spring_vertical", {}

    if any(k in p for k in ["con lắc lò xo", "con lac lo xo", "lò xo"]):
        return "spring_horizontal", {}

    if any(k in p for k in ["ném xiên", "nem xien", "ném ngang"]):
        return "projectile", {}

    if any(k in p for k in ["rơi tự do", "roi tu do"]):
        return "free_fall", {}

    if any(k in p for k in ["sóng dừng", "song dung"]):
        return "standing_wave", {}

    if any(k in p for k in ["giao thoa sóng", "giao thoa ánh sáng", "khe young", "khe yng"]):
        return "young_interference", {}

    if any(k in p for k in ["sóng cơ", "song co", "truyền sóng"]):
        return "wave_snapshot", {}

    if any(k in p for k in ["mạch rlc", "xoay chiều rlc", "mạch điện xoay chiều"]):
        return "circuit_rlc", {}

    if any(k in p for k in ["mạch nối tiếp"]):
        return "circuit_series", {}

    if any(k in p for k in ["mạch song song"]):
        return "circuit_parallel", {}

    if any(k in p for k in ["coulomb", "cu-lông", "hai điện tích"]):
        return "coulomb_two_charges", {}

    if any(k in p for k in ["phản xạ ánh sáng", "gương phẳng"]):
        return "reflection_law", {}

    if any(k in p for k in ["khúc xạ ánh sáng", "lăng kính"]):
        return "refraction", {}

    if any(k in p for k in ["carnot", "chu trình carnot"]):
        return "carnot_cycle", {}

    if any(k in p for k in ["đồ thị p-v", "đồ thị pv", "khí lí tưởng"]):
        return "pv_diagram", {}

    # 3. TAM GIÁC VUÔNG & HỆ THỨC LƯỢNG
    has_tam_giac = any(k in p for k in ["tam giác", "tam giac", "tg ", "tg."]) or bool(re.search(r"\babc\b", p))
    has_vuong = any(k in p for k in ["vuông", "vuong", "vuông tại", "vuong tai"])
    has_duong_cao = bool(re.search(r"(\bđường\s*cao\b|\bduong\s*cao\b|\bđg\s*cao\b|\bah\b|\bh\b|vuông\s*góc|⊥)", p))
    has_trung_tuyen = bool(re.search(r"(\btrung\s*tuyến\b|\btrung\s*tuyen\b|\bam\b)", p))

    if (has_tam_giac and has_vuong) or "pytago" in p or "pythagore" in p or "hệ thức lượng" in p or "he thuc luong" in p:
        nums = [float(n) for n in re.findall(r"\b\d+(?:\.\d+)?\b", p)]
        params: dict[str, Any] = {"b": 4, "c": 3}
        if len(nums) >= 2:
            params["c"] = min(nums[0], nums[1])
            params["b"] = max(nums[0], nums[1])

        if has_trung_tuyen:
            params["mode"] = "trung-tuyen"
            return "right_triangle_altitude", params
        if has_duong_cao or "hệ thức lượng" in p or "he thuc luong" in p or "đường cao" in p:
            params["mode"] = "he-thuc"
            return "right_triangle_altitude", params
        return "right_triangle", params

    # 4. CÁC LOẠI TAM GIÁC KHÁC
    if any(k in p for k in ["tam giác đều", "tam giac deu", "tg đều", "tg deu"]):
        return "equilateral_triangle", {}

    if any(k in p for k in ["ngoại tiếp", "ngoai tiep"]) and (has_tam_giac or "đường tròn" in p):
        return "triangle_circumcircle", {}

    if any(k in p for k in ["nội tiếp", "noi tiep"]) and (has_tam_giac or "đường tròn" in p):
        if any(k in p for k in ["tứ giác", "tu giac"]):
            return "cyclic_quad", {}
        return "triangle_incircle", {}

    if any(k in p for k in ["trọng tâm", "trực tâm", "trong tam", "truc tam", "tâm đường tròn", "đồng quy"]):
        return "triangle_centers", {}

    if any(k in p for k in ["thales", "talet", "ta-lét", "định lí ta lét", "định lý talet"]):
        return "thales", {}

    if has_tam_giac and (has_duong_cao or has_trung_tuyen or "phân giác" in p or "phan giac" in p):
        return "triangle_cevian", {}

    if has_tam_giac:
        return "triangle_labeled", {}

    # 5. TỨ GIÁC & ĐA GIÁC PHẲNG
    if any(k in p for k in ["tứ giác nội tiếp", "tu giac noi tiep"]):
        return "cyclic_quad", {}

    if any(k in p for k in ["hình thang", "hinh thang"]):
        if any(k in p for k in ["đường trung bình", "duong trung binh", "trung bình", "trung binh"]):
            return "trapezoid_midline", {}
        return "trapezoid", {}

    if any(k in p for k in ["hình thoi", "hinh thoi"]):
        return "rhombus", {}

    if any(k in p for k in ["hình bình hành", "hinh binh hanh"]):
        return "parallelogram", {}

    if any(k in p for k in ["hình chữ nhật", "hinh chu nhat"]):
        return "rectangle", {}

    if any(k in p for k in ["hình vuông", "hinh vuong"]):
        return "square", {}

    if any(k in p for k in ["lục giác", "luc giac"]):
        return "regular_polygon", {"n": 6}

    if any(k in p for k in ["ngũ giác", "ngu giac"]):
        return "regular_polygon", {"n": 5}

    if any(k in p for k in ["bát giác", "bat giac"]):
        return "regular_polygon", {"n": 8}

    if any(k in p for k in ["đa giác đều", "da giac deu"]):
        return "regular_polygon", {"n": 6}

    # 6. ĐƯỜNG TRÒN & CUNG TRÒN
    if any(k in p for k in ["tiếp tuyến", "tiep tuyen", "tiếp xúc đường tròn"]):
        return "circle_tangent", {}

    if any(k in p for k in ["cát tuyến", "cat tuyen", "dây cung", "day cung"]):
        return "circle_chord", {}

    if any(k in p for k in ["góc nội tiếp", "goc noi tiep", "cung chứa góc", "cung tròn"]):
        return "inscribed_angle", {}

    if any(k in p for k in ["quạt tròn", "quat tron", "hình quạt"]):
        return "circle_sector", {}

    if any(k in p for k in ["vành khăn", "vanh khan"]):
        return "annulus", {}

    if any(k in p for k in ["vị trí tương đối", "hai đường tròn", "2 đường tròn"]):
        return "circle_positions", {}

    if any(k in p for k in ["đường tròn", "duong tron", "hình tròn", "hinh tron"]):
        return "circle", {"R": 3}

    # 7. ĐỒ THỊ HÀM SỐ & GIẢI TÍCH
    if any(k in p for k in ["parabol", "parabola", "bậc hai", "bac hai", "x^2", "x²"]):
        return "parabola", {}

    if any(k in p for k in ["bậc ba", "bac ba", "x^3", "x³"]):
        return "cubic", {}

    if any(k in p for k in ["bậc bốn", "trùng phương", "trung phuong", "x^4", "x⁴"]):
        return "quartic", {}

    if any(k in p for k in ["phân thức", "phan thuc", "tiệm cận"]):
        return "rational", {}

    if any(k in p for k in ["tiếp tuyến đồ thị", "tiếp tuyến hàm số"]):
        return "tangent_line", {}

    if any(k in p for k in ["diện tích hình phẳng", "hình thang cong", "tích phân diện tích"]):
        if any(k in p for k in ["giữa hai", "hai đồ thị"]):
            return "area_between", {}
        return "area_under", {}

    if any(k in p for k in ["riemann", "tổng riemann"]):
        return "riemann_sum", {}

    if any(k in p for k in ["khoảng đơn điệu", "đồng biến", "nghịch biến", "cực trị"]):
        return "monotone_intervals", {}

    if any(k in p for k in ["max min", "giá trị lớn nhất", "giá trị nhỏ nhất"]):
        return "max_min_segment", {}

    if any(k in p for k in ["elip", "ellipse"]):
        return "conic_ellipse", {}

    if any(k in p for k in ["hyperbol", "hyperbola"]):
        return "conic_hyperbola", {}

    if any(k in p for k in ["đồ thị", "do thi", "hàm số", "ham so"]):
        return "function_plot", {}

    # 8. VECTƠ & LƯỢNG GIÁC
    if any(k in p for k in ["lượng giác", "luong giac", "vòng tròn lượng giác", "đường tròn lượng giác"]):
        return "unit_circle", {}

    if any(k in p for k in ["vectơ", "vector", "vt"]):
        if any(k in p for k in ["tổng", "cộng", "+"]):
            return "vt_tong", {}
        if any(k in p for k in ["hiệu", "trừ", "-"]):
            return "vt_hieu", {}
        if any(k in p for k in ["vô hướng", "tích vô hướng"]):
            return "vt_tich_vo_huong", {}
        if any(k in p for k in ["thẳng hàng"]):
            return "vt_thang_hang", {}
        return "vector_add", {}

    # 9. SỐ PHỨC
    if any(k in p for k in ["số phức", "so phuc"]):
        if any(k in p for k in ["quỹ tích", "quy tich"]):
            return "sp_quy_tich", {}
        return "sp_diem_bieu_dien", {}

    return None, {}


def generate_accurate_math_svg(prompt: str, subject: str = "math") -> tuple[str, str]:
    """Tìm generator chính xác nhất trong 193 bộ máy hình học của AISTEM.

    Trả về tuple: (svg_xml, generator_name).
    """
    gen_name, params = match_geometry_intent(prompt)

    # 1. Thử render bằng AISTEM Accurate Generator
    if gen_name and render_illus:
        try:
            svg_content = render_illus(gen_name, params)
            if svg_content and "<svg" in svg_content:
                return svg_content, f"AISTEM Accurate Engine ({gen_name})"
        except Exception:
            pass

    # 2. Fallback: Nếu không khớp generator cục bộ, dùng LLM sinh SVG có kiểm soát
    from . import llm
    fallback_svg = llm.cloudflare_generate_math_svg(prompt, subject=subject)
    return fallback_svg, "AI Custom SVG (Llama 3.3)"
