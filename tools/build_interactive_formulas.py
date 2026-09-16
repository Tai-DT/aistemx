#!/usr/bin/env python3
"""Trích xuất và tham số hóa tương tác cho toàn bộ 5,272 công thức AISTEM.

Mỗi công thức được phân tích thành:
- Biến đầu ra (Output Variable & Unit)
- Danh sách biến đầu vào kèm thanh trượt (Sliders: min, max, step, default, label, unit)
- Biểu thức tính toán chuẩn JavaScript (phục vụ Frontend chạy offline 60 FPS)
- Biểu thức tính toán chuẩn Python/SymPy (phục vụ Backend CAS solver)
- Phân loại loại hình tương tác (parametric_calculator, parametric_geometry, etc.)
"""
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
FORMULAS_DIR = ROOT / "data" / "formulas"
INTERACTIVE_DIR = ROOT / "data" / "interactive"

RESERVED_KEYWORDS = {
    "default", "case", "switch", "break", "continue", "return", "function", "var",
    "let", "const", "class", "import", "export", "if", "else", "for", "while",
    "do", "try", "catch", "finally", "throw", "new", "typeof", "instanceof", "in",
    "of", "void", "delete", "yield", "await", "null", "undefined", "true", "false",
    "lambda", "is", "not", "and", "or", "def", "from", "as", "with", "pass", "global"
}


def sanitize_identifier(s: str) -> str:
    """Chuyển đổi ký hiệu LaTeX thành tên biến hợp lệ trong JS và Python."""
    s = s.strip()
    s = re.sub(r"\\\\Delta\s*|\\Delta\s*", "Delta_", s)
    s = re.sub(r"\\\\delta\s*|\\delta\s*", "delta_", s)
    s = re.sub(r"\\\\omega\s*|\\omega\s*", "omega", s)
    s = re.sub(r"\\\\alpha\s*|\\alpha\s*", "alpha", s)
    s = re.sub(r"\\\\beta\s*|\\beta\s*", "beta", s)
    s = re.sub(r"\\\\gamma\s*|\\gamma\s*", "gamma", s)
    s = re.sub(r"\\\\theta\s*|\\theta\s*", "theta", s)
    s = re.sub(r"\\\\lambda\s*|\\lambda\s*", "lambda_val", s)
    s = re.sub(r"\\\\mu\s*|\\mu\s*", "mu", s)
    s = re.sub(r"\\\\rho\s*|\\rho\s*", "rho", s)
    s = re.sub(r"\\\\sigma\s*|\\sigma\s*", "sigma", s)
    s = re.sub(r"\\\\phi\s*|\\phi\s*", "phi", s)
    s = re.sub(r"\\\\eta\s*|\\eta\s*", "eta", s)
    s = re.sub(r"\\\\tau\s*|\\tau\s*", "tau", s)
    s = re.sub(r"\\\\pi\s*|\\pi\s*", "PI_val", s)
    s = re.sub(r"\\\\([a-zA-Z]+)", r"\1", s)
    s = re.sub(r"_\{([^{}]+)\}", r"_\1", s)
    s = re.sub(r"\^\{([^{}]+)\}", r"_pow_\1", s)
    s = re.sub(r"[^a-zA-Z0-9_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")

    if not s:
        s = "var_x"
    if s[0].isdigit():
        s = "var_" + s
    if s in RESERVED_KEYWORDS:
        s = s + "_val"
    return s


def clean_latex(s: str) -> str:
    """Loại bỏ ký tự định dạng hiển thị LaTeX thuần tuý."""
    s = s.strip()
    s = re.sub(r"\\left|\\right", "", s)
    s = re.sub(r"\\qquad|\\quad|\\;|\\,|\\!|\\:", " ", s)
    s = re.sub(r"\\text\{[^{}]*\}", "", s)
    s = re.sub(r"\\mathrm\{[^{}]*\}", "", s)
    s = re.sub(r"\\mathbf\{[^{}]*\}", "", s)
    s = re.sub(r"\\displaystyle", "", s)
    return s.strip()


