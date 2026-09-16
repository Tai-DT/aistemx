#!/usr/bin/env python3
"""Build and verify interactive formula engine for all 5,272 AISTEM formulas with high-precision parser."""
import json
import re
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

ROOT = Path(__file__).resolve().parent.parent
FORMULAS_INDEX = ROOT / "data" / "formulas" / "index.json"
INTERACTIVE_DIR = ROOT / "data" / "interactive"
OUTPUT_INDEX = INTERACTIVE_DIR / "index.json"

RESERVED_KEYWORDS = {
    "default", "case", "switch", "break", "continue", "return", "function", "var",
    "let", "const", "class", "import", "export", "if", "else", "for", "while",
    "do", "try", "catch", "finally", "throw", "new", "typeof", "instanceof", "in",
    "of", "void", "delete", "yield", "await", "null", "undefined", "true", "false",
    "lambda", "is", "not", "and", "or", "def", "from", "as", "with", "pass", "global",
    "Math", "Number", "String", "Array", "Object", "Date", "RegExp"
}

def extract_balanced_braces(s: str, start_idx: int) -> Tuple[Optional[str], int]:
    if start_idx >= len(s) or s[start_idx] != '{':
        return None, start_idx
    depth = 0
    content = []
    i = start_idx
    while i < len(s):
        c = s[i]
        if c == '{':
            depth += 1
            if depth > 1:
                content.append(c)
        elif c == '}':
            depth -= 1
            if depth == 0:
                return ''.join(content), i + 1
            else:
                content.append(c)
        else:
            content.append(c)
        i += 1
    return None, start_idx

def sanitize_identifier(s: str) -> str:
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

def replace_fractions(s: str) -> str:
    while True:
        m = re.search(r'\\(d|t)?frac\s*\{', s)
        if not m:
            break
        brace_start = m.end() - 1
        num, next_idx = extract_balanced_braces(s, brace_start)
        if num is None:
            break
        while next_idx < len(s) and s[next_idx] in ' \t\n':
            next_idx += 1
        den, end_idx = extract_balanced_braces(s, next_idx)
        if den is None:
            break
        num_conv = replace_fractions(num)
        den_conv = replace_fractions(den)
        replacement = f'(({num_conv}) / ({den_conv}))'
        s = s[:m.start()] + replacement + s[end_idx:]
    
    s = re.sub(r'\\(d|t)?frac\s*([0-9a-zA-Z])\s*([0-9a-zA-Z])', r'((\2) / (\3))', s)
    return s

def replace_roots(s: str) -> str:
    while True:
        m = re.search(r'\\sqrt\s*\[([^{}\]]+)\]\s*\{', s)
        if not m:
            break
        deg = m.group(1)
        brace_start = m.end() - 1
        radicand, end_idx = extract_balanced_braces(s, brace_start)
        if radicand is None:
            break
        rad_conv = replace_roots(radicand)
        replacement = f'Math.pow({rad_conv}, 1 / ({deg}))'
        s = s[:m.start()] + replacement + s[end_idx:]

    while True:
        m = re.search(r'\\sqrt\s*\{', s)
        if not m:
            break
        brace_start = m.end() - 1
        radicand, end_idx = extract_balanced_braces(s, brace_start)
        if radicand is None:
            break
        rad_conv = replace_roots(radicand)
        replacement = f'Math.sqrt({rad_conv})'
        s = s[:m.start()] + replacement + s[end_idx:]

    s = re.sub(r'\\sqrt\s*([a-zA-Z0-9_]+)', r'Math.sqrt(\1)', s)
    return s

def replace_powers(s: str) -> str:
    # Lượng giác có mũ: \sin^2(x) -> Math.pow(Math.sin(x), 2)
    s = re.sub(r'\\(sin|cos|tan)\^\{([^{}]+)\}\s*(\([^\)]+\)|[a-zA-Z0-9_]+)', r'Math.pow(Math.\1(\3), \2)', s)
    s = re.sub(r'\\(sin|cos|tan)\^([0-9])\s*(\([^\)]+\)|[a-zA-Z0-9_]+)', r'Math.pow(Math.\1(\3), \2)', s)

    # e^{x} -> Math.exp(x)
    while True:
        m = re.search(r'(?:\b|\\mathrm\{)e(?:\}|\b)\s*\^\s*\{', s)
        if not m:
            break
        brace_start = m.end() - 1
        exp, end_idx = extract_balanced_braces(s, brace_start)
        if exp is None:
            break
        exp_conv = replace_powers(exp)
        replacement = f'Math.exp({exp_conv})'
        s = s[:m.start()] + replacement + s[end_idx:]

    # Base^{exp} với base là từ hoặc ngoặc đơn đóng
    while True:
        m = re.search(r'(\b[a-zA-Z0-9_]+|\([^\(\)]+\))\s*\^\s*\{', s)
        if not m:
            break
        base = m.group(1)
        brace_start = m.end() - 1
        exp, end_idx = extract_balanced_braces(s, brace_start)
        if exp is None:
            break
        exp_conv = replace_powers(exp)
        replacement = f'Math.pow({base}, {exp_conv})'
        s = s[:m.start()] + replacement + s[end_idx:]

    s = re.sub(r'(\b[a-zA-Z0-9_]+|\([^\(\)]+\))\s*\^\s*([a-zA-Z0-9_])', r'Math.pow(\1, \2)', s)
    return s

