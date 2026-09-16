"""Khối hình học không gian, chiếu xuống SVG phẳng (nét khuất vẽ đứt).

Kho đã có ``scenes3d.py`` nhưng đó là đường khác: nó sinh scene JSON cho một
trình dựng 3D. Ở đây cần SVG nhúng thẳng vào trang, nên khối được **chiếu trục
đo** một lần rồi vẽ như hình phẳng.

Công thức thể tích và diện tích xung quanh chỉ có nghĩa khi người học nhìn thấy
kích thước nào là kích thước nào, nên mọi hình trong họ này đều đánh dấu sẵn đại
lượng mà công thức dùng tới (h, r, a, l, đường chéo, trung đoạn) chứ không vẽ
khối trơn — một hình lăng trụ không có nhãn thì không minh hoạ được V = S·h.
"""

from __future__ import annotations

import math
from typing import Callable, Sequence

from .svgkit import Canvas, _n

Params = dict

# --------------------------------------------------------------------------
# Phép chiếu
# --------------------------------------------------------------------------
# Hướng nhìn dùng chung cho MỌI khối trong họ: hình hộp cạnh nhau trên một trang
# mà mỗi hình một góc nhìn thì người học tưởng chúng khác nhau về hình dạng.
#
# Chọn phép chiếu trục đo TRỰC GIAO (không phải xiên kiểu cabinet) vì một tính
# chất rất đáng tiền: với hướng nhìn dạng này, mọi đường tròn NẰM NGANG chiếu
# thành elip có trục song song với trục màn hình (rx = r, ry = r·sin(góc nâng)).
# Nhờ vậy đáy hình trụ/nón vẽ được bằng cung elip chuẩn của SVG, không phải elip
# nghiêng — phép chiếu xiên cho ra elip nghiêng, và hình trụ trông như bị đổ.
_AZ = math.radians(-35.0)   # góc phương vị (quay quanh trục đứng)
_EL = math.radians(20.0)    # góc nâng của mắt so với mặt phẳng ngang

_SIN_EL = math.sin(_EL)
_COS_EL = math.cos(_EL)

# Ảnh của ba trục thế giới trên màn hình; y màn hình hướng XUỐNG nên có dấu trừ.
_EX = (math.cos(_AZ), -math.sin(_AZ) * _SIN_EL)
_EY = (-math.sin(_AZ), -math.cos(_AZ) * _SIN_EL)
_EZ = (0.0, -_COS_EL)
# Hướng nhìn (từ mắt vào cảnh): tích vô hướng lớn hơn nghĩa là ở xa hơn.
_DIR = (math.sin(_AZ) * _COS_EL, math.cos(_AZ) * _COS_EL, -_SIN_EL)
# Hướng NẰM NGANG trong thế giới mà phép chiếu đưa đúng về phương ngang của màn
# hình. Thiết diện qua trục phải cắt theo hướng này thì mới hiện ra hình chữ nhật
# dựng đứng ôm sát bóng khối; cắt theo trục x thì thiết diện trông như bị đổ.
_U = (math.cos(_AZ), -math.sin(_AZ), 0.0)

_DASH = ' stroke-dasharray="6 5"'
_THIN = ' stroke-width="1.6"'
# Lớp accent-* khai CẢ fill lẫn stroke, mà khai báo trong <style> thắng thuộc
# tính trình bày `fill="none"` — nên polyline/path viền màu nhấn phải chặn nền
# bằng style nội tuyến, không thì SVG hiện ra một mảng màu đặc.
_NOFILL = ' style="fill:none"'


def _sub(cv: Canvas, x: float, y: float, base: str, sub: str,
         cls: str = "lbl", anchor: str = "start") -> None:
    """Nhãn có chỉ số dưới (r₁, r₂…) dựng bằng ``<tspan>``.

    Không dùng ký tự Unicode hạ chỉ số: bộ chữ toán trong bảng màu không chắc có
    glyph cho chúng, và chỗ nào thiếu thì người học nhìn thấy một ô vuông thay
    cho chỉ số — tức là hình mất đúng cái thông tin nó cần nói.
    """
    from .svgkit import esc
    cv.raw(f'<text x="{_n(x)}" y="{_n(y)}" text-anchor="{anchor}" class="{cls}">'
           f'{esc(base)}<tspan font-size="70%" dy="3.5">{esc(sub)}</tspan></text>')


def _xa_net(x: float, y: float, segments: Sequence) -> float:
    """Khoảng cách từ một chỗ định đặt nhãn tới nét gần nhất."""
    best = 1e9
    for (x1, y1), (x2, y2) in segments:
        dx, dy = x2 - x1, y2 - y1
        length2 = dx * dx + dy * dy
        t = 0.0 if length2 < 1e-12 else ((x - x1) * dx + (y - y1) * dy) / length2
        t = max(0.0, min(1.0, t))
        best = min(best, math.hypot(x - x1 - t * dx, y - y1 - t * dy))
    return best


def _canh_cua(pts, faces) -> list[tuple[tuple[float, float], tuple[float, float]]]:
    """Các cạnh (không lặp) của khối, theo toạ độ màn hình."""
    seen: set[tuple[int, int]] = set()
    out = []
    for face in faces:
        for i, vi in enumerate(face):
            vj = face[(i + 1) % len(face)]
            key = (vi, vj) if vi < vj else (vj, vi)
            if key not in seen:
                seen.add(key)
                out.append((pts[key[0]], pts[key[1]]))
    return out


def _ne_nhan(x0: float, y: float, avoid: Sequence[tuple[tuple[float, float],
                                                        tuple[float, float]]],
             label: str, gap: float = 7.0) -> tuple[float, str]:
    """Chỗ đặt nhãn cạnh một điểm mốc, tự lách khỏi các nét đi ngang qua độ cao ``y``.

    Cần tính chứ không đặt cứng một bên: cạnh bên của chóp tứ giác (đáy quay 45°)
    và của tứ diện chiếu xuống RẤT gần trục cao — lệch chừng chục pixel — nên
    nhãn ``h`` đặt cố định bên phải là chắc chắn bị một nét cắt ngang. Ở đây đo
    khoảng trống hai bên rồi hoặc nép sát trục (nếu bên ấy đủ rộng), hoặc nhảy
    hẳn sang bên kia nét gần nhất.
    """
    width = 8.5 * max(len(label), 1)
    xs: list[float] = []
    for (x1, y1), (x2, y2) in avoid:
        if abs(y2 - y1) < 1e-9:
            continue
        t = (y - y1) / (y2 - y1)
        if -1e-9 <= t <= 1.0 + 1e-9:
            xs.append(x1 + t * (x2 - x1))
    room_r = min((x - x0 for x in xs if x > x0 + 1e-9), default=1e9)
    room_l = min((x0 - x for x in xs if x < x0 - 1e-9), default=1e9)
    if room_r >= room_l:
        if room_r >= width + 2 * gap:
            return x0 + gap, "start"
        return x0 + room_r + gap, "start"
    if room_l >= width + 2 * gap:
        return x0 - gap, "end"
    return x0 - room_l - gap, "end"


