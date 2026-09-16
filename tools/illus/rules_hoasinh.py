"""Luật gán generator hình Hoá - Sinh cho công thức.

Cùng chữ ký với ``matcher.py``: mỗi luật nhận dict công thức, trả
``(tên_generator, params, ghi_chú)`` hoặc ``None``.

Ở họ này luật khớp theo **id đầy đủ**, không theo chuỗi con. Lý do: các hình
Hoá - Sinh gắn rất chặt với NỘI DUNG của từng công thức chứ không với một dạng
toán chung — khung Punnett 4×4 cho tương tác 9:6:1 và cho tương tác 9:7 chỉ khác
nhau ở cách gộp ô, còn "đường cong chuẩn độ acid mạnh" và "acid yếu" là hai hình
khác hẳn. Khớp lỏng theo chủ đề (mọi công thức trong "Động hóa học", mọi công
thức chứa ``ph``) sẽ dán nhầm hình cho hàng chục công thức mà bảng thống kê vẫn
đẹp — đúng kiểu sai nguy hiểm nhất, vì người học không có cách nào phát hiện.

Mỗi id ở đây đều đã được đọc kèm ``latex`` trước khi đưa vào (xem
``tests/illus/test_hoasinh.py::test_moi_id_trong_luat_deu_ton_tai``).
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _id(f: dict) -> str:
    return f.get("id", "")


# --------------------------------------------------------------------------
# HOÁ — giản đồ năng lượng, động học
# --------------------------------------------------------------------------
_GIAN_DO_NL: dict[str, tuple[dict, str]] = {
    "chemistry.thpt.nhiet-hoa.dau-cua-bien-thien-enthalpy":
        ({"mode": "ca-hai"}, "dấu ΔH: toả nhiệt và thu nhiệt"),
    "chemistry.thpt.dong-hoc-tich-phan.nang-luong-hoat-hoa-phan-ung-nghich":
        ({"mode": "toa", "show_reverse": True}, "Ea nghịch = Ea thuận − ΔH"),
    "chemistry.dai-hoc.dong-hoa-hoc.xuc-tac-giam-nang-luong-hoat-hoa":
        ({"mode": "toa", "catalyst": True}, "xúc tác hạ hàng rào năng lượng hoạt hoá"),
}


def r_gian_do_nang_luong(f: dict) -> Optional[Match]:
    hit = _GIAN_DO_NL.get(_id(f))
    return ("energy_profile", hit[0], hit[1]) if hit else None


# Bậc phản ứng suy từ id, không suy từ latex: "bậc 2" trong latex hiện ra dưới
# nhiều dạng (1/[A], [A]^2, hệ số 2kt) nên đọc latex dễ nhận nhầm bậc.
_BAC_DONG_HOC: dict[str, int] = {
    "chemistry.thpt.dong-hoc-tich-phan.bac-khong": 0,
    "chemistry.thpt.dong-hoc-tich-phan.bac-mot": 1,
    "chemistry.thpt.dong-hoc-tich-phan.bac-hai": 2,
    "chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-0": 0,
    "chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-1": 1,
    "chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-2-cung-nong-do": 2,
}
_BAN_HUY: dict[str, int] = {
    "chemistry.thpt.dong-hoc-tich-phan.ban-huy-bac-khong": 0,
    "chemistry.thpt.dong-hoc-tich-phan.ban-huy-bac-mot": 1,
    "chemistry.thpt.dong-hoc-tich-phan.ban-huy-bac-hai": 2,
    "chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-0": 0,
    "chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-1": 1,
    "chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-2": 2,
}
_TEN_BAC = {0: "bậc không", 1: "bậc một", 2: "bậc hai"}


def r_dong_hoc_bac(f: dict) -> Optional[Match]:
    fid = _id(f)
    if fid in _BAC_DONG_HOC:
        bac = _BAC_DONG_HOC[fid]
        return "kinetics_decay", {"order": bac}, f"nồng độ - thời gian, {_TEN_BAC[bac]}"
    if fid in _BAN_HUY:
        bac = _BAN_HUY[fid]
        return ("kinetics_decay", {"order": bac, "half_life": True},
                f"chu kì bán huỷ liên tiếp, {_TEN_BAC[bac]}")
    return None


def r_tuyen_tinh_hoa_bac(f: dict) -> Optional[Match]:
    if _id(f) == "chemistry.thpt.dong-hoc-tich-phan.do-thi-tuyen-tinh-xac-dinh-bac":
        return "kinetics_linearization", {}, "ba đồ thị tuyến tính hoá theo bậc"
    return None


# --------------------------------------------------------------------------
# HOÁ — chuẩn độ acid - base
# --------------------------------------------------------------------------
_CHI_THI = [8.2, 10.0, "phenolphtalein đổi màu"]
_CHUAN_DO: dict[str, tuple[dict, str]] = {
    "chemistry.dai-hoc.hoa-phan-tich.duong-cong-chuan-do-axit-manh":
        ({"kind": "manh-manh"}, "chuẩn độ acid mạnh bằng base mạnh"),
    "chemistry.dai-hoc.hoa-phan-tich.chuan-do-axit-yeu":
        ({"kind": "yeu-manh"}, "chuẩn độ acid yếu bằng base mạnh"),
    "chemistry.thpt.axit-bazo-quoc-te.bon-moc-ph-chuan-do-axit-yeu":
        ({"kind": "yeu-manh"}, "bốn mốc pH trên đường chuẩn độ acid yếu"),
    "chemistry.thpt.axit-bazo-quoc-te.ph-nua-diem-tuong-duong":
        ({"kind": "yeu-manh", "show_buffer": False}, "tại nửa điểm tương đương pH = pKa"),
    "chemistry.thpt.axit-bazo-quoc-te.so-sanh-cac-loai-duong-cong-chuan-do":
        ({"compare": True}, "so sánh đường chuẩn độ acid mạnh và acid yếu"),
    "chemistry.thpt.axit-bazo-quoc-te.chi-thi-khoang-doi-mau":
        ({"kind": "yeu-manh", "show_buffer": False, "indicator": _CHI_THI},
         "khoảng đổi màu của chỉ thị nằm trong bước nhảy"),
    "chemistry.dai-hoc.hoa-phan-tich.chon-chi-thi-axit-bazo":
        ({"kind": "yeu-manh", "show_buffer": False, "indicator": _CHI_THI},
         "chọn chỉ thị theo bước nhảy pH"),
    "chemistry.thpt.axit-bazo-quoc-te.khoang-dem-hieu-qua":
        ({"kind": "yeu-manh"}, "khoảng đệm hiệu quả pKa ± 1"),
    "chemistry.thpt.dien-li.ph-dung-dich-dem":
        ({"kind": "yeu-manh"}, "vùng đệm: pH = pKa khi [A⁻] = [HA]"),
    "chemistry.dai-hoc.hoa-phan-tich.henderson-hasselbalch":
        ({"kind": "yeu-manh"}, "vùng đệm: pH = pKa khi [A⁻] = [HA]"),
}


def r_duong_chuan_do(f: dict) -> Optional[Match]:
    hit = _CHUAN_DO.get(_id(f))
    return ("titration_curve", hit[0], hit[1]) if hit else None


# --------------------------------------------------------------------------
# HOÁ — cấu tạo nguyên tử
# --------------------------------------------------------------------------
def r_bohr(f: dict) -> Optional[Match]:
    if _id(f) == "chemistry.dai-hoc.cau-tao-chat.ban-kinh-bohr":
        return "bohr_atom", {"n": 4}, "bán kính quỹ đạo Bohr tỉ lệ n²"
    return None


_MUC_NL: dict[str, tuple[dict, str]] = {
    "chemistry.dai-hoc.cau-tao-chat.muc-nang-luong-bohr":
        ({"n": 6}, "mức năng lượng En = −13,6·Z²/n²"),
    "chemistry.dai-hoc.cau-tao-chat.cong-thuc-rydberg":
        ({"n": 6}, "các dãy quang phổ ứng với chuyển mức"),
    "chemistry.thpt.cau-tao-quoc-te.gioi-han-hoi-tu-nang-luong-ion-hoa":
        ({"n": 7, "series": ["Lyman"]}, "các mức dồn về giới hạn hội tụ E = 0"),
}


def r_muc_nang_luong(f: dict) -> Optional[Match]:
    hit = _MUC_NL.get(_id(f))
    return ("energy_levels", hit[0], hit[1]) if hit else None


_O_LUONG_TU: dict[str, tuple[dict, str]] = {
    "chemistry.thpt.nguyen-tu.quy-tac-hund":
        ({"mode": "hund", "subshell": "p", "e": 4}, "quy tắc Hund trên phân lớp p"),
    "chemistry.thpt.nguyen-tu.so-electron-toi-da-phan-lop":
        ({"mode": "phan-lop"}, "số ô và số electron tối đa của s, p, d, f"),
    "chemistry.thpt.nguyen-tu.so-orbital-trong-lop":
        ({"mode": "lop", "n": 3}, "số orbital của lớp thứ n bằng n²"),
    "chemistry.thpt.nguyen-tu.so-electron-toi-da-lop":
        ({"mode": "lop", "n": 3}, "số electron tối đa của lớp thứ n bằng 2n²"),
}


def r_o_luong_tu(f: dict) -> Optional[Match]:
    hit = _O_LUONG_TU.get(_id(f))
    return ("orbital_boxes", hit[0], hit[1]) if hit else None


# --------------------------------------------------------------------------
# HOÁ — pin điện hoá
# --------------------------------------------------------------------------
_PIN_DANIELL = {"anode": "Zn", "cathode": "Cu",
                "emf": "E pin = E catot − E anot > 0"}
# Pin nồng độ: hai điện cực cùng kim loại, cực có nồng độ LOÃNG là anot — vẽ
# ngược lại là dạy sai chiều dòng electron.
_PIN_NONG_DO = {"anode": "Cu", "cathode": "Cu", "anode_note": "(loãng)",
                "cathode_note": "(đặc)",
                "emf": "E = (0,0592/n)·log(c đặc / c loãng)"}
_PIN: dict[str, tuple[dict, str]] = {
    "chemistry.thpt.dien-hoa-quoc-te.so-do-pin-iupac":
        ({"anode": "Zn", "cathode": "Cu",
          "emf": "Zn(s) | Zn²⁺(aq) ‖ Cu²⁺(aq) | Cu(s)"},
         "sơ đồ pin Zn - Cu theo quy ước IUPAC: anot bên trái, catot bên phải"),
    "chemistry.thpt.dien-hoa.suc-dien-dong-cua-pin":
        (_PIN_DANIELL, "sức điện động chuẩn của pin"),
    "chemistry.dai-hoc.dien-hoa-hoc.suc-dien-dong-pin":
        (_PIN_DANIELL, "sức điện động của pin điện hoá"),
    "chemistry.thpt.dien-hoa-quoc-te.pin-nong-do": (_PIN_NONG_DO, "pin nồng độ"),
    "chemistry.dai-hoc.dien-hoa-hoc.pin-nong-do": (_PIN_NONG_DO, "pin nồng độ"),
}


def r_pin_dien_hoa(f: dict) -> Optional[Match]:
    hit = _PIN.get(_id(f))
    return ("galvanic_cell", dict(hit[0]), hit[1]) if hit else None


# --------------------------------------------------------------------------
# SINH — khung Punnett
# --------------------------------------------------------------------------
_GIAO_TU_2 = ["AB", "Ab", "aB", "ab"]


def _nhom(keys, cls, label):
    return {"keys": list(keys), "cls": cls, "label": label}


def _lai_2_cap(nhom_list, ratio):
    return {"rows": _GIAO_TU_2, "cols": _GIAO_TU_2, "groups": nhom_list,
            "ratio": ratio, "row_label": "giao tử ♀ (AaBb)",
            "col_label": "giao tử ♂ (AaBb)"}


_PUNNETT: dict[str, tuple[dict, str]] = {
    "biology.thcs.quy-luat-di-truyen.quy-luat-phan-li": (
        {"rows": ["A", "a"], "cols": ["A", "a"],
         "row_label": "giao tử ♀ (Aa)", "col_label": "giao tử ♂ (Aa)",
         "ratio": "1 AA : 2 Aa : 1 aa  →  3 trội : 1 lặn",
         "groups": [_nhom(["A-"], "fill-a", "3 kiểu hình trội (A-)"),
                    _nhom(["aa"], "fill-b", "1 kiểu hình lặn (aa)")]},
        "Aa × Aa cho 1 : 2 : 1"),
    "biology.thcs.quy-luat-di-truyen.lai-phan-tich": (
        {"rows": ["A", "a"], "cols": ["a", "a"],
         "row_label": "giao tử ♀ (Aa)", "col_label": "giao tử ♂ (aa)",
         "ratio": "1 Aa : 1 aa  →  1 trội : 1 lặn",
         "groups": [_nhom(["A-"], "fill-a", "1 trội (Aa)"),
                    _nhom(["aa"], "fill-b", "1 lặn (aa)")]},
        "lai phân tích Aa × aa"),
    "biology.thcs.quy-luat-di-truyen.phan-li-doc-lap": (
        _lai_2_cap([_nhom(["A-B-"], "fill-a", "9 A-B-"),
                    _nhom(["A-bb"], "fill-b", "3 A-bb"),
                    _nhom(["aaB-"], "fill-c", "3 aaB-")],
                   "9 : 3 : 3 : 1  (ô trắng: 1 aabb)"),
        "AaBb × AaBb cho 9 : 3 : 3 : 1"),
    "biology.thpt.quy-luat-di-truyen.tuong-tac-bo-sung-9-3-3-1": (
        _lai_2_cap([_nhom(["A-B-"], "fill-a", "9 A-B-"),
                    _nhom(["A-bb"], "fill-b", "3 A-bb"),
                    _nhom(["aaB-"], "fill-c", "3 aaB-")],
                   "9 : 3 : 3 : 1 — bốn kiểu hình"),
        "tương tác bổ sung 9 : 3 : 3 : 1"),
    "biology.thpt.quy-luat-di-truyen.tuong-tac-bo-sung-9-6-1": (
        _lai_2_cap([_nhom(["A-B-"], "fill-a", "9 A-B-"),
                    _nhom(["A-bb", "aaB-"], "fill-b", "6 (3 A-bb + 3 aaB-) — cùng kiểu hình")],
                   "9 : 6 : 1  (ô trắng: 1 aabb)"),
        "tương tác bổ sung 9 : 6 : 1"),
    "biology.thpt.quy-luat-di-truyen.tuong-tac-bo-sung-9-7": (
        _lai_2_cap([_nhom(["A-B-"], "fill-a", "9 A-B-"),
                    _nhom(["A-bb", "aaB-", "aabb"], "fill-b",
                          "7 (3 A-bb + 3 aaB- + 1 aabb) — cùng kiểu hình")],
                   "9 : 7"),
        "tương tác bổ sung 9 : 7"),
    "biology.thpt.quy-luat-di-truyen.tuong-tac-at-che-12-3-1": (
        _lai_2_cap([_nhom(["A-B-", "A-bb"], "fill-a", "12 (9 A-B- + 3 A-bb) — A át chế"),
                    _nhom(["aaB-"], "fill-c", "3 aaB-")],
                   "12 : 3 : 1  (ô trắng: 1 aabb)"),
        "át chế trội 12 : 3 : 1"),
    "biology.thpt.quy-luat-di-truyen.tuong-tac-at-che-13-3": (
        _lai_2_cap([_nhom(["A-B-", "A-bb", "aabb"], "fill-a",
                          "13 (9 A-B- + 3 A-bb + 1 aabb)"),
                    _nhom(["aaB-"], "fill-c", "3 aaB-")],
                   "13 : 3"),
        "át chế trội 13 : 3"),
    "biology.thpt.quy-luat-di-truyen.tuong-tac-at-che-9-3-4": (
        _lai_2_cap([_nhom(["A-B-"], "fill-a", "9 A-B-"),
                    _nhom(["A-bb"], "fill-b", "3 A-bb"),
                    _nhom(["aaB-", "aabb"], "fill-c", "4 (3 aaB- + 1 aabb) — aa át chế")],
                   "9 : 3 : 4"),
        "át chế lặn 9 : 3 : 4"),
    "biology.thpt.quy-luat-di-truyen.tuong-tac-cong-gop-15-1": (
        _lai_2_cap([_nhom(["A-B-", "A-bb", "aaB-"], "fill-a",
                          "15 — có ít nhất một alen trội")],
                   "15 : 1  (ô trắng: 1 aabb)"),
        "cộng gộp 15 : 1"),
    "biology.thpt.quy-luat-di-truyen.di-truyen-lien-ket-gioi-tinh-tren-x": (
        {"rows": ["Xᴬ", "Xᵃ"], "cols": ["Xᴬ", "Y"],
         "cells": [["XᴬXᴬ", "XᴬY"], ["XᴬXᵃ", "XᵃY"]],
         "row_label": "giao tử ♀ (XᴬXᵃ)", "col_label": "giao tử ♂ (XᴬY)",
         "ratio": "1 XᴬXᴬ : 1 XᴬXᵃ : 1 XᴬY : 1 XᵃY  —  chỉ con trai biểu hiện",
         "groups": [_nhom(["XᵃY"], "fill-b", "con trai mang alen lặn thì biểu hiện bệnh")]},
        "gen lặn trên vùng không tương đồng của X"),
    "biology.thpt.quy-luat-di-truyen.di-truyen-gen-tren-y": (
        {"rows": ["X", "X"], "cols": ["X", "Yᵃ"],
         "cells": [["XX", "XYᵃ"], ["XX", "XYᵃ"]],
         "row_label": "giao tử ♀ (XX)", "col_label": "giao tử ♂ (XYᵃ)",
         "ratio": "1/2 XX bình thường : 1/2 XYᵃ biểu hiện — di truyền thẳng cho con trai",
         "groups": [_nhom(["XYᵃ"], "fill-b", "con trai nhận Y của bố nên đều biểu hiện")]},
        "gen trên vùng không tương đồng của Y"),
    "biology.thpt.quy-luat-di-truyen.lien-ket-gen-hoan-toan": (
        {"rows": ["AB", "ab"], "cols": ["AB", "ab"],
         "cells": [["AB/AB", "AB/ab"], ["AB/ab", "ab/ab"]],
         "row_label": "giao tử ♀ (AB/ab)", "col_label": "giao tử ♂ (AB/ab)",
         "ratio": "1 AB/AB : 2 AB/ab : 1 ab/ab  →  3 A-B- : 1 aabb",
         "groups": [_nhom(["ab/ab"], "fill-b", "1 ab/ab — kiểu hình lặn cả hai tính trạng")]},
        "liên kết hoàn toàn: hai gen di truyền cùng nhau"),
    "biology.thpt.di-truyen-quan-the.dinh-luat-hardy-weinberg": (
        {"rows": ["p (A)", "q (a)"], "cols": ["p (A)", "q (a)"],
         "cells": [["p² AA", "pq Aa"], ["pq Aa", "q² aa"]],
         "row_label": "giao tử ♀ (tần số)", "col_label": "giao tử ♂ (tần số)",
         "ratio": "p² + 2pq + q² = 1"},
        "khung tần số giao tử của quần thể cân bằng"),
    "biology.thpt.bang-cong-thuc-ap.hardy-weinberg-bang-tham-chieu": (
        {"rows": ["p (A)", "q (a)"], "cols": ["p (A)", "q (a)"],
         "cells": [["p² AA", "pq Aa"], ["pq Aa", "q² aa"]],
         "row_label": "giao tử ♀ (tần số)", "col_label": "giao tử ♂ (tần số)",
         "ratio": "p + q = 1;   p² + 2pq + q² = 1"},
        "khung tần số giao tử của quần thể cân bằng"),
}


def r_punnett(f: dict) -> Optional[Match]:
    hit = _PUNNETT.get(_id(f))
    return ("punnett", dict(hit[0]), hit[1]) if hit else None


# --------------------------------------------------------------------------
# SINH — phả hệ
# --------------------------------------------------------------------------
_BO_ME_DI_HOP = [{"sex": "nam", "carrier": True, "label": "Aa"},
                 {"sex": "nu", "carrier": True, "label": "Aa"}]
_PHA_HE: dict[str, tuple[dict, str]] = {
    "biology.thpt.di-truyen-nguoi.xac-suat-sinh-con-benh-tu-bo-me-di-hop": (
        {"parents": _BO_ME_DI_HOP,
         "children": [{"sex": "nam", "label": "AA"},
                      {"sex": "nu", "carrier": True, "label": "Aa"},
                      {"sex": "nam", "carrier": True, "label": "Aa"},
                      {"sex": "nu", "affected": True, "label": "aa"}],
         "note": "P(con bệnh) = 1/4"},
        "bố mẹ đều dị hợp: 1/4 số con biểu hiện bệnh"),
    "biology.thpt.di-truyen-nguoi.xac-suat-theo-pha-he": (
        {"parents": _BO_ME_DI_HOP,
         "children": [{"sex": "nam", "label": "?"},
                      {"sex": "nu", "affected": True},
                      {"sex": "nam", "label": "?"}],
         "note": "quy ước ký hiệu để đọc phả hệ"},
        "ký hiệu phả hệ dùng khi tính xác suất"),
}


def r_pha_he(f: dict) -> Optional[Match]:
    hit = _PHA_HE.get(_id(f))
    return ("pedigree", dict(hit[0]), hit[1]) if hit else None


# --------------------------------------------------------------------------
# SINH — tăng trưởng quần thể
# --------------------------------------------------------------------------
_TANG_TRUONG: dict[str, tuple[dict, str]] = {
    "biology.thpt.sinh-thai.tang-truong-theo-tiem-nang-sinh-hoc":
        ({"mode": "mu"}, "đường cong chữ J: tăng trưởng không giới hạn"),
    "biology.thpt.sinh-thai.tang-truong-mu-theo-thoi-gian":
        ({"mode": "mu"}, "số cá thể tăng theo hàm mũ"),
    "biology.thpt.bang-cong-thuc-ap.tang-truong-mu-rmax":
        ({"mode": "mu"}, "tăng trưởng mũ với r max"),
    "biology.dai-hoc.sinh-thai-hoc.tang-truong-ham-mu":
        ({"mode": "mu"}, "mô hình tăng trưởng hàm mũ"),
    "biology.thpt.sinh-thai.tang-truong-thuc-te-logistic":
        ({"mode": "so-sanh"}, "đường cong chữ S tiến tới sức chứa K"),
    "biology.thpt.bang-cong-thuc-ap.tang-truong-logistic-rmax":
        ({"mode": "logistic"}, "tăng trưởng logistic tiến tới K"),
    "biology.dai-hoc.sinh-thai-hoc.tang-truong-logistic":
        ({"mode": "logistic"}, "nghiệm logistic: chữ S có tiệm cận K"),
    "biology.thpt.sinh-thai.thoi-gian-nhan-doi-quan-the":
        ({"mode": "mu", "doubling": True}, "thời gian để N tăng gấp đôi"),
    "biology.dai-hoc.sinh-thai-hoc.thoi-gian-nhan-doi":
        ({"mode": "mu", "doubling": True}, "thời gian nhân đôi t = ln2/r"),
    "biology.dai-hoc.sinh-thai-hoc.san-luong-ben-vung-toi-da":
        ({"mode": "dndt"}, "dN/dt cực đại rK/4 tại N = K/2"),
    "biology.thpt.bang-cong-thuc-ap.suc-chua-moi-truong-va-toc-do-cuc-dai":
        ({"mode": "dndt"}, "tốc độ tăng trưởng lớn nhất tại một nửa sức chứa"),
    "biology.thpt.vi-sinh-vat.duong-cong-sinh-truong":
        ({"mode": "vi-sinh-vat"}, "bốn pha nuôi cấy không liên tục"),
}


def r_tang_truong_quan_the(f: dict) -> Optional[Match]:
    hit = _TANG_TRUONG.get(_id(f))
    return ("population_growth", hit[0], hit[1]) if hit else None


# --------------------------------------------------------------------------
# SINH / HOÁ — động học enzyme
# --------------------------------------------------------------------------
_ENZYME: dict[str, tuple[dict, str]] = {
    "biology.dai-hoc.dong-hoc-enzyme.phuong-trinh-michaelis-menten":
        ({}, "hyperbol bão hoà: Vmax và KM"),
    "biology.dai-hoc.dong-hoc-enzyme.y-nghia-km":
        ({}, "[S] = KM thì v = ½Vmax"),
    "chemistry.dai-hoc.dong-hoa-hoc.michaelis-menten":
        ({}, "hyperbol bão hoà: Vmax và KM"),
    "biology.dai-hoc.dong-hoc-enzyme.gan-ket-phoi-tu-kd":
        ({"ylabel": "θ", "vmax_label": "1,0", "km_label": "Kd", "half_label": "0,5"},
         "phần bão hoà θ theo [L], nửa bão hoà tại Kd"),
    "biology.dai-hoc.dong-hoc-enzyme.uc-che-canh-tranh":
        ({"inhibition": "canh-tranh"}, "ức chế cạnh tranh: KM tăng, Vmax giữ nguyên"),
    "chemistry.dai-hoc.dong-hoa-hoc.uc-che-enzyme-canh-tranh":
        ({"inhibition": "canh-tranh"}, "ức chế cạnh tranh: KM tăng, Vmax giữ nguyên"),
    "biology.dai-hoc.dong-hoc-enzyme.uc-che-khong-canh-tranh":
        ({"inhibition": "khong-canh-tranh"}, "ức chế không cạnh tranh: Vmax giảm, KM giữ nguyên"),
    "biology.dai-hoc.dong-hoc-enzyme.uc-che-phi-canh-tranh":
        ({"inhibition": "phi-canh-tranh"}, "ức chế phi cạnh tranh: Vmax và KM cùng giảm"),
    "biology.dai-hoc.dong-hoc-enzyme.uc-che-hon-hop":
        ({"inhibition": "hon-hop"}, "ức chế hỗn hợp"),
    "biology.dai-hoc.dong-hoc-enzyme.lineweaver-burk":
        ({"mode": "lineweaver"}, "nghịch đảo kép: giao trục tại 1/Vmax và −1/KM"),
    "chemistry.dai-hoc.dong-hoa-hoc.lineweaver-burk":
        ({"mode": "lineweaver"}, "nghịch đảo kép: giao trục tại 1/Vmax và −1/KM"),
    "biology.dai-hoc.dong-hoc-enzyme.eadie-hofstee":
        ({"mode": "eadie"}, "hệ số góc −KM, cắt trục tung tại Vmax"),
    "biology.dai-hoc.dong-hoc-enzyme.hanes-woolf":
        ({"mode": "hanes"}, "hệ số góc 1/Vmax, cắt trục tung tại KM/Vmax"),
    "biology.dai-hoc.dong-hoc-enzyme.phuong-trinh-hill":
        ({"mode": "hill", "h": 3, "km_label": "K0,5"}, "đường cong sigmoid của enzyme dị lập thể"),
}


def r_dong_hoc_enzyme(f: dict) -> Optional[Match]:
    hit = _ENZYME.get(_id(f))
    return ("enzyme_kinetics", dict(hit[0]), hit[1]) if hit else None


# --------------------------------------------------------------------------
# SINH — tháp sinh thái và dòng năng lượng
# --------------------------------------------------------------------------
_THAP: dict[str, tuple[dict, str]] = {
    "biology.thpt.sinh-thai.hieu-suat-sinh-thai":
        ({}, "hiệu suất giữa hai bậc dinh dưỡng liền kề"),
    "biology.dai-hoc.sinh-thai-hoc.hieu-suat-sinh-thai":
        ({}, "hiệu suất chuyển hoá giữa các bậc"),
    "biology.thpt.sinh-thai.nang-luong-con-lai-qua-cac-bac":
        ({}, "năng lượng còn lại sau mỗi bậc"),
    "biology.thpt.sinh-thai-intl.thap-nang-luong-don-vi":
        ({"unit": "kJ·m⁻²·năm⁻¹"}, "đơn vị của tháp năng lượng"),
    "biology.thpt.sinh-thai.chuoi-va-luoi-thuc-an":
        ({"mode": "chuoi"}, "bậc dinh dưỡng trong chuỗi thức ăn"),
}


def r_thap_sinh_thai(f: dict) -> Optional[Match]:
    hit = _THAP.get(_id(f))
    return ("trophic_pyramid", dict(hit[0]), hit[1]) if hit else None


_DONG_NL: dict[str, tuple[dict, str]] = {
    "biology.thpt.sinh-thai.san-luong-thu-cap":
        ({"caption": "P₂ = C − (F + U) − R"}, "sản lượng thứ cấp sau các khoản thất thoát"),
    "biology.thpt.sinh-thai-intl.hieu-suat-tieu-thu-dong-hoa-san-xuat":
        ({}, "ba hiệu suất trên cùng một dòng năng lượng"),
    "biology.thpt.sinh-thai-intl.san-luong-tieu-thu-aqa":
        ({"show_u": False, "caption": "N = I − (F + R)"},
         "ký hiệu A-Level: bài tiết gộp vào F"),
    "biology.thpt.sinh-thai.san-luong-so-cap-tinh":
        ({"mode": "so-cap", "gross_key": "P G", "net_key": "P N",
          "caption": "P N = P G − R"}, "sản lượng sơ cấp tinh"),
    "biology.dai-hoc.sinh-thai-hoc.nang-suat-so-cap":
        ({"mode": "so-cap"}, "NPP = GPP − R"),
}


def r_dong_nang_luong(f: dict) -> Optional[Match]:
    hit = _DONG_NL.get(_id(f))
    return ("energy_flow", dict(hit[0]), hit[1]) if hit else None


RULES: list[Rule] = [
    r_gian_do_nang_luong, r_dong_hoc_bac, r_tuyen_tinh_hoa_bac, r_duong_chuan_do,
    r_bohr, r_muc_nang_luong, r_o_luong_tu, r_pin_dien_hoa,
    r_punnett, r_pha_he, r_tang_truong_quan_the, r_dong_hoc_enzyme,
    r_thap_sinh_thai, r_dong_nang_luong,
]
