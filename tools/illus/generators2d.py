"""Các generator SVG deterministic cho minh hoạ công thức 2D.

Mỗi generator nhận ``params`` (dict, có mặc định) và trả về chuỗi SVG hoàn chỉnh.
Đăng ký trong ``REGISTRY`` theo tên để builder/matcher tra cứu.

Thêm generator mới: viết hàm ``build_<tên>(p) -> str`` rồi thêm vào ``REGISTRY``.
"""

from __future__ import annotations

import math
from typing import Callable

from .mathexpr import compile_expr, sample_curve
from .svgkit import Canvas, _n

Params = dict


# --------------------------------------------------------------------------
# Hình học phẳng
# --------------------------------------------------------------------------
def build_right_triangle(p: Params) -> str:
    """Tam giác vuông: hai cạnh góc vuông b, c; cạnh huyền a. Có ô vuông Pytago tuỳ chọn."""
    b = float(p.get("b", 4))      # cạnh nằm ngang
    c = float(p.get("c", 3))      # cạnh dọc
    show_squares = bool(p.get("pythagoras", False))
    la = p.get("label_hyp", "a")
    lb = p.get("label_base", "b")
    lc = p.get("label_height", "c")

    if show_squares:
        scale = 24.0
        pad = 36.0
        bw, ch = b * scale, c * scale
        ox = ch + pad
        oy = ch + bw + pad
        w = 2 * ch + bw + 2 * pad
        h = ch + 2 * bw + 2 * pad
    else:
        scale = 46.0
        pad = 56.0
        bw, ch = b * scale, c * scale
        ox, oy = pad, pad + ch
        w = ox + bw + pad
        h = oy + pad

    cv = Canvas(w, h, title="Định lí Pytago" if show_squares else "Tam giác vuông")
    P_right = (ox, oy)
    P_base = (ox + bw, oy)
    P_top = (ox, oy - ch)

    if show_squares:
        # ô vuông trên hai cạnh góc vuông và trên cạnh huyền
        cv.polygon([(ox, oy), (ox + bw, oy), (ox + bw, oy + bw), (ox, oy + bw)], cls="fill-a")
        cv.polyline([(ox, oy), (ox + bw, oy), (ox + bw, oy + bw), (ox, oy + bw), (ox, oy)], cls="ink-thin")

        cv.polygon([(ox, oy), (ox, oy - ch), (ox - ch, oy - ch), (ox - ch, oy)], cls="fill-c")
        cv.polyline([(ox, oy), (ox, oy - ch), (ox - ch, oy - ch), (ox - ch, oy), (ox, oy)], cls="ink-thin")

        p3 = (ox + bw + ch, oy - bw)
        p4 = (ox + ch, oy - ch - bw)
        cv.polygon([P_base, p3, p4, P_top], cls="fill-b")
        cv.polyline([P_base, p3, p4, P_top], cls="ink-thin")

        # Nhãn diện tích bên trong các ô vuông
        cv.text(ox + bw / 2, oy + bw / 2 + 5, "b²", cls="lbl", anchor="middle")
        cv.text(ox - ch / 2, oy - ch / 2 + 5, "c²", cls="lbl", anchor="middle")
        cv.text((P_base[0] + p4[0]) / 2, (P_base[1] + p4[1]) / 2 + 5, "a² = b² + c²", cls="lbl", anchor="middle")

    cv.polygon([P_right, P_base, P_top], cls="fill-a", extra=' fill-opacity="0.1"')
    cv.polyline([P_top, P_right, P_base, P_top], cls="ink", extra=' stroke-width="2.2"')
    cv.right_angle(*P_right, *P_base, *P_top, size=12)

    if show_squares:
        cv.text((ox + P_base[0]) / 2, oy - 6, f"{lb}", cls="lbl", anchor="middle")
        cv.text(ox + 8, (oy + P_top[1]) / 2 + 4, f"{lc}", cls="lbl")
        cv.text((P_base[0] + P_top[0]) / 2 - 8, (P_base[1] + P_top[1]) / 2 - 8, la, cls="lbl")
    else:
        cv.text((ox + P_base[0]) / 2, oy + 20, f"{lb} = {_n(b)}", cls="lbl", anchor="middle")
        cv.text(ox - 12, (oy + P_top[1]) / 2, f"{lc} = {_n(c)}", cls="lbl", anchor="end")
        cv.text((P_base[0] + P_top[0]) / 2 + 10, (P_base[1] + P_top[1]) / 2 - 6, la, cls="lbl")

    if p.get("angle_label"):
        cv.text(P_base[0] - 26, oy - 8, p["angle_label"], cls="lbl-sm", anchor="end")
    return cv.render()


