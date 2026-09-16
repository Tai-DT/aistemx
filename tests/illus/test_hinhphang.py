"""Test họ hình **hinhphang** — hình học phẳng mở rộng.

Ba nhóm test, theo đúng thứ tự mức độ nguy hiểm của lỗi:

1. **Hình có đúng là hình ấy không** — đọc lại chính SVG vừa dựng rồi kiểm bằng
   hình học: tam giác vuông có vuông thật ở A không, đường tròn nội tiếp có
   TIẾP XÚC cả ba cạnh không, đa giác "không đều" có thật sự lồi và không đều
   không. Đây là nhóm quan trọng nhất: một hình vẽ sai thì người học không có
   cách nào phát hiện, khác hẳn một câu chữ sai vốn còn đối chiếu được.
2. **Hình có tràn khung / có tất định / có nhãn cho trình đọc màn hình không.**
3. **Luật khớp có bắt nhầm không** — với mỗi luật, khẳng định nó trả ``None``
   trên những công thức GẦN GIỐNG mà khác nghĩa, lấy id thật trong kho.
"""

from __future__ import annotations

import math
import re
import xml.etree.ElementTree as ET

import pytest
from conftest import svg_is_wellformed

from tools.illus.gen_hinhphang import REGISTRY
from tools.illus import rules_hinhphang as R

NUM = r"-?\d+(?:\.\d+)?"


# --------------------------------------------------------------------------
# Đọc ngược SVG: để kiểm hình bằng hình học chứ không bằng "có chạy là được"
# --------------------------------------------------------------------------
def _root(svg: str) -> ET.Element:
    return ET.fromstring(svg)


def _tag(el: ET.Element) -> str:
    return el.tag.rsplit("}", 1)[-1]


def _polys(svg: str) -> list[list[tuple[float, float]]]:
    out = []
    for el in _root(svg).iter():
        if _tag(el) in {"polygon", "polyline"}:
            out.append([tuple(map(float, s.split(",")))
                        for s in (el.get("points") or "").split()])
    return out


def _circles(svg: str) -> list[tuple[float, float, float]]:
    return [(float(el.get("cx")), float(el.get("cy")), float(el.get("r")))
            for el in _root(svg).iter() if _tag(el) == "circle"]


def _path_points(d: str) -> list[tuple[float, float]]:
    """Điểm mốc của path: điểm M/L và điểm cuối của mỗi cung A."""
    toks = re.findall(r"[A-Za-z]|%s" % NUM, d)
    pts, i, cmd = [], 0, None
    while i < len(toks):
        if re.fullmatch(r"[A-Za-z]", toks[i]):
            cmd, i = toks[i], i + 1
            continue
        if cmd in {"M", "L"}:
            pts.append((float(toks[i]), float(toks[i + 1])))
            i += 2
        elif cmd == "A":
            pts.append((float(toks[i + 5]), float(toks[i + 6])))
            i += 7
        else:
            i += 1
    return pts


def _all_points(svg: str) -> tuple[float, float, list[tuple[str, float, float]]]:
    """Khung và MỌI toạ độ trong hình, kể cả điểm mốc của ``<path>``.

    ``coords_within_viewbox`` dùng chung bỏ qua ``<path>``; họ này vẽ cung tròn
    bằng path nên phải tự soi thêm, không thì cả chương đường tròn không được
    canh khung.
    """
    root = _root(svg)
    _, _, w, h = (float(v) for v in root.get("viewBox").split())
    pts: list[tuple[str, float, float]] = []
    for el in root.iter():
        t = _tag(el)
        if t == "line":
            pts += [(t, float(el.get("x1")), float(el.get("y1"))),
                    (t, float(el.get("x2")), float(el.get("y2")))]
        elif t == "circle":
            cx, cy, r = (float(el.get(k)) for k in ("cx", "cy", "r"))
            pts += [(t, cx - r, cy - r), (t, cx + r, cy + r)]
        elif t == "rect":
            x, y = float(el.get("x")), float(el.get("y"))
            pts += [(t, x, y), (t, x + float(el.get("width")), y + float(el.get("height")))]
        elif t in {"polygon", "polyline"}:
            pts += [(t, x, y) for x, y in
                    [tuple(map(float, s.split(","))) for s in (el.get("points") or "").split()]]
        elif t == "text":
            pts.append((t, float(el.get("x")), float(el.get("y"))))
        elif t == "path":
            pts += [(t, x, y) for x, y in _path_points(el.get("d") or "")]
    return w, h, pts


