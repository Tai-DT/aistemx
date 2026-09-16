"""Áp dụng hàm chưa định nghĩa: nguyên tử mờ và sổ tay định nghĩa hàm.

`P(X = 4)`, `f(1)`, `\\operatorname{Var}(X)` đều là **áp dụng hàm**, và parser
LaTeX hỏng ở mỗi dạng một kiểu khác nhau:

* `P(X = 4)` rụng mất đối số, chỉ còn trơ lại ký hiệu `P` — nên `P(X = 4)` và
  `P(X = 5)` biến thành cùng một thứ. Đây là kiểu hỏng tệ nhất: nó có thể **xác
  nhận** một đẳng thức không hề đúng.
* `\\operatorname{Var}(X)` bị `clean_latex` gỡ vỏ thành `Var(X)` rồi đọc tiếp
  thành tích ba chữ cái `V*a*r`.
* `f(1)` thì antlr đọc đúng thành hàm chưa định nghĩa, nhưng đường cứu cánh
  `sympify` lại đọc `N(2)`, `S(40)` thành hàm dựng sẵn của SymPy và ra một con
  số bịa.

Vì vậy trước đây gặp mọi dạng trên là bỏ nguyên cả bước. Giá phải trả: một bước
như `P(X = 4) = 0{,}343 \\times 0{,}3 = 0{,}1029` có khâu thuần số kiểm được
ngay cũng bị vứt cùng.

Ở đây ta thay mỗi lời gọi bằng một **nguyên tử mờ** — một hàm chưa định nghĩa
của SymPy mang số hiệu riêng. Nó không giả vờ biết `P` là gì, chỉ giữ chỗ, để
các khâu còn lại của chuỗi vẫn kiểm được như thường.

Nguyên tử mờ có một tính chất quý cho việc chống báo oan: SymPy không bao giờ
ép được nó về số, nên mọi phép so dính nguyên tử mờ đều dừng ở "chưa kết luận".
Tự nó đã không kết tội được ai. Chỗ *có thể* kết tội là khi ta thế định nghĩa
hàm vào và mọi thứ thành số thật — nên `resolve()` báo lại việc đã thế, và bên
gọi có bổn phận hạ mọi phán quyết "khác nhau" ở những khâu ấy xuống "chưa kết
luận".
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

import sympy as sp
from sympy.core.function import AppliedUndef

from ..textnorm import split_equation
from .parse import run_guarded, to_sympy, usable

#: Tên hàm giữ chỗ. Bắt buộc phải là **một** token sau khi qua parser LaTeX:
#: tên nhiều chữ cái bị đọc thành tích (`Var(x)` -> `V*a*r(x)`). `\Xi` là lệnh
#: một token, và là chữ Hy Lạp gần như không xuất hiện trong kho.
_PLACEHOLDER_NAME = "Xi"
_PLACEHOLDER_CMD = "\\Xi"
#: Số hiệu bắt đầu từ một chỗ cao và lạ, để `\Xi(9001)` không thể trùng với thứ
#: gì kho tự viết ra.
_FIRST_INDEX = 9001

#: Đối số dài hơn thế này thì gần như chắc chắn ta đang đọc nhầm ranh giới ngoặc.
_MAX_ARG = 48

#: Dấu phẩy trước một lệnh LaTeX, `\,` `\;` … — chỉ là khoảng cách trình bày.
_SPACING_IN_ARG_RE = re.compile(r"\\[,;:!]|\\quad|\\qquad|\\ |\s+")

#: Đối số thuần số: `1`, `-2`, `0.5`, `2{,}1`. Đây là dạng duy nhất được phép
#: đem đi thế định nghĩa hàm, vì chỉ với nó ta mới chắc "đối số" là một giá trị
#: chứ không phải một biểu thức còn ẩn.
_NUMERIC_ARG_RE = re.compile(r"^[-+]?\d+(?:[.]\d+)?$")

#: Dấu hiệu "cái trong ngoặc là một mệnh đề / một tập", tức chắc chắn KHÔNG phải
#: phép nhân: `P(X = 4)`, `P(k \ge 2)`, `\operatorname{Var}(S \mid N)`.
_RELATION_IN_ARG_RE = re.compile(
    r"[=<>]|\\ne\b|\\neq|\\leq?\b|\\geq?\b|\\mid|\\in\b|\\cap|\\cup|\\subset|\\equiv"
)

#: `\left(`/`\right)` chỉ là cỡ dấu ngoặc. Gỡ trước cho phép quét ngoặc cân bằng
#: nhìn thấy đúng cặp ngoặc — `clean_latex` rồi cũng gỡ y hệt ở bước sau.
_LEFTRIGHT_RE = re.compile(r"\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big)\s*(?=[([{|.\\\])}])")

#: Đầu một lời gọi hàm, ngay trước dấu `(`:
#:   * `\operatorname{Var}` — tên nhiều chữ cái, luôn là hàm;
#:   * một chữ cái đứng riêng, có thể kèm dấu phẩy đạo hàm: `f`, `g`, `f'`,
#:     `y^{\prime}`.
#: Ràng buộc "không có chữ cái hay dấu `\` ngay trước" là để `\sin(x)`,
#: `\Phi(0)`, `\min\{...\}` không bị nhận nhầm thành hàm một chữ cái.
_CALL_HEAD_RE = re.compile(
    r"\\operatorname\s*\*?\s*\{\s*([A-Za-z][A-Za-z0-9]*)\s*\}\s*(?=\()"
    r"|(?<![A-Za-z\\])([A-Za-z](?:'+|\^\s*\{?\s*\\prime\s*\}?)?)\s*(?=\()"
)

#: Vế trái của một định nghĩa hàm, sau khi đã qua `split_equation`: `f(x)`,
#: `f'(t)`. Đối số phải là **một chữ cái** — đó là biến, chứ không phải một giá
#: trị cụ thể.
_DEF_HEAD_RE = re.compile(r"^([A-Za-z](?:'+)?)\s*\(\s*([A-Za-z])\s*\)$")

#: Những dấu hiệu cho biết đẳng thức đang xét không phải một định nghĩa hàm
#: dùng được ở mọi nơi: hàm cho theo từng khoảng, định nghĩa kèm điều kiện, hay
#: chỉ là một giá trị xấp xỉ.
_UNSAFE_DEFINITION_RE = re.compile(
    r"\\begin\{cases\}|\\text|\\mbox|\\mid|\||[<>]|\\le\b|\\leq|\\ge\b|\\geq"
    r"|\\forall|\\in\b|\\approx|\\simeq|\\sim\b|\\pm|\\infty|\\ne\b|\\neq"
)


@dataclass(frozen=True)
class _Call:
    """Một lời gọi hàm đã được thay bằng nguyên tử mờ."""

    name: str      # tên hàm như kho viết: `f`, `f'`, `Var`
    arg: str       # đối số đã chuẩn hoá
    numeric: bool  # đối số có phải một con số cụ thể không


@dataclass(frozen=True)
class _Definition:
    variable: sp.Symbol
    expr: sp.Expr


def _canonical_arg(arg: str) -> str:
    """Dạng chuẩn của đối số, để `P(X=4)` và `P(X = 4)` ra cùng một nguyên tử.

    Chỉ bỏ những thứ không mang nghĩa (khoảng trắng, lệnh giãn cách) và quy dấu
    phẩy thập phân LaTeX về dấu chấm. Không đụng gì khác: `P(X=4)` và `P(X=5)`
    **phải** ra hai nguyên tử khác nhau.
    """
    canonical = re.sub(r"(\d)\s*\{\s*,\s*\}\s*(\d)", r"\1.\2", arg)
    return _SPACING_IN_ARG_RE.sub("", canonical)


def _matching_paren(source: str, opening: int) -> int:
    """Vị trí dấu `)` khớp với dấu `(` ở `opening`, hoặc -1 nếu không có."""
    depth = 0
    for i in range(opening, min(len(source), opening + _MAX_ARG + 2)):
        char = source[i]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return i
    return -1


def has_opaque_atom(expr: Any) -> bool:
    """Biểu thức còn chứa hàm chưa định nghĩa nào không?

    Dùng để biết một khâu có dính nguyên tử mờ hay không. SymPy không tính được
    số từ hàm chưa định nghĩa, nên khâu như thế không bao giờ đủ căn cứ kết tội.
    """
    if expr is None or not hasattr(expr, "atoms"):
        return False
    try:
        applied = expr.atoms(AppliedUndef)
        if not applied:
            return False
        # `\frac{dV}{dt}` cũng cho ra một hàm chưa định nghĩa, nhưng vì lí do
        # khác hẳn: `parse._protect_leibniz` đổi `V` thành `V(t)` để đạo hàm
        # không bị `.doit()` rút về 0. Người viết không hề gọi hàm nào ở đó, nên
        # gọi tên nó là "áp dụng hàm chưa định nghĩa" là nói sai với người đọc.
        # Không kết tội thì vẫn không kết tội — quy tắc khác tập ẩn lo phần ấy.
        import sympy as sp

        in_derivative = {
            target
            for derivative in expr.atoms(sp.Derivative)
            for target in derivative.expr.atoms(AppliedUndef)
        }
        return bool(applied - in_derivative)
    except (AttributeError, TypeError):
        return False


class FunctionScope:
    """Sổ tay hàm của **một** lời giải.

    Giữ hai thứ: bảng nguyên tử mờ (để cùng một lời gọi luôn ra cùng một nguyên
    tử suốt cả lời giải) và các định nghĩa hàm bắt được.
    """

    def __init__(self) -> None:
        self._index: dict[str, int] = {}
        self._calls: dict[int, _Call] = {}
        self._definitions: dict[str, _Definition] = {}
        #: Tên hàm bị định nghĩa hai kiểu khác nhau (hàm cho theo từng khoảng,
        #: hàm bị đặt lại giữa chừng). Một khi đã dính vào đây thì cấm thế số
        #: vĩnh viễn: chọn nhầm nhánh là kết tội oan hoặc xác nhận bừa.
        self._poisoned: set[str] = set()

    # --------------------------------------------------------------- viết lại

    def rewrite(self, latex: str) -> str:
        """Thay mọi lời gọi hàm nhận ra được bằng nguyên tử mờ `\\Xi(<số hiệu>)`."""
        source = _LEFTRIGHT_RE.sub("", str(latex))
        if _PLACEHOLDER_CMD in source:
            # Kho tự dùng `\Xi`: không có cách nào bảo đảm không đụng nhau nữa,
            # nên thà không thay gì cả.
            return source

        out: list[str] = []
        copied = 0
        search_from = 0
        while True:
            head = _CALL_HEAD_RE.search(source, search_from)
            if head is None:
                break
            opening = head.end()
            closing = _matching_paren(source, opening)
            name = head.group(1) or head.group(2)
            if closing < 0:
                search_from = opening + 1
                continue
            arg = source[opening + 1 : closing]
            numeric = self._recognise(arg, operator=head.group(1) is not None)
            if numeric is None:
                search_from = opening + 1
                continue
            out.append(source[copied : head.start()])
            out.append(self._token(name, arg, numeric=numeric))
            copied = search_from = closing + 1
        if not out:
            return source
        out.append(source[copied:])
        return "".join(out)

    @staticmethod
    def _recognise(arg: str, *, operator: bool) -> bool | None:
        """Có nhận đây là áp dụng hàm không? Trả True/False = "đối số là số hay không".

        Trả None nghĩa là **không dám khẳng định**: `x(t+1)` trong Vật lí hoàn
        toàn có thể là phép nhân thật, `P` có thể là áp suất nhân với biểu thức
        trong ngoặc. Ở những chỗ mơ hồ đó ta để nguyên cho parser xử lí như cũ
        thay vì chọn bừa một nghĩa.
        """
        canonical = _canonical_arg(arg)
        if not canonical or len(canonical) > _MAX_ARG:
            return None
        if _NUMERIC_ARG_RE.match(canonical):
            return True
        if operator or _RELATION_IN_ARG_RE.search(canonical):
            # `\operatorname{Var}(X)`: tên nhiều chữ cái thì chắc chắn là hàm.
            # Còn trong ngoặc có dấu so sánh thì chắc chắn không phải phép nhân.
            return False
        return None

    def _token(self, name: str, arg: str, *, numeric: bool) -> str:
        key = f"{name}({_canonical_arg(arg)})"
        index = self._index.get(key)
        if index is None:
            index = _FIRST_INDEX + len(self._index)
            self._index[key] = index
            self._calls[index] = _Call(name=name, arg=_canonical_arg(arg), numeric=numeric)
        return f"{_PLACEHOLDER_CMD}({index})"

    def describe(self, expr: Any) -> str:
        """Tên các lời gọi hàm còn nguyên trong biểu thức, để nói cho người đọc."""
        names: list[str] = []
        if expr is None or not hasattr(expr, "atoms"):
            return ""
        try:
            atoms = expr.atoms(AppliedUndef)
        except (AttributeError, TypeError):
            return ""
        for atom in atoms:
            call = self._call_of(atom)
            names.append(f"{call.name}({call.arg})" if call else str(atom))
        return ", ".join(sorted(names)[:3])

    def _call_of(self, atom: Any) -> _Call | None:
        if type(atom).__name__ != _PLACEHOLDER_NAME or len(atom.args) != 1:
            return None
        try:
            return self._calls.get(int(atom.args[0]))
        except (TypeError, ValueError):
            return None

    # ------------------------------------------------------------- định nghĩa

    def learn(self, latex: str) -> None:
        """Nhặt định nghĩa hàm từ một mảnh bước, nếu mảnh ấy đúng là định nghĩa.

        Rất chặt tay, vì một định nghĩa đọc sai sẽ lan sang mọi bước sau: chỉ
        nhận dạng `f(x) = <biểu thức chỉ chứa x>`, không nhận hàm đệ quy, hàm
        cho theo từng khoảng, hay hàm phụ thuộc thứ khác chưa biết.
        """
        text = str(latex)
        parts = split_equation(self.rewrite(text))
        if len(parts) < 2:
            return
        head = _DEF_HEAD_RE.match(parts[0].strip())
        if head is None:
            return
        name, variable = head.group(1), head.group(2)
        if name in self._poisoned or name == variable:
            return

        def _give_up() -> None:
            """Thấy một định nghĩa của `name` mà không dùng được ⇒ **đầu độc** tên ấy.

            Đây là chỗ thứ tự quyết định đúng sai. Nếu chỉ lặng lẽ `return` thì
            một hàm cho theo từng khoảng — nhánh này viết bằng `\begin{cases}`
            (không dùng được), nhánh kia viết `f(x) = 3x - 1` (dùng được) — sẽ
            chỉ để lại nhánh dùng được, và mọi `f(a)` sau đó bị thế bằng đúng
            một nhánh rồi đóng dấu "đã kiểm". Thấy dấu hiệu không dùng được là
            phải bỏ hẳn cái tên, kể cả những cách viết trước đó của nó.
            """
            self._poisoned.add(name)
            self._definitions.pop(name, None)

        if _UNSAFE_DEFINITION_RE.search(text):
            _give_up()
            return

        expr = to_sympy(parts[1])
        if not usable(expr) or isinstance(expr, (sp.Rel, sp.logic.boolalg.Boolean)):
            _give_up()
            return
        if has_opaque_atom(expr):
            # Vế phải còn hàm chưa biết: `f(x) = f(x-1) + 2` (đệ quy),
            # `f(t) = u(t-2)(t-2)` (phụ thuộc hàm bậc thang). Thế vào là bịa.
            _give_up()
            return
        symbol = sp.Symbol(variable)
        try:
            unexpected = expr.free_symbols != {symbol}
        except (AttributeError, TypeError):
            _give_up()
            return
        if unexpected:
            # Vừa chặn tham số lạ (`P(t) = L/(1+Ae^{-kt})` — L, A, k chưa biết),
            # vừa đòi vế phải THỰC SỰ phụ thuộc biến: `P(A) = 0,5` trông y hệt
            # một định nghĩa nhưng `A` ở đó là một biến cố, và coi nó là hàm
            # hằng sẽ "xác nhận" luôn cả `P(B) = 0,5`.
            #
            # Và một khi cái tên ấy đã có thêm một cách viết khác mà ta không
            # dùng được, thì cách viết đang giữ cũng hết đáng tin: đó là dấu
            # hiệu hàm được cho theo từng khoảng hoặc bị đặt lại giữa chừng.
            _give_up()
            return

        previous = self._definitions.get(name)
        if previous is None:
            self._definitions[name] = _Definition(variable=symbol, expr=expr)
            return
        if previous.variable == symbol and _same_expression(previous.expr, expr):
            return
        # Một cái tên, hai công thức: hàm cho theo từng khoảng hoặc bị đặt lại.
        # Không có cách nào biết bước đang xét thuộc nhánh nào, nên bỏ hẳn.
        _give_up()

    def resolve(self, expr: Any) -> tuple[Any, bool]:
        """Thế định nghĩa hàm vào các nguyên tử mờ. Trả (biểu thức, có thế hay không).

        Chỉ thế cho lời gọi có đối số là **số cụ thể**. Không thế cho `f(x)`:
        làm thế thì chính bước định nghĩa `f(x) = x^2 + 1` tự xác nhận nó, một
        lời xác nhận rỗng tuếch.
        """
        if expr is None or not self._definitions or not hasattr(expr, "atoms"):
            return expr, False
        try:
            atoms = expr.atoms(AppliedUndef)
        except (AttributeError, TypeError):
            return expr, False

        mapping: dict[Any, Any] = {}
        for atom in atoms:
            call = self._call_of(atom)
            if call is None or not call.numeric:
                continue
            definition = self._definitions.get(call.name)
            if definition is None:
                continue
            argument = to_sympy(call.arg)
            if not usable(argument) or has_opaque_atom(argument):
                continue
            try:
                if argument.free_symbols:
                    continue
            except (AttributeError, TypeError):
                continue
            value = run_guarded(
                lambda d=definition, a=argument: d.expr.subs(d.variable, a), None
            )
            if usable(value):
                mapping[atom] = value
        if not mapping:
            return expr, False
        replaced = run_guarded(lambda: expr.xreplace(mapping), None)
        return (replaced, True) if usable(replaced) else (expr, False)


def _same_expression(a: sp.Expr, b: sp.Expr) -> bool:
    """Hai vế phải có phải cùng một công thức, chỉ khác cách viết?

    Dùng khi một hàm được viết lại lần thứ hai. Viết lại y hệt (`y(t) = 3-3e^{-2t}`
    rồi `y(t) = 3(1-e^{-2t})`) thì giữ; khác nhau thật thì mới coi là định nghĩa
    theo từng khoảng và vứt cả hai.
    """
    if a == b:
        return True
    return bool(run_guarded(lambda: sp.simplify(a - b) == 0, False))
