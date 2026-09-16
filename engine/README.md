# AISTEM Engine — Hệ thống xử lí bài toán

Lõi xử lí, REST API và CLI dựng trên kho dữ liệu AISTEM (Toán · Lí · Hoá · Sinh).
Nhận một đề bài ở dạng văn bản hoặc ảnh chụp, hệ thống phân loại đề, truy xuất
đúng công thức và bài giảng trong kho, giải từng bước, **rồi tự kiểm chứng lại
lời giải bằng SymPy** trước khi trả về.

```
   đề bài (văn bản / LaTeX / ảnh)
            │
      1. đọc đề          ingest    ảnh → LaTeX bằng Claude vision
            │
      2. phân loại       classify  môn · cấp · chủ đề · độ khó · kỹ năng
            │
      3. truy xuất       retrieve  BM25 + cụm từ + đồ thị liên kết bốn kho
            │
      4. giải            solve     Claude, chỉ được dùng công thức có thật
            │
      5. kiểm chứng      verify    SymPy tính lại đáp số và từng bước
            │
      6. gợi ý           recommend bài giảng và bài luyện vá đúng chỗ vấp
```

Ngoài luồng xử lí từng bài, hệ thống dựng được **lộ trình học** cho cả một mục
tiêu — xem mục dưới.

## Vì sao có bước 5

Mô hình ngôn ngữ viết được lời giải trôi chảy mà sai số học, và đó là kiểu
hỏng người học khó bắt nhất. Nên ở đây mô hình **không phải trọng tài cho chính
nó**: SymPy đọc lại từng bước, tính lại đáp số một cách độc lập, rồi hệ thống
hạ mức tin cậy theo đúng những gì kiểm chứng được.

Kết quả kiểm chứng có ba trạng thái chứ không phải hai — *"chưa kết luận được"*
là câu trả lời hợp lệ và luôn được nói ra, chứ không âm thầm coi là đúng.

Hai chiều kết luận cố ý **bất đối xứng**:

| | nguyên tắc |
|---|---|
| xác nhận | rộng tay — khớp ở bất kỳ bước nào cũng tính |
| kết tội | chặt tay — phải có bằng chứng lỗi số học ở một bước cụ thể |

Lí do: báo oan một lời giải đúng còn tệ hơn bỏ sót, vì nó dạy người dùng bỏ qua
cảnh báo. Đo trên 250 bài tập lấy ngẫu nhiên từ kho (những bài đã được kiểm định
nên đúng là chuẩn để đếm báo động giả):

```
đáp số : 158 xác nhận (63%) · 92 chưa kết luận · 0 bác bỏ
bước   : 444 xác nhận (41,5%) · 599 chưa kết luận · 12 bác bỏ (1,1%)
```

"Chưa kết luận" vẫn chiếm đa số, và phần lớn là hành vi đúng chứ không phải
thiếu sót: bước thế số thì hai vế cố ý khác nhau, bước phát biểu công thức thì
không có gì để đối chiếu, còn lập luận bằng lời thì nằm ngoài tầm một CAS.

Hai con số ấy từng là **29% số bước và 51% số đáp số**. Phần chênh lệch không
đến từ việc nới tay: nó đến từ hàng chục chỗ parser đọc sai mà không ai biết —
xem bảng bẫy bên dưới. Tỉ lệ bác bỏ giảm cùng chiều (1,9% → 1,1%), và một phép
đo riêng (`do-nghiem-kiem-chung`) canh cho việc mở rộng ấy không biến thành xác
nhận khống.

## Chạy thử trong 2 phút

```bash
cd /Volumes/SecondaryDisk/aistemx/engine
uv venv --python 3.13 && uv pip install -e ".[dev]"
```

```bash
./.venv/bin/aistem db build
```

Nạp toàn bộ bốn kho vào một file SQLite (~4 giây). Chưa cần khoá API.

```bash
./.venv/bin/aistem search "dao ham cua tich" --kind formula
```

Gõ không dấu vẫn ra kết quả có dấu.

```bash
./.venv/bin/aistem verify prob.math.ap-calculus.0001
```

Kiểm chứng lại một lời giải có sẵn trong kho bằng CAS — chạy hoàn toàn offline.

```bash
./.venv/bin/aistem grade prob.math.ap-calculus.0001 "B"
```

Chấm một câu trả lời, kèm giải thích vì sao phương án đó sai và nên học lại bài
nào.

## Bật phần giải bài

Ba bước 1, 4 (đọc ảnh và giải) cần khoá Anthropic. Các bước còn lại không.

```bash
cp .env.example .env
```

Điền `AISTEM_ANTHROPIC_API_KEY` rồi:

```bash
./.venv/bin/aistem solve "Tính giới hạn lim x->3 của (x^2-9)/(x^2-5x+6)."
```

```bash
./.venv/bin/aistem solve --image /duong/dan/de-bai.png --heavy
```

Không có khoá thì `solve` vẫn chạy và vẫn trả về phân loại, công thức liên
quan, bài giảng và bài tương tự — chỉ thiếu phần lời giải, kèm cảnh báo rõ ràng.

## Chạy REST API

```bash
./.venv/bin/aistem serve
```

Tài liệu tương tác ở <http://127.0.0.1:8000/docs>, lược đồ máy đọc ở
`/openapi.json` — dùng nó sinh thẳng client TypeScript cho web/mobile sau này,
không phải viết tay tầng gọi API.

Hoặc bằng Docker (ảnh không chứa dữ liệu; kho gắn vào lúc chạy, chỉ-đọc):

```bash
docker compose up --build
```

### Các endpoint

