"""Test cho họ hình **dienquang** (điện - từ - quang - nhiệt - hạt nhân).

Ba nhóm khẳng định, theo đúng thứ tự rủi ro:

1. **Generator không nổ và không tràn khung.** Hình tràn ``viewBox`` là lỗi im
   lặng: SVG vẫn hợp lệ, trình duyệt vẫn hiện, chỉ mất một phần hình.
2. **Luật khớp không bắt nhầm.** Với mỗi luật đều có ca âm lấy id THẬT trong
   kho, chọn những công thức gần giống nhất về id/chủ đề mà khác nghĩa.
3. **Hình đúng nội dung công thức.** Vị trí ảnh qua thấu kính/gương và góc khúc
   xạ được kiểm bằng số, không chỉ kiểm "có vẽ gì đó".
"""

from __future__ import annotations

import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.illus.gen_dienquang import REGISTRY  # noqa: E402
from tools.illus.svgkit import _n  # noqa: E402
from tools.illus import rules_dienquang as RD  # noqa: E402

SVG_NS = "{http://www.w3.org/2000/svg}"
# Tham chiếu tài nguyên ngoài THẬT SỰ. ``xmlns="http://www.w3.org/2000/svg"``
# chỉ là khai báo không gian tên, không phải thứ trình duyệt phải tải về.
EXTERNAL = re.compile(
    r'(?:xlink:)?href\s*=|<image\b|<use\b|src\s*=|@import|url\(\s*["\']?(?:https?:)?//'
)


# --------------------------------------------------------------------------
# Tiện ích
# --------------------------------------------------------------------------
def _viewbox(svg: str) -> tuple[float, float]:
    root = ET.fromstring(svg)
    _, _, w, h = (float(v) for v in root.get("viewBox").split())
    return w, h


def _points(svg: str) -> list[tuple[str, float, float]]:
    """Mọi toạ độ đỉnh/tâm/góc mà một phần tử SVG khai báo tường minh."""
    out: list[tuple[str, float, float]] = []
    for el in ET.fromstring(svg).iter():
        tag = el.tag.replace(SVG_NS, "")
        if tag == "line":
            out += [(tag, float(el.get("x1")), float(el.get("y1"))),
                    (tag, float(el.get("x2")), float(el.get("y2")))]
        elif tag == "circle":
            cx, cy, r = float(el.get("cx")), float(el.get("cy")), float(el.get("r"))
            out += [(tag, cx - r, cy - r), (tag, cx + r, cy + r)]
        elif tag == "rect":
            x, y = float(el.get("x")), float(el.get("y"))
            out += [(tag, x, y),
                    (tag, x + float(el.get("width")), y + float(el.get("height")))]
        elif tag in ("polyline", "polygon"):
            for pair in el.get("points").split():
                x, y = pair.split(",")
                out.append((tag, float(x), float(y)))
        elif tag == "text":
            out.append((tag, float(el.get("x")), float(el.get("y"))))
    return out


def _noi_dung(svg: str) -> str:
    """Toàn bộ chữ HIỂN THỊ trên hình, đã giải mã thực thể XML.

    Phải so trên chuỗi đã parse chứ không trên mã nguồn SVG: dấu ``<`` trong
    "r < i" nằm trong SVG dưới dạng ``&lt;``, tìm thẳng trên chuỗi thô sẽ trượt.
    """
    return "\n".join(el.text or "" for el in ET.fromstring(svg).iter()
                     if el.tag in (f"{SVG_NS}text", f"{SVG_NS}title", f"{SVG_NS}desc"))


def _assert_valid(svg: str) -> None:
    """Mọi khẳng định chung cho một SVG của kho: hợp lệ, kín khung, đọc được."""
    root = ET.fromstring(svg)                       # ném ParseError nếu XML hỏng
    assert root.tag == f"{SVG_NS}svg"
    assert root.find(f"{SVG_NS}title") is not None, "thiếu <title> cho trình đọc màn hình"
    assert root.find(f"{SVG_NS}desc") is not None, "thiếu <desc> cho trình đọc màn hình"
    assert not EXTERNAL.search(svg), "SVG tham chiếu tài nguyên ngoài"
    # Màu phải đi qua lớp CSS để bảng màu tự lật theo dark mode.
    assert not re.search(r'(?:fill|stroke)="#', svg), "hard-code màu bằng mã hex"
    w, h = _viewbox(svg)
    for tag, x, y in _points(svg):
        assert -1.0 <= x <= w + 1.0, f"{tag} tràn khung theo x: {x} ∉ [0, {w}]"
        assert -1.0 <= y <= h + 1.0, f"{tag} tràn khung theo y: {y} ∉ [0, {h}]"