def _dist(P, Q) -> float:
    return math.hypot(Q[0] - P[0], Q[1] - P[1])


def _angle(V, P, Q) -> float:
    """Số đo góc PVQ, đơn vị độ."""
    a = (P[0] - V[0], P[1] - V[1])
    b = (Q[0] - V[0], Q[1] - V[1])
    na, nb = math.hypot(*a), math.hypot(*b)
    cos = (a[0] * b[0] + a[1] * b[1]) / (na * nb)
    return math.degrees(math.acos(max(-1.0, min(1.0, cos))))


def _dist_to_line(P, A, B) -> float:
    ux, uy = B[0] - A[0], B[1] - A[1]
    L = math.hypot(ux, uy)
    return abs((P[0] - A[0]) * uy - (P[1] - A[1]) * ux) / L


def _triangle_of(svg: str) -> list[tuple[float, float]]:
    """Ba đỉnh tam giác: lấy polyline khép kín 4 điểm đầu tiên (A, B, C, A)."""
    for pts in _polys(svg):
        if len(pts) == 4 and pts[0] == pts[3]:
            return pts[:3]
    raise AssertionError("không tìm thấy đường bao tam giác trong SVG")


# --------------------------------------------------------------------------
# 1. Hình có đúng là hình ấy không
# --------------------------------------------------------------------------
def test_tam_giac_vuong_thuc_su_vuong_tai_A() -> None:
    """Hệ thức lượng chỉ đúng khi A vuông và H nằm TRONG cạnh huyền.

    Nếu H rơi ra ngoài BC thì b′, c′ không còn là hình chiếu, mọi hệ thức trong
    hình sai hết — mà nhìn ảnh vẫn thấy "một tam giác có đường cao".
    """
    for b, c in ((4, 3), (1, 7), (5, 5), (9.5, 0.4)):
        svg = REGISTRY["right_triangle_altitude"]({"b": b, "c": c})
        A, B, C = _triangle_of(svg)
        assert abs(_angle(A, B, C) - 90) < 0.5, f"b={b} c={c}: góc A không vuông"
        # chân đường cao = hình chiếu của A lên BC, phải nằm giữa B và C
        t = ((A[0] - B[0]) * (C[0] - B[0]) + (A[1] - B[1]) * (C[1] - B[1])) / _dist(B, C) ** 2
        assert 0 < t < 1, f"b={b} c={c}: chân đường cao rơi ra ngoài cạnh huyền"
        # tỉ lệ cạnh phải giữ đúng: AB/AC = c/b (sai số tương đối — svgkit làm
        # tròn toạ độ về 3 chữ số thập phân, so tuyệt đối sẽ vấp ở hình rất dẹt)
        assert abs(_dist(A, B) / _dist(A, C) / (c / b) - 1) < 1e-3


def test_goc_noi_tiep_chan_nua_duong_tron_dung_90_do() -> None:
    for deg in (20, 62, 90, 150):
        svg = REGISTRY["inscribed_angle"]({"mode": "nua-duong-tron", "apex_deg": deg})
        A, B, C = _triangle_of(svg)
        assert abs(_angle(A, B, C) - 90) < 0.6, f"apex={deg}: góc nội tiếp không vuông"


def test_tam_giac_deu_ba_canh_bang_nhau() -> None:
    A, B, C = _triangle_of(REGISTRY["equilateral_triangle"]({"a": 5}))
    sides = [_dist(A, B), _dist(B, C), _dist(C, A)]
    assert max(sides) - min(sides) < 0.5, f"tam giác 'đều' có ba cạnh {sides}"


def test_hinh_vuong_bon_canh_bang_va_bon_goc_vuong() -> None:
    pts = None
    for poly in _polys(REGISTRY["square"]({"a": 4, "diagonals": 2})):
        if len(poly) == 5 and poly[0] == poly[4]:
            pts = poly[:4]
    assert pts is not None
    sides = [_dist(pts[i], pts[(i + 1) % 4]) for i in range(4)]
    assert max(sides) / min(sides) < 1.001
    for i in range(4):
        assert abs(_angle(pts[i], pts[i - 1], pts[(i + 1) % 4]) - 90) < 0.05