def latex_to_js(expr: str, var_substitutions: Dict[str, str]) -> str:
    """Chuyển đổi biểu thức toán LaTeX sang JavaScript có thể chạy được."""
    s = clean_latex(expr)
    s = re.sub(r"\\cdot|\\times", " * ", s)
    s = re.sub(r"\\pi", "Math.PI", s)
    s = re.sub(r"\\infty", "Infinity", s)

    # Thay thế các biến LaTeX phức tạp bằng tên định danh hợp lệ
    for raw_sym, clean_sym in sorted(var_substitutions.items(), key=lambda x: -len(x[0])):
        if raw_sym and raw_sym in s:
            pattern = re.escape(raw_sym)
            s = re.sub(pattern, clean_sym, s)

    # Xử lý phân số lồng nhau \frac{a}{b} hoặc \dfrac{a}{b}
    for _ in range(5):
        s = re.sub(r"\\d?frac\{([^{}]+)\}\{([^{}]+)\}", r"((\1) / (\2))", s)

    # Xử lý căn bậc hai \sqrt{a}
    for _ in range(3):
        s = re.sub(r"\\sqrt\{([^{}]+)\}", r"Math.sqrt(\1)", s)
    s = re.sub(r"\\sqrt\s*([a-zA-Z0-9_]+)", r"Math.sqrt(\1)", s)

    # Xử lý lũy thừa x^{y} hoặc x^2
    s = re.sub(r"([a-zA-Z0-9_\(\)]+)\^\{([^{}]+)\}", r"Math.pow(\1, \2)", s)
    s = re.sub(r"([a-zA-Z0-9_\(\)]+)\^([a-zA-Z0-9_])", r"Math.pow(\1, \2)", s)

    # Dọn sạch các dấu ngoặc nhọn subscript còn sót lại
    s = re.sub(r"_\{([^{}]+)\}", r"_\1", s)
    s = re.sub(r"[{}]", "", s)

    # Hàm lượng giác & siêu việt
    s = re.sub(r"\\sin", "Math.sin", s)
    s = re.sub(r"\\cos", "Math.cos", s)
    s = re.sub(r"\\tan", "Math.tan", s)
    s = re.sub(r"\\arcsin", "Math.asin", s)
    s = re.sub(r"\\arccos", "Math.acos", s)
    s = re.sub(r"\\arctan", "Math.atan", s)
    s = re.sub(r"\\ln", "Math.log", s)
    s = re.sub(r"\\log_10|\\log", "Math.log10", s)
    s = re.sub(r"\\exp", "Math.exp", s)
    s = re.sub(r"\\approx|\\equiv", " == ", s)

    # Dọn dẹp khoảng trắng dư thừa
    s = re.sub(r"\s+", " ", s).strip()

    # Chuyển đổi phép nhân ẩn (implicit multiplication) thành phép nhân tường minh (*)
    s = re.sub(r"(\b\d+(?:\.\d+)?)\s*([a-zA-Z_])", r"\1 * \2", s)
    s = re.sub(r"(\))\s*([a-zA-Z0-9_])", r"\1 * \2", s)
    s = re.sub(r"(\b\d+(?:\.\d+)?)\s*(\()", r"\1 * \2", s)
    s = re.sub(r"([a-zA-Z0-9_\)])\s+([a-zA-Z_])", r"\1 * \2", s)
    s = re.sub(r"([a-zA-Z0-9_\)])\s+(Math\.)", r"\1 * \2", s)
    s = re.sub(r"(\))\s*(\()", r"\1 * \2", s)
    return s.strip()


