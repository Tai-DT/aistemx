# Kiến trúc dữ liệu AISTEM

Bốn kho nội dung nối với nhau qua `id`, cùng một bộ trường phân loại (`subject`,
`level`, `grades`, `curriculum`) để lọc và ghép chéo.

```
                         data/formulas/  (5 272 công thức)
                          id = math.thpt.dao-ham.dao-ham-cua-tich
                                   ▲            ▲            ▲
                 formulas[]        │            │            │  formulas_must_memorize[]
          ┌────────────────────────┘            │            └────────────────────────┐
          │                        formulas_used[]                                     │
   data/lessons/  (676 bài)              │                                      data/exams/
    id = lesson.math.…            data/problems/  (bài tập)                  id = exam.ap-calculus-bc
    prerequisites[] ─┐             id = prob.math.…
        (nội bộ)  ◄──┘
```

`data/formulas/usage.json` là **đồ thị ngược**: với mỗi công thức, liệt kê bài học và bài
tập nào dùng nó. Nhờ đó khi người học vấp một công thức, hệ thống truy ra ngay bài giảng
và bài luyện tương ứng.

## Bốn kho

| Kho | Thư mục | Bản ghi là | Khoá nối |
|---|---|---|---|
| Công thức | `data/formulas/` | một hệ thức có LaTeX, biến, đơn vị, điều kiện | gốc — được các kho khác trỏ tới |
| Bài học | `data/lessons/` | một bài giảng: mục tiêu, khái niệm, thân bài, ví dụ | `formulas[]` → công thức; `prerequisites[]` → bài học |
| Bài tập | `data/problems/` | một câu hỏi có lời giải từng bước, chấm tự động được | `formulas_used[]` → công thức |
| Đề thi | `data/exams/` | hồ sơ một kỳ thi: cấu trúc, trọng số, chiến thuật | `formulas_must_memorize[]` → công thức |

Mỗi thư mục có `schema.json` (JSON Schema) và `index.json` (gộp + thống kê, sinh tự động).

## Hai tầng minh hoạ (gắn qua `formula_id`)

| Tầng | Thư mục | Bản ghi là | Sinh bởi |
|---|---|---|---|
| Ảnh 2D (SVG) | `data/illustrations/` | SVG vector deterministic | `tools/build_illustrations.py` |
| Ảnh raster (AI) | `data/illustrations/raster/` | PNG sinh bằng text-to-image, gắn qua `raster` | `tools/build_raster_prompts.py` → `tools/gen_raster.py` |
| Scene 3D | `data/scenes3d/` | scene khai báo `aistem-scene-1` (render three.js) | `tools/build_scenes.py` |

Engine thuần Python dùng chung ở `tools/illus/` (`generators2d.py`, `scenes3d.py`,
`matcher.py`, `mathexpr.py`, `svgkit.py`). MCP server `mcp/aistem-3d/` bọc engine để tác
nhân dựng minh hoạ theo yêu cầu; viewer ở `viewer/` (`index.html` cho 3D, `gallery.html`
cho 2D). Chi tiết: [docs/illustrations.md](docs/illustrations.md).

## Trục phân loại dùng chung

- `subject`: `math` · `physics` · `chemistry` · `biology` (+ `mixed` cho file Olympiad/Nga)
- `level`: `tieu-hoc` · `thcs` · `thpt` · `dai-hoc` — cấp **giới thiệu** nội dung
- `grades`: mảng lớp 1–13 (13 = đại học); được phép trải nhiều cấp
- `curriculum`: `vn-gdpt-2018` · `ap` · `ib` · `a-level` · `intl-undergrad` · `olympiad` · `ru-east-eu`

Bốn trục này có mặt ở cả bốn kho, nên mọi truy vấn "Toán 12 theo AP" hay "Sinh đại học hệ
quốc tế" đều lọc được xuyên kho bằng cùng một bộ điều kiện.

## Công cụ

| Lệnh | Việc |
|---|---|
| `python3 tools/normalize.py` | Chuẩn hoá kho công thức (tách khoá gộp, đồng bộ meta, backfill curriculum) |
| `python3 tools/dedupe.py --report` | Soát trùng lặp; `--merge` gộp, `--link` nối liên môn |
| `python3 tools/validate.py` | Kiểm định kho công thức |
| `python3 tools/validate_content.py` | Kiểm định bài học/bài tập/đề thi + đối chiếu chéo id công thức |
| `python3 tools/build_index.py` | Dựng chỉ mục kho công thức |
| `python3 tools/build_content_index.py` | Dựng chỉ mục 3 kho nội dung + đồ thị ngược `usage.json` |
| `python3 tools/query.py "<từ khoá>"` | Tra cứu công thức (tìm không dấu vẫn ra) |
| `python3 tools/build_illustrations.py` | Sinh ảnh SVG 2D + `data/illustrations/index.json` |
| `python3 tools/build_scenes.py` | Sinh scene 3D + `data/scenes3d/index.json` |
| `python3 tools/validate_illustrations.py` | Kiểm định hai tầng minh hoạ (2D + 3D) |

## Quy trình khi thêm dữ liệu

1. Thêm bản ghi vào đúng kho, giữ định dạng theo `schema.json`.
2. `normalize.py` (chỉ kho công thức) → `validate.py` / `validate_content.py` phải sạch lỗi.
3. `build_index.py` và `build_content_index.py` để dựng lại chỉ mục và đồ thị ngược.

## Nạp vào ứng dụng

- `data/formulas/index.json` — toàn bộ công thức + `topic_tree` để dựng menu duyệt.
- `data/*/corpus.jsonl` và `data/content-corpus.jsonl` — mỗi dòng một bản ghi, có sẵn
  trường `search` (có dấu + không dấu) cho pipeline RAG / vector DB.
- `data/formulas/usage.json` — nối công thức ↔ bài học ↔ bài tập cho tính năng gợi ý.