def _dim(p: Params, key: str, default: float) -> float:
    """Đọc một kích thước, ép về khoảng vẽ được.

    Giá trị biên (0, số âm, NaN, số khổng lồ) đến từ dữ liệu chứ không từ người
    vẽ, nên ở đây quay về mặc định chứ không ném lỗi: thà ra một hình đúng hình
    dạng nhưng sai tỉ lệ so với ô dữ liệu lạ, còn hơn cả trang mất hình.
    """
    try:
        value = float(p.get(key, default))
    except (TypeError, ValueError):
        return float(default)
    if not math.isfinite(value) or value <= 0:
        return float(default)
    return min(value, 1e6)


def _scale_for(extent: float, target: float = 205.0) -> float:
    """Số px cho mỗi đơn vị thế giới, sao cho hình luôn cỡ bằng nhau.

    Công thức không nói kích thước thật, nên cạnh 3 hay cạnh 3000 đều phải ra
    một hình vừa mắt; chỉ chặn trên để hình cạnh 0,2 không nở thành tấm áp phích.
    """
    return min(80.0, target / max(extent, 1e-9))


class _View:
    """Phép chiếu + gốc toạ độ màn hình.

    Dùng theo hai nhịp: chiếu thử để canh khung (lúc này gốc còn ở 0), gọi
    ``fit`` đúng MỘT lần, rồi mới chiếu thật để vẽ. Không gộp được thành một
    nhịp vì khung phải biết hình rộng bao nhiêu trước khi đặt gốc.
    """

    def __init__(self, scale: float):
        self.s = float(scale)
        self.ox = 0.0
        self.oy = 0.0

    def p(self, x: float, y: float, z: float = 0.0) -> tuple[float, float]:
        return (
            self.ox + self.s * (x * _EX[0] + y * _EY[0] + z * _EZ[0]),
            self.oy + self.s * (x * _EX[1] + y * _EY[1] + z * _EZ[1]),
        )

    def rx(self, r: float) -> float:
        """Bán trục ngang của đường tròn nằm ngang bán kính r."""
        return r * self.s

    def ry(self, r: float) -> float:
        """Bán trục dọc — đây là chỗ độ 'dẹt' của đáy hình trụ/nón sinh ra."""
        return r * self.s * _SIN_EL

    def fit(self, world_pts: Sequence[tuple[float, float, float]],
            disks: Sequence[tuple[tuple[float, float, float], float, float]] = (),
            left: float = 44.0, right: float = 62.0,
            top: float = 34.0, bottom: float = 40.0) -> tuple[float, float]:
        """Đặt gốc màn hình sao cho hình + lề nhãn nằm gọn trong khung.

        ``disks`` là các hình tròn/elip (tâm thế giới, bán trục px) — chúng không
        có đỉnh nào để canh nên phải khai riêng, quên là mặt cầu bị cắt mất rìa.
        """
        xs: list[float] = []
        ys: list[float] = []
        for point in world_pts:
            sx, sy = self.p(*point)
            xs.append(sx)
            ys.append(sy)
        for center, rx, ry in disks:
            cx, cy = self.p(*center)
            xs.extend((cx - rx, cx + rx))
            ys.extend((cy - ry, cy + ry))
        self.ox = left - min(xs)
        self.oy = top - min(ys)
        return (max(xs) - min(xs) + left + right, max(ys) - min(ys) + top + bottom)


# --------------------------------------------------------------------------
# Khối đa diện: mặt nào quay về phía mắt thì cạnh của nó là nét thấy
# --------------------------------------------------------------------------
def _centroid(points: Sequence[tuple[float, float, float]]) -> tuple[float, float, float]:
    n = float(len(points))
    return (sum(p[0] for p in points) / n,
            sum(p[1] for p in points) / n,
            sum(p[2] for p in points) / n)


def _normal(verts, face) -> tuple[float, float, float]:
    """Pháp tuyến mặt theo Newell (bền cả khi bốn đỉnh không thật sự đồng phẳng)."""
    nx = ny = nz = 0.0
    for i, vi in enumerate(face):
        a = verts[vi]
        b = verts[face[(i + 1) % len(face)]]
        nx += (a[1] - b[1]) * (a[2] + b[2])
        ny += (a[2] - b[2]) * (a[0] + b[0])
        nz += (a[0] - b[0]) * (a[1] + b[1])
    return (nx, ny, nz)


def _face_flags(verts, faces) -> list[bool]:
    """Mặt nào nhìn thấy được.

    Chỉ đúng với khối LỒI — pháp tuyến được lật ra ngoài bằng cách so với tâm
    khối, cách này hỏng ngay nếu khối lõm. Cả họ này toàn khối lồi nên đủ dùng,
    và đổi lại thì hộp, lăng trụ, chóp, chóp cụt dùng chung một đường vẽ nét
    khuất thay vì mỗi hình tự đoán cạnh nào bị che.
    """
    center = _centroid(verts)
    flags: list[bool] = []
    for face in faces:
        nx, ny, nz = _normal(verts, face)
        fx, fy, fz = _centroid([verts[i] for i in face])
        out = (fx - center[0], fy - center[1], fz - center[2])
        if nx * out[0] + ny * out[1] + nz * out[2] < 0:
            nx, ny, nz = -nx, -ny, -nz
        flags.append(nx * _DIR[0] + ny * _DIR[1] + nz * _DIR[2] < -1e-9)
    return flags


def _base_label_pos(view: _View, base_pts,
                    axis: bool = False) -> tuple[float, float, str]:
    """Chỗ đặt nhãn diện tích đáy: ngang trọng tâm của đáy đã chiếu.

    Không lùi về dải sau của đáy: đó đúng là chỗ hai cạnh khuất chụm lại, chữ
    nằm đó bị nét đứt gạch ngang giữa. Ngang trọng tâm thì dây cung của đáy rộng
    nhất và không có cạnh nào đi qua.

    ``axis=True`` cho khối có trục cao xuyên qua đáy (chóp, chóp cụt): trục đi
    đúng qua trọng tâm nên nhãn phải nép hẳn sang một bên.
    """
    pts = [view.p(*w) for w in base_pts]
    cx = sum(x for x, _ in pts) / len(pts)
    cy = sum(y for _, y in pts) / len(pts)
    if axis:
        # Sang PHẢI: ký hiệu vuông góc ở chân trục cao mở về bên trái, nhãn đặt
        # bên ấy là chạm vào nó.
        return cx + 8.0, cy + 5.0, "start"
    return cx, cy + 5.0, "middle"


