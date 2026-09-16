"""Họ **dothi** — đồ thị hàm số và giải tích (SVG deterministic).

Kho đã có ``function_plot`` (một hàm, khung trục trần). Ở đây là lớp hình *dạy được
đặc trưng*: cực trị, điểm uốn, tiệm cận, tiếp tuyến, diện tích dưới đường cong,
tổng Riemann, giới hạn một phía… Mỗi hình chỉ nói đúng một ý và nói cho hết ý đó.

Hai ràng buộc chi phối toàn bộ file:

* **Không có điểm nào được rơi ra ngoài khung.** Hàm phân thức, hàm mũ, tổng
  Riemann… đều có thể văng lên vô cùng, nên mọi đường cong đi qua bộ cắt
  ``_clip_y`` (cắt theo tham số, chèn đúng điểm biên) chứ không chỉ lọc điểm.
  Hình tràn khung là lỗi im lặng — trình duyệt không báo, người đọc thấy đường
  cụt lủn mà tưởng là hình đúng.
* **Tham số rác không được làm nổ generator.** Mọi khoá số đi qua ``_f`` và mọi
  biểu thức đi qua ``_compile`` (có biểu thức dự phòng), vì rule có thể truyền
  vào bất cứ thứ gì và một ngoại lệ ở tầng minh hoạ sẽ giết cả trang bài học.
"""

from __future__ import annotations

import math
from typing import Callable, Optional, Sequence

from .mathexpr import compile_expr
from .svgkit import Canvas, _n

Params = dict

DASH = ' stroke-dasharray="6 4"'
DASH_FINE = ' stroke-dasharray="3 3"'
THIN = ' stroke-width="1.4"'
# Đường cong thứ hai trong cùng một hình: màu lấy từ lớp accent-*, chỉ chặn fill
# bằng style. (polyline mang lớp có fill sẽ bị TÔ ĐẶC: CSS thắng fill="none".)
CURVE2 = ' style="fill:none" stroke-width="2.5"'


# ---------------------------------------------------------------------------
# Tiện ích số học dùng chung
# ---------------------------------------------------------------------------
def _f(v, default: float) -> float:
    """Ép ``v`` về float hữu hạn, rơi về ``default`` nếu không được.

    Rule có thể truyền None/chuỗi/nan; một ``float()`` trần ở đây là chỗ nổ
    thường gặp nhất của cả tầng minh hoạ.
    """
    try:
        x = float(v)
    except (TypeError, ValueError):
        return default
    return x if math.isfinite(x) else default


def _pos(v, default: float) -> float:
    """Như ``_f`` nhưng bắt buộc dương (bán kính, chu kì, cơ số…)."""
    x = _f(v, default)
    return x if x > 0 else default


def _compile(expr, fallback: str, var: str = "x") -> Callable[[float], float]:
    """Biên dịch biểu thức người dùng, hỏng thì dùng ``fallback``.

    ``compile_expr`` đã whitelist AST nên chỗ này chỉ lo chuyện biểu thức sai
    cú pháp/sai tên biến — vẫn phải trả về hình chứ không được ném ra ngoài.
    """
    for candidate in (expr, fallback):
        try:
            return compile_expr(str(candidate), (var,))
        except (ValueError, TypeError):
            continue
    return lambda x: 0.0


def _at(fn: Callable[[float], float], x: float) -> Optional[float]:
    """Giá trị hàm tại x, hoặc None nếu không xác định (chia 0, log âm, tràn số)."""
    try:
        y = fn(x)
    except (ValueError, ZeroDivisionError, OverflowError, ArithmeticError):
        return None
    return y if math.isfinite(y) else None


def _val(fn, x: float, default: float = 0.0) -> float:
    """Giá trị hàm tại x, thay bằng ``default`` khi không xác định.

    KHÔNG viết ``_at(fn, x) or default``: giá trị 0.0 hợp lệ cũng bị nuốt, và ở
    chỗ tìm nghiệm điều đó đẻ ra một nghiệm giả ngay tại nơi hàm bằng 0 — đúng
    kiểu lỗi chỉ lộ ra khi nhìn hình (đã bắt được một ca như vậy ở đồ thị cắt
    bởi đường y = m).
    """
    v = _at(fn, x)
    return default if v is None else v


def _samples(fn, lo: float, hi: float, n: int) -> list[tuple[float, Optional[float]]]:
    """Lấy mẫu đều; điểm không xác định giữ lại dưới dạng None để cắt đứt đường."""
    n = max(int(n), 2)
    step = (hi - lo) / (n - 1)
    return [(lo + i * step, _at(fn, lo + i * step)) for i in range(n)]


def _clip_y(pts: Sequence[tuple[float, Optional[float]]], ymin: float, ymax: float
            ) -> list[list[tuple[float, float]]]:
    """Cắt dãy mẫu theo dải ``[ymin; ymax]``, trả về các đoạn liên tục.

    Cắt theo tham số (chèn đúng giao điểm với biên) chứ không lọc điểm: nếu chỉ
    lọc, nhánh tiệm cận sẽ dừng sớm và người đọc thấy một khoảng trống không có
    thật giữa đường cong và tiệm cận.
    """
    out: list[list[tuple[float, float]]] = []
    cur: list[tuple[float, float]] = []
    for i in range(len(pts) - 1):
        (x0, y0), (x1, y1) = pts[i], pts[i + 1]
        if y0 is None or y1 is None:
            if len(cur) >= 2:
                out.append(cur)
            cur = []
            continue
        t0, t1, dy = 0.0, 1.0, y1 - y0
        ok = True
        for sign, bound in ((1.0, ymax), (-1.0, ymin)):
            p, q = sign * dy, sign * bound - sign * y0
            if abs(p) < 1e-12:
                if q < 0:
                    ok = False
                    break
            else:
                r = q / p
                if p < 0:
                    t0 = max(t0, r)
                else:
                    t1 = min(t1, r)
        if not ok or t0 > t1:
            if len(cur) >= 2:
                out.append(cur)
            cur = []
            continue
        a = (x0 + t0 * (x1 - x0), y0 + t0 * dy)
        b = (x0 + t1 * (x1 - x0), y0 + t1 * dy)
        if not cur:
            cur = [a]
        elif abs(cur[-1][0] - a[0]) > 1e-9 or abs(cur[-1][1] - a[1]) > 1e-9:
            if len(cur) >= 2:
                out.append(cur)
            cur = [a]
        cur.append(b)
    if len(cur) >= 2:
        out.append(cur)
    return out


def _deriv(fn, x: float, h: float = 1e-5) -> float:
    """Đạo hàm số bằng sai phân trung tâm (đủ chính xác để vẽ tiếp tuyến)."""
    a, b = _at(fn, x + h), _at(fn, x - h)
    if a is None or b is None:
        a2, b2 = _at(fn, x + h), _at(fn, x)
        if a2 is None or b2 is None:
            return 0.0
        return (a2 - b2) / h
    return (a - b) / (2 * h)


def _roots(fn, lo: float, hi: float, n: int = 300) -> list[float]:
    """Nghiệm gần đúng trên [lo;hi]: quét đổi dấu rồi chia đôi. Tất định."""
    out: list[float] = []
    prev_x, prev_y = None, None
    for i in range(n + 1):
        x = lo + (hi - lo) * i / n
        y = _at(fn, x)
        if y is not None and prev_y is not None and prev_y * y <= 0 and prev_y != y:
            a, b, fa = prev_x, x, prev_y
            for _ in range(60):
                m = (a + b) / 2
                ym = _at(fn, m)
                if ym is None:
                    break
                if fa * ym <= 0:
                    b = m
                else:
                    a, fa = m, ym
            out.append(round((a + b) / 2, 9))
        if y is not None:
            prev_x, prev_y = x, y
    # gộp nghiệm trùng do quét dày
    uniq: list[float] = []
    for r in out:
        if not uniq or abs(r - uniq[-1]) > (hi - lo) * 1e-4:
            uniq.append(r)
    return uniq


def _integral(fn, a: float, b: float, n: int = 400) -> float:
    """Tích phân số (Simpson) — chỉ dùng để đặt nhãn giá trị trung bình."""
    n = max(2, n + (n % 2))
    h = (b - a) / n
    total = 0.0
    for i in range(n + 1):
        y = _at(fn, a + i * h)
        if y is None:
            continue
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        total += w * y
    return total * h / 3


def _span(values: Sequence[float], pad: float = 0.14, minspan: float = 1.0) -> tuple[float, float]:
    """Khoảng hiển thị bao trọn ``values`` kèm lề, không bao giờ suy biến."""
    vals = [v for v in values if v is not None and math.isfinite(v)]
    if not vals:
        return -1.0, 1.0
    lo, hi = min(vals), max(vals)
    if hi - lo < minspan:
        mid = (lo + hi) / 2
        lo, hi = mid - minspan / 2, mid + minspan / 2
    d = (hi - lo) * pad
    return lo - d, hi + d


def _grid_step(span: float) -> float:
    """Bước lưới "đẹp" (1/2/5 × 10^k) sao cho có 4–8 vạch."""
    if not math.isfinite(span) or span <= 0:
        return 1.0
    raw = span / 6.0
    mag = 10.0 ** math.floor(math.log10(raw)) if raw > 0 else 1.0
    for m in (1.0, 2.0, 5.0):
        if raw <= m * mag:
            return m * mag
    return 10.0 * mag


def _fmt(v: float) -> str:
    return _n(round(float(v), 3))