| | |
|---|---|
| `GET /health` · `GET /stats` | trạng thái và thống kê kho |
| `GET /search` | tìm xuyên bốn kho, lọc theo môn/cấp/lớp/hệ/độ khó |
| `GET /{formulas,lessons,problems,exams}/{id}` | lấy một bản ghi |
| `GET /formulas/{id}/usage` | bài học và bài tập nào dùng công thức này |
| `GET /formulas/{id}/illustration` | hình minh hoạ của công thức, kèm SVG nội tuyến |
| `GET /illustrations/{id}.svg` | lấy thẳng file SVG để nhúng vào thẻ `img` |
| `POST /solve` · `POST /solve/image` | giải bài, có kiểm chứng CAS |
| `POST /classify` | phân loại đề, không cần khoá API |
| `POST /grade` | chấm một câu trả lời, có điểm từng phần |
| `POST /diagnose` | chấm cả loạt và chỉ ra lỗ hổng kiến thức |
| `GET /practice` | đề xuất bài luyện theo kỹ năng |
| `POST /roadmap` | dựng lộ trình học tới một mục tiêu |
| `GET /lessons/{id}/prerequisites` | các bài phải học trước, tuỳ chọn đệ quy |
| `GET /learners/{id}/progress` | đã học gì, thạo tới đâu, cần ôn gì |
| `POST /learners/{id}/lessons/{lesson_id}` | đánh dấu đã học xong một bài |
| `GET /learners/{id}/reviews` | kỹ năng tới hạn ôn, kèm bài tập để ôn |
| `GET /learners/{id}/mastery` | mức thạo từng kỹ năng |
| `POST /exams/mock` | sinh đề thi thử theo bản thiết kế |
| `POST /exams/mock/grade` | chấm bài thi thử, phân tích theo chủ đề |
| `GET /learners/{learner}/report` | báo cáo kỹ năng theo lịch sử làm bài |

## Kiến trúc

```
aistem/
  config.py        cấu hình, mọi thứ đặt được qua biến môi trường AISTEM_*
  textnorm.py      bỏ dấu tiếng Việt · gọt LaTeX · rút số
  models.py        kiểu dữ liệu, bám sát schema.json của bốn kho
  llm.py           lớp gọi Claude: buộc JSON đúng lược đồ, có cache đĩa
  embed.py         nhúng vector (tuỳ chọn, mặc định tắt)
  grading.py       chấm bài và chẩn đoán lỗ hổng
  cli.py           giao diện dòng lệnh
  store/
    db.py          lược đồ SQLite
    build.py       nạp bốn kho JSON, dựng FTS5 và đồ thị liên kết
    search.py      truy xuất lai, hợp nhất bằng RRF
  cas/
    parse.py       LaTeX → SymPy, kèm cổng an toàn chống parse hỏng im lặng
    verify.py      kiểm chứng bước giải và đáp số
    env.py         môi trường ký hiệu mang theo dọc lời giải
    funcalls.py    lời gọi hàm chưa định nghĩa → nguyên tử mờ
    chemistry.py   cân bằng phương trình hoá học và khối lượng mol
    dimensions.py  thứ nguyên của đáp số, ba trạng thái
    units.py       kiểm đơn vị bằng Pint
  pipeline/
    ingest.py      đọc đề từ văn bản hoặc ảnh
    classify.py    phân loại
    retrieve.py    gom ngữ cảnh từ kho
    solve.py       điều phối toàn bộ
  roadmap.py       dựng lộ trình học từ đồ thị tiên quyết
  progress.py      tiến độ học và lịch ôn giãn cách
  mock_exam.py     sinh và chấm đề thi thử theo bản thiết kế
  audit.py         đo chất lượng bằng cách chạy ngược lại trên kho
  api/main.py      REST API
```

### Kho minh hoạ

`data/illustrations/` là kho thứ năm, khoá theo `formula_id`: 42 hình (31 SVG do
`tools/illus/` sinh, 11 raster), có `caption_vi`, tự đổi màu theo dark mode và
có `aria-label`. Engine đính chúng vào `/solve` và trả riêng qua hai endpoint ở
trên. Hình mới ở trạng thái `placeholder` bị bỏ qua — hiện một ô trống cho người
học còn tệ hơn không hiện gì.

### Khớp kỹ năng

Trường `skills` là văn bản tự do và mỗi lát cắt được soạn độc lập, nên cùng một
kỹ năng có cả dạng chữ (`"phân tích đa thức thành nhân tử"`) lẫn dạng slug
(`"phan-tich-da-thuc-thanh-nhan-tu"`). So khớp bằng chuỗi nguyên thì hai nửa kho
không bao giờ gợi ý được cho nhau.

Quan sát để sửa: sau khi bỏ dấu, slug và dạng chữ chỉ khác nhau ở dấu gạch nối
thay dấu cách — tách token thì **trùng khít**. Từ đó dựng chỉ mục token, chấm
điểm bằng độ phủ có cân IDF (`"áp dụng công thức"` có mặt khắp nơi nên gần như
không mang thông tin; `"nhiễu xạ"` thì rất đặc trưng).

Đo trên 250 kỹ năng lấy ngẫu nhiên:

```
                     bài luyện gợi ý được    kỹ năng vô dụng   kỹ năng dùng tốt
so chuỗi nguyên           1,10                    95%                1%
so token + IDF            8,85                     5%               93%
```

102/250 kỹ năng nay bắc cầu được giữa kho VN và kho quốc tế.

### Lưu trữ

Toàn bộ kho (hiện 7 424 bản ghi) nằm trong **một file SQLite**. Không cần server DB, không
cần vector DB: kho chỉ đọc là chính, FTS5 lo tìm kiếm toàn văn, và nếu bật
nhúng vector thì 7 nghìn vector nhân ma trận bằng numpy chỉ mất vài mili-giây.

Bộ nạp quét đệ quy `data/<kho>/**/*.json`, bỏ qua các file dẫn xuất
(`index.json`, `corpus.jsonl`, `usage.json`, `schema.json`). **Thêm một lát cắt
mới chỉ cần thả file vào đúng thư mục** rồi chạy lại `aistem db build` — không
phải khai báo ở đâu cả.

### Truy xuất

Ba kênh chạy song song rồi hợp nhất bằng RRF (Reciprocal Rank Fusion):

1. **cụm từ** — bigram của các từ liền nhau. Tiếng Việt là ngôn ngữ đơn âm:
   "đạo hàm", "động năng", "nồng độ" chỉ mang nghĩa khi đi cạnh nhau, tách ra
   thì "hàm", "năng", "độ" khớp với gần như mọi bản ghi. Đây là kênh quyết định
   chất lượng.
2. **BM25 có dấu**
3. **BM25 không dấu** — để gõ "dao ham" vẫn ra "đạo hàm".

Dùng RRF chứ không cộng điểm thô vì BM25 và cosine không cùng thang đo; RRF chỉ
dùng thứ hạng nên không cần hiệu chỉnh tham số.

