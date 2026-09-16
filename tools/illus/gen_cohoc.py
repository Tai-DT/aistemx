"""Họ hình **cơ học**: động học, động lực học, dao động điều hoà, sóng cơ.

Ba nhóm hình, ứng với ba kiểu hiểu sai hay gặp nhất khi học cơ học phổ thông:

* **Đồ thị chuyển động** (x-t, v-t, a-t) — người học thuộc công thức nhưng không
  đọc được *độ dốc* và *diện tích dưới đồ thị*, vốn mới là chỗ hai đại lượng nối
  vào nhau. Nên mọi đồ thị ở đây đều đánh dấu sẵn một trong hai thứ đó.
* **Sơ đồ lực** — nguồn sai số một của bài động lực học là quên một lực hoặc
  phân tích trọng lực sai trên mặt phẳng nghiêng. Các hình vẽ đủ mọi lực đang
  tác dụng, và với mặt nghiêng thì vẽ luôn hình bình hành phân tích.
* **Dao động & sóng** — chỗ khó là *pha*: v sớm pha π/2 so với x, a ngược pha x,
  điểm trên sóng dừng dao động cùng/ngược pha. Nên có bộ ba đồ thị x-v-a dóng
  thẳng cột theo thời gian và vòng tròn pha.

Quy ước ký hiệu theo sách giáo khoa Việt Nam: v, a, P, N, T, Fₘₛ, F_đh, F_ht,
λ, A, ω, φ. Chỉ số dưới vẽ bằng ``tspan`` chứ không dùng ký tự Unicode hạ chỉ số
— bộ ký tự đó thiếu phần lớn chữ cái (không có "d", "ht", "ms") nên viết được
"v₀" mà không viết được "Fₘₛ", mà nửa nạc nửa mỡ thì còn tệ hơn.
"""

from __future__ import annotations

import math
from typing import Callable, Sequence

from .svgkit import Canvas, _n, esc

Params = dict


# --------------------------------------------------------------------------
# Vệ sinh tham số
# --------------------------------------------------------------------------
def _so(gt, mac_dinh: float, lo: float, hi: float) -> float:
    """Ép tham số về số thực nằm trong ``[lo, hi]``.

    Tham số tới từ luật khớp, từ ``bindings.json`` và từ tay người dùng, nên có
    thể là 0, số âm, chuỗi rác hay số khổng lồ. Kẹp ngay tại cửa vào là cách duy
    nhất bảo đảm mọi toạ độ tính sau đó còn nằm trong khung vẽ — chứ đi kiểm ở
    từng phép nhân thì sót là chắc chắn.
    """
    try:
        x = float(gt)
    except (TypeError, ValueError):
        return mac_dinh
    if not math.isfinite(x):
        return mac_dinh
    return min(max(x, lo), hi)


def _nguyen(gt, mac_dinh: int, lo: int, hi: int) -> int:
    try:
        x = int(float(gt))
    except (TypeError, ValueError, OverflowError):
        return mac_dinh
    return min(max(x, lo), hi)


def _co(gt, mac_dinh: bool) -> bool:
    return mac_dinh if gt is None else bool(gt)


def _chia(lo: float, hi: float, n: int) -> list[float]:
    n = max(int(n), 2)
    buoc = (hi - lo) / (n - 1)
    return [lo + i * buoc for i in range(n)]


def _buoc_dep(span: float, muc_tieu: int = 6) -> float:
    """Bước chia "tròn" (1 · 2 · 2,5 · 5 × 10ᵏ) cho một khoảng bất kỳ.

    Trục có vạch chia lẻ (0,37 — 0,74 — …) thì người học không đọc được giá trị,
    mà đồ thị chuyển động chỉ có nghĩa khi đọc được giá trị.
    """
    if span <= 0:
        return 1.0
    tho = span / max(muc_tieu, 1)
    mu = math.floor(math.log10(tho))
    co_so = tho / (10.0 ** mu)
    for m in (1.0, 2.0, 2.5, 5.0):
        if co_so <= m:
            return m * (10.0 ** mu)
    return 10.0 ** (mu + 1)


# --------------------------------------------------------------------------
# Nét vẽ dùng lại
# --------------------------------------------------------------------------
def _dau_ten(cv: Canvas, x: float, y: float, goc: float, cls: str, dai: float = 6.5) -> None:
    a1, a2 = goc + math.radians(152), goc - math.radians(152)
    cv.polygon(
        [(x, y), (x + dai * math.cos(a1), y + dai * math.sin(a1)),
         (x + dai * math.cos(a2), y + dai * math.sin(a2))],
        cls=cls, extra=' stroke="none" fill-opacity="1"',
    )


def _ten(cv: Canvas, x1: float, y1: float, x2: float, y2: float,
         cls: str = "accent-d", rong: float = 1.4, dai: float = 6.5,
         cls_dau: str | None = None) -> None:
    """Mũi tên nét mảnh cho đường phụ trợ (λ, A, Δt, kích thước…).

    Không dùng ``Canvas.arrow`` vì hàm đó chốt nét 2,5 — đúng cho vectơ lực,
    quá dày cho đường ghi kích thước, và khi hai thứ nằm cạnh nhau thì người xem
    không phân biệt được đâu là đại lượng vật lí, đâu là chú thích.
    """
    cv.line(x1, y1, x2, y2, cls=cls, extra=f' stroke-width="{_n(rong)}"')
    _dau_ten(cv, x2, y2, math.atan2(y2 - y1, x2 - x1), cls_dau or cls, dai)


