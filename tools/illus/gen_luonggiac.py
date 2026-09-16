"""Minh hoạ họ **lượng giác**: đường tròn lượng giác, đồ thị hàm lượng giác,
giải tam giác, vectơ phẳng và số phức.

Bốn mảng này nằm chung một file vì cùng sống trên mặt phẳng toạ độ và dùng lại
đúng một bộ helper: ``_fit`` (tính khung từ hộp bao điểm thật), ``_angle_at``
(vẽ cung góc tại một đỉnh) và ``_stroke`` (ép ``fill:none`` cho nét màu).

Hai quy ước chống lỗi câm, áp cho mọi generator ở đây:

* Tham số đi qua ``_f``/``_clamp`` TRƯỚC khi thành toạ độ. Kho công thức gộp từ
  nhiều nguồn; một góc 0° hay một cạnh âm lọt vào chỉ làm hình méo chứ không ném
  lỗi, nghĩa là người phát hiện sau cùng lại chính là người học.
* Khung vẽ tính ngược từ hộp bao của các điểm đã dựng (``_fit``) chứ không đặt
  cứng, nên hình không tràn khỏi ``viewBox`` khi tham số đổi.

Lưu ý kỹ thuật dễ sập bẫy: lớp ``.accent-*`` đặt CẢ ``stroke`` lẫn ``fill``, mà
thuộc tính trình bày ``fill="none"`` lại thua CSS trong ``<style>``. Vì vậy mọi
``polyline``/``path`` màu phải ép ``style="fill:none"`` — dùng ``_stroke``.
"""

from __future__ import annotations

import math
from typing import Callable, Optional, Sequence

from .mathexpr import sample_curve
from .svgkit import Canvas, _n

Params = dict
Pt = tuple[float, float]


# --------------------------------------------------------------------------
# tiện ích chung
# --------------------------------------------------------------------------
def _f(v, default: float) -> float:
    """Ép về float; None/chuỗi lạ/nan/inf đều rơi về mặc định thay vì làm vỡ hình."""
    try:
        x = float(v)
    except (TypeError, ValueError):
        return float(default)
    return x if math.isfinite(x) else float(default)


def _clamp(v: float, lo: float, hi: float) -> float:
    return lo if v < lo else (hi if v > hi else v)


def _num(v: float, nd: int = 2) -> str:
    """Số cho nhãn: bỏ đuôi 0 và dùng dấu trừ toán học (U+2212) cho dễ đọc."""
    s = f"{float(v):.{nd}f}".rstrip("0").rstrip(".")
    if s in ("-0", "", "-"):
        s = "0"
    return s.replace("-", "−")


def _stroke(width: float = 2.0, dash: str = "") -> str:
    """Thuộc tính nét cho hình dùng lớp ``accent-*``.

    Phải ép ``fill`` bằng inline style: lớp CSS đặt ``fill`` nên thuộc tính
    ``fill="none"`` của svgkit bị thua, cung tròn sẽ bị tô đặc thành hình quạt.
    """
    out = f' style="fill:none" stroke-width="{_n(width)}"'
    if dash:
        out += f' stroke-dasharray="{dash}"'
    return out


def _arc_pts(cx: float, cy: float, r: float, a1: float, a2: float, n: int = 40) -> list[Pt]:
    """Điểm trên cung tròn; góc tính bằng độ theo hệ toán (ngược chiều kim đồng hồ).

    Trả về polyline chứ không phải lệnh ``A`` của SVG: hai cờ large-arc/sweep rất
    dễ đặt sai khi góc đổi dấu, mà sai thì cung vòng ngược nửa đường tròn.
    """
    n = max(2, int(n))
    out: list[Pt] = []
    for i in range(n + 1):
        a = math.radians(a1 + (a2 - a1) * i / n)
        out.append((cx + r * math.cos(a), cy - r * math.sin(a)))
    return out


def _pol(cx: float, cy: float, r: float, deg: float) -> Pt:
    """Điểm cực -> màn hình (trục y lật)."""
    a = math.radians(deg)
    return (cx + r * math.cos(a), cy - r * math.sin(a))


def _angle_at(cv: Canvas, V: Pt, P1: Pt, P2: Pt, r: float = 26.0,
              cls: str = "accent-d", label: str = "", lcls: str = "lbl",
              lgap: float = 15.0) -> None:
    """Cung đánh dấu góc tại đỉnh ``V`` giữa hai tia ``V→P1`` và ``V→P2``."""
    a1 = math.degrees(math.atan2(-(P1[1] - V[1]), P1[0] - V[0]))
    a2 = math.degrees(math.atan2(-(P2[1] - V[1]), P2[0] - V[0]))
    # Đưa a2 về cùng phía a1 để cung quét đúng góc trong, không vòng ra ngoài.
    while a2 - a1 > 180:
        a2 -= 360
    while a2 - a1 < -180:
        a2 += 360
    cv.polyline(_arc_pts(V[0], V[1], r, a1, a2, 24), cls=cls, extra=_stroke(2))
    if label:
        am = math.radians((a1 + a2) / 2)
        cv.text(V[0] + (r + lgap) * math.cos(am), V[1] - (r + lgap) * math.sin(am) + 5,
                label, cls=lcls, anchor="middle")


def _right_angle_at(cv: Canvas, V: Pt, P1: Pt, P2: Pt, size: float = 12.0) -> None:
    cv.right_angle(V[0], V[1], P1[0], P1[1], P2[0], P2[1], size=size)


def _fit(world: Sequence[Pt], scale: float, pad_l: float, pad_r: float,
         pad_t: float, pad_b: float) -> tuple[float, float, Callable[[float, float], Pt]]:
    """Khung vừa khít hộp bao ``world`` (hệ toán, y hướng lên).

    Trả ``(w, h, P)`` với ``P(x, y)`` đổi toạ độ thế giới sang màn hình.
    """
    xs = [p[0] for p in world] or [0.0]
    ys = [p[1] for p in world] or [0.0]
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)
    w = (maxx - minx) * scale + pad_l + pad_r
    h = (maxy - miny) * scale + pad_t + pad_b
    ox = pad_l - minx * scale
    oy = pad_t + maxy * scale

    def P(x: float, y: float) -> Pt:
        return (ox + x * scale, oy - y * scale)

    return w, h, P


def _axes(cv: Canvas, P: Callable[[float, float], Pt], xlo: float, xhi: float,
          ylo: float, yhi: float, xlabel: str = "x", ylabel: str = "y",
          unit_ticks: bool = False) -> None:
    """Hệ trục Oxy đi qua gốc, kèm mũi tên và (tuỳ chọn) vạch đơn vị."""
    x1, y0 = P(xlo, 0)
    x2, _ = P(xhi, 0)
    xc, ya = P(0, ylo)
    _, yb = P(0, yhi)
    cv.arrow(x1, y0, x2, y0, cls="axis", head=7)
    cv.arrow(xc, ya, xc, yb, cls="axis", head=7)
    cv.text(x2 - 2, y0 - 9, xlabel, cls="lbl", anchor="end")
    cv.text(xc + 9, yb + 11, ylabel, cls="lbl")
    cv.text(xc - 8, y0 + 15, "O", cls="lbl", anchor="end")
    if unit_ticks:
        for t in (-1, 1):
            if xlo <= t <= xhi:
                px, py = P(t, 0)
                cv.line(px, py - 4, px, py + 4, cls="ink-thin")
                cv.text(px, py + 17, _num(t), cls="lbl-sm", anchor="middle")
            if ylo <= t <= yhi:
                px, py = P(0, t)
                cv.line(px - 4, py, px + 4, py, cls="ink-thin")
                cv.text(px - 8, py + 4, _num(t), cls="lbl-sm", anchor="end")


def _frame_with_axes(pts: Sequence[Pt], scale: float, pad_l: float, pad_r: float,
                     pad_t: float, pad_b: float, margin: float = 0.5
                     ) -> tuple[float, float, Callable[[float, float], Pt], tuple[float, float, float, float]]:
    """Khung + biên trục tính từ CÙNG một hộp bao.

    Tách hai phép tính này ra (khung một đằng, biên trục một nẻo) là cách chắc
    chắn nhất để mũi tên trục chọc ra ngoài ``viewBox`` mà không ai thấy.
    """
    xs = [q[0] for q in pts] + [0.0]
    ys = [q[1] for q in pts] + [0.0]
    box = (min(xs) - margin, max(xs) + margin, min(ys) - margin, max(ys) + margin)
    w, h, P = _fit([(box[0], box[2]), (box[1], box[3])], scale, pad_l, pad_r, pad_t, pad_b)
    return w, h, P, box


def _k_range(om: float, ph: float, base: float, step: float,
             xmin: float, xmax: float) -> range:
    """Chỉ số k để ``x = (base + k·step − φ)/ω`` rơi vào cửa sổ vẽ.

    Tính ngược từ cửa sổ chứ không quét một dải k cố định: khi φ lớn thì mốc cần
    tìm nằm ở k vài chục, quét dải cố định sẽ lặng lẽ không vẽ gì cả.
    """
    if abs(step) < 1e-9:
        return range(0)
    t0, t1 = om * xmin + ph, om * xmax + ph
    lo, hi = min(t0, t1), max(t0, t1)
    k0 = math.floor((lo - base) / step) - 1
    k1 = math.ceil((hi - base) / step) + 1
    if k1 - k0 > 80:
        return range(0)
    return range(k0, k1 + 1)


#: bề rộng trung bình một ký tự so với cỡ chữ, đo trên lớp `lbl-sm` (12px sans).
_CH_W = 0.54


def _text_w(text: str, size: float = 12.0) -> float:
    """Bề rộng ước lượng của một dòng chữ, đủ chính xác để biết nó có tràn khung."""
    return len(text) * size * _CH_W


def _wrap(text: str, max_w: float, size: float = 12.0) -> list[str]:
    """Cắt dòng tại khoảng trắng sao cho mỗi dòng vừa bề rộng cho phép."""
    words = text.split(" ")
    lines: list[str] = []
    cur = ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if cur and _text_w(trial, size) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def _caption(cv: Canvas, w: float, y: float, text: str) -> None:
    """Dòng chú thích dưới hình, tự xuống dòng khi khung hẹp hơn dòng chữ.

    Chú thích viết một dòng cứng là lỗi câm điển hình: hình nào khung hẹp (quỹ
    tích dạng tia, cung chứa góc) thì hai đầu câu bị ``viewBox`` cắt mất, mà
    kiểm tra toạ độ không thấy gì vì điểm neo vẫn nằm trong khung — chỉ có phần
    chữ vẽ ra mới lòi ra ngoài.
    """
    if not text:
        return
    lines = _wrap(text, w - 24.0)
    for i, line in enumerate(lines):
        cv.text(w / 2, y - (len(lines) - 1 - i) * 15.0, line, cls="lbl-sm", anchor="middle")


def _sub(cv: Canvas, x: float, y: float, base: str, sub: str,
         cls: str = "lbl", anchor: str = "start") -> None:
    """Nhãn có chỉ số dưới, dựng bằng ``<tspan>``.

    Không dùng ký tự chỉ số dưới Unicode: bảng ấy KHÔNG có chữ 'b' và 'c', nên
    nửa số nhãn buộc phải viết "m_b" — gạch dưới lộ nguyên ra thành chữ. Còn
    những chữ có trong bảng (ₐ, ₁) thì máy thiếu font sẽ vẽ ô vuông. ``<tspan>``
    thì mọi trình duyệt đều dựng được.
    """
    from .svgkit import _n as _svg_n
    from .svgkit import esc as _svg_esc

    cv.raw(
        f'<text x="{_svg_n(x)}" y="{_svg_n(y)}" text-anchor="{anchor}" class="{cls}">'
        f"{_svg_esc(base)}"
        f'<tspan font-size="70%" dy="4">{_svg_esc(sub)}</tspan>'
        f"</text>"
    )


def _pi_label(v: float) -> str:
    """Nhãn trục hoành theo bội của π; không phải bội "đẹp" thì trả số thập phân."""
    if abs(v) < 1e-9:
        return "0"
    for den in (1, 2, 3, 4, 6):
        num = v * den / math.pi
        k = round(num)
        if k != 0 and abs(num - k) < 1e-6:
            a = abs(k)
            body = "π" if a == 1 else f"{a}π"
            if den != 1:
                body = f"{body}/{den}"
            return ("−" if k < 0 else "") + body
    return _num(v)


