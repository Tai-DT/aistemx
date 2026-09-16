# 📐 CHUYÊN ĐỀ 1: CÁC KỲ THI OLYMPIAD TOÁN HỌC & TIN HỌC (IMO, AMC, AIME, SASMO, IOI)

Tài liệu này phân tích chi tiết cấu trúc, ma trận nội dung, chiến lược làm bài và các bài toán mẫu kinh điển của các cuộc thi Toán học và Tin học thuật toán danh giá nhất thế giới.

---

## 1. OLYMPIC TOÁN HỌC QUỐC TẾ (IMO - INTERNATIONAL MATHEMATICAL OLYMPIAD)

### 1.1. Cấu Trúc Đề Thi & Barem Chấm Điểm
- **Thời gian**: Thi trong **2 ngày liên tiếp**, mỗi ngày **4 giờ 30 phút** (270 phút).
- **Số lượng câu hỏi**: **6 bài toán tự luận** (Ngày 1: Bài 1, 2, 3; Ngày 2: Bài 4, 5, 6).
- **Thang điểm**: Mỗi bài tối đa **7 điểm** $\implies$ Tổng điểm tuyệt đối là **42 điểm**.
- **Quy tắc xếp giải**:
  - Huy chương Vàng, Bạc, Đồng được trao theo tỉ lệ xấp xỉ $1 : 2 : 3$.
  - Khoảng 50% tổng số thí sinh tham gia được nhận huy chương. Thí sinh không đạt huy chương nhưng đạt 7/7 điểm trọn vẹn ở ít nhất một bài thi sẽ nhận giải Khuyến khích (Honorable Mention).
- **Dụng cụ cho phép**: Compa và thước kẻ không chia độ. **Tuyệt đối cấm** máy tính bỏ túi và mọi tài liệu.