@pytest.fixture(scope="module")
def kho() -> dict[str, dict]:
    data = json.loads((ROOT / "data" / "formulas" / "index.json").read_text("utf-8"))
    return {f["id"]: f for f in data["formulas"]}


def _match(f: dict):
    hits = [m for m in (rule(f) for rule in RD.RULES) if m]
    assert len(hits) <= 1, f"{f['id']} khớp nhiều luật: {[h[0] for h in hits]}"
    return hits[0] if hits else None


# --------------------------------------------------------------------------
# 1. Generator: mặc định, biên, tất định
# --------------------------------------------------------------------------
@pytest.mark.parametrize("name", sorted(REGISTRY))
def test_generator_chay_duoc_voi_params_rong(name: str) -> None:
    """``build_x({})`` phải chạy được: mọi khoá đều có mặc định hợp lí."""
    _assert_valid(REGISTRY[name]({}))


@pytest.mark.parametrize("name", sorted(REGISTRY))
def test_generator_tat_dinh(name: str) -> None:
    """Gọi hai lần ra chuỗi y hệt — nếu không thì mọi lần build lại kho đều bẩn."""
    assert REGISTRY[name]({}) == REGISTRY[name]({})


# Tham số biên: số 0, số âm, số rất lớn, kiểu sai. Không được nổ, và cũng không
# được lặng lẽ đẩy nét vẽ ra ngoài khung.
BIEN = [
    ("circuit_series", {"resistors": [], "voltmeter": 99}),
    ("circuit_series", {"resistors": ["A"] * 20, "voltmeter": -1}),
    ("circuit_parallel", {"resistors": None}),
    ("circuit_emf", {"caption": None, "emf": ""}),
    ("circuit_rlc", {"elements": ["X", "Y"]}),
    ("circuit_rlc", {"elements": "C"}),
    ("phasor_rlc", {"UR": 0, "UL": 0, "UC": 0}),
    ("phasor_rlc", {"UR": -3, "UL": 1e9, "UC": 0}),
    ("field_point_charge", {"sign": 0, "lines": 0}),
    ("field_point_charge", {"lines": 1e9}),
    ("coulomb_two_charges", {"q1": -1, "q2": -1}),
    ("field_parallel_plates", {"lines": -5, "charge": True, "trajectory": True}),
    ("field_wire", {"current_out": -1}),
    ("field_loop", {"ccw": 0}),
    ("field_solenoid", {"turns": 0}),
    ("field_solenoid", {"turns": 1e6}),
    ("lens_ray", {"f": 0, "d": 10}),
    ("lens_ray", {"f": 6, "d": 0}),
    ("lens_ray", {"f": 6, "d": -4}),
    ("lens_ray", {"f": 6, "d": 6}),           # ảnh ở vô cực
    ("lens_ray", {"f": 1e9, "d": 1}),
    ("lens_ray", {"f": 1e-9, "d": 1e9}),
    ("lens_ray", {"f": -1e6, "d": 1e-6}),
    ("mirror_plane", {"d": 0}),
    ("mirror_plane", {"d": -4}),
    ("reflection_law", {"i": 0}),
    ("reflection_law", {"i": -90}),
    ("reflection_law", {"i": 1e6}),
    ("mirror_spherical", {"f": 0, "so": 5}),
    ("mirror_spherical", {"f": 6, "so": 6}),
    ("mirror_spherical", {"f": -1e9, "so": 1e-9}),
    ("refraction", {"n1": 0, "n2": 0, "i": 0}),
    ("refraction", {"n1": -1.5, "n2": 1, "i": 1e9}),
    ("refraction", {"n1": 1e9, "n2": 1e-9, "i": 89}),
    ("pv_diagram", {"V1": 0, "V2": 0, "p1": 0, "gamma": 0}),
    ("pv_diagram", {"process": "khong-ton-tai"}),
    ("pv_diagram", {"process": "polytropic", "n": -3, "work": True}),
    ("pv_diagram", {"V1": 1e9, "V2": 1e9, "p1": 1e9}),
    ("carnot_cycle", {"T1": 1, "T2": 1e-9, "gamma": 1.0}),
    ("carnot_cycle", {"T1": 0, "T2": 0, "V1": 0, "V2": 0}),
    ("carnot_cycle", {"gamma": 1e9}),
    ("heat_engine", {"mode": "khong-ton-tai"}),
    ("decay_curve", {"cycles": 0}),
    ("decay_curve", {"cycles": -4, "quantity": "X"}),
    ("decay_curve", {"cycles": 1e9, "daughter": True}),
    ("decay_scheme", {"kind": "khong-ton-tai"}),
    ("decay_scheme", {"kind": None}),
]


