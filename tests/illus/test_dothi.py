"""Kiểm thử họ **dothi** (đồ thị hàm số và giải tích).

Ba nhóm kiểm tra, xếp theo mức độ nguy hiểm của lỗi mà chúng chặn:

1. **Luật khớp không được bắt nhầm.** Một hình sai dán lên công thức đúng là lỗi
   người học không có cách nào phát hiện, nên phần lớn test ở đây là *khẳng định
   phủ định*: với mỗi luật, vài công thức có thật trong kho, nhìn rất giống,
   nhưng khác nghĩa — luật phải trả None.
2. **Hình không được tràn khung.** SVG tràn viewBox không báo lỗi, chỉ mất một
   mẩu hình; không test thì không ai thấy.
3. **Generator không được nổ** với tham số rác, và phải tất định.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.illus.gen_dothi import REGISTRY  # noqa: E402
from tools.illus.matcher import match_formula as match_cu  # noqa: E402
from tools.illus.rules_dothi import (  # noqa: E402
    RULES, _AREA, _ASYMPTOTE, _CUBIC, _DECAY, _DERIV, _EXPLOG, _GROWTH,
    _INTERSECT, _LIMIT, _LOGISTIC, _MAXMIN, _MONOTONE, _PARABOLA, _RIEMANN,
    _SHAPE, r_area, r_asymptote, r_cubic, r_decay, r_derivative, r_exp_log,
    r_growth, r_intersect, r_limit, r_logistic, r_max_min, r_monotone,
    r_parabola, r_riemann, r_shape,
)

BANG = [_CUBIC, _MONOTONE, _MAXMIN, _PARABOLA, _ASYMPTOTE, _INTERSECT, _EXPLOG,
        _GROWTH, _DECAY, _LOGISTIC, _SHAPE, _LIMIT, _DERIV, _AREA, _RIEMANN]


# ---------------------------------------------------------------------------
# Dữ liệu dùng chung
# ---------------------------------------------------------------------------
@pytest.fixture(scope="module")
def kho() -> dict[str, dict]:
    data = json.loads((ROOT / "data" / "formulas" / "index.json").read_text(encoding="utf-8"))
    return {f["id"]: f for f in data["formulas"]}


def ct(kho: dict[str, dict], formula_id: str) -> dict:
    """Lấy công thức THẬT trong kho; id sai thì fail ngay, để test không mục ruỗng."""
    assert formula_id in kho, f"id không có trong kho: {formula_id}"
    return kho[formula_id]


def khop(f: dict):
    for rule in RULES:
        m = rule(f)
        if m:
            return m
    return None


# ---------------------------------------------------------------------------
# Tiện ích đọc SVG
# ---------------------------------------------------------------------------
_ATTR_X = ("x", "cx", "x1", "x2")
_ATTR_Y = ("y", "cy", "y1", "y2")


def diem_ngoai_khung(svg: str) -> list[tuple]:
    """Mọi toạ độ tuyệt đối trong SVG phải nằm trong viewBox (dung sai 0,5 px)."""
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    assert m, "SVG thiếu viewBox"
    w, h = float(m.group(1)), float(m.group(2))
    xau: list[tuple] = []
    for tag in re.findall(r"<[^>]+>", svg):
        for attr in _ATTR_X + _ATTR_Y:
            for raw in re.findall(rf'\b{attr}="(-?[\d.]+)"', tag):
                v = float(raw)
                gioi_han = w if attr in _ATTR_X else h
                if not -0.5 <= v <= gioi_han + 0.5:
                    xau.append((tag[:60], attr, v, gioi_han))
        pts = re.search(r'points="([^"]+)"', tag)
        if pts:
            for cap in pts.group(1).split():
                px, py = (float(v) for v in cap.split(","))
                if not (-0.5 <= px <= w + 0.5 and -0.5 <= py <= h + 0.5):
                    xau.append((tag[:60], "points", px, py))
    return xau


def kiem_svg(svg: str) -> None:
    assert svg.startswith("<svg ") and svg.endswith("</svg>")
    assert "<title>" in svg and "<desc>" in svg, "thiếu title/desc cho trình đọc màn hình"
    assert svg.count("<svg") == svg.count("</svg>") == 1
    assert not diem_ngoai_khung(svg)


# Tham số rác: rule có thể truyền vào bất cứ thứ gì, hình vẫn phải dựng được.
THAM_SO_BIEN = [
    {},
    dict.fromkeys(
        ("a", "b", "c", "d", "k", "m", "n", "L", "T", "m0", "y0", "p0", "x0", "h",
         "dx", "base", "r", "q", "tmax", "cycles", "periods", "half_width", "range",
         "xmin", "xmax", "ymin", "ymax"), 0),
    dict.fromkeys(
        ("a", "b", "c", "d", "k", "m", "n", "L", "T", "m0", "y0", "p0", "x0", "h",
         "dx", "base", "r", "q", "tmax", "cycles", "periods", "half_width", "range",
         "xmin", "xmax"), -7),
    dict.fromkeys(
        ("a", "b", "c", "d", "k", "m", "L", "T", "m0", "y0", "p0", "x0", "h", "dx",
         "base", "r", "q", "tmax", "half_width", "range", "xmin", "xmax"), 1e9),
    {"expr": "", "f": "", "g": "", "left": "", "right": "", "lower": "", "upper": "",
     "middle": "", "even": "", "odd": ""},
    {"expr": "import os", "f": "x)(", "g": None, "left": [], "right": {},
     "middle": "os.system('x')"},
    {"pieces": "không phải danh sách", "partition": "abc", "splits": "xyz",
     "part_labels": 5, "critical": "vài điểm", "mode": "không-có-mode",
     "kind": 12, "mark": None, "label": 3.14, "discrete": True, "signed": True},
    {"n": 10 ** 6, "periods": 10 ** 6, "cycles": 10 ** 6, "expr": "1/x", "a": -1, "b": 1},
]


# ---------------------------------------------------------------------------
# 1. Generator: chạy được, không tràn khung, tất định
# ---------------------------------------------------------------------------
@pytest.mark.parametrize("ten", sorted(REGISTRY))
def test_generator_chay_voi_mac_dinh(ten):
    kiem_svg(REGISTRY[ten]({}))


@pytest.mark.parametrize("params", THAM_SO_BIEN)
@pytest.mark.parametrize("ten", sorted(REGISTRY))
def test_generator_chiu_duoc_tham_so_bien(ten, params):
    kiem_svg(REGISTRY[ten](dict(params)))


@pytest.mark.parametrize("ten", sorted(REGISTRY))
def test_svg_tat_dinh(ten):
    assert REGISTRY[ten]({}) == REGISTRY[ten]({})
    rac = THAM_SO_BIEN[6]
    assert REGISTRY[ten](dict(rac)) == REGISTRY[ten](dict(rac))


@pytest.mark.parametrize("ten", sorted(REGISTRY))
def test_khong_tham_chieu_tai_nguyen_ngoai(ten):
    svg = REGISTRY[ten]({})
    assert "href" not in svg and "<image" not in svg and "url(" not in svg
    assert svg.count("http") == 1      # đúng một lần: khai báo xmlns


def test_duong_cong_bi_cat_theo_bien_khung():
    """Nhánh tiệm cận phải chạy tới sát biên khung, không dừng sớm.

    Nếu cắt kiểu "lọc điểm ngoài dải" thay vì cắt theo tham số, giữa đường cong
    và mép khung sẽ hở ra một khoảng trắng — nhìn như hàm ngừng tồn tại ở đó.
    """
    svg = REGISTRY["rational"]({"a": 1, "b": 2, "c": 1, "d": -1})
    h = float(re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).group(2))
    ys = [float(y) for tag in re.findall(r'<polyline points="([^"]+)"', svg)
          for _, y in (cap.split(",") for cap in tag.split())]
    assert min(ys) < 40 and max(ys) > h - 60, "nhánh tiệm cận không chạm biên khung"


def test_khong_sinh_nghiem_gia_o_cho_ham_bang_khong():
    """y = x³−3x cắt đường y = 1 đúng ba lần, không phải bốn.

    Bản đầu tiên viết ``_at(fn, x) or m`` nên giá trị 0.0 hợp lệ bị nuốt và
    x = 0 hiện ra như một nghiệm — hình vẽ thừa hẳn một giao điểm.
    """
    svg = REGISTRY["horizontal_cut"]({"expr": "x^3-3*x", "m": 1})
    assert len(re.findall(r'class="accent-d"', svg)) == 3


def test_khong_sinh_giao_diem_gia_o_mien_khong_xac_dinh():
    """log₂x = 2 chỉ có một nghiệm; miền x ≤ 0 không được đẻ ra giao điểm."""
    svg = REGISTRY["horizontal_cut"](
        {"expr": "log(x)/log(2)", "m": 2, "xmin": -0.6, "xmax": 6})
    assert len(re.findall(r'class="accent-d"', svg)) == 1


def test_ham_cho_theo_tung_khoang_khong_cham_bua():
    """Mối nối liền nét (|x| tại 0) không được có chấm; mối nối nhảy thì phải có."""
    rong = re.compile(r'<circle[^>]*style="fill:none"')
    lien = REGISTRY["piecewise"]({})                        # mặc định là y = |x|
    assert not rong.search(lien) and "<circle" not in lien
    nhay = REGISTRY["piecewise"]({"pieces": [
        {"expr": "1", "from": -2, "to": 0},
        {"expr": "2", "from": 0, "to": 2, "open_left": True}]})
    assert rong.search(nhay), "mối nối có bước nhảy phải có đầu mút rỗng"
    assert "<circle" in nhay.replace(rong.search(nhay).group(0), "", 1), "thiếu đầu mút đặc"


# ---------------------------------------------------------------------------
# 2. Luật: đúng id, không trùng, không đụng matcher cũ
# ---------------------------------------------------------------------------
def test_moi_id_trong_luat_deu_ton_tai_trong_kho(kho):
    """id gõ sai = luật chết lặng lẽ: không khớp gì mà cũng không ai biết."""
    thieu = [fid for bang in BANG for fid in bang if fid not in kho]
    assert not thieu, f"id không có trong kho: {thieu}"


def test_khong_hai_luat_cung_bat_mot_id():
    da_gap: dict[str, int] = {}
    trung = []
    for i, bang in enumerate(BANG):
        for fid in bang:
            if fid in da_gap:
                trung.append(fid)
            da_gap[fid] = i
    assert not trung, f"id bị hai bảng cùng nhận: {trung}"


def test_khong_dung_do_voi_matcher_hien_co(kho):
    """Không được giành công thức mà matcher.py đã có hình."""
    dung = [fid for bang in BANG for fid in bang if match_cu(kho[fid])]
    assert not dung, f"đụng độ với matcher.py: {dung}"


def test_moi_luat_dung_generator_co_that_va_dung_duoc(kho):
    for bang in BANG:
        for fid, (gen, params, note) in bang.items():
            assert gen in REGISTRY, f"{fid}: generator không tồn tại: {gen}"
            assert note, f"{fid}: thiếu ghi chú"
            svg = REGISTRY[gen](dict(params))
            kiem_svg(svg)
            assert svg == REGISTRY[gen](dict(params)), f"{fid}: hình không tất định"


def test_so_cong_thuc_khop_dung_bang_tong_so_muc_trong_bang(kho):
    """Luật chỉ được khớp đúng những id đã liệt kê — không lan ra chỗ khác."""
    khop_duoc = [fid for fid, f in kho.items() if khop(f)]
    assert len(khop_duoc) == sum(len(b) for b in BANG)


# ---------------------------------------------------------------------------
# 3. Luật KHÔNG được bắt nhầm (ca gần giống, id có thật trong kho)
# ---------------------------------------------------------------------------
# (luật, id công thức gần giống, vì sao hình sẽ sai nếu bắt)
CA_GAN_GIONG = [
    # "tâm đối xứng" của phân thức không phải điểm uốn của bậc ba
    (r_cubic, "math.thpt.ung-dung-dao-ham.tam-doi-xung-phan-thuc"),
    (r_cubic, "math.thpt.ham-so-bac-nhat-bac-hai.toa-do-dinh-parabol"),
    # bậc ba đơn điệu đi vào hình bậc ba, không đi vào bảng dấu f′
    (r_monotone, "math.thpt.ung-dung-dao-ham.dieu-kien-don-dieu-ham-bac-ba"),
    (r_monotone, "math.thpt.ham-so-bac-nhat-bac-hai.dong-bien-nghich-bien-dinh-nghia"),
    (r_max_min, "math.thpt.ham-so-bac-nhat-bac-hai.gtln-gtnn-ham-bac-hai"),
    # công thức nghiệm thu gọn nói về Δ′, hình parabol không nói được điều đó
    (r_parabola, "math.thpt.ham-so-bac-nhat-bac-hai.cong-thuc-nghiem-thu-gon"),
    (r_parabola, "math.thpt.ham-so-bac-nhat-bac-hai.dinh-li-viete"),
    # dấu tam thức gồm ba trường hợp Δ; một parabol chỉ vẽ được một
    (r_parabola, "math.thpt.ham-so-bac-nhat-bac-hai.dau-tam-thuc-bac-hai"),
    (r_parabola, "math.thpt.ham-so-bac-nhat-bac-hai.dau-nhi-thuc-bac-nhat"),
    # đạo hàm của hàm phân thức KHÔNG phải đồ thị hàm phân thức
    (r_asymptote, "math.thpt.dao-ham.dao-ham-phan-thuc-bac-nhat"),
    (r_asymptote, "math.thpt.gioi-han.dang-vo-dinh-vo-cung-tren-vo-cung"),
    # bất phương trình mũ không đọc bằng một giao điểm
    (r_intersect, "math.thpt.mu-logarit.bat-phuong-trinh-mu"),
    (r_intersect, "math.thpt.mu-logarit.phuong-trinh-mu-cung-co-so"),
    (r_exp_log, "math.thpt.mu-logarit.doi-co-so-logarit"),
    (r_exp_log, "math.thpt.mu-logarit.logarit-cua-tich"),
    # ΔN = N₀(1 − 2^(−t/T)) là đường ĐI LÊN, dán hình phân rã vào là vẽ ngược
    (r_decay, "physics.thpt.hat-nhan.so-hat-nhan-da-phan-ra"),
    (r_decay, "math.thpt.mu-logarit.tinh-chat-luy-thua"),
    (r_growth, "math.thpt.ptvp-quoc-te.ptvp-logistic"),
    (r_growth, "math.thpt.mu-logarit.tinh-chat-co-ban-logarit"),
    (r_logistic, "math.thpt.ptvp-quoc-te.ptvp-tang-truong-mu"),
    # Lí/Sinh có hình riêng của họ chuyên môn — họ dothi không được với sang
    (r_growth, "biology.thpt.sinh-thai.tang-truong-mu-theo-thoi-gian"),
    (r_logistic, "biology.dai-hoc.sinh-thai-hoc.tang-truong-logistic"),
    (r_decay, "physics.thpt.hat-nhan.dinh-luat-phong-xa-so-hat"),
    (r_area, "physics.thpt.dong-hoc.dien-tich-do-thi-van-toc-thoi-gian"),
    (r_derivative, "physics.thpt.dong-hoc.do-doc-do-thi-do-dich-chuyen-thoi-gian"),
    # |a| ở lớp 6–7 là khoảng cách trên trục số, không phải đồ thị hàm
    (r_shape, "math.thcs.so-nguyen.gia-tri-tuyet-doi"),
    (r_shape, "math.thcs.so-nguyen.tinh-chat-gia-tri-tuyet-doi"),
    # "giới hạn" trong xác suất là chuyện hoàn toàn khác
    (r_limit, "math.dai-hoc.dinh-li-gioi-han.dinh-li-gioi-han-trung-tam"),
    (r_limit, "math.dai-hoc.dinh-li-gioi-han.luat-so-lon-yeu"),
    (r_limit, "math.thpt.gioi-han.gioi-han-tai-vo-cuc"),
    (r_limit, "math.dai-hoc.giai-tich-thuc.dinh-nghia-epsilon-delta-gioi-han-ham"),
    (r_limit, "math.thpt.gioi-han.dinh-li-gioi-han-ham-so"),
    # vi phân cấp n và đạo hàm cấp hai không vẽ được bằng hình dy/Δy
    (r_derivative, "math.dai-hoc.dao-ham.vi-phan-cap-n"),
    (r_derivative, "math.thpt.dao-ham.dao-ham-cap-hai"),
    (r_derivative, "math.thpt.dao-ham.van-toc-tuc-thoi"),
    # thể tích tròn xoay là hình 3D; diện tích theo biến y cắt ngang, không cắt dọc
    (r_area, "math.thpt.nguyen-ham-tich-phan.the-tich-tron-xoay-ox"),
    (r_area, "math.thpt.nguyen-ham-tich-phan.dien-tich-hinh-phang-theo-bien-y"),
    (r_area, "math.dai-hoc.ung-dung-tich-phan.dien-tich-toa-do-cuc"),
    # Simpson dùng cung parabol, sai số thì không có gì để vẽ
    (r_riemann, "math.thpt.tong-riemann.quy-tac-simpson"),
    (r_riemann, "math.thpt.tong-riemann.sai-so-quy-tac-hinh-thang"),
    (r_riemann, "math.thpt.tong-riemann.uoc-luong-theo-tinh-loi-lom"),
    (r_riemann, "math.dai-hoc.giai-tich-thuc.tong-darboux"),
]


@pytest.mark.parametrize("rule,formula_id", CA_GAN_GIONG,
                         ids=[f"{r.__name__}:{i.split('.')[-1]}" for r, i in CA_GAN_GIONG])
def test_luat_khong_bat_nham(kho, rule, formula_id):
    assert rule(ct(kho, formula_id)) is None


@pytest.mark.parametrize("formula_id", [i for _, i in CA_GAN_GIONG])
def test_ca_gan_giong_khong_bi_luat_nao_khac_vo_tinh_bat(kho, formula_id):
    """Không luật nào trong họ được nhận các ca gần giống ở trên."""
    ngoai_le = {
        # những id này CÓ hình, nhưng phải là hình khác với luật đang thử ở trên
        "math.thpt.ung-dung-dao-ham.tam-doi-xung-phan-thuc",
        "math.thpt.ham-so-bac-nhat-bac-hai.toa-do-dinh-parabol",
        "math.thpt.ung-dung-dao-ham.dieu-kien-don-dieu-ham-bac-ba",
        "math.thpt.ham-so-bac-nhat-bac-hai.dong-bien-nghich-bien-dinh-nghia",
        "math.thpt.ham-so-bac-nhat-bac-hai.gtln-gtnn-ham-bac-hai",
        "math.thpt.ptvp-quoc-te.ptvp-logistic",
        "math.thpt.ptvp-quoc-te.ptvp-tang-truong-mu",
    }
    if formula_id in ngoai_le:
        pytest.skip("ca này có hình riêng, đã kiểm ở test_luat_khong_bat_nham")
    assert khop(ct(kho, formula_id)) is None


# ---------------------------------------------------------------------------
# 4. Luật bắt ĐÚNG những ca xương sống (hỏng là biết ngay)
# ---------------------------------------------------------------------------
CA_PHAI_BAT = [
    ("math.thpt.ung-dung-dao-ham.dieu-kien-ham-bac-ba-co-cuc-tri", "cubic"),
    ("math.thpt.ung-dung-dao-ham.tiem-can-xien", "oblique_asymptote"),
    ("math.thpt.ung-dung-dao-ham.tiem-can-ngang", "limit_infinity"),
    ("math.thpt.dao-ham.phuong-trinh-tiep-tuyen", "tangent_line"),
    ("math.thpt.dao-ham.dinh-nghia-dao-ham", "secant_tangent"),
    ("math.thpt.nguyen-ham-tich-phan.dien-tich-hinh-phang-hai-duong", "area_between"),
    ("math.thpt.tong-riemann.tong-riemann-trai", "riemann_sum"),
    ("math.thpt.gioi-han.gioi-han-sinx-tren-x", "limit_hole"),
    ("math.thpt.mu-logarit.chu-ki-ban-ra", "half_life"),
    ("math.thpt.ptvp-quoc-te.nghiem-logistic", "logistic"),
]


@pytest.mark.parametrize("formula_id,gen", CA_PHAI_BAT,
                         ids=[i.split(".")[-1] for i, _ in CA_PHAI_BAT])
def test_luat_bat_dung_ca_xuong_song(kho, formula_id, gen):
    m = khop(ct(kho, formula_id))
    assert m is not None and m[0] == gen


def test_ho_dothi_chi_nhan_cong_thuc_mon_toan(kho):
    """Ranh giới với các họ chuyên môn: đồ thị Lí/Sinh là phần của họ khác.

    Hai họ cùng nhận một công thức thì hình phụ thuộc thứ tự nạp module — đổi
    thứ tự là hình đổi theo mà không ai sửa luật nào.
    """
    ngoai_toan = [fid for bang in BANG for fid in bang if kho[fid]["subject"] != "math"]
    assert not ngoai_toan, f"id không thuộc môn Toán: {ngoai_toan}"


def test_moi_generator_duoc_luat_dung_deu_co_trong_registry():
    dung = {gen for bang in BANG for gen, _, _ in bang.values()}
    assert dung <= set(REGISTRY)
