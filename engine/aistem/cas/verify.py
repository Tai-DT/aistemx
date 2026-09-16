"""Kiểm chứng độc lập bằng CAS.

Đây là điểm tựa của toàn hệ thống: mô hình ngôn ngữ có thể viết một lời giải
trôi chảy mà sai số học, nên mọi đáp số và mọi bước biến đổi đều được SymPy
tính lại từ đầu. Kết quả kiểm chứng có ba trạng thái, không phải hai — "chưa
kết luận được" là câu trả lời hợp lệ và phải nói ra, chứ không được coi là đúng.
"""

from __future__ import annotations

import math
import random
import re
from collections.abc import Mapping
from typing import Literal

import sympy as sp

from ..config import settings
from ..models import StepCheck, Verification
from ..textnorm import (
    clean_latex,
    extract_number,
    normalise_degrees,
    split_equation,
    split_relations,
    starts_with_relation,
    strip_trailing_units,
)
from .chemistry import check_equation, check_molar_mass
from .env import SymbolEnv
from .funcalls import FunctionScope, has_opaque_atom
from .parse import (
    out_of_time,
    reset_deadline,
    run_guarded,
    set_deadline,
    to_number,
    to_sympy,
    usable,
)

Equivalence = Literal["equivalent", "different", "unknown"]

_SAMPLE_ROUNDS = 24
#: Trần cho một lượt thay số. Thấp hơn hẳn `cas_timeout` vì phép này nằm trong
#: vòng lặp hàng chục lượt — cộng lại mới ra thời gian thật.
_SAMPLE_TIMEOUT = 0.6
_SAMPLE_RANGE = (0.37, 3.91)  # tránh 0, 1 và các điểm đặc biệt hay gây trùng giả

#: Sai số tương đối cho phép khi đối chiếu hai con số **bên trong** một lời giải.
#: Lời giải sư phạm làm tròn ở từng bước ("≈ 3,16"), rồi sai số ấy truyền tiếp
#: sang bước sau. Bắt bẻ ở mức 1e-9 sẽ báo sai hàng loạt lời giải hoàn toàn
#: đúng, nên ngưỡng đặt ở 0,5% — vẫn thừa chặt để bắt lỗi số học thật, vốn
#: thường lệch hàng chục phần trăm trở lên.
_STEP_ROUNDING_TOLERANCE = 5e-3


def _written_precision_tolerance(value: float) -> float:
    """Sai số tuyệt đối cho phép, suy từ số chữ số thập phân thực sự được viết.

    `-1,1998` viết 4 chữ số sau dấu phẩy, nên mọi giá trị lệch dưới nửa đơn vị
    ở hàng cuối (5e-5) đều là cùng một con số, chỉ khác chỗ làm tròn.
    """
    text = repr(float(value))
    if "e" in text or "E" in text:
        mantissa, _, exponent = text.partition("e")
        decimals = len(mantissa.partition(".")[2])
        return 0.5 * 10 ** (-decimals + int(exponent or 0))
    decimals = len(text.partition(".")[2].rstrip("0")) or 0
    return 0.5 * 10**-decimals


def _numbers_agree_after_rounding(a: float, b: float) -> bool:
    """Hai số có phải cùng một giá trị, chỉ khác chỗ làm tròn?"""
    if not (math.isfinite(a) and math.isfinite(b)):
        return a == b
    gap = abs(a - b)
    if gap <= max(_written_precision_tolerance(a), _written_precision_tolerance(b)):
        return True
    scale = max(abs(a), abs(b))
    return scale > 0 and gap / scale <= _STEP_ROUNDING_TOLERANCE


def numbers_match(
    expected: float | None, got: float | None, tolerance: float | None = None
) -> tuple[bool, float | None]:
    """So sánh hai số theo sai số **tương đối**, có xử lí trường hợp kỳ vọng bằng 0."""
    if expected is None or got is None:
        return False, None
    tol = settings.default_tolerance if tolerance is None else abs(tolerance)
    if not (math.isfinite(expected) and math.isfinite(got)):
        return expected == got, None
    if expected == 0:
        return abs(got) <= max(tol, 1e-9), abs(got)
    error = abs(got - expected) / abs(expected)
    return error <= tol, error


#: Số chữ số có nghĩa của `sp.N(..., 25)`. Dưới ngưỡng này so với độ lớn của
#: chính các số hạng thì cái đọc được chỉ còn là nhiễu của phép tính.
_WORKING_PRECISION = 1e-18


def _cancellation_floor(expr: sp.Expr, subs: dict) -> float:
    """Dưới ngưỡng nào thì một giá trị chỉ còn là nhiễu chứ không phải đại lượng?

    Không thể lấy một hằng số tuyệt đối, và đây là chỗ hệ thống đã sai suốt:
    ngưỡng cũ neo ở `max(1.0, ...)`, nên **mọi** đại lượng nhỏ hơn 10⁻⁹ đều bị
    coi là bằng nhau. Hằng Planck 6,6·10⁻³⁴, điện tích nguyên tố 1,6·10⁻¹⁹, nồng
    độ 10⁻⁹ M — cả mảng Lí và Hoá vi mô của kho — rơi hết vào vùng đó. Hậu quả
    đi cả hai chiều, và chiều nào cũng tệ: hai giá trị lệch nhau 9 lần bị xác
    nhận là bằng nhau (xác nhận khống), còn một biểu thức còn ẩn thì bị coi là
    hằng rồi đem so như số (báo oan).

    Ngưỡng đúng phải suy từ độ lớn của **chính các số hạng** trong biểu thức tại
    điểm đang thay số: `(x+1)^2 - x^2 - 2x - 1` đúng bằng 0 nhưng tính ra 10⁻²⁵,
    và 10⁻²⁵ ấy là nhiễu vì các số hạng của nó cỡ đơn vị. Cùng con số 10⁻²⁵ ở
    một bài vật lí hạt nhân thì lại là một đại lượng thật.
    """
    terms = expr.args if isinstance(expr, sp.Add) else (expr,)
    biggest = 0.0
    for term in terms:
        value = run_guarded(
            lambda t=term: abs(complex(sp.N(t.subs(subs), 25))),
            None,
            timeout=_SAMPLE_TIMEOUT,
        )
        if value is not None and math.isfinite(value):
            biggest = max(biggest, value)
    return biggest * _WORKING_PRECISION


def _sample_compare(a: sp.Expr, b: sp.Expr) -> Equivalence:
    """So hai biểu thức bằng cách thay số ngẫu nhiên vào các ẩn chung.

    Nhanh và quyết đoán: nếu hai biểu thức khác nhau, hầu như chắc chắn lệch
    ngay ở lần thay đầu tiên. Nếu trùng qua hàng chục lần thay thì khả năng
    trùng ngẫu nhiên là không đáng kể.
    """
    try:
        symbols = sorted(a.free_symbols | b.free_symbols, key=str)
    except (AttributeError, TypeError):
        return "unknown"
    if len(symbols) > 8:
        return "unknown"
    rng = random.Random(20260814)
    agree = 0
    evaluated = 0
    for _ in range(_SAMPLE_ROUNDS):
        if out_of_time():
            break
        subs = {s: sp.Float(rng.uniform(*_SAMPLE_RANGE)) for s in symbols}
        # Phải đi qua `run_guarded`: `subs` và `N` trên một biểu thức bệnh lí có
        # thể chạy hàng giây, và chúng nằm trong vòng lặp 24 lượt. Gọi thẳng thì
        # cả lượt kiểm chứng treo mà không lớp chặn thời gian nào bắt được.
        # `subs=subs` là bắt buộc: lambda chạy ở luồng khác, mà vòng lặp thì đi
        # tiếp ngay. Bắt theo tham chiếu thì luồng kia có thể đọc phải bộ giá
        # trị của lượt sau, và kết luận "hai vế khác nhau" sẽ vô căn cứ.
        values = run_guarded(
            lambda subs=subs: (
                complex(sp.N(a.subs(subs), 25)),
                complex(sp.N(b.subs(subs), 25)),
            ),
            None,
            timeout=_SAMPLE_TIMEOUT,
        )
        if values is None:
            continue
        va, vb = values
        if not (math.isfinite(va.real) and math.isfinite(vb.real)):
            continue
        if abs(va.imag) > 1e6 or abs(vb.imag) > 1e6:
            continue
        evaluated += 1
        scale = max(abs(va), abs(vb))
        if abs(va - vb) <= 1e-8 * scale:
            agree += 1
            continue
        # Lệch nhau về mặt tương đối. Trước khi kết luận "khác nhau" phải loại
        # trừ khả năng cả hai vế thực chất bằng 0 và cái đang so chỉ là nhiễu
        # còn lại sau một phép trừ gần triệt tiêu.
        floor = max(_cancellation_floor(a, subs), _cancellation_floor(b, subs))
        if abs(va) <= floor and abs(vb) <= floor:
            agree += 1
            continue
        return "different"
    if evaluated >= 3 and agree == evaluated:
        return "equivalent"
    return "unknown"


