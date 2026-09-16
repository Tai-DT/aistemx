#!/usr/bin/env python3
"""Dựng manifest prompt cho ảnh raster: data/illustrations/raster/prompts.json.

Đọc danh sách ứng viên trong tools/illus/raster.py, đối chiếu với kho công thức, sinh
prompt chuẩn cho từng công thức. Manifest này là đầu vào của tools/gen_raster.py.

    python3 tools/build_raster_prompts.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.illus import raster

FORMULA_INDEX = ROOT / "data" / "formulas" / "index.json"
OUT_DIR = ROOT / "data" / "illustrations" / "raster"
OUT = OUT_DIR / "prompts.json"


def main() -> int:
    formulas = {f["id"]: f for f in json.loads(FORMULA_INDEX.read_text(encoding="utf-8"))["formulas"]}
    prompts, warns = [], []
    for cand in raster.CANDIDATES:
        f = formulas.get(cand["id"])
        if not f:
            warns.append(f"ứng viên không có trong kho: {cand['id']}")
            continue
        prompts.append(raster.build_prompt(cand, f))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {
        "meta": {
            "count": len(prompts),
            "generated_by": "tools/build_raster_prompts.py",
            "default_model": raster.DEFAULT_MODEL,
            "style": raster.STYLE,
            "negative_prompt": raster.NEGATIVE,
            "note": "Đầu vào cho tools/gen_raster.py. Ảnh sinh ra lưu ở raster/<formula_id>.png.",
        },
        "prompts": prompts,
    }
    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã dựng {len(prompts)} prompt -> {OUT.relative_to(ROOT)}")
    for p in prompts:
        print(f"  {p['subject']:9s} {p['formula_id']}")
    if warns:
        print(f"\n⚠ {len(warns)} cảnh báo:")
        for w in warns:
            print("  -", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
