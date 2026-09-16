# Tầng minh hoạ — ảnh 2D (SVG) & scene 3D

Hai kho hình gắn vào kho công thức qua `formula_id`, sinh và kiểm định tự động như các
kho nội dung khác. Một tầng cho **ảnh 2D vector (SVG)**, một tầng cho **scene 3D khai báo**
render bằng three.js.

```
data/formulas/  ──formula_id──►  data/illustrations/  (ảnh SVG 2D)
                └──formula_id──►  data/scenes3d/        (scene 3D aistem-scene-1)

tools/illus/                     engine thuần Python, dùng chung
  generators2d.py  · scenes3d.py · matcher.py · mathexpr.py · svgkit.py
mcp/aistem-3d/                   MCP server bọc scenes3d/generators2d
viewer/                          index.html (3D) · gallery.html (2D)
```

## 1 · Ảnh minh hoạ 2D (SVG)

Mỗi minh hoạ là SVG **sinh bằng code, deterministic**, không tham chiếu tài nguyên ngoài,
màu đi qua biến CSS `--ill-*` nên **tự đọc được ở cả nền sáng lẫn tối** (có `@media
(prefers-color-scheme)` nội bộ); ứng dụng vẫn ghi đè biến để đồng bộ theme.

**Nguồn gán hình** (ưu tiên giảm dần):
1. `data/illustrations/bindings.json` — khai báo thủ công (curated).
2. `tools/illus/matcher.py` — auto-matcher rule-based (khớp theo id-slug / chữ ký LaTeX).

**Generator có sẵn** (`tools/illus/generators2d.py`):

| Generator | Minh hoạ | Tham số chính |
|---|---|---|
| `right_triangle` | Tam giác vuông, ô vuông Pytago | `b`, `c`, `pythagoras` |
| `circle` | Đường tròn, bán kính | `R` |
| `rectangle` | Hình chữ nhật | `a`, `b` |
| `triangle` | Tam giác thường + đường cao | `base`, `height`, `apex` |
| `parallelogram` | Hình bình hành + đường cao | `a`, `height`, `skew` |
| `trapezoid` | Hình thang | `a`, `b`, `height` |
| `function_plot` | Đồ thị y = f(x) | `expr`, `xmin`, `xmax`, `label` |
| `projectile` | Quỹ đạo ném xiên | `v0`, `angle`, `g` |
| `vector_add` | Cộng vectơ (hình bình hành) | `ux,uy,vx,vy` |
| `number_line` | Trục số + điểm/khoảng | `min`, `max`, `points[]` |
| `unit_circle` | Đường tròn lượng giác | `angle` |

`function_plot`/`surface`/`solid_revolution` nhận biểu thức chuỗi (`x^2`, `sin(x)`,
`exp(-0.7*x)`…) qua bộ đánh giá an toàn `mathexpr.py` (whitelist AST).

## 2 · Scene 3D (`aistem-scene-1`)

Scene là JSON khai báo: `camera` + `helpers` (trục/lưới) + `objects`. Các hình cong
(mặt z=f(x,y), khối tròn xoay, đường cong) được **bake sẵn thành `mesh`/`line`** trong
Python, nên viewer chỉ dựng một tập object nguyên thuỷ: `vector · line · point · sphere ·
box · plane · mesh · label`. Quy ước trục: toán (x, y, z=f) ↦ thế giới (X=x, **Y=z**, Z=y),
Y là trục lên.

**Loại scene** (`tools/illus/scenes3d.py`): `coordinate_frame`, `vector3d`,
`cross_product`, `parallelepiped`, `surface`, `solid_revolution`, `sphere_flux`,
`wave_surface`, `atom_bohr`, `molecule`. Khai báo gán trong `data/scenes3d/bindings.json`.

## 3 · Công cụ

| Lệnh | Việc |
|---|---|
| `python3 tools/build_illustrations.py` | Sinh SVG + `data/illustrations/index.json` |
| `python3 tools/build_scenes.py` | Sinh scene JSON + `data/scenes3d/index.json` |
| `python3 tools/validate_illustrations.py` | Kiểm định cả hai tầng (id, file, scene hợp khuôn) |

## 4 · Xem hình

Chạy một http-server tại **gốc repo** (viewer fetch dữ liệu tương đối, `file://` bị chặn):

```bash
python3 -m http.server 8000
```

- 3D: `http://localhost:8000/viewer/` — chọn scene, xoay/zoom (OrbitControls), đổi theme,
  hoặc kéo–thả một file scene JSON vào cửa sổ. Mở thẳng một scene: `…/viewer/?scene=<formula_id>`.
