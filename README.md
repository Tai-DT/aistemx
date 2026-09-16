# AISTEM — Kho dữ liệu Toán · Lí · Hoá · Sinh

Cơ sở dữ liệu giáo dục có cấu trúc, phủ từ **lớp 1 đến lớp 12 và bậc đại học**, bám
Chương trình GDPT 2018 của Việt Nam và mở rộng sang các hệ quốc tế (AP, IB, A-Level,
đại cương quốc tế, Olympiad, hệ Nga/Đông Âu). Thiết kế để nạp trực tiếp vào ứng dụng:
mọi bản ghi đều máy đọc được và nối với nhau qua `id`.

**Bốn kho, tổng 10 682 bản ghi** — kiểm định sạch 0 lỗi:

| Kho | Số lượng | Thư mục |
|---|---:|---|
| Công thức | **5 272** | `data/formulas/` |
| Bài học / lý thuyết | **1 018** | `data/lessons/` |
| Bài tập có lời giải | **4 351** (phần lớn chấm tự động được) | `data/problems/` |
| Hồ sơ đề thi chuẩn hoá | **41** | `data/exams/` |

Độ phủ nội dung (từ `data/formulas/usage.json`): **100%** công thức có bài tập, **100%**
có bài học, **100%** có đầy đủ mọi loại nội dung. Bài học phủ đủ TH · THCS · THPT (VN
GDPT 2018) và cấp 3 + đại học quốc tế; bài tập phủ toàn bộ 5 272 công thức.

Sơ đồ nối bốn kho: xem [ARCHITECTURE.md](ARCHITECTURE.md). Phần dưới mô tả kho công thức;
các kho khác dùng cùng bốn trục phân loại (`subject`, `level`, `grades`, `curriculum`).

---

## Kho công thức

**5 272 công thức**, `tools/validate.py` sạch 0 lỗi / 0 cảnh báo.

| Môn | Tiểu học | THCS | THPT | Đại học | Tổng |
|---|---:|---:|---:|---:|---:|
| Toán học | 146 | 276 | 1 080 | 1 012 | **2 514** |
| Vật lí | – | 154 | 748 | 510 | **1 412** |
| Hoá học | – | 31 | 418 | 377 | **826** |
| Sinh học | – | 15 | 297 | 208 | **520** |
| **Tổng** | **146** | **476** | **2 543** | **2 107** | **5 272** |

Theo hệ chương trình (một công thức có thể thuộc nhiều hệ):

| Hệ | Số công thức |
|---|---:|
| `vn-gdpt-2018` — Chương trình GDPT 2018 Việt Nam | 3 305 |
| `intl-undergrad` — Giáo trình đại cương đại học quốc tế | 961 |
| `a-level` — Cambridge / Edexcel A-Level | 577 |
| `ib` — International Baccalaureate Diploma | 513 |
| `ap` — Advanced Placement (College Board) | 484 |
| `olympiad` — IMO, IPhO, IChO, IBO | 289 |
| `ru-east-eu` — Hệ giáo trình Nga và Đông Âu | 129 |

Ghi chú: `level` là cấp học **giới thiệu** công thức, còn `grades` có thể trải sang cấp
trên (ví dụ phương trình quang hợp: `level = thcs`, `grades = [7, 11]`). Vì vậy tổng theo
cấp và tổng theo lớp không trùng nhau. Lớp 1-2 rất ít công thức vì chương trình ở giai đoạn
này gần như chưa có công thức dạng ký hiệu.

## Cấu trúc thư mục