def _draw_polyhedron(cv: Canvas, view: _View, verts, faces, flags,
                     fills: dict[int, str] | None = None) -> list[tuple[float, float]]:
    """Vẽ khối lồi; trả về toạ độ màn hình của các đỉnh để gắn nhãn."""
    pts = [view.p(*v) for v in verts]
    for index, cls in (fills or {}).items():
        cv.polygon([pts[i] for i in faces[index]], cls=cls)
    # Một cạnh nằm trên hai mặt: chỉ cần MỘT mặt nhìn thấy là cạnh ấy nét liền.
    edges: dict[tuple[int, int], bool] = {}
    for face, seen in zip(faces, flags):
        for i, vi in enumerate(face):
            vj = face[(i + 1) % len(face)]
            key = (vi, vj) if vi < vj else (vj, vi)
            edges[key] = edges.get(key, False) or seen
    for (i, j), seen in edges.items():
        if not seen:
            cv.line(*pts[i], *pts[j], cls="ink-thin", extra=_DASH)
    for (i, j), seen in edges.items():   # nét liền vẽ sau để đè lên nét đứt
        if seen:
            cv.line(*pts[i], *pts[j], cls="ink")
    return pts


def _prism_faces(n: int) -> list[list[int]]:
    """Mặt của khối lăng trụ n cạnh: đáy 0..n-1, nắp n..2n-1."""
    bottom = list(range(n))
    top = list(range(n, 2 * n))
    sides = [[i, (i + 1) % n, n + (i + 1) % n, n + i] for i in range(n)]
    return [bottom, top] + sides


def _regular_base(n: int, a: float) -> list[tuple[float, float]]:
    """Đa giác đều n cạnh, cạnh a, tâm ở gốc, đặt sao cho có cạnh quay về mắt."""
    # Quay sao cho một CẠNH đáy hướng về mắt: đỉnh chĩa về phía người xem thì
    # hai mặt bên hai bên gần như chồng lên nhau, khối trông bẹp như hình phẳng.
    start = {3: 90.0, 4: 45.0, 6: 0.0}.get(n, 0.0)
    radius = a / (2.0 * math.sin(math.pi / n))
    return [
        (radius * math.cos(math.radians(start + 360.0 * i / n)),
         radius * math.sin(math.radians(start + 360.0 * i / n)))
        for i in range(n)
    ]


def _base_polygon(kind: str, a: float) -> tuple[list[tuple[float, float]], bool]:
    """Đáy theo tên; cờ trả về cho biết đáy có đều không (đều mới ghi nhãn cạnh a)."""
    if kind in ("tam-giac-deu", "tam giác đều"):
        return _regular_base(3, a), True
    if kind in ("luc-giac", "luc-giac-deu"):
        return _regular_base(6, a), True
    if kind == "vuong":
        return _regular_base(4, a), True
    if kind == "tam-giac":
        # Đáy tam giác thường: công thức V = S·h đúng với đáy BẤT KÌ, vẽ tam giác
        # đều ở đây sẽ gợi ý sai rằng phải là lăng trụ đều.
        #
        # Ba đỉnh chọn theo ẢNH của chúng chứ không theo hình dạng trong không
        # gian: bộ toạ độ trước đây có hai đỉnh chiếu gần trùng nhau theo phương
        # ngang, nên hai cạnh bên nằm đè lên nhau và cả khối trông như một tờ
        # giấy gấp đôi. Ở đây ba đỉnh cách nhau ít nhất 45% bề ngang của ảnh —
        # tam giác vẫn lệch cạnh rõ (tỉ số cạnh dài/ngắn ≈ 1,37) nhưng đọc ra
        # ngay là khối lăng trụ.
        return [(-0.35 * a, -0.33 * a), (0.64 * a, -0.09 * a), (-0.32 * a, 0.49 * a)], False
    return _regular_base(4, a), True


def _nearest_edge(pts_world, view: _View) -> int:
    """Chỉ số cạnh đáy gần mắt nhất — chỗ duy nhất chắc chắn không bị khối che."""
    best, best_depth = 0, None
    for i, (x, y) in enumerate(pts_world):
        jx, jy = pts_world[(i + 1) % len(pts_world)]
        mx, my = (x + jx) / 2.0, (y + jy) / 2.0
        depth = mx * _DIR[0] + my * _DIR[1]
        if best_depth is None or depth < best_depth:
            best, best_depth = i, depth
    return best


# --------------------------------------------------------------------------
# Khối tròn xoay: cung elip cho vành đáy, tiếp tuyến cho đường sinh
# --------------------------------------------------------------------------
def _arc(x1: float, y1: float, rx: float, ry: float, x2: float, y2: float, sweep: int) -> str:
    return f"M {_n(x1)} {_n(y1)} A {_n(rx)} {_n(ry)} 0 0 {sweep} {_n(x2)} {_n(y2)}"


def _disk(cx: float, cy: float, rx: float, ry: float) -> str:
    """Elip khép kín (dùng cho vành nhìn thấy trọn vẹn và cho mặt cắt)."""
    return (f"M {_n(cx - rx)} {_n(cy)} A {_n(rx)} {_n(ry)} 0 0 1 {_n(cx + rx)} {_n(cy)} "
            f"A {_n(rx)} {_n(ry)} 0 0 1 {_n(cx - rx)} {_n(cy)} Z")


def _tangent(rx: float, ry: float, apex_dy: float) -> tuple[float, float]:
    """Tiếp điểm của đường sinh với vành đáy, tính từ tâm vành (px).

    Nối đỉnh nón thẳng tới hai mút ngang của elip là sai: đường sinh phải TIẾP
    XÚC với vành, nối tới mút ngang thì nó cắt qua vành và hình nón trông như bị
    gãy vai. ``apex_dy`` là khoảng cách dọc từ tâm vành lên đỉnh (dương = đỉnh ở
    trên); trả về (lệch ngang, lệch lên) của tiếp điểm.
    """
    if not math.isfinite(apex_dy) or abs(apex_dy) <= ry:
        return rx, 0.0        # đỉnh nằm trong vành: không có tiếp tuyến, lùi về mút ngang
    dx = rx * math.sqrt(max(0.0, 1.0 - (ry / apex_dy) ** 2))
    return dx, ry * ry / apex_dy


