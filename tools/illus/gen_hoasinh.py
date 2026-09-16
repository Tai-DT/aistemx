"""Generator SVG cho họ hình Hoá học - Sinh học.

Cùng quy ước với ``generators2d``: mỗi hàm ``build_<tên>(p) -> str`` nhận dict tham
số (mọi khoá đều có mặc định, gọi ``build_x({})`` phải chạy được) và trả về chuỗi
SVG hoàn chỉnh, tất định, không tham chiếu tài nguyên ngoài.

Vài hình ở đây (đường chuẩn độ, động học, Michaelis - Menten) phải TÍNH ra số
trước khi vẽ. Nguyên tắc chung của cả file: thà giải đúng phương trình còn hơn
dùng công thức gần đúng cho nhanh — hình vẽ là thứ người học không đối chiếu lại
được, nên chỗ nào gần đúng sai lệch thấy được bằng mắt thì phải giải chính xác.
"""

from __future__ import annotations

import math
from typing import Callable, Iterable, Optional, Sequence

from .svgkit import Canvas, _n

Params = dict


# --------------------------------------------------------------------------
# Tiện ích chung
# --------------------------------------------------------------------------
def _f(p: Params, key: str, default: float) -> float:
    """Đọc tham số số thực; giá trị rác/NaN/inf bị thay bằng mặc định.

    Generator có thể bị gọi từ bindings.json do người soạn gõ tay, nên một tham số
    hỏng chỉ được phép làm hình xấu đi, không được làm sập cả tiến trình dựng ảnh.
    """
    try:
        v = float(p.get(key, default))
    except (TypeError, ValueError):
        return float(default)
    return v if math.isfinite(v) else float(default)


def _pos(p: Params, key: str, default: float, lo: float = 1e-9, hi: float = 1e9) -> float:
    """Tham số buộc phải dương: hằng số tốc độ, nồng độ, K_M, sức chứa K...

    Số 0 hoặc số âm ở các đại lượng này không có nghĩa hoá/sinh nào mà lại sinh
    chia-cho-0 hoặc log số âm, nên kẹp về khoảng an toàn thay vì ném lỗi.
    """
    return min(max(abs(_f(p, key, default)), lo), hi)


def _duong_phu(mau: str = "b", dash: str = "7 4", rong: float = 2.4) -> dict:
    """Tham số ``cls``/``extra`` cho đường cong PHỤ vẽ chồng lên cùng hệ trục.

    Hai cái bẫy gộp lại chỉ còn đúng một lối ra:

    * lớp CSS thắng thuộc tính trình bày, nên viết ``stroke="..."`` để đổi màu một
      đường đang mang lớp ``curve`` là vô ích — đường thứ hai ra y hệt màu đường
      thứ nhất mà không có lỗi nào báo ra;
    * mã màu không được viết thẳng vào thân SVG, vì bảng màu phải tự lật theo nền
      sáng/tối.

    Còn lại: mượn lớp ``accent-*`` để lấy màu, rồi tắt phần tô bằng
    ``fill-opacity`` — thuộc tính này lớp không đặt nên không bị ghi đè.
    """
    extra = f' fill-opacity="0" stroke-width="{_n(rong)}"'
    if dash:
        extra += f' stroke-dasharray="{dash}"'
    return {"cls": f"accent-{mau}", "extra": extra}


def _smooth(t: float) -> float:
    """Hàm làm trơn 3t²-2t³: đạo hàm triệt tiêu ở hai đầu nên hai đoạn ghép lại
    tại đỉnh vẫn liền mượt, và đỉnh nằm ĐÚNG chỗ ta khai báo — cần thiết để mũi
    tên E_a chỉ đúng vào đỉnh đường cong chứ không lệch vài pixel."""
    t = min(max(t, 0.0), 1.0)
    return t * t * (3 - 2 * t)


class _Frame:
    """Khung toạ độ có tick do người gọi liệt kê.

    ``_Plot`` trong ``generators2d`` chỉ vạch lưới theo số nguyên nên không dùng lại
    được cho các trục có thang riêng (pH 0-14, [S] tính theo bội của K_M, thời gian
    tính theo t½...). Ở đây nhãn tick truyền vào tường minh để đơn vị luôn khớp.
    """

    def __init__(self, cv: Canvas, xmin, xmax, ymin, ymax, box):
        self.cv = cv
        self.xmin, self.xmax = float(xmin), float(xmax)
        self.ymin, self.ymax = float(ymin), float(ymax)
        if not (self.xmax > self.xmin):
            self.xmax = self.xmin + 1.0
        if not (self.ymax > self.ymin):
            self.ymax = self.ymin + 1.0
        self.x0, self.y0, self.pw, self.ph = box

    def sx(self, x: float) -> float:
        return self.x0 + (float(x) - self.xmin) / (self.xmax - self.xmin) * self.pw

    def sy(self, y: float) -> float:
        return self.y0 + (self.ymax - float(y)) / (self.ymax - self.ymin) * self.ph

    def inside(self, x: float, y: float) -> bool:
        return (self.xmin - 1e-9 <= x <= self.xmax + 1e-9
                and self.ymin - 1e-9 <= y <= self.ymax + 1e-9)

    # -- khung, trục ------------------------------------------------------
    def axes(self, xlabel="", ylabel="", xticks: Sequence = (), yticks: Sequence = (),
             origin="auto"):
        """``origin="goc"`` ép trục về mép khung.

        Cần cho các đồ thị mà giá trị 0 của trục tung KHÔNG có ý nghĩa (mốc năng
        lượng chọn tuỳ ý, ln[A] âm dương tuỳ đơn vị): vẽ trục ngang xuyên giữa hình
        ở đó sẽ gợi ý sai rằng có một mốc 0 tự nhiên.
        """
        cv = self.cv
        tu_dong = origin != "goc"
        ax = self.sx(0) if tu_dong and self.xmin <= 0 <= self.xmax else self.x0
        ay = self.sy(0) if tu_dong and self.ymin <= 0 <= self.ymax else self.y0 + self.ph
        cv.arrow(self.x0 - 4, ay, self.x0 + self.pw + 10, ay, cls="axis", head=7)
        cv.arrow(ax, self.y0 + self.ph + 4, ax, self.y0 - 10, cls="axis", head=7)
        if xlabel:
            cv.text(self.x0 + self.pw + 8, ay + 18, xlabel, cls="lbl-sm", anchor="end")
        if ylabel:
            cv.text(ax + 6, self.y0 - 14, ylabel, cls="lbl-sm")
        for v, lab in xticks:
            sx = self.sx(v)
            cv.line(sx, ay - 4, sx, ay + 4, cls="ink-thin")
            if lab:
                cv.text(sx, ay + 17, lab, cls="lbl-sm", anchor="middle")
        for v, lab in yticks:
            sy = self.sy(v)
            cv.line(ax - 4, sy, ax + 4, sy, cls="ink-thin")
            if lab:
                cv.text(ax - 8, sy + 4, lab, cls="lbl-sm", anchor="end")

    # -- vẽ ---------------------------------------------------------------
    def curve(self, pts: Iterable[Sequence[float]], cls="curve", extra=""):
        """Vẽ đường qua các điểm THẾ GIỚI, tự cắt khúc khi ra ngoài khung.

        Cắt thay vì kẹp: kẹp toạ độ sẽ tạo ra đoạn thẳng nằm áp mép khung, trông y
        như một phần đồ thị dù thực ra hàm số đã ra ngoài miền vẽ.
        """
        run: list[tuple[float, float]] = []
        for x, y in pts:
            if self.inside(x, y):
                run.append((self.sx(x), self.sy(y)))
            elif run:
                if len(run) > 1:
                    self.cv.polyline(run, cls=cls, extra=extra)
                run = []
        if len(run) > 1:
            self.cv.polyline(run, cls=cls, extra=extra)

    def hline(self, y, x1=None, x2=None, cls="ink-thin", dash="5 4"):
        x1 = self.xmin if x1 is None else x1
        x2 = self.xmax if x2 is None else x2
        self.cv.line(self.sx(x1), self.sy(y), self.sx(x2), self.sy(y),
                     cls=cls, extra=f' stroke-dasharray="{dash}"')

    def vline(self, x, y1=None, y2=None, cls="ink-thin", dash="5 4"):
        y1 = self.ymin if y1 is None else y1
        y2 = self.ymax if y2 is None else y2
        self.cv.line(self.sx(x), self.sy(y1), self.sx(x), self.sy(y2),
                     cls=cls, extra=f' stroke-dasharray="{dash}"')

    def dot(self, x, y, cls="accent-b", r=3.4):
        self.cv.dot(self.sx(x), self.sy(y), r=r, cls=cls)

    def label(self, x, y, s, cls="lbl-sm", anchor="start", dx=0.0, dy=0.0):
        self.cv.text(self.sx(x) + dx, self.sy(y) + dy, s, cls=cls, anchor=anchor)


def _mui_ten_kep(cv: Canvas, x1, y1, x2, y2, cls="accent-d", head=7.0):
    """Mũi tên hai đầu — dùng cho các đoạn "đo" một hiệu số (E_a, ΔH, K_M...)."""
    cv.arrow(x1, y1, x2, y2, cls=cls, head=head)
    cv.arrow(x2, y2, x1, y1, cls=cls, head=head)


# --------------------------------------------------------------------------
# HOÁ — giản đồ năng lượng phản ứng
# --------------------------------------------------------------------------
def _ve_profile(fr: _Frame, ea: float, dh: float, cls="curve", extra="", xp=0.5):
    """Đường "tiến trình phản ứng -> năng lượng": thềm - đỉnh - thềm.

    Ghép hai đoạn làm trơn nên đỉnh nằm đúng cao độ E_a (xem ``_smooth``).
    """
    x1, x2 = 0.16, 0.84
    peak = ea
    pts = [(0.0, 0.0), (x1, 0.0)]
    for i in range(1, 33):
        t = i / 32
        pts.append((x1 + (xp - x1) * t, ea * _smooth(t)))
    for i in range(1, 33):
        t = i / 32
        pts.append((xp + (x2 - xp) * t, peak + (dh - peak) * _smooth(t)))
    pts.append((1.0, dh))
    fr.curve(pts, cls=cls, extra=extra)


