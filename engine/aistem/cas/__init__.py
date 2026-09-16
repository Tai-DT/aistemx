"""Lớp đại số máy tính: đọc LaTeX, kiểm chứng biến đổi, kiểm đơn vị."""

from .chemistry import check_equation, check_molar_mass, molar_mass, parse_formula, parse_side
from .dimensions import check_dimension
from .parse import evaluate_latex, sides, to_number, to_sympy
from .solver import isolate_variable_from_formula, solve_symbolic_equation, symbolic_calculus_eval
from .step_evaluator import evaluate_derivation_step, evaluate_student_solution_pipeline
from .units import check_unit, compare_with_units, convert, extract_unit, normalize_unit, parse_unit
from .verify import check_steps, equivalent, latex_equivalent, numbers_match, verify_answer

__all__ = [
    "check_dimension",
    "check_equation",
    "check_molar_mass",
    "check_steps",
    "check_unit",
    "compare_with_units",
    "convert",
    "equivalent",
    "evaluate_derivation_step",
    "evaluate_latex",
    "evaluate_student_solution_pipeline",
    "extract_unit",
    "isolate_variable_from_formula",
    "latex_equivalent",
    "molar_mass",
    "normalize_unit",
    "numbers_match",
    "parse_formula",
    "parse_side",
    "parse_unit",
    "sides",
    "solve_symbolic_equation",
    "symbolic_calculus_eval",
    "to_number",
    "to_sympy",
    "verify_answer",
]

