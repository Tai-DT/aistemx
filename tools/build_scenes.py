#!/usr/bin/env python3
"""Dựng tầng minh hoạ 3D: sinh scene JSON + data/scenes3d/index.json.

Nguồn scene:
  1. data/scenes3d/bindings.json — khai báo thủ công formula_id → scene + params.
  2. auto-matcher nhẹ (một vài họ công thức rõ ràng: tròn xoay, tích có hướng).

Mỗi scene ghi ra data/scenes3d/<id>.json và một bản ghi trong index.json.

    python3 tools/build_scenes.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.illus import scenes3d

FORMULA_INDEX = ROOT / "data" / "formulas" / "index.json"
SCENE_DIR = ROOT / "data" / "scenes3d"
BINDINGS = SCENE_DIR / "bindings.json"
INDEX_OUT = SCENE_DIR / "index.json"


def load_formulas() -> dict[str, dict]:
    data = json.loads(FORMULA_INDEX.read_text(encoding="utf-8"))
    return {f["id"]: f for f in data["formulas"]}


def auto_match(formulas: dict[str, dict]) -> dict[str, tuple[str, dict]]:
    """Vài rule 3D chính xác cao để minh hoạ khả năng nhân rộng (bindings ưu tiên hơn)."""
    out: dict[str, tuple[str, dict]] = {}
    for fid in formulas:
        if fid.endswith("nguyen-ham-tich-phan.the-tich-tron-xoay-ox"):
            out[fid] = ("solid_revolution", {"expr": "sqrt(x)", "domain": [0.15, 4]})
        elif fid.endswith("oxyz-toa-do.tich-co-huong"):
            out[fid] = ("cross_product", {"a": [3, 1, 0], "b": [1, 3, 0]})
    return out


def collect(formulas: dict[str, dict]) -> tuple[list[dict], list[str]]:
    warnings: list[str] = []
    chosen: dict[str, dict] = {}  # formula_id -> {scene, params, source}

    for fid, (stype, params) in auto_match(formulas).items():
        chosen[fid] = {"scene": stype, "params": params, "source": "auto"}

    bindings = json.loads(BINDINGS.read_text(encoding="utf-8")).get("bindings", [])
    for b in bindings:
        fid = b["formula_id"]
        if fid not in formulas:
            warnings.append(f"binding trỏ tới id không có trong kho: {fid}")
            continue
        if b["scene"] not in scenes3d.REGISTRY:
            warnings.append(f"binding dùng scene không tồn tại: {b['scene']} ({fid})")
            continue
        chosen[fid] = {"scene": b["scene"], "params": dict(b.get("params", {})), "source": "binding"}

    records: list[dict] = []
    for fid in sorted(chosen):
        entry = chosen[fid]
        params = dict(entry["params"])
        params["formula_id"] = fid
        try:
            sc = scenes3d.render(entry["scene"], params)
        except Exception as exc:  # noqa: BLE001
            warnings.append(f"lỗi render scene {fid} ({entry['scene']}): {exc}")
            continue
        # gắn danh tính theo formula_id để id scene là duy nhất
        sc["id"] = fid
        sc["formula_id"] = fid
        problems = scenes3d.validate_scene(sc)
        if problems:
            warnings.append(f"scene {fid} không hợp lệ: {problems}")
            continue
        records.append({
            "id": fid, "formula_id": fid, "scene": entry["scene"],
            "source": entry["source"], "title_vi": sc.get("title_vi", ""),
            "caption_vi": sc.get("caption_vi", ""), "object_count": len(sc["objects"]),
            "scene_dict": sc,
        })
    return records, warnings


def write_scenes(records: list[dict]) -> list[str]:
    warnings: list[str] = []
    SCENE_DIR.mkdir(parents=True, exist_ok=True)
    keep: set[str] = set()
    for rec in records:
        fname = f"{rec['id']}.json"
        (SCENE_DIR / fname).write_text(
            json.dumps(rec["scene_dict"], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        rec["path"] = fname
        keep.add(fname)
    reserved = {"index.json", "schema.json", "bindings.json"}
    for old in SCENE_DIR.glob("*.json"):
        if old.name not in keep and old.name not in reserved:
            old.unlink()
            warnings.append(f"đã xoá scene mồ côi: {old.name}")
    return warnings


def build_index(records: list[dict]) -> dict:
    from collections import Counter
    scenes = [{k: r[k] for k in ("id", "formula_id", "scene", "source", "title_vi",
                                 "caption_vi", "object_count", "path")} for r in records]
    return {
        "meta": {
            "count": len(records),
            "generated_by": "tools/build_scenes.py",
            "scene_format": scenes3d.VERSION,
            "by_scene": dict(sorted(Counter(r["scene"] for r in records).items())),
            "by_source": dict(sorted(Counter(r["source"] for r in records).items())),
            "by_subject": dict(sorted(Counter(r["id"].split(".")[0] for r in records).items())),
        },
        "scenes": scenes,
    }


def main() -> int:
    formulas = load_formulas()
    records, warns = collect(formulas)
    warns += write_scenes(records)
    index = build_index(records)
    INDEX_OUT.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    m = index["meta"]
    print(f"Đã dựng {m['count']} scene 3D -> {INDEX_OUT.relative_to(ROOT)}")
    print("  theo loại scene:", ", ".join(f"{k}={v}" for k, v in m["by_scene"].items()))
    print("  theo nguồn     :", ", ".join(f"{k}={v}" for k, v in m["by_source"].items()))
    print("  theo môn       :", ", ".join(f"{k}={v}" for k, v in m["by_subject"].items()))
    if warns:
        print(f"\n⚠ {len(warns)} cảnh báo:")
        for w in warns:
            print("  -", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
