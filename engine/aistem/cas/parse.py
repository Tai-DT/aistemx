"""LaTeX → SymPy.

SymPy có hai parser LaTeX: `lark` (mặc định từ 1.13, cho cây sạch hơn) và
`antlr`. Cả hai đều vấp ở những chỗ khác nhau, nên ở đây thử lần lượt cả hai
trên chuỗi đã gọt bằng `textnorm.clean_latex`, lấy kết quả đầu tiên dùng được.
"""

from __future__ import annotations

import itertools
import re
import threading
import time
import warnings
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeout
from contextvars import ContextVar
from typing import Any, TypeVar

import sympy as sp

from ..config import settings
from ..textnorm import clean_latex, split_equation

# SymPy cảnh báo rất ồn khi parser LaTeX dựng ra cây lạ. Ta đã tự lọc bằng
# `usable()` nên tắt hẳn cho đỡ nhiễu log.
warnings.filterwarnings("ignore", module="sympy")
try:  # SymPyDeprecationWarning chỉ có ở bản mới
    from sympy.utilities.exceptions import SymPyDeprecationWarning

    warnings.simplefilter("ignore", SymPyDeprecationWarning)
except Exception:  # pragma: no cover
    pass

T = TypeVar("T")

_EXECUTOR = ThreadPoolExecutor(max_workers=8, thread_name_prefix="cas")

#: Hạn chót của **cả lượt kiểm chứng**, không phải của từng phép tính.
#:
#: Chặn thời gian từng phép là chưa đủ: SymPy không huỷ được giữa chừng, nên
#: mỗi lần quá hạn để lại một luồng vẫn chạy và vẫn ăn CPU. Một lời giải như
#: chuỗi Fourier có hàng chục phép nặng, cộng lại thành nhiều phút và một đống
#: luồng ma. Có hạn chót chung thì lượt kiểm chứng dừng đúng lúc và các bước
#: còn lại được ghi thẳng là "bỏ qua vì hết thời gian".
_DEADLINE: ContextVar[float | None] = ContextVar("aistem_cas_deadline", default=None)


def set_deadline(seconds: float | None) -> object:
    """Đặt hạn chót cho lượt kiểm chứng hiện tại. Trả token để khôi phục."""
    return _DEADLINE.set(None if seconds is None else time.monotonic() + seconds)


def reset_deadline(token: object) -> None:
    _DEADLINE.reset(token)  # type: ignore[arg-type]


def time_left() -> float | None:
    """Số giây còn lại, hoặc None nếu không đặt hạn chót."""
    deadline = _DEADLINE.get()
    return None if deadline is None else deadline - time.monotonic()


def out_of_time() -> bool:
    remaining = time_left()
    return remaining is not None and remaining <= 0


#: Số phép tính CAS được chạy đồng thời. Mỗi lần quá hạn là một luồng **mất
#: hẳn**: SymPy không huỷ được giữa chừng nên luồng ấy chạy tiếp mãi mãi và giữ
#: luôn chỗ của nó.
_MAX_CONCURRENT = 8
_SLOTS = threading.BoundedSemaphore(_MAX_CONCURRENT)
_ABANDONED = itertools.count()
_abandoned_total = 0


def abandoned_count() -> int:
    """Số luồng CAS đã mất vì quá hạn, tính từ lúc tiến trình khởi động."""
    return _abandoned_total


def run_guarded(func: Callable[[], T], default: T, timeout: float | None = None) -> T:
    """Chạy một phép tính CAS có chặn thời gian.

    Hai lớp bảo vệ, và lớp thứ hai mới là lớp quan trọng:

    1. **Chặn thời gian** — quá hạn thì trả giá trị mặc định.
    2. **Không bao giờ xếp hàng** — nếu không còn chỗ trống thì bỏ qua ngay lập
       tức thay vì chờ.

    Không có lớp thứ hai thì hệ thống tự bóp cổ mình: mỗi lần quá hạn để lại một
    luồng chạy vĩnh viễn ở 100% CPU và giữ chỗ của nó. Sau đủ số lần, pool cạn,
    và **mọi** phép tính sau đó — kể cả những phép chỉ mất vài mili-giây — đều
    phải xếp hàng chờ hết hạn. Một lượt quét cả kho từ 100 giây thành hơn 10
    phút, còn server thì cứ chạy lâu là chậm dần rồi đứng hẳn.
    """
    limit = timeout if timeout is not None else settings.cas_timeout
    remaining = time_left()
    if remaining is not None:
        if remaining <= 0:
            return default
        limit = min(limit, remaining)

    if not _SLOTS.acquire(blocking=False):
        return default  # hết chỗ: bỏ qua chứ không chờ

    released = False
    try:
        future = _EXECUTOR.submit(func)
        try:
            result = future.result(timeout=limit)
        except FutureTimeout:
            # Luồng vẫn chạy tiếp. Trả chỗ khi nào nó xong — có thể là không
            # bao giờ, và đó chính là điều cần đếm.
            global _abandoned_total
            _abandoned_total = next(_ABANDONED) + 1
            future.add_done_callback(lambda _: _SLOTS.release())
            released = True
            return default
        except Exception:
            return default
        return result
    finally:
        if not released:
            _SLOTS.release()