Riêng khi giải bài còn một lượt tra thêm cho **mệnh đề hỏi** của đề. Phần đầu
đề toàn dữ kiện riêng (khối lượng, thể tích, vận tốc) — những từ ấy có trong
hàng trăm công thức; "Tính động năng của vật" mới là thứ nói đúng đại lượng
cần tìm.

## Những cái bẫy đã xử lí

Phần lớn thời gian dựng hệ thống này là để lời kiểm chứng **không báo oan**.
Ghi lại đây vì chúng đều là bẫy im lặng — sai mà không có lỗi nào ném ra:

| bẫy | vì sao nguy hiểm | cách xử lí |
|---|---|---|
| `0{,}0241` | 31,5% số bước giải trong kho dùng dấu phẩy thập phân kiểu Việt Nam. Bỏ qua thì parser đọc thành số nguyên và **mọi** kiểm chứng sai. | chuẩn hoá `{,}` → `.`, nhưng để nguyên dấu phẩy trần (nó là chỉ số dưới) |
| `F = ma` | SymPy dành `F`, `T`, `S`, `N`, `Q`, `C` cho hằng dựng sẵn — `F` là hằng logic *false*. Trong đề Lí đó là lực. | ép về ký hiệu khi chuỗi không chứa toán tử quan hệ |
| `Symbol` là `Boolean` | SymPy cho `Symbol` kế thừa `Boolean`, nên kiểm "vế có phải mệnh đề không" quá rộng sẽ bỏ qua mọi phép so có ký hiệu trần | chỉ bắt `BooleanAtom` và `BooleanFunction` |
| `2\cos 6\theta + 20` | parser `lark` đọc nhập nhằng, có nhánh nuốt cả `+ 20` vào trong ngoặc, làm một đồng nhất thức lượng giác đúng bị kết luận sai | ưu tiên backend `antlr`, bỏ hẳn kết quả nhập nhằng của `lark` |
| `\lim_{x \to 3}` | `\to` vừa là mũi tên giới hạn vừa là liên từ suy ra; tách theo nó sẽ xé đôi chính biểu thức cần kiểm | không kể `\to` vào danh sách liên từ |
| `1 + (y')^2 = 1 + 4x^2(x^2+1)` | dấu `=` mang hai nghĩa: đồng nhất thức (sai là sai thật) và thế số (hai vế cố ý khác nhau) | khác tập ẩn ⇒ là thế số ⇒ không kết tội |
| `\sin^2 x + \cos^2 x = 1` | nhưng khác tập ẩn cũng có thể là đồng nhất thức thật | thay số kiểm xem vế còn ẩn có phải hằng không |
| `\ln 0{,}30125 = -1{,}1998` | lời giải sư phạm làm tròn ở từng bước rồi sai số truyền tiếp | dung sai suy từ số chữ số thực sự được viết, cộng ngưỡng tương đối 0,5% |
| `P_1 = 0{,}5 \qquad P_2 = 0{,}4` | hai mệnh đề độc lập trên một dòng; tách theo mọi dấu `=` sẽ nối `0,5` với `P_2` thành đẳng thức bịa | tách theo `\qquad`, `\quad`, `;`, `\\` trước |
| `r^2 = 5r - 6 \iff r^2-5r+6 = 0` | phương trình đang giải, không phải đồng nhất thức | có liên từ logic hoặc lời giải nói "giải phương trình" ⇒ chỉ xác nhận, không kết tội |
| `\left(\frac{3}{103}\right)` | ký hiệu Legendre trông hệt một phân số | danh sách ký pháp ngoài tầm parser ⇒ trả "chưa kết luận" |
| gộp token của nhiều kỹ năng | hỏi "bài nào luyện MỘT TRONG các kỹ năng này" mà lại đi đo "bài nào phủ được CẢ" — không bài nào qua ngưỡng, và gợi ý biến mất **đúng lúc người học có nhiều lỗ hổng nhất** | chấm độ phủ theo từng kỹ năng rồi lấy giá trị tốt nhất |
| id công thức mô hình bịa ra | lời giải trông có căn cứ mà dẫn nguồn không tồn tại | đối chiếu lại với kho, loại id giả và ghi cảnh báo |
| `= \frac{x+3}{x-2}` | bước nối tiếp mở đầu bằng `=`; `"" in "<>!:"` cho **True** trong Python nên dấu `=` đầu dòng không bao giờ được tách — mà đây là lối viết phổ biến nhất trong kho | kiểm `prev and prev in ...` |
| kỹ năng viết hai kiểu | `"đổi đơn vị"` và `"doi-don-vi"` là cùng một kỹ năng nhưng so chuỗi nguyên thì thành hai; hậu quả: 95% kỹ năng chỉ ra đúng một bài, tính năng luyện tập vô dụng | chuẩn hoá token + chấm điểm IDF |
| `Q10 ≈ 2,31` | con số dính sau chữ cái là **phần của tên ký hiệu**, không phải giá trị; đọc bừa thì ra 10 | số phải không đứng ngay sau chữ cái; giá trị lấy ở vế phải dấu `=`/`≈` |
| `≈ 2,0 nF` với `answer_numeric = 2e-9` | kho ghi giá trị ở đơn vị gốc còn đáp án hiển thị ở đơn vị có tiền tố; chọn con số trước rồi mới quy đổi là sai | thử từng ứng viên qua đúng đường quy đổi |
| `18,84 cM`, `2,68 × 10³ bp` | Pint không biết đơn vị chuyên ngành; coi "không hiểu" là "sai" thì bộ chấm nói sai với người trả lời đúng | không hiểu đơn vị thì so số và nói rõ là chưa kiểm được đơn vị |
| kho bài tập không phủ tiểu học | phân loại chỉ bỏ phiếu từ kho bài tập nên bài chu vi hình chữ nhật lớp 4 bị gán THPT, rồi truy xuất ra công thức Vật lí | môn và cấp bỏ phiếu từ kho **công thức**, vốn phủ liền mạch lớp 1 - đại học |
| `/{collection}/{record_id}` | route bắt-tất khớp mọi đường dẫn hai đoạn, nuốt luôn `/illustrations/<id>.svg` và trả 422 | khai báo route bắt-tất sau cùng |
| luồng CAS quá hạn không chết | SymPy không huỷ được giữa chừng: mỗi lần quá hạn để lại một luồng chạy vĩnh viễn ở 100% CPU **và giữ chỗ trong pool**. Sau đủ số lần, mọi phép tính sau đó — kể cả loại mất vài mili-giây — đều phải xếp hàng chờ hết hạn. Server cứ chạy lâu là chậm dần rồi đứng hẳn | không bao giờ xếp hàng: hết chỗ thì bỏ qua ngay; đếm số luồng đã mất |
| `subs` bắt theo tham chiếu | lambda thay số chạy ở luồng khác trong khi vòng lặp đã đi tiếp, nên có thể đọc phải bộ giá trị của lượt sau và kết luận "hai vế khác nhau" vô căn cứ | `lambda subs=subs:` |
| `18\ \text{g/m}^3` | bỏ `\text{g/m}` để lại `^3` lơ lửng, CAS đọc thành 18³ = 5832 — con số bị nhân lên 324 lần mà không lỗi nào ném ra | nuốt luôn số mũ đi kèm khi gỡ `\text{...}` |
| `1800 g (1,8 kg)` | chú thích trong ngoặc bị tính vào đơn vị, Pint đọc ra thứ nguyên bậc hai rồi báo sai | gỡ ngoặc cuối trước khi đọc đơn vị |
| `\sum_{n=1}^{\infty}` | `.doit()` trên chuỗi vô hạn chạy hàng phút ở 100% CPU. Chặn thời gian từng phép là chưa đủ: SymPy không huỷ được giữa chừng nên mỗi lần quá hạn để lại một luồng vẫn chạy, và chúng dồn lại làm treo cả tiến trình | hạn chót cho **cả lượt** kiểm chứng, cộng danh sách ký pháp bỏ qua |

