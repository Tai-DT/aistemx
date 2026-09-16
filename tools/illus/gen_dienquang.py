"""Generator SVG cho họ hình **điện - từ - quang - nhiệt - hạt nhân**.

Ba nhóm hình trong file này có yêu cầu chính xác rất khác nhau, và mã phản ánh
đúng sự khác nhau đó:

* **Sơ đồ mạch** chỉ cần đúng tô-pô (nối tiếp / song song / nguồn có điện trở
  trong) và đúng ký hiệu IEC, nên vẽ thẳng bằng toạ độ pixel.
* **Quang hình** bắt buộc tỉ lệ ĐỀU hai trục, và vị trí ảnh phải TÍNH từ công
  thức thấu kính/gương chứ không ước lượng "cho giống sách": người học không có
  cách nào kiểm tra lại một hình dựng ảnh sai.
* **Đồ thị (p-V, phân rã)** có khung toạ độ riêng, giá trị lấy từ hàm thật qua
  ``mathexpr.sample_curve``.

Mọi đoạn thẳng đều đi qua ``_clip_seg`` trước khi vẽ. Nhờ vậy tham số biên
(tiêu cự 0, vật ở rất xa, chu kì bán rã âm) chỉ làm hình rỗng bớt chứ không
đẩy toạ độ ra ngoài ``viewBox`` — một lỗi im lặng rất khó phát hiện khi hình
đã được nhúng vào bài giảng.
"""

from __future__ import annotations

import math
from typing import Callable, Optional, Sequence

from .mathexpr import sample_curve
from .svgkit import Canvas, _n

Params = dict

_EPS = 1e-9


# --------------------------------------------------------------------------
# Tiện ích chung
# --------------------------------------------------------------------------
def _num(p: Params, key: str, default: float) -> float:
    """Đọc tham số số; giá trị hỏng (None, chuỗi, NaN, inf) rơi về mặc định.

    Generator được gọi từ dữ liệu tự sinh, nên phải chịu được params bẩn: một
    hình đơn giản hoá còn hơn một traceback giữa trang bài.
    """
    try:
        v = float(p.get(key, default))
    except (TypeError, ValueError):
        return float(default)
    return v if math.isfinite(v) else float(default)


def _texts(p: Params, key: str, default: Sequence[str], cap: int = 5) -> list[str]:
    """Đọc danh sách nhãn; cắt ở ``cap`` phần tử vì quá đó hình hết đọc được."""
    v = p.get(key)
    if not isinstance(v, (list, tuple)) or not v:
        return [str(s) for s in default]
    out = [str(s) for s in v][:cap]
    return out or [str(s) for s in default]


def _st(fill: str | None = None, width: float | None = None,
        dash: str | None = None) -> str:
    """Ghi đè nét/tô bằng thuộc tính ``style``, KHÔNG bằng attribute rời.

    Bảng màu của ``svgkit`` đặt ``fill`` và ``stroke-width`` trong lớp CSS, mà
    quy tắc CSS thắng attribute trình bày. Viết ``fill="none"`` kiểu attribute
    sẽ bị lớp ``.accent-a`` ghi đè và cả chùm đường sức biến thành đĩa đặc —
    một lỗi chỉ lộ ra khi nhìn ảnh, không lộ ra khi kiểm SVG hợp lệ.
    """
    parts: list[str] = []
    if fill is not None:
        parts.append(f"fill:{fill}")
    if width is not None:
        parts.append(f"stroke-width:{_n(width)}")
    if dash is not None:
        parts.append(f"stroke-dasharray:{dash}")
    return f' style="{";".join(parts)}"' if parts else ""


def _clip_seg(x1: float, y1: float, x2: float, y2: float,
              box: Sequence[float]) -> Optional[tuple[float, float, float, float]]:
    """Cắt đoạn thẳng vào hình chữ nhật ``box = (x, y, w, h)`` (Liang-Barsky).

    Trả ``None`` nếu đoạn nằm hoàn toàn ngoài khung.
    """
    x0, y0, w, h = box
    xmax, ymax = x0 + w, y0 + h
    dx, dy = x2 - x1, y2 - y1
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, x1 - x0), (dx, xmax - x1), (-dy, y1 - y0), (dy, ymax - y1)):
        if abs(pp) < _EPS:
            if qq < 0:
                return None
            continue
        r = qq / pp
        if pp < 0:
            if r > t1:
                return None
            t0 = max(t0, r)
        else:
            if r < t0:
                return None
            t1 = min(t1, r)
    return (x1 + t0 * dx, y1 + t0 * dy, x1 + t1 * dx, y1 + t1 * dy)


def _seg(cv: Canvas, box, x1, y1, x2, y2, cls="ink", extra="") -> None:
    """Vẽ đoạn thẳng ĐÃ cắt về khung; ngoài khung thì bỏ hẳn."""
    c = _clip_seg(x1, y1, x2, y2, box)
    if c is not None and (abs(c[2] - c[0]) > 0.05 or abs(c[3] - c[1]) > 0.05):
        cv.line(c[0], c[1], c[2], c[3], cls=cls, extra=extra)


def _head(cv: Canvas, x: float, y: float, ang: float, size: float = 7.0,
          cls: str = "accent-a") -> None:
    """Đầu mũi tên đặc tại (x, y), ``ang`` là hướng đi TRÊN MÀN HÌNH (rad).

    Tách khỏi ``Canvas.arrow`` vì arrow ép nét 2.5 px — quá dày cho chùm đường
    sức, mà chèn thêm ``stroke-width`` sẽ sinh thuộc tính trùng (XML hỏng).
    """
    a1, a2 = ang + math.radians(150), ang - math.radians(150)
    cv.polygon(
        [(x, y), (x + size * math.cos(a1), y + size * math.sin(a1)),
         (x + size * math.cos(a2), y + size * math.sin(a2))],
        cls=cls, extra=' stroke="none" fill-opacity="1"',
    )


def _arrow_at(cv: Canvas, x1, y1, x2, y2, cls="accent-a", frac=1.0, size=7.0,
              width=1.8, dash="") -> None:
    """Đoạn thẳng có mũi tên đặt ở vị trí ``frac`` dọc đoạn (1.0 = ở cuối)."""
    extra = _st(width=width, dash=dash or None)
    cv.line(x1, y1, x2, y2, cls=cls, extra=extra)
    hx, hy = x1 + (x2 - x1) * frac, y1 + (y2 - y1) * frac
    _head(cv, hx, hy, math.atan2(y2 - y1, x2 - x1), size=size, cls=cls)


def _arc(cv: Canvas, cx, cy, r, a0_deg, a1_deg, cls="ink-thin", width=None) -> None:
    """Cung tròn theo góc TOÁN HỌC (ngược chiều kim đồng hồ, độ).

    Luôn ép ``fill:none``: cung góc mà bị tô sẽ thành một múi quạt đặc che mất
    tia sáng bên dưới, và cả hai lớp ``accent-*`` đều có ``fill`` mặc định.
    """
    a0, a1 = math.radians(a0_deg), math.radians(a1_deg)
    x0, y0 = cx + r * math.cos(a0), cy - r * math.sin(a0)
    x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
    large = 1 if abs(a1_deg - a0_deg) > 180 else 0
    sweep = 0 if a1_deg > a0_deg else 1  # trục y màn hình lộn ngược so với toán học
    cv.path(f"M {_n(x0)} {_n(y0)} A {_n(r)} {_n(r)} 0 {large} {sweep} {_n(x1)} {_n(y1)}",
            cls=cls, extra=_st(fill="none", width=width))


def _dim(cv: Canvas, x1, y1, x2, y2, label: str, off: float = 0.0) -> None:
    """Đường kích thước hai đầu mũi tên kèm nhãn ở giữa."""
    ang = math.atan2(y2 - y1, x2 - x1)
    cv.line(x1, y1, x2, y2, cls="ink-thin")
    _head(cv, x2, y2, ang, size=6, cls="ink-thin")
    _head(cv, x1, y1, ang + math.pi, size=6, cls="ink-thin")
    cv.text((x1 + x2) / 2, (y1 + y2) / 2 - 6 + off, label, cls="lbl-sm", anchor="middle")


class _Frame:
    """Ánh xạ toạ độ vật lí -> pixel với tỉ lệ ĐỀU trên hai trục.

    Quang hình bắt buộc tỉ lệ đều: x và y co giãn khác nhau thì góc tới, góc
    khúc xạ, độ dốc tia ló đều sai — và đó là kiểu sai người học không kiểm
    chứng được.
    """

    def __init__(self, box: Sequence[float], half_x: float):
        self.box = tuple(box)
        x0, y0, w, h = box
        self.k = w / (2 * max(half_x, _EPS))
        self.cx = x0 + w / 2
        self.cy = y0 + h / 2
        self.half_y = (h / 2) / self.k

    def X(self, x: float) -> float:
        return self.cx + x * self.k

    def Y(self, y: float) -> float:
        return self.cy - y * self.k

    def P(self, x: float, y: float) -> tuple[float, float]:
        return (self.X(x), self.Y(y))

    def inside(self, x: float, y: float, margin: float = 0.0) -> bool:
        px, py = self.P(x, y)
        x0, y0, w, h = self.box
        return (x0 + margin <= px <= x0 + w - margin
                and y0 + margin <= py <= y0 + h - margin)

    def seg(self, cv: Canvas, xa, ya, xb, yb, cls="ink", extra="") -> None:
        _seg(cv, self.box, *self.P(xa, ya), *self.P(xb, yb), cls=cls, extra=extra)

    def ray(self, cv: Canvas, x0: float, y0: float, dx: float, dy: float,
            cls="accent-a", extra="", arrow_cls: str | None = None) -> None:
        """Vẽ tia từ (x0,y0) theo hướng (dx,dy), kéo dài rồi cắt về khung."""
        norm = math.hypot(dx, dy)
        if norm < _EPS:
            return
        big = 4 * (self.box[2] + self.box[3]) / self.k
        xe, ye = x0 + dx / norm * big, y0 + dy / norm * big
        c = _clip_seg(*self.P(x0, y0), *self.P(xe, ye), self.box)
        if c is None:
            return
        cv.line(c[0], c[1], c[2], c[3], cls=cls, extra=extra)
        if arrow_cls:
            mx, my = (c[0] + c[2]) / 2, (c[1] + c[3]) / 2
            _head(cv, mx, my, math.atan2(c[3] - c[1], c[2] - c[0]), size=6.5, cls=arrow_cls)


class _Axes:
    """Khung đồ thị có trục (p-V, đường phân rã). Không cần tỉ lệ đều."""

    def __init__(self, box: Sequence[float], xmax: float, ymax: float):
        self.box = tuple(box)
        self.xmax = max(xmax, _EPS)
        self.ymax = max(ymax, _EPS)

    def X(self, x: float) -> float:
        return self.box[0] + x / self.xmax * self.box[2]

    def Y(self, y: float) -> float:
        return self.box[1] + self.box[3] - y / self.ymax * self.box[3]

    def P(self, x, y):
        return (self.X(x), self.Y(y))

    def frame(self, cv: Canvas, xlabel: str, ylabel: str) -> None:
        x0, y0, w, h = self.box
        cv.arrow(x0, y0 + h, x0 + w + 12, y0 + h, cls="axis", head=7)
        cv.arrow(x0, y0 + h, x0, y0 - 12, cls="axis", head=7)
        cv.text(x0 + w + 10, y0 + h + 18, xlabel, cls="lbl", anchor="end")
        cv.text(x0 + 6, y0 - 16, ylabel, cls="lbl")
        cv.text(x0 - 8, y0 + h + 15, "O", cls="lbl-sm", anchor="middle")

    def curve(self, cv: Canvas, pts: Sequence[tuple[float, float]], cls="curve",
              width: float | None = None) -> None:
        """Vẽ đường qua các điểm thế giới, đã lọc điểm ra ngoài khung.

        Ép ``fill:none`` qua ``style``: các lớp ``accent-*`` có ``fill`` mặc
        định, và một đường cong p-V bị tô sẽ biến thành mảng màu đặc nuốt luôn
        những đường quá trình vẽ chồng lên nó.
        """
        extra = _st(fill="none", width=width)
        run: list[tuple[float, float]] = []
        for x, y in pts:
            if 0 <= x <= self.xmax * 1.001 and 0 <= y <= self.ymax * 1.001:
                run.append(self.P(x, y))
            elif len(run) >= 2:
                cv.polyline(run, cls=cls, extra=extra)
                run = []
            else:
                run = []
        if len(run) >= 2:
            cv.polyline(run, cls=cls, extra=extra)


