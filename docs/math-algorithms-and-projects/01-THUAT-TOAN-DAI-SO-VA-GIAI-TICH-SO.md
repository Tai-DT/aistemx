# 🔢 CHUYÊN ĐỀ 1: THUẬT TOÁN ĐẠI SỐ TUYẾN TÍNH VÀ GIẢI TÍCH SỐ

Tài liệu này cung cấp lý thuyết toán học chuyên sâu, thuật toán số (numerical algorithms) và mã nguồn chuẩn hóa (Python + TypeScript) cho các bài toán đại số tuyến tính, giải tích và phương trình vi phân ứng dụng trong **AIstem**.

---

## 1. ĐẠI SỐ TUYẾN TÍNH & MA TRẬN (LINEAR ALGEBRA)

### 1.1. Biến Đổi Tuyến Tính & Ma Trận 2D/3D (Linear & Affine Transformations)

Biến đổi tuyến tính trong không gian $\mathbb{R}^2$ ánh xạ mọi vectơ $\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}$ sang vectơ mới $\vec{v}'$:
$$T(\vec{v}) = A \vec{v} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} ax + by \\ cx + dy \end{pmatrix}$$

- **Định thức $\det(A) = ad - bc$**: Biểu thị **tỉ lệ thay đổi diện tích** (hoặc thể tích trong $\mathbb{R}^3$) của một hình sau biến đổi. Nếu $\det(A) = 0$, không gian bị suy biến (bẹp lại thành một đường thẳng hoặc điểm).
- **Mã TypeScript biến đổi điểm trực tiếp trên Canvas**:

```typescript
export interface Matrix2x2 {
  a: number; b: number;
  c: number; d: number;
}

export function transformPoint(m: Matrix2x2, x: number, y: number): { x: number; y: number } {
  return {
    x: m.a * x + m.b * y,
    y: m.c * x + m.d * y
  };
}

export function determinant(m: Matrix2x2): number {
  return m.a * m.d - m.b * m.c;
}
```

---

### 1.2. Trị Riêng & Vectơ Riêng (Eigenvalues & Eigenvectors)

#### Định nghĩa Toán học
Cho ma trận vuông $A \in \mathbb{R}^{n \times n}$. Một vectơ khác không $\vec{v}$ được gọi là **vectơ riêng** tương ứng với **trị riêng** $\lambda$ nếu:
$$A \vec{v} = \lambda \vec{v} \iff (A - \lambda I)\vec{v} = \vec{0}$$

Để tồn tại nghiệm không tầm thường, phương trình đặc trưng phải thỏa mãn:
$$\det(A - \lambda I) = 0$$

Đối với ma trận $2 \times 2$:
$$\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0 \quad \text{với } \text{tr}(A) = a + d, \; \det(A) = ad - bc$$

#### Thuật toán Lặp Lũy Thừa (Power Iteration Algorithm)
Dùng để tìm trị riêng có độ lớn cực đại $\lambda_{\max}$ và vectơ riêng tương ứng mà không cần giải đa thức đặc trưng:

```python
import numpy as np

def power_iteration(A: np.ndarray, num_simulations: int = 100, eps: float = 1e-9):
    n = A.shape[0]
    # Khởi tạo vector ngẫu nhiên chuẩn hóa
    b_k = np.random.rand(n)
    b_k = b_k / np.linalg.norm(b_k)

    for _ in range(num_simulations):
        # Tính A * b_k
        b_k1 = np.dot(A, b_k)
        norm = np.linalg.norm(b_k1)
        if norm < eps:
            break
        b_k1 = b_k1 / norm
        if np.allclose(b_k, b_k1, atol=eps):
            break
        b_k = b_k1

    # Ước lượng trị riêng bằng Rayleigh Quotient: lambda = (b^T A b) / (b^T b)
    eigenvalue = np.dot(b_k.T, np.dot(A, b_k)) / np.dot(b_k.T, b_k)
    return float(eigenvalue), b_k
```

---

### 1.3. Phân Rã Giá Trị Kỳ Dị (Singular Value Decomposition - SVD)

Mọi ma trận thực $A \in \mathbb{R}^{m \times n}$ đều có thể phân tích thành:
$$A = U \Sigma V^T$$
Trong đó:
- $U \in \mathbb{R}^{m \times m}$ là ma trận trực giao ($U^T U = I$) chứa các vectơ kỳ dị trái.
- $\Sigma \in \mathbb{R}^{m \times n}$ là ma trận đường chéo chứa các giá trị kỳ dị $\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$.
- $V \in \mathbb{R}^{n \times n}$ là ma trận trực giao ($V^T V = I$) chứa các vectơ kỳ dị phải.

