#!/usr/bin/env python3
"""Dựng chỉ mục và bản xuất cho kho công thức AISTEM.

Chạy:  python3 tools/build_index.py

Sinh ra:
  data/formulas/index.json   — toàn bộ công thức gộp lại + thống kê + cây chủ đề
  data/formulas/corpus.jsonl — mỗi dòng một công thức, tiện nạp vào vector DB / RAG
  docs/formulas/<mon>.md     — bản Markdown để người đọc, LaTeX bọc trong $...$
"""
from __future__ import annotations

import json
import unicodedata
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "formulas"
DOCS = ROOT / "docs" / "formulas"

SUBJECT_VI = {"math": "Toán học", "physics": "Vật lí", "chemistry": "Hoá học", "biology": "Sinh học"}
LEVEL_VI = {"tieu-hoc": "Tiểu học (lớp 1-5)", "thcs": "THCS (lớp 6-9)",
            "thpt": "THPT (lớp 10-12)", "dai-hoc": "Đại học"}
LEVEL_ORDER = ["tieu-hoc", "thcs", "thpt", "dai-hoc"]


def strip_accents(s: str) -> str:
    """Bỏ dấu tiếng Việt để phục vụ tìm kiếm không dấu."""
    s = s.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def search_blob(f: dict) -> str:
    """Chuỗi tìm kiếm phẳng: tên, chủ đề, thẻ, biến — cả có dấu lẫn không dấu."""
    parts = [f["name_vi"], f.get("name_en", ""), f["topic"], f.get("subtopic", ""),
             " ".join(f.get("tags", [])), " ".join(f.get("vars", {}).values())]
    raw = " ".join(p for p in parts if p).lower()
    return raw + " " + strip_accents(raw)


def load_slices() -> list[tuple[Path, dict]]:
    out = []
    for p in sorted(DATA.rglob("*.json")):
        if p.name in {"schema.json", "index.json", "usage.json"}:
            continue
        out.append((p, json.loads(p.read_text(encoding="utf-8"))))
    return out


def main() -> int:
    slices = load_slices()
    if not slices:
        print("Chưa có file dữ liệu nào trong", DATA)
        return 1

    formulas: list[dict] = []
    sources: list[dict] = []
    for path, doc in slices:
        rel = str(path.relative_to(ROOT))
        sources.append({
            "file": rel,
            "title": doc["meta"]["title"],
            "subject": doc["meta"]["subject"],
            "levels": doc["meta"]["levels"],
            "count": len(doc["formulas"]),
        })
        for f in doc["formulas"]:
            rec = dict(f)
            rec["source_file"] = rel
            formulas.append(rec)

    formulas.sort(key=lambda f: (
        f["subject"],
        LEVEL_ORDER.index(f["level"]) if f["level"] in LEVEL_ORDER else 9,
        min(f.get("grades", [99])),
        max(f.get("grades", [99])),
        f.get("topic", ""),
        f.get("subtopic", ""),
        f.get("id", "")
    ))

    by_subject: dict[str, int] = defaultdict(int)
    by_level: dict[str, int] = defaultdict(int)
    by_grade: dict[int, int] = defaultdict(int)
    by_tag: dict[str, int] = defaultdict(int)
    topics: dict[str, dict[str, dict[str, int]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

    by_curriculum: dict[str, int] = defaultdict(int)
    for f in formulas:
        by_subject[f["subject"]] += 1
        by_level[f["level"]] += 1
        for c in f.get("curriculum", []):
            by_curriculum[c] += 1
        for g in f.get("grades", []):
            by_grade[g] += 1
        for t in f.get("tags", []):
            by_tag[t] += 1
        topics[f["subject"]][f["level"]][f["topic"]] += 1

    index = {
        "generated_by": "tools/build_index.py",
        "schema": "data/formulas/schema.json",
        "stats": {
            "total": len(formulas),
            "by_subject": {k: by_subject[k] for k in sorted(by_subject)},
            "by_level": {k: by_level[k] for k in LEVEL_ORDER if k in by_level},
            "by_curriculum": dict(sorted(by_curriculum.items(), key=lambda kv: -kv[1])),
            "by_grade": {str(g): by_grade[g] for g in sorted(by_grade)},
            "top_tags": dict(sorted(by_tag.items(), key=lambda kv: -kv[1])[:40]),
            "unique_topics": sum(len(lv) for s in topics.values() for lv in s.values()),
        },
        "sources": sources,
        "topic_tree": {s: {lv: dict(sorted(t.items())) for lv, t in sorted(
            levels.items(), key=lambda kv: LEVEL_ORDER.index(kv[0]) if kv[0] in LEVEL_ORDER else 9)}
            for s, levels in sorted(topics.items())},
        "formulas": formulas,
    }

    (DATA / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")

    # corpus.jsonl — một dòng một công thức, kèm trường tìm kiếm phẳng cho RAG
    with (DATA / "corpus.jsonl").open("w", encoding="utf-8") as fh:
        for f in formulas:
            rec = dict(f)
            rec["search"] = search_blob(f)
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # Bản Markdown cho người đọc
    DOCS.mkdir(parents=True, exist_ok=True)
    for subject in sorted(by_subject):
        lines = [f"# {SUBJECT_VI[subject]} — Tổng hợp công thức AISTEM", "",
                 f"Tổng số: **{by_subject[subject]}** công thức. ",
                 "Sinh tự động từ `data/formulas/` bằng `tools/build_index.py` — không sửa tay file này.", ""]
        subset = [f for f in formulas if f["subject"] == subject]
        for level in LEVEL_ORDER:
            lv = [f for f in subset if f["level"] == level]
            if not lv:
                continue
            lines += [f"## {LEVEL_VI[level]} ({len(lv)} công thức)", ""]
            current_topic = None
            for f in lv:
                if f["topic"] != current_topic:
                    current_topic = f["topic"]
                    lines += [f"### {current_topic}", ""]
                lines.append(f"**{f['name_vi']}**"
                             + (f" — *{f['name_en']}*" if f.get("name_en") else ""))
                lines += ["", f"$${f['latex']}$$", ""]
                if f.get("vars"):
                    lines.append("Trong đó: " + "; ".join(
                        f"`{k}` là {v}" + (f" ({f['units'][k]})" if k in f.get("units", {}) else "")
                        for k, v in f["vars"].items()) + ".")
                    lines.append("")
                if f.get("conditions"):
                    lines += [f"*Điều kiện:* {f['conditions']}", ""]
                if f.get("note"):
                    lines += [f"*Ghi chú:* {f['note']}", ""]
                lines += [f"<sub>`{f['id']}` · lớp {', '.join(map(str, f.get('grades', [])))}"
                          f" · {' '.join('#' + t for t in f.get('tags', []))}</sub>", "", "---", ""]
        (DOCS / f"{subject}.md").write_text("\n".join(lines), encoding="utf-8")

    print(f"index.json    : {len(formulas)} công thức")
    print(f"corpus.jsonl  : {len(formulas)} dòng")
    print(f"docs/formulas : {len(by_subject)} file Markdown")
    print("Theo môn      : " + ", ".join(f"{SUBJECT_VI[k]} {v}" for k, v in sorted(by_subject.items())))
    print("Theo cấp      : " + ", ".join(f"{LEVEL_VI[k]} {by_level[k]}" for k in LEVEL_ORDER if k in by_level))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