def _is_ambiguous(expr: Any) -> bool:
    """Parser lark trả `Tree('_ambig', [...])` khi ngữ pháp đọc được nhiều nghĩa.

    Ví dụ `2\\cos(6\\theta) + 20` đọc được thành `2cos(6θ) + 20` hoặc
    `2cos(6θ + 20)`. Đoán bừa một nhánh là nguồn báo sai kinh điển: chọn nhầm
    thì một đồng nhất thức lượng giác đúng bị kết luận là sai. Gặp nhập nhằng
    thì bỏ hẳn kết quả của lark và để antlr trả lời.
    """
    return expr.__class__.__name__ == "Tree"


#: Tên hàm viết bằng lệnh LaTeX. Dùng để phát hiện parser đã **nuốt mất** một
#: hàm thay vì áp dụng nó.
_FUNCTION_WORDS = (
    "arcsin", "arccos", "arctan", "sinh", "cosh", "tanh",
    "sin", "cos", "tan", "cot", "sec", "csc", "log", "ln", "exp",
)


def _swallowed_function(expr: Any, source: str) -> bool:
    """Parser có biến tên hàm thành một phần của tên ẩn không?

    `W = F d\\cos 0^{\\circ}` là cái bẫy: ngữ pháp antlr coi `d` là dấu vi phân
    (như `\\int f\\,dx`), nên `d\\cos` bị gộp thành **một ký hiệu tên `dcos`**,
    rồi đối số của cosin rơi ra ngoài thành thừa số nhân. Với góc 0 thì cả tích
    thành 0, và một bước hoàn toàn đúng (`15 × 4,0 = 60 J`) bị kết luận `0 ≠ 60`.

    Không lỗi nào ném ra, và biểu thức vẫn "dùng được" theo mọi phép kiểm khác —
    chỉ có nghĩa của nó là đã mất. Gặp dấu hiệu này thì bỏ hẳn kết quả parse chứ
    không đem ra so sánh.

    Chỉ soi những tên hàm **thật sự có trong chuỗi nguồn**: một ẩn tên chứa
    "cos" mà cả biểu thức không hề gọi `\\cos` thì đó chỉ là cái tên.
    """
    try:
        names = [str(s) for s in expr.free_symbols]
    except (AttributeError, TypeError):
        return False
    for word in _FUNCTION_WORDS:
        if f"\\{word}" not in source:
            continue
        if any(word in name for name in names):
            return True
    return False


def _has_stray_tuple(expr: Any) -> bool:
    """`Tuple` nằm làm số hạng của một phép toán là dấu hiệu parser đọc sai.

    Backend lark đọc `F d\\cos (0.5)` thành `F*(d, 0.877)` — một `Tuple` nằm
    trong phép nhân. `usable()` chỉ chặn `Tuple` ở tầng ngoài cùng nên dạng lồng
    này lọt qua, và mọi phép so sau đó đều vô nghĩa.

    Phải soi đúng **chỗ** `Tuple` xuất hiện chứ không phải sự có mặt của nó:
    `Integral`, `Sum`, `Product` đều lưu cận của mình bằng `Tuple`
    (`Integral(1, (phi, 0, phi))`), nên quét cả cây sẽ giết sạch mọi tích phân
    và mọi tổng trong kho — 285 bước — trong khi chẳng bắt thêm lỗi nào.
    """
    try:
        nodes = sp.preorder_traversal(expr)
    except (AttributeError, TypeError):
        return False
    for node in nodes:
        if isinstance(node, (sp.Mul, sp.Add, sp.Pow)):
            if any(isinstance(arg, sp.Tuple) for arg in node.args):
                return True
    return False