def test_hinh_thoi_bon_canh_bang_va_hai_duong_cheo_vuong_goc() -> None:
    svg = REGISTRY["rhombus"]({"d1": 7, "d2": 3})
    pts = next(p[:4] for p in _polys(svg) if len(p) == 5 and p[0] == p[4])
    sides = [_dist(pts[i], pts[(i + 1) % 4]) for i in range(4)]
    assert max(sides) / min(sides) < 1.001, f"hình thoi có cạnh lệch: {sides}"
    # hai đường chéo cắt nhau tại trung điểm mỗi đường và vuông góc với nhau
    tam = ((pts[0][0] + pts[2][0]) / 2, (pts[0][1] + pts[2][1]) / 2)
    assert abs(_angle(tam, pts[0], pts[1]) - 90) < 0.05


def test_duong_tron_noi_tiep_tiep_xuc_ca_ba_canh() -> None:
    """Vẽ một đường tròn "gần gần" ba cạnh là hình sai — phải tiếp xúc đúng."""
    svg = REGISTRY["triangle_incircle"]({})
    A, B, C = _triangle_of(svg)
    inc = [c for c in _circles(svg) if c[2] > 8]
    assert inc, "không thấy đường tròn nội tiếp"
    cx, cy, r = inc[0]
    for P, Q in ((A, B), (B, C), (C, A)):
        assert abs(_dist_to_line((cx, cy), P, Q) - r) < 0.5, "đường tròn không tiếp xúc cạnh"


def test_duong_tron_bang_tiep_tiep_xuc_BC_va_hai_tia_keo_dai() -> None:
    svg = REGISTRY["triangle_incircle"]({"mode": "bang-tiep"})
    A, B, C = _triangle_of(svg)
    cx, cy, r = max(_circles(svg), key=lambda c: c[2])
    for P, Q in ((B, C), (A, B), (A, C)):
        assert abs(_dist_to_line((cx, cy), P, Q) - r) < 0.5
    # tâm bàng tiếp nằm khác phía với A so với BC
    def side(P):
        return ((C[0] - B[0]) * (P[1] - B[1]) - (C[1] - B[1]) * (P[0] - B[0]))
    assert side((cx, cy)) * side(A) < 0, "tâm bàng tiếp nằm cùng phía với A"


def test_duong_tron_ngoai_tiep_di_qua_ca_ba_dinh() -> None:
    for mode_svg in (REGISTRY["triangle_circumcircle"]({}),
                     REGISTRY["triangle_centers"]({"mode": "trung-truc"})):
        A, B, C = _triangle_of(mode_svg)
        cx, cy, r = max(_circles(mode_svg), key=lambda c: c[2])
        for V in (A, B, C):
            assert abs(_dist((cx, cy), V) - r) < 0.6, "đỉnh không nằm trên đường tròn ngoại tiếp"


def test_tu_giac_noi_tiep_co_bon_dinh_tren_duong_tron() -> None:
    svg = REGISTRY["cyclic_quad"]({})
    quad = next(p[:4] for p in _polys(svg) if len(p) == 5 and p[0] == p[4])
    cx, cy, r = max(_circles(svg), key=lambda c: c[2])
    for V in quad:
        assert abs(_dist((cx, cy), V) - r) < 0.5
    # tổng hai góc đối = 180°
    assert abs(_angle(quad[0], quad[3], quad[1]) + _angle(quad[2], quad[1], quad[3]) - 180) < 1.0