### Đợt hai — tìm bằng cách đọc tay từng bước `audit` báo là "bị bác bỏ"

`audit` vẫn báo 1,8% số bước bị bác bỏ, và README này vẫn ghi rằng phần lớn
trong đó là báo oan — nhưng chưa ai hỏi **vì sao**. Lấy năm bước bất kỳ trong
danh sách ấy rồi mở lời giải ra đọc: cả năm đều đúng. Truy ngược từng cái, cộng
với một lượt quét cả kho để đo tần suất, ra bảng dưới đây.

Xếp nguy hiểm nhất lên trước, và tiêu chí "nguy hiểm" ở đây là **xác nhận
khống** đứng trên báo oan: báo oan thì người dùng còn nhìn thấy để cãi lại, còn
một lời "đã kiểm" rỗng nội dung thì không để lại dấu vết nào.

| bẫy | vì sao nguy hiểm | cách xử lí |
|---|---|---|
| `\approx` | parser đọc dấu xấp xỉ thành **một ẩn tự do tên `approx`** rồi nhân vào: `\frac{1}{2} \approx 0{,}5` ra `0{,}25\,approx`. 9,3% số bước của kho có dấu này, và đó chính là chỗ kho ghi giá trị đã tính ra | tách mắt xích theo cả `=` lẫn `≈`; khâu nối bằng `≈` **chỉ được xác nhận, không bao giờ được kết tội** |
| `max(1.0, ...)` làm thang đo | ngưỡng "coi như bằng nhau" neo ở 1.0, nên **mọi** đại lượng nhỏ hơn 10⁻⁹ đều bằng nhau. Hằng Planck, điện tích nguyên tố, nồng độ mol — cả mảng Lí-Hoá vi mô rơi vào đó. Hỏng hai chiều: hai giá trị lệch nhau 9 lần được xác nhận là bằng nhau, còn biểu thức còn ẩn thì bị coi là hằng rồi đem so như số | thang đo lấy từ độ lớn chính các giá trị đọc được; "cả hai thực chất bằng 0" tách riêng, suy từ độ lớn các **số hạng** |
| `P(X = 4)` | parser đánh rơi sạch đối số, chỉ còn `P`. `P(X > 68)` và `P(Z > 1{,}481)` thành **cùng một thứ**, CAS reo "trùng khớp về cấu trúc" rồi xác nhận một bước nó chưa hề kiểm | mỗi lời gọi hàm thành một **nguyên tử mờ** mang số hiệu riêng; khâu dính nguyên tử mờ không bao giờ được kết tội |
| `\bar{x}` | gỡ mũ đi thì trung bình mẫu và biến trần nhập làm một: `z = \frac{x-\bar{x}}{s}` thành `z = 0`, còn `\operatorname{rank} A = \operatorname{rank}\bar{A}` thành hai vế trùng khít rồi được "xác nhận" | đổi tên chứ không gỡ mũ: `\bar{x}` → `x_{bar}` |
| `\frac{dh}{dt}` | SymPy đọc thành `Derivative(h, t)` với `h` là ký hiệu tự do, và `.doit()` cho **0** vì đạo hàm của hằng bằng 0. Mọi bước có ký pháp Leibniz bị đem so với 0 rồi bác bỏ — mà đó là ký pháp trung tâm của giải tích lẫn động học | đổi `h` thành hàm `h(t)`, đạo hàm ở lại dạng chưa tính được |
| `\cos 30^{\circ}` | bỏ mũ tròn thì thành cos(30 **radian**) = 0,154 thay vì 0,866 | đổi `<số>^\circ` sang radian; độ Celsius, trạng thái chuẩn `\Delta H^{\circ}` và phép hợp `f \circ g` vẫn bị chặn như cũ |
| `6{,}0^{\circ}\cdot 4^{3/4} = 6{,}0\cdot 2{,}8284` | một mắt xích **trộn** hai cách ghi: vế có mũ tròn đã đổi sang radian, vế viết trần thì chưa. So thẳng thì lệch đúng 180/π lần | vế nào ghi độ vế nào không thì không so thẳng |
| `4 ( ) + 1` | cả hai parser LaTeX nhận một **tiền tố hợp lệ** rồi vứt phần đuôi mà không ném lỗi nào. `4\ (\text{vòng thơm}) + 1\ (\mathrm{C{=}O}) = 5` gỡ chú thích xong trả về đúng `4`, và CAS kết luận `4 ≠ 5` | cổng an toàn: từ chối kết quả parse khi còn ngoặc rỗng, toán tử cụt, hai cụm số dính nhau, hoặc ẩn trùng tên một lệnh LaTeX parser không hiểu |
| `F d\cos 0^{\circ}` | ngữ pháp coi `d` là dấu vi phân nên `d\cos` gộp thành **một ký hiệu tên `dcos`**, đối số của cosin rơi ra ngoài thành thừa số nhân; với góc 0 thì cả tích thành 0 | cùng cổng an toàn: ẩn mang tên một hàm mà chuỗi nguồn thật sự gọi ⇒ bỏ kết quả parse |
| `\left.t^{2}\right|_{0}^{1}` | gạch thay cận không có trong parser, và nó **lặng lẽ nuốt sạch phần từ dấu gạch trở đi**: `1 + \left.t^{2}\right|_{0}^{1}` đọc thành đúng số `1` | loại **riêng vế ấy**, không bỏ cả bước — khâu `1 + 1 = 2` bên cạnh vẫn kiểm được |
| `U_{\text{eff}}` | `\text` trong chỉ số dưới là **tên** đại lượng, không phải chú thích; gỡ như chú thích để lại `U_{}` và parser chết | mã nhãn thành chỉ số bằng số (`U_{241681}`) — parser đọc chỉ số nhiều chữ cái thành **tích** từng chữ, nên giữ chữ sẽ so nhầm |
| `0{,}0252\ \mathrm{g} = 25{,}2\ \mathrm{mg}` | gỡ đơn vị rồi so số thì một phép **đổi đơn vị** đúng thành lỗi lệch 999 lần | đọc phần số của vế có đơn vị, quy đổi bằng Pint rồi mới so; không quy đổi được thì "chưa kết luận" |
| `2577\times(-7{,}601) = -19{,}59\ \mathrm{kJ/mol}` | chỉ một vế ghi đơn vị, vế kia ngầm ở J/mol | chỉ tha khi tỉ số **đúng là một bội số mười**; tỉ số khác thì đơn vị chẳng giải thích được gì và vẫn phải bác bỏ |
| `\text{s}^{2}/\text{m}^{3}` | gỡ từng mẩu `\text{}` để lại dấu `/` lơ lửng, một vế vốn đọc được thành không đọc được | gỡ **cả cụm** đơn vị nối nhau; một mẩu đứng lẻ sau dấu `+` thì vẫn để cụt, vì ở đó ta thật sự không biết cái bị gỡ đáng giá bao nhiêu |
| `V'(t) > 0 \text{ khi } t < 4` | gỡ chú thích xong còn `V'(t) > 0 t < 4`; vế giữa `0 t` **tính ra số 0** vì SymPy rút gọn `0*t` ngay lúc đọc, và ta "xác nhận" được `0 < 4` — một phép so không có trong lời giải | vế "số thuần" phải không còn chữ cái trần nào |
| `\frac{\pi}{\sin(\pi/3)}` | parser trả `\pi` về **ẩn tự do**, thay số ngẫu nhiên vào rồi kết luận sai. Nhưng trong Thống kê `\pi` là tỉ lệ tổng thể nên đọc nó là hằng π cũng không phải luôn đúng | một cách đọc xác nhận là đủ để xác nhận; phải **cả hai** cùng bác bỏ mới được kết tội |
| `n=2: 4>4\ (\text{sai})` | lời giải **cố tình viết ra bất đẳng thức sai** để chỉ ra mệnh đề hỏng từ đâu | bất đẳng thức và `≈` chỉ được xác nhận, không bao giờ được kết tội |
| `CH_3\text{-}C\equiv CH + AgNO_3 \rightarrow \dots` | sách giáo khoa viết phản ứng hữu cơ theo lối **bộ khung**, lược cả sản phẩm phụ; đếm nguyên tử ở đó luôn lệch mà lời giải hoàn toàn đúng | có ký hiệu liên kết trong công thức ⇒ chỉ xác nhận, không kết tội |
| `180^{\circ}+53{,}1^{\circ} = 233^{\circ}` | lệch 0,04%, đúng chuẩn làm tròn sư phạm. Nhưng khi `to_number` hết giờ vì máy bận, luồng rơi xuống phép thay số vốn so ở ngưỡng 1e-8 và kết tội — **một lời bác bỏ chỉ hiện ra lúc quá tải** | nhánh hai vế đều là số mà chưa quy ra giá trị: xác nhận được thì xác nhận, kết tội thì không |

