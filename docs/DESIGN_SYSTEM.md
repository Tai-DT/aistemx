# Open Design System: AISTEM Modern STEM Platform

Hệ thống thiết kế mở (Open Design System) cho nền tảng Tri thức và Luyện thi STEM Quốc tế AISTEM.

---

## 1. Triết lý Thiết kế (Design Philosophy)
1. **Mathematical Precision & Clarity**: Đảm bảo công thức $\LaTeX$, biểu đồ 2D và mô hình 3D hiển thị rõ nét, sắc sảo ở mọi độ phân giải.
2. **Immersive Dark-First Aesthetic**: Nền tối sâu (`#0b0f19`) kết hợp hiệu ứng Glassmorphism và viền phản quang (`glow`) giúp học sinh tập trung tối đa và giảm mỏi mắt.
3. **Cognitive Ergonomics**: Phân cấp thị giác rõ ràng qua huy hiệu môn học (Màu sắc chuẩn hóa), thanh điều hướng tức thì và phản hồi tương tác mượt mà.

---

## 2. Bảng Màu Chuẩn Hóa (Color Palette & Tokens)

### Màu Nền & Khung Chứa
- `--bg-primary`: `#0b0f19` (Nền chính Dark Mode) / `#f8fafc` (Light Mode)
- `--bg-secondary`: `#111827` (Sidebar & Header) / `#ffffff` (Light Mode)
- `--bg-card`: `rgba(30, 41, 59, 0.7)` (Thẻ kính mờ Glassmorphism)
- `--border-color`: `rgba(255, 255, 255, 0.1)` / `#e2e8f0` (Light Mode)

### Màu Nhận Diện 4 Trụ Cột STEM
| Trụ cột | Tên biến | Mã màu Dark | Mã màu Light | Ý nghĩa nhận diện |
| :--- | :--- | :--- | :--- | :--- |
| 📐 **Toán học** | `--accent-blue` | `#3b82f6` (`#60a5fa`) | `#2563eb` | Logic, cấu trúc, không gian |
| ⚡ **Vật lí** | `--accent-purple` | `#8b5cf6` (`#c084fc`) | `#7c3aed` | Năng lượng, điện từ trường, lượng tử |
| 🧪 **Hoá học** | `--accent-emerald` | `#10b981` (`#34d399`) | `#059669` | Cấu tạo chất, phản ứng, liên kết |
| 🧬 **Sinh học** | `--accent-rose` | `#f43f5e` (`#fb7185`) | `#e11d48` | Sự sống, di truyền học, sinh thái |

---

## 3. Typography & Mathematical Typesetting
- **Phông chữ giao diện chính**: `'Inter', sans-serif` (Trọng lượng: 400 Regular, 500 Medium, 600 SemiBold, 700 Bold, 800 ExtraBold).
- **Phông chữ mã nguồn & ID**: `'JetBrains Mono', 'Fira Code', monospace`.
- **Bộ kết xuất công thức toán học**: `KaTeX` với CSS tùy biến cân đối độ cao dòng (`line-height: 1.6`) và căn giữa các khối phương trình lớn.

---

## 4. Thư viện Thành phần Cốt lõi (Core Components)

### 1. Stat Card (Thẻ Thống kê)
```css
.stat-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 16px;
  padding: 24px;
  backdrop-filter: blur(8px);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.stat-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 0 25px rgba(59, 130, 246, 0.25);
}
```

### 2. Formula Card & KaTeX Box
Khung hiển thị công thức với nền tối mờ `rgba(0, 0, 0, 0.25)`, bo tròn `10px`, tự động cuộn ngang khi công thức $\LaTeX$ quá dài.

### 3. 3D WebGL Canvas Stage
Khung hình Three.js phản hồi thời gian thực với tỷ lệ hiển thị $100\%$ chiều cao linh hoạt, ánh sáng môi trường Ambient + Directional Light và điều khiển quỹ đạo OrbitControls.

### 4. Admin Management Data Tables & Filters
Bảng dữ liệu quản trị với hàng xen kẽ, bộ lọc tức thì theo môn/cấp học, phân trang trực quan và huy hiệu trạng thái (Status Badges).
