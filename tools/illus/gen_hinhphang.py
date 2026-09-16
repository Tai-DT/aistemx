"""Generator SVG cho họ hình học phẳng mở rộng.

Bổ sung những hình mà chương trình THCS/THPT dùng liên tục nhưng tầng minh hoạ
chưa chạm tới: hình thoi/vuông/đa giác đều, cả chương đường tròn (dây, cung,
tiếp tuyến, góc ở tâm, góc nội tiếp, phương tích), các đường đồng quy trong tam
giác, giải tam giác (định lí sin/cosin) và hệ thức lượng trong tam giác vuông.

Ba quy ước xuyên suốt file — nắm ba cái này thì đọc chỗ nào cũng ra:

1. **Toạ độ thế giới là y-HƯỚNG-LÊN**, như trong sách hình học. ``_Frame`` lo việc
   lật sang toạ độ màn hình (y hướng xuống). Nhờ đó công thức hình học chép thẳng
   từ sách vào được, không phải đổi dấu ở từng dòng — chỗ đổi dấu rải rác là
   nguồn sai hình phổ biến nhất.
2. **Khung vẽ tính SAU khi đã biết mọi điểm.** Mỗi generator dựng đủ điểm rồi mới
   khởi tạo ``_Frame``; hình tràn ra ngoài viewBox là lỗi im lặng (SVG vẫn render,
   chỉ mất một góc hình) nên không được để nó xảy ra vì quên cộng lề.
3. **Tham số kích thước đi qua ``_pos``.** Người dùng truyền 0 hay số âm thì hình
   bị bóp về một điểm mà vẫn ra SVG hợp lệ — cũng là một kiểu sai im lặng, nên
   ``_pos`` kéo về mặc định thay vì vẽ ra thứ vô nghĩa.
"""

from __future__ import annotations

import math
from typing import Callable, Iterable, Sequence

from .svgkit import Canvas, _n, esc

Params = dict
Pt = tuple[float, float]


# --------------------------------------------------------------------------
# Tiện ích hình học (toạ độ thế giới, y hướng lên)
# --------------------------------------------------------------------------
def _pos(value, fallback: float) -> float:
    """Ép một tham số KÍCH THƯỚC về số dương hữu hạn, sai thì lấy mặc định."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return fallback
    if not math.isfinite(v) or v <= 0:
        return fallback
    return min(v, 1e6)


def _num(value, fallback: float) -> float:
    """Tham số có dấu (góc, toạ độ): chỉ chặn NaN/inf và giá trị phi số."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        return fallback
    return v if math.isfinite(v) else fallback


def _clamp(v: float, lo: float, hi: float) -> float:
    return lo if v < lo else (hi if v > hi else v)


def _mid(P: Pt, Q: Pt) -> Pt:
    return ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)


def _dist(P: Pt, Q: Pt) -> float:
    return math.hypot(Q[0] - P[0], Q[1] - P[1])


def _lerp(P: Pt, Q: Pt, t: float) -> Pt:
    return (P[0] + (Q[0] - P[0]) * t, P[1] + (Q[1] - P[1]) * t)


def _foot(P: Pt, A: Pt, B: Pt) -> Pt:
    """Chân đường vuông góc hạ từ P xuống đường thẳng AB."""
    dx, dy = B[0] - A[0], B[1] - A[1]
    dd = dx * dx + dy * dy
    if dd == 0:
        return A
    t = ((P[0] - A[0]) * dx + (P[1] - A[1]) * dy) / dd
    return (A[0] + t * dx, A[1] + t * dy)


def _away(P: Pt, ref: Pt, d: float) -> Pt:
    """Dời P ra xa ``ref`` một khoảng d — dùng đẩy nhãn ra ngoài hình."""
    ux, uy = P[0] - ref[0], P[1] - ref[1]
    L = math.hypot(ux, uy)
    if L == 0:
        return (P[0], P[1] + d)
    return (P[0] + ux / L * d, P[1] + uy / L * d)


def _perp_off(P: Pt, Q: Pt, ref: Pt, d: float) -> Pt:
    """Điểm cách trung điểm PQ khoảng d theo phương VUÔNG GÓC, về phía xa ``ref``.

    Nhãn của một đoạn xiên (trung tuyến, phân giác) mà đẩy dọc theo đoạn thì rơi
    ngay lên nét vẽ; đẩy vuông góc mới tách được chữ khỏi đường.
    """
    M = _mid(P, Q)
    ux, uy = Q[0] - P[0], Q[1] - P[1]
    L = math.hypot(ux, uy)
    if L == 0:
        return M
    nx, ny = -uy / L, ux / L
    plus = (M[0] + nx * d, M[1] + ny * d)
    minus = (M[0] - nx * d, M[1] - ny * d)
    return plus if _dist(plus, ref) > _dist(minus, ref) else minus


def _centroid(pts: Sequence[Pt]) -> Pt:
    return (sum(q[0] for q in pts) / len(pts), sum(q[1] for q in pts) / len(pts))


def _circumcenter(A: Pt, B: Pt, C: Pt) -> Pt | None:
    """Tâm đường tròn ngoại tiếp; None nếu ba điểm thẳng hàng."""
    d = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    if abs(d) < 1e-9:
        return None
    a2, b2, c2 = A[0] ** 2 + A[1] ** 2, B[0] ** 2 + B[1] ** 2, C[0] ** 2 + C[1] ** 2
    ox = (a2 * (B[1] - C[1]) + b2 * (C[1] - A[1]) + c2 * (A[1] - B[1])) / d
    oy = (a2 * (C[0] - B[0]) + b2 * (A[0] - C[0]) + c2 * (B[0] - A[0])) / d
    return (ox, oy)


def _incenter(A: Pt, B: Pt, C: Pt) -> tuple[Pt, float]:
    """Tâm và bán kính đường tròn nội tiếp (trọng số là độ dài cạnh đối diện)."""
    a, b, c = _dist(B, C), _dist(C, A), _dist(A, B)
    s = a + b + c
    I = ((a * A[0] + b * B[0] + c * C[0]) / s, (a * A[1] + b * B[1] + c * C[1]) / s)
    return I, 2 * _area(A, B, C) / s


def _excenter(A: Pt, B: Pt, C: Pt) -> tuple[Pt, float]:
    """Tâm và bán kính đường tròn BÀNG tiếp trong góc A (đối diện cạnh a)."""
    a, b, c = _dist(B, C), _dist(C, A), _dist(A, B)
    s = -a + b + c
    if abs(s) < 1e-9:
        return _incenter(A, B, C)
    J = ((-a * A[0] + b * B[0] + c * C[0]) / s, (-a * A[1] + b * B[1] + c * C[1]) / s)
    return J, 2 * _area(A, B, C) / s


def _area(A: Pt, B: Pt, C: Pt) -> float:
    return abs((B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])) / 2


def _line_circle(M: Pt, direction: Pt, O: Pt, R: float) -> list[Pt]:
    """Giao của tia/đường thẳng qua M theo ``direction`` với đường tròn (O; R).

    Trả về danh sách đã sắp theo tham số t tăng dần (tức là theo chiều đi từ M),
    rỗng nếu không cắt. Nhờ vậy chỗ gọi phân biệt được điểm gần/xa M — thứ tự này
    chính là thứ tự A, B trong hệ thức phương tích MA·MB.
    """
    dx, dy = direction
    L = math.hypot(dx, dy)
    if L == 0:
        return []
    dx, dy = dx / L, dy / L
    fx, fy = M[0] - O[0], M[1] - O[1]
    b = 2 * (fx * dx + fy * dy)
    c = fx * fx + fy * fy - R * R
    disc = b * b - 4 * c
    if disc < 0:
        return []
    sq = math.sqrt(disc)
    ts = sorted(((-b - sq) / 2, (-b + sq) / 2))
    return [(M[0] + t * dx, M[1] + t * dy) for t in ts]


class _Frame:
    """Ánh xạ toạ độ thế giới (y lên) sang toạ độ màn hình (y xuống).

    Tỉ lệ suy ra từ bao lồi của chính hình chứ không cố định, nên tham số quá lớn
    (R = 10⁶) hay quá nhỏ cũng cho ra khung vẽ cùng cỡ — chỉ nhãn số là đổi.
    """

    def __init__(self, pts: Iterable[Pt], span: float = 300.0, pad: float = 56.0,
                 max_scale: float = 62.0):
        pts = list(pts) or [(0.0, 0.0)]
        xs = [q[0] for q in pts]
        ys = [q[1] for q in pts]
        self.minx, self.maxx = min(xs), max(xs)
        self.miny, self.maxy = min(ys), max(ys)
        ext = max(self.maxx - self.minx, self.maxy - self.miny)
        self.scale = max_scale if ext <= 1e-9 else min(span / ext, max_scale)
        self.pad = pad
        self.w = (self.maxx - self.minx) * self.scale + 2 * pad
        self.h = (self.maxy - self.miny) * self.scale + 2 * pad

    def P(self, x: float, y: float) -> Pt:
        return (self.pad + (x - self.minx) * self.scale,
                self.pad + (self.maxy - y) * self.scale)

    def pt(self, W: Pt) -> Pt:
        return self.P(W[0], W[1])

    def all(self, ws: Iterable[Pt]) -> list[Pt]:
        return [self.pt(w) for w in ws]


# --------------------------------------------------------------------------
# Tiện ích vẽ (toạ độ màn hình)
# --------------------------------------------------------------------------
def _on(C: Pt, r: float, deg: float) -> Pt:
    """Điểm trên đường tròn tâm C ở góc lượng giác ``deg`` (màn hình, y xuống)."""
    a = math.radians(deg)
    return (C[0] + r * math.cos(a), C[1] - r * math.sin(a))


def _arc_d(C: Pt, r: float, a1: float, a2: float) -> str:
    """Path cung tròn đi từ góc a1 tới a2 (độ), theo đúng chiều a1 → a2.

    y của SVG hướng xuống, nên chiều dương lượng giác (a2 > a1) ứng với
    sweep-flag = 0 — đảo hai cờ này là cách nhanh nhất để vẽ ra cung bù.
    """
    P1, P2 = _on(C, r, a1), _on(C, r, a2)
    large = 1 if abs(a2 - a1) > 180 else 0
    sweep = 0 if a2 >= a1 else 1
    return (f"M {_n(P1[0])} {_n(P1[1])} A {_n(r)} {_n(r)} 0 {large} {sweep} "
            f"{_n(P2[0])} {_n(P2[1])}")


def _arc_span(C: Pt, P1: Pt, P2: Pt, through: Pt) -> tuple[float, float]:
    """Góc đầu và góc quét (có dấu) của cung P1 → P2 đi qua phía ``through``.

    Hai điểm trên đường tròn luôn chia nó thành hai cung; chọn nhầm cung là kiểu
    sai hình không ai phát hiện được, nên chỗ nào cũng phải nêu rõ cung nào.
    """
    a1, a2, at = _ang_deg(C, P1), _ang_deg(C, P2), _ang_deg(C, through)
    d = (a2 - a1) % 360
    dt = (at - a1) % 360
    return a1, (d if dt <= d else d - 360)


def _arc_through_d(C: Pt, r: float, P1: Pt, P2: Pt, through: Pt) -> str:
    a1, sweep = _arc_span(C, P1, P2, through)
    return _arc_d(C, r, a1, a1 + sweep)


def _disc_d(C: Pt, r: float) -> str:
    """Path một đường tròn khép kín (dùng khi cần fill-rule, vd hình vành khăn)."""
    return (f"M {_n(C[0] - r)} {_n(C[1])} "
            f"A {_n(r)} {_n(r)} 0 1 0 {_n(C[0] + r)} {_n(C[1])} "
            f"A {_n(r)} {_n(r)} 0 1 0 {_n(C[0] - r)} {_n(C[1])} Z")