```
data/formulas/
  schema.json                 JSON Schema mô tả định dạng bản ghi
  index.json                  Toàn bộ công thức gộp lại + thống kê + cây chủ đề  (sinh tự động)
  corpus.jsonl                Mỗi dòng một công thức, kèm trường tìm kiếm phẳng  (sinh tự động)
  math/
    01-tieu-hoc.json                    Toán lớp 1-5
    02-thcs.json                        Toán lớp 6-9 (số học, đại số, hình học)
    03-thpt-dai-so-giai-tich.json       Toán 10-12: đại số, lượng giác, thống kê - xác suất, giải tích
    04-thpt-hinh-hoc.json               Toán 10-12: hệ thức lượng, vectơ, hình phẳng, hình không gian, toạ độ
    05-dai-hoc-giai-tich.json           Giải tích 1-2-3, chuỗi, phương trình vi phân
    06-dai-hoc-dai-so-xac-suat.json     Đại số tuyến tính, xác suất - thống kê, toán rời rạc
  physics/
    01-thcs.json                        Vật lí lớp 6-9
    02-thpt-co-nhiet.json               Động học, động lực học, bảo toàn, chất khí, nhiệt động lực học
    03-thpt-dien-tu-song-hien-dai.json  Điện - từ, dao động, sóng, điện xoay chiều, quang, lượng tử, hạt nhân
    04-dai-hoc.json                     Vật lí đại cương: cơ, nhiệt, điện từ, quang, lượng tử, chất rắn
  chemistry/
    01-thcs-dai-cuong.json              Đại lượng cơ bản, cấu tạo nguyên tử, dung dịch, tốc độ - cân bằng, điện li, nhiệt hoá
    02-thpt-vo-co-huu-co.json           Hoá vô cơ, hoá hữu cơ và các công thức giải nhanh
    03-dai-hoc.json                     Nhiệt động, động hoá học, điện hoá, phân tích, cấu tạo chất, hoá keo
  biology/
    01-thcs-thpt.json                   Tế bào, chuyển hoá, di truyền, tiến hoá, sinh thái, sinh lí người
    02-dai-hoc.json                     Hoá sinh, sinh học phân tử, sinh lí học, di truyền quần thể, sinh thái định lượng, tin sinh

docs/formulas/<mon>.md        Bản Markdown cho người đọc                        (sinh tự động)
tools/validate.py             Kiểm định dữ liệu
tools/normalize.py            Chuẩn hoá: tách khoá gộp trong vars/units, đồng bộ level và meta
tools/build_index.py          Dựng index.json, corpus.jsonl và bản Markdown
tools/query.py                Tra cứu từ dòng lệnh
```

## Định dạng một bản ghi

```json
{
  "id": "math.thpt.dao-ham.dao-ham-cua-tich",
  "subject": "math",
  "level": "thpt",
  "grades": [11, 12],
  "topic": "Đạo hàm",
  "subtopic": "Quy tắc tính đạo hàm",
  "name_vi": "Đạo hàm của một tích",
  "name_en": "Product rule",
  "latex": "(uv)' = u'v + uv'",
  "vars": { "u": "hàm số khả vi theo x", "v": "hàm số khả vi theo x" },
  "units": {},
  "conditions": "u, v khả vi tại x",
  "note": "Mở rộng: (uvw)' = u'vw + uv'w + uvw'",
  "tags": ["giai-tich", "dao-ham"],
  "related": ["math.thpt.dao-ham.dao-ham-cua-thuong"]
}
```

Quy ước quan trọng:

| Trường | Ý nghĩa |
|---|---|
| `id` | `<subject>.<level>.<topic-slug>.<name-slug>`, chữ thường không dấu, **duy nhất toàn kho** |
| `subject` | `math` \| `physics` \| `chemistry` \| `biology` |
| `level` | `tieu-hoc` (1-5) \| `thcs` (6-9) \| `thpt` (10-12) \| `dai-hoc` |
| `grades` | mảng lớp áp dụng; `13` nghĩa là bậc đại học |
| `latex` | LaTeX **thuần**, không bọc `$` hay `\[ \]` — phía hiển thị tự chọn cách bao |
| `vars` | giải thích **mọi** ký hiệu xuất hiện trong `latex` |
| `units` | đơn vị SI dạng ASCII (`m/s^2`, `J`, `mol/L`); `{}` nếu không thứ nguyên |
| `conditions` | điều kiện áp dụng / miền xác định |
| `related` | id các công thức liên quan, dùng để dựng đồ thị tri thức |

## Sử dụng

Dựng chỉ mục và các bản xuất (chạy lại mỗi khi sửa dữ liệu):