### Đợt ba — vòng phản biện

Đợt hai làm tám đòn bẩy song song, mỗi cái tự đo trên lát cắt kho của riêng nó,
và **cả tám đều báo "0 bước bị bác bỏ mới"**. Một vòng phản biện riêng, không đo
lại độ phủ mà chỉ **dựng đầu vào hiểm rồi hỏi ngược "chỗ nào hệ thống nói đã
kiểm mà thật ra chưa kiểm gì"**, tìm thêm được chín lỗ hổng — gần như tất cả đều
là xác nhận khống chứ không phải báo oan.

Lí do các phép đo bỏ sót chúng đáng ghi lại: lỗi nằm ở **chỗ hai đòn bẩy gặp
nhau** — hàng rào của cái này bịt miệng kết luận của cái kia — và kho không có
sẵn ca nào bày ra chuyện đó. Đo trên kho không thay được việc tự nghĩ ra đầu vào
hiểm.

| bẫy | vì sao nguy hiểm | cách xử lí |
|---|---|---|
| mâu thuẫn bị bịt miệng | hàng rào đơn vị / độ / `≈` hạ một mắt xích từ "khác nhau" xuống "chưa kết luận", nhưng luật "một mắt xích đúng là cả bước đúng" vẫn chạy. Một dòng vừa chứa mâu thuẫn thật vừa chứa một khâu phụ đúng hiện ra là **verified** | mâu thuẫn bị hạ xuống thì cả bước dừng ở "chưa kết luận"; dấu ấy đi ngược lên tận `check_steps` vì một dòng thường có nhiều mệnh đề độc lập |
| `4 \ge 4{,}4` | dung sai suy từ số chữ số viết ra: `4` chỉ có một chữ số nên dung sai ±0,5, đủ để bất đẳng thức SAI được "xác nhận" là đúng | chiều của bất đẳng thức đo bằng sai số **tương đối**, không bằng số chữ số |
| `2H_2+O_2 \to 2H_2O :\ n = 5\times3 = 16` | nhánh hoá học trả "cân bằng" rồi `return` ngay, nên nhánh SymPy không bao giờ chạy và phép nhân sai ngay cạnh được đóng dấu "đã kiểm" | mẩu bên cạnh còn phép tính thì nhường cho CAS; chỉ đoản mạch khi mẩu ấy chỉ là một giá trị được đặt tên |
| `M_{C} = 12` | `check_molar_mass` chạy cho mọi bước của mọi môn. `M` là mômen lực, trung bình mẫu, tên điểm hình học — chỉ số dưới của chúng vẫn đọc trót lọt thành "công thức một nguyên tố" | tên chất phải TỰ NÓ mang dấu hiệu hoá học mới được tra bảng nguyên tử khối |
| `CuSO_4 \cdot 5H_2O` | `\cdot` bị gỡ rồi khoảng trắng bị xoá, còn `CuSO_45H_2O` — chỉ số đọc ra là **45** | khoảng trắng còn sót nghĩa là có thứ gì vừa bị gỡ ⇒ trả "không đọc được" |
| `f(x)` cho theo từng khoảng | nhánh `\begin{cases}` bị từ chối **trước khi biết tên hàm** nên không đầu độc được tên; nhánh viết thường sau đó được học và đem thế cho mọi `f(a)` | đọc tên trước, rồi đầu độc ở MỌI lối từ chối |
| `3^{\circ} > 2^{\circ} > 1^{\circ}` | bậc carbocation trong Hoá hữu cơ bị quy sang radian rồi "xác nhận" thứ tự 0,0349 > 0,0175 — kiểm đúng cái vừa tự bịa | cả dòng chỉ gồm chữ số mang mũ tròn nối bằng dấu so ⇒ là bảng xếp hạng, không quy đổi |
| `\mathrm{H_2SO_4}` bị tính là đơn vị | lớp châm chước "dòng có nhiều đơn vị khác nhau thì không kết tội" đếm cả công thức hoá học, nên mọi dòng Hoá có hai công thức trở lên được miễn kết tội | chỉ nhãn ASCII, không chỉ số dưới, không chữ số, toàn từ ≤ 4 ký tự mới được tính là đơn vị |
| `p \approx 0{,}58` | vế sau `≈` là con số người viết gõ sẵn, không phải kết quả CAS tính ra, mà lời kết luận vẫn ghi "CAS tính lại được" | nói đúng đã kiểm được cái gì; chỉ nhận là "tính lại" khi một vế khác trong cùng mắt xích tính ra đúng chừng ấy |