def test_da_giac_deu_thi_deu_con_da_giac_loi_thi_khong_deu_nhung_van_loi() -> None:
    """``regular=False`` phải cho ra đa giác LỒI mà KHÔNG đều.

    Hai vế đều quan trọng: không lồi thì công thức tổng góc (n−2)·180° sai;
    còn nếu vẫn đều thì hình lại gợi ý sai rằng công thức đòi hỏi tính đều.
    """
    def sides_and_convex(svg):
        pts = next(p[:-1] for p in _polys(svg) if len(p) >= 4 and p[0] == p[-1])
        n = len(pts)
        lens = [_dist(pts[i], pts[(i + 1) % n]) for i in range(n)]
        crosses = []
        for i in range(n):
            a = pts[(i + 1) % n][0] - pts[i][0], pts[(i + 1) % n][1] - pts[i][1]
            b = pts[(i + 2) % n][0] - pts[(i + 1) % n][0], pts[(i + 2) % n][1] - pts[(i + 1) % n][1]
            crosses.append(a[0] * b[1] - a[1] * b[0])
        return lens, all(c > 0 for c in crosses) or all(c < 0 for c in crosses)

    for n in (4, 5, 6, 8):
        lens, convex = sides_and_convex(REGISTRY["regular_polygon"]({"n": n}))
        assert convex and max(lens) / min(lens) < 1.001, f"đa giác đều {n} cạnh không đều"
        lens, convex = sides_and_convex(REGISTRY["regular_polygon"]({"n": n, "regular": False}))
        assert convex, f"đa giác lồi {n} cạnh hoá ra không lồi"
        assert max(lens) / min(lens) > 1.2, f"đa giác 'không đều' {n} cạnh vẫn gần như đều"


def test_day_cung_dung_khoang_cach_toi_tam() -> None:
    """AB = 2√(R² − d²): kiểm ngay trên toạ độ đã vẽ, không tin vào tham số."""
    for R_, d_ in ((3, 1.5), (4, 0.3), (2, 1.8)):
        svg = REGISTRY["circle_chord"]({"R": R_, "d": d_})
        cx, cy, rp = max(_circles(svg), key=lambda c: c[2])
        scale = rp / R_
        # dây là đoạn nằm ngang dài nhất trong hình
        chord = max(
            (l for l in _root(svg).iter() if _tag(l) == "line"
             and abs(float(l.get("y1")) - float(l.get("y2"))) < 1e-6),
            key=lambda l: abs(float(l.get("x2")) - float(l.get("x1"))),
        )
        length = abs(float(chord.get("x2")) - float(chord.get("x1"))) / scale
        assert abs(length - 2 * math.sqrt(R_ ** 2 - d_ ** 2)) < 0.02
        assert abs(abs(float(chord.get("y1")) - cy) / scale - d_) < 0.02


def test_cung_chua_goc_moi_diem_M_nhin_AB_dung_goc_alpha() -> None:
    """Cung chứa góc chọn nhầm cung là sai lặng lẽ nhất trong cả họ này."""
    for alpha in (35, 55, 90, 120):
        svg = REGISTRY["arc_locus"]({"alpha": alpha})
        dots = sorted(((cx, cy) for cx, cy, r in _circles(svg) if r < 6),
                      key=lambda q: -q[1])
        assert len(dots) >= 4, "thiếu điểm A, B hoặc các điểm M"
        # A và B nằm trên dây ngang nên là hai chấm THẤP nhất trên màn hình;
        # chọn theo hoành độ là sai vì cung lớn còn phình ra quá hai đầu dây
        A, B = sorted(dots[:2], key=lambda q: q[0])
        assert abs(A[1] - B[1]) < 1.0, "A và B không cùng nằm trên một dây ngang"
        Ms = dots[2:]
        assert Ms, "không có điểm M nào trên cung phía trên"
        for M in Ms:
            assert abs(_angle(M, A, B) - alpha) < 1.0, f"α={alpha}: M nhìn AB dưới góc khác"


# --------------------------------------------------------------------------
# 2. Bất biến kỹ thuật của mọi hình trong họ
# --------------------------------------------------------------------------
def _rule_params() -> list[tuple[str, dict]]:
    """Mọi bộ tham số mà RULES thực sự sinh ra — đây mới là cái chạy trong kho."""
    from tools.illus.gen_hinhphang import REGISTRY as reg  # noqa: F401
    import json

    from conftest import ROOT

    formulas = json.loads((ROOT / "data" / "formulas" / "index.json")
                          .read_text(encoding="utf-8"))["formulas"]
    seen, out = set(), []
    for f in formulas:
        for rule in R.RULES:
            got = rule(f)
            if got:
                key = (got[0], json.dumps(got[1], sort_keys=True))
                if key not in seen:
                    seen.add(key)
                    out.append((got[0], got[1]))
                break
    return out


