"""Unit tests cho module SymPy CAS solver và step_evaluator."""
import pytest

try:
    from aistem.cas.solver import (
        solve_symbolic_equation,
        isolate_variable_from_formula,
        symbolic_calculus_eval,
    )
    from aistem.cas.step_evaluator import (
        evaluate_derivation_step,
        evaluate_student_solution_pipeline,
    )
except ImportError:
    from engine.aistem.cas.solver import (
        solve_symbolic_equation,
        isolate_variable_from_formula,
        symbolic_calculus_eval,
    )
    from engine.aistem.cas.step_evaluator import (
        evaluate_derivation_step,
        evaluate_student_solution_pipeline,
    )


def test_solve_symbolic_equation():
    res = solve_symbolic_equation("x^2 - 5*x + 6 = 0", target_var="x")
    assert res["success"] is True
    assert "2" in res["solutions"] and "3" in res["solutions"]


def test_isolate_variable_from_formula():
    res = isolate_variable_from_formula("E = m * c^2", target_var="m")
    assert res["success"] is True
    assert any("E/c" in sol or "E" in sol for sol in res["isolated_str"])


def test_symbolic_calculus_eval():
    res_diff = symbolic_calculus_eval("diff", "x^3", "x")
    assert res_diff["success"] is True
    assert "3*x**2" in res_diff["result_str"]

    res_int = symbolic_calculus_eval("integrate", "x^2", "x", lower_limit="0", upper_limit="3")
    assert res_int["success"] is True
    assert "9" in res_int["result_str"]

    res_lim = symbolic_calculus_eval("limit", "sin(x)/x", "x", point_str="0")
    assert res_lim["success"] is True
    assert "1" in res_lim["result_str"]


def test_evaluate_derivation_step():
    res = evaluate_derivation_step("x^2 - 4 = 0", "(x - 2)*(x + 2) = 0", "x")
    assert res["valid"] is True
    assert res["is_strictly_equivalent"] is True

    res_loss = evaluate_derivation_step("x^2 = 2*x", "x = 2", "x")
    assert any("mất nghiệm" in w for w in res_loss["warnings"])
