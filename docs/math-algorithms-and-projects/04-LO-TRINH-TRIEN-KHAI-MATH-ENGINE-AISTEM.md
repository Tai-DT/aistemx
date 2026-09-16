# 🛠️ CHUYÊN ĐỀ 4: KIẾN TRÚC & LỘ TRÌNH TRIỂN KHAI MATH ENGINE CHO AISTEM

Tài liệu này vạch ra chiến lược tích hợp thực tế, kiến trúc hệ thống và lộ trình phát triển các phòng thí nghiệm toán học tương tác (Interactive Math Labs) trên nền tảng **AIstem**.

---

## 1. TỔNG QUAN KIẾN TRÚC TOÁN HỌC AISTEM (SYSTEM ARCHITECTURE)

Hệ thống AIstem xử lý toán học theo mô hình đa tầng:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           TẦNG GIAO DIỆN (UI)                           │
│  - Next.js 14 App Router + TailwindCSS + KaTeX                          │
│  - 4 Phòng Thí Nghiệm Toán Học Tương Tác:                               │
│    1. MathEngineStudioView: Fourier Epicycles, Eigenvalues, Galton,     │
│                             Mandelbrot Fractal                          │
│    2. GeometryPuzzleArenaView: Dựng hình Euclid (Compa & Thước kẻ)      │
│    3. VectorStudioView: Phép toán vectơ, Tích vô hướng/hướng, Bézier   │
│    4. Live CAS Modal: Máy tính rút ẩn và khảo sát hàm tức thời          │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                     Tương tác số học / API Request
                                     │
┌────────────────────────────────────┴────────────────────────────────────┐
│                       TẦNG TÍNH TOÁN & KIỂM CHỨNG                       │
│                                                                         │
│  [Client-side (Math.js)]                 [Server-side Engine (FastAPI)]  │
│  - Tính toán tức thì 0ms trễ             - SymPy CAS Resolver           │
│  - Parse biểu thức an toàn               - Bước kiểm chứng 5 trong solve│
│  - Ma trận số phức & đạo hàm             - BM25 truy xuất 4 kho dữ liệu │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                             Nạp & Kiểm định
                                     │
┌────────────────────────────────────┴────────────────────────────────────┐
│                      TẦNG DỮ LIỆU CHUẨN HÓA (DATA)                      │
│  - data/formulas/math/: 2,514 công thức toán học (có LaTeX + biến số)   │
│  - data/lessons/: 411 bài giảng lý thuyết toán                          │
│  - data/problems/: 4,161 bài tập có lời giải từng bước có thể chấm tự động│
│  - data/illustrations/: Ảnh vector SVG và Scene 3D Three.js             │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 2. NGUYÊN TẮC THIẾT KẾ PHÒNG THÍ NGHIỆM TOÁN HỌC TRỰC QUAN

Theo hướng dẫn trong `stem-scientific-visualization`, mọi tương tác toán học trên Canvas phải tuân thủ nghiêm ngặt 3 tiêu chuẩn:

1. **HiDPI Retina Canvas Rendering**:
   ```typescript
   const dpr = window.devicePixelRatio || 1;
   canvas.width = displayWidth * dpr;
   canvas.height = displayHeight * dpr;
   ctx.scale(dpr, dpr);
   ```
2. **Neon Bloom Shader & Trực quan hóa véc-tơ sắc nét**:
   - Sử dụng `ctx.shadowBlur = 8` và `ctx.shadowColor` tương ứng với biến màu CSS `--ill-accent` để đường cong tiếp tuyến và véc-tơ phát sáng rõ nét trên nền tối (`slate-950`).