def latex_to_py(expr: str, var_substitutions: Dict[str, str]) -> str:
    """Chuyển đổi biểu thức toán LaTeX sang Python / SymPy."""
    s = clean_latex(expr)
    s = re.sub(r"\\cdot|\\times", " * ", s)
    s = re.sub(r"\\pi", "pi", s)
    s = re.sub(r"\\infty", "oo", s)

    for raw_sym, clean_sym in sorted(var_substitutions.items(), key=lambda x: -len(x[0])):
        if raw_sym and raw_sym in s:
            pattern = re.escape(raw_sym)
            s = re.sub(pattern, clean_sym, s)

    for _ in range(5):
        s = re.sub(r"\\d?frac\{([^{}]+)\}\{([^{}]+)\}", r"((\1) / (\2))", s)

    for _ in range(3):
        s = re.sub(r"\\sqrt\{([^{}]+)\}", r"sqrt(\1)", s)
    s = re.sub(r"\\sqrt\s*([a-zA-Z0-9_]+)", r"sqrt(\1)", s)

    # Lũy thừa kiểu Python
    s = re.sub(r"([a-zA-Z0-9_\(\)]+)\^\{([^{}]+)\}", r"(\1)**(\2)", s)
    s = re.sub(r"([a-zA-Z0-9_\(\)]+)\^([a-zA-Z0-9_])", r"(\1)**(\2)", s)

    s = re.sub(r"_\{([^{}]+)\}", r"_\1", s)
    s = re.sub(r"[{}]", "", s)

    s = re.sub(r"\\sin", "sin", s)
    s = re.sub(r"\\cos", "cos", s)
    s = re.sub(r"\\tan", "tan", s)
    s = re.sub(r"\\ln", "log", s)
    s = re.sub(r"\\exp", "exp", s)
    s = re.sub(r"\s+", " ", s).strip()

    # Nhân ẩn trong Python
    s = re.sub(r"(\b\d+(?:\.\d+)?)\s*([a-zA-Z_])", r"\1 * \2", s)
    s = re.sub(r"(\))\s*([a-zA-Z0-9_])", r"\1 * \2", s)
    s = re.sub(r"(\b\d+(?:\.\d+)?)\s*(\()", r"\1 * \2", s)
    s = re.sub(r"([a-zA-Z0-9_\)])\s+([a-zA-Z_])", r"\1 * \2", s)
    s = re.sub(r"(\))\s*(\()", r"\1 * \2", s)
    return s.strip()


def infer_slider_range(symbol: str, label: str, unit: str, subject: str) -> Tuple[float, float, float, float]:
    """Suy luận dải giá trị mặc định (default, min, max, step) thông minh cho slider."""
    sym_lower = symbol.lower()
    lbl_lower = label.lower()

    # Góc (rad hoặc độ)
    if "góc" in lbl_lower or "angle" in lbl_lower or "alpha" in sym_lower or "beta" in sym_lower or "theta" in sym_lower or "phi" in sym_lower:
        if "độ" in unit or "deg" in unit:
            return (45.0, 0.0, 360.0, 1.0)
        return (0.785, 0.0, 6.283, 0.05)  # pi/4 rad

    # Tần số / chu kỳ / thời gian
    if "thời gian" in lbl_lower or "chu kỳ" in lbl_lower or sym_lower in {"t", "t_0", "delta_t"}:
        return (2.0, 0.1, 60.0, 0.1)

    # Tần số
    if "tần số" in lbl_lower or sym_lower in {"f", "omega", "nu"}:
        return (5.0, 0.5, 100.0, 0.5)

    # Khối lượng
    if "khối lượng" in lbl_lower or sym_lower in {"m", "m_1", "m_2", "m_0"}:
        return (2.0, 0.1, 100.0, 0.1)

    # Bán kính / Khoảng cách / Chiều dài
    if "bán kính" in lbl_lower or "khoảng cách" in lbl_lower or "chiều dài" in lbl_lower or sym_lower in {"r", "r_1", "r_2", "d", "l", "h", "a", "b", "c", "x", "y", "z"}:
        return (3.0, 0.5, 50.0, 0.5)

    # Vận tốc / Tốc độ
    if "vận tốc" in lbl_lower or "tốc độ" in lbl_lower or sym_lower in {"v", "v_0", "u"}:
        return (10.0, 0.0, 100.0, 1.0)

    # Gia tốc
    if "gia tốc" in lbl_lower or sym_lower in {"a", "g"}:
        return (9.8, 0.1, 30.0, 0.1)

    # Điện áp, Cường độ dòng điện, Điện trở
    if "điện áp" in lbl_lower or "hiệu điện thế" in lbl_lower or sym_lower == "u":
        return (220.0, 1.0, 500.0, 5.0)
    if "dòng điện" in lbl_lower or sym_lower in {"i", "i_0"}:
        return (2.0, 0.1, 20.0, 0.1)
    if "điện trở" in lbl_lower or sym_lower in {"r", "r_1", "r_2"}:
        return (50.0, 1.0, 500.0, 5.0)

    # Nhiệt độ (Kelvin)
    if "nhiệt độ" in lbl_lower or sym_lower == "t":
        return (298.15, 200.0, 1000.0, 5.0)

    # Nồng độ mol, Số mol
    if "nồng độ" in lbl_lower or "số mol" in lbl_lower or sym_lower in {"n", "c_m", "c_pt"}:
        return (1.0, 0.01, 10.0, 0.05)

    # Áp suất
    if "áp suất" in lbl_lower or sym_lower == "p":
        return (1.0, 0.1, 50.0, 0.5)

    # Mặc định an toàn
    return (2.0, 0.1, 20.0, 0.1)