# ---------------------------------------------------------------------------
# Khung toạ độ
# ---------------------------------------------------------------------------
class _Frame:
    """Ánh xạ toạ độ thế giới → pixel + các nét lặp lại của hình đồ thị."""

    def __init__(self, cv: Canvas, xmin, xmax, ymin, ymax, box):
        self.cv = cv
        self.xmin, self.xmax = float(xmin), float(xmax)
        self.ymin, self.ymax = float(ymin), float(ymax)
        if self.xmax - self.xmin < 1e-9:
            self.xmax = self.xmin + 1.0
        if self.ymax - self.ymin < 1e-9:
            self.ymax = self.ymin + 1.0
        self.bx, self.by, self.pw, self.ph = box

    # -- đổi toạ độ -------------------------------------------------------
    def sx(self, x: float) -> float:
        t = (float(x) - self.xmin) / (self.xmax - self.xmin)
        return self.bx + min(max(t, 0.0), 1.0) * self.pw

    def sy(self, y: float) -> float:
        t = (self.ymax - float(y)) / (self.ymax - self.ymin)
        return self.by + min(max(t, 0.0), 1.0) * self.ph

    @property
    def axis_y(self) -> float:
        """Tung độ pixel của trục hoành (nếu y = 0 nằm ngoài khung thì lấy đáy)."""
        return self.sy(0) if self.ymin <= 0 <= self.ymax else self.by + self.ph

    @property
    def axis_x(self) -> float:
        return self.sx(0) if self.xmin <= 0 <= self.xmax else self.bx

    # -- nét nền ----------------------------------------------------------
    def _head(self, x, y, dx, dy, cls="axis", size=7.0):
        """Đầu mũi tên vẽ bằng hai nét (chevron), không tô.

        Không dùng tam giác tô đặc: lớp ``.axis`` đặt ``fill:none`` nên muốn tô
        thì phải nhét mã màu thẳng vào hình, mà mã màu cứng thì hình hết tự lật
        được theo nền sáng/tối.
        """
        ang = math.atan2(dy, dx)
        a1, a2 = ang + math.radians(150), ang - math.radians(150)
        self.cv.polyline(
            [(x + size * math.cos(a1), y + size * math.sin(a1)), (x, y),
             (x + size * math.cos(a2), y + size * math.sin(a2))],
            cls=cls, extra=' style="fill:none"')

    def axes(self, xlabel: str = "x", ylabel: str = "y", ticks: bool = True,
             origin: bool = True, skip_x: Sequence[float] = (), skip_y: Sequence[float] = ()
             ) -> None:
        """Vẽ lưới, trục và số trên trục.

        ``skip_x``/``skip_y`` là các vị trí đã có nhãn riêng (a, b, x₀, nghiệm…):
        số trên trục ở gần đó bị bỏ, nếu không hai chữ đè lên nhau và cả hai
        cùng không đọc được — lỗi này chỉ lộ ra khi nhìn ảnh, không lộ khi đọc mã.
        """
        cv = self.cv
        xs, ys = _grid_step(self.xmax - self.xmin), _grid_step(self.ymax - self.ymin)
        k = math.ceil(self.xmin / xs - 1e-9)
        while k * xs <= self.xmax + 1e-9:
            cv.line(self.sx(k * xs), self.by, self.sx(k * xs), self.by + self.ph, cls="grid")
            k += 1
        k = math.ceil(self.ymin / ys - 1e-9)
        while k * ys <= self.ymax + 1e-9:
            cv.line(self.bx, self.sy(k * ys), self.bx + self.pw, self.sy(k * ys), cls="grid")
            k += 1
        ay, ax = self.axis_y, self.axis_x
        cv.line(self.bx - 6, ay, self.bx + self.pw + 8, ay, cls="axis")
        self._head(self.bx + self.pw + 8, ay, 1, 0)
        cv.line(ax, self.by + self.ph + 6, ax, self.by - 8, cls="axis")
        self._head(ax, self.by - 8, 0, -1)
        cv.text(self.bx + self.pw + 6, ay - 9, xlabel, cls="lbl", anchor="end")
        cv.text(ax + 7, self.by - 1, ylabel, cls="lbl")
        if ticks:
            def _pair(item):
                return item if isinstance(item, (tuple, list)) else (item, 20.0)
            busy_x = [(self.sx(v), r) for v, r in map(_pair, skip_x)
                      if self.xmin <= v <= self.xmax]
            busy_y = [self.sy(v) for v in skip_y if self.ymin <= v <= self.ymax]
            k = math.ceil(self.xmin / xs - 1e-9)
            while k * xs <= self.xmax + 1e-9:
                v = k * xs
                if abs(v) > 1e-9:
                    cv.line(self.sx(v), ay - 3, self.sx(v), ay + 3, cls="axis")
                    if all(abs(self.sx(v) - b) > r for b, r in busy_x):
                        cv.text(self.sx(v), ay + 15, _fmt(v), cls="lbl-sm", anchor="middle")
                k += 1
            k = math.ceil(self.ymin / ys - 1e-9)
            while k * ys <= self.ymax + 1e-9:
                v = k * ys
                if abs(v) > 1e-9:
                    cv.line(ax - 3, self.sy(v), ax + 3, self.sy(v), cls="axis")
                    if all(abs(self.sy(v) - b) > 12 for b in busy_y):
                        cv.text(ax - 7, self.sy(v) + 4, _fmt(v), cls="lbl-sm", anchor="end")
                k += 1
        near_origin = any(abs(self.sx(v[0] if isinstance(v, (tuple, list)) else v) - ax) < 26
                          for v in skip_x)
        if origin and not near_origin and self.xmin <= 0 <= self.xmax and self.ymin <= 0 <= self.ymax:
            cv.text(ax - 7, ay + 15, "O", cls="lbl-sm", anchor="end")

    # -- nội dung ---------------------------------------------------------
    def curve(self, fn, cls: str = "curve", n: int = 241, lo=None, hi=None, extra: str = "") -> None:
        lo = self.xmin if lo is None else max(float(lo), self.xmin)
        hi = self.xmax if hi is None else min(float(hi), self.xmax)
        if hi <= lo:
            return
        for seg in _clip_y(_samples(fn, lo, hi, n), self.ymin, self.ymax):
            self.cv.polyline([(self.sx(x), self.sy(y)) for x, y in seg], cls=cls, extra=extra)

    def line(self, x1, y1, x2, y2, cls="ink-thin", extra="") -> None:
        """Đoạn thẳng theo toạ độ thế giới, cắt gọn theo khung.

        Chặn fill ngay tại đây: đoạn hai điểm thì fill vô hại, nhưng nếu sau này
        ai đó truyền vào đường gấp khúc với lớp accent-* thì nó sẽ bị tô đặc
        (CSS thắng thuộc tính ``fill="none"`` mà Canvas sinh ra).
        """
        if "style=" not in extra:
            extra = ' style="fill:none"' + extra
        for seg in _clip_y([(x1, y1), (x2, y2)], self.ymin, self.ymax):
            self.cv.polyline([(self.sx(x), self.sy(y)) for x, y in seg], cls=cls, extra=extra)

    def vdash(self, x, y1, y2, cls="ink-thin", extra=DASH) -> None:
        y1 = min(max(y1, self.ymin), self.ymax)
        y2 = min(max(y2, self.ymin), self.ymax)
        self.cv.line(self.sx(x), self.sy(y1), self.sx(x), self.sy(y2), cls=cls, extra=extra + THIN)

    def hdash(self, y, x1, x2, cls="ink-thin", extra=DASH) -> None:
        x1 = min(max(x1, self.xmin), self.xmax)
        x2 = min(max(x2, self.xmin), self.xmax)
        self.cv.line(self.sx(x1), self.sy(y), self.sx(x2), self.sy(y), cls=cls, extra=extra + THIN)

    def point(self, x, y, cls="accent-b", r=3.6, hollow=False) -> None:
        if not (self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax):
            return
        if hollow:
            # rỗng = KHÔNG thuộc đồ thị; tô "none" để đúng ở cả nền sáng lẫn nền tối
            self.cv.circle(self.sx(x), self.sy(y), r, cls=cls,
                           extra=' style="fill:none" stroke-width="2"')
        else:
            self.cv.dot(self.sx(x), self.sy(y), r, cls=cls)

    def area(self, pts: Sequence[tuple[float, float]], cls="fill-a") -> None:
        if len(pts) >= 3:
            self.cv.polygon([(self.sx(x), self.sy(min(max(y, self.ymin), self.ymax)))
                             for x, y in pts], cls=cls)

    def text(self, x, y, s, cls="lbl-sm", anchor="middle", dx=0.0, dy=0.0) -> None:
        if not str(s):
            return
        px = min(max(self.sx(x) + dx, 4.0), self.cv.w - 4.0)
        py = min(max(self.sy(y) + dy, 12.0), self.cv.h - 4.0)
        self.cv.text(px, py, s, cls=cls, anchor=anchor)


def _mk(title: str, desc: str, xmin, xmax, ymin, ymax,
        w: float = 400.0, h: float = 300.0,
        left: float = 54.0, right: float = 30.0, top: float = 28.0, bottom: float = 44.0
        ) -> tuple[Canvas, _Frame]:
    cv = Canvas(w, h, title=title, desc=desc)
    return cv, _Frame(cv, xmin, xmax, ymin, ymax, (left, top, w - left - right, h - top - bottom))


def _caption(cv: Canvas, text: str) -> None:
    """Nhãn công thức đặt góc trên-phải, không chồng lên vùng vẽ."""
    if text:
        cv.text(cv.w - 8, 17, text, cls="lbl", anchor="end")


def _auto_y(fn, xmin, xmax, extra: Sequence[float] = ()) -> tuple[float, float]:
    """Khoảng y bao được phần "thân" đường cong, bỏ đuôi văng lên vô cùng.

    Lấy phân vị thay vì min/max để một điểm sát tiệm cận không nén bẹp cả hình.
    """
    ys = sorted(y for _, y in _samples(fn, xmin, xmax, 201) if y is not None)
    if not ys:
        return -1.0, 1.0
    lo = ys[int(0.05 * (len(ys) - 1))]
    hi = ys[int(0.95 * (len(ys) - 1))]
    return _span(list((lo, hi)) + list(extra))