# tham số biên: 0, số âm, giá trị rất lớn, kiểu dữ liệu sai, chế độ không tồn tại
BIEN: list[tuple[str, dict]] = [
    ("rhombus", {"d1": 0, "d2": -3}), ("rhombus", {"d1": 1e9, "d2": 1e-9, "height": True}),
    ("square", {"a": 0}), ("square", {"a": -5, "diagonals": 9}),
    ("quad_diagonals", {"d1": 0, "d2": 0, "phi": 0}),
    ("quad_diagonals", {"phi": 400, "t1": -1, "t2": 5}),
    ("regular_polygon", {"n": 0}), ("regular_polygon", {"n": 2}),
    ("regular_polygon", {"n": 1000, "diagonals": True}),
    ("circle_chord", {"R": 0, "d": 0}), ("circle_chord", {"R": -3, "d": 99}),
    ("circle_tangent", {"R": 0}), ("circle_tangent", {"mode": "hai-tiep-tuyen", "dM": 0.01}),
    ("circle_tangent", {"mode": "chế-độ-lạ"}),
    ("circle_sector", {"sweep": 0}), ("circle_sector", {"sweep": -30}),
    ("circle_sector", {"sweep": 1e9}), ("circle_sector", {"R": 0, "mode": "quat"}),
    ("annulus", {"R": 1, "r": 5}), ("annulus", {"R": 0, "r": 0}),
    ("inscribed_angle", {"R": 0}), ("inscribed_angle", {"b_deg": 0, "c_deg": 0}),
    ("arc_locus", {"alpha": 0}), ("arc_locus", {"alpha": -20}), ("arc_locus", {"AB": 0}),
    ("cyclic_quad", {"angles": []}), ("cyclic_quad", {"angles": "x"}),
    ("circle_secants", {"dM": 0.1}), ("circle_secants", {"mode": "trong", "mx": 9, "my": -9}),
    ("circle_positions", {"mode": "duong-thang", "R": 0}),
    ("circle_positions", {"mode": "chế-độ-lạ"}),
    ("triangle_centers", {"A": [0, 0], "B": [0, 0], "C": [0, 0], "mode": "trung-truc"}),
    ("triangle_centers", {"A": [1, 0], "B": [2, 0], "C": [3, 0], "mode": "truc-tam"}),
    ("triangle_cevian", {"A": [0, 0], "B": [0, 0], "C": [0, 0]}),
    ("equilateral_triangle", {"a": 0}), ("equilateral_triangle", {"a": 1e9,
                                                                  "circumcircle": True}),
    ("triangle_circumcircle", {"A": [0, 0], "B": [1, 0], "C": [2, 0]}),
    ("triangle_incircle", {"A": [0, 0], "B": [1, 0], "C": [2, 0], "mode": "bang-tiep"}),
    ("triangle_labeled", {"mark_angles": "A"}), ("triangle_labeled", {"ticks": "x"}),
    ("right_triangle_altitude", {"b": 0, "c": 0}),
    ("right_triangle_altitude", {"b": 1e9, "c": 1, "mode": "trung-tuyen"}),
    ("thales", {"k": 0}), ("thales", {"k": 5}),
    ("trapezoid_midline", {"ab": 6, "cd": 3}), ("trapezoid_midline", {"offset": -9}),
]

MOI_CA: list[tuple[str, dict]] = ([(g, {}) for g in sorted(REGISTRY)]
                                  + _rule_params() + BIEN)


@pytest.mark.parametrize("gen,params", MOI_CA, ids=lambda v: str(v)[:40])
def test_svg_hop_le_va_tat_dinh(gen: str, params: dict) -> None:
    svg = REGISTRY[gen](dict(params))
    assert svg == REGISTRY[gen](dict(params)), "vẽ hai lần ra hai chuỗi khác nhau"
    assert svg_is_wellformed(svg), "SVG hỏng hoặc tham chiếu tài nguyên ngoài"
    assert "<title>" in svg and "<desc>" in svg, "thiếu title/desc cho trình đọc màn hình"
    body = svg.split("</style>", 1)[-1]
    assert "#" not in body, "có mã màu viết thẳng, hình sẽ không lật theo dark mode"