```bash
python3 tools/build_index.py
```

Kiểm định toàn bộ kho (JSON hợp lệ, id trùng, LaTeX cân ngoặc, `related` treo, đơn vị lệch):

```bash
python3 tools/validate.py
```

Tra cứu nhanh — tìm không dấu vẫn ra kết quả có dấu:

```bash
python3 tools/query.py "dao ham" --subject math
```

```bash
python3 tools/query.py --grade 12 --topic "Tích phân" --format latex
```

```bash
python3 tools/query.py --stats
```

## Nạp vào ứng dụng

`index.json` giữ toàn bộ kho trong một object, kèm `stats` và `topic_tree` để dựng menu
duyệt theo môn → cấp → chủ đề.

```python
import json
kho = json.load(open("data/formulas/index.json", encoding="utf-8"))
ct = {f["id"]: f for f in kho["formulas"]}
print(ct["math.thpt.dao-ham.dao-ham-cua-tich"]["latex"])
```

`corpus.jsonl` dành cho pipeline RAG / vector DB: mỗi dòng một công thức, có sẵn trường
`search` gộp tên + chủ đề + thẻ + mô tả biến ở cả dạng có dấu và không dấu, nên nhúng
embedding hay đánh chỉ mục BM25 đều dùng được ngay.

```python
import json
with open("data/formulas/corpus.jsonl", encoding="utf-8") as fh:
    docs = [json.loads(line) for line in fh]
```

## Minh hoạ (ảnh 2D & 3D)

Ngoài công thức, kho có hai tầng hình gắn qua `formula_id`:

- **Ảnh 2D (SVG)** — `data/illustrations/`, sinh bằng code deterministic (tam giác vuông,
  đường tròn, đồ thị hàm, ném xiên, vectơ, trục số, đường tròn lượng giác…). Tự đọc được
  cả nền sáng lẫn tối.
- **Ảnh raster (AI)** — cho công thức khó vẽ SVG (con lắc, quang hợp, phân bào, điện phân…):
  sinh bằng model text-to-image (Cloudflare Workers AI qua REST, hoặc placeholder offline),
  gắn vào công thức qua trường `raster`.
- **Scene 3D** (`data/scenes3d/`, định dạng `aistem-scene-1`) — mặt z=f(x,y), khối tròn
  xoay, tích có hướng, hình hộp, mặt Gauss, mẫu Bohr, phân tử… render bằng three.js.

```bash
python3 tools/build_illustrations.py    # sinh SVG 2D + gộp raster
python3 tools/build_scenes.py           # sinh scene 3D
python3 tools/build_raster_prompts.py   # manifest prompt ảnh raster
python3 tools/gen_raster.py --backend cloudflare   # sinh ảnh AI (cần CF_ACCOUNT_ID/CF_API_TOKEN)
python3 tools/validate_illustrations.py # kiểm định
python3 -m http.server 8000             # rồi mở http://localhost:8000/viewer/ và /gallery.html
```

MCP server `mcp/aistem-3d/` cho phép tác nhân dựng minh hoạ theo yêu cầu. Chi tiết:
[docs/illustrations.md](docs/illustrations.md).

## Mở rộng kho

1. Thêm bản ghi vào đúng file lát cắt trong `data/formulas/<mon>/`, giữ nguyên định dạng.
2. Chạy `python3 tools/normalize.py` — tự đồng bộ `meta.count`, `meta.levels` và tách
   các khoá gộp kiểu `"T_{1}, T_{2}"` thành từng ký hiệu riêng.
3. Chạy `python3 tools/validate.py` — phải sạch lỗi.
4. Chạy `python3 tools/build_index.py` để dựng lại `index.json`, `corpus.jsonl` và Markdown.

Thêm một lát cắt mới thì chỉ cần tạo file `.json` mới trong thư mục môn tương ứng; hai
công cụ trên tự quét đệ quy, không cần khai báo ở đâu khác.

Thêm một lát cắt mới thì chỉ cần tạo file `.json` mới trong thư mục môn tương ứng; hai
công cụ trên tự quét đệ quy, không cần khai báo ở đâu khác.