def categorize_interactive_type(formula: Dict[str, Any]) -> str:
    """Xác định loại hình tương tác phù hợp."""
    subj = formula.get("subject", "")
    topic = (formula.get("topic") or "").lower()
    subtopic = (formula.get("subtopic") or "").lower()
    name = (formula.get("name_vi") or "").lower()
    latex = formula.get("latex", "")

    if "=" not in latex and ("\\rightarrow" in latex or "\\iff" in latex or "\\begin{cases}" in latex):
        return "qualitative_simulation"

    if subj == "math":
        if any(k in topic or k in subtopic or k in name for k in ["không gian", "oxyz", "thể tích", "hình học", "mặt cầu", "mặt phẳng", "nón", "trụ", "khối"]):
            return "parametric_geometry_3d"
        return "parametric_calculator"

    if subj == "physics":
        if any(k in topic or k in subtopic or k in name for k in ["sóng", "dao động", "quang", "điện trường", "từ trường"]):
            return "parametric_physics_simulation"
        return "parametric_calculator"

    if subj == "chemistry":
        if "cấu tạo" in topic or "phân tử" in subtopic:
            return "parametric_chemistry_3d"
        return "parametric_calculator"

    if subj == "biology":
        return "parametric_biology_model"

    return "parametric_calculator"


def build_interactive_entry(formula: Dict[str, Any]) -> Dict[str, Any]:
    """Tạo bản ghi cấu hình tương tác chuẩn mực cho 1 công thức."""
    fid = formula["id"]
    name_vi = formula["name_vi"]
    subj = formula["subject"]
    latex = formula.get("latex", "").strip()
    vars_map = formula.get("vars", {})
    units_map = formula.get("units", {})
    itype = categorize_interactive_type(formula)

    # Lập bản đồ chuẩn hoá định danh cho mọi biến
    var_substitutions = {}
    for raw_k in vars_map.keys():
        var_substitutions[raw_k] = sanitize_identifier(raw_k)

    # 1. Trường hợp công thức có dấu bằng (Quantitative Equation)
    if "=" in latex:
        parts = latex.split("=", 1)
        lhs_raw = parts[0].strip()
        rhs_raw = parts[1].strip()

        # Rút ký hiệu đại lượng đầu ra
        out_symbol = sanitize_identifier(clean_latex(lhs_raw))
        out_name = vars_map.get(out_symbol) or vars_map.get(lhs_raw) or name_vi
        out_unit = units_map.get(out_symbol) or units_map.get(lhs_raw) or ""

        # Tìm các biến đầu vào ở vế phải xuất hiện trong vars_map
        input_sliders = []
        for var_sym, var_desc in vars_map.items():
            clean_sym = var_substitutions[var_sym]
            # Bỏ qua đại lượng đầu ra
            if clean_sym == out_symbol or var_sym == lhs_raw:
                continue

            unit_val = units_map.get(var_sym) or ""
            default_val, min_val, max_val, step_val = infer_slider_range(clean_sym, var_desc, unit_val, subj)

            input_sliders.append({
                "symbol": clean_sym,
                "raw_symbol": var_sym,
                "label": var_desc,
                "unit": unit_val,
                "default": default_val,
                "min": min_val,
                "max": max_val,
                "step": step_val,
            })

        # Nếu không tìm thấy biến nào qua vars_map, tạo 1 biến mặc định nếu vế phải có biến
        if not input_sliders:
            input_sliders.append({
                "symbol": "x",
                "raw_symbol": "x",
                "label": "Biến số đầu vào",
                "unit": "",
                "default": 2.0,
                "min": 0.1,
                "max": 20.0,
                "step": 0.1,
            })

        expr_js = latex_to_js(rhs_raw, var_substitutions)
        expr_py = latex_to_py(rhs_raw, var_substitutions)

        return {
            "formula_id": fid,
            "name_vi": name_vi,
            "subject": subj,
            "interactive_type": itype,
            "is_computable": True,
            "output": {
                "symbol": out_symbol,
                "raw_symbol": lhs_raw,
                "name": out_name,
                "unit": out_unit,
            },
            "expression_js": expr_js,
            "expression_py": expr_py,
            "inputs": input_sliders,
        }

    # 2. Trường hợp định tính hoặc phản ứng (Qualitative / Reaction / Non-equal)
    else:
        qualitative_items = []
        for var_sym, var_desc in vars_map.items():
            qualitative_items.append({
                "symbol": var_substitutions.get(var_sym, sanitize_identifier(var_sym)),
                "raw_symbol": var_sym,
                "label": var_desc,
                "unit": units_map.get(var_sym, ""),
            })

        return {
            "formula_id": fid,
            "name_vi": name_vi,
            "subject": subj,
            "interactive_type": itype,
            "is_computable": False,
            "output": {
                "symbol": "Result",
                "raw_symbol": "Result",
                "name": name_vi,
                "unit": "",
            },
            "expression_js": "",
            "expression_py": "",
            "inputs": qualitative_items,
        }


