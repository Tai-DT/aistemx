import json
import re
from pathlib import Path

def extract_balanced_braces(s: str, start_idx: int):
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

def clean_latex(s: str) -> str:
    s = s.strip()
    # Loại bỏ môi trường LaTeX
    s = re.sub(r'\\begin\{[^{}]*\}', '', s)
    s = re.sub(r'\\end\{[^{}]*\}', '', s)
    # Lấy phương trình đầu nếu có nhiều phương trình ngăn cách bởi ; hoặc \\
    if ';' in s:
        s = s.split(';')[0].strip()
    if '\\\\' in s:
        s = s.split('\\\\')[0].strip()
    if r'\implies' in s:
        # Nếu có \implies, vế sau thường là công thức suy ra
        parts = s.split(r'\implies')
        s = parts[-1].strip() if '=' in parts[-1] else parts[0].strip()
    if r'\iff' in s:
        s = s.split(r'\iff')[0].strip()

    # Bỏ text, format
    s = re.sub(r'\\left\.|\\right\.', '', s)
    s = re.sub(r'\\left|\\right', '', s)
    s = re.sub(r'\\text\{[^{}]*\}', '', s)
    s = re.sub(r'\\mathrm\{[^{}]*\}', '', s)
    s = re.sub(r'\\mathbf\{[^{}]*\}', '', s)
    s = re.sub(r'\\mathit\{[^{}]*\}', '', s)
    s = re.sub(r'\\displaystyle', '', s)
    s = re.sub(r'\\qquad|\\quad|\\;|\\,|\\!|\\:', ' ', s)
    s = re.sub(r'\\\s*\(?\)?', '', s)
    s = re.sub(r'\\cdot|\\times', ' * ', s)
    s = re.sub(r'\\pm|\\mp', ' + ', s)
    return s.strip()

def replace_fractions(s: str) -> str:
    # 1. \frac{a}{b} hoặc \dfrac{a}{b} với ngoặc nhọn
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
    
    # 2. \frac 1 2 hoặc \frac12 (không ngoặc)
    s = re.sub(r'\\(d|t)?frac\s*([0-9a-zA-Z])\s*([0-9a-zA-Z])', r'((\2) / (\3))', s)
    return s

def replace_roots(s: str) -> str:
    # \sqrt[n]{x}
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

    # \sqrt{x}
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

    # Base^{exp} với balanced braces
    while True:
        m = re.search(r'([a-zA-Z0-9_\(\)]+)\s*\^\s*\{', s)
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

    # Base^single
    s = re.sub(r'([a-zA-Z0-9_\(\)]+)\s*\^\s*([a-zA-Z0-9_])', r'Math.pow(\1, \2)', s)
    return s

def replace_subscripts(s: str) -> str:
    # x_{1} -> x_1
    while True:
        m = re.search(r'_\{([^{}]+)\}', s)
        if not m:
            break
        sub_name = re.sub(r'[^a-zA-Z0-9_]', '_', m.group(1))
        s = s[:m.start()] + f'_{sub_name}' + s[m.end():]
    return s

def replace_abs(s: str) -> str:
    # |x| -> Math.abs(x)
    s = re.sub(r'\|([^\|]+)\|', r'Math.abs(\1)', s)
    return s

print('Loaded test module successfully')
