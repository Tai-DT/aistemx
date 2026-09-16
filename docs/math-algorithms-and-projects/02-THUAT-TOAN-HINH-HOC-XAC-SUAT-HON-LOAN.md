# 🌀 CHUYÊN ĐỀ 2: THUẬT TOÁN HÌNH HỌC TÍNH TOÁN, XÁC SUẤT VÀ HỖN LOẠN

Tài liệu này cung cấp cơ sở toán học, thuật toán không gian và mã nguồn thực thi cho **Hình học tính toán (Computational Geometry)**, **Xác suất ngẫu nhiên (Stochastic & Monte Carlo)** và **Hệ động lực phi tuyến / Fractal (Chaos & Fractals)** phục vụ các phòng thí nghiệm tương tác của **AIstem**.

---

## 1. HÌNH HỌC TÍNH TOÁN & ĐƯỜNG CONG (COMPUTATIONAL GEOMETRY)

### 1.1. Đường Cong Bézier & Thuật Toán de Casteljau

Đường cong Bézier bậc $n$ được xác định bởi $n+1$ điểm kiểm soát $P_0, P_1, \dots, P_n$ theo công thức đa thức Bernstein:
$$B(t) = \sum_{i=0}^n \binom{n}{i} (1 - t)^{n-i} t^i P_i, \quad t \in [0, 1]$$

- **Đường cong bậc 3 (Cubic Bézier - chuẩn SVG / Canvas)**:
$$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t)t^2 P_2 + t^3 P_3$$

- **Thuật toán đệ quy de Casteljau**: Tính toán điểm trên đường cong bằng cách nội suy tuyến tính liên tiếp, là nền tảng chia nhỏ đường cong (subdivision) mượt mà 60fps trên Canvas.

```typescript
export interface Point2D {
  x: number;
  y: number;
}

export function evaluateCubicBezier(p0: Point2D, p1: Point2D, p2: Point2D, p3: Point2D, t: number): Point2D {
  const u = 1 - t;
  const tt = t * t;
  const uu = u * u;
  const uuu = uu * u;
  const ttt = tt * t;

  return {
    x: uuu * p0.x + 3 * uu * t * p1.x + 3 * u * tt * p2.x + ttt * p3.x,
    y: uuu * p0.y + 3 * uu * t * p1.y + 3 * u * tt * p2.y + ttt * p3.y
  };
}
```

---

### 1.2. Thuật Toán Bắt Dính Giao Điểm Dựng Hình Euclid (Ruler & Compass Engine)

Phục vụ đấu trường dựng hình hình học `GeometryPuzzleArenaView.tsx`:

#### 1. Giao điểm 2 đường tròn:
Cho đường tròn $C_1(O_1, r_1)$ và $C_2(O_2, r_2)$ với khoảng cách tâm $d = \|O_1 - O_2\|$:
- Nếu $d > r_1 + r_2$ hoặc $d < |r_1 - r_2|$: Không giao nhau.
- Nếu $d = r_1 + r_2$ hoặc $d = |r_1 - r_2|$: Tiếp xúc tại 1 điểm.
- Nếu $|r_1 - r_2| < d < r_1 + r_2$: Cắt nhau tại 2 điểm phân biệt:
$$a = \frac{r_1^2 - r_2^2 + d^2}{2d}, \quad h = \sqrt{r_1^2 - a^2}$$
Điểm trung gian $P = O_1 + \frac{a}{d}(O_2 - O_1)$. Hai giao điểm là:
$$I_{1,2} = \begin{pmatrix} P_x \pm \frac{h}{d}(O_{2y} - O_{1y}) \\ P_y \mp \frac{h}{d}(O_{2x} - O_{1x}) \end{pmatrix}$$

