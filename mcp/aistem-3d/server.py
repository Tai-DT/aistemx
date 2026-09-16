#!/usr/bin/env python3
"""MCP server: aistem-3d — dựng minh hoạ 3D (và 2D SVG) cho công thức AISTEM.

Server phơi ra các tool để tác nhân (Claude Code / ứng dụng) sinh scene 3D khai báo
(định dạng aistem-scene-1) và ảnh SVG 2D từ kho công thức, rồi lưu vào data/scenes3d.

Logic nằm ở phần `core` (thuần Python, test được không cần package `mcp`); FastMCP chỉ
bọc mỏng bên ngoài. Chạy stdio:

    pip install -r requirements.txt
    python server.py

Đăng ký với Claude Code (interactive):
    claude mcp add aistem-3d -- python /Volumes/SecondaryDisk/aistemx/mcp/aistem-3d/server.py
"""

from __future__ import annotations

import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]   # .../AISTEM
sys.path.insert(0, str(ROOT))

from tools.illus import generators2d, scenes3d   # noqa: E402

FORMULA_INDEX = ROOT / "data" / "formulas" / "index.json"
SCENE_DIR = ROOT / "data" / "scenes3d"
VIEWER = ROOT / "viewer" / "index.html"
RASTER_PROMPTS = ROOT / "data" / "illustrations" / "raster" / "prompts.json"

SCENE_DOCS = {
    "coordinate_frame": "Điểm & vectơ vị trí trong hệ Oxyz (toạ độ, khoảng cách).",
    "vector3d": "Một hay nhiều vectơ từ gốc, tuỳ chọn vectơ tổng.",
    "cross_product": "Tích có hướng a×b + hình bình hành diện tích |a×b|.",
    "parallelepiped": "Hình hộp từ 3 vectơ cạnh — tích hỗn tạp / định thức thể tích.",
    "surface": "Mặt z=f(x,y) (bake mesh). params: expr, u=[min,max], v=[min,max], res.",
    "solid_revolution": "Khối tròn xoay y=f(x) quanh Ox. params: expr, domain=[a,b].",
    "sphere_flux": "Mặt Gauss + trường hướng tâm (định luật Gauss / điện trường điểm).",
    "wave_surface": "Mặt sóng phẳng z=A·sin(kx). params: A, k.",
    "atom_bohr": "Mẫu nguyên tử Bohr: hạt nhân + quỹ đạo electron. params: shells.",
    "molecule": "Mô hình bi-que. params: atoms[{at,r,color,label}], bonds[[i,j]].",
}


# --------------------------------------------------------------------------
# core (thuần Python)
# --------------------------------------------------------------------------
def _strip_accents(s: str) -> str:
    s = s.replace("đ", "d").replace("Đ", "D")  # NFD không tách đ/Đ
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


_FORMULAS: list[dict] | None = None


def _load_formulas() -> list[dict]:
    global _FORMULAS
    if _FORMULAS is None:
        _FORMULAS = json.loads(FORMULA_INDEX.read_text(encoding="utf-8"))["formulas"]
    return _FORMULAS


def core_list_scene_types() -> list[dict]:
    return [{"type": t, "description": SCENE_DOCS.get(t, "")} for t in scenes3d.REGISTRY]


def core_list_2d_generators() -> list[str]:
    return list(generators2d.REGISTRY)


def core_get_formula(formula_id: str) -> dict:
    for f in _load_formulas():
        if f["id"] == formula_id:
            return f
    return {"error": f"không tìm thấy công thức: {formula_id}"}


def core_search_formulas(query: str, subject: str = "", limit: int = 15) -> list[dict]:
    q = _strip_accents(query)
    out = []
    for f in _load_formulas():
        if subject and f.get("subject") != subject:
            continue
        hay = _strip_accents(" ".join([f["id"], f.get("name_vi", ""), f.get("name_en", ""),
                                       f.get("topic", ""), f.get("subtopic", "")]))
        if q in hay:
            out.append({"id": f["id"], "name_vi": f.get("name_vi"), "topic": f.get("topic"),
                        "latex": f.get("latex")})
            if len(out) >= limit:
                break
    return out


def core_build_3d_scene(scene_type: str, params: dict | None = None,
                        formula_id: str | None = None) -> dict:
    if scene_type not in scenes3d.REGISTRY:
        return {"error": f"scene không tồn tại: {scene_type}", "available": list(scenes3d.REGISTRY)}
    p = dict(params or {})
    if formula_id:
        p["formula_id"] = formula_id
    scene = scenes3d.render(scene_type, p)
    if formula_id:
        scene["id"] = formula_id
        scene["formula_id"] = formula_id
    problems = scenes3d.validate_scene(scene)
    if problems:
        return {"error": "scene không hợp lệ", "problems": problems}
    return scene