def _round_body(cv: Canvas, view: _View, r_bottom: float, r_top: float, h: float,
                fill: str = "fill-a") -> tuple[tuple[float, float], tuple[float, float],
                                               tuple[float, float], tuple[float, float]]:
    """Thân khối trụ/nón cụt: bóng ngoài, vành đáy (khuất vẽ đứt), vành nắp.

    Trả về (tâm đáy, tâm nắp, tiếp điểm đáy, tiếp điểm nắp) tính bằng px.
    """
    bc = view.p(0.0, 0.0, 0.0)
    tc = view.p(0.0, 0.0, h)
    rb, ryb = view.rx(r_bottom), view.ry(r_bottom)
    rt, ryt = view.rx(r_top), view.ry(r_top)
    hpx = bc[1] - tc[1]
    if abs(r_bottom - r_top) < 1e-9:
        tb = (rb, 0.0)
        tt = (rt, 0.0)
    else:
        apex_from_bottom = hpx * r_bottom / (r_bottom - r_top)
        tb = _tangent(rb, ryb, apex_from_bottom)
        tt = _tangent(rt, ryt, apex_from_bottom - hpx)
    # Bóng ngoài: nửa trước vành đáy + hai đường sinh + nửa sau vành nắp.
    cv.path(
        f"M {_n(bc[0] - tb[0])} {_n(bc[1] + tb[1])} "
        f"A {_n(rb)} {_n(ryb)} 0 0 0 {_n(bc[0] + tb[0])} {_n(bc[1] + tb[1])} "
        f"L {_n(tc[0] + tt[0])} {_n(tc[1] + tt[1])} "
        f"A {_n(rt)} {_n(ryt)} 0 0 0 {_n(tc[0] - tt[0])} {_n(tc[1] + tt[1])} Z",
        cls=fill,
    )
    cv.path(_arc(bc[0] - tb[0], bc[1] + tb[1], rb, ryb, bc[0] + tb[0], bc[1] + tb[1], 1),
            cls="ink-thin", extra=_DASH)
    cv.path(_arc(bc[0] - tb[0], bc[1] + tb[1], rb, ryb, bc[0] + tb[0], bc[1] + tb[1], 0),
            cls="ink")
    cv.path(_disk(tc[0], tc[1], rt, ryt), cls="ink")
    cv.line(bc[0] - tb[0], bc[1] + tb[1], tc[0] - tt[0], tc[1] + tt[1], cls="ink")
    cv.line(bc[0] + tb[0], bc[1] + tb[1], tc[0] + tt[0], tc[1] + tt[1], cls="ink")
    return bc, tc, tb, tt


def _height_mark(cv: Canvas, view: _View, h: float, label: str,
                 side: float = -1.0, avoid: Sequence = ()) -> None:
    """Trục cao vẽ đứt (nó nằm trong lòng khối nên là nét khuất) + ký hiệu vuông góc.

    ``avoid`` là các cạnh (toạ độ màn hình) mà nhãn phải tránh — xem ``_ne_nhan``.
    """
    bc = view.p(0.0, 0.0, 0.0)
    tc = view.p(0.0, 0.0, h)
    cv.line(*bc, *tc, cls="accent-b", extra=_DASH + _THIN)
    edge = view.p(side, 0.0, 0.0)
    cv.right_angle(bc[0], bc[1], edge[0], edge[1], tc[0], tc[1], size=11)
    ly = (bc[1] + tc[1]) / 2.0
    lx, anchor = _ne_nhan(bc[0], ly, avoid, label)
    cv.text(lx, ly, label, cls="lbl", anchor=anchor)


