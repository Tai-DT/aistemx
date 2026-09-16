# 🧬 CHUYÊN ĐỀ 4: CÁC KỲ THI OLYMPIAD SINH HỌC (IBO, USABO, VBO)

Tài liệu này phân tích cấu trúc bài thi lý thuyết, 4 trạm thực hành phòng thí nghiệm chuẩn quốc tế và các dạng bài toán sinh học định lượng của **IBO** và **USABO**.

---

## 1. OLYMPIC SINH HỌC QUỐC TẾ (IBO - INTERNATIONAL BIOLOGY OLYMPIAD)

### 1.1. Cấu Trúc Đề Thi Cân Bằng 50% Lý Thuyết – 50% Thực Hành
IBO là kỳ thi khoa học duy nhất duy trì tỉ lệ điểm thực hành thực nghiệm lên tới **50%**:

```
                                  KỲ THI IBO
                                       │
                ┌──────────────────────┴──────────────────────┐
                ▼                                             ▼
    1. BÀI THI THỰC HÀNH (50%)                    2. BÀI THI LÝ THUYẾT (50%)
    - Gồm 4 trạm Lab (mỗi trạm 90 phút)           - Thi trên máy tính trong 2 buổi:
      1. Tế bào & Sinh học phân tử                  + Buổi A (khoảng 3 giờ)
      2. Giải phẫu & Sinh lý thực vật               + Buổi B (khoảng 3 giờ)
      3. Giải phẫu & Sinh lý động vật             - Câu hỏi dạng Đúng/Sai phức hợp
      4. Hệ thống học, Sinh thái & Tin sinh         (4 mệnh đề cho mỗi tình huống)
```

### 1.2. Chi Tiết 4 Trạm Thực Hành Thí Nghiệm Tiêu Chuẩn
1. **Trạm 1: Sinh học tế bào & Sinh học phân tử (Cell & Molecular Biology)**:
   - Thao tác dùng micropipette chính xác đến microlit ($\mu\text{L}$).
   - Kỹ thuật điện di gel agarose (Gel Electrophoresis) phân tích kích thước đoạn ADN sau khi cắt bằng enzyme giới hạn (Restriction Endonuclease).
   - Đo quang phổ mật độ protein (Bradford assay) hoặc đo hoạt tính enzyme xúc tác.
2. **Trạm 2: Giải phẫu & Sinh lý thực vật (Plant Anatomy & Physiology)**:
   - Cắt tiêu bản thực vật bằng dao cạo tay (Hand-microtome sectioning) để thu được lát cắt mỏng cỡ 1–2 lớp tế bào.
   - Nhuộm màu kép (Double staining với phẩm nhuộm xanh metylen / đỏ son carmine) để phân biệt mô gỗ (lignin bắt màu xanh) và mô rây (cellulose bắt màu hồng).
   - Soi dưới kính hiển vi quang học, đếm mật độ khí khổng và vẽ sơ đồ giải phẫu học sinh học chuẩn xác.
3. **Trạm 3: Giải phẫu & Sinh lý động vật (Animal Anatomy & Physiology)**:
   - Mổ và giải phẫu các mẫu động vật không xương sống hoặc tiêu bản chuẩn.
   - Đo điện thế hoạt động cơ (electromyography) hoặc xác định nhóm máu và kháng thể.
4. **Trạm 4: Hệ thống học, Sinh thái & Tin sinh học (Biosystematics & Bioinformatics)**:
   - Xây dựng cây phân loại phát sinh chủng loại (Cladogram / Phylogenetic Tree) dựa trên ma trận tính trạng hoặc ma trận khoảng cách di truyền.
   - Sử dụng công cụ tin sinh học (BLAST) đối chiếu chuỗi trình tự axit amin và nucleotide.

---

## 2. MA TRẬN TRỌNG SỐ KIẾN THỨC LÝ THUYẾT IBO

| Phân môn | Tỉ trọng | Các chủ đề trọng tâm |
|---|---|---|
| **Sinh học tế bào & Hóa sinh** | **20%** | Cấu trúc màng, ty thể, chu trình Krebs, quang hợp, tín hiệu tế bào |
| **Giải phẫu & Sinh lý thực vật** | **15%** | Vận chuyển dòng mạch gỗ/rây, hormone thực vật (Auxin, Gibberellin), quang chu kỳ |
| **Giải phẫu & Sinh lý động vật** | **25%** | Hệ thần kinh, nội tiết, tuần hoàn, miễn dịch, bài tiết và điều hòa nội môi |
| **Di truyền học & Tiến hóa** | **20%** | Di truyền Men-đen, phả hệ, liên kết gen, đột biến, định luật Hardy-Weinberg |
| **Sinh thái học & Hành vi** | **15%** | Tăng trưởng quần thể logistic, lưới thức ăn, tập tính học động vật |
| **Hệ thống học sinh giới** | **5%** | Cây phát sinh loài, đặc trưng các ngành động vật và thực vật |

---

## 3. BÀI TOÁN MẪU ĐỊNH LƯỢNG: DI TRUYỀN QUẦN THỂ & HARDY-WEINBERG
> **Đề bài**: Trong một quần thể ngẫu phối, xét một gen có 2 alen $A$ và $a$. Tần số alen $A$ là $p = 0.7$, tần số alen $a$ là $q = 0.3$. Nếu kiểu hình lặn $aa$ bị chọn lọc tự nhiên đào thải với hệ số chọn lọc $s = 0.2$ sau mỗi thế hệ, hãy tính tần số alen $a$ ở thế hệ kế tiếp.

#### Lời giải chi tiết:
1. Thành phần kiểu gen ban đầu trước chọn lọc (cân bằng Hardy-Weinberg):
   $$f(AA) = p^2 = 0.7^2 = 0.49$$
   $$f(Aa) = 2pq = 2 \times 0.7 \times 0.3 = 0.42$$
   $$f(aa) = q^2 = 0.3^2 = 0.09$$
2. Độ thích nghi (Fitness $W$) của các kiểu gen:
   $$W_{AA} = 1, \quad W_{Aa} = 1, \quad W_{aa} = 1 - s = 1 - 0.2 = 0.8$$
3. Độ thích nghi trung bình của cả quần thể $\bar{W}$:
   $$\bar{W} = p^2 W_{AA} + 2pq W_{Aa} + q^2 W_{aa} = 0.49 \times 1 + 0.42 \times 1 + 0.09 \times 0.8 = 0.91 + 0.072 = 0.982$$
4. Tần số alen $a$ ở thế hệ kế tiếp ($q'$):
   $$q' = \frac{pq W_{Aa} + q^2 W_{aa}}{\bar{W}} = \frac{0.21 \times 1 + 0.072}{0.982} = \frac{0.282}{0.982} \approx 0.2872$$
5. Nhận xét: Dưới áp lực chọn lọc đào thải $s = 0.2$, tần số alen lặn $a$ đã giảm từ $0.3000$ xuống còn $0.2872$ chỉ sau một thế hệ.
