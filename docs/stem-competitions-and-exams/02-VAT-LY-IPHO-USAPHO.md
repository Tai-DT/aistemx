# ⚡ CHUYÊN ĐỀ 2: CÁC KỲ THI OLYMPIAD VẬT LÝ (IPHO, APHO, F=MA, USAPHO)

Tài liệu này phân tích cấu trúc, ma trận chủ đề thi, mẹo giải nhanh thứ nguyên và bài toán mẫu của các kỳ thi Vật lý danh tiếng: **IPhO**, **F=ma Contest**, và **USAPhO**.

---

## 1. OLYMPIC VẬT LÝ QUỐC TẾ (IPHO & APHO)

### 1.1. Cấu Trúc Hai Ngày Thi Kinh Điển
IPhO gồm 2 bài thi cách nhau 1 ngày nghỉ trọn vẹn:

| Phần thi | Thời gian | Số lượng bài | Điểm tối đa | Trọng số | Đặc trưng khảo sát |
|---|---|---|---|---|---|
| **Lý thuyết (Theoretical)** | 5 giờ | 3 bài toán lớn | 30 điểm | 60% | Bài toán vật lý hiện đại, giải thích hiện tượng tự nhiên bằng mô hình toán |
| **Thực nghiệm (Experimental)** | 5 giờ | 1 – 2 bài Lab | 20 điểm | 40% | Thiết kế mạch, đo đạc dữ liệu thực, vẽ đồ thị tuyến tính hóa, phân tích sai số |
| **Tổng cộng** | **10 giờ** | **4 – 5 bài** | **50 điểm** | **100%** | Huy chương Vàng: Top 8–12% điểm cao nhất |

### 1.2. Ma Trận Nội Dung IPhO Syllabus
1. **Cơ học nâng cao**: Động lực học vật rắn, tenxơ quán tính, hệ quy chiếu phi quán tính (lực quán tính ly tâm & Coriolis), cơ học chất lưu nhớt Navier-Stokes sơ cấp.
2. **Điện từ trường & Điện động lực học**: Định luật Gauss, định luật Ampère-Maxwell, sóng điện từ, lưỡng cực điện/từ, phương trình truyền sóng trong dây dẫn và ống dẫn sóng.
3. **Nhiệt học & Vật lý thống kê**: Khí thực Van der Waals, chu trình Carnot, hàm entropy vi phân, phân bố Maxwell-Boltzmann.
4. **Quang học & Sóng**: Giao thoa nhiều khe, nhiễu xạ Fresnel và Fraunhofer, phân cực ánh sáng (định luật Malus, bản lưỡng chiết).
5. **Vật lý hiện đại & Lượng tử**: Thuyết tương đối hẹp (phép biến đổi Lorentz, hệ thức Einstein $E^2 = p^2 c^2 + m_0^2 c^4$), mô hình nguyên tử Bohr, hiệu ứng quang điện và tán xạ Compton.

---

## 2. KỲ THI F=MA CONTEST (AAPT - HOA KỲ)

### 2.1. Cấu Trúc & Quy Chế
- **Đơn vị tổ chức**: Hiệp hội Giáo viên Vật lý Hoa Kỳ (**AAPT**).
- **Quy mô**: Vòng 1 tuyển chọn đội tuyển Vật lý Hoa Kỳ (khoảng 400 thí sinh điểm cao nhất sẽ bước vào bán kết USAPhO).
- **Thời gian**: **75 phút**.
- **Số lượng câu hỏi**: **25 câu trắc nghiệm** khách quan.
- **Phạm vi kiến thức**: **100% CƠ HỌC CỔ ĐIỂN (Newtonian Mechanics)**. Không có Điện, Quang, Nhiệt hay Vật lý lượng tử.
- **Quy chế tính điểm**:
  - Đúng: $+1$ điểm.
  - Sai hoặc bỏ trống: $0$ điểm.
  - **KHÔNG BỊ TRỪ ĐIỂM KHI ĐOÁN SAI** $\implies$ Phải đánh dấu toàn bộ 25 câu trước khi hết giờ!

