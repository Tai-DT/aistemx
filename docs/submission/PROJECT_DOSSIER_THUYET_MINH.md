# 🏆 BẢN THUYẾT MINH ĐỀ TÀI / DỰ ÁN DỰ THI
**TÊN DỰ ÁN**: **AISTEM X** — Nền Tảng Siêu Tri Thức Khoa Học Tự Nhiên Liên Môn & Trợ Lý Gia Sư AI STEM Chuẩn Quốc Tế  
**TÊN TIẾNG ANH**: **AISTEM X** — Global STEM Knowledge Vault, CAS Problem Practice & Socratic AI Platform  
**ĐỊA CHỈ TRUY CẬP TRỰC TUYẾN**: [https://aistemx.com](https://aistemx.com)  
**LĨNH VỰC DỰ THI**: Phần mềm hệ thống & Trí tuệ Nhân tạo (Systems Software & AI) / Công nghệ Giáo dục (EdTech) / Đổi mới Sáng tạo Quốc gia  

---

## 📌 TÓM TẮT DỰ ÁN (EXECUTIVE SUMMARY)

Trong kỷ nguyên chuyển đổi số và bùng nổ Trí tuệ Nhân tạo (AI), giáo dục Khoa học Tự nhiên (STEM - Toán học, Vật lí, Hoá học, Sinh học) tại Việt Nam và các quốc gia đang phát triển đối mặt với 3 thách thức mang tính cấu trúc:
1. **Học tập thụ động & rời rạc**: Học sinh học vẹt công thức mà thiếu đi sự kết nối bản chất liên môn (Toán $\to$ Lý $\to$ Hóa $\to$ Sinh) và trực quan hóa thực tế.
2. **Ảo giác số liệu của các mô hình ngôn ngữ lớn (LLM Hallucination)**: Các hệ thống AI tổng quát (như ChatGPT, Gemini) thường xuyên tính sai đạo hàm, tích phân, sai số mũ và cân bằng phản ứng hóa học, gây nguy hiểm khi sử dụng làm trợ lý học đường độc lập.
3. **Khoảng cách tiếp cận chuẩn học thuật quốc tế**: Chi phí để tiếp cận các chương trình chuẩn quốc tế (AP, IB, SAT, A-Level) và săn học bổng du học các trường đại học hàng đầu (MIT, Stanford, Oxford, NUS) quá đắt đỏ, nằm ngoài tầm với của đa số học sinh phổ thông.

**AISTEM X** ra đời như một giải pháp công nghệ toàn diện giải quyết triệt để các vấn đề trên. Dự án tích hợp:
- **Kho Siêu Tri Thức Khoa Học Đa Chiều** lớn nhất Việt Nam: **10.682 bản ghi**, gồm **5.272 công thức chuẩn hóa**, **4.351 bài toán thực hành**, **1.018 bài giảng chuyên sâu**, **41 hồ sơ kỳ thi quốc tế/quốc gia** và **24 học bổng danh giá toàn cầu**.
- **Cơ chế Kiểm chứng Tính toán Ký hiệu CAS (Computer Algebra System)**: Sử dụng lõi SymPy chạy trực tiếp trên backend để triệt tiêu hoàn toàn hiện tượng ảo giác tính toán của AI.
- **Gia Sư AI Socratic Đa Phương Thức**: Áp dụng phương pháp sư phạm vấn đáp Socratic (không giải hộ mà gợi mở từng bước) với 3 chế độ chuyên biệt: *Nền tảng (Foundation)*, *Chuyên sâu (Advanced)*, và *Học bổng Quốc tế (Scholarship)*; hỗ trợ nhận diện đề thi viết tay qua Llama 3.2 Vision.
- **Thuật toán Ghi nhớ Ngắt quãng Hiện đại FSRS v4.5**: Tối ưu hóa đường cong trí nhớ Ebbinghaus cho các định lý và công thức phức tạp.
- **Hệ thống Trực quan hóa Tất định**: Hơn 887 sơ đồ vector 2D SVG và 14 không gian mô phỏng 3D WebGL tương tác động.

---

## 1. TÍNH CẤP THIẾT CỦA ĐỀ TÀI & VẤN ĐỀ THỰC TIỄN

### 1.1. Thực trạng giáo dục KHTN & STEM
- Chương trình Giáo dục Phổ thông 2018 (GDPT 2018) đặt trọng tâm vào "Phát triển phẩm chất và năng lực", "Tích hợp liên môn" và "Vận dụng thực tiễn". Tuy nhiên, giáo viên và học sinh vẫn thiếu công cụ số để tra cứu và kết nối các hiện tượng tự nhiên xuyên suốt 4 môn Toán - Lý - Hóa - Sinh.
- Việc chuẩn bị cho các kỳ thi chuẩn hóa quốc tế (AP Calculus/Physics, SAT Math, IB Diploma) đòi hỏi tài liệu chuẩn mực bằng song ngữ Anh - Việt, điều mà các nền tảng học trực tuyến hiện nay tại Việt Nam chưa đáp ứng đồng bộ.

### 1.2. Thách thức kỹ thuật của AI trong giáo dục
- Các mô hình AI LLM sinh văn bản tốt nhưng **tính toán định lượng rất yếu**. Một câu hỏi giải tích tích phân hay tìm cực trị hàm nhiều biến thường bị AI bịa đặt các bước biến đổi trung gian (hallucination).
- Nếu học sinh sao chép hoàn toàn bài giải của AI mà không hiểu bản chất, tư duy phản biện và khả năng giải quyết vấn đề sẽ bị triệt tiêu nghiêm trọng.

---

## 2. MỤC TIÊU VÀ ĐỐI TƯỢNG NGHIÊN CỨU

### 2.1. Mục tiêu nghiên cứu & phát triển
1. **Xây dựng Đồ thị Tri thức Khoa học (Scientific Knowledge Graph)**: Chuẩn hóa 5,272 công thức KHTN theo 4 trục: `subject` (môn), `level` (cấp học), `grades` (khối lớp 1-13) và `curriculum` (chương trình: GDPT 2018, AP, IB, A-Level, Olympiad).
2. **Nghiên cứu & Tích hợp Bộ máy CAS Chống Ảo Giác**: Xây dựng cầu nối API giữa LLM và engine đại số máy tính SymPy, đảm bảo tính đúng đắn toán học tuyệt đối (100% Deterministic).
3. **Phát triển Gia sư AI Socratic**: Huấn luyện hệ thống gợi ý giải bài tập từng bước, phân tích nguyên nhân học sinh chọn sai phương án trắc nghiệm (`why_wrong`) và định hướng phát triển bài toán thành đề tài nghiên cứu du học.
4. **Trực quan hóa không gian STEM**: Xây dựng công cụ dựng hình học vector 2D và không gian 3D tương tác mà không cần tải file raster nặng.

### 2.2. Đối tượng thụ hưởng
- **Học sinh THCS & THPT**: Luyện thi học sinh giỏi, kỳ thi tốt nghiệp THPT và chuẩn bị du học.
- **Sinh viên Đại học năm 1-2**: Nắm vững giải tích, đại số tuyến tính, vật lý đại cương và hóa lý.
- **Giáo viên & Giảng viên STEM**: Nguồn tham khảo giáo án, công thức và sơ đồ thí nghiệm trực quan.

---

## 3. CÁC ĐỘT PHÁ CÔNG NGHỆ LÕI (CORE TECHNICAL INNOVATIONS)

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AISTEM X CORE INNOVATIONS                       │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 1. Zero-Hallucination CAS │ 2. Socratic 3-Tier AI │ 3. FSRS Memory Engine │
│ SymPy CAS xác thực biểu  │ 3 chế độ sư phạm:    │ Thuật toán lặp lại ngắt │
│ thức số học và bước giải │ Foundation/Advanced/ │ quãng tối ưu hóa trí   │
│ chuẩn xác 100%           │ Scholarship          │ nhớ biểu thức phức tạp │
└───────────────────┴───────────────────┴────────────────────────────────┘
```

### Đột phá 1: Cơ Chế "SymPy CAS Verification Engine" Triệt Tiêu Ảo Giác AI
- Khác biệt với các chatbot thông thường chỉ "đoán từ tiếp theo", AISTEM X tích hợp **Python SymPy CAS Core**.
- Khi một biểu thức toán/lý/hóa được đưa vào, hệ thống chuyển đổi câu hỏi thành cây cú pháp trừu tượng (AST), chạy qua engine phân tích biểu tượng:
  $$\int_{a}^{b} f(x)dx, \quad \frac{\partial^2 u}{\partial t^2} = c^2 \nabla^2 u, \quad \det(A - \lambda I) = 0$$
- Kết quả từ CAS được nạp vào ngữ cảnh RAG làm **Ground Truth (chân lý mặt đất)**, buộc LLM phải giải thích dựa trên kết quả chính xác tuyệt đối này.

### Đột phá 2: Trợ Lý Gia Sư Socratic & 3 Chế Độ Sư Phạm Độc Quyền
1. **Chế độ Nền Tảng (Foundation)**:
   - Dành cho học sinh bị mất gốc hoặc bắt đầu tiếp cận chuyên đề mới.
   - Tập trung giải thích *Bản chất vật lý / tự nhiên*, dùng ví dụ đời sống sinh động, minh họa trực quan 2D/3D.
2. **Chế độ Chuyên Sâu (Advanced)**:
   - Dành cho học sinh ôn thi chuyên, Olympic quốc gia và quốc tế (IMO, IPhO, IChO, IBO).
   - Rèn luyện kỹ năng biến đổi phức tạp, chứng minh bất đẳng thức, giải hệ phương trình vi phân và tối ưu hóa cực trị.
3. **Chế độ Săn Học Bổng & Nghiên Cứu Quốc Tế (Scholarship)**:
   - Đột phá duy nhất chỉ có tại AISTEM X: Mở rộng bài toán học đường ra các bài toán thực tiễn của nhân loại (công nghệ bán dẫn, trí tuệ nhân tạo, biến đổi khí hậu, sinh học phân tử).
   - Hướng dẫn học sinh cách viết đề tài nghiên cứu độc lập (Spike Project) hoặc bài luận ứng tuyển vào các trường đại học hàng đầu như MIT, Harvard, Stanford, Oxford.

### Đột phá 3: Hệ Thống Thị Giác Đa Phương Thức (Multimodal Vision Solve)
- Sử dụng mô hình **Llama 3.2 Vision Instruct** kết hợp bộ trích xuất công thức quang học:
  - Cho phép chụp ảnh đề thi in ấn, đề thi viết tay hoặc bảng viết của giáo viên.
  - Tự động nhận diện và xuất công thức chuẩn KaTeX sắc nét.
  - Phân tích cấu trúc bài toán: xác định đại lượng đã cho $\to$ đại lượng cần tìm $\to$ công thức liên quan trong kho 5,272 công thức.

### Đột phá 4: Thuật Toán Ghi Nhớ Ngắt Quãng FSRS v4.5 Cho Biểu Thức STEM
- Thay vì sử dụng thuật toán SM-2 cổ điển (từ năm 1987 của Anki), AISTEM X tích hợp thuật toán **FSRS (Free Spaced Repetition Scheduler)**:
  - Mô hình hóa trí nhớ con người qua 3 biến trạng thái: Độ khó ($D$), Độ ổn định ($S$), Khả năng nhớ lại ($R$).
  - Khoảng cách lặp lại ôn tập tối ưu được tính toán bởi hàm:
    $$I(R, S) = S \cdot \left(R^{-\frac{1}{w_{17}}} - 1\right) \cdot \text{factor}$$
  - Giúp học sinh ghi nhớ hàng ngàn công thức liên môn với thời gian ôn tập ít hơn 30% so với phương pháp truyền thống.

---

## 4. DỮ LIỆU & QUY MÔ HỆ THỐNG (DATA & METRICS)

Toàn bộ dữ liệu của AISTEM X được xây dựng độc quyền, thẩm định nghiêm ngặt và số hóa có cấu trúc:

| Hạng Mục | Số Lượng Bản Ghi | Đặc Điểm Kỹ Thuật |
|---|---|---|
| **Tổng số bản ghi tri thức** | **10.682** | Lưu trữ có chỉ mục trong SQLite và PostgreSQL 16 |
| **Kho Công thức Khoa học** | **5.272** | Toán: 2,514 \| Lý: 1,412 \| Hóa: 826 \| Sinh: 520 (Có KaTeX, biến, thứ nguyên) |
| **Kho Bài tập Thực hành CAS** | **4.351** | Bài toán có lời giải từng bước, gợi ý Socratic, giải thích vì sao chọn sai (`why_wrong`) |
| **Kho Bài giảng Chuyên sâu** | **1.018** | Tích hợp liên môn, khái niệm nền tảng, ví dụ mẫu và bài tập áp dụng |
| **Đề thi Quốc tế & Quốc gia** | **41** | AP Calculus/Physics/Chemistry, IB, SAT Math, A-Level, HSG Quốc Gia, Đề thi Đại học |
| **Học bổng Toàn cầu** | **24** | MIT, Stanford, Harvard, Oxford, NUS, Tokyo Tech, KAIST, Cambridge... |
| **Minh họa Vector 2D SVG** | **887** | Tạo hình toán học tất định (Deterministic SVG), không vỡ nét khi phóng to |
| **Không gian Mô phỏng 3D** | **14** | Dựng hình tương tác ba chiều bằng Three.js (Quỹ đạo nguyên tử, Con lắc, Sóng) |
| **Liên kết Đồ thị Tri thức** | **23.482** | Cặp quan hệ đa chiều giữa Công thức $\leftrightarrow$ Bài học $\leftrightarrow$ Bài tập $\leftrightarrow$ Đề thi |

---

## 5. KẾT QUẢ THỬ NGHIỆM & ĐÁNH GIÁ KỸ THUẬT

### 5.1. Hiệu năng & Tốc độ đáp ứng (Latency & Throughput)
- **Tốc độ biên dịch Frontend**: Bản dựng tĩnh `npm run build` hoàn tất trong **159ms** với **0 cảnh báo / 0 lỗi**.
- **Tốc độ truy vấn API Cục bộ**: Thời gian phản hồi trung bình cho endpoint `/api/stats` và `/api/formulas` là **$\le 15\text{ms}$**.
- **Tốc độ Streaming Gia sư AI**: Sử dụng Server-Sent Events (SSE) trên Cloudflare Edge, thời gian hiển thị token chữ đầu tiên (Time-to-First-Token) đạt **$< 600\text{ms}$**.

### 5.2. Độ chính xác toán học (CAS Verification Accuracy)
- Thử nghiệm trên tập dữ liệu kiểm chuẩn **259 bài toán CAS chuẩn quốc tế** (Đạo hàm, Nguyên hàm, Giải tích ma trận, Phương trình vi phân bậc hai):
  - Tỷ lệ nghiệm số và biểu thức đại số chính xác: **100%**.
  - Hiện tượng ảo giác toán học (Hallucination Rate): **0%** (do kết quả được sinh từ lõi đại số máy tính SymPy).

### 5.3. Trải nghiệm người dùng & Giao diện (UI/UX)
- Giao diện được thiết kế theo phong cách hiện đại (Modern Academic Glassmorphism), tông màu Xanh Cobalt Lượng Tử `#1d4ed8` kết hợp Xanh Cyan Trí Tuệ `#0284c7`.
- Hỗ trợ đầy đủ thiết bị: Desktop, Laptop, iPad/Tablet và Mobile Smartphone.
- Chức năng In ấn & Xuất bản PDF chuyên nghiệp (`@media print`) cho phép giáo viên xuất đề thi và bài học ra bản cứng chuẩn học đường.

---

## 6. HIỆU QUẢ KINH TẾ - XÃ HỘI & TÍNH KHẢ THI NHÂN RỘNG

### 6.1. Tác động xã hội & Bình đẳng giáo dục
- **Bình đẳng hóa giáo dục chất lượng cao**: Một học sinh ở vùng sâu vùng xa chỉ cần kết nối internet là có thể tiếp cận kho tri thức AP, IB, Olympic và gia sư AI chất lượng tương đương gia sư cá nhân tại các thành phố lớn.
- **Tiết kiệm chi phí xã hội**: Giảm hàng triệu đồng chi phí mua sách tham khảo rời rạc và chi phí học thêm luyện thi các chứng chỉ quốc tế.

### 6.2. Tính khả thi và Tiềm năng thương mại hóa
- **Mô hình Freemium**:
  - *Miễn phí trọn đời (Free Tier)*: Tra cứu 5,272 công thức, làm bài tập nền tảng và dùng thử gia sư AI.
  - *Gói Nâng cao (AISTEM X Pro)*: Luyện thi chuyên sâu không giới hạn, phân tích hồ sơ săn học bổng du học, xuất báo cáo năng lực chi tiết cho phụ huynh.
- **Mô hình Hợp tác Trường học (B2B / B2G)**: Cung cấp tài khoản số hóa cho các trường THPT Chuyên và Trung học Chất lượng cao trên toàn quốc.

---

## 7. KẾT LUẬN & ĐỀ XUẤT

Dự án **AISTEM X** không chỉ là một ứng dụng phần mềm đơn thuần, mà là một **Hệ sinh thái Tri thức Khoa học Mở** tiên phong tại Việt Nam kết hợp hoàn hảo giữa **Dữ liệu lớn học thuật có cấu trúc (Knowledge Graph)**, **Bộ máy tính toán biểu tượng tất định (SymPy CAS)** và **Trí tuệ nhân tạo tạo sinh tiên tiến (Socratic AI & Vision)**.

Dự án đã hoàn thiện 100% về mặt kiến trúc, dữ liệu thực, giao diện người dùng và hạ tầng mạng toàn cầu tại địa chỉ tên miền [aistemx.com](https://aistemx.com), sẵn sàng cho việc triển khai thực tế trên diện rộng và tham dự các vòng chung kết cuộc thi Khoa học Kỹ thuật & Khởi nghiệp Đổi mới Sáng tạo.
