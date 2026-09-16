#!/usr/bin/env python3
"""Kiểm định tầng minh hoạ (2D SVG + 3D scene).

Kiểm tra tính toàn vẹn giữa index, file sinh ra và kho công thức gốc:
  - mọi formula_id đều tồn tại trong data/formulas
  - mọi generator/scene-type đều có trong registry
  - mọi file svg / scene json đều tồn tại, parse được, không mồ côi
  - scene 3D hợp khuôn aistem-scene-1

Thoát mã 1 nếu có lỗi (dùng được trong CI). Chạy:

    python3 tools/validate_illustrations.py
"""

from __future__ import annotations

import json
import sys
import xml.dom.minidom as minidom
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.illus.registry import all_generators
from tools.illus import scenes3d

FORMULA_INDEX = ROOT / "data" / "formulas" / "index.json"
ILL_DIR = ROOT / "data" / "illustrations"
SCENE_DIR = ROOT / "data" / "scenes3d"


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warns: list[str] = []
        self.checked = 0

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)


def formula_ids() -> set[str]:
    data = json.loads(FORMULA_INDEX.read_text(encoding="utf-8"))
    return {f["id"] for f in data["formulas"]}


def validate_2d(rep: Report, ids: set[str]) -> None:
    index_path = ILL_DIR / "index.json"
    if not index_path.exists():
        rep.warn("chưa có data/illustrations/index.json (bỏ qua 2D)")
        return
    index = json.loads(index_path.read_text(encoding="utf-8"))
    seen_svg: set[str] = set()
    seen_raster: set[str] = set()
    generators = all_generators()
    for rec in index.get("illustrations", []):
        rep.checked += 1
        fid = rec.get("formula_id", "?")
        if fid not in ids:
            rep.err(f"[2D] formula_id không có trong kho: {fid}")
        # mỗi bản ghi phải có ít nhất SVG hoặc raster
        if not rec.get("svg_path") and not rec.get("raster"):
            rep.err(f"[2D] bản ghi không có SVG lẫn raster: {fid}")
        # nhánh SVG
        sp = rec.get("svg_path")
        if sp:
            if rec.get("generator") not in generators:
                rep.err(f"[2D] generator lạ: {rec.get('generator')} ({fid})")
            svg_file = ILL_DIR / sp
            seen_svg.add(svg_file.name)
            if not svg_file.exists():
                rep.err(f"[2D] file SVG không tồn tại: {sp}")
            else:
                try:
                    minidom.parseString(svg_file.read_text(encoding="utf-8"))
                except Exception as exc:  # noqa: BLE001
                    rep.err(f"[2D] SVG hỏng {sp}: {exc}")
        # nhánh raster
        rast = rec.get("raster")
        if rast:
            rp = rast.get("path")
            if not rp:
                rep.err(f"[2D] raster thiếu path: {fid}")
            else:
                rf = ILL_DIR / rp
                seen_raster.add(rf.name)
                if not rf.exists():
                    rep.err(f"[2D] file raster không tồn tại: {rp}")
                elif rf.stat().st_size == 0:
                    rep.err(f"[2D] file raster rỗng: {rp}")
    # SVG mồ côi
    svg_dir = ILL_DIR / "svg"
    if svg_dir.exists():
        for f in svg_dir.glob("*.svg"):
            if f.name not in seen_svg:
                rep.warn(f"[2D] SVG mồ côi (không có trong index): {f.name}")
    # raster mồ côi
    raster_dir = ILL_DIR / "raster"
    if raster_dir.exists():
        for f in raster_dir.glob("*.png"):
            if f.name not in seen_raster:
                rep.warn(f"[2D] raster mồ côi (không có trong index): {f.name}")


def validate_3d(rep: Report, ids: set[str]) -> None:
    index_path = SCENE_DIR / "index.json"
    if not index_path.exists():
        rep.warn("chưa có data/scenes3d/index.json (bỏ qua 3D)")
        return
    index = json.loads(index_path.read_text(encoding="utf-8"))
    seen: set[str] = set()
    for rec in index.get("scenes", []):
        rep.checked += 1
        sid = rec.get("id", "?")
        fid = rec.get("formula_id")
        if fid and fid not in ids:
            rep.err(f"[3D] formula_id không có trong kho: {fid} (scene {sid})")
        path = rec.get("path")
        if not path:
            rep.err(f"[3D] thiếu path: {sid}")
            continue
        scene_file = SCENE_DIR / path
        seen.add(scene_file.name)
        if not scene_file.exists():
            rep.err(f"[3D] file scene không tồn tại: {path}")
            continue
        try:
            scene = json.loads(scene_file.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            rep.err(f"[3D] scene JSON hỏng {path}: {exc}")
            continue
        for problem in scenes3d.validate_scene(scene):
            rep.err(f"[3D] {sid}: {problem}")
    for f in SCENE_DIR.glob("*.json"):
        if f.name in {"index.json", "schema.json", "bindings.json"}:
            continue
        if f.name not in seen:
            rep.warn(f"[3D] scene mồ côi (không có trong index): {f.name}")


def main() -> int:
    rep = Report()
    ids = formula_ids()
    validate_2d(rep, ids)
    validate_3d(rep, ids)

    print(f"Đã kiểm {rep.checked} bản ghi minh hoạ.")
    if rep.warns:
        print(f"\n⚠ {len(rep.warns)} cảnh báo:")
        for w in rep.warns:
            print("  -", w)
    if rep.errors:
        print(f"\n✖ {len(rep.errors)} LỖI:")
        for e in rep.errors:
            print("  -", e)
        return 1
    print("✓ Sạch lỗi.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
