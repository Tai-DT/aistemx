"""Môi trường ký hiệu tích luỹ dọc theo lời giải.

Lí do tồn tại: `equivalent()` từ chối kết luận khi hai vế khác tập ẩn, vì khác
tập ẩn thường nghĩa là "đây là bước thế số, hai vế cố ý khác nhau". Nhìn RIÊNG
một bước thì lập luận đó đúng — nhưng lời giải là một chuỗi, và những ẩn ấy
thường đã được chính lời giải gán giá trị ở bước trước:

    bước 3:  N = 5{,}54\\left(\\frac{6{,}40}{0{,}24}\\right)^{2} = 3{,}94\\times10^{3}
    bước 4:  H = \\frac{L}{N} = \\frac{250}{3940}

Gom các gán ấy lại thành một môi trường thì khâu `\\frac{L}{N} = \\frac{250}{3940}`
kiểm được, thay vì bị bỏ qua vì "khác tập ẩn".

Toàn bộ module này được viết theo đúng nguyên tắc bất đối xứng của hệ thống:
môi trường chỉ dùng để **xác nhận**. Một ràng buộc sai chỉ làm mất một lần xác
nhận, không bao giờ được biến thành một lời kết tội — xem `env_may_refute`
trong `config.py`, mặc định tắt.
"""

from __future__ import annotations

import math
import re
from collections.abc import Iterable, Mapping

import sympy as sp

from ..textnorm import strip_trailing_units
from .parse import out_of_time, to_number, to_sympy

#: Trần số ràng buộc giữ lại. Lời giải dài nhất trong kho có vài chục bước; quá
#: ngưỡng này thì gần như chắc chắn ta đang gom nhầm thứ gì đó.
_MAX_BINDINGS = 80

#: Hai giá trị coi là "cùng một giá trị, chỉ khác chỗ làm tròn" khi lệch dưới
#: mức này. Dùng để phân biệt *nhắc lại* một ràng buộc (`p = 0{,}140` viết lại
#: lần nữa) với *gán lại* nó sang nghĩa khác.
_REBIND_TOLERANCE = 5e-3

#: Ký hiệu đội mũ là một đại lượng KHÁC với ký hiệu trần cùng tên: `\\bar{d}`
#: là trung bình các hiệu, còn `d` trong cùng bài lại là khoảng cách. Nhưng
#: `clean_latex` gỡ lệnh trình bày nên cả hai rơi về đúng một `Symbol('d')`.
#: Thu ràng buộc từ những dạng này là cách chắc chắn nhất để thay nhầm giá trị
#: vào một ký hiệu trùng tên, nên bỏ hẳn — mất vài lần xác nhận còn hơn.
_DECORATED_RE = re.compile(
    r"\\(?:bar|hat|tilde|vec|overline|widehat|overrightarrow|dot|ddot)\b"
)


def _same_value(a: float, b: float) -> bool:
    if not (math.isfinite(a) and math.isfinite(b)):
        return a == b
    scale = max(abs(a), abs(b))
    return abs(a - b) <= (_REBIND_TOLERANCE * scale if scale else 1e-12)


