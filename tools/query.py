#!/usr/bin/env python3
"""Tra cứu nhanh kho công thức AISTEM (không cần thư viện ngoài).

Ví dụ:
  python3 tools/query.py "dao ham"                    # tìm không dấu vẫn ra
  python3 tools/query.py "thấu kính" --subject physics
  python3 tools/query.py --grade 12 --subject math --topic "Tích phân"
  python3 tools/query.py --id math.thpt.dao-ham.dao-ham-cua-tich
  python3 tools/query.py --tag hardy-weinberg --format json
  python3 tools/query.py --stats

Yêu cầu: đã chạy `python3 tools/build_index.py` để sinh data/formulas/index.json.
"""
from __future__ import annotations

import argparse
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "data" / "formulas" / "index.json"

SUBJECT_VI = {"math": "Toán", "physics": "Vật lí", "chemistry": "Hoá", "biology": "Sinh"}
LEVEL_VI = {"tieu-hoc": "Tiểu học", "thcs": "THCS", "thpt": "THPT", "dai-hoc": "Đại học"}


def fold(s: str) -> str:
    s = s.lower().replace("đ", "d")
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def blob(f: dict) -> str:
    parts = [f.get("name_vi", ""), f.get("name_en", ""), f.get("topic", ""),
             f.get("subtopic", ""), f.get("latex", ""), f.get("note", ""),
             " ".join(f.get("tags", [])), " ".join(f.get("vars", {}).values())]
    return fold(" ".join(parts))


def show(f: dict) -> None:
    grades = ", ".join(str(g) for g in f.get("grades", []))
    head = f"{SUBJECT_VI.get(f['subject'], f['subject'])} · {LEVEL_VI.get(f['level'], f['level'])}"
    print(f"\n\033[1m{f['name_vi']}\033[0m"
          + (f"  ({f['name_en']})" if f.get("name_en") else ""))
    print(f"  {head} · lớp {grades} · {f['topic']}"
          + (f" › {f['subtopic']}" if f.get("subtopic") else ""))
    print(f"  \033[36m{f['latex']}\033[0m")
    if f.get("vars"):
        for k, v in f["vars"].items():
            unit = f.get("units", {}).get(k)
            print(f"    {k} = {v}" + (f"  [{unit}]" if unit else ""))
    if f.get("conditions"):
        print(f"  Điều kiện: {f['conditions']}")
    if f.get("note"):
        print(f"  Ghi chú: {f['note']}")
    print(f"  \033[2m{f['id']}\033[0m")


def main() -> int:
    ap = argparse.ArgumentParser(description="Tra cứu công thức AISTEM")
    ap.add_argument("query", nargs="?", default="", help="từ khoá (có dấu hoặc không dấu)")
    ap.add_argument("--subject", choices=list(SUBJECT_VI))
    ap.add_argument("--level", choices=list(LEVEL_VI))
    ap.add_argument("--grade", type=int)
    ap.add_argument("--topic")
    ap.add_argument("--tag")
    ap.add_argument("--id")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--format", choices=["text", "json", "latex"], default="text")
    ap.add_argument("--stats", action="store_true", help="in thống kê kho dữ liệu rồi thoát")
    a = ap.parse_args()

    if not INDEX.exists():
        print("Chưa có index.json. Chạy: python3 tools/build_index.py", file=sys.stderr)
        return 1
    index = json.loads(INDEX.read_text(encoding="utf-8"))

    if a.stats:
        print(json.dumps(index["stats"], ensure_ascii=False, indent=2))
        return 0

    res = index["formulas"]
    if a.id:
        res = [f for f in res if f["id"] == a.id]
    if a.subject:
        res = [f for f in res if f["subject"] == a.subject]
    if a.level:
        res = [f for f in res if f["level"] == a.level]
    if a.grade:
        res = [f for f in res if a.grade in f.get("grades", [])]
    if a.topic:
        t = fold(a.topic)
        res = [f for f in res if t in fold(f.get("topic", "")) or t in fold(f.get("subtopic", ""))]
    if a.tag:
        res = [f for f in res if a.tag in f.get("tags", [])]
    if a.query:
        q = fold(a.query)
        terms = q.split()
        scored = []
        for f in res:
            b = blob(f)
            if not all(t in b for t in terms):
                continue
            # ưu tiên khớp ở tên công thức, rồi khớp nguyên cụm
            score = (3 if q in fold(f.get("name_vi", "")) else 0) \
                    + (2 if q in b else 0) \
                    + sum(1 for t in terms if t in fold(f.get("name_vi", "")))
            scored.append((-score, f["id"], f))
        res = [f for _, _, f in sorted(scored)]

    total = len(res)
    res = res[: a.limit]

    if a.format == "json":
        print(json.dumps(res, ensure_ascii=False, indent=2))
    elif a.format == "latex":
        for f in res:
            print(f"% {f['name_vi']} ({f['id']})")
            print(f"\\[ {f['latex']} \\]\n")
    else:
        for f in res:
            show(f)
        print(f"\n{len(res)}/{total} kết quả" + (" (dùng --limit để xem thêm)" if total > len(res) else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