def _kich_thuoc(cv: Canvas, x1: float, y1: float, x2: float, y2: float,
                nhan: str = "", cls: str = "accent-d",
                dx: float = 0.0, dy: float = -6.0, anchor: str = "middle",
                cls_nhan: str = "lbl-sm") -> None:
    """Đường kích thước hai đầu mũi tên kèm nhãn ở giữa."""
    cv.line(x1, y1, x2, y2, cls=cls, extra=' stroke-width="1.3"')
    goc = math.atan2(y2 - y1, x2 - x1)
    _dau_ten(cv, x2, y2, goc, cls)
    _dau_ten(cv, x1, y1, goc + math.pi, cls)
    if nhan:
        cv.text((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, nhan, cls=cls_nhan, anchor=anchor)


def _chu(cv: Canvas, x: float, y: float, chinh: str, chi_so: str = "",
         cls: str = "lbl", anchor: str = "start", tren: bool = False) -> None:
    """Nhãn ký hiệu có chỉ số: ``_chu(cv, x, y, "F", "ms")`` → F ms."""
    noi = esc(chinh)
    if chi_so:
        noi += f'<tspan dy="{-4 if tren else 4}" font-size="10">{esc(chi_so)}</tspan>'
    cv.raw(f'<text x="{_n(x)}" y="{_n(y)}" text-anchor="{anchor}" class="{cls}">{noi}</text>')


def _chu_nhieu(cv: Canvas, x: float, y: float, phan: Sequence[Sequence[str]],
               cls: str = "lbl-sm", anchor: str = "start") -> None:
    """Câu có nhiều ký hiệu mang chỉ số: ``[("W", "đ"), (" = W", "t"), (" …", "")]``.

    Sau mỗi ``tspan`` hạ chỉ số phải nâng lại bằng ``dy`` ngược dấu, nếu không
    thì toàn bộ phần chữ còn lại của câu bị tụt xuống theo.
    """
    noi = ""
    for cap in phan:
        chinh, chi_so = (list(cap) + [""])[:2]
        noi += esc(chinh)
        if chi_so:
            noi += f'<tspan dy="4" font-size="10">{esc(chi_so)}</tspan><tspan dy="-4"></tspan>'
    cv.raw(f'<text x="{_n(x)}" y="{_n(y)}" text-anchor="{anchor}" class="{cls}">{noi}</text>')


def _cung(cv: Canvas, cx: float, cy: float, r: float, a1: float, a2: float,
          cls: str = "accent-d", rong: float = 1.4) -> None:
    """Cung tròn từ góc ``a1`` tới ``a2`` (radian, quy ước toán học: y hướng lên).

    Phải khử nền bằng ``style`` chứ không bằng thuộc tính ``fill``: các lớp
    ``accent-*`` đặt ``fill`` trong CSS, mà quy tắc CSS thắng thuộc tính trình
    bày — viết ``fill="none"`` thì cung vẫn bị tô đặc thành một vệt màu.
    """
    x1, y1 = cx + r * math.cos(a1), cy - r * math.sin(a1)
    x2, y2 = cx + r * math.cos(a2), cy - r * math.sin(a2)
    lon = 1 if abs(a2 - a1) > math.pi else 0
    # trục y màn hình lật xuống nên chiều quét của cung cũng đảo so với công thức toán
    quet = 0 if a2 > a1 else 1
    cv.path(
        f"M {_n(x1)} {_n(y1)} A {_n(r)} {_n(r)} 0 {lon} {quet} {_n(x2)} {_n(y2)}",
        cls=cls, extra=f' style="fill:none;stroke-width:{_n(rong)}"',
    )


def _gach_nen(cv: Canvas, x1: float, x2: float, y: float, xuong: bool = True,
              buoc: float = 15.0, dai: float = 9.0, bo_qua: tuple | None = None) -> None:
    """Mặt sàn / trần: đường liền kèm vạch chéo về phía phần "vật chất".

    ``bo_qua`` là khoảng x bỏ trống vạch chéo — dùng khi có vectơ (thường là P)
    đi xuyên qua mặt sàn, để nét chú thích không lẫn vào nét gạch nền.
    """
    cv.line(x1, y, x2, y, cls="ink")
    n = int(max(x2 - x1, 0) // buoc)
    for i in range(n + 1):
        x = x1 + i * buoc + buoc * 0.5
        if x > x2:
            break
        if bo_qua and bo_qua[0] <= x <= bo_qua[1]:
            continue
        cv.line(x, y, x - dai * 0.75, y + (dai if xuong else -dai), cls="ink-thin")


def _lo_xo(cv: Canvas, x1: float, y1: float, x2: float, y2: float,
           vong: int = 8, bien: float = 10.0, cls: str = "ink") -> None:
    """Lò xo zigzag nối hai điểm (số vòng cố định để hình tất định)."""
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1.0
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux
    dau = min(11.0, L * 0.18)
    s0, s1 = dau, L - dau
    pts = [(x1, y1), (x1 + ux * s0, y1 + uy * s0)]
    n = max(int(vong) * 2, 2)
    for i in range(1, n):
        t = s0 + (s1 - s0) * i / n
        dau_hieu = 1 if i % 2 else -1
        pts.append((x1 + ux * t + nx * bien * dau_hieu, y1 + uy * t + ny * bien * dau_hieu))
    pts.append((x1 + ux * s1, y1 + uy * s1))
    pts.append((x2, y2))
    cv.polyline(pts, cls=cls)


def _hop(cv: Canvas, cx: float, cy: float, w: float, h: float, goc: float = 0.0,
         nhan: str = "", cls: str = "fill-a") -> None:
    """Vật (khối hộp) có thể xoay theo mặt phẳng nghiêng."""
    c, s = math.cos(goc), math.sin(goc)
    goc_hop = []
    for sx, sy in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
        px, py = sx * w / 2, sy * h / 2
        goc_hop.append((cx + px * c - py * s, cy + px * s + py * c))
    cv.polygon(goc_hop, cls=cls)
    cv.polyline(goc_hop + [goc_hop[0]], cls="ink")
    if nhan:
        # lệch trái trong lòng vật: đúng tâm là chỗ gốc vectơ P, tên vật đặt ở
        # đó thì luôn bị thân mũi tên xuyên qua
        cv.text(cx - w * 0.22, cy + 5, nhan, cls="lbl", anchor="middle")


def _trong_khung(cv: Canvas, diem: Sequence[Sequence[float]], box: tuple,
                 cls: str, rong: float | None = None) -> None:
    """Vẽ đường nhưng chỉ phần nằm trong ``box``.

    Vòng sóng và nhánh hypebol vốn kéo dài vô hạn; SVG tự cắt ở mép viewBox
    nhưng khi đó toạ độ ghi trong file vẫn nằm ngoài khung — vừa làm hỏng phép
    kiểm "hình không tràn khung", vừa khiến file phình lên vì những điểm không
    ai nhìn thấy. Nên cắt bằng tay ngay lúc dựng.
    """
    x0, y0, w, h = box
    dai: list[list[tuple[float, float]]] = []
    hien: list[tuple[float, float]] = []
    for x, y in diem:
        if x0 <= x <= x0 + w and y0 <= y <= y0 + h:
            hien.append((x, y))
        else:
            if len(hien) > 1:
                dai.append(hien)
            hien = []
    if len(hien) > 1:
        dai.append(hien)
    # ``style`` chứ không phải thuộc tính: lớp accent-* có ``fill`` trong CSS và
    # CSS thắng thuộc tính, để nguyên thì nhánh hypebol biến thành mảng màu đặc.
    kieu = "fill:none"
    if rong:
        kieu += f";stroke-width:{_n(rong)}"
    for d in dai:
        cv.polyline(d, cls=cls, extra=f' style="{kieu}"')


class _Khung:
    """Khung toạ độ có vạch chia và nhãn số.

    Khác ``_Plot`` trong ``generators2d`` ở hai điểm, đều vì đồ thị chuyển động
    cần: trục luôn kèm số đo (đọc được v từ độ dốc thì mới có ý nghĩa), và có
    sẵn ``to_duoi`` để tô diện tích dưới đường — thứ mang nghĩa vật lí (quãng
    đường dưới đồ thị v-t, độ biến thiên vận tốc dưới đồ thị a-t).
    """

    def __init__(self, cv: Canvas, xmin: float, xmax: float, ymin: float, ymax: float,
                 box: tuple[float, float, float, float]):
        self.cv = cv
        self.xmin, self.xmax = float(xmin), float(xmax)
        self.ymin, self.ymax = float(ymin), float(ymax)
        if self.xmax - self.xmin < 1e-9:
            self.xmax = self.xmin + 1.0
        if self.ymax - self.ymin < 1e-9:
            self.ymax = self.ymin + 1.0
        self.x0, self.y0, self.pw, self.ph = box

    def sx(self, x: float) -> float:
        t = (min(max(x, self.xmin), self.xmax) - self.xmin) / (self.xmax - self.xmin)
        return self.x0 + t * self.pw

    def sy(self, y: float) -> float:
        t = (self.ymax - min(max(y, self.ymin), self.ymax)) / (self.ymax - self.ymin)
        return self.y0 + t * self.ph

    def y_truc_x(self) -> float:
        return self.sy(0) if self.ymin <= 0 <= self.ymax else self.y0 + self.ph

    def x_truc_y(self) -> float:
        return self.sx(0) if self.xmin <= 0 <= self.xmax else self.x0

    def truc(self, nhan_x: str = "t (s)", nhan_y: str = "", so_x: bool = True,
             so_y: bool = True, buoc_x: float | None = None, buoc_y: float | None = None) -> None:
        cv = self.cv
        bx = buoc_x or _buoc_dep(self.xmax - self.xmin, 6)
        by = buoc_y or _buoc_dep(self.ymax - self.ymin, 5)
        yx, xy = self.y_truc_x(), self.x_truc_y()
        for i in range(0, 200):
            g = math.ceil(self.xmin / bx) * bx + i * bx
            if g > self.xmax + 1e-9:
                break
            cv.line(self.sx(g), self.y0, self.sx(g), self.y0 + self.ph, cls="grid")
            # bỏ số ở sát mũi tên: chỗ đó đã dành cho tên trục, hai chữ chồng nhau
            if so_x and abs(g) > 1e-9 and self.sx(g) < self.x0 + self.pw - 34:
                cv.text(self.sx(g), yx + 15, _n(round(g, 3)), cls="lbl-sm", anchor="middle")
        for i in range(0, 200):
            g = math.ceil(self.ymin / by) * by + i * by
            if g > self.ymax + 1e-9:
                break
            cv.line(self.x0, self.sy(g), self.x0 + self.pw, self.sy(g), cls="grid")
            if so_y and abs(g) > 1e-9:
                cv.text(xy - 7, self.sy(g) + 4, _n(round(g, 3)), cls="lbl-sm", anchor="end")
        cv.arrow(self.x0, yx, self.x0 + self.pw + 8, yx, cls="axis", head=7)
        cv.arrow(xy, self.y0 + self.ph, xy, self.y0 - 8, cls="axis", head=7)
        cv.text(self.x0 + self.pw + 6, yx + 17, nhan_x, cls="lbl-sm", anchor="end")
        if nhan_y:
            cv.text(xy - 4, self.y0 - 12, nhan_y, cls="lbl-sm", anchor="middle")

    def duong(self, mau: Sequence[Sequence[float]], cls: str = "curve") -> None:
        self.cv.polyline([(self.sx(x), self.sy(y)) for x, y in mau], cls=cls)

    def to_duoi(self, mau: Sequence[Sequence[float]], cls: str = "fill-a") -> None:
        """Tô miền giữa đường và trục hoành (ý nghĩa: tích phân của đại lượng)."""
        if len(mau) < 2:
            return
        yx = self.y_truc_x()
        pts = [(self.sx(mau[0][0]), yx)]
        pts += [(self.sx(x), self.sy(y)) for x, y in mau]
        pts.append((self.sx(mau[-1][0]), yx))
        self.cv.polygon(pts, cls=cls)


# ==========================================================================
# 1. Đồ thị chuyển động
# ==========================================================================
def build_motion_xt(p: Params) -> str:
    """Đồ thị toạ độ (hoặc quãng đường) - thời gian.

    ``a = 0`` cho chuyển động thẳng đều: đường thẳng, độ dốc chính là vận tốc.
    ``a ≠ 0`` cho biến đổi đều: parabol, và khi ấy vận tốc là độ dốc *tiếp
    tuyến* chứ không phải độ dốc dây cung — nên hai thứ ấy được vẽ tách bạch.
    """
    x0 = _so(p.get("x0"), 0.0, -40.0, 40.0)
    v = _so(p.get("v"), 2.0, -20.0, 20.0)
    a = _so(p.get("a"), 0.0, -8.0, 8.0)
    tmax = _so(p.get("tmax"), 6.0, 1.0, 20.0)
    nhan_x = str(p.get("xlabel", "t (s)"))
    nhan_y = str(p.get("ylabel", "x (m)"))
    ten_doc = str(p.get("slope_label", "v"))
    do_doc = _co(p.get("slope"), False)
    day_cung = _co(p.get("chord"), False)
    danh_dau_d = _co(p.get("delta"), False)
    tiep_tuyen = p.get("tangent")
    tho = p.get("points")

    if isinstance(tho, (list, tuple)) and len(tho) >= 2:
        mau = []
        for q in tho:
            try:
                mau.append((_so(q[0], 0.0, 0.0, tmax), _so(q[1], 0.0, -60.0, 60.0)))
            except (TypeError, IndexError, KeyError):
                continue
        mau = mau or [(0.0, x0), (tmax, x0 + v * tmax)]
        mau.sort(key=lambda q: q[0])
    elif abs(a) < 1e-9:
        mau = [(0.0, x0), (tmax, x0 + v * tmax)]
    else:
        mau = [(t, x0 + v * t + 0.5 * a * t * t) for t in _chia(0.0, tmax, 60)]

    ys = [y for _, y in mau] + [0.0]
    lo, hi = min(ys), max(ys)
    bien = max((hi - lo) * 0.18, 0.6)
    ymin, ymax = lo - bien, hi + bien

    w, h = 400.0, 292.0
    box = (60.0, 26.0, w - 92, h - 70)
    cv = Canvas(w, h, title=f"Đồ thị {nhan_y.split(' ')[0]} - t",
                desc="Đồ thị toạ độ theo thời gian; độ dốc của đồ thị là vận tốc.")
    k = _Khung(cv, 0.0, tmax * 1.04, ymin, ymax, box)
    k.truc(nhan_x, nhan_y)
    k.duong(mau, cls="curve")
    cv.dot(k.sx(mau[0][0]), k.sy(mau[0][1]), r=3.2, cls="accent-a")
    cv.dot(k.sx(mau[-1][0]), k.sy(mau[-1][1]), r=3.2, cls="accent-a")

    if do_doc and abs(a) < 1e-9:
        t1, t2 = tmax * 0.22, tmax * 0.66
        y1, y2 = x0 + v * t1, x0 + v * t2
        X1, X2 = k.sx(t1), k.sx(t2)
        Y1, Y2 = k.sy(y1), k.sy(y2)
        cv.line(X1, Y1, X2, Y1, cls="accent-d", extra=' stroke-dasharray="5 4" stroke-width="1.5"')
        cv.line(X2, Y1, X2, Y2, cls="accent-d", extra=' stroke-dasharray="5 4" stroke-width="1.5"')
        cv.text((X1 + X2) / 2, Y1 + (16 if v > 0 else -8), "Δt", cls="lbl-sm", anchor="middle")
        cv.text(X2 + 7, (Y1 + Y2) / 2 + 4, "Δ" + nhan_y[0], cls="lbl-sm")
        cv.text(box[0] + box[2] - 2, box[1] + 16,
                f"{ten_doc} = Δ{nhan_y[0]} / Δt = tan α", cls="lbl-sm", anchor="end")
        _cung(cv, X1, Y1, 26, 0.0, math.atan2(Y1 - Y2, X2 - X1), cls="accent-d")
        cv.text(X1 + 30, Y1 - 6, "α", cls="lbl")

    if day_cung:
        X1, Y1 = k.sx(mau[0][0]), k.sy(mau[0][1])
        X2, Y2 = k.sx(mau[-1][0]), k.sy(mau[-1][1])
        cv.line(X1, Y1, X2, Y2, cls="accent-b", extra=' stroke-dasharray="6 4" stroke-width="1.8"')
        _chu(cv, (X1 + X2) / 2, (Y1 + Y2) / 2 - 9, ten_doc, "tb", cls="lbl", anchor="middle")

    if danh_dau_d:
        (_, y1), (_, y2) = mau[0], mau[-1]
        xm = box[0] + box[2] - 16
        # kẻ hết chiều ngang tới đường kích thước: nếu chỉ kẻ tới điểm trên đồ
        # thị thì mức ứng với t = 0 nằm ngay trên trục tung và biến mất
        for yy, nh in ((y1, "x"), (y2, "x")):
            cv.line(k.x_truc_y(), k.sy(yy), xm + 8, k.sy(yy),
                    cls="ink-thin", extra=' stroke-dasharray="4 4"')
        _chu(cv, k.x_truc_y() - 7, k.sy(y1) + 4, "x", "1", cls="lbl", anchor="end")
        _chu(cv, k.x_truc_y() - 7, k.sy(y2) + 4, "x", "2", cls="lbl", anchor="end")
        _kich_thuoc(cv, xm, k.sy(y1), xm, k.sy(y2), "", cls="accent-b")
        _chu(cv, xm - 6, (k.sy(y1) + k.sy(y2)) / 2 + 4, "d", "", cls="lbl", anchor="end")

    if tiep_tuyen is not None:
        t0 = _so(tiep_tuyen, tmax * 0.5, 0.0, tmax)
        y_0 = x0 + v * t0 + 0.5 * a * t0 * t0
        doc = v + a * t0
        ta, tb = max(0.0, t0 - tmax * 0.28), min(tmax, t0 + tmax * 0.28)
        cv.line(k.sx(ta), k.sy(y_0 + doc * (ta - t0)), k.sx(tb), k.sy(y_0 + doc * (tb - t0)),
                cls="accent-b", extra=' stroke-dasharray="7 4" stroke-width="1.8"')
        cv.dot(k.sx(t0), k.sy(y_0), r=3.6, cls="accent-b")
        cv.text(box[0] + box[2] - 2, box[1] + 16,
                "hệ số góc tiếp tuyến = vận tốc tức thời", cls="lbl-sm", anchor="end")
    if p.get("note"):
        cv.text(box[0] + 2, box[1] + 16, str(p["note"]), cls="lbl-sm")
    return cv.render()


def build_motion_vt(p: Params) -> str:
    """Đồ thị vận tốc - thời gian.

    Hai ý nghĩa hình học được đánh dấu sẵn vì đó là toàn bộ nội dung của đồ thị
    này: **độ dốc** cho gia tốc, **diện tích dưới đồ thị** cho độ dịch chuyển.
    """
    v0 = _so(p.get("v0"), 2.0, -20.0, 20.0)
    a = _so(p.get("a"), 1.5, -8.0, 8.0)
    tmax = _so(p.get("tmax"), 6.0, 1.0, 20.0)
    nhan_y = str(p.get("ylabel", "v (m/s)"))
    ten_doc = str(p.get("slope_label", "a"))
    ten_dt = str(p.get("area_label", "d"))
    to = _co(p.get("area"), False)
    do_doc = _co(p.get("slope"), False)
    trung_binh = _co(p.get("mean"), False)
    dai = p.get("strip")

    mau = [(0.0, v0), (tmax, v0 + a * tmax)]
    ys = [y for _, y in mau] + [0.0]
    lo, hi = min(ys), max(ys)
    bien = max((hi - lo) * 0.18, 0.6)
    w, h = 400.0, 292.0
    box = (60.0, 26.0, w - 92, h - 70)
    cv = Canvas(w, h, title="Đồ thị v - t",
                desc="Đồ thị vận tốc theo thời gian; độ dốc là gia tốc, "
                     "diện tích dưới đồ thị là độ dịch chuyển.")
    k = _Khung(cv, 0.0, tmax * 1.04, lo - bien, hi + bien, box)
    k.truc("t (s)", nhan_y)

    # chỉ tô khi vận tốc không đổi dấu: đổi dấu thì "diện tích" là hiệu đại số,
    # tô một mảng liền sẽ dạy sai rằng quãng đường cộng dồn.
    if to and mau[0][1] >= 0 and mau[1][1] >= 0:
        k.to_duoi(mau, cls="fill-a")
        cv.text(k.sx(tmax * 0.45), k.sy(max(mau[0][1], 0) * 0.42) + 4,
                f"{ten_dt} = diện tích", cls="lbl-sm", anchor="middle")
    k.duong(mau, cls="curve")

    if isinstance(dai, (list, tuple)) and len(dai) == 2:
        t1 = _so(dai[0], 0.0, 0.0, tmax)
        t2 = _so(dai[1], min(t1 + 1.0, tmax), t1, tmax)
        d_mau = [(t1, v0 + a * t1), (t2, v0 + a * t2)]
        if d_mau[0][1] >= 0 and d_mau[1][1] >= 0:
            k.to_duoi(d_mau, cls="fill-b")
        for tt in (t1, t2):
            cv.line(k.sx(tt), k.sy(v0 + a * tt), k.sx(tt), k.y_truc_x(),
                    cls="accent-b", extra=' stroke-width="1.4"')
        cv.text(k.sx((t1 + t2) / 2), k.y_truc_x() - 6, f"Δ{ten_dt}", cls="lbl-sm", anchor="middle")

    if do_doc and abs(a) > 1e-9:
        t1, t2 = tmax * 0.24, tmax * 0.68
        y1, y2 = v0 + a * t1, v0 + a * t2
        X1, X2, Y1, Y2 = k.sx(t1), k.sx(t2), k.sy(y1), k.sy(y2)
        cv.line(X1, Y1, X2, Y1, cls="accent-d", extra=' stroke-dasharray="5 4" stroke-width="1.5"')
        cv.line(X2, Y1, X2, Y2, cls="accent-d", extra=' stroke-dasharray="5 4" stroke-width="1.5"')
        cv.text((X1 + X2) / 2, Y1 + (15 if a > 0 else -7), "Δt", cls="lbl-sm", anchor="middle")
        cv.text(X2 + 7, (Y1 + Y2) / 2 + 4, "Δv", cls="lbl-sm")
        cv.text(box[0] + box[2] - 2, box[1] + 16, f"{ten_doc} = Δv / Δt", cls="lbl-sm", anchor="end")

    if trung_binh:
        vtb = v0 + a * tmax / 2
        cv.line(k.x_truc_y(), k.sy(vtb), k.sx(tmax), k.sy(vtb),
                cls="accent-b", extra=' stroke-dasharray="6 4" stroke-width="1.6"')
        _chu(cv, k.sx(tmax) + 4, k.sy(vtb) + 4, "v", "tb", cls="lbl")
    if p.get("note"):
        cv.text(box[0] + 2, box[1] + 16, str(p["note"]), cls="lbl-sm")
    return cv.render()


def build_motion_trio(p: Params) -> str:
    """Bộ ba đồ thị x-t, v-t, a-t của chuyển động thẳng biến đổi đều.

    Ba khung dóng thẳng cột theo cùng trục thời gian: chỉ khi xếp như vậy mới
    thấy được x là parabol *vì* v là đường thẳng, và v là đường thẳng *vì* a
    không đổi — ba đồ thị rời nhau thì mối quan hệ ấy biến mất.
    """
    x0 = _so(p.get("x0"), 0.0, -30.0, 30.0)
    v0 = _so(p.get("v0"), 1.0, -15.0, 15.0)
    a = _so(p.get("a"), 1.2, -8.0, 8.0)
    tmax = _so(p.get("tmax"), 5.0, 1.0, 15.0)

    w, h = 400.0, 436.0
    pw = w - 96
    cv = Canvas(w, h, title="Đồ thị x - t, v - t, a - t",
                desc="Ba đồ thị chuyển động thẳng biến đổi đều dóng cùng một trục thời gian.")
    khung = []
    for i, (nhan, ham) in enumerate((
        ("x (m)", lambda t: x0 + v0 * t + 0.5 * a * t * t),
        ("v (m/s)", lambda t: v0 + a * t),
        ("a (m/s²)", lambda t: a),
    )):
        mau = [(t, ham(t)) for t in _chia(0.0, tmax, 50 if i == 0 else 2)]
        ys = [y for _, y in mau] + [0.0]
        lo, hi = min(ys), max(ys)
        bien = max((hi - lo) * 0.2, 0.5)
        box = (64.0, 26.0 + i * 138.0, pw, 96.0)
        k = _Khung(cv, 0.0, tmax * 1.04, lo - bien, hi + bien, box)
        k.truc("t (s)" if i == 2 else "t", nhan, so_x=(i == 2))
        if i == 1 and min(y for _, y in mau) >= 0:
            k.to_duoi(mau, cls="fill-a")
        k.duong(mau, cls="curve")
        khung.append(k)
    khung[1].cv.text(khung[1].sx(tmax * 0.5), khung[1].sy(0) - 12,
                     "diện tích = độ dịch chuyển", cls="lbl-sm", anchor="middle")
    cv.text(w - 10, 40, "độ dốc x-t = v", cls="lbl-sm", anchor="end")
    cv.text(w - 10, 178, "độ dốc v-t = a", cls="lbl-sm", anchor="end")
    return cv.render()


def build_free_fall(p: Params) -> str:
    """Rơi tự do (hoặc ném thẳng đứng lên) chụp ảnh hoạt nghiệm.

    Vị trí vật sau những khoảng thời gian **bằng nhau** — nhìn thấy ngay quãng
    đường các giây liên tiếp tỉ lệ 1 : 3 : 5 : 7, tức là chính hệ quả của
    h = ½gt² mà công thức viết ra không nói được.
    """
    h = _so(p.get("h"), 45.0, 1.0, 500.0)
    n = _nguyen(p.get("n"), 4, 2, 6)
    len_ = str(p.get("direction", "xuong")) == "len"
    g = _so(p.get("g"), 9.8, 1.0, 30.0)

    w, hgt = 396.0, 344.0
    x_quy = 176.0
    y_dinh, y_day = 44.0, 280.0
    cao = y_day - y_dinh
    cv = Canvas(w, hgt,
                title="Ném thẳng đứng lên" if len_ else "Rơi tự do",
                desc="Vị trí vật sau những khoảng thời gian bằng nhau; "
                     "quãng đường các khoảng liên tiếp tỉ lệ 1 : 3 : 5 : 7.")
    _gach_nen(cv, 128.0, 330.0, y_day, xuong=True)
    cv.line(x_quy, y_dinh - 8, x_quy, y_day, cls="ink-thin", extra=' stroke-dasharray="4 4"')

    muc = []
    for kk in range(n + 1):
        phan = (kk / n) ** 2 if not len_ else 1.0 - ((n - kk) / n) ** 2
        muc.append(y_dinh + (1.0 - phan) * cao if len_ else y_dinh + phan * cao)
    for kk, y in enumerate(muc):
        cv.line(x_quy - 44, y, x_quy + 46, y, cls="ink-thin", extra=' stroke-dasharray="4 4"')
        cv.circle(x_quy, y, 8.5, cls="fill-a")
        cv.circle(x_quy, y, 8.5, cls="ink")
        nhan_t = "t = 0" if kk == 0 else f"t = {kk}Δt"
        # ghi "v = 0" ngay trên dòng thời gian ở đỉnh, thay vì thành một nhãn
        # riêng: quanh đỉnh các mốc sát nhau, thêm chữ rời là chồng lên nhau
        if len_ and kk == n:
            nhan_t += " (v = 0)"
        cv.text(x_quy - 50, y + 4, nhan_t, cls="lbl-sm", anchor="end")
    for kk in range(n):
        y1, y2 = muc[kk], muc[kk + 1]
        _kich_thuoc(cv, x_quy + 56, y1, x_quy + 56, y2, "", cls="accent-d")
        cv.text(x_quy + 64, (y1 + y2) / 2 + 4,
                f"{2 * kk + 1}" if not len_ else f"{2 * (n - kk) - 1}", cls="lbl-sm")
    _kich_thuoc(cv, x_quy + 108, muc[0], x_quy + 108, muc[-1], "", cls="accent-b")
    cv.text(x_quy + 116, (muc[0] + muc[-1]) / 2 + 4, f"h = {_n(round(h, 1))} m", cls="lbl-sm")

    if len_:
        cv.arrow(x_quy + 22, y_day - 6, x_quy + 22, y_day - 60, cls="accent-a", head=8)
        _chu(cv, x_quy + 28, y_day - 54, "v", "0", cls="lbl")
        ti_le = " : ".join(str(2 * (n - i) - 1) for i in range(n))
        ghi = f"lên chậm dần: quãng đường các khoảng bằng nhau tỉ lệ {ti_le}"
    else:
        cv.arrow(x_quy + 22, y_dinh + 8, x_quy + 22, y_dinh + 62, cls="accent-a", head=8)
        cv.text(x_quy + 28, y_dinh + 58, "v", cls="lbl")
        ti_le = " : ".join(str(2 * i + 1) for i in range(n))
        ghi = f"v tăng đều · quãng đường các khoảng bằng nhau tỉ lệ {ti_le}"
    cv.arrow(44.0, 96.0, 44.0, 146.0, cls="accent-b", head=8)
    cv.text(50.0, 126.0, "g", cls="lbl")
    cv.text(w - 10, hgt - 12, ghi, cls="lbl-sm", anchor="end")
    return cv.render()


def build_horizontal_throw(p: Params) -> str:
    """Ném ngang: nửa parabol từ độ cao H, phân tích vận tốc thành vₓ và v_y.

    Vẽ kèm chuyển động rơi tự do song song ở mép trái để thấy hai vật chạm đất
    cùng lúc — đó là ý cốt lõi "chuyển động theo phương thẳng đứng là rơi tự do,
    không phụ thuộc v₀" mà công thức t = √(2H/g) hàm ý.
    """
    v0 = _so(p.get("v0"), 12.0, 1.0, 60.0)
    H = _so(p.get("H"), 20.0, 1.0, 300.0)
    g = _so(p.get("g"), 9.8, 1.0, 30.0)
    t_roi = math.sqrt(2 * H / g)
    L = v0 * t_roi

    w, h = 470.0, 300.0
    trai, tren = 112.0, 40.0
    rong, cao = 300.0, 190.0
    y_dat = tren + cao
    cv = Canvas(w, h, title="Chuyển động ném ngang",
                desc="Quỹ đạo nửa parabol của vật ném ngang từ độ cao H, "
                     "kèm phân tích vận tốc thành thành phần ngang và thẳng đứng.")
    _gach_nen(cv, 74.0, 430.0, y_dat, xuong=True)
    cv.line(trai - 22, tren, trai, tren, cls="ink")          # mép bệ phóng
    cv.line(trai - 22, tren, trai - 22, y_dat, cls="ink-thin", extra=' stroke-dasharray="4 4"')

    quy_dao = []
    for i in range(0, 61):
        x = L * i / 60.0
        y = g * x * x / (2 * v0 * v0)
        quy_dao.append((trai + x / L * rong, tren + y / H * cao))
    cv.polyline(quy_dao, cls="curve")

    # vật rơi tự do thả cùng lúc từ cùng độ cao, dùng để đối chiếu
    for i in (2, 4, 6):
        yy = tren + ((i / 6.0) ** 2) * cao
        cv.circle(trai - 22, yy, 4.5, cls="accent-c")
        cv.circle(quy_dao[i * 10][0], quy_dao[i * 10][1], 4.5, cls="accent-a")
        cv.line(trai - 22, yy, quy_dao[i * 10][0], quy_dao[i * 10][1],
                cls="ink-thin", extra=' stroke-dasharray="3 4"')

    cv.arrow(trai, tren, trai + 62, tren, cls="accent-b", head=8)
    _chu(cv, trai + 66, tren - 5, "v", "0", cls="lbl")
    _kich_thuoc(cv, trai - 48, tren, trai - 48, y_dat, "", cls="accent-d")
    cv.text(trai - 54, (tren + y_dat) / 2 + 4, f"H = {_n(round(H, 1))} m",
            cls="lbl-sm", anchor="end")
    _kich_thuoc(cv, trai, y_dat + 26, trai + rong, y_dat + 26, "", cls="accent-d")
    cv.text(trai + rong / 2, y_dat + 42, f"L = {_n(round(L, 1))} m", cls="lbl-sm", anchor="middle")

    # phân tích vận tốc tại 3/4 quãng bay
    j = 45
    mx, my = quy_dao[j]
    t = t_roi * j / 60.0
    vx_px, vy_px = 48.0, 48.0 * (g * t) / v0
    vy_px = min(vy_px, 62.0)
    cv.arrow(mx, my, mx + vx_px, my, cls="accent-c", head=7)
    cv.arrow(mx, my, mx, my + vy_px, cls="accent-c", head=7)
    cv.arrow(mx, my, mx + vx_px, my + vy_px, cls="accent-b", head=8)
    _chu(cv, mx + vx_px / 2, my - 6, "v", "x", cls="lbl-sm", anchor="middle")
    _chu(cv, mx - 6, my + vy_px / 2, "v", "y", cls="lbl-sm", anchor="end")
    cv.text(mx + vx_px + 6, my + vy_px + 4, "v", cls="lbl")
    _cung(cv, mx, my, 26.0, 0.0, -math.atan2(vy_px, vx_px), cls="accent-d")
    cv.text(mx + 30, my + 14, "β", cls="lbl-sm")
    return cv.render()


# ==========================================================================
# 2. Chuyển động tròn đều
# ==========================================================================
def build_circular_motion(p: Params) -> str:
    """Chuyển động tròn đều: v tiếp tuyến, gia tốc (hoặc lực) hướng vào tâm.

    Vẽ v và a_ht vuông góc nhau là chủ ý: hiểu sai phổ biến nhất là tưởng gia
    tốc cùng hướng vận tốc, trong khi ở đây tốc độ không đổi mà hướng thì đổi.
    """
    goc = _so(p.get("angle"), 48.0, 0.0, 360.0)
    nhan_a = str(p.get("center_label", "a_ht"))
    hien_a = _co(p.get("show_a"), True)
    hien_v = _co(p.get("show_v"), True)
    hien_goc = _co(p.get("show_omega"), False)
    d_goc = _so(p.get("dphi"), 55.0, 10.0, 120.0)

    R = 96.0
    w, h = 380.0, 300.0
    cx, cy = 168.0, 152.0
    th = math.radians(goc)
    px, py = cx + R * math.cos(th), cy - R * math.sin(th)
    cv = Canvas(w, h, title="Chuyển động tròn đều",
                desc="Vật chuyển động tròn đều: vectơ vận tốc tiếp tuyến với quỹ đạo, "
                     "gia tốc hướng tâm hướng vào tâm.")
    cv.circle(cx, cy, R, cls="ink-thin", extra=' stroke-dasharray="6 5"')
    cv.dot(cx, cy, r=3.4, cls="accent-b")
    cv.text(cx - 12, cy + 5, "O", cls="lbl", anchor="end")
    cv.line(cx, cy, px, py, cls="ink")
    # nhãn r lệch vuông góc bán kính, và lệch về phía KHÔNG có cung Δφ — bên kia
    # đã có vectơ a_ht hoặc cung góc quét chiếm chỗ
    ben = 1.0 if hien_goc else -1.0
    cv.text((cx + px) / 2 + ben * math.sin(th) * 15,
            (cy + py) / 2 + ben * math.cos(th) * 15 + 4, "r", cls="lbl", anchor="middle")
    cv.dot(px, py, r=5.0, cls="accent-a")

    tx, ty = -math.sin(th), -math.cos(th)      # tiếp tuyến, chiều quay ngược kim đồng hồ
    if hien_v:
        cv.arrow(px, py, px + tx * 66, py + ty * 66, cls="accent-a", head=9)
        cv.text(px + tx * 66 + 6, py + ty * 66 - 4, "v", cls="lbl")
    if hien_a:
        nx, ny = (cx - px) / R, (cy - py) / R
        cv.arrow(px, py, px + nx * 58, py + ny * 58, cls="accent-b", head=9)
        chinh, chi = (nhan_a.split("_", 1) + [""])[:2]
        _chu(cv, px + nx * 58 + 8, py + ny * 58 + 12, chinh, chi.strip("{}"), cls="lbl")
        cv.right_angle(px, py, px + tx * 22, py + ty * 22, px + nx * 22, py + ny * 22, size=13)
    if hien_goc:
        th2 = th + math.radians(d_goc)
        qx, qy = cx + R * math.cos(th2), cy - R * math.sin(th2)
        cv.line(cx, cy, qx, qy, cls="ink-thin", extra=' stroke-dasharray="5 4"')
        cv.dot(qx, qy, r=4.0, cls="accent-c")
        _cung(cv, cx, cy, 42.0, th, th2, cls="accent-d", rong=1.8)
        cv.text(cx + 50 * math.cos((th + th2) / 2), cy - 50 * math.sin((th + th2) / 2) + 4,
                "Δφ", cls="lbl-sm")
    # mũi tên chiều quay: tiếp tuyến theo chiều góc tăng là (−sinθ, −cosθ) trên
    # hệ toạ độ màn hình (trục y lật), không phải (−sinθ, cosθ) như hệ toán học
    g2 = math.radians(146)
    _cung(cv, cx, cy, R + 16, math.radians(98), g2, cls="accent-c", rong=2.0)
    _dau_ten(cv, cx + (R + 16) * math.cos(g2), cy - (R + 16) * math.sin(g2),
             math.atan2(-math.cos(g2), -math.sin(g2)), "accent-c", dai=8.0)
    cv.text(cx - 76, cy - R - 20, "ω", cls="lbl")
    cv.text(w - 12, h - 46, "tốc độ không đổi,", cls="lbl-sm", anchor="end")
    cv.text(w - 12, h - 30, "hướng vận tốc đổi liên tục", cls="lbl-sm", anchor="end")
    return cv.render()


# ==========================================================================
# 3. Sơ đồ lực
# ==========================================================================
def build_fbd_horizontal(p: Params) -> str:
    """Sơ đồ lực: vật trên mặt phẳng ngang.

    Luôn vẽ đủ P và N kể cả khi bài chỉ hỏi lực ma sát — quên phản lực là lỗi
    thường gặp nhất, và N mới là cái quyết định độ lớn Fₘₛ = μN.
    """
    keo = _co(p.get("keo"), True)
    ma_sat = _co(p.get("ma_sat"), True)
    gia_toc = str(p.get("gia_toc", ""))
    nhan_keo = str(p.get("nhan_keo", "F"))

    w, h = 400.0, 274.0
    gx, gy = 200.0, 168.0
    y_san = 194.0
    cv = Canvas(w, h, title="Sơ đồ lực - vật trên mặt phẳng ngang",
                desc="Các lực tác dụng lên vật đặt trên mặt phẳng ngang: "
                     "trọng lực, phản lực, lực kéo và lực ma sát.")
    _gach_nen(cv, 36.0, 364.0, y_san, xuong=True, bo_qua=(gx - 22, gx + 22))
    _hop(cv, gx, gy, 78.0, 52.0)

    cv.arrow(gx, gy, gx, gy - 66, cls="accent-c", head=9)
    cv.text(gx + 7, gy - 68, "N", cls="lbl")
    cv.arrow(gx, gy, gx, gy + 64, cls="accent-b", head=9)
    cv.text(gx + 7, gy + 62, "P", cls="lbl")
    if keo:
        cv.arrow(gx + 39, gy, gx + 112, gy, cls="accent-a", head=9)
        cv.text(gx + 116, gy - 6, nhan_keo, cls="lbl")
    if ma_sat:
        cv.arrow(gx - 39, gy, gx - 106, gy, cls="accent-d", head=9)
        _chu(cv, gx - 110, gy - 6, "F", "ms", cls="lbl", anchor="end")
    if gia_toc == "ngang":
        _ten(cv, gx + 44, gy - 46, gx + 104, gy - 46, cls="ink", rong=2.0, cls_dau="lbl")
        cv.text(gx + 108, gy - 42, "a", cls="lbl")
    elif gia_toc in ("len", "xuong"):
        y1 = gy - 8 if gia_toc == "len" else gy - 68
        y2 = gy - 68 if gia_toc == "len" else gy - 8
        _ten(cv, gx + 118, y1, gx + 118, y2, cls="ink", rong=2.0, cls_dau="lbl")
        cv.text(gx + 124, (y1 + y2) / 2 + 4, "a", cls="lbl")
    # chỉ được nói "hợp lực bằng 0" khi hình đúng là thế: có mũi tên gia tốc mà
    # vẫn ghi cân bằng thì câu chú thích phản lại chính hình mình vẽ
    if not keo and not ma_sat:
        if gia_toc:
            cv.text(w - 12, h - 22, "vật có gia tốc thẳng đứng → N ≠ P",
                    cls="lbl-sm", anchor="end")
        else:
            cv.text(w - 12, h - 22, "hợp lực bằng 0 → vật đứng yên hoặc chuyển động thẳng đều",
                    cls="lbl-sm", anchor="end")
    return cv.render()


def build_fbd_incline(p: Params) -> str:
    """Sơ đồ lực trên mặt phẳng nghiêng, kèm phân tích trọng lực.

    Hai thành phần P·sinα (dọc mặt, gây trượt) và P·cosα (ép vuông góc, quyết
    định N) vẽ liền hình bình hành với P: chỗ sai kinh điển là gán nhầm sin cho
    thành phần vuông góc, mà nhìn hình thì không gán nhầm được.
    """
    alpha = _so(p.get("alpha"), 30.0, 8.0, 55.0)
    ma_sat = _co(p.get("ma_sat"), False)
    hien_phan_tich = _co(p.get("phan_tich"), True)
    th = math.radians(alpha)

    day = 300.0
    cao = day * math.tan(th)
    if cao > 186.0:                       # dốc đứng thì rút ngắn đáy cho vừa khung
        cao, day = 186.0, 186.0 / math.tan(th)
    L = math.hypot(day, cao)
    LP = 74.0
    ux, uy = day / L, cao / L            # dọc mặt, hướng xuống dốc (sang phải)
    nx, ny = cao / L, -day / L           # pháp tuyến ngoài (lên trên, ra khỏi mặt)
    canh = 42.0
    # Dốc càng thoải, N càng dựng đứng và càng dễ chọc ra khỏi mép trên; nên lề
    # trên phải tính từ tầm với thật của vectơ chứ không đặt cứng một con số.
    voi_N = (canh / 2 + LP * math.cos(th)) * day / L
    tren = max(46.0, 32.0 + voi_N - 0.54 * cao)
    ox, oy = 66.0, tren + cao
    A = (ox, oy)
    B = (ox + day, oy)
    C = (ox, oy - cao)
    S = (B[0] + (C[0] - B[0]) * 0.46, B[1] + (C[1] - B[1]) * 0.46)
    G = (S[0] + nx * canh / 2, S[1] + ny * canh / 2)
    w = ox + day + 74.0
    h = max(oy + 46.0, G[1] + LP + 30.0)
    cv = Canvas(w, h, title="Sơ đồ lực trên mặt phẳng nghiêng",
                desc="Vật trên mặt phẳng nghiêng góc alpha: trọng lực được phân tích "
                     "thành thành phần dọc mặt nghiêng và thành phần vuông góc với mặt.")
    cv.polygon([A, B, C], cls="fill-c")
    cv.polyline([A, B, C, A], cls="ink")
    _gach_nen(cv, ox, ox + day, oy, xuong=True, buoc=17.0, dai=8.0)
    _hop(cv, G[0], G[1], canh, canh, goc=math.atan2(uy, ux))

    Px, Py = G[0], G[1] + LP
    cv.arrow(G[0], G[1], Px, Py, cls="accent-b", head=9)
    cv.text(Px + 7, Py + 2, "P", cls="lbl")
    if hien_phan_tich:
        dt = LP * math.sin(th)
        dn = LP * math.cos(th)
        T1 = (G[0] + ux * dt, G[1] + uy * dt)
        T2 = (G[0] - nx * dn, G[1] - ny * dn)
        # hai thành phần mang đúng màu của P và vẽ nét mảnh hơn: chúng KHÔNG phải
        # hai lực mới, chỉ là P nhìn theo hai phương — tô màu khác là dạy sai
        _ten(cv, G[0], G[1], T1[0], T1[1], cls="accent-b", rong=1.8, dai=7.5)
        _ten(cv, G[0], G[1], T2[0], T2[1], cls="accent-b", rong=1.8, dai=7.5)
        for T in (T1, T2):
            cv.line(T[0], T[1], Px, Py, cls="ink-thin", extra=' stroke-dasharray="4 4"')
        cv.text(T1[0] + 6, T1[1] + 14, "P sin α", cls="lbl-sm")
        cv.text(T2[0] - 6, T2[1] + 12, "P cos α", cls="lbl-sm", anchor="end")
    cv.arrow(G[0], G[1], G[0] + nx * LP * math.cos(th), G[1] + ny * LP * math.cos(th),
             cls="accent-c", head=9)
    cv.text(G[0] + nx * LP * math.cos(th) + 6, G[1] + ny * LP * math.cos(th) - 4, "N", cls="lbl")
    if ma_sat:
        cv.arrow(G[0], G[1], G[0] - ux * 62, G[1] - uy * 62, cls="accent-d", head=9)
        _chu(cv, G[0] - ux * 62 - 6, G[1] - uy * 62 - 5, "F", "ms", cls="lbl", anchor="end")
    _cung(cv, B[0], B[1], 40.0, math.pi, math.pi - th, cls="accent-d", rong=1.8)
    cv.text(B[0] - 52, B[1] - 12, "α", cls="lbl", anchor="middle")
    return cv.render()


def build_fbd_hanging(p: Params) -> str:
    """Sơ đồ lực: vật treo trên dây (lực căng T và trọng lực P)."""
    gia_toc = str(p.get("gia_toc", ""))
    can_bang = _co(p.get("can_bang"), False)

    w, h = 320.0, 306.0
    x = 140.0
    y_tran = 44.0
    gy = 190.0
    cv = Canvas(w, h, title="Sơ đồ lực - vật treo trên dây",
                desc="Vật treo bằng dây: lực căng dây hướng lên, trọng lực hướng xuống.")
    _gach_nen(cv, 60.0, 224.0, y_tran, xuong=False)
    cv.line(x, y_tran, x, gy - 24, cls="ink")
    _hop(cv, x, gy, 62.0, 46.0)
    # T và P vẽ cùng độ dài: hình này thường dùng cho "hai lực cân bằng", vẽ lệch
    # độ dài là gợi ý sai rằng một lực lớn hơn lực kia
    cv.arrow(x, gy - 24, x, gy - 94, cls="accent-c", head=9)
    cv.text(x + 8, gy - 92, "T", cls="lbl")
    cv.arrow(x, gy, x, gy + 70, cls="accent-b", head=9)
    cv.text(x + 8, gy + 70, "P", cls="lbl")
    if gia_toc in ("len", "xuong"):
        y1 = gy + 20 if gia_toc == "len" else gy - 48
        y2 = gy - 48 if gia_toc == "len" else gy + 20
        _ten(cv, x + 92, y1, x + 92, y2, cls="ink", rong=2.0, cls_dau="lbl")
        cv.text(x + 98, (y1 + y2) / 2 + 4, "a", cls="lbl")
    if can_bang:
        cv.text(w - 12, h - 20, "T = P: hai lực cân bằng", cls="lbl-sm", anchor="end")
    return cv.render()


def build_connected_bodies(p: Params) -> str:
    """Hệ hai vật nối bằng dây: máy Atwood, bàn - vật treo, hoặc kéo trên mặt ngang.

    Vẽ lực căng ở **cả hai đầu dây** cho thấy dây truyền nguyên độ lớn lực căng
    — cơ sở để viết chung một gia tốc cho cả hệ.
    """
    kieu = str(p.get("kind", "atwood"))
    ma_sat = _co(p.get("ma_sat"), False)

    if kieu == "ngang":
        w, h = 430.0, 262.0
        y_san = 190.0
        cv = Canvas(w, h, title="Hai vật nối dây, kéo trên mặt ngang",
                    desc="Hai vật nối bằng dây trên mặt phẳng ngang, chịu lực kéo F.")
        _gach_nen(cv, 40.0, 390.0, y_san, xuong=True)
        g1x, g2x, gy = 140.0, 272.0, 164.0
        _hop(cv, g1x, gy, 60.0, 52.0, nhan="m₁")
        _hop(cv, g2x, gy, 60.0, 52.0, nhan="m₂")
        cv.line(g1x + 30, gy, g2x - 30, gy, cls="ink")
        # hai mũi tên T ngắn hơn nửa khoảng cách hai vật, và nhãn đặt ngay trên
        # thân mũi tên của mình — để ở đầu mũi thì hai chữ T rơi trùng một điểm
        _ten(cv, g1x + 30, gy - 18, g1x + 62, gy - 18, cls="accent-c", rong=2.0)
        cv.text(g1x + 46, gy - 24, "T", cls="lbl", anchor="middle")
        _ten(cv, g2x - 30, gy - 18, g2x - 62, gy - 18, cls="accent-c", rong=2.0)
        cv.text(g2x - 46, gy - 24, "T", cls="lbl", anchor="middle")
        cv.arrow(g2x + 30, gy, g2x + 104, gy, cls="accent-a", head=9)
        cv.text(g2x + 108, gy - 6, "F", cls="lbl")
        if ma_sat:
            for cx in (g1x, g2x):
                _ten(cv, cx - 30, gy + 16, cx - 72, gy + 16, cls="accent-d", rong=2.0)
                _chu(cv, cx - 51, gy + 10, "F", "ms", cls="lbl-sm", anchor="middle")
        cv.text(w - 12, 34.0, "cả hệ cùng một gia tốc a", cls="lbl-sm", anchor="end")
        return cv.render()

    if kieu == "ban-treo":
        w, h = 440.0, 310.0
        y_ban = 148.0
        cv = Canvas(w, h, title="Vật trên bàn nối vật treo qua ròng rọc",
                    desc="Vật trên mặt bàn nằm ngang nối qua ròng rọc với vật treo.")
        cv.line(46.0, y_ban, 312.0, y_ban, cls="ink")
        _gach_nen(cv, 46.0, 300.0, y_ban + 1, xuong=True, buoc=18.0, dai=7.0,
                  bo_qua=(126.0, 158.0))
        g1x, g1y = 146.0, y_ban - 24.0
        _hop(cv, g1x, g1y, 64.0, 46.0, nhan="m₁")
        rx, ry, rr = 312.0, y_ban - 6.0, 18.0
        cv.line(rx, ry, rx, y_ban, cls="ink-thin")     # giá đỡ ròng rọc ở mép bàn
        cv.circle(rx, ry, rr, cls="fill-b")
        cv.circle(rx, ry, rr, cls="ink")
        cv.dot(rx, ry, r=2.6, cls="accent-b")
        cv.line(g1x + 32, g1y, rx, g1y, cls="ink")
        _cung(cv, rx, ry, rr, math.pi / 2, 0.0, cls="ink", rong=2.0)
        g2x, g2y = rx + rr, 236.0
        cv.line(g2x, ry, g2x, g2y - 22, cls="ink")
        _hop(cv, g2x, g2y, 58.0, 44.0, nhan="m₂")
        _ten(cv, g1x + 32, g1y - 14, g1x + 82, g1y - 14, cls="accent-c", rong=2.0)
        cv.text(g1x + 86, g1y - 10, "T", cls="lbl")
        cv.arrow(g1x, g1y, g1x, g1y - 58, cls="accent-c", head=8)
        cv.text(g1x + 7, g1y - 58, "N", cls="lbl")
        cv.arrow(g1x, g1y, g1x, g1y + 54, cls="accent-b", head=8)
        cv.text(g1x + 7, g1y + 54, "P₁", cls="lbl")
        _ten(cv, g2x - 34, g2y - 8, g2x - 34, g2y - 52, cls="accent-c", rong=2.0)
        cv.text(g2x - 42, g2y - 30, "T", cls="lbl", anchor="end")
        cv.arrow(g2x, g2y, g2x, g2y + 50, cls="accent-b", head=8)
        cv.text(g2x + 7, g2y + 50, "P₂", cls="lbl")
        if ma_sat:
            _ten(cv, g1x - 32, g1y, g1x - 80, g1y, cls="accent-d", rong=2.0)
            _chu(cv, g1x - 84, g1y - 5, "F", "ms", cls="lbl", anchor="end")
        return cv.render()

    w, h = 400.0, 364.0
    y_tran = 34.0
    rx, ry, rr = 200.0, 84.0, 40.0
    cv = Canvas(w, h, title="Máy Atwood - hai vật treo qua ròng rọc",
                desc="Hai vật treo hai đầu dây vắt qua ròng rọc cố định.")
    _gach_nen(cv, 106.0, 294.0, y_tran, xuong=False)
    cv.line(rx, y_tran, rx, ry - rr, cls="ink")
    cv.circle(rx, ry, rr, cls="fill-b")
    cv.circle(rx, ry, rr, cls="ink")
    cv.dot(rx, ry, r=3.0, cls="accent-b")
    _cung(cv, rx, ry, rr, 0.0, math.pi, cls="ink", rong=2.0)
    g1x, g1y = rx - rr, 186.0
    g2x, g2y = rx + rr, 252.0
    cv.line(g1x, ry, g1x, g1y - 22, cls="ink")
    cv.line(g2x, ry, g2x, g2y - 22, cls="ink")
    _hop(cv, g1x, g1y, 56.0, 44.0, nhan="m₁")
    _hop(cv, g2x, g2y, 56.0, 44.0, nhan="m₂")
    # T của mỗi vật vẽ ra phía ngoài hệ: vẽ vào giữa thì mũi tên của vật này đè
    # lên thân vật kia, vì hai nhánh dây chỉ cách nhau đúng đường kính ròng rọc
    _ten(cv, g1x - 40, g1y - 8, g1x - 40, g1y - 56, cls="accent-c", rong=2.0)
    cv.text(g1x - 48, g1y - 30, "T", cls="lbl", anchor="end")
    _ten(cv, g2x + 40, g2y - 8, g2x + 40, g2y - 56, cls="accent-c", rong=2.0)
    cv.text(g2x + 48, g2y - 30, "T", cls="lbl")
    cv.arrow(g1x, g1y, g1x, g1y + 52, cls="accent-b", head=8)
    cv.arrow(g2x, g2y, g2x, g2y + 52, cls="accent-b", head=8)
    cv.text(g1x - 8, g1y + 52, "P₁", cls="lbl", anchor="end")
    cv.text(g2x + 8, g2y + 52, "P₂", cls="lbl")
    cv.text(w - 12, h - 18, "m₁ > m₂ → m₁ đi xuống, m₂ đi lên", cls="lbl-sm", anchor="end")
    return cv.render()


# ==========================================================================
# 4. Dao động điều hoà
# ==========================================================================
def build_spring_horizontal(p: Params) -> str:
    """Con lắc lò xo nằm ngang, kèm trục li độ và lực kéo về.

    Mốc O đặt tại vị trí cân bằng chứ không tại đầu lò xo tự nhiên: mọi công
    thức dao động (x, v, a, F = −kx) đều đo từ VTCB, đặt sai mốc là sai hết.
    """
    # mặc định đặt vật ở phía nén (x < 0): khi ấy lực kéo về hướng sang phải, ra
    # khỏi lò xo, nên mũi tên không đè lên các vòng lò xo mà vẫn đúng chiều
    x_li_do = _so(p.get("x"), -0.55, -1.0, 1.0)     # theo đơn vị biên độ A
    hien_luc = _co(p.get("luc"), True)

    w, h = 440.0, 254.0
    y_san = 176.0
    gy = 150.0
    O, A = 246.0, 74.0
    cx = O + x_li_do * A
    cv = Canvas(w, h, title="Con lắc lò xo nằm ngang",
                desc="Con lắc lò xo dao động trên mặt ngang; O là vị trí cân bằng, "
                     "lực kéo về luôn hướng về O.")
    cv.line(46.0, 84.0, 46.0, y_san, cls="ink")
    _gach_nen(cv, 22.0, 46.0, y_san, xuong=True, buoc=13.0, dai=8.0)
    _gach_nen(cv, 46.0, 400.0, y_san, xuong=True, buoc=16.0, dai=8.0)
    _lo_xo(cv, 46.0, gy, cx - 28.0, gy, vong=9, bien=11.0)
    _hop(cv, cx, gy, 56.0, 46.0)

    y_truc = 216.0
    cv.arrow(O - A - 52, y_truc, O + A + 56, y_truc, cls="axis", head=7)
    cv.text(O + A + 54, y_truc - 8, "x", cls="lbl", anchor="end")
    for vt, nhan in ((O - A, "−A"), (O, "O"), (O + A, "A")):
        cv.line(vt, y_truc - 6, vt, y_truc + 6, cls="ink-thin")
        cv.text(vt, y_truc + 20, nhan, cls="lbl-sm", anchor="middle")
        cv.line(vt, y_san + 12, vt, y_truc - 8, cls="ink-thin", extra=' stroke-dasharray="3 4"')
    if abs(x_li_do) > 0.05:
        _kich_thuoc(cv, O, y_truc - 16, cx, y_truc - 16, "x", cls="accent-d", dy=-6)
    if hien_luc and abs(x_li_do) > 0.05:
        huong = -1.0 if x_li_do > 0 else 1.0
        goc_hop = cx + huong * 28
        cv.arrow(goc_hop, gy, goc_hop + huong * 58, gy, cls="accent-b", head=9)
        cv.text(goc_hop + huong * 64, gy - 8, "F", cls="lbl",
                anchor="end" if huong < 0 else "start")
        cv.text(w - 12, 34.0, "F = −kx: luôn hướng về VTCB", cls="lbl-sm", anchor="end")
    return cv.render()


def build_spring_vertical(p: Params) -> str:
    """Lò xo treo thẳng đứng: chiều dài tự nhiên, vị trí cân bằng, biên dưới.

    Ba cột cạnh nhau vì Δℓ₀ = mg/k chỉ hiện ra khi so hai trạng thái, và biên
    độ A đo từ VTCB (không phải từ đầu lò xo tự nhiên) — nguồn nhầm lẫn chính
    khi tính ℓ_max, ℓ_min và lực đàn hồi cực tiểu.
    """
    hien_A = _co(p.get("bien_do"), True)
    hien_luc = _co(p.get("luc"), False)

    L0, D, A = 106.0, 52.0, 46.0
    w = 452.0 if hien_A else 330.0
    h = 366.0
    y_tran = 42.0
    cot = [104.0, 232.0, 360.0][: 3 if hien_A else 2]
    cv = Canvas(w, h, title="Lò xo treo thẳng đứng",
                desc="So sánh lò xo tự nhiên, lò xo ở vị trí cân bằng khi treo vật "
                     "và lò xo ở biên dưới của dao động.")
    _gach_nen(cv, 56.0, w - 56.0, y_tran, xuong=False, buoc=18.0)
    muc_tn = y_tran + L0
    muc_cb = y_tran + L0 + D
    muc_bien = y_tran + L0 + D + A

    _lo_xo(cv, cot[0], y_tran, cot[0], muc_tn, vong=8, bien=12.0)
    cv.text(cot[0], h - 34, "lò xo tự nhiên", cls="lbl-sm", anchor="middle")
    _lo_xo(cv, cot[1], y_tran, cot[1], muc_cb, vong=8, bien=12.0)
    _hop(cv, cot[1], muc_cb + 22, 54.0, 44.0)
    cv.text(cot[1], h - 34, "vị trí cân bằng", cls="lbl-sm", anchor="middle")
    if hien_A:
        _lo_xo(cv, cot[2], y_tran, cot[2], muc_bien, vong=8, bien=12.0)
        _hop(cv, cot[2], muc_bien + 22, 54.0, 44.0)
        cv.text(cot[2], h - 34, "biên dưới", cls="lbl-sm", anchor="middle")

    for muc, tu, den in ((muc_tn, cot[0], w - 66), (muc_cb, cot[1] - 40, w - 66),
                         (muc_bien, cot[2] - 40 if hien_A else 0, w - 66)):
        if muc == muc_bien and not hien_A:
            continue
        cv.line(tu, muc, den, muc, cls="ink-thin", extra=' stroke-dasharray="4 4"')
    _kich_thuoc(cv, 68.0, y_tran, 68.0, muc_tn, "", cls="accent-d")
    cv.text(60.0, (y_tran + muc_tn) / 2 + 4, "ℓ₀", cls="lbl", anchor="end")
    _kich_thuoc(cv, w - 54, muc_tn, w - 54, muc_cb, "", cls="accent-d")
    cv.text(w - 46, (muc_tn + muc_cb) / 2 + 4, "Δℓ₀", cls="lbl")
    if hien_A:
        _kich_thuoc(cv, w - 54, muc_cb, w - 54, muc_bien, "", cls="accent-b")
        cv.text(w - 46, (muc_cb + muc_bien) / 2 + 4, "A", cls="lbl")
    if hien_luc:
        gy = muc_cb + 22
        cv.arrow(cot[1], gy, cot[1], gy + 56, cls="accent-b", head=8)
        cv.text(cot[1] + 7, gy + 56, "P", cls="lbl")
        # gốc mũi tên F_đh vẫn nằm trên thân vật (lệch 18px để không đè lò xo):
        # vẽ rời hẳn sang bên thì trông như một lực tác dụng vào chỗ khác
        cv.arrow(cot[1] - 18, gy, cot[1] - 18, gy - 58, cls="accent-c", head=8)
        _chu(cv, cot[1] - 25, gy - 56, "F", "đh", cls="lbl", anchor="end")
    return cv.render()


def build_simple_pendulum(p: Params) -> str:
    """Con lắc đơn: dây ℓ, li độ góc α, li độ cong s = αℓ, phân tích trọng lực.

    Thành phần tiếp tuyến P sin α mới là lực kéo về; thành phần P cos α cân
    bằng với lực căng. Vẽ tách hai thành phần là cách duy nhất để thấy vì sao
    chu kì con lắc đơn không phụ thuộc khối lượng.
    """
    alpha = _so(p.get("alpha"), 34.0, 8.0, 60.0)
    hien_luc = _co(p.get("luc"), True)
    hien_cao = _co(p.get("do_cao"), False)
    hien_cang = _co(p.get("cang"), False)
    th = math.radians(alpha)

    L = 176.0
    w, h = 420.0, 310.0
    ox, oy = 158.0, 46.0
    bx, by = ox + L * math.sin(th), oy + L * math.cos(th)
    vx, vy = ox, oy + L
    cv = Canvas(w, h, title="Con lắc đơn",
                desc="Con lắc đơn lệch góc alpha: trọng lực phân tích thành thành phần "
                     "tiếp tuyến (lực kéo về) và thành phần dọc dây.")
    _gach_nen(cv, ox - 62, ox + 62, oy, xuong=False, buoc=15.0)
    cv.line(ox, oy, vx, vy + 12, cls="ink-thin", extra=' stroke-dasharray="5 5"')
    cv.line(ox, oy, bx, by, cls="ink")
    cv.text((ox + bx) / 2 - 12, (oy + by) / 2, "ℓ", cls="lbl", anchor="end")
    _cung(cv, ox, oy, 44.0, -math.pi / 2, th - math.pi / 2, cls="accent-d", rong=1.8)
    cv.text(ox + 54 * math.sin(th / 2) + 4, oy + 54 * math.cos(th / 2) + 4, "α", cls="lbl")
    _cung(cv, ox, oy, L, -math.pi / 2, th - math.pi / 2, cls="accent-c", rong=2.0)
    cv.text(ox + (L + 26) * math.sin(th / 2), oy + (L + 26) * math.cos(th / 2) + 4,
            "s = αℓ", cls="lbl-sm", anchor="middle")
    cv.dot(vx, vy, r=3.2, cls="accent-c")
    cv.circle(bx, by, 13.0, cls="fill-a")
    cv.circle(bx, by, 13.0, cls="ink")

    if hien_luc:
        LP = 62.0
        Px, Py = bx, by + LP
        cv.arrow(bx, by, Px, Py, cls="accent-b", head=9)
        cv.text(Px + 7, Py + 2, "P", cls="lbl")
        tx, ty = -math.cos(th), math.sin(th)          # tiếp tuyến, hướng về VTCB
        sx, sy = math.sin(th), math.cos(th)           # dọc dây, ra xa điểm treo
        T1 = (bx + tx * LP * math.sin(th), by + ty * LP * math.sin(th))
        T2 = (bx + sx * LP * math.cos(th), by + sy * LP * math.cos(th))
        cv.arrow(bx, by, T1[0], T1[1], cls="accent-d", head=8)
        cv.arrow(bx, by, T2[0], T2[1], cls="accent-d", head=8)
        for T in (T1, T2):
            cv.line(T[0], T[1], Px, Py, cls="ink-thin", extra=' stroke-dasharray="4 4"')
        cv.text(T1[0] - 8, T1[1] - 8, "P sin α", cls="lbl-sm", anchor="end")
        cv.text(T2[0] + 8, T2[1] + 12, "P cos α", cls="lbl-sm")
    if hien_cang:
        cv.arrow(bx, by, bx - math.sin(th) * 62, by - math.cos(th) * 62, cls="accent-c", head=8)
        cv.text(bx - math.sin(th) * 62 + 8, by - math.cos(th) * 62 + 4, "τ", cls="lbl")
    if hien_cao:
        xm = 54.0
        for yy, xa in ((by, bx), (vy, vx)):
            cv.line(xm, yy, xa, yy, cls="ink-thin", extra=' stroke-dasharray="4 4"')
        _kich_thuoc(cv, xm, by, xm, vy, "", cls="accent-b")
        cv.text(xm + 8, (by + vy) / 2 + 4, "h", cls="lbl")
        cv.text(w - 10, h - 12, "h = ℓ(1 − cos α)", cls="lbl-sm", anchor="end")
    return cv.render()


def build_shm_xt(p: Params) -> str:
    """Đồ thị li độ - thời gian của dao động điều hoà, đánh dấu A và T."""
    A = _so(p.get("A"), 4.0, 0.5, 20.0)
    T = _so(p.get("T"), 2.0, 0.4, 10.0)
    phi = _so(p.get("phi"), 0.0, -360.0, 360.0)
    ghi_chu = str(p.get("note", ""))

    w, h = 440.0, 280.0
    box = (66.0, 30.0, w - 96, h - 84)
    tmax = 2.0 * T
    ph = math.radians(phi)
    mau = [(t, A * math.cos(2 * math.pi * t / T + ph)) for t in _chia(0.0, tmax, 160)]
    cv = Canvas(w, h, title="Đồ thị li độ - thời gian",
                desc="Đồ thị x = A·cos(ωt + φ) trong hai chu kì, có đánh dấu biên độ và chu kì.")
    k = _Khung(cv, 0.0, tmax * 1.03, -A * 1.42, A * 1.42, box)
    k.truc("t (s)", "x (cm)")
    for muc, nhan in ((A, "A"), (-A, "−A")):
        cv.line(box[0], k.sy(muc), box[0] + box[2], k.sy(muc),
                cls="accent-d", extra=' stroke-dasharray="5 4" stroke-width="1.2"')
        cv.text(box[0] + box[2] + 6, k.sy(muc) + 4, nhan, cls="lbl")
    k.duong(mau, cls="curve")
    t1 = (-ph / (2 * math.pi)) * T
    while t1 < 0:
        t1 += T
    t2 = t1 + T
    if t2 <= tmax:
        yT = k.sy(A) - 14
        _kich_thuoc(cv, k.sx(t1), yT, k.sx(t2), yT, "T", cls="accent-b", dy=-6)
        for tt in (t1, t2):
            cv.line(k.sx(tt), yT, k.sx(tt), k.sy(A), cls="ink-thin",
                    extra=' stroke-dasharray="3 3"')
    if ghi_chu:
        cv.text(w - 12, h - 16, ghi_chu, cls="lbl-sm", anchor="end")
    return cv.render()


def build_shm_trio(p: Params) -> str:
    """Ba đồ thị x(t), v(t), a(t) dóng cùng trục thời gian.

    Đường dóng dọc ở các mốc T/4 làm lộ ra quan hệ pha: v sớm pha π/2 so với x
    (v cực đại đúng lúc x = 0), a ngược pha với x (a = −ω²x).
    """
    A = _so(p.get("A"), 4.0, 0.5, 20.0)
    T = _so(p.get("T"), 2.0, 0.4, 10.0)
    omega = 2 * math.pi / T

    w, h = 440.0, 452.0
    # chừa lề phải rộng hơn bề rộng chữ "−ω²A" — nhãn dài nhất trong ba khung
    pw = w - 132
    tmax = 1.5 * T
    cv = Canvas(w, h, title="Li độ, vận tốc, gia tốc theo thời gian",
                desc="Ba đồ thị x, v, a của cùng một dao động điều hoà, "
                     "cho thấy vận tốc sớm pha π/2 so với li độ và gia tốc ngược pha với li độ.")
    bien_do = (A, omega * A, omega * omega * A)
    ham = (
        lambda t: A * math.cos(omega * t),
        lambda t: -omega * A * math.sin(omega * t),
        lambda t: -omega * omega * A * math.cos(omega * t),
    )
    nhan = ("x (cm)", "v (cm/s)", "a (cm/s²)")
    dinh = ("A", "ωA", "ω²A")
    for i in range(3):
        box = (72.0, 30.0 + i * 140.0, pw, 100.0)
        bd = bien_do[i]
        k = _Khung(cv, 0.0, tmax * 1.03, -bd * 1.35, bd * 1.35, box)
        k.truc("t (s)" if i == 2 else "t", nhan[i], so_x=(i == 2), so_y=False)
        for j in range(0, 7):
            tt = j * T / 4
            if tt > tmax:
                break
            cv.line(k.sx(tt), box[1], k.sx(tt), box[1] + box[3],
                    cls="ink-thin", extra=' stroke-dasharray="3 4"')
        k.duong([(t, ham[i](t)) for t in _chia(0.0, tmax, 150)], cls="curve")
        cv.text(box[0] + box[2] + 6, k.sy(bd) + 4, dinh[i], cls="lbl")
        cv.text(box[0] + box[2] + 6, k.sy(-bd) + 4, "−" + dinh[i], cls="lbl")
    cv.text(w - 12, 24.0, "v sớm pha π/2 so với x · a ngược pha với x",
            cls="lbl-sm", anchor="end")
    return cv.render()


def build_shm_phase_ellipse(p: Params) -> str:
    """Hệ thức độc lập thời gian, vẽ dưới dạng elip trong mặt phẳng pha.

    Khử t giữa hai phương trình dao động thì còn lại một elip: mọi trạng thái
    của vật đều nằm trên đúng đường này, nên biết một đại lượng là suy ra đại
    lượng kia mà không cần biết thời điểm.
    """
    A = _so(p.get("A"), 4.0, 0.5, 20.0)
    T = _so(p.get("T"), 2.0, 0.4, 10.0)
    che_do = str(p.get("mode", "x-v"))
    omega = 2 * math.pi / T

    if che_do == "v-a":
        ax, ay = omega * A, omega * omega * A
        nhan_x, nhan_y = "v (cm/s)", "a (cm/s²)"
        dinh_x, dinh_y = "ωA", "ω²A"
        tieu_de = "Hệ thức độc lập giữa v và a"
    else:
        ax, ay = A, omega * A
        nhan_x, nhan_y = "x (cm)", "v (cm/s)"
        dinh_x, dinh_y = "A", "ωA"
        tieu_de = "Hệ thức độc lập giữa x và v"

    w, h = 360.0, 330.0
    box = (56.0, 26.0, w - 92, h - 74)
    cv = Canvas(w, h, title=tieu_de,
                desc="Quỹ đạo pha của dao động điều hoà là một elip; "
                     "mọi trạng thái của vật đều nằm trên đường này.")
    k = _Khung(cv, -ax * 1.35, ax * 1.35, -ay * 1.35, ay * 1.35, box)
    k.truc(nhan_x, nhan_y, so_x=False, so_y=False)
    mau = [(ax * math.cos(t), ay * math.sin(t)) for t in _chia(0.0, 2 * math.pi, 180)]
    cv.polyline([(k.sx(x), k.sy(y)) for x, y in mau], cls="curve")
    for vt, nh, ngang in ((ax, dinh_x, True), (-ax, "−" + dinh_x, True),
                          (ay, dinh_y, False), (-ay, "−" + dinh_y, False)):
        if ngang:
            # nhãn nửa trục ngang đặt phía TRÊN trục, phía dưới đã dành cho tên trục
            cv.dot(k.sx(vt), k.sy(0), r=3.4, cls="accent-b")
            cv.text(k.sx(vt) - (6 if vt > 0 else -6), k.sy(0) - 10, nh, cls="lbl",
                    anchor="end" if vt > 0 else "start")
        else:
            cv.dot(k.sx(0), k.sy(vt), r=3.4, cls="accent-b")
            cv.text(k.sx(0) + 8, k.sy(vt) + 4, nh, cls="lbl")
    tm = math.radians(38.0)
    mx, my = ax * math.cos(tm), ay * math.sin(tm)
    cv.dot(k.sx(mx), k.sy(my), r=4.2, cls="accent-a")
    cv.line(k.sx(mx), k.sy(my), k.sx(mx), k.sy(0), cls="ink-thin", extra=' stroke-dasharray="4 4"')
    cv.line(k.sx(mx), k.sy(my), k.sx(0), k.sy(my), cls="ink-thin", extra=' stroke-dasharray="4 4"')
    cv.text(k.sx(mx) + 8, k.sy(my) - 6, "M", cls="lbl")
    return cv.render()


def build_phasor_circle(p: Params) -> str:
    """Vòng tròn pha: quãng đường lớn nhất và nhỏ nhất trong cùng một Δt.

    Dao động điều hoà là hình chiếu của chuyển động tròn đều, nên trong thời
    gian Δt vật quét đúng một cung Δφ = ωΔt. Cung ấy đặt đối xứng qua VTCB thì
    hình chiếu dài nhất (vật đi nhanh nhất quanh VTCB), đặt đối xứng qua biên
    thì ngắn nhất.
    """
    A = _so(p.get("A"), 1.0, 0.2, 10.0)
    dphi = _so(p.get("dphi"), 100.0, 20.0, 170.0)
    nua = math.radians(dphi) / 2

    R = 84.0
    w, h = 520.0, 316.0
    cv = Canvas(w, h, title="Vòng tròn pha - quãng đường lớn nhất, nhỏ nhất",
                desc="Liên hệ dao động điều hoà với chuyển động tròn đều: "
                     "cùng một góc quét cho quãng đường lớn nhất khi đối xứng qua vị trí "
                     "cân bằng và nhỏ nhất khi đối xứng qua biên.")
    for cot, doi_xung_vtcb in ((144.0, True), (376.0, False)):
        cy = 132.0
        cv.circle(cot, cy, R, cls="ink-thin", extra=' stroke-dasharray="5 5"')
        cv.arrow(cot - R - 24, cy, cot + R + 26, cy, cls="axis", head=7)
        cv.text(cot + R + 24, cy - 8, "x", cls="lbl", anchor="end")
        cv.dot(cot, cy, r=2.8, cls="accent-b")
        cv.text(cot - 8, cy + 16, "O", cls="lbl-sm", anchor="end")
        goc_giua = math.pi / 2 if doi_xung_vtcb else 0.0
        a1, a2 = goc_giua - nua, goc_giua + nua
        _cung(cv, cot, cy, R, a1, a2, cls="accent-b", rong=2.8)
        for g in (a1, a2):
            mx, my = cot + R * math.cos(g), cy - R * math.sin(g)
            cv.dot(mx, my, r=4.0, cls="accent-a")
            cv.line(mx, my, mx, cy, cls="ink-thin", extra=' stroke-dasharray="4 4"')
        # hình chiếu của hai đầu cung: khi cung đối xứng qua biên thì hai đầu
        # chiếu trùng nhau, đoạn vật quét là từ đó ra tận biên rồi quay về — nên
        # phải lấy tới điểm biên x = A, không phải khoảng cách giữa hai hình chiếu
        if doi_xung_vtcb:
            x1, x2 = cot + R * math.cos(a1), cot + R * math.cos(a2)
        else:
            x1, x2 = cot + R * math.cos(nua), cot + R
        cv.line(min(x1, x2), cy, max(x1, x2), cy, cls="accent-c", extra=' stroke-width="4"')
        _kich_thuoc(cv, min(x1, x2), cy + 32, max(x1, x2), cy + 32, "", cls="accent-c")
        _cung(cv, cot, cy, 32.0, a1, a2, cls="accent-d", rong=1.8)
        if doi_xung_vtcb:
            cv.text(cot, cy - 52, "Δφ = ωΔt", cls="lbl-sm", anchor="middle")
            cv.text(cot, cy + R + 42, "S", cls="lbl", anchor="middle")
            _chu(cv, cot + 6, cy + R + 42, "", "max", cls="lbl")
            cv.text(cot, cy + R + 62, "= 2A·sin(ωΔt/2)", cls="lbl-sm", anchor="middle")
            cv.text(cot, h - 12, "cung đối xứng qua vị trí cân bằng",
                    cls="lbl-sm", anchor="middle")
        else:
            cv.text(cot - 12, cy - 44, "Δφ = ωΔt", cls="lbl-sm", anchor="end")
            cv.text(cot, cy + R + 42, "S", cls="lbl", anchor="middle")
            _chu(cv, cot + 6, cy + R + 42, "", "min", cls="lbl")
            cv.text(cot, cy + R + 62, "= 2A(1 − cos(ωΔt/2))", cls="lbl-sm", anchor="middle")
            cv.text(cot, h - 12, "cung đối xứng qua biên: đi ra rồi về",
                    cls="lbl-sm", anchor="middle")
    return cv.render()


def build_shm_energy(p: Params) -> str:
    """Động năng và thế năng theo li độ: hai parabol, tổng luôn là hằng số.

    Vẽ theo li độ chứ không theo thời gian vì đó là dạng cho thấy ngay W = W_đ +
    W_t = ½kA² không đổi, và giao điểm hai parabol là vị trí W_đ = W_t.
    """
    A = _so(p.get("A"), 4.0, 0.5, 20.0)
    n = p.get("n")
    n_val = _so(n, 1.0, 0.05, 20.0) if n is not None else None

    w, h = 430.0, 300.0
    box = (66.0, 34.0, w - 108, h - 84)
    W = 1.0
    cv = Canvas(w, h, title="Động năng và thế năng theo li độ",
                desc="Thế năng là parabol lõm lên, động năng là parabol lõm xuống; "
                     "tổng của chúng là cơ năng không đổi.")
    k = _Khung(cv, -A * 1.36, A * 1.36, 0.0, W * 1.3, box)
    k.truc("x (cm)", "W", so_x=False, so_y=False, buoc_y=W)
    dai_x = _chia(-A, A, 90)
    k.duong([(x, W * (x / A) ** 2) for x in dai_x], cls="curve")
    cv.polyline([(k.sx(x), k.sy(W * (1 - (x / A) ** 2))) for x in dai_x],
                cls="curve", extra=' stroke-dasharray="7 4"')
    cv.line(k.sx(-A * 1.30), k.sy(W), k.sx(A * 1.30), k.sy(W),
            cls="accent-b", extra=' stroke-width="2"')
    cv.text(box[0] + box[2] + 4, k.sy(W) - 8, "W = ½kA²", cls="lbl-sm", anchor="end")
    _chu(cv, k.sx(A * 0.86), k.sy(W * 0.62), "W", "t", cls="lbl", anchor="end")
    _chu(cv, k.sx(-A * 0.30), k.sy(W * 0.90), "W", "đ", cls="lbl", anchor="end")
    for vt, nhan in ((-A, "−A"), (A, "A")):
        cv.line(k.sx(vt), k.sy(0), k.sx(vt), k.sy(W), cls="ink-thin",
                extra=' stroke-dasharray="4 4"')
        cv.text(k.sx(vt), k.sy(0) + 17, nhan, cls="lbl-sm", anchor="middle")
    if n_val is not None:
        xg = A / math.sqrt(n_val + 1.0)
        for dau in (-1.0, 1.0):
            cv.dot(k.sx(dau * xg), k.sy(W / (n_val + 1.0)), r=4.0, cls="accent-c")
            cv.line(k.sx(dau * xg), k.sy(0), k.sx(dau * xg), k.sy(W / (n_val + 1.0)),
                    cls="accent-c", extra=' stroke-dasharray="4 4" stroke-width="1.4"')
        # ghi thành câu ở góc trống phía trên bên trái: đặt cạnh giao điểm thì
        # đụng ngay nhãn W_t và nhãn ±A vốn đã chiếm hết chỗ quanh đó
        duoi = " tại x = ±A/√2" if abs(n_val - 1.0) < 1e-9 else " tại x = ±A/√(n+1)"
        giua = " = W" if abs(n_val - 1.0) < 1e-9 else " = n·W"
        _chu_nhieu(cv, box[0] + 2, box[1] + 14,
                   [("W", "đ"), (giua, "t"), (duoi, "")])
    return cv.render()


# ==========================================================================
# 5. Sóng cơ
# ==========================================================================
def build_wave_snapshot(p: Params) -> str:
    """Ảnh chụp sóng ngang tại một thời điểm: bước sóng λ và biên độ A.

    λ đo giữa **hai đỉnh liên tiếp** — không phải giữa đỉnh và hõm — nên đường
    kích thước được đặt đúng vào hai đỉnh thay vì ghi chữ suông.
    """
    A = _so(p.get("A"), 1.0, 0.2, 10.0)
    so_buoc = _so(p.get("cycles"), 2.5, 1.0, 5.0)
    hai_diem = _co(p.get("two_points"), False)
    d = _so(p.get("d"), 0.75, 0.05, 2.0)          # khoảng cách MN theo đơn vị λ

    w, h = 460.0, 268.0
    box = (58.0, 52.0, w - 92, h - 118)
    cv = Canvas(w, h, title="Sóng ngang tại một thời điểm",
                desc="Hình dạng sợi dây khi có sóng ngang truyền qua, "
                     "đánh dấu bước sóng và biên độ.")
    k = _Khung(cv, 0.0, so_buoc, -A * 1.5, A * 1.5, box)
    yx = k.sy(0)
    cv.arrow(box[0] - 10, yx, box[0] + box[2] + 12, yx, cls="axis", head=7)
    cv.text(box[0] + box[2] + 10, yx + 18, "x", cls="lbl", anchor="end")
    cv.arrow(box[0], box[1] + box[3], box[0], box[1] - 6, cls="axis", head=7)
    cv.text(box[0] - 8, box[1] - 8, "u", cls="lbl", anchor="end")
    k.duong([(x, A * math.cos(2 * math.pi * x)) for x in _chia(0.0, so_buoc, 220)], cls="curve")

    y_dinh = k.sy(A)
    _kich_thuoc(cv, k.sx(0.0), y_dinh - 18, k.sx(1.0), y_dinh - 18, "λ", cls="accent-d", dy=-6)
    for xx in (0.0, 1.0):
        cv.line(k.sx(xx), y_dinh - 18, k.sx(xx), y_dinh, cls="ink-thin",
                extra=' stroke-dasharray="3 3"')
    _kich_thuoc(cv, k.sx(2.0), yx, k.sx(2.0), k.sy(A), "", cls="accent-b")
    cv.text(k.sx(2.0) + 8, (yx + k.sy(A)) / 2 + 4, "A", cls="lbl")
    _ten(cv, box[0] + box[2] - 66, box[1] - 22, box[0] + box[2] + 4, box[1] - 22,
         cls="accent-c", rong=2.0, dai=8.0)
    cv.text(box[0] + box[2] - 70, box[1] - 18, "v", cls="lbl", anchor="end")

    if hai_diem:
        x1 = 0.35
        x2 = min(x1 + d, so_buoc - 0.05)
        for xx, nh in ((x1, "M"), (x2, "N")):
            cv.dot(k.sx(xx), k.sy(A * math.cos(2 * math.pi * xx)), r=4.4, cls="accent-a")
            cv.text(k.sx(xx), k.sy(A * math.cos(2 * math.pi * xx)) - 10, nh,
                    cls="lbl", anchor="middle")
        y_d = box[1] + box[3] + 26
        _kich_thuoc(cv, k.sx(x1), y_d, k.sx(x2), y_d, "d", cls="accent-b", dy=16)
        cv.text(w - 12, h - 14, "Δφ = 2πd / λ", cls="lbl-sm", anchor="end")
    return cv.render()


def build_standing_wave(p: Params) -> str:
    """Sóng dừng trên dây: nút, bụng, và điều kiện về chiều dài dây.

    Vẽ cả hai đường bao (±2A) chứ không vẽ một đường sin: sóng dừng không chạy,
    mỗi điểm chỉ dao động trong khoảng giữa hai đường bao ấy — đó là lí do có
    những điểm đứng yên hẳn.
    """
    k_bo = _nguyen(p.get("k"), 3, 1, 6)
    dau_tu_do = _co(p.get("free_end"), False)
    so_hoa_am = _nguyen(p.get("modes"), 1, 1, 3)
    danh_dau = _co(p.get("mark"), True)

    trai, rong = 62.0, 316.0
    cao_bo = 108.0
    w = 448.0
    # chừa thêm hai hàng dưới cùng cho đường kích thước λ/2 và λ/4
    h = 46.0 + so_hoa_am * (cao_bo + 34.0) + (72.0 if danh_dau and so_hoa_am == 1 else 26.0)
    cv = Canvas(w, h,
                title="Sóng dừng trên dây một đầu tự do" if dau_tu_do else "Sóng dừng trên dây hai đầu cố định",
                desc="Hình dạng sợi dây khi có sóng dừng: các nút đứng yên, "
                     "các bụng dao động với biên độ cực đại.")
    for m in range(so_hoa_am):
        n = k_bo if so_hoa_am == 1 else m + 1
        truc_y = 46.0 + m * (cao_bo + 34.0) + cao_bo / 2
        bien = cao_bo / 2 - 8
        he_so = (2 * n - 1) / 2.0 if dau_tu_do else float(n)
        cv.line(trai - 14, truc_y, trai + rong + 14, truc_y, cls="ink-thin",
                extra=' stroke-dasharray="4 4"')
        for dau in (1.0, -1.0):
            pts = []
            for i in range(0, 161):
                x = rong * i / 160.0
                u = dau * bien * math.sin(he_so * math.pi * x / rong)
                pts.append((trai + x, truc_y - u))
            cv.polyline(pts, cls="curve" if dau > 0 else "ink-thin",
                        extra="" if dau > 0 else ' stroke-dasharray="6 4"')
        # nút: sin(he_so·πx/ℓ) = 0 → x = j·ℓ/he_so (cách nhau λ/2)
        # bụng: |sin| = 1 → x = (2j+1)·ℓ/(2·he_so) (cách nút gần nhất λ/4)
        j = 0
        while j * rong / he_so <= rong + 1e-6:
            xn = j * rong / he_so
            cv.dot(trai + xn, truc_y, r=4.0, cls="accent-b")
            if so_hoa_am == 1 and j == 1:
                cv.text(trai + xn, truc_y + 20, "nút", cls="lbl-sm", anchor="middle")
            j += 1
        j = 0
        while (2 * j + 1) * rong / (2 * he_so) <= rong + 1e-6:
            xb = (2 * j + 1) * rong / (2 * he_so)
            u = bien * math.sin(he_so * math.pi * xb / rong)
            cv.dot(trai + xb, truc_y - u, r=3.6, cls="accent-c")
            if so_hoa_am == 1 and j == 0:
                cv.text(trai + xb, truc_y - u - 10, "bụng", cls="lbl-sm", anchor="middle")
            j += 1
        cv.line(trai, truc_y - bien - 12, trai, truc_y + bien + 12, cls="ink")
        if not dau_tu_do:
            cv.line(trai + rong, truc_y - bien - 12, trai + rong, truc_y + bien + 12, cls="ink")
        else:
            # đầu tự do = vòng trượt trên thanh dẫn: vòng phải nằm ĐÚNG trên
            # đầu dây (một bụng sóng), đặt nó lên trục thì hoá ra thành nút
            u_cuoi = bien * math.sin(he_so * math.pi)
            cv.line(trai + rong, truc_y - bien - 12, trai + rong, truc_y + bien + 12,
                    cls="ink-thin", extra=' stroke-dasharray="4 4"')
            cv.circle(trai + rong, truc_y - u_cuoi, 5.5, cls="fill-b")
            cv.circle(trai + rong, truc_y - u_cuoi, 5.5, cls="ink")
        if so_hoa_am > 1:
            cv.text(w - 12, truc_y - cao_bo / 2 + 12, f"hoạ âm bậc {n}", cls="lbl-sm", anchor="end")

    if danh_dau and so_hoa_am == 1:
        he_so = (2 * k_bo - 1) / 2.0 if dau_tu_do else float(k_bo)
        truc_y = 46.0 + cao_bo / 2
        y_kt = truc_y + cao_bo / 2 + 4
        # cả hai đường kích thước đều đo từ đầu dây: đo từ nút thứ hai thì với
        # k = 1 đoạn λ/4 chạy quá mép phải và bị cắt mất
        _kich_thuoc(cv, trai, y_kt, trai + rong / he_so, y_kt, "λ/2 (nút - nút)",
                    cls="accent-d", dy=16)
        _kich_thuoc(cv, trai, y_kt + 26, trai + rong / (2 * he_so), y_kt + 26,
                    "λ/4 (nút - bụng)", cls="accent-b", dy=16)
    if so_hoa_am > 1:
        chu = "hoạ âm bậc n: ℓ = n·λ/2  →  f_n = n·v/(2ℓ)"
    else:
        chu = "ℓ = (2k+1)·λ/4" if dau_tu_do else "ℓ = k·λ/2"
    cv.text(12.0, h - 10.0, chu, cls="lbl-sm")
    return cv.render()


def build_two_source_interference(p: Params) -> str:
    """Giao thoa hai nguồn cùng pha: vòng sóng, đường cực đại, đường cực tiểu.

    Các vòng tròn là đỉnh sóng phát ra từ mỗi nguồn; **giao điểm của hai đỉnh**
    chính là điểm cực đại, và nối chúng lại được các nhánh hypebol d₂ − d₁ = kλ.
    Vẽ vòng sóng trước rồi mới vẽ hypebol là để thấy đường ấy từ đâu mà ra, chứ
    không phải một công thức từ trên trời rơi xuống.
    """
    lam = 1.0
    khoang = _so(p.get("d"), 4.0, 2.0, 6.0)          # khoảng cách hai nguồn, theo λ
    hien = str(p.get("show", "cuc-dai"))
    kmax = _nguyen(p.get("kmax"), 2, 1, 3)
    danh_dau_M = _co(p.get("mark_M"), True)
    do_khoang = _co(p.get("khoang_cach"), False)

    w, h = 470.0, 348.0
    box = (34.0, 26.0, w - 68, h - 76)
    cx, cy = box[0] + box[2] / 2, box[1] + box[3] / 2
    don_vi = min(box[2] / (khoang + 3.4), box[3] / 4.6)
    c = khoang / 2 * don_vi
    S1 = (cx - c, cy)
    S2 = (cx + c, cy)
    cv = Canvas(w, h, title="Giao thoa sóng của hai nguồn cùng pha",
                desc="Hai nguồn cùng pha tạo các đường cực đại và cực tiểu giao thoa; "
                     "giao điểm của hai đỉnh sóng là điểm cực đại.")
    # chỉ vẽ 5 vòng mỗi nguồn: đủ để thấy các giao điểm sinh ra đường cực đại,
    # thêm nữa thì lưới vòng sóng nuốt mất chính các đường ấy
    for n in range(1, 6):
        for S in (S1, S2):
            vong = [(S[0] + n * lam * don_vi * math.cos(t),
                     S[1] + n * lam * don_vi * math.sin(t))
                    for t in _chia(0.0, 2 * math.pi, 240)]
            _trong_khung(cv, vong, box, cls="ink-thin", rong=0.9)
    cv.line(box[0], cy, box[0] + box[2], cy, cls="ink-thin", extra=' stroke-dasharray="5 4"')

    def nhanh(a_lam: float, cls: str, rong: float, nhan: str) -> None:
        """Nhánh hypebol |d₂ − d₁| = a_lam·λ; đỉnh nằm ở x = −a_lam·λ/2."""
        a = abs(a_lam) * lam / 2 * don_vi
        if a >= c - 1e-6:
            return
        b = math.sqrt(max(c * c - a * a, 1e-9))
        dau = -1.0 if a_lam > 0 else 1.0
        pts = []
        for t in _chia(-2.0, 2.0, 160):
            pts.append((cx + dau * a * math.cosh(t), cy - b * math.sinh(t)))
        _trong_khung(cv, pts, box, cls=cls, rong=rong)
        trong = [q for q in pts if box[0] <= q[0] <= box[0] + box[2]
                 and box[1] <= q[1] <= box[1] + box[3]]
        if trong and nhan:
            dinh = min(trong, key=lambda q: q[1])
            cv.text(dinh[0], dinh[1] - 5, nhan, cls="lbl-sm", anchor="middle")

    if hien in ("cuc-dai", "ca-hai"):
        cv.line(cx, box[1], cx, box[1] + box[3], cls="accent-a", extra=' stroke-width="2.4"')
        cv.text(cx, box[1] - 6, "k = 0", cls="lbl-sm", anchor="middle")
        for kk in range(1, kmax + 1):
            nhanh(float(kk), "accent-a", 2.4, f"k = {kk}")
            nhanh(float(-kk), "accent-a", 2.4, f"k = −{kk}")
        # giao điểm của mỗi đường cực đại với đoạn S₁S₂: đếm được ngay số cực
        # đại trên đoạn ấy, và thấy chúng cách đều nhau λ/2
        for kk in range(-kmax, kmax + 1):
            xk = cx - kk * lam / 2 * don_vi
            if abs(xk - cx) < c - 1e-6:
                cv.dot(xk, cy, r=3.4, cls="accent-a")
        if do_khoang:
            _kich_thuoc(cv, cx, cy + 24, cx - lam / 2 * don_vi, cy + 24, "λ/2",
                        cls="accent-d", dy=16)
    if hien in ("cuc-tieu", "ca-hai"):
        for kk in range(0, kmax + 1):
            # nhánh âm ứng với d₂ − d₁ = −(kk+½)λ = (k+½)λ với k = −(kk+1)
            nhanh(kk + 0.5, "accent-b", 2.0, "" if hien == "ca-hai" else f"k = {kk}")
            nhanh(-(kk + 0.5), "accent-b", 2.0,
                  "" if hien == "ca-hai" else f"k = −{kk + 1}")

    for S, nh in ((S1, "S₁"), (S2, "S₂")):
        cv.circle(S[0], S[1], 6.0, cls="fill-b")
        cv.circle(S[0], S[1], 6.0, cls="ink")
        cv.text(S[0], S[1] + 22, nh, cls="lbl", anchor="middle")
    if danh_dau_M:
        # đặt M vào khoảng GIỮA hai đường cực đại: nằm đúng trên một đường thì
        # người học dễ tưởng d₁, d₂ chỉ có nghĩa ở điểm cực đại
        M = (cx + 1.0 * don_vi, cy - 1.7 * don_vi)
        M = (min(max(M[0], box[0] + 12), box[0] + box[2] - 12),
             min(max(M[1], box[1] + 12), box[1] + box[3] - 12))
        for S, nh in ((S1, "d₁"), (S2, "d₂")):
            cv.line(S[0], S[1], M[0], M[1], cls="accent-c",
                    extra=' stroke-dasharray="6 4" stroke-width="1.6"')
            cv.text((S[0] + M[0]) / 2, (S[1] + M[1]) / 2 - 5, nh, cls="lbl-sm", anchor="middle")
        cv.dot(M[0], M[1], r=4.4, cls="accent-c")
        cv.text(M[0] + 8, M[1] - 6, "M", cls="lbl")
    chu = {"cuc-tieu": "cực tiểu: d₂ − d₁ = (k + ½)λ",
           "ca-hai": "cực đại: d₂ − d₁ = kλ · cực tiểu: (k + ½)λ"}.get(
        hien, "cực đại: d₂ − d₁ = kλ")
    cv.text(12.0, h - 30.0, chu, cls="lbl-sm")
    cv.text(12.0, h - 12.0, "vòng mảnh là đỉnh sóng; hai đỉnh gặp nhau thì đó là điểm cực đại",
            cls="lbl-sm")
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "motion_xt": build_motion_xt,
    "motion_vt": build_motion_vt,
    "motion_trio": build_motion_trio,
    "free_fall": build_free_fall,
    "horizontal_throw": build_horizontal_throw,
    "circular_motion": build_circular_motion,
    "fbd_horizontal": build_fbd_horizontal,
    "fbd_incline": build_fbd_incline,
    "fbd_hanging": build_fbd_hanging,
    "connected_bodies": build_connected_bodies,
    "spring_horizontal": build_spring_horizontal,
    "spring_vertical": build_spring_vertical,
    "simple_pendulum": build_simple_pendulum,
    "shm_xt": build_shm_xt,
    "shm_trio": build_shm_trio,
    "shm_phase_ellipse": build_shm_phase_ellipse,
    "phasor_circle": build_phasor_circle,
    "shm_energy": build_shm_energy,
    "wave_snapshot": build_wave_snapshot,
    "standing_wave": build_standing_wave,
    "two_source_interference": build_two_source_interference,
}