## Lộ trình học

```bash
./.venv/bin/aistem roadmap "định luật Ohm"
./.venv/bin/aistem roadmap exam.ap-calculus-bc --minutes 45 --sessions
```

Mục tiêu nhận **id bài học**, **id kỳ thi**, hoặc **từ khoá chủ đề**. Không cần
khoá API: lộ trình dựng hoàn toàn từ đồ thị tiên quyết của kho.

Bốn bước:

1. **Phân giải mục tiêu** — người học nói "tích phân", không nói id. Với kỳ thi
   thì đi qua `formulas_must_memorize` để tìm bài dạy chúng.
2. **Bao đóng tiên quyết** — mọi bài phải học trước. Bài đã nắm bị cắt **cùng
   toàn bộ nhánh phía trên nó**: đã hiểu đạo hàm hàm hợp thì không quay lại
   định nghĩa đạo hàm. Đây là chỗ lộ trình khác một mục lục sách.
3. **Sắp thứ tự** — tô-pô có hàng trăm thứ tự hợp lệ, và thứ tự "hợp lệ" bất kỳ
   thì nhảy cóc giữa các môn và các cấp. Dùng hàng đợi ưu tiên phá hoà theo cấp
   học → lớp → `unit`/`order` của kho, tức theo đúng trình tự sách giáo khoa.
4. **Xen bài luyện và chia buổi** — mỗi bài giảng kèm bài tập dùng đúng công
   thức nó dạy, độ khó tăng dần; rồi cắt thành các buổi vừa quỹ thời gian.

Ví dụ có thật (`quy tắc L'Hospital`): 9 bài học, 18 bài luyện, 8,1 giờ, 9 buổi
60 phút — bắt đầu từ "Khái niệm giới hạn", kết thúc đúng ở bài đích.

Hai hàng rào đáng chú ý:

- **Tiên quyết luôn đứng trước.** Đo trên 7 mục tiêu và 25 bài lấy ngẫu nhiên
  mỗi lượt `audit`: 0 vi phạm. Vi phạm ở đây thì người học vấp ngay bài đầu mà
  nhìn bảng vẫn thấy hợp lí.
- **Mục tiêu vô nghĩa bị từ chối, không đoán bừa.** BM25 luôn trả về *cái gì
  đó*; một lộ trình 40 giờ nhắm sai chủ đề trông rất thuyết phục. Hệ thống đòi
  mục tiêu phải chia sẻ ít nhất một từ mang nghĩa với bài đích, và **nói rõ đã
  hiểu mục tiêu thành những bài nào** để người học bác lại được.

## Tiến độ và ôn giãn cách

```bash
./.venv/bin/aistem progress done lesson.math.ap-calculus.gioi-han-khai-niem
./.venv/bin/aistem progress show
./.venv/bin/aistem progress review
```

Trước phần này vòng lặp học bị hở: hệ thống chẩn đoán được, dựng được lộ trình,
chấm được bài — nhưng không nhớ gì, nên mỗi lần mở lên là bắt đầu lại và người
học phải tự khai "tôi đã học bài nào".

Ba điểm thiết kế:

- **Đọc bài giảng và làm đúng bài tập là hai chuyện khác nhau** — cái đầu mới là
  đã tiếp xúc, cái sau mới là bằng chứng đã hiểu. Hai bảng riêng.
- **Ôn giãn cách tính theo kỹ năng, không theo từng bài tập.** Người học cần nhớ
  *cách làm*, không cần nhớ một đề cụ thể. Thuật toán lối SM-2; hai cách viết của
  cùng một kỹ năng dùng chung một lịch nhờ khoá chuẩn hoá.