def _constant_value(expr: sp.Expr) -> float | None:
    """Biểu thức có ẩn này thực chất là một hằng số? Nếu có, trả giá trị ấy."""
    try:
        symbols = sorted(expr.free_symbols, key=str)
    except (AttributeError, TypeError):
        return None
    if not symbols or len(symbols) > 6:
        return None

    rng = random.Random(20260814)
    values: list[float] = []
    for _ in range(8):
        if out_of_time():
            break
        subs = {s: sp.Float(rng.uniform(*_SAMPLE_RANGE)) for s in symbols}
        evaluated = run_guarded(
            lambda subs=subs: complex(sp.N(expr.subs(subs), 25)),
            None,
            timeout=_SAMPLE_TIMEOUT,
        )
        if evaluated is None:
            continue
        if not math.isfinite(evaluated.real) or abs(evaluated.imag) > 1e-9:
            continue
        values.append(evaluated.real)
    if len(values) < 4:
        return None
    spread = max(values) - min(values)
    # Thang đo phải là độ lớn của chính các giá trị đọc được, KHÔNG neo ở 1.0:
    # neo ở 1.0 thì `e·4,20·10⁻¹⁵` (với `e` là điện tích nguyên tố, một ẩn thật)
    # biến thiên cả trăm phần trăm mà vẫn "trải rộng" chưa tới 10⁻⁹, nên bị coi
    # là hằng số rồi đem so như một con số — và lời giải đúng bị bác bỏ.
    scale = max(abs(v) for v in values)
    if scale == 0:
        return 0.0  # bằng 0 ở mọi lần thay: đây là hằng số 0 thật
    return values[0] if spread <= 1e-9 * scale else None


_PI_SYMBOL = sp.Symbol("pi")


def _reads_pi_as_symbol(*exprs: sp.Expr | None) -> bool:
    """Có vế nào đang đọc `\\pi` thành **ẩn tự do** thay vì hằng số π không?"""
    for expr in exprs:
        try:
            if _PI_SYMBOL in expr.free_symbols:  # type: ignore[union-attr]
                return True
        except (AttributeError, TypeError):
            continue
    return False


def _as_pi_constant(expr: sp.Expr | None) -> sp.Expr | None:
    """Đọc lại biểu thức với `pi` là hằng số π.

    Bắt mọi lỗi chứ không chỉ vài loại: phép thay này dựng lại cả cây biểu thức,
    và có những chỗ dựng lại được về mặt cú pháp mà SymPy từ chối về mặt nghĩa —
    `\\frac{dP}{d\\pi}` thành "đạo hàm theo hằng số π" và ném `ValueError`. Đây
    chỉ là một cách đọc **thêm**, nên hỏng thì bỏ qua, không được làm đổ cả lượt
    kiểm chứng.
    """
    try:
        return expr.xreplace({_PI_SYMBOL: sp.pi})  # type: ignore[union-attr]
    except Exception:
        return None


def equivalent(
    a: sp.Expr | None,
    b: sp.Expr | None,
    *,
    require_same_symbols: bool = True,
    env: SymbolEnv | None = None,
    defined_here: frozenset[str] = frozenset(),
) -> tuple[Equivalence, str]:
    """Hai biểu thức có bằng nhau không, đọc `\\pi` theo cả hai nghĩa.

    Parser LaTeX trả `\\pi` về một **ẩn tự do** tên `pi`, không phải hằng số π.
    Hậu quả im lặng: `\\frac{\\pi}{\\sin(\\pi/3)} = \\frac{2\\pi}{\\sqrt{3}}` là
    một đẳng thức đúng, nhưng thay số ngẫu nhiên vào `pi` thì `\\sin(pi/3)` cho
    ra giá trị khác hẳn và bước bị **bác bỏ oan**.

    Đọc ngược lại (`pi` là hằng π) cũng không phải lúc nào cũng đúng: trong
    Thống kê `\\pi` là tỉ lệ tổng thể, `\\pi = 0{,}4` hoàn toàn hợp lệ. Vì thế
    hai cách đọc được đối xử bất đối xứng, đúng theo nguyên tắc của cả bộ kiểm
    chứng: **một cách đọc xác nhận là đủ để xác nhận, nhưng phải cả hai cùng
    bác bỏ thì mới được kết tội.**
    """
    verdict, reason = _equivalent_reading(
        a, b, require_same_symbols=require_same_symbols, env=env, defined_here=defined_here
    )
    if verdict == "equivalent" or not _reads_pi_as_symbol(a, b):
        return verdict, reason

    pi_a, pi_b = _as_pi_constant(a), _as_pi_constant(b)
    if pi_a is None or pi_b is None:
        return verdict, reason
    alt, alt_reason = _equivalent_reading(
        pi_a, pi_b, require_same_symbols=require_same_symbols, env=env, defined_here=defined_here
    )
    if alt == "equivalent":
        return "equivalent", f"{alt_reason} (đọc `\\pi` là hằng số π)"
    if verdict == "different" and alt != "different":
        return "unknown", (
            "hai vế chỉ khác nhau khi đọc `\\pi` là một ẩn tự do — chưa đủ căn cứ kết tội"
        )
    return verdict, reason


def _equivalent_reading(
    a: sp.Expr | None,
    b: sp.Expr | None,
    *,
    require_same_symbols: bool = True,
    env: SymbolEnv | None = None,
    defined_here: frozenset[str] = frozenset(),
) -> tuple[Equivalence, str]:
    """Một lượt so hai biểu thức.

    `require_same_symbols` là hàng rào chống báo động giả quan trọng nhất.
    Trong một lời giải, dấu `=` mang hai nghĩa khác hẳn nhau:

    * **đồng nhất thức** — `1 + 4x^2(x^2+1) = 4x^4 + 4x^2 + 1`, đúng với mọi x.
      Sai ở đây là sai thật, phải bác bỏ.
    * **thế số / định nghĩa** — `1 + (y')^2 = 1 + 4x^2(x^2+1)`, chỉ đúng vì `y'`
      đã được tính ở bước trước. CAS nhìn riêng bước này thì thấy "khác nhau",
      nhưng lời giải hoàn toàn đúng.

    Phân biệt hai loại bằng tập ẩn: khác tập ẩn nghĩa là có thế số, và ta trả
    "chưa kết luận" thay vì kết tội oan.
    """
    if not (usable(a) and usable(b)):
        return "unknown", "không đọc được một trong hai vế"

    def _prepare(expr: sp.Expr) -> sp.Expr:
        done = expr.doit() if hasattr(expr, "doit") else expr
        return done if usable(done) else expr

    a = run_guarded(lambda: _prepare(a), a)
    b = run_guarded(lambda: _prepare(b), b)

    if a == b:
        return "equivalent", "trùng khớp về cấu trúc"

    # Bất đẳng thức / mệnh đề logic: không so bằng hiệu số được.
    # Phải bắt đúng `BooleanAtom` và `BooleanFunction`, KHÔNG dùng `Boolean`:
    # trong SymPy `Symbol` cũng kế thừa `Boolean` (để viết được `And(p, q)`),
    # nên bắt rộng sẽ khiến mọi phép so có một vế là ký hiệu trần đều bị bỏ qua.
    _PROPOSITION = (sp.Rel, sp.logic.boolalg.BooleanAtom, sp.logic.boolalg.BooleanFunction)
    if isinstance(a, _PROPOSITION) or isinstance(b, _PROPOSITION):
        return "unknown", "vế là mệnh đề, không so bằng hiệu số"

    try:
        syms_a, syms_b = set(a.free_symbols), set(b.free_symbols)
    except (AttributeError, TypeError):
        return "unknown", "biểu thức không ở dạng CAS xử lí được"

    if require_same_symbols and syms_a != syms_b:
        # Một vế không còn ẩn thì vẫn có thể là đồng nhất thức thật:
        # `sin^2 x + cos^2 x = 1` là ví dụ kinh điển. Phân biệt bằng cách thay
        # số vào vế còn ẩn — nếu nó cho cùng một giá trị ở mọi lần thay thì đó
        # là hằng, và ta đối chiếu được; nếu nó thay đổi thì đây là bước thế số.
        symbolic, constant = (a, b) if syms_a and not syms_b else (b, a)
        if not (syms_a and syms_b):
            value = _constant_value(symbolic)
            other = to_number(constant)
            if value is not None and other is not None:
                if _numbers_agree_after_rounding(value, other):
                    return "equivalent", f"vế còn lại là hằng số {value:.10g}"
                return "different", f"{value:.10g} ≠ {other:.10g}"

        # Lối thoát cho đúng loại "thế số" này: nếu những ẩn còn lệch đã được
        # chính lời giải gán giá trị ở bước trước thì thay chúng vào rồi mới so
        # — lúc đó hai vế mới thật sự nói cùng một chuyện.
        if env is not None and env.usable_for(syms_a ^ syms_b, defined_here):
            resolved = env.reconcile(a, b, exclude=defined_here)
            if resolved is not None:
                subbed_a, subbed_b, used = resolved
                # Gọi lại KHÔNG kèm `env`: sau khi thay thì hai vế đã cùng tập
                # ẩn, và một vòng thay nữa chỉ có thể là thay lồng nhau — thứ
                # không kiểm soát được nguồn gốc.
                verdict, reason = equivalent(subbed_a, subbed_b)
                trail = ", ".join(used[:4])
                if verdict == "equivalent":
                    return "equivalent", f"khớp sau khi thay {trail} từ các bước trước ({reason})"
                if verdict == "different":
                    # Đây là chỗ dễ báo oan nhất của cả đòn bẩy. Ràng buộc lấy từ
                    # bước trước có thể đã hết hiệu lực (ký hiệu đổi nghĩa, đổi
                    # đơn vị, hoặc lời giải sang phần khác của bài) mà không câu
                    # chữ nào báo trước. Lệch sau khi thay là dấu hiệu đáng rà,
                    # KHÔNG phải bằng chứng lỗi số học.
                    if settings.env_may_refute:
                        return "different", f"sau khi thay {trail}: {reason}"
                    return "unknown", (
                        f"thay {trail} từ bước trước thì hai vế lệch nhau — nêu ra để rà,"
                        " chưa đủ căn cứ kết tội vì ràng buộc có thể đã đổi nghĩa"
                    )

        return "unknown", (
            "hai vế có tập ẩn khác nhau ("
            + ", ".join(sorted(str(s) for s in syms_a ^ syms_b)[:4])
            + ") — đây là bước thế số chứ không phải đồng nhất thức"
        )

    both_numeric = not (syms_a or syms_b)
    if both_numeric:
        na, nb = to_number(a), to_number(b)
        if na is not None and nb is not None:
            if _numbers_agree_after_rounding(na, nb):
                return "equivalent", f"cùng giá trị số {na:.10g} (chấp nhận làm tròn)"
            _, err = numbers_match(na, nb, _STEP_ROUNDING_TOLERANCE)
            gap = f" (lệch {err:.3g})" if err is not None else ""
            return "different", f"{na:.10g} ≠ {nb:.10g}{gap}"
        # Hai vế là số nhưng `to_number` không quy ra giá trị (biểu thức phải
        # `.doit()` mới ra số, hoặc đơn giản là hết giờ vì máy bận). Ở đây phép
        # thay số vẫn được **xác nhận**, nhưng không được **kết tội**:
        #
        # `_sample_compare` so ở ngưỡng 1e-8, vốn dành cho đồng nhất thức đại số
        # chứ không dành cho những con số đã làm tròn trong lời giải.
        # `180° + 53,1° = 233°` chỉ lệch 0,04% — đúng chuẩn sư phạm, nhưng thừa
        # sức bị 1e-8 kết tội. Tệ hơn nữa, lỗi ấy chỉ hiện ra khi `to_number`
        # tình cờ hết giờ, tức một lời bác bỏ không lặp lại được.
        if _sample_compare(a, b) == "equivalent":
            return "equivalent", "trùng khớp qua toàn bộ lần thay số ngẫu nhiên"
        return "unknown", "hai vế là số nhưng CAS chưa quy ra giá trị để so"

    sampled = _sample_compare(a, b)
    if sampled == "different":
        return "different", "thay số ngẫu nhiên cho ra hai giá trị khác nhau"
    if sampled == "equivalent":
        # Hai chục lần thay số ngẫu nhiên đều cho cùng giá trị là bằng chứng
        # quá đủ. Chạy tiếp `simplify` chỉ để "cho chắc" là phần tốn kém nhất
        # của cả bộ kiểm chứng, mà không đổi kết luận.
        return "equivalent", "trùng khớp qua toàn bộ lần thay số ngẫu nhiên"

    def _symbolic() -> Equivalence:
        diff = sp.simplify(sp.expand(a - b))
        if diff == 0:
            return "equivalent"
        diff = sp.cancel(sp.together(diff))
        if diff == 0:
            return "equivalent"
        diff = sp.simplify(sp.trigsimp(diff))
        return "equivalent" if diff == 0 else "unknown"

    result = run_guarded(_symbolic, "unknown")
    if result == "equivalent":
        return "equivalent", "hiệu hai vế rút gọn về 0"
    return "unknown", "CAS chưa kết luận được"