```typescript
export function intersectCircles(
  c1: { x: number; y: number; r: number },
  c2: { x: number; y: number; r: number }
): { x: number; y: number }[] {
  const dx = c2.x - c1.x;
  const dy = c2.y - c1.y;
  const d = Math.hypot(dx, dy);

  if (d > c1.r + c2.r || d < Math.abs(c1.r - c2.r) || d === 0) {
    return []; // Không có giao điểm thực
  }

  const a = (c1.r * c1.r - c2.r * c2.r + d * d) / (2 * d);
  const h = Math.sqrt(Math.max(0, c1.r * c1.r - a * a));

  const px = c1.x + (a * dx) / d;
  const py = c1.y + (a * dy) / d;

  if (h < 1e-6) {
    return [{ x: px, y: py }]; // Tiếp xúc
  }

  return [
    { x: px + (h * dy) / d, y: py - (h * dx) / d },
    { x: px - (h * dy) / d, y: py + (h * dx) / d }
  ];
}
```

---

### 1.3. Phân Hoạch Voronoi & Tam Giác Hóa Delaunay

- **Tam giác hóa Delaunay**: Mạng lưới tam giác nối các điểm sao cho không có điểm nào nằm bên trong đường tròn ngoại tiếp của bất kỳ tam giác nào (tối đa hóa góc nhỏ nhất, tránh các tam giác dẹp dài).
- **Sơ đồ Voronoi**: Đồ thị đối ngẫu của Delaunay, phân chia mặt phẳng thành các vùng lân cận gần nhất với mỗi điểm hạt.
- **Ứng dụng STEM**: Mô hình hóa màng tế bào thực vật, phân bố mật độ tế bào biểu bì trong Kính hiển vi (`SpecimensLabView.tsx`), và cấu trúc tinh thể rắn.

---

## 2. XÁC SUẤT, THỐNG KÊ & PHƯƠNG PHÁP MONTE CARLO

### 2.1. Mô Phỏng Bảng Galton (Quincunx) & Định Lý Giới Hạn Trung Tâm (CLT)

Bảng Galton là minh chứng vật lý tuyệt đẹp về sự chuyển hóa từ các biến cố rời rạc độc lập (tung đồng xu rơi sang trái/phải với xác suất $p=0.5$) thành **Phân phối Chuẩn Gauss (Normal Distribution)**:

Số lần bi lệch sang phải sau $N$ tầng đinh tuân theo phân phối nhị thức:
$$P(X = k) = \binom{N}{k} p^k (1 - p)^{N-k}$$

Khi $N \to \infty$, theo định lý De Moivre–Laplace:
$$P(X = k) \approx \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(k - \mu)^2}{2\sigma^2} \right) \quad \text{với } \mu = Np, \; \sigma^2 = Np(1-p)$$

```typescript
// Thuật toán thả hạt mô phỏng rơi vật lý vào các khay (bins)
export function simulateGaltonDrop(rows: number = 16, p: number = 0.5): number {
  let bin = 0;
  for (let r = 0; r < rows; r++) {
    if (Math.random() < p) {
      bin += 1;
    }
  }
  return bin; // Vị trí khay tích lũy từ 0 đến rows
}
```

---

### 2.2. Phương Pháp Tích Phân Monte Carlo (Monte Carlo Integration)

Dùng số ngẫu nhiên để tính diện tích hình phẳng hoặc tích phân đa chiều phức tạp mà giải tích số cổ điển gặp hiện tượng "lời nguyền số chiều" (Curse of Dimensionality).

Ước lượng diện tích miền $\Omega \subset [a, b] \times [c, d]$:
$$I \approx \text{Area}(\text{Bounding Box}) \times \frac{N_{\text{trong}}}{N_{\text{tổng}}}$$

Ước tính số $\pi$ bằng việc thả $N$ điểm ngẫu nhiên vào hình vuông $[-1, 1] \times [-1, 1]$ và đếm số điểm rơi vào hình tròn đơn vị $x^2 + y^2 \le 1$:
$$\pi \approx 4 \times \frac{N_{\text{tròn}}}{N_{\text{tổng}}}$$

---

## 3. HỆ ĐỘNG LỰC, HỖN LOẠN & FRACTAL (CHAOS & FRACTALS)

### 3.1. Tập Hợp Mandelbrot & Julia (Số Phức)

Được định nghĩa bởi ánh xạ đa thức lặp trên trường số phức $\mathbb{C}$:
$$z_{n+1} = z_n^2 + c, \quad z_0 = 0$$