### 2.2. Chiến Thuật Đột Phá: Phân Tích Thứ Nguyên & Giới Hạn Cực Trị
Kỳ thi F=ma có áp lực thời gian cực lớn (trung bình chỉ 3 phút/câu). Các chuyên gia Olympic thường dùng 2 "vũ khí bí mật" để loại trừ phương án:

#### 1. Phân tích thứ nguyên (Dimensional Analysis)
- Kiểm tra đơn vị của 5 đáp án. Nếu đề bài hỏi vận tốc ($[v] = \text{m/s}$), mọi đáp án có thứ nguyên khác $\text{m/s}$ (ví dụ $\sqrt{g/h}$ có thứ nguyên $\text{s}^{-1}$) bị gạch bỏ ngay lập tức trong 5 giây!

#### 2. Xét trường hợp giới hạn cực trị (Limiting Cases)
- Cho góc nghiêng $\theta \to 0$ hoặc $\theta \to 90^\circ$.
- Cho khối lượng $m \to 0$ hoặc $m \to \infty$.
- Đáp án đúng bắt buộc phải thỏa mãn trực giác vật lý tại các điểm kỳ dị này.

### 2.3. Bài Toán Mẫu Điển Hình: Con Lắc Đặt Trong Thang Máy Gia Tốc
> **Đề bài**: Một con lắc đơn có chiều dài $L$, vật nặng khối lượng $m$ được treo trên trần của một toa tàu đang chuyển động với gia tốc nằm ngang không đổi $a$. Tìm chu kỳ dao động nhỏ của con lắc.
> - A. $T = 2\pi \sqrt{\frac{L}{g}}$
> - B. $T = 2\pi \sqrt{\frac{L}{g + a}}$
> - C. $T = 2\pi \sqrt{\frac{L}{\sqrt{g^2 + a^2}}}$
> - D. $T = 2\pi \sqrt{\frac{L}{g - a}}$
> - E. $T = 2\pi \sqrt{\frac{L}{\sqrt{g^2 - a^2}}}$

#### Phân tích chớp nhoáng bằng trường hợp giới hạn:
1. Khi tàu đứng yên ($a = 0$): Chu kỳ phải trở về công thức con lắc quen thuộc $T = 2\pi \sqrt{L/g}$. Cả 5 phương án đều thỏa mãn điều kiện này.
2. Xét trường hợp gia tốc cực lớn ($a \to \infty$): Lực quán tính $F_{qt} = ma$ kéo dạt con lắc cực mạnh $\implies$ Gia tốc trọng trường hiệu dụng tăng vọt $\implies$ Con lắc dao động cực nhanh $\implies$ Chu kỳ $T$ phải giảm về 0 và phải tồn tại nghiệm thực với mọi $a > g$.
   - Phương án E bị loại vì khi $a > g$, biểu thức dưới căn bậc hai bị âm.
3. Vì gia tốc $\vec{a}$ nằm ngang vuông góc với trọng lực $\vec{g}$ hướng thẳng đứng xuống dưới:
   $$\vec{g}_{eff} = \vec{g} - \vec{a} \implies g_{eff} = \sqrt{g^2 + a^2}$$
4. Chu kỳ dao động nhỏ là:
   $$T = 2\pi \sqrt{\frac{L}{g_{eff}}} = 2\pi \sqrt{\frac{L}{\sqrt{g^2 + a^2}}}$$
$\implies$ **Chọn đáp án C**.

---

## 3. KỲ THI USAPHO (USA PHYSICS OLYMPIAD SEMIFINAL)

### 3.1. Cấu Trúc Đề Thi
- Gồm 2 phần thi tự luận trong 3 giờ:
  - **Part A (90 phút)**: 3 bài toán tự luận đa bước.
  - **Part B (90 phút)**: 3 bài toán tự luận sâu, thường có 1 bài xử lý số liệu thực nghiệm và đồ thị logarit.
- Phủ rộng toàn bộ các phân môn: Cơ học Lagrange sơ cấp, trường tĩnh điện Poisson, cảm ứng điện từ Faraday, thấu kính ghép phức tạp và nhiệt động học Carnot.