def latex_equivalent(a: str, b: str) -> tuple[Equivalence, str]:
    return equivalent(to_sympy(a), to_sympy(b))


# --------------------------------------------------------------------------- #
# Kiểm chuỗi biến đổi
# --------------------------------------------------------------------------- #


# Một dòng LaTeX thường chứa nhiều mệnh đề độc lập:
#   P(X=1) = 0,4 + 0,1 = 0,5, \qquad P(Y=1) = 0,3 + 0,1 = 0,4
# Không tách ra thì `split_equation` nối "0,5" với "P(Y=1)" thành một chuỗi
# đẳng thức bịa, rồi báo sai một lời giải đúng.
# Cùng lí do với các liên từ logic: `B = 2 \Rightarrow A = -1` là hai mệnh đề
# nối bằng suy ra, không phải một chuỗi đẳng thức `2 = A`.
# Chú ý: KHÔNG kể `\to` vào đây. Trong kho nó gần như luôn là mũi tên của giới
# hạn (`\lim_{x \to 3}`), tách theo nó sẽ xé đôi chính biểu thức cần kiểm.
_FRAGMENT_RE = re.compile(
    r"\\qquad|\\quad|\\\\|;"
    r"|\\(?:Rightarrow|Longrightarrow|longrightarrow|implies|iff"
    r"|Leftrightarrow|leftrightarrow|therefore)\b"
    r"|,\s*\\[\s,;]|\s{4,}"
)

# Ký pháp nằm ngoài tầm của parser LaTeX trong SymPy. Đọc bừa những dạng này
# rồi đem so sánh là cách chắc chắn nhất để báo sai một lời giải đúng:
#   `\partial Q/\partial x`  -> hiểu thành phân số của hai ẩn
#   `\left(\frac{3}{103}\right)` (ký hiệu Legendre) -> hiểu thành 3/103
#   `53,1^{\circ}` -> mất nghĩa "độ"
_UNSUPPORTED_RE = re.compile(
    r"\\partial|\\circ|\\begin\{[a-z]*matrix\}|\\bmod|\\equiv|\\pmod"
    r"|\\(?:sin|cos|tan|cot|sec|csc)\s*\^\s*\{?\s*-?\d+\s*\}?\s+[^({\s]"
    r"|\\overline|\\widehat|\\mathbb|\\nabla|\\oint"
    r"|\)\s*_\s*\{?\s*\d"                       # (2626)_7 — số ở hệ cơ số khác
    r"|\\mathrm\s*\{[^{}]*\\,"                  # \mathrm{mol\,L^{-1}} — đại số đơn vị
    # Tổng và tích vô hạn: `.doit()` trên chúng có thể chạy hàng phút mà vẫn
    # không ra kết quả (chuỗi Fourier, chuỗi Dirichlet). Không đáng đánh đổi.
    r"|\\(?:sum|prod|int)[^\\]{0,40}\\infty|\\cdots|\\ldots|\\dots"
)

# Lời giải nói bằng lời rằng đây là bước giải phương trình / thế số, chứ không
# phải một đồng nhất thức. Khi ấy hai vế cố ý khác nhau và CAS không có tư cách
# kết tội.
_SOLVING_WORDS = (
    "giải phương trình", "giải hệ", "phương trình", "hệ phương trình", "nghiệm",
    "suy ra", "thay vào", "thế vào", "đặt", "đồng nhất", "cân bằng", "so sánh hệ số",
    "điều kiện", "ta có hệ", "từ đó", "rút ra",
)


def _explains_solving(step: object) -> bool:
    text = step.get("explain") if isinstance(step, dict) else getattr(step, "explain", "")
    lowered = (text or "").lower()
    return any(word in lowered for word in _SOLVING_WORDS)


_CONNECTIVE_RE = re.compile(
    r"\\(?:Rightarrow|Longrightarrow|longrightarrow|implies|iff"
    r"|Leftrightarrow|leftrightarrow|therefore)\b"
)


def _fragments(latex: str) -> list[str]:
    parts = [p.strip() for p in _FRAGMENT_RE.split(str(latex))]
    return [p for p in parts if p and p not in {"=", "≈"}]


def _step_latex(step: object) -> str | None:
    value = step.get("latex") if isinstance(step, dict) else getattr(step, "latex", None)
    return str(value) if value and str(value).strip() else None


#: Đơn vị dán ở cuối một vế. Phải bắt được **cả cụm**, không chỉ mẩu cuối:
#: `2{,}416\times10^{-24}\ \text{kg}\cdot\text{m/s}` và `338{,}8\
#: \text{N·m}^{2}/\text{C}` đều là một đơn vị duy nhất viết thành nhiều mẩu.
#: Cắt sót một mẩu thì phần còn lại là `\cdot` hoặc `/` lơ lửng, và vế ấy trở
#: nên không đọc được — mất luôn một bước vốn kiểm được.
_UNIT_ATOM = (
    r"(?:\\mu\s*)?\\(?:mathrm|text|rm|mbox)\s*\{[^{}]*\}"
    r"(?:\s*\^\s*\{?\s*-?\d+\s*\}?)?"
)
_UNIT_SUFFIX_RE = re.compile(
    rf"(?:\\[,;:!\s]|\s)*{_UNIT_ATOM}"
    rf"(?:\s*(?:\\cdot|·|\*|/|\\[,;:!\s])?\s*{_UNIT_ATOM})*\s*$"
)


def _unit_of(side: str) -> str | None:
    """Đơn vị viết ở cuối một vế, hoặc None nếu vế ấy không ghi đơn vị."""
    match = _UNIT_SUFFIX_RE.search(side or "")
    if not match:
        return None
    text = re.sub(r"\\(?:mathrm|text|rm|mbox)\s*\{([^{}]*)\}", r"\1", match.group(0))
    text = text.replace("\\mu", "µ").replace("\\cdot", "*").replace("·", "*")
    text = re.sub(r"\\[,;:!]|\\\s", " ", text)
    text = re.sub(r"\^\s*\{\s*(-?\d+)\s*\}", r"^\1", text)
    return re.sub(r"\s+", "", text).strip("*") or None


def _chain_units(latex: str) -> list[str | None]:
    """Đơn vị của từng vế trong một mắt xích, đọc từ chuỗi CHƯA gọt."""
    return [_unit_of(part) for part in split_equation(latex, clean=False)]