@pytest.mark.parametrize("gen,params", MOI_CA, ids=lambda v: str(v)[:40])
def test_toa_do_nam_trong_viewbox(gen: str, params: dict) -> None:
    """Kể cả điểm mốc của ``<path>`` — cung tròn ở họ này toàn vẽ bằng path."""
    w, h, pts = _all_points(REGISTRY[gen](dict(params)))
    assert 40 <= w <= 4000 and 40 <= h <= 4000, f"khung phi lí {w}x{h}"
    ngoai = [q for q in pts if not (-0.5 <= q[1] <= w + 0.5 and -0.5 <= q[2] <= h + 0.5)]
    assert not ngoai, f"{len(ngoai)} điểm nằm ngoài khung {w}x{h}: {ngoai[:3]}"


# --------------------------------------------------------------------------
# 3. Luật khớp: đúng cái cần, và KHÔNG bắt nhầm cái gần giống
# --------------------------------------------------------------------------
# Mỗi dòng: (luật, id thật trong kho, vì sao luật này PHẢI bỏ qua nó)
NE: list[tuple[str, str, str]] = [
    ("r_rhombus", "math.thcs.dien-tich.dien-tich-hinh-binh-hanh",
     "hình bình hành, không phải hình thoi"),
    ("r_rhombus", "math.thcs.tu-giac.hinh-vuong", "hình vuông có luật riêng"),
    ("r_square", "math.thcs.dien-tich.dien-tich-hinh-chu-nhat", "hình chữ nhật"),
    ("r_square", "math.thcs.tu-giac.hinh-thoi", "hình thoi"),
    ("r_quad_diagonals", "math.thcs.dien-tich.dien-tich-hinh-thoi",
     "cũng có d₁d₂ nhưng là hình thoi, phải vẽ hình thoi"),
    ("r_polygon", "math.thpt.fm-so-phuc.can-bac-n-da-giac-deu",
     "căn bậc n của số phức, cần mặt phẳng phức chứ không phải đa giác trần"),
    ("r_circle_chord", "math.thpt.oxyz-mat-cau.ban-kinh-duong-tron-giao-tuyen",
     "r = √(R²−d²) nhưng là mặt cầu cắt mặt phẳng trong KHÔNG GIAN"),
    ("r_circle_chord", "math.thpt.oxy-duong-tron.pt-chinh-tac", "phương trình, cần hệ trục"),
    ("r_circle_tangent", "math.thpt.dao-ham.phuong-trinh-tiep-tuyen",
     "tiếp tuyến của đồ thị hàm số, không phải của đường tròn"),
    ("r_circle_tangent", "math.thpt.fm-conic.tiep-tuyen-elip-tai-diem", "tiếp tuyến elip"),
    ("r_circle_tangent", "math.thpt.oxy-duong-tron.tiep-tuyen-tai-diem",
     "phương trình tiếp tuyến trong Oxy, cần hệ trục"),
    ("r_circle_sector", "math.thcs.thong-ke.goc-o-tam-bieu-do-hinh-quat",
     "góc ở tâm của BIỂU ĐỒ quạt thống kê, không phải cung tròn hình học"),
    ("r_annulus", "math.thcs.duong-tron.dien-tich-hinh-tron", "hình tròn đặc"),
    ("r_inscribed_angle", "math.thcs.duong-tron.goc-o-tam", "góc ở tâm, không phải nội tiếp"),
    ("r_inscribed_angle", "math.thcs.duong-tron.cung-chua-goc", "quỹ tích, hình khác hẳn"),
    ("r_arc_locus", "math.thcs.duong-tron.goc-noi-tiep", "góc nội tiếp đơn lẻ"),
    ("r_cyclic_quad", "math.thpt.imo-hinh-hoc.bat-dang-thuc-ptolemy",
     "BẤT đẳng thức Ptolemy đúng cho tứ giác bất kì; vẽ tứ giác nội tiếp là vẽ "
     "đúng trường hợp dấu bằng, tức là gợi ý sai"),
    ("r_circle_secants", "math.thcs.duong-tron.hai-tiep-tuyen-cat-nhau", "tiếp tuyến"),
    ("r_circle_positions", "math.thpt.oxy-duong-tron.pt-tong-quat", "phương trình"),
    ("r_triangle_centers", "math.thpt.oxy-toa-do.toa-do-trong-tam",
     "toạ độ trọng tâm — hình phải có hệ trục"),
    ("r_triangle_centers", "math.thpt.oxyz-toa-do.trong-tam-tu-dien", "tứ diện, hình 3D"),
    ("r_triangle_cevian", "math.thcs.dien-tich.dien-tich-tam-giac",
     "đã có generator `triangle` trong matcher.py nhận"),
    ("r_triangle_cevian", "math.thcs.dong-dang.ti-so-duong-cao",
     "tỉ số đường cao của hai tam giác ĐỒNG DẠNG, cần hai tam giác"),
    ("r_equilateral", "math.thpt.the-tich.lang-tru-dung-tam-giac-deu", "khối lăng trụ, 3D"),
    ("r_equilateral", "math.thcs.dien-tich.dien-tich-tam-giac", "tam giác thường"),
    ("r_triangle_circumcircle", "math.thpt.mat-tron-xoay.mat-cau-ngoai-tiep-chop",
     "mặt cầu ngoại tiếp hình chóp, 3D"),
    ("r_triangle_incircle", "math.thpt.mat-tron-xoay.mat-cau-noi-tiep-da-dien", "3D"),
    ("r_triangle_labeled", "math.dai-hoc.khong-gian-euclid.bat-dang-thuc-tam-giac",
     "cùng tên 'bất đẳng thức tam giác' nhưng là chuẩn vectơ ‖u+v‖ ≤ ‖u‖+‖v‖"),
    ("r_triangle_labeled", "math.thcs.he-thuc-luong.dinh-li-pytago",
     "Pytago đã có rule riêng trong matcher.py"),
    ("r_right_triangle_altitude", "math.thcs.he-thuc-luong.dinh-li-pytago", "Pytago"),
    ("r_right_triangle_altitude", "math.thcs.he-thuc-luong.dinh-li-pytago-dao", "Pytago đảo"),
    ("r_right_triangle_altitude", "math.thpt.he-thuc-luong.dinh-li-cosin",
     "a² = b² + c² − 2bc·cosA: tam giác THƯỜNG, tiền tố giống hệt Pytago"),
    ("r_right_triangle_altitude", "math.thpt.quan-he-vuong-goc.tu-dien-vuong-duong-cao",
     "1/h² = 1/a²+1/b²+1/c² nhưng là tứ diện vuông, 3D"),
    ("r_thales", "math.thcs.tu-giac.duong-trung-binh-hinh-thang", "hình thang"),
    ("r_thales", "math.thcs.dong-dang.ti-so-dien-tich", "tỉ số diện tích"),
    ("r_trapezoid_midline", "math.thcs.tu-giac.duong-trung-binh-tam-giac", "tam giác"),
    ("r_trapezoid_midline", "math.thcs.dien-tich.dien-tich-hinh-thang",
     "diện tích hình thang đã có generator `trapezoid`"),
]


