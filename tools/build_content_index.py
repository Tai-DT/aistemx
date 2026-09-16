#!/usr/bin/env python3
"""Dựng chỉ mục cho kho bài học, bài tập và đề thi của AISTEM.

Chạy:  python3 tools/build_content_index.py

Sinh ra:
  data/lessons/index.json    Toàn bộ bài học + thống kê + cây unit + lộ trình học
  data/problems/index.json   Toàn bộ bài tập + thống kê theo độ khó / kỹ năng
  data/exams/index.json      Toàn bộ hồ sơ đề thi
  data/content-corpus.jsonl  Gộp cả ba, mỗi dòng một bản ghi, có trường search phẳng
  docs/lessons/<mon>.md      Bản Markdown bài học cho người đọc

Ngoài ra dựng ĐỒ THỊ NGƯỢC từ công thức sang nội dung: với mỗi id công thức, biết
những bài học và bài tập nào dùng nó (ghi vào data/formulas/usage.json).
"""
from __future__ import annotations

import json
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "lessons"

SUBJECT_VI = {"math": "Toán học", "physics": "Vật lí", "chemistry": "Hoá học", "biology": "Sinh học"}
LEVEL_VI = {"tieu-hoc": "Tiểu học", "thcs": "THCS", "thpt": "THPT (lớp 10-12)", "dai-hoc": "Đại học"}
LEVEL_ORDER = ["tieu-hoc", "thcs", "thpt", "dai-hoc"]
DIFF_VI = {1: "Nhận biết", 2: "Thông hiểu", 3: "Vận dụng", 4: "Vận dụng cao", 5: "Olympiad"}


def fold(s: str) -> str:
    s = s.lower().replace("đ", "d")
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def load(kind: str) -> list[dict]:
    out: list[dict] = []
    d = DATA / kind
    if not d.exists():
        return out
    for p in sorted(d.rglob("*.json")):
        if p.name in {"schema.json", "index.json"}:
            continue
        doc = json.loads(p.read_text(encoding="utf-8"))
        for r in doc.get(kind, []):
            rec = dict(r)
            rec["source_file"] = str(p.relative_to(ROOT))
            out.append(rec)
    return out


def search_blob(r: dict, kind: str) -> str:
    if kind == "lessons":
        parts = [r["title_vi"], r.get("title_en", ""), r.get("unit", ""),
                 " ".join(r.get("objectives", [])), " ".join(r.get("tags", [])),
                 " ".join(c["term_vi"] + " " + c.get("term_en", "") for c in r.get("key_concepts", []))]
    elif kind == "problems":
        parts = [r["statement_vi"][:400], r.get("topic", ""),
                 " ".join(r.get("skills", [])), " ".join(r.get("tags", []))]
    else:
        parts = [r["name"], r.get("provider", ""), r.get("overview", "")[:400],
                 " ".join(r.get("tags", []))]
    raw = " ".join(p for p in parts if p).lower()
    return raw + " " + fold(raw)


