# MCP server · `aistem-3d`

Server MCP dựng **minh hoạ 3D** (scene JSON `aistem-scene-1`) và **ảnh SVG 2D** cho
công thức trong kho AISTEM. Tác nhân (Claude Code / ứng dụng) gọi tool để sinh, kiểm
định và lưu scene; viewer three.js (`viewer/index.html`) render.

## Cài & chạy

```bash
pip install -r requirements.txt      # cần package `mcp`
python server.py                     # chạy stdio
```

Đăng ký với Claude Code (phiên interactive):

```bash
claude mcp add aistem-3d -- python /Volumes/SecondaryDisk/aistemx/mcp/aistem-3d/server.py
```

Hoặc thêm vào cấu hình MCP:

```json
{
  "mcpServers": {
    "aistem-3d": { "command": "python", "args": ["/Volumes/SecondaryDisk/aistemx/mcp/aistem-3d/server.py"] }
  }
}
```

## Tool

| Tool | Việc |
|---|---|
| `list_scene_types()` | Liệt kê loại scene 3D + mô tả + tham số chính |
| `list_2d_generators()` | Liệt kê generator ảnh SVG 2D |
| `search_formulas(query, subject?, limit?)` | Tìm công thức (không dấu vẫn ra) |
| `get_formula(formula_id)` | Lấy bản ghi công thức theo id |
| `build_3d_scene(scene_type, params?, formula_id?)` | Dựng scene 3D, đã kiểm định |
| `build_2d_svg(generator, params?)` | Sinh ảnh SVG 2D |
| `save_scene(scene, scene_id?)` | Lưu scene vào `data/scenes3d/<id>.json`, trả link viewer |

## Loại scene 3D

`coordinate_frame` · `vector3d` · `cross_product` · `parallelepiped` · `surface` ·
`solid_revolution` · `sphere_flux` · `wave_surface` · `atom_bohr` · `molecule`.

Ví dụ:

```jsonc
build_3d_scene("surface", { "expr": "x^2 - y^2", "u": [-2.2, 2.2], "v": [-2.2, 2.2] },
               "math.dai-hoc.ham-nhieu-bien.phap-tuyen-mat-cong")

build_3d_scene("solid_revolution", { "expr": "sqrt(x)", "domain": [0.2, 4] })

build_3d_scene("molecule", {
  "atoms": [{ "at": [0,0,0], "r": 0.5, "label": "C" }, { "at": [1,1,1], "r": 0.32, "label": "H" }],
  "bonds": [[0, 1]]
})
```

Engine thuần Python nằm ở `tools/illus/scenes3d.py` (dùng lại bởi `tools/build_scenes.py`),
nên tool và CLI luôn sinh ra cùng một định dạng. Không cần `mcp` để chạy CLI hay test engine.
