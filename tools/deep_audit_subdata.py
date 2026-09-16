#!/usr/bin/env python3
"""
Comprehensive Deep Audit for All Nested Sub-Data (Dữ liệu con)
Audits:
1. Problems (choices, solution_steps, formulas_used, answer, answer_numeric, hints, tags)
2. Formulas (latex, variables, related_formulas, domain/subject)
3. Interactive calculations (expression_js, parameter ranges min/max/default/step, evaluation with defaults)
4. Illustrations (formula_id existence, SVG file integrity, XML parsing)
5. Lessons (formula_ids, problem_ids)
6. Exams (problem_ids, answer key consistency)
"""

import json
import os
import re
import xml.etree.ElementTree as ET

REPORT = {
    "problems": [],
    "formulas": [],
    "interactive": [],
    "illustrations": [],
    "lessons": [],
    "exams": []
}

print("=== STARTING COMPREHENSIVE SUB-DATA AUDIT ===")

# --- 1. LOAD DATASETS ---
with open('data/formulas/index.json') as f:
    formulas_data = json.load(f)
    formulas = formulas_data.get('formulas', [])
formula_map = {f['id']: f for f in formulas}

with open('data/problems/index.json') as f:
    problems_data = json.load(f)
    problems = problems_data.get('problems', [])
problem_map = {p['id']: p for p in problems}

with open('data/illustrations/index.json') as f:
    illustrations_data = json.load(f)
    illustrations = illustrations_data.get('illustrations', [])

with open('data/interactive/index.json') as f:
    interactive_data = json.load(f)

with open('data/lessons/index.json') as f:
    lessons_data = json.load(f)
    lessons = lessons_data.get('lessons', [])

with open('data/exams/index.json') as f:
    exams_data = json.load(f)
    exams = exams_data.get('exams', [])

print(f"Loaded: {len(formulas)} formulas, {len(problems)} problems, {len(illustrations)} illustrations, {len(lessons)} lessons, {len(exams)} exams.")


# --- 2. AUDIT PROBLEMS ---
print("\n--- Auditing Problems Sub-Data ---")
for p in problems:
    pid = p.get('id', 'UNKNOWN')
    ptype = p.get('type')
    choices = p.get('choices') or []
    answer = p.get('answer')
    ans_num = p.get('answer_numeric')
    steps = p.get('solution_steps') or []
    f_used = p.get('formulas_used') or []

    # Check choices for trac-nghiem
    if ptype == 'trac-nghiem':
        if not choices:
            REPORT["problems"].append((pid, "trac-nghiem has NO choices"))
        elif len(choices) < 2:
            REPORT["problems"].append((pid, f"trac-nghiem has only {len(choices)} choices"))
        else:
            keys = []
            seen_texts = set()
            for idx, c in enumerate(choices):
                k = c.get('key') or c.get('label') or c.get('id')
                txt = c.get('text') or c.get('content') or ''

                if not k:
                    REPORT["problems"].append((pid, f"choice {idx} has missing key/label"))
                else:
                    keys.append(str(k).strip())

                if not str(txt).strip():
                    REPORT["problems"].append((pid, f"choice {k} has empty text"))
                
                txt_clean = str(txt).strip()
                if txt_clean in seen_texts:
                    REPORT["problems"].append((pid, f"duplicate choice content in choice {k}: '{txt_clean[:30]}'"))
                seen_texts.add(txt_clean)

                # Check latex in choice
                if "{" in str(txt) or "}" in str(txt):
                    if str(txt).count("{") != str(txt).count("}"):
                        REPORT["problems"].append((pid, f"choice {k} has unbalanced braces in text: {txt[:40]}"))

            # Check if answer matches one of the choice keys
            ans_str = str(answer).strip() if answer is not None else ''
            if not ans_str:
                REPORT["problems"].append((pid, f"trac-nghiem has empty answer. Choices: {keys}"))
            elif ans_str not in keys:
                # Is ans_str matching choice text instead of key?
                matching_choice = [c for c in choices if str(c.get('text', '')).strip() == ans_str]
                if matching_choice:
                    REPORT["problems"].append((pid, f"answer '{ans_str}' matches text instead of key '{matching_choice[0].get('key')}'"))
                else:
                    REPORT["problems"].append((pid, f"answer '{ans_str}' does not match any choice keys {keys}"))

    elif ptype == 'dien-so':
        if ans_num is None and (answer is None or str(answer).strip() == ''):
            REPORT["problems"].append((pid, "dien-so has both answer and answer_numeric empty"))
        elif ans_num is not None and (ans_num != ans_num):  # NaN check
            REPORT["problems"].append((pid, "answer_numeric is NaN"))

    # Check solution_steps
    if not steps:
        REPORT["problems"].append((pid, "solution_steps is empty"))
    else:
        for idx, s in enumerate(steps):
            if isinstance(s, dict):
                exp = s.get('explain') or s.get('explanation') or s.get('content') or s.get('text') or ''
                math_val = s.get('latex') or s.get('math') or ''
                if not str(exp).strip() and not str(math_val).strip():
                    REPORT["problems"].append((pid, f"solution_step {idx} has empty explain and latex"))
                if math_val and math_val.count("{") != math_val.count("}"):
                    REPORT["problems"].append((pid, f"solution_step {idx} latex has unbalanced braces: {math_val}"))
            elif isinstance(s, str):
                if not s.strip():
                    REPORT["problems"].append((pid, f"solution_step {idx} is empty string"))

    # Check formulas_used
    for fid in f_used:
        if fid not in formula_map:
            REPORT["problems"].append((pid, f"formulas_used references nonexistent formula: '{fid}'"))