def usable(expr: Any) -> bool:
    """Chỉ chấp nhận thứ SymPy tính toán được.

    Parser LaTeX đôi khi trả `Tuple`, `Tree`, `MatrixBase`… — nhét những thứ đó
    vào `simplify` hay `subs` sẽ nổ ở tận đáy stack, nên chặn ngay tại cửa.
    """
    if expr is None:
        return False
    if isinstance(expr, (sp.Expr, sp.Rel, sp.logic.boolalg.Boolean)):
        return not isinstance(expr, sp.Tuple)
    return isinstance(expr, bool)


_E = sp.Symbol("e")

# SymPy dành riêng một số tên một chữ cái cho hằng dựng sẵn: `F`/`T` là hằng
# logic false/true, `S` là sổ đăng ký singleton, `N`/`O`/`Q`/`C` là hàm và lớp.
# Trong đề Lí - Hoá thì đó lại là lực, chu kì, entropy, số hạt, nhiệt dung…
# Không chặn thì `F = ma` biến thành `False = ma` và mọi kiểm chứng vô nghĩa.
_RESERVED_NAMES = ("F", "T", "S", "N", "O", "Q", "C", "beta", "gamma", "zeta", "lambda")
_SAFE_LOCALS = {name: sp.Symbol(name) for name in _RESERVED_NAMES}

_RELATION_RE = re.compile(r"[=<>]|\\ne|\\leq|\\geq|\\le\b|\\ge\b|\\lt|\\gt")


def _fix_boolean_misparse(expr: Any, source: str) -> Any:
    """Trả về ký hiệu thật khi parser biến một tên thành hằng logic."""
    if not isinstance(expr, sp.logic.boolalg.BooleanAtom):
        return expr
    if _RELATION_RE.search(source):
        return expr  # thật sự là một mệnh đề
    stripped = source.strip()
    return sp.Symbol(stripped) if stripped.isidentifier() else None


def _resolve_euler(expr: sp.Expr) -> sp.Expr:
    """`e^{3}` trong LaTeX là số Euler, nhưng parser trả về ký hiệu tự do `e`.

    Chỉ thay khi `e` đứng làm cơ số của luỹ thừa — đó là lúc nghĩa "số Euler"
    gần như chắc chắn. Để nguyên `e` đứng một mình, vì trong vật lí nó thường
    là điện tích nguyên tố.
    """
    try:
        if _E not in expr.free_symbols:
            return expr
        powers = [p for p in expr.atoms(sp.Pow) if p.base == _E]
        if not powers:
            return expr
        return expr.xreplace({p: sp.exp(p.exp) for p in powers})
    except Exception:
        return expr


#: Tên lệnh LaTeX mà parser dịch thẳng thành ký hiệu cùng tên — ở đó `\alpha`
#: thành `Symbol('alpha')` là nghĩa đúng, không phải parser đoán bừa.
_COMMAND_SYMBOLS = frozenset(
    """
    alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota
    kappa lambda mu nu xi omicron pi varpi rho varrho sigma varsigma tau
    upsilon phi varphi chi psi omega
    Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
    infty hbar ell prime partial degree
    """.split()
)

_COMMAND_RE = re.compile(r"\\([A-Za-z]+)")
#: Ngoặc rỗng còn sót: có thứ gì đó đã bị gỡ ra khỏi giữa biểu thức.
_EMPTY_GROUP_RE = re.compile(r"\(\s*\)|\{\s*\}|\[\s*\]")
#: Toán tử cụt ở đầu hoặc cuối — vế này đã mất một toán hạng.
#: Dấu `-` mở đầu không kể: đó là số âm.
_DANGLING_OP_RE = re.compile(r"^\s*[*/^]|[-+*/^]\s*$")
#: Hai cụm số chỉ cách nhau bằng khoảng trắng. `clean_latex` đã gộp sẵn dạng
#: phân nhóm hàng nghìn, nên cái còn lại ở đây là thật sự nhập nhằng.
_JUXTAPOSED_NUMBERS_RE = re.compile(r"\d\s+\d")


