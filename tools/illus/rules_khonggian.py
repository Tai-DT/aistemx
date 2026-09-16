"""Luật gán generator hình học không gian chiếu trục đo cho công thức.

Ánh xạ chuẩn xác từng công thức hình học không gian (hộp, lập phương, lăng trụ,
chóp, chóp cụt, tứ diện, trụ, nón, nón cụt, mặt cầu) vào các generator trong `gen_khonggian.py`.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    """``id`` có kết thúc bằng ``.<tail>`` không (khớp trọn phần đuôi)."""
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


def r_box3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-hoc-khong-gian.dien-tich-xung-quanh-hinh-hop-chu-nhat",
             "hinh-khong-gian.hinh-hop-chu-nhat-dien-tich-xung-quanh"):
        return "box3d", {"highlight": "xq"}, "diện tích xung quanh hình hộp chữ nhật"
    if _tail(f, "hinh-hoc-khong-gian.dien-tich-toan-phan-hinh-hop-chu-nhat"):
        return "box3d", {}, "diện tích toàn phần hình hộp chữ nhật"
    if _tail(f, "hinh-hoc-khong-gian.the-tich-hinh-hop-chu-nhat",
             "hinh-khong-gian.hinh-hop-chu-nhat-the-tich"):
        return "box3d", {}, "thể tích hình hộp chữ nhật V = a·b·c"
    if _tail(f, "hinh-hoc-khong-gian.chieu-cao-hinh-hop-chu-nhat"):
        return "box3d", {}, "chiều cao hình hộp chữ nhật c = V/(a·b)"
    if _tail(f, "hinh-khong-gian.duong-cheo-hinh-hop-chu-nhat",
             "the-tich.duong-cheo-hinh-hop"):
        return "box3d", {"diagonal": True}, "đường chéo hình hộp d = √(a²+b²+c²)"
    if _tail(f, "mat-tron-xoay.mat-cau-ngoai-tiep-hop"):
        return "box3d", {"circumsphere": True}, "mặt cầu ngoại tiếp hình hộp chữ nhật"
    if _tail(f, "vecto.quy-tac-hinh-hop"):
        return "box3d", {"diagonal": True}, "quy tắc hình hộp cộng vectơ đường chéo"
    return None


def r_cube3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-hoc-khong-gian.dien-tich-xung-quanh-hinh-lap-phuong"):
        return "cube3d", {"highlight": "xq"}, "diện tích xung quanh hình lập phương S_xq = 4a²"
    if _tail(f, "hinh-hoc-khong-gian.dien-tich-toan-phan-hinh-lap-phuong"):
        return "cube3d", {}, "diện tích toàn phần hình lập phương S_tp = 6a²"
    if _tail(f, "hinh-hoc-khong-gian.the-tich-hinh-lap-phuong",
             "hinh-khong-gian.hinh-lap-phuong",
             "the-tich.khoi-lap-phuong"):
        return "cube3d", {}, "thể tích khối lập phương V = a³"
    if _tail(f, "te-bao.ti-le-s-tren-v-hinh-lap-phuong"):
        return "cube3d", {}, "tỉ lệ diện tích trên thể tích S/V tế bào hình lập phương"
    return None


def r_prism3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-khong-gian.lang-tru-dung-dien-tich-xung-quanh"):
        return "prism3d", {"highlight": "xq", "n_sides": 3}, "diện tích xung quanh lăng trụ đứng"
    if _tail(f, "hinh-khong-gian.lang-tru-dung-the-tich",
             "the-tich.khoi-lang-tru",
             "the-tich.lang-tru-dung-tam-giac-deu"):
        return "prism3d", {"n_sides": 3}, "thể tích khối lăng trụ V = S_đáy · h"
    if _tail(f, "mat-tron-xoay.mat-cau-ngoai-tiep-lang-tru"):
        return "prism3d", {"circumsphere": True, "n_sides": 3}, "mặt cầu ngoại tiếp hình lăng trụ"
    return None


def r_pyramid3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-khong-gian.hinh-chop-deu-dien-tich-xung-quanh"):
        return "pyramid3d", {"highlight": "xq", "slant_height": True, "n_sides": 4}, "diện tích xung quanh hình chóp đều (trung đoạn d)"
    if _tail(f, "hinh-khong-gian.hinh-chop-the-tich"):
        return "pyramid3d", {"n_sides": 4}, "thể tích hình chóp V = ⅓ S_đáy · h"
    if _tail(f, "mat-tron-xoay.mat-cau-ngoai-tiep-chop",
             "mat-tron-xoay.mat-cau-ngoai-tiep-chop-deu"):
        return "pyramid3d", {"circumsphere": True, "n_sides": 4}, "mặt cầu ngoại tiếp hình chóp"
    return None


def r_pyramid_frustum3d(f: dict) -> Optional[Match]:
    if _tail(f, "the-tich.khoi-chop-cut"):
        return "pyramid_frustum3d", {"n_sides": 4}, "thể tích khối chóp cụt V = ⅓h(B + B' + √(BB'))"
    return None


def r_tetrahedron3d(f: dict) -> Optional[Match]:
    if _tail(f, "quan-he-vuong-goc.tu-dien-vuong-duong-cao",
             "the-tich.tu-dien-vuong"):
        return "tetrahedron3d", {"right": True}, "tứ diện vuông O.ABC: 1/h² = 1/a² + 1/b² + 1/c²"
    if _tail(f, "the-tich.tu-dien-deu"):
        return "tetrahedron3d", {"regular": True}, "thể tích tứ diện đều cạnh a: V = a³√2/12"
    if _tail(f, "the-tich.tu-dien-theo-goc-tam-dien",
             "the-tich.tu-dien-theo-hai-canh-cheo",
             "oxyz-toa-do.trong-tam-tu-dien",
             "oxyz-toa-do.the-tich-tu-dien"):
        return "tetrahedron3d", {}, "khối tứ diện ABCD trong không gian"
    return None


def r_cylinder3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-khong-gian.hinh-tru-dien-tich",
             "mat-tron-xoay.tru-dien-tich-xung-quanh"):
        return "cylinder3d", {"highlight": "xq"}, "diện tích xung quanh hình trụ S_xq = 2πrl"
    if _tail(f, "mat-tron-xoay.tru-dien-tich-toan-phan"):
        return "cylinder3d", {}, "diện tích toàn phần hình trụ S_tp = 2πrl + 2πr²"
    if _tail(f, "hinh-khong-gian.hinh-tru-the-tich",
             "mat-tron-xoay.tru-the-tich"):
        return "cylinder3d", {}, "thể tích khối trụ V = πr²h"
    if _tail(f, "mat-tron-xoay.tru-thiet-dien-qua-truc"):
        return "cylinder3d", {"axis_section": True}, "thiết diện qua trục của hình trụ"
    if _tail(f, "bang-cong-thuc-ap.ti-le-s-tren-v-hinh-tru"):
        return "cylinder3d", {}, "tỉ lệ diện tích trên thể tích S/V hình trụ"
    return None


def r_cone3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-khong-gian.hinh-non-duong-sinh",
             "mat-tron-xoay.non-duong-sinh"):
        return "cone3d", {}, "đường sinh hình nón l = √(r² + h²)"
    if _tail(f, "hinh-khong-gian.hinh-non-dien-tich",
             "mat-tron-xoay.non-dien-tich-xung-quanh"):
        return "cone3d", {"highlight": "xq"}, "diện tích xung quanh hình nón S_xq = πrl"
    if _tail(f, "mat-tron-xoay.non-dien-tich-toan-phan"):
        return "cone3d", {}, "diện tích toàn phần hình nón S_tp = πrl + πr²"
    if _tail(f, "hinh-khong-gian.hinh-non-the-tich",
             "mat-tron-xoay.non-the-tich"):
        return "cone3d", {}, "thể tích khối nón V = ⅓πr²h"
    if _tail(f, "mat-tron-xoay.non-thiet-dien-qua-truc"):
        return "cone3d", {"axis_section": True}, "thiết diện qua trục của hình nón"
    return None


def r_cone_frustum3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-khong-gian.hinh-non-cut-dien-tich",
             "mat-tron-xoay.non-cut-dien-tich-xung-quanh"):
        return "cone_frustum3d", {"highlight": "xq"}, "diện tích xung quanh nón cụt S_xq = π(r₁ + r₂)l"
    if _tail(f, "hinh-khong-gian.hinh-non-cut-the-tich",
             "mat-tron-xoay.non-cut-the-tich"):
        return "cone_frustum3d", {}, "thể tích khối nón cụt V = ⅓πh(r₁² + r₂² + r₁r₂)"
    if _tail(f, "mat-tron-xoay.non-cut-duong-sinh"):
        return "cone_frustum3d", {}, "đường sinh hình nón cụt l = √((r₁-r₂)² + h²)"
    return None


def r_sphere3d(f: dict) -> Optional[Match]:
    if _tail(f, "hinh-khong-gian.hinh-cau-dien-tich-mat",
             "mat-tron-xoay.mat-cau-dien-tich"):
        return "sphere3d", {}, "diện tích mặt cầu S = 4πR²"
    if _tail(f, "hinh-khong-gian.hinh-cau-the-tich",
             "mat-tron-xoay.khoi-cau-the-tich"):
        return "sphere3d", {}, "thể tích khối cầu V = ⁴⁄₃πR³"
    if _tail(f, "mat-tron-xoay.thiet-dien-mat-cau",
             "oxyz-mat-cau.ban-kinh-duong-tron-giao-tuyen",
             "oxyz-mat-cau.vi-tri-mat-cau-mat-phang"):
        return "sphere3d", {"plane": 1.2}, "giao tuyến mặt phẳng và mặt cầu r = √(R² - d²)"
    if _tail(f, "oxyz-mat-cau.pt-chinh-tac",
             "oxyz-mat-cau.pt-tong-quat"):
        return "sphere3d", {}, "phương trình mặt cầu tâm I bán kính R"
    if _tail(f, "oxyz-mat-cau.tiep-dien"):
        return "sphere3d", {"plane": 1.6}, "tiếp diện mặt cầu tại điểm M₀"
    if _tail(f, "te-bao.ti-le-s-tren-v-hinh-cau"):
        return "sphere3d", {}, "tỉ lệ diện tích trên thể tích S/V tế bào hình cầu"
    return None


RULES: list[Rule] = [
    r_box3d,
    r_cube3d,
    r_prism3d,
    r_pyramid3d,
    r_pyramid_frustum3d,
    r_tetrahedron3d,
    r_cylinder3d,
    r_cone3d,
    r_cone_frustum3d,
    r_sphere3d,
]