- **Tập Mandelbrot**: Tập hợp tất cả các giá trị tham số $c \in \mathbb{C}$ sao cho dãy $\{z_n\}$ bị chặn (không tiến tới vô cùng khi $n \to \infty$).
- **Thuật toán thời gian thoát (Escape-Time Algorithm)**: Nếu tồn tại $n$ sao cho $|z_n| > 2$ thì chắc chắn dãy sẽ phân kỳ ra vô cùng. Ta ghi nhận chỉ số bước lặp $n$ làm màu sắc pixel.

```typescript
export function mandelbrotPixel(
  cr: number,
  ci: number,
  maxIter: number = 100
): { escaped: boolean; iter: number } {
  let zr = 0;
  let zi = 0;
  let zr2 = 0;
  let zi2 = 0;

  for (let i = 0; i < maxIter; i++) {
    zi = 2 * zr * zi + ci;
    zr = zr2 - zi2 + cr;
    zr2 = zr * zr;
    zi2 = zi * zi;

    if (zr2 + zi2 > 4.0) {
      return { escaped: true, iter: i };
    }
  }

  return { escaped: false, iter: maxIter };
}
```

---

### 3.2. Hệ Hấp Dẫn Hỗn Loạn Lorenz (The Lorenz Attractor)

Edward Lorenz (1963) phát hiện ra hệ phương trình vi phân mô hình hóa đối lưu khí quyển:
$$\begin{cases}
\frac{dx}{dt} = \sigma (y - x) \\
\frac{dy}{dt} = x (\rho - z) - y \\
\frac{dz}{dt} = x y - \beta z
\end{cases}$$

Với các tham số kinh điển: $\sigma = 10$, $\rho = 28$, $\beta = \frac{8}{3}$.

- **Tính chất**: Quỹ đạo 3D không bao giờ tự cắt chính nó, tạo thành hình đôi cánh bướm kỳ vĩ với số chiều Hausdorff fractal $D \approx 2.06$.
- **Hiệu ứng cánh bướm (Butterfly Effect)**: Hai điều kiện ban đầu lệch nhau chỉ $10^{-6}$ sau một khoảng thời gian ngắn sẽ dẫn tới hai quỹ đạo hoàn toàn tách biệt.
- **Triển khai trong Three.js (`ThreeDLabView.tsx`)**: Dùng RK4 tính liên tục 50,000 điểm quỹ đạo và render bằng `THREE.LineSegments` hoặc `THREE.Points` với gradient màu sắc theo vận tốc $v = \|\frac{d\vec{r}}{dt}\|$.

---

## 4. MA TRẬN ỨNG DỤNG VÀO PHÒNG THÍ NGHIỆM AISTEM

| Chủ đề thuật toán | Mô hình minh họa tương tác | Vị trí component AIstem | Tác động giáo dục |
|---|---|---|---|
| **Cubic Bézier & Tangents** | Kéo thả 4 điểm điều khiển, hiện tiếp tuyến tức thời | `VectorStudioView.tsx` | Hiểu bản chất đạo hàm tiếp tuyến và đường cong vector |
| **Giao điểm Euclid** | Dựng tam giác đều, đường trung trực, phân giác góc | `GeometryPuzzleArenaView.tsx` | Học sinh tự tay giải đố hình học bằng compa thước kẻ |
| **Bảng Galton & CLT** | Rơi 500 hạt bi qua 16 tầng đinh tạo đường chuông | `MathEngineStudioView.tsx` | Trực quan hóa quy luật số lớn và phân phối xác suất |
| **Fractal Mandelbrot** | Zoom vô cực vào viền hoa tuyết của tập số phức | `MathEngineStudioView.tsx` | Cảm nhận vẻ đẹp kỳ vĩ giữa hình học và số phức |
| **Hệ Lorenz Attractor** | Xoay quỹ đạo 3D cánh bướm trong không gian pha | `ThreeDLabView.tsx` | Khám phá lý thuyết hỗn loạn và cơ học phi tuyến |