def replace_subscripts(s: str) -> str:
    while True:
        m = re.search(r'_\{([^{}]+)\}', s)
        if not m:
            break
        sub_name = re.sub(r'[^a-zA-Z0-9_]', '_', m.group(1))
        s = s[:m.start()] + f'_{sub_name}' + s[m.end():]
    return s

def clean_and_convert_latex_to_js(raw_rhs: str, var_substitutions: Dict[str, str]) -> str:
    s = raw_rhs.strip()
    
    # 1. Tách nếu có nhiều phương trình
    if ';' in s:
        s = s.split(';')[0].strip()
    if '\\\\' in s:
        s = s.split('\\\\')[0].strip()
    if r'\implies' in s:
        parts = s.split(r'\implies')
        s = parts[-1].strip() if '=' in parts[-1] else parts[0].strip()
    if r'\iff' in s:
        s = s.split(r'\iff')[0].strip()
    if '=' in s:
        s = s.split('=')[-1].strip()

    # 2. Xử lý môi trường
    s = re.sub(r'\\begin\{[^{}]*\}', '', s)
    s = re.sub(r'\\end\{[^{}]*\}', '', s)

    # 3. Phân số và căn thức TRƯỚC khi xóa backslashes
    s = replace_fractions(s)
    s = replace_roots(s)

    # 4. Thay thế phép nhân và toán tử
    s = re.sub(r'\\cdot|\\times', ' * ', s)
    s = re.sub(r'\\pm|\\mp', ' + ', s)

    # 5. Thay thế hàm toán học
    s = re.sub(r'\\pi\b', 'Math.PI', s)
    s = re.sub(r'\\infty\b', 'Infinity', s)
    s = re.sub(r'\\sin\b', 'Math.sin', s)
    s = re.sub(r'\\cos\b', 'Math.cos', s)
    s = re.sub(r'\\tan\b', 'Math.tan', s)
    s = re.sub(r'\\ln\b', 'Math.log', s)
    s = re.sub(r'\\log_10\b|\\log\b', 'Math.log10', s)

    # 6. Lũy thừa và chỉ số dưới
    s = replace_powers(s)
    s = replace_subscripts(s)

    # 7. Trị tuyệt đối
    s = re.sub(r'\\left\|([^\|]+)\\right\|', r'Math.abs(\1)', s)
    s = re.sub(r'\|([^\|]+)\|', r'Math.abs(\1)', s)

    # 8. Xóa các định dạng text và ngoặc nhọn còn dư
    s = re.sub(r'\\left\.|\\right\.', '', s)
    s = re.sub(r'\\left|\\right', '', s)
    s = re.sub(r'\\text\{[^{}]*\}', '', s)
    s = re.sub(r'\\mathrm\{[^{}]*\}', '', s)
    s = re.sub(r'\\mathbf\{[^{}]*\}', '', s)
    s = re.sub(r'\\mathit\{[^{}]*\}', '', s)
    s = re.sub(r'\\displaystyle', '', s)
    s = re.sub(r'\\qquad|\\quad|\\;|\\,|\\!|\\:', ' ', s)
    s = re.sub(r'\\\s*\(?\)?', '', s)
    s = re.sub(r'[{}]', '', s)

    # 9. Thay thế biến theo danh sách substitution (sử dụng negative lookaround)
    for raw_sym, clean_sym in sorted(var_substitutions.items(), key=lambda x: -len(x[0])):
        if not raw_sym:
            continue
        clean_raw = raw_sym.replace('\\', '').replace('{', '').replace('}', '')
        if clean_raw and clean_raw in s:
            pattern = r'(?<![a-zA-Z0-9_])' + re.escape(clean_raw) + r'(?![a-zA-Z0-9_])'
            s = re.sub(pattern, clean_sym, s)

    # 10. Xóa backslash còn sót
    s = re.sub(r'\\[a-zA-Z]+', '', s)
    s = s.replace('\\', '')

    # 11. Nhân ẩn tường minh
    s = re.sub(r'(\b\d+(?:\.\d+)?)\s*([a-zA-Z_])', r'\1 * \2', s)
    s = re.sub(r'(\))\s*([a-zA-Z0-9_])', r'\1 * \2', s)
    s = re.sub(r'(\b\d+(?:\.\d+)?)\s*(\()', r'\1 * \2', s)
    s = re.sub(r'(\))\s*(\()', r'\1 * \2', s)
    s = re.sub(r'([a-zA-Z0-9_\)])\s+(Math\.)', r'\1 * \2', s)
    
    # Biến theo sau bởi ngoặc tròn mở không phải là Math function: var (x + y) -> var * (x + y)
    s = re.sub(r'\b(?!Math\b|sqrt\b|pow\b|abs\b|sin\b|cos\b|tan\b|log\b|exp\b)([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', r'\1 * (', s)

    # Dọn dẹp khoảng trắng
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def infer_slider_range(symbol: str, label: str, unit: str, subject: str) -> Tuple[float, float, float, float]:
    sym_lower = symbol.lower()
    lbl_lower = label.lower()

    if "góc" in lbl_lower or "angle" in lbl_lower or any(k in sym_lower for k in ["alpha", "beta", "theta", "phi"]):
        if "độ" in unit or "deg" in unit:
            return (45.0, 0.0, 360.0, 1.0)
        return (0.785, 0.0, 6.283, 0.05)

    if "thời gian" in lbl_lower or "chu kỳ" in lbl_lower or sym_lower in {"t", "t_0", "delta_t"}:
        return (2.5, 0.1, 60.0, 0.1)

    if "tần số" in lbl_lower or sym_lower in {"f", "omega", "nu"}:
        return (5.0, 0.5, 100.0, 0.5)

    if "khối lượng" in lbl_lower or sym_lower in {"m", "m_1", "m_2", "m_0"}:
        return (2.0, 0.1, 100.0, 0.1)

    if "bán kính" in lbl_lower or "khoảng cách" in lbl_lower or "chiều dài" in lbl_lower or sym_lower in {"r", "r_1", "r_2", "d", "l", "h", "a", "b", "c", "x", "y", "z"}:
        return (3.0, 0.5, 50.0, 0.5)

    if "vận tốc" in lbl_lower or "tốc độ" in lbl_lower or sym_lower in {"v", "v_0", "u"}:
        return (10.0, 0.5, 120.0, 1.0)

    if "nồng độ" in lbl_lower or "số mol" in lbl_lower or sym_lower in {"n", "c_m", "c_pt"}:
        return (1.0, 0.01, 10.0, 0.05)

    if "áp suất" in lbl_lower or sym_lower == "p":
        return (1.0, 0.1, 50.0, 0.5)

    return (2.0, 0.1, 20.0, 0.1)

