"""Luật gán generator hình học phẳng mở rộng cho công thức.

Cùng chữ ký với ``matcher.py``: mỗi luật nhận dict công thức, trả
``(tên_generator, params, ghi_chú)`` hoặc ``None``.

Cách khớp ở đây CHẶT hơn ``matcher.py`` một bậc: không dùng kiểm tra chuỗi con
mà so ĐUÔI ``"<chủ-đề>.<tên-công-thức>"`` của ``id``. Lý do rất cụ thể:

* chuỗi con bắt nhầm những chỗ không ngờ — ``"sinh"`` trúng ``"sin"``,
  ``"phuong"`` trúng ``"pH"``;
* khớp đuôi chặn cả kiểu trùng tiền tố: luật lấy ``duong-tron.goc-noi-tiep``
  KHÔNG nuốt ``duong-tron.goc-noi-tiep-chan-nua-duong-tron``, vì đuôi phải trùng
  đến hết chuỗi;
* vẫn chịu được việc kho đổi cấp học (``math.thcs.…`` → ``math.thpt.…``), thứ mà
  khớp ``id`` tuyệt đối sẽ gãy.

Vài chỗ né có chủ ý, ghi lại để lần sau khỏi "sửa nhầm":

* ``he-thuc-luong.dinh-li-pytago`` và ``…-dao`` đã có ``r_pythagoras`` trong
  ``matcher.py`` lo; ở đây không đụng tới.
* ``bat-dang-thuc.bat-dang-thuc-tam-giac`` (|b−c| < a < b+c) được vẽ, còn
  ``khong-gian-euclid.bat-dang-thuc-tam-giac`` (‖u+v‖ ≤ ‖u‖+‖v‖) thì không —
  cùng tên công thức nhưng khác hẳn nội dung, khớp đuôi tự tách được hai cái.
* Các công thức tổng góc / số đường chéo đúng cho MỌI đa giác lồi nên dùng
  ``regular=False``; vẽ đa giác đều ở đó là gợi ý sai về điều kiện.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    """``id`` có kết thúc bằng ``.<tail>`` không (khớp trọn phần đuôi)."""
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


# -- tứ giác đặc biệt, đa giác --------------------------------------------
def r_rhombus(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-hoc-phang.chu-vi-hinh-thoi"):
        return "rhombus", {"diagonals": False}, "chu vi hình thoi (bốn cạnh bằng nhau)"
    if _tail(f, "hinh-hoc-phang.dien-tich-hinh-thoi"):
        return "rhombus", {"d1": 6, "d2": 4}, "S hình thoi theo hai đường chéo"
    if _tail(f, "dien-tich.dien-tich-hinh-thoi"):
        return "rhombus", {"d1": 6, "d2": 4, "height": True}, "S hình thoi = ½d₁d₂ = a·h"
    if _tail(f, "tu-giac.hinh-thoi"):
        return "rhombus", {"d1": 6, "d2": 4}, "dấu hiệu nhận biết hình thoi"
    return None


def r_square(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-hoc-phang.chu-vi-hinh-vuong",
             "hinh-hoc-phang.canh-hinh-vuong-tu-chu-vi",
             "hinh-hoc-phang.dien-tich-hinh-vuong",
             "dien-tich.dien-tich-hinh-vuong"):
        return "square", {"a": 4}, "hình vuông cạnh a"
    if _tail(f, "tu-giac.duong-cheo-hinh-vuong"):
        return "square", {"a": 4, "diagonals": 1}, "đường chéo hình vuông d = a√2"
    if _tail(f, "tu-giac.hinh-vuong"):
        return "square", {"a": 4, "diagonals": 2}, "dấu hiệu nhận biết hình vuông"
    return None


def r_quad_diagonals(f: dict) -> Optional[Match]:
    if _tail(f, "dien-tich.dien-tich-tu-giac-hai-duong-cheo-vuong-goc"):
        return "quad_diagonals", {"phi": 90}, "S tứ giác có hai đường chéo vuông góc"
    if _tail(f, "he-thuc-luong.dien-tich-tu-giac-hai-duong-cheo"):
        return "quad_diagonals", {"phi": 62}, "S tứ giác theo hai đường chéo và góc φ"
    return None


def r_polygon(f: dict) -> Optional[Match]:
    if _tail(f, "tu-giac.goc-cua-da-giac-deu"):
        return "regular_polygon", {"n": 6, "interior_angle": True}, "góc của đa giác đều"
    if _tail(f, "duong-tron.da-giac-deu-noi-tiep"):
        return "regular_polygon", {"n": 6, "circumcircle": True, "incircle": True,
                                   "side_label": True, "central_angle": True}, \
            "đa giác đều nội tiếp: aₙ = 2R·sin(180°/n)"
    if _tail(f, "tu-giac.tong-goc-da-giac-n-canh"):
        return "regular_polygon", {"n": 5, "regular": False, "interior_angle": "all"}, \
            "tổng các góc của đa giác lồi n cạnh"
    if _tail(f, "tu-giac.tong-cac-goc-tu-giac"):
        return "regular_polygon", {"n": 4, "regular": False, "interior_angle": "all"}, \
            "tổng bốn góc của tứ giác"
    if _tail(f, "tu-giac.so-duong-cheo-da-giac"):
        return "regular_polygon", {"n": 6, "regular": False, "diagonals": True}, \
            "số đường chéo của đa giác n cạnh"
    return None


# -- đường tròn ------------------------------------------------------------
def r_circle_chord(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.day-va-khoang-cach-den-tam", "oxy-duong-tron.day-cung"):
        return "circle_chord", {"R": 3, "d": 1.5}, "dây cung: AB = 2√(R² − d²)"
    if _tail(f, "duong-tron.quan-he-duong-kinh-va-day"):
        return "circle_chord", {"R": 3, "d": 1.6, "diameter": True,
                                "chord_name": "CD"}, "đường kính và dây cung"
    return None


def r_circle_tangent(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.tinh-chat-tiep-tuyen"):
        return "circle_tangent", {"mode": "tiep-diem"}, "tiếp tuyến vuông góc bán kính"
    if _tail(f, "duong-tron.hai-tiep-tuyen-cat-nhau"):
        return "circle_tangent", {"mode": "hai-tiep-tuyen"}, "hai tiếp tuyến cắt nhau"
    if _tail(f, "duong-tron.goc-tao-boi-tiep-tuyen-va-day"):
        return "circle_tangent", {"mode": "tiep-tuyen-day"}, "góc giữa tiếp tuyến và dây"
    return None


def r_circle_sector(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.goc-o-tam"):
        return "circle_sector", {"mode": "cung", "arc_label": "cung AB"}, \
            "góc ở tâm bằng số đo cung bị chắn"
    if _tail(f, "duong-tron.do-dai-cung-tron"):
        return "circle_sector", {"mode": "cung"}, "độ dài cung ℓ = πRn/180"
    if _tail(f, "luong-giac.do-dai-cung-tron"):
        # công thức này gói cả ℓ = Rα lẫn S = ½R²α, nên vẽ hình quạt (cung vẫn được
        # tô đậm) chứ không chỉ vẽ cung — vẽ cung thì mất hẳn vế diện tích
        return "circle_sector", {"mode": "quat", "unit": "rad"}, \
            "cung và quạt theo góc radian: ℓ = Rα, S = ½R²α"
    if _tail(f, "duong-tron.dien-tich-hinh-quat-tron"):
        return "circle_sector", {"mode": "quat"}, "diện tích hình quạt"
    if _tail(f, "duong-tron.dien-tich-hinh-vien-phan"):
        return "circle_sector", {"mode": "vien-phan"}, "viên phân = quạt − tam giác OAB"
    return None


def r_annulus(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.dien-tich-hinh-vanh-khan"):
        return "annulus", {"R": 3, "r": 1.9}, "diện tích hình vành khăn"
    return None


def r_inscribed_angle(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.goc-noi-tiep"):
        return "inscribed_angle", {"mode": "goc-o-tam"}, "góc nội tiếp = ½ góc ở tâm"
    if _tail(f, "duong-tron.goc-noi-tiep-cung-chan-mot-cung"):
        return "inscribed_angle", {"mode": "hai-diem"}, "hai góc nội tiếp cùng chắn một cung"
    if _tail(f, "duong-tron.goc-noi-tiep-chan-nua-duong-tron"):
        return "inscribed_angle", {"mode": "nua-duong-tron"}, "góc nội tiếp chắn nửa đường tròn"
    return None


def r_arc_locus(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.cung-chua-goc"):
        return "arc_locus", {"alpha": 55}, "quỹ tích cung chứa góc"
    return None


def r_cyclic_quad(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.tu-giac-noi-tiep", "duong-tron.dau-hieu-tu-giac-noi-tiep"):
        return "cyclic_quad", {}, "tứ giác nội tiếp: hai góc đối bù nhau"
    if _tail(f, "imo-hinh-hoc.dinh-li-ptolemy"):
        return "cyclic_quad", {"diagonals": True}, "định lí Ptolemy cho tứ giác nội tiếp"
    return None


def r_circle_secants(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.phuong-tich-diem-ngoai-duong-tron"):
        return "circle_secants", {"mode": "ngoai", "tangent": True}, \
            "phương tích của điểm ngoài đường tròn"
    if _tail(f, "duong-tron.phuong-tich-diem-trong-duong-tron"):
        return "circle_secants", {"mode": "trong"}, "phương tích của điểm trong đường tròn"
    if _tail(f, "duong-tron.goc-co-dinh-ben-ngoai-duong-tron"):
        return "circle_secants", {"mode": "ngoai", "angle": True}, \
            "góc có đỉnh ngoài đường tròn"
    if _tail(f, "duong-tron.goc-co-dinh-ben-trong-duong-tron"):
        return "circle_secants", {"mode": "trong", "angle": True}, \
            "góc có đỉnh trong đường tròn"
    return None


def r_circle_positions(f: dict) -> Optional[Match]:
    if _tail(f, "duong-tron.vi-tri-tuong-doi-diem-va-duong-tron"):
        return "circle_positions", {"mode": "diem"}, "vị trí tương đối điểm – đường tròn"
    if _tail(f, "duong-tron.vi-tri-tuong-doi-duong-thang-va-duong-tron",
             "oxy-duong-tron.dieu-kien-tiep-xuc"):
        return "circle_positions", {"mode": "duong-thang"}, \
            "vị trí tương đối đường thẳng – đường tròn theo d và R"
    if _tail(f, "duong-tron.vi-tri-tuong-doi-hai-duong-tron",
             "oxy-duong-tron.vi-tri-hai-duong-tron"):
        return "circle_positions", {"mode": "hai-duong-tron"}, \
            "năm vị trí tương đối của hai đường tròn"
    return None


# -- tam giác --------------------------------------------------------------
def r_triangle_centers(f: dict) -> Optional[Match]:
    if _tail(f, "duong-dong-quy.trong-tam-tam-giac"):
        return "triangle_centers", {"mode": "trong-tam"}, "ba trung tuyến và trọng tâm"
    if _tail(f, "duong-dong-quy.truc-tam-tam-giac"):
        return "triangle_centers", {"mode": "truc-tam"}, "ba đường cao và trực tâm"
    if _tail(f, "duong-dong-quy.ba-duong-phan-giac"):
        return "triangle_centers", {"mode": "phan-giac"}, "ba phân giác và tâm nội tiếp"
    if _tail(f, "duong-dong-quy.ba-duong-trung-truc"):
        return "triangle_centers", {"mode": "trung-truc"}, "ba trung trực và tâm ngoại tiếp"
    if _tail(f, "he-thuc-luong.tong-binh-phuong-trung-tuyen"):
        return "triangle_centers", {"mode": "trong-tam"}, "tổng bình phương ba trung tuyến"
    return None


def r_triangle_cevian(f: dict) -> Optional[Match]:
    if _tail(f, "he-thuc-luong.duong-trung-tuyen"):
        return "triangle_cevian", {"mode": "trung-tuyen"}, "độ dài trung tuyến mₐ"
    if _tail(f, "he-thuc-luong.duong-phan-giac", "he-thuc-luong.tinh-chat-duong-phan-giac",
             "dong-dang.tinh-chat-duong-phan-giac-trong-tam-giac"):
        return "triangle_cevian", {"mode": "phan-giac"}, "phân giác trong và tỉ số DB/DC"
    if _tail(f, "he-thuc-luong.dien-tich-duong-cao",
             "hinh-hoc-phang.dien-tich-hinh-tam-giac",
             "hinh-hoc-phang.chieu-cao-hinh-tam-giac"):
        return "triangle_cevian", {"mode": "duong-cao"}, "đường cao và S = ½·a·hₐ"
    return None


def r_equilateral(f: dict) -> Optional[Match]:
    if _tail(f, "dien-tich.dien-tich-tam-giac-deu"):
        return "equilateral_triangle", {"a": 4}, "tam giác đều: h = a√3/2, S = a²√3/4"
    if _tail(f, "he-thuc-luong.tam-giac-deu"):
        return "equilateral_triangle", {"a": 4, "circumcircle": True, "incircle": True}, \
            "tam giác đều: S, h, R, r theo cạnh a"
    if _tail(f, "tam-giac.tam-giac-deu"):
        return "equilateral_triangle", {"a": 4, "height": False, "angles": True}, \
            "tam giác đều có ba góc 60°"
    return None


def r_triangle_circumcircle(f: dict) -> Optional[Match]:
    if _tail(f, "he-thuc-luong.dinh-li-sin", "he-thuc-luong.canh-theo-ban-kinh-ngoai-tiep"):
        return "triangle_circumcircle", {"diameter": True}, "định lí sin: a/sin A = 2R"
    if _tail(f, "he-thuc-luong.ban-kinh-ngoai-tiep", "he-thuc-luong.dien-tich-abc-4r"):
        return "triangle_circumcircle", {}, "bán kính đường tròn ngoại tiếp"
    return None


def r_triangle_incircle(f: dict) -> Optional[Match]:
    if _tail(f, "he-thuc-luong.ban-kinh-noi-tiep", "he-thuc-luong.dien-tich-pr"):
        return "triangle_incircle", {}, "đường tròn nội tiếp: S = p·r"
    if _tail(f, "he-thuc-luong.ban-kinh-bang-tiep"):
        return "triangle_incircle", {"mode": "bang-tiep"}, "đường tròn bàng tiếp rₐ = S/(p − a)"
    return None


def r_triangle_labeled(f: dict) -> Optional[Match]:
    if _tail(f, "he-thuc-luong.dinh-li-cosin", "he-thuc-luong.he-qua-dinh-li-cosin"):
        return "triangle_labeled", {"mark_angles": ["A"]}, \
            "định lí cosin: a² = b² + c² − 2bc·cos A"
    if _tail(f, "he-thuc-luong.dien-tich-hai-canh-sin"):
        return "triangle_labeled", {"mark_angles": ["A", "B", "C"]}, \
            "S = ½ab·sin C (và hai dạng còn lại)"
    if _tail(f, "he-thuc-luong.dien-tich-heron", "he-thuc-luong.nua-chu-vi",
             "hinh-hoc-phang.chu-vi-hinh-tam-giac",
             "tam-giac.bat-dang-thuc-tam-giac",
             "bat-dang-thuc.bat-dang-thuc-tam-giac"):
        return "triangle_labeled", {}, "tam giác với ba cạnh a, b, c"
    if _tail(f, "tam-giac.tong-ba-goc"):
        return "triangle_labeled", {"mark_angles": ["A", "B", "C"]}, "tổng ba góc = 180°"
    if _tail(f, "tam-giac.tam-giac-can"):
        return "triangle_labeled", {"A": [2.5, 4.3], "B": [0, 0], "C": [5, 0],
                                    "ticks": {"b": 1, "c": 1},
                                    "mark_angles": ["B", "C"]}, \
            "tam giác cân: AB = AC ⟺ B̂ = Ĉ"
    return None


def r_right_triangle_altitude(f: dict) -> Optional[Match]:
    if _tail(f, "he-thuc-luong.canh-goc-vuong-va-hinh-chieu",
             "he-thuc-luong.duong-cao-va-hinh-chieu",
             "he-thuc-luong.nghich-dao-binh-phuong-duong-cao",
             "he-thuc-luong.tich-hai-canh-goc-vuong"):
        return "right_triangle_altitude", {"b": 4, "c": 3}, \
            "hệ thức lượng trong tam giác vuông (đường cao ứng cạnh huyền)"
    if _tail(f, "he-thuc-luong.trung-tuyen-canh-huyen"):
        return "right_triangle_altitude", {"b": 4, "c": 3, "mode": "trung-tuyen"}, \
            "trung tuyến ứng với cạnh huyền bằng nửa cạnh huyền"
    return None


def r_thales(f: dict) -> Optional[Match]:
    if _tail(f, "dong-dang.dinh-li-ta-let-thuan", "dong-dang.dinh-li-ta-let-dao",
             "dong-dang.he-qua-ta-let"):
        return "thales", {"k": 0.55}, "định lí Ta-lét trong tam giác"
    if _tail(f, "tu-giac.duong-trung-binh-tam-giac"):
        return "thales", {"midline": True}, "đường trung bình của tam giác"
    return None


def r_trapezoid_midline(f: dict) -> Optional[Match]:
    if _tail(f, "tu-giac.duong-trung-binh-hinh-thang"):
        return "trapezoid_midline", {}, "đường trung bình của hình thang"
    return None


RULES: list[Rule] = [
    r_rhombus, r_square, r_quad_diagonals, r_polygon,
    r_circle_chord, r_circle_tangent, r_circle_sector, r_annulus,
    r_inscribed_angle, r_arc_locus, r_cyclic_quad, r_circle_secants,
    r_circle_positions,
    r_triangle_centers, r_triangle_cevian, r_equilateral,
    r_triangle_circumcircle, r_triangle_incircle, r_triangle_labeled,
    r_right_triangle_altitude, r_thales, r_trapezoid_midline,
]


def match_formula(f: dict) -> Optional[Match]:
    for rule in RULES:
        m = rule(f)
        if m:
            return m
    return None