def _unit_converted_match(left: str, right: str, unit_a: str, unit_b: str) -> bool | None:
    """Hai vế có phải cùng một đại lượng viết ở hai đơn vị khác nhau không?

    `0{,}0252\\ \\mathrm{g} = 25{,}2\\ \\mathrm{mg}` là một phép **đổi đơn vị**
    hoàn toàn đúng. Gỡ đơn vị đi rồi so số thì thành `0,0252 ≠ 25,2` — lệch 999
    lần, và một lời giải đúng bị bác bỏ dứt khoát.

    Trả None khi không đủ căn cứ (Pint không hiểu đơn vị chuyên ngành như `cM`,
    `bp`, `phut`). None ở đây nghĩa là "chưa kiểm được", và người gọi phải hiểu
    nó là lí do để **thôi kết tội**, chứ không phải bằng chứng sai.
    """
    from .units import convert

    value_a = to_number(to_sympy(_UNIT_SUFFIX_RE.sub("", left)))
    value_b = to_number(to_sympy(_UNIT_SUFFIX_RE.sub("", right)))
    if value_a is None or value_b is None:
        return None
    converted = convert(value_a, unit_a, unit_b)
    if converted is None:
        return None
    ok, _ = numbers_match(converted, value_b, _STEP_ROUNDING_TOLERANCE)
    return bool(ok or _numbers_agree_after_rounding(converted, value_b))


# Quan hệ chỉ **khẳng định** được, không bao giờ được kết tội.
#
# `≈` theo nghĩa đen là "xấp xỉ": lời giải có quyền viết `\sqrt{1+x} \approx
# 1 + x/2` hay `\frac{2pq}{q^2} \approx \frac{2}{q}` rồi bỏ đi một số hạng. Hai
# vế lệch nhau ở đó là **cố ý**, không phải lỗi.
#
# Bất đẳng thức còn nguy hiểm hơn. Trong kho có bước liệt kê phản ví dụ:
# `n=1: 2>1 (đúng); n=2: 4>4 (sai); n=3: 8>9 (sai)` — lời giải cố tình viết ra
# những bất đẳng thức SAI để chỉ ra mệnh đề hỏng từ đâu. Kết tội theo dấu `>` ở
# đó là báo oan một lời giải hoàn toàn đúng. Cùng lí do với `\le`: nó thường là
# một cận đang được chứng minh, không phải phép so hai con số đã biết.
#
# Không phải phỏng đoán: đo trên 120 bài, nếu cho phép kết tội theo hai quan hệ
# này thì có 7 mắt xích bị bác bỏ, và đọc tay cả bảy đều là lời giải đúng.
_NUMERIC_ONLY_OPS = ("≈", "<", ">", "<=", ">=")

#: Chú thích chữ trong một dòng: `\text{m}`, `\mathrm{cm}`, `\text{ khi }`.
_ANNOTATION_GROUP_RE = re.compile(r"\\(?:text|textrm|mathrm|rm|mbox|operatorname)\s*\{([^{}]*)\}")


def _looks_like_unit_label(label: str) -> bool:
    r"""Nhãn này trông giống một ĐƠN VỊ, hay là công thức hoá học / tên đại lượng?

    Phân biệt này quyết định lớp châm chước bên dưới có mở ra hay không, nên nó
    phải hẹp: `\mathrm{H_2SO_4}` mà bị tính là "đơn vị" thì mọi dòng Hoá có hai
    công thức trở lên đều được miễn kết tội, và một phép nhân sai nằm ngay cạnh
    phương trình phản ứng sẽ lọt lưới. Đơn vị viết bằng ASCII, không có chỉ số
    dưới, không có chữ số, và gồm toàn từ rất ngắn (`kJ/mol`, `m/s`, `cm`).
    """
    text = (label or "").strip()
    if not text or "_" in text or any(ch.isdigit() for ch in text):
        return False
    if any(ord(ch) > 127 for ch in text if ch.isalpha()):
        return False
    words = [w for w in re.split(r"[^A-Za-z]+", text) if w]
    return bool(words) and all(len(w) <= 4 for w in words)


def _has_mixed_annotations(latex: str) -> bool:
    """Một dòng mang từ hai chú thích chữ khác nhau trở lên?

    Khi ấy dấu `=` giữa chúng rất có thể nối hai cách viết của **cùng một đại
    lượng ở hai đơn vị** (m và mm, năm và tỉ năm). Lớp quy đổi đơn vị bên dưới
    xử lí được những cụm đơn vị dán đuôi mà Pint hiểu; đây là lưới đỡ cho phần
    còn lại — chú thích nằm giữa dòng, đơn vị tiếng Việt, tên chất. Chỉ chặn
    đường kết tội; xác nhận thì vẫn cho phép, vì hai vế bằng nhau về số là bằng
    chứng thuận chứ không phải bằng chứng buộc tội.
    """
    groups = {
        re.sub(r"\s+", "", g)
        for g in _ANNOTATION_GROUP_RE.findall(latex or "")
        if _looks_like_unit_label(g)
    }
    groups.discard("")
    return len(groups) > 1


#: Chỉ tên lệnh LaTeX (`\frac`, `\pi`, `\sqrt`) mới được phép có chữ cái trong
#: một vế "số thuần". Chữ cái trần thì không.
_LATEX_CMD_RE = re.compile(r"\\[A-Za-z]+")
_LETTER_RE = re.compile(r"[A-Za-z]")


def _is_plain_numeric_text(part: str) -> bool:
    """Vế này có phải biểu thức số thuần, không lẫn ký hiệu nào?

    Hàng rào chống một kiểu báo động giả rất khó thấy: `clean_latex` gỡ
    `\\text{...}` đi, nên `V'(t) > 0 \\text{ khi } t < 4` còn lại
    `V'(t) > 0 t < 4`. Vế giữa `0 t` **tính ra số 0** vì SymPy rút gọn `0*t`
    ngay lúc đọc, và ta sẽ "xác nhận" được `0 < 4` — một phép so chẳng có trong
    lời giải. Chỉ cần thấy chữ cái trần là biết vế ấy không phải một con số.
    """
    return not _LETTER_RE.search(_LATEX_CMD_RE.sub(" ", part or ""))


def _numeric_side(text: str, expr: sp.Expr | None) -> float | None:
    """Giá trị số của một vế, hoặc None nếu vế ấy không phải một con số."""
    if expr is None or not _is_plain_numeric_text(text):
        return None
    # Parser trả `\pi` về ký hiệu tự do, nên `S = 4\pi \approx 12{,}5664` mất
    # trắng. Chỉ thay khi π không đứng một mình: trong Thống kê `\pi` là tỉ lệ
    # tổng thể. Đường này chỉ dẫn tới verified/unknown nên nhầm cũng không kết
    # tội ai.
    if isinstance(expr, sp.Expr) and expr != _PI_SYMBOL and _PI_SYMBOL in expr.free_symbols:
        expr = expr.xreplace({_PI_SYMBOL: sp.pi})
    value = to_number(run_guarded(lambda e=expr: e.doit(), expr))
    return value if value is not None and math.isfinite(value) else None


def _chain_numbers(
    parts: list[str], exprs: list[sp.Expr | None], ops: list[str]
) -> list[float | None]:
    """Giá trị số của từng vế, có giải luôn các nhãn được đặt ngay trong chuỗi.

    `p = 0{,}140 < d_{JC} = 0{,}1550` là một khẳng định kiểm được, nhưng mắt
    xích ở giữa lại là `0{,}140 < d_{JC}` — một con số so với một ký hiệu. Cái
    ký hiệu ấy vừa được chính chuỗi này gán giá trị ở mắt xích liền kề, nên
    dùng lại là chính đáng: nguồn của giá trị nằm ngay trong bước đang kiểm.
    """
    values = [_numeric_side(p, e) for p, e in zip(parts, exprs, strict=True)]
    for index, expr in enumerate(exprs):
        # Chỉ nhãn trần mới được thay. `2x` hay `a+b` cũng có một ẩn nhưng
        # không phải tên của một giá trị đã công bố.
        if values[index] is not None or not isinstance(expr, sp.Symbol):
            continue
        for neighbour, op_index in ((index + 1, index), (index - 1, index - 1)):
            if not 0 <= neighbour < len(values) or not 0 <= op_index < len(ops):
                continue
            if ops[op_index] == "=" and values[neighbour] is not None:
                values[index] = values[neighbour]
                break
    return values


def _relation_verdict(
    op: str,
    left: sp.Expr | None,
    right: sp.Expr | None,
    na: float | None,
    nb: float | None,
    *,
    env: SymbolEnv | None = None,
    defined_here: frozenset[str] = frozenset(),
) -> tuple[Equivalence, str]:
    """Kết luận cho MỘT mắt xích, theo đúng quan hệ của chính mắt xích ấy."""
    if op == "=":
        return equivalent(left, right, env=env, defined_here=defined_here)
    if op not in _NUMERIC_ONLY_OPS:
        return "unknown", f"quan hệ `{op}` không kiểm được bằng CAS"
    if na is None or nb is None:
        return "unknown", f"hai vế của `{op}` không cùng quy về số được"

    close = _numbers_agree_after_rounding(na, nb)
    if op == "≈":
        if close:
            return "equivalent", f"{na:.10g} ≈ {nb:.10g} (khớp trong sai số làm tròn)"
        return "unknown", (
            f"{na:.10g} và {nb:.10g} lệch quá mức làm tròn, nhưng `≈` vốn cho phép"
            " bỏ bớt số hạng nên không đủ căn cứ kết tội"
        )
    # Với bất đẳng thức, "không phân biệt nổi" phải đo bằng sai số **tương đối**,
    # không bằng số chữ số người viết gõ ra. `10^{-6}` viết một chữ số có dung
    # sai tới 5·10⁻⁷, nên `7{,}28\times10^{-7} \le 10^{-6}` — lệch 27%, rõ ràng
    # đúng — sẽ bị coi là "hai số bằng nhau". Ngược lại nếu dùng dung sai rộng ấy
    # để KHẲNG ĐỊNH thì `4 \ge 4{,}4` cũng lọt.
    _, relative = numbers_match(na, nb, _STEP_ROUNDING_TOLERANCE)
    if relative is not None and relative <= _STEP_ROUNDING_TOLERANCE:
        return "unknown", f"{na:.10g} và {nb:.10g} sát nhau quá, không kết luận chiều `{op}`"
    holds = {"<": na < nb, ">": na > nb, "<=": na <= nb, ">=": na >= nb}[op]
    if holds:
        return "equivalent", f"{na:.10g} {op} {nb:.10g} đúng"
    return "unknown", (
        f"{na:.10g} {op} {nb:.10g} không đúng với hai số đọc được — vẫn không kết tội,"
        " vì lời giải có quyền viết ra một bất đẳng thức sai để chỉ ra nó sai"
    )


