#!/usr/bin/env python3
"""Chuẩn hoá kho công thức AISTEM sau khi sinh dữ liệu.

Chạy:  python3 tools/normalize.py [--dry-run]

Ba việc:
  1. Tách khoá gộp trong `vars` và `units` ("T_{1}, T_{2}" -> hai khoá riêng),
     chỉ tách dấu phẩy ở mức ngoài cùng để không phá vỡ f(x, y) hay \\frac{a, b}{c}.
     Nhờ vậy mọi ký hiệu đều tra cứu được trực tiếp bằng khoá.
  2. Sửa bản ghi có `level` không chứa bất kỳ lớp nào trong `grades`
     (ví dụ level = thcs nhưng grades = [11]) -> gán lại theo lớp thấp nhất,
     đồng thời viết lại tiền tố `id` và mọi tham chiếu `related` trên TOÀN kho.
  3. Đồng bộ `meta.count` và `meta.levels`.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "formulas"

BANDS = [("tieu-hoc", range(1, 6)), ("thcs", range(6, 10)),
         ("thpt", range(10, 13)), ("dai-hoc", range(13, 14))]
LEVEL_ORDER = [b[0] for b in BANDS]


def band_of(grade: int) -> str | None:
    for name, rng in BANDS:
        if grade in rng:
            return name
    return None


def split_key(key: str) -> list[str]:
    """Tách 'a, b' -> ['a', 'b'], nhưng giữ nguyên 'f(x, y)' và '\\max\\{a, b\\}'."""
    if "," not in key:
        return [key]
    parts, buf, depth = [], [], 0
    i = 0
    while i < len(key):
        c = key[i]
        # bỏ qua ngoặc đã escape \{ \} \( \) \[ \]
        if c == "\\" and i + 1 < len(key) and key[i + 1] in "{}()[]":
            buf.append(key[i:i + 2])
            i += 2
            continue
        if c in "{([":
            depth += 1
        elif c in ")]}":
            depth -= 1
        if c == "," and depth == 0:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(c)
        i += 1
    parts.append("".join(buf))
    out = [p.strip() for p in parts if p.strip()]
    return out or [key]


def expand(mapping: dict) -> tuple[dict, int]:
    out, n = {}, 0
    for k, v in mapping.items():
        keys = split_key(k)
        if len(keys) > 1:
            n += 1
        for sub in keys:
            out.setdefault(sub, v)
    return out, n


import re

# Chỉ số chạy dùng làm chỗ trống: \vec{a}_{i} khớp \vec{a}_{1}, \vec{a}_{2}...
PLACEHOLDER = re.compile(r"_\\\{[ijkn]\\\}")


def family_members(key: str, var_keys: list[str]) -> list[str]:
    """Tìm các ký hiệu con của một khoá 'họ'.

    units thường ghi gọn {"E": "V/m"} để chỉ chung cho E_{ngoai}, E_{trong}, E(\\vec{k})...
    Hàm này trả về mọi khoá trong vars thuộc họ đó, để units thành bản đồ đầy đủ
    tra cứu được theo từng ký hiệu một.
    """
    escaped = re.escape(key)
    pat = PLACEHOLDER.sub(r"_\\{[^}]+\\}", escaped)
    # Khoá có chỉ số chạy (\vec{a}_{i}) khớp trọn vẹn thành viên (\vec{a}_{1}),
    # nên phần đuôi là tuỳ chọn. Khoá không có chỉ số chạy (E) chỉ khớp tiền tố,
    # bắt buộc có chỉ số dưới / mũ / đối số theo sau để khỏi bắt nhầm ký hiệu khác.
    tail = "?" if pat != escaped else ""
    # ký hiệu con có thể nằm sau \sum
    rx = re.compile(rf"^(\\sum\s*)?{pat}(_|\^|\(|\\,){tail}.*$")
    return [v for v in var_keys if rx.match(v)]


def expand_unit_families(f: dict) -> int:
    var_keys = list(f["vars"])
    out, changed = {}, 0
    for k, v in f["units"].items():
        if k in f["vars"]:
            out[k] = v
            continue
        members = family_members(k, var_keys)
        if members:
            for m in members:
                out.setdefault(m, v)
            changed += 1
        else:
            out[k] = v
    f["units"] = out
    return changed


def main() -> int:
    dry = "--dry-run" in sys.argv
    paths = sorted(p for p in DATA.rglob("*.json")
                   if p.name not in {"schema.json", "index.json", "usage.json"})
    docs = {p: json.loads(p.read_text(encoding="utf-8")) for p in paths}

    # --- Bước 1 & 2: tách khoá gộp, phát hiện bản ghi lệch cấp ---
    split_vars = split_units = fam = backfilled = 0
    id_remap: dict[str, str] = {}
    relevel: list[tuple[str, str, str, list[int]]] = []

    for path, doc in docs.items():
        for f in doc["formulas"]:
            f["vars"], a = expand(f["vars"])
            f["units"], b = expand(f["units"])
            split_vars += a
            split_units += b
            fam += expand_unit_families(f)

            # Bản ghi sinh trước khi có trường curriculum đều thuộc chương trình VN
            if not f.get("curriculum"):
                f["curriculum"] = ["vn-gdpt-2018"]
                backfilled += 1

            grades = f.get("grades") or []
            allowed = dict(BANDS).get(f["level"], range(0))
            if grades and not any(g in allowed for g in grades):
                new_level = band_of(min(grades))
                if new_level and new_level != f["level"]:
                    old_id = f["id"]
                    parts = old_id.split(".")
                    parts[1] = new_level
                    new_id = ".".join(parts)
                    relevel.append((old_id, f["level"], new_level, grades))
                    f["level"] = new_level
                    if new_id != old_id:
                        id_remap[old_id] = new_id
                        f["id"] = new_id

    # kiểm tra va chạm id sau khi đổi tên
    all_ids: list[str] = [f["id"] for doc in docs.values() for f in doc["formulas"]]
    dup = {i for i in all_ids if all_ids.count(i) > 1} if len(all_ids) != len(set(all_ids)) else set()
    if dup:
        print("DỪNG: đổi tên id gây trùng lặp:", sorted(dup))
        return 1

    # --- cập nhật mọi tham chiếu related trỏ tới id cũ ---
    rewired = 0
    valid = set(all_ids)
    for doc in docs.values():
        for f in doc["formulas"]:
            new_rel = []
            for r in f.get("related", []):
                if r in id_remap:
                    r = id_remap[r]
                    rewired += 1
                if r in valid and r != f["id"] and r not in new_rel:
                    new_rel.append(r)
            f["related"] = new_rel

    # --- Bước 3: đồng bộ meta ---
    for path, doc in docs.items():
        doc["meta"]["count"] = len(doc["formulas"])
        levels = {f["level"] for f in doc["formulas"]}
        doc["meta"]["levels"] = [lv for lv in LEVEL_ORDER if lv in levels]

    print(f"Tách khoá gộp : {split_vars} trong vars, {split_units} trong units")
    print(f"Khai triển họ : {fam} khoá units gộp theo họ ký hiệu")
    print(f"Backfill      : {backfilled} bản ghi được gán curriculum = [vn-gdpt-2018]")
    print(f"Sửa cấp học   : {len(relevel)} bản ghi, đổi tên {len(id_remap)} id, "
          f"nối lại {rewired} tham chiếu related")
    for old, ol, nl, g in relevel[:12]:
        print(f"  {ol:9s} -> {nl:8s} lớp {g}  {old}")
    if len(relevel) > 12:
        print(f"  ... và {len(relevel) - 12} bản ghi nữa")

    if dry:
        print("\n--dry-run: không ghi file.")
        return 0

    for path, doc in docs.items():
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nĐã ghi lại {len(docs)} file.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