def _panel_nang_luong(cv: Canvas, box, ea, dh, *, tieu_de="", catalyst=None,
                      show_reverse=False):
    lo = min(0.0, dh)
    hi = ea
    span = max(hi - lo, 1e-6)
    fr = _Frame(cv, -0.02, 1.02, lo - 0.22 * span, hi + 0.26 * span, box)
    fr.axes(origin="goc")
    cv.text(box[0] + box[2] / 2, box[1] + box[3] + 24, "tiến trình phản ứng",
            cls="lbl-sm", anchor="middle")
    cv.text(box[0] - 6, box[1] - 12, "Năng lượng", cls="lbl-sm")
    fr.hline(0.0, 0.0, 0.90)
    fr.hline(dh, 0.42, 0.90)
    fr.hline(ea, 0.28, 0.72)
    if catalyst is not None:
        _ve_profile(fr, catalyst, dh, **_duong_phu("c"))
        # chú giải đặt ở góc khung: mọi chỗ cạnh đường nét đứt đều đã có đường cong
        # chính hoặc mũi tên đo đi qua
        cv.text(box[0] + 8, box[1] + 14, "-- có xúc tác", cls="lbl-sm")
    _ve_profile(fr, ea, dh)
    # mũi tên đo E_a thuận / E_a nghịch / ΔH
    _mui_ten_kep(cv, fr.sx(0.31), fr.sy(0.0), fr.sx(0.31), fr.sy(ea))
    cv.text(fr.sx(0.31) - 6, (fr.sy(0.0) + fr.sy(ea)) / 2, "Ea", cls="lbl", anchor="end")
    if show_reverse:
        _mui_ten_kep(cv, fr.sx(0.69), fr.sy(dh), fr.sx(0.69), fr.sy(ea), cls="accent-a")
        cv.text(fr.sx(0.69) + 6, (fr.sy(dh) + fr.sy(ea)) / 2, "Ea nghịch", cls="lbl-sm")
    _mui_ten_kep(cv, fr.sx(0.95), fr.sy(0.0), fr.sx(0.95), fr.sy(dh), cls="accent-b")
    cv.text(fr.sx(0.95) - 5, (fr.sy(0.0) + fr.sy(dh)) / 2, "ΔH", cls="lbl", anchor="end")
    fr.label(0.02, 0.0, "chất đầu", cls="lbl-sm", dy=-9)
    # thềm sản phẩm nằm thấp thì ghi nhãn phía dưới, nằm cao thì ghi phía trên —
    # phía còn lại luôn có đường mức nét đứt chạy qua
    fr.label(0.80, dh, "sản phẩm", cls="lbl-sm", anchor="middle", dy=20 if dh < 0 else -10)
    if tieu_de:
        cv.text(box[0] + box[2] / 2, box[1] - 30, tieu_de, cls="lbl-sm", anchor="middle")
    return fr


def build_energy_profile(p: Params) -> str:
    """Giản đồ năng lượng phản ứng: E_a, ΔH, và nhánh có xúc tác.

    ``mode``: ``"toa"`` (ΔH < 0), ``"thu"`` (ΔH > 0), ``"ca-hai"`` (hai ô cạnh nhau).
    """
    mode = str(p.get("mode", "toa"))
    ea = _pos(p, "ea", 60, lo=1.0, hi=1e4)
    catalyst = None
    if p.get("catalyst"):
        catalyst = min(max(_f(p, "ea_xt", ea * 0.55), 0.15 * ea), 0.95 * ea)
    show_rev = bool(p.get("show_reverse", False))

    if mode == "ca-hai":
        w, h = 660.0, 316.0
        cv = Canvas(w, h, title="Giản đồ năng lượng: phản ứng toả nhiệt và thu nhiệt",
                    desc="Hai giản đồ năng lượng theo tiến trình phản ứng: bên trái sản "
                         "phẩm thấp hơn chất đầu (ΔH < 0, toả nhiệt), bên phải sản phẩm "
                         "cao hơn chất đầu (ΔH > 0, thu nhiệt).")
        _panel_nang_luong(cv, (56.0, 66.0, 244.0, 194.0), ea, -0.55 * ea,
                          tieu_de="Toả nhiệt: ΔH < 0", show_reverse=show_rev)
        _panel_nang_luong(cv, (378.0, 66.0, 244.0, 194.0), ea, 0.55 * ea,
                          tieu_de="Thu nhiệt: ΔH > 0", show_reverse=show_rev)
        return cv.render()

    dh = _f(p, "dh", -0.55 * ea if mode != "thu" else 0.55 * ea)
    # ΔH không thể vượt E_a: đỉnh phải cao hơn cả hai thềm, nếu không hình sẽ mô tả
    # một "hàng rào" thấp hơn sản phẩm — điều vô nghĩa về mặt năng lượng.
    dh = min(dh, 0.85 * ea)
    toa = dh < 0
    w, h = 430.0, 306.0
    cv = Canvas(w, h, title="Giản đồ năng lượng phản ứng " + ("toả nhiệt" if toa else "thu nhiệt"),
                desc="Đường biểu diễn năng lượng theo tiến trình phản ứng, có hàng rào "
                     "năng lượng hoạt hoá Ea ở trạng thái chuyển tiếp và hiệu ΔH giữa "
                     "thềm sản phẩm và thềm chất đầu."
                     + (" Đường nét đứt là đường có xúc tác, hàng rào thấp hơn." if catalyst else ""))
    _panel_nang_luong(cv, (64.0, 62.0, 316.0, 190.0), ea, dh,
                      tieu_de=str(p.get("title", "")), catalyst=catalyst,
                      show_reverse=show_rev)
    return cv.render()


# --------------------------------------------------------------------------
# HOÁ — động học: nồng độ theo thời gian
# --------------------------------------------------------------------------
def _nong_do(order: int, a0: float, k: float, t: float) -> Optional[float]:
    """[A] tại thời điểm t. Trả None khi phản ứng bậc 0 đã hết chất đầu.

    Bậc 0 hết chất tại t = [A]₀/k; kéo đường thẳng qua mốc đó sẽ vẽ ra nồng độ âm.
    """
    if order == 0:
        v = a0 - k * t
        return v if v >= 0 else None
    if order == 1:
        return a0 * math.exp(-k * t)
    return a0 / (1.0 + a0 * k * t)


def _t_nua(order: int, a0: float, k: float) -> float:
    if order == 0:
        return a0 / (2 * k)
    if order == 1:
        return math.log(2) / k
    return 1.0 / (k * a0)


def build_kinetics_decay(p: Params) -> str:
    """Đường cong nồng độ - thời gian của phản ứng bậc 0, 1 hoặc 2.

    ``order`` 0/1/2; ``half_life`` đánh dấu các chu kì bán huỷ liên tiếp — chính chỗ
    phân biệt ba bậc: bậc 0 các t½ ngắn dần, bậc 1 bằng nhau, bậc 2 dài dần.
    """
    order = int(_f(p, "order", 1))
    order = order if order in (0, 1, 2) else 1
    a0 = _pos(p, "a0", 1.0, lo=1e-6, hi=1e6)
    k = _pos(p, "k", {0: 0.25, 1: 0.5, 2: 1.2}[order], lo=1e-6, hi=1e6)
    show_half = bool(p.get("half_life", False))
    t12 = _t_nua(order, a0, k)
    tmax = _f(p, "tmax", a0 / k if order == 0 else 4.2 * t12)
    tmax = min(max(tmax, 1e-6), 1e9)

    w, h = 420.0, 300.0
    ten = {0: "bậc không", 1: "bậc một", 2: "bậc hai"}[order]
    cv = Canvas(w, h, title=f"Nồng độ theo thời gian, phản ứng {ten}",
                desc=f"Đồ thị [A] theo t của phản ứng {ten}: "
                     + {0: "đường thẳng dốc xuống, cắt trục hoành khi hết chất đầu.",
                        1: "đường cong giảm theo hàm mũ, mỗi chu kì bán huỷ bằng nhau.",
                        2: "đường cong giảm chậm dần, các chu kì bán huỷ dài dần."}[order])
    fr = _Frame(cv, -0.04 * tmax, 1.10 * tmax, -0.12 * a0, 1.18 * a0,
                (58.0, 30.0, 322.0, 208.0))
    fr.axes("t", "[A]",
            xticks=[(0, "0")] + ([(t12, "t½")] if show_half and t12 <= tmax else []),
            yticks=[(a0, "[A]₀"), (a0 / 2, "[A]₀/2")])
    pts = []
    for i in range(241):
        t = tmax * 1.06 * i / 240
        v = _nong_do(order, a0, k, t)
        if v is None:
            pts.append((t, 0.0))
            break
        pts.append((t, v))
    fr.curve(pts)
    if show_half:
        # ba chu kì bán huỷ liên tiếp: mỗi lần nồng độ còn một nửa so với mốc trước
        muc = a0
        t_moc = 0.0
        for _ in range(3):
            t_next = t_moc + _t_nua(order, muc, k)
            if t_next > tmax * 1.02:
                break
            fr.hline(muc / 2, 0, t_next, cls="ink-thin")
            fr.vline(t_next, 0, muc / 2, cls="ink-thin")
            fr.dot(t_next, muc / 2, cls="accent-b", r=3.0)
            muc /= 2
            t_moc = t_next
    ct = {0: "[A] = [A]₀ − kt", 1: "[A] = [A]₀·e^(−kt)", 2: "1/[A] = 1/[A]₀ + kt"}[order]
    cv.text(w - 22, h - 14, ct, cls="lbl", anchor="end")
    return cv.render()