# --------------------------------------------------------------------------
# 1. Đường tròn lượng giác
# --------------------------------------------------------------------------
def build_lg_duong_tron_luong_giac(p: Params) -> str:
    """Đường tròn lượng giác: góc α, điểm M, hình chiếu cos/sin, tuỳ chọn trục tang."""
    angle = _f(p.get("angle", 55), 55) % 360.0
    show_tan = bool(p.get("show_tan", False))
    show_sec = bool(p.get("show_sec", False))
    show_identity = bool(p.get("show_identity", False))
    caption = str(p.get("caption", ""))

    R = 118.0
    pad_l = 68.0
    pad_r = 132.0 if show_tan else 74.0
    pad_t = pad_b = 82.0 if show_tan else 62.0
    cx, cy = pad_l + R, pad_t + R
    w = cx + R + pad_r
    h = cy + R + pad_b + (22.0 if caption else 0.0)

    th = math.radians(angle)
    Mx, My = _pol(cx, cy, R, angle)
    Hx = Mx                      # chân hình chiếu trên Ox
    Ky = My                      # chân hình chiếu trên Oy

    cv = Canvas(w, h, title=f"Đường tròn lượng giác, góc {_num(angle)}°",
                desc="Điểm M trên đường tròn đơn vị; hình chiếu lên Ox là cos, lên Oy là sin.")
    cv.arrow(cx - R - 24, cy, cx + R + 30, cy, cls="axis", head=7)
    cv.arrow(cx, cy + R + 24, cx, cy - R - 30, cls="axis", head=7)
    cv.text(cx + R + 28, cy - 10, "cos", cls="lbl-sm", anchor="end")
    cv.text(cx + 9, cy - R - 22, "sin", cls="lbl-sm")
    for t, dx, dy in ((1, R, 0), (-1, -R, 0)):
        cv.line(cx + dx, cy - 4, cx + dx, cy + 4, cls="ink-thin")
        cv.text(cx + dx, cy + 18, _num(t), cls="lbl-sm", anchor="middle")
    for t, dy in ((1, -R), (-1, R)):
        cv.line(cx - 4, cy + dy, cx + 4, cy + dy, cls="ink-thin")
        cv.text(cx - 8, cy + dy + 4, _num(t), cls="lbl-sm", anchor="end")
    cv.circle(cx, cy, R, cls="ink")

    if show_identity:
        # Tam giác vuông OHM có OM = 1: Pytago cho sin²α + cos²α = 1.
        cv.polygon([(cx, cy), (Hx, cy), (Mx, My)], cls="fill-a")
        _right_angle_at(cv, (Hx, cy), (cx, cy), (Mx, My), size=11)

    cv.polyline(_arc_pts(cx, cy, 32, 0, angle), cls="accent-d", extra=_stroke(2))
    cv.text(*_pol(cx, cy, 50, angle / 2), s=f"{_num(angle)}°", cls="lbl-sm", anchor="middle")

    cv.line(Mx, My, Hx, cy, cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.line(Mx, My, cx, Ky, cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.line(cx, cy, Hx, cy, cls="accent-c", extra=_stroke(3.4))
    cv.line(cx, cy, cx, Ky, cls="accent-b", extra=_stroke(3.4))
    cv.arrow(cx, cy, Mx, My, cls="accent-a", head=9)
    cv.dot(Mx, My, r=3.6, cls="accent-a")

    sin_a, cos_a = math.sin(th), math.cos(th)
    # Nhãn cos đặt lệch về phía ngọn đoạn (0.68) chứ không ở giữa: giữa đoạn là
    # chỗ cung đánh dấu góc đi qua, và với góc tù thì hai thứ chồng lên nhau.
    cv.text(cx + (Hx - cx) * 0.68, cy + (22 if sin_a >= 0 else -13),
            "cos α", cls="lbl-sm", anchor="middle")
    # Nhãn sin đặt NGƯỢC phía với nhãn số đo góc (nằm trên tia phân giác α/2),
    # nếu không thì với α quanh 130° hai nhãn rơi trúng nhau. Và đặt ở 0.72 đoạn
    # thay vì giữa đoạn, vì giữa đoạn là nơi tia OM cắt ngang chỗ để chữ.
    on_right = angle >= 180.0
    cv.text(cx + (12 if on_right else -12), cy + (Ky - cy) * 0.72 + 4, "sin α",
            cls="lbl-sm", anchor="start" if on_right else "end")
    lx, ly = _pol(cx, cy, R + 16, angle)
    cv.text(lx, ly + (-6 if sin_a >= 0 else 14), "M", cls="lbl",
            anchor="start" if cos_a >= 0 else "end")

    if show_tan:
        # Trục tang là tiếp tuyến tại điểm gốc A(1; 0): tia OM cắt nó tại (1; tan α).
        ax = cx + R
        cv.line(ax, cy - R - 18, ax, cy + R + 18, cls="ink-thin", extra=' stroke-dasharray="6 4"')
        cv.text(ax + 8, cy - R - 22, "t", cls="lbl-sm")
        cv.dot(ax, cy, r=3, cls="accent-d")
        cv.text(ax + 6, cy + 18, "A", cls="lbl-sm")
        if abs(cos_a) > 1e-6 and abs(sin_a / cos_a) <= 1.45 and cos_a > 0:
            ty = cy - R * (sin_a / cos_a)
            cv.line(cx, cy, ax, ty, cls="ink-thin", extra=' stroke-dasharray="4 3"')
            cv.line(ax, cy, ax, ty, cls="accent-d", extra=_stroke(3.4))
            cv.text(ax + 10, (cy + ty) / 2 + 4, "tan α", cls="lbl-sm")
            cv.dot(ax, ty, r=3.2, cls="accent-d")
            cv.text(ax + 10, ty - 8, "T", cls="lbl")
            if show_sec:
                cv.line(cx, cy, ax, ty, cls="accent-b", extra=_stroke(2))
                _right_angle_at(cv, (ax, cy), (cx, cy), (ax, ty), size=11)
                cv.text((cx + ax) / 2 - 4, (cy + ty) / 2 - 10, "1/cos α", cls="lbl-sm", anchor="middle")

    _caption(cv, w, h - 18, caption)
    return cv.render()


def build_lg_dau_luong_giac(p: Params) -> str:
    """Dấu của sin, cos, tan, cot theo bốn góc phần tư."""
    R = _clamp(_f(p.get("R", 104), 104), 60, 140)
    w, h = 2 * R + 296.0, 2 * R + 224.0
    cx, cy = w / 2, h / 2
    cv = Canvas(w, h, title="Dấu của các giá trị lượng giác theo góc phần tư",
                desc="Bốn góc phần tư của đường tròn lượng giác và dấu của sin, cos, tan, cot ở mỗi phần tư.")
    quads = (
        ("I", 0, 90, "fill-a", ("sin > 0", "cos > 0", "tan, cot > 0")),
        ("II", 90, 180, "fill-b", ("sin > 0", "cos < 0", "tan, cot < 0")),
        ("III", 180, 270, "fill-c", ("sin < 0", "cos < 0", "tan, cot > 0")),
        ("IV", 270, 360, "fill-a", ("sin < 0", "cos > 0", "tan, cot < 0")),
    )
    for name, a1, a2, fill, _lines in quads:
        cv.polygon([(cx, cy)] + _arc_pts(cx, cy, R, a1, a2, 24), cls=fill)
        cv.text(*_pol(cx, cy, R * 0.62, (a1 + a2) / 2), s=name, cls="lbl", anchor="middle")
    cv.circle(cx, cy, R, cls="ink")
    cv.arrow(cx - R - 20, cy, cx + R + 26, cy, cls="axis", head=7)
    cv.arrow(cx, cy + R + 20, cx, cy - R - 26, cls="axis", head=7)
    cv.text(cx + R + 24, cy - 9, "cos", cls="lbl-sm", anchor="end")
    cv.text(cx + 9, cy - R - 18, "sin", cls="lbl-sm")

    # Khối dấu đặt ở bốn góc khung: đặt trong phần tư thì chữ đè lên cung tròn.
    corners = ((w - 14, 34, "end"), (14, 34, "start"),
               (14, h - 62, "start"), (w - 14, h - 62, "end"))
    for (name, _a1, _a2, _fill, lines), (tx, ty, anc) in zip(quads, corners):
        cv.text(tx, ty, f"Góc phần tư {name}", cls="lbl", anchor=anc)
        for i, ln in enumerate(lines):
            cv.text(tx, ty + 17 + i * 15, ln, cls="lbl-sm", anchor=anc)
    return cv.render()


_SPECIAL_DIRS = (
    (0, "0°", "0"), (30, "30°", "π/6"), (45, "45°", "π/4"), (60, "60°", "π/3"),
    (90, "90°", "π/2"), (120, "120°", "2π/3"), (135, "135°", "3π/4"), (150, "150°", "5π/6"),
    (180, "180°", "π"), (210, "210°", "7π/6"), (225, "225°", "5π/4"), (240, "240°", "4π/3"),
    (270, "270°", "3π/2"), (300, "300°", "5π/3"), (315, "315°", "7π/4"), (330, "330°", "11π/6"),
)


def build_lg_goc_dac_biet(p: Params) -> str:
    """Các cung đặc biệt trên đường tròn lượng giác, đối chiếu độ ↔ radian."""
    R = _clamp(_f(p.get("R", 150), 150), 90, 200)
    pad = 84.0
    w = h = 2 * (R + pad)
    cx = cy = R + pad
    cv = Canvas(w, h, title="Cung đặc biệt: độ và radian",
                desc="Đường tròn lượng giác với 16 cung đặc biệt, mỗi cung ghi số đo bằng độ và bằng radian.")
    cv.circle(cx, cy, R, cls="ink")
    # Mũi tên trục dừng TRƯỚC vành nhãn: kéo dài hơn nữa thì nhãn của bốn cung
    # 0°, 90°, 180°, 270° nằm đúng lên thân mũi tên.
    cv.arrow(cx - R - 15, cy, cx + R + 15, cy, cls="axis", head=7)
    cv.arrow(cx, cy + R + 15, cx, cy - R - 15, cls="axis", head=7)
    for deg, dlab, rlab in _SPECIAL_DIRS:
        p1 = _pol(cx, cy, R, deg)
        p2 = _pol(cx, cy, R + 9, deg)
        cv.line(*p1, *p2, cls="ink-thin")
        cv.line(cx, cy, *p1, cls="grid")
        cv.dot(*p1, r=2.8, cls="accent-a")
        c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        tx, ty = _pol(cx, cy, R + 21, deg)
        if abs(s) < 0.01:                     # cung 0° và 180°: nằm ngay trên trục Ox
            anchor, tx, ty = ("start" if c > 0 else "end"), tx, ty - 8
        elif abs(c) < 0.01:                   # cung 90° và 270°: nằm trên trục Oy
            anchor, tx = "start", tx + 10
        else:
            anchor = "start" if c > 0 else "end"
        cv.text(tx, ty - 2, dlab, cls="lbl-sm", anchor=anchor)
        cv.text(tx, ty + 13, rlab, cls="lbl", anchor=anchor)
    return cv.render()


_Q1_VALUES = (
    (0, "0", "(1 ; 0)"),
    (30, "π/6", "(√3/2 ; 1/2)"),
    (45, "π/4", "(√2/2 ; √2/2)"),
    (60, "π/3", "(1/2 ; √3/2)"),
    (90, "π/2", "(0 ; 1)"),
)


def build_lg_gia_tri_dac_biet(p: Params) -> str:
    """Phần tư thứ nhất: toạ độ (cos; sin) của các cung 0, π/6, π/4, π/3, π/2."""
    R = _clamp(_f(p.get("R", 190), 190), 120, 240)
    pad_l, pad_r, pad_t, pad_b = 62.0, 168.0, 72.0, 62.0
    w = pad_l + R + pad_r
    h = pad_t + R + pad_b
    ox, oy = pad_l, pad_t + R
    cv = Canvas(w, h, title="Giá trị lượng giác của cung đặc biệt",
                desc="Cung phần tư thứ nhất của đường tròn đơn vị với toạ độ (cos; sin) của các cung 0, π/6, π/4, π/3, π/2.")
    cv.arrow(ox - 22, oy, ox + R + 28, oy, cls="axis", head=7)
    cv.arrow(ox, oy + 22, ox, oy - R - 30, cls="axis", head=7)
    # Tên trục Oy nhường chỗ sang TRÁI trục: nhãn toạ độ của cung π/2 nằm ngay
    # trên đỉnh cung nên phía phải trục đã có chủ.
    cv.text(ox + R + 26, oy - 10, "cos", cls="lbl-sm", anchor="end")
    cv.text(ox - 9, oy - R - 18, "sin", cls="lbl-sm", anchor="end")
    cv.text(ox - 9, oy + 16, "O", cls="lbl", anchor="end")
    cv.polyline(_arc_pts(ox, oy, R, 0, 90, 48), cls="curve", extra=_stroke(2.5))
    for deg, rad, coord in _Q1_VALUES:
        px, py = _pol(ox, oy, R, deg)
        cv.line(ox, oy, px, py, cls="ink-thin")
        if 0 < deg < 90:
            cv.line(px, py, px, oy, cls="grid", extra=' stroke-dasharray="4 3"')
            cv.line(px, py, ox, py, cls="grid", extra=' stroke-dasharray="4 3"')
        cv.dot(px, py, r=3.4, cls="accent-a")
        tx, ty = _pol(ox, oy, R + 14, deg)
        # Hai cung đầu mút nằm đúng trên trục, phải né sang bên (π/2) hoặc xuống
        # dưới (cung 0) để không đè lên tên trục và mũi tên.
        if deg == 90:
            tx, ty = tx + 8, ty + 4
        elif deg == 0:
            ty += 20
        else:
            ty += 4
        cv.text(tx, ty, f"{rad}  {coord}", cls="lbl-sm", anchor="start")
    return cv.render()


_LIEN_KET = {
    "doi": (lambda a: -a, "Ox", "cos(−α) = cos α  ·  sin(−α) = −sin α"),
    "bu": (lambda a: 180.0 - a, "Oy", "sin(π − α) = sin α  ·  cos(π − α) = −cos α"),
    "hon-kem-pi": (lambda a: 180.0 + a, "O", "sin(π + α) = −sin α  ·  cos(π + α) = −cos α"),
    "phu": (lambda a: 90.0 - a, "y=x", "sin(π/2 − α) = cos α  ·  cos(π/2 − α) = sin α"),
    "hon-kem-pi-hai": (lambda a: 90.0 + a, "quay", "sin(π/2 + α) = cos α  ·  cos(π/2 + α) = −sin α"),
}


def build_lg_cung_lien_ket(p: Params) -> str:
    """Hai cung liên kết trên đường tròn lượng giác (đối, bù, phụ, hơn kém π, hơn kém π/2).

    Vẽ đủ CẢ hai hình chiếu của cả hai điểm: chỉ khi nhìn thấy hai đoạn chiếu
    trùng nhau hay đối nhau thì công thức mới thành hiển nhiên chứ không phải
    thành một dòng chữ phải học thuộc.
    """
    kind = str(p.get("kind", "doi"))
    if kind not in _LIEN_KET:
        kind = "doi"
    beta_of, sym, default_caption = _LIEN_KET[kind]
    alpha = _clamp(_f(p.get("angle", 52), 52), 10, 80)
    if kind == "phu" and abs(alpha - 45) < 7:
        alpha = 32.0        # α = 45° làm hai điểm trùng nhau, hình mất hết ý nghĩa
    beta = beta_of(alpha)
    caption = str(p.get("caption", default_caption))

    R = 120.0
    pad = 78.0
    w = h = 2 * (R + pad)
    h += 24.0
    cx = cy = R + pad
    cv = Canvas(w, h, title=f"Cung liên kết ({kind}) trên đường tròn lượng giác",
                desc="Hai điểm liên kết trên đường tròn đơn vị cùng hình chiếu của chúng lên hai trục.")
    cv.arrow(cx - R - 22, cy, cx + R + 28, cy, cls="axis", head=7)
    cv.arrow(cx, cy + R + 22, cx, cy - R - 28, cls="axis", head=7)
    cv.text(cx + R + 26, cy - 10, "cos", cls="lbl-sm", anchor="end")
    cv.text(cx + 9, cy - R - 20, "sin", cls="lbl-sm")
    cv.circle(cx, cy, R, cls="ink")

    # Yếu tố đối xứng: chính nó giải thích vì sao hai giá trị bằng hay đối nhau.
    if sym == "Ox":
        cv.line(cx - R - 14, cy, cx + R + 14, cy, cls="accent-d", extra=_stroke(2.4, "7 5"))
    elif sym == "Oy":
        cv.line(cx, cy - R - 14, cx, cy + R + 14, cls="accent-d", extra=_stroke(2.4, "7 5"))
    elif sym == "y=x":
        d = (R + 14) / math.sqrt(2)
        cv.line(cx - d, cy + d, cx + d, cy - d, cls="accent-d", extra=_stroke(2.4, "7 5"))
        # Ghi tên trục đối xứng ở đầu DƯỚI: đầu trên là góc phần tư thứ nhất,
        # nơi cả M lẫn N đều nằm khi α nhọn, nên ba nhãn sẽ chồng lên nhau.
        cv.text(cx - d - 4, cy + d + 14, "y = x", cls="lbl-sm", anchor="end")

    Mx, My = _pol(cx, cy, R, alpha)
    Nx, Ny = _pol(cx, cy, R, beta)
    if sym == "O":
        cv.line(Nx, Ny, Mx, My, cls="accent-d", extra=_stroke(2.4, "7 5"))
    elif sym == "quay":
        cv.polyline(_arc_pts(cx, cy, R + 14, alpha, beta, 20), cls="accent-d", extra=_stroke(2.4, "5 4"))

    for (px, py), cls in (((Mx, My), "accent-a"), ((Nx, Ny), "accent-b")):
        cv.line(px, py, px, cy, cls="ink-thin", extra=' stroke-dasharray="4 3"')
        cv.line(px, py, cx, py, cls="ink-thin", extra=' stroke-dasharray="4 3"')
        cv.arrow(cx, cy, px, py, cls=cls, head=9)
        cv.dot(px, py, r=3.4, cls=cls)
    cv.line(cx, cy, Mx, cy, cls="accent-a", extra=_stroke(3.6))
    cv.line(cx, cy, Nx, cy, cls="accent-b", extra=_stroke(2.2, "5 3"))
    cv.line(cx, cy, cx, My, cls="accent-a", extra=_stroke(3.6))
    cv.line(cx, cy, cx, Ny, cls="accent-b", extra=_stroke(2.2, "5 3"))

    ax, ay = _pol(cx, cy, R + 18, alpha)
    bx, by = _pol(cx, cy, R + 18, beta)
    cv.text(ax, ay + 4, "M(α)", cls="lbl",
            anchor="start" if math.cos(math.radians(alpha)) >= 0 else "end")
    cv.text(bx, by + 4, "N", cls="lbl",
            anchor="start" if math.cos(math.radians(beta)) >= 0 else "end")
    _caption(cv, w, h - 16, caption)
    return cv.render()


def build_lg_cung_quat(p: Params) -> str:
    """Hình quạt: độ dài cung ℓ = Rα và diện tích quạt S = ½R²α (α tính bằng radian)."""
    alpha = _clamp(_f(p.get("alpha", 72), 72), 8, 330)
    R = _clamp(_f(p.get("R_px", 128), 128), 70, 170)
    pad = 76.0
    w = h = 2 * (R + pad)
    cx = cy = R + pad
    caption = str(p.get("caption", "ℓ = R·α  ·  S = ½R²α  (α tính bằng radian)"))
    cv = Canvas(w, h, title="Độ dài cung và diện tích hình quạt",
                desc="Hình quạt tròn bán kính R chắn góc ở tâm α; cung tương ứng có độ dài R·α.")
    cv.polygon([(cx, cy)] + _arc_pts(cx, cy, R, 0, alpha, 48), cls="fill-a")
    cv.circle(cx, cy, R, cls="ink-thin")
    cv.polyline(_arc_pts(cx, cy, R, 0, alpha, 60), cls="accent-b", extra=_stroke(4))
    cv.line(cx, cy, cx + R, cy, cls="ink")
    cv.line(cx, cy, *_pol(cx, cy, R, alpha), cls="ink")
    cv.polyline(_arc_pts(cx, cy, 30, 0, alpha, 24), cls="accent-d", extra=_stroke(2))
    cv.text(*_pol(cx, cy, 46, alpha / 2), s="α", cls="lbl", anchor="middle")
    cv.dot(cx, cy, r=3, cls="accent-a")
    cv.text(cx - 8, cy + 16, "O", cls="lbl", anchor="end")
    cv.text(cx + R / 2, cy - 8, "R", cls="lbl", anchor="middle")
    lx, ly = _pol(cx, cy, R + 22, alpha / 2)
    cv.text(lx, ly + 4, "ℓ", cls="lbl",
            anchor="start" if math.cos(math.radians(alpha / 2)) >= 0 else "end")
    # Nhãn diện tích đẩy ra 0.66R: ở 0.5R nó rơi trúng nhãn góc α (bán kính 46)
    # khi R nhỏ, hai dòng chữ in đè lên nhau thành một vệt không đọc được.
    sx, sy = _pol(cx, cy, R * 0.66, alpha / 2)
    cv.text(sx, sy + 4, "S", cls="lbl", anchor="middle")
    _caption(cv, w, h - 22, caption)
    return cv.render()


# --------------------------------------------------------------------------
# 2. Đồ thị hàm lượng giác
# --------------------------------------------------------------------------
def _trig_value(fn: str, t: float) -> float:
    if fn == "sin":
        return math.sin(t)
    if fn == "cos":
        return math.cos(t)
    if fn == "tan":
        c = math.cos(t)
        if abs(c) < 1e-9:
            raise ValueError("tiệm cận")
        return math.sin(t) / c
    s = math.sin(t)
    if abs(s) < 1e-9:
        raise ValueError("tiệm cận")
    return math.cos(t) / s


def build_lg_do_thi_luong_giac(p: Params) -> str:
    """Đồ thị y = A·f(ωx + φ) với biên độ, chu kì và pha vẽ thành đại lượng đo được.

    Biên độ và chu kì được đánh dấu bằng mũi tên hai đầu trên chính đồ thị: đó là
    cách duy nhất để "A" và "T" thôi là ký hiệu trong công thức mà thành đoạn
    thẳng người học đo được trên hình.
    """
    fn = str(p.get("fn", "sin")).lower()
    if fn not in ("sin", "cos", "tan", "cot"):
        fn = "sin"
    A = _f(p.get("A", 1), 1)
    if abs(A) < 1e-6:
        A = 1.0
    om = _f(p.get("omega", 1), 1)
    if abs(om) < 1e-6:
        om = 1.0
    ph = _f(p.get("phi", 0), 0)
    periodic = fn in ("sin", "cos")
    T = (2 * math.pi if periodic else math.pi) / abs(om)
    x0 = -ph / om                                 # điểm mốc pha (ωx + φ = 0)
    xmin = x0 - 0.42 * T
    xmax = x0 + 2.12 * T
    ylim = abs(A) * (1.55 if periodic else 2.8)

    w, h = 528.0, 344.0
    bx, by, bw, bh = 54.0, 34.0, 440.0, 250.0
    cv = Canvas(w, h, title=f"Đồ thị hàm y = A·{fn}(ωx + φ)",
                desc="Đồ thị hàm lượng giác với biên độ, chu kì và pha ban đầu được đánh dấu trên hình.")

    def sx(x: float) -> float:
        return bx + (x - xmin) / (xmax - xmin) * bw

    def sy(y: float) -> float:
        return by + (ylim - y) / (2 * ylim) * bh

    y0 = sy(0)
    # Vạch chia đặt tại bội của T/4 (sin, cos) hay T/2 (tan, cot): đúng chỗ đồ thị
    # cắt trục / đạt cực trị / có tiệm cận, nên đọc chu kì được ngay trên trục.
    step = T / (4 if periodic else 2)
    k0 = math.ceil((xmin - x0) / step)
    k1 = math.floor((xmax - x0) / step)
    x_axis_y = sx(min(max(0.0, xmin), xmax))     # hoành độ trục Oy trong khung
    for k in range(k0, k1 + 1):
        xv = x0 + k * step
        px = sx(xv)
        cv.line(px, by, px, by + bh, cls="grid")
        cv.line(px, y0 - 4, px, y0 + 4, cls="ink-thin")
        # Vạch nào trùng trục tung thì đẩy nhãn sang trái, kẻo số nằm đè lên trục.
        near_axis = abs(px - x_axis_y) < 9
        cv.text(px - (7 if near_axis else 0), y0 + 18, _pi_label(xv),
                cls="lbl-sm", anchor="end" if near_axis else "middle")
    for yv in (-abs(A), abs(A)):
        cv.line(bx, sy(yv), bx + bw, sy(yv), cls="grid")

    cv.arrow(bx - 10, y0, bx + bw + 10, y0, cls="axis", head=7)
    cv.arrow(x_axis_y, by + bh + 8, x_axis_y, by - 8, cls="axis", head=7)
    cv.text(bx + bw + 8, y0 - 10, "x", cls="lbl", anchor="end")
    cv.text(x_axis_y + 9, by - 4, "y", cls="lbl")

    # tiệm cận của tan/cot
    if not periodic:
        base = math.pi / 2 if fn == "tan" else 0.0
        for k in _k_range(om, ph, base, math.pi, xmin, xmax):
            xa = ((base + k * math.pi) - ph) / om
            if xmin <= xa <= xmax:
                cv.line(sx(xa), by, sx(xa), by + bh, cls="accent-b", extra=_stroke(1.4, "6 4"))

    N = 600
    samples: list[tuple[float, Optional[float]]] = []
    for i in range(N + 1):
        x = xmin + (xmax - xmin) * i / N
        try:
            y = A * _trig_value(fn, om * x + ph)
        except (ValueError, ZeroDivisionError, OverflowError):
            y = None
        if y is not None and not math.isfinite(y):
            y = None
        samples.append((x, y))

    seg: list[Pt] = []
    prev: Optional[float] = None
    for x, y in samples:
        broken = (y is None or abs(y) > ylim * 1.25
                  or (prev is not None and abs(y - prev) > ylim))
        if broken:
            if len(seg) > 1:
                cv.polyline(seg, cls="curve")
            seg = []
            prev = None if y is None else y
            continue
        seg.append((sx(x), sy(y)))
        prev = y
    if len(seg) > 1:
        cv.polyline(seg, cls="curve")

    if periodic and bool(p.get("show_amplitude", True)):
        # Đỉnh gần nhất nằm trong khung: sin đạt cực đại khi ωx + φ = π/2, cos khi = 0.
        base = (math.pi / 2 if fn == "sin" else 0.0)
        peaks = sorted(px_ for px_ in
                       (((base + 2 * math.pi * k) - ph) / om
                        for k in _k_range(om, ph, base, 2 * math.pi, xmin, xmax))
                       if xmin + 0.02 * T <= px_ <= xmax - 0.02 * T)
        if peaks:
            xp = peaks[0]
            cv.arrow(sx(xp), y0, sx(xp), sy(A), cls="accent-c", head=7)
            cv.arrow(sx(xp), sy(A), sx(xp), y0, cls="accent-c", head=7)
            cv.text(sx(xp) + 7, (y0 + sy(A)) / 2 + 4,
                    str(p.get("amp_label", "A")), cls="lbl")
        if len(peaks) >= 2 and bool(p.get("show_period", True)):
            ymark = sy(abs(A) * 1.28 if A > 0 else -abs(A) * 1.28)
            cv.arrow(sx(peaks[0]), ymark, sx(peaks[1]), ymark, cls="accent-d", head=7)
            cv.arrow(sx(peaks[1]), ymark, sx(peaks[0]), ymark, cls="accent-d", head=7)
            cv.text((sx(peaks[0]) + sx(peaks[1])) / 2, ymark - 7,
                    str(p.get("period_label", "T = 2π/|ω|")), cls="lbl-sm", anchor="middle")
    elif not periodic and bool(p.get("show_period", True)):
        base = math.pi / 2 if fn == "tan" else 0.0
        asym = sorted(a for a in (((base + math.pi * k) - ph) / om
                                  for k in _k_range(om, ph, base, math.pi, xmin, xmax))
                      if xmin <= a <= xmax)
        if len(asym) >= 2:
            ymark = sy(ylim * 0.82)
            cv.arrow(sx(asym[0]), ymark, sx(asym[1]), ymark, cls="accent-d", head=7)
            cv.arrow(sx(asym[1]), ymark, sx(asym[0]), ymark, cls="accent-d", head=7)
            cv.text((sx(asym[0]) + sx(asym[1])) / 2, ymark - 7,
                    str(p.get("period_label", "T = π/|ω|")), cls="lbl-sm", anchor="middle")

    if bool(p.get("bounds", False)) and periodic:
        for yv, lab in ((abs(A), "y = 1"), (-abs(A), "y = −1")):
            cv.line(bx, sy(yv), bx + bw, sy(yv), cls="accent-b", extra=_stroke(1.6, "6 4"))
            cv.text(bx + bw - 4, sy(yv) - 6, str(p.get("bound_label", lab)),
                    cls="lbl-sm", anchor="end")

    levels = p.get("levels")
    if levels is None and p.get("level") is not None:
        levels = [p.get("level")]
    if levels:
        for raw in list(levels)[:3]:
            m = _f(raw, 0)
            if abs(m) > ylim:
                continue
            cv.line(bx, sy(m), bx + bw, sy(m), cls="accent-b", extra=_stroke(1.8, "7 4"))
            cv.text(bx + 2, sy(m) - 6, f"y = {_num(m)}", cls="lbl-sm")
            prev_x = prev_y = None
            for x, y in samples:
                if y is not None and prev_y is not None and abs(y - prev_y) < ylim:
                    if (prev_y - m) * (y - m) <= 0 and prev_y != y:
                        xr = prev_x + (m - prev_y) * (x - prev_x) / (y - prev_y)
                        if xmin <= xr <= xmax:
                            cv.dot(sx(xr), sy(m), r=3.6, cls="accent-b")
                prev_x, prev_y = x, y
    _caption(cv, w, h - 12, str(p.get("caption", "")))
    return cv.render()


# --------------------------------------------------------------------------
# 3. Tam giác vuông & tỉ số lượng giác
# --------------------------------------------------------------------------
_TISO_SIDES = {
    "sin": ("doi", "huyen"),
    "cos": ("ke", "huyen"),
    "tan": ("doi", "ke"),
    "cot": ("ke", "doi"),
}


def build_lg_ti_so_luong_giac(p: Params) -> str:
    """Tam giác vuông với góc nhọn α: cạnh đối, cạnh kề, cạnh huyền.

    ``highlight`` tô đậm đúng hai cạnh của tỉ số đang xét — không tô thì bốn công
    thức sin/cos/tan/cot dùng chung một hình, người học không biết nhìn vào đâu.
    """
    alpha = _clamp(_f(p.get("alpha", 38), 38), 12, 78)
    mode = str(p.get("mode", "ti-so"))
    highlight = p.get("highlight")
    if highlight not in _TISO_SIDES:
        highlight = None

    t = math.tan(math.radians(alpha))
    if t > 1:
        vert, horiz = 208.0, 208.0 / t
    else:
        horiz, vert = 208.0, 208.0 * t
    pad_l, pad_r, pad_t, pad_b = 74.0, 122.0, 62.0, 66.0
    w = pad_l + horiz + pad_r
    h = pad_t + vert + pad_b
    O = (pad_l, pad_t + vert)
    H = (pad_l + horiz, pad_t + vert)
    C = (pad_l + horiz, pad_t)

    if mode == "don-vi":
        lab_ke, lab_doi, lab_huyen = "cos α", "sin α", "1"
        caption = "Cạnh huyền bằng 1 ⇒ Pytago cho sin²α + cos²α = 1"
    else:
        lab_ke, lab_doi, lab_huyen = "cạnh kề", "cạnh đối", "cạnh huyền"
        caption = str(p.get("caption", ""))

    cls_ke = cls_doi = cls_huyen = "ink"
    if highlight:
        tu, mau = _TISO_SIDES[highlight]          # tử số, mẫu số của tỉ số đang xét
        colors = {tu: "accent-b", mau: "accent-c"}
        cls_ke = colors.get("ke", "ink")
        cls_doi = colors.get("doi", "ink")
        cls_huyen = colors.get("huyen", "ink")

    cv = Canvas(w, h, title=f"Tỉ số lượng giác của góc nhọn {_num(alpha)}°",
                desc="Tam giác vuông với góc nhọn α, ghi rõ cạnh đối, cạnh kề và cạnh huyền.")
    cv.polygon([O, H, C], cls="fill-a")
    cv.line(*O, *H, cls=cls_ke, extra=_stroke(3.6) if cls_ke != "ink" else "")
    cv.line(*H, *C, cls=cls_doi, extra=_stroke(3.6) if cls_doi != "ink" else "")
    cv.line(*C, *O, cls=cls_huyen, extra=_stroke(3.6) if cls_huyen != "ink" else "")
    _right_angle_at(cv, H, O, C, size=13)
    _angle_at(cv, O, H, C, r=34, label="α", lgap=16)

    cv.text((O[0] + H[0]) / 2, O[1] + 22, lab_ke, cls="lbl-sm", anchor="middle")
    cv.text(H[0] + 10, (H[1] + C[1]) / 2 + 4, lab_doi, cls="lbl-sm")
    # Nhãn cạnh huyền đẩy 24px theo pháp tuyến: 17px thì nét vẽ còn cắt ngang
    # phần chân chữ, vì điểm neo của <text> là đường cơ sở chứ không phải tâm.
    mx, my = (O[0] + C[0]) / 2, (O[1] + C[1]) / 2
    nx, ny = -(O[1] - C[1]), -(C[0] - O[0])
    nl = math.hypot(nx, ny) or 1.0
    cv.text(mx + 24 * nx / nl, my + 24 * ny / nl + 4, lab_huyen, cls="lbl-sm", anchor="middle")
    _caption(cv, w, h - 16, caption)
    return cv.render()


def build_lg_tam_giac_vuong_abc(p: Params) -> str:
    """Tam giác ABC vuông tại A: cạnh a, b, c và hai góc nhọn B, C (phụ nhau)."""
    B_deg = _clamp(_f(p.get("B", 54), 54), 15, 75)
    show_phu = bool(p.get("show_phu", False))
    t = math.tan(math.radians(B_deg))
    if t > 1:
        vert, horiz = 206.0, 206.0 / t
    else:
        horiz, vert = 206.0, 206.0 * t
    pad_l, pad_r, pad_t, pad_b = 86.0, 92.0, 66.0, 68.0
    w = pad_l + horiz + pad_r
    h = pad_t + vert + pad_b
    A = (pad_l, pad_t + vert)
    B = (pad_l + horiz, pad_t + vert)
    C = (pad_l, pad_t)

    cv = Canvas(w, h, title="Tam giác ABC vuông tại A",
                desc="Tam giác vuông tại A với cạnh huyền a = BC, hai cạnh góc vuông b = AC và c = AB.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    _right_angle_at(cv, A, B, C, size=13)
    _angle_at(cv, B, A, C, r=32, label="B", lgap=15)
    _angle_at(cv, C, A, B, r=32, label="C", lgap=15)
    cv.text(A[0] - 10, A[1] + 18, "A", cls="lbl", anchor="end")
    cv.text(B[0] + 10, B[1] + 18, "B", cls="lbl")
    cv.text(C[0] - 10, C[1] - 8, "C", cls="lbl", anchor="end")
    cv.text((A[0] + B[0]) / 2, A[1] + 22, "c", cls="lbl", anchor="middle")
    cv.text(A[0] - 12, (A[1] + C[1]) / 2 + 4, "b", cls="lbl", anchor="end")
    cv.text((B[0] + C[0]) / 2 + 12, (B[1] + C[1]) / 2 - 6, "a", cls="lbl")
    if show_phu:
        _caption(cv, w, h - 16, "B + C = 90° ⇒ sin B = cos C, tan B = cot C")
    else:
        _caption(cv, w, h - 16, str(p.get("caption", "")))
    return cv.render()


def build_lg_he_thuc_tam_giac_vuong(p: Params) -> str:
    """Hệ thức lượng trong tam giác vuông: đường cao AH ứng với cạnh huyền, hoặc trung tuyến AM."""
    kind = str(p.get("kind", "duong-cao"))
    if kind not in ("duong-cao", "trung-tuyen"):
        kind = "duong-cao"
    b = _clamp(_f(p.get("b", 4), 4), 0.6, 20)      # AC
    c = _clamp(_f(p.get("c", 3), 3), 0.6, 20)      # AB
    a = math.hypot(b, c)
    hh = b * c / a                                  # đường cao AH
    cc = c * c / a                                  # hình chiếu HB
    scale = 260.0 / a
    # B ở gốc, C trên tia Ox, A phía trên; toạ độ thế giới (y hướng lên).
    Bw, Cw = (0.0, 0.0), (a, 0.0)
    Aw = (cc, hh)
    Mw = (a / 2, 0.0)
    pts = [Bw, Cw, Aw, Mw]
    if kind == "trung-tuyen":
        pts.append((a / 2, a / 2))     # chừa chỗ cho đường tròn ngoại tiếp tâm M
    w, h, P = _fit(pts, scale, 66.0, 66.0, 62.0, 66.0)
    B, C, A, M = P(*Bw), P(*Cw), P(*Aw), P(*Mw)
    H = P(cc, 0.0)

    cv = Canvas(w, h, title="Hệ thức lượng trong tam giác vuông",
                desc="Tam giác vuông tại A với đường cao AH xuống cạnh huyền BC.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    _right_angle_at(cv, A, B, C, size=13)
    for pt, name, anc, dx, dy in ((A, "A", "middle", 0, -12), (B, "B", "end", -8, 18),
                                  (C, "C", "start", 8, 18)):
        cv.text(pt[0] + dx, pt[1] + dy, name, cls="lbl", anchor=anc)
    cv.text((A[0] + B[0]) / 2 - 12, (A[1] + B[1]) / 2, "c", cls="lbl", anchor="end")
    cv.text((A[0] + C[0]) / 2 + 10, (A[1] + C[1]) / 2, "b", cls="lbl")

    if kind == "duong-cao":
        cv.line(*A, *H, cls="accent-b", extra=_stroke(2.4))
        _right_angle_at(cv, H, B, A, size=11)
        cv.dot(*H, r=3, cls="accent-b")
        cv.text(H[0] + 8, H[1] + 18, "H", cls="lbl")
        cv.text(A[0] + 10, (A[1] + H[1]) / 2, "h", cls="lbl")
        cv.line(B[0], B[1] + 22, H[0], H[1] + 22, cls="accent-c", extra=_stroke(2))
        cv.line(H[0], H[1] + 22, C[0], C[1] + 22, cls="accent-d", extra=_stroke(2))
        cv.text((B[0] + H[0]) / 2, B[1] + 38, "c′", cls="lbl", anchor="middle")
        cv.text((H[0] + C[0]) / 2, C[1] + 38, "b′", cls="lbl", anchor="middle")
        _caption(cv, w, h - 14, str(p.get("caption", "b² = a·b′,  c² = a·c′,  h² = b′·c′,  a·h = b·c")))
    else:
        cv.circle(M[0], M[1], a / 2 * scale, cls="ink-thin", extra=' stroke-dasharray="6 5"')
        cv.line(*A, *M, cls="accent-b", extra=_stroke(2.6))
        cv.dot(*M, r=3.2, cls="accent-b")
        cv.text(M[0], M[1] + 20, "M", cls="lbl", anchor="middle")
        cv.text((A[0] + M[0]) / 2 + 8, (A[1] + M[1]) / 2, "m", cls="lbl")
        _caption(cv, w, h - 14, str(p.get("caption", "M là trung điểm BC ⇒ AM = MB = MC = ½·BC")))
    return cv.render()


# --------------------------------------------------------------------------
# 4. Giải tam giác
# --------------------------------------------------------------------------
def _tri_bcA(b: float, c: float, A_deg: float) -> tuple[Pt, Pt, Pt]:
    """Tam giác từ hai cạnh b = AC, c = AB và góc xen giữa A (hệ toán, y hướng lên)."""
    ar = math.radians(A_deg)
    return (0.0, 0.0), (c, 0.0), (b * math.cos(ar), b * math.sin(ar))


def _label_vertices(cv: Canvas, A: Pt, B: Pt, C: Pt,
                    names: Sequence[str] = ("A", "B", "C"), gap: float = 17.0) -> None:
    """Nhãn ba đỉnh, đẩy ra ngoài theo hướng trọng tâm → đỉnh.

    Đặt cứng "A dưới-trái, B dưới-phải, C phía trên" chỉ đúng với đúng một cách
    dựng tam giác. Generator nào xếp đỉnh khác đi — tam giác đều lấy A làm đỉnh
    trên chẳng hạn — là nhãn rơi vào TRONG tam giác, đè lên cạnh.
    """
    gx = (A[0] + B[0] + C[0]) / 3
    gy = (A[1] + B[1] + C[1]) / 3
    for pt, name in zip((A, B, C), names):
        dx, dy = pt[0] - gx, pt[1] - gy
        d = math.hypot(dx, dy) or 1.0
        cv.text(pt[0] + gap * dx / d, pt[1] + gap * dy / d + 5, name,
                cls="lbl", anchor="middle")


def _side_label(cv: Canvas, P1: Pt, P2: Pt, Q: Pt, text: str, cls: str = "lbl",
                gap: float = 18.0) -> None:
    """Nhãn cạnh P1P2, đẩy theo PHÁP TUYẾN của cạnh, về phía ngược với đỉnh Q.

    Đẩy theo hướng "ra xa Q" thì đúng với tam giác gần đều nhưng sai hẳn khi
    tam giác tù: lúc ấy hướng ra xa Q gần như SONG SONG với cạnh, nên nhãn trượt
    dọc theo cạnh rồi nằm đè lên chính nét vẽ (định lí cosin với A = 120° là ví
    dụ thấy rõ nhất).
    """
    mx, my = (P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2
    ex, ey = P2[0] - P1[0], P2[1] - P1[1]
    L = math.hypot(ex, ey) or 1.0
    nx, ny = -ey / L, ex / L
    if (mx - Q[0]) * nx + (my - Q[1]) * ny < 0:
        nx, ny = -nx, -ny
    # Cạnh càng dựng đứng thì nhãn (căn giữa theo chiều ngang) càng phải đẩy xa:
    # khoảng cách cố định chỉ đủ cho cạnh nằm ngang, còn cạnh gần thẳng đứng thì
    # nửa bề rộng chữ thò ngược lại và cạnh gạch ngang qua giữa nhãn.
    half = 0.5 * _text_w(text, 15.0 if cls == "lbl" else 12.0)
    push = gap + half * abs(nx)
    cv.text(mx + push * nx, my + push * ny + 4, text, cls=cls, anchor="middle")


def build_lg_tam_giac_co_ban(p: Params) -> str:
    """Tam giác ABC với ba cạnh a, b, c (và nửa chu vi p nếu cần)."""
    b = _clamp(_f(p.get("b", 5), 5), 0.5, 40)
    c = _clamp(_f(p.get("c", 6.4), 6.4), 0.5, 40)
    A_deg = _clamp(_f(p.get("A", 58), 58), 15, 160)
    Aw, Bw, Cw = _tri_bcA(b, c, A_deg)
    scale = 250.0 / max(b, c)
    w, h, P = _fit((Aw, Bw, Cw), scale, 72.0, 72.0, 66.0, 74.0)
    A, B, C = P(*Aw), P(*Bw), P(*Cw)
    a = math.dist(Bw, Cw)
    cv = Canvas(w, h, title="Tam giác ABC với ba cạnh a, b, c",
                desc="Tam giác ABC, cạnh a đối diện đỉnh A, cạnh b đối diện B, cạnh c đối diện C.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    _label_vertices(cv, A, B, C)
    _side_label(cv, B, C, A, "a")
    _side_label(cv, A, C, B, "b")
    _side_label(cv, A, B, C, "c")
    del a
    _caption(cv, w, h - 16,
             str(p.get("caption", "a, b, c là ba cạnh · nửa chu vi p = (a + b + c)/2")))
    return cv.render()


def build_lg_dinh_li_cosin(p: Params) -> str:
    """Định lí cosin: a² = b² + c² − 2bc·cos A — hình dựng đúng từ b, c và góc A."""
    b = _clamp(_f(p.get("b", 5), 5), 0.5, 40)
    c = _clamp(_f(p.get("c", 6.4), 6.4), 0.5, 40)
    A_deg = _clamp(_f(p.get("A", 62), 62), 15, 160)
    Aw, Bw, Cw = _tri_bcA(b, c, A_deg)
    a = math.dist(Bw, Cw)
    scale = 248.0 / max(b, c)
    w, h, P = _fit((Aw, Bw, Cw), scale, 78.0, 78.0, 68.0, 76.0)
    A, B, C = P(*Aw), P(*Bw), P(*Cw)
    cv = Canvas(w, h, title="Định lí cosin trong tam giác",
                desc="Tam giác ABC với hai cạnh b, c và góc A xen giữa; cạnh a đối diện A được tính theo định lí cosin.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    cv.line(*B, *C, cls="accent-b", extra=_stroke(3.4))
    _label_vertices(cv, A, B, C)
    _angle_at(cv, A, B, C, r=34, label="A", lgap=16)
    _side_label(cv, B, C, A, f"a = {_num(a)}", cls="lbl")
    _side_label(cv, A, C, B, f"b = {_num(b)}")
    _side_label(cv, A, B, C, f"c = {_num(c)}")
    _caption(cv, w, h - 16,
             str(p.get("caption", f"a² = b² + c² − 2bc·cos A  (A = {_num(A_deg)}°)")))
    return cv.render()


def build_lg_dinh_li_sin(p: Params) -> str:
    """Định lí sin: tam giác ABC nội tiếp đường tròn bán kính R, a/sin A = 2R."""
    A_deg = _clamp(_f(p.get("A", 48), 48), 20, 120)
    B_deg = _clamp(_f(p.get("B", 72), 72), 20, 120)
    if A_deg + B_deg > 155:
        A_deg, B_deg = 48.0, 72.0
    R = _clamp(_f(p.get("R_px", 122), 122), 80, 160)
    pad = 84.0
    w = h = 2 * (R + pad)
    h += 22.0
    cx = cy = R + pad
    # Cung BC có số đo 2A nên đặt B, C đối xứng qua phương thẳng đứng dưới tâm.
    thB, thC = 270.0 - A_deg, 270.0 + A_deg
    thA = 270.0 + A_deg + 2 * B_deg
    B, C, A = _pol(cx, cy, R, thB), _pol(cx, cy, R, thC), _pol(cx, cy, R, thA)
    cv = Canvas(w, h, title="Định lí sin và đường tròn ngoại tiếp",
                desc="Tam giác ABC nội tiếp đường tròn tâm O bán kính R; tỉ số a chia sin A bằng 2R.")
    cv.circle(cx, cy, R, cls="ink-thin")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    cv.line(*B, *C, cls="accent-b", extra=_stroke(3.4))
    cv.line(cx, cy, *A, cls="accent-c", extra=_stroke(2.4))
    cv.dot(cx, cy, r=3.2, cls="accent-c")
    cv.text(cx - 8, cy + 16, "O", cls="lbl", anchor="end")
    # Nhãn R đẩy theo pháp tuyến của OA về phía ngoài tam giác: đặt lệch 8px
    # theo trục hoành thì với A ở gần đỉnh, nó rơi đúng vào nhãn góc A.
    gx, gy = (A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3
    rnx, rny = -(A[1] - cy), A[0] - cx
    rl = math.hypot(rnx, rny) or 1.0
    # Neo nhãn R ở 0.62 quãng A→O chứ không ở giữa: nửa trên của bán kính OA nằm
    # ngay dưới đỉnh A, đúng chỗ cung đánh dấu góc A và nhãn của nó chiếm.
    mid_r = (A[0] + 0.62 * (cx - A[0]), A[1] + 0.62 * (cy - A[1]))
    if (mid_r[0] - gx) * rnx + (mid_r[1] - gy) * rny < 0:
        rnx, rny = -rnx, -rny
    cv.text(mid_r[0] + 15 * rnx / rl, mid_r[1] + 15 * rny / rl + 4, "R",
            cls="lbl", anchor="middle")
    _angle_at(cv, A, B, C, r=30, label="A", lgap=15)
    for pt, name in ((A, "A"), (B, "B"), (C, "C")):
        dx, dy = pt[0] - cx, pt[1] - cy
        d = math.hypot(dx, dy) or 1.0
        cv.text(pt[0] + 17 * dx / d, pt[1] + 17 * dy / d + 5, name, cls="lbl", anchor="middle")
    _side_label(cv, B, C, A, "a")
    _caption(cv, w, h - 14, str(p.get("caption", "a / sin A = b / sin B = c / sin C = 2R")))
    return cv.render()


def build_lg_dien_tich_sin(p: Params) -> str:
    """S = ½·a·b·sin C: đường cao hạ từ A xuống CB có độ dài đúng bằng b·sin C."""
    a = _clamp(_f(p.get("a", 6.4), 6.4), 0.5, 40)     # CB
    b = _clamp(_f(p.get("b", 4.6), 4.6), 0.5, 40)     # CA
    C_deg = _clamp(_f(p.get("C", 58), 58), 15, 150)
    cr = math.radians(C_deg)
    Cw = (0.0, 0.0)
    Bw = (a, 0.0)
    Aw = (b * math.cos(cr), b * math.sin(cr))
    Fw = (Aw[0], 0.0)                                  # chân đường cao
    scale = 246.0 / max(a, b)
    w, h, P = _fit((Cw, Bw, Aw, Fw), scale, 78.0, 78.0, 66.0, 76.0)
    C, B, A, F = P(*Cw), P(*Bw), P(*Aw), P(*Fw)
    cv = Canvas(w, h, title="Diện tích tam giác theo hai cạnh và góc xen giữa",
                desc="Tam giác ABC với đường cao hạ từ A xuống đường thẳng CB; đường cao này bằng b nhân sin C.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    cv.line(*A, *F, cls="accent-b", extra=_stroke(2.2, "6 4"))
    _right_angle_at(cv, F, C, A, size=11)
    _angle_at(cv, C, B, A, r=32, label="C", lgap=15)
    _label_vertices(cv, A, B, C)
    cv.text((C[0] + B[0]) / 2, C[1] + 22, "a", cls="lbl", anchor="middle")
    _side_label(cv, C, A, B, "b")
    # Trên hình chỉ ghi "h", còn "h = b·sin C" để dành cho chú thích. Khi góc C
    # tù thì chân đường cao rơi ra NGOÀI đoạn CB, sát mép trái khung: một nhãn
    # dài đặt ở đó hoặc bị lề cắt cụt, hoặc chui vào chỗ nhãn cạnh b.
    outward = 11.0 if F[0] >= C[0] else -11.0
    cv.text(A[0] + outward, (A[1] + F[1]) / 2, "h", cls="lbl",
            anchor="start" if outward > 0 else "end")
    _caption(cv, w, h - 16,
             str(p.get("caption", "h = b·sin C  ⇒  S = ½·a·h = ½·a·b·sin C")))
    return cv.render()


def build_lg_duong_tron_noi_tiep(p: Params) -> str:
    """Đường tròn nội tiếp bán kính r: S = p·r (p là nửa chu vi)."""
    b = _clamp(_f(p.get("b", 5.2), 5.2), 0.6, 30)
    c = _clamp(_f(p.get("c", 6.6), 6.6), 0.6, 30)
    A_deg = _clamp(_f(p.get("A", 62), 62), 20, 140)
    Aw, Bw, Cw = _tri_bcA(b, c, A_deg)
    a = math.dist(Bw, Cw)
    per = a + b + c
    Iw = ((a * Aw[0] + b * Bw[0] + c * Cw[0]) / per,
          (a * Aw[1] + b * Bw[1] + c * Cw[1]) / per)
    s = per / 2
    area = max(1e-9, s * (s - a) * (s - b) * (s - c)) ** 0.5
    r = area / s
    scale = 244.0 / max(b, c)
    w, h, P = _fit((Aw, Bw, Cw), scale, 76.0, 76.0, 66.0, 76.0)
    A, B, C, I = P(*Aw), P(*Bw), P(*Cw), P(*Iw)
    cv = Canvas(w, h, title="Đường tròn nội tiếp tam giác",
                desc="Tam giác ABC và đường tròn nội tiếp tâm I bán kính r tiếp xúc ba cạnh.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    cv.circle(I[0], I[1], r * scale, cls="accent-c", extra=_stroke(2))
    cv.dot(*I, r=3.2, cls="accent-c")
    cv.text(I[0] + 8, I[1] + 15, "I", cls="lbl")
    # Bán kính vẽ vuông góc xuống AB (nằm trên trục hoành thế giới) — tiếp điểm thật.
    Tw = (Iw[0], 0.0)
    T = P(*Tw)
    cv.line(*I, *T, cls="accent-b", extra=_stroke(2.4))
    _right_angle_at(cv, T, I, B, size=10)
    cv.text((I[0] + T[0]) / 2 + 8, (I[1] + T[1]) / 2 + 4, "r", cls="lbl")
    _label_vertices(cv, A, B, C)
    _caption(cv, w, h - 16, str(p.get("caption", "S = p·r  với  p = (a + b + c)/2")))
    return cv.render()


_CEVA_KINDS = ("duong-cao", "trung-tuyen", "phan-giac", "ba-trung-tuyen")


def build_lg_tam_giac_duong_dac_biet(p: Params) -> str:
    """Đường cao, trung tuyến hoặc phân giác kẻ từ đỉnh A của tam giác ABC."""
    kind = str(p.get("kind", "trung-tuyen"))
    if kind not in _CEVA_KINDS:
        kind = "trung-tuyen"
    b = _clamp(_f(p.get("b", 5.0), 5.0), 0.6, 30)
    c = _clamp(_f(p.get("c", 6.8), 6.8), 0.6, 30)
    A_deg = _clamp(_f(p.get("A", 66), 66), 20, 140)
    Aw, Bw, Cw = _tri_bcA(b, c, A_deg)
    # Dựng lại với BC nằm ngang cho dễ đọc: quay hệ sao cho B, C cùng tung độ.
    ang = math.atan2(Cw[1] - Bw[1], Cw[0] - Bw[0])
    ca, sa = math.cos(-ang), math.sin(-ang)

    def rot(q: Pt) -> Pt:
        x, y = q[0] - Bw[0], q[1] - Bw[1]
        return (x * ca - y * sa, x * sa + y * ca)

    Aw, Bw, Cw = rot(Aw), rot(Bw), rot(Cw)
    if Aw[1] < 0:
        Aw, Bw, Cw = (Aw[0], -Aw[1]), (Bw[0], -Bw[1]), (Cw[0], -Cw[1])
    a = math.dist(Bw, Cw)

    # Nhãn viết dạng (gốc, chỉ số) để vẽ bằng <tspan>; chú thích thì diễn đạt
    # bằng lời, vì một dòng chữ chạy ngang không có chỗ cho chỉ số dưới.
    if kind == "duong-cao":
        Fw = (Aw[0], Bw[1])
        label, cap = ("h", "a"), "S = ½·a·h  (h là đường cao ứng với cạnh a)"
    elif kind == "phan-giac":
        # Chân phân giác chia BC theo tỉ số c : b (tính chất đường phân giác).
        tt = c / (b + c)
        Fw = (Bw[0] + (Cw[0] - Bw[0]) * tt, Bw[1] + (Cw[1] - Bw[1]) * tt)
        label, cap = ("l", "a"), "DB / DC = AB / AC = c / b"
    else:
        Fw = ((Bw[0] + Cw[0]) / 2, (Bw[1] + Cw[1]) / 2)
        label, cap = ("m", "a"), "Trung tuyến kẻ từ A: 4m² = 2(b² + c²) − a²"

    extra_pts: list[Pt] = []
    if kind == "ba-trung-tuyen":
        Mb = ((Aw[0] + Cw[0]) / 2, (Aw[1] + Cw[1]) / 2)
        Mc = ((Aw[0] + Bw[0]) / 2, (Aw[1] + Bw[1]) / 2)
        extra_pts = [Mb, Mc]
        cap = "Tổng bình phương ba trung tuyến bằng ¾(a² + b² + c²)"

    scale = 250.0 / max(a, b, c)
    w, h, P = _fit([Aw, Bw, Cw, Fw] + extra_pts, scale, 74.0, 74.0, 64.0, 78.0)
    A, B, C, F = P(*Aw), P(*Bw), P(*Cw), P(*Fw)
    cv = Canvas(w, h, title=f"Tam giác ABC: {kind.replace('-', ' ')}",
                desc="Tam giác ABC và đường đặc biệt kẻ từ đỉnh A xuống cạnh BC.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    _label_vertices(cv, A, B, C)
    # Nhãn cạnh a đặt ở 1/4 đoạn BC chứ không ở giữa: giữa BC là chỗ chân trung
    # tuyến (và gần chân phân giác), nên nhãn cạnh và tên chân đường đè lên nhau.
    cv.text(B[0] + (C[0] - B[0]) * 0.25, B[1] + 22, "a", cls="lbl", anchor="middle")
    _side_label(cv, A, C, B, "b")
    _side_label(cv, A, B, C, "c")

    if kind == "ba-trung-tuyen":
        Mb, Mc = P(*extra_pts[0]), P(*extra_pts[1])
        for Q, src, sub in ((F, A, "a"), (Mb, B, "b"), (Mc, C, "c")):
            cv.line(*src, *Q, cls="accent-b", extra=_stroke(2.2))
            cv.dot(*Q, r=3, cls="accent-b")
            _sub(cv, (src[0] + Q[0]) / 2 + 8, (src[1] + Q[1]) / 2, "m", sub, cls="lbl-sm")
    else:
        cv.line(*A, *F, cls="accent-b", extra=_stroke(2.6))
        cv.dot(*F, r=3.2, cls="accent-b")
        cv.text(F[0], F[1] + 20, "M" if kind == "trung-tuyen" else ("H" if kind == "duong-cao" else "D"),
                cls="lbl", anchor="middle")
        _sub(cv, (A[0] + F[0]) / 2 + 9, (A[1] + F[1]) / 2, label[0], label[1])
        if kind == "duong-cao":
            _right_angle_at(cv, F, B, A, size=11)
        if kind == "trung-tuyen":
            for (P1, P2) in ((B, F), (F, C)):
                mid = ((P1[0] + P2[0]) / 2, (P1[1] + P2[1]) / 2)
                cv.line(mid[0], mid[1] - 6, mid[0], mid[1] + 6, cls="accent-c", extra=_stroke(2))
        if kind == "phan-giac":
            # Hai cung CÙNG bán kính: vẽ lệch bán kính là ngầm bảo hai góc khác
            # nhau, đúng ngược với điều hình này muốn nói.
            _angle_at(cv, A, B, F, r=32, cls="accent-c")
            _angle_at(cv, A, F, C, r=32, cls="accent-c")
    _caption(cv, w, h - 16, str(p.get("caption", cap)))
    return cv.render()


def build_lg_tam_giac_deu(p: Params) -> str:
    """Tam giác đều cạnh a: đường cao, đường tròn nội tiếp và ngoại tiếp."""
    a = _clamp(_f(p.get("a", 6), 6), 0.5, 40)
    hgt = a * math.sqrt(3) / 2
    Bw, Cw = (0.0, 0.0), (a, 0.0)
    Aw = (a / 2, hgt)
    Gw = (a / 2, hgt / 3)
    Rr = a * math.sqrt(3) / 3
    scale = 236.0 / max(a, 2 * Rr)
    w, h, P = _fit([Bw, Cw, Aw, (a / 2, hgt / 3 + Rr), (a / 2, hgt / 3 - Rr)],
                   scale, 70.0, 70.0, 62.0, 74.0)
    A, B, C, G = P(*Aw), P(*Bw), P(*Cw), P(*Gw)
    Fw = (a / 2, 0.0)
    F = P(*Fw)
    cv = Canvas(w, h, title="Tam giác đều cạnh a",
                desc="Tam giác đều với đường cao, đường tròn nội tiếp bán kính r và đường tròn ngoại tiếp bán kính R.")
    cv.circle(G[0], G[1], Rr * scale, cls="ink-thin", extra=' stroke-dasharray="6 5"')
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    cv.circle(G[0], G[1], (Rr / 2) * scale, cls="accent-c", extra=_stroke(1.8))
    cv.line(*A, *F, cls="accent-b", extra=_stroke(2.2, "6 4"))
    _right_angle_at(cv, F, B, A, size=10)
    cv.dot(*G, r=3, cls="accent-d")
    # Bán kính ngoại tiếp kẻ tới đỉnh C chứ không tới A: GA nằm TRÙNG đường cao
    # AF nên đoạn R vẽ đè lên đoạn h, và người xem thấy một nét thay vì hai.
    cv.line(*G, *C, cls="accent-d", extra=_stroke(2))
    cv.text((G[0] + C[0]) / 2, (G[1] + C[1]) / 2 - 8, "R", cls="lbl", anchor="middle")
    cv.text((G[0] + F[0]) / 2 + 9, (G[1] + F[1]) / 2, "r", cls="lbl")
    _label_vertices(cv, A, B, C)
    cv.text((B[0] + C[0]) / 2, B[1] + 22, f"a = {_num(a)}", cls="lbl", anchor="middle")
    cv.text(A[0] - 12, (A[1] + F[1]) / 2, "h", cls="lbl", anchor="end")
    _caption(cv, w, h - 16,
             str(p.get("caption", "h = a√3/2 · S = a²√3/4 · R = a√3/3 · r = a√3/6")))
    return cv.render()


def build_lg_tu_giac_duong_cheo(p: Params) -> str:
    """Tứ giác có hai đường chéo d₁, d₂ cắt nhau dưới góc φ: S = ½·d₁·d₂·sin φ."""
    d1 = _clamp(_f(p.get("d1", 6.4), 6.4), 0.6, 30)
    d2 = _clamp(_f(p.get("d2", 5.0), 5.0), 0.6, 30)
    phi = _clamp(_f(p.get("phi", 62), 62), 15, 165)
    t1 = _clamp(_f(p.get("t1", 0.42), 0.42), 0.2, 0.8)   # giao điểm chia d₁
    t2 = _clamp(_f(p.get("t2", 0.55), 0.55), 0.2, 0.8)
    Iw = (0.0, 0.0)
    Aw = (-d1 * t1, 0.0)
    Cw = (d1 * (1 - t1), 0.0)
    pr = math.radians(phi)
    Bw = (d2 * t2 * math.cos(pr), d2 * t2 * math.sin(pr))
    Dw = (-d2 * (1 - t2) * math.cos(pr), -d2 * (1 - t2) * math.sin(pr))
    scale = 230.0 / max(d1, d2)
    w, h, P = _fit([Aw, Bw, Cw, Dw], scale, 72.0, 72.0, 62.0, 74.0)
    A, B, C, D, I = P(*Aw), P(*Bw), P(*Cw), P(*Dw), P(*Iw)
    cv = Canvas(w, h, title="Tứ giác với hai đường chéo",
                desc="Tứ giác ABCD có hai đường chéo AC và BD cắt nhau tại I dưới góc phi.")
    cv.polygon([A, B, C, D], cls="fill-a")
    cv.polyline([A, B, C, D, A], cls="ink")
    cv.line(*A, *C, cls="accent-b", extra=_stroke(2.4))
    cv.line(*B, *D, cls="accent-c", extra=_stroke(2.4))
    _angle_at(cv, I, C, B, r=26, label="φ", lgap=14)
    cv.dot(*I, r=3, cls="accent-d")
    for pt, name in ((A, "A"), (B, "B"), (C, "C"), (D, "D")):
        dx, dy = pt[0] - I[0], pt[1] - I[1]
        d = math.hypot(dx, dy) or 1.0
        cv.text(pt[0] + 15 * dx / d, pt[1] + 15 * dy / d + 4, name, cls="lbl", anchor="middle")
    cv.text((A[0] + I[0]) / 2, A[1] - 10, "d₁", cls="lbl", anchor="middle")
    cv.text((B[0] + I[0]) / 2 + 12, (B[1] + I[1]) / 2, "d₂", cls="lbl")
    _caption(cv, w, h - 16, str(p.get("caption", "S = ½·d₁·d₂·sin φ")))
    return cv.render()


# --------------------------------------------------------------------------
# 5. Vectơ phẳng
# --------------------------------------------------------------------------
def _vec_canvas(pts: Sequence[Pt], scale: float = 46.0, pad: float = 56.0,
                pad_b: float = 68.0) -> tuple[float, float, Callable[[float, float], Pt]]:
    return _fit(list(pts) + [(0.0, 0.0)], scale, pad, pad + 24.0, pad, pad_b)


def build_vt_tong(p: Params) -> str:
    """Cộng hai vectơ: quy tắc hình bình hành hoặc quy tắc ba điểm (nối đuôi)."""
    rule = str(p.get("rule", "hbh"))
    if rule not in ("hbh", "tam-giac"):
        rule = "hbh"
    ux, uy = _f(p.get("ux", 3.2), 3.2), _f(p.get("uy", 0.9), 0.9)
    vx, vy = _f(p.get("vx", 1.1), 1.1), _f(p.get("vy", 2.4), 2.4)
    if math.hypot(ux, uy) < 0.2 or math.hypot(vx, vy) < 0.2:
        ux, uy, vx, vy = 3.2, 0.9, 1.1, 2.4
    lu = str(p.get("label_u", "u"))
    lv = str(p.get("label_v", "v"))
    ls = str(p.get("label_sum", "u + v"))
    caption = str(p.get("caption", ""))
    w, h, P = _vec_canvas([(ux, uy), (vx, vy), (ux + vx, uy + vy)])
    O, U, V, W = P(0, 0), P(ux, uy), P(vx, vy), P(ux + vx, uy + vy)
    cv = Canvas(w, h, title="Cộng hai vectơ",
                desc="Tổng hai vectơ dựng theo quy tắc hình bình hành hoặc quy tắc ba điểm.")
    if rule == "hbh":
        cv.polygon([O, U, W, V], cls="fill-a")
        cv.line(*U, *W, cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.line(*V, *W, cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.arrow(*O, *U, cls="accent-a", head=9)
        cv.arrow(*O, *V, cls="accent-c", head=9)
        cv.text(U[0] + 7, U[1] - 5, lu, cls="lbl")
        cv.text(V[0] - 7, V[1] - 5, lv, cls="lbl", anchor="end")
        names = p.get("vertices")
        if isinstance(names, (list, tuple)) and len(names) == 4:
            for pt, nm, anc in ((O, names[0], "end"), (U, names[1], "start"),
                                (W, names[2], "start"), (V, names[3], "end")):
                cv.text(pt[0] + (8 if anc == "start" else -8), pt[1] + 16, str(nm),
                        cls="lbl-sm", anchor=anc)
    else:
        cv.arrow(*O, *U, cls="accent-a", head=9)
        cv.arrow(*U, *W, cls="accent-c", head=9)
        cv.text((O[0] + U[0]) / 2, (O[1] + U[1]) / 2 - 9, lu, cls="lbl", anchor="middle")
        cv.text((U[0] + W[0]) / 2 + 9, (U[1] + W[1]) / 2, lv, cls="lbl")
        names = p.get("vertices")
        if isinstance(names, (list, tuple)) and len(names) >= 3:
            for pt, nm, anc in ((O, names[0], "end"), (U, names[1], "start"), (W, names[2], "start")):
                cv.text(pt[0] + (8 if anc == "start" else -8), pt[1] + 16, str(nm),
                        cls="lbl-sm", anchor=anc)
    cv.arrow(*O, *W, cls="accent-b", head=10)
    cv.text(W[0] + 7, W[1] - 5, ls, cls="lbl")
    cv.dot(*O, r=3, cls="ink")
    _caption(cv, w, h - 18, caption)
    return cv.render()


def build_vt_hieu(p: Params) -> str:
    """Quy tắc trừ: OB − OA = AB (hiệu hai vectơ chung gốc là vectơ nối hai ngọn)."""
    ax, ay = _f(p.get("ax", 1.2), 1.2), _f(p.get("ay", 2.3), 2.3)
    bx, by = _f(p.get("bx", 3.4), 3.4), _f(p.get("by", 0.9), 0.9)
    if math.hypot(bx - ax, by - ay) < 0.3:
        ax, ay, bx, by = 1.2, 2.3, 3.4, 0.9
    w, h, P = _vec_canvas([(ax, ay), (bx, by)])
    O, A, B = P(0, 0), P(ax, ay), P(bx, by)
    cv = Canvas(w, h, title="Hiệu hai vectơ chung gốc",
                desc="Hai vectơ OA và OB chung gốc O; hiệu của chúng là vectơ AB nối ngọn A tới ngọn B.")
    cv.polygon([O, A, B], cls="fill-a")
    cv.arrow(*O, *A, cls="accent-a", head=9)
    cv.arrow(*O, *B, cls="accent-c", head=9)
    cv.arrow(*A, *B, cls="accent-b", head=10)
    cv.dot(*O, r=3, cls="ink")
    cv.text(O[0] - 8, O[1] + 17, "O", cls="lbl", anchor="end")
    cv.text(A[0] - 8, A[1] - 6, "A", cls="lbl", anchor="end")
    cv.text(B[0] + 8, B[1] - 6, "B", cls="lbl")
    cv.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 - 9, "AB", cls="lbl", anchor="middle")
    _caption(cv, w, h - 18, str(p.get("caption", "OB − OA = AB")))
    return cv.render()


def build_vt_nhan_so(p: Params) -> str:
    """Nhân vectơ với một số k: cùng phương, độ dài nhân |k|, đổi chiều khi k < 0.

    Hai vectơ vẽ trên hai đường song song lệch nhau chứ không chung gốc: chồng
    lên nhau thì không nhìn ra cái nào dài hơn cái nào.
    """
    ax, ay = _f(p.get("ax", 2.4), 2.4), _f(p.get("ay", 1.1), 1.1)
    if math.hypot(ax, ay) < 0.2:
        ax, ay = 2.4, 1.1
    k = _clamp(_f(p.get("k", 2), 2), -3.5, 3.5)
    if abs(k) < 0.15:
        k = 2.0
    la = str(p.get("label_a", "a"))
    lk = str(p.get("label_ka", f"{_num(k)}·a"))
    L = math.hypot(ax, ay)
    nx, ny = -ay / L, ax / L                      # pháp tuyến để tách hai đường
    off = 1.05
    p0 = (nx * off, ny * off)
    p1 = (p0[0] + ax, p0[1] + ay)
    q0 = (-nx * off, -ny * off)
    q1 = (q0[0] + k * ax, q0[1] + k * ay)
    w, h, P = _fit([p0, p1, q0, q1, (0.0, 0.0)], 44.0, 64.0, 88.0, 60.0, 72.0)
    cv = Canvas(w, h, title=f"Nhân vectơ với số k = {_num(k)}",
                desc="Vectơ a và vectơ k·a vẽ song song để so sánh hướng và độ dài.")
    cv.arrow(*P(*p0), *P(*p1), cls="accent-a", head=9)
    cv.arrow(*P(*q0), *P(*q1), cls="accent-b", head=9)
    m1 = P((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2)
    m2 = P((q0[0] + q1[0]) / 2, (q0[1] + q1[1]) / 2)
    cv.text(m1[0], m1[1] - 9, la, cls="lbl", anchor="middle")
    cv.text(m2[0], m2[1] + 18, lk, cls="lbl", anchor="middle")
    cap = "k > 0: cùng hướng · |k·a| = |k|·|a|" if k > 0 else "k < 0: ngược hướng · |k·a| = |k|·|a|"
    _caption(cv, w, h - 18, str(p.get("caption", cap)))
    return cv.render()


def build_vt_thang_hang(p: Params) -> str:
    """Ba điểm thẳng hàng: AB = k·AC (hai vectơ cùng phương chung gốc A)."""
    k = _clamp(_f(p.get("k", 0.62), 0.62), -1.6, 1.6)
    if abs(k) < 0.15:
        k = 0.62
    cx, cy = _f(p.get("cx", 4.4), 4.4), _f(p.get("cy", 1.8), 1.8)
    if math.hypot(cx, cy) < 0.4:
        cx, cy = 4.4, 1.8
    Aw = (0.0, 0.0)
    Cw = (cx, cy)
    Bw = (k * cx, k * cy)
    L = math.hypot(cx, cy)
    nx, ny = -cy / L, cx / L
    w, h, P = _fit([Aw, Bw, Cw, (nx * 0.9, ny * 0.9),
                    (Cw[0] - nx * 0.9, Cw[1] - ny * 0.9)], 46.0, 66.0, 76.0, 66.0, 74.0)
    A, B, C = P(*Aw), P(*Bw), P(*Cw)
    cv = Canvas(w, h, title="Ba điểm thẳng hàng",
                desc="Ba điểm A, B, C cùng nằm trên một đường thẳng; vectơ AB bằng k lần vectơ AC.")
    cv.line(A[0] - (C[0] - A[0]) * 0.12, A[1] - (C[1] - A[1]) * 0.12,
            C[0] + (C[0] - A[0]) * 0.12, C[1] + (C[1] - A[1]) * 0.12,
            cls="ink-thin", extra=' stroke-dasharray="6 5"')
    off = (nx * 0.62, ny * 0.62)
    cv.arrow(*P(off[0], off[1]), *P(Bw[0] + off[0], Bw[1] + off[1]), cls="accent-a", head=9)
    cv.arrow(*P(-off[0], -off[1]), *P(Cw[0] - off[0], Cw[1] - off[1]), cls="accent-b", head=9)
    for pt, nm in ((A, "A"), (B, "B"), (C, "C")):
        cv.dot(*pt, r=3.4, cls="ink")
        cv.text(pt[0], pt[1] + 19, nm, cls="lbl", anchor="middle")
    m1 = P(Bw[0] / 2 + off[0], Bw[1] / 2 + off[1])
    m2 = P(Cw[0] / 2 - off[0], Cw[1] / 2 - off[1])
    cv.text(m1[0], m1[1] - 9, "AB", cls="lbl", anchor="middle")
    cv.text(m2[0], m2[1] + 18, "AC", cls="lbl", anchor="middle")
    _caption(cv, w, h - 18, str(p.get("caption", f"AB = k·AC  (k = {_num(k)})")))
    return cv.render()


def build_vt_tich_vo_huong(p: Params) -> str:
    """Tích vô hướng: góc giữa hai vectơ và hình chiếu của b lên phương của a."""
    la = _clamp(_f(p.get("len_a", 4.2), 4.2), 0.8, 9)
    lb = _clamp(_f(p.get("len_b", 3.0), 3.0), 0.8, 9)
    phi = _clamp(_f(p.get("phi", 52), 52), 0, 180)
    show_coords = bool(p.get("show_coords", False))
    Aw = (la, 0.0)
    Bw = (lb * math.cos(math.radians(phi)), lb * math.sin(math.radians(phi)))
    Fw = (Bw[0], 0.0)                              # chân hình chiếu của b lên Ox
    w, h, P, box = _frame_with_axes([(0.0, 0.0), Aw, Bw, Fw], 48.0, 74.0, 92.0, 72.0, 76.0, 0.7)
    O, A, B, F = P(0, 0), P(*Aw), P(*Bw), P(*Fw)
    cv = Canvas(w, h, title="Tích vô hướng của hai vectơ",
                desc="Hai vectơ chung gốc hợp với nhau góc phi; hình chiếu của vectơ b lên phương của a có độ dài bằng b nhân cos phi.")
    if show_coords:
        _axes(cv, P, *box)
    if abs(phi - 90) < 0.5:
        _right_angle_at(cv, O, A, B, size=15)
        cap_default = "a ⊥ b ⇔ a·b = 0"
    else:
        _angle_at(cv, O, A, B, r=34, label="φ", lgap=16)
        cap_default = "a·b = |a|·|b|·cos φ"
    if abs(phi - 90) > 0.5:
        cv.line(*B, *F, cls="ink-thin", extra=' stroke-dasharray="4 3"')
        _right_angle_at(cv, F, O, B, size=10)
        cv.text((O[0] + F[0]) / 2, O[1] + 21, "|b|·cos φ", cls="lbl-sm", anchor="middle")
    cv.arrow(*O, *A, cls="accent-a", head=9)
    cv.arrow(*O, *B, cls="accent-c", head=9)
    if abs(phi - 90) > 0.5:
        # Đoạn hình chiếu vẽ SAU vectơ a, vì nó nằm chồng lên chính vectơ a khi
        # φ nhọn; vẽ trước thì màu nhấn bị nét xanh phủ mất, hình chiếu biến mất.
        cv.line(*O, *F, cls="accent-d", extra=_stroke(4.2))
    cv.text(A[0] + 8, A[1] - 6, "a", cls="lbl")
    cv.text(B[0] + 8, B[1] - 6, "b", cls="lbl")
    cv.dot(*O, r=3, cls="ink")
    if show_coords:
        cv.text(A[0] + 8, A[1] + 15, "(x₁; y₁)", cls="lbl-sm")
        cv.text(B[0] + 8, B[1] + 12, "(x₂; y₂)", cls="lbl-sm")
        cap_default = "a·b = x₁x₂ + y₁y₂"
    _caption(cv, w, h - 18, str(p.get("caption", cap_default)))
    return cv.render()


def build_vt_phan_tich(p: Params) -> str:
    """Phân tích một vectơ theo hai phương không cùng phương: x = m·a + n·b."""
    ax, ay = _f(p.get("ax", 2.6), 2.6), _f(p.get("ay", 0.5), 0.5)
    bx, by = _f(p.get("bx", 0.8), 0.8), _f(p.get("by", 2.2), 2.2)
    m = _clamp(_f(p.get("m", 1.5), 1.5), -2.5, 2.5)
    n = _clamp(_f(p.get("n", 1.2), 1.2), -2.5, 2.5)
    if abs(ax * by - ay * bx) < 0.25:              # hai phương gần trùng thì không phân tích được
        ax, ay, bx, by = 2.6, 0.5, 0.8, 2.2
    if abs(m) < 0.2:
        m = 1.5
    if abs(n) < 0.2:
        n = 1.2
    Ma = (m * ax, m * ay)
    Nb = (n * bx, n * by)
    X = (Ma[0] + Nb[0], Ma[1] + Nb[1])
    w, h, P = _fit([(0.0, 0.0), (ax, ay), (bx, by), Ma, Nb, X], 44.0, 70.0, 92.0, 66.0, 76.0)
    O = P(0, 0)
    cv = Canvas(w, h, title="Phân tích vectơ theo hai phương",
                desc="Vectơ x viết thành tổng của m lần vectơ a và n lần vectơ b.")
    cv.polygon([O, P(*Ma), P(*X), P(*Nb)], cls="fill-a")
    cv.line(*P(*Ma), *P(*X), cls="ink-thin", extra=' stroke-dasharray="5 4"')
    cv.line(*P(*Nb), *P(*X), cls="ink-thin", extra=' stroke-dasharray="5 4"')
    cv.arrow(*O, *P(ax, ay), cls="accent-a", head=8)
    cv.arrow(*O, *P(bx, by), cls="accent-c", head=8)
    cv.arrow(*O, *P(*Ma), cls="accent-a", head=9)
    cv.arrow(*O, *P(*Nb), cls="accent-c", head=9)
    cv.arrow(*O, *P(*X), cls="accent-b", head=10)
    pa, pb = P(ax, ay), P(bx, by)
    cv.text(pa[0] + 7, pa[1] + 16, "a", cls="lbl")
    cv.text(pb[0] - 7, pb[1] + 14, "b", cls="lbl", anchor="end")
    cv.text(P(*Ma)[0] + 7, P(*Ma)[1] - 6, "m·a", cls="lbl-sm")
    cv.text(P(*Nb)[0] - 7, P(*Nb)[1] - 6, "n·b", cls="lbl-sm", anchor="end")
    cv.text(P(*X)[0] + 8, P(*X)[1] - 6, "x", cls="lbl")
    cv.dot(*O, r=3, cls="ink")
    _caption(cv, w, h - 18, str(p.get("caption", f"x = m·a + n·b  (m = {_num(m)}, n = {_num(n)})")))
    return cv.render()


def build_vt_diem_dac_biet(p: Params) -> str:
    """Hệ thức vectơ cho trung điểm, trọng tâm hoặc trung tuyến."""
    kind = str(p.get("kind", "trung-diem"))
    if kind not in ("trung-diem", "trong-tam", "trung-tuyen"):
        kind = "trung-diem"
    if kind == "trung-diem":
        Aw, Bw = (-2.4, 0.0), (2.4, 0.0)
        Iw = ((Aw[0] + Bw[0]) / 2, (Aw[1] + Bw[1]) / 2)
        Mw = (0.6, 2.5)
        w, h, P = _fit([Aw, Bw, Iw, Mw], 52.0, 68.0, 68.0, 62.0, 76.0)
        A, B, I, M = P(*Aw), P(*Bw), P(*Iw), P(*Mw)
        cv = Canvas(w, h, title="Hệ thức vectơ trung điểm",
                    desc="I là trung điểm của đoạn AB; hai vectơ IA và IB đối nhau.")
        cv.line(*A, *B, cls="ink")
        for pt, nm in ((A, "A"), (B, "B"), (I, "I"), (M, "M")):
            cv.dot(*pt, r=3.4, cls="ink")
            cv.text(pt[0], pt[1] + (20 if nm != "M" else -10), nm, cls="lbl", anchor="middle")
        cv.arrow(I[0], I[1] - 16, A[0], A[1] - 16, cls="accent-a", head=8)
        cv.arrow(I[0], I[1] - 16, B[0], B[1] - 16, cls="accent-b", head=8)
        for tgt, cls in ((A, "accent-a"), (B, "accent-b"), (I, "accent-d")):
            cv.line(*M, *tgt, cls=cls, extra=_stroke(1.6, "5 4"))
        _caption(cv, w, h - 18,
                 str(p.get("caption", "IA + IB = 0  ⇔  MA + MB = 2·MI  (mọi điểm M)")))
        return cv.render()

    Aw, Bw, Cw = (0.0, 3.0), (-2.6, -1.4), (2.9, -1.2)
    Mw = ((Bw[0] + Cw[0]) / 2, (Bw[1] + Cw[1]) / 2)
    Gw = ((Aw[0] + Bw[0] + Cw[0]) / 3, (Aw[1] + Bw[1] + Cw[1]) / 3)
    w, h, P = _fit([Aw, Bw, Cw, Mw, Gw], 50.0, 70.0, 70.0, 62.0, 76.0)
    A, B, C, M, G = P(*Aw), P(*Bw), P(*Cw), P(*Mw), P(*Gw)
    cv = Canvas(w, h, title="Hệ thức vectơ trong tam giác",
                desc="Tam giác ABC với trung điểm M của BC và trọng tâm G.")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    for pt, nm, dy in ((A, "A", -10), (B, "B", 20), (C, "C", 20), (M, "M", 20)):
        cv.dot(*pt, r=3.2, cls="ink")
        cv.text(pt[0], pt[1] + dy, nm, cls="lbl", anchor="middle")
    if kind == "trung-tuyen":
        cv.arrow(*A, *B, cls="accent-a", head=9)
        cv.arrow(*A, *C, cls="accent-c", head=9)
        cv.arrow(*A, *M, cls="accent-b", head=10)
        cv.text((A[0] + M[0]) / 2 + 9, (A[1] + M[1]) / 2, "AM", cls="lbl")
        _caption(cv, w, h - 18, str(p.get("caption", "AM = ½·(AB + AC)")))
    else:
        cv.line(*A, *M, cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.line(*B, *P((Aw[0] + Cw[0]) / 2, (Aw[1] + Cw[1]) / 2),
                cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.line(*C, *P((Aw[0] + Bw[0]) / 2, (Aw[1] + Bw[1]) / 2),
                cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.arrow(*G, *A, cls="accent-a", head=8)
        cv.arrow(*G, *B, cls="accent-c", head=8)
        cv.arrow(*G, *C, cls="accent-b", head=8)
        cv.dot(*G, r=3.6, cls="accent-d")
        cv.text(G[0] + 10, G[1] + 14, "G", cls="lbl")
        _caption(cv, w, h - 18, str(p.get("caption", "GA + GB + GC = 0")))
    return cv.render()


# --------------------------------------------------------------------------
# 6. Số phức trên mặt phẳng Argand
# --------------------------------------------------------------------------
def _argand(cv: Canvas, P: Callable[[float, float], Pt], xlo: float, xhi: float,
            ylo: float, yhi: float) -> None:
    _axes(cv, P, xlo, xhi, ylo, yhi, xlabel="Re", ylabel="Im")


def build_sp_diem_bieu_dien(p: Params) -> str:
    """Điểm biểu diễn số phức z = a + bi, môđun r = |z| và acgumen φ."""
    a = _f(p.get("a", 3), 3)
    b = _f(p.get("b", 2.2), 2.2)
    if math.hypot(a, b) < 0.4:
        a, b = 3.0, 2.2
    r = math.hypot(a, b)
    phi = math.degrees(math.atan2(b, a))
    # Chừa sẵn một đoạn trục thực dương dài bằng |a|: acgumen đo TỪ tia Ox dương,
    # nên phần âm mà không có phần dương thì cung góc φ chạy ra ngoài khung trục.
    w, h, P, box = _frame_with_axes([(0.0, 0.0), (a, b), (a, 0.0), (0.0, b),
                                     (max(abs(a), 1.2), 0.0)],
                                    58.0, 66.0, 96.0, 62.0, 76.0, 0.7)
    O, M = P(0, 0), P(a, b)
    cv = Canvas(w, h, title="Điểm biểu diễn số phức",
                desc="Số phức z = a + bi ứng với điểm M(a; b) trên mặt phẳng toạ độ; môđun là độ dài OM, acgumen là góc giữa tia OM và trục thực.")
    _argand(cv, P, *box)
    cv.line(*M, *P(a, 0), cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.line(*M, *P(0, b), cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.arrow(*O, *M, cls="accent-a", head=9)
    cv.dot(*M, r=3.8, cls="accent-a")
    _angle_at(cv, O, P(max(abs(a), 1.0), 0), M, r=30, label="φ", lgap=15)
    cv.text(M[0] + 9 * (1 if a >= 0 else -1), M[1] - 8, "M(a; b)", cls="lbl",
            anchor="start" if a >= 0 else "end")
    # Nhãn môđun đẩy theo pháp tuyến của OM: lệch cứng sang trái thì với a < 0
    # (vectơ hướng lên-trái) nó nằm đúng trên nét vectơ.
    mnx, mny = -(M[1] - O[1]), M[0] - O[0]
    ml = math.hypot(mnx, mny) or 1.0
    if mnx > 0:                                  # luôn đẩy sang phía trái-trên
        mnx, mny = -mnx, -mny
    cv.text((O[0] + M[0]) / 2 + 16 * mnx / ml, (O[1] + M[1]) / 2 + 16 * mny / ml + 4,
            "r = |z|", cls="lbl-sm", anchor="middle")
    cv.text(P(a, 0)[0], P(a, 0)[1] + 17, "a", cls="lbl", anchor="middle")
    # Nhãn b nằm về phía ĐỐI DIỆN M so với trục Oy, nếu không thì nó đè lên chính
    # đoạn nét đứt nối M với trục ảo.
    cv.text(P(0, b)[0] + (-9 if a >= 0 else 9), P(0, b)[1] + 4, "b", cls="lbl",
            anchor="end" if a >= 0 else "start")
    _caption(cv, w, h - 18,
             str(p.get("caption", f"z = a + bi,  r = √(a² + b²) = {_num(r)},  φ ≈ {_num(phi)}°")))
    return cv.render()


def build_sp_lien_hop(p: Params) -> str:
    """Số phức liên hợp: z và z̄ đối xứng nhau qua trục thực."""
    a = _f(p.get("a", 3), 3)
    b = _f(p.get("b", 2.2), 2.2)
    if abs(b) < 0.4:
        b = 2.2
    if abs(a) < 0.2:
        a = 3.0
    w, h, P, box = _frame_with_axes([(0.0, 0.0), (a, b), (a, -b)],
                                    56.0, 66.0, 96.0, 60.0, 76.0, 0.8)
    O, M, N = P(0, 0), P(a, b), P(a, -b)
    cv = Canvas(w, h, title="Số phức liên hợp",
                desc="Điểm biểu diễn của z và của số phức liên hợp đối xứng nhau qua trục thực.")
    _argand(cv, P, *box)
    cv.line(*M, *N, cls="accent-d", extra=_stroke(1.8, "5 4"))
    cv.arrow(*O, *M, cls="accent-a", head=9)
    cv.arrow(*O, *N, cls="accent-b", head=9)
    cv.dot(*M, r=3.6, cls="accent-a")
    cv.dot(*N, r=3.6, cls="accent-b")
    cv.text(M[0] + 9, M[1] - 7, "M(a; b) ↔ z", cls="lbl")
    cv.text(N[0] + 9, N[1] + 14, "M′(a; −b) ↔ z̄", cls="lbl")
    mid = ((M[0] + N[0]) / 2, (M[1] + N[1]) / 2)
    _right_angle_at(cv, mid, M, P(a - max(abs(a), 1) * 0.4, 0), size=10)
    _caption(cv, w, h - 18, str(p.get("caption", "z̄ = a − bi · |z̄| = |z| · z·z̄ = a² + b² = |z|²")))
    return cv.render()


def build_sp_cong(p: Params) -> str:
    """Cộng (hoặc trừ) số phức chính là cộng (trừ) vectơ trên mặt phẳng Argand."""
    mode = str(p.get("mode", "tong"))
    if mode not in ("tong", "hieu"):
        mode = "tong"
    a1, b1 = _f(p.get("a1", 3.0), 3.0), _f(p.get("b1", 0.9), 0.9)
    a2, b2 = _f(p.get("a2", 1.1), 1.1), _f(p.get("b2", 2.3), 2.3)
    if math.hypot(a1, b1) < 0.4 or math.hypot(a2, b2) < 0.4:
        a1, b1, a2, b2 = 3.0, 0.9, 1.1, 2.3
    if mode == "tong":
        Rw = (a1 + a2, b1 + b2)
    else:
        Rw = (a1 - a2, b1 - b2)
    w, h, P, box = _frame_with_axes([(0.0, 0.0), (a1, b1), (a2, b2), Rw],
                                    52.0, 70.0, 96.0, 64.0, 78.0, 0.6)
    O, M1, M2, Rp = P(0, 0), P(a1, b1), P(a2, b2), P(*Rw)
    cv = Canvas(w, h, title="Cộng và trừ số phức trên mặt phẳng Argand",
                desc="Tổng hai số phức ứng với đường chéo hình bình hành dựng trên hai vectơ biểu diễn.")
    _argand(cv, P, *box)
    if mode == "tong":
        cv.polygon([O, M1, Rp, M2], cls="fill-a")
        cv.line(*M1, *Rp, cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.line(*M2, *Rp, cls="ink-thin", extra=' stroke-dasharray="5 4"')
        lab = "z₁ + z₂"
        cap = "|z₁ + z₂| ≤ |z₁| + |z₂| (bất đẳng thức tam giác)"
    else:
        cv.line(*M2, *M1, cls="accent-d", extra=_stroke(3))
        cv.text((M1[0] + M2[0]) / 2, (M1[1] + M2[1]) / 2 - 9, "M₂M₁", cls="lbl-sm", anchor="middle")
        lab = "z₁ − z₂"
        cap = "|z₁ − z₂| = M₁M₂ (khoảng cách hai điểm biểu diễn)"
    cv.arrow(*O, *M1, cls="accent-a", head=9)
    cv.arrow(*O, *M2, cls="accent-c", head=9)
    cv.arrow(*O, *Rp, cls="accent-b", head=10)
    cv.text(M1[0] + 8, M1[1] - 6, "z₁", cls="lbl")
    cv.text(M2[0] + 8, M2[1] - 6, "z₂", cls="lbl")
    cv.text(Rp[0] + 8, Rp[1] - 6, lab, cls="lbl")
    _caption(cv, w, h - 18, str(p.get("caption", cap)))
    return cv.render()


def build_sp_nhan_quay(p: Params) -> str:
    """Nhân số phức = quay một góc bằng acgumen và co giãn theo môđun."""
    mode = str(p.get("mode", "nhan"))
    if mode not in ("nhan", "luy-thua"):
        mode = "nhan"
    r1 = _clamp(_f(p.get("r1", 2.1), 2.1), 0.4, 6)
    f1 = _f(p.get("phi1", 26), 26)
    r2 = _clamp(_f(p.get("r2", 1.45), 1.45), 0.35, 3)
    f2 = _clamp(_f(p.get("phi2", 48), 48), 8, 150)
    if mode == "luy-thua":
        r2, f2 = r1, f1
    z1 = (r1 * math.cos(math.radians(f1)), r1 * math.sin(math.radians(f1)))
    rp, fp = r1 * r2, f1 + f2
    z3 = (rp * math.cos(math.radians(fp)), rp * math.sin(math.radians(fp)))
    SC = 56.0
    big = max(rp, r1)
    # Hộp bao phải chứa CẢ hai đường tròn môđun, không chỉ hai ngọn vectơ.
    w, h, P, box = _frame_with_axes([(0.0, 0.0), z1, z3, (big, 0.0), (-big, 0.0),
                                     (0.0, big), (0.0, -big)], SC, 68.0, 92.0, 62.0, 78.0, 0.4)
    O = P(0, 0)
    cv = Canvas(w, h, title="Nhân số phức là phép quay kết hợp vị tự",
                desc="Nhân z với một số phức làm acgumen cộng thêm và môđun nhân lên.")
    _argand(cv, P, *box)
    cv.circle(O[0], O[1], r1 * SC, cls="ink-thin", extra=' stroke-dasharray="5 5"')
    cv.circle(O[0], O[1], rp * SC, cls="accent-b", extra=_stroke(1.4, "5 5"))
    cv.polyline(_arc_pts(O[0], O[1], rp * SC * 0.5, f1, fp, 32), cls="accent-d", extra=_stroke(2))
    cv.text(*_pol(O[0], O[1], rp * SC * 0.5 + 16, (f1 + fp) / 2),
            s=("φ₂" if mode == "nhan" else "φ"), cls="lbl", anchor="middle")
    cv.arrow(*O, *P(*z1), cls="accent-a", head=9)
    cv.arrow(*O, *P(*z3), cls="accent-b", head=10)
    cv.text(P(*z1)[0] + 8, P(*z1)[1] - 6, "z₁", cls="lbl")
    cv.text(P(*z3)[0] + 8, P(*z3)[1] - 6, "z₁z₂" if mode == "nhan" else "z²", cls="lbl")
    cap = ("z₁z₂: môđun r₁r₂, acgumen φ₁ + φ₂" if mode == "nhan"
           else "zⁿ: môđun rⁿ, acgumen n·φ (công thức Moivre)")
    _caption(cv, w, h - 18, str(p.get("caption", cap)))
    return cv.render()


def build_sp_luy_thua_i(p: Params) -> str:
    """Luỹ thừa của đơn vị ảo: nhân với i là phép quay 90°, chu kì lặp lại sau 4 bước."""
    R = _clamp(_f(p.get("R", 108), 108), 70, 150)
    pad = 76.0
    w = h = 2 * (R + pad)
    h += 20.0
    cx = cy = R + pad
    cv = Canvas(w, h, title="Luỹ thừa của đơn vị ảo i",
                desc="Bốn giá trị 1, i, −1, −i nằm trên đường tròn đơn vị; mỗi lần nhân với i quay thêm 90 độ.")
    cv.circle(cx, cy, R, cls="ink-thin")
    # Mũi tên trục dừng ở R+16 để bốn nhãn 1, i, −1, −i (đặt ở R+22) nằm hẳn
    # ngoài đầu mũi tên; tên trục Re lùi xuống dưới nhường chỗ cho nhãn "1".
    cv.arrow(cx - R - 16, cy, cx + R + 16, cy, cls="axis", head=7)
    cv.arrow(cx, cy + R + 16, cx, cy - R - 16, cls="axis", head=7)
    cv.text(cx + R + 24, cy - 14, "Re", cls="lbl-sm", anchor="end")
    cv.text(cx + 9, cy - R - 20, "Im", cls="lbl-sm")
    # Nhãn chỉ ghi bốn GIÁ TRỊ; công thức i⁴ᵏ⁺ʳ dồn xuống chú thích. Ghi cả công
    # thức lên vành tròn thì dòng "−1 = i⁴ᵏ⁺²" dài hơn cả lề trái và bị khung cắt
    # mất — mà kiểm tra toạ độ không bắt được, vì điểm neo vẫn nằm trong khung.
    marks = ((0, "1", "start"), (90, "i", "middle"),
             (180, "−1", "end"), (270, "−i", "middle"))
    for deg, lab, anc in marks:
        px, py = _pol(cx, cy, R, deg)
        cv.arrow(cx, cy, px, py, cls="accent-a", head=8)
        cv.dot(px, py, r=3.6, cls="accent-a")
        tx, ty = _pol(cx, cy, R + 22, deg)
        cv.text(tx, ty + (4 if deg in (0, 180) else (-9 if deg == 90 else 18)), lab,
                cls="lbl", anchor=anc)
        # Cung hở hai đầu (10°…80°): bốn cung 90° liền nhau khép thành một vòng
        # tròn kín, nhìn ra đường tròn thứ hai chứ không ra bốn phép quay.
        cv.polyline(_arc_pts(cx, cy, R * 0.52, deg + 10, deg + 80, 20),
                    cls="accent-d", extra=_stroke(2))
        ax, ay = _pol(cx, cy, R * 0.52 + 15, deg + 45)
        cv.text(ax, ay + 4, "×i", cls="lbl-sm", anchor="middle")
    _caption(cv, w, h - 14,
             str(p.get("caption", "Nhân với i là quay 90°, nên i⁴ᵏ = 1, i⁴ᵏ⁺¹ = i, "
                                  "i⁴ᵏ⁺² = −1, i⁴ᵏ⁺³ = −i")))
    return cv.render()


def build_sp_can_bac_n(p: Params) -> str:
    """Căn bậc n của một số phức: n điểm chia đều đường tròn, tạo thành đa giác đều."""
    n = int(_clamp(_f(p.get("n", 5), 5), 2, 12))
    phi0 = _f(p.get("phi", 0), 0) / max(n, 1)
    R = _clamp(_f(p.get("R", 118), 118), 70, 160)
    pad = 82.0
    w = h = 2 * (R + pad)
    h += 20.0
    cx = cy = R + pad
    cv = Canvas(w, h, title=f"Căn bậc {n} của một số phức",
                desc="Các căn bậc n nằm trên một đường tròn tâm O và chia đường tròn thành n phần bằng nhau.")
    cv.circle(cx, cy, R, cls="ink-thin", extra=' stroke-dasharray="6 5"')
    cv.arrow(cx - R - 22, cy, cx + R + 28, cy, cls="axis", head=7)
    cv.arrow(cx, cy + R + 22, cx, cy - R - 28, cls="axis", head=7)
    # Tên trục ghi DƯỚI trục thực: căn bậc n của số dương luôn có một nghiệm nằm
    # đúng trên tia Ox dương, và nhãn nghiệm ấy chiếm sẵn chỗ phía trên.
    cv.text(cx + R + 26, cy + 18, "Re", cls="lbl-sm", anchor="end")
    cv.text(cx + 9, cy - R - 20, "Im", cls="lbl-sm")
    roots = [_pol(cx, cy, R, phi0 + 360.0 * k / n) for k in range(n)]
    cv.polygon(roots, cls="fill-a")
    cv.polyline(roots + [roots[0]], cls="accent-c", extra=_stroke(2))
    for k, (px, py) in enumerate(roots):
        cv.line(cx, cy, px, py, cls="ink-thin")
        cv.dot(px, py, r=3.6, cls="accent-a")
        deg = phi0 + 360.0 * k / n
        tx, ty = _pol(cx, cy, R + 17, deg)
        c, s = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        anc = "middle" if abs(c) < 0.34 else ("start" if c > 0 else "end")
        # Nghiệm nằm sát trục thực thì nhấc nhãn lên khỏi thân mũi tên trục.
        _sub(cv, tx, ty + (4 if abs(s) > 0.25 else -9), "z", str(k),
             cls="lbl-sm", anchor=anc)
    cv.dot(cx, cy, r=3, cls="ink")
    _caption(cv, w, h - 14,
             str(p.get("caption", f"n = {n} căn cách đều nhau góc 2π/n trên đường tròn bán kính ⁿ√r")))
    return cv.render()


def build_sp_quy_tich(p: Params) -> str:
    """Tập hợp điểm biểu diễn số phức thoả một điều kiện về môđun hoặc acgumen."""
    kind = str(p.get("kind", "duong-tron"))
    if kind not in ("duong-tron", "trung-truc", "elip", "tia", "apollonius", "cung-tron"):
        kind = "duong-tron"
    S = 46.0                                     # px trên một đơn vị

    if kind == "duong-tron":
        a0, b0 = _f(p.get("a0", 1.2), 1.2), _f(p.get("b0", 0.9), 0.9)
        R = _clamp(_f(p.get("R", 2.2), 2.2), 0.4, 6)
        pts = [(a0 - R, b0 - R), (a0 + R, b0 + R), (0.0, 0.0)]
        w, h, P = _fit(pts, S, 68.0, 82.0, 62.0, 78.0)
        cv = Canvas(w, h, title="Tập hợp điểm |z − z₀| = R",
                    desc="Tập hợp các điểm cách điểm I cố định một khoảng không đổi là một đường tròn.")
        _argand(cv, P, a0 - R - 0.5, a0 + R + 0.6, b0 - R - 0.5, b0 + R + 0.6)
        I = P(a0, b0)
        cv.circle(I[0], I[1], R * S, cls="accent-a", extra=_stroke(2.4))
        cv.dot(*I, r=3.4, cls="accent-b")
        cv.text(I[0] + 8, I[1] + 16, "I(a₀; b₀)", cls="lbl-sm")
        M = P(a0 + R * math.cos(math.radians(48)), b0 + R * math.sin(math.radians(48)))
        cv.line(*I, *M, cls="accent-b", extra=_stroke(2))
        cv.dot(*M, r=3.4, cls="accent-b")
        cv.text((I[0] + M[0]) / 2 + 6, (I[1] + M[1]) / 2 - 6, "R", cls="lbl")
        cv.text(M[0] + 8, M[1] - 7, "M", cls="lbl")
        cap = "|z − z₀| = R ⇔ M chạy trên đường tròn tâm I bán kính R"

    elif kind == "trung-truc":
        A, B = (-2.0, -0.6), (2.2, 1.1)
        mid = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
        dx, dy = B[0] - A[0], B[1] - A[1]
        L = math.hypot(dx, dy) or 1.0
        nx, ny = -dy / L, dx / L
        t = 2.4
        E1 = (mid[0] + nx * t, mid[1] + ny * t)
        E2 = (mid[0] - nx * t, mid[1] - ny * t)
        Mw = (mid[0] + nx * 1.5, mid[1] + ny * 1.5)
        w, h, P = _fit([A, B, E1, E2, (0.0, 0.0)], S, 66.0, 80.0, 60.0, 78.0)
        cv = Canvas(w, h, title="Tập hợp điểm |z − z₁| = |z − z₂|",
                    desc="Tập hợp các điểm cách đều hai điểm cho trước là đường trung trực của đoạn nối chúng.")
        _argand(cv, P, min(A[0], B[0], E1[0], E2[0]) - 0.5, max(A[0], B[0], E1[0], E2[0]) + 0.6,
                min(A[1], B[1], E1[1], E2[1]) - 0.5, max(A[1], B[1], E1[1], E2[1]) + 0.6)
        cv.line(*P(*A), *P(*B), cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.line(*P(*E1), *P(*E2), cls="accent-a", extra=_stroke(2.4))
        _right_angle_at(cv, P(*mid), P(*B), P(*E1), size=11)
        for q, nm in ((A, "M₁"), (B, "M₂")):
            cv.dot(*P(*q), r=3.4, cls="accent-b")
            cv.text(P(*q)[0], P(*q)[1] + 19, nm, cls="lbl", anchor="middle")
        cv.dot(*P(*Mw), r=3.4, cls="accent-c")
        cv.text(P(*Mw)[0] + 8, P(*Mw)[1] - 7, "M", cls="lbl")
        cv.line(*P(*Mw), *P(*A), cls="accent-c", extra=_stroke(1.6, "5 4"))
        cv.line(*P(*Mw), *P(*B), cls="accent-c", extra=_stroke(1.6, "5 4"))
        cap = "MM₁ = MM₂ ⇔ M thuộc đường trung trực của M₁M₂"

    elif kind == "elip":
        c = 1.9
        a0 = _clamp(_f(p.get("a0", 2.8), 2.8), c + 0.4, 6)
        bb = math.sqrt(max(a0 * a0 - c * c, 0.04))
        w, h, P = _fit([(-a0, -bb), (a0, bb), (0.0, 0.0)], S, 66.0, 82.0, 60.0, 78.0)
        cv = Canvas(w, h, title="Tập hợp điểm |z − z₁| + |z − z₂| = 2a",
                    desc="Tập hợp các điểm có tổng khoảng cách tới hai tiêu điểm không đổi là một elip.")
        _argand(cv, P, -a0 - 0.6, a0 + 0.7, -bb - 0.6, bb + 0.7)
        ell = [P(a0 * math.cos(2 * math.pi * i / 120), bb * math.sin(2 * math.pi * i / 120))
               for i in range(121)]
        cv.polyline(ell, cls="accent-a", extra=_stroke(2.4))
        F1, F2 = P(-c, 0), P(c, 0)
        Mp = P(a0 * math.cos(1.0), bb * math.sin(1.0))
        for q, nm in ((F1, "M₁"), (F2, "M₂")):
            cv.dot(*q, r=3.4, cls="accent-b")
            cv.text(q[0], q[1] + 19, nm, cls="lbl", anchor="middle")
        cv.line(*Mp, *F1, cls="accent-c", extra=_stroke(1.8, "5 4"))
        cv.line(*Mp, *F2, cls="accent-c", extra=_stroke(1.8, "5 4"))
        cv.dot(*Mp, r=3.4, cls="accent-c")
        cv.text(Mp[0] + 8, Mp[1] - 7, "M", cls="lbl")
        cap = "MM₁ + MM₂ = 2a ⇔ M chạy trên elip nhận M₁, M₂ làm tiêu điểm"

    elif kind == "tia":
        # Gốc tia đặt xa hẳn gốc toạ độ, và hướng tia chọn sao cho tia KHÔNG đi
        # qua gần O: để A sát O thì cung góc θ vẽ tại A phủ luôn lên nhãn "O".
        a, b = _f(p.get("a", -1.6), -1.6), _f(p.get("b", -2.6), -2.6)
        th = _clamp(_f(p.get("theta", 48), 48), -170, 170)
        Lr = 4.2
        E = (a + Lr * math.cos(math.radians(th)), b + Lr * math.sin(math.radians(th)))
        w, h, P = _fit([(a, b), E, (0.0, 0.0), (a + 2.4, b)], S, 66.0, 82.0, 62.0, 78.0)
        cv = Canvas(w, h, title="Tập hợp điểm arg(z − a) = θ",
                    desc="Tập hợp các điểm nhìn từ A theo một hướng cố định là một tia gốc A, bỏ chính điểm A.")
        _argand(cv, P, min(a, E[0], 0) - 0.6, max(a + 2.6, E[0], 0) + 0.6,
                min(b, E[1], 0) - 0.6, max(b, E[1], 0) + 0.6)
        A = P(a, b)
        cv.line(*A, *P(a + 2.4, b), cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.arrow(*A, *P(*E), cls="accent-a", head=9)
        _angle_at(cv, A, P(a + 2.4, b), P(*E), r=30, label="θ", lgap=15)
        cv.circle(A[0], A[1], 4, cls="accent-b", extra=' style="fill:none" stroke-width="2"')
        cv.text(A[0] - 9, A[1] + 17, "A", cls="lbl", anchor="end")
        cap = "arg(z − a) = θ ⇔ M thuộc tia gốc A, hướng θ (không lấy điểm A)"

    elif kind == "apollonius":
        A, B = (-1.8, 0.0), (2.0, 0.0)
        k = _clamp(_f(p.get("k", 1.8), 1.8), 0.25, 4)
        if abs(k - 1) < 0.08:
            k = 1.8
        den = 1 - k * k
        Cc = ((A[0] - k * k * B[0]) / den, (A[1] - k * k * B[1]) / den)
        Rr = k * math.hypot(A[0] - B[0], A[1] - B[1]) / abs(den)
        w, h, P = _fit([(Cc[0] - Rr, Cc[1] - Rr), (Cc[0] + Rr, Cc[1] + Rr), A, B, (0.0, 0.0)],
                       S, 66.0, 82.0, 60.0, 78.0)
        cv = Canvas(w, h, title="Đường tròn Apollonius |z − a| = k|z − b|",
                    desc="Tập hợp các điểm có tỉ số khoảng cách tới hai điểm cố định không đổi là một đường tròn.")
        _argand(cv, P, Cc[0] - Rr - 0.6, Cc[0] + Rr + 0.7, Cc[1] - Rr - 0.6, Cc[1] + Rr + 0.7)
        I = P(*Cc)
        cv.circle(I[0], I[1], Rr * S, cls="accent-a", extra=_stroke(2.4))
        Mp = P(Cc[0] + Rr * math.cos(1.05), Cc[1] + Rr * math.sin(1.05))
        for q, nm in ((P(*A), "A"), (P(*B), "B")):
            cv.dot(*q, r=3.4, cls="accent-b")
            cv.text(q[0], q[1] + 19, nm, cls="lbl", anchor="middle")
        cv.line(*Mp, *P(*A), cls="accent-c", extra=_stroke(1.8, "5 4"))
        cv.line(*Mp, *P(*B), cls="accent-c", extra=_stroke(1.8, "5 4"))
        cv.dot(*Mp, r=3.4, cls="accent-c")
        cv.text(Mp[0] + 8, Mp[1] - 7, "M", cls="lbl")
        cap = f"MA = k·MB (k = {_num(k)}) ⇔ M chạy trên một đường tròn"

    else:  # cung-tron
        th = _clamp(_f(p.get("theta", 62), 62), 15, 165)
        L = 2.0
        A, B = (-L, 0.0), (L, 0.0)
        Rr = L / math.sin(math.radians(th))
        Oy = L / math.tan(math.radians(th))
        top = Oy + Rr
        w, h, P = _fit([A, B, (0.0, top), (0.0, min(0.0, Oy) - 0.4), (0.0, 0.0)],
                       S, 68.0, 82.0, 62.0, 78.0)
        cv = Canvas(w, h, title="Cung chứa góc: arg((z − a)/(z − b)) = θ",
                    desc="Tập hợp các điểm nhìn đoạn AB dưới một góc không đổi là một cung tròn qua A và B.")
        _argand(cv, P, -L - 0.7, L + 0.8, min(0.0, Oy) - 0.7, top + 0.7)
        a1 = math.degrees(math.atan2(A[1] - Oy, A[0] - 0.0))
        a2 = math.degrees(math.atan2(B[1] - Oy, B[0] - 0.0))
        while a2 < a1:
            a2 += 360
        cen = P(0.0, Oy)
        cv.polyline(_arc_pts(cen[0], cen[1], Rr * S, a2, a1 + 360, 80),
                    cls="accent-a", extra=_stroke(2.4))
        # M lấy lệch khỏi đỉnh cung: đỉnh nằm đúng trên trục ảo, nhãn "M" ở đó
        # sẽ đè lên tên trục "Im".
        Mp = P(Rr * math.cos(math.radians(108.0)), Oy + Rr * math.sin(math.radians(108.0)))
        cv.line(*Mp, *P(*A), cls="accent-c", extra=_stroke(1.8))
        cv.line(*Mp, *P(*B), cls="accent-c", extra=_stroke(1.8))
        _angle_at(cv, Mp, P(*A), P(*B), r=28, label="θ", lgap=14)
        for q, nm in ((P(*A), "A"), (P(*B), "B")):
            cv.dot(*q, r=3.4, cls="accent-b")
            cv.text(q[0], q[1] + 19, nm, cls="lbl", anchor="middle")
        cv.dot(*Mp, r=3.4, cls="accent-c")
        cv.text(Mp[0] + 8, Mp[1] - 8, "M", cls="lbl")
        cap = "Góc AMB không đổi ⇔ M chạy trên cung chứa góc θ dựng trên AB"

    _caption(cv, w, h - 18, str(p.get("caption", cap)))
    return cv.render()


# --------------------------------------------------------------------------
# 7. Toạ độ cực
# --------------------------------------------------------------------------
def build_lg_toa_do_cuc(p: Params) -> str:
    """Toạ độ cực (r; θ) và liên hệ với toạ độ Descartes x = r cos θ, y = r sin θ."""
    r = _clamp(_f(p.get("r", 3.4), 3.4), 0.5, 12)
    th = _clamp(_f(p.get("theta", 42), 42), 5, 175)
    x, y = r * math.cos(math.radians(th)), r * math.sin(math.radians(th))
    w, h, P = _fit([(0.0, 0.0), (x, y), (x, 0.0), (0.0, y), (r * 1.08, 0.0), (0.0, r * 1.08)],
                   54.0, 68.0, 96.0, 62.0, 78.0)
    O, M = P(0, 0), P(x, y)
    cv = Canvas(w, h, title="Toạ độ cực và toạ độ Descartes",
                desc="Điểm M có toạ độ cực r và theta; hình chiếu lên hai trục cho x = r cos theta và y = r sin theta.")
    _axes(cv, P, min(-0.4, x) - 0.3, max(r * 1.12, x) + 0.4, -0.5, max(r * 1.12, y) + 0.4)
    cv.line(*M, *P(x, 0), cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.line(*M, *P(0, y), cls="ink-thin", extra=' stroke-dasharray="4 3"')
    cv.polyline(_arc_pts(O[0], O[1], min(r * 54.0 * 0.45, 52), 0, th, 28),
                cls="accent-d", extra=_stroke(2))
    cv.text(*_pol(O[0], O[1], min(r * 54.0 * 0.45, 52) + 16, th / 2), s="θ", cls="lbl", anchor="middle")
    cv.arrow(*O, *M, cls="accent-a", head=9)
    cv.dot(*M, r=3.8, cls="accent-a")
    cv.text(M[0] + 9, M[1] - 8, "M(r; θ)", cls="lbl")
    cv.text((O[0] + M[0]) / 2 - 10, (O[1] + M[1]) / 2 - 8, "r", cls="lbl", anchor="end")
    # Trên hình chỉ ghi tên hai hình chiếu; công thức đầy đủ dồn xuống chú thích.
    # Viết "y = r·sin θ" ngay cạnh trục tung thì dòng chữ thò hẳn ra ngoài lề trái.
    cv.text(P(x, 0)[0], P(x, 0)[1] + 18, "x", cls="lbl", anchor="middle")
    cv.text(P(0, y)[0] - 9, P(0, y)[1] + 4, "y", cls="lbl", anchor="end")
    _caption(cv, w, h - 18,
             str(p.get("caption", "x = r·cos θ,  y = r·sin θ,  r² = x² + y²,  tan θ = y/x")))
    return cv.render()


def build_lg_duong_cong_cuc(p: Params) -> str:
    """Đường cong trong toạ độ cực r = f(θ): cardioid, hoa hồng, xoắn ốc Archimedes…"""
    expr = str(p.get("expr", "1 + cos(t)"))
    tmin = _f(p.get("tmin", 0), 0)
    tmax = _f(p.get("tmax", 2 * math.pi), 2 * math.pi)
    if abs(tmax - tmin) < 1e-3:
        tmin, tmax = 0.0, 2 * math.pi
    try:
        pts_polar = sample_curve(expr, "t", tmin, tmax, 480)
    except Exception:                                   # biểu thức hỏng thì lui về cardioid
        expr = "1 + cos(t)"
        pts_polar = sample_curve(expr, "t", 0.0, 2 * math.pi, 480)
    world = [(rr * math.cos(tt), rr * math.sin(tt)) for tt, rr in pts_polar]
    if not world:
        world = [(0.0, 0.0)]
    span = max(max(abs(q[0]) for q in world), max(abs(q[1]) for q in world), 0.5)
    scale = 128.0 / span
    w, h, P = _fit(world + [(-span, -span), (span, span)], scale, 62.0, 62.0, 58.0, 74.0)
    O = P(0, 0)
    cv = Canvas(w, h, title=f"Đường cong cực r = {expr}",
                desc="Đường cong cho bởi phương trình trong toạ độ cực, vẽ trên mặt phẳng Oxy.")
    for k in (0.5, 1.0):
        cv.circle(O[0], O[1], span * k * scale, cls="grid")
    for deg in range(0, 360, 45):
        cv.line(*O, *_pol(O[0], O[1], span * scale, deg), cls="grid")
    _axes(cv, P, -span * 1.05, span * 1.08, -span * 1.05, span * 1.08)
    if bool(p.get("shade", False)):
        cv.polygon([O] + [P(*q) for q in world], cls="fill-a")
    cv.polyline([P(*q) for q in world], cls="curve")
    _caption(cv, w, h - 16, str(p.get("caption", f"r = {expr}")))
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    # đường tròn lượng giác
    "lg_duong_tron_luong_giac": build_lg_duong_tron_luong_giac,
    "lg_dau_luong_giac": build_lg_dau_luong_giac,
    "lg_goc_dac_biet": build_lg_goc_dac_biet,
    "lg_gia_tri_dac_biet": build_lg_gia_tri_dac_biet,
    "lg_cung_lien_ket": build_lg_cung_lien_ket,
    "lg_cung_quat": build_lg_cung_quat,
    # đồ thị
    "lg_do_thi_luong_giac": build_lg_do_thi_luong_giac,
    # tam giác vuông
    "lg_ti_so_luong_giac": build_lg_ti_so_luong_giac,
    "lg_tam_giac_vuong_abc": build_lg_tam_giac_vuong_abc,
    "lg_he_thuc_tam_giac_vuong": build_lg_he_thuc_tam_giac_vuong,
    # giải tam giác
    "lg_tam_giac_co_ban": build_lg_tam_giac_co_ban,
    "lg_dinh_li_cosin": build_lg_dinh_li_cosin,
    "lg_dinh_li_sin": build_lg_dinh_li_sin,
    "lg_dien_tich_sin": build_lg_dien_tich_sin,
    "lg_duong_tron_noi_tiep": build_lg_duong_tron_noi_tiep,
    "lg_tam_giac_duong_dac_biet": build_lg_tam_giac_duong_dac_biet,
    "lg_tam_giac_deu": build_lg_tam_giac_deu,
    "lg_tu_giac_duong_cheo": build_lg_tu_giac_duong_cheo,
    # vectơ phẳng
    "vt_tong": build_vt_tong,
    "vt_hieu": build_vt_hieu,
    "vt_nhan_so": build_vt_nhan_so,
    "vt_thang_hang": build_vt_thang_hang,
    "vt_tich_vo_huong": build_vt_tich_vo_huong,
    "vt_phan_tich": build_vt_phan_tich,
    "vt_diem_dac_biet": build_vt_diem_dac_biet,
    # số phức
    "sp_diem_bieu_dien": build_sp_diem_bieu_dien,
    "sp_lien_hop": build_sp_lien_hop,
    "sp_cong": build_sp_cong,
    "sp_nhan_quay": build_sp_nhan_quay,
    "sp_luy_thua_i": build_sp_luy_thua_i,
    "sp_can_bac_n": build_sp_can_bac_n,
    "sp_quy_tich": build_sp_quy_tich,
    # toạ độ cực
    "lg_toa_do_cuc": build_lg_toa_do_cuc,
    "lg_duong_cong_cuc": build_lg_duong_cong_cuc,
}


def render(generator: str, params: Params | None = None) -> str:
    if generator not in REGISTRY:
        raise KeyError(f"generator họ lượng giác không tồn tại: {generator}")
    return REGISTRY[generator](params or {})
