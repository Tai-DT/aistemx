#!/usr/bin/env python3
"""Soát và gộp công thức trùng lặp trong kho AISTEM.

    python3 tools/dedupe.py --report
        Liệt kê các nhóm trùng tên tiếng Anh, phân loại thành:
          TRÙNG THẬT   cùng môn + cùng cấp + cùng chương trình -> nên gộp
          LIÊN MÔN     cùng công thức nhưng khác môn          -> giữ cả hai, nên nối related
          KHÁC PHẠM VI khác cấp hoặc khác chương trình         -> giữ cả hai, hợp lệ

    python3 tools/dedupe.py --merge <id_xoa>=<id_giu> [...]
        Xoá bản ghi thừa, dồn "related" của nó sang bản giữ lại, và nối lại
        MỌI tham chiếu tới id đã xoá trên toàn kho.

    python3 tools/dedupe.py --link
        Với các nhóm LIÊN MÔN, thêm related hai chiều để đồ thị tri thức nối
        được cùng một công thức giữa các môn.

Thêm --dry-run để xem trước mà không ghi file.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "formulas"


def load() -> dict[Path, dict]:
    return {p: json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(DATA.rglob("*.json"))
            if p.name not in {"schema.json", "index.json", "usage.json"}}


def save(docs: dict[Path, dict]) -> None:
    for p, d in docs.items():
        d["meta"]["count"] = len(d["formulas"])
        p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def groups(docs: dict[Path, dict]) -> dict[str, list[dict]]:
    by: dict[str, list[dict]] = defaultdict(list)
    for d in docs.values():
        for f in d["formulas"]:
            k = f.get("name_en", "").strip().lower()
            if k:
                by[k].append(f)
    return {k: v for k, v in by.items() if len(v) > 1}


def classify(v: list[dict]) -> str:
    sigs = {(f["subject"], f["level"], tuple(sorted(f["curriculum"]))) for f in v}
    if len(sigs) < len(v):
        return "TRUNG THAT"
    if len({f["subject"] for f in v}) > 1:
        return "LIEN MON"
    return "KHAC PHAM VI"


def cmd_report(docs: dict[Path, dict]) -> None:
    g = groups(docs)
    buckets: dict[str, list] = defaultdict(list)
    for k, v in g.items():
        buckets[classify(v)].append((k, v))
    for kind in ("TRUNG THAT", "LIEN MON", "KHAC PHAM VI"):
        items = buckets[kind]
        print(f"\n{'=' * 62}\n{kind}: {len(items)} nhóm, {sum(len(v) for _, v in items)} bản ghi\n{'=' * 62}")
        for k, v in sorted(items)[: 40 if kind == "TRUNG THAT" else 12]:
            print(f"  {k!r}")
            for f in v:
                print(f"     {f['id']}  [{f['subject']}|{f['level']}|{','.join(f['curriculum'])}]")
        if len(items) > (40 if kind == "TRUNG THAT" else 12):
            print(f"  ... và {len(items) - (40 if kind == 'TRUNG THAT' else 12)} nhóm nữa")


def cmd_merge(docs: dict[Path, dict], pairs: list[str], dry: bool) -> int:
    index = {f["id"]: f for d in docs.values() for f in d["formulas"]}
    plan: dict[str, str] = {}
    for spec in pairs:
        if "=" not in spec:
            print(f"Bỏ qua {spec!r}: phải có dạng id_xoa=id_giu")
            continue
        drop, keep = spec.split("=", 1)
        if drop not in index:
            print(f"Bỏ qua: không có id {drop}")
            continue
        if keep not in index:
            print(f"Bỏ qua: không có id giữ lại {keep}")
            continue
        plan[drop] = keep

    if not plan:
        print("Không có cặp hợp lệ nào.")
        return 1

    # dồn related của bản bị xoá sang bản giữ lại
    for drop, keep in plan.items():
        k = index[keep]
        for r in index[drop].get("related", []):
            if r != keep and r not in k["related"] and r not in plan:
                k["related"].append(r)

    removed = 0
    for d in docs.values():
        before = len(d["formulas"])
        d["formulas"] = [f for f in d["formulas"] if f["id"] not in plan]
        removed += before - len(d["formulas"])

    # nối lại mọi tham chiếu trỏ tới id đã xoá
    rewired = 0
    valid = {f["id"] for d in docs.values() for f in d["formulas"]}
    for d in docs.values():
        for f in d["formulas"]:
            out = []
            for r in f.get("related", []):
                r = plan.get(r, r)
                if r != f["id"] and r in valid and r not in out:
                    out.append(r)
                elif r not in valid:
                    rewired += 0
            if out != f.get("related"):
                rewired += 1
            f["related"] = out

    for drop, keep in plan.items():
        print(f"  xoá {drop}\n   -> giữ {keep}")
    print(f"\nĐã xoá {removed} bản ghi, cập nhật related của {rewired} bản ghi.")
    if dry:
        print("--dry-run: không ghi file.")
        return 0
    save(docs)
    print("Đã ghi lại kho.")
    return 0


def cmd_link(docs: dict[Path, dict], dry: bool) -> int:
    g = groups(docs)
    added = 0
    for k, v in g.items():
        if classify(v) != "LIEN MON":
            continue
        for a in v:
            for b in v:
                if a is b or a["subject"] == b["subject"]:
                    continue
                if b["id"] not in a["related"]:
                    a["related"].append(b["id"])
                    added += 1
    print(f"Thêm {added} liên kết related liên môn.")
    if dry:
        print("--dry-run: không ghi file.")
        return 0
    save(docs)
    print("Đã ghi lại kho.")
    return 0


def main() -> int:
    args = sys.argv[1:]
    dry = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    docs = load()

    if not args or args[0] == "--report":
        cmd_report(docs)
        return 0
    if args[0] == "--merge":
        return cmd_merge(docs, args[1:], dry)
    if args[0] == "--link":
        return cmd_link(docs, dry)
    print(__doc__)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