@pytest.mark.parametrize("name,params", BIEN, ids=lambda v: str(v)[:40])
def test_generator_chiu_duoc_tham_so_bien(name: str, params: dict) -> None:
    _assert_valid(REGISTRY[name](params))


def test_moi_generator_deu_co_trong_bien_test() -> None:
    """Ràng buộc mềm: thêm generator mới thì phải thêm ca biên cho nó."""
    assert set(REGISTRY) - {n for n, _ in BIEN} == set()


# --------------------------------------------------------------------------
# 2. Nội dung hình phải khớp công thức (kiểm bằng số, không kiểm "có vẽ")
# --------------------------------------------------------------------------
@pytest.mark.parametrize("f,d,that,nguoc", [
    (6, 15, True, True),     # d > 2f : ảnh thật, ngược chiều, nhỏ hơn
    (6, 9, True, True),      # f < d < 2f : ảnh thật, ngược chiều, lớn hơn
    (6, 4, False, False),    # d < f : ảnh ảo, cùng chiều, lớn hơn
    (-6, 10, False, False),  # phân kì : luôn ảnh ảo, cùng chiều, nhỏ hơn
])
def test_thau_kinh_dung_ban_chat_anh(f: float, d: float, that: bool, nguoc: bool) -> None:
    """Chú thích hình phải khớp dấu của d′ và k tính từ công thức thấu kính.

    Đây là chỗ dễ sai nhất của cả họ: vẽ ảnh sai vị trí thì người học không có
    cách nào phát hiện, nên phải kiểm bằng chính công thức chứ không bằng mắt.
    """
    dp = d * f / (d - f)
    k = -dp / d
    assert (dp > 0) is that
    assert (k < 0) is nguoc
    svg = REGISTRY["lens_ray"]({"f": f, "d": d})
    _assert_valid(svg)
    txt = _noi_dung(svg)
    assert f"d′ = {_n(round(dp, 2))}" in txt, "hình ghi sai vị trí ảnh"
    assert ("ảnh thật, ngược chiều" if that else "ảnh ảo, cùng chiều") in txt


def test_thau_kinh_ve_anh_dung_toa_do() -> None:
    """Ba tia ló phải đồng quy tại đúng điểm ảnh d′ = df/(d − f), k = −d′/d.

    Kiểm gián tiếp qua mũi tên ảnh: nó phải nằm đúng tỉ lệ (d′/d) so với vật
    trên trục hoành của hình, và cao đúng |k| lần.
    """
    f_, d_ = 6.0, 15.0
    dp = d_ * f_ / (d_ - f_)                     # = 10
    k = -dp / d_                                 # = −2/3
    svg = REGISTRY["lens_ray"]({"f": f_, "d": d_, "h": 3.0})
    root = ET.fromstring(svg)
    # Vật và ảnh là hai mũi tên duy nhất mang lớp accent-c.
    arrows = [el for el in root.iter(f"{SVG_NS}line") if el.get("class") == "accent-c"]
    assert len(arrows) == 2, "phải có đúng hai mũi tên vật và ảnh"
    vat, anh = arrows                            # vật vẽ trước, ảnh vẽ sau
    x_lens = float([el for el in root.iter(f"{SVG_NS}line")
                    if el.get("class") == "ink"][0].get("x1"))
    px_per_unit = (x_lens - float(vat.get("x1"))) / d_
    assert float(anh.get("x1")) == pytest.approx(x_lens + dp * px_per_unit, abs=0.5)
    cao_vat = float(vat.get("y1")) - float(vat.get("y2"))
    cao_anh = float(anh.get("y1")) - float(anh.get("y2"))
    assert cao_anh / cao_vat == pytest.approx(k, abs=0.02)