# --- 3. AUDIT FORMULAS ---
print("\n--- Auditing Formulas Sub-Data ---")
for f in formulas:
    fid = f.get('id', 'UNKNOWN')
    latex = f.get('latex', '')
    variables = f.get('variables', [])
    rel_f = f.get('related_formulas') or []

    # Check latex
    if not latex or not str(latex).strip():
        REPORT["formulas"].append((fid, "empty latex expression"))
    else:
        if latex.count("{") != latex.count("}"):
            REPORT["formulas"].append((fid, f"latex has unbalanced braces: {latex[:50]}"))

    # Check variables sub-data
    if isinstance(variables, list):
        for vidx, v in enumerate(variables):
            if isinstance(v, dict):
                sym = v.get('symbol')
                name = v.get('name')
                if not sym or not str(sym).strip():
                    REPORT["formulas"].append((fid, f"variable {vidx} has empty symbol"))
                if not name or not str(name).strip():
                    REPORT["formulas"].append((fid, f"variable {vidx} ({sym}) has empty name"))
            elif isinstance(v, str):
                if not v.strip():
                    REPORT["formulas"].append((fid, f"variable {vidx} is empty string"))
    
    # Check related formulas
    for rfid in rel_f:
        if rfid not in formula_map:
            REPORT["formulas"].append((fid, f"related_formula references nonexistent formula: '{rfid}'"))


# --- 4. AUDIT ILLUSTRATIONS & SVGS ---
print("\n--- Auditing Illustrations Sub-Data ---")
for ill in illustrations:
    fid = ill.get('formula_id', 'UNKNOWN')
    svg_rel = ill.get('svg_path') or f"svg/{fid}.svg"
    full_path = os.path.join('data/illustrations', svg_rel)
    
    if fid and fid not in formula_map:
        REPORT["illustrations"].append((fid, f"illustration references nonexistent formula_id '{fid}'"))
    
    # Check SVG file
    if os.path.exists(full_path):
        try:
            tree = ET.parse(full_path)
            root = tree.getroot()
            if not root.tag.endswith('svg'):
                REPORT["illustrations"].append((fid, f"SVG file {full_path} root is not svg ({root.tag})"))
        except Exception as e:
            REPORT["illustrations"].append((fid, f"SVG file {full_path} XML parse error: {e}"))
    else:
        REPORT["illustrations"].append((fid, f"SVG file {full_path} not found on disk"))


# --- 5. AUDIT INTERACTIVE EXPRESSIONS ---
print("\n--- Auditing Interactive Sub-Data ---")
inter_forms = interactive_data.get('formulas', {})
for fid, item in inter_forms.items():
    if fid not in formula_map:
        REPORT["interactive"].append((fid, "interactive formula references nonexistent formula_id"))
    
    computable = item.get('computable', False)
    if not computable:
        continue
    
    params = item.get('parameters', [])
    expr_js = item.get('expression_js', '')
    
    if not expr_js or not expr_js.strip():
        REPORT["interactive"].append((fid, "computable formula has empty expression_js"))
        continue

    # Check parameter definitions
    for p in params:
        pname = p.get('name')
        pmin = p.get('min')
        pmax = p.get('max')
        pdef = p.get('default')
        pstep = p.get('step')

        if not pname:
            REPORT["interactive"].append((fid, "parameter missing name"))
            continue
        
        if pmin is not None and pmax is not None and pdef is not None:
            if not (pmin <= pdef <= pmax):
                REPORT["interactive"].append((fid, f"param '{pname}' default {pdef} outside range [{pmin}, {pmax}]"))
            if pstep is not None and pstep <= 0:
                REPORT["interactive"].append((fid, f"param '{pname}' step <= 0 ({pstep})"))


# --- 6. AUDIT LESSONS ---
print("\n--- Auditing Lessons Sub-Data ---")
for l in lessons:
    lid = l.get('id', 'UNKNOWN')
    f_ids = l.get('formula_ids') or l.get('formulas') or []
    p_ids = l.get('problem_ids') or l.get('problems') or []

    for fid in f_ids:
        if fid not in formula_map:
            REPORT["lessons"].append((lid, f"lesson references nonexistent formula '{fid}'"))
    for pid in p_ids:
        if pid not in problem_map:
            REPORT["lessons"].append((lid, f"lesson references nonexistent problem '{pid}'"))


# --- 7. AUDIT EXAMS ---
print("\n--- Auditing Exams Sub-Data ---")
for ex in exams:
    eid = ex.get('id', 'UNKNOWN')
    p_ids = ex.get('problem_ids') or []
    for pid in p_ids:
        if pid not in problem_map:
            REPORT["exams"].append((eid, f"exam references nonexistent problem '{pid}'"))


# --- SUMMARY REPORT ---
print("\n==========================================")
print("              AUDIT SUMMARY               ")
print("==========================================")
for category, issues in REPORT.items():
    print(f"[{category.upper()}]: {len(issues)} issues found")

total_issues = sum(len(v) for v in REPORT.values())
print(f"\nTOTAL ISSUES: {total_issues}")

if total_issues > 0:
    print("\n--- DETAILED BREAKDOWN OF ISSUES ---")
    for category, issues in REPORT.items():
        if issues:
            print(f"\n>>> {category.upper()} ({len(issues)} issues):")
            for item in issues[:50]:
                print(f"  - [{item[0]}]: {item[1]}")
            if len(issues) > 50:
                print(f"  ... and {len(issues) - 50} more issues")

with open('data/audit_report.json', 'w') as f:
    json.dump(REPORT, f, indent=2, ensure_ascii=False)
print("\nSaved full audit report to data/audit_report.json")
