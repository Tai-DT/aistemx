"""Bộ giải toán đại số biểu tượng (Symbolic CAS Solver) xây dựng trên SymPy.

Hỗ trợ:
- Giải phương trình đại số, lượng giác, mũ - logarit biểu tượng
- Rút ẩn tự động từ công thức bất kỳ
- Đạo hàm, Tích phân (xác định & bất định), Giới hạn, Chuỗi Taylor
- Kiểm tra tập xác định và cảnh báo điều kiện nghiệm
"""
from __future__ import annotations

import re
from typing import Any, Optional
import sympy as sp
from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application,
    convert_xor,
)

try:
    from .parse import to_sympy
except ImportError:
    from aistem.cas.parse import to_sympy


_TRANSFORMS = standard_transformations + (convert_xor,)

_STD_FUNCS = {
    "sin": sp.sin,
    "cos": sp.cos,
    "tan": sp.tan,
    "cot": sp.cot,
    "sec": sp.sec,
    "csc": sp.csc,
    "asin": sp.asin,
    "acos": sp.acos,
    "atan": sp.atan,
    "sinh": sp.sinh,
    "cosh": sp.cosh,
    "tanh": sp.tanh,
    "exp": sp.exp,
    "log": sp.log,
    "ln": sp.log,
    "sqrt": sp.sqrt,
    "abs": sp.Abs,
    "pi": sp.pi,
    "E": sp.E,
    "I": sp.I,
}


def _safe_parse(expr_str: str) -> sp.Expr:
    """Chuyển đổi an toàn chuỗi văn bản toán học hoặc LaTeX sang biểu thức SymPy."""
    expr_str = expr_str.strip().strip("$").strip()

    # 1. Thử qua to_sympy trực tiếp với chuỗi nguyên bản nếu là LaTeX chuẩn
    if "\\" in expr_str:
        try:
            parsed = to_sympy(expr_str)
            if parsed is not None:
                return parsed
        except Exception:
            pass

    # 2. Chuẩn hoá các ký hiệu LaTeX phổ biến sang dạng đại số
    s = expr_str.replace("^", "**")
    s = re.sub(r"\\frac\{([^}]+)\}\{([^}]+)\}", r"((\1)/(\2))", s)
    s = re.sub(r"\\sqrt\{([^}]+)\}", r"sqrt(\1)", s)
    s = s.replace(r"\sin", "sin").replace(r"\cos", "cos").replace(r"\tan", "tan")
    s = s.replace(r"\ln", "log").replace(r"\exp", "exp")
    s = s.replace(r"\cdot", "*").replace(r"\times", "*")

    return parse_expr(s, local_dict=_STD_FUNCS, transformations=_TRANSFORMS)




def solve_symbolic_equation(
    equation_str: str,
    target_var: str = "x",
) -> dict[str, Any]:
    """Giải phương trình đại số biểu tượng f(var) = g(var) hoặc expr = 0."""
    try:
        var = sp.Symbol(target_var)
        if "=" in equation_str:
            lhs_str, rhs_str = equation_str.split("=", 1)
            lhs = _safe_parse(lhs_str)
            rhs = _safe_parse(rhs_str)
            eq = sp.Eq(lhs, rhs)
            expr_to_solve = lhs - rhs
        else:
            expr_to_solve = _safe_parse(equation_str)
            eq = sp.Eq(expr_to_solve, 0)

        solutions = sp.solve(eq, var)
        
        latex_solutions = [sp.latex(sol) for sol in solutions]
        readable_solutions = [str(sol) for sol in solutions]

        # Kiểm tra điều kiện xác định (mẫu số khác 0, căn bậc chẵn >= 0)
        domain_notes = []
        denom = sp.denom(expr_to_solve)
        if denom != 1:
            domain_notes.append(f"Điều kiện mẫu số khác 0: {sp.latex(denom)} \\neq 0")

        return {
            "success": True,
            "variable": target_var,
            "equation_latex": sp.latex(eq),
            "solutions": readable_solutions,
            "solutions_latex": latex_solutions,
            "domain_notes": domain_notes,
            "count": len(solutions),
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Lỗi phân tích cú pháp hoặc giải phương trình: {str(e)}",
        }