def main():
    print("=" * 65)
    print("🚀 BẮT ĐẦU XÂY DỰNG DỮ LIỆU TƯƠNG TÁC TOÀN DIỆN CHO 5,272 CÔNG THỨC")
    print("=" * 65)

    slice_files = sorted(FORMULAS_DIR.glob("*/*.json"))
    if not slice_files:
        print("❌ Không tìm thấy các file lát cắt công thức!")
        sys.exit(1)

    INTERACTIVE_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Tạo Schema cho kho tương tác
    schema_path = INTERACTIVE_DIR / "schema.json"
    schema_doc = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "AISTEM Interactive Formula Config",
        "description": "Cấu hình tham số hoá tương tác và máy tính thời gian thực cho công thức AISTEM.",
        "type": "object",
        "required": ["formula_id", "name_vi", "subject", "interactive_type", "is_computable", "output", "inputs"],
        "properties": {
            "formula_id": { "type": "string" },
            "name_vi": { "type": "string" },
            "subject": { "type": "string" },
            "interactive_type": { "type": "string" },
            "is_computable": { "type": "boolean" },
            "output": { "type": "object" },
            "expression_js": { "type": "string" },
            "expression_py": { "type": "string" },
            "inputs": { "type": "array" }
        }
    }
    schema_path.write_text(json.dumps(schema_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ Đã tạo schema tại: {schema_path}")

    # 2. Xử lý toàn bộ công thức
    all_interactive = {}
    type_counts = {}
    computable_count = 0
    total_formulas = 0

    for sfile in slice_files:
        try:
            data = json.loads(sfile.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"⚠️ Lỗi đọc file {sfile}: {e}")
            continue

        formulas = data.get("formulas", [])
        for f in formulas:
            entry = build_interactive_entry(f)
            fid = entry["formula_id"]
            all_interactive[fid] = entry
            total_formulas += 1

            if entry["is_computable"]:
                computable_count += 1

            itype = entry["interactive_type"]
            type_counts[itype] = type_counts.get(itype, 0) + 1

    # 3. Xuất ra data/interactive/index.json
    index_path = INTERACTIVE_DIR / "index.json"
    index_data = {
        "version": "aistem-interactive-v1",
        "total_formulas": total_formulas,
        "computable_count": computable_count,
        "type_counts": type_counts,
        "formulas": all_interactive,
    }
    index_path.write_text(json.dumps(index_data, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n🎉 HOÀN THÀNH XÂY DỰNG DỮ LIỆU TƯƠNG TÁC CHO {total_formulas:,} CÔNG THỨC!")
    print(f"📂 File lưu trữ: {index_path} ({index_path.stat().st_size / (1024*1024):.2f} MB)")
    print(f"⚡ Công thức có thể tính toán động (Computable): {computable_count:,} ({computable_count/total_formulas*100:.1f}%)")
    print("\n📊 Phân bố loại hình tương tác:")
    for tname, cnt in sorted(type_counts.items(), key=lambda x: -x[1]):
        print(f"   • {tname:<32}: {cnt:,}")


if __name__ == "__main__":
    main()