def _ratio_is_power_of_ten(left: str, right: str) -> bool:
    """Hai vế có lệch nhau đúng một bội số mười không?

    Đây là dấu hiệu của một lần đổi tiền tố đơn vị không viết ra (J sang kJ, g
    sang mg). Mọi tỉ số khác thì đơn vị không giải thích được, và chênh lệch ấy
    là lỗi tính thật.
    """
    value_a = to_number(to_sympy(_UNIT_SUFFIX_RE.sub("", left)))
    value_b = to_number(to_sympy(_UNIT_SUFFIX_RE.sub("", right)))
    if not value_a or not value_b:
        return False
    try:
        ratio = abs(value_a / value_b)
        exponent = round(math.log10(ratio))
    except (ValueError, ZeroDivisionError, OverflowError):
        return False
    if not 0 < abs(exponent) <= 12:
        return False
    # Dung sai làm tròn, không phải bằng chính xác: `2577\times(-7{,}601)` ra
    # -19588,8 còn vế kia ghi -19,59, nên tỉ số là 999,94 chứ không phải 1000.
    return numbers_match(10.0**exponent, ratio, _STEP_ROUNDING_TOLERANCE)[0]


#: Dấu đóng vào lí do khi kết luận đến từ bộ kiểm hoá học, để `check_steps` phân
#: biệt được với kết luận của SymPy.
#:
#: Vì sao cần phân biệt: một bước Hoá gần như luôn kích hoạt `derivation` (chữ
#: "cân bằng", "phản ứng", "suy ra" nằm sẵn trong `_SOLVING_WORDS`), và với
#: `derivation` thì mọi kết luận "different" bị hạ xuống "inconclusive". Hàng rào
#: ấy đúng cho SymPy — `r^2 = 5r - 6 \iff ...` là phương trình đang giải nên hai
#: vế cố ý khác nhau. Nhưng mũi tên phản ứng KHÔNG mang nghĩa ấy: nó khẳng định
#: bảo toàn khối lượng, và không câu chữ nào trong lời giải làm cho một phương
#: trình lệch nguyên tử thành đúng. Để nguyên hàng rào thì khả năng bắt lỗi cân
#: bằng — lí do tồn tại của cả module này — sẽ không bao giờ kích hoạt, mà lại
#: không có lỗi nào báo ra. Đúng loại hỏng im lặng README dặn phải tránh.
_CHEM_MARK = "[hoá] "

#: Đóng vào lí do khi một mâu thuẫn bị hàng rào hạ xuống "chưa kết luận". Phải
#: đi ngược lên tận `check_steps`: một dòng thường gồm nhiều mệnh đề độc lập
#: (`\qquad`, `;`), và mệnh đề này bị bịt miệng trong khi mệnh đề kia kiểm được
#: thì cả bước vẫn không đáng dán nhãn "đã kiểm".
_SILENCED_MARK = "[treo] "

#: Mẩu còn lại của dòng có phép so nào không? Có thì nhánh hoá học không được
#: kết luận thay cho cả mắt xích.
#: Phải có CẢ quan hệ lẫn một phép toán: `n = 5 \times 3 = 16` là phép tính có
#: thể sai, còn `n_{NaOH} = 0{,}2` chỉ là một giá trị được đặt tên — chặn nhánh
#: hoá học vì nó thì mất luôn khả năng kiểm cân bằng của cả dòng.
_RELATION_LEFTOVER_RE = re.compile(
    r"(?=.*(?:[=<>]|\\approx|\\leq|\\geq|≈|≤|≥))"
    r".*(?:[+/]|\\times|\\cdot|\\div|\\frac|\\dfrac|\\tfrac|\\sqrt|(?<=\d)\s*-\s*(?=\d))",
    re.S,
)


def _check_chemistry(latex: str) -> tuple[Equivalence, str] | None:
    """Bước này có phải phương trình hoá học không? Không chắc thì trả `None`.

    Chú thích sau dấu `:` rất phổ biến trong kho Hoá
    (`... \\to ... :\\ n_{NaOH} = 0{,}2`), nên thử từng mẩu chứ không đòi cả dòng
    phải là phương trình.

    Nhưng chỉ được đoản mạch cả mắt xích khi **không mẩu nào khác còn phép tính
    để kiểm**. Một dòng như `2H_2 + O_2 \\to 2H_2O :\\ n = 5 \\times 3 = 16` mà trả
    "cân bằng" ngay thì nhánh SymPy không bao giờ chạy, và phép nhân sai nằm
    ngay cạnh được đóng dấu "đã kiểm" — xác nhận khống, đúng loại nguy hiểm nhất.
    """
    pieces = latex.split(":")
    for index, piece in enumerate(pieces):
        verdict, reason = check_equation(piece)
        if verdict == "unknown":
            continue
        others = [p for position, p in enumerate(pieces) if position != index]
        if any(_RELATION_LEFTOVER_RE.search(other) for other in others):
            return None  # còn phép tính bên cạnh: để nhánh CAS trả lời
        if verdict == "balanced":
            return "equivalent", _CHEM_MARK + reason
        return "different", _CHEM_MARK + reason
    return None


# Ký pháp thay cận: `\left. t^{2} \right|_{0}^{1}`. Parser LaTeX **im lặng nuốt
# sạch phần từ dấu gạch trở đi**: `1 + .t^{2}|_{0}^{1}` được đọc thành đúng số
# `1`. Không lỗi nào ném ra, chỉ còn một con số sai đem đi so — và nó lệch đúng
# bằng giá trị của tích phân, tức là lệch nhiều, tức là đủ để kết tội một lời
# giải hoàn toàn đúng.
#
# Chặn ở mức TỪNG VẾ chứ không bỏ cả bước: một bước như
# `x(1) = 1 + \int_{0}^{1}2t\,dt = 1 + \left.t^{2}\right|_{0}^{1} = 1 + 1 = 2`
# vẫn còn khâu `1 + 1 = 2` kiểm được đàng hoàng.
#
# Chỉ bắt dấu gạch mang **chỉ số dưới** (`|_{a}^{b}`, `\big|_{t=1}`). Dấu gạch
# mang số mũ thì lại là dấu giá trị tuyệt đối: `|z_1|^2 = 13`, `|V_{fi}|^{2}` —
# parser đọc đúng thành `Abs(...)**2`, chặn nhầm ở đó là vứt đi những vế hoàn
# toàn đọc được.
_MANGLED_PART_RE = re.compile(r"\|\s*_")


def _definienda(exprs: list[sp.Expr | None]) -> frozenset[str]:
    r"""Các ký hiệu đang được ĐỊNH NGHĨA bởi chính mắt xích này.

    Một vế chỉ gồm đúng một ký hiệu trần (`\omega_c = ...`) là vế đang được gán,
    không phải vế cần thay. Thay ràng buộc cũ vào đúng chỗ ấy là cách sinh ra
    lời kết tội bịa gọn gàng nhất: một phép gán lại hoàn toàn hợp lệ (`x = 7`
    sau khi `x = 5`) sẽ hoá thành `5 = 7`.
    """
    return frozenset(str(e) for e in exprs if isinstance(e, sp.Symbol))


def _excuse_units(
    verdict: Equivalence,
    reason: str,
    raw: list[str],
    units: list[str | None],
    index: int,
    converts_units: bool,
    aligned: bool,
) -> tuple[Equivalence, str]:
    """Chênh lệch ở mắt xích này có thể chỉ là một phép **đổi đơn vị** không?

    Hai lớp, từ chắc chắn tới phòng xa:

    1. Cả hai vế có đơn vị dán đuôi và Pint quy đổi được ⇒ trả lời dứt khoát,
       kể cả xác nhận. `0{,}0252\\ \\mathrm{g} = 25{,}2\\ \\mathrm{mg}` là đúng,
       và nói được là đúng chứ không phải chỉ "chưa kết luận".
    2. Chỉ một vế ghi đơn vị, hoặc dòng có nhiều chú thích chữ khác nhau ⇒ chỉ
       chặn đường kết tội. Ở đây ta không biết đủ để phán gì cả, mà gỡ đơn vị ra
       khỏi một vế thì có thể đã đổi luôn độ lớn của nó.
    """
    if aligned:
        unit_a, unit_b = units[index], units[index + 1]
        if unit_a and unit_b and unit_a != unit_b:
            matched = _unit_converted_match(raw[index], raw[index + 1], unit_a, unit_b)
            if matched is True:
                return "equivalent", f"cùng đại lượng, đổi {unit_a} sang {unit_b}"
            return "unknown", (
                f"hai vế viết ở hai đơn vị khác nhau ({unit_a}, {unit_b}) —"
                " là bước đổi đơn vị, không so thẳng hai con số được"
            )
        # Chỉ một vế ghi đơn vị: vế kia có thể đang ở một bội số khác mà không
        # nói ra (`2577\times(-7{,}601) = -19{,}59\ \mathrm{kJ/mol}` để vế giữa
        # ở J/mol). Cái cớ ấy chỉ dùng được khi tỉ số ĐÚNG là một bội số mười —
        # nếu không thì đơn vị chẳng giải thích được gì, và
        # `9{,}000 \times 26{,}43 = 26{,}43\ \mathrm{kJ}` vẫn phải bị bác bỏ.
        if (bool(unit_a) != bool(unit_b)) and _ratio_is_power_of_ten(raw[index], raw[index + 1]):
            return "unknown", (
                f"chỉ một vế ghi đơn vị ({unit_a or unit_b}) và hai vế lệch nhau đúng một"
                " bội số mười — nhiều khả năng là đổi tiền tố chứ không phải lỗi tính"
            )

    if converts_units:
        return "unknown", (
            f"{reason} — nhưng dòng này có nhiều đơn vị/chú thích khác nhau,"
            " chênh lệch ấy có thể chỉ là một phép quy đổi đơn vị"
        )
    return verdict, reason


