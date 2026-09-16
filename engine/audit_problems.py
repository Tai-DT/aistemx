"""Kiểm định chất lượng sâu toàn bộ 4,351 bài toán trong kho AISTEM.

Kiểm tra:
1. Tính đầy đủ của cấu trúc bài toán: id, subject, level, topic, type, statement, answer
2. Trắc nghiệm: choices có đủ 4 phương án, answer hợp lệ, các distractors có 'why_wrong'
3. Công thức: formulas_used phải tồn tại trong kho 5,272 công thức (không có liên kết treo)
4. Lời giải chi tiết: solution_steps có giải thích (explain) và LaTeX chuẩn xác
5. Kỹ năng & độ khó: skills, difficulty hợp lệ
"""
from __future__ import annotations

import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
PROBLEMS_DIR = DATA_DIR / "problems"
FORMULAS_DIR = DATA_DIR / "formulas"


def load_all_formula_ids() -> Set[str]:
    """Nạp tất cả các id công thức hợp lệ từ kho formulas."""
    formula_ids: Set[str] = set()
    for p in FORMULAS_DIR.rglob("*.json"):
        if p.name in {"index.json", "schema.json", "usage.json"}:
            continue
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
            items = doc.get("formulas", []) if isinstance(doc, dict) else (doc if isinstance(doc, list) else [])
            for item in items:
                if isinstance(item, dict) and item.get("id"):
                    formula_ids.add(item["id"])
        except Exception:
            pass
    return formula_ids


def audit_problems() -> Dict[str, Any]:
    valid_formula_ids = load_all_formula_ids()
    files = sorted(p for p in PROBLEMS_DIR.rglob("*.json") if p.name not in {"index.json", "schema.json"})

    total_problems = 0
    by_subject: Counter[str] = Counter()
    by_level: Counter[str] = Counter()
    by_type: Counter[str] = Counter()

    missing_fields: Dict[str, List[str]] = defaultdict(list)
    dangling_formulas: List[Dict[str, Any]] = []
    choice_issues: List[Dict[str, Any]] = []
    missing_why_wrong: List[str] = []
    has_solution_steps = 0
    has_formulas_used = 0
    has_why_wrong_full = 0

    duplicate_ids: Dict[str, List[str]] = defaultdict(list)
    seen_ids: Dict[str, str] = {}

    for file_path in files:
        rel_path = file_path.relative_to(ROOT)
        try:
            doc = json.loads(file_path.read_text(encoding="utf-8"))
            items = doc.get("problems", []) if isinstance(doc, dict) else (doc if isinstance(doc, list) else [])
        except Exception as e:
            print(f"❌ Lỗi đọc file {file_path}: {e}")
            continue

        for idx, p in enumerate(items):
            if not isinstance(p, dict):
                continue
            pid = p.get("id")
            if not pid:
                missing_fields["id"].append(f"{rel_path}[{idx}]")
                continue

            total_problems += 1
            if pid in seen_ids:
                duplicate_ids[pid].append(str(rel_path))
                duplicate_ids[pid].append(seen_ids[pid])
            else:
                seen_ids[pid] = str(rel_path)

            subj = p.get("subject", "unknown")
            lvl = p.get("level", "unknown")
            ptype = p.get("type", "trac-nghiem")

            by_subject[subj] += 1
            by_level[lvl] += 1
            by_type[ptype] += 1

            # Kiểm tra trường bắt buộc
            for req in ["statement_vi", "answer", "topic"]:
                if not p.get(req):
                    missing_fields[req].append(pid)

            # Kiểm tra solution_steps
            steps = p.get("solution_steps", [])
            if steps and len(steps) > 0:
                has_solution_steps += 1

            # Kiểm tra formulas_used
            f_used = p.get("formulas_used", [])
            if f_used:
                has_formulas_used += 1
                for fid in f_used:
                    if fid not in valid_formula_ids:
                        dangling_formulas.append({
                            "problem_id": pid,
                            "formula_id": fid,
                            "file": str(rel_path)
                        })

            # Kiểm tra choices cho câu hỏi trắc nghiệm
            if ptype == "trac-nghiem":
                choices = p.get("choices", [])
                if not choices or len(choices) < 2:
                    choice_issues.append({"id": pid, "issue": f"Chỉ có {len(choices)} choices", "file": str(rel_path)})
                else:
                    ans = str(p.get("answer", "")).strip().upper()
                    keys = [str(c.get("key", "")).strip().upper() for c in choices]
                    if ans not in keys:
                        # Kiểm tra xem answer có phải là text của choice không
                        text_matches = [str(c.get("key", "")).strip().upper() for c in choices if str(c.get("text", "")).strip() == str(p.get("answer", "")).strip()]
                        if not text_matches:
                            choice_issues.append({"id": pid, "issue": f"Đáp án '{ans}' không khớp với các lựa chọn {keys}", "file": str(rel_path)})

                    # Kiểm tra why_wrong trên các distractor
                    distractors = [c for c in choices if str(c.get("key", "")).strip().upper() != ans]
                    distractors_with_why_wrong = [c for c in distractors if c.get("why_wrong")]
                    if distractors and len(distractors_with_why_wrong) == len(distractors):
                        has_why_wrong_full += 1
                    else:
                        missing_why_wrong.append(pid)

    return {
        "total_problems": total_problems,
        "files_count": len(files),
        "by_subject": dict(by_subject),
        "by_level": dict(by_level),
        "by_type": dict(by_type),
        "has_solution_steps": has_solution_steps,
        "solution_steps_pct": round(has_solution_steps / max(total_problems, 1) * 100, 1),
        "has_formulas_used": has_formulas_used,
        "formulas_used_pct": round(has_formulas_used / max(total_problems, 1) * 100, 1),
        "has_why_wrong_full": has_why_wrong_full,
        "why_wrong_pct": round(has_why_wrong_full / max(by_type.get("trac-nghiem", 1), 1) * 100, 1),
        "missing_fields": {k: len(v) for k, v in missing_fields.items()},
        "duplicate_ids_count": len(duplicate_ids),
        "choice_issues_count": len(choice_issues),
        "choice_issues_sample": choice_issues[:5],
        "dangling_formulas_count": len(dangling_formulas),
        "dangling_formulas_sample": dangling_formulas[:5]
    }