def test_guong_cau_lom_cho_anh_that_khi_vat_ngoai_tieu_cu() -> None:
    svg = REGISTRY["mirror_spherical"]({"f": 6, "so": 15})
    _assert_valid(svg)
    txt = _noi_dung(svg)
    assert "ảnh thật, ngược chiều" in txt
    assert "s_i = 10" in txt and "m = -0.67" in txt


def test_guong_cau_loi_luon_cho_anh_ao() -> None:
    svg = REGISTRY["mirror_spherical"]({"f": -6, "so": 10})
    assert "ảnh ảo, cùng chiều" in _noi_dung(svg)


def test_khuc_xa_tinh_dung_goc_theo_snell() -> None:
    txt = _noi_dung(REGISTRY["refraction"]({"n1": 1.0, "n2": 1.5, "i": 45}))
    r = math.degrees(math.asin(1.0 * math.sin(math.radians(45)) / 1.5))
    assert f"r = {round(r, 1)}°" in txt
    assert "r < i" in txt, "vào môi trường chiết quang hơn thì r phải nhỏ hơn i"


def test_khuc_xa_tu_chuyen_sang_phan_xa_toan_phan() -> None:
    """n₁ > n₂ và i > i_gh: KHÔNG được vẽ tia khúc xạ nào."""
    txt = _noi_dung(REGISTRY["refraction"]({"n1": 1.5, "n2": 1.0, "i": 50}))
    assert "phản xạ toàn phần" in txt
    assert "sin r" not in txt
    igh = math.degrees(math.asin(1.0 / 1.5))
    assert f"i_gh = {round(igh, 1)}°" in txt


def test_khuc_xa_duoi_goc_gioi_han_van_co_tia_khuc_xa() -> None:
    txt = _noi_dung(REGISTRY["refraction"]({"n1": 1.5, "n2": 1.0, "i": 30}))
    assert "phản xạ toàn phần" not in txt
    assert "r > i" in txt


def test_gian_do_frenen_cong_huong_thi_pha_bang_khong() -> None:
    assert "cộng hưởng: φ = 0" in _noi_dung(REGISTRY["phasor_rlc"]({"resonance": True}))
    assert "cảm kháng" in _noi_dung(REGISTRY["phasor_rlc"]({"UL": 4, "UC": 1}))
    assert "dung kháng" in _noi_dung(REGISTRY["phasor_rlc"]({"UL": 1, "UC": 4}))


def test_decay_curve_doi_ky_hieu_theo_dai_luong() -> None:
    """Công thức về độ phóng xạ H không được dán nhãn trục N/N₀."""
    assert "H / H₀" in _noi_dung(REGISTRY["decay_curve"]({"quantity": "H"}))
    assert "N / N₀" in _noi_dung(REGISTRY["decay_curve"]({"quantity": "N"}))
    assert "m / m₀" in _noi_dung(REGISTRY["decay_curve"]({"quantity": "m"}))


def test_so_do_phan_ra_dung_dinh_luat_bao_toan() -> None:
    assert "ΔZ = -2,  ΔN = -2" in _noi_dung(REGISTRY["decay_scheme"]({"kind": "alpha"}))
    assert "ΔZ = +1,  ΔN = -1" in _noi_dung(REGISTRY["decay_scheme"]({"kind": "beta-"}))
    assert "ΔZ = -1,  ΔN = +1" in _noi_dung(REGISTRY["decay_scheme"]({"kind": "beta+"}))
    assert "số khối A và số proton Z không đổi" in _noi_dung(REGISTRY["decay_scheme"]({"kind": "gamma"}))


def test_mach_chi_chua_tu_thi_khong_ve_r_va_l() -> None:
    """Công thức về dung kháng chỉ nói tới tụ điện — vẽ đủ RLC là sai đề."""
    txt = _noi_dung(REGISTRY["circuit_rlc"]({"elements": ["C"]}))
    assert "u_C" in txt and "u_R" not in txt and "u_L" not in txt