- 2D: `http://localhost:8000/viewer/gallery.html` — lưới toàn bộ ảnh, lọc theo generator/từ khoá.

Viewer nạp three.js r160 qua CDN (ESM importmap) — cần mạng khi mở.

## 5 · MCP server 3D

`mcp/aistem-3d/server.py` phơi các tool (`build_3d_scene`, `build_2d_svg`, `search_formulas`,
`get_formula`, `save_scene`…) để tác nhân dựng minh hoạ theo yêu cầu. Xem `mcp/aistem-3d/README.md`.
Engine dùng chung với CLI nên tool và build luôn cho cùng định dạng.

## 6 · Mở rộng

**Thêm generator 2D:** viết `build_<tên>(p) -> str` trong `generators2d.py`, thêm vào
`REGISTRY`. **Thêm loại scene 3D:** viết `build_<tên>(p) -> dict` trong `scenes3d.py`
(dùng helper `vector/line/sphere/grid_mesh/scene`), thêm vào `REGISTRY`.

**Gắn hình cho công thức:** thêm mục vào `bindings.json` tương ứng (`formula_id` +
generator/scene + `params` + `caption_vi`), rồi chạy lại builder + validate. Với các họ
công thức lớn, thêm rule vào `matcher.py` (2D) hoặc `auto_match()` trong `build_scenes.py`
(3D) để tự phủ nhiều id.

## 7 · Ảnh raster (AI) — cho công thức khó vẽ SVG

SVG hợp hình hình học/đồ thị; các công thức có "vật thật" (con lắc, bình điện phân, lá
quang hợp, phân bào, chuỗi xoắn ADN…) thì ảnh AI trực quan hơn. Tầng raster gắn ảnh PNG
vào công thức qua cùng `formula_id`, **độc lập backend sinh ảnh**.

**Đường đi:**

```
tools/illus/raster.py            ứng viên đã tuyển + prompt engineering (style nhất quán, chặn chữ)
   │  python3 tools/build_raster_prompts.py
   ▼
data/illustrations/raster/prompts.json     manifest: prompt, negative, model, kích thước, seed
   │  python3 tools/gen_raster.py --backend <...>
   ▼
data/illustrations/raster/<formula_id>.png + attached.json
   │  python3 tools/build_illustrations.py     (gộp raster vào index)
   ▼
data/illustrations/index.json    bản ghi kind "2d-raster" hoặc "2d-svg+raster"
```

**Sinh ảnh — hai backend** (`tools/gen_raster.py`):

```bash
# 1) Cloudflare Workers AI (ảnh thật) — cần token của bạn, KHÔNG lưu trong repo
export CF_ACCOUNT_ID=xxxx CF_API_TOKEN=yyyy
python3 tools/gen_raster.py --backend cloudflare
python3 tools/build_illustrations.py

# 2) Placeholder (Pillow, offline) — ảnh tạm để chạy thử toàn tuyến
python3 tools/gen_raster.py --backend placeholder
```

Ảnh gắn `status`: `ai` (ảnh thật) hoặc `placeholder` (ảnh tạm, badge "ẢNH TẠM" trong
gallery). Thay ảnh tạm bằng ảnh thật: chạy backend `cloudflare` với `--force` rồi build lại.
Xoá hẳn: xoá PNG trong `raster/`, chạy `gen_raster.py --attach-only` rồi build lại.

**Đổi model / provider:** model đặt trong `raster.py` (`DEFAULT_MODEL`, mặc định
`@cf/black-forest-labs/flux-1-schnell`; đổi sang SDXL/Lightning… tuỳ ý). Muốn dùng provider
khác (DALL·E, Firefly, Stability…) chỉ cần viết thêm một hàm backend trong `gen_raster.py`
theo cùng chữ ký `gen(prompt_record) -> bytes`.

**Tự sinh qua MCP:** server `aistem-3d` phơi `list_raster_prompts()` / `get_raster_prompt(id)`
để tác nhân lấy prompt chuẩn rồi gọi tool tạo ảnh sẵn có trong phiên.

Bản ghi `raster` trong index: `{ "path", "width", "height", "prompt", "model", "status" }`.
Xem `data/illustrations/schema.json`. Ứng viên hiện tại: 11 công thức (Lí, Hoá, Sinh) —
mở rộng bằng cách thêm mục vào `CANDIDATES` trong `raster.py`.
