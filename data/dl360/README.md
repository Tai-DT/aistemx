# DigitalLearning.vn — dataset crawl (2026-10-08)

Nguồn: https://digitallearning.vn (Next.js/Turbopack "Kho học liệu 360").
Data trích từ: (1) React Server Component payload `self.__next_f.push` trong HTML
list page — nơi chứa toàn bộ catalog JSON; (2) SSR HTML trang chi tiết; (3) JS
chunk của client bundle — chứa code + data table + chuỗi UI tiếng Việt của từng
module; (4) capture network (CDP) để map module → chunk.

## Cấu trúc thư mục

| Path | Nội dung |
|---|---|
| `app_library_items.json` | **315 resources** đầy đủ metadata — catalog sau login (`/app/library`) |
| `library_items.json` | 101 resources công khai (subset) |
| `app_library_catalog.csv` / `library_catalog.csv` | Bảng phẳng 315 / 101 dòng |
| `thumbnails/` | 315 ảnh avatar `.webp` |
| `share-images/` | 101 ảnh OG share (chỉ có cho resource public) |
| `pages/` | 315 file SSR HTML trang chi tiết (`/app/resources/<slug>`) — chứa nội dung render đầy đủ |
| `app/` | HTML 8 trang sau login (overview, library, collections, favorites, recent, settings, help, feedback) |
| `subjects/` | 6 trang môn học `/mon-hoc/*` |
| `misc/` | classroom-tools, gioi-thieu |
| `chunks/` | **205 file JS** — toàn bộ client bundle (11MB): base + lazy module chunks |
| `module_data/<slug>/` | Data trích xuất per module: `strings_vi.json` (chuỗi UI tiếng Việt), data tables (vd `ELEMENT_PROPERTIES` 118 nguyên tố), `_sim_source_urls.json` (map module → URL PhET gốc) |
| `module_manifest.json` | Map 75 module → own_chunks + shared_chunks + sim_source_url + data_files |
| `module_runtime_chunks.json` | Kết quả capture CDP: chunk JS mỗi trang module load lúc runtime |
| `user_profile.json` | Tài khoản đã login (role `user`) |
| `cookies.txt` / `cookies.json` | Session `dlp_session` — **sensitive, không commit** |
| `fetch_library.py` | Script crawl lại catalog |
| `detail_*.html`, `login.html` | File mẫu |

## Phát hiện chính

- Public: 101 resources. Sau login: **315** (+214 `isPublic:false` — chỉ member thấy,
  vẫn status `published`). Resource private 404 ở route public nhưng xem được ở `/app/resources/`.
- Members-only: 179 virtual-tour heritage + 35 sim PhET có `provenance.reuseApproved=false`
  (chưa duyệt licensing GPL/PhET → không phát hành lại được).
- Subjects: heritage 239, physics 26, math 18, chemistry 15, biology 10, geography 7.
- Renderer: `external-embed` 240 (iframe → vr360.com.vn, vrmap.danangfantasticity.com…);
  `code-module` 75 (module React/three.js bundle sẵn — đã tải hết code).
- Sim PhET: ~50 module là port tiếng Việt của sim PhET; `_sim_source_urls.json` map
  module → URL upstream phet.colorado.edu. Chuỗi UI tiếng Việt trích ra ở
  `module_data/<slug>/strings_vi.json`.
- Data tables mẫu đã trích: `module_data/periodic-table/` (118 elements, IONS,
  PHASES, CATEGORIES, METRICS — kèm nguồn PubChem per element),
  `module_data/vietnam-natural-atlas/` (HEIGHT_BINS…).
- Tài khoản test: favorites/collections/history rỗng; `/studio` cần role admin.

## Giới hạn

- Nội dung thực của 240 virtual-tour nằm trên host ngoài (vr360.com.vn,
  vrmap.danangfantasticity.com) — chỉ có URL embed, chưa tải panorama.
- 76MB share-images chỉ có cho 101 resource public.
- Cookie `dlp_session` hết hạn theo phiên — crawl lại cần login mới.