# --------------------------------------------------------------------------
# Ký hiệu mạch điện (IEC)
# --------------------------------------------------------------------------
_RES_L, _RES_W = 46.0, 18.0     # dài / rộng thân điện trở hình chữ nhật


def _sym_resistor(cv: Canvas, cx, cy, label="", vertical=False) -> None:
    """Điện trở: hình chữ nhật rỗng (IEC 60617), KHÔNG dùng ký hiệu răng cưa."""
    if vertical:
        cv.rect(cx - _RES_W / 2, cy - _RES_L / 2, _RES_W, _RES_L, cls="ink")
        if label:
            cv.text(cx + _RES_W / 2 + 7, cy + 5, label, cls="lbl")
    else:
        cv.rect(cx - _RES_L / 2, cy - _RES_W / 2, _RES_L, _RES_W, cls="ink")
        if label:
            cv.text(cx, cy - _RES_W / 2 - 8, label, cls="lbl", anchor="middle")


def _sym_battery(cv: Canvas, cx, cy, vertical=True, label="", plus_first=True) -> None:
    """Nguồn một chiều: vạch DÀI là cực dương, vạch NGẮN là cực âm.

    ``plus_first`` = cực dương nằm ở phía trên (dọc) hoặc bên phải (ngang) —
    quyết định chiều dòng điện quy ước vẽ trên sơ đồ.
    """
    long_h, short_h = 26.0, 14.0
    if vertical:
        y_plus = cy - 6 if plus_first else cy + 6
        y_minus = cy + 6 if plus_first else cy - 6
        cv.line(cx - long_h / 2, y_plus, cx + long_h / 2, y_plus, cls="ink")
        cv.line(cx - short_h / 2, y_minus, cx + short_h / 2, y_minus,
                cls="ink", extra=_st(width=4))
        cv.text(cx - long_h / 2 - 6, y_plus + 4, "+", cls="lbl-sm", anchor="end")
        cv.text(cx - long_h / 2 - 6, y_minus + 5, "−", cls="lbl-sm", anchor="end")
        if label:
            cv.text(cx + long_h / 2 + 8, cy + 5, label, cls="lbl")
    else:
        x_plus = cx + 6 if plus_first else cx - 6
        x_minus = cx - 6 if plus_first else cx + 6
        cv.line(x_plus, cy - long_h / 2, x_plus, cy + long_h / 2, cls="ink")
        cv.line(x_minus, cy - short_h / 2, x_minus, cy + short_h / 2,
                cls="ink", extra=_st(width=4))
        cv.text(x_plus + 4, cy + long_h / 2 + 15, "+", cls="lbl-sm", anchor="middle")
        cv.text(x_minus - 4, cy + long_h / 2 + 15, "−", cls="lbl-sm", anchor="middle")
        if label:
            cv.text(cx, cy - long_h / 2 - 7, label, cls="lbl", anchor="middle")


def _sym_capacitor(cv: Canvas, cx, cy, label="") -> None:
    """Tụ điện trên dây ngang: hai bản song song, khe hở 8 px."""
    cv.line(cx - 4, cy - 13, cx - 4, cy + 13, cls="ink")
    cv.line(cx + 4, cy - 13, cx + 4, cy + 13, cls="ink")
    if label:
        cv.text(cx, cy - 20, label, cls="lbl", anchor="middle")


def _sym_inductor(cv: Canvas, cx, cy, label="", turns=4) -> None:
    """Cuộn cảm trên dây ngang: chuỗi nửa cung tròn nhô lên."""
    r = _RES_L / (2 * turns)
    x = cx - _RES_L / 2
    d = [f"M {_n(x)} {_n(cy)}"]
    for _ in range(turns):
        d.append(f"a {_n(r)} {_n(r)} 0 0 1 {_n(2 * r)} 0")
    cv.path(" ".join(d), cls="ink")
    if label:
        cv.text(cx, cy - r - 10, label, cls="lbl", anchor="middle")


def _sym_meter(cv: Canvas, cx, cy, letter: str, r: float = 13.0) -> None:
    """Ampe kế (A) / vôn kế (V): vòng tròn có chữ."""
    cv.circle(cx, cy, r, cls="ink")
    cv.text(cx, cy + 5, letter, cls="lbl-sm", anchor="middle")


def _sym_ac(cv: Canvas, cx, cy, r: float = 17.0, label="") -> None:
    """Nguồn xoay chiều: vòng tròn có hình sin."""
    cv.circle(cx, cy, r, cls="ink")
    a = r * 0.55
    cv.path(
        f"M {_n(cx - a)} {_n(cy)} C {_n(cx - a * 0.6)} {_n(cy - a * 1.5)},"
        f" {_n(cx - a * 0.3)} {_n(cy - a * 1.5)}, {_n(cx)} {_n(cy)}"
        f" C {_n(cx + a * 0.3)} {_n(cy + a * 1.5)},"
        f" {_n(cx + a * 0.6)} {_n(cy + a * 1.5)}, {_n(cx + a)} {_n(cy)}",
        cls="ink",
    )
    if label:
        cv.text(cx - r - 8, cy + 5, label, cls="lbl", anchor="end")


def _sym_switch(cv: Canvas, cx, cy, w: float = 30.0) -> None:
    """Khoá K hở: hai chấm nối và một thanh nghiêng."""
    cv.dot(cx - w / 2, cy, 3, cls="accent-a")
    cv.dot(cx + w / 2, cy, 3, cls="accent-a")
    cv.line(cx - w / 2, cy, cx + w / 2 - 4, cy - 14, cls="ink")
    cv.text(cx, cy + 18, "K", cls="lbl", anchor="middle")


def _wire_gaps(cv: Canvas, y: float, x_from: float, x_to: float,
               gaps: Sequence[tuple[float, float]]) -> None:
    """Vẽ dây ngang từ x_from đến x_to, chừa các khoảng ``gaps`` cho linh kiện."""
    cur = x_from
    for g0, g1 in sorted(gaps):
        if g0 > cur:
            cv.line(cur, y, g0, y, cls="ink")
        cur = max(cur, g1)
    if x_to > cur:
        cv.line(cur, y, x_to, y, cls="ink")


# --------------------------------------------------------------------------
# 1. Sơ đồ mạch một chiều
# --------------------------------------------------------------------------
def build_circuit_series(p: Params) -> str:
    """Mạch nối tiếp: nguồn + n điện trở, tuỳ chọn ampe kế và vôn kế.

    Ampe kế mắc NỐI TIẾP trên dây, vôn kế mắc SONG SONG với điện trở được đo —
    vẽ ngược lại là dạy sai một trong những lỗi hay gặp nhất của học sinh.
    """
    labels = _texts(p, "resistors", ["R₁", "R₂"])
    n = len(labels)
    ammeter = bool(p.get("ammeter", False))
    vm = p.get("voltmeter")
    vm_idx = vm if isinstance(vm, int) and 0 <= vm < n else None
    caption = str(p.get("caption") or "")
    source = str(p.get("source") or "U")

    left, top, bot = 62.0, 64.0, 198.0
    inner = max(230.0, n * 112.0)
    right = left + inner
    width = right + 48
    height = bot + (54 if caption else 32)

    cv = Canvas(width, height, title="Mạch điện nối tiếp",
                desc="Sơ đồ mạch điện: nguồn một chiều nối tiếp với "
                     + ", ".join(labels) + ".")
    xs = [left + (i + 0.5) * inner / n for i in range(n)]
    _wire_gaps(cv, top, left, right, [(x - _RES_L / 2, x + _RES_L / 2) for x in xs])
    mid = (top + bot) / 2
    cv.line(left, top, left, mid - 16, cls="ink")
    cv.line(left, mid + 16, left, bot, cls="ink")
    cv.line(right, top, right, bot, cls="ink")
    if ammeter:
        xa = (left + right) / 2
        _wire_gaps(cv, bot, left, right, [(xa - 13, xa + 13)])
        _sym_meter(cv, xa, bot, "A")
    else:
        cv.line(left, bot, right, bot, cls="ink")
    _sym_battery(cv, left, mid, vertical=True, label=source, plus_first=True)
    for x, lb in zip(xs, labels):
        _sym_resistor(cv, x, top, label=lb)
    # Cực dương ở trên nên dòng quy ước đi lên dây trái rồi sang phải trên dây trên.
    x0 = left + 14
    _arrow_at(cv, x0, top, x0 + 34, top, cls="accent-b", width=2.2, size=8)
    cv.text(x0 + 17, top - 9, "I", cls="lbl", anchor="middle")
    if vm_idx is not None:
        xc = xs[vm_idx]
        yv = top + 44
        cv.line(xc - _RES_L / 2, top, xc - _RES_L / 2, yv, cls="ink-thin")
        cv.line(xc + _RES_L / 2, top, xc + _RES_L / 2, yv, cls="ink-thin")
        cv.line(xc - _RES_L / 2, yv, xc - 13, yv, cls="ink-thin")
        cv.line(xc + 13, yv, xc + _RES_L / 2, yv, cls="ink-thin")
        _sym_meter(cv, xc, yv, "V")
    if caption:
        cv.text(width / 2, bot + 40, caption, cls="lbl", anchor="middle")
    return cv.render()


def build_circuit_parallel(p: Params) -> str:
    """Mạch song song: các điện trở nằm giữa hai thanh cái, cùng hiệu điện thế."""
    labels = _texts(p, "resistors", ["R₁", "R₂"])
    n = len(labels)
    caption = str(p.get("caption") or "")
    source = str(p.get("source") or "U")

    left, top, bot = 66.0, 66.0, 208.0
    inner = max(210.0, n * 96.0)
    right = left + inner
    width = right + 60
    height = bot + (54 if caption else 34)

    cv = Canvas(width, height, title="Mạch điện song song",
                desc="Sơ đồ mạch điện: nguồn một chiều và các điện trở "
                     + ", ".join(labels) + " mắc song song.")
    mid = (top + bot) / 2
    cv.line(left, top, right, top, cls="ink")
    cv.line(left, bot, right, bot, cls="ink")
    cv.line(left, top, left, mid - 16, cls="ink")
    cv.line(left, mid + 16, left, bot, cls="ink")
    _sym_battery(cv, left, mid, vertical=True, label=source, plus_first=True)
    xs = [left + (i + 1) * inner / (n + 1) for i in range(n)]
    for x, lb in zip(xs, labels):
        cv.line(x, top, x, mid - _RES_L / 2, cls="ink")
        cv.line(x, mid + _RES_L / 2, x, bot, cls="ink")
        _sym_resistor(cv, x, mid, label=lb, vertical=True)
        cv.dot(x, top, 3, cls="accent-a")
        cv.dot(x, bot, 3, cls="accent-a")
    # Dòng mạch chính rẽ tại nút, nên vẽ mũi tên I trước nút đầu tiên.
    _arrow_at(cv, left + 12, top, left + 44, top, cls="accent-b", width=2.2, size=8)
    cv.text(left + 28, top - 9, "I", cls="lbl", anchor="middle")
    cv.line(right, top, right, bot, cls="ink")
    cv.text(right + 14, mid + 5, "U", cls="lbl")
    if caption:
        cv.text(width / 2, bot + 40, caption, cls="lbl", anchor="middle")
    return cv.render()


def build_circuit_emf(p: Params) -> str:
    """Toàn mạch: nguồn (ξ, r) ở trong khung nét đứt, mạch ngoài R_N.

    Điện trở trong r vẽ NẰM TRONG khung nguồn để thấy rõ vì sao U_N = ξ − I·r
    chứ không phải một điện trở rời của mạch ngoài.
    """
    caption = str(p.get("caption") or "")
    rn_label = str(p.get("load") or "R_N")
    emf_label = str(p.get("emf") or "ξ")
    r_label = str(p.get("r") or "r")

    left, right, top, bot = 66.0, 348.0, 70.0, 206.0
    width, height = right + 46, bot + (68 if caption else 46)
    cv = Canvas(width, height, title="Mạch kín có nguồn điện",
                desc="Nguồn điện suất điện động ξ, điện trở trong r, "
                     "mạch ngoài điện trở R_N.")
    bx1, bx2 = left + 62, left + 148
    _wire_gaps(cv, bot, left, right, [(bx1 - 14, bx1 + 14), (bx2 - _RES_L / 2, bx2 + _RES_L / 2)])
    _wire_gaps(cv, top, left, right, [((left + right) / 2 - _RES_L / 2, (left + right) / 2 + _RES_L / 2)])
    cv.line(left, top, left, bot, cls="ink")
    cv.line(right, top, right, bot, cls="ink")
    box_x, box_w = left - 14, bx2 - left + 46
    cv.rect(box_x, bot - 42, box_w, 74, cls="ink-thin", extra=_st(dash="6 4"))
    cv.text(box_x + box_w / 2, bot - 50, "nguồn điện", cls="lbl-sm", anchor="middle")
    _sym_battery(cv, bx1, bot, vertical=False, label=emf_label, plus_first=True)
    _sym_resistor(cv, bx2, bot, label=r_label)
    _sym_resistor(cv, (left + right) / 2, top, label=rn_label)
    # Cực dương quay sang phải nên dòng đi phải -> lên -> trái qua mạch ngoài.
    _arrow_at(cv, right, bot - 20, right, bot - 54, cls="accent-b", width=2.2, size=8)
    cv.text(right + 8, bot - 34, "I", cls="lbl")
    cv.text((left + right) / 2, top - 30, f"U_N = {emf_label} − I·{r_label}",
            cls="lbl-sm", anchor="middle")
    if caption:
        cv.text(width / 2, bot + 56, caption, cls="lbl", anchor="middle")
    return cv.render()