def main() -> int:
    lessons = load("lessons")
    problems = load("problems")
    exams = load("exams")
    if not (lessons or problems or exams):
        print("Chưa có dữ liệu bài học / bài tập / đề thi.")
        return 1

    # ---------- bài học ----------
    if lessons:
        lessons.sort(key=lambda l: (l["subject"], LEVEL_ORDER.index(l["level"]) if l["level"] in LEVEL_ORDER else 9,
                                    l.get("unit", ""), l.get("order", 0)))
        by_s: dict[str, int] = defaultdict(int)
        by_l: dict[str, int] = defaultdict(int)
        by_c: dict[str, int] = defaultdict(int)
        units: dict[str, dict[str, list]] = defaultdict(lambda: defaultdict(list))
        minutes = 0
        for l in lessons:
            by_s[l["subject"]] += 1
            by_l[l["level"]] += 1
            for c in l.get("curriculum", []):
                by_c[c] += 1
            minutes += l.get("duration_minutes", 0)
            units[l["subject"]][l.get("unit", "(chưa phân unit)")].append(
                {"id": l["id"], "order": l.get("order", 0), "title": l["title_vi"]})
        for s in units:
            for u in units[s]:
                units[s][u].sort(key=lambda x: x["order"])
        (DATA / "lessons" / "index.json").write_text(json.dumps({
            "generated_by": "tools/build_content_index.py",
            "schema": "data/lessons/schema.json",
            "stats": {"total": len(lessons), "by_subject": dict(sorted(by_s.items())),
                      "by_level": {k: by_l[k] for k in LEVEL_ORDER if k in by_l},
                      "by_curriculum": dict(sorted(by_c.items(), key=lambda kv: -kv[1])),
                      "total_hours": round(minutes / 60, 1)},
            "unit_tree": {s: dict(sorted(u.items())) for s, u in sorted(units.items())},
            "lessons": lessons,
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------- bài tập ----------
    if problems:
        problems.sort(key=lambda p: (p["subject"], LEVEL_ORDER.index(p["level"]) if p["level"] in LEVEL_ORDER else 9,
                                     p.get("topic", ""), p["id"]))
        by_s = defaultdict(int); by_l = defaultdict(int)
        by_d: dict[int, int] = defaultdict(int)
        by_t: dict[str, int] = defaultdict(int)
        by_skill: dict[str, int] = defaultdict(int)
        for p in problems:
            by_s[p["subject"]] += 1
            by_l[p["level"]] += 1
            by_d[p.get("difficulty", 0)] += 1
            by_t[p.get("type", "")] += 1
            for k in p.get("skills", []):
                by_skill[k] += 1
        (DATA / "problems" / "index.json").write_text(json.dumps({
            "generated_by": "tools/build_content_index.py",
            "schema": "data/problems/schema.json",
            "stats": {"total": len(problems), "by_subject": dict(sorted(by_s.items())),
                      "by_level": {k: by_l[k] for k in LEVEL_ORDER if k in by_l},
                      "by_difficulty": {str(k): by_d[k] for k in sorted(by_d)},
                      "by_type": dict(sorted(by_t.items(), key=lambda kv: -kv[1])),
                      "auto_gradable": sum(1 for p in problems
                                           if p.get("type") == "trac-nghiem" or p.get("answer_numeric") is not None),
                      "top_skills": dict(sorted(by_skill.items(), key=lambda kv: -kv[1])[:40])},
            "problems": problems,
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------- đề thi ----------
    if exams:
        exams.sort(key=lambda e: e["id"])
        (DATA / "exams" / "index.json").write_text(json.dumps({
            "generated_by": "tools/build_content_index.py",
            "schema": "data/exams/schema.json",
            "stats": {"total": len(exams),
                      "by_subject": dict(sorted(defaultdict(int, {
                          s: sum(1 for e in exams if e["subject"] == s)
                          for s in {e["subject"] for e in exams}}).items()))},
            "exams": exams,
        }, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------- corpus gộp cho RAG ----------
    with (DATA / "content-corpus.jsonl").open("w", encoding="utf-8") as fh:
        for kind, items in (("lessons", lessons), ("problems", problems), ("exams", exams)):
            for r in items:
                rec = dict(r)
                rec["kind"] = kind
                rec["search"] = search_blob(r, kind)
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # ---------- đồ thị ngược: công thức -> nội dung dùng nó ----------
    usage: dict[str, dict[str, list[str]]] = defaultdict(lambda: {"lessons": [], "problems": [], "exams": []})
    for l in lessons:
        for fid in l.get("formulas", []):
            usage[fid]["lessons"].append(l["id"])
    for p in problems:
        for fid in p.get("formulas_used", []):
            usage[fid]["problems"].append(p["id"])
    for e in exams:
        for fid in e.get("formulas_must_memorize", []):
            usage[fid]["exams"].append(e["id"])
    (DATA / "formulas" / "usage.json").write_text(
        json.dumps({"generated_by": "tools/build_content_index.py",
                    "described": len(usage), "usage": dict(sorted(usage.items()))},
                   ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------- Markdown bài học ----------
    if lessons:
        DOCS.mkdir(parents=True, exist_ok=True)
        for subject in sorted({l["subject"] for l in lessons}):
            subset = [l for l in lessons if l["subject"] == subject]
            lines = [f"# {SUBJECT_VI[subject]} — Bài học AISTEM", "",
                     f"Tổng số: **{len(subset)}** bài. Sinh tự động bằng `tools/build_content_index.py`.", ""]
            cur_unit = None
            for l in subset:
                if l.get("unit") != cur_unit:
                    cur_unit = l.get("unit")
                    lines += [f"## {cur_unit}", ""]
                lines += [f"### {l.get('order', '')}. {l['title_vi']}",
                          f"*{l.get('title_en', '')}* · {LEVEL_VI.get(l['level'], l['level'])} · "
                          f"{', '.join(l.get('curriculum', []))} · {l.get('duration_minutes', '?')} phút · "
                          f"{l.get('difficulty', '')}", ""]
                if l.get("objectives"):
                    lines += ["**Mục tiêu:**"] + [f"- {o}" for o in l["objectives"]] + [""]
                lines += [l["content"], ""]
                if l.get("common_mistakes"):
                    lines += ["**Lỗi thường gặp:**"] + [f"- {m}" for m in l["common_mistakes"]] + [""]
                lines += [f"<sub>`{l['id']}`</sub>", "", "---", ""]
            (DOCS / f"{subject}.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"Bài học      : {len(lessons)}")
    print(f"Bài tập      : {len(problems)}")
    print(f"Hồ sơ đề thi : {len(exams)}")
    print(f"Công thức được nội dung tham chiếu: {len(usage)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
