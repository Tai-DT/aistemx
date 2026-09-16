"""Minh hoạ thống kê và xác suất (họ ``thongke``).

Hình của họ này gần như luôn là hình *có số liệu*. Khác với một tam giác vuông —
nhìn là biết đúng sai — một biểu đồ hộp vẽ sai vị trí Q₁ hay một đường hồi quy
vẽ lệch thì người học không có cách nào phát hiện. Vì vậy nguyên tắc xuyên suốt
tệp này: **mọi đại lượng in ra hình đều được tính lại từ chính dữ liệu đang vẽ**
(trung bình, tứ phân vị, hàng rào ngoại lệ, hệ số hồi quy, hệ số tương quan,
diện tích dưới đường cong chuẩn), không có con số nào viết tay.

Về tích phân của đường cong chuẩn: không tự viết công thức xấp xỉ bảng
(Abramowitz–Stegun 26.2.17 có sai số cỡ 7,5·10⁻⁸) vì thư viện chuẩn đã có
``math.erf`` — sai số cỡ 10⁻¹⁵. Dùng Φ(z) = ½·(1 + erf(z/√2)); nhờ vậy các con
số 68,3% / 95,4% / 99,7% trên hình là giá trị thật, không phải số nhớ.

Toàn bộ hình deterministic: dữ liệu "ngẫu nhiên" của biểu đồ tán xạ lấy từ một
bảng nhiễu cố định trong tệp này, không gọi ``random``.
"""

from __future__ import annotations

import math
from typing import Callable, Iterable, Sequence

from .svgkit import Canvas, _n

Params = dict


# --------------------------------------------------------------------------
# Hạ tầng dùng chung
# --------------------------------------------------------------------------
def _vn(v: float, nd: int = 2) -> str:
    """Số theo lối viết Việt Nam (dấu phẩy thập phân), bỏ đuôi 0 thừa.

    Gom "-0" về "0": số âm rất nhỏ sau khi làm tròn mà vẫn giữ dấu trừ trông
    như một lỗi tính toán trên hình.
    """
    if abs(v) < 0.5 * 10 ** (-nd):
        v = 0.0
    s = f"{v:.{nd}f}"
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    # dấu trừ toán học U+2212 thay hyphen: hyphen ở cỡ chữ nhỏ dễ đọc nhầm thành gạch nối
    return (s or "0").replace(".", ",").replace("-", "−")


def _pdf(z: float) -> float:
    """Mật độ chuẩn tắc φ(z)."""
    return math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)


def _cdf(z: float) -> float:
    """Φ(z) qua ``math.erf`` — xem chú thích đầu tệp về sai số."""
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def _nice_step(span: float, target: int = 5) -> float:
    """Bước chia trục "đẹp" (1/2/2,5/5 × 10ⁿ) để nhãn trục không ra số lẻ."""
    if not math.isfinite(span) or span <= 0:
        return 1.0
    raw = span / max(target, 1)
    mag = 10.0 ** math.floor(math.log10(raw))
    for m in (1.0, 2.0, 2.5, 5.0):
        if raw <= m * mag:
            return m * mag
    return 10.0 * mag


def _fnum(v, default: float) -> float:
    """Ép tham số về float; tham số hỏng thì lùi về mặc định thay vì nổ.

    Generator phải gọi được với params bất kỳ (kể cả rỗng) nên mọi lối vào đều
    đi qua đây.
    """
    try:
        x = float(v)
    except (TypeError, ValueError):
        return float(default)
    return x if math.isfinite(x) else float(default)


def _inum(v, default: int, lo: int, hi: int) -> int:
    """Ép tham số về int rồi kẹp vào [lo, hi] — chặn n = 10⁹ làm treo vòng lặp."""
    try:
        x = int(v)
    except (TypeError, ValueError):
        return default
    return max(lo, min(hi, x))


def _floats(seq, default: Sequence[float]) -> list[float]:
    """Danh sách số hữu hạn; rỗng hoặc hỏng thì lùi về mặc định."""
    if not isinstance(seq, (list, tuple)):
        return [float(v) for v in default]
    out = []
    for v in seq:
        try:
            x = float(v)
        except (TypeError, ValueError):
            continue
        if math.isfinite(x):
            out.append(x)
    return out or [float(v) for v in default]


class _Frame:
    """Khung có trục: đổi toạ độ dữ liệu sang toạ độ SVG.

    Không dùng ``_Plot`` của ``generators2d`` vì nó kẻ lưới theo từng số nguyên —
    với thang thống kê (tần số 0..40, điểm 0..100) thì lưới ấy dày đặc vô nghĩa.
    """

    def __init__(self, cv: Canvas, box, xmin, xmax, ymin, ymax):
        self.cv = cv
        self.x0, self.y0, self.w, self.h = box
        if xmax - xmin < 1e-9:
            xmin, xmax = xmin - 1.0, xmax + 1.0
        if ymax - ymin < 1e-9:
            ymin, ymax = ymin - 1.0, ymax + 1.0
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def sx(self, x: float) -> float:
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def sy(self, y: float) -> float:
        return self.y0 + (self.ymax - y) / (self.ymax - self.ymin) * self.h

    @property
    def bottom(self) -> float:
        return self.y0 + self.h

    def frame_x(self, label: str = "", ticks: Iterable[float] = (), fmt=None, nd=None,
                stagger: bool = False) -> int:
        """Trục hoành nằm đáy khung, kèm vạch chia và nhãn. Trả số DÒNG nhãn đã dùng.

        ``stagger``: khi hai nhãn kề nhau sẽ chồng lên nhau thì đẩy nhãn sau
        xuống dòng dưới. Cần cho đường cong chuẩn, nơi các mốc được tô (μ ± zσ)
        có thể nằm sát nhau tuỳ z — mà bỏ mốc đi thì mất đúng thứ hình muốn chỉ.
        Truyền ``ticks`` theo thứ tự ƯU TIÊN (mốc quan trọng trước): nhãn nào hết
        chỗ ở cả hai dòng mới bị bỏ, và μ nên đứng cuối vì đã có nét đứt chỉ chỗ.
        """
        cv = self.cv
        yb = self.bottom
        ticks = list(ticks)
        if nd is None:
            nd = _auto_nd(ticks)
        cv.line(self.x0 - 6, yb, self.x0 + self.w + 10, yb, cls="axis")
        taken: list[list[tuple[float, float]]] = [[], []]
        rows_used = 1
        for t in ticks:
            sx = self.sx(t)
            cv.line(sx, yb, sx, yb + 5, cls="axis")
            txt = fmt(t) if fmt else _vn(t, nd)
            row = 0
            if stagger:
                # ước lượng bề rộng nhãn theo số ký tự (lbl-sm là 12px sans-serif,
                # ~6,6px/ký tự) — chỉ cần đủ chặt để phát hiện chồng lấn
                half = 3.3 * len(txt) + 5.0
                while row < 2 and any(sx - half < r and l < sx + half for l, r in taken[row]):
                    row += 1
                if row >= 2:
                    continue      # hết chỗ: bỏ nhãn còn hơn in đè lên nhãn khác
                taken[row].append((sx - half, sx + half))
                rows_used = max(rows_used, row + 1)
            cv.text(sx, yb + 19 + row * 15, txt, cls="lbl-sm", anchor="middle")
        if label:
            # xuống hẳn dưới dòng nhãn cuối: ngang hàng vạch chia thì nhãn trục đè lên nó
            cv.text(self.x0 + self.w + 10, self.label_bottom(rows_used) + 17,
                    label, cls="lbl", anchor="end")
        return rows_used

    def label_bottom(self, rows_used: int = 1) -> float:
        """Đường cơ sở của dòng nhãn trục hoành cuối cùng — mốc để xếp chú thích dưới."""
        return self.bottom + 19 + 15 * (rows_used - 1)

    def frame_y(self, label: str = "", ticks: Iterable[float] = (), nd=None, grid=True):
        """Trục tung kèm lưới ngang mờ — lưới giúp so chiều cao cột, nên giữ."""
        cv = self.cv
        ticks = list(ticks)
        if nd is None:
            nd = _auto_nd(ticks)
        cv.line(self.x0, self.bottom + 6, self.x0, self.y0 - 10, cls="axis")
        for t in ticks:
            sy = self.sy(t)
            if grid and t > self.ymin:
                cv.line(self.x0, sy, self.x0 + self.w, sy, cls="grid")
            cv.line(self.x0 - 5, sy, self.x0, sy, cls="axis")
            cv.text(self.x0 - 9, sy + 4, _vn(t, nd), cls="lbl-sm", anchor="end")
        if label:
            cv.text(max(6.0, self.x0 - 36), self.y0 - 16, label, cls="lbl-sm")

    def ticks_x(self, target: int = 6) -> list[float]:
        return _ticks(self.xmin, self.xmax, target)

    def ticks_y(self, target: int = 5) -> list[float]:
        return _ticks(self.ymin, self.ymax, target)


def _auto_nd(ticks: Sequence[float]) -> int:
    """Số chữ số thập phân nhỏ nhất mà mọi vạch chia vẫn in ra đúng giá trị.

    Ép cứng nd = 0 từng làm vạch 12,5 hiện thành "12" — nhãn trục sai như vậy
    còn nguy hơn không có nhãn.
    """
    for nd in range(5):
        if all(abs(t - round(t, nd)) < 1e-9 for t in ticks):
            return nd
    return 4


def _ticks(lo: float, hi: float, target: int) -> list[float]:
    step = _nice_step(hi - lo, target)
    start = math.ceil(lo / step) * step
    out: list[float] = []
    t = start
    # chặn cứng 40 vạch: tham số biên (span khổng lồ) không được biến thành vòng lặp dài
    while t <= hi + 1e-9 and len(out) < 40:
        out.append(0.0 if abs(t) < 1e-12 else t)
        t += step
    return out


def _dash(width: float = 1.6) -> str:
    return f' stroke-dasharray="5 4" stroke-width="{_n(width)}"'


def _pts(pairs: Iterable[Sequence[float]]) -> str:
    """Chuỗi ``d`` của path: luôn viết toạ độ dạng ``x,y`` để test soi được."""
    return " ".join(f"{_n(x)},{_n(y)}" for x, y in pairs)


