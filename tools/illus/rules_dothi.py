"""Luật khớp cho họ **dothi** — đồ thị hàm số và giải tích.

Toàn bộ file khớp bằng **id đầy đủ, so sánh bằng nhau**, không dùng chuỗi con.
Lý do rất cụ thể: kho này có ``math.thpt.gioi-han.*`` (giới hạn hàm số) nằm cạnh
``math.dai-hoc.dinh-li-gioi-han.*`` (định lí giới hạn trung tâm — xác suất), và
``math.thpt.ham-so-bac-nhat-bac-hai.*`` nằm cạnh ``math.thcs.ham-so-bac-nhat.*``.
Một luật khớp theo chuỗi con kiểu ``"gioi-han" in id`` sẽ dán đồ thị giới hạn lên
định lí giới hạn trung tâm — bảng thống kê vẫn đẹp, người học vẫn sai.

Đổi lại, luật ở đây **không tự lan** sang công thức mới: thêm công thức thì phải
thêm id. Đó là cái giá phải trả, và với tầng minh hoạ thì đáng trả.

Mỗi mục trong bảng là ``id -> (generator, params, ghi chú)``. Tham số được chọn
sao cho hình nói đúng *trường hợp mà công thức phát biểu*: công thức nào chỉ đúng
trong một trường hợp (Δ > 0, a > 0, ad − bc > 0…) thì hình ghi rõ trường hợp ấy
trong nhãn, không vẽ chung chung rồi để người đọc tự suy.

**Phạm vi: chỉ công thức môn Toán.** Kho có nhiều công thức Lí/Sinh cũng là đồ
thị (phân rã phóng xạ, tăng trưởng quần thể, đồ thị v–t), nhưng các họ chuyên
môn — ``cohoc``, ``hoasinh`` — đã nhận chúng bằng những hình gắn với ngữ cảnh
môn học. Hai họ cùng nhận một công thức thì hình phụ thuộc thứ tự nạp module,
nên ở đây nhường hẳn phần ấy thay vì tranh.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]

_Table = dict[str, tuple[str, dict, str]]


def _lookup(f: dict, table: _Table) -> Optional[Match]:
    hit = table.get(f.get("id", ""))
    return (hit[0], dict(hit[1]), hit[2]) if hit else None


# ---------------------------------------------------------------------------
# Hàm bậc ba: cực trị, điểm uốn, tâm đối xứng
# ---------------------------------------------------------------------------
_CUBIC: _Table = {
    "math.thpt.ung-dung-dao-ham.dieu-kien-ham-bac-ba-co-cuc-tri": (
        "cubic",
        {"a": 1, "b": 0, "c": -3, "d": 1, "mark": "extrema",
         "label": "b² − 3ac > 0: có hai cực trị"},
        "bậc ba có hai cực trị"),
    "math.thpt.ung-dung-dao-ham.dieu-kien-don-dieu-ham-bac-ba": (
        "cubic",
        {"a": 1, "b": 0, "c": 1, "d": 0, "mark": "none",
         "label": "b² − 3ac ≤ 0: đơn điệu trên ℝ"},
        "bậc ba không có cực trị"),
    "math.thpt.ung-dung-dao-ham.dieu-kien-can-cuc-tri": (
        "cubic",
        {"a": 1, "b": 0, "c": -3, "d": 1, "mark": "extrema", "horizontal_tangents": True,
         "label": "tại cực trị: tiếp tuyến nằm ngang, f′(x₀) = 0"},
        "điều kiện cần của cực trị"),
    "math.thpt.ung-dung-dao-ham.quy-tac-2-cuc-tri": (
        "cubic",
        {"a": 1, "b": 0, "c": -3, "d": 1, "mark": "extrema", "horizontal_tangents": True,
         "label": "f′(x₀) = 0 và f″(x₀) < 0 ⇒ cực đại"},
        "quy tắc 2 tìm cực trị"),
    "math.thpt.ung-dung-dao-ham.diem-uon": (
        "cubic",
        {"a": 1, "b": -3, "c": 0, "d": 2, "mark": "inflection",
         "inflection_label": "U (điểm uốn)", "label": "f″ đổi dấu khi qua điểm uốn"},
        "điểm uốn của hàm bậc ba"),
    "math.thpt.ung-dung-dao-ham.tam-doi-xung-ham-bac-ba": (
        "cubic",
        {"a": 1, "b": -3, "c": 0, "d": 2, "mark": "both",
         "inflection_label": "I (tâm đối xứng)", "label": "I(−b/3a; f(−b/3a))"},
        "tâm đối xứng của hàm bậc ba"),
}


def r_cubic(f: dict) -> Optional[Match]:
    return _lookup(f, _CUBIC)


# ---------------------------------------------------------------------------
# Đơn điệu, cực trị, GTLN–GTNN
# ---------------------------------------------------------------------------
_MONOTONE: _Table = {
    "math.thpt.ung-dung-dao-ham.dieu-kien-don-dieu": (
        "monotone_intervals",
        {"expr": "x^3-3*x", "label": "f′ > 0 ⇒ đồng biến; f′ < 0 ⇒ nghịch biến"},
        "điều kiện đơn điệu"),
    "math.thpt.ung-dung-dao-ham.quy-tac-1-cuc-tri": (
        "monotone_intervals",
        {"expr": "x^3-3*x", "label": "f′ đổi dấu + → − : cực đại; − → + : cực tiểu"},
        "quy tắc 1 tìm cực trị"),
}

_MAXMIN: _Table = {
    "math.thpt.ung-dung-dao-ham.gtln-gtnn-tren-doan": (
        "max_min_segment",
        {"expr": "x^3-3*x", "a": -1.5, "b": 2.2,
         "label": "so sánh f(a), f(b) và f tại các điểm tới hạn"},
        "GTLN–GTNN trên đoạn"),
}


def r_monotone(f: dict) -> Optional[Match]:
    return _lookup(f, _MONOTONE)


def r_max_min(f: dict) -> Optional[Match]:
    return _lookup(f, _MAXMIN)


# ---------------------------------------------------------------------------
# Parabol / tam thức bậc hai
# ---------------------------------------------------------------------------
_PARABOLA: _Table = {
    "math.thpt.ham-so-bac-nhat-bac-hai.toa-do-dinh-parabol": (
        "parabola",
        {"a": 1, "b": -2, "c": -3, "vertex": True, "axis": False, "roots": False,
         "label": "I(−b/2a; −Δ/4a)"},
        "toạ độ đỉnh parabol"),
    "math.thpt.ham-so-bac-nhat-bac-hai.truc-doi-xung-parabol": (
        "parabola",
        {"a": 1, "b": -2, "c": -3, "vertex": True, "axis": True, "roots": False,
         "label": "trục đối xứng x = −b/2a"},
        "trục đối xứng parabol"),
    "math.thpt.ham-so-bac-nhat-bac-hai.gtln-gtnn-ham-bac-hai": (
        "parabola",
        {"a": 1, "b": -2, "c": -3, "vertex": True, "axis": True, "roots": False,
         "label": "a > 0: giá trị nhỏ nhất −Δ/4a đạt tại đỉnh"},
        "GTNN của hàm bậc hai (a > 0)"),
    "math.thpt.ham-so-bac-nhat-bac-hai.tam-thuc-luon-duong": (
        "parabola",
        {"a": 1, "b": -2, "c": 3, "vertex": True, "axis": False, "roots": False,
         "shade": "all", "label": "a > 0 và Δ < 0: f(x) > 0 với mọi x"},
        "tam thức luôn dương"),
    "math.thpt.ham-so-bac-nhat-bac-hai.tam-thuc-luon-am": (
        "parabola",
        {"a": -1, "b": 2, "c": -3, "vertex": True, "axis": False, "roots": False,
         "shade": "all", "label": "a < 0 và Δ < 0: f(x) < 0 với mọi x"},
        "tam thức luôn âm"),
    "math.thpt.ham-so-bac-nhat-bac-hai.bat-phuong-trinh-bac-hai": (
        "parabola",
        {"a": 1, "b": -1, "c": -2, "vertex": False, "axis": False, "roots": True,
         "shade": "between", "label": "a > 0, Δ > 0: f(x) < 0 ⟺ x₁ < x < x₂"},
        "bất phương trình bậc hai"),
    "math.thpt.ham-so-bac-nhat-bac-hai.cong-thuc-nghiem-phuong-trinh-bac-hai": (
        "parabola",
        {"a": 1, "b": -1, "c": -2, "vertex": False, "axis": False, "roots": True,
         "label": "Δ > 0: hai nghiệm phân biệt x₁, x₂"},
        "công thức nghiệm (trường hợp Δ > 0)"),
}


def r_parabola(f: dict) -> Optional[Match]:
    return _lookup(f, _PARABOLA)


# ---------------------------------------------------------------------------
# Phân thức và tiệm cận
# ---------------------------------------------------------------------------
_ASYMPTOTE: _Table = {
    "math.thpt.ung-dung-dao-ham.tiem-can-dung": (
        "rational",
        {"a": 1, "b": 2, "c": 1, "d": -1, "label": "x = x₀ là tiệm cận đứng"},
        "tiệm cận đứng"),
    "math.thpt.ung-dung-dao-ham.tam-doi-xung-phan-thuc": (
        "rational",
        {"a": 1, "b": 2, "c": 1, "d": -1, "center": True,
         "center_label": "I(−d/c; a/c)", "label": "giao hai tiệm cận là tâm đối xứng"},
        "tâm đối xứng hàm phân thức"),
    "math.thpt.ung-dung-dao-ham.bien-thien-ham-phan-thuc": (
        "rational",
        {"a": 1, "b": -2, "c": 1, "d": 1,
         "label": "ad − bc > 0: đồng biến trên từng khoảng xác định"},
        "chiều biến thiên hàm phân thức"),
    "math.thpt.ung-dung-dao-ham.tiem-can-ngang": (
        "limit_infinity",
        {"expr": "2 - 3/(x^2+1)", "y0": 2, "label": "y = y₀ là tiệm cận ngang"},
        "tiệm cận ngang"),
    "math.thpt.ung-dung-dao-ham.tiem-can-xien": (
        "oblique_asymptote",
        {"m": 1, "n": 1, "k": 1, "q": 1, "oblique_label": "y = ax + b",
         "label": "tiệm cận xiên y = ax + b"},
        "tiệm cận xiên"),
}


def r_asymptote(f: dict) -> Optional[Match]:
    return _lookup(f, _ASYMPTOTE)


# ---------------------------------------------------------------------------
# Nghiệm và tương giao đọc trên đồ thị
# ---------------------------------------------------------------------------
_INTERSECT: _Table = {
    "math.thpt.ung-dung-dao-ham.so-nghiem-phuong-trinh-theo-do-thi": (
        "horizontal_cut",
        {"expr": "x^3-3*x", "m": 1, "line_label": "d: y = m",
         "label": "số nghiệm = số giao điểm của (C) và d"},
        "số nghiệm theo đồ thị"),
    "math.thpt.ung-dung-dao-ham.tuong-giao-do-thi": (
        "graph_intersection",
        {"f": "x^2-1", "g": "x+1", "label": "hoành độ giao điểm là nghiệm của f(x) = g(x)"},
        "tương giao hai đồ thị"),
    "math.thpt.mu-logarit.phuong-trinh-mu-co-ban": (
        "horizontal_cut",
        {"expr": "2^x", "m": 3, "xmin": -1.4, "xmax": 3, "line_label": "y = b",
         "root_label": "x = logₐb", "label": "aˣ = b ⟺ x = logₐb"},
        "phương trình mũ cơ bản"),
    "math.thpt.mu-logarit.phuong-trinh-logarit-co-ban": (
        "horizontal_cut",
        {"expr": "log(x)/log(2)", "m": 2, "xmin": -0.6, "xmax": 6, "line_label": "y = b",
         "root_label": "x = aᵇ", "label": "logₐx = b ⟺ x = aᵇ"},
        "phương trình logarit cơ bản"),
}


def r_intersect(f: dict) -> Optional[Match]:
    return _lookup(f, _INTERSECT)


# ---------------------------------------------------------------------------
# Mũ – logarit
# ---------------------------------------------------------------------------
_EXPLOG: _Table = {
    "math.thpt.mu-logarit.dinh-nghia-logarit": (
        "exp_log_pair", {"base": 2}, "logarit là hàm ngược của hàm mũ"),
    "math.thpt.mu-logarit.so-sanh-hai-luy-thua": (
        "base_family", {"kind": "exp", "base": 2}, "so sánh hai luỹ thừa cùng cơ số"),
    "math.thpt.mu-logarit.so-sanh-hai-logarit": (
        "base_family", {"kind": "log", "base": 2}, "so sánh hai logarit cùng cơ số"),
}

# Tăng trưởng mũ: hàm mũ trong Toán và lãi kép (rời rạc lẫn liên tục).
_GROWTH: _Table = {
    "math.thpt.mu-logarit.tang-truong-mu": (
        "exp_growth",
        {"y0": 1, "k": 0.45, "ylabel": "N", "y0_label": "N₀", "curve_label": "N = N₀eᵏᵗ"},
        "tăng trưởng mũ"),
    "math.thpt.mu-logarit.lai-kep-lien-tuc": (
        "exp_growth",
        {"y0": 1, "k": 0.35, "ylabel": "S", "y0_label": "A", "curve_label": "S = Aeʳᵗ"},
        "lãi kép liên tục"),
    "math.thpt.mu-logarit.lai-kep": (
        "exp_growth",
        {"y0": 1, "r": 0.25, "periods": 8, "discrete": True, "ylabel": "T",
         "xlabel": "n (kì)", "note": "vốn chỉ nhảy ở cuối mỗi kì",
         "label": "T = A(1 + r)ⁿ"},
        "lãi kép theo kì"),
    "math.thpt.ptvp-quoc-te.ptvp-tang-truong-mu": (
        "exp_growth",
        {"y0": 1, "k": 0.45, "ylabel": "y", "y0_label": "y₀", "curve_label": "y = y₀eᵏᵗ"},
        "nghiệm của y′ = ky"),
}

# Phân rã theo chu kì bán rã. Bản Lí (phóng xạ) do họ chuyên môn vẽ, ở đây chỉ
# giữ công thức Toán.
_DECAY: _Table = {
    "math.thpt.mu-logarit.chu-ki-ban-ra": (
        "half_life", {"m0": 100, "T": 1, "ylabel": "m", "m0_label": "m₀",
                      "label": "m(t) = m₀·2^(−t/T)"}, "chu kì bán rã"),
}

_LOGISTIC_MATH = {"L": 100, "p0": 8, "k": 0.9, "ylabel": "P", "p0_label": "P₀"}
_LOGISTIC: _Table = {
    "math.thpt.ptvp-quoc-te.nghiem-logistic": (
        "logistic", dict(_LOGISTIC_MATH, label="P(t) = L/(1 + Ae^(−kt))"),
        "nghiệm phương trình logistic"),
    "math.thpt.ptvp-quoc-te.ptvp-logistic": (
        "logistic", dict(_LOGISTIC_MATH, label="P′ = kP(1 − P/L)"),
        "phương trình vi phân logistic"),
    "math.thpt.ptvp-quoc-te.ptvp-logistic-dang-tich": (
        "logistic", dict(_LOGISTIC_MATH, label="P′ = aP(M − P)"),
        "logistic dạng tích"),
    "math.thpt.ptvp-quoc-te.logistic-gioi-han": (
        "logistic", dict(_LOGISTIC_MATH, L_label="y = L (giới hạn khi t → +∞)"),
        "giới hạn của nghiệm logistic"),
    "math.thpt.ptvp-quoc-te.logistic-toc-do-cuc-dai": (
        "logistic", dict(_LOGISTIC_MATH,
                         inflection_label="P = L/2: tốc độ tăng lớn nhất"),
        "tốc độ tăng lớn nhất của logistic"),
}


def r_exp_log(f: dict) -> Optional[Match]:
    return _lookup(f, _EXPLOG)


def r_growth(f: dict) -> Optional[Match]:
    return _lookup(f, _GROWTH)


def r_decay(f: dict) -> Optional[Match]:
    return _lookup(f, _DECAY)


def r_logistic(f: dict) -> Optional[Match]:
    return _lookup(f, _LOGISTIC)


# ---------------------------------------------------------------------------
# Tính chất hàm số, hàm cho theo từng khoảng
# ---------------------------------------------------------------------------
# ``piecewise`` cố tình chưa có luật nào: công thức giá trị tuyệt đối duy nhất ở
# bậc phổ thông nằm ở lớp 6–7 và chú thích của chính nó nói |a| là *khoảng cách
# trên trục số* — hình đúng cho nó là trục số, không phải đồ thị hàm. Generator
# vẫn giữ để gắn tay qua bindings.json khi cần vẽ hàm cho theo từng khoảng.
_SHAPE: _Table = {
    "math.thpt.ham-so-bac-nhat-bac-hai.ham-so-chan-le": (
        "parity", {"even": "0.5*x^2-1", "odd": "0.4*x^3-x"}, "hàm chẵn và hàm lẻ"),
}


def r_shape(f: dict) -> Optional[Match]:
    return _lookup(f, _SHAPE)


# ---------------------------------------------------------------------------
# Giới hạn và liên tục
# ---------------------------------------------------------------------------
_LIMIT: _Table = {
    "math.thpt.gioi-han.gioi-han-mot-ben": (
        "one_sided_limit",
        {"mode": "jump", "x0": 1, "left": "x+2", "right": "x^2",
         "label": "L⁻ ≠ L⁺ ⇒ không tồn tại giới hạn tại x₀"},
        "giới hạn một bên"),
    "math.thpt.gioi-han.dieu-kien-lien-tuc-tai-mot-diem": (
        "one_sided_limit",
        {"mode": "equal", "x0": 1, "left": "x^2", "right": "2*x-1",
         "label": "L⁻ = L⁺ = f(x₀) ⇒ liên tục tại x₀"},
        "điều kiện liên tục tại một điểm"),
    "math.thpt.gioi-han.dinh-nghia-ham-lien-tuc": (
        "one_sided_limit",
        {"mode": "equal", "x0": 1, "left": "x^2", "right": "2*x-1",
         "label": "lim f(x) = f(x₀) ⇒ liên tục tại x₀"},
        "định nghĩa hàm liên tục"),
    "math.thpt.gioi-han.gioi-han-sinx-tren-x": (
        "limit_hole",
        {"expr": "sin(x)/x", "x0": 0, "L": 1, "half_width": 6, "label": "lim (sin x)/x = 1"},
        "giới hạn cơ bản sin x / x"),
    "math.dai-hoc.gioi-han.gioi-han-co-ban-sinx-tren-x": (
        "limit_hole",
        {"expr": "sin(x)/x", "x0": 0, "L": 1, "half_width": 6, "label": "lim (sin x)/x = 1"},
        "giới hạn cơ bản sin x / x"),
    "math.thpt.gioi-han.gioi-han-e-mu-x-tru-mot": (
        "limit_hole",
        {"expr": "(exp(x)-1)/x", "x0": 0, "L": 1, "half_width": 2,
         "label": "lim (eˣ − 1)/x = 1"},
        "giới hạn (eˣ − 1)/x"),
    "math.thpt.gioi-han.gioi-han-ln-mot-cong-x": (
        "limit_hole",
        {"expr": "log(1+x)/x", "x0": 0, "L": 1, "half_width": 0.9,
         "label": "lim ln(1 + x)/x = 1"},
        "giới hạn ln(1+x)/x"),
    "math.thpt.gioi-han.gioi-han-mot-tru-cos": (
        "limit_hole",
        {"expr": "(1-cos(x))/x^2", "x0": 0, "L": 0.5, "half_width": 6,
         "label": "lim (1 − cos x)/x² = 1/2"},
        "giới hạn (1 − cos x)/x²"),
    "math.thpt.gioi-han.gioi-han-day-mot-tren-n": (
        "sequence_limit",
        {"expr": "1/n", "L": 0, "n": 12, "label": "lim 1/nᵏ = 0"},
        "giới hạn dãy 1/nᵏ"),
    "math.thpt.gioi-han.dinh-li-kep": (
        "squeeze",
        {"discrete": True, "label": "u(n) ≤ v(n) ≤ w(n), hai biên cùng giới hạn L"},
        "định lí kẹp cho dãy số"),
    "math.dai-hoc.gioi-han.gioi-han-ke-kep": (
        "squeeze",
        {"discrete": False, "L": 1, "label": "g ≤ f ≤ h và hai biên cùng giới hạn L"},
        "định lí kẹp cho hàm số"),
    "math.thpt.gioi-han.dinh-li-gia-tri-trung-gian": (
        "ivt",
        {"expr": "x^3-x-2", "a": 1, "b": 2,
         "label": "f(a)·f(b) < 0 ⇒ có nghiệm c ∈ (a; b)"},
        "định lí giá trị trung gian"),
}


def r_limit(f: dict) -> Optional[Match]:
    return _lookup(f, _LIMIT)


# ---------------------------------------------------------------------------
# Đạo hàm: tiếp tuyến, cát tuyến, vi phân
# ---------------------------------------------------------------------------
_DERIV: _Table = {
    "math.thpt.dao-ham.phuong-trinh-tiep-tuyen": (
        "tangent_line",
        {"expr": "x^2", "x0": 1, "label": "y = f′(x₀)(x − x₀) + f(x₀)"},
        "phương trình tiếp tuyến"),
    "math.thpt.dao-ham.tiep-tuyen-biet-he-so-goc": (
        "tangent_line",
        {"expr": "x^2", "x0": 1, "label": "hệ số góc tiếp tuyến k = f′(x₀)"},
        "tiếp tuyến biết hệ số góc"),
    "math.thpt.dao-ham.dinh-nghia-dao-ham": (
        "secant_tangent",
        {"expr": "x^2", "x0": 1, "h": 1.2, "dx_label": "x − x₀",
         "dy_label": "f(x) − f(x₀)", "point_label": "M₀",
         "label": "cho x → x₀, cát tuyến tiến tới tiếp tuyến"},
        "định nghĩa đạo hàm"),
    "math.thpt.dao-ham.dinh-nghia-dao-ham-so-gia": (
        "secant_tangent",
        {"expr": "x^2", "x0": 1, "h": 1.2, "dx_label": "Δx = h", "dy_label": "Δy",
         "point_label": "M₀", "label": "f′(x₀) = lim Δy/Δx khi Δx → 0"},
        "định nghĩa đạo hàm theo số gia"),
    "math.thpt.ham-so-bac-nhat-bac-hai.dong-bien-nghich-bien-dinh-nghia": (
        "secant_tangent",
        {"expr": "x^2", "x0": 1, "h": 1.2, "tangent": False, "dx_label": "x₂ − x₁",
         "dy_label": "f(x₂) − f(x₁)", "point_label": "M₁",
         "label": "tỉ số biến thiên > 0 ⇒ đồng biến"},
        "định nghĩa đồng biến – nghịch biến"),
    "math.thpt.dao-ham.vi-phan": (
        "differential",
        {"expr": "x^2", "x0": 1, "dx": 1, "label": "dy = f′(x₀)·dx"},
        "vi phân"),
    "math.dai-hoc.dao-ham.xap-xi-vi-phan": (
        "differential",
        {"expr": "x^2", "x0": 1, "dx": 1,
         "label": "f(x₀ + Δx) ≈ f(x₀) + f′(x₀)Δx"},
        "xấp xỉ bằng vi phân"),
}


def r_derivative(f: dict) -> Optional[Match]:
    return _lookup(f, _DERIV)


# ---------------------------------------------------------------------------
# Tích phân: diện tích, giá trị trung bình
# ---------------------------------------------------------------------------
_AREA: _Table = {
    "math.thpt.nguyen-ham-tich-phan.dien-tich-hinh-phang-mot-duong": (
        "area_under",
        {"expr": "0.5*x^2+1", "a": 1, "b": 4, "part_labels": ["S"],
         "label": "S = ∫|f(x)|dx"},
        "diện tích hình phẳng một đường"),
    "math.thpt.nguyen-ham-tich-phan.cong-thuc-newton-leibniz": (
        "area_under",
        {"expr": "0.5*x^2+1", "a": 1, "b": 4, "part_labels": ["S"],
         "label": "∫f(x)dx = F(b) − F(a)"},
        "công thức Newton – Leibniz"),
    "math.dai-hoc.tich-phan.cong-thuc-newton-leibniz": (
        "area_under",
        {"expr": "0.5*x^2+1", "a": 1, "b": 4, "part_labels": ["S"],
         "label": "∫f(x)dx = F(b) − F(a)"},
        "công thức Newton – Leibniz"),
    "math.thpt.nguyen-ham-tich-phan.tinh-chat-tich-phan-chen-can": (
        "area_under",
        {"expr": "0.5*x^2+1", "a": 1, "b": 4, "splits": [2.5],
         "part_labels": ["S₁", "S₂"], "label": "chèn cận c: S = S₁ + S₂"},
        "tính chất chèn cận"),
    "math.thpt.nguyen-ham-tich-phan.tich-phan-ham-chan": (
        "area_under",
        {"expr": "x^2", "a": -2, "b": 2, "splits": [0], "part_labels": ["S", "S"],
         "label": "f chẵn: hai nửa có diện tích bằng nhau"},
        "tích phân hàm chẵn"),
    "math.thpt.nguyen-ham-tich-phan.tich-phan-ham-le": (
        "area_under",
        {"expr": "x^3", "a": -2, "b": 2, "splits": [0], "signed": True,
         "part_labels": ["−S", "+S"], "label": "f lẻ: hai phần triệt tiêu nhau"},
        "tích phân hàm lẻ"),
    "math.thpt.nguyen-ham-tich-phan.quang-duong-theo-van-toc": (
        "area_under",
        {"expr": "0.6*x+1", "a": 1, "b": 4, "xlabel": "t", "ylabel": "v(t)",
         "part_labels": ["s"], "label": "s = ∫|v(t)|dt"},
        "quãng đường bằng diện tích dưới đồ thị v–t"),
    "math.thpt.nguyen-ham-tich-phan.dien-tich-hinh-phang-hai-duong": (
        "area_between",
        {"f": "4-x^2", "g": "x+2", "label": "S = ∫|f(x) − g(x)|dx"},
        "diện tích giữa hai đường"),
    "math.dai-hoc.ung-dung-tich-phan.dien-tich-descartes": (
        "area_between",
        {"f": "4-x^2", "g": "x+2", "label": "S = ∫|f(x) − g(x)|dx"},
        "diện tích hình phẳng trong hệ Descartes"),
    "math.thpt.nguyen-ham-tich-phan.gia-tri-trung-binh-ham-so": (
        "mean_value_integral",
        {"expr": "0.4*x^2+0.5", "a": 0.5, "b": 3.5,
         "label": "hình chữ nhật cùng diện tích, chiều cao là giá trị trung bình"},
        "giá trị trung bình của hàm số"),
    "math.dai-hoc.ung-dung-tich-phan.gia-tri-trung-binh-ham": (
        "mean_value_integral",
        {"expr": "0.4*x^2+0.5", "a": 0.5, "b": 3.5,
         "label": "hình chữ nhật cùng diện tích, chiều cao là giá trị trung bình"},
        "giá trị trung bình của hàm số"),
    "math.dai-hoc.tich-phan.dinh-li-gia-tri-trung-binh": (
        "mean_value_integral",
        {"expr": "0.4*x^2+0.5", "a": 0.5, "b": 3.5,
         "label": "tồn tại c: diện tích = f(c)·(b − a)"},
        "định lí giá trị trung bình của tích phân"),
}


def r_area(f: dict) -> Optional[Match]:
    return _lookup(f, _AREA)


# ---------------------------------------------------------------------------
# Tổng Riemann và xấp xỉ tích phân
# ---------------------------------------------------------------------------
_UNEVEN = [0, 0.5, 1.4, 2.0, 3.2, 4]      # phân hoạch không đều dùng chung
_RIEMANN: _Table = {
    "math.thpt.tong-riemann.tong-riemann-trai": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "n": 6, "mode": "left",
         "label": "tổng trái: chiều cao lấy ở mút trái"},
        "tổng Riemann trái"),
    "math.thpt.tong-riemann.tong-riemann-phai": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "n": 6, "mode": "right",
         "label": "tổng phải: chiều cao lấy ở mút phải"},
        "tổng Riemann phải"),
    "math.thpt.tong-riemann.tong-riemann-giua": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "n": 6, "mode": "mid",
         "label": "tổng giữa: chiều cao lấy ở trung điểm"},
        "tổng Riemann giữa"),
    "math.thpt.tong-riemann.tong-riemann-tong-quat": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "mode": "mid", "partition": _UNEVEN,
         "label": "xᵢ* lấy tuỳ ý trong mỗi đoạn chia"},
        "tổng Riemann tổng quát"),
    "math.thpt.tong-riemann.chuan-phan-hoach": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "mode": "left", "partition": _UNEVEN,
         "mark_norm": True, "label": "‖P‖ = đoạn chia dài nhất"},
        "chuẩn của phân hoạch"),
    "math.thpt.tong-riemann.gioi-han-tong-deu": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "n": 20, "mode": "right",
         "show_samples": False, "label": "n càng lớn, tổng càng sát tích phân"},
        "giới hạn tổng đều"),
    "math.thpt.tong-riemann.tong-hinh-thang-deu": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "n": 6, "mode": "trapezoid",
         "label": "tổng hình thang: mỗi mảnh là một hình thang"},
        "tổng hình thang đều"),
    "math.thpt.tong-riemann.tong-hinh-thang-khong-deu": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "mode": "trapezoid", "partition": _UNEVEN,
         "label": "hình thang trên phân hoạch không đều"},
        "tổng hình thang không đều"),
    "math.thpt.tong-riemann.hinh-thang-bang-trung-binh-trai-phai": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "n": 6, "mode": "trapezoid", "ghosts": True,
         "label": "hình thang = trung bình của mút trái (xanh) và mút phải (đỏ)"},
        "tổng hình thang là trung bình trái – phải"),
    "math.dai-hoc.giai-tich-thuc.tong-riemann-va-tich-phan": (
        "riemann_sum",
        {"expr": "0.4*x^2+1", "a": 0, "b": 4, "mode": "mid", "partition": _UNEVEN,
         "label": "S(f, P, ξ) = Σ f(ξᵢ)Δxᵢ"},
        "tổng Riemann và tích phân"),
}


def r_riemann(f: dict) -> Optional[Match]:
    return _lookup(f, _RIEMANN)


RULES: list[Rule] = [
    r_cubic, r_monotone, r_max_min, r_parabola, r_asymptote, r_intersect,
    r_exp_log, r_growth, r_decay, r_logistic, r_shape, r_limit,
    r_derivative, r_area, r_riemann,
]