def test_may_lanh_khong_phai_dong_co_nhiet_ve_nguoc_nhan() -> None:
    engine = REGISTRY["heat_engine"]({"mode": "engine"})
    fridge = REGISTRY["heat_engine"]({"mode": "fridge"})
    assert "sinh công" in _noi_dung(engine) and "tiêu thụ" in _noi_dung(fridge)
    assert engine != fridge


# --------------------------------------------------------------------------
# 3. Luật khớp: bắt đúng cái cần bắt
# --------------------------------------------------------------------------
KHOP_DUNG = {
    "physics.thcs.dien-hoc.noi-tiep-dien-tro": "circuit_series",
    "physics.thcs.dien-hoc.song-song-dien-tro": "circuit_parallel",
    "physics.thpt.dong-dien-khong-doi.dinh-luat-om-toan-mach": "circuit_emf",
    "physics.thpt.dien-xoay-chieu.mach-chi-chua-c": "circuit_rlc",
    "physics.thpt.dien-xoay-chieu.tong-tro-rlc": "phasor_rlc",
    "physics.thpt.dien-tich-dien-truong.dien-truong-dien-tich-diem": "field_point_charge",
    "physics.thpt.dien-tich-dien-truong.dinh-luat-coulomb-chan-khong": "coulomb_two_charges",
    "physics.thpt.dien-tich-dien-truong.lien-he-e-u-d": "field_parallel_plates",
    "physics.thpt.tu-truong.cam-ung-tu-dong-dien-thang-dai": "field_wire",
    "physics.thpt.tu-truong.cam-ung-tu-dong-dien-tron": "field_loop",
    "physics.thpt.tu-truong.cam-ung-tu-ong-day": "field_solenoid",
    "physics.thcs.quang-hoc.cong-thuc-thau-kinh": "lens_ray",
    "physics.thcs.quang-hoc.anh-qua-guong-phang": "mirror_plane",
    "physics.thcs.quang-hoc.dinh-luat-phan-xa-anh-sang": "reflection_law",
    "physics.thpt.quang-hinh-quoc-te.guong-cau-quy-uoc-quoc-te": "mirror_spherical",
    "physics.thpt.song-anh-sang.phan-xa-toan-phan": "refraction",
    "physics.thpt.chat-khi.dinh-luat-boyle": "pv_diagram",
    "physics.dai-hoc.nhiet-hoc.chu-trinh-carnot": "carnot_cycle",
    "physics.thpt.nhiet-dong-luc-hoc.hieu-nang-may-lanh": "heat_engine",
    "physics.thpt.hat-nhan.dinh-luat-phong-xa-so-hat": "decay_curve",
    "physics.thpt.hat-nhan.phong-xa-alpha": "decay_scheme",
}


@pytest.mark.parametrize("fid,gen", sorted(KHOP_DUNG.items()))
def test_luat_bat_dung_cong_thuc_dai_dien(kho, fid: str, gen: str) -> None:
    hit = _match(kho[fid])
    assert hit is not None, f"{fid} phải khớp {gen}"
    assert hit[0] == gen


def test_moi_ca_khop_deu_dung_duoc_hinh(kho) -> None:
    """Không luật nào được trỏ tới generator/params mà dựng ra hình hỏng."""
    dung = 0
    for f in kho.values():
        hit = _match(f)
        if hit is None:
            continue
        gen, params, note = hit
        assert gen in REGISTRY, f"{f['id']} trỏ tới generator không tồn tại: {gen}"
        assert note, f"{f['id']} thiếu ghi chú"
        _assert_valid(REGISTRY[gen](params))
        dung += 1
    assert dung >= 100, f"chỉ còn {dung} ca khớp — luật bị nới hoặc bị hụt"


def test_params_khong_dung_chung_o_nho(kho) -> None:
    """Sửa params của một ca không được lây sang ca khác (bảng trả bản sao)."""
    f = kho["physics.thpt.chat-khi.dinh-luat-boyle"]
    _match(f)[1]["process"] = "BAN"
    assert _match(f)[1]["process"] == "isothermal"


