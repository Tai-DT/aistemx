#!/usr/bin/env python3
"""Kiểm định ba kho nội dung: bài học, bài tập, đề thi.

Chạy:  python3 tools/validate_content.py [--strict]

Ngoài kiểm tra cấu trúc, công cụ này đối chiếu CHÉO sang kho công thức:
mọi id công thức được tham chiếu trong bài học / bài tập / hồ sơ đề thi
đều phải tồn tại thật trong data/formulas.

Thoát mã 1 nếu có lỗi. --strict coi cảnh báo cũng là lỗi.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SUBJECTS = {"math", "physics", "chemistry", "biology"}
LEVELS = {"tieu-hoc", "thcs", "thpt", "dai-hoc"}
CURRICULA = {"vn-gdpt-2018", "ap", "ib", "a-level",
             "intl-undergrad", "olympiad", "ru-east-eu"}
LEVEL_GRADES = {"tieu-hoc": set(range(1, 6)), "thcs": set(range(6, 10)),
                "thpt": set(range(10, 13)), "dai-hoc": {13}}

LESSON_KEYS = {"id", "subject", "level", "grades", "curriculum", "unit", "order",
               "title_vi", "title_en", "objectives", "prerequisites", "key_concepts",
               "content", "formulas", "worked_examples", "common_mistakes",
               "duration_minutes", "difficulty", "tags"}
PROBLEM_KEYS = {"id", "subject", "level", "grades", "curriculum", "topic", "type",
                "statement_vi", "statement_en", "answer", "solution_steps",
                "formulas_used", "difficulty", "estimated_minutes", "skills", "tags"}
EXAM_KEYS = {"id", "name", "provider", "subject", "curriculum", "level", "overview",
             "sections", "topic_weights", "question_types", "formula_sheet_provided",
             "formulas_must_memorize", "scoring", "strategies", "common_traps", "tags"}

OPT = {
    "lessons": {"sources", "video_lectures", "animations"},
    "problems": {"choices", "answer_numeric", "answer_unit", "tolerance", "hints", "sources"},
    "exams": {"sources"},
}
REQ = {"lessons": LESSON_KEYS, "problems": PROBLEM_KEYS, "exams": EXAM_KEYS}
ID_RE = {
    "lessons": re.compile(r"^lesson\.[a-z]+(\.[a-z0-9-]+){2}$"),
    "problems": re.compile(r"^prob\.[a-z]+\.[a-z0-9-]+\.[0-9]{4}$"),
    "exams": re.compile(r"^exam\.[a-z0-9-]+$"),
}
TAG_RE = re.compile(r"^[a-z0-9-]+$")
LEFT_RE = re.compile(r"\\left(?![a-zA-Z])")
RIGHT_RE = re.compile(r"\\right(?![a-zA-Z])")

errors: list[str] = []
warnings: list[str] = []


def err(w: str, m: str) -> None:
    errors.append(f"ERROR {w}: {m}")


def warn(w: str, m: str) -> None:
    warnings.append(f"WARN  {w}: {m}")


def formula_ids() -> set[str]:
    out: set[str] = set()
    for p in (DATA / "formulas").rglob("*.json"):
        if p.name in {"schema.json", "index.json"}:
            continue
        try:
            for f in json.loads(p.read_text(encoding="utf-8")).get("formulas", []):
                out.add(f["id"])
        except (json.JSONDecodeError, KeyError, TypeError):
            pass
    return out


def check_latex(where: str, s: str) -> None:
    if not s:
        return
    g = s.replace(r"\{", "").replace(r"\}", "")
    if g.count("{") != g.count("}"):
        err(where, f"latex lệch ngoặc nhọn: {g.count('{')} / {g.count('}')}")
    if len(LEFT_RE.findall(s)) != len(RIGHT_RE.findall(s)):
        err(where, r"latex lệch \left / \right")
    if s.strip().startswith("$") or s.strip().endswith("$"):
        err(where, "latex trong solution_steps không được bọc dấu $")


def check_common(where: str, r: dict, kind: str) -> None:
    if r.get("subject") not in SUBJECTS:
        err(where, f"subject không hợp lệ: {r.get('subject')!r}")
    if r.get("level") not in LEVELS:
        err(where, f"level không hợp lệ: {r.get('level')!r}")
    cur = r.get("curriculum")
    if not isinstance(cur, list) or not cur:
        err(where, "curriculum phải là mảng không rỗng")
    else:
        bad = [c for c in cur if c not in CURRICULA]
        if bad:
            err(where, f"curriculum không hợp lệ: {bad}")
    if kind != "exams":
        g = r.get("grades")
        if not isinstance(g, list) or not g:
            err(where, "grades phải là mảng không rỗng")
        elif not any(x in LEVEL_GRADES.get(r.get("level"), set()) for x in g):
            warn(where, f"grades {g} không có lớp nào thuộc level {r.get('level')}")
    tags = r.get("tags")
    if not isinstance(tags, list) or not tags:
        err(where, "tags phải là mảng không rỗng")
    else:
        for t in tags:
            if not isinstance(t, str) or not TAG_RE.match(t):
                err(where, f"tag sai định dạng: {t!r}")


def check_refs(where: str, ids: list, pool: set[str], label: str) -> None:
    if not isinstance(ids, list):
        err(where, f"{label} phải là mảng")
        return
    for i in ids:
        if i not in pool:
            err(where, f"{label} trỏ tới id không tồn tại: {i}")


def main() -> int:
    strict = "--strict" in sys.argv
    fids = formula_ids()
    if not fids:
        print("Cảnh báo: không đọc được kho công thức, bỏ qua đối chiếu chéo id.")

    counts: dict[str, int] = defaultdict(int)
    all_lesson_ids: set[str] = set()
    docs: list[tuple[str, Path, dict]] = []

    for kind in ("lessons", "problems", "exams"):
        d = DATA / kind
        if not d.exists():
            continue
        for p in sorted(d.rglob("*.json")):
            if p.name in {"schema.json", "index.json"}:
                continue
            try:
                docs.append((kind, p, json.loads(p.read_text(encoding="utf-8"))))
            except json.JSONDecodeError as e:
                err(str(p.relative_to(ROOT)), f"JSON hỏng: {e}")

    if not docs:
        print("Chưa có dữ liệu bài học / bài tập / đề thi để kiểm định.")
        return 0

    # gom trước toàn bộ id để kiểm tra trùng và tham chiếu nội bộ
    seen: dict[str, str] = {}
    for kind, p, doc in docs:
        rel = str(p.relative_to(ROOT))
        for r in doc.get(kind, []):
            rid = r.get("id")
            if not isinstance(rid, str):
                continue
            if rid in seen:
                err(rel, f"id TRÙNG với {seen[rid]}: {rid}")
            else:
                seen[rid] = rel
            if kind == "lessons":
                all_lesson_ids.add(rid)

    for kind, p, doc in docs:
        rel = str(p.relative_to(ROOT))
        if set(doc) != {"meta", kind}:
            err(rel, f"cấp cao nhất phải là meta/{kind}, đang có {sorted(doc)}")
            continue
        records = doc[kind]
        if doc["meta"].get("count") != len(records):
            err(rel, f"meta.count = {doc['meta'].get('count')} nhưng có {len(records)} bản ghi")
        counts[kind] += len(records)

        for i, r in enumerate(records):
            rid = r.get("id", f"#{i}")
            where = f"{rel}[{rid}]"
            missing = REQ[kind] - set(r)
            extra = set(r) - REQ[kind] - OPT[kind]
            if missing:
                err(where, f"thiếu khoá: {sorted(missing)}")
            if extra:
                err(where, f"khoá lạ: {sorted(extra)}")
            if missing:
                continue
            if not ID_RE[kind].match(r["id"]):
                err(where, f"id sai định dạng: {r['id']!r}")
            check_common(where, r, kind)

            if kind == "lessons":
                check_refs(where, r["formulas"], fids, "formulas")
                check_refs(where, r["prerequisites"], all_lesson_ids, "prerequisites")
                if r["id"] in r["prerequisites"]:
                    err(where, "prerequisites tự trỏ vào chính nó")
                if len(r["content"]) < 200:
                    err(where, f"content quá ngắn ({len(r['content'])} ký tự, tối thiểu 200)")
                if not r["objectives"]:
                    err(where, "objectives rỗng")
                if not r["worked_examples"]:
                    err(where, "worked_examples rỗng")
                if r["difficulty"] not in {"co-ban", "trung-binh", "nang-cao", "chuyen-sau"}:
                    err(where, f"difficulty không hợp lệ: {r['difficulty']!r}")

            elif kind == "problems":
                check_refs(where, r["formulas_used"], fids, "formulas_used")
                if r["type"] not in {"trac-nghiem", "tu-luan", "dien-so", "dung-sai", "ghep-doi"}:
                    err(where, f"type không hợp lệ: {r['type']!r}")
                if r["type"] == "trac-nghiem":
                    ch = r.get("choices")
                    if not isinstance(ch, list) or len(ch) < 2:
                        err(where, "trắc nghiệm phải có tối thiểu 2 phương án")
                    else:
                        keys = [c.get("key") for c in ch]
                        if len(keys) != len(set(keys)):
                            err(where, f"khoá phương án trùng: {keys}")
                        if r["answer"] not in keys:
                            err(where, f"answer {r['answer']!r} không khớp phương án nào {keys}")
                elif r.get("choices"):
                    warn(where, f"type = {r['type']} nhưng vẫn khai báo choices")
                if not isinstance(r["difficulty"], int) or not 1 <= r["difficulty"] <= 5:
                    err(where, f"difficulty phải là số nguyên 1-5, đang là {r['difficulty']!r}")
                if not r["solution_steps"]:
                    err(where, "solution_steps rỗng")
                for j, s in enumerate(r["solution_steps"]):
                    if not s.get("explain"):
                        err(where, f"solution_steps[{j}] thiếu explain")
                    check_latex(f"{where}.step{j}", s.get("latex", ""))
                if r.get("tolerance") is not None and r.get("answer_numeric") is None:
                    warn(where, "có tolerance nhưng thiếu answer_numeric để chấm tự động")

            else:  # exams
                check_refs(where, r["formulas_must_memorize"], fids, "formulas_must_memorize")
                sw = sum(s.get("weight_percent", 0) for s in r["sections"])
                if abs(sw - 100) > 1.5:
                    warn(where, f"tổng weight_percent các phần = {sw}, lệch xa 100")
                tw = sum(r["topic_weights"].values())
                if r["topic_weights"] and abs(tw - 100) > 5:
                    warn(where, f"tổng topic_weights = {tw:.1f}, lệch xa 100")
                if not r["strategies"]:
                    err(where, "strategies rỗng")

    for line in warnings:
        print(line)
    for line in errors:
        print(line)

    print("\n" + "=" * 58)
    print("Bài học: {}  |  Bài tập: {}  |  Hồ sơ đề thi: {}".format(
        counts["lessons"], counts["problems"], counts["exams"]))
    print(f"Đối chiếu chéo với {len(fids)} id công thức")
    print(f"Lỗi: {len(errors)} | Cảnh báo: {len(warnings)}")
    print("=" * 58)

    if errors or (strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
