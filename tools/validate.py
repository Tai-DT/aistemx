#!/usr/bin/env python3
"""Kiểm định kho công thức AISTEM.

Chạy:  python3 tools/validate.py [--strict]

Kiểm tra:
  1. JSON hợp lệ, đúng cấu trúc {meta, formulas}
  2. Đủ khoá bắt buộc, đúng kiểu, đúng enum
  3. id đúng định dạng và duy nhất trên TOÀN BỘ kho
  4. meta.count khớp số bản ghi thực tế
  5. related trỏ tới id có thật
  6. LaTeX: cân bằng ngoặc, không bọc $, không có backslash mồ côi
  7. Ký hiệu khai báo trong units phải có trong vars
  8. grades nhất quán với level

Thoát mã 1 nếu có lỗi (ERROR). --strict coi cảnh báo (WARN) cũng là lỗi.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "formulas"

SUBJECTS = {"math", "physics", "chemistry", "biology"}
LEVELS = {"tieu-hoc", "thcs", "thpt", "dai-hoc"}
LEVEL_GRADES = {
    "tieu-hoc": set(range(1, 6)),
    "thcs": set(range(6, 10)),
    "thpt": set(range(10, 13)),
    "dai-hoc": {13},
}

FORMULA_KEYS = {
    "id", "subject", "level", "grades", "curriculum", "topic", "subtopic",
    "name_vi", "name_en", "latex", "vars", "units",
    "conditions", "note", "tags", "related",
}
OPTIONAL_KEYS = {"sources"}
CURRICULA = {"vn-gdpt-2018", "ap", "ib", "a-level",
             "intl-undergrad", "olympiad", "ru-east-eu"}
META_KEYS = {"file", "subject", "title", "levels", "count"}

ID_RE = re.compile(r"^[a-z0-9]+(\.[a-z0-9-]+){3}$")
TAG_RE = re.compile(r"^[a-z0-9-]+$")

errors: list[str] = []
warnings: list[str] = []


def err(where: str, msg: str) -> None:
    errors.append(f"ERROR {where}: {msg}")


def warn(where: str, msg: str) -> None:
    warnings.append(f"WARN  {where}: {msg}")


LEFT_RE = re.compile(r"\\left(?![a-zA-Z])")
RIGHT_RE = re.compile(r"\\right(?![a-zA-Z])")


def check_latex(where: str, latex: str) -> None:
    s = latex.strip()
    if s.startswith("$") or s.endswith("$"):
        err(where, "latex không được bọc trong dấu $")
    # Chỉ là lỗi khi BỌC cả biểu thức; \\[4pt] giữa \begin{cases} là xuống dòng hợp lệ.
    if s.startswith("\\[") or s.endswith("\\]"):
        err(where, "latex không được bọc trong \\[ \\]")

    # Ngoặc nhọn là ngoặc gom nhóm của LaTeX, bắt buộc cân. Bỏ \{ \} đã escape.
    grouping = s.replace(r"\{", "").replace(r"\}", "")
    if grouping.count("{") != grouping.count("}"):
        err(where, f"latex lệch ngoặc nhọn: {grouping.count('{')} mở / {grouping.count('}')} đóng")

    # \left / \right phải đủ cặp — dùng lookahead để không bắt nhầm
    # \rightarrow, \rightleftharpoons, \leftrightarrow...
    nl, nr = len(LEFT_RE.findall(s)), len(RIGHT_RE.findall(s))
    if nl != nr:
        err(where, rf"latex lệch \left / \right: {nl} / {nr}")
    if s.count(r"\begin") != s.count(r"\end"):
        err(where, r"latex lệch \begin / \end")

    # Ngoặc tròn/vuông KHÔNG bắt buộc cân trong toán học hợp lệ
    # (khoảng nửa mở [a; b), hệ tuyển \left[ ... \right.) nên chỉ cảnh báo
    # khi không có dấu hiệu của các cấu trúc đó.
    if nl == 0 and r"\infty" not in s:
        for op, cl, name in (("(", ")", "ngoặc tròn"), ("[", "]", "ngoặc vuông")):
            if s.count(op) != s.count(cl):
                warn(where, f"latex lệch {name}: {s.count(op)} mở / {s.count(cl)} đóng")


def check_formula(where: str, f: dict, all_ids: set[str]) -> None:
    missing = FORMULA_KEYS - set(f)
    extra = set(f) - FORMULA_KEYS - OPTIONAL_KEYS
    if missing:
        err(where, f"thiếu khoá: {sorted(missing)}")
    if extra:
        err(where, f"khoá lạ: {sorted(extra)}")
    if missing:
        return

    if not ID_RE.match(f["id"]):
        err(where, f"id sai định dạng: {f['id']!r}")
    if f["subject"] not in SUBJECTS:
        err(where, f"subject không hợp lệ: {f['subject']!r}")
    if f["level"] not in LEVELS:
        err(where, f"level không hợp lệ: {f['level']!r}")

    if not isinstance(f["grades"], list) or not f["grades"]:
        err(where, "grades phải là mảng không rỗng")
    else:
        # level = cấp học GIỚI THIỆU công thức; grades được phép trải sang cấp trên
        # (ví dụ quang hợp: dạy lớp 7, ôn lại lớp 11 -> level thcs, grades [7, 11]).
        # Chỉ báo khi không có lớp nào thuộc cấp đã khai báo.
        allowed = LEVEL_GRADES.get(f["level"], set())
        if not any(g in allowed for g in f["grades"]):
            warn(where, f"grades {f['grades']} không có lớp nào thuộc level "
                        f"{f['level']} (cho phép {sorted(allowed)})")

    if not isinstance(f["curriculum"], list) or not f["curriculum"]:
        err(where, "curriculum phải là mảng không rỗng")
    else:
        bad = [c for c in f["curriculum"] if c not in CURRICULA]
        if bad:
            err(where, f"curriculum không hợp lệ: {bad}")

    for key in ("topic", "name_vi", "latex"):
        if not isinstance(f[key], str) or not f[key].strip():
            err(where, f"{key} rỗng")

    check_latex(where, f["latex"])

    if not isinstance(f["vars"], dict):
        err(where, "vars phải là object")
    if not isinstance(f["units"], dict):
        err(where, "units phải là object")
    if isinstance(f["vars"], dict) and isinstance(f["units"], dict):
        orphan = set(f["units"]) - set(f["vars"])
        if orphan:
            warn(where, f"units khai báo ký hiệu không có trong vars: {sorted(orphan)}")

    if not isinstance(f["tags"], list) or not f["tags"]:
        err(where, "tags phải là mảng không rỗng")
    else:
        for t in f["tags"]:
            if not isinstance(t, str) or not TAG_RE.match(t):
                err(where, f"tag sai định dạng: {t!r}")

    if not isinstance(f["related"], list):
        err(where, "related phải là mảng")
    else:
        for r in f["related"]:
            if r == f["id"]:
                warn(where, "related tự trỏ vào chính nó")
            elif r not in all_ids:
                warn(where, f"related trỏ tới id không tồn tại: {r}")


def main() -> int:
    strict = "--strict" in sys.argv

    files = sorted(p for p in DATA.rglob("*.json")
                   if p.name not in {"schema.json", "index.json", "usage.json"})
    if not files:
        print("Không tìm thấy file dữ liệu nào trong", DATA)
        return 1

    docs: list[tuple[Path, dict]] = []
    for path in files:
        rel = path.relative_to(ROOT)
        try:
            docs.append((path, json.loads(path.read_text(encoding="utf-8"))))
        except json.JSONDecodeError as e:
            err(str(rel), f"JSON hỏng: {e}")

    all_ids: set[str] = set()
    id_owner: dict[str, str] = {}
    for path, doc in docs:
        rel = str(path.relative_to(ROOT))
        for f in doc.get("formulas", []):
            fid = f.get("id")
            if not isinstance(fid, str):
                continue
            if fid in all_ids:
                err(rel, f"id TRÙNG với {id_owner[fid]}: {fid}")
            else:
                all_ids.add(fid)
                id_owner[fid] = rel

    per_subject: dict[str, int] = defaultdict(int)
    per_level: dict[str, int] = defaultdict(int)
    total = 0

    for path, doc in docs:
        rel = str(path.relative_to(ROOT))
        if set(doc) != {"meta", "formulas"}:
            err(rel, f"cấp cao nhất phải đúng 2 khoá meta/formulas, đang có {sorted(doc)}")
            continue

        meta = doc["meta"]
        if set(meta) != META_KEYS:
            err(rel, f"meta sai khoá: thiếu {sorted(META_KEYS - set(meta))}, thừa {sorted(set(meta) - META_KEYS)}")
        for lv in meta.get("levels", []):
            if lv not in LEVELS:
                err(rel, f"meta.levels chứa giá trị lạ: {lv!r}")

        formulas = doc["formulas"]
        n = len(formulas)
        total += n
        if meta.get("count") != n:
            err(rel, f"meta.count = {meta.get('count')} nhưng có {n} bản ghi")

        for i, f in enumerate(formulas):
            fid = f.get("id", f"#{i}")
            check_formula(f"{rel}[{fid}]", f, all_ids)
            if f.get("subject") in SUBJECTS:
                per_subject[f["subject"]] += 1
            if f.get("level") in LEVELS:
                per_level[f["level"]] += 1
            # meta.subject = "mixed" dành cho file đa môn (Olympiad, hệ Nga/Đông Âu)
            if meta.get("subject") != "mixed" and f.get("subject") != meta.get("subject"):
                warn(f"{rel}[{fid}]", "subject của bản ghi khác meta.subject")

    for line in warnings:
        print(line)
    for line in errors:
        print(line)

    names = {"math": "Toán", "physics": "Vật lí", "chemistry": "Hoá học", "biology": "Sinh học"}
    lv_names = {"tieu-hoc": "Tiểu học", "thcs": "THCS", "thpt": "THPT", "dai-hoc": "Đại học"}
    print("\n" + "=" * 58)
    print(f"Tổng: {total} công thức trong {len(docs)} file")
    print("- Theo môn:  " + ", ".join(f"{names[k]} {per_subject[k]}" for k in sorted(per_subject)))
    print("- Theo cấp:  " + ", ".join(f"{lv_names[k]} {per_level[k]}" for k in
                                      sorted(per_level, key=lambda x: list(LEVELS).index(x) if x in LEVELS else 9)))
    print(f"- Lỗi: {len(errors)} | Cảnh báo: {len(warnings)}")
    print("=" * 58)

    if errors:
        return 1
    if strict and warnings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
