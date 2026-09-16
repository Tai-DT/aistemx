"""Kiểm thử họ hình Hoá - Sinh: generator không nổ, hình nằm trong khung, luật không bắt nhầm.

Ba nhóm bảo đảm, theo thứ tự quan trọng:

1. **Luật không bắt nhầm.** Một hình sai tệ hơn không có hình, nên phần lớn test ở
   đây là test PHỦ ĐỊNH: với mỗi luật, khẳng định nó trả ``None`` trên những công
   thức THẬT trong kho vốn rất giống công thức đích nhưng khác nghĩa.
2. **Hình vẽ ra hợp lệ và nằm trong ``viewBox``.** Toạ độ tràn khung là lỗi im
   lặng: SVG vẫn hợp lệ, trình duyệt vẫn hiển thị, chỉ mất mất một phần hình.
3. **Tất định.** Gọi hai lần phải ra đúng cùng một chuỗi byte.
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.illus.gen_hoasinh import REGISTRY  # noqa: E402
from tools.illus import rules_hoasinh as R  # noqa: E402

FORMULA_INDEX = ROOT / "data" / "formulas" / "index.json"


# --------------------------------------------------------------------------
# tiện ích
# --------------------------------------------------------------------------
def _vebox(svg: str) -> tuple[float, float]:
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    assert m, "SVG thiếu viewBox"
    return float(m.group(1)), float(m.group(2))


_SO = re.compile(r"-?\d+(?:\.\d+)?")


def _toa_do(svg: str) -> list[tuple[float, float, str]]:
    """Rút mọi điểm hình học ra khỏi SVG để đối chiếu với khung.

    Nhãn chữ chỉ lấy điểm neo (không đo bề rộng glyph vì còn phụ thuộc font),
    nên test này bắt được lỗi đặt hình sai chỗ chứ không bắt được chữ dài tràn ra.
    """
    root = ET.fromstring(svg)
    diem: list[tuple[float, float, str]] = []
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        g = el.attrib.get
        if tag == "line":
            diem += [(float(g("x1")), float(g("y1")), tag), (float(g("x2")), float(g("y2")), tag)]
        elif tag == "rect" and el.attrib.get("class") != "ill-bg":
            x, y = float(g("x")), float(g("y"))
            diem += [(x, y, tag), (x + float(g("width")), y + float(g("height")), tag)]
        elif tag == "circle":
            cx, cy, r = float(g("cx")), float(g("cy")), float(g("r"))
            diem += [(cx - r, cy - r, tag), (cx + r, cy + r, tag)]
        elif tag in ("polyline", "polygon"):
            so = [float(v) for v in _SO.findall(g("points", ""))]
            diem += [(so[i], so[i + 1], tag) for i in range(0, len(so) - 1, 2)]
        elif tag == "path":
            so = [float(v) for v in _SO.findall(g("d", ""))]
            diem += [(so[i], so[i + 1], tag) for i in range(0, len(so) - 1, 2)]
        elif tag == "text":
            diem.append((float(g("x")), float(g("y")), tag))
    return diem


def _kiem_svg(svg: str, ten: str) -> None:
    assert svg.startswith("<svg "), f"{ten}: không phải SVG"
    ET.fromstring(svg)                      # hợp lệ về XML
    assert "<title>" in svg and "<desc>" in svg, f"{ten}: thiếu title/desc cho trình đọc màn hình"
    assert "http://" not in svg.replace('xmlns="http://www.w3.org/2000/svg"', ""), \
        f"{ten}: SVG tham chiếu tài nguyên ngoài"
    w, h = _vebox(svg)
    le = 2.0
    for x, y, tag in _toa_do(svg):
        assert -le <= x <= w + le, f"{ten}: {tag} có x={x} ngoài khung rộng {w}"
        assert -le <= y <= h + le, f"{ten}: {tag} có y={y} ngoài khung cao {h}"


@pytest.fixture(scope="module")
def kho() -> dict[str, dict]:
    if not FORMULA_INDEX.exists():
        pytest.skip("chưa có data/formulas/index.json")
    data = json.loads(FORMULA_INDEX.read_text(encoding="utf-8"))
    return {f["id"]: f for f in data["formulas"]}


def _khop(fid: str, kho: dict[str, dict]):
    f = kho.get(fid, {"id": fid})
    for rule in R.RULES:
        m = rule(f)
        if m:
            return m
    return None


# --------------------------------------------------------------------------
# 1. Generator chạy được với mặc định và với tham số biên
# --------------------------------------------------------------------------
@pytest.mark.parametrize("ten", sorted(REGISTRY))
def test_mac_dinh_chay_duoc(ten):
    _kiem_svg(REGISTRY[ten]({}), ten)


@pytest.mark.parametrize("ten", sorted(REGISTRY))
def test_tat_dinh(ten):
    assert REGISTRY[ten]({}) == REGISTRY[ten]({}), f"{ten}: hai lần gọi ra hai chuỗi khác nhau"


# Bộ tham số biên: 0, số âm, số rất lớn, chuỗi rác, None — mọi khoá số của mọi
# generator đều bị dội qua các giá trị này. Generator được phép vẽ xấu, không
# được phép ném lỗi (nó chạy trong vòng dựng ảnh hàng loạt).
_BIEN = [0, -1, -1e9, 1e12, 1e-12, "rác", None, float("nan"), float("inf")]
_KHOA_SO = ["ea", "ea_xt", "dh", "order", "k", "a0", "tmax", "ca", "cb", "va", "pka",
            "n", "Z", "e", "K", "N0", "r", "vmax", "km", "h", "alpha", "alpha2", "smax"]


@pytest.mark.parametrize("ten", sorted(REGISTRY))
def test_tham_so_bien(ten):
    for khoa in _KHOA_SO:
        for gt in _BIEN:
            svg = REGISTRY[ten]({khoa: gt})
            _kiem_svg(svg, f"{ten}[{khoa}={gt!r}]")


@pytest.mark.parametrize("mode", ["toa", "thu", "ca-hai", "khong-co-mode-nay"])
def test_energy_profile_moi_mode(mode):
    _kiem_svg(REGISTRY["energy_profile"]({"mode": mode, "catalyst": True,
                                          "show_reverse": True}), f"energy_profile/{mode}")


@pytest.mark.parametrize("mode", ["mm", "lineweaver", "eadie", "hanes", "hill", "lung tung"])
@pytest.mark.parametrize("uc_che", ["", "canh-tranh", "khong-canh-tranh", "phi-canh-tranh", "hon-hop"])
def test_enzyme_moi_mode(mode, uc_che):
    _kiem_svg(REGISTRY["enzyme_kinetics"]({"mode": mode, "inhibition": uc_che}), f"{mode}/{uc_che}")


@pytest.mark.parametrize("mode", ["mu", "logistic", "so-sanh", "dndt", "vi-sinh-vat", "?"])
def test_population_moi_mode(mode):
    _kiem_svg(REGISTRY["population_growth"]({"mode": mode, "doubling": True}), mode)


def test_punnett_rong_va_lech_kich_thuoc():
    """Khung Punnett phải chịu được dữ liệu hỏng: thiếu ô, lệch số hàng/cột, rỗng."""
    for p in ({"rows": [], "cols": []},
              {"rows": ["A"], "cols": ["A", "a", "B", "b", "C"]},
              {"rows": ["A", "a"], "cols": ["A", "a"], "cells": [["x"]]},
              {"rows": ["AB", "Ab", "aB", "ab"], "cols": ["AB", "Ab", "aB", "ab"],
               "groups": [{"keys": ["A-B-"], "cls": "fill-a", "label": "9"}]}):
        _kiem_svg(REGISTRY["punnett"](p), f"punnett {p}")


def test_pedigree_du_lieu_thieu():
    for p in ({"parents": []}, {"children": []}, {"parents": [{}], "children": [{}] * 9}):
        _kiem_svg(REGISTRY["pedigree"](p), f"pedigree {p}")


def test_trophic_pyramid_gia_tri_bang_nhau_va_rac():
    for p in ({"levels": []},
              {"levels": [{"label": "a", "value": 5}, {"label": "b", "value": 5}]},
              {"levels": [{"label": "x", "value": "rác"}, {"label": "y", "value": 0}]}):
        _kiem_svg(REGISTRY["trophic_pyramid"](p), f"thap {p}")


# --------------------------------------------------------------------------
# 2. Nội dung phải ĐÚNG, không chỉ hợp lệ
# --------------------------------------------------------------------------
def test_bac_khong_khong_ve_nong_do_am():
    """Phản ứng bậc 0 hết chất tại t = [A]₀/k; kéo dài đường thẳng qua đó là vẽ ra
    nồng độ âm — sai về hoá học mà nhìn đồ thị vẫn thấy "đẹp"."""
    from tools.illus.gen_hoasinh import _nong_do
    assert _nong_do(0, 1.0, 0.5, 1.9) == pytest.approx(0.05)
    assert _nong_do(0, 1.0, 0.5, 2.5) is None


def test_ph_chuan_do_dung_o_cac_moc_chuan():
    """Bộ giải pH phải khớp các mốc lí thuyết, nếu không cả đường cong đều lệch."""
    from tools.illus.gen_hoasinh import _ph_chuan_do
    manh, yeu = 1e6, 10 ** -4.76
    # acid mạnh 0,1 M chưa chuẩn độ: pH = 1
    assert _ph_chuan_do(0.1, 25, 0.1, 0, manh) == pytest.approx(1.0, abs=0.02)
    # acid mạnh - base mạnh tại điểm tương đương: pH = 7
    assert _ph_chuan_do(0.1, 25, 0.1, 25, manh) == pytest.approx(7.0, abs=0.05)
    # acid yếu tại nửa điểm tương đương: pH = pKa
    assert _ph_chuan_do(0.1, 25, 0.1, 12.5, yeu) == pytest.approx(4.76, abs=0.05)
    # acid yếu tại điểm tương đương: base yếu liên hợp nên pH > 7
    assert _ph_chuan_do(0.1, 25, 0.1, 25, yeu) > 8.0
    # pH đơn điệu tăng theo thể tích base
    day = [_ph_chuan_do(0.1, 25, 0.1, v, yeu) for v in range(0, 50)]
    assert all(b > a for a, b in zip(day, day[1:]))


def test_hund_dien_don_truoc_roi_moi_ghep_doi():
    """p³ phải là ba mũi tên đi lên ở ba ô khác nhau, không có ô nào ghép đôi."""
    svg = REGISTRY["orbital_boxes"]({"mode": "hund", "subshell": "p", "e": 3})
    root = ET.fromstring(svg)
    len_up = [el for el in root.iter() if el.tag.endswith("line")
              and el.attrib.get("class") == "accent-a"]
    len_down = [el for el in root.iter() if el.tag.endswith("line")
                and el.attrib.get("class") == "accent-b"]
    assert len(len_up) == 3 and len(len_down) == 0
    svg6 = REGISTRY["orbital_boxes"]({"mode": "hund", "subshell": "p", "e": 6})
    root6 = ET.fromstring(svg6)
    assert len([el for el in root6.iter() if el.tag.endswith("line")
                and el.attrib.get("class") == "accent-b"]) == 3


def test_ket_hop_giao_tu_viet_alen_troi_truoc():
    from tools.illus.gen_hoasinh import _ket_hop, _kieu_hinh
    assert _ket_hop("a", "A") == "Aa"
    assert _ket_hop("A", "a") == "Aa"
    assert _ket_hop("Ab", "aB") == "AaBb"
    assert _ket_hop("ab", "ab") == "aabb"
    assert _kieu_hinh("AaBb") == "A-B-"
    assert _kieu_hinh("aaBb") == "aaB-"
    assert _kieu_hinh("aabb") == "aabb"


def test_punnett_9_3_3_1_to_dung_so_o():
    """Khung 4×4 của AaBb × AaBb phải cho đúng 9 ô A-B-, 3 ô A-bb, 3 ô aaB-."""
    from tools.illus.gen_hoasinh import _ket_hop, _kieu_hinh
    gt = ["AB", "Ab", "aB", "ab"]
    dem: dict[str, int] = {}
    for r in gt:
        for c in gt:
            k = _kieu_hinh(_ket_hop(r, c))
            dem[k] = dem.get(k, 0) + 1
    assert dem == {"A-B-": 9, "A-bb": 3, "aaB-": 3, "aabb": 1}


# --------------------------------------------------------------------------
# 3. Luật khớp: đúng id, và KHÔNG bắt nhầm
# --------------------------------------------------------------------------
def _moi_id_khai_bao() -> set[str]:
    ids: set[str] = set()
    for bang in (R._GIAN_DO_NL, R._BAC_DONG_HOC, R._BAN_HUY, R._CHUAN_DO, R._MUC_NL,
                 R._O_LUONG_TU, R._PIN, R._PUNNETT, R._PHA_HE, R._TANG_TRUONG,
                 R._ENZYME, R._THAP, R._DONG_NL):
        ids |= set(bang)
    ids |= {"chemistry.dai-hoc.cau-tao-chat.ban-kinh-bohr",
            "chemistry.thpt.dong-hoc-tich-phan.do-thi-tuyen-tinh-xac-dinh-bac"}
    return ids


def test_moi_id_trong_luat_deu_ton_tai(kho):
    """Id gõ sai sẽ im lặng không khớp gì cả — chỉ test này phát hiện được."""
    thieu = sorted(i for i in _moi_id_khai_bao() if i not in kho)
    assert not thieu, f"id không có trong kho: {thieu}"


def test_luat_chi_khop_dung_cac_id_da_khai_bao(kho):
    """Chốt chặn quan trọng nhất: quét TOÀN kho, tập id khớp được phải trùng khít
    tập id đã khai báo. Ai nới luật thành khớp chuỗi con sẽ làm test này đỏ."""
    khop = {fid for fid, f in kho.items() if _khop(fid, kho)}
    assert khop == _moi_id_khai_bao()


def test_moi_ca_khop_deu_dung_generator_co_that_va_ve_duoc(kho):
    for fid in sorted(_moi_id_khai_bao()):
        m = _khop(fid, kho)
        assert m is not None, fid
        gen, params, note = m
        assert gen in REGISTRY, f"{fid}: generator {gen} không tồn tại"
        assert note.strip(), f"{fid}: thiếu ghi chú"
        _kiem_svg(REGISTRY[gen](params), f"{fid} -> {gen}")


# Các công thức THẬT trong kho, rất giống công thức đích nhưng khác nghĩa.
# Nếu một luật nào đó bắt phải chúng thì người học sẽ nhận một hình sai hoàn toàn.
_GAN_GIONG_NHUNG_KHAC = [
    # nhiệt hoá: chu trình Hess và Arrhenius KHÔNG phải giản đồ E_a - ΔH một bước
    "chemistry.thpt.nhiet-hoa.dinh-luat-hess",
    "chemistry.thpt.nhiet-hoa.enthalpy-phan-ung-nghich",
    "chemistry.thpt.nhiet-hoa.nang-luong-tu-do-gibbs",
    "chemistry.dai-hoc.dong-hoa-hoc.arrhenius-dang-mu",
    "chemistry.thpt.toc-do.phuong-trinh-arrhenius",
    # động học: bậc 3, bậc n, bậc 2 hai chất khác nồng độ — đường cong khác hẳn
    "chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-3",
    "chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-n",
    "chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-2-khac-nong-do",
    "chemistry.dai-hoc.dong-hoa-hoc.phan-ung-noi-tiep",
    "chemistry.dai-hoc.dong-hoa-hoc.phan-ung-song-song",
    "chemistry.thpt.dong-hoc-tich-phan.ban-huy-lien-tiep-khong-doi",
    "chemistry.thpt.toc-do.bac-phan-ung",
    # pH: tính pH của một dung dịch KHÔNG phải là đường chuẩn độ
    "chemistry.thpt.dien-li.ph-cua-acid-yeu",
    "chemistry.thpt.dien-li.ph-cua-dung-dich",
    "chemistry.thpt.dien-li.ph-dung-dich-dem-base",
    "chemistry.thpt.dien-li.tich-so-tan",
    "chemistry.dai-hoc.hoa-phan-tich.ph-axit-yeu",
    "chemistry.dai-hoc.hoa-phan-tich.dung-luong-dem",
    # chuẩn độ khác loại: kết tủa, complexon, oxi hoá - khử, hai bước nhảy
    "chemistry.dai-hoc.hoa-phan-tich.chuan-do-ket-tua",
    "chemistry.dai-hoc.hoa-phan-tich.chuan-do-complexon",
    "chemistry.dai-hoc.hoa-phan-tich.the-tai-diem-tuong-duong",
    "chemistry.thpt.icho-can-bang.tach-hai-buoc-nhay-chuan-do",
    # nguyên tử: hộp thế, Klechkovski, cấu hình ngoại lệ — hình khác
    "chemistry.dai-hoc.hoa-luong-tu.hat-trong-hop-1d-muc-nang-luong",
    "chemistry.thpt.nguyen-tu.quy-tac-klechkovski",
    "chemistry.thpt.nguyen-tu.cau-hinh-electron-ion",
    "chemistry.thpt.cau-tao-quoc-te.cau-hinh-electron-ngoai-le",
    "chemistry.thpt.nguyen-tu.nang-luong-ion-hoa",
    # Bohr / Rydberg bên VẬT LÍ: họ khác quản, không được lấn sang
    "physics.thpt.luong-tu-anh-sang.cong-thuc-rydberg",
    "physics.thpt.vat-li-hien-dai-qt.luong-tu-hoa-momen-dong-luong-bohr",
    "physics.dai-hoc.luong-tu.ban-kinh-bohr-va-quang-pho-hidro",
    # điện hoá: điện phân và điện cực đơn lẻ KHÔNG phải sơ đồ pin hai nửa
    "chemistry.thpt.dien-hoa.dinh-luat-faraday",
    "chemistry.thpt.dien-hoa.phuong-trinh-nernst",
    "chemistry.thpt.dien-hoa-quoc-te.dien-cuc-hidro-chuan",
    "chemistry.thpt.dien-hoa-quoc-te.so-sanh-pin-galvani-va-binh-dien-phan",
    "chemistry.dai-hoc.dien-hoa-hoc.dien-cuc-loai-1",
    # di truyền: công thức đếm tổng quát cho n cặp gen, không vẽ được bằng 1 khung
    "biology.thpt.quy-luat-di-truyen.ti-le-kieu-gen-tong-quat",
    "biology.thpt.quy-luat-di-truyen.ti-le-kieu-hinh-tong-quat",
    "biology.thpt.quy-luat-di-truyen.so-loai-giao-tu-n-cap-di-hop",
    "biology.thpt.quy-luat-di-truyen.so-loai-kieu-gen-doi-con",
    "biology.thpt.quy-luat-di-truyen.tan-so-hoan-vi-gen",
    "biology.thpt.quy-luat-di-truyen.ti-le-giao-tu-hoan-vi",
    "biology.thpt.quy-luat-di-truyen.di-truyen-ngoai-nhan",
    "biology.thpt.di-truyen-quan-the.dieu-kien-hardy-weinberg",
    "biology.thpt.di-truyen-quan-the.hardy-weinberg-nhieu-alen",
    "biology.thpt.di-truyen-quan-the.gen-tren-nst-gioi-tinh-x",
    "biology.thpt.di-truyen-nguoi.xac-suat-sinh-con-theo-gioi-tinh",
    "biology.thpt.di-truyen-nguoi.chi-so-iq",
    # quần thể: mô hình rời rạc và mô hình nhiều loài — đường cong khác
    "biology.dai-hoc.ibo-sinh-thai.mo-hinh-ricker",
    "biology.dai-hoc.ibo-sinh-thai.mo-hinh-beverton-holt",
    "biology.dai-hoc.sinh-thai-hoc.lotka-volterra-canh-tranh",
    "biology.dai-hoc.sinh-thai-hoc.mo-hinh-sir",
    "biology.thpt.sinh-thai.kich-thuoc-quan-the",
    "biology.thpt.sinh-thai-intl.thoi-gian-nhan-doi-quy-tac-70",
    "biology.thpt.vi-sinh-vat.so-te-bao-sau-n-lan-phan-chia",
    # enzyme: các phép tuyến tính hoá / hằng số khác, trục khác hẳn
    "biology.dai-hoc.dong-hoc-enzyme.do-thi-hill",
    "biology.dai-hoc.dong-hoc-enzyme.scatchard",
    "biology.dai-hoc.dong-hoc-enzyme.cheng-prusoff",
    "biology.dai-hoc.dong-hoc-enzyme.km-briggs-haldane",
    "biology.dai-hoc.dong-hoc-enzyme.so-vong-quay-kcat",
    "biology.dai-hoc.dong-hoc-enzyme.hang-so-uc-che-ki",
    "chemistry.dai-hoc.dong-hoa-hoc.xuc-tac-di-the-langmuir-hinshelwood",
    # sinh thái: chỉ số đa dạng, không liên quan tháp năng lượng
    "biology.thpt.sinh-thai.chi-so-simpson",
    "biology.thpt.sinh-thai.do-da-dang-shannon",
    "biology.thpt.sinh-thai.mat-do-ca-the",
    "biology.thpt.sinh-thai-intl.dau-chan-sinh-thai",
    "biology.dai-hoc.sinh-thai-hoc.duong-cong-loai-dien-tich",
    "biology.dai-hoc.sinh-thai-hoc.nguong-mien-dich-cong-dong",
]


@pytest.mark.parametrize("fid", _GAN_GIONG_NHUNG_KHAC)
def test_khong_bat_nham_cong_thuc_gan_giong(fid, kho):
    assert fid in kho, f"id ví dụ không còn trong kho, cần cập nhật test: {fid}"
    hit = _khop(fid, kho)
    assert hit is None, f"{fid} bị {hit[0]} bắt nhầm — đây là công thức khác nghĩa"


def test_khong_lan_sang_mon_khac(kho):
    """Họ này chỉ nhận Hoá và Sinh; lấn sang Toán/Lí là giẫm chân họ hình khác."""
    for fid, f in kho.items():
        if f.get("subject") not in ("chemistry", "biology"):
            assert _khop(fid, kho) is None, f"{fid} ({f.get('subject')}) bị bắt nhầm"