def build_circuit_rlc(p: Params) -> str:
    """Mạch xoay chiều: các phần tử trong ``elements`` mắc nối tiếp với nguồn ~.

    ``elements`` cho phép dựng cả mạch chỉ chứa R, chỉ chứa L, chỉ chứa C —
    vẽ đủ R-L-C cho một công thức chỉ nói về tụ điện là minh hoạ sai đề.
    """
    raw = p.get("elements")
    allowed = ("R", "L", "C")
    seq = raw if isinstance(raw, (list, tuple, str)) else ()
    els = [str(e).upper() for e in seq if str(e).upper() in allowed]
    if not els:
        els = ["R", "L", "C"]
    caption = str(p.get("caption") or "")
    show_u = bool(p.get("show_u", True))

    left, top, bot = 74.0, 74.0, 200.0
    inner = max(210.0, len(els) * 104.0)
    right = left + inner
    width, height = right + 46, bot + (56 if caption else 34)
    names = {"R": "R", "L": "L", "C": "C"}
    ulab = {"R": "u_R", "L": "u_L", "C": "u_C"}
    cv = Canvas(width, height, title="Mạch xoay chiều nối tiếp",
                desc="Nguồn điện xoay chiều nối tiếp với " + " - ".join(els) + ".")
    xs = [left + (i + 0.5) * inner / len(els) for i in range(len(els))]
    # Tụ điện chỉ chừa khe hẹp bằng đúng khoảng cách hai bản; R và L chiếm trọn
    # chiều dài thân nên khe rộng hơn.
    gaps = [(x - (8.0 if e == "C" else _RES_L / 2), x + (8.0 if e == "C" else _RES_L / 2))
            for x, e in zip(xs, els)]
    _wire_gaps(cv, top, left, right, gaps)
    mid = (top + bot) / 2
    cv.line(left, top, left, mid - 17, cls="ink")
    cv.line(left, mid + 17, left, bot, cls="ink")
    cv.line(right, top, right, bot, cls="ink")
    cv.line(left, bot, right, bot, cls="ink")
    _sym_ac(cv, left, mid, label="u")
    for x, e in zip(xs, els):
        if e == "R":
            _sym_resistor(cv, x, top, label=names[e])
        elif e == "L":
            _sym_inductor(cv, x, top, label=names[e])
        else:
            _sym_capacitor(cv, x, top, label=names[e])
        if show_u:
            cv.text(x, top + 26, ulab[e], cls="lbl-sm", anchor="middle")
    _arrow_at(cv, left + 12, top, left + 44, top, cls="accent-b", width=2.2, size=8)
    cv.text(left + 28, top - 26, "i", cls="lbl", anchor="middle")
    if caption:
        cv.text(width / 2, bot + 42, caption, cls="lbl", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 2. Giản đồ vectơ Fre-nen
# --------------------------------------------------------------------------
def build_phasor_rlc(p: Params) -> str:
    """Giản đồ Fre-nen mạch RLC nối tiếp.

    Trục hoành lấy theo vectơ dòng điện (chung cho ba phần tử vì mắc nối tiếp);
    U_L vượt pha +90°, U_C trễ pha −90°. Vectơ tổng dựng bằng quy tắc đa giác
    nên U, U_R và (U_L − U_C) luôn tạo đúng tam giác vuông của công thức
    U² = U_R² + (U_L − U_C)².
    """
    ur = abs(_num(p, "UR", 3.0))
    ul = abs(_num(p, "UL", 4.0))
    uc = abs(_num(p, "UC", 1.5))
    if bool(p.get("resonance", False)):
        uc = ul  # cộng hưởng: hai vectơ ngược pha triệt tiêu nhau
    sym = str(p.get("quantity") or "U")
    labels = {"U": ("U_R", "U_L", "U_C", "U"), "Z": ("R", "Z_L", "Z_C", "Z")}
    lr, ll, lc, lt = labels.get(sym, labels["U"])

    dy = ul - uc
    span = max(ur, ul, uc, abs(dy), 1e-3)
    cv = Canvas(400.0, 320.0, title="Giản đồ vectơ Fre-nen của mạch RLC",
                desc="Giản đồ vectơ: U_R theo trục dòng điện, U_L vượt pha 90 độ, "
                     "U_C trễ pha 90 độ, vectơ tổng U.")
    box = (46.0, 26.0, 320.0, 236.0)
    fr = _Frame(box, span * 1.45)
    ox, oy = fr.P(0, 0)
    # Trục: hoành = phương của i, tung = phương vượt pha 90°.
    _seg(cv, box, box[0], oy, box[0] + box[2], oy, cls="axis")
    _seg(cv, box, ox, box[1], ox, box[1] + box[3], cls="axis")
    cv.text(box[0] + box[2] - 4, oy + 18, "i", cls="lbl", anchor="end")

    pr = fr.P(ur, 0)
    pl = fr.P(0, ul)
    pc = fr.P(0, -uc)
    pd = fr.P(ur, dy)
    cv.arrow(ox, oy, *pl, cls="accent-c", head=8)
    cv.text(pl[0] - 8, pl[1] - 6, ll, cls="lbl", anchor="end")
    cv.arrow(ox, oy, *pc, cls="accent-d", head=8)
    cv.text(pc[0] - 8, pc[1] + 14, lc, cls="lbl", anchor="end")
    cv.arrow(ox, oy, *pr, cls="accent-a", head=9)
    cv.text((ox + pr[0]) / 2, oy + 18, lr, cls="lbl", anchor="middle")
    if abs(dy) > 1e-6:
        cv.arrow(pr[0], pr[1], pd[0], pd[1], cls="accent-c", head=8)
        cv.text(pd[0] + 8, (pr[1] + pd[1]) / 2, f"{ll} − {lc}", cls="lbl-sm")
        cv.line(pl[0], pl[1], pd[0], pd[1], cls="ink-thin", extra=_st(dash="5 4"))
        cv.arrow(ox, oy, pd[0], pd[1], cls="accent-b", head=10)
        cv.text(pd[0] + 10, pd[1] - 6, lt, cls="lbl")
        cv.right_angle(pr[0], pr[1], ox, oy, pd[0], pd[1], size=11)
        phi = math.degrees(math.atan2(dy, ur))
        _arc(cv, ox, oy, 42, 0, phi, cls="accent-b", width=1.8)
        # Đặt nhãn φ trên tia phân giác của góc: nằm gọn giữa U_R và U thay vì
        # đè lên chính hai vectơ đang cần đọc.
        hb = math.radians(phi / 2)
        cv.text(ox + 52 * math.cos(hb), oy - 52 * math.sin(hb) + 4, "φ", cls="lbl")
    else:
        cv.text(pr[0] + 10, pr[1] - 8, f"{lt} ≡ {lr}", cls="lbl")
        cv.text(ox + 44, oy - 10, "φ = 0", cls="lbl-sm")
    cv.text(box[0], box[1] + box[3] + 34,
            "cộng hưởng: φ = 0" if abs(dy) <= 1e-6 else
            (f"φ = {_n(round(math.degrees(math.atan2(dy, ur)), 1))}° — mạch có tính "
             + ("cảm kháng" if dy > 0 else "dung kháng")),
            cls="lbl-sm")
    return cv.render()


# --------------------------------------------------------------------------
# 3. Đường sức điện trường và từ trường
# --------------------------------------------------------------------------
def build_field_point_charge(p: Params) -> str:
    """Đường sức của một điện tích điểm: hướng ra nếu q > 0, hướng vào nếu q < 0."""
    sign = 1.0 if _num(p, "sign", 1.0) >= 0 else -1.0
    nlines = int(max(6, min(20, _num(p, "lines", 12))))
    equi = bool(p.get("equipotential", False))
    size = 320.0
    cv = Canvas(size, size, title="Điện trường của điện tích điểm",
                desc=("Đường sức hướng ra xa điện tích dương." if sign > 0
                      else "Đường sức hướng vào điện tích âm."))
    cx = cy = size / 2
    r_in, r_out = 20.0, 128.0
    if equi:
        for rr in (52.0, 84.0, 116.0):
            cv.circle(cx, cy, rr, cls="ink-thin", extra=_st(dash="4 5"))
        cv.text(cx + 116 * 0.72, cy - 116 * 0.72, "mặt đẳng thế", cls="lbl-sm")
    for i in range(nlines):
        a = 2 * math.pi * i / nlines
        ux, uy = math.cos(a), math.sin(a)
        x1, y1 = cx + r_in * ux, cy + r_in * uy
        x2, y2 = cx + r_out * ux, cy + r_out * uy
        cv.line(x1, y1, x2, y2, cls="accent-a", extra=_st(width=1.5))
        mx, my = cx + (r_in + r_out) / 2 * ux, cy + (r_in + r_out) / 2 * uy
        ang = math.atan2(uy, ux) if sign > 0 else math.atan2(-uy, -ux)
        _head(cv, mx, my, ang, size=7, cls="accent-a")
    cv.circle(cx, cy, r_in * 0.72, cls="fill-b" if sign > 0 else "fill-a")
    cv.circle(cx, cy, r_in * 0.72, cls="ink")
    cv.text(cx, cy + 6, "+q" if sign > 0 else "−q", cls="lbl", anchor="middle")
    # Cùng một hình dùng cho cả E lẫn V quanh điện tích điểm, nên dòng chú thích
    # phải do luật khớp quyết định — ghi cứng "E = ..." dưới công thức điện thế
    # là dán nhầm nhãn cho hình.
    cv.text(size / 2, size - 10,
            str(p.get("caption") or f"E = k|Q| / r²   "
                f"({'điện tích dương' if sign > 0 else 'điện tích âm'})"),
            cls="lbl-sm", anchor="middle")
    return cv.render()


def build_coulomb_two_charges(p: Params) -> str:
    """Tương tác Cu-lông giữa hai điện tích điểm cách nhau r.

    Chiều lực suy TỪ dấu của hai điện tích: cùng dấu thì đẩy, trái dấu thì hút.
    Vẽ cứng một chiều rồi đổi nhãn là kiểu sai kinh điển của hình minh hoạ.
    """
    s1 = 1.0 if _num(p, "q1", 1.0) >= 0 else -1.0
    s2 = 1.0 if _num(p, "q2", 1.0) >= 0 else -1.0
    repel = s1 * s2 > 0
    w, h = 420.0, 190.0
    cv = Canvas(w, h, title="Lực tương tác giữa hai điện tích điểm",
                desc=("Hai điện tích cùng dấu đẩy nhau." if repel
                      else "Hai điện tích trái dấu hút nhau."))
    y = 84.0
    x1, x2 = 120.0, 300.0
    r_c = 17.0
    cv.line(x1, y, x2, y, cls="ink-thin", extra=_st(dash="5 4"))
    for x, s in ((x1, s1), (x2, s2)):
        cv.circle(x, y, r_c, cls="fill-b" if s > 0 else "fill-a")
        cv.circle(x, y, r_c, cls="ink")
    cv.text(x1, y + 6, "q₁", cls="lbl", anchor="middle")
    cv.text(x2, y + 6, "q₂", cls="lbl", anchor="middle")
    cv.text(x1, y - r_c - 8, "+" if s1 > 0 else "−", cls="lbl-sm", anchor="middle")
    cv.text(x2, y - r_c - 8, "+" if s2 > 0 else "−", cls="lbl-sm", anchor="middle")
    d = 62.0
    if repel:
        _arrow_at(cv, x1 - r_c, y, x1 - r_c - d, y, cls="accent-b", width=2.4, size=9)
        _arrow_at(cv, x2 + r_c, y, x2 + r_c + d, y, cls="accent-b", width=2.4, size=9)
        cv.text(x1 - r_c - d / 2, y - 10, "F₁₂", cls="lbl", anchor="middle")
        cv.text(x2 + r_c + d / 2, y - 10, "F₂₁", cls="lbl", anchor="middle")
    else:
        _arrow_at(cv, x1 - 2, y - 30, x1 + 52, y - 30, cls="accent-b", width=2.4, size=9)
        _arrow_at(cv, x2 + 2, y - 30, x2 - 52, y - 30, cls="accent-b", width=2.4, size=9)
        cv.text(x1 + 26, y - 38, "F₁₂", cls="lbl", anchor="middle")
        cv.text(x2 - 26, y - 38, "F₂₁", cls="lbl", anchor="middle")
    _dim(cv, x1, y + 46, x2, y + 46, "r")
    cv.text(w / 2, h - 16, "F = k·|q₁q₂| / r²   —   "
            + ("cùng dấu: đẩy nhau" if repel else "trái dấu: hút nhau"),
            cls="lbl-sm", anchor="middle")
    return cv.render()


def build_field_parallel_plates(p: Params) -> str:
    """Điện trường đều giữa hai bản song song tích điện trái dấu.

    Đường sức đi từ bản dương sang bản âm, song song và cách đều — đúng cái làm
    nên E = U/d. Tuỳ chọn vẽ điện tích thử (lực F = qE) hoặc quỹ đạo parabol
    của hạt bay vuông góc vào điện trường.
    """
    charge = bool(p.get("charge", False))
    traj = bool(p.get("trajectory", False))
    nlines = int(max(4, min(12, _num(p, "lines", 7))))
    w, h = 430.0, 280.0
    cv = Canvas(w, h, title="Điện trường đều giữa hai bản song song",
                desc="Hai bản kim loại song song tích điện trái dấu, đường sức "
                     "điện đều hướng từ bản dương sang bản âm.")
    xl, xr = 76.0, 344.0
    yt, yb = 70.0, 200.0
    cv.line(xl, yt, xr, yt, cls="ink", extra=_st(width=4))
    cv.line(xl, yb, xr, yb, cls="ink", extra=_st(width=4))
    for i in range(5):
        x = xl + (i + 0.5) * (xr - xl) / 5
        cv.text(x, yt - 9, "+", cls="lbl-sm", anchor="middle")
        cv.text(x, yb + 17, "−", cls="lbl-sm", anchor="middle")
    for i in range(nlines):
        x = xl + (i + 0.5) * (xr - xl) / nlines
        cv.line(x, yt + 4, x, yb - 4, cls="accent-a", extra=_st(width=1.5))
        _head(cv, x, (yt + yb) / 2, math.pi / 2, size=7, cls="accent-a")
    cv.text(xr + 10, (yt + yb) / 2 + 5, "E", cls="lbl")
    if not traj:
        # Ở chế độ quỹ đạo, chỗ này là nơi vectơ v₀ đi vào — nhường chỗ cho nó.
        cv.text(xl - 12, (yt + yb) / 2 + 5, "U", cls="lbl", anchor="end")
        _dim(cv, xr + 36, yt, xr + 36, yb, "d")
    else:
        # Với bài toán hạt bay xuyên qua, đại lượng cần đọc là chiều dài bản ℓ,
        # không phải khoảng cách d — vẽ cả hai sẽ chồng lên nhau và rối.
        _dim(cv, xl, yb + 32, xr, yb + 32, "ℓ")
    if charge:
        cxq, cyq = (xl + xr) / 2, (yt + yb) / 2
        cv.circle(cxq, cyq, 12, cls="fill-b")
        cv.circle(cxq, cyq, 12, cls="ink")
        cv.text(cxq, cyq + 5, "+q", cls="lbl-sm", anchor="middle")
        _arrow_at(cv, cxq, cyq + 12, cxq, cyq + 46, cls="accent-b", width=2.4, size=9)
        cv.text(cxq + 8, cyq + 38, "F = qE", cls="lbl-sm")
    if traj:
        # Parabol y = a·x² của hạt vào vuông góc; hệ số chọn để hạt ra khỏi bản
        # ở khoảng 60% nửa khoảng cách — đúng dạng, không phải đúng số liệu.
        y0 = (yt + yb) / 2
        drop = 0.60 * (yb - yt) / 2
        pts = []
        for i in range(41):
            t = i / 40
            pts.append((xl + t * (xr - xl), y0 + drop * t * t))
        cv.polyline(pts, cls="curve")
        _arrow_at(cv, xl - 46, y0, xl - 6, y0, cls="accent-c", width=2.2, size=8)
        cv.text(xl - 26, y0 - 8, "v₀", cls="lbl", anchor="middle")
        ex, ey = pts[-1]
        cv.line(ex, ey, ex + 52, ey, cls="ink-thin", extra=_st(dash="4 4"))
        _arc(cv, ex, ey, 36, 0, -math.degrees(math.atan2(2 * drop, xr - xl)),
             cls="accent-d", width=1.8)
        cv.text(ex + 42, ey + 20, "α", cls="lbl")
        cv.dot(ex, ey, 3.4, cls="accent-b")
    cv.text(w / 2, h - 14,
            str(p.get("caption") or "E = U / d, đường sức song song và cách đều"),
            cls="lbl-sm", anchor="middle")
    return cv.render()


def build_field_wire(p: Params) -> str:
    """Từ trường của dòng điện thẳng dài, nhìn dọc theo dây.

    Dây vuông góc mặt phẳng hình vẽ, dòng hướng RA (ký hiệu ⊙); theo quy tắc
    nắm tay phải, đường sức là những đường tròn đồng tâm chiều NGƯỢC kim đồng
    hồ. Nếu đổi chiều dòng thì phải đổi cả chiều mũi tên — hai thứ đó gắn với
    nhau bằng vật lí, không phải bằng thẩm mĩ.
    """
    out = _num(p, "current_out", 1.0) >= 0
    size = 330.0
    cv = Canvas(size, size, title="Từ trường của dòng điện thẳng dài",
                desc="Các đường sức từ là những đường tròn đồng tâm quanh dây dẫn "
                     "thẳng, nằm trong mặt phẳng vuông góc với dây.")
    cx = cy = size / 2
    for rr in (44.0, 76.0, 108.0, 140.0):
        cv.circle(cx, cy, rr, cls="accent-a", extra=_st(fill="none", width=1.5))
        # Mũi tên tiếp tuyến: ngược kim đồng hồ khi dòng hướng ra khỏi trang.
        ang = math.radians(50)
        px, py = cx + rr * math.cos(ang), cy - rr * math.sin(ang)
        tang = math.atan2(-math.cos(ang), -math.sin(ang)) if out else \
            math.atan2(math.cos(ang), math.sin(ang))
        _head(cv, px, py, tang, size=7.5, cls="accent-a")
    cv.circle(cx, cy, 13, cls="ink")
    if out:
        cv.dot(cx, cy, 4, cls="accent-b")
    else:
        cv.line(cx - 9, cy - 9, cx + 9, cy + 9, cls="ink")
        cv.line(cx - 9, cy + 9, cx + 9, cy - 9, cls="ink")
    cv.text(cx - 20, cy + 5, "I", cls="lbl", anchor="end")
    ar = math.radians(-32)
    mx, my = cx + 108 * math.cos(ar), cy - 108 * math.sin(ar)
    cv.line(cx, cy, mx, my, cls="ink-thin", extra=_st(dash="5 4"))
    cv.text((cx + mx) / 2, (cy + my) / 2 + 16, "r", cls="lbl", anchor="middle")
    cv.dot(mx, my, 3.4, cls="accent-b")
    tb = math.atan2(-math.cos(ar), -math.sin(ar)) if out else math.atan2(math.cos(ar), math.sin(ar))
    _arrow_at(cv, mx, my, mx + 40 * math.cos(tb), my + 40 * math.sin(tb),
              cls="accent-b", width=2.3, size=8)
    cv.text(mx + 44 * math.cos(tb), my + 44 * math.sin(tb) + 4, "B", cls="lbl")
    cv.text(size / 2, size - 12,
            "dòng điện hướng ra khỏi mặt phẳng hình vẽ" if out
            else "dòng điện hướng vào mặt phẳng hình vẽ",
            cls="lbl-sm", anchor="middle")
    return cv.render()


def build_field_loop(p: Params) -> str:
    """Dòng điện tròn nhìn chính diện: B tại tâm vuông góc mặt phẳng vòng dây."""
    ccw = _num(p, "ccw", 1.0) >= 0
    size = 320.0
    cv = Canvas(size, size, title="Từ trường tại tâm dòng điện tròn",
                desc="Vòng dây tròn nhìn chính diện; cảm ứng từ tại tâm vuông góc "
                     "với mặt phẳng vòng dây.")
    cx = cy = size / 2 - 6
    R = 104.0
    cv.circle(cx, cy, R, cls="ink", extra=_st(width=2.5))
    for adeg in (60.0, 180.0, 300.0):
        a = math.radians(adeg)
        px, py = cx + R * math.cos(a), cy - R * math.sin(a)
        tang = math.atan2(-math.cos(a), -math.sin(a)) if ccw else \
            math.atan2(math.cos(a), math.sin(a))
        _head(cv, px, py, tang, size=9, cls="accent-b")
    cv.text(cx + R + 8, cy - 8, "I", cls="lbl")
    cv.line(cx, cy, cx + R * math.cos(math.radians(35)), cy - R * math.sin(math.radians(35)),
            cls="ink-thin", extra=_st(dash="5 4"))
    cv.text(cx + R * 0.5, cy - R * 0.28, "R", cls="lbl")
    cv.circle(cx, cy, 13, cls="ink-thin")
    if ccw:
        cv.dot(cx, cy, 4.2, cls="accent-c")
        note = "B hướng ra khỏi mặt phẳng hình vẽ"
    else:
        cv.line(cx - 9, cy - 9, cx + 9, cy + 9, cls="accent-c")
        cv.line(cx - 9, cy + 9, cx + 9, cy - 9, cls="accent-c")
        note = "B hướng vào mặt phẳng hình vẽ"
    cv.text(cx + 20, cy + 5, "B", cls="lbl")
    cv.text(size / 2, size - 10, note, cls="lbl-sm", anchor="middle")
    return cv.render()


def build_field_solenoid(p: Params) -> str:
    """Ống dây hình trụ cắt dọc: vòng trên ⊙, vòng dưới ⊗ nên B trong lòng hướng sang phải.

    Chiều B suy từ quy tắc nắm tay phải cho từng vòng: hàng trên có dòng hướng
    ra, hàng dưới hướng vào, cả hai đều cho B cùng chiều +x trong lòng ống.
    Đầu phải là cực Bắc vì đường sức đi ra ở đó.
    """
    turns = int(max(3, min(8, _num(p, "turns", 6))))
    w, h = 440.0, 280.0
    cv = Canvas(w, h, title="Từ trường trong lòng ống dây",
                desc="Ống dây hình trụ; trong lòng ống các đường sức từ song song "
                     "và cách đều, ngoài ống chúng khép kín từ cực Bắc về cực Nam.")
    xl, xr = 110.0, 330.0
    yt, yb = 96.0, 184.0
    cv.rect(xl, yt, xr - xl, yb - yt, cls="ink-thin", extra=_st(dash="6 5"))
    for i in range(turns):
        x = xl + (i + 0.5) * (xr - xl) / turns
        cv.circle(x, yt, 9, cls="ink")
        cv.dot(x, yt, 3, cls="accent-b")
        cv.circle(x, yb, 9, cls="ink")
        cv.line(x - 6, yb - 6, x + 6, yb + 6, cls="ink-thin")
        cv.line(x - 6, yb + 6, x + 6, yb - 6, cls="ink-thin")
    for k in (-1, 0, 1):
        y = (yt + yb) / 2 + k * 24
        cv.line(xl + 6, y, xr - 6, y, cls="accent-a", extra=_st(width=1.5))
        _head(cv, (xl + xr) / 2, y, 0.0, size=7.5, cls="accent-a")
    cv.text((xl + xr) / 2, yt - 22, "B = μ₀·n·I", cls="lbl", anchor="middle")
    cv.text(xr + 12, (yt + yb) / 2 + 5, "N", cls="lbl")
    cv.text(xl - 12, (yt + yb) / 2 + 5, "S", cls="lbl", anchor="end")
    # Đường sức khép kín bên ngoài: ra ở cực Bắc, vòng về cực Nam.
    for k, spread in ((1, 58.0), (-1, 58.0)):
        ym = (yt + yb) / 2
        cv.path(
            f"M {_n(xr - 6)} {_n(ym)} C {_n(xr + 74)} {_n(ym)},"
            f" {_n(xr + 46)} {_n(ym - k * spread)}, {_n((xl + xr) / 2)} {_n(ym - k * spread)}"
            f" C {_n(xl - 46)} {_n(ym - k * spread)}, {_n(xl - 74)} {_n(ym)}, {_n(xl + 6)} {_n(ym)}",
            cls="accent-a", extra=_st(fill="none", width=1.3))
        _head(cv, (xl + xr) / 2, ym - k * spread, math.pi, size=7, cls="accent-a")
    _dim(cv, xl, yb + 46, xr, yb + 46, "ℓ  (N vòng)")
    cv.text(w / 2, h - 12, "trong lòng ống dây từ trường coi như đều",
            cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 4. Quang hình
# --------------------------------------------------------------------------
def _lens_geometry(f: float, d: float) -> tuple[Optional[float], Optional[float]]:
    """Trả (d', k) theo 1/f = 1/d + 1/d'. ``None`` khi ảnh ở vô cực."""
    if abs(d - f) < 1e-9:
        return None, None
    dp = d * f / (d - f)
    return dp, -dp / d


def build_lens_ray(p: Params) -> str:
    """Dựng ảnh qua thấu kính mỏng bằng ba tia đặc trưng.

    Vị trí và độ cao ảnh TÍNH từ d' = d·f/(d − f) và k = −d'/d chứ không đặt
    tay: cả ba tia ló đều được vẽ hướng qua đúng điểm ảnh đó, nên nếu công thức
    sai thì hình cũng gãy chứ không "trông vẫn ổn".

    f > 0: thấu kính hội tụ. f < 0: thấu kính phân kì (ảnh ảo, nét đứt).
    """
    f = _num(p, "f", 6.0)
    d = _num(p, "d", 15.0)
    w, hgt = 490.0, 310.0
    box = (26.0, 22.0, 438.0, 244.0)
    conv = f > 0
    cv = Canvas(w, hgt,
                title="Dựng ảnh qua thấu kính " + ("hội tụ" if conv else "phân kì"),
                desc="Ba tia đặc trưng qua thấu kính mỏng: tia song song trục "
                     "chính, tia qua quang tâm và tia qua tiêu điểm vật.")

    if abs(f) < 1e-9 or d <= 0:
        fr = _Frame(box, 10.0)
        _seg(cv, box, box[0], fr.Y(0), box[0] + box[2], fr.Y(0), cls="axis")
        cv.text(w / 2, hgt / 2, "tham số không dựng được ảnh (f = 0 hoặc d ≤ 0)",
                cls="lbl-sm", anchor="middle")
        return cv.render()

    dp, k = _lens_geometry(f, d)
    reach = max(d, 2 * abs(f))
    if dp is not None and abs(dp) < 2.4 * reach:
        reach = max(reach, abs(dp))
    fr = _Frame(box, reach * 1.16)
    # Chiều cao vật phải co lại theo |k|: ảnh phóng đại 3 lần mà giữ nguyên h thì
    # đầu mũi tên ảnh rơi ra ngoài khung và người đọc mất hẳn kết quả dựng hình.
    h = _num(p, "h", min(0.30 * reach, 0.80 * fr.half_y / max(abs(k or 1.0), 1.0)))
    hp = k * h if k is not None else None

    ax_y = fr.Y(0)
    _seg(cv, box, box[0], ax_y, box[0] + box[2], ax_y, cls="axis")
    cv.text(box[0] + box[2] - 4, ax_y - 8, "trục chính", cls="lbl-sm", anchor="end")

    # Thấu kính: mũi tên hai đầu hướng RA = hội tụ, hướng VÀO = phân kì.
    lx = fr.X(0)
    half = box[3] / 2 - 8
    cv.line(lx, ax_y - half, lx, ax_y + half, cls="ink", extra=_st(width=2.5))
    if conv:
        _head(cv, lx, ax_y - half, -math.pi / 2, size=9, cls="ink")
        _head(cv, lx, ax_y + half, math.pi / 2, size=9, cls="ink")
    else:
        _head(cv, lx, ax_y - half + 10, math.pi / 2, size=9, cls="ink")
        _head(cv, lx, ax_y + half - 10, -math.pi / 2, size=9, cls="ink")
    cv.dot(lx, ax_y, 3.2, cls="ink")
    cv.text(lx + 6, ax_y + 16, "O", cls="lbl")
    for xf, name in ((-f, "F"), (f, "F′")):
        if fr.inside(xf, 0, margin=2):
            cv.dot(fr.X(xf), ax_y, 3.2, cls="accent-d")
            cv.text(fr.X(xf), ax_y + 20, name, cls="lbl", anchor="middle")

    # Vật AB
    ox, oy = fr.P(-d, 0)
    cv.arrow(ox, oy, *fr.P(-d, h), cls="accent-c", head=9)
    cv.text(fr.X(-d) - 6, fr.Y(h) - 6, "B", cls="lbl", anchor="end")
    cv.text(ox - 6, oy + 16, "A", cls="lbl", anchor="end")

    solid = _st(width=1.9)
    dash = _st(width=1.6, dash="6 4")
    if dp is None:
        # d = f: chùm tia ló song song, ảnh ở vô cực.
        fr.seg(cv, -d, h, 0, h, cls="accent-a", extra=solid)
        fr.ray(cv, 0, h, f, -h, cls="accent-a", extra=solid, arrow_cls="accent-a")
        fr.seg(cv, -d, h, 0, 0, cls="accent-b", extra=solid)
        fr.ray(cv, 0, 0, d, -h, cls="accent-b", extra=solid, arrow_cls="accent-b")
        cv.text(box[0] + box[2] - 6, box[1] + 20, "d = f → ảnh ở vô cực",
                cls="lbl-sm", anchor="end")
        return cv.render()

    sgn = 1.0 if dp > 0 else -1.0
    # Tia 1: song song trục chính, ló đi qua (hoặc có đường kéo dài qua) tiêu điểm ảnh.
    fr.seg(cv, -d, h, 0, h, cls="accent-a", extra=solid)
    fr.ray(cv, 0, h, sgn * dp, sgn * (hp - h), cls="accent-a", extra=solid,
           arrow_cls="accent-a")
    # Tia 2: qua quang tâm, truyền thẳng.
    fr.seg(cv, -d, h, 0, 0, cls="accent-b", extra=solid)
    fr.ray(cv, 0, 0, d, -h, cls="accent-b", extra=solid, arrow_cls="accent-b")
    # Tia 3: qua tiêu điểm vật F(−f, 0) → ló song song trục chính ở độ cao h′.
    fr.seg(cv, -d, h, 0, hp, cls="accent-d", extra=solid)
    fr.ray(cv, 0, hp, 1.0, 0.0, cls="accent-d", extra=solid, arrow_cls="accent-d")
    if (conv and d < f) or not conv:
        fr.seg(cv, -d, h, -f, 0, cls="accent-d", extra=dash)
    if dp < 0:
        # Ảnh ảo: đường kéo dài của tia ló mới cắt nhau, vẽ nét đứt.
        fr.seg(cv, 0, h, dp, hp, cls="accent-a", extra=dash)
        fr.seg(cv, 0, hp, dp, hp, cls="accent-d", extra=dash)

    if fr.inside(dp, 0, margin=2) and fr.inside(dp, hp, margin=2):
        cv.arrow(fr.X(dp), ax_y, *fr.P(dp, hp), cls="accent-c", head=9,
                 extra="" if dp > 0 else _st(dash="6 4"))
        cv.text(fr.X(dp) + 7, fr.Y(hp) + (-6 if hp > 0 else 16), "B′", cls="lbl")
        cv.text(fr.X(dp) + 7, ax_y + 16, "A′", cls="lbl")
    kind = ("ảnh thật, ngược chiều" if dp > 0 else "ảnh ảo, cùng chiều")
    cv.text(box[0] + 2, box[1] + box[3] + 22,
            f"f = {_n(round(f, 2))} · d = {_n(round(d, 2))} · "
            f"d′ = {_n(round(dp, 2))} · k = {_n(round(k, 2))}", cls="lbl-sm")
    cv.text(box[0] + 2, box[1] + box[3] + 38, kind, cls="lbl-sm")
    return cv.render()


def build_mirror_plane(p: Params) -> str:
    """Ảnh qua gương phẳng: ảnh ảo, đối xứng qua mặt gương, d′ = d và h′ = h."""
    w, hgt = 440.0, 300.0
    box = (24.0, 20.0, 392.0, 220.0)
    cv = Canvas(w, hgt, title="Ảnh của vật qua gương phẳng",
                desc="Vật đặt trước gương phẳng cho ảnh ảo, đối xứng với vật qua "
                     "mặt gương, cùng chiều và cùng độ lớn.")
    d = max(abs(_num(p, "d", 4.0)), 0.3)
    fr = _Frame(box, d * 2.5)
    h = _num(p, "h", d * 0.55)
    mx = fr.X(0)
    top, bottom = box[1] + 12, box[1] + box[3] - 12
    cv.line(mx, top, mx, bottom, cls="ink", extra=_st(width=3))
    for i in range(11):
        y = top + i * (bottom - top) / 10
        cv.line(mx, y, mx + 11, y - 11, cls="ink-thin")
    base = fr.Y(0)
    cv.arrow(fr.X(-d), base, *fr.P(-d, h), cls="accent-c", head=9)
    cv.text(fr.X(-d) - 7, fr.Y(h) - 5, "B", cls="lbl", anchor="end")
    cv.text(fr.X(-d) - 7, base + 15, "A", cls="lbl", anchor="end")
    cv.arrow(fr.X(d), base, *fr.P(d, h), cls="accent-c", head=9,
             extra=_st(dash="6 4"))
    cv.text(fr.X(d) + 22, fr.Y(h) - 5, "B′", cls="lbl")
    cv.text(fr.X(d) + 22, base + 15, "A′", cls="lbl")
    # Hai tia phản xạ đều có đường kéo dài đi qua ảnh B′ — đó là toàn bộ lí do
    # mắt "thấy" ảnh nằm sau gương.
    for yh in (h, 0.30 * h):
        fr.seg(cv, -d, h, 0, yh, cls="accent-a", extra=_st(width=1.8))
        fr.ray(cv, 0, yh, -d, yh - h, cls="accent-a", extra=_st(width=1.8),
               arrow_cls="accent-a")
        fr.seg(cv, 0, yh, d, h, cls="accent-a",
               extra=_st(width=1.5, dash="6 4"))
    _dim(cv, fr.X(-d), base + 42, mx, base + 42, "d")
    _dim(cv, mx, base + 42, fr.X(d), base + 42, "d′ = d")
    cv.text(box[0] + 2, box[1] + box[3] + 44,
            "ảnh ảo, cùng chiều, h′ = h, đối xứng với vật qua mặt gương",
            cls="lbl-sm")
    return cv.render()


def build_reflection_law(p: Params) -> str:
    """Định luật phản xạ ánh sáng: góc phản xạ bằng góc tới, đo từ pháp tuyến."""
    i = min(max(_num(p, "i", 40.0), 5.0), 80.0)
    w, hgt = 420.0, 280.0
    cv = Canvas(w, hgt, title="Định luật phản xạ ánh sáng",
                desc="Tia tới, pháp tuyến và tia phản xạ; góc phản xạ bằng góc tới.")
    cx, cy = w / 2, 196.0
    cv.line(60, cy, w - 60, cy, cls="ink", extra=_st(width=3))
    for kk in range(13):
        x = 60 + kk * (w - 120) / 12
        cv.line(x, cy, x - 10, cy + 10, cls="ink-thin")
    cv.line(cx, cy, cx, cy - 150, cls="ink-thin", extra=_st(dash="6 4"))
    cv.text(cx + 6, cy - 152, "N", cls="lbl")
    L = 138.0
    a = math.radians(i)
    sx, sy = cx - L * math.sin(a), cy - L * math.cos(a)
    rx, ry = cx + L * math.sin(a), cy - L * math.cos(a)
    _arrow_at(cv, sx, sy, cx, cy, cls="accent-a", frac=0.62, width=2.2, size=9)
    _arrow_at(cv, cx, cy, rx, ry, cls="accent-b", frac=0.72, width=2.2, size=9)
    cv.text(sx - 6, sy - 6, "S", cls="lbl", anchor="end")
    cv.text(rx + 6, ry - 6, "R", cls="lbl")
    cv.dot(cx, cy, 3.4, cls="accent-c")
    cv.text(cx - 8, cy + 18, "I", cls="lbl", anchor="end")
    _arc(cv, cx, cy, 52, 90, 90 + i, cls="accent-a", width=1.8)
    _arc(cv, cx, cy, 52, 90 - i, 90, cls="accent-b", width=1.8)
    cv.text(cx - 62 * math.sin(a / 2), cy - 62 * math.cos(a / 2) + 4, "i",
            cls="lbl", anchor="middle")
    cv.text(cx + 62 * math.sin(a / 2), cy - 62 * math.cos(a / 2) + 4, "i′",
            cls="lbl", anchor="middle")
    cv.text(w / 2, hgt - 14, f"i′ = i = {_n(round(i, 1))}°  (đo từ pháp tuyến)",
            cls="lbl-sm", anchor="middle")
    return cv.render()


def build_mirror_spherical(p: Params) -> str:
    """Dựng ảnh qua gương cầu: 1/s_o + 1/s_i = 1/f = 2/R, m = −s_i/s_o.

    Mặt phản xạ vẽ đúng cung tròn tâm C bán kính R (lõm: f > 0, C ở trước gương;
    lồi: f < 0, C ở sau gương). Ba tia dựng theo xấp xỉ cận trục — đúng phạm vi
    mà công thức gương cầu có giá trị.
    """
    f = _num(p, "f", 6.0)
    so = _num(p, "so", 12.0)
    w, hgt = 480.0, 310.0
    box = (26.0, 22.0, 428.0, 244.0)
    concave = f > 0
    cv = Canvas(w, hgt, title="Dựng ảnh qua gương cầu " + ("lõm" if concave else "lồi"),
                desc="Gương cầu với tiêu điểm F, tâm C và ba tia dựng ảnh.")
    if abs(f) < 1e-9 or so <= 0:
        cv.text(w / 2, hgt / 2, "tham số không dựng được ảnh (f = 0 hoặc s_o ≤ 0)",
                cls="lbl-sm", anchor="middle")
        return cv.render()
    R = 2 * f
    si, m = _lens_geometry(f, so)          # cùng dạng đại số với thấu kính
    reach = max(so, 2 * abs(f), abs(R))
    if si is not None and abs(si) < 2.4 * reach:
        reach = max(reach, abs(si))
    fr = _Frame(box, reach * 1.16)
    mag = abs(m) if m else 1.0
    h = _num(p, "h", min(0.26 * reach, 0.78 * fr.half_y / max(mag, 1.0)))
    ax_y = fr.Y(0)
    _seg(cv, box, box[0], ax_y, box[0] + box[2], ax_y, cls="axis")

    # Mặt gương: cung tròn tâm C = (−R, 0) bán kính |R| đi qua đỉnh (0, 0).
    half_world = min(fr.half_y * 0.82, abs(R) * 0.9)
    phimax = math.asin(min(1.0, half_world / abs(R)))
    pts = []
    for j in range(37):
        phi = -phimax + 2 * phimax * j / 36
        pts.append(fr.P(-R + R * math.cos(phi), R * math.sin(phi)))
    inside = [q for q in pts
              if box[0] <= q[0] <= box[0] + box[2] and box[1] <= q[1] <= box[1] + box[3]]
    if len(inside) >= 2:
        cv.polyline(inside, cls="ink", extra=_st(width=2.6))
    for xx, nm, cls in ((-R, "C", "accent-d"), (-f, "F", "accent-d")):
        if fr.inside(xx, 0, margin=2):
            cv.dot(fr.X(xx), ax_y, 3.2, cls=cls)
            cv.text(fr.X(xx), ax_y + 20, nm, cls="lbl", anchor="middle")
    cv.text(fr.X(0), ax_y + 20, "V", cls="lbl", anchor="middle")

    cv.arrow(fr.X(-so), ax_y, *fr.P(-so, h), cls="accent-c", head=9)
    cv.text(fr.X(-so) - 6, fr.Y(h) - 6, "B", cls="lbl", anchor="end")
    solid = _st(width=1.9)
    dash = _st(width=1.6, dash="6 4")
    if si is None:
        fr.seg(cv, -so, h, 0, h, cls="accent-a", extra=solid)
        fr.ray(cv, 0, h, -f, -h, cls="accent-a", extra=solid, arrow_cls="accent-a")
        cv.text(box[0] + box[2] - 6, box[1] + 20, "s_o = f → ảnh ở vô cực",
                cls="lbl-sm", anchor="end")
        return cv.render()
    hi = m * h
    # Tia ló của gương luôn quay NGƯỢC lại phía vật (sang trái); ảnh nằm ở
    # hoành độ −s_i, nên hướng tia ló là hướng tới (hoặc rời khỏi) điểm ảnh đó.
    d1 = (-si, hi - h) if si > 0 else (si, h - hi)
    fr.seg(cv, -so, h, 0, h, cls="accent-a", extra=solid)
    fr.ray(cv, 0, h, d1[0], d1[1], cls="accent-a", extra=solid, arrow_cls="accent-a")
    fr.seg(cv, -so, h, 0, 0, cls="accent-b", extra=solid)
    # Tia qua đỉnh V phản xạ đối xứng qua trục chính: đảo dấu thành phần ngang.
    fr.ray(cv, 0, 0, -so, -h, cls="accent-b", extra=solid, arrow_cls="accent-b")
    fr.seg(cv, -so, h, 0, hi, cls="accent-d", extra=solid)
    fr.ray(cv, 0, hi, -1.0, 0.0, cls="accent-d", extra=solid, arrow_cls="accent-d")
    if not (0.0 < f <= so):
        # F nằm ngoài đoạn vật→gương (gương lồi, hoặc vật trong tiêu cự): tia tới
        # chỉ HƯỚNG về F, nên nối bằng nét đứt cho thấy đúng quy tắc dựng.
        fr.seg(cv, -so, h, -f, 0, cls="accent-d", extra=dash)
    if si < 0:
        fr.seg(cv, 0, h, -si, hi, cls="accent-a", extra=dash)
        fr.seg(cv, 0, hi, -si, hi, cls="accent-d", extra=dash)
    if fr.inside(-si, 0, margin=2) and fr.inside(-si, hi, margin=2):
        cv.arrow(fr.X(-si), ax_y, *fr.P(-si, hi), cls="accent-c", head=9,
                 extra="" if si > 0 else _st(dash="6 4"))
        cv.text(fr.X(-si) + 7, fr.Y(hi) + (-6 if hi > 0 else 16), "B′", cls="lbl")
    cv.text(box[0] + 2, box[1] + box[3] + 22,
            f"f = {_n(round(f, 2))} · R = {_n(round(R, 2))} · "
            f"s_o = {_n(round(so, 2))} · s_i = {_n(round(si, 2))} · m = {_n(round(m, 2))}",
            cls="lbl-sm")
    cv.text(box[0] + 2, box[1] + box[3] + 38,
            "ảnh thật, ngược chiều" if si > 0 else "ảnh ảo, cùng chiều", cls="lbl-sm")
    return cv.render()


def build_refraction(p: Params) -> str:
    """Khúc xạ qua mặt phân cách hai môi trường; tự chuyển sang phản xạ toàn phần.

    Góc khúc xạ tính từ chính định luật Snell: sin r = n₁·sin i / n₂. Nếu vế
    phải vượt 1 thì KHÔNG có tia khúc xạ và hình tự vẽ phản xạ toàn phần —
    vẽ sẵn một tia khúc xạ "cho đẹp" trong trường hợp đó là dạy sai.
    """
    n1 = max(_num(p, "n1", 1.0), 0.05)
    n2 = max(_num(p, "n2", 1.5), 0.05)
    i = min(max(_num(p, "i", 45.0), 3.0), 87.0)
    w, hgt = 440.0, 330.0
    cv = Canvas(w, hgt, title="Khúc xạ ánh sáng qua mặt phân cách",
                desc="Tia tới, pháp tuyến, tia phản xạ và tia khúc xạ tại mặt phân "
                     "cách giữa hai môi trường trong suốt.")
    cx, cy = w / 2, 150.0
    cv.rect(40, cy, w - 80, 130, cls="fill-a")
    cv.line(40, cy, w - 40, cy, cls="ink", extra=_st(width=2.5))
    cv.line(cx, cy - 118, cx, cy + 118, cls="ink-thin", extra=_st(dash="6 4"))
    cv.text(cx + 6, cy - 120, "N", cls="lbl")
    cv.text(48, cy - 12, f"n₁ = {_n(round(n1, 3))}", cls="lbl-sm")
    cv.text(48, cy + 22, f"n₂ = {_n(round(n2, 3))}", cls="lbl-sm")
    L = 118.0
    a = math.radians(i)
    sx, sy = cx - L * math.sin(a), cy - L * math.cos(a)
    _arrow_at(cv, sx, sy, cx, cy, cls="accent-a", frac=0.62, width=2.2, size=9)
    cv.text(sx - 6, sy - 4, "S", cls="lbl", anchor="end")
    cv.dot(cx, cy, 3.4, cls="accent-c")
    _arc(cv, cx, cy, 46, 90, 90 + i, cls="accent-a", width=1.8)
    cv.text(cx - 56 * math.sin(a / 2), cy - 56 * math.cos(a / 2) + 4, "i",
            cls="lbl", anchor="middle")
    s_r = n1 * math.sin(a) / n2
    if s_r <= 1.0:
        r = math.asin(s_r)
        rx, ry = cx + L * math.sin(r), cy + L * math.cos(r)
        _arrow_at(cv, cx, cy, rx, ry, cls="accent-b", frac=0.74, width=2.2, size=9)
        cv.text(rx + 6, ry + 10, "R", cls="lbl")
        # Tia khúc xạ đi xuống-PHẢI, nên cung góc r nằm bên phải pháp tuyến dưới
        # (270°); vẽ về phía 270° − r là lật hình sang nhánh không có tia nào.
        _arc(cv, cx, cy, 46, 270, 270 + math.degrees(r),
             cls="accent-b", width=1.8)
        cv.text(cx + 56 * math.sin(r / 2), cy + 56 * math.cos(r / 2) + 4, "r",
                cls="lbl", anchor="middle")
        # Tia phản xạ một phần luôn tồn tại, vẽ mảnh để không tranh chỗ tia chính.
        _arrow_at(cv, cx, cy, cx + L * 0.72 * math.sin(a), cy - L * 0.72 * math.cos(a),
                  cls="accent-d", frac=0.85, width=1.4, size=7, dash="5 4")
        note = (f"n₁·sin i = n₂·sin r → r = {_n(round(math.degrees(r), 1))}°"
                + ("   (đi vào môi trường chiết quang hơn: r < i)" if n2 > n1
                   else "   (đi ra môi trường chiết quang kém: r > i)"))
    else:
        _arrow_at(cv, cx, cy, cx + L * math.sin(a), cy - L * math.cos(a),
                  cls="accent-b", frac=0.74, width=2.4, size=9)
        cv.text(cx + L * math.sin(a) + 6, cy - L * math.cos(a) - 4, "R", cls="lbl")
        _arc(cv, cx, cy, 46, 90 - i, 90, cls="accent-b",
             width=1.8)
        cv.text(cx + 56 * math.sin(a / 2), cy - 56 * math.cos(a / 2) + 4, "i′",
                cls="lbl", anchor="middle")
        igh = math.degrees(math.asin(min(1.0, n2 / n1)))
        ag = math.radians(igh)
        cv.line(cx, cy, cx - L * math.sin(ag), cy - L * math.cos(ag),
                cls="ink-thin", extra=_st(dash="5 4"))
        cv.text(cx - L * math.sin(ag) - 4, cy - L * math.cos(ag) - 6,
                f"i_gh = {_n(round(igh, 1))}°", cls="lbl-sm", anchor="end")
        note = f"i ≥ i_gh → phản xạ toàn phần, không có tia khúc xạ"
    cv.text(w / 2, hgt - 14, note, cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 5. Nhiệt học
# --------------------------------------------------------------------------
# Số mũ đa biến/đoạn nhiệt thực tế nằm trong [1; 2]. Kẹp lại vì ``2.0 ** 1e9``
# ném OverflowError ngay khi tính hằng số, trước cả khi ``sample_curve`` kịp
# bắt lỗi — và một tham số vô lí không được phép làm hỏng cả trang.
_EXPO_MIN, _EXPO_MAX = 0.05, 8.0


def _pv_curve(p1: float, v1: float, v2: float, expo: float) -> list[tuple[float, float]]:
    """Lấy mẫu đường ``pV^expo = const`` qua ``mathexpr.sample_curve``.

    Dùng bộ lấy mẫu chung thay vì tự lặp để mọi đường cong trong kho đều bỏ
    điểm không xác định theo cùng một quy tắc (V ≤ 0, luỹ thừa tràn số).
    """
    expo = min(max(expo, _EXPO_MIN), _EXPO_MAX)
    try:
        const = p1 * (v1 ** expo)
    except (OverflowError, ValueError):
        return []
    if not math.isfinite(const):
        return []
    return sample_curve(f"{const!r}/x**{expo!r}", "x", v1, v2, 60)


def _pv_points(kind: str, v1: float, v2: float, p1: float, gamma: float,
               n_poly: float) -> list[tuple[float, float]]:
    """Các điểm của một quá trình cơ bản trên giản đồ p-V."""
    if kind == "isobaric":
        return [(v1, p1), (v2, p1)]
    if kind == "isochoric":
        return [(v1, p1), (v1, p1 * 0.35)]
    expo = {"isothermal": 1.0, "adiabatic": gamma, "polytropic": n_poly}.get(kind, 1.0)
    return _pv_curve(p1, v1, v2, expo)


def build_pv_diagram(p: Params) -> str:
    """Giản đồ p-V cho một quá trình của khí lí tưởng, tuỳ chọn tô phần công.

    ``process``: isothermal | isobaric | isochoric | adiabatic | polytropic |
    all | cycle. Diện tích dưới đường quá trình chính là công khí sinh ra, nên
    khi ``work`` bật thì miền tô luôn giới hạn bởi ĐÚNG đường vừa vẽ.
    """
    kind = str(p.get("process") or "isothermal")
    work = bool(p.get("work", False))
    gamma = _num(p, "gamma", 1.4)
    n_poly = _num(p, "n", 1.2)
    v1 = max(_num(p, "V1", 1.0), 0.05)
    v2 = max(_num(p, "V2", 3.2), v1 + 0.05)
    p1 = max(_num(p, "p1", 4.0), 0.05)

    w, hgt = 420.0, 320.0
    box = (58.0, 30.0, 300.0, 216.0)
    names = {"isothermal": "đẳng nhiệt (T = const)", "isobaric": "đẳng áp (p = const)",
             "isochoric": "đẳng tích (V = const)", "adiabatic": "đoạn nhiệt (pVᵞ = const)",
             "polytropic": "đa biến (pVⁿ = const)", "all": "bốn quá trình cơ bản",
             "cycle": "chu trình kín"}
    cv = Canvas(w, hgt, title="Giản đồ p - V: " + names.get(kind, kind),
                desc="Giản đồ áp suất - thể tích của khí lí tưởng.")
    ax = _Axes(box, v2 * 1.3, p1 * 1.3)
    ax.frame(cv, "V", "p")

    if kind == "cycle":
        p2 = p1 * 0.4
        poly = [(v1, p1), (v2, p1), (v2, p2), (v1, p2)]
        cv.polygon([ax.P(*q) for q in poly] , cls="fill-a")
        cv.polyline([ax.P(*q) for q in poly] + [ax.P(*poly[0])], cls="curve")
        for j, q in enumerate(poly):
            cv.dot(*ax.P(*q), r=3.4, cls="accent-b")
            cv.text(ax.X(q[0]) + (8 if j in (1, 2) else -8), ax.Y(q[1]) - 8,
                    str(j + 1), cls="lbl", anchor="start" if j in (1, 2) else "end")
        cv.text(ax.X((v1 + v2) / 2), ax.Y((p1 + p2) / 2) + 5,
                "W = diện tích", cls="lbl-sm", anchor="middle")
        cv.text(box[0], box[1] + box[3] + 46,
                "công của chu trình bằng diện tích hình kín trên giản đồ p-V",
                cls="lbl-sm")
        return cv.render()

    if kind == "all":
        for k, cls, lab in (("isothermal", "accent-a", "đẳng nhiệt"),
                            ("adiabatic", "accent-b", "đoạn nhiệt"),
                            ("isobaric", "accent-c", "đẳng áp"),
                            ("isochoric", "accent-d", "đẳng tích")):
            pts = _pv_points(k, v1, v2, p1, gamma, n_poly)
            ax.curve(cv, pts, cls=cls, width=2.2)
            if pts:
                ex, ey = pts[-1]
                cv.text(min(ax.X(ex) + 6, box[0] + box[2] + 4),
                        max(ax.Y(ey) + 4, box[1] + 10), lab, cls="lbl-sm")
        cv.dot(*ax.P(v1, p1), r=3.6, cls="accent-b")
        cv.text(ax.X(v1) - 8, ax.Y(p1) - 6, "1", cls="lbl", anchor="end")
        cv.text(box[0], box[1] + box[3] + 46,
                "cùng xuất phát từ trạng thái 1: đoạn nhiệt dốc hơn đẳng nhiệt",
                cls="lbl-sm")
        return cv.render()

    pts = _pv_points(kind, v1, v2, p1, gamma, n_poly)
    if work and len(pts) >= 2 and kind != "isochoric":
        poly = [ax.P(pts[0][0], 0.0)] + [ax.P(x, y) for x, y in pts
                                         if 0 <= x <= ax.xmax and 0 <= y <= ax.ymax]
        poly.append(ax.P(pts[-1][0], 0.0))
        cv.polygon(poly, cls="fill-a")
        cv.text(ax.X((pts[0][0] + pts[-1][0]) / 2), box[1] + box[3] - 22,
                "A′ = ∫p dV", cls="lbl-sm", anchor="middle")
    ax.curve(cv, pts, cls="curve")
    # Chỉ đánh dấu trạng thái NẰM TRONG khung. Với số mũ đa biến vô lí, p₂ có
    # thể vọt lên hàng trăm lần p₁ và chấm trạng thái 2 rơi ra ngoài viewBox —
    # đúng kiểu lỗi im lặng mà nhìn ảnh không thấy.
    inside = [q for q in pts if 0 <= q[0] <= ax.xmax and 0 <= q[1] <= ax.ymax]
    if inside:
        for q, name, anchor in ((inside[0], "1", "end"), (inside[-1], "2", "start")):
            cv.dot(*ax.P(*q), r=3.6, cls="accent-b")
            cv.text(ax.X(q[0]) + (8 if anchor == "start" else -8), ax.Y(q[1]) - 8,
                    name, cls="lbl", anchor=anchor)
        mid = inside[len(inside) // 2]
        _head(cv, *ax.P(*mid), math.atan2(ax.Y(inside[-1][1]) - ax.Y(inside[0][1]),
                                          ax.X(inside[-1][0]) - ax.X(inside[0][0])),
              size=7.5, cls="accent-b")
    cv.text(box[0], box[1] + box[3] + 46,
            str(p.get("caption") or names.get(kind, kind)), cls="lbl-sm")
    return cv.render()


def build_carnot_cycle(p: Params) -> str:
    """Chu trình Carnot trên giản đồ p-V: hai đẳng nhiệt xen hai đoạn nhiệt.

    Bốn trạng thái tính từ chính T₁, T₂ và γ (đoạn nhiệt: T·V^(γ−1) = const),
    nên tỉ số nén giãn trên hình luôn khớp với η = 1 − T₂/T₁ ghi ở chú thích.
    """
    gamma = min(max(_num(p, "gamma", 1.4), 1.02), _EXPO_MAX)
    th = max(_num(p, "T1", 4.0), 0.2)
    tc = _num(p, "T2", 2.8)
    tc = min(max(tc, 0.05), th * 0.98)
    v1 = max(_num(p, "V1", 1.0), 0.05)
    v2 = max(_num(p, "V2", 2.0), v1 * 1.05)

    ratio = (th / tc) ** (1.0 / (gamma - 1.0))
    ratio = min(ratio, 6.0)                       # giữ hình trong khung khi T₂ rất nhỏ
    v3, v4 = v2 * ratio, v1 * ratio
    states = [(v1, th / v1), (v2, th / v2), (v3, tc / v3), (v4, tc / v4)]

    w, hgt = 430.0, 330.0
    box = (58.0, 30.0, 312.0, 222.0)
    cv = Canvas(w, hgt, title="Chu trình Carnot",
                desc="Chu trình Carnot gồm hai quá trình đẳng nhiệt và hai quá "
                     "trình đoạn nhiệt trên giản đồ p - V.")
    ax = _Axes(box, v3 * 1.18, states[0][1] * 1.22)
    ax.frame(cv, "V", "p")

    legs = [_pv_curve(states[0][1], states[0][0], states[1][0], 1.0),
            _pv_curve(states[1][1], states[1][0], states[2][0], gamma),
            _pv_curve(states[2][1], states[2][0], states[3][0], 1.0),
            _pv_curve(states[3][1], states[3][0], states[0][0], gamma)]
    ring: list[tuple[float, float]] = []
    for seg in legs:
        ring.extend(seg)
    if len(ring) >= 3:
        cv.polygon([ax.P(x, y) for x, y in ring
                    if 0 <= x <= ax.xmax and 0 <= y <= ax.ymax], cls="fill-a")
    for seg, cls in zip(legs, ("accent-b", "accent-d", "accent-a", "accent-d")):
        ax.curve(cv, seg, cls=cls, width=2.4)
    for j, st in enumerate(states):
        if not (0 <= st[0] <= ax.xmax and 0 <= st[1] <= ax.ymax):
            continue                       # γ vô lí có thể đẩy trạng thái ra ngoài khung
        cv.dot(*ax.P(*st), r=3.6, cls="accent-b")
        cv.text(ax.X(st[0]) + (-9 if j in (0, 3) else 9), ax.Y(st[1]) - 8,
                str(j + 1), cls="lbl", anchor="end" if j in (0, 3) else "start")
    for vm, tm, dy, lab in ((( v1 + v2) / 2, th, -12, "T₁ (nhận Q₁)"),
                            ((v3 + v4) / 2, tc, 18, "T₂ (nhả Q₂)")):
        if 0 <= vm <= ax.xmax and 0 <= tm / vm <= ax.ymax:
            cv.text(ax.X(vm) + (16 if dy < 0 else 0), ax.Y(tm / vm) + dy, lab,
                    cls="lbl-sm", anchor="start" if dy < 0 else "middle")
    cv.text(box[0], box[1] + box[3] + 46,
            f"1→2, 3→4 đẳng nhiệt;  2→3, 4→1 đoạn nhiệt", cls="lbl-sm")
    cv.text(box[0], box[1] + box[3] + 62,
            f"η = 1 − T₂/T₁ = {_n(round(1 - tc / th, 3))}", cls="lbl-sm")
    return cv.render()


def build_heat_engine(p: Params) -> str:
    """Sơ đồ dòng năng lượng của động cơ nhiệt (hoặc máy lạnh khi ``mode='fridge'``).

    Máy lạnh KHÔNG phải động cơ nhiệt vẽ ngược nhãn: cả ba mũi tên đều đổi
    chiều, vì công là thứ được đưa VÀO chứ không lấy ra.
    """
    fridge = str(p.get("mode") or "engine") == "fridge"
    w, hgt = 380.0, 330.0
    cv = Canvas(w, hgt,
                title="Máy lạnh / bơm nhiệt" if fridge else "Động cơ nhiệt",
                desc="Sơ đồ trao đổi nhiệt giữa nguồn nóng, tác nhân và nguồn lạnh.")
    cx = 150.0
    cv.rect(cx - 108, 26, 216, 44, cls="fill-b")
    cv.rect(cx - 108, 26, 216, 44, cls="ink")
    cv.text(cx, 54, "nguồn nóng  T₁", cls="lbl-sm", anchor="middle")
    cv.rect(cx - 108, 250, 216, 44, cls="fill-a")
    cv.rect(cx - 108, 250, 216, 44, cls="ink")
    cv.text(cx, 278, "nguồn lạnh  T₂", cls="lbl-sm", anchor="middle")
    cv.circle(cx, 160, 44, cls="ink")
    cv.text(cx, 165, "máy lạnh" if fridge else "động cơ", cls="lbl-sm", anchor="middle")
    if fridge:
        _arrow_at(cv, cx, 116, cx, 74, cls="accent-b", width=2.6, size=10)
        _arrow_at(cv, cx, 246, cx, 206, cls="accent-a", width=2.6, size=10)
        _arrow_at(cv, w - 26, 160, cx + 46, 160, cls="accent-c", width=2.6, size=10)
        cv.text(cx + 10, 96, "Q₁ (nhả ra)", cls="lbl-sm")
        cv.text(cx + 10, 232, "Q₂ (lấy đi)", cls="lbl-sm")
        cv.text(w - 30, 150, "A (tiêu thụ)", cls="lbl-sm", anchor="end")
        foot = "ε = Q₂ / A  (máy lạnh)   ·   ε_bơm = Q₁ / A"
    else:
        _arrow_at(cv, cx, 74, cx, 114, cls="accent-b", width=2.6, size=10)
        _arrow_at(cv, cx, 206, cx, 246, cls="accent-a", width=2.6, size=10)
        _arrow_at(cv, cx + 46, 160, w - 26, 160, cls="accent-c", width=2.6, size=10)
        cv.text(cx + 10, 96, "Q₁ (nhận)", cls="lbl-sm")
        cv.text(cx + 10, 232, "Q₂ (nhả)", cls="lbl-sm")
        cv.text(w - 30, 150, "A′ (sinh công)", cls="lbl-sm", anchor="end")
        foot = "H = A′ / Q₁ = 1 − |Q₂| / Q₁"
    cv.text(w / 2, hgt - 12, foot, cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 6. Hạt nhân
# --------------------------------------------------------------------------
def build_decay_curve(p: Params) -> str:
    """Đường phân rã phóng xạ N = N₀·2^(−t/T), có vạch mốc tại T, 2T, 3T.

    Vẽ theo trục t/T nên hình đúng cho MỌI chu kì bán rã — không cần bịa một
    giá trị T cụ thể rồi ghi đơn vị năm hay giây cho một công thức tổng quát.
    """
    cycles = min(max(_num(p, "cycles", 4.0), 1.0), 8.0)
    daughter = bool(p.get("daughter", False))
    # Số hạt nhân N, khối lượng m và độ phóng xạ H giảm theo CÙNG một quy luật,
    # nhưng nhãn trục phải mang đúng ký hiệu của công thức đang minh hoạ: vẽ
    # "N/N₀" cạnh công thức về độ phóng xạ là đổi tên đại lượng cho người học.
    q = str(p.get("quantity") or "N")
    if q not in ("N", "m", "H"):
        q = "N"
    w, hgt = 420.0, 310.0
    box = (58.0, 28.0, 300.0, 208.0)
    cv = Canvas(w, hgt, title="Định luật phóng xạ",
                desc="Đồ thị đại lượng đặc trưng cho lượng chất phóng xạ theo thời "
                     "gian, giảm một nửa sau mỗi chu kì bán rã.")
    ax = _Axes(box, cycles * 1.08, 1.12)
    ax.frame(cv, "t / T", f"{q} / {q}₀")
    pts = sample_curve("2**(-x)", "x", 0.0, cycles, 120)
    if daughter:
        ax.curve(cv, [(x, 1 - y) for x, y in pts], cls="accent-c", width=2.2)
        cv.text(ax.X(cycles * 0.62), ax.Y(1 - 2 ** (-cycles * 0.62)) - 10,
                "hạt nhân con", cls="lbl-sm")
    ax.curve(cv, pts, cls="curve")
    kmax = int(cycles)
    for kk in range(1, kmax + 1):
        yv = 2.0 ** (-kk)
        cv.line(ax.X(kk), ax.Y(0), ax.X(kk), ax.Y(yv), cls="grid",
                extra=_st(dash="4 4"))
        cv.line(ax.X(0), ax.Y(yv), ax.X(kk), ax.Y(yv), cls="grid",
                extra=_st(dash="4 4"))
        cv.dot(ax.X(kk), ax.Y(yv), 3.4, cls="accent-b")
        cv.text(ax.X(kk), ax.Y(0) + 17, f"{kk}T", cls="lbl-sm", anchor="middle")
        cv.text(ax.X(0) - 6, ax.Y(yv) + 4, f"1/{2 ** kk}", cls="lbl-sm", anchor="end")
    cv.text(box[0], box[1] + box[3] + 48,
            f"{q} = {q}₀·2^(−t/T) = {q}₀·e^(−λt),  λ = ln2 / T", cls="lbl-sm")
    if daughter:
        cv.text(box[0], box[1] + box[3] + 64,
                "đường trên: số hạt nhân con đã tạo thành, ΔN = N₀(1 − 2^(−t/T))",
                cls="lbl-sm")
    return cv.render()


def _nuclide_w(a: str, z: str, sym: str) -> float:
    """Bề rộng ước lượng của một ký hiệu hạt nhân (px), để căn giữa phương trình."""
    return max(len(a), len(z)) * 6.8 + len(sym) * 9.2 + 10.0


def _nuclide(cv: Canvas, x: float, y: float, a: str, z: str, sym: str) -> float:
    """Đặt ký hiệu hạt nhân với A phía trên, Z phía dưới, ký hiệu nguyên tố ở giữa.

    Xếp bằng ba phần tử ``text`` thay vì một chuỗi Unicode có chỉ số trên/dưới:
    ``ᴬ`` và ``₋₂`` không có đủ trong mọi font, và một phương trình phân rã hiển
    thị sai chỉ số là sai hẳn về vật lí chứ không chỉ xấu.
    """
    idx = max(len(a), len(z)) * 6.8
    cv.text(x + idx, y - 7, a, cls="lbl-sm", anchor="end")
    cv.text(x + idx, y + 10, z, cls="lbl-sm", anchor="end")
    cv.text(x + idx + 3, y + 5, sym, cls="lbl")
    return x + _nuclide_w(a, z, sym)


def _reaction(cv: Canvas, cx: float, y: float, parts: Sequence[tuple]) -> None:
    """Xếp một phương trình hạt nhân căn giữa quanh ``cx``.

    ``parts``: ``("n", A, Z, sym)`` cho hạt nhân, ``("t", chuỗi)`` cho toán tử.
    """
    total = 0.0
    for it in parts:
        total += _nuclide_w(it[1], it[2], it[3]) if it[0] == "n" else len(it[1]) * 6.8 + 12
    x = cx - total / 2
    for it in parts:
        if it[0] == "n":
            x = _nuclide(cv, x, y, it[1], it[2], it[3])
        else:
            cv.text(x + 6, y + 5, it[1], cls="lbl-sm")
            x += len(it[1]) * 6.8 + 12


def build_decay_scheme(p: Params) -> str:
    """Sơ đồ phân rã: α, β⁻, β⁺ trên lưới (Z, N), hoặc γ trên giản đồ mức năng lượng.

    Bước dịch chuyển lấy đúng theo định luật bảo toàn số khối và điện tích:
    α: (Z−2, N−2);  β⁻: (Z+1, N−1);  β⁺: (Z−1, N+1).
    """
    kind = str(p.get("kind") or "alpha")
    w, hgt = 400.0, 320.0
    if kind == "gamma":
        cv = Canvas(w, hgt, title="Phóng xạ gamma",
                    desc="Hạt nhân ở trạng thái kích thích chuyển về mức thấp hơn "
                         "và phát ra photon gamma.")
        x0, x1 = 90.0, 310.0
        y_hi, y_lo = 96.0, 216.0
        cv.line(x0, y_hi, x1, y_hi, cls="ink", extra=_st(width=2.6))
        cv.line(x0, y_lo, x1, y_lo, cls="ink", extra=_st(width=2.6))
        cv.text(x1 + 6, y_hi + 5, "E_cao", cls="lbl")
        cv.text(x1 + 6, y_lo + 5, "E_thấp", cls="lbl")
        _nuclide(cv, x0 - 46, y_hi - 16, "A", "Z", "X*")
        _nuclide(cv, x0 - 46, y_lo + 26, "A", "Z", "X")
        _arrow_at(cv, (x0 + x1) / 2, y_hi + 4, (x0 + x1) / 2, y_lo - 4,
                  cls="accent-b", width=2.4, size=9)
        cv.text((x0 + x1) / 2 + 10, (y_hi + y_lo) / 2, "γ", cls="lbl")
        cv.text(w / 2, hgt - 40, "ε_γ = E_cao − E_thấp", cls="lbl", anchor="middle")
        cv.text(w / 2, hgt - 18,
                "số khối A và số proton Z không đổi", cls="lbl-sm", anchor="middle")
        return cv.render()

    steps = {"alpha": (-2, -2, "α  (⁴₂He)", "accent-b"),
             "beta-": (1, -1, "β⁻  (electron)", "accent-c"),
             "beta+": (-1, 1, "β⁺  (pozitron)", "accent-d")}
    dz, dn, plabel, cls = steps.get(kind, steps["alpha"])
    cv = Canvas(w, hgt, title="Sơ đồ phóng xạ " + plabel.split()[0],
                desc="Vị trí hạt nhân mẹ và hạt nhân con trên lưới số proton Z - "
                     "số nơtron N.")
    cell = 40.0
    ncol, nrow = 6, 5
    zc, nc = 3, 3           # ô của hạt nhân mẹ; chọn giữa lưới để mọi kiểu
    gx0, gy0 = 66.0, 236.0  # phân rã (±2 ô theo Z và N) đều còn nằm trong lưới
    for c in range(ncol + 1):
        cv.line(gx0 + c * cell, gy0, gx0 + c * cell, gy0 - nrow * cell, cls="grid")
    for r in range(nrow + 1):
        cv.line(gx0, gy0 - r * cell, gx0 + ncol * cell, gy0 - r * cell, cls="grid")
    cv.arrow(gx0, gy0, gx0 + ncol * cell + 14, gy0, cls="axis", head=7)
    cv.arrow(gx0, gy0, gx0, gy0 - nrow * cell - 14, cls="axis", head=7)
    cv.text(gx0 + ncol * cell + 12, gy0 + 18, "Z", cls="lbl", anchor="end")
    cv.text(gx0 + 8, gy0 - nrow * cell - 8, "N", cls="lbl")

    def cellpt(zz, nn):
        return (gx0 + zz * cell, gy0 - nn * cell)

    px, py = cellpt(zc, nc)
    qx, qy = cellpt(zc + dz, nc + dn)
    cv.circle(px, py, 15, cls="fill-b")
    cv.circle(px, py, 15, cls="ink")
    cv.circle(qx, qy, 15, cls="fill-c")
    cv.circle(qx, qy, 15, cls="ink")
    cv.text(px, py + 5, "X", cls="lbl", anchor="middle")
    cv.text(qx, qy + 5, "Y", cls="lbl", anchor="middle")
    # Nhãn đặt theo hướng mũi tên phân rã: mỗi kiểu phóng xạ đi một hướng khác
    # nhau nên toạ độ cố định sẽ đè lên chính mũi tên ở hai trong ba trường hợp.
    ang = math.atan2(qy - py, qx - px)
    ux, uy = math.cos(ang), math.sin(ang)
    cv.text(px - 26 * ux, py - 26 * uy + 4, "mẹ", cls="lbl-sm", anchor="middle")
    cv.text(qx + 26 * ux, qy + 26 * uy + 4, "con", cls="lbl-sm", anchor="middle")
    _arrow_at(cv, px + 16 * ux, py + 16 * uy, qx - 16 * ux, qy - 16 * uy,
              cls=cls, width=2.4, size=9)
    cv.text((px + qx) / 2 - 16 * uy, (py + qy) / 2 + 16 * ux + 4, plabel,
            cls="lbl-sm", anchor="start" if uy <= 0 else "end")
    eq = {
        "alpha": [("n", "A", "Z", "X"), ("t", "→"), ("n", "4", "2", "He"),
                  ("t", "+"), ("n", "A−4", "Z−2", "Y")],
        "beta-": [("n", "A", "Z", "X"), ("t", "→"), ("n", "0", "−1", "e"),
                  ("t", "+"), ("n", "A", "Z+1", "Y"), ("t", "+ phản nơtrinô")],
        "beta+": [("n", "A", "Z", "X"), ("t", "→"), ("n", "0", "+1", "e"),
                  ("t", "+"), ("n", "A", "Z−1", "Y"), ("t", "+ nơtrinô")],
    }[kind if kind in steps else "alpha"]
    _reaction(cv, w / 2, hgt - 46, eq)
    cv.text(w / 2, hgt - 14, f"ΔZ = {dz:+d},  ΔN = {dn:+d}", cls="lbl-sm", anchor="middle")
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "circuit_series": build_circuit_series,
    "circuit_parallel": build_circuit_parallel,
    "circuit_emf": build_circuit_emf,
    "circuit_rlc": build_circuit_rlc,
    "phasor_rlc": build_phasor_rlc,
    "field_point_charge": build_field_point_charge,
    "coulomb_two_charges": build_coulomb_two_charges,
    "field_parallel_plates": build_field_parallel_plates,
    "field_wire": build_field_wire,
    "field_loop": build_field_loop,
    "field_solenoid": build_field_solenoid,
    "lens_ray": build_lens_ray,
    "mirror_plane": build_mirror_plane,
    "reflection_law": build_reflection_law,
    "mirror_spherical": build_mirror_spherical,
    "refraction": build_refraction,
    "pv_diagram": build_pv_diagram,
    "carnot_cycle": build_carnot_cycle,
    "heat_engine": build_heat_engine,
    "decay_curve": build_decay_curve,
    "decay_scheme": build_decay_scheme,
}