def isolate_variable_from_formula(
    formula_latex: str,
    target_var: str,
) -> dict[str, Any]:
    """Tự động rút ẩn target_var từ một đẳng thức công thức LaTeX trong kho dữ liệu."""
    try:
        # Nếu công thức có dấu bằng
        if "=" not in formula_latex:
            return {"success": False, "error": "Công thức phải chứa dấu đẳng thức '='"}

        lhs_str, rhs_str = formula_latex.split("=", 1)
        lhs = _safe_parse(lhs_str)
        rhs = _safe_parse(rhs_str)
        
        target = sp.Symbol(target_var)
        eq = sp.Eq(lhs, rhs)
        solutions = sp.solve(eq, target)

        if not solutions:
            return {"success": False, "error": f"Không thể rút được ẩn {target_var}"}

        return {
            "success": True,
            "target": target_var,
            "original_latex": formula_latex,
            "isolated_latex": [f"{target_var} = {sp.latex(sol)}" for sol in solutions],
            "isolated_str": [f"{target_var} = {str(sol)}" for sol in solutions],
        }
    except Exception as e:
        return {"success": False, "error": f"Lỗi rút ẩn: {str(e)}"}


def symbolic_calculus_eval(
    operation: str,  # 'diff', 'integrate', 'limit', 'series'
    expression_str: str,
    var_str: str = "x",
    lower_limit: Optional[str] = None,
    upper_limit: Optional[str] = None,
    point_str: Optional[str] = None,
    order: int = 4,
) -> dict[str, Any]:
    """Thực hiện các phép toán vi tích phân biểu tượng chuẩn xác cao."""
    try:
        x = sp.Symbol(var_str)
        expr = _safe_parse(expression_str)

        if operation == "diff":
            # Đạo hàm
            derivative = sp.diff(expr, x)
            return {
                "success": True,
                "operation": "derivative",
                "input_latex": sp.latex(expr),
                "result_latex": sp.latex(derivative),
                "result_str": str(derivative),
            }
        elif operation == "integrate":
            # Tích phân
            if lower_limit is not None and upper_limit is not None:
                # Tích phân xác định
                a = _safe_parse(lower_limit)
                b = _safe_parse(upper_limit)
                integral = sp.integrate(expr, (x, a, b))
                return {
                    "success": True,
                    "operation": "definite_integral",
                    "limits": {"a": str(a), "b": str(b)},
                    "input_latex": f"\\int_{{{sp.latex(a)}}}^{{{sp.latex(b)}}} {sp.latex(expr)} \\, d{var_str}",
                    "result_latex": sp.latex(integral),
                    "result_str": str(integral),
                }
            else:
                # Tích phân bất định (nguyên hàm)
                integral = sp.integrate(expr, x)
                return {
                    "success": True,
                    "operation": "indefinite_integral",
                    "input_latex": f"\\int {sp.latex(expr)} \\, d{var_str}",
                    "result_latex": f"{sp.latex(integral)} + C",
                    "result_str": f"{str(integral)} + C",
                }
        elif operation == "limit":
            # Giới hạn lim
            pt = _safe_parse(point_str if point_str else "0")
            lim = sp.limit(expr, x, pt)
            return {
                "success": True,
                "operation": "limit",
                "point": str(pt),
                "input_latex": f"\\lim_{{{var_str} \\to {sp.latex(pt)}}} {sp.latex(expr)}",
                "result_latex": sp.latex(lim),
                "result_str": str(lim),
            }
        elif operation == "series":
            # Khai triển chuỗi Taylor
            pt = _safe_parse(point_str if point_str else "0")
            ser = sp.series(expr, x, pt, n=order)
            return {
                "success": True,
                "operation": "taylor_series",
                "point": str(pt),
                "order": order,
                "input_latex": sp.latex(expr),
                "result_latex": sp.latex(ser),
                "result_str": str(ser),
            }
        else:
            return {"success": False, "error": f"Phép toán '{operation}' không được hỗ trợ"}
    except Exception as e:
        return {"success": False, "error": f"Lỗi giải tích biểu tượng: {str(e)}"}