def build_circle(p: Params) -> str:
    """Đường tròn bán kính R, có tâm, bán kính minh hoạ, nhãn diện tích/chu vi."""
    R = float(p.get("R", 3))
    scale = 40.0
    r = R * scale
    pad = 46.0
    cx = cy = pad + r
    w = h = 2 * (pad + r)
    cv = Canvas(w, h, title="Đường tròn")
    cv.circle(cx, cy, r, cls="fill-a")
    cv.circle(cx, cy, r, cls="curve")
    cv.dot(cx, cy, 3, cls="accent-b")
    ang = math.radians(-35)
    ex, ey = cx + r * math.cos(ang), cy + r * math.sin(ang)
    cv.line(cx, cy, ex, ey, cls="accent-b", extra=' stroke-width="2"')
    cv.text((cx + ex) / 2, (cy + ey) / 2 - 6, p.get("label_r", "R"), cls="lbl")
    cv.text(cx, cy + 4, "O", cls="lbl-sm", anchor="middle")
    return cv.render()


def build_rectangle(p: Params) -> str:
    """Hình chữ nhật a×b (mặc định minh hoạ diện tích/chu vi)."""
    a = float(p.get("a", 5))
    b = float(p.get("b", 3))
    scale = 44.0
    pad = 40.0
    padL = 58.0   # lề trái rộng hơn để nhãn cạnh "b = …" không bị cắt
    aw, bh = a * scale, b * scale
    cv = Canvas(aw + padL + pad, bh + 2 * pad, title="Hình chữ nhật")
    cv.rect(padL, pad, aw, bh, cls="fill-a")
    cv.rect(padL, pad, aw, bh, cls="ink")
    cv.text(padL + aw / 2, pad + bh + 22, f"{p.get('label_a','a')} = {_n(a)}", cls="lbl", anchor="middle")
    cv.text(padL - 12, pad + bh / 2, f"{p.get('label_b','b')} = {_n(b)}", cls="lbl", anchor="end")
    return cv.render()


def build_triangle(p: Params) -> str:
    """Tam giác thường: đáy và đường cao (minh hoạ S = ½·đáy·cao)."""
    base = float(p.get("base", 5))
    height = float(p.get("height", 3))
    apex = float(p.get("apex", 0.35))   # vị trí đỉnh theo tỉ lệ đáy (0..1)
    scale = 44.0
    pad = 46.0
    bw, hh = base * scale, height * scale
    ox, oy = pad, pad + hh
    A = (ox, oy)
    B = (ox + bw, oy)
    C = (ox + apex * bw, oy - hh)
    cv = Canvas(bw + 2 * pad, hh + 2 * pad, title="Tam giác")
    cv.polygon([A, B, C], cls="fill-a")
    cv.polyline([A, B, C, A], cls="ink")
    foot = (C[0], oy)
    cv.line(C[0], C[1], foot[0], foot[1], cls="accent-b", extra=' stroke-dasharray="5 4" stroke-width="1.6"')
    cv.right_angle(foot[0], foot[1], foot[0] + 12, foot[1], foot[0], foot[1] - 12, size=11)
    cv.text((A[0] + B[0]) / 2, oy + 22, f"đáy = {_n(base)}", cls="lbl", anchor="middle")
    cv.text(C[0] + 8, (C[1] + oy) / 2, f"h = {_n(height)}", cls="lbl")
    return cv.render()


def build_parallelogram(p: Params) -> str:
    """Hình bình hành: cạnh đáy a, đường cao h."""
    a = float(p.get("a", 5))
    height = float(p.get("height", 3))
    skew = float(p.get("skew", 1.4))
    scale = 42.0
    pad = 56.0
    aw, hh, sk = a * scale, height * scale, skew * scale
    ox, oy = pad + sk, pad + hh
    A = (ox, oy)
    B = (ox + aw, oy)
    C = (ox + aw - sk, oy - hh)
    D = (ox - sk, oy - hh)
    cv = Canvas(aw + sk + 2 * pad, hh + 2 * pad, title="Hình bình hành")
    cv.polygon([A, B, C, D], cls="fill-a")
    cv.polyline([A, B, C, D, A], cls="ink")
    cv.line(D[0], D[1], D[0], oy, cls="accent-b", extra=' stroke-dasharray="5 4" stroke-width="1.6"')
    cv.right_angle(D[0], oy, D[0] + 12, oy, D[0], oy - 12, size=11)
    cv.text((A[0] + B[0]) / 2, oy + 22, f"a = {_n(a)}", cls="lbl", anchor="middle")
    cv.text(D[0] - 10, (D[1] + oy) / 2, f"h = {_n(height)}", cls="lbl", anchor="end")
    return cv.render()