def _untrustworthy(source: str, expr: Any) -> str | None:
    """Parser có đọc trọn vẹn chuỗi này không, hay nó đã âm thầm bịa/bỏ bớt?

    Đây là hàng rào quan trọng nhất của cả bộ đọc, vì hỏng ở đây là hỏng **im
    lặng**: cả hai parser LaTeX của SymPy đều sẵn sàng nhận một tiền tố hợp lệ
    rồi vứt phần đuôi mà không ném lỗi nào. Đo trên kho:

    * `4 ( ) + 1` trả về đúng `4` — mất hẳn vế sau.
    * `1 + 2 +` trả về `3` — toán hạng cuối bốc hơi.
    * `5 7` (vốn là `5 \\quad 7`, hai mệnh đề rời) trả về `57`.
    * `2 + 3 \\mathrm{C{=}O}` trả về `3*mathrm + 2` — một lệnh LaTeX bị biến
      thành ký hiệu toán học.

    Mỗi trường hợp đều cho ra một biểu thức **trông hợp lệ** rồi được đem đi so
    sánh, nên hậu quả không phải là "không đọc được" mà là một kết luận sai đầy
    tự tin. Thà trả None: "chưa kiểm được" là câu trả lời hợp lệ, "sai" thì không.
    """
    if _EMPTY_GROUP_RE.search(source):
        return "còn ngoặc rỗng — có thứ gì đó đã bị gỡ khỏi giữa biểu thức"
    if _DANGLING_OP_RE.search(source):
        return "toán tử cụt ở đầu hoặc cuối — vế này thiếu một toán hạng"
    if _JUXTAPOSED_NUMBERS_RE.search(source):
        return "hai cụm số dính nhau bằng khoảng trắng — không rõ một số hay hai"

    unknown = {m.group(1) for m in _COMMAND_RE.finditer(source)} - _COMMAND_SYMBOLS
    if unknown:
        invented = {str(s) for s in free_symbols(expr)} & unknown
        if invented:
            return "parser bịa ký hiệu từ lệnh nó không hiểu: " + ", ".join(sorted(invented))
    return None


def _protect_leibniz(expr: sp.Expr) -> sp.Expr:
    """Giữ `dh/dt` ở dạng chưa tính được thay vì để nó rút về 0.

    `\\frac{dh}{dt}` được SymPy đọc thành `Derivative(h, t)` với `h` là một ký
    hiệu **tự do**. Đạo hàm của một hằng theo `t` đúng bằng 0, nên `.doit()` cho
    ra 0 — trong khi lời giải đang nói về một đại lượng khác 0. Hậu quả: mọi
    bước chứa ký pháp Leibniz bị đem so với 0 rồi bị bác bỏ, và đây là ký pháp
    trung tâm của cả giải tích lẫn động học (148 bước trong kho, 2,7%):

        -2 = 4\\pi\\frac{dh}{dt}   ->  "-2 ≠ 0"        (thực ra bài đúng)
        \\frac{dN}{dt} = ... = 24  ->  "0 ≠ 24"        (thực ra bài đúng)

    Đổi `h` thành hàm `h(t)` giữ đạo hàm ở dạng chưa tính được — tức là giữ đúng
    nghĩa "đại lượng này chưa biết", và bước ấy trở lại thành "chưa kết luận".
    """
    try:
        derivatives = expr.atoms(sp.Derivative)
    except Exception:
        return expr

    swap: dict[sp.Expr, sp.Expr] = {}
    for derivative in derivatives:
        target = derivative.expr
        if not isinstance(target, sp.Symbol):
            continue  # đạo hàm của một biểu thức thật — SymPy tính đúng, để yên
        variables = [var for var, _ in derivative.variable_count]
        if target in variables:
            continue  # `dx/dx`: để nguyên cho SymPy trả 1
        try:
            swap[derivative] = sp.Derivative(
                sp.Function(target.name)(*variables), *derivative.variable_count
            )
        except Exception:
            continue
    if not swap:
        return expr
    try:
        return expr.xreplace(swap)
    except Exception:
        return expr


#: Bộ nhớ đệm cho những chuỗi đã đọc được. Đọc LaTeX bằng antlr chiếm ~90% thời
#: gian của cả lớp kiểm chứng, mà một lời giải hỏi đi hỏi lại **cùng một chuỗi**
#: rất nhiều lần: vế phải của bước trước được mang sang bước sau, phần rút giá
#: trị số quét lại từ đầu, lớp đổi đơn vị đọc lại vế đã đọc, sổ tay ký hiệu ghi
#: lại vế vừa kiểm.
#:
#: Chỉ đệm kết quả **đọc được**. Một lần trả None có thể chỉ vì hết giờ (máy
#: bận), và nhớ nó lại thì cái rủi thoáng qua ấy thành vĩnh viễn: bước đó không
#: bao giờ kiểm được nữa trong suốt vòng đời tiến trình.
_PARSE_CACHE: dict[tuple[str, bool], sp.Expr] = {}
_PARSE_CACHE_LIMIT = 4096