class SymbolEnv:
    """Các ràng buộc `ký hiệu → giá trị số` đã tích luỹ được tới thời điểm này.

    Chỉ giữ giá trị số chứ không giữ biểu thức: mục tiêu là kiểm những khâu thế
    số, và ràng buộc dạng biểu thức kéo theo cả chuyện thay lồng nhau, vòng lặp
    ràng buộc, lẫn nguy cơ thay nhầm — không đáng đánh đổi.
    """

    __slots__ = ("_conflicted", "_values")

    def __init__(self, seed: Mapping[str, float] | None = None) -> None:
        self._values: dict[str, float] = {}
        #: Ký hiệu đã mang hai giá trị khác nhau trong cùng một lời giải. Đó là
        #: dấu hiệu nó được dùng lại cho việc khác (`t` vừa là thời gian vừa là
        #: thống kê t), nên mọi ràng buộc của nó đều hết đáng tin.
        self._conflicted: set[str] = set()
        for name, value in (seed or {}).items():
            try:
                self.bind(str(name), float(value))
            except (TypeError, ValueError):
                continue

    def __bool__(self) -> bool:
        return bool(self._values)

    def bind(self, name: str, value: float) -> None:
        if not name or not math.isfinite(value) or len(self._values) >= _MAX_BINDINGS:
            return
        previous = self._values.get(name)
        if previous is not None and not _same_value(previous, value):
            # Gán lại sang giá trị khác. Ràng buộc cũ chết ngay tại đây, và ta
            # còn đánh dấu luôn ký hiệu là không đáng tin: một lời giải dùng
            # cùng một chữ cái cho hai đại lượng thì không có cách nào biết ở
            # một bước bất kỳ nó đang mang nghĩa nào.
            self._conflicted.add(name)
        self._values[name] = value

    def value(self, name: str) -> float | None:
        if name in self._conflicted:
            return None
        return self._values.get(name)

    # ---------------------------------------------------------------- thu nạp
    def record(self, parts: list[str], raw: str) -> None:
        """Nhặt ràng buộc từ một mắt xích: `<ký hiệu> = ... = <giá trị>`.

        Nhận các vế **đã tách** để nơi thu ràng buộc và nơi kiểm chứng luôn đọc
        mắt xích y hệt nhau — kể cả chuyện vế nào nằm sau dấu xấp xỉ. Nhưng
        cũng đòi luôn chuỗi `raw` chưa gọt, vì hàng rào ký hiệu đội mũ chỉ nhìn
        thấy được trước khi `clean_latex` gỡ mất `\\bar`, `\\vec`, `\\dot`.
        """
        if len(parts) < 2 or _DECORATED_RE.search(raw or ""):
            return
        head = to_sympy(parts[0])
        # Chỉ nhận vế trái là một ký hiệu trần. `f(1) = 3` hay `2x = 6` cũng là
        # thông tin, nhưng rút ra ràng buộc từ chúng đòi giải phương trình —
        # tức là đoán, và đoán sai ở đây thì hỏng âm thầm.
        if not isinstance(head, sp.Symbol):
            return
        for part in reversed(parts[1:]):
            for candidate in (part, strip_trailing_units(part)):
                value = to_number(to_sympy(candidate))
                if value is not None and math.isfinite(value):
                    self.bind(str(head), value)
                    return

    # --------------------------------------------------------------- sử dụng
    def reconcile(
        self,
        a: sp.Expr,
        b: sp.Expr,
        *,
        exclude: Iterable[str] = (),
    ) -> tuple[sp.Expr, sp.Expr, list[str]] | None:
        """Thay ràng buộc vào để hai vế về cùng tập ẩn. None nếu không làm được.

        Chỉ động tới những ký hiệu nằm trong **phần lệch** giữa hai tập ẩn: ký
        hiệu có mặt ở cả hai vế thì đã đối chiếu được rồi, thay thêm chỉ tăng
        cơ hội sai mà không thêm kết luận nào.

        `exclude` là các ký hiệu đang được ĐỊNH NGHĨA bởi chính bước này. Đây là
        hàng rào quan trọng nhất của cả đòn bẩy: `x = 7` sau khi bước trước đã
        đặt `x = 5` là một phép gán lại hoàn toàn hợp lệ, mà thay ràng buộc cũ
        vào thì thành `5 = 7` — một lời kết tội hoàn toàn bịa.
        """
        try:
            syms_a, syms_b = set(a.free_symbols), set(b.free_symbols)
        except (AttributeError, TypeError):
            return None
        differing = syms_a ^ syms_b
        if not differing:
            return None

        blocked = set(exclude)
        subs: dict[sp.Symbol, sp.Float] = {}
        for symbol in differing:
            name = str(symbol)
            if name in blocked:
                continue
            value = self.value(name)
            if value is not None:
                subs[symbol] = sp.Float(value)
        if not subs:
            return None

        try:
            new_a, new_b = a.subs(subs), b.subs(subs)
            if set(new_a.free_symbols) != set(new_b.free_symbols):
                return None
        except Exception:
            return None
        return new_a, new_b, sorted(f"{s}={subs[s]:.6g}" for s in subs)

    def usable_for(self, symbols: Iterable[sp.Symbol], exclude: Iterable[str] = ()) -> bool:
        """Có ràng buộc nào dùng được cho tập ký hiệu này không? (kiểm rẻ tiền)"""
        if not self._values or out_of_time():
            return False
        blocked = set(exclude)
        return any(
            str(s) not in blocked and self.value(str(s)) is not None for s in symbols
        )