# --------------------------------------------------------------------------
# Khối đa diện
# --------------------------------------------------------------------------
def build_box3d(p: Params) -> str:
    """Hình hộp chữ nhật a×b×c: ba kích thước, tuỳ chọn đường chéo và mặt cầu ngoại tiếp."""
    a = _dim(p, "a", 3.6)      # theo trục x — cạnh trước-dưới
    b = _dim(p, "b", 2.4)      # theo trục y — chiều sâu
    c = _dim(p, "c", 2.6)      # theo trục z — chiều cao
    la = str(p.get("label_a", "a"))
    lb = str(p.get("label_b", "b"))
    lc = str(p.get("label_c", "c"))
    highlight = str(p.get("highlight", ""))
    sphere = bool(p.get("circumsphere", False))
    diagonal = bool(p.get("diagonal", False)) or sphere

    view = _View(_scale_for(a + 0.7 * b))
    verts = [(0, 0, 0), (a, 0, 0), (a, b, 0), (0, b, 0),
             (0, 0, c), (a, 0, c), (a, b, c), (0, b, c)]
    faces = _prism_faces(4)
    radius = math.sqrt(a * a + b * b + c * c) / 2.0
    disks = [((a / 2, b / 2, c / 2), view.rx(radius), view.rx(radius))] if sphere else []
    w, h = view.fit(verts, disks, left=40.0, right=64.0, top=32.0, bottom=44.0)

    cv = Canvas(w, h, title=str(p.get("title", "Hình hộp chữ nhật")),
                desc=str(p.get("desc", "Hình hộp chữ nhật với ba kích thước đáy và chiều cao")))
    flags = _face_flags(verts, faces)
    fills: dict[int, str] = {}
    if highlight == "xq":
        # Chỉ tô mặt bên NHÌN THẤY: tô cả bốn mặt thì hai mặt sau chồng lên hai
        # mặt trước, chỗ đậm chỗ nhạt, nhìn ra một khối lỗ chỗ chứ không ra "xung quanh".
        fills = {i: "fill-a" for i in range(2, 6) if flags[i]}
    elif highlight == "day":
        fills = {0: "fill-c"}
    pts = _draw_polyhedron(cv, view, verts, faces, flags, fills)

    if sphere:
        center = view.p(a / 2, b / 2, c / 2)
        # Phép chiếu là trực giao nên ảnh của mặt cầu là ĐƯỜNG TRÒN bán kính R·s.
        cv.circle(center[0], center[1], view.rx(radius), cls="ink-thin")
        # Bán kính nối tới đỉnh (0, 0, c) chứ KHÔNG tới (a, b, c): tâm là trung
        # điểm đường chéo, nối tới đỉnh ấy thì đoạn R nằm trọn trong đường chéo
        # và biến mất dưới nét của nó — người học chỉ còn thấy một đoạn thẳng,
        # không biết R đo từ đâu tới đâu. Đỉnh (a, 0, c) cũng không dùng được:
        # ảnh của nó lệch chưa tới 6° so với đường chéo.
        cv.line(*center, *pts[4], cls="accent-c", extra=_THIN)
        cv.text((center[0] + pts[4][0]) / 2 - 5, (center[1] + pts[4][1]) / 2 - 6,
                str(p.get("label_radius", "R")), cls="lbl", anchor="end")
        cv.dot(*center, r=2.8, cls="accent-c")
    if diagonal:
        cv.line(*pts[0], *pts[6], cls="accent-b", extra=_THIN)
        # Nhãn lệch theo phương VUÔNG GÓC với đường chéo (để không dính vào chính
        # nó), rồi chọn phía nào thoáng hơn. Đặt cứng ở giữa và lệch xuống thì với
        # hình lập phương nó rơi đúng vào chân cạnh đứng khuất.
        dx, dy = pts[6][0] - pts[0][0], pts[6][1] - pts[0][1]
        norm = math.hypot(dx, dy) or 1.0
        mx = pts[0][0] + 0.34 * dx
        my = pts[0][1] + 0.34 * dy
        ox, oy = -dy / norm * 14.0, dx / norm * 14.0
        canh = _canh_cua(pts, faces)
        lx, ly = max(((mx + ox, my + oy), (mx - ox, my - oy)),
                     key=lambda q: _xa_net(q[0], q[1], canh))
        cv.text(lx, ly, str(p.get("label_diagonal", "d")), cls="lbl", anchor="middle")
    if la:
        cv.text((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2 + 20, la,
                cls="lbl", anchor="middle")
    if lb:
        cv.text((pts[1][0] + pts[2][0]) / 2 + 8, (pts[1][1] + pts[2][1]) / 2 + 16, lb, cls="lbl")
    if lc:
        cv.text((pts[2][0] + pts[6][0]) / 2 + 10, (pts[2][1] + pts[6][1]) / 2 + 4, lc, cls="lbl")
    if highlight == "day":
        bx, by, anchor = _base_label_pos(view, [verts[i] for i in faces[0]])
        cv.text(bx, by, str(p.get("label_base", "S đáy")), cls="lbl-sm", anchor=anchor)
    return cv.render()


def build_cube3d(p: Params) -> str:
    """Hình lập phương cạnh a (chỉ ghi nhãn một cạnh — ba cạnh bằng nhau)."""
    a = _dim(p, "a", 2.8)
    q = dict(p)
    q.update(a=a, b=a, c=a,
             label_a=p.get("label_a", "a"), label_b="", label_c="",
             label_diagonal=p.get("label_diagonal", "d"),
             title=p.get("title", "Hình lập phương"),
             desc=p.get("desc", "Hình lập phương cạnh a"))
    return build_box3d(q)


def build_prism3d(p: Params) -> str:
    """Lăng trụ đứng: đáy tam giác/tam giác đều/lục giác/tứ giác, chiều cao h."""
    kind = str(p.get("base", "tam-giac-deu"))
    a = _dim(p, "a", 2.6)
    h = _dim(p, "h", 3.0)
    highlight = str(p.get("highlight", "day"))
    base, regular = _base_polygon(kind, a)
    n = len(base)

    span = max(max(x for x, _ in base) - min(x for x, _ in base),
               max(y for _, y in base) - min(y for _, y in base))
    view = _View(_scale_for(max(1.35 * span, 0.85 * h + 0.6 * span)))
    verts = [(x, y, 0.0) for x, y in base] + [(x, y, h) for x, y in base]
    faces = _prism_faces(n)
    w, hgt = view.fit(verts, left=46.0, right=60.0, top=34.0, bottom=44.0)

    cv = Canvas(w, hgt, title=str(p.get("title", "Hình lăng trụ đứng")),
                desc=str(p.get("desc", "Lăng trụ đứng với đáy và chiều cao được đánh dấu")))
    flags = _face_flags(verts, faces)
    fills: dict[int, str] = {}
    if highlight == "xq":
        fills = {i: "fill-a" for i in range(2, 2 + n) if flags[i]}
    elif highlight == "day":
        fills = {0: "fill-c"}
    pts = _draw_polyhedron(cv, view, verts, faces, flags, fills)

    # Chiều cao ghi ở cạnh bên ngoài cùng bên phải: cạnh ấy chắc chắn là nét thấy
    # và không có nét nào của khối cắt ngang nhãn.
    right = max(range(n), key=lambda i: pts[i][0])
    cv.line(*pts[right], *pts[right + n], cls="accent-b", extra=_THIN)
    cv.text(pts[right][0] + 10, (pts[right][1] + pts[right + n][1]) / 2 + 4,
            str(p.get("label_h", "h")), cls="lbl")
    if regular:
        i = _nearest_edge(base, view)
        j = (i + 1) % n
        cv.text((pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2 + 20,
                str(p.get("label_a", "a")), cls="lbl", anchor="middle")
    if highlight == "day":
        bx, by, anchor = _base_label_pos(view, [verts[i] for i in faces[0]])
        cv.text(bx, by, str(p.get("label_base", "S đáy")), cls="lbl-sm", anchor=anchor)
    return cv.render()


def build_pyramid3d(p: Params) -> str:
    """Hình chóp: đáy vuông/tam giác/lục giác, chiều cao h, tuỳ chọn trung đoạn."""
    kind = str(p.get("base", "vuong"))
    a = _dim(p, "a", 2.6)
    h = _dim(p, "h", 3.0)
    highlight = str(p.get("highlight", "day"))
    slant = bool(p.get("slant", False))
    apothem = bool(p.get("apothem", False))
    base, regular = _base_polygon(kind, a)
    n = len(base)

    span = max(max(x for x, _ in base) - min(x for x, _ in base),
               max(y for _, y in base) - min(y for _, y in base))
    view = _View(_scale_for(max(1.35 * span, 0.9 * h + 0.5 * span)))
    verts = [(x, y, 0.0) for x, y in base] + [(0.0, 0.0, h)]
    faces = [list(range(n))] + [[i, (i + 1) % n, n] for i in range(n)]
    w, hgt = view.fit(verts, left=46.0, right=58.0, top=34.0, bottom=46.0)

    cv = Canvas(w, hgt, title=str(p.get("title", "Hình chóp")),
                desc=str(p.get("desc", "Hình chóp với diện tích đáy và chiều cao được đánh dấu")))
    flags = _face_flags(verts, faces)
    fills: dict[int, str] = {}
    if highlight == "xq":
        fills = {i: "fill-a" for i in range(1, 1 + n) if flags[i]}
    elif highlight == "day":
        fills = {0: "fill-c"}
    pts = _draw_polyhedron(cv, view, verts, faces, flags, fills)

    # Nhãn h phải né cạnh bên, và né cả trung đoạn nếu có vẽ — nên hình học của
    # trung đoạn tính TRƯỚC khi đánh dấu chiều cao, dù nó được vẽ sau.
    i = _nearest_edge(base, view)
    j = (i + 1) % n
    mid = ((base[i][0] + base[j][0]) / 2.0, (base[i][1] + base[j][1]) / 2.0)
    mx, my = view.p(mid[0], mid[1], 0.0)
    apex = pts[n]
    net = [(pts[k], apex) for k in range(n)]
    if slant:
        net.append(((mx, my), apex))
    _height_mark(cv, view, h, str(p.get("label_h", "h")), avoid=net)
    if slant or apothem:
        if slant:
            cv.line(mx, my, *apex, cls="accent-d", extra=_THIN)
            cv.text((mx + apex[0]) / 2 - 8, (my + apex[1]) / 2 + 4,
                    str(p.get("label_slant", "d")), cls="lbl", anchor="end")
            # Trung đoạn vuông góc với cạnh đáy — không đánh dấu thì nó chỉ là
            # một đoạn xiên bất kì, và công thức S_xq = p·d mất chỗ dựa.
            cv.right_angle(mx, my, pts[j][0], pts[j][1], apex[0], apex[1], size=10)
        if apothem:
            ox, oy = view.p(0.0, 0.0, 0.0)
            cv.line(ox, oy, mx, my, cls="accent-c", extra=_DASH + _THIN)
            cv.text((ox + mx) / 2, (oy + my) / 2 - 6,
                    str(p.get("label_apothem", "r")), cls="lbl", anchor="middle")
    if regular:
        i = _nearest_edge(base, view)
        j = (i + 1) % n
        cv.text((pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2 + 21,
                str(p.get("label_a", "a")), cls="lbl", anchor="middle")
    if highlight == "day":
        bx, by, anchor = _base_label_pos(view, [verts[i] for i in faces[0]], axis=True)
        cv.text(bx, by, str(p.get("label_base", "S đáy")), cls="lbl-sm", anchor=anchor)
    return cv.render()


def build_pyramid_frustum3d(p: Params) -> str:
    """Hình chóp cụt đáy vuông: đáy lớn a, đáy nhỏ b, chiều cao h."""
    a = _dim(p, "a", 3.0)
    b = _dim(p, "b", 1.7)
    h = _dim(p, "h", 2.4)
    lower, _ = _base_polygon("vuong", a)
    upper, _ = _base_polygon("vuong", b)

    view = _View(_scale_for(max(1.4 * a, 0.9 * h + 0.5 * a)))
    verts = [(x, y, 0.0) for x, y in lower] + [(x, y, h) for x, y in upper]
    faces = _prism_faces(4)
    w, hgt = view.fit(verts, left=48.0, right=58.0, top=38.0, bottom=44.0)

    cv = Canvas(w, hgt, title=str(p.get("title", "Hình chóp cụt")),
                desc=str(p.get("desc", "Hình chóp cụt với hai đáy song song và chiều cao")))
    flags = _face_flags(verts, faces)
    pts = _draw_polyhedron(cv, view, verts, faces, flags, {0: "fill-c", 1: "fill-a"})
    canh_ben = [(pts[i], pts[4 + i]) for i in range(4)]
    _height_mark(cv, view, h, str(p.get("label_h", "h")), avoid=canh_ben)

    bx, by = view.p(*_centroid([verts[i] for i in faces[0]]))
    cv.text(bx, by + 17, str(p.get("label_base", "B")), cls="lbl", anchor="middle")
    # Nhãn đáy nhỏ nằm ngay dưới đỉnh trục cao và ngay cạnh bên khuất chạy dọc —
    # để giữa là bị cả hai nét xuyên qua.
    tx, ty = view.p(*_centroid([verts[i] for i in faces[1]]))
    ltop = str(p.get("label_top", "B′"))
    lx, anchor = _ne_nhan(tx, ty + 5, canh_ben, ltop)
    cv.text(lx, ty + 5, ltop, cls="lbl", anchor=anchor)
    return cv.render()


def build_tetrahedron3d(p: Params) -> str:
    """Tứ diện: ``mode='deu'`` tứ diện đều cạnh a, ``mode='vuong'`` tứ diện vuông a,b,c."""
    mode = str(p.get("mode", "deu"))
    if mode == "vuong":
        a = _dim(p, "a", 2.6)
        b = _dim(p, "b", 3.2)
        c = _dim(p, "c", 2.6)
        verts = [(0.0, 0.0, 0.0), (a, 0.0, 0.0), (0.0, b, 0.0), (0.0, 0.0, c)]
        view = _View(_scale_for(max(a + 0.7 * b, 0.9 * c + 0.5 * b)))
        title = "Tứ diện vuông"
    else:
        a = _dim(p, "a", 2.6)
        base, _ = _base_polygon("tam-giac-deu", a)
        height = a * math.sqrt(6.0) / 3.0
        verts = [(x, y, 0.0) for x, y in base] + [(0.0, 0.0, height)]
        view = _View(_scale_for(max(1.5 * a, 0.9 * height + 0.5 * a)))
        title = "Tứ diện đều"
    faces = [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]]
    w, hgt = view.fit(verts, left=48.0, right=56.0, top=34.0, bottom=44.0)

    cv = Canvas(w, hgt, title=str(p.get("title", title)),
                desc=str(p.get("desc", "Khối tứ diện với các cạnh được đánh dấu")))
    flags = _face_flags(verts, faces)
    pts = _draw_polyhedron(cv, view, verts, faces, flags, {})
    canh = [(pts[i], pts[j]) for i, j in
            ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))]

    if mode == "vuong":
        cv.right_angle(pts[0][0], pts[0][1], pts[1][0], pts[1][1], pts[3][0], pts[3][1], size=11)
        cv.right_angle(pts[0][0], pts[0][1], pts[2][0], pts[2][1], pts[3][0], pts[3][1], size=11)
        cv.text((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2 + 19,
                str(p.get("label_a", "a")), cls="lbl", anchor="middle")
        cv.text((pts[0][0] + pts[2][0]) / 2 + 6, (pts[0][1] + pts[2][1]) / 2 + 17,
                str(p.get("label_b", "b")), cls="lbl")
        cv.text(pts[0][0] - 10, (pts[0][1] + pts[3][1]) / 2, str(p.get("label_c", "c")),
                cls="lbl", anchor="end")
        if p.get("show_height"):
            # Chân đường cao hạ từ đỉnh vuông xuống mặt (ABC): H = h²·(1/a; 1/b; 1/c),
            # đúng theo 1/h² = 1/a² + 1/b² + 1/c² — vẽ được thì công thức tự lộ ra.
            inv = 1.0 / (a * a) + 1.0 / (b * b) + 1.0 / (c * c)
            hh = 1.0 / inv
            foot = view.p(hh / a, hh / b, hh / c)
            cv.line(*pts[0], *foot, cls="accent-b", extra=_THIN)
            cv.dot(*foot, r=2.8, cls="accent-b")
            # Đường cao này đi gần như song song với cạnh b (cả hai đều hướng ra
            # sau-phải trên màn hình), nên nhãn phải tự chọn phía trống.
            lh = str(p.get("label_h", "h"))
            ly = (pts[0][1] + foot[1]) / 2.0 - 4
            lx, anchor = _ne_nhan((pts[0][0] + foot[0]) / 2.0, ly, canh, lh)
            cv.text(lx, ly, lh, cls="lbl", anchor=anchor)
    else:
        i = _nearest_edge([(v[0], v[1]) for v in verts[:3]], view)
        j = (i + 1) % 3
        cv.text((pts[i][0] + pts[j][0]) / 2, (pts[i][1] + pts[j][1]) / 2 + 20,
                str(p.get("label_a", "a")), cls="lbl", anchor="middle")
        if p.get("show_height", True):
            _height_mark(cv, view, verts[3][2], str(p.get("label_h", "h")),
                         avoid=[(pts[i], pts[3]) for i in range(3)])
    return cv.render()


# --------------------------------------------------------------------------
# Khối tròn xoay
# --------------------------------------------------------------------------
def build_cylinder3d(p: Params) -> str:
    """Hình trụ: bán kính đáy r, chiều cao h; tuỳ chọn thiết diện qua trục."""
    r = _dim(p, "r", 1.5)
    h = _dim(p, "h", 3.2)
    section = bool(p.get("axial_section", False))
    highlight = str(p.get("highlight", ""))

    view = _View(_scale_for(max(2.4 * r, 0.9 * h + 0.8 * r)))
    corners = [(r, 0, 0), (-r, 0, 0), (r, 0, h), (-r, 0, h)]
    disks = [((0, 0, 0), view.rx(r), view.ry(r)), ((0, 0, h), view.rx(r), view.ry(r))]
    w, hgt = view.fit(corners, disks, left=46.0, right=58.0, top=36.0, bottom=42.0)

    cv = Canvas(w, hgt, title=str(p.get("title", "Hình trụ")),
                desc=str(p.get("desc", "Hình trụ với bán kính đáy và chiều cao được đánh dấu")))
    bc, tc, _, _ = _round_body(cv, view, r, r, h)
    if highlight == "day":
        cv.path(_disk(bc[0], bc[1], view.rx(r), view.ry(r)), cls="fill-c")
    if section:
        # Thiết diện qua trục nằm trong mặt phẳng y = 0 (mặt phẳng quay về mắt),
        # nên nó hiện ra trọn vẹn chứ không bị thân trụ che.
        ux, uy = r * _U[0], r * _U[1]
        quad = [view.p(-ux, -uy, 0), view.p(ux, uy, 0),
                view.p(ux, uy, h), view.p(-ux, -uy, h)]
        cv.polygon(quad, cls="fill-b")
        cv.polyline(quad + [quad[0]], cls="accent-b", extra=_THIN + _NOFILL)
        cv.text((quad[0][0] + quad[1][0]) / 2, (quad[0][1] + quad[1][1]) / 2 + 19,
                str(p.get("label_width", "2r")), cls="lbl", anchor="middle")

    cv.line(*bc, *tc, cls="accent-b", extra=_DASH + _THIN)
    cv.right_angle(bc[0], bc[1], bc[0] - 14, bc[1], tc[0], tc[1], size=10)
    cv.text(bc[0] + 8, (bc[1] + tc[1]) / 2, str(p.get("label_h", "h")), cls="lbl")
    cv.line(tc[0], tc[1], tc[0] + view.rx(r), tc[1], cls="accent-c", extra=_THIN)
    cv.dot(*tc, r=2.6, cls="accent-c")
    cv.text(tc[0] + view.rx(r) / 2, tc[1] - 7, str(p.get("label_r", "r")),
            cls="lbl", anchor="middle")
    return cv.render()


def build_cone3d(p: Params) -> str:
    """Hình nón: bán kính đáy r, chiều cao h, đường sinh l; tuỳ chọn thiết diện qua trục."""
    r = _dim(p, "r", 1.6)
    h = _dim(p, "h", 3.0)
    show_l = bool(p.get("show_l", True))
    section = bool(p.get("axial_section", False))
    highlight = str(p.get("highlight", ""))

    view = _View(_scale_for(max(2.4 * r, 0.9 * h + 0.8 * r)))
    apex_world = (0.0, 0.0, h)
    disks = [((0, 0, 0), view.rx(r), view.ry(r))]
    w, hgt = view.fit([apex_world, (r, 0, 0), (-r, 0, 0)], disks,
                      left=46.0, right=58.0, top=36.0, bottom=42.0)

    cv = Canvas(w, hgt, title=str(p.get("title", "Hình nón")),
                desc=str(p.get("desc", "Hình nón với bán kính đáy, chiều cao và đường sinh")))
    bc = view.p(0.0, 0.0, 0.0)
    apex = view.p(*apex_world)
    rx, ry = view.rx(r), view.ry(r)
    dx, dy = _tangent(rx, ry, bc[1] - apex[1])
    cv.path(f"M {_n(apex[0])} {_n(apex[1])} L {_n(bc[0] - dx)} {_n(bc[1] - dy)} "
            f"A {_n(rx)} {_n(ry)} 0 0 0 {_n(bc[0] + dx)} {_n(bc[1] - dy)} Z", cls="fill-a")
    cv.path(_arc(bc[0] - dx, bc[1] - dy, rx, ry, bc[0] + dx, bc[1] - dy, 1),
            cls="ink-thin", extra=_DASH)
    cv.path(_arc(bc[0] - dx, bc[1] - dy, rx, ry, bc[0] + dx, bc[1] - dy, 0), cls="ink")
    if highlight == "day":
        cv.path(_disk(bc[0], bc[1], rx, ry), cls="fill-c")
    cv.line(apex[0], apex[1], bc[0] - dx, bc[1] - dy, cls="ink")
    cv.line(apex[0], apex[1], bc[0] + dx, bc[1] - dy, cls="ink")
    if section:
        ux, uy = r * _U[0], r * _U[1]
        tri = [view.p(-ux, -uy, 0), view.p(ux, uy, 0), apex]
        cv.polygon(tri, cls="fill-b")
        cv.polyline(tri + [tri[0]], cls="accent-b", extra=_THIN + _NOFILL)
        cv.text((tri[0][0] + tri[1][0]) / 2, (tri[0][1] + tri[1][1]) / 2 + 19,
                str(p.get("label_width", "2r")), cls="lbl", anchor="middle")

    cv.line(*bc, *apex, cls="accent-b", extra=_DASH + _THIN)
    cv.line(bc[0], bc[1], bc[0] + rx, bc[1], cls="accent-c", extra=_DASH + _THIN)
    cv.right_angle(bc[0], bc[1], bc[0] + 14, bc[1], apex[0], apex[1], size=10)
    cv.text(bc[0] - 8, (bc[1] + apex[1]) / 2, str(p.get("label_h", "h")),
            cls="lbl", anchor="end")
    cv.text(bc[0] + rx / 2, bc[1] - 8, str(p.get("label_r", "r")), cls="lbl", anchor="middle")
    if show_l:
        cv.text((apex[0] + bc[0] + dx) / 2 + 9, (apex[1] + bc[1] - dy) / 2,
                str(p.get("label_l", "l")), cls="lbl")
    return cv.render()


def build_cone_frustum3d(p: Params) -> str:
    """Hình nón cụt: hai bán kính đáy r₁ (dưới) và r₂ (trên), chiều cao h, đường sinh l."""
    r1 = _dim(p, "r1", 1.9)
    r2 = _dim(p, "r2", 1.05)
    h = _dim(p, "h", 2.6)
    show_l = bool(p.get("show_l", True))

    view = _View(_scale_for(max(2.4 * max(r1, r2), 0.9 * h + 0.9 * max(r1, r2))))
    disks = [((0, 0, 0), view.rx(r1), view.ry(r1)), ((0, 0, h), view.rx(r2), view.ry(r2))]
    w, hgt = view.fit([(r1, 0, 0), (-r1, 0, 0), (r2, 0, h), (-r2, 0, h)], disks,
                      left=48.0, right=58.0, top=38.0, bottom=42.0)

    cv = Canvas(w, hgt, title=str(p.get("title", "Hình nón cụt")),
                desc=str(p.get("desc", "Hình nón cụt với hai bán kính đáy, chiều cao và đường sinh")))
    bc, tc, tb, tt = _round_body(cv, view, r1, r2, h)
    cv.line(*bc, *tc, cls="accent-b", extra=_DASH + _THIN)
    cv.right_angle(bc[0], bc[1], bc[0] - 14, bc[1], tc[0], tc[1], size=10)
    cv.text(bc[0] + 8, (bc[1] + tc[1]) / 2, str(p.get("label_h", "h")), cls="lbl")
    cv.line(bc[0], bc[1], bc[0] + view.rx(r1), bc[1], cls="accent-c", extra=_DASH + _THIN)
    _sub(cv, bc[0] + view.rx(r1) / 2, bc[1] - 8, str(p.get("label_r1", "r")), "1",
         anchor="middle")
    cv.line(tc[0], tc[1], tc[0] + view.rx(r2), tc[1], cls="accent-c", extra=_THIN)
    cv.dot(*tc, r=2.6, cls="accent-c")
    # Nhãn r₂ đặt HẲN trên vành nắp: để ngay dưới tâm nắp thì nó rơi đúng vào
    # nửa trước của vành, chữ và nét elip chồng lên nhau.
    _sub(cv, tc[0] + view.rx(r2) / 2, tc[1] - view.ry(r2) - 7, str(p.get("label_r2", "r")), "2",
         anchor="middle")
    if show_l:
        cv.text((bc[0] + tb[0] + tc[0] + tt[0]) / 2 + 10,
                (bc[1] + tb[1] + tc[1] + tt[1]) / 2, str(p.get("label_l", "l")), cls="lbl")
    return cv.render()


def build_sphere3d(p: Params) -> str:
    """Hình cầu bán kính R, có xích đạo và kinh tuyến gợi khối; tuỳ chọn thiết diện."""
    R = _dim(p, "R", 2.2)
    label_r = str(p.get("label_r", "R"))
    cut = p.get("section_d")

    view = _View(_scale_for(2.7 * R))
    rr = view.rx(R)
    plane = float(cut) if isinstance(cut, (int, float)) and math.isfinite(float(cut)) else None
    if plane is not None:
        plane = max(-0.85 * R, min(0.85 * R, plane))
    reach = 1.35 * R
    frame = [(reach, reach, plane), (-reach, -reach, plane),
             (reach, -reach, plane), (-reach, reach, plane)] if plane is not None else []
    w, hgt = view.fit(frame, [((0, 0, 0), rr, rr)],
                      left=44.0, right=52.0, top=34.0, bottom=40.0)

    cv = Canvas(w, hgt, title=str(p.get("title", "Hình cầu")),
                desc=str(p.get("desc", "Hình cầu với bán kính, xích đạo và kinh tuyến")))
    center = view.p(0.0, 0.0, 0.0)
    if plane is not None:
        quad = [view.p(-reach, -reach, plane), view.p(reach, -reach, plane),
                view.p(reach, reach, plane), view.p(-reach, reach, plane)]
        cv.polygon(quad, cls="fill-c")
        cv.polyline(quad + [quad[0]], cls="ink-thin")
    cv.circle(*center, rr, cls="fill-a")
    cv.circle(*center, rr, cls="ink")
    # Xích đạo: nửa sau bị khối che nên vẽ đứt. Kinh tuyến nằm trong mặt phẳng
    # chứa trục nhìn-ngang nên nửa DƯỚI mới là nửa ở xa (đổi vai so với xích đạo).
    eq = view.ry(R)
    cv.path(_arc(center[0] - rr, center[1], rr, eq, center[0] + rr, center[1], 1),
            cls="ink-thin", extra=_DASH)
    cv.path(_arc(center[0] - rr, center[1], rr, eq, center[0] + rr, center[1], 0), cls="ink-thin")
    mer = rr * _COS_EL
    cv.path(_arc(center[0] - rr, center[1], rr, mer, center[0] + rr, center[1], 1),
            cls="ink-thin")
    cv.path(_arc(center[0] - rr, center[1], rr, mer, center[0] + rr, center[1], 0),
            cls="ink-thin", extra=_DASH)
    cv.dot(*center, r=2.8, cls="accent-b")

    if plane is None:
        ang = math.radians(-38.0)
        end = (center[0] + rr * math.cos(ang), center[1] + rr * math.sin(ang))
        cv.line(*center, *end, cls="accent-b", extra=_THIN)
        cv.text((center[0] + end[0]) / 2 + 2, (center[1] + end[1]) / 2 - 7, label_r, cls="lbl")
        cv.text(center[0] - 6, center[1] + 15, "O", cls="lbl-sm", anchor="end")
    else:
        r_cut = math.sqrt(max(R * R - plane * plane, 1e-9))
        icx, icy = view.p(0.0, 0.0, plane)
        cv.path(_disk(icx, icy, view.rx(r_cut), view.ry(r_cut)), cls="accent-a",
                extra=' stroke-width="2"' + _NOFILL)
        rim = (icx + view.rx(r_cut), icy)
        cv.line(*center, icx, icy, cls="accent-b", extra=_THIN)
        cv.line(icx, icy, *rim, cls="accent-c", extra=_THIN)
        cv.line(*center, *rim, cls="accent-d", extra=_THIN)
        cv.right_angle(icx, icy, center[0], center[1], rim[0], rim[1], size=10)
        cv.text(center[0] - 7, (center[1] + icy) / 2, str(p.get("label_d", "d")),
                cls="lbl", anchor="end")
        cv.text((icx + rim[0]) / 2, icy + 15, str(p.get("label_cut", "r")),
                cls="lbl", anchor="middle")
        cv.text((center[0] + rim[0]) / 2 + 4, (center[1] + rim[1]) / 2 + 16, label_r, cls="lbl")
        cv.dot(icx, icy, r=2.6, cls="accent-a")
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "box3d": build_box3d,
    "cube3d": build_cube3d,
    "prism3d": build_prism3d,
    "pyramid3d": build_pyramid3d,
    "pyramid_frustum3d": build_pyramid_frustum3d,
    "tetrahedron3d": build_tetrahedron3d,
    "cylinder3d": build_cylinder3d,
    "cone3d": build_cone3d,
    "cone_frustum3d": build_cone_frustum3d,
    "sphere3d": build_sphere3d,
}