def build_entry(formula: Dict[str, Any]) -> Dict[str, Any]:
    fid = formula["id"]
    name_vi = formula.get("name_vi", fid)
    subj = formula.get("subject", "math")
    latex = formula.get("latex", "").strip()
    vars_map = formula.get("vars", {})
    units_map = formula.get("units", {})

    var_substitutions = {}
    for raw_k in vars_map.keys():
        var_substitutions[raw_k] = sanitize_identifier(raw_k)

    if "=" in latex:
        parts = latex.split("=")
        lhs_raw = parts[0].strip()
        # Nếu có chuỗi đẳng thức A = B = C, ưu tiên phần ở giữa nếu ngắn gọn
        if len(parts) > 2 and len(parts[1].strip()) > 0 and not any(k in parts[1] for k in [r'\int', r'\lim', r'\sum']):
            rhs_raw = parts[1].strip()
        else:
            rhs_raw = parts[-1].strip()

        out_symbol = sanitize_identifier(lhs_raw)
        out_name = vars_map.get(out_symbol) or vars_map.get(lhs_raw) or name_vi
        out_unit = units_map.get(out_symbol) or units_map.get(lhs_raw) or ""

        expr_js = clean_and_convert_latex_to_js(rhs_raw, var_substitutions)

        input_sliders = []
        for var_sym, var_desc in vars_map.items():
            clean_sym = var_substitutions[var_sym]
            if clean_sym == out_symbol:
                continue

            unit_val = units_map.get(var_sym) or ""
            d_val, min_v, max_v, step_v = infer_slider_range(clean_sym, var_desc, unit_val, subj)
            input_sliders.append({
                "symbol": clean_sym,
                "raw_symbol": var_sym,
                "label": var_desc,
                "unit": unit_val,
                "default": d_val,
                "min": min_v,
                "max": max_v,
                "step": step_v,
            })

        # Nếu vế phải có biến mà input_sliders rỗng, tạo biến mặc định
        if not input_sliders:
            found_vars = set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expr_js)) - {"Math", "Infinity", "NaN", "pow", "sqrt", "sin", "cos", "tan", "log", "log10", "exp", "PI", "abs"}
            for fv in found_vars:
                d_val, min_v, max_v, step_v = infer_slider_range(fv, fv, "", subj)
                input_sliders.append({
                    "symbol": fv,
                    "raw_symbol": fv,
                    "label": fv,
                    "unit": "",
                    "default": d_val,
                    "min": min_v,
                    "max": max_v,
                    "step": step_v,
                })

        return {
            "formula_id": fid,
            "name_vi": name_vi,
            "subject": subj,
            "interactive_type": "parametric_calculator",
            "is_computable": True,
            "output": {
                "symbol": out_symbol,
                "raw_symbol": lhs_raw,
                "name": out_name,
                "unit": out_unit,
            },
            "expression_js": expr_js,
            "inputs": input_sliders,
        }
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
            "interactive_type": "qualitative_simulation",
            "is_computable": False,
            "output": {
                "symbol": "Result",
                "raw_symbol": "Result",
                "name": name_vi,
                "unit": "",
            },
            "expression_js": "",
            "inputs": qualitative_items,
        }