def _check_chain(
    latex: str,
    carry: str | None,
    env: SymbolEnv | None = None,
    scope: FunctionScope | None = None,
) -> tuple[Equivalence, str, str | None]:
    """Kiểm một mắt xích `a = b ≈ c < d`. Trả (kết luận, lí do, vế cuối)."""
    # Đổi độ sang radian TRƯỚC khi hỏi danh sách chặn, để bước chỉ còn bị chặn
    # khi trong nó thật sự còn một `\circ` chưa hiểu được nghĩa.
    source = latex
    latex = normalise_degrees(latex)

    # Hoá học đi trước: một phương trình phản ứng không có dấu `=` nào nên lối
    # kiểm bằng SymPy phía dưới chỉ trả được "chỉ có một vế, không có gì để đối
    # chiếu" — đúng nhóm chiếm 17% số bước chưa kết luận được.
    chemical = _check_chemistry(latex)
    if chemical is not None:
        return chemical[0], chemical[1], None

    if _UNSUPPORTED_RE.search(latex):
        parts = split_equation(latex)
        return "unknown", "ký pháp nằm ngoài tầm của parser LaTeX, không kết luận", (
            parts[-1] if parts else None
        )

    # Mọi lời gọi hàm nhận ra được thành **nguyên tử mờ** trước khi tách vế.
    # Trước đây gặp `P(X = 4)` hay `f(1)` là bỏ nguyên mắt xích, nên khâu thuần
    # số `0{,}343 \times 0{,}3 = 0{,}1029` nằm cùng dòng cũng mất theo.
    if scope is not None:
        latex = scope.rewrite(latex)

    parts, ops = split_relations(latex)
    raw, raw_ops = split_relations(latex, clean=False)
    if parts and not parts[0] and ops:
        # Bước nối tiếp mở đầu bằng quan hệ (`= \frac{x+3}{x-2}`): vế trái của
        # nó là vế phải của bước trước. Chỉ được nối khi chuỗi **thô** cũng mở
        # đầu bằng quan hệ — `\text{cận dưới} = 16 + 5 + 8` sau khi gỡ chú thích
        # cũng bắt đầu bằng `=`, nhưng vế trái của nó là cái nhãn vừa bị gỡ, và
        # nối nó vào bước trước là dựng ra một đẳng thức không ai viết.
        if carry and starts_with_relation(latex):
            parts[0] = carry
        else:
            parts, ops = parts[1:], ops[1:]
            raw, raw_ops = (raw[1:], raw_ops[1:]) if raw else (raw, raw_ops)

    # Vế cuối chỉ được mang sang bước sau khi mắt xích cuối là một đẳng thức.
    # Sau `n = 12 < 30` thì "vế phải cuối cùng" là một cận chứ không phải giá
    # trị của `n`; nối nó vào bước sau là dựng ra một đẳng thức không ai viết.
    tail = parts[-1] if parts and (not ops or ops[-1] == "=") else None
    if len(parts) < 2:
        return "unknown", "chỉ có một vế, không có gì để đối chiếu", tail

    # Đơn vị đọc từ chuỗi CHƯA gọt, chỉ dùng được khi hai lần tách khớp nhau.
    aligned = len(raw) == len(parts) and raw_ops == ops
    units = [_unit_of(part) for part in raw] if aligned else [None] * len(parts)

    # Độ cũng là một đơn vị, và một mắt xích có thể **trộn** hai cách ghi:
    #
    #   \theta_1 = 6{,}0^{\circ}\cdot 4^{3/4} = 6{,}0\cdot 2{,}8284 = 16{,}97^{\circ}
    #
    # Vế giữa viết trần (ngầm hiểu là độ), hai vế kia có mũ tròn và đã được đổi
    # sang radian. So thẳng thì lệch đúng 180/π lần và một lời giải đúng bị bác
    # bỏ. Đọc trên chuỗi GỐC vì `normalise_degrees` đã xoá dấu vết ở phía trên.
    degrees = [False] * len(parts)
    if aligned:
        source_parts, source_ops = split_relations(source, clean=False)
        if len(source_parts) == len(parts) and source_ops == ops:
            degrees = ["\\circ" in part for part in source_parts]

    # `\mathrm{V}` được `clean_latex` gỡ vỏ thành ký hiệu `V`, nên `0{,}02671\
    # \mathrm{V}` thành `0.02671*V` — một biểu thức còn ẩn, và cả mắt xích tuột
    # sang "chưa kết luận" dù hai vế đều là số. Vế nào có đơn vị dán đuôi thì
    # đọc phần số của nó, rồi để phần đơn vị cho lớp đổi đơn vị bên dưới lo.
    exprs: list[sp.Expr | None] = []
    for index, part in enumerate(parts):
        if _MANGLED_PART_RE.search(part):
            exprs.append(None)  # vế bị parser nuốt mất, không đem ra so
            continue
        expr = None
        if units[index]:
            expr = to_sympy(_UNIT_SUFFIX_RE.sub("", raw[index]))
        exprs.append(expr if expr is not None else (to_sympy(part) if part else None))
    if all(e is None for e in exprs):
        return "unknown", "CAS không đọc được biểu thức", tail

    # Thế định nghĩa hàm nếu bắt được ở bước khác: `f(x) = x^2+1` rồi `f(5) = 26`.
    substituted = [False] * len(exprs)
    if scope is not None:
        resolved = [scope.resolve(e) for e in exprs]
        exprs = [e for e, _ in resolved]
        substituted = [used for _, used in resolved]

    defined_here = _definienda(exprs)
    numbers: list[float | None] = (
        _chain_numbers(parts, exprs, ops) if any(op != "=" for op in ops) else [None] * len(parts)
    )
    converts_units = _has_mixed_annotations(latex)

    # CAS đã nhìn thấy hai vế lệch nhau ở một mắt xích nào đó, nhưng bị một hàng
    # rào bịt miệng (đơn vị khác nhau, độ trộn số trần, `≈`, hàm chưa định
    # nghĩa). Đó là **chưa kết luận được**, không phải bằng chứng thuận — nên
    # một mắt xích khác kiểm được cũng không đủ để đóng dấu "đã kiểm" cho cả
    # bước. Thiếu cờ này thì một dòng vừa chứa mâu thuẫn thật vừa chứa một khâu
    # phụ đúng sẽ hiện ra là "verified", đúng kiểu xác nhận khống tệ nhất.
    silenced = False

    verdicts: list[tuple[Equivalence, str]] = []
    for index, op in enumerate(ops):
        if not parts[index] or not parts[index + 1]:
            verdicts.append(("unknown", "một vế rỗng, không có gì để đối chiếu"))
            continue
        verdict, reason = _relation_verdict(
            op,
            exprs[index],
            exprs[index + 1],
            numbers[index],
            numbers[index + 1],
            env=env,
            defined_here=defined_here,
        )
        raw_verdict = verdict
        if verdict == "different" and (substituted[index] or substituted[index + 1]):
            # Định nghĩa hàm có thể chỉ đúng trên một miền (`f` cho theo từng
            # khoảng), hoặc là một hàm khác trùng tên. Xác nhận thì cứ xác nhận;
            # kết tội thì không đủ tư cách.
            verdict, reason = "unknown", (
                "hai vế lệch nhau sau khi thế định nghĩa hàm — định nghĩa có thể chỉ"
                " đúng trên một miền, chưa đủ căn cứ kết tội"
            )
        elif verdict == "different" and (
            has_opaque_atom(exprs[index]) or has_opaque_atom(exprs[index + 1])
        ):
            verdict, reason = "unknown", "khâu có hàm chưa định nghĩa, không đủ căn cứ kết tội"
        elif verdict == "unknown" and (
            has_opaque_atom(exprs[index]) or has_opaque_atom(exprs[index + 1])
        ):
            names = ""
            if scope is not None:
                names = scope.describe(exprs[index]) or scope.describe(exprs[index + 1])
            reason = (
                f"có áp dụng hàm chưa định nghĩa ({names}) nên khâu này không đối chiếu được"
                if names
                else "có áp dụng hàm chưa định nghĩa nên khâu này không đối chiếu được"
            )
        elif verdict == "different" and degrees[index] != degrees[index + 1]:
            verdict, reason = "unknown", (
                "một vế ghi độ còn vế kia viết số trần — không so thẳng được,"
                " vì độ đã được đổi sang radian trước khi tính"
            )
        elif verdict == "different":
            verdict, reason = _excuse_units(
                verdict, reason, raw, units, index, converts_units, aligned
            )
        # Chỉ tính là "bịt miệng" khi mâu thuẫn bị hạ xuống **chưa kết luận**.
        # Nếu hàng rào giải thích được nó thành `equivalent` (quy đổi đơn vị
        # khớp) thì mâu thuẫn ấy đã được trả lời, không còn gì treo lại.
        if verdict == "unknown" and raw_verdict == "different":
            silenced = True
        verdicts.append((verdict, reason))
    if not verdicts:
        return "unknown", "chỉ có một vế, không có gì để đối chiếu", tail

    if any(v == "different" for v, _ in verdicts):
        return "different", next(d for v, d in verdicts if v == "different"), tail
    # Một mắt xích thường trộn cả thế số lẫn biến đổi: `x = 3 + 3 = 6` có khâu
    # `x = 3+3` không kiểm được và khâu `3+3 = 6` kiểm được. Xác nhận được một
    # khâu đã là có căn cứ, miễn là không khâu nào bị bác bỏ.
    if any(v == "equivalent" for v, _ in verdicts) and not silenced:
        return "equivalent", next(d for v, d in verdicts if v == "equivalent"), tail
    if silenced:
        return "unknown", _SILENCED_MARK + next(
            (d for v, d in verdicts if v == "unknown"), "có mâu thuẫn chưa giải thích được"
        ), tail
    return "unknown", verdicts[0][1], tail