3. **Toán học chính xác, không giả lập ngẫu nhiên (No Hallucinated Visuals)**:
   - Các điểm giao cắt hình học, đường tiếp tuyến, phép xoay ma trận và phân phối xác suất phải tính toán bằng các thuật toán giải tích và đại số thực sự (xem [01-THUAT-TOAN-DAI-SO-VA-GIAI-TICH-SO.md](file:///Volumes/SecondaryDisk/aistemx/docs/math-algorithms-and-projects/01-THUAT-TOAN-DAI-SO-VA-GIAI-TICH-SO.md)).

---

## 3. LỘ TRÌNH 4 GIAI ĐOẠN PHÁT TRIỂN MATH ENGINE CHO AISTEM

### 📍 Giai đoạn 1: Hoàn thiện các Module Tương tác Canvas 2D (Hiện tại)
- ✅ `MathEngineStudioView.tsx`:
  - Mô phỏng chuỗi Fourier biến đổi sóng vuông, tam giác, răng cưa bằng các vòng tròn ngoại luân (Epicycles).
  - Khảo sát biến đổi ma trận $2 \times 2$ (phép quay, trượt, co giãn, suy biến $\det = 0$) kèm trực quan hóa vectơ riêng (Eigenvectors).
  - Bảng Galton 21 khay rơi 500 hạt bi mô phỏng Định lý Giới hạn Trung tâm (CLT).
  - Fractal Mandelbrot cho phép zoom sâu vào vùng số phức kỳ ảo.
- ✅ `GeometryPuzzleArenaView.tsx`:
  - 5 màn thử thách dựng hình Euclid kinh điển (Dựng tam giác đều, đường trung trực, phân giác góc, tiếp tuyến đường tròn).
  - Hệ thống tính toán giao điểm đường tròn - đường thẳng tự động.
- ✅ `VectorStudioView.tsx`:
  - Thao tác kéo thả các vectơ $\vec{u}, \vec{v}$, tính tổng, hiệu, tích vô hướng $\vec{u} \cdot \vec{v} = |\vec{u}||\vec{v}|\cos\theta$ và hình chiếu trực giao.

---

### 📍 Giai đoạn 2: Tích hợp Hệ Thống Đại Số Máy Tính Tức Thời (Live Client CAS)
- **Mục tiêu**: Khi học sinh xem bất kỳ công thức toán học nào trong số 2,514 công thức (ví dụ: *Đạo hàm của tích*, *Nghiệm phương trình bậc 3*, *Tích phân từng phần*):
  - Có ngay một tab **"Máy tính biểu tượng Live CAS"** cạnh bài học.
  - Cho phép nhập tham số bằng thanh trượt (Sliders) hoặc bàn phím toán học để thấy đồ thị biến thiên tương ứng theo thời gian thực ($< 16\text{ ms}$).
  - Sử dụng thư viện `Math.js` trên Client và fallback về `SymPy` ở server nếu gặp các phương trình phi tuyến cấp cao hoặc vi phân.

---

### 📍 Giai đoạn 3: Bộ Công Cụ Thao Tác Trực Quan (Visual Manipulatives - Chuẩn Mathigon)
- **Mục tiêu**: Xây dựng kho linh kiện trực quan cho học sinh cấp 1, 2 và 3:
  1. **Algebra Tiles (Ô gạch đại số)**:
     - Biểu diễn $x^2, x, 1$ dưới dạng các khối hình học màu sắc.
     - Khi học sinh ghép 1 ô $x^2$, 3 ô $x$ và 2 ô $1$ thành một hình chữ nhật lớn, kích thước hai cạnh chính là $(x+1)$ và $(x+2)$ $\implies$ Hiểu sâu sắc bản chất phân tích đa thức thành nhân tử.
  2. **Prime Factor Bubbles (Bong bóng thừa số nguyên tố)**:
     - Mỗi số nguyên tố có một màu sắc đặc trưng. Kéo hai bong bóng số 2 và 3 nhập vào nhau sẽ sinh ra bong bóng số 6. Kéo tách bong bóng 12 ra sẽ thành $2 \times 2 \times 3$.
  3. **Vòng tròn Lượng giác Tương tác (Interactive Unit Circle)**:
     - Kéo điểm trên đường tròn đơn vị để quan sát đồng thời sự thay đổi của trục $\sin, \cos, \tan, \cot$ và đồ thị hàm sóng chạy ngang.

---

### 📍 Giai đoạn 4: Thẩm Định Lời Giải Từng Bước & Chứng Minh Hình Thức (Olympiad Engine)
- **Mục tiêu**: Nâng cấp module `engine/deep_analysis.py` và `engine/server.py`:
  - Ứng dụng tư duy suy luận hình thức từ **Lean 4**: chia nhỏ bài toán chứng minh hình học hoặc bất đẳng thức thành một cây logic (Proof Tree).
  - Tự động phát hiện các lỗi ngụy biện thường gặp của học sinh: chia cho 0, bình phương hai vế làm xuất hiện nghiệm ngoại lai, quên điều kiện xác định của hàm logarit và căn bậc chẵn.
  - Gợi ý định lý cần dùng tiếp theo dựa trên đồ thị liên kết công thức `data/formulas/usage.json`.

---

## 5. HƯỚNG DẪN VIẾT BÀI GIẢNG TOÁN HỌC CHUẨN MARKDOWN TRÊN AISTEM

Khi thêm hoặc chỉnh sửa các file Markdown bài giảng trong `data/lessons/` hoặc `docs/lessons/`:

1. **Công thức Toán chuẩn KaTeX**:
   - Dùng `$ ... $` cho công thức nội dòng (inline): `$f(x) = ax^2 + bx + c$`.
   - Dùng `$$ ... $$` cho công thức khối (display):
     $$\int_{a}^{b} f(x) dx = F(b) - F(a)$$
2. **Cấu trúc sư phạm bắt buộc**:
   - **Mục tiêu bài học**: 3 gạch đầu dòng rõ ràng.
   - **Bản chất trực giác**: Giải thích ý nghĩa hình học hoặc ứng dụng thực tế trước khi đi vào biến đổi đại số.
   - **Công thức & Điều kiện nghiệm**: Nêu rõ tập xác định và các trường hợp biên.
   - **Sai lầm kinh điển (Common Pitfalls)**: Nêu ít nhất 2 bẫy học sinh hay mắc phải.
   - **Khóa nối ID**: Gắn nhãn `formula_id` để hệ thống tự động kết nối với phòng thí nghiệm tương tác.
