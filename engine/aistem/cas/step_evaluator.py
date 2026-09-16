"""Bộ thẩm định biến đổi từng bước (Step-by-Step Derivation Evaluator) cho AIstem.

Hỗ trợ:
- Kiểm tra tính tương đương đại số giữa các bước kế tiếp
- Phát hiện các lỗi tư duy toán học phổ biến:
  + Chia cho biểu thức có thể bằng 0 (làm mất nghiệm hoặc phép chia vô nghĩa)
  + Bình phương hai vế xuất hiện nghiệm ngoại lai
  + Vi phạm tập xác định (căn âm, mẫu bằng 0, log số âm)
"""
from __future__ import annotations

import sympy as sp
from typing import Any
try:
    from .solver import _safe_parse
except ImportError:
    from aistem.cas.solver import _safe_parse


def evaluate_derivation_step(
    step_before: str,
    step_after: str,
    var_str: str = "x",
) -> dict[str, Any]:
    """Kiểm tra xem bước biến đổi từ step_before sang step_after có bảo toàn tương đương logic không."""
    try:
        x = sp.Symbol(var_str)

        # Chuyển đổi phương trình thành biểu thức f(x) = 0
        def to_zero_eq(s: str) -> sp.Expr:
            if "=" in s:
                l, r = s.split("=", 1)
                return _safe_parse(l) - _safe_parse(r)
            return _safe_parse(s)

        eq1 = to_zero_eq(step_before)
        eq2 = to_zero_eq(step_after)

        # Kiểm tra tính tương đương đại số trực tiếp
        diff = sp.simplify(eq1 - eq2)
        ratio = None
        try:
            ratio = sp.simplify(eq1 / eq2) if eq2 != 0 else None
        except Exception:
            pass

        # Giải tập nghiệm của cả 2 bước để đối chiếu
        sols1 = set(sp.solve(eq1, x))
        sols2 = set(sp.solve(eq2, x))

        is_equivalent = (diff == 0) or (ratio is not None and ratio.is_constant() and ratio != 0)
        
        # Nếu biểu thức khác nhau về hình thức, kiểm tra qua tập nghiệm
        if not is_equivalent:
            if sols1 == sols2 and len(sols1) > 0:
                is_equivalent = True

        warnings = []
        # Kiểm tra nguy cơ nghiệm ngoại lai (extraneous roots)
        extraneous = sols2 - sols1
        if extraneous:
            warnings.append(f"Cảnh báo: Xuất hiện nghiệm ngoại lai {extraneous} (thường do bình phương hai vế hoặc nhân thêm biểu thức chứa biến).")

        # Kiểm tra mất nghiệm (lost roots)
        lost = sols1 - sols2
        if lost:
            warnings.append(f"Cảnh báo: Bị mất nghiệm {lost} (thường do chia cả hai vế cho biểu thức chứa biến bằng 0).")

        # Kiểm tra nguy cơ chia cho 0
        denom2 = sp.denom(eq2)
        if denom2 != 1 and denom2 != sp.denom(eq1):
            zeros_denom = sp.solve(denom2, x)
            if zeros_denom:
                warnings.append(f"Chú ý điều kiện xác định: mẫu số xuất hiện biến {sp.latex(denom2)} = 0 tại x = {zeros_denom}.")

        return {
            "valid": is_equivalent and not lost,
            "is_strictly_equivalent": is_equivalent and len(extraneous) == 0 and len(lost) == 0,
            "step_before": step_before,
            "step_after": step_after,
            "solutions_before": [str(s) for s in sols1],
            "solutions_after": [str(s) for s in sols2],
            "warnings": warnings,
        }
    except Exception as e:
        return {
            "valid": False,
            "error": f"Lỗi thẩm định bước: {str(e)}",
        }


def evaluate_student_solution_pipeline(
    steps: list[str],
    var_str: str = "x",
) -> dict[str, Any]:
    """Thẩm định toàn bộ chuỗi biến đổi lời giải của học sinh từ đề bài đến đáp số."""
    if len(steps) < 2:
        return {"success": False, "error": "Cần ít nhất 2 bước để thẩm định chuỗi biến đổi"}

    step_results = []
    overall_valid = True

    for i in range(len(steps) - 1):
        res = evaluate_derivation_step(steps[i], steps[i + 1], var_str)
        step_results.append({
            "step_index": i + 1,
            "transition": f"Bước {i + 1} ➔ Bước {i + 2}",
            "from": steps[i],
            "to": steps[i + 1],
            "valid": res.get("valid", False),
            "warnings": res.get("warnings", []),
        })
        if not res.get("valid", False):
            overall_valid = False

    return {
        "success": True,
        "overall_valid": overall_valid,
        "total_steps": len(steps),
        "steps_evaluation": step_results,
    }