@pytest.mark.parametrize("ten_luat,fid,ly_do", NE, ids=lambda v: str(v)[:44])
def test_luat_khong_bat_nham(ten_luat: str, fid: str, ly_do: str,
                             formula_by_id: dict[str, dict]) -> None:
    assert fid in formula_by_id, f"id {fid} không còn trong kho — cập nhật lại test"
    rule = getattr(R, ten_luat)
    assert rule(formula_by_id[fid]) is None, f"{ten_luat} bắt nhầm {fid}: {ly_do}"


# Vài ca khớp ĐÚNG, chốt cả generator lẫn chế độ — đổi chế độ là đổi nghĩa hình.
KHOP: list[tuple[str, str, dict]] = [
    ("math.thcs.duong-tron.goc-noi-tiep", "inscribed_angle", {"mode": "goc-o-tam"}),
    ("math.thcs.duong-tron.goc-noi-tiep-chan-nua-duong-tron", "inscribed_angle",
     {"mode": "nua-duong-tron"}),
    ("math.thcs.duong-tron.goc-noi-tiep-cung-chan-mot-cung", "inscribed_angle",
     {"mode": "hai-diem"}),
    ("math.thcs.he-thuc-luong.trung-tuyen-canh-huyen", "right_triangle_altitude",
     {"b": 4, "c": 3, "mode": "trung-tuyen"}),
    ("math.thpt.he-thuc-luong.dinh-li-cosin", "triangle_labeled", {"mark_angles": ["A"]}),
    ("math.thpt.he-thuc-luong.dinh-li-sin", "triangle_circumcircle", {"diameter": True}),
    ("math.thcs.duong-tron.dien-tich-hinh-quat-tron", "circle_sector", {"mode": "quat"}),
    ("math.thcs.duong-tron.dien-tich-hinh-vien-phan", "circle_sector", {"mode": "vien-phan"}),
    ("math.thcs.tu-giac.tong-goc-da-giac-n-canh", "regular_polygon",
     {"n": 5, "regular": False, "interior_angle": "all"}),
]


