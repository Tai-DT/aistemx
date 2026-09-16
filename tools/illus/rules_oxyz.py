"""Luật gán generator cho Hình học toạ độ không gian Oxyz (Toán 12).

Ánh xạ chuẩn xác từng công thức toạ độ điểm/vectơ, mặt phẳng, đường thẳng, góc và khoảng cách
vào các generator chuyên biệt trong `gen_oxyz.py`.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _tail(f: dict, *tails: str) -> bool:
    fid = f.get("id") or ""
    return any(fid.endswith("." + t) for t in tails)


def r_oxyz_coords(f: dict) -> Optional[Match]:
    """Hệ trục toạ độ Oxyz và toạ độ điểm/vectơ cơ bản."""
    if _tail(f, "oxyz-toa-do.toa-do-diem"):
        return "oxyz_coords", {"mode": "point"}, "tọa độ điểm M(x, y, z) trong không gian Oxyz"
    if _tail(f, "oxyz-toa-do.toa-do-vecto-hai-diem"):
        return "oxyz_coords", {"mode": "point"}, "tọa độ vectơ AB = (x_B - x_A, y_B - y_A, z_B - z_A)"
    if _tail(f, "oxyz-toa-do.do-dai-vecto"):
        return "oxyz_coords", {"mode": "point"}, "độ dài vectơ |u| = √(x² + y² + z²)"
    if _tail(f, "oxyz-toa-do.khoang-cach-hai-diem"):
        return "oxyz_coords", {"mode": "point"}, "khoảng cách giữa hai điểm AB = √((x_B-x_A)² + (y_B-y_A)² + (z_B-z_A)²)"
    if _tail(f, "oxyz-toa-do.hinh-chieu-doi-xung-mat-toa-do"):
        return "oxyz_coords", {"mode": "point"}, "hình chiếu và đối xứng của M qua các mặt phẳng toạ độ"
    if _tail(f, "oxyz-toa-do.phep-toan-vecto"):
        return "oxyz_coords", {"mode": "unit_vectors"}, "các phép toán vectơ theo hệ toạ độ không gian Oxyz"
    if _tail(f, "oxyz-toa-do.trung-diem"):
        return "oxyz_coords", {"mode": "midpoint_centroid"}, "tọa độ trung điểm M của đoạn thẳng AB"
    if _tail(f, "oxyz-toa-do.trong-tam-tam-giac"):
        return "oxyz_coords", {"mode": "midpoint_centroid"}, "tọa độ trọng tâm G của tam giác ABC"
    if _tail(f, "oxyz-toa-do.diem-chia-doan"):
        return "oxyz_coords", {"mode": "midpoint_centroid"}, "tọa độ điểm chia đoạn thẳng theo tỉ số k"
    return None


def r_oxyz_vectors(f: dict) -> Optional[Match]:
    """Tích có hướng, tích vô hướng và các ứng dụng hình học."""
    if _tail(f, "oxyz-toa-do.tich-co-huong"):
        return "oxyz_vectors", {"mode": "cross_product"}, "tích có hướng [u, v] vuông góc với cả u và v"
    if _tail(f, "oxyz-toa-do.tich-co-huong-tinh-chat"):
        return "oxyz_vectors", {"mode": "cross_product"}, "tính chất của tích có hướng trong không gian"
    if _tail(f, "oxyz-toa-do.dieu-kien-vuong-goc"):
        return "oxyz_vectors", {"mode": "cross_product"}, "điều kiện hai vectơ vuông góc u · v = 0"
    if _tail(f, "oxyz-toa-do.dieu-kien-cung-phuong"):
        return "oxyz_vectors", {"mode": "cross_product"}, "điều kiện hai vectơ cùng phương [u, v] = 0"
    if _tail(f, "oxyz-toa-do.dieu-kien-dong-phang"):
        return "oxyz_vectors", {"mode": "box_volume"}, "điều kiện ba vectơ đồng phẳng [u, v] · w = 0"
    if _tail(f, "oxyz-toa-do.goc-hai-vecto"):
        return "oxyz_vectors", {"mode": "dot_product"}, "góc giữa hai vectơ cos φ = (u·v)/(|u|·|v|)"
    if _tail(f, "oxyz-toa-do.tich-vo-huong"):
        return "oxyz_vectors", {"mode": "dot_product"}, "tích vô hướng u · v = |u|·|v|·cos φ"
    if _tail(f, "oxyz-toa-do.dien-tich-hinh-binh-hanh"):
        return "oxyz_vectors", {"mode": "parallelogram"}, "diện tích hình bình hành S = |[AB, AD]|"
    if _tail(f, "oxyz-toa-do.dien-tich-tam-giac"):
        return "oxyz_vectors", {"mode": "triangle"}, "diện tích tam giác S = ½ |[AB, AC]|"
    if _tail(f, "oxyz-toa-do.the-tich-khoi-hop"):
        return "oxyz_vectors", {"mode": "box_volume"}, "thể tích khối hộp V = |[AB, AD] · AA'|"
    return None


def r_oxyz_plane(f: dict) -> Optional[Match]:
    """Mặt phẳng trong không gian Oxyz."""
    if _tail(f, "oxyz-mat-phang.pt-tong-quat"):
        return "oxyz_plane", {"mode": "general"}, "phương trình tổng quát mặt phẳng (P): Ax + By + Cz + D = 0"
    if _tail(f, "oxyz-mat-phang.pt-qua-ba-diem"):
        return "oxyz_plane", {"mode": "general"}, "phương trình mặt phẳng đi qua ba điểm không thẳng hàng"
    if _tail(f, "oxyz-mat-phang.khoang-cach-diem-mat-phang"):
        return "oxyz_plane", {"mode": "distance"}, "khoảng cách từ điểm M đến mặt phẳng (P)"
    if _tail(f, "oxyz-mat-phang.hinh-chieu-vuong-goc-diem"):
        return "oxyz_plane", {"mode": "distance"}, "hình chiếu vuông góc của điểm trên mặt phẳng"
    if _tail(f, "oxyz-mat-phang.khoang-cach-hai-mat-song-song"):
        return "oxyz_plane", {"mode": "parallel"}, "khoảng cách giữa hai mặt phẳng song song"
    if _tail(f, "oxyz-mat-phang.vi-tri-tuong-doi"):
        return "oxyz_plane", {"mode": "parallel"}, "vị trí tương đối của hai mặt phẳng"
    if _tail(f, "oxyz-mat-phang.goc-hai-mat-phang"):
        return "oxyz_plane", {"mode": "angle"}, "góc giữa hai mặt phẳng cos φ = |n₁·n₂|/(|n₁|·|n₂|)"
    if _tail(f, "oxyz-mat-phang.pt-doan-chan"):
        return "oxyz_plane", {"mode": "intercept"}, "phương trình mặt phẳng theo đoạn chắn x/a + y/b + z/c = 1"
    if _tail(f, "oxyz-mat-phang.mat-phang-trung-truc"):
        return "oxyz_plane", {"mode": "midplane"}, "phương trình mặt phẳng trung trực của đoạn thẳng"
    return None


def r_oxyz_line(f: dict) -> Optional[Match]:
    """Đường thẳng trong không gian Oxyz và vị trí tương đối."""
    if _tail(f, "oxyz-duong-thang.pt-tham-so"):
        return "oxyz_line", {"mode": "param"}, "phương trình tham số của đường thẳng d"
    if _tail(f, "oxyz-duong-thang.pt-chinh-tac"):
        return "oxyz_line", {"mode": "param"}, "phương trình chính tắc của đường thẳng d"
    if _tail(f, "oxyz-duong-thang.goc-duong-mat"):
        return "oxyz_line", {"mode": "line_plane_angle"}, "góc giữa đường thẳng và mặt phẳng sin φ = |u·n|/(|u|·|n|)"
    if _tail(f, "oxyz-duong-thang.vi-tri-duong-mat"):
        return "oxyz_line", {"mode": "line_plane_angle"}, "vị trí tương đối của đường thẳng và mặt phẳng"
    if _tail(f, "oxyz-duong-thang.goc-hai-duong-thang"):
        return "oxyz_line", {"mode": "two_lines_angle"}, "góc giữa hai đường thẳng cos φ = |u₁·u₂|/(|u₁|·|u₂|)"
    if _tail(f, "oxyz-duong-thang.vi-tri-hai-duong-thang"):
        return "oxyz_line", {"mode": "two_lines_angle"}, "vị trí tương đối của hai đường thẳng"
    if _tail(f, "oxyz-duong-thang.khoang-cach-diem-duong-thang"):
        return "oxyz_line", {"mode": "point_line_dist"}, "khoảng cách từ điểm M đến đường thẳng d"
    if _tail(f, "oxyz-duong-thang.khoang-cach-hai-duong-cheo-nhau"):
        return "oxyz_line", {"mode": "skew_lines"}, "khoảng cách giữa hai đường thẳng chéo nhau"
    if _tail(f, "oxyz-duong-thang.khoang-cach-hai-duong-song-song"):
        return "oxyz_line", {"mode": "skew_lines"}, "khoảng cách giữa hai đường thẳng song song"
    if _tail(f, "oxyz-mat-cau.vi-tri-mat-cau-duong-thang"):
        return "oxyz_line", {"mode": "sphere_line"}, "vị trí tương đối giữa mặt cầu và đường thẳng"
    return None


RULES: list[Rule] = [
    r_oxyz_coords,
    r_oxyz_vectors,
    r_oxyz_plane,
    r_oxyz_line,
]