def _circle_path(cx: float, cy: float, r: float) -> str:
    """Đường tròn dưới dạng path (để ghép fill-rule evenodd khoét lỗ)."""
    return (
        f"M {_n(cx - r)},{_n(cy)} A {_n(r)} {_n(r)} 0 1 1 {_n(cx + r)},{_n(cy)} "
        f"A {_n(r)} {_n(r)} 0 1 1 {_n(cx - r)},{_n(cy)} Z"
    )


# --------------------------------------------------------------------------
# 1. Biểu đồ cột tần số (số liệu rời rạc)
# --------------------------------------------------------------------------
def build_bar_chart(p: Params) -> str:
    """Biểu đồ cột tần số. Tuỳ chọn: kẻ đường trung bình, tô cột mốt.

    Trung bình được tính từ chính ``values``/``freqs`` đang vẽ, nên vị trí đường
    đứt luôn khớp với con số ghi bên cạnh.
    """
    values = _floats(p.get("values"), [1, 2, 3, 4, 5, 6])
    freqs = _floats(p.get("freqs"), [3, 7, 12, 9, 5, 2])
    k = min(len(values), len(freqs))
    values, freqs = values[:k], [max(0.0, v) for v in freqs[:k]]
    show_mean = bool(p.get("show_mean", False))
    show_mode = bool(p.get("show_mode", False))
    show_percent = bool(p.get("show_percent", False))
    xlabel = str(p.get("xlabel", "x"))
    ylabel = str(p.get("ylabel", "tần số n"))

    total = sum(freqs) or 1.0
    mean = sum(v * f for v, f in zip(values, freqs)) / total
    # cùng khung này còn dùng cho BẢNG PHÂN PHỐI XÁC SUẤT (cột là pᵢ chứ không phải
    # tần số): ép 0 chữ số thập phân thì 0,3 in ra thành "0" — nhãn sai hẳn giá trị.
    nd_f = 0 if all(abs(f - round(f)) < 1e-9 for f in freqs) else 2
    gaps = [b - a for a, b in zip(values, values[1:])]
    gap = min((g for g in gaps if g > 0), default=1.0)
    half = 0.31 * gap

    w, h = 470.0, 320.0
    box = (62.0, 46.0, 372.0, 210.0)
    lo, hi = min(values) - gap * 0.8, max(values) + gap * 0.8
    top = max(freqs) * 1.2 or 1.0
    cv = Canvas(w, h, title="Biểu đồ cột tần số",
                desc="Biểu đồ cột biểu diễn tần số của mẫu số liệu.")
    fr = _Frame(cv, box, lo, hi, 0.0, top)
    fr.frame_y(ylabel, fr.ticks_y(5))

    mode_i = max(range(k), key=lambda i: freqs[i]) if k else -1
    # nhãn tần số gom lại vẽ SAU đường trung bình: SVG vẽ sau thì đè lên trên, mà
    # đường x̄ hay rơi trúng đỉnh cột cao nhất và gạch ngang qua con số ở đó.
    tops: list[tuple[float, float, str]] = []
    for i, (v, f) in enumerate(zip(values, freqs)):
        x1, x2 = fr.sx(v - half), fr.sx(v + half)
        ytop, ybot = fr.sy(f), fr.sy(0)
        hot = show_mode and i == mode_i
        cv.rect(x1, ytop, x2 - x1, ybot - ytop, cls="fill-b" if hot else "fill-a")
        cv.rect(x1, ytop, x2 - x1, ybot - ytop, cls="ink-thin")
        lbl = _vn(f, nd_f)
        if show_percent:
            lbl += f" ({_vn(100 * f / total, 1)}%)"
        tops.append(((x1 + x2) / 2, ytop - 6, lbl))

    fr.frame_x(xlabel, values, fmt=lambda t: _vn(t, 0))
    if show_mode and mode_i >= 0:
        cv.text(fr.sx(values[mode_i]), box[1] - 28,
                f"Mₒ = {_vn(values[mode_i], 0)}", cls="lbl", anchor="middle")
    if show_mean:
        mx = fr.sx(mean)
        cv.line(mx, fr.bottom, mx, box[1] - 6, cls="accent-c", extra=_dash(2.0))
        cv.text(mx + 6, box[1] - 10, f"x̄ = {_vn(mean, 2)}", cls="lbl")
    for tx, ty, lbl in tops:
        cv.text(tx, ty, lbl, cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 2. Biểu đồ tần số ghép nhóm (histogram)
# --------------------------------------------------------------------------
def build_histogram(p: Params) -> str:
    """Biểu đồ tần số ghép nhóm: cột liền nhau trên các nửa khoảng [uᵢ; uᵢ₊₁)."""
    bounds = _floats(p.get("bounds"), [0, 10, 20, 30, 40, 50])
    freqs = _floats(p.get("freqs"), [4, 9, 15, 10, 6])
    if len(bounds) < 2:
        bounds = [0.0, 1.0]
    bounds = sorted(bounds)
    k = min(len(bounds) - 1, len(freqs))
    bounds, freqs = bounds[: k + 1], [max(0.0, v) for v in freqs[:k]]
    show_mean = bool(p.get("show_mean", False))
    highlight = p.get("highlight")
    xlabel = str(p.get("xlabel", "giá trị"))

    mids = [(bounds[i] + bounds[i + 1]) / 2 for i in range(k)]
    total = sum(freqs) or 1.0
    mean = sum(c * f for c, f in zip(mids, freqs)) / total
    nd_f = 0 if all(abs(f - round(f)) < 1e-9 for f in freqs) else 2  # xem build_bar_chart

    w, h = 480.0, 320.0
    box = (62.0, 52.0, 384.0, 202.0)
    span = bounds[-1] - bounds[0]
    lo, hi = bounds[0] - 0.06 * span, bounds[-1] + 0.06 * span
    top = (max(freqs) if freqs else 1.0) * 1.24 or 1.0
    cv = Canvas(w, h, title="Biểu đồ tần số ghép nhóm",
                desc="Biểu đồ cột liền biểu diễn tần số của mẫu số liệu ghép nhóm.")
    fr = _Frame(cv, box, lo, hi, 0.0, top)
    fr.frame_y("tần số n", fr.ticks_y(5))

    hi_idx = _inum(highlight, -1, -1, k - 1) if highlight is not None else -1
    tops: list[tuple[float, float, str]] = []      # xem chú thích cùng chỗ ở build_bar_chart
    for i in range(k):
        x1, x2 = fr.sx(bounds[i]), fr.sx(bounds[i + 1])
        ytop, ybot = fr.sy(freqs[i]), fr.sy(0)
        cv.rect(x1, ytop, x2 - x1, ybot - ytop,
                cls="fill-b" if i == hi_idx else "fill-a")
        cv.rect(x1, ytop, x2 - x1, ybot - ytop, cls="ink-thin")
        tops.append(((x1 + x2) / 2, ytop - 6, _vn(freqs[i], nd_f)))
    fr.frame_x(xlabel, bounds)

    if hi_idx >= 0:
        cv.text(fr.sx(mids[hi_idx]), box[1] - 30,
                str(p.get("highlight_label", "nhóm chứa mốt")), cls="lbl-sm", anchor="middle")
    if show_mean:
        mx = fr.sx(mean)
        cv.line(mx, fr.bottom, mx, box[1] - 4, cls="accent-c", extra=_dash(2.0))
        cv.text(mx + 6, box[1] - 8, f"x̄ ≈ {_vn(mean, 2)}", cls="lbl")
    for tx, ty, lbl in tops:
        cv.text(tx, ty, lbl, cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 3. Đường tần số tích luỹ
# --------------------------------------------------------------------------
def build_cumulative_curve(p: Params) -> str:
    """Đường tần số tích luỹ, kèm cách "đọc ngược" trung vị / tứ phân vị.

    Vạch đọc ngược chính là phép nội suy tuyến tính mà công thức trung vị ghép
    nhóm trong SGK đang làm, nên vị trí trên hình và giá trị in ra luôn khớp.
    """
    bounds = _floats(p.get("bounds"), [0, 10, 20, 30, 40, 50])
    freqs = _floats(p.get("freqs"), [4, 9, 15, 10, 6])
    fractions = _floats(p.get("fractions"), [0.5])
    labels = p.get("fraction_labels")
    if len(bounds) < 2:
        bounds = [0.0, 1.0]
    bounds = sorted(bounds)
    k = min(len(bounds) - 1, len(freqs))
    bounds, freqs = bounds[: k + 1], [max(0.0, v) for v in freqs[:k]]

    cum = [0.0]
    for f in freqs:
        cum.append(cum[-1] + f)
    total = cum[-1] or 1.0

    def read_x(target: float) -> float:
        """Nội suy tuyến tính trên đường tích luỹ: y = target → x."""
        for i in range(k):
            if cum[i + 1] >= target:
                lo_c, hi_c = cum[i], cum[i + 1]
                if hi_c - lo_c < 1e-12:
                    return bounds[i]
                t = (target - lo_c) / (hi_c - lo_c)
                return bounds[i] + t * (bounds[i + 1] - bounds[i])
        return bounds[-1]

    w, h = 480.0, 330.0
    box = (66.0, 34.0, 372.0, 220.0)
    span = bounds[-1] - bounds[0]
    cv = Canvas(w, h, title="Đường tần số tích luỹ",
                desc="Đường tần số tích luỹ và cách đọc trung vị, tứ phân vị từ đồ thị.")
    fr = _Frame(cv, box, bounds[0] - 0.04 * span, bounds[-1] + 0.06 * span,
                0.0, total * 1.12)
    fr.frame_y("tần số tích luỹ", fr.ticks_y(5))
    fr.frame_x(str(p.get("xlabel", "giá trị")), bounds)

    curve = [(fr.sx(bounds[i]), fr.sy(cum[i])) for i in range(k + 1)]
    cv.polyline(curve, cls="curve")
    for sxy in curve:
        cv.dot(sxy[0], sxy[1], r=3.0, cls="accent-a")

    names = labels if isinstance(labels, list) and len(labels) == len(fractions) else None
    for j, q in enumerate(fractions):
        q = min(max(q, 0.0), 1.0)
        yv = q * total
        xv = read_x(yv)
        sx, sy = fr.sx(xv), fr.sy(yv)
        cv.line(fr.x0, sy, sx, sy, cls="accent-b", extra=_dash(1.5))
        cv.line(sx, sy, sx, fr.bottom, cls="accent-b", extra=_dash(1.5))
        cv.dot(sx, sy, r=3.4, cls="accent-b")
        name = names[j] if names else f"Q({_vn(q, 2)})"
        cv.text(sx - 8, sy - 8, f"{name} ≈ {_vn(xv, 1)}", cls="lbl-sm", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# 4. Biểu đồ hình quạt tròn
# --------------------------------------------------------------------------
def build_pie_chart(p: Params) -> str:
    """Biểu đồ hình quạt: mỗi nhóm một hình quạt, ghi rõ góc ở tâm αᵢ.

    Góc vẽ ra đúng bằng góc ghi trong chú giải (nᵢ/N · 360°) — đây chính là nội
    dung công thức nên không được phép làm tròn cho "đẹp" rồi vẽ khác.
    """
    freqs = [max(0.0, v) for v in _floats(p.get("freqs"), [12, 8, 6, 4])][:8]
    raw_labels = p.get("labels")
    labels = [str(s) for s in raw_labels] if isinstance(raw_labels, list) else []
    while len(labels) < len(freqs):
        labels.append(f"nhóm {len(labels) + 1}")
    labels = labels[: len(freqs)]
    total = sum(freqs)
    if total <= 0:
        freqs, total = [1.0] * len(freqs), float(len(freqs))

    w = 470.0
    h = max(300.0, 66.0 + len(freqs) * 24.0 + 40.0)
    cx, cy, r = 140.0, h / 2 + 6.0, 100.0
    cv = Canvas(w, h, title="Biểu đồ hình quạt tròn",
                desc="Biểu đồ hình quạt tròn với góc ở tâm của từng nhóm.")
    cv.text(20, 28, str(p.get("caption", "Góc ở tâm: αᵢ = nᵢ/N · 360°")), cls="lbl-sm")

    # bảng màu chung chỉ có 3 lớp fill; xoay thêm một vòng độ đục đậm hơn để 6 nhóm
    # đầu tiên vẫn phân biệt được bằng mắt mà không phải hard-code màu
    # phải là style nội tuyến, không phải fill-opacity: lớp .fill-* đã đặt opacity:.2 nên
    # thuộc tính trình bày chỉ nhân xuống (nhạt đi), còn style nội tuyến mới ghi đè được
    styles = [("fill-a", ""), ("fill-b", ""), ("fill-c", ""),
              ("fill-a", ' style="opacity:.48"'), ("fill-b", ' style="opacity:.48"'),
              ("fill-c", ' style="opacity:.48"'), ("fill-a", ' style="opacity:.72"'),
              ("fill-b", ' style="opacity:.72"')]
    ang = -90.0  # bắt đầu từ đỉnh, cùng quy ước với sách giáo khoa
    ly = 66.0
    for i, (f, name) in enumerate(zip(freqs, labels)):
        deg = f / total * 360.0
        a1, a2 = math.radians(ang), math.radians(ang + deg)
        p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
        p2 = (cx + r * math.cos(a2), cy + r * math.sin(a2))
        large = 1 if deg > 180 else 0
        d = (f"M {_n(cx)},{_n(cy)} L {_n(p1[0])},{_n(p1[1])} "
             f"A {_n(r)} {_n(r)} 0 {large} 1 {_n(p2[0])},{_n(p2[1])} Z")
        fill_cls, fill_extra = styles[i % len(styles)]
        cv.path(d, cls=fill_cls, extra=fill_extra)
        cv.path(d, cls="ink-thin")
        ang += deg
        # chú giải bên phải: ô màu + tần số + góc ở tâm
        cv.rect(300, ly - 10, 13, 13, cls=fill_cls, extra=fill_extra)
        cv.rect(300, ly - 10, 13, 13, cls="ink-thin")
        cv.text(320, ly, f"{name}: n = {_vn(f, 0)}, α = {_vn(deg, 1)}°", cls="lbl-sm")
        ly += 24
    cv.circle(cx, cy, r, cls="ink")
    cv.text(cx, cy + r + 26, f"N = {_vn(total, 0)}", cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 5. Biểu đồ hộp
# --------------------------------------------------------------------------
def _five_number(data: list[float]):
    """Năm số tóm tắt theo quy ước SGK: Q₂ là trung vị, Q₁/Q₃ là trung vị hai nửa.

    Khi n lẻ thì hai nửa KHÔNG chứa Q₂ — chi tiết này quyết định vị trí cạnh hộp
    nên phải làm đúng, không mượn quy ước khác.
    """
    xs = sorted(data)
    n = len(xs)

    def med(a: list[float]) -> float:
        m = len(a)
        if m == 0:
            return 0.0
        return a[m // 2] if m % 2 else 0.5 * (a[m // 2 - 1] + a[m // 2])

    q2 = med(xs)
    half = n // 2
    lower = xs[:half]
    upper = xs[half + 1:] if n % 2 else xs[half:]
    q1, q3 = med(lower) if lower else q2, med(upper) if upper else q2
    iqr = q3 - q1
    lo_fence, hi_fence = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    inliers = [x for x in xs if lo_fence <= x <= hi_fence] or xs
    return xs, q1, q2, q3, iqr, lo_fence, hi_fence, min(inliers), max(inliers), \
        [x for x in xs if x < lo_fence or x > hi_fence]


def build_box_plot(p: Params) -> str:
    """Biểu đồ hộp: hộp Q₁–Q₃, râu tới giá trị trong hàng rào, chấm ngoại lai.

    Dữ liệu mặc định cố tình có một giá trị vượt Q₃ + 1,5·ΔQ để hình luôn cho
    thấy ngoại lai trông thế nào — đó là phần người học hay bỏ sót nhất.
    """
    data = _floats(p.get("data"), [12, 15, 16, 18, 19, 20, 21, 22, 24, 25, 27, 44])
    show_fence = bool(p.get("show_fence", True))
    show_iqr = bool(p.get("show_iqr", True))
    show_points = bool(p.get("show_points", False))
    xs, q1, q2, q3, iqr, flo, fhi, wlo, whi, outs = _five_number(data)

    w, h = 480.0, 288.0
    box = (52.0, 48.0, 396.0, 156.0)
    lo_v, hi_v = min(xs + [flo]), max(xs + [fhi])
    pad = 0.09 * (hi_v - lo_v or 1.0)
    cv = Canvas(w, h, title="Biểu đồ hộp",
                desc="Biểu đồ hộp với tứ phân vị, râu và giá trị ngoại lệ.")
    fr = _Frame(cv, box, lo_v - pad, hi_v + pad, 0.0, 1.0)
    fr.frame_x(str(p.get("xlabel", "giá trị")), fr.ticks_x(6))

    ymid = box[1] + 62.0
    hbox = 28.0
    x1, x2, x3 = fr.sx(q1), fr.sx(q2), fr.sx(q3)
    xw1, xw2 = fr.sx(wlo), fr.sx(whi)
    # râu
    cv.line(xw1, ymid, x1, ymid, cls="ink")
    cv.line(x3, ymid, xw2, ymid, cls="ink")
    cv.line(xw1, ymid - 10, xw1, ymid + 10, cls="ink")
    cv.line(xw2, ymid - 10, xw2, ymid + 10, cls="ink")
    # hộp
    cv.rect(x1, ymid - hbox, x3 - x1, 2 * hbox, cls="fill-a")
    cv.rect(x1, ymid - hbox, x3 - x1, 2 * hbox, cls="ink")
    cv.line(x2, ymid - hbox, x2, ymid + hbox, cls="accent-b", extra=' stroke-width="2.6"')

    for lbl, xv, sx in (("Q₁", q1, x1), ("Q₂", q2, x2), ("Q₃", q3, x3)):
        cv.text(sx, ymid - hbox - 20, lbl, cls="lbl", anchor="middle")
        cv.text(sx, ymid - hbox - 7, _vn(xv, 1), cls="lbl-sm", anchor="middle")
    cv.text(xw1, ymid + hbox + 17, _vn(wlo, 1), cls="lbl-sm", anchor="middle")
    cv.text(xw2, ymid + hbox + 17, _vn(whi, 1), cls="lbl-sm", anchor="middle")

    if show_iqr:
        cv.line(x1, ymid + hbox + 32, x3, ymid + hbox + 32, cls="accent-c",
                extra=' stroke-width="2"')
        cv.text((x1 + x3) / 2, ymid + hbox + 47, f"ΔQ = {_vn(iqr, 1)}",
                cls="lbl-sm", anchor="middle")
    if show_fence:
        for xv in (flo, fhi):
            sx = fr.sx(xv)
            cv.line(sx, ymid - hbox - 4, sx, ymid + hbox + 4, cls="accent-d", extra=_dash(1.5))
        cv.text(fr.sx(fhi), box[1] - 22, "Q₃ + 1,5·ΔQ", cls="lbl-sm", anchor="middle")
        cv.text(fr.sx(flo), box[1] - 22, "Q₁ − 1,5·ΔQ", cls="lbl-sm", anchor="middle")
    if show_points:
        # đặt trong nửa dưới của hộp: đây là vùng trống duy nhất không đụng nhãn
        for xv in xs:
            cv.dot(fr.sx(xv), ymid + 16, r=2.6, cls="accent-c")
    for xv in outs:
        cv.dot(fr.sx(xv), ymid, r=4.2, cls="accent-b")
        cv.text(fr.sx(xv), ymid - hbox - 7, "ngoại lệ", cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 6. Dải điểm dữ liệu + mốc thống kê
# --------------------------------------------------------------------------
def build_data_dots(p: Params) -> str:
    """Dải chấm dữ liệu trên trục số, kèm một mốc thống kê.

    ``mark``: ``mean`` (trung bình), ``median`` (trung vị), ``range`` (khoảng
    biến thiên), ``deviation`` (các độ lệch xᵢ − x̄ — nền của phương sai).
    """
    data = _floats(p.get("data"), [4, 5, 5, 6, 7, 7, 7, 8, 9, 11])[:24]
    mark = str(p.get("mark", "mean"))
    xs = sorted(data)
    n = len(xs)
    mean = sum(xs) / n
    median = xs[n // 2] if n % 2 else 0.5 * (xs[n // 2 - 1] + xs[n // 2])

    # Ở chế độ độ lệch, MỖI giá trị chiếm một dòng riêng. Xếp chồng như các chế độ
    # khác thì mọi giá trị khác nhau cùng nằm ở dòng đáy, và các đoạn lệch nối
    # đuôi nhau thành MỘT vạch dài từ min tới max — nhìn không ra đoạn nào là
    # độ lệch nào, tức là hình nói sai chính điều chú thích của nó hứa.
    rows = mark == "deviation"
    plot_h = max(126.0, 22.0 + n * 13.0) if rows else 126.0
    w = 480.0
    h = 54.0 + plot_h + 68.0
    box = (48.0, 54.0, 402.0, plot_h)
    lo_v, hi_v = min(xs), max(xs)
    pad = 0.12 * (hi_v - lo_v or 1.0)
    cv = Canvas(w, h, title="Dải số liệu và mốc thống kê",
                desc="Các giá trị của mẫu trên trục số cùng một số đặc trưng của mẫu.")
    fr = _Frame(cv, box, lo_v - pad, hi_v + pad, 0.0, 1.0)
    fr.frame_x(str(p.get("xlabel", "giá trị")), fr.ticks_x(6))

    top = box[1] + 6.0
    if not rows:
        base = fr.bottom - 16.0
        seen: dict[float, int] = {}
        for xv in xs:
            level = seen.get(xv, 0)
            seen[xv] = level + 1
            cv.dot(fr.sx(xv), base - level * 13.0, r=4.0, cls="accent-a")

    if mark in ("mean", "deviation"):
        mx = fr.sx(mean)
        cv.line(mx, fr.bottom, mx, top, cls="accent-b", extra=_dash(2.2))
        cv.text(mx, top - 8, f"x̄ = {_vn(mean, 2)}", cls="lbl", anchor="middle")
    if rows:
        step = (fr.bottom - 14.0 - (top + 10.0)) / max(n - 1, 1)
        for i, xv in enumerate(xs):
            cy = fr.bottom - 14.0 - i * step
            cv.line(fr.sx(xv), cy, fr.sx(mean), cy, cls="accent-c", extra=_dash(1.4))
            cv.dot(fr.sx(xv), cy, r=4.0, cls="accent-a")
        cv.text(fr.x0, box[1] - 22, "mỗi đoạn nét đứt là một độ lệch xᵢ − x̄",
                cls="lbl-sm")
    if mark == "median":
        mx = fr.sx(median)
        cv.line(mx, fr.bottom, mx, top, cls="accent-b", extra=_dash(2.2))
        cv.text(mx, top - 8, f"Mₑ = {_vn(median, 2)}", cls="lbl", anchor="middle")
    if mark == "range":
        y = top + 4
        cv.arrow(fr.sx(lo_v), y, fr.sx(hi_v), y, cls="accent-b", head=8)
        cv.arrow(fr.sx(hi_v), y, fr.sx(lo_v), y, cls="accent-b", head=8)
        cv.text((fr.sx(lo_v) + fr.sx(hi_v)) / 2, y - 8,
                f"R = {_vn(hi_v - lo_v, 1)}", cls="lbl", anchor="middle")
        for xv in (lo_v, hi_v):
            cv.line(fr.sx(xv), fr.bottom, fr.sx(xv), y, cls="ink-thin", extra=_dash(1.2))
    cv.text(fr.x0 + fr.w, box[1] - 22, f"n = {n}", cls="lbl-sm", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# 7. Đường cong chuẩn có tô vùng — hình quan trọng nhất của họ này
# --------------------------------------------------------------------------
_SHADES = {"none", "sigma", "left", "right", "two_tail", "between", "center"}


def build_normal_curve(p: Params) -> str:
    """Đường cong chuẩn N(μ, σ²) với một vùng được tô.

    ``shade``:
      * ``sigma``     — ba dải ±1σ, ±2σ, ±3σ kèm 68,3% / 95,4% / 99,7%;
      * ``left``/``right`` — một đuôi (giá trị p một phía, Φ(z));
      * ``two_tail``  — hai đuôi (miền bác bỏ, mức ý nghĩa α);
      * ``between``   — vùng giữa a và b;
      * ``center``    — vùng tin cậy giữa μ ± z·σ.

    Mọi phần trăm in trên hình đều lấy từ Φ tính bằng ``math.erf``, nên đổi z là
    con số tự đổi theo — không có nhãn nào "chết cứng".
    """
    mu = _fnum(p.get("mu"), 0.0)
    sigma = abs(_fnum(p.get("sigma"), 1.0))
    if sigma < 1e-9:
        sigma = 1.0
    shade = str(p.get("shade", "sigma"))
    if shade not in _SHADES:
        shade = "sigma"
    # z có dấu cho một đuôi (đuôi trái ứng với z âm); hai đuôi và khoảng tin cậy
    # thì đối xứng nên chỉ dùng |z|.
    z_raw = _fnum(p.get("z"), 1.96)
    z = abs(z_raw)
    a = _fnum(p.get("a"), mu - 0.6 * sigma)
    b = _fnum(p.get("b"), mu + 1.4 * sigma)
    if b < a:
        a, b = b, a
    xlabel = str(p.get("xlabel", "x"))
    area_label = p.get("area_label")
    caption = p.get("caption")

    tall = shade in ("sigma", "center", "two_tail")
    w = 490.0
    # sigma cần ba thanh nhịp chồng nhau nên cao hơn hẳn hai chế độ tall còn lại
    h = 372.0 if shade == "sigma" else (356.0 if tall else 306.0)
    box = (54.0, 54.0, 400.0, 176.0)
    # khung phải chứa trọn mọi mốc được tô, nếu không vùng tô sẽ bị cắt câm lặng
    reach = 3.7
    if shade in ("left", "right", "two_tail", "center"):
        reach = max(reach, z + 1.4)
    if shade == "between":
        reach = max(reach, abs(a - mu) / sigma + 1.0, abs(b - mu) / sigma + 1.0)
    reach = min(reach, 12.0)
    lo, hi = mu - reach * sigma, mu + reach * sigma
    ytop = _pdf(0.0) / sigma * 1.16
    cv = Canvas(w, h, title="Đường cong chuẩn",
                desc="Đường cong phân phối chuẩn với vùng diện tích được tô.")
    fr = _Frame(cv, box, lo, hi, 0.0, ytop)

    def dens(x: float) -> float:
        return _pdf((x - mu) / sigma) / sigma

    def curve_pts(x1: float, x2: float, n: int = 90):
        n = max(n, 2)
        step = (x2 - x1) / (n - 1)
        return [(fr.sx(x1 + i * step), fr.sy(dens(x1 + i * step))) for i in range(n)]

    def fill_between(x1: float, x2: float, cls: str):
        x1, x2 = max(x1, lo), min(x2, hi)
        if x2 - x1 <= 1e-9:
            return
        pts = [(fr.sx(x1), fr.sy(0.0))] + curve_pts(x1, x2, 64) + [(fr.sx(x2), fr.sy(0.0))]
        cv.polygon(pts, cls=cls)

    def centred(sx: float, text: str) -> float:
        """Kéo nhãn canh giữa vào trong khung ảnh.

        Kẹp theo mép vùng vẽ là chưa đủ: nhãn dài (``area_label`` do luật truyền
        vào) vẫn thò khỏi viewBox và bị cắt cụt một đầu — mà bản thân file SVG
        thì vẫn hợp lệ nên không có gì báo lỗi. Ước lượng bề rộng ~6,6px/ký tự.
        """
        half = 3.3 * len(text) + 4.0
        return min(max(sx, half + 6.0), w - half - 6.0)

    def span_label(x1: float, x2: float, y: float, text: str):
        """Thanh |←— … —→| dưới trục: gọn hơn là nhét chữ vào trong vùng tô."""
        s1, s2 = fr.sx(x1), fr.sx(x2)
        cv.line(s1, y - 5, s1, y + 5, cls="ink-thin")
        cv.line(s2, y - 5, s2, y + 5, cls="ink-thin")
        cv.arrow(s1, y, s2, y, cls="axis", head=7)
        cv.arrow(s2, y, s1, y, cls="axis", head=7)
        cv.text((s1 + s2) / 2, y - 7, text, cls="lbl-sm", anchor="middle")

    # `xt` xếp theo thứ tự ƯU TIÊN, không theo thứ tự trên trục: mốc của vùng tô
    # là thứ hình muốn chỉ, còn μ đã có nét đứt nên nhường chỗ khi chật.
    xt: list[float] = []
    if shade == "sigma":
        for kk, cls in ((3, "fill-c"), (2, "fill-c"), (1, "fill-a")):
            fill_between(mu - kk * sigma, mu + kk * sigma, cls)
        xt = [mu + kk * sigma for kk in (0, -1, 1, -2, 2, -3, 3)]
    elif shade == "left":
        fill_between(lo, mu + z_raw * sigma, "fill-a")
        xt = [mu + z_raw * sigma, mu]
    elif shade == "right":
        fill_between(mu + z_raw * sigma, hi, "fill-b")
        xt = [mu + z_raw * sigma, mu]
    elif shade == "two_tail":
        fill_between(lo, mu - z * sigma, "fill-b")
        fill_between(mu + z * sigma, hi, "fill-b")
        xt = [mu - z * sigma, mu + z * sigma, mu]
    elif shade == "between":
        fill_between(a, b, "fill-a")
        xt = [a, b, mu]
    elif shade == "center":
        fill_between(mu - z * sigma, mu + z * sigma, "fill-a")
        xt = [mu - z * sigma, mu + z * sigma, mu]
    else:
        xt = [mu]

    cv.polyline(curve_pts(lo, hi, 140), cls="curve")
    cv.line(fr.sx(mu), fr.bottom, fr.sx(mu), fr.sy(dens(mu)), cls="ink-thin", extra=_dash(1.4))

    def tick_name(x: float) -> str:
        k = (x - mu) / sigma
        if abs(k) < 1e-9:
            return "μ"
        sign = "+" if k > 0 else "−"
        mag = abs(k)
        return f"μ {sign} {'' if abs(mag - 1) < 1e-9 else _vn(mag, 2)}σ"

    rows_used = fr.frame_x(xlabel, xt, fmt=tick_name, stagger=True)
    # thanh nhịp nằm DƯỚI cả nhãn trục, nếu không nó lọt vào đúng dòng của nhãn ấy
    span_y = fr.label_bottom(rows_used) + 45

    # phần trăm diện tích: luôn tính lại từ Φ
    def area(x1: float, x2: float) -> float:
        return _cdf((x2 - mu) / sigma) - _cdf((x1 - mu) / sigma)

    if shade == "sigma":
        y = span_y
        for kk in (1, 2, 3):
            span_label(mu - kk * sigma, mu + kk * sigma, y,
                       f"{_vn(100 * area(mu - kk * sigma, mu + kk * sigma), 1)}%")
            y += 26
    elif shade in ("left", "right"):
        edge = mu + z_raw * sigma
        # đuôi THẬT chứ không phải diện tích đã bị khung cắt: nhãn ghi Φ(z) / giá trị p
        # nên con số phải là Φ(z), khớp với bảng tra — cắt ở μ ± 3,7σ lệch tới 10⁻⁴.
        val = _cdf(z_raw) if shade == "left" else 1.0 - _cdf(z_raw)
        txt = f"{area_label or ('Φ(z)' if shade == 'left' else 'giá trị p')} ≈ {_vn(val, 4)}"
        sx = fr.sx(mu + (z_raw + (1.5 if shade == "right" else -1.5)) * sigma)
        cv.text(centred(sx, txt), fr.sy(0.0) - 26, txt, cls="lbl-sm", anchor="middle")
    elif shade == "two_tail":
        tail = _cdf(-z)
        txt = f"{area_label or 'α/2'} ≈ {_vn(tail, 4)}"
        for side in (-1, 1):
            sx = centred(fr.sx(mu + side * (z + 1.1) * sigma), txt)
            cv.text(sx, fr.sy(0.0) - 26, txt, cls="lbl-sm", anchor="middle")
            cv.text(centred(sx, "miền bác bỏ"), span_y + 26, "miền bác bỏ",
                    cls="lbl-sm", anchor="middle")
        span_label(mu - z * sigma, mu + z * sigma, span_y,
                   f"không bác bỏ H₀ — {_vn(100 * area(mu - z * sigma, mu + z * sigma), 1)}%")
    elif shade == "between":
        txt = f"{area_label or 'P(a < X < b)'} ≈ {_vn(area(a, b), 4)}"
        cv.text(centred(fr.sx(0.5 * (a + b)), txt), fr.sy(0.0) - 26, txt,
                cls="lbl-sm", anchor="middle")
    elif shade == "center":
        conf = area(mu - z * sigma, mu + z * sigma)
        txt = f"{area_label or 'độ tin cậy'} ≈ {_vn(100 * conf, 1)}%"
        cv.text(centred(fr.sx(mu), txt), fr.sy(0.0) - 30, txt,
                cls="lbl-sm", anchor="middle")
        span_label(mu - z * sigma, mu + z * sigma, span_y,
                   f"± {_vn(z, 3)}σ  (biên sai số ME)")

    if caption:
        cv.text(20, 28, str(caption), cls="lbl-sm")
    else:
        cv.text(20, 28, f"N(μ = {_vn(mu, 2)}; σ = {_vn(sigma, 2)})", cls="lbl-sm")
    return cv.render()


# --------------------------------------------------------------------------
# 8. Hai đường cong chuẩn: α, β và lực kiểm định
# --------------------------------------------------------------------------
def build_power_curves(p: Params) -> str:
    """Phân phối dưới H₀ và dưới Hₐ trên cùng một trục, kèm vùng α và vùng β.

    Đây là hình duy nhất cho thấy vì sao α và β không thể cùng nhỏ: đẩy ranh
    giới c sang phải thì vùng α co lại nhưng vùng β nở ra.
    """
    mu0 = _fnum(p.get("mu0"), 0.0)
    mua = _fnum(p.get("mua"), 3.0)
    sigma = abs(_fnum(p.get("sigma"), 1.0)) or 1.0
    crit = _fnum(p.get("crit"), 1.645)
    if mua < mu0:
        mu0, mua = mua, mu0
    crit_x = mu0 + crit * sigma

    w, h = 500.0, 312.0
    box = (52.0, 62.0, 412.0, 176.0)
    lo = min(mu0, mua, crit_x) - 3.6 * sigma
    hi = max(mu0, mua, crit_x) + 3.6 * sigma
    ytop = _pdf(0.0) / sigma * 1.2
    cv = Canvas(w, h, title="Lực kiểm định",
                desc="Phân phối dưới giả thuyết không và giả thuyết đối, vùng sai lầm loại I và loại II.")
    fr = _Frame(cv, box, lo, hi, 0.0, ytop)

    def dens(x: float, m: float) -> float:
        return _pdf((x - m) / sigma) / sigma

    def curve(m: float, x1: float, x2: float, n: int = 120):
        step = (x2 - x1) / (n - 1)
        return [(fr.sx(x1 + i * step), fr.sy(dens(x1 + i * step, m))) for i in range(n)]

    def fill(m: float, x1: float, x2: float, cls: str):
        x1, x2 = max(x1, lo), min(x2, hi)
        if x2 - x1 <= 1e-9:
            return
        cv.polygon([(fr.sx(x1), fr.sy(0.0))] + curve(m, x1, x2, 70) + [(fr.sx(x2), fr.sy(0.0))],
                   cls=cls)

    fill(mu0, crit_x, hi, "fill-b")           # α — bác bỏ H₀ khi H₀ đúng
    fill(mua, lo, crit_x, "fill-c")           # β — không bác bỏ H₀ khi Hₐ đúng
    cv.polyline(curve(mu0, lo, hi), cls="curve")
    cv.polyline(curve(mua, lo, hi), cls="curve", extra=' stroke-dasharray="7 5"')
    cv.line(fr.sx(crit_x), fr.bottom, fr.sx(crit_x), box[1] - 6, cls="ink", extra=_dash(2.0))

    alpha = 1.0 - _cdf((crit_x - mu0) / sigma)
    beta = _cdf((crit_x - mua) / sigma)
    fr.frame_x(str(p.get("xlabel", "thống kê kiểm định")), [mu0, crit_x, mua],
               fmt=lambda t: "μ₀" if abs(t - mu0) < 1e-9 else ("μₐ" if abs(t - mua) < 1e-9 else "c"))
    cv.text(fr.sx(mu0), fr.sy(dens(mu0, mu0)) - 8, "H₀", cls="lbl", anchor="middle")
    cv.text(fr.sx(mua), fr.sy(dens(mua, mua)) - 8, "Hₐ", cls="lbl", anchor="middle")
    cv.text(fr.sx(crit_x), box[1] - 14, "ngưỡng c", cls="lbl-sm", anchor="middle")
    cv.text(fr.sx(crit_x) + 16, fr.bottom - 12, "α", cls="lbl")
    cv.text(fr.sx(crit_x) - 16, fr.bottom - 12, "β", cls="lbl", anchor="end")
    cv.text(20, 28, f"α = {_vn(alpha, 4)}   (sai lầm loại I)", cls="lbl-sm")
    cv.text(20, 44, f"β = {_vn(beta, 4)}   →   lực = 1 − β = {_vn(1 - beta, 4)}", cls="lbl-sm")
    return cv.render()


# --------------------------------------------------------------------------
# 9–11. Phân phối rời rạc dạng cột
# --------------------------------------------------------------------------
def _binom_pmf(n: int, prob: float) -> list[float]:
    """P(X = k) tính truy hồi để không phải dựng số tổ hợp khổng lồ."""
    out = [0.0] * (n + 1)
    if prob <= 0:
        out[0] = 1.0
        return out
    if prob >= 1:
        out[n] = 1.0
        return out
    out[0] = (1 - prob) ** n
    for k in range(n):
        out[k + 1] = out[k] * (n - k) / (k + 1) * prob / (1 - prob)
    return out


def _poisson_pmf(lam: float, kmax: int) -> list[float]:
    out = [math.exp(-lam)]
    for k in range(1, kmax + 1):
        out.append(out[-1] * lam / k)
    return out


def _geom_pmf(prob: float, kmax: int) -> list[float]:
    """Phân phối hình học đếm từ k = 1 (số phép thử tới lần thành công đầu tiên)."""
    return [(1 - prob) ** (k - 1) * prob for k in range(1, kmax + 1)]


def _discrete_bars(p: Params, ks: list[int], pmf: list[float], title: str,
                   desc: str, caption: str, mean: float, sd: float,
                   xlabel: str = "k") -> str:
    """Khung chung cho mọi biểu đồ cột phân phối rời rạc."""
    shade = str(p.get("shade", "none"))       # none | le | ge | eq
    at = _inum(p.get("at"), ks[len(ks) // 2], ks[0], ks[-1])
    show_mean = bool(p.get("show_mean", False))
    overlay = bool(p.get("overlay_normal", False))

    w, h = 480.0, 330.0
    box = (64.0, 74.0, 380.0, 186.0)
    top = (max(pmf) if pmf else 1.0) * 1.2 or 1.0
    cv = Canvas(w, h, title=title, desc=desc)
    fr = _Frame(cv, box, ks[0] - 0.7, ks[-1] + 0.7, 0.0, top)
    fr.frame_y("P(X = k)", fr.ticks_y(5))

    shaded = 0.0
    for k, pk in zip(ks, pmf):
        hot = (shade == "le" and k <= at) or (shade == "ge" and k >= at) \
            or (shade == "eq" and k == at)
        if hot:
            shaded += pk
        x1, x2 = fr.sx(k - 0.36), fr.sx(k + 0.36)
        y1, y2 = fr.sy(pk), fr.sy(0.0)
        cv.rect(x1, y1, x2 - x1, y2 - y1, cls="fill-b" if hot else "fill-a")
        cv.rect(x1, y1, x2 - x1, y2 - y1, cls="ink-thin")

    step = max(1, len(ks) // 12)
    fr.frame_x(xlabel, [k for i, k in enumerate(ks) if i % step == 0], nd=0)

    if overlay and sd > 0:
        n = 100
        x1, x2 = ks[0] - 0.5, ks[-1] + 0.5
        st = (x2 - x1) / (n - 1)
        pts = []
        for i in range(n):
            x = x1 + i * st
            pts.append((fr.sx(x), fr.sy(_pdf((x - mean) / sd) / sd)))
        cv.polyline(pts, cls="curve", extra=' stroke-dasharray="6 4"')
        cv.text(20, 46, f"xấp xỉ bằng N({_vn(mean, 2)}; {_vn(sd * sd, 2)})", cls="lbl-sm")
    if show_mean:
        mx = fr.sx(mean)
        cv.line(mx, fr.bottom, mx, box[1] - 4, cls="accent-c", extra=_dash(2.0))
        cv.text(mx + 6, box[1] - 8, f"μ = {_vn(mean, 2)}", cls="lbl")
    if shade in ("le", "ge", "eq"):
        sym = {"le": "≤", "ge": "≥", "eq": "="}[shade]
        # Đuôi phải phải cộng cả phần khối lượng nằm NGOÀI khung vẽ. Phân phối hình
        # học cắt ở k = 15 còn sót 0,65¹⁵ ≈ 0,0016 — đủ để P(X ≥ 5) in ra 0,1769
        # thay vì 0,1785 = 0,65⁴, tức là lệch hẳn con số người học tự tính được.
        if shade == "ge":
            shaded += max(0.0, 1.0 - sum(pmf))
        cv.text(w - 20, 46, f"P(X {sym} {at}) = {_vn(min(shaded, 1.0), 4)}",
                cls="lbl-sm", anchor="end")
    cv.text(20, 28, caption, cls="lbl-sm")
    cv.text(w - 20, 28, f"μ = {_vn(mean, 2)};  σ = {_vn(sd, 2)}",
            cls="lbl-sm", anchor="end")
    return cv.render()


def build_binomial_bars(p: Params) -> str:
    """Phân phối nhị thức B(n, p) dạng cột; tô được đuôi trái/phải hoặc một cột."""
    n = _inum(p.get("n"), 10, 1, 60)
    prob = min(max(_fnum(p.get("p"), 0.4), 0.0), 1.0)
    pmf = _binom_pmf(n, prob)
    mean = n * prob
    sd = math.sqrt(n * prob * (1 - prob))
    return _discrete_bars(p, list(range(n + 1)), pmf, "Phân phối nhị thức",
                          "Biểu đồ cột xác suất của phân phối nhị thức.",
                          f"X ~ B(n = {n}; p = {_vn(prob, 2)})", mean, sd)


def build_poisson_bars(p: Params) -> str:
    """Phân phối Poisson Po(λ) dạng cột."""
    lam = min(max(_fnum(p.get("lam"), 4.0), 0.0), 60.0)
    kmax = max(6, int(lam + 4 * math.sqrt(lam) + 4))
    kmax = min(kmax, 60)
    pmf = _poisson_pmf(lam, kmax)
    return _discrete_bars(p, list(range(kmax + 1)), pmf, "Phân phối Poisson",
                          "Biểu đồ cột xác suất của phân phối Poisson.",
                          f"X ~ Po(λ = {_vn(lam, 2)})", lam, math.sqrt(lam))


def build_geometric_bars(p: Params) -> str:
    """Phân phối hình học: số phép thử tới lần thành công đầu tiên (k = 1, 2, …)."""
    prob = min(max(_fnum(p.get("p"), 0.35), 0.02), 1.0)
    kmax = min(24, max(6, int(math.ceil(5 / prob))))
    pmf = _geom_pmf(prob, kmax)
    mean = 1.0 / prob
    sd = math.sqrt(1 - prob) / prob
    return _discrete_bars(p, list(range(1, kmax + 1)), pmf, "Phân phối hình học",
                          "Biểu đồ cột xác suất của phân phối hình học.",
                          f"P(X = k) = (1 − p)^(k−1)·p,  p = {_vn(prob, 2)}", mean, sd)


# --------------------------------------------------------------------------
# 12. Sơ đồ cây xác suất
# --------------------------------------------------------------------------
_TREE_DEFAULT = [
    {"label": "A", "p": 0.6, "children": [{"label": "B", "p": 0.7},
                                          {"label": "B̄", "p": 0.3}]},
    {"label": "Ā", "p": 0.4, "children": [{"label": "B", "p": 0.2},
                                          {"label": "B̄", "p": 0.8}]},
]


def _tree_branches(raw) -> list[dict]:
    """Chuẩn hoá cấu trúc cây; dữ liệu hỏng thì dùng cây mặc định."""
    if not isinstance(raw, list) or not raw:
        return [dict(b, children=list(b["children"])) for b in _TREE_DEFAULT]
    out = []
    for b in raw[:4]:
        if not isinstance(b, dict):
            continue
        kids_raw = b.get("children")
        kids = []
        if isinstance(kids_raw, list):
            for c in kids_raw[:4]:
                if isinstance(c, dict):
                    kids.append({"label": str(c.get("label", "")),
                                 "p": _fnum(c.get("p"), 0.5)})
        if not kids:
            kids = [{"label": "B", "p": 0.5}, {"label": "B̄", "p": 0.5}]
        out.append({"label": str(b.get("label", "")), "p": _fnum(b.get("p"), 0.5),
                    "children": kids})
    return out or [dict(b, children=list(b["children"])) for b in _TREE_DEFAULT]


def build_prob_tree(p: Params) -> str:
    """Sơ đồ cây hai giai đoạn.

    ``mode='prob'``: cạnh ghi xác suất, lá ghi tích dọc theo nhánh — đúng cái mà
    công thức nhân / xác suất toàn phần / Bayes đang nói.
    ``mode='count'``: cạnh không ghi số, chỉ đếm số nhánh (quy tắc nhân).
    """
    mode = "count" if str(p.get("mode", "prob")) == "count" else "prob"
    l1 = str(p.get("label1", "hành động 1"))
    l2 = str(p.get("label2", "hành động 2"))
    if mode == "count":
        m = _inum(p.get("m"), 3, 1, 5)
        nn = _inum(p.get("n"), 4, 1, 5)
        branches = [{"label": f"{i + 1}", "p": None,
                     "children": [{"label": f"{j + 1}", "p": None} for j in range(nn)]}
                    for i in range(m)]
    else:
        branches = _tree_branches(p.get("branches"))
    highlight = p.get("highlight")
    hi_pairs = set()
    if isinstance(highlight, list):
        for item in highlight:
            if isinstance(item, (list, tuple)) and len(item) == 2:
                hi_pairs.add((int(item[0]), int(item[1])))

    leaves = sum(len(b["children"]) for b in branches)
    w = 500.0
    h = max(230.0, 70.0 + leaves * 34.0)
    x_root, x1, x2 = 40.0, 176.0, 330.0
    ytop, ybot = 64.0, h - 34.0
    cv = Canvas(w, h, title="Sơ đồ cây xác suất",
                desc="Sơ đồ hình cây cho phép thử gồm hai giai đoạn.")

    step = (ybot - ytop) / max(leaves - 1, 1) if leaves > 1 else 0.0
    ys: list[list[float]] = []
    idx = 0
    for b in branches:
        row = []
        for _ in b["children"]:
            row.append(ytop + idx * step if leaves > 1 else (ytop + ybot) / 2)
            idx += 1
        ys.append(row)
    y1s = [sum(row) / len(row) for row in ys]
    y_root = sum(y1s) / len(y1s)

    cv.dot(x_root, y_root, r=4.0, cls="accent-a")
    total_named = 0.0
    for i, b in enumerate(branches):
        hot_branch = any(pair[0] == i for pair in hi_pairs)
        cls = "accent-b" if hot_branch else "ink"
        cv.line(x_root, y_root, x1, y1s[i], cls=cls)
        cv.dot(x1, y1s[i], r=3.6, cls="accent-a")
        cv.text(x1 + 8, y1s[i] - 6, b["label"], cls="lbl" if mode == "prob" else "lbl-sm")
        if mode == "prob":
            cv.text((x_root + x1) / 2, (y_root + y1s[i]) / 2 - 5,
                    _vn(b["p"], 3), cls="lbl-sm", anchor="middle")
        for j, c in enumerate(b["children"]):
            hot = (i, j) in hi_pairs
            cv.line(x1, y1s[i], x2, ys[i][j], cls="accent-b" if hot else "ink")
            cv.dot(x2, ys[i][j], r=3.6, cls="accent-a")
            cv.text(x2 + 8, ys[i][j] + 4, c["label"], cls="lbl")
            if mode == "prob":
                cv.text((x1 + x2) / 2, (y1s[i] + ys[i][j]) / 2 - 5,
                        _vn(c["p"], 3), cls="lbl-sm", anchor="middle")
                prod = b["p"] * c["p"]
                if hot:
                    total_named += prod
                cv.text(w - 16, ys[i][j] + 4, _vn(prod, 4),
                        cls="lbl-sm", anchor="end")
    if mode == "prob":
        cv.text(w - 16, 30, "tích dọc nhánh", cls="lbl-sm", anchor="end")
        if hi_pairs:
            cv.text(20, 30, f"tổng nhánh thuận lợi = {_vn(total_named, 4)}", cls="lbl-sm")
    else:
        m, nn = len(branches), len(branches[0]["children"])
        cv.text(x1, 32, f"{l1} ({m} cách)", cls="lbl-sm", anchor="middle")
        cv.text(x2, 32, f"{l2} ({nn} cách)", cls="lbl-sm", anchor="middle")
        cv.text(w / 2, h - 10, f"n(Ω) = {m} · {nn} = {m * nn}", cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 13–14. Tán xạ + hồi quy, và bảng minh hoạ hệ số tương quan
# --------------------------------------------------------------------------
# Bảng nhiễu cố định: hình phải deterministic nên không được gọi random.
_NOISE = [0.42, -0.87, 1.13, -0.35, 0.66, -1.24, 0.19, 0.95,
          -0.58, 1.41, -0.72, 0.28, -1.05, 0.81]


def _fit(pts: list[tuple[float, float]]):
    """Hồi quy bình phương tối thiểu y theo x: trả (a, b, r, x̄, ȳ)."""
    n = len(pts)
    xm = sum(x for x, _ in pts) / n
    ym = sum(y for _, y in pts) / n
    sxx = sum((x - xm) ** 2 for x, _ in pts)
    syy = sum((y - ym) ** 2 for _, y in pts)
    sxy = sum((x - xm) * (y - ym) for x, y in pts)
    b = sxy / sxx if sxx > 1e-12 else 0.0
    a = ym - b * xm
    r = sxy / math.sqrt(sxx * syy) if sxx > 1e-12 and syy > 1e-12 else 0.0
    return a, b, max(-1.0, min(1.0, r)), xm, ym


def _make_points(slope: float, intercept: float, noise: float, n: int):
    n = max(3, min(n, len(_NOISE)))
    return [(float(i + 1), intercept + slope * (i + 1) + noise * _NOISE[i])
            for i in range(n)]


def _points_for_r(target: float, n: int = 12) -> list[tuple[float, float]]:
    """Dựng mẫu điểm có hệ số tương quan xấp xỉ ``target``.

    |r| tăng đơn điệu theo |hệ số góc| khi biên độ nhiễu cố định, nên chia đôi
    trên hệ số góc là đủ; r hiển thị trên hình vẫn được tính lại từ điểm thật.
    """
    sign = -1.0 if target < 0 else 1.0
    goal = min(abs(target), 0.995)
    lo, hi = 0.0, 40.0
    pts = _make_points(0.0, 10.0, 1.0, n)
    for _ in range(48):
        mid = 0.5 * (lo + hi)
        pts = _make_points(mid, 10.0, 1.0, n)
        if abs(_fit(pts)[2]) < goal:
            lo = mid
        else:
            hi = mid
    return [(x, 10.0 + sign * (y - 10.0)) for x, y in pts]


def build_scatter_regression(p: Params) -> str:
    """Biểu đồ tán xạ + đường hồi quy bình phương tối thiểu.

    Hệ số a, b và r in trên hình đều được ``_fit`` tính lại từ chính các điểm
    đang vẽ, nên đường thẳng và con số không thể lệch nhau.
    """
    raw = p.get("points")
    pts: list[tuple[float, float]] = []
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, (list, tuple)) and len(item) == 2:
                pts.append((_fnum(item[0], 0.0), _fnum(item[1], 0.0)))
    if len(pts) < 3:
        pts = _make_points(_fnum(p.get("slope"), 1.6), _fnum(p.get("intercept"), 4.0),
                           _fnum(p.get("noise"), 1.7), _inum(p.get("n"), 12, 3, 14))
    show_res = bool(p.get("show_residuals", False))
    show_mean = bool(p.get("show_mean_point", False))
    a, b, r, xm, ym = _fit(pts)

    w, h = 460.0, 344.0
    box = (58.0, 68.0, 372.0, 202.0)
    xs = [x for x, _ in pts]
    ys = [y for _, y in pts]
    fx = [min(xs), max(xs)]
    line_y = [a + b * fx[0], a + b * fx[1]]
    xlo, xhi = min(xs), max(xs)
    ylo, yhi = min(ys + line_y), max(ys + line_y)
    px, py = 0.10 * (xhi - xlo or 1.0), 0.14 * (yhi - ylo or 1.0)
    cv = Canvas(w, h, title="Biểu đồ tán xạ và đường hồi quy",
                desc="Biểu đồ tán xạ với đường hồi quy bình phương tối thiểu.")
    fr = _Frame(cv, box, xlo - px, xhi + px, ylo - py, yhi + py)
    fr.frame_y(str(p.get("ylabel", "y")), fr.ticks_y(5))
    fr.frame_x(str(p.get("xlabel", "x")), fr.ticks_x(6))

    x_left, x_right = fr.xmin, fr.xmax
    cv.line(fr.sx(x_left), fr.sy(a + b * x_left), fr.sx(x_right), fr.sy(a + b * x_right),
            cls="accent-b", extra=' stroke-width="2.4"')
    if show_res:
        for x, y in pts:
            cv.line(fr.sx(x), fr.sy(y), fr.sx(x), fr.sy(a + b * x),
                    cls="accent-c", extra=_dash(1.5))
    for x, y in pts:
        cv.dot(fr.sx(x), fr.sy(y), r=3.6, cls="accent-a")
    if show_mean:
        cv.line(fr.x0, fr.sy(ym), fr.sx(xm), fr.sy(ym), cls="ink-thin", extra=_dash(1.3))
        cv.line(fr.sx(xm), fr.bottom, fr.sx(xm), fr.sy(ym), cls="ink-thin", extra=_dash(1.3))
        cv.dot(fr.sx(xm), fr.sy(ym), r=5.0, cls="accent-d")
        # đặt xuống DƯỚI đường hồi quy, về phía đường đi lên: để nguyên phía trên
        # thì nhãn nằm đúng trên nét hồi quy và thường trùng luôn một điểm dữ liệu
        side = 10.0 if b >= 0 else -10.0
        cv.text(fr.sx(xm) + side, fr.sy(ym) + 20, "(x̄; ȳ)", cls="lbl",
                anchor="start" if b >= 0 else "end")

    # hệ số góc âm phải thành "− 1,58·x", không phải "+ −1,58·x"
    cv.text(20, 28, f"ŷ = {_vn(a, 2)} {'+' if b >= 0 else '−'} {_vn(abs(b), 2)}·x", cls="lbl")
    cv.text(w - 18, 28, f"r = {_vn(r, 3)};  r² = {_vn(r * r, 3)}",
            cls="lbl-sm", anchor="end")
    if show_res:
        rss = sum((y - (a + b * x)) ** 2 for x, y in pts)
        cv.text(w - 18, 44, f"Σeᵢ² = {_vn(rss, 2)}", cls="lbl-sm", anchor="end")
    return cv.render()


def build_correlation_panels(p: Params) -> str:
    """Ba biểu đồ tán xạ cạnh nhau để thấy r nói lên điều gì.

    Giá trị r ghi dưới mỗi ô là r THẬT của bộ điểm trong ô đó (tính lại bằng
    ``_fit``), không phải giá trị đặt hàng — nên hình không bao giờ "hứa" một
    mức tương quan mà đám mây điểm không có.
    """
    targets = _floats(p.get("rs"), [0.95, 0.0, -0.85])[:3]
    while len(targets) < 3:
        targets.append(0.0)

    pw, ph = 142.0, 132.0
    gap = 22.0
    w = 3 * pw + 4 * gap
    h = 236.0
    cv = Canvas(w, h, title="Hệ số tương quan",
                desc="Ba đám mây điểm minh hoạ hệ số tương quan dương, gần không và âm.")
    cv.text(gap, 28, str(p.get("caption", "Hệ số tương quan r đo mức độ tuyến tính")),
            cls="lbl-sm")
    for i, target in enumerate(targets):
        pts = _points_for_r(target, 12)
        a, b, r, _, _ = _fit(pts)
        x0 = gap + i * (pw + gap)
        y0 = 50.0
        cv.rect(x0, y0, pw, ph, cls="ink-thin")
        xs = [x for x, _ in pts]
        ys = [y for _, y in pts]
        px = 0.08 * (max(xs) - min(xs) or 1.0)
        py = 0.12 * (max(ys) - min(ys) or 1.0)
        fr = _Frame(cv, (x0 + 8, y0 + 8, pw - 16, ph - 16),
                    min(xs) - px, max(xs) + px, min(ys) - py, max(ys) + py)
        cv.line(fr.sx(fr.xmin), fr.sy(a + b * fr.xmin),
                fr.sx(fr.xmax), fr.sy(a + b * fr.xmax),
                cls="accent-b", extra=' stroke-width="2"')
        for x, y in pts:
            cv.dot(fr.sx(x), fr.sy(y), r=3.0, cls="accent-a")
        cv.text(x0 + pw / 2, y0 + ph + 22, f"r = {_vn(r, 2)}", cls="lbl", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# 15–16. Sơ đồ Venn
# --------------------------------------------------------------------------
_VENN2 = {"union", "intersection", "disjoint", "complement", "conditional",
          "classical", "difference"}


def _lens_path(x1: float, x2: float, cy: float, r: float) -> str | None:
    """Path phần giao của hai đường tròn cùng bán kính (rỗng nếu không cắt nhau)."""
    d = x2 - x1
    if d <= 0 or d >= 2 * r:
        return None
    xm = 0.5 * (x1 + x2)
    hh = math.sqrt(max(r * r - (d / 2) ** 2, 0.0))
    return (f"M {_n(xm)},{_n(cy - hh)} A {_n(r)} {_n(r)} 0 0 1 {_n(xm)},{_n(cy + hh)} "
            f"A {_n(r)} {_n(r)} 0 0 1 {_n(xm)},{_n(cy - hh)} Z")


def _minus_path(x1: float, x2: float, cy: float, r: float) -> str:
    """Path phần A \\ B của hai đường tròn cùng bán kính (A trái, B phải).

    Không ghép hai đường tròn với ``fill-rule="evenodd"``: cách ấy cho hiệu ĐỐI
    XỨNG (A △ B) — tô cả hai múi ngoài — trong khi A \\ B chỉ có múi trái. Hình
    sai kiểu này người học không thể phát hiện, nên phải dựng biên tường minh:
    cung lớn của A đi vòng bên trái, rồi cung của B lồi vào trong A.
    """
    d = x2 - x1
    if d <= 0 or d >= 2 * r:                      # rời nhau: A \\ B chính là A
        return _circle_path(x1, cy, r)
    xm = 0.5 * (x1 + x2)
    hh = math.sqrt(max(r * r - (d / 2) ** 2, 0.0))
    return (f"M {_n(xm)},{_n(cy - hh)} "
            f"A {_n(r)} {_n(r)} 0 1 0 {_n(xm)},{_n(cy + hh)} "   # vòng ngoài theo A
            f"A {_n(r)} {_n(r)} 0 0 1 {_n(xm)},{_n(cy - hh)} Z")  # cắt vào theo B


def build_venn2(p: Params) -> str:
    """Sơ đồ Venn hai tập trong không gian mẫu Ω.

    ``mode``: ``union`` (phần giao đậm hơn — đúng chỗ bị đếm hai lần),
    ``intersection``, ``disjoint`` (xung khắc), ``complement`` (biến cố đối),
    ``conditional`` (B thành không gian mẫu mới), ``difference`` (A \\ B),
    ``classical`` (Ω gồm các kết quả đồng khả năng, đếm được bằng chấm).
    """
    mode = str(p.get("mode", "union"))
    if mode not in _VENN2:
        mode = "union"
    la = str(p.get("label_a", "A"))
    lb = str(p.get("label_b", "B"))

    w, h = 440.0, 290.0
    rx, ry, rw, rh = 34.0, 52.0, 372.0, 190.0
    cy = ry + rh / 2
    r = 76.0
    disjoint = mode in ("disjoint",)
    x1 = rx + rw / 2 - (100.0 if disjoint else 46.0)
    x2 = rx + rw / 2 + (100.0 if disjoint else 46.0)
    cv = Canvas(w, h, title="Sơ đồ Venn hai tập",
                desc="Sơ đồ Venn của hai biến cố trong không gian mẫu.")
    rect_path = (f"M {_n(rx)},{_n(ry)} L {_n(rx + rw)},{_n(ry)} "
                 f"L {_n(rx + rw)},{_n(ry + rh)} L {_n(rx)},{_n(ry + rh)} Z")
    cv.rect(rx, ry, rw, rh, cls="ink-thin")
    # nhãn Ω nằm ở góc dưới-trái: góc trên-trái là chỗ các chấm kết quả hay rơi vào
    cv.text(rx + 8, ry + rh - 10, "Ω", cls="lbl")

    lens = _lens_path(x1, x2, cy, r)
    if mode == "union":
        cv.circle(x1, cy, r, cls="fill-a")
        cv.circle(x2, cy, r, cls="fill-a")
        cv.text(rx + rw / 2, ry + rh + 26,
                "phần giao được tô hai lớp: đó là phần bị đếm hai lần",
                cls="lbl-sm", anchor="middle")
    elif mode == "intersection" and lens:
        cv.path(lens, cls="fill-b")
        cv.text(rx + rw / 2, ry + rh + 26, "A ∩ B", cls="lbl-sm", anchor="middle")
    elif mode == "disjoint":
        cv.circle(x1, cy, r, cls="fill-a")
        cv.circle(x2, cy, r, cls="fill-c")
        cv.text(rx + rw / 2, ry + rh + 26, "A ∩ B = ∅ (xung khắc)",
                cls="lbl-sm", anchor="middle")
    elif mode == "complement":
        cxo = rx + rw / 2
        cv.path(rect_path + " " + _circle_path(cxo, cy, r), cls="fill-b",
                extra=' fill-rule="evenodd"')
        cv.rect(rx, ry, rw, rh, cls="ink-thin")   # vẽ lại: vùng tô vừa phủ mất viền Ω
        cv.circle(cxo, cy, r, cls="ink")
        cv.text(cxo, cy + 6, la, cls="lbl", anchor="middle")
        cv.text(rx + rw / 2, ry + rh + 26, "vùng tô là biến cố đối Ā",
                cls="lbl-sm", anchor="middle")
        return cv.render()
    elif mode == "conditional":
        cv.circle(x2, cy, r, cls="fill-a")
        if lens:
            cv.path(lens, cls="fill-b")
        cv.text(rx + rw / 2, ry + rh + 26,
                "B trở thành không gian mẫu mới; phần đậm là A ∩ B",
                cls="lbl-sm", anchor="middle")
    elif mode == "difference":
        cv.path(_minus_path(x1, x2, cy, r), cls="fill-a")
        cv.text(rx + rw / 2, ry + rh + 26, "A \\ B", cls="lbl-sm", anchor="middle")
    elif mode == "classical":
        n_omega = _inum(p.get("n_omega"), 12, 2, 40)
        n_a = _inum(p.get("n_a"), 5, 0, n_omega)
        cx = rx + rw / 2 - 60
        cv.circle(cx, cy, r, cls="fill-a")
        inside, outside = _classical_dots(rx, ry, rw, rh, cx, cy, r, n_a, n_omega - n_a)
        for dx, dy in inside:
            cv.dot(dx, dy, r=4.0, cls="accent-b")
        for dx, dy in outside:
            cv.dot(dx, dy, r=4.0, cls="accent-a")
        cv.circle(cx, cy, r, cls="ink")
        cv.text(cx, cy + r - 14, la, cls="lbl", anchor="middle")
        cv.text(rx + rw / 2, ry + rh + 26,
                f"P(A) = n(A)/n(Ω) = {len(inside)}/{n_omega}",
                cls="lbl-sm", anchor="middle")
        return cv.render()

    cv.circle(x1, cy, r, cls="ink")
    cv.circle(x2, cy, r, cls="ink")
    # nhãn nằm HẲN trong đĩa (cách tâm 0,62·r): đặt cách tâm đúng r như trước thì
    # chữ rơi trúng nét tròn và bị đường viền cắt ngang
    off = 0.44 * r
    cv.text(x1 - off, cy - off + 5, la, cls="lbl", anchor="middle")
    cv.text(x2 + off, cy - off + 5, lb, cls="lbl", anchor="middle")
    return cv.render()


def _classical_dots(rx, ry, rw, rh, cx, cy, r, k_in, k_out):
    """Chấm kết quả đồng khả năng: k_in chấm trong A, k_out chấm ngoài A.

    Đặt theo lưới cố định (không random) và loại thẳng những ô rơi sai phía, để
    số chấm đếm được trên hình đúng bằng n(A) và n(Ω) ghi ở chú thích.
    """
    cand_in: list[tuple[float, float]] = []
    cand_out: list[tuple[float, float]] = []
    cols, rows = 12, 5
    for j in range(rows):
        for i in range(cols):
            x = rx + rw * (i + 0.5) / cols
            y = ry + rh * (j + 0.5) / rows
            d = math.hypot(x - cx, y - cy)
            if d < r - 18:
                cand_in.append((x, y))
            elif d > r + 16 and y < ry + rh - 26:
                cand_out.append((x, y))

    def spread(cands, k):
        """Chọn k vị trí rải đều trong danh sách ứng viên (thứ tự cố định).

        Lấy k phần tử đầu thì mọi chấm dồn hết lên hàng trên cùng — nhìn như lỗi
        vẽ chứ không như một tập kết quả.
        """
        k = max(0, min(k, len(cands)))
        if k == 0:
            return []
        stride = len(cands) / k
        return [cands[min(int(i * stride), len(cands) - 1)] for i in range(k)]

    return spread(cand_in, k_in), spread(cand_out, k_out)


def build_venn3(p: Params) -> str:
    """Sơ đồ Venn ba tập cho công thức cộng ba biến cố / bao hàm – loại trừ.

    Ba đĩa cùng tô một lớp mờ: chỗ giao đôi thành hai lớp, chỗ giao ba thành ba
    lớp. Độ đậm tăng dần chính là số lần một phần tử bị đếm thừa — cũng chính là
    lí do công thức phải trừ đi rồi cộng lại.
    """
    mode = "disjoint" if str(p.get("mode", "overlap")) == "disjoint" else "overlap"
    labels = p.get("labels")
    la, lb, lc = (list(labels) + ["A", "B", "C"])[:3] if isinstance(labels, list) \
        else ("A", "B", "C")

    w, h = 430.0, 336.0
    rx, ry, rw, rh = 26.0, 44.0, 378.0, 250.0
    cv = Canvas(w, h, title="Sơ đồ Venn ba tập",
                desc="Sơ đồ Venn của ba biến cố trong không gian mẫu.")
    cv.rect(rx, ry, rw, rh, cls="ink-thin")
    cv.text(rx + 10, ry + 20, "Ω", cls="lbl")

    if mode == "disjoint":
        # tâm chia đều bề ngang Ω (cách nhau rw/3 = 126) và r = 54 < 126/2:
        # ba đĩa RỜI hẳn nhau. Bố cục cũ (r = 52, tâm cách 93) cho hai chỗ giao
        # nhau thấy rõ — đúng cái mà chữ "đôi một rời nhau" nói là không có.
        r = 54.0
        centres = [(rx + rw * k / 6, ry + rh / 2) for k in (1, 3, 5)]
        fills = ["fill-a", "fill-b", "fill-c"]
        for (cx, cy), fill, name in zip(centres, fills, (la, lb, lc)):
            cv.circle(cx, cy, r, cls=fill)
            cv.circle(cx, cy, r, cls="ink")
            cv.text(cx, cy + 5, str(name), cls="lbl", anchor="middle")
        cv.text(rx + rw / 2, ry + rh + 26, "đôi một rời nhau",
                cls="lbl-sm", anchor="middle")
        return cv.render()

    r = 76.0
    cx0, cy0 = rx + rw / 2, ry + rh / 2 - 14
    d = 52.0
    centres = [(cx0 - d, cy0 - 16), (cx0 + d, cy0 - 16), (cx0, cy0 + 44)]
    for cx, cy in centres:
        cv.circle(cx, cy, r, cls="fill-a")
    for (cx, cy) in centres:
        cv.circle(cx, cy, r, cls="ink")
    cv.text(centres[0][0] - 40, centres[0][1] - 30, str(la), cls="lbl", anchor="middle")
    cv.text(centres[1][0] + 40, centres[1][1] - 30, str(lb), cls="lbl", anchor="middle")
    cv.text(centres[2][0], centres[2][1] + 52, str(lc), cls="lbl", anchor="middle")
    cv.text(rx + rw / 2, ry + rh + 26,
            "càng đậm càng bị đếm nhiều lần: 1 lớp, 2 lớp, 3 lớp",
            cls="lbl-sm", anchor="middle")
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "bar_chart": build_bar_chart,
    "histogram": build_histogram,
    "cumulative_curve": build_cumulative_curve,
    "pie_chart": build_pie_chart,
    "box_plot": build_box_plot,
    "data_dots": build_data_dots,
    "normal_curve": build_normal_curve,
    "power_curves": build_power_curves,
    "binomial_bars": build_binomial_bars,
    "poisson_bars": build_poisson_bars,
    "geometric_bars": build_geometric_bars,
    "prob_tree": build_prob_tree,
    "scatter_regression": build_scatter_regression,
    "correlation_panels": build_correlation_panels,
    "venn2": build_venn2,
    "venn3": build_venn3,
}