- **Mức thạo giảm trọng theo thời gian** (nửa đời 30 ngày). Làm đúng ba lần hồi
  tháng trước rồi sai hôm nay thì mức thạo phải xuống, mà tỉ lệ đúng thô vẫn 75%.

Chấm bài tự cập nhật lịch ôn, và `roadmap --learner <ai>` tự lấy bài đã học cùng
kỹ năng yếu từ tiến độ thật thay vì bắt khai tay.

## Thi thử

```bash
./.venv/bin/aistem mock-exam exam.ap-calculus-bc -n 20
```

36 hồ sơ kỳ thi trong kho không phải mô tả suông: mỗi hồ sơ có `sections` (số
câu, thời lượng, có được dùng máy tính), `topic_weights` cộng đúng 100%, và
`scoring`. Đủ chi tiết để bốc bài từ ngân hàng cho ra đề **cùng tỉ trọng** với đề
thật, rồi chấm và phân tích theo từng chủ đề của bản thiết kế.

Chia số câu theo lối Hamilton nên tổng luôn khớp. Chủ đề nào kho chưa đủ bài thì
**báo thẳng** trong `coverage` và `warnings` — lấy bừa bài chủ đề khác cho đủ số
câu là cách chắc chắn nhất để người học tưởng mình đã ôn kín trong khi có mảng
chưa đụng tới.

## Chấm bài

Bất biến quan trọng nhất của một bộ chấm: **nộp đúng đáp án mà kho công bố thì
phải được chấm đúng**. Đo lần đầu trên toàn kho thì 436/1258 bài (35%) trượt
bất biến này — và bộ chấm nói "sai" chứ không nói "không chấm được", tức là nói
sai với người trả lời đúng. Sau khi sửa:

```
chấm đúng            1 223 / 1 258   (97%)
nói không chấm được     35           (2,8%, thành thật)
chấm oan                 0           (đầu: 436 = 35%)
```

Vẫn nghiêm: nộp đáp án lệch 60% thì **100%** bị bắt, và với bài nhiều phần thì
nhân đôi mọi con số cũng bị bắt hết (204/204).

Hai đợt sửa sau đưa "không chấm được" từ 155 bài xuống 35, và đóng lại lớp xác
nhận khống cuối cùng của bộ chấm:

**Một câu diễn giải không được làm hỏng cả đáp án.** `Ức chế cạnh tranh; K_i =
0,25 mM` từng bị trả về "không chấm được" nguyên bài, chỉ vì mẩu đầu là chữ.
Nay phần chấm được thì chấm, phần bằng lời được ghi là **chưa chấm được** —
trạng thái thứ ba, đúng như lớp kiểm chứng CAS. Xếp nó vào ô "sai" là nói với
người học rằng họ làm sai một thứ chưa ai chấm.

**Trường `tolerance` của kho lẫn lộn hai quy ước.** Phần lớn ghi sai số **tương
đối** (`0{,}01` = ±1%), nhưng 119 bài (9,5%) ghi **tuyệt đối** — `50000` cho đáp
án `k_{cat}/K_M = 7{,}5\times10^{6}`, tức ±0,67%. Bộ chấm đọc mọi giá trị như
tương đối, nên cửa sổ chấp nhận của những bài ấy rộng tới năm triệu phần trăm và
người học sai gấp đôi vẫn được khen đúng. Đây là bẫy im lặng tệ nhất của bộ
chấm: nó không báo gì, chỉ gật đầu.

Phân biệt bằng chính con số, không đoán theo tên trường: sai số tương đối lớn
hơn 20% thì không còn là quy ước chấm bài nào cả, nên giá trị ấy chắc chắn là
tuyệt đối. Quy đổi xong mà **vẫn** quá rộng thì con số ấy không phải dung sai
của đại lượng đang xét — thường là dung sai kho khai cho một đại lượng khác
trong cùng đáp án nhiều phần — nên bỏ hẳn, lấy mặc định.

Sửa xong, `do-nghiem` từ 97% lên **100%**.

Bốn cách chấm, chọn theo dạng bài:

- **trắc nghiệm** — so khoá phương án, và với phương án sai thì trả luôn
  `why_wrong` mà kho đã ghi sẵn: *vì sao phương án nhiễu ấy hấp dẫn và sai ở đâu*.
- **nhiều đại lượng** — `Vmax = 50 μmol/phút; Km = 4,0 mM` được tách ra chấm
  từng cái, ghép theo nhãn nên trả lời sai thứ tự không bị phạt, và cho **điểm
  từng phần** kèm tên đại lượng còn sai. Mẩu nào là diễn giải bằng lời thì ghi
  rõ **chưa chấm được**, không xếp vào ô sai.
- **bảng đúng/sai** — `(a) Đúng; (b) Sai; (c) Đúng; (d) Sai`, dạng câu trắc
  nghiệm đúng-sai của đề thi hiện hành. Chấm tất định theo từng ý, thiếu một ý
  là thiếu chứ không phải trả lời ngược.
- **điền số** — so theo dung sai, **tự quy đổi đơn vị**: `980 cm/s²` và `9,8 m/s²`
  là cùng một đáp án. Đúng số mà sai đơn vị là một verdict riêng (`sai-don-vi`),
  không gộp chung với sai hẳn. Lệch dưới 5% được xếp `gan-dung` kèm nhắc "làm
  tròn quá sớm ở bước trung gian".
- **tự luận** — so **tương đương biểu thức** bằng CAS, nên `\frac{1}{2}`, `0.5`
  và `2^{-1}` đều được chấp nhận như nhau.
- còn lại — so văn bản đã chuẩn hoá không dấu, và nói thẳng là cần người chấm.

`POST /diagnose` nhận cả loạt câu trả lời rồi chỉ ra kỹ năng nào đang yếu (theo
**tỉ lệ** sai, không theo số câu sai tuyệt đối), chủ đề nào sai nhiều, và đi
ngược đồ thị công thức → bài giảng để gợi đúng phần cần học lại.

## Đo chất lượng: `aistem audit`

```bash
./.venv/bin/aistem audit
```

