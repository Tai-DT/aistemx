#!/usr/bin/env python3
"""Dựng tầng minh hoạ 2D: sinh SVG + data/illustrations/index.json.

Nguồn minh hoạ (ưu tiên giảm dần):
  1. data/illustrations/bindings.json  — khai báo thủ công (curated).
  2. tools/illus/matcher.py            — tự gán theo id-slug / chữ ký LaTeX.

Mỗi công thức được minh hoạ sinh ra một file svg/<formula_id>.svg và một bản ghi
trong index.json. Chạy lại mỗi khi sửa generator, bindings hoặc kho công thức.

    python3 tools/build_illustrations.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.illus import registry as illus_registry
from tools.illus.registry import match_formula

FORMULA_INDEX = ROOT / "data" / "formulas" / "index.json"
ILL_DIR = ROOT / "data" / "illustrations"
SVG_DIR = ILL_DIR / "svg"
BINDINGS = ILL_DIR / "bindings.json"
INDEX_OUT = ILL_DIR / "index.json"


def load_formulas() -> dict[str, dict]:
    data = json.loads(FORMULA_INDEX.read_text(encoding="utf-8"))
    return {f["id"]: f for f in data["formulas"]}


def _facets(f: dict) -> dict:
    """Các trục lọc chép sẵn vào bản ghi minh hoạ.

    Chép chứ không tra ngược sang kho công thức lúc hiển thị: trình duyệt mở
    `index.json` là xong, không phải tải thêm 5 272 bản ghi công thức chỉ để
    biết một hình thuộc môn nào.
    """
    return {
        "subject": f.get("subject", ""),
        "level": f.get("level", ""),
        "topic": f.get("topic", ""),
        "title": f.get("name_vi", "") or f.get("name", ""),
        "latex": f.get("latex", ""),
    }


def collect(formulas: dict[str, dict]) -> tuple[list[dict], list[str]]:
    """Trả (danh sách bản ghi minh hoạ, danh sách cảnh báo)."""
    warnings: list[str] = []
    records: dict[str, dict] = {}

    # 1) auto-matcher
    for fid, f in formulas.items():
        m = match_formula(f)
        if m:
            gen, params, note = m
            records[fid] = {
                "formula_id": fid, "generator": gen, "params": params,
                "kind": "2d-svg", "source": "auto", "note": note,
                "caption_vi": f.get("note", "") or f.get("name_vi", ""),
                "raster": None,
                **_facets(f),
            }

    # 2) bindings ghi đè
    bindings = json.loads(BINDINGS.read_text(encoding="utf-8")).get("bindings", [])
    for b in bindings:
        fid = b["formula_id"]
        if fid not in formulas:
            warnings.append(f"binding trỏ tới id không có trong kho: {fid}")
            continue
        if b["generator"] not in illus_registry.all_generators():
            warnings.append(f"binding dùng generator không tồn tại: {b['generator']} ({fid})")
            continue
        records[fid] = {
            "formula_id": fid, "generator": b["generator"], "params": b.get("params", {}),
            "kind": "2d-svg", "source": "binding",
            "caption_vi": b.get("caption_vi", ""),
            "raster": None,
            **_facets(formulas[fid]),
        }

    ordered = [records[k] for k in sorted(records)]
    return ordered, warnings


def write_svgs(records: list[dict]) -> list[str]:
    warnings: list[str] = []
    SVG_DIR.mkdir(parents=True, exist_ok=True)
    keep: set[str] = set()
    for rec in records:
        fid = rec["formula_id"]
        try:
            svg = illus_registry.render(rec["generator"], rec.get("params", {}))
        except Exception as exc:  # noqa: BLE001 - báo rồi bỏ qua bản ghi hỏng
            warnings.append(f"lỗi render {fid} ({rec['generator']}): {exc}")
            continue
        fname = f"{fid}.svg"
        (SVG_DIR / fname).write_text(svg, encoding="utf-8")
        rec["svg_path"] = f"svg/{fname}"
        keep.add(fname)
    # dọn SVG mồ côi để thư mục luôn khớp index
    for old in SVG_DIR.glob("*.svg"):
        if old.name not in keep:
            old.unlink()
            warnings.append(f"đã xoá SVG mồ côi: {old.name}")
    return warnings


def build_index(records: list[dict]) -> dict:
    from collections import Counter
    shown = [r for r in records if r.get("svg_path") or r.get("raster")]
    gens = Counter(r["generator"] for r in shown if r.get("generator"))
    src = Counter(r["source"] for r in shown)
    subj = Counter(r.get("subject") or r["formula_id"].split(".")[0] for r in shown)
    lvl = Counter(r.get("level", "") for r in shown if r.get("level"))
    kinds = Counter(r["kind"] for r in shown)
    raster_status = Counter(r["raster"]["status"] for r in shown if r.get("raster") and r["raster"].get("status"))
    return {
        "meta": {
            "count": len(shown),
            "generated_by": "tools/build_illustrations.py",
            "generators": dict(sorted(gens.items())),
            "by_source": dict(sorted(src.items())),
            "by_subject": dict(sorted(subj.items())),
            "by_level": dict(sorted(lvl.items())),
            "by_kind": dict(sorted(kinds.items())),
            "raster": dict(sorted(raster_status.items())),
        },
        "illustrations": shown,
    }


ATTACHED = ILL_DIR / "raster" / "attached.json"


def merge_raster(records: list[dict], formulas: dict[str, dict]) -> list[str]:
    """Gộp raster/attached.json vào records: gắn vào bản ghi SVG sẵn có, hoặc tạo bản ghi chỉ-raster."""
    warnings: list[str] = []
    if not ATTACHED.exists():
        return warnings
    attached = json.loads(ATTACHED.read_text(encoding="utf-8")).get("attached", [])
    by_id = {r["formula_id"]: r for r in records}
    for a in attached:
        fid = a["formula_id"]
        if fid not in formulas:
            warnings.append(f"raster trỏ tới id không có trong kho: {fid}")
            continue
        if not (ILL_DIR / a["path"]).exists():
            warnings.append(f"file raster không tồn tại: {a['path']}")
            continue
        meta = {k: a[k] for k in ("path", "width", "height", "prompt", "model", "status") if k in a}
        if fid in by_id:                       # đã có SVG → gắn thêm raster
            by_id[fid]["raster"] = meta
            by_id[fid]["kind"] = "2d-svg+raster"
        else:                                  # chỉ có raster
            f = formulas[fid]
            records.append({
                "formula_id": fid, "generator": None, "kind": "2d-raster", "source": "raster",
                "caption_vi": f.get("note", "") or f.get("name_vi", ""),
                "raster": meta,
            })
    return warnings


def main() -> int:
    formulas = load_formulas()
    records, warns = collect(formulas)
    warns += write_svgs([r for r in records])
    warns += merge_raster(records, formulas)
    index = build_index(records)
    INDEX_OUT.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    m = index["meta"]
    print(f"Đã dựng {m['count']} minh hoạ 2D -> {INDEX_OUT.relative_to(ROOT)}")
    print("  theo generator:", ", ".join(f"{k}={v}" for k, v in m["generators"].items()))
    print("  theo loại     :", ", ".join(f"{k}={v}" for k, v in m["by_kind"].items()))
    print("  theo nguồn    :", ", ".join(f"{k}={v}" for k, v in m["by_source"].items()))
    print("  theo môn      :", ", ".join(f"{k}={v}" for k, v in m["by_subject"].items()))
    if m["raster"]:
        print("  raster        :", ", ".join(f"{k}={v}" for k, v in m["raster"].items()))
    if warns:
        print(f"\n⚠ {len(warns)} cảnh báo:")
        for w in warns:
            print("  -", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
