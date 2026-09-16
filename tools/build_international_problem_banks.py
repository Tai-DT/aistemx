#!/usr/bin/env python3
"""Sinh các tập dữ liệu bài tập Olympic Quốc tế & Khoa học Tự nhiên STEM:
- data/problems/intl-competitions-amc-aime.json (AMC 8, AMC 10, AMC 12, AIME)
- data/problems/intl-competitions-science-olympiad.json (IPhO, IChO, IBO, USAPhO, USNCO, USABO)
- data/problems/intl-competitions-kangaroo-sasmo.json (Kangaroo IKMC, SASMO, Bebras)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "data" / "problems"

# -------------------------------------------------------------
# 1. AMC & AIME Dataset (30 problems)
# -------------------------------------------------------------
amc_aime_problems = []

# Generate structured problems for AMC 8/10/12 and AIME
for i in range(1, 31):
    pid = f"prob.math.amc-aime.{i:04d}"
    if i <= 10:
        # AMC 8 / 10 Algebra & Number theory
        topic = f"AMC 10: Đại số & Số học chuyên sâu - Chủ đề {i}"
        stmt_vi = f"Cho số nguyên dương n thỏa mãn phương trình n^2 + {2*i}n = {i*100 + 44}. Tìm giá trị của n."
        stmt_en = f"Find the positive integer n satisfying n^2 + {2*i}n = {i*100 + 44}."
        # n^2 + 2*i*n - (100i+44) = 0 -> delta' = i^2 + 100i + 44 = (i + 50)^2 - 2500 + 44
        # Let's create an exact integer root problem:
        root = 10 + i
        c_val = root**2 + 2*i*root
        stmt_vi = f"Tìm số nguyên dương n thỏa mãn phương trình n^2 + {2*i}n = {c_val}."
        stmt_en = f"Find the positive integer n satisfying n^2 + {2*i}n = {c_val}."
        ans = str(root)
        steps = [
            {"explain": "Chuyển vế phương trình bậc hai về dạng chuẩn: n^2 + 2in - C = 0.", "latex": f"n^2 + {2*i}n - {c_val} = 0"},
            {"explain": f"Tính biệt thức delta': delta' = i^2 + {c_val} = {(root+i)**2}.", "latex": f"\\Delta' = {i}^2 + {c_val} = {(root+i)**2}"},
            {"explain": f"Suy ra nghiệm dương: n = -{i} + {root+i} = {root}.", "latex": f"n = -{i} + {root+i} = {root}"}
        ]
        amc_aime_problems.append({
            "id": pid,
            "subject": "math",
            "level": "thpt",
            "grades": [9, 10, 11],
            "curriculum": ["olympiad"],
            "topic": topic,
            "type": "dien-so",
            "statement_vi": stmt_vi,
            "statement_en": stmt_en,
            "answer": ans,
            "answer_numeric": root,
            "answer_unit": "",
            "tolerance": 0.001,
            "solution_steps": steps,
            "formulas_used": ["math.thpt.to-hop-xac-suat.quy-tac-cong"],
            "difficulty": 2 if i <= 5 else 3,
            "estimated_minutes": 6 + i % 4,
            "skills": ["giải phương trình bậc hai", "đại số AMC 10", "tính toán số học"],
            "hints": ["Đưa phương trình về dạng bình phương hoàn chỉnh (n + i)^2.", "Khai căn để tìm nghiệm nguyên dương."],
            "tags": ["amc-10", "algebra", "olympiad"]
        })
    elif i <= 20:
        # AMC 12 Combinatorics & Geometry
        k = i - 10
        topic = f"AMC 12: Tổ hợp & Xác suất rời rạc - Dạng {k}"
        total_items = 10 + k
        choose_k = 3
        from math import comb
        ans_num = comb(total_items, choose_k)
        stmt_vi = f"Có bao nhiêu cách chọn ra 3 học sinh từ một đội tuyển gồm {total_items} học sinh để tham gia ban đại diện?"
        stmt_en = f"In how many ways can 3 students be chosen from a team of {total_items} students to form a representative committee?"
        steps = [
            {"explain": f"Số cách chọn 3 phần tử không phân biệt thứ tự từ {total_items} phần tử là tổ hợp chập 3 của {total_items}.", "latex": f"C_{{{total_items}}}^3 = \\binom{{{total_items}}}{3}"},
            {"explain": f"Áp dụng công thức tính tổ hợp: C({total_items}, 3) = ({total_items} * {total_items-1} * {total_items-2}) / 6.", "latex": f"\\binom{{{total_items}}}{3} = \\frac{{{total_items} \\times {total_items-1} \\times {total_items-2}}}{{6}} = {ans_num}"}
        ]
        amc_aime_problems.append({
            "id": pid,
            "subject": "math",
            "level": "thpt",
            "grades": [10, 11, 12],
            "curriculum": ["olympiad"],
            "topic": topic,
            "type": "dien-so",
            "statement_vi": stmt_vi,
            "statement_en": stmt_en,
            "answer": str(ans_num),
            "answer_numeric": ans_num,
            "answer_unit": "cách",
            "tolerance": 0.001,
            "solution_steps": steps,
            "formulas_used": ["math.thpt.to-hop-xac-suat.to-hop-chap-k"],
            "difficulty": 3,
            "estimated_minutes": 8,
            "skills": ["tổ hợp chập k", "quy tắc đếm", "xác suất rời rạc"],
            "hints": ["Sử dụng công thức tổ hợp C(n, k).", "Không phân biệt thứ tự giữa các người được chọn."],
            "tags": ["amc-12", "combinatorics", "counting", "olympiad"]
        })
    else:
        # AIME 3-digit integer problems (000-999)
        m = i - 20
        ans_aime = 100 + m * 23
        topic = f"AIME: Bài toán điền số nguyên 3 chữ số - Đề mục {m}"
        stmt_vi = f"Trong một dãy số cấp số cộng hữu hạn có số hạng đầu là {m*3} và công sai là {m+2}. Tìm số hạng thứ {20 + m} của dãy."
        stmt_en = f"In an arithmetic progression with first term {m*3} and common difference {m+2}, find the {20 + m}-th term."
        n_term = 20 + m
        ans_val = (m*3) + (n_term - 1) * (m+2)
        steps = [
            {"explain": f"Công thức số hạng tổng quát của cấp số cộng: u_n = u_1 + (n - 1)d.", "latex": f"u_{{{n_term}}} = u_1 + ({n_term} - 1)d"},
            {"explain": f"Thay số với u_1 = {m*3}, d = {m+2}, n = {n_term}: u_{{{n_term}}} = {m*3} + {n_term-1} \\times {m+2} = {ans_val}.", "latex": f"u_{{{n_term}}} = {m*3} + {n_term-1} \\times {m+2} = {ans_val}"}
        ]
        amc_aime_problems.append({
            "id": pid,
            "subject": "math",
            "level": "thpt",
            "grades": [11, 12],
            "curriculum": ["olympiad"],
            "topic": topic,
            "type": "dien-so",
            "statement_vi": stmt_vi,
            "statement_en": stmt_en,
            "answer": f"{ans_val:03d}",
            "answer_numeric": ans_val,
            "answer_unit": "",
            "tolerance": 0.001,
            "solution_steps": steps,
            "formulas_used": ["math.thpt.to-hop-xac-suat.quy-tac-cong"],
            "difficulty": 4,
            "estimated_minutes": 12,
            "skills": ["cấp số cộng", "AIME integer calculation", "dãy số nguyên"],
            "hints": ["Sử dụng công thức u_n = u_1 + (n-1)d.", "Tính cẩn thận tích (n-1)*d."],
            "tags": ["aime", "arithmetic-progression", "sequences", "olympiad"]
        })

# Write AMC/AIME slice
(PROBLEMS_DIR / "intl-competitions-amc-aime.json").write_text(json.dumps({
    "meta": {
        "file": "intl-competitions-amc-aime.json",
        "subject": "math",
        "title": "Tuyển tập Bài toán Đề thi Quốc tế AMC 8, AMC 10, AMC 12 và AIME",
        "levels": ["thcs", "thpt"],
        "count": len(amc_aime_problems)
    },
    "problems": amc_aime_problems
}, ensure_ascii=False, indent=2), encoding="utf-8")

# -------------------------------------------------------------
# 2. Science Olympiad Dataset (IPhO, IChO, IBO - 30 problems)
# -------------------------------------------------------------
sci_olympiad_problems = []

# Physics IPhO / USAPhO (10 problems)
for i in range(1, 11):
    pid = f"prob.physics.ipho-usapho.{i:04d}"
    v0 = 10 + i * 2
    angle = 30
    h_max = (v0**2 * 0.25) / (2 * 9.8)
    stmt_vi = f"Một vật được ném từ mặt đất với vận tốc ban đầu v₀ = {v0} m/s hợp với phương ngang một góc 30°. Bỏ qua sức cản không khí, lấy g = 9.8 m/s². Tính độ cao cực đại mà vật đạt được theo đơn vị mét (làm tròn 2 chữ số thập phân)."
    stmt_en = f"A projectile is launched from ground with initial velocity v₀ = {v0} m/s at an angle of 30° above horizontal. Taking g = 9.8 m/s² and ignoring air resistance, find the maximum height in meters (rounded to 2 decimal places)."
    ans_num = round(h_max, 2)
    sci_olympiad_problems.append({
        "id": pid,
        "subject": "physics",
        "level": "thpt",
        "grades": [10, 11, 12],
        "curriculum": ["olympiad"],
        "topic": f"IPhO Cơ học: Chuyển động ném xiên trong trường trọng lực - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(ans_num),
        "answer_numeric": ans_num,
        "answer_unit": "m",
        "tolerance": 0.05,
        "solution_steps": [
            {"explain": "Phân tích thành phần vận tốc theo phương thẳng đứng: v_{0y} = v_0 \\sin 30°.", "latex": f"v_{{0y}} = {v0} \\times 0.5 = {v0/2} \\text{{ m/s}}"},
            {"explain": "Độ cao cực đại đạt được khi vận tốc theo phương y triệt tiêu (v_y = 0): H = v_{0y}^2 / (2g).", "latex": f"H = \\frac{{{v0/2}^2}}{{2 \\times 9.8}} = \\frac{{{((v0/2)**2)}}}{{19.6}} \\approx {ans_num} \\text{{ m}}"}
        ],
        "formulas_used": ["physics.thpt.intl-dong-hoc.nem-xien-tach-thanh-phan"],
        "difficulty": 3,
        "estimated_minutes": 8,
        "skills": ["phân tích chuyển động ném xiên", "định luật bảo toàn cơ năng", "động học 2D"],
        "hints": ["Tính thành phần vận tốc ban đầu theo phương thẳng đứng.", "Dùng hệ thức độc lập v_y^2 - v_{0y}^2 = -2gH."],
        "tags": ["ipho", "usapho", "mechanics", "projectile-motion"]
    })

# Chemistry IChO / USNCO (10 problems)
for i in range(1, 11):
    pid = f"prob.chemistry.icho-usnco.{i:04d}"
    T = 298.15
    R_gas = 8.314
    delta_H = -50.0 - i * 5.0 # kJ/mol
    delta_S = -100.0 - i * 2.0 # J/(mol K)
    delta_G = delta_H - T * (delta_S / 1000.0)
    ans_num = round(delta_G, 2)
    stmt_vi = f"Một phản ứng hóa học ở 298.15 K có biến thiên enthalpy standard ΔH° = {delta_H} kJ/mol và biến thiên entropy standard ΔS° = {delta_S} J/(mol·K). Tính biến thiên năng lượng tự do Gibbs ΔG° của phản ứng theo kJ/mol (làm tròn 2 chữ số)."
    stmt_en = f"A chemical reaction at 298.15 K has standard enthalpy change ΔH° = {delta_H} kJ/mol and standard entropy change ΔS° = {delta_S} J/(mol·K). Calculate the standard Gibbs free energy change ΔG° in kJ/mol (rounded to 2 decimal places)."
    sci_olympiad_problems.append({
        "id": pid,
        "subject": "chemistry",
        "level": "thpt",
        "grades": [11, 12],
        "curriculum": ["olympiad"],
        "topic": f"IChO Nhiệt động hóa học: Phương trình Gibbs - Helmholtz - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(ans_num),
        "answer_numeric": ans_num,
        "answer_unit": "kJ/mol",
        "tolerance": 0.1,
        "solution_steps": [
            {"explain": "Đổi đơn vị entropy ΔS° từ J/(mol·K) sang kJ/(mol·K): chia cho 1000.", "latex": f"\\Delta S^\\circ = \\frac{{{delta_S}}}{{1000}} = {delta_S/1000} \\text{{ kJ/(mol\\cdot K)}}"},
            {"explain": "Áp dụng phương trình Gibbs: ΔG° = ΔH° - T·ΔS°.", "latex": f"\\Delta G^\\circ = {delta_H} - 298.15 \\times ({delta_S/1000}) = {ans_num} \\text{{ kJ/mol}}"}
        ],
        "formulas_used": ["chemistry.thpt.nhiet-hoa.nang-luong-tu-do-gibbs"],
        "difficulty": 3,
        "estimated_minutes": 8,
        "skills": ["phương trình Gibbs-Helmholtz", "chiều hướng tự diễn biến của phản ứng", "nhiệt động học hóa học"],
        "hints": ["Đổi đơn vị ΔS° sang kJ/(mol·K) trước khi nhân với T.", "Áp dụng ΔG = ΔH - TΔS."],
        "tags": ["icho", "usnco", "thermodynamics", "gibbs-energy"]
    })

# Biology IBO / USABO (10 problems)
for i in range(1, 11):
    pid = f"prob.biology.ibo-usabo.{i:04d}"
    p_allele = round(0.1 * i, 2)
    q_allele = round(1.0 - p_allele, 2)
    hetero_freq = round(2 * p_allele * q_allele * 100, 2)
    stmt_vi = f"Trong một quần thể giao phối ngẫu nhiên ở trạng thái cân bằng di truyền Hardy-Weinberg, tần số allele trội A là p = {p_allele} và tần số allele lặn a là q = {q_allele}. Tỉ lệ phần trăm cá thể có kiểu gen dị hợp tử Aa trong quần thể là bao nhiêu %?"
    stmt_en = f"In a randomly mating population in Hardy-Weinberg equilibrium, the frequency of dominant allele A is p = {p_allele} and recessive allele a is q = {q_allele}. What is the percentage of heterozygous Aa individuals in the population?"
    sci_olympiad_problems.append({
        "id": pid,
        "subject": "biology",
        "level": "thpt",
        "grades": [11, 12],
        "curriculum": ["olympiad"],
        "topic": f"IBO Di truyền học quần thể: Định luật Hardy - Weinberg - Bài {i}",
        "type": "dien-so",
        "statement_vi": stmt_vi,
        "statement_en": stmt_en,
        "answer": str(hetero_freq),
        "answer_numeric": hetero_freq,
        "answer_unit": "%",
        "tolerance": 0.05,
        "solution_steps": [
            {"explain": "Định luật Hardy-Weinberg phát biểu rằng cấu trúc di truyền của quần thể cân bằng có dạng: p² AA + 2pq Aa + q² aa = 1.", "latex": "p^2 + 2pq + q^2 = 1"},
            {"explain": f"Tần số kiểu gen dị hợp tử 2pq: 2 * {p_allele} * {q_allele} = {round(2*p_allele*q_allele, 4)}.", "latex": f"2pq = 2 \\times {p_allele} \\times {q_allele} = {round(2*p_allele*q_allele, 4)}"},
            {"explain": f"Đổi sang tỉ lệ phần trăm: {hetero_freq} %.", "latex": f"\\text{{Tỉ lệ}} = {hetero_freq}\\%"}
        ],
        "formulas_used": ["biology.thpt.di-truyen-quan-the.dinh-luat-hardy-weinberg"],
        "difficulty": 2,
        "estimated_minutes": 6,
        "skills": ["tính tần số kiểu gen quần thể", "định luật Hardy-Weinberg", "di truyền học số lượng"],
        "hints": ["Tần số cá thể dị hợp tử được tính bằng 2pq.", "Nhân với 100 để đưa về phần trăm."],
        "tags": ["ibo", "usabo", "hardy-weinberg", "population-genetics"]
    })

# Write Science Olympiad slice
(PROBLEMS_DIR / "intl-competitions-science-olympiad.json").write_text(json.dumps({
    "meta": {
        "file": "intl-competitions-science-olympiad.json",
        "subject": "physics",
        "title": "Tuyển tập Đề thi Olympic Khoa học Tự nhiên IPhO, IChO, IBO",
        "levels": ["thpt", "dai-hoc"],
        "count": len(sci_olympiad_problems)
    },
    "problems": sci_olympiad_problems
}, ensure_ascii=False, indent=2), encoding="utf-8")

# -------------------------------------------------------------
# 3. Kangaroo, SASMO & Bebras Dataset (30 problems)
# -------------------------------------------------------------
kangaroo_sasmo_problems = []

for i in range(1, 31):
    pid = f"prob.math.kangaroo-sasmo.{i:04d}"
    if i <= 10:
        # Kangaroo spatial and logic
        n_sides = 3 + i
        sum_angles = (n_sides - 2) * 180
        stmt_vi = f"Tổng số đo các góc trong của một đa giác lồi có {n_sides} cạnh bằng bao nhiêu độ?"
        stmt_en = f"What is the sum of interior angles of a convex polygon with {n_sides} sides in degrees?"
        steps = [
            {"explain": f"Công thức tổng các góc trong của một đa giác lồi n cạnh là S = (n - 2) * 180°.", "latex": f"S = (n - 2) \\times 180^\\circ"},
            {"explain": f"Thay n = {n_sides}: S = ({n_sides} - 2) * 180° = {sum_angles}°.", "latex": f"S = ({n_sides} - 2) \\times 180^\\circ = {sum_angles}^\\circ"}
        ]
        kangaroo_sasmo_problems.append({
            "id": pid,
            "subject": "math",
            "level": "thcs",
            "grades": [6, 7, 8],
            "curriculum": ["olympiad"],
            "topic": f"Kangaroo Math: Hình học phẳng & Đa giác lồi - Bài {i}",
            "type": "dien-so",
            "statement_vi": stmt_vi,
            "statement_en": stmt_en,
            "answer": str(sum_angles),
            "answer_numeric": sum_angles,
            "answer_unit": "độ",
            "tolerance": 0.001,
            "solution_steps": steps,
            "formulas_used": ["math.thpt.to-hop-xac-suat.quy-tac-cong"],
            "difficulty": 1 if i <= 5 else 2,
            "estimated_minutes": 5,
            "skills": ["tính tổng góc đa giác lồi", "hình học Kangaroo", "tư duy trực quan"],
            "hints": ["Mỗi đa giác n cạnh có thể chia thành (n - 2) tam giác.", "Tổng các góc trong tam giác là 180 độ."],
            "tags": ["kangaroo", "ikmc", "polygon-angles", "geometry"]
        })
    elif i <= 20:
        # SASMO cryptarithm and logic grids
        k = i - 10
        base_sum = 100 * k + 45
        stmt_vi = f"Tìm chữ số A trong phép nhân A × 9 = {k}A{k+1} (nếu tích có dạng biểu thức 3 chữ số)."
        # Let's create a solid arithmetic logic question:
        # Find sum of digits of a large number pattern
        sum_digits = 9 * k
        stmt_vi = f"Cho số A = 999...9 (gồm {k*2} chữ số 9). Tính tổng các chữ số của số B = A^2."
        stmt_en = f"Let A = 999...9 (having {k*2} nines). Find the sum of the digits of B = A^2."
        ans_num = 9 * (k * 2)
        steps = [
            {"explain": f"Nhận xét quy luật: 9^2 = 81 (tổng 9), 99^2 = 9801 (tổng 18), 999^2 = 998001 (tổng 27). Số A gồm m chữ số 9 khi bình phương luôn có tổng các chữ số bằng 9 * m.", "latex": "S(A^2) = 9 \\times m"},
            {"explain": f"Với m = {k*2} chữ số 9, tổng các chữ số của B = A^2 là 9 * {k*2} = {ans_num}.", "latex": f"S(B) = 9 \\times {k*2} = {ans_num}"}
        ]
        kangaroo_sasmo_problems.append({
            "id": pid,
            "subject": "math",
            "level": "thcs",
            "grades": [7, 8, 9],
            "curriculum": ["olympiad"],
            "topic": f"SASMO Olympiad: Quy luật số học & Tổng các chữ số - Bài {k}",
            "type": "dien-so",
            "statement_vi": stmt_vi,
            "statement_en": stmt_en,
            "answer": str(ans_num),
            "answer_numeric": ans_num,
            "answer_unit": "",
            "tolerance": 0.001,
            "solution_steps": steps,
            "formulas_used": ["math.thpt.to-hop-xac-suat.quy-tac-cong"],
            "difficulty": 2,
            "estimated_minutes": 6,
            "skills": ["quy luật số học", "tổng chữ số của bình phương", "quy nạp nhận diện quy luật"],
            "hints": ["Hãy thử với các trường hợp nhỏ: 9^2, 99^2, 999^2 để tìm quy luật tổng chữ số.", "Tổng các chữ số luôn là bội của 9."],
            "tags": ["sasmo", "number-patterns", "digit-sum", "olympiad"]
        })
    else:
        # Bebras Graph & Binary Logic
        m = i - 20
        num_nodes = 4 + m
        # Complete graph edges = n*(n-1)/2
        num_edges = num_nodes * (num_nodes - 1) // 2
        stmt_vi = f"Trong một mạng máy tính đầy đủ (mesh network) gồm {num_nodes} máy chủ, mỗi cặp máy chủ được nối trực tiếp với nhau bằng đúng một đường cáp truyền dẫn. Cần tất cả bao nhiêu đường cáp nối?"
        stmt_en = f"In a fully connected mesh network of {num_nodes} servers, every pair of servers is directly connected by a cable. How many cables are required in total?"
        steps = [
            {"explain": f"Số đường cáp nối giữa {num_nodes} máy chủ tương ứng với số cạnh của đồ thị đầy đủ K_{{{num_nodes}}}.", "latex": f"|E| = \\binom{{{num_nodes}}}{2} = \\frac{{{num_nodes}({num_nodes} - 1)}}{2}"},
            {"explain": f"Tính giá trị số học: ({num_nodes} * {num_nodes-1}) / 2 = {num_edges} đường cáp.", "latex": f"|E| = \\frac{{{num_nodes} \\times {num_nodes-1}}}{2} = {num_edges}"}
        ]
        kangaroo_sasmo_problems.append({
            "id": pid,
            "subject": "math",
            "level": "thcs",
            "grades": [6, 7, 8, 9],
            "curriculum": ["olympiad"],
            "topic": f"Bebras Computational Thinking: Đồ thị mạng máy tính - Bài {m}",
            "type": "dien-so",
            "statement_vi": stmt_vi,
            "statement_en": stmt_en,
            "answer": str(num_edges),
            "answer_numeric": num_edges,
            "answer_unit": "đường cáp",
            "tolerance": 0.001,
            "solution_steps": steps,
            "formulas_used": ["math.thpt.to-hop-xac-suat.to-hop-chap-k"],
            "difficulty": 2,
            "estimated_minutes": 5,
            "skills": ["lý thuyết đồ thị mạng", "đồ thị đầy đủ Kn", "tư duy tính toán Bebras"],
            "hints": ["Mỗi máy chủ nối với (n - 1) máy chủ còn lại.", "Mỗi đường cáp có 2 đầu nối, do đó chia cho 2."],
            "tags": ["bebras", "graph-theory", "computational-thinking", "mesh-network"]
        })

# Write Kangaroo/SASMO slice
(PROBLEMS_DIR / "intl-competitions-kangaroo-sasmo.json").write_text(json.dumps({
    "meta": {
        "file": "intl-competitions-kangaroo-sasmo.json",
        "subject": "math",
        "title": "Tuyển tập Đề thi Tư duy Trực quan Kangaroo Math, SASMO và Bebras",
        "levels": ["thcs", "thpt"],
        "count": len(kangaroo_sasmo_problems)
    },
    "problems": kangaroo_sasmo_problems
}, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"Generated 3 datasets successfully: {len(amc_aime_problems) + len(sci_olympiad_problems) + len(kangaroo_sasmo_problems)} total problems.")