Chạy hệ thống **ngược lại trên chính kho** rồi đo tỉ lệ tự mâu thuẫn. Đây là
cách tìm lỗi hiệu quả nhất ở dự án này, hơn hẳn test viết tay — test chỉ kiểm
những trường hợp người viết nghĩ ra được, còn kho 7 424 bản ghi chứa đủ mọi cách
viết không ai đoán hết nổi. Ba lần dùng nó đều lòi ra lỗi nặng:

| phép đo | bất biến | lần đo đầu | hiện tại |
|---|---|---|---|
| `cham-bai` | nộp đúng đáp án kho công bố thì phải chấm đúng | 436/1258 sai (35%) | 0/400, chấm được 391/400 |
| `kiem-chung` | lời giải đã kiểm định nên bước bị bác bỏ phải hiếm | 294 bước, gần hết báo oan | 1,1% |
| `do-nghiem-kiem-chung` | làm hỏng một con số trong bước đã xác nhận thì nhãn "đã kiểm" phải mất | — | 6% xác nhận khống |
| `goi-y-luyen-tap` | mỗi kỹ năng phải gợi được vài bài luyện | 95% kỹ năng vô dụng | 1,5% |
| `lo-trinh` | đồ thị tiên quyết phi chu trình, lộ trình đúng thứ tự | — | 0 chu trình, 0 vi phạm |
| `do-nghiem` | nới cho đúng dễ nới quá tay — kiểm chiều ngược lại | — | bắt 100% |
| `lien-ket` | liên kết giữa các kho phải trỏ tới bản ghi có thật | — | 0 cạnh treo |

`do-nghiem-kiem-chung` là bản đối xứng của `do-nghiem`: `do-nghiem` canh bộ
**chấm bài**, còn phép đo này canh bộ **kiểm chứng**. Thiếu nó thì "nới cho đỡ
báo oan" và "nới tới mức xác nhận khống" trông giống hệt nhau trên mọi con số
báo cáo — trong khi xác nhận khống nguy hiểm hơn, vì báo oan thì người dùng còn
nhìn thấy để cãi lại.

Ngưỡng của nó đặt ở 15% chứ không phải 0, và đó là chủ ý: một bước gồm nhiều mắt
xích được xác nhận khi **một** mắt xích kiểm được, nên làm hỏng con số ở mắt
xích khác không nhất thiết làm mất nhãn. Đọc "verified" là "CAS đã tính lại
được ít nhất một khâu của bước này", không phải "cả bước đều đúng".

Mẫu 400 bài mặc định chạy khoảng 65 giây. `-n 0` quét cả kho nhưng mất nhiều
phút: kho có một cụm bài (chuỗi Fourier, ma trận lớn) mà SymPy xử lí rất nặng và
chúng chi phối gần hết thời gian chạy. `--json` trả mã thoát khác 0 khi có phép
đo không đạt, dùng được trong CI.

Gần như toàn bộ thời gian ấy nằm ở **một chỗ**: đọc LaTeX bằng antlr chiếm ~90%
hồ sơ chạy. Vì thế `to_sympy` có bộ đệm trong tiến trình — một lời giải hỏi đi
hỏi lại cùng một chuỗi rất nhiều lần (vế phải mang sang bước sau, phần rút giá
trị số quét lại, lớp đổi đơn vị đọc lại vế đã đọc), và đệm chúng cắt được 44%
thời gian. Chỉ đệm kết quả **đọc được**: một lần trả None có thể chỉ vì hết giờ
lúc máy bận, nhớ lại thì cái rủi thoáng qua ấy thành vĩnh viễn.

Chạy lại sau mỗi lần kho mở rộng.

## Phát triển

```bash
./.venv/bin/python -m pytest -q
```

469 test, chạy **không cần khoá API**: phần gọi mô hình được thay bằng bản giả
lập (fixture `fake_llm`), nên kiểm được cả những đường lỗi khó dựng bằng API
thật — mô hình bịa id công thức, mô hình tự tin mà tính sai, mô hình lỗi giữa
chừng.

Quá nửa số test nằm ở lớp CAS, và chúng chia đôi theo chủ đích: một nửa khẳng
định hệ thống **xác nhận thêm được**, nửa còn lại khẳng định nó **vẫn im lặng**
ở đúng những chỗ bảng bẫy phía trên liệt kê. Nửa sau mới là nửa dễ mất: mỗi lần
nới độ phủ là một lần có thể vô tình mở lại một đường báo oan cũ.

```bash
./.venv/bin/ruff check aistem tests
```

## Giới hạn cần biết

- Kiểm chứng CAS **không thay được giáo viên**. Nó bắt lỗi số học và lỗi biến
  đổi đại số; nó không đánh giá được lập luận, cách trình bày, hay việc một
  phương pháp có phù hợp với chương trình người học đang theo hay không.
- Khoảng 1,1% số bước bị bác bỏ trong khi lời giải thật ra đúng — chủ yếu ở ký
  pháp ngoài tầm parser (ma trận, ký hiệu Legendre, đại số đơn vị, hệ cơ số).
- CAS xác nhận được **41%** số bước và **63%** số đáp số của kho; phần còn lại
  ghi rõ là "chưa kết luận được". Đừng đọc "chưa kết luận" thành "sai" — phần
  lớn trong đó là bước thế số, bước phát biểu công thức, hoặc lập luận bằng lời,
  tức những chỗ vốn không có gì để một CAS đối chiếu.
- "Đã kiểm" nghĩa là **ít nhất một khâu** của bước ấy được tính lại và khớp,
  không phải cả bước. `aistem audit` đo đúng chỗ hở này (`do-nghiem-kiem-chung`).
- Mỗi lượt kiểm chứng có trần thời gian (`AISTEM_VERIFY_BUDGET`, mặc định 20 s).
  Hết giờ thì các bước còn lại ghi rõ là "bỏ qua vì hết thời gian" — chưa kiểm,
  chứ không im lặng coi như đã kiểm.
- Dữ liệu trong kho do mô hình sinh và đã qua một vòng kiểm định tự động; trước
  khi dùng dạy học chính thức vẫn cần giáo viên bộ môn rà lại.
- Bộ nhớ đệm lời gọi mô hình nằm ở `engine/.cache/`, khoá theo nội dung prompt.
  Xoá thư mục đó nếu muốn giải lại từ đầu.