# --- ca ÂM: những công thức gần giống mà KHÁC NGHĨA ------------------------
# Mỗi dòng là một cái bẫy thật trong kho: id chứa cùng từ khoá, hoặc cùng chủ
# đề, nhưng hình của họ dienquang sẽ minh hoạ SAI nếu luật bắt phải.
KHONG_DUOC_KHOP = [
    # "dien-tro" xuất hiện trong cả nối tiếp lẫn song song lẫn điện trở dây dẫn
    "physics.thcs.dien-hoc.dien-tro-day-dan",
    "physics.thpt.dong-dien-khong-doi.dien-tro-day-dan",
    "physics.thpt.dong-dien-khong-doi.dien-tro-suat-theo-nhiet-do",
    "physics.thcs.dien-hoc.bien-tro",
    # ghép NGUỒN, không phải ghép điện trở
    "physics.thpt.dong-dien-khong-doi.ghep-nguon-noi-tiep",
    "physics.thpt.dong-dien-khong-doi.ghep-nguon-song-song",
    "physics.thpt.dong-dien-khong-doi.ghep-nguon-hon-hop-doi-xung",
    # Ôm cho đoạn mạch CHỨA NGUỒN / MÁY THU: sơ đồ khác hẳn
    "physics.thpt.dong-dien-khong-doi.dinh-luat-om-doan-mach-chua-nguon",
    "physics.thpt.dong-dien-khong-doi.dinh-luat-om-doan-mach-chua-may-thu",
    # xoay chiều nhưng không phải mạch RLC nối tiếp / giản đồ vectơ
    "physics.thpt.dien-xoay-chieu.may-bien-ap",
    "physics.thpt.dien-xoay-chieu.dong-dien-ba-pha",
    "physics.thpt.dien-xoay-chieu.mac-sao-mac-tam-giac",
    "physics.thpt.dien-xoay-chieu.cong-suat-hao-phi-truyen-tai",
    "physics.thpt.dien-xoay-chieu.tan-so-may-phat-mot-pha",
    "physics.thpt.dien-xoay-chieu.gia-tri-hieu-dung",
    # điện trường nhưng KHÔNG phải điện tích điểm hay hai bản song song
    "physics.thpt.tinh-dien-gauss.dien-truong-day-dai-vo-han",
    "physics.thpt.tinh-dien-gauss.dien-truong-mat-phang-vo-han",
    "physics.thpt.tinh-dien-gauss.dien-truong-vo-cau-dan",
    "physics.thpt.tinh-dien-gauss.dien-truong-trong-qua-cau-dac",
    "physics.thpt.dien-tich-dien-truong.nguyen-li-chong-chat-dien-truong",
    "physics.thpt.dien-tich-dien-truong.tong-hop-hai-vecto-dien-truong",
    # tụ điện phẳng: cùng "hai bản song song" nhưng công thức về điện dung
    "physics.thpt.tu-dien-mach-rc.tu-dien-co-dien-moi-kappa",
    "physics.thpt.tu-dien-mach-rc.luc-hut-giua-hai-ban-tu",
    # từ trường nhưng hình học khác: hai dây song song, hạt chuyển động
    "physics.thpt.tu-truong.luc-tuong-tac-hai-day-song-song",
    "physics.thpt.tu-truong.ban-kinh-quy-dao-tron-trong-tu-truong",
    "physics.thpt.tu-truong.luc-lorentz",
    "physics.thpt.tu-truong.momen-ngau-luc-tu",
    "physics.dai-hoc.tu-truong.dinh-luat-biot-savart-laplace",
    # quang: lăng kính, giao thoa, kính thiên văn — không dựng ảnh thấu kính
    "physics.thpt.song-anh-sang.cong-thuc-lang-kinh",
    "physics.thpt.song-anh-sang.lang-kinh-goc-lech-cuc-tieu",
    "physics.thpt.song-anh-sang.khoang-van",
    "physics.thpt.song-anh-sang.vi-tri-van-sang",
    "physics.thpt.quang-hinh-quoc-te.khuc-xa-qua-mat-cau",
    "physics.thpt.quang-hinh-quoc-te.he-hai-thau-kinh-cach-nhau",
    "physics.thpt.quang-hinh-quoc-te.do-tu-va-ghep-sat-thau-kinh",
    "physics.thpt.quang-hinh-quoc-te.do-boi-giac-kinh-thien-van",
    "physics.thpt.quang-hinh-quoc-te.cong-thuc-nha-lam-kinh-cartesian",
    "physics.thcs.quang-hoc.chieu-cao-guong-toi-thieu",
    "physics.thcs.quang-hoc.kinh-can-thi",
    "physics.thcs.quang-hoc.mat-va-su-dieu-tiet",
    "physics.thcs.quang-hoc.chiet-suat",
    "physics.thpt.song-anh-sang.chiet-suat-tuyet-doi",
    # nhiệt: không phải quá trình trên giản đồ p-V
    "physics.thpt.chat-khi.phuong-trinh-trang-thai",
    "physics.thpt.chat-khi.phuong-trinh-clapeyron-mendeleev",
    "physics.thpt.chat-khi.dinh-luat-dalton",
    "physics.thpt.nhiet-dong-luc-hoc.nguyen-li-i-nhiet-dong-luc-hoc",
    "physics.thpt.nhiet-dong-luc-hoc.nguyen-li-ii-nhiet-dong-luc-hoc",
    "physics.thpt.nhiet-dong-luc-hoc.entropy",
    "physics.dai-hoc.nhiet-hoc.hieu-suat-chu-trinh-otto",
    "physics.dai-hoc.nhiet-hoc.hieu-suat-chu-trinh-diesel",
    "physics.dai-hoc.nhiet-hoc.phuong-trinh-van-der-waals",
    "physics.thcs.nhiet-hoc.hieu-suat-bep-dun",
    "physics.thcs.nhiet-hoc.nhiet-luong-thu-vao",
    # hạt nhân: không phải phân rã theo thời gian, cũng không phải sơ đồ α/β/γ
    "physics.thpt.hat-nhan.phan-hach",
    "physics.thpt.hat-nhan.nhiet-hach",
    "physics.thpt.hat-nhan.nang-luong-lien-ket",
    "physics.thpt.hat-nhan.do-hut-khoi",
    "physics.thpt.hat-nhan.cau-tao-hat-nhan",
    "physics.thpt.hat-nhan.bao-toan-phan-ung-hat-nhan",
    "physics.thpt.hat-nhan.so-hat-nhan-trong-khoi-luong",
    # cái bẫy chuỗi con kinh điển: "sinh" chứa "sin", "phuong" chứa "pH"
    "biology.thcs.chuyen-hoa-thuc-vat.phuong-trinh-quang-hop",
]