## module_data/ — nội dung học tập trích từ JS chunks (đợt 2)

Mỗi `module_data/<slug>/` có thể chứa:
- `strings_vi.json` — toàn bộ chuỗi UI tiếng Việt (75/75 module)
- `i18n.json` — bundle `defineLocalizedResourceContent` đầy đủ: eyebrow/title/description/modes/câu hỏi (14 module)
- `content_objects.json` — object literal nội dung eval được (69 module): mô tả, mốc bài học, bảng dữ liệu nhúng
- `calls.json` — các call dạng `f("vi","en")` song ngữ / milestone calls (23 module; vd unit-circle 186 cặp, cell-division 67 milestones)
- data tables riêng — vd periodic-table: ELEMENT_PROPERTIES (118 nguyên tố), IONS, PHASES, CATEGORIES, METRICS; vietnam-natural-atlas: HEIGHT_BINS...
- `_sim_source_urls.json` — map ~50 module → URL PhET gốc phet.colorado.edu
- `_vi_fact_registry.json` — registry 15 fact-sheet theo topic (hookes-law, natural-selection, gene-expression, balancing-chemical-equations, plinko-probability...)

Trích bằng: `python3 /tmp/extract_i18n.py` + `/tmp/extract_content2.py` (scan balanced literal → eval bằng node; ternary `t?"en":"vi"` eval với t=false lấy bản VI).

## tours/ — virtual-tour data từ host ngoài (đợt 3)

240 resource `external-embed` → `tours/index.json` map slug → thư mục:

- `tours/p2v/` — **65 project Pano2VR** (vr360.com.vn 64 + bandosohonggai.gov.vn): `pano.xml` đầy đủ (node graph, title, lat/lng, description, hotspot links), `tour.json` parsed, `tiles/` = level preview thấp nhất (312px, 6 tile/node — đủ để duyệt tour; không mirror full-res pyramid vì ~100GB+).
- `tours/viewers/` — **44 viewer-app** (vrmap.danangfantasticity.com 37, diachidogialai/diachidohanoi/voduongbinhdinh 7): `rooms.json` (full config 120+ fields, rooms kèm lat/lon/multires), `maps/gallery/presentation/announce/info_box/custom_box.json`, **292 panorama JPG full-size**, thumbs, audio.
- `tours/matterport/` — 27: show.html + meta.json + cover.jpg (3D model proprietary, không rip được).
- `tours/misc/` — webar sky-lab (shell.js + preview), misc html.

Cách lấy: CDP (Chrome DevTools Protocol) capture network của viewer page — API nội bộ `viewer/ajax/get_rooms.php` POST code=<32hex>; pano ở `viewer/panoramas/<panorama_image>`. Pano2VR lấy trực tiếp `pano.xml` + tile template `tiles/nodeN/cf_%c/l_%l/c_%x/tile_%y.webp`. 3DVista (fao-vr360, truong-viet-my) lấy `script_general.js` + `media/`.

Lỗ hổng còn lại: bana-rita-farm (tour trên vrmap không fire ajax — có thể đã unpublish), voduongbinhdinh (static site, đã lưu assets), matterport (proprietary), p2v full-res tiles (theo yêu cầu riêng).

## Git export note

Bản trên repo này chỉ chứa **data dạng text** (~95MB): JSON catalog, CSV, HTML trang, JS chunks, module_data, pano.xml, rooms/tour.json, scripts. **Binary media bị loại khỏi git** (~3.3GB trên máy gốc): thumbnails, share-images, pano JPG full-size, tile webp, media 3DVista, cover.jpg — lấy lại bằng `fetch_library.py` + các script trong `/tmp` (xem phần tours) hoặc liên hệ người crawl.

`cookies.txt`/`cookies.json` không được commit (session secret).
Note: Mapbox public tokens (pk.eyJ...) embedded in upstream pano.xml are redacted to `pk.REDACTED_PUBLIC_TOKEN` — GitHub push-protection rejects them. Originals remain in upstream pano.xml on vr360.com.vn/bandosohonggai.gov.vn.