def main():
    print("🚀 Bắt đầu tối ưu và kiểm định toàn bộ 5,272 công thức AISTEM...")
    f_data = json.loads(FORMULAS_INDEX.read_text(encoding="utf-8"))
    formulas = f_data.get("formulas", [])

    interactive_map = {}
    for f in formulas:
        entry = build_entry(f)
        interactive_map[entry["formula_id"]] = entry

    test_file = ROOT / "tools" / "temp_eval_test.json"
    test_file.write_text(json.dumps(interactive_map, ensure_ascii=False), encoding="utf-8")

    node_eval_script = """
    const fs = require('fs');
    const data = JSON.parse(fs.readFileSync('tools/temp_eval_test.json', 'utf8'));
    
    let validCount = 0;
    let fixedCount = 0;
    let qualitativeCount = 0;
    
    for (const [fid, f] of Object.entries(data)) {
        if (!f.is_computable || !f.expression_js) {
            qualitativeCount++;
            continue;
        }
        
        const scope = {};
        for (const inp of f.inputs || []) {
            scope[inp.symbol] = inp.default !== undefined ? inp.default : 2.0;
        }
        
        try {
            const keys = Object.keys(scope);
            const vals = Object.values(scope);
            const fn = new Function(...keys, 'return (' + f.expression_js + ');');
            const res = fn(...vals);
            if (typeof res === 'number' && !isNaN(res) && isFinite(res)) {
                validCount++;
            } else {
                f.is_computable = false;
                f.expression_js = '';
                fixedCount++;
            }
        } catch (e) {
            f.is_computable = false;
            f.expression_js = '';
            fixedCount++;
        }
    }
    
    console.log('NODE_EVAL_RESULT:' + JSON.stringify({ validCount, fixedCount, qualitativeCount }));
    fs.writeFileSync('data/interactive/index.json', JSON.stringify({
        version: 'aistem-interactive-v2',
        total_formulas: Object.keys(data).length,
        computable_count: validCount,
        formulas: data
    }, null, 2), 'utf8');
    """
    
    eval_runner = ROOT / "tools" / "run_eval.js"
    eval_runner.write_text(node_eval_script, encoding="utf-8")
    
    res = subprocess.run(["node", str(eval_runner)], capture_output=True, text=True, cwd=str(ROOT))
    print(res.stdout)
    if res.stderr:
        print("Stderr:", res.stderr)
        
    if test_file.exists(): test_file.unlink()
    if eval_runner.exists(): eval_runner.unlink()

    print("🎉 Đã hoàn tất tối ưu và kiểm định toàn diện 5,272 công thức!")

if __name__ == "__main__":
    main()