def to_sympy(latex: str, *, clean: bool = True) -> sp.Expr | None:
    """Đọc một biểu thức LaTeX thành đối tượng SymPy. Trả None nếu không đọc được."""
    if not latex or not str(latex).strip():
        return None
    key = (str(latex), clean)
    cached = _PARSE_CACHE.get(key)
    if cached is not None:
        return cached
    source = clean_latex(latex) if clean else str(latex).strip()
    if not source:
        return None

    def _finish(result: sp.Expr) -> sp.Expr | None:
        """Cổng cuối: chỉ trả về thứ parser thật sự đọc được trọn vẹn.

        Trả None nghĩa là "backend này đọc hỏng", không phải "chuỗi này không
        đọc được": nơi gọi thử tiếp backend sau rồi mới tới đường cứu cánh.
        """
        if _untrustworthy(source, result) is not None:
            return None
        # Đọc được về mặt cú pháp vẫn chưa đủ: hai dạng hỏng dưới đây cho ra
        # biểu thức hợp lệ nhưng sai nghĩa, và sai lặng lẽ.
        if _swallowed_function(result, source) or _has_stray_tuple(result):
            return None
        return _protect_leibniz(_resolve_euler(result))

    def _parse() -> sp.Expr | None:
        from sympy.parsing.latex import parse_latex

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            # antlr đi trước: ngữ pháp của nó quyết đoán hơn ở đúng những chỗ
            # lark nhập nhằng (hàm lượng giác, áp dụng hàm). lark giữ lại làm
            # phương án hai vì nó đọc được vài dạng antlr chịu thua.
            for backend in ("antlr", "lark"):
                try:
                    parsed = parse_latex(source, backend=backend)
                except Exception:
                    continue
                if _is_ambiguous(parsed):
                    continue
                parsed = _fix_boolean_misparse(parsed, source)
                if usable(parsed):
                    try:
                        result = sp.sympify(parsed)
                    except Exception:
                        continue
                    result = _fix_boolean_misparse(result, source)
                    if usable(result):
                        checked = _finish(result)
                        if checked is not None:
                            return checked
                        continue
            # Cứu cánh cuối: chuỗi có thể vốn đã là cú pháp Python/SymPy.
            try:
                result = sp.sympify(source.replace("^", "**"), locals=_SAFE_LOCALS)
            except Exception:
                return None
            result = _fix_boolean_misparse(result, source)
            return _finish(result) if usable(result) else None

    parsed = run_guarded(_parse, None)
    if parsed is not None:
        if len(_PARSE_CACHE) >= _PARSE_CACHE_LIMIT:
            _PARSE_CACHE.clear()  # xoá sạch, đơn giản hơn LRU và cũng đủ
        _PARSE_CACHE[key] = parsed
    return parsed


def sides(latex: str) -> list[sp.Expr]:
    """Tách `a = b = c` rồi đọc từng vế. Vế nào không đọc được thì bỏ."""
    out: list[sp.Expr] = []
    for part in split_equation(latex):
        expr = to_sympy(part)
        if expr is not None:
            out.append(expr)
    return out


def free_symbols(expr: sp.Expr | None) -> set[sp.Symbol]:
    if expr is None:
        return set()
    try:
        return set(expr.free_symbols)
    except Exception:
        return set()


def to_number(expr: sp.Expr | None) -> float | None:
    """Ép biểu thức về số thực nếu nó không còn ẩn."""
    if expr is None:
        return None

    def _eval() -> float | None:
        try:
            if isinstance(expr, sp.Equality):
                target = expr.rhs
            else:
                target = expr
            if target.free_symbols:
                return None
            value = complex(sp.N(target, 20))
            if abs(value.imag) > 1e-9 * max(1.0, abs(value.real)):
                return None
            return float(value.real)
        except Exception:
            return None

    return run_guarded(_eval, None)


def evaluate_latex(latex: str) -> float | None:
    """Tính giá trị số của một biểu thức LaTeX (kể cả `\\lim`, `\\int`, `\\sum`)."""
    expr = to_sympy(latex)
    if expr is None:
        return None

    def _doit() -> sp.Expr:
        return sp.simplify(expr.doit()) if hasattr(expr, "doit") else expr

    return to_number(run_guarded(_doit, expr))