def build_trapezoid(p: Params) -> str:
    """Hình thang: hai đáy a (dưới), b (trên), đường cao h."""
    a = float(p.get("a", 6))
    b = float(p.get("b", 3.4))
    height = float(p.get("height", 3))
    scale = 40.0
    pad = 48.0
    aw, bw, hh = a * scale, b * scale, height * scale
    ox, oy = pad, pad + hh
    off = (aw - bw) / 2
    A = (ox, oy)
    B = (ox + aw, oy)
    C = (ox + off + bw, oy - hh)
    D = (ox + off, oy - hh)
    cv = Canvas(aw + 2 * pad, hh + 2 * pad, title="Hình thang")
    cv.polygon([A, B, C, D], cls="fill-a")
    cv.polyline([A, B, C, D, A], cls="ink")
    cv.line(D[0], D[1], D[0], oy, cls="accent-b", extra=' stroke-dasharray="5 4" stroke-width="1.6"')
    cv.text((A[0] + B[0]) / 2, oy + 22, f"a = {_n(a)}", cls="lbl", anchor="middle")
    cv.text((D[0] + C[0]) / 2, D[1] - 8, f"b = {_n(b)}", cls="lbl", anchor="middle")
    cv.text(D[0] - 10, (D[1] + oy) / 2, f"h = {_n(height)}", cls="lbl", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# Hệ trục & đồ thị hàm
# --------------------------------------------------------------------------
class _Plot:
    """Ánh xạ toạ độ thế giới -> màn hình cho các đồ thị có trục."""

    def __init__(self, cv: Canvas, xmin, xmax, ymin, ymax, box):
        self.cv = cv
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax
        self.x0, self.y0, self.pw, self.ph = box  # góc trái-trên + rộng/cao vùng vẽ

    def sx(self, x):
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.pw

    def sy(self, y):
        return self.y0 + (self.ymax - y) / (self.ymax - self.ymin) * self.ph

    def axes(self, xlabel="x", ylabel="y"):
        cv = self.cv
        # lưới số nguyên
        gx = math.floor(self.xmin)
        while gx <= self.xmax:
            cv.line(self.sx(gx), self.y0, self.sx(gx), self.y0 + self.ph, cls="grid")
            gx += 1
        gy = math.floor(self.ymin)
        while gy <= self.ymax:
            cv.line(self.x0, self.sy(gy), self.x0 + self.pw, self.sy(gy), cls="grid")
            gy += 1
        # trục
        y_axis_x = self.sx(0) if self.xmin <= 0 <= self.xmax else self.x0
        x_axis_y = self.sy(0) if self.ymin <= 0 <= self.ymax else self.y0 + self.ph
        cv.arrow(self.x0, x_axis_y, self.x0 + self.pw + 6, x_axis_y, cls="axis", head=7)
        cv.arrow(y_axis_x, self.y0 + self.ph, y_axis_x, self.y0 - 6, cls="axis", head=7)
        cv.text(self.x0 + self.pw + 4, x_axis_y - 8, xlabel, cls="lbl", anchor="end")
        cv.text(y_axis_x + 8, self.y0 - 2, ylabel, cls="lbl")

    def plot_expr(self, expr, cls="curve"):
        pts = sample_curve(expr, "x", self.xmin, self.xmax, 120)
        screen = [(self.sx(x), self.sy(y)) for x, y in pts if self.ymin - 1 <= y <= self.ymax + 1]
        if screen:
            self.cv.polyline(screen, cls=cls)


def build_function_plot(p: Params) -> str:
    """Đồ thị y = f(x). ``expr`` là biểu thức theo x (vd ``x^2``, ``sin(x)``, ``2*x+1``)."""
    expr = str(p.get("expr", "x^2"))
    xmin = float(p.get("xmin", -4))
    xmax = float(p.get("xmax", 4))
    ymin = p.get("ymin")
    ymax = p.get("ymax")
    if ymin is None or ymax is None:
        pts = sample_curve(expr, "x", xmin, xmax, 80)
        ys = [y for _, y in pts] or [-1, 1]
        lo, hi = min(ys), max(ys)
        span = max(hi - lo, 1.0)
        ymin = math.floor(lo - 0.15 * span) if ymin is None else float(ymin)
        ymax = math.ceil(hi + 0.15 * span) if ymax is None else float(ymax)
    w, h = 380.0, 300.0
    box = (46.0, 24.0, w - 70, h - 60)
    cv = Canvas(w, h, title=f"Đồ thị y = {expr}")
    plot = _Plot(cv, xmin, xmax, float(ymin), float(ymax), box)
    plot.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    plot.plot_expr(expr)
    if p.get("label"):
        cv.text(box[0] + box[2] - 6, box[1] + 18, p["label"], cls="lbl", anchor="end")
    return cv.render()


def build_projectile(p: Params) -> str:
    """Quỹ đạo ném xiên: vận tốc đầu v0, góc ném (độ). Parabol + vectơ vận tốc đầu."""
    v0 = float(p.get("v0", 20))
    angle = float(p.get("angle", 45))
    g = float(p.get("g", 9.8))
    th = math.radians(angle)
    rng = v0 * v0 * math.sin(2 * th) / g
    hmax = (v0 * math.sin(th)) ** 2 / (2 * g)
    xmax = max(rng * 1.15, 1.0)
    ymax = max(hmax * 1.5, 1.0)
    w, h = 400.0, 280.0
    box = (44.0, 20.0, w - 66, h - 56)
    cv = Canvas(w, h, title="Chuyển động ném xiên")
    plot = _Plot(cv, 0, xmax, 0, ymax, box)
    plot.axes("x (m)", "y (m)")
    steps = 60
    pts = []
    for i in range(steps + 1):
        x = rng * i / steps
        y = x * math.tan(th) - g * x * x / (2 * (v0 * math.cos(th)) ** 2)
        pts.append((plot.sx(x), plot.sy(max(y, 0))))
    cv.polyline(pts, cls="curve")
    # vectơ vận tốc đầu
    ox, oy = plot.sx(0), plot.sy(0)
    vlen = 58.0
    cv.arrow(ox, oy, ox + vlen * math.cos(th), oy - vlen * math.sin(th), cls="accent-b", head=8)
    cv.text(ox + vlen * math.cos(th) + 6, oy - vlen * math.sin(th) - 4, "v₀", cls="lbl")
    # đỉnh
    apex = (plot.sx(rng / 2), plot.sy(hmax))
    cv.dot(*apex, r=3, cls="accent-c")
    cv.text(apex[0], apex[1] - 8, f"H = {_n(round(hmax, 2))} m", cls="lbl-sm", anchor="middle")
    cv.text(plot.sx(rng), oy + 16, f"L = {_n(round(rng, 2))} m", cls="lbl-sm", anchor="middle")
    cv.text(ox + 30, oy - 6, f"{_n(angle)}°", cls="lbl-sm")
    return cv.render()


def build_vector_add(p: Params) -> str:
    """Cộng hai vectơ theo quy tắc hình bình hành: u + v = w."""
    ux, uy = float(p.get("ux", 3)), float(p.get("uy", 1))
    vx, vy = float(p.get("vx", 1)), float(p.get("vy", 2.5))
    scale = 46.0
    allx = [0, ux, vx, ux + vx]
    ally = [0, uy, vy, uy + vy]
    pad = 44.0
    minx, maxx = min(allx), max(allx)
    miny, maxy = min(ally), max(ally)
    w = (maxx - minx) * scale + 2 * pad
    h = (maxy - miny) * scale + 2 * pad
    ox = pad - minx * scale
    oy = h - pad + miny * scale

    def P(x, y):
        return ox + x * scale, oy - y * scale

    cv = Canvas(w, h, title="Cộng vectơ")
    O = P(0, 0)
    U = P(ux, uy)
    V = P(vx, vy)
    W = P(ux + vx, uy + vy)
    cv.line(*U, *W, cls="ink-thin", extra=' stroke-dasharray="5 4"')
    cv.line(*V, *W, cls="ink-thin", extra=' stroke-dasharray="5 4"')
    cv.arrow(*O, *U, cls="accent-a", head=9)
    cv.arrow(*O, *V, cls="accent-c", head=9)
    cv.arrow(*O, *W, cls="accent-b", head=10)
    cv.text(U[0] + 6, U[1] - 4, p.get("label_u", "u"), cls="lbl")
    cv.text(V[0] - 6, V[1] - 4, p.get("label_v", "v"), cls="lbl", anchor="end")
    cv.text(W[0] + 6, W[1] - 4, p.get("label_w", "u + v"), cls="lbl")
    cv.dot(*O, r=3, cls="accent-b")
    return cv.render()


def build_number_line(p: Params) -> str:
    """Trục số với các điểm/khoảng được đánh dấu."""
    lo = float(p.get("min", -3))
    hi = float(p.get("max", 3))
    points = p.get("points", [{"x": 0, "label": "0"}])
    w, h = 420.0, 90.0
    pad = 32.0
    y = 52.0

    def sx(x):
        return pad + (x - lo) / (hi - lo) * (w - 2 * pad)

    cv = Canvas(w, h, title="Trục số")
    cv.arrow(pad - 8, y, w - pad + 8, y, cls="axis", head=7)
    t = math.floor(lo)
    while t <= hi:
        cv.line(sx(t), y - 5, sx(t), y + 5, cls="ink-thin")
        cv.text(sx(t), y + 22, _n(t), cls="lbl-sm", anchor="middle")
        t += 1
    for pt in points:
        px = sx(float(pt["x"]))
        filled = pt.get("filled", True)
        cv.circle(px, y, 5, cls="accent-b" if filled else "accent-b",
                  extra="" if filled else ' fill="var(--ill-bg,#fff)"')
        if pt.get("label"):
            cv.text(px, y - 14, str(pt["label"]), cls="lbl", anchor="middle")
    return cv.render()


def build_unit_circle(p: Params) -> str:
    """Đường tròn lượng giác: góc θ với hình chiếu sin/cos."""
    angle = float(p.get("angle", 45))
    th = math.radians(angle)
    R = 96.0
    pad = 40.0
    cx = cy = pad + R
    w = h = 2 * (pad + R)
    px, py = cx + R * math.cos(th), cy - R * math.sin(th)
    cv = Canvas(w, h, title="Đường tròn lượng giác")
    cv.arrow(cx - R - 12, cy, cx + R + 14, cy, cls="axis", head=7)
    cv.arrow(cx, cy + R + 12, cx, cy - R - 14, cls="axis", head=7)
    cv.circle(cx, cy, R, cls="ink")
    cv.path(f"M {_n(cx + 28)} {_n(cy)} A 28 28 0 0 0 {_n(cx + 28 * math.cos(th))} {_n(cy - 28 * math.sin(th))}",
            cls="accent-d", extra=' stroke-width="2"')
    cv.line(px, py, px, cy, cls="accent-b", extra=' stroke-dasharray="4 3" stroke-width="1.6"')  # sin
    cv.line(cx, cy, px, cy, cls="accent-c", extra=' stroke-width="2"')                              # cos
    cv.arrow(cx, cy, px, py, cls="accent-a", head=8)
    cv.dot(px, py, r=3.4, cls="accent-a")
    cv.text(px + 8, py - 6, f"({_n(round(math.cos(th),2))}; {_n(round(math.sin(th),2))})", cls="lbl-sm")
    cv.text(cx + 34, cy - 8, f"θ = {_n(angle)}°", cls="lbl-sm")
    cv.text((cx + px) / 2, cy + 16, "cos θ", cls="lbl-sm", anchor="middle")
    cv.text(px + 6, (py + cy) / 2, "sin θ", cls="lbl-sm")
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "right_triangle": build_right_triangle,
    "circle": build_circle,
    "rectangle": build_rectangle,
    "triangle": build_triangle,
    "parallelogram": build_parallelogram,
    "trapezoid": build_trapezoid,
    "function_plot": build_function_plot,
    "projectile": build_projectile,
    "vector_add": build_vector_add,
    "number_line": build_number_line,
    "unit_circle": build_unit_circle,
}


def render(generator: str, params: Params | None = None) -> str:
    if generator not in REGISTRY:
        raise KeyError(f"generator 2D không tồn tại: {generator}")
    return REGISTRY[generator](params or {})