def _learn_definitions(steps: list, scope: FunctionScope) -> None:
    """Lượt quét đầu: nhặt mọi định nghĩa hàm của cả lời giải.

    Quét trọn một lượt trước khi kiểm, chứ không vừa đi vừa học. Lí do là hàm
    cho theo từng khoảng: `f(x) = 3x - 1` ở bước 1 và `f(x) = ax^2 + b` ở bước 4
    là hai nhánh của cùng một hàm, và chỉ khi đã nhìn hết mới biết cái tên `f`
    có bị định nghĩa hai kiểu hay không. Học tới đâu dùng tới đó thì các bước ở
    giữa vẫn kịp thế nhầm nhánh.
    """
    for step in steps:
        if out_of_time():
            return
        latex = _step_latex(step)
        if latex is None or _UNSUPPORTED_RE.search(latex):
            continue
        for fragment in _fragments(latex):
            scope.learn(fragment)


def check_steps(
    steps: list[dict] | list,
    *,
    max_steps: int = 24,
    given: Mapping[str, float] | None = None,
) -> list[StepCheck]:
    """Kiểm từng bước biến đổi trong lời giải.

    Lời giải trong kho viết theo lối nối tiếp: bước sau có thể mở đầu bằng dấu
    `=` để nối vào vế phải của bước trước. Hàm này dựng lại chuỗi đó rồi bắt
    SymPy xác nhận mọi vế trong cùng một mắt xích thực sự bằng nhau.
    """
    checks: list[StepCheck] = []
    carry: str | None = None  # vế phải cuối cùng của bước trước
    # Môi trường chỉ tích luỹ theo chiều xuôi — kiểm xong bước i mới nạp các gán
    # của bước i — nên không bao giờ dùng một ràng buộc đặt ở phía sau để phán
    # về phía trước.
    env = SymbolEnv(given)
    # Sổ tay hàm dùng chung cho cả lời giải: cùng một lời gọi phải ra cùng một
    # nguyên tử ở mọi bước, nếu không thì chuỗi nối tiếp giữa các bước đứt.
    scope = FunctionScope()
    _learn_definitions(steps[:max_steps], scope)

    for index, step in enumerate(steps[:max_steps]):
        if out_of_time():
            checks.append(
                StepCheck(index=index, latex=_step_latex(step), status="skipped",
                          detail="hết thời gian kiểm chứng, bỏ qua bước này")
            )
            continue

        latex = _step_latex(step)
        if latex is None:
            checks.append(
                StepCheck(index=index, latex=None, status="skipped",
                          detail="bước không có biểu thức")
            )
            continue

        # Bước có liên từ logic là một chuỗi suy luận, không phải một đồng nhất
        # thức: `r^2 = 5r - 6 \iff r^2 - 5r + 6 = 0` là phương trình đang giải,
        # hai vế cố ý khác nhau. Ở những bước như thế ta chỉ xác nhận, không
        # bao giờ kết tội.
        derivation = bool(_CONNECTIVE_RE.search(latex)) or _explains_solving(step)

        results: list[tuple[Equivalence, str]] = []
        parsed_any = False
        for fragment in _fragments(latex):
            verdict, reason, tail = _check_chain(fragment, carry, env, scope)
            if tail:
                carry = tail
            if reason != "CAS không đọc được biểu thức":
                parsed_any = True
            results.append((verdict, reason))
            # Nạp sau khi đã kiểm: mảnh sau trong cùng một dòng được dùng ràng
            # buộc của mảnh trước (`s_{d} = 1{,}9014 ; SE = \frac{...}{...}`),
            # còn mảnh đang kiểm thì không tự chứng minh bằng chính nó.
            env.record(split_relations(fragment)[0], fragment)

        # Khối lượng mol đọc trên cả dòng chứ không theo mắt xích: `M_{H_2SO_4}`
        # và giá trị của nó phải nhìn cùng lúc mới đối chiếu được với bảng
        # nguyên tử khối.
        molar_verdict, molar_reason = check_molar_mass(latex)
        if molar_verdict == "balanced":
            results.append(("equivalent", _CHEM_MARK + molar_reason))
            parsed_any = True
        elif molar_verdict == "unbalanced":
            results.append(("different", _CHEM_MARK + molar_reason))
            parsed_any = True

        # Kết tội của bộ kiểm hoá học không đi qua hàng rào `derivation` — xem
        # chú thích ở `_CHEM_MARK`.
        chemical_refutation = next(
            (d for v, d in results if v == "different" and d.startswith(_CHEM_MARK)), None
        )

        if not results:
            checks.append(
                StepCheck(index=index, latex=latex, status="skipped", detail="bước rỗng")
            )
        elif chemical_refutation is not None:
            checks.append(
                StepCheck(index=index, latex=latex, status="refuted",
                          detail=chemical_refutation.removeprefix(_CHEM_MARK))
            )
        elif any(v == "different" for v, _ in results) and not derivation:
            reason = next(d for v, d in results if v == "different")
            checks.append(
                StepCheck(index=index, latex=latex, status="refuted",
                          detail=f"hai vế không bằng nhau: {reason}")
            )
        elif any(v == "different" for v, _ in results):
            checks.append(
                StepCheck(index=index, latex=latex, status="inconclusive",
                          detail="bước suy luận có liên từ logic — hai vế không cần bằng nhau")
            )
        elif any(d.startswith(_SILENCED_MARK) for _, d in results):
            reason = next(d for _, d in results if d.startswith(_SILENCED_MARK))
            checks.append(
                StepCheck(index=index, latex=latex, status="inconclusive",
                          detail=reason.removeprefix(_SILENCED_MARK))
            )
        elif any(v == "equivalent" for v, _ in results):
            # Ưu tiên lí do của bộ kiểm hoá học: "phương trình cân bằng nguyên
            # tử" nói rõ đã kiểm được cái gì hơn hẳn "trùng khớp về cấu trúc".
            reasons = [d for v, d in results if v == "equivalent"]
            reason = next((d for d in reasons if d.startswith(_CHEM_MARK)), reasons[0])
            checks.append(
                StepCheck(index=index, latex=latex, status="verified",
                          detail=reason.removeprefix(_CHEM_MARK))
            )
        elif not parsed_any:
            checks.append(
                StepCheck(index=index, latex=latex, status="unparsed",
                          detail="CAS không đọc được biểu thức của bước này")
            )
        else:
            checks.append(
                StepCheck(index=index, latex=latex, status="inconclusive",
                          detail=results[0][1])
            )
    return checks


# --------------------------------------------------------------------------- #
# Kiểm đáp số
# --------------------------------------------------------------------------- #

# "(a) N_e = 72; (b) N_e = 357" — đáp án nhiều phần. Con số đầu tiên trong
# chuỗi không phải kết quả cuối của lời giải, nên không được đem ra bác bỏ.
_MULTIPART_RE = re.compile(r"\(\s*[a-dạ-ỹ1-4]\s*\)|;\s*\S|\bphần\b|\bcâu\b", re.IGNORECASE)


def _looks_multipart(answer: str) -> bool:
    return bool(_MULTIPART_RE.search(answer or ""))


#: Đáp án là một khoá trắc nghiệm ("A"…"E") — con số kèm theo trong
#: `answer_numeric` là giá trị của phương án, không phải kết quả bước cuối.
_CHOICE_KEY_RE = re.compile(r"^\s*[A-E]\s*$")


def _answer_is_plain_number(answer: str) -> bool:
    """Đáp án có phải chỉ gồm một con số kèm đơn vị, không có mô tả bằng lời?

    `3,71 × 10^3 s` thì có; `10 số hạng` hay `9,93 năm` thì không — phần chữ
    cho biết con số ấy đếm cái gì, và lời giải thường không kết thúc bằng đúng
    con số đó, nên đem ra đối chiếu sẽ kết tội oan.
    """
    text = (answer or "").strip()
    if not text or _CHOICE_KEY_RE.match(text):
        return False
    remainder = re.sub(
        r"[-+]?(?:\d+(?:[.,]\d+)?|\.\d+)"      # con số
        r"|\\times|\\cdot"                      # dấu nhân LaTeX
        r"|(?<=\d)\s*[eE](?=[-+\d])"            # e của ký hiệu khoa học, không phải chữ e
        r"|[×·*^{}()\[\]/\\,.\s=≈±_]",          # dấu ngăn cách
        " ",
        text,
    )
    words = [w for w in remainder.split() if w]
    for word in words:
        if any(ord(ch) > 127 for ch in word):  # có dấu tiếng Việt -> là chữ, không phải đơn vị
            return False
        if len(word) > 4:  # đơn vị SI dài nhất trong kho là 4 ký tự ("kmol")
            return False
    return True