def build_kinetics_linearization(p: Params) -> str:
    """Ba đồ thị tuyến tính hoá dùng để nhận bậc phản ứng.

    Mỗi ô vẽ đúng dạng đồ thị THẲNG của bậc tương ứng — đó là cả nội dung của quy
    tắc: bậc nào cho đường thẳng thì phản ứng thuộc bậc ấy.
    """
    a0 = _pos(p, "a0", 1.0, lo=1e-3, hi=1e3)
    k = _pos(p, "k", 0.5, lo=1e-3, hi=1e3)
    w, h = 660.0, 250.0
    cv = Canvas(w, h, title="Tuyến tính hoá đồ thị để xác định bậc phản ứng",
                desc="Ba đồ thị theo thời gian: [A] theo t thẳng ứng với bậc 0, "
                     "ln[A] theo t thẳng ứng với bậc 1, 1/[A] theo t thẳng ứng với bậc 2.")
    # mỗi ô là một phản ứng giả định khác nhau nên có miền thời gian riêng: ô bậc 0
    # phải dừng trước khi [A] chạm 0, nếu dùng chung tmax thì đường thẳng sẽ đi
    # xuống dưới trục và vẽ ra nồng độ âm.
    cau_hinh = [
        ("[A] theo t", "bậc 0 — hệ số góc −k", lambda t: a0 - k * t, 0.85 * a0 / k),
        ("ln[A] theo t", "bậc 1 — hệ số góc −k", lambda t: math.log(a0) - k * t, 1.6 / k),
        ("1/[A] theo t", "bậc 2 — hệ số góc +k", lambda t: 1 / a0 + k * t, 1.6 / k),
    ]
    for i, (ylab, chu, fn, tmax) in enumerate(cau_hinh):
        y0v, y1v = fn(0.0), fn(tmax)
        lo, hi = min(y0v, y1v), max(y0v, y1v)
        span = max(hi - lo, 1e-6)
        box = (48.0 + i * 208.0, 46.0, 148.0, 142.0)
        fr = _Frame(cv, -0.05 * tmax, 1.15 * tmax, lo - 0.22 * span, hi + 0.22 * span, box)
        fr.axes("t", ylab, origin="goc")
        fr.curve([(tmax * j / 40, fn(tmax * j / 40)) for j in range(41)])
        cv.text(box[0] + box[2] / 2, box[1] + box[3] + 44, chu, cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# HOÁ — đường cong chuẩn độ acid - base
# --------------------------------------------------------------------------
def _ph_chuan_do(ca: float, va: float, cb: float, vb: float, ka: float,
                 kw: float = 1e-14) -> float:
    """pH của Va mL acid (nồng độ Ca, hằng số Ka) sau khi thêm Vb mL base mạnh Cb.

    Giải thẳng phương trình trung hoà điện bằng chia đôi trên thang log thay vì
    ghép các công thức gần đúng từng đoạn: Henderson-Hasselbalch và √(Ka·C) sai rõ
    ngay đầu phép chuẩn độ và ngay quanh điểm tương đương — đúng hai chỗ đường cong
    đổi dốc mạnh nhất, tức là chỗ người học nhìn kỹ nhất.
    """
    v = va + vb
    if v <= 0:
        return 7.0
    ct = ca * va / v          # tổng nồng độ acid ở mọi dạng
    cna = cb * vb / v         # nồng độ cation của base mạnh đã thêm
    lo, hi = 1e-15, 1.0       # [H⁺] chắc chắn nằm trong khoảng này với nồng độ dạy học
    for _ in range(100):
        hcon = math.sqrt(lo * hi)
        f = cna + hcon - kw / hcon - ct * ka / (ka + hcon)
        if f > 0:
            hi = hcon
        else:
            lo = hcon
    return -math.log10(math.sqrt(lo * hi))


def _mau_chuan_do(veq: float, vmax: float, n: int = 190) -> list[float]:
    """Lưới thể tích: dày thêm quanh điểm tương đương để bước nhảy pH không bị cắt cụt."""
    vs = [vmax * i / n for i in range(n + 1)]
    lo, hi = max(0.0, 0.94 * veq), min(vmax, 1.06 * veq)
    if hi > lo:
        vs += [lo + (hi - lo) * i / 140 for i in range(141)]
    vs.sort()
    return vs


def build_titration_curve(p: Params) -> str:
    """Đường cong chuẩn độ acid bằng base mạnh (pH theo thể tích base).

    ``kind``: ``"manh-manh"`` hoặc ``"yeu-manh"``; ``compare`` vẽ chồng cả hai để so
    sánh bước nhảy. Điểm tương đương và điểm nửa tương đương được lấy TỪ CHÍNH hàm
    tính pH nên chấm luôn nằm trên đường cong, không bị lệch.
    """
    kind = str(p.get("kind", "yeu-manh"))
    ca = _pos(p, "ca", 0.1, lo=1e-4, hi=5)
    cb = _pos(p, "cb", 0.1, lo=1e-4, hi=5)
    va = _pos(p, "va", 25.0, lo=1.0, hi=500)
    pka = min(max(_f(p, "pka", 4.76), 0.5), 11.0)
    compare = bool(p.get("compare", False))
    veq = ca * va / cb
    vmax = 2.0 * veq

    w, h = 450.0, 316.0
    cv = Canvas(w, h, title="Đường cong chuẩn độ acid - base",
                desc="Đồ thị pH theo thể tích dung dịch base mạnh thêm vào: pH tăng "
                     "chậm, nhảy vọt quanh điểm tương đương rồi lại tăng chậm.")
    fr = _Frame(cv, -0.05 * vmax, 1.10 * vmax, 0.0, 14.6, (56.0, 40.0, 320.0, 208.0))
    fr.axes("V base (mL)", "pH",
            xticks=[(0, "0"), (veq / 2, "½V tđ"), (veq, "V tđ")],
            yticks=[(0, "0"), (7, "7"), (14, "14")], origin="goc")

    def ve(ka_val: float, **kw) -> None:
        fr.curve([(v, _ph_chuan_do(ca, va, cb, v, ka_val)) for v in _mau_chuan_do(veq, vmax)], **kw)

    ka_manh = 1e6      # acid mạnh: coi như phân li hoàn toàn trong cùng một mô hình
    ka_yeu = 10 ** (-pka)
    if compare:
        ve(ka_manh)
        ve(ka_yeu, **_duong_phu("b"))
        cv.text(fr.x0 + 8, fr.y0 + 14, "— acid mạnh", cls="lbl-sm")
        cv.text(fr.x0 + 8, fr.y0 + 30, "-- acid yếu", cls="lbl-sm")
        ka_chinh = ka_yeu
    else:
        ka_chinh = ka_manh if kind == "manh-manh" else ka_yeu
        ve(ka_chinh)

    yeu = ka_chinh < 1.0
    if yeu and p.get("show_buffer", True):
        # vùng đệm đúng bằng khoảng tỉ lệ [A⁻]/[HA] từ 1:10 tới 10:1
        v1, v2 = veq / 11.0, veq * 10.0 / 11.0
        cv.rect(fr.sx(v1), fr.sy(pka + 1), fr.sx(v2) - fr.sx(v1),
                fr.sy(pka - 1) - fr.sy(pka + 1), cls="fill-c")
        cv.text((fr.sx(v1) + fr.sx(v2)) / 2, fr.sy(pka - 1) + 15, "vùng đệm",
                cls="lbl-sm", anchor="middle")
    if yeu and p.get("show_half", True):
        ph_half = _ph_chuan_do(ca, va, cb, veq / 2, ka_chinh)
        fr.dot(veq / 2, ph_half, cls="accent-c")
        fr.label(veq / 2, ph_half, "pH = pKa", cls="lbl-sm", anchor="end", dx=-8, dy=-6)
    ind = p.get("indicator")
    if isinstance(ind, (list, tuple)) and len(ind) >= 2:
        lo, hi = float(ind[0]), float(ind[1])
        lo, hi = min(max(lo, 0), 14), min(max(hi, 0), 14)
        if hi > lo:
            cv.rect(fr.sx(0), fr.sy(hi), fr.sx(vmax) - fr.sx(0),
                    fr.sy(lo) - fr.sy(hi), cls="fill-b")
            cv.text(fr.sx(vmax), fr.sy(hi) - 5,
                    str(ind[2]) if len(ind) > 2 else "khoảng đổi màu",
                    cls="lbl-sm", anchor="end")
    ph_eq = _ph_chuan_do(ca, va, cb, veq, ka_chinh)
    fr.vline(veq, 0.0, ph_eq)
    fr.dot(veq, ph_eq, cls="accent-b", r=4)
    fr.label(veq, ph_eq, "điểm tương đương", cls="lbl-sm", dx=8, dy=4)
    return cv.render()


# --------------------------------------------------------------------------
# HOÁ — nguyên tử: quỹ đạo Bohr, mức năng lượng, ô lượng tử
# --------------------------------------------------------------------------
def build_bohr_atom(p: Params) -> str:
    """Mô hình Bohr: hạt nhân và các quỹ đạo dừng, bán kính tỉ lệ n².

    Bán kính vẽ đúng tỉ lệ n² (chứ không cách đều) vì đó chính là nội dung của
    rₙ = n²a₀/Z; vẽ cách đều sẽ dạy sai ngay từ hình. Mặc định chỉ 3 quỹ đạo: với
    n = 4 thì quỹ đạo trong cùng chỉ còn 1/16 bán kính ngoài, nhỏ tới mức không
    còn chỗ ghi nhãn — muốn thêm quỹ đạo thì truyền ``n`` lớn hơn và chấp nhận
    các quỹ đạo trong không có nhãn.
    """
    nmax = int(min(max(_f(p, "n", 3), 2), 6))
    z = int(min(max(_f(p, "Z", 1), 1), 30))
    R = 108.0
    pad = 46.0
    cx = cy = pad + R
    w = 2 * (pad + R)
    h = w + 26.0
    cv = Canvas(w, h, title="Mô hình nguyên tử Bohr",
                desc=f"Hạt nhân ở tâm và {nmax} quỹ đạo dừng tròn đồng tâm; bán kính "
                     "quỹ đạo thứ n tỉ lệ với n² nên các quỹ đạo càng ra ngoài càng "
                     "thưa dần.")
    truoc = 0.0
    for n in range(1, nmax + 1):
        r = R * (n * n) / (nmax * nmax)
        cv.circle(cx, cy, r, cls="ink-thin" if n < nmax else "ink")
        # chỉ ghi nhãn khi vòng này còn cách vòng trong đủ xa để chữ không đè lên nó
        if r - truoc >= 18.0:
            cv.text(cx, cy - r - 5, f"n = {n}", cls="lbl-sm", anchor="middle")
        truoc = r
    cv.circle(cx, cy, 5, cls="accent-b", extra=' fill-opacity="1"')
    # electron trên quỹ đạo ngoài cùng, kèm đoạn đo bán kính r_n
    ang = math.radians(-35)
    ex, ey = cx + R * math.cos(ang), cy + R * math.sin(ang)
    cv.dot(ex, ey, r=5, cls="accent-a")
    cv.line(cx, cy, ex, ey, cls="accent-a", extra=' stroke-width="1.6" stroke-dasharray="4 3"')
    cv.text(cx + R * 0.55 * math.cos(ang) + 4, cy + R * 0.55 * math.sin(ang) - 6,
            "r" + "₀₁₂₃₄₅₆"[nmax], cls="lbl")
    cv.text(pad - 22, h - 10, "chấm đỏ ở tâm: hạt nhân", cls="lbl-sm")
    cv.text(w - pad + 22, h - 10, "r(n) = n²·a₀ / Z", cls="lbl", anchor="end")
    return cv.render()


_SERIES = (("Lyman", 1, "accent-a"), ("Balmer", 2, "accent-c"), ("Paschen", 3, "accent-d"))


def build_energy_levels(p: Params) -> str:
    """Giản đồ mức năng lượng của nguyên tử hiđrô và các dãy quang phổ.

    Trục năng lượng tuyến tính theo E = −13,6·Z²/n² nên các mức tự động dồn lại
    gần giới hạn ion hoá — đó là điều cần thấy, không được vẽ cách đều cho đẹp.
    """
    nmax = int(min(max(_f(p, "n", 6), 3), 8))
    z = int(min(max(_f(p, "Z", 1), 1), 10))
    e1 = -13.6 * z * z
    show = [s for s in _SERIES if s[1] < nmax]
    if isinstance(p.get("series"), (list, tuple)) and p["series"]:
        ten = [str(s).lower() for s in p["series"]]
        show = [s for s in show if s[0].lower() in ten] or show

    w, h = 470.0, 320.0
    cv = Canvas(w, h, title="Giản đồ mức năng lượng và dãy quang phổ hiđrô",
                desc="Các mức năng lượng nằm ngang, đánh số n = 1 tới n = "
                     f"{nmax}, dồn dần về giới hạn ion hoá E = 0. Mũi tên đi xuống là "
                     "các chuyển mức phát xạ của từng dãy quang phổ.")
    fr = _Frame(cv, 0.0, 1.0, e1 * 1.06, -e1 * 0.10, (74.0, 34.0, 306.0, 230.0))
    cv.line(fr.sx(0.02), fr.sy(0), fr.sx(1.0), fr.sy(0), cls="ink-thin",
            extra=' stroke-dasharray="6 4"')
    cv.text(fr.sx(1.0) + 4, fr.sy(0) - 5, "E = 0  (ion hoá)", cls="lbl-sm")
    for n in range(1, nmax + 1):
        en = e1 / (n * n)
        cv.line(fr.sx(0.02), fr.sy(en), fr.sx(1.0), fr.sy(en), cls="ink")
        # Các mức cao dồn sát nhau (đúng bản chất của E ~ −1/n²) nên không thể ghi
        # riêng từng số: ba mức đầu ghi rõ, cả khối phía trên gộp thành một nhãn.
        if n <= 3:
            cv.text(fr.sx(1.0) + 4, fr.sy(en) + 4, f"n = {n}", cls="lbl-sm")
        elif n == nmax:
            cv.text(fr.sx(1.0) + 4, fr.sy(en) + 4,
                    f"n = 4–{nmax}" if nmax > 4 else "n = 4", cls="lbl-sm")
        if n <= 3:
            cv.text(fr.sx(0.02) - 6, fr.sy(en) + 4, f"{_n(round(en, 2))} eV",
                    cls="lbl-sm", anchor="end")
    for j, (ten_day, nlo, cls) in enumerate(show):
        x = 0.14 + 0.28 * j
        elo = e1 / (nlo * nlo)
        so_vach = max(1, 4 - nlo)      # dãy càng cao thì các mức xuất phát càng sít nhau
        for k in range(1, so_vach + 1):
            nhi = nlo + k
            if nhi > nmax:
                break
            ehi = e1 / (nhi * nhi)
            cv.arrow(fr.sx(x + 0.05 * (k - 1)), fr.sy(ehi),
                     fr.sx(x + 0.05 * (k - 1)), fr.sy(elo), cls=cls, head=7)
        cv.text(fr.sx(x + 0.04), fr.sy(elo) + 17, ten_day, cls="lbl-sm", anchor="middle")
    cv.text(74.0, h - 14, "E(n) = −13,6·Z²/n²  (eV)", cls="lbl")
    return cv.render()


_PHAN_LOP = (("s", 1), ("p", 3), ("d", 5), ("f", 7))


def _o_luong_tu(cv: Canvas, x, y, so_o: int, so_e: int, size=26.0, gap=3.0):
    """Vẽ dãy ô lượng tử và điền ``so_e`` electron theo quy tắc Hund."""
    for i in range(so_o):
        cv.rect(x + i * (size + gap), y, size, size, cls="ink")
    don = min(so_e, so_o)                 # điền một electron vào mỗi ô trước
    doi = max(0, so_e - so_o)             # rồi mới ghép đôi
    for i in range(don):
        bx = x + i * (size + gap) + size / 2
        cv.arrow(bx - 5, y + size - 5, bx - 5, y + 5, cls="accent-a", head=5)
    for i in range(doi):
        bx = x + i * (size + gap) + size / 2
        cv.arrow(bx + 5, y + 5, bx + 5, y + size - 5, cls="accent-b", head=5)


def build_orbital_boxes(p: Params) -> str:
    """Cấu hình electron theo ô lượng tử.

    ``mode``: ``"phan-lop"`` (số ô và số electron tối đa của s, p, d, f),
    ``"hund"`` (điền ``e`` electron vào một phân lớp theo quy tắc Hund),
    ``"lop"`` (các phân lớp của lớp thứ n, tổng n² ô và 2n² electron).
    """
    mode = str(p.get("mode", "phan-lop"))
    size, gap = 26.0, 3.0

    if mode == "hund":
        lop = str(p.get("subshell", "p"))
        so_o = dict(_PHAN_LOP).get(lop, 3)
        so_e = int(min(max(_f(p, "e", so_o), 0), 2 * so_o))
        w = 2 * 46.0 + so_o * (size + gap)
        h = 130.0
        # bề rộng tối thiểu tính theo dòng chú thích bên dưới, không theo dãy ô:
        # dãy ô chỉ dài chừng 90px nên khung vừa khít ô sẽ cắt cụt câu chú thích
        cv = Canvas(max(w, 396.0), h, title=f"Quy tắc Hund cho phân lớp {lop}",
                    desc=f"Dãy {so_o} ô lượng tử của phân lớp {lop}, điền {so_e} electron: "
                         "mỗi ô nhận một electron spin song song trước, sau đó mới ghép đôi.")
        _o_luong_tu(cv, 46.0, 44.0, so_o, so_e, size, gap)
        cv.text(46.0, 34.0, f"{lop}{'⁰¹²³⁴⁵⁶⁷⁸⁹'[so_e] if so_e < 10 else ''}", cls="lbl")
        cv.text(46.0, 44.0 + size + 26, "điền đơn, spin song song trước — rồi mới ghép đôi",
                cls="lbl-sm")
        return cv.render()

    if mode == "lop":
        n = int(min(max(_f(p, "n", 3), 1), 4))
        hang = _PHAN_LOP[:n]
        rong = max(so_o for _t, so_o in hang) * (size + gap)
        w = 96.0 + rong + 150.0
        h = 56.0 + n * (size + 18.0)
        cv = Canvas(w, h, title=f"Các orbital của lớp electron thứ {n}",
                    desc=f"Lớp thứ {n} gồm các phân lớp {', '.join(t for t, _ in hang)}; "
                         f"tổng cộng {n*n} orbital nên chứa tối đa {2*n*n} electron.")
        for i, (ten, so_o) in enumerate(hang):
            y = 44.0 + i * (size + 18.0)
            cv.text(70.0, y + size / 2 + 5, f"{n}{ten}", cls="lbl", anchor="end")
            _o_luong_tu(cv, 78.0, y, so_o, 2 * so_o, size, gap)
        cv.text(78.0, h - 14, f"số AO = n² = {n*n};  số e tối đa = 2n² = {2*n*n}", cls="lbl-sm")
        return cv.render()

    rong = 7 * (size + gap)
    w = 96.0 + rong + 132.0
    h = 56.0 + 4 * (size + 18.0)
    cv = Canvas(w, h, title="Số ô lượng tử và số electron tối đa của mỗi phân lớp",
                desc="Bốn dãy ô: phân lớp s có 1 ô, p có 3 ô, d có 5 ô, f có 7 ô; "
                     "mỗi ô chứa tối đa 2 electron ngược spin.")
    for i, (ten, so_o) in enumerate(_PHAN_LOP):
        y = 44.0 + i * (size + 18.0)
        cv.text(70.0, y + size / 2 + 5, ten, cls="lbl", anchor="end")
        _o_luong_tu(cv, 78.0, y, so_o, 2 * so_o, size, gap)
        cv.text(78.0 + rong + 12, y + size / 2 + 5,
                f"2(2ℓ+1) = {2 * so_o} e", cls="lbl-sm")
    return cv.render()


# --------------------------------------------------------------------------
# HOÁ — pin điện hoá
# --------------------------------------------------------------------------
def build_galvanic_cell(p: Params) -> str:
    """Sơ đồ pin điện hoá: anot, catot, cầu muối, chiều electron.

    Quy ước không được vẽ sai: anot là nơi OXI HOÁ và là cực ÂM của pin Galvani,
    electron chạy TRONG DÂY từ anot sang catot, còn anion trong cầu muối chạy
    ngược lại về phía anot.
    """
    kim_a = str(p.get("anode", "Zn"))
    kim_c = str(p.get("cathode", "Cu"))
    ion_a = str(p.get("anode_ion", f"{kim_a}²⁺"))
    ion_c = str(p.get("cathode_ion", f"{kim_c}²⁺"))
    ghi_a = str(p.get("anode_note", ""))
    ghi_c = str(p.get("cathode_note", ""))
    emf = str(p.get("emf", "E pin = E catot − E anot"))

    w, h = 480.0, 330.0
    cv = Canvas(w, h, title="Sơ đồ pin điện hoá",
                desc=f"Hai cốc dung dịch nối nhau bằng cầu muối; điện cực {kim_a} là anot "
                     f"(cực âm, xảy ra oxi hoá), điện cực {kim_c} là catot (cực dương, xảy "
                     "ra khử); electron đi trong dây dẫn ngoài từ anot sang catot.")
    # hai cốc
    for x0 in (46.0, 274.0):
        cv.polyline([(x0, 132.0), (x0, 286.0), (x0 + 160.0, 286.0), (x0 + 160.0, 132.0)],
                    cls="ink")
        cv.rect(x0 + 2, 176.0, 156.0, 108.0, cls="fill-a")
    # điện cực
    for x, ten in ((110.0, kim_a), (350.0, kim_c)):
        cv.rect(x - 11, 108.0, 22.0, 132.0, cls="ink")
        cv.text(x, 100.0, ten, cls="lbl", anchor="middle")
    # dây dẫn + vôn kế
    cv.polyline([(110.0, 108.0), (110.0, 62.0), (206.0, 62.0)], cls="ink")
    cv.polyline([(254.0, 62.0), (350.0, 62.0), (350.0, 108.0)], cls="ink")
    cv.circle(230.0, 62.0, 24.0, cls="ink")
    cv.text(230.0, 67.0, "V", cls="lbl", anchor="middle")
    cv.arrow(150.0, 48.0, 196.0, 48.0, cls="accent-b", head=8)
    cv.text(173.0, 40.0, "e⁻", cls="lbl", anchor="middle")
    # cầu muối: chạy phía trên mặt thoáng hai cốc
    cv.path("M 150 192 L 150 156 L 310 156 L 310 192", cls="ink",
            extra=' stroke-width="6" stroke-opacity="0.35"')
    cv.text(230.0, 150.0, "cầu muối", cls="lbl-sm", anchor="middle")
    cv.arrow(258.0, 172.0, 198.0, 172.0, cls="accent-c", head=7)
    cv.text(264.0, 176.0, "anion", cls="lbl-sm")
    # nhãn cực và nửa phản ứng
    cv.text(126.0, 300.0, "anot (−) — oxi hoá", cls="lbl-sm", anchor="middle")
    cv.text(354.0, 300.0, "catot (+) — khử", cls="lbl-sm", anchor="middle")
    cv.text(126.0, 318.0, f"{kim_a} → {ion_a} + 2e⁻", cls="lbl", anchor="middle")
    cv.text(354.0, 318.0, f"{ion_c} + 2e⁻ → {kim_c}", cls="lbl", anchor="middle")
    # nhãn ion đặt dưới chân điện cực: đặt ngang thanh điện cực sẽ bị nó che
    cv.text(126.0, 264.0, ion_a + (f" {ghi_a}" if ghi_a else ""), cls="lbl", anchor="middle")
    cv.text(354.0, 264.0, ion_c + (f" {ghi_c}" if ghi_c else ""), cls="lbl", anchor="middle")
    cv.text(230.0, 24.0, emf, cls="lbl-sm", anchor="middle")
    return cv.render()


# --------------------------------------------------------------------------
# SINH — khung Punnett
# --------------------------------------------------------------------------
def _ket_hop(a: str, b: str) -> str:
    """Ghép hai giao tử thành kiểu gen, mỗi locus viết alen trội trước."""
    if len(a) != len(b):
        return a + b
    out = []
    for x, y in zip(a, b):
        out.append(x + y if x.isupper() or not y.isupper() else y + x)
    return "".join(out)


def _kieu_hinh(gen: str) -> str:
    """Quy kiểu gen (2 alen mỗi locus) về ký hiệu kiểu hình dạng ``A-B-``/``aabb``."""
    out = []
    for i in range(0, len(gen) - 1, 2):
        cap = gen[i:i + 2]
        chu = cap[0].lower()
        out.append(chu.upper() + "-" if any(c.isupper() for c in cap) else chu + chu)
    return "".join(out)


def build_punnett(p: Params) -> str:
    """Khung Punnett n×n cho phép lai.

    ``rows``/``cols`` là giao tử của mẹ/bố; ô được ghép tự động (``cells`` cho phép
    ghi đè khi ký hiệu không phải một chữ cái mỗi locus, ví dụ gen trên NST giới
    tính). ``groups`` tô màu các ô theo nhóm kiểu hình để đọc ra tỉ lệ.
    """
    rows = [str(s) for s in p.get("rows", ["A", "a"])] or ["A", "a"]
    cols = [str(s) for s in p.get("cols", ["A", "a"])] or ["A", "a"]
    rows, cols = rows[:4], cols[:4]
    cells = p.get("cells")
    if not (isinstance(cells, (list, tuple)) and len(cells) == len(rows)
            and all(isinstance(r, (list, tuple)) and len(r) == len(cols) for r in cells)):
        cells = [[_ket_hop(r, c) for c in cols] for r in rows]
    cells = [[str(x) for x in r] for r in cells]
    groups = p.get("groups") if isinstance(p.get("groups"), (list, tuple)) else []

    nr, nc = len(rows), len(cols)
    o = 96.0 if max(nr, nc) <= 2 else 74.0
    hd = 44.0                     # bề rộng dải tiêu đề giao tử
    nhan_hang = str(p.get("row_label", "giao tử ♀"))
    # lề trái tính theo độ dài nhãn hàng (~6,4px/ký tự ở cỡ lbl-sm): nhãn dài như
    # "giao tử ♀ (tần số)" mà dùng lề cố định thì bị cắt cụt ngoài khung
    pad_l, pad_t = max(96.0, 14.0 + 6.4 * len(nhan_hang)), 56.0
    chu_thich = 22.0 * len(groups) + (12.0 if groups else 0.0)
    w = pad_l + hd + nc * o + 28.0
    h = pad_t + hd + nr * o + 30.0 + chu_thich
    cv = Canvas(w, h, title="Khung Punnett",
                desc=f"Khung Punnett {nr}×{nc}: hàng là giao tử {', '.join(rows)}, cột là "
                     f"giao tử {', '.join(cols)}; mỗi ô là kiểu gen của hợp tử tương ứng.")
    ox, oy = pad_l + hd, pad_t + hd
    cv.text(pad_l, pad_t - 26, str(p.get("title", "")), cls="lbl-sm")
    cv.text(ox + nc * o / 2, pad_t - 8, str(p.get("col_label", "giao tử ♂")),
            cls="lbl-sm", anchor="middle")
    cv.text(pad_l - 10, oy + nr * o / 2, nhan_hang, cls="lbl-sm", anchor="end")
    for j, c in enumerate(cols):
        cv.text(ox + j * o + o / 2, pad_t + hd - 14, c, cls="lbl", anchor="middle")
    for i, r in enumerate(rows):
        cv.text(ox - hd / 2, oy + i * o + o / 2 + 5, r, cls="lbl", anchor="middle")
    # nền ô theo nhóm kiểu hình, vẽ trước lưới để viền không bị che
    for i in range(nr):
        for j in range(nc):
            kh = _kieu_hinh(cells[i][j])
            for g in groups:
                keys = [str(k) for k in g.get("keys", [])]
                if cells[i][j] in keys or kh in keys:
                    cv.rect(ox + j * o, oy + i * o, o, o, cls=str(g.get("cls", "fill-a")))
                    break
    for i in range(nr + 1):
        cv.line(ox, oy + i * o, ox + nc * o, oy + i * o, cls="ink")
    for j in range(nc + 1):
        cv.line(ox + j * o, oy, ox + j * o, oy + nr * o, cls="ink")
    kich_co = "lbl" if max(nr, nc) <= 2 else "lbl-sm"
    for i in range(nr):
        for j in range(nc):
            cv.text(ox + j * o + o / 2, oy + i * o + o / 2 + 5, cells[i][j],
                    cls=kich_co, anchor="middle")
    y = oy + nr * o + 24.0
    if p.get("ratio"):
        cv.text(pad_l, y, str(p["ratio"]), cls="lbl")
        y += 20.0
    for g in groups:
        cv.rect(pad_l, y - 10, 14.0, 12.0, cls=str(g.get("cls", "fill-a")))
        cv.rect(pad_l, y - 10, 14.0, 12.0, cls="ink-thin")
        cv.text(pad_l + 22, y, str(g.get("label", "")), cls="lbl-sm")
        y += 22.0
    return cv.render()


# --------------------------------------------------------------------------
# SINH — phả hệ
# --------------------------------------------------------------------------
def _ky_hieu_pha_he(cv: Canvas, x, y, sex: str, benh: bool, mang: bool, s=13.0):
    """Nam = hình vuông, nữ = hình tròn; tô đặc = bị bệnh; chấm giữa = mang gen."""
    dac = ' fill-opacity="1"'
    if str(sex).startswith("n") and str(sex) != "nu":     # 'nam'
        if benh:
            cv.rect(x - s, y - s, 2 * s, 2 * s, cls="accent-b", extra=dac)
        cv.rect(x - s, y - s, 2 * s, 2 * s, cls="ink")
    else:
        if benh:
            cv.circle(x, y, s, cls="accent-b", extra=dac)
        cv.circle(x, y, s, cls="ink")
    if mang and not benh:
        cv.dot(x, y, r=4.0, cls="accent-b")


def build_pedigree(p: Params) -> str:
    """Sơ đồ phả hệ hai thế hệ: một cặp bố mẹ và các con, kèm chú giải ký hiệu.

    Vẽ kèm chú giải là bắt buộc: ký hiệu phả hệ chỉ có nghĩa khi người đọc biết
    quy ước vuông/tròn và tô đặc/chấm giữa.
    """
    bo_me = p.get("parents")
    if not (isinstance(bo_me, (list, tuple)) and len(bo_me) == 2):
        bo_me = [{"sex": "nam", "carrier": True}, {"sex": "nu", "carrier": True}]
    con = p.get("children")
    if not (isinstance(con, (list, tuple)) and con):
        con = [{"sex": "nam"}, {"sex": "nu", "affected": True},
               {"sex": "nu", "carrier": True}, {"sex": "nam", "carrier": True}]
    con = list(con)[:6]
    nc = len(con)

    buoc = 74.0
    rong_con = (nc - 1) * buoc
    w = max(360.0, rong_con + 150.0)
    h = 300.0
    cx = w / 2
    y_bm, y_con = 84.0, 196.0
    cv = Canvas(w, h, title="Sơ đồ phả hệ",
                desc=f"Phả hệ hai thế hệ: một cặp bố mẹ ở thế hệ I và {nc} người con ở thế "
                     "hệ II; hình vuông là nam, hình tròn là nữ, ký hiệu tô đặc là người "
                     "bị bệnh, chấm ở giữa là người mang gen bệnh nhưng không biểu hiện.")
    cv.text(24.0, y_bm + 5, "I", cls="lbl", anchor="middle")
    cv.text(24.0, y_con + 5, "II", cls="lbl", anchor="middle")
    xa, xb = cx - 52.0, cx + 52.0
    cv.line(xa + 13, y_bm, xb - 13, y_bm, cls="ink")          # vạch hôn phối
    for x, ind in ((xa, bo_me[0]), (xb, bo_me[1])):
        _ky_hieu_pha_he(cv, x, y_bm, ind.get("sex", "nam"),
                        bool(ind.get("affected")), bool(ind.get("carrier")))
        if ind.get("label"):
            cv.text(x, y_bm - 22, str(ind["label"]), cls="lbl-sm", anchor="middle")
    y_nhanh = (y_bm + y_con) / 2
    cv.line(cx, y_bm, cx, y_nhanh, cls="ink")                 # đường xuống đời con
    x0 = cx - rong_con / 2
    if nc > 1:
        cv.line(x0, y_nhanh, x0 + rong_con, y_nhanh, cls="ink")
    for i, ind in enumerate(con):
        x = x0 + i * buoc
        cv.line(x, y_nhanh, x, y_con - 13, cls="ink")
        _ky_hieu_pha_he(cv, x, y_con, ind.get("sex", "nam"),
                        bool(ind.get("affected")), bool(ind.get("carrier")))
        if ind.get("label"):
            cv.text(x, y_con + 30, str(ind["label"]), cls="lbl-sm", anchor="middle")
    # chú giải
    yl = 258.0
    cv.rect(40.0, yl - 9, 18.0, 18.0, cls="ink")
    cv.text(64.0, yl + 5, "nam", cls="lbl-sm")
    cv.circle(122.0, yl, 9.0, cls="ink")
    cv.text(136.0, yl + 5, "nữ", cls="lbl-sm")
    cv.circle(184.0, yl, 9.0, cls="accent-b", extra=' fill-opacity="1"')
    cv.text(198.0, yl + 5, "bị bệnh", cls="lbl-sm")
    cv.circle(262.0, yl, 9.0, cls="ink")
    cv.dot(262.0, yl, r=3.4, cls="accent-b")
    cv.text(276.0, yl + 5, "mang gen", cls="lbl-sm")
    if p.get("note"):
        cv.text(w - 24, 30.0, str(p["note"]), cls="lbl", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# SINH — tăng trưởng quần thể
# --------------------------------------------------------------------------
def build_population_growth(p: Params) -> str:
    """Đường cong tăng trưởng quần thể.

    ``mode``: ``"mu"`` (chữ J), ``"logistic"`` (chữ S có tiệm cận K), ``"so-sanh"``
    (chồng hai đường), ``"dndt"`` (parabol dN/dt theo N, cực đại tại N = K/2),
    ``"vi-sinh-vat"`` (bốn pha nuôi cấy không liên tục).
    """
    mode = str(p.get("mode", "logistic"))
    K = _pos(p, "K", 1000.0, lo=1.0, hi=1e9)
    n0 = min(_pos(p, "N0", K * 0.04, lo=1e-6, hi=1e9), 0.9 * K)
    r = _pos(p, "r", 1.0, lo=1e-4, hi=50.0)
    w, h = 430.0, 300.0
    box = (62.0, 30.0, 320.0, 210.0)

    if mode == "dndt":
        cv = Canvas(w, h, title="Tốc độ tăng trưởng theo kích thước quần thể",
                    desc="Parabol dN/dt theo N của mô hình logistic: bằng 0 khi N = 0 và "
                         "khi N = K, đạt cực đại rK/4 tại N = K/2.")
        vmax = r * K / 4
        fr = _Frame(cv, -0.05 * K, 1.15 * K, -0.12 * vmax, 1.30 * vmax, box)
        fr.axes("N", "dN/dt",
                xticks=[(0, "0"), (K / 2, "K/2"), (K, "K")],
                yticks=[(vmax, "rK/4")])
        fr.curve([(K * i / 120, r * (K * i / 120) * (1 - i / 120)) for i in range(121)])
        fr.vline(K / 2, 0, vmax)
        fr.hline(vmax, 0, K / 2)
        fr.dot(K / 2, vmax, cls="accent-b", r=4)
        cv.text(w - 22, h - 14, "dN/dt = rN(1 − N/K)", cls="lbl", anchor="end")
        return cv.render()

    if mode == "vi-sinh-vat":
        cv = Canvas(w, h, title="Đường cong sinh trưởng của vi khuẩn trong nuôi cấy không liên tục",
                    desc="Đồ thị log số tế bào theo thời gian gồm bốn pha nối tiếp: tiềm "
                         "phát nằm ngang, luỹ thừa đi lên thẳng, cân bằng nằm ngang, suy "
                         "vong đi xuống.")
        fr = _Frame(cv, -0.3, 10.6, -0.4, 9.4, box)
        fr.axes("t", "log N", xticks=[(0, "0")])
        moc = [(0.0, 2.0), (2.0, 2.0), (5.5, 8.0), (8.0, 8.0), (10.0, 5.6)]
        pts = []
        for i in range(len(moc) - 1):
            (x1, y1), (x2, y2) = moc[i], moc[i + 1]
            for j in range(25):
                t = j / 24
                pts.append((x1 + (x2 - x1) * t, y1 + (y2 - y1) * t))
        pts.append(moc[-1])
        fr.curve(pts)
        for x1, x2, ten in ((0.0, 2.0, "tiềm phát"), (2.0, 5.5, "luỹ thừa"),
                            (5.5, 8.0, "cân bằng"), (8.0, 10.0, "suy vong")):
            fr.vline(x2, -0.4, 9.4, cls="grid", dash="4 4")
            fr.label((x1 + x2) / 2, 9.0, ten, cls="lbl-sm", anchor="middle")
        return cv.render()

    tmax = _f(p, "tmax", 8.0 / r)
    tmax = min(max(tmax, 1e-3), 1e6)

    def logistic(t):
        return K / (1 + (K - n0) / n0 * math.exp(-r * t))

    def mu(t):
        return n0 * math.exp(r * t)

    if mode == "mu":
        # hàm mũ không có tiệm cận để bám nên miền t phải tự chọn theo BỘI SỐ của N₀:
        # lấy tmax quá lớn thì mốc 2N₀ tụt xuống sát trục hoành, mốc t = ln2/r vẽ ra
        # cũng không đọc được nữa
        boi = 12.0 if p.get("doubling", False) else 40.0
        if "tmax" not in p:
            tmax = math.log(boi) / r
        ytop = mu(tmax) * 1.12
        cv = Canvas(w, h, title="Tăng trưởng theo tiềm năng sinh học (đường cong chữ J)",
                    desc="Đồ thị số cá thể theo thời gian tăng theo hàm mũ: càng về sau "
                         "đường cong càng dốc, không có giới hạn trên.")
        fr = _Frame(cv, -0.04 * tmax, 1.10 * tmax, -0.10 * ytop, ytop, box)
        fr.axes("t", "N", xticks=[(0, "0")], yticks=[(n0, "N₀")])
        fr.curve([(tmax * i / 160, mu(tmax * i / 160)) for i in range(161)])
        if p.get("doubling", False):
            td = math.log(2) / r
            if td <= tmax:
                fr.hline(2 * n0, 0, td)
                fr.vline(td, 0, 2 * n0)
                fr.dot(td, 2 * n0, cls="accent-b")
                fr.label(td, 0, "t = ln2/r", cls="lbl-sm", dx=6, dy=18)
                fr.label(0, 2 * n0, "2N₀", cls="lbl-sm", anchor="end", dx=-8, dy=4)
        cv.text(w - 22, h - 14, "N(t) = N₀·e^(rt)", cls="lbl", anchor="end")
        return cv.render()

    cv = Canvas(w, h,
                title="Tăng trưởng logistic của quần thể" + (" so với tăng trưởng mũ" if mode == "so-sanh" else ""),
                desc="Đồ thị số cá thể theo thời gian: đường cong chữ S đi lên nhanh nhất "
                     "tại N = K/2 rồi chậm dần, tiến tới đường tiệm cận nằm ngang là sức "
                     "chứa K của môi trường."
                     + (" Đường nét đứt là tăng trưởng mũ không giới hạn." if mode == "so-sanh" else ""))
    fr = _Frame(cv, -0.04 * tmax, 1.10 * tmax, -0.10 * K, 1.24 * K, box)
    fr.axes("t", "N", xticks=[(0, "0")], yticks=[(n0, "N₀"), (K / 2, "K/2"), (K, "K")])
    fr.hline(K, 0, 1.10 * tmax, cls="accent-b")
    if mode == "so-sanh":
        fr.curve([(tmax * i / 160, mu(tmax * i / 160)) for i in range(161)], **_duong_phu("b"))
        cv.text(fr.x0 + 8, fr.y0 + 14, "-- tăng trưởng mũ", cls="lbl-sm")
    fr.curve([(tmax * i / 160, logistic(tmax * i / 160)) for i in range(161)])
    # điểm uốn N = K/2: nơi tốc độ tăng trưởng lớn nhất
    t_uon = math.log((K - n0) / n0) / r
    if 0 < t_uon < tmax:
        fr.dot(t_uon, K / 2, cls="accent-c", r=4)
        fr.vline(t_uon, 0, K / 2, cls="ink-thin")
        fr.label(t_uon, K / 2, "điểm uốn", cls="lbl-sm", dx=8, dy=14)
    cv.text(w - 22, h - 14, "dN/dt = rN(1 − N/K)", cls="lbl", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# SINH — động học enzyme
# --------------------------------------------------------------------------
def _alpha(p: Params) -> tuple[float, float]:
    """(α, α′) theo kiểu ức chế: α nhân vào K_M, α′ nhân vào [S]."""
    kieu = str(p.get("inhibition", "") or "")
    a = min(max(_f(p, "alpha", 2.5), 1.0), 12.0)
    if kieu == "canh-tranh":
        return a, 1.0
    if kieu == "khong-canh-tranh":
        return a, a
    if kieu == "phi-canh-tranh":
        return 1.0, a
    if kieu == "hon-hop":
        return a, min(max(_f(p, "alpha2", 1.6), 1.0), 12.0)
    return 1.0, 1.0


def build_enzyme_kinetics(p: Params) -> str:
    """Động học enzyme.

    ``mode``: ``"mm"`` (v theo [S], hyperbol bão hoà), ``"lineweaver"`` (1/v theo
    1/[S]), ``"eadie"`` (v theo v/[S]), ``"hanes"`` ([S]/v theo [S]), ``"hill"``
    (đường cong sigmoid). ``inhibition`` thêm đường thứ hai của chất ức chế.
    """
    mode = str(p.get("mode", "mm"))
    vmax = _pos(p, "vmax", 100.0, lo=1e-3, hi=1e6)
    km = _pos(p, "km", 2.0, lo=1e-4, hi=1e6)
    a, a2 = _alpha(p)
    co_uc_che = (a, a2) != (1.0, 1.0)
    ylab = str(p.get("ylabel", "v₀"))
    vlab = str(p.get("vmax_label", "Vmax"))
    klab = str(p.get("km_label", "KM"))
    w, h = 430.0, 300.0
    box = (66.0, 30.0, 318.0, 208.0)

    if mode == "lineweaver":
        # trục hoành kéo qua âm để thấy giao điểm −1/K_M, vốn là ý nghĩa của đồ thị
        xmax = 1.0 / (0.35 * km)
        xmin = -1.6 / km
        ymax = (km / vmax) * xmax + 1 / vmax
        cv = Canvas(w, h, title="Đồ thị Lineweaver - Burk",
                    desc="Đồ thị 1/v theo 1/[S] là đường thẳng: cắt trục tung tại 1/Vmax, "
                         "cắt trục hoành tại −1/KM, hệ số góc bằng KM/Vmax.")
        fr = _Frame(cv, xmin, xmax * 1.08, -0.35 * ymax, ymax * 1.12, box)
        fr.axes("1/[S]", "1/v₀", xticks=[(-1 / km, "−1/KM")], yticks=[(1 / vmax, "1/Vmax")])
        fr.curve([(xmin + (xmax - xmin) * i / 60, (km / vmax) * (xmin + (xmax - xmin) * i / 60) + 1 / vmax)
                  for i in range(61)])
        fr.dot(0, 1 / vmax, cls="accent-b")
        fr.dot(-1 / km, 0, cls="accent-b")
        if co_uc_che:
            fr.curve([(xmin + (xmax - xmin) * i / 60,
                       (a * km / vmax) * (xmin + (xmax - xmin) * i / 60) + a2 / vmax)
                      for i in range(61)], **_duong_phu("b"))
            cv.text(fr.x0 + 8, fr.y0 + 14, "-- có chất ức chế", cls="lbl-sm")
        cv.text(w - 22, h - 14, "1/v = (KM/Vmax)·(1/[S]) + 1/Vmax", cls="lbl-sm", anchor="end")
        return cv.render()

    if mode == "eadie":
        xmax = vmax / km * 1.05
        cv = Canvas(w, h, title="Đồ thị Eadie - Hofstee",
                    desc="Đồ thị v theo v/[S] là đường thẳng có hệ số góc −KM và cắt trục "
                         "tung tại Vmax.")
        fr = _Frame(cv, -0.06 * xmax, 1.16 * xmax, -0.12 * vmax, 1.20 * vmax, box)
        fr.axes("v₀/[S]", "v₀", yticks=[(vmax, "Vmax")])
        # dừng đúng ở giao điểm với trục hoành: kéo dài thêm sẽ vẽ ra tốc độ âm
        xend = vmax / km
        fr.curve([(xend * i / 60, vmax - km * xend * i / 60) for i in range(61)])
        fr.dot(0, vmax, cls="accent-b")
        fr.dot(vmax / km, 0, cls="accent-b")
        # nhãn giao điểm đặt PHÍA TRÊN trục, nếu để dưới sẽ đè lên nhãn trục hoành
        fr.label(vmax / km, 0, "Vmax/KM", cls="lbl-sm", anchor="middle", dy=-10)
        cv.text(w - 22, h - 14, "v = Vmax − KM·(v/[S])", cls="lbl-sm", anchor="end")
        return cv.render()

    if mode == "hanes":
        smax = 6.0 * km
        ymax = (smax + km) / vmax
        cv = Canvas(w, h, title="Đồ thị Hanes - Woolf",
                    desc="Đồ thị [S]/v theo [S] là đường thẳng có hệ số góc 1/Vmax, cắt "
                         "trục tung tại KM/Vmax và cắt trục hoành tại −KM.")
        fr = _Frame(cv, -1.6 * km, smax * 1.08, -0.30 * ymax, ymax * 1.14, box)
        fr.axes("[S]", "[S]/v₀", xticks=[(-km, "−KM")], yticks=[(km / vmax, "KM/Vmax")])
        fr.curve([(-1.6 * km + (smax + 1.6 * km) * i / 60,
                   ((-1.6 * km + (smax + 1.6 * km) * i / 60) + km) / vmax) for i in range(61)])
        fr.dot(0, km / vmax, cls="accent-b")
        fr.dot(-km, 0, cls="accent-b")
        cv.text(w - 22, h - 14, "[S]/v = [S]/Vmax + KM/Vmax", cls="lbl-sm", anchor="end")
        return cv.render()

    hill = min(max(_f(p, "h", 3.0), 1.0), 8.0) if mode == "hill" else 1.0
    # với h > 1 đường cong bão hoà rất nhanh, để [S] chạy tới 9·K sẽ chỉ thấy một
    # đoạn nằm ngang dài; thu miền lại mới nhìn ra được dạng chữ S
    smax = _f(p, "smax", 4.0 * km if mode == "hill" else 9.0 * km)
    smax = min(max(smax, 2.0 * km), 1e6)
    tieu_de = ("Đường cong Hill (enzyme dị lập thể)" if mode == "hill"
               else "Đường cong Michaelis - Menten")
    cv = Canvas(w, h, title=tieu_de,
                desc=("Đồ thị tốc độ theo nồng độ cơ chất có dạng chữ S, tiến tới đường "
                      "tiệm cận Vmax; nồng độ ứng với nửa Vmax là K0,5."
                      if mode == "hill" else
                      f"Đồ thị {ylab} theo nồng độ cơ chất là hyperbol bão hoà, tiến tới "
                      f"đường tiệm cận {vlab}; nồng độ ứng với nửa {vlab} bằng {klab}."))
    fr = _Frame(cv, -0.05 * smax, 1.12 * smax, -0.10 * vmax, 1.26 * vmax, box)
    fr.axes("[S]", ylab, xticks=[(0, "0"), (km, klab)],
            yticks=[(vmax, vlab), (vmax / 2, str(p.get("half_label", "½ " + vlab)))])
    fr.hline(vmax, 0, 1.12 * smax, cls="accent-b")

    def v_cua(s, aa, aa2):
        sh = s ** hill
        kh = (aa * km) ** hill
        return vmax * sh / (kh + aa2 * sh) if (kh + aa2 * sh) > 0 else 0.0

    fr.curve([(smax * i / 200, v_cua(smax * i / 200, 1.0, 1.0)) for i in range(201)])
    if co_uc_che:
        fr.curve([(smax * i / 200, v_cua(smax * i / 200, a, a2)) for i in range(201)],
                 **_duong_phu("b"))
        cv.text(fr.x0 + 8, fr.y0 + 14, "-- có chất ức chế", cls="lbl-sm")
    fr.hline(vmax / 2, 0, km, cls="ink-thin")
    fr.vline(km, 0, vmax / 2, cls="ink-thin")
    fr.dot(km, vmax / 2, cls="accent-c", r=4)
    cv.text(w - 22, h - 14,
            "v = Vmax·[S]^h / (K^h + [S]^h)" if mode == "hill" else f"{ylab} = {vlab}·[S]/({klab} + [S])",
            cls="lbl-sm", anchor="end")
    return cv.render()


# --------------------------------------------------------------------------
# SINH — tháp sinh thái và dòng năng lượng
# --------------------------------------------------------------------------
_BAC_MAC_DINH = (
    {"label": "SV sản xuất", "value": 10000.0},
    {"label": "SVTT bậc 1", "value": 1000.0},
    {"label": "SVTT bậc 2", "value": 100.0},
    {"label": "SVTT bậc 3", "value": 10.0},
)


def build_trophic_pyramid(p: Params) -> str:
    """Tháp sinh thái (``mode="thap"``) hoặc chuỗi thức ăn (``mode="chuoi"``).

    Bề rộng mỗi bậc tỉ lệ với giá trị của chính bậc đó, nên hình tự thể hiện hiệu
    suất sinh thái ~10% mà không cần nói thêm.
    """
    mode = str(p.get("mode", "thap"))
    bac = p.get("levels")
    if not (isinstance(bac, (list, tuple)) and bac):
        bac = _BAC_MAC_DINH
    bac = [dict(b) for b in list(bac)[:5]]
    n = len(bac)
    don_vi = str(p.get("unit", "kcal·m⁻²·năm⁻¹"))

    if mode == "chuoi":
        w = max(520.0, 60.0 + n * 118.0)
        h = 200.0
        cv = Canvas(w, h, title="Chuỗi thức ăn và bậc dinh dưỡng",
                    desc="Các mắt xích nối nhau bằng mũi tên chỉ chiều truyền chất và "
                         "năng lượng; mỗi mắt xích là một bậc dinh dưỡng, đánh số từ 1.")
        bw, bh = 104.0, 56.0
        for i, b in enumerate(bac):
            x = 34.0 + i * (bw + 14.0)
            cv.rect(x, 76.0, bw, bh, cls="fill-a")
            cv.rect(x, 76.0, bw, bh, cls="ink")
            cv.text(x + bw / 2, 108.0, str(b.get("label", "")), cls="lbl-sm", anchor="middle")
            cv.text(x + bw / 2, 66.0, f"bậc {i + 1}", cls="lbl-sm", anchor="middle")
            if i < n - 1:
                cv.arrow(x + bw + 1, 104.0, x + bw + 13.0, 104.0, cls="accent-b", head=7)
        cv.text(34.0, 168.0, "mũi tên chỉ chiều dòng năng lượng đi qua các bậc dinh dưỡng",
                cls="lbl-sm")
        return cv.render()

    vals = []
    for b in bac:
        try:
            vals.append(abs(float(b.get("value", 1.0))) or 1.0)
        except (TypeError, ValueError):
            vals.append(1.0)
    vmax = max(vals)
    rong_max, rong_min = 268.0, 44.0
    le_trai = 108.0            # chỗ cho cột "hiệu suất sinh thái" nằm ngoài tháp
    w = le_trai + rong_max + 118.0
    h = 66.0 + n * 46.0
    cv = Canvas(w, h, title="Tháp sinh thái",
                desc=f"Tháp gồm {n} bậc chồng lên nhau, bậc dưới rộng hơn bậc trên vì mỗi "
                     "lần chuyển bậc chỉ một phần nhỏ năng lượng được tích luỹ lại.")
    cx = le_trai + rong_max / 2
    cv.text(le_trai - 8, 34.0, "hiệu suất", cls="lbl-sm", anchor="end")
    cv.text(cx + rong_max / 2 + 10, 34.0, don_vi, cls="lbl-sm")
    for i, (b, v) in enumerate(zip(bac, vals)):
        # bề rộng theo căn bậc bốn của tỉ lệ: giữ đúng thứ tự lớn - nhỏ mà bậc trên
        # cùng vẫn còn nhìn thấy được khi tỉ lệ giữa các bậc lên tới 1000 lần
        ti_le = (v / vmax) ** 0.25
        bw = rong_min + (rong_max - rong_min) * ti_le
        y = h - 20.0 - (i + 1) * 46.0
        cv.rect(cx - bw / 2, y, bw, 40.0, cls="fill-c")
        cv.rect(cx - bw / 2, y, bw, 40.0, cls="ink")
        cv.text(cx, y + 25.0, str(b.get("label", "")), cls="lbl-sm", anchor="middle")
        cv.text(cx + rong_max / 2 + 10, y + 25.0, f"{_n(round(v, 2))}", cls="lbl")
        if i > 0 and vals[i - 1] > 0:
            hs = 100.0 * v / vals[i - 1]
            cv.text(le_trai - 8, y + 46.0, f"≈{_n(round(hs, 1))}%", cls="lbl-sm", anchor="end")
    return cv.render()


def build_energy_flow(p: Params) -> str:
    """Sơ đồ dòng năng lượng qua một bậc dinh dưỡng.

    ``mode="tieu-thu"``: I → A → P với ba nhánh thất thoát F (phân), U (bài tiết),
    R (hô hấp). ``mode="so-cap"``: GPP → NPP với nhánh hô hấp R.

    ``show_u``/``caption`` để khớp quy ước ký hiệu của từng chương trình: có sách
    gộp bài tiết vào phân (N = I − (F + R)), vẽ thừa nhánh U ra sẽ lệch với đúng
    công thức mà hình đang minh hoạ.
    """
    mode = str(p.get("mode", "tieu-thu"))
    w, h = 520.0, 280.0

    if mode == "so-cap":
        cv = Canvas(w, h, title="Dòng năng lượng ở sinh vật sản xuất",
                    desc="Năng lượng đồng hoá được (sản lượng sơ cấp thô) chia thành phần "
                         "mất đi do hô hấp và phần còn lại tích luỹ thành sản lượng sơ cấp tinh.")
        hop = ((40.0, str(p.get("gross_key", "GPP")), "sản lượng sơ cấp thô"),
               (310.0, str(p.get("net_key", "NPP")), "sản lượng sơ cấp tinh"))
        for x, ky, ten in hop:
            cv.rect(x, 96.0, 170.0, 66.0, cls="fill-a")
            cv.rect(x, 96.0, 170.0, 66.0, cls="ink")
            cv.text(x + 85.0, 126.0, ky, cls="lbl", anchor="middle")
            cv.text(x + 85.0, 148.0, ten, cls="lbl-sm", anchor="middle")
        cv.arrow(212.0, 129.0, 304.0, 129.0, cls="accent-a", head=8)
        cv.arrow(258.0, 122.0, 258.0, 62.0, cls="accent-b", head=8)
        cv.text(266.0, 56.0, "R — hô hấp", cls="lbl-sm")
        cv.text(40.0, 208.0, str(p.get("caption", "NPP = GPP − R")), cls="lbl")
        return cv.render()

    cv = Canvas(w, h, title="Dòng năng lượng qua một bậc dinh dưỡng",
                desc="Năng lượng trong thức ăn lấy vào (I) chia thành phần không đồng hoá "
                     "được thải ra (F) và phần đồng hoá (A); phần đồng hoá lại chia thành "
                     "bài tiết (U), hô hấp (R) và sản lượng tích luỹ (P).")
    hop = ((30.0, "I", "thức ăn lấy vào"), (200.0, "A", "đồng hoá"),
           (370.0, "P", "sản lượng"))
    for x, ky, ten in hop:
        cv.rect(x, 96.0, 120.0, 66.0, cls="fill-a")
        cv.rect(x, 96.0, 120.0, 66.0, cls="ink")
        cv.text(x + 60.0, 126.0, ky, cls="lbl", anchor="middle")
        cv.text(x + 60.0, 148.0, ten, cls="lbl-sm", anchor="middle")
    cv.arrow(152.0, 129.0, 196.0, 129.0, cls="accent-a", head=8)
    cv.arrow(322.0, 129.0, 366.0, 129.0, cls="accent-a", head=8)
    cv.arrow(90.0, 164.0, 90.0, 214.0, cls="accent-b", head=8)
    cv.text(98.0, 212.0, "F — phân (không đồng hoá)", cls="lbl-sm")
    if p.get("show_u", True):
        cv.arrow(236.0, 94.0, 236.0, 48.0, cls="accent-b", head=8)
        cv.text(244.0, 44.0, "U — bài tiết", cls="lbl-sm")
    cv.arrow(286.0, 164.0, 286.0, 214.0, cls="accent-b", head=8)
    cv.text(294.0, 212.0, "R — hô hấp", cls="lbl-sm")
    cv.text(30.0, 254.0,
            str(p.get("caption", "A = I − F;   P = A − (U + R) = I − (F + U) − R")), cls="lbl")
    return cv.render()


REGISTRY: dict[str, Callable[[Params], str]] = {
    "energy_profile": build_energy_profile,
    "kinetics_decay": build_kinetics_decay,
    "kinetics_linearization": build_kinetics_linearization,
    "titration_curve": build_titration_curve,
    "bohr_atom": build_bohr_atom,
    "energy_levels": build_energy_levels,
    "orbital_boxes": build_orbital_boxes,
    "galvanic_cell": build_galvanic_cell,
    "punnett": build_punnett,
    "pedigree": build_pedigree,
    "population_growth": build_population_growth,
    "enzyme_kinetics": build_enzyme_kinetics,
    "trophic_pyramid": build_trophic_pyramid,
    "energy_flow": build_energy_flow,
}