### 1.2. Bốn Trụ Cột Kiến Thức Cốt Lõi (Four Pillars)
IMO không yêu cầu giải tích vi tích phân (Calculus), đại số tuyến tính ma trận hay xác suất đại học, nhưng đòi hỏi sự sáng tạo và tư duy chiều sâu tột bậc ở 4 phân môn sơ cấp:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        BỐN PHÂN MÔN IMO TOÁN HỌC                      │
├──────────────────────────────────┬─────────────────────────────────────┤
│ 1. ĐẠI SỐ (Algebra)              │ 2. HÌNH HỌC PHẲNG (Geometry)        │
│ - Bất đẳng thức (AM-GM, Cauchy)  │ - Hình học Euclid thuần túy         │
│ - Phương trình hàm (Cauchy, v.v) │ - Phương tích & Trục đẳng phương    │
│ - Đa thức, Dãy số & Giới hạn sơ  │ - Biến hình, Tọa độ tỉ cự, Nghịch đảo│
├──────────────────────────────────┼─────────────────────────────────────┤
│ 3. SỐ HỌC (Number Theory)        │ 4. TỔ HỢP (Combinatorics)           │
│ - Bổ đề nâng lũy thừa LTE        │ - Nguyên lý Dirichlet, Bất biến     │
│ - Định lý Thặng dư Trung Hoa     │ - Lý thuyết đồ thị, Quy hoạch rời rạc│
│ - Phương trình Diophantine       │ - Trò chơi toán học & Phân hoạch tập │
└──────────────────────────────────┴─────────────────────────────────────┘
```

### 1.3. Bài Toán Mẫu Điển Hình: Kỹ Thuật Nhảy Vieta (Vieta Jumping)
> **Đề bài (IMO 1988 - Bài 6)**: Cho $a, b$ là hai số nguyên dương sao cho $ab + 1$ là ước của $a^2 + b^2$. Chứng minh rằng biểu thức $k = \frac{a^2 + b^2}{ab + 1}$ là một số chính phương.

#### Lời giải chi tiết từng bước:
1. Giả sử tồn tại số nguyên dương $k$ không phải là số chính phương sao cho phương trình $\frac{a^2 + b^2}{ab + 1} = k$ có nghiệm nguyên dương.
2. Viết lại thành phương trình bậc hai theo biến $a$:
   $$a^2 - (kb)a + (b^2 - k) = 0$$
3. Trong tất cả các cặp nghiệm nguyên dương $(a, b)$, ta chọn cặp $(A, B)$ có tổng $A + B$ **nhỏ nhất** (không mất tính tổng quát, giả sử $A \ge B \ge 1$).
4. Theo định lý Vieta, phương trình bậc hai $x^2 - (kB)x + (B^2 - k) = 0$ có một nghiệm là $x_1 = A$ và nghiệm còn lại là $x_2$:
   $$x_1 + x_2 = kB \implies x_2 = kB - A$$
   $$x_1 \cdot x_2 = B^2 - k \implies x_2 = \frac{B^2 - k}{A}$$
5. Ta chứng minh $x_2$ là số nguyên dương và $x_2 < A$:
   - Do $k$ không là số chính phương nên $B^2 - k \neq 0 \implies x_2 \neq 0$.
   - Nếu $x_2 < 0$, thì $x_2 \le -1$. Khi đó $x_2^2 - (kB)x_2 + (B^2 - k) \ge 1 + kB + B^2 - k > 0$ (mâu thuẫn). Vậy $x_2 > 0$.
   - Ta có $x_2 = \frac{B^2 - k}{A} < \frac{B^2}{A} \le \frac{A^2}{A} = A$.
6. Như vậy cặp nghiệm $(x_2, B)$ là một cặp nghiệm nguyên dương mới có tổng $x_2 + B < A + B$, mâu thuẫn với giả thiết $(A, B)$ là cặp nghiệm có tổng nhỏ nhất.
7. Do đó, $k$ bắt buộc phải là một số chính phương (ĐPCM).

---

## 2. HỆ THỐNG CÁC KỲ THI TOÁN HOA KỲ (AMC 8 / 10 / 12 & AIME)

### 2.1. Cấu Trúc & Quy Chế Tính Điểm Của AMC 10 & AMC 12
- **Thời lượng**: **75 phút**.
- **Hình thức**: **25 câu hỏi trắc nghiệm** khách quan 5 lựa chọn (A, B, C, D, E). Không dùng máy tính.
- **Quy chế tính điểm độc đáo của MAA**:
  - **Câu trả lời đúng**: $+6$ điểm.
  - **Câu bỏ trống (không làm)**: $+1.5$ điểm.
  - **Câu trả lời sai**: $0$ điểm.
  - **Điểm số tối đa**: $25 \times 6 = 150$ điểm.

> [!TIP]
> **Chiến thuật tính điểm kỳ thi AMC**:
> - Nếu bạn hoàn toàn không biết làm và đoán mò ngẫu nhiên (xác suất đúng $1/5 = 20\%$), kỳ vọng điểm số là $0.2 \times 6 + 0.8 \times 0 = 1.2$ điểm $\implies$ **thấp hơn** việc bỏ trống nhận chắc chắn $1.5$ điểm!
> - **Nguyên tắc vàng**: Chỉ nên đoán mò khi đã **loại trừ được ít nhất 2 phương án chắc chắn sai** (khi đó xác suất đúng $\ge 1/3$, kỳ vọng điểm $\ge 2.0 > 1.5$).

### 2.2. Chiến Lược Phân Bổ Thời Gian AMC 10/12 (75 Phút)
- **Câu 1 – 10 (Nền tảng - 20 phút)**: Tốc độ cao, tính toán cẩn thận, không để mất điểm sơ đẳng.
- **Câu 11 – 18 (Phân hóa trung bình - 25 phút)**: Vận dụng biến đổi đại số, giải phương trình, hình học tọa độ.
- **Câu 19 – 25 (Thách thức cao cấp - 30 phút)**: Chọn 2-3 câu thế mạnh nhất để tập trung giải quyết, các câu còn lại cân nhắc bỏ trống để bảo toàn $1.5$ điểm/câu.

### 2.3. Kỳ Thi AIME (American Invitational Mathematics Examination)
- **Đối tượng**: Top 2.5% thí sinh AMC 10 và Top 5% thí sinh AMC 12.
- **Hình thức**: **15 câu hỏi tự luận ngắn**, thí sinh điền đáp số là một số nguyên từ $000$ đến $999$.
- **Thời gian**: **3 giờ** (180 phút). Mỗi câu đúng được 1 điểm, không bị trừ điểm khi sai.

---

## 3. TOÁN ỨNG DỤNG & LOGIC TIỂU HỌC/THCS (KANGAROO & SASMO)

### 3.1. Kỳ Thi Toán Quốc Tế Kangaroo (IKMC)
- **Đặc trưng**: Khác với toán trường lớp, Kangaroo tập trung vào các câu đố hình học không gian, gấp giấy, bánh răng cơ học, quy luật màu sắc và tư duy phản biện.
- **Phân bổ thang điểm**:
  - Phần A: Các câu hỏi 3 điểm (nhận biết, tư duy trực quan nhanh).
  - Phần B: Các câu hỏi 4 điểm (suy luận logic 2-3 bước).
  - Phần C: Các câu hỏi 5 điểm (bài toán tối ưu, đếm tổ hợp phức tạp).

### 3.2. Kỳ Thi SASMO (Singapore and Asian Schools Math Olympiad)
- **Cấu trúc (25 câu - 90 phút)**:
  - **Section A**: 15 câu trắc nghiệm (2 điểm/câu đúng, -1 điểm/câu sai, 0 điểm/bỏ trống).
  - **Section B**: 10 câu trả lời ngắn (4 điểm/câu đúng, 0 điểm/sai hoặc bỏ trống).

---

## 4. OLYMPIC TIN HỌC & TƯ DUY THUẬT TOÁN (IOI & BEBRAS)

### 4.1. Kỳ Thi Bebras (Thử Thách Tư Duy Thuật Toán Không Cần Code)
- Thiết kế cho học sinh từ Tiểu học đến THPT làm quen với các khái niệm khoa học máy tính: đồ thị, cây nhị phân, giải thuật sắp xếp, mã hóa dữ liệu qua các bài toán hình ảnh sinh động.

### 4.2. Kỳ Thi Olympic Tin Học Quốc Tế (IOI)
- **Môi trường lập trình**: C++ (chuẩn C++20), hệ điều hành Linux.
- **Các chuyên đề thuật toán hạt nhân**:
  - **Cấu trúc dữ liệu nâng cao**: Segment Tree (Cây phân đoạn), Fenwick Tree, Trie, Treap, Heavy-Light Decomposition.
  - **Quy hoạch động (Dynamic Programming)**: DP Bitmask, DP Digit, DP trên cây, Tối ưu hóa bao lồi (Convex Hull Trick), Knuth Optimization.
  - **Lý thuyết đồ thị**: Luồng cực đại (Dinic / Push-Relabel), Cặp ghép cực đại (Hopcroft-Karp), Thành phần liên thông mạnh Tarjan.