def _txt(cv: Canvas, P: Pt, s: str, cls: str = "lbl", anchor: str = "middle",
         dy: float = 4.5) -> None:
    """Nhãn canh giữa theo chiều dọc (SVG neo chữ ở đường cơ sở, không ở tâm)."""
    cv.text(P[0], P[1] + dy, s, cls=cls, anchor=anchor)


def _sub(cv: Canvas, P: Pt, base: str, sub: str, cls: str = "lbl",
         anchor: str = "middle", dy: float = 4.5) -> None:
    """Nhãn có chỉ số dưới (hₐ, mₐ, aₙ…) dựng bằng ``<tspan>``.

    Không dùng ký tự Unicode chỉ số cho CHỮ CÁI: U+2090/U+2099 vắng mặt trong
    phần lớn font hệ thống (Roboto, Segoe UI, Georgia) nên chúng hiện ra ô vuông
    — chỉ số bằng số (₁, ₂) thì an toàn, chỉ số bằng chữ thì không.
    """
    cv.raw(f'<text x="{_n(P[0])}" y="{_n(P[1] + dy)}" text-anchor="{anchor}" '
           f'class="{cls}">{esc(base)}'
           f'<tspan font-size="70%" dy="3.5">{esc(sub)}</tspan></text>')


def _ra(cv: Canvas, V: Pt, P: Pt, Q: Pt, size: float = 12.0) -> None:
    cv.right_angle(V[0], V[1], P[0], P[1], Q[0], Q[1], size)


def _ang_deg(V: Pt, P: Pt) -> float:
    """Góc lượng giác của tia VP tính bằng độ (bù dấu y của màn hình)."""
    return math.degrees(math.atan2(-(P[1] - V[1]), P[0] - V[0]))


def _angle_mark(cv: Canvas, V: Pt, P: Pt, Q: Pt, r: float = 24.0,
                label: str | None = None, cls: str = "accent-d",
                lcls: str = "lbl-sm", lgap: float = 15.0) -> None:
    """Cung đánh dấu góc PVQ (luôn lấy góc nhỏ hơn 180°) kèm nhãn đặt giữa cung."""
    a1, a2 = _ang_deg(V, P), _ang_deg(V, Q)
    d = (a2 - a1) % 360
    if d > 180:
        a1, d = a2, 360 - d
    cv.path(_arc_d(V, r, a1, a1 + d), cls=cls, extra=' style="fill:none" stroke-width="1.8"')
    if label:
        _txt(cv, _on(V, r + lgap, a1 + d / 2), label, cls=lcls)


def _ticks(cv: Canvas, P: Pt, Q: Pt, n: int = 1, size: float = 6.0,
           gap: float = 5.0) -> None:
    """Gạch ngang giữa đoạn PQ — ký hiệu quy ước cho các đoạn bằng nhau."""
    ux, uy = Q[0] - P[0], Q[1] - P[1]
    L = math.hypot(ux, uy)
    if L == 0:
        return
    ux, uy = ux / L, uy / L
    nx, ny = -uy, ux
    M = _mid(P, Q)
    for i in range(max(1, n)):
        off = (i - (max(1, n) - 1) / 2) * gap
        c = (M[0] + ux * off, M[1] + uy * off)
        cv.line(c[0] - nx * size, c[1] - ny * size,
                c[0] + nx * size, c[1] + ny * size, cls="ink-thin")


def _dash(width: float = 1.6, pattern: str = "5 4") -> str:
    return f' stroke-dasharray="{pattern}" stroke-width="{_n(width)}"'


def _fmt(v: float) -> str:
    """Số hiển thị trên nhãn: gọn, không đuôi 0, không lộ sai số dấu phẩy động."""
    r = round(v, 2)
    return _n(r if abs(r) > 1e-9 else 0.0)


def _triangle(p: Params, default=((1.9, 4.0), (0.0, 0.0), (6.0, 0.0))) -> tuple[Pt, Pt, Pt]:
    """Đọc ba đỉnh A, B, C từ params; suy biến thì trả tam giác mặc định.

    Tam giác mặc định là tam giác NHỌN lệch — trực tâm và tâm ngoại tiếp nằm
    trong hình, nên các generator vẽ đường đồng quy không bị điểm rơi ra ngoài
    khung mà không ai kiểm được.
    """
    def rd(key, fb: Pt) -> Pt:
        v = p.get(key)
        if isinstance(v, (list, tuple)) and len(v) == 2:
            return (_num(v[0], fb[0]), _num(v[1], fb[1]))
        return fb

    A, B, C = rd("A", default[0]), rd("B", default[1]), rd("C", default[2])
    if _area(A, B, C) < 1e-6:
        return default
    return A, B, C


def _tri_labels(cv: Canvas, A: Pt, B: Pt, C: Pt, names=("A", "B", "C"),
                gap: float = 17.0) -> None:
    """Nhãn ba đỉnh, đẩy ra ngoài theo hướng từ trọng tâm."""
    G = _centroid([A, B, C])
    for P, nm in zip((A, B, C), names):
        _txt(cv, _away(P, G, gap), nm, cls="lbl")


# --------------------------------------------------------------------------
# Tứ giác đặc biệt
# --------------------------------------------------------------------------
def build_rhombus(p: Params) -> str:
    """Hình thoi cho bởi hai đường chéo d₁ (ngang) và d₂ (dọc).

    Vẽ ở tư thế "quả trám" vì đó là tư thế làm bật hai tính chất then chốt: hai
    đường chéo vuông góc và cắt nhau tại trung điểm mỗi đường.
    """
    d1 = _pos(p.get("d1", 6), 6.0)
    d2 = _pos(p.get("d2", 4), 4.0)
    show_diag = bool(p.get("diagonals", True))
    show_height = bool(p.get("height", False))
    equal = bool(p.get("equal_ticks", True))

    L, R = (-d1 / 2, 0.0), (d1 / 2, 0.0)
    B, T = (0.0, -d2 / 2), (0.0, d2 / 2)
    fr = _Frame([L, R, B, T], span=280)
    sL, sR, sB, sT = fr.all([L, R, B, T])
    O = fr.pt((0.0, 0.0))

    cv = Canvas(fr.w, fr.h, title="Hình thoi",
                desc=f"Hình thoi có hai đường chéo d₁ = {_fmt(d1)} và d₂ = {_fmt(d2)} "
                     "vuông góc với nhau tại trung điểm mỗi đường.")
    cv.polygon([sL, sT, sR, sB], cls="fill-a")
    cv.polyline([sL, sT, sR, sB, sL], cls="ink")
    if show_diag:
        cv.line(*sL, *sR, cls="accent-b", extra=_dash(1.8))
        cv.line(*sB, *sT, cls="accent-c", extra=_dash(1.8))
        _ra(cv, O, sR, sT, size=11)
        # cả hai nhãn đường chéo dồn về NỬA TRÁI, chừa nửa phải cho đường cao h
        _txt(cv, (_mid(O, sL)[0], O[1] - 12), f"d₁ = {_fmt(d1)}", cls="lbl")
        _txt(cv, (O[0] - 12, _mid(O, sB)[1]), f"d₂ = {_fmt(d2)}", cls="lbl", anchor="end")
    if equal:
        for P, Q in ((sL, sT), (sT, sR), (sR, sB), (sB, sL)):
            _ticks(cv, P, Q, 1)
    if show_height:
        # Đường cao của hình thoi = khoảng cách giữa hai cạnh song song; hạ từ đỉnh
        # T xuống cạnh BR thì chân đường vuông góc luôn rơi TRONG cạnh, khác với
        # hạ từ đỉnh L (rơi ra ngoài khi hình thoi bè ngang).
        F = _foot(T, B, R)
        sF = fr.pt(F)
        cv.line(*sT, *sF, cls="accent-d", extra=_dash(1.6))
        _ra(cv, sF, sT, sR, size=10)
        _txt(cv, _away(_mid(sT, sF), sB, 15), "h", cls="lbl")
    _txt(cv, _away(_mid(sT, sR), O, 16), p.get("label_side", "a"), cls="lbl")
    return cv.render()


def build_square(p: Params) -> str:
    """Hình vuông cạnh a; ``diagonals`` = 0 / 1 / 2 đường chéo."""
    a = _pos(p.get("a", 4), 4.0)
    nd = int(_clamp(_num(p.get("diagonals", 0), 0), 0, 2))
    equal = bool(p.get("equal_ticks", True))

    A, B = (0.0, 0.0), (a, 0.0)
    C, D = (a, a), (0.0, a)
    fr = _Frame([A, B, C, D], span=270)
    sA, sB, sC, sD = fr.all([A, B, C, D])
    O = fr.pt((a / 2, a / 2))

    cv = Canvas(fr.w, fr.h, title="Hình vuông",
                desc=f"Hình vuông cạnh a = {_fmt(a)}, bốn cạnh bằng nhau và bốn góc vuông.")
    cv.polygon([sA, sB, sC, sD], cls="fill-a")
    cv.polyline([sA, sB, sC, sD, sA], cls="ink")
    _ra(cv, sA, sB, sD, size=12)
    if nd >= 1:
        cv.line(*sA, *sC, cls="accent-b", extra=_dash(1.8))
        _txt(cv, _away(_mid(sA, sC), sD, 15), p.get("label_diag", "d"), cls="lbl")
    if nd >= 2:
        cv.line(*sB, *sD, cls="accent-c", extra=_dash(1.8))
        _ra(cv, O, sC, sD, size=10)
    if equal:
        for P, Q in ((sA, sB), (sB, sC), (sC, sD), (sD, sA)):
            _ticks(cv, P, Q, 1)
    _txt(cv, (_mid(sA, sB)[0], sA[1] + 20), f"{p.get('label_side', 'a')} = {_fmt(a)}", cls="lbl")
    _txt(cv, (sA[0] - 14, _mid(sA, sD)[1]), p.get("label_side", "a"), cls="lbl", anchor="end")
    return cv.render()


def build_quad_diagonals(p: Params) -> str:
    """Tứ giác dựng theo hai đường chéo d₁, d₂ cắt nhau dưới góc φ.

    Không vẽ hình thoi cho công thức S = ½d₁d₂: hệ thức ấy đúng cho MỌI tứ giác
    có hai đường chéo vuông góc, vẽ hình thoi sẽ khiến người học tưởng là điều
    kiện bắt buộc.
    """
    d1 = _pos(p.get("d1", 6), 6.0)
    d2 = _pos(p.get("d2", 4.6), 4.6)
    phi = _clamp(_num(p.get("phi", 90), 90), 20, 160)
    t1 = _clamp(_num(p.get("t1", 0.45), 0.45), 0.15, 0.85)
    t2 = _clamp(_num(p.get("t2", 0.55), 0.55), 0.15, 0.85)

    M = (0.0, 0.0)
    u = (1.0, 0.0)
    v = (math.cos(math.radians(phi)), math.sin(math.radians(phi)))
    A = (M[0] - t1 * d1 * u[0], M[1] - t1 * d1 * u[1])
    C = (M[0] + (1 - t1) * d1 * u[0], M[1] + (1 - t1) * d1 * u[1])
    Bv = (M[0] - t2 * d2 * v[0], M[1] - t2 * d2 * v[1])
    D = (M[0] + (1 - t2) * d2 * v[0], M[1] + (1 - t2) * d2 * v[1])

    fr = _Frame([A, Bv, C, D], span=300)
    sA, sB, sC, sD, sM = fr.all([A, Bv, C, D, M])
    cv = Canvas(fr.w, fr.h, title="Tứ giác và hai đường chéo",
                desc="Tứ giác ABCD với hai đường chéo AC = d₁ và BD = d₂ cắt nhau "
                     f"dưới góc φ = {_fmt(phi)}°.")
    cv.polygon([sA, sB, sC, sD], cls="fill-a")
    cv.polyline([sA, sB, sC, sD, sA], cls="ink")
    cv.line(*sA, *sC, cls="accent-b", extra=' stroke-width="2"')
    cv.line(*sB, *sD, cls="accent-c", extra=' stroke-width="2"')
    cv.dot(*sM, r=3, cls="accent-b")
    if abs(phi - 90) < 0.5:
        _ra(cv, sM, sC, sD, size=11)
    else:
        _angle_mark(cv, sM, sC, sD, r=22, label="φ")
    _txt(cv, _away(_mid(sA, sM), _centroid([sA, sB, sC, sD]), 14), "d₁", cls="lbl")
    _txt(cv, _away(_mid(sD, sM), _centroid([sA, sB, sC, sD]), 14), "d₂", cls="lbl")
    _tri_labels(cv, sA, sB, sC, names=("A", "B", "C"))
    _txt(cv, _away(sD, _centroid([sA, sB, sC, sD]), 17), "D", cls="lbl")
    return cv.render()