@pytest.mark.parametrize("fid", KHONG_DUOC_KHOP)
def test_luat_khong_bat_nham(kho, fid: str) -> None:
    assert fid in kho, f"id ca âm không còn trong kho, cần cập nhật test: {fid}"
    hit = _match(kho[fid])
    assert hit is None, f"luật bắt NHẦM {fid} -> {hit[0] if hit else ''}"


def test_moi_luat_deu_co_it_nhat_mot_ca_am() -> None:
    """Luật nào cũng phải có ca âm; thiếu là chưa chứng minh được nó chặt tay."""
    assert len(KHONG_DUOC_KHOP) >= 2 * len(RD.RULES)


def test_khong_dung_do_voi_matcher_san_co(kho) -> None:
    """Không được phủ chồng lên luật đã có trong ``matcher.py``."""
    from tools.illus.matcher import match_formula

    for f in kho.values():
        if _match(f) is not None:
            assert match_formula(f) is None, f"{f['id']} bị hai bộ luật cùng bắt"


def test_moi_id_trong_bang_luat_deu_ton_tai(kho) -> None:
    """Gõ sai một id thì luật im lặng không bao giờ khớp — bắt lỗi đó ở đây."""
    declared: set[str] = set()
    for name, val in vars(RD).items():
        if name.startswith("_") and name[1:2].isupper() and isinstance(val, dict):
            declared |= set(val)
    declared |= {"physics.thcs.quang-hoc.anh-qua-guong-phang",
                 "physics.thpt.quang-hinh-quoc-te.guong-cau-quy-uoc-quoc-te"}
    assert declared, "không đọc được bảng luật nào"
    assert sorted(d for d in declared if d not in kho) == []