# ---------------------------------------------------------------------------
# 1. Đa thức: bậc ba, trùng phương, parabol
# ---------------------------------------------------------------------------
def build_cubic(p: Params) -> str:
    """Đồ thị bậc ba y = ax³+bx²+cx+d: hai cực trị (hoặc không), điểm uốn/tâm đối xứng.

    ``mark``: "extrema" | "inflection" | "both" | "none"; ``horizontal_tangents``
    vẽ tiếp tuyến ngang tại cực trị (minh hoạ f'(x₀) = 0).
    """
    a = _f(p.get("a", 1), 1.0) or 1.0
    b, c, d = _f(p.get("b", 0), 0.0), _f(p.get("c", -3), -3.0), _f(p.get("d", 1), 1.0)
    mark = str(p.get("mark", "extrema"))
    fn = lambda x: ((a * x + b) * x + c) * x + d  # noqa: E731 - Horner cho gọn
    disc = b * b - 3 * a * c
    xi = -b / (3 * a)                      # hoành độ điểm uốn = tâm đối xứng
    crit: list[float] = []
    if disc > 0:
        r = math.sqrt(disc)
        crit = sorted(((-b - r) / (3 * a), (-b + r) / (3 * a)))
    half = max(abs(xi) + 1.0, (max(abs(x) for x in crit) + 1.2) if crit else 2.2)
    xmin, xmax = xi - half, xi + half
    ymin, ymax = _auto_y(fn, xmin, xmax, [fn(x) for x in crit] + [fn(xi)])
    cv, fr = _mk("Đồ thị hàm bậc ba",
                 "Đường cong bậc ba với cực đại, cực tiểu và điểm uốn được đánh dấu.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.curve(fn)
    if mark in ("extrema", "both") and crit:
        names = ("CĐ", "CT") if a > 0 else ("CT", "CĐ")
        for x, name in zip(crit, names):
            y = fn(x)
            fr.point(x, y, cls="accent-b")
            fr.text(x, y, f"{name} ({_fmt(x)}; {_fmt(y)})", dy=-10 if name == "CĐ" else 18)
            if p.get("horizontal_tangents"):
                dx = (xmax - xmin) * 0.12
                fr.line(x - dx, y, x + dx, y, cls="accent-d", extra=THIN)
    if mark in ("inflection", "both"):
        fr.point(xi, fn(xi), cls="accent-c")
        fr.text(xi, fn(xi), p.get("inflection_label", "U (điểm uốn)"), dx=8, dy=-8, anchor="start")
    if not crit and mark != "inflection":
        fr.text((xmin + xmax) / 2, ymin, "y' không đổi dấu → hàm đơn điệu", dy=-8)
    _caption(cv, p.get("label", "y = ax³ + bx² + cx + d"))
    return cv.render()


def build_quartic(p: Params) -> str:
    """Đồ thị trùng phương y = ax⁴+bx²+c: đối xứng qua Oy, một hoặc ba cực trị."""
    a = _f(p.get("a", 1), 1.0) or 1.0
    b, c = _f(p.get("b", -2), -2.0), _f(p.get("c", 1), 1.0)
    fn = lambda x: (a * x * x + b) * x * x + c  # noqa: E731
    crit = [0.0]
    if -b / (2 * a) > 0:
        crit = sorted([-math.sqrt(-b / (2 * a)), 0.0, math.sqrt(-b / (2 * a))])
    half = max(abs(x) for x in crit) * 1.6 + 0.9
    xmin, xmax = -half, half
    ymin, ymax = _auto_y(fn, xmin, xmax, [fn(x) for x in crit])
    cv, fr = _mk("Đồ thị hàm trùng phương",
                 "Đường cong trùng phương đối xứng qua trục tung, các cực trị được đánh dấu.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=crit)
    fr.vdash(0, ymin, ymax, cls="accent-d")
    fr.curve(fn)
    for x in crit:
        y = fn(x)
        fr.point(x, y, cls="accent-b")
        up = _deriv(lambda t: _deriv(fn, t), x) > 0   # lõm lên → cực tiểu
        fr.text(x, y, f"({_fmt(x)}; {_fmt(y)})", dy=16 if up else -10)
    fr.text(0, ymax, "trục đối xứng Oy", dy=14, dx=6, anchor="start")
    _caption(cv, p.get("label", "y = ax⁴ + bx² + c"))
    return cv.render()


def build_parabola(p: Params) -> str:
    """Parabol y = ax²+bx+c: đỉnh I, trục đối xứng, nghiệm, miền dấu.

    ``shade``: "between" (giữa hai nghiệm) | "outside" | "all" | "" — dùng cho
    bất phương trình bậc hai và tam thức luôn dương/luôn âm.
    """
    a = _f(p.get("a", 1), 1.0) or 1.0
    b, c = _f(p.get("b", -2), -2.0), _f(p.get("c", -3), -3.0)
    fn = lambda x: (a * x + b) * x + c  # noqa: E731
    xv = -b / (2 * a)
    yv = fn(xv)
    disc = b * b - 4 * a * c
    roots = sorted([(-b - math.sqrt(disc)) / (2 * a), (-b + math.sqrt(disc)) / (2 * a)]) if disc > 0 \
        else ([xv] if abs(disc) < 1e-12 else [])
    half = max((abs(r - xv) for r in roots), default=1.0) * 1.9 + 1.0
    xmin, xmax = xv - half, xv + half
    ymin, ymax = _auto_y(fn, xmin, xmax, [yv, 0.0])
    cv, fr = _mk("Parabol y = ax² + bx + c",
                 "Parabol với đỉnh, trục đối xứng và giao điểm với trục hoành.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=list(roots) + [xv])
    shade = str(p.get("shade", ""))
    if shade:
        parts = []
        if shade == "between" and len(roots) == 2:
            parts = [(roots[0], roots[1])]
        elif shade == "outside" and len(roots) == 2:
            parts = [(xmin, roots[0]), (roots[1], xmax)]
        elif shade == "all":
            parts = [(xmin, xmax)]
        for lo, hi in parts:
            pts = [(x, y) for x, y in _samples(fn, lo, hi, 60) if y is not None]
            if pts:
                fr.area([(lo, 0.0)] + pts + [(hi, 0.0)],
                        cls="fill-a" if a > 0 else "fill-b")
    if p.get("axis", True):
        fr.vdash(xv, ymin, ymax, cls="accent-d")
        fr.text(xv, ymax, f"x = {_fmt(xv)}", dy=14, dx=5, anchor="start")
    fr.curve(fn)
    if p.get("vertex", True):
        fr.point(xv, yv, cls="accent-b")
        fr.text(xv, yv, f"I({_fmt(xv)}; {_fmt(yv)})", dy=-10 if a > 0 else 18)
    if p.get("roots", True):
        for i, r in enumerate(roots):
            fr.point(r, 0.0, cls="accent-c", r=3.2)
            fr.text(r, 0.0, f"x{'₁₂'[i] if i < 2 else ''}", dy=-8)
    _caption(cv, p.get("label", "y = ax² + bx + c"))
    return cv.render()


# ---------------------------------------------------------------------------
# 2. Phân thức & tiệm cận
# ---------------------------------------------------------------------------
def build_rational(p: Params) -> str:
    """Phân thức bậc nhất/bậc nhất y = (ax+b)/(cx+d): hai nhánh, TCĐ và TCN vẽ đứt."""
    a, b = _f(p.get("a", 1), 1.0), _f(p.get("b", 2), 2.0)
    c = _f(p.get("c", 1), 1.0) or 1.0
    d = _f(p.get("d", -1), -1.0)
    if abs(a * d - b * c) < 1e-12:      # suy biến thành hằng số → về mặc định
        a, b, c, d = 1.0, 2.0, 1.0, -1.0
    fn = lambda x: (a * x + b) / (c * x + d)  # noqa: E731
    xv, yh = -d / c, a / c                     # tiệm cận đứng / ngang
    half = _pos(p.get("half_width", 3.4), 3.4)
    xmin, xmax = xv - half, xv + half
    ymin, ymax = yh - half * abs(a * d - b * c) / (c * c) * 1.2 - 1.0, \
        yh + half * abs(a * d - b * c) / (c * c) * 1.2 + 1.0
    ymin, ymax = _span([ymin, ymax, 0.0], pad=0.05)
    cv, fr = _mk("Đồ thị hàm phân thức bậc nhất",
                 "Hai nhánh hypebol cùng tiệm cận đứng và tiệm cận ngang vẽ nét đứt.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.vdash(xv, ymin, ymax, cls="accent-b")
    fr.hdash(yh, xmin, xmax, cls="accent-c")
    eps = (xmax - xmin) * 1e-3
    fr.curve(fn, lo=xmin, hi=xv - eps)
    fr.curve(fn, lo=xv + eps, hi=xmax)
    fr.text(xv, ymax, f"TCĐ: x = {_fmt(xv)}", dx=6, dy=14, anchor="start")
    fr.text(xmin, yh, f"TCN: y = {_fmt(yh)}", dx=6, dy=-8, anchor="start")
    if p.get("center"):
        fr.point(xv, yh, cls="accent-d")
        fr.text(xv, yh, p.get("center_label", "I"), dx=8, dy=16, anchor="start")
    _caption(cv, p.get("label", "y = (ax + b)/(cx + d)"))
    return cv.render()


def build_oblique_asymptote(p: Params) -> str:
    """Đồ thị y = mx + n + k/(x−q): tiệm cận xiên y = mx + n và tiệm cận đứng x = q."""
    m = _f(p.get("m", 1), 1.0)
    n = _f(p.get("n", 0), 0.0)
    k = _f(p.get("k", 1), 1.0) or 1.0
    q = _f(p.get("q", 1), 1.0)
    fn = lambda x: m * x + n + k / (x - q)  # noqa: E731
    half = _pos(p.get("half_width", 3.6), 3.6)
    xmin, xmax = q - half, q + half
    ymin, ymax = _span([m * xmin + n, m * xmax + n, 0.0], pad=0.35)
    cv, fr = _mk("Tiệm cận xiên",
                 "Đường cong áp sát đường thẳng xiên khi x ra vô cùng, và có tiệm cận đứng.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.vdash(q, ymin, ymax, cls="accent-b")
    fr.line(xmin, m * xmin + n, xmax, m * xmax + n, cls="accent-c", extra=DASH + THIN)
    eps = (xmax - xmin) * 1e-3
    fr.curve(fn, lo=xmin, hi=q - eps)
    fr.curve(fn, lo=q + eps, hi=xmax)
    fr.text(xmax, m * xmax + n, p.get("oblique_label", "y = ax + b"), dx=-6, dy=-8, anchor="end")
    fr.text(q, ymax, f"x = {_fmt(q)}", dx=-6, dy=14, anchor="end")
    _caption(cv, p.get("label", "tiệm cận xiên"))
    return cv.render()


def build_limit_infinity(p: Params) -> str:
    """Giới hạn tại vô cực: đường cong áp sát tiệm cận ngang y = y₀ khi x → ±∞."""
    expr = p.get("expr", "2 - 3/(x^2+1)")
    y0 = _f(p.get("y0", 2), 2.0)
    xmin, xmax = _f(p.get("xmin", -8), -8.0), _f(p.get("xmax", 8), 8.0)
    if xmax <= xmin:
        xmin, xmax = -8.0, 8.0
    fn = _compile(expr, "2 - 3/(x^2+1)")
    ymin, ymax = _auto_y(fn, xmin, xmax, [y0, 0.0])
    cv, fr = _mk("Giới hạn tại vô cực",
                 "Đường cong tiến sát đường nằm ngang y = y₀ khi x ra vô cùng.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.hdash(y0, xmin, xmax, cls="accent-b")
    fr.curve(fn)
    fr.text(xmax, y0, f"y = {_fmt(y0)}", dx=-4, dy=-8, anchor="end")
    fr.text(xmax, ymin, "x → +∞", dx=-4, dy=-8, anchor="end")
    fr.text(xmin, ymin, "x → −∞", dx=4, dy=-8, anchor="start")
    _caption(cv, p.get("label", "tiệm cận ngang"))
    return cv.render()


# ---------------------------------------------------------------------------
# 3. Mũ – logarit – logistic
# ---------------------------------------------------------------------------
def build_exp_log_pair(p: Params) -> str:
    """y = aˣ và y = log_a x đối xứng nhau qua đường y = x (quan hệ hàm ngược)."""
    a = _pos(p.get("base", 2), 2.0)
    if abs(a - 1.0) < 1e-9:
        a = 2.0
    ex = lambda x: a ** x            # noqa: E731
    lg = lambda x: math.log(x, a)    # noqa: E731
    lim = _pos(p.get("range", 4), 4.0)
    cv, fr = _mk("Hàm mũ và hàm logarit",
                 "Đồ thị hàm mũ và hàm logarit cùng cơ số, đối xứng qua đường thẳng y = x.",
                 -lim, lim, -lim, lim, w=340.0, h=340.0)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.line(-lim, -lim, lim, lim, cls="ink-thin", extra=DASH)
    fr.curve(ex, cls="curve")
    fr.curve(lg, cls="accent-c", lo=1e-3, extra=CURVE2)
    fr.point(0, 1, cls="accent-a")
    fr.point(1, 0, cls="accent-c")
    fr.text(lim * 0.42, _val(ex, lim * 0.42), "y = aˣ", dx=6, dy=-4, anchor="start", cls="lbl")
    fr.text(lim * 0.8, _val(lg, lim * 0.8), "y = logₐx", dx=2, dy=18, anchor="middle", cls="lbl")
    fr.text(lim * 0.72, lim * 0.72, "y = x", dx=8, dy=12, anchor="start")
    return cv.render()


def build_base_family(p: Params) -> str:
    """Hai đồ thị cùng họ với a > 1 và 0 < a < 1 — cho thấy chiều biến thiên theo cơ số.

    ``kind``: "exp" (y = aˣ) hoặc "log" (y = log_a x).
    """
    kind = "log" if str(p.get("kind", "exp")).startswith("log") else "exp"
    a = _pos(p.get("base", 2), 2.0)
    if abs(a - 1.0) < 1e-9:
        a = 2.0
    if kind == "exp":
        up = lambda x: a ** x           # noqa: E731
        dn = lambda x: (1 / a) ** x     # noqa: E731
        xmin, xmax = -2.6, 2.6
        ymin, ymax = -0.6, a ** 2.6
        t_up, t_dn = "y = aˣ (a > 1): đồng biến", "y = aˣ (0 < a < 1): nghịch biến"
    else:
        up = lambda x: math.log(x, a)        # noqa: E731
        dn = lambda x: math.log(x, 1 / a)    # noqa: E731
        xmin, xmax = -0.4, 6.0
        ymin, ymax = -3.0, 3.0
        t_up, t_dn = "y = log_a x (a > 1): đồng biến", "y = log_a x (0 < a < 1): nghịch biến"
    cv, fr = _mk("So sánh theo cơ số",
                 "Hai đường cong cùng họ ứng với cơ số lớn hơn 1 và cơ số nằm giữa 0 và 1.",
                 xmin, xmax, ymin, ymax, h=310.0, bottom=54.0)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    lo = 1e-3 if kind == "log" else None
    fr.curve(up, cls="curve", lo=lo)
    fr.curve(dn, cls="accent-b", lo=lo, extra=CURVE2)
    cv.text(58, cv.h - 22, t_up, cls="lbl-sm", anchor="start")
    cv.text(58, cv.h - 8, t_dn, cls="lbl-sm", anchor="start")
    cv.line(40, cv.h - 26, 54, cv.h - 26, cls="accent-a", extra=' stroke-width="2.5"')
    cv.line(40, cv.h - 12, 54, cv.h - 12, cls="accent-b", extra=' stroke-width="2.5"')
    return cv.render()


def build_exp_growth(p: Params) -> str:
    """Tăng trưởng/suy giảm theo hàm mũ y = y₀·e^{kt} (k > 0 tăng, k < 0 giảm).

    ``discrete=True`` vẽ dãy điểm rời rạc (lãi kép theo kì) thay vì đường liền —
    giá trị chỉ tồn tại ở các mốc nguyên, vẽ liền nét là nói sai.
    """
    y0 = _pos(p.get("y0", 1), 1.0)
    k = _f(p.get("k", 0.45), 0.45)
    discrete = bool(p.get("discrete"))
    periods = max(2, min(int(_pos(p.get("periods", 8), 8.0)), 20))
    rate = _f(p.get("r", 0.25), 0.25)
    fn = lambda t: y0 * math.exp(k * t)  # noqa: E731
    if discrete:
        tmax = float(periods)
        ys = [y0 * (1 + rate) ** i for i in range(periods + 1)]
    else:
        tmax = _pos(p.get("tmax", 6), 6.0)
        ys = [v for _, v in _samples(fn, 0, tmax, 60) if v is not None]
    ymin, ymax = _span([0.0] + ys, pad=0.1)
    ymin = min(ymin, 0.0)
    cv, fr = _mk("Tăng trưởng theo hàm mũ",
                 "Đường cong hàm mũ đi lên (hoặc đi xuống) từ giá trị ban đầu trên trục tung.",
                 -tmax * 0.06, tmax, ymin, ymax)
    fr.axes(p.get("xlabel", "t"), p.get("ylabel", p.get("ylabel", "y")))
    if discrete:
        for i in range(periods + 1):
            v = y0 * (1 + rate) ** i
            if v > ymax:
                break
            fr.vdash(i, 0, v, cls="ink-thin", extra=DASH_FINE)
            fr.point(i, v, cls="accent-b", r=3.2)
        fr.text(tmax / 2, ymax, p.get("note", "giá trị chỉ có ở cuối mỗi kì"), dy=14)
    else:
        fr.curve(fn)
        fr.point(0, y0, cls="accent-b")
        fr.text(0, y0, p.get("y0_label", "y₀"), dx=8, dy=-6, anchor="start")
        fr.text(tmax * 0.62, _val(fn, tmax * 0.62), p.get("curve_label", "y = y₀eᵏᵗ"),
                dx=-6, dy=14, anchor="end", cls="lbl")
    _caption(cv, p.get("label", ""))
    return cv.render()


def build_half_life(p: Params) -> str:
    """Phân rã theo chu kì bán rã: sau mỗi T, đại lượng còn một nửa (mốc T, 2T, 3T)."""
    m0 = _pos(p.get("m0", 100), 100.0)
    T = _pos(p.get("T", 1), 1.0)
    cycles = int(_pos(p.get("cycles", 3), 3.0))
    cycles = max(1, min(cycles, 5))
    fn = lambda t: m0 * 2 ** (-t / T)  # noqa: E731
    tmax = T * (cycles + 0.6)
    cv, fr = _mk("Chu kì bán rã",
                 "Đường cong phân rã: mỗi chu kì bán rã, đại lượng còn lại một nửa.",
                 -tmax * 0.05, tmax, -m0 * 0.12, m0 * 1.12)
    fr.axes(p.get("xlabel", "t"), p.get("ylabel", "m"), ticks=False)
    fr.curve(fn)
    fr.point(0, m0, cls="accent-b")
    fr.text(0, m0, p.get("m0_label", "m₀"), dx=8, dy=-6, anchor="start")
    for i in range(1, cycles + 1):
        t, v = i * T, m0 / (2 ** i)
        fr.vdash(t, 0, v, cls="accent-d")
        fr.hdash(v, 0, t, cls="accent-d")
        fr.point(t, v, cls="accent-b", r=3.2)
        fr.text(t, 0, f"{i if i > 1 else ''}T", dy=16)
        fr.text(0, v, f"m₀/{2 ** i}", dx=-6, dy=-5, anchor="end")
    _caption(cv, p.get("label", "m(t) = m₀·2^(−t/T)"))
    return cv.render()


def build_logistic(p: Params) -> str:
    """Đường cong logistic: chữ S, tiệm cận ngang y = L, điểm uốn ở mức L/2."""
    L = _pos(p.get("L", 100), 100.0)
    p0 = _pos(p.get("p0", 8), 8.0)
    if p0 >= L:
        p0 = L / 8
    k = _pos(p.get("k", 0.9), 0.9)
    A = (L - p0) / p0
    fn = lambda t: L / (1 + A * math.exp(-k * t))  # noqa: E731
    t_inf = math.log(A) / k if A > 0 else 0.0
    tmax = max(t_inf * 2.2, 4.0 / k)
    cv, fr = _mk("Đường cong logistic",
                 "Đường cong hình chữ S tiến tới sức chứa L, uốn tại mức L/2.",
                 -tmax * 0.04, tmax, -L * 0.12, L * 1.18)
    fr.axes(p.get("xlabel", "t"), p.get("ylabel", p.get("ylabel", "P")))
    fr.hdash(L, 0, tmax, cls="accent-b")
    fr.text(tmax, L, p.get("L_label", "y = L"), dx=-4, dy=-8, anchor="end")
    fr.curve(fn)
    fr.point(0, p0, cls="accent-c", r=3.2)
    fr.text(0, p0, p.get("p0_label", "P₀"), dx=8, dy=12, anchor="start")
    if 0 < t_inf < tmax:
        fr.hdash(L / 2, 0, t_inf, cls="accent-d")
        fr.vdash(t_inf, 0, L / 2, cls="accent-d")
        fr.point(t_inf, L / 2, cls="accent-d")
        fr.text(t_inf, L / 2, p.get("inflection_label", "điểm uốn: P = L/2"),
                dx=8, dy=-8, anchor="start")
    _caption(cv, p.get("label", ""))
    return cv.render()


# ---------------------------------------------------------------------------
# 4. Giao điểm & nghiệm đọc trên đồ thị
# ---------------------------------------------------------------------------
def build_horizontal_cut(p: Params) -> str:
    """Số nghiệm của f(x) = m = số giao điểm của (C): y = f(x) với đường thẳng y = m."""
    expr = p.get("expr", "x^3-3*x")
    m = _f(p.get("m", 1), 1.0)
    xmin, xmax = _f(p.get("xmin", -2.6), -2.6), _f(p.get("xmax", 2.6), 2.6)
    if xmax <= xmin:
        xmin, xmax = -2.6, 2.6
    fn = _compile(expr, "x^3-3*x")
    ymin, ymax = _auto_y(fn, xmin, xmax, [m, 0.0])
    cv, fr = _mk("Nghiệm phương trình đọc trên đồ thị",
                 "Đường thẳng nằm ngang cắt đồ thị; mỗi giao điểm là một nghiệm.",
                 xmin, xmax, ymin, ymax)
    roots = _roots(lambda x: fn(x) - m, xmin, xmax)
    room = 20.0 + 3.5 * len(str(p.get("root_label", "")))
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[(r, room) for r in roots])
    fr.hdash(m, xmin, xmax, cls="accent-b")
    fr.text(xmin, m, p.get("line_label", f"y = {_fmt(m)}"), dx=4, dy=-8, anchor="start")
    fr.curve(fn)
    for r in roots:
        fr.point(r, m, cls="accent-d")
        fr.vdash(r, 0, m, cls="ink-thin", extra=DASH_FINE)
        fr.text(r, 0, p.get("root_label", _fmt(r)), dy=16)
    _caption(cv, p.get("label", ""))
    return cv.render()


def build_graph_intersection(p: Params) -> str:
    """Tương giao hai đồ thị: hoành độ giao điểm là nghiệm của f(x) = g(x)."""
    f_expr, g_expr = p.get("f", "x^2-1"), p.get("g", "x+1")
    xmin, xmax = _f(p.get("xmin", -2.6), -2.6), _f(p.get("xmax", 3.0), 3.0)
    if xmax <= xmin:
        xmin, xmax = -2.6, 3.0
    fn, gn = _compile(f_expr, "x^2-1"), _compile(g_expr, "x+1")
    lo1, hi1 = _auto_y(fn, xmin, xmax)
    lo2, hi2 = _auto_y(gn, xmin, xmax)
    ymin, ymax = _span([lo1, hi1, lo2, hi2, 0.0], pad=0.06)
    cv, fr = _mk("Tương giao hai đồ thị",
                 "Hai đường cong cắt nhau; mỗi giao điểm ứng với một nghiệm của phương trình.",
                 xmin, xmax, ymin, ymax)
    roots = _roots(lambda x: fn(x) - gn(x), xmin, xmax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=roots)
    fr.curve(fn)
    fr.curve(gn, cls="accent-c", extra=CURVE2)
    for r in roots:
        y = _at(fn, r)
        if y is not None:
            fr.point(r, y, cls="accent-b")
            fr.vdash(r, 0, y, cls="ink-thin", extra=DASH_FINE)
            fr.text(r, 0, _fmt(r), dy=16)
    fr.text(xmax, _val(fn, xmax), p.get("f_label", "y = f(x)"), dx=-6, dy=-8, anchor="end")
    fr.text(xmin, _val(gn, xmin), p.get("g_label", "y = g(x)"), dx=6, dy=16, anchor="start")
    return cv.render()


def build_parity(p: Params) -> str:
    """Hai bảng cạnh nhau: hàm chẵn (đối xứng qua Oy) và hàm lẻ (đối xứng qua O)."""
    even_expr = p.get("even", "0.5*x^2-1")
    odd_expr = p.get("odd", "0.4*x^3-x")
    fe, fo = _compile(even_expr, "0.5*x^2-1"), _compile(odd_expr, "0.4*x^3-x")
    lim = _pos(p.get("range", 2.4), 2.4)
    cv = Canvas(660, 300, title="Hàm số chẵn và hàm số lẻ",
                desc="Hai đồ thị: hàm chẵn đối xứng qua trục tung, hàm lẻ đối xứng qua gốc toạ độ.")
    for i, (fn, kind) in enumerate(((fe, "chẵn"), (fo, "lẻ"))):
        ymin, ymax = _auto_y(fn, -lim, lim, [0.0])
        fr = _Frame(cv, -lim, lim, ymin, ymax, (44.0 + i * 330.0, 34.0, 256.0, 218.0))
        fr.axes("x", "y", ticks=False)
        fr.curve(fn)
        x1 = lim * 0.62
        y1 = _at(fn, x1)
        y2 = _at(fn, -x1)
        if y1 is not None and y2 is not None:
            fr.point(x1, y1, cls="accent-b")
            fr.point(-x1, y2, cls="accent-b")
            if kind == "chẵn":
                fr.hdash(y1, -x1, x1, cls="accent-d")
            else:
                fr.line(-x1, y2, x1, y1, cls="accent-d", extra=DASH + THIN)
            fr.vdash(x1, 0, y1, cls="ink-thin", extra=DASH_FINE)
            fr.vdash(-x1, 0, y2, cls="ink-thin", extra=DASH_FINE)
        cv.text(44.0 + i * 330.0 + 128, 22,
                "hàm chẵn: f(−x) = f(x)" if kind == "chẵn" else "hàm lẻ: f(−x) = −f(x)",
                cls="lbl", anchor="middle")
        cv.text(44.0 + i * 330.0 + 128, 290,
                "đối xứng qua trục Oy" if kind == "chẵn" else "đối xứng qua gốc O",
                cls="lbl-sm", anchor="middle")
    return cv.render()


# ---------------------------------------------------------------------------
# 5. Hàm cho theo từng khoảng, giới hạn, liên tục
# ---------------------------------------------------------------------------
def build_piecewise(p: Params) -> str:
    """Hàm cho theo từng khoảng: mỗi nhánh một biểu thức, đầu mút đặc/rỗng đúng quy ước.

    ``pieces``: [{"expr", "from", "to", "open_left", "open_right"}]. Mặc định là y = |x|.
    """
    pieces = p.get("pieces") or [
        {"expr": "-x", "from": -3, "to": 0, "open_right": False},
        {"expr": "x", "from": 0, "to": 3, "open_left": True},
    ]
    if not isinstance(pieces, (list, tuple)) or not pieces:
        pieces = [{"expr": "x", "from": -3, "to": 3}]
    prepared = []
    for piece in pieces:
        piece = piece if isinstance(piece, dict) else {}
        lo, hi = _f(piece.get("from", -3), -3.0), _f(piece.get("to", 3), 3.0)
        if hi <= lo:
            lo, hi = min(lo, hi), min(lo, hi) + 1.0
        prepared.append((_compile(piece.get("expr", "x"), "x"), lo, hi,
                         bool(piece.get("open_left")), bool(piece.get("open_right"))))
    xmin = min(lo for _, lo, _, _, _ in prepared)
    xmax = max(hi for _, _, hi, _, _ in prepared)
    ys: list[float] = []
    for fn, lo, hi, _, _ in prepared:
        ys += [v for _, v in _samples(fn, lo, hi, 40) if v is not None]
    ymin, ymax = _span(ys + [0.0])
    cv, fr = _mk(p.get("title", "Hàm cho theo từng khoảng"),
                 "Đồ thị gồm nhiều nhánh; đầu mút tô đặc là điểm thuộc đồ thị, rỗng là không thuộc.",
                 xmin - 0.2, xmax + 0.2, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    # Chấm đầu mút chỉ có nghĩa ở mối nối BÊN TRONG: chấm ở hai mút ngoài cùng sẽ
    # bảo người đọc rằng hàm chỉ xác định đến đó, mà thường thì không phải vậy.
    joints: dict[float, list[tuple[float, bool]]] = {}
    for fn, lo, hi, ol, orr in prepared:
        fr.curve(fn, lo=lo, hi=hi, n=121)
        for x, open_here in ((lo, ol), (hi, orr)):
            if abs(x - xmin) < 1e-9 or abs(x - xmax) < 1e-9:
                continue
            y = _at(fn, x)
            if y is not None:
                joints.setdefault(round(x, 9), []).append((y, open_here))
    for x, vals in joints.items():
        ys = [y for y, _ in vals]
        if max(ys) - min(ys) < 1e-9:
            continue        # hai nhánh gặp nhau: đồ thị liền nét, không chấm gì cả
        for y, open_here in vals:
            fr.point(x, y, cls="accent-b", hollow=open_here)
    _caption(cv, p.get("label", ""))
    return cv.render()


def build_one_sided_limit(p: Params) -> str:
    """Giới hạn một phía tại x₀: nhánh trái và nhánh phải, có/không gặp nhau.

    ``mode="jump"``: hai giới hạn khác nhau → không tồn tại giới hạn (hàm gián đoạn).
    ``mode="equal"``: hai giới hạn bằng nhau và bằng f(x₀) → hàm liên tục tại x₀.
    """
    mode = "equal" if str(p.get("mode", "jump")) == "equal" else "jump"
    x0 = _f(p.get("x0", 1), 1.0)
    left = p.get("left", "x+2" if mode == "jump" else "x^2")
    right = p.get("right", "x^2" if mode == "jump" else "2*x-1")
    fl, fr_ = _compile(left, "x+2"), _compile(right, "x^2")
    half = _pos(p.get("half_width", 2.0), 2.0)
    xmin, xmax = x0 - half, x0 + half
    ys = [v for _, v in _samples(fl, xmin, x0, 40) if v is not None]
    ys += [v for _, v in _samples(fr_, x0, xmax, 40) if v is not None]
    ymin, ymax = _span(ys + [0.0])
    cv, fr = _mk("Giới hạn một phía",
                 "Nhánh trái và nhánh phải của đồ thị quanh một điểm, kèm giá trị giới hạn hai phía.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.curve(fl, lo=xmin, hi=x0, n=121)
    fr.curve(fr_, lo=x0, hi=xmax, n=121)
    eps = half * 1e-4
    lv, rv = _at(fl, x0 - eps), _at(fr_, x0 + eps)
    fr.vdash(x0, ymin, ymax, cls="ink-thin")
    fr.text(x0, ymin, "x₀ = " + _fmt(x0), dy=16)
    if lv is not None:
        fr.point(x0, lv, cls="accent-b", hollow=(mode == "jump"))
        fr.hdash(lv, xmin, x0, cls="accent-b")
        fr.text(xmin, lv, p.get("left_label", "L⁻"), dx=4, dy=-6, anchor="start")
    if rv is not None:
        fr.point(x0, rv, cls="accent-c", hollow=(mode == "jump"))
        fr.hdash(rv, x0, xmax, cls="accent-c")
        fr.text(xmax, rv, p.get("right_label", "L⁺"), dx=-4, dy=-6, anchor="end")
    _caption(cv, p.get("label", "L⁻ ≠ L⁺ → không có giới hạn"
                       if mode == "jump" else "L⁻ = L⁺ = f(x₀) → liên tục"))
    return cv.render()


def build_limit_hole(p: Params) -> str:
    """Giới hạn tại điểm hàm không xác định: đồ thị có "lỗ thủng" ở x₀ nhưng vẫn tiến về L."""
    expr = p.get("expr", "sin(x)/x")
    x0 = _f(p.get("x0", 0), 0.0)
    L = _f(p.get("L", 1), 1.0)
    half = _pos(p.get("half_width", 6.0), 6.0)
    fn = _compile(expr, "sin(x)/x")
    xmin, xmax = x0 - half, x0 + half
    ymin, ymax = _auto_y(fn, xmin, xmax, [L, 0.0])
    cv, fr = _mk("Giới hạn tại điểm không xác định",
                 "Đồ thị có một lỗ thủng tại x₀ nhưng hai phía đều tiến về cùng một giá trị L.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[x0])
    gap = half * 0.012
    fr.curve(fn, lo=xmin, hi=x0 - gap, n=181)
    fr.curve(fn, lo=x0 + gap, hi=xmax, n=181)
    fr.hdash(L, xmin, x0, cls="accent-b")
    if abs(fr.sx(x0) - fr.axis_x) > 3:      # x₀ = 0 thì gióng đứng trùng luôn trục tung
        fr.vdash(x0, min(0.0, L), L, cls="accent-b")
    fr.point(x0, L, cls="accent-b", hollow=True)
    fr.text(xmin, L, f"L = {_fmt(L)}", dx=4, dy=-7, anchor="start")
    fr.text(x0, 0.0, p.get("x0_label", "x₀"), dy=16, dx=8)
    _caption(cv, p.get("label", ""))
    return cv.render()


def build_sequence_limit(p: Params) -> str:
    """Dãy số hội tụ: các điểm u_n dồn về đường nằm ngang y = L khi n tăng."""
    expr = p.get("expr", "1/n")
    L = _f(p.get("L", 0), 0.0)
    N = int(_pos(p.get("n", 12), 12.0))
    N = max(3, min(N, 30))
    fn = _compile(expr, "1/n", var="n")
    vals = [(i, _at(fn, float(i))) for i in range(1, N + 1)]
    ys = [v for _, v in vals if v is not None]
    ymin, ymax = _span(ys + [L], pad=0.25)
    cv, fr = _mk("Giới hạn của dãy số",
                 "Các điểm của dãy dồn dần về một đường nằm ngang khi chỉ số tăng.",
                 0, N + 1, ymin, ymax, w=420.0)
    fr.axes(p.get("xlabel", "n"), p.get("ylabel", "u(n)"))
    fr.hdash(L, 0, N + 1, cls="accent-b")
    fr.text(0, L, f"L = {_fmt(L)}", dx=6, dy=-8, anchor="start")
    for i, v in vals:
        if v is not None:
            fr.point(i, v, cls="accent-a", r=3.0)
    _caption(cv, p.get("label", ""))
    return cv.render()


def build_squeeze(p: Params) -> str:
    """Định lí kẹp: đồ thị (hoặc dãy) ở giữa bị hai đường bao cùng tiến về một giới hạn."""
    discrete = bool(p.get("discrete"))
    if discrete:
        lo_e = p.get("lower", "1-1/n")
        mid_e = p.get("middle", "1+sin(n)/n")
        hi_e = p.get("upper", "1+1/n")
        N = int(_pos(p.get("n", 14), 14.0))
        N = max(4, min(N, 30))
        fl, fm, fh = (_compile(lo_e, "1-1/n", "n"), _compile(mid_e, "1+sin(n)/n", "n"),
                      _compile(hi_e, "1+1/n", "n"))
        vals = [(i, _at(fl, float(i)), _at(fm, float(i)), _at(fh, float(i)))
                for i in range(1, N + 1)]
        ys = [v for row in vals for v in row[1:] if v is not None]
        ymin, ymax = _span(ys, pad=0.2)
        cv, fr = _mk("Định lí kẹp", "Dãy ở giữa bị kẹp giữa hai dãy cùng hội tụ về một giới hạn.",
                     0, N + 1, ymin, ymax, w=420.0)
        fr.axes("n", "u(n)")
        # dãy chặn vẽ điểm rỗng, dãy bị kẹp vẽ điểm đặc — nhìn là biết ai kẹp ai
        for idx, cls, hollow in ((1, "accent-c", True), (3, "accent-c", True),
                                 (2, "accent-a", False)):
            pts = [(row[0], row[idx]) for row in vals if row[idx] is not None]
            if hollow and len(pts) >= 2:
                fr.cv.polyline([(fr.sx(x), fr.sy(y)) for x, y in pts], cls="accent-c",
                               extra=' style="fill:none"' + DASH + THIN)
            for x, y in pts:
                fr.point(x, y, cls=cls, r=2.8, hollow=hollow)
    else:
        fl = _compile(p.get("lower", "1-x^2"), "1-x^2")
        fm = _compile(p.get("middle", "1+0.5*x^2*cos(6*x)"), "1+0.5*x^2*cos(6*x)")
        fh = _compile(p.get("upper", "1+x^2"), "1+x^2")
        half = _pos(p.get("half_width", 1.2), 1.2)
        xmin, xmax = -half, half
        ys = [v for fn in (fl, fm, fh) for _, v in _samples(fn, xmin, xmax, 60) if v is not None]
        ymin, ymax = _span(ys, pad=0.18)
        cv, fr = _mk("Định lí kẹp", "Đường ở giữa bị kẹp giữa hai đường cùng tiến về một giới hạn.",
                     xmin, xmax, ymin, ymax)
        fr.axes("x", "y")
        fr.curve(fl, cls="accent-c", extra=CURVE2 + DASH)
        fr.curve(fh, cls="accent-c", extra=CURVE2 + DASH)
        fr.curve(fm)
        L = _f(p.get("L", 1), 1.0)
        fr.point(0, L, cls="accent-b")
        fr.text(xmin, L, f"L = {_fmt(L)}", dx=4, dy=-8, anchor="start")
    _caption(cv, p.get("label", "u ≤ v ≤ w → cùng giới hạn"))
    return cv.render()


def build_ivt(p: Params) -> str:
    """Định lí giá trị trung gian: f liên tục, f(a)·f(b) < 0 nên đồ thị phải cắt trục hoành."""
    expr = p.get("expr", "x^3-x-2")
    a, b = _f(p.get("a", 1), 1.0), _f(p.get("b", 2), 2.0)
    if b <= a:
        a, b = 1.0, 2.0
    fn = _compile(expr, "x^3-x-2")
    pad = (b - a) * 0.28
    xmin, xmax = a - pad, b + pad
    ymin, ymax = _auto_y(fn, xmin, xmax, [0.0])
    cv, fr = _mk("Định lí giá trị trung gian",
                 "Đồ thị liên tục nối một điểm dưới trục hoành với một điểm trên trục hoành nên phải cắt trục.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[a, b] + _roots(fn, a, b)[:1])
    fr.curve(fn)
    for x, name in ((a, "a"), (b, "b")):
        y = _at(fn, x)
        if y is not None:
            fr.point(x, y, cls="accent-b")
            fr.vdash(x, 0, y, cls="ink-thin", extra=DASH_FINE)
            fr.text(x, 0, name, dy=16)
            fr.text(x, y, f"f({name}) = {_fmt(y)}", dx=6, dy=-8, anchor="start")
    for r in _roots(fn, a, b)[:1]:
        fr.point(r, 0.0, cls="accent-d")
        fr.text(r, 0.0, p.get("root_label", "c"), dy=-9)
    _caption(cv, p.get("label", "f(a)·f(b) < 0 ⇒ có nghiệm c ∈ (a; b)"))
    return cv.render()


# ---------------------------------------------------------------------------
# 6. Đạo hàm: tiếp tuyến, cát tuyến, vi phân, đơn điệu
# ---------------------------------------------------------------------------
def build_tangent_line(p: Params) -> str:
    """Tiếp tuyến tại M(x₀; f(x₀)): hệ số góc k = f'(x₀) là ý nghĩa hình học của đạo hàm."""
    expr = p.get("expr", "x^2")
    x0 = _f(p.get("x0", 1), 1.0)
    fn = _compile(expr, "x^2")
    y0 = _at(fn, x0)
    if y0 is None:
        fn, x0, y0 = _compile("x^2", "x^2"), 1.0, 1.0
    k = _f(p.get("k"), _deriv(fn, x0))
    half = _pos(p.get("half_width", 2.0), 2.0)
    xmin, xmax = x0 - half, x0 + half
    ymin, ymax = _auto_y(fn, xmin, xmax, [y0, 0.0])
    cv, fr = _mk("Tiếp tuyến của đồ thị",
                 "Đường thẳng chạm đồ thị tại một điểm; độ dốc của nó là đạo hàm tại điểm đó.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[x0])
    fr.curve(fn)
    fr.line(xmin, y0 + k * (xmin - x0), xmax, y0 + k * (xmax - x0),
            cls="accent-b", extra=' stroke-width="2"')
    if p.get("slope_triangle", True):
        dx = half * 0.45
        fr.line(x0, y0, x0 + dx, y0, cls="accent-d", extra=THIN + DASH_FINE)
        fr.line(x0 + dx, y0, x0 + dx, y0 + k * dx, cls="accent-d", extra=THIN + DASH_FINE)
        fr.text(x0 + dx / 2, y0, "1", dy=14)
        fr.text(x0 + dx, y0 + k * dx / 2, "k", dx=6, anchor="start")
    fr.point(x0, y0, cls="accent-b")
    fr.vdash(x0, 0, y0, cls="ink-thin", extra=DASH_FINE)
    fr.text(x0, 0, p.get("x0_label", "x₀"), dy=16)
    fr.text(x0, y0, p.get("point_label", "M"), dx=-8, dy=-8, anchor="end")
    _caption(cv, p.get("label", "k = f′(x₀)"))
    return cv.render()


def build_secant_tangent(p: Params) -> str:
    """Cát tuyến → tiếp tuyến: tỉ số Δy/Δx là hệ số góc cát tuyến, cho x → x₀ được đạo hàm."""
    expr = p.get("expr", "x^2")
    x0 = _f(p.get("x0", 1), 1.0)
    h = _f(p.get("h", 1.2), 1.2)
    if abs(h) < 1e-6:
        h = 1.2
    fn = _compile(expr, "x^2")
    y0, y1 = _at(fn, x0), _at(fn, x0 + h)
    if y0 is None or y1 is None:
        fn, x0, h = _compile("x^2", "x^2"), 1.0, 1.2
        y0, y1 = 1.0, (x0 + h) ** 2
    xmin, xmax = min(x0, x0 + h) - abs(h) * 0.8, max(x0, x0 + h) + abs(h) * 0.8
    ymin, ymax = _auto_y(fn, xmin, xmax, [y0, y1, 0.0])
    cv, fr = _mk("Cát tuyến và hệ số góc",
                 "Hai điểm trên đồ thị nối bởi cát tuyến; hai cạnh góc vuông là số gia của biến và của hàm.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.curve(fn)
    slope = (y1 - y0) / h
    fr.line(xmin, y0 + slope * (xmin - x0), xmax, y0 + slope * (xmax - x0),
            cls="accent-b", extra=' stroke-width="2"')
    if p.get("tangent", True):
        k = _deriv(fn, x0)
        fr.line(xmin, y0 + k * (xmin - x0), xmax, y0 + k * (xmax - x0),
                cls="accent-c", extra=THIN + DASH)
    fr.line(x0, y0, x0 + h, y0, cls="accent-d", extra=THIN)
    fr.line(x0 + h, y0, x0 + h, y1, cls="accent-d", extra=THIN)
    fr.text((x0 + x0 + h) / 2, y0, p.get("dx_label", "Δx"), dy=15)
    fr.text(x0 + h, (y0 + y1) / 2, p.get("dy_label", "Δy"), dx=7, anchor="start")
    fr.point(x0, y0, cls="accent-b")
    fr.point(x0 + h, y1, cls="accent-b")
    fr.text(x0, y0, p.get("point_label", "M₀"), dx=-8, dy=-6, anchor="end")
    _caption(cv, p.get("label", "Δy/Δx = hệ số góc cát tuyến"))
    return cv.render()


def build_differential(p: Params) -> str:
    """Vi phân dy so với số gia Δy: dy đo trên tiếp tuyến, Δy đo trên đồ thị."""
    expr = p.get("expr", "x^2")
    x0 = _f(p.get("x0", 1), 1.0)
    dx = _f(p.get("dx", 1.0), 1.0)
    if abs(dx) < 1e-6:
        dx = 1.0
    fn = _compile(expr, "x^2")
    y0 = _at(fn, x0)
    y1 = _at(fn, x0 + dx)
    if y0 is None or y1 is None:
        fn, x0, dx = _compile("x^2", "x^2"), 1.0, 1.0
        y0, y1 = 1.0, 4.0
    k = _deriv(fn, x0)
    yt = y0 + k * dx
    xmin, xmax = min(x0, x0 + dx) - abs(dx) * 0.7, max(x0, x0 + dx) + abs(dx) * 0.7
    ymin, ymax = _auto_y(fn, xmin, xmax, [y0, y1, yt, 0.0])
    cv, fr = _mk("Vi phân và số gia",
                 "Trên cùng một số gia của biến: vi phân đo dọc tiếp tuyến, số gia của hàm đo dọc đồ thị.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.curve(fn)
    fr.line(xmin, y0 + k * (xmin - x0), xmax, y0 + k * (xmax - x0),
            cls="accent-c", extra=' stroke-width="2"')
    fr.line(x0, y0, x0 + dx, y0, cls="accent-d", extra=THIN)
    fr.line(x0 + dx, y0, x0 + dx, yt, cls="accent-c", extra=' stroke-width="2.4"')
    fr.line(x0 + dx, y0, x0 + dx, y1, cls="accent-b", extra=THIN + DASH)
    fr.point(x0, y0, cls="accent-b")
    fr.point(x0 + dx, y1, cls="accent-b")
    fr.point(x0 + dx, yt, cls="accent-c")
    fr.text((x0 + x0 + dx) / 2, y0, "dx = Δx", dy=15)
    fr.text(x0 + dx, (y0 + yt) / 2, "dy", dx=7, anchor="start")
    fr.text(x0 + dx, (y0 + y1) / 2, "Δy", dx=-7, anchor="end")
    _caption(cv, p.get("label", "dy = f′(x₀)·dx"))
    return cv.render()


def build_monotone_intervals(p: Params) -> str:
    """Khoảng đồng biến/nghịch biến: dải dấu của f′ đặt ngay dưới đồ thị, kèm cực trị.

    Mũi tên trong dải đi lên/xuống theo dấu f′ để nối được "dấu đạo hàm" với
    "chiều đi của đồ thị" — đó là toàn bộ nội dung của quy tắc xét đơn điệu.
    """
    expr = p.get("expr", "x^3-3*x")
    fn = _compile(expr, "x^3-3*x")
    xmin, xmax = _f(p.get("xmin", -2.4), -2.4), _f(p.get("xmax", 2.4), 2.4)
    if xmax <= xmin:
        xmin, xmax = -2.4, 2.4
    crit = p.get("critical")
    if not isinstance(crit, (list, tuple)):
        crit = _roots(lambda x: _deriv(fn, x), xmin, xmax, n=200)
    crit = sorted({round(_f(c, 0.0), 4) for c in crit if xmin < _f(c, xmin) < xmax})
    ymin, ymax = _auto_y(fn, xmin, xmax, [v for v in (_at(fn, c) for c in crit) if v is not None])
    cv, fr = _mk("Khoảng đồng biến và nghịch biến",
                 "Đồ thị kèm dải dấu của đạo hàm: dấu cộng ứng với đoạn đi lên, dấu trừ ứng với đoạn đi xuống.",
                 xmin, xmax, ymin, ymax, h=336.0, bottom=80.0)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"))
    fr.curve(fn)
    bounds = [xmin] + list(crit) + [xmax]
    strip = fr.by + fr.ph + 46
    cv.text(fr.bx - 8, strip + 4, "f′", cls="lbl", anchor="end")
    for lo, hi in zip(bounds[:-1], bounds[1:]):
        mid = (lo + hi) / 2
        up = _deriv(fn, mid) > 0
        x1, x2 = fr.sx(lo) + 6, fr.sx(hi) - 6
        if x2 - x1 < 6:
            continue
        cv.arrow(x1, strip, x2, strip, cls="accent-c" if up else "accent-b", head=7)
        cv.text((x1 + x2) / 2, strip - 8, "+" if up else "−",
                cls="lbl", anchor="middle")
        cv.text((x1 + x2) / 2, strip + 20,
                "đồng biến" if up else "nghịch biến", cls="lbl-sm", anchor="middle")
    for c in crit:
        y = _at(fn, c)
        if y is None:
            continue
        fr.point(c, y, cls="accent-d")
        cv.line(fr.sx(c), strip - 14, fr.sx(c), strip + 8, cls="ink-thin")
        cv.text(fr.sx(c), strip + 20, _fmt(c), cls="lbl-sm", anchor="middle")
        after = _deriv(fn, c + (xmax - xmin) * 0.02)
        fr.text(c, y, "CĐ" if after < 0 else "CT", dy=-10 if after < 0 else 18)
    _caption(cv, p.get("label", "f′ > 0 ⇒ đồng biến; f′ < 0 ⇒ nghịch biến"))
    return cv.render()


def build_max_min_segment(p: Params) -> str:
    """GTLN–GTNN trên đoạn [a; b]: so giá trị ở hai đầu mút với giá trị tại điểm tới hạn."""
    expr = p.get("expr", "x^3-3*x")
    a, b = _f(p.get("a", -1.5), -1.5), _f(p.get("b", 2.2), 2.2)
    if b <= a:
        a, b = -1.5, 2.2
    fn = _compile(expr, "x^3-3*x")
    crit = [c for c in _roots(lambda x: _deriv(fn, x), a, b, n=200) if a < c < b]
    cand = [(x, _at(fn, x)) for x in [a] + crit + [b]]
    cand = [(x, y) for x, y in cand if y is not None]
    if not cand:
        cand = [(a, 0.0), (b, 0.0)]
    pad = (b - a) * 0.18
    xmin, xmax = a - pad, b + pad
    ymin, ymax = _auto_y(fn, xmin, xmax, [y for _, y in cand] + [0.0])
    cv, fr = _mk("Giá trị lớn nhất – nhỏ nhất trên đoạn",
                 "Đồ thị trên một đoạn, các điểm dự tuyển gồm hai đầu mút và các điểm tới hạn.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[x for x, _ in cand])
    fr.curve(fn, cls="ink-thin")
    fr.curve(fn, lo=a, hi=b)
    hi = max(cand, key=lambda t: t[1])
    lo = min(cand, key=lambda t: t[1])
    for x, y in cand:
        fr.point(x, y, cls="accent-d", r=3.2)
        fr.vdash(x, 0, y, cls="ink-thin", extra=DASH_FINE)
    fr.point(*hi, cls="accent-b")
    fr.point(*lo, cls="accent-c")
    for (x, y), name, off in ((hi, "max", -9), (lo, "min", 17)):
        right = fr.sx(x) > fr.bx + fr.pw * 0.6
        fr.text(x, y, f"{name} = {_fmt(y)}", dx=-7 if right else 7, dy=off,
                anchor="end" if right else "start")
    fr.text(a, 0, "a", dy=16)
    fr.text(b, 0, "b", dy=16)
    _caption(cv, p.get("label", ""))
    return cv.render()


# ---------------------------------------------------------------------------
# 7. Tích phân: diện tích, giá trị trung bình, tổng Riemann
# ---------------------------------------------------------------------------
def _area_polygon(fn, lo: float, hi: float, n: int = 80) -> list[tuple[float, float]]:
    pts = [(x, y) for x, y in _samples(fn, lo, hi, n) if y is not None]
    if len(pts) < 2:
        return []
    return [(lo, 0.0)] + pts + [(hi, 0.0)]


def build_area_under(p: Params) -> str:
    """Diện tích hình phẳng giới hạn bởi y = f(x), trục hoành và hai đường x = a, x = b.

    ``splits`` chia miền thành nhiều mảnh (tính chất chèn cận, hàm chẵn);
    ``signed=True`` tô khác màu phần nằm dưới trục (tích phân mang dấu âm).
    """
    expr = p.get("expr", "0.5*x^2+1")
    a, b = _f(p.get("a", 1), 1.0), _f(p.get("b", 4), 4.0)
    if b <= a:
        a, b = 1.0, 4.0
    fn = _compile(expr, "0.5*x^2+1")
    signed = bool(p.get("signed"))
    splits = [s for s in (p.get("splits") or []) if a < _f(s, a) < b]
    bounds = [a] + sorted(_f(s, a) for s in splits) + [b]
    pad = (b - a) * 0.22
    xmin, xmax = min(a - pad, _f(p.get("xmin", a - pad), a - pad)), \
        max(b + pad, _f(p.get("xmax", b + pad), b + pad))
    ymin, ymax = _auto_y(fn, a, b, [0.0])
    cv, fr = _mk("Diện tích dưới đường cong",
                 "Miền được tô nằm giữa đồ thị và trục hoành, chặn hai bên bởi hai đường thẳng đứng.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=bounds)
    labels = p.get("part_labels") or []
    if not isinstance(labels, (list, tuple)):
        labels = []
    for i, (lo, hi) in enumerate(zip(bounds[:-1], bounds[1:])):
        poly = _area_polygon(fn, lo, hi)
        if not poly:
            continue
        mid = _val(fn, (lo + hi) / 2)
        cls = "fill-b" if (signed and mid < 0) else "fill-a"
        fr.area(poly, cls=cls)
        text = labels[i] if i < len(labels) else ("S" if len(bounds) == 2 else f"S{i + 1}")
        thick = sorted(((abs(y), x, y) for x, y in poly[1:-1]))
        if thick:
            _, lx, ly = thick[int(0.7 * (len(thick) - 1))]
            fr.text(lx, ly / 2, text, cls="lbl")
    for x, name in zip(bounds, ["a"] + [f"c{i}" if len(bounds) > 3 else "c"
                                       for i in range(1, len(bounds) - 1)] + ["b"]):
        y = _at(fn, x)
        if y is not None:
            fr.vdash(x, 0, y, cls="accent-b")
        fr.text(x, 0, name, dy=16)
    fr.curve(fn)
    _caption(cv, p.get("label", "S = ∫f(x)dx"))
    return cv.render()


def build_area_between(p: Params) -> str:
    """Diện tích hình phẳng giữa hai đường y = f(x) và y = g(x) trên [a; b]."""
    f_expr, g_expr = p.get("f", "4-x^2"), p.get("g", "x+2")
    fn, gn = _compile(f_expr, "4-x^2"), _compile(g_expr, "x+2")
    a, b = p.get("a"), p.get("b")
    if a is None or b is None:
        rs = _roots(lambda x: fn(x) - gn(x), -6, 6)
        a, b = (rs[0], rs[-1]) if len(rs) >= 2 else (-1.0, 1.0)
    a, b = _f(a, -2.0), _f(b, 1.0)
    if b <= a:
        a, b = a, a + 1.0
    pad = (b - a) * 0.3
    xmin, xmax = a - pad, b + pad
    lo1, hi1 = _auto_y(fn, xmin, xmax)
    lo2, hi2 = _auto_y(gn, xmin, xmax)
    ymin, ymax = _span([lo1, hi1, lo2, hi2, 0.0], pad=0.06)
    cv, fr = _mk("Diện tích giữa hai đường cong",
                 "Miền được tô kẹp giữa hai đồ thị, chặn hai bên bởi hoành độ giao điểm.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[a, b])
    top = [(x, y) for x, y in _samples(fn, a, b, 80) if y is not None]
    bot = [(x, y) for x, y in _samples(gn, a, b, 80) if y is not None]
    if top and bot:
        fr.area(top + bot[::-1], cls="fill-a")
    fr.curve(fn)
    fr.curve(gn, cls="accent-c", extra=CURVE2)
    for x, name in ((a, "a"), (b, "b")):
        yf, yg = _at(fn, x), _at(gn, x)
        if yf is not None and yg is not None:
            fr.vdash(x, min(yf, yg), max(yf, yg), cls="accent-b")
            fr.point(x, yf, cls="accent-b", r=3.0)
        fr.text(x, 0, name, dy=16)
    mid = (a + b) / 2
    ym, yg = _at(fn, mid), _at(gn, mid)
    if ym is not None and yg is not None:
        fr.text(mid, (ym + yg) / 2, "S", cls="lbl")
    fr.text(mid, _val(fn, mid), p.get("f_label", "y = f(x)"), dy=-11)
    fr.text(xmax, _val(gn, xmax), p.get("g_label", "y = g(x)"), dx=-4, dy=-8, anchor="end")
    _caption(cv, p.get("label", "S = ∫|f(x) − g(x)|dx"))
    return cv.render()


def build_mean_value_integral(p: Params) -> str:
    """Giá trị trung bình của hàm: hình chữ nhật cao f̄ có diện tích bằng miền dưới đường cong."""
    expr = p.get("expr", "0.4*x^2+0.5")
    a, b = _f(p.get("a", 0.5), 0.5), _f(p.get("b", 3.5), 3.5)
    if b <= a:
        a, b = 0.5, 3.5
    fn = _compile(expr, "0.4*x^2+0.5")
    mean = _integral(fn, a, b) / (b - a)
    pad = (b - a) * 0.2
    xmin, xmax = a - pad, b + pad
    ymin, ymax = _auto_y(fn, xmin, xmax, [0.0, mean])
    cv, fr = _mk("Giá trị trung bình của hàm số",
                 "Hình chữ nhật có cùng diện tích với miền dưới đường cong; chiều cao của nó là giá trị trung bình.",
                 xmin, xmax, ymin, ymax)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[a, b])
    poly = _area_polygon(fn, a, b)
    if poly:
        fr.area(poly, cls="fill-a")
    fr.area([(a, 0.0), (a, mean), (b, mean), (b, 0.0)], cls="fill-c")
    fr.hdash(mean, xmin, xmax, cls="accent-c")
    fr.curve(fn)
    fr.text(xmin, mean, p.get("mean_label", "giá trị trung bình"), dx=4, dy=-7, anchor="start")
    for x, name in ((a, "a"), (b, "b")):
        fr.vdash(x, 0, _val(fn, x), cls="accent-b")
        fr.text(x, 0, name, dy=16)
    for c in _roots(lambda x: fn(x) - mean, a, b)[:1]:
        fr.point(c, mean, cls="accent-d")
        fr.text(c, mean, "c", dx=5, dy=-8, anchor="start")
    _caption(cv, p.get("label", ""))
    return cv.render()


def build_riemann_sum(p: Params) -> str:
    """Tổng Riemann: hình chữ nhật trái/phải/giữa hoặc hình thang xấp xỉ diện tích.

    ``mode``: "left" | "right" | "mid" | "trapezoid"; ``partition`` là danh sách
    mốc chia không đều (dùng cho phân hoạch tổng quát và chuẩn phân hoạch ‖P‖).
    ``mark_norm`` đánh dấu đoạn chia dài nhất (định nghĩa ‖P‖); ``ghosts`` vẽ mờ
    mút trái và mút phải của mỗi mảnh để thấy hình thang đúng là trung bình của
    hai tổng chữ nhật — không có nó thì hình chỉ nói được một nửa công thức.
    """
    expr = p.get("expr", "0.4*x^2+1")
    a, b = _f(p.get("a", 0), 0.0), _f(p.get("b", 4), 4.0)
    if b <= a:
        a, b = 0.0, 4.0
    mode = str(p.get("mode", "left"))
    if mode not in ("left", "right", "mid", "trapezoid"):
        mode = "left"
    fn = _compile(expr, "0.4*x^2+1")
    part = p.get("partition")
    if isinstance(part, (list, tuple)) and len(part) >= 2:
        nodes = sorted({round(_f(v, a), 6) for v in part})
        nodes = [v for v in nodes if a - 1e-9 <= v <= b + 1e-9]
        if len(nodes) < 2 or abs(nodes[0] - a) > 1e-9 or abs(nodes[-1] - b) > 1e-9:
            nodes = [a] + [v for v in nodes if a < v < b] + [b]
    else:
        n = int(_pos(p.get("n", 6), 6.0))
        n = max(1, min(n, 40))
        nodes = [a + (b - a) * i / n for i in range(n + 1)]
    pad = (b - a) * 0.12
    xmin, xmax = a - pad, b + pad
    ymin, ymax = _auto_y(fn, xmin, xmax, [0.0])
    cv, fr = _mk("Tổng Riemann",
                 "Miền dưới đường cong được xấp xỉ bằng các hình chữ nhật (hoặc hình thang) trên từng đoạn chia.",
                 xmin, xmax, ymin, ymax,
                 h=316.0 if p.get("mark_norm") else 300.0,
                 bottom=60.0 if p.get("mark_norm") else 44.0)
    fr.axes(p.get("xlabel", "x"), p.get("ylabel", "y"), skip_x=[nodes[0], nodes[-1]])
    marks: list[tuple[float, float]] = []
    for lo, hi in zip(nodes[:-1], nodes[1:]):
        if hi <= lo:
            continue
        if mode == "trapezoid":
            ylo, yhi = _at(fn, lo), _at(fn, hi)
            if ylo is None or yhi is None:
                continue
            fr.area([(lo, 0.0), (lo, ylo), (hi, yhi), (hi, 0.0)], cls="fill-a")
            if p.get("ghosts"):
                fr.line(lo, ylo, hi, ylo, cls="accent-c", extra=THIN + DASH_FINE)
                fr.line(lo, yhi, hi, yhi, cls="accent-b", extra=THIN + DASH_FINE)
            fr.line(lo, ylo, hi, yhi, cls="accent-a", extra=THIN)
            fr.line(lo, 0.0, lo, ylo, cls="accent-a", extra=THIN)
            fr.line(hi, 0.0, hi, yhi, cls="accent-a", extra=THIN)
        else:
            xs = {"left": lo, "right": hi, "mid": (lo + hi) / 2}[mode]
            ys = _at(fn, xs)
            if ys is None:
                continue
            fr.area([(lo, 0.0), (lo, ys), (hi, ys), (hi, 0.0)], cls="fill-a")
            fr.line(lo, 0.0, lo, ys, cls="accent-a", extra=THIN)
            fr.line(hi, 0.0, hi, ys, cls="accent-a", extra=THIN)
            fr.line(lo, ys, hi, ys, cls="accent-a", extra=THIN)
            marks.append((xs, ys))
    fr.curve(fn)
    if p.get("show_samples", True):
        for x, y in marks:
            fr.point(x, y, cls="accent-b", r=2.8)
    if p.get("mark_norm"):
        # ‖P‖ là đoạn chia DÀI NHẤT: không chỉ ra đoạn nào thì nhãn ‖P‖ nói suông
        widths = [(hi - lo, lo, hi) for lo, hi in zip(nodes[:-1], nodes[1:])]
        _, lo, hi = max(widths)
        y = fr.by + fr.ph + 26
        cv.arrow(fr.sx(hi) - 1, y, fr.sx(lo), y, cls="accent-d", head=7)
        cv.arrow(fr.sx(lo) + 1, y, fr.sx(hi), y, cls="accent-d", head=7)
        cv.text((fr.sx(lo) + fr.sx(hi)) / 2, y - 6, "‖P‖", cls="lbl-sm", anchor="middle")
    for x, name in ((nodes[0], "a"), (nodes[-1], "b")):
        fr.text(x, 0, name, dy=16)
    names = {"left": "mút trái", "right": "mút phải", "mid": "trung điểm",
             "trapezoid": "hình thang"}
    _caption(cv, p.get("label", f"xấp xỉ bằng {names[mode]}"))
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "cubic": build_cubic,
    "quartic": build_quartic,
    "parabola": build_parabola,
    "rational": build_rational,
    "oblique_asymptote": build_oblique_asymptote,
    "limit_infinity": build_limit_infinity,
    "exp_log_pair": build_exp_log_pair,
    "base_family": build_base_family,
    "exp_growth": build_exp_growth,
    "half_life": build_half_life,
    "logistic": build_logistic,
    "horizontal_cut": build_horizontal_cut,
    "graph_intersection": build_graph_intersection,
    "parity": build_parity,
    "piecewise": build_piecewise,
    "one_sided_limit": build_one_sided_limit,
    "limit_hole": build_limit_hole,
    "sequence_limit": build_sequence_limit,
    "squeeze": build_squeeze,
    "ivt": build_ivt,
    "tangent_line": build_tangent_line,
    "secant_tangent": build_secant_tangent,
    "differential": build_differential,
    "monotone_intervals": build_monotone_intervals,
    "max_min_segment": build_max_min_segment,
    "area_under": build_area_under,
    "area_between": build_area_between,
    "mean_value_integral": build_mean_value_integral,
    "riemann_sum": build_riemann_sum,
}
