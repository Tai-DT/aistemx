# Hoá học — Tổng hợp công thức AISTEM

Tổng số: **826** công thức. 
Sinh tự động từ `data/formulas/` bằng `tools/build_index.py` — không sửa tay file này.

## THCS (lớp 6-9) (31 công thức)

### Các định luật bảo toàn

**Tính khối lượng một chất còn lại theo bảo toàn khối lượng** — *Finding an unknown mass by conservation of mass*

$$m_{A} + m_{B} = m_{C} + m_{D} \Rightarrow m_{D} = m_{A} + m_{B} - m_{C}$$

Trong đó: `m_{A}` là khối lượng chất tham gia A (g); `m_{B}` là khối lượng chất tham gia B (g); `m_{C}` là khối lượng sản phẩm C (g); `m_{D}` là khối lượng sản phẩm D cần tìm (g).

*Điều kiện:* Phản ứng dạng A + B -> C + D, hệ kín

*Ghi chú:* Với phản ứng có chất khí thoát ra, khối lượng bình giảm đúng bằng khối lượng khí bay đi.

<sub>`chemistry.thcs.bao-toan.tinh-khoi-luong-con-lai` · lớp 8, 9 · #bao-toan-khoi-luong #tinh-toan #thcs</sub>

---

### Dung dịch

**Khối lượng chất tan theo nồng độ phần trăm** — *Mass of solute from mass percent*

$$m_{ct} = \dfrac{C\% \cdot m_{dd}}{100}$$

Trong đó: `m_{ct}` là khối lượng chất tan (g); `C\%` là nồng độ phần trăm (%); `m_{dd}` là khối lượng dung dịch (g).

*Điều kiện:* 0 < C% <= 100

*Ghi chú:* Dạng biến đổi của công thức C%; hay dùng khi pha chế dung dịch theo khối lượng.

<sub>`chemistry.thcs.dung-dich.khoi-luong-chat-tan` · lớp 8, 9 · #dung-dich #nong-do-phan-tram #pha-che</sub>

---

**Khối lượng dung dịch** — *Mass of a solution*

$$m_{dd} = m_{ct} + m_{dm}$$

Trong đó: `m_{dd}` là khối lượng dung dịch (g); `m_{ct}` là khối lượng chất tan (g); `m_{dm}` là khối lượng dung môi (g).

*Điều kiện:* Chất tan tan hết, hệ kín, không có chất bay hơi

*Ghi chú:* Hệ quả của định luật bảo toàn khối lượng áp dụng cho quá trình hòa tan.

<sub>`chemistry.thcs.dung-dich.khoi-luong-dung-dich` · lớp 8, 9 · #dung-dich #khoi-luong #thcs</sub>

---

**Nồng độ phần trăm của dung dịch** — *Mass percent concentration*

$$C\% = \dfrac{m_{ct}}{m_{dd}} \times 100\%$$

Trong đó: `C\%` là nồng độ phần trăm (%); `m_{ct}` là khối lượng chất tan (g); `m_{dd}` là khối lượng dung dịch (g).

*Điều kiện:* m_dd > 0; chất tan tan hoàn toàn

*Ghi chú:* C% cho biết số gam chất tan có trong 100 gam dung dịch.

<sub>`chemistry.thcs.dung-dich.nong-do-phan-tram` · lớp 8, 9 · #dung-dich #nong-do-phan-tram #thcs</sub>

---

**Độ tan của chất trong nước** — *Solubility in water*

$$S = \dfrac{m_{ct}}{m_{H_{2}O}} \times 100$$

Trong đó: `S` là độ tan của chất ở nhiệt độ xác định (g/100 g H2O); `m_{ct}` là khối lượng chất tan trong dung dịch bão hòa (g); `m_{H_{2}O}` là khối lượng nước (dung môi) (g).

*Điều kiện:* Dung dịch bão hòa ở nhiệt độ xác định

*Ghi chú:* S là số gam chất tan tối đa hòa tan trong 100 g nước ở nhiệt độ đó. Độ tan chất rắn thường tăng theo nhiệt độ, độ tan chất khí giảm khi tăng nhiệt độ.

<sub>`chemistry.thcs.dung-dich.do-tan` · lớp 8, 9 · #do-tan #dung-dich-bao-hoa #thcs</sub>

---

### Liên kết hóa học

**Quy tắc hóa trị trong hợp chất hai nguyên tố** — *Valence rule for binary compounds*

$$a \cdot x = b \cdot y \quad \text{voi hop chat } \mathrm{A}_{x}\mathrm{B}_{y}$$

Trong đó: `a` là hóa trị của nguyên tố A; `x` là chỉ số của A; `b` là hóa trị của nguyên tố B; `y` là chỉ số của B.

*Điều kiện:* Hợp chất hai nguyên tố (hoặc nguyên tố với nhóm nguyên tử); x, y là số nguyên tối giản

*Ghi chú:* Suy ra x : y = b : a. Hiđro có hóa trị I, oxi có hóa trị II được dùng làm chuẩn.

<sub>`chemistry.thcs.lien-ket.quy-tac-hoa-tri` · lớp 8, 9 · #hoa-tri #cong-thuc-hoa-hoc #thcs</sub>

---

### Đại lượng cơ bản

**Khối lượng mol của chất** — *Molar mass*

$$M = \dfrac{m}{n}$$

Trong đó: `M` là khối lượng mol (g/mol); `m` là khối lượng chất (g); `n` là số mol chất (mol).

*Điều kiện:* n > 0

*Ghi chú:* Khối lượng mol có trị số bằng khối lượng phân tử (hoặc nguyên tử khối) tính theo amu.

<sub>`chemistry.thcs.dai-luong-co-ban.khoi-luong-mol` · lớp 8, 9 · #mol #khoi-luong-mol #dai-luong-co-ban</sub>

---

**Khối lượng chất tính theo số mol** — *Mass from amount of substance*

$$m = n \cdot M$$

Trong đó: `m` là khối lượng chất (g); `n` là số mol chất (mol); `M` là khối lượng mol của chất (g/mol).

*Điều kiện:* n >= 0

*Ghi chú:* Dạng biến đổi của n = m/M, dùng khi đã biết số mol từ phương trình hóa học.

<sub>`chemistry.thcs.dai-luong-co-ban.khoi-luong-theo-so-mol` · lớp 8, 9 · #mol #khoi-luong #dai-luong-co-ban</sub>

---

**Số mol tính theo khối lượng** — *Amount of substance from mass*

$$n = \dfrac{m}{M}$$

Trong đó: `n` là số mol chất (mol); `m` là khối lượng chất (g); `M` là khối lượng mol của chất (g/mol).

*Điều kiện:* M > 0; m và M cùng hệ đơn vị (g và g/mol)

*Ghi chú:* Công thức gốc của mọi bài toán hóa học định lượng. Ghi nhớ tam giác n - m - M.

<sub>`chemistry.thcs.dai-luong-co-ban.so-mol-theo-khoi-luong` · lớp 8, 9 · #mol #dai-luong-co-ban #thcs</sub>

---

**Phần trăm khối lượng nguyên tố trong hợp chất** — *Mass percentage of an element in a compound*

$$\%m_{A} = \dfrac{x \cdot M_{A}}{M_{A_{x}B_{y}}} \times 100\%$$

Trong đó: `\%m_{A}` là phần trăm khối lượng nguyên tố A (%); `x` là số nguyên tử A trong một phân tử; `M_{A}` là nguyên tử khối của A (g/mol); `M_{A_{x}B_{y}}` là khối lượng mol phân tử hợp chất (g/mol).

*Điều kiện:* Hợp chất có công thức xác định A_xB_y

*Ghi chú:* Tổng phần trăm khối lượng của mọi nguyên tố trong hợp chất bằng 100%.

<sub>`chemistry.thcs.dai-luong-co-ban.phan-tram-khoi-luong-nguyen-to` · lớp 8, 9 · #phan-tram-khoi-luong #hop-chat #thcs</sub>

---

**Số mol khí tính theo thể tích ở đktc** — *Moles of gas from volume at STP*

$$n = \dfrac{V}{22.4}$$

Trong đó: `n` là số mol khí (mol); `V` là thể tích khí ở đktc (L).

*Điều kiện:* Khí ở 0 độ C và 1 atm

*Ghi chú:* Chỉ áp dụng cho chất khí, không dùng cho chất rắn hay chất lỏng.

<sub>`chemistry.thcs.dai-luong-co-ban.so-mol-khi-dktc` · lớp 8, 9 · #khi #mol #dktc</sub>

---

**Thể tích chất khí ở điều kiện tiêu chuẩn (0 độ C, 1 atm)** — *Gas volume at STP (0 C, 1 atm)*

$$V = 22.4\,n$$

Trong đó: `V` là thể tích chất khí ở đktc (L); `n` là số mol khí (mol).

*Điều kiện:* Khí lí tưởng ở 0 độ C (273.15 K) và 1 atm (101 325 Pa)

*Ghi chú:* Thể tích mol khí ở đktc V_m = 22.4 L/mol. Sách giáo khoa cũ dùng điều kiện này.

<sub>`chemistry.thcs.dai-luong-co-ban.the-tich-khi-dktc` · lớp 8, 9 · #khi #the-tich-mol #dktc</sub>

---

### Dung dịch

**Khối lượng dung dịch theo thể tích và khối lượng riêng** — *Solution mass from volume and density*

$$m_{dd} = V_{dd} \cdot D$$

Trong đó: `m_{dd}` là khối lượng dung dịch (g); `V_{dd}` là thể tích dung dịch (mL); `D` là khối lượng riêng của dung dịch (g/mL).

*Điều kiện:* V và D cùng hệ đơn vị (mL và g/mL, hoặc L và g/L)

*Ghi chú:* Cầu nối giữa nồng độ phần trăm (theo khối lượng) và nồng độ mol (theo thể tích).

<sub>`chemistry.thcs.dung-dich.khoi-luong-dung-dich-theo-the-tich` · lớp 8, 9, 10 · #dung-dich #khoi-luong-rieng #the-tich</sub>

---

**Khối lượng tinh thể tách ra khi hạ nhiệt độ dung dịch bão hòa** — *Mass of crystals separating on cooling a saturated solution*

$$m_{tt} = m_{dd(t_{1})} \cdot \dfrac{S_{1} - S_{2}}{100 + S_{1}}$$

Trong đó: `m_{tt}` là khối lượng tinh thể khan tách ra khỏi dung dịch (g); `m_{dd(t_{1})}` là khối lượng dung dịch bão hòa ban đầu ở nhiệt độ t1 (g); `S_{1}` là độ tan của chất ở nhiệt độ t1 (g/100 g H2O); `S_{2}` là độ tan của chất ở nhiệt độ t2 (g/100 g H2O).

*Điều kiện:* Dung dịch bão hòa ở cả hai nhiệt độ; t1 > t2 nên S1 > S2; tinh thể tách ra là chất khan; khối lượng nước không đổi (không bay hơi)

*Ghi chú:* Chứng minh: khối lượng nước trong dung dịch không đổi và bằng 100 m_dd/(100 + S1). Nếu tinh thể tách ra ở dạng ngậm nước thì phải đặt ẩn và lập hệ theo khối lượng nước cùng khối lượng chất tan còn lại.

<sub>`chemistry.thcs.dung-dich.khoi-luong-tinh-the-tach-ra` · lớp 8, 9, 10 · #do-tan #dung-dich-bao-hoa #ket-tinh</sub>

---

**Nồng độ phần trăm của dung dịch bão hòa theo độ tan** — *Mass percent of a saturated solution from solubility*

$$C\%_{bh} = \dfrac{S}{100 + S} \times 100\%$$

Trong đó: `C\%_{bh}` là nồng độ phần trăm của dung dịch bão hòa (%); `S` là độ tan của chất ở nhiệt độ đang xét (g/100 g H2O).

*Điều kiện:* Dung dịch bão hòa ở cùng nhiệt độ với giá trị S

*Ghi chú:* Suy ngược: S = 100 C% / (100 - C%).

<sub>`chemistry.thcs.dung-dich.nong-do-phan-tram-bao-hoa` · lớp 8, 9, 10 · #do-tan #dung-dich-bao-hoa #nong-do-phan-tram</sub>

---

### Đại lượng cơ bản

**Số hạt vi mô trong n mol chất** — *Number of particles from moles*

$$N = n \cdot N_{A}$$

Trong đó: `N` là số hạt vi mô (nguyên tử, phân tử, ion); `n` là số mol chất (mol); `N_{A}` là hằng số Avogadro (1/mol).

*Điều kiện:* n >= 0

*Ghi chú:* N_A = 6.022e23 mol^-1 (giá trị dùng trong CT GDPT 2018: 6.022 x 10^23).

<sub>`chemistry.thcs.dai-luong-co-ban.so-hat-vi-mo` · lớp 8, 9, 10 · #mol #avogadro #so-hat</sub>

---

**Số mol tính theo số hạt vi mô** — *Moles from number of particles*

$$n = \dfrac{N}{N_{A}}$$

Trong đó: `n` là số mol chất (mol); `N` là số hạt vi mô; `N_{A}` là hằng số Avogadro (1/mol).

*Điều kiện:* N >= 0

*Ghi chú:* 1 mol bất kì chứa 6.022e23 hạt vi mô tương ứng.

<sub>`chemistry.thcs.dai-luong-co-ban.so-mol-theo-so-hat` · lớp 8, 9, 10 · #mol #avogadro #so-hat</sub>

---

**Phần trăm thể tích của một khí trong hỗn hợp** — *Volume percentage of a gas in a mixture*

$$\%V_{i} = \dfrac{V_{i}}{V_{hh}} \times 100\% = \dfrac{n_{i}}{n_{hh}} \times 100\%$$

Trong đó: `\%V_{i}` là phần trăm thể tích khí i (%); `V_{i}` là thể tích khí i (L); `V_{hh}` là tổng thể tích hỗn hợp khí (L); `n_{i}` là số mol khí i (mol); `n_{hh}` là tổng số mol khí (mol).

*Điều kiện:* Các khí đo ở cùng nhiệt độ và áp suất

*Ghi chú:* Với chất khí: tỉ lệ thể tích bằng tỉ lệ số mol, nên %V = %n.

<sub>`chemistry.thcs.dai-luong-co-ban.phan-tram-the-tich-khi` · lớp 8, 9, 10 · #phan-tram-the-tich #hon-hop-khi #thcs</sub>

---

**Định luật Avogadro về thể tích chất khí** — *Avogadro's law*

$$\dfrac{V_{1}}{n_{1}} = \dfrac{V_{2}}{n_{2}} \quad (\text{cung } T,\, p)$$

Trong đó: `V_{1}` là thể tích hai mẫu khí (L); `V_{2}` là thể tích hai mẫu khí (L); `n_{1}` là số mol tương ứng của hai mẫu khí (mol); `n_{2}` là số mol tương ứng của hai mẫu khí (mol); `T` là nhiệt độ; `p` là áp suất.

*Điều kiện:* Hai mẫu khí đo ở cùng nhiệt độ và áp suất

*Ghi chú:* Ở cùng điều kiện, những thể tích khí bằng nhau chứa số phân tử bằng nhau, vì vậy tỉ lệ thể tích khí bằng tỉ lệ hệ số trong phương trình hóa học.

<sub>`chemistry.thcs.dai-luong-co-ban.dinh-luat-avogadro` · lớp 8, 9, 10 · #avogadro #the-tich-khi #thcs</sub>

---

**Số mol khí tính theo thể tích ở điều kiện chuẩn** — *Moles of gas from volume at 25 C, 1 bar*

$$n = \dfrac{V}{24.79}$$

Trong đó: `n` là số mol khí (mol); `V` là thể tích khí ở điều kiện chuẩn (L).

*Điều kiện:* Khí ở 25 độ C và 1 bar

*Ghi chú:* Đây là công thức chuẩn dùng trong KHTN 8 và Hóa học 10 theo CT 2018.

<sub>`chemistry.thcs.dai-luong-co-ban.so-mol-khi-dkc` · lớp 8, 9, 10 · #khi #mol #dieu-kien-chuan</sub>

---

**Thể tích chất khí ở điều kiện chuẩn (25 độ C, 1 bar)** — *Gas volume at standard conditions (25 C, 1 bar)*

$$V = 24.79\,n$$

Trong đó: `V` là thể tích chất khí ở điều kiện chuẩn (L); `n` là số mol khí (mol).

*Điều kiện:* Khí lí tưởng ở 25 độ C (298.15 K) và 1 bar (10^5 Pa)

*Ghi chú:* Chương trình GDPT 2018 dùng thể tích mol khí ở điều kiện chuẩn V_m = 24.79 L/mol.

<sub>`chemistry.thcs.dai-luong-co-ban.the-tich-khi-dkc` · lớp 8, 9, 10 · #khi #the-tich-mol #dieu-kien-chuan</sub>

---

**Tỉ lệ số mol các chất theo phương trình hóa học** — *Mole ratios from a balanced equation*

$$\dfrac{n_{A}}{a} = \dfrac{n_{B}}{b} = \dfrac{n_{C}}{c} = \dfrac{n_{D}}{d}$$

Trong đó: `n_{A}` là số mol các chất tham gia đã phản ứng (mol); `n_{B}` là số mol các chất tham gia đã phản ứng (mol); `n_{C}` là số mol các sản phẩm tạo thành (mol); `n_{D}` là số mol các sản phẩm tạo thành (mol); `a` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD; `b` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD; `c` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD; `d` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD.

*Điều kiện:* Phương trình hóa học đã được cân bằng; phản ứng xảy ra hoàn toàn

*Ghi chú:* Đây là cơ sở của mọi bài toán tính theo phương trình hóa học: đổi ra mol, lập tỉ lệ, rồi đổi ngược về khối lượng hoặc thể tích.

<sub>`chemistry.thcs.dai-luong-co-ban.ti-le-mol-theo-phuong-trinh` · lớp 8, 9, 10 · #phuong-trinh-hoa-hoc #ti-le-mol #thcs</sub>

---

**Tỉ khối của khí A so với khí B** — *Relative density of gas A to gas B*

$$d_{A/B} = \dfrac{M_{A}}{M_{B}}$$

Trong đó: `d_{A/B}` là tỉ khối của khí A so với khí B; `M_{A}` là khối lượng mol khí A (g/mol); `M_{B}` là khối lượng mol khí B (g/mol).

*Điều kiện:* Hai khí đo ở cùng điều kiện nhiệt độ và áp suất

*Ghi chú:* d > 1: khí A nặng hơn khí B; d < 1: khí A nhẹ hơn khí B. Tỉ khối không có đơn vị.

<sub>`chemistry.thcs.dai-luong-co-ban.ti-khoi-hai-khi` · lớp 8, 9, 10 · #ti-khoi #khi #dai-luong-co-ban</sub>

---

**Tỉ khối của khí A so với không khí** — *Relative density of a gas to air*

$$d_{A/kk} = \dfrac{M_{A}}{29}$$

Trong đó: `d_{A/kk}` là tỉ khối của khí A so với không khí; `M_{A}` là khối lượng mol khí A (g/mol).

*Điều kiện:* Cùng điều kiện nhiệt độ, áp suất

*Ghi chú:* Khối lượng mol trung bình của không khí lấy bằng 29 g/mol (khoảng 80% N2 và 20% O2 theo thể tích).

<sub>`chemistry.thcs.dai-luong-co-ban.ti-khoi-so-voi-khong-khi` · lớp 8, 9, 10 · #ti-khoi #khong-khi #khi</sub>

---

**Lập công thức hóa học từ phần trăm khối lượng** — *Deriving a chemical formula from mass percentages*

$$x : y = \dfrac{\%m_{A}}{M_{A}} : \dfrac{\%m_{B}}{M_{B}}$$

Trong đó: `x` là số nguyên tử A; `y` là số nguyên tử B; `\%m_{A}` là phần trăm khối lượng A (%); `\%m_{B}` là phần trăm khối lượng B (%); `M_{A}` là nguyên tử khối A (g/mol); `M_{B}` là nguyên tử khối B (g/mol).

*Điều kiện:* x : y phải rút gọn về tỉ lệ số nguyên tối giản

*Ghi chú:* Kết quả cho công thức đơn giản nhất (công thức thực nghiệm); cần thêm M phân tử để suy ra công thức phân tử.

<sub>`chemistry.thcs.dai-luong-co-ban.lap-cong-thuc-tu-phan-tram` · lớp 8, 9, 11 · #cong-thuc-hoa-hoc #phan-tram-khoi-luong #lap-cong-thuc</sub>

---

### Các định luật bảo toàn

**Định luật bảo toàn khối lượng** — *Law of conservation of mass*

$$\sum m_{\text{chat tham gia}} = \sum m_{\text{san pham}}$$

Trong đó: `m_{\text{chat tham gia}}` là khối lượng các chất tham gia phản ứng (g); `m_{\text{san pham}}` là khối lượng các sản phẩm (g).

*Điều kiện:* Hệ kín, phản ứng hóa học thông thường (không phải phản ứng hạt nhân)

*Ghi chú:* Do số nguyên tử mỗi nguyên tố được bảo toàn nên tổng khối lượng không đổi (Lomonosov - Lavoisier).

<sub>`chemistry.thcs.bao-toan.bao-toan-khoi-luong` · lớp 8, 9, 10, 11, 12 · #bao-toan-khoi-luong #dinh-luat #thcs</sub>

---

**Độ tinh khiết của mẫu chất** — *Purity of a sample*

$$\text{Do tinh khiet}\,\% = \dfrac{m_{\text{chat nguyen chat}}}{m_{\text{mau}}} \times 100\%$$

Trong đó: `m_{\text{chat nguyen chat}}` là khối lượng chất nguyên chất trong mẫu (g); `m_{\text{mau}}` là khối lượng mẫu chất (kể cả tạp chất) (g).

*Điều kiện:* Tạp chất không tham gia phản ứng đang xét

*Ghi chú:* Phần trăm tạp chất = 100% - độ tinh khiết. Khối lượng chất nguyên chất mới được dùng để tính theo phương trình.

<sub>`chemistry.thcs.bao-toan.do-tinh-khiet` · lớp 9, 10, 11 · #do-tinh-khiet #tap-chat #tinh-toan</sub>

---

**Hiệu suất phản ứng tính theo sản phẩm** — *Percent yield based on product*

$$H\% = \dfrac{m_{tt}}{m_{lt}} \times 100\%$$

Trong đó: `H\%` là hiệu suất phản ứng (%); `m_{tt}` là khối lượng sản phẩm thu được thực tế (g); `m_{lt}` là khối lượng sản phẩm tính theo lí thuyết (g).

*Điều kiện:* 0 < H% <= 100; m_lt tính từ chất phản ứng hết theo phương trình hóa học

*Ghi chú:* Có thể thay khối lượng bằng số mol: H% = n_tt/n_lt x 100%.

<sub>`chemistry.thcs.bao-toan.hieu-suat-phan-ung-theo-san-pham` · lớp 9, 10, 11, 12 · #hieu-suat #phan-ung #tinh-toan</sub>

---

### Dung dịch

**Nồng độ mol của dung dịch** — *Molar concentration*

$$C_{M} = \dfrac{n_{ct}}{V_{dd}}$$

Trong đó: `C_{M}` là nồng độ mol (mol/L); `n_{ct}` là số mol chất tan (mol); `V_{dd}` là thể tích dung dịch (L).

*Điều kiện:* V_dd tính bằng lít; V_dd > 0

*Ghi chú:* Kí hiệu 1 M nghĩa là 1 mol/L. Chú ý đổi mL sang L trước khi tính.

<sub>`chemistry.thcs.dung-dich.nong-do-mol` · lớp 9, 10, 11, 12 · #dung-dich #nong-do-mol #thcs</sub>

---

### Điện hóa

**Dãy hoạt động hóa học của kim loại** — *Reactivity series of metals*

$$\mathrm{K},\,\mathrm{Ba},\,\mathrm{Ca},\,\mathrm{Na},\,\mathrm{Mg},\,\mathrm{Al},\,\mathrm{Zn},\,\mathrm{Fe},\,\mathrm{Ni},\,\mathrm{Sn},\,\mathrm{Pb},\,\mathrm{H},\,\mathrm{Cu},\,\mathrm{Hg},\,\mathrm{Ag},\,\mathrm{Pt},\,\mathrm{Au}$$

Trong đó: `\mathrm{K}` là các kim loại xếp theo chiều giảm dần mức độ hoạt động hóa học; `\ldots` là các kim loại xếp theo chiều giảm dần mức độ hoạt động hóa học; `\mathrm{Au}` là các kim loại xếp theo chiều giảm dần mức độ hoạt động hóa học.

*Điều kiện:* Dãy sắp xếp theo mức độ hoạt động hóa học giảm dần từ trái sang phải

*Ghi chú:* Kim loại đứng trước H đẩy được hiđro ra khỏi dung dịch acid loãng; từ Mg trở đi kim loại đứng trước đẩy được kim loại đứng sau ra khỏi dung dịch muối.

<sub>`chemistry.thcs.dien-hoa.day-hoat-dong-hoa-hoc` · lớp 9, 12 · #day-hoat-dong #kim-loai #thcs</sub>

---

### Đại lượng cơ bản

**Xác định chất phản ứng hết và chất còn dư** — *Identifying the limiting reactant*

$$\dfrac{n_{A}}{a} < \dfrac{n_{B}}{b} \;\Rightarrow\; \text{A het, B du}$$

Trong đó: `n_{A}` là số mol chất A ban đầu (mol); `n_{B}` là số mol chất B ban đầu (mol); `a` là hệ số của A trong phương trình; `b` là hệ số của B trong phương trình.

*Điều kiện:* Phương trình đã cân bằng; áp dụng cho phản ứng một giai đoạn

*Ghi chú:* Mọi tính toán về sản phẩm phải dựa vào chất phản ứng hết (chất thiếu). Nếu hai tỉ lệ bằng nhau thì cả hai chất cùng hết.

<sub>`chemistry.thcs.dai-luong-co-ban.xac-dinh-chat-du` · lớp 9, 10, 11, 12 · #chat-du #chat-het #phuong-trinh-hoa-hoc</sub>

---

## THPT (lớp 10-12) (418 công thức)

### Bảng tuần hoàn

**Công thức hợp chất khí với hiđro** — *Formula of the volatile hydride*

$$\mathrm{RH}_{8-n} \;(n = \text{STT nhom A})$$

Trong đó: `\mathrm{R}` là kí hiệu nguyên tố phi kim; `n` là số thứ tự nhóm A.

*Điều kiện:* Nguyên tố thuộc nhóm IVA đến VIIA

*Ghi chú:* IVA: RH4; VA: RH3; VIA: RH2; VIIA: RH. Ví dụ CH4, NH3, H2S, HCl.

<sub>`chemistry.thpt.bang-tuan-hoan.cong-thuc-hop-chat-khi-voi-hidro` · lớp 10 · #hop-chat-khi-hidro #bang-tuan-hoan #hoa-tri</sub>

---

**Công thức oxit cao nhất của nguyên tố nhóm A** — *Formula of the highest oxide*

$$\mathrm{R}_{2}\mathrm{O}_{n} \;(n = \text{STT nhom A})$$

Trong đó: `\mathrm{R}` là kí hiệu nguyên tố; `n` là số thứ tự nhóm A, bằng hóa trị cao nhất với oxi.

*Điều kiện:* n từ 1 đến 7; rút gọn chỉ số khi n chẵn

*Ghi chú:* Nhóm IA: R2O; IIA: RO; IIIA: R2O3; IVA: RO2; VA: R2O5; VIA: RO3; VIIA: R2O7.

<sub>`chemistry.thpt.bang-tuan-hoan.cong-thuc-oxit-cao-nhat` · lớp 10 · #oxit-cao-nhat #bang-tuan-hoan #hoa-tri</sub>

---

**Hóa trị cao nhất với oxi và hóa trị với hiđro** — *Highest oxide valence and hydride valence*

$$n_{O} = \text{STT nhom A}, \quad n_{H} = 8 - n_{O}$$

Trong đó: `n_{O}` là hóa trị cao nhất của nguyên tố trong oxit; `n_{H}` là hóa trị của nguyên tố trong hợp chất khí với hiđro.

*Điều kiện:* Nguyên tố nhóm A; hợp chất khí với hiđro chỉ xét cho các nhóm IVA đến VIIA

*Ghi chú:* Tổng hóa trị cao nhất với oxi và hóa trị với hiđro luôn bằng 8. Flo và oxi không có oxit cao nhất theo quy luật này.

<sub>`chemistry.thpt.bang-tuan-hoan.hoa-tri-cao-nhat-voi-oxi` · lớp 10 · #bang-tuan-hoan #hoa-tri #oxit-cao-nhat</sub>

---

**Phần trăm khối lượng nguyên tố trong hợp chất khí với hiđro** — *Mass percent of R in its volatile hydride*

$$\%m_{R} = \dfrac{M_{R}}{M_{R} + (8-n)} \times 100\%$$

Trong đó: `\%m_{R}` là phần trăm khối lượng của R trong hợp chất RH_(8-n) (%); `M_{R}` là nguyên tử khối của R (g/mol); `n` là số thứ tự nhóm A của R.

*Điều kiện:* Nguyên tố R thuộc nhóm IVA đến VIIA, hợp chất khí với hiđro có dạng RH_(8-n); lấy nguyên tử khối của H bằng 1

*Ghi chú:* Cặp đôi với công thức tính %R trong oxit cao nhất; kết hợp hai dữ kiện thường đủ để xác định nguyên tố R.

<sub>`chemistry.thpt.bang-tuan-hoan.phan-tram-r-trong-hop-chat-khi-hidro` · lớp 10 · #hop-chat-khi-hidro #phan-tram-khoi-luong #xac-dinh-nguyen-to</sub>

---

**Phần trăm khối lượng nguyên tố trong oxit cao nhất** — *Mass percent of R in its highest oxide*

$$\%m_{R} = \dfrac{2M_{R}}{2M_{R} + 16n} \times 100\%$$

Trong đó: `\%m_{R}` là phần trăm khối lượng của R trong oxit R2On (%); `M_{R}` là nguyên tử khối của R (g/mol); `n` là hóa trị cao nhất của R với oxi.

*Điều kiện:* Oxit cao nhất có dạng R2On

*Ghi chú:* Dạng bài quen thuộc: cho %R và nhóm, giải ra M_R để xác định nguyên tố.

<sub>`chemistry.thpt.bang-tuan-hoan.phan-tram-r-trong-oxit-cao-nhat` · lớp 10 · #oxit-cao-nhat #phan-tram-khoi-luong #xac-dinh-nguyen-to</sub>

---

**Quy luật biến đổi tính chất trong chu kì và nhóm A** — *Periodic trends across periods and groups*

$$\begin{cases} \text{Trong chu ki (trai} \to \text{phai)}: r \downarrow,\; \chi \uparrow,\; I_{1} \uparrow,\; \text{tinh kim loai} \downarrow,\; \text{tinh phi kim} \uparrow \\ \text{Trong nhom A (tren} \to \text{duoi)}: r \uparrow,\; \chi \downarrow,\; I_{1} \downarrow,\; \text{tinh kim loai} \uparrow,\; \text{tinh phi kim} \downarrow \end{cases}$$

Trong đó: `r` là bán kính nguyên tử (nm); `\chi` là độ âm điện; `I_{1}` là năng lượng ion hóa thứ nhất (kJ/mol).

*Điều kiện:* Áp dụng cho các nguyên tố nhóm A; có một số ngoại lệ nhỏ với năng lượng ion hóa

*Ghi chú:* Hệ quả: tính base của oxit và hydroxide giảm, tính acid tăng theo chiều trái sang phải của chu kì.

<sub>`chemistry.thpt.bang-tuan-hoan.quy-luat-bien-doi` · lớp 10 · #quy-luat-tuan-hoan #ban-kinh #do-am-dien</sub>

---

**Số thứ tự chu kì bằng số lớp electron** — *Period number equals number of electron shells*

$$\text{STT chu ki} = \text{so lop electron} = n_{max}$$

Trong đó: `\text{STT chu ki}` là số thứ tự chu kì; `n_{max}` là số thứ tự lớp electron ngoài cùng.

*Điều kiện:* Áp dụng cho mọi nguyên tố trong bảng tuần hoàn

*Ghi chú:* Bảng tuần hoàn hiện nay có 7 chu kì; chu kì 1, 2, 3 là chu kì nhỏ.

<sub>`chemistry.thpt.bang-tuan-hoan.so-thu-tu-chu-ki` · lớp 10 · #bang-tuan-hoan #chu-ki #cau-hinh-electron</sub>

---

**Số thứ tự nhóm A bằng số electron lớp ngoài cùng** — *Group A number equals valence electrons*

$$\text{STT nhom A} = \text{so electron lop ngoai cung} = a\;(\text{trong } ns^{a} \text{ hoac } ns^{2}np^{b})$$

Trong đó: `a` là số electron của phân lớp ns; `b` là số electron của phân lớp np; `n` là số thứ tự lớp ngoài cùng.

*Điều kiện:* Nguyên tố nhóm A (nguyên tố s và nguyên tố p)

*Ghi chú:* Với nguyên tố p: STT nhóm A = 2 + b. Nhóm IA là kim loại kiềm, IIA kiềm thổ, VIIA halogen, VIIIA khí hiếm.

<sub>`chemistry.thpt.bang-tuan-hoan.so-thu-tu-nhom-a` · lớp 10 · #bang-tuan-hoan #nhom-a #electron-hoa-tri</sub>

---

**Xác định nhóm B theo số electron hóa trị** — *Determining group B from valence electrons*

$$\text{Cau hinh } (n-1)d^{a}ns^{b},\; x = a + b : \begin{cases} 3 \le x \le 7 & \text{nhom } x\mathrm{B} \\ 8 \le x \le 10 & \text{nhom VIIIB} \\ x = 11,\,12 & \text{nhom } (x-10)\mathrm{B} \end{cases}$$

Trong đó: `x` là tổng số electron hóa trị; `a` là số electron phân lớp (n-1)d; `b` là số electron phân lớp ns; `n` là số thứ tự lớp electron ngoài cùng.

*Điều kiện:* Nguyên tố d (nguyên tố nhóm B, kim loại chuyển tiếp)

*Ghi chú:* Electron hóa trị của nguyên tố d gồm electron phân lớp ns và (n-1)d.

<sub>`chemistry.thpt.bang-tuan-hoan.so-thu-tu-nhom-b` · lớp 10 · #bang-tuan-hoan #nhom-b #nguyen-to-d</sub>

---

**Quan hệ giữa số thứ tự ô và số hiệu nguyên tử** — *Element order number equals atomic number*

$$\text{STT o} = Z = P = E$$

Trong đó: `\text{STT o}` là số thứ tự ô trong bảng tuần hoàn; `Z` là số hiệu nguyên tử; `P` là số proton; `E` là số electron của nguyên tử.

*Điều kiện:* Nguyên tử trung hòa về điện

*Ghi chú:* Nguyên tắc sắp xếp: theo chiều tăng dần điện tích hạt nhân.

<sub>`chemistry.thpt.bang-tuan-hoan.so-thu-tu-o` · lớp 10 · #bang-tuan-hoan #vi-tri #so-hieu-nguyen-tu</sub>

---

### Cấu tạo nguyên tử

**Cấu hình electron của ion** — *Electron configuration of ions*

$$\mathrm{M} \rightarrow \mathrm{M}^{n+} + ne \;(\text{bot } n\,e\;\text{lop ngoai cung}), \quad \mathrm{X} + me \rightarrow \mathrm{X}^{m-} \;(\text{them } m\,e)$$

Trong đó: `\mathrm{M}` là nguyên tử kim loại; `\mathrm{M}^{n+}` là cation có điện tích n+; `\mathrm{X}` là nguyên tử phi kim; `\mathrm{X}^{m-}` là anion có điện tích m-; `n` là số electron nhường hoặc nhận; `m` là số electron nhường hoặc nhận.

*Điều kiện:* Số proton không đổi khi tạo ion; chỉ số electron thay đổi

*Ghi chú:* Với nguyên tố d, khi tạo cation phải tách electron ở phân lớp ns trước rồi mới đến (n-1)d. Ví dụ Fe là [Ar]3d6 4s2, còn Fe2+ là [Ar]3d6.

<sub>`chemistry.thpt.nguyen-tu.cau-hinh-electron-ion` · lớp 10 · #cau-hinh-electron #ion #thpt</sub>

---

**Quy tắc Hund và nguyên lí vững bền** — *Hund's rule and the Aufbau principle*

$$\text{Trong cung mot phan lop: dien } 1e\;\text{vao moi orbital truoc, spin song song, roi moi ghep doi}$$

Trong đó: `\text{phan lop}` là tập hợp các orbital có cùng mức năng lượng (s, p, d, f); `e` là electron.

*Điều kiện:* Áp dụng cho nguyên tử ở trạng thái cơ bản

*Ghi chú:* Ba quy tắc viết cấu hình: nguyên lí vững bền (điền từ mức năng lượng thấp lên cao), nguyên lí Pauli (tối đa 2e mỗi orbital, spin ngược nhau) và quy tắc Hund.

<sub>`chemistry.thpt.nguyen-tu.quy-tac-hund` · lớp 10 · #quy-tac-hund #cau-hinh-electron #pauli</sub>

---

**Quy tắc Klechkovski về thứ tự mức năng lượng** — *Klechkovski (Madelung) rule*

$$1s\,2s\,2p\,3s\,3p\,4s\,3d\,4p\,5s\,4d\,5p\,6s\,4f\,5d\,6p\,7s\,5f\,6d$$

Trong đó: `1s` là các phân lớp electron xếp theo chiều tăng dần mức năng lượng; `2s` là các phân lớp electron xếp theo chiều tăng dần mức năng lượng; `2p` là các phân lớp electron xếp theo chiều tăng dần mức năng lượng; `\ldots` là các phân lớp electron xếp theo chiều tăng dần mức năng lượng.

*Điều kiện:* Electron điền vào phân lớp có tổng (n + l) nhỏ trước; nếu (n + l) bằng nhau thì phân lớp có n nhỏ hơn được điền trước

*Ghi chú:* Viết cấu hình theo mức năng lượng rồi sắp xếp lại theo lớp. Ngoại lệ bán bão hòa và bão hòa: Cr là 3d5 4s1, Cu là 3d10 4s1.

<sub>`chemistry.thpt.nguyen-tu.quy-tac-klechkovski` · lớp 10 · #cau-hinh-electron #klechkovski #thpt</sub>

---

**Quan hệ số proton, số electron và điện tích hạt nhân** — *Nuclear charge, protons and electrons*

$$Z = P = E, \quad q_{hn} = +Z e$$

Trong đó: `Z` là số hiệu nguyên tử; `P` là số proton; `E` là số electron của nguyên tử trung hòa; `q_{hn}` là điện tích hạt nhân (C); `e` là điện tích nguyên tố (C).

*Điều kiện:* Nguyên tử trung hòa về điện (không phải ion)

*Ghi chú:* e = 1.602e-19 C. Với ion M(n+) thì số electron bằng Z - n; với ion X(m-) thì bằng Z + m.

<sub>`chemistry.thpt.nguyen-tu.dien-tich-hat-nhan` · lớp 10 · #nguyen-tu #proton #electron</sub>

---

**Điều kiện bền của hạt nhân nguyên tử** — *Stability condition of a nucleus*

$$1 \le \dfrac{N}{Z} \le 1.5$$

Trong đó: `N` là số neutron; `Z` là số proton.

*Điều kiện:* Áp dụng cho các nguyên tố bền có Z từ 2 đến 82; riêng hiđro nhẹ có N = 0

*Ghi chú:* Dùng để chặn nghiệm khi giải bài toán tìm Z từ tổng số hạt.

<sub>`chemistry.thpt.nguyen-tu.dieu-kien-ben-hat-nhan` · lớp 10 · #nguyen-tu #hat-nhan-ben #bien-luan</sub>

---

**Khoảng xác định số proton từ tổng số hạt** — *Bounding Z from the total particle count*

$$\dfrac{S}{3.5} \le Z \le \dfrac{S}{3}$$

Trong đó: `S` là tổng số hạt cơ bản của nguyên tử; `Z` là số proton.

*Điều kiện:* Suy ra từ S = 2Z + N và điều kiện bền Z <= N <= 1.5Z; đúng với Z <= 82

*Ghi chú:* Sau khi chặn khoảng, thử các giá trị Z nguyên rồi kiểm tra lại điều kiện bền.

<sub>`chemistry.thpt.nguyen-tu.khoang-xac-dinh-z` · lớp 10 · #nguyen-tu #bai-toan-so-hat #bien-luan</sub>

---

**Số khối của hạt nhân nguyên tử** — *Mass number*

$$A = Z + N$$

Trong đó: `A` là số khối; `Z` là số proton (số hiệu nguyên tử); `N` là số neutron.

*Điều kiện:* A, Z, N là các số nguyên dương (N có thể bằng 0 với hiđro nhẹ)

*Ghi chú:* Kí hiệu nguyên tử viết dạng A-X-Z với A ở trên, Z ở dưới. Số khối xấp xỉ nguyên tử khối tính theo amu.

<sub>`chemistry.thpt.nguyen-tu.so-khoi` · lớp 10 · #nguyen-tu #so-khoi #hat-nhan</sub>

---

**Tổng số hạt cơ bản trong nguyên tử** — *Total number of subatomic particles*

$$S = P + N + E = 2Z + N$$

Trong đó: `S` là tổng số hạt cơ bản; `P` là số proton; `N` là số neutron; `E` là số electron; `Z` là số hiệu nguyên tử.

*Điều kiện:* Nguyên tử trung hòa; với ion phải cộng hoặc trừ số electron tương ứng

*Ghi chú:* Số hạt mang điện là 2Z, số hạt không mang điện là N. Hiệu số hạt mang điện và không mang điện bằng 2Z - N.

<sub>`chemistry.thpt.nguyen-tu.tong-so-hat` · lớp 10 · #nguyen-tu #so-hat #bai-toan-so-hat</sub>

---

**Khối lượng riêng của nguyên tử** — *Density of an atom*

$$D = \dfrac{m_{nt}}{V} = \dfrac{M}{N_{A} \cdot \dfrac{4}{3}\pi r^{3}}$$

Trong đó: `D` là khối lượng riêng của nguyên tử (g/cm^3); `m_{nt}` là khối lượng một nguyên tử (g); `V` là thể tích một nguyên tử (cm^3); `M` là khối lượng mol nguyên tử (g/mol); `N_{A}` là hằng số Avogadro (1/mol); `r` là bán kính nguyên tử (cm).

*Điều kiện:* Coi nguyên tử là hình cầu; nếu tính khối lượng riêng của tinh thể phải nhân thêm độ đặc khít

*Ghi chú:* Khối lượng một nguyên tử: m_nt = M/N_A (gam).

<sub>`chemistry.thpt.nguyen-tu.khoi-luong-rieng-nguyen-tu` · lớp 10 · #khoi-luong-rieng #nguyen-tu #thpt</sub>

---

**Thể tích nguyên tử theo bán kính** — *Atomic volume from radius*

$$V = \dfrac{4}{3}\pi r^{3}$$

Trong đó: `V` là thể tích của một nguyên tử (coi là hình cầu) (cm^3); `r` là bán kính nguyên tử (cm).

*Điều kiện:* Mô hình nguyên tử hình cầu

*Ghi chú:* 1 nm = 1e-7 cm; 1 angstrom = 1e-8 cm = 0.1 nm. Bán kính nguyên tử cỡ 1e-8 cm.

<sub>`chemistry.thpt.nguyen-tu.the-tich-nguyen-tu` · lớp 10 · #ban-kinh-nguyen-tu #the-tich #thpt</sub>

---

**Năng lượng ion hóa thứ nhất** — *First ionization energy*

$$\mathrm{X}(g) \rightarrow \mathrm{X}^{+}(g) + 1e, \quad \Delta E = I_{1}$$

Trong đó: `\mathrm{X}(g)` là nguyên tử ở thể khí, trạng thái cơ bản; `\mathrm{X}^{+}(g)` là ion dương tạo thành ở thể khí; `I_{1}` là năng lượng ion hóa thứ nhất (kJ/mol).

*Điều kiện:* Nguyên tử ở thể khí, cô lập, trạng thái cơ bản

*Ghi chú:* Luôn có I1 < I2 < I3 < ... Trong một chu kì, I1 nói chung tăng theo chiều tăng của điện tích hạt nhân; trong một nhóm A, I1 giảm từ trên xuống.

<sub>`chemistry.thpt.nguyen-tu.nang-luong-ion-hoa` · lớp 10 · #nang-luong-ion-hoa #nguyen-tu #bang-tuan-hoan</sub>

---

**Năng lượng của photon hấp thụ hoặc phát xạ** — *Photon energy*

$$E = h\nu = \dfrac{hc}{\lambda}$$

Trong đó: `E` là năng lượng photon (J); `h` là hằng số Planck (J.s); `\nu` là tần số bức xạ (1/s); `c` là tốc độ ánh sáng trong chân không (m/s); `\lambda` là bước sóng bức xạ (m).

*Điều kiện:* Bức xạ điện từ trong chân không

*Ghi chú:* h = 6.626e-34 J.s; c = 2.998e8 m/s. Nhân với N_A để đổi sang J/mol.

<sub>`chemistry.thpt.nguyen-tu.nang-luong-photon` · lớp 10 · #photon #nang-luong #quang-pho</sub>

---

**Số electron tối đa trong lớp thứ n** — *Maximum electrons in shell n*

$$e_{max}(n) = 2n^{2}$$

Trong đó: `e_{max}(n)` là số electron tối đa của lớp thứ n; `n` là số thứ tự lớp electron.

*Điều kiện:* Công thức đúng về mặt sức chứa lí thuyết với n từ 1 đến 4 trong chương trình phổ thông

*Ghi chú:* Lớp K (n=1): 2e; L (n=2): 8e; M (n=3): 18e; N (n=4): 32e.

<sub>`chemistry.thpt.nguyen-tu.so-electron-toi-da-lop` · lớp 10 · #cau-hinh-electron #lop-electron #thpt</sub>

---

**Số electron tối đa trong một phân lớp** — *Maximum electrons in a subshell*

$$e_{max} = 2(2\ell + 1) \Rightarrow s:2,\; p:6,\; d:10,\; f:14$$

Trong đó: `e_{max}` là số electron tối đa của phân lớp; `\ell` là số lượng tử phụ (s: 0, p: 1, d: 2, f: 3).

*Điều kiện:* Theo nguyên lí Pauli: mỗi orbital chứa tối đa 2 electron có spin ngược nhau

*Ghi chú:* Số orbital của phân lớp bằng 2l + 1: s có 1, p có 3, d có 5, f có 7 orbital.

<sub>`chemistry.thpt.nguyen-tu.so-electron-toi-da-phan-lop` · lớp 10 · #cau-hinh-electron #phan-lop #pauli</sub>

---

**Số orbital nguyên tử trong lớp thứ n** — *Number of atomic orbitals in shell n*

$$\text{So AO} = n^{2}$$

Trong đó: `n` là số thứ tự lớp electron; `\text{So AO}` là số orbital nguyên tử (AO) có trong lớp thứ n.

*Điều kiện:* n là số nguyên dương

*Ghi chú:* Mỗi AO chứa tối đa 2 electron nên số electron tối đa của lớp là 2n^2.

<sub>`chemistry.thpt.nguyen-tu.so-orbital-trong-lop` · lớp 10 · #orbital #lop-electron #thpt</sub>

---

**Nguyên tử khối trung bình của nguyên tố có nhiều đồng vị** — *Average atomic mass of isotopes*

$$\overline{A} = \dfrac{A_{1}x_{1} + A_{2}x_{2} + \cdots + A_{k}x_{k}}{100}$$

Trong đó: `\overline{A}` là nguyên tử khối trung bình (amu); `A_{i}` là số khối (nguyên tử khối) của đồng vị thứ i; `x_{i}` là phần trăm số nguyên tử của đồng vị thứ i (%).

*Điều kiện:* Tổng các phần trăm x_i bằng 100

*Ghi chú:* 1 amu = 1.6605e-27 kg. Nguyên tử khối ghi trong bảng tuần hoàn là giá trị trung bình này.

<sub>`chemistry.thpt.nguyen-tu.nguyen-tu-khoi-trung-binh` · lớp 10 · #dong-vi #nguyen-tu-khoi-trung-binh #thpt</sub>

---

**Phần trăm mỗi đồng vị khi nguyên tố có hai đồng vị** — *Isotope abundances for a two-isotope element*

$$x_{1} = \dfrac{\overline{A} - A_{2}}{A_{1} - A_{2}} \times 100\%, \quad x_{2} = 100\% - x_{1}$$

Trong đó: `x_{1}` là phần trăm đồng vị 1 (%); `x_{2}` là phần trăm đồng vị 2 (%); `\overline{A}` là nguyên tử khối trung bình (amu); `A_{1}` là số khối đồng vị 1 (amu); `A_{2}` là số khối đồng vị 2 (amu).

*Điều kiện:* A1 khác A2; giá trị trung bình nằm giữa A1 và A2

*Ghi chú:* Đây chính là quy tắc đường chéo áp dụng cho hỗn hợp hai đồng vị.

<sub>`chemistry.thpt.nguyen-tu.phan-tram-hai-dong-vi` · lớp 10 · #dong-vi #duong-cheo #thpt</sub>

---

### Liên kết hóa học

**Điện tích hình thức trong công thức Lewis** — *Formal charge in a Lewis structure*

$$FC = V - L - \dfrac{B}{2}$$

Trong đó: `FC` là điện tích hình thức của nguyên tử; `V` là số electron hóa trị của nguyên tử tự do; `L` là số electron không liên kết (electron riêng); `B` là số electron tham gia liên kết của nguyên tử đó.

*Điều kiện:* Áp dụng cho một công thức Lewis đã viết xong

*Ghi chú:* Công thức Lewis hợp lí nhất là công thức có các điện tích hình thức gần 0 nhất. Tổng FC bằng điện tích của tiểu phân.

<sub>`chemistry.thpt.lien-ket.dien-tich-hinh-thuc` · lớp 10 · #cong-thuc-lewis #dien-tich-hinh-thuc #thpt</sub>

---

**Số cặp electron dùng chung khi viết công thức Lewis** — *Number of shared electron pairs in a Lewis structure*

$$\text{So cap dung chung} = \dfrac{\text{So e can de du octet} - \text{Tong so e hoa tri}}{2}$$

Trong đó: `\text{So e can de du octet}` là tổng số electron cần để mọi nguyên tử đạt octet (H cần 2); `\text{Tong so e hoa tri}` là tổng số electron hóa trị của các nguyên tử, có hiệu chỉnh theo điện tích ion.

*Điều kiện:* Phân tử hoặc ion tuân theo quy tắc octet

*Ghi chú:* Với ion âm cộng thêm số electron bằng điện tích; với ion dương trừ đi. Số electron riêng = tổng e hóa trị - 2 x số cặp dùng chung.

<sub>`chemistry.thpt.lien-ket.so-electron-hoa-tri-trong-lewis` · lớp 10 · #cong-thuc-lewis #octet #thpt</sub>

---

**Số cặp electron hóa trị, kiểu lai hóa và dạng hình học phân tử** — *Steric number, hybridization and molecular geometry*

$$SN = \sigma + E : \begin{cases} SN = 2 & sp,\; \text{thang, } 180^{\circ} \\ SN = 3 & sp^{2},\; \text{tam giac phang, } 120^{\circ} \\ SN = 4 & sp^{3},\; \text{tu dien, } 109.5^{\circ} \end{cases}$$

Trong đó: `SN` là số cặp electron hóa trị quanh nguyên tử trung tâm; `\sigma` là số liên kết sigma với nguyên tử xung quanh; `E` là số cặp electron hóa trị riêng của nguyên tử trung tâm.

*Điều kiện:* Mô hình VSEPR; liên kết bội tính là một liên kết sigma

*Ghi chú:* Cặp electron riêng đẩy mạnh hơn nên làm giảm góc liên kết: CH4 109.5 độ, NH3 khoảng 107 độ, H2O khoảng 104.5 độ.

<sub>`chemistry.thpt.lien-ket.so-cap-electron-va-lai-hoa` · lớp 10 · #lai-hoa #vsepr #hinh-hoc-phan-tu</sub>

---

**Quan hệ giữa bậc liên kết, độ dài liên kết và năng lượng liên kết** — *Bond order, bond length and bond energy*

$$\text{Bac lien ket} \uparrow \;\Rightarrow\; d \downarrow \;\text{va}\; E_{b} \uparrow$$

Trong đó: `d` là độ dài liên kết (pm); `E_{b}` là năng lượng liên kết (kJ/mol).

*Điều kiện:* So sánh giữa các liên kết cùng loại nguyên tử

*Ghi chú:* Ví dụ với C-C: liên kết đơn khoảng 154 pm, liên kết đôi khoảng 134 pm, liên kết ba khoảng 120 pm. 1 pm = 1e-12 m.

<sub>`chemistry.thpt.lien-ket.do-dai-lien-ket` · lớp 10 · #do-dai-lien-ket #bac-lien-ket #nang-luong-lien-ket</sub>

---

**Năng lượng liên kết** — *Bond dissociation energy*

$$E_{b}(\mathrm{A-B}) : \mathrm{AB}(g) \rightarrow \mathrm{A}(g) + \mathrm{B}(g), \; \Delta H = +E_{b}$$

Trong đó: `E_{b}(\mathrm{A-B})` là năng lượng liên kết A-B (kJ/mol); `\Delta H` là biến thiên enthalpy của quá trình phá vỡ liên kết (kJ/mol).

*Điều kiện:* Các chất ở thể khí; giá trị thường là năng lượng liên kết trung bình

*Ghi chú:* Phá vỡ liên kết luôn thu nhiệt (dấu dương), hình thành liên kết luôn tỏa nhiệt (dấu âm). Năng lượng liên kết càng lớn thì liên kết càng bền.

<sub>`chemistry.thpt.lien-ket.nang-luong-lien-ket` · lớp 10 · #nang-luong-lien-ket #nhiet-hoa-hoc #thpt</sub>

---

**Hiệu độ âm điện và loại liên kết** — *Electronegativity difference and bond type*

$$\Delta \chi = \left| \chi_{A} - \chi_{B} \right| : \begin{cases} 0 \le \Delta \chi < 0.4 & \text{cong hoa tri khong cuc} \\ 0.4 \le \Delta \chi < 1.7 & \text{cong hoa tri co cuc} \\ \Delta \chi \ge 1.7 & \text{lien ket ion} \end{cases}$$

Trong đó: `\Delta \chi` là hiệu độ âm điện giữa hai nguyên tử; `\chi_{A}` là độ âm điện của nguyên tử A; `\chi_{B}` là độ âm điện của nguyên tử B.

*Điều kiện:* Dùng thang độ âm điện Pauling; chỉ mang tính quy ước tương đối

*Ghi chú:* Độ âm điện lớn nhất là F (3.98), nhỏ nhất trong các nguyên tố phổ biến là Cs (0.79).

<sub>`chemistry.thpt.lien-ket.hieu-do-am-dien` · lớp 10 · #do-am-dien #lien-ket-ion #cong-hoa-tri</sub>

---

**Quy tắc octet (quy tắc bát tử)** — *Octet rule*

$$\text{So electron lop ngoai cung sau lien ket} = 8 \;(\text{hoac } 2 \text{ voi He, H, Li, Be})$$

Trong đó: `\text{So electron lop ngoai cung}` là số electron ở lớp ngoài cùng của nguyên tử trong phân tử hoặc ion.

*Điều kiện:* Áp dụng tốt cho nguyên tố chu kì 2; nhiều ngoại lệ với nguyên tố chu kì 3 trở đi (SF6, PCl5, BF3, NO)

*Ghi chú:* Nguyên tử có xu hướng nhường, nhận hoặc góp chung electron để đạt cấu hình bền vững của khí hiếm gần nhất.

<sub>`chemistry.thpt.lien-ket.quy-tac-octet` · lớp 10 · #octet #lien-ket-hoa-hoc #thpt</sub>

---

### Nhiệt hóa học

**Biến thiên enthalpy xác định từ thí nghiệm nhiệt lượng kế** — *Enthalpy change from calorimetry*

$$\Delta_{r}H = -\dfrac{Q}{n}$$

Trong đó: `\Delta_{r}H` là biến thiên enthalpy của phản ứng (J/mol); `Q` là nhiệt lượng dung dịch nhận được (J); `n` là số mol chất phản ứng hết theo phương trình (mol).

*Điều kiện:* Áp suất không đổi; hệ cách nhiệt tốt

*Ghi chú:* Dấu trừ vì nhiệt lượng dung dịch nhận được chính là nhiệt lượng phản ứng tỏa ra. Nhiệt độ tăng nghĩa là phản ứng tỏa nhiệt.

<sub>`chemistry.thpt.nhiet-hoa.enthalpy-tu-nhiet-luong-ke` · lớp 10 · #nhiet-luong-ke #enthalpy #thuc-hanh</sub>

---

**Nhiệt lượng trao đổi trong nhiệt lượng kế** — *Heat exchanged in a calorimeter*

$$Q = m \cdot c \cdot \Delta t$$

Trong đó: `Q` là nhiệt lượng dung dịch hấp thụ hoặc giải phóng (J); `m` là khối lượng dung dịch trong nhiệt lượng kế (g); `c` là nhiệt dung riêng của dung dịch (J/(g.K)); `\Delta t` là độ biến thiên nhiệt độ (K).

*Điều kiện:* Bỏ qua nhiệt lượng mà nhiệt lượng kế hấp thụ; dung dịch loãng

*Ghi chú:* Nhiệt dung riêng của nước c = 4.18 J/(g.K). Delta t tính theo độ C hay K đều cho cùng giá trị.

<sub>`chemistry.thpt.nhiet-hoa.nhiet-luong-nhiet-luong-ke` · lớp 10 · #nhiet-luong-ke #nhiet-dung-rieng #thuc-hanh</sub>

---

**Nhiệt tạo thành chuẩn của một chất** — *Standard enthalpy of formation*

$$\Delta_{f}H_{298}^{0} \;:\; \text{cac don chat ben} \rightarrow 1\;\text{mol chat}, \quad \Delta_{f}H_{298}^{0}(\text{don chat ben}) = 0$$

Trong đó: `\Delta_{f}H_{298}^{0}` là nhiệt tạo thành chuẩn (enthalpy tạo thành chuẩn) của chất (kJ/mol).

*Điều kiện:* Tạo thành đúng 1 mol chất từ các đơn chất bền nhất ở điều kiện chuẩn (1 bar, 298 K)

*Ghi chú:* Quy ước nhiệt tạo thành chuẩn của đơn chất ở dạng bền nhất bằng 0, ví dụ O2(g), N2(g), C(graphite), Br2(l).

<sub>`chemistry.thpt.nhiet-hoa.nhiet-tao-thanh-chuan` · lớp 10 · #nhiet-tao-thanh #enthalpy #thpt</sub>

---

**Nhiệt lượng tỏa ra khi đốt cháy nhiên liệu** — *Heat released by burning a fuel*

$$Q = n \cdot \left| \Delta_{c}H_{298}^{0} \right| = \dfrac{m}{M} \cdot \left| \Delta_{c}H_{298}^{0} \right|$$

Trong đó: `Q` là nhiệt lượng tỏa ra (kJ); `n` là số mol nhiên liệu bị đốt cháy (mol); `\Delta_{c}H_{298}^{0}` là nhiệt đốt cháy chuẩn của nhiên liệu (kJ/mol); `m` là khối lượng nhiên liệu (g); `M` là khối lượng mol nhiên liệu (g/mol).

*Điều kiện:* Đốt cháy hoàn toàn 1 mol chất trong khí oxi dư ở điều kiện chuẩn

*Ghi chú:* Nhiệt đốt cháy luôn có giá trị âm vì phản ứng cháy luôn tỏa nhiệt.

<sub>`chemistry.thpt.nhiet-hoa.nhiet-dot-chay` · lớp 10 · #nhiet-dot-chay #nhien-lieu #enthalpy</sub>

---

**Dấu của biến thiên enthalpy trong phản ứng tỏa nhiệt và thu nhiệt** — *Sign of enthalpy change: exothermic and endothermic*

$$\begin{cases} \Delta_{r}H_{298}^{0} < 0 & \text{phan ung toa nhiet} \\ \Delta_{r}H_{298}^{0} > 0 & \text{phan ung thu nhiet} \end{cases}$$

Trong đó: `\Delta_{r}H_{298}^{0}` là biến thiên enthalpy chuẩn của phản ứng ở 298 K (kJ/mol).

*Điều kiện:* Điều kiện chuẩn: áp suất 1 bar, nhiệt độ thường lấy 298 K (25 độ C), chất ở trạng thái bền nhất

*Ghi chú:* Phản ứng tỏa nhiệt giải phóng năng lượng ra môi trường; phản ứng thu nhiệt cần cung cấp năng lượng.

<sub>`chemistry.thpt.nhiet-hoa.dau-cua-bien-thien-enthalpy` · lớp 10 · #enthalpy #toa-nhiet #thu-nhiet</sub>

---

**Biến thiên enthalpy chuẩn tính theo năng lượng liên kết** — *Reaction enthalpy from bond energies*

$$\Delta_{r}H_{298}^{0} = \sum E_{b}(\text{chat dau}) - \sum E_{b}(\text{san pham})$$

Trong đó: `\Delta_{r}H_{298}^{0}` là biến thiên enthalpy chuẩn của phản ứng (kJ/mol); `E_{b}` là năng lượng liên kết của từng liên kết, nhân với số liên kết tương ứng (kJ/mol).

*Điều kiện:* Chỉ áp dụng khi tất cả các chất trong phản ứng đều ở thể khí

*Ghi chú:* Ngược chiều với công thức theo nhiệt tạo thành: ở đây lấy chất đầu trừ sản phẩm, vì phá vỡ liên kết thu nhiệt.

<sub>`chemistry.thpt.nhiet-hoa.enthalpy-theo-nang-luong-lien-ket` · lớp 10 · #enthalpy #nang-luong-lien-ket #thpt</sub>

---

**Biến thiên enthalpy chuẩn tính theo nhiệt đốt cháy** — *Reaction enthalpy from enthalpies of combustion*

$$\Delta_{r}H_{298}^{0} = \sum \Delta_{c}H_{298}^{0}(\text{chat dau}) - \sum \Delta_{c}H_{298}^{0}(\text{san pham})$$

Trong đó: `\Delta_{r}H_{298}^{0}` là biến thiên enthalpy chuẩn của phản ứng (kJ/mol); `\Delta_{c}H_{298}^{0}` là nhiệt đốt cháy chuẩn của từng chất, nhân với hệ số tỉ lượng tương ứng (kJ/mol).

*Điều kiện:* Mọi chất đều có nhiệt đốt cháy xác định ở điều kiện chuẩn (1 bar, 298 K); sản phẩm cháy quy về CO2(g) và H2O(l)

*Ghi chú:* Chú ý dấu ngược với công thức theo nhiệt tạo thành: ở đây lấy chất đầu trừ sản phẩm. Cả hai đều là hệ quả của định luật Hess.

<sub>`chemistry.thpt.nhiet-hoa.enthalpy-theo-nhiet-dot-chay` · lớp 10 · #nhiet-dot-chay #enthalpy #dinh-luat-hess</sub>

---

**Biến thiên enthalpy chuẩn tính theo nhiệt tạo thành** — *Reaction enthalpy from enthalpies of formation*

$$\Delta_{r}H_{298}^{0} = \sum \Delta_{f}H_{298}^{0}(\text{san pham}) - \sum \Delta_{f}H_{298}^{0}(\text{chat dau})$$

Trong đó: `\Delta_{r}H_{298}^{0}` là biến thiên enthalpy chuẩn của phản ứng (kJ/mol); `\Delta_{f}H_{298}^{0}` là nhiệt tạo thành chuẩn của từng chất, nhân với hệ số tỉ lượng (kJ/mol).

*Điều kiện:* Mọi chất ở điều kiện chuẩn; phải nhân nhiệt tạo thành với hệ số tỉ lượng tương ứng

*Ghi chú:* Mẹo nhớ: sản phẩm trừ chất đầu. Đây là hệ quả của định luật Hess.

<sub>`chemistry.thpt.nhiet-hoa.enthalpy-theo-nhiet-tao-thanh` · lớp 10 · #enthalpy #nhiet-tao-thanh #hess</sub>

---

**Định luật Hess** — *Hess's law*

$$\Delta_{r}H = \Delta_{r}H_{1} + \Delta_{r}H_{2} + \cdots + \Delta_{r}H_{k}$$

Trong đó: `\Delta_{r}H` là biến thiên enthalpy của phản ứng tổng (kJ/mol); `\Delta_{r}H_{i}` là biến thiên enthalpy của giai đoạn thứ i (kJ/mol).

*Điều kiện:* Cùng trạng thái đầu và trạng thái cuối; enthalpy là hàm trạng thái

*Ghi chú:* Nhiệt phản ứng chỉ phụ thuộc trạng thái đầu và cuối, không phụ thuộc đường đi hay số giai đoạn trung gian.

<sub>`chemistry.thpt.nhiet-hoa.dinh-luat-hess` · lớp 10 · #hess #enthalpy #nhiet-hoa-hoc</sub>

---

**Biến thiên enthalpy của phản ứng nghịch và khi nhân hệ số** — *Enthalpy of the reverse and scaled reaction*

$$\Delta_{r}H_{\text{nghich}} = -\Delta_{r}H_{\text{thuan}}, \quad \Delta_{r}H' = p \cdot \Delta_{r}H \;\text{khi nhan he so voi } p$$

Trong đó: `\Delta_{r}H_{\text{thuan}}` là biến thiên enthalpy của phản ứng thuận (kJ/mol); `\Delta_{r}H_{\text{nghich}}` là biến thiên enthalpy của phản ứng nghịch (kJ/mol); `p` là hệ số nhân toàn phương trình; `\Delta_{r}H'` là biến thiên enthalpy sau khi nhân hệ số (kJ/mol).

*Điều kiện:* Cùng điều kiện nhiệt độ và áp suất

*Ghi chú:* Vì vậy nếu phản ứng thuận tỏa nhiệt thì phản ứng nghịch thu nhiệt với cùng độ lớn.

<sub>`chemistry.thpt.nhiet-hoa.enthalpy-phan-ung-nghich` · lớp 10 · #enthalpy #hess #phan-ung-nghich</sub>

---

### Tốc độ phản ứng

**Các yếu tố ảnh hưởng đến tốc độ phản ứng** — *Factors affecting reaction rate*

$$v \uparrow \;\text{khi}\; C \uparrow,\; p_{khi} \uparrow,\; T \uparrow,\; S_{\text{be mat}} \uparrow,\; \text{co xuc tac}$$

Trong đó: `v` là tốc độ phản ứng (mol/(L.s)); `C` là nồng độ chất phản ứng (mol/L); `p_{khi}` là áp suất của chất khí (Pa); `T` là nhiệt độ (K); `S_{\text{be mat}}` là diện tích bề mặt tiếp xúc của chất rắn (m^2).

*Điều kiện:* Yếu tố áp suất chỉ ảnh hưởng khi có chất khí tham gia phản ứng

*Ghi chú:* Chất xúc tác làm tăng tốc độ phản ứng nhưng không bị tiêu hao và không làm chuyển dịch cân bằng.

<sub>`chemistry.thpt.toc-do.cac-yeu-to-anh-huong` · lớp 10 · #yeu-to-anh-huong #xuc-tac #toc-do-phan-ung</sub>

---

**Tốc độ trung bình theo biến thiên nồng độ một chất** — *Average rate from concentration change*

$$\overline{v} = -\dfrac{\Delta C_{\text{chat dau}}}{\Delta t} = +\dfrac{\Delta C_{\text{san pham}}}{\Delta t}$$

Trong đó: `\overline{v}` là tốc độ trung bình của phản ứng theo chất đang xét (mol/(L.s)); `\Delta C` là biến thiên nồng độ của chất trong khoảng thời gian xét (mol/L); `\Delta t` là khoảng thời gian (s).

*Điều kiện:* Thể tích hệ không đổi; tốc độ luôn là đại lượng dương

*Ghi chú:* Dấu trừ đặt trước biến thiên nồng độ chất đầu vì nồng độ chất đầu giảm dần theo thời gian.

<sub>`chemistry.thpt.toc-do.toc-do-trung-binh-theo-mot-chat` · lớp 10 · #toc-do-phan-ung #toc-do-trung-binh #thpt</sub>

---

**Tốc độ trung bình tổng quát của phản ứng** — *General average reaction rate*

$$\overline{v} = -\dfrac{1}{a}\dfrac{\Delta C_{A}}{\Delta t} = -\dfrac{1}{b}\dfrac{\Delta C_{B}}{\Delta t} = \dfrac{1}{c}\dfrac{\Delta C_{C}}{\Delta t} = \dfrac{1}{d}\dfrac{\Delta C_{D}}{\Delta t}$$

Trong đó: `\overline{v}` là tốc độ trung bình của phản ứng (mol/(L.s)); `a` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD; `b` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD; `c` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD; `d` là hệ số tỉ lượng trong phương trình aA + bB -> cC + dD; `\Delta t` là khoảng thời gian (s); `\Delta C_{A}` là biến thiên nồng độ của các chất A, B, C, D trong khoảng thời gian xét (mol/L); `\Delta C_{B}` là biến thiên nồng độ của các chất A, B, C, D trong khoảng thời gian xét (mol/L); `\Delta C_{C}` là biến thiên nồng độ của các chất A, B, C, D trong khoảng thời gian xét (mol/L); `\Delta C_{D}` là biến thiên nồng độ của các chất A, B, C, D trong khoảng thời gian xét (mol/L).

*Điều kiện:* Phản ứng aA + bB -> cC + dD xảy ra trong hệ có thể tích không đổi

*Ghi chú:* Nhờ chia cho hệ số tỉ lượng, tốc độ phản ứng có giá trị duy nhất dù tính theo chất nào.

<sub>`chemistry.thpt.toc-do.toc-do-trung-binh-tong-quat` · lớp 10 · #toc-do-phan-ung #he-so-ti-luong #thpt</sub>

---

**Bậc chung của phản ứng** — *Overall reaction order*

$$\text{Bac phan ung} = m + n$$

Trong đó: `m` là bậc riêng theo chất A; `n` là bậc riêng theo chất B.

*Điều kiện:* Xác định từ biểu thức tốc độ thực nghiệm

*Ghi chú:* Đơn vị của k phụ thuộc bậc phản ứng: bậc 1 là 1/s, bậc 2 là L/(mol.s), bậc 0 là mol/(L.s).

<sub>`chemistry.thpt.toc-do.bac-phan-ung` · lớp 10 · #bac-phan-ung #toc-do-phan-ung #thpt</sub>

---

**Biểu thức tốc độ phản ứng** — *Rate law expression*

$$v = k \left[ \mathrm{A} \right]^{m} \left[ \mathrm{B} \right]^{n}$$

Trong đó: `v` là tốc độ tức thời của phản ứng (mol/(L.s)); `k` là hằng số tốc độ phản ứng; `\left[ \mathrm{A} \right]` là nồng độ chất A (mol/L); `\left[ \mathrm{B} \right]` là nồng độ chất B (mol/L); `m` là bậc phản ứng riêng theo A; `n` là bậc phản ứng riêng theo B.

*Điều kiện:* m và n xác định bằng thực nghiệm; với phản ứng đơn giản (một giai đoạn) thì m, n bằng hệ số tỉ lượng

*Ghi chú:* Chất rắn nguyên chất và dung môi không xuất hiện trong biểu thức tốc độ. Khi mọi nồng độ bằng 1 mol/L thì v = k.

<sub>`chemistry.thpt.toc-do.bieu-thuc-toc-do` · lớp 10 · #dinh-luat-tac-dung-khoi-luong #hang-so-toc-do #toc-do-phan-ung</sub>

---

**Ý nghĩa của hằng số tốc độ phản ứng** — *Meaning of the rate constant*

$$k = \dfrac{v}{\left[ \mathrm{A} \right]^{m} \left[ \mathrm{B} \right]^{n}}$$

Trong đó: `k` là hằng số tốc độ; `v` là tốc độ phản ứng (mol/(L.s)); `\left[ \mathrm{A} \right]` là nồng độ các chất phản ứng (mol/L); `\left[ \mathrm{B} \right]` là nồng độ các chất phản ứng (mol/L); `m` là bậc riêng tương ứng; `n` là bậc riêng tương ứng.

*Điều kiện:* k chỉ phụ thuộc bản chất phản ứng, nhiệt độ và chất xúc tác; không phụ thuộc nồng độ

*Ghi chú:* k càng lớn phản ứng xảy ra càng nhanh. Tăng nhiệt độ hoặc dùng xúc tác đều làm tăng k.

<sub>`chemistry.thpt.toc-do.hang-so-toc-do` · lớp 10 · #hang-so-toc-do #xuc-tac #toc-do-phan-ung</sub>

---

**Phương trình Arrhenius về sự phụ thuộc của hằng số tốc độ vào nhiệt độ** — *Arrhenius equation*

$$k = A\,e^{-\frac{E_{a}}{RT}} \;\Leftrightarrow\; \ln \dfrac{k_{2}}{k_{1}} = \dfrac{E_{a}}{R}\left( \dfrac{1}{T_{1}} - \dfrac{1}{T_{2}} \right)$$

Trong đó: `k` là hằng số tốc độ phản ứng; `A` là thừa số tần số (hằng số Arrhenius); `E_{a}` là năng lượng hoạt hóa của phản ứng (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `k_{1}` là hằng số tốc độ ở nhiệt độ T1; `k_{2}` là hằng số tốc độ ở nhiệt độ T2; `T_{1}` là nhiệt độ tuyệt đối thứ nhất (K); `T_{2}` là nhiệt độ tuyệt đối thứ hai (K).

*Điều kiện:* T tính theo Kelvin và T > 0; E_a không đổi trong khoảng nhiệt độ khảo sát; đơn vị của k và A phụ thuộc bậc phản ứng

*Ghi chú:* Kiến thức nâng cao (chuyên đề). R = 8.314 J/(mol.K). Đây là cơ sở định lượng của quy tắc Van't Hoff: E_a càng lớn thì tốc độ càng nhạy với nhiệt độ. Chất xúc tác làm giảm E_a nên làm tăng k.

<sub>`chemistry.thpt.toc-do.phuong-trinh-arrhenius` · lớp 10 · #arrhenius #nang-luong-hoat-hoa #toc-do-phan-ung</sub>

---

**Quy tắc Van't Hoff về ảnh hưởng của nhiệt độ** — *Van't Hoff temperature rule*

$$\dfrac{v_{2}}{v_{1}} = \gamma^{\frac{T_{2} - T_{1}}{10}}$$

Trong đó: `v_{1}` là tốc độ phản ứng ở nhiệt độ T1 (mol/(L.s)); `v_{2}` là tốc độ phản ứng ở nhiệt độ T2 (mol/(L.s)); `\gamma` là hệ số nhiệt độ Van't Hoff; `T_{1}` là nhiệt độ ban đầu (K); `T_{2}` là nhiệt độ sau (K).

*Điều kiện:* Gamma thường nhận giá trị từ 2 đến 4; hiệu nhiệt độ tính theo độ C hoặc K đều cho cùng kết quả

*Ghi chú:* Ý nghĩa: cứ tăng 10 độ thì tốc độ phản ứng tăng gamma lần.

<sub>`chemistry.thpt.toc-do.quy-tac-vant-hoff` · lớp 10 · #vant-hoff #nhiet-do #toc-do-phan-ung</sub>

---

**Thời gian phản ứng khi thay đổi nhiệt độ** — *Reaction time change with temperature*

$$\dfrac{t_{1}}{t_{2}} = \gamma^{\frac{T_{2} - T_{1}}{10}}$$

Trong đó: `t_{1}` là thời gian phản ứng ở nhiệt độ T1 (s); `t_{2}` là thời gian phản ứng ở nhiệt độ T2 (s); `\gamma` là hệ số nhiệt độ; `T_{1}` là nhiệt độ ban đầu (K); `T_{2}` là nhiệt độ sau (K).

*Điều kiện:* Cùng lượng chất phản ứng và cùng mức độ chuyển hóa

*Ghi chú:* Thời gian tỉ lệ nghịch với tốc độ nên tăng nhiệt độ làm thời gian phản ứng giảm.

<sub>`chemistry.thpt.toc-do.thoi-gian-phan-ung-theo-vant-hoff` · lớp 10 · #vant-hoff #thoi-gian #toc-do-phan-ung</sub>

---

### Dung dịch

**Nồng độ molan** — *Molality*

$$C_{m} = \dfrac{n_{ct}}{m_{dm}}$$

Trong đó: `C_{m}` là nồng độ molan (mol/kg); `n_{ct}` là số mol chất tan (mol); `m_{dm}` là khối lượng dung môi (kg).

*Điều kiện:* m_dm tính bằng kilogam (chỉ tính dung môi, không tính chất tan)

*Ghi chú:* Khác nồng độ mol ở chỗ nồng độ molan không phụ thuộc nhiệt độ vì dùng khối lượng thay cho thể tích.

<sub>`chemistry.thpt.dung-dich.nong-do-molan` · lớp 10, 11 · #dung-dich #nong-do-molan #thpt</sub>

---

**Phần mol của một cấu tử** — *Mole fraction*

$$x_{i} = \dfrac{n_{i}}{\sum_{k} n_{k}}$$

Trong đó: `x_{i}` là phần mol của cấu tử i; `n_{i}` là số mol cấu tử i (mol); `n_{k}` là số mol của cấu tử thứ k trong hệ (mol).

*Điều kiện:* Tổng số mol của hệ khác 0

*Ghi chú:* Phần mol không có đơn vị và tổng các phần mol trong hệ luôn bằng 1.

<sub>`chemistry.thpt.dung-dich.phan-mol` · lớp 10, 11 · #dung-dich #phan-mol #thpt</sub>

---

**Công thức pha loãng dung dịch theo nồng độ phần trăm** — *Dilution formula (mass percent)*

$$m_{1} \cdot C_{1}\% = m_{2} \cdot C_{2}\%$$

Trong đó: `m_{1}` là khối lượng dung dịch ban đầu (g); `C_{1}\%` là nồng độ phần trăm ban đầu (%); `m_{2}` là khối lượng dung dịch sau pha loãng (g); `C_{2}\%` là nồng độ phần trăm sau pha loãng (%).

*Điều kiện:* Khối lượng chất tan không đổi khi pha loãng bằng dung môi

*Ghi chú:* Khối lượng dung môi cần thêm: m_dm = m_2 - m_1.

<sub>`chemistry.thpt.dung-dich.pha-loang-theo-nong-do-phan-tram` · lớp 10, 11 · #pha-loang #nong-do-phan-tram #dung-dich</sub>

---

### Liên kết hóa học

**Số liên kết sigma và pi trong liên kết bội** — *Sigma and pi bonds in multiple bonds*

$$\begin{cases} \text{lien ket don} & 1\sigma \\ \text{lien ket doi} & 1\sigma + 1\pi \\ \text{lien ket ba} & 1\sigma + 2\pi \end{cases}$$

Trong đó: `\sigma` là liên kết sigma (xen phủ trục); `\pi` là liên kết pi (xen phủ bên).

*Điều kiện:* Áp dụng cho liên kết cộng hóa trị giữa các nguyên tử

*Ghi chú:* Liên kết sigma bền hơn liên kết pi; liên kết pi kém bền nên là trung tâm của phản ứng cộng.

<sub>`chemistry.thpt.lien-ket.so-lien-ket-sigma-va-pi` · lớp 10, 11 · #lien-ket-sigma #lien-ket-pi #cong-hoa-tri</sub>

---

### Đại lượng cơ bản

**Khối lượng riêng của chất khí** — *Density of a gas*

$$D = \dfrac{M}{V_{m}} = \dfrac{pM}{RT}$$

Trong đó: `D` là khối lượng riêng của khí (g/L); `M` là khối lượng mol của khí (g/mol); `V_{m}` là thể tích mol khí ở điều kiện đang xét (L/mol); `p` là áp suất (bar); `R` là hằng số khí (L.bar/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Khí lí tưởng; để D ra g/L phải dùng p (bar), V_m (L/mol) và R = 0.08314 L.bar/(mol.K)

*Ghi chú:* Ở điều kiện chuẩn (25 độ C, 1 bar): D = M/24.79 (g/L); ở đktc (0 độ C, 1 atm): D = M/22.4 (g/L). Nếu dùng p (Pa) và R = 8.314 J/(mol.K) thì pM/(RT) cho kết quả theo g/m^3.

<sub>`chemistry.thpt.dai-luong-co-ban.khoi-luong-rieng-chat-khi` · lớp 10, 11 · #khoi-luong-rieng #khi #thpt</sub>

---

**Phương trình liên hệ hai trạng thái của một lượng khí xác định** — *Combined gas law for a fixed amount of gas*

$$\dfrac{p_{1}V_{1}}{T_{1}} = \dfrac{p_{2}V_{2}}{T_{2}}$$

Trong đó: `p_{1}` là áp suất ở trạng thái 1 (bar); `V_{1}` là thể tích ở trạng thái 1 (L); `T_{1}` là nhiệt độ tuyệt đối ở trạng thái 1 (K); `p_{2}` là áp suất ở trạng thái 2 (bar); `V_{2}` là thể tích ở trạng thái 2 (L); `T_{2}` là nhiệt độ tuyệt đối ở trạng thái 2 (K).

*Điều kiện:* Cùng một lượng khí (số mol không đổi), khí lí tưởng; T phải tính theo Kelvin và T > 0; p1, p2 cùng đơn vị, V1, V2 cùng đơn vị

*Ghi chú:* Suy ra từ pV = nRT khi n không đổi. Dùng để quy thể tích khí đo ở điều kiện phòng về điều kiện chuẩn hoặc đktc.

<sub>`chemistry.thpt.dai-luong-co-ban.phuong-trinh-hai-trang-thai-khi` · lớp 10, 11 · #khi-li-tuong #the-tich #chuyen-doi-dieu-kien</sub>

---

**Phương trình trạng thái khí lí tưởng** — *Ideal gas equation*

$$pV = nRT$$

Trong đó: `p` là áp suất khí (Pa); `V` là thể tích khí (m^3); `n` là số mol khí (mol); `R` là hằng số khí lí tưởng (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Khí lí tưởng; T tính theo Kelvin: T(K) = t(độ C) + 273.15

*Ghi chú:* R = 8.314 J/(mol.K) khi p tính bằng Pa và V bằng m^3; R = 0.08206 L.atm/(mol.K) khi p bằng atm và V bằng L.

<sub>`chemistry.thpt.dai-luong-co-ban.phuong-trinh-khi-li-tuong` · lớp 10, 11 · #khi-li-tuong #phuong-trinh-trang-thai #thpt</sub>

---

**Số mol khí ở điều kiện bất kì** — *Moles of gas at arbitrary conditions*

$$n = \dfrac{pV}{RT}$$

Trong đó: `n` là số mol khí (mol); `p` là áp suất khí (Pa); `V` là thể tích khí (m^3); `R` là hằng số khí lí tưởng (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Khí lí tưởng; đơn vị của p, V phải phù hợp với R

*Ghi chú:* Thay p = 1 bar, T = 298.15 K, R = 8.314 J/(mol.K) thu được V_m = 24.79 L/mol.

<sub>`chemistry.thpt.dai-luong-co-ban.so-mol-khi-dieu-kien-bat-ki` · lớp 10, 11 · #khi-li-tuong #mol #thpt</sub>

---

### Các định luật bảo toàn

**Định luật bảo toàn electron** — *Conservation of electrons*

$$\sum n_{e\,\text{nhuong}} = \sum n_{e\,\text{nhan}}$$

Trong đó: `n_{e\,\text{nhuong}}` là tổng số mol electron do các chất khử nhường (mol); `n_{e\,\text{nhan}}` là tổng số mol electron do các chất oxi hóa nhận (mol).

*Điều kiện:* Phản ứng oxi hóa - khử xảy ra hoàn toàn trong hệ đang xét

*Ghi chú:* Số mol electron của một chất: n_e = n_chat x (độ biến thiên số oxi hóa).

<sub>`chemistry.thpt.bao-toan.bao-toan-electron` · lớp 10, 11, 12 · #bao-toan-electron #oxi-hoa-khu #thpt</sub>

---

**Định luật bảo toàn electron** — *Conservation of electrons in redox processes*

$$\sum n_{e\ nhuong} = \sum n_{e\ nhan}$$

Trong đó: `n_{e\ nhuong}` là số mol electron do các chất khử nhường (mol); `n_{e\ nhan}` là số mol electron do các chất oxi hóa nhận (mol).

*Điều kiện:* Quá trình oxi hóa - khử; chỉ cần so sánh trạng thái đầu và trạng thái cuối, không cần viết các phương trình trung gian

*Ghi chú:* Với kim loại M hóa trị a thì n(e nhường) = a·n(M). Đây là công cụ chủ lực cho bài toán kim loại tác dụng HNO3, H2SO4 đặc và bài toán điện phân.

<sub>`chemistry.thpt.bao-toan.electron` · lớp 10, 11, 12 · #bao-toan-electron #dai-cuong #giai-nhanh</sub>

---

**Định luật bảo toàn khối lượng** — *Law of conservation of mass*

$$\sum m_{chat\ tham\ gia} = \sum m_{san\ pham}$$

Trong đó: `m_{chat\ tham\ gia}` là khối lượng các chất phản ứng (g); `m_{san\ pham}` là khối lượng các sản phẩm (g).

*Điều kiện:* Hệ kín, mọi phản ứng hóa học

*Ghi chú:* Kết hợp với bảo toàn nguyên tố và bảo toàn electron là bộ ba công cụ giải nhanh mạnh nhất.

<sub>`chemistry.thpt.bao-toan.khoi-luong` · lớp 10, 11, 12 · #bao-toan-khoi-luong #dai-cuong #giai-nhanh</sub>

---

**Định luật bảo toàn nguyên tố** — *Conservation of elements*

$$\sum n_{X\,(\text{truoc phan ung})} = \sum n_{X\,(\text{sau phan ung})}$$

Trong đó: `n_{X}` là tổng số mol nguyên tố X trong tất cả các chất (mol).

*Điều kiện:* Không phải phản ứng hạt nhân; tính đủ mọi chất chứa nguyên tố X

*Ghi chú:* Ví dụ đốt cháy hiđrocacbon: n_C = n_CO2 và n_H = 2 n_H2O.

<sub>`chemistry.thpt.bao-toan.bao-toan-nguyen-to` · lớp 10, 11, 12 · #bao-toan-nguyen-to #dinh-luat #thpt</sub>

---

**Định luật bảo toàn nguyên tố** — *Conservation of each element*

$$\sum n_{X(truoc\ pu)} = \sum n_{X(sau\ pu)}$$

Trong đó: `n_{X(truoc\ pu)}` là số mol nguyên tử nguyên tố X trong các chất trước phản ứng (mol); `n_{X(sau\ pu)}` là số mol nguyên tử nguyên tố X trong các chất sau phản ứng (mol).

*Điều kiện:* Áp dụng cho từng nguyên tố riêng biệt trong mọi quá trình hóa học

*Ghi chú:* Ví dụ: đốt cháy hợp chất hữu cơ, n(C trong X) = n(CO2); n(H trong X) = 2n(H2O).

<sub>`chemistry.thpt.bao-toan.nguyen-to` · lớp 10, 11, 12 · #bao-toan-nguyen-to #dai-cuong #giai-nhanh</sub>

---

**Hiệu suất phản ứng tính theo chất phản ứng** — *Percent conversion based on a reactant*

$$H\% = \dfrac{n_{\text{da phan ung}}}{n_{\text{ban dau}}} \times 100\%$$

Trong đó: `H\%` là hiệu suất (độ chuyển hóa) (%); `n_{\text{da phan ung}}` là số mol chất đã phản ứng (mol); `n_{\text{ban dau}}` là số mol chất ban đầu (mol).

*Điều kiện:* Hiệu suất phải tính theo chất phản ứng hết trước (chất thiếu)

*Ghi chú:* So sánh tỉ lệ n/hệ số của các chất tham gia để xác định chất hết trước.

<sub>`chemistry.thpt.bao-toan.hieu-suat-theo-chat-phan-ung` · lớp 10, 11, 12 · #hieu-suat #do-chuyen-hoa #thpt</sub>

---

**Khối lượng sản phẩm thực tế theo hiệu suất** — *Actual product mass from percent yield*

$$m_{tt} = m_{lt} \cdot \dfrac{H\%}{100}$$

Trong đó: `m_{tt}` là khối lượng sản phẩm thực tế (g); `m_{lt}` là khối lượng sản phẩm lí thuyết (g); `H\%` là hiệu suất phản ứng (%).

*Điều kiện:* 0 < H% <= 100

*Ghi chú:* Ngược lại, lượng chất đầu cần dùng: m_dau = m_lt x 100/H%.

<sub>`chemistry.thpt.bao-toan.khoi-luong-thuc-te-theo-hieu-suat` · lớp 10, 11, 12 · #hieu-suat #san-pham #tinh-toan</sub>

---

### Cân bằng acid - base quốc tế

**Phần trăm điện li của acid yếu và ảnh hưởng của sự pha loãng** — *Percent ionization of a weak acid and the effect of dilution*

$$\alpha_{\%} = \dfrac{[\mathrm{H_{3}O^{+}}]_{cb}}{C_{0}} \times 100\% \approx \sqrt{\dfrac{K_{a}}{C_{0}}} \times 100\%$$

Trong đó: `\alpha_{\%}` là phần trăm điện li của acid yếu (); `[\mathrm{H_{3}O^{+}}]_{cb}` là nồng độ ion hydronium lúc cân bằng (mol/L); `C_{0}` là nồng độ ban đầu của acid yếu (mol/L); `K_{a}` là hằng số phân li của acid yếu ().

*Điều kiện:* Acid yếu đơn nấc, bỏ qua sự điện li của nước; dạng căn ở vế phải chỉ dùng khi phép xấp xỉ bỏ qua x hợp lệ, tức C0/Ka lớn hơn khoảng 400

*Ghi chú:* AP Chemistry Topic 8.3 'Weak Acid and Base Equilibria' yêu cầu giải thích rằng chỉ một phần trăm nhỏ phân tử acid yếu bị ion hoá; IB Reactivity 3.1 dùng cùng ý. Kết luận quan trọng nhất và cũng là câu bẫy hay gặp: khi PHA LOÃNG thì phần trăm điện li TĂNG (vì alpha tỉ lệ nghịch với căn bậc hai của C0) trong khi Ka KHÔNG ĐỔI, và pH vẫn tăng vì dung dịch bớt acid hơn. Phân biệt rõ với độ điện li alpha của CT GDPT 2018 Việt Nam: Việt Nam nêu alpha như một tỉ số tổng quát, còn AP và IB gắn nó với Ka và với hành vi khi pha loãng.

<sub>`chemistry.thpt.axit-bazo-quoc-te.phan-tram-dien-li` · lớp 10, 11, 12 · #ap #ib #acid-yeu #phan-tram-dien-li</sub>

---

**Các nấc phân li của acid đa nấc** — *Successive dissociation constants of a polyprotic acid*

$$K_{a1} \gg K_{a2} \gg K_{a3}, \qquad \dfrac{K_{a1}}{K_{a2}} \sim 10^{4} - 10^{6}$$

Trong đó: `K_{a1}` là hằng số phân li nấc thứ nhất (); `K_{a2}` là hằng số phân li nấc thứ hai (); `K_{a3}` là hằng số phân li nấc thứ ba ().

*Điều kiện:* Vì các nấc chênh nhau rất nhiều nên pH của dung dịch acid đa nấc hầu như chỉ do nấc thứ nhất quyết định

*Ghi chú:* AP Unit 8 và IB HL. Hệ quả trên đường chuẩn độ: acid đa nấc cho nhiều bước nhảy, mỗi bước ứng với một nấc; giữa hai điểm tương đương là vùng đệm với pH = pKa tương ứng. Ranh giới của AP: CED có exclusion statement 'Computation of the concentration of each species present in the titration curve for polyprotic acids will not be assessed on the AP Exam' - AP chỉ hỏi lập luận định tính và nhận dạng vùng đệm, còn tính số cụ thể thì chỉ với acid đơn nấc. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam giới thiệu acid nhiều nấc nhưng không khai thác định lượng.

<sub>`chemistry.thpt.axit-bazo-quoc-te.axit-da-nac-cac-nac` · lớp 10, 11, 12 · #ap #ib-hl #acid-da-nac #chuan-do</sub>

---

**Điểm cuối, điểm tương đương và sai số chuẩn độ** — *End point, equivalence point and titration error*

$$E_{cd} = \dfrac{V_{cuoi} - V_{td}}{V_{td}} \times 100\%$$

Trong đó: `E_{cd}` là sai số chuẩn độ tính theo phần trăm (); `V_{cuoi}` là thể tích tại điểm cuối, nơi chỉ thị đổi màu (mL); `V_{td}` là thể tích tại điểm tương đương lí thuyết (mL).

*Điều kiện:* Sai số nhỏ khi khoảng đổi màu của chỉ thị nằm trong bước nhảy pH; luôn khác 0 vì hai điểm không trùng nhau

*Ghi chú:* IB và A-Level phân biệt rất rõ equivalence point (khái niệm hoá học lượng) với end point (quan sát thực nghiệm); AP cũng hỏi khái niệm này. CT GDPT 2018 Việt Nam thường dùng lẫn hai thuật ngữ và không định lượng sai số chuẩn độ.

<sub>`chemistry.thpt.axit-bazo-quoc-te.sai-so-chuan-do` · lớp 10, 11, 12 · #ib #a-level #ap #chuan-do #sai-so</sub>

---

**Khoảng đổi màu của chỉ thị và cách chọn chỉ thị** — *Indicator transition range and indicator selection*

$$\mathrm{pH}_{doi\ mau} = \mathrm{p}K_{In} \pm 1$$

Trong đó: `\mathrm{pH}_{doi\ mau}` là khoảng pH trong đó quan sát được sự đổi màu của chỉ thị; `\mathrm{p}K_{In}` là chỉ số phân li của chỉ thị, chỉ thị là một acid yếu HIn.

*Điều kiện:* Chỉ thị phù hợp khi khoảng đổi màu nằm trọn trong bước nhảy pH của đường chuẩn độ

*Ghi chú:* AP Unit 8, IB Reactivity 3.1 và A-Level AQA/Edexcel dùng pK_In để chọn chỉ thị. Ranh giới cần nhớ: Cambridge 9701 ghi rõ 'select suitable indicators for acid-alkali titrations, given appropriate data (pKa values will not be used)', tức CIE chỉ cho đọc khoảng đổi màu tra bảng chứ không tính qua pK_In. Ví dụ: phenolphthalein (khoảng 8,3 - 10,0) hợp cho chuẩn độ acid yếu bằng base mạnh; methyl orange (khoảng 3,1 - 4,4) hợp cho chuẩn độ base yếu bằng acid mạnh. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam nêu chỉ thị định tính, không dùng pK_In.

<sub>`chemistry.thpt.axit-bazo-quoc-te.chi-thi-khoang-doi-mau` · lớp 10, 11, 12 · #ap #ib #a-level #chi-thi #chuan-do</sub>

---

**Dung lượng đệm của dung dịch** — *Buffer capacity*

$$\beta = \dfrac{\Delta n_{b}}{\Delta \mathrm{pH}}$$

Trong đó: `\beta` là dung lượng đệm: số mol base mạnh cần thêm vào 1 lít dung dịch để pH tăng 1 đơn vị (mol/L); `\Delta n_{b}` là số mol base mạnh (hoặc acid mạnh) thêm vào mỗi lít dung dịch (mol/L); `\Delta \mathrm{pH}` là độ biến thiên pH tương ứng ().

*Điều kiện:* Dung lượng đệm lớn nhất khi pH = pKa và khi tổng nồng độ hai cấu tử đệm lớn

*Ghi chú:* AP Unit 8 và IB HL yêu cầu giải thích định tính rằng dung dịch đệm đặc hơn thì chống thay đổi pH tốt hơn. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam không có khái niệm dung lượng đệm.

<sub>`chemistry.thpt.axit-bazo-quoc-te.dung-luong-dem` · lớp 10, 11, 12 · #ap #ib-hl #dung-dich-dem #dung-luong-dem</sub>

---

**Khoảng đệm hiệu quả của một hệ đệm** — *Effective buffer range*

$$\mathrm{p}K_{a} - 1 \le \mathrm{pH} \le \mathrm{p}K_{a} + 1 \quad \Leftrightarrow \quad \dfrac{1}{10} \le \dfrac{[\mathrm{A^{-}}]}{[\mathrm{HA}]} \le 10$$

Trong đó: `\mathrm{p}K_{a}` là chỉ số phân li của acid yếu tạo đệm; `\mathrm{pH}` là pH của dung dịch đệm; `[\mathrm{A^{-}}]` là nồng độ base liên hợp (mol/L); `[\mathrm{HA}]` là nồng độ acid yếu (mol/L).

*Điều kiện:* Ngoài khoảng này hệ mất khả năng đệm vì một trong hai cấu tử gần cạn kiệt

*Ghi chú:* Tiêu chí chọn hệ đệm trong AP Unit 8, IB HL và A-Level: chọn acid yếu có pKa gần nhất với pH mong muốn. CT GDPT 2018 Việt Nam có phương trình Henderson - Hasselbalch nhưng không nêu khoảng đệm hiệu quả.

<sub>`chemistry.thpt.axit-bazo-quoc-te.khoang-dem-hieu-qua` · lớp 10, 11, 12 · #ap #ib-hl #dung-dich-dem #pka</sub>

---

**pH của dung dịch đệm sau khi thêm acid mạnh hoặc base mạnh** — *pH of a buffer after adding a strong acid or a strong base*

$$\mathrm{pH} = \mathrm{p}K_{a} + \log \dfrac{n_{A^{-}} \mp n_{s}}{n_{HA} \pm n_{s}}$$

Trong đó: `\mathrm{pH}` là pH của dung dịch đệm sau khi thêm; `\mathrm{p}K_{a}` là chỉ số phân li của acid yếu tạo đệm; `n_{A^{-}}` là số mol base liên hợp trước khi thêm (mol); `n_{HA}` là số mol acid yếu trước khi thêm (mol); `n_{s}` là số mol acid mạnh (lấy dấu trên) hoặc base mạnh (lấy dấu dưới) thêm vào (mol).

*Điều kiện:* Acid mạnh thêm vào chuyển A- thành HA; base mạnh thêm vào chuyển HA thành A-; n_s phải nhỏ hơn cả hai số mol có sẵn

*Ghi chú:* IB HL Reactivity 3.1 và A-Level (AQA 3.1.12, Cambridge 9701 mục 25.2) đều yêu cầu tính lại pH của dung dịch đệm sau khi thêm acid mạnh hoặc base mạnh. KHÔNG được gán cho AP: CED của AP Chemistry có exclusion statement 'Computation of the change in pH resulting from the addition of an acid or a base to a buffer will not be assessed on the AP Exam'. Mẹo quan trọng: tính theo SỐ MOL chứ không theo nồng độ vì thể tích triệt tiêu trong tỉ số, nhờ đó pha loãng đệm gần như không đổi pH. CT GDPT 2018 Việt Nam chưa có dạng bài này.

<sub>`chemistry.thpt.axit-bazo-quoc-te.ph-dem-sau-khi-them-axit` · lớp 10, 11, 12 · #ib-hl #a-level #dung-dich-dem #henderson-hasselbalch</sub>

---

**pH của dung dịch muối lưỡng tính** — *pH of an amphiprotic salt solution*

$$\mathrm{pH} = \tfrac{1}{2}\left( \mathrm{p}K_{a1} + \mathrm{p}K_{a2} \right)$$

Trong đó: `\mathrm{pH}` là pH của dung dịch muối lưỡng tính, ví dụ NaHCO3 hoặc NaH2PO4; `\mathrm{p}K_{a1}` là chỉ số phân li nấc 1 của acid đa nấc tương ứng; `\mathrm{p}K_{a2}` là chỉ số phân li nấc 2 của acid đa nấc tương ứng.

*Điều kiện:* Dung dịch không quá loãng; ion lưỡng tính vừa cho vừa nhận proton nên pH gần như không phụ thuộc nồng độ

*Ghi chú:* SỬA PHẠM VI CHƯƠNG TRÌNH: công thức pH = (pKa1 + pKa2)/2 là kết quả chuẩn của hoá phân tích đại học và của đề olympic, KHÔNG nằm trong bảng công thức AP, IB hay A-Level. IB Reactivity 3.1 chỉ yêu cầu nhận biết tiểu phân lưỡng tính (amphiprotic) ở mức định tính; CED của AP loại trừ việc tính nồng độ từng tiểu phân trong đường chuẩn độ acid đa nấc. Kết quả đáng nhớ: pH của dung dịch NaHCO3 xấp xỉ 8,3 bất kể nồng độ. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam không có công thức này.

<sub>`chemistry.thpt.axit-bazo-quoc-te.ph-muoi-luong-tinh` · lớp 10, 11, 12 · #olympiad #luong-tinh #acid-da-nac #hoa-phan-tich</sub>

---

**Sự phụ thuộc của Kw vào nhiệt độ và pH trung tính** — *Temperature dependence of Kw and the neutral pH*

$$\mathrm{pH}_{trung\ tinh} = \tfrac{1}{2}\,\mathrm{p}K_{w}(T)$$

Trong đó: `\mathrm{pH}_{trung\ tinh}` là pH của nước nguyên chất ở nhiệt độ T; `\mathrm{p}K_{w}(T)` là chỉ số tích số ion của nước ở nhiệt độ T, bằng trừ logarit của Kw.

*Điều kiện:* Sự tự ion hoá của nước là quá trình THU nhiệt nên Kw tăng khi nhiệt độ tăng

*Ghi chú:* Điểm phân biệt quan trọng của A-Level (AQA, CIE) và IB: ở 25 độ C thì pKw = 14,00 và nước trung tính có pH = 7,00; ở nhiệt độ cao hơn Kw lớn hơn nên pH trung tính NHỎ hơn 7 mặc dù nước vẫn trung tính (vì [H+] = [OH-]). CT GDPT 2018 Việt Nam mặc định Kw = 1,0x10^-14 và pH trung tính luôn bằng 7.

<sub>`chemistry.thpt.axit-bazo-quoc-te.kw-phu-thuoc-nhiet-do` · lớp 10, 11, 12 · #a-level #ib #kw #nhiet-do</sub>

---

**Bốn mốc pH trên đường chuẩn độ acid yếu bằng base mạnh** — *The four key pH regions when titrating a weak acid with a strong base*

$$\begin{cases} V = 0 & \mathrm{pH} = \tfrac{1}{2}\left( \mathrm{p}K_{a} - \log C_{a} \right) \\ 0 < V < V_{td} & \mathrm{pH} = \mathrm{p}K_{a} + \log \dfrac{n_{A^{-}}}{n_{HA}} \\ V = V_{td} & \mathrm{pH} = 7 + \tfrac{1}{2}\left( \mathrm{p}K_{a} + \log C_{A^{-}} \right) \\ V > V_{td} & \mathrm{pH} = 14 + \log C_{OH^{-}} \end{cases}$$

Trong đó: `V` là thể tích base mạnh đã thêm (mL); `V_{td}` là thể tích base mạnh tại điểm tương đương (mL); `\mathrm{pH}` là pH của dung dịch; `\mathrm{p}K_{a}` là chỉ số phân li của acid yếu; `C_{a}` là nồng độ acid yếu ban đầu (mol/L); `n_{A^{-}}` là số mol base liên hợp đã tạo thành (mol); `n_{HA}` là số mol acid yếu còn lại (mol); `C_{A^{-}}` là nồng độ base liên hợp tại điểm tương đương, đã tính pha loãng (mol/L); `C_{OH^{-}}` là nồng độ hydroxide dư sau điểm tương đương (mol/L).

*Điều kiện:* Acid yếu đơn nấc, base mạnh; các công thức ở nhiệt độ 25 độ C và dùng phép xấp xỉ nồng độ đầu

*Ghi chú:* AP Unit 8 và IB HL yêu cầu tính pH ở cả bốn vùng của một đường chuẩn độ. Điểm tương đương của acid yếu luôn có pH > 7 do base liên hợp thuỷ phân. Kho AISTEM đã có bản đại học; CT GDPT 2018 Việt Nam chỉ tính pH từng trường hợp rời rạc, không xâu chuỗi theo đường chuẩn độ.

<sub>`chemistry.thpt.axit-bazo-quoc-te.bon-moc-ph-chuan-do-axit-yeu` · lớp 10, 11, 12 · #ap #ib-hl #chuan-do #duong-cong-chuan-do</sub>

---

**pH tại điểm nửa tương đương bằng pKa** — *pH at the half-equivalence point equals pKa*

$$V = \tfrac{1}{2}V_{td} \Rightarrow [\mathrm{HA}] = [\mathrm{A^{-}}] \Rightarrow \mathrm{pH} = \mathrm{p}K_{a}$$

Trong đó: `V` là thể tích base mạnh đã thêm vào (mL); `V_{td}` là thể tích base mạnh cần để tới điểm tương đương (mL); `[\mathrm{HA}]` là nồng độ acid yếu còn lại (mol/L); `[\mathrm{A^{-}}]` là nồng độ base liên hợp đã tạo thành (mol/L); `\mathrm{pH}` là pH của dung dịch tại điểm nửa tương đương; `\mathrm{p}K_{a}` là chỉ số phân li acid, bằng trừ logarit của Ka.

*Điều kiện:* Chuẩn độ acid yếu đơn nấc bằng base mạnh; suy trực tiếp từ phương trình Henderson - Hasselbalch

*Ghi chú:* Phương pháp thực nghiệm chuẩn để XÁC ĐỊNH Ka của acid yếu trong AP (Unit 8), IB và A-Level: đọc pH tại nửa thể tích tương đương trên đường chuẩn độ. Dung dịch tại đó có dung lượng đệm lớn nhất. CT GDPT 2018 Việt Nam có phương trình Henderson - Hasselbalch nhưng không khai thác điểm nửa tương đương.

<sub>`chemistry.thpt.axit-bazo-quoc-te.ph-nua-diem-tuong-duong` · lớp 10, 11, 12 · #ap #ib #a-level #chuan-do #pka</sub>

---

**So sánh bốn loại đường cong chuẩn độ acid - base** — *Comparing the four types of acid-base titration curve*

$$\mathrm{pH}_{td} \begin{cases} = 7 & \text{acid manh - base manh} \\ > 7 & \text{acid yeu - base manh} \\ < 7 & \text{acid manh - base yeu} \\ \approx 7,\ \text{buoc nhay rat nho} & \text{acid yeu - base yeu} \end{cases}$$

Trong đó: `\mathrm{pH}_{td}` là pH tại điểm tương đương của phép chuẩn độ.

*Điều kiện:* Dung dịch loãng ở 25 độ C; bước nhảy pH càng nhỏ khi acid hoặc base càng yếu

*Ghi chú:* AP Unit 8, IB Reactivity 3.1 và A-Level đều yêu cầu nhận dạng bốn dạng đường cong và chọn chỉ thị phù hợp. Không thể chuẩn độ acid yếu bằng base yếu vì bước nhảy quá nhỏ. CT GDPT 2018 Việt Nam chỉ khảo sát chuẩn độ acid mạnh - base mạnh.

<sub>`chemistry.thpt.axit-bazo-quoc-te.so-sanh-cac-loai-duong-cong-chuan-do` · lớp 10, 11, 12 · #ap #ib #a-level #duong-cong-chuan-do</sub>

---

**Định nghĩa acid - base theo Lewis** — *Lewis definition of acids and bases*

$$\mathrm{A} + :\!\mathrm{B} \rightarrow \mathrm{A}\!\leftarrow\!\mathrm{B}$$

Trong đó: `\mathrm{A}` là acid Lewis: tiểu phân NHẬN cặp electron, có orbital trống; `:\!\mathrm{B}` là base Lewis: tiểu phân CHO cặp electron chưa liên kết; `\mathrm{A}\!\leftarrow\!\mathrm{B}` là liên kết cho - nhận (liên kết phối trí) tạo thành.

*Điều kiện:* Không cần có proton; áp dụng được cho cả phản ứng trong dung môi không nước

*Ghi chú:* IB HL dùng khái niệm acid - base Lewis để định nghĩa tác nhân electrophin là acid Lewis và nucleophin là base Lewis (Reactivity 3.4); mọi ion kim loại tạo phức đều là acid Lewis còn phối tử là base Lewis. KHÔNG được gán cho AP: CED của AP Chemistry có exclusion statement 'Lewis acid-base concepts will not be assessed on the AP Exam. The emphasis in AP Chemistry is on reactions in aqueous solution'. Cambridge 9701 cũng không dùng thuật ngữ acid - base Lewis (chỉ dùng 'liên kết cho - nhận' và 'phối tử có cặp electron chưa liên kết'). Ví dụ điển hình: BF3 + NH3. CT GDPT 2018 Việt Nam chỉ dạy Arrhenius và Bronsted - Lowry.

<sub>`chemistry.thpt.axit-bazo-quoc-te.axit-bazo-lewis` · lớp 10, 11, 12 · #ib-hl #ib #lewis #acid-base</sub>

---

### Cân bằng hoá học quốc tế

**Ảnh hưởng của khí trơ đến cân bằng pha khí** — *Effect of an inert gas on a gas-phase equilibrium*

$$\begin{cases} V = \text{const} & \text{can bang khong chuyen dich} \\ P = \text{const} & \text{chuyen dich theo chieu tang } \Delta n \end{cases}$$

Trong đó: `V` là thể tích bình phản ứng (L); `P` là áp suất tổng của hệ (Pa); `\Delta n` là hiệu số mol khí giữa sản phẩm và chất tham gia ().

*Điều kiện:* Khí trơ không tham gia phản ứng; ở thể tích không đổi, áp suất riêng phần các chất phản ứng không đổi nên Q không đổi

*Ghi chú:* Câu hỏi bẫy kinh điển của AP Unit 7 và A-Level. Thêm khí trơ ở thể tích không đổi làm tăng áp suất tổng nhưng KHÔNG chuyển dịch cân bằng; thêm ở áp suất không đổi buộc thể tích tăng nên tương đương pha loãng. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam không phân biệt hai trường hợp này.

<sub>`chemistry.thpt.can-bang-quoc-te.anh-huong-khi-tro` · lớp 10, 11, 12 · #ap #a-level #le-chatelier #khi-tro</sub>

---

**Ảnh hưởng của nhiệt độ lên giá trị hằng số cân bằng** — *Effect of temperature on the value of the equilibrium constant*

$$\Delta H < 0: T \uparrow \Rightarrow K \downarrow; \qquad \Delta H > 0: T \uparrow \Rightarrow K \uparrow$$

Trong đó: `\Delta H` là biến thiên enthalpy của phản ứng thuận (kJ/mol); `T` là nhiệt độ tuyệt đối (K); `K` là hằng số cân bằng ().

*Điều kiện:* Chỉ nhiệt độ mới làm thay đổi giá trị K; nồng độ, áp suất và xúc tác đều không đổi được K

*Ghi chú:* AP Unit 7, IB Reactivity 2.3 và A-Level đều nhấn mạnh điểm này. Hệ quả công nghiệp (quá trình Haber, quá trình Contact): phải chọn nhiệt độ dung hoà giữa hiệu suất cân bằng và tốc độ. CT GDPT 2018 Việt Nam nêu nguyên lí Le Chatelier nhưng không tách bạch việc chỉ nhiệt độ mới làm K thay đổi.

<sub>`chemistry.thpt.can-bang-quoc-te.anh-huong-nhiet-do-len-k` · lớp 10, 11, 12 · #ap #ib #a-level #le-chatelier #hang-so-can-bang</sub>

---

**Hiệu ứng ion chung đối với độ tan** — *Common-ion effect on solubility*

$$K_{sp} = (s + c)\,s \quad \Rightarrow \quad s \approx \dfrac{K_{sp}}{c} \ \ (c \gg s)$$

Trong đó: `K_{sp}` là tích số tan của hợp chất ít tan dạng AB (); `s` là độ tan mol của AB trong dung dịch đã có sẵn ion chung (mol/L); `c` là nồng độ ion chung đưa thêm vào từ chất điện li mạnh (mol/L).

*Điều kiện:* Hợp chất dạng AB (tỉ lệ 1:1); ion chung có nồng độ lớn hơn nhiều so với độ tan

*Ghi chú:* AP Unit 7 và IB HL. Kết luận: thêm ion chung làm GIẢM độ tan nhưng KHÔNG làm thay đổi Ksp. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam có Ksp và điều kiện kết tủa nhưng không có dạng bài tính lại độ tan khi có ion chung.

<sub>`chemistry.thpt.can-bang-quoc-te.hieu-ung-ion-chung` · lớp 10, 11, 12 · #ap #ib-hl #ion-chung #do-tan</sub>

---

**Hằng số tạo phức (hằng số bền): Kf theo sách Mỹ, Kstab theo A-Level** — *Formation (stability) constant of a complex ion*

$$\mathrm{M}^{n+} + x\,\mathrm{L} \rightleftharpoons \mathrm{ML}_{x}^{n+}, \qquad K_{f} = \dfrac{[\mathrm{ML}_{x}^{n+}]}{[\mathrm{M}^{n+}][\mathrm{L}]^{x}}$$

Trong đó: `K_{f}` là hằng số tạo phức (hằng số bền) của ion phức; `[\mathrm{ML}_{x}^{n+}]` là nồng độ cân bằng của ion phức (mol/L); `[\mathrm{M}^{n+}]` là nồng độ cân bằng của ion kim loại tự do (mol/L); `[\mathrm{L}]` là nồng độ cân bằng của phối tử tự do (mol/L); `x` là số phối tử trong ion phức ().

*Điều kiện:* Dung dịch nước, phối tử dư; Kf càng lớn thì phức càng bền

*Ghi chú:* Cambridge 9701 mục 28.5 'Stability constants, Kstab' yêu cầu định nghĩa Kstab, viết biểu thức (không đưa [H2O] vào), tính toán với Kstab và giải thích phản ứng trao đổi phối tử bằng cạnh tranh cân bằng; IB HL (Structure 3.1) bàn về phức chất kim loại chuyển tiếp. Khác biệt kí hiệu: A-Level viết Kstab, sách Mỹ viết Kf. KHÔNG gán cho AP: CED của AP Chemistry không có hằng số tạo phức của ion phức (các cụm từ 'formation constant' và 'complex ion' không xuất hiện trong CED). Ứng dụng: hoà tan AgCl bằng dung dịch NH3 nhờ tạo [Ag(NH3)2]+. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam giới thiệu phức chất định tính, không đưa Kf.

<sub>`chemistry.thpt.can-bang-quoc-te.hang-so-tao-phuc` · lớp 10, 11, 12 · #a-level #ib-hl #phuc-chat #hang-so-ben</sub>

---

**Kp biểu diễn qua phân số mol và áp suất tổng** — *Kp expressed through mole fractions and total pressure*

$$K_{p} = K_{x} \cdot P^{\Delta n}, \qquad p_{i} = x_{i} P$$

Trong đó: `K_{p}` là hằng số cân bằng theo áp suất riêng phần (); `K_{x}` là hằng số cân bằng viết theo phân số mol (); `P` là áp suất tổng của hỗn hợp khí lúc cân bằng (Pa); `\Delta n` là hiệu số mol khí giữa sản phẩm và chất tham gia (); `p_{i}` là áp suất riêng phần của cấu tử i (Pa); `x_{i}` là phân số mol của cấu tử i lúc cân bằng ().

*Điều kiện:* Hỗn hợp khí lí tưởng ở cân bằng đồng thể

*Ghi chú:* Cách trình bày chuẩn của A-Level (CIE 9701, AQA): đề bài cho số mol lúc cân bằng và áp suất tổng, học sinh phải tính phân số mol rồi ra áp suất riêng phần rồi mới thay vào Kp. Hệ quả quan trọng: nếu Delta n khác 0 thì thay đổi áp suất tổng làm đổi thành phần cân bằng dù Kp không đổi. Kho AISTEM có bản đại học Kp - Kx; CT GDPT 2018 Việt Nam dừng ở Kp theo áp suất riêng phần.

<sub>`chemistry.thpt.can-bang-quoc-te.kp-theo-phan-mol` · lớp 10, 11, 12 · #a-level #kp #phan-mol #can-bang-khi</sub>

---

**Bảng ICE (ban đầu - biến thiên - cân bằng)** — *ICE table (Initial - Change - Equilibrium)*

$$[A]_{cb} = [A]_{0} - a x, \qquad [C]_{cb} = [C]_{0} + c x$$

Trong đó: `[A]_{cb}` là nồng độ chất tham gia A lúc cân bằng (mol/L); `[A]_{0}` là nồng độ ban đầu của A (mol/L); `a` là hệ số tỉ lượng của A (); `x` là biến thiên nồng độ ứng với một đơn vị tiến trình phản ứng (mol/L); `[C]_{cb}` là nồng độ sản phẩm C lúc cân bằng (mol/L); `[C]_{0}` là nồng độ ban đầu của C (mol/L); `c` là hệ số tỉ lượng của C ().

*Điều kiện:* Biến thiên của mỗi chất tỉ lệ với hệ số tỉ lượng; nghiệm x phải làm mọi nồng độ cân bằng không âm

*Ghi chú:* Bảng ICE là công cụ chuẩn của AP Chemistry (Unit 7) và IB; thay vào biểu thức K rồi giải phương trình bậc hai. CT GDPT 2018 Việt Nam giải cùng loại bài toán nhưng dùng bảng số mol ba dòng theo phương trình chứ không dùng thuật ngữ và bố cục ICE, và thường không giải phương trình bậc hai.

<sub>`chemistry.thpt.can-bang-quoc-te.bang-ice` · lớp 10, 11, 12 · #ap #ib #bang-ice #can-bang</sub>

---

**Phép xấp xỉ bỏ qua x và quy tắc kiểm tra 5%** — *The small-x approximation and the 5% rule*

$$[A]_{0} - x \approx [A]_{0} \quad \text{khi} \quad \dfrac{x}{[A]_{0}} \times 100\% < 5\%$$

Trong đó: `[A]_{0}` là nồng độ ban đầu của chất tham gia A (mol/L); `x` là biến thiên nồng độ khi đạt cân bằng (mol/L).

*Điều kiện:* Thường hợp lệ khi K rất nhỏ so với nồng độ đầu, cụ thể khi [A]0/K lớn hơn khoảng 400

*Ghi chú:* Quy tắc 5% được AP Chemistry và các giáo trình quốc tế dùng để tránh giải phương trình bậc hai, sau đó BẮT BUỘC kiểm tra lại. Nếu vượt 5% thì phải giải chính xác. CT GDPT 2018 Việt Nam dùng phép xấp xỉ tương tự khi tính pH acid yếu nhưng không nêu tiêu chí định lượng để kiểm tra.

<sub>`chemistry.thpt.can-bang-quoc-te.xap-xi-bo-qua-x` · lớp 10, 11, 12 · #ap #ib #xap-xi #can-bang</sub>

---

### Cấu tạo nguyên tử và liên kết theo chương trình quốc tế

**Tam giác liên kết van Arkel - Ketelaar** — *van Arkel - Ketelaar bonding triangle*

$$\Delta\chi = \left| \chi_{a} - \chi_{b} \right|, \qquad \bar{\chi} = \dfrac{\chi_{a} + \chi_{b}}{2}$$

Trong đó: `\Delta\chi` là hiệu độ âm điện, đóng vai trò trục tung của tam giác liên kết; `\chi_{a}` là độ âm điện của nguyên tố a; `\chi_{b}` là độ âm điện của nguyên tố b; `\bar{\chi}` là độ âm điện trung bình, đóng vai trò trục hoành của tam giác liên kết.

*Điều kiện:* Dùng thang độ âm điện Pauling; điểm biểu diễn nằm ở góc trên là liên kết ion, góc phải dưới là cộng hoá trị, góc trái dưới là kim loại

*Ghi chú:* Tam giác van Arkel - Ketelaar được in trong Chemistry Data Booklet của IB (mục 17) và là công cụ bắt buộc của IB Structure 2.4 để lập luận rằng liên kết là một dải liên tục chứ không phải ba loại rời rạc. CT GDPT 2018 Việt Nam chỉ dùng MỘT tiêu chí là hiệu độ âm điện, nên không phân biệt được hợp chất kim loại với hợp chất cộng hoá trị có cùng hiệu độ âm điện.

<sub>`chemistry.thpt.cau-tao-quoc-te.tam-giac-van-arkel-ketelaar` · lớp 10, 11, 12 · #ib #lien-ket #do-am-dien #van-arkel</sub>

---

**Các ngoại lệ của quy tắc octet** — *Exceptions to the octet rule*

$$n_{e} \begin{cases} < 8 & \text{thieu electron: } \mathrm{BF_{3}},\ \mathrm{BeCl_{2}} \\ = 8 & \text{tuan theo octet} \\ > 8 & \text{octet mo rong: } \mathrm{PCl_{5}},\ \mathrm{SF_{6}} \end{cases}$$

Trong đó: `n_{e}` là số electron hoá trị quanh nguyên tử trung tâm trong công thức Lewis ().

*Điều kiện:* Octet mở rộng chỉ gặp với nguyên tử trung tâm từ chu kì 3 trở đi (nguyên tử đủ lớn để nhận nhiều hơn bốn cặp electron); ngoài ra còn phân tử có số electron lẻ như NO, NO2

*Ghi chú:* IB Structure 2.2 và A-Level yêu cầu vẽ được công thức Lewis của các trường hợp ngoại lệ. Ranh giới của AP: CED cho phép Lewis diagram (Topic 2.5) nhưng có exclusion statement 'Hybridization involving d orbitals will not be assessed... When an atom has more than four pairs of electrons surrounding the central atom, students are only responsible for the shape of the resulting molecule' - với SF6 và PCl5 thì AP chỉ hỏi DẠNG HÌNH HỌC. Lưu ý khoa học: cách giải thích cổ điển 'nhờ phân lớp d trống' vẫn được sách A-Level dùng, nhưng tính toán hiện đại cho thấy orbital d tham gia rất ít; nguyên nhân chính là kích thước nguyên tử trung tâm đủ lớn. CT GDPT 2018 Việt Nam nêu quy tắc octet và có nhắc ngoại lệ nhưng không phân loại thành ba nhóm.

<sub>`chemistry.thpt.cau-tao-quoc-te.ngoai-le-quy-tac-octet` · lớp 10, 11, 12 · #ap #ib #a-level #lewis #octet</sub>

---

**Ngoại lệ cấu hình electron của chromium và copper** — *Anomalous electron configurations of chromium and copper*

$$\mathrm{Cr}: [\mathrm{Ar}]3d^{5}4s^{1}, \qquad \mathrm{Cu}: [\mathrm{Ar}]3d^{10}4s^{1}$$

Trong đó: `[\mathrm{Ar}]` là lõi khí hiếm argon, viết tắt cho cấu hình 1s2 2s2 2p6 3s2 3p6; `3d^{5}4s^{1}` là cấu hình thực tế của chromium: phân lớp d bán bão hoà; `3d^{10}4s^{1}` là cấu hình thực tế của copper: phân lớp d bão hoà.

*Điều kiện:* Chỉ áp dụng cho nguyên tử ở trạng thái cơ bản; khi tạo ion của kim loại chuyển tiếp thì electron 4s bị tách ra TRƯỚC electron 3d

*Ghi chú:* IB Structure 1.3 và A-Level (Cambridge 9701, AQA 3.1.1) liệt kê Cr và Cu là hai ngoại lệ bắt buộc phải nhớ, giải thích bằng độ bền phụ trội của phân lớp d bán bão hoà và bão hoà. KHÔNG được gán cho AP: CED của AP Chemistry có exclusion statement 'Writing the electron configuration of elements that are exceptions to the aufbau principle will not be assessed on the AP Exam'. Khi tạo ion của kim loại chuyển tiếp thì electron 4s bị tách ra TRƯỚC electron 3d. CT GDPT 2018 Việt Nam có dạy quy tắc Klechkovski và nhắc ngoại lệ ở mức đọc thêm, không yêu cầu giải thích.

<sub>`chemistry.thpt.cau-tao-quoc-te.cau-hinh-electron-ngoai-le` · lớp 10, 11, 12 · #ib #a-level #cau-hinh-electron #ngoai-le</sub>

---

**Cấu trúc cộng hưởng và bậc liên kết trung bình** — *Resonance structures and average bond order*

$$\bar{b} = \dfrac{N_{lk}}{N_{vt}}$$

Trong đó: `\bar{b}` là bậc liên kết trung bình của một vị trí liên kết (); `N_{lk}` là tổng số liên kết (đơn cộng đôi cộng ba) giữa nguyên tử trung tâm và các nguyên tử tương đương, tính trên một cấu trúc cộng hưởng (); `N_{vt}` là số vị trí liên kết tương đương ().

*Điều kiện:* Các cấu trúc cộng hưởng phải có cùng vị trí hạt nhân, chỉ khác cách phân bố electron; cấu trúc thật là trung bình có trọng số của chúng

*Ghi chú:* AP Unit 2, IB Structure 2.2 và A-Level. Ví dụ NO3- có bậc liên kết trung bình 4/3 nên ba liên kết N-O dài bằng nhau, ngắn hơn liên kết đơn và dài hơn liên kết đôi. CT GDPT 2018 Việt Nam có nhắc cộng hưởng ở benzene nhưng không định lượng bậc liên kết trung bình cho ion đa nguyên tử.

<sub>`chemistry.thpt.cau-tao-quoc-te.cong-huong-bac-lien-ket-trung-binh` · lớp 10, 11, 12 · #ap #ib #a-level #cong-huong #bac-lien-ket</sub>

---

**Phân loại và thứ tự độ mạnh của lực liên phân tử** — *Classification and relative strength of intermolecular forces*

$$E_{\text{lk hydrogen}} > E_{\text{luong cuc}} > E_{\text{London}}$$

Trong đó: `E_{\text{lk hydrogen}}` là năng lượng liên kết hydrogen, chỉ hình thành khi H liên kết trực tiếp với N, O hoặc F (kJ/mol); `E_{\text{luong cuc}}` là năng lượng tương tác lưỡng cực - lưỡng cực giữa các phân tử phân cực (kJ/mol); `E_{\text{London}}` là năng lượng lực phân tán London, tăng theo số electron và diện tích tiếp xúc của phân tử (kJ/mol).

*Điều kiện:* So sánh cho các phân tử có kích thước tương đương; với phân tử rất lớn, tổng lực London có thể vượt cả liên kết hydrogen

*Ghi chú:* AP Unit 3, IB Structure 2.2 và A-Level dùng lực liên phân tử để giải thích nhiệt độ sôi, độ tan và tính chất dung môi; AP còn tách riêng lực ion - lưỡng cực và lưỡng cực cảm ứng. CT GDPT 2018 Việt Nam có liên kết hydrogen và tương tác van der Waals nhưng không phân loại chi tiết và không nhấn mạnh vai trò của độ phân cực hoá (polarizability).

<sub>`chemistry.thpt.cau-tao-quoc-te.luc-lien-phan-tu` · lớp 10, 11, 12 · #ap #ib #a-level #luc-lien-phan-tu #lien-ket-hydrogen</sub>

---

**Năng lượng ion hoá liên tiếp và bằng chứng về cấu trúc lớp electron** — *Successive ionization energies as evidence for electron shells*

$$\lg I_{k}\ \text{theo}\ k:\ \text{buoc nhay lon} \Rightarrow \text{so electron lop ngoai cung} = k - 1$$

Trong đó: `I_{k}` là năng lượng ion hoá thứ k, ứng với việc tách electron thứ k (kJ/mol); `k` là số thứ tự của lần ion hoá ().

*Điều kiện:* Nguyên tử ở thể khí; luôn có I1 < I2 < I3 < ... vì tách electron khỏi ion tích điện dương ngày càng khó

*Ghi chú:* Dạng bài đặc trưng của A-Level (CIE 9701, AQA) và IB Structure 1.3: cho bảng hoặc đồ thị lg(I) theo số thứ tự electron, học sinh phải chỉ ra bước nhảy lớn để xác định nhóm của nguyên tố. CT GDPT 2018 Việt Nam nêu xu hướng biến đổi I1 nhưng không có dạng bài đọc đồ thị năng lượng ion hoá liên tiếp.

<sub>`chemistry.thpt.cau-tao-quoc-te.nang-luong-ion-hoa-lien-tiep` · lớp 10, 11, 12 · #a-level #ib #nang-luong-ion-hoa #do-thi</sub>

---

**Xác định phân tử phân cực bằng tổng vectơ momen lưỡng cực** — *Molecular polarity from the vector sum of bond dipoles*

$$\vec{\mu} = \sum_{i} \vec{\mu_{i}}; \qquad \left| \vec{\mu} \right| = 0 \Leftrightarrow \text{phan tu khong phan cuc}$$

Trong đó: `\vec{\mu}` là momen lưỡng cực tổng của phân tử (D); `\vec{\mu_{i}}` là momen lưỡng cực của liên kết thứ i, hướng từ nguyên tử dương hơn sang nguyên tử âm hơn (D).

*Điều kiện:* Phải xác định đúng dạng hình học trước; các cặp electron tự do cũng đóng góp vào momen tổng

*Ghi chú:* AP Unit 2, IB Structure 2.2 và A-Level yêu cầu kết luận phân tử phân cực hay không bằng lập luận vectơ: CO2 và CCl4 có liên kết phân cực nhưng phân tử KHÔNG phân cực do đối xứng, trong khi H2O và NH3 phân cực. CT GDPT 2018 Việt Nam dừng ở hiệu độ âm điện của từng liên kết; kho AISTEM chỉ có momen lưỡng cực ở bậc đại học.

<sub>`chemistry.thpt.cau-tao-quoc-te.phan-cuc-phan-tu-tong-vecto` · lớp 10, 11, 12 · #ap #ib #a-level #phan-cuc #momen-luong-cuc</sub>

---

**Giới hạn hội tụ và năng lượng ion hoá tính từ phổ phát xạ** — *Convergence limit and ionization energy from an emission spectrum*

$$I_{1} = N_{A}\,h\,f_{\infty} = \dfrac{N_{A}\,h\,c}{\lambda_{\infty}}$$

Trong đó: `I_{1}` là năng lượng ion hoá thứ nhất, tính cho 1 mol nguyên tử (J/mol); `N_{A}` là hằng số Avogadro, 6,02x10^23 mol^-1 (1/mol); `h` là hằng số Planck, 6,63x10^-34 J.s (J*s); `f_{\infty}` là tần số tại giới hạn hội tụ của dãy phổ (1/s); `c` là tốc độ ánh sáng trong chân không, 3,00x10^8 m/s (m/s); `\lambda_{\infty}` là bước sóng tại giới hạn hội tụ của dãy phổ (m).

*Điều kiện:* Dùng dãy Lyman (n = 1) của hidrogen; giới hạn hội tụ là nơi các vạch phổ chụm lại, ứng với chuyển mức từ n vô cùng về n = 1

*Ghi chú:* IB HL Structure 1.3 yêu cầu tính năng lượng ion hoá từ giới hạn hội tụ của phổ phát xạ hidrogen. Data Booklet IB cấp E = hf, c = f.lambda và N_A nhưng KHÔNG cấp công thức Rydberg. CT GDPT 2018 Việt Nam có công thức năng lượng photon nhưng không có dạng bài này.

<sub>`chemistry.thpt.cau-tao-quoc-te.gioi-han-hoi-tu-nang-luong-ion-hoa` · lớp 10, 11, 12 · #ib-hl #pho-phat-xa #nang-luong-ion-hoa #gioi-han-hoi-tu</sub>

---

**Phổ quang electron (PES) và năng lượng liên kết electron** — *Photoelectron spectroscopy (PES) and electron binding energy*

$$E_{lk} = h\nu - E_{k}$$

Trong đó: `E_{lk}` là năng lượng liên kết của electron với hạt nhân, đọc trên trục hoành của phổ PES (J); `h` là hằng số Planck, 6,63x10^-34 J.s (J*s); `\nu` là tần số của photon tới dùng để bắn phá (1/s); `E_{k}` là động năng của electron bị bật ra, đo được bằng máy (J).

*Điều kiện:* Photon phải đủ năng lượng để tách electron; trên phổ, vị trí đỉnh cho năng lượng liên kết (thường tính bằng MJ/mol) còn CHIỀU CAO đỉnh tỉ lệ với số electron trong phân lớp

*Ghi chú:* Nội dung RIÊNG CÓ của AP Chemistry (Unit 1): không có trong IB, A-Level hay CT GDPT 2018 Việt Nam. Từ phổ PES suy ra cấu hình electron: mỗi đỉnh là một phân lớp, đỉnh ở năng lượng liên kết lớn ứng với electron gần hạt nhân.

<sub>`chemistry.thpt.cau-tao-quoc-te.pho-quang-electron-pes` · lớp 10, 11, 12 · #ap #pes #cau-hinh-electron #pho</sub>

---

**Quy tắc định lượng về ảnh hưởng của cặp electron tự do đến góc liên kết** — *Quantitative effect of lone pairs on bond angles*

$$\theta \approx \theta_{0} - 2.5^{\circ} \times n_{lp}$$

Trong đó: `\theta` là góc liên kết thực tế của phân tử (); `\theta_{0}` là góc liên kết lí tưởng khi không có cặp electron tự do (); `n_{lp}` là số cặp electron tự do (lone pair) trên nguyên tử trung tâm ().

*Điều kiện:* Quy tắc kinh nghiệm cho khung tứ diện (theta0 = 109,5 độ); lực đẩy giảm dần theo thứ tự cặp tự do - cặp tự do > cặp tự do - cặp liên kết > cặp liên kết - cặp liên kết

*Ghi chú:* Con số 2,5 độ cho mỗi cặp electron tự do là QUY TẮC KINH NGHIỆM được sách giáo khoa A-Level (AQA, Edexcel, Cambridge) dùng để nhớ nhanh, KHÔNG phải một công thức in trong bản đặc tả: Cambridge 9701 chỉ liệt kê giá trị thực nghiệm của từng phân tử (H2O 104,5 độ) và yêu cầu giải thích bằng thứ tự lực đẩy cặp tự do - cặp tự do > cặp tự do - cặp liên kết > cặp liên kết - cặp liên kết. Quy tắc cho kết quả đúng với khung tứ diện (NH3 107 độ, H2O 104,5 độ) nhưng không áp dụng cho khung lưỡng chóp tam giác hay bát diện. Kho Việt Nam đã có bản VSEPR nêu ảnh hưởng của cặp tự do nhưng chỉ ở mức định tính.

<sub>`chemistry.thpt.cau-tao-quoc-te.goc-lien-ket-va-cap-electron-tu-do` · lớp 10, 11, 12 · #a-level #vsepr #goc-lien-ket #cap-electron-tu-do</sub>

---

**Kí hiệu AXmEn và cách gọi tên dạng hình học phân tử** — *AXmEn notation and molecular shape names*

$$\mathrm{A}\mathrm{X}_{m}\mathrm{E}_{n}, \qquad SN = m + n$$

Trong đó: `\mathrm{A}` là nguyên tử trung tâm; `\mathrm{X}` là nguyên tử (hoặc nhóm) liên kết với nguyên tử trung tâm; `\mathrm{E}` là cặp electron tự do trên nguyên tử trung tâm; `m` là số nguyên tử liên kết trực tiếp với nguyên tử trung tâm (); `n` là số cặp electron tự do trên nguyên tử trung tâm (); `SN` là số miền electron (steric number), quyết định dạng hình học cặp electron ().

*Điều kiện:* Liên kết đôi và liên kết ba được tính là MỘT miền electron; dạng hình học phân tử chỉ xét vị trí các nguyên tử X

*Ghi chú:* Kí hiệu AXE là quy ước chuẩn của AP Unit 2, IB Structure 2.2 và A-Level: AX2 thẳng, AX3 tam giác phẳng, AX2E gấp khúc, AX4 tứ diện, AX3E chóp tam giác, AX2E2 gấp khúc, AX5 lưỡng chóp tam giác, AX6 bát diện. CT GDPT 2018 Việt Nam mô tả dạng hình học qua số cặp electron nhưng KHÔNG dùng kí hiệu AXmEn nên học sinh dễ bỡ ngỡ với đề quốc tế.

<sub>`chemistry.thpt.cau-tao-quoc-te.ky-hieu-axe-vsepr` · lớp 10, 11, 12 · #ap #ib #a-level #vsepr #axe</sub>

---

**Định luật Coulomb dạng tỉ lệ dùng trong giải thích xu hướng hoá học** — *Coulomb's law as used for chemical trends*

$$F_{coulomb} \propto \dfrac{q_{1}q_{2}}{r^{2}}, \qquad E_{p} \propto \dfrac{q_{1}q_{2}}{r}$$

Trong đó: `F_{coulomb}` là lực tương tác tĩnh điện giữa hai điện tích (N); `q_{1}` là điện tích thứ nhất (ví dụ điện tích hạt nhân hiệu dụng) (C); `q_{2}` là điện tích thứ hai (ví dụ điện tích electron hoặc ion đối) (C); `r` là khoảng cách giữa hai điện tích (m); `E_{p}` là thế năng tương tác tĩnh điện của cặp điện tích (J).

*Điều kiện:* Hai điện tích điểm; trong môn Hoá học chỉ dùng để SO SÁNH định tính chứ không thay số tính giá trị

*Ghi chú:* SỬA KÍ HIỆU: bảng công thức và CED của AP Chemistry (mục 1.5.A.2) in đúng dạng TỈ LỆ 'F_coulombic tỉ lệ với q1.q2/r^2', KHÔNG kèm bất kì hằng số nào, vì AP chỉ yêu cầu so sánh xu hướng chứ không tính số. Bản ghi trước đây viết F = k.q1.q2/r^2 với k = 8,99x10^9 là lấy từ Vật lí, không đúng với cách trình bày của AP Chemistry. Trong Vật lí, hằng số đầy đủ là 1/(4.pi.epsilon0) = 8,99x10^9 N.m^2/C^2. AP dùng tỉ lệ này xuyên suốt Unit 1 và Unit 2 để giải thích năng lượng ion hoá, bán kính nguyên tử và năng lượng mạng lưới. CT GDPT 2018 KHÔNG dùng định luật Coulomb trong môn Hoá học.

<sub>`chemistry.thpt.cau-tao-quoc-te.luc-coulomb-tuong-tac-tinh-dien` · lớp 10, 11, 12 · #ap #coulomb #tinh-dien #quy-uoc-ky-hieu</sub>

---

**Điện tích hạt nhân hiệu dụng và hiệu ứng chắn** — *Effective nuclear charge and shielding*

$$Z_{eff} \approx Z - S$$

Trong đó: `Z_{eff}` là điện tích hạt nhân hiệu dụng mà electron ngoài cùng thực sự chịu (); `Z` là số proton trong hạt nhân (); `S` là hằng số chắn, ở mức THPT quốc tế lấy xấp xỉ bằng số electron thuộc các lớp bên trong ().

*Điều kiện:* Phép xấp xỉ đơn giản dùng để so sánh xu hướng, không dùng để tính giá trị chính xác

*Ghi chú:* AP Unit 1 và IB Structure 3.1 dùng Z_eff để giải thích mọi xu hướng tuần hoàn: trong một chu kì Z_eff tăng nên bán kính giảm và năng lượng ion hoá tăng; trong một nhóm Z_eff gần như không đổi nhưng số lớp tăng nên bán kính tăng. CT GDPT 2018 Việt Nam giải thích xu hướng bằng lực hút hạt nhân định tính, không dùng đại lượng Z_eff; kho AISTEM chỉ có quy tắc Slater ở bậc đại học.

<sub>`chemistry.thpt.cau-tao-quoc-te.dien-tich-hat-nhan-hieu-dung` · lớp 10, 11, 12 · #ap #ib #z-hieu-dung #xu-huong-tuan-hoan</sub>

---

### Dung dịch

**Khối lượng dung dịch sau phản ứng** — *Solution mass after a reaction*

$$m_{dd\,sau} = m_{cac\,chat\,cho\,vao} - m_{\downarrow} - m_{\uparrow}$$

Trong đó: `m_{dd\,sau}` là khối lượng dung dịch sau phản ứng (g); `m_{cac\,chat\,cho\,vao}` là tổng khối lượng các chất đưa vào (dung dịch và chất tham gia) (g); `m_{\downarrow}` là khối lượng kết tủa tách ra (g); `m_{\uparrow}` là khối lượng khí thoát ra (g).

*Điều kiện:* Phản ứng xảy ra hoàn toàn trong dung dịch; kết tủa được tách khỏi dung dịch

*Ghi chú:* Hệ quả trực tiếp của định luật bảo toàn khối lượng; là bước bắt buộc để tính C% sau phản ứng.

<sub>`chemistry.thpt.dung-dich.khoi-luong-dung-dich-sau-phan-ung` · lớp 10, 11, 12 · #dung-dich #bao-toan-khoi-luong #sau-phan-ung</sub>

---

**Quan hệ giữa nồng độ mol và nồng độ phần trăm** — *Relation between molarity and mass percent*

$$C_{M} = \dfrac{10 \cdot D \cdot C\%}{M}$$

Trong đó: `C_{M}` là nồng độ mol (mol/L); `D` là khối lượng riêng của dung dịch (g/mL); `C\%` là nồng độ phần trăm (%); `M` là khối lượng mol chất tan (g/mol).

*Điều kiện:* D tính bằng g/mL, C% tính theo số phần trăm (ví dụ 98 chứ không phải 0.98)

*Ghi chú:* Hệ số 10 xuất hiện do đổi 1 L = 1000 mL và chia cho 100 của phần trăm.

<sub>`chemistry.thpt.dung-dich.quan-he-cm-va-cphan-tram` · lớp 10, 11, 12 · #dung-dich #nong-do-mol #nong-do-phan-tram</sub>

---

**Công thức pha loãng dung dịch theo nồng độ mol** — *Dilution formula (molarity)*

$$C_{1}V_{1} = C_{2}V_{2}$$

Trong đó: `C_{1}` là nồng độ mol dung dịch ban đầu (mol/L); `V_{1}` là thể tích dung dịch ban đầu (L); `C_{2}` là nồng độ mol dung dịch sau pha loãng (mol/L); `V_{2}` là thể tích dung dịch sau pha loãng (L).

*Điều kiện:* Chỉ thêm dung môi, số mol chất tan không đổi

*Ghi chú:* Bản chất là bảo toàn số mol chất tan: n = C1V1 = C2V2. Khi pha loãng, luôn rót axit đặc vào nước, không làm ngược lại.

<sub>`chemistry.thpt.dung-dich.pha-loang-theo-nong-do-mol` · lớp 10, 11, 12 · #pha-loang #dung-dich #nong-do-mol</sub>

---

**Quy tắc đường chéo theo nồng độ mol** — *Cross rule for molarity*

$$\dfrac{V_{1}}{V_{2}} = \dfrac{\left| C_{2} - C \right|}{\left| C - C_{1} \right|}$$

Trong đó: `V_{1}` là thể tích dung dịch 1 (L); `V_{2}` là thể tích dung dịch 2 (L); `C_{1}` là nồng độ mol dung dịch 1 (mol/L); `C_{2}` là nồng độ mol dung dịch 2 (mol/L); `C` là nồng độ mol dung dịch sau trộn (mol/L).

*Điều kiện:* C nằm giữa C1 và C2; thể tích được coi là cộng tính

*Ghi chú:* Quy tắc đường chéo cũng áp dụng cho khối lượng mol trung bình của hỗn hợp khí.

<sub>`chemistry.thpt.dung-dich.quy-tac-duong-cheo-nong-do-mol` · lớp 10, 11, 12 · #duong-cheo #nong-do-mol #tron-dung-dich</sub>

---

**Quy tắc đường chéo theo nồng độ phần trăm** — *Cross rule for mass percent*

$$\dfrac{m_{1}}{m_{2}} = \dfrac{\left| C_{2}\% - C\% \right|}{\left| C\% - C_{1}\% \right|}$$

Trong đó: `m_{1}` là khối lượng dung dịch 1 (g); `m_{2}` là khối lượng dung dịch 2 (g); `C_{1}\%` là nồng độ dung dịch 1 (%); `C_{2}\%` là nồng độ dung dịch 2 (%); `C\%` là nồng độ dung dịch sau khi trộn (%).

*Điều kiện:* C% nằm giữa C1% và C2%; hai dung dịch cùng chất tan, không phản ứng

*Ghi chú:* Nước coi như dung dịch có C% = 0; chất tan nguyên chất coi như C% = 100.

<sub>`chemistry.thpt.dung-dich.quy-tac-duong-cheo-nong-do-phan-tram` · lớp 10, 11, 12 · #duong-cheo #tron-dung-dich #nong-do-phan-tram</sub>

---

**Nồng độ mol khi trộn hai dung dịch cùng chất tan** — *Molarity after mixing two solutions of the same solute*

$$C_{M} = \dfrac{C_{1}V_{1} + C_{2}V_{2}}{V_{1} + V_{2}}$$

Trong đó: `C_{M}` là nồng độ mol sau khi trộn (mol/L); `C_{1}` là nồng độ dung dịch 1 (mol/L); `V_{1}` là thể tích dung dịch 1 (L); `C_{2}` là nồng độ dung dịch 2 (mol/L); `V_{2}` là thể tích dung dịch 2 (L).

*Điều kiện:* Coi thể tích dung dịch sau trộn bằng tổng thể tích, không có phản ứng hóa học

*Ghi chú:* Nếu đề cho khối lượng riêng, phải tính thể tích thực tế thay vì cộng đơn thuần.

<sub>`chemistry.thpt.dung-dich.tron-hai-dung-dich-cung-chat` · lớp 10, 11, 12 · #tron-dung-dich #nong-do-mol #thpt</sub>

---

### Entropy và năng lượng Gibbs bậc THPT

**Biến thiên entropy chuẩn của phản ứng** — *Standard entropy change of reaction*

$$\Delta S^{\ominus} = \sum n\, S^{\ominus}_{sp} - \sum m\, S^{\ominus}_{tg}$$

Trong đó: `\Delta S^{\ominus}` là biến thiên entropy chuẩn của phản ứng (J/(mol*K)); `n` là hệ số tỉ lượng của từng sản phẩm (); `S^{\ominus}_{sp}` là entropy mol chuẩn của từng sản phẩm (J/(mol*K)); `m` là hệ số tỉ lượng của từng chất tham gia (); `S^{\ominus}_{tg}` là entropy mol chuẩn của từng chất tham gia (J/(mol*K)).

*Điều kiện:* Dùng entropy mol chuẩn tra bảng ở 298 K; khác với enthalpy tạo thành, đơn chất bền có entropy chuẩn KHÁC 0

*Ghi chú:* Có trên bảng công thức AP Chemistry (Unit 9), trong IB Reactivity 1.4 và A-Level. Dấu hiệu nhanh: Delta S > 0 khi số mol khí tăng. Đơn vị J/(mol.K) trong khi Delta H là kJ/mol nên phải đổi đơn vị trước khi thay vào Delta G = Delta H - T Delta S. CT GDPT 2018 Việt Nam có Delta G ở mức tham khảo nhưng không cấp bảng entropy chuẩn.

<sub>`chemistry.thpt.nhiet-dong-thpt.entropy-chuan-phan-ung` · lớp 10, 11, 12 · #ap #ib #a-level #entropy</sub>

---

**Biến thiên entropy của môi trường** — *Entropy change of the surroundings*

$$\Delta S_{surr} = -\dfrac{\Delta H_{sys}}{T}$$

Trong đó: `\Delta S_{surr}` là biến thiên entropy của môi trường xung quanh (J/(mol*K)); `\Delta H_{sys}` là biến thiên enthalpy của hệ (phản ứng) (J/mol); `T` là nhiệt độ tuyệt đối tại đó xảy ra quá trình (K).

*Điều kiện:* Áp suất không đổi; Delta H phải đổi sang J/mol (không dùng kJ/mol) để cùng đơn vị với entropy

*Ghi chú:* Đặc trưng của A-Level (AQA 3.1.8, OCR, Edexcel): tiếp cận tính khả thi bằng ENTROPY TỔNG thay vì bằng năng lượng Gibbs. Phản ứng toả nhiệt (Delta H < 0) làm entropy môi trường TĂNG. CT GDPT 2018 Việt Nam chỉ dùng tiêu chuẩn Delta G, không tách entropy hệ và entropy môi trường.

<sub>`chemistry.thpt.nhiet-dong-thpt.entropy-moi-truong` · lớp 10, 11, 12 · #a-level #entropy #moi-truong #kha-thi</sub>

---

**Đồ thị năng lượng Gibbs theo nhiệt độ** — *Plot of Gibbs energy against temperature*

$$\Delta G^{\ominus} = (-\Delta S^{\ominus})\,T + \Delta H^{\ominus}$$

Trong đó: `\Delta G^{\ominus}` là biến thiên năng lượng Gibbs chuẩn, đóng vai trò tung độ (kJ/mol); `\Delta S^{\ominus}` là biến thiên entropy chuẩn; hệ số góc của đường thẳng bằng trừ Delta S chuẩn (kJ/(mol*K)); `T` là nhiệt độ tuyệt đối, đóng vai trò hoành độ (K); `\Delta H^{\ominus}` là biến thiên enthalpy chuẩn, bằng tung độ gốc (kJ/mol).

*Điều kiện:* Giả thiết Delta H chuẩn và Delta S chuẩn không đổi theo nhiệt độ trong khoảng khảo sát

*Ghi chú:* Dạng bài tuyến tính hoá đặc trưng của A-Level và AP: từ đồ thị Delta G theo T đọc ra Delta H (tung độ gốc) và Delta S (trừ hệ số góc), giao điểm với trục hoành cho nhiệt độ cân bằng. CT GDPT 2018 Việt Nam không có dạng bài này.

<sub>`chemistry.thpt.nhiet-dong-thpt.do-thi-gibbs-theo-nhiet-do` · lớp 10, 11, 12 · #a-level #ap #gibbs #do-thi-tuyen-tinh</sub>

---

**Năng lượng Gibbs chuẩn của phản ứng tính từ năng lượng Gibbs tạo thành** — *Standard Gibbs energy of reaction from Gibbs energies of formation*

$$\Delta G^{\ominus} = \sum n\, \Delta_{f}G^{\ominus}_{sp} - \sum m\, \Delta_{f}G^{\ominus}_{tg}$$

Trong đó: `\Delta G^{\ominus}` là biến thiên năng lượng Gibbs chuẩn của phản ứng (kJ/mol); `n` là hệ số tỉ lượng của từng sản phẩm (); `\Delta_{f}G^{\ominus}_{sp}` là năng lượng Gibbs tạo thành chuẩn của từng sản phẩm (kJ/mol); `m` là hệ số tỉ lượng của từng chất tham gia (); `\Delta_{f}G^{\ominus}_{tg}` là năng lượng Gibbs tạo thành chuẩn của từng chất tham gia (kJ/mol).

*Điều kiện:* Năng lượng Gibbs tạo thành của đơn chất bền ở trạng thái chuẩn bằng 0

*Ghi chú:* Nằm trên bảng công thức AP Chemistry (Unit 9). CT GDPT 2018 Việt Nam chỉ cấp bảng enthalpy tạo thành chuẩn chứ không cấp bảng năng lượng Gibbs tạo thành nên không có dạng bài này.

<sub>`chemistry.thpt.nhiet-dong-thpt.gibbs-chuan-tu-nang-luong-tao-thanh` · lớp 10, 11, 12 · #ap #gibbs #nang-luong-tao-thanh</sub>

---

**Năng lượng Gibbs ở điều kiện bất kì** — *Gibbs energy under non-standard conditions*

$$\Delta G = \Delta G^{\ominus} + RT \ln Q$$

Trong đó: `\Delta G` là biến thiên năng lượng Gibbs ở điều kiện đang xét (J/mol); `\Delta G^{\ominus}` là biến thiên năng lượng Gibbs ở điều kiện chuẩn (J/mol); `R` là hằng số khí, 8,314 J/(K.mol) (J/(mol*K)); `T` là nhiệt độ tuyệt đối (K); `Q` là thương số phản ứng tính theo nồng độ hoặc áp suất tức thời ().

*Điều kiện:* Khi Q = K thì Delta G = 0, hệ đạt cân bằng

*Ghi chú:* Chemistry Data Booklet của IB (mục 1) in nguyên văn 'Delta G = Delta G(chuẩn) + RT ln Q' - đây là nội dung IB HL Reactivity 1.4. KHÔNG có trên bảng công thức AP: bảng của AP chỉ in Delta G(chuẩn) = Delta H(chuẩn) - T.Delta S(chuẩn) = -RT lnK = -nFE(chuẩn), cùng phương trình Nernst. Đây là cầu nối giữa nhiệt động lực học và cân bằng: dấu của Delta G phụ thuộc thành phần tức thời của hệ chứ không chỉ phụ thuộc Delta G chuẩn. CT GDPT 2018 Việt Nam không có hệ thức này ở THPT; kho AISTEM chỉ có bản đại học (đẳng nhiệt Van't Hoff).

<sub>`chemistry.thpt.nhiet-dong-thpt.gibbs-dieu-kien-bat-ki` · lớp 10, 11, 12 · #ib-hl #ib #gibbs #thuong-so-phan-ung</sub>

---

**Quan hệ giữa năng lượng Gibbs chuẩn và hằng số cân bằng** — *Relation between standard Gibbs energy and the equilibrium constant*

$$\Delta G^{\ominus} = -RT \ln K \quad \Leftrightarrow \quad K = e^{-\Delta G^{\ominus}/(RT)}$$

Trong đó: `\Delta G^{\ominus}` là biến thiên năng lượng Gibbs chuẩn của phản ứng (J/mol); `R` là hằng số khí, 8,314 J/(K.mol) (J/(mol*K)); `T` là nhiệt độ tuyệt đối (K); `K` là hằng số cân bằng nhiệt động, không thứ nguyên ().

*Điều kiện:* K là hằng số cân bằng nhiệt động tính theo hoạt độ so với trạng thái chuẩn nên không có đơn vị

*Ghi chú:* Có trên bảng công thức AP Chemistry (Unit 9) và trong IB HL Reactivity 1.4. Hệ quả: Delta G chuẩn < 0 thì K > 1. CT GDPT 2018 Việt Nam có mối liên hệ E chuẩn - K trong điện hoá nhưng KHÔNG có hệ thức Delta G chuẩn - K ở THPT.

<sub>`chemistry.thpt.nhiet-dong-thpt.gibbs-va-hang-so-can-bang` · lớp 10, 11, 12 · #ap #ib-hl #gibbs #hang-so-can-bang</sub>

---

**Bảng dấu enthalpy - entropy và tính tự diễn biến theo nhiệt độ** — *Sign table of enthalpy and entropy versus spontaneity*

$$\Delta G = \Delta H - T\Delta S \Rightarrow \begin{cases} \Delta H < 0,\ \Delta S > 0 & \text{tu dien bien o moi } T \\ \Delta H > 0,\ \Delta S < 0 & \text{khong tu dien bien o moi } T \\ \Delta H < 0,\ \Delta S < 0 & \text{tu dien bien o } T \text{ thap} \\ \Delta H > 0,\ \Delta S > 0 & \text{tu dien bien o } T \text{ cao} \end{cases}$$

Trong đó: `\Delta G` là biến thiên năng lượng Gibbs (kJ/mol); `\Delta H` là biến thiên enthalpy của phản ứng (kJ/mol); `T` là nhiệt độ tuyệt đối (K); `\Delta S` là biến thiên entropy của phản ứng (kJ/(mol*K)).

*Điều kiện:* Áp suất không đổi; kết luận chỉ nói về khả năng nhiệt động, không nói gì về tốc độ phản ứng

*Ghi chú:* Bảng bốn trường hợp là kiến thức bắt buộc của AP Unit 9 và IB Reactivity 1.4. AP nhấn mạnh thêm khái niệm phản ứng bị kiểm soát động học: Delta G < 0 nhưng phản ứng vẫn không xảy ra vì Ea quá lớn. CT GDPT 2018 Việt Nam chỉ nêu ba trường hợp dấu của Delta G, không phân tích theo nhiệt độ.

<sub>`chemistry.thpt.nhiet-dong-thpt.bang-dau-tu-dien-bien` · lớp 10, 11, 12 · #ap #ib #gibbs #tu-dien-bien</sub>

---

**Entropy tổng và điều kiện khả thi của phản ứng** — *Total entropy change and feasibility*

$$\Delta S_{total} = \Delta S_{sys} + \Delta S_{surr} = \Delta S_{sys} - \dfrac{\Delta H_{sys}}{T} > 0$$

Trong đó: `\Delta S_{total}` là biến thiên entropy tổng của hệ và môi trường (J/(mol*K)); `\Delta S_{sys}` là biến thiên entropy của hệ phản ứng (J/(mol*K)); `\Delta S_{surr}` là biến thiên entropy của môi trường (J/(mol*K)); `\Delta H_{sys}` là biến thiên enthalpy của hệ (J/mol); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Phản ứng khả thi về mặt nhiệt động khi Delta S tổng dương; Delta S tổng = 0 ứng với trạng thái cân bằng

*Ghi chú:* Đây là phát biểu nguyên lí II theo cách của A-Level. CT GDPT 2018 Việt Nam phát biểu tiêu chuẩn tự diễn biến bằng Delta G < 0; hai cách hoàn toàn tương đương vì Delta G = -T.Delta S(tổng).

<sub>`chemistry.thpt.nhiet-dong-thpt.entropy-tong` · lớp 10, 11, 12 · #a-level #entropy #nguyen-li-ii #tu-dien-bien</sub>

---

**Quan hệ giữa năng lượng Gibbs và entropy tổng** — *Relation between Gibbs energy and total entropy*

$$\Delta G = -T\,\Delta S_{total}$$

Trong đó: `\Delta G` là biến thiên năng lượng Gibbs của hệ (J/mol); `T` là nhiệt độ tuyệt đối (K); `\Delta S_{total}` là biến thiên entropy tổng của hệ và môi trường (J/(mol*K)).

*Điều kiện:* Nhiệt độ và áp suất không đổi

*Ghi chú:* Cầu nối giữa hai cách trình bày: A-Level dùng Delta S(tổng) > 0 còn AP, IB và CT GDPT 2018 Việt Nam dùng Delta G < 0. Hệ thức cho thấy chúng chỉ khác nhau ở thừa số -T, mà T luôn dương nên hai bất đẳng thức ngược chiều nhau.

<sub>`chemistry.thpt.nhiet-dong-thpt.gibbs-va-entropy-tong` · lớp 10, 11, 12 · #a-level #ap #gibbs #entropy</sub>

---

**Nhiệt độ tối thiểu để phản ứng trở nên khả thi** — *Minimum temperature for feasibility*

$$T > \dfrac{\Delta H^{\ominus}}{\Delta S^{\ominus}}$$

Trong đó: `T` là nhiệt độ tuyệt đối cần đạt để phản ứng tự diễn biến (K); `\Delta H^{\ominus}` là biến thiên enthalpy chuẩn của phản ứng (J/mol); `\Delta S^{\ominus}` là biến thiên entropy chuẩn của phản ứng (J/(mol*K)).

*Điều kiện:* Chỉ áp dụng khi Delta H > 0 và Delta S > 0; nếu Delta H < 0 và Delta S < 0 thì điều kiện đảo lại thành T < Delta H/Delta S

*Ghi chú:* Câu hỏi kinh điển của A-Level và IB: tính nhiệt độ nung tối thiểu để phân huỷ CaCO3. Suy ra bằng cách đặt Delta G = 0 trong Delta G = Delta H - T Delta S. Nhớ đổi Delta H sang J/mol. CT GDPT 2018 Việt Nam không yêu cầu dạng bài này.

<sub>`chemistry.thpt.nhiet-dong-thpt.nhiet-do-kha-thi` · lớp 10, 11, 12 · #a-level #ib #gibbs #nhiet-do-kha-thi</sub>

---

### Hoá học hữu cơ quốc tế: lập thể và cơ chế phản ứng

**Cơ chế cộng electrophin vào alkene và quy tắc Markovnikov** — *Electrophilic addition to alkenes and Markovnikov's rule*

$$\mathrm{C\!=\!C} + \mathrm{H\!-\!X} \rightarrow \mathrm{C^{+}\!-\!C\!-\!H} \xrightarrow{\ \mathrm{X^{-}}\ } \mathrm{X\!-\!C\!-\!C\!-\!H}$$

Trong đó: `\mathrm{C\!=\!C}` là liên kết đôi của alkene, đóng vai trò trung tâm giàu electron; `\mathrm{H\!-\!X}` là tác nhân electrophin, ví dụ HBr; `\mathrm{C^{+}\!-\!C\!-\!H}` là carbocation trung gian tạo thành sau khi cộng H+; `\mathrm{X^{-}}` là anion tấn công carbocation ở giai đoạn hai; `\mathrm{X\!-\!C\!-\!C\!-\!H}` là sản phẩm cộng theo quy tắc Markovnikov.

*Điều kiện:* Hai giai đoạn: liên kết pi cho cặp electron tạo carbocation bền nhất, sau đó anion tấn công carbocation

*Ghi chú:* A-Level (AQA 3.3.4 Alkenes, CIE 9701) và IB HL Reactivity 3.4 yêu cầu vẽ cơ chế bằng mũi tên cong. Quy tắc Markovnikov được GIẢI THÍCH bằng độ bền carbocation chứ không học thuộc: H cộng vào carbon có nhiều H hơn để tạo carbocation bậc cao hơn. CT GDPT 2018 Việt Nam nêu quy tắc Markovnikov nhưng không dạy cơ chế và mũi tên cong.

<sub>`chemistry.thpt.huu-co-quoc-te.cong-electrophin-markovnikov` · lớp 10, 11, 12 · #a-level #ib-hl #co-che #markovnikov #cong-electrophin</sub>

---

**Cơ chế cộng nucleophin vào nhóm carbonyl** — *Nucleophilic addition to a carbonyl group*

$$\mathrm{C^{\delta+}\!\!=\!\!O^{\delta-}} + \mathrm{Nu^{-}} \rightarrow \mathrm{Nu\!-\!C\!-\!O^{-}} \xrightarrow{\ \mathrm{H^{+}}\ } \mathrm{Nu\!-\!C\!-\!OH}$$

Trong đó: `\mathrm{C^{\delta+}\!\!=\!\!O^{\delta-}}` là nhóm carbonyl phân cực, carbon mang một phần điện tích dương; `\mathrm{Nu^{-}}` là tác nhân nucleophin, ví dụ ion cyanide hoặc hydride từ NaBH4; `\mathrm{Nu\!-\!C\!-\!O^{-}}` là alkoxide trung gian tạo thành sau khi nucleophin tấn công; `\mathrm{H^{+}}` là proton từ nước hoặc acid ở bước xử lí; `\mathrm{Nu\!-\!C\!-\!OH}` là sản phẩm cộng cuối cùng.

*Điều kiện:* Nhóm carbonyl phân cực nên carbon là tâm ái nhân; aldehyde phản ứng dễ hơn ketone do ít cản trở không gian và ít hiệu ứng đẩy electron

*Ghi chú:* Cơ chế bắt buộc của A-Level (AQA 3.3.8, CIE 9701) và IB HL: cộng HCN vào aldehyde tạo hydroxynitrile, khử bằng NaBH4 tạo alcohol. Chú ý: cộng HCN vào aldehyde bất đối tạo hỗn hợp racemic vì nucleophin tấn công hai phía mặt phẳng carbonyl như nhau. CT GDPT 2018 Việt Nam nêu sản phẩm phản ứng nhưng không dạy cơ chế cộng nucleophin.

<sub>`chemistry.thpt.huu-co-quoc-te.cong-nucleophin-vao-carbonyl` · lớp 10, 11, 12 · #a-level #ib-hl #co-che #cong-nucleophin #carbonyl</sub>

---

**Cơ chế thế gốc tự do khi halogen hoá alkane** — *Free-radical substitution mechanism in the halogenation of alkanes*

$$\mathrm{Cl_{2}} \xrightarrow{\ h\nu\ } 2\mathrm{Cl^{\bullet}};\quad \mathrm{Cl^{\bullet}} + \mathrm{CH_{4}} \rightarrow \mathrm{HCl} + \mathrm{CH_{3}^{\bullet}};\quad \mathrm{CH_{3}^{\bullet}} + \mathrm{Cl_{2}} \rightarrow \mathrm{CH_{3}Cl} + \mathrm{Cl^{\bullet}};\quad 2\mathrm{Cl^{\bullet}} \rightarrow \mathrm{Cl_{2}}$$

Trong đó: `\mathrm{Cl_{2}}` là phân tử chlorine bị phân cắt đồng li; `h\nu` là năng lượng photon tử ngoại gây khơi mào; `\mathrm{Cl^{\bullet}}` là gốc tự do chlorine; `\mathrm{CH_{4}}` là alkane tham gia phản ứng; `\mathrm{HCl}` là sản phẩm phụ hydrogen chloride; `\mathrm{CH_{3}^{\bullet}}` là gốc tự do methyl; `\mathrm{CH_{3}Cl}` là sản phẩm thế chloromethane.

*Điều kiện:* Cần ánh sáng tử ngoại hoặc nhiệt độ cao để khơi mào; ba giai đoạn khơi mào - phát triển mạch - tắt mạch

*Ghi chú:* Cơ chế bắt buộc phải viết đầy đủ ba giai đoạn trong A-Level (AQA 3.3.2, CIE 9701) và IB Reactivity 3.4; đây cũng là cơ sở giải thích sự phá huỷ tầng ozone bởi CFC. CT GDPT 2018 Việt Nam nêu phản ứng thế halogen của alkane nhưng không yêu cầu viết cơ chế gốc tự do.

<sub>`chemistry.thpt.huu-co-quoc-te.the-goc-tu-do-halogen-hoa` · lớp 10, 11, 12 · #a-level #ib #co-che #goc-tu-do #halogen-hoa</sub>

---

**Điều kiện ưu tiên giữa thế nucleophin và tách** — *Conditions favouring substitution versus elimination*

$$\begin{cases} \mathrm{Nu^{-}}\ \text{manh, base yeu, } 1^{\circ},\ \text{dung moi aprotic} & S_{N}2 \\ \text{base manh cong kenh, nhiet do cao} & E2 \\ \text{co chat } 3^{\circ},\ \text{dung moi protic, base yeu} & S_{N}1\ \text{va}\ E1 \end{cases}$$

Trong đó: `\mathrm{Nu^{-}}` là tác nhân nucleophin; `S_{N}2` là thế nucleophin lưỡng phân tử; `E2` là tách lưỡng phân tử; `S_{N}1` là thế nucleophin đơn phân tử; `E1` là tách đơn phân tử.

*Điều kiện:* Cùng một dẫn xuất halogen có thể cho cả hai loại sản phẩm; tỉ lệ do dung môi, base và nhiệt độ quyết định

*Ghi chú:* Ví dụ điển hình của A-Level: bromoalkane với KOH trong NƯỚC cho alcohol (thế), nhưng với KOH trong ETHANOL và đun nóng lại cho alkene (tách). CT GDPT 2018 Việt Nam có nêu hai điều kiện phản ứng khác nhau nhưng không giải thích bằng cạnh tranh cơ chế.

<sub>`chemistry.thpt.huu-co-quoc-te.canh-tranh-the-va-tach` · lớp 10, 11, 12 · #a-level #ib-hl #co-che #the-va-tach</sub>

---

**Cơ chế SN1: thế nucleophin đơn phân tử** — *SN1 mechanism: unimolecular nucleophilic substitution*

$$v = k\,[\mathrm{RX}]$$

Trong đó: `v` là tốc độ phản ứng thế (mol/(L*s)); `k` là hằng số tốc độ bậc một (1/s); `[\mathrm{RX}]` là nồng độ dẫn xuất halogen (mol/L).

*Điều kiện:* Ưu tiên với dẫn xuất bậc III, dung môi phân cực có proton; hai giai đoạn với bước chậm là sự ion hoá tạo carbocation

*Ghi chú:* A-Level và IB HL. Hệ quả lập thể: carbocation phẳng bị tấn công từ cả hai phía nên sản phẩm là hỗn hợp racemic - đây là bằng chứng thực nghiệm phân biệt SN1 với SN2. Tốc độ KHÔNG phụ thuộc nồng độ nucleophin. CT GDPT 2018 Việt Nam không dạy cơ chế này.

<sub>`chemistry.thpt.huu-co-quoc-te.co-che-sn1` · lớp 10, 11, 12 · #a-level #ib-hl #sn1 #co-che #carbocation</sub>

---

**Cơ chế SN2: thế nucleophin lưỡng phân tử** — *SN2 mechanism: bimolecular nucleophilic substitution*

$$v = k\,[\mathrm{RX}]\,[\mathrm{Nu^{-}}]$$

Trong đó: `v` là tốc độ phản ứng thế (mol/(L*s)); `k` là hằng số tốc độ bậc hai (L/(mol*s)); `[\mathrm{RX}]` là nồng độ dẫn xuất halogen (mol/L); `[\mathrm{Nu^{-}}]` là nồng độ tác nhân nucleophin (mol/L).

*Điều kiện:* Ưu tiên với dẫn xuất bậc I, nucleophin mạnh, dung môi phân cực không proton; một giai đoạn qua trạng thái chuyển tiếp năm phối trí

*Ghi chú:* Cơ chế bắt buộc của A-Level (AQA 3.3.3, CIE 9701) và IB HL Reactivity 3.4. Hệ quả lập thể quan trọng: nucleophin tấn công từ phía đối diện nhóm đi ra nên cấu hình bị NGHỊCH ĐẢO (Walden inversion). CT GDPT 2018 Việt Nam mô tả phản ứng thế của dẫn xuất halogen nhưng không dạy cơ chế SN1/SN2.

<sub>`chemistry.thpt.huu-co-quoc-te.co-che-sn2` · lớp 10, 11, 12 · #a-level #ib-hl #sn2 #co-che #the-nucleophin</sub>

---

**Quy tắc định hướng của nhóm thế trên vòng benzene** — *Directing effects of substituents on a benzene ring*

$$\begin{cases} \text{nhom day electron } (-\mathrm{OH},\ -\mathrm{NH_{2}},\ -\mathrm{R}) & \text{hoat hoa, dinh huong } ortho,\ para \\ \text{nhom hut electron } (-\mathrm{NO_{2}},\ -\mathrm{COOH},\ -\mathrm{CN}) & \text{phan hoat hoa, dinh huong } meta \\ \text{halogen } (-\mathrm{X}) & \text{phan hoat hoa nhung dinh huong } ortho,\ para \end{cases}$$

Trong đó: `-\mathrm{OH}` là nhóm hydroxyl, đẩy electron mạnh bằng hiệu ứng liên hợp dương; `-\mathrm{NH_{2}}` là nhóm amino, đẩy electron mạnh; `-\mathrm{R}` là gốc alkyl, đẩy electron yếu bằng hiệu ứng cảm ứng dương; `-\mathrm{NO_{2}}` là nhóm nitro, hút electron mạnh; `-\mathrm{COOH}` là nhóm carboxyl, hút electron; `-\mathrm{CN}` là nhóm cyano, hút electron; `-\mathrm{X}` là nguyên tử halogen, hút electron theo cảm ứng nhưng đẩy theo liên hợp.

*Điều kiện:* Áp dụng cho phản ứng thế electrophin trên vòng thơm đã có sẵn một nhóm thế

*Ghi chú:* Cambridge 9701 mục 27.1 yêu cầu 'describe that in the electrophilic substitution of arenes, different substituents direct to different ring positions'; AQA và Edexcel cũng có. Halogen là trường hợp bất thường đáng nhớ (vừa phản hoạt hoá vừa định hướng ortho, para) vì hút electron theo cảm ứng nhưng đẩy electron theo liên hợp. Kho Việt Nam chỉ có công thức đếm đồng phân vị trí của dẫn xuất hai nhóm thế, không có quy tắc định hướng.

<sub>`chemistry.thpt.huu-co-quoc-te.dinh-huong-nhom-the-vong-thom` · lớp 10, 11, 12 · #a-level #vong-thom #dinh-huong #the-electrophin</sub>

---

**Cơ chế thế electrophin vào vòng thơm** — *Electrophilic aromatic substitution mechanism*

$$\mathrm{C_{6}H_{6}} + \mathrm{E^{+}} \rightarrow \left[ \mathrm{C_{6}H_{6}E} \right]^{+} \rightarrow \mathrm{C_{6}H_{5}E} + \mathrm{H^{+}}$$

Trong đó: `\mathrm{C_{6}H_{6}}` là benzene, hệ thơm giàu electron pi; `\mathrm{E^{+}}` là tác nhân electrophin, ví dụ NO2+ hoặc CH3CO+; `\left[ \mathrm{C_{6}H_{6}E} \right]^{+}` là phức sigma (ion arenium) trung gian, mất tính thơm tạm thời; `\mathrm{C_{6}H_{5}E}` là sản phẩm thế trên vòng thơm; `\mathrm{H^{+}}` là proton tách ra để khôi phục hệ thơm.

*Điều kiện:* Electrophin thường phải được tạo ra tại chỗ, ví dụ NO2+ từ hỗn hợp HNO3 đặc và H2SO4 đặc, hoặc CH3CO+ nhờ xúc tác AlCl3

*Ghi chú:* A-Level (AQA 3.3.10, CIE) và IB HL yêu cầu vẽ cơ chế nitro hoá và acyl hoá Friedel - Crafts bằng mũi tên cong. Điểm mấu chốt: benzene ưu tiên THẾ chứ không CỘNG để giữ lại năng lượng bền hoá thơm. CT GDPT 2018 Việt Nam có phản ứng nitro hoá benzene nhưng không yêu cầu cơ chế.

<sub>`chemistry.thpt.huu-co-quoc-te.the-electrophin-vong-thom` · lớp 10, 11, 12 · #a-level #ib-hl #co-che #the-electrophin #vong-thom</sub>

---

**Cơ chế E1: tách đơn phân tử** — *E1 mechanism: unimolecular elimination*

$$v = k\,[\mathrm{RX}]$$

Trong đó: `v` là tốc độ phản ứng tách (mol/(L*s)); `k` là hằng số tốc độ bậc một (1/s); `[\mathrm{RX}]` là nồng độ dẫn xuất halogen hoặc alcohol đã proton hoá (mol/L).

*Điều kiện:* Base yếu, dung môi phân cực có proton, cơ chất bậc III; hai giai đoạn với bước chậm là tạo carbocation, giống hệt bước đầu của SN1

*Ghi chú:* A-Level nâng cao và giáo trình quốc tế. Vì E1 và SN1 dùng chung bước chậm nên chúng luôn cạnh tranh và cho hỗn hợp sản phẩm. Phản ứng tách nước alcohol bằng H2SO4 đặc mà CT GDPT 2018 Việt Nam dạy chính là cơ chế E1, nhưng chương trình Việt Nam không gọi tên và không phân tích cơ chế.

<sub>`chemistry.thpt.huu-co-quoc-te.co-che-e1` · lớp 10, 11, 12 · #a-level #e1 #co-che #carbocation</sub>

---

**Cơ chế E2 và quy tắc Zaitsev** — *E2 mechanism and Zaitsev's rule*

$$v = k\,[\mathrm{RX}]\,[\mathrm{B^{-}}]$$

Trong đó: `v` là tốc độ phản ứng tách (mol/(L*s)); `k` là hằng số tốc độ bậc hai (L/(mol*s)); `[\mathrm{RX}]` là nồng độ dẫn xuất halogen (mol/L); `[\mathrm{B^{-}}]` là nồng độ base mạnh (mol/L).

*Điều kiện:* Base mạnh (ví dụ KOH trong ethanol), nhiệt độ cao; H bị tách và nhóm X phải ở vị trí anti-periplanar (cùng mặt phẳng, đối diện nhau)

*Ghi chú:* A-Level (AQA, CIE) và IB HL. Quy tắc Zaitsev: alkene chính là alkene có nhiều nhóm thế nhất trên liên kết đôi vì bền hơn. CT GDPT 2018 Việt Nam có quy tắc Zaitsev cho phản ứng tách nước của alcohol nhưng không dạy cơ chế E2 và yêu cầu anti-periplanar.

<sub>`chemistry.thpt.huu-co-quoc-te.co-che-e2` · lớp 10, 11, 12 · #a-level #ib-hl #e2 #co-che #zaitsev</sub>

---

**Bậc của nguyên tử carbon và bậc của dẫn xuất** — *Degree (class) of a carbon atom and of a derivative*

$$b_{C} = n_{C\!-\!C}$$

Trong đó: `b_{C}` là bậc của nguyên tử carbon đang xét (); `n_{C\!-\!C}` là số nguyên tử carbon khác liên kết trực tiếp với nguyên tử carbon đó ().

*Điều kiện:* Chỉ đếm liên kết C-C, không đếm liên kết với H hay với nhóm chức

*Ghi chú:* Thuật ngữ primary (bậc I), secondary (bậc II), tertiary (bậc III) và quaternary (bậc IV) được dùng liên tục trong AP, IB và A-Level để dự đoán cơ chế (SN1 hay SN2) và sản phẩm oxi hoá alcohol. Chú ý khác biệt: bậc của AMINE được tính theo số gốc hydrocarbon gắn với nitrogen chứ không theo bậc của carbon. CT GDPT 2018 Việt Nam có nói bậc alcohol và bậc amine nhưng không hệ thống hoá thành định nghĩa dùng cho lập luận cơ chế.

<sub>`chemistry.thpt.huu-co-quoc-te.bac-nguyen-tu-carbon` · lớp 10, 11, 12 · #ap #ib #a-level #danh-phap #bac-carbon</sub>

---

**Thứ tự độ bền của carbocation** — *Stability order of carbocations*

$$\mathrm{R_{3}C^{+}} > \mathrm{R_{2}CH^{+}} > \mathrm{RCH_{2}^{+}} > \mathrm{CH_{3}^{+}}$$

Trong đó: `\mathrm{R_{3}C^{+}}` là carbocation bậc III; `\mathrm{R_{2}CH^{+}}` là carbocation bậc II; `\mathrm{RCH_{2}^{+}}` là carbocation bậc I; `\mathrm{CH_{3}^{+}}` là cation methyl.

*Điều kiện:* Nhóm alkyl đẩy electron (hiệu ứng cảm ứng dương và siêu liên hợp) làm giảm mật độ điện tích dương nên bền hơn; carbocation allyl và benzyl còn bền hơn nhờ cộng hưởng

*Ghi chú:* Nguyên lí giải thích xuyên suốt của A-Level và IB HL: vì sao dẫn xuất bậc III đi theo SN1, vì sao quy tắc Markovnikov đúng. CT GDPT 2018 Việt Nam nêu quy tắc Markovnikov như một quy tắc kinh nghiệm mà không giải thích bằng độ bền carbocation.

<sub>`chemistry.thpt.huu-co-quoc-te.do-ben-carbocation` · lớp 10, 11, 12 · #a-level #ib-hl #carbocation #do-ben</sub>

---

**Danh pháp E/Z cho đồng phân hình học** — *E/Z nomenclature for geometric isomers*

$$\begin{cases} \text{hai nhom uu tien cung phia} & Z \\ \text{hai nhom uu tien khac phia} & E \end{cases}$$

Trong đó: `Z` là cấu hình zusammen: hai nhóm ưu tiên cao ở hai carbon nằm cùng phía mặt phẳng liên kết đôi; `E` là cấu hình entgegen: hai nhóm ưu tiên cao nằm khác phía.

*Điều kiện:* Xác định nhóm ưu tiên trên MỖI carbon của liên kết đôi theo quy tắc CIP; áp dụng được cả khi mỗi carbon mang hai nhóm đều khác nhau

*Ghi chú:* Danh pháp IUPAC hiện hành, bắt buộc trong AQA (3.3.1), Edexcel và IB. Ranh giới cần nhớ: Cambridge 9701 ghi 'use of E/Z nomenclature is acceptable but is not required', tức thi CIE vẫn chấm điểm cis/trans. Khác với cis/trans của CT GDPT 2018 Việt Nam: cis/trans chỉ dùng được khi mỗi carbon của liên kết đôi mang một nguyên tử hydrogen hoặc hai nhóm giống nhau, còn E/Z luôn dùng được. Không phải lúc nào cis cũng trùng Z.

<sub>`chemistry.thpt.huu-co-quoc-te.danh-phap-e-z` · lớp 10, 11, 12 · #a-level #ib #iupac #e-z #dong-phan-hinh-hoc</sub>

---

**Quy tắc Cahn - Ingold - Prelog và danh pháp R/S** — *Cahn - Ingold - Prelog rules and R/S nomenclature*

$$a > b > c > d,\ d\ \text{huong ra xa} \Rightarrow a \to b \to c:\ \text{cung chieu kim dong ho} = R,\ \text{nguoc lai} = S$$

Trong đó: `a` là nhóm thế có độ ưu tiên cao nhất trên tâm lập thể; `b` là nhóm thế có độ ưu tiên thứ hai; `c` là nhóm thế có độ ưu tiên thứ ba; `d` là nhóm thế có độ ưu tiên thấp nhất, được hướng ra xa người quan sát; `R` là cấu hình rectus, chiều a - b - c cùng chiều kim đồng hồ; `S` là cấu hình sinister, chiều a - b - c ngược chiều kim đồng hồ.

*Điều kiện:* Độ ưu tiên xếp theo số hiệu nguyên tử của nguyên tử gắn trực tiếp; nếu bằng nhau thì so tiếp ở lớp nguyên tử kế tiếp; liên kết đôi được nhân đôi nguyên tử

*Ghi chú:* SỬA PHẠM VI CHƯƠNG TRÌNH: danh pháp R/S theo quy tắc Cahn - Ingold - Prelog là chuẩn IUPAC nhưng KHÔNG nằm trong AP Chemistry, IB Chemistry hay A-Level Chemistry. Cambridge 9701 chỉ yêu cầu nhận diện tâm bất đối và hai đối quang, còn E/Z thì 'acceptable but is not required'; AQA và Edexcel cũng dừng lại ở E/Z. R/S được dùng ở đề olympic hoá học, ở các chương trình dự bị đại học và từ năm thứ nhất đại học trở đi. Độ ưu tiên xếp theo số hiệu nguyên tử của nguyên tử gắn trực tiếp, liên kết đôi được nhân đôi nguyên tử. CT GDPT 2018 Việt Nam không dạy quy tắc CIP cho tâm lập thể.

<sub>`chemistry.thpt.huu-co-quoc-te.quy-tac-cip-r-s` · lớp 10, 11, 12 · #olympiad #iupac #cip #danh-phap-r-s</sub>

---

**Tâm lập thể và số đồng phân lập thể tối đa** — *Stereocentres and the maximum number of stereoisomers*

$$N_{lt} = 2^{n^{*}}$$

Trong đó: `N_{lt}` là số đồng phân lập thể tối đa của phân tử (); `n^{*}` là số tâm lập thể (nguyên tử carbon bất đối) trong phân tử ().

*Điều kiện:* Carbon bất đối là carbon liên kết với BỐN nhóm khác nhau; số thực tế nhỏ hơn 2^n nếu phân tử có yếu tố đối xứng nội (hợp chất meso)

*Ghi chú:* IB Structure 3.2 (HL) và A-Level yêu cầu nhận diện carbon bất đối và đếm đồng phân quang học; AP nhắc tới đồng phân quang học ở mức nhận biết. Ranh giới cần nhớ: Cambridge 9701 ghi rõ 'candidates should appreciate that compounds can contain more than one chiral centre, but knowledge of meso compounds, or nomenclature such as diastereoisomers is not required' - hợp chất meso chỉ bắt buộc với AQA/Edexcel và IB, không bắt buộc với CIE. Hai đối quang có tính chất vật lí giống hệt nhau trừ chiều quay mặt phẳng ánh sáng phân cực và hoạt tính sinh học. CT GDPT 2018 Việt Nam chỉ dạy đồng phân hình học cis - trans, không dạy đồng phân quang học ở THPT.

<sub>`chemistry.thpt.huu-co-quoc-te.tam-lap-the-va-so-dong-phan` · lớp 10, 11, 12 · #ib-hl #a-level #dong-phan-quang-hoc #tam-lap-the</sub>

---

### Khí lí tưởng và thuyết động học phân tử

**Định luật Graham về khuếch tán và thoát khí** — *Graham's law of diffusion and effusion*

$$\dfrac{r_{1}}{r_{2}} = \sqrt{\dfrac{M_{2}}{M_{1}}} = \sqrt{\dfrac{\rho_{2}}{\rho_{1}}}$$

Trong đó: `r_{1}` là tốc độ thoát (hoặc khuếch tán) của khí 1 (mol/s); `r_{2}` là tốc độ thoát (hoặc khuếch tán) của khí 2 (mol/s); `M_{1}` là khối lượng mol của khí 1 (g/mol); `M_{2}` là khối lượng mol của khí 2 (g/mol); `\rho_{1}` là khối lượng riêng của khí 1 (kg/m^3); `\rho_{2}` là khối lượng riêng của khí 2 (kg/m^3).

*Điều kiện:* Hai khí ở cùng nhiệt độ và áp suất, coi là khí lí tưởng; với sự thoát khí (effusion) thì lỗ thoát phải rất nhỏ so với quãng đường tự do trung bình

*Ghi chú:* SỬA PHẠM VI CHƯƠNG TRÌNH: định luật Graham KHÔNG còn nằm trong AP Chemistry - hai từ khoá 'effusion' và 'Graham' không xuất hiện ở bất kì đâu trong CED hiện hành (hiệu lực từ mùa thu 2024) và cũng không có trên bảng công thức kì thi; nội dung này bị loại từ đợt thiết kế lại năm 2013. Định luật cũng không có trong IB Chemistry (first assessment 2025) lẫn Cambridge 9701. Giữ lại vì vẫn rất phổ biến trong sách giáo khoa quốc tế cũ và trong đề olympic. Vì tốc độ tỉ lệ nghịch với thời gian nên cũng viết được t1/t2 = căn(M1/M2). CT GDPT 2018 Việt Nam không có định luật Graham.

<sub>`chemistry.thpt.khi-li-tuong.dinh-luat-graham` · lớp 10, 11, 12 · #olympiad #khi-li-tuong #graham #khuech-tan</sub>

---

**Thừa số Boltzmann: tỉ lệ phân tử vượt năng lượng hoạt hoá** — *Boltzmann factor: fraction of molecules exceeding the activation energy*

$$f = e^{-E_{a}/(RT)}$$

Trong đó: `f` là tỉ lệ số phân tử có năng lượng lớn hơn hoặc bằng năng lượng hoạt hoá (); `E_{a}` là năng lượng hoạt hoá của phản ứng (J/mol); `R` là hằng số khí, 8,314 J/(K.mol) (J/(mol*K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Ea phải cùng đơn vị với RT, thường quy về J/mol

*Ghi chú:* A-Level (AQA 3.1.5 và 3.1.9, CIE 9701) và IB (Reactivity 2.2) dùng thừa số này để giải thích đường cong Maxwell - Boltzmann: tăng nhiệt độ hoặc dùng xúc tác đều làm tăng mạnh phần diện tích bên phải Ea. Đây chính là phần mũ của phương trình Arrhenius. CT GDPT 2018 chỉ nêu định tính, không đưa biểu thức.

<sub>`chemistry.thpt.khi-li-tuong.thua-so-boltzmann` · lớp 10, 11, 12 · #a-level #ib #maxwell-boltzmann #nang-luong-hoat-hoa</sub>

---

**Hệ số nén và sai lệch của khí thực khỏi khí lí tưởng** — *Compressibility factor and deviations from ideal behaviour*

$$Z = \dfrac{p V_{m}}{RT}$$

Trong đó: `Z` là hệ số nén; khí lí tưởng có Z = 1 ở mọi điều kiện (); `p` là áp suất của khí (Pa); `V_{m}` là thể tích mol thực tế của khí (m^3/mol); `R` là hằng số khí, 8,314 J/(K.mol) (J/(mol*K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Z < 1 khi lực hút liên phân tử chiếm ưu thế (áp suất trung bình, nhiệt độ thấp); Z > 1 khi thể tích riêng của phân tử chiếm ưu thế (áp suất rất cao)

*Ghi chú:* SỬA PHẠM VI CHƯƠNG TRÌNH: hệ số nén Z là công cụ ĐỊNH LƯỢNG không nằm trong AP, IB hay A-Level. AP Chemistry Topic 3.6 'Deviation from Ideal Gas Law' chỉ yêu cầu giải thích ĐỊNH TÍNH rằng sai lệch sinh ra từ lực hút liên phân tử (gần điều kiện ngưng tụ) và từ thể tích riêng của phân tử (áp suất rất cao); Cambridge 9701 không có 'compression factor'. Z là chuẩn mực định lượng ở bậc đại học và trong đề olympic. Kết luận định tính chung cho cả ba hệ: khí gần lí tưởng nhất ở áp suất thấp và nhiệt độ cao. CT GDPT 2018 Việt Nam không đưa hệ số nén Z vào môn Hoá học.

<sub>`chemistry.thpt.khi-li-tuong.he-so-nen-khi-thuc` · lớp 10, 11, 12 · #olympiad #khi-thuc #he-so-nen #khi-li-tuong</sub>

---

### Liên kết hóa học

**Tổng số oxi hóa trong ion đa nguyên tử** — *Sum of oxidation numbers in a polyatomic ion*

$$\sum_{i} x_{i} \cdot \text{SOH}_{i} = q_{ion}$$

Trong đó: `x_{i}` là số nguyên tử của nguyên tố thứ i; `\text{SOH}_{i}` là số oxi hóa của nguyên tố thứ i; `q_{ion}` là điện tích của ion.

*Điều kiện:* Ion đa nguyên tử; điện tích tính theo đơn vị điện tích nguyên tố

*Ghi chú:* Ví dụ trong SO4 2-: SOH(S) + 4(-2) = -2 nên SOH(S) = +6. Với ion đơn nguyên tử, số oxi hóa bằng điện tích ion.

<sub>`chemistry.thpt.lien-ket.so-oxi-hoa-trong-ion` · lớp 10, 11, 12 · #so-oxi-hoa #ion #thpt</sub>

---

**Tổng số oxi hóa trong phân tử trung hòa** — *Sum of oxidation numbers in a neutral molecule*

$$\sum_{i} x_{i} \cdot \text{SOH}_{i} = 0$$

Trong đó: `x_{i}` là số nguyên tử của nguyên tố thứ i trong phân tử; `\text{SOH}_{i}` là số oxi hóa của nguyên tố thứ i.

*Điều kiện:* Phân tử trung hòa điện

*Ghi chú:* Quy ước: số oxi hóa của đơn chất bằng 0; H thường là +1 (trừ hiđrua kim loại là -1); O thường là -2 (trừ peroxide là -1 và OF2 là +2).

<sub>`chemistry.thpt.lien-ket.so-oxi-hoa-trong-phan-tu` · lớp 10, 11, 12 · #so-oxi-hoa #quy-tac #thpt</sub>

---

### Nhiệt hoá học quốc tế

**Chu trình Born - Haber cho hợp chất ion** — *Born - Haber cycle for an ionic compound*

$$\Delta_{f}H^{\ominus} = \Delta_{at}H^{\ominus}(\mathrm{M}) + \sum \Delta_{IE}H^{\ominus} + \Delta_{at}H^{\ominus}(\mathrm{X}) + \sum \Delta_{EA}H^{\ominus} + \Delta_{lat}H^{\ominus}_{f}$$

Trong đó: `\Delta_{f}H^{\ominus}` là enthalpy tạo thành chuẩn của hợp chất ion rắn (kJ/mol); `\Delta_{at}H^{\ominus}(\mathrm{M})` là enthalpy nguyên tử hoá của kim loại (kJ/mol); `\Delta_{IE}H^{\ominus}` là năng lượng ion hoá từng nấc của kim loại (kJ/mol); `\Delta_{at}H^{\ominus}(\mathrm{X})` là enthalpy nguyên tử hoá của phi kim (kJ/mol); `\Delta_{EA}H^{\ominus}` là ái lực electron từng nấc của phi kim (kJ/mol); `\Delta_{lat}H^{\ominus}_{f}` là enthalpy mạng lưới theo quy ước tạo thành (kJ/mol).

*Điều kiện:* Mỗi số hạng lấy đúng số mol theo công thức hợp chất; bản chất là định luật Hess áp dụng cho chu trình khép kín

*Ghi chú:* Nội dung trọng tâm của A-Level (AQA 3.1.8, CIE 9701, Edexcel Topic 13) và IB HL. So sánh enthalpy mạng lưới thực nghiệm (từ Born - Haber) với giá trị lí thuyết theo mô hình ion thuần tuý cho biết mức độ cộng hoá trị của liên kết. Kho AISTEM đã có bản đại học; bản này trình bày ở dạng THPT quốc tế.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.chu-trinh-born-haber` · lớp 10, 11, 12 · #a-level #ib-hl #born-haber #chu-trinh-nang-luong</sub>

---

**Enthalpy hoà tan tính theo chu trình năng lượng** — *Enthalpy of solution from an energy cycle*

$$\Delta_{sol}H^{\ominus} = -\Delta_{lat}H^{\ominus}_{f} + \sum \Delta_{hyd}H^{\ominus}$$

Trong đó: `\Delta_{sol}H^{\ominus}` là enthalpy hoà tan chuẩn của hợp chất ion (kJ/mol); `\Delta_{lat}H^{\ominus}_{f}` là enthalpy mạng lưới theo quy ước tạo thành, giá trị âm (kJ/mol); `\Delta_{hyd}H^{\ominus}` là enthalpy hidrat hoá của từng ion, lấy đúng số mol ion (kJ/mol).

*Điều kiện:* Chu trình Hess: phá mạng tinh thể thành ion khí rồi hidrat hoá các ion đó

*Ghi chú:* A-Level chuẩn. Nếu dùng quy ước phân li thì công thức thành Delta_sol H = Delta_lat H(phân li) + tổng Delta_hyd H. Muối tan thu nhiệt như NH4NO3 là do enthalpy mạng lưới trội hơn hidrat hoá, quá trình vẫn xảy ra nhờ entropy tăng. CT GDPT 2018 Việt Nam không có nội dung này.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.enthalpy-hoa-tan` · lớp 10, 11, 12 · #a-level #enthalpy-hoa-tan #chu-trinh-nang-luong #hess</sub>

---

**Enthalpy phản ứng tính từ enthalpy đốt cháy chuẩn** — *Enthalpy of reaction from standard enthalpies of combustion*

$$\Delta H^{\ominus} = \sum m\, \Delta_{c}H^{\ominus}_{tg} - \sum n\, \Delta_{c}H^{\ominus}_{sp}$$

Trong đó: `\Delta H^{\ominus}` là biến thiên enthalpy chuẩn của phản ứng cần tính (kJ/mol); `m` là hệ số tỉ lượng của từng chất tham gia (); `\Delta_{c}H^{\ominus}_{tg}` là enthalpy đốt cháy chuẩn của từng chất tham gia (kJ/mol); `n` là hệ số tỉ lượng của từng sản phẩm (); `\Delta_{c}H^{\ominus}_{sp}` là enthalpy đốt cháy chuẩn của từng sản phẩm (kJ/mol).

*Điều kiện:* Mọi chất đều cháy hoàn toàn ra cùng bộ sản phẩm (CO2 và H2O); điều kiện chuẩn, thường quy về 298 K

*Ghi chú:* Chemistry Data Booklet của IB (mục 1) in ĐỒNG THỜI hai hệ thức Hess: dạng theo enthalpy TẠO THÀNH (sản phẩm trừ chất tham gia) và dạng theo enthalpy ĐỐT CHÁY (chất tham gia trừ sản phẩm). Bẫy lớn nhất là thứ tự trừ ĐẢO NGƯỢC giữa hai hệ thức. A-Level (Cambridge 9701 mục 6.2, AQA 3.1.4) coi đây là một trong hai chu trình Hess bắt buộc, dùng cho phản ứng không đo trực tiếp được như sự tạo thành hydrocarbon từ đơn chất. CT GDPT 2018 Việt Nam chỉ cấp bảng enthalpy tạo thành chuẩn nên không có dạng bài này.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.enthalpy-tu-nhiet-dot-chay` · lớp 10, 11, 12 · #ib #a-level #hess #enthalpy-dot-chay</sub>

---

**Ái lực electron thứ nhất và thứ hai** — *First and second electron affinity*

$$\mathrm{X}(g) + e^{-} \rightarrow \mathrm{X}^{-}(g),\ \Delta_{EA1}H^{\ominus} < 0; \qquad \mathrm{X}^{-}(g) + e^{-} \rightarrow \mathrm{X}^{2-}(g),\ \Delta_{EA2}H^{\ominus} > 0$$

Trong đó: `\Delta_{EA1}H^{\ominus}` là ái lực electron thứ nhất: nhiệt kèm theo khi 1 mol nguyên tử khí nhận 1 mol electron (kJ/mol); `\Delta_{EA2}H^{\ominus}` là ái lực electron thứ hai: nhiệt kèm theo khi 1 mol ion 1- nhận thêm 1 mol electron (kJ/mol).

*Điều kiện:* Mọi tiểu phân ở thể khí, điều kiện chuẩn

*Ghi chú:* A-Level và IB HL yêu cầu giải thích vì sao ái lực electron thứ nhất âm (hạt nhân hút electron) còn thứ hai luôn dương (phải đẩy electron vào ion đã tích điện âm). Với oxygen: EA1 khoảng -141 kJ/mol, EA2 khoảng +798 kJ/mol. CT GDPT 2018 Việt Nam chỉ dạy năng lượng ion hoá, không dạy ái lực electron định lượng.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.ai-luc-electron` · lớp 10, 11, 12 · #a-level #ib-hl #ai-luc-electron #born-haber</sub>

---

**Enthalpy hidrat hoá của ion** — *Standard enthalpy of hydration of an ion*

$$\mathrm{X}^{z}(g) \rightarrow \mathrm{X}^{z}(aq), \qquad \Delta_{hyd}H^{\ominus} < 0, \qquad \left| \Delta_{hyd}H^{\ominus} \right| \propto \dfrac{|z|}{r_{ion}}$$

Trong đó: `\Delta_{hyd}H^{\ominus}` là enthalpy hidrat hoá chuẩn: nhiệt kèm theo khi 1 mol ion khí tan vào lượng nước rất lớn (kJ/mol); `z` là điện tích của ion (); `r_{ion}` là bán kính ion (m).

*Điều kiện:* Ion ban đầu ở thể khí, sản phẩm là dung dịch loãng vô hạn; quá trình luôn toả nhiệt

*Ghi chú:* A-Level (AQA 3.1.8, Edexcel Topic 13) yêu cầu giải thích xu hướng: ion nhỏ và điện tích lớn có mật độ điện tích cao nên hidrat hoá mạnh hơn. Đây là mảnh ghép để tính enthalpy hoà tan. CT GDPT 2018 Việt Nam không có đại lượng này.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.enthalpy-hidrat-hoa` · lớp 10, 11, 12 · #a-level #hidrat-hoa #enthalpy #mat-do-dien-tich</sub>

---

**Enthalpy nguyên tử hoá chuẩn** — *Standard enthalpy of atomisation*

$$\tfrac{1}{2}\mathrm{Cl_{2}}(g) \rightarrow \mathrm{Cl}(g), \qquad \Delta_{at}H^{\ominus} > 0$$

Trong đó: `\Delta_{at}H^{\ominus}` là enthalpy nguyên tử hoá chuẩn: nhiệt kèm theo khi tạo 1 mol nguyên tử thể khí từ đơn chất ở trạng thái chuẩn (kJ/mol).

*Điều kiện:* Điều kiện chuẩn 100 kPa, thường quy về 298 K; luôn thu nhiệt vì phải phá vỡ liên kết

*Ghi chú:* Định nghĩa bắt buộc của A-Level (AQA 3.1.8, CIE 9701) để dựng chu trình Born - Haber. Chú ý: với Cl2 thì Delta_at H bằng MỘT NỬA năng lượng liên kết Cl-Cl vì tính cho 1 mol nguyên tử. CT GDPT 2018 Việt Nam không có đại lượng này.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.enthalpy-nguyen-tu-hoa` · lớp 10, 11, 12 · #a-level #born-haber #enthalpy #nguyen-tu-hoa</sub>

---

**Enthalpy trung hoà chuẩn** — *Standard enthalpy of neutralisation*

$$\mathrm{H^{+}}(aq) + \mathrm{OH^{-}}(aq) \rightarrow \mathrm{H_{2}O}(l), \qquad \Delta_{neut}H^{\ominus} \approx -57\ \mathrm{kJ\,mol^{-1}}$$

Trong đó: `\Delta_{neut}H^{\ominus}` là enthalpy trung hoà chuẩn: nhiệt toả ra khi tạo 1 mol nước từ phản ứng acid - base trong dung dịch loãng (kJ/mol).

*Điều kiện:* Acid mạnh với base mạnh, dung dịch loãng, điều kiện chuẩn; tính cho 1 mol H2O tạo thành

*Ghi chú:* A-Level và IB dùng làm giá trị đối chiếu cho thí nghiệm nhiệt lượng kế cốc nhựa (giá trị thường trích dẫn từ -57 đến -58 kJ/mol). Điểm quan trọng: với acid yếu hoặc base yếu, giá trị kém âm hơn vì một phần nhiệt dùng cho sự điện li. CT GDPT 2018 Việt Nam không đưa đại lượng chuẩn hoá này.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.enthalpy-trung-hoa-chuan` · lớp 10, 11, 12 · #a-level #ib #enthalpy #trung-hoa</sub>

---

**Enthalpy mạng lưới: quy ước tạo thành và quy ước phân li** — *Lattice enthalpy: formation and dissociation conventions*

$$\mathrm{M}^{n+}(g) + n\,\mathrm{X}^{-}(g) \rightarrow \mathrm{MX}_{n}(s), \quad \Delta_{lat}H^{\ominus}_{f} = -\Delta_{lat}H^{\ominus}_{d} < 0$$

Trong đó: `\Delta_{lat}H^{\ominus}_{f}` là enthalpy mạng lưới theo quy ước TẠO THÀNH mạng tinh thể từ các ion khí, luôn âm (kJ/mol); `\Delta_{lat}H^{\ominus}_{d}` là enthalpy mạng lưới theo quy ước PHÂN LI mạng tinh thể thành các ion khí, luôn dương (kJ/mol); `n` là số ion X- ứng với một ion M(n+) trong công thức hợp chất ().

*Điều kiện:* Các ion ở thể khí và cách nhau vô cùng; hợp chất ion ở trạng thái chuẩn rắn

*Ghi chú:* Điểm bẫy khi thi A-Level: AQA và Edexcel dùng quy ước TẠO THÀNH (giá trị âm) còn OCR và nhiều sách dùng quy ước PHÂN LI (giá trị dương) - phải đọc kĩ đề. Độ lớn tăng khi điện tích ion tăng và bán kính ion giảm. CT GDPT 2018 Việt Nam không có đại lượng này ở THPT; kho AISTEM chỉ có bản đại học qua phương trình Born - Lande.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.nang-luong-mang-luoi` · lớp 10, 11, 12 · #a-level #nang-luong-mang-luoi #born-haber #quy-uoc-dau</sub>

---

**Hiệu chỉnh nhiệt độ bằng phép ngoại suy đồ thị** — *Extrapolation correction for heat loss in calorimetry*

$$\Delta T_{hc} = T_{ext} - T_{0}$$

Trong đó: `\Delta T_{hc}` là độ tăng nhiệt độ đã hiệu chỉnh, dùng để tính nhiệt lượng (K); `T_{ext}` là nhiệt độ cực đại suy ra bằng cách ngoại suy đoạn nguội về thời điểm trộn (K); `T_{0}` là nhiệt độ ban đầu của hệ tại thời điểm trộn (K).

*Điều kiện:* Dùng khi phản ứng chậm hoặc nhiệt lượng kế mất nhiệt đáng kể; vẽ đồ thị nhiệt độ theo thời gian rồi kéo dài đoạn tuyến tính phần nguội ngược về thời điểm trộn

*Ghi chú:* Kĩ thuật thực hành bắt buộc trong A-Level (AQA Required Practical, Edexcel Core Practical) và được khuyến khích trong IB IA. CT GDPT 2018 Việt Nam chỉ lấy trực tiếp nhiệt độ cao nhất đo được.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.hieu-chinh-ngoai-suy-nhiet-do` · lớp 10, 11, 12 · #a-level #ib #thuc-nghiem #nhiet-luong-ke</sub>

---

**Hằng số nhiệt lượng kế và phép chuẩn hoá** — *Calorimeter constant and calibration*

$$C_{cal} = \dfrac{q_{chuan}}{\Delta T_{chuan}}$$

Trong đó: `C_{cal}` là hằng số (nhiệt dung) của nhiệt lượng kế (J/K); `q_{chuan}` là nhiệt lượng đã biết chính xác cấp cho nhiệt lượng kế khi chuẩn hoá (J); `\Delta T_{chuan}` là độ tăng nhiệt độ trong phép chuẩn hoá (K).

*Điều kiện:* Chuẩn hoá bằng chất chuẩn có nhiệt đốt cháy đã biết (thường là acid benzoic) hoặc bằng dây đốt điện với q = UIt

*Ghi chú:* Bước bắt buộc trong thí nghiệm bomb calorimetry của A-Level. Không gán cho AP vì AP không làm nhiệt lượng kế đẳng tích (xem bản ghi bomb calorimeter). CT GDPT 2018 Việt Nam giả thiết toàn bộ nhiệt truyền vào nước với c = 4,18 J/(g.K) và bỏ qua nhiệt dung của dụng cụ.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.hang-so-nhiet-luong-ke` · lớp 10, 11, 12 · #a-level #nhiet-luong-ke #chuan-hoa</sub>

---

**Nhiệt lượng kế thể tích không đổi (bom nhiệt lượng)** — *Constant-volume (bomb) calorimetry*

$$q_{V} = -C_{cal}\,\Delta T, \qquad \Delta U_{r} = \dfrac{q_{V}}{n}$$

Trong đó: `q_{V}` là nhiệt lượng phản ứng trao đổi ở thể tích không đổi (J); `C_{cal}` là nhiệt dung của toàn bộ nhiệt lượng kế, kể cả nước và vỏ bom (J/K); `\Delta T` là độ tăng nhiệt độ đo được của nhiệt lượng kế (K); `\Delta U_{r}` là biến thiên nội năng của phản ứng, tính cho 1 mol chất (J/mol); `n` là số mol chất bị đốt cháy (mol).

*Điều kiện:* Bom kín nên thể tích không đổi, không có công giãn nở; nhiệt đo được ứng với biến thiên NỘI NĂNG chứ không phải enthalpy

*Ghi chú:* A-Level (Edexcel, Cambridge 9701) mô tả bomb calorimeter để đo nhiệt đốt cháy. KHÔNG được gán cho AP: CED của AP Chemistry có exclusion statement 'The technical distinctions between enthalpy and internal energy will not be assessed on the AP Exam', và AP chỉ làm nhiệt lượng kế đẳng áp (Topic 6.4 Heat Capacity and Calorimetry). Khác biệt cốt lõi so với nhiệt lượng kế cốc cà phê đẳng áp mà CT GDPT 2018 dùng: đẳng tích cho Delta U, đẳng áp cho Delta H; với phản ứng không đổi số mol khí thì hai đại lượng bằng nhau.

<sub>`chemistry.thpt.nhiet-hoa-quoc-te.nhiet-luong-ke-the-tich-khong-doi` · lớp 10, 11, 12 · #a-level #nhiet-luong-ke #bomb-calorimeter #noi-nang</sub>

---

### Nhiệt hóa học

**Biến thiên năng lượng tự do Gibbs** — *Gibbs free energy change*

$$\Delta G = \Delta H - T \Delta S$$

Trong đó: `\Delta G` là biến thiên năng lượng tự do Gibbs (J/mol); `\Delta H` là biến thiên enthalpy (J/mol); `T` là nhiệt độ tuyệt đối (K); `\Delta S` là biến thiên entropy (J/(mol.K)).

*Điều kiện:* Nhiệt độ và áp suất không đổi; chú ý thống nhất đơn vị (kJ và J)

*Ghi chú:* Kiến thức nâng cao. Delta G < 0: quá trình tự diễn biến; Delta G = 0: hệ ở cân bằng; Delta G > 0: không tự diễn biến.

<sub>`chemistry.thpt.nhiet-hoa.nang-luong-tu-do-gibbs` · lớp 10, 12 · #gibbs #entropy #nang-cao</sub>

---

### Olympiad Hoá học: Cân bằng và phân tích (IChO)

**Điều kiện tách hai bước nhảy khi chuẩn độ hỗn hợp hai axit** — *Condition for resolving two end points when titrating a mixture of acids*

$$\Delta pK_{a}=pK_{a2}-pK_{a1}\ge 4$$

Trong đó: `\Delta pK_{a}` là hiệu số hai giá trị pKa (); `pK_{a1}` là pKa của axit mạnh hơn (hoặc nấc thứ nhất) (); `pK_{a2}` là pKa của axit yếu hơn (hoặc nấc thứ hai) ().

*Điều kiện:* Áp dụng cho hỗn hợp hai axit đơn chức hoặc hai nấc của một axit đa nấc, ở nồng độ không quá loãng (thường trên 0,01 mol/L). Nếu hiệu nhỏ hơn 4 thì hai bước nhảy chồng lên nhau và chỉ quan sát được một bước nhảy tổng

*Ghi chú:* Tiêu chuẩn định lượng này thường được hỏi trong bài chuẩn độ phức tạp của IChO. Kho Việt Nam có các mốc pH trên đường chuẩn độ axit yếu và cách chọn chỉ thị, nhưng không có tiêu chuẩn tách hai bước nhảy.

<sub>`chemistry.thpt.icho-can-bang.tach-hai-buoc-nhay-chuan-do` · lớp 10, 11, 12 · #icho #chuan-do #buoc-nhay #hon-hop</sub>

---

**Phân số nồng độ alpha của axit đơn chức** — *Fractional composition (alpha values) of a monoprotic acid*

$$\alpha_{\mathrm{HA}}=\frac{[\mathrm{H}^{+}]}{[\mathrm{H}^{+}]+K_{a}},\qquad \alpha_{\mathrm{A}^{-}}=\frac{K_{a}}{[\mathrm{H}^{+}]+K_{a}}$$

Trong đó: `\alpha_{\mathrm{HA}}` là phân số nồng độ của dạng axit chưa phân li (); `\alpha_{\mathrm{A}^{-}}` là phân số nồng độ của dạng bazơ liên hợp (); `[\mathrm{H}^{+}]` là nồng độ cân bằng của ion hiđro (mol/L); `K_{a}` là hằng số phân li axit (mol/L).

*Điều kiện:* Tổng hai phân số luôn bằng 1. Tại pH = pKa hai phân số đều bằng 0,5

*Ghi chú:* Giản đồ phân bố alpha theo pH là công cụ chuẩn của IChO khi phân tích hệ đệm và chuẩn độ. Chương trình GDPT 2018 và các file hiện có trong kho không có khái niệm phân số nồng độ alpha.

<sub>`chemistry.thpt.icho-can-bang.phan-so-alpha-axit-don-chuc` · lớp 10, 11, 12 · #icho #can-bang #phan-so-alpha #gian-do-phan-bo</sub>

---

**Định luật giới hạn Debye - Hückel** — *Debye–Hückel limiting law*

$$\log \gamma_{\pm}=-A\,|z_{+}z_{-}|\sqrt{I},\qquad I=\frac{1}{2}\sum_{i} c_{i}z_{i}^{2}$$

Trong đó: `\gamma_{\pm}` là hệ số hoạt độ trung bình của chất điện li (); `A` là hằng số Debye - Hückel, bằng 0,509 với dung dịch nước ở 25 độ C (); `z_{+}` là điện tích của cation (); `z_{-}` là điện tích của anion (); `I` là lực ion của dung dịch (mol/L); `c_{i}` là nồng độ mol của ion thứ i (mol/L); `z_{i}` là điện tích của ion thứ i (); `i` là chỉ số chạy trên tất cả các ion trong dung dịch.

*Điều kiện:* Chỉ đúng ở dung dịch rất loãng, lực ion nhỏ hơn khoảng 0,01 mol/L. Với lực ion lớn hơn phải dùng phương trình Debye - Hückel mở rộng hoặc phương trình Davies

*Ghi chú:* IChO yêu cầu hiệu chỉnh hoạt độ khi tính pH và tích số tan chính xác. Kho Việt Nam có phương trình Debye - Hückel MỞ RỘNG và Davies ở bậc đại học nhưng không có định luật giới hạn cùng định nghĩa lực ion - dạng thường dùng trong đề IChO.

<sub>`chemistry.thpt.icho-can-bang.debye-huckel-gioi-han` · lớp 10, 11, 12 · #icho #hoat-do #debye-huckel #luc-ion</sub>

---

**Điều kiện proton (proton balance)** — *Proton condition (proton balance equation)*

$$\sum \left[\text{tiểu phân nhận proton}\right]\times n = \sum \left[\text{tiểu phân nhường proton}\right]\times n$$

Trong đó: `n` là số proton mà tiểu phân đó đã nhận thêm hoặc nhường bớt so với mức quy chiếu (); `\left[\text{tiểu phân nhận proton}\right]` là nồng độ cân bằng của tiểu phân đã nhận proton so với mức quy chiếu (mol/L); `\left[\text{tiểu phân nhường proton}\right]` là nồng độ cân bằng của tiểu phân đã nhường proton so với mức quy chiếu (mol/L).

*Điều kiện:* Phải chọn mức quy chiếu (reference level) gồm các tiểu phân có mặt ban đầu và nước. Điều kiện proton tương đương với tổ hợp cân bằng điện tích và cân bằng khối lượng

*Ghi chú:* Điều kiện proton là công cụ lập phương trình chính xác nhanh nhất trong bài IChO về dung dịch nhiều cân bằng. Chương trình GDPT 2018 và giáo trình phân tích Việt Nam trong kho chỉ dùng cân bằng khối lượng và điện tích riêng lẻ, không hệ thống hoá điều kiện proton.

<sub>`chemistry.thpt.icho-can-bang.dieu-kien-proton` · lớp 10, 11, 12 · #icho #can-bang #dieu-kien-proton #phan-tich</sub>

---

**Phương trình bậc ba chính xác tính nồng độ H+ của axit yếu đơn chức** — *Exact cubic equation for the hydrogen ion concentration of a weak monoprotic acid*

$$[\mathrm{H}^{+}]^{3}+K_{a}[\mathrm{H}^{+}]^{2}-\left(K_{a}C+K_{w}\right)[\mathrm{H}^{+}]-K_{a}K_{w}=0$$

Trong đó: `[\mathrm{H}^{+}]` là nồng độ cân bằng của ion hiđro (mol/L); `K_{a}` là hằng số phân li axit (mol/L); `K_{w}` là tích số ion của nước (mol^2/L^2); `C` là nồng độ ban đầu (nồng độ phân tích) của axit (mol/L).

*Điều kiện:* Suy ra từ ba điều kiện đồng thời: cân bằng khối lượng, cân bằng điện tích và các biểu thức hằng số cân bằng. Không dùng bất kì phép gần đúng nào. Kw = 1,0e-14 mol^2/L^2 ở 25 độ C

*Ghi chú:* IChO thường yêu cầu giải chính xác khi axit rất loãng hoặc rất yếu, lúc đó công thức gần đúng căn(Ka*C) sai lệch lớn. Kho Việt Nam có công thức pH của axit yếu dạng gần đúng; ở đây bổ sung phương trình chính xác và cơ sở suy ra nó.

<sub>`chemistry.thpt.icho-can-bang.phuong-trinh-chinh-xac-ph-axit-yeu` · lớp 10, 11, 12 · #icho #can-bang #ph #chinh-xac</sub>

---

**Tiêu chuẩn áp dụng phép gần đúng khi tính pH** — *Validity criteria for approximations in pH calculations*

$$K_{a}C \ge 10\,K_{w}\;\; \text{(bỏ qua nước)},\qquad \frac{C}{K_{a}} \ge 100\;\; \text{(bỏ qua độ phân li)}$$

Trong đó: `K_{a}` là hằng số phân li axit (mol/L); `K_{w}` là tích số ion của nước (mol^2/L^2); `C` là nồng độ phân tích của axit (mol/L).

*Điều kiện:* Hai tiêu chuẩn độc lập nhau. Tiêu chuẩn thứ nhất cho phép bỏ qua sự phân li của nước; tiêu chuẩn thứ hai cho phép coi nồng độ axit chưa phân li bằng C, sai số khi đó dưới 5%

*Ghi chú:* IChO chấm cả việc thí sinh có kiểm tra điều kiện áp dụng gần đúng hay không. Kho Việt Nam có quy tắc kiểm tra 5% cho bảng ICE ở phần cân bằng quốc tế nhưng không nêu tiêu chuẩn bỏ qua sự phân li của nước.

<sub>`chemistry.thpt.icho-can-bang.tieu-chuan-xap-xi-ph` · lớp 10, 11, 12 · #icho #can-bang #gan-dung #ph</sub>

---

**Tổ hợp thế điện cực trên giản đồ Latimer** — *Combining standard potentials on a Latimer diagram*

$$E^{\circ}_{\mathrm{tong}}=\frac{\sum_{i} n_{i}E^{\circ}_{i}}{\sum_{i} n_{i}}$$

Trong đó: `E^{\circ}_{\mathrm{tong}}` là thế điện cực chuẩn của quá trình tổng hợp (V); `n_{i}` là số electron trao đổi ở bước thứ i (); `E^{\circ}_{i}` là thế điện cực chuẩn của bước thứ i (V); `i` là chỉ số bước trong giản đồ Latimer.

*Điều kiện:* Chỉ tổ hợp được các bước NỐI TIẾP nhau trong cùng một giản đồ. Cơ sở là tính cộng được của năng lượng Gibbs (delta G = -nFE), KHÔNG phải tính cộng được của thế điện cực

*Ghi chú:* Giản đồ Latimer và Frost là công cụ chuẩn của IChO khi khảo sát tính bền và sự dị phân của các trạng thái oxi hoá. Kho Việt Nam có phương trình Nernst và cách tính hằng số cân bằng từ sức điện động nhưng không có quy tắc tổ hợp thế trên giản đồ Latimer.

<sub>`chemistry.thpt.icho-can-bang.so-do-latimer` · lớp 10, 11, 12 · #icho #dien-hoa #latimer #the-dien-cuc</sub>

---

### Olympiad Hoá học: Hoá lượng tử và nhiệt động thống kê (IChO)

**Mô hình electron tự do (FEMO) cho bước sóng hấp thụ của polyen liên hợp** — *Free-electron (FEMO) model for the absorption maximum of a conjugated polyene*

$$\Delta E=E_{n_{H}+1}-E_{n_{H}}=\frac{h^{2}\left(N_{\pi}+1\right)}{8m_{e}L^{2}},\qquad \lambda_{\max}=\frac{hc}{\Delta E}=\frac{8m_{e}cL^{2}}{h\left(N_{\pi}+1\right)}$$

Trong đó: `\Delta E` là hiệu năng lượng giữa HOMO và LUMO của hệ pi (J); `E_{n_{H}}` là năng lượng của obitan bị chiếm cao nhất (HOMO) (J); `E_{n_{H}+1}` là năng lượng của obitan trống thấp nhất (LUMO) (J); `n_{H}` là số lượng tử của HOMO, bằng N_pi/2 (); `N_{\pi}` là số electron pi (chẵn) trong mạch liên hợp (); `h` là hằng số Planck (J*s); `m_{e}` là khối lượng electron (kg); `L` là chiều dài hiệu dụng của hộp thế, lấy bằng chiều dài mạch liên hợp (m); `c` là tốc độ ánh sáng trong chân không (m/s); `\lambda_{\max}` là bước sóng hấp thụ cực đại (m).

*Điều kiện:* Suy ra từ mức năng lượng của hạt trong hộp thế một chiều thành cao vô hạn E_n = n^2*h^2/(8*m*L^2), áp dụng nguyên lí Pauli: N_pi electron lấp đầy N_pi/2 obitan thấp nhất. Hằng số: h = 6,62607015e-34 J.s (chính xác theo định nghĩa SI 2019); m_e = 9,1093837015e-31 kg; c = 2,99792458e8 m/s (chính xác). Mô hình dự đoán đúng xu hướng lambda_max tăng theo L^2 nhưng sai lệch định lượng vì thế không thực sự phẳng

*Ghi chú:* Đây là bài toán ước lượng màu của polyen liên hợp và phẩm nhuộm cyanin - dạng bài kinh điển của IChO. Kho đã có nghiệm mức năng lượng của hộp thế một chiều (chemistry.dai-hoc.hoa-luong-tu.hat-trong-hop-1d-muc-nang-luong và bản vật lí dạng giếng thế sâu vô hạn); bản ghi này KHÔNG lặp lại mức E_n mà bổ sung bước áp dụng cho chuyển dời HOMO-LUMO và công thức lambda_max theo số electron pi. Không có trong chương trình GDPT 2018.

<sub>`chemistry.thpt.icho-luong-tu.mo-hinh-electron-tu-do-polyen` · lớp 10, 11, 12 · #icho #luong-tu #hop-the #polyen</sub>

---

**Tỉ số phân bố Boltzmann có kể độ suy biến** — *Boltzmann population ratio including degeneracy*

$$\frac{n_{i}}{n_{j}}=\frac{g_{i}}{g_{j}}\exp\left(-\frac{E_{i}-E_{j}}{k_{B}T}\right)$$

Trong đó: `n_{i}` là số phân tử ở mức năng lượng thứ i (); `n_{j}` là số phân tử ở mức năng lượng thứ j (); `g_{i}` là độ suy biến của mức thứ i (); `g_{j}` là độ suy biến của mức thứ j (); `E_{i}` là năng lượng của mức thứ i (J); `E_{j}` là năng lượng của mức thứ j (J); `k_{B}` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Hệ ở cân bằng nhiệt tại nhiệt độ T. Hằng số Boltzmann k_B = 1,380649e-23 J/K (giá trị chính xác theo định nghĩa SI 2019)

*Ghi chú:* IChO dùng tỉ số Boltzmann có suy biến khi phân tích phổ quay - dao động và cường độ vạch phổ. Kho Việt Nam có thừa số Boltzmann dạng đơn giản (tỉ lệ phân tử vượt năng lượng hoạt hoá) nhưng không kể độ suy biến của mức.

<sub>`chemistry.thpt.icho-luong-tu.ti-so-boltzmann-co-suy-bien` · lớp 10, 11, 12 · #icho #nhiet-dong-thong-ke #boltzmann #suy-bien</sub>

---

### Olympiad Hoá học: Tinh thể học (IChO)

**Khoảng cách giữa hai mặt mạng liên tiếp trong tinh thể lập phương** — *Interplanar spacing for a cubic lattice*

$$d_{hkl}=\frac{a}{\sqrt{h^{2}+k^{2}+l^{2}}}$$

Trong đó: `d_{hkl}` là khoảng cách giữa hai mặt mạng liên tiếp có chỉ số Miller (hkl) (m); `a` là hằng số mạng của ô cơ sở lập phương (m); `h` là chỉ số Miller thứ nhất (); `k` là chỉ số Miller thứ hai (); `l` là chỉ số Miller thứ ba ().

*Điều kiện:* Chỉ đúng cho hệ tinh thể lập phương. Kết hợp với định luật Bragg để quy các vạch nhiễu xạ về chỉ số Miller

*Ghi chú:* Việc quy kết các vạch nhiễu xạ tia X (indexing) là dạng bài quen thuộc của IChO tinh thể học. Kho Việt Nam có định luật Bragg và bảy hệ tinh thể nhưng không có công thức khoảng cách mặt mạng theo chỉ số Miller.

<sub>`chemistry.thpt.icho-tinh-the.khoang-cach-mat-mang-lap-phuong` · lớp 10, 11, 12 · #icho #tinh-the #miller #nhieu-xa</sub>

---

**Bán kính lớn nhất của ion lọt vào hốc bát diện và hốc tứ diện** — *Maximum radius of an ion fitting an octahedral or tetrahedral hole*

$$\frac{r_{\mathrm{oct}}}{R}=\sqrt{2}-1\approx 0{,}414,\qquad \frac{r_{\mathrm{tet}}}{R}=\sqrt{\frac{3}{2}}-1\approx 0{,}225$$

Trong đó: `r_{\mathrm{oct}}` là bán kính lớn nhất của quả cầu lọt vừa hốc bát diện (m); `r_{\mathrm{tet}}` là bán kính lớn nhất của quả cầu lọt vừa hốc tứ diện (m); `R` là bán kính của các quả cầu xếp chặt tạo nên mạng (m).

*Điều kiện:* Mô hình quả cầu cứng xếp chặt (lập phương tâm mặt hoặc lục phương xếp chặt). Trong một ô xếp chặt gồm N quả cầu có N hốc bát diện và 2N hốc tứ diện

*Ghi chú:* Các giá trị 0,414 và 0,225 là mốc phân loại kiểu cấu trúc tinh thể ion trong đề IChO. Kho Việt Nam có bảng tỉ số bán kính - số phối trí nhưng không có phần dẫn xuất bán kính hốc và số lượng hốc trong ô xếp chặt.

<sub>`chemistry.thpt.icho-tinh-the.ban-kinh-hoc-trong-tinh-the` · lớp 10, 11, 12 · #icho #tinh-the #hoc-bat-dien #xep-chat</sub>

---

### Phương pháp phổ và phân tích công cụ

**Độ dịch chuyển hoá học trong phổ NMR proton** — *Chemical shift in proton NMR*

$$\delta = \dfrac{\nu_{mau} - \nu_{TMS}}{\nu_{may}} \times 10^{6}$$

Trong đó: `\delta` là độ dịch chuyển hoá học, tính bằng phần triệu (ppm) (); `\nu_{mau}` là tần số cộng hưởng của proton trong mẫu (Hz); `\nu_{TMS}` là tần số cộng hưởng của proton trong chất chuẩn tetramethylsilane (Hz); `\nu_{may}` là tần số làm việc của máy phổ (MHz).

*Điều kiện:* TMS được chọn làm gốc với delta = 0 vì trơ, dễ bay hơi và cho một tín hiệu duy nhất ở vùng rất cao trường

*Ghi chú:* IB Structure 3.2 (mục 21 Data Booklet) và A-Level. Giá trị tham chiếu: CH3 khoảng 0,9 - 1,0; CH2 cạnh halogen 3,5 - 4,4; H của aldehyde 9,4 - 10,0; H của nhóm COOH 9,0 - 13,0 ppm. Chia cho tần số máy nên delta KHÔNG phụ thuộc từ trường của máy. CT GDPT 2018 Việt Nam không dạy phổ NMR.

<sub>`chemistry.thpt.pho-phan-tich.do-dich-chuyen-hoa-hoc-nmr` · lớp 10, 11, 12 · #ib #a-level #nmr #do-dich-chuyen</sub>

---

**Quy tắc n + 1 về sự tách tín hiệu trong phổ NMR** — *The n + 1 splitting rule in proton NMR*

$$S = n + 1$$

Trong đó: `S` là số vạch (bội) của một tín hiệu cộng hưởng (); `n` là số proton tương đương trên các nguyên tử carbon LIỀN KỀ ().

*Điều kiện:* Chỉ áp dụng cho phổ NMR proton phân giải cao; proton của nhóm OH và NH thường không tách do trao đổi nhanh

*Ghi chú:* Nội dung bắt buộc của A-Level: Cambridge 9701 yêu cầu suy số proton kề bên 'using the n + 1 rule (limited to singlet, doublet, triplet, quartet)'; AQA và Edexcel tương tự; IB HL Structure 3.2 cũng có. Ví dụ: nhóm CH3 cạnh CH2 cho tín hiệu ba vạch (triplet), nhóm CH2 cạnh CH3 cho tín hiệu bốn vạch (quartet). Proton của nhóm OH và NH thường không tách do trao đổi nhanh. CT GDPT 2018 Việt Nam không dạy quy tắc này.

<sub>`chemistry.thpt.pho-phan-tich.quy-tac-n-cong-1` · lớp 10, 11, 12 · #a-level #ib-hl #nmr #tach-tin-hieu</sub>

---

**Tích phân tín hiệu NMR và tỉ lệ số proton** — *NMR integration and the ratio of protons*

$$\dfrac{S_{1}}{S_{2}} = \dfrac{N_{1}}{N_{2}}$$

Trong đó: `S_{1}` là diện tích (giá trị tích phân) của tín hiệu thứ nhất; `S_{2}` là diện tích của tín hiệu thứ hai; `N_{1}` là số proton tương đương gây ra tín hiệu thứ nhất (); `N_{2}` là số proton tương đương gây ra tín hiệu thứ hai ().

*Điều kiện:* Tích phân chỉ cho TỈ LỆ chứ không cho số tuyệt đối; phải kết hợp với công thức phân tử để suy ra số proton thật

*Ghi chú:* A-Level và IB Structure 3.2. Kết hợp ba dữ kiện của phổ NMR proton: số tín hiệu cho số loại proton, độ dịch chuyển cho môi trường hoá học, tích phân cho tỉ lệ số proton và quy tắc n+1 cho số proton kề bên. CT GDPT 2018 Việt Nam không dạy nội dung này.

<sub>`chemistry.thpt.pho-phan-tich.tich-phan-nmr` · lớp 10, 11, 12 · #a-level #ib #nmr #tich-phan</sub>

---

**Các vùng hấp thụ đặc trưng trên phổ hồng ngoại** — *Characteristic infrared absorption regions*

$$\tilde{\nu} = \dfrac{1}{\lambda}: \ \mathrm{O\!-\!H}\ 3200\text{--}3600; \ \mathrm{N\!-\!H}\ 3300\text{--}3500; \ \mathrm{C\!-\!H}\ 2850\text{--}3090; \ \mathrm{C\!\equiv\!C}\ 2100\text{--}2260; \ \mathrm{C\!=\!O}\ 1700\text{--}1750; \ \mathrm{C\!=\!C}\ 1620\text{--}1680$$

Trong đó: `\tilde{\nu}` là số sóng, nghịch đảo của bước sóng, là đại lượng ghi trên trục hoành của phổ IR (1/cm); `\lambda` là bước sóng của bức xạ hồng ngoại (cm).

*Điều kiện:* Các khoảng số sóng tính bằng cm^-1 theo mục 20 Chemistry Data Booklet của IB; O-H của acid carboxylic có liên kết hydrogen nằm thấp hơn, ở 2500 - 3000 cm^-1 và rất tù

*Ghi chú:* IB Structure 3.2 và A-Level yêu cầu nhận diện nhóm chức từ phổ IR. Vùng dưới 1500 cm^-1 là vùng vân tay (fingerprint), dùng để đối chiếu với phổ chuẩn chứ không gán cho một nhóm chức cụ thể. CT GDPT 2018 Việt Nam có giới thiệu phổ IR nhưng bảng số sóng không chi tiết như Data Booklet quốc tế.

<sub>`chemistry.thpt.pho-phan-tich.vung-hap-thu-ir` · lớp 10, 11, 12 · #ib #a-level #pho-ir #nhom-chuc</sub>

---

**Các mảnh trung hoà thường bị mất trong phổ khối lượng** — *Common neutral fragments lost in a mass spectrum*

$$\Delta\!\left( \dfrac{m}{z} \right) \in \{15, 17, 18, 28, 29, 31, 45\}$$

Trong đó: `\Delta\!\left( \dfrac{m}{z} \right)` là hiệu giữa m/z của ion phân tử và m/z của pic mảnh, bằng khối lượng của mảnh trung hoà bị mất.

*Điều kiện:* Áp dụng cho phổ khối lượng va chạm electron của hợp chất hữu cơ

*Ghi chú:* Bảng mục 22 Chemistry Data Booklet của IB: mất 15 là gốc CH3, 17 là gốc OH, 18 là H2O, 28 là CH2=CH2 hoặc CO, 29 là gốc C2H5 hoặc CHO, 31 là gốc OCH3 hoặc CH2OH, 45 là gốc COOH. Đây là công cụ suy cấu tạo của IB Structure 3.2 và A-Level; CT GDPT 2018 Việt Nam không có bảng này.

<sub>`chemistry.thpt.pho-phan-tich.manh-mat-pho-khoi` · lớp 10, 11, 12 · #ib #a-level #pho-khoi #phan-manh</sub>

---

**Pic ion phân tử và phân tử khối** — *Molecular ion peak and relative molecular mass*

$$M^{+\bullet}: \ \dfrac{m}{z} = M_{r} \ \ (z = 1)$$

Trong đó: `M^{+\bullet}` là ion phân tử, tạo ra khi phân tử mất đúng một electron; `m` là khối lượng của ion (u); `z` là điện tích của ion, hầu như luôn bằng 1 trong phổ khối lượng hữu cơ (); `M_{r}` là phân tử khối của chất ().

*Điều kiện:* Pic ion phân tử là pic có m/z lớn nhất, không kể các pic đồng vị M+1 và M+2

*Ghi chú:* Cambridge 9701 mục 22.2 yêu cầu 'deduce the molecular mass of an organic molecule from the molecular ion peak in a mass spectrum' và 'analyse mass spectra in terms of m/e values and isotopic abundances'; IB Structure 3.2 (mục 22 Data Booklet) tương tự. Khác biệt kí hiệu: CIE viết m/e, IB và sách Mỹ viết m/z. Chú ý: hợp chất dễ phân mảnh có thể có pic ion phân tử rất yếu hoặc không thấy. CT GDPT 2018 Việt Nam có giới thiệu phổ khối lượng để xác định phân tử khối nhưng không khai thác phân mảnh.

<sub>`chemistry.thpt.pho-phan-tich.pic-ion-phan-tu` · lớp 10, 11, 12 · #ib #a-level #pho-khoi #ion-phan-tu</sub>

---

**Dùng pic M+1 để đếm số nguyên tử carbon** — *Counting carbon atoms from the M+1 peak*

$$n_{C} = \dfrac{100}{1.1} \times \dfrac{h_{M+1}}{h_{M}}$$

Trong đó: `n_{C}` là số nguyên tử carbon trong phân tử (); `h_{M+1}` là chiều cao (độ lớn tương đối) của pic M+1; `h_{M}` là chiều cao của pic ion phân tử M.

*Điều kiện:* Giả thiết mọi pic M+1 đều do đồng vị carbon-13 gây ra; độ phổ biến tự nhiên của carbon-13 lấy bằng 1,1%

*Ghi chú:* Công thức riêng của A-Level (Edexcel Topic 7, CIE 9701 mục 22). Vì carbon-13 chiếm khoảng 1,1% nên phân tử càng nhiều carbon thì pic M+1 càng cao. CT GDPT 2018 Việt Nam không có nội dung này.

<sub>`chemistry.thpt.pho-phan-tich.pic-m-cong-1-so-carbon` · lớp 10, 11, 12 · #a-level #pho-khoi #dong-vi #m-cong-1</sub>

---

**Nhận biết chlorine và bromine qua pic M+2** — *Identifying chlorine and bromine from the M+2 peak*

$$\dfrac{h_{M}}{h_{M+2}} = \begin{cases} 3 : 1 & \text{co mot nguyen tu } \mathrm{Cl} \\ 1 : 1 & \text{co mot nguyen tu } \mathrm{Br} \end{cases}$$

Trong đó: `h_{M}` là chiều cao của pic ion phân tử M; `h_{M+2}` là chiều cao của pic M+2.

*Điều kiện:* Chlorine có hai đồng vị 35Cl và 37Cl theo tỉ lệ khoảng 3:1; bromine có 79Br và 81Br theo tỉ lệ khoảng 1:1

*Ghi chú:* Nội dung bắt buộc của A-Level (CIE 9701 mục 22, Edexcel) và có trong IB Structure 3.2. Với hai nguyên tử chlorine thì tỉ lệ M : M+2 : M+4 là 9 : 6 : 1. CT GDPT 2018 Việt Nam không có nội dung này.

<sub>`chemistry.thpt.pho-phan-tich.pic-m-cong-2-clo-brom` · lớp 10, 11, 12 · #a-level #ib #pho-khoi #dong-vi</sub>

---

**Định luật Beer - Lambert** — *Beer - Lambert law*

$$A = \varepsilon\, b\, c$$

Trong đó: `A` là độ hấp thụ (không thứ nguyên) (); `\varepsilon` là hệ số hấp thụ mol của chất tan tại bước sóng khảo sát (L/(mol*cm)); `b` là chiều dày lớp dung dịch mà ánh sáng đi qua (bề dày cuvet) (cm); `c` là nồng độ mol của chất hấp thụ (mol/L).

*Điều kiện:* Ánh sáng đơn sắc, dung dịch loãng và đồng nhất, không có phản ứng hoặc kết tụ làm đổi dạng chất hấp thụ

*Ghi chú:* In sẵn trên bảng công thức kì thi AP Chemistry dưới dạng 'A = epsilon.b.c' (mục Gases, Liquids, and Solutions) và là một topic riêng của AP: Topic 3.13 Beer-Lambert Law. A-Level (AQA, Edexcel) dùng trong phép so màu để lập đường chuẩn. Với IB thì định luật này thuộc kĩ năng thực hành và bài IA chứ KHÔNG được in trong Chemistry Data Booklet 2025 (mục 1 của Data Booklet không có Beer - Lambert). Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam không có định luật này ở THPT.

<sub>`chemistry.thpt.pho-phan-tich.dinh-luat-beer-lambert` · lớp 10, 11, 12 · #ap #a-level #beer-lambert #so-mau</sub>

---

**Quan hệ giữa độ hấp thụ và độ truyền qua** — *Relation between absorbance and transmittance*

$$A = -\log_{10} T = \log_{10}\dfrac{I_{0}}{I}, \qquad T = \dfrac{I}{I_{0}}$$

Trong đó: `A` là độ hấp thụ (); `T` là độ truyền qua, thường biểu diễn dưới dạng phần trăm (); `I_{0}` là cường độ chùm sáng tới (W/m^2); `I` là cường độ chùm sáng ló ra khỏi dung dịch (W/m^2).

*Điều kiện:* Cùng bước sóng và cùng cuvet cho cả hai phép đo

*Ghi chú:* Máy so màu trong thí nghiệm A-Level và IB IA thường hiển thị phần trăm truyền qua, học sinh phải đổi sang độ hấp thụ mới dùng được Beer - Lambert vì chỉ A mới tỉ lệ thuận với nồng độ. CT GDPT 2018 Việt Nam không có nội dung này.

<sub>`chemistry.thpt.pho-phan-tich.do-hap-thu-va-do-truyen-qua` · lớp 10, 11, 12 · #a-level #ib #do-truyen-qua #so-mau</sub>

---

**Hệ số lưu giữ Rf trong sắc kí giấy và sắc kí lớp mỏng** — *Retardation factor Rf in paper and thin-layer chromatography*

$$R_{f} = \dfrac{d_{chat}}{d_{dung\ moi}}$$

Trong đó: `R_{f}` là hệ số lưu giữ, luôn nằm giữa 0 và 1 (); `d_{chat}` là quãng đường tâm vết chất di chuyển được, tính từ vạch xuất phát (cm); `d_{dung\ moi}` là quãng đường mặt dung môi di chuyển được, tính từ vạch xuất phát (cm).

*Điều kiện:* Cùng một hệ pha tĩnh - pha động, cùng nhiệt độ; chất nào ái lực với pha động lớn hơn thì Rf lớn hơn

*Ghi chú:* A-Level (AQA, Edexcel: sắc kí lớp mỏng và sắc kí giấy trong phân tích amino acid, chất màu) dùng Rf để nhận danh chất bằng cách đối chiếu với giá trị chuẩn đo trong cùng hệ dung môi. CT GDPT 2018 Việt Nam có giới thiệu sắc kí nhưng không đưa công thức Rf thành nội dung tính toán.

<sub>`chemistry.thpt.pho-phan-tich.he-so-luu-giu-rf` · lớp 10, 11, 12 · #a-level #sac-ki #rf #phan-tich</sub>

---

### Phản ứng oxi hóa - khử

**Điều kiện cân bằng điện tích của nửa phản ứng** — *Charge balance condition for a half-reaction*

$$\sum q_{\text{ve trai}} = \sum q_{\text{ve phai}}$$

Trong đó: `q_{\text{ve trai}}` là tổng điện tích các tiểu phân ở vế trái; `q_{\text{ve phai}}` là tổng điện tích các tiểu phân ở vế phải.

*Điều kiện:* Áp dụng cho mỗi nửa phản ứng và cho phương trình ion rút gọn

*Ghi chú:* Kiểm tra đồng thời hai điều kiện: bảo toàn nguyên tố và bảo toàn điện tích.

<sub>`chemistry.thpt.oxi-hoa-khu.can-bang-dien-tich-nua-phan-ung` · lớp 10, 11, 12 · #ion-electron #bao-toan-dien-tich #can-bang-phuong-trinh</sub>

---

**Phương pháp ion - electron (nửa phản ứng) trong môi trường acid** — *Half-reaction (ion-electron) method in acidic medium*

$$\mathrm{MnO_{4}^{-}} + 8\mathrm{H^{+}} + 5e \rightarrow \mathrm{Mn^{2+}} + 4\mathrm{H_{2}O}$$

Trong đó: `\mathrm{MnO_{4}^{-}}` là ion permanganate (chất oxi hóa); `\mathrm{H^{+}}` là ion hiđro của môi trường acid; `e` là electron; `\mathrm{Mn^{2+}}` là ion manganese(II) sản phẩm khử; `\mathrm{H_{2}O}` là phân tử nước dùng để cân bằng nguyên tố oxi.

*Điều kiện:* Phản ứng trong dung dịch; môi trường acid dùng H+ và H2O để cân bằng O và H

*Ghi chú:* Quy tắc: thiếu O thì thêm H2O ở vế thiếu và H+ ở vế kia (môi trường acid); trong môi trường base dùng OH- và H2O. Cân bằng điện tích hai vế bằng cách thêm electron.

<sub>`chemistry.thpt.oxi-hoa-khu.phuong-phap-ion-electron` · lớp 10, 11, 12 · #ion-electron #nua-phan-ung #oxi-hoa-khu</sub>

---

**Số mol electron trao đổi của một chất** — *Moles of electrons transferred by a species*

$$n_{e} = n_{\text{chat}} \cdot \left| \Delta \text{SOH} \right| \cdot k$$

Trong đó: `n_{e}` là số mol electron nhường hoặc nhận (mol); `n_{\text{chat}}` là số mol chất tham gia (mol); `\Delta \text{SOH}` là độ biến thiên số oxi hóa của nguyên tố; `k` là số nguyên tử của nguyên tố đó trong một phân tử chất.

*Điều kiện:* Nguyên tố có thay đổi số oxi hóa

*Ghi chú:* Ví dụ 1 mol Al nhường 3 mol electron; 1 mol N trong HNO3 tạo NO nhận 3 mol electron, tạo NO2 nhận 1 mol electron.

<sub>`chemistry.thpt.oxi-hoa-khu.so-mol-electron-trao-doi` · lớp 10, 11, 12 · #oxi-hoa-khu #bao-toan-electron #tinh-toan</sub>

---

**Phương pháp thăng bằng electron** — *Oxidation number (electron balance) method*

$$a \times \left( \mathrm{X}^{x_{1}} \rightarrow \mathrm{X}^{x_{2}} + p e \right), \quad b \times \left( \mathrm{Y}^{y_{1}} + q e \rightarrow \mathrm{Y}^{y_{2}} \right), \quad a\,p = b\,q$$

Trong đó: `a` là hệ số của quá trình oxi hóa; `b` là hệ số của quá trình khử; `p` là số electron nhường của một nguyên tử chất khử; `q` là số electron nhận của một nguyên tử chất oxi hóa; `x_{1}` là số oxi hóa của nguyên tố X trước và sau phản ứng; `x_{2}` là số oxi hóa của nguyên tố X trước và sau phản ứng; `y_{1}` là số oxi hóa của nguyên tố Y trước và sau phản ứng; `y_{2}` là số oxi hóa của nguyên tố Y trước và sau phản ứng.

*Điều kiện:* Phản ứng oxi hóa - khử; a, b chọn là bội chung nhỏ nhất để tổng e nhường bằng tổng e nhận

*Ghi chú:* Bốn bước: xác định số oxi hóa; viết quá trình oxi hóa và quá trình khử; tìm hệ số thăng bằng electron; đặt hệ số vào phương trình và kiểm tra.

<sub>`chemistry.thpt.oxi-hoa-khu.thang-bang-electron` · lớp 10, 11, 12 · #oxi-hoa-khu #can-bang-phuong-trinh #thang-bang-electron</sub>

---

**Xác định chất khử và chất oxi hóa** — *Identifying oxidizing and reducing agents*

$$\begin{cases} \text{Chat khu}: \text{SOH tang, nhuong } e,\; \text{bi oxi hoa} \\ \text{Chat oxi hoa}: \text{SOH giam, nhan } e,\; \text{bi khu} \end{cases}$$

Trong đó: `\text{SOH}` là số oxi hóa của nguyên tố; `e` là electron.

*Điều kiện:* Phản ứng có sự thay đổi số oxi hóa của ít nhất một nguyên tố

*Ghi chú:* Mẹo nhớ: khử cho - o nhận (chất khử cho electron, chất oxi hóa nhận electron).

<sub>`chemistry.thpt.oxi-hoa-khu.chat-khu-chat-oxi-hoa` · lớp 10, 11, 12 · #oxi-hoa-khu #chat-khu #chat-oxi-hoa</sub>

---

### Xác định công thức chất vô cơ

**Xác định kim loại chưa biết dựa vào khối lượng mol** — *Identifying an unknown metal from its molar mass*

$$M = \dfrac{m_{KL}}{n_{KL}} = \dfrac{a \cdot m_{KL}}{n_e}$$

Trong đó: `M` là khối lượng mol nguyên tử của kim loại (g/mol); `m_{KL}` là khối lượng kim loại phản ứng (g); `n_{KL}` là số mol kim loại (mol); `a` là hóa trị của kim loại trong phản ứng; `n_e` là số mol electron kim loại nhường (mol).

*Điều kiện:* Kim loại tan hết; biết hóa trị hoặc phải biện luận hóa trị a = 1, 2, 3

*Ghi chú:* Với hỗn hợp hai kim loại cùng nhóm ở hai chu kì liên tiếp, dùng M trung bình rồi kẹp: M1 < M(tb) < M2.

<sub>`chemistry.thpt.xac-dinh-cong-thuc.kim-loai-chua-biet` · lớp 10, 11, 12 · #vo-co #xac-dinh-cong-thuc #bien-luan</sub>

---

**Xác định công thức muối ngậm nước** — *Determining the formula of a hydrated salt*

$$A \cdot xH_2O:\quad x = \dfrac{n_{H_2O}}{n_{A}} = \dfrac{m_{tinh\ the} - m_{khan}}{18 \, n_{A}}$$

Trong đó: `x` là số phân tử nước kết tinh; `A` là công thức muối khan; `n_{H_2O}` là số mol nước kết tinh (mol); `n_{A}` là số mol muối khan (mol); `m_{tinh\ the}` là khối lượng tinh thể ngậm nước (g); `m_{khan}` là khối lượng muối khan sau khi nung (g).

*Điều kiện:* x là số nguyên dương; nung đến khối lượng không đổi và muối khan không bị phân hủy

*Ghi chú:* Ví dụ quen thuộc: CuSO4·5H2O (M = 250), Na2CO3·10H2O (M = 286), MgSO4·7H2O (M = 246).

<sub>`chemistry.thpt.xac-dinh-cong-thuc.muoi-ngam-nuoc` · lớp 10, 11, 12 · #vo-co #xac-dinh-cong-thuc #muoi</sub>

---

**Xác định công thức oxit kim loại MxOy** — *Determining the formula of a metal oxide*

$$\dfrac{x}{y} = \dfrac{n_{M}}{n_{O}} = \dfrac{\%M / M_{M}}{\%O / 16};\quad M_{oxit} = xM_{M} + 16y$$

Trong đó: `x` là chỉ số nguyên tử kim loại trong công thức oxit; `y` là chỉ số nguyên tử oxi trong công thức oxit; `n_{M}` là số mol nguyên tử kim loại (mol); `n_{O}` là số mol nguyên tử oxi (mol); `\%M` là phần trăm khối lượng kim loại trong oxit (%); `\%O` là phần trăm khối lượng oxi trong oxit (%); `M_{M}` là khối lượng mol nguyên tử kim loại (g/mol); `M_{oxit}` là khối lượng mol phân tử oxit (g/mol).

*Điều kiện:* x, y là số nguyên dương tối giản; hóa trị kim loại là 2y/x

*Ghi chú:* Các oxit sắt thường gặp: FeO (x:y = 1:1), Fe3O4 (3:4), Fe2O3 (2:3).

<sub>`chemistry.thpt.xac-dinh-cong-thuc.oxit-kim-loai` · lớp 10, 11, 12 · #vo-co #xac-dinh-cong-thuc #oxit</sub>

---

### Điện hoá học quốc tế

**Cân bằng nửa phản ứng trong môi trường base** — *Balancing a half-reaction in basic medium*

$$a\,\mathrm{Ox} + b\,\mathrm{H_{2}O} + n e^{-} \rightleftharpoons c\,\mathrm{Red} + d\,\mathrm{OH^{-}}$$

Trong đó: `a` là hệ số của dạng oxi hoá (); `\mathrm{Ox}` là dạng oxi hoá của cặp oxi hoá - khử; `b` là số phân tử nước thêm vào để cân bằng nguyên tố oxygen và hydrogen (); `n` là số electron trao đổi trong nửa phản ứng (); `c` là hệ số của dạng khử (); `\mathrm{Red}` là dạng khử của cặp oxi hoá - khử; `d` là số ion hydroxide xuất hiện ở vế còn lại ().

*Điều kiện:* Dung dịch base; cân bằng nguyên tố bằng H2O và OH-, cân bằng điện tích bằng electron; trong môi trường base KHÔNG được để H+ trong phương trình cuối

*Ghi chú:* AP Unit 4 và IB HL Reactivity 3.2 yêu cầu cân bằng cả trong môi trường acid và base. Thủ thuật chuẩn: cân bằng như trong môi trường acid trước, sau đó thêm vào HAI VẾ số mol OH- bằng số mol H+, rồi ghép H+ với OH- thành H2O và rút gọn. Kho Việt Nam chỉ có phương pháp ion - electron trong môi trường acid.

<sub>`chemistry.thpt.dien-hoa-quoc-te.can-bang-oxi-hoa-khu-moi-truong-kiem` · lớp 10, 11, 12 · #ap #ib-hl #oxi-hoa-khu #moi-truong-base</sub>

---

**Sơ đồ pin theo quy ước IUPAC và sức điện động** — *IUPAC cell diagram notation and cell potential*

$$\mathrm{Zn}(s)\,|\,\mathrm{Zn^{2+}}(aq)\,\|\,\mathrm{Cu^{2+}}(aq)\,|\,\mathrm{Cu}(s), \qquad E^{\ominus}_{pin} = E^{\ominus}_{phai} - E^{\ominus}_{trai}$$

Trong đó: `E^{\ominus}_{pin}` là sức điện động chuẩn của pin (V); `E^{\ominus}_{phai}` là thế khử chuẩn của nửa pin viết bên PHẢI sơ đồ (nơi xảy ra sự khử, cathode) (V); `E^{\ominus}_{trai}` là thế khử chuẩn của nửa pin viết bên TRÁI sơ đồ (nơi xảy ra sự oxi hoá, anode) (V).

*Điều kiện:* Một gạch đứng là ranh giới hai pha, hai gạch đứng là cầu muối; theo quy ước IUPAC anode luôn viết bên trái

*Ghi chú:* Quy ước kí hiệu pin của IUPAC là nội dung bắt buộc của A-Level (CIE 9701, Edexcel) và IB HL; AP dùng cách gọi cathode - anode. Điểm khác so với CT GDPT 2018 Việt Nam: Việt Nam viết E(pin) = E(cực dương) - E(cực âm) mà không dùng sơ đồ pin, nên học sinh dễ nhầm khi gặp đề quốc tế cho sẵn sơ đồ.

<sub>`chemistry.thpt.dien-hoa-quoc-te.so-do-pin-iupac` · lớp 10, 11, 12 · #a-level #ib-hl #so-do-pin #iupac</sub>

---

**Pin nhiên liệu hydrogen - oxygen** — *Hydrogen - oxygen fuel cell*

$$2\mathrm{H_{2}}(g) + \mathrm{O_{2}}(g) \rightarrow 2\mathrm{H_{2}O}(l), \qquad E^{\ominus}_{pin} = 1.23\ \mathrm{V}$$

Trong đó: `E^{\ominus}_{pin}` là sức điện động chuẩn của pin nhiên liệu hydrogen - oxygen ở 298 K (V).

*Điều kiện:* Điều kiện chuẩn, môi trường acid hoặc base tuỳ loại màng; chất phản ứng được cấp liên tục nên pin không tự cạn

*Ghi chú:* Nội dung bắt buộc của A-Level (AQA, CIE) và IB (Reactivity 3.2): viết nửa phản ứng ở cả môi trường acid và base, so sánh pin nhiên liệu với pin thường và với động cơ đốt trong. Giá trị 1,23 V bằng hiệu thế khử chuẩn của cặp O2/H2O (+1,23 V) và cặp H+/H2 (0,00 V). CT GDPT 2018 Việt Nam chỉ nhắc pin nhiên liệu ở mức giới thiệu.

<sub>`chemistry.thpt.dien-hoa-quoc-te.pin-nhien-lieu-hidro` · lớp 10, 11, 12 · #a-level #ib #pin-nhien-lieu #dien-hoa</sub>

---

**So sánh dấu điện cực trong pin Galvani và bình điện phân** — *Electrode signs in galvanic versus electrolytic cells*

$$\begin{cases} \text{pin Galvani} & \text{anode}\ (-),\ \text{cathode}\ (+),\ E_{pin} > 0 \\ \text{binh dien phan} & \text{anode}\ (+),\ \text{cathode}\ (-),\ E_{ap} > \left| E_{pin} \right| \end{cases}$$

Trong đó: `E_{pin}` là sức điện động của phản ứng xảy ra trong pin (V); `E_{ap}` là hiệu điện thế ngoài áp vào bình điện phân (V).

*Điều kiện:* Trong cả hai loại, oxi hoá luôn xảy ra ở anode và khử luôn xảy ra ở cathode; chỉ DẤU của điện cực đảo lại

*Ghi chú:* A-Level (Cambridge 9701 mục 24, Edexcel) và IB Reactivity 3.2 yêu cầu xác định dấu điện cực trong pin Galvani và trong bình điện phân; đây là lỗi sai phổ biến nhất của học sinh. KHÔNG được gán cho AP: CED của AP Chemistry có exclusion statement 'Labeling an electrode as positive or negative will not be assessed on the AP Exam' - AP chỉ dùng cặp thuật ngữ anode/cathode. Trong cả hai loại, oxi hoá luôn xảy ra ở anode và khử luôn xảy ra ở cathode; chỉ DẤU của điện cực đảo lại. CT GDPT 2018 Việt Nam nêu quy ước cho pin Galvani nhưng không nhấn mạnh sự đảo dấu khi chuyển sang bình điện phân.

<sub>`chemistry.thpt.dien-hoa-quoc-te.so-sanh-pin-galvani-va-binh-dien-phan` · lớp 10, 11, 12 · #a-level #ib #dien-phan #pin-galvani</sub>

---

**Sức điện động của pin nồng độ** — *Electromotive force of a concentration cell*

$$E_{pin} = \dfrac{0.0592}{n} \log \dfrac{c_{dac}}{c_{loang}}$$

Trong đó: `E_{pin}` là sức điện động của pin nồng độ (V); `n` là số electron trao đổi trong phản ứng nửa pin (); `c_{dac}` là nồng độ ion kim loại ở nửa pin đặc hơn, đóng vai trò cathode (mol/L); `c_{loang}` là nồng độ ion kim loại ở nửa pin loãng hơn, đóng vai trò anode (mol/L).

*Điều kiện:* Hai nửa pin cùng cặp oxi hoá - khử nên E chuẩn của pin bằng 0; nhiệt độ 25 độ C

*Ghi chú:* Cambridge 9701 mục 24.2 yêu cầu 'use the Nernst equation, e.g. E = E(chuẩn) + (0,059/z) log([oxidised species]/[reduced species])' - chú ý A-Level dùng hệ số 0,059 và kí hiệu z cho số electron, còn sách Mỹ dùng 0,0592 và kí hiệu n. Pin nồng độ là trường hợp đặc biệt: hai nửa pin cùng cặp oxi hoá - khử nên E chuẩn của pin bằng 0, pin ngừng hoạt động khi hai nồng độ bằng nhau. KHÔNG gán cho AP ở mức định lượng: CED của AP (mục 9.10.A.4) ghi rõ 'Algorithmic calculations using the Nernst equation are insufficient... students should qualitatively understand the effects of concentration on cell potential', tức AP chỉ đòi hỏi lập luận định tính. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam có phương trình Nernst nhưng không có dạng pin nồng độ.

<sub>`chemistry.thpt.dien-hoa-quoc-te.pin-nong-do` · lớp 10, 11, 12 · #a-level #pin-nong-do #nernst #dien-hoa</sub>

---

**Điện cực hydrogen chuẩn và mốc quy ước của thang thế** — *Standard hydrogen electrode as the zero of the potential scale*

$$2\mathrm{H^{+}}(aq,\ 1\ \mathrm{mol\,dm^{-3}}) + 2e^{-} \rightleftharpoons \mathrm{H_{2}}(g,\ 100\ \mathrm{kPa}), \qquad E^{\ominus} = 0.00\ \mathrm{V}$$

Trong đó: `E^{\ominus}` là thế khử chuẩn của cặp H+/H2, được quy ước bằng đúng 0 vôn (V).

*Điều kiện:* Nồng độ H+ bằng 1 mol/dm^3, áp suất H2 bằng 100 kPa, nhiệt độ 298 K, điện cực platinum phủ muội platinum

*Ghi chú:* A-Level (CIE 9701, AQA) yêu cầu mô tả chi tiết cấu tạo và điều kiện của điện cực hydrogen chuẩn, và giải thích rằng mọi thế khử chuẩn đều là giá trị TƯƠNG ĐỐI so với mốc này. CT GDPT 2018 Việt Nam cho sẵn bảng thế điện cực chuẩn nhưng không yêu cầu mô tả điện cực chuẩn.

<sub>`chemistry.thpt.dien-hoa-quoc-te.dien-cuc-hidro-chuan` · lớp 10, 11, 12 · #a-level #ib-hl #the-dien-cuc-chuan #she</sub>

---

### Đại cương

**Hiệu suất phản ứng** — *Reaction yield*

$$H = \dfrac{m_{tt}}{m_{lt}} \times 100\% = \dfrac{n_{pu}}{n_{bd}} \times 100\%$$

Trong đó: `H` là hiệu suất phản ứng (%); `m_{tt}` là khối lượng sản phẩm thực tế thu được (g); `m_{lt}` là khối lượng sản phẩm tính theo lí thuyết (g); `n_{pu}` là số mol chất thiếu đã phản ứng (mol); `n_{bd}` là số mol chất thiếu ban đầu (mol).

*Điều kiện:* 0 < H ≤ 100%; tính theo chất phản ứng hết trước

*Ghi chú:* Qua n giai đoạn nối tiếp: H(tổng) = H1·H2·...·Hn (dạng thập phân).

<sub>`chemistry.thpt.dai-cuong.hieu-suat-phan-ung` · lớp 10, 11, 12 · #dai-cuong #hieu-suat #giai-nhanh</sub>

---

**Tỉ khối của chất khí** — *Relative density of gases*

$$d_{A/B} = \dfrac{M_A}{M_B};\quad d_{A/kk} = \dfrac{M_A}{29}$$

Trong đó: `d_{A/B}` là tỉ khối của khí A so với khí B; `M_A` là khối lượng mol phân tử của khí A (g/mol); `M_B` là khối lượng mol phân tử của khí B (g/mol); `d_{A/kk}` là tỉ khối của khí A so với không khí.

*Điều kiện:* Hai khí đo ở cùng điều kiện nhiệt độ và áp suất

*Ghi chú:* Khối lượng mol trung bình của không khí lấy bằng 29 g/mol.

<sub>`chemistry.thpt.dai-cuong.ti-khoi-chat-khi` · lớp 10, 11, 12 · #dai-cuong #chat-khi #ti-khoi</sub>

---

### Đại lượng cơ bản

**Khối lượng mol trung bình của hỗn hợp** — *Average molar mass of a mixture*

$$\overline{M} = \dfrac{m_{hh}}{n_{hh}} = \dfrac{\sum n_{i} M_{i}}{\sum n_{i}}$$

Trong đó: `\overline{M}` là khối lượng mol trung bình của hỗn hợp (g/mol); `m_{hh}` là tổng khối lượng hỗn hợp (g); `n_{hh}` là tổng số mol hỗn hợp (mol); `n_{i}` là số mol chất thứ i (mol); `M_{i}` là khối lượng mol chất thứ i (g/mol).

*Điều kiện:* Hỗn hợp không xảy ra phản ứng; n_hh > 0

*Ghi chú:* Luôn có M_min < M_trung bình < M_max, dùng để chặn khoảng khi biện luận.

<sub>`chemistry.thpt.dai-luong-co-ban.khoi-luong-mol-trung-binh` · lớp 10, 11, 12 · #hon-hop-khi #khoi-luong-mol-trung-binh #thpt</sub>

---

**Khối lượng mol trung bình theo phần trăm thể tích** — *Average molar mass from volume percentages*

$$\overline{M} = \dfrac{M_{1}\%V_{1} + M_{2}\%V_{2} + \cdots + M_{k}\%V_{k}}{100}$$

Trong đó: `\overline{M}` là khối lượng mol trung bình (g/mol); `M_{i}` là khối lượng mol khí thứ i (g/mol); `\%V_{i}` là phần trăm thể tích khí thứ i (%).

*Điều kiện:* Các khí đo cùng điều kiện; tổng %V bằng 100%

*Ghi chú:* Với chất khí, phần trăm thể tích bằng phần trăm số mol (định luật Avogadro).

<sub>`chemistry.thpt.dai-luong-co-ban.khoi-luong-mol-trung-binh-theo-phan-tram` · lớp 10, 11, 12 · #hon-hop-khi #phan-tram-the-tich #thpt</sub>

---

**Số mol nguyên tố trong hợp chất** — *Moles of an element within a compound*

$$n_{A} = x \cdot n_{A_{x}B_{y}}$$

Trong đó: `n_{A}` là số mol nguyên tố A (mol); `x` là chỉ số của A trong công thức; `n_{A_{x}B_{y}}` là số mol hợp chất (mol).

*Điều kiện:* Hợp chất có công thức phân tử xác định

*Ghi chú:* Là bước trung gian bắt buộc khi áp dụng định luật bảo toàn nguyên tố.

<sub>`chemistry.thpt.dai-luong-co-ban.so-mol-nguyen-to-trong-hop-chat` · lớp 10, 11, 12 · #mol #bao-toan-nguyen-to #hop-chat</sub>

---

### Định lượng hoá học theo quy ước quốc tế

**Nguyên tắc chuẩn độ ngược (back titration)** — *Back titration principle*

$$n_{X} = n_{0} - n_{d}$$

Trong đó: `n_{X}` là số mol chất cần xác định, tính qua lượng thuốc thử đã phản ứng (mol); `n_{0}` là số mol thuốc thử cho vào ban đầu, lấy dư và biết chính xác (mol); `n_{d}` là số mol thuốc thử còn dư, xác định bằng phép chuẩn độ thứ hai (mol).

*Điều kiện:* Dùng khi chất cần phân tích là chất rắn khó tan, phản ứng chậm hoặc không có chỉ thị thích hợp cho chuẩn độ trực tiếp

*Ghi chú:* Kĩ thuật bắt buộc trong A-Level (ví dụ xác định hàm lượng CaCO3 trong đá vôi hoặc vỏ trứng) và trong IB. CT GDPT 2018 Việt Nam chỉ dạy chuẩn độ trực tiếp acid - base.

<sub>`chemistry.thpt.dinh-luong-quoc-te.chuan-do-nguoc` · lớp 10, 11, 12 · #a-level #ib #chuan-do #chuan-do-nguoc</sub>

---

**Hệ thức tỉ lượng tổng quát trong chuẩn độ thể tích** — *Stoichiometric relation in a volumetric titration*

$$\dfrac{c_{A} V_{A}}{a} = \dfrac{c_{B} V_{B}}{b}$$

Trong đó: `c_{A}` là nồng độ mol của chất A (dung dịch chuẩn trên buret) (mol/L); `V_{A}` là thể tích dung dịch A đã dùng đến điểm cuối (L); `a` là hệ số tỉ lượng của A trong phương trình đã cân bằng (); `c_{B}` là nồng độ mol của chất B (dung dịch được chuẩn độ) (mol/L); `V_{B}` là thể tích dung dịch B lấy để chuẩn độ (L); `b` là hệ số tỉ lượng của B trong phương trình đã cân bằng ().

*Điều kiện:* Đúng tại điểm tương đương; nồng độ và thể tích phải cùng hệ đơn vị

*Ghi chú:* AP (Unit 4), IB (Reactivity 3.1) và A-Level đều dùng dạng tổng quát có hệ số tỉ lượng a, b - không giới hạn ở chuẩn độ acid - base tỉ lệ 1:1 như phần lớn bài tập CT GDPT 2018. Kho AISTEM đã có bản đại học tương đương; bản này đặt ở bậc THPT quốc tế.

<sub>`chemistry.thpt.dinh-luong-quoc-te.he-thuc-chuan-do` · lớp 10, 11, 12 · #ap #ib #a-level #chuan-do</sub>

---

**Hiệu suất nguyên tử (atom economy)** — *Atom economy*

$$AE = \dfrac{\nu_{p} M_{p}}{\sum_{i} \nu_{i} M_{i}} \times 100\%$$

Trong đó: `AE` là hiệu suất nguyên tử: phần trăm khối lượng chất tham gia đi vào sản phẩm mong muốn (); `\nu_{p}` là hệ số tỉ lượng của sản phẩm mong muốn trong phương trình đã cân bằng; `M_{p}` là khối lượng mol của sản phẩm mong muốn (g/mol); `\nu_{i}` là hệ số tỉ lượng của chất tham gia thứ i; `M_{i}` là khối lượng mol của chất tham gia thứ i (g/mol).

*Điều kiện:* Tính trên phương trình đã cân bằng; mẫu số lấy tổng theo mọi chất tham gia (tương đương tổng theo mọi sản phẩm)

*Ghi chú:* Chemistry Data Booklet của IB (mục 1) in dạng rút gọn '% atom economy = molar mass of desired product / molar mass of all reactants x 100', trong đó 'all reactants' đã ngầm bao gồm hệ số tỉ lượng; công thức ở đây là dạng tổng quát viết rõ hệ số. IB (Reactivity 2.1) và AQA A-level (3.1.2) đều yêu cầu tính atom economy như một chỉ số hoá học xanh; Cambridge 9701 KHÔNG có nội dung này. Đây là đại lượng LÍ THUYẾT chỉ phụ thuộc phương trình, khác hẳn hiệu suất phản ứng (percentage yield) là đại lượng thực nghiệm. Phản ứng cộng có AE = 100%; phản ứng thế và tách luôn có AE < 100%. CT GDPT 2018 Việt Nam không có khái niệm này.

<sub>`chemistry.thpt.dinh-luong-quoc-te.hieu-suat-nguyen-tu` · lớp 10, 11, 12 · #ib #a-level #hoa-hoc-xanh #atom-economy</sub>

---

**Thể tích mol khí ở r.t.p. (điều kiện phòng) trong A-Level** — *Molar gas volume at room temperature and pressure (r.t.p.)*

$$V_{m}(\mathrm{r.t.p.}) = 24.0\ \mathrm{dm^{3}\,mol^{-1}} \quad \Rightarrow \quad n = \dfrac{V}{24.0}$$

Trong đó: `V_{m}` là thể tích mol của khí ở điều kiện phòng (khoảng 20 độ C, 101 kPa) (dm^3/mol); `n` là số mol khí (mol); `V` là thể tích khí đo ở điều kiện phòng, tính bằng dm^3 (dm^3).

*Điều kiện:* Khí lí tưởng ở điều kiện phòng (khoảng 20 độ C, áp suất khí quyển); chỉ dùng khi đề bài ghi rõ r.t.p. hoặc 'room conditions'

*Ghi chú:* Mục dữ liệu của Cambridge 9701 ghi nguyên văn 'V_m = 24,0 dm^3 mol^-1 at room conditions' (AQA và OCR gọi là r.t.p.); tính theo cm^3 là 24000 cm^3/mol. Chú ý: cùng bảng dữ liệu đó còn cấp V_m = 22,4 dm^3/mol ở s.t.p. (101 kPa, 273 K), nên A-Level dùng ĐỒNG THỜI hai hằng số tuỳ điều kiện đề bài cho. CT GDPT 2018 Việt Nam không dùng khái niệm r.t.p.; Việt Nam dùng 24,79 L/mol ở 25 độ C và 1 bar.

<sub>`chemistry.thpt.dinh-luong-quoc-te.the-tich-mol-rtp` · lớp 10, 11, 12 · #a-level #rtp #the-tich-mol</sub>

---

**Thể tích mol khí ở STP theo định nghĩa IUPAC hiện hành** — *Molar volume of an ideal gas at IUPAC STP*

$$V_{m} = \dfrac{RT}{p} = \dfrac{8.314 \times 273.15}{1.00 \times 10^{5}} = 2.27 \times 10^{-2}\ \mathrm{m^{3}\,mol^{-1}} = 22.7\ \mathrm{dm^{3}\,mol^{-1}}$$

Trong đó: `V_{m}` là thể tích mol của khí lí tưởng (thể tích của 1 mol khí) (m^3/mol); `R` là hằng số khí lí tưởng, R = 8,314 J/(K.mol) (J/(mol*K)); `T` là nhiệt độ tuyệt đối ở STP, T = 273,15 K (0 độ C) (K); `p` là áp suất chuẩn ở STP, p = 100 kPa = 1 bar (Pa).

*Điều kiện:* Khí được coi là khí lí tưởng; STP theo IUPAC sau 1982 là 0 độ C và 100 kPa (1 bar), KHÔNG phải 1 atm

*Ghi chú:* Chỉ IB dùng định nghĩa STP hiện hành của IUPAC: Chemistry Data Booklet của IB (mục 2) ghi V_m = 2,27x10^-2 m^3/mol = 22,7 dm^3/mol ở STP. BA con số phải phân biệt rõ: (a) 22,7 L/mol - IB, STP theo IUPAC sau 1982 là 0 độ C và 100 kPa (1 bar); (b) 22,4 L/mol - bảng công thức kì thi AP Chemistry ghi nguyên văn 'STP = 273.15 K and 1.0 atm, Ideal gas at STP = 22.4 L mol^-1', và mục dữ liệu Cambridge 9701 ghi 'V_m = 22,4 dm^3/mol at s.t.p. (101 kPa and 273 K)', tức cả AP lẫn CIE vẫn dùng STP CŨ ở 1 atm; (c) 24,79 L/mol - CT GDPT 2018 Việt Nam, 'điều kiện chuẩn' 25 độ C và 1 bar. Đây là khác biệt quy ước gây sai số vài phần trăm nếu dùng lẫn.

<sub>`chemistry.thpt.dinh-luong-quoc-te.the-tich-mol-stp-iupac` · lớp 10, 11, 12 · #ib #iupac #the-tich-mol #stp</sub>

---

**Độ không đảm bảo tương đối (phần trăm) của một phép đo** — *Percentage (relative) uncertainty of a measurement*

$$u_{\%} = \dfrac{\Delta x}{x} \times 100\%$$

Trong đó: `u_{\%}` là độ không đảm bảo tương đối tính theo phần trăm (); `\Delta x` là độ không đảm bảo tuyệt đối của dụng cụ hoặc phép đo (); `x` là giá trị đo được ().

*Điều kiện:* Với dụng cụ chia độ, Delta x thường lấy bằng nửa vạch chia nhỏ nhất; với buret phải nhân đôi vì phải đọc hai lần

*Ghi chú:* Bắt buộc trong IB Internal Assessment và trong practical endorsement của A-Level. CT GDPT 2018 Việt Nam không yêu cầu xử lí độ không đảm bảo trong bài thực hành Hoá học.

<sub>`chemistry.thpt.dinh-luong-quoc-te.do-khong-dam-bao-tuong-doi` · lớp 10, 11, 12 · #ib #a-level #thuc-nghiem #sai-so</sub>

---

**Quy tắc lan truyền độ không đảm bảo** — *Propagation of uncertainties*

$$y = a \pm b \Rightarrow \Delta y = \Delta a + \Delta b; \qquad y = \dfrac{a\,b}{c} \Rightarrow \dfrac{\Delta y}{y} = \dfrac{\Delta a}{a} + \dfrac{\Delta b}{b} + \dfrac{\Delta c}{c}$$

Trong đó: `y` là đại lượng cần tính; `a` là đại lượng đo thứ nhất; `b` là đại lượng đo thứ hai; `c` là đại lượng đo thứ ba; `\Delta y` là độ không đảm bảo tuyệt đối của y; `\Delta a` là độ không đảm bảo tuyệt đối của a; `\Delta b` là độ không đảm bảo tuyệt đối của b; `\Delta c` là độ không đảm bảo tuyệt đối của c.

*Điều kiện:* Cộng hoặc trừ: cộng các độ không đảm bảo TUYỆT ĐỐI. Nhân hoặc chia: cộng các độ không đảm bảo TƯƠNG ĐỐI

*Ghi chú:* Quy tắc do IB quy định cho Internal Assessment và được A-Level dùng khi đánh giá thí nghiệm. Với luỹ thừa y = a^n thì Delta y/y = n(Delta a/a). CT GDPT 2018 Việt Nam không dạy nội dung này ở môn Hoá học.

<sub>`chemistry.thpt.dinh-luong-quoc-te.lan-truyen-do-khong-dam-bao` · lớp 10, 11, 12 · #ib #a-level #sai-so #thuc-nghiem</sub>

---

**Sai số phần trăm so với giá trị lí thuyết** — *Percentage error against the literature value*

$$E_{\%} = \left| \dfrac{x_{tn} - x_{lt}}{x_{lt}} \right| \times 100\%$$

Trong đó: `E_{\%}` là sai số phần trăm của kết quả thí nghiệm (); `x_{tn}` là giá trị thu được từ thí nghiệm (); `x_{lt}` là giá trị lí thuyết hoặc giá trị tra bảng ().

*Điều kiện:* Chỉ dùng khi có giá trị tham chiếu đáng tin cậy

*Ghi chú:* IB IA yêu cầu so sánh sai số phần trăm với tổng độ không đảm bảo phần trăm: nếu sai số phần trăm lớn hơn nhiều thì kết luận có sai số hệ thống. Đây là kĩ năng đánh giá đặc trưng của IB và A-Level, không có trong CT GDPT 2018.

<sub>`chemistry.thpt.dinh-luong-quoc-te.sai-so-phan-tram-thuc-nghiem` · lớp 10, 11, 12 · #ib #a-level #sai-so #danh-gia</sub>

---

**Nồng độ phần triệu ppm và phần tỉ ppb** — *Concentration in parts per million and parts per billion*

$$c_{\mathrm{ppm}} = \dfrac{m_{B}}{m_{dd}} \times 10^{6}, \qquad c_{\mathrm{ppb}} = \dfrac{m_{B}}{m_{dd}} \times 10^{9}$$

Trong đó: `c_{\mathrm{ppm}}` là nồng độ tính theo phần triệu (); `c_{\mathrm{ppb}}` là nồng độ tính theo phần tỉ (); `m_{B}` là khối lượng chất tan B (g); `m_{dd}` là khối lượng toàn bộ dung dịch hoặc mẫu (g).

*Điều kiện:* Với dung dịch nước loãng, khối lượng riêng xấp xỉ 1 g/mL nên 1 ppm tương đương 1 mg/L

*Ghi chú:* IB (Structure 1.4) và A-Level dùng ppm cho phân tích môi trường, nước và khí quyển. KHÔNG được gán cho AP: CED của AP Chemistry có exclusion statement 'Calculations of molality, percent by mass, and percent by volume for solutions will not be assessed on the AP Exam' - AP chỉ dùng nồng độ mol. CT GDPT 2018 Việt Nam không đưa ppm vào phần nồng độ dung dịch bắt buộc.

<sub>`chemistry.thpt.dinh-luong-quoc-te.nong-do-ppm` · lớp 10, 11, 12 · #ib #a-level #nong-do #ppm</sub>

---

**Định nghĩa mol theo SI 2019 và hằng số khối lượng mol** — *The 2019 SI definition of the mole and the molar mass constant*

$$N_{A} = 6.02214076 \times 10^{23}\ \mathrm{mol^{-1}}, \qquad M_{u} = N_{A}\, m_{u} \approx 1\ \mathrm{g\,mol^{-1}}$$

Trong đó: `N_{A}` là hằng số Avogadro, từ 20/5/2019 được ấn định là một giá trị chính xác theo định nghĩa (1/mol); `M_{u}` là hằng số khối lượng mol, dùng để chuyển nguyên tử khối tương đối sang khối lượng mol (g/mol); `m_{u}` là đơn vị khối lượng nguyên tử thống nhất, bằng 1/12 khối lượng một nguyên tử carbon-12 (kg).

*Điều kiện:* Định nghĩa hiện hành: 1 mol chứa đúng 6,02214076x10^23 thực thể xác định

*Ghi chú:* IB (Structure 1.4) và IUPAC nêu rõ: sau cải cách SI 2019, mol KHÔNG còn được định nghĩa qua 12 g carbon-12, do đó M(12C) = 12 g/mol chỉ còn đúng trong sai số thực nghiệm chứ không còn là định nghĩa. CT GDPT 2018 Việt Nam vẫn phát biểu theo lối cũ nên đây là điểm khác biệt về quy ước khi học chương trình quốc tế.

<sub>`chemistry.thpt.dinh-luong-quoc-te.dinh-nghia-mol-si-2019` · lớp 10, 11, 12 · #ib #iupac #mol #hang-so-avogadro</sub>

---

### Động học phản ứng bậc THPT quốc tế

**Bước quyết định tốc độ và biểu thức tốc độ suy từ cơ chế** — *Rate-determining step and the rate law derived from a mechanism*

$$v = k_{\text{RDS}} \prod_{i} [X_{i}]^{\nu_{i}}$$

Trong đó: `v` là tốc độ chung của phản ứng (mol/(L*s)); `k_{\text{RDS}}` là hằng số tốc độ của bước chậm nhất (bước quyết định tốc độ); `[X_{i}]` là nồng độ của tiểu phân tham gia bước quyết định tốc độ (mol/L); `\nu_{i}` là hệ số tỉ lượng của tiểu phân X_i trong bước quyết định tốc độ.

*Điều kiện:* Cơ chế phải cộng lại đúng phương trình tổng; chất trung gian xuất hiện trong biểu thức phải được khử bằng cân bằng nhanh đứng trước

*Ghi chú:* AP Unit 5, IB HL Reactivity 2.2 và A-Level đều yêu cầu suy biểu thức tốc độ từ cơ chế và ngược lại, kiểm tra cơ chế bằng biểu thức tốc độ thực nghiệm. Số phân tử tham gia một bước sơ cấp gọi là phân tử số (molecularity) và bằng đúng số mũ trong bước đó - điều KHÔNG đúng cho phản ứng tổng. CT GDPT 2018 Việt Nam không dạy cơ chế nhiều bước ở THPT.

<sub>`chemistry.thpt.dong-hoc-tich-phan.buoc-quyet-dinh-toc-do` · lớp 10, 11, 12 · #ap #ib-hl #a-level #co-che #buoc-cham</sub>

---

**Phân biệt chất trung gian và chất xúc tác trong cơ chế** — *Distinguishing an intermediate from a catalyst in a mechanism*

$$I:\ \text{ve phai buoc } i \rightarrow \text{ve trai buoc } j; \qquad C:\ \text{ve trai buoc } i \rightarrow \text{ve phai buoc } j$$

Trong đó: `I` là chất trung gian: xuất hiện lần đầu ở vế phải của một bước rồi bị tiêu thụ ở bước sau; `C` là chất xúc tác: xuất hiện lần đầu ở vế trái của một bước rồi được tái tạo ở bước sau; `i` là chỉ số của bước mà tiểu phân xuất hiện lần đầu; `j` là chỉ số của bước sau đó, trong đó tiểu phân xuất hiện ở vế đối diện.

*Điều kiện:* Cả hai đều KHÔNG xuất hiện trong phương trình tổng của phản ứng

*Ghi chú:* AP Unit 5 (Topic 5.8 Reaction Mechanism and Rate Law, Topic 5.11 Catalysis), IB HL và Cambridge 9701 mục 26.1 đều hỏi trực tiếp dạng này. Ranh giới của AP: CED có exclusion statement 'Collection of data pertaining to detection of a reaction intermediate will not be assessed on the AP Exam' - AP hỏi NHẬN DẠNG chất trung gian trong cơ chế cho sẵn chứ không hỏi cách phát hiện nó bằng thực nghiệm. Chất xúc tác có thể có mặt trong biểu thức tốc độ (xúc tác đồng thể), chất trung gian thì phải khử khỏi biểu thức. AP còn phân biệt xúc tác đồng thể, xúc tác dị thể và xúc tác enzyme. CT GDPT 2018 Việt Nam chỉ nêu định nghĩa xúc tác, không phân tích cơ chế nhiều bước.

<sub>`chemistry.thpt.dong-hoc-tich-phan.chat-trung-gian-va-xuc-tac` · lớp 10, 11, 12 · #ap #ib-hl #co-che #xuc-tac</sub>

---

**Năng lượng hoạt hoá của phản ứng nghịch trên giản đồ năng lượng** — *Activation energy of the reverse reaction from the energy profile*

$$E_{a}^{ngh} = E_{a}^{thuan} - \Delta H$$

Trong đó: `E_{a}^{ngh}` là năng lượng hoạt hoá của phản ứng nghịch (kJ/mol); `E_{a}^{thuan}` là năng lượng hoạt hoá của phản ứng thuận (kJ/mol); `\Delta H` là biến thiên enthalpy của phản ứng thuận (kJ/mol).

*Điều kiện:* Đọc trên giản đồ năng lượng theo toạ độ phản ứng; Delta H là hiệu mức năng lượng sản phẩm trừ chất tham gia

*Ghi chú:* Câu hỏi thường gặp của AP Unit 5 và A-Level khi cho giản đồ năng lượng. Với phản ứng toả nhiệt (Delta H < 0) thì Ea nghịch luôn LỚN hơn Ea thuận. CT GDPT 2018 Việt Nam vẽ giản đồ năng lượng nhưng không yêu cầu tính Ea nghịch.

<sub>`chemistry.thpt.dong-hoc-tich-phan.nang-luong-hoat-hoa-phan-ung-nghich` · lớp 10, 11, 12 · #ap #a-level #nang-luong-hoat-hoa #gian-do-nang-luong</sub>

---

**Phương trình Arrhenius dạng logarit và đồ thị Arrhenius** — *Arrhenius equation in logarithmic form and the Arrhenius plot*

$$\ln k = -\dfrac{E_{a}}{R}\cdot\dfrac{1}{T} + \ln A$$

Trong đó: `k` là hằng số tốc độ ở nhiệt độ T; `E_{a}` là năng lượng hoạt hoá (J/mol); `R` là hằng số khí, 8,314 J/(K.mol) (J/(mol*K)); `T` là nhiệt độ tuyệt đối (K); `A` là thừa số tần số (hằng số Arrhenius).

*Điều kiện:* Ea coi như không đổi trong khoảng nhiệt độ khảo sát

*Ghi chú:* Chemistry Data Booklet của IB (mục 1) in cả hai dạng k = A.e^(-Ea/RT) và ln k = -Ea/(RT) + ln A; IB HL Reactivity 2.2 yêu cầu phân tích biểu diễn đồ thị của phương trình Arrhenius kể cả dạng tuyến tính. AQA (3.1.9) và Cambridge 9701 cũng yêu cầu đồ thị ln k theo 1/T: hệ số góc -Ea/R, tung độ gốc ln A. KHÔNG được gán cho AP: CED của AP Chemistry có exclusion statement 'Calculations involving the Arrhenius equation will not be assessed on the AP Exam'. Kho Việt Nam đã có phương trình Arrhenius dạng mũ và dạng hai nhiệt độ ở THPT, nhưng KHÔNG có dạng tuyến tính hoá dùng để đọc Ea từ đồ thị.

<sub>`chemistry.thpt.dong-hoc-tich-phan.arrhenius-dang-logarit` · lớp 10, 11, 12 · #a-level #ib-hl #arrhenius #do-thi-tuyen-tinh</sub>

---

**Phương trình động học tích phân bậc 2** — *Integrated rate law for a second-order reaction*

$$\dfrac{1}{[A]_{t}} - \dfrac{1}{[A]_{0}} = kt$$

Trong đó: `[A]_{t}` là nồng độ chất A tại thời điểm t (mol/L); `[A]_{0}` là nồng độ ban đầu của chất A (mol/L); `k` là hằng số tốc độ của phản ứng bậc 2 (L/(mol*s)); `t` là thời gian phản ứng (s).

*Điều kiện:* Phản ứng bậc 2 theo một chất A duy nhất (hoặc hai chất có cùng nồng độ đầu và hệ số tỉ lượng bằng nhau)

*Ghi chú:* Dạng in trên bảng công thức kì thi AP Chemistry (Unit 5). Đồ thị 1/[A] theo t là đường thẳng hệ số góc +k (hệ số góc DƯƠNG, khác hai bậc còn lại). Không gán cho IB và A-Level vì hai hệ này xác định bậc bằng đồ thị và phương pháp tốc độ đầu chứ không cấp phương trình tích phân. Kho AISTEM đã có bản đại học; CT GDPT 2018 Việt Nam không có ở THPT.

<sub>`chemistry.thpt.dong-hoc-tich-phan.bac-hai` · lớp 10, 11, 12 · #ap #bac-hai #dong-hoc #phuong-trinh-tich-phan</sub>

---

**Phương trình động học tích phân bậc 0** — *Integrated rate law for a zero-order reaction*

$$[A]_{t} - [A]_{0} = -kt$$

Trong đó: `[A]_{t}` là nồng độ chất A tại thời điểm t (mol/L); `[A]_{0}` là nồng độ ban đầu của chất A (mol/L); `k` là hằng số tốc độ của phản ứng bậc 0 (mol/(L*s)); `t` là thời gian phản ứng (s).

*Điều kiện:* Phản ứng bậc 0 theo A; tốc độ không phụ thuộc nồng độ A (thường gặp khi bề mặt xúc tác hoặc enzyme đã bão hoà)

*Ghi chú:* Dạng viết chuyển vế này chính là dạng in trên bảng công thức kì thi AP Chemistry ('[A]t - [A]0 = -kt', Unit 5). Đồ thị [A] theo t là đường thẳng hệ số góc -k. Không gán cho IB và A-Level: IB HL Reactivity 2.2 và Cambridge 9701 mục 26.1 xác định bậc từ ĐỒ THỊ nồng độ - thời gian, từ đồ thị tốc độ - nồng độ và từ phương pháp tốc độ đầu chứ không cấp phương trình động học tích phân. Kho AISTEM đã có bản đại học; CT GDPT 2018 Việt Nam KHÔNG có phương trình động học tích phân ở THPT.

<sub>`chemistry.thpt.dong-hoc-tich-phan.bac-khong` · lớp 10, 11, 12 · #ap #dong-hoc #bac-khong #phuong-trinh-tich-phan</sub>

---

**Phương trình động học tích phân bậc 1** — *Integrated rate law for a first-order reaction*

$$\ln[A]_{t} - \ln[A]_{0} = -kt \quad \Leftrightarrow \quad [A]_{t} = [A]_{0}e^{-kt}$$

Trong đó: `[A]_{t}` là nồng độ chất A tại thời điểm t (mol/L); `[A]_{0}` là nồng độ ban đầu của chất A (mol/L); `k` là hằng số tốc độ của phản ứng bậc 1 (1/s); `t` là thời gian phản ứng (s).

*Điều kiện:* Phản ứng bậc 1 theo A; có thể thay nồng độ bằng áp suất riêng phần hoặc số mol vì tỉ số là như nhau

*Ghi chú:* Dạng hiệu hai logarit là dạng in trên bảng công thức kì thi AP Chemistry (Unit 5). Cambridge 9701 (mục 26.1) không cấp phương trình này mà dùng hệ quả tương đương k = 0,693/t(1/2) cho bậc 1; IB HL xác định bậc từ đồ thị nồng độ - thời gian. Đồ thị ln[A] theo t là đường thẳng hệ số góc -k. Kho AISTEM đã có bản đại học; CT GDPT 2018 Việt Nam không có ở THPT.

<sub>`chemistry.thpt.dong-hoc-tich-phan.bac-mot` · lớp 10, 11, 12 · #ap #a-level #bac-mot #dong-hoc</sub>

---

**Thời gian bán huỷ của phản ứng bậc 2** — *Half-life of a second-order reaction*

$$t_{1/2} = \dfrac{1}{k[A]_{0}}$$

Trong đó: `t_{1/2}` là thời gian để nồng độ A giảm còn một nửa (s); `k` là hằng số tốc độ bậc 2 (L/(mol*s)); `[A]_{0}` là nồng độ ban đầu của A (mol/L).

*Điều kiện:* Phản ứng bậc 2 theo A

*Ghi chú:* Hệ quả suy từ phương trình động học tích phân bậc 2 có trên bảng công thức AP; cùng ranh giới như bán huỷ bậc 0 - CED của AP chỉ bắt buộc công thức bán huỷ cho bậc 1. Thời gian bán huỷ TĂNG gấp đôi sau mỗi chu kì - dấu hiệu phân biệt rõ với bậc 1 (không đổi) và bậc 0 (giảm một nửa). CT GDPT 2018 Việt Nam không có nội dung này. Kho AISTEM đã có bản đại học chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-2; bản này đặt ở bậc THPT quốc tế và nêu rõ ranh giới đánh giá của AP.

<sub>`chemistry.thpt.dong-hoc-tich-phan.ban-huy-bac-hai` · lớp 10, 11, 12 · #ap #ban-huy #bac-hai #dong-hoc</sub>

---

**Thời gian bán huỷ của phản ứng bậc 0** — *Half-life of a zero-order reaction*

$$t_{1/2} = \dfrac{[A]_{0}}{2k}$$

Trong đó: `t_{1/2}` là thời gian để nồng độ A giảm còn một nửa (s); `[A]_{0}` là nồng độ ban đầu của A (mol/L); `k` là hằng số tốc độ bậc 0 (mol/(L*s)).

*Điều kiện:* Phản ứng bậc 0 theo A

*Ghi chú:* Hệ quả suy trực tiếp từ phương trình động học tích phân bậc 0 có trên bảng công thức AP. Ranh giới cần nhớ: CED của AP (mục 5.3.A.5) chỉ nêu công thức bán huỷ t(1/2) = 0,693/k cho phản ứng BẬC 1, và bảng công thức cũng chỉ in đúng công thức đó; biểu thức bán huỷ bậc 0 là kết quả suy ra, dùng để NHẬN DẠNG bậc chứ không phải công thức bắt buộc nhớ. Đặc điểm nhận dạng: thời gian bán huỷ GIẢM dần vì phụ thuộc nồng độ đầu. CT GDPT 2018 Việt Nam không dạy nội dung này. Kho AISTEM đã có bản đại học chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-0 phát biểu trong khuôn khổ động hoá học đại cương; bản này đặt ở bậc THPT quốc tế và nêu rõ ranh giới đánh giá của AP.

<sub>`chemistry.thpt.dong-hoc-tich-phan.ban-huy-bac-khong` · lớp 10, 11, 12 · #ap #ban-huy #bac-khong #dong-hoc</sub>

---

**Thời gian bán huỷ của phản ứng bậc 1** — *Half-life of a first-order reaction*

$$t_{1/2} = \dfrac{\ln 2}{k} = \dfrac{0.693}{k}$$

Trong đó: `t_{1/2}` là thời gian để nồng độ A giảm còn một nửa (s); `k` là hằng số tốc độ bậc 1 (1/s).

*Điều kiện:* Phản ứng bậc 1; thời gian bán huỷ KHÔNG phụ thuộc nồng độ ban đầu

*Ghi chú:* In sẵn trên bảng công thức kì thi AP Chemistry dưới dạng t(1/2) = 0,693/k (CED mục 5.3.A.5). Cambridge 9701 mục 26.1 yêu cầu 'use the half-life of a first-order reaction in calculations' và tính k bằng k = 0,693/t(1/2); IB HL nêu tính chất thời gian bán huỷ không đổi của bậc 1. Là cơ sở của bài toán phân rã phóng xạ và của dấu hiệu nhận biết bậc 1 khi đo động học. CT GDPT 2018 Việt Nam không có ở môn Hoá học THPT. Kho AISTEM đã có bản đại học chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-1; bản này giữ ở bậc THPT quốc tế vì các hệ AP, IB và A-Level đều dùng trực tiếp trong bài thi.

<sub>`chemistry.thpt.dong-hoc-tich-phan.ban-huy-bac-mot` · lớp 10, 11, 12 · #ap #ib-hl #a-level #ban-huy</sub>

---

**Dùng các thời gian bán huỷ liên tiếp để nhận biết bậc phản ứng** — *Using successive half-lives to identify the reaction order*

$$\dfrac{t_{1/2}^{(2)}}{t_{1/2}^{(1)}} = \begin{cases} 1/2 & \text{bac } 0 \\ 1 & \text{bac } 1 \\ 2 & \text{bac } 2 \end{cases}$$

Trong đó: `t_{1/2}^{(1)}` là thời gian bán huỷ thứ nhất, đo từ nồng độ đầu (s); `t_{1/2}^{(2)}` là thời gian bán huỷ thứ hai, đo tiếp ngay sau đó (s).

*Điều kiện:* Đọc trực tiếp trên đồ thị nồng độ theo thời gian của một thí nghiệm duy nhất

*Ghi chú:* Kĩ thuật continuous monitoring của A-Level (AQA, Edexcel) và IB HL: nếu các thời gian bán huỷ liên tiếp bằng nhau thì phản ứng bậc 1. CT GDPT 2018 Việt Nam không có nội dung này.

<sub>`chemistry.thpt.dong-hoc-tich-phan.ban-huy-lien-tiep-khong-doi` · lớp 10, 11, 12 · #a-level #ib-hl #ban-huy #bac-phan-ung</sub>

---

**Tuyến tính hoá đồ thị để xác định bậc phản ứng** — *Determining reaction order from linearised plots*

$$\begin{cases} [A]\ \text{theo}\ t\ \text{thang} & \text{bac } 0,\ \text{he so goc} = -k \\ \ln[A]\ \text{theo}\ t\ \text{thang} & \text{bac } 1,\ \text{he so goc} = -k \\ 1/[A]\ \text{theo}\ t\ \text{thang} & \text{bac } 2,\ \text{he so goc} = +k \end{cases}$$

Trong đó: `[A]` là nồng độ chất phản ứng A (mol/L); `t` là thời gian (s); `k` là hằng số tốc độ phản ứng ().

*Điều kiện:* Chỉ một trong ba đồ thị cho đường thẳng; bậc phản ứng là bậc ứng với đồ thị tuyến tính đó

*Ghi chú:* Kĩ năng cốt lõi được hỏi trong FRQ của AP Chemistry (Unit 5) và trong IB HL. Đơn vị của k phụ thuộc bậc phản ứng nên cột 'units' để trống cho k. CT GDPT 2018 Việt Nam không có dạng bài xác định bậc bằng tuyến tính hoá đồ thị.

<sub>`chemistry.thpt.dong-hoc-tich-phan.do-thi-tuyen-tinh-xac-dinh-bac` · lớp 10, 11, 12 · #ap #ib-hl #do-thi-tuyen-tinh #bac-phan-ung</sub>

---

**Đơn vị của hằng số tốc độ theo bậc phản ứng** — *Units of the rate constant as a function of reaction order*

$$[k] = \mathrm{mol^{1-n}\,L^{\,n-1}\,s^{-1}}$$

Trong đó: `[k]` là đơn vị của hằng số tốc độ; `n` là bậc chung của phản ứng ().

*Điều kiện:* Suy ra từ điều kiện đồng nhất thứ nguyên của biểu thức tốc độ v = k[A]^a[B]^b với n = a + b

*Ghi chú:* A-Level (AQA, CIE) và IB HL thường cho điểm riêng cho việc suy ra đơn vị của k, coi đó là bằng chứng học sinh hiểu bậc phản ứng. Bậc 0: mol/(L.s); bậc 1: 1/s; bậc 2: L/(mol.s). Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam không yêu cầu suy đơn vị của k.

<sub>`chemistry.thpt.dong-hoc-tich-phan.don-vi-hang-so-toc-do` · lớp 10, 11, 12 · #a-level #ib-hl #hang-so-toc-do #don-vi</sub>

---

**Phương pháp tốc độ đầu xác định bậc riêng phần** — *Initial-rate method for partial orders*

$$a = \dfrac{\ln\left( v_{2}/v_{1} \right)}{\ln\left( [A]_{2}/[A]_{1} \right)}$$

Trong đó: `a` là bậc riêng phần của phản ứng theo chất A (); `v_{1}` là tốc độ đầu của thí nghiệm 1 (mol/(L*s)); `v_{2}` là tốc độ đầu của thí nghiệm 2 (mol/(L*s)); `[A]_{1}` là nồng độ đầu của A trong thí nghiệm 1 (mol/L); `[A]_{2}` là nồng độ đầu của A trong thí nghiệm 2 (mol/L).

*Điều kiện:* Hai thí nghiệm chỉ khác nhau nồng độ đầu của A, mọi chất khác và nhiệt độ giữ nguyên

*Ghi chú:* Dạng bài bảng số liệu kinh điển của AP Unit 5, IB HL và A-Level. Kho AISTEM có bản đại học; CT GDPT 2018 Việt Nam nêu biểu thức tốc độ nhưng không có dạng bài xác định bậc từ bảng tốc độ đầu.

<sub>`chemistry.thpt.dong-hoc-tich-phan.phuong-phap-toc-do-dau` · lớp 10, 11, 12 · #ap #ib-hl #a-level #toc-do-dau #bac-phan-ung</sub>

---

### Bài toán đốt cháy hợp chất hữu cơ

**Đốt cháy ancol no, mạch hở** — *Combustion of saturated open-chain alcohols*

$$n_{ancol} = n_{H_2O} - n_{CO_2};\quad n_{OH} = n_{O(ancol)} = 2n_{CO_2} + n_{H_2O} - 2n_{O_2}$$

Trong đó: `n_{ancol}` là số mol ancol no mạch hở bị đốt (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{OH}` là tổng số mol nhóm -OH trong lượng ancol đó (mol); `n_{O(ancol)}` là số mol nguyên tử oxi trong ancol (mol); `n_{O_2}` là số mol O2 đã dùng (mol).

*Điều kiện:* Ancol no, mạch hở (đơn chức hoặc đa chức); đốt cháy hoàn toàn

*Ghi chú:* Số nhóm OH trung bình = n(O trong ancol)/n(ancol). Với ancol no đơn chức thì n(O) = n(ancol).

<sub>`chemistry.thpt.dot-chay.ancol-no` · lớp 11 · #huu-co #dot-chay #ancol</sub>

---

**Số mol O2 khi đốt ancol no, đơn chức, mạch hở** — *Oxygen needed to burn a saturated monohydric alcohol*

$$C_nH_{2n+2}O + \dfrac{3n}{2}O_2 \rightarrow nCO_2 + (n+1)H_2O;\quad n_{O_2} = \dfrac{3}{2}n_{CO_2}$$

Trong đó: `n` là số nguyên tử cacbon của ancol; `n_{O_2}` là số mol oxi cần dùng (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol).

*Điều kiện:* Ancol no, đơn chức, mạch hở CnH2n+2O; đốt cháy hoàn toàn

*Ghi chú:* Hệ quả đẹp: với ancol no đơn chức mạch hở thì n(O2) luôn bằng 1,5 lần n(CO2).

<sub>`chemistry.thpt.dot-chay.ancol-no-don-chuc-o2` · lớp 11 · #huu-co #dot-chay #ancol</sub>

---

**Liên hệ giữa số mol chất, CO2, H2O và độ bất bão hòa** — *Relation between moles, CO2, H2O and unsaturation degree*

$$n_{CO_2} - n_{H_2O} = (k-1)\,n_X$$

Trong đó: `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `k` là độ bất bão hòa của phân tử X; `n_X` là số mol chất hữu cơ X bị đốt (mol).

*Điều kiện:* Đốt cháy hoàn toàn; X có công thức bất kì chứa C, H, O (nguyên tử O không ảnh hưởng công thức này)

*Ghi chú:* Với k = 0 (no, hở): n(X) = n(H2O) − n(CO2). Với k = 1: n(CO2) = n(H2O). Với k = 2: n(X) = n(CO2) − n(H2O).

<sub>`chemistry.thpt.dot-chay.hidrocacbon-tong-quat` · lớp 11 · #huu-co #dot-chay #do-bat-bao-hoa</sub>

---

**Đốt cháy ankan** — *Combustion of alkanes*

$$n_{ankan} = n_{H_2O} - n_{CO_2};\quad n_{O_2} = \dfrac{3n+1}{2}n_{ankan}$$

Trong đó: `n_{ankan}` là số mol ankan bị đốt cháy (mol); `n_{H_2O}` là số mol nước sinh ra (mol); `n_{CO_2}` là số mol khí CO2 sinh ra (mol); `n_{O_2}` là số mol oxi cần dùng (mol); `n` là số nguyên tử cacbon của ankan.

*Điều kiện:* Đốt cháy hoàn toàn; áp dụng cho ankan hoặc hỗn hợp các ankan

*Ghi chú:* Dấu hiệu nhận biết: n(H2O) > n(CO2) thì hợp chất là ankan (hoặc chất có k = 0 mạch hở như ancol no, ete no).

<sub>`chemistry.thpt.dot-chay.ankan` · lớp 11 · #huu-co #dot-chay #ankan</sub>

---

**Đốt cháy anken hoặc xicloankan** — *Combustion of alkenes or cycloalkanes*

$$n_{CO_2} = n_{H_2O};\quad n_{O_2} = \dfrac{3n}{2}n_{anken} = \dfrac{3}{2}n_{CO_2}$$

Trong đó: `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{O_2}` là số mol oxi cần dùng (mol); `n_{anken}` là số mol anken bị đốt (mol); `n` là số nguyên tử cacbon của anken.

*Điều kiện:* Đốt cháy hoàn toàn hợp chất CnH2n (anken hoặc xicloankan)

*Ghi chú:* Không tính được số mol chất từ hiệu số mol khí; phải dùng thêm dữ kiện khối lượng hoặc M trung bình.

<sub>`chemistry.thpt.dot-chay.anken` · lớp 11 · #huu-co #dot-chay #anken</sub>

---

**Đốt cháy ankin hoặc ankađien** — *Combustion of alkynes or alkadienes*

$$n_{hidrocacbon} = n_{CO_2} - n_{H_2O}$$

Trong đó: `n_{hidrocacbon}` là số mol ankin hoặc ankađien bị đốt (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol).

*Điều kiện:* Đốt cháy hoàn toàn hợp chất CnH2n-2 mạch hở (k = 2)

*Ghi chú:* Dấu hiệu: n(CO2) > n(H2O) chứng tỏ phân tử có k ≥ 2.

<sub>`chemistry.thpt.dot-chay.ankin-ankadien` · lớp 11 · #huu-co #dot-chay #ankin</sub>

---

**Độ tăng khối lượng bình hấp thụ sản phẩm cháy** — *Mass increase of absorption vessels for combustion products*

$$\begin{cases} \text{bình } H_2SO_4\ \text{đặc, } P_2O_5,\ CaCl_2: & \Delta m = 18n_{H_2O} \\ \text{bình } NaOH,\ KOH: & \Delta m = 44n_{CO_2} \\ \text{bình } Ca(OH)_2\ \text{dư}: & \Delta m_{dd} = 44n_{CO_2} + 18n_{H_2O} - 100n_{CaCO_3} \end{cases}$$

Trong đó: `\Delta m` là độ tăng khối lượng bình hấp thụ (g); `\Delta m_{dd}` là độ biến thiên khối lượng dung dịch (g); `n_{H_2O}` là số mol H2O bị hấp thụ (mol); `n_{CO_2}` là số mol CO2 bị hấp thụ (mol); `n_{CaCO_3}` là số mol kết tủa CaCO3 (mol).

*Điều kiện:* Dẫn toàn bộ sản phẩm cháy qua bình; bình H2SO4 đặc đặt trước bình kiềm

*Ghi chú:* Nếu dẫn qua dung dịch Ca(OH)2 (không tách nước trước) thì khối lượng bình tăng = m(CO2) + m(H2O).

<sub>`chemistry.thpt.dot-chay.khoi-luong-binh-hap-thu` · lớp 11 · #huu-co #dot-chay #hap-thu</sub>

---

**Số mol O2 cần để đốt cháy hiđrocacbon** — *Oxygen required to burn a hydrocarbon*

$$n_{O_2} = n_{CO_2} + \dfrac{n_{H_2O}}{2}$$

Trong đó: `n_{O_2}` là số mol khí oxi cần dùng (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol).

*Điều kiện:* Đốt cháy hoàn toàn hiđrocacbon (phân tử không chứa oxi)

*Ghi chú:* Suy trực tiếp từ bảo toàn nguyên tố oxi: 2n(O2) = 2n(CO2) + n(H2O).

<sub>`chemistry.thpt.dot-chay.so-mol-o2-hidrocacbon` · lớp 11 · #huu-co #dot-chay #bao-toan-nguyen-to</sub>

---

### Cân bằng hóa học

**Thương số phản ứng và chiều diễn biến** — *Reaction quotient and direction of change*

$$Q_{C} = \dfrac{C_{\mathrm{C}}^{c} C_{\mathrm{D}}^{d}}{C_{\mathrm{A}}^{a} C_{\mathrm{B}}^{b}} : \begin{cases} Q_{C} < K_{C} & \text{phan ung theo chieu thuan} \\ Q_{C} = K_{C} & \text{he da can bang} \\ Q_{C} > K_{C} & \text{phan ung theo chieu nghich} \end{cases}$$

Trong đó: `Q_{C}` là thương số phản ứng tại thời điểm đang xét; `C_{\mathrm{A}}` là nồng độ tức thời của các chất (mol/L); `C_{\mathrm{B}}` là nồng độ tức thời của các chất (mol/L); `C_{\mathrm{C}}` là nồng độ tức thời của các chất (mol/L); `C_{\mathrm{D}}` là nồng độ tức thời của các chất (mol/L); `K_{C}` là hằng số cân bằng.

*Điều kiện:* Q có biểu thức giống K nhưng dùng nồng độ ở thời điểm bất kì, không nhất thiết ở cân bằng

*Ghi chú:* Cách nhớ: hệ luôn biến đổi theo chiều làm Q tiến về K.

<sub>`chemistry.thpt.can-bang.thuong-so-phan-ung` · lớp 11 · #thuong-so-phan-ung #can-bang-hoa-hoc #chieu-phan-ung</sub>

---

**Nguyên lí chuyển dịch cân bằng Le Chatelier** — *Le Chatelier's principle*

$$\begin{cases} C \uparrow \text{cua mot chat} & \text{can bang chuyen theo chieu lam giam chat do} \\ p \uparrow & \text{chuyen ve phia co tong so mol khi nho hon} \\ T \uparrow & \text{chuyen theo chieu thu nhiet } (\Delta_{r}H > 0) \end{cases}$$

Trong đó: `C` là nồng độ chất trong hệ cân bằng (mol/L); `p` là áp suất chung của hệ (bar); `T` là nhiệt độ (K); `\Delta_{r}H` là biến thiên enthalpy của phản ứng thuận (kJ/mol).

*Điều kiện:* Hệ đang ở trạng thái cân bằng và chịu một tác động từ bên ngoài

*Ghi chú:* Chất xúc tác không làm chuyển dịch cân bằng, chỉ giúp hệ đạt cân bằng nhanh hơn. Áp suất không ảnh hưởng khi tổng số mol khí hai vế bằng nhau.

<sub>`chemistry.thpt.can-bang.nguyen-li-le-chatelier` · lớp 11 · #le-chatelier #chuyen-dich-can-bang #thpt</sub>

---

**Hiệu suất chuyển hóa tại trạng thái cân bằng** — *Equilibrium conversion*

$$\alpha = \dfrac{n_{0} - n_{cb}}{n_{0}} \times 100\%$$

Trong đó: `\alpha` là hiệu suất (độ) chuyển hóa của chất đang xét (%); `n_{0}` là số mol chất ban đầu (mol); `n_{cb}` là số mol chất còn lại ở trạng thái cân bằng (mol).

*Điều kiện:* Hệ đã đạt trạng thái cân bằng; n0 > 0

*Ghi chú:* Do phản ứng thuận nghịch không xảy ra hoàn toàn nên hiệu suất chuyển hóa luôn nhỏ hơn 100%.

<sub>`chemistry.thpt.can-bang.hieu-suat-chuyen-hoa` · lớp 11 · #hieu-suat-chuyen-hoa #can-bang-hoa-hoc #thpt</sub>

---

**Áp suất riêng phần của một khí trong hỗn hợp** — *Partial pressure of a gas in a mixture*

$$p_{i} = x_{i} \cdot P = \dfrac{n_{i}}{n_{hh}} \cdot P$$

Trong đó: `p_{i}` là áp suất riêng phần của khí i (bar); `x_{i}` là phần mol của khí i; `P` là áp suất tổng của hỗn hợp (bar); `n_{i}` là số mol khí i (mol); `n_{hh}` là tổng số mol khí (mol).

*Điều kiện:* Hỗn hợp khí lí tưởng (định luật Dalton)

*Ghi chú:* Tổng các áp suất riêng phần bằng áp suất tổng của hỗn hợp khí.

<sub>`chemistry.thpt.can-bang.ap-suat-rieng-phan` · lớp 11 · #ap-suat-rieng-phan #dalton #hon-hop-khi</sub>

---

**Hằng số cân bằng theo nồng độ** — *Equilibrium constant in terms of concentration*

$$K_{C} = \dfrac{\left[ \mathrm{C} \right]^{c} \left[ \mathrm{D} \right]^{d}}{\left[ \mathrm{A} \right]^{a} \left[ \mathrm{B} \right]^{b}}$$

Trong đó: `K_{C}` là hằng số cân bằng theo nồng độ; `\left[ \mathrm{A} \right]` là nồng độ các chất đầu ở trạng thái cân bằng; `\left[ \mathrm{B} \right]` là nồng độ các chất đầu ở trạng thái cân bằng; `\left[ \mathrm{C} \right]` là nồng độ các sản phẩm ở trạng thái cân bằng; `\left[ \mathrm{D} \right]` là nồng độ các sản phẩm ở trạng thái cân bằng; `a` là hệ số tỉ lượng của phản ứng aA + bB <=> cC + dD; `b` là hệ số tỉ lượng của phản ứng aA + bB <=> cC + dD; `c` là hệ số tỉ lượng của phản ứng aA + bB <=> cC + dD; `d` là hệ số tỉ lượng của phản ứng aA + bB <=> cC + dD.

*Điều kiện:* Phản ứng thuận nghịch đã đạt cân bằng; không đưa chất rắn nguyên chất và dung môi vào biểu thức

*Ghi chú:* K_C chỉ phụ thuộc bản chất phản ứng và nhiệt độ. K_C càng lớn thì cân bằng càng chuyển dịch về phía sản phẩm.

<sub>`chemistry.thpt.can-bang.hang-so-can-bang-kc` · lớp 11 · #can-bang-hoa-hoc #hang-so-can-bang #kc</sub>

---

**Hằng số cân bằng theo áp suất riêng phần** — *Equilibrium constant in terms of partial pressures*

$$K_{p} = \dfrac{p_{\mathrm{C}}^{c} \, p_{\mathrm{D}}^{d}}{p_{\mathrm{A}}^{a} \, p_{\mathrm{B}}^{b}}$$

Trong đó: `K_{p}` là hằng số cân bằng theo áp suất; `p_{\mathrm{A}}` là áp suất riêng phần của các chất đầu ở cân bằng (bar); `p_{\mathrm{B}}` là áp suất riêng phần của các chất đầu ở cân bằng (bar); `p_{\mathrm{C}}` là áp suất riêng phần của các sản phẩm ở cân bằng (bar); `p_{\mathrm{D}}` là áp suất riêng phần của các sản phẩm ở cân bằng (bar); `a` là hệ số tỉ lượng; `b` là hệ số tỉ lượng; `c` là hệ số tỉ lượng; `d` là hệ số tỉ lượng.

*Điều kiện:* Chỉ áp dụng cho các chất ở thể khí; áp suất quy chiếu theo áp suất chuẩn 1 bar

*Ghi chú:* Áp suất riêng phần của khí i: p_i = x_i x P, trong đó x_i là phần mol và P là áp suất tổng.

<sub>`chemistry.thpt.can-bang.hang-so-can-bang-kp` · lớp 11 · #can-bang-hoa-hoc #kp #ap-suat-rieng-phan</sub>

---

**Hằng số cân bằng của phản ứng nghịch và khi nhân hệ số** — *Equilibrium constant for reverse and scaled reactions*

$$K_{nghich} = \dfrac{1}{K_{thuan}}, \quad K' = K^{p} \;\text{khi nhan he so voi } p$$

Trong đó: `K_{thuan}` là hằng số cân bằng của phản ứng thuận; `K_{nghich}` là hằng số cân bằng của phản ứng nghịch; `K'` là hằng số cân bằng của phản ứng sau khi nhân hệ số; `p` là hệ số nhân cho toàn bộ phương trình.

*Điều kiện:* Cùng nhiệt độ

*Ghi chú:* Khi cộng hai phương trình, hằng số cân bằng của phản ứng tổng bằng tích các hằng số thành phần.

<sub>`chemistry.thpt.can-bang.hang-so-can-bang-phan-ung-nghich` · lớp 11 · #hang-so-can-bang #phan-ung-nghich #can-bang-hoa-hoc</sub>

---

**Quan hệ giữa Kp và Kc** — *Relation between Kp and Kc*

$$K_{p} = K_{C} \left( RT \right)^{\Delta n}, \quad \Delta n = \sum n_{\text{khi san pham}} - \sum n_{\text{khi chat dau}}$$

Trong đó: `K_{p}` là hằng số cân bằng theo áp suất; `K_{C}` là hằng số cân bằng theo nồng độ; `R` là hằng số khí (L.bar/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `\Delta n` là độ chênh lệch tổng hệ số tỉ lượng của các chất khí.

*Điều kiện:* Khí lí tưởng; khi Kp tính theo bar và Kc tính theo mol/L thì R = 0.08314 L.bar/(mol.K)

*Ghi chú:* Nếu số mol khí hai vế bằng nhau (delta n = 0) thì Kp = Kc. Nếu dùng áp suất theo atm thì R = 0.08206 L.atm/(mol.K).

<sub>`chemistry.thpt.can-bang.quan-he-kp-kc` · lớp 11 · #kp #kc #can-bang-hoa-hoc</sub>

---

### Công thức tổng quát các dãy đồng đẳng

**Công thức tổng quát của ancol no, đa chức, mạch hở** — *General formula of saturated polyhydric alcohols*

$$C_nH_{2n+2}O_x \equiv C_nH_{2n+2-x}(OH)_x\ (2 \le x \le n)$$

Trong đó: `n` là số nguyên tử cacbon; `x` là số nhóm hiđroxyl -OH trong phân tử.

*Điều kiện:* 2 ≤ x ≤ n; mỗi nguyên tử C chỉ mang tối đa một nhóm -OH

*Ghi chú:* Etylen glicol C2H4(OH)2 (M = 62) và glixerol C3H5(OH)3 (M = 92) hòa tan Cu(OH)2 tạo dung dịch xanh lam.

<sub>`chemistry.thpt.cttq.ancol-da-chuc` · lớp 11 · #huu-co #cong-thuc-tong-quat #ancol</sub>

---

**Công thức tổng quát của ancol no, đơn chức, mạch hở** — *General formula of saturated monohydric alcohols*

$$C_nH_{2n+2}O \equiv C_nH_{2n+1}OH\ (n \ge 1)$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử ancol.

*Điều kiện:* n ≥ 1; mạch hở, no, chỉ có một nhóm -OH gắn vào nguyên tử C no

*Ghi chú:* M = 14n + 18. CH3OH (32), C2H5OH (46), C3H7OH (60), C4H9OH (74).

<sub>`chemistry.thpt.cttq.ancol-no-don-chuc` · lớp 11 · #huu-co #cong-thuc-tong-quat #ancol</sub>

---

**Công thức tổng quát của anđehit no, đơn chức, mạch hở** — *General formula of saturated monofunctional aldehydes*

$$C_nH_{2n}O \equiv C_{n-1}H_{2n-1}CHO\ (n \ge 1)$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử anđehit.

*Điều kiện:* n ≥ 1; mạch hở, no, chứa đúng một nhóm -CHO

*Ghi chú:* M = 14n + 16. HCHO (30), CH3CHO (44). Anđehit no, mạch hở, a chức có công thức CnH(2n+2-2a)Oa.

<sub>`chemistry.thpt.cttq.andehit-no-don-chuc` · lớp 11 · #huu-co #cong-thuc-tong-quat #andehit</sub>

---

**Công thức tổng quát của ete no, đơn chức, mạch hở** — *General formula of saturated ethers*

$$R-O-R' \equiv C_nH_{2n+2}O\ (n \ge 2)$$

Trong đó: `R` là gốc hiđrocacbon no thứ nhất; `R'` là gốc hiđrocacbon no thứ hai; `n` là tổng số nguyên tử cacbon.

*Điều kiện:* n ≥ 2; hai gốc no, mạch hở

*Ghi chú:* Ete là đồng phân khác chức của ancol no đơn chức; ete không tác dụng với Na.

<sub>`chemistry.thpt.cttq.ete` · lớp 11 · #huu-co #cong-thuc-tong-quat #ete</sub>

---

**Công thức tổng quát của ankađien** — *General formula of alkadienes*

$$C_nH_{2n-2}\ (n \ge 3),\quad k = 2\ (\text{2 liên kết } \pi)$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử; `k` là độ bất bão hòa, bằng 2 ứng với hai liên kết đôi.

*Điều kiện:* n ≥ 3; mạch hở, chứa hai liên kết đôi C=C

*Ghi chú:* M = 14n − 2. Buta-1,3-đien (C4H6) và isopren (2-metylbuta-1,3-đien, C5H8) là monome điều chế cao su.

<sub>`chemistry.thpt.cttq.ankadien` · lớp 11 · #huu-co #cong-thuc-tong-quat #hidrocacbon</sub>

---

**Công thức tổng quát của anken** — *General formula of alkenes*

$$C_nH_{2n}\ (n \ge 2),\quad k = 1\ (\text{1 liên kết } \pi)$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử; `k` là độ bất bão hòa, bằng 1 ứng với một liên kết đôi C=C.

*Điều kiện:* n ≥ 2; mạch hở, chứa đúng một liên kết đôi C=C

*Ghi chú:* M = 14n. Anken làm mất màu dung dịch brom và dung dịch KMnO4.

<sub>`chemistry.thpt.cttq.anken` · lớp 11 · #huu-co #cong-thuc-tong-quat #hidrocacbon</sub>

---

**Công thức tổng quát của ankin** — *General formula of alkynes*

$$C_nH_{2n-2}\ (n \ge 2),\quad k = 2\ (\text{1 liên kết ba } C \equiv C)$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử; `k` là độ bất bão hòa, bằng 2 ứng với một liên kết ba.

*Điều kiện:* n ≥ 2; mạch hở, chứa đúng một liên kết ba C≡C

*Ghi chú:* M = 14n − 2. Ankin có liên kết ba đầu mạch tạo kết tủa vàng nhạt với dung dịch AgNO3/NH3.

<sub>`chemistry.thpt.cttq.ankin` · lớp 11 · #huu-co #cong-thuc-tong-quat #hidrocacbon</sub>

---

**Công thức tổng quát của ankan** — *General formula of alkanes*

$$C_nH_{2n+2}\ (n \ge 1),\quad k = 0$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử; `k` là độ bất bão hòa của phân tử.

*Điều kiện:* n nguyên dương, n ≥ 1; mạch hở, chỉ có liên kết đơn

*Ghi chú:* M = 14n + 2. Ankan chỉ tham gia phản ứng thế, tách và cháy; không làm mất màu dung dịch brom.

<sub>`chemistry.thpt.cttq.ankan` · lớp 11 · #huu-co #cong-thuc-tong-quat #hidrocacbon</sub>

---

**Công thức tổng quát của xicloankan đơn vòng** — *General formula of monocyclic cycloalkanes*

$$C_nH_{2n}\ (n \ge 3),\quad k = 1\ (\text{1 vòng})$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử; `k` là độ bất bão hòa (ở đây là 1 vòng no).

*Điều kiện:* n ≥ 3; phân tử chỉ có một vòng no, không có liên kết bội

*Ghi chú:* M = 14n. Xicloankan đồng phân với anken cùng số C nhưng không làm mất màu dung dịch brom (trừ vòng 3, 4 cạnh mở vòng).

<sub>`chemistry.thpt.cttq.xicloankan` · lớp 11 · #huu-co #cong-thuc-tong-quat #hidrocacbon</sub>

---

**Công thức tổng quát của aren (đồng đẳng benzen)** — *General formula of arenes*

$$C_nH_{2n-6}\ (n \ge 6),\quad k = 4$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử; `k` là độ bất bão hòa, bằng 4 (1 vòng benzen + 3 liên kết pi).

*Điều kiện:* n ≥ 6; phân tử chứa một vòng benzen, nhánh no

*Ghi chú:* M = 14n − 6. Benzen C6H6, toluen C7H8, xilen và etylbenzen C8H10.

<sub>`chemistry.thpt.cttq.aren` · lớp 11 · #huu-co #cong-thuc-tong-quat #aren</sub>

---

**Công thức của phenol và đồng đẳng** — *Formula of phenol and its homologues*

$$C_6H_5OH;\quad \text{đồng đẳng đơn chức}: C_nH_{2n-6}O\ (n \ge 6)$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử.

*Điều kiện:* Nhóm -OH gắn trực tiếp vào vòng benzen

*Ghi chú:* M(C6H5OH) = 94 g/mol. Phenol tác dụng được với NaOH (khác ancol) và tạo kết tủa trắng với nước brom.

<sub>`chemistry.thpt.cttq.phenol` · lớp 11 · #huu-co #cong-thuc-tong-quat #phenol</sub>

---

**Công thức tổng quát của xeton no, đơn chức, mạch hở** — *General formula of saturated ketones*

$$R-CO-R' \equiv C_nH_{2n}O\ (n \ge 3)$$

Trong đó: `R` là gốc hiđrocacbon no thứ nhất; `R'` là gốc hiđrocacbon no thứ hai; `n` là số nguyên tử cacbon trong phân tử.

*Điều kiện:* n ≥ 3; nhóm C=O nằm giữa mạch, hai bên đều là gốc hiđrocacbon

*Ghi chú:* Xeton là đồng phân của anđehit cùng công thức phân tử nhưng KHÔNG tham gia phản ứng tráng bạc.

<sub>`chemistry.thpt.cttq.xeton` · lớp 11 · #huu-co #cong-thuc-tong-quat #xeton</sub>

---

### Dung dịch

**Nồng độ ion trong dung dịch chất điện li mạnh** — *Ion concentration for a strong electrolyte*

$$\left[ M^{n+} \right] = x \cdot C_{M}, \quad \left[ X^{m-} \right] = y \cdot C_{M}$$

Trong đó: `\left[ M^{n+} \right]` là nồng độ ion dương (mol/L); `\left[ X^{m-} \right]` là nồng độ ion âm (mol/L); `x` là chỉ số ion dương trong công thức M_xX_y; `y` là chỉ số ion âm trong công thức M_xX_y; `C_{M}` là nồng độ mol của chất điện li (mol/L).

*Điều kiện:* Chất điện li mạnh, phân li hoàn toàn (alpha = 1)

*Ghi chú:* Ví dụ dung dịch Al2(SO4)3 0.1 M có [Al3+] = 0.2 M và [SO4 2-] = 0.3 M.

<sub>`chemistry.thpt.dung-dich.nong-do-ion-chat-dien-li-manh` · lớp 11 · #dien-li #nong-do-ion #thpt</sub>

---

### Dung dịch chất điện li

**pH và pOH của dung dịch** — *pH and pOH of a solution*

$$pH = -\log[H^+];\quad pOH = -\log[OH^-];\quad pH + pOH = 14$$

Trong đó: `pH` là chỉ số pH của dung dịch; `pOH` là chỉ số pOH của dung dịch; `[H^+]` là nồng độ mol ion H+ (mol/L); `[OH^-]` là nồng độ mol ion OH- (mol/L).

*Điều kiện:* Dung dịch loãng ở 25 °C, tích số ion của nước Kw = [H+][OH-] = 1,0·10^-14

*Ghi chú:* pH < 7 môi trường axit, pH = 7 trung tính, pH > 7 môi trường bazơ (ở 25 °C).

<sub>`chemistry.thpt.dung-dich.ph-dung-dich` · lớp 11 · #vo-co #dung-dich #ph</sub>

---

### Lập công thức phân tử hợp chất hữu cơ

**Từ công thức đơn giản nhất suy ra công thức phân tử** — *Molecular formula from the empirical formula*

$$CTPT = \left(CTDGN\right)_m,\quad m = \dfrac{M}{M_{CTDGN}}$$

Trong đó: `m` là hệ số nguyên dương nhân với công thức đơn giản nhất; `M` là khối lượng mol phân tử của hợp chất (g/mol); `M_{CTDGN}` là khối lượng mol ứng với công thức đơn giản nhất (g/mol).

*Điều kiện:* m là số nguyên dương; cần biết M từ tỉ khối hoặc từ dữ kiện khác

*Ghi chú:* Kiểm tra lại kết quả bằng độ bất bão hòa k phải nguyên và không âm.

<sub>`chemistry.thpt.huu-co.ctdgn-sang-ctpt` · lớp 11 · #huu-co #lap-cong-thuc #cong-thuc-don-gian</sub>

---

**Lập công thức đơn giản nhất từ phần trăm khối lượng các nguyên tố** — *Empirical formula from mass percentages*

$$x : y : z : t = \dfrac{\%C}{12} : \dfrac{\%H}{1} : \dfrac{\%O}{16} : \dfrac{\%N}{14}$$

Trong đó: `x` là chỉ số nguyên tử C trong công thức đơn giản nhất; `y` là chỉ số nguyên tử H; `z` là chỉ số nguyên tử O; `t` là chỉ số nguyên tử N; `\%C` là phần trăm khối lượng cacbon (%); `\%H` là phần trăm khối lượng hiđro (%); `\%O` là phần trăm khối lượng oxi (%); `\%N` là phần trăm khối lượng nitơ (%).

*Điều kiện:* Tỉ lệ phải rút gọn về các số nguyên nhỏ nhất; %O = 100% − %C − %H − %N

*Ghi chú:* Có thể thay % khối lượng bằng khối lượng thực của mỗi nguyên tố trong cùng một lượng chất.

<sub>`chemistry.thpt.huu-co.lap-ctpt-tu-phan-tram` · lớp 11 · #huu-co #lap-cong-thuc #cong-thuc-don-gian</sub>

---

**Xác định số nguyên tử mỗi nguyên tố từ sản phẩm cháy** — *Element amounts from combustion products*

$$n_{C} = n_{CO_2},\quad n_{H} = 2n_{H_2O},\quad n_{N} = 2n_{N_2},\quad m_{O} = m_X - 12n_{CO_2} - 2n_{H_2O} - 28n_{N_2}$$

Trong đó: `n_{C}` là số mol nguyên tử C trong hợp chất X (mol); `n_{H}` là số mol nguyên tử H trong X (mol); `n_{N}` là số mol nguyên tử N trong X (mol); `m_{O}` là khối lượng oxi trong X (g); `m_X` là khối lượng hợp chất hữu cơ X đem đốt (g); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{N_2}` là số mol N2 sinh ra (mol).

*Điều kiện:* Đốt cháy hoàn toàn X trong oxi dư; toàn bộ C thành CO2, H thành H2O, N thành N2

*Ghi chú:* Nếu m(O) = 0 thì X chỉ chứa C, H (và N). Sau đó n(O) = m(O)/16.

<sub>`chemistry.thpt.huu-co.lap-ctpt-tu-san-pham-chay` · lớp 11 · #huu-co #lap-cong-thuc #dot-chay</sub>

---

**Số nguyên tử C, H, O trong phân tử theo số mol chất** — *Atoms per molecule from mole ratios*

$$x = \dfrac{n_{CO_2}}{n_X},\quad y = \dfrac{2n_{H_2O}}{n_X},\quad z = \dfrac{n_{O(X)}}{n_X}$$

Trong đó: `x` là số nguyên tử C trong một phân tử X; `y` là số nguyên tử H trong một phân tử X; `z` là số nguyên tử O trong một phân tử X; `n_X` là số mol hợp chất X đem đốt (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{O(X)}` là số mol nguyên tử oxi trong X (mol).

*Điều kiện:* X là chất tinh khiết (không phải hỗn hợp); x, y, z nguyên dương

*Ghi chú:* Nếu X là hỗn hợp thì các giá trị này trở thành số nguyên tử trung bình.

<sub>`chemistry.thpt.huu-co.so-nguyen-tu-tu-so-mol` · lớp 11 · #huu-co #lap-cong-thuc #dot-chay</sub>

---

### Phân bón hóa học

**Độ dinh dưỡng của phân kali** — *Nutrient content of potassium fertilizer*

$$\%K_2O = \dfrac{m_{K_2O}}{m_{phan}} \times 100\%,\quad n_{K_2O} = \dfrac{n_{K}}{2}$$

Trong đó: `\%K_2O` là độ dinh dưỡng của phân kali (%); `m_{K_2O}` là khối lượng K2O quy đổi từ toàn bộ kali trong phân (g); `m_{phan}` là khối lượng phân bón (g); `n_{K_2O}` là số mol K2O quy đổi (mol); `n_{K}` là số mol nguyên tử kali trong phân (mol).

*Điều kiện:* Quy đổi toàn bộ K trong phân về K2O

*Ghi chú:* M(K2O) = 94 g/mol. Phân kali phổ biến: KCl, K2SO4.

<sub>`chemistry.thpt.phan-bon.do-dinh-duong-kali` · lớp 11 · #vo-co #phan-bon #kali</sub>

---

**Độ dinh dưỡng của phân lân** — *Nutrient content of phosphate fertilizer*

$$\%P_2O_5 = \dfrac{m_{P_2O_5}}{m_{phan}} \times 100\%,\quad n_{P_2O_5} = \dfrac{n_{P}}{2}$$

Trong đó: `\%P_2O_5` là độ dinh dưỡng của phân lân (%); `m_{P_2O_5}` là khối lượng P2O5 quy đổi từ toàn bộ photpho trong phân (g); `m_{phan}` là khối lượng phân bón (g); `n_{P_2O_5}` là số mol P2O5 quy đổi (mol); `n_{P}` là số mol nguyên tử photpho trong phân (mol).

*Điều kiện:* Toàn bộ P trong phân được quy đổi về P2O5 dù thực tế tồn tại dưới dạng muối photphat

*Ghi chú:* M(P2O5) = 142 g/mol. Supephotphat kép Ca(H2PO4)2 có độ dinh dưỡng cao hơn supephotphat đơn.

<sub>`chemistry.thpt.phan-bon.do-dinh-duong-lan` · lớp 11 · #vo-co #phan-bon #lan</sub>

---

**Độ dinh dưỡng của phân đạm** — *Nutrient content of nitrogen fertilizer*

$$\%N = \dfrac{m_{N}}{m_{phan}} \times 100\%$$

Trong đó: `\%N` là độ dinh dưỡng của phân đạm (%); `m_{N}` là khối lượng nguyên tố nitơ trong phân (g); `m_{phan}` là khối lượng phân bón (g).

*Điều kiện:* Độ dinh dưỡng của phân đạm được đánh giá bằng phần trăm khối lượng nitơ

*Ghi chú:* Urê (NH2)2CO có %N ≈ 46,67% là phân đạm tốt nhất; NH4NO3 có %N = 35%.

<sub>`chemistry.thpt.phan-bon.do-dinh-duong-dam` · lớp 11 · #vo-co #phan-bon #dam</sub>

---

### Phản ứng đặc trưng của hợp chất hữu cơ

**Phản ứng thế của ank-1-in với dung dịch AgNO3/NH3** — *Terminal alkynes reacting with silver ammonia solution*

$$R-C \equiv CH + AgNO_3 + NH_3 \rightarrow R-C \equiv CAg \downarrow + NH_4NO_3$$

Trong đó: `R` là gốc hiđrocacbon hoặc H; `R-C \equiv CAg` là kết tủa vàng nhạt của bạc axetilua thế.

*Điều kiện:* Chỉ ank-1-in (liên kết ba ở đầu mạch) mới phản ứng; ank-2-in trở đi không phản ứng

*Ghi chú:* Axetilen C2H2 có hai đầu mạch nên tạo Ag2C2 (M = 240), n(kết tủa) = n(C2H2). Với R-C≡CH khác thì M(kết tủa) = M(ankin) + 107.

<sub>`chemistry.thpt.phan-ung.ankin-agno3` · lớp 11 · #huu-co #ankin #nhan-biet</sub>

---

**Phản ứng cracking ankan** — *Cracking of alkanes*

$$C_nH_{2n+2} \xrightarrow{t^o,\ xt} C_aH_{2a} + C_bH_{2b+2}\ (a + b = n);\quad m_{truoc} = m_{sau},\ \ n_{ankan\ pu} = n_{sau} - n_{truoc}$$

Trong đó: `n` là số nguyên tử cacbon của ankan ban đầu; `a` là số nguyên tử cacbon của anken tạo thành; `b` là số nguyên tử cacbon của ankan tạo thành; `m_{truoc}` là khối lượng hỗn hợp khí trước phản ứng (g); `m_{sau}` là khối lượng hỗn hợp khí sau phản ứng (g); `n_{truoc}` là tổng số mol khí trước phản ứng (mol); `n_{sau}` là tổng số mol khí sau phản ứng (mol); `n_{ankan\ pu}` là số mol ankan đã bị cracking (mol).

*Điều kiện:* Mỗi phân tử ankan bị cracking tạo đúng hai phân tử nên số mol khí tăng; khối lượng hỗn hợp không đổi (bình kín)

*Ghi chú:* Từ bảo toàn khối lượng: n(trước)·M(trước) = n(sau)·M(sau), nên M trung bình giảm sau cracking. Hiệu suất cracking H = (n_sau − n_trước)/n_trước × 100%.

<sub>`chemistry.thpt.phan-ung.cracking-ankan` · lớp 11 · #huu-co #ankan #cracking #bao-toan-khoi-luong</sub>

---

**Oxi hóa ancol bằng CuO nung nóng** — *Oxidation of alcohols by hot copper(II) oxide*

$$RCH_2OH + CuO \xrightarrow{t^o} RCHO + Cu + H_2O;\quad m_{ran\ giam} = 16\,n_{ancol\ pu}$$

Trong đó: `m_{ran\ giam}` là độ giảm khối lượng chất rắn sau phản ứng (g); `n_{ancol\ pu}` là số mol ancol đã bị oxi hóa (mol); `R` là gốc hiđrocacbon hoặc H.

*Điều kiện:* CuO dư, đun nóng; mỗi mol ancol lấy đi 1 mol nguyên tử O của CuO

*Ghi chú:* Ancol bậc I tạo anđehit, ancol bậc II tạo xeton, ancol bậc III không bị oxi hóa trong điều kiện này.

<sub>`chemistry.thpt.phan-ung.oxi-hoa-ancol-cuo` · lớp 11 · #huu-co #ancol #oxi-hoa</sub>

---

**Phản ứng thế brom vào vòng benzen của phenol** — *Bromination of phenol*

$$C_6H_5OH + 3Br_2 \rightarrow C_6H_2Br_3OH \downarrow + 3HBr;\quad n_{Br_2} = 3n_{phenol},\ \ n_{\downarrow} = n_{phenol}$$

Trong đó: `n_{Br_2}` là số mol brom phản ứng (mol); `n_{phenol}` là số mol phenol (mol); `n_{\downarrow}` là số mol kết tủa 2,4,6-tribromphenol (mol).

*Điều kiện:* Dùng nước brom ở nhiệt độ thường, không cần xúc tác; nhóm -OH hoạt hóa vòng benzen và định hướng vào vị trí ortho, para

*Ghi chú:* Kết tủa trắng 2,4,6-tribromphenol có M = 331 g/mol. Benzen và toluen không phản ứng với nước brom, nên đây là phản ứng nhận biết phenol.

<sub>`chemistry.thpt.phan-ung.phenol-tac-dung-brom` · lớp 11 · #huu-co #phenol #nhan-biet</sub>

---

**Ancol tác dụng với natri** — *Alcohols reacting with sodium*

$$n_{H_2} = \dfrac{a \cdot n_{ancol}}{2} = \dfrac{n_{OH}}{2};\quad m_{muoi} = m_{ancol} + 22n_{OH}$$

Trong đó: `n_{H_2}` là số mol khí H2 thoát ra (mol); `a` là số nhóm -OH trong một phân tử ancol; `n_{ancol}` là số mol ancol (mol); `n_{OH}` là tổng số mol nhóm -OH (mol); `m_{muoi}` là khối lượng ancolat (muối natri) khan (g); `m_{ancol}` là khối lượng ancol ban đầu (g).

*Điều kiện:* Na dư; ancol khan (nếu có nước thì nước cũng phản ứng với Na)

*Ghi chú:* 22 = 23 − 1 (thay H của nhóm OH bằng Na). Tỉ lệ n(H2)/n(ancol) = 0,5 cho biết ancol đơn chức, = 1 cho biết ancol hai chức.

<sub>`chemistry.thpt.phan-ung.ancol-tac-dung-na` · lớp 11 · #huu-co #ancol #phan-ung-the</sub>

---

**Tách nước ancol tạo anken ở 170 độ C** — *Dehydration of alcohols to alkenes at 170 degrees Celsius*

$$C_nH_{2n+1}OH \xrightarrow[170^oC]{H_2SO_4\ dac} C_nH_{2n} + H_2O;\quad n_{anken} = n_{H_2O} = n_{ancol\ pu}$$

Trong đó: `n` là số nguyên tử cacbon của ancol (n ≥ 2); `n_{anken}` là số mol anken tạo thành (mol); `n_{H_2O}` là số mol nước sinh ra (mol); `n_{ancol\ pu}` là số mol ancol đã phản ứng (mol).

*Điều kiện:* Ancol no đơn chức mạch hở có từ 2 C trở lên; H2SO4 đặc, khoảng 170 °C

*Ghi chú:* Theo quy tắc Zai-xép, nhóm -OH tách cùng H ở nguyên tử C bậc cao hơn tạo anken chính.

<sub>`chemistry.thpt.phan-ung.tach-nuoc-tao-anken` · lớp 11 · #huu-co #ancol #tach-nuoc</sub>

---

**Tách nước ancol tạo ete ở 140 độ C** — *Dehydration of alcohols to ethers at 140 degrees Celsius*

$$2ROH \xrightarrow[140^oC]{H_2SO_4\ dac} ROR + H_2O;\quad n_{H_2O} = n_{ete} = \dfrac{n_{ancol}}{2},\ \ m_{ancol} = m_{ete} + m_{H_2O}$$

Trong đó: `n_{H_2O}` là số mol nước sinh ra (mol); `n_{ete}` là tổng số mol ete tạo thành (mol); `n_{ancol}` là số mol ancol đã phản ứng (mol); `m_{ancol}` là khối lượng ancol phản ứng (g); `m_{ete}` là khối lượng ete thu được (g); `m_{H_2O}` là khối lượng nước sinh ra (g); `R` là gốc hiđrocacbon.

*Điều kiện:* Ancol no đơn chức, H2SO4 đặc, nhiệt độ khoảng 140 °C

*Ghi chú:* Từ n ancol khác nhau tách nước thu được tối đa n(n+1)/2 ete. Nếu các ete có số mol bằng nhau thì các ancol cũng có số mol bằng nhau.

<sub>`chemistry.thpt.phan-ung.tach-nuoc-tao-ete` · lớp 11 · #huu-co #ancol #tach-nuoc</sub>

---

### Sự điện li

**Phương trình Henderson - Hasselbalch cho dung dịch đệm** — *Henderson-Hasselbalch equation*

$$\mathrm{pH} = \mathrm{p}K_{a} + \log \dfrac{\left[ \mathrm{A^{-}} \right]}{\left[ \mathrm{HA} \right]}$$

Trong đó: `\mathrm{pH}` là pH của dung dịch đệm; `\mathrm{p}K_{a}` là chỉ số acid của acid yếu; `\left[ \mathrm{A^{-}} \right]` là nồng độ base liên hợp (muối) (mol/L); `\left[ \mathrm{HA} \right]` là nồng độ acid yếu (mol/L).

*Điều kiện:* Hệ đệm gồm acid yếu và base liên hợp có nồng độ tương đương nhau (tỉ lệ trong khoảng 0.1 đến 10)

*Ghi chú:* Khi [A-] = [HA] thì pH = pKa, dung dịch đệm có khả năng đệm tốt nhất. Ví dụ hệ đệm CH3COOH/CH3COONa.

<sub>`chemistry.thpt.dien-li.ph-dung-dich-dem` · lớp 11 · #dung-dich-dem #henderson-hasselbalch #ph</sub>

---

**pOH của dung dịch đệm base yếu và muối** — *Henderson-Hasselbalch equation for a basic buffer*

$$\mathrm{pOH} = \mathrm{p}K_{b} + \log \dfrac{\left[ \mathrm{BH^{+}} \right]}{\left[ \mathrm{B} \right]}$$

Trong đó: `\mathrm{pOH}` là chỉ số pOH của dung dịch đệm; `\mathrm{p}K_{b}` là chỉ số base; `\left[ \mathrm{BH^{+}} \right]` là nồng độ acid liên hợp (muối) (mol/L); `\left[ \mathrm{B} \right]` là nồng độ base yếu (mol/L).

*Điều kiện:* Hệ đệm base yếu - muối của nó, ví dụ NH3 và NH4Cl

*Ghi chú:* Sau khi tính pOH, suy ra pH = 14 - pOH ở 25 độ C.

<sub>`chemistry.thpt.dien-li.ph-dung-dich-dem-base` · lớp 11 · #dung-dich-dem #poh #base-yeu</sub>

---

**Hằng số phân li acid** — *Acid dissociation constant*

$$\mathrm{HA} \rightleftharpoons \mathrm{H^{+}} + \mathrm{A^{-}}, \quad K_{a} = \dfrac{\left[ \mathrm{H^{+}} \right] \left[ \mathrm{A^{-}} \right]}{\left[ \mathrm{HA} \right]}$$

Trong đó: `K_{a}` là hằng số phân li acid; `\left[ \mathrm{H^{+}} \right]` là nồng độ cân bằng của ion H+ (mol/L); `\left[ \mathrm{A^{-}} \right]` là nồng độ cân bằng của base liên hợp (mol/L); `\left[ \mathrm{HA} \right]` là nồng độ cân bằng của acid chưa phân li (mol/L).

*Điều kiện:* Dung dịch loãng, acid yếu, ở nhiệt độ xác định (thường 25 độ C)

*Ghi chú:* Ka càng lớn thì acid càng mạnh. Ví dụ CH3COOH có Ka = 1.75e-5 ở 25 độ C.

<sub>`chemistry.thpt.dien-li.hang-so-phan-li-acid` · lớp 11 · #ka #acid-yeu #dien-li</sub>

---

**Hằng số phân li base** — *Base dissociation constant*

$$\mathrm{B} + \mathrm{H_{2}O} \rightleftharpoons \mathrm{BH^{+}} + \mathrm{OH^{-}}, \quad K_{b} = \dfrac{\left[ \mathrm{BH^{+}} \right] \left[ \mathrm{OH^{-}} \right]}{\left[ \mathrm{B} \right]}$$

Trong đó: `K_{b}` là hằng số phân li base; `\left[ \mathrm{BH^{+}} \right]` là nồng độ acid liên hợp (mol/L); `\left[ \mathrm{OH^{-}} \right]` là nồng độ ion hydroxide (mol/L); `\left[ \mathrm{B} \right]` là nồng độ base chưa phản ứng (mol/L).

*Điều kiện:* Dung dịch loãng, base yếu, nhiệt độ xác định

*Ghi chú:* Nồng độ nước được coi là hằng số nên không xuất hiện trong biểu thức Kb. NH3 có Kb = 1.8e-5 ở 25 độ C.

<sub>`chemistry.thpt.dien-li.hang-so-phan-li-base` · lớp 11 · #kb #base-yeu #dien-li</sub>

---

**Giá trị pKa và pKb** — *pKa and pKb*

$$\mathrm{p}K_{a} = -\log K_{a}, \quad \mathrm{p}K_{b} = -\log K_{b}$$

Trong đó: `\mathrm{p}K_{a}` là chỉ số acid; `K_{a}` là hằng số phân li acid; `\mathrm{p}K_{b}` là chỉ số base; `K_{b}` là hằng số phân li base.

*Điều kiện:* Ka, Kb dương

*Ghi chú:* pKa càng nhỏ thì acid càng mạnh. CH3COOH có pKa khoảng 4.76.

<sub>`chemistry.thpt.dien-li.pka` · lớp 11 · #pka #pkb #dien-li</sub>

---

**Quan hệ giữa Ka và Kb của cặp acid - base liên hợp** — *Relation between Ka and Kb of a conjugate pair*

$$K_{a} \cdot K_{b} = K_{w} = 1.0 \times 10^{-14}, \quad \mathrm{p}K_{a} + \mathrm{p}K_{b} = 14$$

Trong đó: `K_{a}` là hằng số phân li của acid; `K_{b}` là hằng số phân li của base liên hợp; `K_{w}` là tích số ion của nước; `\mathrm{p}K_{a}` là âm logarit thập phân của Ka; `\mathrm{p}K_{b}` là âm logarit thập phân của Kb.

*Điều kiện:* Cặp acid - base liên hợp, ở 25 độ C

*Ghi chú:* Acid càng mạnh thì base liên hợp càng yếu và ngược lại.

<sub>`chemistry.thpt.dien-li.quan-he-ka-kb-kw` · lớp 11 · #ka #kb #acid-base-lien-hop</sub>

---

**pH của dung dịch sau khi trộn acid mạnh với base mạnh** — *pH after mixing a strong acid with a strong base*

$$\left[ \mathrm{H^{+}} \right]_{du} = \dfrac{n_{\mathrm{H^{+}}} - n_{\mathrm{OH^{-}}}}{V_{1} + V_{2}}, \quad \left[ \mathrm{OH^{-}} \right]_{du} = \dfrac{n_{\mathrm{OH^{-}}} - n_{\mathrm{H^{+}}}}{V_{1} + V_{2}}$$

Trong đó: `\left[ \mathrm{H^{+}} \right]_{du}` là nồng độ ion H+ dư sau phản ứng (mol/L); `\left[ \mathrm{OH^{-}} \right]_{du}` là nồng độ ion OH- dư sau phản ứng (mol/L); `n_{\mathrm{H^{+}}}` là số mol H+ ban đầu (mol); `n_{\mathrm{OH^{-}}}` là số mol OH- ban đầu (mol); `V_{1}` là thể tích hai dung dịch đem trộn (L); `V_{2}` là thể tích hai dung dịch đem trộn (L).

*Điều kiện:* Acid mạnh và base mạnh; coi thể tích cộng tính; nếu hai số mol bằng nhau thì pH = 7 ở 25 độ C

*Ghi chú:* Sau khi có nồng độ ion dư, dùng pH = -log[H+] hoặc pH = 14 + log[OH-].

<sub>`chemistry.thpt.dien-li.ph-sau-khi-tron-acid-base-manh` · lớp 11 · #ph #trung-hoa #tron-dung-dich</sub>

---

**Điều kiện trung hòa acid - base** — *Acid-base neutralization condition*

$$n_{\mathrm{H^{+}}} = n_{\mathrm{OH^{-}}} \;\Leftrightarrow\; C_{a}V_{a} \cdot k_{a} = C_{b}V_{b} \cdot k_{b}$$

Trong đó: `n_{\mathrm{H^{+}}}` là số mol ion H+ (mol); `n_{\mathrm{OH^{-}}}` là số mol ion OH- (mol); `C_{a}` là nồng độ acid (mol/L); `V_{a}` là thể tích dung dịch acid (L); `k_{a}` là số ion H+ do một phân tử acid phân li; `C_{b}` là nồng độ base (mol/L); `V_{b}` là thể tích dung dịch base (L); `k_{b}` là số ion OH- do một phân tử base phân li.

*Điều kiện:* Phản ứng trung hòa hoàn toàn; đây là công thức nền của phép chuẩn độ acid - base

*Ghi chú:* Phương trình ion rút gọn: H+ + OH- -> H2O. Nếu H+ dư thì pH tính theo số mol H+ dư chia tổng thể tích.

<sub>`chemistry.thpt.dien-li.phan-ung-trung-hoa` · lớp 11 · #trung-hoa #chuan-do #dien-li</sub>

---

**pH dung dịch muối của acid yếu và base mạnh** — *pH of a salt of a weak acid and strong base*

$$\mathrm{pH} \approx 7 + \dfrac{1}{2}\left( \mathrm{p}K_{a} + \log C \right)$$

Trong đó: `\mathrm{pH}` là pH của dung dịch muối; `\mathrm{p}K_{a}` là chỉ số acid của acid yếu tương ứng; `C` là nồng độ mol của muối (mol/L).

*Điều kiện:* Muối tan hoàn toàn, anion thủy phân yếu, ở 25 độ C

*Ghi chú:* Dung dịch có môi trường base (pH > 7). Ví dụ CH3COONa, Na2CO3.

<sub>`chemistry.thpt.dien-li.ph-muoi-cua-acid-yeu` · lớp 11 · #thuy-phan-muoi #ph #muoi</sub>

---

**pH dung dịch muối của base yếu và acid mạnh** — *pH of a salt of a weak base and strong acid*

$$\mathrm{pH} \approx 7 - \dfrac{1}{2}\left( \mathrm{p}K_{b} + \log C \right)$$

Trong đó: `\mathrm{pH}` là pH của dung dịch muối; `\mathrm{p}K_{b}` là chỉ số base của base yếu tương ứng; `C` là nồng độ mol của muối (mol/L).

*Điều kiện:* Muối tan hoàn toàn, cation thủy phân yếu, ở 25 độ C

*Ghi chú:* Dung dịch có môi trường acid (pH < 7). Ví dụ NH4Cl, AlCl3, FeCl3.

<sub>`chemistry.thpt.dien-li.ph-muoi-cua-base-yeu` · lớp 11 · #thuy-phan-muoi #ph #muoi</sub>

---

**Điều kiện tạo thành kết tủa** — *Precipitation condition*

$$Q_{sp} = \left[ \mathrm{M}^{y+} \right]^{x} \left[ \mathrm{X}^{x-} \right]^{y} : \begin{cases} Q_{sp} > K_{sp} & \text{co ket tua} \\ Q_{sp} = K_{sp} & \text{dung dich bao hoa} \\ Q_{sp} < K_{sp} & \text{khong ket tua} \end{cases}$$

Trong đó: `Q_{sp}` là tích ion tại thời điểm đang xét; `K_{sp}` là tích số tan; `\left[ \mathrm{M}^{y+} \right]` là nồng độ cation sau khi trộn (mol/L); `\left[ \mathrm{X}^{x-} \right]` là nồng độ anion sau khi trộn (mol/L).

*Điều kiện:* Nồng độ ion phải tính sau khi pha trộn (đã kể đến sự pha loãng)

*Ghi chú:* Hiệu ứng ion chung: thêm ion cùng loại làm giảm độ tan của chất kết tủa.

<sub>`chemistry.thpt.dien-li.dieu-kien-ket-tua` · lớp 11 · #ket-tua #ksp #dien-li</sub>

---

**Độ tan mol tính từ tích số tan** — *Molar solubility from Ksp*

$$K_{sp} = x^{x} y^{y} s^{x+y} \;\Rightarrow\; s = \sqrt[x+y]{\dfrac{K_{sp}}{x^{x} y^{y}}}$$

Trong đó: `K_{sp}` là tích số tan của MxXy; `s` là độ tan mol của chất trong nước nguyên chất (mol/L); `x` là chỉ số của cation và anion trong công thức; `y` là chỉ số của cation và anion trong công thức.

*Điều kiện:* Dung dịch bão hòa trong nước nguyên chất; bỏ qua thủy phân của ion

*Ghi chú:* Với AB (x = y = 1): s = căn bậc hai của Ksp. Với AB2 hoặc A2B: s = căn bậc ba của (Ksp/4).

<sub>`chemistry.thpt.dien-li.do-tan-tu-tich-so-tan` · lớp 11 · #tich-so-tan #do-tan #ksp</sub>

---

**Tích số tan của chất điện li ít tan** — *Solubility product*

$$\mathrm{M}_{x}\mathrm{X}_{y}(s) \rightleftharpoons x\mathrm{M}^{y+} + y\mathrm{X}^{x-}, \quad K_{sp} = \left[ \mathrm{M}^{y+} \right]^{x} \left[ \mathrm{X}^{x-} \right]^{y}$$

Trong đó: `K_{sp}` là tích số tan; `\left[ \mathrm{M}^{y+} \right]` là nồng độ cation ở trạng thái bão hòa (mol/L); `\left[ \mathrm{X}^{x-} \right]` là nồng độ anion ở trạng thái bão hòa (mol/L); `x` là chỉ số trong công thức của chất ít tan; `y` là chỉ số trong công thức của chất ít tan.

*Điều kiện:* Dung dịch bão hòa có mặt chất rắn ít tan; ở nhiệt độ xác định

*Ghi chú:* Ksp càng nhỏ thì chất càng khó tan. Chất rắn nguyên chất không xuất hiện trong biểu thức.

<sub>`chemistry.thpt.dien-li.tich-so-tan` · lớp 11 · #tich-so-tan #ksp #ket-tua</sub>

---

**pH của dung dịch acid mạnh** — *pH of a strong acid solution*

$$\left[ \mathrm{H^{+}} \right] = k \cdot C_{a} \;\Rightarrow\; \mathrm{pH} = -\log \left( k \cdot C_{a} \right)$$

Trong đó: `\left[ \mathrm{H^{+}} \right]` là nồng độ ion H+ (mol/L); `k` là số ion H+ mà một phân tử acid phân li ra; `C_{a}` là nồng độ mol của acid (mol/L).

*Điều kiện:* Acid mạnh phân li hoàn toàn; C_a không quá loãng (lớn hơn khoảng 1e-6 mol/L)

*Ghi chú:* Ví dụ HCl 0.01 M có pH = 2; H2SO4 0.005 M có [H+] = 0.01 M nên pH = 2.

<sub>`chemistry.thpt.dien-li.ph-cua-acid-manh` · lớp 11 · #ph #acid-manh #dien-li</sub>

---

**pH của dung dịch acid yếu đơn chức** — *pH of a weak monoprotic acid*

$$\left[ \mathrm{H^{+}} \right] \approx \sqrt{K_{a} C_{a}} \;\Rightarrow\; \mathrm{pH} \approx \dfrac{1}{2}\left( \mathrm{p}K_{a} - \log C_{a} \right)$$

Trong đó: `\left[ \mathrm{H^{+}} \right]` là nồng độ ion H+ ở cân bằng (mol/L); `K_{a}` là hằng số phân li acid; `C_{a}` là nồng độ ban đầu của acid (mol/L); `\mathrm{p}K_{a}` là chỉ số acid.

*Điều kiện:* Acid yếu đơn chức, độ điện li nhỏ (alpha dưới khoảng 5%), bỏ qua sự điện li của nước

*Ghi chú:* Công thức gần đúng do coi [HA] ở cân bằng xấp xỉ C_a. Khi Ka lớn hoặc dung dịch quá loãng phải giải phương trình bậc hai.

<sub>`chemistry.thpt.dien-li.ph-cua-acid-yeu` · lớp 11 · #ph #acid-yeu #ka</sub>

---

**pH của dung dịch base mạnh** — *pH of a strong base solution*

$$\left[ \mathrm{OH^{-}} \right] = k \cdot C_{b} \;\Rightarrow\; \mathrm{pH} = 14 + \log \left( k \cdot C_{b} \right)$$

Trong đó: `\left[ \mathrm{OH^{-}} \right]` là nồng độ ion OH- (mol/L); `k` là số ion OH- mà một phân tử base phân li ra; `C_{b}` là nồng độ mol của base (mol/L).

*Điều kiện:* Base mạnh phân li hoàn toàn; ở 25 độ C

*Ghi chú:* Ví dụ NaOH 0.01 M có pOH = 2 nên pH = 12; Ba(OH)2 0.005 M cũng cho pH = 12.

<sub>`chemistry.thpt.dien-li.ph-cua-base-manh` · lớp 11 · #ph #base-manh #dien-li</sub>

---

**pH của dung dịch base yếu** — *pH of a weak base*

$$\left[ \mathrm{OH^{-}} \right] \approx \sqrt{K_{b} C_{b}} \;\Rightarrow\; \mathrm{pH} \approx 14 - \dfrac{1}{2}\left( \mathrm{p}K_{b} - \log C_{b} \right)$$

Trong đó: `\left[ \mathrm{OH^{-}} \right]` là nồng độ ion OH- ở cân bằng (mol/L); `K_{b}` là hằng số phân li base; `C_{b}` là nồng độ ban đầu của base (mol/L); `\mathrm{p}K_{b}` là chỉ số base.

*Điều kiện:* Base yếu, độ điện li nhỏ, ở 25 độ C

*Ghi chú:* Tương đương pOH = (pKb - logC_b)/2 rồi lấy pH = 14 - pOH.

<sub>`chemistry.thpt.dien-li.ph-cua-base-yeu` · lớp 11 · #ph #base-yeu #kb</sub>

---

**Định nghĩa pH** — *Definition of pH*

$$\mathrm{pH} = -\log \left[ \mathrm{H^{+}} \right] \;\Leftrightarrow\; \left[ \mathrm{H^{+}} \right] = 10^{-\mathrm{pH}}$$

Trong đó: `\mathrm{pH}` là chỉ số pH của dung dịch; `\left[ \mathrm{H^{+}} \right]` là nồng độ ion H+ (hay H3O+) (mol/L).

*Điều kiện:* Dung dịch loãng; logarit cơ số 10

*Ghi chú:* Ở 25 độ C: pH < 7 môi trường acid, pH = 7 trung tính, pH > 7 môi trường base.

<sub>`chemistry.thpt.dien-li.ph-cua-dung-dich` · lớp 11 · #ph #dien-li #thpt</sub>

---

**Định nghĩa pOH** — *Definition of pOH*

$$\mathrm{pOH} = -\log \left[ \mathrm{OH^{-}} \right] \;\Leftrightarrow\; \left[ \mathrm{OH^{-}} \right] = 10^{-\mathrm{pOH}}$$

Trong đó: `\mathrm{pOH}` là chỉ số pOH của dung dịch; `\left[ \mathrm{OH^{-}} \right]` là nồng độ ion OH- (mol/L).

*Điều kiện:* Dung dịch loãng

*Ghi chú:* pOH thường dùng trung gian khi tính pH của dung dịch base.

<sub>`chemistry.thpt.dien-li.poh` · lớp 11 · #poh #ph #dien-li</sub>

---

**Quan hệ giữa pH và pOH** — *Relation between pH and pOH*

$$\mathrm{pH} + \mathrm{pOH} = 14 \;(25\,^{\circ}\mathrm{C})$$

Trong đó: `\mathrm{pH}` là chỉ số pH; `\mathrm{pOH}` là chỉ số pOH.

*Điều kiện:* Dung dịch loãng ở 25 độ C (pKw = 14)

*Ghi chú:* Suy từ Kw = [H+][OH-] = 1.0e-14 bằng cách lấy âm logarit hai vế.

<sub>`chemistry.thpt.dien-li.quan-he-ph-poh` · lớp 11 · #ph #poh #kw</sub>

---

**Tích số ion của nước** — *Ion product of water*

$$K_{w} = \left[ \mathrm{H^{+}} \right]\left[ \mathrm{OH^{-}} \right] = 1.0 \times 10^{-14} \;(25\,^{\circ}\mathrm{C})$$

Trong đó: `K_{w}` là tích số ion của nước; `\left[ \mathrm{H^{+}} \right]` là nồng độ ion H+ (mol/L); `\left[ \mathrm{OH^{-}} \right]` là nồng độ ion OH- (mol/L).

*Điều kiện:* Dung dịch loãng ở 25 độ C; Kw thay đổi theo nhiệt độ

*Ghi chú:* Nước nguyên chất ở 25 độ C có [H+] = [OH-] = 1.0e-7 mol/L nên pH = 7 (môi trường trung tính).

<sub>`chemistry.thpt.dien-li.tich-so-ion-cua-nuoc` · lớp 11 · #kw #tich-so-ion #ph</sub>

---

**Định luật pha loãng Ostwald** — *Ostwald dilution law*

$$K_{a} = \dfrac{C \alpha^{2}}{1 - \alpha} \;\xrightarrow{\alpha \ll 1}\; \alpha \approx \sqrt{\dfrac{K_{a}}{C}}$$

Trong đó: `K_{a}` là hằng số phân li acid; `C` là nồng độ ban đầu của chất điện li yếu (mol/L); `\alpha` là độ điện li.

*Điều kiện:* Chất điện li yếu đơn chức; công thức gần đúng khi alpha nhỏ hơn nhiều so với 1

*Ghi chú:* Hệ quả: pha loãng dung dịch (C giảm) làm độ điện li alpha tăng, nhưng Ka không đổi.

<sub>`chemistry.thpt.dien-li.dinh-luat-pha-loang-ostwald` · lớp 11 · #ostwald #do-dien-li #ka</sub>

---

**Độ điện li của chất điện li** — *Degree of dissociation*

$$\alpha = \dfrac{n_{\text{phan li}}}{n_{\text{hoa tan}}} = \dfrac{C_{\text{phan li}}}{C_{0}}$$

Trong đó: `\alpha` là độ điện li; `n_{\text{phan li}}` là số mol chất đã phân li thành ion; `n_{\text{hoa tan}}` là tổng số mol chất hòa tan; `C_{\text{phan li}}` là nồng độ chất đã phân li (mol/L); `C_{0}` là nồng độ ban đầu (mol/L).

*Điều kiện:* 0 < alpha <= 1 (hoặc 0% đến 100%)

*Ghi chú:* alpha = 1: chất điện li mạnh; 0 < alpha < 1: chất điện li yếu. Độ điện li tăng khi pha loãng dung dịch.

<sub>`chemistry.thpt.dien-li.do-dien-li` · lớp 11 · #dien-li #do-dien-li #thpt</sub>

---

### Đếm đồng phân hợp chất hữu cơ

**Số đồng phân ancol no, đơn chức, mạch hở** — *Number of isomers of saturated monohydric alcohols*

$$S = 2^{\,n-2}\quad (1 < n < 6)$$

Trong đó: `S` là số đồng phân ancol; `n` là số nguyên tử cacbon của ancol CnH2n+2O.

*Điều kiện:* Công thức đúng với n = 2, 3, 4, 5; từ n ≥ 6 phải đếm trực tiếp

*Ghi chú:* n = 2 cho 1 đồng phân, n = 3 cho 2, n = 4 cho 4, n = 5 cho 8 đồng phân ancol.

<sub>`chemistry.thpt.dong-phan.ancol-no-don-chuc` · lớp 11 · #huu-co #dem-dong-phan #ancol</sub>

---

**Số đồng phân anđehit no, đơn chức, mạch hở** — *Number of isomers of saturated aldehydes*

$$S = 2^{\,n-3}\quad (2 < n < 7)$$

Trong đó: `S` là số đồng phân anđehit; `n` là số nguyên tử cacbon của anđehit CnH2nO.

*Điều kiện:* Công thức đúng với n = 3, 4, 5, 6

*Ghi chú:* n = 4 cho 2 đồng phân, n = 5 cho 4 đồng phân, n = 6 cho 8 đồng phân.

<sub>`chemistry.thpt.dong-phan.andehit-no-don-chuc` · lớp 11 · #huu-co #dem-dong-phan #andehit</sub>

---

**Số đồng phân ete no, đơn chức, mạch hở** — *Number of isomers of saturated ethers*

$$S = \dfrac{(n-1)(n-2)}{2}\quad (2 < n < 6)$$

Trong đó: `S` là số đồng phân ete; `n` là số nguyên tử cacbon của ete CnH2n+2O.

*Điều kiện:* Công thức đúng với n = 3, 4, 5

*Ghi chú:* n = 3 cho 1 ete, n = 4 cho 3 ete, n = 5 cho 6 ete. Tổng số đồng phân CnH2n+2O = số ancol + số ete.

<sub>`chemistry.thpt.dong-phan.ete` · lớp 11 · #huu-co #dem-dong-phan #ete</sub>

---

**Số đồng phân cấu tạo của ankan** — *Number of structural isomers of alkanes*

$$\begin{array}{c|c|c|c|c|c|c|c|c|c|c} n & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\ \hline \text{số đồng phân} & 1 & 1 & 1 & 2 & 3 & 5 & 9 & 18 & 35 & 75 \end{array}$$

Trong đó: `n` là số nguyên tử cacbon của ankan CnH2n+2.

*Điều kiện:* Chỉ tính đồng phân cấu tạo mạch cacbon; ankan không có đồng phân hình học

*Ghi chú:* Không có công thức tổng quát đơn giản, cần học thuộc bảng. Từ C4 trở đi mới có đồng phân mạch nhánh.

<sub>`chemistry.thpt.dong-phan.ankan` · lớp 11 · #huu-co #dem-dong-phan #ankan</sub>

---

**Số đồng phân vị trí của dẫn xuất hai nhóm thế trên vòng benzen** — *Positional isomers of disubstituted benzenes*

$$S = 3:\ \text{ortho (1,2)},\ \text{meta (1,3)},\ \text{para (1,4)}$$

Trong đó: `S` là số đồng phân vị trí khi vòng benzen có hai nhóm thế.

*Điều kiện:* Vòng benzen mang đúng hai nhóm thế; ba nhóm thế giống nhau cho 3 đồng phân (1,2,3 / 1,2,4 / 1,3,5)

*Ghi chú:* Xilen C8H10 có 3 đồng phân o-, m-, p-xilen, cộng thêm etylbenzen là 4 đồng phân thơm của C8H10.

<sub>`chemistry.thpt.dong-phan.dan-xuat-benzen` · lớp 11 · #huu-co #dem-dong-phan #aren</sub>

---

**Số đồng phân xeton no, đơn chức, mạch hở** — *Number of isomers of saturated ketones*

$$S = \dfrac{(n-2)(n-3)}{2}\quad (3 < n < 7)$$

Trong đó: `S` là số đồng phân xeton; `n` là số nguyên tử cacbon của xeton CnH2nO.

*Điều kiện:* Công thức đúng với n = 4, 5, 6

*Ghi chú:* n = 4 cho 1 xeton (axeton là n = 3, chỉ 1 chất), n = 5 cho 3, n = 6 cho 6 xeton.

<sub>`chemistry.thpt.dong-phan.xeton` · lớp 11 · #huu-co #dem-dong-phan #xeton</sub>

---

**Điều kiện có đồng phân hình học cis - trans** — *Condition for cis-trans geometric isomerism*

$$\underset{b}{\overset{a}{C}} = \underset{d}{\overset{c}{C}}\ \text{có đồng phân hình học} \iff a \ne b\ \text{và}\ c \ne d$$

Trong đó: `a` là nhóm thế thứ nhất trên nguyên tử C thứ nhất; `b` là nhóm thế thứ hai trên nguyên tử C thứ nhất; `c` là nhóm thế thứ nhất trên nguyên tử C thứ hai; `d` là nhóm thế thứ hai trên nguyên tử C thứ hai.

*Điều kiện:* Phân tử phải có liên kết đôi C=C (hoặc vòng no) và mỗi nguyên tử C của liên kết đôi mang hai nhóm thế khác nhau

*Ghi chú:* Dạng cis có hai nhóm lớn cùng phía, dạng trans có hai nhóm lớn khác phía. But-2-en có đồng phân hình học, but-1-en thì không.

<sub>`chemistry.thpt.dong-phan.hinh-hoc` · lớp 11 · #huu-co #dong-phan-hinh-hoc #anken</sub>

---

### Bài toán đốt cháy hợp chất hữu cơ

**Đốt cháy axit cacboxylic no, đơn chức, mạch hở** — *Combustion of saturated monocarboxylic acids*

$$n_{CO_2} = n_{H_2O};\quad n_{O(axit)} = 2n_{axit} = 2n_{CO_2} + n_{H_2O} - 2n_{O_2}$$

Trong đó: `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{axit}` là số mol axit CnH2nO2 bị đốt (mol); `n_{O(axit)}` là số mol nguyên tử oxi trong axit (mol); `n_{O_2}` là số mol O2 đã dùng (mol).

*Điều kiện:* Axit no, đơn chức, mạch hở CnH2nO2; đốt cháy hoàn toàn

*Ghi chú:* Axit no đơn chức hở và este no đơn chức hở cùng công thức CnH2nO2 nên kết quả đốt cháy giống hệt nhau.

<sub>`chemistry.thpt.dot-chay.axit-no-don-chuc` · lớp 11, 12 · #huu-co #dot-chay #axit-cacboxylic</sub>

---

**Số nguyên tử cacbon trung bình** — *Average number of carbon atoms*

$$\overline{C} = \dfrac{n_{CO_2}}{n_{hh}}$$

Trong đó: `\overline{C}` là số nguyên tử cacbon trung bình của hỗn hợp; `n_{CO_2}` là tổng số mol CO2 thu được (mol); `n_{hh}` là tổng số mol hỗn hợp chất hữu cơ đem đốt (mol).

*Điều kiện:* Đốt cháy hoàn toàn hỗn hợp; luôn có C(nhỏ nhất) < C trung bình < C(lớn nhất)

*Ghi chú:* Với hai chất đồng đẳng kế tiếp, nếu C trung bình = 2,4 thì hai chất có 2 và 3 nguyên tử C.

<sub>`chemistry.thpt.dot-chay.so-c-trung-binh` · lớp 11, 12 · #huu-co #dot-chay #gia-tri-trung-binh</sub>

---

**Số nguyên tử hiđro trung bình** — *Average number of hydrogen atoms*

$$\overline{H} = \dfrac{2n_{H_2O}}{n_{hh}}$$

Trong đó: `\overline{H}` là số nguyên tử hiđro trung bình của hỗn hợp; `n_{H_2O}` là tổng số mol H2O thu được (mol); `n_{hh}` là tổng số mol hỗn hợp chất hữu cơ đem đốt (mol).

*Điều kiện:* Đốt cháy hoàn toàn hỗn hợp chất hữu cơ

*Ghi chú:* Nếu H trung bình < 4 thì trong hỗn hợp chắc chắn có chất có ít hơn 4 nguyên tử H (ví dụ C2H2).

<sub>`chemistry.thpt.dot-chay.so-h-trung-binh` · lớp 11, 12 · #huu-co #dot-chay #gia-tri-trung-binh</sub>

---

**Bảo toàn nguyên tố oxi trong phản ứng cháy** — *Oxygen atom balance in combustion*

$$n_{O(X)} + 2n_{O_2} = 2n_{CO_2} + n_{H_2O}$$

Trong đó: `n_{O(X)}` là số mol nguyên tử oxi có trong chất hữu cơ X (mol); `n_{O_2}` là số mol khí O2 đã dùng (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol).

*Điều kiện:* Đốt cháy hoàn toàn hợp chất hữu cơ chứa C, H, O (và có thể có N)

*Ghi chú:* Đây là công cụ chủ lực để tìm số nhóm chức chứa oxi khi biết n(O2), n(CO2), n(H2O).

<sub>`chemistry.thpt.dot-chay.bao-toan-oxi` · lớp 11, 12 · #huu-co #dot-chay #bao-toan-nguyen-to</sub>

---

**Số mol O2 cần đốt cháy hợp chất hữu cơ chứa oxi** — *Oxygen required to burn an oxygen-containing organic compound*

$$n_{O_2} = n_{CO_2} + \dfrac{n_{H_2O}}{2} - \dfrac{n_{O(X)}}{2}$$

Trong đó: `n_{O_2}` là số mol khí oxi cần dùng (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{O(X)}` là số mol nguyên tử oxi có sẵn trong X (mol).

*Điều kiện:* Đốt cháy hoàn toàn; X chứa C, H, O

*Ghi chú:* Kết hợp bảo toàn khối lượng: m(X) + 32n(O2) = 44n(CO2) + 18n(H2O) + 28n(N2).

<sub>`chemistry.thpt.dot-chay.so-mol-o2-tong-quat` · lớp 11, 12 · #huu-co #dot-chay #bao-toan-nguyen-to</sub>

---

### CO2 tác dụng với dung dịch kiềm

**Cho từ từ axit vào muối cacbonat và trường hợp đổ ngược lại** — *Adding acid to a carbonate solution and the reverse order*

$$\begin{cases} \text{nhỏ từ từ } H^+ \text{ vào muối}: & n_{CO_2} = n_{H^+} - n_{CO_3^{2-}} \\ \text{đổ từ từ muối vào } H^+: & n_{CO_2} = \dfrac{(x+y)\,n_{H^+}}{2x + y} \end{cases}$$

Trong đó: `n_{CO_2}` là số mol khí CO2 thoát ra (mol); `n_{H^+}` là số mol ion H+ của axit (mol); `n_{CO_3^{2-}}` là số mol ion cacbonat trong dung dịch muối (mol); `x` là số phần mol CO3^2- trong hỗn hợp muối; `y` là số phần mol HCO3- trong hỗn hợp muối.

*Điều kiện:* Nhỏ từ từ axit: nấc H+ + CO3^2- → HCO3- xảy ra hết trước rồi mới tới H+ + HCO3- → CO2 + H2O, nên công thức chỉ đúng khi n(CO3^2-) ≤ n(H+) ≤ 2n(CO3^2-) + n(HCO3-). Đổ muối vào axit: hai muối phản ứng đồng thời theo đúng tỉ lệ x : y và axit phải hết

*Ghi chú:* Cùng lượng chất nhưng thứ tự đổ khác nhau cho lượng khí khác nhau; đổ muối vào axit luôn cho nhiều CO2 hơn. Nếu chỉ có muối cacbonat (y = 0) thì n(CO2) = n(H+)/2.

<sub>`chemistry.thpt.co2-kiem.axit-vao-cacbonat` · lớp 11, 12 · #vo-co #co2-kiem #ion #giai-nhanh</sub>

---

**Biện luận sản phẩm theo tỉ lệ T** — *Product determination from OH-/CO2 ratio*

$$\begin{cases} T \le 1 & \Rightarrow \text{chỉ tạo } HCO_3^-,\ CO_2 \text{ có thể dư} \\ 1 < T < 2 & \Rightarrow \text{tạo đồng thời } HCO_3^- \text{ và } CO_3^{2-} \\ T \ge 2 & \Rightarrow \text{chỉ tạo } CO_3^{2-},\ OH^- \text{ có thể dư} \end{cases}$$

Trong đó: `T` là tỉ lệ n(OH-)/n(CO2); `HCO_3^-` là ion hiđrocacbonat (muối axit); `CO_3^{2-}` là ion cacbonat (muối trung hòa).

*Điều kiện:* Phản ứng xảy ra hoàn toàn trong dung dịch

*Ghi chú:* Mẹo nhớ: T nhỏ (thiếu kiềm) tạo muối axit, T lớn (dư kiềm) tạo muối trung hòa.

<sub>`chemistry.thpt.co2-kiem.san-pham-theo-t` · lớp 11, 12 · #vo-co #co2-kiem #bien-luan</sub>

---

**Tỉ lệ T = n(OH-)/n(CO2)** — *Hydroxide to carbon dioxide mole ratio*

$$T = \dfrac{n_{OH^-}}{n_{CO_2}}$$

Trong đó: `T` là tỉ lệ mol dùng để biện luận sản phẩm; `n_{OH^-}` là tổng số mol ion hiđroxit trong dung dịch kiềm (mol); `n_{CO_2}` là số mol khí CO2 bị hấp thụ (mol).

*Điều kiện:* Dung dịch kiềm mạnh (NaOH, KOH, Ca(OH)2, Ba(OH)2); tính n_OH- theo tổng của mọi bazơ

*Ghi chú:* Với Ca(OH)2 hay Ba(OH)2 thì n_OH- = 2·n_bazơ. Áp dụng tương tự cho SO2.

<sub>`chemistry.thpt.co2-kiem.ti-le-t` · lớp 11, 12 · #vo-co #co2-kiem #giai-nhanh</sub>

---

**Bài toán ngược: tính n(CO2) khi biết lượng kết tủa (hai nghiệm)** — *Two solutions for CO2 amount from a given precipitate*

$$\begin{cases} n_{CO_2} = n_{\downarrow} & \text{(kiềm dư, kết tủa chưa bị hòa tan)} \\ n_{CO_2} = n_{OH^-} - n_{\downarrow} & \text{(CO}_2 \text{ dư, kết tủa đã tan một phần)} \end{cases}$$

Trong đó: `n_{CO_2}` là số mol CO2 cần tìm (mol); `n_{\downarrow}` là số mol kết tủa CaCO3 hoặc BaCO3 thu được (mol); `n_{OH^-}` là tổng số mol OH- ban đầu (mol).

*Điều kiện:* n(kết tủa) < n(M2+); nếu n(kết tủa) = n(M2+) thì chỉ có một nghiệm nhỏ nhất và một khoảng nghiệm

*Ghi chú:* Bài yêu cầu 'giá trị lớn nhất của V(CO2)' thì lấy nghiệm thứ hai; 'nhỏ nhất' thì lấy nghiệm thứ nhất.

<sub>`chemistry.thpt.co2-kiem.bai-toan-nguoc-hai-nghiem` · lớp 11, 12 · #vo-co #co2-kiem #hai-nghiem</sub>

---

**CO2 tác dụng với hỗn hợp NaOH và Ca(OH)2** — *CO2 absorbed by a mixture of sodium and calcium hydroxide*

$$n_{OH^-} = n_{NaOH} + 2n_{Ca(OH)_2};\quad n_{\downarrow CaCO_3} = \min\left(n_{OH^-} - n_{CO_2},\ n_{Ca^{2+}}\right)$$

Trong đó: `n_{OH^-}` là tổng số mol OH- của hỗn hợp bazơ (mol); `n_{NaOH}` là số mol NaOH (mol); `n_{Ca(OH)_2}` là số mol Ca(OH)2 (mol); `n_{CO_2}` là số mol CO2 hấp thụ (mol); `n_{Ca^{2+}}` là số mol ion Ca2+ (mol); `n_{\downarrow CaCO_3}` là số mol kết tủa CaCO3 (mol).

*Điều kiện:* CO2 hấp thụ hết; nếu biểu thức trong min âm thì không có kết tủa

*Ghi chú:* Nên tư duy theo ion: trước hết tính n(CO3^2-), sau đó mới ghép với Ca2+.

<sub>`chemistry.thpt.co2-kiem.hon-hop-naoh-caoh2` · lớp 11, 12 · #vo-co #co2-kiem #ion</sub>

---

**Độ tăng (giảm) khối lượng dung dịch khi hấp thụ CO2** — *Change in solution mass after CO2 absorption*

$$\Delta m_{dd} = m_{CO_2} - m_{\downarrow} = 44n_{CO_2} - m_{\downarrow}$$

Trong đó: `\Delta m_{dd}` là độ biến thiên khối lượng dung dịch (dương là tăng, âm là giảm) (g); `m_{CO_2}` là khối lượng CO2 bị hấp thụ (g); `m_{\downarrow}` là khối lượng kết tủa tách ra (g); `n_{CO_2}` là số mol CO2 bị hấp thụ (mol).

*Điều kiện:* CO2 được hấp thụ hoàn toàn; kết tủa được tách khỏi dung dịch

*Ghi chú:* M(CO2) = 44 g/mol. Nếu m(kết tủa) > 44·n(CO2) thì khối lượng dung dịch giảm.

<sub>`chemistry.thpt.co2-kiem.khoi-luong-dung-dich-thay-doi` · lớp 11, 12 · #vo-co #co2-kiem #bao-toan-khoi-luong</sub>

---

**Số mol kết tủa khi CO2 tác dụng với Ca(OH)2 hoặc Ba(OH)2** — *Precipitate formed when CO2 reacts with calcium or barium hydroxide*

$$n_{\downarrow} = \min\left(n_{CO_3^{2-}},\ n_{M^{2+}}\right),\quad n_{CO_3^{2-}} = n_{OH^-} - n_{CO_2}$$

Trong đó: `n_{\downarrow}` là số mol kết tủa CaCO3 hoặc BaCO3 (mol); `n_{CO_3^{2-}}` là số mol ion cacbonat sinh ra (mol); `n_{M^{2+}}` là số mol ion Ca2+ hoặc Ba2+ trong dung dịch (mol); `n_{OH^-}` là số mol ion OH- (mol); `n_{CO_2}` là số mol CO2 bị hấp thụ (mol).

*Điều kiện:* CO2 bị hấp thụ hết; nếu n(CO3^2-) tính ra âm thì không có kết tủa

*Ghi chú:* M(CaCO3) = 100 g/mol; M(BaCO3) = 197 g/mol.

<sub>`chemistry.thpt.co2-kiem.ket-tua-caco3` · lớp 11, 12 · #vo-co #co2-kiem #ket-tua</sub>

---

**Muối hiđrocacbonat tác dụng với dung dịch kiềm** — *Hydrogencarbonate reacting with hydroxide*

$$HCO_3^- + OH^- \rightarrow CO_3^{2-} + H_2O;\quad n_{CO_3^{2-}} = \min\left(n_{HCO_3^-},\ n_{OH^-}\right)$$

Trong đó: `n_{HCO_3^-}` là số mol ion hiđrocacbonat (mol); `n_{OH^-}` là số mol ion hiđroxit (mol); `n_{CO_3^{2-}}` là số mol ion cacbonat tạo thành (mol).

*Điều kiện:* Phản ứng xảy ra hoàn toàn theo tỉ lệ mol 1 : 1

*Ghi chú:* Nếu dung dịch có thêm Ca2+ hoặc Ba2+ thì CO3^2- sinh ra sẽ tạo kết tủa ngay.

<sub>`chemistry.thpt.co2-kiem.hco3-tac-dung-oh` · lớp 11, 12 · #vo-co #co2-kiem #ion</sub>

---

**Nhiệt phân muối hiđrocacbonat và cacbonat** — *Thermal decomposition of hydrogencarbonates and carbonates*

$$2M(HCO_3)_n \xrightarrow{t^o} M_2(CO_3)_n + nCO_2 + nH_2O;\quad CaCO_3 \xrightarrow{t^o} CaO + CO_2$$

Trong đó: `M` là kim loại hóa trị n; `n` là hóa trị của kim loại M.

*Điều kiện:* Muối cacbonat của kim loại kiềm (Na2CO3, K2CO3) bền, không bị nhiệt phân

*Ghi chú:* Độ giảm khối lượng khi nhiệt phân M(HCO3)n chính là khối lượng CO2 và H2O thoát ra.

<sub>`chemistry.thpt.co2-kiem.nhiet-phan-hidrocacbonat` · lớp 11, 12 · #vo-co #nhiet-phan #cacbonat</sub>

---

**SO2 tác dụng với dung dịch kiềm** — *Sulfur dioxide reacting with alkali solution*

$$T = \dfrac{n_{OH^-}}{n_{SO_2}};\quad n_{SO_3^{2-}} = n_{OH^-} - n_{SO_2},\ \ n_{HSO_3^-} = 2n_{SO_2} - n_{OH^-}$$

Trong đó: `T` là tỉ lệ mol OH- trên SO2; `n_{SO_2}` là số mol SO2 bị hấp thụ (mol); `n_{SO_3^{2-}}` là số mol muối sunfit (mol); `n_{HSO_3^-}` là số mol muối hiđrosunfit (mol); `n_{OH^-}` là số mol ion OH- (mol).

*Điều kiện:* Công thức tính hai muối chỉ dùng khi 1 < T < 2

*Ghi chú:* Biện luận hoàn toàn tương tự CO2: T ≤ 1 chỉ tạo HSO3-, T ≥ 2 chỉ tạo SO3^2-.

<sub>`chemistry.thpt.co2-kiem.so2-kiem` · lớp 11, 12 · #vo-co #so2 #co2-kiem</sub>

---

**Số mol muối trung hòa và muối axit tạo thành** — *Moles of carbonate and hydrogencarbonate formed*

$$\begin{cases} n_{CO_3^{2-}} = n_{OH^-} - n_{CO_2} \\ n_{HCO_3^-} = 2n_{CO_2} - n_{OH^-} \end{cases}$$

Trong đó: `n_{CO_3^{2-}}` là số mol muối cacbonat (muối trung hòa) (mol); `n_{HCO_3^-}` là số mol muối hiđrocacbonat (muối axit) (mol); `n_{OH^-}` là số mol ion OH- (mol); `n_{CO_2}` là số mol CO2 bị hấp thụ hết (mol).

*Điều kiện:* Chỉ dùng khi 1 < T < 2, tức là tạo đồng thời hai muối và cả CO2 lẫn OH- đều hết

*Ghi chú:* Kiểm tra lại: n(CO3^2-) + n(HCO3^-) = n(CO2) và 2n(CO3^2-) + n(HCO3^-) = n(OH-).

<sub>`chemistry.thpt.co2-kiem.so-mol-hai-muoi` · lớp 11, 12 · #vo-co #co2-kiem #giai-nhanh</sub>

---

### Các định luật bảo toàn

**Bảo toàn liên kết pi trong phản ứng cộng** — *Conservation of pi bonds in addition reactions*

$$n_{\pi} = k \cdot n_{hidrocacbon} = n_{H_{2}\,\text{phan ung}} + n_{Br_{2}\,\text{phan ung}}$$

Trong đó: `n_{\pi}` là tổng số mol liên kết pi (mol); `k` là số liên kết pi trong một phân tử (mạch hở); `n_{hidrocacbon}` là số mol hiđrocacbon (mol); `n_{H_{2}\,\text{phan ung}}` là số mol H2 đã cộng (mol); `n_{Br_{2}\,\text{phan ung}}` là số mol Br2 đã cộng (mol).

*Điều kiện:* Hiđrocacbon mạch hở; mỗi liên kết pi cộng được 1 phân tử H2 hoặc 1 phân tử Br2

*Ghi chú:* Liên kết pi trong vòng benzene không cộng Br2 trong dung dịch nên không tính vào công thức này.

<sub>`chemistry.thpt.bao-toan.bao-toan-lien-ket-pi` · lớp 11, 12 · #lien-ket-pi #huu-co #phan-ung-cong</sub>

---

**Định luật bảo toàn điện tích trong dung dịch** — *Charge balance in solution*

$$\sum \left| z_{+} \right| n_{\text{cation}} = \sum \left| z_{-} \right| n_{\text{anion}}$$

Trong đó: `z_{+}` là điện tích của cation; `n_{\text{cation}}` là số mol cation (mol); `z_{-}` là điện tích của anion; `n_{\text{anion}}` là số mol anion (mol).

*Điều kiện:* Dung dịch trung hòa điện; phải kể đủ mọi ion có mặt

*Ghi chú:* Hệ quả: khối lượng muối khan = tổng khối lượng các ion trong dung dịch.

<sub>`chemistry.thpt.bao-toan.bao-toan-dien-tich` · lớp 11, 12 · #bao-toan-dien-tich #dung-dich #ion</sub>

---

**Khối lượng muối khan thu được khi cô cạn dung dịch** — *Mass of dry salt from the ions in solution*

$$m_{\text{muoi khan}} = m_{\text{cation}} + m_{\text{anion}} = \sum n_{i} M_{i}$$

Trong đó: `m_{\text{muoi khan}}` là khối lượng muối khan thu được (g); `m_{\text{cation}}` là tổng khối lượng các cation trong dung dịch (g); `m_{\text{anion}}` là tổng khối lượng các anion trong dung dịch (g); `n_{i}` là số mol ion thứ i (mol); `M_{i}` là khối lượng mol của ion thứ i (g/mol).

*Điều kiện:* Cô cạn dung dịch, muối không bị nhiệt phân; các ion phải thỏa mãn bảo toàn điện tích

*Ghi chú:* Kết hợp bảo toàn điện tích để tìm số mol ion còn thiếu trước khi tính khối lượng.

<sub>`chemistry.thpt.bao-toan.khoi-luong-muoi-khan` · lớp 11, 12 · #bao-toan-dien-tich #muoi-khan #co-can</sub>

---

**Hiệu suất của quá trình gồm nhiều giai đoạn** — *Overall yield of a multi-step process*

$$H = H_{1} \cdot H_{2} \cdots H_{k}$$

Trong đó: `H` là hiệu suất tổng của cả quá trình; `H_{1}` là hiệu suất giai đoạn 1; `H_{2}` là hiệu suất giai đoạn 2; `H_{k}` là hiệu suất giai đoạn thứ k.

*Điều kiện:* Các hiệu suất viết dưới dạng số thập phân (ví dụ 80% ghi là 0.8); các giai đoạn nối tiếp nhau

*Ghi chú:* Nếu tính theo phần trăm: H% = H1% x H2% x ... / 100^(k-1).

<sub>`chemistry.thpt.bao-toan.hieu-suat-nhieu-giai-doan` · lớp 11, 12 · #hieu-suat #san-xuat #thpt</sub>

---

### Cân bằng hoá học quốc tế

**Quy ước hằng số cân bằng không thứ nguyên theo trạng thái chuẩn** — *Dimensionless equilibrium constant referenced to standard states*

$$K^{\ominus} = \prod_{i} \left( \dfrac{p_{i}}{p^{\ominus}} \right)^{\nu_{i}}, \qquad K^{\ominus} = \prod_{i} \left( \dfrac{c_{i}}{c^{\ominus}} \right)^{\nu_{i}}$$

Trong đó: `K^{\ominus}` là hằng số cân bằng nhiệt động, không có đơn vị (); `p_{i}` là áp suất riêng phần của cấu tử i lúc cân bằng (Pa); `p^{\ominus}` là áp suất trạng thái chuẩn, bằng 100 kPa (1 bar) (Pa); `c_{i}` là nồng độ của cấu tử i lúc cân bằng (mol/L); `c^{\ominus}` là nồng độ trạng thái chuẩn, bằng 1 mol/L (mol/L); `\nu_{i}` là hệ số tỉ lượng của cấu tử i: dương với sản phẩm, âm với chất tham gia ().

*Điều kiện:* Chỉ khi chia cho trạng thái chuẩn thì K mới không thứ nguyên; chất rắn nguyên chất, chất lỏng nguyên chất và dung môi có hoạt độ bằng 1 nên không xuất hiện trong biểu thức

*Ghi chú:* Đây là quy ước BUỘC PHẢI hiểu trước khi dùng Delta G(chuẩn) = -RT lnK và E = E(chuẩn) - (RT/nF)lnQ, vì chỉ lấy logarit được của một số không thứ nguyên. Cả ba hệ quốc tế đều tránh chuyển đổi Kc - Kp: CED của AP Chemistry có exclusion statement 'Conversion between Kc and Kp will not be assessed on the AP Exam. Students should be aware of the conceptual differences'; Cambridge 9701 ghi 'use of the relationship between Kp and Kc is not required'. Khác biệt với CT GDPT 2018 Việt Nam: sách Việt Nam thường viết Kc và Kp KÈM ĐƠN VỊ và có dạy hệ thức Kp = Kc(RT)^(delta n); khi làm đề quốc tế phải bỏ đơn vị và không được dùng hệ thức chuyển đổi đó.

<sub>`chemistry.thpt.can-bang-quoc-te.hang-so-can-bang-khong-thu-nguyen` · lớp 11, 12 · #ap #ib #a-level #hang-so-can-bang #trang-thai-chuan</sub>

---

### Công thức tổng quát các dãy đồng đẳng

**Công thức tổng quát của axit cacboxylic no, đơn chức, mạch hở** — *General formula of saturated monocarboxylic acids*

$$C_nH_{2n}O_2 \equiv C_{n-1}H_{2n-1}COOH\ (n \ge 1)$$

Trong đó: `n` là số nguyên tử cacbon trong phân tử axit.

*Điều kiện:* n ≥ 1; mạch hở, no, chứa đúng một nhóm -COOH

*Ghi chú:* M = 14n + 32. HCOOH (46), CH3COOH (60), C2H5COOH (74). Axit no hai chức mạch hở: CnH2n-2O4.

<sub>`chemistry.thpt.cttq.axit-cacboxylic` · lớp 11, 12 · #huu-co #cong-thuc-tong-quat #axit-cacboxylic</sub>

---

### Dung dịch chất điện li

**Khối lượng muối khan tính theo khối lượng các ion** — *Mass of dry salts from the masses of ions*

$$m_{muoi\ khan} = m_{cation} + m_{anion}$$

Trong đó: `m_{muoi\ khan}` là khối lượng muối khan thu được khi cô cạn (g); `m_{cation}` là tổng khối lượng các ion dương (g); `m_{anion}` là tổng khối lượng các ion âm (g).

*Điều kiện:* Muối không bị phân hủy khi cô cạn; dung dịch không chứa ion HCO3- (sẽ phân hủy khi đun)

*Ghi chú:* Nếu dung dịch chứa HCO3-, khi cô cạn: 2HCO3- → CO3^2- + CO2 + H2O.

<sub>`chemistry.thpt.dung-dich.khoi-luong-muoi-tu-ion` · lớp 11, 12 · #vo-co #dung-dich #bao-toan-khoi-luong</sub>

---

### Entropy và năng lượng Gibbs bậc THPT

**Phản ứng ghép cặp để thực hiện quá trình không tự diễn biến** — *Coupled reactions driving a thermodynamically unfavourable process*

$$\Delta G^{\ominus}_{tong} = \Delta G^{\ominus}_{1} + \Delta G^{\ominus}_{2} < 0, \qquad \Delta G^{\ominus}_{1} > 0$$

Trong đó: `\Delta G^{\ominus}_{tong}` là năng lượng Gibbs chuẩn của quá trình tổng sau khi ghép cặp (kJ/mol); `\Delta G^{\ominus}_{1}` là năng lượng Gibbs chuẩn của phản ứng KHÔNG thuận lợi (dương), là phản ứng ta muốn xảy ra (kJ/mol); `\Delta G^{\ominus}_{2}` là năng lượng Gibbs chuẩn của phản ứng thuận lợi (âm) được ghép vào để kéo theo (kJ/mol).

*Điều kiện:* Hai phản ứng phải có chung ít nhất một chất để thực sự ghép được với nhau; bản chất là tính cộng được của hàm trạng thái G, tương tự định luật Hess

*Ghi chú:* Đây là Topic 9.7 'Coupled Reactions' của AP Chemistry, một topic RIÊNG trong CED: 'A desired product can be formed by coupling a thermodynamically unfavorable reaction that produces that product to a favorable reaction'. Ví dụ chuẩn của AP: thuỷ phân ATP thành ADP ghép với các quá trình sinh tổng hợp; hoặc dùng nguồn năng lượng ngoài (điện năng cho bình điện phân, ánh sáng cho quang hợp) để đẩy quá trình không thuận lợi. IB và A-Level không tách thành mục riêng. CT GDPT 2018 Việt Nam không có nội dung này.

<sub>`chemistry.thpt.nhiet-dong-thpt.phan-ung-ghep-cap` · lớp 11, 12 · #ap #gibbs #ghep-cap #tu-dien-bien</sub>

---

**Phản ứng bị kiểm soát động học: thuận lợi nhiệt động nhưng không xảy ra** — *Kinetic control: a thermodynamically favoured reaction that does not proceed*

$$\Delta G^{\ominus} < 0 \ \text{nhung} \ E_{a} \gg RT \Rightarrow k = A e^{-E_{a}/(RT)} \to 0$$

Trong đó: `\Delta G^{\ominus}` là biến thiên năng lượng Gibbs chuẩn của phản ứng; âm nên phản ứng thuận lợi về nhiệt động (kJ/mol); `E_{a}` là năng lượng hoạt hoá của phản ứng (J/mol); `R` là hằng số khí, 8,314 J/(K.mol) (J/(mol*K)); `T` là nhiệt độ tuyệt đối (K); `k` là hằng số tốc độ của phản ứng (); `A` là thừa số tần số trong phương trình Arrhenius.

*Điều kiện:* Kết luận nhiệt động chỉ nói về VỊ TRÍ cân bằng cuối cùng, không nói gì về TỐC ĐỘ đạt tới vị trí đó

*Ghi chú:* Đây là Topic 9.4 'Thermodynamic and Kinetic Control' của AP Chemistry, một topic RIÊNG trong CED: 'Processes that are thermodynamically favored, but do not proceed at a measurable rate, are under kinetic control. High activation energy is a common reason'. Ví dụ kinh điển: kim cương chuyển thành graphite có Delta G < 0 nhưng Ea quá lớn; hỗn hợp H2 và O2 bền ở nhiệt độ phòng cho đến khi có tia lửa. IB (Reactivity 1.4) cũng nhấn mạnh ý này. Đơn vị của k để trống vì phụ thuộc bậc phản ứng. CT GDPT 2018 Việt Nam nêu riêng rẽ tiêu chuẩn Delta G và các yếu tố ảnh hưởng tốc độ, không đặt cạnh nhau thành khái niệm 'kiểm soát động học'.

<sub>`chemistry.thpt.nhiet-dong-thpt.kiem-soat-dong-hoc` · lớp 11, 12 · #ap #ib #kiem-soat-dong-hoc #gibbs</sub>

---

### Khử oxit kim loại

**Khối lượng kim loại thu được sau khi khử oxit** — *Mass of metal obtained after oxide reduction*

$$m_{KL} = m_{oxit} - 16n_{O}$$

Trong đó: `m_{KL}` là khối lượng kim loại thu được (g); `m_{oxit}` là khối lượng hỗn hợp oxit ban đầu (g); `n_{O}` là số mol nguyên tử oxi bị khử (mol).

*Điều kiện:* Oxit bị khử hoàn toàn thành kim loại; nếu khử không hoàn toàn thì m(rắn) = m(oxit) − 16·n(O bị lấy)

*Ghi chú:* M(O) = 16 g/mol. Đây chính là biểu thức của định luật bảo toàn khối lượng.

<sub>`chemistry.thpt.oxit-axit.khoi-luong-kim-loai-sau-khu` · lớp 11, 12 · #vo-co #khu-oxit #bao-toan-khoi-luong</sub>

---

**Khử oxit kim loại bằng CO** — *Reduction of metal oxides by carbon monoxide*

$$n_{CO} = n_{CO_2} = n_{O(bi\ lay)};\quad m_{chat\ ran\ giam} = 16n_{O}$$

Trong đó: `n_{CO}` là số mol CO đã phản ứng (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{O(bi\ lay)}` là số mol nguyên tử oxi bị tách khỏi oxit (mol); `n_{O}` là số mol nguyên tử oxi bị tách (mol); `m_{chat\ ran\ giam}` là độ giảm khối lượng chất rắn (g).

*Điều kiện:* CO chỉ khử được oxit của kim loại đứng sau Al trong dãy hoạt động (ZnO, FeO, Fe2O3, CuO...)

*Ghi chú:* Khí sau phản ứng hấp thụ vào Ca(OH)2 dư cho n(CaCO3) = n(CO2) = n(O bị lấy).

<sub>`chemistry.thpt.oxit-axit.khu-oxit-bang-co` · lớp 11, 12 · #vo-co #khu-oxit #bao-toan-nguyen-to</sub>

---

**Khử oxit kim loại bằng H2** — *Reduction of metal oxides by hydrogen*

$$n_{H_2} = n_{H_2O} = n_{O(bi\ lay)}$$

Trong đó: `n_{H_2}` là số mol H2 đã phản ứng (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{O(bi\ lay)}` là số mol nguyên tử oxi bị tách khỏi oxit (mol).

*Điều kiện:* H2 khử oxit của kim loại đứng sau Al ở nhiệt độ cao

*Ghi chú:* Hơi nước sinh ra có thể hấp thụ bằng H2SO4 đặc hoặc P2O5 để cân khối lượng.

<sub>`chemistry.thpt.oxit-axit.khu-oxit-bang-h2` · lớp 11, 12 · #vo-co #khu-oxit #bao-toan-nguyen-to</sub>

---

### Kim loại tác dụng với H2SO4 đặc nóng

**Số mol electron trao đổi theo sản phẩm khử của H2SO4 đặc** — *Electrons transferred from concentrated sulfuric acid reduction products*

$$n_e = 2n_{SO_2} + 6n_{S} + 8n_{H_2S}$$

Trong đó: `n_e` là tổng số mol electron kim loại nhường (mol); `n_{SO_2}` là số mol khí SO2 (mol); `n_{S}` là số mol lưu huỳnh đơn chất (mol); `n_{H_2S}` là số mol khí H2S (mol).

*Điều kiện:* H2SO4 đặc, nóng; kim loại tan hết

*Ghi chú:* Hệ số là độ giảm số oxi hóa của S từ +6: SO2 (2), S (6), H2S (8).

<sub>`chemistry.thpt.kim-loai-h2so4-dac.so-mol-electron` · lớp 11, 12 · #vo-co #h2so4-dac #bao-toan-electron</sub>

---

**Khối lượng muối sunfat theo số mol electron trao đổi** — *Mass of sulfate salts from electrons transferred*

$$m_{muoi} = m_{KL} + 96 \cdot \dfrac{n_e}{2} = m_{KL} + 48n_e$$

Trong đó: `m_{muoi}` là khối lượng muối sunfat khan (g); `m_{KL}` là khối lượng kim loại phản ứng (g); `n_e` là tổng số mol electron kim loại nhường (mol).

*Điều kiện:* Kim loại tan hết trong H2SO4 đặc nóng

*Ghi chú:* M(SO4^2-) = 96 g/mol; mỗi gốc SO4^2- ứng với 2 electron. Ví dụ chỉ tạo SO2: m(muối) = m(KL) + 96·n(SO2).

<sub>`chemistry.thpt.kim-loai-h2so4-dac.khoi-luong-muoi` · lớp 11, 12 · #vo-co #h2so4-dac #khoi-luong-muoi</sub>

---

**Số mol H2SO4 đặc phản ứng** — *Moles of concentrated sulfuric acid consumed*

$$n_{H_2SO_4} = 2n_{SO_2} + 4n_{S} + 5n_{H_2S} = \dfrac{n_e}{2} + n_{S(spk)}$$

Trong đó: `n_{H_2SO_4}` là số mol H2SO4 đã phản ứng (mol); `n_{SO_2}` là số mol khí SO2 (mol); `n_{S}` là số mol S đơn chất (mol); `n_{H_2S}` là số mol khí H2S (mol); `n_e` là tổng số mol electron trao đổi (mol); `n_{S(spk)}` là tổng số mol nguyên tử S trong các sản phẩm khử (mol).

*Điều kiện:* H2SO4 đặc nóng, kim loại tan hết, không tính phần axit dư

*Ghi chú:* Một nửa số mol electron chính là số mol gốc SO4^2- đi vào muối.

<sub>`chemistry.thpt.kim-loai-h2so4-dac.so-mol-axit` · lớp 11, 12 · #vo-co #h2so4-dac #giai-nhanh</sub>

---

### Kim loại tác dụng với HNO3

**Số mol electron trao đổi theo sản phẩm khử của HNO3** — *Electrons transferred from nitric acid reduction products*

$$n_e = n_{NO_2} + 3n_{NO} + 8n_{N_2O} + 10n_{N_2} + 8n_{NH_4^+}$$

Trong đó: `n_e` là tổng số mol electron kim loại nhường (mol); `n_{NO_2}` là số mol khí NO2 (mol); `n_{NO}` là số mol khí NO (mol); `n_{N_2O}` là số mol khí N2O (mol); `n_{N_2}` là số mol khí N2 (mol); `n_{NH_4^+}` là số mol ion amoni (trong NH4NO3) (mol).

*Điều kiện:* Kim loại tan hết trong HNO3; các sản phẩm khử được xác định đầy đủ

*Ghi chú:* Hệ số chính là độ giảm số oxi hóa của N từ +5: NO2 (1), NO (3), N2O (8), N2 (10), NH4+ (8).

<sub>`chemistry.thpt.kim-loai-hno3.so-mol-electron-trao-doi` · lớp 11, 12 · #vo-co #hno3 #bao-toan-electron</sub>

---

**Khối lượng muối khi có tạo NH4NO3** — *Mass of salts when ammonium nitrate is also formed*

$$m_{muoi} = m_{KL} + 62n_e + 80n_{NH_4NO_3}$$

Trong đó: `m_{muoi}` là tổng khối lượng muối khan (muối nitrat kim loại và NH4NO3) (g); `m_{KL}` là khối lượng kim loại phản ứng (g); `n_e` là tổng số mol electron kim loại nhường (đã kể phần tạo NH4+) (mol); `n_{NH_4NO_3}` là số mol NH4NO3 sinh ra (mol).

*Điều kiện:* Kim loại mạnh (Mg, Al, Zn) tác dụng với HNO3 loãng, dung dịch sau phản ứng có NH4NO3

*Ghi chú:* M(NH4NO3) = 80 g/mol. Dấu hiệu có NH4NO3: n(e) tính theo khí nhỏ hơn n(e) tính theo kim loại.

<sub>`chemistry.thpt.kim-loai-hno3.khoi-luong-muoi-co-nh4no3` · lớp 11, 12 · #vo-co #hno3 #nh4no3</sub>

---

**Khối lượng muối nitrat theo số mol electron trao đổi** — *Mass of nitrate salts from electrons transferred*

$$m_{muoi} = m_{KL} + 62n_e$$

Trong đó: `m_{muoi}` là khối lượng muối nitrat khan thu được (g); `m_{KL}` là khối lượng kim loại (hoặc hỗn hợp kim loại) đã phản ứng (g); `n_e` là tổng số mol electron kim loại nhường (mol).

*Điều kiện:* Kim loại tan hết; KHÔNG có sản phẩm khử NH4NO3

*Ghi chú:* M(NO3-) = 62 g/mol. Số mol NO3- trong muối đúng bằng số mol electron trao đổi.

<sub>`chemistry.thpt.kim-loai-hno3.khoi-luong-muoi-nitrat` · lớp 11, 12 · #vo-co #hno3 #khoi-luong-muoi</sub>

---

**Số mol HNO3 phản ứng** — *Moles of nitric acid consumed*

$$n_{HNO_3} = 2n_{NO_2} + 4n_{NO} + 10n_{N_2O} + 12n_{N_2} + 10n_{NH_4NO_3}$$

Trong đó: `n_{HNO_3}` là số mol HNO3 đã phản ứng (mol); `n_{NO_2}` là số mol khí NO2 (mol); `n_{NO}` là số mol khí NO (mol); `n_{N_2O}` là số mol khí N2O (mol); `n_{N_2}` là số mol khí N2 (mol); `n_{NH_4NO_3}` là số mol amoni nitrat sinh ra trong dung dịch (mol).

*Điều kiện:* Kim loại tan hết, HNO3 chỉ đóng vai trò chất oxi hóa và tạo muối nitrat

*Ghi chú:* Cách nhớ: n(HNO3) = n(e) + n(N trong sản phẩm khử). Ví dụ NO: 3 + 1 = 4.

<sub>`chemistry.thpt.kim-loai-hno3.so-mol-hno3-phan-ung` · lớp 11, 12 · #vo-co #hno3 #giai-nhanh</sub>

---

**Kim loại tác dụng với dung dịch chứa đồng thời H+ và NO3-** — *Metals in a solution containing both hydrogen and nitrate ions*

$$4H^+ + NO_3^- + 3e \rightarrow NO + 2H_2O;\quad n_{NO} = \min\left(\dfrac{n_{H^+}}{4},\ n_{NO_3^-},\ \dfrac{n_e}{3}\right)$$

Trong đó: `n_{H^+}` là số mol ion H+ (từ HCl, H2SO4 loãng hoặc HNO3) (mol); `n_{NO_3^-}` là số mol ion NO3- (từ muối nitrat hoặc HNO3) (mol); `n_e` là số mol electron kim loại nhường (mol); `n_{NO}` là số mol khí NO sinh ra (mol).

*Điều kiện:* NO là sản phẩm khử duy nhất; dung dịch chứa đồng thời H+ và NO3- có tính oxi hóa mạnh như HNO3 loãng

*Ghi chú:* Cu không tan trong dung dịch HCl loãng nhưng tan trong hỗn hợp HCl và NaNO3. Nếu sau phản ứng H+ vẫn dư thì Fe3+ không bị khử tiếp thành Fe2+.

<sub>`chemistry.thpt.kim-loai-hno3.ion-h-va-no3` · lớp 11, 12 · #vo-co #hno3 #bao-toan-electron</sub>

---

**Số mol NH4NO3 sinh ra** — *Moles of ammonium nitrate produced*

$$n_{NH_4NO_3} = \dfrac{n_e^{(KL)} - \left(n_{NO_2} + 3n_{NO} + 8n_{N_2O} + 10n_{N_2}\right)}{8}$$

Trong đó: `n_{NH_4NO_3}` là số mol NH4NO3 sinh ra (mol); `n_e^{(KL)}` là số mol electron tính theo kim loại (tổng hóa trị nhân số mol) (mol); `n_{NO_2}` là số mol NO2 (mol); `n_{NO}` là số mol NO (mol); `n_{N_2O}` là số mol N2O (mol); `n_{N_2}` là số mol N2 (mol).

*Điều kiện:* Kim loại tan hết; kết quả phải không âm, nếu bằng 0 thì không tạo NH4NO3

*Ghi chú:* N+5 + 8e → N-3, nên mỗi mol NH4+ nhận 8 mol electron.

<sub>`chemistry.thpt.kim-loai-hno3.so-mol-nh4no3` · lớp 11, 12 · #vo-co #hno3 #nh4no3</sub>

---

### Kim loại tác dụng với axit loãng

**Kim loại tác dụng với HCl: số mol axit và khối lượng muối** — *Metals with hydrochloric acid: acid moles and salt mass*

$$n_{HCl} = 2n_{H_2};\quad m_{muoi} = m_{KL} + 71n_{H_2}$$

Trong đó: `n_{HCl}` là số mol HCl đã phản ứng (mol); `n_{H_2}` là số mol khí H2 thoát ra (mol); `m_{muoi}` là khối lượng muối clorua khan (g); `m_{KL}` là khối lượng kim loại phản ứng (g).

*Điều kiện:* Kim loại đứng trước H trong dãy hoạt động hóa học; kim loại tan hết; không có phản ứng phụ

*Ghi chú:* 71 = 2 × 35,5 (khối lượng 2 gốc Cl- ứng với 1 mol H2).

<sub>`chemistry.thpt.kim-loai-axit-loang.hcl-khoi-luong-muoi` · lớp 11, 12 · #vo-co #axit-loang #khoi-luong-muoi</sub>

---

**Kim loại tác dụng với H2SO4 loãng: số mol axit và khối lượng muối** — *Metals with dilute sulfuric acid: acid moles and salt mass*

$$n_{H_2SO_4} = n_{H_2};\quad m_{muoi} = m_{KL} + 96n_{H_2}$$

Trong đó: `n_{H_2SO_4}` là số mol H2SO4 loãng phản ứng (mol); `n_{H_2}` là số mol khí H2 thoát ra (mol); `m_{muoi}` là khối lượng muối sunfat khan (g); `m_{KL}` là khối lượng kim loại phản ứng (g).

*Điều kiện:* Kim loại đứng trước H; H2SO4 loãng (không thể hiện tính oxi hóa của S+6)

*Ghi chú:* Fe tạo muối Fe(II) với axit loãng, nhưng tạo muối Fe(III) với HNO3 hoặc H2SO4 đặc nóng dư.

<sub>`chemistry.thpt.kim-loai-axit-loang.h2so4-loang-khoi-luong-muoi` · lớp 11, 12 · #vo-co #axit-loang #khoi-luong-muoi</sub>

---

**Kim loại tác dụng với hỗn hợp HCl và H2SO4 loãng** — *Metals with a mixture of hydrochloric and dilute sulfuric acid*

$$m_{muoi} = m_{KL} + 35{,}5n_{HCl} + 96n_{H_2SO_4};\quad n_{H_2} = \dfrac{n_{HCl} + 2n_{H_2SO_4}}{2}$$

Trong đó: `m_{muoi}` là tổng khối lượng muối khan (g); `m_{KL}` là khối lượng kim loại phản ứng (g); `n_{HCl}` là số mol HCl phản ứng (mol); `n_{H_2SO_4}` là số mol H2SO4 phản ứng (mol); `n_{H_2}` là số mol khí H2 thoát ra (mol).

*Điều kiện:* Cả hai axit phản ứng hết; kim loại tan hết

*Ghi chú:* Tổng quát: n(H+) = 2n(H2); khối lượng muối = m(kim loại) + m(gốc axit).

<sub>`chemistry.thpt.kim-loai-axit-loang.hon-hop-hai-axit` · lớp 11, 12 · #vo-co #axit-loang #bao-toan-khoi-luong</sub>

---

### Lập công thức phân tử hợp chất hữu cơ

**Khối lượng hợp chất hữu cơ tính theo sản phẩm cháy** — *Mass of an organic compound from its combustion products*

$$m_X = 12n_{CO_2} + 2n_{H_2O} + 16n_{O(X)} + 28n_{N_2}$$

Trong đó: `m_X` là khối lượng hợp chất hữu cơ X đem đốt (g); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{O(X)}` là số mol nguyên tử oxi có trong X (mol); `n_{N_2}` là số mol N2 sinh ra (mol).

*Điều kiện:* Đốt cháy hoàn toàn X (chứa C, H và có thể có O, N) trong oxi dư

*Ghi chú:* Suy từ m(X) = m(C) + m(H) + m(O) + m(N), trong đó m(N) = 14·2n(N2) = 28n(N2). Kết hợp bảo toàn khối lượng: m(X) + 32n(O2) = 44n(CO2) + 18n(H2O) + 28n(N2).

<sub>`chemistry.thpt.huu-co.khoi-luong-theo-san-pham-chay` · lớp 11, 12 · #huu-co #dot-chay #bao-toan-khoi-luong</sub>

---

**Độ bất bão hòa của phân tử hợp chất hữu cơ** — *Degree of unsaturation*

$$k = \dfrac{2C + 2 + N - H - X}{2}$$

Trong đó: `k` là độ bất bão hòa, bằng tổng số liên kết pi và số vòng; `C` là số nguyên tử cacbon (hóa trị IV); `N` là số nguyên tử nitơ (hóa trị III); `H` là số nguyên tử hiđro; `X` là số nguyên tử halogen (F, Cl, Br, I).

*Điều kiện:* k phải là số nguyên không âm; nguyên tử oxi và lưu huỳnh (hóa trị II) không ảnh hưởng đến k

*Ghi chú:* k = 0: no mạch hở; k = 1: 1 liên kết đôi hoặc 1 vòng; k = 4 với vòng benzen. Đây là điều kiện kiểm tra tính hợp lí của công thức phân tử.

<sub>`chemistry.thpt.huu-co.do-bat-bao-hoa` · lớp 11, 12 · #huu-co #do-bat-bao-hoa #lap-cong-thuc</sub>

---

### Oxit kim loại tác dụng với axit

**Oxit kim loại tác dụng với H2SO4 loãng** — *Metal oxides reacting with dilute sulfuric acid*

$$n_{H_2SO_4} = n_{O};\quad m_{muoi} = m_{oxit} + 80n_{O}$$

Trong đó: `n_{H_2SO_4}` là số mol H2SO4 loãng phản ứng (mol); `n_{O}` là số mol nguyên tử oxi trong oxit (mol); `m_{muoi}` là khối lượng muối sunfat khan (g); `m_{oxit}` là khối lượng oxit ban đầu (g).

*Điều kiện:* Oxit bazơ tan hết; H2SO4 loãng

*Ghi chú:* 80 = 96 − 16 (thay 1 O bằng 1 gốc SO4^2-).

<sub>`chemistry.thpt.oxit-axit.oxit-tac-dung-h2so4` · lớp 11, 12 · #vo-co #oxit #khoi-luong-muoi</sub>

---

**Oxit kim loại tác dụng với HCl** — *Metal oxides reacting with hydrochloric acid*

$$n_{HCl} = 2n_{O};\quad m_{muoi} = m_{oxit} + 55n_{O}$$

Trong đó: `n_{HCl}` là số mol HCl phản ứng (mol); `n_{O}` là số mol nguyên tử oxi trong oxit (mol); `m_{muoi}` là khối lượng muối clorua khan (g); `m_{oxit}` là khối lượng oxit ban đầu (g).

*Điều kiện:* Oxit bazơ tan hết trong axit; không có phản ứng oxi hóa khử

*Ghi chú:* 55 = 2·35,5 − 16 (thay 1 O bằng 2 Cl). Cũng có thể viết n(H2O) = n(O).

<sub>`chemistry.thpt.oxit-axit.oxit-tac-dung-hcl` · lớp 11, 12 · #vo-co #oxit #khoi-luong-muoi</sub>

---

### Phản ứng đặc trưng của hợp chất hữu cơ

**Phản ứng cộng brom vào liên kết pi** — *Bromine addition to pi bonds*

$$n_{Br_2} = n_{\pi} = k \cdot n_X$$

Trong đó: `n_{Br_2}` là số mol brom đã phản ứng cộng (mol); `n_{\pi}` là số mol liên kết pi ở gốc hiđrocacbon (mol); `k` là số liên kết pi cộng được brom trong một phân tử; `n_X` là số mol hợp chất không no (mol).

*Điều kiện:* Brom trong dung dịch (nước brom hoặc CCl4); mỗi liên kết pi C=C hoặc C≡C cộng 1 phân tử Br2

*Ghi chú:* Anken cộng 1 Br2, ankin và ankađien cộng 2 Br2. Anđehit làm mất màu nước brom do bị oxi hóa (RCHO + Br2 + H2O → RCOOH + 2HBr).

<sub>`chemistry.thpt.phan-ung.cong-br2` · lớp 11, 12 · #huu-co #phan-ung-cong #brom</sub>

---

**Phản ứng cộng hiđro và độ giảm số mol khí** — *Hydrogenation and the decrease in gas moles*

$$n_{H_2\ pu} = n_{truoc} - n_{sau};\quad m_{truoc} = m_{sau} \Rightarrow n_{truoc}\overline{M}_{truoc} = n_{sau}\overline{M}_{sau}$$

Trong đó: `n_{H_2\ pu}` là số mol H2 đã phản ứng (mol); `n_{truoc}` là tổng số mol hỗn hợp khí trước phản ứng (mol); `n_{sau}` là tổng số mol hỗn hợp khí sau phản ứng (mol); `m_{truoc}` là khối lượng hỗn hợp trước phản ứng (g); `m_{sau}` là khối lượng hỗn hợp sau phản ứng (g); `\overline{M}_{truoc}` là khối lượng mol trung bình trước phản ứng (g/mol); `\overline{M}_{sau}` là khối lượng mol trung bình sau phản ứng (g/mol).

*Điều kiện:* Phản ứng trong bình kín, xúc tác Ni, nung nóng; hỗn hợp trước và sau đều ở thể khí

*Ghi chú:* Mỗi mol H2 cộng vào làm giảm đúng 1 mol khí. Khối lượng hỗn hợp không đổi nên M trung bình tăng.

<sub>`chemistry.thpt.phan-ung.cong-h2` · lớp 11, 12 · #huu-co #phan-ung-cong #bao-toan-khoi-luong</sub>

---

**Số mol liên kết pi trong hợp chất mạch hở** — *Moles of pi bonds in an open-chain compound*

$$n_{\pi} = k \cdot n_X$$

Trong đó: `n_{\pi}` là tổng số mol liên kết pi (mol); `k` là số liên kết pi trong một phân tử (bằng độ bất bão hòa nếu mạch hở); `n_X` là số mol chất X (mol).

*Điều kiện:* Phân tử mạch hở (không có vòng); chỉ tính các liên kết pi ở gốc hiđrocacbon nếu xét phản ứng cộng

*Ghi chú:* Liên kết pi trong nhóm -COOH, -COO- và vòng benzen KHÔNG cộng brom trong dung dịch.

<sub>`chemistry.thpt.phan-ung.so-mol-lien-ket-pi` · lớp 11, 12 · #huu-co #phan-ung-cong #do-bat-bao-hoa</sub>

---

**Phản ứng este hóa và hiệu suất** — *Esterification reaction and its yield*

$$RCOOH + R'OH \rightleftharpoons RCOOR' + H_2O;\quad H = \dfrac{n_{este}}{n_{bd(thieu)}} \times 100\%$$

Trong đó: `R` là gốc hiđrocacbon (hoặc H) của axit; `R'` là gốc hiđrocacbon của ancol; `H` là hiệu suất phản ứng este hóa (%); `n_{este}` là số mol este thực tế thu được (mol); `n_{bd(thieu)}` là số mol ban đầu của chất phản ứng thiếu (mol).

*Điều kiện:* Xúc tác H2SO4 đặc, đun nóng; phản ứng thuận nghịch nên hiệu suất luôn nhỏ hơn 100%

*Ghi chú:* Để tăng hiệu suất: dùng dư một chất, tách bớt este hoặc nước ra khỏi hỗn hợp.

<sub>`chemistry.thpt.phan-ung.este-hoa` · lớp 11, 12 · #huu-co #este-hoa #hieu-suat</sub>

---

**Hằng số cân bằng của phản ứng este hóa** — *Equilibrium constant of esterification*

$$K_C = \dfrac{[RCOOR'] \cdot [H_2O]}{[RCOOH] \cdot [R'OH]}$$

Trong đó: `K_C` là hằng số cân bằng tính theo nồng độ; `[RCOOR']` là nồng độ mol của este lúc cân bằng (mol/L); `[H_2O]` là nồng độ mol của nước lúc cân bằng (mol/L); `[RCOOH]` là nồng độ mol của axit lúc cân bằng (mol/L); `[R'OH]` là nồng độ mol của ancol lúc cân bằng (mol/L).

*Điều kiện:* Hệ đã đạt trạng thái cân bằng ở nhiệt độ xác định; các chất đều ở cùng một pha lỏng

*Ghi chú:* Vì cùng thể tích nên có thể thay nồng độ bằng số mol. Với CH3COOH và C2H5OH, Kc xấp xỉ 4 nên hiệu suất tối đa khoảng 67% khi trộn tỉ lệ 1 : 1.

<sub>`chemistry.thpt.phan-ung.hang-so-can-bang-este-hoa` · lớp 11, 12 · #huu-co #este-hoa #can-bang-hoa-hoc</sub>

---

**Phản ứng tráng bạc của anđehit** — *Silver mirror reaction of aldehydes*

$$RCHO + 2AgNO_3 + 3NH_3 + H_2O \xrightarrow{t^o} RCOONH_4 + 2Ag \downarrow + 2NH_4NO_3;\quad n_{Ag} = 2n_{CHO}$$

Trong đó: `n_{Ag}` là số mol bạc kết tủa (mol); `n_{CHO}` là tổng số mol nhóm chức -CHO (mol); `R` là gốc hiđrocacbon hoặc H.

*Điều kiện:* Anđehit tác dụng với dung dịch AgNO3 trong NH3, đun nóng

*Ghi chú:* Ngoại lệ: HCHO cho 4 mol Ag vì bị oxi hóa hai nấc. Nếu n(Ag)/n(anđehit đơn chức) = 4 thì đó là HCHO. HCOOH và HCOOR cũng tráng bạc cho 2Ag.

<sub>`chemistry.thpt.phan-ung.trang-bac-andehit` · lớp 11, 12 · #huu-co #trang-bac #andehit</sub>

---

**Axit cacboxylic tác dụng với Na, NaOH và NaHCO3** — *Carboxylic acids with sodium, sodium hydroxide and hydrogencarbonate*

$$n_{H_2} = \dfrac{n_{COOH}}{2};\quad n_{NaOH} = n_{COOH};\quad n_{CO_2} = n_{COOH}$$

Trong đó: `n_{H_2}` là số mol H2 khi cho tác dụng Na (mol); `n_{COOH}` là tổng số mol nhóm -COOH (mol); `n_{NaOH}` là số mol NaOH cần để trung hòa (mol); `n_{CO_2}` là số mol CO2 khi tác dụng với NaHCO3 dư (mol).

*Điều kiện:* Na dư, NaOH vừa đủ, NaHCO3 dư

*Ghi chú:* Phản ứng với NaHCO3 sinh CO2 dùng để phân biệt axit cacboxylic với phenol và ancol.

<sub>`chemistry.thpt.phan-ung.axit-tac-dung-na` · lớp 11, 12 · #huu-co #axit-cacboxylic #nhan-biet</sub>

---

### Đếm đồng phân hợp chất hữu cơ

**Số đồng phân axit cacboxylic no, đơn chức, mạch hở** — *Number of isomers of saturated monocarboxylic acids*

$$S = 2^{\,n-3}\quad (2 < n < 7)$$

Trong đó: `S` là số đồng phân axit; `n` là số nguyên tử cacbon của axit CnH2nO2.

*Điều kiện:* Công thức đúng với n = 3, 4, 5, 6

*Ghi chú:* n = 4 cho 2 đồng phân axit (butanoic và 2-metylpropanoic), n = 5 cho 4 đồng phân.

<sub>`chemistry.thpt.dong-phan.axit-no-don-chuc` · lớp 11, 12 · #huu-co #dem-dong-phan #axit-cacboxylic</sub>

---

### Động học phản ứng bậc THPT quốc tế

**Xấp xỉ tiền cân bằng khi bước đầu không phải bước chậm** — *Pre-equilibrium approximation when the first step is not rate limiting*

$$K_{1} = \dfrac{[I]}{[A][B]} \Rightarrow [I] = K_{1}[A][B] \Rightarrow v = k_{2}[I][C] = k_{2}K_{1}[A][B][C]$$

Trong đó: `K_{1}` là hằng số cân bằng của bước sơ cấp thứ nhất (nhanh, thuận nghịch) (L/mol); `[I]` là nồng độ chất trung gian sinh ra ở bước một (mol/L); `[A]` là nồng độ chất tham gia A trong bước một (mol/L); `[B]` là nồng độ chất tham gia B trong bước một (mol/L); `k_{2}` là hằng số tốc độ của bước hai, là bước quyết định tốc độ (L/(mol*s)); `[C]` là nồng độ chất tham gia C trong bước quyết định tốc độ (mol/L); `v` là tốc độ chung của phản ứng (mol/(L*s)).

*Điều kiện:* Bước một đạt cân bằng nhanh trước khi bước hai kịp xảy ra; dùng để KHỬ nồng độ chất trung gian ra khỏi biểu thức tốc độ vì chất trung gian không đo được

*Ghi chú:* Đây là Topic 5.9 'Pre-Equilibrium Approximation' của AP Chemistry, một topic RIÊNG trong CED: 'If the first elementary reaction is not rate limiting, approximations (such as pre-equilibrium) must be made to determine a rate law expression'. IB HL và A-Level chỉ yêu cầu cơ chế mà bước đầu là bước chậm (khi đó biểu thức tốc độ đọc thẳng từ bước một). Dấu hiệu nhận dạng trên đề: biểu thức tốc độ thực nghiệm có bậc ÂM hoặc bậc PHÂN SỐ theo một chất thì gần như chắc chắn phải dùng tiền cân bằng. CT GDPT 2018 Việt Nam không dạy cơ chế nhiều bước ở THPT.

<sub>`chemistry.thpt.dong-hoc-tich-phan.xap-xi-tien-can-bang` · lớp 11, 12 · #ap #co-che #tien-can-bang #chat-trung-gian</sub>

---

### Amin, amino axit và peptit

**Số mắt xích và số liên kết peptit** — *Number of residues and peptide bonds*

$$k = \dfrac{n_{NaOH}}{n_{peptit}};\quad \text{số liên kết peptit} = k - 1$$

Trong đó: `k` là số mắt xích amino axit trong phân tử peptit; `n_{NaOH}` là số mol NaOH cần để thủy phân hoàn toàn peptit (mol); `n_{peptit}` là số mol peptit (mol).

*Điều kiện:* Peptit chỉ tạo từ các amino axit có một nhóm -NH2 và một nhóm -COOH

*Ghi chú:* Peptit có từ 2 liên kết peptit trở lên (từ tripeptit) mới cho phản ứng màu biure với Cu(OH)2.

<sub>`chemistry.thpt.peptit.so-lien-ket-va-mat-xich` · lớp 12 · #huu-co #peptit #thuy-phan</sub>

---

**Thủy phân peptit trong dung dịch HCl** — *Peptide hydrolysis in hydrochloric acid solution*

$$m_{muoi} = m_{peptit} + 18(k-1)n_{peptit} + 36{,}5\,n_{HCl},\quad n_{HCl} = k\,n_{peptit}$$

Trong đó: `m_{muoi}` là khối lượng muối clorua của các amino axit (g); `m_{peptit}` là khối lượng peptit (g); `k` là số mắt xích của peptit; `n_{peptit}` là số mol peptit (mol); `n_{HCl}` là số mol HCl phản ứng (mol).

*Điều kiện:* Peptit tạo từ amino axit có 1 nhóm NH2 và 1 nhóm COOH; HCl vừa đủ

*Ghi chú:* Khác với NaOH, thủy phân bằng HCl cần (k − 1) mol H2O cho mỗi mol peptit và HCl cộng vào nhóm -NH2.

<sub>`chemistry.thpt.peptit.tac-dung-hcl` · lớp 12 · #huu-co #peptit #bao-toan-khoi-luong</sub>

---

**Thủy phân peptit trong dung dịch NaOH** — *Peptide hydrolysis in sodium hydroxide solution*

$$m_{muoi} = m_{peptit} + 40\,n_{NaOH} - 18\,n_{peptit},\quad n_{NaOH} = k\,n_{peptit}$$

Trong đó: `m_{muoi}` là khối lượng muối natri của các amino axit (g); `m_{peptit}` là khối lượng peptit (g); `n_{NaOH}` là số mol NaOH phản ứng (mol); `n_{peptit}` là số mol peptit (mol); `k` là số mắt xích của peptit.

*Điều kiện:* NaOH vừa đủ; mỗi mol peptit khi thủy phân bằng kiềm chỉ giải phóng 1 mol H2O

*Ghi chú:* Nếu NaOH dư thì chất rắn sau cô cạn còn chứa NaOH dư, phải cộng thêm khối lượng đó.

<sub>`chemistry.thpt.peptit.tac-dung-naoh` · lớp 12 · #huu-co #peptit #bao-toan-khoi-luong</sub>

---

**Bảo toàn khối lượng khi thủy phân hoàn toàn peptit** — *Mass balance in complete peptide hydrolysis*

$$m_{peptit} + 18\,n_{H_2O} = m_{amino\ axit},\quad n_{H_2O} = (k-1)\,n_{peptit}$$

Trong đó: `m_{peptit}` là khối lượng peptit đem thủy phân (g); `n_{H_2O}` là số mol nước tham gia thủy phân (mol); `m_{amino\ axit}` là tổng khối lượng amino axit thu được (g); `k` là số mắt xích của peptit; `n_{peptit}` là số mol peptit (mol).

*Điều kiện:* Thủy phân hoàn toàn trong môi trường trung tính hoặc có xúc tác enzim

*Ghi chú:* Thủy phân không hoàn toàn thì n(H2O) = số liên kết peptit bị cắt; luôn có n(H2O) = n(sản phẩm) − n(peptit ban đầu).

<sub>`chemistry.thpt.peptit.thuy-phan-bao-toan-khoi-luong` · lớp 12 · #huu-co #peptit #bao-toan-khoi-luong</sub>

---

**Amin tác dụng với dung dịch HCl** — *Amines reacting with hydrochloric acid*

$$n_{HCl} = a \cdot n_{amin};\quad m_{muoi} = m_{amin} + 36{,}5\,n_{HCl}$$

Trong đó: `n_{HCl}` là số mol HCl phản ứng (mol); `a` là số nhóm chức amin (-NH2) trong một phân tử; `n_{amin}` là số mol amin (mol); `m_{muoi}` là khối lượng muối amoni clorua thu được (g); `m_{amin}` là khối lượng amin ban đầu (g).

*Điều kiện:* HCl vừa đủ; đây là hệ quả của định luật bảo toàn khối lượng

*Ghi chú:* M(HCl) = 36,5 g/mol. Tỉ lệ n(HCl)/n(amin) cho biết số nhóm chức amin.

<sub>`chemistry.thpt.amin.tac-dung-hcl` · lớp 12 · #huu-co #amin #bao-toan-khoi-luong</sub>

---

**Amino axit tác dụng lần lượt với HCl rồi NaOH** — *Amino acid treated successively with acid then base*

$$n_{NaOH\ tong} = n_{HCl\ ban\ dau} + b\,n_{aa};\quad n_{HCl\ tong} = n_{NaOH\ ban\ dau} + a\,n_{aa}$$

Trong đó: `n_{NaOH\ tong}` là tổng số mol NaOH cần dùng ở giai đoạn sau (mol); `n_{HCl\ ban\ dau}` là số mol HCl đã dùng ở giai đoạn đầu (mol); `n_{HCl\ tong}` là tổng số mol HCl cần dùng ở giai đoạn sau (mol); `n_{NaOH\ ban\ dau}` là số mol NaOH đã dùng ở giai đoạn đầu (mol); `a` là số nhóm -NH2 trong phân tử; `b` là số nhóm -COOH trong phân tử; `n_{aa}` là số mol amino axit (mol).

*Điều kiện:* Phản ứng xảy ra hoàn toàn; có thể coi như cho hỗn hợp amino axit và axit (hoặc bazơ) phản ứng cùng lúc

*Ghi chú:* Mẹo giải: quy về bài toán trung hòa, dùng bảo toàn khối lượng cho toàn bộ quá trình.

<sub>`chemistry.thpt.amino-axit.hai-giai-doan` · lớp 12 · #huu-co #amino-axit #giai-nhanh</sub>

---

**Amino axit tác dụng với HCl và với NaOH** — *Amino acids reacting with hydrochloric acid and sodium hydroxide*

$$n_{HCl} = a\,n_{aa},\ m_{muoi} = m_{aa} + 36{,}5n_{HCl};\quad n_{NaOH} = b\,n_{aa},\ m_{muoi} = m_{aa} + 22n_{NaOH}$$

Trong đó: `n_{HCl}` là số mol HCl phản ứng (mol); `n_{NaOH}` là số mol NaOH phản ứng (mol); `a` là số nhóm -NH2 trong phân tử amino axit; `b` là số nhóm -COOH trong phân tử amino axit; `n_{aa}` là số mol amino axit (mol); `m_{aa}` là khối lượng amino axit (g); `m_{muoi}` là khối lượng muối tương ứng (g).

*Điều kiện:* Axit hoặc bazơ dùng vừa đủ; amino axit là chất lưỡng tính

*Ghi chú:* 22 = 23 − 1 (thay H của -COOH bằng Na). Nếu a = b thì dung dịch amino axit có môi trường gần trung tính.

<sub>`chemistry.thpt.amino-axit.tac-dung-hcl-naoh` · lớp 12 · #huu-co #amino-axit #luong-tinh</sub>

---

**Số đipeptit, tripeptit tối đa tạo từ n amino axit** — *Maximum number of dipeptides and tripeptides from n amino acids*

$$\text{số đipeptit} = n^2,\quad \text{số tripeptit} = n^3,\quad \text{số } k\text{-peptit} = n^k$$

Trong đó: `n` là số loại amino axit khác nhau dùng để tạo peptit; `k` là số mắt xích của peptit.

*Điều kiện:* Mỗi amino axit có 1 nhóm NH2 và 1 nhóm COOH; cho phép một amino axit lặp lại nhiều lần trong mạch

*Ghi chú:* Nếu yêu cầu peptit chứa đủ n gốc amino axit khác nhau, mỗi loại đúng một lần, thì số peptit là n! (giai thừa).

<sub>`chemistry.thpt.peptit.so-dipeptit-tripeptit` · lớp 12 · #huu-co #peptit #dem-dong-phan</sub>

---

### Bài toán đốt cháy hợp chất hữu cơ

**Đốt cháy amin no, đơn chức, mạch hở** — *Combustion of saturated monofunctional amines*

$$n_{amin} = \dfrac{2\left(n_{H_2O} - n_{CO_2}\right)}{3} = 2n_{N_2};\quad n_{O_2} = \dfrac{6n+3}{4}n_{amin}$$

Trong đó: `n_{amin}` là số mol amin CnH2n+3N bị đốt (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{N_2}` là số mol khí N2 sinh ra (mol); `n_{O_2}` là số mol O2 cần dùng (mol); `n` là số nguyên tử cacbon của amin.

*Điều kiện:* Amin no, đơn chức, mạch hở CnH2n+3N; đốt cháy hoàn toàn trong O2, nitơ chuyển hết thành N2

*Ghi chú:* Vì n(H2O) − n(CO2) = 1,5n(amin) nên với amin no đơn chức hở luôn có n(H2O) > n(CO2).

<sub>`chemistry.thpt.dot-chay.amin-no-don-chuc` · lớp 12 · #huu-co #dot-chay #amin</sub>

---

**Đốt cháy amino axit no, mạch hở, có một nhóm NH2 và một nhóm COOH** — *Combustion of a saturated amino acid with one amino and one carboxyl group*

$$C_nH_{2n+1}NO_2:\quad n_{H_2O} - n_{CO_2} = \dfrac{n_{aa}}{2} = n_{N_2};\quad n_{O_2} = \dfrac{6n-3}{4}\,n_{aa}$$

Trong đó: `n` là số nguyên tử cacbon của amino axit; `n_{aa}` là số mol amino axit bị đốt (mol); `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{N_2}` là số mol N2 sinh ra (mol); `n_{O_2}` là số mol O2 cần dùng (mol).

*Điều kiện:* Amino axit no, mạch hở CnH2n+1NO2 (n ≥ 2); đốt cháy hoàn toàn, toàn bộ nitơ chuyển thành N2

*Ghi chú:* Glyxin C2H5NO2 và alanin C3H7NO2 thuộc dãy này. Vì n(H2O) − n(CO2) = 0,5n(aa) > 0 nên luôn có n(H2O) > n(CO2).

<sub>`chemistry.thpt.dot-chay.amino-axit` · lớp 12 · #huu-co #dot-chay #amino-axit</sub>

---

**Đốt cháy este no, đơn chức, mạch hở** — *Combustion of saturated monofunctional esters*

$$n_{CO_2} = n_{H_2O};\quad n_{O_2} = \dfrac{3}{2}n_{CO_2} - n_{este}$$

Trong đó: `n_{CO_2}` là số mol CO2 sinh ra (mol); `n_{H_2O}` là số mol H2O sinh ra (mol); `n_{O_2}` là số mol O2 cần dùng (mol); `n_{este}` là số mol este CnH2nO2 bị đốt (mol).

*Điều kiện:* Este no, đơn chức, mạch hở CnH2nO2 (n ≥ 2); đốt cháy hoàn toàn

*Ghi chú:* Suy từ bảo toàn oxi: 2n(este) + 2n(O2) = 3n(CO2). Este không no 1 nối đôi đơn chức hở CnH2n-2O2 cho n(CO2) − n(H2O) = n(este).

<sub>`chemistry.thpt.dot-chay.este-no-don-chuc` · lớp 12 · #huu-co #dot-chay #este</sub>

---

### Cacbohiđrat

**Số mắt xích trong phân tử tinh bột hoặc xenlulozơ** — *Number of monomer units in starch or cellulose*

$$n = \dfrac{M_{polisaccarit}}{162}$$

Trong đó: `n` là số mắt xích C6H10O5 trong một phân tử; `M_{polisaccarit}` là khối lượng mol phân tử của tinh bột hoặc xenlulozơ (g/mol).

*Điều kiện:* M là giá trị trung bình vì polisaccarit là hỗn hợp các phân tử có độ dài mạch khác nhau

*Ghi chú:* M(C6H10O5) = 162 g/mol. Xenlulozơ có n từ khoảng 10000 đến 14000, lớn hơn tinh bột.

<sub>`chemistry.thpt.cacbohidrat.so-mat-xich-polisaccarit` · lớp 12 · #huu-co #cacbohidrat #polime</sub>

---

**Hiệu suất lên men rượu từ glucozơ** — *Yield of alcoholic fermentation of glucose*

$$C_6H_{12}O_6 \xrightarrow{men\ ruou} 2C_2H_5OH + 2CO_2;\quad m_{C_2H_5OH} = \dfrac{92\,m_{glucozo}}{180} \cdot H$$

Trong đó: `m_{C_2H_5OH}` là khối lượng ancol etylic thu được (g); `m_{glucozo}` là khối lượng glucozơ đem lên men (g); `H` là hiệu suất phản ứng lên men (dạng thập phân).

*Điều kiện:* Lên men ở 30-35 °C với men rượu; H là hiệu suất của cả quá trình

*Ghi chú:* n(CO2) = 2·n(glucozơ)·H; hấp thụ CO2 vào nước vôi trong dư cho n(CaCO3) = n(CO2). Khối lượng riêng của C2H5OH nguyên chất là 0,789 g/mL.

<sub>`chemistry.thpt.cacbohidrat.len-men-ruou` · lớp 12 · #huu-co #cacbohidrat #len-men #hieu-suat</sub>

---

**Khử glucozơ bằng hiđro tạo sobitol** — *Reduction of glucose to sorbitol*

$$C_6H_{12}O_6 + H_2 \xrightarrow{Ni,\ t^o} C_6H_{14}O_6;\quad n_{H_2} = n_{glucozo}$$

Trong đó: `n_{H_2}` là số mol H2 phản ứng (mol); `n_{glucozo}` là số mol glucozơ tham gia (mol).

*Điều kiện:* Xúc tác Ni, đun nóng; chỉ nhóm -CHO bị khử

*Ghi chú:* M(sobitol C6H14O6) = 182 g/mol. Fructozơ cũng bị khử thành sobitol.

<sub>`chemistry.thpt.cacbohidrat.glucozo-tac-dung-h2` · lớp 12 · #huu-co #cacbohidrat #phan-ung-cong</sub>

---

**Điều chế xenlulozơ trinitrat từ xenlulozơ và HNO3** — *Preparation of cellulose trinitrate from cellulose and nitric acid*

$$[C_6H_7O_2(OH)_3]_n + 3nHNO_3 \xrightarrow{H_2SO_4\ dac} [C_6H_7O_2(ONO_2)_3]_n + 3nH_2O;\quad m_{sp} = \dfrac{297}{162}\,m_{xenlulozo} \cdot H$$

Trong đó: `m_{sp}` là khối lượng xenlulozơ trinitrat thu được (g); `m_{xenlulozo}` là khối lượng xenlulozơ ban đầu (g); `H` là hiệu suất phản ứng (dạng thập phân); `n` là hệ số polime hóa của xenlulozơ.

*Điều kiện:* HNO3 đặc, xúc tác H2SO4 đặc, đun nóng; mỗi mắt xích có 3 nhóm -OH được este hóa

*Ghi chú:* M(mắt xích xenlulozơ) = 162, M(mắt xích trinitrat) = 297. Xenlulozơ trinitrat là thuốc súng không khói.

<sub>`chemistry.thpt.cacbohidrat.xenlulozo-trinitrat` · lớp 12 · #huu-co #cacbohidrat #xenlulozo</sub>

---

**Thủy phân tinh bột hoặc xenlulozơ thành glucozơ** — *Hydrolysis of starch or cellulose to glucose*

$$(C_6H_{10}O_5)_n + nH_2O \xrightarrow{H^+,\ t^o} nC_6H_{12}O_6;\quad m_{glucozo} = \dfrac{180}{162}\,m_{tinh\ bot} \cdot H$$

Trong đó: `m_{glucozo}` là khối lượng glucozơ thu được (g); `m_{tinh\ bot}` là khối lượng tinh bột (hoặc xenlulozơ) đem thủy phân (g); `H` là hiệu suất phản ứng thủy phân (dạng thập phân); `n` là hệ số polime hóa.

*Điều kiện:* Xúc tác axit hoặc enzim; thủy phân hoàn toàn cho sản phẩm duy nhất là glucozơ

*Ghi chú:* Tỉ lệ 180/162 = 10/9. Thủy phân saccarozơ (C12H22O11) cho 1 glucozơ và 1 fructozơ, tỉ lệ khối lượng 360/342.

<sub>`chemistry.thpt.cacbohidrat.thuy-phan-tinh-bot` · lớp 12 · #huu-co #cacbohidrat #thuy-phan</sub>

---

**Thủy phân saccarozơ** — *Hydrolysis of sucrose*

$$C_{12}H_{22}O_{11} + H_2O \xrightarrow{H^+,\ t^o} C_6H_{12}O_6\,(\text{glucozơ}) + C_6H_{12}O_6\,(\text{fructozơ});\quad n_{glucozo} = n_{fructozo} = H\,n_{saccarozo}$$

Trong đó: `n_{glucozo}` là số mol glucozơ tạo thành (mol); `n_{fructozo}` là số mol fructozơ tạo thành (mol); `n_{saccarozo}` là số mol saccarozơ đem thủy phân (mol); `H` là hiệu suất thủy phân (dạng thập phân).

*Điều kiện:* Xúc tác axit hoặc enzim, đun nóng; 0 < H ≤ 1

*Ghi chú:* M(saccarozơ) = 342 g/mol. Saccarozơ KHÔNG tráng bạc nhưng sản phẩm thủy phân thì có: n(Ag) = 4n(saccarozơ đã thủy phân) vì cả glucozơ và fructozơ đều cho 2Ag.

<sub>`chemistry.thpt.cacbohidrat.thuy-phan-saccarozo` · lớp 12 · #huu-co #cacbohidrat #thuy-phan</sub>

---

### Công thức tổng quát các dãy đồng đẳng

**Công thức tổng quát của amin** — *General formula of amines*

$$C_xH_yN_z\ (y \le 2x + 2 + z,\ y \equiv z \ (\mathrm{mod}\ 2));\quad \text{amin no, đơn chức, mạch hở}: C_nH_{2n+3}N\ (n \ge 1)$$

Trong đó: `x` là số nguyên tử cacbon; `y` là số nguyên tử hiđro; `z` là số nguyên tử nitơ; `n` là số nguyên tử cacbon của amin no đơn chức.

*Điều kiện:* Số nguyên tử H và số nguyên tử N phải cùng tính chẵn lẻ

*Ghi chú:* M(CnH2n+3N) = 14n + 17. CH3NH2 (31), C2H5NH2 (45), C6H5NH2 anilin (93).

<sub>`chemistry.thpt.cttq.amin` · lớp 12 · #huu-co #cong-thuc-tong-quat #amin</sub>

---

**Công thức tổng quát của amino axit** — *General formula of amino acids*

$$(H_2N)_a R (COOH)_b;\quad \text{no, 1 nhóm } NH_2,\ 1 \text{ nhóm } COOH: C_nH_{2n+1}NO_2\ (n \ge 2)$$

Trong đó: `a` là số nhóm amino -NH2; `b` là số nhóm cacboxyl -COOH; `R` là gốc hiđrocacbon; `n` là số nguyên tử cacbon.

*Điều kiện:* n ≥ 2 với amino axit no mạch hở có 1 nhóm NH2 và 1 nhóm COOH

*Ghi chú:* Glyxin C2H5NO2 (75), alanin C3H7NO2 (89), valin C5H11NO2 (117), lysin C6H14N2O2 (146), axit glutamic C5H9NO4 (147).

<sub>`chemistry.thpt.cttq.amino-axit` · lớp 12 · #huu-co #cong-thuc-tong-quat #amino-axit</sub>

---

**Công thức phân tử các cacbohiđrat quan trọng** — *Molecular formulas of the main carbohydrates*

$$\begin{cases} \text{glucozơ, fructozơ}: C_6H_{12}O_6 & (M = 180) \\ \text{saccarozơ, mantozơ}: C_{12}H_{22}O_{11} & (M = 342) \\ \text{tinh bột, xenlulozơ}: (C_6H_{10}O_5)_n & (M = 162n) \end{cases}$$

Trong đó: `n` là hệ số polime hóa của tinh bột hoặc xenlulozơ; `M` là khối lượng mol phân tử (g/mol).

*Điều kiện:* Cacbohiđrat có công thức chung Cm(H2O)n

*Ghi chú:* Xenlulozơ còn viết [C6H7O2(OH)3]n, mỗi mắt xích có 3 nhóm -OH tự do.

<sub>`chemistry.thpt.cttq.cacbohidrat` · lớp 12 · #huu-co #cacbohidrat #cong-thuc-tong-quat</sub>

---

**Công thức tổng quát của chất béo (triglixerit)** — *General formula of fats (triglycerides)*

$$(RCOO)_3C_3H_5\ \text{hay}\ \begin{matrix} CH_2-OOCR_1 \\ CH-OOCR_2 \\ CH_2-OOCR_3 \end{matrix}$$

Trong đó: `R` là gốc hiđrocacbon của axit béo; `R_1` là gốc axit béo thứ nhất; `R_2` là gốc axit béo thứ hai; `R_3` là gốc axit béo thứ ba; `C_3H_5` là gốc glixerol (propan-1,2,3-triyl).

*Điều kiện:* Chất béo là trieste của glixerol với các axit béo (axit monocacboxylic mạch không phân nhánh, số C chẵn, thường 12-24 C)

*Ghi chú:* Axit béo thường gặp: panmitic C15H31COOH (M = 256), stearic C17H35COOH (M = 284), oleic C17H33COOH (M = 282), linoleic C17H31COOH (M = 280). Tristearin M = 890.

<sub>`chemistry.thpt.cttq.chat-beo` · lớp 12 · #huu-co #cong-thuc-tong-quat #chat-beo</sub>

---

**Công thức tổng quát của este no, đơn chức, mạch hở** — *General formula of saturated monofunctional esters*

$$RCOOR' \equiv C_nH_{2n}O_2\ (n \ge 2),\ R' \ne H$$

Trong đó: `R` là gốc hiđrocacbon (hoặc H) của phần axit; `R'` là gốc hiđrocacbon của phần ancol, khác H; `n` là số nguyên tử cacbon trong phân tử este.

*Điều kiện:* n ≥ 2; no, đơn chức, mạch hở

*Ghi chú:* M = 14n + 32; este no đơn chức mạch hở là đồng phân của axit no đơn chức mạch hở cùng số C.

<sub>`chemistry.thpt.cttq.este-no-don-chuc` · lớp 12 · #huu-co #cong-thuc-tong-quat #este</sub>

---

**Công thức và khối lượng mol của peptit tạo từ amino axit** — *Formula and molar mass of a peptide*

$$M_{peptit} = \sum_{i=1}^{n} M_{aa_i} - 18(n-1)$$

Trong đó: `M_{peptit}` là khối lượng mol của peptit (g/mol); `M_{aa_i}` là khối lượng mol của amino axit thứ i (g/mol); `n` là số mắt xích (số gốc amino axit) trong phân tử peptit.

*Điều kiện:* Peptit tạo thành từ n phân tử amino axit, tách ra (n − 1) phân tử H2O

*Ghi chú:* Số liên kết peptit = n − 1. Peptit từ 2-10 gốc là oligopeptit, từ 11-50 gốc là polipeptit.

<sub>`chemistry.thpt.cttq.peptit` · lớp 12 · #huu-co #peptit #cong-thuc-tong-quat</sub>

---

**Công thức chung của polime** — *General formula of polymers*

$$\left(-\text{mắt xích}-\right)_n;\quad M_{polime} = n \cdot M_{mat\ xich}$$

Trong đó: `n` là hệ số polime hóa (độ polime hóa), bằng số mắt xích; `M_{polime}` là khối lượng mol trung bình của polime (g/mol); `M_{mat\ xich}` là khối lượng mol của một mắt xích (g/mol).

*Điều kiện:* n là số nguyên rất lớn; M(polime) là giá trị trung bình

*Ghi chú:* PE (-CH2-CH2-)n M(mắt xích) = 28; PVC (-CH2-CHCl-)n = 62,5; PS = 104; nilon-6,6 = 226; cao su buna = 54.

<sub>`chemistry.thpt.cttq.polime` · lớp 12 · #huu-co #polime #cong-thuc-tong-quat</sub>

---

**Cấu tạo của protein** — *Structure of proteins*

$$\left[-NH-CHR-CO-\right]_n \quad (n > 50)$$

Trong đó: `R` là gốc hiđrocacbon (khác nhau ở mỗi mắt xích); `n` là số mắt xích amino axit trong chuỗi polipeptit.

*Điều kiện:* Protein đơn giản là polipeptit có phân tử khối từ vài chục nghìn đến vài triệu đvC

*Ghi chú:* Protein cho phản ứng màu biure với Cu(OH)2 (màu tím) và bị đông tụ khi đun nóng hoặc gặp axit, bazơ, muối kim loại nặng.

<sub>`chemistry.thpt.cttq.protein` · lớp 12 · #huu-co #protein #peptit</sub>

---

### Este và chất béo

**Chỉ số axit của chất béo** — *Acid value of a fat*

$$A = \dfrac{m_{KOH}\,(\text{mg})}{m_{chat\ beo}\,(\text{g})} = \dfrac{56000 \cdot n_{COOH\ tu\ do}}{m_{chat\ beo}}$$

Trong đó: `A` là chỉ số axit (số mg KOH cần trung hòa axit béo tự do trong 1 gam chất béo) (mg/g); `m_{KOH}` là khối lượng KOH cần dùng để trung hòa, tính bằng miligam (mg); `m_{chat\ beo}` là khối lượng mẫu chất béo, tính bằng gam (g); `n_{COOH\ tu\ do}` là số mol nhóm -COOH của axit béo tự do (mol).

*Điều kiện:* Chỉ tính phần axit béo tự do, không tính phần este

*Ghi chú:* M(KOH) = 56 g/mol nên 1 mol KOH ứng với 56000 mg. Chỉ số axit càng cao thì chất béo càng kém chất lượng.

<sub>`chemistry.thpt.chat-beo.chi-so-axit` · lớp 12 · #huu-co #chat-beo #chi-so</sub>

---

**Chỉ số iot của chất béo** — *Iodine value of a fat*

$$I = \dfrac{254 \cdot n_{I_2}}{m_{chat\ beo}} \times 100$$

Trong đó: `I` là chỉ số iot (số gam I2 cộng vào 100 gam chất béo) (g/(100 g)); `n_{I_2}` là số mol I2 cộng vào lượng chất béo khảo sát (mol); `m_{chat\ beo}` là khối lượng chất béo khảo sát, tính bằng gam (g).

*Điều kiện:* I2 cộng vào các liên kết đôi C=C của gốc axit béo không no theo tỉ lệ 1 : 1

*Ghi chú:* M(I2) = 254 g/mol. Chỉ số iot càng lớn thì chất béo càng chứa nhiều gốc axit béo không no (càng lỏng).

<sub>`chemistry.thpt.chat-beo.chi-so-iot` · lớp 12 · #huu-co #chat-beo #chi-so</sub>

---

**Chỉ số xà phòng hóa và chỉ số este** — *Saponification value and ester value*

$$S = \dfrac{56000\left(n_{COOH\ tu\ do} + 3n_{chat\ beo}\right)}{m_{chat\ beo}};\quad E = S - A$$

Trong đó: `S` là chỉ số xà phòng hóa (số mg KOH để xà phòng hóa este và trung hòa axit tự do trong 1 gam chất béo) (mg/g); `E` là chỉ số este (số mg KOH chỉ dùng để xà phòng hóa este trong 1 gam chất béo) (mg/g); `A` là chỉ số axit (mg/g); `n_{COOH\ tu\ do}` là số mol axit béo tự do (mol); `n_{chat\ beo}` là số mol triglixerit (mol); `m_{chat\ beo}` là khối lượng mẫu chất béo, tính bằng gam (g).

*Điều kiện:* Mẫu chất béo gồm triglixerit và một lượng axit béo tự do

*Ghi chú:* Luôn có S > A; chỉ số este E đặc trưng cho lượng triglixerit trong mẫu.

<sub>`chemistry.thpt.chat-beo.chi-so-xa-phong-hoa` · lớp 12 · #huu-co #chat-beo #chi-so</sub>

---

**Hiđro hóa chất béo lỏng thành chất béo rắn** — *Hydrogenation of liquid fats to solid fats*

$$n_{H_2} = k \cdot n_{chat\ beo};\quad m_{chat\ beo\ ran} = m_{chat\ beo\ long} + 2n_{H_2}$$

Trong đó: `n_{H_2}` là số mol H2 đã cộng vào (mol); `k` là số liên kết đôi C=C ở gốc hiđrocacbon của một phân tử chất béo; `n_{chat\ beo}` là số mol chất béo (mol); `m_{chat\ beo\ ran}` là khối lượng chất béo rắn thu được (g); `m_{chat\ beo\ long}` là khối lượng chất béo lỏng ban đầu (g).

*Điều kiện:* Xúc tác Ni, đun nóng, áp suất cao; chỉ cộng vào liên kết đôi C=C, không cộng vào C=O của nhóm este

*Ghi chú:* Triolein (C17H33COO)3C3H5 có k = 3, cộng 3H2 tạo tristearin (M từ 884 lên 890).

<sub>`chemistry.thpt.chat-beo.hidro-hoa` · lớp 12 · #huu-co #chat-beo #phan-ung-cong</sub>

---

**Khối lượng xà phòng thu được** — *Mass of soap obtained*

$$m_{xa\ phong} = m_{chat\ beo} + 40n_{NaOH} - 92n_{glixerol}$$

Trong đó: `m_{xa\ phong}` là khối lượng muối của axit béo (xà phòng) (g); `m_{chat\ beo}` là khối lượng chất béo đem xà phòng hóa (g); `n_{NaOH}` là số mol NaOH phản ứng (mol); `n_{glixerol}` là số mol glixerol sinh ra (mol).

*Điều kiện:* NaOH vừa đủ, phản ứng hoàn toàn; đây chính là định luật bảo toàn khối lượng

*Ghi chú:* Nếu dùng KOH: m(xà phòng) = m(chất béo) + 56n(KOH) − 92n(glixerol).

<sub>`chemistry.thpt.chat-beo.khoi-luong-xa-phong` · lớp 12 · #huu-co #chat-beo #bao-toan-khoi-luong</sub>

---

**Xà phòng hóa chất béo: lượng kiềm và glixerol** — *Saponification of fats: alkali and glycerol amounts*

$$n_{NaOH} = 3n_{chat\ beo};\quad n_{glixerol} = n_{chat\ beo}$$

Trong đó: `n_{NaOH}` là số mol NaOH cần dùng (mol); `n_{chat\ beo}` là số mol chất béo (triglixerit) (mol); `n_{glixerol}` là số mol glixerol C3H5(OH)3 sinh ra (mol).

*Điều kiện:* Thủy phân hoàn toàn trong môi trường kiềm, đun nóng

*Ghi chú:* M(glixerol) = 92 g/mol. Nếu dùng KOH thì n(KOH) = 3n(chất béo), M(KOH) = 56.

<sub>`chemistry.thpt.chat-beo.xa-phong-hoa` · lớp 12 · #huu-co #chat-beo #xa-phong-hoa</sub>

---

**Bảo toàn khối lượng khi thủy phân este trong NaOH** — *Mass balance for ester saponification with sodium hydroxide*

$$m_{este} + 40n_{NaOH} = m_{muoi} + m_{ancol};\quad n_{NaOH} = a \cdot n_{este}$$

Trong đó: `m_{este}` là khối lượng este đem thủy phân (g); `n_{NaOH}` là số mol NaOH phản ứng (mol); `m_{muoi}` là khối lượng muối cacboxylat khan (g); `m_{ancol}` là khối lượng ancol sinh ra (g); `a` là số nhóm chức este trong một phân tử; `n_{este}` là số mol este đem thủy phân (mol).

*Điều kiện:* NaOH vừa đủ; nếu NaOH dư thì khi cô cạn phải cộng thêm khối lượng NaOH dư vào chất rắn

*Ghi chú:* Este của phenol cần 2 mol NaOH cho 1 nhóm chức và tạo hai muối, không tạo ancol.

<sub>`chemistry.thpt.este.thuy-phan-naoh-btkl` · lớp 12 · #huu-co #este #bao-toan-khoi-luong</sub>

---

### Khử oxit kim loại

**Quy đổi hỗn hợp Fe và các oxit sắt tác dụng với axit có tính oxi hóa mạnh** — *Converting an iron and iron-oxide mixture using the 0.7m + 5.6ne rule*

$$m_{Fe} = 0{,}7m + 5{,}6n_e$$

Trong đó: `m_{Fe}` là khối lượng Fe có trong hỗn hợp ban đầu (g); `m` là khối lượng hỗn hợp gồm Fe, FeO, Fe3O4, Fe2O3 (g); `n_e` là số mol electron mà sản phẩm khử (NO, NO2, SO2...) nhận (mol).

*Điều kiện:* Hỗn hợp chỉ gồm Fe và các oxit sắt; tan hết trong HNO3 hoặc H2SO4 đặc nóng tạo muối Fe(III)

*Ghi chú:* Suy ra từ hệ: 56x + 16y = m và 3x = 2y + n(e) với x = n(Fe), y = n(O). Hệ quả: n(Fe) = (m + 8n_e)/80.

<sub>`chemistry.thpt.oxit-axit.quy-doi-fe-oxit-sat` · lớp 12 · #vo-co #sat #quy-doi #giai-nhanh</sub>

---

**Quy đổi hỗn hợp oxit sắt thành Fe và O** — *Reducing an iron oxide mixture to Fe and O components*

$$\begin{cases} 56n_{Fe} + 16n_{O} = m_{hh} \\ n_{H^+} = 2n_{O} + 2n_{H_2} \end{cases}$$

Trong đó: `m_{hh}` là khối lượng hỗn hợp Fe và các oxit sắt (g); `n_{Fe}` là số mol nguyên tử Fe trong hỗn hợp (mol); `n_{O}` là số mol nguyên tử O trong hỗn hợp (mol); `n_{H^+}` là số mol ion H+ của axit không có tính oxi hóa (HCl, H2SO4 loãng) (mol); `n_{H_2}` là số mol khí H2 thoát ra (mol).

*Điều kiện:* Mọi hỗn hợp Fe/FeO/Fe2O3/Fe3O4 đều quy về hai nguyên tố Fe và O

*Ghi chú:* Fe3O4 có thể quy đổi thành FeO·Fe2O3 hoặc thành hỗn hợp Fe và O tùy bài.

<sub>`chemistry.thpt.oxit-axit.quy-doi-hon-hop-sat-hcl` · lớp 12 · #vo-co #sat #quy-doi</sub>

---

### Kim loại tác dụng với dung dịch muối

**Độ tăng (giảm) khối lượng thanh kim loại nhúng vào dung dịch muối** — *Mass change of a metal bar immersed in a salt solution*

$$\Delta m = m_{KL\ bam\ vao} - m_{KL\ tan\ ra} = M_B n_B - M_A n_A$$

Trong đó: `\Delta m` là độ biến thiên khối lượng thanh kim loại (dương là tăng) (g); `m_{KL\ bam\ vao}` là khối lượng kim loại B bám vào thanh (g); `m_{KL\ tan\ ra}` là khối lượng kim loại A đã tan ra (g); `M_A` là khối lượng mol kim loại A (thanh kim loại) (g/mol); `M_B` là khối lượng mol kim loại B (trong muối) (g/mol); `n_A` là số mol kim loại A tan ra (mol); `n_B` là số mol kim loại B sinh ra bám vào thanh (mol).

*Điều kiện:* Kim loại A mạnh hơn B (đứng trước B trong dãy điện hóa) và không tan trong nước; toàn bộ B sinh ra bám hết vào thanh

*Ghi chú:* Áp dụng bảo toàn electron: a·n_A = b·n_B với a, b lần lượt là hóa trị của A và B.

<sub>`chemistry.thpt.kim-loai-muoi.tang-giam-khoi-luong` · lớp 12 · #vo-co #kim-loai #tang-giam-khoi-luong</sub>

---

### Kim loại tác dụng với nước

**Kim loại kiềm, kim loại kiềm thổ tác dụng với nước** — *Alkali and alkaline earth metals reacting with water*

$$M + nH_2O \rightarrow M(OH)_n + \dfrac{n}{2}H_2 \uparrow;\quad n_{OH^-} = 2n_{H_2} = n_e$$

Trong đó: `M` là kim loại kiềm (n = 1) hoặc Ca, Sr, Ba (n = 2); `n` là hóa trị của kim loại M; `n_{H_2}` là số mol khí H2 thoát ra (mol); `n_{OH^-}` là số mol ion OH- trong dung dịch thu được (mol); `n_e` là số mol electron kim loại nhường (mol).

*Điều kiện:* Các kim loại kiềm (Li, Na, K, Rb, Cs) và Ca, Sr, Ba tan trong nước ở nhiệt độ thường; Be không phản ứng, Mg phản ứng rất chậm

*Ghi chú:* Khối lượng dung dịch tăng = m(kim loại) − 2n(H2) vì M(H2) = 2 g/mol. Dung dịch kiềm thu được thường dùng tiếp cho bài toán CO2 hoặc Al.

<sub>`chemistry.thpt.kim-loai-nuoc.kiem-kiem-tho-tac-dung-nuoc` · lớp 12 · #vo-co #kim-loai-kiem #kiem-tho</sub>

---

### Muối nhôm, kẽm tác dụng với kiềm

**Dung dịch NaAlO2 tác dụng với axit (hai nghiệm)** — *Aluminate solution reacting with acid, two solutions*

$$\begin{cases} n_{H^+} = n_{\downarrow} & \text{(axit thiếu)} \\ n_{H^+} = 4n_{AlO_2^-} - 3n_{\downarrow} & \text{(axit dư, kết tủa tan một phần)} \end{cases}$$

Trong đó: `n_{H^+}` là số mol axit (ion H+) cần dùng (mol); `n_{\downarrow}` là số mol kết tủa Al(OH)3 thu được (mol); `n_{AlO_2^-}` là số mol ion aluminat ban đầu (mol).

*Điều kiện:* n(kết tủa) < n(AlO2-); nếu dung dịch còn OH- dư phải cộng thêm n(OH-) vào cả hai nghiệm

*Ghi chú:* AlO2- + H+ + H2O → Al(OH)3; Al(OH)3 + 3H+ → Al3+ + 3H2O. Dùng CO2 dư thì kết tủa KHÔNG tan.

<sub>`chemistry.thpt.nhom-kem.aluminat-tac-dung-axit` · lớp 12 · #vo-co #nhom #hai-nghiem</sub>

---

**Bài toán ngược: tính n(OH-) khi biết lượng kết tủa Al(OH)3 (hai nghiệm)** — *Two solutions for hydroxide amount from a given Al(OH)3 precipitate*

$$\begin{cases} n_{OH^-} = 3n_{\downarrow} & \text{(OH}^- \text{ thiếu)} \\ n_{OH^-} = 4n_{Al^{3+}} - n_{\downarrow} & \text{(OH}^- \text{ dư, kết tủa tan một phần)} \end{cases}$$

Trong đó: `n_{OH^-}` là số mol OH- cần tìm (mol); `n_{\downarrow}` là số mol kết tủa Al(OH)3 thu được (mol); `n_{Al^{3+}}` là số mol Al3+ ban đầu (mol).

*Điều kiện:* n(kết tủa) < n(Al3+); nếu dung dịch còn H+ dư phải cộng thêm n(H+) vào cả hai nghiệm

*Ghi chú:* Giá trị lớn nhất của n(OH-) ứng với nghiệm thứ hai, nhỏ nhất ứng với nghiệm thứ nhất.

<sub>`chemistry.thpt.nhom-kem.bai-toan-nguoc-al3` · lớp 12 · #vo-co #nhom #hai-nghiem</sub>

---

**Hỗn hợp Na và Al tan hết trong nước** — *Sodium and aluminium mixture dissolving completely in water*

$$n_{H_2} = \dfrac{1}{2}n_{Na} + \dfrac{3}{2}n_{Al}\quad \text{với điều kiện } n_{Na} \ge n_{Al}$$

Trong đó: `n_{H_2}` là số mol khí H2 thoát ra (mol); `n_{Na}` là số mol natri (mol); `n_{Al}` là số mol nhôm (mol).

*Điều kiện:* Hỗn hợp tan hoàn toàn trong nước dư, tức là n(NaOH sinh ra) = n(Na) ≥ n(Al)

*Ghi chú:* Nếu n(Na) < n(Al) thì Al chỉ tan một phần: n(Al phản ứng) = n(Na).

<sub>`chemistry.thpt.nhom-kem.hon-hop-na-al-vao-nuoc` · lớp 12 · #vo-co #nhom #kim-loai-kiem</sub>

---

**Kết tủa Zn(OH)2 khi cho kiềm vào dung dịch Zn2+** — *Zinc hydroxide precipitate versus hydroxide added*

$$n_{\downarrow} = \begin{cases} \dfrac{n_{OH^-}}{2} & \text{khi } n_{OH^-} \le 2n_{Zn^{2+}} \\[4pt] \dfrac{4n_{Zn^{2+}} - n_{OH^-}}{2} & \text{khi } 2n_{Zn^{2+}} < n_{OH^-} < 4n_{Zn^{2+}} \\[4pt] 0 & \text{khi } n_{OH^-} \ge 4n_{Zn^{2+}} \end{cases}$$

Trong đó: `n_{\downarrow}` là số mol kết tủa Zn(OH)2 (mol); `n_{OH^-}` là số mol OH- cho vào (mol); `n_{Zn^{2+}}` là số mol Zn2+ ban đầu (mol).

*Điều kiện:* Kiềm mạnh; kết tủa cực đại khi n(OH-) = 2n(Zn2+), tan hết khi n(OH-) ≥ 4n(Zn2+)

*Ghi chú:* Zn(OH)2 tan cả trong kiềm dư (tạo ZnO2^2-) và trong NH3 dư (tạo phức [Zn(NH3)4]2+), khác Al(OH)3.

<sub>`chemistry.thpt.nhom-kem.ket-tua-zn-theo-oh` · lớp 12 · #vo-co #kem #luong-tinh</sub>

---

**Điều kiện kết tủa Al(OH)3 cực đại và tan hết** — *Conditions for maximum and complete dissolution of aluminium hydroxide*

$$\begin{cases} n_{OH^-} = 3n_{Al^{3+}} & \Rightarrow \text{kết tủa cực đại } n_{\downarrow} = n_{Al^{3+}} \\ n_{OH^-} \ge 4n_{Al^{3+}} & \Rightarrow \text{kết tủa tan hết} \end{cases}$$

Trong đó: `n_{OH^-}` là số mol OH- cho vào (mol); `n_{Al^{3+}}` là số mol ion Al3+ ban đầu (mol); `n_{\downarrow}` là số mol kết tủa Al(OH)3 (mol).

*Điều kiện:* Kiềm mạnh (NaOH, KOH, Ba(OH)2); dung dịch không chứa axit dư hay ion khác phản ứng với OH-

*Ghi chú:* Al3+ + 3OH- → Al(OH)3; Al(OH)3 + OH- → AlO2- + 2H2O. Với NH3 dư thì Al(OH)3 KHÔNG tan.

<sub>`chemistry.thpt.nhom-kem.ket-tua-al-cuc-dai` · lớp 12 · #vo-co #nhom #kiem</sub>

---

**Số mol kết tủa Al(OH)3 theo số mol OH-** — *Moles of Al(OH)3 as a function of hydroxide added*

$$n_{\downarrow} = \begin{cases} \dfrac{n_{OH^-}}{3} & \text{khi } n_{OH^-} \le 3n_{Al^{3+}} \\[4pt] 4n_{Al^{3+}} - n_{OH^-} & \text{khi } 3n_{Al^{3+}} < n_{OH^-} < 4n_{Al^{3+}} \\[4pt] 0 & \text{khi } n_{OH^-} \ge 4n_{Al^{3+}} \end{cases}$$

Trong đó: `n_{\downarrow}` là số mol kết tủa Al(OH)3 còn lại (mol); `n_{OH^-}` là số mol OH- đã cho vào (mol); `n_{Al^{3+}}` là số mol Al3+ ban đầu (mol).

*Điều kiện:* Dung dịch chỉ chứa Al3+ (không có H+ dư); kiềm mạnh

*Ghi chú:* Đồ thị n(kết tủa) theo n(OH-) là đường gấp khúc lên với hệ số 1/3 rồi xuống với hệ số -1.

<sub>`chemistry.thpt.nhom-kem.ket-tua-al-theo-oh` · lớp 12 · #vo-co #nhom #do-thi</sub>

---

**Nhôm tác dụng với dung dịch kiềm** — *Aluminium reacting with alkali solution*

$$Al + NaOH + H_2O \rightarrow NaAlO_2 + \tfrac{3}{2}H_2 \uparrow;\quad n_{H_2} = \dfrac{3}{2}n_{Al},\ \ n_{NaOH} = n_{Al}$$

Trong đó: `n_{Al}` là số mol nhôm phản ứng (mol); `n_{H_2}` là số mol khí hiđro thoát ra (mol); `n_{NaOH}` là số mol NaOH phản ứng (mol).

*Điều kiện:* NaOH đủ hoặc dư; Al tan hết

*Ghi chú:* Zn cũng tan trong kiềm: Zn + 2NaOH → Na2ZnO2 + H2, với n(H2) = n(Zn).

<sub>`chemistry.thpt.nhom-kem.al-tac-dung-naoh` · lớp 12 · #vo-co #nhom #kiem</sub>

---

### Nước cứng

**Nguyên tắc và lượng hóa chất làm mềm nước cứng** — *Principle and reagent amount for water softening*

$$n_{Na_2CO_3} \ge n_{Ca^{2+}} + n_{Mg^{2+}};\quad n_{Ca(OH)_2} = n_{HCO_3^-}/2 \ (\text{với nước cứng tạm thời})$$

Trong đó: `n_{Na_2CO_3}` là số mol Na2CO3 tối thiểu cần dùng (mol); `n_{Ca^{2+}}` là số mol ion Ca2+ (mol); `n_{Mg^{2+}}` là số mol ion Mg2+ (mol); `n_{Ca(OH)_2}` là số mol Ca(OH)2 vừa đủ (mol); `n_{HCO_3^-}` là số mol ion hiđrocacbonat (mol).

*Điều kiện:* Nguyên tắc: làm giảm nồng độ Ca2+, Mg2+ bằng cách kết tủa hoặc trao đổi ion

*Ghi chú:* Na2CO3 và Na3PO4 làm mềm được cả hai loại nước cứng; đun sôi hoặc Ca(OH)2 vừa đủ chỉ làm mềm nước cứng tạm thời.

<sub>`chemistry.thpt.nuoc-cung.lam-mem-nuoc` · lớp 12 · #vo-co #nuoc-cung #ung-dung</sub>

---

**Độ cứng của nước và phân loại** — *Water hardness and its classification*

$$\text{Độ cứng} \propto \left(C_{Ca^{2+}} + C_{Mg^{2+}}\right);\ \begin{cases} \text{tạm thời}: HCO_3^- \\ \text{vĩnh cửu}: Cl^-,\ SO_4^{2-} \\ \text{toàn phần}: \text{cả hai} \end{cases}$$

Trong đó: `C_{Ca^{2+}}` là nồng độ mol ion canxi trong nước (mol/L); `C_{Mg^{2+}}` là nồng độ mol ion magie trong nước (mol/L).

*Điều kiện:* Nước cứng là nước chứa nhiều ion Ca2+ và Mg2+

*Ghi chú:* Nước mềm là nước chứa ít hoặc không chứa Ca2+, Mg2+.

<sub>`chemistry.thpt.nuoc-cung.do-cung-tong-cong` · lớp 12 · #vo-co #nuoc-cung #kim-loai-kiem-tho</sub>

---

### Phản ứng nhiệt nhôm

**Hiệu suất phản ứng nhiệt nhôm** — *Yield of the thermite reaction*

$$H = \dfrac{n_{pu}}{n_{bd}} \times 100\%$$

Trong đó: `H` là hiệu suất phản ứng (%); `n_{pu}` là số mol chất đã phản ứng của chất thiếu (mol); `n_{bd}` là số mol ban đầu của chất thiếu (mol).

*Điều kiện:* Hiệu suất luôn tính theo chất phản ứng hết trước (chất thiếu)

*Ghi chú:* Hỗn hợp sau phản ứng tác dụng NaOH dư sinh H2 chứng tỏ còn Al dư, khi đó hiệu suất tính theo oxit.

<sub>`chemistry.thpt.nhiet-nhom.hieu-suat` · lớp 12 · #vo-co #nhiet-nhom #hieu-suat</sub>

---

**Phản ứng nhiệt nhôm và định luật bảo toàn khối lượng** — *Thermite reaction and mass conservation*

$$2Al + Fe_2O_3 \xrightarrow{t^o} Al_2O_3 + 2Fe;\quad m_{truoc} = m_{sau}$$

Trong đó: `m_{truoc}` là khối lượng hỗn hợp trước phản ứng (g); `m_{sau}` là khối lượng hỗn hợp rắn sau phản ứng (g).

*Điều kiện:* Phản ứng thực hiện trong điều kiện không có không khí

*Ghi chú:* Có thể dùng bảo toàn nguyên tố: n(Al ban đầu) = 2n(Al2O3) + n(Al dư); n(Fe) + 2n(Fe2O3 dư) = 2n(Fe2O3 ban đầu).

<sub>`chemistry.thpt.nhiet-nhom.phuong-trinh-va-bao-toan` · lớp 12 · #vo-co #nhiet-nhom #bao-toan-khoi-luong</sub>

---

### Phản ứng đặc trưng của hợp chất hữu cơ

**Phản ứng tráng bạc của glucozơ** — *Silver mirror reaction of glucose*

$$n_{Ag} = 2n_{glucozo};\quad m_{Ag} = 216\,n_{glucozo}$$

Trong đó: `n_{Ag}` là số mol Ag kết tủa (mol); `n_{glucozo}` là số mol glucozơ (hoặc fructozơ) tham gia (mol); `m_{Ag}` là khối lượng bạc thu được (g).

*Điều kiện:* Dung dịch AgNO3/NH3, đun nóng; glucozơ có nhóm -CHO

*Ghi chú:* M(Ag) = 108 g/mol. Fructozơ cũng tráng bạc vì chuyển hóa thành glucozơ trong môi trường kiềm. Saccarozơ KHÔNG tráng bạc.

<sub>`chemistry.thpt.phan-ung.trang-bac-glucozo` · lớp 12 · #huu-co #trang-bac #cacbohidrat</sub>

---

### Polime và vật liệu polime

**Phần trăm lưu huỳnh trong cao su lưu hóa** — *Sulfur content of vulcanized rubber*

$$\%S = \dfrac{32a}{68k + 32a - 2} \times 100\%$$

Trong đó: `\%S` là phần trăm khối lượng lưu huỳnh trong cao su lưu hóa (%); `a` là số nguyên tử S trong một cầu nối lưu huỳnh (a = 1 cầu monosunfua, a = 2 cầu đisunfua); `k` là số mắt xích isopren C5H8 ứng với một cầu nối lưu huỳnh.

*Điều kiện:* Mỗi cầu nối lưu huỳnh thay thế 2 nguyên tử H ở hai mạch cao su nên khối lượng mắt xích giảm 2 đvC; M(C5H8) = 68 g/mol; k nguyên dương

*Ghi chú:* Với cầu đisunfua (a = 2): %S = 64/(68k + 62). Bài toán quen thuộc: cao su lưu hóa chứa 2% S thì 64/(68k + 62) = 0,02, suy ra k ≈ 46 mắt xích isopren có một cầu nối. %S càng lớn thì cao su càng cứng.

<sub>`chemistry.thpt.polime.cao-su-luu-hoa` · lớp 12 · #huu-co #polime #cao-su</sub>

---

**Clo hóa PVC điều chế tơ clorin** — *Chlorination of PVC to make chlorinated fibre*

$$\%Cl = \dfrac{35{,}5(k+1)}{62{,}5k + 34{,}5} \times 100\%$$

Trong đó: `\%Cl` là phần trăm khối lượng clo trong sản phẩm (%); `k` là số mắt xích PVC (-CH2-CHCl-) ứng với một phân tử Cl2 tham gia thế.

*Điều kiện:* Mỗi phân tử Cl2 thế một nguyên tử H và giải phóng một phân tử HCl

*Ghi chú:* Từ M(PVC k mắt xích) = 62,5k, sau khi thế: 62,5k + 71 − 36,5 = 62,5k + 34,5.

<sub>`chemistry.thpt.polime.clo-hoa-pvc` · lớp 12 · #huu-co #polime #pvc</sub>

---

**Hiệu suất phản ứng trùng hợp và trùng ngưng** — *Yield of polymerization and polycondensation*

$$H = \dfrac{m_{polime}}{m_{monome\ bd}} \times 100\%\ (\text{trùng hợp});\quad H = \dfrac{m_{polime}}{m_{monome\ bd} - m_{H_2O}} \times 100\%\ (\text{trùng ngưng})$$

Trong đó: `H` là hiệu suất phản ứng (%); `m_{polime}` là khối lượng polime thực tế thu được (g); `m_{monome\ bd}` là khối lượng monome ban đầu (g); `m_{H_2O}` là khối lượng nước tách ra theo lí thuyết trong trùng ngưng (g).

*Điều kiện:* Trùng hợp bảo toàn khối lượng nên khối lượng polime tối đa bằng khối lượng monome

*Ghi chú:* Nilon-6,6 điều chế bằng trùng ngưng hexametylenđiamin và axit ađipic, mỗi mắt xích tách 2 phân tử H2O.

<sub>`chemistry.thpt.polime.hieu-suat` · lớp 12 · #huu-co #polime #hieu-suat</sub>

---

**Hệ số trùng hợp (số mắt xích) của polime** — *Degree of polymerization*

$$n = \dfrac{M_{polime}}{M_{monome}}$$

Trong đó: `n` là hệ số trùng hợp, cũng là số mắt xích trong một phân tử polime; `M_{polime}` là khối lượng mol trung bình của polime (g/mol); `M_{monome}` là khối lượng mol của monome (bằng khối lượng mol của một mắt xích) (g/mol).

*Điều kiện:* Phản ứng trùng hợp: khối lượng mắt xích bằng khối lượng monome

*Ghi chú:* Với trùng ngưng thì M(mắt xích) = M(monome) − M(phân tử nhỏ tách ra), ví dụ nilon-6,6 tách H2O.

<sub>`chemistry.thpt.polime.he-so-trung-hop` · lớp 12 · #huu-co #polime #trung-hop</sub>

---

**Số mắt xích có trong một khối lượng polime** — *Number of monomer units in a given polymer mass*

$$N_{mat\ xich} = \dfrac{m_{polime}}{M_{mat\ xich}} \cdot N_A$$

Trong đó: `N_{mat\ xich}` là tổng số mắt xích; `m_{polime}` là khối lượng polime (g); `M_{mat\ xich}` là khối lượng mol của một mắt xích (g/mol); `N_A` là hằng số Avogadro (mol^-1).

*Điều kiện:* Polime đồng nhất, mắt xích xác định

*Ghi chú:* N_A = 6,022·10^23 mol^-1.

<sub>`chemistry.thpt.polime.so-mat-xich-theo-avogadro` · lớp 12 · #huu-co #polime #avogadro</sub>

---

**Phần trăm khối lượng nguyên tố trong polime** — *Mass percentage of an element in a polymer*

$$\%X = \dfrac{s \cdot M_X}{M_{mat\ xich}} \times 100\%$$

Trong đó: `\%X` là phần trăm khối lượng của nguyên tố X trong polime (%); `s` là số nguyên tử X trong một mắt xích; `M_X` là khối lượng mol nguyên tử của X (g/mol); `M_{mat\ xich}` là khối lượng mol của một mắt xích (g/mol).

*Điều kiện:* Bỏ qua ảnh hưởng của hai nhóm cuối mạch vì hệ số polime hóa rất lớn

*Ghi chú:* Ví dụ PVC (-CH2-CHCl-)n có M(mắt xích) = 62,5 nên %Cl = 35,5/62,5 = 56,8%.

<sub>`chemistry.thpt.polime.phan-tram-nguyen-to` · lớp 12 · #huu-co #polime #thanh-phan-nguyen-to</sub>

---

### Sắt và hợp chất

**Điều kiện tạo muối Fe(II) hay Fe(III) khi Fe tác dụng với HNO3** — *Condition for iron(II) or iron(III) salt with nitric acid*

$$\begin{cases} n_{Fe} \le \dfrac{n_e}{3} & \Rightarrow \text{chỉ tạo } Fe^{3+} \\[4pt] n_{Fe} \ge \dfrac{n_e}{2} & \Rightarrow \text{chỉ tạo } Fe^{2+},\ Fe \text{ có thể dư} \\[4pt] \dfrac{n_e}{3} < n_{Fe} < \dfrac{n_e}{2} & \Rightarrow \text{tạo cả } Fe^{2+} \text{ và } Fe^{3+} \end{cases}$$

Trong đó: `n_{Fe}` là số mol Fe tham gia phản ứng (mol); `n_e` là số mol electron mà sản phẩm khử nhận (mol).

*Điều kiện:* Fe tan hết hoặc còn dư; Fe dư sẽ khử tiếp Fe3+ thành Fe2+

*Ghi chú:* Fe + 2Fe(NO3)3 → 3Fe(NO3)2. Fe, Al, Cr bị thụ động trong HNO3 đặc nguội và H2SO4 đặc nguội.

<sub>`chemistry.thpt.sat.fe-tac-dung-hno3` · lớp 12 · #vo-co #sat #hno3 #bien-luan</sub>

---

### Điện hóa

**Phương trình Nernst** — *Nernst equation*

$$E = E^{0} - \dfrac{RT}{nF} \ln Q$$

Trong đó: `E` là thế điện cực (hoặc sức điện động) ở điều kiện không chuẩn (V); `E^{0}` là giá trị chuẩn tương ứng (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `n` là số mol electron trao đổi; `F` là hằng số Faraday (C/mol); `Q` là thương số phản ứng.

*Điều kiện:* Hệ điện hóa chưa đạt cân bằng; Q tính theo hoạt độ, gần đúng bằng nồng độ hoặc áp suất riêng phần

*Ghi chú:* Kiến thức nâng cao. Khi hệ đạt cân bằng thì E = 0 và Q = K.

<sub>`chemistry.thpt.dien-hoa.phuong-trinh-nernst` · lớp 12 · #nernst #the-dien-cuc #nang-cao</sub>

---

**Phương trình Nernst ở 25 độ C** — *Nernst equation at 25 C*

$$E = E^{0} - \dfrac{0.0592}{n} \log Q$$

Trong đó: `E` là thế điện cực hoặc sức điện động thực tế (V); `E^{0}` là giá trị chuẩn (V); `n` là số mol electron trao đổi; `Q` là thương số phản ứng.

*Điều kiện:* Nhiệt độ 298 K (25 độ C); hệ số 0.0592 V có được từ 2.303RT/F

*Ghi chú:* Kiến thức nâng cao. Cứ Q tăng 10 lần thì E giảm 0.0592/n vôn.

<sub>`chemistry.thpt.dien-hoa.phuong-trinh-nernst-25-do` · lớp 12 · #nernst #dien-hoa #nang-cao</sub>

---

**Quan hệ giữa biến thiên năng lượng Gibbs và sức điện động** — *Relation between Gibbs energy and cell potential*

$$\Delta G^{0} = -n F E^{0}_{pin}$$

Trong đó: `\Delta G^{0}` là biến thiên năng lượng tự do Gibbs chuẩn của phản ứng trong pin (J/mol); `n` là số mol electron trao đổi theo phương trình; `F` là hằng số Faraday (C/mol); `E^{0}_{pin}` là sức điện động chuẩn của pin (V).

*Điều kiện:* Phản ứng xảy ra trong pin ở điều kiện chuẩn

*Ghi chú:* F = 96 485 C/mol (thường làm tròn 96 500). E chuẩn của pin dương tương ứng Delta G chuẩn âm nên phản ứng tự xảy ra.

<sub>`chemistry.thpt.dien-hoa.quan-he-gibbs-va-suc-dien-dong` · lớp 12 · #gibbs #suc-dien-dong #faraday</sub>

---

**Quan hệ giữa sức điện động chuẩn và hằng số cân bằng** — *Relation between standard cell potential and equilibrium constant*

$$\log K = \dfrac{n E^{0}_{pin}}{0.0592} \quad (25\,^{\circ}\mathrm{C})$$

Trong đó: `K` là hằng số cân bằng của phản ứng xảy ra trong pin; `n` là số mol electron trao đổi; `E^{0}_{pin}` là sức điện động chuẩn của pin (V).

*Điều kiện:* Ở 25 độ C; suy ra từ Delta G chuẩn = -nFE chuẩn = -RT lnK

*Ghi chú:* Kiến thức nâng cao. E chuẩn của pin càng lớn thì K càng lớn, phản ứng càng xảy ra hoàn toàn.

<sub>`chemistry.thpt.dien-hoa.quan-he-suc-dien-dong-va-hang-so-can-bang` · lớp 12 · #suc-dien-dong #hang-so-can-bang #nang-cao</sub>

---

**Sức điện động chuẩn của pin điện hóa** — *Standard cell potential*

$$E^{0}_{pin} = E^{0}_{catot} - E^{0}_{anot} = E^{0}_{\text{cuc duong}} - E^{0}_{\text{cuc am}}$$

Trong đó: `E^{0}_{pin}` là sức điện động chuẩn của pin (V); `E^{0}_{catot}` là thế điện cực chuẩn của điện cực xảy ra sự khử (cực dương) (V); `E^{0}_{anot}` là thế điện cực chuẩn của điện cực xảy ra sự oxi hóa (cực âm) (V).

*Điều kiện:* Pin Galvani hoạt động ở điều kiện chuẩn; E chuẩn của pin luôn dương

*Ghi chú:* Trong pin Galvani, anode là cực âm (oxi hóa), cathode là cực dương (khử). Ví dụ pin Zn-Cu có E chuẩn = 0.340 - (-0.763) = 1.103 V.

<sub>`chemistry.thpt.dien-hoa.suc-dien-dong-cua-pin` · lớp 12 · #pin-dien-hoa #suc-dien-dong #galvani</sub>

---

**Quy tắc alpha xác định chiều phản ứng oxi hóa - khử** — *Alpha rule for redox reaction direction*

$$\text{Oxh manh} + \text{Kh manh} \rightarrow \text{Oxh yeu} + \text{Kh yeu} \;\Leftrightarrow\; E^{0}_{\text{cap chua chat oxi hoa}} > E^{0}_{\text{cap chua chat khu}}$$

Trong đó: `E^{0}_{\text{cap chua chat oxi hoa}}` là thế điện cực chuẩn của cặp oxi hóa - khử chứa chất oxi hóa tham gia phản ứng (V); `E^{0}_{\text{cap chua chat khu}}` là thế điện cực chuẩn của cặp oxi hóa - khử chứa chất khử tham gia phản ứng (V).

*Điều kiện:* So sánh hai cặp oxi hóa - khử ở điều kiện chuẩn

*Ghi chú:* Thế điện cực chuẩn được định nghĩa cho một cặp oxi hóa - khử, không phải cho riêng một chất. Phản ứng tự xảy ra khi sức điện động chuẩn của pin dương, tức E chuẩn của cặp nhận electron lớn hơn E chuẩn của cặp nhường electron.

<sub>`chemistry.thpt.dien-hoa.quy-tac-alpha` · lớp 12 · #quy-tac-alpha #the-dien-cuc #oxi-hoa-khu</sub>

---

**Thế điện cực chuẩn của cặp oxi hóa - khử** — *Standard electrode potential*

$$E^{0}_{\mathrm{M^{n+}/M}} \;:\; \mathrm{M^{n+}} + n e \rightleftharpoons \mathrm{M}, \quad E^{0}_{\mathrm{2H^{+}/H_{2}}} = 0.00\;\mathrm{V}$$

Trong đó: `E^{0}_{\mathrm{M^{n+}/M}}` là thế điện cực chuẩn của cặp oxi hóa - khử M(n+)/M (V); `n` là số electron trao đổi; `E^{0}_{\mathrm{2H^{+}/H_{2}}}` là thế điện cực chuẩn của cặp 2H+/H2, được quy ước bằng 0.00 V (điện cực hiđro chuẩn) (V).

*Điều kiện:* Điều kiện chuẩn: nồng độ ion 1 M, áp suất khí 1 bar, nhiệt độ 25 độ C; đo so với điện cực hiđro chuẩn

*Ghi chú:* E chuẩn càng lớn thì dạng oxi hóa càng mạnh và dạng khử càng yếu. Ví dụ E chuẩn của Zn2+/Zn là -0.763 V, của Cu2+/Cu là +0.340 V.

<sub>`chemistry.thpt.dien-hoa.the-dien-cuc-chuan` · lớp 12 · #the-dien-cuc #dien-hoa #thpt</sub>

---

**Điều kiện xảy ra ăn mòn điện hóa học** — *Conditions for electrochemical corrosion*

$$\begin{cases} \text{(1) Hai dien cuc khac ban chat (kim loai - kim loai hoac kim loai - phi kim)} \\ \text{(2) Hai dien cuc tiep xuc truc tiep hoac qua day dan} \\ \text{(3) Cung tiep xuc voi mot dung dich chat dien li} \end{cases}$$

Trong đó: `\text{dien cuc}` là cặp điện cực tạo thành pin điện hóa trong quá trình ăn mòn.

*Điều kiện:* Phải thỏa mãn đồng thời cả ba điều kiện

*Ghi chú:* Kim loại hoạt động mạnh hơn đóng vai trò cực âm (anode) và bị ăn mòn trước. Ứng dụng: bảo vệ vỏ tàu bằng khối kẽm hi sinh.

<sub>`chemistry.thpt.dien-hoa.an-mon-dien-hoa` · lớp 12 · #an-mon-dien-hoa #kim-loai #thpt</sub>

---

**Điện lượng đi qua bình điện phân** — *Charge passed through an electrolytic cell*

$$q = I \cdot t$$

Trong đó: `q` là điện lượng đi qua bình điện phân (C); `I` là cường độ dòng điện (A); `t` là thời gian điện phân (s).

*Điều kiện:* Dòng điện một chiều có cường độ không đổi

*Ghi chú:* 1 C = 1 A.s. Nhớ đổi thời gian ra giây trước khi tính.

<sub>`chemistry.thpt.dien-hoa.dien-luong` · lớp 12 · #dien-phan #dien-luong #thpt</sub>

---

**Định luật Faraday về điện phân** — *Faraday's law of electrolysis*

$$m = \dfrac{A \cdot I \cdot t}{n \cdot F}$$

Trong đó: `m` là khối lượng chất thoát ra ở điện cực (g); `A` là khối lượng mol nguyên tử của chất (g/mol); `I` là cường độ dòng điện (A); `t` là thời gian điện phân (s); `n` là số electron mà một nguyên tử (hoặc ion) trao đổi; `F` là hằng số Faraday (C/mol).

*Điều kiện:* Hiệu suất điện phân 100%; dòng điện một chiều không đổi

*Ghi chú:* F = 96 485 C/mol, thường làm tròn 96 500 C/mol trong bài tập phổ thông.

<sub>`chemistry.thpt.dien-hoa.dinh-luat-faraday` · lớp 12 · #faraday #dien-phan #thpt</sub>

---

**Số mol electron trao đổi trong điện phân** — *Moles of electrons in electrolysis*

$$n_{e} = \dfrac{I \cdot t}{F}$$

Trong đó: `n_{e}` là số mol electron trao đổi ở mỗi điện cực (mol); `I` là cường độ dòng điện (A); `t` là thời gian điện phân (s); `F` là hằng số Faraday (C/mol).

*Điều kiện:* Hiệu suất điện phân 100%; dòng điện không đổi

*Ghi chú:* F = 96 485 C/mol. Số mol electron ở catot luôn bằng số mol electron ở anot (bảo toàn electron).

<sub>`chemistry.thpt.dien-hoa.so-mol-electron-dien-phan` · lớp 12 · #dien-phan #faraday #bao-toan-electron</sub>

---

**Thời gian điện phân để thu được khối lượng chất xác định** — *Electrolysis time for a given mass*

$$t = \dfrac{m \cdot n \cdot F}{A \cdot I}$$

Trong đó: `t` là thời gian điện phân (s); `m` là khối lượng chất cần thu (g); `n` là số electron trao đổi của một nguyên tử hoặc ion; `F` là hằng số Faraday (C/mol); `A` là khối lượng mol nguyên tử (g/mol); `I` là cường độ dòng điện (A).

*Điều kiện:* Hiệu suất điện phân 100%

*Ghi chú:* Dạng biến đổi của định luật Faraday. Nếu hiệu suất là H% thì thời gian thực tế bằng t chia cho H/100.

<sub>`chemistry.thpt.dien-hoa.thoi-gian-dien-phan` · lớp 12 · #faraday #dien-phan #thoi-gian</sub>

---

**Thứ tự điện phân ở các điện cực trong dung dịch** — *Order of discharge at the electrodes*

$$\begin{cases} \text{Catot (khu)}: \mathrm{Ag^{+}} > \mathrm{Fe^{3+}} > \mathrm{Cu^{2+}} > \mathrm{H^{+}}_{(acid)} > \mathrm{Fe^{2+}} > \mathrm{Zn^{2+}} > \mathrm{H_{2}O} \\ \text{Anot (oxi hoa)}: \mathrm{S^{2-}} > \mathrm{I^{-}} > \mathrm{Br^{-}} > \mathrm{Cl^{-}} > \mathrm{H_{2}O} > \mathrm{SO_{4}^{2-}},\, \mathrm{NO_{3}^{-}} \end{cases}$$

Trong đó: `\text{Catot}` là cực âm của bình điện phân, nơi xảy ra sự khử; `\text{Anot}` là cực dương của bình điện phân, nơi xảy ra sự oxi hóa.

*Điều kiện:* Điện phân dung dịch với điện cực trơ (graphite hoặc platinum)

*Ghi chú:* Cation kim loại từ Al trở về trước (K+, Na+, Mg2+, Al3+) không bị khử trong dung dịch, khi đó nước bị khử: 2H2O + 2e -> H2 + 2OH-. Các anion SO4 2-, NO3- không bị oxi hóa, khi đó nước bị oxi hóa: 2H2O -> O2 + 4H+ + 4e.

<sub>`chemistry.thpt.dien-hoa.thu-tu-dien-phan` · lớp 12 · #dien-phan #catot #anot</sub>

---

### Điện phân

**Số mol electron trao đổi khi điện phân** — *Moles of electrons transferred during electrolysis*

$$n_e = \dfrac{It}{F} = \dfrac{It}{96500}$$

Trong đó: `n_e` là số mol electron đi qua mạch (mol); `I` là cường độ dòng điện (A); `t` là thời gian điện phân (s); `F` là hằng số Faraday (C/mol).

*Điều kiện:* Dòng điện không đổi; hiệu suất 100%

*Ghi chú:* Số mol electron ở catot luôn bằng số mol electron ở anot: đây là chìa khóa giải bài điện phân.

<sub>`chemistry.thpt.dien-phan.so-mol-electron` · lớp 12 · #vo-co #dien-phan #bao-toan-electron</sub>

---

**Khối lượng kim loại bám vào catot và độ giảm khối lượng dung dịch** — *Mass deposited at the cathode and the decrease in solution mass*

$$m_{catot} = \dfrac{A}{n}\,n_{e(KL)};\quad m_{dd\ giam} = m_{KL} + m_{khi}$$

Trong đó: `m_{catot}` là khối lượng kim loại bám vào catot (g); `A` là khối lượng mol nguyên tử của kim loại (g/mol); `n` là số electron mà một ion kim loại nhận; `n_{e(KL)}` là số mol electron dùng để khử ion kim loại đó (mol); `m_{dd\ giam}` là độ giảm khối lượng dung dịch sau điện phân (g); `m_{KL}` là khối lượng kim loại thoát ra ở catot (g); `m_{khi}` là tổng khối lượng khí thoát ra ở hai điện cực (g).

*Điều kiện:* Điện cực trơ, hiệu suất 100%; nếu nhiều cation cùng bị khử thì cộng theo đúng thứ tự điện phân, phần electron dư dùng để khử nước

*Ghi chú:* Ví dụ điện phân dung dịch CuSO4: m(catot) = 64·n_e/2 = 32n_e và khối lượng dung dịch giảm = m(Cu) + m(O2).

<sub>`chemistry.thpt.dien-phan.khoi-luong-catot` · lớp 12 · #vo-co #dien-phan #catot</sub>

---

**Số mol khí thoát ra ở các điện cực khi điện phân** — *Moles of gas evolved at the electrodes*

$$n_{Cl_2} = \dfrac{n_e}{2},\quad n_{O_2} = \dfrac{n_e}{4},\quad n_{H_2} = \dfrac{n_e}{2};\quad V = 24{,}79\,n\ (\text{đkc}) = 22{,}4\,n\ (\text{đktc})$$

Trong đó: `n_e` là số mol electron trao đổi (phần dùng để sinh khí đó) (mol); `n_{Cl_2}` là số mol khí clo ở anot (mol); `n_{O_2}` là số mol khí oxi ở anot (mol); `n_{H_2}` là số mol khí hiđro ở catot (mol); `V` là thể tích khí ở điều kiện tiêu chuẩn (L); `n` là số mol khí (mol).

*Điều kiện:* Ở điều kiện chuẩn theo chương trình GDPT 2018 (đkc: 25 °C, 1 bar) thì 1 mol khí chiếm 24,79 L; ở điều kiện tiêu chuẩn cũ (đktc: 0 °C, 1 atm) là 22,4 L

*Ghi chú:* Mỗi công thức chỉ dùng phần electron thực sự sinh ra khí đó. Khí ở catot chỉ xuất hiện khi cation kim loại đã bị khử hết (hoặc dung dịch có axit).

<sub>`chemistry.thpt.dien-phan.the-tich-khi` · lớp 12 · #vo-co #dien-phan #the-tich-khi</sub>

---

**Sự thay đổi pH của dung dịch khi điện phân** — *pH change of the solution during electrolysis*

$$\begin{cases} \text{điện phân } NaCl \text{ (màng ngăn)}: & pH \uparrow \ (\text{tạo } NaOH) \\ \text{điện phân } CuSO_4: & pH \downarrow \ (\text{tạo } H_2SO_4) \\ \text{điện phân } Na_2SO_4: & pH \text{ hầu như không đổi} \end{cases}$$

Trong đó: `pH` là chỉ số pH của dung dịch sau điện phân.

*Điều kiện:* Điện phân dung dịch với điện cực trơ

*Ghi chú:* Muối của kim loại mạnh với gốc axit mạnh có oxi (Na2SO4, KNO3) thực chất là điện phân nước, nồng độ muối tăng dần.

<sub>`chemistry.thpt.dien-phan.thay-doi-ph` · lớp 12 · #vo-co #dien-phan #ph</sub>

---

**Thứ tự oxi hóa ở anot khi điện phân dung dịch** — *Order of oxidation at the anode in solution electrolysis*

$$S^{2-} > I^- > Br^- > Cl^- > H_2O > SO_4^{2-},\ NO_3^-,\ F^-$$

Trong đó: `Cl^-` là ion clorua, bị oxi hóa tạo Cl2; `H_2O` là nước, bị oxi hóa tạo O2 và H+; `SO_4^{2-}` là ion sunfat, không bị điện phân trong dung dịch.

*Điều kiện:* Anot trơ (than chì, platin). Nếu anot tan (kim loại) thì chính anot bị oxi hóa trước

*Ghi chú:* Khi nước bị oxi hóa: 2H2O → O2 + 4H+ + 4e, làm dung dịch quanh anot có tính axit.

<sub>`chemistry.thpt.dien-phan.thu-tu-anot` · lớp 12 · #vo-co #dien-phan #anot</sub>

---

**Thứ tự khử ở catot khi điện phân dung dịch** — *Order of reduction at the cathode in solution electrolysis*

$$Ag^+ > Fe^{3+} > Cu^{2+} > H^+_{(axit)} > Pb^{2+} > Sn^{2+} > Ni^{2+} > Fe^{2+} > Zn^{2+} > H_2O$$

Trong đó: `Ag^+` là ion bạc, bị khử trước nhất; `Fe^{3+}` là ion sắt(III), bị khử về Fe2+ trước khi Cu2+ bị khử; `Cu^{2+}` là ion đồng(II); `H^+_{(axit)}` là ion H+ của axit; `Pb^{2+}` là ion chì(II); `Sn^{2+}` là ion thiếc(II); `Ni^{2+}` là ion niken(II); `Fe^{2+}` là ion sắt(II); `Zn^{2+}` là ion kẽm, cation cuối cùng còn bị khử trước nước; `H_2O` là nước, bị khử tạo H2 và OH-.

*Điều kiện:* Điện phân dung dịch với điện cực trơ; các cation K+, Na+, Ca2+, Mg2+, Al3+ (kim loại từ Al trở về trước) KHÔNG bị khử trong dung dịch, khi đó nước bị khử thay

*Ghi chú:* Fe3+ bị khử hai nấc: Fe3+ + 1e → Fe2+ (rất sớm), sau đó Fe2+ + 2e → Fe (rất muộn). Khi nước bị khử: 2H2O + 2e → H2 + 2OH-, làm dung dịch quanh catot có tính bazơ.

<sub>`chemistry.thpt.dien-phan.thu-tu-catot` · lớp 12 · #vo-co #dien-phan #catot</sub>

---

### Đếm đồng phân hợp chất hữu cơ

**Số đồng phân amin no, đơn chức, mạch hở** — *Number of isomers of saturated monofunctional amines*

$$S_{tong} = 2^{\,n-1},\quad S_{bac\ I} = 2^{\,n-2}\quad (n < 5)$$

Trong đó: `S_{tong}` là tổng số đồng phân amin (cả bậc I, II, III); `S_{bac\ I}` là số đồng phân amin bậc một; `n` là số nguyên tử cacbon của amin CnH2n+3N.

*Điều kiện:* Công thức tổng số đồng phân amin đúng với 1 ≤ n ≤ 4; công thức amin bậc I chỉ đúng với 2 ≤ n ≤ 4 (n = 1 chỉ có duy nhất một amin bậc I là CH3NH2); từ n ≥ 5 phải đếm trực tiếp

*Ghi chú:* n = 2 cho 2 amin (1 bậc I, 1 bậc II); n = 3 cho 4 amin (2 bậc I); n = 4 cho 8 amin (4 bậc I).

<sub>`chemistry.thpt.dong-phan.amin-bac-mot` · lớp 12 · #huu-co #dem-dong-phan #amin</sub>

---

**Số trieste tối đa tạo từ glixerol và n axit béo** — *Maximum number of triglycerides from glycerol and n fatty acids*

$$S = \dfrac{n^2(n+1)}{2}$$

Trong đó: `S` là số trieste (triglixerit) tối đa; `n` là số axit béo khác nhau tham gia.

*Điều kiện:* Xét cả đồng phân vị trí trên ba nhóm -OH của glixerol

*Ghi chú:* n = 2 cho 6 trieste, n = 3 cho 18 trieste. Đây là công thức đếm quen thuộc trong đề thi.

<sub>`chemistry.thpt.dong-phan.trieste-glixerol` · lớp 12 · #huu-co #dem-dong-phan #chat-beo</sub>

---

**Số đồng phân este no, đơn chức, mạch hở** — *Number of isomers of saturated monofunctional esters*

$$S = 2^{\,n-2}\quad (1 < n < 5)$$

Trong đó: `S` là số đồng phân este; `n` là số nguyên tử cacbon của este CnH2nO2.

*Điều kiện:* Công thức đúng với n = 2, 3, 4; từ n = 5 trở đi phải đếm trực tiếp (C5H10O2 có 9 este)

*Ghi chú:* n = 2 cho 1 este (HCOOCH3), n = 3 cho 2, n = 4 cho 4 este. Tổng số đồng phân đơn chức mạch hở của CnH2nO2 = số axit + số este.

<sub>`chemistry.thpt.dong-phan.este-no-don-chuc` · lớp 12 · #huu-co #dem-dong-phan #este</sub>

---

## Đại học (377 công thức)

### Cân bằng hóa học

**Ảnh hưởng của khí trơ và áp suất tới cân bằng khí** — *Effect of inert gas and pressure on gas-phase equilibrium*

$$K_{x} = K_{p}P^{-\Delta n};\qquad K_{n} = K_{p}\left(\frac{\sum n_{i}}{P}\right)^{\Delta n}$$

Trong đó: `K_x` là hằng số cân bằng theo phần mol (); `K_p` là hằng số cân bằng theo áp suất (chỉ phụ thuộc T) (); `K_n` là hằng số cân bằng theo số mol (); `P` là áp suất tổng (bar); `Σn_i` là tổng số mol khí (kể cả khí trơ) (mol); `Δn` là biến thiên số mol khí ().

*Điều kiện:* Khí lí tưởng, nhiệt độ không đổi

*Ghi chú:* Thêm khí trơ ở V, T không đổi: không chuyển dịch cân bằng (các áp suất riêng phần không đổi). Thêm khí trơ ở P, T không đổi: cân bằng chuyển dịch theo chiều làm tăng số mol khí (chiều thuận khi Δn > 0, chiều nghịch khi Δn < 0, không đổi khi Δn = 0). Tăng P: chuyển theo chiều giảm số mol khí.

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.anh-huong-khi-tro` · lớp 13 · #can-bang #le-chatelier #khi-tro</sub>

---

**Hằng số cân bằng theo nồng độ Kc** — *Equilibrium constant in terms of concentration*

$$K_{C} = \frac{[C]^{c}[D]^{d}}{[A]^{a}[B]^{b}}$$

Trong đó: `K_C` là hằng số cân bằng theo nồng độ ((mol/L)^delta_n); `[A]` là nồng độ mol các chất lúc cân bằng (mol/L); `[B]` là nồng độ mol các chất lúc cân bằng (mol/L); `[C]` là nồng độ mol các chất lúc cân bằng (mol/L); `[D]` là nồng độ mol các chất lúc cân bằng (mol/L); `a` là hệ số tỉ lượng; `b` là hệ số tỉ lượng; `c` là hệ số tỉ lượng; `d` là hệ số tỉ lượng.

*Điều kiện:* Hệ đã đạt cân bằng, nhiệt độ không đổi; dung dịch loãng hoặc khí lí tưởng

*Ghi chú:* Kc chỉ phụ thuộc nhiệt độ. Thứ nguyên của Kc là (mol/L)^Δn với Δn = (c+d) - (a+b).

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.hang-so-can-bang-kc` · lớp 13 · #can-bang #hang-so-can-bang</sub>

---

**Hằng số cân bằng theo áp suất riêng phần Kp** — *Equilibrium constant in terms of partial pressures*

$$K_{p} = \frac{p_{C}^{c}\,p_{D}^{d}}{p_{A}^{a}\,p_{B}^{b}};\qquad p_{i} = x_{i}P$$

Trong đó: `K_p` là hằng số cân bằng theo áp suất riêng phần (bar^delta_n); `p_i` là áp suất riêng phần của cấu tử i lúc cân bằng (bar); `x_i` là phần mol của cấu tử i (); `P` là áp suất tổng của hệ (bar).

*Điều kiện:* Cân bằng trong pha khí, các khí coi là lí tưởng, nhiệt độ không đổi

*Ghi chú:* Định luật Dalton: P = Σp_i. Kp chỉ phụ thuộc nhiệt độ, không phụ thuộc áp suất tổng.

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.hang-so-can-bang-kp` · lớp 13 · #can-bang #hang-so-can-bang #pha-khi</sub>

---

**Quan hệ giữa Kp và Kc** — *Relation between Kp and Kc*

$$K_{p} = K_{C}(RT)^{\Delta n};\qquad \Delta n = \sum \nu_{\text{khí, sp}} - \sum \nu_{\text{khí, cđ}}$$

Trong đó: `K_p` là hằng số cân bằng theo áp suất (); `K_C` là hằng số cân bằng theo nồng độ (); `R` là hằng số khí (L.bar/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `Δn` là biến thiên số mol khí theo phương trình phản ứng ().

*Điều kiện:* Khí lí tưởng; đơn vị của R phải phù hợp với đơn vị áp suất và nồng độ (R = 0.08314 L.bar/(mol.K) hoặc 0.08206 L.atm/(mol.K))

*Ghi chú:* Nếu Δn = 0 thì Kp = Kc.

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.quan-he-kp-kc` · lớp 13 · #can-bang #hang-so-can-bang #pha-khi</sub>

---

**Quan hệ giữa Kp, Kx và Kn** — *Relation between Kp, Kx and Kn*

$$K_{p} = K_{x}\,P^{\Delta n} = K_{n}\left(\frac{P}{\sum n_{i}}\right)^{\Delta n}$$

Trong đó: `K_p` là hằng số cân bằng theo áp suất riêng phần (); `K_x` là hằng số cân bằng theo phần mol (); `K_n` là hằng số cân bằng theo số mol (); `P` là áp suất tổng (bar); `Σn_i` là tổng số mol khí lúc cân bằng (mol); `Δn` là biến thiên số mol khí ().

*Điều kiện:* Hỗn hợp khí lí tưởng ở cân bằng

*Ghi chú:* Kp chỉ phụ thuộc T; Kx và Kn còn phụ thuộc áp suất tổng khi Δn khác 0. Đó là cơ sở giải thích ảnh hưởng của áp suất tới cân bằng.

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.quan-he-kp-kx` · lớp 13 · #can-bang #hang-so-can-bang #phan-mol</sub>

---

**Thương số phản ứng** — *Reaction quotient*

$$aA + bB \rightleftharpoons cC + dD:\qquad Q = \frac{a_{C}^{c}\,a_{D}^{d}}{a_{A}^{a}\,a_{B}^{b}}$$

Trong đó: `Q` là thương số phản ứng tại thời điểm bất kì (); `a_i` là hoạt độ của cấu tử i (quy về trạng thái chuẩn) (); `a` là hệ số tỉ lượng; `b` là hệ số tỉ lượng; `c` là hệ số tỉ lượng; `d` là hệ số tỉ lượng.

*Điều kiện:* Chất rắn nguyên chất và chất lỏng nguyên chất có hoạt độ bằng 1 nên không xuất hiện trong biểu thức

*Ghi chú:* Q có dạng giống K nhưng tính với nồng độ (áp suất) tức thời. So sánh Q với K để biết chiều diễn biến.

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.thuong-so-phan-ung` · lớp 13 · #can-bang #thuong-so-phan-ung</sub>

---

**Quy tắc tổ hợp hằng số cân bằng** — *Combining equilibrium constants*

$$K_{\text{nghịch}} = \frac{1}{K};\qquad K_{(n\times pt)} = K^{n};\qquad K_{\text{tổng}} = K_{1}\cdot K_{2}\cdots K_{m}$$

Trong đó: `K` là hằng số cân bằng của phản ứng gốc (); `K_nghịch` là hằng số cân bằng của phản ứng nghịch (); `n` là hệ số nhân phương trình (); `K_tổng` là hằng số cân bằng của phản ứng tổng cộng (); `K_1...K_m` là hằng số cân bằng của các phản ứng thành phần ().

*Điều kiện:* Các phản ứng thành phần cộng lại đúng bằng phản ứng tổng, cùng nhiệt độ

*Ghi chú:* Tương ứng với tính cộng của Δ_rG0 (định luật Hess) vì Δ_rG0 = -RT lnK.

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.to-hop-hang-so-can-bang` · lớp 13 · #can-bang #hang-so-can-bang #to-hop</sub>

---

**Độ chuyển hóa và độ phân li** — *Degree of conversion (degree of dissociation)*

$$\alpha = \frac{n_{0} - n}{n_{0}} = \frac{n_{\text{đã phản ứng}}}{n_{0}};\qquad 0 \le \alpha \le 1$$

Trong đó: `α` là độ chuyển hóa (độ phân li) (); `n_0` là số mol chất ban đầu (mol); `n` là số mol chất còn lại lúc cân bằng (mol).

*Điều kiện:* Tính cho một chất tham gia xác định

*Ghi chú:* Với phản ứng phân li A ⇌ 2B, hệ số nở khí: Σn = n_0(1 + α); từ tỉ khối hơi có thể suy ra α theo M_lt/M_tt = 1 + α.

<sub>`chemistry.dai-hoc.can-bang-hoa-hoc.do-chuyen-hoa` · lớp 13 · #can-bang #do-chuyen-hoa #phan-li</sub>

---

### Cân bằng pha

**Phương trình Clausius - Clapeyron dạng tích phân** — *Clausius - Clapeyron equation (integrated form)*

$$\ln\frac{p_{2}}{p_{1}} = -\frac{\Delta H_{hh}}{R}\left(\frac{1}{T_{2}} - \frac{1}{T_{1}}\right);\qquad \ln p = -\frac{\Delta H_{hh}}{RT} + C$$

Trong đó: `p1` là áp suất hơi bão hòa ở T1 (Pa); `p2` là áp suất hơi bão hòa ở T2 (Pa); `ΔH_hh` là nhiệt hóa hơi mol (J/mol); `R` là hằng số khí (J/(mol.K)); `T1` là nhiệt độ thứ nhất (K); `T2` là nhiệt độ thứ hai (K); `C` là hằng số tích phân ().

*Điều kiện:* ΔH_hh coi như không đổi trong khoảng nhiệt độ khảo sát

*Ghi chú:* Đồ thị lnp theo 1/T là đường thẳng có hệ số góc -ΔH_hh/R - dùng để xác định nhiệt hóa hơi bằng thực nghiệm.

<sub>`chemistry.dai-hoc.can-bang-pha.clausius-clapeyron-tich-phan` · lớp 13 · #can-bang-pha #clausius-clapeyron #ap-suat-hoi</sub>

---

**Phương trình Clausius - Clapeyron dạng vi phân** — *Clausius - Clapeyron equation (differential form)*

$$\frac{d\ln p}{dT} = \frac{\Delta H_{hh}}{RT^{2}}$$

Trong đó: `p` là áp suất hơi bão hòa (Pa); `T` là nhiệt độ tuyệt đối (K); `ΔH_hh` là nhiệt hóa hơi mol (hoặc nhiệt thăng hoa) (J/mol); `R` là hằng số khí (J/(mol.K)).

*Điều kiện:* Cân bằng lỏng - hơi (hoặc rắn - hơi); hơi coi là khí lí tưởng; thể tích pha ngưng tụ bỏ qua so với pha hơi

*Ghi chú:* Suy từ phương trình Clapeyron với ΔV ≈ V_hơi = RT/p.

<sub>`chemistry.dai-hoc.can-bang-pha.clausius-clapeyron-vi-phan` · lớp 13 · #can-bang-pha #clausius-clapeyron #ap-suat-hoi</sub>

---

**Phương trình Clapeyron** — *Clapeyron equation*

$$\frac{dp}{dT} = \frac{\Delta H_{cp}}{T\,\Delta V_{cp}}$$

Trong đó: `p` là áp suất cân bằng giữa hai pha (Pa); `T` là nhiệt độ chuyển pha (K); `ΔH_cp` là nhiệt chuyển pha mol (J/mol); `ΔV_cp` là biến thiên thể tích mol khi chuyển pha (m^3/mol).

*Điều kiện:* Cân bằng giữa hai pha của một chất nguyên chất

*Ghi chú:* Với nước, ΔV khi nóng chảy âm nên dp/dT < 0: tăng áp suất làm hạ nhiệt độ nóng chảy của nước đá.

<sub>`chemistry.dai-hoc.can-bang-pha.phuong-trinh-clapeyron` · lớp 13 · #can-bang-pha #clapeyron #chuyen-pha</sub>

---

**Quy tắc Trouton** — *Trouton's rule*

$$\Delta S_{hh} = \frac{\Delta H_{hh}}{T_{s}} \approx 88\ \text{J.mol}^{-1}\text{.K}^{-1}$$

Trong đó: `ΔS_hh` là entropy hóa hơi mol (J/(mol.K)); `ΔH_hh` là nhiệt hóa hơi mol tại nhiệt độ sôi thường (J/mol); `T_s` là nhiệt độ sôi ở 1 atm (K).

*Điều kiện:* Chất lỏng không liên kết hydrogen, không kết hợp phân tử

*Ghi chú:* Nước (109), ethanol (110) lệch nhiều do liên kết hydrogen. Dùng để ước lượng nhanh ΔH_hh khi biết nhiệt độ sôi.

<sub>`chemistry.dai-hoc.can-bang-pha.quy-tac-trouton` · lớp 13 · #can-bang-pha #trouton #entropy</sub>

---

**Điểm ba và bậc tự do trên giản đồ pha một cấu tử** — *Triple point and degrees of freedom in a one-component phase diagram*

$$c = 1:\; f = 3 - \phi \Rightarrow \begin{cases} \phi = 1 \Rightarrow f = 2 & \text{(miền pha)} \\ \phi = 2 \Rightarrow f = 1 & \text{(đường cân bằng)} \\ \phi = 3 \Rightarrow f = 0 & \text{(điểm ba)} \end{cases}$$

Trong đó: `c` là số cấu tử (); `f` là số bậc tự do (); `φ` là số pha ().

*Điều kiện:* Hệ một cấu tử ở cân bằng, chỉ xét biến p và T

*Ghi chú:* Điểm ba của nước: T = 273.16 K, p = 611.657 Pa. Điểm tới hạn của nước: 647.1 K và 22.06 MPa.

<sub>`chemistry.dai-hoc.can-bang-pha.gian-do-pha-diem-ba` · lớp 13 · #can-bang-pha #gian-do-pha #diem-ba</sub>

---

**Quy tắc đòn bẩy trên giản đồ pha hai cấu tử** — *Lever rule*

$$n_{\alpha}\,l_{\alpha} = n_{\beta}\,l_{\beta} \quad \Leftrightarrow \quad \frac{n_{\alpha}}{n_{\beta}} = \frac{l_{\beta}}{l_{\alpha}}$$

Trong đó: `n_α` là số mol (hoặc khối lượng) pha α (mol); `n_β` là số mol (hoặc khối lượng) pha β (mol); `l_α` là khoảng cách từ điểm hệ tới điểm biểu diễn pha α (); `l_β` là khoảng cách từ điểm hệ tới điểm biểu diễn pha β ().

*Điều kiện:* Điểm biểu diễn hệ nằm trong vùng hai pha của giản đồ

*Ghi chú:* Pha nào ở gần điểm hệ hơn thì có lượng nhiều hơn - giống nguyên tắc đòn bẩy trong cơ học.

<sub>`chemistry.dai-hoc.can-bang-pha.quy-tac-don-bay` · lớp 13 · #can-bang-pha #gian-do-pha #don-bay</sub>

---

**Quy tắc pha Gibbs** — *Gibbs phase rule*

$$f = c - \phi + 2$$

Trong đó: `f` là số bậc tự do của hệ (); `c` là số cấu tử độc lập (); `φ` là số pha có mặt trong hệ ().

*Điều kiện:* Hệ ở cân bằng nhiệt động; chỉ có nhiệt độ và áp suất là các thông số bên ngoài ảnh hưởng

*Ghi chú:* Nếu cố định thêm một thông số (ví dụ p không đổi) thì f = c - φ + 1. Số cấu tử độc lập c = số chất - số phương trình liên hệ (phản ứng, điều kiện tỉ lượng).

<sub>`chemistry.dai-hoc.can-bang-pha.quy-tac-pha-gibbs` · lớp 13 · #can-bang-pha #quy-tac-pha #gian-do-pha</sub>

---

### Cấu tạo chất

**Hệ thức de Broglie và nguyên lí bất định Heisenberg** — *De Broglie relation and Heisenberg uncertainty principle*

$$\lambda = \frac{h}{p} = \frac{h}{mv};\qquad \Delta x\,\Delta p_{x} \geq \frac{\hbar}{2}$$

Trong đó: `λ` là bước sóng de Broglie (m); `h` là hằng số Planck (J.s); `p` là động lượng (kg.m/s); `m` là khối lượng hạt (kg); `v` là tốc độ hạt (m/s); `Δx` là độ bất định về vị trí (m); `Δp_x` là độ bất định về động lượng (kg.m/s); `ħ` là hằng số Planck rút gọn (J.s).

*Điều kiện:* Áp dụng cho mọi hạt vi mô; hiệu ứng chỉ đáng kể với hạt có khối lượng rất nhỏ

*Ghi chú:* h = 6.626e-34 J.s, ħ = h/(2π) = 1.055e-34 J.s. Vì bất định nên không thể nói tới quỹ đạo của electron, chỉ nói tới obitan (vùng xác suất).

<sub>`chemistry.dai-hoc.cau-tao-chat.he-thuc-de-broglie` · lớp 13 · #cau-tao-chat #luong-tu #de-broglie</sub>

---

**Phương trình Schrödinger ở trạng thái dừng** — *Time-independent Schrödinger equation*

$$\hat{H}\psi = E\psi;\qquad -\frac{\hbar^{2}}{2m}\nabla^{2}\psi + V\psi = E\psi$$

Trong đó: `H` là toán tử Hamilton (toán tử năng lượng toàn phần); `ψ` là hàm sóng của hệ (m^-1.5); `E` là năng lượng của trạng thái (J); `ħ` là hằng số Planck rút gọn (h/2π) (J.s); `m` là khối lượng hạt (kg); `∇^2` là toán tử Laplace; `V` là thế năng (J).

*Điều kiện:* Hệ không phụ thuộc thời gian; hàm sóng phải đơn trị, liên tục, hữu hạn và chuẩn hóa

*Ghi chú:* ħ = 1.055e-34 J.s. Bình phương môđun hàm sóng |ψ|^2 là mật độ xác suất tìm thấy electron (obitan nguyên tử).

<sub>`chemistry.dai-hoc.cau-tao-chat.phuong-trinh-schrodinger` · lớp 13 · #cau-tao-chat #luong-tu #schrodinger</sub>

---

**Momen lưỡng cực và phần trăm ion của liên kết** — *Dipole moment and percent ionic character*

$$\mu = q\,d;\qquad \%\text{ion} = \frac{\mu_{tn}}{\mu_{ion}}\times 100 = \frac{\mu_{tn}}{e\,d}\times 100$$

Trong đó: `μ` là momen lưỡng cực (C.m); `q` là điện tích hiệu dụng ở mỗi cực (C); `d` là độ dài liên kết (m); `μ_tn` là momen lưỡng cực đo được bằng thực nghiệm (D); `μ_ion` là momen lưỡng cực nếu liên kết là ion 100% (D); `e` là điện tích nguyên tố (C).

*Điều kiện:* Liên kết hai tâm; với phân tử nhiều liên kết, momen tổng là tổng vectơ

*Ghi chú:* 1 D (Debye) = 3.336e-30 C.m. HCl có μ = 1.08 D, d = 127 pm nên khoảng 17% ion. Phân tử đối xứng (CO2, CCl4, BF3) có μ = 0 dù các liên kết phân cực.

<sub>`chemistry.dai-hoc.cau-tao-chat.momen-luong-cuc` · lớp 13 · #cau-tao-chat #luong-cuc #phan-cuc</sub>

---

**Bán kính quỹ đạo Bohr** — *Bohr radius*

$$r_{n} = \frac{n^{2}}{Z}a_{0};\qquad a_{0} = \frac{\varepsilon_{0}h^{2}}{\pi m_{e}e^{2}} = 52.9\ \mathrm{pm}$$

Trong đó: `r_n` là bán kính quỹ đạo thứ n (pm); `n` là số lượng tử chính (); `Z` là số hiệu nguyên tử (); `a_0` là bán kính Bohr thứ nhất (pm); `ε_0` là hằng số điện môi chân không; `h` là hằng số Planck; `m_e` là khối lượng electron; `e` là điện tích nguyên tố.

*Điều kiện:* Mô hình Bohr cho hệ một electron

*Ghi chú:* a_0 = 0.529 angstrom = 5.29e-11 m. Trong cơ học lượng tử, a_0 là khoảng cách xác suất tìm thấy electron 1s lớn nhất.

<sub>`chemistry.dai-hoc.cau-tao-chat.ban-kinh-bohr` · lớp 13 · #cau-tao-chat #bohr #ban-kinh</sub>

---

**Công thức Rydberg và năng lượng photon** — *Rydberg formula and photon energy*

$$\frac{1}{\lambda} = R_{H}Z^{2}\left(\frac{1}{n_{1}^{2}}-\frac{1}{n_{2}^{2}}\right);\qquad \Delta E = h\nu = \frac{hc}{\lambda}$$

Trong đó: `λ` là bước sóng bức xạ (m); `R_H` là hằng số Rydberg (m^-1); `Z` là số hiệu nguyên tử; `n_1` là số lượng tử của mức thấp (); `n_2` là số lượng tử của mức cao (n_2 > n_1) (); `ΔE` là hiệu năng lượng hai mức (J); `h` là hằng số Planck (J.s); `ν` là tần số bức xạ (Hz); `c` là tốc độ ánh sáng trong chân không (m/s).

*Điều kiện:* Hệ một electron; chuyển mức electron kèm phát xạ hoặc hấp thụ photon

*Ghi chú:* R_H = 1.097e7 m^-1; h = 6.626e-34 J.s; c = 2.998e8 m/s. Dãy Lyman (n1=1, tử ngoại), Balmer (n1=2, khả kiến), Paschen (n1=3, hồng ngoại).

<sub>`chemistry.dai-hoc.cau-tao-chat.cong-thuc-rydberg` · lớp 13 · #cau-tao-chat #quang-pho #rydberg</sub>

---

**Mức năng lượng của nguyên tử hiđrô và ion giống hiđrô** — *Energy levels of hydrogen-like atoms*

$$E_{n} = -\frac{m_{e}e^{4}Z^{2}}{8\varepsilon_{0}^{2}h^{2}n^{2}} = -13.6\,\frac{Z^{2}}{n^{2}}\ \mathrm{eV} = -2.18\times10^{-18}\frac{Z^{2}}{n^{2}}\ \mathrm{J}$$

Trong đó: `E_n` là năng lượng của mức thứ n (J); `n` là số lượng tử chính (1, 2, 3...) (); `Z` là số hiệu nguyên tử (điện tích hạt nhân) (); `m_e` là khối lượng electron (kg); `e` là điện tích nguyên tố (C); `ε_0` là hằng số điện môi chân không (F/m); `h` là hằng số Planck (J.s).

*Điều kiện:* Hệ một electron: H, He+, Li2+, Be3+...

*Ghi chú:* Năng lượng ion hóa của H bằng 13.6 eV = 1312 kJ/mol. h = 6.626e-34 J.s, m_e = 9.109e-31 kg, e = 1.602e-19 C.

<sub>`chemistry.dai-hoc.cau-tao-chat.muc-nang-luong-bohr` · lớp 13 · #cau-tao-chat #bohr #nang-luong</sub>

---

**Quy tắc Slater tính điện tích hạt nhân hiệu dụng** — *Slater's rules for the effective nuclear charge*

$$Z^{*} = Z - S;\qquad E_{n} = -13.6\frac{(Z^{*})^{2}}{(n^{*})^{2}}\ \mathrm{eV}$$

Trong đó: `Z*` là điện tích hạt nhân hiệu dụng (); `Z` là số hiệu nguyên tử (); `S` là hằng số chắn (tổng đóng góp của các electron khác) (); `E_n` là năng lượng obitan (eV); `n*` là số lượng tử chính hiệu dụng ().

*Điều kiện:* Áp dụng cho electron đang xét trong nguyên tử nhiều electron

*Ghi chú:* Hằng số chắn: electron cùng nhóm (ns, np) góp 0.35 (riêng 1s góp 0.30); lớp n-1 góp 0.85; lớp n-2 trở vào góp 1.00. Với electron d hoặc f: cùng nhóm 0.35, mọi electron bên trong 1.00. n* = 1, 2, 3, 3.7, 4.0, 4.2 ứng với n = 1, 2, 3, 4, 5, 6.

<sub>`chemistry.dai-hoc.cau-tao-chat.quy-tac-slater` · lớp 13 · #cau-tao-chat #slater #dien-tich-hieu-dung</sub>

---

**Bốn số lượng tử và điều kiện của chúng** — *The four quantum numbers*

$$\begin{cases} n = 1,2,3,\ldots \\ \ell = 0,1,\ldots,n-1 \\ m_{\ell} = -\ell,\ldots,0,\ldots,+\ell \quad (2\ell+1\ \text{giá trị}) \\ m_{s} = \pm\tfrac{1}{2} \end{cases};\quad \text{số obitan} = n^{2},\ \text{số electron tối đa} = 2n^{2}$$

Trong đó: `n` là số lượng tử chính (lớp) (); `ℓ` là số lượng tử obitan (phân lớp: s, p, d, f) (); `m_ℓ` là số lượng tử từ (định hướng obitan) (); `m_s` là số lượng tử spin ().

*Điều kiện:* Nguyên lí Pauli: không có hai electron nào trong cùng nguyên tử có đủ bốn số lượng tử giống nhau

*Ghi chú:* ℓ = 0, 1, 2, 3 tương ứng phân lớp s, p, d, f với 1, 3, 5, 7 obitan. Quy tắc Hund: các electron điền vào các obitan cùng mức năng lượng sao cho tổng spin lớn nhất.

<sub>`chemistry.dai-hoc.cau-tao-chat.cac-so-luong-tu` · lớp 13 · #cau-tao-chat #so-luong-tu #obitan</sub>

---

**Momen động lượng obitan và hình chiếu của nó** — *Orbital angular momentum and its projection*

$$|\vec{L}| = \sqrt{\ell(\ell+1)}\,\hbar;\qquad L_{z} = m_{\ell}\hbar;\qquad |\vec{S}| = \sqrt{s(s+1)}\,\hbar$$

Trong đó: `|L|` là độ lớn momen động lượng obitan (J.s); `ℓ` là số lượng tử obitan; `ħ` là hằng số Planck rút gọn (J.s); `L_z` là hình chiếu momen động lượng lên trục z (J.s); `m_ℓ` là số lượng tử từ; `|S|` là độ lớn momen spin; `s` là số lượng tử spin (bằng 1/2 với một electron).

*Điều kiện:* Hệ lượng tử; các giá trị bị lượng tử hóa

*Ghi chú:* Momen động lượng bị lượng tử hóa cả về độ lớn lẫn hướng. Với nhiều electron dùng tổng L, S và số hạng phổ (2S+1)L_J.

<sub>`chemistry.dai-hoc.cau-tao-chat.momen-dong-luong-obitan` · lớp 13 · #cau-tao-chat #luong-tu #momen-dong-luong</sub>

---

**Quy tắc 18 electron** — *The 18-electron rule*

$$\mathrm{VE} = n_{d}(\text{kim loại}) + \sum n_{e}(\text{phối tử}) - q = 18$$

Trong đó: `VE` là tổng số electron hóa trị của phức (); `n_d` là số electron hóa trị của nguyên tử kim loại trung tâm ở trạng thái tự do (); `n_e` là số electron mà mỗi phối tử cho (); `q` là điện tích của phức ().

*Điều kiện:* Phức cơ kim của kim loại chuyển tiếp d, đặc biệt với phối tử trường mạnh (CO, PR3, olefin)

*Ghi chú:* Phối tử cho 2 electron: CO, PR3, NH3, alkene. Cho 1 electron: H, halogen, CH3. Cho 5: Cp (η5-C5H5). Cho 6: benzene (η6). Ví dụ Ni(CO)4: 10 + 4x2 = 18; Fe(CO)5: 8 + 10 = 18.

<sub>`chemistry.dai-hoc.cau-tao-chat.quy-tac-18-electron` · lớp 13 · #cau-tao-chat #co-kim #18-electron</sub>

---

**Số obitan lai hóa và dạng hình học phân tử (thuyết VB - VSEPR)** — *Hybridisation number and molecular geometry*

$$H = \sigma + n_{lp} = \frac{1}{2}\left(N_{\text{hóa trị}} + N_{\text{phối tử}} - q\right)$$

Trong đó: `H` là số obitan lai hóa (số miền electron) (); `σ` là số liên kết sigma của nguyên tử trung tâm (); `n_lp` là số cặp electron không liên kết trên nguyên tử trung tâm (); `N_hóa trị` là số electron hóa trị của nguyên tử trung tâm; `N_phối tử` là số phối tử liên kết bằng một electron (H, halogen); `q` là điện tích của ion ().

*Điều kiện:* Nguyên tử trung tâm thuộc chu kì 2 hoặc 3; công thức đếm không áp dụng cho phức chất kim loại chuyển tiếp

*Ghi chú:* H = 2: sp, thẳng 180 độ; H = 3: sp2, tam giác phẳng 120 độ; H = 4: sp3, tứ diện 109.5 độ; H = 5: sp3d, lưỡng chóp tam giác; H = 6: sp3d2, bát diện 90 độ. Cặp electron tự do đẩy mạnh hơn nên làm giảm góc liên kết.

<sub>`chemistry.dai-hoc.cau-tao-chat.lai-hoa-obitan` · lớp 13 · #cau-tao-chat #lai-hoa #hinh-hoc-phan-tu</sub>

---

**Bậc liên kết theo thuyết obitan phân tử** — *Bond order from molecular orbital theory*

$$N = \frac{n_{lk} - n_{plk}}{2}$$

Trong đó: `N` là bậc liên kết (); `n_lk` là số electron trên các obitan liên kết (); `n_plk` là số electron trên các obitan phản liên kết ().

*Điều kiện:* Giản đồ MO của phân tử hai nguyên tử; electron điền theo nguyên lí vững bền, Pauli và quy tắc Hund

*Ghi chú:* N = 0 thì phân tử không tồn tại (He2). Bậc liên kết càng lớn thì liên kết càng ngắn và càng bền. O2 có N = 2 và hai electron độc thân nên thuận từ - điểm mạnh của thuyết MO so với thuyết VB.

<sub>`chemistry.dai-hoc.cau-tao-chat.bac-lien-ket-mo` · lớp 13 · #cau-tao-chat #mo #bac-lien-ket</sub>

---

**Năng lượng bền hóa trường tinh thể CFSE** — *Crystal field stabilisation energy*

$$\mathrm{CFSE} = \left(-0.4\,n_{t_{2g}} + 0.6\,n_{e_{g}}\right)\Delta_{o} + m\,P$$

Trong đó: `CFSE` là năng lượng bền hóa trường tinh thể (cm^-1); `n_t2g` là số electron trên bộ obitan t2g (); `n_eg` là số electron trên bộ obitan eg (); `Δ_o` là năng lượng tách trường bát diện (cm^-1); `m` là số cặp electron ghép đôi tăng thêm so với ion tự do (); `P` là năng lượng ghép đôi electron (cm^-1).

*Điều kiện:* Phức bát diện; CFSE quy ước âm nghĩa là bền hóa

*Ghi chú:* Δ_o > P: trường mạnh, phức spin thấp. Δ_o < P: trường yếu, phức spin cao. Cấu hình d3 và d8 (spin cao) hay d6 (spin thấp) có CFSE lớn nên phức rất bền.

<sub>`chemistry.dai-hoc.cau-tao-chat.cfse` · lớp 13 · #cau-tao-chat #cfse #phuc-chat</sub>

---

**Momen từ spin thuần túy** — *Spin-only magnetic moment*

$$\mu_{s} = \sqrt{n(n+2)}\ \mu_{B} = 2\sqrt{S(S+1)}\ \mu_{B};\qquad S = \frac{n}{2}$$

Trong đó: `μ_s` là momen từ spin thuần túy (BM); `n` là số electron độc thân (); `μ_B` là magneton Bohr (J/T); `S` là tổng số lượng tử spin ().

*Điều kiện:* Bỏ qua đóng góp của momen obitan (đúng tốt với ion 3d)

*Ghi chú:* 1 magneton Bohr (BM) = 9.274e-24 J/T. n = 1, 2, 3, 4, 5 cho μ = 1.73; 2.83; 3.87; 4.90; 5.92 BM. Đo μ thực nghiệm suy ra số electron độc thân, từ đó biết phức là spin cao hay spin thấp.

<sub>`chemistry.dai-hoc.cau-tao-chat.momen-tu-spin-thuan-tuy` · lớp 13 · #cau-tao-chat #tu-tinh #phuc-chat</sub>

---

**Năng lượng tách trường tinh thể** — *Crystal field splitting energy*

$$\Delta_{o} = 10Dq;\qquad E(t_{2g}) = -0.4\Delta_{o},\; E(e_{g}) = +0.6\Delta_{o};\qquad \Delta_{t} = \frac{4}{9}\Delta_{o}$$

Trong đó: `Δ_o` là năng lượng tách trường bát diện (cm^-1); `Δ_t` là năng lượng tách trường tứ diện (cm^-1); `Dq` là tham số trường tinh thể (cm^-1); `E(t2g)` là năng lượng của bộ obitan t2g so với trọng tâm (cm^-1); `E(eg)` là năng lượng của bộ obitan eg (cm^-1).

*Điều kiện:* Phức bát diện (hoặc tứ diện) của kim loại chuyển tiếp d; phối tử coi như điện tích điểm

*Ghi chú:* Dãy quang phổ hóa học (tăng dần Δ): I- < Br- < Cl- < F- < OH- < H2O < NH3 < en < CN- ≈ CO. Δ tăng khi điện tích ion trung tâm tăng và khi đi từ 3d xuống 4d, 5d. Δ_o cũng liên hệ với bước sóng hấp thụ: Δ_o = hc/λ.

<sub>`chemistry.dai-hoc.cau-tao-chat.nang-luong-tach-truong-tinh-the` · lớp 13 · #cau-tao-chat #truong-tinh-the #phuc-chat</sub>

---

### Dung dịch

**Định luật phân bố Nernst** — *Nernst distribution law*

$$K_{D} = \frac{C_{\text{hữu cơ}}}{C_{\text{nước}}};\qquad \text{sau } n \text{ lần chiết: } m_{n} = m_{0}\left(\frac{V_{n}}{V_{n} + K_{D}V_{hc}}\right)^{n}$$

Trong đó: `K_D` là hệ số phân bố (); `C_hữu cơ` là nồng độ chất tan trong pha hữu cơ (mol/L); `C_nước` là nồng độ chất tan trong pha nước (mol/L); `m_0` là khối lượng chất ban đầu trong pha nước (g); `m_n` là khối lượng chất còn lại sau n lần chiết (g); `V_n` là thể tích pha nước (L); `V_hc` là thể tích dung môi hữu cơ mỗi lần chiết (L); `n` là số lần chiết ().

*Điều kiện:* Chất tan tồn tại cùng một dạng phân tử trong cả hai pha, dung dịch loãng, hai dung môi không trộn lẫn, nhiệt độ không đổi

*Ghi chú:* Chiết nhiều lần với thể tích nhỏ hiệu quả hơn chiết một lần với toàn bộ thể tích dung môi.

<sub>`chemistry.dai-hoc.dung-dich.he-so-phan-bo-nernst` · lớp 13 · #dung-dich #chiet #phan-bo</sub>

---

**Hệ số Van't Hoff của chất điện li** — *Van't Hoff factor*

$$i = \frac{\text{số tiểu phân thực tế}}{\text{số phân tử hòa tan}} = 1 + \alpha(\nu - 1)$$

Trong đó: `i` là hệ số Van't Hoff (hệ số đẳng trương) (); `α` là độ điện li (); `ν` là số ion tạo thành khi một phân tử điện li hoàn toàn ().

*Điều kiện:* Dung dịch loãng; bỏ qua tương tác ion

*Ghi chú:* NaCl (ν = 2, α ≈ 1) có i ≈ 2; CaCl2 có i ≈ 3; chất không điện li i = 1. Suy ra độ điện li: α = (i - 1)/(ν - 1).

<sub>`chemistry.dai-hoc.dung-dich.he-so-vant-hoff` · lớp 13 · #dung-dich #dien-li #vant-hoff</sub>

---

**Các cách biểu diễn nồng độ dung dịch** — *Concentration units of solutions*

$$C_{M} = \frac{n_{ct}}{V_{dd}};\quad C_{m} = \frac{n_{ct}}{m_{dm}};\quad x_{i} = \frac{n_{i}}{\sum n_{j}};\quad C\% = \frac{m_{ct}}{m_{dd}}\times 100$$

Trong đó: `C_M` là nồng độ mol (molarity) (mol/L); `C_m` là nồng độ molan (molality) (mol/kg); `x_i` là phần mol của cấu tử i (); `C%` là nồng độ phần trăm khối lượng (%); `n_ct` là số mol chất tan (mol); `V_dd` là thể tích dung dịch (L); `m_dm` là khối lượng dung môi (kg); `m_ct` là khối lượng chất tan (g); `m_dd` là khối lượng dung dịch (g).

*Điều kiện:* Nồng độ mol phụ thuộc nhiệt độ (do V giãn nở), nồng độ molan và phần mol thì không

*Ghi chú:* Với dung dịch nước rất loãng: C_M ≈ C_m. Liên hệ: C_M = 10.d.C%/M với d là khối lượng riêng (g/mL) và M khối lượng mol (g/mol).

<sub>`chemistry.dai-hoc.dung-dich.cac-loai-nong-do` · lớp 13 · #dung-dich #nong-do</sub>

---

**Định luật giới hạn Debye - Hückel** — *Debye - Hückel limiting law*

$$\lg \gamma_{\pm} = -A\,|z_{+}z_{-}|\sqrt{I}$$

Trong đó: `γ±` là hệ số hoạt độ ion trung bình (); `A` là hằng số Debye - Hückel của dung môi ((mol/L)^-0.5); `z+` là điện tích cation (); `z-` là điện tích anion (); `I` là lực ion (mol/L).

*Điều kiện:* Dung dịch rất loãng, I nhỏ hơn khoảng 0.01 mol/L

*Ghi chú:* Trong nước ở 25 độ C: A = 0.509 (mol/L)^(-1/2). Với ion đơn: lg γ_i = -A z_i^2 √I.

<sub>`chemistry.dai-hoc.dung-dich.debye-huckel-gioi-han` · lớp 13 · #dung-dich #debye-huckel #hoat-do</sub>

---

**Phương trình Debye - Hückel mở rộng và Davies** — *Extended Debye - Hückel and Davies equations*

$$\lg\gamma_{\pm} = \frac{-A|z_{+}z_{-}|\sqrt{I}}{1 + B a_{0}\sqrt{I}};\qquad \text{Davies: } \lg\gamma_{\pm} = -A|z_{+}z_{-}|\left(\frac{\sqrt{I}}{1+\sqrt{I}} - 0.3I\right)$$

Trong đó: `γ±` là hệ số hoạt độ ion trung bình (); `A` là hằng số Debye - Hückel ((mol/L)^-0.5); `B` là hằng số phụ thuộc dung môi và nhiệt độ ((mol/L)^-0.5.pm^-1); `a_0` là bán kính ion hydrat hóa hiệu dụng (pm); `z+` là điện tích cation; `z-` là điện tích anion; `I` là lực ion (mol/L).

*Điều kiện:* Phương trình mở rộng dùng tới I ≈ 0.1 mol/L; phương trình Davies dùng tới I ≈ 0.5 mol/L

*Ghi chú:* Trong nước 25 độ C: A = 0.509, B ≈ 3.29e-3 (pm^-1.(mol/L)^-0.5); tích B.a_0 thường lấy ≈ 1 khi a_0 ≈ 300 pm.

<sub>`chemistry.dai-hoc.dung-dich.debye-huckel-mo-rong` · lớp 13 · #dung-dich #debye-huckel #hoat-do</sub>

---

**Lực ion của dung dịch** — *Ionic strength*

$$I = \frac{1}{2}\sum_{i} C_{i}z_{i}^{2}$$

Trong đó: `I` là lực ion của dung dịch (mol/L); `C_i` là nồng độ mol (hoặc molan) của ion i (mol/L); `z_i` là điện tích của ion i ().

*Điều kiện:* Tổng lấy trên tất cả các ion có mặt trong dung dịch

*Ghi chú:* Chất điện li 1-1 (NaCl): I = C. Chất 1-2 (Na2SO4, CaCl2): I = 3C. Chất 2-2 (MgSO4): I = 4C.

<sub>`chemistry.dai-hoc.dung-dich.luc-ion` · lớp 13 · #dung-dich #luc-ion #dien-li</sub>

---

**Hoạt độ và hệ số hoạt độ** — *Activity and activity coefficient*

$$a_{i} = \gamma_{i}\,\frac{C_{i}}{C^{0}};\qquad \mu_{i} = \mu_{i}^{0} + RT\ln a_{i};\qquad \gamma_{\pm} = \left(\gamma_{+}^{\nu_{+}}\gamma_{-}^{\nu_{-}}\right)^{1/(\nu_{+}+\nu_{-})}$$

Trong đó: `a_i` là hoạt độ của cấu tử i (); `γ_i` là hệ số hoạt độ (); `C_i` là nồng độ của i (mol/L); `C0` là nồng độ chuẩn (1 mol/L) (mol/L); `μ_i` là thế hóa học (J/mol); `μ_i0` là thế hóa học chuẩn; `γ±` là hệ số hoạt độ ion trung bình (); `ν+` là số cation trong công thức; `ν-` là số anion trong công thức.

*Điều kiện:* Khi dung dịch loãng vô hạn thì γ -> 1 và a -> C/C0

*Ghi chú:* Hoạt độ là 'nồng độ hiệu dụng'. Với chất điện li, chỉ đo được γ± chứ không đo riêng γ+ hay γ-.

<sub>`chemistry.dai-hoc.dung-dich.hoat-do-he-so-hoat-do` · lớp 13 · #dung-dich #hoat-do #dien-li</sub>

---

**Thế hóa học của cấu tử trong dung dịch lí tưởng** — *Chemical potential in an ideal solution*

$$\mu_{i} = \mu_{i}^{*} + RT\ln x_{i};\qquad \Delta G_{tr} = nRT\sum x_{i}\ln x_{i};\quad \Delta H_{tr} = 0;\quad \Delta V_{tr} = 0$$

Trong đó: `μ_i` là thế hóa học của cấu tử i trong dung dịch (J/mol); `μ_i*` là thế hóa học của i nguyên chất (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `x_i` là phần mol của i (); `ΔG_tr` là biến thiên năng lượng Gibbs khi trộn (J); `ΔH_tr` là nhiệt trộn (J); `ΔV_tr` là biến thiên thể tích khi trộn (m^3); `n` là tổng số mol.

*Điều kiện:* Dung dịch lí tưởng: tuân theo định luật Raoult ở mọi nồng độ

*Ghi chú:* Dung dịch thực thay x_i bằng hoạt độ a_i. Vì ln x_i < 0 nên ΔG_tr < 0: quá trình trộn luôn tự diễn biến.

<sub>`chemistry.dai-hoc.dung-dich.the-hoa-hoc-dung-dich-li-tuong` · lớp 13 · #dung-dich #the-hoa-hoc #li-tuong</sub>

---

**Áp suất thẩm thấu (phương trình Van't Hoff)** — *Osmotic pressure (Van't Hoff equation)*

$$\pi = i\,C_{M}RT = i\,\frac{n}{V}RT$$

Trong đó: `π` là áp suất thẩm thấu (Pa); `i` là hệ số Van't Hoff (); `C_M` là nồng độ mol của chất tan (mol/m^3); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `n` là số mol chất tan (mol); `V` là thể tích dung dịch (m^3).

*Điều kiện:* Dung dịch loãng, màng bán thấm chỉ cho dung môi đi qua

*Ghi chú:* Rất nhạy: dung dịch 0.01 M ở 25 độ C đã cho π ≈ 0.25 bar, nên dùng để xác định khối lượng mol polymer. Dùng R = 0.08206 L.atm/(mol.K) nếu π tính bằng atm và C bằng mol/L.

<sub>`chemistry.dai-hoc.dung-dich.ap-suat-tham-thau` · lớp 13 · #dung-dich #tham-thau #tinh-chat-tap-hop</sub>

---

**Độ giảm áp suất hơi tương đối** — *Relative lowering of vapour pressure*

$$\frac{p_{1}^{*} - p_{1}}{p_{1}^{*}} = x_{2}$$

Trong đó: `p_1*` là áp suất hơi của dung môi nguyên chất (Pa); `p_1` là áp suất hơi của dung môi trên dung dịch (Pa); `x_2` là phần mol chất tan ().

*Điều kiện:* Chất tan không bay hơi, không điện li; dung dịch lí tưởng hoặc rất loãng

*Ghi chú:* Với chất điện li phải nhân thêm hệ số Van't Hoff i. Đây là một trong bốn tính chất tập hợp (colligative).

<sub>`chemistry.dai-hoc.dung-dich.do-giam-ap-suat-hoi-tuong-doi` · lớp 13 · #dung-dich #raoult #tinh-chat-tap-hop</sub>

---

**Độ hạ điểm đông đặc của dung dịch** — *Freezing-point depression*

$$\Delta T_{f} = i\,K_{f}\,C_{m};\qquad K_{f} = \frac{R\,T_{f}^{*2}M_{1}}{\Delta H_{nc}}$$

Trong đó: `ΔT_f` là độ hạ nhiệt độ đông đặc (K); `i` là hệ số Van't Hoff (); `K_f` là hằng số nghiệm lạnh (nghiệm đông) của dung môi (K.kg/mol); `C_m` là nồng độ molan (mol/kg); `R` là hằng số khí (J/(mol.K)); `T_f*` là nhiệt độ đông đặc của dung môi nguyên chất (K); `M_1` là khối lượng mol dung môi (kg/mol); `ΔH_nc` là nhiệt nóng chảy mol của dung môi (J/mol).

*Điều kiện:* Dung dịch loãng; chỉ dung môi nguyên chất kết tinh ra

*Ghi chú:* Nước: K_f = 1.86 K.kg/mol; benzene: 5.12; camphor: 40. Dùng để xác định khối lượng mol: M_2 = K_f.m_2/(ΔT_f.m_1).

<sub>`chemistry.dai-hoc.dung-dich.do-ha-diem-dong-dac` · lớp 13 · #dung-dich #nghiem-lanh #tinh-chat-tap-hop</sub>

---

**Độ tăng điểm sôi của dung dịch** — *Boiling-point elevation*

$$\Delta T_{s} = i\,K_{b}\,C_{m};\qquad K_{b} = \frac{R\,T_{s}^{*2}M_{1}}{\Delta H_{hh}}$$

Trong đó: `ΔT_s` là độ tăng nhiệt độ sôi (K); `i` là hệ số Van't Hoff (bằng 1 với chất không điện li) (); `K_b` là hằng số nghiệm sôi của dung môi (K.kg/mol); `C_m` là nồng độ molan của chất tan (mol/kg); `R` là hằng số khí (J/(mol.K)); `T_s*` là nhiệt độ sôi của dung môi nguyên chất (K); `M_1` là khối lượng mol dung môi (kg/mol); `ΔH_hh` là nhiệt hóa hơi mol của dung môi (J/mol).

*Điều kiện:* Dung dịch loãng, chất tan không bay hơi

*Ghi chú:* Nước: K_b = 0.512 K.kg/mol; benzene: 2.53; camphor: 5.95. K_b chỉ phụ thuộc bản chất dung môi.

<sub>`chemistry.dai-hoc.dung-dich.do-tang-diem-soi` · lớp 13 · #dung-dich #nghiem-soi #tinh-chat-tap-hop</sub>

---

**Xác định khối lượng mol chất tan bằng phương pháp nghiệm lạnh** — *Molar mass determination by cryoscopy*

$$M_{2} = \frac{K_{f}\,m_{2}}{\Delta T_{f}\,m_{1}}$$

Trong đó: `M_2` là khối lượng mol chất tan (kg/mol); `K_f` là hằng số nghiệm lạnh của dung môi (K.kg/mol); `m_2` là khối lượng chất tan (kg); `ΔT_f` là độ hạ nhiệt độ đông đặc đo được (K); `m_1` là khối lượng dung môi (kg).

*Điều kiện:* Chất tan không điện li, không kết hợp; dung dịch loãng

*Ghi chú:* Nếu chất tan điện li hoặc kết hợp phân tử thì M tính được sai lệch so với thực - từ đó suy ra hệ số i hoặc mức độ kết hợp.

<sub>`chemistry.dai-hoc.dung-dich.xac-dinh-khoi-luong-mol` · lớp 13 · #dung-dich #nghiem-lanh #khoi-luong-mol</sub>

---

**Định luật Raoult** — *Raoult's law*

$$p_{i} = x_{i}\,p_{i}^{*};\qquad P = \sum_{i} x_{i}p_{i}^{*}$$

Trong đó: `p_i` là áp suất hơi riêng phần của cấu tử i trên dung dịch (Pa); `x_i` là phần mol của i trong pha lỏng (); `p_i*` là áp suất hơi bão hòa của i nguyên chất ở cùng nhiệt độ (Pa); `P` là áp suất hơi tổng (Pa).

*Điều kiện:* Dung dịch lí tưởng (các cấu tử giống nhau về bản chất) hoặc dung môi trong dung dịch rất loãng

*Ghi chú:* Dung dịch thực có sai lệch dương (lực hút giữa các cấu tử khác loại yếu hơn) hoặc sai lệch âm. Thành phần pha hơi: y_i = p_i/P.

<sub>`chemistry.dai-hoc.dung-dich.dinh-luat-raoult` · lớp 13 · #dung-dich #raoult #ap-suat-hoi</sub>

---

**Định luật Henry** — *Henry's law*

$$p_{2} = K_{H}\,x_{2} \quad \text{hoặc} \quad C_{2} = k_{H}\,p_{2}$$

Trong đó: `p_2` là áp suất riêng phần của khí trên dung dịch (bar); `K_H` là hằng số Henry (dạng áp suất) (bar); `x_2` là phần mol khí tan trong dung dịch (); `C_2` là nồng độ khí tan (mol/L); `k_H` là hằng số Henry (dạng nồng độ), k_H = 1/K_H quy đổi (mol/(L.bar)).

*Điều kiện:* Dung dịch loãng của chất khí ít tan, khí không phản ứng với dung môi

*Ghi chú:* Định luật Raoult mô tả dung môi, định luật Henry mô tả chất tan trong dung dịch loãng. K_H tăng khi nhiệt độ tăng, nên độ tan của khí giảm khi đun nóng.

<sub>`chemistry.dai-hoc.dung-dich.dinh-luat-henry` · lớp 13 · #dung-dich #henry #do-tan-khi</sub>

---

### Dung dịch và điện hoá nâng cao

**Phương trình Nernst - Einstein** — *Nernst - Einstein equation*

$$\lambda_{i} = \frac{z_{i}^{2}D_{i}F^{2}}{RT};\qquad \Lambda_{m}^{\circ} = \frac{F^{2}}{RT}\left(\nu_{+}z_{+}^{2}D_{+} + \nu_{-}z_{-}^{2}D_{-}\right)$$

Trong đó: `λ_i` là độ dẫn điện mol của ion i (S.m^2/mol); `z_i` là điện tích của ion i (); `D_i` là hệ số khuếch tán của ion i (m^2/s); `F` là hằng số Faraday (C/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `Λ_m°` là độ dẫn điện mol giới hạn của chất điện li (S.m^2/mol); `ν_+` là số cation trong công thức (); `ν_-` là số anion trong công thức (); `z_+` là điện tích cation (); `z_-` là điện tích anion (); `D_+` là hệ số khuếch tán cation (m^2/s); `D_-` là hệ số khuếch tán anion (m^2/s).

*Điều kiện:* Dung dịch loãng; ion chuyển động độc lập; áp dụng ở pha loãng vô hạn

*Ghi chú:* Atkins Focus 16B. Cầu nối định lượng giữa ĐỘ DẪN ĐIỆN (đo bằng điện hoá) và HỆ SỐ KHUẾCH TÁN (đại lượng vận chuyển) - cùng một chuyển động nhiệt của ion. Kho Việt Nam có linh độ ion và Kohlrausch nhưng không có liên hệ với hệ số khuếch tán.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.phuong-trinh-nernst-einstein` · lớp 13 · #dien-hoa #nernst-einstein #khuech-tan #intl-undergrad</sub>

---

**Phương trình Stokes - Einstein** — *Stokes - Einstein equation*

$$D = \frac{k_{B}T}{6\pi\eta a};\qquad u = \frac{|z|eD}{k_{B}T} = \frac{|z|e}{6\pi\eta a}$$

Trong đó: `D` là hệ số khuếch tán của tiểu phân (m^2/s); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `η` là độ nhớt của dung môi (Pa.s); `a` là bán kính thuỷ động học của tiểu phân (m); `u` là linh độ điện của ion (m^2/(V.s)); `z` là điện tích ion (); `e` là điện tích nguyên tố (C).

*Điều kiện:* Tiểu phân hình cầu lớn hơn nhiều so với phân tử dung môi; chế độ chảy tầng (định luật Stokes); điều kiện dính (stick) trên bề mặt

*Ghi chú:* Atkins Focus 16B. Kho Việt Nam có phương trình Einstein - Smoluchowski về chuyển động Brown và phương trình Stokes về sa lắng, nhưng không có dạng D = kT/(6πηa) - dạng dùng để suy bán kính thuỷ động học của protein và hạt nano từ phép đo DLS. Bất thường quan trọng: H+ và OH- có linh độ cao bất thường do cơ chế Grotthuss chứ không phải khuếch tán Stokes.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.phuong-trinh-stokes-einstein` · lớp 13 · #dung-dich #stokes-einstein #khuech-tan #intl-undergrad</sub>

---

**Các hàm nhiệt động của quá trình trộn lí tưởng** — *Thermodynamic functions of ideal mixing*

$$\Delta_{\text{trộn}}G = nRT\sum_{J}x_{J}\ln x_{J} < 0;\qquad \Delta_{\text{trộn}}S = -nR\sum_{J}x_{J}\ln x_{J} > 0;\qquad \Delta_{\text{trộn}}H = 0;\qquad \Delta_{\text{trộn}}V = 0$$

Trong đó: `Δ_trộnG` là biến thiên năng lượng Gibbs khi trộn (J); `Δ_trộnS` là biến thiên entropy khi trộn (J/K); `Δ_trộnH` là biến thiên enthalpy khi trộn (J); `Δ_trộnV` là biến thiên thể tích khi trộn (m^3); `n` là tổng số mol (mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `x_J` là phân số mol cấu tử J ().

*Điều kiện:* Dung dịch lí tưởng (mọi tương tác A-A, B-B, A-B như nhau); áp dụng cho cả hỗn hợp khí lí tưởng

*Ghi chú:* Atkins Focus 5B. Trộn lí tưởng là quá trình HOÀN TOÀN do entropy điều khiển. Kho Việt Nam có entropy trộn khí lí tưởng nhưng không có bộ đầy đủ bốn hàm trộn cho dung dịch lỏng lí tưởng.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.ham-tron-li-tuong` · lớp 13 · #dung-dich #tron #entropy #intl-undergrad</sub>

---

**Hàm dư và mô hình dung dịch chính quy** — *Excess functions and the regular solution model*

$$X^{E} = \Delta_{\text{trộn}}X - \Delta_{\text{trộn}}X^{\text{lí tưởng}};\qquad H^{E} = n\xi RT\,x_{A}x_{B};\qquad \ln\gamma_{A} = \xi x_{B}^{2},\quad \ln\gamma_{B} = \xi x_{A}^{2}$$

Trong đó: `X^E` là hàm dư của đại lượng X (); `H^E` là enthalpy dư (J); `n` là tổng số mol (mol); `ξ` là tham số tương tác của dung dịch chính quy (); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `x_A` là phân số mol A (); `x_B` là phân số mol B (); `γ_A` là hệ số hoạt độ của A (); `γ_B` là hệ số hoạt độ của B (); `Δ_trộnX` là biến thiên đại lượng X khi trộn thực tế (); `Δ_trộnX^lí tưởng` là biến thiên đại lượng X khi trộn lí tưởng cùng thành phần (); `X` là một hàm nhiệt động quảng tính bất kì (G, H, S, V, ...) ().

*Điều kiện:* Dung dịch chính quy: S^E = 0 nhưng H^E khác 0 (phân bố phân tử vẫn ngẫu nhiên nhưng năng lượng tương tác A-B khác trung bình của A-A và B-B)

*Ghi chú:* Atkins Focus 5D. ξ > 0 (tương tác A-B kém thuận lợi) và ξ > 2 thì dung dịch tách thành hai pha - mô hình đơn giản nhất giải thích sự không trộn lẫn và nhiệt độ tới hạn dung hợp. Kho Việt Nam không có hàm dư.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.dung-dich-chinh-quy` · lớp 13 · #dung-dich #ham-du #dung-dich-chinh-quy #intl-undergrad</sub>

---

**Hệ số thẩm thấu của dung môi** — *Osmotic coefficient of the solvent*

$$\phi = -\frac{x_{A}}{x_{B}}\ln a_{A};\qquad \phi \to 1\ \text{khi } x_{B}\to 0$$

Trong đó: `φ` là hệ số thẩm thấu (thang phân số mol) (); `x_A` là phân số mol dung môi (); `x_B` là phân số mol chất tan (); `a_A` là hoạt độ của dung môi ().

*Điều kiện:* Dung dịch loãng; dùng khi γ_A rất gần 1 nên sai số tương đối của (1 - γ_A) lớn

*Ghi chú:* Atkins Focus 5F. Hệ số thẩm thấu nhạy hơn hệ số hoạt độ khi mô tả độ lệch của DUNG MÔI khỏi lí tưởng, nên là đại lượng chuẩn trong hoá lí dung dịch điện li và hoá sinh vật lí. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.he-so-tham-thau-dung-moi` · lớp 13 · #dung-dich #he-so-tham-thau #hoat-do #intl-undergrad</sub>

---

**Hai quy ước định nghĩa hoạt độ: Raoult và Henry** — *The Raoult and Henry conventions for activity*

$$\text{(I) } a_{A} = \frac{p_{A}}{p_{A}^{*}},\ \gamma_{A} = \frac{a_{A}}{x_{A}} \to 1\ \text{khi } x_{A}\to 1;\qquad \text{(II) } a_{B} = \frac{p_{B}}{K_{B}},\ \gamma_{B} = \frac{a_{B}}{x_{B}} \to 1\ \text{khi } x_{B}\to 0$$

Trong đó: `a_A` là hoạt độ của dung môi (quy ước I) (); `p_A` là áp suất hơi riêng phần của dung môi (Pa); `p_A*` là áp suất hơi bão hoà của dung môi nguyên chất (Pa); `γ_A` là hệ số hoạt độ của dung môi (); `x_A` là phân số mol dung môi (); `a_B` là hoạt độ của chất tan (quy ước II) (); `p_B` là áp suất hơi riêng phần của chất tan (Pa); `K_B` là hằng số Henry của chất tan (Pa); `γ_B` là hệ số hoạt độ của chất tan (); `x_B` là phân số mol chất tan ().

*Điều kiện:* Quy ước I (trạng thái chuẩn là chất nguyên chất) dùng cho dung môi; quy ước II (trạng thái chuẩn là dung dịch loãng lí tưởng giả định) dùng cho chất tan

*Ghi chú:* Atkins Focus 5E. Kho Việt Nam có hoạt độ với trạng thái chuẩn nồng độ 1 mol/L nhưng KHÔNG phân biệt hai quy ước Raoult/Henry - đây là khác biệt quy ước đáng kể, vì cùng một dung dịch có hai giá trị γ khác nhau tuỳ trạng thái chuẩn chọn.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.hoat-do-hai-quy-uoc-raoult-henry` · lớp 13 · #dung-dich #hoat-do #raoult #henry #intl-undergrad</sub>

---

**Hoạt độ trung bình ion và molan trung bình ion trên thang molan** — *Mean ionic activity and mean ionic molality on the molality scale*

$$a_{\pm} = \left(a_{+}^{p}\,a_{-}^{q}\right)^{1/s},\quad s = p+q;\qquad a\!\left(\mathrm{M}_{p}\mathrm{X}_{q}\right) = a_{\pm}^{s};\qquad a_{\pm} = \gamma_{\pm}\frac{b_{\pm}}{b^{\circ}},\qquad b_{\pm} = \left(p^{p}q^{q}\right)^{1/s} b$$

Trong đó: `a_±` là hoạt độ trung bình ion (); `a_+` là hoạt độ của cation (); `a_-` là hoạt độ của anion (); `p` là số cation trong công thức M_pX_q (); `q` là số anion trong công thức M_pX_q (); `s` là tổng số ion trên một đơn vị công thức, s = p + q (); `a` là hoạt độ của chất điện li nguyên vẹn M_pX_q (); `γ_±` là hệ số hoạt độ trung bình ion (thang molan) (); `b_±` là molan trung bình ion (mol/kg); `b` là molan của chất điện li (mol/kg); `b°` là molan chuẩn, quy ước bằng 1 mol/kg (mol/kg); `M` là kí hiệu cation trong công thức chất điện li M_pX_q (); `X` là kí hiệu anion trong công thức chất điện li M_pX_q ().

*Điều kiện:* Chất điện li M_pX_q tan hoàn toàn; hoạt độ của từng ion riêng lẻ KHÔNG đo được bằng thực nghiệm (vì không thể thay đổi nồng độ một ion mà giữ nguyên điện trung hoà), chỉ tổ hợp trung bình a_± mới có nghĩa nhiệt động; trạng thái chuẩn là dung dịch loãng lí tưởng giả định ở b° = 1 mol/kg (quy ước Henry)

*Ghi chú:* Atkins Focus 5F. QUY ƯỚC KHÁC BIỆT quan trọng: kho Việt Nam định nghĩa hoạt độ trên thang NỒNG ĐỘ MOL với trạng thái chuẩn C° = 1 mol/L (chemistry.dai-hoc.dung-dich.hoat-do-he-so-hoat-do, ở đó đã có biểu thức γ_± theo ν+ và ν-); giáo trình quốc tế (Atkins, Levine) dùng thang MOLAN b (mol/kg dung môi) vì molan không phụ thuộc nhiệt độ và áp suất. Bản ghi này bổ sung hai đại lượng mà kho chưa có: molan trung bình ion b_± = (p^p q^q)^{1/s} b và hệ thức a = a_±^s. Ví dụ: với CaCl2 (p = 1, q = 2, s = 3) thì b_± = 4^{1/3} b = 1.587b và a = a_±^3; với NaCl thì b_± = b. Định luật giới hạn Debye - Hückel lg γ_± = -A|z+z-|căn(I) phát biểu cho chính γ_± này.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.hoat-do-trung-binh-ion-thang-molan` · lớp 13 · #hoat-do #dien-li #thang-molan #intl-undergrad</sub>

---

**Đại lượng mol riêng phần** — *Partial molar quantity*

$$V_{J} = \left(\frac{\partial V}{\partial n_{J}}\right)_{p,T,n_{i\neq J}};\qquad V = \sum_{J}n_{J}V_{J}$$

Trong đó: `V_J` là thể tích mol riêng phần của cấu tử J (m^3/mol); `V` là thể tích tổng của dung dịch (m^3); `n_J` là số mol cấu tử J (mol); `p` là áp suất (Pa); `T` là nhiệt độ tuyệt đối (K); `n_i` là số mol các cấu tử khác (mol).

*Điều kiện:* Định nghĩa cho mọi hàm trạng thái quảng tính (V, G, H, S, ...); giá trị phụ thuộc thành phần dung dịch

*Ghi chú:* Atkins Focus 5A. Đại lượng mol riêng phần CÓ THỂ ÂM: thêm MgSO4 vào nước làm thể tích giảm nên V(MgSO4) khoảng -1.4 cm^3/mol ở pha loãng vô hạn. Thế hoá học chính là năng lượng Gibbs mol riêng phần. Kho Việt Nam có thế hoá học nhưng không có khái niệm đại lượng mol riêng phần tổng quát.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.dai-luong-mol-rieng-phan` · lớp 13 · #dung-dich #mol-rieng-phan #intl-undergrad</sub>

---

**Phương trình Gibbs - Duhem** — *Gibbs - Duhem equation*

$$\sum_{J}n_{J}\,d\mu_{J} = 0\quad (T,p\ \text{không đổi});\qquad x_{A}\,d\mu_{A} + x_{B}\,d\mu_{B} = 0$$

Trong đó: `n_J` là số mol cấu tử J (mol); `μ_J` là thế hoá học của cấu tử J (J/mol); `x_A` là phân số mol cấu tử A (); `x_B` là phân số mol cấu tử B (); `μ_A` là thế hoá học của A (J/mol); `μ_B` là thế hoá học của B (J/mol); `T` là nhiệt độ (K); `p` là áp suất (Pa).

*Điều kiện:* Nhiệt độ và áp suất không đổi; áp dụng cho mọi đại lượng mol riêng phần, không chỉ thế hoá học

*Ghi chú:* Atkins Focus 5A. Hệ quả then chốt: thế hoá học của hai cấu tử KHÔNG độc lập - nếu μ của một cấu tử tăng thì μ của cấu tử kia phải giảm. Từ đó suy ra: nếu một cấu tử tuân theo định luật Raoult trong một khoảng thành phần thì cấu tử kia BẮT BUỘC tuân theo định luật Henry trong khoảng đó. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.phuong-trinh-gibbs-duhem` · lớp 13 · #dung-dich #gibbs-duhem #the-hoa-hoc #intl-undergrad</sub>

---

**Độ dài Debye (bề dày khí quyển ion)** — *Debye length (thickness of the ionic atmosphere)*

$$r_{D} = \left(\frac{\varepsilon_{0}\varepsilon_{r}RT}{2F^{2}I_{c}}\right)^{1/2};\qquad r_{D}\ (\mathrm{nm}) \approx \frac{0.304}{\sqrt{I_{c}/(\mathrm{mol\,L^{-1}})}}\ \text{trong nước ở } 25\,^{\circ}\mathrm{C}$$

Trong đó: `r_D` là độ dài Debye (m); `ε_0` là hằng số điện môi chân không (F/m); `ε_r` là hằng số điện môi tương đối của dung môi (); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `F` là hằng số Faraday (C/mol); `I_c` là lực ion tính theo nồng độ mol (mol/L).

*Điều kiện:* Chất điện li 1:1 trong dung dịch loãng; công thức rút gọn 0.304 nm áp dụng cho nước ở 25 độ C (ε_r = 78.4)

*Ghi chú:* Atkins Focus 5F, 16D. Ví dụ: NaCl 0.1 M cho r_D khoảng 0.96 nm; NaCl 1 mM cho r_D khoảng 9.6 nm. Tăng lực ion làm 'nén' lớp điện kép - cơ sở lượng hoá của quy tắc Schulze - Hardy về keo tụ và của thế zeta. F = 96485.332 C/mol. Kho Việt Nam có thế zeta và Debye - Hückel nhưng không có độ dài Debye.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.do-dai-debye` · lớp 13 · #dien-hoa #lop-dien-kep #debye #intl-undergrad</sub>

---

**Cân bằng Donnan qua màng bán thấm** — *Donnan membrane equilibrium*

$$[\mathrm{Na^{+}}]_{\text{trong}}[\mathrm{Cl^{-}}]_{\text{trong}} = [\mathrm{Na^{+}}]_{\text{ngoài}}[\mathrm{Cl^{-}}]_{\text{ngoài}};\qquad \Delta\phi = \frac{RT}{F}\ln\frac{[\mathrm{Na^{+}}]_{\text{ngoài}}}{[\mathrm{Na^{+}}]_{\text{trong}}}$$

Trong đó: `[Na+]_trong` là nồng độ cation khuếch tán được ở phía trong màng (mol/L); `[Cl-]_trong` là nồng độ anion khuếch tán được ở phía trong màng (mol/L); `[Na+]_ngoài` là nồng độ cation ở phía ngoài màng (mol/L); `[Cl-]_ngoài` là nồng độ anion ở phía ngoài màng (mol/L); `Δφ` là thế Donnan, quy ước Δφ = φ(phía trong) - φ(phía ngoài) (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `F` là hằng số Faraday (C/mol).

*Điều kiện:* Màng cho ion nhỏ đi qua nhưng giữ lại polyion (protein, polyelectrolyte) ở một phía; hệ ở cân bằng nhiệt động, không phải trạng thái dừng. Biểu thức Δφ suy từ điều kiện thế điện hoá học của Na+ bằng nhau ở hai phía, với quy ước Δφ = φ_trong - φ_ngoài

*Ghi chú:* Atkins Focus 5F/16C. Hệ quả: phía chứa polyion tích điện âm sẽ tích luỹ cation và nghèo anion, đồng thời có áp suất thẩm thấu dư - cần hiệu chỉnh khi xác định khối lượng mol protein bằng phép đo thẩm thấu. Khác với thế màng Goldman - Hodgkin - Katz (trạng thái dừng, đã có ở file sinh học). Kho Việt Nam không có cân bằng Donnan trong hoá học.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.can-bang-donnan` · lớp 13 · #dien-hoa #donnan #mang #intl-undergrad</sub>

---

**Thế điện hoá học của ion** — *Electrochemical potential of an ion*

$$\tilde{\mu}_{i} = \mu_{i} + z_{i}F\phi = \mu_{i}^{\circ} + RT\ln a_{i} + z_{i}F\phi;\qquad \tilde{\mu}_{i}^{(\alpha)} = \tilde{\mu}_{i}^{(\beta)}\ \text{khi cân bằng}$$

Trong đó: `μ̃_i` là thế điện hoá học của ion i (J/mol); `μ_i` là thế hoá học của ion i (J/mol); `μ_i°` là thế hoá học chuẩn (J/mol); `z_i` là điện tích của ion (kèm dấu) (); `F` là hằng số Faraday (C/mol); `φ` là thế điện Galvani của pha (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `a_i` là hoạt độ của ion i (); `α` là kí hiệu pha thứ nhất (); `β` là kí hiệu pha thứ hai ().

*Điều kiện:* Pha mang điện; điều kiện cân bằng của ion giữa hai pha là thế ĐIỆN HOÁ HỌC bằng nhau (không phải thế hoá học)

*Ghi chú:* Atkins Focus 16C. Đây là đại lượng nền tảng để dẫn ra phương trình Nernst, thế màng, cân bằng Donnan và lực đẩy proton trong hoá sinh. Kho Việt Nam có thế hoá học và phương trình Nernst nhưng không có thế điện hoá học như khái niệm trung gian.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.the-dien-hoa-hoc` · lớp 13 · #dien-hoa #the-dien-hoa-hoc #intl-undergrad</sub>

---

**Phương trình Debye - Hückel - Onsager** — *Debye - Hückel - Onsager equation*

$$\Lambda_{m} = \Lambda_{m}^{\circ} - \left(A + B\Lambda_{m}^{\circ}\right)\sqrt{c}$$

Trong đó: `Λ_m` là độ dẫn điện mol ở nồng độ c (S.m^2/mol); `Λ_m°` là độ dẫn điện mol giới hạn (pha loãng vô hạn) (S.m^2/mol); `A` là hệ số hiệu ứng điện di (phụ thuộc dung môi và nhiệt độ) (S.m^2.mol^-1.(mol/L)^-0.5); `B` là hệ số hiệu ứng hồi phục ((mol/L)^-0.5); `c` là nồng độ mol của chất điện li (mol/L).

*Điều kiện:* Chất điện li mạnh, dung dịch loãng; hai hiệu ứng làm chậm ion: hiệu ứng ĐIỆN DI (khí quyển ion chuyển ngược chiều) và hiệu ứng HỒI PHỤC (khí quyển ion bị lệch tâm)

*Ghi chú:* Atkins Focus 16B. Kho Việt Nam đã có định luật Kohlrausch dạng thực nghiệm Λ_m = Λ_m° - K.căn(c); bản này là dạng LÍ THUYẾT giải thích và tách hằng số K thành hai đóng góp vật lí riêng biệt, với A và B tính được từ tính chất dung môi. Với chất điện li 1:1 trong nước ở 25 độ C: A = 6.02e-3 S.m^2.mol^-1.(mol/L)^-1/2 và B = 0.229 (mol/L)^-1/2.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.debye-huckel-onsager` · lớp 13 · #dien-hoa #do-dan-dien #onsager #intl-undergrad</sub>

---

**Dạng tuyến tính của phương trình Butler - Volmer ở quá thế nhỏ** — *Linearised Butler - Volmer equation at low overpotential*

$$j \approx \frac{j_{0}\,F\,\eta}{RT};\qquad R_{ct} = \frac{RT}{F\,j_{0}}\ \ (|\eta| \ll RT/F \approx 25.7\ \mathrm{mV}\ \text{ở}\ 25\,^{\circ}\mathrm{C})$$

Trong đó: `j` là mật độ dòng thực (A/m^2); `j_0` là mật độ dòng trao đổi (A/m^2); `F` là hằng số Faraday (C/mol); `η` là quá thế (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `R_ct` là điện trở chuyển điện tích (trên đơn vị diện tích) (ohm.m^2).

*Điều kiện:* Quá thế nhỏ (dưới khoảng 10 mV); phản ứng một electron; khai triển hàm mũ tới bậc nhất

*Ghi chú:* Atkins Focus 19E. Kho Việt Nam đã có Butler - Volmer đầy đủ và Tafel (giới hạn quá thế LỚN); bản này bổ sung giới hạn quá thế NHỎ, ở đó điện cực hành xử như một điện trở thuần - cơ sở của phép đo tổng trở điện hoá (EIS) và của việc xác định j_0. RT/F = 25.693 mV ở 298.15 K.

<sub>`chemistry.dai-hoc.dung-dich-dien-hoa-nang-cao.butler-volmer-qua-the-nho` · lớp 13 · #dien-hoa #butler-volmer #qua-the #intl-undergrad</sub>

---

### Hoá hữu cơ nâng cao

**Phương trình tốc độ và hệ quả lập thể của SN1 và SN2** — *Rate laws and stereochemical consequences of SN1 and SN2*

$$v_{\mathrm{SN2}} = k_{2}\left[\mathrm{RX}\right]\left[\mathrm{Nu^{-}}\right];\qquad v_{\mathrm{SN1}} = k_{1}\left[\mathrm{RX}\right]$$

Trong đó: `v_SN2` là tốc độ phản ứng thế lưỡng phân tử (mol/(L.s)); `v_SN1` là tốc độ phản ứng thế đơn phân tử (mol/(L.s)); `k_2` là hằng số tốc độ bậc hai của SN2 (L/(mol.s)); `k_1` là hằng số tốc độ bậc một của SN1 (bước ion hoá) (s^-1); `[RX]` là nồng độ dẫn xuất halogen (mol/L); `[Nu-]` là nồng độ tác nhân nucleophile (mol/L).

*Điều kiện:* SN2: một bước, trạng thái chuyển tiếp năm phối trí; SN1: hai bước với bước ion hoá chậm quyết định tốc độ

*Ghi chú:* Clayden ch.15. Hệ quả lập thể là tiêu chí phân biệt mạnh nhất: SN2 luôn NGHỊCH ĐẢO cấu hình (Walden inversion) và tốc độ giảm theo bậc carbon (methyl > bậc một > bậc hai, bậc ba hầu như không xảy ra); SN1 cho hỗn hợp raxemic (thường kèm phần nghịch đảo trội do cặp ion) và tốc độ tăng theo bậc carbon. Kho Việt Nam mô tả định tính SN1/SN2 nhưng không có bản ghi biểu thức tốc độ kèm hệ quả lập thể ở mức đại học quốc tế.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.dong-hoc-sn1-sn2` · lớp 13 · #huu-co #sn1-sn2 #co-che #intl-undergrad</sub>

---

**Nguyên lí Curtin - Hammett** — *Curtin - Hammett principle*

$$\frac{[\mathrm{P}_{1}]}{[\mathrm{P}_{2}]} = \frac{k_{1}K}{k_{2}} = \exp\!\left(-\frac{\Delta\Delta^{\ddagger}G}{RT}\right)$$

Trong đó: `[P_1]` là lượng sản phẩm sinh từ cấu dạng 1 (mol/L); `[P_2]` là lượng sản phẩm sinh từ cấu dạng 2 (mol/L); `k_1` là hằng số tốc độ phản ứng của cấu dạng 1 (s^-1); `k_2` là hằng số tốc độ phản ứng của cấu dạng 2 (s^-1); `K` là hằng số cân bằng giữa hai cấu dạng (); `ΔΔ‡G` là hiệu năng lượng của hai trạng thái chuyển tiếp (tính từ cùng một mốc) (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Hai cấu dạng (hoặc hai đồng phân) chuyển hoá lẫn nhau NHANH hơn nhiều so với tốc độ phản ứng tạo sản phẩm

*Ghi chú:* Clayden ch.31, Anslyn & Dougherty ch.7. Kết luận phản trực giác nhưng cực kì quan trọng: tỉ lệ sản phẩm KHÔNG phụ thuộc tỉ lệ dân số của hai cấu dạng ở trạng thái đầu, mà chỉ phụ thuộc HIỆU NĂNG LƯỢNG hai trạng thái chuyển tiếp. Vì vậy một cấu dạng chiếm dưới 1% vẫn có thể cho ra sản phẩm chính. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.nguyen-li-curtin-hammett` · lớp 13 · #huu-co #curtin-hammett #co-che #intl-undergrad</sub>

---

**Quy tắc Baldwin về đóng vòng** — *Baldwin's rules for ring closure*

$$n\text{-}\left(\mathrm{exo}\ \text{hoặc}\ \mathrm{endo}\right)\text{-}\left(\mathrm{tet},\ \mathrm{trig},\ \mathrm{dig}\right);\qquad 3\text{--}7\text{-}\mathrm{exo}\text{-}\mathrm{tet}\ \text{ưu tiên},\quad 5\text{--}6\text{-}\mathrm{endo}\text{-}\mathrm{tet}\ \text{bị cấm}$$

Trong đó: `n` là kích thước vòng được tạo thành (số nguyên tử) (); `exo` là liên kết bị đứt nằm NGOÀI vòng đang tạo (); `endo` là liên kết bị đứt nằm TRONG vòng đang tạo (); `tet` là carbon bị tấn công lai hoá sp3 (tetrahedral) (); `trig` là carbon bị tấn công lai hoá sp2 (trigonal) (); `dig` là carbon bị tấn công lai hoá sp (digonal) ().

*Điều kiện:* Quy tắc dựa trên yêu cầu HÌNH HỌC của góc tấn công: 180 độ với carbon tet (đường Bürgi - Dunitz cho tet là trục nối), khoảng 107 độ với carbon trig, khoảng 120 độ với carbon dig

*Ghi chú:* Clayden ch.31 và 42. Các trường hợp then chốt: 3-7-exo-tet ưu tiên; 5-6-endo-tet bị cấm; 3-7-exo-trig ưu tiên; 3-5-endo-trig bị cấm nhưng 6-7-endo-trig được phép; 3-4-exo-dig bị cấm còn 5-7-exo-dig và 3-7-endo-dig được phép. Đây là công cụ dự đoán sản phẩm đóng vòng chuẩn trong hoá hữu cơ đại học quốc tế; kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.quy-tac-baldwin` · lớp 13 · #huu-co #baldwin #dong-vong #intl-undergrad</sub>

---

**Tiên đề Hammond** — *Hammond postulate*

$$\Delta_{r}H \ll 0 \Rightarrow \text{TTCT giống CHẤT ĐẦU (sớm)};\qquad \Delta_{r}H \gg 0 \Rightarrow \text{TTCT giống SẢN PHẨM (muộn)}$$

Trong đó: `Δ_rH` là biến thiên enthalpy của bước phản ứng khảo sát (kJ/mol); `TTCT` là trạng thái chuyển tiếp ().

*Điều kiện:* Áp dụng cho từng BƯỚC cơ bản của cơ chế, không phải cho phản ứng tổng; hai trạng thái gần nhau về năng lượng thì cũng gần nhau về cấu trúc

*Ghi chú:* Clayden ch.12, Anslyn & Dougherty ch.7. Ứng dụng chuẩn: halogen hoá gốc tự do bằng Br2 rất thu nhiệt ở bước tách H nên TTCT giống gốc alkyl -> tính chọn lọc rất cao (bậc ba nhiều hơn bậc một); với Cl2 bước này toả nhiệt nên TTCT sớm, chọn lọc kém. Kho Việt Nam không có tiên đề Hammond như bản ghi độc lập.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.tien-de-hammond` · lớp 13 · #huu-co #hammond #co-che #intl-undergrad</sub>

---

**Quan hệ giữa độ chọn lọc đối quang và hiệu năng lượng hoạt hoá** — *Relation between enantioselectivity and the difference in activation energies*

$$\Delta\Delta^{\ddagger}G = -RT\ln\frac{k_{R}}{k_{S}} = -RT\ln(er)$$

Trong đó: `ΔΔ‡G` là hiệu năng lượng Gibbs hoạt hoá của hai trạng thái chuyển tiếp đối quang (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `k_R` là hằng số tốc độ tạo sản phẩm R (s^-1); `k_S` là hằng số tốc độ tạo sản phẩm S (s^-1); `er` là tỉ lệ đối quang của sản phẩm ().

*Điều kiện:* Kiểm soát động học (sản phẩm không cân bằng lại); phản ứng bất đối xứng dưới điều kiện xúc tác chọn lọc

*Ghi chú:* Clayden ch.41. Con số gây ấn tượng: ở 25 độ C (RT = 2.478 kJ/mol) chỉ cần ΔΔ‡G = RT.ln19 khoảng 7.3 kJ/mol để đạt er = 95:5 (ee = 90%), và RT.ln99 khoảng 11.4 kJ/mol để đạt er = 99:1 - nhỏ hơn năng lượng của một liên kết hydro. Đây là lí do xúc tác bất đối xứng khả thi nhưng khó tinh chỉnh: chỉ vài kJ/mol quyết định toàn bộ độ chọn lọc.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.chon-loc-doi-quang-va-ddg` · lớp 13 · #huu-co #hoa-lap-the #xuc-tac-bat-doi #intl-undergrad</sub>

---

**Độ dư đối quang, tỉ lệ đối quang và độ tinh khiết quang học** — *Enantiomeric excess, enantiomeric ratio and optical purity*

$$ee = \frac{|n_{R} - n_{S}|}{n_{R}+n_{S}}\times 100\%;\qquad er = n_{R}:n_{S};\qquad ee\,(\%) = \frac{er - 1}{er + 1}\times 100;\qquad ee \approx \frac{\left[\alpha\right]_{\text{mẫu}}}{\left[\alpha\right]_{\text{tinh khiết}}}\times 100$$

Trong đó: `ee` là độ dư đối quang (%); `n_R` là số mol đồng phân R (mol); `n_S` là số mol đồng phân S (mol); `er` là tỉ lệ đối quang (viết dưới dạng x:1) (); `[α]_mẫu` là độ quay cực riêng đo được của mẫu (độ.mL/(g.dm)); `[α]_tinh khiết` là độ quay cực riêng của đối quang tinh khiết (độ.mL/(g.dm)).

*Điều kiện:* Công thức tính ee theo độ quay cực chỉ đúng khi độ quay cực TỈ LỆ TUYẾN TÍNH với thành phần (không có hiệu ứng phi tuyến do liên hợp phân tử)

*Ghi chú:* Clayden ch.41. Ví dụ: er = 95:5 tương ứng ee = 90%; ee = 99% tương ứng er = 199:1. Ngày nay tài liệu quốc tế ưa dùng er hơn ee vì er tỉ lệ trực tiếp với hiệu năng lượng tự do của hai trạng thái chuyển tiếp. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.do-du-doi-quang-ee` · lớp 13 · #huu-co #hoa-lap-the #doi-quang #intl-undergrad</sub>

---

**Độ quay cực riêng** — *Specific rotation*

$$\left[\alpha\right]_{\lambda}^{T} = \frac{\alpha}{l\,c};\qquad \left[M\right]_{\lambda}^{T} = \frac{\left[\alpha\right]_{\lambda}^{T}\,M}{100}$$

Trong đó: `[α]` là độ quay cực riêng ở nhiệt độ T và bước sóng λ (độ.mL/(g.dm)); `α` là góc quay mặt phẳng phân cực đo được (độ); `l` là chiều dài ống đo (dm); `c` là nồng độ dung dịch (g/mL); `[M]` là độ quay cực mol (độ.cm^2/dmol); `M` là khối lượng mol chất quang hoạt (g/mol); `T` là nhiệt độ (K); `λ` là bước sóng ánh sáng dùng đo (nm).

*Điều kiện:* QUY ƯỚC BẮT BUỘC: l tính bằng ĐỀ-XI-MÉT và c tính bằng GAM TRÊN MILILÍT; thường đo ở vạch D của natri (589 nm) và 20 hoặc 25 độ C; với chất lỏng nguyên chất thay c bằng khối lượng riêng

*Ghi chú:* Clayden ch.14. Ghi kèm dung môi và nồng độ vì [α] phụ thuộc cả hai. Đây là đại lượng chuẩn trong hoá lập thể quốc tế; chương trình Việt Nam có nói tới tính quang hoạt nhưng không có bản ghi định lượng cho độ quay cực riêng với quy ước đơn vị dm và g/mL. PHẠM VI: A-Level và IB chỉ mô tả định tính hiện tượng quay mặt phẳng phân cực; công thức [α] với quy ước dm và g/mL là nội dung đại học, nên bản ghi này chỉ gắn intl-undergrad.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.do-quay-cuc-rieng` · lớp 13 · #huu-co #hoa-lap-the #quang-hoat #intl-undergrad</sub>

---

**Phân bố cấu dạng theo Boltzmann và năng lượng cấu dạng của butane** — *Boltzmann distribution of conformers and butane conformational energies*

$$\frac{N_{2}}{N_{1}} = \frac{g_{2}}{g_{1}}e^{-\Delta G^{\circ}/RT};\qquad \Delta G^{\circ}(\text{gauche} - \text{anti}) \approx 3.8\ \mathrm{kJ\,mol^{-1}}$$

Trong đó: `N_2` là số phân tử ở cấu dạng 2 (); `N_1` là số phân tử ở cấu dạng 1 (); `g_2` là bậc suy biến (số cấu dạng tương đương) của dạng 2 (); `g_1` là bậc suy biến của dạng 1 (); `ΔG°` là hiệu năng lượng Gibbs giữa hai cấu dạng (kJ/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Các cấu dạng chuyển hoá nhanh và ở cân bằng nhiệt; PHẢI tính bậc suy biến (butane có HAI cấu dạng gauche tương đương nhưng chỉ MỘT anti)

*Ghi chú:* Clayden ch.16. Số liệu chuẩn cho butane: gauche cao hơn anti khoảng 3.8 kJ/mol; hàng rào quay ethane khoảng 12 kJ/mol; hàng rào che khuất CH3-CH3 của butane khoảng 19-20 kJ/mol. Ở 298 K, tỉ lệ anti:gauche khoảng 70:30 sau khi tính hai cấu dạng gauche. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.phan-bo-boltzmann-cau-dang` · lớp 13 · #huu-co #cau-dang #boltzmann #intl-undergrad</sub>

---

**Giá trị A và cân bằng cấu dạng của cyclohexane thế** — *A-values and the conformational equilibrium of substituted cyclohexanes*

$$A = -\Delta G^{\circ}_{\text{ax}\to\text{eq}} = RT\ln K;\qquad K = \frac{\left[\text{eq}\right]}{\left[\text{ax}\right]} = e^{A/RT}$$

Trong đó: `A` là giá trị A của nhóm thế (ưu thế của vị trí xích đạo) (kJ/mol); `ΔG°` là biến thiên năng lượng Gibbs chuẩn khi chuyển nhóm thế từ vị trí trục sang vị trí xích đạo (mang dấu ÂM) (kJ/mol); `K` là hằng số cân bằng giữa hai cấu dạng ghế (); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `[eq]` là nồng độ cấu dạng có nhóm thế ở vị trí xích đạo (mol/L); `[ax]` là nồng độ cấu dạng có nhóm thế ở vị trí trục (mol/L).

*Điều kiện:* Cyclohexane một nhóm thế; theo định nghĩa A = -ΔG°(ax -> eq) nên A LUÔN DƯƠNG (vị trí xích đạo bền hơn) do tương tác 1,3-diaxial; với nhiều nhóm thế thì cộng gần đúng các giá trị A

*Ghi chú:* Clayden ch.16-18. Giá trị A tiêu biểu (kJ/mol): CH3 khoảng 7.3-7.6; C2H5 khoảng 7.5; iso-propyl khoảng 9.2; tert-butyl khoảng 21-23; OH khoảng 2.2-4.2; Cl và Br khoảng 1.8-2.1; C6H5 khoảng 12. Với tert-butyl, K vượt 4000 nên vòng coi như bị 'khoá' - kĩ thuật chuẩn để nghiên cứu lập thể. Kho Việt Nam không có phân tích cấu dạng định lượng.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.phan-tich-cau-dang-cyclohexane` · lớp 13 · #huu-co #cau-dang #cyclohexane #intl-undergrad</sub>

---

**Quy tắc Woodward - Hoffmann cho chuyển vị sigmatropic** — *Woodward - Hoffmann rules for sigmatropic rearrangements*

$$\left[i,j\right]\text{-sigmatropic}:\ N_{e} = i + j;\qquad N_{e} = 4n+2 \Rightarrow \text{suprafacial, cho phép NHIỆT};\qquad N_{e} = 4n \Rightarrow \text{phải antarafacial}$$

Trong đó: `i` là chỉ số thứ nhất của chuyển vị sigmatropic (); `j` là chỉ số thứ hai của chuyển vị sigmatropic (); `N_e` là tổng số electron tham gia trạng thái chuyển tiếp vòng (); `n` là số nguyên không âm ().

*Điều kiện:* Đếm số electron trong trạng thái chuyển tiếp vòng: một liên kết sigma đóng góp 2 electron, mỗi liên kết pi đóng góp 2 electron; chuyển vị [1,j] đếm (j+1) electron, chuyển vị [3,3] đếm 6 electron

*Ghi chú:* Clayden ch.36. Kết quả cụ thể: chuyển vị [1,5]-H (6 electron) xảy ra dễ dàng khi đun nóng theo kiểu suprafacial (cyclopentadiene); chuyển vị [1,3]-H (4 electron) suprafacial bị cấm nên không quan sát được; chuyển vị [3,3] (6 electron) là cơ sở của phản ứng Cope và Claisen. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.woodward-hoffmann-chuyen-vi-sigma` · lớp 13 · #huu-co #woodward-hoffmann #sigmatropic #intl-undergrad</sub>

---

**Quy tắc Woodward - Hoffmann cho phản ứng cộng vòng** — *Woodward - Hoffmann rules for cycloadditions*

$$N_{\pi} = 4n+2 \Rightarrow \left[\pi_{s} + \pi_{s}\right]\ \text{cho phép NHIỆT};\qquad N_{\pi} = 4n \Rightarrow \left[\pi_{s} + \pi_{a}\right]\ \text{cho phép nhiệt},\ \left[\pi_{s}+\pi_{s}\right]\ \text{cho phép QUANG HOÁ}$$

Trong đó: `N_π` là tổng số electron pi của cả hai thành phần (); `n` là số nguyên không âm (); `π_s` là thành phần pi phản ứng theo kiểu suprafacial (cùng phía) (); `π_a` là thành phần pi phản ứng theo kiểu antarafacial (khác phía) ().

*Điều kiện:* Cộng vòng đồng bộ; đếm TỔNG số electron pi của cả hai phân tử tham gia

*Ghi chú:* Clayden ch.34-35. Ví dụ chuẩn: Diels - Alder [4+2] có 6 electron pi nên cho phép nhiệt theo kiểu supra-supra (giải thích tính lập thể đặc thù cis và quy tắc endo). Ngược lại [2+2] có 4 electron pi nên bị CẤM về nhiệt nhưng cho phép khi chiếu sáng - lí do dimer hoá thymine trong DNA chỉ xảy ra dưới tia UV. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.woodward-hoffmann-cong-vong` · lớp 13 · #huu-co #woodward-hoffmann #diels-alder #intl-undergrad</sub>

---

**Quy tắc Woodward - Hoffmann cho phản ứng đóng/mở vòng electrocyclic** — *Woodward - Hoffmann rules for electrocyclic reactions*

$$\begin{array}{c|c|c} N_{\pi} & \text{nhiệt} & \text{quang hoá}\\ \hline 4n & \text{quay cùng chiều (con)} & \text{quay ngược chiều (dis)}\\ 4n+2 & \text{quay ngược chiều (dis)} & \text{quay cùng chiều (con)} \end{array}$$

Trong đó: `N_π` là số electron pi tham gia hệ liên hợp đóng vòng (); `n` là số nguyên không âm (); `con` là quay cùng chiều (conrotatory) (); `dis` là quay ngược chiều (disrotatory) ().

*Điều kiện:* Phản ứng vòng hoá đồng bộ (pericyclic) qua trạng thái chuyển tiếp vòng; điều kiện nhiệt dùng HOMO của trạng thái cơ bản, điều kiện quang hoá dùng HOMO của trạng thái kích thích thứ nhất

*Ghi chú:* Clayden ch.34-35. Hệ quả lập thể: butadiene (4 electron pi) đóng vòng NHIỆT theo kiểu con nên cho cyclobutene trans; hexatriene (6 electron pi) đóng vòng nhiệt theo kiểu dis. Chiếu sáng thì đảo ngược hoàn toàn. Đây là nội dung chuẩn của giáo trình hữu cơ đại học quốc tế (Clayden, Carey - Sundberg) và hoàn toàn không có trong kho Việt Nam.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.woodward-hoffmann-dong-vong` · lớp 13 · #huu-co #woodward-hoffmann #pericyclic #intl-undergrad</sub>

---

**Quy tắc Woodward - Hoffmann tổng quát** — *General Woodward - Hoffmann selection rule*

$$\text{Cho phép ở trạng thái cơ bản (nhiệt)} \Leftrightarrow \#\left[(4q+2)_{s}\right] + \#\left[(4r)_{a}\right] = \text{số LẺ}$$

Trong đó: `(4q+2)_s` là số thành phần chứa 4q+2 electron phản ứng theo kiểu suprafacial (); `(4r)_a` là số thành phần chứa 4r electron phản ứng theo kiểu antarafacial (); `q` là số nguyên không âm (); `r` là số nguyên không âm ().

*Điều kiện:* Phản ứng pericyclic đồng bộ bất kì; với phản ứng quang hoá (trạng thái kích thích thứ nhất) thì điều kiện đảo lại thành số CHẴN

*Ghi chú:* Clayden ch.36. Đây là dạng phát biểu THỐNG NHẤT bao trùm cả ba loại phản ứng pericyclic (electrocyclic, cộng vòng, sigmatropic) - dạng chuẩn trong giáo trình hữu cơ nâng cao quốc tế. Ví dụ Diels - Alder: một thành phần 4 electron suprafacial (không đếm) và một thành phần 2 electron suprafacial (đếm 1) nên tổng = 1, số lẻ, cho phép nhiệt. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.woodward-hoffmann-quy-tac-tong-quat` · lớp 13 · #huu-co #woodward-hoffmann #pericyclic #intl-undergrad</sub>

---

**Quy tắc Woodward - Fieser cho dien liên hợp** — *Woodward - Fieser rules for conjugated dienes*

$$\lambda_{\max} = \lambda_{\text{cơ sở}} + \sum_{i}\Delta_{i};\qquad \lambda_{\text{cơ sở}} = 217\ (\text{acyclic}),\ 214\ (\text{heteroannular}),\ 253\ (\text{homoannular})\ \mathrm{nm}$$

Trong đó: `λ_max` là bước sóng hấp thụ cực đại dự đoán (nm); `λ_cơ sở` là giá trị cơ sở theo kiểu khung dien (nm); `Δ_i` là số gia của yếu tố cấu trúc thứ i (nm).

*Điều kiện:* Chuyển dời pi -> pi* của hệ dien liên hợp; đo trong ethanol hoặc hexane; quy tắc chỉ áp dụng cho dien và trien, không áp dụng cho hệ thơm

*Ghi chú:* Pavia ch.7. Các số gia chuẩn: mỗi liên kết đôi kéo dài liên hợp +30; mỗi nhóm alkyl hoặc mảnh vòng +5; liên kết đôi ngoại vòng (exocyclic) +5; -OC(O)R (acyl oxy) 0; -OR +6; -SR +30; -Cl hoặc -Br +5; -NR2 +60. Đây là công cụ chuẩn của phần UV-Vis trong hoá hữu cơ đại học quốc tế, hoàn toàn không có trong chương trình Việt Nam.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.quy-tac-woodward-fieser-dien` · lớp 13 · #huu-co #woodward-fieser #uv-vis #intl-undergrad</sub>

---

**Quy tắc Woodward - Fieser cho hợp chất carbonyl liên hợp** — *Woodward - Fieser rules for conjugated carbonyl compounds*

$$\lambda_{\max} = \lambda_{\text{cơ sở}} + \sum_{i}\Delta_{i};\qquad \lambda_{\text{cơ sở}} = 215\ (\text{enone vòng 6 hoặc mạch hở}),\ 202\ (\text{enone vòng 5}),\ 210\ (\text{enal}),\ 195\ (\text{acid, ester})\ \mathrm{nm}$$

Trong đó: `λ_max` là bước sóng hấp thụ cực đại dự đoán (nm); `λ_cơ sở` là giá trị cơ sở theo kiểu khung carbonyl liên hợp (nm); `Δ_i` là số gia của yếu tố cấu trúc thứ i (nm).

*Điều kiện:* Chuyển dời pi -> pi* của hệ enone; giá trị cơ sở quy chiếu về dung môi ethanol nên phải hiệu chỉnh khi đo trong dung môi khác

*Ghi chú:* Pavia ch.7. Số gia chuẩn: liên kết đôi kéo dài liên hợp +30; thành phần dien đồng vòng (homoannular) +39; liên kết đôi ngoại vòng +5; nhóm alkyl hoặc mảnh vòng ở vị trí alpha +10, beta +12, gamma và xa hơn +18; -OH ở alpha +35, beta +30, delta +50; -OR ở alpha +35, beta +30, gamma +17, delta +31; -Cl ở alpha +15, beta +12; -Br ở alpha +25, beta +30; -NR2 ở beta +95. Bảng số gia có thay đổi nhỏ giữa các giáo trình nên khi làm bài phải dùng đúng bảng của tài liệu đang học. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.quy-tac-woodward-fieser-enone` · lớp 13 · #huu-co #woodward-fieser #uv-vis #intl-undergrad</sub>

---

**Các thang hằng số nhóm thế mở rộng sigma+ và sigma-** — *Extended substituent constant scales: sigma-plus and sigma-minus*

$$\sigma^{+}\ \text{(điện tích dương liên hợp trực tiếp)};\qquad \sigma^{-}\ \text{(điện tích âm liên hợp trực tiếp)};\qquad \lg\frac{k}{k_{0}} = \rho^{+}\sigma^{+}\ \text{hoặc}\ \rho^{-}\sigma^{-}$$

Trong đó: `σ+` là hằng số nhóm thế dùng khi điện tích dương liên hợp trực tiếp với nhóm thế (); `σ-` là hằng số nhóm thế dùng khi điện tích âm liên hợp trực tiếp với nhóm thế (); `ρ+` là hằng số phản ứng tương ứng với thang sigma+ (); `ρ-` là hằng số phản ứng tương ứng với thang sigma- (); `k` là hằng số tốc độ của dẫn xuất thế (s^-1); `k_0` là hằng số tốc độ của hợp chất không thế (s^-1).

*Điều kiện:* Dùng khi trung tâm phản ứng liên hợp TRỰC TIẾP với nhóm thế qua hệ pi (chỉ với nhóm thế ở para), khiến thang sigma thường không mô tả đúng

*Ghi chú:* Anslyn & Dougherty ch.8. Ví dụ: p-OCH3 có sigma = -0.27 nhưng sigma+ = -0.78 (do cho electron mạnh bằng cộng hưởng khi cần ổn định cation); p-NO2 có sigma = 0.78 nhưng sigma- = 1.27 (ổn định anion). Điểm gãy trong đồ thị Hammett hoặc việc phải chuyển sang thang sigma+ là bằng chứng về sự thay đổi cơ chế hoặc về bản chất điện tích ở trạng thái chuyển tiếp. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.hang-so-hammett-sigma-plus-minus` · lớp 13 · #huu-co #hammett #co-che #intl-undergrad</sub>

---

**Phương trình Hammett** — *Hammett equation*

$$\lg\frac{k}{k_{0}} = \rho\,\sigma;\qquad \lg\frac{K}{K_{0}} = \rho\,\sigma;\qquad \sigma_{X} \equiv \lg\frac{K_{X}}{K_{H}}\ (\text{acid benzoic, } \mathrm{H_{2}O},\ 25\,^{\circ}\mathrm{C})$$

Trong đó: `k` là hằng số tốc độ của dẫn xuất mang nhóm thế (s^-1); `k_0` là hằng số tốc độ của hợp chất không thế (X = H) (s^-1); `K` là hằng số cân bằng của dẫn xuất mang nhóm thế (); `K_0` là hằng số cân bằng của hợp chất không thế (); `ρ` là hằng số phản ứng (đặc trưng cho phản ứng và điều kiện) (); `σ` là hằng số nhóm thế (đặc trưng cho nhóm thế và vị trí meta/para) (); `K_X` là hằng số acid của acid benzoic thế X (mol/L); `K_H` là hằng số acid của acid benzoic (mol/L).

*Điều kiện:* Nhóm thế ở vị trí META hoặc PARA của vòng benzene (vị trí ortho bị nhiễu bởi hiệu ứng không gian nên không dùng); phản ứng phải có cùng cơ chế trong cả dãy

*Ghi chú:* Anslyn & Dougherty ch.8, Clayden ch.39. Theo định nghĩa ρ = 1 cho phản ứng ion hoá acid benzoic trong nước ở 25 độ C. Giá trị σ tiêu biểu: p-NO2 +0.78; m-NO2 +0.71; p-CN +0.66; p-Cl +0.23; H 0.00; p-CH3 -0.17; p-OCH3 -0.27; p-NH2 -0.66. Ý nghĩa dấu ρ: ρ > 0 thì trạng thái chuyển tiếp tích luỹ điện tích ÂM (nhóm hút electron làm nhanh); ρ < 0 thì tích luỹ điện tích DƯƠNG. Kho Việt Nam không có quan hệ năng lượng tự do tuyến tính.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.phuong-trinh-hammett` · lớp 13 · #huu-co #hammett #co-che #intl-undergrad</sub>

---

**Phương trình Taft tách hiệu ứng cảm ứng và hiệu ứng không gian** — *Taft equation separating polar and steric effects*

$$\lg\frac{k}{k_{0}} = \rho^{*}\sigma^{*} + \delta E_{s}$$

Trong đó: `k` là hằng số tốc độ của hợp chất khảo sát (s^-1); `k_0` là hằng số tốc độ của hợp chất chuẩn (thường nhóm methyl) (s^-1); `ρ*` là độ nhạy của phản ứng với hiệu ứng cảm ứng (phân cực) (); `σ*` là hằng số cảm ứng Taft của nhóm thế (); `δ` là độ nhạy của phản ứng với hiệu ứng không gian (); `E_s` là tham số không gian Taft của nhóm thế ().

*Điều kiện:* Áp dụng cho hệ béo (aliphatic) và hệ có nhóm thế ortho, nơi hiệu ứng không gian không thể bỏ qua; σ* và E_s xác định từ tốc độ thuỷ phân ester trong môi trường acid và base

*Ghi chú:* Anslyn & Dougherty ch.8. Ý tưởng gốc của Taft: thuỷ phân ester xúc tác ACID hầu như chỉ nhạy với hiệu ứng không gian, còn xúc tác BASE nhạy với cả hai - lấy hiệu hai logarit thì tách được σ*. E_s âm dần khi nhóm thế cồng kềnh hơn (CH3 = 0 theo quy ước, t-Bu khoảng -1.54). Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.phuong-trinh-taft` · lớp 13 · #huu-co #taft #hieu-ung-khong-gian #intl-undergrad</sub>

---

**Quy tắc cắt mạch trong phân tích retrosynthesis** — *Disconnection rules in retrosynthetic analysis*

$$\mathrm{TM} \Longrightarrow \mathrm{synthon}^{+} + \mathrm{synthon}^{-} \;\longrightarrow\; \mathrm{electrophile} + \mathrm{nucleophile};\qquad \text{cắt ở } C\text{--}X\ \text{và } C\text{--}C\ \text{cạnh nhóm chức}$$

Trong đó: `TM` là phân tử đích (target molecule) (); `synthon+` là mảnh mang điện tích dương hình thức (tương ứng tác nhân electrophile) (); `synthon-` là mảnh mang điện tích âm hình thức (tương ứng tác nhân nucleophile) (); `X` là dị tố (O, N, halogen) ().

*Điều kiện:* Mũi tên đôi (=>) chỉ phép cắt ngược, KHÔNG phải phản ứng thật; mỗi synthon phải tương ứng với một tác nhân (reagent) có thật

*Ghi chú:* Clayden ch.28. Ba nguyên tắc chọn chỗ cắt: (1) cắt ở liên kết C-X hoặc C-C gần nhóm chức vì ở đó phân cực sẵn; (2) cắt sao cho hai mảnh có độ lớn tương đương; (3) ưu tiên cắt tạo ra quan hệ 1,3-dioxy (aldol) hoặc 1,5-dioxy (Michael) - các quan hệ 'tự nhiên'; quan hệ 1,2- và 1,4- đòi hỏi umpolung (đảo cực). Đây là khung tư duy tổng hợp chuẩn quốc tế; kho Việt Nam không có.

<sub>`chemistry.dai-hoc.huu-co-nang-cao.phan-tich-retrosynthesis` · lớp 13 · #huu-co #retrosynthesis #tong-hop #intl-undergrad</sub>

---

### Hoá lượng tử

**Kí hiệu số hạng của phân tử hai nguyên tử** — *Molecular term symbol of a diatomic molecule*

$$^{2S+1}\Lambda_{\Omega}^{\pm}\ (g/u);\qquad \Lambda = \left|\sum_{i}\lambda_{i}\right|,\qquad \Sigma = \sum_{i} m_{s}(i),\qquad \Omega = \left|\Lambda + \Sigma\right|$$

Trong đó: `Λ` là số lượng tử hình chiếu momen obitan tổng lên trục phân tử (Λ = 0, 1, 2, 3 kí hiệu Σ, Π, Δ, Φ) (); `λ_i` là hình chiếu momen obitan của electron thứ i lên trục phân tử (); `S` là số lượng tử spin tổng (); `Σ` là hình chiếu spin tổng lên trục phân tử (); `m_s(i)` là hình chiếu spin của electron thứ i (); `Ω` là số lượng tử hình chiếu momen toàn phần lên trục phân tử (); `2S+1` là độ bội spin (); `g` là chỉ số chẵn (gerade) - chỉ dùng cho phân tử đồng hạch có tâm đối xứng (); `u` là chỉ số lẻ (ungerade) - chỉ dùng cho phân tử đồng hạch (); `±` là dấu đối xứng của hàm sóng đối với phép phản xạ qua mặt phẳng chứa trục phân tử, chỉ ghi cho trạng thái Σ ().

*Điều kiện:* Phân tử hai nguyên tử (đối xứng trụ quanh trục liên kết); ghép Russell - Saunders; các obitan phân tử đã đầy đóng góp Λ = 0 và S = 0; chỉ số g/u chỉ có nghĩa với phân tử đồng hạch, dấu ± chỉ ghi cho trạng thái Σ

*Ghi chú:* Atkins Focus 11F, Levine ch.13, Hollas ch.7. Đây là ngôn ngữ bắt buộc để đọc phổ điện tử phân tử, tương ứng với kí hiệu số hạng nguyên tử ^{2S+1}L_J. Ví dụ chuẩn: N2 có trạng thái cơ bản 1Σ_g+, O2 có 3Σ_g- (giải thích tính thuận từ của O2 - điều mà thuyết liên kết hoá trị không dự đoán được), NO có 2Π. Quy tắc lọc lựa cho chuyển dời điện tử của phân tử hai nguyên tử: ΔΛ = 0, ±1; ΔS = 0; g <-> u; và Σ+ <-> Σ+, Σ- <-> Σ-. Kho Việt Nam có cấu hình electron phân tử và bậc liên kết MO nhưng không có kí hiệu số hạng phân tử.

<sub>`chemistry.dai-hoc.hoa-luong-tu.ki-hieu-so-hang-phan-tu` · lớp 13 · #hoa-luong-tu #so-hang-phan-tu #pho-dien-tu #intl-undergrad</sub>

---

**Năng lượng obitan phân tử LCAO của hệ hai nguyên tử đồng hạch** — *LCAO molecular orbital energies of a homonuclear diatomic*

$$E_{\pm} = \frac{\alpha \pm \beta}{1 \pm S};\qquad \psi_{\pm} = \frac{1}{\sqrt{2(1 \pm S)}}\left(\chi_{A} \pm \chi_{B}\right)$$

Trong đó: `E_+` là năng lượng obitan liên kết (J); `E_-` là năng lượng obitan phản liên kết (J); `α` là tích phân Coulomb (H_AA = H_BB) (J); `β` là tích phân cộng hưởng (H_AB), giá trị âm (J); `S` là tích phân xen phủ giữa hai obitan nguyên tử (); `ψ_+` là obitan phân tử liên kết (); `ψ_-` là obitan phân tử phản liên kết (); `χ_A` là obitan nguyên tử trên tâm A (); `χ_B` là obitan nguyên tử trên tâm B ().

*Điều kiện:* Hai obitan nguyên tử tương đương (đồng hạch); khai triển LCAO hai hàm cơ sở

*Ghi chú:* Atkins Focus 9C. Vì mẫu số 1 - S nhỏ hơn 1 + S nên obitan phản liên kết bị đẩy lên NHIỀU HƠN mức obitan liên kết bị hạ xuống - kết quả này không thấy được nếu bỏ qua S, và là lí do He2 không bền. Kho Việt Nam mới chỉ có bậc liên kết MO chứ chưa có biểu thức năng lượng LCAO.

<sub>`chemistry.dai-hoc.hoa-luong-tu.lcao-mo-hai-nguyen-tu-dong-hach` · lớp 13 · #hoa-luong-tu #lcao #obitan-phan-tu #intl-undergrad</sub>

---

**Tích phân xen phủ, tích phân Coulomb và tích phân cộng hưởng** — *Overlap, Coulomb and resonance integrals*

$$S_{AB} = \int \chi_{A}^{*}\chi_{B}\,d\tau;\qquad \alpha = \int \chi_{A}^{*}\hat{H}\chi_{A}\,d\tau;\qquad \beta = \int \chi_{A}^{*}\hat{H}\chi_{B}\,d\tau$$

Trong đó: `S_AB` là tích phân xen phủ giữa hai obitan nguyên tử (); `α` là tích phân Coulomb (năng lượng của electron trên obitan nguyên tử trong phân tử) (J); `β` là tích phân cộng hưởng (tích phân trao đổi/tương tác giữa hai tâm) (J); `χ_A` là obitan nguyên tử trên tâm A (); `χ_B` là obitan nguyên tử trên tâm B (); `H` là toán tử Hamilton một electron của phân tử (J).

*Điều kiện:* Các obitan nguyên tử đã chuẩn hoá; 0 <= |S_AB| <= 1; S_AB = 0 khi hai obitan trực giao theo đối xứng

*Ghi chú:* Atkins Focus 9C. Xen phủ chỉ khác 0 khi hai obitan có cùng đối xứng đối với trục liên kết - đây là dạng phát biểu 'quy tắc chọn lọc đối xứng' của thuyết MO. |β| tỉ lệ gần đúng với S_AB. Kho Việt Nam chưa có các tích phân này.

<sub>`chemistry.dai-hoc.hoa-luong-tu.tich-phan-xen-phu` · lớp 13 · #hoa-luong-tu #xen-phu #lcao #intl-undergrad</sub>

---

**Xấp xỉ Born - Oppenheimer** — *Born - Oppenheimer approximation*

$$\Psi_{\text{toàn phần}}(\mathbf{r},\mathbf{R}) \approx \psi_{e}(\mathbf{r};\mathbf{R})\,\chi_{N}(\mathbf{R});\qquad \hat{H}_{e}\psi_{e} = E_{e}(\mathbf{R})\,\psi_{e}$$

Trong đó: `Ψ_toàn phần` là hàm sóng toàn phần của phân tử (); `ψ_e` là hàm sóng electron, phụ thuộc tham số vào toạ độ hạt nhân (); `χ_N` là hàm sóng hạt nhân (dao động - quay) (); `r` là tập toạ độ electron (m); `R` là tập toạ độ hạt nhân (m); `H_e` là toán tử Hamilton electron (hạt nhân đứng yên) (J); `E_e(R)` là năng lượng electron, đóng vai trò thế năng cho chuyển động hạt nhân (J).

*Điều kiện:* Khối lượng hạt nhân lớn hơn khối lượng electron hàng nghìn lần nên electron thích ứng tức thời với vị trí hạt nhân; xấp xỉ kém chính xác khi hai mặt thế năng gần nhau (giao cắt hình nón)

*Ghi chú:* Atkins Focus 9A, Levine ch.13. Hệ quả: khái niệm 'mặt thế năng' và 'cấu trúc hình học phân tử' chỉ có nghĩa trong khuôn khổ xấp xỉ này; cũng là nền tảng của nguyên lí Franck - Condon. Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.xap-xi-born-oppenheimer` · lớp 13 · #hoa-luong-tu #born-oppenheimer #mat-the-nang #intl-undergrad</sub>

---

**Số hạng năng lượng dao động của dao động tử điều hoà** — *Vibrational term values of a harmonic oscillator*

$$E_{v} = \left(v + \tfrac{1}{2}\right)\hbar\omega = \left(v + \tfrac{1}{2}\right)h\nu;\qquad G(v) = \left(v + \tfrac{1}{2}\right)\tilde{\nu}_{e},\quad v = 0,1,2,\dots$$

Trong đó: `E_v` là năng lượng mức dao động thứ v (J); `v` là số lượng tử dao động (); `ħ` là hằng số Planck rút gọn (J.s); `ω` là tần số góc dao động (rad/s); `h` là hằng số Planck (J.s); `ν` là tần số dao động (Hz); `G(v)` là số hạng dao động biểu diễn theo số sóng (cm^-1); `ṽ_e` là số sóng dao động điều hoà (hằng số dao động) (cm^-1).

*Điều kiện:* Thế năng parabol V = kx^2/2; các mức cách đều nhau; áp dụng cho dao động biên độ nhỏ quanh vị trí cân bằng

*Ghi chú:* Atkins Focus 7E và Focus 11C. Kho Việt Nam đã có dao động tử điều hoà lượng tử ở file vật lí đại học viết theo E_n = (n + 1/2)ħω; bản quốc tế trong hoá học bổ sung dạng số hạng G(v) tính bằng số sóng cm^-1 - đơn vị chuẩn của phổ học phân tử, và dùng chỉ số v (vibrational) thay cho n.

<sub>`chemistry.dai-hoc.hoa-luong-tu.dao-dong-tu-dieu-hoa-so-hang` · lớp 13 · #hoa-luong-tu #dao-dong #pho-hoc #intl-undergrad</sub>

---

**Khối lượng rút gọn và tần số dao động của phân tử hai nguyên tử** — *Reduced mass and vibrational frequency of a diatomic molecule*

$$\mu = \frac{m_{1}m_{2}}{m_{1}+m_{2}};\qquad \omega = \sqrt{\frac{k_{f}}{\mu}};\qquad \tilde{\nu}_{e} = \frac{1}{2\pi c}\sqrt{\frac{k_{f}}{\mu}}$$

Trong đó: `μ` là khối lượng rút gọn của phân tử hai nguyên tử (kg); `m_1` là khối lượng nguyên tử thứ nhất (kg); `m_2` là khối lượng nguyên tử thứ hai (kg); `ω` là tần số góc dao động (rad/s); `k_f` là hằng số lực của liên kết (N/m); `ṽ_e` là số sóng dao động điều hoà (cm^-1); `c` là tốc độ ánh sáng (cm/s).

*Điều kiện:* Dao động hoá trị của phân tử hai nguyên tử; khi tính ṽ_e theo cm^-1 phải lấy c theo cm/s (c = 2.99792458e10 cm/s)

*Ghi chú:* Atkins Focus 11C. Hằng số lực k_f đo độ cứng của liên kết (H-F khoảng 966 N/m, H-Cl khoảng 516 N/m). Thay đồng vị làm đổi μ nên đổi ṽ_e mà không đổi k_f - cơ sở của phép gán vạch phổ theo đồng vị. Kho Việt Nam chưa có khái niệm khối lượng rút gọn trong ngữ cảnh phổ dao động phân tử.

<sub>`chemistry.dai-hoc.hoa-luong-tu.khoi-luong-rut-gon-tan-so-dao-dong` · lớp 13 · #hoa-luong-tu #dao-dong #hang-so-luc #intl-undergrad</sub>

---

**Năng lượng điểm không của dao động phân tử** — *Zero-point vibrational energy*

$$E_{\mathrm{ZPE}} = \tfrac{1}{2}h\nu = \tfrac{1}{2}hc\,\tilde{\nu}_{e};\qquad E_{\mathrm{ZPE}}^{\text{(đa nguyên tử)}} = \tfrac{1}{2}hc\sum_{i=1}^{3N-6}\tilde{\nu}_{i}$$

Trong đó: `E_ZPE` là năng lượng điểm không (J); `h` là hằng số Planck (J.s); `ν` là tần số dao động (Hz); `c` là tốc độ ánh sáng (cm/s); `ṽ_e` là số sóng dao động điều hoà (cm^-1); `ṽ_i` là số sóng của dao động chuẩn tắc thứ i (cm^-1); `N` là số nguyên tử trong phân tử ().

*Điều kiện:* Phân tử phi tuyến có 3N - 6 dao động chuẩn tắc; phân tử thẳng có 3N - 5

*Ghi chú:* Atkins Focus 11C, 13E. Năng lượng điểm không không thể triệt tiêu (hệ quả của nguyên lí bất định) và là nguyên nhân của hiệu ứng đồng vị động học: liên kết C-D có ZPE thấp hơn C-H nên khó đứt hơn. Kho Việt Nam chưa có nội dung này.

<sub>`chemistry.dai-hoc.hoa-luong-tu.nang-luong-diem-khong-dao-dong` · lớp 13 · #hoa-luong-tu #diem-khong #dong-vi #intl-undergrad</sub>

---

**Hàm sóng chuẩn hoá của hạt trong hộp thế một chiều** — *Normalised wavefunction of a particle in a one-dimensional box*

$$\psi_{n}(x) = \sqrt{\frac{2}{L}}\,\sin\!\left(\frac{n\pi x}{L}\right),\qquad \int_{0}^{L}\psi_{n}^{2}(x)\,dx = 1$$

Trong đó: `ψ_n` là hàm sóng của trạng thái thứ n (m^-0.5); `x` là toạ độ của hạt trong hộp (m); `n` là số lượng tử tịnh tiến (); `L` là chiều dài hộp thế (m).

*Điều kiện:* 0 <= x <= L; ψ_n(0) = ψ_n(L) = 0 (điều kiện biên); hàm sóng đã chuẩn hoá

*Ghi chú:* Atkins Focus 7B. Số nút bên trong hộp bằng n - 1. Xác suất tìm thấy hạt trong khoảng [a, b] là tích phân của ψ_n^2 trên khoảng đó. Kho Việt Nam chưa có dạng hàm sóng tường minh này.

<sub>`chemistry.dai-hoc.hoa-luong-tu.hat-trong-hop-1d-ham-song` · lớp 13 · #hoa-luong-tu #ham-song #intl-undergrad</sub>

---

**Khoảng cách giữa hai mức kề nhau trong hộp thế một chiều** — *Spacing between adjacent levels of a particle in a box*

$$\Delta E = E_{n+1} - E_{n} = (2n+1)\,\frac{h^{2}}{8mL^{2}}$$

Trong đó: `ΔE` là khoảng cách hai mức năng lượng kề nhau (J); `E_n` là năng lượng mức n (J); `n` là số lượng tử của mức dưới (); `h` là hằng số Planck (J.s); `m` là khối lượng hạt (kg); `L` là chiều dài hộp (m).

*Điều kiện:* Hộp thế một chiều thành vô hạn

*Ghi chú:* Atkins Focus 7B. Khi m hoặc L lớn thì ΔE tiến tới 0: đó là giới hạn cổ điển (nguyên lí tương ứng). Dùng để giải thích vì sao chuyển động tịnh tiến của phân tử coi như liên tục còn chuyển động electron thì lượng tử hoá rõ rệt.

<sub>`chemistry.dai-hoc.hoa-luong-tu.hat-trong-hop-1d-khoang-cach-muc` · lớp 13 · #hoa-luong-tu #hat-trong-hop #intl-undergrad</sub>

---

**Mức năng lượng của hạt trong hộp thế một chiều** — *Energy levels of a particle in a one-dimensional box*

$$E_{n} = \frac{n^{2}h^{2}}{8mL^{2}} = \frac{n^{2}\pi^{2}\hbar^{2}}{2mL^{2}},\qquad n = 1,2,3,\dots$$

Trong đó: `E_n` là năng lượng của mức thứ n (J); `n` là số lượng tử tịnh tiến (số nguyên dương) (); `h` là hằng số Planck (J.s); `ħ` là hằng số Planck rút gọn h/(2π) (J.s); `m` là khối lượng hạt (kg); `L` là chiều dài hộp thế (m).

*Điều kiện:* Thành hộp cao vô hạn; V = 0 với 0 < x < L và V = vô cùng ở ngoài; n không nhận giá trị 0 (nếu n = 0 thì hàm sóng triệt tiêu khắp nơi)

*Ghi chú:* Atkins Focus 7 (Quantum theory), McQuarrie ch.3 - bài toán mở đầu của hoá lượng tử. Kho Việt Nam đã có bài toán này ở file vật lí đại học dưới tên 'giếng thế vuông góc sâu vô hạn' và viết theo ħ; ở đây dùng quy ước hoá học h^2/(8mL^2) - dạng dùng trực tiếp cho mô hình electron tự do của polyene liên hợp - kèm dạng ħ tương đương, và tách riêng khoảng cách hai mức thành bản ghi độc lập. h = 6.62607015e-34 J.s (chính xác theo SI 2019).

<sub>`chemistry.dai-hoc.hoa-luong-tu.hat-trong-hop-1d-muc-nang-luong` · lớp 13 · #hoa-luong-tu #hat-trong-hop #intl-undergrad</sub>

---

**Hạt trong hộp thế hai chiều** — *Particle in a two-dimensional box*

$$E_{n_{x},n_{y}} = \frac{h^{2}}{8m}\left(\frac{n_{x}^{2}}{L_{x}^{2}} + \frac{n_{y}^{2}}{L_{y}^{2}}\right);\qquad \psi_{n_{x},n_{y}} = \frac{2}{\sqrt{L_{x}L_{y}}}\,\sin\!\left(\frac{n_{x}\pi x}{L_{x}}\right)\sin\!\left(\frac{n_{y}\pi y}{L_{y}}\right)$$

Trong đó: `E` là năng lượng của trạng thái (n_x, n_y) (J); `ψ` là hàm sóng hai chiều (m^-1); `n_x` là số lượng tử theo phương x (); `n_y` là số lượng tử theo phương y (); `L_x` là kích thước hộp theo phương x (m); `L_y` là kích thước hộp theo phương y (m); `x` là toạ độ theo phương x (m); `y` là toạ độ theo phương y (m); `h` là hằng số Planck (J.s); `m` là khối lượng hạt (kg).

*Điều kiện:* Hộp chữ nhật thành vô hạn; nghiệm tách biến ψ(x,y) = X(x)Y(y)

*Ghi chú:* Atkins Focus 7D, McQuarrie ch.3. Khi L_x = L_y xuất hiện suy biến: các trạng thái (n_x, n_y) và (n_y, n_x) có cùng năng lượng. Đây là ví dụ chuẩn về sự suy biến do đối xứng. Kho Việt Nam chưa có nội dung này.

<sub>`chemistry.dai-hoc.hoa-luong-tu.hat-trong-hop-2d` · lớp 13 · #hoa-luong-tu #hat-trong-hop #suy-bien #intl-undergrad</sub>

---

**Hạt trong hộp thế ba chiều và bậc suy biến** — *Particle in a three-dimensional box and level degeneracy*

$$E_{n_{x},n_{y},n_{z}} = \frac{h^{2}}{8m}\left(\frac{n_{x}^{2}}{L_{x}^{2}} + \frac{n_{y}^{2}}{L_{y}^{2}} + \frac{n_{z}^{2}}{L_{z}^{2}}\right);\qquad L_{x}=L_{y}=L_{z}=L:\;\; E = \frac{h^{2}}{8mL^{2}}\left(n_{x}^{2}+n_{y}^{2}+n_{z}^{2}\right)$$

Trong đó: `E` là năng lượng của trạng thái (n_x, n_y, n_z) (J); `n_x` là số lượng tử theo phương x (); `n_y` là số lượng tử theo phương y (); `n_z` là số lượng tử theo phương z (); `L_x` là kích thước hộp theo x (m); `L_y` là kích thước hộp theo y (m); `L_z` là kích thước hộp theo z (m); `L` là cạnh của hộp lập phương (m); `h` là hằng số Planck (J.s); `m` là khối lượng hạt (kg).

*Điều kiện:* Hộp hình hộp chữ nhật thành vô hạn; với hộp lập phương thì bậc suy biến bằng số bộ (n_x, n_y, n_z) khác nhau cho cùng tổng bình phương

*Ghi chú:* Atkins Focus 7D. Ví dụ hộp lập phương: mức (1,1,2), (1,2,1), (2,1,1) suy biến bậc 3. Kết quả này là cơ sở để lập hàm phân bố tịnh tiến trong nhiệt động lực học thống kê.

<sub>`chemistry.dai-hoc.hoa-luong-tu.hat-trong-hop-3d-suy-bien` · lớp 13 · #hoa-luong-tu #hat-trong-hop #suy-bien #intl-undergrad</sub>

---

**Mô hình electron tự do cho polyene liên hợp** — *Free-electron molecular orbital (FEMO) model for a conjugated polyene*

$$\Delta E = E_{\mathrm{LUMO}} - E_{\mathrm{HOMO}} = \frac{h^{2}(N+1)}{8m_{e}L^{2}};\qquad \lambda_{\max} = \frac{8m_{e}\,c\,L^{2}}{h\,(N+1)}$$

Trong đó: `ΔE` là hiệu năng lượng HOMO - LUMO (J); `N` là số electron pi liên hợp (số chẵn) (); `L` là chiều dài hộp thế mô phỏng mạch liên hợp (m); `m_e` là khối lượng electron (kg); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng trong chân không (m/s); `λ_max` là bước sóng hấp thụ cực đại (m).

*Điều kiện:* N electron pi lấp đầy N/2 obitan thấp nhất; HOMO ứng với n = N/2, LUMO ứng với n = N/2 + 1; L thường lấy bằng số liên kết nhân độ dài liên kết trung bình, có khi cộng thêm một liên kết ở mỗi đầu

*Ghi chú:* Atkins Focus 7B (ví dụ ứng dụng), McQuarrie ch.3. Mô hình giải thích vì sao mạch liên hợp càng dài thì λ_max càng lớn (dịch chuyển đỏ) - cơ sở màu của carotenoid và thuốc nhuộm cyanine. m_e = 9.1093837139e-31 kg. Kho Việt Nam không có mô hình này.

<sub>`chemistry.dai-hoc.hoa-luong-tu.mo-hinh-electron-tu-do-polyene` · lớp 13 · #hoa-luong-tu #polyene #pho-uv-vis #intl-undergrad</sub>

---

**Hàm phân bố xuyên tâm và bán kính có xác suất lớn nhất** — *Radial distribution function and most probable radius*

$$P(r) = r^{2}R_{n\ell}^{2}(r);\qquad \int_{0}^{\infty}P(r)\,dr = 1;\qquad r_{\max}(1s) = \frac{a_{0}}{Z}$$

Trong đó: `P(r)` là hàm phân bố xuyên tâm (xác suất trên đơn vị bán kính) (m^-1); `r` là khoảng cách tới hạt nhân (m); `R_nl` là phần bán kính của hàm sóng (m^-1.5); `r_max` là bán kính ứng với xác suất lớn nhất (m); `a_0` là bán kính Bohr (m); `Z` là điện tích hạt nhân ().

*Điều kiện:* Obitan có đối xứng cầu hoặc lấy trung bình theo góc; P(r)dr là xác suất tìm thấy electron trong lớp cầu mỏng bán kính r dày dr

*Ghi chú:* Atkins Focus 8B. Với obitan 1s, mặc dù |ψ|^2 lớn nhất tại hạt nhân, P(r) lại cực đại tại r = a_0/Z do thừa số thể tích 4πr^2. Số cực đại của P(r) bằng n - l. Kho Việt Nam chưa có khái niệm này.

<sub>`chemistry.dai-hoc.hoa-luong-tu.ham-phan-bo-xuyen-tam` · lớp 13 · #hoa-luong-tu #nguyen-tu-hydro #mat-do-xac-suat #intl-undergrad</sub>

---

**Hàm sóng 1s của nguyên tử giống hydro** — *1s wavefunction of a hydrogen-like atom*

$$\psi_{1s}(r) = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_{0}}\right)^{3/2}e^{-Zr/a_{0}};\qquad \psi_{n\ell m} = R_{n\ell}(r)\,Y_{\ell}^{m}(\theta,\varphi)$$

Trong đó: `ψ_1s` là hàm sóng của obitan 1s (m^-1.5); `r` là khoảng cách từ electron tới hạt nhân (m); `Z` là điện tích hạt nhân (số proton) (); `a_0` là bán kính Bohr (m); `ψ_nlm` là hàm sóng tổng quát của obitan (n, l, m) (m^-1.5); `R_nl` là phần bán kính của hàm sóng (m^-1.5); `Y_l^m` là hàm cầu điều hoà (phần góc) (); `θ` là góc cực (rad); `φ` là góc phương vị (rad).

*Điều kiện:* Hệ một electron (H, He+, Li2+, ...); hàm sóng đã chuẩn hoá trong toạ độ cầu với yếu tố thể tích r^2 sin(θ) dr dθ dφ

*Ghi chú:* Atkins Focus 8A, Levine ch.6. a_0 = 5.29177210544e-11 m (CODATA 2022). Chỉ obitan s có ψ khác 0 tại hạt nhân - lí do sinh ra tương tác Fermi contact trong NMR và EPR. Kho Việt Nam chỉ có mức năng lượng Bohr, chưa có dạng hàm sóng tường minh.

<sub>`chemistry.dai-hoc.hoa-luong-tu.ham-song-1s-nguyen-tu-hydro` · lớp 13 · #hoa-luong-tu #nguyen-tu-hydro #ham-song #intl-undergrad</sub>

---

**Số nút của obitan nguyên tử** — *Number of nodes of an atomic orbital*

$$n_{\text{nút bán kính}} = n - \ell - 1;\qquad n_{\text{nút góc}} = \ell;\qquad n_{\text{nút tổng}} = n - 1$$

Trong đó: `n` là số lượng tử chính (); `l` là số lượng tử obitan (momen động lượng) (); `n_nút bán kính` là số mặt nút hình cầu (); `n_nút góc` là số mặt phẳng (hoặc mặt nón) nút đi qua hạt nhân (); `n_nút tổng` là tổng số mặt nút ().

*Điều kiện:* Obitan của nguyên tử một electron; 0 <= l <= n - 1

*Ghi chú:* Atkins Focus 8B, Levine ch.6. Ví dụ 3d (n = 3, l = 2): 0 nút bán kính, 2 nút góc. Số nút càng nhiều thì năng lượng obitan càng cao. Nội dung này thuộc chuẩn giáo trình quốc tế (Atkins, Levine) nhưng không có trong kho Việt Nam.

<sub>`chemistry.dai-hoc.hoa-luong-tu.so-nut-cua-obitan` · lớp 13 · #hoa-luong-tu #obitan #nut #intl-undergrad</sub>

---

**Định lí Koopmans** — *Koopmans' theorem*

$$I_{1} \approx -\varepsilon_{\mathrm{HOMO}};\qquad A_{e} \approx -\varepsilon_{\mathrm{LUMO}}$$

Trong đó: `I_1` là năng lượng ion hoá thứ nhất (J); `ε_HOMO` là năng lượng obitan bị chiếm cao nhất (J); `A_e` là ái lực electron (J); `ε_LUMO` là năng lượng obitan trống thấp nhất (J).

*Điều kiện:* Giả thiết các obitan còn lại không thay đổi khi bớt (hoặc thêm) một electron - bỏ qua hiệu ứng hồi phục và tương quan electron

*Ghi chú:* Atkins Focus 9E, Levine ch.11. Với I_1 hai sai số (hồi phục làm giảm, tương quan làm tăng) bù trừ nhau nên kết quả khá tốt; với ái lực electron thì không bù trừ nên ước lượng kém. Đây là cầu nối giữa tính toán MO và phổ quang electron (UPS/XPS). Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.dinh-li-koopmans` · lớp 13 · #hoa-luong-tu #koopmans #nang-luong-ion-hoa #intl-undergrad</sub>

---

**Định thức Slater và nguyên lí phản đối xứng** — *Slater determinant and the antisymmetry principle*

$$\Psi(1,2,\dots,N) = \frac{1}{\sqrt{N!}}\det\left|\psi_{1}(1)\;\psi_{2}(2)\;\cdots\;\psi_{N}(N)\right|;\qquad \Psi(\dots,i,\dots,j,\dots) = -\Psi(\dots,j,\dots,i,\dots)$$

Trong đó: `Ψ` là hàm sóng nhiều electron (); `N` là số electron (); `ψ_k` là obitan spin thứ k (); `i` là chỉ số electron thứ i (); `j` là chỉ số electron thứ j ().

*Điều kiện:* Electron là fermion; hàm sóng phải phản đối xứng khi hoán vị hai electron bất kì

*Ghi chú:* Atkins Focus 8B, Levine ch.10. Nếu hai obitan spin trùng nhau thì định thức có hai hàng giống nhau nên bằng 0 - đây là dạng phát biểu tổng quát và chặt chẽ của nguyên lí loại trừ Pauli. Kho Việt Nam chỉ phát biểu Pauli dưới dạng 'mỗi obitan chứa tối đa 2 electron có spin đối nhau'; định thức Slater đã có ở file vật lí đại học quốc tế (physics.dai-hoc.luong-tu-nang-cao.dinh-thuc-slater) nhưng ở đó dùng cho hệ fermion tổng quát, còn bản hoá học này gắn trực tiếp với obitan spin nguyên tử/phân tử và là tiền đề của phương pháp Hartree - Fock.

<sub>`chemistry.dai-hoc.hoa-luong-tu.dinh-thuc-slater` · lớp 13 · #hoa-luong-tu #slater #pauli #intl-undergrad</sub>

---

**Năng lượng electron toàn phần Hartree - Fock của hệ vỏ đóng** — *Total Hartree - Fock electronic energy of a closed-shell system*

$$E_{\mathrm{HF}} = 2\sum_{i}h_{ii} + \sum_{i}\sum_{j}\left(2J_{ij} - K_{ij}\right) = \sum_{i}\left(\varepsilon_{i} + h_{ii}\right) \neq 2\sum_{i}\varepsilon_{i}$$

Trong đó: `E_HF` là năng lượng electron toàn phần Hartree - Fock (J); `h_ii` là tích phân một electron của obitan i (J); `J_ij` là tích phân Coulomb (J); `K_ij` là tích phân trao đổi (J); `ε_i` là năng lượng obitan thứ i (J).

*Điều kiện:* Hệ vỏ đóng với 2 electron trên mỗi obitan không gian; tổng chạy trên các obitan bị chiếm; năng lượng toàn phần của phân tử còn phải cộng thêm lực đẩy hạt nhân

*Ghi chú:* Atkins Focus 9E, Levine ch.11. Điểm cốt lõi: tổng các năng lượng obitan KHÔNG bằng năng lượng toàn phần vì tương tác electron - electron bị tính hai lần; do đó E_HF nhỏ hơn 2 lần tổng ε_i. Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.nang-luong-tong-hartree-fock` · lớp 13 · #hoa-luong-tu #hartree-fock #nang-luong-obitan #intl-undergrad</sub>

---

**Năng lượng tương quan electron** — *Electron correlation energy*

$$E_{\mathrm{corr}} = E_{\text{chính xác}}^{\text{phi tương đối tính}} - E_{\mathrm{HF}}^{\text{giới hạn}} < 0$$

Trong đó: `E_corr` là năng lượng tương quan electron (J); `E_chính xác` là năng lượng chính xác (nghiệm đúng của phương trình Schrödinger phi tương đối tính) (J); `E_HF giới hạn` là năng lượng Hartree - Fock ở giới hạn bộ hàm cơ sở đầy đủ (J).

*Điều kiện:* Cùng hình học phân tử, cùng Hamilton phi tương đối tính; theo nguyên lí biến phân E_corr luôn âm

*Ghi chú:* Levine ch.15, Atkins Focus 9E. Tuy chỉ chiếm khoảng 1% năng lượng toàn phần nhưng E_corr có bậc độ lớn tương đương năng lượng liên kết nên bắt buộc phải tính (MP2, CI, CCSD(T), DFT). Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.nang-luong-tuong-quan-electron` · lớp 13 · #hoa-luong-tu #tuong-quan-electron #hoa-tinh-toan #intl-undergrad</sub>

---

**Phương trình Hartree - Fock và năng lượng obitan** — *Hartree - Fock equations and orbital energies*

$$\hat{F}\phi_{i} = \varepsilon_{i}\phi_{i};\qquad \hat{F} = \hat{h}^{\text{lõi}} + \sum_{j}\left(2\hat{J}_{j} - \hat{K}_{j}\right);\qquad \varepsilon_{i} = h_{ii} + \sum_{j}\left(2J_{ij} - K_{ij}\right)$$

Trong đó: `F` là toán tử Fock (J); `φ_i` là obitan không gian thứ i (); `ε_i` là năng lượng obitan thứ i (J); `h^lõi` là toán tử một electron (động năng + hút hạt nhân) (J); `J_j` là toán tử Coulomb của obitan j (J); `K_j` là toán tử trao đổi của obitan j (J); `h_ii` là tích phân một electron của obitan i (J); `J_ij` là tích phân Coulomb giữa obitan i và j (J); `K_ij` là tích phân trao đổi giữa obitan i và j (J).

*Điều kiện:* Hệ vỏ đóng (closed-shell, RHF); hàm sóng là một định thức Slater duy nhất; giải lặp tự hợp (SCF) vì F phụ thuộc chính các obitan cần tìm

*Ghi chú:* Atkins Focus 9E, Levine ch.11 và 13. Số hạng trao đổi K chỉ xuất hiện giữa các electron cùng spin - nguồn gốc lượng tử của 'năng lượng trao đổi' làm bền trạng thái spin cao (cơ sở lí thuyết của quy tắc Hund). Kho Việt Nam chưa có Hartree - Fock.

<sub>`chemistry.dai-hoc.hoa-luong-tu.phuong-trinh-hartree-fock` · lớp 13 · #hoa-luong-tu #hartree-fock #scf #intl-undergrad</sub>

---

**Phương trình thế kỉ và định thức thế kỉ** — *Secular equations and the secular determinant*

$$\sum_{j}c_{j}\left(H_{ij} - E\,S_{ij}\right) = 0 \quad \forall i;\qquad \det\left|H_{ij} - E\,S_{ij}\right| = 0$$

Trong đó: `c_j` là hệ số khai triển của hàm cơ sở thứ j (); `H_ij` là phần tử ma trận Hamilton giữa hàm cơ sở i và j (J); `S_ij` là phần tử ma trận xen phủ giữa hàm cơ sở i và j (); `E` là năng lượng obitan (nghiệm của định thức) (J).

*Điều kiện:* Khai triển tuyến tính hàm sóng thử theo bộ hàm cơ sở; nghiệm không tầm thường tồn tại khi định thức bằng 0; định thức bậc N cho N nghiệm năng lượng

*Ghi chú:* Atkins Focus 9E, Levine ch.8. Đây là bộ khung toán học chung của cả phương pháp Hückel, Hartree - Fock lẫn các phương pháp ab initio hiện đại. Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.dinh-thuc-the-ki` · lớp 13 · #hoa-luong-tu #dinh-thuc-the-ki #lcao #intl-undergrad</sub>

---

**Nguyên lí biến phân** — *Variational principle*

$$E_{\text{thử}} = \frac{\int \phi^{*}\hat{H}\phi\,d\tau}{\int \phi^{*}\phi\,d\tau} \;\geq\; E_{0}$$

Trong đó: `E_thử` là năng lượng tính từ hàm sóng thử (J); `φ` là hàm sóng thử (hàm biến phân) (); `H` là toán tử Hamilton của hệ (J); `E_0` là năng lượng chính xác của trạng thái cơ bản (J); `dτ` là yếu tố thể tích tích phân ().

*Điều kiện:* Hàm thử φ phải thoả các điều kiện biên và có thể bình phương khả tích; dấu bằng chỉ xảy ra khi φ trùng hàm sóng chính xác của trạng thái cơ bản

*Ghi chú:* Atkins Focus 9E, Levine ch.8. Là cơ sở của toàn bộ hoá học tính toán: tối ưu các tham số trong φ để cực tiểu hoá E_thử. PHÂN BIỆT với bản ghi cùng nội dung bên môn vật lí (physics.dai-hoc.luong-tu-nang-cao.phuong-phap-bien-phan): bản vật lí dùng kí hiệu Dirac với ràng buộc chuẩn hoá ⟨ψ|ψ⟩ = 1 nên tử số là trị trung bình ⟨H⟩; bản hoá học ở đây viết dưới dạng thương Rayleigh với hàm thử CHƯA chuẩn hoá (chia cho ∫φ*φ dτ) - dạng bắt buộc khi dẫn ra hệ phương trình thế kỉ của Hückel và Hartree - Fock.

<sub>`chemistry.dai-hoc.hoa-luong-tu.nguyen-li-bien-phan` · lớp 13 · #hoa-luong-tu #bien-phan #hoa-tinh-toan #intl-undergrad</sub>

---

**Momen quán tính của phân tử hai nguyên tử** — *Moment of inertia of a diatomic molecule*

$$I = \mu R^{2},\qquad \mu = \frac{m_{1}m_{2}}{m_{1}+m_{2}}$$

Trong đó: `I` là momen quán tính quanh trục đi qua khối tâm và vuông góc với trục phân tử (kg.m^2); `μ` là khối lượng rút gọn (kg); `R` là độ dài liên kết ở vị trí cân bằng (m); `m_1` là khối lượng nguyên tử thứ nhất (kg); `m_2` là khối lượng nguyên tử thứ hai (kg).

*Điều kiện:* Phân tử hai nguyên tử coi như quay tử cứng; khối lượng nguyên tử lấy theo đồng vị cụ thể (chia khối lượng mol cho N_A)

*Ghi chú:* Atkins Focus 11B. Đo hằng số quay B từ phổ vi sóng suy ra I rồi suy ra độ dài liên kết R với độ chính xác rất cao - đây là phương pháp chuẩn xác định cấu trúc phân tử ở pha khí. Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.momen-quan-tinh-phan-tu-hai-nguyen-tu` · lớp 13 · #hoa-luong-tu #momen-quan-tinh #pho-quay #intl-undergrad</sub>

---

**Mức năng lượng quay của quay tử cứng thẳng** — *Rotational energy levels of a linear rigid rotor*

$$E_{J} = \frac{\hbar^{2}}{2I}J(J+1) = hcB\,J(J+1);\qquad g_{J} = 2J+1,\quad J = 0,1,2,\dots$$

Trong đó: `E_J` là năng lượng mức quay thứ J (J); `J` là số lượng tử quay (); `ħ` là hằng số Planck rút gọn (J.s); `I` là momen quán tính của phân tử (kg.m^2); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `B` là hằng số quay biểu diễn theo số sóng (cm^-1); `g_J` là bậc suy biến của mức quay thứ J ().

*Điều kiện:* Phân tử thẳng, độ dài liên kết coi như không đổi khi quay (bỏ qua biến dạng li tâm)

*Ghi chú:* Atkins Focus 11B, McQuarrie ch.5. Bậc suy biến 2J + 1 ứng với các giá trị M_J = -J, ..., +J. Kết hợp với thừa số Boltzmann cho ra mức quay có dân số lớn nhất J_max xấp xỉ căn bậc hai của kT/(2hcB) trừ 1/2. Kho Việt Nam chưa có quay tử cứng.

<sub>`chemistry.dai-hoc.hoa-luong-tu.quay-tu-cung-muc-nang-luong` · lớp 13 · #hoa-luong-tu #quay-tu-cung #pho-quay #intl-undergrad</sub>

---

**Kí hiệu số hạng nguyên tử (term symbol)** — *Atomic term symbol*

$$^{2S+1}L_{J};\qquad S = \left|\sum_{i} m_{s}(i)\right|_{\max},\quad L = \left|\sum_{i} m_{\ell}(i)\right|_{\max},\quad J = |L-S|,\,|L-S|+1,\,\dots,\,L+S$$

Trong đó: `S` là số lượng tử spin tổng (); `L` là số lượng tử momen động lượng obitan tổng (); `J` là số lượng tử momen động lượng toàn phần (); `2S+1` là độ bội spin (multiplicity) (); `m_s(i)` là hình chiếu spin của electron thứ i (); `m_l(i)` là hình chiếu momen obitan của electron thứ i ().

*Điều kiện:* Ghép Russell - Saunders (ghép L-S), áp dụng tốt cho nguyên tử nhẹ (Z nhỏ hơn khoảng 30); các lớp đầy đóng góp L = 0, S = 0

*Ghi chú:* Atkins Focus 8C, Levine ch.11. L = 0, 1, 2, 3, 4 kí hiệu là S, P, D, F, G. Ví dụ cấu hình 2p^2 của carbon cho các số hạng 3P, 1D, 1S và trạng thái cơ bản là 3P_0. Kho Việt Nam chưa có kí hiệu số hạng nguyên tử.

<sub>`chemistry.dai-hoc.hoa-luong-tu.ki-hieu-so-hang-nguyen-tu` · lớp 13 · #hoa-luong-tu #so-hang-nguyen-tu #russell-saunders #intl-undergrad</sub>

---

**Ba quy tắc Hund xác định số hạng cơ bản** — *Hund's rules for the ground-state term*

$$\text{(1) } S_{\max}\;\Rightarrow\;\text{(2) } L_{\max}\;\Rightarrow\;\text{(3) } J = |L-S|\ (\text{lớp } <\!\tfrac{1}{2}\ \text{đầy}),\quad J = L+S\ (\text{lớp } >\!\tfrac{1}{2}\ \text{đầy})$$

Trong đó: `S` là số lượng tử spin tổng (); `L` là số lượng tử momen obitan tổng (); `J` là số lượng tử momen động lượng toàn phần ().

*Điều kiện:* Chỉ dùng để chọn số hạng CƠ BẢN trong cùng một cấu hình electron; áp dụng cho ghép Russell - Saunders

*Ghi chú:* Atkins Focus 8C, Levine ch.11. Cần phân biệt với 'quy tắc Hund' dạng phổ thông đã có trong kho Việt Nam (chemistry.thcs.cau-hinh-electron.quy-tac-hund - chỉ nói về cách điền electron vào obitan cùng phân lớp). Ba quy tắc ở đây phát biểu ở mức số hạng nguyên tử, có thêm quy tắc về L và về J. Ví dụ: Fe2+ (d^6) cho số hạng cơ bản 5D_4; Ti3+ (d^1) cho 2D_{3/2}.

<sub>`chemistry.dai-hoc.hoa-luong-tu.quy-tac-hund-so-hang-co-ban` · lớp 13 · #hoa-luong-tu #quy-tac-hund #so-hang-nguyen-tu #intl-undergrad</sub>

---

**Số vi trạng thái của một cấu hình electron** — *Number of microstates of an electron configuration*

$$N_{\text{vi trạng thái}} = \binom{2(2\ell+1)}{n_{e}} = \frac{\left[2(2\ell+1)\right]!}{n_{e}!\left[2(2\ell+1)-n_{e}\right]!}$$

Trong đó: `N_vi trạng thái` là số vi trạng thái (số cách sắp electron) (); `l` là số lượng tử obitan của phân lớp (); `n_e` là số electron trong phân lớp chưa đầy ().

*Điều kiện:* Chỉ đếm phân lớp chưa đầy; đã tính đến nguyên lí loại trừ Pauli

*Ghi chú:* Atkins Focus 8C, Levine ch.11. Ví dụ cấu hình p^2 (l = 1, n_e = 2) có C(6,2) = 15 vi trạng thái, phân thành các số hạng 3P (9), 1D (5), 1S (1). Kiểm tra tổng (2S+1)(2L+1) phải bằng số vi trạng thái. Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.so-vi-trang-thai-cau-hinh` · lớp 13 · #hoa-luong-tu #vi-trang-thai #so-hang-nguyen-tu #intl-undergrad</sub>

---

**Năng lượng tương tác spin - obitan** — *Spin-orbit coupling energy*

$$E_{\mathrm{SO}} = \tfrac{1}{2}A\left[J(J+1) - L(L+1) - S(S+1)\right];\qquad \Delta E(J\to J+1) = A\,(J+1)$$

Trong đó: `E_SO` là năng lượng tương tác spin - obitan (cm^-1); `A` là hằng số ghép spin - obitan (cm^-1); `J` là số lượng tử momen toàn phần (); `L` là số lượng tử momen obitan tổng (); `S` là số lượng tử spin tổng (); `ΔE` là khoảng cách giữa hai mức J kề nhau trong cùng số hạng (cm^-1).

*Điều kiện:* Ghép Russell - Saunders; A > 0 với lớp nhỏ hơn nửa đầy (bội thường), A < 0 với lớp lớn hơn nửa đầy (bội đảo)

*Ghi chú:* Atkins Focus 8C. Quy tắc khoảng cách Landé: ΔE tỉ lệ với (J + 1). A tăng nhanh theo Z (xấp xỉ Z^4 với nguyên tử nhẹ), giải thích vì sao vạch đôi natri (589.0 và 589.6 nm) tách rõ còn hydro thì không. Kho Việt Nam chưa có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.tuong-tac-spin-obitan` · lớp 13 · #hoa-luong-tu #spin-obitan #cau-truc-tinh-te #intl-undergrad</sub>

---

**Bậc liên kết pi theo Hückel và chỉ số hoá trị tự do** — *Hückel pi bond order and free valence index*

$$p_{rs} = \sum_{j}n_{j}\,c_{jr}c_{js};\qquad F_{r} = \sqrt{3} - \sum_{s\neq r}p_{rs}$$

Trong đó: `p_rs` là bậc liên kết pi giữa nguyên tử r và s (); `n_j` là số electron chiếm obitan phân tử j (); `c_jr` là hệ số LCAO của obitan j tại nguyên tử r (); `c_js` là hệ số LCAO của obitan j tại nguyên tử s (); `F_r` là chỉ số hoá trị tự do tại nguyên tử r (); `j` là chỉ số obitan phân tử ().

*Điều kiện:* Tổng chạy trên các obitan pi bị chiếm; hằng số căn bậc hai của 3 (khoảng 1.732) trong F_r là tổng bậc liên kết pi lớn nhất mà một nguyên tử carbon có thể đạt (nguyên tử carbon trung tâm của trimethylenemethane)

*Ghi chú:* Levine ch.16. Bậc liên kết pi tương quan chặt với độ dài liên kết thực nghiệm: benzene p = 0.667 cho mọi liên kết C-C (139 pm); butadiene p_12 = 0.894, p_23 = 0.447. F_r lớn thì vị trí đó hoạt động với gốc tự do. Kho Việt Nam có bậc liên kết MO tổng quát nhưng không có bậc liên kết pi Hückel theo hệ số LCAO.

<sub>`chemistry.dai-hoc.hoa-luong-tu.huckel-bac-lien-ket-pi` · lớp 13 · #hoa-luong-tu #huckel #bac-lien-ket #intl-undergrad</sub>

---

**Các giả thiết cơ bản của thuyết Hückel** — *Basic approximations of Hückel molecular orbital theory*

$$H_{rr} = \alpha;\quad H_{rs} = \begin{cases}\beta & r,s\ \text{kề nhau}\\ 0 & \text{khác}\end{cases};\quad S_{rs} = \delta_{rs};\qquad \det\left|H_{rs} - E\,\delta_{rs}\right| = 0$$

Trong đó: `H_rr` là phần tử đường chéo của ma trận Hamilton (nguyên tử r) (J); `H_rs` là phần tử ngoài đường chéo giữa nguyên tử r và s (J); `α` là tích phân Coulomb của nguyên tử carbon sp2 (giá trị âm) (J); `β` là tích phân cộng hưởng giữa hai nguyên tử kề nhau (giá trị âm) (J); `S_rs` là tích phân xen phủ (); `δ_rs` là kí hiệu Kronecker (); `E` là năng lượng obitan pi (J).

*Điều kiện:* Chỉ xét hệ electron pi (tách sigma - pi); mỗi nguyên tử carbon đóng góp một obitan 2p_z; bỏ qua xen phủ giữa các tâm khác nhau

*Ghi chú:* Atkins Focus 9F, Levine ch.16. Đặt x = (α - E)/β thì định thức thế kỉ chỉ còn chứa 0, 1 và x. Giá trị thực nghiệm gần đúng: β khoảng -75 kJ/mol (-0.78 eV). Kho Việt Nam không có thuyết Hückel.

<sub>`chemistry.dai-hoc.hoa-luong-tu.huckel-gia-thiet-co-ban` · lớp 13 · #hoa-luong-tu #huckel #he-pi-lien-hop #intl-undergrad</sub>

---

**Mật độ electron pi và điện tích trên nguyên tử theo Hückel** — *Hückel pi electron density and atomic charge*

$$q_{r} = \sum_{j}n_{j}\,c_{jr}^{2};\qquad Q_{r} = 1 - q_{r}$$

Trong đó: `q_r` là mật độ electron pi trên nguyên tử r (); `n_j` là số electron chiếm obitan phân tử j (0, 1 hoặc 2) (); `c_jr` là hệ số LCAO của obitan j tại nguyên tử r (); `Q_r` là điện tích pi hình thức trên nguyên tử r (); `j` là chỉ số obitan phân tử (); `r` là chỉ số nguyên tử ().

*Điều kiện:* Mỗi nguyên tử carbon sp2 đóng góp một electron pi nên mật độ tham chiếu bằng 1; tổng q_r bằng tổng số electron pi

*Ghi chú:* Levine ch.16, Atkins Focus 9F. Nguyên tử có q_r > 1 mang điện tích âm nên dễ bị tác nhân electrophile tấn công - Hückel dự đoán đúng vị trí thế của naphthalene và của các dị vòng. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.hoa-luong-tu.huckel-mat-do-electron-pi` · lớp 13 · #hoa-luong-tu #huckel #mat-do-electron #intl-undergrad</sub>

---

**Nghiệm Hückel của polyene mạch hở** — *Hückel solution for a linear polyene*

$$E_{j} = \alpha + 2\beta\cos\!\left(\frac{j\pi}{N+1}\right);\qquad c_{jr} = \sqrt{\frac{2}{N+1}}\,\sin\!\left(\frac{jr\pi}{N+1}\right),\quad j,r = 1,2,\dots,N$$

Trong đó: `E_j` là năng lượng obitan pi thứ j (J); `α` là tích phân Coulomb (J); `β` là tích phân cộng hưởng (âm) (J); `N` là số nguyên tử carbon trong mạch liên hợp thẳng (); `j` là chỉ số obitan phân tử (); `r` là chỉ số nguyên tử carbon (); `c_jr` là hệ số LCAO của obitan j tại nguyên tử r ().

*Điều kiện:* Mạch liên hợp thẳng, không phân nhánh, N nguyên tử carbon sp2; áp dụng các giả thiết Hückel

*Ghi chú:* Atkins Focus 9F, Levine ch.16. Với butadiene (N = 4): E = α ± 1.618β và α ± 0.618β. Vì β âm nên j = 1 là obitan thấp nhất. PHÂN BIỆT với chemistry.dai-hoc.icho-luong-tu.huckel-mach-ho (file olympiad) vốn chỉ cho mức năng lượng E_j: bản ghi này bổ sung công thức HỆ SỐ LCAO c_jr, thứ cần thiết để tính mật độ electron pi, bậc liên kết pi và hoá trị tự do ở các bản ghi tiếp theo.

<sub>`chemistry.dai-hoc.hoa-luong-tu.huckel-polyene-mach-ho` · lớp 13 · #hoa-luong-tu #huckel #polyene #intl-undergrad</sub>

---

**Nghiệm Hückel của hệ vòng liên hợp và giản đồ Frost** — *Hückel solution for a cyclic polyene and the Frost circle*

$$E_{j} = \alpha + 2\beta\cos\!\left(\frac{2\pi j}{N}\right),\qquad j = 0,\pm 1,\pm 2,\dots$$

Trong đó: `E_j` là năng lượng obitan pi thứ j (J); `α` là tích phân Coulomb (J); `β` là tích phân cộng hưởng (âm) (J); `N` là số nguyên tử carbon trong vòng liên hợp (); `j` là chỉ số obitan phân tử ().

*Điều kiện:* Vòng phẳng đều gồm N nguyên tử carbon sp2 liên hợp; điều kiện biên tuần hoàn

*Ghi chú:* Atkins Focus 9F. Giản đồ Frost: vẽ đa giác đều N cạnh nội tiếp đường tròn bán kính 2|β| với một đỉnh ở đáy; tung độ các đỉnh cho ngay các mức E_j. Mức j = 0 không suy biến, các mức còn lại suy biến bậc 2 (riêng j = N/2 khi N chẵn cũng không suy biến) - từ đó suy ra quy tắc 4n + 2. Benzene: E = α + 2β, α + β (x2), α - β (x2), α - 2β. Kho Việt Nam không có nghiệm Hückel cho hệ vòng ở các file chương trình trong nước.

<sub>`chemistry.dai-hoc.hoa-luong-tu.huckel-vong-frost` · lớp 13 · #hoa-luong-tu #huckel #frost #thom #intl-undergrad</sub>

---

**Năng lượng giải toả (năng lượng cộng hưởng Hückel)** — *Delocalisation (Hückel resonance) energy*

$$E_{\mathrm{deloc}} = E_{\pi}^{\text{giải toả}} - E_{\pi}^{\text{định xứ}} = E_{\pi} - N_{\text{lk}}\left(2\alpha + 2\beta\right)$$

Trong đó: `E_deloc` là năng lượng giải toả (J); `E_π` là tổng năng lượng electron pi tính theo Hückel (J); `N_lk` là số liên kết đôi định xứ trong cấu trúc tham chiếu (); `α` là tích phân Coulomb (J); `β` là tích phân cộng hưởng (âm) (J).

*Điều kiện:* Cấu trúc tham chiếu là tập các liên kết đôi ethene định xứ, mỗi liên kết đóng góp 2α + 2β

*Ghi chú:* Atkins Focus 9F, Levine ch.16. Benzene: E_π = 6α + 8β, tham chiếu 3 ethene = 6α + 6β, nên E_deloc = 2β (khoảng -150 kJ/mol). Butadiene: E_deloc = 0.472β. Cần phân biệt với 'năng lượng cộng hưởng nhiệt hoá học' của benzene (khoảng -150 kJ/mol suy từ nhiệt hidro hoá) - hai đại lượng khác định nghĩa dù trùng số. File olympiad của kho cũng có một bản ghi cùng nội dung dành cho IChO; bản ghi này giữ quy ước Atkins với cấu trúc tham chiếu viết tường minh theo số liên kết đôi định xứ và bổ sung trường hợp butadiene.

<sub>`chemistry.dai-hoc.hoa-luong-tu.nang-luong-giai-toa-pi` · lớp 13 · #hoa-luong-tu #huckel #giai-toa #intl-undergrad</sub>

---

**Quy tắc Hückel 4n + 2 về tính thơm** — *Hückel's 4n + 2 rule of aromaticity*

$$N_{\pi} = 4n + 2\ (n = 0,1,2,\dots)\;\Rightarrow\;\text{thơm};\qquad N_{\pi} = 4n\;\Rightarrow\;\text{phản thơm}$$

Trong đó: `N_π` là số electron pi giải toả trong vòng (); `n` là số nguyên không âm ().

*Điều kiện:* Vòng phải kín, phẳng và liên hợp hoàn toàn (mọi nguyên tử trong vòng có obitan p vuông góc mặt phẳng vòng); quy tắc chỉ áp dụng cho hệ đơn vòng

*Ghi chú:* Clayden ch.7, Atkins Focus 9F. Ví dụ: benzene (6 e pi, thơm), cyclobutadiene (4 e pi, phản thơm), anion cyclopentadienyl (6 e pi, thơm), cation cycloheptatrienyl (6 e pi, thơm). Đây là nội dung chuẩn của A-Level/IB nâng cao và mọi giáo trình hữu cơ quốc tế; kho Việt Nam chưa có bản ghi tường minh cho quy tắc này. PHẠM VI: A-Level chỉ dạy benzene có 6 electron pi giải toả chứ không phát biểu quy tắc 4n + 2 tổng quát, nên bản ghi này gắn intl-undergrad và olympiad.

<sub>`chemistry.dai-hoc.hoa-luong-tu.quy-tac-huckel-4n2` · lớp 13 · #hoa-luong-tu #huckel #thom #intl-undergrad #olympiad</sub>

---

### Hoá sinh vật lí

**Khai triển virial của áp suất thẩm thấu và khối lượng mol trung bình số** — *Virial expansion of the osmotic pressure and the number-average molar mass*

$$\frac{\Pi}{c} = RT\left(\frac{1}{M_{n}} + B_{2}c + \cdots\right);\qquad \bar{M}_{n} = \frac{\sum_{i}N_{i}M_{i}}{\sum_{i}N_{i}},\qquad \bar{M}_{w} = \frac{\sum_{i}N_{i}M_{i}^{2}}{\sum_{i}N_{i}M_{i}}$$

Trong đó: `Π` là áp suất thẩm thấu (Pa); `c` là nồng độ khối lượng của đại phân tử (kg/m^3); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `M_n` là khối lượng mol trung bình SỐ (kg/mol); `B_2` là hệ số virial thứ hai của áp suất thẩm thấu (m^3.mol/kg^2); `M_w` là khối lượng mol trung bình KHỐI LƯỢNG (kg/mol); `N_i` là số phân tử có khối lượng mol M_i (); `M_i` là khối lượng mol của cấu tử thứ i (kg/mol).

*Điều kiện:* Dung dịch loãng; ngoại suy Π/c về c = 0 để loại ảnh hưởng của tương tác; phép đo thẩm thấu cho M_n còn tán xạ ánh sáng cho M_w

*Ghi chú:* van Holde ch.13, Atkins Focus 14. Chỉ số phân tán M_w/M_n bằng 1 với mẫu đơn phân tán (protein tinh khiết) và lớn hơn 1 với polymer tổng hợp. B_2 > 0 nghĩa là dung môi tốt (polymer giãn), B_2 = 0 là điều kiện theta. Kho Việt Nam có áp suất thẩm thẩu Van't Hoff nhưng không có khai triển virial và các loại khối lượng mol trung bình.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.ap-suat-tham-thau-virial-polymer` · lớp 13 · #hoa-sinh-vat-li #polymer #tham-thau #intl-undergrad</sub>

---

**Nồng độ mixen tới hạn và năng lượng Gibbs tạo mixen** — *Critical micelle concentration and the Gibbs energy of micellisation*

$$\Delta G^{\circ}_{\text{mixen}} = RT\ln x_{\mathrm{CMC}}\ (\text{chất hoạt động bề mặt không ion});\qquad \Delta G^{\circ}_{\text{mixen}} = (1+\beta)RT\ln x_{\mathrm{CMC}}\ (\text{ion})$$

Trong đó: `ΔG°_mixen` là năng lượng Gibbs chuẩn của quá trình tạo mixen (trên mol chất hoạt động bề mặt) (kJ/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `x_CMC` là nồng độ mixen tới hạn biểu diễn theo phân số mol (); `β` là phần đối ion bị gắn vào mixen (0 <= β <= 1) ().

*Điều kiện:* Mô hình tách pha giả (pseudo-phase) với số tụ hợp lớn; x_CMC tính theo phân số mol (nếu dùng nồng độ mol thì phải quy đổi qua nồng độ chuẩn)

*Ghi chú:* Atkins Focus 14D. Tạo mixen là quá trình do HIỆU ỨNG KỊ NƯỚC điều khiển: ΔH gần bằng 0 hoặc dương nhẹ, còn ΔS dương lớn do nước bị 'giải phóng' khỏi cấu trúc kiểu lồng quanh đuôi hydrocarbon. lg(CMC) giảm tuyến tính theo số nguyên tử carbon của đuôi. Kho Việt Nam không có mixen định lượng.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.nong-do-mixen-toi-han` · lớp 13 · #hoa-sinh-vat-li #mixen #chat-hoat-dong-be-mat #intl-undergrad</sub>

---

**Góc elip mol trung bình theo gốc amino acid trong phổ CD** — *Mean residue ellipticity in circular dichroism*

$$\left[\theta\right]_{\mathrm{MRE}} = \frac{\theta_{\text{đo}}}{10\,l\,C\,n};\qquad \theta\,(\text{độ}) = 32.98\left(A_{L}-A_{R}\right),\quad \theta\,(\mathrm{mdeg}) = 32980\left(A_{L}-A_{R}\right)$$

Trong đó: `[θ]_MRE` là góc elip mol trung bình theo gốc amino acid (deg.cm^2/dmol); `θ_đo` là góc elip đo được (mdeg); `l` là chiều dài cuvet (cm); `C` là nồng độ mol của protein (mol/L); `n` là số gốc amino acid trong một phân tử protein (); `A_L` là độ hấp thụ ánh sáng phân cực tròn trái (); `A_R` là độ hấp thụ ánh sáng phân cực tròn phải (); `θ` là góc elip suy từ hiệu độ hấp thụ hai thành phần phân cực tròn (deg).

*Điều kiện:* Chuẩn hoá theo số gốc amino acid để so sánh được giữa các protein khác kích thước; phổ vùng xa UV (190-250 nm) phản ánh cấu trúc bậc hai. QUY ƯỚC ĐƠN VỊ: θ_đo tính bằng mdeg, l bằng cm, C bằng mol/L thì [θ]_MRE ra deg.cm^2/dmol; hệ số 32.98 chỉ đúng khi θ tính bằng ĐỘ (θ = ln10 x ΔA/4 rad = 32.98 ΔA độ), nếu lấy θ theo mdeg thì hệ số là 32980

*Ghi chú:* van Holde ch.8. Dấu hiệu chuẩn: xoắn alpha cho hai cực tiểu ở 208 và 222 nm với [θ]_MRE khoảng -33000 deg.cm^2/dmol tại 222 nm khi xoắn 100%; phiến beta cho một cực tiểu quanh 218 nm; cuộn ngẫu nhiên cho cực tiểu mạnh dưới 200 nm. Kho Việt Nam không có phổ lưỡng sắc tròn.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.goc-elip-mol-tren-goc-amino-acid` · lớp 13 · #hoa-sinh-vat-li #cd #cau-truc-bac-hai #intl-undergrad</sub>

---

**Chuẩn độ nhiệt lượng đẳng nhiệt (ITC) và bộ ba thông số nhiệt động** — *Isothermal titration calorimetry and the complete thermodynamic signature*

$$\Delta G^{\circ} = -RT\ln K_{a} = \Delta H^{\circ} - T\Delta S^{\circ};\qquad c = n\left[\mathrm{M}\right]_{0}K_{a}\ \ (5 \leq c \leq 500)$$

Trong đó: `ΔG°` là năng lượng Gibbs chuẩn của quá trình liên kết (kJ/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `K_a` là hằng số liên kết (hằng số bền) (L/mol); `ΔH°` là enthalpy liên kết chuẩn (đo trực tiếp từ nhiệt toả ra) (kJ/mol); `ΔS°` là entropy liên kết chuẩn (suy ra) (J/(mol.K)); `c` là tham số Wiseman của thí nghiệm (); `n` là số vị trí liên kết trên mỗi đại phân tử (); `[M]_0` là nồng độ đại phân tử ban đầu trong buồng đo (mol/L).

*Điều kiện:* Một thí nghiệm ITC cho đồng thời K_a, ΔH° và n; ΔS° suy ra từ ΔG° và ΔH°. Tham số Wiseman c quyết định độ cong của đường chuẩn độ: c quá nhỏ thì không xác định được K_a, c quá lớn thì đường chuẩn độ dốc đứng

*Ghi chú:* van Holde ch.13, Atkins Focus 2/3 (calorimetry). ITC là phương pháp DUY NHẤT đo trực tiếp cả enthalpy lẫn hằng số liên kết trong một thí nghiệm, không cần đánh dấu. Bù trừ enthalpy - entropy là hiện tượng phổ biến gây khó cho thiết kế thuốc. Kho Việt Nam có nhiệt lượng kế nhưng không có ITC và bộ ba thông số liên kết.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.chuan-do-nhiet-luong-dang-nhiet-itc` · lớp 13 · #hoa-sinh-vat-li #itc #lien-ket #nhiet-luong-ke #intl-undergrad</sub>

---

**Bất đẳng hướng huỳnh quang và phương trình Perrin** — *Fluorescence anisotropy and the Perrin equation*

$$r = \frac{I_{\parallel} - I_{\perp}}{I_{\parallel} + 2I_{\perp}};\qquad \frac{r_{0}}{r} = 1 + \frac{\tau}{\theta_{r}},\qquad \theta_{r} = \frac{\eta V}{k_{B}T}$$

Trong đó: `r` là bất đẳng hướng huỳnh quang đo được (); `I_∥` là cường độ huỳnh quang phân cực song song với ánh sáng kích thích (); `I_⊥` là cường độ huỳnh quang phân cực vuông góc (); `r_0` là bất đẳng hướng cơ bản (khi không có chuyển động quay) (); `τ` là thời gian sống huỳnh quang (s); `θ_r` là thời gian tương quan quay của tiểu phân (s); `η` là độ nhớt dung môi (Pa.s); `V` là thể tích thuỷ động học của tiểu phân (m^3); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Kích thích bằng ánh sáng phân cực thẳng; quay đẳng hướng (isotropic) của tiểu phân hình cầu; r_0 tối đa bằng 0.4 khi lưỡng cực hấp thụ và phát xạ song song

*Ghi chú:* Lakowicz ch.10-12, van Holde ch.11. Tiểu phân lớn quay chậm (θ_r lớn) nên giữ được bất đẳng hướng cao - nguyên lí của phép đo liên kết phối tử - protein bằng phân cực huỳnh quang (fluorescence polarisation assay) rất phổ biến trong sàng lọc thuốc. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.bat-dang-huong-huynh-quang-perrin` · lớp 13 · #hoa-sinh-vat-li #huynh-quang #perrin #intl-undergrad</sub>

---

**Hiệu suất truyền năng lượng cộng hưởng Förster (FRET)** — *Förster resonance energy transfer efficiency*

$$E = \frac{R_{0}^{6}}{R_{0}^{6} + r^{6}} = 1 - \frac{F_{DA}}{F_{D}} = 1 - \frac{\tau_{DA}}{\tau_{D}};\qquad R_{0}^{6} \propto \kappa^{2}\,n^{-4}\,\Phi_{D}\,J(\lambda)$$

Trong đó: `E` là hiệu suất truyền năng lượng (); `R_0` là bán kính Förster (khoảng cách cho E = 50%) (nm); `r` là khoảng cách giữa chất cho và chất nhận (nm); `F_DA` là cường độ huỳnh quang của chất cho khi có chất nhận (); `F_D` là cường độ huỳnh quang của chất cho khi không có chất nhận (); `τ_DA` là thời gian sống của chất cho khi có chất nhận (s); `τ_D` là thời gian sống của chất cho khi không có chất nhận (s); `κ^2` là thừa số định hướng lưỡng cực (2/3 khi định hướng ngẫu nhiên) (); `n` là chiết suất môi trường (); `Φ_D` là hiệu suất lượng tử của chất cho (); `J(λ)` là tích phân xen phủ phổ phát xạ của chất cho và phổ hấp thụ của chất nhận (L/(mol.cm.nm^4)).

*Điều kiện:* Truyền năng lượng không bức xạ qua tương tác lưỡng cực - lưỡng cực; đòi hỏi phổ phát xạ của chất cho xen phủ phổ hấp thụ của chất nhận; nhạy nhất trong khoảng 0.5R_0 đến 2R_0

*Ghi chú:* Lakowicz ch.13, van Holde ch.11. Vì E phụ thuộc r mũ 6 nên FRET là 'thước đo phân tử' cực nhạy trong dải 2-10 nm - đúng khoảng kích thước protein và tương tác protein - protein. Kho Việt Nam không có FRET.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.hieu-suat-fret` · lớp 13 · #hoa-sinh-vat-li #fret #huynh-quang #intl-undergrad</sub>

---

**Hệ số lắng và đơn vị svedberg** — *Sedimentation coefficient and the svedberg unit*

$$s = \frac{u}{\omega^{2}r} = \frac{M\left(1 - \bar{v}\rho\right)}{N_{A}f};\qquad 1\ \mathrm{S} = 10^{-13}\ \mathrm{s}$$

Trong đó: `s` là hệ số lắng (s); `u` là tốc độ lắng của tiểu phân (m/s); `ω` là tốc độ góc của rotor siêu li tâm (rad/s); `r` là khoảng cách từ trục quay tới tiểu phân (m); `M` là khối lượng mol của đại phân tử (kg/mol); `v̄` là thể tích riêng riêng phần của đại phân tử (m^3/kg); `ρ` là khối lượng riêng của dung môi (kg/m^3); `N_A` là hằng số Avogadro (mol^-1); `f` là hệ số ma sát thuỷ động học (kg/s).

*Điều kiện:* Trạng thái dừng trong trường li tâm (lực li tâm cân bằng lực ma sát và lực đẩy Archimedes); tiểu phân loãng, không tương tác

*Ghi chú:* van Holde ch.5, Atkins Focus 16C. Nếu v̄ρ > 1 thì s âm và tiểu phân NỔI thay vì lắng (cơ sở của li tâm gradient tỉ trọng CsCl). Ribosome vi khuẩn 70S gồm hai tiểu đơn vị 50S và 30S - lưu ý các hệ số svedberg KHÔNG cộng được vì phụ thuộc cả hình dạng. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.he-so-lang-svedberg` · lớp 13 · #hoa-sinh-vat-li #svedberg #sieu-li-tam #intl-undergrad</sub>

---

**Phương trình Svedberg xác định khối lượng mol** — *Svedberg equation for the molar mass*

$$M = \frac{s\,R\,T}{D\left(1 - \bar{v}\rho\right)};\qquad \frac{f}{f_{0}} = \frac{f}{6\pi\eta\left(\dfrac{3M\bar{v}}{4\pi N_{A}}\right)^{1/3}}$$

Trong đó: `M` là khối lượng mol của đại phân tử (kg/mol); `s` là hệ số lắng (s); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `D` là hệ số khuếch tán (m^2/s); `v̄` là thể tích riêng riêng phần (m^3/kg); `ρ` là khối lượng riêng của dung môi (kg/m^3); `f` là hệ số ma sát thực nghiệm (kg/s); `f_0` là hệ số ma sát của quả cầu tương đương cùng thể tích (kg/s); `η` là độ nhớt dung môi (Pa.s); `N_A` là hằng số Avogadro (mol^-1).

*Điều kiện:* Đo đồng thời s (siêu li tâm) và D (tán xạ ánh sáng động hoặc khuếch tán); phép đo KHÔNG cần giả thiết gì về hình dạng phân tử

*Ghi chú:* van Holde ch.5. Tỉ số f/f_0 (hệ số hình dạng Perrin) cho biết độ lệch khỏi hình cầu: bằng 1.0-1.2 với protein cầu, lớn hơn 1.5 với protein sợi hoặc mất trật tự. Đây là phương pháp xác định khối lượng mol tuyệt đối, không cần chất chuẩn - khác với SDS-PAGE hay lọc gel. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.phuong-trinh-svedberg-khoi-luong-mol` · lớp 13 · #hoa-sinh-vat-li #svedberg #khoi-luong-mol #intl-undergrad</sub>

---

**Độ linh động điện di của đại phân tử** — *Electrophoretic mobility of a macromolecule*

$$\mu = \frac{v}{E} = \frac{q}{f};\qquad \text{SDS-PAGE: } \lg M = a - b\,R_{f}$$

Trong đó: `μ` là độ linh động điện di (m^2/(V.s)); `v` là tốc độ di chuyển của đại phân tử (m/s); `E` là cường độ điện trường (V/m); `q` là điện tích thực của đại phân tử (C); `f` là hệ số ma sát thuỷ động học (kg/s); `M` là khối lượng mol của protein (g/mol); `R_f` là độ linh động tương đối so với chất chỉ thị đầu gel (); `a` là tung độ gốc của đường chuẩn (); `b` là hệ số góc của đường chuẩn ().

*Điều kiện:* Điện di tự do: μ = q/f. Trong SDS-PAGE, SDS gắn theo tỉ lệ khối lượng cố định (khoảng 1.4 g SDS trên 1 g protein) nên q/M gần như không đổi, và sự phân tách hoàn toàn do rây phân tử của gel

*Ghi chú:* van Holde ch.5. Điểm cần nhấn mạnh: trong điện di TỰ DO, protein cùng tỉ số q/f di chuyển như nhau bất kể khối lượng; chỉ nhờ gel làm rây mới có quan hệ tuyến tính giữa lg M và R_f. Protein rất acid, rất base hoặc glycosyl hoá cho khối lượng biểu kiến sai lệch. Kho Việt Nam có điện di ở file sinh học ở mức mô tả, không có công thức độ linh động.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.do-linh-dong-dien-di-dai-phan-tu` · lớp 13 · #hoa-sinh-vat-li #dien-di #protein #intl-undergrad</sub>

---

**Cân bằng hai trạng thái của quá trình gấp cuộn protein** — *Two-state equilibrium of protein folding*

$$K = \frac{\left[\mathrm{U}\right]}{\left[\mathrm{F}\right]} = \frac{f_{U}}{1-f_{U}};\qquad \Delta G_{U} = -RT\ln K$$

Trong đó: `K` là hằng số cân bằng của quá trình mở cuộn (); `[U]` là nồng độ dạng mở cuộn (unfolded) (mol/L); `[F]` là nồng độ dạng gấp cuộn (folded) (mol/L); `f_U` là phân số phân tử ở dạng mở cuộn (); `ΔG_U` là năng lượng Gibbs của quá trình mở cuộn (độ bền của protein) (kJ/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Mô hình hai trạng thái (không có trung gian bền); f_U tính từ tín hiệu quang phổ theo f_U = (y - y_F)/(y_U - y_F)

*Ghi chú:* van Holde ch.4. Điểm gây ngạc nhiên: ΔG_U của protein cầu điển hình chỉ khoảng 20-60 kJ/mol - tương đương vài liên kết hydro, nên protein chỉ 'bền một cách vừa đủ'. Kho Việt Nam không có nhiệt động gấp cuộn protein.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.can-bang-hai-trang-thai-gap-cuon` · lớp 13 · #hoa-sinh-vat-li #protein #gap-cuon #intl-undergrad</sub>

---

**Nhiệt độ nóng chảy và enthalpy Van't Hoff từ đường cong biến tính** — *Melting temperature and van't Hoff enthalpy from a denaturation curve*

$$T_{m}:\ f_{U} = \tfrac{1}{2},\ \Delta G_{U} = 0,\ \Delta S_{U} = \frac{\Delta H_{U}}{T_{m}};\qquad \Delta H_{vH} = 4RT_{m}^{2}\left(\frac{df_{U}}{dT}\right)_{T_{m}}$$

Trong đó: `T_m` là nhiệt độ nóng chảy (nhiệt độ chuyển tiếp) (K); `f_U` là phân số phân tử mở cuộn (); `ΔG_U` là năng lượng Gibbs mở cuộn (kJ/mol); `ΔS_U` là entropy mở cuộn (J/(mol.K)); `ΔH_U` là enthalpy mở cuộn (kJ/mol); `ΔH_vH` là enthalpy Van't Hoff (kJ/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Chuyển tiếp hai trạng thái; đo độ dốc của đường cong biến tính tại điểm giữa

*Ghi chú:* van Holde ch.4, Atkins Focus 4 (Impact on biochemistry). Tiêu chí kiểm tra mô hình hai trạng thái: tỉ số ΔH_vH/ΔH_nhiệt lượng kế (đo bằng DSC) phải bằng 1; nếu nhỏ hơn 1 thì có trung gian, nếu lớn hơn 1 thì có tương tác giữa các tiểu đơn vị. Kho Việt Nam có Tm của DNA theo thành phần GC ở file sinh học nhưng không có phân tích nhiệt động này.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.enthalpy-vant-hoff-tu-duong-cong-nong-chay` · lớp 13 · #hoa-sinh-vat-li #protein #vant-hoff #dsc #intl-undergrad</sub>

---

**Đường cong ổn định protein theo phương trình Gibbs - Helmholtz mở rộng** — *Protein stability curve from the extended Gibbs - Helmholtz equation*

$$\Delta G_{U}(T) = \Delta H_{m}\left(1 - \frac{T}{T_{m}}\right) - \Delta C_{p}\left[\left(T_{m}-T\right) + T\ln\frac{T}{T_{m}}\right]$$

Trong đó: `ΔG_U(T)` là năng lượng Gibbs mở cuộn ở nhiệt độ T (kJ/mol); `ΔH_m` là enthalpy mở cuộn tại T_m (kJ/mol); `T` là nhiệt độ tuyệt đối (K); `T_m` là nhiệt độ nóng chảy (K); `ΔC_p` là biến thiên nhiệt dung đẳng áp khi mở cuộn (kJ/(mol.K)).

*Điều kiện:* ΔC_p coi như không phụ thuộc nhiệt độ; ΔC_p của protein luôn DƯƠNG và lớn (khoảng 5-15 kJ/(mol.K)) do lộ ra bề mặt kị nước khi mở cuộn

*Ghi chú:* van Holde ch.4. Hệ quả nổi bật: vì ΔC_p lớn, đường cong ΔG_U(T) là parabol úp xuống nên protein có HAI nhiệt độ biến tính - biến tính nóng ở T cao và BIẾN TÍNH LẠNH ở T thấp (thường dưới 0 độ C). Đây là kết quả đặc trưng của hoá sinh vật lí quốc tế; kho Việt Nam không có.

<sub>`chemistry.dai-hoc.hoa-sinh-vat-li.gibbs-helmholtz-on-dinh-protein` · lớp 13 · #hoa-sinh-vat-li #protein #gibbs-helmholtz #intl-undergrad</sub>

---

### Hoá vô cơ nâng cao

**Dãy Irving - Williams** — *Irving - Williams series*

$$\mathrm{Mn^{2+}} < \mathrm{Fe^{2+}} < \mathrm{Co^{2+}} < \mathrm{Ni^{2+}} < \mathrm{Cu^{2+}} > \mathrm{Zn^{2+}}$$

Trong đó: `Mn2+` là ion Mn(II), cấu hình d5 spin cao (); `Fe2+` là ion Fe(II), d6 (); `Co2+` là ion Co(II), d7 (); `Ni2+` là ion Ni(II), d8 (); `Cu2+` là ion Cu(II), d9 (); `Zn2+` là ion Zn(II), d10 ().

*Điều kiện:* Dãy độ bền phức bát diện của ion kim loại chuyển tiếp dãy thứ nhất ở trạng thái oxi hoá +2, với hầu hết phối tử; thứ tự này gần như không phụ thuộc bản chất phối tử

*Ghi chú:* Housecroft ch.20, Miessler ch.10. Hai nguyên nhân: bán kính ion giảm dần từ Mn2+ tới Zn2+ (tăng lực hút tĩnh điện) và CFSE tăng dần; cực đại bất thường ở Cu2+ là do biến dạng Jahn - Teller làm bền thêm bốn liên kết xích đạo. Rất quan trọng trong hoá sinh vô cơ (cạnh tranh ion kim loại tại tâm protein). Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.day-irving-williams` · lớp 13 · #vo-co #irving-williams #hang-so-ben #intl-undergrad</sub>

---

**Thừa số thống kê của các hằng số bền từng nấc** — *Statistical factor for stepwise formation constants*

$$\frac{K_{n}}{K_{n+1}}\bigg|_{\text{thống kê}} = \frac{(N-n+1)(n+1)}{n\,(N-n)}$$

Trong đó: `K_n` là hằng số bền nấc thứ n (L/mol); `K_n+1` là hằng số bền nấc thứ n+1 (L/mol); `N` là tổng số vị trí phối trí tương đương của ion trung tâm (); `n` là số thứ tự của nấc ().

*Điều kiện:* Các vị trí phối trí hoàn toàn tương đương và độc lập; không tính hiệu ứng điện tích, hiệu ứng không gian hay biến dạng hình học

*Ghi chú:* Housecroft ch.7. Ý nghĩa: ngay cả khi không có tương tác gì, K_n vẫn GIẢM dần theo n chỉ vì lí do thống kê (số vị trí trống giảm, số phối tử có thể ra đi tăng). Sai lệch mạnh so với giá trị thống kê mới là dấu hiệu của hiệu ứng thực (Jahn - Teller, thay đổi spin, đổi hình học). Kho Việt Nam có β_n = k1k2...kn nhưng không có thừa số thống kê.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.hang-so-ben-tung-nac-thong-ke` · lớp 13 · #vo-co #hang-so-ben #thong-ke #intl-undergrad</sub>

---

**Hiệu ứng chelat xét theo nhiệt động lực học** — *Thermodynamic origin of the chelate effect*

$$\Delta_{r}G^{\circ} = \Delta_{r}H^{\circ} - T\Delta_{r}S^{\circ};\qquad \Delta_{r}S^{\circ} > 0\ \text{do } \Delta n_{\text{tiểu phân}} > 0 \Rightarrow \lg\beta(\text{chelat}) \gg \lg\beta(\text{đơn răng})$$

Trong đó: `Δ_rG°` là biến thiên năng lượng Gibbs chuẩn của phản ứng tạo phức (kJ/mol); `Δ_rH°` là biến thiên enthalpy chuẩn (kJ/mol); `Δ_rS°` là biến thiên entropy chuẩn (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `Δn_tiểu phân` là biến thiên số tiểu phân tự do trong dung dịch (); `β` là hằng số bền tổng ().

*Điều kiện:* So sánh phối tử đa răng với số phối tử đơn răng tương đương về mặt nguyên tử cho; hiệu ứng mạnh nhất với vòng chelat 5 hoặc 6 cạnh

*Ghi chú:* Housecroft ch.7, Miessler ch.9. Ví dụ chuẩn: [Ni(NH3)6]2+ có lgβ6 = 8.6 còn [Ni(en)3]2+ có lgβ3 = 18.3 - chênh gần 10 đơn vị log, chủ yếu do entropy vì 3 phân tử en giải phóng 6 phân tử nước (Δn = +3) trong khi 6 NH3 chỉ cho Δn = 0. Hiệu ứng macro vòng (macrocyclic effect) còn mạnh hơn nữa. Kho Việt Nam có hằng số bền nhưng không phân tích nhiệt động của hiệu ứng chelat.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.hieu-ung-chelat-nhiet-dong` · lớp 13 · #vo-co #chelat #hang-so-ben #intl-undergrad</sub>

---

**Nguyên lí acid - base cứng và mềm (HSAB)** — *Hard and Soft Acids and Bases (HSAB) principle*

$$\text{cứng}\!-\!\text{cứng}\ \text{và}\ \text{mềm}\!-\!\text{mềm}\ \text{bền hơn};\qquad \eta = \frac{I - A_{e}}{2},\qquad \chi_{\mathrm{M}} = \frac{I + A_{e}}{2}$$

Trong đó: `η` là độ cứng tuyệt đối của tiểu phân (eV); `χ_M` là độ âm điện Mulliken (thế hoá học electron lấy dấu ngược) (eV); `I` là năng lượng ion hoá thứ nhất (eV); `A_e` là ái lực electron (eV).

*Điều kiện:* Acid cứng: ion nhỏ, điện tích cao, ít bị phân cực (H+, Li+, Al3+, Fe3+, Ti4+); acid mềm: ion lớn, điện tích thấp, dễ phân cực (Ag+, Au+, Hg2+, Pd2+, Pt2+); base cứng: F-, OH-, NH3, H2O; base mềm: I-, RS-, CN-, CO, PR3

*Ghi chú:* Miessler ch.6, Housecroft ch.7. Định nghĩa định lượng η và χ do Pearson và Parr đưa ra dựa trên DFT khái niệm. Ứng dụng: giải thích vì sao Ag+ kết tủa với I- chứ không với F-, vì sao quặng sulfide chứa kim loại mềm còn quặng oxide/carbonate chứa kim loại cứng, và cơ sở của độc tính thuỷ ngân (ái lực với nhóm -SH). Kho Việt Nam không có HSAB.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.nguyen-li-hsab` · lớp 13 · #vo-co #hsab #acid-base #intl-undergrad</sub>

---

**Tổng số electron hoá trị của cluster borane theo kiểu cấu trúc** — *Total valence electron count of borane clusters by structural class*

$$\mathrm{TVE} = 4n+2\ (\mathrm{closo});\quad 4n+4\ (\mathrm{nido});\quad 4n+6\ (\mathrm{arachno});\quad 4n+8\ (\mathrm{hypho})$$

Trong đó: `TVE` là tổng số electron hoá trị của cluster (); `n` là số nguyên tử tạo khung cluster ().

*Điều kiện:* Đếm toàn bộ electron hoá trị của các nguyên tử khung cộng phối tử cộng điện tích; tương đương quy tắc Wade vì mỗi đỉnh B-H dùng 2 electron cho liên kết ngoại vi

*Ghi chú:* Housecroft ch.13. Ví dụ B6H6^2- có TVE = 6x3 + 6x1 + 2 = 26 = 4x6 + 2 nên là closo (bát diện). B5H9: 5x3 + 9 = 24 = 4x5 + 4 nên là nido. Đây là cách đếm nhanh, thay thế cho việc đếm cặp electron khung. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.dem-electron-hoa-tri-cluster-borane` · lớp 13 · #vo-co #cluster #borane #intl-undergrad</sub>

---

**Quy tắc Wade về số cặp electron khung của cluster** — *Wade's rules for skeletal electron pairs in clusters*

$$\mathrm{SEP} = n+1\ (\mathrm{closo});\quad n+2\ (\mathrm{nido});\quad n+3\ (\mathrm{arachno});\quad n+4\ (\mathrm{hypho})$$

Trong đó: `SEP` là số cặp electron khung (skeletal electron pairs) (); `n` là số đỉnh của khung cluster (số nguyên tử tạo khung) ().

*Điều kiện:* Cluster borane, carborane và cluster kim loại tuân theo quy tắc Wade - Mingos; mỗi đơn vị B-H đóng góp 2 electron khung, mỗi C-H đóng góp 3, mỗi M(CO)3 đóng góp 2

*Ghi chú:* Housecroft ch.13, Miessler ch.15. Cách dùng: đếm SEP rồi suy ra khung deltahedral n+1 đỉnh gốc; closo dùng đủ đỉnh, nido bỏ 1 đỉnh, arachno bỏ 2 đỉnh. Ví dụ B5H9 có SEP = 7 = n+2 với n = 5 nên có cấu trúc nido (kim tự tháp đáy vuông, suy từ bát diện bỏ một đỉnh). Kho Việt Nam không có thuyết cluster.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.quy-tac-wade-cluster` · lớp 13 · #vo-co #wade #cluster #borane #intl-undergrad</sub>

---

**Tương tự isolobal** — *Isolobal analogy*

$$\mathrm{CH}_{3} \longleftrightarrow \mathrm{Mn(CO)}_{5} \longleftrightarrow \mathrm{Co(CO)}_{4};\qquad \mathrm{CH}_{2} \longleftrightarrow \mathrm{Fe(CO)}_{4};\qquad \mathrm{CH} \longleftrightarrow \mathrm{Co(CO)}_{3}$$

Trong đó: `CH_3` là mảnh methyl (7 electron hoá trị, 1 obitan biên đơn chiếm) (); `Mn(CO)_5` là mảnh cơ kim 17 electron (); `Co(CO)_4` là mảnh cơ kim 17 electron (); `CH_2` là mảnh methylene (2 obitan biên đơn chiếm) (); `Fe(CO)_4` là mảnh cơ kim 16 electron (); `CH` là mảnh methylidyne (3 obitan biên đơn chiếm) (); `Co(CO)_3` là mảnh cơ kim 15 electron ().

*Điều kiện:* Hai mảnh isolobal khi có cùng SỐ LƯỢNG, ĐỐI XỨNG, NĂNG LƯỢNG GẦN NHAU và cùng số electron chiếm trên các obitan biên

*Ghi chú:* Miessler ch.15, Housecroft ch.24 (Hoffmann, Nobel Hoá học 1981). Ứng dụng: từ cyclopropane C3H6 suy ra Os3(CO)12 tồn tại; từ tetrahedrane suy ra Co4(CO)12 và các cluster hỗn hợp như HCCo3(CO)9. Cầu nối khái niệm giữa hoá hữu cơ và hoá cơ kim; kho Việt Nam không có.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.tuong-tu-isolobal` · lớp 13 · #vo-co #isolobal #cluster #intl-undergrad</sub>

---

**Hai phương pháp đếm electron: phương pháp ion và phương pháp trung hoà** — *Ionic (donor pair) and neutral (covalent) electron-counting methods*

$$\mathrm{VE}_{\text{ion}} = d^{n}\!\left(\mathrm{M}^{x+}\right) + \sum_{L}2\,(\text{phối tử cho cặp});\qquad \mathrm{VE}_{\text{trung hoà}} = n_{\text{hoá trị}}\!\left(\mathrm{M}^{0}\right) + \sum_{L}e_{L} - q$$

Trong đó: `VE_ion` là tổng số electron hoá trị đếm theo phương pháp ion (donor pair) (); `VE_trung hoà` là tổng số electron hoá trị đếm theo phương pháp trung hoà (covalent) (); `d^n` là số electron d của ion kim loại ở trạng thái oxi hoá x+ (điện tích phức đã được tính vào x) (); `n_hoá trị` là số electron hoá trị của nguyên tử kim loại TRUNG HOÀ (); `e_L` là số electron mà mỗi phối tử đóng góp (2 cho L, 1 cho X trong phương pháp trung hoà) (); `q` là điện tích tổng của phức (chỉ trừ trong phương pháp TRUNG HOÀ) (); `x` là số oxi hoá của kim loại (); `L` là chỉ số chạy trên các phối tử (); `M` là nguyên tử (M^0) hoặc ion (M^x+) kim loại trung tâm ().

*Điều kiện:* Hai phương pháp LUÔN cho cùng kết quả nếu áp dụng nhất quán. Điểm dễ sai: ở phương pháp ION KHÔNG được trừ điện tích q lần nữa vì điện tích đã nằm trong số oxi hoá x khi xác định d^n; chỉ phương pháp TRUNG HOÀ mới trừ q. Kiểm tra với [Mn(CO)6]+: ion Mn(I) là d6, cộng 6x2 = 12 cho ra 18; trung hoà Mn(0) 7 electron cộng 12 trừ 1 cũng cho 18

*Ghi chú:* Miessler ch.13, Housecroft ch.24. Kho Việt Nam có quy tắc 18 electron nhưng chỉ trình bày MỘT cách đếm; giáo trình quốc tế bắt buộc phân biệt hai phương pháp vì trạng thái oxi hoá chỉ xác định được bằng phương pháp ion, còn phương pháp trung hoà thuận tiện hơn cho phối tử hapto. Kí hiệu phổ biến ở hệ quốc tế: phối tử L (cho 2e, trung hoà) và X (cho 1e theo phương pháp trung hoà).

<sub>`chemistry.dai-hoc.vo-co-nang-cao.dem-electron-ion-va-trung-hoa` · lớp 13 · #vo-co #co-kim #dem-electron #intl-undergrad</sub>

---

**Góc nón Tolman và tham số điện tử Tolman của phối tử phosphine** — *Tolman cone angle and Tolman electronic parameter*

$$\theta\ (\text{góc nón});\qquad \mathrm{TEP} = \tilde{\nu}_{\mathrm{CO}}\left(\mathrm{A_{1}}\right)\ \text{của}\ \mathrm{Ni(CO)_{3}L}$$

Trong đó: `θ` là góc nón Tolman của phối tử (độ); `TEP` là tham số điện tử Tolman (cm^-1); `ṽ_CO` là số sóng dao động hoá trị CO (mode đối xứng A1) (cm^-1); `L` là phối tử phosphine khảo sát ().

*Điều kiện:* Góc nón đo bằng hình nón có đỉnh cách nguyên tử P 2.28 Å bao trọn các nguyên tử ngoài cùng của phối tử; TEP đo trên phức chuẩn Ni(CO)3L

*Ghi chú:* Miessler ch.13, Housecroft ch.24. Góc nón tiêu biểu: PH3 87 độ, PMe3 118 độ, PPh3 145 độ, P(t-Bu)3 182 độ, P(o-tolyl)3 194 độ. TEP càng THẤP thì phối tử càng cho electron mạnh (làm giàu mật độ trên Ni, tăng phản hồi pi vào CO, làm yếu liên kết CO). Đây là hai trục chuẩn để thiết kế phối tử trong xúc tác đồng thể; kho Việt Nam không có.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.goc-non-tolman-va-tham-so-dien-tu` · lớp 13 · #vo-co #tolman #phosphine #xuc-tac #intl-undergrad</sub>

---

**Biến thiên số electron, số oxi hoá và số phối trí trong các bước cơ bản của xúc tác cơ kim** — *Changes in electron count, oxidation state and coordination number in organometallic elementary steps*

$$\begin{array}{lccc} \text{Bước} & \Delta\mathrm{VE} & \Delta\mathrm{OS} & \Delta\mathrm{CN}\\ \hline \text{cộng oxi hoá} & +2 & +2 & +2\\ \text{tách khử} & -2 & -2 & -2\\ \text{gắn phối tử} & +2 & 0 & +1\\ \text{tách phối tử} & -2 & 0 & -1\\ \text{chèn di cư} & -2 & 0 & -1\\ \text{tách } \beta\text{-hydrua} & +2 & 0 & +1 \end{array}$$

Trong đó: `ΔVE` là biến thiên tổng số electron hoá trị (); `ΔOS` là biến thiên số oxi hoá của kim loại (); `ΔCN` là biến thiên số phối trí ().

*Điều kiện:* Áp dụng cho phức cơ kim của kim loại chuyển tiếp; chu trình xúc tác thường luân phiên giữa 16 và 18 electron

*Ghi chú:* Miessler ch.14, Housecroft ch.24. Bảng này là công cụ kiểm tra tính hợp lí của mọi chu trình xúc tác đề xuất (hydro hoá Wilkinson, hydroformyl hoá, Heck, Suzuki). Lưu ý: chèn di cư giữ nguyên số oxi hoá dù bề ngoài giống phản ứng cộng. Kho Việt Nam có quy tắc 18 electron nhưng không có bảng biến thiên này.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.thay-doi-so-electron-trong-chu-trinh-xuc-tac` · lớp 13 · #vo-co #co-kim #xuc-tac #intl-undergrad</sub>

---

**Giản đồ Tanabe - Sugano và xác định Δo, B từ phổ d-d** — *Tanabe - Sugano diagrams and determination of Delta-o and B from d-d spectra*

$$\frac{E}{B} = f\!\left(\frac{\Delta_{o}}{B}\right);\qquad \text{với } d^{3},\ d^{8}:\ \tilde{\nu}_{1} = \Delta_{o}$$

Trong đó: `E` là năng lượng của số hạng kích thích so với số hạng cơ bản (cm^-1); `B` là tham số Racah B của phức (cm^-1); `Δ_o` là năng lượng tách trường bát diện (cm^-1); `ṽ_1` là số sóng của dải hấp thụ d-d năng lượng thấp nhất (cm^-1).

*Điều kiện:* Phức bát diện của ion d^n; trục hoành và trục tung đều chuẩn hoá theo B để giản đồ dùng chung cho mọi phức cùng cấu hình d^n; đường thẳng đứng trên giản đồ d4-d7 đánh dấu điểm chuyển spin cao sang spin thấp

*Ghi chú:* Housecroft ch.20, Miessler ch.11. Quy trình chuẩn: đo tỉ số ṽ_2/ṽ_1, tra giản đồ để tìm Δ_o/B, từ đó suy ra B rồi ra Δ_o. Với d3 (Cr3+) và d8 (Ni2+) thì dải đầu tiên bằng chính Δ_o. Kho Việt Nam không có phổ phức chất định lượng.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.gian-do-tanabe-sugano` · lớp 13 · #vo-co #tanabe-sugano #pho-d-d #intl-undergrad</sub>

---

**Tham số Racah và hiệu ứng nephelauxetic** — *Racah parameters and the nephelauxetic effect*

$$\beta = \frac{B_{\text{phức}}}{B_{\text{ion tự do}}} < 1;\qquad 1 - \beta \approx h_{\text{phối tử}}\times k_{\text{ion}}$$

Trong đó: `β` là tỉ số nephelauxetic (); `B_phức` là tham số Racah B của ion kim loại trong phức (cm^-1); `B_ion tự do` là tham số Racah B của ion kim loại tự do (cm^-1); `h_phối tử` là tham số đặc trưng cho phối tử (); `k_ion` là tham số đặc trưng cho ion kim loại ().

*Điều kiện:* Tham số Racah B (và C) mô tả lực đẩy giữa các electron d; xác định từ vị trí các dải hấp thụ d-d

*Ghi chú:* Housecroft ch.20, Miessler ch.11. β < 1 nghĩa là mây electron d GIÃN RA khi tạo phức (nephelauxetic nghĩa là 'làm nở mây'), chứng tỏ liên kết kim loại - phối tử có phần cộng hoá trị - bằng chứng thực nghiệm bác bỏ mô hình trường tinh thể thuần tuý tĩnh điện. Dãy nephelauxetic (β giảm dần): F- > H2O > NH3 > en > oxalat > Cl- > CN- > Br- > I-. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.tham-so-racah-nephelauxetic` · lớp 13 · #vo-co #racah #nephelauxetic #intl-undergrad</sub>

---

**Ảnh hưởng của phối tử pi-cho và pi-nhận lên năng lượng tách trường bát diện** — *Effect of pi-donor and pi-acceptor ligands on the octahedral field splitting*

$$\Delta_{o} = E\!\left(e_{g}^{*}\right) - E\!\left(t_{2g}\right);\qquad \pi\text{-cho} \Rightarrow t_{2g}\ \text{phản liên kết},\ \Delta_{o}\ \text{giảm};\qquad \pi\text{-nhận} \Rightarrow t_{2g}\ \text{liên kết},\ \Delta_{o}\ \text{tăng}$$

Trong đó: `Δ_o` là năng lượng tách trường bát diện (cm^-1); `E(e_g^*)` là năng lượng của bộ obitan phân tử phản liên kết e_g (nguồn gốc sigma) (cm^-1); `E(t_2g)` là năng lượng của bộ obitan t_2g (không liên kết nếu phối tử chỉ cho sigma) (cm^-1); `t_2g` là bộ ba obitan phân tử d_xy, d_yz, d_zx trong trường bát diện (); `e_g^*` là bộ hai obitan phân tử phản liên kết d_(z^2), d_(x^2-y^2) (); `π` là tương tác kiểu pi giữa obitan kim loại và obitan phối tử ().

*Điều kiện:* Phức bát diện ML6 xét theo giản đồ obitan phân tử; phối tử chỉ sigma-cho (NH3, en, amine) để t_2g không liên kết; phối tử pi-cho (halogenua, OH-, O^2-, RS-) có cặp electron pi đã đầy nằm THẤP hơn t_2g; phối tử pi-nhận (CO, CN-, bpy, phen, PR3, NO+) có obitan pi* trống nằm CAO hơn t_2g

*Ghi chú:* Housecroft ch.20-21, Miessler ch.10. Đây là lời giải thích duy nhất đúng cho thứ tự dãy quang phổ hoá, thứ mà thuyết trường tinh thể tĩnh điện không cho được. Hệ quả kéo theo: phối tử pi-nhận vừa làm Δ_o lớn (dễ spin thấp) vừa làm bền trạng thái oxi hoá THẤP của kim loại (phản hồi pi từ kim loại giàu electron), là cơ sở của toàn bộ hoá học carbonyl kim loại và của tham số điện tử Tolman; phối tử pi-cho làm bền trạng thái oxi hoá CAO (MnO4-, CrO4^2-). Kho Việt Nam chỉ có thuyết trường tinh thể tĩnh điện, không có phân tích pi-cho / pi-nhận.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.anh-huong-pi-cho-pi-nhan` · lớp 13 · #truong-phoi-tu #phuc-chat #pi-nhan #intl-undergrad</sub>

---

**Dãy quang phổ hoá và hệ thức Jørgensen** — *The spectrochemical series and the Jorgensen f-g relation*

$$\mathrm{I^{-}} < \mathrm{Br^{-}} < \mathrm{Cl^{-}} < \mathrm{F^{-}} < \mathrm{OH^{-}} < \mathrm{H_{2}O} < \mathrm{NH_{3}} < \mathrm{en} < \mathrm{bpy} < \mathrm{NO_{2}^{-}} < \mathrm{CN^{-}} < \mathrm{CO};\qquad \Delta_{o} \approx f \times g$$

Trong đó: `Δ_o` là năng lượng tách trường bát diện (cm^-1); `f` là tham số đặc trưng cho phối tử (quy ước f = 1.00 cho H2O) (); `g` là tham số đặc trưng cho ion kim loại trung tâm (cm^-1).

*Điều kiện:* Dãy sắp theo Δ_o TĂNG dần và gần như không phụ thuộc bản chất ion kim loại; viết tắt phối tử: en = ethylenediamine (1,2-diaminoethane), bpy = 2,2'-bipyridine. Hệ thức tích f x g (Jørgensen) là gần đúng cho phức bát diện đồng phối tử; Δ_o còn tăng khi số oxi hoá của kim loại tăng và khi đi từ 3d xuống 4d, 5d (mỗi bậc khoảng 40-50%)

*Ghi chú:* Housecroft ch.20, Miessler ch.10. Điểm mấu chốt: thứ tự của dãy KHÔNG giải thích được bằng thuyết trường tinh thể tĩnh điện thuần tuý (I- có điện tích giống F- nhưng gây tách yếu hơn nhiều), mà phải dùng thuyết trường phối tử: phối tử pi-cho làm giảm Δ_o, phối tử chỉ sigma-cho cho Δ_o trung bình, phối tử pi-nhận làm tăng Δ_o. Kho Việt Nam có nhắc dãy này trong GHI CHÚ của bản ghi chemistry.dai-hoc.cau-tao-chat.nang-luong-tach-truong-tinh-the nhưng chưa có bản ghi riêng và chưa có hệ thức tách Δ_o thành thừa số phối tử và thừa số kim loại.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.day-quang-pho-hoa` · lớp 13 · #truong-phoi-tu #day-quang-pho-hoa #phuc-chat #intl-undergrad</sub>

---

**Định lí Jahn - Teller** — *Jahn - Teller theorem*

$$\text{Trạng thái điện tử suy biến của phân tử phi tuyến} \Rightarrow \text{biến dạng để khử suy biến};\qquad \text{mạnh khi } e_{g}\ \text{bị chiếm không đều}$$

Trong đó: `e_g` là bộ obitan e_g trong trường bát diện (); `t_2g` là bộ obitan t_2g trong trường bát diện ().

*Điều kiện:* Phân tử phi tuyến ở trạng thái điện tử suy biến (không phải suy biến Kramers do spin); biến dạng thường là kéo dài hoặc nén dọc trục z

*Ghi chú:* Housecroft ch.20, Miessler ch.10. Biến dạng MẠNH khi suy biến ở e_g (obitan hướng thẳng vào phối tử): d4 spin cao (Cr2+, Mn3+), d7 spin thấp, d9 (Cu2+). Biến dạng YẾU khi suy biến ở t_2g. Đó là lí do phức Cu(II) bát diện hầu như luôn có hai liên kết trục dài hơn bốn liên kết xích đạo. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.dinh-li-jahn-teller` · lớp 13 · #vo-co #jahn-teller #phuc-chat #intl-undergrad</sub>

---

**Năng lượng bền hoá trường tinh thể của phức tứ diện** — *Crystal field stabilisation energy of a tetrahedral complex*

$$E(e) = -0.6\Delta_{t},\quad E(t_{2}) = +0.4\Delta_{t};\qquad \mathrm{CFSE} = \left(-0.6\,n_{e} + 0.4\,n_{t_{2}}\right)\Delta_{t}$$

Trong đó: `E(e)` là năng lượng của bộ obitan e so với trọng tâm (cm^-1); `E(t2)` là năng lượng của bộ obitan t2 so với trọng tâm (cm^-1); `Δ_t` là năng lượng tách trường tứ diện (cm^-1); `n_e` là số electron trên bộ obitan e (); `n_t2` là số electron trên bộ obitan t2 (); `CFSE` là năng lượng bền hoá trường tinh thể (cm^-1).

*Điều kiện:* Phức tứ diện; thứ tự mức ĐẢO NGƯỢC so với bát diện (bộ e nằm THẤP hơn bộ t2); Δ_t = (4/9)Δ_o nên luôn nhỏ hơn năng lượng ghép đôi, do đó phức tứ diện hầu như LUÔN spin cao

*Ghi chú:* Housecroft ch.20, Miessler ch.10. Kho Việt Nam đã có CFSE bát diện và hệ thức Δ_t = (4/9)Δ_o, nhưng KHÔNG có biểu thức CFSE tứ diện với thứ tự mức đảo ngược. Hệ quả quan trọng: Co(II) d7 và Ni(II) d8 dễ tạo phức tứ diện, còn d3 và d8 spin thấp thì ưu tiên bát diện mạnh.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.cfse-tu-dien` · lớp 13 · #vo-co #truong-tinh-the #tu-dien #intl-undergrad</sub>

---

**Tiêu chuẩn spin cao - spin thấp theo năng lượng ghép đôi** — *High-spin versus low-spin criterion and the pairing energy*

$$\Delta_{o} > P \Rightarrow \text{spin thấp};\qquad \Delta_{o} < P \Rightarrow \text{spin cao};\qquad P = P_{\text{Coulomb}} + P_{\text{trao đổi}}$$

Trong đó: `Δ_o` là năng lượng tách trường bát diện (cm^-1); `P` là năng lượng ghép đôi trung bình (cm^-1); `P_Coulomb` là phần đẩy Coulomb khi hai electron cùng một obitan (cm^-1); `P_trao đổi` là phần mất năng lượng trao đổi khi giảm số electron song song (cm^-1).

*Điều kiện:* Chỉ có ý nghĩa với cấu hình d4 đến d7 trong trường bát diện (d1-d3 và d8-d10 chỉ có một cách sắp xếp)

*Ghi chú:* Housecroft ch.20, Miessler ch.10. Giá trị P của ion 3d tự do khoảng 15000-25000 cm^-1 và giảm khoảng 15-30% khi tạo phức (hiệu ứng nephelauxetic). Ion 4d và 5d có Δ_o lớn hơn 3d khoảng 50% nên hầu như luôn spin thấp. Kho Việt Nam có nêu tiêu chuẩn Δ_o so với P trong GHI CHÚ của bản ghi CFSE (chemistry.dai-hoc.cau-tao-chat.cfse) nhưng không có bản ghi riêng, và không tách P thành phần Coulomb và phần trao đổi - phần tách này mới giải thích được vì sao P giảm khi tạo phức.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.tieu-chuan-spin-cao-spin-thap` · lớp 13 · #vo-co #truong-tinh-the #spin #intl-undergrad</sub>

---

**Định luật Curie và momen từ hiệu dụng từ độ cảm từ** — *Curie law and the effective magnetic moment from magnetic susceptibility*

$$\chi_{M} = \frac{C}{T};\qquad \mu_{\mathrm{eff}} = 2.828\sqrt{\chi_{M}T}\ \ (\chi_{M}\ \text{theo cm}^{3}\mathrm{mol^{-1}},\ \mu_{\mathrm{eff}}\ \text{theo BM})$$

Trong đó: `χ_M` là độ cảm từ mol (đã hiệu chỉnh nghịch từ) (cm^3/mol); `C` là hằng số Curie (cm^3.K/mol); `T` là nhiệt độ tuyệt đối (K); `μ_eff` là momen từ hiệu dụng (BM).

*Điều kiện:* Chất thuận từ tuân theo định luật Curie (không có tương tác trao đổi giữa các tâm từ); phải hiệu chỉnh đóng góp nghịch từ của lõi và phối tử (hằng số Pascal); công thức 2.828 dùng hệ đơn vị cgs-emu truyền thống

*Ghi chú:* Housecroft ch.20. Đây là công thức LÀM VIỆC nối phép đo cân từ Gouy/Evans/SQUID với số electron độc thân. Nếu χ_M tuân theo Curie - Weiss (C/(T - θ)) thì có tương tác trao đổi giữa các tâm kim loại. Kho Việt Nam có momen từ spin thuần tuý nhưng không có cách xác định μ từ thực nghiệm.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.do-cam-tu-va-momen-tu-thuc-nghiem` · lớp 13 · #vo-co #tu-tinh #curie #intl-undergrad</sub>

---

**Momen từ hiệu dụng có đóng góp obitan** — *Effective magnetic moment including the orbital contribution*

$$\mu_{S+L} = \sqrt{4S(S+1) + L(L+1)}\ \mu_{B};\qquad \mu_{J} = g_{J}\sqrt{J(J+1)}\ \mu_{B}$$

Trong đó: `μ_S+L` là momen từ khi tính cả đóng góp spin và obitan (BM); `S` là số lượng tử spin tổng (); `L` là số lượng tử momen obitan tổng (); `μ_B` là magneton Bohr (J/T); `μ_J` là momen từ trong ghép J (BM); `g_J` là thừa số Landé (); `J` là số lượng tử momen toàn phần ().

*Điều kiện:* Công thức μ_S+L dùng khi ghép spin - obitan yếu (ion 3d); công thức μ_J dùng khi ghép mạnh (ion lantan 4f); với hầu hết ion 3d thì momen obitan bị 'dập tắt' bởi trường phối tử nên giá trị thực nghiệm gần công thức spin thuần tuý

*Ghi chú:* Housecroft ch.20, Miessler ch.10. Kho Việt Nam chỉ có momen từ SPIN THUẦN TUÝ; bản này bổ sung đóng góp obitan và trường hợp ion 4f - nơi công thức spin thuần tuý sai hoàn toàn (ví dụ Dy3+ có μ thực nghiệm khoảng 10.6 BM trong khi spin thuần tuý chỉ cho 5.9 BM). μ_B = 9.2740100657e-24 J/T.

<sub>`chemistry.dai-hoc.vo-co-nang-cao.momen-tu-hieu-dung-spin-obitan` · lớp 13 · #vo-co #tu-tinh #lantan #intl-undergrad</sub>

---

### Hóa học phân tích

**Khoảng đổi màu của chỉ thị và nguyên tắc chọn chỉ thị** — *Indicator transition range and indicator choice*

$$\mathrm{pH}_{\text{đổi màu}} = \mathrm{p}K_{\mathrm{HIn}} \pm 1;\qquad \mathrm{pT} \in \text{bước nhảy pH của đường chuẩn độ}$$

Trong đó: `pH_đổi màu` là khoảng pH mà chỉ thị đổi màu (); `pK_HIn` là -lgK_a của chỉ thị axit - bazơ (); `pT` là chỉ số chuẩn độ (pH tại đó chỉ thị đổi màu rõ nhất) ().

*Điều kiện:* Chỉ thị là axit (hoặc bazơ) yếu có màu hai dạng khác nhau; nồng độ chỉ thị rất nhỏ để không ảnh hưởng pH

*Ghi chú:* Methyl orange: 3.1 - 4.4; methyl red: 4.4 - 6.2; bromothymol blue: 6.0 - 7.6; phenolphthalein: 8.0 - 10.0. Chọn chỉ thị có pT nằm trong bước nhảy pH.

<sub>`chemistry.dai-hoc.hoa-phan-tich.chon-chi-thi-axit-bazo` · lớp 13 · #phan-tich #chi-thi #chuan-do</sub>

---

**pH tại các điểm đặc trưng khi chuẩn độ axit yếu bằng bazơ mạnh** — *Key pH values in the titration of a weak acid with a strong base*

$$\begin{cases} \text{tại nửa ĐTĐ}: \mathrm{pH} = \mathrm{p}K_{a} \\ \text{tại ĐTĐ}: \mathrm{pH} = 7 + \frac{1}{2}\mathrm{p}K_{a} + \frac{1}{2}\lg C_{muối} \\ \text{vùng đệm}: \mathrm{pH} = \mathrm{p}K_{a} + \lg\frac{V_{b}}{V_{td}-V_{b}} \end{cases}$$

Trong đó: `pH` là chỉ số hydrogen (); `pK_a` là -lgK_a của axit yếu (); `C_muối` là nồng độ muối tại điểm tương đương (mol/L); `V_b` là thể tích bazơ đã thêm (mL); `V_tđ` là thể tích bazơ tại điểm tương đương (mL).

*Điều kiện:* Axit đơn chức yếu, bazơ chuẩn mạnh; K_a không quá nhỏ (chuẩn độ được khi C.K_a > 1e-8)

*Ghi chú:* Điểm tương đương nằm trong vùng bazơ (pH > 7) nên phải dùng chỉ thị phenolphthalein, không dùng methyl orange.

<sub>`chemistry.dai-hoc.hoa-phan-tich.chuan-do-axit-yeu` · lớp 13 · #phan-tich #chuan-do #axit-yeu</sub>

---

**Đường cong chuẩn độ axit mạnh bằng bazơ mạnh** — *Titration curve of a strong acid with a strong base*

$$\text{Trước ĐTĐ: } [\mathrm{H}^{+}] = \frac{C_{a}V_{a}-C_{b}V_{b}}{V_{a}+V_{b}};\quad \text{tại ĐTĐ: } \mathrm{pH}=7;\quad \text{sau ĐTĐ: } [\mathrm{OH}^{-}] = \frac{C_{b}V_{b}-C_{a}V_{a}}{V_{a}+V_{b}}$$

Trong đó: `C_a` là nồng độ axit (mol/L); `V_a` là thể tích axit lấy chuẩn độ (mL); `C_b` là nồng độ bazơ chuẩn (mol/L); `V_b` là thể tích bazơ đã thêm (mL); `pH` là chỉ số hydrogen (); `ĐTĐ` là điểm tương đương.

*Điều kiện:* Cả axit và bazơ đều mạnh, điện li hoàn toàn; ở 25 độ C

*Ghi chú:* Với dung dịch 0.1 M, bước nhảy pH từ 4.3 đến 9.7 (sai số ±0.1%): dùng được cả methyl orange lẫn phenolphthalein. Nồng độ càng loãng thì bước nhảy càng ngắn.

<sub>`chemistry.dai-hoc.hoa-phan-tich.duong-cong-chuan-do-axit-manh` · lớp 13 · #phan-tich #chuan-do #duong-cong</sub>

---

**Chuẩn độ kết tủa (phương pháp bạc)** — *Precipitation titration (argentometry)*

$$\mathrm{pAg} = -\lg[\mathrm{Ag}^{+}];\quad \text{tại ĐTĐ: } [\mathrm{Ag}^{+}] = [\mathrm{Cl}^{-}] = \sqrt{K_{sp}} \Rightarrow \mathrm{pAg}_{td} = \frac{1}{2}\mathrm{p}K_{sp}$$

Trong đó: `pAg` là -lg nồng độ ion Ag+ (); `[Ag+]` là nồng độ ion bạc (mol/L); `[Cl-]` là nồng độ ion chloride (mol/L); `K_sp` là tích số tan của AgCl (); `pK_sp` là -lgK_sp ().

*Điều kiện:* Kết tủa ít tan, tạo thành nhanh; có cách xác định điểm cuối

*Ghi chú:* AgCl có pK_sp = 9.75 nên pAg tại điểm tương đương ≈ 4.87. Phương pháp Mohr (chỉ thị K2CrO4, pH 6.5-10), Volhard (chuẩn độ ngược bằng SCN-, chỉ thị Fe3+), Fajans (chỉ thị hấp phụ).

<sub>`chemistry.dai-hoc.hoa-phan-tich.chuan-do-ket-tua` · lớp 13 · #phan-tich #chuan-do #ket-tua</sub>

---

**Thế tại điểm tương đương của chuẩn độ oxi hóa - khử** — *Potential at the equivalence point of a redox titration*

$$E_{td} = \frac{n_{1}E_{1}^{0} + n_{2}E_{2}^{0}}{n_{1}+n_{2}}$$

Trong đó: `E_tđ` là thế tại điểm tương đương (V); `n_1` là số electron trao đổi của cặp 1 (); `n_2` là số electron trao đổi của cặp 2 (); `E_1^0` là thế chuẩn (hoặc thế chuẩn điều kiện) của cặp 1 (V); `E_2^0` là thế chuẩn của cặp 2 (V).

*Điều kiện:* Phản ứng chuẩn độ đối xứng (không có H+ hay các tiểu phân khác tham gia làm thay đổi tỉ lệ); nếu có H+ phải thêm số hạng chứa pH

*Ghi chú:* Bước nhảy thế càng lớn khi hiệu E_1^0 - E_2^0 càng lớn; cần ít nhất khoảng 0.2 - 0.4 V để chuẩn độ được. Chọn chỉ thị oxi hóa khử có E0 nằm trong bước nhảy.

<sub>`chemistry.dai-hoc.hoa-phan-tich.the-tai-diem-tuong-duong` · lớp 13 · #phan-tich #chuan-do #oxi-hoa-khu</sub>

---

**Chuẩn độ complexon với EDTA** — *Complexometric (EDTA) titration*

$$\mathrm{M}^{n+} + \mathrm{Y}^{4-} \rightarrow \mathrm{MY}^{(n-4)}:\quad n_{\mathrm{M}} = n_{\mathrm{EDTA}} \Rightarrow C_{\mathrm{M}}V_{\mathrm{M}} = C_{\mathrm{EDTA}}V_{\mathrm{EDTA}};\quad \mathrm{pM} = \lg K'_{\mathrm{MY}} + \lg\frac{C_{\mathrm{Y}}}{[\mathrm{MY}]}$$

Trong đó: `n_M` là số mol ion kim loại (mol); `n_EDTA` là số mol EDTA (mol); `C_M` là nồng độ ion kim loại (mol/L); `V_M` là thể tích dung dịch kim loại (L); `C_EDTA` là nồng độ dung dịch chuẩn EDTA (mol/L); `V_EDTA` là thể tích EDTA tiêu tốn (L); `pM` là -lg nồng độ ion kim loại tự do (); `K'_MY` là hằng số bền điều kiện; `C_Y` là tổng nồng độ EDTA dư chưa tạo phức (mol/L); `[MY]` là nồng độ phức MY (mol/L).

*Điều kiện:* Phản ứng tỉ lệ 1:1 với mọi ion kim loại bất kể điện tích; dung dịch phải được đệm pH; dùng chỉ thị kim loại (eriochrome black T, murexide); công thức pM áp dụng cho vùng sau điểm tương đương (có EDTA dư)

*Ghi chú:* Suy từ K'_MY = [MY]/([M].C_Y). Tại điểm tương đương pM = (lgK'_MY + pC_MY)/2. Chuẩn độ Ca2+, Mg2+ (độ cứng của nước) ở pH 10 với ETOO. Chuẩn độ Ca2+ riêng ở pH 12 với murexide.

<sub>`chemistry.dai-hoc.hoa-phan-tich.chuan-do-complexon` · lớp 13 · #phan-tich #chuan-do #edta</sub>

---

**Định nghĩa pH** — *Definition of pH*

$$\mathrm{pH} = -\lg a_{\mathrm{H}^{+}} \approx -\lg[\mathrm{H}^{+}];\qquad [\mathrm{H}^{+}] = 10^{-\mathrm{pH}}$$

Trong đó: `pH` là chỉ số hydrogen (); `a(H+)` là hoạt độ ion H+ (); `[H+]` là nồng độ ion H+ (mol/L).

*Điều kiện:* Định nghĩa chặt chẽ dùng hoạt độ; với dung dịch loãng (I < 0.01) có thể dùng nồng độ

*Ghi chú:* Tương tự: pOH = -lg[OH-], pK = -lgK, pM = -lg[M].

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-dinh-nghia` · lớp 13 · #phan-tich #ph #axit-bazo</sub>

---

**Quan hệ giữa Ka và Kb của cặp axit - bazơ liên hợp** — *Relation between Ka and Kb of a conjugate pair*

$$K_{a}\,K_{b} = K_{w};\qquad \mathrm{p}K_{a} + \mathrm{p}K_{b} = 14\ (25\,^{\circ}\mathrm{C})$$

Trong đó: `K_a` là hằng số axit của axit HA (mol/L); `K_b` là hằng số bazơ của bazơ liên hợp A- (mol/L); `K_w` là tích số ion của nước (); `pK_a` là -lgK_a (); `pK_b` là -lgK_b ().

*Điều kiện:* Cặp axit - bazơ liên hợp trong dung dịch nước ở 25 độ C

*Ghi chú:* Axit càng mạnh thì bazơ liên hợp càng yếu. Với axit đa chức: K_a1.K_b(n) = K_w, K_a2.K_b(n-1) = K_w...

<sub>`chemistry.dai-hoc.hoa-phan-tich.quan-he-ka-kb` · lớp 13 · #phan-tich #axit-bazo #lien-hop</sub>

---

**Tích số ion của nước** — *Ionic product of water*

$$K_{w} = [\mathrm{H}^{+}][\mathrm{OH}^{-}] = 1.0\times 10^{-14}\ (25\,^{\circ}\mathrm{C});\qquad \mathrm{pH} + \mathrm{pOH} = 14$$

Trong đó: `K_w` là tích số ion của nước (); `[H+]` là nồng độ ion hydronium (mol/L); `[OH-]` là nồng độ ion hydroxide (mol/L); `pH` là chỉ số hydrogen (); `pOH` là chỉ số hydroxide ().

*Điều kiện:* Dung dịch nước ở 25 độ C; K_w tăng theo nhiệt độ (ở 100 độ C, K_w ≈ 5.1e-13)

*Ghi chú:* pK_w = 14.00 ở 25 độ C. Sự điện li của nước là quá trình thu nhiệt nên K_w tăng khi đun nóng, do đó pH trung tính ở 60 độ C là 6.51 chứ không phải 7.

<sub>`chemistry.dai-hoc.hoa-phan-tich.tich-so-ion-cua-nuoc` · lớp 13 · #phan-tich #axit-bazo #ph</sub>

---

**Ảnh hưởng của ion chung tới độ tan** — *Common-ion effect on solubility*

$$\mathrm{AgCl}\ \text{trong}\ \mathrm{NaCl}\ C\ \mathrm{M}: \quad s = \frac{K_{sp}}{C + s} \approx \frac{K_{sp}}{C}\quad (C \gg s)$$

Trong đó: `s` là độ tan trong dung dịch có ion chung (mol/L); `K_sp` là tích số tan (); `C` là nồng độ ion chung thêm vào (mol/L).

*Điều kiện:* Nồng độ ion chung lớn hơn nhiều so với độ tan; chưa xảy ra hiệu ứng tạo phức khi dư quá nhiều

*Ghi chú:* Ion chung làm giảm độ tan. Nhưng dư quá nhiều Cl- lại làm AgCl tan trở lại do tạo phức AgCl2-. Ion lạ (hiệu ứng muối) làm tăng nhẹ độ tan do giảm hệ số hoạt độ.

<sub>`chemistry.dai-hoc.hoa-phan-tich.anh-huong-ion-chung` · lớp 13 · #phan-tich #do-tan #ion-chung</sub>

---

**Ảnh hưởng của pH tới độ tan của muối axit yếu** — *Effect of pH on the solubility of a salt of a weak acid*

$$s = \sqrt{K_{sp}\left(1 + \frac{[\mathrm{H}^{+}]}{K_{a}}\right)};\qquad K_{sp}' = \frac{K_{sp}}{\alpha_{\mathrm{A}}},\; \alpha_{\mathrm{A}} = \frac{K_{a}}{K_{a}+[\mathrm{H}^{+}]}$$

Trong đó: `s` là độ tan ở pH đang xét (mol/L); `K_sp` là tích số tan của MA (); `[H+]` là nồng độ ion H+ (mol/L); `K_a` là hằng số axit của HA (mol/L); `K_sp'` là tích số tan điều kiện; `α_A` là phần mol của dạng A- trong tổng nồng độ ().

*Điều kiện:* Muối MA của axit đơn chức yếu HA; bỏ qua thủy phân cation

*Ghi chú:* pH càng thấp thì độ tan càng lớn. Đó là lí do CaCO3, CaC2O4, các sulfide tan trong axit mạnh, còn AgCl và BaSO4 thì không.

<sub>`chemistry.dai-hoc.hoa-phan-tich.anh-huong-ph-len-do-tan` · lớp 13 · #phan-tich #do-tan #ph</sub>

---

**Ảnh hưởng của sự tạo phức tới độ tan** — *Effect of complex formation on solubility*

$$\alpha_{\mathrm{M}} = \frac{1}{1 + \beta_{1}[\mathrm{L}] + \beta_{2}[\mathrm{L}]^{2} + \cdots + \beta_{n}[\mathrm{L}]^{n}};\qquad K_{sp}' = \frac{K_{sp}}{\alpha_{\mathrm{M}}\,\alpha_{\mathrm{X}}}$$

Trong đó: `α_M` là phần mol của ion kim loại tự do (); `β_i` là hằng số bền tổng hợp của phức bậc i (); `[L]` là nồng độ phối tử tự do (mol/L); `K_sp'` là tích số tan điều kiện (); `K_sp` là tích số tan nhiệt động (); `α_X` là phần mol của anion tự do.

*Điều kiện:* Có mặt phối tử tạo phức với ion kim loại của kết tủa

*Ghi chú:* AgCl tan trong NH3 dư tạo [Ag(NH3)2]+; Al(OH)3 tan trong NaOH dư tạo [Al(OH)4]-.

<sub>`chemistry.dai-hoc.hoa-phan-tich.anh-huong-tao-phuc-len-do-tan` · lớp 13 · #phan-tich #do-tan #tao-phuc</sub>

---

**Quan hệ giữa độ tan và tích số tan** — *Relation between solubility and solubility product*

$$K_{sp} = m^{m}n^{n}\,s^{m+n} \;\Rightarrow\; s = \left(\frac{K_{sp}}{m^{m}n^{n}}\right)^{\frac{1}{m+n}}$$

Trong đó: `s` là độ tan mol của chất ít tan (mol/L); `K_sp` là tích số tan (); `m` là số cation trong công thức (); `n` là số anion trong công thức ().

*Điều kiện:* Bỏ qua thủy phân, tạo phức và ảnh hưởng của lực ion; nước tinh khiết

*Ghi chú:* AgCl (1:1): s = căn(K_sp). Ag2CrO4 (2:1): K_sp = 4s^3. Ca3(PO4)2 (3:2): K_sp = 108s^5.

<sub>`chemistry.dai-hoc.hoa-phan-tich.do-tan-tu-tich-so-tan` · lớp 13 · #phan-tich #do-tan #tich-so-tan</sub>

---

**Tích số tan** — *Solubility product*

$$\mathrm{M}_{m}\mathrm{X}_{n}(r) \rightleftharpoons m\mathrm{M}^{n+} + n\mathrm{X}^{m-}:\qquad K_{sp} = [\mathrm{M}^{n+}]^{m}[\mathrm{X}^{m-}]^{n}$$

Trong đó: `K_sp` là tích số tan (còn kí hiệu T hoặc K_s) (); `[M^n+]` là nồng độ cation lúc bão hòa (mol/L); `[X^m-]` là nồng độ anion lúc bão hòa (mol/L); `m` là hệ số tỉ lượng; `n` là hệ số tỉ lượng.

*Điều kiện:* Dung dịch bão hòa, có mặt kết tủa; hoạt độ chất rắn bằng 1

*Ghi chú:* Điều kiện kết tủa: tích ion Q > K_sp. Q < K_sp thì kết tủa tan. Q = K_sp thì bão hòa.

<sub>`chemistry.dai-hoc.hoa-phan-tich.tich-so-tan` · lớp 13 · #phan-tich #tich-so-tan #ket-tua</sub>

---

**Hằng số bền điều kiện của phức EDTA** — *Conditional formation constant*

$$K'_{\mathrm{MY}} = \alpha_{\mathrm{Y(H)}}\,\alpha_{\mathrm{M(L)}}\,K_{\mathrm{MY}};\qquad \lg K'_{\mathrm{MY}} = \lg K_{\mathrm{MY}} + \lg\alpha_{\mathrm{Y(H)}} + \lg\alpha_{\mathrm{M(L)}}$$

Trong đó: `K'_MY` là hằng số bền điều kiện của phức MY (); `K_MY` là hằng số bền nhiệt động (); `α_Y(H)` là phần mol của dạng Y(4-) trong tổng EDTA (phụ thuộc pH, luôn ≤ 1) (); `α_M(L)` là phần mol của ion kim loại tự do (phụ thuộc phối tử phụ) ().

*Điều kiện:* pH và nồng độ phối tử phụ (chất tạo phức che, đệm) xác định và không đổi

*Ghi chú:* K'_MY quyết định bước nhảy của đường chuẩn độ complexon. Muốn chuẩn độ tốt cần lgK' ít nhất 8. pH càng cao thì α_Y(H) càng gần 1.

<sub>`chemistry.dai-hoc.hoa-phan-tich.hang-so-ben-dieu-kien` · lớp 13 · #phan-tich #edta #hang-so-dieu-kien</sub>

---

**Hằng số bền và hằng số không bền của phức chất** — *Formation and dissociation constants of complexes*

$$\beta_{n} = \frac{[\mathrm{ML}_{n}]}{[\mathrm{M}][\mathrm{L}]^{n}} = k_{1}k_{2}\cdots k_{n};\qquad K_{kb} = \frac{1}{\beta_{n}}$$

Trong đó: `β_n` là hằng số bền tổng hợp của phức ML_n (); `[ML_n]` là nồng độ phức (mol/L); `[M]` là nồng độ ion kim loại tự do (mol/L); `[L]` là nồng độ phối tử tự do (mol/L); `k_i` là hằng số bền từng nấc; `K_kb` là hằng số không bền (hằng số phân li phức) ().

*Điều kiện:* Dung dịch ở cân bằng; bỏ qua hệ số hoạt độ

*Ghi chú:* β càng lớn thì phức càng bền. [Ag(NH3)2]+ có lgβ2 = 7.2; [Fe(CN)6]4- có lgβ6 ≈ 35.

<sub>`chemistry.dai-hoc.hoa-phan-tich.hang-so-ben-phuc-chat` · lớp 13 · #phan-tich #phuc-chat #hang-so-ben</sub>

---

**Dung lượng đệm** — *Buffer capacity*

$$\beta = \frac{dC_{b}}{d\mathrm{pH}} = -\frac{dC_{a}}{d\mathrm{pH}} = 2.303\,C_{T}\frac{K_{a}[\mathrm{H}^{+}]}{(K_{a}+[\mathrm{H}^{+}])^{2}};\qquad \beta_{max} = 0.576\,C_{T}$$

Trong đó: `β` là dung lượng đệm (mol/(L.pH)); `C_b` là số mol bazơ mạnh thêm vào 1 L dung dịch (mol/L); `C_a` là số mol axit mạnh thêm vào 1 L dung dịch (mol/L); `C_T` là tổng nồng độ hệ đệm (C_axit + C_bazơ) (mol/L); `K_a` là hằng số axit (mol/L); `[H+]` là nồng độ ion H+ (mol/L); `β_max` là dung lượng đệm cực đại (khi pH = pK_a) (mol/(L.pH)).

*Điều kiện:* Hệ đệm một cặp axit - bazơ liên hợp; bỏ qua đóng góp của nước

*Ghi chú:* β cực đại tại pH = pK_a với giá trị (ln10/4).C_T ≈ 0.576.C_T. Dung lượng đệm tỉ lệ thuận với tổng nồng độ hệ đệm.

<sub>`chemistry.dai-hoc.hoa-phan-tich.dung-luong-dem` · lớp 13 · #phan-tich #dung-dich-dem #dung-luong</sub>

---

**Phương trình Henderson - Hasselbalch** — *Henderson - Hasselbalch equation*

$$\mathrm{pH} = \mathrm{p}K_{a} + \lg\frac{[\mathrm{A}^{-}]}{[\mathrm{HA}]} = \mathrm{p}K_{a} + \lg\frac{C_{\text{bazơ}}}{C_{\text{axit}}}$$

Trong đó: `pH` là chỉ số hydrogen của dung dịch đệm (); `pK_a` là -lgK_a của axit yếu (); `[A-]` là nồng độ dạng bazơ liên hợp (mol/L); `[HA]` là nồng độ dạng axit (mol/L); `C_bazơ` là nồng độ đầu của muối (bazơ liên hợp) (mol/L); `C_axit` là nồng độ đầu của axit yếu (mol/L).

*Điều kiện:* Dung dịch đệm với nồng độ hai cấu tử không quá nhỏ (lớn hơn khoảng 1e-3 M) và tỉ lệ nằm trong 1:10 đến 10:1

*Ghi chú:* Đệm hiệu quả nhất khi pH = pK_a (tỉ lệ 1:1). Khoảng đệm hữu ích: pH = pK_a ± 1. Với đệm bazơ: pOH = pK_b + lg(C_axit/C_bazơ).

<sub>`chemistry.dai-hoc.hoa-phan-tich.henderson-hasselbalch` · lớp 13 · #phan-tich #dung-dich-dem #ph</sub>

---

**Định luật Lambert - Beer** — *Beer - Lambert law*

$$A = \varepsilon\,l\,C = -\lg T;\qquad T = \frac{I}{I_{0}};\qquad \%T = 100\times 10^{-A}$$

Trong đó: `A` là độ hấp thụ quang (mật độ quang) (); `ε` là hệ số hấp thụ mol (hệ số tắt phân tử) (L/(mol.cm)); `l` là bề dày lớp dung dịch (chiều dài cuvet) (cm); `C` là nồng độ chất hấp thụ (mol/L); `T` là độ truyền qua (); `I_0` là cường độ chùm sáng tới (W/m^2); `I` là cường độ chùm sáng ló (W/m^2).

*Điều kiện:* Ánh sáng đơn sắc, dung dịch loãng (C nhỏ hơn khoảng 0.01 M), chất hấp thụ không tham gia phản ứng phụ, không có tán xạ

*Ghi chú:* Sai số đo nhỏ nhất khi A nằm trong khoảng 0.2 - 0.8 (T = 15 - 65%). Nhiều chất cùng hấp thụ thì A cộng tính: A = Σε_i.l.C_i.

<sub>`chemistry.dai-hoc.hoa-phan-tich.dinh-luat-lambert-beer` · lớp 13 · #phan-tich #lambert-beer #quang-pho</sub>

---

**Định luật hợp thức trong chuẩn độ** — *Stoichiometric relation in titration*

$$\frac{C_{A}V_{A}}{a} = \frac{C_{B}V_{B}}{b};\qquad \text{theo đương lượng: } N_{A}V_{A} = N_{B}V_{B}$$

Trong đó: `C_A` là nồng độ mol chất A (mol/L); `V_A` là thể tích dung dịch A (mL); `C_B` là nồng độ mol chất chuẩn B (mol/L); `V_B` là thể tích chất chuẩn tiêu tốn (mL); `a` là hệ số tỉ lượng của A và B; `b` là hệ số tỉ lượng của A và B; `N_A` là nồng độ đương lượng của A (eq/L); `N_B` là nồng độ đương lượng của B (eq/L).

*Điều kiện:* Phản ứng chuẩn độ xảy ra hoàn toàn, nhanh, theo đúng tỉ lệ hợp thức và có cách nhận biết điểm tương đương

*Ghi chú:* Với chuẩn độ ngược (chuẩn độ dư): n_chất cần xác định = n_thuốc thử thêm vào - n_chất chuẩn dùng để chuẩn phần dư.

<sub>`chemistry.dai-hoc.hoa-phan-tich.dinh-luat-hop-thuc-chuan-do` · lớp 13 · #phan-tich #chuan-do #the-tich</sub>

---

**pH của dung dịch axit đa chức** — *pH of a polyprotic acid solution*

$$K_{a1} \gg K_{a2} \gg K_{a3} \Rightarrow [\mathrm{H}^{+}] \approx \sqrt{K_{a1}C_{a}};\qquad [\mathrm{A}^{2-}] \approx K_{a2}$$

Trong đó: `K_a1` là hằng số phân li nấc 1, 2, 3 (mol/L); `K_a2` là hằng số phân li nấc 1, 2, 3 (mol/L); `K_a3` là hằng số phân li nấc 1, 2, 3 (mol/L); `C_a` là nồng độ đầu của axit (mol/L); `[H+]` là nồng độ ion H+ (mol/L); `[A^2-]` là nồng độ anion nấc hai (mol/L).

*Điều kiện:* Các hằng số cách nhau ít nhất 1e3 - 1e4 lần nên chỉ nấc một quyết định pH

*Ghi chú:* H3PO4: pK_a1 = 2.15, pK_a2 = 7.20, pK_a3 = 12.35. H2CO3: pK_a1 = 6.35, pK_a2 = 10.33. Với H2A, nồng độ A(2-) xấp xỉ bằng K_a2 bất kể nồng độ đầu.

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-axit-da-chuc` · lớp 13 · #phan-tich #ph #axit-da-chuc</sub>

---

**pH của dung dịch axit mạnh** — *pH of a strong acid solution*

$$\mathrm{pH} = -\lg C_{a};\qquad \text{khi } C_{a} \lesssim 10^{-6}\,\mathrm{M}: [\mathrm{H}^{+}] = \frac{C_{a}+\sqrt{C_{a}^{2}+4K_{w}}}{2}$$

Trong đó: `pH` là chỉ số hydrogen (); `C_a` là nồng độ mol của axit mạnh (đã nhân số nấc) (mol/L); `K_w` là tích số ion của nước (); `[H+]` là nồng độ ion H+ (mol/L).

*Điều kiện:* Axit điện li hoàn toàn; công thức đơn giản áp dụng khi C_a lớn hơn khoảng 1e-6 M

*Ghi chú:* Với H2SO4 loãng coi như điện li hai nấc hoàn toàn: C(H+) = 2C. Không bao giờ có pH > 7 với axit dù rất loãng.

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-axit-manh` · lớp 13 · #phan-tich #ph #axit-manh</sub>

---

**pH của dung dịch axit yếu** — *pH of a weak acid solution*

$$[\mathrm{H}^{+}] = \sqrt{K_{a}C_{a}} \;\Rightarrow\; \mathrm{pH} = \frac{1}{2}\left(\mathrm{p}K_{a} - \lg C_{a}\right);\qquad \text{chính xác hơn: } [\mathrm{H}^{+}] = \frac{-K_{a}+\sqrt{K_{a}^{2}+4K_{a}C_{a}}}{2}$$

Trong đó: `[H+]` là nồng độ ion H+ (mol/L); `K_a` là hằng số phân li axit (mol/L); `C_a` là nồng độ đầu của axit yếu (mol/L); `pH` là chỉ số hydrogen (); `pK_a` là -lgK_a ().

*Điều kiện:* Công thức gần đúng dùng khi C_a/K_a > 100 (độ điện li nhỏ hơn 5%) và C_a.K_a >> K_w

*Ghi chú:* CH3COOH có pK_a = 4.76. Độ điện li α = căn(K_a/C_a) tăng khi pha loãng (định luật pha loãng Ostwald).

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-axit-yeu` · lớp 13 · #phan-tich #ph #axit-yeu</sub>

---

**pH của dung dịch bazơ mạnh** — *pH of a strong base solution*

$$\mathrm{pOH} = -\lg C_{b};\qquad \mathrm{pH} = 14 + \lg C_{b}$$

Trong đó: `pOH` là chỉ số hydroxide (); `pH` là chỉ số hydrogen (); `C_b` là nồng độ mol của bazơ mạnh (đã nhân số nhóm OH) (mol/L).

*Điều kiện:* Bazơ điện li hoàn toàn; C_b lớn hơn khoảng 1e-6 M; ở 25 độ C

*Ghi chú:* Ba(OH)2 0.01 M cho [OH-] = 0.02 M nên pH = 12.3.

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-bazo-manh` · lớp 13 · #phan-tich #ph #bazo-manh</sub>

---

**pH của dung dịch bazơ yếu** — *pH of a weak base solution*

$$[\mathrm{OH}^{-}] = \sqrt{K_{b}C_{b}} \;\Rightarrow\; \mathrm{pOH} = \frac{1}{2}\left(\mathrm{p}K_{b} - \lg C_{b}\right);\qquad \mathrm{pH} = 14 - \mathrm{pOH}$$

Trong đó: `[OH-]` là nồng độ ion OH- (mol/L); `K_b` là hằng số phân li bazơ (mol/L); `C_b` là nồng độ đầu của bazơ yếu (mol/L); `pOH` là chỉ số hydroxide (); `pH` là chỉ số hydrogen (); `pK_b` là -lgK_b ().

*Điều kiện:* C_b/K_b > 100; ở 25 độ C

*Ghi chú:* NH3 có pK_b = 4.75. Với bazơ liên hợp của axit yếu, K_b = K_w/K_a.

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-bazo-yeu` · lớp 13 · #phan-tich #ph #bazo-yeu</sub>

---

**pH của dung dịch muối axit (chất lưỡng tính)** — *pH of an amphiprotic salt solution*

$$\mathrm{pH} = \frac{\mathrm{p}K_{a1} + \mathrm{p}K_{a2}}{2};\qquad \text{tổng quát: } [\mathrm{H}^{+}] = \sqrt{\frac{K_{a1}K_{a2}C + K_{a1}K_{w}}{K_{a1}+C}}$$

Trong đó: `pH` là chỉ số hydrogen (); `pK_a1` là -lgK_a1 của axit tương ứng (); `pK_a2` là -lgK_a2 (); `C` là nồng độ muối axit (mol/L); `K_w` là tích số ion của nước ().

*Điều kiện:* Công thức đơn giản đúng khi C >> K_a1 và K_a2.C >> K_w

*Ghi chú:* Đặc điểm: pH gần như không phụ thuộc nồng độ. NaHCO3: pH = (6.35+10.33)/2 = 8.34. NaH2PO4: pH = (2.15+7.20)/2 = 4.68.

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-muoi-axit` · lớp 13 · #phan-tich #ph #luong-tinh</sub>

---

**pH của dung dịch muối tạo bởi axit yếu và bazơ yếu** — *pH of a salt of a weak acid and a weak base*

$$\mathrm{pH} = 7 + \frac{1}{2}\mathrm{p}K_{a} - \frac{1}{2}\mathrm{p}K_{b} = \frac{1}{2}\left(\mathrm{p}K_{a(\mathrm{HA})} + \mathrm{p}K_{a(\mathrm{BH}^{+})}\right)$$

Trong đó: `pH` là chỉ số hydrogen (); `pK_a` là -lgK_a của axit yếu HA (); `pK_b` là -lgK_b của bazơ yếu B (); `pK_a(BH+)` là -lgK_a của axit liên hợp BH+ ().

*Điều kiện:* Nồng độ muối không quá nhỏ; K_a và K_b không quá khác biệt so với K_w

*Ghi chú:* pH không phụ thuộc nồng độ muối. CH3COONH4 có pH ≈ 7 vì pK_a(CH3COOH) = 4.76 và pK_b(NH3) = 4.75.

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-muoi-axit-yeu-bazo-yeu` · lớp 13 · #phan-tich #ph #thuy-phan</sub>

---

**pH của dung dịch muối bị thủy phân** — *pH of a hydrolysing salt solution*

$$\begin{cases} \text{muối của axit yếu, bazơ mạnh: } \mathrm{pH} = 7 + \frac{1}{2}\mathrm{p}K_{a} + \frac{1}{2}\lg C_{s} \\ \text{muối của axit mạnh, bazơ yếu: } \mathrm{pH} = 7 - \frac{1}{2}\mathrm{p}K_{b} - \frac{1}{2}\lg C_{s} \end{cases}$$

Trong đó: `pH` là chỉ số hydrogen (); `pK_a` là -lgK_a của axit yếu tương ứng (); `pK_b` là -lgK_b của bazơ yếu tương ứng (); `C_s` là nồng độ muối (mol/L).

*Điều kiện:* Dung dịch nước 25 độ C; áp dụng gần đúng như với bazơ yếu (hoặc axit yếu) có K = K_w/K_a

*Ghi chú:* CH3COONa cho môi trường bazơ; NH4Cl cho môi trường axit; NaCl trung tính (pH = 7).

<sub>`chemistry.dai-hoc.hoa-phan-tich.ph-muoi-thuy-phan` · lớp 13 · #phan-tich #ph #thuy-phan</sub>

---

**Giá trị trung bình và độ lệch chuẩn** — *Mean and standard deviation*

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_{i};\qquad s = \sqrt{\frac{\sum_{i=1}^{n}(x_{i}-\bar{x})^{2}}{n-1}};\qquad RSD = \frac{s}{\bar{x}}\times 100\%$$

Trong đó: `x̄` là giá trị trung bình (); `x_i` là kết quả đo lần thứ i (); `n` là số lần đo (); `s` là độ lệch chuẩn của mẫu (); `RSD` là độ lệch chuẩn tương đối (hệ số biến thiên CV) (%).

*Điều kiện:* Các phép đo độc lập, chỉ chứa sai số ngẫu nhiên, phân bố chuẩn

*Ghi chú:* Mẫu số n-1 là số bậc tự do. RSD đánh giá độ lặp lại: RSD < 2% thường được coi là tốt trong phân tích thể tích.

<sub>`chemistry.dai-hoc.hoa-phan-tich.do-lech-chuan` · lớp 13 · #phan-tich #thong-ke #sai-so</sub>

---

**Khoảng tin cậy của giá trị trung bình** — *Confidence interval of the mean*

$$\mu = \bar{x} \pm \frac{t_{(P,f)}\,s}{\sqrt{n}};\qquad s_{\bar{x}} = \frac{s}{\sqrt{n}}$$

Trong đó: `μ` là giá trị thực (kì vọng) (); `x̄` là giá trị trung bình thực nghiệm (); `t_(P,f)` là hệ số Student ứng với độ tin cậy P và bậc tự do f = n-1 (); `s` là độ lệch chuẩn (); `n` là số phép đo (); `s_x̄` là sai số chuẩn của trung bình ().

*Điều kiện:* Sai số ngẫu nhiên phân bố chuẩn; đã loại bỏ sai số thô và sai số hệ thống

*Ghi chú:* Ví dụ t(95%, f=4) = 2.776; t(95%, f=9) = 2.262. Tăng số lần đo n làm khoảng tin cậy hẹp lại theo căn bậc hai của n.

<sub>`chemistry.dai-hoc.hoa-phan-tich.khoang-tin-cay` · lớp 13 · #phan-tich #thong-ke #khoang-tin-cay</sub>

---

**Kiểm định Q (Dixon) loại bỏ số liệu nghi ngờ** — *Dixon's Q test for outliers*

$$Q_{tn} = \frac{|x_{\text{nghi ngờ}} - x_{\text{lân cận}}|}{x_{max} - x_{min}};\qquad Q_{tn} > Q_{\text{bảng}} \Rightarrow \text{loại bỏ}$$

Trong đó: `Q_tn` là giá trị Q tính từ thực nghiệm (); `x_nghi ngờ` là giá trị nghi ngờ (lớn nhất hoặc nhỏ nhất); `x_lân cận` là giá trị gần với giá trị nghi ngờ nhất; `x_max` là giá trị lớn nhất trong dãy; `x_min` là giá trị nhỏ nhất trong dãy; `Q_bảng` là giá trị Q tới hạn tra bảng theo n và độ tin cậy ().

*Điều kiện:* Dãy số liệu nhỏ (n từ 3 đến 10), phân bố chuẩn; chỉ loại tối đa một giá trị

*Ghi chú:* Q(95%) với n = 3 là 0.970; n = 4 là 0.829; n = 5 là 0.710; n = 6 là 0.625; n = 7 là 0.568.

<sub>`chemistry.dai-hoc.hoa-phan-tich.kiem-dinh-q` · lớp 13 · #phan-tich #thong-ke #kiem-dinh</sub>

---

**Kiểm định t (Student) phát hiện sai số hệ thống** — *Student's t-test*

$$t_{tn} = \frac{|\bar{x}-\mu|\sqrt{n}}{s};\qquad \text{so sánh hai trung bình: } t_{tn} = \frac{|\bar{x}_{1}-\bar{x}_{2}|}{s_{p}}\sqrt{\frac{n_{1}n_{2}}{n_{1}+n_{2}}}$$

Trong đó: `t_tn` là giá trị t thực nghiệm (); `x̄` là trung bình thực nghiệm (); `μ` là giá trị thực (giá trị chứng nhận) (); `n` là số phép đo; `s` là độ lệch chuẩn (); `x̄_1` là trung bình của hai dãy số liệu; `x̄_2` là trung bình của hai dãy số liệu; `s_p` là độ lệch chuẩn gộp; `n_1` là số phép đo của hai dãy; `n_2` là số phép đo của hai dãy.

*Điều kiện:* Số liệu phân bố chuẩn; với phép so sánh hai dãy cần phương sai đồng nhất (kiểm định F trước)

*Ghi chú:* Nếu t_tn > t_bảng(P, f) thì khác biệt có ý nghĩa thống kê, tức là có sai số hệ thống. Độ lệch chuẩn gộp: s_p^2 = [(n1-1)s1^2 + (n2-1)s2^2]/(n1+n2-2).

<sub>`chemistry.dai-hoc.hoa-phan-tich.kiem-dinh-t` · lớp 13 · #phan-tich #thong-ke #kiem-dinh</sub>

---

**Giới hạn phát hiện LOD và giới hạn định lượng LOQ** — *Limit of detection and limit of quantification*

$$\mathrm{LOD} = \frac{3\,s_{b}}{b} \;(\text{hoặc } 3.3\,s_{b}/b);\qquad \mathrm{LOQ} = \frac{10\,s_{b}}{b} = \frac{10}{3}\mathrm{LOD}$$

Trong đó: `LOD` là giới hạn phát hiện (mol/L); `LOQ` là giới hạn định lượng (mol/L); `s_b` là độ lệch chuẩn của tín hiệu mẫu trắng (hoặc sai số chuẩn của tung độ gốc) (); `b` là hệ số góc của đường chuẩn (L/mol).

*Điều kiện:* Đường chuẩn tuyến tính; s_b xác định từ ít nhất 10 lần đo mẫu trắng

*Ghi chú:* LOD ứng với tỉ số tín hiệu/nhiễu S/N = 3; LOQ ứng với S/N = 10. LOQ ≈ 3.3 lần LOD.

<sub>`chemistry.dai-hoc.hoa-phan-tich.lod-loq` · lớp 13 · #phan-tich #lod #gioi-han-phat-hien</sub>

---

**Phương trình đường chuẩn (hồi quy tuyến tính)** — *Calibration curve (linear regression)*

$$y = a + bx;\qquad b = \frac{\sum(x_{i}-\bar{x})(y_{i}-\bar{y})}{\sum(x_{i}-\bar{x})^{2}};\qquad a = \bar{y} - b\bar{x};\qquad r = \frac{\sum(x_{i}-\bar{x})(y_{i}-\bar{y})}{\sqrt{\sum(x_{i}-\bar{x})^{2}\sum(y_{i}-\bar{y})^{2}}}$$

Trong đó: `y` là tín hiệu đo (độ hấp thụ, cường độ pic...) (); `x` là nồng độ chất chuẩn (mol/L); `a` là tung độ gốc (); `b` là hệ số góc (độ nhạy của phương pháp) (L/mol); `x̄` là trung bình các nồng độ chuẩn; `ȳ` là trung bình các tín hiệu; `r` là hệ số tương quan ().

*Điều kiện:* Quan hệ tuyến tính trong khoảng nồng độ khảo sát; sai số chủ yếu ở y, x coi như chính xác

*Ghi chú:* Yêu cầu thông thường: r lớn hơn 0.995 (hoặc R^2 > 0.99). Nồng độ mẫu: x = (y - a)/b. Phương pháp thêm chuẩn dùng khi có ảnh hưởng nền mẫu.

<sub>`chemistry.dai-hoc.hoa-phan-tich.phuong-trinh-duong-chuan` · lớp 13 · #phan-tich #duong-chuan #hoi-quy</sub>

---

**Sai số tuyệt đối, sai số tương đối và độ thu hồi** — *Absolute error, relative error and recovery*

$$\Delta = \bar{x} - \mu;\qquad \delta\% = \frac{\bar{x}-\mu}{\mu}\times 100;\qquad R\% = \frac{C_{\text{tìm thấy}}}{C_{\text{thêm vào}}}\times 100$$

Trong đó: `Δ` là sai số tuyệt đối (); `x̄` là giá trị đo được (trung bình); `μ` là giá trị thực; `δ%` là sai số tương đối (%); `R%` là độ thu hồi (%); `C_tìm thấy` là nồng độ xác định được; `C_thêm vào` là nồng độ chuẩn đã thêm.

*Điều kiện:* Cần biết giá trị thực (mẫu chuẩn được chứng nhận) hoặc dùng phương pháp thêm chuẩn

*Ghi chú:* Sai số tương đối đánh giá độ đúng (accuracy); độ lệch chuẩn đánh giá độ chụm (precision). Độ thu hồi chấp nhận được thường trong khoảng 95 - 105%.

<sub>`chemistry.dai-hoc.hoa-phan-tich.sai-so-tuong-doi` · lớp 13 · #phan-tich #sai-so #do-thu-hoi</sub>

---

### Hóa keo và hóa học bề mặt

**Phương trình Kelvin** — *Kelvin equation*

$$\ln\frac{p_{r}}{p_{0}} = \frac{2\sigma V_{m}}{rRT}$$

Trong đó: `p_r` là áp suất hơi bão hòa trên mặt cong bán kính r (Pa); `p_0` là áp suất hơi bão hòa trên mặt phẳng (Pa); `σ` là sức căng bề mặt (N/m); `V_m` là thể tích mol của chất lỏng (m^3/mol); `r` là bán kính cong (dương với giọt lồi, âm với mặt lõm) (m); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Giọt lỏng hoặc mao quản có bán kính rất nhỏ (cỡ nanomet đến micromet)

*Ghi chú:* Giải thích hiện tượng chậm ngưng tụ, chậm sôi, ngưng tụ mao quản trong vật liệu xốp và sự lớn lên của tinh thể lớn nhờ tinh thể nhỏ tan (chín Ostwald).

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.phuong-trinh-kelvin` · lớp 13 · #hoa-keo #kelvin #ap-suat-hoi</sub>

---

**Đẳng nhiệt hấp phụ Freundlich** — *Freundlich adsorption isotherm*

$$\frac{x}{m} = k\,C^{1/n};\qquad \lg\frac{x}{m} = \lg k + \frac{1}{n}\lg C$$

Trong đó: `x/m` là lượng chất bị hấp phụ trên một đơn vị khối lượng chất hấp phụ (mol/g); `k` là hằng số Freundlich (đặc trưng dung lượng hấp phụ) (); `C` là nồng độ (hoặc áp suất) cân bằng của chất bị hấp phụ (mol/L); `n` là hằng số đặc trưng cường độ hấp phụ (thường n > 1) ().

*Điều kiện:* Công thức thực nghiệm, phù hợp ở vùng áp suất (nồng độ) trung bình, bề mặt không đồng nhất

*Ghi chú:* Đồ thị lg(x/m) theo lgC là đường thẳng: hệ số góc 1/n, tung độ gốc lgk. Không mô tả được vùng bão hòa như Langmuir.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.dang-nhiet-freundlich` · lớp 13 · #hoa-keo #hap-phu #freundlich</sub>

---

**Đẳng nhiệt hấp phụ Langmuir** — *Langmuir adsorption isotherm*

$$\theta = \frac{bp}{1+bp};\qquad a = a_{max}\frac{bC}{1+bC};\qquad \frac{p}{a} = \frac{1}{a_{max}b} + \frac{p}{a_{max}}$$

Trong đó: `θ` là độ che phủ bề mặt (phần bề mặt bị chiếm) (); `b` là hằng số hấp phụ (liên hệ với nhiệt hấp phụ) (Pa^-1); `p` là áp suất chất bị hấp phụ (Pa); `a` là lượng chất bị hấp phụ (mol/g); `a_max` là dung lượng hấp phụ cực đại (đơn lớp) (mol/g); `C` là nồng độ chất bị hấp phụ trong dung dịch (mol/L).

*Điều kiện:* Hấp phụ đơn lớp, bề mặt đồng nhất, các tâm hấp phụ tương đương và độc lập, không tương tác giữa các phân tử bị hấp phụ

*Ghi chú:* Áp suất thấp: a tỉ lệ thuận với p (bậc một). Áp suất cao: a bão hòa bằng a_max (bậc không). Dạng tuyến tính p/a theo p cho phép xác định a_max và b.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.dang-nhiet-langmuir` · lớp 13 · #hoa-keo #hap-phu #langmuir</sub>

---

**Phương trình hấp phụ BET** — *BET adsorption equation*

$$\frac{p}{V(p_{0}-p)} = \frac{1}{V_{m}C} + \frac{C-1}{V_{m}C}\cdot\frac{p}{p_{0}};\qquad S = \frac{V_{m}N_{A}\,\omega}{V_{0}}$$

Trong đó: `p` là áp suất cân bằng của khí (Pa); `p_0` là áp suất hơi bão hòa của khí ở nhiệt độ đo (Pa); `V` là thể tích khí bị hấp phụ trên 1 g chất hấp phụ (quy về điều kiện tiêu chuẩn) (cm^3/g); `V_m` là thể tích khí ứng với một lớp đơn phân tử trên 1 g chất hấp phụ (cm^3/g); `C` là hằng số BET (liên hệ nhiệt hấp phụ lớp một và nhiệt ngưng tụ) (); `S` là diện tích bề mặt riêng (m^2/g); `N_A` là số Avogadro (mol^-1); `ω` là tiết diện ngang của một phân tử bị hấp phụ (m^2); `V_0` là thể tích mol khí ở điều kiện tiêu chuẩn (22414 cm^3/mol) (cm^3/mol).

*Điều kiện:* Hấp phụ đa lớp; áp dụng trong khoảng p/p_0 = 0.05 - 0.35

*Ghi chú:* Là phương pháp chuẩn xác định bề mặt riêng của vật liệu xốp, thường đo bằng hấp phụ N2 ở 77 K với ω(N2) = 0.162 nm^2.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.phuong-trinh-bet` · lớp 13 · #hoa-keo #hap-phu #bet</sub>

---

**Phương trình hấp phụ Gibbs** — *Gibbs adsorption isotherm*

$$\Gamma = -\frac{C}{RT}\cdot\frac{d\sigma}{dC} = -\frac{1}{RT}\cdot\frac{d\sigma}{d\ln C}$$

Trong đó: `Γ` là độ hấp phụ bề mặt (lượng dư bề mặt) (mol/m^2); `C` là nồng độ chất tan trong lòng dung dịch (mol/L); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `σ` là sức căng bề mặt (N/m); `dσ/dC` là hoạt tính bề mặt của chất tan.

*Điều kiện:* Dung dịch loãng, hệ hai cấu tử, chọn mặt phân chia Gibbs sao cho lượng dư dung môi bằng 0

*Ghi chú:* dσ/dC < 0 (chất hoạt động bề mặt) thì Γ > 0: chất tan tập trung ở bề mặt. dσ/dC > 0 (chất không hoạt động bề mặt như muối vô cơ) thì Γ < 0.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.phuong-trinh-hap-phu-gibbs` · lớp 13 · #hoa-keo #hap-phu #gibbs</sub>

---

**Phương trình Einstein - Smoluchowski về chuyển động Brown** — *Einstein - Smoluchowski equation for Brownian motion*

$$\overline{\Delta x^{2}} = 2Dt;\qquad D = \frac{k_{B}T}{6\pi\eta r} = \frac{RT}{6\pi\eta r N_{A}}$$

Trong đó: `Δx^2 trung bình` là bình phương trung bình độ dịch chuyển theo một phương (m^2); `D` là hệ số khuếch tán (m^2/s); `t` là thời gian quan sát (s); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `η` là độ nhớt của môi trường (Pa.s); `r` là bán kính hạt keo (m); `R` là hằng số khí; `N_A` là số Avogadro (mol^-1).

*Điều kiện:* Hạt hình cầu, môi trường liên tục (định luật Stokes), hệ loãng

*Ghi chú:* k_B = 1.381e-23 J/K. Công thức D = k_B.T/(6πηr) gọi là hệ thức Stokes - Einstein, dùng để xác định kích thước hạt keo và phân tử polymer.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.chuyen-dong-brown` · lớp 13 · #hoa-keo #brown #khuech-tan</sub>

---

**Phương trình Stokes về tốc độ sa lắng** — *Stokes equation for sedimentation velocity*

$$v = \frac{2r^{2}(\rho - \rho_{0})g}{9\eta};\qquad r = \sqrt{\frac{9\eta v}{2(\rho-\rho_{0})g}}$$

Trong đó: `v` là tốc độ sa lắng ổn định của hạt (m/s); `r` là bán kính hạt (m); `ρ` là khối lượng riêng của hạt (kg/m^3); `ρ_0` là khối lượng riêng của môi trường phân tán (kg/m^3); `g` là gia tốc trọng trường (m/s^2); `η` là độ nhớt của môi trường (Pa.s).

*Điều kiện:* Hạt hình cầu, cứng, chuyển động chậm (số Reynolds nhỏ), hệ loãng, bỏ qua chuyển động Brown (hạt lớn hơn khoảng 1 micromet)

*Ghi chú:* g = 9.8 m/s^2. Nếu ρ < ρ_0 thì v < 0: hạt nổi lên. Trong máy siêu li tâm thay g bằng gia tốc li tâm ω^2x.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.phuong-trinh-stokes` · lớp 13 · #hoa-keo #stokes #sa-lang</sub>

---

**Thế zeta và phương trình Smoluchowski về điện di** — *Zeta potential and the Smoluchowski equation*

$$u = \frac{v}{E} = \frac{\varepsilon_{0}\varepsilon_{r}\zeta}{\eta} \;\Rightarrow\; \zeta = \frac{\eta\,u}{\varepsilon_{0}\varepsilon_{r}}$$

Trong đó: `u` là độ linh động điện di của hạt keo (m^2/(V.s)); `v` là tốc độ chuyển động của hạt keo (m/s); `E` là cường độ điện trường (V/m); `ε_0` là hằng số điện môi chân không (F/m); `ε_r` là hằng số điện môi tương đối của môi trường (); `ζ` là thế zeta (thế điện động ở mặt trượt) (V); `η` là độ nhớt của môi trường (Pa.s).

*Điều kiện:* Hạt keo lớn so với bề dày lớp điện kép (mô hình Smoluchowski); môi trường có hằng số điện môi lớn

*Ghi chú:* |ζ| lớn hơn khoảng 30 mV thì hệ keo bền vững do lực đẩy tĩnh điện. Thêm chất điện li nén lớp điện kép làm giảm ζ và gây keo tụ (quy tắc Schulze - Hardy).

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.the-zeta` · lớp 13 · #hoa-keo #the-zeta #dien-di</sub>

---

**Công thức Jurin về hiện tượng mao dẫn** — *Jurin's law of capillary rise*

$$h = \frac{2\sigma\cos\theta}{\rho\,g\,r}$$

Trong đó: `h` là độ dâng (hoặc hạ) của chất lỏng trong ống mao quản (m); `σ` là sức căng bề mặt (N/m); `θ` là góc thấm ướt (góc tiếp xúc) (degree); `ρ` là khối lượng riêng của chất lỏng (kg/m^3); `g` là gia tốc trọng trường (m/s^2); `r` là bán kính trong của ống mao quản (m).

*Điều kiện:* Ống mao quản hình trụ, bán kính nhỏ; chất lỏng thấm ướt (θ < 90 độ) thì dâng lên, không thấm ướt (θ > 90 độ) thì hạ xuống

*Ghi chú:* g = 9.8 m/s^2. Đây là cơ sở của phương pháp đo sức căng bề mặt bằng ống mao quản.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.hien-tuong-mao-dan` · lớp 13 · #hoa-keo #mao-dan #suc-cang</sub>

---

**Sức căng bề mặt** — *Surface tension*

$$\sigma = \left(\frac{\partial G}{\partial A}\right)_{T,p} = \frac{F}{l};\qquad W = \sigma\,\Delta A$$

Trong đó: `σ` là sức căng bề mặt (còn kí hiệu γ) (N/m); `G` là năng lượng Gibbs của hệ (J); `A` là diện tích bề mặt (m^2); `F` là lực căng bề mặt (N); `l` là chiều dài đường tiếp xúc (m); `W` là công tạo bề mặt mới (J); `ΔA` là độ tăng diện tích bề mặt (m^2).

*Điều kiện:* Nhiệt độ và áp suất không đổi; bề mặt phân chia pha sạch

*Ghi chú:* Nước ở 20 độ C có σ = 72.8 mN/m; thủy ngân 485 mN/m; ethanol 22 mN/m. σ giảm khi nhiệt độ tăng và bằng 0 ở nhiệt độ tới hạn.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.suc-cang-be-mat` · lớp 13 · #hoa-keo #be-mat #suc-cang</sub>

---

**Phương trình Young - Laplace** — *Young - Laplace equation*

$$\Delta p = \sigma\left(\frac{1}{R_{1}}+\frac{1}{R_{2}}\right) \;\xrightarrow{\text{giọt cầu}}\; \Delta p = \frac{2\sigma}{r};\qquad \text{bong bóng xà phòng: } \Delta p = \frac{4\sigma}{r}$$

Trong đó: `Δp` là độ chênh áp suất qua mặt cong (áp suất mao dẫn) (Pa); `σ` là sức căng bề mặt (N/m); `R_1` là bán kính cong chính thứ nhất (m); `R_2` là bán kính cong chính thứ hai (m); `r` là bán kính của giọt hoặc bọt cầu (m).

*Điều kiện:* Mặt phân chia pha ở cân bằng cơ học; bỏ qua trọng lực

*Ghi chú:* Bong bóng xà phòng có hai mặt phân chia nên hệ số là 4. Giọt càng nhỏ thì áp suất bên trong càng lớn.

<sub>`chemistry.dai-hoc.hoa-keo-be-mat.young-laplace` · lớp 13 · #hoa-keo #be-mat #young-laplace</sub>

---

### IChO Hoá lượng tử

**Năng lượng khử định cư (năng lượng liên hợp) theo thuyết Hückel** — *Huckel delocalization energy of a conjugated system*

$$E_{\mathrm{deloc}}=E_{\pi}-2n\left(\alpha+\beta\right);\qquad \text{benzen}:\; E_{\pi}=6\alpha+8\beta,\; n=3 \;\Rightarrow\; E_{\mathrm{deloc}}=2\beta$$

Trong đó: `E_{\mathrm{deloc}}` là năng lượng khử định cư (âm vì beta âm, ứng với sự bền hoá) (J); `E_{\pi}` là tổng năng lượng của các electron pi tính theo thuyết Hückel (J); `n` là số liên kết đôi C=C định cư trong cấu trúc tham chiếu (); `\alpha` là tích phân Coulomb (năng lượng của một obitan p cô lập) (J); `\beta` là tích phân cộng hưởng giữa hai nguyên tử liền kề, mang giá trị ÂM (J).

*Điều kiện:* Cấu trúc tham chiếu gồm n liên kết đôi ĐỊNH CƯ kiểu etilen, mỗi liên kết đóng góp 2 electron ở mức alpha + beta. Với benzen: các mức Hückel là alpha + 2beta (1 obitan) và alpha + beta (2 obitan suy biến), sáu electron pi cho E_pi = 6alpha + 8beta, trong khi ba etilen cho 6alpha + 6beta. Giá trị thực nghiệm |2beta| vào khoảng 150 kJ/mol

*Ghi chú:* Câu hỏi "tính năng lượng bền hoá do liên hợp" là dạng bài cố định của IChO ở nội dung cấp độ 3, và là cách định lượng khái niệm tính thơm. Kho có nghiệm Hückel cho hệ vòng (giản đồ Frost) nhưng chưa có định nghĩa và cách tính năng lượng khử định cư. Không có trong chương trình GDPT 2018.

<sub>`chemistry.dai-hoc.icho-luong-tu.nang-luong-khu-dinh-cu-huckel` · lớp 13 · #icho #huckel #tinh-thom #hoa-luong-tu</sub>

---

### IChO Động hoá học

**Phản ứng song song bậc một và tỉ lệ sản phẩm** — *Parallel first-order reactions and the product ratio*

$$k_{\text{tong}}=k_{1}+k_{2},\qquad [\mathrm{A}]=[\mathrm{A}]_{0}e^{-\left(k_{1}+k_{2}\right)t},\qquad \frac{[\mathrm{B}]}{[\mathrm{C}]}=\frac{k_{1}}{k_{2}},\qquad \Phi_{\mathrm{B}}=\frac{k_{1}}{k_{1}+k_{2}}$$

Trong đó: `k_{\text{tong}}` là hằng số tốc độ biểu kiến của sự tiêu hao chất đầu A (1/s); `k_{1}` là hằng số tốc độ của hướng tạo sản phẩm B (1/s); `k_{2}` là hằng số tốc độ của hướng tạo sản phẩm C (1/s); `[\mathrm{A}]` là nồng độ chất đầu A tại thời điểm t (mol/L); `[\mathrm{A}]_{0}` là nồng độ ban đầu của A (mol/L); `[\mathrm{B}]` là nồng độ sản phẩm B (mol/L); `[\mathrm{C}]` là nồng độ sản phẩm C (mol/L); `t` là thời gian (s); `\Phi_{\mathrm{B}}` là hiệu suất phân đoạn (tỉ lệ mol) của sản phẩm B ().

*Điều kiện:* A phản ứng song song theo hai hướng bậc một không thuận nghịch cho B và C; hai sản phẩm không chuyển hoá lẫn nhau; ban đầu chỉ có A. Dấu hiệu nhận biết cơ chế song song: tỉ lệ [B]/[C] KHÔNG đổi theo thời gian. Nếu hai hướng có năng lượng hoạt hoá khác nhau thì tỉ lệ sản phẩm phụ thuộc nhiệt độ - đó là cơ sở của khống chế động học

*Ghi chú:* Phản ứng song song là một trong ba sơ đồ động học phức tạp bắt buộc của IChO (cùng phản ứng nối tiếp và phản ứng thuận nghịch). Kho Việt Nam có phản ứng nối tiếp và nguyên lí nồng độ ổn định nhưng chưa có sơ đồ song song cùng công thức hiệu suất phân đoạn.

<sub>`chemistry.dai-hoc.icho-dong-hoc.phan-ung-song-song` · lớp 13 · #icho #dong-hoc #phan-ung-song-song #co-che</sub>

---

### Nhiệt động hóa học

**Phương trình Gibbs - Helmholtz** — *Gibbs - Helmholtz equation*

$$\left[\frac{\partial}{\partial T}\left(\frac{G}{T}\right)\right]_{p} = -\frac{H}{T^{2}};\qquad \left[\frac{\partial}{\partial T}\left(\frac{\Delta G}{T}\right)\right]_{p} = -\frac{\Delta H}{T^{2}}$$

Trong đó: `G` là năng lượng Gibbs (J); `H` là enthalpy (J); `T` là nhiệt độ tuyệt đối (K); `ΔG` là biến thiên năng lượng Gibbs của phản ứng (J/mol); `ΔH` là biến thiên enthalpy của phản ứng (J/mol).

*Điều kiện:* Áp suất không đổi

*Ghi chú:* Dạng tương đương: G = H + T(∂G/∂T)_p. Kết hợp với ΔG0 = -RT lnK cho ngay phương trình đẳng áp Van't Hoff.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.gibbs-helmholtz` · lớp 13 · #nhiet-dong #gibbs-helmholtz #nang-luong-gibbs</sub>

---

**Các hệ thức Maxwell** — *Maxwell relations*

$$\left(\frac{\partial T}{\partial V}\right)_{S} = -\left(\frac{\partial p}{\partial S}\right)_{V};\quad \left(\frac{\partial T}{\partial p}\right)_{S} = \left(\frac{\partial V}{\partial S}\right)_{p};\quad \left(\frac{\partial S}{\partial V}\right)_{T} = \left(\frac{\partial p}{\partial T}\right)_{V};\quad \left(\frac{\partial S}{\partial p}\right)_{T} = -\left(\frac{\partial V}{\partial T}\right)_{p}$$

Trong đó: `T` là nhiệt độ tuyệt đối (K); `S` là entropy (J/K); `p` là áp suất (Pa); `V` là thể tích (m^3).

*Điều kiện:* Hệ kín, thành phần không đổi; suy từ tính chất vi phân toàn phần của U, H, A, G

*Ghi chú:* Hai hệ thức cuối rất hữu ích: cho phép tính biến thiên entropy theo các đại lượng đo được (p, V, T).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.he-thuc-maxwell` · lớp 13 · #nhiet-dong #maxwell #vi-phan</sub>

---

**Bốn phương trình cơ bản của nhiệt động lực học** — *The four fundamental thermodynamic equations*

$$\begin{cases} dU = T\,dS - p\,dV \\ dH = T\,dS + V\,dp \\ dA = -S\,dT - p\,dV \\ dG = -S\,dT + V\,dp \end{cases}$$

Trong đó: `U` là nội năng (J); `H` là enthalpy (J); `A` là năng lượng Helmholtz (J); `G` là năng lượng Gibbs (J); `T` là nhiệt độ tuyệt đối (K); `S` là entropy (J/K); `p` là áp suất (Pa); `V` là thể tích (m^3).

*Điều kiện:* Hệ kín, thành phần không đổi, chỉ có công thể tích, quá trình thuận nghịch

*Ghi chú:* Suy ra: (∂G/∂T)_p = -S và (∂G/∂p)_T = V. Ghi nhớ bằng hình vuông nhiệt động (bảng Born).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.phuong-trinh-co-ban-nhiet-dong` · lớp 13 · #nhiet-dong #the-nhiet-dong #vi-phan</sub>

---

**Công trong quá trình đoạn nhiệt** — *Work in an adiabatic process*

$$Q = 0 \Rightarrow W = \Delta U = n\,C_{V,m}\,(T_{2} - T_{1})$$

Trong đó: `Q` là nhiệt trao đổi (J); `W` là công hệ nhận (J); `ΔU` là biến thiên nội năng (J); `n` là số mol khí (mol); `C_V` là nhiệt dung mol đẳng tích (J/(mol.K)); `m` là nhiệt dung mol đẳng tích (J/(mol.K)); `T1` là nhiệt độ đầu (K); `T2` là nhiệt độ cuối (K).

*Điều kiện:* Khí lí tưởng, quá trình đoạn nhiệt (thuận nghịch hoặc không)

*Ghi chú:* Khi khí dãn nở đoạn nhiệt thì khí sinh công nên nhiệt độ giảm.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.cong-doan-nhiet` · lớp 13 · #nhiet-dong #doan-nhiet #cong</sub>

---

**Phương trình quá trình đoạn nhiệt thuận nghịch (Poisson)** — *Reversible adiabatic (isentropic) process equation*

$$pV^{\gamma} = \text{const};\quad TV^{\gamma-1} = \text{const};\quad T^{\gamma}p^{1-\gamma} = \text{const};\quad \gamma = \frac{C_{p}}{C_{V}}$$

Trong đó: `p` là áp suất (Pa); `V` là thể tích (m^3); `T` là nhiệt độ tuyệt đối (K); `γ` là hệ số đoạn nhiệt (chỉ số Poisson) (); `C_p` là nhiệt dung đẳng áp (J/K); `C_V` là nhiệt dung đẳng tích (J/K).

*Điều kiện:* Khí lí tưởng, quá trình đoạn nhiệt (Q = 0) và thuận nghịch, nhiệt dung không đổi

*Ghi chú:* Khí đơn nguyên tử γ = 5/3 ≈ 1.67; khí hai nguyên tử γ = 7/5 = 1.40.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.qua-trinh-doan-nhiet-thuan-nghich` · lớp 13 · #nhiet-dong #doan-nhiet #khi-li-tuong</sub>

---

**Công dãn nở chống áp suất ngoài không đổi** — *Expansion work against constant external pressure*

$$W = -p_{ext}\,\Delta V = -p_{ext}(V_{2} - V_{1})$$

Trong đó: `W` là công hệ nhận được từ môi trường (J); `p_ext` là áp suất ngoài (không đổi) (Pa); `ΔV` là biến thiên thể tích của hệ (m^3); `V1` là thể tích đầu (m^3); `V2` là thể tích cuối (m^3).

*Điều kiện:* Quá trình bất thuận nghịch, áp suất ngoài giữ không đổi; quy ước IUPAC (công hệ nhận là dương)

*Ghi chú:* Dãn nở (ΔV > 0) thì W < 0: hệ sinh công. Nếu dãn vào chân không (p_ext = 0) thì W = 0.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.cong-dan-no-chong-ap-suat-ngoai` · lớp 13 · #nhiet-dong #cong #nguyen-li-i</sub>

---

**Công dãn nở đẳng nhiệt thuận nghịch của khí lí tưởng** — *Isothermal reversible expansion work of an ideal gas*

$$W = -\int_{V_{1}}^{V_{2}} p\,dV = -nRT\ln\frac{V_{2}}{V_{1}} = nRT\ln\frac{p_{2}}{p_{1}}$$

Trong đó: `W` là công hệ nhận được (J); `n` là số mol khí (mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (không đổi) (K); `V1` là thể tích đầu (m^3); `V2` là thể tích cuối (m^3); `p1` là áp suất đầu (Pa); `p2` là áp suất cuối (Pa).

*Điều kiện:* Khí lí tưởng, quá trình đẳng nhiệt thuận nghịch

*Ghi chú:* R = 8.314 J/(mol.K). Vì T không đổi nên ΔU = 0, do đó Q = -W = nRT.ln(V2/V1).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.cong-dan-no-dang-nhiet-thuan-nghich` · lớp 13 · #nhiet-dong #cong #khi-li-tuong</sub>

---

**Định nghĩa enthalpy** — *Definition of enthalpy*

$$H = U + pV$$

Trong đó: `H` là enthalpy (J); `U` là nội năng (J); `p` là áp suất (Pa); `V` là thể tích (m^3).

*Điều kiện:* Áp dụng cho mọi hệ; H là hàm trạng thái

*Ghi chú:* H không đo được giá trị tuyệt đối, chỉ đo được biến thiên ΔH.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.enthalpy-dinh-nghia` · lớp 13 · #nhiet-dong #enthalpy #ham-trang-thai</sub>

---

**Nhiệt đẳng áp bằng biến thiên enthalpy** — *Heat at constant pressure equals enthalpy change*

$$Q_{p} = \Delta H$$

Trong đó: `Q_p` là nhiệt trao đổi ở áp suất không đổi (J); `ΔH` là biến thiên enthalpy (J).

*Điều kiện:* Quá trình đẳng áp, chỉ có công thể tích

*Ghi chú:* ΔH < 0: phản ứng tỏa nhiệt; ΔH > 0: phản ứng thu nhiệt.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-dang-ap` · lớp 13 · #nhiet-dong #enthalpy #nhiet-phan-ung</sub>

---

**Quan hệ giữa nhiệt đẳng áp và nhiệt đẳng tích** — *Relation between enthalpy and internal energy change of reaction*

$$\Delta H = \Delta U + \Delta n_{k}RT$$

Trong đó: `ΔH` là biến thiên enthalpy của phản ứng (J/mol); `ΔU` là biến thiên nội năng của phản ứng (J/mol); `Δn_k` là biến thiên số mol khí = tổng mol khí sản phẩm - tổng mol khí chất đầu (mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Các chất khí coi là khí lí tưởng; bỏ qua thể tích pha ngưng tụ; T không đổi

*Ghi chú:* Nếu Δn_k = 0 thì ΔH = ΔU. R = 8.314 J/(mol.K).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.quan-he-delta-h-delta-u` · lớp 13 · #nhiet-dong #enthalpy #noi-nang</sub>

---

**Công thức Boltzmann về entropy** — *Boltzmann entropy formula*

$$S = k_{B}\ln W$$

Trong đó: `S` là entropy của hệ (J/K); `k_B` là hằng số Boltzmann (J/K); `W` là số trạng thái vi mô (xác suất nhiệt động) ứng với trạng thái vĩ mô ().

*Điều kiện:* Hệ ở trạng thái cân bằng, các trạng thái vi mô đồng xác suất

*Ghi chú:* k_B = 1.381e-23 J/K = R/N_A. Entropy đo mức độ hỗn loạn (số cách sắp xếp) của hệ.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-boltzmann` · lớp 13 · #nhiet-dong #entropy #thong-ke</sub>

---

**Định nghĩa entropy theo Clausius** — *Clausius definition of entropy*

$$dS = \frac{\delta Q_{tn}}{T};\qquad \Delta S = \int_{1}^{2}\frac{\delta Q_{tn}}{T}$$

Trong đó: `S` là entropy (J/K); `δQ_tn` là nhiệt nguyên tố trao đổi theo con đường thuận nghịch (J); `T` là nhiệt độ tuyệt đối (K); `ΔS` là biến thiên entropy (J/K).

*Điều kiện:* Tích phân phải lấy theo đường thuận nghịch nối hai trạng thái

*Ghi chú:* S là hàm trạng thái nên ΔS chỉ phụ thuộc trạng thái đầu và cuối, dù quá trình thực có bất thuận nghịch.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-dinh-nghia-clausius` · lớp 13 · #nhiet-dong #entropy #nguyen-li-ii</sub>

---

**Biến thiên entropy chuẩn của phản ứng** — *Standard reaction entropy*

$$\Delta_{r}S^{0} = \sum \nu_{i}S^{0}_{i}(\text{sản phẩm}) - \sum \nu_{j}S^{0}_{j}(\text{chất đầu})$$

Trong đó: `Δ_rS0` là biến thiên entropy chuẩn của phản ứng (J/(mol.K)); `S0` là entropy tuyệt đối chuẩn của chất (J/(mol.K)); `ν` là hệ số tỉ lượng ().

*Điều kiện:* Điều kiện chuẩn (p = 1 bar), thường ở 298 K

*Ghi chú:* Nếu Δn_khí > 0 thì thường Δ_rS0 > 0. Khác với enthalpy, đơn chất bền có S0 khác 0.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-phan-ung-chuan` · lớp 13 · #nhiet-dong #entropy #phan-ung</sub>

---

**Hiệu suất của chu trình Carnot** — *Efficiency of the Carnot cycle*

$$\eta = \frac{|W|}{Q_{1}} = \frac{T_{1} - T_{2}}{T_{1}} = 1 - \frac{T_{2}}{T_{1}}$$

Trong đó: `η` là hiệu suất nhiệt (); `W` là công máy sinh ra trong một chu trình (J); `Q1` là nhiệt nhận từ nguồn nóng (J); `T1` là nhiệt độ nguồn nóng (K); `T2` là nhiệt độ nguồn lạnh (K).

*Điều kiện:* Chu trình Carnot thuận nghịch giữa hai nguồn nhiệt có nhiệt độ không đổi

*Ghi chú:* Đây là hiệu suất cực đại của mọi máy nhiệt làm việc giữa hai nguồn nhiệt T1 và T2 (định lí Carnot).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.hieu-suat-carnot` · lớp 13 · #nhiet-dong #carnot #nguyen-li-ii</sub>

---

**Nguyên lí thứ hai của nhiệt động lực học** — *Second law of thermodynamics*

$$\Delta S_{\text{hệ}} + \Delta S_{\text{mt}} = \Delta S_{\text{cô lập}} \geq 0$$

Trong đó: `ΔS_hệ` là biến thiên entropy của hệ (J/K); `ΔS_mt` là biến thiên entropy của môi trường (J/K); `ΔS_cô lập` là biến thiên entropy của hệ cô lập (hệ + môi trường) (J/K).

*Điều kiện:* Áp dụng cho hệ cô lập; dấu bằng ứng với quá trình thuận nghịch

*Ghi chú:* Trong hệ cô lập: ΔS > 0 quá trình tự diễn biến; ΔS = 0 hệ ở cân bằng. Với môi trường ở T không đổi: ΔS_mt = -Q_hệ/T.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nguyen-li-ii` · lớp 13 · #nhiet-dong #entropy #nguyen-li-ii</sub>

---

**Nguyên lí thứ ba của nhiệt động lực học** — *Third law of thermodynamics*

$$\lim_{T \to 0}S = 0 \quad \text{(tinh thể hoàn hảo)};\qquad S^{0}_{T} = \int_{0}^{T}\frac{C_{p}}{T}\,dT + \sum \frac{\Delta H_{cp}}{T_{cp}}$$

Trong đó: `S` là entropy (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `S0_T` là entropy tuyệt đối chuẩn ở nhiệt độ T (J/(mol.K)); `C_p` là nhiệt dung đẳng áp (J/(mol.K)); `ΔH_cp` là nhiệt chuyển pha (J/mol); `T_cp` là nhiệt độ chuyển pha (K).

*Điều kiện:* Tinh thể hoàn hảo, nguyên chất ở 0 K

*Ghi chú:* Nhờ nguyên lí III mà entropy có giá trị tuyệt đối, khác với U và H. Bảng tra thường cho S0_298.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nguyen-li-iii` · lớp 13 · #nhiet-dong #entropy #nguyen-li-iii</sub>

---

**Nguyên lí thứ nhất của nhiệt động lực học** — *First law of thermodynamics*

$$\Delta U = Q + W \quad ; \quad dU = \delta Q + \delta W$$

Trong đó: `ΔU` là biến thiên nội năng của hệ (J); `Q` là nhiệt hệ nhận được (J); `W` là công hệ nhận được (J).

*Điều kiện:* Hệ kín (không trao đổi chất với môi trường)

*Ghi chú:* U là hàm trạng thái, Q và W là hàm quá trình. Với hệ cô lập ΔU = 0. Quy ước IUPAC: hệ nhận nhiệt/công thì mang dấu dương.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nguyen-li-i` · lớp 13 · #nhiet-dong #nguyen-li-i #noi-nang</sub>

---

**Nhiệt đẳng tích bằng biến thiên nội năng** — *Heat at constant volume equals internal energy change*

$$Q_{V} = \Delta U$$

Trong đó: `Q_V` là nhiệt trao đổi ở thể tích không đổi (J); `ΔU` là biến thiên nội năng (J).

*Điều kiện:* Quá trình đẳng tích, chỉ có công thể tích (W = 0)

*Ghi chú:* Đo bằng bom nhiệt lượng kế (calorimeter đẳng tích).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-dang-tich` · lớp 13 · #nhiet-dong #nguyen-li-i #noi-nang</sub>

---

**Hệ thức Mayer cho khí lí tưởng** — *Mayer relation for ideal gases*

$$C_{p,m} - C_{V,m} = R$$

Trong đó: `C_p` là nhiệt dung mol đẳng áp (J/(mol.K)); `m` là nhiệt dung mol đẳng áp (J/(mol.K)); `C_V` là nhiệt dung mol đẳng tích (J/(mol.K)); `R` là hằng số khí (J/(mol.K)).

*Điều kiện:* Khí lí tưởng

*Ghi chú:* Khí đơn nguyên tử: C_V,m = 3R/2, C_p,m = 5R/2. Khí hai nguyên tử (bỏ qua dao động): C_V,m = 5R/2, C_p,m = 7R/2. R = 8.314 J/(mol.K).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.he-thuc-mayer` · lớp 13 · #nhiet-dong #nhiet-dung #khi-li-tuong</sub>

---

**Nhiệt dung đẳng áp** — *Heat capacity at constant pressure*

$$C_{p} = \left(\frac{\partial H}{\partial T}\right)_{p} \quad \Rightarrow \quad \Delta H = \int_{T_{1}}^{T_{2}} C_{p}\,dT$$

Trong đó: `C_p` là nhiệt dung đẳng áp (J/K); `H` là enthalpy (J); `T` là nhiệt độ tuyệt đối (K); `T1` là nhiệt độ đầu (K); `T2` là nhiệt độ cuối (K).

*Điều kiện:* Áp suất không đổi, không có chuyển pha trong khoảng nhiệt độ xét

*Ghi chú:* Thực nghiệm thường biểu diễn C_p,m = a + bT + cT^2 hoặc a + bT + c'/T^2.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-dung-dang-ap` · lớp 13 · #nhiet-dong #nhiet-dung #enthalpy</sub>

---

**Nhiệt dung đẳng tích** — *Heat capacity at constant volume*

$$C_{V} = \left(\frac{\partial U}{\partial T}\right)_{V} \quad \Rightarrow \quad \Delta U = \int_{T_{1}}^{T_{2}} C_{V}\,dT$$

Trong đó: `C_V` là nhiệt dung đẳng tích (J/K); `U` là nội năng (J); `T` là nhiệt độ tuyệt đối (K); `T1` là nhiệt độ đầu (K); `T2` là nhiệt độ cuối (K).

*Điều kiện:* Thể tích không đổi, không có chuyển pha trong khoảng nhiệt độ xét

*Ghi chú:* Nếu C_V coi như hằng số thì ΔU = C_V(T2 - T1). Nhiệt dung mol kí hiệu C_V,m đơn vị J/(mol.K).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-dung-dang-tich` · lớp 13 · #nhiet-dong #nhiet-dung</sub>

---

**Nhiệt lượng trao đổi khi thay đổi nhiệt độ** — *Heat exchanged on temperature change*

$$Q = n\,C_{m}\,\Delta T = m\,c\,\Delta T$$

Trong đó: `Q` là nhiệt lượng trao đổi (J); `n` là số mol chất (mol); `C_m` là nhiệt dung mol (J/(mol.K)); `m` là khối lượng chất (kg); `c` là nhiệt dung riêng (J/(kg.K)); `ΔT` là độ biến thiên nhiệt độ (K).

*Điều kiện:* Nhiệt dung coi như không đổi trong khoảng nhiệt độ xét, không có chuyển pha

*Ghi chú:* Nhiệt dung riêng của nước lỏng c = 4.18 kJ/(kg.K) = 75.3 J/(mol.K).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-luong-theo-nhiet-dung` · lớp 13 · #nhiet-dong #nhiet-dung #nhiet-luong-ke</sub>

---

**Định luật Hess** — *Hess's law*

$$\Delta H_{\text{tổng}} = \sum_{i} \Delta H_{i}$$

Trong đó: `ΔH_tổng` là biến thiên enthalpy của quá trình tổng (kJ/mol); `ΔH_i` là biến thiên enthalpy của giai đoạn thứ i (kJ/mol).

*Điều kiện:* Cùng trạng thái đầu và trạng thái cuối; quá trình đẳng áp (hoặc đẳng tích với ΔU)

*Ghi chú:* Hệ quả của tính chất hàm trạng thái của H: nhiệt phản ứng không phụ thuộc đường đi. Đảo chiều phản ứng thì đổi dấu ΔH; nhân hệ số k thì ΔH nhân k.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.dinh-luat-hess` · lớp 13 · #nhiet-hoa-hoc #dinh-luat-hess #enthalpy</sub>

---

**Tính nhiệt phản ứng theo nhiệt đốt cháy chuẩn** — *Reaction enthalpy from standard enthalpies of combustion*

$$\Delta_{r}H^{0}_{298} = \sum \nu_{j}\,\Delta_{c}H^{0}_{298}(\text{chất đầu}) - \sum \nu_{i}\,\Delta_{c}H^{0}_{298}(\text{sản phẩm})$$

Trong đó: `Δ_rH0_298` là biến thiên enthalpy chuẩn của phản ứng (kJ/mol); `Δ_cH0_298` là nhiệt đốt cháy chuẩn của chất (kJ/mol); `ν` là hệ số tỉ lượng ().

*Điều kiện:* Các chất cháy hoàn toàn thành cùng một bộ sản phẩm (CO2 khí, H2O lỏng, N2 khí, SO2 khí)

*Ghi chú:* Chú ý dấu ngược với công thức theo nhiệt tạo thành: lấy chất đầu trừ sản phẩm. Δ_cH0 luôn âm.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-dot-chay-chuan` · lớp 13 · #nhiet-hoa-hoc #enthalpy #dot-chay</sub>

---

**Tính nhiệt phản ứng theo năng lượng liên kết** — *Reaction enthalpy from bond energies*

$$\Delta_{r}H = \sum E_{b}(\text{liên kết bị phá vỡ}) - \sum E_{b}(\text{liên kết được tạo thành})$$

Trong đó: `Δ_rH` là biến thiên enthalpy của phản ứng (kJ/mol); `E_b` là năng lượng liên kết trung bình (kJ/mol).

*Điều kiện:* Tất cả các chất ở trạng thái khí; chỉ cho kết quả gần đúng vì dùng năng lượng liên kết trung bình

*Ghi chú:* Phá vỡ liên kết thu nhiệt (E_b > 0), tạo liên kết tỏa nhiệt. Ví dụ E(H-H) = 436 kJ/mol, E(O=O) = 498 kJ/mol.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-phan-ung-theo-nang-luong-lien-ket` · lớp 13 · #nhiet-hoa-hoc #nang-luong-lien-ket #enthalpy</sub>

---

**Tính nhiệt phản ứng theo nhiệt tạo thành chuẩn** — *Reaction enthalpy from standard enthalpies of formation*

$$\Delta_{r}H^{0}_{298} = \sum \nu_{i}\,\Delta_{f}H^{0}_{298}(\text{sản phẩm}) - \sum \nu_{j}\,\Delta_{f}H^{0}_{298}(\text{chất đầu})$$

Trong đó: `Δ_rH0_298` là biến thiên enthalpy chuẩn của phản ứng ở 298 K (kJ/mol); `Δ_fH0_298` là nhiệt tạo thành chuẩn (enthalpy tạo thành chuẩn) của chất (kJ/mol); `ν` là hệ số tỉ lượng trong phương trình hóa học ().

*Điều kiện:* Điều kiện chuẩn: p = 1 bar, các chất ở trạng thái chuẩn, thường quy về 298 K

*Ghi chú:* Quy ước Δ_fH0 = 0 với đơn chất bền nhất ở điều kiện chuẩn (O2 khí, C graphit, Br2 lỏng...).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nhiet-tao-thanh-chuan` · lớp 13 · #nhiet-hoa-hoc #enthalpy #dinh-luat-hess</sub>

---

**Phương trình Kirchhoff dạng tích phân** — *Kirchhoff's equation (integrated form)*

$$\Delta_{r}H(T_{2}) = \Delta_{r}H(T_{1}) + \int_{T_{1}}^{T_{2}} \Delta C_{p}\,dT \;\xrightarrow{\Delta C_{p}=\text{const}}\; \Delta_{r}H(T_{2}) = \Delta_{r}H(T_{1}) + \Delta C_{p}(T_{2}-T_{1})$$

Trong đó: `Δ_rH(T)` là biến thiên enthalpy của phản ứng ở nhiệt độ T (J/mol); `ΔC_p` là biến thiên nhiệt dung đẳng áp của phản ứng (J/(mol.K)); `T1` là nhiệt độ đầu (K); `T2` là nhiệt độ cuối (K).

*Điều kiện:* Không có chuyển pha giữa T1 và T2; áp suất không đổi

*Ghi chú:* Tương tự cho entropy: ΔS(T2) = ΔS(T1) + ∫ (ΔC_p/T) dT.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.phuong-trinh-kirchhoff-tich-phan` · lớp 13 · #nhiet-hoa-hoc #kirchhoff #enthalpy</sub>

---

**Phương trình Kirchhoff dạng vi phân** — *Kirchhoff's equation (differential form)*

$$\left(\frac{\partial \Delta_{r}H}{\partial T}\right)_{p} = \Delta C_{p};\qquad \Delta C_{p} = \sum \nu_{i}C_{p,i}(\text{sp}) - \sum \nu_{j}C_{p,j}(\text{cđ})$$

Trong đó: `Δ_rH` là biến thiên enthalpy của phản ứng (J/mol); `T` là nhiệt độ tuyệt đối (K); `ΔC_p` là biến thiên nhiệt dung đẳng áp của phản ứng (J/(mol.K)); `C_p` là nhiệt dung mol đẳng áp của chất i (J/(mol.K)); `i` là nhiệt dung mol đẳng áp của chất i (J/(mol.K)); `ν` là hệ số tỉ lượng.

*Điều kiện:* Áp suất không đổi; không có chuyển pha trong khoảng nhiệt độ xét

*Ghi chú:* Dạng tương tự cho đẳng tích: (∂ΔU/∂T)_V = ΔC_V.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.phuong-trinh-kirchhoff-vi-phan` · lớp 13 · #nhiet-hoa-hoc #kirchhoff #nhiet-dung</sub>

---

**Định nghĩa thế hóa học** — *Chemical potential*

$$\mu_{i} = \left(\frac{\partial G}{\partial n_{i}}\right)_{T,p,n_{j\neq i}};\qquad dG = -S\,dT + V\,dp + \sum_{i}\mu_{i}\,dn_{i}$$

Trong đó: `μ_i` là thế hóa học của cấu tử i (J/mol); `G` là năng lượng Gibbs của hệ (J); `n_i` là số mol cấu tử i (mol); `T` là nhiệt độ (K); `p` là áp suất (Pa); `S` là entropy (J/K); `V` là thể tích (m^3).

*Điều kiện:* Hệ mở hoặc hệ có thay đổi thành phần

*Ghi chú:* Điều kiện cân bằng pha: thế hóa học của mỗi cấu tử bằng nhau trong mọi pha. Điều kiện cân bằng hóa học: Σν_i μ_i = 0.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.the-hoa-hoc` · lớp 13 · #nhiet-dong #the-hoa-hoc #can-bang-pha</sub>

---

**Thế hóa học của khí lí tưởng** — *Chemical potential of an ideal gas*

$$\mu = \mu^{0} + RT\ln\frac{p}{p^{0}};\qquad \text{khí thực: } \mu = \mu^{0} + RT\ln\frac{f}{p^{0}},\; f = \varphi p$$

Trong đó: `μ` là thế hóa học ở áp suất p (J/mol); `μ0` là thế hóa học chuẩn (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `p` là áp suất riêng phần (bar); `p0` là áp suất chuẩn (1 bar) (bar); `f` là fugacity (hoạt áp) của khí thực (bar); `φ` là hệ số fugacity ().

*Điều kiện:* Khí lí tưởng; với khí thực thay p bằng fugacity f

*Ghi chú:* Khi p -> 0 thì φ -> 1, khí thực tiến về khí lí tưởng.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.the-hoa-hoc-khi-li-tuong` · lớp 13 · #nhiet-dong #the-hoa-hoc #khi-li-tuong</sub>

---

**Biến thiên năng lượng Gibbs theo áp suất** — *Pressure dependence of Gibbs energy*

$$\Delta G = \int_{p_{1}}^{p_{2}} V\,dp \;\xrightarrow{\text{khí lí tưởng}}\; nRT\ln\frac{p_{2}}{p_{1}}$$

Trong đó: `ΔG` là biến thiên năng lượng Gibbs (J); `V` là thể tích (m^3); `p1` là áp suất đầu (Pa); `p2` là áp suất cuối (Pa); `n` là số mol (mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Nhiệt độ không đổi; với chất lỏng và chất rắn coi V không đổi nên ΔG ≈ V(p2 - p1)

*Ghi chú:* Nén khí (p2 > p1) làm G tăng.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.bien-thien-g-theo-ap-suat` · lớp 13 · #nhiet-dong #nang-luong-gibbs #khi-li-tuong</sub>

---

**Công hữu ích cực đại của quá trình đẳng nhiệt - đẳng áp** — *Maximum non-expansion work*

$$W_{\text{hữu ích, max}} = \Delta G_{T,p}$$

Trong đó: `W_hữu ích` là công hữu ích (không phải công thể tích) cực đại mà hệ nhận (J); `max` là công hữu ích (không phải công thể tích) cực đại mà hệ nhận (J); `ΔG` là biến thiên năng lượng Gibbs (J).

*Điều kiện:* Quá trình thuận nghịch, T và p không đổi

*Ghi chú:* Là cơ sở của pin điện hóa: -ΔG = nFE là công điện cực đại pin sinh ra.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.cong-huu-ich-cuc-dai` · lớp 13 · #nhiet-dong #nang-luong-gibbs #cong</sub>

---

**Phương trình đẳng áp Van't Hoff dạng tích phân** — *Van't Hoff equation (integrated form)*

$$\ln\frac{K_{2}}{K_{1}} = -\frac{\Delta_{r}H^{0}}{R}\left(\frac{1}{T_{2}} - \frac{1}{T_{1}}\right) = \frac{\Delta_{r}H^{0}}{R}\cdot\frac{T_{2}-T_{1}}{T_{1}T_{2}}$$

Trong đó: `K1` là hằng số cân bằng ở T1 (); `K2` là hằng số cân bằng ở T2 (); `Δ_rH0` là biến thiên enthalpy chuẩn của phản ứng (J/mol); `R` là hằng số khí (J/(mol.K)); `T1` là nhiệt độ thứ nhất (K); `T2` là nhiệt độ thứ hai (K).

*Điều kiện:* Coi Δ_rH0 không đổi trong khoảng nhiệt độ T1 - T2

*Ghi chú:* Dạng đường thẳng: lnK = -Δ_rH0/(RT) + Δ_rS0/R, đồ thị lnK theo 1/T có hệ số góc -Δ_rH0/R.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.dang-ap-vant-hoff-tich-phan` · lớp 13 · #nhiet-dong #can-bang #vant-hoff</sub>

---

**Phương trình đẳng áp Van't Hoff dạng vi phân** — *Van't Hoff equation (differential form)*

$$\left(\frac{d\ln K_{p}}{dT}\right) = \frac{\Delta_{r}H^{0}}{RT^{2}}$$

Trong đó: `K_p` là hằng số cân bằng theo áp suất riêng phần (); `T` là nhiệt độ tuyệt đối (K); `Δ_rH0` là biến thiên enthalpy chuẩn của phản ứng (J/mol); `R` là hằng số khí (J/(mol.K)).

*Điều kiện:* Áp suất chuẩn cố định; Δ_rH0 phụ thuộc T nói chung

*Ghi chú:* Phản ứng thu nhiệt (Δ_rH0 > 0): tăng T thì K tăng. Phản ứng tỏa nhiệt: tăng T thì K giảm - phù hợp nguyên lí Le Chatelier.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.dang-ap-vant-hoff-vi-phan` · lớp 13 · #nhiet-dong #can-bang #vant-hoff</sub>

---

**Phương trình đẳng nhiệt Van't Hoff** — *Van't Hoff isotherm*

$$\Delta_{r}G = \Delta_{r}G^{0} + RT\ln Q = RT\ln\frac{Q}{K}$$

Trong đó: `Δ_rG` là biến thiên năng lượng Gibbs của phản ứng ở điều kiện đang xét (J/mol); `Δ_rG0` là biến thiên năng lượng Gibbs chuẩn (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `Q` là thương số phản ứng (tỉ số hoạt độ tức thời) (); `K` là hằng số cân bằng ().

*Điều kiện:* T, p không đổi; Q và K biểu diễn theo cùng loại đại lượng (hoạt độ hoặc áp suất riêng phần quy chuẩn)

*Ghi chú:* Q < K thì Δ_rG < 0, phản ứng diễn ra theo chiều thuận; Q > K thì diễn ra theo chiều nghịch; Q = K thì cân bằng.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.dang-nhiet-vant-hoff` · lớp 13 · #nhiet-dong #can-bang #nang-luong-gibbs</sub>

---

**Biến thiên năng lượng Gibbs chuẩn của phản ứng** — *Standard Gibbs energy change of reaction*

$$\Delta_{r}G^{0}_{T} = \Delta_{r}H^{0}_{T} - T\Delta_{r}S^{0}_{T} = \sum \nu_{i}\Delta_{f}G^{0}_{i}(\text{sp}) - \sum \nu_{j}\Delta_{f}G^{0}_{j}(\text{cđ})$$

Trong đó: `Δ_rG0_T` là biến thiên năng lượng Gibbs chuẩn của phản ứng ở T (kJ/mol); `Δ_rH0_T` là biến thiên enthalpy chuẩn (kJ/mol); `Δ_rS0_T` là biến thiên entropy chuẩn (J/(mol.K)); `Δ_fG0` là năng lượng Gibbs tạo thành chuẩn (kJ/mol); `T` là nhiệt độ tuyệt đối (K); `ν` là hệ số tỉ lượng.

*Điều kiện:* Điều kiện chuẩn p = 1 bar; khi dùng gần đúng Δ_rH0 và Δ_rS0 lấy ở 298 K coi như không đổi theo T

*Ghi chú:* Nhớ đổi đơn vị: Δ_rS0 tính bằng J/(mol.K) còn Δ_rH0 bằng kJ/mol. Nhiệt độ đảo chiều phản ứng: T = Δ_rH0/Δ_rS0.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.delta-g-chuan-phan-ung` · lớp 13 · #nhiet-dong #nang-luong-gibbs #phan-ung</sub>

---

**Quan hệ giữa năng lượng Gibbs chuẩn và hằng số cân bằng** — *Relation between standard Gibbs energy and equilibrium constant*

$$\Delta_{r}G^{0} = -RT\ln K \quad \Leftrightarrow \quad K = e^{-\Delta_{r}G^{0}/(RT)}$$

Trong đó: `Δ_rG0` là biến thiên năng lượng Gibbs chuẩn của phản ứng (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `K` là hằng số cân bằng nhiệt động (không thứ nguyên) ().

*Điều kiện:* K là hằng số cân bằng nhiệt động, tính theo hoạt độ quy về trạng thái chuẩn

*Ghi chú:* Ở 298 K: Δ_rG0 = -5.708.logK (kJ/mol). Δ_rG0 < 0 thì K > 1.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.delta-g0-va-hang-so-can-bang` · lớp 13 · #nhiet-dong #can-bang #nang-luong-gibbs</sub>

---

**Năng lượng Gibbs (thế đẳng áp - đẳng nhiệt)** — *Gibbs free energy*

$$G = H - TS = U + pV - TS$$

Trong đó: `G` là năng lượng Gibbs (J); `H` là enthalpy (J); `T` là nhiệt độ tuyệt đối (K); `S` là entropy (J/K); `U` là nội năng (J); `p` là áp suất (Pa); `V` là thể tích (m^3).

*Điều kiện:* Hàm trạng thái, dùng cho quá trình đẳng nhiệt - đẳng áp

*Ghi chú:* Ở T, p không đổi: ΔG = ΔH - TΔS.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nang-luong-gibbs` · lớp 13 · #nhiet-dong #nang-luong-gibbs #the-nhiet-dong</sub>

---

**Năng lượng Helmholtz (thế đẳng tích - đẳng nhiệt)** — *Helmholtz free energy*

$$A = U - TS;\qquad G = A + pV$$

Trong đó: `A` là năng lượng Helmholtz (còn kí hiệu F) (J); `U` là nội năng (J); `T` là nhiệt độ tuyệt đối (K); `S` là entropy (J/K); `G` là năng lượng Gibbs (J); `p` là áp suất (Pa); `V` là thể tích (m^3).

*Điều kiện:* Hàm trạng thái, dùng cho quá trình đẳng nhiệt - đẳng tích

*Ghi chú:* Ở T, V không đổi, quá trình tự diễn biến khi ΔA < 0. -ΔA bằng công cực đại hệ có thể sinh ra trong quá trình đẳng nhiệt.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.nang-luong-helmholtz` · lớp 13 · #nhiet-dong #helmholtz #the-nhiet-dong</sub>

---

**Tiêu chuẩn tự diễn biến và cân bằng** — *Criteria of spontaneity and equilibrium*

$$\begin{cases} (\Delta G)_{T,p} < 0 & \text{tự diễn biến} \\ (\Delta G)_{T,p} = 0 & \text{cân bằng} \\ (\Delta G)_{T,p} > 0 & \text{không tự diễn biến} \end{cases}$$

Trong đó: `ΔG` là biến thiên năng lượng Gibbs của hệ (J); `T` là nhiệt độ tuyệt đối (K); `p` là áp suất (Pa).

*Điều kiện:* Hệ đóng, nhiệt độ và áp suất không đổi, chỉ có công thể tích

*Ghi chú:* Tiêu chuẩn tương ứng ở T, V không đổi là ΔA. Bốn trường hợp dấu ΔH, ΔS: ΔH<0 và ΔS>0 tự diễn biến ở mọi T; ΔH>0 và ΔS<0 không bao giờ tự diễn biến.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.tieu-chuan-tu-dien-bien` · lớp 13 · #nhiet-dong #nang-luong-gibbs #tu-dien-bien</sub>

---

**Biến thiên entropy của quá trình chuyển pha** — *Entropy change of a phase transition*

$$\Delta S_{cp} = \frac{\Delta H_{cp}}{T_{cp}}$$

Trong đó: `ΔS_cp` là biến thiên entropy chuyển pha (J/(mol.K)); `ΔH_cp` là nhiệt (enthalpy) chuyển pha (J/mol); `T_cp` là nhiệt độ chuyển pha (K).

*Điều kiện:* Chuyển pha thuận nghịch, xảy ra ở nhiệt độ và áp suất không đổi

*Ghi chú:* Nóng chảy, bay hơi, thăng hoa đều làm tăng entropy. Ví dụ nước: ΔH_hh = 40.7 kJ/mol ở 373.15 K nên ΔS_hh = 109 J/(mol.K).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-chuyen-pha` · lớp 13 · #nhiet-dong #entropy #chuyen-pha</sub>

---

**Biến thiên entropy khi đun nóng đẳng áp** — *Entropy change on isobaric heating*

$$\Delta S = \int_{T_{1}}^{T_{2}} \frac{C_{p}}{T}\,dT \;\xrightarrow{C_{p}=\text{const}}\; nC_{p,m}\ln\frac{T_{2}}{T_{1}}$$

Trong đó: `ΔS` là biến thiên entropy (J/K); `C_p` là nhiệt dung đẳng áp (J/K); `m` là nhiệt dung mol đẳng áp (J/(mol.K)); `n` là số mol (mol); `T1` là nhiệt độ đầu (K); `T2` là nhiệt độ cuối (K).

*Điều kiện:* Áp suất không đổi, không có chuyển pha giữa T1 và T2

*Ghi chú:* Đun nóng (T2 > T1) làm entropy tăng.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-dang-ap` · lớp 13 · #nhiet-dong #entropy #nhiet-dung</sub>

---

**Biến thiên entropy trong quá trình đẳng nhiệt của khí lí tưởng** — *Entropy change in an isothermal ideal-gas process*

$$\Delta S = nR\ln\frac{V_{2}}{V_{1}} = nR\ln\frac{p_{1}}{p_{2}}$$

Trong đó: `ΔS` là biến thiên entropy (J/K); `n` là số mol khí (mol); `R` là hằng số khí (J/(mol.K)); `V1` là thể tích đầu (m^3); `V2` là thể tích cuối (m^3); `p1` là áp suất đầu (Pa); `p2` là áp suất cuối (Pa).

*Điều kiện:* Khí lí tưởng, nhiệt độ không đổi

*Ghi chú:* Công thức đúng cho cả quá trình bất thuận nghịch vì S là hàm trạng thái.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-dang-nhiet-khi-li-tuong` · lớp 13 · #nhiet-dong #entropy #khi-li-tuong</sub>

---

**Biến thiên entropy khi đun nóng đẳng tích** — *Entropy change on isochoric heating*

$$\Delta S = \int_{T_{1}}^{T_{2}} \frac{C_{V}}{T}\,dT \;\xrightarrow{C_{V}=\text{const}}\; nC_{V,m}\ln\frac{T_{2}}{T_{1}}$$

Trong đó: `ΔS` là biến thiên entropy (J/K); `C_V` là nhiệt dung đẳng tích (J/K); `m` là nhiệt dung mol đẳng tích (J/(mol.K)); `n` là số mol (mol); `T1` là nhiệt độ đầu (K); `T2` là nhiệt độ cuối (K).

*Điều kiện:* Thể tích không đổi, không có chuyển pha giữa T1 và T2

*Ghi chú:* Quá trình tổng quát (đổi cả T và V) của khí lí tưởng: ΔS = nC_V,m.ln(T2/T1) + nR.ln(V2/V1).

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-dang-tich` · lớp 13 · #nhiet-dong #entropy #nhiet-dung</sub>

---

**Biến thiên entropy khi trộn khí lí tưởng** — *Entropy of mixing of ideal gases*

$$\Delta S_{tr} = -nR\sum_{i} x_{i}\ln x_{i} > 0$$

Trong đó: `ΔS_tr` là biến thiên entropy trộn (J/K); `n` là tổng số mol khí (mol); `R` là hằng số khí (J/(mol.K)); `x_i` là phần mol của khí i trong hỗn hợp ().

*Điều kiện:* Các khí lí tưởng, trộn ở cùng nhiệt độ và áp suất, không phản ứng với nhau

*Ghi chú:* Vì 0 < x_i < 1 nên ln x_i < 0, do đó ΔS_tr luôn dương: quá trình trộn tự diễn biến. Với dung dịch lí tưởng cũng có dạng tương tự.

<sub>`chemistry.dai-hoc.nhiet-dong-hoa-hoc.entropy-tron-khi` · lớp 13 · #nhiet-dong #entropy #hon-hop-khi</sub>

---

### Nhiệt động lực học thống kê

**Áp suất tính từ hàm phân bố** — *Pressure from the partition function*

$$p = k_{B}T\left(\frac{\partial \ln Q}{\partial V}\right)_{T}\;\Rightarrow\; pV = nRT\ \text{(khí lí tưởng)}$$

Trong đó: `p` là áp suất (Pa); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `Q` là hàm phân bố chính tắc (); `V` là thể tích (m^3); `n` là số mol (mol); `R` là hằng số khí (J/(mol.K)).

*Điều kiện:* Hệ chính tắc; với khí lí tưởng chỉ q^T phụ thuộc V nên lnQ chứa N lnV, cho ngay phương trình trạng thái

*Ghi chú:* Atkins Focus 13C. Đây là chứng minh 'từ nguyên lí đầu' của phương trình khí lí tưởng - kết quả không có trong chương trình Việt Nam (ở đó pV = nRT là định luật thực nghiệm).

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.ap-suat-tu-ham-phan-bo` · lớp 13 · #nhiet-dong-thong-ke #ap-suat #khi-li-tuong #intl-undergrad</sub>

---

**Entropy thống kê tính từ hàm phân bố** — *Statistical entropy from the partition function*

$$S = \frac{U - U(0)}{T} + k_{B}\ln Q;\qquad A - A(0) = -k_{B}T\ln Q$$

Trong đó: `S` là entropy của hệ (J/K); `U` là nội năng (J); `U(0)` là nội năng ở 0 K (J); `T` là nhiệt độ tuyệt đối (K); `k_B` là hằng số Boltzmann (J/K); `Q` là hàm phân bố chính tắc (); `A` là năng lượng Helmholtz (J); `A(0)` là năng lượng Helmholtz ở 0 K (J).

*Điều kiện:* Hệ chính tắc; entropy đo từ giá trị 0 ở 0 K (phù hợp nguyên lí thứ ba)

*Ghi chú:* Atkins Focus 13E. Đây là cầu nối định lượng giữa mô tả vi mô và nhiệt động lực học cổ điển: mọi hàm nhiệt động đều suy ra được từ Q. Kho Việt Nam có công thức Boltzmann S = k lnW nhưng không có dạng qua hàm phân bố này.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.entropy-tu-ham-phan-bo` · lớp 13 · #nhiet-dong-thong-ke #entropy #helmholtz #intl-undergrad</sub>

---

**Nội năng tính từ hàm phân bố** — *Internal energy from the partition function*

$$U - U(0) = -\left(\frac{\partial \ln Q}{\partial \beta}\right)_{V} = k_{B}T^{2}\left(\frac{\partial \ln Q}{\partial T}\right)_{V}$$

Trong đó: `U` là nội năng của hệ (J); `U(0)` là nội năng ở 0 K (J); `Q` là hàm phân bố chính tắc (); `β` là nghịch đảo nhiệt độ 1/(k_BT) (J^-1); `V` là thể tích (m^3); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Hệ chính tắc (N, V, T không đổi)

*Ghi chú:* Atkins Focus 13C, McQuarrie ch.17. Với khí lí tưởng đơn nguyên tử, công thức này cho ngay U - U(0) = (3/2)nRT. Chương trình Việt Nam đưa ra kết quả này bằng thuyết động học chứ không qua hàm phân bố; dạng ⟨E⟩ = -∂lnZ/∂β đã có ở file vật lí đại học quốc tế (physics.dai-hoc.thong-ke-nang-cao.nang-luong-trung-binh-tu-z), bản này viết theo quy ước hoá học với mốc U(0) - mốc bắt buộc khi lập bảng hàm nhiệt động.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.noi-nang-tu-ham-phan-bo` · lớp 13 · #nhiet-dong-thong-ke #noi-nang #intl-undergrad</sub>

---

**Phương trình Sackur - Tetrode** — *Sackur - Tetrode equation*

$$S_{m} = R\ln\!\left(\frac{e^{5/2}\,V_{m}}{N_{A}\Lambda^{3}}\right) = R\ln\!\left(\frac{e^{5/2}k_{B}T}{p\,\Lambda^{3}}\right),\qquad \Lambda = \frac{h}{\sqrt{2\pi m k_{B}T}}$$

Trong đó: `S_m` là entropy mol của khí lí tưởng đơn nguyên tử (J/(mol.K)); `R` là hằng số khí (J/(mol.K)); `V_m` là thể tích mol (m^3/mol); `N_A` là hằng số Avogadro (mol^-1); `Λ` là bước sóng nhiệt de Broglie (m); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `p` là áp suất (Pa); `h` là hằng số Planck (J.s); `m` là khối lượng một nguyên tử (kg).

*Điều kiện:* Khí lí tưởng ĐƠN NGUYÊN TỬ (chỉ có đóng góp tịnh tiến, q^E = g_0); áp dụng ở nhiệt độ đủ cao để dùng xấp xỉ liên tục

*Ghi chú:* Atkins Focus 13E. Kiểm chứng: argon ở 298.15 K, 1 bar cho S_m = 154.8 J/(mol.K), khớp rất tốt với giá trị nhiệt lượng kế - một trong những thắng lợi lớn nhất của nhiệt động lực học thống kê. R = 8.314462618 J/(mol.K), N_A = 6.02214076e23 mol^-1. Kho đã có công thức này ở file vật lí đại học quốc tế (physics.dai-hoc.thong-ke-nang-cao.cong-thuc-sackur-tetrode) viết cho hệ N hạt; bản hoá học ở đây viết cho entropy MOL theo V_m hoặc theo áp suất p - dạng dùng trực tiếp để so với entropy chuẩn trong bảng nhiệt hoá học.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.phuong-trinh-sackur-tetrode` · lớp 13 · #nhiet-dong-thong-ke #sackur-tetrode #entropy #intl-undergrad</sub>

---

**Hàm phân bố chính tắc của hệ N phân tử** — *Canonical partition function of an N-particle system*

$$Q = \frac{q^{N}}{N!}\ (\text{hạt không phân biệt được});\qquad Q = q^{N}\ (\text{hạt định xứ, phân biệt được})$$

Trong đó: `Q` là hàm phân bố chính tắc của hệ (); `q` là hàm phân bố của một phân tử (); `N` là số phân tử trong hệ ().

*Điều kiện:* Các phân tử độc lập nhau (khí lí tưởng); thừa số N! chỉ đúng khi số trạng thái khả dụng lớn hơn nhiều số phân tử (giới hạn Maxwell - Boltzmann)

*Ghi chú:* Atkins Focus 13B, McQuarrie ch.17. Thừa số 1/N! chính là lời giải cho nghịch lí Gibbs về entropy trộn hai khí giống nhau và là nguồn gốc số hạng '5/2' trong phương trình Sackur - Tetrode. Kho đã có tổng thống kê của hệ nhiều hạt ở file vật lí đại học quốc tế (physics.dai-hoc.thong-ke-nang-cao.tong-thong-ke-he-nhieu-hat); bản ghi này nhấn mạnh sự phân biệt hạt định xứ / không phân biệt được theo cách trình bày của hoá lí.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.ham-phan-bo-chinh-tac` · lớp 13 · #nhiet-dong-thong-ke #ham-phan-bo-chinh-tac #intl-undergrad</sub>

---

**Hàm phân bố dao động** — *Vibrational partition function*

$$q^{\mathrm{V}} = \frac{1}{1 - e^{-hc\tilde{\nu}/k_{B}T}};\qquad q^{\mathrm{V}}_{\text{đa nguyên tử}} = \prod_{i}\frac{1}{1 - e^{-hc\tilde{\nu}_{i}/k_{B}T}}$$

Trong đó: `q^V` là hàm phân bố dao động (); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `ṽ` là số sóng dao động (cm^-1); `ṽ_i` là số sóng của dao động chuẩn tắc thứ i (cm^-1); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Dao động tử điều hoà với các mức cách đều; năng lượng đo từ mức v = 0 (đã trừ năng lượng điểm không); tổng cấp số nhân hội tụ chính xác

*Ghi chú:* Atkins Focus 13B. Ở nhiệt độ phòng, với ṽ khoảng 2000-3000 cm^-1 thì q^V rất gần 1 - hầu như mọi phân tử ở mức dao động cơ bản, nên dao động đóng góp không đáng kể vào nhiệt dung. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.ham-phan-bo-dao-dong` · lớp 13 · #nhiet-dong-thong-ke #ham-phan-bo #dao-dong #intl-undergrad</sub>

---

**Hàm phân bố điện tử** — *Electronic partition function*

$$q^{\mathrm{E}} = g_{0} + g_{1}e^{-\varepsilon_{1}/k_{B}T} + \cdots \approx g_{0} = 2S+1$$

Trong đó: `q^E` là hàm phân bố điện tử (); `g_0` là bậc suy biến của trạng thái điện tử cơ bản (); `g_1` là bậc suy biến của trạng thái điện tử kích thích thứ nhất (); `ε_1` là năng lượng của trạng thái kích thích thứ nhất (J); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `S` là số lượng tử spin tổng của trạng thái cơ bản ().

*Điều kiện:* Khoảng cách các mức điện tử thường rất lớn (hàng chục nghìn cm^-1) nên chỉ trạng thái cơ bản đóng góp; ngoại lệ quan trọng: NO và các gốc tự do có mức spin - obitan thấp, ion kim loại chuyển tiếp

*Ghi chú:* Atkins Focus 13B. Ví dụ: O2 có trạng thái cơ bản triplet nên q^E = 3; NO có hai mức 2Pi(1/2) và 2Pi(3/2) cách nhau 121 cm^-1 nên q^E phụ thuộc nhiệt độ rõ rệt. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.ham-phan-bo-dien-tu` · lớp 13 · #nhiet-dong-thong-ke #ham-phan-bo #dien-tu #intl-undergrad</sub>

---

**Hàm phân bố phân tử và phân bố Boltzmann** — *Molecular partition function and the Boltzmann distribution*

$$q = \sum_{i}g_{i}\,e^{-\varepsilon_{i}/k_{B}T} = \sum_{\text{trạng thái}}e^{-\beta\varepsilon};\qquad \frac{N_{i}}{N} = \frac{g_{i}e^{-\varepsilon_{i}/k_{B}T}}{q},\qquad \beta = \frac{1}{k_{B}T}$$

Trong đó: `q` là hàm phân bố phân tử (); `g_i` là bậc suy biến của mức năng lượng thứ i (); `ε_i` là năng lượng của mức thứ i (tính từ mức thấp nhất) (J); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `N_i` là số phân tử ở mức thứ i (); `N` là tổng số phân tử (); `β` là nghịch đảo nhiệt độ nhiệt động (J^-1).

*Điều kiện:* Hệ ở cân bằng nhiệt; các mức năng lượng đo từ mức cơ bản (ε_0 = 0) nên q -> g_0 khi T -> 0 và q -> tổng số trạng thái khi T -> vô cùng

*Ghi chú:* Atkins Focus 13A, McQuarrie ch.17. q đo 'số trạng thái thực sự có thể tiếp cận được' ở nhiệt độ T - đại lượng trung tâm của nhiệt động lực học thống kê. Chương trình Việt Nam (GDPT 2018 và hoá lí đại học trong kho) chỉ có công thức Boltzmann S = k lnW, không có hàm phân bố; tổng thống kê Z của hệ đã có ở file vật lí đại học quốc tế (physics.dai-hoc.thong-ke-nang-cao.tong-thong-ke-z), còn bản ghi này là hàm phân bố của MỘT PHÂN TỬ q - đại lượng mà hoá học dùng để tách thành q^T q^R q^V q^E.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.ham-phan-bo-phan-tu` · lớp 13 · #nhiet-dong-thong-ke #ham-phan-bo #boltzmann #intl-undergrad</sub>

---

**Hàm phân bố quay của phân tử thẳng và phi tuyến** — *Rotational partition function of linear and non-linear molecules*

$$q^{\mathrm{R}}_{\text{thẳng}} = \frac{k_{B}T}{\sigma\,hcB};\qquad q^{\mathrm{R}}_{\text{phi tuyến}} = \frac{1}{\sigma}\left(\frac{k_{B}T}{hc}\right)^{3/2}\sqrt{\frac{\pi}{ABC}}$$

Trong đó: `q^R` là hàm phân bố quay (); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `σ` là số đối xứng của phân tử (); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `B` là hằng số quay của phân tử thẳng (cm^-1); `A` là hằng số quay thứ nhất của phân tử phi tuyến (cm^-1); `C` là hằng số quay thứ ba của phân tử phi tuyến (cm^-1).

*Điều kiện:* Xấp xỉ nhiệt độ cao T lớn hơn nhiều so với nhiệt độ đặc trưng quay (đúng ở nhiệt độ phòng cho hầu hết phân tử trừ H2); σ = 1 (HCl), 2 (H2, CO2), 3 (NH3), 12 (CH4, benzene)

*Ghi chú:* Atkins Focus 13B, McQuarrie ch.18. Số đối xứng σ tránh đếm trùng các cấu hình không phân biệt được khi quay - đây là điểm dễ sai nhất khi tính entropy quay. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.ham-phan-bo-quay` · lớp 13 · #nhiet-dong-thong-ke #ham-phan-bo #quay #intl-undergrad</sub>

---

**Hàm phân bố tịnh tiến và bước sóng nhiệt de Broglie** — *Translational partition function and the thermal de Broglie wavelength*

$$q^{\mathrm{T}} = \frac{V}{\Lambda^{3}};\qquad \Lambda = \frac{h}{\sqrt{2\pi m k_{B}T}}$$

Trong đó: `q^T` là hàm phân bố tịnh tiến (); `V` là thể tích bình chứa (m^3); `Λ` là bước sóng nhiệt de Broglie (m); `h` là hằng số Planck (J.s); `m` là khối lượng một phân tử (kg); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Các mức tịnh tiến rất sát nhau nên tổng được thay bằng tích phân (đúng khi Λ nhỏ hơn nhiều so với kích thước bình); suy ra từ bài toán hạt trong hộp ba chiều

*Ghi chú:* Atkins Focus 13B, McQuarrie ch.18. Với N2 ở 298 K, Λ khoảng 19 pm; lấy thể tích MOL ở 1 bar (V_m = 24.8 L) thì q^T khoảng 3.5e30 - số trạng thái tịnh tiến khả dụng là khổng lồ (lưu ý q^T tỉ lệ thuận với V nên luôn phải nói rõ thể tích). Khi Λ so sánh được với khoảng cách phân tử thì hiệu ứng lượng tử trở nên quan trọng (khí suy biến). Kho đã có bước sóng nhiệt de Broglie ở file vật lí (physics.dai-hoc.thong-ke-nang-cao.buoc-song-nhiet-de-broglie) và q^T ở file olympiad (chemistry.dai-hoc.icho-luong-tu.ham-phan-bo-tinh-tien); bản ghi này gộp cả hai và đặt trong mạch tách thừa số hàm phân bố của Atkins.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.ham-phan-bo-tinh-tien` · lớp 13 · #nhiet-dong-thong-ke #ham-phan-bo #tinh-tien #intl-undergrad</sub>

---

**Nhiệt độ đặc trưng quay và nhiệt độ đặc trưng dao động** — *Characteristic rotational and vibrational temperatures*

$$\theta_{R} = \frac{hcB}{k_{B}};\qquad \theta_{V} = \frac{hc\tilde{\nu}}{k_{B}}$$

Trong đó: `θ_R` là nhiệt độ đặc trưng quay (K); `θ_V` là nhiệt độ đặc trưng dao động (K); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `B` là hằng số quay (cm^-1); `ṽ` là số sóng dao động (cm^-1); `k_B` là hằng số Boltzmann (J/K).

*Điều kiện:* T lớn hơn nhiều so với θ thì bậc tự do tương ứng được 'kích hoạt' hoàn toàn và đóng góp theo định lí phân bố đều; T nhỏ hơn nhiều so với θ thì bậc tự do bị 'đóng băng'

*Ghi chú:* Atkins Focus 13B. hc/k_B = 1.43878 cm.K nên θ = 1.43878 × (giá trị số sóng theo cm^-1). Ví dụ N2: θ_R = 2.88 K nhưng θ_V = 3374 K - giải thích vì sao ở 298 K nhiệt dung mol của N2 là (5/2)R chứ không phải (7/2)R. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.nhiet-do-dac-trung` · lớp 13 · #nhiet-dong-thong-ke #nhiet-do-dac-trung #nhiet-dung #intl-undergrad</sub>

---

**Tách thừa số hàm phân bố theo các dạng chuyển động** — *Factorisation of the molecular partition function*

$$q = q^{\mathrm{T}}\,q^{\mathrm{R}}\,q^{\mathrm{V}}\,q^{\mathrm{E}};\qquad \varepsilon = \varepsilon^{\mathrm{T}} + \varepsilon^{\mathrm{R}} + \varepsilon^{\mathrm{V}} + \varepsilon^{\mathrm{E}}$$

Trong đó: `q` là hàm phân bố phân tử toàn phần (); `q^T` là hàm phân bố tịnh tiến (); `q^R` là hàm phân bố quay (); `q^V` là hàm phân bố dao động (); `q^E` là hàm phân bố điện tử (); `ε` là năng lượng phân tử (J); `ε^T` là năng lượng tịnh tiến (J); `ε^R` là năng lượng quay (J); `ε^V` là năng lượng dao động (J); `ε^E` là năng lượng điện tử (J).

*Điều kiện:* Các dạng chuyển động coi như độc lập nhau (năng lượng cộng tính) - xấp xỉ tốt khi bỏ qua tương tác quay - dao động

*Ghi chú:* Atkins Focus 13B, McQuarrie ch.18. Vì năng lượng cộng tính nên hàm mũ tách thành tích, do đó hàm phân bố tách thừa số. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.tach-thua-so-ham-phan-bo` · lớp 13 · #nhiet-dong-thong-ke #ham-phan-bo #intl-undergrad</sub>

---

**Entropy dư của tinh thể ở 0 K** — *Residual entropy of a crystal at 0 K*

$$S_{m}(0) = R\ln s$$

Trong đó: `S_m(0)` là entropy dư mol ở 0 K (J/(mol.K)); `R` là hằng số khí (J/(mol.K)); `s` là số định hướng (cấu hình) tương đương của mỗi phân tử trong tinh thể ().

*Điều kiện:* Tinh thể mất trật tự định hướng bị 'đóng băng' khi làm lạnh; các cấu hình có năng lượng gần bằng nhau

*Ghi chú:* Atkins Focus 13E. Ví dụ CO có hai định hướng CO/OC nên S_m(0) = R ln2 = 5.76 J/(mol.K) (thực nghiệm khoảng 5 J/(mol.K)); nước đá có s = 3/2 cho mỗi phân tử, S_m(0) = R ln(3/2) = 3.4 J/(mol.K) (thực nghiệm 3.4). Đây là trường hợp nguyên lí thứ ba bị 'vi phạm biểu kiến' - nội dung chuẩn của giáo trình quốc tế nhưng không có trong kho Việt Nam.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.entropy-du-tinh-the` · lớp 13 · #nhiet-dong-thong-ke #entropy-du #nguyen-li-iii #intl-undergrad</sub>

---

**Hằng số cân bằng tính từ hàm phân bố** — *Equilibrium constant from partition functions*

$$K = \left(\prod_{J}\left(\frac{q_{J}^{\circ}}{N_{A}}\right)^{\nu_{J}}\right)e^{-\Delta_{r}E_{0}/RT}$$

Trong đó: `K` là hằng số cân bằng nhiệt động (); `q_J°` là hàm phân bố chuẩn (tính cho một mol) của chất J (mol^-1); `N_A` là hằng số Avogadro (mol^-1); `ν_J` là hệ số tỉ lượng của chất J (dương cho sản phẩm, âm cho chất đầu) (); `Δ_rE_0` là hiệu năng lượng giữa các mức cơ bản của sản phẩm và chất đầu ở 0 K (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Phản ứng pha khí giữa các khí lí tưởng; các hàm phân bố tính ở áp suất chuẩn p° = 1 bar; mọi năng lượng đo từ mức cơ bản của mỗi chất

*Ghi chú:* Atkins Focus 13F, McQuarrie ch.18. Ý nghĩa: hằng số cân bằng được tính HOÀN TOÀN từ dữ liệu phổ (khối lượng, hằng số quay, số sóng dao động, năng lượng phân li) mà không cần đo nhiệt hoá học - đây là điểm mạnh nhất của nhiệt động lực học thống kê. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.hang-so-can-bang-tu-ham-phan-bo` · lớp 13 · #nhiet-dong-thong-ke #hang-so-can-bang #intl-undergrad</sub>

---

**Đóng góp dao động vào nhiệt dung theo mô hình Einstein** — *Vibrational contribution to the heat capacity (Einstein model)*

$$C_{Vm}^{\mathrm{vib}} = R\left(\frac{\theta_{V}}{T}\right)^{2}\frac{e^{\theta_{V}/T}}{\left(e^{\theta_{V}/T}-1\right)^{2}};\qquad C_{Vm}^{\mathrm{tt}} = 3R\left(\frac{\theta_{E}}{T}\right)^{2}\frac{e^{\theta_{E}/T}}{\left(e^{\theta_{E}/T}-1\right)^{2}}$$

Trong đó: `C_Vm^vib` là đóng góp của một dao động chuẩn tắc vào nhiệt dung mol đẳng tích (J/(mol.K)); `C_Vm^tt` là nhiệt dung mol đẳng tích của tinh thể theo mô hình Einstein (J/(mol.K)); `R` là hằng số khí (J/(mol.K)); `θ_V` là nhiệt độ đặc trưng dao động (K); `θ_E` là nhiệt độ Einstein của tinh thể (K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Mọi dao động coi như dao động tử điều hoà độc lập cùng tần số; khi T lớn hơn nhiều so với θ thì C tiến tới R (hoặc 3R - định luật Dulong - Petit); khi T nhỏ thì C giảm về 0

*Ghi chú:* Atkins Focus 13C, McQuarrie ch.18. Kho Việt Nam đã có mô hình Debye và định luật Dulong - Petit ở file vật lí đại học; bản này bổ sung mô hình EINSTEIN viết theo hàm phân bố dao động - dạng dùng trong hoá lí để tính đóng góp của từng dao động chuẩn tắc phân tử. Mô hình Einstein cho C giảm quá nhanh ở T thấp, mô hình Debye (T^3) mới đúng.

<sub>`chemistry.dai-hoc.nhiet-dong-thong-ke.nhiet-dung-einstein` · lớp 13 · #nhiet-dong-thong-ke #nhiet-dung #einstein #intl-undergrad</sub>

---

### Olympiad Hoá học: Cân bằng và phân tích (IChO)

**Phân số nồng độ alpha tổng quát cho axit đa nấc** — *General alpha expression for a polyprotic acid*

$$\alpha_{j}=\frac{[\mathrm{H}^{+}]^{n-j}\prod_{i=1}^{j}K_{ai}}{\sum_{k=0}^{n}[\mathrm{H}^{+}]^{n-k}\prod_{i=1}^{k}K_{ai}}$$

Trong đó: `\alpha_{j}` là phân số nồng độ của tiểu phân đã mất j proton (); `n` là số nấc phân li của axit (); `j` là số proton đã bị mất, chạy từ 0 đến n; `k` là chỉ số chạy trong tổng ở mẫu số; `i` là chỉ số chạy trong tích các hằng số nấc; `K_{ai}` là hằng số phân li của nấc thứ i (mol/L); `[\mathrm{H}^{+}]` là nồng độ cân bằng của ion hiđro (mol/L).

*Điều kiện:* Quy ước tích rỗng bằng 1 khi j = 0 hoặc k = 0. Tổng tất cả các alpha_j bằng 1

*Ghi chú:* Công thức tổng quát này cho phép tính nhanh nồng độ mọi dạng của H3PO4, H2CO3, EDTA... ở một pH cho trước - dạng bài tính toán đặc trưng của IChO. Kho Việt Nam chỉ liệt kê các nấc phân li riêng lẻ, không có công thức phân số tổng quát.

<sub>`chemistry.dai-hoc.icho-can-bang.phan-so-alpha-axit-da-nac` · lớp 13 · #icho #can-bang #phan-so-alpha #da-nac</sub>

---

### Olympiad Hoá học: Hoá lượng tử và nhiệt động thống kê (IChO)

**Hàm phân bố tịnh tiến của phân tử khí** — *Translational molecular partition function*

$$q_{\mathrm{tt}}=\left(\frac{2\pi m k_{B}T}{h^{2}}\right)^{3/2}V$$

Trong đó: `q_{\mathrm{tt}}` là hàm phân bố tịnh tiến của một phân tử (); `m` là khối lượng của một phân tử (kg); `k_{B}` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `h` là hằng số Planck (J*s); `V` là thể tích chứa khí (m^3).

*Điều kiện:* Khí lí tưởng, các mức tịnh tiến rất sát nhau nên tổng được thay bằng tích phân. Kết hợp với các hàm phân bố quay, dao động và electron để tính hằng số cân bằng từ dữ liệu phổ

*Ghi chú:* Tính hằng số cân bằng từ hàm phân bố là nội dung cấp độ 3 của IChO. Kho Việt Nam có công thức Boltzmann về entropy nhưng không có hàm phân bố phân tử.

<sub>`chemistry.dai-hoc.icho-luong-tu.ham-phan-bo-tinh-tien` · lớp 13 · #icho #nhiet-dong-thong-ke #ham-phan-bo #khi-li-tuong</sub>

---

**Mức năng lượng Hückel của hệ pi liên hợp mạch hở** — *Hückel energy levels of a linear conjugated pi system*

$$E_{j}=\alpha+2\beta\cos\left(\frac{j\pi}{N+1}\right),\qquad j=1,2,\dots,N$$

Trong đó: `E_{j}` là năng lượng của obitan phân tử pi thứ j (J); `\alpha` là tích phân Coulomb (năng lượng của obitan p cô lập) (J); `\beta` là tích phân cộng hưởng giữa hai nguyên tử liền kề, mang giá trị âm (J); `N` là số nguyên tử carbon trong mạch liên hợp (); `j` là chỉ số của obitan phân tử, chạy từ 1 đến N ().

*Điều kiện:* Áp dụng thuyết Hückel đơn giản: chỉ xét electron pi, bỏ qua tương tác giữa các nguyên tử không liền kề và bỏ qua tích phân xen phủ. Mạch hở (polyen thẳng)

*Ghi chú:* Thuyết Hückel là nội dung cấp độ 3 của IChO, dùng để tính năng lượng liên hợp và giải thích tính thơm. Kho đã có nghiệm Hückel cho hệ VÒNG (chemistry.dai-hoc.hoa-luong-tu.huckel-vong-frost, mức alpha + 2beta*cos(2*pi*j/N), điều kiện biên tuần hoàn nên các mức suy biến bậc hai); bản ghi này là nghiệm cho MẠCH HỞ với điều kiện biên hai đầu tự do, mẫu số là N+1 chứ không phải N và KHÔNG có mức nào suy biến. Không có trong chương trình GDPT 2018.

<sub>`chemistry.dai-hoc.icho-luong-tu.huckel-mach-ho` · lớp 13 · #icho #luong-tu #huckel #lien-hop</sub>

---

### Olympiad Hoá học: Động hoá học (IChO)

**Hiệu ứng đồng vị động học sơ cấp** — *Primary kinetic isotope effect*

$$\frac{k_{H}}{k_{D}}=\exp\!\left[\frac{h\left(\nu_{H}-\nu_{D}\right)}{2k_{B}T}\right]$$

Trong đó: `k_{H}` là hằng số tốc độ của hợp chất chứa hiđro nhẹ (); `k_{D}` là hằng số tốc độ của hợp chất chứa đơteri (); `h` là hằng số Planck (J*s); `\nu_{H}` là tần số dao động hoá trị của liên kết C-H (1/s); `\nu_{D}` là tần số dao động hoá trị của liên kết C-D (1/s); `k_{B}` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Áp dụng khi liên kết C-H bị đứt ở bước quyết định tốc độ. Xuất phát từ chênh lệch năng lượng điểm không. Hằng số: h = 6,62607015e-34 J s; k_B = 1,380649e-23 J/K (giá trị chính xác theo định nghĩa SI 2019). Ở 25 độ C tỉ số này thường vào khoảng 6 - 8

*Ghi chú:* Hiệu ứng đồng vị động học là công cụ suy luận cơ chế phản ứng, thuộc nội dung cấp độ 3 của IChO. Không có trong chương trình GDPT 2018 và chưa có trong kho. Khác bản chemistry.dai-hoc.dong-hoc-nang-cao.hieu-ung-dong-vi-dong-hoc trong kho về QUY ƯỚC KÝ HIỆU: bản đó viết theo SỐ SÓNG (cm^-1) nên có thêm thừa số c, còn bản IChO ở đây viết theo TẦN SỐ nu (Hz) nên không có c.

<sub>`chemistry.dai-hoc.icho-dong-hoc.hieu-ung-dong-vi-dong-hoc` · lớp 13 · #icho #dong-hoc #dong-vi #co-che</sub>

---

**Hằng số tốc độ biểu kiến của cơ chế Lindemann - Hinshelwood** — *Apparent rate constant of the Lindemann–Hinshelwood mechanism*

$$k_{\mathrm{uni}}=\frac{k_{1}k_{2}[\mathrm{M}]}{k_{-1}[\mathrm{M}]+k_{2}}$$

Trong đó: `k_{\mathrm{uni}}` là hằng số tốc độ biểu kiến của phản ứng đơn phân tử (1/s); `k_{1}` là hằng số tốc độ của bước hoạt hoá do va chạm (L/(mol*s)); `k_{-1}` là hằng số tốc độ của bước khử hoạt hoá (L/(mol*s)); `k_{2}` là hằng số tốc độ của bước phân huỷ phân tử đã hoạt hoá (1/s); `[\mathrm{M}]` là nồng độ của phân tử va chạm (chất khí thứ ba hoặc chính chất phản ứng) (mol/L).

*Điều kiện:* Áp dụng nguyên lí nồng độ ổn định cho phân tử đã hoạt hoá. Ở áp suất cao (nồng độ M lớn) phản ứng có bậc một biểu kiến; ở áp suất thấp phản ứng chuyển sang bậc hai

*Ghi chú:* Cơ chế Lindemann là ví dụ chuẩn giải thích vì sao phản ứng 'đơn phân tử' đổi bậc theo áp suất - nội dung cấp độ 3 của IChO. Kho Việt Nam có nguyên lí nồng độ ổn định (Bodenstein) nhưng không có cơ chế Lindemann và biểu thức k biểu kiến.

<sub>`chemistry.dai-hoc.icho-dong-hoc.co-che-lindemann` · lớp 13 · #icho #dong-hoc #lindemann #nong-do-on-dinh</sub>

---

**Nồng độ cực đại của chất trung gian trong phản ứng nối tiếp** — *Maximum intermediate concentration in consecutive first-order reactions*

$$\frac{[\mathrm{B}]_{\max}}{[\mathrm{A}]_{0}}=\left(\frac{k_{1}}{k_{2}}\right)^{\frac{k_{2}}{k_{2}-k_{1}}}$$

Trong đó: `[\mathrm{B}]_{\max}` là nồng độ lớn nhất của chất trung gian B (mol/L); `[\mathrm{A}]_{0}` là nồng độ ban đầu của chất đầu A (mol/L); `k_{1}` là hằng số tốc độ bước thứ nhất (1/s); `k_{2}` là hằng số tốc độ bước thứ hai (1/s).

*Điều kiện:* Sơ đồ A -> B -> C, hai bước bậc một không thuận nghịch, k1 khác k2, ban đầu chỉ có A

*Ghi chú:* Đi kèm công thức t_max, cặp công thức này là bộ câu hỏi tiêu chuẩn về phản ứng nối tiếp ở IChO. Không có trong kho công thức Việt Nam.

<sub>`chemistry.dai-hoc.icho-dong-hoc.nong-do-cuc-dai-trung-gian` · lớp 13 · #icho #dong-hoc #noi-tiep #cuc-dai</sub>

---

**Thời điểm nồng độ chất trung gian đạt cực đại trong phản ứng nối tiếp** — *Time of maximum intermediate concentration in consecutive first-order reactions*

$$t_{\max}=\frac{\ln\left(\dfrac{k_{2}}{k_{1}}\right)}{k_{2}-k_{1}}$$

Trong đó: `t_{\max}` là thời điểm nồng độ chất trung gian đạt giá trị lớn nhất (s); `k_{1}` là hằng số tốc độ của bước thứ nhất (A tạo thành B) (1/s); `k_{2}` là hằng số tốc độ của bước thứ hai (B tạo thành C) (1/s).

*Điều kiện:* Sơ đồ A -> B -> C với cả hai bước đều là bậc một và không thuận nghịch; ban đầu chỉ có A. Yêu cầu k1 khác k2 (khi k1 = k2 thì t_max = 1/k)

*Ghi chú:* Xác định thời điểm và nồng độ cực đại của chất trung gian là câu hỏi kinh điển của IChO động hoá học (ví dụ tối ưu thời gian dừng phản ứng). Kho Việt Nam có phương trình động học phản ứng nối tiếp nhưng không có công thức thời điểm cực đại.

<sub>`chemistry.dai-hoc.icho-dong-hoc.thoi-diem-cuc-dai-trung-gian` · lớp 13 · #icho #dong-hoc #noi-tiep #trung-gian</sub>

---

### Phổ học phân tử

**Độ rộng vạch phổ do thời gian sống hữu hạn** — *Lifetime broadening of spectral lines*

$$\delta E \approx \frac{\hbar}{\tau};\qquad \delta\tilde{\nu} = \frac{1}{2\pi c\,\tau} \approx \frac{5.31\ \mathrm{cm^{-1}}}{\tau/\mathrm{ps}}$$

Trong đó: `δE` là độ bất định năng lượng của mức (J); `ħ` là hằng số Planck rút gọn (J.s); `τ` là thời gian sống của trạng thái kích thích (s); `δṽ` là độ rộng vạch tính theo số sóng (cm^-1); `c` là tốc độ ánh sáng (cm/s).

*Điều kiện:* Độ rộng tự nhiên (Lorentz); ngoài ra còn có mở rộng Doppler và mở rộng do va chạm

*Ghi chú:* Atkins Focus 11A. Trạng thái sống càng ngắn thì vạch càng rộng - vì vậy vạch của trạng thái phân li nhanh hoặc trạng thái chuyển tiếp bị nhoè. Kho Việt Nam có nguyên lí bất định ở vật lí nhưng không có ứng dụng vào độ rộng vạch phổ phân tử.

<sub>`chemistry.dai-hoc.pho-hoc.do-rong-vach-do-thoi-gian-song` · lớp 13 · #pho-hoc #do-rong-vach #bat-dinh #intl-undergrad</sub>

---

**Chuyển đổi các đơn vị năng lượng dùng trong phổ học** — *Conversion between spectroscopic energy units*

$$1\ \mathrm{eV} = 8065.544\ \mathrm{cm^{-1}} = 96.485\ \mathrm{kJ\,mol^{-1}};\qquad 1\ \mathrm{cm^{-1}} = 11.9627\ \mathrm{J\,mol^{-1}};\qquad \frac{hc}{k_{B}} = 1.43878\ \mathrm{cm\,K}$$

Trong đó: `eV` là electronvolt (eV); `cm^-1` là số sóng (kayser) (cm^-1); `kJ/mol` là kilojoule trên mol (kJ/mol); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `k_B` là hằng số Boltzmann (J/K).

*Điều kiện:* Các hệ số quy đổi suy ra từ các hằng số cơ bản SI 2019 (đều là giá trị chính xác nên hệ số quy đổi chỉ bị làm tròn)

*Ghi chú:* Atkins Data section. Rất hữu ích khi so sánh: k_BT ở 298 K tương ứng khoảng 207 cm^-1 (2.48 kJ/mol) - nhỏ hơn nhiều so với khoảng cách mức dao động (hàng nghìn cm^-1) nhưng lớn hơn khoảng cách mức quay (vài cm^-1). Kho Việt Nam không có bảng quy đổi này.

<sub>`chemistry.dai-hoc.pho-hoc.doi-don-vi-nang-luong-pho-hoc` · lớp 13 · #pho-hoc #don-vi #hang-so #intl-undergrad</sub>

---

**Quan hệ năng lượng - tần số - bước sóng - số sóng** — *Relation between energy, frequency, wavelength and wavenumber*

$$\Delta E = h\nu = \frac{hc}{\lambda} = hc\,\tilde{\nu};\qquad \tilde{\nu} = \frac{1}{\lambda} = \frac{\nu}{c}$$

Trong đó: `ΔE` là hiệu năng lượng giữa hai mức (J); `h` là hằng số Planck (J.s); `ν` là tần số bức xạ (Hz); `c` là tốc độ ánh sáng trong chân không (cm/s); `λ` là bước sóng (cm); `ṽ` là số sóng (cm^-1).

*Điều kiện:* Bức xạ trong chân không; khi tính ṽ theo cm^-1 phải lấy λ theo cm và c theo cm/s

*Ghi chú:* Atkins Focus 11A. Số sóng ṽ (cm^-1, đọc là 'kayser') là đơn vị năng lượng chuẩn của phổ học phân tử quốc tế - chương trình Việt Nam hầu như chỉ dùng λ (nm) và ν (Hz), nên đây là khác biệt quy ước đáng kể. h = 6.62607015e-34 J.s, c = 2.99792458e10 cm/s (giá trị chính xác theo SI 2019).

<sub>`chemistry.dai-hoc.pho-hoc.nang-luong-tan-so-so-song` · lớp 13 · #pho-hoc #so-song #intl-undergrad</sub>

---

**Phân bố Boltzmann giữa các mức phổ có suy biến** — *Boltzmann population ratio between degenerate spectroscopic levels*

$$\frac{N_{2}}{N_{1}} = \frac{g_{2}}{g_{1}}\exp\!\left(-\frac{\Delta E}{k_{B}T}\right) = \frac{g_{2}}{g_{1}}\exp\!\left(-\frac{hc\,\Delta\tilde{\nu}}{k_{B}T}\right)$$

Trong đó: `N_2` là số phân tử ở mức trên (); `N_1` là số phân tử ở mức dưới (); `g_2` là bậc suy biến của mức trên (); `g_1` là bậc suy biến của mức dưới (); `ΔE` là hiệu năng lượng hai mức (J); `Δṽ` là hiệu năng lượng tính theo số sóng (cm^-1); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s).

*Điều kiện:* Hệ ở cân bằng nhiệt; áp dụng cho mọi loại mức (quay, dao động, electron, spin hạt nhân)

*Ghi chú:* Atkins Focus 11A và 13B. Kho Việt Nam có 'thừa số Boltzmann' ở file hoá quốc tế THPT nhưng chỉ dạng phần phân tử vượt E_a, và có phân bố Boltzmann theo thế năng ở vật lí; bản này bổ sung thừa số suy biến g và dạng tính theo số sóng - dạng bắt buộc khi giải thích cường độ vạch phổ quay. k_B = 1.380649e-23 J/K (chính xác).

<sub>`chemistry.dai-hoc.pho-hoc.phan-bo-boltzmann-muc-pho` · lớp 13 · #pho-hoc #boltzmann #cuong-do-vach #intl-undergrad</sub>

---

**Dịch chuyển Stokes của huỳnh quang** — *Stokes shift of fluorescence*

$$\Delta\tilde{\nu}_{\text{Stokes}} = \tilde{\nu}_{\text{hấp thụ}}^{\max} - \tilde{\nu}_{\text{phát xạ}}^{\max} > 0$$

Trong đó: `Δṽ_Stokes` là dịch chuyển Stokes (cm^-1); `ṽ_hấp thụ` là số sóng cực đại của dải hấp thụ (cm^-1); `ṽ_phát xạ` là số sóng cực đại của dải huỳnh quang (cm^-1).

*Điều kiện:* Phân tử trong dung dịch; huỳnh quang phát ra từ mức dao động thấp nhất của S1 (quy tắc Kasha)

*Ghi chú:* Atkins Focus 13B, Lakowicz ch.1. Nguyên nhân: hồi phục dao động và tái định hướng dung môi trước khi phát xạ - do đó huỳnh quang luôn ở bước sóng DÀI hơn hấp thụ. Phổ huỳnh quang thường là ảnh gương của phổ hấp thụ (hệ quả của nguyên lí Franck - Condon). Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.dich-chuyen-stokes-huynh-quang` · lớp 13 · #pho-hoc #huynh-quang #stokes #intl-undergrad</sub>

---

**Hiệu suất lượng tử huỳnh quang** — *Fluorescence quantum yield*

$$\Phi_{F} = \frac{\text{số photon phát ra}}{\text{số photon hấp thụ}} = \frac{k_{F}}{k_{F} + k_{IC} + k_{ISC} + k_{q}[Q]}$$

Trong đó: `Φ_F` là hiệu suất lượng tử huỳnh quang (); `k_F` là hằng số tốc độ phát huỳnh quang (s^-1); `k_IC` là hằng số tốc độ chuyển nội (internal conversion) (s^-1); `k_ISC` là hằng số tốc độ chuyển hệ giao (intersystem crossing) (s^-1); `k_q` là hằng số tốc độ dập tắt lưỡng phân tử (L/(mol.s)); `[Q]` là nồng độ chất dập tắt (mol/L).

*Điều kiện:* Trạng thái kích thích singlet S1 khử kích thích theo các kênh song song bậc một (hoặc giả bậc một)

*Ghi chú:* Atkins Focus 13B, Lakowicz ch.1. 0 <= Φ_F <= 1. Đây là đại lượng trung tâm của quang hoá học và hoá sinh vật lí quốc tế; kho Việt Nam không có bản ghi nào về huỳnh quang định lượng (hiệu suất lượng tử duy nhất xuất hiện trong kho là hiệu suất lượng tử của phản ứng quang hoá, một khái niệm khác). Ví dụ: fluorescein trong dung dịch kiềm có Φ_F gần 0.9, còn tryptophan trong nước chỉ khoảng 0.13.

<sub>`chemistry.dai-hoc.pho-hoc.hieu-suat-luong-tu-huynh-quang` · lớp 13 · #pho-hoc #huynh-quang #hieu-suat-luong-tu #intl-undergrad</sub>

---

**Phương trình Stern - Volmer về dập tắt huỳnh quang** — *Stern - Volmer equation for fluorescence quenching*

$$\frac{\Phi_{F}^{0}}{\Phi_{F}} = \frac{I_{0}}{I} = \frac{\tau_{0}}{\tau} = 1 + K_{SV}[Q];\qquad K_{SV} = k_{q}\tau_{0}$$

Trong đó: `Φ_F^0` là hiệu suất lượng tử khi không có chất dập tắt (); `Φ_F` là hiệu suất lượng tử khi có chất dập tắt (); `I_0` là cường độ huỳnh quang khi không có chất dập tắt (); `I` là cường độ huỳnh quang khi có chất dập tắt (); `τ_0` là thời gian sống khi không có chất dập tắt (s); `τ` là thời gian sống khi có chất dập tắt (s); `K_SV` là hằng số Stern - Volmer (L/mol); `[Q]` là nồng độ chất dập tắt (mol/L); `k_q` là hằng số tốc độ dập tắt lưỡng phân tử (L/(mol.s)).

*Điều kiện:* Dập tắt động (va chạm); đồ thị I_0/I theo [Q] là đường thẳng có hệ số góc K_SV. Nếu chỉ cường độ giảm mà thời gian sống không đổi thì đó là dập tắt tĩnh (tạo phức)

*Ghi chú:* Atkins Focus 13B, Lakowicz ch.8. So sánh đồ thị theo cường độ và theo thời gian sống là cách phân biệt dập tắt động với dập tắt tĩnh. Khi k_q đạt giới hạn khuếch tán (khoảng 7e9 - 1e10 L/(mol.s) trong nước ở 25 độ C) thì mỗi va chạm đều gây dập tắt. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.phuong-trinh-stern-volmer` · lớp 13 · #pho-hoc #huynh-quang #stern-volmer #intl-undergrad</sub>

---

**Thời gian sống huỳnh quang quan sát và thời gian sống bức xạ** — *Observed and radiative fluorescence lifetimes*

$$\tau = \frac{1}{\sum_{i}k_{i}};\qquad \tau_{0} = \frac{1}{k_{F}};\qquad \Phi_{F} = \frac{\tau}{\tau_{0}} = k_{F}\tau;\qquad I(t) = I_{0}e^{-t/\tau}$$

Trong đó: `τ` là thời gian sống huỳnh quang quan sát được (s); `τ_0` là thời gian sống bức xạ (khi không có kênh không bức xạ) (s); `k_i` là hằng số tốc độ của kênh khử kích thích thứ i (s^-1); `k_F` là hằng số tốc độ phát huỳnh quang (s^-1); `Φ_F` là hiệu suất lượng tử huỳnh quang (); `I(t)` là cường độ huỳnh quang tại thời điểm t (); `I_0` là cường độ huỳnh quang tại t = 0 (); `t` là thời gian (s).

*Điều kiện:* Khử kích thích tuân theo động học bậc một; kích thích bằng xung ngắn

*Ghi chú:* Atkins Focus 13B, Lakowicz ch.1. Huỳnh quang có τ khoảng 1-100 ns còn lân quang có τ khoảng micro giây tới giây (vì chuyển dời triplet - singlet bị cấm spin). Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.thoi-gian-song-huynh-quang` · lớp 13 · #pho-hoc #huynh-quang #thoi-gian-song #intl-undergrad</sub>

---

**Cấu trúc siêu tinh tế trong phổ EPR** — *Hyperfine structure in EPR spectra*

$$M = 2nI + 1;\qquad B_{\text{cộng hưởng}} = \frac{h\nu}{g\mu_{B}} - a\,m_{I}$$

Trong đó: `M` là số vạch siêu tinh tế (); `n` là số hạt nhân tương đương ghép với electron độc thân (); `I` là spin của hạt nhân đó (); `B_cộng hưởng` là cảm ứng từ tại đó xảy ra cộng hưởng (T); `h` là hằng số Planck (J.s); `ν` là tần số vi sóng (Hz); `g` là hệ số g (); `μ_B` là magneton Bohr (J/T); `a` là hằng số ghép siêu tinh tế (T); `m_I` là hình chiếu spin hạt nhân ().

*Điều kiện:* Electron độc thân ghép với các hạt nhân từ lân cận (1H có I = 1/2, 14N có I = 1)

*Ghi chú:* Atkins Focus 12E. Ví dụ gốc methyl CH3 cho 4 vạch (n = 3, I = 1/2) tỉ lệ 1:3:3:1; gốc benzene anion cho 7 vạch. Hằng số a tỉ lệ với mật độ spin trên nguyên tử tương ứng (quan hệ McConnell) nên EPR cho bản đồ phân bố electron độc thân. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.cau-truc-sieu-tinh-te-epr` · lớp 13 · #pho-hoc #epr #sieu-tinh-te #intl-undergrad</sub>

---

**Điều kiện cộng hưởng EPR và hệ số g** — *EPR resonance condition and the g factor*

$$h\nu = g\,\mu_{B}B_{0};\qquad g = \frac{h\nu}{\mu_{B}B_{0}};\qquad g_{e} = 2.00232$$

Trong đó: `h` là hằng số Planck (J.s); `ν` là tần số vi sóng (Hz); `g` là hệ số g của tiểu phân thuận từ (); `μ_B` là magneton Bohr (J/T); `B_0` là cảm ứng từ cộng hưởng (T); `g_e` là hệ số g của electron tự do ().

*Điều kiện:* Tiểu phân có electron độc thân (gốc tự do, ion kim loại chuyển tiếp, trạng thái triplet); phổ EPR thường ghi ở băng X (khoảng 9.5 GHz, B_0 khoảng 0.34 T)

*Ghi chú:* Atkins Focus 12E. μ_B = 9.2740100657e-24 J/T và g_e = 2.00231930436092 (CODATA 2022). Độ lệch của g khỏi g_e phản ánh đóng góp của momen obitan, nên g là 'dấu vân tay' của môi trường electron độc thân - vai trò tương tự độ dịch chuyển hoá học trong NMR. Kho Việt Nam không có EPR.

<sub>`chemistry.dai-hoc.pho-hoc.dieu-kien-cong-huong-epr` · lớp 13 · #pho-hoc #epr #he-so-g #intl-undergrad</sub>

---

**Chuyển đổi độ dịch chuyển hoá học sang hertz** — *Converting chemical shift from ppm to hertz*

$$\Delta\nu\ (\mathrm{Hz}) = \delta\ (\mathrm{ppm}) \times \frac{\nu_{\text{máy}}\ (\mathrm{MHz})}{1};\qquad \Delta\nu_{2} = \Delta\nu_{1}\frac{\nu_{\text{máy},2}}{\nu_{\text{máy},1}}$$

Trong đó: `Δν` là khoảng cách tần số so với chất chuẩn (Hz); `δ` là độ dịch chuyển hoá học (ppm); `ν_máy` là tần số làm việc của máy phổ (MHz); `Δν_1` là khoảng cách tần số trên máy thứ nhất (Hz); `Δν_2` là khoảng cách tần số trên máy thứ hai (Hz).

*Điều kiện:* Áp dụng cho cùng loại hạt nhân; khác biệt về độ dịch chuyển hoá học (tính bằng Hz) tỉ lệ thuận với B_0, còn hằng số ghép J thì không

*Ghi chú:* Atkins Focus 12B, Pavia ch.5. Đây là lí do máy từ trường càng cao càng dễ phân giải: tỉ số Δν/J tăng, phổ chuyển từ bậc hai sang bậc một. Ví dụ δ = 2.0 ppm trên máy 400 MHz ứng với 800 Hz. Kho Việt Nam không có. PHẠM VI: A-Level và IB chỉ yêu cầu đọc δ theo ppm, không yêu cầu quy đổi ppm sang Hz hay so sánh hai máy khác từ trường, nên bản ghi này chỉ gắn intl-undergrad.

<sub>`chemistry.dai-hoc.pho-hoc.dich-chuyen-hoa-hoc-theo-hz` · lớp 13 · #pho-hoc #nmr #do-phan-giai #intl-undergrad</sub>

---

**Độ chênh dân số hai mức spin và độ nhạy NMR** — *Population difference between spin states and NMR sensitivity*

$$\frac{\Delta N}{N} \approx \frac{\gamma \hbar B_{0}}{2k_{B}T} = \frac{h\nu_{L}}{2k_{B}T}$$

Trong đó: `ΔN` là hiệu số hạt nhân giữa hai mức spin (); `N` là tổng số hạt nhân (); `γ` là tỉ số từ hồi chuyển (rad/(s.T)); `ħ` là hằng số Planck rút gọn (J.s); `B_0` là cảm ứng từ (T); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `h` là hằng số Planck (J.s); `ν_L` là tần số Larmor (Hz).

*Điều kiện:* Xấp xỉ nhiệt độ cao (ΔE nhỏ hơn nhiều so với k_BT), luôn đúng trong NMR thông thường

*Ghi chú:* Atkins Focus 12A. Ở 500 MHz và 300 K, ΔN/N chỉ khoảng 4e-5 - NMR là kĩ thuật phổ CỰC KÌ kém nhạy so với IR hay UV-Vis, giải thích vì sao phải tăng B_0, cộng dồn nhiều lần quét và dùng các kĩ thuật tăng cường phân cực. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.do-chenh-dan-so-nmr` · lớp 13 · #pho-hoc #nmr #do-nhay #intl-undergrad</sub>

---

**Độ dịch chuyển hoá học trong phổ NMR** — *Chemical shift in NMR spectroscopy*

$$\delta = \frac{\nu - \nu^{\circ}}{\nu_{\text{máy}}}\times 10^{6}\ (\mathrm{ppm});\qquad \delta \approx \left(\sigma^{\circ} - \sigma\right)\times 10^{6}$$

Trong đó: `δ` là độ dịch chuyển hoá học (ppm); `ν` là tần số cộng hưởng của hạt nhân khảo sát (Hz); `ν°` là tần số cộng hưởng của chất chuẩn (TMS) (Hz); `ν_máy` là tần số làm việc của máy phổ (Hz); `σ` là hằng số chắn của hạt nhân khảo sát (); `σ°` là hằng số chắn của hạt nhân trong chất chuẩn ().

*Điều kiện:* Chất chuẩn quy ước là tetramethylsilane (TMS) với δ = 0; thang δ không phụ thuộc cường độ từ trường của máy

*Ghi chú:* Atkins Focus 12B, Pavia ch.3-4. Hạt nhân bị CHẮN nhiều (mật độ electron cao) cộng hưởng ở δ nhỏ (phía trường cao). Khoảng δ thường gặp trong 1H NMR: 0.9-1.8 (alkyl), 2.0-2.5 (alpha-carbonyl), 3.3-4.5 (C-O), 4.5-6.5 (alkene), 6.5-8.5 (thơm), 9-10 (aldehyde), 10-13 (COOH). Đẳng thức thứ nhất (định nghĩa δ theo TMS) chính là nội dung A-Level và IB HL Structure 3.2, đã có ở file 04-intl-thpt; đẳng thức thứ hai (δ ≈ (σ° - σ)x10^6, nối δ với hằng số chắn) chỉ có ở bậc đại học. Chương trình GDPT 2018 không dạy NMR.

<sub>`chemistry.dai-hoc.pho-hoc.do-dich-chuyen-hoa-hoc-nmr` · lớp 13 · #pho-hoc #nmr #dich-chuyen-hoa-hoc #intl-undergrad</sub>

---

**Hằng số ghép spin - spin J** — *Spin-spin coupling constant J*

$$E_{\text{ghép}} = h\,J\,m_{I}(1)\,m_{I}(2);\qquad J \neq f(B_{0});\qquad ^{n}J:\ n = \text{số liên kết giữa hai hạt nhân}$$

Trong đó: `E_ghép` là năng lượng tương tác ghép giữa hai spin hạt nhân (J); `h` là hằng số Planck (J.s); `J` là hằng số ghép spin - spin (Hz); `m_I(1)` là hình chiếu spin của hạt nhân thứ nhất (); `m_I(2)` là hình chiếu spin của hạt nhân thứ hai (); `B_0` là cảm ứng từ của máy phổ (T); `n` là số liên kết ngăn cách hai hạt nhân ().

*Điều kiện:* Ghép truyền qua các electron liên kết (ghép vô hướng); thường chỉ quan sát được với n <= 3, trừ hệ liên hợp hoặc hệ cứng (ghép W)

*Ghi chú:* Atkins Focus 12C, Pavia ch.5. Điểm cốt lõi: J KHÔNG phụ thuộc cường độ từ trường (vì tương tác truyền qua electron chứ không phải qua trường ngoài) - đây là tiêu chí phân biệt vạch ghép với vạch của hai chất khác nhau. Giá trị điển hình trong 1H NMR: 2J(gem) 0-18 Hz; 3J(vic, tự do quay) 6-8 Hz; 3J(cis alkene) 6-12 Hz; 3J(trans alkene) 12-18 Hz; 3J(thơm ortho) 6-10 Hz. Kho Việt Nam không có. PHẠM VI: A-Level và IB chỉ mô tả hiện tượng tách vạch (quy tắc n+1) chứ không định lượng hằng số ghép J, nên bản ghi này chỉ gắn intl-undergrad.

<sub>`chemistry.dai-hoc.pho-hoc.hang-so-ghep-j-nmr` · lớp 13 · #pho-hoc #nmr #hang-so-ghep #intl-undergrad</sub>

---

**Phương trình Karplus liên hệ 3J với góc nhị diện** — *Karplus equation relating 3J to the dihedral angle*

$$^{3}\!J(\phi) = A\cos^{2}\phi + B\cos\phi + C$$

Trong đó: `3J` là hằng số ghép vicinal (qua ba liên kết) (Hz); `φ` là góc nhị diện H-C-C-H (độ); `A` là hệ số thực nghiệm chính (dương, khoảng 7-10 Hz) (Hz); `B` là hệ số thực nghiệm bậc nhất (thường âm, khoảng -1 Hz) (Hz); `C` là hệ số hằng thực nghiệm (khoảng 0-1.5 Hz) (Hz).

*Điều kiện:* Các hệ số A, B, C phụ thuộc hệ khảo sát (độ âm điện của nhóm thế, độ dài và góc liên kết) nên phải hiệu chuẩn theo từng lớp hợp chất

*Ghi chú:* Clayden ch.31, Pavia ch.5. Kết quả định tính quan trọng: 3J cực đại ở φ = 180 độ (anti, 10-16 Hz), lớn ở φ = 0 độ (syn, 8-10 Hz) và gần bằng 0 ở φ = 90 độ. Đây là công cụ chính để xác định cấu dạng vòng cyclohexane (ax-ax khoảng 10-13 Hz, ax-eq và eq-eq khoảng 2-5 Hz) và cấu hình tương đối trong hoá lập thể. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.phuong-trinh-karplus` · lớp 13 · #pho-hoc #nmr #karplus #cau-dang #intl-undergrad</sub>

---

**Quy tắc bội n + 1 và bội tổng quát trong NMR** — *The n + 1 multiplicity rule in NMR*

$$M = n + 1\ (I = \tfrac{1}{2});\qquad M = 2nI + 1\ (\text{tổng quát});\qquad M = \prod_{k}\left(n_{k}+1\right)\ (\text{nhiều nhóm khác nhau})$$

Trong đó: `M` là số vạch của cụm bội (multiplicity) (); `n` là số hạt nhân tương đương ở nguyên tử kề bên (); `I` là số lượng tử spin hạt nhân (); `n_k` là số hạt nhân tương đương thuộc nhóm thứ k ().

*Điều kiện:* Phổ bậc một (Δν lớn hơn nhiều so với J); các hạt nhân ghép phải KHÔNG tương đương với hạt nhân đang xét; ghép giữa các hạt nhân tương đương không quan sát được

*Ghi chú:* Atkins Focus 12C, Pavia ch.5. Cường độ các vạch trong cụm bội theo hệ số tam giác Pascal (1:1, 1:2:1, 1:3:3:1, ...) khi I = 1/2. Với deuteri (I = 1) thì một D cho 3 vạch cường độ bằng nhau. Dạng M = n + 1 là nội dung A-Level và IB HL (đã có ở file 04-intl-thpt dưới id chemistry.thpt.pho-phan-tich.quy-tac-n-cong-1); hai dạng tổng quát M = 2nI + 1 và tích các (n_k + 1) cho nhiều nhóm không tương đương chỉ có ở bậc đại học. Chương trình GDPT 2018 không dạy NMR.

<sub>`chemistry.dai-hoc.pho-hoc.quy-tac-boi-nmr` · lớp 13 · #pho-hoc #nmr #boi-vach #intl-undergrad</sub>

---

**Tần số Larmor và điều kiện cộng hưởng NMR** — *Larmor frequency and the NMR resonance condition*

$$\nu_{L} = \frac{\gamma B_{0}}{2\pi}\quad(\text{hạt nhân trần});\qquad \nu = \frac{\gamma B_{\text{loc}}}{2\pi} = \frac{(1-\sigma)\gamma B_{0}}{2\pi}\quad(\text{hạt nhân trong phân tử});\qquad \Delta E = \gamma\hbar B_{0} = h\nu_{L}$$

Trong đó: `ν_L` là tần số Larmor của hạt nhân trần (chưa bị chắn) (Hz); `ν` là tần số cộng hưởng thực tế của hạt nhân trong phân tử (Hz); `γ` là tỉ số từ hồi chuyển của hạt nhân (rad/(s.T)); `B_0` là cảm ứng từ của từ trường ngoài (T); `B_loc` là cảm ứng từ thực tế tại hạt nhân, B_loc = (1 - σ)B_0 (T); `σ` là hằng số chắn của hạt nhân trong phân tử (); `ΔE` là khoảng cách hai mức spin hạt nhân (J); `ħ` là hằng số Planck rút gọn (J.s); `h` là hằng số Planck (J.s).

*Điều kiện:* Hạt nhân có spin I khác 0 (1H, 13C, 19F, 31P có I = 1/2); từ trường tĩnh đồng nhất

*Ghi chú:* Atkins Focus 12A, Pavia ch.3. LƯU Ý quy ước: ν_L (hạt nhân trần) và ν (hạt nhân bị chắn trong phân tử) là HAI đại lượng khác nhau, chỉ trùng nhau khi σ = 0. Với 1H, γ/(2π) = 42.577 MHz/T (CODATA 2022); do đó máy 500 MHz ứng với B_0 khoảng 11.7 T. PHẠM VI: điều kiện cộng hưởng theo γ và B_0 KHÔNG thuộc syllabus A-Level hay IB (hai hệ này chỉ dạy phổ 1H NMR ở mức độ dịch chuyển hoá học, tích phân và quy tắc n+1), nên bản ghi này chỉ gắn intl-undergrad. Kho Việt Nam có phổ NMR mức phổ thông quốc tế ở file 04-intl-thpt (độ dịch chuyển hoá học, quy tắc n+1, tích phân) nhưng không có điều kiện cộng hưởng Larmor.

<sub>`chemistry.dai-hoc.pho-hoc.tan-so-larmor-nmr` · lớp 13 · #pho-hoc #nmr #larmor #intl-undergrad</sub>

---

**Dịch chuyển Raman Stokes và anti-Stokes** — *Stokes and anti-Stokes Raman shifts*

$$\tilde{\nu}_{\text{Stokes}} = \tilde{\nu}_{0} - \Delta\tilde{\nu}_{M};\qquad \tilde{\nu}_{\text{anti-Stokes}} = \tilde{\nu}_{0} + \Delta\tilde{\nu}_{M}$$

Trong đó: `ṽ_Stokes` là số sóng của vạch Stokes (cm^-1); `ṽ_anti-Stokes` là số sóng của vạch anti-Stokes (cm^-1); `ṽ_0` là số sóng của bức xạ laser kích thích (cm^-1); `Δṽ_M` là dịch chuyển Raman (bằng số sóng mức dao động hoặc quay của phân tử) (cm^-1).

*Điều kiện:* Tán xạ không đàn hồi của ánh sáng đơn sắc; quy tắc lọc lựa tổng thể của Raman là ĐỘ PHÂN CỰC phải biến thiên theo toạ độ dao động

*Ghi chú:* Atkins Focus 11C-11E. Dịch chuyển Raman không phụ thuộc bước sóng laser - đó là đại lượng đặc trưng cho phân tử. Vạch Rayleigh (không dịch chuyển) mạnh nhất. Kho Việt Nam không có phổ Raman.

<sub>`chemistry.dai-hoc.pho-hoc.pho-raman-dich-chuyen-stokes` · lớp 13 · #pho-hoc #raman #stokes #intl-undergrad</sub>

---

**Quy tắc loại trừ lẫn nhau giữa phổ IR và phổ Raman** — *Rule of mutual exclusion between IR and Raman spectra*

$$\text{Phân tử có tâm đối xứng} \Rightarrow \left(\text{hoạt động IR}\right) \cap \left(\text{hoạt động Raman}\right) = \varnothing$$

Trong đó: `hoạt động IR` là tập các dao động chuẩn tắc cho vạch hồng ngoại (); `hoạt động Raman` là tập các dao động chuẩn tắc cho vạch Raman ().

*Điều kiện:* Chỉ áp dụng cho phân tử CÓ tâm đối xứng (tâm nghịch đảo i): CO2, C2H4, N2, benzene, SF6

*Ghi chú:* Atkins Focus 11E. Dao động chẵn (g) hoạt động Raman, dao động lẻ (u) hoạt động IR. Đây là công cụ thực nghiệm mạnh để phân biệt đồng phân có và không có tâm đối xứng (ví dụ trans- và cis-[PtCl2(NH3)2]). Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.quy-tac-loai-tru-lan-nhau` · lớp 13 · #pho-hoc #raman #doi-xung #intl-undergrad</sub>

---

**Quy tắc lọc lựa và vị trí vạch của phổ quay Raman** — *Selection rules and line positions in rotational Raman spectroscopy*

$$\Delta J = 0,\pm 2;\qquad \tilde{\nu}_{S}(J) = \tilde{\nu}_{0} - 2B(2J+3),\ J = 0,1,2,\dots;\qquad \tilde{\nu}_{aS}(J) = \tilde{\nu}_{0} + 2B(2J-1),\ J = 2,3,\dots;\qquad \Delta\tilde{\nu}_{\text{hai vạch kề}} = 4B$$

Trong đó: `ΔJ` là biến thiên số lượng tử quay (); `ṽ_S` là số sóng của vạch Stokes trong nhánh quay S (J -> J + 2) (cm^-1); `ṽ_aS` là số sóng của vạch anti-Stokes trong nhánh quay O (J -> J - 2) (cm^-1); `ṽ_0` là số sóng của bức xạ laser kích thích (cm^-1); `B` là hằng số quay của phân tử (cm^-1); `J` là số lượng tử quay của trạng thái đầu (); `Δṽ_hai vạch kề` là khoảng cách giữa hai vạch quay Raman liên tiếp trong cùng một nhánh (cm^-1).

*Điều kiện:* Quay tử cứng thẳng; quy tắc lọc lựa TỔNG THỂ của Raman quay là độ phân cực phải BẤT ĐẲNG HƯỚNG - mọi phân tử đều thoả trừ con quay cầu (CH4, SF6); vạch Rayleigh ứng với ΔJ = 0

*Ghi chú:* Atkins Focus 11E, Hollas ch.5. Đối chiếu quan trọng với phổ quay vi sóng (ΔJ = ±1, khoảng cách 2B, đòi hỏi momen lưỡng cực vĩnh cửu): phổ quay RAMAN có ΔJ = ±2, khoảng cách vạch 4B, và không đòi hỏi momen lưỡng cực - nhờ đó N2, O2, H2, Cl2 tuy 'câm' trong vùng vi sóng vẫn cho phổ quay Raman, và đây là cách duy nhất đo độ dài liên kết của phân tử đồng hạch ở pha khí. Khoảng cách giữa vạch Stokes đầu tiên và vạch anti-Stokes đầu tiên là 12B chứ không phải 4B. Kho Việt Nam không có phổ quay Raman.

<sub>`chemistry.dai-hoc.pho-hoc.quy-tac-loc-lua-pho-quay-raman` · lớp 13 · #pho-raman #pho-quay #quy-tac-loc-lua #intl-undergrad</sub>

---

**Tỉ số cường độ vạch anti-Stokes và Stokes** — *Anti-Stokes to Stokes intensity ratio*

$$\frac{I_{\text{anti-Stokes}}}{I_{\text{Stokes}}} = \left(\frac{\tilde{\nu}_{0}+\Delta\tilde{\nu}_{M}}{\tilde{\nu}_{0}-\Delta\tilde{\nu}_{M}}\right)^{4}\exp\!\left(-\frac{hc\,\Delta\tilde{\nu}_{M}}{k_{B}T}\right)$$

Trong đó: `I_anti-Stokes` là cường độ vạch anti-Stokes (); `I_Stokes` là cường độ vạch Stokes (); `ṽ_0` là số sóng laser kích thích (cm^-1); `Δṽ_M` là dịch chuyển Raman (cm^-1); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Hệ ở cân bằng nhiệt; thừa số mũ 4 đến từ sự phụ thuộc tần số của tán xạ

*Ghi chú:* Atkins Focus 11E, Hollas ch.5. Vạch anti-Stokes luôn yếu hơn Stokes vì cần phân tử đã ở mức dao động kích thích. Đo tỉ số này cho phép xác định NHIỆT ĐỘ tại chỗ - nguyên lí của nhiệt kế Raman. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.ti-so-cuong-do-anti-stokes-stokes` · lớp 13 · #pho-hoc #raman #nhiet-do #intl-undergrad</sub>

---

**Dao động phi điều hoà và thế Morse** — *Anharmonic vibration and the Morse potential*

$$V(x) = D_{e}\left[1 - e^{-ax}\right]^{2};\qquad G(v) = \left(v+\tfrac{1}{2}\right)\tilde{\nu}_{e} - \left(v+\tfrac{1}{2}\right)^{2}\tilde{\nu}_{e}x_{e}$$

Trong đó: `V(x)` là thế năng Morse (J); `D_e` là độ sâu giếng thế (tính từ đáy giếng) (cm^-1); `a` là tham số bề rộng của thế Morse (m^-1); `x` là độ lệch khỏi độ dài liên kết cân bằng (m); `G(v)` là số hạng dao động (cm^-1); `v` là số lượng tử dao động (); `ṽ_e` là số sóng dao động điều hoà (cm^-1); `x_e` là hằng số phi điều hoà (không thứ nguyên) ().

*Điều kiện:* Mô hình Morse cho phân tử hai nguyên tử; số mức dao động là hữu hạn; áp dụng tốt cho các mức v thấp và trung bình

*Ghi chú:* Atkins Focus 11D. Hệ quả then chốt: các mức dao động HỘI TỤ khi v tăng (khoảng cách giảm dần), khác hẳn dao động tử điều hoà. Với thế Morse: D_e = ṽ_e/(4x_e). Ví dụ 1H35Cl: ṽ_e = 2990 cm^-1, ṽ_e x_e = 52.8 cm^-1. Kho Việt Nam không có phi điều hoà.

<sub>`chemistry.dai-hoc.pho-hoc.dao-dong-phi-dieu-hoa-morse` · lớp 13 · #pho-hoc #morse #phi-dieu-hoa #intl-undergrad</sub>

---

**Hiệu ứng đồng vị lên số sóng dao động** — *Isotope effect on the vibrational wavenumber*

$$\frac{\tilde{\nu}_{1}}{\tilde{\nu}_{2}} = \sqrt{\frac{\mu_{2}}{\mu_{1}}}\qquad (k_{f}\ \text{không đổi})$$

Trong đó: `ṽ_1` là số sóng dao động của đồng vị thứ nhất (cm^-1); `ṽ_2` là số sóng dao động của đồng vị thứ hai (cm^-1); `μ_1` là khối lượng rút gọn của đồng vị thứ nhất (kg); `μ_2` là khối lượng rút gọn của đồng vị thứ hai (kg); `k_f` là hằng số lực của liên kết (N/m).

*Điều kiện:* Thay đồng vị không đổi mặt thế năng electron nên hằng số lực k_f giữ nguyên (hệ quả của xấp xỉ Born - Oppenheimer)

*Ghi chú:* Atkins Focus 11C. Phải dùng KHỐI LƯỢNG RÚT GỌN chứ không phải khối lượng nguyên tử: với C-H thì μ = 12x1/13 = 0.923 u, với C-D thì μ = 12x2/14 = 1.714 u, nên ṽ(C-D)/ṽ(C-H) = căn(0.923/1.714) = 0.734; C-H khoảng 3000 cm^-1 cho C-D khoảng 2200 cm^-1. Ước lượng thô 'chia cho căn 2' (ra 2120 cm^-1) chỉ đúng nếu coi nguyên tử carbon nặng vô hạn. Đây là cơ sở của việc gán vạch phổ bằng phép thế đồng vị và của hiệu ứng đồng vị động học. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.hieu-ung-dong-vi-tan-so-dao-dong` · lớp 13 · #pho-hoc #dong-vi #hong-ngoai #intl-undergrad</sub>

---

**Năng lượng phân li quang phổ D0 và độ sâu giếng thế De** — *Spectroscopic dissociation energy D0 versus well depth De*

$$D_{0} = D_{e} - E_{\mathrm{ZPE}} = D_{e} - \tfrac{1}{2}\tilde{\nu}_{e} + \tfrac{1}{4}\tilde{\nu}_{e}x_{e}$$

Trong đó: `D_0` là năng lượng phân li đo từ mức dao động v = 0 (đại lượng đo được) (cm^-1); `D_e` là độ sâu giếng thế đo từ cực tiểu đường cong thế năng (cm^-1); `E_ZPE` là năng lượng điểm không (cm^-1); `ṽ_e` là số sóng dao động điều hoà (cm^-1); `x_e` là hằng số phi điều hoà ().

*Điều kiện:* Phân tử hai nguyên tử ở trạng thái electron cơ bản; D_0 là đại lượng thực nghiệm, D_e là đại lượng lí thuyết

*Ghi chú:* Atkins Focus 11D. Phân biệt D_0 và D_e là điểm bắt buộc trong giáo trình quốc tế: chỉ D_0 mới so sánh trực tiếp được với năng lượng liên kết nhiệt hoá học, còn D_e mới là đại lượng cho ra bởi tính toán lượng tử. Hai đồng vị của cùng một phân tử có cùng D_e nhưng D_0 khác nhau. Kho Việt Nam chỉ có 'năng lượng liên kết' nhiệt hoá học.

<sub>`chemistry.dai-hoc.pho-hoc.nang-luong-phan-li-d0-de` · lớp 13 · #pho-hoc #nang-luong-phan-li #diem-khong #intl-undergrad</sub>

---

**Ngoại suy Birge - Sponer xác định năng lượng phân li** — *Birge - Sponer extrapolation for the dissociation energy*

$$\Delta G_{v+1/2} = G(v+1) - G(v) = \tilde{\nu}_{e} - 2\tilde{\nu}_{e}x_{e}(v+1);\qquad D_{0} = \sum_{v=0}^{v_{\max}}\Delta G_{v+1/2}$$

Trong đó: `ΔG_{v+1/2}` là khoảng cách giữa hai mức dao động kề nhau (cm^-1); `G(v)` là số hạng dao động của mức v (cm^-1); `v` là số lượng tử dao động (); `ṽ_e` là số sóng dao động điều hoà (cm^-1); `x_e` là hằng số phi điều hoà (); `D_0` là năng lượng phân li từ mức v = 0 (cm^-1); `v_max` là số lượng tử dao động cao nhất còn liên kết ().

*Điều kiện:* Đồ thị ΔG theo (v + 1/2) là đường thẳng (giả thiết Morse); D_0 bằng diện tích dưới đường thẳng đó

*Ghi chú:* Atkins Focus 11D, Hollas ch.6. Phương pháp Birge - Sponer thường cho D_0 hơi lớn hơn giá trị thật vì đường ΔG thực tế cong xuống ở v lớn. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.ngoai-suy-birge-sponer` · lớp 13 · #pho-hoc #birge-sponer #phan-li #intl-undergrad</sub>

---

**Nhánh P, Q, R của phổ dao động - quay** — *P, Q and R branches of a vibration-rotation spectrum*

$$\tilde{\nu}_{R}(J) = \tilde{\nu}_{0} + 2B(J+1),\ J=0,1,\dots;\qquad \tilde{\nu}_{P}(J) = \tilde{\nu}_{0} - 2BJ,\ J=1,2,\dots;\qquad \tilde{\nu}_{Q} = \tilde{\nu}_{0}$$

Trong đó: `ṽ_R` là số sóng vạch nhánh R (ΔJ = +1) (cm^-1); `ṽ_P` là số sóng vạch nhánh P (ΔJ = -1) (cm^-1); `ṽ_Q` là số sóng vạch nhánh Q (ΔJ = 0) (cm^-1); `ṽ_0` là số sóng của vạch trung tâm (chuyển dời dao động thuần tuý) (cm^-1); `B` là hằng số quay (cm^-1); `J` là số lượng tử quay của trạng thái đầu ().

*Điều kiện:* Coi hằng số quay ở hai trạng thái dao động là như nhau; nhánh Q chỉ xuất hiện khi phân tử có momen động lượng electron khác 0 hoặc với dao động biến dạng của phân tử thẳng

*Ghi chú:* Atkins Focus 11C. Khoảng trống 4B ở giữa hai nhánh P và R là dấu hiệu nhận biết đặc trưng của phổ IR pha khí độ phân giải cao. Kho Việt Nam không có cấu trúc quay của dải hồng ngoại.

<sub>`chemistry.dai-hoc.pho-hoc.nhanh-p-r-pho-dao-dong-quay` · lớp 13 · #pho-hoc #hong-ngoai #nhanh-p-r #intl-undergrad</sub>

---

**Quy tắc lọc lựa của phổ dao động hồng ngoại** — *Selection rules for infrared vibrational spectroscopy*

$$\Delta v = \pm 1\ (\text{điều hoà});\qquad \left(\frac{\partial \mu}{\partial Q}\right)_{0} \neq 0$$

Trong đó: `Δv` là biến thiên số lượng tử dao động (); `μ` là momen lưỡng cực của phân tử (C.m); `Q` là toạ độ chuẩn tắc của dao động (m).

*Điều kiện:* Dao động tử điều hoà; quy tắc lọc lựa tổng thể đòi hỏi momen lưỡng cực phải BIẾN THIÊN theo toạ độ dao động (không đòi hỏi phải có momen lưỡng cực vĩnh cửu)

*Ghi chú:* Atkins Focus 11C. Vì vậy CO2 tuy không có momen lưỡng cực vĩnh cửu vẫn hoạt động hồng ngoại ở dao động bất đối xứng và dao động biến dạng, còn dao động đối xứng thì không (nhưng hoạt động Raman). Với dao động phi điều hoà, Δv = ±2, ±3 trở nên yếu nhưng cho phép (vạch bội). Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.quy-tac-loc-lua-dao-dong` · lớp 13 · #pho-hoc #hong-ngoai #quy-tac-loc-lua #intl-undergrad</sub>

---

**Cường độ pic đồng vị M+1 và M+2 trong phổ khối** — *Intensity of the M+1 and M+2 isotope peaks*

$$\frac{I(M\!+\!1)}{I(M)}\times 100 \approx 1.1\,n_{\mathrm{C}} + 0.37\,n_{\mathrm{N}};\qquad \frac{I(M)}{I(M\!+\!2)} = 3:1\ (\mathrm{Cl}),\quad 1:1\ (\mathrm{Br})$$

Trong đó: `I(M)` là cường độ pic ion phân tử (); `I(M+1)` là cường độ pic đồng vị M+1 (); `I(M+2)` là cường độ pic đồng vị M+2 (); `n_C` là số nguyên tử carbon trong phân tử (); `n_N` là số nguyên tử nitơ trong phân tử ().

*Điều kiện:* Độ phổ biến tự nhiên: 13C 1.07%, 15N 0.36%, 37Cl 24.2% (tỉ lệ 35Cl:37Cl xấp xỉ 3:1), 81Br 49.3% (79Br:81Br xấp xỉ 1:1), 34S 4.2%

*Ghi chú:* Pavia ch.8. Đếm số carbon từ pic M+1 và nhận biết halogen từ mẫu M/M+2 là kĩ năng chuẩn trong xác định cấu trúc quốc tế. Với hai nguyên tử clo, tỉ lệ M:M+2:M+4 = 9:6:1. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.pho-khoi-pic-dong-vi` · lớp 13 · #pho-hoc #pho-khoi #dong-vi #intl-undergrad</sub>

---

**Tỉ số khối trên điện tích và độ phân giải của phổ khối** — *Mass-to-charge ratio and resolving power in mass spectrometry*

$$\frac{m}{z} = \frac{m_{\text{ion}}}{z\,e}\ \text{(quy ước không thứ nguyên)};\qquad R = \frac{m}{\Delta m}$$

Trong đó: `m/z` là tỉ số khối trên điện tích của ion (); `m_ion` là khối lượng ion tính theo đơn vị khối lượng nguyên tử (u); `z` là số điện tích nguyên tố của ion (); `e` là điện tích nguyên tố (C); `R` là độ phân giải khối (); `Δm` là hiệu khối lượng nhỏ nhất còn phân biệt được (u); `m` là khối lượng danh nghĩa tại vùng khảo sát (u).

*Điều kiện:* Theo quy ước IUPAC, m/z là đại lượng KHÔNG thứ nguyên (khối lượng tính theo u chia cho số điện tích); với ion đơn điện tích m/z trùng số trị với khối lượng ion

*Ghi chú:* Pavia ch.8. Máy phân giải cao (R lớn hơn 10000) phân biệt được các ion cùng khối lượng danh nghĩa nhưng khác công thức, ví dụ CO (27.9949) và N2 (28.0062) - cơ sở của phép xác định công thức phân tử chính xác. Kho Việt Nam có phổ kế khối Bainbridge ở vật lí (nguyên lí tách ion) nhưng không có phổ khối như công cụ xác định cấu trúc hoá học.

<sub>`chemistry.dai-hoc.pho-hoc.pho-khoi-ti-so-m-tren-z` · lớp 13 · #pho-hoc #pho-khoi #do-phan-giai #intl-undergrad</sub>

---

**Quy tắc nitơ trong phổ khối** — *The nitrogen rule in mass spectrometry*

$$M\ \text{lẻ} \Leftrightarrow n_{\mathrm{N}}\ \text{lẻ};\qquad M\ \text{chẵn} \Leftrightarrow n_{\mathrm{N}}\ \text{chẵn (kể cả }0)$$

Trong đó: `M` là khối lượng danh nghĩa của ion phân tử (u); `n_N` là số nguyên tử nitơ trong phân tử ().

*Điều kiện:* Phân tử chỉ chứa C, H, O, N, S, halogen, Si, P; áp dụng cho ion phân tử (không phải mảnh)

*Ghi chú:* Pavia ch.8. Với mảnh sinh ra do đứt một liên kết đơn (mảnh gốc-cation), quy tắc bị đảo lại. Kết hợp quy tắc nitơ với độ bất bão hoà cho phép thu hẹp nhanh các công thức phân tử khả dĩ. Kho Việt Nam đã có 'độ bất bão hoà' nhưng chưa có quy tắc nitơ. PHẠM VI: quy tắc nitơ không nằm trong đặc tả A-Level hay IB (hai hệ này chỉ yêu cầu pic ion phân tử, mảnh và mẫu đồng vị), nên bản ghi này chỉ gắn intl-undergrad.

<sub>`chemistry.dai-hoc.pho-hoc.quy-tac-nito-pho-khoi` · lớp 13 · #pho-hoc #pho-khoi #quy-tac-nito #intl-undergrad</sub>

---

**Hiệu chỉnh biến dạng li tâm trong phổ quay** — *Centrifugal distortion correction in rotational spectra*

$$F(J) = B\,J(J+1) - D_{J}\,J^{2}(J+1)^{2};\qquad D_{J} \approx \frac{4B^{3}}{\tilde{\nu}_{e}^{2}}$$

Trong đó: `F(J)` là số hạng quay đã hiệu chỉnh (cm^-1); `B` là hằng số quay (cm^-1); `J` là số lượng tử quay (); `D_J` là hằng số biến dạng li tâm (cm^-1); `ṽ_e` là số sóng dao động điều hoà của liên kết (cm^-1).

*Điều kiện:* Phân tử thẳng; D_J rất nhỏ so với B nên chỉ đáng kể ở J lớn

*Ghi chú:* Atkins Focus 11B. Liên kết càng cứng (ṽ_e lớn) thì D_J càng nhỏ. Hệ quả quan sát được: các vạch phổ quay không còn cách đều tuyệt đối mà hơi co lại khi J tăng. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.bien-dang-li-tam` · lớp 13 · #pho-hoc #pho-quay #li-tam #intl-undergrad</sub>

---

**Hằng số quay và khoảng cách vạch trong phổ quay** — *Rotational constant and line spacing in a rotational spectrum*

$$B = \frac{h}{8\pi^{2}cI};\qquad F(J) = B\,J(J+1);\qquad \tilde{\nu}(J\!\to\!J\!+\!1) = 2B(J+1);\qquad \Delta\tilde{\nu} = 2B$$

Trong đó: `B` là hằng số quay biểu diễn theo số sóng (cm^-1); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `I` là momen quán tính của phân tử (kg.m^2); `F(J)` là số hạng quay của mức J (cm^-1); `J` là số lượng tử quay (); `ṽ` là số sóng của vạch hấp thụ (cm^-1); `Δṽ` là khoảng cách giữa hai vạch liên tiếp (cm^-1).

*Điều kiện:* Quay tử cứng thẳng; bỏ qua biến dạng li tâm; nếu I tính theo kg.m^2 thì phải đổi đơn vị cho phù hợp để B ra cm^-1

*Ghi chú:* Atkins Focus 11B. Phổ quay là dãy vạch CÁCH ĐỀU nhau 2B - đo Δṽ cho ngay B, từ đó suy ra I rồi ra độ dài liên kết. Ví dụ 1H35Cl có B khoảng 10.59 cm^-1. Kho Việt Nam không có phổ quay.

<sub>`chemistry.dai-hoc.pho-hoc.hang-so-quay-va-khoang-cach-vach` · lớp 13 · #pho-hoc #pho-quay #hang-so-quay #intl-undergrad</sub>

---

**Mức quay có dân số lớn nhất và bao hình cường độ của phổ quay** — *Most populated rotational level and the intensity envelope of a rotational spectrum*

$$N_{J} \propto (2J+1)\,e^{-hcBJ(J+1)/k_{B}T};\qquad J_{\max} \approx \sqrt{\frac{k_{B}T}{2hcB}} - \frac{1}{2}$$

Trong đó: `N_J` là số phân tử ở mức quay thứ J (); `J` là số lượng tử quay (); `J_max` là số lượng tử quay của mức có dân số lớn nhất (); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `B` là hằng số quay biểu diễn theo số sóng (cm^-1); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Quay tử cứng thẳng ở cân bằng nhiệt; xấp xỉ J liên tục khi tìm cực đại (chỉ tốt khi k_BT lớn hơn nhiều hcB, đúng ở nhiệt độ phòng cho hầu hết phân tử trừ H2); J_max thu được phải làm tròn về số nguyên

*Ghi chú:* Atkins Focus 11B, Hollas ch.5. Tích của thừa số suy biến (2J + 1) TĂNG theo J và thừa số Boltzmann GIẢM theo J tạo ra bao hình cường độ có cực đại đặc trưng của mọi phổ quay và của cấu trúc quay trong dải hồng ngoại - đo vị trí cực đại này là cách ước lượng nhiệt độ khí (nhiệt kế phổ học). Ví dụ 1H35Cl (B = 10.59 cm^-1) ở 298 K cho J_max khoảng 3; CO (B = 1.93 cm^-1) cho J_max khoảng 7. k_B = 1.380649e-23 J/K, hc/k_B = 1.43878 cm.K. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.muc-quay-dan-so-cuc-dai` · lớp 13 · #pho-quay #boltzmann #cuong-do-vach #intl-undergrad</sub>

---

**Quy tắc lọc lựa của phổ quay thuần tuý** — *Selection rules for pure rotational spectroscopy*

$$\Delta J = \pm 1,\qquad \Delta M_{J} = 0,\pm 1;\qquad \text{điều kiện tổng thể: }\ \mu_{\text{vĩnh cửu}} \neq 0$$

Trong đó: `ΔJ` là biến thiên số lượng tử quay (); `ΔM_J` là biến thiên số lượng tử hình chiếu (); `μ_vĩnh cửu` là momen lưỡng cực vĩnh cửu của phân tử (C.m).

*Điều kiện:* Phổ hấp thụ vi sóng; phân tử phải có momen lưỡng cực vĩnh cửu (quy tắc lọc lựa tổng thể). Phân tử đồng hạch (N2, O2) và phân tử đối xứng cao (CH4, CO2) không cho phổ quay vi sóng

*Ghi chú:* Atkins Focus 11B. Đối lập: phổ quay RAMAN chỉ đòi hỏi độ phân cực bất đẳng hướng và có ΔJ = 0, ±2, nên N2 và O2 vẫn cho phổ quay Raman. Kho Việt Nam không có quy tắc lọc lựa phổ phân tử.

<sub>`chemistry.dai-hoc.pho-hoc.quy-tac-loc-lua-pho-quay` · lớp 13 · #pho-hoc #pho-quay #quy-tac-loc-lua #intl-undergrad</sub>

---

**Hệ số hấp thụ mol tích phân và lực dao động tử** — *Integrated absorption coefficient and oscillator strength*

$$\mathcal{A} = \int_{\text{dải}}\varepsilon(\tilde{\nu})\,d\tilde{\nu};\qquad f = 4.319\times 10^{-9}\int_{\text{dải}}\varepsilon(\tilde{\nu})\,d\tilde{\nu}$$

Trong đó: `A` là hệ số hấp thụ mol tích phân trên toàn dải (L/(mol.cm^2)); `ε(ṽ)` là hệ số hấp thụ mol ở số sóng ṽ (L/(mol.cm)); `ṽ` là số sóng (cm^-1); `f` là lực dao động tử (không thứ nguyên) ().

*Điều kiện:* ε tính theo L.mol^-1.cm^-1 và ṽ theo cm^-1 thì hệ số 4.319e-9 cho f không thứ nguyên; f <= 1 với chuyển dời cho phép hoàn toàn

*Ghi chú:* Atkins Focus 11F, Hollas ch.2. Kho Việt Nam đã có định luật Lambert - Beer với ε ở dạng điểm; bản quốc tế bổ sung dạng TÍCH PHÂN trên cả dải và lực dao động tử f - đại lượng nối cường độ thực nghiệm với momen chuyển dời tính từ hàm sóng. f khoảng 1 với chuyển dời pi -> pi* cho phép, f khoảng 1e-4 với chuyển dời n -> pi* bị cấm. PHẠM VI: IB chỉ yêu cầu định luật Beer - Lambert dạng A = εcl; hệ số hấp thụ tích phân và lực dao động tử f là nội dung đại học, nên bản ghi này chỉ gắn intl-undergrad.

<sub>`chemistry.dai-hoc.pho-hoc.he-so-hap-thu-mol-tich-phan` · lớp 13 · #pho-hoc #hap-thu #luc-dao-dong-tu #intl-undergrad</sub>

---

**Nguyên lí Franck - Condon và thừa số Franck - Condon** — *Franck - Condon principle and Franck - Condon factor*

$$S_{v'v''} = \left|\int \chi_{v'}^{*}(R)\,\chi_{v''}(R)\,dR\right|^{2};\qquad I \propto S_{v'v''}$$

Trong đó: `S_{v'v''}` là thừa số Franck - Condon (); `χ_v'` là hàm sóng dao động của trạng thái electron kích thích (); `χ_v''` là hàm sóng dao động của trạng thái electron cơ bản (); `R` là toạ độ hạt nhân (độ dài liên kết) (m); `I` là cường độ vạch dao động trong dải electron ().

*Điều kiện:* Chuyển dời electron xảy ra nhanh hơn nhiều so với chuyển động hạt nhân nên hạt nhân coi như đứng yên (chuyển dời 'thẳng đứng' trên giản đồ thế năng)

*Ghi chú:* Atkins Focus 11F. Nếu độ dài liên kết ở trạng thái kích thích lệch nhiều so với trạng thái cơ bản thì dải hấp thụ trải rộng và cực đại ở v' cao; nếu hai đường cong thế năng nằm chồng nhau thì chuyển dời 0-0 mạnh nhất. Đây là hệ quả trực tiếp của xấp xỉ Born - Oppenheimer. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.pho-hoc.nguyen-li-franck-condon` · lớp 13 · #pho-hoc #franck-condon #pho-dien-tu #intl-undergrad</sub>

---

**Phương trình cơ bản của phổ quang electron (UPS/XPS)** — *Basic equation of photoelectron spectroscopy*

$$\tfrac{1}{2}m_{e}v^{2} = h\nu - I_{i};\qquad E_{\text{lk}} = h\nu - E_{\text{động}} - \phi_{\text{máy}}$$

Trong đó: `m_e` là khối lượng electron (kg); `v` là tốc độ electron bật ra (m/s); `h` là hằng số Planck (J.s); `ν` là tần số bức xạ ion hoá (Hz); `I_i` là năng lượng ion hoá của obitan thứ i (J); `E_lk` là năng lượng liên kết của electron trong mẫu (J); `E_động` là động năng đo được của quang electron (J); `φ_máy` là công thoát của máy phổ (J).

*Điều kiện:* Nguồn đơn sắc (He I 21.22 eV cho UPS; Al Kα 1486.6 eV cho XPS); mẫu và máy dò tiếp xúc điện nên dùng công thoát của máy

*Ghi chú:* Atkins Focus 11G. Kết hợp với định lí Koopmans, phổ quang electron cho phép ĐO trực tiếp năng lượng các obitan phân tử - bằng chứng thực nghiệm mạnh nhất cho thuyết MO. Cấu trúc dao động trên mỗi dải cho biết obitan bị ion hoá là liên kết, phản liên kết hay không liên kết. Kho Việt Nam không có (chỉ có hiệu ứng quang điện kim loại ở vật lí).

<sub>`chemistry.dai-hoc.pho-hoc.pho-quang-electron` · lớp 13 · #pho-hoc #quang-electron #xps #intl-undergrad</sub>

---

**Quy tắc lọc lựa cho chuyển dời điện tử (quy tắc spin và quy tắc Laporte)** — *Selection rules for electronic transitions: the spin rule and the Laporte rule*

$$\Delta S = 0;\qquad \Delta L = 0,\pm 1;\qquad \Delta J = 0,\pm 1\ \left(J = 0 \to J = 0\ \text{bị cấm}\right);\qquad \text{Laporte: } g \leftrightarrow u\ \text{cho phép},\ g \leftrightarrow g\ \text{và}\ u \leftrightarrow u\ \text{bị cấm}$$

Trong đó: `ΔS` là biến thiên số lượng tử spin tổng giữa hai trạng thái điện tử (); `ΔL` là biến thiên số lượng tử momen động lượng obitan tổng (); `ΔJ` là biến thiên số lượng tử momen động lượng toàn phần (); `J` là số lượng tử momen động lượng toàn phần (); `g` là trạng thái chẵn (gerade) đối với phép nghịch đảo qua tâm đối xứng (); `u` là trạng thái lẻ (ungerade) đối với phép nghịch đảo qua tâm đối xứng ().

*Điều kiện:* Chuyển dời lưỡng cực điện; ghép Russell - Saunders (nguyên tử nhẹ); quy tắc Laporte chỉ áp dụng cho tiểu phân CÓ tâm đối xứng (phức bát diện, phân tử đồng hạch), không áp dụng cho phức tứ diện

*Ghi chú:* Atkins Focus 11F, Housecroft ch.20, Miessler ch.11. Đây là chìa khoá định lượng để hiểu cường độ dải hấp thụ: dải d-d của phức bát diện vừa bị cấm Laporte vừa yếu (ε khoảng 1-100 L/(mol.cm)) và chỉ xuất hiện nhờ ghép dao động - điện tử (vibronic coupling) làm mất tạm thời tâm đối xứng; phức tứ diện không có tâm đối xứng nên dải d-d mạnh hơn khoảng 100 lần; dải chuyển điện tích (charge transfer) không vi phạm quy tắc nào nên rất mạnh (ε khoảng 1e3-1e4) - đó là màu đậm của MnO4- và CrO4^2-. Chuyển dời vi phạm quy tắc spin (ví dụ singlet -> triplet) rất yếu, trừ khi ghép spin - obitan mạnh (ion 4d, 5d). Kho Việt Nam có quy tắc lọc lựa cho nguyên tử ở file vật lí nhưng không có quy tắc Laporte và cách dùng nó cho phổ phức chất.

<sub>`chemistry.dai-hoc.pho-hoc.quy-tac-loc-lua-pho-dien-tu` · lớp 13 · #pho-dien-tu #quy-tac-loc-lua #laporte #phuc-chat #intl-undergrad</sub>

---

### Tinh thể học

**Độ đặc khít của các kiểu mạng tinh thể kim loại** — *Packing efficiency of metallic lattices*

$$P = \frac{Z\cdot\frac{4}{3}\pi r^{3}}{a^{3}};\quad \begin{cases} \text{lập phương đơn giản: } a=2r,\ P=52.4\% \\ \text{lập phương tâm khối: } a\sqrt{3}=4r,\ P=68.0\% \\ \text{lập phương tâm diện: } a\sqrt{2}=4r,\ P=74.0\% \\ \text{lục phương chặt khít: } P=74.0\% \end{cases}$$

Trong đó: `P` là độ đặc khít (phần thể tích bị chiếm) (%); `Z` là số nguyên tử trong ô mạng (); `r` là bán kính nguyên tử (pm); `a` là hằng số mạng (pm).

*Điều kiện:* Nguyên tử coi như quả cầu cứng đồng nhất tiếp xúc nhau

*Ghi chú:* Số phối trí: lập phương đơn giản 6, tâm khối 8, tâm diện và lục phương chặt khít 12. Hai kiểu chặt khít nhất (74%) là fcc và hcp.

<sub>`chemistry.dai-hoc.tinh-the-hoc.do-dac-khit` · lớp 13 · #tinh-the #do-dac-khit #kim-loai</sub>

---

**Định luật Bragg** — *Bragg's law*

$$2d_{hkl}\sin\theta = n\lambda;\qquad d_{hkl} = \frac{a}{\sqrt{h^{2}+k^{2}+l^{2}}}\ \text{(hệ lập phương)}$$

Trong đó: `d_hkl` là khoảng cách giữa hai mặt mạng liên tiếp (hkl) (pm); `θ` là góc tới (góc Bragg) (degree); `n` là bậc nhiễu xạ (số nguyên) (); `λ` là bước sóng tia X (pm); `a` là hằng số mạng (pm); `h` là chỉ số Miller của mặt mạng; `k` là chỉ số Miller của mặt mạng; `l` là chỉ số Miller của mặt mạng.

*Điều kiện:* Nhiễu xạ trên các mặt mạng song song cách đều; giao thoa tăng cường

*Ghi chú:* Tia X thường dùng: Cu K-alpha có λ = 154.2 pm. Từ phổ nhiễu xạ tia X bột xác định được hệ tinh thể và hằng số mạng.

<sub>`chemistry.dai-hoc.tinh-the-hoc.dinh-luat-bragg` · lớp 13 · #tinh-the #bragg #nhieu-xa-tia-x</sub>

---

**Phương trình Born - Landé tính năng lượng mạng lưới** — *Born - Landé equation for lattice energy*

$$U = -\frac{N_{A}\,M\,|z_{+}z_{-}|\,e^{2}}{4\pi\varepsilon_{0}\,r_{0}}\left(1 - \frac{1}{n}\right)$$

Trong đó: `U` là năng lượng mạng lưới (âm, ứng với quá trình tạo tinh thể từ các ion khí) (J/mol); `N_A` là số Avogadro (mol^-1); `M` là hằng số Madelung (phụ thuộc kiểu mạng) (); `z+` là số điện tích của cation (); `z-` là số điện tích của anion (lấy trị tuyệt đối trong công thức) (); `e` là điện tích nguyên tố (C); `ε_0` là hằng số điện môi chân không (F/m); `r_0` là khoảng cách cân bằng giữa hai ion trái dấu gần nhất (m); `n` là số mũ Born (thường 5 - 12) ().

*Điều kiện:* Tinh thể ion thuần túy, ion là quả cầu cứng tích điện điểm; các đại lượng tính theo hệ SI (r_0 bằng m), sau đó đổi U sang kJ/mol

*Ghi chú:* Dấu trừ và trị tuyệt đối |z+z-| bảo đảm U < 0. ε_0 = 8.854e-12 F/m, e = 1.602e-19 C. Hằng số Madelung: NaCl 1.748; CsCl 1.763; ZnS blende 1.638; CaF2 2.519. |U| tỉ lệ với tích điện tích và tỉ lệ nghịch với khoảng cách ion.

<sub>`chemistry.dai-hoc.tinh-the-hoc.born-lande` · lớp 13 · #tinh-the #nang-luong-mang #born-lande</sub>

---

**Chu trình Born - Haber** — *Born - Haber cycle*

$$\Delta_{f}H^{0}(\mathrm{MX}) = \Delta_{th}H(\mathrm{M}) + \frac{1}{2}D(\mathrm{X}_{2}) + I_{1}(\mathrm{M}) + A(\mathrm{X}) + U$$

Trong đó: `Δ_fH0(MX)` là nhiệt tạo thành chuẩn của tinh thể ion MX (kJ/mol); `Δ_thH(M)` là nhiệt thăng hoa (nguyên tử hóa) của kim loại (kJ/mol); `D(X2)` là năng lượng phân li liên kết của phân tử X2 (kJ/mol); `I_1(M)` là năng lượng ion hóa thứ nhất của kim loại (kJ/mol); `A(X)` là ái lực electron của phi kim (mang dấu âm khi tỏa nhiệt) (kJ/mol); `U` là năng lượng mạng lưới (âm) (kJ/mol).

*Điều kiện:* Áp dụng định luật Hess cho chu trình khép kín; chú ý dấu và số nấc ion hóa của kim loại

*Ghi chú:* Cho phép xác định gián tiếp năng lượng mạng lưới U hoặc ái lực electron A vốn khó đo trực tiếp. NaCl có U ≈ -787 kJ/mol.

<sub>`chemistry.dai-hoc.tinh-the-hoc.chu-trinh-born-haber` · lớp 13 · #tinh-the #born-haber #dinh-luat-hess</sub>

---

**Phương trình Kapustinskii** — *Kapustinskii equation*

$$U = -\frac{1202.5\,\nu\,|z_{+}z_{-}|}{r_{+}+r_{-}}\left(1 - \frac{34.5}{r_{+}+r_{-}}\right)\ \mathrm{kJ/mol}$$

Trong đó: `U` là năng lượng mạng lưới (kJ/mol); `ν` là tổng số ion trong một đơn vị công thức (); `z+` là điện tích cation (); `z-` là điện tích anion (); `r+` là bán kính cation (pm); `r-` là bán kính anion (pm).

*Điều kiện:* Bán kính tính bằng pm; công thức gần đúng không cần biết kiểu mạng

*Ghi chú:* Ưu điểm: không cần hằng số Madelung nên áp dụng được cho cả hợp chất chưa biết cấu trúc. NaCl có ν = 2, KAl(SO4)2 có ν = 4.

<sub>`chemistry.dai-hoc.tinh-the-hoc.kapustinskii` · lớp 13 · #tinh-the #nang-luong-mang #kapustinskii</sub>

---

**Tỉ số bán kính và số phối trí trong tinh thể ion** — *Radius ratio rule*

$$\frac{r_{+}}{r_{-}}:\quad \begin{cases} 0.155 - 0.225 & \text{phối trí } 3\ (\text{tam giác}) \\ 0.225 - 0.414 & \text{phối trí } 4\ (\text{tứ diện}) \\ 0.414 - 0.732 & \text{phối trí } 6\ (\text{bát diện}) \\ 0.732 - 1.000 & \text{phối trí } 8\ (\text{lập phương}) \end{cases}$$

Trong đó: `r+` là bán kính cation (pm); `r-` là bán kính anion (pm).

*Điều kiện:* Mô hình quả cầu cứng, liên kết ion thuần túy; chỉ mang tính định hướng

*Ghi chú:* NaCl (r+/r- = 0.56) có phối trí 6:6; CsCl (0.93) có phối trí 8:8; ZnS (0.40) có phối trí 4:4.

<sub>`chemistry.dai-hoc.tinh-the-hoc.ti-so-ban-kinh` · lớp 13 · #tinh-the #tinh-the-ion #ban-kinh-ion</sub>

---

**Bảy hệ tinh thể và điều kiện về hằng số mạng** — *The seven crystal systems*

$$\begin{cases} \text{Lập phương: } a=b=c;\ \alpha=\beta=\gamma=90^{\circ} \\ \text{Tứ phương: } a=b\neq c;\ \alpha=\beta=\gamma=90^{\circ} \\ \text{Trực thoi: } a\neq b\neq c;\ \alpha=\beta=\gamma=90^{\circ} \\ \text{Lục phương: } a=b\neq c;\ \alpha=\beta=90^{\circ},\gamma=120^{\circ} \\ \text{Ba phương: } a=b=c;\ \alpha=\beta=\gamma\neq 90^{\circ} \\ \text{Đơn tà: } a\neq b\neq c;\ \alpha=\gamma=90^{\circ}\neq\beta \\ \text{Tam tà: } a\neq b\neq c;\ \alpha\neq\beta\neq\gamma\neq 90^{\circ} \end{cases}$$

Trong đó: `a` là độ dài các cạnh của ô mạng cơ sở (pm); `b` là độ dài các cạnh của ô mạng cơ sở (pm); `c` là độ dài các cạnh của ô mạng cơ sở (pm); `α` là các góc giữa các cạnh của ô mạng (degree); `β` là các góc giữa các cạnh của ô mạng (degree); `γ` là các góc giữa các cạnh của ô mạng (degree).

*Điều kiện:* Ô mạng cơ sở là đơn vị lặp lại nhỏ nhất của mạng tinh thể

*Ghi chú:* Kết hợp bảy hệ với bốn kiểu mạng Bravais (P, I, F, C) cho 14 mạng Bravais.

<sub>`chemistry.dai-hoc.tinh-the-hoc.bay-he-tinh-the` · lớp 13 · #tinh-the #o-mang #bravais</sub>

---

**Khối lượng riêng tinh thể theo hằng số mạng** — *Crystal density from lattice parameters*

$$\rho = \frac{Z\,M}{N_{A}\,V_{\hat{o}}} \;\xrightarrow{\text{lập phương}}\; \rho = \frac{Z\,M}{N_{A}\,a^{3}}$$

Trong đó: `ρ` là khối lượng riêng của tinh thể (g/cm^3); `Z` là số đơn vị cấu trúc trong ô mạng (); `M` là khối lượng mol của đơn vị cấu trúc (g/mol); `N_A` là số Avogadro (mol^-1); `V_ô` là thể tích ô mạng cơ sở (cm^3); `a` là hằng số mạng (cạnh ô lập phương) (cm).

*Điều kiện:* Tinh thể lí tưởng, không có khuyết tật; đơn vị của a phải quy về cm khi tính ρ theo g/cm^3

*Ghi chú:* N_A = 6.022e23 mol^-1. So sánh ρ tính toán với ρ đo được cho biết mức độ khuyết tật (lỗ trống, chèn kẽ) trong tinh thể.

<sub>`chemistry.dai-hoc.tinh-the-hoc.khoi-luong-rieng-tinh-the` · lớp 13 · #tinh-the #khoi-luong-rieng #o-mang</sub>

---

**Số đơn vị cấu trúc Z trong ô mạng cơ sở** — *Number of formula units Z per unit cell*

$$Z = n_{\text{trong}} + \frac{n_{\text{mặt}}}{2} + \frac{n_{\text{cạnh}}}{4} + \frac{n_{\text{đỉnh}}}{8}$$

Trong đó: `Z` là số đơn vị cấu trúc trong một ô mạng cơ sở (); `n_trong` là số tiểu phân nằm hoàn toàn bên trong ô mạng; `n_mặt` là số tiểu phân ở tâm mặt; `n_cạnh` là số tiểu phân ở giữa cạnh; `n_đỉnh` là số tiểu phân ở đỉnh.

*Điều kiện:* Ô mạng lập phương hoặc tứ phương (các hệ có góc vuông)

*Ghi chú:* Lập phương đơn giản Z = 1; lập phương tâm khối Z = 2; lập phương tâm diện Z = 4. NaCl kiểu lập phương tâm diện có Z = 4 đơn vị NaCl.

<sub>`chemistry.dai-hoc.tinh-the-hoc.so-don-vi-cau-truc` · lớp 13 · #tinh-the #o-mang #so-don-vi</sub>

---

### Điện hóa học

**Điện cực khí hydro** — *Hydrogen gas electrode*

$$2\mathrm{H}^{+} + 2e \rightleftharpoons \mathrm{H}_{2}:\qquad E = -0.0592\,\mathrm{pH} + \frac{0.0592}{2}\lg\frac{1}{p_{H_{2}}/p^{0}}\;\xrightarrow{p_{H_{2}}=1\,\mathrm{bar}}\; E = -0.0592\,\mathrm{pH}$$

Trong đó: `E` là thế điện cực hydro (V); `pH` là pH của dung dịch (); `p_H2` là áp suất riêng phần của khí H2 (bar); `p0` là áp suất chuẩn (1 bar) (bar).

*Điều kiện:* Điện cực Pt phủ muội platin, khí H2 sục qua; 25 độ C

*Ghi chú:* Điện cực hydro chuẩn (SHE): a(H+) = 1, p(H2) = 1 bar, quy ước E0 = 0.000 V - là mốc của mọi thế điện cực.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.dien-cuc-khi-hydro` · lớp 13 · #dien-hoa #dien-cuc-khi #ph</sub>

---

**Điện cực loại một (kim loại - ion kim loại)** — *Electrode of the first kind*

$$M^{n+} + ne \rightleftharpoons M:\qquad E = E^{0} + \frac{0.0592}{n}\lg[M^{n+}]$$

Trong đó: `E` là thế điện cực (V); `E0` là thế điện cực chuẩn của cặp M(n+)/M (V); `n` là số electron trao đổi (); `[M^n+]` là nồng độ ion kim loại (mol/L).

*Điều kiện:* Kim loại nhúng trong dung dịch muối của chính nó; ở 25 độ C; hoạt độ kim loại rắn bằng 1

*Ghi chú:* Ví dụ Zn2+/Zn có E0 = -0.76 V, Cu2+/Cu có E0 = +0.34 V.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.dien-cuc-loai-1` · lớp 13 · #dien-hoa #dien-cuc #nernst</sub>

---

**Điện cực loại hai (kim loại - muối ít tan)** — *Electrode of the second kind*

$$\mathrm{AgCl} + e \rightleftharpoons \mathrm{Ag} + \mathrm{Cl}^{-}:\qquad E = E^{0} - 0.0592\lg[\mathrm{Cl}^{-}];\qquad E^{0}_{AgCl/Ag} = E^{0}_{Ag^{+}/Ag} + 0.0592\lg K_{sp}$$

Trong đó: `E` là thế điện cực (V); `E0` là thế chuẩn của điện cực loại hai (V); `[Cl-]` là nồng độ ion Cl- (mol/L); `K_sp` là tích số tan của AgCl ().

*Điều kiện:* Kim loại phủ muối ít tan của nó, nhúng trong dung dịch chứa anion của muối đó; 25 độ C

*Ghi chú:* Điện cực so sánh thông dụng: calomel bão hòa (SCE) E = +0.2444 V, Ag/AgCl trong KCl bão hòa E = +0.199 V so với điện cực hydro chuẩn.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.dien-cuc-loai-2` · lớp 13 · #dien-hoa #dien-cuc-so-sanh #tich-so-tan</sub>

---

**Điện cực oxi hóa - khử (điện cực trơ)** — *Redox (inert) electrode*

$$\mathrm{Pt}\,|\,Ox, Kh:\qquad E = E^{0} + \frac{0.0592}{n}\lg\frac{[Ox]}{[Kh]};\qquad \text{ví dụ } \mathrm{MnO_{4}^{-}}: E = E^{0} + \frac{0.0592}{5}\lg\frac{[\mathrm{MnO_{4}^{-}}][\mathrm{H^{+}}]^{8}}{[\mathrm{Mn^{2+}}]}$$

Trong đó: `E` là thế điện cực (V); `E0` là thế chuẩn của cặp oxi hóa - khử (V); `n` là số electron trao đổi (); `[Ox]` là nồng độ dạng oxi hóa (mol/L); `[Kh]` là nồng độ dạng khử (mol/L); `[H+]` là nồng độ ion H+ (mol/L).

*Điều kiện:* Kim loại trơ (Pt, Au) chỉ dẫn electron, cả hai dạng Ox và Kh đều tan trong dung dịch

*Ghi chú:* Thế của cặp có H+ tham gia phụ thuộc mạnh vào pH: E(MnO4-/Mn2+) giảm khi pH tăng.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.dien-cuc-oxi-hoa-khu` · lớp 13 · #dien-hoa #dien-cuc #oxi-hoa-khu</sub>

---

**Điện cực thủy tinh đo pH** — *Glass pH electrode*

$$E_{tt} = \text{const} - 0.0592\,\mathrm{pH};\qquad \mathrm{pH}_{x} = \mathrm{pH}_{s} + \frac{(E_{x}-E_{s})F}{2.303RT}$$

Trong đó: `E_tt` là thế của điện cực thủy tinh (V); `pH` là pH dung dịch đo (); `pH_x` là pH của dung dịch cần đo; `pH_s` là pH của dung dịch chuẩn; `E_x` là sức điện động đo với dung dịch x (V); `E_s` là sức điện động đo với dung dịch chuẩn (V); `F` là hằng số Faraday (C/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Phải chuẩn hóa (calibration) bằng dung dịch đệm chuẩn; sai số kiềm ở pH > 12 do ion Na+

*Ghi chú:* const bao gồm thế bất đối xứng của màng và thế của điện cực so sánh bên trong. Điện cực thủy tinh là điện cực chọn lọc ion H+.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.dien-cuc-thuy-tinh` · lớp 13 · #dien-hoa #ph #dien-cuc-chon-loc</sub>

---

**Quan hệ giữa năng lượng Gibbs và sức điện động** — *Relation between Gibbs energy and cell emf*

$$\Delta_{r}G = -nFE;\qquad \Delta_{r}G^{0} = -nFE^{0}$$

Trong đó: `Δ_rG` là biến thiên năng lượng Gibbs của phản ứng trong pin (J/mol); `Δ_rG0` là biến thiên năng lượng Gibbs chuẩn (J/mol); `n` là số mol electron trao đổi (mol); `F` là hằng số Faraday (C/mol); `E` là sức điện động của pin (V); `E0` là sức điện động chuẩn (V).

*Điều kiện:* Pin làm việc thuận nghịch ở T, p không đổi

*Ghi chú:* F = 96485 C/mol. E > 0 tương ứng Δ_rG < 0: phản ứng tự diễn biến trong pin.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.delta-g-va-suc-dien-dong` · lớp 13 · #dien-hoa #nang-luong-gibbs #pin</sub>

---

**Tính hằng số cân bằng từ sức điện động chuẩn** — *Equilibrium constant from standard cell potential*

$$\ln K = \frac{nFE^{0}}{RT} \quad \Leftrightarrow \quad \lg K = \frac{nE^{0}}{0.0592}\ (25\,^{\circ}\mathrm{C})$$

Trong đó: `K` là hằng số cân bằng của phản ứng oxi hóa - khử (); `n` là số electron trao đổi (); `F` là hằng số Faraday (C/mol); `E0` là sức điện động chuẩn của pin (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Nhiệt độ 298 K khi dùng hệ số 0.0592

*Ghi chú:* Chỉ cần E0 = 0.3 V với n = 2 đã cho K ≈ 1e10: phản ứng gần như hoàn toàn.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.hang-so-can-bang-tu-the-chuan` · lớp 13 · #dien-hoa #can-bang #the-chuan</sub>

---

**Sự phụ thuộc của sức điện động vào nhiệt độ** — *Temperature dependence of cell emf*

$$\Delta_{r}S = nF\left(\frac{\partial E}{\partial T}\right)_{p};\qquad \Delta_{r}H = -nF\left[E - T\left(\frac{\partial E}{\partial T}\right)_{p}\right];\qquad Q_{tn} = nFT\left(\frac{\partial E}{\partial T}\right)_{p}$$

Trong đó: `Δ_rS` là biến thiên entropy của phản ứng trong pin (J/(mol.K)); `Δ_rH` là biến thiên enthalpy của phản ứng trong pin (J/mol); `n` là số electron trao đổi (mol); `F` là hằng số Faraday (C/mol); `E` là sức điện động (V); `T` là nhiệt độ tuyệt đối (K); `(∂E/∂T)_p` là hệ số nhiệt độ của sức điện động (V/K); `Q_tn` là nhiệt trao đổi thuận nghịch của pin (J/mol).

*Điều kiện:* Pin làm việc thuận nghịch; đo E ở nhiều nhiệt độ

*Ghi chú:* Đây là phương pháp điện hóa xác định ΔH, ΔS, ΔG của phản ứng mà không cần nhiệt lượng kế.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.he-so-nhiet-do-suc-dien-dong` · lớp 13 · #dien-hoa #pin #nhiet-dong</sub>

---

**Sức điện động của pin nồng độ** — *Electromotive force of a concentration cell*

$$E^{0} = 0 \Rightarrow E = \frac{RT}{nF}\ln\frac{C_{2}}{C_{1}} = \frac{0.0592}{n}\lg\frac{C_{2}}{C_{1}}\quad (C_{2} > C_{1},\ 25\,^{\circ}\mathrm{C})$$

Trong đó: `E` là sức điện động của pin nồng độ (V); `E0` là sức điện động chuẩn (bằng 0 vì hai điện cực cùng bản chất) (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `n` là số electron trao đổi (); `F` là hằng số Faraday (C/mol); `C_1` là nồng độ (hoạt độ) chất điện hoạt ở điện cực loãng hơn - đóng vai trò anot (mol/L); `C_2` là nồng độ (hoạt độ) chất điện hoạt ở điện cực đặc hơn - đóng vai trò catot (mol/L).

*Điều kiện:* Hai điện cực cùng bản chất, chỉ khác nồng độ (hoặc áp suất) chất điện hoạt; bỏ qua thế khuếch tán nhờ cầu muối; dung dịch loãng nên thay hoạt độ bằng nồng độ; hệ số 0.0592 chỉ đúng ở 298.15 K

*Ghi chú:* Vì E0 = 0 nên sức điện động chỉ sinh ra do chênh lệch nồng độ; pin ngừng hoạt động khi hai nồng độ bằng nhau. Ứng dụng: đo pH, xác định tích số tan, hằng số bền của phức và hệ số hoạt độ.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.pin-nong-do` · lớp 13 · #dien-hoa #pin #nernst</sub>

---

**Sức điện động của pin điện hóa** — *Electromotive force of a galvanic cell*

$$E_{pin} = E_{catot} - E_{anot} = E_{(+)} - E_{(-)};\qquad E^{0}_{pin} = E^{0}_{catot} - E^{0}_{anot}$$

Trong đó: `E_pin` là sức điện động của pin (V); `E_catot` là thế điện cực catot (cực dương, xảy ra khử) (V); `E_anot` là thế điện cực anot (cực âm, xảy ra oxi hóa) (V); `E0_pin` là sức điện động chuẩn (V).

*Điều kiện:* Pin làm việc thuận nghịch, đo ở dòng bằng không (phương pháp bù)

*Ghi chú:* Pin tự phóng điện khi E_pin > 0. Quy ước sơ đồ pin: anot bên trái, catot bên phải: (-) A | dd A || dd C | C (+).

<sub>`chemistry.dai-hoc.dien-hoa-hoc.suc-dien-dong-pin` · lớp 13 · #dien-hoa #pin #suc-dien-dong</sub>

---

**Phương trình Nernst dạng tổng quát** — *Nernst equation (general form)*

$$E = E^{0} - \frac{RT}{nF}\ln\frac{a_{Kh}}{a_{Ox}} = E^{0} + \frac{RT}{nF}\ln\frac{a_{Ox}}{a_{Kh}}$$

Trong đó: `E` là thế điện cực (hoặc sức điện động) ở điều kiện đang xét (V); `E0` là thế điện cực chuẩn (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `n` là số electron trao đổi (); `F` là hằng số Faraday (C/mol); `a_Ox` là hoạt độ dạng oxi hóa (lũy thừa theo hệ số tỉ lượng) (); `a_Kh` là hoạt độ dạng khử ().

*Điều kiện:* Hệ ở cân bằng điện hóa, không có dòng chạy qua

*Ghi chú:* F = 96485 C/mol. Dung dịch loãng có thể thay hoạt độ bằng nồng độ.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.phuong-trinh-nernst` · lớp 13 · #dien-hoa #nernst #the-dien-cuc</sub>

---

**Phương trình Nernst dạng logarit thập phân ở 25 độ C** — *Nernst equation at 25 degrees Celsius*

$$E = E^{0} + \frac{0.0592}{n}\lg\frac{[Ox]^{a}}{[Kh]^{b}}\quad (25\,^{\circ}\mathrm{C});\qquad \frac{2.303RT}{F} = 0.0592\ \text{V}$$

Trong đó: `E` là thế điện cực (V); `E0` là thế điện cực chuẩn (V); `n` là số electron trao đổi (); `[Ox]` là nồng độ dạng oxi hóa (mol/L); `[Kh]` là nồng độ dạng khử (mol/L); `a` là hệ số tỉ lượng tương ứng; `b` là hệ số tỉ lượng tương ứng.

*Điều kiện:* Nhiệt độ 298.15 K; dung dịch loãng (thay hoạt độ bằng nồng độ)

*Ghi chú:* Giá trị chính xác 2.303RT/F = 0.05916 V ở 298.15 K, thường làm tròn 0.059 hoặc 0.0592 V. Nếu có H+ tham gia thì phải đưa [H+] vào biểu thức.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.phuong-trinh-nernst-25do` · lớp 13 · #dien-hoa #nernst #the-dien-cuc</sub>

---

**Định luật Faraday về điện phân** — *Faraday's laws of electrolysis*

$$m = \frac{M\,I\,t}{nF} = \frac{M\,q}{nF};\qquad n_{e} = \frac{It}{F}$$

Trong đó: `m` là khối lượng chất thoát ra ở điện cực (g); `M` là khối lượng mol của chất (g/mol); `I` là cường độ dòng điện (A); `t` là thời gian điện phân (s); `n` là số electron trao đổi trên một đơn vị chất (); `F` là hằng số Faraday (C/mol); `q` là điện lượng đã dùng (C); `n_e` là số mol electron (mol).

*Điều kiện:* Hiệu suất dòng điện 100%; nếu không thì nhân thêm hiệu suất H

*Ghi chú:* F = 96485 C/mol ≈ 96500 C/mol = N_A.e. Định luật II: cùng điện lượng thì khối lượng các chất tỉ lệ với đương lượng của chúng.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.dinh-luat-faraday` · lớp 13 · #dien-hoa #dien-phan #faraday</sub>

---

**Độ dẫn điện mol và độ dẫn điện đương lượng** — *Molar and equivalent conductivity*

$$\Lambda_{m} = \frac{\kappa}{C};\qquad \lambda_{td} = \frac{\kappa}{C_{N}} = \frac{\Lambda_{m}}{z}$$

Trong đó: `Λ_m` là độ dẫn điện mol (S.m^2/mol); `κ` là độ dẫn điện riêng (S/m); `C` là nồng độ mol của chất điện li (mol/m^3); `λ_td` là độ dẫn điện đương lượng (S.m^2/mol); `C_N` là nồng độ đương lượng (mol/m^3); `z` là số đương lượng trên một mol chất điện li ().

*Điều kiện:* Nồng độ phải quy đổi đúng đơn vị (mol/m^3 khi κ tính bằng S/m)

*Ghi chú:* Chất điện li mạnh: Λ_m giảm chậm khi C tăng. Chất điện li yếu: Λ_m giảm rất nhanh do độ điện li giảm.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.do-dan-dien-mol` · lớp 13 · #dien-hoa #do-dan-dien #dien-li</sub>

---

**Độ dẫn điện riêng và hằng số bình đo** — *Conductivity and cell constant*

$$\kappa = \frac{1}{R}\cdot\frac{l}{A} = \frac{K_{b}}{R};\qquad K_{b} = \frac{l}{A}$$

Trong đó: `κ` là độ dẫn điện riêng (S/m); `R` là điện trở đo được của dung dịch (ohm); `l` là khoảng cách giữa hai điện cực (m); `A` là diện tích điện cực (m^2); `K_b` là hằng số bình đo độ dẫn (m^-1).

*Điều kiện:* Đo bằng dòng xoay chiều để tránh phân cực điện cực; nhiệt độ ổn định

*Ghi chú:* K_b xác định bằng dung dịch KCl chuẩn đã biết κ. Đơn vị thực dụng thường dùng S/cm hoặc mS/cm.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.do-dan-dien-rieng` · lớp 13 · #dien-hoa #do-dan-dien #thuc-nghiem</sub>

---

**Xác định độ điện li và hằng số điện li từ độ dẫn điện** — *Degree of dissociation from conductivity (Ostwald dilution law)*

$$\alpha = \frac{\Lambda_{m}}{\Lambda_{m}^{0}};\qquad K_{a} = \frac{\alpha^{2}C}{1-\alpha} = \frac{C\Lambda_{m}^{2}}{\Lambda_{m}^{0}(\Lambda_{m}^{0}-\Lambda_{m})}$$

Trong đó: `α` là độ điện li (); `Λ_m` là độ dẫn điện mol ở nồng độ C (S.m^2/mol); `Λ_m^0` là độ dẫn điện mol giới hạn (S.m^2/mol); `K_a` là hằng số điện li (hằng số axit) (mol/L); `C` là nồng độ mol của chất điện li yếu (mol/L).

*Điều kiện:* Chất điện li yếu, dung dịch loãng, bỏ qua hệ số hoạt độ

*Ghi chú:* Đây là định luật pha loãng Ostwald. Khi α << 1: K_a ≈ α^2C nên α ≈ căn(K_a/C).

<sub>`chemistry.dai-hoc.dien-hoa-hoc.do-dien-li-theo-do-dan` · lớp 13 · #dien-hoa #ostwald #dien-li-yeu</sub>

---

**Định luật Kohlrausch về căn bậc hai nồng độ** — *Kohlrausch square-root law*

$$\Lambda_{m} = \Lambda_{m}^{0} - K\sqrt{C}$$

Trong đó: `Λ_m` là độ dẫn điện mol ở nồng độ C (S.m^2/mol); `Λ_m^0` là độ dẫn điện mol giới hạn (S.m^2/mol); `K` là hằng số phụ thuộc bản chất chất điện li và dung môi (S.m^2.mol^-1.(mol/L)^-0.5); `C` là nồng độ mol (mol/L).

*Điều kiện:* Chỉ đúng cho chất điện li MẠNH ở nồng độ loãng

*Ghi chú:* Ngoại suy đồ thị Λ_m theo căn C về C = 0 cho Λ_m^0. Chất điện li yếu không tuân theo quy luật này.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.kohlrausch-dung-dich-loang` · lớp 13 · #dien-hoa #kohlrausch #do-dan-dien</sub>

---

**Định luật Kohlrausch về sự chuyển động độc lập của ion** — *Kohlrausch law of independent ionic migration*

$$\Lambda_{m}^{0} = \nu_{+}\lambda_{+}^{0} + \nu_{-}\lambda_{-}^{0}$$

Trong đó: `Λ_m^0` là độ dẫn điện mol giới hạn (ở độ loãng vô hạn) (S.m^2/mol); `ν+` là số cation trong một đơn vị công thức (); `ν-` là số anion trong một đơn vị công thức (); `λ+^0` là độ dẫn điện mol giới hạn của cation (S.m^2/mol); `λ-^0` là độ dẫn điện mol giới hạn của anion (S.m^2/mol).

*Điều kiện:* Dung dịch loãng vô hạn, các ion chuyển động độc lập, không tương tác

*Ghi chú:* Cho phép tính Λ0 của chất điện li yếu (như CH3COOH) từ Λ0 của các chất điện li mạnh. H+ (349.8) và OH- (198.0 x1e-4 S.m^2/mol) có linh độ đặc biệt lớn nhờ cơ chế Grotthuss.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.kohlrausch-gioi-han` · lớp 13 · #dien-hoa #kohlrausch #do-dan-dien</sub>

---

**Linh độ ion và độ dẫn điện mol của ion** — *Ionic mobility and molar ionic conductivity*

$$\lambda_{i} = |z_{i}|Fu_{i};\qquad u_{i} = \frac{v_{i}}{E};\qquad u_{i} = \frac{|z_{i}|e}{6\pi\eta r_{i}}$$

Trong đó: `λ_i` là độ dẫn điện mol của ion i (S.m^2/mol); `z_i` là điện tích ion (); `F` là hằng số Faraday (C/mol); `u_i` là linh độ (độ linh động) của ion (m^2/(V.s)); `v_i` là tốc độ chuyển động của ion (m/s); `E` là cường độ điện trường (V/m); `e` là điện tích nguyên tố (C); `η` là độ nhớt dung môi (Pa.s); `r_i` là bán kính ion hydrat hóa (m).

*Điều kiện:* Ion coi như quả cầu chuyển động trong môi trường liên tục (định luật Stokes)

*Ghi chú:* F = 96485 C/mol, e = 1.602e-19 C. Ion nhỏ nhưng hydrat hóa mạnh (Li+) lại có linh độ nhỏ hơn ion lớn ít hydrat hóa (K+, Cs+).

<sub>`chemistry.dai-hoc.dien-hoa-hoc.linh-do-ion` · lớp 13 · #dien-hoa #linh-do-ion #stokes</sub>

---

**Số vận chuyển của ion** — *Ionic transport (transference) number*

$$t_{+} = \frac{I_{+}}{I} = \frac{\nu_{+}\lambda_{+}}{\nu_{+}\lambda_{+}+\nu_{-}\lambda_{-}} = \frac{u_{+}}{u_{+}+u_{-}};\qquad t_{+} + t_{-} = 1$$

Trong đó: `t+` là số vận chuyển của cation (); `t-` là số vận chuyển của anion (); `I+` là phần dòng điện do cation tải (A); `I` là tổng cường độ dòng điện (A); `λ+` là độ dẫn điện mol của cation (S.m^2/mol); `λ-` là độ dẫn điện mol của anion; `u+` là linh độ tuyệt đối của cation (m^2/(V.s)); `u-` là linh độ tuyệt đối của anion.

*Điều kiện:* Dung dịch chỉ chứa một chất điện li; xác định bằng phương pháp Hittorf hoặc ranh giới chuyển động

*Ghi chú:* Trong dung dịch HCl, t(H+) ≈ 0.82 vì proton linh động hơn nhiều so với Cl-.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.so-van-chuyen` · lớp 13 · #dien-hoa #so-van-chuyen #do-dan-dien</sub>

---

**Phương trình Butler - Volmer** — *Butler - Volmer equation*

$$j = j_{0}\left[\exp\!\left(\frac{\alpha_{a}nF\eta}{RT}\right) - \exp\!\left(-\frac{\alpha_{c}nF\eta}{RT}\right)\right];\qquad \alpha_{a}+\alpha_{c}=1$$

Trong đó: `j` là mật độ dòng điện thực (A/m^2); `j_0` là mật độ dòng trao đổi (A/m^2); `α_a` là hệ số chuyển điện tích anot (); `α_c` là hệ số chuyển điện tích catot (); `n` là số electron trao đổi (); `F` là hằng số Faraday (C/mol); `η` là quá thế (V); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Phản ứng điện cực khống chế bởi giai đoạn chuyển electron (không bị khống chế khuếch tán)

*Ghi chú:* Với quá thế rất nhỏ: j ≈ j_0.nFη/(RT) - quan hệ tuyến tính. Với quá thế lớn: rút về phương trình Tafel.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.butler-volmer` · lớp 13 · #dien-hoa #butler-volmer #dong-hoc-dien-hoa</sub>

---

**Phương trình Tafel** — *Tafel equation*

$$\eta = a + b\lg|j|;\qquad a = -\frac{2.303RT}{\alpha nF}\lg j_{0},\quad b = \frac{2.303RT}{\alpha nF}$$

Trong đó: `η` là quá thế (V); `j` là mật độ dòng điện (A/m^2); `j_0` là mật độ dòng trao đổi (A/m^2); `a` là hằng số Tafel (tung độ gốc) (V); `b` là hệ số góc Tafel (V/decade); `α` là hệ số chuyển điện tích (); `n` là số electron trao đổi; `F` là hằng số Faraday (C/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Quá thế đủ lớn (|η| lớn hơn khoảng 0.1 V) để bỏ qua một trong hai số hạng của Butler - Volmer

*Ghi chú:* Đồ thị Tafel (η theo lg|j|) cho phép xác định α và j_0. Với α = 0.5, n = 1 ở 25 độ C thì b ≈ 0.118 V/decade.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.phuong-trinh-tafel` · lớp 13 · #dien-hoa #tafel #dong-hoc-dien-hoa</sub>

---

**Quá thế và điện thế phân hủy** — *Overpotential and decomposition voltage*

$$\eta = E_{\text{đo}} - E_{\text{cân bằng}};\qquad U_{ph} = E_{\text{phân cực}} + |\eta_{a}| + |\eta_{c}| + IR$$

Trong đó: `η` là quá thế (V); `E_đo` là thế điện cực khi có dòng chạy qua (V); `E_cân bằng` là thế điện cực cân bằng (Nernst) (V); `U_ph` là điện thế phân hủy thực tế (V); `η_a` là quá thế anot (V); `η_c` là quá thế catot (V); `I` là cường độ dòng (A); `R` là điện trở dung dịch (ohm).

*Điều kiện:* Điện cực bị phân cực do có dòng điện chạy qua

*Ghi chú:* Quá thế hydro trên Hg rất lớn (khoảng 1.5 V) nên có thể điện phân dung dịch muối kim loại kiềm trên catot Hg.

<sub>`chemistry.dai-hoc.dien-hoa-hoc.qua-the` · lớp 13 · #dien-hoa #qua-the #dien-phan</sub>

---

### Động hoá học nâng cao

**Phương trình Marcus về chuyển electron** — *Marcus equation for electron transfer*

$$\Delta^{\ddagger}G = \frac{\lambda}{4}\left(1 + \frac{\Delta_{r}G^{\circ}}{\lambda}\right)^{2};\qquad k_{\mathrm{ET}} \propto \exp\!\left(-\frac{\Delta^{\ddagger}G}{RT}\right)$$

Trong đó: `ΔG‡` là năng lượng Gibbs hoạt hoá của bước chuyển electron (J/mol); `λ` là năng lượng tái tổ chức (của phân tử và của dung môi) (J/mol); `Δ_rG°` là biến thiên năng lượng Gibbs chuẩn của phản ứng chuyển electron (J/mol); `k_ET` là hằng số tốc độ chuyển electron (s^-1); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Chuyển electron ngoại cầu (outer-sphere); hai mặt thế năng coi như parabol cùng độ cong

*Ghi chú:* Atkins Focus 19D. Dự đoán then chốt: khi -Δ_rG° vượt quá λ thì tốc độ GIẢM khi phản ứng càng thuận lợi hơn - 'vùng nghịch đảo Marcus', được xác nhận thực nghiệm và mang lại giải Nobel Hoá học 1992. Rất quan trọng trong quang hợp nhân tạo và pin. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.phuong-trinh-marcus` · lớp 13 · #dong-hoc #marcus #chuyen-electron #intl-undergrad</sub>

---

**Xấp xỉ tiền cân bằng** — *Pre-equilibrium approximation*

$$\mathrm{A} + \mathrm{B} \rightleftharpoons \mathrm{I} \xrightarrow{k_{2}} \mathrm{P};\qquad K = \frac{k_{1}}{k_{-1}} = \frac{[\mathrm{I}]}{[\mathrm{A}][\mathrm{B}]};\qquad v = k_{2}K[\mathrm{A}][\mathrm{B}]$$

Trong đó: `K` là hằng số cân bằng của bước tiền cân bằng (L/mol); `k_1` là hằng số tốc độ thuận của bước tạo trung gian (L/(mol.s)); `k_-1` là hằng số tốc độ nghịch (s^-1); `k_2` là hằng số tốc độ của bước chậm tạo sản phẩm (s^-1); `[I]` là nồng độ chất trung gian (mol/L); `[A]` là nồng độ chất A (mol/L); `[B]` là nồng độ chất B (mol/L); `v` là tốc độ tạo sản phẩm (mol/(L.s)).

*Điều kiện:* Điều kiện áp dụng: k_-1 lớn hơn nhiều so với k_2 (bước tạo trung gian cân bằng nhanh so với bước tiêu thụ); khác với nguyên lí nồng độ ổn định vốn không đòi hỏi điều kiện này

*Ghi chú:* Atkins Focus 17E. Hệ quả quan trọng: hằng số tốc độ quan sát k_obs = k_2K nên năng lượng hoạt hoá biểu kiến bằng E_a(k_2) + Δ_rH°(bước cân bằng) - có thể ÂM nếu bước tiền cân bằng toả nhiệt mạnh, giải thích các phản ứng chậm lại khi tăng nhiệt độ. Kho Việt Nam có nguyên lí nồng độ ổn định nhưng không có xấp xỉ tiền cân bằng.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.xap-xi-tien-can-bang` · lớp 13 · #dong-hoc #co-che #tien-can-bang #intl-undergrad</sub>

---

**Hiệu ứng muối sơ cấp (phương trình Brønsted - Bjerrum)** — *Primary kinetic salt effect (Brønsted - Bjerrum equation)*

$$\lg\frac{k}{k^{\circ}} = 2A\,z_{A}z_{B}\sqrt{I},\qquad A = 0.509\ (\mathrm{mol\,kg^{-1}})^{-1/2}\ \text{trong nước ở } 25\,^{\circ}\mathrm{C}$$

Trong đó: `k` là hằng số tốc độ ở lực ion I (L/(mol.s)); `k°` là hằng số tốc độ ở pha loãng vô hạn (I = 0) (L/(mol.s)); `A` là hằng số Debye - Hückel của dung môi (); `z_A` là điện tích của ion phản ứng A (); `z_B` là điện tích của ion phản ứng B (); `I` là lực ion của dung dịch (mol/kg).

*Điều kiện:* Phản ứng lưỡng phân tử giữa hai ion trong dung dịch loãng; áp dụng định luật giới hạn Debye - Hückel cho hệ số hoạt độ của phức hoạt động

*Ghi chú:* Atkins Focus 18D. Nếu z_A z_B > 0 (cùng dấu) thì tăng lực ion làm TĂNG tốc độ; nếu trái dấu thì làm GIẢM tốc độ; nếu một chất trung hoà thì không ảnh hưởng. Đo hệ số góc của lgk theo căn I cho ngay tích z_A z_B - công cụ xác định điện tích của các tiểu phân trong bước quyết định tốc độ. Kho Việt Nam có Debye - Hückel nhưng không có ứng dụng động học này.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.hieu-ung-muoi-dong-hoc` · lớp 13 · #dong-hoc #hieu-ung-muoi #debye-huckel #intl-undergrad</sub>

---

**Quy tắc Hughes - Ingold về ảnh hưởng của độ phân cực dung môi** — *Hughes - Ingold rules for solvent polarity effects*

$$\text{Điện tích tăng ở TTCT} \Rightarrow \uparrow k\ \text{khi } \varepsilon_{r}\uparrow;\qquad \text{Điện tích phân tán hoặc giảm} \Rightarrow \downarrow k\ \text{khi } \varepsilon_{r}\uparrow$$

Trong đó: `k` là hằng số tốc độ phản ứng (s^-1); `ε_r` là hằng số điện môi tương đối (độ phân cực) của dung môi (); `TTCT` là trạng thái chuyển tiếp ().

*Điều kiện:* So sánh mật độ điện tích của trạng thái chuyển tiếp với chất đầu; áp dụng cho phản ứng ion và phản ứng tạo/huỷ điện tích

*Ghi chú:* Clayden ch.15, Atkins Focus 18D. Ví dụ: SN1 của R-Br tạo cặp ion nên tăng mạnh trong dung môi phân cực proton; SN2 giữa anion và phân tử trung hoà (điện tích bị PHÂN TÁN ở TTCT) thì chậm lại trong dung môi phân cực proton nhưng nhanh lên rõ rệt trong dung môi phân cực aproton (DMSO, DMF, acetone) vì anion không bị solvat hoá bằng liên kết hydro. Kho Việt Nam không có phân tích ảnh hưởng dung môi ở mức này.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.quy-tac-hughes-ingold` · lớp 13 · #dong-hoc #dung-moi #co-che #intl-undergrad</sub>

---

**Hiệu ứng đồng vị động học sơ cấp** — *Primary kinetic isotope effect*

$$\frac{k_{\mathrm{H}}}{k_{\mathrm{D}}} = \exp\!\left[\frac{hc}{2k_{B}T}\left(\tilde{\nu}_{\mathrm{CH}} - \tilde{\nu}_{\mathrm{CD}}\right)\right] = \exp\!\left[\frac{hc\,\tilde{\nu}_{\mathrm{CH}}}{2k_{B}T}\left(1 - \sqrt{\frac{\mu_{\mathrm{CH}}}{\mu_{\mathrm{CD}}}}\right)\right]$$

Trong đó: `k_H` là hằng số tốc độ của hợp chất chứa hydro (s^-1); `k_D` là hằng số tốc độ của hợp chất chứa deuteri (s^-1); `h` là hằng số Planck (J.s); `c` là tốc độ ánh sáng (cm/s); `k_B` là hằng số Boltzmann (J/K); `T` là nhiệt độ tuyệt đối (K); `ṽ_CH` là số sóng dao động hoá trị C-H (cm^-1); `ṽ_CD` là số sóng dao động hoá trị C-D (cm^-1); `μ_CH` là khối lượng rút gọn của C-H (kg); `μ_CD` là khối lượng rút gọn của C-D (kg).

*Điều kiện:* Liên kết C-H (hoặc X-H) bị ĐỨT ở giai đoạn quyết định tốc độ; ở trạng thái chuyển tiếp dao động hoá trị coi như đã mất hoàn toàn năng lượng điểm không

*Ghi chú:* Atkins Focus 18C, Clayden ch.12. Với ṽ_CH khoảng 2900 cm^-1, giá trị lí thuyết cực đại ở 298 K là k_H/k_D khoảng 7. KIE sơ cấp lớn (5-8) là bằng chứng mạnh rằng liên kết C-H đứt ở bước chậm; KIE gần 1 thì không. PHÂN BIỆT với bản ghi IChO cùng tên (chemistry.dai-hoc.icho-dong-hoc.hieu-ung-dong-vi-dong-hoc): bản IChO viết theo TẦN SỐ ν (Hz), bản này viết theo SỐ SÓNG ṽ (cm^-1) - quy ước chuẩn của hoá lí quốc tế - và bổ sung dạng tính trực tiếp từ tỉ số khối lượng rút gọn, nên chỉ gắn intl-undergrad để tránh chồng lấn với file olympiad.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.hieu-ung-dong-vi-dong-hoc` · lớp 13 · #dong-hoc #dong-vi #co-che #intl-undergrad</sub>

---

**Điều kiện nổ của phản ứng dây chuyền phân nhánh** — *Explosion condition for a branched chain reaction*

$$\frac{d[\text{gốc}]}{dt} = \left(f k_{\text{nhánh}} - k_{\text{đứt}}\right)[\text{gốc}];\qquad f k_{\text{nhánh}} > k_{\text{đứt}} \Rightarrow \text{nổ nhánh}$$

Trong đó: `[gốc]` là nồng độ các trung tâm hoạt động (gốc tự do) (mol/L); `t` là thời gian (s); `f` là hệ số phân nhánh (số trung tâm mới sinh ra trên mỗi trung tâm bị tiêu thụ trừ 1) (); `k_nhánh` là hằng số tốc độ giai đoạn phân nhánh (s^-1); `k_đứt` là hằng số tốc độ tổng của các giai đoạn đứt mạch (s^-1).

*Điều kiện:* Phản ứng có giai đoạn phân nhánh (một gốc sinh ra nhiều gốc); nồng độ gốc tăng theo hàm mũ khi bất đẳng thức thoả mãn

*Ghi chú:* Atkins Focus 17F. Giải thích ba giới hạn nổ của hỗn hợp H2 + O2: giới hạn dưới do đứt mạch trên thành bình (áp suất thấp), giới hạn giữa do đứt mạch trong thể tích qua va chạm ba phân tử, giới hạn trên do nổ nhiệt. Kho Việt Nam có 'độ dài mạch của phản ứng dây chuyền' nhưng không có tiêu chuẩn nổ nhánh.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.dieu-kien-no-day-chuyen-phan-nhanh` · lớp 13 · #dong-hoc #day-chuyen #no #intl-undergrad</sub>

---

**Hằng số tốc độ giới hạn khuếch tán** — *Diffusion-limited rate constant*

$$k_{d} = 4\pi R^{*}D\,N_{A};\qquad k_{d} \approx \frac{8RT}{3\eta}\ \ (\text{hai tiểu phân kích thước tương đương})$$

Trong đó: `k_d` là hằng số tốc độ giới hạn khuếch tán (m^3/(mol.s)); `R*` là khoảng cách tiếp cận phản ứng (tổng bán kính hai tiểu phân) (m); `D` là tổng hệ số khuếch tán của hai tiểu phân (m^2/s); `N_A` là hằng số Avogadro (mol^-1); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `η` là độ nhớt của dung môi (Pa.s).

*Điều kiện:* Mọi cuộc gặp đều dẫn tới phản ứng (phản ứng 'hoàn hảo về mặt hoạt hoá'); dạng thứ hai dùng quan hệ Stokes - Einstein và giả thiết R* bằng tổng hai bán kính bằng nhau

*Ghi chú:* Atkins Focus 18D. Trong nước ở 25 độ C (η = 0.891 mPa.s), k_d khoảng 7.4e9 L/(mol.s). Đây là TRẦN tốc độ của phản ứng trong dung dịch - dùng để nhận biết phản ứng đã đạt giới hạn khuếch tán (trung hoà H+ + OH-, dập tắt huỳnh quang, một số enzyme). Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.hang-so-toc-do-gioi-han-khuech-tan` · lớp 13 · #dong-hoc #khuech-tan #dung-dich #intl-undergrad</sub>

---

**Cơ chế Lindemann - Hinshelwood của phản ứng đơn phân tử** — *Lindemann - Hinshelwood mechanism for unimolecular reactions*

$$k_{\text{đơn}} = \frac{k_{a}k_{b}[\mathrm{M}]}{k_{a}'[\mathrm{M}] + k_{b}};\qquad \frac{1}{k_{\text{đơn}}} = \frac{k_{a}'}{k_{a}k_{b}} + \frac{1}{k_{a}[\mathrm{M}]}$$

Trong đó: `k_đơn` là hằng số tốc độ biểu kiến bậc một quan sát được (s^-1); `k_a` là hằng số tốc độ hoạt hoá do va chạm (L/(mol.s)); `k_a'` là hằng số tốc độ khử hoạt hoá do va chạm (L/(mol.s)); `k_b` là hằng số tốc độ phân huỷ của phân tử đã hoạt hoá (s^-1); `[M]` là nồng độ tổng của các phân tử va chạm (thường là chính chất phản ứng hoặc khí trơ) (mol/L).

*Điều kiện:* Áp dụng nguyên lí nồng độ ổn định cho phân tử đã hoạt hoá A*; áp suất cao thì k_đơn -> k_a k_b/k_a' (bậc một); áp suất thấp thì k_đơn -> k_a[M] (bậc hai)

*Ghi chú:* Atkins Focus 18B. Đồ thị 1/k_đơn theo 1/[M] là đường thẳng - phép kiểm chứng thực nghiệm chuẩn. Thực tế đồ thị hơi cong, dẫn tới lí thuyết RRK/RRKM. Đây là lời giải cho nghịch lí 'phản ứng đơn phân tử lấy năng lượng từ đâu'. Kho Việt Nam không có.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.co-che-lindemann-hinshelwood` · lớp 13 · #dong-hoc #lindemann #don-phan-tu #intl-undergrad</sub>

---

**Đồ thị Eyring xác định enthalpy và entropy hoạt hoá** — *Eyring plot for the activation enthalpy and entropy*

$$\ln\!\frac{k}{T} = -\frac{\Delta^{\ddagger}H^{\circ}}{R}\cdot\frac{1}{T} + \left[\ln\frac{k_{B}}{h} + \frac{\Delta^{\ddagger}S^{\circ}}{R}\right];\qquad \Delta^{\ddagger}G^{\circ} = \Delta^{\ddagger}H^{\circ} - T\Delta^{\ddagger}S^{\circ}$$

Trong đó: `k` là hằng số tốc độ (s^-1); `T` là nhiệt độ tuyệt đối (K); `ΔH‡` là enthalpy hoạt hoá chuẩn (J/mol); `ΔS‡` là entropy hoạt hoá chuẩn (J/(mol.K)); `ΔG‡` là năng lượng Gibbs hoạt hoá chuẩn (J/mol); `R` là hằng số khí (J/(mol.K)); `k_B` là hằng số Boltzmann (J/K); `h` là hằng số Planck (J.s).

*Điều kiện:* Đo k ở nhiều nhiệt độ; hệ số truyền qua κ = 1; với phản ứng bậc hai phải dùng k theo đơn vị chuẩn hoá (chia cho c°)

*Ghi chú:* Atkins Focus 18C. Kho Việt Nam đã có phương trình Eyring dạng mũ; bản này là DẠNG LÀM VIỆC ĐỒ THỊ, cho phép tách riêng ΔH‡ (hệ số góc) và ΔS‡ (tung độ gốc). Ý nghĩa cơ chế: ΔS‡ âm mạnh chỉ cơ chế liên hợp (hai tiểu phân hợp thành một trạng thái chuyển tiếp trật tự, ví dụ Diels - Alder khoảng -150 J/(mol.K)); ΔS‡ dương chỉ cơ chế phân li (SN1).

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.do-thi-eyring` · lớp 13 · #dong-hoc #eyring #entropy-hoat-hoa #intl-undergrad</sub>

---

**Tiết diện phản ứng phụ thuộc năng lượng** — *Energy-dependent reactive cross-section*

$$\sigma(\varepsilon) = \begin{cases}0 & \varepsilon \leq \varepsilon_{a}\\ \sigma\left(1 - \dfrac{\varepsilon_{a}}{\varepsilon}\right) & \varepsilon > \varepsilon_{a}\end{cases}$$

Trong đó: `σ(ε)` là tiết diện phản ứng ở năng lượng va chạm ε (m^2); `ε` là năng lượng động học tương đối dọc theo đường nối tâm (J); `ε_a` là năng lượng ngưỡng của phản ứng (J); `σ` là tiết diện va chạm hình học (quả cầu cứng) (m^2).

*Điều kiện:* Mô hình quả cầu cứng có ngưỡng; chỉ thành phần động năng dọc đường nối tâm mới có tác dụng gây phản ứng

*Ghi chú:* Atkins Focus 18B. Lấy trung bình σ(ε) theo phân bố Maxwell - Boltzmann sinh ra chính dạng Arrhenius với E_a = N_A ε_a. Kho Việt Nam có thuyết va chạm dạng k = P.Z0.exp(-Ea/RT) nhưng KHÔNG có hàm kích thích σ(ε) - bước trung gian giải thích vì sao thừa số mũ Arrhenius xuất hiện.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.tiet-dien-phan-ung-theo-nang-luong` · lớp 13 · #dong-hoc #tiet-dien-phan-ung #va-cham #intl-undergrad</sub>

---

**Động học xúc tác dị thể theo cơ chế Eley - Rideal** — *Eley - Rideal kinetics of heterogeneous catalysis*

$$v = k\,p_{A}\,\theta_{B} = \frac{k\,K_{B}\,p_{A}p_{B}}{1 + K_{B}p_{B}}$$

Trong đó: `v` là tốc độ phản ứng bề mặt (mol/(m^2.s)); `k` là hằng số tốc độ của bước bề mặt (mol/(m^2.s.Pa)); `p_A` là áp suất riêng phần của chất A ở pha khí (không bị hấp phụ) (Pa); `θ_B` là độ che phủ bề mặt bởi chất B (); `K_B` là hằng số hấp phụ Langmuir của B (Pa^-1); `p_B` là áp suất riêng phần của B (Pa).

*Điều kiện:* Chỉ MỘT chất bị hấp phụ; chất kia phản ứng trực tiếp từ pha khí khi va chạm với phân tử đã hấp phụ; hấp phụ tuân theo đẳng nhiệt Langmuir

*Ghi chú:* Atkins Focus 19C. Khác biệt với Langmuir - Hinshelwood (đã có trong kho Việt Nam), ở đó CẢ HAI chất đều phải hấp phụ và tốc độ đạt cực đại rồi giảm khi một chất chiếm hết bề mặt. Eley - Rideal cho v tăng đơn điệu theo p_A. Kho Việt Nam chỉ có Langmuir - Hinshelwood.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.co-che-eley-rideal` · lớp 13 · #dong-hoc #xuc-tac-di-the #eley-rideal #intl-undergrad</sub>

---

**Hiệu quả xúc tác kcat/KM và giới hạn hoàn hảo** — *Catalytic efficiency kcat/KM and catalytic perfection*

$$v = \frac{k_{cat}}{K_{M}}[\mathrm{E}]_{0}[\mathrm{S}]\ \ ([\mathrm{S}] \ll K_{M});\qquad \frac{k_{cat}}{K_{M}} \leq k_{d} \approx 10^{8}\text{--}10^{9}\ \mathrm{L\,mol^{-1}s^{-1}}$$

Trong đó: `v` là tốc độ phản ứng enzyme (mol/(L.s)); `k_cat` là hằng số xúc tác (số vòng quay) (s^-1); `K_M` là hằng số Michaelis (mol/L); `[E]_0` là nồng độ enzyme tổng (mol/L); `[S]` là nồng độ cơ chất (mol/L); `k_d` là hằng số tốc độ giới hạn khuếch tán (L/(mol.s)).

*Điều kiện:* Vùng nồng độ cơ chất thấp; kcat/KM là hằng số tốc độ bậc hai biểu kiến của phản ứng giữa enzyme tự do và cơ chất tự do

*Ghi chú:* Atkins Focus 19B. kcat/KM là thước đo ĐÚNG của hiệu quả xúc tác khi so sánh các cơ chất khác nhau (không phải KM hay kcat riêng lẻ). Enzyme 'hoàn hảo về mặt xúc tác' đạt giới hạn khuếch tán: carbonic anhydrase, catalase, triosephosphate isomerase. Kho Việt Nam có Michaelis - Menten và nhắc kcat/KM trong ghi chú nhưng không có bản ghi riêng với giới hạn khuếch tán.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.hieu-qua-xuc-tac-kcat-km` · lớp 13 · #dong-hoc #enzyme #hieu-qua-xuc-tac #intl-undergrad</sub>

---

**Hiệu suất lượng tử của phản ứng quang hoá** — *Quantum yield of a photochemical reaction*

$$\Phi = \frac{\text{số phân tử biến đổi}}{\text{số photon bị hấp thụ}} = \frac{n_{\text{phản ứng}}}{n_{\text{photon hấp thụ}}};\qquad \sum_{i}\Phi_{i} = 1\ (\text{sơ cấp})$$

Trong đó: `Φ` là hiệu suất lượng tử tổng thể (); `n_phản ứng` là số mol chất biến đổi (mol); `n_photon hấp thụ` là số mol photon bị hấp thụ (einstein) (mol); `Φ_i` là hiệu suất lượng tử của quá trình sơ cấp thứ i ().

*Điều kiện:* Chỉ tính photon THỰC SỰ bị chất khảo sát hấp thụ (định luật Grotthuss - Draper); 1 einstein = 1 mol photon = N_A photon

*Ghi chú:* Atkins Focus 17G. Tổng hiệu suất lượng tử của các quá trình SƠ CẤP bằng 1, nhưng hiệu suất lượng tử TỔNG THỂ có thể rất lớn nếu có phản ứng dây chuyền (ví dụ H2 + Cl2 có Φ khoảng 1e6) hoặc nhỏ hơn 1 nếu có tái hợp. Kho Việt Nam không có động học quang hoá. PHẠM VI: IB Chemistry không có hiệu suất lượng tử quang hoá; đây là nội dung Atkins Focus 17G bậc đại học, nên bản ghi này chỉ gắn intl-undergrad.

<sub>`chemistry.dai-hoc.dong-hoc-nang-cao.hieu-suat-luong-tu-quang-hoa` · lớp 13 · #dong-hoc #quang-hoa #hieu-suat-luong-tu #intl-undergrad</sub>

---

### Động hóa học

**Thứ nguyên của hằng số tốc độ** — *Units of the rate constant*

$$[k] = (\text{mol.L}^{-1})^{1-n}\,\text{s}^{-1}$$

Trong đó: `k` là hằng số tốc độ (mol^(1-n).L^(n-1).s^-1); `n` là bậc tổng của phản ứng ().

*Điều kiện:* Nồng độ tính bằng mol/L, thời gian bằng s

*Ghi chú:* Bậc 0: mol/(L.s); bậc 1: s^-1; bậc 2: L/(mol.s); bậc 3: L^2/(mol^2.s). Nhìn đơn vị của k là đoán được bậc.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.don-vi-hang-so-toc-do` · lớp 13 · #dong-hoc #hang-so-toc-do #don-vi</sub>

---

**Phương trình tốc độ và bậc phản ứng** — *Rate law and reaction order*

$$v = k\,[A]^{m}[B]^{n};\qquad \text{bậc tổng} = m + n$$

Trong đó: `v` là tốc độ phản ứng (mol/(L.s)); `k` là hằng số tốc độ (mol^(1-n).L^(n-1).s^-1); `[A]` là nồng độ các chất phản ứng (mol/L); `[B]` là nồng độ các chất phản ứng (mol/L); `m` là bậc riêng phần theo A (); `n` là bậc riêng phần theo B ().

*Điều kiện:* Bậc phản ứng xác định bằng thực nghiệm, nói chung KHÔNG bằng hệ số tỉ lượng (trừ phản ứng sơ cấp)

*Ghi chú:* Với phản ứng sơ cấp, bậc trùng phân tử số. Bậc có thể là số thập phân, bằng 0 hoặc âm.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phuong-trinh-toc-do` · lớp 13 · #dong-hoc #bac-phan-ung #hang-so-toc-do</sub>

---

**Tốc độ phản ứng theo độ chuyển hóa** — *Rate of reaction (extent-based definition)*

$$v = \frac{1}{V}\frac{d\xi}{dt} = \frac{1}{\nu_{i}}\frac{d[i]}{dt} = -\frac{1}{a}\frac{d[A]}{dt} = \frac{1}{c}\frac{d[C]}{dt}$$

Trong đó: `v` là tốc độ phản ứng (mol/(L.s)); `V` là thể tích hệ (L); `ξ` là độ tiến triển của phản ứng (mol); `t` là thời gian (s); `ν_i` là hệ số tỉ lượng (âm với chất đầu, dương với sản phẩm); `[A]` là nồng độ chất đầu A (mol/L); `[C]` là nồng độ sản phẩm C (mol/L); `a` là hệ số tỉ lượng của A và C; `c` là hệ số tỉ lượng của A và C.

*Điều kiện:* Hệ đồng thể, thể tích không đổi

*Ghi chú:* Định nghĩa này cho một giá trị tốc độ duy nhất, không phụ thuộc chọn chất nào để theo dõi.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.toc-do-phan-ung` · lớp 13 · #dong-hoc #toc-do-phan-ung</sub>

---

**Phương trình động học phản ứng bậc không** — *Integrated rate law for a zero-order reaction*

$$-\frac{d[A]}{dt} = k \;\Rightarrow\; [A] = [A]_{0} - kt$$

Trong đó: `[A]` là nồng độ chất A tại thời điểm t (mol/L); `[A]_0` là nồng độ đầu của A (mol/L); `k` là hằng số tốc độ bậc không (mol/(L.s)); `t` là thời gian (s).

*Điều kiện:* Tốc độ không phụ thuộc nồng độ, thường gặp ở xúc tác dị thể bão hòa bề mặt hoặc xúc tác enzyme khi [S] rất lớn

*Ghi chú:* Đồ thị [A] theo t là đường thẳng hệ số góc -k. Phản ứng kết thúc hoàn toàn sau t = [A]_0/k.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-0` · lớp 13 · #dong-hoc #bac-khong #phuong-trinh-tich-phan</sub>

---

**Phương trình động học phản ứng bậc một** — *Integrated rate law for a first-order reaction*

$$-\frac{d[A]}{dt} = k[A] \;\Rightarrow\; \ln\frac{[A]_{0}}{[A]} = kt \;\Leftrightarrow\; [A] = [A]_{0}e^{-kt}$$

Trong đó: `[A]` là nồng độ A tại thời điểm t (mol/L); `[A]_0` là nồng độ đầu của A (mol/L); `k` là hằng số tốc độ bậc một (s^-1); `t` là thời gian (s).

*Điều kiện:* Phản ứng bậc một theo A; thể tích không đổi

*Ghi chú:* Đồ thị ln[A] theo t là đường thẳng hệ số góc -k. Dùng cho phân rã phóng xạ, thủy phân bậc một, đồng phân hóa.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-1` · lớp 13 · #dong-hoc #bac-mot #phuong-trinh-tich-phan</sub>

---

**Phương trình động học phản ứng bậc hai (một chất hoặc hai chất cùng nồng độ đầu)** — *Integrated second-order rate law (equal initial concentrations)*

$$-\frac{d[A]}{dt} = k[A]^{2} \;\Rightarrow\; \frac{1}{[A]} - \frac{1}{[A]_{0}} = kt$$

Trong đó: `[A]` là nồng độ A tại thời điểm t (mol/L); `[A]_0` là nồng độ đầu (mol/L); `k` là hằng số tốc độ bậc hai (L/(mol.s)); `t` là thời gian (s).

*Điều kiện:* Phản ứng 2A -> sản phẩm hoặc A + B với [A]_0 = [B]_0 và bậc 1 theo mỗi chất

*Ghi chú:* Đồ thị 1/[A] theo t là đường thẳng hệ số góc k. Chú ý: với 2A -> sp, nếu định nghĩa v = -(1/2)d[A]/dt thì hệ số góc là 2k.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-2-cung-nong-do` · lớp 13 · #dong-hoc #bac-hai #phuong-trinh-tich-phan</sub>

---

**Phương trình động học bậc hai với hai chất khác nồng độ đầu** — *Second-order rate law with different initial concentrations*

$$\frac{1}{[B]_{0}-[A]_{0}}\ln\frac{[A]_{0}\,[B]}{[B]_{0}\,[A]} = kt$$

Trong đó: `[A]_0` là nồng độ đầu của A (mol/L); `[B]_0` là nồng độ đầu của B (mol/L); `[A]` là nồng độ A tại thời điểm t (mol/L); `[B]` là nồng độ B tại thời điểm t (mol/L); `k` là hằng số tốc độ bậc hai (L/(mol.s)); `t` là thời gian (s).

*Điều kiện:* Phản ứng A + B -> sản phẩm, bậc 1 theo mỗi chất, [A]_0 khác [B]_0

*Ghi chú:* Với x là lượng đã phản ứng: [A] = [A]_0 - x, [B] = [B]_0 - x. Nếu [B]_0 >> [A]_0 thì phản ứng trở thành giả bậc một với k' = k[B]_0.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-2-khac-nong-do` · lớp 13 · #dong-hoc #bac-hai #phuong-trinh-tich-phan</sub>

---

**Phương trình động học phản ứng bậc ba (cùng nồng độ đầu)** — *Integrated third-order rate law (equal initial concentrations)*

$$-\frac{d[A]}{dt} = k[A]^{3} \;\Rightarrow\; \frac{1}{[A]^{2}} - \frac{1}{[A]_{0}^{2}} = 2kt;\qquad t_{1/2} = \frac{3}{2k[A]_{0}^{2}}$$

Trong đó: `[A]` là nồng độ A tại thời điểm t (mol/L); `[A]_0` là nồng độ đầu (mol/L); `k` là hằng số tốc độ bậc ba (L^2/(mol^2.s)); `t` là thời gian (s); `t_1/2` là thời gian bán hủy (s).

*Điều kiện:* Phản ứng bậc ba theo một chất hoặc ba chất cùng nồng độ đầu

*Ghi chú:* Phản ứng bậc ba rất hiếm, ví dụ 2NO + O2 -> 2NO2.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.dong-hoc-bac-3` · lớp 13 · #dong-hoc #bac-ba #phuong-trinh-tich-phan</sub>

---

**Nguyên lí nồng độ ổn định (Bodenstein)** — *Steady-state approximation*

$$\frac{d[I]}{dt} \approx 0 \;\Rightarrow\; [I]_{ss} = \frac{\text{tốc độ sinh ra I}}{\text{tổng hệ số tốc độ tiêu thụ I}}$$

Trong đó: `[I]` là nồng độ tiểu phân trung gian hoạt động (mol/L); `[I]_ss` là nồng độ ổn định của tiểu phân trung gian (mol/L); `t` là thời gian (s).

*Điều kiện:* Tiểu phân trung gian rất hoạt động, nồng độ rất nhỏ và gần như không đổi sau giai đoạn cảm ứng

*Ghi chú:* Ví dụ cơ chế Lindemann cho phản ứng đơn phân tử: k_hiệu dụng = k_1k_2[M]/(k_-1[M] + k_2), cho bậc 2 ở áp suất thấp và bậc 1 ở áp suất cao.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.nguyen-li-nong-do-on-dinh` · lớp 13 · #dong-hoc #co-che #nong-do-on-dinh</sub>

---

**Độ dài mạch của phản ứng dây chuyền** — *Chain length of a chain reaction*

$$\nu = \frac{v_{\text{tổng}}}{v_{\text{khơi mào}}} = \frac{v_{\text{phát triển mạch}}}{v_{\text{tắt mạch}}}$$

Trong đó: `ν` là độ dài mạch (số lần lặp mắt xích trên một tiểu phân khơi mào) (); `v_tổng` là tốc độ tiêu thụ chất đầu (mol/(L.s)); `v_khơi mào` là tốc độ giai đoạn khơi mào (mol/(L.s)); `v_phát triển mạch` là tốc độ giai đoạn phát triển mạch; `v_tắt mạch` là tốc độ giai đoạn tắt mạch.

*Điều kiện:* Phản ứng dây chuyền ở trạng thái ổn định (tốc độ khơi mào bằng tốc độ tắt mạch)

*Ghi chú:* Ba giai đoạn: khơi mào - phát triển mạch - tắt mạch. Với mạch phân nhánh (H2 + O2), độ dài mạch tăng vô hạn gây nổ.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phan-ung-day-chuyen` · lớp 13 · #dong-hoc #day-chuyen #goc-tu-do</sub>

---

**Động học phản ứng nối tiếp bậc một** — *Kinetics of consecutive first-order reactions*

$$A\xrightarrow{k_{1}}B\xrightarrow{k_{2}}C:\quad [B] = \frac{k_{1}[A]_{0}}{k_{2}-k_{1}}\left(e^{-k_{1}t}-e^{-k_{2}t}\right);\quad t_{max} = \frac{\ln(k_{2}/k_{1})}{k_{2}-k_{1}}$$

Trong đó: `[A]_0` là nồng độ đầu của A (mol/L); `[B]` là nồng độ chất trung gian B (mol/L); `k_1` là hằng số tốc độ giai đoạn 1 (s^-1); `k_2` là hằng số tốc độ giai đoạn 2 (s^-1); `t` là thời gian (s); `t_max` là thời điểm nồng độ B đạt cực đại (s).

*Điều kiện:* Hai giai đoạn nối tiếp bậc một, không thuận nghịch, k_1 khác k_2; ban đầu chỉ có A

*Ghi chú:* Nếu k_2 >> k_1 thì B là chất trung gian hoạt động, có thể dùng nguyên lí nồng độ ổn định. Giai đoạn chậm nhất là giai đoạn quyết định tốc độ.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phan-ung-noi-tiep` · lớp 13 · #dong-hoc #noi-tiep #trung-gian</sub>

---

**Động học phản ứng song song bậc một** — *Kinetics of parallel first-order reactions*

$$[A] = [A]_{0}e^{-(k_{1}+k_{2})t};\qquad \frac{[B]}{[C]} = \frac{k_{1}}{k_{2}};\qquad \text{độ chọn lọc } = \frac{k_{1}}{k_{1}+k_{2}}$$

Trong đó: `[A]` là nồng độ chất đầu tại thời điểm t (mol/L); `[A]_0` là nồng độ đầu của A (mol/L); `k_1` là hằng số tốc độ tạo B (s^-1); `k_2` là hằng số tốc độ tạo C (s^-1); `[B]` là nồng độ sản phẩm B (mol/L); `[C]` là nồng độ sản phẩm C (mol/L); `t` là thời gian (s).

*Điều kiện:* Hai (hoặc nhiều) phản ứng bậc một cạnh tranh cùng chất đầu, không thuận nghịch

*Ghi chú:* Tỉ lệ sản phẩm không đổi theo thời gian (khống chế động học). Thời gian bán hủy chung t_1/2 = ln2/(k_1 + k_2).

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phan-ung-song-song` · lớp 13 · #dong-hoc #song-song #do-chon-loc</sub>

---

**Động học phản ứng thuận nghịch bậc một** — *Kinetics of a reversible first-order reaction*

$$A \underset{k_{-1}}{\overset{k_{1}}{\rightleftharpoons}} B:\qquad \ln\frac{x_{e}}{x_{e}-x} = (k_{1}+k_{-1})t;\qquad K = \frac{k_{1}}{k_{-1}} = \frac{x_{e}}{[A]_{0}-x_{e}}$$

Trong đó: `k_1` là hằng số tốc độ phản ứng thuận (s^-1); `k_-1` là hằng số tốc độ phản ứng nghịch (s^-1); `x` là lượng A đã chuyển thành B tại thời điểm t (mol/L); `x_e` là lượng đã chuyển hóa lúc cân bằng (mol/L); `t` là thời gian (s); `K` là hằng số cân bằng (); `[A]_0` là nồng độ A ban đầu (mol/L).

*Điều kiện:* Cả hai chiều đều bậc một; ban đầu chỉ có A

*Ghi chú:* Hệ tiến tới cân bằng theo hàm mũ với hằng số hồi phục τ = 1/(k_1 + k_-1). Kết hợp với K = k_1/k_-1 để tách riêng từng hằng số tốc độ.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phan-ung-thuan-nghich-bac-1` · lớp 13 · #dong-hoc #thuan-nghich #phan-ung-phuc-tap</sub>

---

**Phương trình Eyring (thuyết trạng thái chuyển tiếp)** — *Eyring equation (transition state theory)*

$$k = \frac{k_{B}T}{h}\,K^{\ddagger} = \frac{k_{B}T}{h}\,e^{\Delta S^{\ddagger}/R}\,e^{-\Delta H^{\ddagger}/(RT)}$$

Trong đó: `k` là hằng số tốc độ (s^-1); `k_B` là hằng số Boltzmann (J/K); `h` là hằng số Planck (J.s); `T` là nhiệt độ tuyệt đối (K); `K‡` là hằng số cân bằng tạo phức hoạt động (); `ΔS‡` là entropy hoạt hóa (J/(mol.K)); `ΔH‡` là enthalpy hoạt hóa (J/mol); `R` là hằng số khí (J/(mol.K)).

*Điều kiện:* Phức hoạt động ở cân bằng giả với chất đầu; hệ số truyền qua κ coi bằng 1

*Ghi chú:* k_B = 1.381e-23 J/K, h = 6.626e-34 J.s. Ở 298 K, k_B.T/h ≈ 6.21e12 s^-1. Dạng logarit: ln(k/T) = -ΔH‡/(RT) + ln(k_B/h) + ΔS‡/R.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phuong-trinh-eyring` · lớp 13 · #dong-hoc #eyring #trang-thai-chuyen-tiep</sub>

---

**Quan hệ giữa năng lượng hoạt hóa Arrhenius và enthalpy hoạt hóa** — *Relation between Arrhenius activation energy and activation enthalpy*

$$E_{a} = \Delta H^{\ddagger} + (1 - \Delta n^{\ddagger})RT;\qquad \text{phản ứng trong dung dịch hoặc đơn phân tử: } E_{a} = \Delta H^{\ddagger} + RT$$

Trong đó: `E_a` là năng lượng hoạt hóa Arrhenius (J/mol); `ΔH‡` là enthalpy hoạt hóa (J/mol); `Δn‡` là biến thiên số mol tiểu phân khi tạo phức hoạt động, Δn‡ = 1 - phân tử số (bằng 0 cho phản ứng đơn phân tử, -1 cho lưỡng phân tử pha khí) (); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Áp dụng cho phương trình Eyring viết theo thang nồng độ; suy từ E_a = RT^2.dlnk/dT

*Ghi chú:* Phản ứng lưỡng phân tử pha khí (Δn‡ = -1): E_a = ΔH‡ + 2RT. Thừa số A liên hệ với ΔS‡: A = e^(1-Δn‡).(k_B T/h).e^(ΔS‡/R); riêng phản ứng đơn phân tử A = e.(k_B T/h).e^(ΔS‡/R).

<sub>`chemistry.dai-hoc.dong-hoa-hoc.quan-he-ea-enthalpy-hoat-hoa` · lớp 13 · #dong-hoc #eyring #nang-luong-hoat-hoa</sub>

---

**Thuyết va chạm hoạt động** — *Collision theory*

$$k = P\,Z_{0}\,e^{-E_{a}/(RT)};\qquad Z_{0} = N_{A}\sigma\sqrt{\frac{8k_{B}T}{\pi\mu}}$$

Trong đó: `k` là hằng số tốc độ (m^3/(mol.s)); `P` là thừa số định hướng (thừa số không gian, P ≤ 1) (); `Z_0` là tần số va chạm ứng với nồng độ đơn vị (m^3/(mol.s)); `E_a` là năng lượng hoạt hóa (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K); `N_A` là số Avogadro (mol^-1); `σ` là tiết diện va chạm (m^2); `k_B` là hằng số Boltzmann (J/K); `μ` là khối lượng rút gọn của cặp phân tử va chạm (kg).

*Điều kiện:* Phản ứng lưỡng phân tử trong pha khí; phân tử coi như quả cầu cứng; các đại lượng tính theo hệ SI

*Ghi chú:* N_A = 6.022e23 mol^-1, k_B = 1.381e-23 J/K. Công thức cho Z_0 theo SI có đơn vị m^3/(mol.s); đổi sang đơn vị thực dụng: 1 m^3/(mol.s) = 1000 L/(mol.s). Tần số va chạm tỉ lệ với căn bậc hai của T, nhưng thừa số mũ mới quyết định sự phụ thuộc nhiệt độ.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.thuyet-va-cham-hoat-dong` · lớp 13 · #dong-hoc #thuyet-va-cham #nang-luong-hoat-hoa</sub>

---

**Thời gian bán hủy của phản ứng bậc không** — *Half-life of a zero-order reaction*

$$t_{1/2} = \frac{[A]_{0}}{2k}$$

Trong đó: `t_1/2` là thời gian bán hủy (s); `[A]_0` là nồng độ đầu (mol/L); `k` là hằng số tốc độ bậc không (mol/(L.s)).

*Điều kiện:* Phản ứng bậc không theo A

*Ghi chú:* t_1/2 tỉ lệ thuận với nồng độ đầu - dấu hiệu nhận biết bậc không.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-0` · lớp 13 · #dong-hoc #bac-khong #ban-huy</sub>

---

**Thời gian bán hủy của phản ứng bậc một** — *Half-life of a first-order reaction*

$$t_{1/2} = \frac{\ln 2}{k} \approx \frac{0.693}{k}$$

Trong đó: `t_1/2` là thời gian bán hủy (s); `k` là hằng số tốc độ bậc một (s^-1).

*Điều kiện:* Phản ứng bậc một

*Ghi chú:* Đặc trưng: t_1/2 KHÔNG phụ thuộc nồng độ đầu - dấu hiệu nhận biết bậc một. Sau n chu kì bán hủy còn lại [A]_0/2^n.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-1` · lớp 13 · #dong-hoc #bac-mot #ban-huy</sub>

---

**Thời gian bán hủy của phản ứng bậc hai** — *Half-life of a second-order reaction*

$$t_{1/2} = \frac{1}{k\,[A]_{0}}$$

Trong đó: `t_1/2` là thời gian bán hủy (s); `k` là hằng số tốc độ bậc hai (L/(mol.s)); `[A]_0` là nồng độ đầu (mol/L).

*Điều kiện:* Phản ứng bậc hai với một chất phản ứng (hoặc hai chất cùng nồng độ đầu)

*Ghi chú:* t_1/2 tỉ lệ nghịch với nồng độ đầu - dấu hiệu nhận biết bậc hai.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-2` · lớp 13 · #dong-hoc #bac-hai #ban-huy</sub>

---

**Phương trình động học và thời gian bán hủy phản ứng bậc n** — *Integrated rate law and half-life for order n*

$$\frac{1}{[A]^{n-1}} - \frac{1}{[A]_{0}^{n-1}} = (n-1)kt;\qquad t_{1/2} = \frac{2^{n-1}-1}{(n-1)k[A]_{0}^{n-1}}$$

Trong đó: `[A]` là nồng độ A tại thời điểm t (mol/L); `[A]_0` là nồng độ đầu (mol/L); `n` là bậc phản ứng (); `k` là hằng số tốc độ (mol^(1-n).L^(n-1).s^-1); `t` là thời gian (s); `t_1/2` là thời gian bán hủy (s).

*Điều kiện:* n khác 1 (với n = 1 dùng công thức logarit)

*Ghi chú:* Tổng quát t_1/2 tỉ lệ với [A]_0^(1-n). Lấy logarit: ln t_1/2 = const + (1-n)ln[A]_0 - đó là phương pháp bán hủy để xác định bậc.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.ban-huy-bac-n` · lớp 13 · #dong-hoc #bac-n #ban-huy</sub>

---

**Thời gian sống trung bình của phản ứng bậc một** — *Mean lifetime of a first-order process*

$$\tau = \frac{1}{k} = \frac{t_{1/2}}{\ln 2}$$

Trong đó: `τ` là thời gian sống trung bình (s); `k` là hằng số tốc độ bậc một (s^-1); `t_1/2` là thời gian bán hủy (s).

*Điều kiện:* Quá trình bậc một (phân rã, hồi phục)

*Ghi chú:* Sau thời gian τ, nồng độ còn lại [A]_0/e ≈ 36.8% nồng độ đầu.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.thoi-gian-song-trung-binh` · lớp 13 · #dong-hoc #bac-mot #thoi-gian-song</sub>

---

**Phương pháp thời gian bán hủy xác định bậc phản ứng** — *Half-life method for reaction order*

$$n = 1 + \frac{\ln\left(t_{1/2}^{(1)}/t_{1/2}^{(2)}\right)}{\ln\left([A]_{0}^{(2)}/[A]_{0}^{(1)}\right)}$$

Trong đó: `n` là bậc phản ứng (); `t_1/2^(1)` là thời gian bán hủy ứng với nồng độ đầu thứ nhất (s); `t_1/2^(2)` là thời gian bán hủy ứng với nồng độ đầu thứ hai (s); `[A]_0^(1)` là nồng độ đầu thứ nhất (mol/L); `[A]_0^(2)` là nồng độ đầu thứ hai (mol/L).

*Điều kiện:* Chỉ có một chất phản ứng hoặc các chất khác lấy dư; cùng nhiệt độ

*Ghi chú:* Suy từ t_1/2 tỉ lệ với [A]_0^(1-n).

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phuong-phap-ban-huy` · lớp 13 · #dong-hoc #bac-phan-ung #ban-huy</sub>

---

**Phương pháp cô lập Ostwald (giả bậc)** — *Ostwald isolation method (pseudo-order)*

$$[B]_{0} \gg [A]_{0} \Rightarrow v = k[A]^{m}[B]^{n} \approx k'[A]^{m},\quad k' = k[B]_{0}^{n}$$

Trong đó: `v` là tốc độ phản ứng (mol/(L.s)); `k` là hằng số tốc độ thực (mol^(1-n).L^(n-1).s^-1); `k'` là hằng số tốc độ biểu kiến (giả bậc) (s^-1); `[A]` là nồng độ chất được cô lập (mol/L); `[B]_0` là nồng độ chất lấy dư (mol/L); `m` là bậc theo A; `n` là bậc theo B.

*Điều kiện:* Nồng độ chất B lớn hơn nhiều lần (thường 10 lần trở lên) để coi như không đổi trong suốt phản ứng

*Ghi chú:* Ví dụ thủy phân ester trong nước dư là phản ứng giả bậc một dù thực chất bậc hai.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phuong-phap-co-lap` · lớp 13 · #dong-hoc #bac-phan-ung #gia-bac</sub>

---

**Phương pháp tốc độ đầu xác định bậc phản ứng** — *Initial-rate method for determining reaction order*

$$m = \frac{\ln(v_{2}/v_{1})}{\ln([A]_{2}/[A]_{1})}$$

Trong đó: `m` là bậc riêng phần theo chất A (); `v_1` là tốc độ đầu ở nồng độ [A]_1 (mol/(L.s)); `v_2` là tốc độ đầu ở nồng độ [A]_2 (mol/(L.s)); `[A]_1` là nồng độ đầu thí nghiệm 1 (mol/L); `[A]_2` là nồng độ đầu thí nghiệm 2 (mol/L).

*Điều kiện:* Chỉ thay đổi nồng độ của chất A, giữ nguyên nồng độ các chất khác và nhiệt độ

*Ghi chú:* Nếu tăng gấp đôi [A] mà v không đổi thì m = 0; v gấp đôi thì m = 1; v gấp bốn thì m = 2.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.phuong-phap-toc-do-dau` · lớp 13 · #dong-hoc #bac-phan-ung #thuc-nghiem</sub>

---

**Động học xúc tác dị thể theo cơ chế Langmuir - Hinshelwood** — *Langmuir - Hinshelwood kinetics of heterogeneous catalysis*

$$v = k\,\theta_{A}\theta_{B} = k\,\frac{b_{A}p_{A}\,b_{B}p_{B}}{\left(1 + b_{A}p_{A} + b_{B}p_{B}\right)^{2}};\qquad \text{một chất phản ứng: } v = k\,\frac{bp}{1+bp}$$

Trong đó: `v` là tốc độ phản ứng trên bề mặt xúc tác (mol/(g.s)); `k` là hằng số tốc độ của phản ứng bề mặt (mol/(g.s)); `θ_A` là độ che phủ bề mặt bởi chất A (); `θ_B` là độ che phủ bề mặt bởi chất B (); `b_A` là hằng số hấp phụ Langmuir của A (Pa^-1); `b_B` là hằng số hấp phụ Langmuir của B (Pa^-1); `p_A` là áp suất riêng phần của A (Pa); `p_B` là áp suất riêng phần của B (Pa); `b` là hằng số hấp phụ của chất phản ứng duy nhất (Pa^-1); `p` là áp suất của chất phản ứng duy nhất (Pa).

*Điều kiện:* Xúc tác dị thể; hấp phụ tuân theo đẳng nhiệt Langmuir (đơn lớp, bề mặt đồng nhất); giai đoạn quyết định tốc độ là phản ứng giữa hai tiểu phân đã hấp phụ cạnh nhau; bỏ qua khuếch tán ngoài và trong hạt

*Ghi chú:* Áp suất thấp (bp << 1): bậc một theo mỗi chất. Áp suất cao: bậc không (bề mặt bão hòa). Nếu một chất hấp phụ quá mạnh nó tự kìm hãm phản ứng: tốc độ giảm khi tăng áp suất chất đó (bậc âm biểu kiến). Cơ chế Eley - Rideal (một chất hấp phụ, một chất ở pha khí): v = k.θ_A.p_B.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.xuc-tac-di-the-langmuir-hinshelwood` · lớp 13 · #dong-hoc #xuc-tac #di-the #langmuir-hinshelwood</sub>

---

**Xúc tác đồng thể axit - bazơ và hệ thức Brønsted** — *Homogeneous acid - base catalysis and the Brønsted catalysis law*

$$k_{qs} = k_{0} + k_{\mathrm{H}^{+}}[\mathrm{H}^{+}] + k_{\mathrm{OH}^{-}}[\mathrm{OH}^{-}] + k_{\mathrm{HA}}[\mathrm{HA}] + k_{\mathrm{A}^{-}}[\mathrm{A}^{-}];\qquad \lg k_{\mathrm{HA}} = \alpha\lg K_{a} + \text{const}$$

Trong đó: `k_qs` là hằng số tốc độ biểu kiến (giả bậc một) quan sát được (s^-1); `k_0` là hằng số tốc độ của phản ứng không xúc tác (do dung môi) (s^-1); `k_H+` là hằng số xúc tác của ion H+ (xúc tác axit đặc hiệu) (L/(mol.s)); `k_OH-` là hằng số xúc tác của ion OH- (xúc tác bazơ đặc hiệu) (L/(mol.s)); `k_HA` là hằng số xúc tác của axit yếu HA (xúc tác axit chung) (L/(mol.s)); `k_A-` là hằng số xúc tác của bazơ liên hợp A- (xúc tác bazơ chung) (L/(mol.s)); `[H+]` là nồng độ ion H+ (mol/L); `[OH-]` là nồng độ ion OH- (mol/L); `[HA]` là nồng độ axit yếu (mol/L); `[A-]` là nồng độ bazơ liên hợp (mol/L); `α` là hệ số Brønsted (0 < α < 1) (); `K_a` là hằng số axit của chất xúc tác HA (mol/L).

*Điều kiện:* Phản ứng trong dung dịch, chất xúc tác lấy dư nên nồng độ coi như không đổi (điều kiện giả bậc một); hệ thức Brønsted chỉ đúng trong một dãy axit cùng loại với 0 < α < 1

*Ghi chú:* Xúc tác axit đặc hiệu: k_qs = k_H+[H+] nên lg k_qs = lg k_H+ - pH (đồ thị lg k theo pH có hệ số góc -1). Xúc tác bazơ đặc hiệu cho hệ số góc +1. Hệ thức Brønsted cho bazơ: lg k_B = -β.lg K_a + const. Xúc tác càng mạnh khi axit càng mạnh.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.xuc-tac-dong-the-axit-bazo` · lớp 13 · #dong-hoc #xuc-tac #axit-bazo #bronsted</sub>

---

**Ảnh hưởng của xúc tác lên hằng số tốc độ** — *Effect of a catalyst on the rate constant*

$$\frac{k_{xt}}{k} = \frac{A_{xt}}{A}\exp\left(\frac{E_{a} - E_{a,xt}}{RT}\right)$$

Trong đó: `k_xt` là hằng số tốc độ khi có xúc tác (); `k` là hằng số tốc độ khi không xúc tác (); `A_xt` là thừa số trước lũy thừa của phản ứng xúc tác; `A` là thừa số trước lũy thừa của phản ứng không xúc tác; `E_a` là năng lượng hoạt hóa khi không xúc tác (J/mol); `xt` là năng lượng hoạt hóa khi có xúc tác (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* So sánh ở cùng nhiệt độ; nếu coi A_xt ≈ A thì tỉ số bằng exp((E_a - E_a,xt)/RT)

*Ghi chú:* Xúc tác chỉ làm tăng tốc độ (giảm Ea của cả chiều thuận lẫn nghịch), KHÔNG làm chuyển dịch cân bằng và không đổi ΔG.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.xuc-tac-giam-nang-luong-hoat-hoa` · lớp 13 · #dong-hoc #xuc-tac #nang-luong-hoat-hoa</sub>

---

**Phương trình Lineweaver - Burk (đồ thị nghịch đảo kép)** — *Lineweaver - Burk equation*

$$\frac{1}{v} = \frac{K_{M}}{V_{max}}\cdot\frac{1}{[S]} + \frac{1}{V_{max}}$$

Trong đó: `v` là tốc độ đầu (mol/(L.s)); `V_max` là tốc độ cực đại (mol/(L.s)); `K_M` là hằng số Michaelis (mol/L); `[S]` là nồng độ cơ chất (mol/L).

*Điều kiện:* Động học Michaelis - Menten tuân theo đúng; số liệu ở nhiều nồng độ cơ chất

*Ghi chú:* Đồ thị 1/v theo 1/[S] là đường thẳng: tung độ gốc 1/V_max, hoành độ gốc -1/K_M, hệ số góc K_M/V_max. Dùng phân biệt kiểu ức chế cạnh tranh và không cạnh tranh.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.lineweaver-burk` · lớp 13 · #dong-hoc #enzyme #do-thi</sub>

---

**Phương trình Michaelis - Menten** — *Michaelis - Menten equation*

$$v = \frac{V_{max}[S]}{K_{M} + [S]};\qquad K_{M} = \frac{k_{-1}+k_{2}}{k_{1}};\qquad V_{max} = k_{cat}[E]_{0}$$

Trong đó: `v` là tốc độ đầu của phản ứng enzyme (mol/(L.s)); `V_max` là tốc độ cực đại (khi enzyme bão hòa cơ chất) (mol/(L.s)); `[S]` là nồng độ cơ chất (mol/L); `K_M` là hằng số Michaelis (mol/L); `k_1` là hằng số tốc độ tạo phức ES (L/(mol.s)); `k_-1` là hằng số tốc độ phân li phức ES (s^-1); `k_2` là hằng số tốc độ giai đoạn tạo sản phẩm từ ES (s^-1); `k_cat` là hằng số tốc độ xúc tác (số vòng quay), với cơ chế đơn giản k_cat = k_2 (s^-1); `[E]_0` là nồng độ enzyme tổng (mol/L).

*Điều kiện:* Áp dụng nguyên lí nồng độ ổn định cho phức enzyme - cơ chất ES; [S] >> [E]_0; đo tốc độ đầu

*Ghi chú:* Khi [S] = K_M thì v = V_max/2. Khi [S] << K_M: bậc một theo [S]; khi [S] >> K_M: bậc không. Hiệu quả xúc tác đánh giá bằng k_cat/K_M.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.michaelis-menten` · lớp 13 · #dong-hoc #enzyme #michaelis-menten</sub>

---

**Ức chế cạnh tranh trong động học enzyme** — *Competitive inhibition in enzyme kinetics*

$$v = \frac{V_{max}[S]}{\alpha K_{M} + [S]};\qquad \alpha = 1 + \frac{[I]}{K_{I}};\qquad K_{I} = \frac{[E][I]}{[EI]}$$

Trong đó: `v` là tốc độ đầu khi có mặt chất ức chế (mol/(L.s)); `V_max` là tốc độ cực đại (không đổi khi ức chế cạnh tranh) (mol/(L.s)); `[S]` là nồng độ cơ chất (mol/L); `K_M` là hằng số Michaelis khi không có chất ức chế (mol/L); `α` là hệ số ức chế; K_M biểu kiến bằng αK_M (); `[I]` là nồng độ chất ức chế tự do (mol/L); `K_I` là hằng số phân li của phức enzyme - chất ức chế EI (mol/L); `[E]` là nồng độ enzyme tự do (mol/L); `[EI]` là nồng độ phức enzyme - chất ức chế (mol/L).

*Điều kiện:* Chất ức chế gắn thuận nghịch vào tâm hoạt động của enzyme tự do (cạnh tranh với cơ chất); vẫn áp dụng nguyên lí nồng độ ổn định của Michaelis - Menten; [I] >> [E]_0

*Ghi chú:* Ức chế cạnh tranh làm tăng K_M biểu kiến nhưng KHÔNG đổi V_max, nên có thể khắc phục bằng cách tăng [S]. Ức chế không cạnh tranh thuần túy thì ngược lại: V_max giảm còn V_max/α, K_M không đổi. Trên đồ thị Lineweaver - Burk, các đường thẳng của ức chế cạnh tranh cắt nhau tại cùng tung độ gốc 1/V_max.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.uc-che-enzyme-canh-tranh` · lớp 13 · #dong-hoc #enzyme #uc-che</sub>

---

**Phương trình Arrhenius dạng logarit** — *Arrhenius equation (logarithmic form)*

$$\ln k = \ln A - \frac{E_{a}}{RT};\qquad \lg k = \lg A - \frac{E_{a}}{2.303\,RT}$$

Trong đó: `k` là hằng số tốc độ (mol^(1-n).L^(n-1).s^-1); `A` là thừa số trước lũy thừa (cùng đơn vị với k); `E_a` là năng lượng hoạt hóa (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* Khoảng nhiệt độ không quá rộng

*Ghi chú:* Đồ thị lnk theo 1/T (đồ thị Arrhenius) là đường thẳng hệ số góc -E_a/R, tung độ gốc lnA.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.arrhenius-dang-logarit` · lớp 13 · #dong-hoc #arrhenius #do-thi</sub>

---

**Phương trình Arrhenius dạng mũ** — *Arrhenius equation (exponential form)*

$$k = A\,e^{-E_{a}/(RT)}$$

Trong đó: `k` là hằng số tốc độ (mol^(1-n).L^(n-1).s^-1); `A` là thừa số trước lũy thừa (thừa số tần số) (cùng đơn vị với k); `E_a` là năng lượng hoạt hóa (J/mol); `R` là hằng số khí (J/(mol.K)); `T` là nhiệt độ tuyệt đối (K).

*Điều kiện:* A và E_a coi như không phụ thuộc nhiệt độ trong khoảng khảo sát

*Ghi chú:* Thừa số e^(-Ea/RT) là phần phân tử có năng lượng vượt rào thế. E_a càng lớn thì k càng nhạy với nhiệt độ.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.arrhenius-dang-mu` · lớp 13 · #dong-hoc #arrhenius #nang-luong-hoat-hoa</sub>

---

**Tính năng lượng hoạt hóa từ hằng số tốc độ ở hai nhiệt độ** — *Activation energy from rate constants at two temperatures*

$$\ln\frac{k_{2}}{k_{1}} = \frac{E_{a}}{R}\left(\frac{1}{T_{1}} - \frac{1}{T_{2}}\right) = \frac{E_{a}}{R}\cdot\frac{T_{2}-T_{1}}{T_{1}T_{2}}$$

Trong đó: `k_1` là hằng số tốc độ ở T1 (); `k_2` là hằng số tốc độ ở T2 (); `E_a` là năng lượng hoạt hóa (J/mol); `R` là hằng số khí (J/(mol.K)); `T1` là nhiệt độ thứ nhất (K); `T2` là nhiệt độ thứ hai (K).

*Điều kiện:* E_a không đổi trong khoảng T1 - T2

*Ghi chú:* Dạng tương tự phương trình đẳng áp Van't Hoff nhưng dấu ngược (vì Ea ở tử số dương). R = 8.314 J/(mol.K).

<sub>`chemistry.dai-hoc.dong-hoa-hoc.arrhenius-hai-nhiet-do` · lớp 13 · #dong-hoc #arrhenius #nang-luong-hoat-hoa</sub>

---

**Hệ số nhiệt độ Van't Hoff của tốc độ phản ứng** — *Van't Hoff temperature coefficient*

$$\gamma = \frac{k_{T+10}}{k_{T}};\qquad \frac{k_{T_{2}}}{k_{T_{1}}} = \gamma^{\frac{T_{2}-T_{1}}{10}}$$

Trong đó: `γ` là hệ số nhiệt độ (thường 2 - 4) (); `k_T` là hằng số tốc độ ở nhiệt độ T (); `k_(T+10)` là hằng số tốc độ ở nhiệt độ T + 10 K; `T1` là nhiệt độ đầu (K); `T2` là nhiệt độ sau (K).

*Điều kiện:* Quy tắc thực nghiệm gần đúng, dùng trong khoảng nhiệt độ hẹp gần nhiệt độ phòng

*Ghi chú:* Quy tắc kinh nghiệm: tăng 10 độ thì tốc độ phản ứng tăng 2 - 4 lần.

<sub>`chemistry.dai-hoc.dong-hoa-hoc.he-so-nhiet-do-vant-hoff` · lớp 13 · #dong-hoc #nhiet-do #vant-hoff</sub>

---