---

## Ba kho nội dung: Bài học · Bài tập · Đề thi

Ba kho này tập trung ở **cấp 3 và đại học theo chương trình quốc tế** (AP, IB, A-Level,
đại cương quốc tế, Olympiad). Mỗi kho có `schema.json` riêng và nối về kho công thức
qua `id`. Chi tiết kiến trúc: [ARCHITECTURE.md](ARCHITECTURE.md).

**Bài học** (`data/lessons/`) — 676 bài, ≈622 giờ giảng. Mỗi bài là một bài giảng hoàn
chỉnh: mục tiêu học tập, khái niệm song ngữ, thân bài Markdown, ví dụ có lời giải, lỗi
thường gặp. Trường `formulas[]` trỏ tới công thức, `prerequisites[]` dựng lộ trình học.
Phân bố: Toán 270 · Vật lí 164 · Hoá 123 · Sinh 119; theo hệ `intl-undergrad` 285 ·
`a-level` 280 · `ap` 265 · `ib` 259 · `olympiad` 61.

**Bài tập** (`data/problems/`) — 947 bài, 874 chấm tự động được (92%). Mỗi bài có lời
giải từng bước (giải thích *tại sao*, không chỉ biến đổi), `answer_numeric` + `tolerance`
để chấm máy, phương án nhiễu kèm `why_wrong`, gợi ý mở dần, gắn `difficulty` 1–5 và
`skills` để chẩn đoán lỗ hổng. Toàn bộ đáp số đã được tính lại độc lập bằng Python ở
chặng kiểm định. Phân bố dạng: điền số 527 · tự luận 206 · trắc nghiệm 194 · khác 20.

**Đề thi** (`data/exams/`) — 36 hồ sơ kỳ thi: AP 9, IB 10, A-Level 6, chuẩn hoá tuyển
sinh (SAT/ACT/GRE/MCAT) 6, Olympiad (IMO/IPhO/IChO/IBO/APhO) 5. Mỗi hồ sơ mô tả cấu
trúc đề, trọng số chủ đề, công thức được cấp sẵn vs phải thuộc, thang điểm, chiến thuật,
bẫy. Số liệu cấu trúc đề đã đối chiếu nguồn chính thức và ghi rõ mốc hiệu lực khi kỳ thi
đổi khung (ví dụ IB Sciences 2025, khung Toán IB 2029, Digital SAT 2024).

Công cụ cho ba kho:

```bash
python3 tools/validate_content.py      # kiểm định + đối chiếu chéo id công thức
python3 tools/build_content_index.py   # dựng index.json 3 kho + đồ thị ngược usage.json
```

`data/formulas/usage.json` là **đồ thị ngược**: với mỗi công thức, biết bài học và bài
tập nào dùng nó — để hệ thống gợi đúng bài giảng/bài luyện khi người học vấp một công thức.
Hiện 3 455 công thức đã có nội dung gắn kèm.

## Giới hạn cần biết

- Kho công thức tập trung vào **hệ thức định lượng**; nội dung định tính (khái niệm, cơ
  chế, phương trình phản ứng cụ thể) nằm trong kho bài học chứ không trong kho công thức.
- Phần đại học bám giáo trình đại cương dùng chung cho khối kỹ thuật và khoa học tự
  nhiên, không đi vào chuyên ngành hẹp.
- Đề bài trong kho bài tập và ví dụ đề trong hồ sơ kỳ thi đều **tự soạn** theo dạng và
  mức độ của từng chương trình, không sao chép đề thi thật có bản quyền.
- Dữ liệu do mô hình sinh và đã qua một vòng kiểm định tự động (tính lại đáp số bằng
  Python, đối chiếu nguồn chính thức cho hằng số và cấu trúc đề). Trước khi dùng cho dạy
  học chính thức, nên rà soát lại theo môn với giáo viên bộ môn. Riêng số liệu cấu trúc
  đề thi thay đổi theo năm — cần kiểm tra lại với nguồn chính thức trước mỗi mùa thi.