#: Một vế chỉ gồm đúng một con số, không có phép toán nào.
_BARE_NUMBER_RE = re.compile(r"^[-+]?\d+(?:[.]\d+)?$")


def _numeric_values_in_steps(steps: list) -> list[tuple[int, float, str, bool]]:
    """Mọi giá trị số đọc được từ lời giải, kèm chỉ số bước, theo thứ tự xuất hiện.

    Giữ cả chuỗi chứ không chỉ giá trị cuối: lời giải hay kết thúc bằng một câu
    kết luận bằng chữ, hoặc bằng một đại lượng phụ, nên đáp số thật có thể nằm
    ở bước áp chót.

    Phần tử thứ tư nói giá trị ấy có phải do CAS **tính lại** không. Phân biệt
    này là chuyện trung thực với người đọc, không phải chuyện kỹ thuật: vế đứng
    sau dấu `≈` gần như luôn là một con số trần do chính người viết lời giải gõ
    ra (đã làm tròn sẵn), nên khớp với nó chỉ chứng minh "đáp án công bố ăn khớp
    với các bước", chứ không chứng minh "CAS tính lại ra đúng chừng ấy".
    """
    found: list[tuple[int, float, str, bool]] = []
    for index, step in enumerate(steps):
        if out_of_time():
            break
        latex = _step_latex(step)
        if latex is None or _UNSUPPORTED_RE.search(latex):
            continue
        for fragment in _fragments(latex):
            # Tách theo cả `≈`: kho ghi kết quả đã tính ra ở ngay sau dấu ấy
            # (`SE = \frac{1{,}9014}{\sqrt{12}} \approx 0{,}54889`), nên bỏ qua
            # nó là bỏ mất đúng con số cần đối chiếu với đáp án. Nhưng KHÔNG lấy
            # vế đứng sau một bất đẳng thức: sau `n = 12 < 30` thì `30` là một
            # cận, và đem đáp số đi so với một cận là so nhầm thứ.
            parts, ops = split_relations(fragment)
            if not parts:
                continue
            usable_parts = [
                part
                for position, part in enumerate(parts)
                if position == 0 or ops[position - 1] in ("=", "≈")
            ]
            if not usable_parts:
                continue
            tail = usable_parts[-1]
            for candidate in (tail, strip_trailing_units(tail)):
                expr = to_sympy(candidate)
                if expr is None:
                    continue
                value = to_number(run_guarded(lambda e=expr: e.doit(), expr))
                if value is None or not math.isfinite(value):
                    continue
                computed = not _BARE_NUMBER_RE.match(clean_latex(candidate))
                if not computed:
                    # `40 \cdot 0{,}6 = 24`: vế cuối là con số trần, nhưng một
                    # vế trước nó trong cùng mắt xích tính ra đúng chừng ấy —
                    # nghĩa là CAS thật sự có tính lại, chỉ là kết quả trùng với
                    # con số người viết đã ghi sẵn.
                    computed = any(
                        (other := to_number(to_sympy(part))) is not None
                        and math.isfinite(other)
                        and _numbers_agree_after_rounding(other, value)
                        for part in usable_parts[:-1]
                        if not _BARE_NUMBER_RE.match(clean_latex(part))
                    )
                found.append((index, value, candidate, computed))
                break
    return found


def verify_answer(
    *,
    answer: str,
    answer_numeric: float | None = None,
    steps: list | None = None,
    tolerance: float | None = None,
    expected_unit: str | None = None,
    budget: float | None = None,
) -> Verification:
    """Kiểm chứng đáp số và toàn bộ chuỗi biến đổi của một lời giải.

    `budget` là trần thời gian cho **cả lượt**. Hết ngân sách thì các bước còn
    lại được ghi là "bỏ qua vì hết thời gian" — nói thật ra là chưa kiểm, chứ
    không im lặng coi như đã kiểm.
    """
    token = set_deadline(budget if budget is not None else settings.verify_budget)
    try:
        return _verify_answer(
            answer=answer,
            answer_numeric=answer_numeric,
            steps=steps,
            tolerance=tolerance,
            expected_unit=expected_unit,
        )
    finally:
        reset_deadline(token)


def _verify_answer(
    *,
    answer: str,
    answer_numeric: float | None,
    steps: list | None,
    tolerance: float | None,
    expected_unit: str | None,
) -> Verification:
    result = Verification()
    steps = steps or []

    result.steps = check_steps(steps)
    result.steps_total = len(result.steps)
    result.steps_verified = sum(1 for s in result.steps if s.status == "verified")
    result.steps_refuted = sum(1 for s in result.steps if s.status == "refuted")
    result.steps_inconclusive = sum(1 for s in result.steps if s.status == "inconclusive")

    # Giá trị đáp án mà lời giải công bố.
    claimed = answer_numeric if answer_numeric is not None else extract_number(answer)

    values = _numeric_values_in_steps(steps)
    if values:
        _, result.cas_value, result.cas_expression, _ = values[-1]

    if claimed is None:
        result.answer_status = "unchecked"
        result.answer_detail = "đáp án không phải một giá trị số, chỉ kiểm được các bước biến đổi"
        return result

    if not values:
        result.answer_status = "unchecked"
        result.answer_detail = "CAS không tính lại được giá trị nào từ lời giải để đối chiếu"
        return result

    # Hai chiều kết luận cố ý bất đối xứng. Xác nhận thì rộng tay: khớp ở bất kỳ
    # bước nào cũng tính. Kết tội thì chặt tay: chỉ khi giá trị cuối đến từ một
    # bước mà chính CAS đã xác nhận là đúng. Sai lầm của một bộ kiểm chứng học
    # thuật không cân nhau — báo oan một lời giải đúng còn tệ hơn bỏ sót.
    tol = tolerance if tolerance is not None else settings.default_tolerance
    for position, (_, value, expression, computed) in enumerate(reversed(values)):
        ok, _ = numbers_match(claimed, value, tol)
        if ok or _numbers_agree_after_rounding(claimed, value):
            result.cas_value, result.cas_expression = value, expression
            result.answer_status = "verified"
            where = "bước cuối" if position == 0 else f"bước thứ {len(values) - position}"
            result.answer_detail = (
                f"CAS tính lại được {value:.10g} ở {where}, khớp đáp án công bố"
                if computed
                else f"khớp giá trị {value:.10g} mà chính lời giải công bố ở {where}"
                " — con số ấy do lời giải viết ra, CAS không tính lại được nó"
            )
            return result

    last_index, last_value, last_expression, _ = values[-1]
    last_step_verified = any(
        s.index == last_index and s.status == "verified" for s in result.steps
    )

    if _looks_multipart(answer):
        result.answer_status = "unchecked"
        result.answer_detail = (
            "đáp án gồm nhiều phần, không đối chiếu tự động được với một giá trị số duy nhất"
        )
        return result
    if not _answer_is_plain_number(answer):
        result.answer_status = "unchecked"
        result.answer_detail = (
            "đáp án không phải một con số thuần (là khoá trắc nghiệm hoặc có mô tả bằng lời),"
            " không đủ căn cứ đối chiếu với giá trị CAS tính được"
        )
        return result
    if not last_step_verified:
        result.answer_status = "unchecked"
        result.answer_detail = (
            f"CAS không xác nhận được bước cuối nên không đủ căn cứ kết luận"
            f" (giá trị đọc được ở đó: {last_value:.10g})"
        )
        return result

    _, error = numbers_match(claimed, last_value, tol)
    gap = f" (lệch {error:.3g})" if error is not None else ""
    discrepancy = (
        f"đáp án công bố {claimed:.10g} nhưng giá trị cuối CAS đọc được là "
        f"{last_value:.10g} từ `{last_expression}`{gap}"
    )

    # Kết tội đáp số cần bằng chứng độc lập, không chỉ một phép so giá trị cuối.
    # Lí do: lời giải rất hay kết thúc bằng một đại lượng phụ, một phép kiểm
    # lại, hay một câu kết luận — khi đó "giá trị cuối" không phải đáp số, và
    # bác bỏ dựa vào nó là kết tội oan. Có một bước bị bác bỏ thì mới là bằng
    # chứng thật sự có lỗi số học trong bài.
    if result.steps_refuted:
        result.answer_status = "refuted"
        result.answer_detail = discrepancy + ", và CAS đã bác bỏ một bước biến đổi trong bài"
    else:
        result.answer_status = "unchecked"
        result.answer_mismatch = True
        result.answer_detail = (
            discrepancy
            + " — chưa kết luận sai, vì lời giải có thể kết thúc bằng một đại lượng phụ"
        )

    if expected_unit:
        # Cố ý KHÔNG dùng `check_unit` ở đây. Hàm ấy chấm bài **học sinh**, nơi
        # "thiếu đơn vị" hay "đơn vị lạ" là nhận xét chính đáng. Ở đây cả đáp án
        # lẫn đơn vị đều do kho/mô hình công bố, nên hai chuyện đó chỉ là lối
        # viết — gọi chúng là sai thứ nguyên thì 44% số bài có `answer_unit`
        # trong kho bị báo oan.
        from .dimensions import check_dimension

        status, detail = check_dimension(answer, expected_unit)
        result.unit_status = "unchecked" if status == "unknown" else status
        result.unit_detail = detail

    return result
