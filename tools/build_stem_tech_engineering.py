#!/usr/bin/env python3
"""Sinh hai tập dữ liệu bài tập STEM & Công nghệ Kỹ thuật mở rộng:
1. data/problems/stem-technology-engineering.json (30 bài toán Technology & Engineering)
2. data/problems/intl-olympiad-advanced-sciences.json (30 bài toán Olympic Khoa học Nâng cao)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "data" / "problems"

# -------------------------------------------------------------
# 1. STEM Technology & Engineering Dataset (30 problems)
# -------------------------------------------------------------
tech_eng_problems = []

# Part A: Boolean Algebra & Logic Gates (10 problems)
for i in range(1, 11):
    pid = f"prob.math.boolean-logic.{i:04d}"
    n_vars = 2 + (i % 4)
    total_funcs = 2**(2**n_vars)
    stmt_vi = f"Trong thiết kế mạch số và đại số Boole, có tất cả bao nhiêu hàm Boole phân biệt của {n_vars} biến nhị phân f: {{0, 1}}^{n_vars} -> {{0, 1}}?"
    stmt_en = f"In digital circuit design and Boolean algebra, how many distinct Boolean functions of {n_vars} binary variables f: {{0, 1}}^{n_vars} -> {{0, 1}} are there?"
    steps = [
        {"explain": f"Bảng chân trị của một hàm Boole {n_vars} biến có đúng 2^{n_vars} hàng (tổ hợp đầu vào).", "latex": f"N_{{\\text{{hàng}}}} = 2^{{{n_vars}}} = {2**n_vars}"},
        {"explain": f"Mỗi hàng của bảng chân trị có thể nhận 1 trong 2 giá trị đầu ra (0 hoặc 1). Do đó tổng số hàm Boole phân biệt là 2^(2^{n_vars}) = 2^{{{2**n_vars}}}.", "latex": f"|\\mathcal{{F}}| = 2^{{2^{{{n_vars}}}}} = 2^{{{2**n_vars}}} = {total_funcs}"}
    ]
    tech_eng_problems.append({
        "id": pid,
        "subject": "math",
        "level": "dai-hoc",
        "grades": [13],
        "curriculum": ["intl-undergrad"],
        "topic": f"Công nghệ & Mạch số: Đại số Boole và Hàm logic - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(total_funcs),
        "answer_numeric": total_funcs,
        "answer_unit": "hàm",
        "tolerance": 0.001,
        "solution_steps": steps,
        "formulas_used": ["math.dai-hoc.dai-so-boole.so-ham-boole"],
        "difficulty": 3,
        "estimated_minutes": 6,
        "skills": ["đại số Boole", "thiết kế mạch số", "bảng chân trị logic"],
        "hints": ["Tính số hàng của bảng chân trị.", "Mỗi hàng có 2 cách chọn giá trị đầu ra."],
        "tags": ["boolean-algebra", "digital-logic", "technology", "computer-science"]
    })

# Part B: Electrical Engineering & Circuits (10 problems)
for i in range(1, 11):
    pid = f"prob.physics.ee-circuits.{i:04d}"
    E = 12.0 + i * 2.0  # V
    r = 1.0 + (i % 3) * 0.5 # Ohm
    R_ext = 4.0 + i * 1.5 # Ohm
    I_current = round(E / (R_ext + r), 2)
    stmt_vi = f"Một nguồn điện có suất điện động E = {E} V và điện trở trong r = {r} Ω được mắc với một mạch ngoài có điện trở R = {R_ext} Ω thành mạch kín. Tính cường độ dòng điện chạy trong mạch theo đơn vị Ampe (làm tròn 2 chữ số thập phân)."
    stmt_en = f"A power source with EMF E = {E} V and internal resistance r = {r} Ω is connected to an external resistor R = {R_ext} Ω in a closed loop. Find the electric current in the circuit in Amperes (rounded to 2 decimal places)."
    steps = [
        {"explain": "Áp dụng định luật Ohm cho toàn mạch: I = E / (R + r).", "latex": "I = \\frac{\\mathcal{E}}{R + r}"},
        {"explain": f"Thay số với E = {E} V, R = {R_ext} Ω, r = {r} Ω: I = {E} / ({R_ext} + {r}) = {I_current} A.", "latex": f"I = \\frac{{{E}}}{{{R_ext} + {r}}} = {I_current} \\text{{ A}}"}
    ]
    tech_eng_problems.append({
        "id": pid,
        "subject": "physics",
        "level": "thpt",
        "grades": [11, 12],
        "curriculum": ["vn-gdpt-2018"],
        "topic": f"Kỹ thuật Điện: Định luật Ohm cho toàn mạch - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(I_current),
        "answer_numeric": I_current,
        "answer_unit": "A",
        "tolerance": 0.05,
        "solution_steps": steps,
        "formulas_used": ["physics.thpt.dong-dien-khong-doi.dinh-luat-om-toan-mach"],
        "difficulty": 2,
        "estimated_minutes": 5,
        "skills": ["định luật Ohm toàn mạch", "kỹ thuật mạch điện DC", "tính toán dòng điện"],
        "hints": ["Dùng công thức I = E / (R_ngoài + r_trong).", "Cộng điện trở trong với điện trở ngoài."],
        "tags": ["electrical-engineering", "circuits", "ohm-law", "physics"]
    })

# Part C: Algorithms & Information Theory (10 problems)
for i in range(1, 11):
    pid = f"prob.math.algorithms.{i:04d}"
    n_nodes = 5 + i * 2
    tree_edges = n_nodes - 1
    stmt_vi = f"Trong khoa học máy tính, một cây khung nhỏ nhất (Minimum Spanning Tree) của một đồ thị liên thông gồm {n_nodes} đỉnh có đúng bao nhiêu cạnh?"
    stmt_en = f"In computer science, how many edges does a Minimum Spanning Tree of a connected graph with {n_nodes} vertices have?"
    steps = [
        {"explain": f"Theo định nghĩa cấu trúc dữ liệu Cây (Tree), một cây gồm n đỉnh liên thông và không có chu trình luôn luôn có đúng (n - 1) cạnh.", "latex": "|E| = |V| - 1"},
        {"explain": f"Thay |V| = {n_nodes}: |E| = {n_nodes} - 1 = {tree_edges} cạnh.", "latex": f"|E| = {n_nodes} - 1 = {tree_edges}"}
    ]
    tech_eng_problems.append({
        "id": pid,
        "subject": "math",
        "level": "dai-hoc",
        "grades": [13],
        "curriculum": ["intl-undergrad"],
        "topic": f"Khoa học Máy tính: Cấu trúc Cây và Thuật toán Đồ thị - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(tree_edges),
        "answer_numeric": tree_edges,
        "answer_unit": "cạnh",
        "tolerance": 0.001,
        "solution_steps": steps,
        "formulas_used": ["math.thpt.to-hop-xac-suat.quy-tac-cong"],
        "difficulty": 2,
        "estimated_minutes": 5,
        "skills": ["thuật toán cây khung MST", "cấu trúc dữ liệu cây", "lý thuyết đồ thị máy tính"],
        "hints": ["Một cây liên thông n đỉnh có bao nhiêu cạnh?", "Số cạnh của cây luôn bằng n - 1."],
        "tags": ["computer-science", "spanning-tree", "algorithms", "data-structures"]
    })

(PROBLEMS_DIR / "stem-technology-engineering.json").write_text(json.dumps({
    "meta": {
        "file": "stem-technology-engineering.json",
        "subject": "math",
        "title": "Tuyển tập Bài toán Công nghệ, Kỹ thuật Điện & Khoa học Máy tính STEM",
        "levels": ["thpt", "dai-hoc"],
        "count": len(tech_eng_problems)
    },
    "problems": tech_eng_problems
}, ensure_ascii=False, indent=2), encoding="utf-8")

# -------------------------------------------------------------
# 2. International Advanced Science Olympiad Dataset (30 problems)
# -------------------------------------------------------------
adv_sci_problems = []

# Physics Advanced (10 problems)
for i in range(1, 11):
    pid = f"prob.physics.adv-olympiad.{i:04d}"
    k_spring = 50.0 + i * 10.0 # N/m
    m_mass = 0.2 + i * 0.05 # kg
    omega = round((k_spring / m_mass)**0.5, 2)
    stmt_vi = f"Một con lắc lò xo gồm vật nặng khối lượng m = {m_mass} kg và lò xo có độ cứng k = {k_spring} N/m dao động điều hòa tự do. Tính tần số góc ω của dao động theo đơn vị rad/s (làm tròn 2 chữ số thập phân)."
    stmt_en = f"A spring-mass system with mass m = {m_mass} kg and spring constant k = {k_spring} N/m undergoes simple harmonic motion. Find the angular frequency ω in rad/s (rounded to 2 decimal places)."
    steps = [
        {"explain": "Tần số góc của con lắc lò xo dao động điều hòa: ω = sqrt(k / m).", "latex": "\\omega = \\sqrt{\\frac{k}{m}}"},
        {"explain": f"Thay k = {k_spring} N/m và m = {m_mass} kg: ω = sqrt({k_spring} / {m_mass}) = {omega} rad/s.", "latex": f"\\omega = \\sqrt{{\\frac{{{k_spring}}}{{{m_mass}}}}} = {omega} \\text{{ rad/s}}"}
    ]
    adv_sci_problems.append({
        "id": pid,
        "subject": "physics",
        "level": "thpt",
        "grades": [11, 12],
        "curriculum": ["olympiad"],
        "topic": f"IPhO Dao động cơ học: Con lắc lò xo và Tần số góc - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(omega),
        "answer_numeric": omega,
        "answer_unit": "rad/s",
        "tolerance": 0.05,
        "solution_steps": steps,
        "formulas_used": ["physics.thpt.dao-dong-dieu-hoa.con-lac-lo-xo-chu-ki"],
        "difficulty": 2,
        "estimated_minutes": 5,
        "skills": ["tính tần số góc dao động điều hòa", "con lắc lò xo", "cơ học dao động IPhO"],
        "hints": ["Sử dụng công thức ω = √(k/m).", "Kiểm tra đơn vị m là kg và k là N/m."],
        "tags": ["ipho", "harmonic-oscillator", "mechanics", "physics"]
    })

# Chemistry Advanced (10 problems)
for i in range(1, 11):
    pid = f"prob.chemistry.adv-olympiad.{i:04d}"
    pH = round(3.0 + i * 0.4, 2)
    H_conc = round(10**(-pH) * 1e6, 2) # in micromol/L
    stmt_vi = f"Một dung dịch đệm hóa học ở 25°C có giá trị pH = {pH}. Nồng độ ion H+ trong dung dịch bằng bao nhiêu μmol/L (micromol/lít, làm tròn 2 chữ số thập phân)?"
    stmt_en = f"A chemical buffer solution at 25°C has pH = {pH}. What is the H+ ion concentration in μmol/L (micromoles per liter, rounded to 2 decimal places)?"
    steps = [
        {"explain": "Định nghĩa chỉ số pH: pH = -log10[H+] => [H+] = 10^(-pH) mol/L.", "latex": "[H^+] = 10^{-\\text{pH}}"},
        {"explain": f"Tính nồng độ theo mol/L: [H+] = 10^(-{pH}) mol/L.", "latex": f"[H^+] = 10^{{-{pH}}} \\text{{ mol/L}}"},
        {"explain": f"Đổi sang đơn vị μmol/L (nhân với 10^6): [H+] = 10^(-{pH}) * 10^6 = {H_conc} μmol/L.", "latex": f"[H^+] = {H_conc} \\; \\mu\\text{{mol/L}}"}
    ]
    adv_sci_problems.append({
        "id": pid,
        "subject": "chemistry",
        "level": "thpt",
        "grades": [11, 12],
        "curriculum": ["olympiad"],
        "topic": f"IChO Cân bằng Axit - Bazơ: Nồng độ ion H+ và pH - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(H_conc),
        "answer_numeric": H_conc,
        "answer_unit": "μmol/L",
        "tolerance": 0.05,
        "solution_steps": steps,
        "formulas_used": ["chemistry.thpt.dung-dich.ph-dung-dich"],
        "difficulty": 2,
        "estimated_minutes": 5,
        "skills": ["tính nồng độ ion H+ từ pH", "chuyển đổi đơn vị vi lượng micromol", "cân bằng axit bazơ"],
        "hints": ["[H+] = 10^(-pH) (mol/L).", "1 mol/L = 10^6 μmol/L."],
        "tags": ["icho", "acid-base", "ph-calculation", "chemistry"]
    })

# Biology Advanced (10 problems)
for i in range(1, 11):
    pid = f"prob.biology.adv-olympiad.{i:04d}"
    N_nucleotides = 1200 + i * 150
    length_A = round((N_nucleotides / 2) * 3.4, 1)
    stmt_vi = f"Một phân tử DNA mạch kép xoắn kép chuẩn B-DNA có tổng số {N_nucleotides} nucleotide. Biết chiều dài mỗi cặp base là 3.4 Å (Angstrom). Tính chiều dài của phân tử DNA này theo đơn vị Å (làm tròn 1 chữ số thập phân)."
    stmt_en = f"A double-stranded B-DNA molecule contains {N_nucleotides} nucleotides in total. Knowing that each base pair measures 3.4 Å, calculate the length of the DNA in Å (rounded to 1 decimal place)."
    steps = [
        {"explain": f"Số cặp nucleotide (base pairs) của DNA mạch kép: N_bp = N / 2 = {N_nucleotides} / 2 = {N_nucleotides // 2} bp.", "latex": f"N_{{\\text{{bp}}}} = \\frac{{{N_nucleotides}}}{{2}} = {N_nucleotides // 2}"},
        {"explain": f"Chiều dài của phân tử DNA: L = N_bp * 3.4 Å = {N_nucleotides // 2} * 3.4 = {length_A} Å.", "latex": f"L = {N_nucleotides // 2} \\times 3.4 = {length_A} \\text{{ \\AA}}"}
    ]
    adv_sci_problems.append({
        "id": pid,
        "subject": "biology",
        "level": "thpt",
        "grades": [10, 11, 12],
        "curriculum": ["olympiad"],
        "topic": f"IBO Di truyền học Phân tử: Cấu trúc không gian DNA B-form - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(length_A),
        "answer_numeric": length_A,
        "answer_unit": "Å",
        "tolerance": 0.1,
        "solution_steps": steps,
        "formulas_used": ["biology.dai-hoc.sinh-hoc-phan-tu.chieu-dai-va-so-chu-ki-xoan-adn"],
        "difficulty": 2,
        "estimated_minutes": 5,
        "skills": ["tính chiều dài phân tử DNA", "cấu trúc xoắn kép B-DNA", "di truyền học phân tử IBO"],
        "hints": ["DNA mạch kép gồm 2 mạch đơn, chia tổng số nu cho 2 để tìm số cặp.", "Mỗi cặp base dài 3.4 Å."],
        "tags": ["ibo", "molecular-biology", "dna-structure", "genetics"]
    })

(PROBLEMS_DIR / "intl-olympiad-advanced-sciences.json").write_text(json.dumps({
    "meta": {
        "file": "intl-olympiad-advanced-sciences.json",
        "subject": "physics",
        "title": "Tuyển tập Đề thi Olympic Khoa học Nâng cao IPhO, IChO, IBO",
        "levels": ["thpt", "dai-hoc"],
        "count": len(adv_sci_problems)
    },
    "problems": adv_sci_problems
}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Generated 60 additional problems successfully (30 tech/eng + 30 adv science).")