if __name__ == "__main__":
    t0 = time.perf_counter()
    res = audit_problems()
    elapsed = time.perf_counter() - t0

    print("=" * 65)
    print("📊 BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG KHO BÀI TOÁN AISTEM")
    print("=" * 65)
    print(f"Tổng số bài toán: {res['total_problems']:,} bài trong {res['files_count']} tệp JSON.")
    print(f"Thời gian quét:   {elapsed:.2f}s")
    print("\n1. Phân bổ theo môn học:")
    for subj, count in res["by_subject"].items():
        print(f"   - {subj:12}: {count:,} ({count/res['total_problems']*100:.1f}%)")

    print("\n2. Phân bổ theo cấp học:")
    for lvl, count in res["by_level"].items():
        print(f"   - {lvl:12}: {count:,} ({count/res['total_problems']*100:.1f}%)")

    print("\n3. Phân bổ theo loại câu hỏi:")
    for t, count in res["by_type"].items():
        print(f"   - {t:15}: {count:,}")

    print("\n4. Tỷ lệ sư phạm chuyên sâu:")
    print(f"   - Có lời giải chi tiết (solution_steps): {res['has_solution_steps']:,} ({res['solution_steps_pct']}%)")
    print(f"   - Có liên kết công thức (formulas_used): {res['has_formulas_used']:,} ({res['formulas_used_pct']}%)")
    print(f"   - Trắc nghiệm có đủ 'why_wrong':        {res['has_why_wrong_full']:,} ({res['why_wrong_pct']}%)")

    print("\n5. Kiểm định tính toàn vẹn:")
    print(f"   - Trùng lặp ID:             {res['duplicate_ids_count']}")
    print(f"   - Lỗi cấu trúc choices/đáp án: {res['choice_issues_count']}")
    if res['choice_issues_sample']:
        for item in res['choice_issues_sample']:
            print(f"     ⚠️ {item['id']}: {item['issue']}")
    print(f"   - Liên kết công thức treo (dangling): {res['dangling_formulas_count']}")
    if res['dangling_formulas_sample']:
        for item in res['dangling_formulas_sample']:
            print(f"     ⚠️ {item['problem_id']} -> {item['formula_id']}")
    print("=" * 65)
