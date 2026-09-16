# 📐 BỘ TÀI LIỆU THUẬT TOÁN & PROJECT TOÁN HỌC CHO AISTEM

Bộ tài liệu này cung cấp nền tảng lý thuyết thuật toán định lượng, phân tích các dự án toán học mã nguồn mở tiên tiến nhất trên thế giới, và định hình kiến trúc phát triển cho hệ thống **AIstem (Toán · Lí · Hoá · Sinh)**.

---

## 🧭 CẤU TRÚC BỘ TÀI LIỆU (DOCUMENTATION SUITE)

```
docs/math-algorithms-and-projects/
├── README.md                                    # Chỉ mục & Kiến trúc tổng thể bộ tài liệu
├── 01-THUAT-TOAN-DAI-SO-VA-GIAI-TICH-SO.md      # SVD, Trị riêng, FFT, RK4, Newton-Raphson, Cầu phương Gauss
├── 02-THUAT-TOAN-HINH-HOC-XAC-SUAT-HON-LOAN.md  # Bézier, Voronoi/Delaunay, Monte Carlo, Galton, Mandelbrot, Lorenz
├── 03-KHAO-SAT-CAC-PROJECT-TOAN-HOC-HANG-DAU.md # Manim, Mathigon Polypad, GeoGebra, JSXGraph, SymPy, Lean 4
└── 04-LO-TRINH-TRIEN-KHAI-MATH-ENGINE-AISTEM.md # Blueprint kiến trúc Engine & Interactive Labs cho AIstem
```

---

## 🎯 MỤC TIÊU CHIẾN LƯỢC CHO AISTEM

1. **Toán học chính xác & Không ảo giác (Deterministic Math)**: 
   - Thay vì để mô hình ngôn ngữ tự sinh lời giải thuần chữ có thể sai số, AIstem tích hợp trực tiếp các thuật toán giải tích số (Numerical Methods) và hệ thống máy tính đại số biểu tượng (Symbolic CAS như SymPy / Math.js) để tính toán và kiểm chứng độc lập.
2. **Trực quan hóa khoa học tương tác cao (Interactive Scientific Visualization)**:
   - Học tập các project đỉnh cao như **Mathigon Polypad**, **GeoGebra**, và **3Blue1Brown Manim**, chuyển hóa các công thức tĩnh trên sách giáo khoa thành các phòng thí nghiệm toán học động (Interactive Math Labs) 60fps trên Web (Canvas Retina HiDPI & Three.js 3D).
3. **Cầu nối liên môn STEM**:
   - Toán học đóng vai trò ngôn ngữ nền tảng:
     - **Giải phương trình vi phân (ODE / Runge-Kutta)** $\to$ Mô phỏng Động lực học chất điểm & Mạch dao động trong **Vật lý**.
     - **Đại số ma trận & Cân bằng phương trình** $\to$ Cân bằng phản ứng oxi hóa khử & Động học hóa học trong **Hóa học**.
     - **Xác suất thống kê & Chuỗi Markov / Di truyền quần thể** $\to$ Mô hình Hardy-Weinberg & Di truyền Mendel trong **Sinh học**.

---

## 🗺️ MA TRẬN LIÊN KẾT: THUẬT TOÁN ↔ PROJECT THAM CHIẾU ↔ MODULE AISTEM

| Phân loại toán học | Thuật toán cốt lõi | Project tham chiếu tiêu biểu | Module AIstem tích hợp |
|---|---|---|---|
| **Đại số tuyến tính** | SVD, Phân rã QR/LU, Trị riêng/Vectơ riêng, Biến đổi Affine | *NumPy, SciPy, 3Blue1Brown Manim* | `VectorStudioView.tsx`, `MathEngineStudioView.tsx` (Eigen Mode) |
| **Giải tích & Tín hiệu** | Khai triển Fourier, FFT, Đạo hàm số, Tích phân Gauss | *Manim, Wolfram Alpha, SciPy FFT* | `MathEngineStudioView.tsx` (Fourier Epicycles), `Live CAS` |
| **Phương trình vi phân** | Euler, Runge-Kutta 4 (RK4), Verlet Integration | *PhET Simulations, SciML (Julia)* | `VirtualLabView.tsx` (Con lắc, Ném xiên, Quỹ đạo hành tinh) |
| **Hình học tính toán** | Dựng hình Euclid, Đường cong Bézier, Voronoi/Delaunay | *GeoGebra, JSXGraph, Mathigon* | `GeometryPuzzleArenaView.tsx`, `generators2d.py` |
| **Xác suất & Hỗn loạn** | Bảng Galton, Monte Carlo, Fractal Mandelbrot, Lorenz Attractor | *Mathigon, Desmos, Shadertoy* | `MathEngineStudioView.tsx` (Galton, Mandelbrot), `ArenaView` |
| **Đại số máy tính (CAS)** | Đơn giản hóa biểu thức, Rút ẩn, Khai triển đa thức, Giới hạn | *SymPy, Giac/Xcas, Math.js* | `engine/server.py`, `aistem/verify.py`, `KatexMath.tsx` |
| **Chứng minh hình thức** | Kiểm tra logic vị từ, Suy diễn từng bước | *Lean 4 (Mathlib), Coq* | `engine/deep_analysis.py`, Luyện thi Olympic & AP |

---

## 🚀 HƯỚNG DẪN ĐỌC VÀ TRIỂN KHAI

- Nếu cần tìm hiểu **công thức và mã nguồn mẫu thuật toán**: Đọc file [01-THUAT-TOAN-DAI-SO-VA-GIAI-TICH-SO.md](file:///Volumes/SecondaryDisk/aistemx/docs/math-algorithms-and-projects/01-THUAT-TOAN-DAI-SO-VA-GIAI-TICH-SO.md) và [02-THUAT-TOAN-HINH-HOC-XAC-SUAT-HON-LOAN.md](file:///Volumes/SecondaryDisk/aistemx/docs/math-algorithms-and-projects/02-THUAT-TOAN-HINH-HOC-XAC-SUAT-HON-LOAN.md).
- Nếu cần học hỏi **cách tổ chức phần mềm và kiến trúc mã nguồn mở**: Đọc file [03-KHAO-SAT-CAC-PROJECT-TOAN-HOC-HANG-DAU.md](file:///Volumes/SecondaryDisk/aistemx/docs/math-algorithms-and-projects/03-KHAO-SAT-CAC-PROJECT-TOAN-HOC-HANG-DAU.md).
- Nếu cần triển khai **tính năng thực tế vào Frontend / Backend của AIstem**: Đọc file [04-LO-TRINH-TRIEN-KHAI-MATH-ENGINE-AISTEM.md](file:///Volumes/SecondaryDisk/aistemx/docs/math-algorithms-and-projects/04-LO-TRINH-TRIEN-KHAI-MATH-ENGINE-AISTEM.md).