# Bước góc lệch nhau dùng cho đa giác KHÔNG đều. Đỉnh vẫn nằm trên một đường tròn
# và xếp theo góc tăng dần nên đa giác chắc chắn LỒI — điều kiện của các công thức
# tổng góc / số đường chéo.
_UNEVEN = (1.0, 1.42, 0.78, 1.18, 0.88, 1.3, 0.95, 1.12)


def build_regular_polygon(p: Params) -> str:
    """Đa giác n cạnh, tuỳ chọn đường tròn ngoại tiếp / nội tiếp / đường chéo.

    ``regular=False`` cho ra một đa giác LỒI nhưng không đều — bắt buộc với những
    công thức đúng cho mọi đa giác lồi (tổng góc, số đường chéo): vẽ hình đều ở đó
    sẽ khiến người học tưởng "đều" là điều kiện của công thức.
    ``interior_angle`` nhận True (đánh dấu một góc) hoặc ``"all"`` (mọi góc).
    """
    n = int(_clamp(_num(p.get("n", 6), 6), 3, 24))
    R = _pos(p.get("R", 3), 3.0)
    regular = bool(p.get("regular", True))
    # Đường tròn ngoại tiếp / nội tiếp và góc ở tâm 360°/n chỉ đúng cho đa giác ĐỀU,
    # nên nhánh không đều tự tắt chúng thay vì vẽ ra một đường tròn không có thật.
    show_circ = bool(p.get("circumcircle", False)) and regular
    show_in = bool(p.get("incircle", False)) and regular
    show_diag = bool(p.get("diagonals", False))
    mark_interior = p.get("interior_angle", False)
    mark_central = bool(p.get("central_angle", False))
    show_side = bool(p.get("side_label", False))

    if regular:
        degs = [90 + k * 360 / n for k in range(n)]
        verts = [(R * math.cos(math.radians(t)), R * math.sin(math.radians(t))) for t in degs]
    else:
        w = [_UNEVEN[k % len(_UNEVEN)] for k in range(n)]
        total = sum(w)
        degs, acc = [], 90.0
        for wk in w:
            degs.append(acc)
            acc += 360 * wk / total
        # đỉnh đặt trên một ELIP, vẫn theo thứ tự góc tăng dần: elip lồi nên đa giác
        # nội tiếp nó chắc chắn lồi, mà cạnh và góc thì khác hẳn nhau
        verts = [(R * math.cos(math.radians(t)), 0.72 * R * math.sin(math.radians(t)))
                 for t in degs]
    fr = _Frame(verts + ([(-R, -R), (R, R)] if (show_circ or show_in) else []), span=300)
    sv = fr.all(verts)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale
    rp = Rp * math.cos(math.pi / n)

    kind = "đều" if regular else "lồi"
    cv = Canvas(fr.w, fr.h, title=f"Đa giác {kind} {n} cạnh",
                desc=f"Đa giác {kind} {n} cạnh nội tiếp đường tròn bán kính R = {_fmt(R)}.")
    if show_circ:
        cv.circle(*O, Rp, cls="ink-thin")
    if show_in:
        cv.circle(*O, rp, cls="ink-thin", extra=_dash(1.2, "4 3"))
    cv.polygon(sv, cls="fill-a")
    cv.polyline(sv + [sv[0]], cls="ink")
    if show_diag:
        for i in range(n):
            for j in range(i + 2, n):
                if i == 0 and j == n - 1:
                    continue  # cạnh, không phải đường chéo
                cv.line(*sv[i], *sv[j], cls="ink-thin")
    # Ba đại lượng R, r, a_n đều bám quanh tâm nên phải tách chúng ra ba hướng khác
    # nhau, nếu không nhãn chồng lên nhau và người đọc gán nhầm ký hiệu cho đoạn.
    v_R = sv[0]                                   # đỉnh trên cùng
    m_r = _mid(sv[n // 2], sv[n // 2 + 1]) if n >= 4 else _mid(sv[1], sv[2])
    m_side = _mid(sv[0], sv[1])
    if show_circ:
        cv.line(*O, *v_R, cls="accent-b", extra=' stroke-width="2"')
        _txt(cv, _away(_mid(O, v_R), sv[1], 13), "R", cls="lbl")
    if show_in:
        cv.line(*O, *m_r, cls="accent-c", extra=' stroke-width="2"')
        _ra(cv, m_r, O, sv[(n // 2 + 1) % n] if n >= 4 else sv[2], size=10)
        _txt(cv, _away(_mid(O, m_r), v_R, 13), "r", cls="lbl")
    if mark_central and regular:
        _angle_mark(cv, O, sv[0], sv[1], r=Rp * 0.3,
                    label=f"{_fmt(360 / n)}°", lgap=15)
    if mark_interior == "all":
        for k in range(n):
            _angle_mark(cv, sv[k], sv[(k - 1) % n], sv[(k + 1) % n], r=20)
    elif mark_interior:
        _angle_mark(cv, sv[1], sv[0], sv[2], r=22, label="α")
    if show_side:
        _sub(cv, _away(m_side, O, 16), str(p.get("label_side", "a")), "n")
    if show_circ or show_in or mark_central:
        cv.dot(*O, r=2.8, cls="accent-b")
        _txt(cv, (O[0] - 12, O[1]), "O", cls="lbl-sm", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# Đường tròn: dây, cung, tiếp tuyến, góc
# --------------------------------------------------------------------------
def build_circle_chord(p: Params) -> str:
    """Dây cung và khoảng cách từ tâm tới dây (OI ⊥ AB, IA = IB)."""
    R = _pos(p.get("R", 3), 3.0)
    d = _clamp(_pos(p.get("d", 1.5), 1.5), 0.05 * R, 0.92 * R)
    show_diameter = bool(p.get("diameter", False))
    equal = bool(p.get("equal_ticks", True))
    names = str(p.get("chord_name", "AB"))
    na, nb = (names + "AB")[0], (names + "AB")[1]

    half = math.sqrt(max(R * R - d * d, 0.0))
    A, B = (-half, -d), (half, -d)
    I = (0.0, -d)
    fr = _Frame([(-R, -R), (R, R)], span=260)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale
    sA, sB, sI = fr.all([A, B, I])

    cv = Canvas(fr.w, fr.h, title="Dây cung và khoảng cách tới tâm",
                desc=f"Đường tròn (O; R) với dây {na}{nb}; OI vuông góc với dây tại "
                     f"trung điểm I, OI = d = {_fmt(d)}.")
    cv.circle(*O, Rp, cls="ink")
    if show_diameter:
        P1, P2 = _on(O, Rp, 180), _on(O, Rp, 0)
        cv.line(*P1, *P2, cls="accent-c", extra=' stroke-width="2.2"')
        _txt(cv, (_mid(O, P2)[0], O[1] - 13), "2R", cls="lbl-sm")
    cv.line(*sA, *sB, cls="accent-a", extra=' stroke-width="2.6"')
    cv.line(*O, *sI, cls="accent-b", extra=_dash(1.8))
    # Bán kính minh hoạ vẽ lên phía TRÊN (135°), tách hẳn khỏi cụm OI–dây ở dưới;
    # nối O với A thì nhãn R và nhãn d rơi chồng lên nhau.
    Rend = _on(O, Rp, 135)
    cv.line(*O, *Rend, cls="ink-thin")
    _ra(cv, sI, O, sB, size=11)
    cv.dot(*O, r=3, cls="accent-b")
    cv.dot(*sI, r=2.8, cls="accent-b")
    if equal:
        _ticks(cv, sA, sI, 1)
        _ticks(cv, sI, sB, 1)
    _txt(cv, _away(sA, O, 15), na, cls="lbl")
    _txt(cv, _away(sB, O, 15), nb, cls="lbl")
    _txt(cv, (O[0] + 13, O[1] - 8), "O", cls="lbl-sm", anchor="start")
    _txt(cv, (sI[0] + 11, sI[1] + 15), "I", cls="lbl-sm")
    _txt(cv, (O[0] - 11, _mid(O, sI)[1]), f"d = {_fmt(d)}", cls="lbl", anchor="end")
    _txt(cv, _away(_mid(O, Rend), sB, 13), "R", cls="lbl")
    return cv.render()


def build_circle_tangent(p: Params) -> str:
    """Tiếp tuyến của đường tròn.

    ``mode``: ``tiep-diem`` (tiếp tuyến ⊥ bán kính tại tiếp điểm),
    ``hai-tiep-tuyen`` (hai tiếp tuyến cắt nhau tại M), ``tiep-tuyen-day``
    (góc tạo bởi tiếp tuyến và dây cung).
    """
    mode = str(p.get("mode", "tiep-diem"))
    R = _pos(p.get("R", 3), 3.0)

    if mode == "hai-tiep-tuyen":
        dM = _pos(p.get("dM", 2.3), 2.3) * R
        dM = max(dM, 1.25 * R)
        alpha = math.degrees(math.acos(_clamp(R / dM, -1.0, 1.0)))
        fr = _Frame([(-R, -R), (R, R), (dM, 0.0)], span=300)
        O = fr.pt((0.0, 0.0))
        Rp = R * fr.scale
        M = fr.pt((dM, 0.0))
        Ta, Tb = _on(O, Rp, alpha), _on(O, Rp, -alpha)
        cv = Canvas(fr.w, fr.h, title="Hai tiếp tuyến cắt nhau",
                    desc="Từ điểm M ngoài đường tròn (O; R) kẻ hai tiếp tuyến MA và MB; "
                         "MA = MB và MO là phân giác của góc AMB.")
        cv.circle(*O, Rp, cls="ink")
        cv.line(*M, *Ta, cls="accent-a", extra=' stroke-width="2.4"')
        cv.line(*M, *Tb, cls="accent-a", extra=' stroke-width="2.4"')
        cv.line(*O, *Ta, cls="ink-thin")
        cv.line(*O, *Tb, cls="ink-thin")
        cv.line(*O, *M, cls="accent-b", extra=_dash(1.6))
        _ra(cv, Ta, O, M, size=10)
        _ra(cv, Tb, O, M, size=10)
        _ticks(cv, M, Ta, 1)
        _ticks(cv, M, Tb, 1)
        _angle_mark(cv, M, Ta, O, r=30, label=None)
        _angle_mark(cv, M, O, Tb, r=30, label=None)
        cv.dot(*O, r=3, cls="accent-b")
        cv.dot(*M, r=3, cls="accent-b")
        _txt(cv, _away(Ta, O, 15), "A", cls="lbl")
        _txt(cv, _away(Tb, O, 15), "B", cls="lbl")
        _txt(cv, (M[0] + 14, M[1] + 4), "M", cls="lbl")
        _txt(cv, (O[0] - 6, O[1] + 16), "O", cls="lbl-sm", anchor="end")
        return cv.render()

    if mode == "tiep-tuyen-day":
        bdeg = _clamp(_num(p.get("chord_deg", -20), -20), -80, 40)
        # A đặt ở đáy đường tròn để tiếp tuyến nằm ngang: cung bị chắn nằm gọn
        # trong góc xAB, người đọc thấy ngay "nửa số đo cung" là nửa cung nào.
        fr = _Frame([(-1.5 * R, -R), (1.5 * R, R)], span=320)
        O = fr.pt((0.0, 0.0))
        Rp = R * fr.scale
        A = _on(O, Rp, -90)
        Bp = _on(O, Rp, bdeg)
        cv = Canvas(fr.w, fr.h, title="Góc tạo bởi tiếp tuyến và dây cung",
                    desc="Tiếp tuyến Ax tại A và dây AB; góc xAB bằng nửa số đo cung AB "
                         "nằm bên trong góc đó.")
        cv.circle(*O, Rp, cls="ink")
        cv.path(_arc_d(O, Rp, -90, bdeg), cls="accent-a",
                extra=' style="fill:none" stroke-width="3.4"')
        cv.line(A[0] - Rp * 1.15, A[1], A[0] + Rp * 1.25, A[1], cls="accent-c",
                extra=' stroke-width="2.2"')
        cv.line(*A, *Bp, cls="ink", extra=' stroke-width="2.2"')
        cv.line(*O, *A, cls="ink-thin")
        cv.line(*O, *Bp, cls="ink-thin")
        _angle_mark(cv, A, (A[0] + Rp, A[1]), Bp, r=26, label="α")
        _angle_mark(cv, O, A, Bp, r=Rp * 0.4, label="2α", lgap=14)
        cv.dot(*A, r=3, cls="accent-b")
        cv.dot(*Bp, r=3, cls="accent-b")
        cv.dot(*O, r=2.8, cls="accent-b")
        _txt(cv, (A[0] - 10, A[1] + 16), "A", cls="lbl")
        _txt(cv, _away(Bp, O, 15), "B", cls="lbl")
        _txt(cv, (A[0] + Rp * 1.25 + 12, A[1]), "x", cls="lbl")
        _txt(cv, (O[0] - 12, O[1] - 4), "O", cls="lbl-sm", anchor="end")
        return cv.render()

    tdeg = _num(p.get("point_deg", 35), 35)
    fr = _Frame([(-R, -R), (1.35 * R, 1.35 * R)], span=280)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale
    A = _on(O, Rp, tdeg)
    ux, uy = -(A[1] - O[1]) / Rp, (A[0] - O[0]) / Rp  # vectơ chỉ phương tiếp tuyến
    ln = Rp * 0.95
    T1 = (A[0] - ux * ln, A[1] - uy * ln)
    T2 = (A[0] + ux * ln, A[1] + uy * ln)
    cv = Canvas(fr.w, fr.h, title="Tiếp tuyến của đường tròn",
                desc="Đường thẳng a tiếp xúc đường tròn (O; R) tại A khi và chỉ khi "
                     "a vuông góc với bán kính OA tại A.")
    cv.circle(*O, Rp, cls="ink")
    cv.line(*T1, *T2, cls="accent-a", extra=' stroke-width="2.6"')
    cv.line(*O, *A, cls="accent-b", extra=' stroke-width="2"')
    _ra(cv, A, O, T2, size=12)
    cv.dot(*O, r=3, cls="accent-b")
    cv.dot(*A, r=3.2, cls="accent-b")
    _txt(cv, _away(A, O, 16), "A", cls="lbl")
    _txt(cv, _mid(O, A), "R", cls="lbl", anchor="end", dy=-4)
    _txt(cv, _away(T2, A, 12), "a", cls="lbl")
    _txt(cv, (O[0] - 12, O[1] + 4), "O", cls="lbl-sm", anchor="end")
    return cv.render()


def build_circle_sector(p: Params) -> str:
    """Cung tròn, hình quạt hoặc hình viên phân ứng với góc ở tâm n°.

    ``mode``: ``cung`` (độ dài cung / góc ở tâm), ``quat`` (hình quạt),
    ``vien-phan`` (viên phân = quạt trừ tam giác OAB).
    """
    mode = str(p.get("mode", "quat"))
    R = _pos(p.get("R", 3), 3.0)
    start = _num(p.get("start", 28), 28)
    sweep = _clamp(_pos(p.get("sweep", 110), 110), 6, 350)
    unit = str(p.get("unit", "do"))
    amark = "α" if unit == "rad" else f"{_fmt(sweep)}°"

    fr = _Frame([(-R, -R), (R, R)], span=250)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale
    A = _on(O, Rp, start)
    B = _on(O, Rp, start + sweep)
    arc = _arc_d(O, Rp, start, start + sweep)
    large = 1 if sweep > 180 else 0

    titles = {"cung": "Cung tròn và góc ở tâm", "quat": "Hình quạt tròn",
              "vien-phan": "Hình viên phân"}
    cv = Canvas(fr.w, fr.h, title=titles.get(mode, "Hình quạt tròn"),
                desc=f"Đường tròn (O; R = {_fmt(R)}) với góc ở tâm AOB = {amark}; "
                     "cung AB nằm trong góc đó được tô đậm.")
    cv.circle(*O, Rp, cls="ink-thin")
    if mode == "quat":
        cv.path(f"M {_n(O[0])} {_n(O[1])} L {_n(A[0])} {_n(A[1])} "
                f"A {_n(Rp)} {_n(Rp)} 0 {large} 0 {_n(B[0])} {_n(B[1])} Z", cls="fill-a")
    elif mode == "vien-phan":
        cv.path(f"M {_n(A[0])} {_n(A[1])} "
                f"A {_n(Rp)} {_n(Rp)} 0 {large} 0 {_n(B[0])} {_n(B[1])} Z", cls="fill-b")
        cv.polyline([O, A, B, O], cls="ink-thin")
        cv.line(*A, *B, cls="accent-c", extra=' stroke-width="2.2"')
    cv.path(arc, cls="accent-a", extra=' style="fill:none" stroke-width="3.4"')
    cv.line(*O, *A, cls="ink")
    cv.line(*O, *B, cls="ink")
    if sweep <= 180:
        _angle_mark(cv, O, A, B, r=Rp * 0.3, label=amark, lgap=13)
    else:
        # Góc lớn hơn 180° thì _angle_mark sẽ vẽ cung bù (nó luôn lấy góc nhỏ),
        # nên ở đây chỉ ghi số đo vào giữa phần quạt.
        _txt(cv, _on(O, Rp * 0.42, start + sweep / 2), amark, cls="lbl-sm")
    cv.dot(*O, r=3, cls="accent-b")
    _txt(cv, _away(A, O, 15), "A", cls="lbl")
    _txt(cv, _away(B, O, 15), "B", cls="lbl")
    _txt(cv, (O[0], O[1] + 17), "O", cls="lbl-sm")
    mid_deg = start + sweep / 2
    if mode == "cung":
        _txt(cv, _on(O, Rp + 20, mid_deg), p.get("arc_label", "ℓ"), cls="lbl-sm")
    elif mode == "quat":
        _txt(cv, _on(O, Rp * 0.58, mid_deg), p.get("arc_label", "S quạt"), cls="lbl-sm")
    else:
        _txt(cv, _on(O, Rp * 0.88, mid_deg), p.get("arc_label", "S viên phân"), cls="lbl-sm")
    _txt(cv, _away(_mid(O, A), B, 12), "R", cls="lbl")
    return cv.render()


def build_annulus(p: Params) -> str:
    """Hình vành khăn giới hạn bởi hai đường tròn đồng tâm bán kính R và r."""
    R = _pos(p.get("R", 3), 3.0)
    r = _pos(p.get("r", 1.9), 1.9)
    if r >= R:
        R, r = max(R, r), min(R, r) * 0.6 or 1.0
    fr = _Frame([(-R, -R), (R, R)], span=240)
    O = fr.pt((0.0, 0.0))
    Rp, rp = R * fr.scale, r * fr.scale
    cv = Canvas(fr.w, fr.h, title="Hình vành khăn",
                desc=f"Phần mặt phẳng giữa hai đường tròn đồng tâm bán kính R = {_fmt(R)} "
                     f"và r = {_fmt(r)}.")
    cv.path(_disc_d(O, Rp) + " " + _disc_d(O, rp), cls="fill-a",
            extra=' fill-rule="evenodd"')
    cv.circle(*O, Rp, cls="ink")
    cv.circle(*O, rp, cls="ink")
    cv.line(*O, *_on(O, Rp, 128), cls="accent-b", extra=' stroke-width="2"')
    cv.line(*O, *_on(O, rp, -38), cls="accent-c", extra=' stroke-width="2"')
    cv.dot(*O, r=3, cls="accent-b")
    _txt(cv, _on(O, Rp * 0.62, 128), "R", cls="lbl", dy=-6)
    _txt(cv, _on(O, rp * 0.62, -38), "r", cls="lbl", dy=14)
    _txt(cv, (O[0] - 11, O[1] + 4), "O", cls="lbl-sm", anchor="end")
    return cv.render()


def build_inscribed_angle(p: Params) -> str:
    """Góc nội tiếp đường tròn.

    ``mode``: ``goc-o-tam`` (nội tiếp = nửa góc ở tâm cùng chắn một cung),
    ``hai-diem`` (hai góc nội tiếp cùng chắn một cung thì bằng nhau),
    ``nua-duong-tron`` (góc nội tiếp chắn nửa đường tròn là góc vuông).
    """
    mode = str(p.get("mode", "goc-o-tam"))
    R = _pos(p.get("R", 3), 3.0)
    fr = _Frame([(-R, -R), (R, R)], span=260)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale

    if mode == "nua-duong-tron":
        adeg = _clamp(_num(p.get("apex_deg", 62), 62), 15, 165)
        Bp, Cp = _on(O, Rp, 180), _on(O, Rp, 0)
        A = _on(O, Rp, adeg)
        cv = Canvas(fr.w, fr.h, title="Góc nội tiếp chắn nửa đường tròn",
                    desc="BC là đường kính nên góc BAC nội tiếp chắn nửa đường tròn "
                         "và bằng 90°.")
        cv.circle(*O, Rp, cls="ink")
        cv.polygon([A, Bp, Cp], cls="fill-a")
        cv.polyline([A, Bp, Cp, A], cls="ink")
        cv.line(*Bp, *Cp, cls="accent-c", extra=' stroke-width="2.4"')
        _ra(cv, A, Bp, Cp, size=13)
        cv.dot(*O, r=3, cls="accent-b")
        _tri_labels(cv, A, Bp, Cp)
        _txt(cv, (O[0], O[1] + 17), "O", cls="lbl-sm")
        return cv.render()

    b_deg = _num(p.get("b_deg", -30), -30)
    c_deg = _num(p.get("c_deg", 210), 210)
    Bp, Cp = _on(O, Rp, b_deg), _on(O, Rp, c_deg)
    # cung BC bị chắn là cung KHÔNG chứa đỉnh; đi từ C sang B theo chiều dương
    arc_from, arc_to = c_deg, c_deg + ((b_deg - c_deg) % 360)

    if mode == "hai-diem":
        a1 = _num(p.get("apex_deg", 70), 70)
        a2 = _num(p.get("apex2_deg", 130), 130)
        A, D = _on(O, Rp, a1), _on(O, Rp, a2)
        cv = Canvas(fr.w, fr.h, title="Hai góc nội tiếp cùng chắn một cung",
                    desc="Góc BAC và góc BDC cùng chắn cung BC nên bằng nhau.")
        cv.circle(*O, Rp, cls="ink")
        cv.path(_arc_d(O, Rp, arc_from, arc_to), cls="accent-a",
                extra=' style="fill:none" stroke-width="3.4"')
        for V in (A, D):
            cv.line(*V, *Bp, cls="ink")
            cv.line(*V, *Cp, cls="ink")
        cv.line(*Bp, *Cp, cls="ink-thin", extra=_dash(1.4))
        _angle_mark(cv, A, Bp, Cp, r=26, label="α")
        _angle_mark(cv, D, Bp, Cp, r=26, label="α", cls="accent-c")
        _txt(cv, _away(A, O, 15), "A", cls="lbl")
        _txt(cv, _away(D, O, 15), "D", cls="lbl")
        _txt(cv, _away(Bp, O, 15), "B", cls="lbl")
        _txt(cv, _away(Cp, O, 15), "C", cls="lbl")
        cv.dot(*O, r=2.8, cls="accent-b")
        return cv.render()

    adeg = _num(p.get("apex_deg", 90), 90)
    A = _on(O, Rp, adeg)
    cv = Canvas(fr.w, fr.h, title="Góc nội tiếp và góc ở tâm",
                desc="Góc nội tiếp BAC bằng nửa số đo cung BC, cũng là nửa góc ở tâm BOC.")
    cv.circle(*O, Rp, cls="ink")
    cv.path(_arc_d(O, Rp, arc_from, arc_to), cls="accent-a",
            extra=' style="fill:none" stroke-width="3.4"')
    cv.line(*A, *Bp, cls="ink")
    cv.line(*A, *Cp, cls="ink")
    cv.line(*O, *Bp, cls="accent-c", extra=' stroke-width="2"')
    cv.line(*O, *Cp, cls="accent-c", extra=' stroke-width="2"')
    cv.line(*Bp, *Cp, cls="ink-thin", extra=_dash(1.4))
    _angle_mark(cv, A, Bp, Cp, r=28, label="α")
    _angle_mark(cv, O, Bp, Cp, r=Rp * 0.32, label="2α", cls="accent-c", lgap=14)
    cv.dot(*O, r=3, cls="accent-b")
    _txt(cv, _away(A, O, 15), "A", cls="lbl")
    _txt(cv, _away(Bp, O, 15), "B", cls="lbl")
    _txt(cv, _away(Cp, O, 15), "C", cls="lbl")
    _txt(cv, (O[0] - 12, O[1] - 6), "O", cls="lbl-sm", anchor="end")
    return cv.render()


def build_arc_locus(p: Params) -> str:
    """Quỹ tích cung chứa góc α dựng trên đoạn AB.

    Vẽ CẢ HAI cung đối xứng qua AB — vẽ một cung là bỏ mất nửa quỹ tích, đúng
    kiểu sai mà người học không có cách nào phát hiện.
    """
    alpha = _clamp(_pos(p.get("alpha", 55), 55), 15, 150)
    AB = _pos(p.get("AB", 4.4), 4.4)
    a = math.radians(alpha)
    R = AB / (2 * math.sin(a))
    # Tâm cung nằm cách AB một khoảng R·cos α — dấu ÂM khi α > 90°, lúc ấy cung
    # chứa góc là cung NHỎ nằm cùng phía với đỉnh M chứ không phải cung lớn.
    h = R * math.cos(a)

    A, B = (-AB / 2, 0.0), (AB / 2, 0.0)
    ymax = h + R                       # đỉnh cung trên; luôn dương vì |h| < R
    xmax = R if h > 0 else AB / 2      # cung lớn mới chạm hai mép trái/phải đường tròn
    fr = _Frame([(-xmax, -ymax), (xmax, ymax)], span=280)
    sA, sB = fr.all([A, B])
    Rp = R * fr.scale

    cv = Canvas(fr.w, fr.h, title="Cung chứa góc",
                desc=f"Quỹ tích các điểm M nhìn đoạn AB dưới góc {_fmt(alpha)}° là hai "
                     "cung tròn đối xứng nhau qua AB.")
    up = fr.pt((0.0, ymax))            # đỉnh cung trên
    down = fr.pt((0.0, -ymax))
    O1, O2 = fr.pt((0.0, h)), fr.pt((0.0, -h))
    for O, apex in ((O1, up), (O2, down)):
        cv.path(_arc_through_d(O, Rp, sA, sB, apex), cls="accent-a",
                extra=' style="fill:none" stroke-width="3"')
    cv.line(*sA, *sB, cls="ink", extra=' stroke-width="2.4"')
    a_from, sweep = _arc_span(O1, sA, sB, up)
    for t in (0.3, 0.62):
        M = _on(O1, Rp, a_from + sweep * t)
        cv.line(*M, *sA, cls="ink-thin")
        cv.line(*M, *sB, cls="ink-thin")
        _angle_mark(cv, M, sA, sB, r=22, label=f"{_fmt(alpha)}°")
        cv.dot(*M, r=3, cls="accent-b")
        _txt(cv, _away(M, _mid(sA, sB), 15), "M", cls="lbl-sm")
    cv.dot(*sA, r=3, cls="accent-b")
    cv.dot(*sB, r=3, cls="accent-b")
    _txt(cv, (sA[0] - 14, sA[1] + 4), "A", cls="lbl", anchor="end")
    _txt(cv, (sB[0] + 14, sB[1] + 4), "B", cls="lbl")
    return cv.render()


def build_cyclic_quad(p: Params) -> str:
    """Tứ giác nội tiếp đường tròn: hai góc đối bù nhau; tuỳ chọn hai đường chéo."""
    R = _pos(p.get("R", 3), 3.0)
    degs = p.get("angles", [110, 195, 285, 20])
    try:
        degs = [_num(v, 0) for v in degs][:4]
    except TypeError:
        degs = [110, 195, 285, 20]
    if len(degs) != 4:
        degs = [110, 195, 285, 20]
    show_diag = bool(p.get("diagonals", False))

    fr = _Frame([(-R, -R), (R, R)], span=250)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale
    A, B, C, D = (_on(O, Rp, t) for t in degs)
    cv = Canvas(fr.w, fr.h, title="Tứ giác nội tiếp",
                desc="Tứ giác ABCD nội tiếp đường tròn: tổng hai góc đối bằng 180°.")
    cv.circle(*O, Rp, cls="ink")
    cv.polygon([A, B, C, D], cls="fill-a")
    cv.polyline([A, B, C, D, A], cls="ink")
    if show_diag:
        cv.line(*A, *C, cls="accent-b", extra=_dash(1.8))
        cv.line(*B, *D, cls="accent-c", extra=_dash(1.8))
    _angle_mark(cv, A, D, B, r=24, label="Â")
    _angle_mark(cv, C, B, D, r=24, label="Ĉ", cls="accent-c")
    cv.dot(*O, r=2.8, cls="accent-b")
    for P, nm in zip((A, B, C, D), ("A", "B", "C", "D")):
        _txt(cv, _away(P, O, 16), nm, cls="lbl")
    return cv.render()


def build_circle_secants(p: Params) -> str:
    """Hai cát tuyến / hai dây qua một điểm M — nền hình cho phương tích và các
    góc có đỉnh trong, ngoài đường tròn.

    ``mode``: ``ngoai`` (M ngoài đường tròn) hoặc ``trong`` (M trong đường tròn).
    """
    mode = str(p.get("mode", "ngoai"))
    R = _pos(p.get("R", 3), 3.0)
    show_tangent = bool(p.get("tangent", False))
    show_angle = bool(p.get("angle", False))

    if mode == "trong":
        M = (_clamp(_num(p.get("mx", 0.5), 0.5), -0.6, 0.6) * R,
             _clamp(_num(p.get("my", -0.25), -0.25), -0.6, 0.6) * R)
        fr = _Frame([(-R, -R), (R, R)], span=270)
        O = fr.pt((0.0, 0.0))
        Rp = R * fr.scale
        sM = fr.pt(M)
        cv = Canvas(fr.w, fr.h, title="Hai dây cắt nhau trong đường tròn",
                    desc="Hai dây AB và CD cắt nhau tại M nằm trong đường tròn: "
                         "MA·MB = MC·MD.")
        cv.circle(*O, Rp, cls="ink")
        pairs = []
        for deg, cls in ((22, "accent-a"), (104, "accent-c")):
            u = (math.cos(math.radians(deg)), -math.sin(math.radians(deg)))
            hits = _line_circle(sM, u, O, Rp)
            if len(hits) == 2:
                cv.line(*hits[0], *hits[1], cls=cls, extra=' stroke-width="2.4"')
                pairs.append(hits)
        cv.dot(*sM, r=3.4, cls="accent-b")
        cv.dot(*O, r=2.6, cls="accent-b")
        names = ("A", "B", "C", "D")
        flat = [q for pair in pairs for q in pair]
        for P, nm in zip(flat, names):
            _txt(cv, _away(P, O, 15), nm, cls="lbl")
        _txt(cv, (sM[0] - 6, sM[1] + 17), "M", cls="lbl")
        if show_angle and len(flat) == 4:
            _angle_mark(cv, sM, flat[1], flat[3], r=24)
        return cv.render()

    dM = max(_pos(p.get("dM", 2.1), 2.1), 1.3) * R
    fr = _Frame([(-R, -R), (R, R), (-dM, 0.0)], span=310)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale
    sM = fr.pt((-dM, 0.0))
    cv = Canvas(fr.w, fr.h, title="Hai cát tuyến từ điểm ngoài đường tròn",
                desc="Từ M ngoài đường tròn kẻ hai cát tuyến MAB và MCD: "
                     "MA·MB = MC·MD = MT².")
    cv.circle(*O, Rp, cls="ink")
    flat: list[Pt] = []
    for deg, cls in ((15, "accent-a"), (-16, "accent-c")):
        u = (math.cos(math.radians(deg)), -math.sin(math.radians(deg)))
        hits = _line_circle(sM, u, O, Rp)
        if len(hits) == 2:
            cv.line(*sM, *hits[1], cls=cls, extra=' stroke-width="2.4"')
            flat.extend(hits)
    if show_tangent:
        # Tiếp tuyến từ M: độ dài MT = √(MO² − R²), và tia MT lệch khỏi tia MO một
        # góc β với sin β = R/MO. Dựng theo hai đại lượng này thay vì giải hệ để
        # tiếp điểm luôn nằm đúng trên đường tròn kể cả khi M rất gần đường tròn.
        MO = _dist(sM, O)
        beta = math.degrees(math.asin(_clamp(Rp / MO, -1.0, 1.0)))
        tlen = math.sqrt(max(MO * MO - Rp * Rp, 0.0))
        dirT = math.radians(_ang_deg(sM, O) + beta)
        T = (sM[0] + tlen * math.cos(dirT), sM[1] - tlen * math.sin(dirT))
        cv.line(*sM, *T, cls="accent-d", extra=' stroke-width="2.2"')
        cv.line(*O, *T, cls="ink-thin")
        _ra(cv, T, O, sM, size=10)
        cv.dot(*T, r=3, cls="accent-d")
        _txt(cv, _away(T, O, 15), "T", cls="lbl")
    cv.dot(*sM, r=3.4, cls="accent-b")
    cv.dot(*O, r=2.6, cls="accent-b")
    for P, nm in zip(flat, ("A", "B", "C", "D")):
        _txt(cv, _away(P, O, 15), nm, cls="lbl")
    _txt(cv, (sM[0] - 14, sM[1] + 4), "M", cls="lbl", anchor="end")
    _txt(cv, (O[0], O[1] + 17), "O", cls="lbl-sm")
    if show_angle and len(flat) == 4:
        _angle_mark(cv, sM, flat[1], flat[3], r=30)
    return cv.render()


def build_circle_positions(p: Params) -> str:
    """Vị trí tương đối với đường tròn.

    ``mode``: ``diem`` (điểm), ``duong-thang`` (đường thẳng), ``hai-duong-tron``
    (đủ năm trường hợp — thiếu một trường hợp là hình nói dối bằng cách im lặng).
    """
    mode = str(p.get("mode", "diem"))

    if mode == "duong-thang":
        R = _pos(p.get("R", 3), 3.0)
        fr = _Frame([(-1.45 * R, -1.15 * R), (1.45 * R, 1.45 * R)], span=280, pad=60)
        O = fr.pt((0.0, 0.0))
        Rp = R * fr.scale
        cv = Canvas(fr.w, fr.h, title="Vị trí tương đối của đường thẳng và đường tròn",
                    desc="Ba trường hợp: d < R đường thẳng cắt đường tròn, d = R tiếp xúc, "
                         "d > R không có điểm chung.")
        cv.circle(*O, Rp, cls="ink")
        cv.dot(*O, r=3, cls="accent-b")
        x1, x2 = O[0] - Rp * 1.35, O[0] + Rp * 1.35
        cases = ((-0.5, "accent-a", "d < R"), (1.0, "accent-c", "d = R"),
                 (1.32, "accent-d", "d > R"))
        for frac, cls, lab in cases:
            y = O[1] - Rp * frac
            cv.line(x1, y, x2, y, cls=cls, extra=' stroke-width="2.4"')
            cv.line(*O, O[0], y, cls="ink-thin", extra=_dash(1.2, "3 3"))
            _txt(cv, (x2 + 8, y), lab, cls="lbl-sm", anchor="start")
        _txt(cv, (O[0] - 12, O[1] + 4), "O", cls="lbl-sm", anchor="end")
        return cv.render()

    if mode == "hai-duong-tron":
        # Năm ô nhỏ, mỗi ô một trường hợp; bố cục 3 + 2 để khung không quá dài.
        cw, ch = 208.0, 152.0
        cv = Canvas(3 * cw, 2 * ch, title="Vị trí tương đối của hai đường tròn",
                    desc="Năm trường hợp theo khoảng cách d giữa hai tâm: ngoài nhau, "
                         "tiếp xúc ngoài, cắt nhau, tiếp xúc trong, đựng nhau.")
        R1, R2 = 42.0, 26.0
        cases = (
            (R1 + R2 + 16, R2, "ở ngoài nhau", "d > R + r"),
            (R1 + R2, R2, "tiếp xúc ngoài", "d = R + r"),
            (R1 + 6, R2, "cắt nhau", "|R − r| < d < R + r"),
            (R1 - R2, R2, "tiếp xúc trong", "d = |R − r|"),
            (R1 - R2 - 12, R2, "đựng nhau", "d < |R − r|"),
        )
        for i, (d, r2, name, cond) in enumerate(cases):
            col, row = i % 3, i // 3
            cx = col * cw + cw / 2 - d / 2
            cy = row * ch + ch / 2 - 6
            cv.circle(cx, cy, R1, cls="ink")
            cv.circle(cx + d, cy, r2, cls="accent-a", extra=' style="fill:none" stroke-width="2"')
            cv.dot(cx, cy, r=2.2, cls="accent-b")
            cv.dot(cx + d, cy, r=2.2, cls="accent-b")
            cv.line(cx, cy, cx + d, cy, cls="ink-thin", extra=_dash(1.1, "3 3"))
            _txt(cv, (col * cw + cw / 2, row * ch + ch - 34), name, cls="lbl-sm")
            _txt(cv, (col * cw + cw / 2, row * ch + ch - 18), cond, cls="lbl-sm")
        return cv.render()

    R = _pos(p.get("R", 3), 3.0)
    fr = _Frame([(-1.45 * R, -1.45 * R), (1.45 * R, 1.45 * R)], span=270)
    O = fr.pt((0.0, 0.0))
    Rp = R * fr.scale
    cv = Canvas(fr.w, fr.h, title="Vị trí tương đối của điểm và đường tròn",
                desc="Điểm M nằm trong, nằm trên hay nằm ngoài đường tròn tuỳ theo "
                     "OM nhỏ hơn, bằng hay lớn hơn R.")
    cv.circle(*O, Rp, cls="fill-a")
    cv.circle(*O, Rp, cls="ink")
    cv.dot(*O, r=3, cls="accent-b")
    spots = ((0.5, 150, "M₁", "OM < R"), (1.0, 30, "M₂", "OM = R"),
             (1.32, -74, "M₃", "OM > R"))
    for frac, deg, nm, cond in spots:
        M = _on(O, Rp * frac, deg)
        cv.line(*O, *M, cls="ink-thin", extra=_dash(1.2, "3 3"))
        cv.dot(*M, r=3.4, cls="accent-b")
        # tên điểm bám sát điểm, điều kiện đẩy xa thêm một dòng chữ để hai nhãn
        # không dính nhau khi bán kính gần nằm ngang
        _txt(cv, _away(M, O, 14), nm, cls="lbl")
        _txt(cv, _away(M, O, 40), cond, cls="lbl-sm")
    _txt(cv, (O[0] - 12, O[1] + 4), "O", cls="lbl-sm", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# Tam giác: đường đồng quy, đường đặc biệt, đường tròn nội/ngoại tiếp
# --------------------------------------------------------------------------
def build_triangle_centers(p: Params) -> str:
    """Ba đường đồng quy trong tam giác.

    ``mode``: ``trong-tam`` (ba trung tuyến), ``truc-tam`` (ba đường cao),
    ``phan-giac`` (ba phân giác + đường tròn nội tiếp),
    ``trung-truc`` (ba trung trực + đường tròn ngoại tiếp).
    """
    mode = str(p.get("mode", "trong-tam"))
    A, B, C = _triangle(p)

    extra_pts: list[Pt] = []
    O = _circumcenter(A, B, C)
    if mode == "trung-truc" and O is not None:
        Rw = _dist(O, A)
        extra_pts = [(O[0] - Rw, O[1] - Rw), (O[0] + Rw, O[1] + Rw)]

    fr = _Frame([A, B, C] + extra_pts, span=300)
    sA, sB, sC = fr.all([A, B, C])
    cv = Canvas(fr.w, fr.h, title="Ba đường đồng quy trong tam giác", desc="")
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")

    if mode == "truc-tam":
        cv.desc = ("Ba đường cao của tam giác ABC đồng quy tại trực tâm H.")
        H = None
        for V, P, Q in ((A, B, C), (B, C, A), (C, A, B)):
            F = _foot(V, P, Q)
            sV, sF = fr.pt(V), fr.pt(F)
            cv.line(*sV, *sF, cls="accent-b", extra=_dash(1.7))
            _ra(cv, sF, sV, fr.pt(Q), size=9)
        if O is not None:
            H = (A[0] + B[0] + C[0] - 2 * O[0], A[1] + B[1] + C[1] - 2 * O[1])
            sH = fr.pt(H)
            cv.dot(*sH, r=4, cls="accent-d")
            _txt(cv, (sH[0] + 13, sH[1] + 4), "H", cls="lbl")
    elif mode == "phan-giac":
        cv.desc = ("Ba đường phân giác trong đồng quy tại tâm I của đường tròn nội tiếp; "
                   "I cách đều ba cạnh.")
        I, r = _incenter(A, B, C)
        sI = fr.pt(I)
        cv.circle(*sI, r * fr.scale, cls="ink-thin")
        for V, P, Q in ((A, B, C), (B, C, A), (C, A, B)):
            D = _lerp(P, Q, _dist(V, P) / max(_dist(V, P) + _dist(V, Q), 1e-9))
            cv.line(*fr.pt(V), *fr.pt(D), cls="accent-b", extra=_dash(1.7))
            _angle_mark(cv, fr.pt(V), fr.pt(P), fr.pt(D), r=20, label=None)
            _angle_mark(cv, fr.pt(V), fr.pt(D), fr.pt(Q), r=26, label=None)
        F = _foot(I, B, C)
        cv.line(*sI, *fr.pt(F), cls="accent-c", extra=' stroke-width="2"')
        _ra(cv, fr.pt(F), sI, sC, size=9)
        _txt(cv, _mid(sI, fr.pt(F)), "r", cls="lbl", anchor="end")
        cv.dot(*sI, r=4, cls="accent-d")
        _txt(cv, (sI[0] + 13, sI[1] + 4), "I", cls="lbl")
    elif mode == "trung-truc" and O is not None:
        cv.desc = ("Ba đường trung trực đồng quy tại tâm O của đường tròn ngoại tiếp; "
                   "OA = OB = OC = R.")
        sO = fr.pt(O)
        Rp = _dist(O, A) * fr.scale
        cv.circle(*sO, Rp, cls="ink-thin")
        for P, Q in ((A, B), (B, C), (C, A)):
            sM = fr.pt(_mid(P, Q))
            # Vẽ hẳn ĐƯỜNG trung trực (đoạn đối xứng qua trung điểm) chứ không chỉ
            # nối O với trung điểm: nối như thế trông giống bán kính, mất ý "đường
            # vuông góc với cạnh tại trung điểm".
            ux, uy = sO[0] - sM[0], sO[1] - sM[1]
            L = math.hypot(ux, uy)
            if L < 1e-6:                       # O trùng trung điểm (tam giác vuông)
                sQ = fr.pt(Q)
                ux, uy = -(sQ[1] - sM[1]), sQ[0] - sM[0]
                L = math.hypot(ux, uy) or 1.0
            ux, uy = ux / L, uy / L
            ext = max(L, Rp * 0.35)
            cv.line(sM[0] - ux * ext * 0.3, sM[1] - uy * ext * 0.3,
                    sM[0] + ux * ext * 1.35, sM[1] + uy * ext * 1.35,
                    cls="accent-b", extra=_dash(1.7))
            _ra(cv, sM, sO if L > 1e-6 else fr.pt(Q), fr.pt(Q), size=9)
            _ticks(cv, fr.pt(P), sM, 1)
            _ticks(cv, sM, fr.pt(Q), 1)
        for V in (sA, sB, sC):
            cv.line(*sO, *V, cls="accent-c", extra=_dash(1.3, "3 3"))
        _txt(cv, _away(_mid(sO, sA), sB, 12), "R", cls="lbl-sm")
        cv.dot(*sO, r=4, cls="accent-d")
        _txt(cv, (sO[0] + 13, sO[1] + 4), "O", cls="lbl")
    else:
        cv.desc = ("Ba đường trung tuyến đồng quy tại trọng tâm G với AG = 2/3 AM.")
        G = _centroid([A, B, C])
        for V, P, Q in ((A, B, C), (B, C, A), (C, A, B)):
            M = _mid(P, Q)
            cv.line(*fr.pt(V), *fr.pt(M), cls="accent-b", extra=_dash(1.7))
            _ticks(cv, fr.pt(P), fr.pt(M), 1)
            _ticks(cv, fr.pt(M), fr.pt(Q), 1)
        sG = fr.pt(G)
        sM = fr.pt(_mid(B, C))
        cv.dot(*sG, r=4, cls="accent-d")
        _txt(cv, (sG[0] + 13, sG[1] + 4), "G", cls="lbl")
        _txt(cv, (sM[0], sM[1] + 19), "M", cls="lbl-sm")
    _tri_labels(cv, sA, sB, sC)
    return cv.render()


def build_triangle_cevian(p: Params) -> str:
    """Một đường đặc biệt kẻ từ đỉnh A.

    ``mode``: ``duong-cao`` (đường cao h_a), ``trung-tuyen`` (trung tuyến m_a),
    ``phan-giac`` (phân giác trong, kèm hệ thức DB/DC = AB/AC).
    """
    mode = str(p.get("mode", "duong-cao"))
    A, B, C = _triangle(p)
    fr = _Frame([A, B, C], span=300)
    sA, sB, sC = fr.all([A, B, C])
    a, b, c = _dist(B, C), _dist(C, A), _dist(A, B)

    cv = Canvas(fr.w, fr.h, title="Đường đặc biệt trong tam giác", desc="")
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")

    if mode == "trung-tuyen":
        cv.desc = "Trung tuyến AM của tam giác ABC (M là trung điểm cạnh BC)."
        M = _mid(B, C)
        sM = fr.pt(M)
        cv.line(*sA, *sM, cls="accent-b", extra=' stroke-width="2.2"')
        _ticks(cv, sB, sM, 1)
        _ticks(cv, sM, sC, 1)
        _sub(cv, _perp_off(sA, sM, sC, 15), "m", "a")
        _txt(cv, (sM[0], sM[1] + 19), "M", cls="lbl-sm")
    elif mode == "phan-giac":
        cv.desc = ("Phân giác trong AD của góc A chia cạnh BC theo tỉ số "
                   "DB : DC = AB : AC.")
        D = _lerp(B, C, c / max(b + c, 1e-9))
        sD = fr.pt(D)
        cv.line(*sA, *sD, cls="accent-b", extra=' stroke-width="2.2"')
        _angle_mark(cv, sA, sB, sD, r=22, label=None)
        _angle_mark(cv, sA, sD, sC, r=28, label=None)
        _sub(cv, _perp_off(sA, sD, sC, 15), "l", "a")
        _txt(cv, (sD[0], sD[1] + 19), "D", cls="lbl-sm")
        _txt(cv, (_mid(sB, sD)[0], sB[1] + 21), "DB", cls="lbl-sm")
        _txt(cv, (_mid(sD, sC)[0], sC[1] + 21), "DC", cls="lbl-sm")
    else:
        cv.desc = "Đường cao AH hạ từ A xuống cạnh BC; S = ½·a·h_a."
        H = _foot(A, B, C)
        sH = fr.pt(H)
        cv.line(*sA, *sH, cls="accent-b", extra=_dash(1.8))
        _ra(cv, sH, sA, sC, size=11)
        _sub(cv, (sH[0] + 14, _mid(sA, sH)[1]), "h", "a")
        _txt(cv, (sH[0], sH[1] + 19), "H", cls="lbl-sm")
        _txt(cv, (_mid(sB, sC)[0], max(sB[1], sC[1]) + 21), f"a = {_fmt(a)}", cls="lbl-sm")
    _tri_labels(cv, sA, sB, sC)
    return cv.render()


def build_equilateral_triangle(p: Params) -> str:
    """Tam giác đều cạnh a: đường cao h = a√3/2, tuỳ chọn R và r."""
    a = _pos(p.get("a", 4), 4.0)
    show_h = bool(p.get("height", True))
    show_R = bool(p.get("circumcircle", False))
    show_r = bool(p.get("incircle", False))
    mark_angles = bool(p.get("angles", False))

    h = a * math.sqrt(3) / 2
    B, C = (0.0, 0.0), (a, 0.0)
    A = (a / 2, h)
    O = (a / 2, h / 3)                     # tâm ngoại tiếp trùng tâm nội tiếp
    Rw, rw = a / math.sqrt(3), a / (2 * math.sqrt(3))
    bounds = [B, C, A]
    if show_R:
        bounds += [(O[0] - Rw, O[1] - Rw), (O[0] + Rw, O[1] + Rw)]
    fr = _Frame(bounds, span=280)
    sA, sB, sC, sO = fr.all([A, B, C, O])

    cv = Canvas(fr.w, fr.h, title="Tam giác đều",
                desc=f"Tam giác đều cạnh a = {_fmt(a)}: ba cạnh bằng nhau, ba góc 60°, "
                     "đường cao h = a√3/2.")
    if show_R:
        cv.circle(*sO, Rw * fr.scale, cls="ink-thin")
    if show_r:
        cv.circle(*sO, rw * fr.scale, cls="ink-thin", extra=_dash(1.2, "4 3"))
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")
    for P, Q in ((sA, sB), (sB, sC), (sC, sA)):
        _ticks(cv, P, Q, 2)
    if show_h:
        sH = fr.pt((a / 2, 0.0))
        cv.line(*sA, *sH, cls="accent-b", extra=_dash(1.7))
        _ra(cv, sH, sA, sC, size=10)
        # đường cao trùng trục đối xứng, nên nhãn h phải nhường phía có R/r
        side = -15 if (show_R or show_r) else 14
        _txt(cv, (sH[0] + side, _mid(sA, sH)[1]), "h", cls="lbl",
             anchor="end" if side < 0 else "start")
    if show_R or show_r:
        cv.dot(*sO, r=3, cls="accent-d")
        if show_R:
            cv.line(*sO, *sB, cls="accent-c", extra=' stroke-width="1.8"')
            _txt(cv, _away(_mid(sO, sB), sA, 12), "R", cls="lbl")
        if show_r:
            sF = fr.pt(_foot(O, A, C))
            cv.line(*sO, *sF, cls="accent-d", extra=' stroke-width="1.8"')
            _txt(cv, _away(_mid(sO, sF), sB, 12), "r", cls="lbl")
    if mark_angles:
        for V, P, Q in ((sA, sB, sC), (sB, sC, sA), (sC, sA, sB)):
            _angle_mark(cv, V, P, Q, r=21, label="60°", lgap=13)
    _txt(cv, (_mid(sB, sC)[0], sB[1] + 21), f"a = {_fmt(a)}", cls="lbl")
    _tri_labels(cv, sA, sB, sC)
    return cv.render()


def build_triangle_circumcircle(p: Params) -> str:
    """Tam giác nội tiếp đường tròn (O; R) — nền hình cho định lí sin."""
    A, B, C = _triangle(p)
    O = _circumcenter(A, B, C)
    if O is None:
        A, B, C = _triangle({})
        O = _circumcenter(A, B, C)
    Rw = _dist(O, A)
    show_angles = bool(p.get("angles", True))
    show_diameter = bool(p.get("diameter", False))

    fr = _Frame([(O[0] - Rw, O[1] - Rw), (O[0] + Rw, O[1] + Rw)], span=290)
    sA, sB, sC, sO = fr.all([A, B, C, O])
    cv = Canvas(fr.w, fr.h, title="Đường tròn ngoại tiếp tam giác",
                desc="Tam giác ABC nội tiếp đường tròn (O; R): a/sin A = b/sin B = "
                     "c/sin C = 2R.")
    cv.circle(*sO, Rw * fr.scale, cls="ink")
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")
    cv.line(*sO, *sA, cls="accent-b", extra=_dash(1.6))
    _txt(cv, _away(_mid(sO, sA), sC, 13), "R", cls="lbl")
    if show_diameter:
        Bop = (2 * O[0] - B[0], 2 * O[1] - B[1])
        sBop = fr.pt(Bop)
        cv.line(*sB, *sBop, cls="accent-c", extra=_dash(1.6))
        _txt(cv, _perp_off(_lerp(sB, sBop, 0.72), sBop, sA, 13), "2R", cls="lbl-sm")
    if show_angles:
        # chỉ vẽ cung góc, KHÔNG ghi chữ trong cung: tên đỉnh đã nằm ngoài hình,
        # ghi thêm lần nữa ở trong sẽ thành hai chữ A trên cùng một tam giác
        _angle_mark(cv, sA, sB, sC, r=23)
        _angle_mark(cv, sB, sC, sA, r=23)
        _angle_mark(cv, sC, sA, sB, r=23)
    _tri_labels(cv, sA, sB, sC)
    G = _centroid([sA, sB, sC])
    _txt(cv, _away(_mid(sB, sC), G, 15), "a", cls="lbl")
    _txt(cv, _away(_mid(sC, sA), G, 15), "b", cls="lbl")
    _txt(cv, _away(_mid(sA, sB), G, 15), "c", cls="lbl")
    cv.dot(*sO, r=3.4, cls="accent-d")
    _txt(cv, (sO[0] + 12, sO[1] + 14), "O", cls="lbl-sm")
    return cv.render()


def build_triangle_incircle(p: Params) -> str:
    """Đường tròn nội tiếp (mặc định) hoặc bàng tiếp trong góc A của tam giác."""
    mode = str(p.get("mode", "noi-tiep"))
    A, B, C = _triangle(p)

    if mode == "bang-tiep":
        # Tam giác mặc định riêng cho nhánh này: r_a = S/(p − a) phình rất nhanh khi
        # a lớn, lấy tam giác có cạnh a ngắn thì đường tròn bàng tiếp mới cùng cỡ
        # với tam giác thay vì nuốt trọn khung hình.
        A, B, C = _triangle(p, default=((1.0, 4.0), (0.0, 0.0), (2.0, 0.0)))
        J, ra = _excenter(A, B, C)
        # Hai tia kéo dài phải nằm TRONG bao lồi dùng dựng khung: quên chúng thì
        # nét đứt lấn vào lề và bị cắt ở những tam giác dẹt.
        fars = [_lerp(A, P, 1 + 1.5 * _dist(P, J) / max(_dist(A, P), 1e-9)) for P in (B, C)]
        fr = _Frame([A, B, C, (J[0] - ra, J[1] - ra), (J[0] + ra, J[1] + ra)] + fars, span=300)
        sA, sB, sC, sJ = fr.all([A, B, C, J])
        cv = Canvas(fr.w, fr.h, title="Đường tròn bàng tiếp",
                    desc="Đường tròn bàng tiếp trong góc A tiếp xúc cạnh BC và phần kéo "
                         "dài của hai cạnh AB, AC; bán kính r_a = S/(p − a).")
        # chỉ vẽ PHẦN KÉO DÀI (từ B, C trở đi) — vẽ cả cạnh sẽ đè nét đứt lên nét liền
        for P, far in zip((B, C), fars):
            cv.line(*fr.pt(P), *fr.pt(far), cls="ink-thin", extra=_dash(1.4, "6 4"))
        cv.circle(*sJ, ra * fr.scale, cls="ink-thin")
        cv.polygon([sA, sB, sC], cls="fill-a")
        cv.polyline([sA, sB, sC, sA], cls="ink")
        F = _foot(J, B, C)
        cv.line(*sJ, *fr.pt(F), cls="accent-b", extra=' stroke-width="2"')
        _ra(cv, fr.pt(F), sJ, sC, size=10)
        _sub(cv, _perp_off(sJ, fr.pt(F), sB, 13), "r", "a")
        # ba tiếp điểm: không chấm ra thì người đọc chỉ thấy "một đường tròn ở gần",
        # không thấy nó TIẾP XÚC với cạnh BC và hai tia kéo dài
        for P, Q in ((B, C), (A, B), (A, C)):
            cv.dot(*fr.pt(_foot(J, P, Q)), r=2.8, cls="accent-d")
        cv.dot(*sJ, r=3.6, cls="accent-d")
        _sub(cv, (sJ[0] + 15, sJ[1] + 4), "I", "a")
        _tri_labels(cv, sA, sB, sC)
        return cv.render()

    I, r = _incenter(A, B, C)
    fr = _Frame([A, B, C], span=300)
    sA, sB, sC, sI = fr.all([A, B, C, I])
    cv = Canvas(fr.w, fr.h, title="Đường tròn nội tiếp tam giác",
                desc="Đường tròn nội tiếp (I; r) tiếp xúc cả ba cạnh; S = p·r.")
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")
    cv.circle(*sI, r * fr.scale, cls="ink")
    for P, Q in ((B, C), (C, A), (A, B)):
        F = fr.pt(_foot(I, P, Q))
        cv.line(*sI, *F, cls="accent-b", extra=_dash(1.5))
        _ra(cv, F, sI, fr.pt(Q), size=9)
    _txt(cv, _perp_off(sI, fr.pt(_foot(I, B, C)), sC, 13), "r", cls="lbl")
    cv.dot(*sI, r=3.6, cls="accent-d")
    _txt(cv, (sI[0] + 13, sI[1] - 8), "I", cls="lbl")
    G = _centroid([sA, sB, sC])
    _txt(cv, _away(_mid(sB, sC), G, 16), "a", cls="lbl")
    _txt(cv, _away(_mid(sC, sA), G, 16), "b", cls="lbl")
    _txt(cv, _away(_mid(sA, sB), G, 16), "c", cls="lbl")
    _tri_labels(cv, sA, sB, sC)
    return cv.render()


def build_triangle_labeled(p: Params) -> str:
    """Tam giác có nhãn ba cạnh a, b, c; tuỳ chọn đánh dấu góc và cạnh bằng nhau.

    ``mark_angles``: danh sách đỉnh cần đánh dấu góc (vd ``["A"]`` cho định lí
    cosin, ``["C"]`` cho S = ½ab·sin C, ``["A","B","C"]`` cho tổng ba góc).
    ``ticks``: dict cạnh → số gạch, để chỉ các cạnh bằng nhau (tam giác cân).
    """
    A, B, C = _triangle(p)
    marks = p.get("mark_angles", [])
    if isinstance(marks, str):
        marks = [marks]
    marks = [str(m) for m in marks] if isinstance(marks, (list, tuple)) else []
    ticks = p.get("ticks", {})
    ticks = ticks if isinstance(ticks, dict) else {}
    show_sides = bool(p.get("side_labels", True))

    fr = _Frame([A, B, C], span=300)
    sA, sB, sC = fr.all([A, B, C])
    G = _centroid([sA, sB, sC])
    cv = Canvas(fr.w, fr.h, title="Tam giác ABC",
                desc="Tam giác ABC với cạnh a = BC, b = CA, c = AB đối diện các đỉnh "
                     "A, B, C.")
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")
    sides = {"a": (sB, sC), "b": (sC, sA), "c": (sA, sB)}
    if show_sides:
        for nm, (P, Q) in sides.items():
            _txt(cv, _away(_mid(P, Q), G, 16), nm, cls="lbl")
    for nm, count in ticks.items():
        if nm in sides:
            _ticks(cv, *sides[nm], int(_clamp(_num(count, 1), 1, 3)))
    corners = {"A": (sA, sB, sC), "B": (sB, sC, sA), "C": (sC, sA, sB)}
    for nm in marks:
        if nm in corners:
            V, P, Q = corners[nm]
            _angle_mark(cv, V, P, Q, r=24, label=nm)
    _tri_labels(cv, sA, sB, sC)
    return cv.render()


def build_right_triangle_altitude(p: Params) -> str:
    """Hệ thức lượng trong tam giác vuông: đường cao ứng với cạnh huyền.

    Tam giác ABC vuông tại A, cạnh huyền BC nằm ngang, AH ⊥ BC. Hai hình chiếu
    c' = BH và b' = CH luôn nằm TRONG cạnh huyền — đó là lý do đặt cạnh huyền
    làm đáy chứ không đặt hai cạnh góc vuông theo trục như hình Pytago.

    ``mode``: ``he-thuc`` (mặc định) hoặc ``trung-tuyen`` (AM = ½BC).
    """
    b = _pos(p.get("b", 4), 4.0)      # AC
    c = _pos(p.get("c", 3), 3.0)      # AB
    mode = str(p.get("mode", "he-thuc"))
    a = math.hypot(b, c)
    Hx, Ay = c * c / a, b * c / a

    B, C = (0.0, 0.0), (a, 0.0)
    A = (Hx, Ay)
    H = (Hx, 0.0)
    # nhánh trung tuyến vẽ thêm nửa đường tròn đường kính BC; đỉnh của nó ở độ cao
    # a/2 nên phải đưa vào bao lồi, nếu không nét cung bị lề cắt mất
    extra = [(a / 2, a / 2)] if mode == "trung-tuyen" else []
    fr = _Frame([B, C, A] + extra, span=310)
    sA, sB, sC, sH = fr.all([A, B, C, H])

    cv = Canvas(fr.w, fr.h, title="Hệ thức lượng trong tam giác vuông",
                desc="Tam giác ABC vuông tại A, đường cao AH ứng với cạnh huyền BC; "
                     "c′ = BH và b′ = CH là hình chiếu của hai cạnh góc vuông.")
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")
    _ra(cv, sA, sB, sC, size=13)

    if mode == "trung-tuyen":
        cv.desc = ("Trong tam giác vuông tại A, trung tuyến AM ứng với cạnh huyền "
                   "bằng nửa cạnh huyền: AM = MB = MC.")
        M = _mid(B, C)
        sM = fr.pt(M)
        # chỉ nửa đường tròn PHÍA TRÊN BC: A nằm trên nửa ấy, vẽ trọn đường tròn thì
        # nửa dưới không mang thông tin gì mà lại chiếm mất khung
        cv.path(_arc_d(sM, a / 2 * fr.scale, 0, 180), cls="ink-thin",
                extra=' style="fill:none"' + _dash(1.2, "4 3"))
        cv.line(*sA, *sM, cls="accent-b", extra=' stroke-width="2.2"')
        for P, Q in ((sA, sM), (sB, sM), (sM, sC)):
            _ticks(cv, P, Q, 1)
        _txt(cv, (sM[0], sM[1] + 19), "M", cls="lbl-sm")
        _sub(cv, _perp_off(sA, sM, sC, 15), "m", "a")
    else:
        cv.line(*sA, *sH, cls="accent-b", extra=' stroke-width="2.2"')
        _ra(cv, sH, sA, sC, size=10)
        _txt(cv, (sH[0] + 13, _mid(sA, sH)[1]), "h", cls="lbl")
        _txt(cv, (sH[0], sH[1] + 18), "H", cls="lbl-sm")
        _txt(cv, (_mid(sB, sH)[0], sB[1] + 22), "c′", cls="lbl")
        _txt(cv, (_mid(sH, sC)[0], sC[1] + 22), "b′", cls="lbl")
        _txt(cv, (_mid(sB, sC)[0], sB[1] + 40), f"a = {_fmt(a)}", cls="lbl-sm")
    _txt(cv, _away(_mid(sA, sB), _centroid([sA, sB, sC]), 15), f"c = {_fmt(c)}", cls="lbl")
    _txt(cv, _away(_mid(sA, sC), _centroid([sA, sB, sC]), 15), f"b = {_fmt(b)}", cls="lbl")
    _tri_labels(cv, sA, sB, sC)
    return cv.render()


def build_thales(p: Params) -> str:
    """Định lí Ta-lét trong tam giác: MN ∥ BC cắt hai cạnh AB, AC.

    ``k`` là tỉ số AM/AB; ``k = 0.5`` chính là đường trung bình, khi đó thêm gạch
    đánh dấu trung điểm để phân biệt với trường hợp tổng quát.
    """
    k = _clamp(_pos(p.get("k", 0.55), 0.55), 0.15, 0.85)
    midline = bool(p.get("midline", False))
    if midline:
        k = 0.5
    A, B, C = _triangle(p, default=((2.2, 4.4), (0.0, 0.0), (5.6, 0.0)))
    M, N = _lerp(A, B, k), _lerp(A, C, k)

    fr = _Frame([A, B, C], span=290)
    sA, sB, sC, sM, sN = fr.all([A, B, C, M, N])
    cv = Canvas(fr.w, fr.h, title="Định lí Ta-lét trong tam giác",
                desc="MN song song với BC nên AM/AB = AN/AC = MN/BC.")
    cv.polygon([sA, sB, sC], cls="fill-a")
    cv.polyline([sA, sB, sC, sA], cls="ink")
    cv.line(*sM, *sN, cls="accent-b", extra=' stroke-width="2.4"')
    cv.dot(*sM, r=3, cls="accent-b")
    cv.dot(*sN, r=3, cls="accent-b")
    if midline:
        for P, Q in ((sA, sM), (sM, sB), (sA, sN), (sN, sC)):
            _ticks(cv, P, Q, 1)
    # hai gạch chéo cùng kiểu trên MN và BC là ký hiệu quy ước cho "song song"
    for P, Q in ((sM, sN), (sB, sC)):
        mid = _mid(P, Q)
        L = _dist(P, Q) or 1.0
        ux, uy = (Q[0] - P[0]) / L, (Q[1] - P[1]) / L
        for off in (-3.5, 3.5):
            cx, cy = mid[0] + ux * off, mid[1] + uy * off
            cv.line(cx - ux * 4 - uy * 5, cy - uy * 4 + ux * 5,
                    cx + ux * 4 + uy * 5, cy + uy * 4 - ux * 5, cls="ink-thin")
    _txt(cv, (sM[0] - 14, sM[1]), "M", cls="lbl", anchor="end")
    _txt(cv, (sN[0] + 14, sN[1]), "N", cls="lbl")
    _tri_labels(cv, sA, sB, sC)
    return cv.render()


def build_trapezoid_midline(p: Params) -> str:
    """Đường trung bình của hình thang: MN ∥ AB ∥ CD và MN = (AB + CD)/2."""
    ab = _pos(p.get("ab", 3.2), 3.2)    # đáy nhỏ
    cd = _pos(p.get("cd", 6.0), 6.0)    # đáy lớn
    h = _pos(p.get("h", 3.0), 3.0)
    if ab > cd:
        ab, cd = cd, ab
    off = float(p.get("offset", 0.9))

    D, C = (0.0, 0.0), (cd, 0.0)
    A, B = (off, h), (off + ab, h)
    M, N = _mid(A, D), _mid(B, C)
    fr = _Frame([A, B, C, D], span=300)
    sA, sB, sC, sD, sM, sN = fr.all([A, B, C, D, M, N])

    cv = Canvas(fr.w, fr.h, title="Đường trung bình của hình thang",
                desc="M, N là trung điểm hai cạnh bên; MN song song hai đáy và bằng "
                     "nửa tổng hai đáy.")
    cv.polygon([sA, sB, sC, sD], cls="fill-a")
    cv.polyline([sA, sB, sC, sD, sA], cls="ink")
    cv.line(*sM, *sN, cls="accent-b", extra=' stroke-width="2.4"')
    cv.dot(*sM, r=3, cls="accent-b")
    cv.dot(*sN, r=3, cls="accent-b")
    for P, Q in ((sA, sM), (sM, sD), (sB, sN), (sN, sC)):
        _ticks(cv, P, Q, 1)
    _txt(cv, (_mid(sA, sB)[0], sA[1] - 14), f"AB = {_fmt(ab)}", cls="lbl")
    _txt(cv, (_mid(sD, sC)[0], sD[1] + 21), f"CD = {_fmt(cd)}", cls="lbl")
    _txt(cv, (_mid(sM, sN)[0], sM[1] - 12), "MN", cls="lbl")
    _txt(cv, (sM[0] - 13, sM[1] + 4), "M", cls="lbl", anchor="end")
    _txt(cv, (sN[0] + 13, sN[1] + 4), "N", cls="lbl")
    _txt(cv, _away(sA, _centroid([sA, sB, sC, sD]), 15), "A", cls="lbl")
    _txt(cv, _away(sB, _centroid([sA, sB, sC, sD]), 15), "B", cls="lbl")
    _txt(cv, _away(sC, _centroid([sA, sB, sC, sD]), 15), "C", cls="lbl")
    _txt(cv, _away(sD, _centroid([sA, sB, sC, sD]), 15), "D", cls="lbl")
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "rhombus": build_rhombus,
    "square": build_square,
    "quad_diagonals": build_quad_diagonals,
    "regular_polygon": build_regular_polygon,
    "circle_chord": build_circle_chord,
    "circle_tangent": build_circle_tangent,
    "circle_sector": build_circle_sector,
    "annulus": build_annulus,
    "inscribed_angle": build_inscribed_angle,
    "arc_locus": build_arc_locus,
    "cyclic_quad": build_cyclic_quad,
    "circle_secants": build_circle_secants,
    "circle_positions": build_circle_positions,
    "triangle_centers": build_triangle_centers,
    "triangle_cevian": build_triangle_cevian,
    "equilateral_triangle": build_equilateral_triangle,
    "triangle_circumcircle": build_triangle_circumcircle,
    "triangle_incircle": build_triangle_incircle,
    "triangle_labeled": build_triangle_labeled,
    "right_triangle_altitude": build_right_triangle_altitude,
    "thales": build_thales,
    "trapezoid_midline": build_trapezoid_midline,
}


def render(generator: str, params: Params | None = None) -> str:
    if generator not in REGISTRY:
        raise KeyError(f"generator hinhphang không tồn tại: {generator}")
    return REGISTRY[generator](params or {})