**Ứng dụng trong AIstem**:
- **Nén ảnh & ma trận**: Xấp xỉ hạng thấp $A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$ giúp học sinh thấy trực quan cách một bức ảnh $512 \times 512$ được phục hồi từ $k=5, 10, 20$ giá trị kỳ dị.
- **PCA (Phân tích thành phần chính)**: Giảm chiều dữ liệu khoa học để vẽ đồ thị phân cụm mẫu vật trong Biology Lab.

---

## 2. GIẢI TÍCH SỐ & PHƯƠNG TRÌNH VI PHÂN (NUMERICAL METHODS & ODES)

### 2.1. Tìm Nghiệm Phương Trình Phi Tuyến: Newton-Raphson

Tìm nghiệm của phương trình $f(x) = 0$ từ xấp xỉ tuyến tính tiếp tuyến:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

```typescript
export function newtonRaphson(
  f: (x: number) => number,
  df: (x: number) => number,
  x0: number,
  tol: number = 1e-7,
  maxIter: number = 100
): { root: number; iterations: number; history: number[] } {
  let x = x0;
  const history = [x];
  for (let i = 0; i < maxIter; i++) {
    const fx = f(x);
    if (Math.abs(fx) < tol) {
      return { root: x, iterations: i, history };
    }
    const dfx = df(x);
    if (Math.abs(dfx) < 1e-12) {
      throw new Error("Đạo hàm xấp xỉ 0, không thể tiếp tục tiếp tuyến");
    }
    x = x - fx / dfx;
    history.push(x);
  }
  return { root: x, iterations: maxIter, history };
}
```

---

### 2.2. Giải Phương Trình Vi Phân Thường (ODEs): Runge-Kutta Bậc 4 (RK4)

Hầu hết các hệ chuyển động cơ học trong vật lý (con lắc đơn, dao động có ma sát, tương tác hấp dẫn hành tinh) đều được mô tả bằng hệ phương trình vi phân cấp 1:
$$\frac{d\vec{y}}{dt} = \vec{f}(t, \vec{y})$$

Phương pháp Euler thường phân kỳ rất nhanh do sai số $O(\Delta t)$. **Runge-Kutta bậc 4 (RK4)** là thuật toán chuẩn mực vàng với sai số tích lũy chỉ $O(\Delta t^4)$:
$$\vec{y}_{n+1} = \vec{y}_n + \frac{\Delta t}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$
với:
$$k_1 = \vec{f}(t_n, \vec{y}_n)$$
$$k_2 = \vec{f}\left(t_n + \frac{\Delta t}{2}, \vec{y}_n + \frac{\Delta t}{2}k_1\right)$$
$$k_3 = \vec{f}\left(t_n + \frac{\Delta t}{2}, \vec{y}_n + \frac{\Delta t}{2}k_2\right)$$
$$k_4 = \vec{f}(t_n + \Delta t, \vec{y}_n + \Delta t k_3)$$

#### Code RK4 cho Con Lắc Đơn Phi Tuyến ($\ddot{\theta} + \frac{g}{L}\sin\theta = 0$):
```typescript
export interface PendulumState {
  theta: number; // Góc lệch (rad)
  omega: number; // Vận tốc góc (rad/s)
}

export function rk4PendulumStep(
  state: PendulumState,
  dt: number,
  g: number = 9.81,
  L: number = 1.0,
  damping: number = 0.05
): PendulumState {
  const f = (s: PendulumState): { dTheta: number; dOmega: number } => ({
    dTheta: s.omega,
    dOmega: -(g / L) * Math.sin(s.theta) - damping * s.omega
  });

  // k1
  const k1 = f(state);

  // k2
  const s_k2: PendulumState = {
    theta: state.theta + 0.5 * dt * k1.dTheta,
    omega: state.omega + 0.5 * dt * k1.dOmega
  };
  const k2 = f(s_k2);

  // k3
  const s_k3: PendulumState = {
    theta: state.theta + 0.5 * dt * k2.dTheta,
    omega: state.omega + 0.5 * dt * k2.dOmega
  };
  const k3 = f(s_k3);

  // k4
  const s_k4: PendulumState = {
    theta: state.theta + dt * k3.dTheta,
    omega: state.omega + dt * k3.dOmega
  };
  const k4 = f(s_k4);

  return {
    theta: state.theta + (dt / 6) * (k1.dTheta + 2 * k2.dTheta + 2 * k3.dTheta + k4.dTheta),
    omega: state.omega + (dt / 6) * (k1.dOmega + 2 * k2.dOmega + 2 * k3.dOmega + k4.dOmega)
  };
}
```

---

### 2.3. Tích Phân Số: Cầu Phương Simpson 1/3 & Gauss-Legendre

Để tính $\int_a^b f(x) dx$ mà không tìm được nguyên hàm sơ cấp:

#### Công thức Simpson 1/3:
Chia khoảng $[a, b]$ thành $N$ đoạn con chẵn ($N = 2m$):
$$\int_a^b f(x) dx \approx \frac{h}{3} \left[ f(x_0) + 4\sum_{i=1,3,\dots}^{N-1} f(x_i) + 2\sum_{i=2,4,\dots}^{N-2} f(x_i) + f(x_N) \right]$$
với $h = \frac{b - a}{N}$.

#### Cầu phương Gauss-Legendre 3 điểm (Độ chính xác đại số bậc 5):
Đổi biến từ $[a, b]$ về $[-1, 1]$:
$$\int_a^b f(x)dx = \frac{b - a}{2} \int_{-1}^1 f\left(\frac{b-a}{2}t + \frac{a+b}{2}\right) dt \approx \frac{b-a}{2} \left[ \frac{5}{9}f\left(-\sqrt{\frac{3}{5}}\right) + \frac{8}{9}f(0) + \frac{5}{9}f\left(\sqrt{\frac{3}{5}}\right) \right]$$

---

## 3. GIẢI TÍCH FOURIER & XỬ LÝ TÍN HIỆU (FOURIER ANALYSIS)

### 3.1. Chuỗi Fourier & Hoạt Họa Epicycles (3Blue1Brown Style)

Mọi hàm tuần hoàn $f(t)$ chu kỳ $T = \frac{2\pi}{\omega}$ đều có thể khai triển thành tổng vô hạn của các hàm điều hòa cơ bản:
$$f(t) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega t) + b_n \sin(n\omega t) \right]$$

Hoặc dưới dạng số phức:
$$f(t) = \sum_{n=-\infty}^{\infty} c_n e^{i n \omega t}, \quad c_n = \frac{1}{T} \int_0^T f(t) e^{-i n \omega t} dt$$

#### Ý nghĩa trực quan hình học:
Mỗi số hạng $c_n e^{i n \omega t}$ là một **vectơ quay** (vòng tròn quay với tần số góc $n\omega$ và bán kính $|c_n|$). Khi nối đầu mút của vòng tròn này vào tâm của vòng tròn tiếp theo, đầu mút cuối cùng sẽ vẽ ra đường viền chính xác của bất kỳ hình dạng nào (tương tự như màn Epicycles trong `MathEngineStudioView.tsx`).

### 3.2. Thuật toán Biến Đổi Fourier Nhanh (Cooley-Tukey FFT)
Giảm độ phức tạp tính toán từ $O(N^2)$ của DFT trực tiếp xuống $O(N \log N)$ bằng chiến lược chia để trị (chia mảng thành chỉ số chẵn và lẻ):

```python
import cmath

def fft(x: list[complex]) -> list[complex]:
    N = len(x)
    if N <= 1:
        return x
    if (N & (N - 1)) != 0:
        raise ValueError("Chiều dài mảng N phải là lũy thừa của 2")
        
    even = fft(x[0::2])
    odd = fft(x[1::2])
    
    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]
```

---

## 4. BẢNG TỔNG HỢP SO SÁNH HIỆU NĂNG VÀ ĐỘ CHÍNH XÁC

| Thuật toán | Lĩnh vực | Độ phức tạp | Sai số ước lượng | Ứng dụng cụ thể trong AIstem |
|---|---|---|---|---|
| **Power Iteration** | Trị riêng ma trận | $O(k \cdot n^2)$ | Phụ thuộc tỉ số $|\lambda_2 / \lambda_1|$ | Khảo sát ma trận biến đổi trong Math Studio |
| **SVD Truncated** | Đại số ma trận | $O(m \cdot n \cdot k)$ | Tối ưu ma trận Frobenius | Nén dữ liệu ảnh phổ & Giảm chiều PCA |
| **Newton-Raphson** | Tìm nghiệm phi tuyến | $O(k)$ (Hội tụ bậc 2) | $|\epsilon_{n+1}| \le C |\epsilon_n|^2$ | Giải phương trình giao điểm & Cân bằng hóa học |
| **RK4 Integration** | Phương trình vi phân | $O(N)$ bước | Cục bộ $O(h^5)$, Toàn cục $O(h^4)$ | Mô phỏng con lắc, quỹ đạo đạn đạo, mạch RLC |
| **Simpson 1/3** | Tích phân số | $O(N)$ | $O(h^4)$ | Tính công cơ học $W = \int F dx$, điện tích $Q = \int I dt$ |
| **Cooley-Tukey FFT** | Phân tích tần số | $O(N \log N)$ | Chính xác số học chuẩn IEEE 754 | Biểu diễn sóng âm, phổ quang học, Epicycles |