@pytest.mark.parametrize("fid,gen,params", KHOP, ids=lambda v: str(v)[:44])
def test_khop_dung_generator_va_che_do(fid: str, gen: str, params: dict,
                                       formula_by_id: dict[str, dict]) -> None:
    assert fid in formula_by_id, f"id {fid} không còn trong kho"
    got = R.match_formula(formula_by_id[fid])
    assert got is not None, f"{fid}: không luật nào nhận"
    assert (got[0], got[1]) == (gen, params), f"{fid}: khớp ra {got[0]} {got[1]}"


def test_chi_nhan_cong_thuc_toan(formulas: list[dict]) -> None:
    """Không một công thức Lí/Hoá/Sinh nào được lọt vào họ hình học phẳng.

    Đây là lưới chắn rẻ nhất cho kiểu khớp lỏng: `sinh` trúng `sin`, `phuong`
    trúng `pH`. Nếu luật nào nới ra quá tay, gần như chắc chắn nó sẽ vấp ở đây.
    """
    la = [f["id"] for f in formulas
          if f.get("subject") != "math" and R.match_formula(f) is not None]
    assert not la, f"họ hinhphang nhận nhầm công thức ngoài môn Toán: {la[:5]}"


def test_chi_nhan_bac_pho_thong(formulas: list[dict]) -> None:
    """Họ này phục vụ tiểu học – THCS – THPT; lọt bậc đại học là dấu hiệu khớp lỏng."""
    la = [f["id"] for f in formulas
          if f.get("level") == "dai-hoc" and R.match_formula(f) is not None]
    assert not la, f"nhận nhầm công thức bậc đại học: {la[:5]}"


def test_khong_dung_do_voi_matcher_cu(formulas: list[dict]) -> None:
    """Không giành lại công thức mà `matcher.py` đã nhận.

    `matcher.py` đứng trước trong registry nên trùng thì luật cũ thắng — nhưng
    trùng nghĩa là một trong hai bên đang với tay quá phạm vi của mình.
    """
    from tools.illus.matcher import match_formula as cu

    dung = [f["id"] for f in formulas if cu(f) and R.match_formula(f)]
    assert not dung, f"tranh chấp với matcher.py: {dung}"


def test_moi_luat_deu_bat_duoc_it_nhat_mot_cong_thuc(formulas: list[dict]) -> None:
    """Luật không bắt được gì là luật viết sai tên id — im lặng và vô hình."""
    cheo = {rule.__name__: 0 for rule in R.RULES}
    for f in formulas:
        for rule in R.RULES:
            if rule(f):
                cheo[rule.__name__] += 1
                break
    trong = [k for k, v in cheo.items() if v == 0]
    assert not trong, f"luật không khớp được công thức nào: {trong}"


def test_luat_chi_tro_toi_generator_co_that(formulas: list[dict]) -> None:
    for f in formulas:
        got = R.match_formula(f)
        if got:
            assert got[0] in REGISTRY, f"{f['id']}: trỏ tới generator lạ {got[0]!r}"


def test_do_phu_khong_tut(formulas: list[dict]) -> None:
    """Chốt con số đã tự đọc và duyệt tay từng ca: 87 công thức.

    Con số cứng ở đây là có chủ ý. Nó tụt xuống nghĩa là kho đổi id (phải sửa
    luật); nó vọt lên nghĩa là ai đó vừa nới luật — và mọi ca mới phải được đọc
    lại bằng mắt trước khi tin, chứ không được để nó tự tăng.
    """
    n = sum(1 for f in formulas if R.match_formula(f) is not None)
    assert n == 87, f"số công thức khớp đổi từ 87 thành {n} — đọc lại từng ca mới"