def core_build_2d_svg(generator: str, params: dict | None = None) -> dict:
    if generator not in generators2d.REGISTRY:
        return {"error": f"generator không tồn tại: {generator}", "available": list(generators2d.REGISTRY)}
    return {"svg": generators2d.render(generator, params or {})}


def _load_raster_prompts() -> list[dict]:
    if not RASTER_PROMPTS.exists():
        return []
    return json.loads(RASTER_PROMPTS.read_text(encoding="utf-8")).get("prompts", [])


def core_list_raster_prompts() -> list[dict]:
    return [{"formula_id": p["formula_id"], "subject": p["subject"], "name_vi": p.get("name_vi", "")}
            for p in _load_raster_prompts()]


def core_get_raster_prompt(formula_id: str) -> dict:
    for p in _load_raster_prompts():
        if p["formula_id"] == formula_id:
            return p
    return {"error": f"không có prompt raster cho: {formula_id}",
            "hint": "Thêm ứng viên vào tools/illus/raster.py rồi chạy tools/build_raster_prompts.py"}


def core_save_scene(scene: dict, scene_id: str | None = None) -> dict:
    sid = scene_id or scene.get("id") or scene.get("formula_id")
    if not sid:
        return {"error": "thiếu scene_id / scene.id"}
    problems = scenes3d.validate_scene(scene)
    if problems:
        return {"error": "từ chối lưu scene không hợp lệ", "problems": problems}
    scene["id"] = sid
    SCENE_DIR.mkdir(parents=True, exist_ok=True)
    path = SCENE_DIR / f"{sid}.json"
    path.write_text(json.dumps(scene, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return {
        "saved": str(path.relative_to(ROOT)),
        "viewer": f"file://{VIEWER}?scene={sid}",
        "note": "Thêm formula_id vào data/scenes3d/bindings.json rồi chạy tools/build_scenes.py để cố định.",
    }


# --------------------------------------------------------------------------
# lớp MCP (FastMCP)
# --------------------------------------------------------------------------
def build_server():
    from mcp.server.fastmcp import FastMCP

    mcp = FastMCP("aistem-3d")

    @mcp.tool()
    def list_scene_types() -> list[dict]:
        """Liệt kê các loại scene 3D dựng được, kèm mô tả và tham số chính."""
        return core_list_scene_types()

    @mcp.tool()
    def list_2d_generators() -> list[str]:
        """Liệt kê các generator ảnh SVG 2D."""
        return core_list_2d_generators()

    @mcp.tool()
    def get_formula(formula_id: str) -> dict:
        """Lấy một bản ghi công thức trong kho AISTEM theo id."""
        return core_get_formula(formula_id)

    @mcp.tool()
    def search_formulas(query: str, subject: str = "", limit: int = 15) -> list[dict]:
        """Tìm công thức (không dấu vẫn ra). subject lọc math|physics|chemistry|biology."""
        return core_search_formulas(query, subject, limit)

    @mcp.tool()
    def build_3d_scene(scene_type: str, params: dict | None = None,
                       formula_id: str | None = None) -> dict:
        """Dựng scene 3D (aistem-scene-1) theo scene_type + params; gắn formula_id nếu có.

        Ví dụ scene_type: surface {expr:'x^2-y^2'}, solid_revolution {expr:'sqrt(x)',domain:[0.2,4]},
        cross_product {a:[3,1,0],b:[1,3,0]}, molecule {atoms:[...],bonds:[...]}.
        """
        return core_build_3d_scene(scene_type, params, formula_id)

    @mcp.tool()
    def build_2d_svg(generator: str, params: dict | None = None) -> dict:
        """Sinh ảnh minh hoạ 2D dạng SVG (chuỗi) theo generator + params."""
        return core_build_2d_svg(generator, params)

    @mcp.tool()
    def save_scene(scene: dict, scene_id: str | None = None) -> dict:
        """Lưu scene JSON vào data/scenes3d/<id>.json (đã kiểm định), trả link viewer."""
        return core_save_scene(scene, scene_id)

    @mcp.tool()
    def list_raster_prompts() -> list[dict]:
        """Liệt kê công thức có prompt ảnh raster (loại khó vẽ SVG: con lắc, quang hợp, phân bào…)."""
        return core_list_raster_prompts()

    @mcp.tool()
    def get_raster_prompt(formula_id: str) -> dict:
        """Lấy prompt ảnh raster đầy đủ (prompt, negative, model, kích thước, seed) cho một công thức."""
        return core_get_raster_prompt(formula_id)

    return mcp


def main() -> int:
    try:
        server = build_server()
    except ModuleNotFoundError:
        print("Chưa cài package 'mcp'. Chạy: pip install -r requirements.txt", file=sys.stderr)
        return 1
    server.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
