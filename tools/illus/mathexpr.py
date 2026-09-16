"""Bộ đánh giá biểu thức toán an toàn (whitelist AST).

Dùng chung cho: vẽ đồ thị hàm trong SVG 2D và "bake" lưới điểm cho mặt/khối 3D.
Chỉ cho phép số, biến khai báo trước, toán tử số học, luỹ thừa ``^``/``**`` và một
tập hàm/toán hằng an toàn. Mọi thứ khác (tên lạ, gọi thuộc tính, lambda...) bị chặn.
"""

from __future__ import annotations

import ast
import math
from typing import Callable, Iterable

# Hàm và hằng được phép xuất hiện trong biểu thức người dùng.
_FUNCS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan, "atan2": math.atan2,
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    "exp": math.exp, "log": math.log, "ln": math.log, "log10": math.log10,
    "sqrt": math.sqrt, "abs": abs, "sign": lambda x: (x > 0) - (x < 0),
    "floor": math.floor, "ceil": math.ceil,
    "min": min, "max": max, "pow": pow,
}
_CONSTS = {"pi": math.pi, "e": math.e, "tau": math.tau}

_ALLOWED_BINOPS = (ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.Mod, ast.FloorDiv)
_ALLOWED_UNARY = (ast.UAdd, ast.USub)


class ExprError(ValueError):
    """Biểu thức không hợp lệ hoặc dùng cú pháp bị cấm."""


def _check(node: ast.AST, names: set[str]) -> None:
    if isinstance(node, ast.Expression):
        _check(node.body, names)
    elif isinstance(node, ast.Constant):
        if not isinstance(node.value, (int, float)):
            raise ExprError(f"hằng không cho phép: {node.value!r}")
    elif isinstance(node, ast.Name):
        if node.id not in names and node.id not in _CONSTS:
            raise ExprError(f"tên không cho phép: {node.id}")
    elif isinstance(node, ast.BinOp):
        if not isinstance(node.op, _ALLOWED_BINOPS):
            raise ExprError(f"toán tử không cho phép: {type(node.op).__name__}")
        _check(node.left, names)
        _check(node.right, names)
    elif isinstance(node, ast.UnaryOp):
        if not isinstance(node.op, _ALLOWED_UNARY):
            raise ExprError(f"toán tử một ngôi không cho phép: {type(node.op).__name__}")
        _check(node.operand, names)
    elif isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id not in _FUNCS:
            raise ExprError("chỉ được gọi hàm trong whitelist")
        for arg in node.args:
            _check(arg, names)
        if node.keywords:
            raise ExprError("không hỗ trợ tham số keyword")
    else:
        raise ExprError(f"cú pháp không cho phép: {type(node).__name__}")


def compile_expr(expr: str, variables: Iterable[str] = ("x",)) -> Callable[..., float]:
    """Biên dịch ``expr`` thành hàm Python theo thứ tự ``variables``.

    ``^`` được coi là luỹ thừa (đổi thành ``**``). Trả về callable ném ``ExprError``
    lúc biên dịch nếu biểu thức vi phạm whitelist; lúc gọi có thể ném lỗi toán học
    (vd ``sqrt`` số âm) — phía gọi tự bắt để bỏ điểm không xác định.
    """
    names = set(variables)
    src = expr.replace("^", "**")
    try:
        tree = ast.parse(src, mode="eval")
    except SyntaxError as exc:  # pragma: no cover - thông điệp rõ ràng là đủ
        raise ExprError(f"lỗi cú pháp: {exc.msg}") from exc
    _check(tree, names)
    code = compile(tree, "<expr>", "eval")
    env = {"__builtins__": {}, **_FUNCS, **_CONSTS}
    order = list(variables)

    def fn(*args: float) -> float:
        local = dict(zip(order, args))
        return float(eval(code, env, local))  # noqa: S307 - AST đã whitelist

    fn.__doc__ = f"f({', '.join(order)}) = {expr}"
    return fn


def sample_curve(expr: str, var: str, lo: float, hi: float, n: int) -> list[tuple[float, float]]:
    """Lấy ``n`` mẫu ``(t, f(t))`` trên đoạn ``[lo, hi]``; bỏ điểm không xác định."""
    fn = compile_expr(expr, (var,))
    out: list[tuple[float, float]] = []
    if n < 2:
        n = 2
    step = (hi - lo) / (n - 1)
    for i in range(n):
        t = lo + i * step
        try:
            y = fn(t)
        except (ValueError, ZeroDivisionError, OverflowError):
            continue
        if math.isfinite(y):
            out.append((t, y))
    return out
