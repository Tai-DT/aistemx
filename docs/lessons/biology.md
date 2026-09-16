# Sinh học — Bài học AISTEM

Tổng số: **147** bài. Sinh tự động bằng `tools/build_content_index.py`.

## Chủ đề: Di truyền

### 1. Lai một cặp tính trạng và xác suất di truyền đơn giản
*Monohybrid cross and simple genetic probability* · THCS · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được tỉ lệ kiểu hình đời con trong phép lai một cặp tính trạng theo quy luật phân li
- Tính được xác suất xuất hiện một tính trạng ở đời con bằng suy luận đơn giản

## Menđen và cây đậu Hà Lan

Menđen lai đậu **hoa đỏ** thuần chủng với **hoa trắng** thuần chủng. Đời $F_1$ toàn hoa đỏ — đỏ là **tính trạng trội** (kí hiệu $A$), trắng là **lặn** ($a$).

## Vì sao $F_2$ có tỉ lệ 3 : 1

Cho $F_1$ ($Aa$) tự thụ phấn. Mỗi cây cho hai loại giao tử $A$ và $a$ với tỉ lệ bằng nhau. Kẻ **khung Punnett**:

| | A | a |
|---|---|---|
| **A** | AA | Aa |
| **a** | Aa | aa |

Đời $F_2$ có kiểu gen $1\,AA : 2\,Aa : 1\,aa$. Vì $A$ trội, ba tổ hợp đầu ($AA, Aa, Aa$) đều cho hoa đỏ, chỉ $aa$ cho hoa trắng. Vậy **kiểu hình 3 đỏ : 1 trắng**.

## Từ tỉ lệ sang xác suất

Tỉ lệ $3:1$ nghĩa là xác suất cây $F_2$ hoa trắng là $\dfrac{1}{4} = 25\%$, hoa đỏ là $\dfrac{3}{4} = 75\%$. Với một số cây $F_2$ đủ lớn, số cây hoa trắng gần bằng $\dfrac{1}{4}$ tổng số. Đây là cách dùng xác suất để dự đoán kết quả lai.

**Lỗi thường gặp:**
- Viết tỉ lệ kiểu gen (1:2:1) thành tỉ lệ kiểu hình; kiểu hình trội : lặn là 3 : 1.
- Cho rằng đúng 1/4 số cây là hoa trắng; thực tế chỉ xấp xỉ vì đây là xác suất, số mẫu càng lớn càng gần.
- Nhầm tính trạng trội luôn chiếm đa số kiểu gen; thực ra $F_2$ có 2 phần dị hợp $Aa$ vẫn biểu hiện trội.

<sub>`lesson.biology.thcs-hoa-sinh.lai-mot-cap-tinh-trang-va-xac-suat`</sub>

---

## Chủ đề: Sinh lí người

### 1. Chỉ số BMI và nhu cầu năng lượng của cơ thể
*BMI and the body's energy needs* · THCS · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Tính được chỉ số khối cơ thể BMI và nhận xét về thể trạng
- Ước lượng được giá trị năng lượng của khẩu phần ăn từ khối lượng các chất dinh dưỡng

## BMI: cơ thể cân đối chưa

**Chỉ số khối cơ thể** BMI giúp đánh giá nhanh cân nặng so với chiều cao:

$$BMI = \frac{m}{h^2}$$

với $m$ là cân nặng (kg), $h$ là chiều cao (**mét**). Với người trưởng thành, BMI bình thường khoảng $18{,}5$ đến $25$; dưới là gầy, trên là thừa cân. (Ở tuổi thiếu niên còn phải so với bảng theo tuổi.)

## Đừng để sai đơn vị chiều cao

Lỗi phổ biến nhất là để chiều cao bằng centimet. Phải đổi ra mét: cao $160$ cm nghĩa là $h = 1{,}6$ m.

## Năng lượng từ thức ăn

Cơ thể cần năng lượng đo bằng kilocalo (kcal). Mỗi loại chất dinh dưỡng cho lượng khác nhau:

- 1 g carbohydrate: khoảng 4 kcal
- 1 g protein: khoảng 4 kcal
- 1 g chất béo (lipid): khoảng 9 kcal

Tổng năng lượng khẩu phần bằng tổng năng lượng của từng nhóm chất. Đối chiếu với **nhu cầu năng lượng** hằng ngày để ăn uống hợp lí, tránh thừa hay thiếu.

**Lỗi thường gặp:**
- Để chiều cao bằng centimet khi tính BMI nên kết quả nhỏ hơn thật hàng chục nghìn lần.
- Quên bình phương chiều cao (chia cho $h$ thay vì $h^2$).
- Dùng 4 kcal cho chất béo; chất béo cho tới 9 kcal mỗi gam.

<sub>`lesson.biology.thcs-hoa-sinh.bmi-va-nhu-cau-nang-luong`</sub>

---

### 2. Nhịp tim, lưu lượng tim và thông khí phổi
*Heart rate, cardiac output and pulmonary ventilation* · THCS · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Tính được lưu lượng tim từ thể tích tâm thu và nhịp tim
- Tính được lượng khí thông khí phổi trong một phút từ thể tích khí lưu thông và nhịp thở

## Tim bơm được bao nhiêu máu mỗi phút

Mỗi lần đập, tim đẩy đi một lượng máu gọi là **thể tích tâm thu** $Q_s$ (thường khoảng 70 mL ở người lớn). Nhân với **nhịp tim** $f$ ta được **lưu lượng tim** — lượng máu bơm trong một phút:

$$Q = Q_s\times f$$

Ví dụ tim đập 75 lần/phút, mỗi lần 70 mL thì bơm được $70\times75 = 5250$ mL $= 5{,}25$ lít máu mỗi phút.

## Khi vận động

Lúc chạy nhảy, cơ cần nhiều oxygen hơn nên nhịp tim tăng, lưu lượng tim tăng để đưa máu (mang $O_2$) tới cơ nhanh hơn. Đó là lí do tim đập nhanh khi tập thể dục.

## Phổi thông khí

Tương tự, mỗi nhịp thở đưa vào một **thể tích khí lưu thông** (khoảng 0,5 lít). Nhân với **nhịp thở** ra lượng khí trao đổi mỗi phút:

$$\text{thông khí phổi} = \text{thể tích khí lưu thông}\times \text{nhịp thở}$$

Hai công thức cùng một dạng "lượng mỗi lần × số lần mỗi phút", rất dễ nhớ.

**Lỗi thường gặp:**
- Nhầm thể tích tâm thu (mỗi lần đập) với lưu lượng tim (mỗi phút).
- Quên đổi mL sang lít khi đề hỏi lít/phút.
- Cộng thể tích và nhịp thay vì nhân chúng.

<sub>`lesson.biology.thcs-hoa-sinh.nhip-tim-luu-luong-va-ho-hap`</sub>

---

## Chủ đề: Trao đổi chất và chuyển hoá năng lượng ở thực vật

### 1. Quang hợp và hô hấp ở thực vật
*Photosynthesis and respiration in plants* · THCS · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Viết được phương trình tổng quát của quang hợp và của hô hấp ở thực vật
- So sánh được quang hợp và hô hấp về chất tham gia, sản phẩm và vai trò

## Hai quá trình ngược chiều

Cây xanh vừa "nấu ăn" vừa "tiêu thụ" thức ăn. Hai việc đó là quang hợp và hô hấp — gần như ngược nhau.

## Quang hợp: tạo chất và tích năng lượng

Diễn ra ở lục lạp trong lá, cần **ánh sáng** và **diệp lục**:

$$6CO_2 + 6H_2O \xrightarrow{\text{ánh sáng, diệp lục}} C_6H_{12}O_6 + 6O_2$$

Cây lấy khí carbon dioxide và nước, tạo ra glucose (thức ăn) và nhả khí oxygen. Quang hợp chỉ xảy ra khi có ánh sáng.

## Hô hấp: phân giải chất và giải phóng năng lượng

Diễn ra ở mọi tế bào sống, **suốt ngày đêm**:

$$C_6H_{12}O_6 + 6O_2 \rightarrow 6CO_2 + 6H_2O + \text{năng lượng}$$

Cây dùng oxygen "đốt" glucose để lấy năng lượng cho sinh trưởng.

## Ghi nhớ bằng cách so sánh

| | Quang hợp | Hô hấp |
|---|---|---|
| Lấy vào | $CO_2$, $H_2O$ | $O_2$, glucose |
| Thải ra | $O_2$, glucose | $CO_2$, $H_2O$ |
| Năng lượng | tích trữ | giải phóng |
| Khi nào | có ánh sáng | mọi lúc |

Hai quá trình bù trừ nhau, giữ cân bằng khí $O_2$ và $CO_2$ cho Trái Đất.

**Lỗi thường gặp:**
- Cho rằng cây chỉ hô hấp vào ban đêm; thực ra cây hô hấp cả ngày lẫn đêm, ban ngày quang hợp mạnh nên che lấp.
- Nhầm chất tham gia và sản phẩm giữa quang hợp và hô hấp vì hai phương trình gần như ngược nhau.
- Quên điều kiện ánh sáng và diệp lục của quang hợp.

<sub>`lesson.biology.thcs-hoa-sinh.quang-hop-va-ho-hap-o-thuc-vat`</sub>

---

## Chủ đề: Tế bào

### 1. Tế bào: tỉ lệ diện tích - thể tích và độ phóng đại kính hiển vi
*Cells: surface-to-volume ratio and microscope magnification* · THCS · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Giải thích được vì sao tế bào có kích thước rất nhỏ dựa vào tỉ lệ diện tích trên thể tích
- Tính được độ phóng đại của kính hiển vi và kích thước thật của vật quan sát

## Vì sao tế bào phải nhỏ

Tế bào trao đổi chất qua **bề mặt** nhưng nuôi toàn bộ **thể tích** bên trong. Khi vật to lên, thể tích tăng nhanh hơn diện tích, nên **tỉ lệ diện tích trên thể tích (S/V)** giảm. Tế bào nhỏ giữ tỉ lệ S/V lớn, giúp lấy chất dinh dưỡng và thải chất thải đủ nhanh. Đó là lí do tế bào có kích thước hiển vi.

## Nhìn tế bào bằng kính hiển vi

Mắt thường không thấy tế bào, phải dùng kính hiển vi. **Độ phóng đại** tổng cộng bằng tích của hai thấu kính:

$$G = G_{thị kính}\times G_{vật kính}$$

Ví dụ thị kính $10\times$ và vật kính $40\times$ cho ảnh lớn gấp $400$ lần.

## Kích thước thật của vật

Đo kích thước ảnh rồi chia cho độ phóng đại sẽ ra kích thước thật:

$$\text{kích thước thật} = \frac{\text{kích thước ảnh}}{G}$$

Nhớ đổi đơn vị cho khớp: $1$ mm $= 1000\ \mu m$. Đây là kĩ năng quan sát cốt lõi trong bài thực hành sinh học lớp 6.

**Lỗi thường gặp:**
- Cộng độ phóng đại của thị kính và vật kính thay vì nhân chúng.
- Quên đổi đơn vị mm sang µm nên kết quả sai 1000 lần.
- Cho rằng vật to thì trao đổi chất tốt hơn; thực ra vật to có tỉ lệ S/V nhỏ, trao đổi chất kém hơn.

<sub>`lesson.biology.thcs-hoa-sinh.te-bao-ti-le-svr-do-phong-dai`</sub>

---

## Chương 3: Di truyền học và Ứng dụng

### 5. Ứng dụng di truyền học: Ưu thế lai, Hệ số di truyền và Chọn giống
*Applied genetics: Heterosis, heritability, and selective breeding* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích cơ sở di truyền của hiện tượng ưu thế lai và phương pháp tạo dòng thuần
- Tính tỉ lệ giảm dị hợp tử qua các thế hệ tự thụ phấn hoặc giao phối cận huyết
- Vận dụng hệ số di truyền nghĩa rộng, nghĩa hẹp để dự đoán hiệu quả chọn lọc

## Sự biến đổi cấu trúc di truyền qua tự thụ phấn

Khi tự thụ phấn hoặc nội phối qua $n$ thế hệ, tỉ lệ dị hợp tử giảm đi một nửa sau mỗi thế hệ:

$$H_n = H_0 \left(\frac{1}{2}\right)^n$$

Điều này dẫn tới thoái hoá giống do các alen lặn có hại chuyển về trạng thái đồng hợp tử. Tuy nhiên tự thụ bắt buộc được dùng để tạo dòng thuần chủng phục vụ phép lai kinh tế tạo ưu thế lai.

## Hệ số di truyền và Hiệu quả chọn lọc

Phương sai kiểu hình tổng quát: $V_P = V_G + V_E = V_A + V_D + V_I + V_E$.

- Hệ số di truyền nghĩa rộng: $H^2 = \frac{V_G}{V_P}$
- Hệ số di truyền nghĩa hẹp: $h^2 = \frac{V_A}{V_P}$

Phương trình phản ứng chọn lọc (định luật chọn giống): $R = h^2 \cdot S$, trong đó $S$ là độ lệch chọn lọc và $R$ là đáp ứng chọn lọc.

**Lỗi thường gặp:**
- Nhầm lẫn giữa hệ số di truyền nghĩa rộng H^2 (toàn bộ phương sai gen) và nghĩa hẹp h^2 (chỉ tính phương sai cộng gộp)
- Dùng con lai F1 có ưu thế lai cao để làm giống cho thế hệ sau (sẽ bị phân tính làm giảm năng suất)

<sub>`lesson.biology.vn-thpt-biology.ung-dung-di-truyen-uu-the-lai-chon-giong`</sub>

---

## Chương: Biến dị

### 1. Đột biến gen
*Gene mutation* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được ba dạng đột biến điểm: mất, thêm và thay thế một cặp nucleotit
- Tính được sự thay đổi số nucleotit, chiều dài và số liên kết hiđro của gen sau đột biến
- Tính được tần số đột biến gen trong quần thể

## Một cặp nucleotit đổi chỗ, hệ quả tới đâu?

Đột biến gen là những thay đổi rất nhỏ ở mức phân tử, nhưng có thể làm hỏng cả một protein. Có ba dạng đột biến điểm cơ bản, mỗi dạng để lại 'dấu vết số học' riêng trên gen.

## Ba dạng và hệ quả định lượng

- **Mất một cặp nucleotit**: $N$ giảm 2, chiều dài giảm $3{,}4\ \text{Å}$; nếu mất cặp A-T thì $H$ giảm 2, mất cặp G-X thì $H$ giảm 3. Khung đọc bị lệch.
- **Thêm một cặp nucleotit**: $N$ tăng 2, chiều dài tăng $3{,}4\ \text{Å}$; $H$ tăng 2 hoặc 3 tuỳ loại cặp. Khung đọc bị lệch.
- **Thay thế một cặp nucleotit**: $N$ và chiều dài **không đổi**; chỉ $H$ có thể đổi $\pm 1$ (thay A-T bằng G-X: $H$ tăng 1; ngược lại giảm 1).

## Mất/thêm nguy hiểm hơn thay thế

Mất hoặc thêm một cặp gây **dịch khung**: mọi bộ ba từ điểm đột biến trở đi đều bị đọc sai, làm thay đổi hàng loạt axit amin. Thay thế thường chỉ ảnh hưởng một bộ ba (đột biến sai nghĩa, vô nghĩa hoặc đồng nghĩa). **Tần số đột biến gen** trong quần thể được tính bằng tỉ lệ giao tử mang alen đột biến mới trên tổng số giao tử.

**Lỗi thường gặp:**
- Cho rằng đột biến thay thế làm đổi chiều dài gen — sai, vì thay một cặp bằng một cặp khác giữ nguyên tổng số nucleotit, nên chiều dài và khối lượng gen không đổi, chỉ số liên kết hiđro có thể thay đổi.
- Nghĩ mất hay thêm 3 cặp nucleotit vẫn gây dịch khung — sai, vì mất/thêm một số cặp là bội của 3 chỉ làm mất/thêm nguyên các bộ ba, không làm lệch khung đọc phía sau.
- Tính $H$ giảm 2 khi mất một cặp G-X — sai, vì cặp G-X có 3 liên kết hiđro nên mất nó làm $H$ giảm 3, chỉ mất cặp A-T mới làm giảm 2.

<sub>`lesson.biology.vn-thpt-biology.dot-bien-gen`</sub>

---

### 2. Đột biến nhiễm sắc thể: lệch bội và đa bội
*Chromosomal mutations: aneuploidy and polyploidy* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được bộ nhiễm sắc thể của các thể lệch bội và số loại thể lệch bội có thể tạo ra
- Tính được tỉ lệ giao tử của thể tam bội và thể tứ bội
- Xác định được số kiểu gen tối đa và tỉ lệ kiểu hình đời con trong các phép lai đa bội

## Khi cả nhiễm sắc thể thay đổi số lượng

Khác với đột biến gen chỉ đụng đến vài nucleotit, đột biến nhiễm sắc thể làm thay đổi **cấu trúc** hoặc **số lượng** NST, kéo theo nhiều gen cùng lúc. Ta tập trung vào hai nhóm định lượng quan trọng: lệch bội và đa bội.

## Lệch bội

Một cặp NST không phân li tạo giao tử thừa hoặc thiếu, khi thụ tinh cho thể ba $(2n+1)$, thể một $(2n-1)$... Với loài có $n$ cặp NST, số loại thể ba (hoặc thể một) khác nhau bằng đúng số cặp NST, tức $n$ loại.

## Đa bội và giao tử

Thể đa bội mang bộ NST tăng theo bội của $n$. Điểm mấu chốt của bài tập là tỉ lệ giao tử. Thể **tứ bội AAaa** giảm phân bình thường cho giao tử lưỡng bội tỉ lệ:
$$1\,AA : 4\,Aa : 1\,aa$$
Dùng sơ đồ tổ hợp chập 2 của 4 alen $\{A,A,a,a\}$ để hiểu tỉ lệ này. Thể **tam bội AAa** cho giao tử theo tỉ lệ $1\,AA : 2\,Aa : 2\,A : 1\,a$ (gồm cả giao tử lưỡng bội và đơn bội). Từ tỉ lệ giao tử, ta suy ra tỉ lệ kiểu gen và kiểu hình đời con — ví dụ phép lai $AAaa \times AAaa$ cho tỉ lệ kiểu hình trội : lặn là $35 : 1$.

**Lỗi thường gặp:**
- Cho rằng thể tứ bội AAaa cho giao tử tỉ lệ $1:2:1$ như thể lưỡng bội Aa — sai, vì phải tổ hợp chập 2 của bốn alen nên tỉ lệ đúng là $1AA : 4Aa : 1aa$.
- Nhầm thể ba $(2n+1)$ với thể tam bội $(3n)$ — sai, vì thể ba chỉ thừa một NST ở một cặp, còn thể tam bội thừa nguyên một bộ $n$ ở tất cả các cặp.
- Tính số loại thể ba bằng $2^n$ — sai, vì mỗi thể ba chỉ khác nhau ở việc cặp NST nào bị thừa, nên số loại đúng bằng số cặp NST là $n$.

<sub>`lesson.biology.vn-thpt-biology.dot-bien-nhiem-sac-the`</sub>

---

## Chương: Chuyển hoá vật chất và năng lượng ở thực vật

### 1. Quang hợp ở thực vật: cường độ, năng suất và các điểm ánh sáng
*Photosynthesis in plants: rate, productivity and light points* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được cường độ quang hợp biểu kiến và cường độ quang hợp thực
- Xác định được điểm bù ánh sáng và điểm bão hoà ánh sáng dựa trên đồ thị quang hợp
- Tính được năng suất sinh học, năng suất kinh tế và hệ số kinh tế của cây trồng

## Đo quang hợp thực chất là đo gì?

Khi cắm một cành rong vào ống nghiệm rồi đếm bọt khí, ta không đo trực tiếp toàn bộ quang hợp: cây vẫn hô hấp và tiêu thụ một phần $O_2$. Do đó số ta quan sát là **quang hợp biểu kiến**, còn tổng lượng chất hữu cơ thực sự tổng hợp là **quang hợp thực**:
$$I_{thực} = I_{biểu\ kiến} + I_{hô\ hấp}$$

## Các điểm ánh sáng đặc trưng

Vẽ đồ thị cường độ quang hợp theo cường độ ánh sáng, ta thấy hai mốc quan trọng. Tại **điểm bù ánh sáng**, quang hợp vừa đủ bù hô hấp nên trao đổi khí biểu kiến bằng 0. Khi tăng sáng, quang hợp tăng rồi chững lại ở **điểm bão hoà ánh sáng** — lúc này $CO_2$ hoặc enzyme mới là yếu tố giới hạn.

## Năng suất cây trồng

Từ chất khô cây tích luỹ, ta định nghĩa:
$$N_{sinh\ học} = \dfrac{\text{khối lượng chất khô}}{\text{diện tích} \times \text{thời gian}}$$
Năng suất kinh tế chỉ tính phần chất khô ở cơ quan thu hoạch (hạt, củ). Hệ số kinh tế $K = \dfrac{N_{kinh\ tế}}{N_{sinh\ học}}$ cho biết cây phân bổ bao nhiêu phần trăm sản phẩm quang hợp vào bộ phận ta cần. Chọn giống có $K$ cao là một mục tiêu của chọn giống cây trồng.

**Lỗi thường gặp:**
- Đồng nhất quang hợp biểu kiến với quang hợp thực — sai, vì phép đo trao đổi khí luôn bị hô hấp làm giảm bớt, nên quang hợp thực bao giờ cũng lớn hơn biểu kiến một lượng đúng bằng cường độ hô hấp.
- Cho rằng cứ tăng ánh sáng thì quang hợp tăng mãi — sai, vì sau điểm bão hoà ánh sáng, $CO_2$ hoặc enzyme trở thành yếu tố giới hạn nên đồ thị nằm ngang.
- Nhầm năng suất kinh tế với năng suất sinh học — sai, vì năng suất sinh học là toàn bộ chất khô tích luỹ, còn năng suất kinh tế chỉ là phần ở cơ quan thu hoạch, luôn nhỏ hơn.

<sub>`lesson.biology.vn-thpt-biology.quang-hop-o-thuc-vat`</sub>

---

### 2. Hô hấp ở thực vật và hệ số hô hấp (RQ)
*Respiration in plants and the respiratory quotient (RQ)* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được hệ số hô hấp RQ từ tỉ lệ $CO_2$ thải ra và $O_2$ hấp thụ
- Suy luận được loại nguyên liệu hô hấp (carbohydrate, lipid, acid hữu cơ) dựa vào giá trị RQ
- Giải thích được ý nghĩa của số ATP thu được khi phân giải hoàn toàn một phân tử glucose

## Vì sao đo hai loại khí lại biết được cây 'ăn' gì?

Hô hấp là quá trình oxy hoá chất hữu cơ: cây lấy $O_2$ và thải $CO_2$. Nhưng tỉ lệ hai khí này không cố định — nó phụ thuộc mức độ giàu oxy của nguyên liệu bị đốt. Chính vì thế **hệ số hô hấp** trở thành một dấu vân tay hoá học:
$$RQ = \frac{\text{số mol } CO_2 \text{ thải ra}}{\text{số mol } O_2 \text{ hấp thụ}}$$

## Đọc giá trị RQ

- Glucose: $C_6H_{12}O_6 + 6O_2 \rightarrow 6CO_2 + 6H_2O$ nên $RQ = 6/6 = 1$.
- Lipid (ví dụ acid béo) nghèo oxy trong phân tử, cần nhiều $O_2$ để oxy hoá nên $RQ \approx 0{,}7$.
- Acid hữu cơ (như acid malic) đã giàu oxy sẵn nên thải nhiều $CO_2$ mà tốn ít $O_2$, $RQ > 1$.

Biết RQ, ta suy ngược ra loại cơ chất mà mô đang hô hấp — hạt nảy mầm giàu dầu thường có RQ thấp, còn hạt giàu tinh bột có RQ gần 1.

## Về mặt năng lượng

Phân giải hoàn toàn 1 phân tử glucose theo con đường hiếu khí giải phóng khoảng 30-38 ATP. Con số này giải thích vì sao hô hấp hiếu khí hiệu quả hơn lên men rất nhiều: lên men chỉ thu 2 ATP mỗi glucose.

**Lỗi thường gặp:**
- Cho rằng RQ luôn bằng 1 — sai, vì RQ chỉ bằng 1 khi cơ chất là carbohydrate; với lipid RQ khoảng 0,7 và với acid hữu cơ RQ lớn hơn 1 do sự khác nhau về hàm lượng oxy trong phân tử.
- Đảo ngược công thức thành $O_2/CO_2$ — sai, vì theo định nghĩa RQ là $CO_2$ thải chia cho $O_2$ hấp thụ; đảo tử số và mẫu số sẽ cho kết luận sai về loại nguyên liệu.
- Nghĩ lên men cũng cho nhiều ATP như hô hấp hiếu khí — sai, vì lên men chỉ tạo 2 ATP mỗi glucose do không có chuỗi truyền electron, kém xa con số 30-38 ATP của hô hấp hiếu khí.

<sub>`lesson.biology.vn-thpt-biology.ho-hap-o-thuc-vat-he-so-ho-hap`</sub>

---

## Chương: Cơ sở phân tử của hiện tượng di truyền

### 1. Cấu trúc ADN và các công thức đếm nucleotit
*DNA structure and nucleotide-counting formulas* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng nguyên tắc bổ sung để thiết lập quan hệ giữa các loại nucleotit trong gen
- Tính được tổng số nucleotit, chiều dài, khối lượng, số chu kì xoắn và số liên kết hiđro của gen
- Suy ra được số nucleotit từng loại khi biết phần trăm hoặc số liên kết hiđro

## Một chuỗi số học ẩn trong phân tử di truyền

ADN không chỉ mang thông tin sinh học mà còn tuân theo những ràng buộc số học chặt chẽ nhờ **nguyên tắc bổ sung**. Vì A luôn bắt cặp với T, G luôn bắt cặp với X, ta có ngay $A = T$ và $G = X$. Từ đó mọi công thức đếm được suy ra.

## Bộ công thức lõi

Gọi $N$ là tổng số nucleotit của gen (mạch kép):
$$N = 2A + 2G = 2(A + G)$$
Mỗi nucleotit dài $3{,}4\ \text{Å}$ và một mạch có $N/2$ nucleotit nên **chiều dài gen**:
$$L = \frac{N}{2} \times 3{,}4\ (\text{Å})$$
**Khối lượng** gen $M = N \times 300$ đvC; **số chu kì xoắn** $C = N/20$ (mỗi vòng xoắn 20 nucleotit); **số liên kết hiđro** $H = 2A + 3G$.

## Chiến lược giải nhanh

Đề thi thường cho hai trong các dữ kiện $\{N, L, M, C, H, \%A\}$ rồi bắt tìm số nucleotit từng loại. Mẹo: luôn quy về $N$ trước, dùng $A + G = N/2$ làm phương trình thứ nhất, rồi ghép với dữ kiện thứ hai (thường là $H = 2A + 3G$ hoặc $\%A$) để giải hệ hai ẩn $A, G$. Nhờ $A = T, G = X$, biết $A$ và $G$ là biết cả bốn loại.

**Lỗi thường gặp:**
- Nhầm chiều dài một mạch với chiều dài tính trên cả $N$ — sai, vì $N/2$ mới là số nucleotit trên một mạch, nên $L = (N/2)\times 3{,}4$; quên chia đôi sẽ làm $N$ gấp đôi.
- Cho rằng $\%A = \%G$ luôn bằng nhau — sai, vì nguyên tắc bổ sung chỉ bảo đảm $\%A = \%T$ và $\%G = \%X$; tỉ lệ giữa nhóm A-T và nhóm G-X thay đổi tuỳ gen.
- Tính số liên kết hiđro bằng $H = A + G$ — sai, vì mỗi cặp A-T có 2 liên kết và mỗi cặp G-X có 3 liên kết, nên đúng phải là $H = 2A + 3G$.

<sub>`lesson.biology.vn-thpt-biology.cau-truc-adn-va-cong-thuc-dem-nucleotit`</sub>

---

### 2. Nhân đôi ADN: nguyên liệu, đoạn mồi và đoạn Okazaki
*DNA replication: substrates, primers and Okazaki fragments* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được số phân tử ADN con và số nucleotit môi trường cung cấp sau k lần nhân đôi
- Vận dụng nguyên tắc bán bảo tồn để tính số ADN con chứa hoàn toàn nguyên liệu mới
- Tính được số đoạn mồi và số đoạn Okazaki trong quá trình nhân đôi

## Nhân đôi diễn ra theo kiểu nào?

ADN tự sao theo **nguyên tắc bán bảo tồn**: hai mạch mẹ tách ra, mỗi mạch làm khuôn tổng hợp một mạch mới bổ sung. Kết quả là mỗi ADN con có một mạch cũ và một mạch mới — chi tiết này chi phối toàn bộ các công thức đếm.

## Số phân tử và nguyên liệu

Sau $k$ lần nhân đôi từ 1 phân tử, ta được $2^k$ ADN con. Nhưng vì mỗi phân tử luôn mang một mạch của tổ tiên, chỉ có $2^k - 2$ phân tử được cấu tạo **hoàn toàn** từ nguyên liệu mới. Số nucleotit môi trường cung cấp:
$$N_{cc} = N\,(2^k - 1)$$
và số nucleotit từng loại: $A_{cc} = T_{cc} = A(2^k - 1)$, $G_{cc} = X_{cc} = G(2^k - 1)$. Số liên kết hiđro bị phá vỡ qua $k$ lần: $H(2^k - 1)$.

## Đoạn mồi và Okazaki

Vì ADN polymerase chỉ kéo dài theo chiều $5'\to 3'$, mạch chậm phải tổng hợp gián đoạn thành nhiều **đoạn Okazaki**, mỗi đoạn cần một đoạn mồi; mạch nhanh chỉ cần một mồi. Nếu một đơn vị tái bản có $x$ đoạn Okazaki thì cần $x + 1$ đoạn mồi. Nắm mối quan hệ mồi - Okazaki giúp giải nhanh các câu hỏi vận dụng cao về cơ chế tái bản.

**Lỗi thường gặp:**
- Tính số ADN con hoàn toàn mới bằng $2^k$ — sai, vì hai mạch của ADN mẹ luôn được giữ lại trong hai phân tử con nên chỉ có $2^k - 2$ phân tử hoàn toàn mới.
- Dùng $N_{cc} = N \cdot 2^k$ — sai, vì tổng nucleotit trong $2^k$ phân tử là $N\cdot 2^k$ nhưng mạch mẹ ban đầu đã có sẵn $N$, nên môi trường chỉ cung cấp $N(2^k - 1)$.
- Cho rằng mỗi mạch mới chỉ cần một đoạn mồi — sai, vì mạch chậm được tổng hợp gián đoạn nên mỗi đoạn Okazaki cần một mồi riêng, tổng số mồi lớn hơn nhiều so với 2.

<sub>`lesson.biology.vn-thpt-biology.nhan-doi-adn`</sub>

---

### 3. Phiên mã và dịch mã: số axit amin và số liên kết peptit
*Transcription and translation: amino acids and peptide bonds* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được số ribonucleotit môi trường cung cấp cho phiên mã
- Xác định được số bộ ba, số axit amin môi trường cung cấp và số axit amin của chuỗi polipeptit hoàn chỉnh
- Tính được số liên kết peptit và số phân tử nước giải phóng khi tổng hợp chuỗi polipeptit

## Từ gen đến protein: hai bước, nhiều con số

Thông tin trong gen được biểu hiện qua **phiên mã** (ADN $\to$ mARN) rồi **dịch mã** (mARN $\to$ chuỗi polipeptit). Mỗi bước có bộ công thức đếm riêng, nhưng tất cả đều bắt nguồn từ số nucleotit của gen.

## Phiên mã

mARN được tổng hợp bổ sung từ mạch gốc của gen, nên số ribonucleotit của mARN bằng số nucleotit một mạch: $r_N = N/2$. Số ribonucleotit môi trường cung cấp khi gen phiên mã $k$ lần là $k \cdot r_N$.

## Dịch mã

Số bộ ba trên mARN là $r_N/3$. Ribôxôm đọc từ bộ ba mở đầu đến bộ ba kết thúc:
- Số axit amin **môi trường cung cấp** $= \dfrac{r_N}{3} - 1$ (bỏ bộ ba kết thúc).
- Số axit amin của chuỗi **hoàn chỉnh** $= \dfrac{r_N}{3} - 2$ (bỏ thêm axit amin mở đầu bị cắt).

Khi nối $m$ axit amin thành chuỗi, mỗi liên kết peptit hình thành kèm một phân tử nước bị loại: có $m - 1$ liên kết peptit và $m - 1$ phân tử nước giải phóng. Nếu có $x$ ribôxôm trượt qua và $t$ phân tử mARN thì tổng số chuỗi polipeptit tạo ra là $x \cdot t$.

**Lỗi thường gặp:**
- Quên trừ bộ ba kết thúc khi tính số axit amin — sai, vì bộ ba kết thúc (UAA, UAG, UGA) không mã hoá axit amin nào, nên số axit amin cung cấp là $r_N/3 - 1$.
- Cho rằng chuỗi hoàn chỉnh vẫn giữ axit amin mở đầu — sai, vì ở tế bào axit amin mở đầu (Met hoặc formyl-Met) thường bị enzyme cắt bỏ, nên chuỗi hoàn chỉnh có $r_N/3 - 2$ axit amin.
- Tính số liên kết peptit bằng đúng số axit amin — sai, vì nối $m$ axit amin chỉ tạo $m - 1$ liên kết peptit, tương tự số phân tử nước giải phóng cũng là $m - 1$.

<sub>`lesson.biology.vn-thpt-biology.phien-ma-va-dich-ma`</sub>

---

## Chương: Di truyền học quần thể

### 1. Cấu trúc di truyền của quần thể tự thụ phấn và giao phối gần
*Genetic structure of self-pollinating and inbreeding populations* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được tần số alen từ tần số kiểu gen và từ số lượng cá thể
- Tính được tỉ lệ kiểu gen dị hợp và đồng hợp sau n thế hệ tự thụ phấn
- Giải thích được vì sao tự thụ phấn và giao phối gần làm nghèo vốn gen của quần thể

## Vì sao tự thụ phấn làm 'thuần' giống?

Quần thể tự thụ phấn hoặc giao phối gần có một đặc điểm rõ rệt: tỉ lệ dị hợp giảm dần, tỉ lệ đồng hợp tăng dần, dù **tần số alen không đổi**. Đây là cơ sở của việc tạo dòng thuần trong chọn giống.

## Tần số alen: điểm khởi đầu

Với gen hai alen, từ tần số kiểu gen $f(AA), f(Aa), f(aa)$:
$$p = f(AA) + \tfrac{1}{2}f(Aa), \qquad q = f(aa) + \tfrac{1}{2}f(Aa)$$
Mỗi cá thể dị hợp đóng góp một nửa alen A, một nửa alen a — đó là lí do hệ số $1/2$.

## Quy luật giảm dị hợp

Bắt đầu từ quần thể toàn $Aa$, sau $n$ thế hệ tự thụ:
$$Aa = \left(\frac{1}{2}\right)^{n}, \quad AA = aa = \frac{1 - (1/2)^{n}}{2}$$
Mỗi thế hệ, một nửa số dị hợp 'tách' thành đồng hợp. Vì tần số alen giữ nguyên, tự thụ chỉ **phân bố lại** kiểu gen chứ không tạo hay mất alen.

## Hệ quả sinh học

Giao phối gần làm tăng tỉ lệ đồng hợp lặn, bộc lộ các alen lặn có hại vốn ẩn ở thể dị hợp — đó là hiện tượng thoái hoá giống. Nhưng nó cũng là công cụ để tạo dòng thuần đồng nhất về di truyền phục vụ lai giống.

**Lỗi thường gặp:**
- Cho rằng tự thụ phấn làm thay đổi tần số alen — sai, vì tự thụ chỉ chuyển dị hợp thành đồng hợp, tổng số mỗi loại alen trong quần thể không đổi.
- Chia phần đồng hợp không đều khi quần thể ban đầu không cân đối — sai, vì $AA$ và $aa$ chỉ bằng nhau khi tỉ lệ hai đồng hợp ban đầu bằng nhau; nếu khác, phải cộng riêng phần đồng hợp phát sinh vào phần có sẵn.
- Tính tần số alen mà quên hệ số $1/2$ cho thể dị hợp — sai, vì mỗi cá thể $Aa$ chỉ đóng góp một nửa số alen là A, nên $p = f(AA) + \tfrac{1}{2}f(Aa)$.

<sub>`lesson.biology.vn-thpt-biology.cau-truc-di-truyen-quan-the-tu-thu-phan`</sub>

---

### 2. Định luật Hardy - Weinberg và điều kiện nghiệm đúng
*The Hardy-Weinberg law and its conditions* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu được định luật Hardy - Weinberg và nêu năm điều kiện nghiệm đúng
- Tính được tần số alen và tần số kiểu gen của quần thể cân bằng từ tỉ lệ kiểu hình lặn
- Kiểm tra được một quần thể có đang ở trạng thái cân bằng di truyền hay không

## Một điểm tựa để phát hiện tiến hoá

Định luật Hardy - Weinberg mô tả trạng thái quần thể **không tiến hoá**: nếu không có nhân tố nào tác động, tần số alen và kiểu gen giữ nguyên qua các thế hệ. Chính vì thế, khi quần thể **lệch** khỏi Hardy - Weinberg, ta biết có nhân tố tiến hoá đang hoạt động.

## Công thức và cách dùng

Với gen hai alen tần số $p(A)$ và $q(a)$, $p + q = 1$, quần thể cân bằng có:
$$p^{2}\,AA + 2pq\,Aa + q^{2}\,aa = 1$$
Dạng bài phổ biến nhất: biết tỉ lệ kiểu hình lặn $q^2$, lấy căn để có $q = \sqrt{q^2}$, rồi $p = 1 - q$; từ đó suy ra mọi tần số kiểu gen. Ví dụ bệnh lặn chiếm $q^2 = 0{,}04$ thì $q = 0{,}2$, $p = 0{,}8$, tần số người lành mang gen $2pq = 0{,}32$.

## Năm điều kiện nghiệm đúng

Quần thể phải: (1) kích thước lớn, (2) ngẫu phối, (3) không đột biến, (4) không di - nhập gen, (5) không chọn lọc. Vi phạm bất kì điều kiện nào đều có thể làm tần số alen thay đổi.

## Kiểm tra cân bằng

Một quần thể đang cân bằng nếu tần số kiểu gen thoả $(2pq)^2 = 4p^2 q^2$, tức $f(Aa)^2 = 4\,f(AA)\,f(aa)$. Đây là công cụ nhanh để xác nhận trạng thái cân bằng mà không cần theo dõi nhiều thế hệ.

**Lỗi thường gặp:**
- Lấy tần số alen lặn bằng tỉ lệ người bệnh $q^2$ thay vì $\sqrt{q^2}$ — sai, vì người bệnh là thể đồng hợp lặn ứng với $q^2$, muốn có tần số alen phải khai căn.
- Áp dụng Hardy - Weinberg cho quần thể tự thụ phấn hoặc giao phối gần — sai, vì định luật chỉ đúng với quần thể ngẫu phối; tự phối làm tăng đồng hợp nên tần số kiểu gen lệch khỏi $p^2 : 2pq : q^2$.
- Quên rằng người dị hợp cũng mang alen bệnh — sai, vì tần số alen lặn gồm cả phần trong thể dị hợp: $q = q^2 + \tfrac{1}{2}(2pq)$, nên đa số alen lặn nằm ở người lành mang gen.

<sub>`lesson.biology.vn-thpt-biology.dinh-luat-hardy-weinberg`</sub>

---

## Chương: Phân bào - Nguyên phân và Giảm phân

### 1. Nguyên phân: số tế bào con và nhiễm sắc thể môi trường cung cấp
*Mitosis: daughter cells and chromosomes supplied by the environment* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được số tế bào con tạo ra sau k lần nguyên phân từ a tế bào ban đầu
- Tính được số nhiễm sắc thể môi trường cung cấp cho quá trình nguyên phân
- Xác định được số NST và cromatit qua các kì của nguyên phân

## Đếm tế bào và vật chất di truyền

Nguyên phân giữ nguyên bộ NST: từ một tế bào $2n$ tạo ra hai tế bào con cũng $2n$. Nhờ tính chất nhân đôi này, mọi bài toán đếm đều quy về luỹ thừa của 2.

## Số tế bào con và số lần nguyên phân

Từ $a$ tế bào ban đầu, sau $k$ lần nguyên phân số tế bào con là
$$S = a \cdot 2^{k}$$

## Nhiễm sắc thể môi trường cung cấp

Mỗi lần phân bào đòi hỏi nhân đôi ADN, tức tổng hợp NST mới. Tổng số NST đơn môi trường cung cấp cho $a$ tế bào $2n$ qua $k$ lần:
$$\text{NST}_{cc} = 2n \cdot a \cdot (2^{k} - 1)$$
Dấu $(2^k - 1)$ xuất hiện vì tế bào mẹ ban đầu đã mang sẵn bộ NST, môi trường chỉ cấp phần tăng thêm.

## NST qua các kì

Theo dõi một tế bào: kì trung gian nhân đôi thành $2n$ NST kép ($4n$ cromatit); kì giữa các NST kép xếp một hàng ở mặt phẳng xích đạo; kì sau tách tâm động cho $4n$ NST đơn đi về hai cực; kì cuối mỗi tế bào con nhận $2n$ NST đơn. Nắm rõ số NST và cromatit từng kì là chìa khoá cho các câu hỏi lí thuyết định lượng.

**Lỗi thường gặp:**
- Tính NST môi trường cung cấp bằng $2n\cdot a\cdot 2^k$ — sai, vì bộ NST của các tế bào mẹ ban đầu đã tồn tại, môi trường chỉ cung cấp phần tăng thêm nên phải dùng $(2^k - 1)$.
- Cho rằng kì giữa nguyên phân có $4n$ NST — sai, vì kì giữa có $2n$ NST kép (mỗi NST gồm 2 cromatit), tổng cộng $4n$ cromatit chứ không phải $4n$ NST.
- Nhân số tế bào con bằng $a + 2^k$ — sai, vì mỗi tế bào ban đầu độc lập tạo $2^k$ tế bào con, nên tổng là tích $a\cdot 2^k$ chứ không phải tổng.

<sub>`lesson.biology.vn-thpt-biology.nguyen-phan`</sub>

---

### 2. Giảm phân và thụ tinh: số loại giao tử, trao đổi chéo, hiệu suất thụ tinh
*Meiosis and fertilization: gamete types, crossing over, fertilization efficiency* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được số loại giao tử tối đa của cơ thể có n cặp NST, kể cả khi có trao đổi chéo
- Tính được số giao tử tạo ra từ tế bào sinh tinh và tế bào sinh trứng
- Tính được hiệu suất thụ tinh của giao tử

## Vì sao đời con đa dạng đến vậy?

Giảm phân là nguồn gốc chính của biến dị tổ hợp. Mỗi cặp NST tương đồng phân li độc lập, nên số tổ hợp giao tử tăng theo luỹ thừa của 2.

## Số loại giao tử

Cơ thể dị hợp $n$ cặp gen nằm trên $n$ cặp NST khác nhau tạo tối đa
$$2^{n}\ \text{loại giao tử}$$
Nếu có **trao đổi chéo** đơn tại $k$ cặp NST, mỗi cặp đó cho thêm loại giao tử hoán vị, nâng số loại lên $2^{n+k}$. Số cách sắp xếp NST ở kì giữa giảm phân I cũng là $2^{n-1}$ cách khác nhau cho mỗi tế bào.

## Số giao tử và hiệu suất thụ tinh

Một tế bào sinh tinh giảm phân cho **4 tinh trùng**; một tế bào sinh trứng chỉ cho **1 trứng** (và 3 thể cực tiêu biến). **Hiệu suất thụ tinh**:
$$H = \frac{\text{số hợp tử}}{\text{số giao tử}}\times 100\%$$
Vì mỗi hợp tử cần 1 trứng và 1 tinh trùng, số hợp tử bằng số trứng (hoặc tinh trùng) được thụ tinh. Hiệu suất thụ tinh của trứng thường cao (gần 100%), còn của tinh trùng rất thấp do số lượng tinh trùng khổng lồ.

**Lỗi thường gặp:**
- Cho rằng tế bào sinh trứng cũng tạo 4 trứng như tế bào sinh tinh — sai, vì trong sinh trứng chỉ 1 trong 4 tế bào con phát triển thành trứng, 3 tế bào còn lại là thể cực tiêu biến.
- Tính số loại giao tử bằng $n^2$ hoặc $2n$ — sai, vì mỗi cặp NST dị hợp cho 2 khả năng và các cặp phân li độc lập nên số loại giao tử là $2^n$.
- Nhầm hiệu suất thụ tinh với tỉ lệ sống sót của hợp tử — sai, vì hiệu suất thụ tinh chỉ xét bước giao tử kết hợp thành hợp tử, chưa nói gì đến việc hợp tử phát triển tiếp.

<sub>`lesson.biology.vn-thpt-biology.giam-phan-va-thu-tinh`</sub>

---

## Chương: Quy luật di truyền

### 1. Quy luật phân li, phân li độc lập và công thức tổng quát n cặp gen
*Segregation, independent assortment and the general n-gene formulas* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng quy luật phân li và phân li độc lập của Mendel để dự đoán tỉ lệ đời con
- Áp dụng công thức tổng quát tính số loại giao tử, kiểu gen, kiểu hình khi lai n cặp gen dị hợp
- Sử dụng nhị thức Newton để tính xác suất xuất hiện một tổ hợp kiểu hình cụ thể

## Từ hạt đậu của Mendel đến công thức tổng quát

Mendel phát hiện mỗi cặp alen phân li về giao tử một cách độc lập. Khi lai nhiều cặp tính trạng, các cặp tổ hợp tự do — đó là **phân li độc lập**. Sức mạnh của quy luật này nằm ở chỗ ta có thể tổng quát hoá thành công thức cho $n$ cặp gen.

## Bộ công thức vàng cho phép lai n cặp dị hợp

Xét cơ thể dị hợp $n$ cặp gen $(AaBb\ldots)$, các gen phân li độc lập, trội hoàn toàn. Khi tự thụ $F_1 \times F_1$:

| Đại lượng | Công thức |
|---|---|
| Số loại giao tử mỗi bên | $2^n$ |
| Số kiểu tổ hợp giao tử | $4^n$ |
| Số loại kiểu gen | $3^n$ |
| Số loại kiểu hình | $2^n$ |
| Tỉ lệ phân li kiểu hình | $(3:1)^n$ |

Tỉ lệ kiểu hình mang toàn tính trạng lặn là $(1/4)^n$.

## Khi cần một tổ hợp cụ thể

Muốn tính xác suất, chẳng hạn, một cặp bố mẹ $AaBb \times AaBb$ sinh 3 con trong đó có đúng 2 con trội cả hai tính trạng, ta tách bài toán: xác suất mỗi con trội hai tính trạng là $9/16$, rồi áp **nhị thức Newton** $C_3^2 (9/16)^2(7/16)^1$. Cách tách 'tính xác suất một cá thể rồi nhân với tổ hợp' là công cụ mạnh cho mọi bài xác suất di truyền.

**Lỗi thường gặp:**
- Áp dụng công thức $(3:1)^n$ khi các gen không phân li độc lập — sai, vì công thức tổng quát chỉ đúng khi mỗi cặp gen nằm trên một cặp NST khác nhau; nếu liên kết gen thì tỉ lệ khác hẳn.
- Tính số kiểu gen bằng $2^n$ thay vì $3^n$ — sai, vì mỗi cặp gen dị hợp cho 3 loại kiểu gen (AA, Aa, aa) chứ không phải 2; $2^n$ là số loại kiểu hình.
- Cộng xác suất các cặp gen thay vì nhân — sai, vì các sự kiện di truyền độc lập nên xác suất đồng thời phải nhân, không phải cộng.

<sub>`lesson.biology.vn-thpt-biology.quy-luat-phan-li-va-phan-li-doc-lap`</sub>

---

### 2. Tương tác gen
*Gene interaction* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được tương tác bổ sung, tương tác át chế và tương tác cộng gộp
- Nhận ra các tỉ lệ biến dạng của tỉ lệ 9:3:3:1 (9:7, 9:6:1, 12:3:1, 13:3, 9:3:4, 15:1)
- Xác định được kiểu gen bố mẹ từ tỉ lệ kiểu hình đời con trong tương tác gen

## Khi nhiều gen cùng quyết định một tính trạng

Mendel giả định mỗi gen quy định một tính trạng riêng. Nhưng nhiều tính trạng thực tế do **nhiều gen không alen** cùng chi phối. Dấu hiệu nhận biết: phép lai hai cặp gen dị hợp cho tỉ lệ kiểu hình là **biến dạng** của $9:3:3:1$ (tổng vẫn bằng 16).

## Bảng nhận diện nhanh

| Kiểu tương tác | Tỉ lệ $F_2$ |
|---|---|
| Bổ sung (4 kiểu hình) | $9:3:3:1$ |
| Bổ sung (2 kiểu hình) | $9:7$ |
| Bổ sung (3 kiểu hình) | $9:6:1$ |
| Át chế trội | $12:3:1$ hoặc $13:3$ |
| Át chế lặn | $9:3:4$ |
| Cộng gộp | $15:1$ |

Mẹo: cộng các nhóm của $9:3:3:1$ để suy ra tỉ lệ mới. Ví dụ $9:7$ là gộp $(3+3+1)$ thành nhóm lặn; $12:3:1$ là gộp $(9+3)$ do gen trội át.

## Từ tỉ lệ suy ngược kiểu gen

Gặp tỉ lệ lạ như $9:6:1$ hay $13:3$, trước hết quy về tổng 16 để khẳng định có hai cặp gen phân li độc lập, rồi nhóm các tổ hợp $A\_B\_ : A\_bb : aaB\_ : aabb$ theo kiểu hình. **Tương tác cộng gộp** giải thích các tính trạng số lượng (chiều cao, màu da): càng nhiều alen trội, kiểu hình càng đậm, tạo dãy biến dị liên tục.

**Lỗi thường gặp:**
- Kết luận có nhiều cặp gen dựa vào tỉ lệ mà quên kiểm tra tổng bằng 16 — sai, vì các biến dạng của tương tác hai cặp gen luôn có tổng các phần bằng 16; nếu tổng khác thì phải xét số cặp gen khác.
- Nhầm tương tác át chế trội (12:3:1) với át chế lặn (9:3:4) — sai, vì át chế trội do alen trội che khuất nên nhóm trội gộp lại lớn (12), còn át chế lặn do kiểu gen đồng hợp lặn ở một gen gây ra kiểu hình thứ ba.
- Cho rằng tương tác gen vi phạm quy luật phân li độc lập — sai, vì các gen vẫn phân li độc lập bình thường; chỉ có cách chúng biểu hiện thành kiểu hình là phối hợp với nhau.

<sub>`lesson.biology.vn-thpt-biology.tuong-tac-gen`</sub>

---

### 3. Liên kết gen và hoán vị gen: tần số hoán vị và bản đồ gen
*Gene linkage and recombination: recombination frequency and gene mapping* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được liên kết gen hoàn toàn và hoán vị gen dựa trên tỉ lệ giao tử
- Tính được tần số hoán vị gen từ tỉ lệ giao tử hoán vị hoặc tỉ lệ kiểu hình đời con
- Lập được bản đồ di truyền từ tần số hoán vị giữa các cặp gen

## Khi các gen 'đi cùng nhau'

Nếu hai gen nằm trên cùng một NST, chúng có xu hướng di truyền cùng nhau — **liên kết gen**. Liên kết hoàn toàn chỉ cho 2 loại giao tử (giao tử liên kết), làm giảm biến dị tổ hợp so với phân li độc lập.

## Hoán vị gen và tần số

Ở giảm phân, trao đổi chéo giữa hai cromatit tạo **giao tử hoán vị**. Gọi $f$ là **tần số hoán vị**:
$$f = \frac{\text{số cá thể (giao tử) hoán vị}}{\text{tổng số}}\times 100\%$$
Hai loại giao tử hoán vị có tỉ lệ bằng nhau, mỗi loại $= f/2$; hai loại giao tử liên kết mỗi loại $= (1 - f)/2$. Vì trao đổi chéo chỉ xảy ra giữa hai trong bốn cromatit, $f$ **không bao giờ vượt 50%**; $f = 50\%$ tương đương phân li độc lập.

## Lập bản đồ gen

Tần số hoán vị tỉ lệ thuận với khoảng cách giữa hai gen: hai gen càng xa nhau càng dễ bị trao đổi chéo tách rời. Do đó $1\%$ hoán vị $= 1$ centimorgan (cM). Với ba gen A, B, C, ta đo $f$ từng cặp rồi cộng dồn để sắp thứ tự: nếu $f_{AB} = 20\%$, $f_{BC} = 10\%$, $f_{AC} = 30\%$ thì B nằm giữa và bản đồ là A—20—B—10—C. Đây là nguyên lí lập bản đồ di truyền cổ điển.

**Lỗi thường gặp:**
- Cho rằng tần số hoán vị có thể lớn hơn 50% — sai, vì trao đổi chéo chỉ xảy ra giữa hai trong bốn cromatit nên tối đa một nửa số giao tử là hoán vị; $f \le 50\%$.
- Chia tần số hoán vị cho hai loại giao tử liên kết thay vì hoán vị — sai, vì $f$ là tổng tỉ lệ giao tử hoán vị, nên mỗi giao tử hoán vị $= f/2$, còn giao tử liên kết chiếm phần lớn $(1-f)/2$.
- Xác định sai giao tử liên kết khi cơ thể ở thế dị hợp chéo (trans) $\dfrac{Ab}{aB}$ — sai, vì lúc đó giao tử liên kết là $Ab, aB$ còn giao tử hoán vị mới là $AB, ab$, ngược với thế dị hợp đều.

<sub>`lesson.biology.vn-thpt-biology.lien-ket-gen-va-hoan-vi-gen`</sub>

---

### 4. Di truyền liên kết giới tính và di truyền ngoài nhân
*Sex-linked inheritance and extranuclear inheritance* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được đặc điểm di truyền của gen nằm trên vùng không tương đồng của NST X
- Phân biệt được di truyền liên kết với X, liên kết với Y và di truyền ngoài nhân
- Vận dụng nhị thức Newton để tính xác suất về giới tính của con

## Vì sao bệnh mù màu gặp ở nam nhiều hơn nữ?

Một số gen nằm trên NST giới tính, khiến quy luật di truyền phụ thuộc giới. Với gen lặn trên **vùng không tương đồng của X**, nam chỉ có một X nên chỉ cần một alen lặn $X^a Y$ đã biểu hiện bệnh; nữ cần cả hai $X^a X^a$ mới mắc. Đó là lí do bệnh mù màu, máu khó đông phổ biến ở nam.

## Ba kiểu di truyền đặc biệt

- **Liên kết X**: di truyền **chéo** — mẹ truyền cho con trai, bố truyền cho con gái. Con trai nhận X từ mẹ nên kiểu hình con trai phản ánh kiểu gen mẹ.
- **Liên kết Y**: di truyền **thẳng** — chỉ bố truyền cho tất cả con trai, con gái không bao giờ mang.
- **Di truyền ngoài nhân**: gen ở ti thể/lục lạp, con nhận tế bào chất từ mẹ nên di truyền **theo dòng mẹ**; phép lai thuận nghịch cho kết quả khác nhau, đời con luôn giống mẹ.

## Xác suất về giới tính

Vì mỗi lần sinh xác suất con trai và con gái đều $1/2$ và độc lập nhau, ta dùng **nhị thức Newton** để tính, ví dụ, xác suất một gia đình 4 con có đúng 2 trai: $C_4^2 (1/2)^2 (1/2)^2 = 6/16 = 3/8$. Kết hợp quy luật liên kết giới tính với xác suất giới tính là dạng câu hỏi vận dụng cao thường gặp.

**Lỗi thường gặp:**
- Cho rằng gen lặn liên kết X biểu hiện như nhau ở hai giới — sai, vì nam chỉ có một X nên chỉ cần một alen lặn đã biểu hiện, còn nữ phải đồng hợp lặn, khiến tần số bệnh ở nam cao hơn.
- Nhầm di truyền ngoài nhân với di truyền liên kết X — sai, vì di truyền ngoài nhân do gen ti thể/lục lạp, con luôn giống mẹ bất kể giới tính; còn liên kết X vẫn tuân theo phân li của NST giới tính.
- Quên nhân hệ số $1/2$ giới tính khi tính tỉ lệ 'con trai bị bệnh trên tổng số con' — sai, vì tỉ lệ trong nhóm con trai khác với tỉ lệ trên toàn bộ con, phải nhân thêm xác suất là con trai.

<sub>`lesson.biology.vn-thpt-biology.di-truyen-lien-ket-gioi-tinh`</sub>

---

### 5. Số kiểu gen tối đa trong quần thể
*Maximum number of genotypes in a population* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · chuyen-sau

**Mục tiêu:**
- Tính được số kiểu gen tối đa của một gen có r alen trên NST thường
- Tính được số kiểu gen tối đa khi nhiều gen cùng nằm trên một cặp NST hoặc trên NST giới tính
- Kết hợp các trường hợp để tính số kiểu gen và số kiểu giao phối tối đa của quần thể

## Bài toán tổ hợp ẩn trong di truyền

Số kiểu gen tối đa của quần thể là một bài toán đếm tổ hợp thuần tuý, nhưng phải xử lí đúng vị trí của gen: trên NST thường, cùng một NST, hay trên NST giới tính.

## Công thức nền tảng

Một gen có $r$ alen trên NST thường: mỗi kiểu gen là một cặp không thứ tự chọn từ $r$ alen (cho phép lặp), nên số kiểu gen $= \dfrac{r(r+1)}{2}$. Trong đó $r$ kiểu đồng hợp và $\dfrac{r(r-1)}{2}$ kiểu dị hợp.

## Các trường hợp mở rộng

- **Nhiều gen trên nhiều cặp NST khác nhau**: tính số kiểu gen mỗi gen rồi **nhân** lại.
- **Nhiều gen trên cùng một cặp NST**: mỗi NST mang một tổ hợp alen, coi tổ hợp đó như một 'alen lớn'. Nếu có $m$ loại NST thì số kiểu gen $= \dfrac{m(m+1)}{2}$.
- **Gen trên vùng không tương đồng của X**: giới XX có $\dfrac{r(r+1)}{2}$ kiểu, giới XY có $r$ kiểu; cộng lại.

Cuối cùng, **số kiểu giao phối tối đa** trong quần thể là số cách ghép hai kiểu gen (có phân biệt đực - cái nếu cần). Chiến lược chung: xác định vị trí gen $\to$ đếm từng phần $\to$ nhân các phần độc lập, cộng các giới. Nhầm giữa 'nhân' và 'cộng' là lỗi phổ biến nhất.

**Lỗi thường gặp:**
- Nhân số alen thay vì dùng công thức tổ hợp — sai, vì số kiểu gen của một gen $r$ alen là $\dfrac{r(r+1)}{2}$ (kể cả đồng hợp và dị hợp), không phải $r$ hay $r^2$.
- Cộng số kiểu gen của các gen trên các cặp NST khác nhau — sai, vì các gen độc lập nên số kiểu gen tổ hợp phải nhân với nhau, không phải cộng.
- Áp dụng công thức gen trên NST thường cho gen trên X — sai, vì ở NST giới tính phải tính riêng giới XX (dạng $\dfrac{r(r+1)}{2}$) và giới XY (dạng $r$) rồi cộng lại.

<sub>`lesson.biology.vn-thpt-biology.so-kieu-gen-toi-da-trong-quan-the`</sub>

---

## Chương: Sinh học tế bào - Vận chuyển các chất qua màng

### 1. Thế nước và sự trao đổi nước ở tế bào thực vật
*Water potential and water exchange in plant cells* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được bản chất của thế nước và vì sao nước luôn di chuyển từ nơi thế nước cao đến nơi thế nước thấp
- Tính được thế nước của tế bào từ thế thẩm thấu và thế áp suất
- Dự đoán được chiều di chuyển của nước khi đặt tế bào vào môi trường ưu trương, nhược trương hoặc đẳng trương

## Vì sao cần một đại lượng gọi là "thế nước"?

Khi ngâm một lát khoai tây vào nước cất, nó cứng lên; ngâm vào dung dịch muối đậm, nó mềm đi. Để nói chính xác nước sẽ đi theo hướng nào, ta cần một thước đo chung cho "khả năng dịch chuyển" của nước: đó là **thế nước** $\Psi$.

## Xây dựng công thức

Thế nước của một tế bào là tổng của hai thành phần:
$$\Psi = \Psi_s + \Psi_p$$
trong đó $\Psi_s$ (thế thẩm thấu, luôn âm) phản ánh lượng chất tan, còn $\Psi_p$ (thế áp suất, thường dương) phản ánh sức căng của thành tế bào. Thế thẩm thấu của một dung dịch tính theo áp suất thẩm thấu Van't Hoff:
$$\Psi_s = -\pi = -iCRT$$
với $i$ là hệ số Van't Hoff, $C$ nồng độ mol, $R = 0{,}082$ L·atm/(mol·K), $T$ nhiệt độ tuyệt đối.

## Khi nào dùng?

- So sánh $\Psi$ tế bào với $\Psi$ môi trường để suy ra chiều di chuyển của nước: nước đi về phía $\Psi$ thấp hơn.
- Trong môi trường **nhược trương** ($\Psi_{mt} > \Psi_{tb}$) tế bào hút nước, trương lên; **ưu trương** thì mất nước, co nguyên sinh; **đẳng trương** thì cân bằng.

Sức hút nước của tế bào $S = \pi - T$ chính là cách viết cũ của $-\Psi$: khi thành tế bào chưa căng ($T=0$) thì sức hút nước bằng đúng áp suất thẩm thấu.

**Lỗi thường gặp:**
- Nghĩ rằng dung dịch đặc hơn thì thế nước cao hơn — sai, vì thêm chất tan làm $\Psi_s$ âm hơn nên thế nước giảm; dung dịch càng đặc thì $\Psi$ càng thấp và càng hút nước.
- Chỉ so sánh nồng độ chất tan mà bỏ qua thế áp suất — sai, vì ở tế bào trương nước thành tế bào tạo $\Psi_p > 0$ có thể đẩy thế nước tế bào lên cao hơn cả môi trường, khiến nước ngừng vào dù trong tế bào vẫn đặc hơn.
- Quên đổi nhiệt độ ra Kelvin khi dùng $\pi = iCRT$ — sai, vì công thức Van't Hoff đòi hỏi nhiệt độ tuyệt đối $T = t + 273$, dùng độ C sẽ cho áp suất thẩm thấu sai lệch lớn.

<sub>`lesson.biology.vn-thpt-biology.the-nuoc-trao-doi-nuoc-o-te-bao`</sub>

---

## Chương: Sinh học vi sinh vật

### 1. Sinh trưởng của quần thể vi sinh vật
*Growth of microbial populations* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được số tế bào của quần thể vi khuẩn sau n lần phân chia
- Xác định được số lần phân chia và thời gian thế hệ từ số tế bào ban đầu và số tế bào cuối
- Mô tả được bốn pha của đường cong sinh trưởng trong nuôi cấy không liên tục

## Từ một tế bào đến hàng tỉ

Vi khuẩn sinh sản bằng phân đôi: mỗi lần một tế bào thành hai. Nếu ban đầu có $N_0$ tế bào và trải qua $n$ lần phân chia thì số tế bào là
$$N_t = N_0 \cdot 2^{n}$$
Đây là biểu thức luỹ thừa cơ số 2, giải thích vì sao vi khuẩn có thể sinh khối bùng nổ trong thời gian ngắn.

## Thời gian thế hệ

Nếu trong thời gian $t$ có $n$ lần phân chia thì **thời gian thế hệ** là
$$g = \frac{t}{n}$$
Muốn tìm $n$ khi biết $N_0$ và $N_t$, ta lấy logarit: $n = \log_2(N_t/N_0)$. Thời gian thế hệ càng ngắn thì vi sinh vật sinh trưởng càng nhanh — E. coli có $g \approx 20$ phút trong điều kiện tối ưu.

## Đường cong sinh trưởng

Trong **nuôi cấy không liên tục**, quần thể đi qua bốn pha: pha tiềm phát (làm quen, tổng hợp enzyme), pha luỹ thừa (phân chia mạnh nhất, tuân theo $N_t = N_0 2^n$), pha cân bằng (số sinh ra bằng số chết đi do cạn dinh dưỡng và tích luỹ chất độc) và pha suy vong (số chết vượt số sinh). Hiểu bốn pha này giúp chọn đúng thời điểm thu sinh khối hoặc sản phẩm trao đổi chất.

**Lỗi thường gặp:**
- Dùng công thức $N_t = N_0 \cdot n$ thay vì $N_0 \cdot 2^n$ — sai, vì mỗi lần phân chia làm số tế bào nhân đôi chứ không cộng thêm, nên phải dùng luỹ thừa cơ số 2.
- Cho rằng vi khuẩn sinh trưởng luỹ thừa mãi mãi — sai, vì trong nuôi cấy không liên tục dinh dưỡng cạn dần và chất độc tích luỹ, đưa quần thể sang pha cân bằng rồi suy vong.
- Nhầm thời gian thế hệ với tổng thời gian nuôi cấy — sai, vì thời gian thế hệ chỉ là thời gian cho một lần nhân đôi, bằng tổng thời gian chia cho số lần phân chia.

<sub>`lesson.biology.vn-thpt-biology.sinh-truong-cua-quan-the-vi-sinh-vat`</sub>

---

## Chương: Sinh lí người và động vật

### 1. Sinh lí người: tuần hoàn, hô hấp và bài tiết
*Human physiology: circulation, respiration and excretion* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được lưu lượng tim, huyết áp trung bình và vận tốc máu trong hệ mạch
- Tính được độ lọc cầu thận và áp suất lọc hữu hiệu ở cầu thận
- Tính được chỉ số khối cơ thể BMI và đánh giá tình trạng cơ thể

## Cơ thể là một hệ định lượng

Sinh lí người không chỉ là mô tả: nhiều chức năng có thể đo và tính bằng công thức. Ba hệ tiêu biểu là tuần hoàn, bài tiết và các chỉ số cơ thể.

## Tuần hoàn

**Lưu lượng tim** (cardiac output) là thể tích máu tim bơm mỗi phút:
$$Q = f_{tim} \times V_{tâm\ thu}$$
ví dụ nhịp 75 lần/phút, mỗi lần bơm 70 ml thì $Q = 75\times 70 = 5250$ ml/phút $\approx 5{,}25$ L/phút. **Huyết áp trung bình** xấp xỉ $P_{tb} = P_{tâm\ trương} + \dfrac{1}{3}(P_{tâm\ thu} - P_{tâm\ trương})$. **Vận tốc máu** tỉ lệ nghịch với tổng tiết diện mạch, nên chậm nhất ở mao mạch — thuận lợi cho trao đổi chất.

## Bài tiết

Ở cầu thận, **áp suất lọc hữu hiệu** là hiệu giữa áp suất máu đẩy và tổng của áp suất keo huyết tương cùng áp suất trong nang Bowman; chính nó quyết định **độ lọc cầu thận** (GFR). GFR giảm khi huyết áp tụt là cơ chế bảo vệ nhưng cũng là dấu hiệu suy thận.

## Chỉ số cơ thể

**BMI** $= \dfrac{m}{h^2}$ dùng phân loại thể trạng: dưới 18,5 là gầy, 18,5-22,9 bình thường (chuẩn châu Á), từ 23 trở lên là thừa cân. Các con số này giúp chuyển kiến thức sinh lí thành công cụ theo dõi sức khoẻ thực tế.

**Lỗi thường gặp:**
- Cho rằng vận tốc máu nhanh nhất ở mao mạch vì mạch nhỏ — sai, vì vận tốc tỉ lệ nghịch với tổng tiết diện; mao mạch tuy nhỏ nhưng tổng tiết diện rất lớn nên máu chảy chậm nhất, thuận lợi trao đổi chất.
- Tính BMI với chiều cao bằng centimet — sai, vì công thức $BMI = m/h^2$ yêu cầu chiều cao tính bằng mét; dùng cm sẽ cho giá trị nhỏ hơn hàng chục nghìn lần.
- Nhầm áp suất lọc hữu hiệu bằng chính huyết áp — sai, vì áp suất lọc là huyết áp trong cầu thận trừ đi áp suất keo huyết tương và áp suất trong nang Bowman, nên nhỏ hơn huyết áp nhiều.

<sub>`lesson.biology.vn-thpt-biology.sinh-li-nguoi-tuan-hoan-ho-hap-bai-tiet`</sub>

---

## Chương: Sinh thái học

### 1. Sinh thái quần thể: kích thước và tăng trưởng
*Population ecology: size and growth* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được kích thước quần thể tại một thời điểm từ các yếu tố sinh, tử, xuất, nhập cư
- Phân biệt được tăng trưởng theo tiềm năng sinh học (chữ J) và tăng trưởng thực tế (chữ S)
- Ước lượng được kích thước quần thể bằng phương pháp bắt - đánh dấu - thả - bắt lại

## Quần thể lớn lên như thế nào?

Kích thước quần thể không cố định mà thay đổi theo bốn dòng: sinh, tử, nhập cư, xuất cư:
$$N_t = N_0 + B - D + I - E$$
Hiểu bốn yếu tố này giúp lí giải mọi biến động số lượng.

## Hai kiểu tăng trưởng

- **Theo tiềm năng sinh học** (chữ J): khi nguồn sống dồi dào, quần thể tăng theo hàm mũ $N_t = N_0 e^{rt}$ với $r$ là tốc độ tăng riêng tức thời. Đường cong dựng đứng, không giới hạn — chỉ đúng trong thời gian ngắn.
- **Thực tế** (chữ S, logistic): môi trường có **sức chứa** $K$; khi $N$ tăng, cạnh tranh làm tốc độ tăng chậm lại: $\dfrac{dN}{dt} = rN\dfrac{K - N}{K}$. Khi $N \to K$, tăng trưởng dừng.

## Ước lượng kích thước quần thể

Với động vật di chuyển, ta dùng phương pháp **bắt - đánh dấu - thả - bắt lại** (Lincoln - Petersen): bắt $M$ cá thể đánh dấu rồi thả; lần sau bắt $C$ cá thể thấy $R$ con có dấu. Vì tỉ lệ đánh dấu trong mẫu phản ánh tỉ lệ trong quần thể:
$$N \approx \frac{M \times C}{R}$$
Đây là công cụ cơ bản của sinh thái học thực địa. **Thời gian quần thể tăng gấp đôi** trong pha mũ là $t_2 = \dfrac{\ln 2}{r}$.

**Lỗi thường gặp:**
- Cho rằng tăng trưởng theo tiềm năng sinh học kéo dài mãi — sai, vì môi trường luôn có sức chứa $K$ giới hạn, nên trong thực tế đường cong chuyển sang dạng chữ S khi nguồn sống cạn dần.
- Bỏ qua nhập cư và xuất cư khi tính biến động số lượng — sai, vì kích thước quần thể phụ thuộc cả bốn yếu tố sinh, tử, nhập, xuất; chỉ tính sinh và tử sẽ sai với quần thể mở.
- Đảo công thức bắt - thả thành $N = R\times C / M$ — sai, vì số cá đánh dấu ban đầu $M$ phải ở tử số; đặt sai vị trí sẽ cho kết quả vô lí nhỏ hơn cả mẫu.

<sub>`lesson.biology.vn-thpt-biology.sinh-thai-quan-the-va-tang-truong`</sub>

---

### 2. Dòng năng lượng, chuỗi thức ăn và hiệu suất sinh thái
*Energy flow, food chains and ecological efficiency* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được bậc dinh dưỡng của các sinh vật trong chuỗi và lưới thức ăn
- Tính được hiệu suất sinh thái giữa hai bậc dinh dưỡng
- Tính được năng lượng còn lại sau n bậc dinh dưỡng từ hiệu suất chuyển hoá

## Vì sao chuỗi thức ăn không dài vô hạn?

Năng lượng đi qua hệ sinh thái theo **dòng một chiều**: từ ánh sáng $\to$ sinh vật sản xuất $\to$ các bậc tiêu thụ. Nhưng mỗi lần chuyển bậc, phần lớn năng lượng bị mất qua hô hấp, bài tiết và nhiệt. Đó là lí do chuỗi thức ăn hiếm khi quá 4-5 bậc.

## Hiệu suất sinh thái

Giữa hai bậc dinh dưỡng liên tiếp:
$$eff = \frac{\text{năng lượng ở bậc sau}}{\text{năng lượng ở bậc trước}}\times 100\%$$
Quy tắc gần đúng 10% (Lindeman) nói rằng chỉ khoảng 10% năng lượng được truyền lên bậc kế tiếp.

## Năng lượng còn lại sau nhiều bậc

Nếu năng lượng bậc 1 là $E_0$ và hiệu suất mỗi bậc là $h$ (dạng thập phân), thì sau $n$ bậc:
$$E_n = E_0 \cdot h^{n}$$
Vì $h$ nhỏ (khoảng 0,1), năng lượng suy giảm rất nhanh theo bậc — giải thích vì sao sinh khối động vật ăn thịt đầu bảng luôn ít.

## Chuỗi và lưới thức ăn

Một **chuỗi thức ăn** là dãy tuyến tính các bậc dinh dưỡng; nhiều chuỗi đan xen tạo thành **lưới thức ăn**. Xác định đúng bậc dinh dưỡng của mỗi loài (một loài có thể ở nhiều bậc trong lưới) là bước đầu để tính toán dòng năng lượng.

**Lỗi thường gặp:**
- Đếm sai số lần chuyển bậc giữa sinh vật sản xuất và bậc cần tính — sai, vì tiêu thụ bậc 3 là bậc dinh dưỡng cấp 4, đã qua 3 lần chuyển, nên số mũ là 3 chứ không phải 4.
- Cộng hiệu suất qua các bậc thay vì nhân — sai, vì năng lượng ở mỗi bậc bằng năng lượng bậc trước nhân hiệu suất, nên qua $n$ bậc phải nhân luỹ thừa $h^n$, không phải cộng.
- Cho rằng năng lượng được tái sử dụng như vật chất — sai, vì dòng năng lượng đi một chiều và mất dần qua hô hấp, khác với chu trình vật chất được tuần hoàn.

<sub>`lesson.biology.vn-thpt-biology.dong-nang-luong-va-hieu-suat-sinh-thai`</sub>

---

## Chương: Tiến hoá

### 1. Các nhân tố tiến hoá làm thay đổi tần số alen
*Evolutionary factors changing allele frequencies* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · chuyen-sau

**Mục tiêu:**
- Tính được sự thay đổi tần số alen do chọn lọc tự nhiên qua các thế hệ
- Tính được thay đổi tần số alen do đột biến và do di - nhập gen
- Giải thích được tác động của các yếu tố ngẫu nhiên đến vốn gen của quần thể nhỏ

## Điều gì phá vỡ trạng thái Hardy - Weinberg?

Hardy - Weinberg mô tả quần thể đứng yên. Tiến hoá xảy ra khi một trong các **nhân tố tiến hoá** làm tần số alen thay đổi. Ta định lượng ba nhân tố quan trọng nhất.

## Chọn lọc tự nhiên

Mỗi kiểu gen có **độ thích nghi tương đối** $w$; **hệ số chọn lọc** $s = 1 - w$. Với alen lặn a bị chọn lọc hoàn toàn ($s = 1$, thể $aa$ không sinh sản), tần số alen lặn sau $n$ thế hệ:
$$q_n = \frac{q_0}{1 + n\,q_0}$$
Công thức này cho thấy chọn lọc chống alen lặn ngày càng chậm khi $q$ nhỏ, vì alen lặn ẩn trong thể dị hợp.

## Đột biến và di - nhập gen

Đột biến làm thay đổi tần số alen rất chậm theo tốc độ đột biến. **Di - nhập gen** thay đổi nhanh hơn: sau một thế hệ nhập cư tỉ lệ $m$ từ nhóm có tần số $q_m$,
$$q' = (1 - m)q + m\,q_m$$

## Yếu tố ngẫu nhiên

Ở quần thể nhỏ, **phiêu bạt di truyền** làm tần số alen dao động ngẫu nhiên, có thể cố định hoặc loại bỏ alen bất kể giá trị thích nghi. Kích thước quần thể hiệu dụng càng nhỏ, phiêu bạt càng mạnh — đó là lí do các quần thể nhỏ dễ mất đa dạng di truyền.

**Lỗi thường gặp:**
- Cho rằng chọn lọc loại hết alen lặn ngay sau một thế hệ — sai, vì alen lặn còn ẩn trong thể dị hợp $Aa$ không bị chọn lọc, nên chỉ giảm dần chứ không mất ngay.
- Nhầm di - nhập gen với đột biến về tốc độ thay đổi — sai, vì đột biến làm thay đổi tần số alen cực chậm (theo tốc độ đột biến rất nhỏ), còn di - nhập gen có thể đổi tần số nhanh trong một thế hệ.
- Cho rằng phiêu bạt di truyền luôn giữ lại alen có lợi — sai, vì yếu tố ngẫu nhiên tác động không định hướng, ở quần thể nhỏ có thể cố định cả alen có hại và loại bỏ alen có lợi.

<sub>`lesson.biology.vn-thpt-biology.cac-nhan-to-tien-hoa-lam-thay-doi-tan-so-alen`</sub>

---

## Unit 10: Sinh lí người (IB/A-Level Human Physiology)

### 1. Hệ tuần hoàn: chu kì tim, huyết áp và vận tốc máu
*The circulatory system: cardiac cycle, blood pressure and blood velocity* · THPT (lớp 10-12) · ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Mô tả được ba pha của chu kì tim và cơ chế đóng mở van theo chênh lệch áp suất
- Giải thích được vì sao vận tốc máu chậm nhất ở mao mạch dù mỗi mao mạch rất hẹp
- Vận dụng được công thức lưu lượng tim và huyết áp trung bình để phân tích số liệu

## Vì sao người cần tuần hoàn kép

Khuếch tán đủ nhanh trên vài chục micromet nhưng vô vọng trên hàng mét (thời gian tỉ lệ với bình phương quãng đường). Cơ thể lớn buộc phải có hệ vận chuyển đối lưu. Tuần hoàn **kép** cho phép giữ áp suất thấp ở vòng phổi (tránh làm vỡ màng trao đổi mỏng manh của phế nang) trong khi vẫn duy trì áp suất cao ở vòng hệ thống.

## Chu kì tim: van mở đóng theo áp suất

Nguyên tắc bao trùm: **van mở khi áp suất phía trước thấp hơn phía sau, đóng khi ngược lại**. Không có cơ nào 'điều khiển' van cả.

1. **Tâm nhĩ thu** (~0,1 s): áp suất nhĩ vượt áp suất thất, van nhĩ thất mở, đẩy nốt khoảng 20-30% máu vào thất.
2. **Tâm thất thu** (~0,3 s): thất co, áp suất vượt nhĩ → van nhĩ thất **đóng** (tiếng tim thứ nhất); khi vượt áp suất động mạch chủ → van bán nguyệt mở, máu phóng ra.
3. **Pha giãn chung** (~0,4 s): thất giãn, áp suất tụt dưới động mạch → van bán nguyệt đóng (tiếng tim thứ hai); máu từ tĩnh mạch đổ về đầy nhĩ và thất.

Tổng khoảng 0,8 s, tương ứng 75 nhịp/phút.

## Vận tốc máu và tổng tiết diện

Quan hệ then chốt: $v = \dfrac{Q}{A_{\text{tổng}}}$ với $Q$ là lưu lượng không đổi qua mọi tầng mạch. Động mạch chủ có tiết diện khoảng $3\ \text{cm}^2$ nên $v \approx 30$ cm/s. Mao mạch tuy mỗi cái chỉ rộng vài micromet nhưng có hàng tỉ cái, **tổng** tiết diện đạt khoảng $2500\ \text{cm}^2$ nên $v$ tụt xuống khoảng 0,03 cm/s — chậm hơn ở động mạch chủ chừng một nghìn lần.

Đây không phải sự cố mà là thích nghi: máu chảy chậm ở mao mạch cho đủ thời gian trao đổi chất, đúng ở nơi cần trao đổi nhất.

## Điều hoà

Thụ thể áp lực ở xoang cảnh và cung động mạch chủ báo về hành não. Huyết áp tăng → tăng tín hiệu phó giao cảm qua dây X → giảm nhịp tim và giãn mạch → huyết áp trở về bình thường. Đây là một vòng phản hồi âm điển hình.

**Lỗi thường gặp:**
- Nói van tim 'được cơ điều khiển đóng mở' — sai, van tim hoàn toàn thụ động và chỉ đáp ứng chênh lệch áp suất hai bên; hiểu sai điều này làm không giải thích được thứ tự hai tiếng tim.
- Kết luận máu chảy chậm ở mao mạch 'vì mao mạch hẹp nên cản trở lớn' — sai về mặt lập luận, nguyên nhân là **tổng** tiết diện của toàn bộ mao mạch lớn hơn động mạch chủ hàng nghìn lần, mà $v = Q/A$.
- Tính huyết áp trung bình bằng trung bình cộng của tâm thu và tâm trương — sai, vì pha tâm trương chiếm khoảng hai phần ba chu kì nên phải lấy trọng số nghiêng về tâm trương theo công thức $P_d + \frac{1}{3}(P_s - P_d)$.

<sub>`lesson.biology.sinh-li-nguoi-intl.he-tuan-hoan-tim-va-huyet-ap`</sub>

---

### 2. Hệ hô hấp: thông khí và đường cong phân li hemoglobin
*The respiratory system: ventilation and the haemoglobin dissociation curve* · THPT (lớp 10-12) · ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được cơ chế thông khí và các thích nghi của phế nang theo định luật Fick
- Diễn giải được đường cong phân li oxy-hemoglobin dạng chữ S và hiệu ứng Bohr
- Tính được thông khí phế nang và lượng oxygen nhả cho mô từ số liệu

## Thông khí: bơm áp suất âm

Khác với ếch (nuốt khí bằng áp suất dương), người hít vào bằng cách **tạo áp suất âm**: cơ hoành hạ xuống, cơ liên sườn ngoài nâng lồng ngực → thể tích khoang ngực tăng → áp suất trong phổi tụt dưới áp suất khí quyển → khí tràn vào. Thở ra lúc nghỉ là quá trình **thụ động** nhờ tính đàn hồi của mô phổi.

## Phế nang là hiện thân của định luật Fick

$$\text{Tốc độ khuếch tán} \propto \frac{S \times \Delta C}{d}$$

- $S$ lớn: khoảng 300 triệu phế nang, tổng diện tích $70$-$80\ \text{m}^2$.
- $d$ nhỏ: thành phế nang và thành mao mạch đều chỉ một lớp tế bào dẹt, tổng khoảng $0{,}5\ \mu\text{m}$.
- $\Delta C$ được duy trì: thông khí liên tục làm mới khí, dòng máu liên tục mang oxygen đi.

Lớp surfactant do tế bào phế nang loại II tiết ra làm giảm sức căng bề mặt, ngăn phế nang xẹp lúc thở ra — thiếu chất này là nguyên nhân hội chứng suy hô hấp ở trẻ sinh non.

## Đường cong chữ S

Đồ thị phần trăm bão hoà hemoglobin theo $p\text{O}_2$ có dạng sigmoid, không phải đường thẳng. Nguyên nhân là **tính hợp tác**: gắn phân tử oxygen đầu tiên khó (đoạn dốc thoải ban đầu), nhưng nó làm hemoglobin đổi hình dạng khiến ba phân tử sau gắn dễ hơn nhiều (đoạn dốc đứng).

Hai hệ quả sinh lí quan trọng:

- Ở phổi ($p\text{O}_2 \approx 100$ mmHg) đường cong đã nằm ở đoạn phẳng trên, nên độ bão hoà đạt 97-98% và **ít bị ảnh hưởng** dù $p\text{O}_2$ giảm chút ít (lên cao, bệnh phổi nhẹ) — một cơ chế an toàn.
- Ở mô ($p\text{O}_2 \approx 40$ mmHg) ta đang ở đoạn dốc đứng, nên chỉ cần $p\text{O}_2$ giảm nhẹ là oxygen được nhả ra rất nhiều.

## Hiệu ứng Bohr và các biến thể

Mô hoạt động mạnh thải nhiều $\text{CO}_2$, tạo acid carbonic làm pH giảm; đường cong **dịch phải**, hemoglobin nhả thêm oxygen đúng nơi cần. Đây là một cơ chế tự điều chỉnh không cần bất kì tín hiệu thần kinh nào.

So sánh: hemoglobin **thai nhi** có đường cong dịch **trái** so với mẹ, tức ái lực cao hơn — điều kiện bắt buộc để thai lấy được oxygen từ máu mẹ qua nhau thai. Myoglobin ở cơ có ái lực còn cao hơn nữa và đường cong dạng hyperbol, phù hợp vai trò dự trữ oxygen chỉ nhả ra khi $p\text{O}_2$ xuống rất thấp.

**Lỗi thường gặp:**
- Tính thông khí bằng thể tích khí lưu thông nhân tần số rồi gọi đó là thông khí phế nang — sai, phải trừ khoảng chết giải phẫu vì lượng khí đó không bao giờ đến được bề mặt trao đổi.
- Nói đường cong dịch phải nghĩa là 'hemoglobin gắn oxygen kém nên có hại' — sai, dịch phải làm tăng lượng oxygen **nhả cho mô** ở đúng nơi đang cần; ở phổi độ bão hoà gần như không giảm vì đoạn đó của đường cong đã phẳng.
- Giải thích dạng chữ S của đường cong bằng 'nồng độ oxygen thay đổi' — sai, dạng sigmoid là hệ quả của tính hợp tác giữa bốn tiểu đơn vị hemoglobin; myoglobin chỉ có một chuỗi nên đường cong của nó là hyperbol.

<sub>`lesson.biology.sinh-li-nguoi-intl.he-ho-hap-va-van-chuyen-oxygen`</sub>

---

### 3. Hệ thần kinh: điện thế nghỉ, điện thế hoạt động và truyền tin qua synapse
*The nervous system: resting potential, action potential and synaptic transmission* · THPT (lớp 10-12) · ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được cơ sở ion của điện thế nghỉ và vai trò của bơm natri - kali
- Mô tả được các pha của điện thế hoạt động và cơ chế truyền theo quy luật tất cả hoặc không
- Phân tích được vai trò của bao myelin và các yếu tố ảnh hưởng tốc độ dẫn truyền

## Điện thế nghỉ: pin sinh học đã nạp sẵn

Bơm Na⁺/K⁺ đẩy 3 Na⁺ ra và lấy 2 K⁺ vào mỗi chu kì, tiêu tốn ATP. Kết quả: Na⁺ cao ngoài, K⁺ cao trong. Nhưng bản thân bơm chỉ đóng góp một phần nhỏ vào −70 mV; phần chính đến từ chỗ màng có nhiều kênh rò K⁺ hơn kênh rò Na⁺, nên K⁺ khuếch tán ra ngoài để lại các anion protein không qua được màng — bên trong tích điện âm.

Định lượng (mức mở rộng): điện thế cân bằng của riêng K⁺ tính theo phương trình Nernst cho khoảng $-90$ mV. Màng thực tế dừng ở $-70$ mV chứ không phải $-90$ mV vì nó vẫn hơi thấm Na⁺; phương trình Goldman gộp cả ba loại ion theo **tính thấm tương đối** và giải thích đúng con số đó. Nói cách khác, điện thế nghỉ là kết quả cạnh tranh giữa các dòng ion chứ không do một mình bơm quyết định.

## Điện thế hoạt động: bốn pha

1. **Khử cực**: kích thích đạt ngưỡng (khoảng −55 mV) → kênh Na⁺ cổng điện thế mở → Na⁺ ào vào → điện thế vọt lên +30 mV. Đây là một vòng **phản hồi dương**: khử cực mở thêm kênh Na⁺.
2. **Tái cực**: kênh Na⁺ tự bất hoạt, kênh K⁺ mở chậm hơn → K⁺ ra ngoài → điện thế tụt về âm.
3. **Ưu phân cực**: kênh K⁺ đóng trễ nên điện thế xuống dưới −70 mV một chút.
4. **Phục hồi**: bơm Na⁺/K⁺ khôi phục phân bố ion ban đầu.

**Giai đoạn trơ** (kênh Na⁺ chưa hết bất hoạt) có hai vai trò thiết yếu: bảo đảm xung chỉ truyền **một chiều** (vùng vừa đi qua chưa thể kích thích lại) và giới hạn tần số xung tối đa.

## Mã hoá cường độ

Vì mọi điện thế hoạt động đều có biên độ như nhau, hệ thần kinh không thể mã hoá cường độ bằng độ lớn xung. Nó dùng **tần số**: kích thích mạnh cho nhiều xung mỗi giây hơn, và huy động thêm nhiều nơron cùng phát.

## Synapse hoá học

Điện thế hoạt động tới cúc synapse → kênh Ca²⁺ mở → Ca²⁺ vào → túi chứa chất dẫn truyền dung hợp với màng → chất dẫn truyền khuếch tán qua khe → gắn thụ thể trên màng sau → mở kênh ion → điện thế màng sau thay đổi.

Hai lí do sinh học của cấu trúc tưởng như 'chậm' này: nó bảo đảm truyền **một chiều** (chỉ màng sau có thụ thể), và cho phép **tích hợp tín hiệu** — nơron sau cộng dồn các đầu vào kích thích và ức chế từ hàng nghìn synapse rồi mới quyết định có phát xung hay không. Đó chính là nền tảng vật lí của tính toán thần kinh.

Chất dẫn truyền phải bị loại bỏ ngay (acetylcholinesterase phân giải acetylcholine); thuốc trừ sâu lân hữu cơ ức chế enzyme này gây co cơ liên tục và liệt hô hấp.

**Lỗi thường gặp:**
- Cho rằng kích thích mạnh hơn tạo ra điện thế hoạt động lớn hơn — sai, theo quy luật tất cả hoặc không mọi xung có cùng biên độ; cường độ được mã hoá bằng tần số xung và số nơron được huy động.
- Nói bơm Na⁺/K⁺ trực tiếp tạo ra toàn bộ điện thế nghỉ −70 mV — sai, bơm chỉ đóng góp một phần nhỏ; nguyên nhân chính là màng thấm K⁺ mạnh hơn Na⁺ nên K⁺ khuếch tán ra để lại anion protein bên trong.
- Giải thích tính một chiều của xung thần kinh chỉ bằng cấu tạo synapse — chưa đủ, ngay trên sợi trục tính một chiều đã được bảo đảm bởi giai đoạn trơ: vùng vừa có xung đi qua chưa thể bị kích thích lại.

<sub>`lesson.biology.sinh-li-nguoi-intl.he-than-kinh-dien-the-hoat-dong-va-synapse`</sub>

---

### 4. Hệ nội tiết và điều hoà đường huyết
*The endocrine system and blood glucose regulation* · THPT (lớp 10-12) · ib, a-level, ap · 45 phút · trung-binh

**Mục tiêu:**
- So sánh được điều khiển bằng thần kinh và bằng nội tiết theo tốc độ, phạm vi và thời gian tác dụng
- Mô tả được vòng phản hồi âm điều hoà đường huyết bằng insulin và glucagon
- Phân biệt được đái tháo đường type 1 và type 2 theo cơ chế bệnh sinh

## Hai hệ điều khiển, hai thế mạnh

| | Thần kinh | Nội tiết |
|---|---|---|
| Tín hiệu | Xung điện + chất dẫn truyền | Hormone theo máu |
| Tốc độ | Mili giây | Giây đến giờ |
| Phạm vi | Rất cục bộ, có địa chỉ | Toàn thân, chọn lọc theo thụ thể |
| Thời gian tác dụng | Ngắn | Dài |

Hai hệ không tách rời: vùng dưới đồi vừa là trung khu thần kinh vừa là tuyến nội tiết, chính là điểm nối giữa chúng.

## Điều hoà đường huyết

Giá trị đặt khoảng $4$-$6\ \text{mmol/L}$ ($70$-$110\ \text{mg/dL}$). Bộ cảm nhận và trung tâm điều khiển nằm ngay tại đảo tuỵ Langerhans.

**Khi đường huyết tăng** (sau ăn): tế bào $\beta$ tiết **insulin** → tăng số kênh GLUT4 trên màng tế bào cơ và mô mỡ → glucose vào tế bào; đồng thời gan tăng tổng hợp glycogen và tăng chuyển glucose thành mỡ → đường huyết giảm.

**Khi đường huyết giảm** (đói, vận động): tế bào $\alpha$ tiết **glucagon** → gan phân giải glycogen và tân tạo đường từ amino acid, glycerol → đường huyết tăng.

Adrenaline bổ sung một đường điều khiển nhanh khi cần phản ứng khẩn cấp, tác dụng cùng chiều glucagon.

## Hai loại đái tháo đường

- **Type 1**: bệnh tự miễn, tế bào $\beta$ bị phá huỷ → **thiếu insulin tuyệt đối**. Thường khởi phát ở người trẻ, bắt buộc tiêm insulin.
- **Type 2**: tế bào đích **kháng insulin**; tuỵ ban đầu tăng tiết bù nên insulin máu **cao**, về sau tế bào $\beta$ kiệt sức. Liên quan mạnh tới béo phì và ít vận động; điều trị bắt đầu bằng thay đổi lối sống và thuốc uống.

Điểm phân biệt then chốt trong phân tích số liệu: đo nồng độ insulin. Type 1 cho insulin thấp, type 2 cho insulin bình thường hoặc cao — cùng một triệu chứng tăng đường huyết nhưng hai cơ chế trái ngược.

## Nghiệm pháp dung nạp glucose

Uống một lượng glucose chuẩn rồi đo đường huyết theo thời gian. Người bình thường: tăng lên khoảng $7$-$8\ \text{mmol/L}$ rồi trở về mức nền trong vòng 2 giờ. Người đái tháo đường: đỉnh cao hơn và **trở về rất chậm hoặc không trở về** — chính đặc điểm 'chậm trở về' này, chứ không phải đỉnh cao, mới là dấu hiệu vòng phản hồi âm bị hỏng.

**Lỗi thường gặp:**
- Nói insulin 'phân giải glucose' — sai, insulin không phải enzyme chuyển hoá glucose; nó là tín hiệu làm tăng số kênh GLUT4 trên màng và kích thích gan tổng hợp glycogen.
- Chẩn đoán đái tháo đường chỉ dựa vào đường huyết cao mà không xét insulin — sai, cả hai type đều tăng đường huyết nhưng type 1 có insulin thấp còn type 2 có insulin bình thường hoặc cao; điều trị hoàn toàn khác nhau.
- Cho rằng glucagon và insulin là 'hai hormone cùng điều hoà nên tác dụng bổ trợ nhau' — sai, chúng là cặp **đối vận** với tác dụng ngược chiều; chính sự đối lập đó cho phép điều chỉnh hai chiều nhanh và chính xác.

<sub>`lesson.biology.sinh-li-nguoi-intl.he-noi-tiet-va-dieu-hoa-duong-huyet`</sub>

---

### 5. Hệ miễn dịch: đáp ứng không đặc hiệu, đặc hiệu và cơ sở của vaccine
*The immune system: innate and adaptive responses, and the basis of vaccination* · THPT (lớp 10-12) · ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được miễn dịch không đặc hiệu và miễn dịch đặc hiệu theo tính đặc hiệu và trí nhớ
- Giải thích được cơ chế đáp ứng thứ phát và cơ sở khoa học của tiêm chủng
- Phân tích được nguyên nhân phải thay đổi vaccine cúm hằng năm

## Ba tuyến phòng thủ

1. **Hàng rào**: da, niêm mạc, dịch nhày, lysozyme trong nước mắt, pH acid dạ dày, hệ vi sinh vật cộng sinh.
2. **Miễn dịch không đặc hiệu**: thực bào (đại thực bào, bạch cầu trung tính), phản ứng viêm, sốt, interferon. Phản ứng nhanh (vài giờ), giống nhau với mọi tác nhân, **không có trí nhớ**.
3. **Miễn dịch đặc hiệu**: lympho B và lympho T. Chậm hơn ở lần đầu (vài ngày đến vài tuần) nhưng đặc hiệu cao và **có trí nhớ**.

## Chọn lọc dòng — ý tưởng trung tâm

Cơ thể **không** tạo kháng thể theo 'khuôn' của kháng nguyên. Thay vào đó, trong quá trình phát triển, các gen mã hoá thụ thể được tái tổ hợp ngẫu nhiên tạo ra hàng triệu dòng lympho, mỗi dòng một loại thụ thể. Kháng nguyên đến chỉ việc **chọn** dòng khớp với nó và kích thích dòng đó tăng sinh.

Sự phân hoá sau đó cho hai loại: **tương bào** tiết kháng thể ngay, và **tế bào nhớ** tồn tại nhiều năm.

## Vì sao đáp ứng thứ phát mạnh hơn

Lần đầu: chỉ vài tế bào khớp với kháng nguyên, phải mất nhiều ngày để tăng sinh — trong thời gian đó ta bị bệnh. Lần sau: đã có sẵn hàng nghìn tế bào nhớ đặc hiệu, đáp ứng khởi động trong vài giờ, hiệu giá kháng thể lên cao gấp nhiều lần và mầm bệnh bị dập tắt trước khi gây triệu chứng.

**Vaccine** khai thác đúng cơ chế này: đưa vào kháng nguyên đã làm mất khả năng gây bệnh (mầm bất hoạt, giảm độc lực, protein tái tổ hợp, mARN mã hoá protein bề mặt) để tạo tế bào nhớ mà không phải mắc bệnh.

**Miễn dịch cộng đồng**: khi tỉ lệ tiêm chủng đủ cao, chuỗi lây truyền bị cắt và cả những người không tiêm được (trẻ quá nhỏ, người suy giảm miễn dịch) cũng được bảo vệ gián tiếp. Ngưỡng này tính được: nếu mỗi ca lây trung bình cho $R_0$ người trong quần thể chưa có miễn dịch thì tỉ lệ cần miễn dịch là $H_c = 1 - 1/R_0$. Sởi có $R_0 \approx 15$ nên $H_c \approx 93\%$; vì vaccine không hiệu lực 100%, tỉ lệ **tiêm chủng** phải cao hơn nữa, trên 95%. Cúm mùa có $R_0$ nhỏ hơn nhiều nên ngưỡng thấp hơn.

## Vì sao vaccine cúm phải đổi hằng năm

Virus cúm có bộ gen ARN phân đoạn và ARN polymerase không có hoạt tính đọc sửa, nên tốc độ đột biến rất cao. Hai cơ chế: **trôi kháng nguyên** (đột biến điểm tích luỹ dần, làm kháng thể cũ nhận diện kém) và **chuyển kháng nguyên** (tráo đổi cả đoạn gen giữa các chủng, tạo biến chủng hoàn toàn mới, có thể gây đại dịch). Tế bào nhớ vẫn còn nhưng thụ thể của chúng không còn khớp với kháng nguyên đã biến đổi — do đó phải cập nhật vaccine.

**Lỗi thường gặp:**
- Nói cơ thể 'tạo kháng thể dựa trên khuôn của kháng nguyên' — sai, theo thuyết chọn lọc dòng các thụ thể đã được tạo ngẫu nhiên từ trước; kháng nguyên chỉ chọn và kích thích dòng phù hợp.
- Cho rằng vaccine cung cấp kháng thể cho cơ thể — sai, vaccine cung cấp **kháng nguyên** để cơ thể tự tạo kháng thể và tế bào nhớ (miễn dịch chủ động); truyền kháng thể có sẵn là huyết thanh, cho miễn dịch thụ động và không tạo trí nhớ.
- Giải thích việc phải tiêm vaccine cúm hằng năm bằng 'kháng thể hết hạn sau một năm' — sai, nguyên nhân chính là virus biến đổi kháng nguyên bề mặt nên tế bào nhớ cũ không còn nhận diện được chủng mới.

<sub>`lesson.biology.sinh-li-nguoi-intl.he-mien-dich`</sub>

---

### 6. Hệ bài tiết: lọc ở cầu thận, tái hấp thu và cân bằng thẩm thấu
*Excretion: glomerular filtration, reabsorption and osmoregulation* · THPT (lớp 10-12) · ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được cơ chế lọc ở cầu thận dựa trên cân bằng các áp suất
- Mô tả được cơ chế nhân nồng độ ngược dòng ở quai Henle
- Phân tích được vai trò của ADH trong vòng phản hồi âm điều hoà áp suất thẩm thấu máu

## Ba quá trình tạo nước tiểu

1. **Lọc ở cầu thận**: lọc theo kích thước, không chọn lọc theo chất. Mọi phân tử nhỏ (nước, glucose, amino acid, ion, ure) đều bị đẩy ra nang Bowman; tế bào máu và protein lớn bị giữ lại.
2. **Tái hấp thu ở ống thận**: thu lại những gì cơ thể cần. Ống lượn gần thu về gần như **100% glucose và amino acid**, khoảng 65% nước và Na⁺.
3. **Bài tiết chủ động**: thải thêm H⁺, K⁺ và một số thuốc từ máu vào lòng ống.

Chiến lược 'lọc bừa rồi thu lại' thoạt nhìn lãng phí — mỗi ngày lọc 180 L để cuối cùng thải 1,5 L. Nhưng nó có ưu điểm lớn: cơ thể không cần một thụ thể riêng cho mọi chất độc lạ; bất cứ phân tử nhỏ nào không được tái hấp thu chủ động sẽ tự động bị thải.

## Áp suất lọc

$$P_{\text{lọc}} = P_{\text{thuỷ tĩnh máu}} - (P_{\text{keo máu}} + P_{\text{thuỷ tĩnh nang}})$$

Áp suất thuỷ tĩnh trong mao mạch cầu thận cao bất thường (~55 mmHg) vì tiểu động mạch đi có đường kính **nhỏ hơn** tiểu động mạch đến — một chi tiết giải phẫu tạo ra toàn bộ động lực lọc.

## Quai Henle và nghịch lí nước tiểu cô đặc

Để thải chất tan mà giữ nước, thận phải tạo nước tiểu ưu trương so với máu — điều không thể làm bằng thẩm thấu đơn thuần. Giải pháp:

- **Nhánh xuống**: thấm nước, không thấm muối → nước ra, dịch cô đặc dần.
- **Nhánh lên**: không thấm nước, **bơm chủ động** Na⁺ và Cl⁻ ra ngoài → vùng tuỷ trở nên rất ưu trương (tới 1200 mOsm ở đỉnh tuỷ), còn dịch trong ống nhược trương dần.
- **Ống góp** đi xuyên qua vùng tuỷ ưu trương đó: nếu màng thấm nước (khi có ADH), nước thoát ra theo thẩm thấu và nước tiểu được cô đặc.

Gradient này là công trình tốn ATP nhưng chỉ cần duy trì một lần, sau đó ống góp khai thác lại nhiều lần. Động vật sa mạc như chuột túi kangaroo có quai Henle rất dài, tạo gradient mạnh hơn và nước tiểu cô đặc hơn nhiều.

## Vòng phản hồi âm với ADH

Mất nước → áp suất thẩm thấu máu tăng → thụ thể thẩm thấu ở vùng dưới đồi phát hiện → tuyến yên sau tiết ADH → tăng aquaporin ở ống góp → tái hấp thu nhiều nước → nước tiểu ít và đậm, áp suất thẩm thấu máu trở về bình thường. Uống nhiều nước hoặc uống rượu (ức chế tiết ADH) cho kết quả ngược lại.

**Lỗi thường gặp:**
- Nói cầu thận 'lọc chọn lọc, chỉ cho chất thải đi qua' — sai, màng lọc chỉ phân biệt theo kích thước và điện tích nên glucose, amino acid và ion cũng bị lọc ra; tính chọn lọc thực sự nằm ở bước tái hấp thu.
- Cho rằng ống góp tự bơm nước ra khỏi lòng ống — sai, nước chỉ di chuyển thụ động theo thẩm thấu; điều kiện bắt buộc là gradient thẩm thấu ở vùng tuỷ do quai Henle tạo ra và sự có mặt của aquaporin do ADH điều khiển.
- Nghĩ ADH làm tăng lượng nước tiểu vì tên gọi có chữ 'niệu' — sai, ADH là hormone **chống** bài niệu: nó tăng tái hấp thu nước nên làm nước tiểu ít hơn và đậm đặc hơn.

<sub>`lesson.biology.sinh-li-nguoi-intl.he-bai-tiet-va-can-bang-tham-thau`</sub>

---

## Unit 1: Chemistry of Life (Hoá học của sự sống)

### 1. Nước: liên kết hydrogen và các tính chất nâng đỡ sự sống
*Water: hydrogen bonding and the properties that support life* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Giải thích được vì sao phân tử nước phân cực và hình thành được liên kết hydrogen
- Phân tích được cách bốn tính chất của nước (bám dính, nhiệt dung riêng, nhiệt hoá hơi, dung môi) bắt nguồn từ cùng một nguyên nhân cấu trúc
- Vận dụng được khái niệm pH và hệ đệm để giải thích sự ổn định của môi trường trong tế bào

## Vì sao một môn sinh học lại mở đầu bằng nước

Cơ thể người chứa khoảng 60% nước theo khối lượng, và mọi phản ứng sinh hoá đều diễn ra trong môi trường nước. Nhưng nước không chỉ là *nơi chứa*: chính các tính chất bất thường của nó đã định hình cách sự sống vận hành.

## Một nguyên nhân, nhiều hệ quả

Oxygen có độ âm điện 3,44 còn hydrogen 2,20. Cặp electron liên kết bị kéo lệch về phía oxygen, tạo ra $\delta^-$ trên O và $\delta^+$ trên mỗi H. Vì phân tử có hình chữ V (góc $104{,}5^\circ$), hai lưỡng cực **không** triệt tiêu nhau — nước là phân tử phân cực. Mỗi phân tử nước có thể tạo tối đa 4 liên kết hydrogen với các phân tử lân cận.

Từ một nguyên nhân đó suy ra bốn nhóm hệ quả sinh học:

- **Bám dính và liên kết (cohesion - adhesion)**: cột nước trong mạch gỗ không đứt khi bị kéo lên hàng chục mét; sức căng bề mặt cho phép côn trùng đi trên mặt nước.
- **Nhiệt dung riêng lớn** ($4{,}18\ \text{J g}^{-1}\text{K}^{-1}$): phải phá vỡ liên kết hydrogen trước khi phân tử chuyển động nhanh hơn, nên nhiệt độ cơ thể và đại dương ổn định.
- **Nhiệt hoá hơi lớn** ($\approx 2260\ \text{J g}^{-1}$): đổ mồ hôi và thoát hơi nước làm mát rất hiệu quả.
- **Dung môi phân cực**: hoà tan ion và các chất ưa nước; ngược lại đẩy các phân tử kị nước lại gần nhau — đây chính là động lực làm màng phospholipid tự lắp ráp và protein cuộn gấp.

## Nước và pH

Nước tự phân li rất ít: $\text{H}_2\text{O} \rightleftharpoons \text{H}^+ + \text{OH}^-$, với $[\text{H}^+] = 10^{-7}\ \text{M}$ ở $25^\circ\text{C}$, tức pH = 7. Vì $\text{pH} = -\log[\text{H}^+]$, giảm 1 đơn vị pH nghĩa là nồng độ $\text{H}^+$ tăng **10 lần**. Enzyme rất nhạy với pH nên tế bào phải dùng hệ đệm.

**Giới hạn áp dụng**: các lập luận trên chỉ đúng cho nước lỏng ở khoảng nhiệt độ sinh lí. Ở nhiệt độ dưới $0^\circ\text{C}$ mạng tinh thể mở của nước đá làm nước đá nhẹ hơn nước lỏng — có lợi cho sinh vật dưới băng nhưng lại gây vỡ tế bào khi mô đóng băng.

**Lỗi thường gặp:**
- Nói liên kết hydrogen là 'một loại liên kết cộng hoá trị yếu' — sai, vì nó không hề có sự dùng chung electron, mà thuần tuý là lực hút tĩnh điện giữa các phần điện tích trái dấu; đó là lí do nó đứt và nối lại liên tục ở nhiệt độ phòng.
- Cho rằng pH 4 'acid gấp đôi' pH 8 — sai, vì pH là thang logarit cơ số 10: chênh 4 đơn vị nghĩa là nồng độ H+ chênh $10^4$ lần chứ không phải 2 lần.
- Giải thích nhiệt dung riêng lớn của nước bằng 'phân tử nước nặng' — sai, vì khối lượng phân tử nước (18) nhỏ hơn nhiều so với $\text{H}_2\text{S}$ (34) vốn có nhiệt dung riêng nhỏ hơn; nguyên nhân thật là năng lượng bị tiêu tốn để phá liên kết hydrogen chứ không làm tăng động năng.

<sub>`lesson.biology.hoa-hoc-su-song.nuoc-va-lien-ket-hydrogen`</sub>

---

### 2. Đại phân tử sinh học: monome, phản ứng ngưng tụ và thuỷ phân
*Biological macromolecules: monomers, condensation and hydrolysis* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Xác định được monome và loại liên kết đặc trưng của bốn nhóm đại phân tử sinh học
- Giải thích được vì sao ngưng tụ và thuỷ phân là hai chiều của cùng một phản ứng
- Phân tích được quan hệ giữa cấu trúc mạch của polysaccharide và chức năng dự trữ hay cấu trúc

## Bốn nhóm phân tử, một quy luật lắp ráp

Sự sống dùng đi dùng lại rất ít loại linh kiện. Toàn bộ carbohydrate được xây từ monosaccharide, toàn bộ protein từ 20 loại amino acid, toàn bộ acid nucleic từ 4-5 loại nucleotide. Điều đáng nói là **cách nối** chúng lại giống nhau về nguyên tắc.

## Ngưng tụ và thuỷ phân

Mỗi lần thêm một monome vào chuỗi, tế bào loại ra một phân tử nước:

$$n\ \text{monome} \longrightarrow \text{polime } n\text{ đơn phân} + (n-1)\ \text{H}_2\text{O}$$

Liên kết tạo thành mang tên riêng theo từng nhóm: liên kết **glycosidic** ở carbohydrate, liên kết **peptide** ở protein, liên kết **phosphodiester** ở acid nucleic, liên kết **ester** giữa glycerol và acid béo. Chiều ngược lại — thuỷ phân — là cách tiêu hoá thức ăn và cũng là cách tế bào tái sử dụng vật liệu.

Vì hai chiều dùng chung một cân bằng, điều quyết định chiều diễn ra trong tế bào là **enzyme nào đang có mặt** và nồng độ chất tham gia, chứ không phải bản thân liên kết ưa chiều nào.

## Carbohydrate: cùng đơn phân, khác chức năng

Tinh bột, glycogen và cellulose đều là polime của glucose, nhưng:

- Tinh bột và glycogen dùng $\alpha$-glucose, mạch xoắn, phân nhánh nhiều (glycogen nhánh dày hơn) → dễ bị enzyme cắt nhanh → **dự trữ năng lượng**.
- Cellulose dùng $\beta$-glucose, mỗi đơn phân lật ngược $180^\circ$ → mạch thẳng, xếp song song, liên kết hydrogen giữa các mạch tạo vi sợi → **chức năng cấu trúc**, và người không có enzyme cellulase nên không tiêu hoá được.

## Lipid: ngoại lệ có lí do

Triglyceride và phospholipid không phải polime vì chúng không có đơn phân lặp lại nối tiếp vô hạn. Điều đáng nhớ là mật độ năng lượng: lipid cho khoảng $38\ \text{kJ g}^{-1}$ so với $17\ \text{kJ g}^{-1}$ của carbohydrate, do carbon trong acid béo ở trạng thái khử sâu hơn nên oxi hoá được nhiều hơn.

**Lỗi thường gặp:**
- Viết số phân tử nước giải phóng bằng số monome — sai vì chuỗi thẳng $n$ đơn phân chỉ có $n-1$ liên kết; chỉ khi chuỗi khép vòng thì mới có $n$ liên kết.
- Nói cellulose và tinh bột khác nhau vì 'khác loại đường' — sai, cả hai đều là polime của glucose; khác biệt nằm ở đồng phân $\alpha$ hay $\beta$ và do đó ở hình học liên kết glycosidic.
- Coi lipid là polime của acid béo — sai, vì acid béo không nối tiếp nhau thành chuỗi lặp; chúng chỉ gắn riêng lẻ vào khung glycerol nên triglyceride luôn có tối đa ba gốc.

<sub>`lesson.biology.hoa-hoc-su-song.dai-phan-tu-ngung-tu-thuy-phan`</sub>

---

### 3. Bốn bậc cấu trúc protein và quan hệ cấu trúc - chức năng
*The four levels of protein structure and structure-function relationship* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được loại liên kết giữ ổn định từng bậc cấu trúc protein
- Giải thích được vì sao trình tự amino acid quyết định toàn bộ hình dạng không gian
- Phân tích được cơ chế biến tính protein bởi nhiệt độ và pH

## Vì sao hình dạng lại là tất cả

Một enzyme chỉ xúc tác đúng một loại phản ứng, một kháng thể chỉ nhận đúng một kháng nguyên. Tính đặc hiệu này không nằm ở thành phần hoá học — mọi protein đều làm từ cùng 20 amino acid — mà nằm ở **hình dạng ba chiều**.

## Bốn bậc, bốn loại liên kết

| Bậc | Nội dung | Liên kết giữ ổn định |
|---|---|---|
| 1 | Trình tự amino acid | Liên kết peptide (cộng hoá trị) |
| 2 | Xoắn $\alpha$, phiến gấp $\beta$ | Liên kết hydrogen của **khung** |
| 3 | Hình dạng ba chiều toàn chuỗi | Tương tác kị nước, liên kết hydrogen, ion, cầu disulfide giữa các **mạch bên R** |
| 4 | Lắp ráp nhiều chuỗi | Cùng loại liên kết như bậc ba nhưng giữa các tiểu đơn vị |

Điểm mấu chốt: bậc hai chỉ dùng khung, bậc ba dùng mạch bên. Đó là lí do bậc hai giống nhau ở mọi protein còn bậc ba thì mỗi protein một kiểu.

## Nguyên lí Anfinsen

Thí nghiệm kinh điển với ribonuclease cho thấy: khi loại tác nhân biến tính, protein tự cuộn lại đúng hình dạng cũ và phục hồi hoạt tính. Kết luận: **toàn bộ thông tin về hình dạng đã nằm sẵn trong trình tự bậc một**. Trong tế bào sống, protein chaperone chỉ giúp quá trình này diễn ra nhanh và tránh kết tụ, chứ không cung cấp thông tin mới.

## Khi nào lập luận này không còn đủ

Một số protein nội tại không có cấu trúc cố định (intrinsically disordered) chỉ định hình khi gắn đối tác. Và prion cho thấy cùng một trình tự có thể tồn tại ở hai hình dạng bền khác nhau — trường hợp trình tự **không** quyết định duy nhất một hình dạng.

## Biến tính

Nhiệt độ cao làm tăng dao động, phá liên kết hydrogen và tương tác kị nước. Thay đổi pH làm nhóm -COO$^-$ và -NH$_3^+$ đổi trạng thái tích điện, phá liên kết ion. Cả hai đều **không** cắt liên kết peptide, nên bậc một còn nguyên — đó là lí do lòng trắng trứng chín vẫn còn đủ amino acid dinh dưỡng.

**Lỗi thường gặp:**
- Nói liên kết hydrogen của bậc hai hình thành giữa các mạch bên R — sai, vì bậc hai chỉ dùng nhóm C=O và N-H của khung polypeptide; nếu dùng mạch bên thì mỗi trình tự sẽ cho một kiểu xoắn khác nhau, trái với thực tế xoắn $\alpha$ giống nhau ở mọi protein.
- Cho rằng biến tính làm đứt liên kết peptide — sai, vì nhiệt độ nấu ăn hay pH dạ dày chỉ đủ phá các liên kết yếu; cắt liên kết peptide cần enzyme protease hoặc đun sôi trong acid mạnh nhiều giờ.
- Coi mọi protein đều có cấu trúc bậc bốn — sai, bậc bốn chỉ tồn tại ở protein gồm từ hai chuỗi polypeptide trở lên; myoglobin chỉ có một chuỗi nên dừng ở bậc ba.

<sub>`lesson.biology.hoa-hoc-su-song.cau-truc-protein-bon-bac`</sub>

---

### 4. Cấu trúc acid nucleic: ADN, ARN và nguyên tắc bổ sung
*Nucleic acid structure: DNA, RNA and complementary base pairing* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Mô tả được cấu tạo của một nucleotide và cách các nucleotide nối thành mạch có chiều 5' → 3'
- Giải thích được vì sao hai mạch ADN phải đối song song và tuân theo quy tắc Chargaff
- Vận dụng được quan hệ giữa số nucleotide, chiều dài gen và số liên kết hydrogen

## Bài toán mà ADN phải giải

Vật chất di truyền phải làm được ba việc mâu thuẫn nhau: lưu trữ lượng thông tin khổng lồ, sao chép chính xác, và thỉnh thoảng biến đổi. Cấu trúc xoắn kép giải cả ba cùng lúc.

## Từ nucleotide tới xoắn kép

Một nucleotide gồm đường pentose + phosphate + base. Các nucleotide nối nhau bằng liên kết phosphodiester giữa C5' của cái này và C3' của cái kia, tạo khung có **chiều**. Đầu mạch còn nhóm phosphate tự do gọi là đầu 5', đầu còn nhóm -OH tự do là đầu 3'.

Hai mạch xoắn quanh một trục chung, khung đường-phosphate quay ra ngoài (ưa nước), base quay vào trong (kị nước). Base bắt cặp theo nguyên tắc bổ sung:

$$A = T\ (2\ \text{liên kết H}), \qquad G \equiv C\ (3\ \text{liên kết H})$$

Một purine (A, G — hai vòng) luôn bắt cặp với một pyrimidine (T, C — một vòng) nên đường kính xoắn không đổi, bằng $2\ \text{nm}$. Mỗi chu kì xoắn dài $34\ \text{Å} = 3{,}4\ \text{nm}$ và chứa 10 cặp base, nên mỗi cặp base cách nhau $3{,}4\ \text{Å}$.

## Quy tắc Chargaff

Hệ quả trực tiếp của bắt cặp bổ sung: trong ADN mạch kép, $\%A = \%T$ và $\%G = \%C$, do đó $\%A + \%G = 50\%$. Chargaff phát hiện quy luật này **trước** khi biết cấu trúc xoắn kép, và chính nó là manh mối then chốt cho Watson - Crick.

## ADN so với ARN

ARN dùng ribose (có -OH ở C2'), dùng uracil thay thymine, và thường ở dạng mạch đơn. Nhóm -OH thêm vào ở C2' làm ARN kém bền hoá học hơn — phù hợp với vai trò bản sao tạm thời. ARN mạch đơn còn tự gấp lại được thành cấu trúc không gian (như tARN hình chữ L), nhờ đó một số ARN có hoạt tính xúc tác (ribozyme).

**Lưu ý áp dụng**: quy tắc Chargaff chỉ đúng cho ADN mạch kép. Với ADN mạch đơn của một số virus, hay với ARN, %A hoàn toàn có thể khác %U.

**Lỗi thường gặp:**
- Dùng công thức $L = (N/2) \times 3{,}4$ nhưng quên chia đôi, cho ra chiều dài gấp đôi — sai vì $3{,}4\ \text{Å}$ là khoảng cách giữa hai **cặp** base liên tiếp chứ không phải giữa hai nucleotide trên cùng một mạch.
- Áp dụng %A = %T cho ARN hoặc cho một mạch đơn của gen — sai, vì quy tắc Chargaff là hệ quả của bắt cặp bổ sung giữa hai mạch; trên một mạch riêng lẻ tỉ lệ các base hoàn toàn tự do.
- Nói A bắt cặp với T bằng 3 liên kết hydrogen — sai; A-T có 2 liên kết, G-C có 3, và chính điều này khiến vùng giàu G-C có nhiệt độ nóng chảy cao hơn.

<sub>`lesson.biology.hoa-hoc-su-song.cau-truc-axit-nucleic`</sub>

---

## Unit 2: Cell Structure and Function (Cấu trúc và chức năng tế bào)

### 1. Tế bào nhân sơ và nhân thực: phân khoang chức năng
*Prokaryotic and eukaryotic cells: functional compartmentalisation* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được tế bào nhân sơ và nhân thực theo tiêu chí có màng nhân và bào quan có màng
- Giải thích được lợi ích của việc phân khoang bằng hệ thống nội màng
- Vận dụng được công thức độ phóng đại để tính kích thước thật của cấu trúc tế bào

## Cùng làm một việc, hai cách tổ chức

Cả vi khuẩn lẫn tế bào gan đều phải sao chép ADN, tổng hợp protein và tạo ATP. Khác biệt nằm ở **tổ chức không gian**.

## Nhân sơ: một khoang duy nhất

Tế bào nhân sơ (đường kính $0{,}5$-$5\ \mu\text{m}$) không có màng nhân; ADN vòng nằm trong vùng nhân (nucleoid) tiếp xúc trực tiếp với tế bào chất. Hệ quả quan trọng: **phiên mã và dịch mã diễn ra đồng thời** trên cùng một phân tử mARN. Ribosome là loại 70S. Thành tế bào bằng peptidoglycan — đích tác dụng của penicillin.

## Nhân thực: hệ thống nội màng

Tế bào nhân thực ($10$-$100\ \mu\text{m}$) tách nhân bằng màng kép có lỗ nhân, nên phiên mã (trong nhân) và dịch mã (ở tế bào chất) tách rời về không gian và thời gian. Khoảng cách này chính là nơi chèn thêm bước hoàn thiện ARN và nhiều tầng điều hoà biểu hiện gen mà nhân sơ không có.

Hệ nội màng vận hành như một dây chuyền: **lưới nội chất hạt** tổng hợp protein tiết → túi vận chuyển → **bộ máy Golgi** biến đổi và dán nhãn → túi tiết hoặc **lysosome**. Ti thể và lục lạp nằm ngoài hệ này vì chúng có nguồn gốc nội cộng sinh.

## Vì sao phân khoang lại quý

- Lysosome giữ pH ~4,8 cho enzyme thuỷ phân hoạt động mà không tiêu hoá phần còn lại của tế bào.
- Màng trong ti thể duy trì được gradient $\text{H}^+$ — điều bất khả nếu không có hai lớp màng.
- Tăng diện tích màng cho các phản ứng gắn màng (mào ti thể, thylakoid).

## Quan sát tế bào

Muốn nhìn thấy bào quan phải dùng kính hiển vi điện tử vì ribosome chỉ khoảng $25\ \text{nm}$, nhỏ hơn giới hạn phân giải $200\ \text{nm}$ của kính quang học. Công thức làm việc bắt buộc: $\text{độ phóng đại} = \dfrac{\text{kích thước ảnh}}{\text{kích thước thật}}$, và luôn đổi về cùng một đơn vị trước khi chia.

**Lỗi thường gặp:**
- Quên đổi đơn vị trước khi chia trong công thức độ phóng đại — sai vì độ phóng đại là tỉ số không thứ nguyên, chỉ đúng khi tử và mẫu cùng đơn vị; chia mm cho μm cho kết quả lệch 1000 lần.
- Nhầm độ phóng đại với độ phân giải — sai, vì phóng to một ảnh mờ chỉ cho ảnh mờ to hơn; độ phân giải bị chặn bởi bước sóng của bức xạ dùng để quan sát chứ không tăng theo số lần phóng đại.
- Cho rằng tế bào nhân sơ 'không có bào quan' — sai, chúng vẫn có ribosome 70S; điều đúng phải nói là chúng không có bào quan **có màng bao bọc**.

<sub>`lesson.biology.cau-truc-te-bao.te-bao-nhan-so-va-nhan-thuc`</sub>

---

### 2. Tỉ lệ diện tích bề mặt trên thể tích và giới hạn kích thước tế bào
*Surface area to volume ratio and limits on cell size* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Tính được tỉ lệ S/V cho khối lập phương, hình cầu và hình trụ
- Giải thích được vì sao S/V giảm khi kích thước tăng và hệ quả sinh học của quy luật đó
- Phân tích được các cách thích nghi làm tăng S/V ở tế bào và ở cơ thể

## Câu hỏi mở đầu: vì sao không có vi khuẩn to bằng quả bóng

Câu trả lời nằm ở hình học chứ không ở sinh học. Khi một tế bào lớn lên gấp đôi về mỗi chiều, diện tích màng tăng $2^2 = 4$ lần nhưng thể tích tăng $2^3 = 8$ lần. Nhu cầu (tỉ lệ với V) tăng nhanh gấp đôi so với khả năng cung cấp (tỉ lệ với S).

## Công thức nền

Với khối lập phương cạnh $a$: $S = 6a^2$, $V = a^3$, do đó

$$\frac{S}{V} = \frac{6a^2}{a^3} = \frac{6}{a}$$

Với hình cầu bán kính $r$: $S = 4\pi r^2$, $V = \dfrac{4}{3}\pi r^3$, nên $\dfrac{S}{V} = \dfrac{3}{r}$.

Cả hai đều có dạng **hằng số chia cho kích thước**. Đây là quy luật tổng quát: mọi họ hình đồng dạng đều cho $S/V \propto 1/L$.

## Hai hệ quả sinh học

1. **Giới hạn kích thước tế bào.** Ngoài S/V, còn một rào cản thứ hai: thời gian khuếch tán $t$ tỉ lệ với $x^2$. Tăng bán kính 10 lần thì thời gian để phân tử đi từ màng tới trung tâm tăng 100 lần. Tế bào lớn sẽ 'chết đói ở giữa' dù màng vẫn đủ diện tích.

2. **Chiến lược thích nghi.** Sinh vật lách quy luật bằng cách thay đổi hình dạng chứ không thay đổi toán học: tế bào biểu mô ruột có vi nhung mao, phế nang chia phổi thành 300 triệu túi nhỏ, tế bào hồng cầu lõm hai mặt, rễ cây có lông hút, ti thể có mào. Ở mức cơ thể, động vật lớn phải phát triển **hệ vận chuyển** (tuần hoàn) thay vì dựa vào khuếch tán.

## Ứng dụng trong bài thi

Cả AP và A-Level đều hay hỏi dạng: cho nhiều khối thạch chứa chỉ thị pH, ngâm trong acid, đo phần trăm thể tích bị thấm. Kết quả luôn cho thấy khối nhỏ thấm hết nhanh hơn — bằng chứng thực nghiệm trực tiếp cho quy luật $S/V$.

**Lỗi thường gặp:**
- Trừ độ dày thấm chỉ một lần khi tính cạnh lõi — sai, vì chất thấm vào từ cả hai mặt đối diện của mỗi chiều nên mỗi cạnh giảm đi hai lần độ dày thấm.
- Kết luận 'tế bào lớn có S/V lớn vì diện tích lớn hơn' — sai, vì S/V là tỉ số chứ không phải giá trị S; diện tích tuyệt đối tăng nhưng thể tích tăng nhanh hơn nên tỉ số giảm.
- So sánh S/V giữa hai vật khác hình dạng rồi kết luận về kích thước — sai, vì hằng số trong công thức phụ thuộc hình dạng (6/a cho lập phương, 3/r cho cầu); chỉ so sánh được khi cùng dạng hình hoặc khi đã tính ra số cụ thể.

<sub>`lesson.biology.cau-truc-te-bao.ti-le-dien-tich-tren-the-tich`</sub>

---

### 3. Màng sinh chất và mô hình khảm động
*The plasma membrane and the fluid mosaic model* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao phospholipid tự lắp ráp thành lớp kép trong nước
- Phân tích được vai trò của cholesterol và protein màng đối với tính chất của màng
- Chứng minh được tính động của màng bằng bằng chứng thực nghiệm

## Màng tự lắp ráp như thế nào

Phospholipid có một đầu phosphate tích điện (ưa nước) và hai đuôi acid béo (kị nước). Khi thả vào nước, hệ tự sắp xếp sao cho đuôi kị nước tránh tiếp xúc nước. Đây **không** phải là lực hút giữa các đuôi mà là hệ quả entropy: nước quanh chuỗi kị nước bị buộc phải sắp xếp trật tự; đẩy các đuôi lại gần nhau giải phóng các phân tử nước đó, làm entropy toàn hệ tăng. Vì vậy màng tự vá lành khi bị chọc thủng nhỏ.

## 'Khảm' và 'động'

**Khảm**: protein nằm rải rác trong nền lipid như các mảnh khảm — protein xuyên màng, protein bám màng, glycoprotein và glycolipid (tạo lớp áo đường nhận diện tế bào).

**Động**: các phân tử di chuyển ngang tự do. Thí nghiệm Frye - Edidin (1970) dung hợp tế bào người và tế bào chuột, đánh dấu protein bằng huỳnh quang hai màu; sau 40 phút ở $37^\circ\text{C}$ hai màu trộn đều — bằng chứng trực tiếp cho tính động. Đáng chú ý: ở $0^\circ\text{C}$ hai màu không trộn, chứng tỏ đây là khuếch tán phụ thuộc nhiệt độ.

## Cholesterol: chất đệm hai chiều

Cholesterol chèn giữa các phospholipid ở màng động vật và có tác dụng **ngược nhau tuỳ nhiệt độ**:

- Nhiệt độ cao: hạn chế chuyển động của đuôi acid béo → giảm tính lỏng, giảm rò rỉ.
- Nhiệt độ thấp: chèn vào giữa, ngăn các đuôi xếp sát thành tinh thể → giữ màng khỏi đông cứng.

Đây là ý tưởng hay bị hiểu nhầm nhất trong bài, nên hãy nhớ cholesterol là **chất điều hoà độ lỏng**, không phải chất làm cứng.

## Tính thấm chọn lọc

Lõi kị nước cho phép phân tử nhỏ không phân cực ($\text{O}_2$, $\text{CO}_2$) và phân tử nhỏ phân cực không tích điện (ure, ethanol) đi qua trực tiếp. Ion và phân tử lớn phân cực (glucose, amino acid) bị chặn và bắt buộc phải qua protein — đó chính là nền tảng để tế bào **kiểm soát** thành phần bên trong.

**Lỗi thường gặp:**
- Nói cholesterol 'làm màng cứng hơn' như một kết luận chung — sai, vì tác dụng của cholesterol phụ thuộc nhiệt độ: giảm tính lỏng khi nóng nhưng ngăn đông cứng khi lạnh.
- Cho rằng đuôi kị nước 'hút nhau' nên màng hình thành — sai, vì giữa các chuỗi hydrocarbon chỉ có lực van der Waals rất yếu; động lực thật là hiệu ứng kị nước, tức sự tăng entropy của nước khi các đuôi bị đẩy lại với nhau.
- Nghĩ mọi phân tử nhỏ đều qua màng dễ dàng — sai, vì yếu tố quyết định là **độ phân cực và điện tích** chứ không chỉ kích thước; ion Na⁺ nhỏ hơn phân tử ethanol nhiều nhưng lại gần như không qua được lớp lipid kép.

<sub>`lesson.biology.cau-truc-te-bao.mang-sinh-chat-kham-dong`</sub>

---

### 4. Vận chuyển thụ động và vận chuyển chủ động qua màng
*Passive and active transport across membranes* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được khuếch tán đơn giản, khuếch tán tăng cường và vận chuyển chủ động theo tiêu chí gradient và ATP
- Vận dụng được định luật Fick để dự đoán tốc độ khuếch tán
- Giải thích được cơ chế bơm natri - kali và ý nghĩa của vận chuyển chủ động thứ cấp

## Ba câu hỏi để phân loại mọi kiểu vận chuyển

Gặp bất kì cơ chế vận chuyển nào, chỉ cần hỏi ba câu: (1) đi **xuôi** hay **ngược** gradient? (2) có cần **protein** không? (3) có tiêu tốn **ATP** không? Bảng phân loại rơi ra ngay lập tức.

| Kiểu | Gradient | Protein | ATP |
|---|---|---|---|
| Khuếch tán đơn giản | Xuôi | Không | Không |
| Khuếch tán tăng cường | Xuôi | Có | Không |
| Thẩm thấu | Xuôi (thế nước) | Không hoặc aquaporin | Không |
| Chủ động sơ cấp | Ngược | Có | Có |
| Chủ động thứ cấp | Ngược cho chất này | Có | Gián tiếp |

## Định luật Fick và ba cách tăng tốc

$$\text{Tốc độ khuếch tán} \propto \frac{S \times \Delta C}{d}$$

Mọi thích nghi trao đổi khí đều đọc được từ công thức này: phế nang tăng $S$, mao mạch dày đặc và dòng máu liên tục duy trì $\Delta C$ lớn, thành phế nang chỉ một lớp tế bào để $d$ nhỏ. Ở cá, dòng máu chảy ngược chiều dòng nước qua mang (dòng ngược chiều) giữ $\Delta C$ dương suốt chiều dài phiến mang.

## Dấu hiệu nhận ra khuếch tán tăng cường

Khi vẽ đồ thị tốc độ vận chuyển theo nồng độ ngoài: khuếch tán đơn giản cho **đường thẳng** không giới hạn, còn khuếch tán tăng cường cho đường **cong tới bão hoà**. Nguyên nhân là số protein vận chuyển hữu hạn — cùng logic với $V_{max}$ của enzyme.

## Bơm natri - kali

Mỗi chu kì bơm dùng 1 ATP để đẩy **3 Na⁺ ra** và **2 K⁺ vào**. Vì số điện tích dương ra nhiều hơn vào, bơm sinh ra chênh lệch điện tích: bên trong âm hơn bên ngoài — nền tảng của điện thế nghỉ ở nơron.

Gradient Na⁺ đó lại được 'bán lại': ở tế bào biểu mô ruột, chất đồng vận chuyển SGLT1 cho Na⁺ đi vào theo gradient và **kéo theo glucose ngược gradient**. Đây là vận chuyển chủ động thứ cấp — không dùng ATP trực tiếp nhưng sẽ dừng ngay nếu bơm Na⁺/K⁺ bị ức chế.

**Lỗi thường gặp:**
- Cho rằng cứ có protein tham gia thì là vận chuyển chủ động — sai, vì kênh và chất mang trong khuếch tán tăng cường vẫn chỉ cho chất đi xuôi gradient và không dùng ATP; tiêu chí quyết định là chiều gradient chứ không phải sự có mặt của protein.
- Nói vận chuyển chủ động thứ cấp 'không cần năng lượng' — sai, nó vẫn dùng năng lượng nhưng ở dạng gradient ion đã được ATP nạp sẵn; ngừng cấp ATP thì gradient tan và cơ chế dừng.
- Kết luận từ đồ thị bão hoà rằng 'chất tan đã hết' — sai, đường cong đạt trần vì mọi protein vận chuyển đều đang bận, tăng nồng độ ngoài không giúp thêm được nữa.

<sub>`lesson.biology.cau-truc-te-bao.van-chuyen-thu-dong-va-chu-dong`</sub>

---

### 5. Thẩm thấu, thế nước và thế chất tan
*Osmosis, water potential and solute potential* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Xác định được chiều di chuyển của nước dựa trên so sánh thế nước
- Tính được thế chất tan của dung dịch bằng công thức $\Psi_S = -iCRT$
- Phân tích được phản ứng khác nhau của tế bào động vật và tế bào thực vật trong môi trường nhược trương

## Vì sao phải bỏ khái niệm 'nồng độ' để dùng 'thế nước'

Nói 'nước đi từ nơi loãng sang nơi đặc' đúng trong ống nghiệm nhưng sai với tế bào thực vật đã trương nước: ở đó dịch bào đặc hơn nước ngoài mà nước vẫn không vào thêm. Lí do là thành tế bào tạo áp suất ngược. Cần một đại lượng gộp cả hai tác nhân — đó là **thế nước**:

$$\Psi = \Psi_S + \Psi_P$$

Nguyên tắc duy nhất cần nhớ: **nước luôn đi từ nơi có $\Psi$ cao sang nơi có $\Psi$ thấp**, tức từ nơi ít âm sang nơi âm nhiều hơn.

## Tính thế chất tan

$$\Psi_S = -iCRT$$

- $i$: số tiểu phân mà một phân tử chất tan phân li ra (sucrose $i=1$, NaCl $i=2$, $\text{CaCl}_2$ $i=3$).
- $C$: nồng độ mol/L; $R = 0{,}0831\ \text{L·bar·mol}^{-1}\text{K}^{-1}$; $T$ tính bằng **Kelvin**.

Dấu trừ có ý nghĩa vật lí: thêm chất tan luôn **hạ** thế nước.

## Hai kiểu tế bào, hai số phận

Trong môi trường **nhược trương** ($\Psi_{\text{ngoài}} > \Psi_{\text{trong}}$), nước vào tế bào:

- Tế bào động vật không có thành → phồng lên rồi **vỡ** (tan bào). Đây là lí do dịch truyền tĩnh mạch phải đẳng trương với huyết tương (NaCl 0,9%).
- Tế bào thực vật có thành cellulose → $\Psi_P$ tăng dần cho tới khi $\Psi$ trong bằng $\Psi$ ngoài, tế bào **trương nước** và dừng lại. Trạng thái trương chính là cơ chế giữ cây đứng thẳng; mất nước thì cây héo.

Trong môi trường **ưu trương**, tế bào thực vật mất nước, màng sinh chất tách khỏi thành: **co nguyên sinh**. Tại thời điểm bắt đầu tách, $\Psi_P = 0$ nên $\Psi_{\text{tế bào}} = \Psi_S$ — đây chính là mẹo đo thế chất tan của dịch bào trong bài thực hành.

## Ranh giới áp dụng

Công thức $-iCRT$ giả thiết dung dịch loãng và lí tưởng. Với dung dịch đặc, $i$ thực tế nhỏ hơn giá trị lí thuyết do các ion hút nhau; kết quả tính sẽ âm hơn thực tế.

**Lỗi thường gặp:**
- Quên hệ số $i$ khi chất tan phân li — sai vì thế thẩm thấu phụ thuộc số **tiểu phân** chứ không phải số phân tử; dùng NaCl mà lấy $i=1$ sẽ cho kết quả chỉ bằng một nửa giá trị đúng.
- So sánh hai số âm và chọn nhầm chiều: nghĩ $-0{,}75$ 'lớn hơn' $-0{,}45$ — sai, giá trị càng âm thì thế nước càng thấp, nước chảy về phía âm hơn.
- Dùng nhiệt độ Celsius trong công thức $-iCRT$ — sai vì $R$ được định nghĩa theo thang Kelvin; ở 27 °C mà thay $T=27$ sẽ cho kết quả nhỏ hơn giá trị đúng hơn 11 lần.

<sub>`lesson.biology.cau-truc-te-bao.tham-thau-va-the-nuoc`</sub>

---

## Unit 3: Cellular Energetics (Năng lượng học tế bào)

### 1. Enzyme và động học enzyme: mô hình Michaelis - Menten
*Enzymes and enzyme kinetics: the Michaelis-Menten model* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được cơ chế hạ năng lượng hoạt hoá của enzyme theo mô hình khớp cảm ứng
- Phân tích được ý nghĩa của $V_{max}$ và $K_m$ từ đồ thị tốc độ theo nồng độ cơ chất
- Vận dụng được hệ số nhiệt $Q_{10}$ để đánh giá ảnh hưởng của nhiệt độ tới tốc độ phản ứng

## Enzyme làm gì và không làm gì

Enzyme là chất xúc tác sinh học **hạ năng lượng hoạt hoá** $E_a$ của phản ứng. Điều quan trọng không kém là những gì enzyme **không** làm: nó không cung cấp năng lượng, không làm phản ứng thu năng lượng trở thành tự phát, không làm thay đổi $\Delta G$ hay vị trí cân bằng — chỉ giúp cân bằng đó đạt tới nhanh hơn.

Cơ chế: tâm hoạt động gắn cơ chất, thay đổi hình dạng ôm lấy nó (**khớp cảm ứng**), làm căng và yếu đi liên kết cần cắt, đồng thời định hướng các nhóm phản ứng lại gần nhau đúng góc độ.

## Đường cong bão hoà

Vẽ tốc độ ban đầu $v_0$ theo nồng độ cơ chất $[S]$ ta được đường cong tăng rồi phẳng dần:

$$v_0 = \frac{V_{max}[S]}{K_m + [S]}$$

Đọc đồ thị theo hai vùng:

- $[S]$ thấp: hầu hết tâm hoạt động trống, thêm cơ chất là thêm va chạm → $v_0$ gần tỉ lệ thuận với $[S]$. Yếu tố giới hạn là **nồng độ cơ chất**.
- $[S]$ cao: mọi tâm hoạt động đều bận, thêm cơ chất vô ích → $v_0 \to V_{max}$. Yếu tố giới hạn là **số phân tử enzyme**.

Thay $[S] = K_m$ vào công thức cho $v_0 = V_{max}/2$ — đó là cách đọc $K_m$ trực tiếp từ đồ thị.

## Nhiệt độ: hai xu hướng đối nghịch

Tăng nhiệt độ vừa tăng động năng (tăng tần suất va chạm hiệu quả) vừa tăng nguy cơ biến tính. Kết quả là đường cong có **đỉnh** ở nhiệt độ tối ưu. Trước đỉnh, quy tắc thực nghiệm $Q_{10} = \dfrac{v_{T+10}}{v_T} \approx 2$ thường đúng. Sau đỉnh tốc độ giảm rất dốc vì biến tính là quá trình gần như không thuận nghịch.

## Lưu ý khi đo

Luôn đo **tốc độ ban đầu** (độ dốc tiếp tuyến tại $t=0$) chứ không lấy tốc độ trung bình cả thí nghiệm, vì càng về sau cơ chất càng cạn và sản phẩm tích tụ, làm tốc độ giảm vì lí do không liên quan tới biến số đang khảo sát.

**Lỗi thường gặp:**
- Nói enzyme 'cung cấp năng lượng cho phản ứng' — sai, vì enzyme chỉ hạ rào cản $E_a$; một phản ứng có $\Delta G > 0$ vẫn không tự xảy ra dù có bao nhiêu enzyme, nó phải được ghép cặp với thuỷ phân ATP.
- Cho rằng $K_m$ lớn nghĩa là enzyme mạnh — sai, $K_m$ lớn nghĩa là cần nhiều cơ chất mới đạt nửa tốc độ, tức **ái lực thấp**; đại lượng đo sức mạnh xúc tác là $V_{max}$ (hay $k_{cat}$).
- Giải thích đoạn phẳng của đồ thị bằng 'enzyme đã biến tính' — sai, ở đoạn bão hoà enzyme vẫn nguyên vẹn và vẫn làm việc hết công suất; nguyên nhân là mọi tâm hoạt động đều đã bị chiếm.

<sub>`lesson.biology.nang-luong-te-bao.enzyme-va-dong-hoc-enzyme`</sub>

---

### 2. Ức chế enzyme cạnh tranh, không cạnh tranh và điều hoà dị lập thể
*Competitive, non-competitive inhibition and allosteric regulation* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Phân biệt được ức chế cạnh tranh và không cạnh tranh bằng tiêu chí đồ thị $V_{max}$ và $K_m$
- Giải thích được cơ chế điều hoà dị lập thể và ức chế ngược trong con đường chuyển hoá
- Vận dụng được công thức phần trăm ức chế để xử lí số liệu thực nghiệm

## Hai kiểu ức chế, một câu hỏi phân biệt

Câu hỏi duy nhất cần đặt ra là: **tăng thật nhiều cơ chất có cứu được không?**

- Có → **ức chế cạnh tranh**. Chất ức chế và cơ chất tranh nhau cùng một chỗ; đông cơ chất thì cơ chất thắng. Đồ thị: $V_{max}$ giữ nguyên (chỉ đạt tới ở $[S]$ cao hơn), $K_m$ biểu kiến **tăng**.
- Không → **ức chế không cạnh tranh**. Chất ức chế bám chỗ khác và bẻ méo tâm hoạt động; cơ chất có nhiều đến đâu cũng không gỡ được. Đồ thị: $V_{max}$ **giảm**, $K_m$ không đổi.

Mẹo đọc đồ thị nhanh trong đề AP và A-Level: nhìn đường tiệm cận ngang. Nếu hai đường cong cùng tiến tới một trần thì đó là cạnh tranh; nếu trần bị hạ xuống thì đó là không cạnh tranh.

## Ứng dụng y học

- Ethanol là chất ức chế cạnh tranh của alcohol dehydrogenase đối với methanol; truyền ethanol là cách cấp cứu ngộ độc methanol vì nó chiếm chỗ, ngăn methanol bị chuyển thành formaldehyde độc.
- Ion kim loại nặng ($\text{Hg}^{2+}$, $\text{Pb}^{2+}$) gắn nhóm -SH ở vị trí xa tâm hoạt động → ức chế không cạnh tranh, thường không thuận nghịch.

## Điều hoà dị lập thể và ức chế ngược

Enzyme dị lập thể có thêm một **vị trí điều hoà**. Chất gắn vào đó chuyển enzyme giữa dạng hoạt động và dạng bất hoạt. Cơ chế này cho phép **ức chế ngược**: trong con đường tổng hợp isoleucine từ threonine gồm 5 bước, isoleucine dư gắn ngược vào enzyme bước 1 (threonine deaminase) và tắt nó.

Vì sao lại tắt bước **đầu tiên** chứ không tắt bước cuối? Vì tắt bước đầu ngăn toàn bộ dòng nguyên liệu đi vào con đường, tránh tích tụ các chất trung gian vô dụng. Đây là ví dụ mẫu mực của phản hồi âm ở cấp phân tử.

**Lỗi thường gặp:**
- Kết luận kiểu ức chế chỉ từ một điểm đo ở nồng độ cơ chất thấp — sai, vì ở vùng đó cả hai kiểu đều làm giảm tốc độ; chỉ vùng bão hoà mới phân biệt được do nó phản ánh $V_{max}$.
- Nói ức chế cạnh tranh 'không ảnh hưởng tốc độ phản ứng' — sai; nó vẫn làm giảm tốc độ ở mọi nồng độ cơ chất hữu hạn, chỉ là ảnh hưởng đó tiến về 0 khi cơ chất tiến tới vô hạn.
- Cho rằng ức chế ngược tác động lên enzyme của bước cuối cùng — sai, sản phẩm cuối ức chế enzyme bước **đầu tiên**; nếu tắt bước cuối thì các chất trung gian vẫn được tạo ra và tích tụ vô ích.

<sub>`lesson.biology.nang-luong-te-bao.uc-che-enzyme`</sub>

---

### 3. Năng lượng tự do Gibbs trong hệ sinh học và vai trò của ATP
*Gibbs free energy in biological systems and the role of ATP* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được phản ứng toả năng lượng hay thu năng lượng từ dấu của $\Delta G$
- Giải thích được vì sao sự sống không vi phạm định luật hai nhiệt động lực học
- Phân tích được cơ chế ghép cặp năng lượng qua ATP trong tế bào

## Câu hỏi khó của nhiệt động lực học

Định luật hai nói entropy của vũ trụ luôn tăng. Vậy làm sao một hạt giống lại tự tổ chức thành cây với trật tự cực cao? Câu trả lời: tế bào là **hệ mở**. Nó giảm entropy cục bộ bằng cách xuất khẩu entropy ra môi trường dưới dạng nhiệt và các phân tử nhỏ ($\text{CO}_2$, $\text{H}_2\text{O}$). Tổng entropy vũ trụ vẫn tăng.

## Dấu của $\Delta G$

$$\Delta G = \Delta H - T\Delta S$$

- $\Delta G < 0$: **toả năng lượng** (exergonic), tự phát. Ví dụ: hô hấp tế bào, thuỷ phân ATP.
- $\Delta G > 0$: **thu năng lượng** (endergonic), không tự phát. Ví dụ: quang hợp, tổng hợp protein, vận chuyển chủ động.
- $\Delta G = 0$: hệ ở trạng thái cân bằng — với tế bào sống, đó là trạng thái **chết**, vì không còn khả năng sinh công.

Điểm dễ hiểu nhầm nhất: '$\Delta G < 0$, tự phát' **không** đồng nghĩa với 'xảy ra nhanh'. Glucose trong không khí có $\Delta G$ rất âm nhưng vẫn bền hàng năm vì $E_a$ cao. Nhiệt động lực học nói về **chiều**, động học nói về **tốc độ**.

## ATP: đồng tiền năng lượng

ATP gồm adenine + ribose + ba nhóm phosphate. Ba nhóm phosphate cạnh nhau đều mang điện âm nên đẩy nhau mạnh; thuỷ phân liên kết cuối giải toả sức đẩy đó:

$$\text{ATP} + \text{H}_2\text{O} \rightarrow \text{ADP} + \text{P}_i, \qquad \Delta G^{\circ\prime} \approx -30{,}5\ \text{kJ/mol}$$

## Ghép cặp

Tổng hợp glutamine từ glutamate và $\text{NH}_3$ có $\Delta G = +14{,}2$ kJ/mol — không tự phát. Ghép với thuỷ phân ATP:

$$+14{,}2 + (-30{,}5) = -16{,}3\ \text{kJ/mol} < 0$$

nên cặp phản ứng trở nên tự phát. Cơ chế thực tế là **phosphoryl hoá**: nhóm phosphate được chuyển sang cơ chất, tạo chất trung gian giàu năng lượng, chứ không phải 'nhiệt từ ATP đẩy phản ứng'.

ATP được chọn làm đồng tiền chung vì nó ở mức năng lượng **trung gian**: đủ cao để thúc đẩy hầu hết phản ứng thu năng lượng, đủ thấp để được tái tạo nhanh từ hô hấp. Một tế bào cơ chỉ giữ đủ ATP cho vài giây hoạt động mạnh và quay vòng hết kho ATP của nó trong khoảng một phút; tính trên cả cơ thể, mỗi phân tử ATP được tái tạo hàng trăm lần mỗi ngày.

**Lỗi thường gặp:**
- Đồng nhất '$\Delta G$ âm' với 'phản ứng xảy ra nhanh' — sai, vì $\Delta G$ chỉ cho biết chiều tự phát; tốc độ do năng lượng hoạt hoá và enzyme quyết định.
- Nói ATP là 'phân tử dự trữ năng lượng dài hạn của tế bào' — sai, ATP là đồng tiền lưu thông tồn tại vài giây; dự trữ dài hạn là glycogen và mỡ, vốn có mật độ năng lượng cao hơn nhiều lần.
- Cho rằng sinh vật vi phạm định luật hai vì tự tổ chức — sai, vì định luật hai áp dụng cho hệ cô lập; sinh vật là hệ mở, giảm entropy bên trong nhờ tăng entropy môi trường nhiều hơn.

<sub>`lesson.biology.nang-luong-te-bao.nang-luong-tu-do-gibbs-va-atp`</sub>

---

### 4. Hô hấp tế bào: các giai đoạn và cân bằng ATP
*Cellular respiration: stages and ATP balance* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Mô tả được vị trí, nguyên liệu và sản phẩm của bốn giai đoạn hô hấp hiếu khí
- Tính được tổng ATP thu được từ một phân tử glucose và giải thích vì sao con số này dao động
- Vận dụng được hệ số hô hấp RQ để xác định loại cơ chất đang bị oxi hoá

## Bức tranh tổng thể

$$\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2 \rightarrow 6\text{CO}_2 + 6\text{H}_2\text{O} + \text{năng lượng}$$

Điều dễ bỏ sót: tế bào **không** đốt glucose một lần. Nó tháo dỡ từng bước, mỗi bước lấy ra một lượng nhỏ năng lượng dưới dạng electron mang năng lượng cao chuyển cho NAD⁺ và FAD.

## Bốn giai đoạn

| Giai đoạn | Vị trí | Vào | Ra (mỗi glucose) |
|---|---|---|---|
| Đường phân | Bào tương | 1 glucose | 2 pyruvate, **2 ATP**, 2 NADH |
| Oxi hoá pyruvate | Chất nền ti thể | 2 pyruvate | 2 acetyl-CoA, 2 CO₂, 2 NADH |
| Chu trình Krebs | Chất nền ti thể | 2 acetyl-CoA | 4 CO₂, **2 ATP**, 6 NADH, 2 FADH₂ |
| Chuỗi vận chuyển electron | Màng trong ti thể | 10 NADH, 2 FADH₂, 6 O₂ | ~26-28 ATP, 12 H₂O |

Toàn bộ CO₂ thải ra đến từ oxi hoá pyruvate và chu trình Krebs, **không** từ đường phân. Toàn bộ O₂ tiêu thụ chỉ dùng ở bước cuối cùng, làm chất nhận electron cuối cùng.

## Vì sao con số ATP không cố định

Sách cũ ghi 38 ATP, sách hiện đại ghi 30-32. Ba lí do:

1. Tỉ lệ H⁺ trên ATP không phải số nguyên: cần khoảng 4 H⁺ cho mỗi ATP, nên 1 NADH cho ~2,5 ATP và 1 FADH₂ cho ~1,5 ATP.
2. NADH tạo ở bào tương phải được 'chuyển tiếp' vào ti thể; con thoi glycerol phosphate làm mất năng lượng (chuyển thành FADH₂) còn con thoi malate-aspartate thì không.
3. Gradient H⁺ còn bị dùng cho việc khác (nhập phosphate, sinh nhiệt), không dành trọn cho ATP synthase.

## Khi thiếu oxygen

Không có O₂ thì NADH không được tái oxi hoá, NAD⁺ cạn và đường phân dừng. Lên men giải quyết đúng vấn đề đó: nó **không tạo thêm ATP** mà chỉ tái tạo NAD⁺ để đường phân tiếp tục cho 2 ATP mỗi glucose. Ở người tạo lactate, ở nấm men tạo ethanol và CO₂.

**Lỗi thường gặp:**
- Cho rằng CO₂ được thải ra trong đường phân — sai, đường phân không giải phóng CO₂ nào; carbon chỉ rời phân tử ở bước oxi hoá pyruvate và trong chu trình Krebs.
- Nói lên men 'tạo ATP trong điều kiện thiếu oxygen' — sai một nửa: ATP vẫn do đường phân tạo ra; vai trò riêng của lên men chỉ là tái tạo NAD⁺ để đường phân không bị tắc.
- Coi 38 ATP là con số chính xác phải học thuộc — sai, vì tỉ lệ H⁺/ATP không phải số nguyên và một phần gradient bị dùng cho việc khác; giá trị hiện đại là 30-32 ATP và cần nói rõ đây là ước lượng.

<sub>`lesson.biology.nang-luong-te-bao.ho-hap-te-bao-cac-giai-doan`</sub>

---

### 5. Chuỗi vận chuyển electron và thuyết hoá thẩm
*The electron transport chain and chemiosmotic theory* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được cách năng lượng của electron được chuyển thành gradient proton
- Chứng minh được vai trò của gradient H⁺ bằng thí nghiệm với chất tách cặp
- Phân tích được điểm chung giữa hoá thẩm ở ti thể và ở lục lạp

## Vấn đề cần giải

Sau chu trình Krebs, tế bào đang cầm 10 NADH và 2 FADH₂ — tức là các electron ở mức năng lượng cao — nhưng chỉ mới thu được 4 ATP. Toàn bộ phần còn lại nằm ở bước này.

## Electron rơi từng bậc

Màng trong ti thể chứa bốn phức hệ protein. NADH nhường electron cho phức hệ I, FADH₂ nhường cho phức hệ II. Electron đi qua chuỗi các chất mang có **thế oxi hoá - khử tăng dần**, cuối cùng được O₂ nhận:

$$\tfrac{1}{2}\text{O}_2 + 2\text{H}^+ + 2e^- \rightarrow \text{H}_2\text{O}$$

Mỗi lần chuyển bậc, một ít năng lượng được giải phóng. Nếu rơi một lần từ NADH thẳng xuống O₂ ($\Delta G \approx -220$ kJ/mol) thì toàn bộ sẽ hoá nhiệt. Chia thành nhiều bậc nhỏ cho phép **thu hồi** năng lượng ở từng bậc.

## Năng lượng đó dùng làm gì

Phức hệ I, III, IV dùng năng lượng để **bơm H⁺** từ chất nền ra khoang gian màng. Khoang gian màng trở nên acid hơn và dương điện hơn. Đây là điểm cách mạng trong thuyết Mitchell: năng lượng không được lưu ở một 'liên kết cao năng' bí ẩn nào, mà lưu ở **chênh lệch nồng độ qua màng** — tức là một dạng thế năng vị trí.

## ATP synthase: động cơ quay

H⁺ chảy ngược vào chất nền qua kênh của ATP synthase, làm phần rotor quay. Chuyển động quay đó bẻ hình dạng ba tiểu đơn vị xúc tác, mỗi vòng quay tổng hợp 3 ATP. Vì cần khoảng 4 H⁺ cho mỗi ATP nên 1 NADH (bơm ~10 H⁺) cho ~2,5 ATP, còn 1 FADH₂ (vào ở phức hệ II, chỉ bơm ~6 H⁺) cho ~1,5 ATP.

## Bằng chứng quyết định

Thêm DNP — chất làm màng thấm H⁺ — vào ti thể đang hoạt động: tiêu thụ O₂ **tăng vọt** nhưng tổng hợp ATP **dừng**, và ti thể toả nhiệt mạnh. Nếu ATP được tạo trực tiếp từ dòng electron thì hai đại lượng phải cùng tăng; kết quả thực tế chứng minh gradient H⁺ là mắt xích bắt buộc. Cơ thể người dùng chính nguyên lí này ở mô mỡ nâu để sinh nhiệt cho trẻ sơ sinh.

**Lỗi thường gặp:**
- Nói ATP synthase 'nhận electron để tạo ATP' — sai, ATP synthase không tham gia vận chuyển electron; nó chỉ là một tuabin được quay bởi dòng H⁺.
- Cho rằng O₂ 'cung cấp năng lượng' cho hô hấp — sai, O₂ chỉ là chất nhận electron cuối cùng; vai trò của nó là giữ cho chuỗi không bị ứ, năng lượng đến từ các electron của glucose.
- Kết luận rằng chất tách cặp làm hô hấp ngừng lại — sai, ngược lại hô hấp tăng tốc vì gradient không bao giờ đạt trạng thái đối áp; cái bị mất là sự ghép cặp giữa hô hấp và tổng hợp ATP.

<sub>`lesson.biology.nang-luong-te-bao.chuoi-van-chuyen-electron-va-hoa-tham`</sub>

---

### 6. Quang hợp pha sáng: sắc tố, quang hệ và quang phân li nước
*Light-dependent reactions: pigments, photosystems and photolysis* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao lá cây có màu lục dựa trên phổ hấp thụ của sắc tố
- Mô tả được dòng electron không vòng từ nước tới NADPH và sản phẩm của pha sáng
- Vận dụng được kĩ thuật sắc kí giấy và giá trị Rf để nhận diện sắc tố quang hợp

## Vì sao lá có màu lục

Diệp lục a và b hấp thụ mạnh ánh sáng đỏ (~660 nm) và xanh tím (~430 nm), nhưng **phản xạ** ánh sáng lục. Màu ta thấy là màu bị loại bỏ, không phải màu được dùng. Đồ thị **phổ tác dụng** (tốc độ quang hợp theo bước sóng) trùng khớp gần như hoàn toàn với **phổ hấp thụ** của diệp lục — đây là bằng chứng kinh điển (thí nghiệm Engelmann với tảo sợi và vi khuẩn hiếu khí) rằng diệp lục là sắc tố thực hiện quang hợp.

Các sắc tố phụ (carotene, xanthophyll) hấp thụ ở vùng diệp lục hấp thụ kém và truyền năng lượng về, đồng thời bảo vệ diệp lục khỏi oxi hoá quang.

## Dòng electron không vòng

Diễn ra trên màng thylakoid theo sơ đồ chữ Z:

$$\text{H}_2\text{O} \rightarrow \text{PSII} \rightarrow \text{chuỗi vận chuyển e}^- \rightarrow \text{PSI} \rightarrow \text{NADP}^+$$

1. Ánh sáng kích thích P680; electron bật lên chất nhận sơ cấp. P680⁺ nay là chất oxi hoá mạnh nhất trong sinh học — đủ mạnh để giật electron từ nước, gây **quang phân li nước** và thải O₂.
2. Electron đi qua chuỗi chất mang; năng lượng dùng bơm H⁺ vào **xoang thylakoid**.
3. Tại PSI, ánh sáng nâng electron lên lần nữa để khử NADP⁺ thành NADPH.
4. H⁺ chảy ngược qua ATP synthase ra chất nền → ATP. Đây chính là hoá thẩm, giống hệt ti thể nhưng khác về nguồn electron và hướng bơm.

**Sản phẩm pha sáng: ATP, NADPH và O₂.** Toàn bộ O₂ khí quyển đến từ nước, không phải từ CO₂ — bằng chứng là thí nghiệm đánh dấu đồng vị $^{18}\text{O}$ của Ruben và Kamen.

## Dòng vòng

Khi tế bào cần ATP nhiều hơn NADPH, electron từ PSI có thể quay lại chuỗi vận chuyển thay vì đến NADP⁺: chỉ tạo ATP, không tạo NADPH, không thải O₂. Đây là van điều chỉnh tỉ lệ ATP:NADPH cho phù hợp nhu cầu của chu trình Calvin.

**Lỗi thường gặp:**
- Nói O₂ thải ra trong quang hợp đến từ CO₂ — sai, thí nghiệm đánh dấu $^{18}\text{O}$ chứng minh oxygen đến từ nước bị quang phân li ở PSII.
- Cho rằng ánh sáng lục hoàn toàn không được dùng nên cây trồng dưới đèn lục sẽ chết ngay — sai một phần: diệp lục vẫn hấp thụ một tỉ lệ nhỏ ánh sáng lục, quang hợp chỉ giảm mạnh chứ không bằng 0.
- Dùng chiều dài tờ giấy làm mẫu số khi tính Rf — sai, mẫu số phải là quãng đường **dung môi** chạy được, nếu không giá trị Rf sẽ không còn là hằng số đặc trưng của sắc tố.

<sub>`lesson.biology.nang-luong-te-bao.quang-hop-pha-sang`</sub>

---

### 7. Chu trình Calvin, quang hô hấp và so sánh C3 - C4 - CAM
*The Calvin cycle, photorespiration and C3-C4-CAM comparison* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Mô tả được ba giai đoạn của chu trình Calvin và vai trò của enzyme rubisco
- Giải thích được nguyên nhân quang hô hấp và vì sao nó gây thiệt hại cho cây C3
- So sánh được ba con đường cố định CO₂ theo tiêu chí tách biệt không gian và thời gian

## Pha tối dùng gì của pha sáng

Chu trình Calvin diễn ra trong **chất nền lục lạp** và tiêu thụ đúng hai sản phẩm của pha sáng: ATP và NADPH. Nó không cần ánh sáng trực tiếp, nhưng dừng trong tối vì hết nguyên liệu — nên gọi 'pha tối' dễ gây hiểu nhầm, tên chính xác là **pha không phụ thuộc ánh sáng**.

Ba giai đoạn:

1. **Cố định CO₂**: rubisco gắn CO₂ vào RuBP (5C) → hợp chất 6C không bền → tách thành 2 phân tử 3-phosphoglycerate (3C). Đây là lí do gọi 'thực vật C3'.
2. **Khử**: dùng ATP và NADPH biến 3-PGA thành G3P.
3. **Tái tạo RuBP**: 5 trong 6 G3P quay lại tái tạo RuBP, tốn thêm ATP. Chỉ 1 G3P rời chu trình.

Cần **6 vòng** (6 CO₂) để tạo ra 1 phân tử glucose, tiêu tốn 18 ATP và 12 NADPH.

## Nhược điểm chí mạng của rubisco

Rubisco tiến hoá khi khí quyển giàu CO₂ và nghèo O₂, nên nó không phân biệt tốt hai phân tử này. Khi trời nóng và khô, cây đóng khí khổng để giữ nước; CO₂ trong lá cạn dần còn O₂ (sản phẩm pha sáng) tích tụ. Tỉ lệ $\text{O}_2/\text{CO}_2$ tăng làm rubisco gắn O₂ — **quang hô hấp** — tiêu ATP, nhả CO₂ và không tạo đường. Ở cây C3 vùng nhiệt đới, tổn thất có thể tới 25% năng suất.

## Ba giải pháp tiến hoá

| | C3 | C4 | CAM |
|---|---|---|---|
| Enzyme cố định đầu tiên | Rubisco | PEP carboxylase | PEP carboxylase |
| Tách biệt bằng | Không | **Không gian** (mô giậu / bao bó mạch) | **Thời gian** (đêm / ngày) |
| Khí khổng mở | Ban ngày | Ban ngày | Ban đêm |
| Ví dụ | Lúa, lúa mì, đậu | Ngô, mía, cỏ lồng vực | Xương rồng, dứa, thanh long |

Điểm chung của C4 và CAM: dùng PEP carboxylase — enzyme **không** phản ứng với O₂ và có ái lực CO₂ cao hơn rubisco nhiều lần — để bơm CO₂ tới nơi rubisco làm việc. Cả hai đều tốn thêm ATP, nên C4 chỉ có lợi khi nắng gắt và nóng; ở vùng ôn đới mát mẻ, cây C3 lại hiệu quả hơn.

**Lỗi thường gặp:**
- Gọi chu trình Calvin là 'pha tối' rồi kết luận nó xảy ra vào ban đêm — sai, chu trình chủ yếu chạy ban ngày vì nó phụ thuộc ATP và NADPH do pha sáng cung cấp liên tục.
- Nói cây C4 luôn quang hợp mạnh hơn cây C3 — sai, cơ chế bơm CO₂ tốn thêm ATP nên ở nhiệt độ thấp và ánh sáng vừa phải, cây C3 lại hiệu quả hơn.
- Nhầm quang hô hấp với hô hấp tế bào — sai, quang hô hấp xảy ra trong lục lạp, peroxisome và ti thể dưới ánh sáng, tiêu tốn ATP mà **không** tạo ATP, khác hẳn hô hấp tế bào vốn sinh ATP.

<sub>`lesson.biology.nang-luong-te-bao.chu-trinh-calvin-va-c3-c4-cam`</sub>

---

## Unit 4: Cell Communication and Cell Cycle (Truyền tin và chu kì tế bào)

### 1. Truyền tin tế bào: các loại tín hiệu, thụ thể và cascade khuếch đại
*Cell signalling: signal types, receptors and amplification cascades* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được bốn kiểu truyền tin theo khoảng cách giữa tế bào phát và tế bào đích
- Giải thích được vì sao hormone steroid dùng thụ thể nội bào còn hormone peptide dùng thụ thể màng
- Phân tích được cơ chế khuếch đại tín hiệu trong cascade truyền tin

## Vì sao 30 nghìn tỉ tế bào không hỗn loạn

Cơ thể đa bào chỉ hoạt động được nếu các tế bào biết nhau đang làm gì. Bốn kiểu truyền tin phân theo khoảng cách:

- **Tiếp xúc trực tiếp**: cầu sinh chất ở thực vật, khe nối ở động vật; hoặc tiếp xúc protein bề mặt (nhận diện miễn dịch).
- **Cận tiết (paracrine)**: chất tiết khuếch tán tới tế bào lân cận, ví dụ yếu tố tăng trưởng khi lành vết thương.
- **Synapse**: chất dẫn truyền thần kinh qua khe rất hẹp — nhanh và cực kì chính xác về địa chỉ.
- **Nội tiết (endocrine)**: hormone theo máu đi khắp cơ thể, chậm nhưng tác dụng kéo dài.

## Ba bước bất biến

Mọi con đường truyền tin đều gồm **tiếp nhận → truyền tin → đáp ứng**.

Bước tiếp nhận quyết định loại thụ thể theo tính chất hoá học của tín hiệu:

- Hormone **steroid** (testosterone, estrogen, cortisol) kị nước → qua được lớp lipid kép → thụ thể **nội bào**; phức hợp hormone - thụ thể vào nhân, hoạt động như yếu tố phiên mã → đáp ứng **chậm nhưng lâu dài** vì đi qua tổng hợp protein mới.
- Hormone **peptide** (insulin, glucagon, adrenaline) ưa nước → không qua màng → thụ thể **màng** → đáp ứng **nhanh** vì chỉ cần hoạt hoá enzyme có sẵn.

## Khuếch đại: sức mạnh thật sự

Một phân tử adrenaline gắn thụ thể → hoạt hoá vài chục G-protein → mỗi G-protein hoạt hoá adenylyl cyclase tạo hàng trăm cAMP → mỗi cAMP hoạt hoá protein kinase A → mỗi kinase phosphoryl hoá hàng trăm enzyme đích. Kết quả: **một** phân tử tín hiệu có thể dẫn tới giải phóng **hàng trăm triệu** phân tử glucose từ glycogen.

Đây là lí do hormone có tác dụng ở nồng độ cực thấp ($10^{-9}$ M hoặc thấp hơn) — điều không thể giải thích nếu mỗi phân tử tín hiệu chỉ tác động lên một phân tử đích.

## Một tín hiệu, nhiều đáp ứng

Adrenaline làm gan phân giải glycogen nhưng làm cơ trơn phế quản giãn. Cùng tín hiệu, khác đáp ứng — vì mỗi loại tế bào có tập hợp **protein đích** khác nhau ở cuối con đường. Tín hiệu chỉ là cái công tắc; nội dung nằm ở bộ máy được bật.

**Lỗi thường gặp:**
- Nói hormone 'chỉ tác động lên tế bào đích vì chỉ đến được đó' — sai, hormone nội tiết theo máu đi khắp cơ thể; tính chọn lọc đến từ việc chỉ tế bào đích mới có thụ thể tương ứng.
- Cho rằng chất truyền tin thứ hai chính là phân tử hormone đi vào tế bào — sai, hormone peptide không vào được tế bào; chất truyền tin thứ hai như cAMP được tổng hợp mới ở mặt trong màng.
- Giải thích tác dụng khác nhau của cùng một hormone bằng 'nồng độ khác nhau' — sai, nguyên nhân chính là mỗi loại tế bào có bộ protein đích và bộ thụ thể khác nhau ở cuối con đường truyền tin.

<sub>`lesson.biology.truyen-tin-va-chu-ki-te-bao.truyen-tin-te-bao-va-thu-the`</sub>

---

### 2. Phản hồi âm, phản hồi dương và nội cân bằng
*Negative feedback, positive feedback and homeostasis* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được phản hồi âm và phản hồi dương theo chiều tác động lên kích thích ban đầu
- Xác định được bốn thành phần của một vòng điều khiển nội cân bằng trong ví dụ cụ thể
- Giải thích được vì sao phản hồi dương ít gặp và luôn cần một cơ chế kết thúc

## Bốn thành phần của mọi vòng điều khiển

Mọi hệ nội cân bằng, dù ở tế bào hay ở cơ thể, đều gồm:

1. **Giá trị đặt** (set point) — mức mà hệ hướng tới, ví dụ $37^\circ\text{C}$.
2. **Bộ cảm nhận** — phát hiện sai lệch, ví dụ thụ thể nhiệt ở da và vùng dưới đồi.
3. **Trung tâm điều khiển** — so sánh với giá trị đặt và ra lệnh.
4. **Bộ đáp ứng** — thực thi, ví dụ cơ dựng lông, tuyến mồ hôi, cơ vân run.

Điểm hay bị bỏ sót: nội cân bằng **không** giữ giá trị cố định tuyệt đối mà tạo ra dao động quanh giá trị đặt. Vì phải chờ sai lệch xuất hiện rồi mới sửa, hệ luôn có độ trễ và luôn dao động — đó là lí do thân nhiệt buổi sáng và buổi chiều khác nhau khoảng $0{,}5^\circ\text{C}$.

## Phản hồi âm: quy tắc chung

Điều hoà đường huyết là ví dụ mẫu:

- Đường huyết tăng sau ăn → tế bào $\beta$ đảo tuỵ tiết **insulin** → gan và cơ hấp thu glucose và tổng hợp glycogen → đường huyết giảm → tín hiệu tiết insulin yếu đi.
- Đường huyết giảm khi đói → tế bào $\alpha$ tiết **glucagon** → gan phân giải glycogen → đường huyết tăng.

Hai hormone tác dụng đối lập gọi là **đối vận**, cho phép điều chỉnh hai chiều — chính xác hơn nhiều so với chỉ có một hormone.

## Phản hồi dương: hiếm nhưng cần thiết

- **Cơn co tử cung khi sinh**: đầu thai nhi ép cổ tử cung → tiết oxytocin → co mạnh hơn → ép nhiều hơn → vòng lặp tăng dần. Sự kiện kết thúc: em bé ra đời, kích thích biến mất.
- **Điện thế hoạt động**: Na⁺ vào làm khử cực → mở thêm kênh Na⁺ → vào nhiều hơn. Kết thúc: kênh Na⁺ tự bất hoạt.
- **Đông máu**: thrombin hoạt hoá các yếu tố tạo ra thêm thrombin.

Đặc điểm chung: phản hồi dương **không** duy trì nội cân bằng, nó phá vỡ trạng thái hiện tại để chuyển hệ sang một trạng thái mới thật nhanh, và luôn có cơ chế tự chấm dứt. Nếu thiếu cơ chế đó, vòng lặp trở thành bệnh lí — ví dụ sốt cao ác tính hay sốc nhiễm khuẩn.

**Lỗi thường gặp:**
- Gọi mọi cơ chế 'làm tăng một đại lượng' là phản hồi dương — sai, tiêu chí không phải là chiều tăng hay giảm của đại lượng mà là đáp ứng có làm **mạnh thêm kích thích ban đầu** hay không; glucagon làm tăng đường huyết nhưng vẫn là phản hồi âm vì nó triệt tiêu kích thích 'đường huyết thấp'.
- Nói nội cân bằng nghĩa là giữ giá trị hoàn toàn không đổi — sai, vì hệ chỉ phản ứng sau khi phát hiện sai lệch nên luôn tồn tại dao động quanh giá trị đặt.
- Cho rằng phản hồi dương luôn có hại — sai, nó là cơ chế cần thiết trong sinh con, đông máu và điện thế hoạt động; vấn đề chỉ phát sinh khi thiếu sự kiện chấm dứt vòng lặp.

<sub>`lesson.biology.truyen-tin-va-chu-ki-te-bao.phan-hoi-am-duong-va-noi-can-bang`</sub>

---

### 3. Chu kì tế bào, điểm kiểm soát và nguyên phân
*The cell cycle, checkpoints and mitosis* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Mô tả được các pha của chu kì tế bào và sự kiện đặc trưng của từng kì nguyên phân
- Giải thích được vai trò của ba điểm kiểm soát và hệ cyclin - CDK
- Vận dụng được chỉ số phân bào để ước lượng thời gian các kì

## Chu kì tế bào là gì

Một vòng chu kì gồm **kì trung gian** (G1 - S - G2, chiếm khoảng 90% thời gian) và **pha M** (nguyên phân + phân chia tế bào chất).

- **G1**: tế bào lớn lên, tổng hợp bào quan và protein. Tế bào không phân chia nữa (nơron, tế bào cơ tim) dừng ở trạng thái **G0**.
- **S**: nhân đôi ADN. Sau pha S, mỗi nhiễm sắc thể gồm 2 chromatid chị em dính nhau ở tâm động — số **nhiễm sắc thể không đổi** nhưng lượng ADN tăng gấp đôi.
- **G2**: kiểm tra ADN đã nhân đôi, tổng hợp protein cho thoi phân bào.

## Bốn kì nguyên phân

| Kì | Sự kiện then chốt |
|---|---|
| Đầu | NST co xoắn, màng nhân tiêu biến, thoi phân bào hình thành |
| Giữa | NST kép xếp thành **một hàng** trên mặt phẳng xích đạo |
| Sau | Tâm động tách, hai chromatid chị em tách nhau về hai cực |
| Cuối | NST dãn xoắn, màng nhân tái lập, tế bào chất phân chia |

Kì sau là thời điểm duy nhất số nhiễm sắc thể của tế bào tạm thời tăng gấp đôi (4n ở tế bào 2n), vì mỗi chromatid tách ra trở thành một nhiễm sắc thể độc lập.

## Ba điểm kiểm soát

1. **G1 (điểm hạn định)**: kích thước đủ chưa? có yếu tố tăng trưởng không? ADN có hỏng không? Đây là điểm quyết định quan trọng nhất — qua được là cam kết đi hết chu kì.
2. **G2**: ADN đã nhân đôi xong và không có sai hỏng chưa?
3. **Kì giữa (điểm kiểm soát thoi)**: **mọi** tâm động đã gắn đúng vào thoi từ hai phía chưa? Chỉ cần một nhiễm sắc thể chưa gắn, tín hiệu ức chế vẫn còn và kì sau không được khởi động. Cơ chế này ngăn phân li lệch.

Cyclin tích tụ dần rồi bị phân giải đột ngột ở mỗi lần chuyển pha; chính sự **dao động** này, chứ không phải bản thân CDK, tạo nhịp cho chu kì.

## Vì sao nguyên phân quan trọng

Nguyên phân tạo hai tế bào con có bộ nhiễm sắc thể **giống hệt** tế bào mẹ, là cơ sở của sinh trưởng, thay thế tế bào chết, tái sinh mô và sinh sản vô tính.

**Lỗi thường gặp:**
- Nói pha S làm tăng gấp đôi **số nhiễm sắc thể** — sai, số nhiễm sắc thể không đổi vì hai chromatid chị em vẫn dính chung một tâm động; cái tăng gấp đôi là lượng ADN.
- Kết luận từ chỉ số phân bào cao rằng 'tế bào phân chia nhanh hơn' mà không xét chu kì — sai, chỉ số phân bào đo **tỉ lệ thời gian** dành cho pha M; muốn suy ra tốc độ phân chia phải biết thêm độ dài chu kì.
- Cho rằng điểm kiểm soát thoi kiểm tra ADN có bị hỏng hay không — sai, việc đó do điểm G1 và G2 đảm nhiệm; điểm kiểm soát thoi chỉ kiểm tra mọi tâm động đã gắn đúng vào vi ống từ hai cực chưa.

<sub>`lesson.biology.truyen-tin-va-chu-ki-te-bao.chu-ki-te-bao-diem-kiem-soat-nguyen-phan`</sub>

---

### 4. Ung thư: mất kiểm soát chu kì tế bào
*Cancer: loss of cell cycle control* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Phân biệt được gen tiền ung thư và gen ức chế khối u theo kiểu đột biến gây bệnh
- Giải thích được vì sao ung thư cần tích luỹ nhiều đột biến chứ không phải một
- Phân tích được cơ sở khoa học của một số hướng điều trị và phòng ngừa

## Ung thư là bệnh của chu kì tế bào

Tế bào ung thư khác tế bào thường ở bốn điểm: (1) không tuân theo tín hiệu dừng của điểm kiểm soát; (2) mất **ức chế tiếp xúc** nên chồng chất lên nhau; (3) không cần yếu tố tăng trưởng từ bên ngoài; (4) thoát khỏi chết theo chương trình và trở nên 'bất tử' nhờ tái hoạt hoá telomerase.

## Hai loại gen, hai kiểu hỏng

So sánh dễ nhớ: gen tiền ung thư là **chân ga**, gen ức chế khối u là **chân phanh**.

- Chân ga bị kẹt: chỉ cần một alen đột biến làm protein hoạt động liên tục. Ví dụ Ras đột biến vẫn phát tín hiệu phân chia dù không có yếu tố tăng trưởng.
- Chân phanh bị hỏng: phải hỏng **cả hai** alen mới mất phanh. Đây là lí do người mang một alen BRCA1 hỏng từ khi sinh ra chưa bị bệnh, nhưng nguy cơ cao hơn nhiều vì chỉ còn cần một 'cú đánh' nữa (giả thuyết hai cú đánh của Knudson).

## p53: người gác cổng bộ gen

p53 phát hiện ADN hỏng và có ba lựa chọn: dừng chu kì ở G1 để sửa chữa, kích hoạt bộ máy sửa chữa, hoặc ra lệnh **apoptosis** nếu tổn thương quá nặng. Hơn 50% khối u ở người có đột biến p53 — đủ cho thấy tầm quan trọng của nó.

## Vì sao cần nhiều đột biến

Một đột biến duy nhất hiếm khi đủ, vì các cơ chế bảo vệ chồng lớp lên nhau. Mô hình ung thư đại trực tràng cho thấy trình tự tích luỹ khoảng 4-7 đột biến ở APC, KRAS, p53... trong nhiều năm. Hai hệ quả:

- Tần suất ung thư **tăng vọt theo tuổi**, vì xác suất tích đủ đột biến tăng theo thời gian phơi nhiễm.
- Tác nhân gây đột biến (thuốc lá, tia UV, tia ion hoá, aflatoxin, một số virus như HPV và HBV) làm tăng nguy cơ vì rút ngắn thời gian tích luỹ.

## Cơ sở của điều trị

Hoá trị và xạ trị nhắm vào tế bào **đang phân chia nhanh** — điều này giải thích cả hiệu quả lẫn tác dụng phụ (rụng tóc, loét niêm mạc, giảm bạch cầu), vì nang tóc, niêm mạc ruột và tuỷ xương cũng phân chia nhanh. Liệu pháp trúng đích và liệu pháp miễn dịch ra đời để khắc phục chính hạn chế đó.

**Lỗi thường gặp:**
- Nói 'ung thư di truyền' nghĩa là chắc chắn mắc bệnh — sai, cái di truyền là một alen hỏng làm tăng nguy cơ; vẫn cần thêm đột biến ở alen còn lại và thường thêm nhiều đột biến khác.
- Cho rằng đột biến ở gen ức chế khối u là trội — sai, phải mất chức năng cả hai alen nên ở mức tế bào nó biểu hiện như tính trạng lặn; điều gây nhầm là kiểu di truyền trong gia hệ lại giống trội vì xác suất cú đánh thứ hai rất cao.
- Nghĩ khối u lành tính và ác tính khác nhau ở tốc độ phân chia — sai, tiêu chí phân biệt then chốt là khả năng **xâm lấn mô lân cận và di căn**, chứ không phải riêng tốc độ tăng sinh.

<sub>`lesson.biology.truyen-tin-va-chu-ki-te-bao.ung-thu-va-mat-kiem-soat-chu-ki`</sub>

---

## Unit 5: Heredity (Di truyền học)

### 1. Giảm phân và ba nguồn biến dị di truyền
*Meiosis and three sources of genetic variation* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- So sánh được giảm phân I và giảm phân II về hành vi nhiễm sắc thể
- Chứng minh được ba nguồn biến dị của sinh sản hữu tính bằng tính toán số tổ hợp
- Giải thích được hậu quả của phân li không đều nhiễm sắc thể

## Bài toán của sinh sản hữu tính

Nếu tinh trùng và trứng đều mang bộ 2n thì hợp tử sẽ là 4n, và số nhiễm sắc thể sẽ tăng gấp đôi mỗi thế hệ. Giảm phân giải quyết bằng cách giảm một nửa bộ nhiễm sắc thể — nhưng nó còn làm một việc quan trọng hơn: **tạo biến dị**.

## Hai lần phân bào, hai nhiệm vụ khác nhau

- **Giảm phân I** là lần phân bào **giảm nhiễm**: hai nhiễm sắc thể **tương đồng** tách nhau. Sau GP I, mỗi tế bào con có n nhiễm sắc thể kép ($n$ NST, $2n$ chromatid).
- **Giảm phân II** giống nguyên phân: hai **chromatid chị em** tách nhau, số nhiễm sắc thể không giảm nữa.

Mẹo nhận diện trên tiêu bản: ở kì giữa I các nhiễm sắc thể xếp thành **hai hàng** (từng cặp tương đồng đối diện nhau); ở kì giữa II và kì giữa nguyên phân chúng xếp **một hàng**.

## Ba nguồn biến dị

1. **Phân li độc lập**: mỗi cặp tương đồng xếp ngẫu nhiên một trong hai chiều → $2^{23} \approx 8{,}4$ triệu loại giao tử ở người.
2. **Trao đổi chéo**: mỗi cặp tương đồng trao đổi trung bình 1-3 điểm → gần như mỗi chromatid là duy nhất, làm con số trên tăng lên gần vô hạn.
3. **Thụ tinh ngẫu nhiên**: $8{,}4 \times 10^6 \times 8{,}4 \times 10^6 \approx 7 \times 10^{13}$ tổ hợp hợp tử, chưa kể trao đổi chéo.

Hai nguồn đầu xảy ra ở giảm phân I, nguồn thứ ba ở thụ tinh. Cả ba đều chỉ **sắp xếp lại** alen sẵn có; nguồn tạo alen mới duy nhất là **đột biến**.

## Khi giảm phân sai

Không phân li ở GP I tạo hai loại giao tử: (n+1) và (n−1). Thụ tinh với giao tử bình thường cho hợp tử 2n+1 (thể ba) hoặc 2n−1 (thể một). Hội chứng Down là thể ba nhiễm sắc thể 21; nguy cơ tăng theo tuổi mẹ vì noãn bào bị 'treo' ở kì đầu I từ trước khi sinh, có khi hàng chục năm, khiến các protein cố kết nhiễm sắc thể suy yếu dần.

**Lỗi thường gặp:**
- Nói số nhiễm sắc thể giảm một nửa ở giảm phân II — sai, việc giảm nhiễm hoàn tất ngay ở giảm phân I khi các nhiễm sắc thể tương đồng tách nhau; giảm phân II chỉ tách chromatid nên số nhiễm sắc thể giữ nguyên là n.
- Cho rằng trao đổi chéo tạo ra alen mới — sai, nó chỉ tạo **tổ hợp** alen mới trên cùng một nhiễm sắc thể; alen mới chỉ sinh ra từ đột biến gen.
- Áp dụng công thức $2^n$ cho số cách sắp xếp ở kì giữa I mà không phân biệt với số loại giao tử — sai, số hình ảnh sắp xếp khác nhau là $2^{n-1}$ vì hai cách đối xứng gương cho cùng một hình, trong khi số loại giao tử vẫn là $2^n$.

<sub>`lesson.biology.di-truyen-hoc.giam-phan-va-nguon-bien-di`</sub>

---

### 2. Quy luật Mendel và các mở rộng: trội không hoàn toàn, đa alen, tương tác gen
*Mendelian laws and extensions: incomplete dominance, multiple alleles, gene interaction* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu được quy luật phân li và quy luật phân li độc lập kèm cơ sở tế bào học chính xác
- Vận dụng được quy tắc nhân và quy tắc cộng xác suất thay cho khung Punnett trong bài toán nhiều cặp gen
- Phân tích được các tỉ lệ biến dạng của 9:3:3:1 để nhận ra kiểu tương tác gen

## Vì sao Mendel thành công

Mendel chọn đậu Hà Lan (tự thụ phấn, dễ lai có kiểm soát), chọn **bảy tính trạng tương phản rõ ràng**, và quan trọng nhất là **đếm số lượng lớn rồi xử lí bằng toán học** — điều các nhà lai giống trước ông không làm. May mắn cho ông: bảy tính trạng đó nằm trên các nhiễm sắc thể khác nhau hoặc quá xa nhau nên đều phân li độc lập.

## Hai quy luật và cơ sở tế bào học

- **Phân li**: cặp alen tách nhau khi tạo giao tử ⟸ cặp nhiễm sắc thể tương đồng tách ở kì sau I.
- **Phân li độc lập**: các cặp alen khác nhau phân li độc lập ⟸ các cặp tương đồng xếp ngẫu nhiên ở kì giữa I.

Quy luật thứ hai chỉ đúng khi các gen nằm trên **các cặp nhiễm sắc thể khác nhau** (hoặc rất xa nhau trên cùng một nhiễm sắc thể). Đây là giới hạn quan trọng, dẫn tới bài học về liên kết gen.

## Dùng xác suất thay vì khung Punnett

Khung Punnett cho phép lai 4 cặp gen dị hợp có $16 \times 16 = 256$ ô — không khả thi. Thay bằng hai quy tắc:

- **Quy tắc nhân** (biến cố độc lập, 'và'): $P(A \cap B) = P(A) \times P(B)$.
- **Quy tắc cộng** (biến cố xung khắc, 'hoặc'): $P(A \cup B) = P(A) + P(B)$.

Tách bài toán nhiều cặp gen thành tích các bài toán một cặp gen là kĩ năng cốt lõi của cả AP và A-Level.

## Bốn mở rộng cần nắm

1. **Trội không hoàn toàn**: hoa mõm chó đỏ × trắng → hồng; F2 cho 1 đỏ : 2 hồng : 1 trắng.
2. **Đồng trội**: nhóm máu AB biểu hiện **cả hai** kháng nguyên — khác trung gian ở chỗ hai sản phẩm cùng xuất hiện đầy đủ.
3. **Đa alen**: hệ ABO có ba alen $I^A, I^B, i$ trong quần thể, nhưng mỗi cá thể vẫn chỉ mang hai.
4. **Tương tác gen**: hai gen cùng chi phối một tính trạng. Nhận diện qua tổng các số hạng tỉ lệ luôn bằng 16: 9:7 và 9:6:1 (bổ sung), 12:3:1 và 13:3 (át trội), 9:3:4 (át lặn), 15:1 (cộng gộp).

Dấu hiệu chung để nhận ra tương tác gen: phép lai **một** tính trạng mà F2 lại cho tỉ lệ có tổng 16 phần.

**Lỗi thường gặp:**
- Quên hệ số tổ hợp khi bài hỏi 'đúng k trong n tính trạng' — sai, vì có $\binom{n}{k}$ cách chọn tính trạng nào rơi vào nhóm nào, và các cách này xung khắc nên phải cộng lại.
- Nhầm trội không hoàn toàn với đồng trội — sai; trội không hoàn toàn cho kiểu hình **trung gian** mới (đỏ × trắng ra hồng), còn đồng trội biểu hiện **đồng thời cả hai** kiểu hình bố mẹ (nhóm máu AB có cả kháng nguyên A và B).
- Áp dụng quy luật phân li độc lập cho hai gen nằm gần nhau trên cùng một nhiễm sắc thể — sai, vì cơ sở tế bào học của quy luật là sự sắp xếp độc lập của các **cặp nhiễm sắc thể**; gen cùng nhiễm sắc thể sẽ liên kết và cho tỉ lệ lệch hẳn.

<sub>`lesson.biology.di-truyen-hoc.quy-luat-mendel-va-mo-rong`</sub>

---

### 3. Liên kết gen, hoán vị gen và bản đồ di truyền
*Gene linkage, recombination and genetic mapping* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao gen liên kết cho tỉ lệ phân li khác dự đoán của Mendel
- Tính được tần số hoán vị gen từ kết quả phép lai phân tích
- Vận dụng được tần số hoán vị để dựng bản đồ di truyền ba gen

## Khi Mendel không còn đúng

Bateson và Punnett lai đậu thơm hai cặp tính trạng nhưng F2 không cho 9:3:3:1 mà lệch hẳn về phía tổ hợp giống bố mẹ. Morgan giải thích trên ruồi giấm: các gen đó **nằm trên cùng một nhiễm sắc thể** nên đi cùng nhau.

## Ba trường hợp và ba tỉ lệ giao tử

Xét cơ thể dị hợp hai cặp gen:

- **Phân li độc lập**: 4 loại giao tử, mỗi loại 25%.
- **Liên kết hoàn toàn**: chỉ 2 loại giao tử liên kết, mỗi loại 50%; không có giao tử tái tổ hợp.
- **Hoán vị gen với tần số $f$**: 2 loại giao tử liên kết mỗi loại $\dfrac{1-f}{2}$, và 2 loại tái tổ hợp mỗi loại $\dfrac{f}{2}$.

Vì trao đổi chéo chỉ xảy ra giữa **hai trong bốn** chromatid, ngay cả khi mọi tế bào đều trao đổi chéo thì tối đa cũng chỉ 50% giao tử là tái tổ hợp. Do đó $f \le 50\%$; khi $f = 50\%$ ta không phân biệt được với phân li độc lập.

## Đo tần số hoán vị

Phương pháp chuẩn là **lai phân tích**: lai cá thể dị hợp với cá thể đồng hợp lặn. Khi đó kiểu hình đời con phản ánh trực tiếp loại giao tử của cơ thể dị hợp.

$$f = \frac{\text{số cá thể tái tổ hợp}}{\text{tổng số cá thể}} \times 100\%$$

Hai kiểu hình chiếm tỉ lệ **nhỏ** là tái tổ hợp; hai kiểu hình chiếm tỉ lệ lớn phản ánh kiểu gen liên kết của bố mẹ (cho biết là kiểu **đồng** hay **đối**).

## Dựng bản đồ

Sturtevant nhận ra: nếu trao đổi chéo xảy ra ngẫu nhiên theo chiều dài nhiễm sắc thể thì hai gen càng xa nhau càng dễ bị tách, nên $f$ tỉ lệ với khoảng cách. Quy ước $1\% = 1$ cM. Với ba gen, khoảng cách gần như cộng tính: $d_{AC} \approx d_{AB} + d_{BC}$.

**Giới hạn**: với khoảng cách lớn ($f > 20\%$), trao đổi chéo kép làm hai gen 'trở về' vị trí ban đầu, khiến $f$ đo được **thấp hơn** khoảng cách thật. Vì vậy bản đồ chính xác phải được dựng từ nhiều cặp gen gần nhau rồi cộng dồn, chứ không đo trực tiếp hai gen ở hai đầu.

**Lỗi thường gặp:**
- Tính tần số hoán vị bằng cách lấy nhóm kiểu hình lớn chia tổng — sai, tần số hoán vị phải tính từ nhóm **tái tổ hợp** tức nhóm có số lượng nhỏ, vì trao đổi chéo là sự kiện ít xảy ra.
- Cho rằng tần số hoán vị có thể vượt 50% khi hai gen rất xa nhau — sai, vì mỗi lần trao đổi chéo chỉ liên quan 2 trong 4 chromatid nên tỉ lệ tái tổ hợp bị chặn trên ở 50%, và khi đạt 50% thì kết quả không phân biệt được với phân li độc lập.
- Dùng tần số hoán vị đo giữa hai gen ở hai đầu nhiễm sắc thể làm khoảng cách chính xác — sai, trao đổi chéo kép khôi phục tổ hợp bố mẹ nên khoảng cách đo được bị đánh giá thấp; phải cộng dồn nhiều khoảng ngắn.

<sub>`lesson.biology.di-truyen-hoc.lien-ket-gen-hoan-vi-va-ban-do-gen`</sub>

---

### 4. Di truyền liên kết giới tính và phân tích phả hệ
*Sex-linked inheritance and pedigree analysis* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao bệnh lặn liên kết X gặp ở nam nhiều hơn nữ
- Phân tích được phả hệ để xác định kiểu di truyền của một tính trạng
- Vận dụng được xác suất để dự đoán nguy cơ ở đời con

## Vì sao giới tính lại làm thay đổi kết quả lai

Morgan lai ruồi giấm mắt đỏ với mắt trắng và nhận thấy kết quả **khác nhau khi đảo vai trò bố mẹ** — điều không thể xảy ra với gen trên nhiễm sắc thể thường. Kết luận: gen quy định màu mắt nằm trên nhiễm sắc thể X.

## Ba cấu hình gen liên quan giới tính

- **Vùng không tương đồng của X**: nữ XX có hai alen, nam XY chỉ có một (bán hợp tử). Ví dụ: mù màu, máu khó đông (hemophilia A), loạn dưỡng cơ Duchenne.
- **Vùng không tương đồng của Y**: chỉ truyền từ bố sang **tất cả** con trai, không bao giờ sang con gái (di truyền thẳng). Ví dụ: gen SRY quyết định giới tính nam, các gen vùng AZF cần cho sinh tinh (mất đoạn AZF gây vô sinh nam và chỉ truyền theo dòng bố).
- **Vùng tương đồng của X và Y**: di truyền như gen trên nhiễm sắc thể thường.

## Vì sao nam mắc bệnh lặn liên kết X nhiều hơn nữ

Gọi tần số alen bệnh là $q$. Nam chỉ cần **một** alen bệnh nên tỉ lệ mắc là $q$. Nữ cần **hai** alen nên tỉ lệ mắc là $q^2$. Với mù màu $q \approx 0{,}08$: nam khoảng 8%, nữ khoảng $0{,}64\%$ — chênh nhau 12,5 lần. Tỉ số này chính là $1/q$, nên bệnh càng hiếm thì chênh lệch nam - nữ càng lớn.

## Đọc phả hệ theo bốn câu hỏi

1. Bố mẹ bình thường sinh con bệnh? → tính trạng **lặn** (bệnh 'ẩn' trong dị hợp).
2. Bố mẹ bệnh sinh con bình thường? → tính trạng **trội**.
3. Với tính trạng lặn: có con **gái** bị bệnh mà bố **không** bệnh? → **không** phải liên kết X (vì con gái bệnh phải nhận alen bệnh từ cả bố lẫn mẹ). Nếu không mâu thuẫn, ưu tiên giả thiết liên kết X khi nam mắc nhiều hơn hẳn.
4. Với tính trạng trội: có con **trai** bệnh mà mẹ bình thường? → không phải liên kết X.

Mẹo bổ sung: nếu tính trạng chỉ xuất hiện ở nam và **mọi** con trai của người bệnh đều bệnh → gen trên Y.

**Lỗi thường gặp:**
- Viết kiểu gen nam mắc bệnh liên kết X là $X^h X^h$ — sai, nam chỉ có một X nên phải viết $X^h Y$; sai lầm này kéo theo mọi bước tính xác suất đều lệch.
- Nhầm xác suất đồng thời với xác suất có điều kiện: trả lời 1/2 cho câu hỏi 'xác suất sinh con trai bị bệnh' — sai, vì phải nhân thêm xác suất là con trai; 1/2 chỉ đúng khi đã biết đứa trẻ là con trai.
- Kết luận bệnh lặn liên kết X ngay khi thấy nam mắc nhiều hơn nữ mà không kiểm tra mâu thuẫn — sai, phải kiểm tra điều kiện bắt buộc: mọi con gái bị bệnh đều phải có bố bị bệnh; nếu phả hệ vi phạm điều đó thì gen nằm trên nhiễm sắc thể thường.

<sub>`lesson.biology.di-truyen-hoc.di-truyen-lien-ket-gioi-tinh`</sub>

---

### 5. Di truyền ngoài nhân và đột biến nhiễm sắc thể
*Extranuclear inheritance and chromosomal mutations* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Nhận diện được di truyền theo dòng mẹ qua kết quả lai thuận nghịch
- Phân loại được đột biến cấu trúc và đột biến số lượng nhiễm sắc thể
- Giải thích được vì sao thể đa bội phổ biến ở thực vật nhưng hiếm ở động vật

## Dấu hiệu nhận ra gen không nằm trong nhân

Phép **lai thuận nghịch** là công cụ phân biệt. Nếu kết quả hai chiều lai như nhau → gen trên nhiễm sắc thể thường. Nếu khác nhau, có hai khả năng: gen liên kết giới tính (đời con có phân li khác nhau theo giới) hoặc gen ngoài nhân (**toàn bộ** đời con giống mẹ, không phân li theo giới).

Nguyên nhân: hợp tử nhận tế bào chất gần như hoàn toàn từ trứng; tinh trùng góp nhân là chính. Vì vậy ADN ti thể ở người luôn theo dòng mẹ — cơ sở để truy nguyên phả hệ mẫu hệ và để nghiên cứu 'Eve ti thể'.

## Đột biến cấu trúc nhiễm sắc thể

| Dạng | Hệ quả về gen | Ví dụ |
|---|---|---|
| Mất đoạn | Giảm số gen, thường gây chết | Hội chứng tiếng mèo kêu (5p−) |
| Lặp đoạn | Tăng số gen, tạo nguyên liệu cho gen mới tiến hoá | Mắt dẹt ở ruồi giấm |
| Đảo đoạn | Số gen không đổi, thay đổi trật tự và mức biểu hiện | Đảo đoạn ở muỗi Anopheles |
| Chuyển đoạn | Chuyển gen sang nhiễm sắc thể khác | Bạch cầu tuỷ mạn (NST Philadelphia) |

Đảo đoạn và chuyển đoạn không làm mất vật chất di truyền nhưng vẫn nguy hiểm: chúng gây khó khăn khi bắt cặp ở giảm phân, tạo giao tử mất cân bằng, làm giảm khả năng sinh sản. Đồng thời đây là cơ chế quan trọng góp phần **cách li sinh sản** và hình thành loài.

## Đột biến số lượng

- **Lệch bội**: do không phân li một cặp. Ở người phần lớn gây chết phôi; các trường hợp sống được là Down (thể ba 21), Turner (XO), Klinefelter (XXY) — đều liên quan các nhiễm sắc thể nhỏ hoặc nhiễm sắc thể giới tính có cơ chế bù liều.
- **Đa bội**: rất phổ biến ở thực vật (khoảng 50-70% loài thực vật có hoa có tổ tiên đa bội), tạo cây to, quả lớn, chống chịu tốt. Thể **tam bội** bất thụ vì bộ ba nhiễm sắc thể không thể chia đôi đều — chính đặc điểm này được khai thác để tạo dưa hấu, chuối không hạt.

Đa bội hiếm ở động vật vì hai lí do: cơ chế xác định giới tính dựa trên tỉ lệ nhiễm sắc thể giới tính trên nhiễm sắc thể thường bị phá vỡ, và động vật hầu hết sinh sản hữu tính bắt buộc nên không thể duy trì dòng bất thụ như thực vật sinh sản sinh dưỡng.

**Lỗi thường gặp:**
- Kết luận 'gen liên kết giới tính' ngay khi thấy lai thuận nghịch cho kết quả khác nhau — sai, vì di truyền ngoài nhân cũng cho kết quả khác nhau; dấu hiệu phân biệt là ở di truyền ngoài nhân **toàn bộ** đời con giống mẹ và không có sự phân li khác nhau giữa hai giới.
- Tính giao tử của thể tứ bội AAaa theo tỉ lệ 1:2:1 như thể lưỡng bội — sai, phải dùng tổ hợp chọn 2 trong 4 alen nên tỉ lệ đúng là 1:4:1.
- Nói đảo đoạn 'vô hại vì không mất gen' — sai, đảo đoạn làm thay đổi vị trí gen so với vùng điều hoà và gây khó khăn bắt cặp ở giảm phân, dẫn tới giao tử mất cân bằng và giảm khả năng sinh sản.

<sub>`lesson.biology.di-truyen-hoc.di-truyen-ngoai-nhan-va-dot-bien-nst`</sub>

---

## Unit 6: Gene Expression and Regulation (Biểu hiện và điều hoà gen)

### 1. Nhân đôi ADN: cơ chế bán bảo toàn và bộ máy sao chép
*DNA replication: semi-conservative mechanism and the replication machinery* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Chứng minh được cơ chế bán bảo toàn dựa trên thí nghiệm Meselson - Stahl
- Giải thích được vì sao một mạch được tổng hợp liên tục còn mạch kia gián đoạn
- Vận dụng được công thức tính số nucleotide môi trường cung cấp qua k lần nhân đôi

## Ba giả thuyết và một thí nghiệm quyết định

Năm 1958 có ba khả năng: bảo toàn (giữ nguyên phân tử mẹ, tạo phân tử con hoàn toàn mới), bán bảo toàn, và phân tán (mỗi mạch chắp vá cũ - mới).

Meselson và Stahl nuôi *E. coli* trong môi trường $^{15}\text{N}$ nhiều thế hệ rồi chuyển sang $^{14}\text{N}$, li tâm theo gradient tỉ trọng CsCl:

- Sau **1** thế hệ: chỉ **một** vạch ở tỉ trọng trung gian → loại bỏ giả thuyết bảo toàn (giả thuyết này đòi hỏi hai vạch).
- Sau **2** thế hệ: **hai** vạch, một nhẹ và một trung gian, tỉ lệ 1:1 → loại bỏ giả thuyết phân tán (giả thuyết này đòi một vạch duy nhất ngày càng nhẹ).

Chỉ bán bảo toàn giải thích được cả hai kết quả.

## Bộ máy sao chép

1. **Helicase** tháo xoắn tại điểm khởi đầu, tạo chạc chữ Y; protein SSB giữ hai mạch tách rời; **topoisomerase** gỡ xoắn căng phía trước.
2. **Primase** đặt đoạn mồi ARN cung cấp đầu 3'-OH.
3. **ADN polymerase III** kéo dài mạch mới chỉ theo chiều **5' → 3'**.
4. **ADN polymerase I** thay mồi ARN bằng ADN; **ligase** nối các đoạn.

## Hệ quả của quy tắc 5' → 3'

Vì hai mạch khuôn đối song song, tại một chạc sao chép chỉ **một** mạch cho phép tổng hợp liên tục hướng về chạc — **mạch dẫn đầu**. Mạch còn lại phải tổng hợp thành từng **đoạn Okazaki** ngược hướng chạc — **mạch chậm**. Đây không phải sự bất tiện ngẫu nhiên mà là hệ quả tất yếu của việc polymerase chỉ gắn nucleotide vào đầu 3'-OH.

## Độ chính xác

ADN polymerase có hoạt tính **đọc sửa** exonuclease 3' → 5': gặp base sai thì lùi lại, cắt bỏ rồi gắn lại. Kết hợp với hệ sửa sai bắt cặp sau sao chép, tỉ lệ sai giảm từ $10^{-5}$ xuống khoảng $10^{-9}$ — tức trung bình một sai sót trên một tỉ nucleotide.

**Lỗi thường gặp:**
- Tính số phân tử ADN con hoàn toàn mới bằng $2^k - 1$ — sai, vì ADN mẹ có **hai** mạch và sau nhân đôi hai mạch này nằm trong hai phân tử khác nhau, nên số phân tử chứa mạch cũ luôn bằng 2 và công thức đúng là $2^k - 2$.
- Nói ADN polymerase 'tổng hợp mạch mới theo cả hai chiều' — sai, enzyme chỉ gắn nucleotide vào đầu 3'-OH nên mạch mới luôn dài ra theo chiều 5' → 3'; chính ràng buộc này sinh ra mạch chậm và đoạn Okazaki.
- Cho rằng kết quả sau một thế hệ của Meselson - Stahl đã đủ chứng minh bán bảo toàn — sai, một vạch trung gian cũng phù hợp với giả thuyết phân tán; phải có kết quả thế hệ thứ hai mới loại bỏ được giả thuyết đó.

<sub>`lesson.biology.bieu-hien-gen.cau-truc-va-nhan-doi-adn`</sub>

---

### 2. Phiên mã và hoàn thiện ARN ở sinh vật nhân thực
*Transcription and RNA processing in eukaryotes* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Mô tả được ba giai đoạn phiên mã và vai trò của mạch khuôn
- Giải thích được ba bước hoàn thiện mARN sơ khai ở sinh vật nhân thực
- Phân tích được ý nghĩa tiến hoá của cắt nối luân phiên

## Vì sao cần bản sao trung gian

ADN là bản gốc quý và nằm trong nhân; ribosome lại ở tế bào chất. Thay vì mang bản gốc ra ngoài, tế bào tạo bản sao dùng một lần — mARN. Cách này còn cho phép **khuếch đại**: một gen phiên mã ra hàng nghìn mARN, mỗi mARN dịch mã ra hàng chục protein.

## Ba giai đoạn

1. **Khởi đầu**: yếu tố phiên mã nhận diện hộp TATA ở vùng khởi động, ARN polymerase II gắn vào, tháo xoắn.
2. **Kéo dài**: enzyme trượt dọc mạch khuôn theo chiều **3' → 5'**, tổng hợp ARN theo chiều 5' → 3', bắt cặp A-U, T-A, G-C, C-G.
3. **Kết thúc**: gặp tín hiệu kết thúc, ARN được giải phóng.

Khác biệt then chốt với nhân đôi: chỉ **một** mạch được dùng làm khuôn, chỉ **một đoạn** ADN (một gen) được sao chép, sản phẩm là **mạch đơn** và **không cần đoạn mồi** vì ARN polymerase tự khởi đầu được.

## Hoàn thiện ARN — đặc quyền của nhân thực

mARN sơ khai phải qua ba bước trước khi ra khỏi nhân:

- **Mũ 7-methylguanosine** ở đầu 5': bảo vệ khỏi enzyme phân giải và là tín hiệu cho ribosome nhận diện.
- **Đuôi poly-A** ở đầu 3' (50-250 adenine): tăng độ bền; đuôi càng dài mARN càng sống lâu nên càng dịch mã được nhiều lần.
- **Cắt intron nối exon** nhờ spliceosome.

Sinh vật nhân sơ không có bước này — mARN của chúng được dịch mã ngay khi còn đang được phiên mã.

## Cắt nối luân phiên giải một nghịch lí

Bộ gen người chỉ khoảng 20 000 gen mã hoá protein, nhưng cơ thể tạo ra hơn 100 000 loại protein khác nhau. Cắt nối luân phiên là lời giải chính: gen troponin T cho hàng chục biến thể, gen Dscam của ruồi giấm về lí thuyết cho hơn 38 000 biến thể.

Điều này buộc phải xét lại định nghĩa 'một gen - một chuỗi polypeptide' — nó chỉ đúng ở nhân sơ. Ngoài ra intron còn là nơi trao đổi module giữa các gen (xáo trộn exon), một nguồn tạo protein mới trong tiến hoá.

**Lỗi thường gặp:**
- Cho rằng cả hai mạch của gen đều được dùng làm khuôn phiên mã — sai, mỗi gen chỉ dùng một mạch làm khuôn; nếu dùng cả hai sẽ tạo ra hai mARN bổ sung nhau, chúng bắt cặp với nhau và không dịch mã được.
- Tính số ribonucleotide của mARN bằng tổng số nucleotide của gen — sai, phải chia đôi vì mARN chỉ được tổng hợp theo **một** mạch khuôn.
- Nghĩ intron là 'ADN rác vô dụng' — sai, intron chứa trình tự điều hoà, cho phép cắt nối luân phiên tạo nhiều protein từ một gen, và tạo điều kiện cho xáo trộn exon trong tiến hoá.

<sub>`lesson.biology.bieu-hien-gen.phien-ma-va-hoan-thien-arn`</sub>

---

### 3. Dịch mã và đặc điểm của mã di truyền
*Translation and the properties of the genetic code* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu được bốn đặc điểm của mã di truyền và hệ quả sinh học của mỗi đặc điểm
- Mô tả được ba giai đoạn dịch mã và vai trò của tARN, ribosome
- Vận dụng được các công thức tính số amino acid, số liên kết peptide và thời gian dịch mã

## Bài toán ghép mã

Có 20 loại amino acid nhưng chỉ 4 loại nucleotide. Mã một nucleotide cho $4^1 = 4$ tổ hợp — thiếu. Mã hai nucleotide cho $4^2 = 16$ — vẫn thiếu. Mã ba nucleotide cho $4^3 = 64$ — đủ và **dư**. Chính lượng dư này tạo ra tính thoái hoá.

## Bốn đặc điểm và hệ quả

| Đặc điểm | Nội dung | Hệ quả |
|---|---|---|
| Bộ ba | Đọc theo cụm 3 nucleotide liên tục, không gối lên nhau | Thêm/mất 1-2 nucleotide gây dịch khung, hậu quả nặng |
| Đặc hiệu | Mỗi codon chỉ mã hoá một amino acid | Bản dịch không mơ hồ |
| Thoái hoá | Nhiều codon cho cùng một amino acid | Đột biến ở nucleotide thứ ba thường **im lặng** |
| Phổ biến | Gần như mọi loài dùng chung bảng mã | Cơ sở cho công nghệ gen chuyển loài và bằng chứng nguồn gốc chung |

## Ba giai đoạn dịch mã

1. **Mở đầu**: tiểu đơn vị bé của ribosome gắn mARN, tìm codon AUG; tARN mang methionine (fMet ở nhân sơ) khớp vào vị trí P; tiểu đơn vị lớn ráp vào.
2. **Kéo dài**: tARN mang amino acid tương ứng vào vị trí A; ribosome xúc tác tạo liên kết peptide (hoạt tính này do **rARN** đảm nhiệm — một ribozyme); ribosome dịch chuyển ba nucleotide, tARN rỗng rời khỏi vị trí E.
3. **Kết thúc**: gặp UAA, UAG hoặc UGA — không tARN nào khớp; yếu tố giải phóng thuỷ phân liên kết và chuỗi polypeptide được thả ra.

Sau đó methionine mở đầu thường bị cắt bỏ, và chuỗi cuộn gấp thành cấu trúc bậc ba, có thể được biến đổi thêm ở Golgi.

## Tốc độ và hiệu quả

Ribosome nhân sơ dịch khoảng 15-20 amino acid mỗi giây. Nhiều ribosome cùng làm việc trên một mARN tạo **polysome**, cách nhau tối thiểu khoảng 80 nucleotide. Ở nhân sơ, phiên mã và dịch mã còn ghép đồng thời nên phản ứng của tế bào với môi trường cực nhanh — ưu thế đánh đổi bằng việc mất đi các tầng điều hoà tinh vi của nhân thực.

**Lỗi thường gặp:**
- Lấy số bộ ba trên mARN làm số amino acid của chuỗi polypeptide — sai, phải trừ bộ ba kết thúc (không mã hoá amino acid) và trừ tiếp methionine mở đầu nếu đề hỏi chuỗi **hoàn chỉnh**.
- Nói mã di truyền thoái hoá nghĩa là 'một codon mã hoá nhiều amino acid' — sai và ngược hẳn; thoái hoá là nhiều codon cùng chỉ một amino acid, còn mỗi codon vẫn chỉ ứng với đúng một amino acid (tính đặc hiệu).
- Cho rằng liên kết peptide do protein của ribosome xúc tác — sai, hoạt tính peptidyl transferase nằm ở **rARN** của tiểu đơn vị lớn, nghĩa là ribosome là một ribozyme.

<sub>`lesson.biology.bieu-hien-gen.dich-ma-va-ma-di-truyen`</sub>

---

### 4. Điều hoà biểu hiện gen ở sinh vật nhân sơ: mô hình operon
*Prokaryotic gene regulation: the operon model* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Mô tả được cấu trúc của operon và vai trò từng thành phần
- So sánh được operon cảm ứng (lac) và operon ức chế (trp) theo logic điều khiển
- Phân tích được kết quả đột biến ở từng thành phần của operon lac

## Vì sao vi khuẩn cần điều hoà

*E. coli* có khoảng 4300 gen nhưng không bao giờ cần tất cả cùng lúc. Sản xuất enzyme không dùng tới là lãng phí nguyên liệu và ATP. Jacob và Monod (1961) tìm ra cơ chế và đoạt giải Nobel — đây là mô hình điều hoà gen đầu tiên được giải mã.

## Cấu trúc operon lac

$$\text{Gen điều hoà } (lacI) \quad | \quad \text{P} \;-\; \text{O} \;-\; lacZ \;-\; lacY \;-\; lacA$$

Gen điều hoà nằm **ngoài** operon và có promoter riêng, luôn phiên mã ở mức thấp để tạo protein ức chế.

## Logic hai chiều

**Operon lac — cảm ứng, điều khiển dị hoá:**

- Không có lactose: protein ức chế gắn vùng vận hành → operon **tắt**. Hợp lí vì không có cơ chất thì làm enzyme để làm gì.
- Có lactose: allolactose gắn protein ức chế, làm nó rời vùng vận hành → operon **bật**.

**Operon trp — ức chế, điều khiển đồng hoá:**

- Không có tryptophan: protein ức chế ở dạng bất hoạt → operon **bật**, tế bào tự tổng hợp trp.
- Dư tryptophan: trp đóng vai trò **đồng ức chế**, gắn vào protein ức chế làm nó hoạt động → operon **tắt**.

Quy luật chung: gen dị hoá thường **cảm ứng** bởi cơ chất; gen đồng hoá thường **ức chế** bởi sản phẩm. Cả hai đều là phản hồi âm nhưng ở hai chiều ngược nhau.

## Tầng điều khiển thứ hai

Ngay cả khi có lactose, nếu môi trường còn glucose thì vi khuẩn vẫn ưu tiên glucose. Cơ chế: glucose thấp → cAMP cao → phức hợp CAP-cAMP gắn vùng gần promoter và **tăng ái lực** của ARN polymerase. Vậy operon lac chỉ chạy hết công suất khi **có lactose và thiếu glucose** — đây là điều khiển hai đầu vào, một dạng cổng logic AND ở cấp phân tử.

**Lỗi thường gặp:**
- Nói lactose 'gắn vào vùng vận hành để bật operon' — sai, lactose (dạng allolactose) gắn vào **protein ức chế** chứ không gắn ADN; chính sự đổi hình dạng của protein mới làm nó rời vùng vận hành.
- Cho rằng operon lac bật hết công suất chỉ cần có lactose — sai, còn phải thiếu glucose để cAMP tăng và phức hợp CAP-cAMP hoạt hoá promoter; có cả hai đường thì lactose vẫn gần như không được dùng.
- Coi gen điều hoà lacI là một phần của operon — sai, nó nằm ngoài operon với promoter riêng và được phiên mã độc lập; nếu nó thuộc operon thì khi operon tắt sẽ không còn protein ức chế, dẫn tới mâu thuẫn logic.

<sub>`lesson.biology.bieu-hien-gen.dieu-hoa-gen-o-nhan-so-operon`</sub>

---

### 5. Điều hoà biểu hiện gen ở sinh vật nhân thực và biệt hoá tế bào
*Eukaryotic gene regulation and cell differentiation* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Liệt kê và giải thích được các tầng điều hoà từ cấu trúc chromatin tới sau dịch mã
- Giải thích được cơ chế biểu sinh qua methyl hoá ADN và biến đổi histone
- Phân tích được vì sao các tế bào cùng bộ gen lại có kiểu hình khác nhau

## Nghịch lí cần giải

Mọi tế bào trong cơ thể bạn (trừ giao tử và tế bào miễn dịch đã tái tổ hợp) mang **cùng một bộ gen**. Vậy vì sao tế bào thần kinh, tế bào gan và tế bào cơ lại khác nhau đến thế? Câu trả lời: khác nhau ở **gen nào đang được bật**, chứ không phải gen nào đang có.

## Điều hoà theo tầng

1. **Cấu trúc chromatin**: ADN quấn quanh histone. Chromatin cuộn chặt (dị nhiễm sắc) thì bộ máy phiên mã không tiếp cận được. Acetyl hoá đuôi histone làm trung hoà điện tích dương, nới lỏng liên kết với ADN âm → **mở** gen. Methyl hoá ADN ở đảo CpG thường làm **đóng** gen.
2. **Khởi đầu phiên mã** — tầng quan trọng nhất: tổ hợp các yếu tố phiên mã gắn promoter và enhancer. Enhancer có thể nằm cách gen hàng chục nghìn cặp base và tác động nhờ ADN uốn cong lại.
3. **Hoàn thiện ARN**: cắt nối luân phiên chọn tổ hợp exon phù hợp từng mô.
4. **Vận chuyển và độ bền mARN**: đuôi poly-A dài hay ngắn; miRNA phân giải mARN đích.
5. **Dịch mã**: yếu tố khởi đầu bị phosphoryl hoá để tắt dịch mã hàng loạt khi stress.
6. **Sau dịch mã**: cắt tiền chất (proinsulin → insulin), gắn nhóm chức, hoặc gắn ubiquitin để đánh dấu phân giải ở proteasome.

## Biểu sinh: bộ nhớ của tế bào

Dấu biểu sinh được sao chép sang tế bào con, nên một tế bào gan phân chia ra hai tế bào gan chứ không ra tế bào thần kinh. Đây chính là **bộ nhớ** giúp biệt hoá bền vững.

Biểu sinh cũng phần nào **đảo ngược được** — cơ sở của công nghệ tế bào gốc cảm ứng iPSC của Yamanaka: chỉ cần đưa bốn yếu tố phiên mã vào tế bào da trưởng thành là đưa được nó về trạng thái đa năng. Ngoài ra, dấu biểu sinh chịu ảnh hưởng của môi trường (dinh dưỡng, stress, độc chất) và một phần có thể truyền qua vài thế hệ — chủ đề đang được nghiên cứu tích cực.

**Lỗi thường gặp:**
- Nói tế bào biệt hoá 'mất bớt gen không cần thiết' — sai, hầu hết tế bào giữ nguyên toàn bộ bộ gen; bằng chứng là thí nghiệm nhân bản cừu Dolly từ nhân tế bào tuyến vú vẫn tạo được cá thể hoàn chỉnh.
- Đồng nhất biểu sinh với đột biến — sai, biểu sinh **không** thay đổi trình tự nucleotide và có thể đảo ngược, còn đột biến thay đổi trình tự và thường bền vững.
- Cho rằng điều hoà ở nhân thực chỉ diễn ra ở bước phiên mã — sai, tế bào nhân thực điều hoà ở nhiều tầng từ chromatin tới sau dịch mã, và chính sự phân tầng này tạo nên độ tinh vi mà operon nhân sơ không có.

<sub>`lesson.biology.bieu-hien-gen.dieu-hoa-gen-o-nhan-thuc`</sub>

---

### 6. Đột biến gen: các dạng và hậu quả ở mức phân tử
*Gene mutations: types and molecular consequences* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân loại được đột biến điểm theo hậu quả lên chuỗi polypeptide
- Giải thích được vì sao đột biến dịch khung nguy hiểm hơn đột biến thay thế
- Đánh giá được vai trò hai mặt của đột biến đối với cá thể và quần thể

## Đột biến gen là gì

Đột biến gen là thay đổi trong trình tự nucleotide của một gen. Đột biến **điểm** chỉ liên quan một cặp nucleotide và có ba dạng: thay thế, thêm, mất.

## Bốn hậu quả của đột biến thay thế

| Dạng | Mô tả | Ví dụ |
|---|---|---|
| Im lặng | Codon mới cùng mã hoá amino acid cũ | UCU → UCC (đều Ser) |
| Sai nghĩa | Đổi sang amino acid khác | GAG → GUG (Glu → Val), hồng cầu hình liềm |
| Vô nghĩa | Đổi thành codon kết thúc | UGG → UGA, chuỗi cụt |
| Ở vị trí cắt nối | Làm sai quá trình cắt intron | Nhiều dạng beta-thalassemia |

Đột biến im lặng chiếm tỉ lệ đáng kể vì tính thoái hoá tập trung ở **nucleotide thứ ba** của codon — thay đổi ở vị trí này thường không đổi amino acid.

Mức nghiêm trọng của đột biến sai nghĩa phụ thuộc hai yếu tố: (1) amino acid mới có tính chất khác nhiều không (kị nước thay ưa nước là nặng); (2) vị trí đó có nằm ở tâm hoạt động hay vùng bảo thủ không.

## Vì sao dịch khung nặng hơn

Thêm hoặc mất 1-2 nucleotide làm mọi codon phía sau bị đọc lệch → chuỗi amino acid từ điểm đó trở đi hoàn toàn khác, và thường xuất hiện codon kết thúc sớm một cách ngẫu nhiên. Ngược lại, thêm hoặc mất đúng **3** nucleotide chỉ thêm/mất một amino acid mà giữ nguyên khung — nhẹ hơn nhiều (bệnh xơ nang thường do mất 3 nucleotide, protein CFTR chỉ thiếu một phenylalanine nhưng gấp sai).

## Hai mặt của đột biến

Với **cá thể**, đột biến ở tế bào sinh dưỡng có thể gây ung thư, ở tế bào sinh dục có thể gây bệnh di truyền. Với **quần thể và tiến hoá**, đột biến là nguồn **duy nhất** tạo alen mới — nguyên liệu sơ cấp cho chọn lọc tự nhiên. Không có đột biến thì mọi cơ chế còn lại (giảm phân, thụ tinh, trôi dạt) chỉ xáo trộn lại vốn alen sẵn có mà không bao giờ tạo ra cái mới.

Tần số đột biến tự phát rất thấp ($10^{-6}$ đến $10^{-4}$ trên mỗi gen mỗi thế hệ), nhưng nhân với hàng chục nghìn gen và hàng triệu cá thể thì mỗi thế hệ vẫn có rất nhiều alen mới xuất hiện.

**Lỗi thường gặp:**
- Cho rằng mọi đột biến thay thế đều làm đổi amino acid — sai, do mã di truyền thoái hoá nên thay đổi ở nucleotide thứ ba của codon thường cho đột biến im lặng.
- Nghĩ đột biến mất 3 nucleotide cũng gây dịch khung — sai, mất bội số của 3 giữ nguyên khung đọc nên chỉ mất một amino acid; chỉ số nucleotide không chia hết cho 3 mới gây dịch khung.
- Kết luận 'đột biến luôn có hại' — sai, phần lớn đột biến là trung tính, một số có lợi trong môi trường nhất định, và về mặt tiến hoá đột biến là nguồn duy nhất tạo alen mới.

<sub>`lesson.biology.bieu-hien-gen.dot-bien-gen-va-hau-qua`</sub>

---

### 7. Công nghệ ADN: PCR, điện di, giải trình tự và CRISPR
*DNA technology: PCR, gel electrophoresis, sequencing and CRISPR* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được ba bước của một chu kì PCR và vai trò của enzyme chịu nhiệt
- Phân tích được nguyên lí phân tách đoạn ADN bằng điện di trên gel
- Đánh giá được cơ chế và các vấn đề đạo đức của chỉnh sửa gen bằng CRISPR-Cas9

## PCR: photocopy phân tử

Một chu kì gồm ba bước, lặp lại 25-35 lần:

1. **Biến tính** ($94$-$96^\circ\text{C}$): tách hai mạch bằng cách phá liên kết hydrogen.
2. **Gắn mồi** ($50$-$65^\circ\text{C}$): hai mồi bám hai đầu vùng đích. Nhiệt độ bước này là biến then chốt — quá thấp thì mồi bám cả chỗ không đặc hiệu, quá cao thì mồi không bám.
3. **Kéo dài** ($72^\circ\text{C}$): Taq polymerase tổng hợp mạch mới.

Số bản sao tăng theo $2^n$; sau 30 chu kì được khoảng $10^9$ bản. Taq polymerase — tách từ vi khuẩn suối nước nóng *Thermus aquaticus* — là mấu chốt: enzyme thường sẽ biến tính ngay ở bước 1. Đây là ví dụ điển hình cho việc nghiên cứu cơ bản về sinh vật ưa nhiệt sinh ra ứng dụng không lường trước.

## Điện di: sàng phân tử

ADN tích điện âm đồng đều theo chiều dài nên **tỉ lệ điện tích trên khối lượng gần như không đổi** — nghĩa là mọi đoạn chịu lực điện tương đương trên một đơn vị khối lượng. Vì vậy yếu tố phân tách duy nhất là **kích thước**: đoạn ngắn luồn qua mạng lưới agarose dễ hơn nên đi xa hơn. So với thang chuẩn (ladder) ta ước lượng được kích thước; quan hệ giữa quãng đường và $\log(\text{số cặp base})$ gần tuyến tính.

## Giải trình tự Sanger

Thêm một tỉ lệ nhỏ **dideoxynucleotide** (ddNTP) thiếu nhóm 3'-OH: khi được gắn vào, mạch dừng ngay. Kết quả là tập hợp các mạch có mọi chiều dài, mỗi mạch kết thúc bằng một ddNTP đánh dấu huỳnh quang bốn màu. Điện di mao quản đọc lần lượt màu theo chiều dài tăng dần chính là đọc được trình tự.

## CRISPR-Cas9

Vốn là hệ miễn dịch của vi khuẩn chống thực khuẩn thể. Được cải biên thành công cụ: thay ARN dẫn đường là nhắm được bất kì trình tự nào. Ứng dụng gồm tạo mô hình bệnh, liệu pháp gen cho bệnh hồng cầu hình liềm và beta-thalassemia (đã được phê duyệt), cải tạo cây trồng.

**Giới hạn và tranh cãi**: cắt nhầm ngoài đích (off-target), khảm khi chỉnh sửa phôi, và ranh giới đạo đức giữa chỉnh sửa **tế bào sinh dưỡng** (chỉ ảnh hưởng bệnh nhân) với chỉnh sửa **dòng mầm** (di truyền cho đời sau, hiện bị cấm hoặc hạn chế nghiêm ngặt ở hầu hết các nước).

**Lỗi thường gặp:**
- Nói đoạn ADN lớn chạy xa hơn trên gel vì 'nặng hơn nên bị đẩy mạnh hơn' — sai, tỉ lệ điện tích trên khối lượng gần như không đổi nên lực điện trên đơn vị khối lượng như nhau; yếu tố quyết định là ma sát khi luồn qua lưới gel, nên đoạn **nhỏ** đi xa hơn.
- Cho rằng PCR cần enzyme ligase và helicase như nhân đôi trong tế bào — sai, PCR dùng **nhiệt độ** để tách mạch thay cho helicase, và tổng hợp trọn vẹn đoạn đích nên không cần ligase nối các đoạn.
- Áp dụng quy tắc nhân xác suất cho hồ sơ ADN của hai anh em ruột — sai, các locus vẫn độc lập nhưng hai người thân chia sẻ alen theo huyết thống nên xác suất trùng khớp cao hơn nhiều so với người không họ hàng.

<sub>`lesson.biology.bieu-hien-gen.cong-nghe-adn-pcr-dien-di-crispr`</sub>

---

## Unit 7: Natural Selection (Chọn lọc tự nhiên và tiến hoá)

### 1. Bằng chứng tiến hoá: từ hoá thạch tới sinh học phân tử
*Evidence for evolution: from fossils to molecular biology* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được cơ quan tương đồng và cơ quan tương tự cùng ý nghĩa tiến hoá của mỗi loại
- Giải thích được vì sao bằng chứng phân tử là bằng chứng mạnh nhất về nguồn gốc chung
- Đánh giá được điểm mạnh và hạn chế của bằng chứng hoá thạch

## Bằng chứng giải phẫu

Chi trước của người, cá voi, dơi và ngựa có chức năng hoàn toàn khác nhau (cầm nắm, bơi, bay, chạy) nhưng đều gồm cùng một bộ xương: một xương cánh tay, hai xương cẳng tay, các xương cổ tay và năm ngón. Không có lí do kĩ thuật nào bắt buộc phải như vậy — trừ khi cả bốn loài thừa hưởng cùng một sơ đồ từ tổ tiên chung rồi biến đổi theo hướng khác nhau (**tiến hoá phân li**).

Ngược lại, cánh chim và cánh côn trùng cùng để bay nhưng cấu tạo hoàn toàn khác: đó là **tiến hoá hội tụ**, chứng minh áp lực chọn lọc tương tự tạo giải pháp tương tự chứ không chứng minh quan hệ họ hàng.

**Cơ quan thoái hoá** (xương chậu ở cá voi, ruột thừa, cơ dựng lông ở người) là bằng chứng đặc biệt thuyết phục vì chúng vô nghĩa nếu mỗi loài được thiết kế riêng biệt, nhưng hoàn toàn hợp lí như di tích của tổ tiên.

## Bằng chứng phôi sinh học

Phôi cá, kì giông, rùa, gà và người ở giai đoạn sớm đều có khe mang và đuôi. Điều này không có nghĩa 'phôi người lặp lại lịch sử tiến hoá' — cách diễn giải đó đã bị bác bỏ — mà nghĩa là các loài này chia sẻ chung một bộ **gen điều hoà phát triển** (gen Hox) từ tổ tiên.

## Bằng chứng phân tử — mạnh nhất

Mọi sinh vật đều dùng ADN, dùng chung bảng **mã di truyền**, dùng ATP, có ribosome. Xác suất để điều này xảy ra độc lập nhiều lần là cực nhỏ.

Định lượng hơn: so sánh trình tự cytochrome c hoặc rARN cho ra 'khoảng cách di truyền' phù hợp với cây phân loại dựng từ hình thái. Hai nguồn dữ liệu độc lập cho cùng kết luận là kiểm chứng chéo mạnh mẽ.

Khoảng cách thô đo bằng tỉ lệ vị trí khác nhau, $p = n_d/n$. Nếu tốc độ thay thế trung tính $\mu$ gần như không đổi thì $d = 2\mu t$ — hệ số 2 vì **cả hai** dòng cùng tích luỹ đột biến kể từ tổ tiên chung. Đây là **đồng hồ phân tử**, phải hiệu chuẩn bằng hoá thạch và chỉ đáng tin trong khoảng thời gian chưa bão hoà: khi hai loài quá xa nhau, một vị trí có thể bị thay đổi nhiều lần nên $p$ đánh giá **thấp** khoảng cách thật.

## Hạn chế của hoá thạch

Hoá thạch cho bằng chứng trực tiếp về dạng trung gian (*Archaeopteryx*, *Tiktaalik*) và về trình tự thời gian. Nhưng hồ sơ hoá thạch **không đầy đủ** vì hoá thạch chỉ hình thành trong điều kiện hiếm gặp, thiên lệch về loài có xương/vỏ cứng, sống ở nơi lắng đọng trầm tích. Vì thế 'thiếu mắt xích' là điều được dự đoán trước chứ không phải phản chứng.

**Lỗi thường gặp:**
- Dùng cánh chim và cánh dơi làm ví dụ cơ quan tương tự — sai một nửa: xét như 'cánh' thì chúng tương tự (bề mặt bay hình thành độc lập), nhưng xét bộ xương bên trong thì chúng tương đồng vì đều là chi trước của động vật bốn chân.
- Nói 'còn thiếu mắt xích nên tiến hoá chưa được chứng minh' — sai, hoá thạch hoá là sự kiện hiếm và thiên lệch, nên hồ sơ không đầy đủ là điều lí thuyết dự đoán trước; hơn nữa bằng chứng phân tử độc lập đã đủ mạnh.
- Giải thích khe mang ở phôi người bằng 'phôi lặp lại các giai đoạn tiến hoá' — sai, cách diễn giải này đã bị bác bỏ; nguyên nhân đúng là các loài chia sẻ chung bộ gen điều hoà phát triển thừa hưởng từ tổ tiên.

<sub>`lesson.biology.chon-loc-tu-nhien.bang-chung-tien-hoa`</sub>

---

### 2. Chọn lọc tự nhiên và ba kiểu chọn lọc
*Natural selection and three modes of selection* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu được bốn tiền đề dẫn tới chọn lọc tự nhiên theo lập luận của Darwin
- Phân biệt được chọn lọc ổn định, chọn lọc vận động và chọn lọc phân hoá qua dạng phân bố kiểu hình
- Vận dụng được hệ số chọn lọc để tính biến đổi tần số alen qua các thế hệ

## Bốn tiền đề của Darwin

Lập luận chọn lọc tự nhiên chặt chẽ như một chứng minh toán học:

1. Sinh vật sinh ra **nhiều con hơn** số có thể sống sót.
2. Các cá thể trong quần thể **biến dị** về nhiều đặc điểm.
3. Một phần biến dị đó **di truyền được**.
4. ⟹ Cá thể mang đặc điểm phù hợp với môi trường sống sót và sinh sản nhiều hơn; tần số alen tương ứng tăng qua các thế hệ.

Mấu chốt thường bị bỏ sót: chọn lọc tác động lên **kiểu hình** của cá thể, nhưng hệ quả tiến hoá xảy ra ở **tần số alen của quần thể**. Cá thể không tiến hoá — quần thể mới tiến hoá.

## Ba kiểu chọn lọc

| Kiểu | Kiểu hình được ưu tiên | Hệ quả với phương sai | Ví dụ |
|---|---|---|---|
| Ổn định | Trung gian | Giảm | Khối lượng sơ sinh ở người |
| Vận động | Một cực | Trung bình dịch chuyển | Bướm bạch dương thời công nghiệp; kháng kháng sinh |
| Phân hoá | Cả hai cực | Tăng, phân bố hai đỉnh | Kích thước mỏ chim sẻ Darwin khi chỉ có hạt rất to và rất nhỏ |

## Vì sao alen có hại không biến mất hoàn toàn

Chọn lọc chỉ 'nhìn thấy' kiểu hình. Alen lặn có hại nằm trong thể **dị hợp** được che giấu, nên không bị loại bỏ. Khi tần số $q$ đã rất nhỏ, hầu như toàn bộ alen lặn nằm ở thể dị hợp: tỉ số $\dfrac{2pq}{q^2} = \dfrac{2p}{q}$ tăng vọt khi $q \to 0$. Đó là lí do dù chọn lọc chống thể lặn hoàn toàn ($s = 1$), tần số $q$ giảm ngày càng chậm theo công thức

$$q_n = \frac{q_0}{1 + n q_0}$$

và không bao giờ về 0.

Ngoài ra, dị hợp tử có thể có **ưu thế** — alen hồng cầu hình liềm được duy trì ở vùng sốt rét vì thể dị hợp $HbA/HbS$ vừa không bị thiếu máu nặng vừa kháng sốt rét tốt hơn.

**Lỗi thường gặp:**
- Nói 'cá thể tiến hoá để thích nghi với môi trường' — sai, cá thể không thay đổi kiểu gen trong đời sống; biến dị có sẵn trước khi áp lực chọn lọc xuất hiện và chọn lọc chỉ sàng lọc, tiến hoá xảy ra ở mức quần thể.
- Đo độ thích nghi bằng sức khoẻ hoặc tuổi thọ — sai, tiêu chí duy nhất là số con cháu sống sót tới tuổi sinh sản; một cá thể sống lâu nhưng không sinh sản có độ thích nghi bằng 0.
- Cho rằng chọn lọc hoàn toàn ($s = 1$) sẽ loại hẳn alen lặn khỏi quần thể sau vài thế hệ — sai, alen lặn được che giấu trong thể dị hợp nên tần số chỉ tiệm cận 0 theo hàm $q_0/(1+nq_0)$ mà không bao giờ đạt 0.

<sub>`lesson.biology.chon-loc-tu-nhien.chon-loc-tu-nhien-va-cac-kieu-chon-loc`</sub>

---

### 3. Cân bằng Hardy - Weinberg: mô hình, điều kiện và ứng dụng
*Hardy-Weinberg equilibrium: model, conditions and applications* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu được năm điều kiện của cân bằng Hardy - Weinberg và ý nghĩa của việc chúng bị vi phạm
- Tính được tần số alen và tần số kiểu gen từ tỉ lệ kiểu hình lặn
- Xác định được một quần thể có đang ở trạng thái cân bằng di truyền hay không

## Vì sao cần một mô hình 'không có gì xảy ra'

Câu hỏi ban đầu của di truyền học quần thể: alen trội có tự nhiên tăng dần lên và thay thế alen lặn không? Hardy và Weinberg chứng minh: **không**. Nếu không có tác nhân nào can thiệp, tần số alen giữ nguyên vô hạn.

Giá trị của mô hình nằm ở chỗ nó là **mô hình không**. Khi số liệu thực tế lệch khỏi dự đoán, ta biết chắc có một tác nhân tiến hoá đang hoạt động và có thể đi tìm nó.

## Hai phương trình

$$p + q = 1 \qquad\text{và}\qquad p^2 + 2pq + q^2 = 1$$

Trong đó $p^2$ là tần số đồng hợp trội, $2pq$ là dị hợp, $q^2$ là đồng hợp lặn. Với tính trạng trội hoàn toàn, đại lượng **quan sát trực tiếp được** duy nhất là $q^2$ (kiểu hình lặn), nên mọi bài toán đều bắt đầu từ đó: $q = \sqrt{q^2}$.

## Năm điều kiện

1. Quần thể **rất lớn** (không có trôi dạt di truyền).
2. **Giao phối ngẫu nhiên** (không giao phối chọn lọc, không nội phối).
3. Không có **đột biến**.
4. Không có **di - nhập gen**.
5. Không có **chọn lọc tự nhiên**.

Không quần thể tự nhiên nào thoả mãn đủ cả năm. Đó không phải khuyết điểm của mô hình mà chính là công dụng của nó.

## Kiểm tra cân bằng

Quy trình: từ số liệu kiểu gen quan sát tính $p$ và $q$ → tính tần số kiểu gen **kì vọng** theo $p^2, 2pq, q^2$ → so sánh với quan sát → dùng kiểm định chi bình phương với 1 bậc tự do (vì đã dùng số liệu để ước lượng một tham số).

Sai lệch điển hình và ý nghĩa: thiếu dị hợp so với kì vọng thường chỉ ra **nội phối** hoặc quần thể bị chia nhỏ; thừa dị hợp chỉ ra **ưu thế dị hợp** hoặc giao phối không cùng loại.

## Trường hợp gen trên X

Với gen trên vùng không tương đồng của X, nam giới chỉ có một alen nên tần số nam mắc bệnh **chính bằng** $q$, trong khi nữ mắc bệnh là $q^2$. Đây là cách tính $q$ nhanh và chính xác nhất cho mù màu hay máu khó đông.

**Lỗi thường gặp:**
- Lấy tỉ lệ kiểu hình lặn làm luôn tần số alen lặn — sai, tỉ lệ kiểu hình lặn là $q^2$ chứ không phải $q$; phải khai căn, và bỏ qua bước này sẽ cho $q$ lớn hơn thực tế rất nhiều khi bệnh hiếm.
- Dùng $2pq$ làm xác suất một người **khoẻ mạnh** mang gen — sai, phải chia cho tỉ lệ người khoẻ $(p^2 + 2pq)$ vì đây là xác suất có điều kiện; sai số nhỏ khi bệnh hiếm nhưng lớn khi bệnh phổ biến.
- Kết luận quần thể 'đang tiến hoá' chỉ vì tần số kiểu gen lệch khỏi $p^2 : 2pq : q^2$ — sai, sai lệch có thể do giao phối không ngẫu nhiên (nội phối) vốn làm thay đổi tần số **kiểu gen** mà không làm thay đổi tần số **alen**.

<sub>`lesson.biology.chon-loc-tu-nhien.hardy-weinberg-va-dieu-kien`</sub>

---

### 4. Trôi dạt di truyền, dòng gen và các nhân tố tiến hoá khác
*Genetic drift, gene flow and other evolutionary forces* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao trôi dạt di truyền mạnh hơn ở quần thể nhỏ
- Phân biệt được hiệu ứng thắt cổ chai và hiệu ứng kẻ sáng lập
- So sánh được vai trò của năm nhân tố tiến hoá đối với tần số alen

## Năm nhân tố làm quần thể lệch khỏi Hardy - Weinberg

Mỗi điều kiện của mô hình không, khi bị vi phạm, cho một nhân tố tiến hoá:

| Nhân tố | Tác động lên tần số alen | Có tạo thích nghi không |
|---|---|---|
| Đột biến | Chậm, tạo alen **mới** | Ngẫu nhiên |
| Chọn lọc tự nhiên | Có hướng | **Có** |
| Trôi dạt di truyền | Ngẫu nhiên, mạnh ở quần thể nhỏ | Không |
| Dòng gen | Làm đồng nhất các quần thể | Không trực tiếp |
| Giao phối không ngẫu nhiên | Đổi tần số **kiểu gen**, không đổi tần số alen | Không |

Điểm quan trọng: chỉ **chọn lọc tự nhiên** tạo ra thích nghi. Bốn nhân tố còn lại làm thay đổi vốn gen nhưng không theo hướng phù hợp môi trường.

## Vì sao trôi dạt mạnh ở quần thể nhỏ

Đây là bài toán lấy mẫu. Tung đồng xu 10 lần rất dễ ra 7 sấp 3 ngửa (lệch 20% so với kì vọng); tung 10 000 lần thì tỉ lệ gần như chắc chắn sát 50-50. Tương tự, quần thể nhỏ chọn giao tử từ một 'mẫu' nhỏ nên tần số alen dao động mạnh mỗi thế hệ, và alen có thể **cố định** (đạt 1) hoặc **mất hẳn** (đạt 0) hoàn toàn ngẫu nhiên.

Hai kịch bản kinh điển:

- **Thắt cổ chai**: quần thể bị giảm đột ngột do thảm hoạ. Báo cheetah, hải cẩu voi phương Bắc (từng còn khoảng 20 cá thể) nay có đa dạng di truyền cực thấp dù số lượng đã phục hồi — vì đa dạng mất đi không tự quay lại nhanh.
- **Kẻ sáng lập**: nhóm nhỏ di cư lập quần thể mới. Cộng đồng Amish ở Pennsylvania có tần số hội chứng Ellis-van Creveld cao bất thường vì một trong các cặp vợ chồng sáng lập mang alen đó.

## Kích thước quần thể hiệu dụng

$N_e$ — số cá thể thực sự đóng góp gen — thường **nhỏ hơn nhiều** so với tổng số cá thể đếm được, do tỉ lệ giới tính lệch, chênh lệch số con giữa các cá thể, và dao động số lượng qua các năm. Đây là đại lượng then chốt trong sinh học bảo tồn: một đàn 500 con nhưng chỉ vài con đực tham gia sinh sản có thể có $N_e$ chỉ vài chục, và mất đa dạng di truyền nhanh như quần thể vài chục cá thể.

**Lỗi thường gặp:**
- Nói trôi dạt di truyền 'loại bỏ alen có hại' — sai, trôi dạt hoàn toàn ngẫu nhiên và có thể cố định cả alen có hại; chỉ chọn lọc tự nhiên mới tác động theo hướng phù hợp môi trường.
- Cho rằng giao phối không ngẫu nhiên làm thay đổi tần số alen — sai, nội phối chỉ làm tăng tỉ lệ đồng hợp và giảm dị hợp; tần số alen $p$ và $q$ vẫn giữ nguyên nên bản thân nó không phải nhân tố tiến hoá theo nghĩa chặt.
- Dùng tổng số cá thể đếm được để đánh giá nguy cơ mất đa dạng di truyền — sai, đại lượng quyết định là kích thước quần thể **hiệu dụng** $N_e$, thường nhỏ hơn nhiều do tỉ lệ giới tính lệch và chênh lệch số con.

<sub>`lesson.biology.chon-loc-tu-nhien.troi-dat-di-truyen-va-dong-gen`</sub>

---

### 5. Hình thành loài, cây phát sinh chủng loại và nguồn gốc sự sống
*Speciation, phylogenetic trees and the origin of life* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được hình thành loài khác khu và cùng khu qua vai trò của cách li địa lí
- Đọc và diễn giải được cây phát sinh chủng loại theo nút phân nhánh và nhóm đơn ngành
- Đánh giá được các bằng chứng thực nghiệm về nguồn gốc sự sống

## Loài là gì

Khái niệm loài sinh học: nhóm quần thể có khả năng giao phối tự nhiên và sinh con hữu thụ, cách li sinh sản với nhóm khác. Định nghĩa này mạnh nhưng có giới hạn rõ: không áp dụng được cho sinh vật sinh sản vô tính, cho hoá thạch, và cho các trường hợp lai được một phần trong tự nhiên. Vì thế thực tế còn dùng khái niệm loài hình thái, loài sinh thái và loài phát sinh chủng loại.

## Hai con đường hình thành loài

- **Khác khu (allopatric)**: rào cản địa lí chia cắt quần thể → hai vốn gen phân hoá độc lập do chọn lọc khác nhau, đột biến khác nhau và trôi dạt → khi gặp lại, cách li sinh sản đã hình thành. Ví dụ: sóc Abert hai bên hẻm núi Grand Canyon; chim sẻ Darwin trên các đảo Galapagos.
- **Cùng khu (sympatric)**: phổ biến ở thực vật qua **đa bội hoá**, xảy ra chỉ trong một thế hệ. Cây tứ bội 4n giao phối với cây gốc 2n cho con lai 3n bất thụ, nên nó lập tức cách li sinh sản với loài mẹ.

## Nhịp độ tiến hoá

Hai mô hình không loại trừ nhau: **tiệm tiến** (biến đổi đều đặn, thấy rõ ở các dãy hoá thạch động vật thân mềm) và **đứt quãng cân bằng** (giai đoạn ổn định dài xen kẽ biến đổi nhanh khi môi trường thay đổi đột ngột hoặc quần thể nhỏ tách ra).

## Đọc cây phát sinh chủng loại

Quy tắc bắt buộc: quan hệ họ hàng được xác định bởi **vị trí nút phân nhánh chung gần nhất**, không phải bởi khoảng cách ngang trên hình vẽ hay thứ tự các nhánh ở ngọn. Nhánh có thể xoay quanh nút mà cây không đổi ý nghĩa. Cá sấu gần chim hơn gần thằn lằn — kết luận phản trực giác nhưng đúng, và đó là lí do 'bò sát' không phải nhóm đơn ngành.

## Nguồn gốc sự sống

Giả thuyết bốn giai đoạn: (1) tổng hợp phi sinh học các đơn phân hữu cơ; (2) trùng hợp thành polime; (3) hình thành protobiont có màng bao và môi trường trong khác ngoài; (4) xuất hiện di truyền.

Thí nghiệm Miller - Urey (1953) chứng minh giai đoạn 1 khả thi: phóng điện qua hỗn hợp khí khử tạo ra amino acid. Đối với giai đoạn 4, giả thuyết **thế giới ARN** được ủng hộ mạnh vì ARN vừa lưu trữ thông tin vừa có hoạt tính xúc tác (ribozyme) — nó giải được nghịch lí 'ADN cần protein để sao chép, protein cần ADN để được tạo ra'.

**Lưu ý về giới hạn**: đây là các giả thuyết có bằng chứng ủng hộ ở từng bước, chưa phải một con đường đã được tái dựng hoàn chỉnh trong phòng thí nghiệm.

**Lỗi thường gặp:**
- Đọc cây phát sinh theo thứ tự nhánh ở ngọn, cho rằng hai nhánh vẽ cạnh nhau là họ hàng gần — sai, các nhánh có thể xoay tự do quanh nút; tiêu chí duy nhất là vị trí nút tổ tiên chung gần nhất.
- Nói loài ở ngọn cây 'tiến hoá cao hơn' loài ở nhánh tách sớm — sai, mọi loài còn sống đều có cùng độ dài lịch sử tiến hoá tính từ tổ tiên chung; cây chỉ mô tả quan hệ họ hàng chứ không xếp hạng.
- Cho rằng thí nghiệm Miller - Urey đã 'tạo ra sự sống' — sai, nó chỉ chứng minh các đơn phân hữu cơ có thể hình thành phi sinh học, tức mới là giai đoạn đầu tiên trong bốn giai đoạn giả thuyết.

<sub>`lesson.biology.chon-loc-tu-nhien.hinh-thanh-loai-cay-phat-sinh-nguon-goc-su-song`</sub>

---

## Unit 8: Ecology (Sinh thái học)

### 1. Đáp ứng của sinh vật với môi trường: giới hạn sinh thái và ổ sinh thái
*Organism responses to the environment: tolerance limits and ecological niche* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Xác định được giới hạn sinh thái, khoảng thuận lợi và khoảng chống chịu từ đồ thị
- Phân biệt được ổ sinh thái cơ bản và ổ sinh thái thực tế
- Giải thích được ảnh hưởng của nhiệt độ tới tốc độ chuyển hoá qua hệ số $Q_{10}$

## Nhân tố sinh thái và quy luật giới hạn

Nhân tố sinh thái chia hai nhóm: **vô sinh** (nhiệt độ, ánh sáng, độ ẩm, pH, độ mặn) và **hữu sinh** (các sinh vật khác). Với mỗi nhân tố, đồ thị mức sống sót theo cường độ nhân tố có dạng chuông: hai điểm gây chết ở hai đầu, khoảng chống chịu ở hai bên và khoảng thuận lợi ở giữa.

Hai hệ quả cần nhớ:

- Loài có giới hạn **rộng** với nhiều nhân tố thì phân bố rộng (loài rộng nhiệt, rộng muối); loài có giới hạn hẹp thì phân bố hạn chế và dễ bị đe doạ khi môi trường đổi.
- Phân bố thực tế bị quyết định bởi nhân tố **bất lợi nhất**, dù các nhân tố khác đều tối ưu — đây là quy luật yếu tố giới hạn.

## Ổ sinh thái: 'nghề' chứ không phải 'nhà'

Nơi ở là địa chỉ, ổ sinh thái là nghề nghiệp. Phân biệt tiếp:

- **Ổ cơ bản**: toàn bộ điều kiện loài có thể sống được nếu không có cạnh tranh.
- **Ổ thực tế**: phần thực sự chiếm được sau khi bị các loài khác cạnh tranh.

Thí nghiệm Connell với hai loài hà biển ở vùng triều Scotland cho thấy điều này rất rõ: loài *Chthamalus* có thể sống ở cả vùng triều cao và thấp, nhưng khi có mặt *Balanus* cạnh tranh mạnh hơn thì nó bị đẩy hẳn lên vùng triều cao. Loại bỏ *Balanus* thì *Chthamalus* lan xuống — chứng minh ổ thực tế nhỏ hơn ổ cơ bản.

## Nhiệt độ và chuyển hoá

Vì mọi phản ứng sinh học đều do enzyme xúc tác, tốc độ chuyển hoá tăng theo nhiệt độ tới điểm tối ưu rồi giảm dốc do biến tính. Trong khoảng an toàn:

$$Q_{10} = \left(\frac{k_2}{k_1}\right)^{\frac{10}{T_2 - T_1}} \approx 2$$

Động vật **biến nhiệt** có thân nhiệt thay đổi theo môi trường nên tốc độ chuyển hoá dao động lớn, nhưng tiết kiệm năng lượng. Động vật **hằng nhiệt** giữ thân nhiệt ổn định nên hoạt động được ở dải nhiệt độ rộng, đổi lại phải chi 60-80% năng lượng ăn vào chỉ để duy trì thân nhiệt. Đây là một sự đánh đổi tiến hoá, không có phương án nào ưu việt tuyệt đối.

**Lỗi thường gặp:**
- Đồng nhất ổ sinh thái với nơi ở — sai, nơi ở chỉ là vị trí không gian còn ổ sinh thái bao gồm cả nguồn thức ăn, thời gian hoạt động và mọi yêu cầu môi trường; hai loài có thể cùng nơi ở mà khác ổ sinh thái.
- Ngoại suy $Q_{10}$ ra ngoài khoảng nhiệt độ đã đo — sai, quan hệ mũ chỉ đúng dưới nhiệt độ tối ưu; vượt qua đó enzyme biến tính và tốc độ giảm đột ngột.
- Cho rằng loài phân bố hẹp là do 'thiếu một nhân tố nào đó' chung chung — sai, phải chỉ ra nhân tố **giới hạn** cụ thể: phân bố bị quyết định bởi nhân tố bất lợi nhất chứ không bởi trung bình của các nhân tố.

<sub>`lesson.biology.sinh-thai-hoc.dap-ung-cua-sinh-vat-voi-moi-truong`</sub>

---

### 2. Sinh thái quần thể: mô hình tăng trưởng mũ và logistic
*Population ecology: exponential and logistic growth models* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được tăng trưởng theo hàm mũ và tăng trưởng logistic qua dạng đồ thị và điều kiện áp dụng
- Tính được tốc độ tăng trưởng quần thể từ số liệu sinh - tử - nhập cư - di cư
- Vận dụng được phương pháp bắt - đánh dấu - thả - bắt lại để ước lượng kích thước quần thể

## Bốn quá trình quyết định kích thước quần thể

$$N_{t+1} = N_t + (\text{sinh} + \text{nhập cư}) - (\text{tử} + \text{di cư})$$

Quần thể tăng khi tổng vào lớn hơn tổng ra — đơn giản nhưng dễ bị bỏ sót hai thành phần di cư trong bài toán thực tế.

## Mô hình mũ: tiềm năng sinh học

$$\frac{dN}{dt} = r_{max} N$$

Đồ thị hình chữ J. Điều kiện áp dụng rất hẹp: tài nguyên **không giới hạn**, không có cạnh tranh, không dịch bệnh, không kẻ thù. Trong tự nhiên chỉ gặp trong thời gian ngắn — vi khuẩn mới cấy vào môi trường, loài xâm lấn mới vào vùng đất mới, quần thể phục hồi sau thảm hoạ.

Điểm dễ hiểu nhầm: tốc độ tăng riêng $r$ **không đổi**, nhưng số cá thể thêm vào mỗi đơn vị thời gian lại tăng dần vì $N$ tăng. Đó là lí do đồ thị dốc lên ngày càng nhanh.

## Mô hình logistic: có sức chứa

$$\frac{dN}{dt} = r_{max} N \frac{K - N}{K}$$

Thừa số $\dfrac{K-N}{K}$ là 'phanh sinh thái': khi $N$ nhỏ nó gần bằng 1 (tăng trưởng gần như hàm mũ), khi $N \to K$ nó tiến về 0. Tại $N = K$ quần thể ổn định.

Tốc độ tăng **tuyệt đối** lớn nhất tại $N = K/2$ — kết quả có ý nghĩa thực tiễn lớn: trong khai thác thuỷ sản và lâm nghiệp, giữ quần thể quanh $K/2$ cho sản lượng bền vững cao nhất.

## Nhân tố điều chỉnh

- **Phụ thuộc mật độ**: cạnh tranh thức ăn, dịch bệnh, chất thải, vật ăn thịt — tác động mạnh hơn khi mật độ cao, tạo phản hồi âm giữ $N$ quanh $K$.
- **Không phụ thuộc mật độ**: bão, cháy rừng, rét đậm — tác động như nhau ở mọi mật độ, gây biến động đột ngột.

## Ước lượng kích thước quần thể

Với động vật di động, dùng chỉ số Lincoln: bắt $n_1$ cá thể, đánh dấu, thả; sau một thời gian bắt lại $n_2$ cá thể thấy $m_2$ con có dấu. Khi đó $N = \dfrac{n_1 n_2}{m_2}$. Giả thiết bắt buộc: cá thể đánh dấu trộn đều trở lại, dấu không rơi và không làm cá thể dễ bị bắt hay dễ bị ăn thịt hơn, không có sinh - tử - di cư đáng kể giữa hai lần bắt.

**Lỗi thường gặp:**
- Nói trong tăng trưởng hàm mũ 'tốc độ tăng trưởng ngày càng lớn nên $r$ tăng dần' — sai, $r$ là hằng số; cái tăng là số cá thể thêm vào mỗi đơn vị thời gian, vì nó bằng $rN$ mà $N$ đang tăng.
- Cho rằng quần thể tăng nhanh nhất khi $N$ gần $K$ vì có nhiều cá thể sinh sản — sai, khi $N \to K$ thừa số $(K-N)/K$ tiến về 0 nên tốc độ tuyệt đối giảm; cực đại nằm ở $N = K/2$.
- Áp dụng chỉ số Lincoln mà không kiểm tra giả thiết — sai, nếu con vật bị đánh dấu trở nên dễ bắt lại (quen bẫy) thì $m_2$ tăng giả tạo và $N$ bị ước lượng **thấp** hơn thực tế; ngược lại nếu dấu làm chúng dễ bị ăn thịt thì $N$ bị ước lượng cao.

<sub>`lesson.biology.sinh-thai-hoc.tang-truong-quan-the-mu-va-logistic`</sub>

---

### 3. Tương tác giữa các loài trong quần xã
*Interspecific interactions in communities* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân loại được các kiểu tương tác theo dấu tác động lên mỗi loài
- Giải thích được nguyên lí loại trừ cạnh tranh và cơ chế phân hoá ổ sinh thái
- Phân tích được vai trò của loài chủ chốt đối với cấu trúc quần xã

## Bảng phân loại theo dấu

Cách gọn nhất để nhớ là ghi dấu tác động lên từng loài:

| Kiểu | Loài A | Loài B | Ví dụ |
|---|---|---|---|
| Cạnh tranh | − | − | Hai loài trùng cỏ tranh thức ăn |
| Vật ăn thịt - con mồi | + | − | Linh miêu và thỏ tuyết |
| Kí sinh | + | − | Giun đũa và người |
| Cộng sinh | + | + | Vi khuẩn nốt sần và cây họ Đậu |
| Hợp tác | + | + | Chim mỏ đỏ và trâu rừng |
| Hội sinh | + | 0 | Phong lan bám thân cây gỗ |
| Ức chế - cảm nhiễm | 0 | − | Tảo giáp tiết độc tố gây chết cá |

Phân biệt cộng sinh và hợp tác: cộng sinh là quan hệ **bắt buộc** (tách ra thì ít nhất một bên không sống được), hợp tác là quan hệ có lợi nhưng **không bắt buộc**.

## Nguyên lí loại trừ cạnh tranh

Gause nuôi *Paramecium aurelia* và *P. caudatum* riêng rẽ: cả hai đều đạt cân bằng logistic. Nuôi chung trong cùng bình với cùng loại thức ăn: *P. caudatum* bị tiêu diệt sau khoảng 16 ngày. Nhưng nuôi *P. aurelia* với *P. bursaria* — loài kiếm ăn ở đáy bình thay vì trong nước — thì cả hai cùng tồn tại. Kết luận: cùng tồn tại được hay không phụ thuộc mức **trùng lặp ổ sinh thái**.

Trong tự nhiên, hệ quả tiến hoá là **phân li tính trạng**: chim sẻ Darwin sống chung trên một đảo có kích thước mỏ khác nhau rõ rệt hơn so với khi mỗi loài sống riêng trên đảo của mình — bằng chứng trực tiếp cho việc cạnh tranh định hình tiến hoá.

## Loài chủ chốt

Thí nghiệm Paine trên bãi đá triều: loại bỏ sao biển *Pisaster* — vốn chỉ chiếm một phần nhỏ sinh khối — khiến trai vẹm bùng phát và độc chiếm giá thể, số loài giảm từ 15 xuống còn 8. Sao biển giữ đa dạng bằng cách kìm hãm loài cạnh tranh mạnh nhất.

Bài học ứng dụng: bảo tồn không thể chỉ đếm số loài mà phải xác định **loài nào giữ vai trò cấu trúc**. Việc tái thả sói vào Yellowstone kéo theo thay đổi cả thảm thực vật ven suối và dòng chảy — một chuỗi tác động từ trên xuống (top-down) qua nhiều bậc dinh dưỡng.

**Lỗi thường gặp:**
- Coi kí sinh và vật ăn thịt là một — sai, vật ăn thịt thường giết chết con mồi nhanh và ăn nhiều cá thể, còn vật kí sinh sống lâu dài trên một vật chủ và thường **không** giết ngay vì cần vật chủ sống để tồn tại.
- Kết luận từ nguyên lí loại trừ cạnh tranh rằng hai loài cạnh tranh không bao giờ cùng tồn tại — sai, chúng vẫn cùng tồn tại được nếu ổ sinh thái chỉ trùng một phần, hoặc nếu môi trường biến động thường xuyên nên chưa kịp đạt cân bằng.
- Xác định loài chủ chốt dựa vào sinh khối hoặc độ phong phú — sai, đặc trưng của loài chủ chốt là ảnh hưởng lớn **không tương xứng** với sinh khối; loài chiếm sinh khối lớn nhất được gọi là loài ưu thế, không phải loài chủ chốt.

<sub>`lesson.biology.sinh-thai-hoc.tuong-tac-giua-cac-loai`</sub>

---

### 4. Cấu trúc quần xã, diễn thế sinh thái và đo đa dạng sinh học
*Community structure, ecological succession and measuring biodiversity* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được diễn thế nguyên sinh và diễn thế thứ sinh qua điểm xuất phát
- Tính được chỉ số đa dạng Simpson và giải thích ý nghĩa của giá trị thu được
- Vận dụng được phương pháp ô tiêu chuẩn để ước lượng độ phong phú và độ phủ

## Ba đại lượng mô tả quần xã

- **Độ giàu loài** (species richness): đếm số loài, không quan tâm số lượng cá thể.
- **Độ đồng đều** (evenness): các loài phân bố cá thể đều nhau hay có một loài áp đảo.
- **Đa dạng loài**: chỉ số gộp cả hai, ví dụ Simpson và Shannon.

Đây là ba đại lượng khác nhau và hay bị lẫn. Hai quần xã cùng có 5 loài (cùng độ giàu) nhưng một quần xã có 1 loài chiếm 96% cá thể thì kém đa dạng hơn hẳn quần xã phân bố đều.

## Chỉ số Simpson

Dạng dùng ở IB và A-Level:

$$D = \frac{N(N-1)}{\sum n(n-1)}$$

với $N$ là tổng số cá thể và $n$ là số cá thể mỗi loài. Ý nghĩa xác suất của $\sum p_i^2$ là: xác suất hai cá thể bốc ngẫu nhiên thuộc **cùng** một loài. Vì vậy chỉ số càng lớn (hoặc $1 - \sum p_i^2$ càng gần 1) thì đa dạng càng cao.

Dạng $\dfrac{N(N-1)}{\sum n(n-1)}$ là hiệu chỉnh cho mẫu hữu hạn: bốc không hoàn lại nên sau khi lấy cá thể thứ nhất chỉ còn $N-1$ cá thể để bốc lần hai.

## Diễn thế sinh thái

| | Nguyên sinh | Thứ sinh |
|---|---|---|
| Xuất phát | Không có đất, không có sinh vật | Đã có đất, còn hạt giống và rễ ngầm |
| Loài tiên phong | Địa y, rêu (chịu khô, cố định đạm) | Cỏ dại, cây bụi mọc nhanh |
| Thời gian tới đỉnh cực | Hàng trăm - hàng nghìn năm | Hàng chục - hàng trăm năm |
| Ví dụ | Đảo Surtsey sau phun trào, băng hà rút | Rừng sau cháy, ruộng bỏ hoang |

Xu hướng chung trong diễn thế: sinh khối tăng, độ giàu loài tăng rồi ổn định, lưới thức ăn phức tạp dần, và tỉ số **sản lượng sơ cấp thô trên hô hấp** giảm dần về 1 ở quần xã đỉnh cực — nghĩa là hệ trưởng thành dùng gần hết năng lượng sản xuất được cho duy trì chính nó.

## Lấy mẫu bằng ô tiêu chuẩn

Quy trình chuẩn: chia khu vực thành lưới toạ độ, dùng số ngẫu nhiên chọn vị trí đặt ô (tránh thiên lệch do người chọn), đếm số cá thể hoặc ước lượng phần trăm độ phủ, lặp lại đủ nhiều ô cho tới khi giá trị trung bình cộng dồn ổn định. Mật độ ước lượng $=$ số cá thể trung bình trên một ô chia diện tích ô; kích thước quần thể $=$ mật độ nhân tổng diện tích.

**Lỗi thường gặp:**
- Đánh giá đa dạng chỉ bằng số loài — sai, hai quần xã cùng số loài vẫn khác nhau rất nhiều về đa dạng nếu độ đồng đều khác nhau; chỉ số Simpson và Shannon tồn tại chính vì lí do này.
- Nhầm hai dạng của chỉ số Simpson: $\sum p_i^2$ (chỉ số ưu thế, càng nhỏ càng đa dạng) và $1 - \sum p_i^2$ hay $N(N-1)/\sum n(n-1)$ (chỉ số đa dạng, càng lớn càng đa dạng) — dùng lẫn sẽ cho kết luận ngược hoàn toàn.
- Đặt ô tiêu chuẩn ở chỗ 'trông có vẻ tiêu biểu' — sai, đó là thiên lệch chủ quan; vị trí phải chọn bằng số ngẫu nhiên trên lưới toạ độ để mẫu đại diện cho toàn khu vực.

<sub>`lesson.biology.sinh-thai-hoc.cau-truc-quan-xa-dien-the-va-da-dang-sinh-hoc`</sub>

---

### 5. Dòng năng lượng, hiệu suất sinh thái và tháp sinh thái
*Energy flow, ecological efficiency and ecological pyramids* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao chuỗi thức ăn hiếm khi dài quá năm bậc dinh dưỡng
- Tính được hiệu suất sinh thái và năng suất sơ cấp tinh từ số liệu
- Phân tích được vì sao tháp sinh khối có thể lộn ngược còn tháp năng lượng thì không

## Vì sao năng lượng chỉ đi một chiều

Khác với vật chất (được tái sử dụng qua các chu trình), năng lượng **đi một chiều**: vào hệ dưới dạng ánh sáng, ra khỏi hệ dưới dạng nhiệt. Nhiệt không thể tái sử dụng để tạo chất hữu cơ, nên hệ sinh thái phải liên tục được cấp năng lượng mới từ Mặt Trời.

## Ba lí do năng lượng thất thoát giữa các bậc

1. Không phải mọi cá thể bậc dưới đều bị ăn (một phần chết đi vào chuỗi mùn bã).
2. Không phải mọi thứ ăn vào đều được hấp thụ (phần không tiêu hoá thải ra theo phân).
3. Phần lớn năng lượng hấp thụ được dùng cho **hô hấp** để duy trì hoạt động sống và thoát ra dưới dạng nhiệt.

Kết quả là hiệu suất sinh thái trung bình khoảng 10%. Với chuỗi 5 bậc, năng lượng đến bậc cuối chỉ còn $10^{-4}$ so với ban đầu — đây chính là lí do vật lí khiến chuỗi thức ăn hiếm khi dài quá 4-5 bậc, và vì sao động vật ăn thịt đầu bảng luôn hiếm.

## Hai đại lượng năng suất

$$GPP = \text{tổng năng lượng cố định qua quang hợp}, \qquad NPP = GPP - R$$

Chỉ NPP mới là 'thu nhập ròng' — phần chuyển lên bậc trên được. Ở rừng nhiệt đới GPP rất cao nhưng R cũng rất cao (sinh khối lớn phải nuôi), nên tỉ lệ NPP/GPP thấp hơn so với cây nông nghiệp non đang lớn nhanh.

## Ba loại tháp

- **Tháp số lượng** có thể lộn ngược: một cây sồi nuôi hàng nghìn sâu.
- **Tháp sinh khối** có thể lộn ngược ở hệ thuỷ sinh: sinh khối thực vật phù du tại một thời điểm nhỏ hơn sinh khối động vật phù du, vì thực vật phù du có tuổi thọ vài ngày và được thay thế liên tục — tốc độ luân chuyển rất nhanh.
- **Tháp năng lượng** không bao giờ lộn ngược, vì nó đo năng lượng **đi qua** mỗi bậc trong một khoảng thời gian (thường kJ·m⁻²·năm⁻¹), tức đã tính cả sự luân chuyển. Định luật hai nhiệt động lực học bảo đảm điều này.

## Ứng dụng

Một hecta trồng lúa nuôi được nhiều người hơn hẳn cùng diện tích chăn nuôi bò, vì ăn chay rút ngắn chuỗi thức ăn xuống một bậc và tránh được lần thất thoát 90%. Đây là lập luận sinh thái học định lượng cho các vấn đề an ninh lương thực.

**Lỗi thường gặp:**
- Dùng GPP làm mẫu số khi tính hiệu suất sinh thái giữa thực vật và động vật ăn cỏ — sai, phải dùng NPP vì phần năng lượng thực vật đã hô hấp mất không còn tồn tại dưới dạng chất hữu cơ để bị ăn.
- Nói tháp sinh khối luôn có đáy rộng — sai, ở hệ thuỷ sinh tháp sinh khối có thể lộn ngược do thực vật phù du có tốc độ luân chuyển rất nhanh; chỉ tháp **năng lượng** mới luôn đáy rộng.
- Giải thích chuỗi thức ăn ngắn bằng 'không đủ loài' — sai, nguyên nhân là định lượng năng lượng: mỗi bậc mất khoảng 90% nên sau 4-5 bậc năng lượng còn lại không đủ nuôi một quần thể tồn tại được.

<sub>`lesson.biology.sinh-thai-hoc.dong-nang-luong-va-thap-sinh-thai`</sub>

---

### 6. Chu trình sinh địa hoá, tác động của con người và biến đổi khí hậu
*Biogeochemical cycles, human impact and climate change* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Mô tả được các bể chứa và dòng chuyển chính trong chu trình carbon và chu trình nitrogen
- Giải thích được cơ chế hiệu ứng nhà kính và bằng chứng về biến đổi khí hậu do con người
- Phân tích được hậu quả sinh thái của phú dưỡng và axit hoá đại dương

## Nguyên tắc chung của chu trình vật chất

Khác với năng lượng, các nguyên tố được **tuần hoàn**: từ môi trường vô sinh vào cơ thể sinh vật, qua các bậc dinh dưỡng, rồi trở lại môi trường nhờ sinh vật phân giải. Mỗi chu trình có các **bể chứa** (nơi tích luỹ, luân chuyển chậm) và các **dòng chuyển** (luân chuyển nhanh).

## Chu trình carbon

Dòng chính: quang hợp lấy $\text{CO}_2$ ra khỏi khí quyển; hô hấp và phân giải trả lại. Trạng thái tự nhiên gần cân bằng.

Con người phá vỡ cân bằng bằng hai việc: **đốt nhiên liệu hoá thạch** (giải phóng carbon đã bị khoá hàng trăm triệu năm) và **phá rừng** (vừa giảm hấp thụ vừa giải phóng carbon dự trữ). Nồng độ $\text{CO}_2$ khí quyển tăng từ khoảng 280 ppm thời tiền công nghiệp lên trên 420 ppm hiện nay.

## Chu trình nitrogen

Nghịch lí: khí quyển có 78% $\text{N}_2$ nhưng cây không dùng được vì liên kết ba $\text{N}\equiv\text{N}$ cực bền. Các bước do vi khuẩn thực hiện:

$$\text{N}_2 \xrightarrow{\text{cố định}} \text{NH}_4^+ \xrightarrow{\text{nitrat hoá}} \text{NO}_2^- \rightarrow \text{NO}_3^- \xrightarrow{\text{đồng hoá}} \text{protein}$$

và đường trở về: **amôn hoá** (phân giải xác thành $\text{NH}_4^+$) cùng **phản nitrat hoá** (trả $\text{N}_2$ về khí quyển trong điều kiện yếm khí).

## Hiệu ứng nhà kính

Bức xạ Mặt Trời sóng ngắn xuyên qua khí quyển, mặt đất hấp thụ rồi phát lại bức xạ **hồng ngoại sóng dài**. Các khí nhà kính ($\text{CO}_2$, $\text{CH}_4$, $\text{N}_2\text{O}$, hơi nước) hấp thụ bức xạ này và phát lại theo mọi hướng, giữ nhiệt lại. Đây là hiệu ứng **tự nhiên và cần thiết** — không có nó nhiệt độ trung bình Trái Đất sẽ khoảng $-18^\circ\text{C}$. Vấn đề là mức **tăng cường** do phát thải.

Ba hậu quả liên kết: (1) băng tan và giãn nở nhiệt làm mực nước biển dâng; (2) đại dương hấp thụ $\text{CO}_2$ tạo acid carbonic làm **axit hoá đại dương**, cản trở sinh vật tạo vỏ calcium carbonate; (3) vùng phân bố của loài dịch chuyển về cực và lên cao, gây lệch pha giữa các loài phụ thuộc nhau (chim di cư đến khi sâu bướm đã qua đỉnh).

## Phú dưỡng

Phân bón dư và nước thải mang nitrate, phosphate vào thuỷ vực → tảo bùng phát → che ánh sáng làm thực vật đáy chết → vi khuẩn phân giải bùng nổ và tiêu thụ hết oxygen hoà tan → cá và động vật đáy chết hàng loạt, tạo 'vùng chết'. Chỉ số BOD tăng cao là dấu hiệu định lượng của quá trình này.

**Lỗi thường gặp:**
- Nói hiệu ứng nhà kính là hiện tượng có hại do con người tạo ra — sai, hiệu ứng nhà kính tự nhiên là điều kiện cần cho sự sống; vấn đề nằm ở mức **tăng cường** do phát thải khí nhà kính.
- Cho rằng cây trồng lấy nitrogen trực tiếp từ khí $\text{N}_2$ trong không khí — sai, liên kết ba của $\text{N}_2$ quá bền; cây chỉ hấp thụ được $\text{NH}_4^+$ và $\text{NO}_3^-$ sau khi vi khuẩn cố định đạm hoặc quá trình công nghiệp chuyển hoá.
- Giải thích cá chết trong phú dưỡng bằng 'tảo tiết chất độc' — sai trong đa số trường hợp; nguyên nhân chính là oxygen hoà tan bị vi khuẩn phân giải xác tảo tiêu thụ hết, tức chết vì thiếu oxygen.

<sub>`lesson.biology.sinh-thai-hoc.chu-trinh-sinh-dia-hoa-va-bien-doi-khi-hau`</sub>

---

## Unit 8: IBO - Phân tích dữ liệu và chiến lược làm bài

### 1. Đọc và phân tích dữ liệu thí nghiệm sinh học
*Reading and analysing biological experimental data* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được biến độc lập, biến phụ thuộc và biến kiểm soát trong một thiết kế thí nghiệm
- Phân tích được vai trò của nhóm đối chứng và mẫu lặp lại
- Đánh giá được kết luận nào rút ra được và kết luận nào vượt quá dữ liệu

## Câu hỏi đầu tiên khi nhìn một bảng dữ liệu

Không phải "kết quả là gì" mà là **"thí nghiệm này đo cái gì và kiểm soát cái gì"**. IBO chấm rất nặng phần này.

1. **Biến độc lập** (cái người làm thí nghiệm thay đổi) — thường là cột đầu tiên hoặc trục hoành.
2. **Biến phụ thuộc** (cái được đo) — trục tung.
3. **Biến kiểm soát** — thường ẩn trong phần mô tả phương pháp; đề hay hỏi "còn yếu tố nào chưa được kiểm soát?".
4. **Đối chứng** — âm (không có tác nhân) và dương (tác nhân đã biết có hiệu quả).

## Đọc bảng số liệu theo trình tự

- Đọc **tiêu đề và đơn vị** trước khi đọc số.
- Tìm **xu hướng**: tăng, giảm, bão hoà, có cực trị, hay không đổi.
- Tìm **điểm gãy**: nơi xu hướng đổi, thường là dấu hiệu của một yếu tố giới hạn mới.
- So sánh **độ lớn của khác biệt** với **độ lớn của biến thiên nội bộ** (độ lệch chuẩn, thanh sai số). Khác biệt nhỏ hơn biến thiên nội bộ thì không có ý nghĩa.

## Nguyên tắc vàng về kết luận

**Tương quan không phải nhân quả.** Dữ liệu quan sát cho phép nói "A đi kèm B"; chỉ thí nghiệm có can thiệp và đối chứng mới cho phép nói "A gây ra B".

Các động từ được phép dùng theo mức bằng chứng:

| Mức bằng chứng | Động từ hợp lệ |
|---|---|
| Số liệu mô tả | "tăng", "giảm", "cao hơn" |
| Có kiểm định thống kê | "khác biệt có ý nghĩa" |
| Có đối chứng và can thiệp | "gây ra", "dẫn tới" |
| Không có gì trong ba mức trên | "gợi ý rằng", "phù hợp với giả thuyết" |

## Đánh giá thiết kế: bốn câu hỏi mẫu

1. Cỡ mẫu có đủ không? Có bao nhiêu lặp lại **sinh học**?
2. Có đối chứng phù hợp không?
3. Có yếu tố gây nhiễu nào chưa kiểm soát (nhiệt độ, thời gian, tuổi mẫu)?
4. Phép đo có ngẫu nhiên hoá và mù đôi không (với thí nghiệm có đánh giá chủ quan)?

Trả lời được bốn câu này là làm chủ phần lớn điểm của câu hỏi phân tích dữ liệu.

**Lỗi thường gặp:**
- Kết luận nhân quả từ dữ liệu quan sát không có can thiệp — sai vì một biến thứ ba có thể gây ra cả hai hiện tượng; chỉ thiết kế có đối chứng và ngẫu nhiên hoá mới loại được khả năng này.
- Coi các lần đo lặp trên cùng một mẫu là lặp lại độc lập — sai vì chúng chỉ phản ánh sai số của dụng cụ, không phản ánh biến dị sinh học, nên không dùng để suy rộng ra quần thể.
- So sánh hai trung bình mà bỏ qua thanh sai số chồng lấn — sai vì khi hai khoảng sai số chồng lên nhau nhiều, khác biệt quan sát được có thể chỉ do biến động ngẫu nhiên.

<sub>`lesson.biology.ibo.doc-va-phan-tich-du-lieu-thi-nghiem`</sub>

---

### 2. Suy luận từ đồ thị sinh học: nhận dạng và diễn giải
*Interpreting biological graphs* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Nhận dạng được các dạng đồ thị đặc trưng trong sinh học và ý nghĩa của chúng
- Xác định được điểm bù, điểm bão hoà và yếu tố giới hạn từ đồ thị
- Vận dụng được đồ thị tuyến tính hoá để lấy tham số động học enzyme

## Thư viện dạng đồ thị sinh học

| Dạng | Ý nghĩa điển hình |
|---|---|
| Tăng rồi bão hoà (hyperbol) | Động học enzyme, quang hợp theo ánh sáng — một yếu tố giới hạn chuyển sang yếu tố khác |
| Chữ S (sigmoid) | Hợp tác dương: đường cong phân li oxygen của hemoglobin, tăng trưởng logistic |
| Chuông (đỉnh rồi giảm) | Ảnh hưởng nhiệt độ hoặc pH lên enzyme — tăng do động năng, giảm do biến tính |
| Mũ | Tăng trưởng quần thể không giới hạn, phản ứng dây chuyền |
| Giảm mũ | Phân rã, thải trừ thuốc, chết theo thời gian |
| Dao động lệch pha | Vật ăn thịt - con mồi (Lotka-Volterra) |

## Ba chỗ phải chỉ ra trên mỗi đồ thị

1. **Điểm bù** — nơi đường cắt trục, ví dụ điểm bù ánh sáng là khi quang hợp bằng hô hấp.
2. **Điểm bão hoà** — nơi đường bắt đầu nằm ngang; sau điểm này yếu tố trên trục hoành **không còn giới hạn**.
3. **Độ dốc ban đầu** — cho tốc độ tối đa khi yếu tố còn dồi dào, dùng để so sánh giữa các nghiệm thức.

## Đọc đồ thị enzyme cho đúng

Đồ thị $v$ theo $[S]$ là hyperbol Michaelis-Menten: $v=\dfrac{V_{\max}[S]}{K_M+[S]}$. Đọc $K_M$ là nồng độ cơ chất cho $v=V_{\max}/2$ — nhưng $V_{\max}$ trên hyperbol chỉ tiếp cận tiệm cận, khó đọc chính xác. Vì thế phải **tuyến tính hoá** bằng Lineweaver-Burk.

Phân biệt kiểu ức chế trên đồ thị nghịch đảo kép:

- **Cạnh tranh**: cùng tung độ gốc ($V_{\max}$ không đổi), hệ số góc tăng ($K_M$ tăng).
- **Không cạnh tranh**: cùng hoành độ gốc ($K_M$ không đổi), tung độ gốc tăng ($V_{\max}$ giảm).
- **Phi cạnh tranh (uncompetitive)**: hai đường **song song**.

Đây là câu hỏi xuất hiện gần như mọi kỳ IBO.

## Đường cong phân li oxygen

Dạng sigmoid do hợp tác giữa bốn tiểu đơn vị. Dịch **sang phải** (hiệu ứng Bohr) khi $CO_2$ tăng, pH giảm, nhiệt độ tăng, hoặc 2,3-BPG tăng — nghĩa là ái lực giảm, nhả oxygen dễ hơn ở mô hoạt động. Hemoglobin thai nhi và myoglobin nằm **bên trái** vì ái lực cao hơn.

**Lỗi thường gặp:**
- Đọc $V_{\max}$ trực tiếp từ đồ thị hyperbol — sai vì đường cong chỉ tiệm cận tới $V_{\max}$ mà không bao giờ đạt; giá trị đọc bằng mắt luôn thấp hơn thật, phải tuyến tính hoá.
- Nói 'dịch phải làm hemoglobin gắn oxygen tốt hơn' — sai vì dịch phải nghĩa là ở cùng áp suất riêng phần oxygen, độ bão hoà THẤP hơn, tức ái lực GIẢM và nhả oxygen dễ hơn.
- Kết luận yếu tố trên trục hoành vẫn giới hạn ở đoạn đồ thị nằm ngang — sai vì đoạn bão hoà cho thấy tăng yếu tố đó không làm tăng tốc độ nữa; lúc này một yếu tố khác mới là yếu tố giới hạn.

<sub>`lesson.biology.ibo.suy-luan-tu-do-thi-sinh-hoc`</sub>

---

### 3. Bài toán di truyền phức tạp: từ tỉ lệ phân li tới cơ chế
*Complex genetics problems: from ratios to mechanisms* · THPT (lớp 10-12) · olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Suy ra được kiểu tương tác gen từ tỉ lệ phân li kiểu hình ở đời con
- Tính được tần số hoán vị gen và lập được bản đồ di truyền ba điểm
- Vận dụng được kiểm định chi bình phương để kiểm tra một mô hình di truyền

## Đọc tỉ lệ như đọc dấu vân tay

Bảng tra nhanh cho phép lai $F_1\times F_1$ dị hợp hai cặp gen (tổng 16 phần):

| Tỉ lệ | Cơ chế |
|---|---|
| 9:3:3:1 | phân li độc lập, không tương tác |
| 9:7 | bổ sung — cần cả hai gen trội |
| 9:6:1 | bổ sung — hai gen trội riêng cho cùng kiểu hình |
| 9:3:4 | át chế lặn |
| 12:3:1 | át chế trội |
| 13:3 | át chế trội (dạng khác) |
| 15:1 | cộng gộp |
| 1:2:1 | trội không hoàn toàn hoặc gen gây chết |
| 3:1 thay vì 9:3:3:1 | hai gen liên kết hoàn toàn |

Mẹo: **luôn quy tổng về 16** (hoặc 4 với một cặp gen). Nếu tổng không quy về 16 được, nghĩ tới gen gây chết hoặc liên kết gen.

## Quy trình giải bài lai

1. Đếm số kiểu hình và quy tỉ lệ về dạng chuẩn.
2. Đối chiếu bảng $\Rightarrow$ đoán mô hình.
3. Viết kiểu gen của bố mẹ theo mô hình, dự đoán tỉ lệ.
4. **Kiểm định chi bình phương** để xác nhận mô hình: $\chi^2=\sum\dfrac{(O-E)^2}{E}$, bậc tự do $=$ số lớp $-1$.
5. Nếu $\chi^2$ vượt giá trị tới hạn, bác bỏ mô hình và quay lại bước 2.

## Lập bản đồ ba điểm

Từ phép lai phân tích cá thể dị hợp ba cặp gen:

1. Hai lớp **nhiều nhất** là kiểu bố mẹ.
2. Hai lớp **ít nhất** là trao đổi chéo kép.
3. So sánh lớp trao đổi kép với lớp bố mẹ: gen nào **đổi vị trí** là gen nằm **ở giữa**.
4. Khoảng cách giữa hai gen $=$ (số tái tổ hợp đơn giữa chúng $+$ số trao đổi kép) chia tổng số, nhân 100.
5. Hệ số trùng hợp $=\dfrac{\text{số kép quan sát}}{\text{số kép kì vọng}}$; nhiễu $=1-$ hệ số trùng hợp.

## Sai lầm cần tránh về khoảng cách

Tần số tái tổ hợp quan sát được **bão hoà ở 50%** dù hai gen cách xa bao nhiêu. Vì vậy hai gen trên cùng nhiễm sắc thể nhưng rất xa nhau biểu hiện y hệt hai gen phân li độc lập. Muốn chứng minh chúng cùng nhiễm sắc thể phải dùng gen trung gian.

**Lỗi thường gặp:**
- Cộng thẳng tần số tái tổ hợp của hai khoảng liền kề để ra khoảng cách hai đầu — sai vì trao đổi chéo kép làm cá thể trở lại kiểu bố mẹ nên không được đếm; phải cộng thêm hai lần số kép.
- Kết luận hai gen phân li độc lập khi tần số tái tổ hợp bằng 50% — sai vì hai gen rất xa nhau trên CÙNG nhiễm sắc thể cũng cho 50%; cần gen trung gian để phân biệt.
- Dùng kiểm định chi bình phương với số bậc tự do bằng số lớp — sai vì mất một bậc do tổng số cá thể đã cố định; bậc tự do đúng là số lớp trừ 1 (trừ thêm nếu có tham số ước lượng từ chính dữ liệu).

<sub>`lesson.biology.ibo.bai-toan-di-truyen-phuc-tap`</sub>

---

### 4. Thống kê sinh học ứng dụng: chọn đúng kiểm định và đọc đúng kết quả
*Applied biostatistics: choosing and interpreting tests* · THPT (lớp 10-12) · olympiad · 50 phút · nang-cao

**Mục tiêu:**
- Chọn được kiểm định thống kê phù hợp với loại dữ liệu và câu hỏi nghiên cứu
- Giải thích được ý nghĩa của giá trị p ở ngưỡng ý nghĩa 0,05
- Phân biệt được ý nghĩa thống kê và ý nghĩa sinh học

## Cây quyết định chọn kiểm định

| Câu hỏi | Loại dữ liệu | Kiểm định |
|---|---|---|
| Hai trung bình có khác nhau không? | định lượng, hai nhóm độc lập | kiểm định t hai mẫu |
| Ba nhóm trở lên? | định lượng | ANOVA một yếu tố |
| Tỉ lệ quan sát có khớp tỉ lệ lí thuyết không? | đếm, phân loại | chi bình phương phù hợp |
| Hai biến phân loại có liên quan không? | bảng chéo | chi bình phương độc lập |
| Hai biến định lượng có tương quan không? | định lượng, phân phối chuẩn | hệ số Pearson |
| Tương quan hạng (dữ liệu thứ bậc) | thứ bậc | hệ số Spearman |

## Quy trình năm bước bắt buộc

1. Phát biểu $H_0$ và $H_1$ bằng lời, cụ thể cho bối cảnh sinh học.
2. Chọn kiểm định và **nêu lí do chọn**.
3. Tính thống kê kiểm định.
4. Tính bậc tự do và tra giá trị tới hạn ở $\alpha=0{,}05$.
5. So sánh và kết luận **bằng ngôn ngữ sinh học**, không chỉ nói "bác bỏ $H_0$".

## Bậc tự do - chỗ hay sai nhất

- Chi bình phương phù hợp: $df=$ số lớp $-1$; trừ thêm 1 cho mỗi tham số ước lượng từ dữ liệu (ví dụ kiểm định Hardy-Weinberg: $df=$ số kiểu gen $-$ số alen).
- Chi bình phương độc lập bảng $r\times c$: $df=(r-1)(c-1)$.
- Kiểm định t hai mẫu độc lập: $df=n_1+n_2-2$.

## Diễn giải đúng giá trị p

$p$ **không** phải xác suất giả thuyết không đúng, cũng **không** phải độ lớn của hiệu ứng. Nó chỉ nói: nếu $H_0$ đúng thì khả năng thấy dữ liệu cực đoan thế này là bao nhiêu.

Hệ quả thực dụng: với cỡ mẫu rất lớn, một khác biệt sinh học không đáng kể vẫn cho $p<0{,}05$. Vì vậy IBO luôn hỏi thêm: khác biệt đó có **ý nghĩa sinh học** không? Hãy báo cáo cả **độ lớn hiệu ứng** (chênh lệch trung bình, tỉ số) chứ không chỉ $p$.

## Đọc thanh sai số nhanh

Nếu hai khoảng $\pm2\,SE$ **không chồng lấn**, khác biệt gần như chắc chắn có ý nghĩa ở mức 0,05. Nếu chồng lấn nhiều, gần như chắc chắn không. Vùng chồng lấn nhẹ thì phải tính thật.

**Lỗi thường gặp:**
- Nói 'p lớn nên đã chứng minh giả thuyết không đúng' — sai vì kiểm định chỉ có thể BÁC BỎ; không bác bỏ được chỉ nghĩa là dữ liệu chưa đủ mạnh, không phải bằng chứng cho sự bằng nhau.
- Chạy chi bình phương trên tỉ lệ phần trăm thay vì số đếm thô — sai vì thống kê chi bình phương phụ thuộc cỡ mẫu; quy về 100 làm mất thông tin cỡ mẫu và cho giá trị hoàn toàn khác.
- Kết luận có ý nghĩa sinh học chỉ vì $p<0{,}05$ — sai vì với cỡ mẫu lớn, khác biệt cực nhỏ cũng đạt ý nghĩa thống kê; phải báo cáo thêm độ lớn hiệu ứng.

<sub>`lesson.biology.ibo.thong-ke-sinh-hoc-ung-dung`</sub>

---

### 5. Chiến lược làm câu trắc nghiệm nhiều đáp án đúng của IBO
*Strategy for IBO multiple-true-false questions* · THPT (lớp 10-12) · olympiad · 40 phút · trung-binh

**Mục tiêu:**
- Phân tích được cấu trúc chấm điểm của dạng câu nhiều mệnh đề đúng sai
- Vận dụng được kỹ thuật xét từng mệnh đề độc lập thay vì so sánh các phương án
- Xác định được các từ tuyệt đối và từ định lượng làm thay đổi giá trị chân lí của mệnh đề

## Cấu trúc đề IBO và hệ quả về chiến thuật

Phần lí thuyết IBO gồm nhiều câu, mỗi câu có 4 mệnh đề A, B, C, D và thí sinh đánh dấu đúng/sai cho **từng mệnh đề**. Điểm tính theo số mệnh đề trả lời chính xác, thường có ngưỡng: trả lời đúng cả 4 mới được điểm tối đa, sai một vẫn còn điểm phần.

Hệ quả quan trọng: **không có phương án nào để loại trừ lẫn nhau**. Kỹ thuật "chọn đáp án hợp lí nhất" của trắc nghiệm bốn lựa chọn hoàn toàn vô dụng ở đây. Mỗi mệnh đề là một câu hỏi độc lập.

## Quy trình xử lí một mệnh đề

1. **Che các mệnh đề khác lại.** Đọc mệnh đề đang xét như một khẳng định riêng.
2. **Gạch chân từ định lượng và từ tuyệt đối.** "tất cả", "chỉ", "luôn", "không bao giờ", "tăng", "giảm", "cần thiết".
3. **Tìm một phản ví dụ.** Sinh học đầy ngoại lệ; nếu nghĩ ra được một trường hợp trái, mệnh đề sai.
4. **Kiểm tra chiều nhân quả.** Nhiều mệnh đề sai chỉ vì đảo ngược nguyên nhân và kết quả.

## Bảng từ khoá cảnh báo

| Từ trong mệnh đề | Xác suất mệnh đề sai |
|---|---|
| luôn luôn, mọi, không bao giờ, chỉ duy nhất | cao |
| thường, có thể, phần lớn, một số | thấp |
| tỉ lệ thuận, tỉ lệ nghịch | trung bình — phải kiểm tra định lượng |
| tăng gấp đôi, giảm một nửa | phải tính, không đoán |

## Chiến thuật thời gian và rủi ro

- Nếu không bị trừ điểm khi sai: **trả lời hết**, không bỏ trống mệnh đề nào.
- Nếu có trừ điểm: chỉ trả lời khi độ tự tin trên khoảng 60%.
- Phân bổ thời gian đều; đánh dấu câu nghi ngờ để quay lại, đừng dừng quá lâu ở một mệnh đề.
- Với mệnh đề dựa trên đồ thị hoặc bảng đi kèm, hãy **đọc dữ liệu trước, đọc mệnh đề sau** để tránh bị dẫn dắt.

## Sai lầm tâm lí phổ biến

Thấy ba mệnh đề đầu đều đúng rồi đoán mệnh đề thứ tư phải sai "cho cân đối". Không có quy luật cân đối nào; cả bốn mệnh đề đều đúng hoặc đều sai là chuyện bình thường.

**Lỗi thường gặp:**
- So sánh các mệnh đề với nhau để chọn 'cái đúng nhất' — sai vì mỗi mệnh đề được chấm độc lập; không có ràng buộc nào bắt đúng một mệnh đề phải đúng.
- Bỏ qua từ tuyệt đối khi đọc nhanh — sai vì một chữ 'mọi' hay 'luôn' đủ biến mệnh đề đúng thành sai; sinh học hầu như luôn có ngoại lệ đáng kể.
- Đoán mệnh đề cuối phải sai vì ba mệnh đề đầu đã đúng — sai vì đề thi không thiết kế theo tỉ lệ cân đối; phân bố đúng sai trong một câu là hoàn toàn tự do.

<sub>`lesson.biology.ibo.chien-luoc-trac-nghiem-nhieu-dap-an`</sub>

---

## Unit 9: Kĩ năng thống kê và thực hành (IB/A-Level Practical Skills)

### 1. Thiết kế thí nghiệm có kiểm soát biến và xử lí sai số
*Designing controlled experiments and handling measurement uncertainty* · THPT (lớp 10-12) · ib, a-level, ap · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được biến độc lập, biến phụ thuộc và biến kiểm soát trong một thiết kế thí nghiệm
- Phân biệt được sai số hệ thống và sai số ngẫu nhiên cùng cách khắc phục mỗi loại
- Tính được phần trăm độ không đảm bảo đo của một phép đo tổ hợp

## Ba loại biến — nền tảng của mọi thiết kế

- **Biến độc lập**: đại lượng người làm thí nghiệm chủ động thay đổi (nồng độ cơ chất, nhiệt độ, pH).
- **Biến phụ thuộc**: đại lượng được đo để phản ánh kết quả (thể tích khí, độ hấp thụ, thời gian).
- **Biến kiểm soát**: mọi đại lượng khác có thể ảnh hưởng, phải giữ không đổi.

Một thiết kế thiếu kiểm soát biến sẽ cho kết quả **không diễn giải được**, vì không thể biết thay đổi quan sát được do đâu. Ví dụ: khảo sát ảnh hưởng của nhiệt độ tới hoạt tính catalase mà không cố định pH và nồng độ enzyme thì mọi kết luận đều vô nghĩa.

## Đối chứng: hai kiểu

- **Đối chứng âm**: thiếu yếu tố khảo sát, kì vọng không có đáp ứng. Ví dụ đun sôi enzyme rồi làm thí nghiệm — nếu vẫn có bọt khí thì bọt đó không do enzyme.
- **Đối chứng dương**: chắc chắn cho đáp ứng, dùng để chứng minh hệ đo đang hoạt động. Thiếu bước này, kết quả 'không có phản ứng' có thể chỉ là do máy hỏng.

## Sai số: hai loại, hai cách chữa

| | Sai số hệ thống | Sai số ngẫu nhiên |
|---|---|---|
| Đặc điểm | Luôn lệch một chiều | Lệch hai chiều quanh giá trị thật |
| Nguyên nhân | Dụng cụ chưa chuẩn, đọc lệch mắt cố định | Dao động không kiểm soát được |
| Ảnh hưởng | Sai **độ chính xác** (accuracy) | Sai **độ chụm** (precision) |
| Cách chữa | Hiệu chuẩn dụng cụ, sửa phương pháp | **Lặp lại nhiều lần** rồi lấy trung bình |

Đây là điểm phân biệt then chốt: lặp lại phép đo giảm được sai số ngẫu nhiên nhưng **hoàn toàn không** giảm sai số hệ thống — cân lệch 2 g thì đo 100 lần vẫn lệch 2 g.

## Độ không đảm bảo đo

Với dụng cụ chia độ, độ không đảm bảo thường lấy bằng nửa vạch chia nhỏ nhất. Phần trăm độ không đảm bảo:

$$\%u = \frac{\text{độ không đảm bảo tuyệt đối}}{\text{giá trị đo}} \times 100\%$$

Quy tắc lan truyền cần nhớ: khi **cộng hoặc trừ** hai đại lượng thì cộng độ không đảm bảo **tuyệt đối**; khi **nhân hoặc chia** thì cộng độ không đảm bảo **phần trăm**. Hệ quả thực hành quan trọng: đo một hiệu số nhỏ giữa hai giá trị lớn (ví dụ khối lượng trước và sau khi ngâm) luôn cho phần trăm sai số rất lớn, nên phải chọn mẫu có thay đổi đủ rõ.

**Lỗi thường gặp:**
- Nghĩ lặp lại phép đo nhiều lần sẽ khắc phục được mọi sai số — sai, lặp lại chỉ giảm sai số ngẫu nhiên; sai số hệ thống do dụng cụ chưa hiệu chuẩn vẫn giữ nguyên độ lớn và chiều ở mọi lần đo.
- Cộng độ không đảm bảo phần trăm khi thực hiện phép trừ — sai, quy tắc đúng là cộng độ không đảm bảo **tuyệt đối** khi cộng/trừ và cộng **phần trăm** khi nhân/chia; làm ngược sẽ đánh giá sai mức tin cậy của kết quả.
- Bỏ qua đối chứng vì 'kết quả đã rõ ràng' — sai, không có đối chứng thì không loại trừ được các nguyên nhân khác; ví dụ bọt khí trong thí nghiệm catalase có thể đến từ chính sự phân huỷ tự phát của $\text{H}_2\text{O}_2$.

<sub>`lesson.biology.ki-nang-thong-ke-sinh-hoc.thiet-ke-thi-nghiem-kiem-soat-bien`</sub>

---

### 2. Thống kê mô tả: độ lệch chuẩn, sai số chuẩn và khoảng tin cậy
*Descriptive statistics: standard deviation, standard error and confidence intervals* · THPT (lớp 10-12) · ib, a-level, ap · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được độ lệch chuẩn và sai số chuẩn theo đại lượng mà mỗi cái mô tả
- Tính được khoảng tin cậy 95% dạng hai lần sai số chuẩn và vẽ được thanh sai số
- Diễn giải được mức chồng lấn của thanh sai số để rút ra kết luận sơ bộ

## Hai câu hỏi khác nhau, hai đại lượng khác nhau

Đây là chỗ nhầm lẫn phổ biến nhất trong bài thực hành IB và A-Level.

- **Độ lệch chuẩn $s$** trả lời: *các cá thể trong quần thể khác nhau nhiều hay ít?* Nếu quần thể vốn biến dị lớn, $s$ lớn — và đo thêm 1000 cá thể nữa cũng không làm nó nhỏ đi.
- **Sai số chuẩn $SE$** trả lời: *ta tin tưởng đến đâu vào con số trung bình vừa tính được?* Đo càng nhiều thì càng tin, nên $SE = s/\sqrt{n}$ giảm khi $n$ tăng.

Hệ quả thực tế: dấu $\sqrt{n}$ cho biết muốn giảm một nửa sai số chuẩn phải tăng cỡ mẫu lên **bốn lần** — quy luật lợi ích giảm dần, rất đáng cân nhắc khi lập kế hoạch thí nghiệm.

## Quy tắc 68 - 95

Với phân bố chuẩn: khoảng $\bar{x} \pm s$ chứa khoảng 68% số cá thể; khoảng $\bar{x} \pm 2s$ chứa khoảng 95%. Chú ý đây là phát biểu về **cá thể**, dùng $s$ chứ không dùng $SE$.

Khoảng tin cậy 95% của **trung bình** thì dùng $SE$: $\bar{x} \pm 2SE$.

## Đọc thanh sai số

Quy tắc thực hành được cả IB và A-Level dùng:

- Thanh sai số (vẽ theo $\pm 2SE$) của hai nhóm **không chồng lấn** → khác biệt gần như chắc chắn có ý nghĩa thống kê; nên tiến hành kiểm định t để khẳng định.
- Thanh sai số **chồng lấn nhiều** → không đủ bằng chứng kết luận có khác biệt.
- Chồng lấn ít → không kết luận được bằng mắt, bắt buộc phải kiểm định.

Luôn ghi rõ thanh sai số biểu diễn $s$, $SE$ hay khoảng tin cậy — cùng một bộ số liệu vẽ theo $s$ sẽ cho thanh dài hơn nhiều lần so với vẽ theo $SE$, dẫn tới kết luận trái ngược.

## Hệ số biến thiên

Khi so sánh mức biến dị giữa hai đại lượng có đơn vị hoặc độ lớn khác nhau (chiều dài lá tính bằng cm với khối lượng hạt tính bằng mg), không so sánh $s$ trực tiếp được. Dùng $CV = \dfrac{s}{\bar{x}} \times 100\%$ — đại lượng không thứ nguyên nên so sánh được.

**Lỗi thường gặp:**
- Dùng độ lệch chuẩn để vẽ thanh sai số rồi kết luận về khác biệt giữa hai trung bình — sai, $s$ mô tả phân tán của **cá thể** còn kết luận về trung bình phải dựa trên $SE$; nhầm lẫn này thường dẫn tới kết luận 'không có khác biệt' một cách sai lầm.
- Chia cho $n$ thay vì $n-1$ khi tính độ lệch chuẩn mẫu — sai, chia cho $n$ cho ước lượng chệch thấp hơn giá trị thật; bậc tự do bị mất một vì trung bình mẫu đã được ước lượng từ chính dữ liệu đó.
- So sánh trực tiếp độ lệch chuẩn của hai đại lượng khác đơn vị hoặc khác độ lớn — sai, phải dùng hệ số biến thiên $CV = s/\bar{x}$ vì $s$ mang đơn vị và tỉ lệ theo độ lớn của đại lượng.

<sub>`lesson.biology.ki-nang-thong-ke-sinh-hoc.thong-ke-mo-ta-sai-so-chuan-khoang-tin-cay`</sub>

---

### 3. Kiểm định chi bình phương trong di truyền và sinh thái
*The chi-square test in genetics and ecology* · THPT (lớp 10-12) · ib, a-level, ap · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu được giả thuyết không phù hợp cho một bài toán chi bình phương
- Tính được giá trị chi bình phương và xác định đúng số bậc tự do
- Diễn giải được kết quả so với giá trị tới hạn ở mức ý nghĩa 0,05

## Vấn đề: bao nhiêu lệch thì gọi là lệch

Lai $Aa \times Aa$ kì vọng 3:1. Thu được 74 trội : 26 lặn trên 100 cây — có phải bằng chứng chống lại quy luật Mendel không? Rõ ràng không, vì mọi thí nghiệm đều có dao động ngẫu nhiên. Nhưng 60:40 thì sao? Cần một tiêu chí khách quan.

## Công thức và quy trình

$$\chi^2 = \sum \frac{(O - E)^2}{E}$$

với $O$ là số **quan sát** và $E$ là số **kì vọng**. Chú ý: luôn dùng **số lượng cá thể**, tuyệt đối không dùng tỉ lệ phần trăm.

Sáu bước bắt buộc:

1. Phát biểu $H_0$: 'số liệu quan sát phù hợp với tỉ lệ lí thuyết X, sai khác chỉ do ngẫu nhiên'.
2. Tính $E$ cho từng lớp từ tỉ lệ lí thuyết và tổng số cá thể.
3. Tính $\chi^2$.
4. Xác định bậc tự do: kiểm định phù hợp $df = k - 1$ với $k$ là số lớp.
5. Tra giá trị tới hạn ở $p = 0{,}05$ (df = 1 → 3,84; df = 2 → 5,99; df = 3 → 7,81).
6. So sánh: $\chi^2 \ge$ giá trị tới hạn → **bác bỏ** $H_0$; $\chi^2 <$ giá trị tới hạn → **không đủ bằng chứng bác bỏ** $H_0$.

## Diễn giải cho đúng

Hai điểm hay bị nói sai:

- Khi $\chi^2$ nhỏ, kết luận đúng là 'không đủ bằng chứng để bác bỏ $H_0$', **không** phải 'đã chứng minh $H_0$ đúng'. Kiểm định thống kê không bao giờ chứng minh một giả thuyết.
- $p < 0{,}05$ nghĩa là: *nếu* $H_0$ đúng thì xác suất thu được sai lệch lớn như quan sát (hoặc lớn hơn) là dưới 5%. Nó **không** phải xác suất $H_0$ sai.

## Hai ứng dụng chuẩn

- **Di truyền**: kiểm tra tỉ lệ phân li (3:1, 9:3:3:1, 1:1:1:1). Nếu phép lai hai cặp gen cho $\chi^2$ lớn so với kì vọng 9:3:3:1, giả thuyết phân li độc lập bị bác bỏ và ta nghĩ tới **liên kết gen**.
- **Sinh thái**: kiểm tra tính liên kết giữa hai loài, hoặc phân bố cá thể theo sinh cảnh, dùng bảng liên hợp với $df = (r-1)(c-1)$.

**Điều kiện áp dụng**: dữ liệu là tần số đếm được, các lớp loại trừ nhau, và mọi giá trị kì vọng nên $\ge 5$. Nếu có lớp $E < 5$ thì phải gộp lớp, nếu không giá trị $\chi^2$ bị phóng đại.

**Lỗi thường gặp:**
- Đưa tỉ lệ phần trăm vào công thức thay vì số lượng cá thể — sai, vì $\chi^2$ phụ thuộc cỡ mẫu: cùng một tỉ lệ lệch nhưng thu 40 cá thể hay 4000 cá thể cho mức bằng chứng hoàn toàn khác nhau, dùng phần trăm sẽ xoá mất thông tin đó.
- Kết luận 'đã chứng minh giả thuyết đúng' khi $\chi^2$ nhỏ — sai, kiểm định chỉ cho phép bác bỏ hoặc không bác bỏ; không bác bỏ nghĩa là dữ liệu tương thích với $H_0$, chứ không loại trừ các giả thuyết khác cũng tương thích.
- Lấy bậc tự do bằng số lớp — sai, phải trừ đi 1 vì khi tổng đã cố định thì lớp cuối cùng được xác định bởi các lớp trước; lấy df quá lớn sẽ dùng giá trị tới hạn cao hơn và dễ bỏ sót khác biệt thật.

<sub>`lesson.biology.ki-nang-thong-ke-sinh-hoc.kiem-dinh-chi-binh-phuong`</sub>

---

### 4. Kiểm định t hai mẫu độc lập và hệ số tương quan Spearman
*Independent-samples t-test and Spearman rank correlation* · THPT (lớp 10-12) · ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Chọn được kiểm định thống kê phù hợp với loại dữ liệu và câu hỏi nghiên cứu
- Vận dụng được kiểm định t hai mẫu độc lập và diễn giải đúng kết quả thu được
- Tính được hệ số tương quan hạng Spearman và phân biệt tương quan với nhân quả

## Chọn kiểm định nào

| Câu hỏi | Loại dữ liệu | Kiểm định |
|---|---|---|
| Tần số quan sát có khớp tỉ lệ kì vọng không? | Đếm theo lớp | Chi bình phương |
| Hai nhóm có trung bình khác nhau không? | Liên tục, phân bố chuẩn | Kiểm định t |
| Hai biến có liên hệ với nhau không? | Liên tục, quan hệ tuyến tính | Tương quan Pearson |
| Hai biến có liên hệ đơn điệu không? | Thứ hạng hoặc không chuẩn | Tương quan Spearman |

Chọn sai kiểm định là lỗi nặng trong bài IA của IB và Paper 5 của A-Level, kể cả khi tính toán chính xác.

## Kiểm định t

$$t = \frac{|\bar{x}_1 - \bar{x}_2|}{\sqrt{\dfrac{s_1^2}{n_1} + \dfrac{s_2^2}{n_2}}}, \qquad df = n_1 + n_2 - 2$$

Cấu trúc công thức nói lên tất cả: tử số là **tín hiệu** (khác biệt giữa hai nhóm), mẫu số là **nhiễu** (mức dao động do lấy mẫu). $t$ lớn nghĩa là tín hiệu lấn át nhiễu.

So $t$ tính được với giá trị tới hạn ở $p = 0{,}05$ và đúng bậc tự do: $t \ge t_{\text{tới hạn}}$ → bác bỏ $H_0$, kết luận có khác biệt có ý nghĩa thống kê.

## Tương quan Spearman

$$r_s = 1 - \frac{6\sum d^2}{n(n^2 - 1)}$$

với $d$ là hiệu hai thứ hạng của cùng một cá thể. Ưu điểm so với Pearson: không đòi hỏi phân bố chuẩn, không đòi hỏi quan hệ tuyến tính (chỉ cần đơn điệu), và ít bị ảnh hưởng bởi giá trị ngoại lai — đúng những đặc điểm hay gặp ở số liệu sinh thái thực địa.

Diễn giải độ lớn: $|r_s|$ từ 0,0-0,3 là yếu, 0,3-0,7 là trung bình, trên 0,7 là mạnh; dấu cho biết chiều thuận hay nghịch.

## Cảnh báo quan trọng nhất

Tương quan **không** chứng minh nhân quả. Ba cách giải thích luôn phải xét: (1) A gây ra B; (2) B gây ra A; (3) một biến thứ ba C gây ra cả hai. Ví dụ kinh điển trong sinh thái: độ ẩm đất và số lượng giun tương quan mạnh, nhưng cũng có thể do cả hai cùng phụ thuộc hàm lượng chất hữu cơ. Chỉ thí nghiệm có kiểm soát mới tách được các khả năng này.

**Lỗi thường gặp:**
- Dùng kiểm định t cho dữ liệu đếm theo lớp (số cá thể mỗi kiểu hình) — sai, dữ liệu tần số phải dùng chi bình phương; kiểm định t đòi hỏi biến liên tục đo được trên từng cá thể.
- Tính bậc tự do của kiểm định t hai mẫu bằng $n_1 + n_2 - 1$ — sai, phải trừ 2 vì đã ước lượng **hai** trung bình từ dữ liệu; dùng df sai dẫn tới tra nhầm giá trị tới hạn.
- Kết luận nhân quả từ hệ số tương quan lớn — sai, tương quan mạnh vẫn tương thích với chiều nhân quả ngược lại hoặc với một biến gây nhiễu thứ ba; chỉ thí nghiệm có kiểm soát biến mới xác lập được nhân quả.

<sub>`lesson.biology.ki-nang-thong-ke-sinh-hoc.kiem-dinh-t-va-tuong-quan-spearman`</sub>

---

## Unit 1: Hoá sinh - cấu trúc protein và động học enzyme

### 1. Cấu trúc bốn bậc của protein và các lực ổn định
*Four levels of protein structure and the stabilising forces* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân tích được vai trò của liên kết peptide phẳng và hai góc xoay $\phi, \psi$ trong việc giới hạn không gian cấu hình
- Giải thích được vì sao xoắn $\alpha$ và phiến $\beta$ là hai motif chiếm ưu thế trong protein cầu
- Xác định được các lực không cộng hoá trị ổn định cấu trúc bậc ba và đánh giá đóng góp tương đối của chúng

## Bài toán: một chuỗi, một cấu trúc

Một chuỗi 150 gốc amino acid về nguyên tắc có số cấu hình khổng lồ, nhưng trong tế bào nó gấp thành **một** cấu trúc xác định trong vài trăm mili giây. Muốn hiểu vì sao, phải bắt đầu từ những ràng buộc hình học của chính bộ khung.

## Bậc một và ràng buộc của liên kết peptide

Cấu trúc bậc một là trình tự gốc amino acid theo chiều N đến C. Liên kết peptide có đặc tính liên kết đôi một phần nên **không quay tự do**: sáu nguyên tử $C_\alpha - C(=O) - N(H) - C_\alpha$ đồng phẳng. Chỉ còn hai góc quay tự do quanh mỗi $C_\alpha$ là $\phi$ và $\psi$. Va chạm không gian loại bỏ phần lớn mặt phẳng $(\phi,\psi)$, chỉ chừa lại các vùng hẹp trên đồ thị Ramachandran — chính là các vùng ứng với xoắn $\alpha$ và phiến $\beta$.

## Bậc hai: xoắn và phiến

Xoắn $\alpha$ phải là 3,6 gốc một vòng vì đó là bước xoắn cho phép nhóm $C=O$ của gốc $i$ tạo liên kết hydrogen với nhóm $N-H$ của gốc $i+4$ mà không căng. Phiến $\beta$ thì tạo liên kết hydrogen **giữa các đoạn chuỗi** ở xa nhau trong trình tự. Điểm chung: cả hai đều nhằm bão hoà các nhóm phân cực của bộ khung khi chúng bị chôn vào lõi không có nước.

## Bậc ba và bậc bốn

Cấu trúc bậc ba do bốn nhóm lực giữ: hiệu ứng kị nước (đóng góp lớn nhất), liên kết hydrogen, cầu muối và lực van der Waals; cầu disulfide chỉ phổ biến ở protein ngoại bào vì bào tương là môi trường khử. Bậc bốn là cách nhiều tiểu đơn vị lắp lại, và chỉ khi có bậc bốn mới có hiện tượng hợp tác giữa các tâm gắn.

## Giới hạn của mô hình

Không phải protein nào cũng có cấu trúc xác định: khoảng 30% protein người chứa vùng nội tại vô trật tự, chỉ gấp khi gặp đối tác. Với những protein đó, "trình tự quy định cấu trúc" phải hiểu là trình tự quy định một tập hợp cấu hình chứ không phải một cấu trúc duy nhất.

**Lỗi thường gặp:**
- Nói rằng lõi kị nước hình thành vì các gốc không phân cực hút nhau. Sai về bản chất động lực: đóng góp chính là entropy của nước — nước quanh bề mặt kị nước bị sắp xếp trật tự, khi các gốc kị nước gom lại thì lượng nước bị trói này được giải phóng, entropy hệ tăng.
- Cho rằng cầu disulfide là lực chính giữ cấu trúc bậc ba của mọi protein. Thực tế bào tương có glutathione ở dạng khử nên cầu disulfide gần như không tồn tại bền trong protein nội bào; nó chỉ phổ biến ở protein tiết và protein màng ngoài.
- Đồng nhất "cấu trúc bậc bốn" với "protein lớn". Bậc bốn được định nghĩa bằng việc có từ hai chuỗi polypeptide riêng biệt lắp với nhau; một chuỗi đơn dài 2000 gốc vẫn chỉ có tới bậc ba.

<sub>`lesson.biology.hoa-sinh.cau-truc-protein`</sub>

---

### 2. Gấp cuộn protein, chaperone và bệnh do gấp cuộn sai
*Protein folding, chaperones and misfolding diseases* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được nghịch lí Levinthal và cách mô hình phễu năng lượng giải quyết nó
- Phân tích được đường cong biến tính hai trạng thái để rút ra $\Delta G$ ổn định và $T_m$
- Giải thích được cơ chế chung của bệnh amyloid dựa trên động học tạo nhân

## Nghịch lí Levinthal

Nếu mỗi gốc chỉ có 3 cấu hình thì chuỗi 100 gốc có $3^{100}\approx 5\times10^{47}$ cấu hình. Dò tuần tự với tốc độ picogiây mỗi cấu hình sẽ mất lâu hơn tuổi vũ trụ, trong khi thực nghiệm cho thấy protein gấp trong mili giây. Kết luận: protein **không** dò ngẫu nhiên.

## Phễu năng lượng

Cách giải là bề mặt năng lượng có dạng phễu: mỗi tiếp xúc gốc đúng vừa hạ enthalpy vừa thu hẹp không gian cấu hình còn lại, nên đường đi tự thu hẹp dần. Có nhiều lộ trình song song, không có "con đường duy nhất".

## Đo độ bền bằng biến tính hai trạng thái

Thêm urea hay tăng nhiệt độ, theo dõi tín hiệu CD hay huỳnh quang, ta thu được phần biến tính $f_U$. Nếu chỉ có hai trạng thái thì

$$K = \frac{f_U}{1-f_U}, \qquad \Delta G = -RT\ln K$$

Ngoại suy $\Delta G$ về nồng độ chất biến tính bằng 0 cho $\Delta G_{H_2O}$, thường chỉ 20-60 kJ/mol — bằng vài liên kết hydrogen. Protein là cấu trúc **bền vừa đủ**, không phải bền tuyệt đối, và điều đó là cần thiết để chúng còn linh động mà hoạt động.

## Khi gấp cuộn hỏng

Bề mặt kị nước lộ ra của chuỗi chưa gấp xong dễ dính vào nhau. Chaperone Hsp70 và lồng chaperonin GroEL/GroES ngăn điều này bằng cách cô lập chuỗi. Khi hệ thống quá tải, protein chuyển sang trạng thái giàu phiến $\beta$ xếp chồng, tạo sợi amyloid. Động học của quá trình này có pha trễ vì cần tạo nhân; một khi có mầm thì sợi kéo dài nhanh và tự nhân lên — đây là lí do các bệnh Alzheimer, Parkinson, prion đều khởi phát muộn rồi tiến triển nhanh.

## Ranh giới áp dụng

Phân tích $\Delta G$ hai trạng thái chỉ hợp lệ khi đường cong biến tính theo dõi bằng hai kĩ thuật khác nhau trùng nhau. Nếu lệch, có trung gian tích tụ và mọi giá trị $\Delta G$ tính theo hai trạng thái đều sai lệch.

**Lỗi thường gặp:**
- Hiểu "chaperone giúp protein gấp đúng" thành "chaperone chỉ ra cấu trúc đích". Sai vì chaperone không mang thông tin cấu trúc; nó chỉ ngăn các con đường kết tụ, còn thông tin cấu trúc vẫn nằm trong trình tự.
- Cho rằng protein bền vì $\Delta G$ lớn. Thực tế $\Delta G_{H_2O}$ chỉ cỡ vài chục kJ/mol vì đây là **hiệu** của hai số hạng rất lớn gần triệt tiêu nhau (tổng tương tác thuận lợi và mất entropy cấu hình); nhầm lẫn này khiến ước lượng ảnh hưởng của một đột biến điểm bị đánh giá thấp.
- Coi sợi amyloid là sản phẩm của protein bị "phân huỷ". Ngược lại, amyloid là một trạng thái gấp cuộn có trật tự cao và thường bền nhiệt động hơn cả trạng thái tự nhiên; rào cản chỉ là động học tạo nhân.

<sub>`lesson.biology.hoa-sinh.gap-cuon-protein-va-benh`</sub>

---

### 3. Hệ đệm sinh học, phương trình Henderson - Hasselbalch và điểm đẳng điện
*Biological buffers, the Henderson-Hasselbalch equation and isoelectric point* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được phương trình Henderson - Hasselbalch để tính pH của hệ đệm và tỉ lệ dạng ion hoá
- Giải thích được vì sao dung lượng đệm cực đại tại $pH = pK_a$
- Tính được điểm đẳng điện của amino acid và dự đoán chiều di chuyển trong điện di

## Vì sao hoá sinh phải bắt đầu từ pH

Hầu hết enzyme mất hoạt tính khi pH lệch quá 1 đơn vị, và điện tích của mọi protein, nucleotide, phospholipid đều phụ thuộc pH. Kiểm soát pH vì thế không phải chi tiết kĩ thuật mà là điều kiện tồn tại.

## Henderson - Hasselbalch

Từ $K_a = \dfrac{[H^+][A^-]}{[HA]}$, lấy $-\log$ hai vế:

$$pH = pK_a + \log\frac{[A^-]}{[HA]}$$

Ba hệ quả cần thuộc: khi $[A^-]=[HA]$ thì $pH=pK_a$; lệch 1 đơn vị pH ứng với tỉ lệ 10:1; lệch 2 đơn vị ứng với 100:1. Vùng đệm hữu ích do đó là $pK_a \pm 1$, ngoài vùng này chỉ cần thêm rất ít acid là pH đổ nhào.

## Dung lượng đệm cực đại ở đâu

Đạo hàm cho thấy $\beta = 2{,}303\,C\,\dfrac{K_a[H^+]}{(K_a+[H^+])^2}$ cực đại khi $[H^+]=K_a$. Diễn giải: ở đó cả kho acid lẫn kho base liên hợp đều dồi dào, nên hệ hấp thu được cả hai chiều nhiễu loạn.

## Ứng dụng: máu và hệ bicarbonat

Hệ $CO_2/HCO_3^-$ có $pK_a = 6{,}1$, cách xa pH máu 7,4 — theo lí thuyết đệm kín thì đây là hệ đệm tồi. Nó vẫn là hệ chính của cơ thể vì là **hệ hở**: phổi điều chỉnh $pCO_2$ và thận điều chỉnh $[HCO_3^-]$ độc lập nhau, nên mẫu số và tử số của tỉ lệ đều là biến điều khiển được.

## Điểm đẳng điện

Với amino acid trung tính chỉ có nhóm $\alpha$-COOH và $\alpha$-NH$_3^+$: $pI = \dfrac{pK_1+pK_2}{2}$. Với amino acid có nhóm R ion hoá, phải lấy trung bình hai $pK_a$ **kề hai bên** dạng trung hoà. Nguyên tắc dùng chung: ở $pH < pI$ phân tử tích điện dương và chạy về cực âm; ở $pH > pI$ thì ngược lại. Đây chính là cơ sở của sắc kí trao đổi ion và của điện di đẳng điện.

**Lỗi thường gặp:**
- Kết luận hệ bicarbonat là hệ đệm kém vì $pK_a = 6{,}1$ cách pH 7,4 tới 1,3 đơn vị. Lập luận này chỉ đúng cho hệ kín; trong cơ thể $CO_2$ được phổi thải liên tục nên mẫu số bị giữ cố định, làm hiệu lực đệm thực tế lớn hơn nhiều lần.
- Tính pI của amino acid có nhóm R ion hoá bằng trung bình $pK_1$ và $pK_2$. Sai vì pI phải là trung bình hai $pK_a$ nằm ngay hai bên dạng trung hoà; với glutamate đó là $pK_1$ và $pK_R$, không phải $pK_2$.
- Dùng Henderson - Hasselbalch khi lượng acid mạnh thêm vào lớn hơn lượng base liên hợp có sẵn. Khi đó base liên hợp bị dùng hết, hệ không còn là đệm và phương trình cho kết quả vô nghĩa (log của số âm hoặc pH sai hoàn toàn).

<sub>`lesson.biology.hoa-sinh.dem-sinh-hoc-va-diem-dang-dien`</sub>

---

### 4. Động học Michaelis - Menten và ý nghĩa của $K_M$, $k_{cat}$
*Michaelis-Menten kinetics and the meaning of KM and kcat* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Chứng minh được phương trình Michaelis - Menten từ giả thiết trạng thái dừng Briggs - Haldane
- Giải thích được ý nghĩa vật lí của $K_M$, $k_{cat}$ và hằng số đặc hiệu $k_{cat}/K_M$
- Vận dụng được các dạng tuyến tính hoá để ước lượng tham số động học từ dữ liệu thực nghiệm

## Vấn đề: đường cong bão hoà

Đo tốc độ ban đầu $v_0$ theo $[S]$, ta không được đường thẳng mà được hyperbol vuông: tăng nhanh rồi bão hoà. Phản ứng hoá học thường không như vậy. Nguyên nhân là số tâm xúc tác hữu hạn — khi mọi enzyme đã bận, thêm cơ chất không giúp gì.

## Dẫn xuất theo trạng thái dừng

Xét $E + S \underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}} ES \overset{k_2}{\rightarrow} E + P$. Đặt $d[ES]/dt = 0$:

$$k_1[E][S] = (k_{-1}+k_2)[ES]$$

Thay $[E] = [E]_T - [ES]$ và đặt $K_M = (k_{-1}+k_2)/k_1$, với $v_0 = k_2[ES]$ ta được

$$v_0 = \frac{V_{max}[S]}{K_M+[S]}, \qquad V_{max}=k_{cat}[E]_T$$

## Đọc ba tham số

$V_{max}$ phụ thuộc lượng enzyme nên không phải hằng số của enzyme; $k_{cat} = V_{max}/[E]_T$ mới là số vòng quay riêng. $K_M$ là thang nồng độ: nếu $[S]\ll K_M$ thì $v_0 \approx (k_{cat}/K_M)[E]_T[S]$, phản ứng bậc nhất theo $S$; nếu $[S]\gg K_M$ thì $v_0\approx V_{max}$, bậc không. Trong tế bào $[S]$ thường ở lân cận $K_M$, chính là vùng enzyme còn nhạy với thay đổi nồng độ cơ chất.

## Tuyến tính hoá và cạm bẫy của nó

Lineweaver - Burk cho $1/v_0 = (K_M/V_{max})(1/[S]) + 1/V_{max}$. Đồ thị này dễ đọc nhưng khuếch đại sai số của các điểm $[S]$ nhỏ, nên chỉ nên dùng để **nhìn kiểu ức chế**, còn ước lượng tham số thì phải khớp phi tuyến trực tiếp hoặc dùng Eadie - Hofstee, Hanes - Woolf.

## Khi mô hình không dùng được

Mô hình đòi hỏi $[S]\gg[E]_T$, đo ở tốc độ **ban đầu** (chưa tích luỹ sản phẩm, chưa nghịch đảo), và một tâm xúc tác độc lập. Enzyme dị lập thể nhiều tiểu đơn vị cho đường cong sigmoid, phải dùng phương trình Hill.

**Lỗi thường gặp:**
- Coi $K_M$ luôn là hằng số phân li của phức ES, tức đo ái lực. Chỉ đúng khi $k_2 \ll k_{-1}$; với enzyme xúc tác rất nhanh thì $k_2$ chi phối và $K_M$ lớn hơn $K_d$ nhiều, nên $K_M$ nhỏ không đồng nghĩa gắn chặt.
- So sánh hai enzyme bằng $V_{max}$. Sai vì $V_{max}$ tỉ lệ với lượng enzyme trong ống nghiệm; muốn so sánh bản chất xúc tác phải dùng $k_{cat}$, còn muốn so sánh hiệu quả trên cơ chất loãng phải dùng $k_{cat}/K_M$.
- Đo tốc độ ở thời điểm muộn rồi khớp Michaelis - Menten. Khi đó cơ chất đã cạn, sản phẩm đã tích luỹ gây ức chế và phản ứng nghịch, nên đường cong bị bẻ và tham số ước lượng lệch hệ thống.
- Dùng Lineweaver - Burk với hồi quy bình phương tối thiểu thông thường. Phép nghịch đảo làm sai số của các giá trị $v_0$ nhỏ (ứng với $[S]$ nhỏ) bị khuếch đại thành các điểm nằm rất xa, kéo lệch đường thẳng khớp.

<sub>`lesson.biology.hoa-sinh.dong-hoc-michaelis-menten`</sub>

---

### 5. Các dạng ức chế enzyme và cách phân biệt bằng thực nghiệm
*Types of enzyme inhibition and how to distinguish them experimentally* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được ức chế cạnh tranh, phi cạnh tranh, không cạnh tranh và hỗn hợp qua ảnh hưởng lên $K_M$ và $V_{max}$
- Vận dụng được đồ thị Lineweaver - Burk và đồ thị Dixon để xác định kiểu ức chế và $K_i$
- Giải thích được vì sao $IC_{50}$ phụ thuộc nồng độ cơ chất còn $K_i$ thì không

## Vì sao phải phân loại

Phần lớn thuốc là chất ức chế enzyme. Biết kiểu ức chế cho biết chất đó gắn vào đâu và, quan trọng hơn, tác dụng của nó thay đổi thế nào khi nồng độ cơ chất trong cơ thể dao động.

## Bốn kiểu theo hai hệ số

Đặt $\alpha = 1 + [I]/K_i$ (gắn vào E) và $\alpha' = 1+[I]/K_i'$ (gắn vào ES). Phương trình tổng quát:

$$v_0 = \frac{V_{max}[S]}{\alpha K_M + \alpha'[S]}$$

- Cạnh tranh: $\alpha>1,\ \alpha'=1$ — $K_M$ tăng, $V_{max}$ giữ nguyên.
- Phi cạnh tranh: $\alpha=1,\ \alpha'>1$ — cả $K_M$ và $V_{max}$ giảm cùng hệ số.
- Không cạnh tranh thuần: $\alpha=\alpha'>1$ — $V_{max}$ giảm, $K_M$ không đổi.
- Hỗn hợp: $\alpha\ne\alpha'$, cả hai đều đổi.

## Đọc bằng đồ thị

Trên Lineweaver - Burk: cạnh tranh cho chùm đường **cắt nhau trên trục tung** (cùng $1/V_{max}$); không cạnh tranh cắt nhau **trên trục hoành**; phi cạnh tranh cho các đường **song song** vì dạng nghịch đảo là $1/v_0 = (\alpha K_M/V_{max})(1/[S]) + \alpha'/V_{max}$, nên hệ số góc $\alpha K_M/V_{max}$ không đổi khi $\alpha=1$ trong khi tung độ gốc tăng. Đồ thị Dixon vẽ $1/v$ theo $[I]$ ở vài giá trị $[S]$, giao điểm cho $-K_i$ trực tiếp.

## $IC_{50}$ và $K_i$ khác nhau ở đâu

$IC_{50}$ là nồng độ ức chế 50% hoạt tính **trong điều kiện đo cụ thể**. Với ức chế cạnh tranh, quan hệ Cheng - Prusoff cho

$$K_i = \frac{IC_{50}}{1+[S]/K_M}$$

nên báo cáo $IC_{50}$ mà không nói $[S]$ là vô nghĩa: cùng một chất, đo ở $[S]=10K_M$ sẽ ra $IC_{50}$ lớn gấp 11 lần so với đo ở $[S]\ll K_M$.

## Ý nghĩa dược lí

Ức chế cạnh tranh bị vô hiệu khi cơ chất tích luỹ — đó là lí do thuốc ức chế cạnh tranh thường cần liều cao và duy trì. Ngược lại, ức chế phi cạnh tranh mạnh lên khi $[S]$ cao, nên là chiến lược tốt cho các con đường có cơ chất dồi dào.

**Lỗi thường gặp:**
- Kết luận kiểu ức chế chỉ từ việc $V_{max}$ có giảm hay không. Không đủ: ức chế phi cạnh tranh và không cạnh tranh đều làm $V_{max}$ giảm, phải xét thêm $K_M$ mới phân biệt được.
- Báo cáo $IC_{50}$ như một hằng số của chất ức chế. Sai vì với ức chế cạnh tranh $IC_{50}$ tỉ lệ với $(1+[S]/K_M)$, nên hai phòng thí nghiệm dùng $[S]$ khác nhau sẽ ra hai con số khác nhau cho cùng một chất.
- Nhầm ức chế phi cạnh tranh (uncompetitive) với không cạnh tranh (noncompetitive) do bản dịch. Chúng khác hẳn: phi cạnh tranh chỉ gắn ES nên các đường Lineweaver - Burk song song, còn không cạnh tranh gắn cả E lẫn ES với cùng ái lực nên các đường cắt nhau trên trục hoành.
- Coi mọi giảm hoạt tính khi tăng cơ chất là do tạp chất. Có hiện tượng thật là ức chế bởi chính cơ chất: phân tử cơ chất thứ hai gắn vào phức ES tạo ESS không sinh sản phẩm, làm đường cong $v_0$ có cực đại rồi đi xuống.

<sub>`lesson.biology.hoa-sinh.uc-che-enzyme`</sub>

---

### 6. Điều hoà dị lập thể, tính hợp tác và phương trình Hill
*Allosteric regulation, cooperativity and the Hill equation* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao enzyme dị lập thể cho đường cong sigmoid thay vì hyperbol
- Vận dụng được phương trình Hill và đồ thị Hill để định lượng mức hợp tác
- So sánh được mô hình đối xứng MWC và mô hình tuần tự KNF về mặt dự đoán thực nghiệm

## Enzyme nào cần đường cong dốc

Enzyme đầu chốt của một con đường chuyển hoá phải hoạt động như **công tắc**: tắt gần như hoàn toàn dưới ngưỡng và bật gần như hoàn toàn trên ngưỡng. Hyperbol Michaelis - Menten quá thoải cho việc đó: muốn đi từ 10% lên 90% hoạt tính phải tăng $[S]$ tới 81 lần.

## Sigmoid nhờ hợp tác

Nếu enzyme có nhiều tiểu đơn vị và việc gắn ở tâm này làm tăng ái lực ở tâm kia, đường cong thành sigmoid. Phương trình Hill mô tả nó:

$$\theta = \frac{[L]^n}{K_{0,5}^n+[L]^n}, \qquad \text{hay}\quad \log\frac{\theta}{1-\theta} = n\log[L] - n\log K_{0,5}$$

Với $n = 4$, đi từ 10% lên 90% chỉ cần tăng $[L]$ khoảng 3 lần. Đó chính là cái mà hemoglobin dùng để nhả oxygen ở mô mà vẫn nạp đầy ở phổi.

## $n$ nghĩa là gì và không nghĩa là gì

$n$ **không** phải số tâm gắn. Nó là số tâm gắn chỉ trong giới hạn hợp tác vô hạn. Hemoglobin có 4 tâm nhưng $n\approx2{,}8$; $n<1$ báo hiệu hợp tác âm hoặc hệ không đồng nhất.

## Hai mô hình cơ chế

MWC giả định đối xứng tuyệt đối: toàn phân tử ở T hoặc ở R, phối tử chỉ **chọn lọc** trạng thái R có sẵn. Mô hình này giải thích gọn ức chế và hoạt hoá dị lập thể (chất ức chế ổn định T, chất hoạt hoá ổn định R) nhưng theo nguyên tắc không giải thích được hợp tác âm. KNF cho phép từng tiểu đơn vị đổi cấu hình lần lượt, nên mô tả được cả hợp tác âm nhưng phải thêm nhiều tham số.

## Điều hoà mà không đổi $V_{max}$

Enzyme dị lập thể chia thành hai loại: loại K (chất điều hoà đổi $K_{0,5}$, giữ $V_{max}$) và loại V (đổi $V_{max}$). Điểm cần nhớ: chất điều hoà dị lập thể gắn ở **vị trí khác tâm hoạt động**, nên nó không cần giống cơ chất về cấu trúc — đó là lí do sản phẩm cuối của cả con đường có thể ức chế enzyme đầu tiên (ức chế ngược).

**Lỗi thường gặp:**
- Đọc hệ số Hill là số tâm gắn oxygen của hemoglobin và kết luận $n = 4$. Sai vì $n$ chỉ đạt số tâm khi hợp tác là vô hạn (mọi tâm gắn đồng thời); thực nghiệm luôn cho $n$ nhỏ hơn, với hemoglobin là khoảng 2,8.
- Cho rằng chất ức chế dị lập thể phải giống cơ chất về cấu trúc. Không cần, vì nó gắn ở vị trí điều hoà riêng biệt; chính điều này cho phép sản phẩm cuối con đường (cấu trúc rất khác cơ chất đầu) ức chế enzyme mở đầu.
- Khớp dữ liệu enzyme dị lập thể bằng phương trình Michaelis - Menten rồi báo cáo $K_M$. Đường cong sigmoid không có $K_M$ theo nghĩa Michaelis; đại lượng đúng là $K_{0,5}$ và bắt buộc phải kèm hệ số Hill, nếu không mất hoàn toàn thông tin về độ dốc chuyển tiếp.
- Dùng mô hình MWC để giải thích hợp tác âm. Mô hình MWC với giả thiết đối xứng chỉ sinh ra được hợp tác dương; hợp tác âm đòi hỏi các tiểu đơn vị được phép khác cấu hình nhau, tức là khung KNF.

<sub>`lesson.biology.hoa-sinh.dieu-hoa-di-lap-the`</sub>

---

## Unit 2: Nhiệt động học sinh học và chuyển hoá

### 1. Nhiệt động học sinh học, ATP và phản ứng ghép đôi
*Bioenergetics, ATP and coupled reactions* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được $\Delta G^{0'}$ và $\Delta G$ thực tế trong tế bào và giải thích ý nghĩa của mỗi đại lượng
- Vận dụng được nguyên tắc ghép đôi phản ứng để chứng minh một quá trình thu năng lượng vẫn xảy ra được
- Tính được thế năng phosphoryl hoá của tế bào từ nồng độ ATP, ADP và phosphate vô cơ

## Hai chữ $\Delta G$ rất khác nhau

$\Delta G^{0'}$ là hằng số của phản ứng, liên hệ trực tiếp với hằng số cân bằng:

$$\Delta G^{0'} = -RT\ln K'_{eq}$$

Còn $\Delta G$ thực tế phụ thuộc nồng độ tức thời trong tế bào:

$$\Delta G = \Delta G^{0'} + RT\ln Q$$

Chỉ $\Delta G$ mới trả lời được câu hỏi "phản ứng đang chạy chiều nào". Ví dụ kinh điển: phản ứng aldolase có $\Delta G^{0'} = +23{,}8$ kJ/mol, nghe như không thể xảy ra, nhưng trong hồng cầu sản phẩm bị tiêu thụ liên tục nên $Q$ rất nhỏ và $\Delta G$ thực tế âm.

## Vì sao ATP là đồng tiền

Thuỷ phân ATP có $\Delta G^{0'} \approx -30{,}5$ kJ/mol. Ba nguyên nhân: giải toả đẩy tĩnh điện giữa các nhóm phosphate mang điện âm, sản phẩm $P_i$ được ổn định bằng cộng hưởng, và sản phẩm được solvat hoá tốt hơn. Nhưng điểm quan trọng nhất: ATP nằm ở **giữa** thang thế năng chuyển nhóm phosphoryl — phosphoenolpyruvate ($-61{,}9$) và 1,3-bisphosphoglycerate ($-49{,}3$) đủ mạnh để nạp ATP, còn glucose-6-phosphate ($-13{,}8$) đủ yếu để nhận từ ATP. Nếu ATP là chất mạnh nhất thì nó không thể được tái tạo dễ dàng.

## Ghép đôi phải qua trung gian

Ghép đôi không phải "cộng hai phương trình cho vui". Về mặt cơ chế phải có một trung gian dùng chung: trong hexokinase, nhóm phosphoryl chuyển **trực tiếp** từ ATP sang glucose ngay trong tâm hoạt động, không có bước thuỷ phân tự do nào cả.

## Trong tế bào ATP mạnh hơn con số chuẩn

Với $[ATP]\approx3$ mM, $[ADP]\approx0{,}3$ mM, $[P_i]\approx5$ mM, tỉ số $Q$ nhỏ hơn 1 rất nhiều nên $\Delta G$ thực tế đạt khoảng $-50$ đến $-60$ kJ/mol. Nói cách khác, con số $-30{,}5$ kJ/mol thường bị trích dẫn là giá trị **chuẩn**, không phải giá trị sinh lí.

**Lỗi thường gặp:**
- Nói "liên kết phosphate cao năng lượng" và hiểu rằng bản thân liên kết chứa nhiều năng lượng. Sai về vật lí: phá liên kết luôn thu năng lượng; năng lượng giải phóng đến từ việc **sản phẩm** bền hơn chất phản ứng (cộng hưởng, giải toả điện tích, solvat hoá).
- Dùng $\Delta G^{0'}$ để kết luận một bước chuyển hoá không thể xảy ra trong tế bào. Sai vì tế bào không ở trạng thái chuẩn: nồng độ chất tham gia và sản phẩm chênh lệch hàng nghìn lần, và chính $RT\ln Q$ có thể đảo dấu $\Delta G$.
- Coi $\Delta G$ âm lớn nghĩa là phản ứng xảy ra nhanh. Nhiệt động học chỉ nói về chiều và giới hạn, còn tốc độ do rào cản hoạt hoá quyết định; ATP trong nước bền hàng năm dù $\Delta G$ rất âm, chính vì thế mới dùng làm chất dự trữ được.

<sub>`lesson.biology.chuyen-hoa.nhiet-dong-hoc-sinh-hoc-va-atp`</sub>

---

### 2. Đường phân: logic của mười bước và ba điểm điều hoà
*Glycolysis: the logic of ten steps and three control points* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân tích được vì sao đường phân chia thành pha đầu tư và pha thu hồi năng lượng
- Xác định được ba phản ứng không thuận nghịch và giải thích vai trò điều hoà của chúng
- Giải thích được vì sao tế bào phải tái oxi hoá NADH và các con đường để làm việc đó

## Cấu trúc bài toán

Đường phân biến một phân tử glucose 6 carbon thành hai pyruvate 3 carbon, thu ròng 2 ATP và 2 NADH. Con số ròng đó che giấu một cấu trúc hai pha: **đầu tư** 2 ATP ở các bước 1 và 3, rồi **thu hồi** 4 ATP ở các bước 7 và 10.

## Vì sao phải đầu tư trước

Phosphoryl hoá glucose làm hai việc: giữ đường trong tế bào (phân tử tích điện không qua được màng) và hạ năng lượng tự do của phân tử để các bước cắt sau khả thi. Đây là mẫu chung trong chuyển hoá: chi trước để cam kết cơ chất vào con đường.

## Ba điểm không thuận nghịch

Hexokinase, PFK-1 và pyruvate kinase có $\Delta G$ thực tế rất âm; bảy bước còn lại gần cân bằng. Hệ quả quan trọng: chỉ ba bước đó mới điều hoà được, và chỉ ba bước đó mới cần enzyme riêng khi chạy chiều ngược (tân tạo đường).

PFK-1 là điểm chốt thật sự: bị ATP và citrate ức chế (báo hiệu đủ năng lượng), được AMP và fructose-2,6-bisphosphate hoạt hoá (báo hiệu thiếu). Lưu ý AMP là tín hiệu nhạy hơn ADP nhiều vì phản ứng adenylate kinase $2\mathrm{ADP}\rightleftharpoons \mathrm{ATP}+\mathrm{AMP}$ khuếch đại thay đổi nhỏ của ATP thành thay đổi lớn của AMP.

## Nút thắt NAD⁺

Bước glyceraldehyde-3-phosphate dehydrogenase tiêu thụ $NAD^+$. Tế bào chỉ có lượng $NAD^+$ rất nhỏ, nên nếu không tái oxi hoá NADH thì đường phân dừng trong vài giây. Ba lối thoát: lên men lactate (cơ, hồng cầu), lên men ethanol (nấm men), hoặc chuyển electron vào ti thể qua con thoi malate-aspartate hay glycerol-3-phosphate.

## Điểm dễ hiểu sai

Lên men lactate không phải để "tạo năng lượng" — nó không sinh ATP nào. Mục đích duy nhất là **tái sinh $NAD^+$** để đường phân tiếp tục chạy và tiếp tục sinh ATP ở bước 7 và 10.

**Lỗi thường gặp:**
- Nói lên men lactate sinh năng lượng cho cơ. Không đúng: bản thân bước lactate dehydrogenase không tạo ATP; nó chỉ tái sinh $NAD^+$, và chính việc tái sinh đó mới cho phép đường phân tiếp tục tạo ATP ở mức cơ chất.
- Coi hexokinase là điểm điều hoà chính của đường phân. Ở gan glucose-6-phosphate còn đi vào tổng hợp glycogen và con đường pentose phosphate, nên bước thật sự cam kết vào đường phân là PFK-1; ức chế hexokinase không đặc hiệu cho đường phân.
- Cho rằng fructose-2,6-bisphosphate là một trung gian của đường phân. Nó không nằm trên con đường; nó là phân tử tín hiệu do enzyme lưỡng chức PFK-2/FBPase-2 tạo ra dưới kiểm soát của insulin và glucagon.
- Tính ATP ròng bằng 4 vì có hai bước tạo ATP mỗi bước cho 2 phân tử. Quên trừ 2 ATP đã đầu tư ở hexokinase và PFK-1, nên kết quả ròng đúng phải là 2 ATP mỗi glucose.

<sub>`lesson.biology.chuyen-hoa.duong-phan`</sub>

---

### 3. Chu trình acid citric và vai trò lưỡng dụng của nó
*The citric acid cycle and its amphibolic role* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao chu trình Krebs là chu trình chứ không phải chuỗi phản ứng thẳng
- Xác định được các bước sinh NADH, FADH₂, GTP và ba điểm điều hoà của chu trình
- Phân tích được vai trò lưỡng dụng và ý nghĩa của các phản ứng bổ sung cơ chất

## Vì sao là vòng tròn

Chu trình bắt đầu bằng việc acetyl-CoA (2C) ngưng tụ với oxaloacetate (4C) thành citrate (6C), rồi qua tám bước quay lại oxaloacetate. Ý nghĩa của thiết kế vòng: oxaloacetate đóng vai **chất xúc tác** — một phân tử có thể xử lí vô số acetyl-CoA. Đó là lí do tế bào chỉ cần giữ nồng độ oxaloacetate rất thấp.

## Kết toán một vòng

Mỗi acetyl-CoA cho 3 NADH, 1 FADH₂, 1 GTP (hoặc ATP) và 2 $CO_2$. Điểm cần nhấn: hai $CO_2$ thoát ra trong vòng **không phải** hai carbon vừa nhập vào — chúng đến từ oxaloacetate. Phải qua vài vòng thì carbon của acetyl mới bị thải.

## Bản chất là quá trình oxi hoá

Chu trình không dùng $O_2$ ở bất kì bước nào, nhưng vẫn dừng ngay khi thiếu $O_2$. Lí do: nó tiêu thụ $NAD^+$ và FAD, mà hai chất này chỉ được tái sinh nhờ chuỗi truyền electron, vốn cần $O_2$ làm chất nhận cuối. Đây là lí do chu trình Krebs được xếp vào hô hấp **hiếu khí** dù bản thân không gặp oxygen.

## Điều hoà

Ba enzyme chốt điều hoà là citrate synthase, isocitrate dehydrogenase và $\alpha$-ketoglutarate dehydrogenase; cả ba đều bị ức chế bởi NADH và ATP, được ADP và $Ca^{2+}$ hoạt hoá. Lưu ý citrate synthase không phải dehydrogenase và không dùng $NAD^+$ — ba dehydrogenase phụ thuộc $NAD^+$ của chu trình là isocitrate dehydrogenase, $\alpha$-ketoglutarate dehydrogenase và malate dehydrogenase, trong đó hai enzyme đầu trùng với hai điểm điều hoà. $Ca^{2+}$ là tín hiệu tinh tế: khi cơ co, $Ca^{2+}$ vào bào tương đồng thời báo cho ti thể tăng sản xuất ATP, tức là nhu cầu và cung ứng được đồng bộ bằng cùng một tín hiệu.

## Lưỡng dụng và hệ quả

$\alpha$-ketoglutarate đi ra làm glutamate, succinyl-CoA làm heme, oxaloacetate làm aspartate và glucose. Mỗi lần rút trung gian là mỗi lần chu trình mất chất xúc tác, nên phải có phản ứng bổ sung. Pyruvate carboxylase được acetyl-CoA hoạt hoá dị lập thể: khi acetyl-CoA ứ lại vì thiếu oxaloacetate, chính nó ra lệnh sản xuất thêm oxaloacetate.

**Lỗi thường gặp:**
- Nói hai phân tử $CO_2$ thoát ra trong một vòng chính là hai carbon của acetyl-CoA vừa nhập. Theo dõi đồng vị cho thấy chúng đến từ oxaloacetate; carbon của acetyl chỉ bị thải ở các vòng sau, nên không thể lập luận "carbon vào rồi ra ngay".
- Cho rằng chu trình Krebs cần oxygen trực tiếp. Không bước nào dùng $O_2$; nó phụ thuộc oxygen gián tiếp vì cần $NAD^+$ và FAD do chuỗi truyền electron tái sinh.
- Coi acetyl-CoA có thể chuyển ngược thành glucose. Sai vì bước pyruvate dehydrogenase không thuận nghịch và hai carbon của acetyl bị thải dưới dạng $CO_2$ trong chu trình; động vật do đó không tân tạo được đường từ acid béo chuỗi chẵn.

<sub>`lesson.biology.chuyen-hoa.chu-trinh-acid-citric`</sub>

---

### 4. Chuỗi truyền electron, thuyết hoá thẩm và phosphoryl hoá oxi hoá
*Electron transport, chemiosmosis and oxidative phosphorylation* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao electron đi theo thứ tự các phức hợp dựa trên thế khử chuẩn
- Tính được lực proton động từ chênh lệch pH và điện thế màng
- Phân tích được sự khác nhau giữa chất ức chế chuỗi hô hấp và chất tách cặp

## Vì sao có thứ tự phức hợp

Electron đi từ NADH ($E^{0'} = -0{,}32$ V) tới $O_2$ ($+0{,}82$ V), tổng chênh lệch $1{,}14$ V tương ứng $\Delta G^{0'} = -nF\Delta E^{0'} \approx -220$ kJ/mol. Nếu giải phóng một lần thì phần lớn thành nhiệt. Chuỗi chia quãng rơi này thành nhiều bậc nhỏ, mỗi bậc vừa đủ để bơm proton. Thứ tự các chất mang **do thế khử quyết định**: chất nào có $E^{0'}$ cao hơn thì nhận electron từ chất có $E^{0'}$ thấp hơn.

## Lực proton động

$$\Delta p = \Delta\psi - \frac{2{,}303RT}{F}\Delta pH$$

Ở ti thể động vật, $\Delta\psi \approx 160$ mV chiếm phần lớn, còn $\Delta pH$ chỉ khoảng 0,5-0,75 đơn vị. Ở lục lạp thì ngược lại: màng thylakoid thấm ion nên $\Delta\psi$ gần bằng 0 và gần như toàn bộ năng lượng nằm ở $\Delta pH \approx 3$.

## ATP synthase là động cơ quay

Dòng proton qua kênh $F_o$ làm vòng c quay, kéo trục $\gamma$ quay bên trong đầu $F_1$. Ba tiểu đơn vị $\beta$ lần lượt đổi qua ba cấu hình: lỏng (gắn ADP + $P_i$), chặt (tạo ATP), mở (nhả ATP). Điểm phản trực giác được Boyer chứng minh: **bước tạo liên kết ATP gần như không cần năng lượng**; năng lượng của gradient dùng để nhả ATP đã tạo ra khỏi enzyme.

## Ức chế và tách cặp khác nhau

- Chất ức chế chuỗi (cyanide ở phức hợp IV, rotenone ở I, antimycin ở III): electron dừng, gradient tan, ATP ngừng, tiêu thụ $O_2$ **giảm**.
- Chất tách cặp (2,4-dinitrophenol, protein UCP1 của mô mỡ nâu): gradient bị rò, ATP ngừng nhưng tiêu thụ $O_2$ **tăng** vì chuỗi mất tải trọng ngược.

Hai dấu hiệu đối lập về tiêu thụ $O_2$ là cách phân biệt thực nghiệm chắc chắn nhất.

## Số ATP không phải số nguyên

Tỉ lệ P/O hiện được chấp nhận là 2,5 cho NADH và 1,5 cho $FADH_2$, vì vòng c có số tiểu đơn vị không chia hết cho 3 và vì bản thân việc nhập $P_i$ và ADP cũng tiêu proton.

**Lỗi thường gặp:**
- Nhầm chất tách cặp với chất ức chế chuỗi hô hấp vì cả hai đều làm ngừng tổng hợp ATP. Dấu hiệu phân biệt là tiêu thụ oxygen: chất ức chế làm giảm, chất tách cặp làm tăng, vì chuỗi mất áp lực ngược của gradient.
- Cho rằng năng lượng của gradient dùng để tạo liên kết phosphoanhydride của ATP. Thí nghiệm trao đổi đồng vị của Boyer cho thấy ATP hình thành ngay trên enzyme gần như không tốn năng lượng; gradient chủ yếu dùng cho bước nhả ATP ra khỏi tâm chặt.
- Dùng con số 3 ATP mỗi NADH như một hằng số. Tỉ lệ P/O không phải số nguyên vì số tiểu đơn vị c của vòng ATP synthase khác nhau giữa các loài và vì nhập $P_i$/ADP cũng tiêu proton; giá trị thực nghiệm hiện nay là khoảng 2,5.
- Nghĩ mô mỡ nâu sinh nhiệt bằng cách đốt nhiều ATP hơn. Thực chất UCP1 làm rò proton nên năng lượng chuyển thẳng thành nhiệt mà **không** đi qua ATP; đó là sinh nhiệt không run cơ.

<sub>`lesson.biology.chuyen-hoa.phosphoryl-hoa-oxi-hoa`</sub>

---

### 5. Chuyển hoá lipid và amino acid: beta-oxi hoá, thể ceton và chu trình ure
*Lipid and amino acid metabolism: beta-oxidation, ketone bodies and the urea cycle* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Phân tích được vì sao acid béo cho nhiều ATP trên mỗi gram hơn carbohydrate
- Giải thích được điều kiện sinh thể ceton và vai trò của chúng khi đói kéo dài
- Giải thích được vì sao động vật trên cạn phải chuyển amoniac thành ure và chi phí năng lượng của việc đó

## Vì sao mỡ là kho dự trữ

Acid béo cho khoảng 37 kJ/g so với 17 kJ/g của carbohydrate, vì carbon của acid béo ở trạng thái khử sâu hơn. Thêm nữa glycogen ngậm nước gấp 2-3 lần khối lượng bản thân, còn triacylglycerol thì kị nước hoàn toàn. Tổng cộng, mô mỡ dự trữ năng lượng hiệu quả hơn glycogen khoảng sáu lần trên mỗi gram khối lượng cơ thể.

## Beta-oxi hoá: bốn bước lặp

Mỗi vòng gồm oxi hoá, hydrat hoá, oxi hoá, cắt thiol, rút ngắn mạch 2 carbon và cho 1 $FADH_2$ + 1 NADH + 1 acetyl-CoA. Điểm kiểm soát nằm ở cửa vào: CPT-1 bị malonyl-CoA — chất trung gian đầu tiên của **tổng hợp** acid béo — ức chế. Nhờ vậy tế bào không bao giờ đồng thời tổng hợp và phân giải acid béo, tránh chu trình vô ích.

## Thể ceton sinh ra khi nào

Khi đói, tân tạo đường rút oxaloacetate ra khỏi ti thể gan. Thiếu oxaloacetate, acetyl-CoA từ beta-oxi hoá không vào được chu trình Krebs nên bị chuyển thành thể ceton. Câu tóm tắt kinh điển: *chất béo cháy trong ngọn lửa của carbohydrate*. Não vốn không dùng được acid béo (chúng gắn albumin, không qua hàng rào máu não) nhưng dùng được thể ceton, nên sau vài ngày đói nhu cầu glucose của não giảm còn khoảng một phần ba, tiết kiệm protein cơ.

## Nitrogen phải đi đâu

Khung carbon của amino acid vào chu trình Krebs hoặc thành acetyl-CoA, nhưng nhóm amino trở thành $NH_4^+$ vốn độc với hệ thần kinh. Gan gom nitrogen qua chuyển amin (ALT, AST dùng pyridoxal phosphate) rồi khử amin oxi hoá ở glutamate dehydrogenase, sau đó đưa vào chu trình ure. Chi phí là 4 liên kết cao năng lượng mỗi phân tử ure — cái giá của việc sống trên cạn, nơi không thể thải amoniac loãng như cá.

## Ranh giới

Acid béo chuỗi lẻ cho một propionyl-CoA cuối cùng, chất này vào succinyl-CoA nên **có thể** tân tạo đường; đây là ngoại lệ duy nhất đáng kể của quy tắc "mỡ không thành đường".

**Lỗi thường gặp:**
- Tính số vòng beta-oxi hoá của acid béo 16C là 8. Sai vì vòng cuối cùng cắt một đoạn 4C thành hai acetyl-CoA, nên số vòng là 7 chứ không phải 8; nhầm chỗ này làm dư 1 NADH và 1 FADH₂.
- Quên rằng hoạt hoá acid béo tốn tương đương 2 ATP chứ không phải 1. Phản ứng tạo AMP + PPi, và pyrophosphatase thuỷ phân PPi để đẩy phản ứng, nên hai liên kết cao năng lượng bị tiêu.
- Cho rằng thể ceton là sản phẩm bệnh lí. Ở người khoẻ khi nhịn ăn hay ăn rất ít carbohydrate, thể ceton là nhiên liệu sinh lí bình thường cho não và cơ tim; chỉ trong đái tháo đường type 1 mất kiểm soát chúng mới tích luỹ tới mức gây nhiễm toan.
- Nói acetyl-CoA từ mỡ có thể chuyển thành glucose. Không được, vì hai carbon nhập vào chu trình Krebs bị thải dưới dạng $CO_2$; chỉ propionyl-CoA từ acid béo chuỗi lẻ và glycerol của triacylglycerol mới tạo glucose được.

<sub>`lesson.biology.chuyen-hoa.chuyen-hoa-lipid-va-amino-acid`</sub>

---

### 6. Tích hợp và điều hoà chuyển hoá giữa các cơ quan
*Integration and hormonal regulation of metabolism* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân tích được phân công chuyển hoá giữa gan, cơ, mô mỡ và não ở trạng thái no và đói
- Giải thích được cơ chế tác động đối lập của insulin và glucagon qua các tầng khuếch đại tín hiệu
- Vận dụng được các công thức chuyển hoá cơ bản để ước tính nhu cầu năng lượng

## Bốn cơ quan, bốn vai

- **Gan**: trung tâm điều phối. Có glucose-6-phosphatase nên là mô duy nhất thải glucose ra máu được với lượng lớn.
- **Cơ**: kho glycogen lớn nhất về khối lượng nhưng **không** chia sẻ được, vì thiếu glucose-6-phosphatase; glycogen cơ chỉ phục vụ chính nó.
- **Mô mỡ**: kho triacylglycerol, đồng thời là cơ quan nội tiết tiết leptin và adiponectin.
- **Não**: tiêu 20% năng lượng cơ thể, gần như chỉ dùng glucose và (khi đói dài) thể ceton.

## Hai tín hiệu đối lập

Insulin (no) và glucagon (đói) tác động lên cùng những enzyme nhưng theo chiều ngược nhau, thông qua phosphoryl hoá. Điểm tinh tế: **phosphoryl hoá không đồng nghĩa với hoạt hoá**. Cùng một tín hiệu glucagon làm glycogen phosphorylase được hoạt hoá và glycogen synthase bị bất hoạt — cả hai đều do phosphoryl hoá. Sự thống nhất nằm ở kết quả sinh lí, không ở dấu hoá học.

## Tầng khuếch đại

Glucagon → receptor ghép protein G → adenylyl cyclase → cAMP → PKA → phosphorylase kinase → glycogen phosphorylase. Mỗi tầng nhân số phân tử lên hàng chục tới hàng trăm lần, nên vài phân tử hormone đủ huy động hàng triệu phân tử glucose. Cái giá là độ trễ vài giây và nhu cầu phải có phosphatase để tắt tín hiệu.

## Diễn biến khi đói

Giờ 0-4: glycogen gan là nguồn chính. Giờ 4-24: glycogen cạn, tân tạo đường từ lactate (chu trình Cori), glycerol và alanine chiếm ưu thế. Ngày 2-3: thể ceton tăng nhanh. Sau tuần thứ hai: não dùng chủ yếu thể ceton, tốc độ phân giải protein cơ giảm mạnh — đây chính là cơ chế kéo dài thời gian sống sót.

## AMPK là cảm biến chung

AMPK không nghe hormone mà nghe trực tiếp tình trạng năng lượng. Khi ATP giảm, AMP tăng (bình phương mức giảm của ATP nhờ adenylate kinase), AMPK bật oxi hoá acid béo và nhập glucose, tắt tổng hợp acid béo và cholesterol. Metformin tác động một phần qua chính con đường này.

**Lỗi thường gặp:**
- Cho rằng glycogen cơ giúp duy trì đường huyết. Không đúng: cơ thiếu glucose-6-phosphatase nên glucose-6-phosphate không thoát ra máu được; cơ chỉ gián tiếp góp phần qua lactate và alanine gửi về gan.
- Hiểu phosphoryl hoá luôn là hoạt hoá enzyme. Cùng một PKA phosphoryl hoá làm glycogen phosphorylase hoạt hoá nhưng glycogen synthase bất hoạt; ý nghĩa của một biến đổi cộng hoá trị phụ thuộc enzyme cụ thể chứ không phải quy tắc chung.
- Coi tân tạo đường là đường phân chạy ngược. Bảy bước gần cân bằng dùng chung enzyme, nhưng ba bước không thuận nghịch phải đi vòng qua enzyme khác (pyruvate carboxylase + PEP carboxykinase, FBPase-1, glucose-6-phosphatase); nếu dùng chung toàn bộ thì hai chiều không thể điều hoà độc lập.
- Nghĩ chỉ hormone mới điều hoà chuyển hoá. AMPK đáp ứng trực tiếp với tỉ lệ AMP/ATP nội bào, hoạt động ngay cả khi không có tín hiệu nội tiết nào — đây là tầng điều hoà tế bào tự chủ.

<sub>`lesson.biology.chuyen-hoa.tich-hop-va-dieu-hoa-chuyen-hoa`</sub>

---

## Unit 3: Sinh học phân tử của gen

### 1. Cấu trúc chromatin và tổ chức không gian của hệ gen
*Chromatin structure and spatial genome organisation* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Tính được hệ số nén của ADN qua các bậc tổ chức chromatin
- Giải thích được vai trò của đuôi histone và các phức hợp tái định vị nucleosome
- Phân tích được ý nghĩa của TAD và vòng chromatin đối với điều hoà biểu hiện gen

## Bài toán đóng gói

Hệ gen người khoảng $6\times10^9$ cặp base ở tế bào lưỡng bội, tương ứng chiều dài duỗi thẳng khoảng 2 m, phải nằm trong nhân đường kính 6 µm. Cần hệ số nén cỡ $10^4$-$10^5$. Nhưng nén không được làm mất khả năng đọc: đây là một bài toán nén **có truy cập ngẫu nhiên**.

## Các bậc tổ chức

Sợi 11 nm (chuỗi hạt nucleosome) nén khoảng 6-7 lần. Sợi 30 nm — vốn còn tranh cãi về sự tồn tại trong tế bào sống — nén thêm khoảng 6 lần. Các vòng gắn vào bộ khung nhân và cuộn xoắn bậc cao đưa hệ số lên $10^4$; ở kì giữa nguyên phân đạt tới $10^4$-$10^5$.

## Đuôi histone: nơi ghi thông tin

Đuôi N tận của histone thò ra khỏi lõi và chịu nhiều biến đổi: acetyl hoá lysine, methyl hoá lysine/arginine, phosphoryl hoá serine, ubiquitin hoá. Acetyl hoá trung hoà điện tích dương của lysine, làm giảm lực hút với khung phosphate âm của ADN, do đó nới lỏng chromatin — quy tắc gần như không có ngoại lệ. Methyl hoá thì **không** đổi điện tích, tác dụng của nó phụ thuộc vị trí: H3K4me3 gắn với promoter hoạt động, còn H3K9me3 và H3K27me3 gắn với vùng bị ức chế.

## Vị trí nucleosome không ngẫu nhiên

Promoter hoạt động thường có một vùng trống nucleosome khoảng 150 bp ngay trước điểm khởi đầu phiên mã. Các phức hợp SWI/SNF và ISWI dùng ATP để duy trì hoặc phá vỡ cấu hình này — đây là lí do cùng một trình tự ADN cho biểu hiện rất khác nhau ở hai loại tế bào.

## Tổ chức bậc cao và ý nghĩa chức năng

Kĩ thuật Hi-C cho thấy nhiễm sắc thể chia thành TAD. Một enhancer chỉ tác động lên promoter **trong cùng TAD**; khi biên TAD bị xoá do đột biến cấu trúc, enhancer có thể bắt cặp nhầm promoter và gây bệnh — cơ chế này đã được chứng minh trong một số dị tật chi bẩm sinh. Đó là bằng chứng rằng vị trí ba chiều là một tầng thông tin thật sự, không phải hệ quả phụ của việc đóng gói.

**Lỗi thường gặp:**
- Cho rằng acetyl hoá và methyl hoá histone đều làm giãn chromatin. Acetyl hoá trung hoà điện tích lysine nên luôn giảm lực bám ADN; methyl hoá giữ nguyên điện tích và hiệu ứng phụ thuộc hoàn toàn vào vị trí gốc bị methyl và protein đọc dấu.
- Tính số nucleosome bằng cách chia tổng số bp cho 147. Bỏ qua ADN nối dài 20-90 bp giữa các nucleosome, nên kết quả dư khoảng 35%; phải dùng chu kì lặp (khoảng 180-200 bp) mới đúng.
- Coi chromatin đặc là bất hoạt tuyệt đối và chromatin mở là hoạt động. Trạng thái chromatin chỉ điều chỉnh xác suất tiếp cận; nhiều gen trong vùng euchromatin vẫn im lặng vì thiếu yếu tố phiên mã đặc hiệu.
- Nghĩ vị trí ba chiều của gen trong nhân là hệ quả ngẫu nhiên của việc gấp ADN. Thí nghiệm xoá biên TAD cho thấy tổ chức không gian có tác động nhân quả lên biểu hiện, vì nó quyết định enhancer nào gặp được promoter nào.

<sub>`lesson.biology.sinh-hoc-phan-tu.cau-truc-chromatin`</sub>

---

### 2. Nhân đôi ADN: bộ máy enzyme và nguồn gốc độ chính xác
*DNA replication: the enzyme machinery and the origin of fidelity* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao tổng hợp chỉ theo chiều 5' đến 3' dẫn tới mạch trễ gián đoạn
- Phân tích được ba tầng đảm bảo độ chính xác và đóng góp định lượng của mỗi tầng
- Giải thích được vấn đề đầu mút nhiễm sắc thể và vai trò của telomerase

## Một ràng buộc hoá học sinh ra toàn bộ cấu trúc chạc

Mọi ADN polymerase đã biết chỉ gắn nucleotide vào đầu **3'-OH** tự do. Ràng buộc này không phải ngẫu nhiên: nếu polymerase kéo dài theo chiều 3' đến 5' thì khi cắt bỏ một nucleotide sai, đầu triphosphate cung cấp năng lượng sẽ mất theo, và chuỗi không kéo dài tiếp được. Nghĩa là **đọc sửa và chiều tổng hợp là hai mặt của cùng một thiết kế**.

Hệ quả: hai mạch khuôn đối song nên một mạch được tổng hợp liên tục (mạch dẫn), mạch kia phải đứt quãng thành đoạn Okazaki dài 100-200 nt ở eukaryote, 1000-2000 nt ở vi khuẩn.

## Dàn enzyme

Helicase mở xoắn; protein SSB giữ mạch đơn; topoisomerase gỡ xoắn dương phía trước; primase đặt mồi ARN; polymerase kéo dài; RNase H và FEN1 loại mồi; ligase nối. Kẹp trượt PCNA (eukaryote) hoặc $\beta$-clamp (vi khuẩn) giữ polymerase trên khuôn, nâng độ tiến triển từ vài chục lên hàng chục nghìn nucleotide.

## Ba tầng độ chính xác

1. Chọn nucleotide đúng theo hình học cặp base: sai số $\sim10^{-5}$.
2. Đọc sửa exonuclease 3'→5': cải thiện 100 lần, còn $\sim10^{-7}$.
3. Sửa sai bắt cặp (mismatch repair) sau sao chép: cải thiện thêm 100-1000 lần, còn $\sim10^{-9}$-$10^{-10}$.

Ba tầng nhân nhau chứ không cộng, đó là lí do một hệ gen 3 tỉ base chỉ tích luỹ vài lỗi mỗi lần phân bào.

## Đầu mút nhiễm sắc thể

Sau khi loại mồi ARN ngoài cùng của mạch trễ, không có đầu 3'-OH nào phía trước để lấp. Mỗi lần phân bào, nhiễm sắc thể ngắn đi 50-200 bp. Telomere là đoạn lặp TTAGGG hi sinh cho việc này. Telomerase — một ribonucleoprotein mang chính khuôn ARN của mình — kéo dài telomere ở tế bào mầm và tế bào gốc, nhưng bị tắt ở phần lớn tế bào soma; khoảng 85-90% ung thư tái hoạt hoá nó.

## Ranh giới

Ở eukaryote có hàng chục nghìn điểm khởi đầu, mỗi điểm chỉ được kích hoạt **một lần** mỗi chu kì nhờ cơ chế cấp phép phụ thuộc chu kì tế bào. Nếu cơ chế này hỏng, vùng ADN bị nhân lên nhiều lần và gây mất ổn định hệ gen.

**Lỗi thường gặp:**
- Nói ADN polymerase tổng hợp mạch trễ theo chiều 3' đến 5'. Không enzyme nào làm vậy: từng đoạn Okazaki vẫn được tổng hợp 5'→3', chỉ có **thứ tự** các đoạn là ngược chiều di chuyển của chạc.
- Cho rằng độ chính xác $10^{-10}$ đến từ riêng khả năng bắt cặp bổ sung. Bắt cặp chỉ cho $10^{-5}$; hai bậc còn lại đến từ đọc sửa exonuclease và sửa sai bắt cặp sau sao chép, và các hệ số nhân với nhau.
- Coi telomerase là enzyme sửa chữa đứt gãy ADN. Nó chỉ kéo dài đầu mút bằng khuôn ARN nội tại của chính nó; đầu mút nhiễm sắc thể còn phải được phức hợp shelterin che để tế bào không nhầm nó với một đứt gãy sợi đôi.
- Nghĩ mồi ARN là chi tiết thừa. Primase cần thiết vì polymerase không khởi đầu chuỗi mới được; dùng ARN thay vì ADN là có chủ đích, vì nó đánh dấu đoạn cần loại bỏ và thay bằng ADN đã đọc sửa kĩ.

<sub>`lesson.biology.sinh-hoc-phan-tu.nhan-doi-adn`</sub>

---

### 3. Sửa chữa ADN và tái tổ hợp tương đồng
*DNA repair and homologous recombination* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Phân loại được các con đường sửa chữa theo loại tổn thương mà chúng xử lí
- Giải thích được vì sao đứt gãy sợi đôi nguy hiểm hơn tổn thương một sợi
- Phân tích được cơ sở phân tử của các hội chứng ung thư di truyền liên quan sửa chữa ADN

## Quy mô của vấn đề

Mỗi tế bào người hứng khoảng $10^4$-$10^5$ tổn thương ADN mỗi ngày, phần lớn từ chuyển hoá nội sinh: thuỷ phân mất base purine, khử amin cytosine thành uracil, oxi hoá guanine thành 8-oxoG. Không có sửa chữa thì hệ gen tan rã trong vài ngày.

## Chọn con đường theo loại tổn thương

- **BER**: tổn thương base nhỏ, không méo xoắn (uracil, 8-oxoG). Glycosylase đặc hiệu → AP endonuclease → polymerase β → ligase.
- **NER**: tổn thương làm méo xoắn (dimer pyrimidine do UV, adduct cồng kềnh). Cắt một đoạn 24-32 nt chứa tổn thương rồi tổng hợp lại. Hỏng NER gây khô da sắc tố (xeroderma pigmentosum) với nguy cơ ung thư da tăng hàng nghìn lần.
- **MMR**: sai bắt cặp sót lại sau sao chép. Hỏng MMR gây hội chứng Lynch và tạo kiểu hình mất ổn định vi vệ tinh.
- **Đứt gãy sợi đôi**: NHEJ hoặc HR.

## Vì sao đứt gãy sợi đôi là nghiêm trọng nhất

Với tổn thương một sợi, mạch đối diện luôn là bản sao thông tin nguyên vẹn để chép lại. Với đứt gãy sợi đôi, **thông tin bị mất ở cả hai mạch** tại cùng vị trí; ngoài ra hai đầu tự do có thể nối nhầm với đầu của nhiễm sắc thể khác, tạo chuyển đoạn — cơ chế sinh ra nhiễm sắc thể Philadelphia trong bệnh bạch cầu tuỷ mạn.

## Hai lựa chọn và cái giá của mỗi lựa chọn

HR dùng nhiễm sắc thể chị em làm khuôn nên chính xác, nhưng **chỉ khả dụng ở pha S và G2**, khi bản sao chị em đã tồn tại. NHEJ dùng được mọi lúc nhưng dễ sai. Tế bào chọn theo pha chu kì, thông qua mức độ cắt đầu 5' do CDK điều khiển.

## Ứng dụng: gây chết tổng hợp

PARP sửa đứt gãy một sợi. Ức chế PARP làm các đứt gãy một sợi tồn đọng, gặp chạc sao chép thì chuyển thành đứt gãy sợi đôi. Tế bào bình thường có BRCA1/2 nên sửa được bằng HR; tế bào ung thư mất BRCA thì không, và chết. Đây là ví dụ mẫu mực về việc khai thác một khiếm khuyết di truyền của khối u làm điểm yếu điều trị.

**Lỗi thường gặp:**
- Cho rằng tổn thương ADN chủ yếu do tác nhân bên ngoài như tia UV hay hoá chất. Phần lớn tổn thương hằng ngày là nội sinh: thuỷ phân, khử amin, và các gốc oxy hoá sinh ra từ chính hô hấp tế bào.
- Coi NHEJ là cơ chế kém và HR luôn tốt hơn. HR đòi hỏi có nhiễm sắc thể chị em nên chỉ dùng được ở pha S/G2; ở tế bào G0/G1 (phần lớn tế bào cơ thể) NHEJ là lựa chọn duy nhất, và độ chính xác của nó thực ra khá cao khi hai đầu còn tương thích.
- Nghĩ đột biến BRCA làm tế bào ung thư nhạy PARP vì PARP là mục tiêu trực tiếp của BRCA. Cơ chế thật là gây chết tổng hợp: hai con đường sửa chữa độc lập cùng hỏng thì tế bào chết, chứ hai protein không nằm trên cùng một con đường.
- Nhầm rằng sửa chữa sai bắt cặp và đọc sửa của polymerase là một. Đọc sửa xảy ra ngay tại đầu 3' đang kéo dài, còn MMR hoạt động sau khi mạch đã hoàn tất và phải phân biệt được mạch mới với mạch khuôn để không sửa nhầm mạch gốc.

<sub>`lesson.biology.sinh-hoc-phan-tu.sua-chua-adn-va-tai-to-hop`</sub>

---

### 4. Phiên mã và các yếu tố phiên mã ở eukaryote
*Transcription and eukaryotic transcription factors* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- So sánh được cơ chế khởi đầu phiên mã ở vi khuẩn và ở eukaryote
- Phân tích được cấu tạo mô đun của yếu tố phiên mã và ý nghĩa của việc tách miền gắn ADN khỏi miền hoạt hoá
- Giải thích được vì sao enhancer hoạt động được ở khoảng cách xa và theo cả hai chiều

## Vi khuẩn: một enzyme, một yếu tố sigma

ARN polymerase vi khuẩn tự nhận promoter nhờ tiểu đơn vị $\sigma$ đọc hai hộp $-10$ và $-35$. Đổi $\sigma$ là đổi cả chương trình gen — cơ chế đáp ứng sốc nhiệt và tạo bào tử đều dựa vào đó.

## Eukaryote: ba polymerase và một dàn yếu tố

Pol I làm rARN, Pol II làm mARN và phần lớn ARN điều hoà, Pol III làm tARN và 5S rARN. Pol II **không tự nhận** promoter: TFIID (chứa TBP) gắn hộp TATA hoặc các yếu tố lõi khác trước, rồi các yếu tố còn lại lắp dần. TFIIH có hai hoạt tính then chốt: helicase mở xoắn tạo bong bóng phiên mã và kinase phosphoryl hoá đuôi CTD của Pol II, tín hiệu cho phép chuyển từ khởi đầu sang kéo dài.

## Đuôi CTD là bảng điều phối

Đuôi CTD gồm 52 bản lặp heptapeptide ở người. Mẫu phosphoryl hoá của nó thay đổi dọc theo gen và quyết định enzyme hoàn thiện ARN nào được tuyển: Ser5-P ở đầu gen tuyển enzyme gắn mũ, Ser2-P ở cuối gen tuyển máy cắt nối và polyadenyl hoá. Nhờ vậy phiên mã và hoàn thiện ARN xảy ra **đồng thời**, không tuần tự.

## Yếu tố phiên mã có cấu tạo mô đun

Một yếu tố phiên mã điển hình gồm miền gắn ADN (ngón tay kẽm, xoắn-vòng-xoắn, khoá leucine) và miền hoạt hoá riêng biệt. Thí nghiệm ghép miền chứng minh tính mô đun này: gắn miền hoạt hoá của VP16 vào miền gắn ADN của GAL4 cho một protein lai hoạt động hoàn hảo. Đây cũng là cơ sở của kĩ thuật lai hai lai (two-hybrid).

## Vì sao enhancer hoạt động từ xa

Enhancer có thể nằm cách promoter hàng trăm kilobase, trước hoặc sau gen, thậm chí trong intron. Lời giải thích được chấp nhận: ADN uốn vòng, protein gắn enhancer tiếp xúc trực tiếp với Mediator và bộ máy tại promoter. Điều đó cũng lí giải vì sao chiều của enhancer không quan trọng — cái quan trọng là **tiếp xúc không gian**, không phải quét dọc theo sợi. Ràng buộc thật sự là biên TAD: enhancer chỉ với tới promoter trong cùng vùng.

**Lỗi thường gặp:**
- Cho rằng ARN polymerase II tự nhận ra promoter như polymerase vi khuẩn. Pol II hoàn toàn không có khả năng đó; nó cần TFIID và cả bộ yếu tố tổng quát để được đặt đúng chỗ và đúng chiều.
- Hiểu enhancer là đoạn nằm ngay trước promoter. Enhancer có thể ở xa hàng trăm kb, nằm phía sau gen hoặc trong intron, và đảo chiều vẫn hoạt động, vì cơ chế là uốn vòng ADN chứ không phải quét dọc sợi.
- Nghĩ hoàn thiện ARN xảy ra sau khi phiên mã kết thúc. Gắn mũ, cắt nối và polyadenyl hoá diễn ra đồng thời với kéo dài, được tuyển tới nhờ mẫu phosphoryl hoá của đuôi CTD; điều này ảnh hưởng trực tiếp tới lựa chọn exon.
- Coi việc một trình tự khớp motif là bằng chứng yếu tố phiên mã gắn ở đó. Số vị trí khớp ngẫu nhiên trong hệ gen lớn hơn số vị trí gắn thật hàng trăm lần; muốn kết luận phải có dữ liệu ChIP-seq hoặc bằng chứng chromatin mở.

<sub>`lesson.biology.sinh-hoc-phan-tu.phien-ma-va-yeu-to-phien-ma`</sub>

---

### 5. Hoàn thiện ARN và cắt nối luân phiên
*RNA processing and alternative splicing* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được chức năng của mũ 5', đuôi poly(A) và việc loại intron đối với số phận mARN
- Phân tích được cơ chế nhận diện ranh giới exon - intron và vai trò của spliceosome
- Giải thích được vì sao cắt nối luân phiên làm số protein vượt xa số gen

## Ba biến đổi bắt buộc

Tiền mARN của eukaryote không dùng được ngay. Nó phải: gắn mũ 7-methylguanosine ở đầu 5' (nối bằng liên kết 5'-5' bất thường), loại intron, và cắt rồi gắn đuôi poly(A) 150-250 nucleotide ở đầu 3'. Mũ và đuôi cùng làm ba việc: bảo vệ khỏi exonuclease, làm tín hiệu xuất khỏi nhân, và làm điểm bám cho bộ máy dịch mã.

## Nhận ranh giới intron

Intron ở eukaryote gần như luôn bắt đầu bằng GU và kết thúc bằng AG, cộng thêm điểm nhánh adenosine và vùng giàu pyrimidine trước đầu 3'. Nhưng những tín hiệu này quá ngắn để đủ đặc hiệu: intron người dài trung bình hàng nghìn nucleotide, trong đó có vô số GU và AG giả. Lời giải là **định nghĩa theo exon**: U1 snRNP và U2AF gắn ở hai đầu của một exon ngắn (trung bình chỉ 140 nt) và bắt cặp qua exon đó, nên bộ máy nhận exon chứ không nhận intron.

## Hai phản ứng chuyển ester

Adenosine điểm nhánh tấn công đầu 5' của intron tạo cấu trúc thòng lọng; sau đó đầu 3'-OH của exon phía trước tấn công đầu 3' intron, nối hai exon. Không tiêu ATP cho bản thân phản ứng — ATP chỉ dùng cho việc lắp ráp và tái sắp xếp spliceosome.

## Cắt nối luân phiên và hệ quả số học

Khoảng 95% gen người có nhiều exon được cắt nối luân phiên. Gen $Dscam$ của ruồi giấm có thể tạo tới 38016 isoform — nhiều hơn tổng số gen của chính nó. Đây là câu trả lời cho nghịch lí "người chỉ có khoảng 20000 gen": độ phức tạp không nằm ở số gen mà ở tổ hợp.

Lựa chọn exon do các protein SR (thúc đẩy) và hnRNP (ức chế) quyết định, với tỉ lệ khác nhau theo mô. Chính vì vậy cùng một gen cho protein khác nhau ở não và ở cơ.

## Khi cắt nối hỏng

Một đột biến điểm ở vị trí cắt nối có thể làm bỏ cả exon. Ước tính 15-30% đột biến gây bệnh ở người tác động qua cắt nối. Ngược lại, thuốc antisense như nusinersen điều trị teo cơ tuỷ bằng cách **ép** spliceosome giữ lại exon 7 của gen SMN2 — điều trị bằng cách điều khiển cắt nối.

**Lỗi thường gặp:**
- Cho rằng spliceosome là enzyme protein. Hoạt tính xúc tác nằm ở các snARN, đặc biệt U6 và U2 — spliceosome là một ribozyme, giống ribosome; điều này quan trọng vì nó ủng hộ giả thuyết thế giới ARN.
- Nghĩ intron chỉ cần có GU ở đầu và AG ở cuối là đủ để được nhận diện. Trong intron dài hàng nghìn nucleotide có vô số cặp GU/AG ngẫu nhiên; nhận diện thực tế dựa trên định nghĩa exon và trên các trình tự tăng cường/ức chế cắt nối nằm trong exon.
- Coi đuôi poly(A) do khuôn ADN mã hoá. Đuôi được poly(A) polymerase thêm vào sau khi mARN bị cắt tại tín hiệu AAUAAA; không có đoạn poly-T tương ứng trên gen.
- Cho rằng mọi isoform cắt nối đều tạo protein chức năng. Một tỉ lệ đáng kể isoform lệch khung đọc và bị NMD phân huỷ; chính việc tạo isoform "để bị huỷ" là một cơ chế điều hoà mức protein.

<sub>`lesson.biology.sinh-hoc-phan-tu.hoan-thien-arn-va-cat-noi-luan-phien`</sub>

---

### 6. Dịch mã, độ chính xác và kiểm soát chất lượng protein
*Translation, fidelity and protein quality control* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vai trò của aminoacyl-tARN synthetase trong việc quyết định độ chính xác của mã di truyền
- Phân tích được ba giai đoạn dịch mã và điểm tiêu tốn năng lượng của mỗi giai đoạn
- Giải thích được cơ chế đánh dấu ubiquitin và vai trò của proteasome

## Nơi thật sự quyết định mã di truyền

Ribosome chỉ kiểm tra cặp codon - anticodon, **không** kiểm tra amino acid đang gắn trên tARN. Nếu một tARN$^{Ala}$ bị gắn nhầm valine, ribosome sẽ vui vẻ đưa valine vào vị trí của alanine. Vì vậy độ trung thực của mã nằm ở aminoacyl-tARN synthetase.

Enzyme này dùng cơ chế hai sàng: tâm hoạt hoá có kích thước loại mọi amino acid lớn hơn cơ chất đúng; tâm hiệu đính có kích thước cho phép các amino acid nhỏ hơn lọt vào và bị thuỷ phân. Kết quả là tỉ lệ lỗi khoảng $10^{-4}$-$10^{-5}$, dù isoleucine và valine chỉ khác nhau một nhóm methyl.

## Ba giai đoạn và hoá đơn năng lượng

Khởi đầu ở eukaryote: eIF4E nhận mũ 5', tiểu đơn vị nhỏ quét tới codon AUG đầu tiên nằm trong bối cảnh Kozak. Kéo dài: mỗi vòng dùng 1 ATP (nạp tARN) + 2 GTP (EF-Tu/eEF1A đưa tARN vào, EF-G/eEF2 dịch chuyển). Kết thúc: yếu tố giải phóng đọc codon dừng, thuỷ phân liên kết peptidyl-tARN.

Tổng cộng khoảng **4 liên kết cao năng lượng mỗi liên kết peptide** — dịch mã là quá trình tốn năng lượng nhất của tế bào đang tăng trưởng, chiếm tới 50% ngân sách ATP ở vi khuẩn.

## Ribosome là ribozyme

Cấu trúc tinh thể cho thấy trong bán kính 18 Å quanh tâm chuyển peptidyl không có protein nào — phản ứng do rARN 23S/28S xúc tác. Đây là lí do nhiều kháng sinh (chloramphenicol, macrolide, tetracycline) nhắm vào rARN vi khuẩn, và vì khác biệt rARN 70S với 80S mà chúng có tính chọn lọc.

## Kiểm soát chất lượng nhiều tầng

- Trên mARN: NMD loại mARN có codon dừng sớm; hệ no-go và non-stop giải cứu ribosome bị kẹt.
- Trên protein mới sinh: chaperone hỗ trợ gấp; nếu thất bại, E3 ligase gắn polyubiquitin và proteasome phân huỷ.
- Ở lưới nội chất: protein gấp sai bị chuyển ngược ra bào tương để phân huỷ (ERAD), và nếu quá tải thì đáp ứng protein chưa gấp (UPR) khởi động, giảm dịch mã tổng thể.

Sự cân bằng này chính là chỗ nhiều bệnh thoái hoá thần kinh bị phá vỡ.

**Lỗi thường gặp:**
- Cho rằng ribosome kiểm tra amino acid gắn trên tARN. Ribosome chỉ kiểm tra hình học cặp codon - anticodon; nếu synthetase gắn sai amino acid thì lỗi đi thẳng vào protein, nên chính synthetase mới là tầng bảo đảm độ trung thực.
- Tính số amino acid bằng cách chia số nucleotide cho 3 mà không trừ codon kết thúc. Codon dừng không được đọc thành amino acid nào, nên kết quả luôn dư đúng một đơn vị.
- Nghĩ mỗi liên kết peptide chỉ tốn một liên kết cao năng lượng. Thực tế tốn khoảng bốn: một ATP thành AMP + PPi khi nạp tARN (tương đương hai) cộng hai GTP trong chu kì kéo dài.
- Coi proteasome phân huỷ protein một cách không chọn lọc như lysosome. Proteasome chỉ nhận protein đã bị gắn chuỗi polyubiquitin do E3 ligase đặc hiệu đánh dấu, và chính tính đặc hiệu của E3 quyết định protein nào bị loại và khi nào.

<sub>`lesson.biology.sinh-hoc-phan-tu.dich-ma-va-kiem-soat-chat-luong`</sub>

---

### 7. Điều hoà sau phiên mã và các ARN nhỏ
*Post-transcriptional regulation and small RNAs* · Đại học · intl-undergrad · 45 phút · nang-cao

**Mục tiêu:**
- Phân biệt được cơ chế và hệ quả của miARN so với siARN
- Giải thích được vai trò của vùng 3'UTR trong quyết định thời gian sống của mARN
- Vận dụng được phương pháp $2^{-\Delta\Delta C_t}$ để định lượng thay đổi biểu hiện gen

## Lượng protein không tỉ lệ với lượng mARN

Đo song song transcriptome và proteome cho thấy tương quan chỉ khoảng $R^2 \approx 0{,}4$. Phần lớn khác biệt đến từ ba biến sau phiên mã: thời gian sống của mARN, hiệu suất dịch mã và thời gian sống của protein. Vì vậy nói "gen này biểu hiện mạnh" chỉ dựa trên RNA-seq là một suy luận chưa hoàn tất.

## 3'UTR là bảng điều khiển

Vùng 3'UTR mang: vị trí gắn miARN, các yếu tố giàu AU (ARE) làm mARN mất bền nhanh, và tín hiệu định vị mARN trong tế bào. Các cytokine như TNF-$\alpha$ có ARE mạnh nên mARN chỉ tồn tại vài chục phút — đó là cách hệ miễn dịch tắt tín hiệu viêm nhanh mà không cần tắt gen.

## miARN và siARN: cùng máy, khác kết cục

Cả hai đều được Dicer cắt và nạp vào phức hợp RISC chứa Argonaute. Khác biệt then chốt là **mức bắt cặp**:

- Bắt cặp gần như hoàn toàn (siARN, phổ biến ở thực vật) → Argonaute cắt mARN.
- Bắt cặp một phần, chủ yếu ở vùng hạt giống (miARN, phổ biến ở động vật) → ức chế dịch mã và khử adenyl hoá, mARN suy giảm dần.

Vì vùng hạt giống chỉ 7 nucleotide, một miARN có hàng trăm đích tiềm năng; hệ quả là miARN thường tinh chỉnh nhiều gen trong cùng một mạng chứ không tắt hẳn một gen.

## Điều hoà dịch mã có chọn lọc

Khi tế bào stress, kinase phosphoryl hoá eIF2$\alpha$ làm dịch mã tổng thể giảm mạnh, nhưng một số mARN mang uORF (ATF4 ở người, GCN4 ở nấm men) lại **tăng** dịch mã trong đúng điều kiện đó. Cơ chế: ribosome quét bỏ sót uORF ức chế khi lượng phức hợp khởi đầu thấp. Đây là ví dụ đẹp về việc cùng một tín hiệu cho hai kết quả trái chiều tuỳ cấu trúc mARN.

## Ứng dụng

siARN tổng hợp và ARN antisense đã thành thuốc (patisiran điều trị amyloidosis do transthyretin). Điểm hạn chế chính không phải cơ chế mà là đưa thuốc tới đúng mô, vì ARN mang điện âm mạnh và bị nuclease phân huỷ nhanh.

**Lỗi thường gặp:**
- Coi miARN luôn cắt mARN đích. Ở động vật, bắt cặp thường không hoàn toàn nên Argonaute không cắt; cơ chế chủ yếu là ức chế dịch mã kèm khử adenyl hoá, và mARN suy giảm chậm hơn nhiều so với cắt trực tiếp.
- Dự đoán đích của miARN chỉ bằng tìm trình tự bổ sung với vùng hạt giống. Số vị trí khớp trong transcriptome rất lớn; đích thật còn phụ thuộc cấu trúc bậc hai của mARN, protein gắn ARN cạnh tranh và mức biểu hiện đồng thời của cả hai phân tử trong cùng tế bào.
- Dùng $2^{-\Delta\Delta C_t}$ khi hiệu suất khuếch đại của gen đích và gen tham chiếu khác nhau rõ rệt. Công thức giả định cả hai đều nhân đôi mỗi chu kì; nếu hiệu suất lệch, phải dùng phương pháp Pfaffl có hiệu chỉnh hiệu suất, nếu không kết quả sai theo cấp số nhân.
- Kết luận mức protein từ mức mARN. Tương quan giữa hai đại lượng chỉ ở mức trung bình, vì hiệu suất dịch mã và tốc độ phân huỷ protein thay đổi hàng chục lần giữa các gen.

<sub>`lesson.biology.sinh-hoc-phan-tu.dieu-hoa-sau-phien-ma-va-arn-nho`</sub>

---

### 8. Epigenetics: methyl hoá ADN, dấu ấn hệ gen và trí nhớ tế bào
*Epigenetics: DNA methylation, genomic imprinting and cellular memory* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Định nghĩa được biến đổi epigenetic và phân biệt với đột biến di truyền
- Giải thích được cơ chế duy trì methyl hoá qua phân bào và ý nghĩa của nó với trí nhớ tế bào
- Phân tích được hiện tượng dấu ấn hệ gen và bất hoạt nhiễm sắc thể X

## Vấn đề trí nhớ tế bào

Một tế bào gan phân chia hàng trăm lần vẫn cho ra tế bào gan, dù ADN giống hệt tế bào thần kinh. Phải có cơ chế **sao chép trạng thái biểu hiện** cùng lúc với sao chép trình tự.

## Methyl hoá ADN và cơ chế duy trì

DNMT3A/3B thiết lập methyl hoá mới; DNMT1 duy trì. Điểm then chốt nằm ở tính đối xứng của dinucleotide CpG: sau nhân đôi, mạch cũ còn methyl còn mạch mới thì chưa, tạo vị trí bán methyl hoá. DNMT1 nhận đúng dạng bán methyl này và methyl hoá mạch mới. Nhờ vậy dấu methyl được truyền như một mã nhị phân song song với trình tự — đây chính là cơ sở phân tử của trí nhớ tế bào.

## Methyl hoá làm im lặng bằng hai đường

Trực tiếp: nhóm methyl cản yếu tố phiên mã gắn. Gián tiếp và quan trọng hơn: protein MeCP2 và họ MBD nhận methyl-CpG rồi kéo theo phức hợp histone deacetylase, chuyển vùng đó sang chromatin đặc. Đột biến MECP2 gây hội chứng Rett — bằng chứng rằng việc *đọc* dấu epigenetic cũng thiết yếu như việc *ghi*.

## Dấu ấn hệ gen

Khoảng 100-200 gen người biểu hiện theo nguồn gốc bố mẹ. Vùng IGF2/H19 là ví dụ chuẩn: ở alen mẹ, CTCF gắn vùng chưa methyl và chặn enhancer với tới IGF2; ở alen bố vùng đó bị methyl, CTCF không gắn được, enhancer kích hoạt IGF2. Mất dấu ấn ở vùng 15q11-13 gây hội chứng Prader-Willi (mất bản bố) hoặc Angelman (mất bản mẹ) — cùng một đoạn nhiễm sắc thể, hai bệnh hoàn toàn khác nhau.

## Bất hoạt X

ARN dài Xist do chính X bị bất hoạt phiên mã ra, phủ lên nhiễm sắc thể đó theo kiểu cis và tuyển các phức hợp làm im lặng. Vì việc chọn X nào bất hoạt là ngẫu nhiên và xảy ra sớm, cơ thể nữ là thể khảm — điều này giải thích bộ lông tam thể ở mèo cái và mức độ biểu hiện bệnh rất khác nhau giữa các nữ mang gen bệnh liên kết X.

## Ranh giới cần thận trọng

Dấu epigenetic bị xoá gần như hoàn toàn hai lần: ở giao tử và sau thụ tinh. Vì vậy các tuyên bố về "di truyền epigenetic xuyên thế hệ" ở người cần bằng chứng rất mạnh, vì phải chứng minh dấu đã vượt qua hai lần tái lập trình đó.

**Lỗi thường gặp:**
- Coi biến đổi epigenetic là đột biến "nhẹ". Chúng không đụng tới trình tự nucleotide; hệ quả là chúng có thể đảo ngược bằng enzyme demethylase hoặc bằng thuốc, khác hẳn đột biến điểm.
- Cho rằng methyl hoá ADN luôn làm im lặng gen ở mọi vị trí. Quy tắc này đúng cho promoter và đảo CpG; methyl hoá trong thân gen lại tương quan **dương** với mức phiên mã vì nó ngăn khởi đầu phiên mã sai vị trí bên trong gen.
- Nghĩ nữ giới không bao giờ biểu hiện bệnh liên kết X lặn. Do bất hoạt X là ngẫu nhiên, một số nữ mang gen có tỉ lệ lệch bất lợi trong mô đích và biểu hiện triệu chứng rõ; đây là hệ quả trực tiếp của tính khảm.
- Kết luận một hiện tượng là "di truyền epigenetic xuyên thế hệ" khi chỉ quan sát hai thế hệ. Phôi trong bụng mẹ đã bị phơi nhiễm trực tiếp, và tế bào mầm của phôi cũng vậy, nên phải theo dõi tới thế hệ F3 mới loại được phơi nhiễm trực tiếp.

<sub>`lesson.biology.sinh-hoc-phan-tu.epigenetics-va-dau-an-he-gen`</sub>

---

### 9. PCR, PCR định lượng và định lượng acid nucleic
*PCR, quantitative PCR and nucleic acid quantification* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Thiết kế được mồi và tính được nhiệt độ nóng chảy, nhiệt độ bắt cặp phù hợp
- Giải thích được vì sao qPCR đo ở pha luỹ thừa chứ không đo sản phẩm cuối
- Đánh giá được chất lượng mẫu acid nucleic từ tỉ số A260/A280 và A260/A230

## Vì sao PCR hoạt động

Ba bước lặp lại: biến tính 95 °C, bắt cặp mồi 50-65 °C, kéo dài 72 °C. Sau $n$ chu kì lí tưởng, số bản sao là $N = N_0 \times 2^n$. Nhưng cấp số nhân này chỉ đúng ở giai đoạn đầu; khi dNTP cạn, polymerase mất hoạt tính và sản phẩm tự bắt cặp lại, phản ứng vào pha bình nguyên.

**Đây chính là lí do PCR điểm cuối không định lượng được**: hai mẫu chênh nhau 1000 lần vẫn cho cùng một lượng sản phẩm nếu chạy đủ nhiều chu kì.

## qPCR đo ở đúng chỗ

qPCR theo dõi huỳnh quang từng chu kì và lấy $C_t$ — điểm tín hiệu vượt ngưỡng, nằm trong pha luỹ thừa nơi động học còn tuân theo $2^n$. Quan hệ là tuyến tính với logarit lượng khuôn:

$$C_t = -\frac{1}{\log(1+E)}\log N_0 + \text{const}$$

Với $E = 1$ (hiệu suất 100%), chênh 1 $C_t$ tương ứng chênh 2 lần lượng khuôn, và chênh $3{,}32$ $C_t$ tương ứng 10 lần.

## Thiết kế mồi

Mồi 18-25 nt, GC 40-60%, hai mồi có $T_m$ lệch nhau dưới 5 °C, tránh tự bổ sung ở đầu 3'. Ước lượng nhanh dùng công thức Wallace $T_m = 2(A+T) + 4(G+C)$, chỉ đáng tin với mồi dưới 20 nt; mồi dài hơn phải dùng công thức theo hàm lượng GC có hiệu chỉnh muối, chính xác nhất là mô hình lân cận gần nhất. Nhiệt độ bắt cặp thường đặt thấp hơn $T_m$ khoảng 3-5 °C: cao quá thì mồi không bám (không có sản phẩm), thấp quá thì mồi bám vị trí gần đúng (sản phẩm phụ).

## Kiểm tra chất lượng mẫu

$A_{260}/A_{280}$ khoảng 1,8 cho ADN sạch và 2,0 cho ARN sạch; thấp hơn báo hiệu nhiễm protein hoặc phenol. $A_{260}/A_{230}$ nên trên 2,0; thấp hơn báo hiệu còn guanidine, phenol hay carbohydrate — những chất này ức chế polymerase, và đây là nguyên nhân phổ biến nhất khiến qPCR thất bại mà không rõ lí do.

## Xác nhận sản phẩm

Đường cong nóng chảy sau qPCR với SYBR Green phải cho **một** đỉnh duy nhất. Nhiều đỉnh nghĩa là có sản phẩm phụ hoặc dimer mồi, và khi đó mọi $C_t$ đo được đều không đáng tin.

**Lỗi thường gặp:**
- Định lượng bằng cách so độ đậm băng trên gel sau 35 chu kì PCR. Ở số chu kì đó phản ứng đã vào pha bình nguyên, nơi lượng sản phẩm bị giới hạn bởi dNTP và enzyme chứ không bởi lượng khuôn ban đầu, nên hai mẫu chênh nghìn lần vẫn cho băng như nhau.
- Dùng công thức Wallace cho mồi dài 28 nucleotide. Công thức này được xây dựng cho oligo ngắn dưới 20 nt trong điều kiện muối chuẩn; với mồi dài nó cho $T_m$ cao hơn thực tế nhiều chục độ, dẫn tới đặt nhiệt độ bắt cặp sai.
- Bỏ qua tỉ số $A_{260}/A_{230}$ vì thấy $A_{260}/A_{280}$ đã đạt 1,8. Hai tỉ số bắt các chất nhiễm khác nhau: 280 nm bắt protein, 230 nm bắt guanidine, phenol và carbohydrate — nhóm sau mới là nhóm ức chế polymerase mạnh nhất.
- Chấp nhận kết quả qPCR SYBR Green mà không xem đường cong nóng chảy. Nếu có dimer mồi hoặc sản phẩm phụ, huỳnh quang đo được gồm cả phần không đặc hiệu và $C_t$ bị kéo sớm lại, làm cao giả mức biểu hiện.

<sub>`lesson.biology.sinh-hoc-phan-tu.pcr-va-pcr-dinh-luong`</sub>

---

### 10. Điện di, western blot và định lượng protein
*Electrophoresis, western blotting and protein quantification* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao SDS-PAGE tách protein theo khối lượng phân tử
- Vận dụng được quan hệ tuyến tính giữa $R_f$ và logarit khối lượng phân tử để ước lượng kích thước
- Lựa chọn được phương pháp định lượng protein phù hợp với mẫu và nêu được giới hạn của mỗi phương pháp

## Vì sao phải có SDS

Protein tự nhiên khác nhau cả về điện tích lẫn hình dạng, nên điện di không SDS trộn lẫn ba biến. SDS làm hai việc: phá cấu trúc bậc hai, ba, bốn, và gắn khoảng 1,4 g SDS trên mỗi gam protein. Vì SDS mang điện âm mạnh, tỉ lệ điện tích trên khối lượng trở thành **gần như hằng số** cho mọi protein. Chỉ khi đó, ma trận gel mới sàng lọc thuần tuý theo kích thước.

## Đọc kích thước bằng $R_f$

Trong khoảng phân tách của gel, quan hệ là

$$\log M = a - b\,R_f$$

Dựng đường chuẩn từ thang protein đã biết rồi nội suy. Lưu ý phải **nội suy**, không ngoại suy: ngoài khoảng phân tách, các băng dồn lại và quan hệ mất tuyến tính.

## Khi khối lượng biểu kiến khác khối lượng thật

Có ba nguyên nhân thường gặp. Protein glycosyl hoá chạy chậm hơn (biểu kiến lớn hơn) vì đường không gắn SDS. Protein rất acid gắn ít SDS hơn nên chạy chậm. Và nếu mẫu không được khử bằng $\beta$-mercaptoethanol hoặc DTT, cầu disulfide nội phân tử làm protein gọn lại và chạy nhanh hơn thực tế.

## Định lượng protein: chọn phương pháp nào

- $A_{280}$: nhanh, không phá mẫu, nhưng phụ thuộc số gốc Trp/Tyr nên sai lớn với protein nghèo gốc thơm, và bị acid nucleic gây nhiễu mạnh.
- Bradford: nhanh, ít bị chất khử làm nhiễu, nhưng đáp ứng khác nhau nhiều giữa các protein và bị chất tẩy (kể cả SDS) phá.
- Lowry và BCA: đáp ứng đồng đều hơn giữa các protein, chịu được chất tẩy, nhưng bị chất khử và chelator gây nhiễu.

Nguyên tắc chung: dựng đường chuẩn bằng **cùng loại protein** nếu có thể, và luôn pha chuẩn trong cùng đệm với mẫu.

## Western blot là bán định lượng

Tín hiệu hoá phát quang có dải tuyến tính hẹp và dễ bão hoà. Muốn so sánh, phải chuẩn hoá theo protein nội chuẩn và chứng minh cả hai tín hiệu nằm trong dải tuyến tính. Nói "protein tăng 2 lần" từ một băng đậm hơn mà không có đường chuẩn là kết luận vượt quá dữ liệu.

**Lỗi thường gặp:**
- Vẽ đường chuẩn khối lượng phân tử theo thang tuyến tính thay vì thang logarit. Quan hệ tuyến tính chỉ đúng giữa $R_f$ và $\log M$; dùng thang thẳng sẽ cho sai số hàng chục phần trăm ở hai đầu dải.
- Kết luận protein bị biến đổi khi khối lượng biểu kiến trên gel lệch khối lượng tính từ trình tự. Glycosyl hoá, điện tích rất âm và việc khử không hoàn toàn cầu disulfide đều làm lệch $R_f$ mà không liên quan tới đột biến.
- Dùng Bradford cho mẫu đã hoà trong đệm chứa SDS. Chất tẩy phá phức thuốc nhuộm - protein nên tín hiệu sụp; với mẫu có chất tẩy phải chuyển sang BCA hoặc Lowry biến thể chịu được chất tẩy.
- Báo cáo bội số thay đổi từ western blot mà không kiểm tra dải tuyến tính. Phim và cảm biến hoá phát quang bão hoà rất nhanh, nên một băng đậm gấp đôi về mắt thường có thể tương ứng với lượng protein gấp năm lần hoặc chỉ gấp 1,2 lần.

<sub>`lesson.biology.sinh-hoc-phan-tu.dien-di-va-phan-tich-protein`</sub>

---

### 11. CRISPR-Cas9, chỉnh sửa hệ gen và công nghệ tế bào gốc
*CRISPR-Cas9, genome editing and stem cell technology* · Đại học · intl-undergrad · 50 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được cơ chế định vị của Cas9 và vai trò bắt buộc của trình tự PAM
- So sánh được kết quả sửa chữa qua NHEJ và qua HDR về mặt ứng dụng
- Phân tích được nguyên lí tái lập trình tế bào thành iPSC và các giới hạn của công nghệ này

## Từ hệ miễn dịch vi khuẩn tới công cụ

CRISPR nguyên gốc là miễn dịch thích ứng của vi khuẩn: đoạn ADN của thực khuẩn thể được lưu vào locus CRISPR, phiên mã thành ARN dẫn đường, rồi hướng Cas9 tới cắt ADN xâm nhập lần sau. Điểm khiến nó thành công cụ vạn năng: **tính đặc hiệu do ARN quyết định**, nên đổi đích chỉ cần đổi 20 nucleotide, thay vì thiết kế lại cả protein như với ZFN và TALEN.

## PAM đến trước, bắt cặp đến sau

Cas9 không quét ADN bằng cách thử bắt cặp. Nó dò tìm PAM trước; chỉ tại các vị trí có PAM, nó mới mở xoắn cục bộ và cho ARN dẫn đường thử bắt cặp. Cơ chế này giảm không gian tìm kiếm hàng chục lần và giải thích vì sao vi khuẩn không tự cắt locus CRISPR của mình — locus đó không có PAM ở đúng vị trí.

## Hai kết cục sau khi cắt

- **NHEJ**: chèn/mất vài nucleotide ngẫu nhiên. Nếu rơi vào vùng mã hoá, thường gây lệch khung và bất hoạt gen. Dùng khi mục tiêu là **knockout**. Hoạt động ở mọi pha chu kì nên hiệu suất cao.
- **HDR**: chèn chính xác trình tự mong muốn theo khuôn. Dùng khi cần **sửa** một đột biến. Hạn chế lớn: chỉ chạy ở pha S/G2, hiệu suất thường dưới 10%, và rất thấp ở tế bào không phân chia như neuron.

Chính giới hạn này thúc đẩy các thế hệ sau: base editor đổi một cặp base mà không cần cắt sợi đôi, prime editor viết trình tự mới bằng khuôn ARN gắn liền.

## Cắt nhầm đích

ARN dẫn đường vẫn cho phép vài sai lệch, nhất là ở đầu xa PAM. Các biện pháp giảm: dùng Cas9 độ chính xác cao đã kĩ thuật hoá, dùng cặp nickase cắt hai sợi riêng (cần hai lần nhận diện độc lập), giới hạn thời gian tồn tại của Cas9 bằng cách đưa vào dạng phức hợp protein-ARN thay vì plasmid.

## Tế bào gốc và tái lập trình

Yamanaka chứng minh bốn yếu tố phiên mã đủ để đưa nguyên bào sợi trưởng thành về trạng thái vạn năng — nghĩa là trạng thái biệt hoá là một mạng điều hoà **có thể đảo ngược**, không phải thay đổi vĩnh viễn. Kết hợp iPSC với CRISPR cho mô hình bệnh trên chính tế bào bệnh nhân: sửa đột biến để tạo cặp đối chứng đẳng gen, cách duy nhất loại bỏ hoàn toàn nhiễu do nền di truyền khác nhau.

## Ranh giới đạo đức và kĩ thuật

Chỉnh sửa tế bào soma chỉ ảnh hưởng người được điều trị; chỉnh sửa dòng mầm truyền cho thế hệ sau và hiện bị cấm ở hầu hết các nước. Về kĩ thuật, thể khảm khi chỉnh sửa phôi và các sắp xếp lại lớn quanh vị trí cắt vẫn là vấn đề chưa giải quyết.

**Lỗi thường gặp:**
- Nghĩ có thể nhắm bất kì vị trí nào trong hệ gen bằng CRISPR. Bắt buộc phải có PAM ngay cạnh đích; với SpCas9 điều đó giới hạn đích vào các vị trí có NGG, và nhiều đột biến điểm nằm ở vùng không có PAM phù hợp nên phải dùng biến thể Cas khác.
- Kì vọng sửa được đột biến trong neuron bằng HDR. HDR đòi hỏi nhiễm sắc thể chị em và các enzyme chỉ hoạt động ở pha S/G2; tế bào thần kinh trưởng thành không phân chia nên hầu như chỉ dùng NHEJ, và với chúng phải chọn base editor hoặc prime editor.
- Coi CRISPR "sửa" gen trong mọi trường hợp. Bản thân Cas9 chỉ cắt; kết quả cuối cùng do con đường sửa chữa của tế bào quyết định, và nếu không cung cấp khuôn thì kết quả gần như luôn là chèn/mất ngẫu nhiên chứ không phải sửa.
- Cho rằng iPSC hoàn toàn tương đương tế bào gốc phôi. iPSC còn giữ một phần dấu epigenetic của mô gốc, có tần số biến dị soma tích luỹ trong quá trình nuôi cấy, nên hai dòng phải được so sánh có đối chứng đẳng gen trước khi kết luận về kiểu hình.

<sub>`lesson.biology.sinh-hoc-phan-tu.crispr-va-cong-nghe-te-bao-goc`</sub>

---

## Unit 4: Sinh học tế bào

### 1. Bộ khung tế bào và cơ sở phân tử của vận động
*The cytoskeleton and the molecular basis of movement* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- So sánh được ba hệ sợi của bộ khung tế bào về cấu tạo, động học và chức năng
- Giải thích được hiện tượng bất ổn định động của vi ống và ý nghĩa của nó
- Phân tích được cách protein động cơ chuyển hoá năng lượng ATP thành chuyển động có hướng

## Ba hệ sợi, ba vai trò

- **Vi sợi actin** (đường kính 7 nm): chịu lực kéo, tạo hình vỏ tế bào, làm nền cho co cơ và di chuyển bò.
- **Vi ống** (25 nm): ống rỗng cứng, làm đường ray vận chuyển và thoi phân bào.
- **Sợi trung gian** (10 nm): chịu lực căng cơ học, không có tính phân cực và không gắn protein động cơ.

Khác biệt then chốt: actin và tubulin **gắn nucleotide** (ATP và GTP tương ứng) nên có động học phụ thuộc năng lượng; sợi trung gian thì không, nên chúng bền và không có động cơ chạy trên đó.

## Vì sao vi ống phải bất ổn định

Tubulin gắn GTP polymer hoá và tạo mũ GTP ở đầu đang mọc. GTP dần bị thuỷ phân trong thân ống. Nếu tốc độ thuỷ phân đuổi kịp tốc độ thêm, mũ mất và ống co rút cực nhanh (tới 20 µm/phút).

Ý nghĩa: bất ổn định cho phép vi ống **dò tìm không gian**. Trong nguyên phân, vi ống mọc thử mọi hướng, ống nào chạm kinetochore thì được ổn định, ống nào không thì co lại và thử lại. Đây là cơ chế tìm kiếm bằng thử-và-chọn, hiệu quả hơn nhiều so với mọc có định hướng sẵn.

Taxol ổn định vi ống, vinblastine ngăn polymer hoá — cả hai đều là thuốc chống ung thư, vì cả "khoá cứng" lẫn "phá huỷ" đều làm thoi phân bào không hoạt động được. Điều này cho thấy cái tế bào cần không phải vi ống dài hay ngắn, mà là khả năng **thay đổi**.

## Protein động cơ đi về đâu

Kinesin đi về đầu dương (ra ngoại vi), dynein đi về đầu âm (về trung tâm tổ chức vi ống). Myosin đi trên actin, chủ yếu về đầu dương. Kinesin-1 bước theo kiểu "tay này qua tay kia", mỗi bước 8 nm và tiêu đúng một ATP, với tính tiến triển cao nên đi được hàng micromet mà không rời đường ray.

## Vận động của cả tế bào

Di chuyển bò gồm bốn pha lặp: polymer hoá actin đẩy màng phía trước, hình thành bám dính mới, myosin II kéo thân, và tháo bám dính phía sau. Điểm cần nhớ: lực đẩy màng đến từ **chính việc polymer hoá**, không phải từ động cơ — đây là dạng chuyển hoá năng lượng khác hẳn cơ chế bước của myosin.

**Lỗi thường gặp:**
- Coi bộ khung tế bào là giàn giáo tĩnh. Actin và vi ống liên tục lắp ráp và tháo dỡ với chu kì tính bằng giây tới phút; chính tính động này, chứ không phải độ cứng, mới là cơ sở của phân bào và di chuyển.
- Cho rằng thuốc ổn định vi ống (taxol) và thuốc phá vi ống (vinblastine) phải có tác dụng trái ngược. Cả hai đều chặn phân bào, vì thoi phân bào cần khả năng thay đổi chiều dài; khoá ở trạng thái nào cũng làm mất chức năng.
- Nghĩ sợi trung gian cũng có protein động cơ chạy trên đó. Sợi trung gian được lắp từ các dimer cuộn xoắn đối song nên **không phân cực**; không có đầu dương/âm thì không thể định hướng chuyển động, và thực tế không có động cơ nào dùng chúng làm đường ray.
- Giải thích lực đẩy màng ở mép trước tế bào bằng hoạt động của myosin. Lực đó do chính quá trình polymer hoá actin sinh ra theo cơ chế bánh cóc nhiệt; myosin II tham gia ở phía sau để kéo thân tế bào, không phải ở mép trước.

<sub>`lesson.biology.sinh-hoc-te-bao.bo-khung-te-bao-va-van-dong`</sub>

---

### 2. Chu kì tế bào, cyclin - CDK và các điểm kiểm soát
*The cell cycle, cyclin-CDK and checkpoints* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao hoạt tính CDK dao động theo chu kì trong khi lượng CDK không đổi
- Phân tích được logic của ba điểm kiểm soát chính và hậu quả khi chúng hỏng
- Giải thích được vai trò của p53 và Rb với tư cách gen ức chế khối u

## Vì sao cần một đồng hồ

Các sự kiện của chu kì phải theo đúng thứ tự: không được phân li nhiễm sắc thể trước khi sao chép xong, không được sao chép lại đoạn đã sao chép. Bộ đếm thời gian đơn thuần không đủ, vì thời gian mỗi pha thay đổi theo điều kiện. Giải pháp tiến hoá là **kiểm soát theo trạng thái**: chỉ chuyển pha khi bước trước đã hoàn tất.

## Cyclin đặt nhịp

CDK có mặt ổn định suốt chu kì; hoạt tính của nó do cyclin quyết định. Cyclin D-CDK4/6 ở G1, cyclin E-CDK2 ở chuyển G1/S, cyclin A-CDK2 ở S, cyclin B-CDK1 ở G2/M. Cyclin bị phân huỷ đột ngột qua ubiquitin hoá — đây là điểm quan trọng: **phân huỷ protein là không thuận nghịch**, nên chu kì chỉ chạy được một chiều, không bao giờ lùi.

## Ba điểm kiểm soát

1. **G1/S**: kiểm tra kích thước, dinh dưỡng, tín hiệu tăng trưởng và toàn vẹn ADN. Cyclin D-CDK4/6 phosphoryl hoá Rb, giải phóng E2F, bật các gen của pha S. Đây chính là điểm hạn chế.
2. **G2/M**: kiểm tra ADN đã sao chép xong và không có tổn thương.
3. **Kì giữa - kì sau**: kiểm tra mọi kinetochore đã gắn hai cực. Một kinetochore chưa gắn cũng đủ phát tín hiệu ức chế APC/C và giữ toàn bộ tế bào lại — độ nhạy tuyệt đối này là cần thiết vì phân li sai một nhiễm sắc thể đã đủ gây lệch bội.

## p53: canh gác hệ gen

Khi ADN tổn thương, ATM/ATR phosphoryl hoá p53, làm nó thoát khỏi sự phân huỷ do MDM2 điều khiển. p53 tích luỹ và bật p21 — chất ức chế CDK — làm dừng chu kì để sửa chữa; nếu tổn thương quá nặng, p53 khởi động apoptosis. Khoảng 50% khối u người có p53 đột biến, đúng như dự đoán từ vai trò trung tâm của nó.

## Cơ chế bật dứt khoát

Các chuyển pha không diễn ra dần dần mà theo kiểu công tắc, nhờ vòng phản hồi dương: cyclin B-CDK1 hoạt hoá phosphatase Cdc25 vốn lại hoạt hoá chính CDK1. Kết quả là một lượng nhỏ hoạt tính ban đầu tự khuếch đại thành chuyển pha toàn phần trong vài phút — tế bào không bao giờ ở trạng thái "nửa vào nguyên phân".

**Lỗi thường gặp:**
- Nghĩ hoạt tính CDK thay đổi vì lượng CDK thay đổi. Nồng độ CDK gần như không đổi suốt chu kì; biến số là cyclin, và thêm nữa hoạt tính còn bị điều chỉnh bởi phosphoryl hoá ức chế của Wee1 và khử phosphoryl hoá của Cdc25.
- Coi điểm kiểm soát lắp ráp thoi đếm số kinetochore đã gắn. Nó làm ngược lại: kinetochore **chưa gắn** phát tín hiệu ức chế; chỉ khi tín hiệu cuối cùng tắt thì APC/C mới được giải phóng, nên cơ chế nhạy với dù chỉ một lỗi.
- Cho rằng tế bào có thể quay lại pha trước nếu điều kiện xấu đi. Sau điểm hạn chế, các cyclin đã bị phân huỷ bằng ubiquitin - proteasome; phân huỷ protein là bước không thuận nghịch nên chu kì chỉ chạy một chiều.
- Hiểu p53 là gen gây ung thư khi bị đột biến "tăng chức năng". p53 là gen ức chế khối u: bệnh phát sinh khi **mất** chức năng, và vì vậy cần cả hai alen bị hỏng ở mức tế bào (dù một số đột biến p53 còn có tác dụng trội âm).

<sub>`lesson.biology.sinh-hoc-te-bao.chu-ki-te-bao-va-diem-kiem-soat`</sub>

---

### 3. Chết tế bào theo chương trình: apoptosis và các dạng khác
*Programmed cell death: apoptosis and other modalities* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được apoptosis với hoại tử về cơ chế và hệ quả với mô xung quanh
- So sánh được con đường nội sinh và con đường ngoại sinh khởi động caspase
- Giải thích được vì sao rối loạn apoptosis góp phần vào ung thư và bệnh thoái hoá thần kinh

## Chết có tổ chức và chết do tai nạn

Apoptosis: tế bào co lại, chromatin cô đặc, ADN bị cắt thành bội số 180 bp, màng vẫn nguyên vẹn tới cuối, tế bào vỡ thành các thể apoptotic được đại thực bào nuốt. **Không có viêm**. Hoại tử: tế bào phồng lên, màng vỡ sớm, nội dung tràn ra và gây viêm mạnh.

Sự khác biệt này không phải chi tiết hình thái — nó là lí do cơ thể có thể loại bỏ $10^{11}$ tế bào mỗi ngày mà không viêm toàn thân.

## Vì sao dùng tầng protease

Caspase khởi đầu (2, 8, 9, 10) tự hoạt hoá khi được tập trung lại; caspase thực thi (3, 6, 7) do caspase khởi đầu cắt. Một phân tử caspase-9 hoạt hoá nhiều caspase-3, mỗi caspase-3 cắt hàng nghìn cơ chất. Vì cắt protein là không thuận nghịch, tế bào **không thể đổi ý** sau khi vượt ngưỡng — đúng thứ cần cho một quyết định sinh tử.

## Hai con đường khởi động

- **Nội sinh**: stress nội bào (tổn thương ADN, thiếu yếu tố sống, stress lưới nội chất) làm p53 bật các protein BH3-only; chúng vô hiệu Bcl-2 và Bcl-xL, cho phép Bax/Bak tạo lỗ trên màng ngoài ti thể. Cytochrome c thoát ra, lắp apoptosome cùng Apaf-1, hoạt hoá caspase-9.
- **Ngoại sinh**: phối tử Fas hay TNF gắn thụ thể chết, lắp phức hợp DISC, hoạt hoá caspase-8 trực tiếp. Đây là cách tế bào lympho T gây độc giết tế bào nhiễm virus.

Hai con đường gặp nhau ở caspase thực thi; ngoài ra caspase-8 còn cắt Bid để khuếch đại qua ti thể ở nhiều loại tế bào.

## Cytochrome c làm hai việc

Cùng một protein vừa là chất mang electron của chuỗi hô hấp vừa là tín hiệu chết khi ra bào tương. Đây là ví dụ tiêu biểu về tiết kiệm tiến hoá: định vị sai một protein trở thành tín hiệu tin cậy rằng ti thể đã hỏng.

## Khi cân bằng lệch

Quá ít apoptosis: tế bào lẽ ra phải chết vẫn sống — u lympho nang có chuyển đoạn làm Bcl-2 biểu hiện quá mức, và đây là ung thư do **không chết** chứ không phải do tăng sinh nhanh. Quá nhiều apoptosis: neuron chết dần trong bệnh thoái hoá thần kinh, tế bào cơ tim chết sau nhồi máu.

## Các dạng khác

Necroptosis là chết có lập trình nhưng gây viêm, dùng khi caspase-8 bị virus ức chế — một cơ chế dự phòng chống lại việc mầm bệnh chặn apoptosis. Pyroptosis do inflammasome khởi động, cố ý gây viêm để báo động.

**Lỗi thường gặp:**
- Coi apoptosis và hoại tử chỉ khác nhau về tốc độ chết. Khác biệt bản chất là ở tính toàn vẹn màng: apoptosis giữ màng nguyên tới khi được thực bào nên không gây viêm, hoại tử làm màng vỡ sớm và giải phóng chất gây viêm.
- Nghĩ ung thư luôn do tế bào phân chia quá nhanh. Nhiều khối u, điển hình là u lympho nang với chuyển đoạn t(14;18) làm tăng Bcl-2, phát sinh do tế bào **không chết đúng hạn**; tốc độ phân chia của chúng thậm chí thấp.
- Cho rằng cytochrome c ra bào tương là hậu quả phụ của tế bào đang chết. Đó là bước khởi động chủ động, được Bax/Bak kiểm soát chặt; giải phóng cytochrome c là nguyên nhân chứ không phải hệ quả của việc hoạt hoá caspase-9.
- Đánh đồng mọi chết tế bào có lập trình với apoptosis. Necroptosis và pyroptosis cũng được lập trình nhưng cố ý gây viêm; cơ thể dùng chúng khi cần báo động miễn dịch hoặc khi mầm bệnh đã chặn con đường caspase.

<sub>`lesson.biology.sinh-hoc-te-bao.chet-te-bao-theo-chuong-trinh`</sub>

---

### 4. Truyền tin nội bào: thụ thể, chất truyền tin thứ hai và tầng khuếch đại
*Cell signalling: receptors, second messengers and amplification cascades* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Phân loại được các họ thụ thể chính theo cơ chế chuyển tín hiệu qua màng
- Vận dụng được phương trình gắn kết phối tử để tính phần thụ thể bị chiếm
- Giải thích được vì sao tế bào cần cả cơ chế khuếch đại lẫn cơ chế tắt tín hiệu

## Ba họ thụ thể, ba cách xuyên màng

- **Kênh ion điều khiển bằng phối tử**: nhanh nhất (mili giây), dùng ở synapse.
- **GPCR**: chiếm khoảng 4% hệ gen người và là đích của khoảng một phần ba thuốc đang lưu hành; đáp ứng trong giây.
- **Thụ thể có hoạt tính enzyme** (điển hình là thụ thể tyrosine kinase): phối tử làm hai phân tử thụ thể xích lại, chúng phosphoryl hoá chéo nhau, tạo bến đậu cho protein có miền SH2.

Điểm chung: tín hiệu ngoài màng được chuyển thành một **thay đổi cấu hình hoặc vị trí** ở phía trong, chứ bản thân phối tử không vào tế bào (trừ hormone steroid vốn qua màng và gắn thụ thể nội bào).

## Định lượng gắn kết

Phần thụ thể bị chiếm tuân theo

$$\theta = \frac{[L]}{K_d+[L]}$$

Hệ quả có thể kiểm chứng: nồng độ phối tử bằng $K_d$ thì chiếm 50% thụ thể. Nhưng ở nhiều hệ, đáp ứng sinh học đạt tối đa khi mới chỉ 10-20% thụ thể bị chiếm — hiện tượng **thụ thể dự trữ**, hệ quả của khuếch đại ở các tầng dưới.

## Khuếch đại có giá của nó

Một phân tử adrenaline → một GPCR hoạt hoá vài chục protein G → mỗi adenylyl cyclase tạo hàng nghìn cAMP → PKA phosphoryl hoá hàng nghìn cơ chất. Tổng hệ số khuếch đại có thể đạt $10^{6}$-$10^{8}$.

Mặt trái: hệ như vậy sẽ bão hoà vĩnh viễn nếu không có cơ chế tắt. Vì thế mỗi tầng đều có đối trọng — GTPase nội tại của $G\alpha$, phosphodiesterase phân huỷ cAMP, phosphatase gỡ phosphate, arrestin kéo thụ thể vào trong. Cường độ tín hiệu thực chất là **kết quả cân bằng động** giữa bật và tắt, không phải chỉ do mức kích thích.

## Vì sao cần thích nghi

Khử nhạy cảm cho phép tế bào phát hiện **thay đổi tương đối** trên một nền rất rộng — nguyên lí giống thích nghi của mắt với ánh sáng. Đó cũng là cơ sở của hiện tượng dung nạp thuốc: dùng chất chủ vận opioid kéo dài làm thụ thể bị nội bào hoá, nên cần liều cao hơn để đạt cùng đáp ứng.

## Một tín hiệu, nhiều kết quả

Acetylcholine làm cơ vân co nhưng làm tim đập chậm, vì hai mô dùng hai loại thụ thể khác nhau (nicotinic là kênh ion, muscarinic là GPCR). Ý nghĩa của một tín hiệu do **bộ máy nhận** quy định, không do bản thân phân tử tín hiệu.

**Lỗi thường gặp:**
- Suy ra $K_d$ của phối tử từ $EC_{50}$ của đường cong liều - đáp ứng. Khi có thụ thể dự trữ hoặc khuếch đại mạnh, $EC_{50}$ nhỏ hơn $K_d$ nhiều lần; muốn đo ái lực phải dùng thí nghiệm gắn kết trực tiếp.
- Cho rằng cường độ đáp ứng chỉ phụ thuộc lượng phối tử. Đáp ứng là cân bằng động giữa các bước bật và các bước tắt (GTPase, phosphodiesterase, phosphatase, arrestin); ức chế phosphodiesterase làm tăng đáp ứng mà không cần thêm phối tử — đó chính là cơ chế của caffeine và sildenafil.
- Nghĩ một phân tử tín hiệu luôn cho một hiệu ứng cố định. Acetylcholine kích thích cơ vân nhưng ức chế nhịp tim, vì hai mô biểu hiện hai họ thụ thể khác nhau; ý nghĩa nằm ở bộ máy nhận tín hiệu.
- Coi việc thụ thể bị nội bào hoá là hỏng hóc. Đó là cơ chế khử nhạy cảm có chủ đích, cho phép tế bào đo thay đổi tương đối trên nền rộng, và là nguyên nhân sinh lí của hiện tượng dung nạp thuốc.

<sub>`lesson.biology.sinh-hoc-te-bao.truyen-tin-noi-bao`</sub>

---

### 5. Vận chuyển qua màng, nội bào và định vị protein tới bào quan
*Membrane transport, endomembrane traffic and protein targeting* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được khuếch tán, khuếch tán hỗ trợ, vận chuyển chủ động sơ cấp và thứ cấp theo nguồn năng lượng
- Giải thích được nguyên lí tín hiệu định vị và cách protein được đưa tới đúng bào quan
- Vận dụng được định luật Fick và phương trình Michaelis - Menten cho vận chuyển qua màng

## Bốn cách qua màng, phân theo nguồn năng lượng

1. **Khuếch tán đơn thuần**: chỉ chất nhỏ, không tích điện, tan trong lipid. Tốc độ tuân theo định luật Fick, tuyến tính với gradient, **không bão hoà**.
2. **Khuếch tán hỗ trợ**: qua kênh hoặc chất mang, vẫn xuôi gradient nên không tốn năng lượng, nhưng **có bão hoà** vì số protein hữu hạn — động học kiểu Michaelis - Menten với $K_m$ và $V_{max}$.
3. **Chủ động sơ cấp**: bơm thuỷ phân ATP trực tiếp, như $Na^+/K^+$-ATPase (3 Na ra, 2 K vào mỗi ATP, do đó sinh điện).
4. **Chủ động thứ cấp**: dùng chính gradient $Na^+$ do bơm tạo ra, như SGLT1 hấp thu glucose ở ruột.

Mẹo nhận diện thực nghiệm: nếu tốc độ bão hoà theo nồng độ thì có protein tham gia; nếu chất di chuyển ngược gradient thì phải có nguồn năng lượng ở đâu đó.

## Vì sao chỉ hai loại vận chuyển chủ động

Bơm là nơi năng lượng vào hệ; mọi vận chuyển ngược gradient khác đều "vay" từ gradient mà bơm đã tạo. Đây là lí do ức chế $Na^+/K^+$-ATPase bằng digoxin làm ngừng luôn cả hấp thu glucose, dù digoxin không đụng tới SGLT1.

## Định vị protein: hai thời điểm quyết định

Mọi protein bắt đầu dịch mã trên ribosome tự do. Nếu chuỗi mới sinh lộ ra một peptide tín hiệu hướng lưới nội chất, hạt nhận tín hiệu SRP tạm dừng dịch mã và đưa cả phức hợp tới màng lưới nội chất — dịch mã tiếp tục **xuyên qua** kênh translocon. Đây là con đường đồng dịch mã.

Nếu không có tín hiệu đó, dịch mã hoàn tất trong bào tương, và protein được đưa **sau dịch mã** tới nhân (tín hiệu NLS), ti thể (tiền peptide lưỡng cực), hoặc peroxisome (tín hiệu PTS1 ở đầu C).

## Áo túi quyết định hướng đi

COPII đưa hàng từ lưới nội chất tới Golgi; COPI đưa ngược về; clathrin làm túi từ màng sinh chất và mạng trans-Golgi. Tính đặc hiệu của đích đến do cặp protein Rab và SNARE bảo đảm: túi chỉ dung hợp khi v-SNARE trên túi khớp t-SNARE trên màng đích — một khoá và một chìa.

## Kiểm chứng bằng bệnh

Bệnh tế bào I (I-cell disease) do thiếu enzyme gắn mannose-6-phosphate: các enzyme lysosome không được đánh dấu nên bị tiết ra ngoài thay vì tới lysosome. Bệnh nhân có enzyme bình thường trong máu nhưng lysosome rỗng — bằng chứng trực tiếp rằng nhãn định vị, chứ không phải bản thân enzyme, quyết định vị trí.

**Lỗi thường gặp:**
- Phân biệt khuếch tán hỗ trợ với vận chuyển chủ động bằng việc có bão hoà hay không. Cả hai đều bão hoà vì đều dùng protein; tiêu chí đúng là chiều so với gradient điện hoá và việc có tiêu năng lượng hay không.
- Cho rằng vận chuyển chủ động thứ cấp không tốn năng lượng vì không thuỷ phân ATP. Nó tiêu gradient $Na^+$, mà gradient đó do bơm ATP tạo ra; ức chế bơm sẽ làm ngừng cả vận chuyển thứ cấp sau vài phút.
- Nghĩ protein được tổng hợp sẵn trong bào quan tương ứng. Mọi protein đều bắt đầu dịch mã trên ribosome bào tương; nơi đến do peptide tín hiệu quyết định, và bệnh tế bào I chứng minh rằng mất nhãn thì enzyme đúng vẫn tới sai chỗ.
- Áp dụng định luật Fick cho vận chuyển qua chất mang. Fick mô tả khuếch tán tự do và dự đoán tốc độ tăng vô hạn theo gradient; với chất mang phải dùng dạng bão hoà, nếu không sẽ ước lượng quá cao ở nồng độ cao.

<sub>`lesson.biology.sinh-hoc-te-bao.van-chuyen-mang-va-dinh-vi-protein`</sub>

---

### 6. Liên kết tế bào, ma trận ngoại bào và truyền tín hiệu cơ học
*Cell junctions, extracellular matrix and mechanotransduction* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- Phân loại được các kiểu liên kết tế bào theo chức năng cơ học, kín khít hay truyền thông
- Giải thích được vai trò cấu trúc và tín hiệu của collagen, proteoglycan và fibronectin
- Phân tích được cách tế bào chuyển lực cơ học thành tín hiệu sinh hoá qua integrin

## Mô cần ba thứ khác nhau

Một biểu mô phải: chịu lực kéo mà không rách, chặn dòng chất qua khe giữa các tế bào, và phối hợp hoạt động của các tế bào. Ba yêu cầu này do ba nhóm liên kết đảm nhiệm.

- **Liên kết neo** (desmosome, thể bán liên kết, liên kết dính): chịu lực. Desmosome nối sợi trung gian của hai tế bào; thể bán liên kết nối tế bào với màng đáy. Bệnh pemphigus do tự kháng thể chống desmoglein làm da bong thành bọng nước — bằng chứng lâm sàng cho vai trò cơ học.
- **Liên kết kín**: chặn khe. Ở ruột, chúng buộc mọi chất phải **đi xuyên qua** tế bào, nhờ đó cơ thể kiểm soát được cái gì được hấp thu.
- **Liên kết khe** (gap junction): kênh cho ion và phân tử dưới 1 kDa đi thẳng giữa hai bào tương, cho phép cơ tim co đồng bộ.

## Ma trận ngoại bào không phải chất độn

Collagen chịu lực kéo (collagen type I có độ bền kéo so sánh được với thép trên cùng tiết diện). Elastin cho tính đàn hồi. Proteoglycan ngậm nước tạo gel chịu **lực nén** — nguyên lí của sụn khớp. Fibronectin và laminin làm cầu nối giữa các thành phần ma trận và integrin trên tế bào.

Quan trọng hơn: ma trận là **kho chứa tín hiệu**. Các yếu tố tăng trưởng như TGF-$\beta$ và FGF được giữ ở dạng bất hoạt trong ma trận và được giải phóng khi ma trận bị phân giải bởi metalloproteinase. Vì thế tổn thương mô tự nó khởi động tín hiệu sửa chữa.

## Truyền tín hiệu cơ học

Integrin không chỉ dán tế bào vào ma trận. Khi bị kéo, các protein ở điểm bám dính (talin, vinculin) duỗi ra, để lộ vị trí gắn mới — lực cơ học được dịch thành thay đổi cấu hình protein, rồi thành tín hiệu sinh hoá qua FAK và Rho.

Hệ quả được kiểm chứng: tế bào gốc trung mô nuôi trên nền mềm như mô não thì biệt hoá thành neuron; trên nền cứng như xương thì thành nguyên bào xương — **cùng môi trường hoá học, chỉ khác độ cứng nền**. Đây là bằng chứng mạnh nhất rằng cơ học là một kênh thông tin thật sự.

## Khi mất kiểm soát

Tế bào biểu mô bình thường chết theo chương trình khi mất bám dính (hiện tượng anoikis) — cơ chế ngăn tế bào lang thang định cư sai chỗ. Tế bào ung thư di căn phải vượt qua chính rào cản này, và đó là một trong những bước khó nhất của quá trình di căn.

**Lỗi thường gặp:**
- Coi ma trận ngoại bào là vật liệu trơ lấp đầy khoảng trống. Ma trận quyết định biệt hoá qua độ cứng, giữ và giải phóng yếu tố tăng trưởng, và định hướng di chuyển tế bào; thay đổi ma trận đủ để đổi số phận tế bào mà không cần đổi tín hiệu hoá học.
- Nhầm liên kết kín với desmosome vì cả hai đều nằm ở vùng đỉnh - bên. Chúng khác hẳn chức năng: liên kết kín bịt khe với dòng chất tan, desmosome chịu lực kéo và không có tác dụng chặn dòng; mất mỗi loại cho một bệnh lí khác nhau.
- Nghĩ integrin chỉ truyền tín hiệu từ ngoài vào trong. Integrin truyền hai chiều: tín hiệu nội bào cũng làm nó đổi cấu hình để tăng hay giảm ái lực với ma trận, và đây là cơ chế bạch cầu bám thành mạch đúng lúc, đúng chỗ.
- Giải thích di căn chỉ bằng khả năng di chuyển của tế bào ung thư. Tế bào biểu mô mất bám dính bình thường sẽ chết do anoikis; muốn di căn, tế bào ung thư trước hết phải kháng được cơ chế chết này.

<sub>`lesson.biology.sinh-hoc-te-bao.tuong-tac-te-bao-va-ma-tran-ngoai-bao`</sub>

---

## Unit 5: Di truyền học

### 1. Mendel mở rộng: tương tác gen, độ thấm và biểu hiện đa dạng
*Extending Mendel: gene interaction, penetrance and expressivity* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được cơ sở sinh hoá của các tỉ lệ biến dạng từ 9:3:3:1
- Phân biệt được độ thấm không hoàn toàn với mức biểu hiện thay đổi
- Vận dụng được kiểm định chi bình phương để đánh giá sự phù hợp của số liệu với giả thuyết di truyền

## Vì sao 9:3:3:1 biến dạng

Tỉ lệ 9:3:3:1 giả định hai gen tác động độc lập lên hai tính trạng riêng. Khi hai gen cùng nằm trên **một con đường sinh hoá**, các lớp kiểu hình gộp lại và tỉ lệ biến dạng — nhưng tổng vẫn là 16.

- **9:7** — bổ sung: cần cả hai enzyme mới ra sản phẩm cuối; thiếu enzyme nào cũng cho cùng kiểu hình đột biến.
- **9:3:4** — át chế lặn: đồng hợp lặn ở gen thứ hai chặn con đường ở bước sớm hơn nên che luôn gen thứ nhất.
- **12:3:1** và **13:3** — át chế trội: một alen trội tạo chất ức chế.
- **15:1** — cộng gộp trùng lặp: hai gen làm cùng một việc, chỉ cần một alen trội bất kì là đủ.

Giá trị của cách đọc này: **tỉ lệ kiểu hình là bản đồ của con đường sinh hoá**. Từ 9:3:4 ta suy được thứ tự hai bước enzyme trong đường tổng hợp sắc tố.

## Một gen, nhiều kiểu quan hệ alen

Trội không hoàn toàn cho kiểu hình trung gian ($F_2$ là 1:2:1); đồng trội cho cả hai kiểu hình cùng hiện (nhóm máu AB); dãy alen như $I^A, I^B, i$ cho nhiều tổ hợp; gen gây chết làm tỉ lệ $F_2$ thành 2:1 (chuột vàng $A^Y$).

## Độ thấm và mức biểu hiện là hai chuyện khác nhau

Độ thấm trả lời "có biểu hiện hay không" và đo trên quần thể; mức biểu hiện trả lời "nặng đến đâu" và đo trên cá thể. Một bệnh có thể thấm 100% mà mức biểu hiện rất khác nhau (u xơ thần kinh type 1), hoặc thấm 60% mà ai đã biểu hiện thì đều nặng như nhau.

Hệ quả thực tiễn: trong tư vấn di truyền, phả hệ có thể "nhảy cóc" một thế hệ do độ thấm không hoàn toàn — người mang gen truyền bệnh cho con dù bản thân khoẻ mạnh. Nếu bỏ qua điều này, ta sẽ kết luận sai kiểu di truyền.

## Kiểm định giả thuyết

Số liệu thực nghiệm không bao giờ khớp đúng tỉ lệ lí thuyết. Chi bình phương cho biết độ lệch quan sát có nằm trong biên độ ngẫu nhiên hay không:

$$\chi^2 = \sum\frac{(O-E)^2}{E}$$

Bậc tự do bằng số lớp trừ 1. Cần nhớ giới hạn: chi bình phương chỉ dùng cho **số đếm thật**, không dùng cho tỉ lệ phần trăm, và mỗi lớp nên có kì vọng ít nhất 5.

**Lỗi thường gặp:**
- Nhầm át chế với trội - lặn. Trội - lặn là quan hệ giữa hai alen của **cùng một gen**; át chế là quan hệ giữa alen của **hai gen khác nhau**, và chính vì vậy nó làm biến dạng tỉ lệ 16 phần chứ không phải tỉ lệ 4 phần.
- Dùng chi bình phương trên tỉ lệ phần trăm thay vì số đếm. Thống kê này phụ thuộc cỡ mẫu qua chính các con số đếm; quy về 100% sẽ xoá mất thông tin về cỡ mẫu và cho kết luận sai hoàn toàn.
- Kết luận "đã chứng minh tỉ lệ 9:7" khi $\chi^2$ nhỏ. Kiểm định chỉ cho phép không bác bỏ; các mô hình khác có tỉ lệ gần 9:7 vẫn có thể phù hợp, và muốn phân biệt phải có phép lai bổ sung như lai phân tích.
- Kết luận một tính trạng không di truyền vì có người mang gen mà không biểu hiện. Đó là độ thấm không hoàn toàn; kiểu gen vẫn được truyền bình thường và có thể biểu hiện trở lại ở thế hệ sau.

<sub>`lesson.biology.di-truyen-hoc.mendel-mo-rong-va-tuong-tac-gen`</sub>

---

### 2. Liên kết gen, tái tổ hợp và lập bản đồ di truyền
*Linkage, recombination and genetic mapping* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Tính được tần số tái tổ hợp và chuyển đổi thành khoảng cách bản đồ
- Vận dụng được phép lai ba điểm để xác định thứ tự gen và hệ số trùng hợp
- Giải thích được vì sao khoảng cách bản đồ bị đánh giá thấp khi hai gen ở xa nhau

## Vì sao tần số tái tổ hợp không vượt 0,5

Mỗi lần trao đổi chéo giữa hai chromatid không chị em chỉ liên quan 2 trong 4 chromatid, nên tạo ra 2 giao tử tái tổ hợp trong 4. Dù có bao nhiêu lần trao đổi chéo, trung bình cũng chỉ đạt 50% giao tử tái tổ hợp. Vì vậy $RF = 0{,}5$ **không phân biệt được** hai gen ở xa trên cùng nhiễm sắc thể với hai gen trên hai nhiễm sắc thể khác nhau — muốn phân biệt phải dùng gen trung gian.

## Đơn vị bản đồ

$1$ cM $= 1\%$ tái tổ hợp. Quan hệ giữa cM và kilobase không cố định: ở người trung bình 1 cM $\approx$ 1 Mb, nhưng tần số trao đổi chéo cao ở gần telomere, thấp ở gần tâm động, và cao hơn ở nữ so với nam. Bản đồ di truyền và bản đồ vật lí do đó không tỉ lệ thuận.

## Phép lai ba điểm

Quy trình chuẩn gồm bốn bước:
1. Xác định hai lớp **nhiều nhất** — đó là kiểu bố mẹ.
2. Xác định hai lớp **ít nhất** — đó là trao đổi chéo kép.
3. So sánh hai lớp này: gen nào **đổi vị trí** so với kiểu bố mẹ chính là gen nằm giữa.
4. Tính $RF$ cho từng cặp, nhớ cộng cả lớp trao đổi chéo kép vào cả hai khoảng.

Bước 4 là chỗ hay sai nhất: cá thể trao đổi chéo kép đã tái tổ hợp ở **cả hai** khoảng, quên cộng chúng vào sẽ làm cả hai khoảng bị ngắn lại.

## Nhiễu

Một trao đổi chéo thường ức chế trao đổi chéo thứ hai ở gần. Hệ số trùng hợp $c = \dfrac{\text{kép quan sát}}{\text{kép kì vọng}}$, độ nhiễu $I = 1-c$. Với $I > 0$ có nhiễu dương (thường gặp), $I = 0$ nghĩa là hai lần trao đổi chéo độc lập.

## Vì sao khoảng cách xa bị đánh giá thấp

Hai lần trao đổi chéo giữa hai gen sẽ khôi phục lại tổ hợp bố mẹ, nên **không đếm được**. Càng xa, càng nhiều lần trao đổi chéo kép bị bỏ sót, và $RF$ tiệm cận 0,5 dù khoảng cách thật vẫn tăng. Hàm Haldane $d = -\frac{1}{2}\ln(1-2r)$ hiệu chỉnh điều này với giả thiết không có nhiễu; Kosambi $d = \frac{1}{4}\ln\frac{1+2r}{1-2r}$ có tính tới nhiễu và thường sát thực tế hơn ở khoảng cách trung bình.

Quy tắc thực hành: xây bản đồ bằng cách **cộng các khoảng ngắn** đo trực tiếp, thay vì đo một khoảng dài rồi hiệu chỉnh.

**Lỗi thường gặp:**
- Quên cộng lớp trao đổi chéo kép vào cả hai khoảng khi tính tần số tái tổ hợp. Cá thể trao đổi chéo kép đã tái tổ hợp ở cả hai vùng, nên bỏ sót chúng làm cả hai khoảng cách đều ngắn hơn thực tế.
- Kết luận hai gen nằm trên hai nhiễm sắc thể khác nhau khi $RF = 0{,}5$. Hai gen ở rất xa trên cùng nhiễm sắc thể cũng cho đúng giá trị này; chỉ có thể phân biệt bằng cách dùng các marker trung gian nối chúng lại.
- Cộng trực tiếp các khoảng cách lớn để ra bản đồ. Với $RF$ lớn, các trao đổi chéo kép bị bỏ sót nên tổng hai khoảng ngắn luôn lớn hơn khoảng dài đo trực tiếp; phải cộng các khoảng ngắn hoặc dùng hàm Haldane/Kosambi.
- Đổi centimorgan sang kilobase bằng một hệ số cố định. Tần số trao đổi chéo thay đổi hàng chục lần dọc nhiễm sắc thể và khác nhau giữa hai giới, nên bản đồ di truyền không tỉ lệ với bản đồ vật lí.

<sub>`lesson.biology.di-truyen-hoc.lien-ket-gen-va-lap-ban-do`</sub>

---

### 3. Di truyền vi sinh vật: trao đổi gen ngang và nguồn gốc đột biến
*Microbial genetics: horizontal gene transfer and the origin of mutation* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- So sánh được ba cơ chế trao đổi gen ngang ở vi khuẩn
- Giải thích được thí nghiệm Luria - Delbrück và ý nghĩa của nó với thuyết tiến hoá
- Phân tích được cơ chế lan truyền kháng kháng sinh dưới góc độ di truyền quần thể

## Vi khuẩn không có giảm phân, vẫn có tái tổ hợp

Ba cơ chế trao đổi gen ngang:
- **Biến nạp**: hấp thu ADN trần từ môi trường. Chính là thí nghiệm Griffith và sau đó Avery - MacLeod - McCarty chứng minh ADN là vật chất di truyền.
- **Tiếp hợp**: chuyển qua tiếp xúc. Chủng Hfr có plasmid F cài vào nhiễm sắc thể, khi tiếp hợp sẽ chuyển dần nhiễm sắc thể theo thứ tự — cơ sở của bản đồ gen tính bằng **phút**.
- **Tải nạp**: nhờ thực khuẩn thể.

Điểm chung khiến chúng quan trọng: gen di chuyển **giữa các cá thể cùng thế hệ**, thậm chí giữa các loài khác nhau. Cây phát sinh của vi khuẩn vì thế giống một mạng lưới hơn là một cây.

## Đột biến có phải đáp ứng với môi trường không

Đây là câu hỏi Luria và Delbrück giải quyết năm 1943. Hai giả thuyết cho dự đoán khác nhau về **phương sai**:

- Nếu đột biến do phage cảm ứng ra (thuyết Lamarck): mỗi tế bào có xác suất nhỏ độc lập, số khuẩn lạc kháng theo Poisson, phương sai $\approx$ trung bình.
- Nếu đột biến xảy ra ngẫu nhiên trước khi gặp phage (thuyết Darwin): đột biến sớm sinh ra dòng lớn, đột biến muộn sinh dòng nhỏ, nên phương sai **lớn hơn trung bình rất nhiều**.

Kết quả thực nghiệm cho phương sai vượt trung bình hàng chục lần. Đây là một trong những thí nghiệm đẹp nhất sinh học: một đại lượng thống kê phân biệt được hai thế giới quan.

## Kháng kháng sinh dưới góc nhìn quần thể

Kháng sinh không tạo ra đột biến kháng, nó chỉ **chọn lọc** những đột biến đã có sẵn ở tần số thấp. Kèm theo đó, gen kháng thường nằm trên plasmid mang nhiều gen kháng cùng lúc, và các transposon di chuyển chúng giữa các plasmid. Kết quả là kháng đa thuốc có thể lan nhanh hơn nhiều so với dự đoán từ riêng tốc độ đột biến.

Hệ quả thực hành: dùng liều đủ mạnh và đủ dài để không để lại quần thể trung gian; dùng phối hợp thuốc để xác suất một tế bào mang đồng thời hai đột biến kháng trở nên rất nhỏ (tích của hai xác suất nhỏ).

## Vì sao vi sinh vật là hệ mẫu

Thời gian thế hệ 20 phút, quần thể $10^9$ tế bào trong một ống, chọn lọc bằng đĩa thạch. Nghĩa là ta quan sát được tiến hoá trong thời gian thực — điều không làm được với sinh vật bậc cao.

**Lỗi thường gặp:**
- Nói kháng sinh làm vi khuẩn đột biến để kháng lại. Thí nghiệm Luria - Delbrück bác bỏ điều này bằng phân tích phương sai: đột biến đã có sẵn trước khi tiếp xúc, kháng sinh chỉ chọn lọc chúng.
- Cho rằng tần số đột biến thấp thì kháng thuốc hiếm gặp trên lâm sàng. Với cỡ quần thể $10^9$-$10^{10}$ trong một ổ nhiễm, ngay cả tần số $10^{-9}$ cũng cho hàng chục tế bào kháng; điều quyết định là tích của tần số với cỡ quần thể, không phải riêng tần số.
- Coi trao đổi gen ngang là hiện tượng hiếm và không đáng kể trong tiến hoá. Ở vi khuẩn nó phổ biến tới mức cây phát sinh chủng loại dựng từ các gen khác nhau cho các cấu trúc khác nhau, và toàn bộ cụm gen kháng có thể chuyển nguyên khối qua plasmid.
- Dựng bản đồ gen vi khuẩn bằng tần số tái tổ hợp như ở eukaryote. Ở chủng Hfr, bản đồ được dựng theo **thứ tự thời gian** gen được chuyển sang tế bào nhận, đơn vị là phút, vì không có giảm phân và trao đổi chéo tương hỗ.

<sub>`lesson.biology.di-truyen-hoc.di-truyen-vi-sinh-vat`</sub>

---

### 4. Di truyền quần thể: Hardy - Weinberg mở rộng và các sai lệch
*Population genetics: extended Hardy-Weinberg and its deviations* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Vận dụng được nguyên lí Hardy - Weinberg cho nhiều alen và cho gen liên kết giới tính
- Kiểm định được cân bằng Hardy - Weinberg trên số liệu thực tế và diễn giải kết quả
- Phân tích được ảnh hưởng của nội phối và của cấu trúc quần thể lên tần số kiểu gen

## Hardy - Weinberg là mô hình rỗng, và đó là ưu điểm

Nguyên lí phát biểu: nếu không có lực tiến hoá nào tác động, tần số alen **không đổi** qua các thế hệ và tần số kiểu gen là $p^2 : 2pq : q^2$. Vì tất cả các giả thiết đều không đúng trong tự nhiên, giá trị của mô hình không nằm ở việc mô tả thực tế mà ở việc làm **mốc so sánh**: mọi sai lệch so với HW đều chỉ ra một lực tiến hoá đang hoạt động.

## Ba mở rộng cần thuộc

- **Nhiều alen**: với $p+q+r=1$, khai triển $(p+q+r)^2$ cho sáu kiểu gen. Áp dụng cho nhóm máu ABO.
- **Gen liên kết X**: nam giới bán hợp tử nên tần số kiểu hình lặn ở nam **bằng chính** $q$; ở nữ là $q^2$. Với $q=0{,}08$ (mù màu), 8% nam nhưng chỉ 0,64% nữ bị bệnh. Đây là cách nhanh nhất để ước lượng $q$ cho gen liên kết X.
- **Nội phối**: tần số kiểu gen thành $p^2+Fpq$, $2pq(1-F)$, $q^2+Fpq$. Chú ý tần số **alen** không đổi — nội phối chỉ sắp xếp lại alen vào các kiểu gen.

## Vì sao dị hợp tử là chỉ báo nhạy

Cả nội phối, hiệu ứng Wahlund và chọn lọc chống dị hợp đều làm thiếu hụt dị hợp tử. Vì thế bước đầu tiên khi phân tích số liệu quần thể luôn là so sánh $H_{obs}$ với $H_{exp} = 2pq$. Chỉ số $F_{ST}$ đo mức phân hoá giữa các quần thể chính là dạng chuẩn hoá của ý tưởng này.

## Kiểm định trong thực tế

Dùng chi bình phương với bậc tự do bằng số kiểu gen trừ số alen. Với một locus hai alen: $3-2 = 1$ bậc tự do, không phải 2 — vì tần số alen được ước lượng từ chính số liệu, mất thêm một bậc.

Lưu ý diễn giải: sai lệch HW ở một locus thường **không** phải bằng chứng chọn lọc, mà hay là dấu hiệu của lỗi kiểu gen hoá (alen câm không được phát hiện làm dị hợp bị đọc thành đồng hợp), hoặc quần thể bị phân tầng. Đây cũng là bước kiểm tra chất lượng bắt buộc trong mọi nghiên cứu GWAS.

## Ranh giới

HW nói về **tần số kiểu gen tại một locus**, không nói gì về hai locus. Hai locus có thể cân bằng HW riêng lẻ mà vẫn mất cân bằng liên kết với nhau, và chính đại lượng đó mới là cơ sở của lập bản đồ liên kết trong GWAS.

**Lỗi thường gặp:**
- Dùng 2 bậc tự do khi kiểm định HW cho locus hai alen. Vì tần số alen được ước lượng từ chính số liệu nên mất thêm một bậc; bậc tự do đúng là số kiểu gen trừ số alen, tức $3-2=1$.
- Cho rằng nội phối làm thay đổi tần số alen. Nội phối chỉ phân bố lại alen vào các kiểu gen, làm giảm dị hợp và tăng cả hai loại đồng hợp; tần số alen chỉ đổi khi có chọn lọc, đột biến, di nhập gen hoặc trôi dạt.
- Tính tần số alen lặn liên kết X ở nam bằng cách lấy căn bậc hai tỉ lệ nam mắc bệnh. Nam chỉ có một alen X nên tỉ lệ nam mắc bệnh **bằng chính** $q$; lấy căn sẽ cho kết quả sai lệch rất lớn.
- Kết luận ngay có chọn lọc khi số liệu lệch HW. Trên thực tế nguyên nhân phổ biến hơn nhiều là phân tầng quần thể và lỗi kiểu gen hoá; đây chính là lí do kiểm định HW được dùng làm bước kiểm soát chất lượng trong GWAS chứ không phải bằng chứng tiến hoá.

<sub>`lesson.biology.di-truyen-hoc.di-truyen-quan-the-hardy-weinberg`</sub>

---

### 5. Di truyền số lượng, phân tích phương sai và hệ số di truyền
*Quantitative genetics, variance partitioning and heritability* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Phân tách được phương sai kiểu hình thành các thành phần di truyền và môi trường
- Phân biệt được hệ số di truyền nghĩa rộng và nghĩa hẹp về định nghĩa và về ứng dụng
- Vận dụng được phương trình chọn giống để dự đoán đáp ứng chọn lọc

## Tính trạng liên tục vẫn tuân theo Mendel

Chiều cao, năng suất, huyết áp phân bố liên tục vì chúng do nhiều locus, mỗi locus tác động nhỏ, cộng thêm môi trường. Mô hình đa gen của Fisher chỉ ra rằng chỉ cần vài chục locus cộng gộp là phân bố đã xấp xỉ chuẩn — không cần cơ chế di truyền mới nào.

## Phân tách phương sai

$$V_P = V_G + V_E + 2\mathrm{Cov}(G,E) + V_{G\times E}$$
$$V_G = V_A + V_D + V_I$$

Trong đó $V_A$ là cộng gộp, $V_D$ là trội, $V_I$ là át chế. Hai hệ số di truyền:

$$H^2 = \frac{V_G}{V_P} \quad (\text{nghĩa rộng}), \qquad h^2 = \frac{V_A}{V_P} \quad (\text{nghĩa hẹp})$$

## Vì sao chỉ $h^2$ dự đoán được chọn lọc

Bố mẹ truyền **alen**, không truyền kiểu gen. Tổ hợp trội $Aa$ của bố mẹ bị phá vỡ khi tạo giao tử, nên $V_D$ không truyền sang đời con một cách tin cậy. Chỉ hiệu ứng trung bình của từng alen — tức $V_A$ — mới truyền được. Đó là lí do phương trình chọn giống dùng $h^2$:

$$R = h^2 S$$

## Hiểu đúng hệ số di truyền

Ba điểm hay bị hiểu sai, và cả ba đều nghiêm trọng:

1. $h^2$ là thuộc tính của **quần thể trong một môi trường cụ thể**, không phải của tính trạng hay của cá thể. Cùng một tính trạng có $h^2$ khác nhau ở hai quần thể.
2. $h^2$ cao **không** nghĩa là môi trường không tác động được. Chiều cao người có $h^2 \approx 0{,}8$ nhưng trung bình chiều cao đã tăng hơn 10 cm trong một thế kỉ nhờ dinh dưỡng — $h^2$ nói về *biến thiên trong quần thể*, không nói về *khả năng thay đổi trung bình*.
3. $h^2$ **không** giải thích được khác biệt **giữa** các nhóm. Nếu hai nhóm sống trong hai môi trường khác nhau, chênh lệch trung bình giữa chúng có thể hoàn toàn do môi trường ngay cả khi $h^2$ trong mỗi nhóm bằng 1.

## Đo bằng cách nào

Hồi quy con theo trung bình bố mẹ cho ước lượng $h^2$ trực tiếp bằng hệ số góc. So sánh cặp sinh đôi cùng trứng và khác trứng cho $H^2$. Với số liệu hiện đại, SNP-heritability ước lượng từ ma trận quan hệ di truyền toàn hệ gen; giá trị này thường thấp hơn ước lượng từ phả hệ, tạo nên vấn đề "độ di truyền còn thiếu".

**Lỗi thường gặp:**
- Hiểu $h^2 = 0{,}8$ nghĩa là 80% chiều cao của một người do gen quy định. Hệ số di truyền mô tả tỉ lệ **phương sai trong quần thể**, hoàn toàn không phân tách được nguyên nhân ở mức cá thể — với một cá thể, câu hỏi "bao nhiêu phần trăm do gen" không có nghĩa.
- Dùng $H^2$ thay cho $h^2$ trong phương trình chọn giống. $H^2$ bao gồm cả $V_D$ và $V_I$ vốn bị phá vỡ khi tạo giao tử, nên dùng nó sẽ dự đoán đáp ứng chọn lọc cao hơn thực tế, đôi khi vài lần.
- Suy từ $h^2$ cao trong mỗi nhóm rằng chênh lệch trung bình giữa hai nhóm là do di truyền. Đây là sai lầm logic nghiêm trọng: hai nhóm gieo cùng một giống trên hai loại đất khác nhau vẫn cho $h^2$ cao trong mỗi ruộng, trong khi toàn bộ chênh lệch giữa hai ruộng là do đất.
- Cho rằng $h^2$ cao nghĩa là can thiệp môi trường vô ích. Chiều cao và chỉ số IQ đều có $h^2$ cao nhưng trung bình quần thể đã dịch chuyển mạnh trong một thế kỉ nhờ dinh dưỡng và giáo dục; $h^2$ chỉ mô tả môi trường **hiện có**, không mô tả các môi trường chưa từng thử.

<sub>`lesson.biology.di-truyen-hoc.di-truyen-so-luong-va-he-so-di-truyen`</sub>

---

### 6. Chọn lọc, trôi dạt, di nhập gen và động lực tiến hoá
*Selection, drift, gene flow and evolutionary dynamics* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Tính được thay đổi tần số alen sau một thế hệ chọn lọc với các mô hình độ thích nghi khác nhau
- Giải thích được vì sao chọn lọc chống alen lặn trở nên rất kém hiệu quả khi alen đã hiếm
- So sánh được vai trò tương đối của chọn lọc và trôi dạt theo kích thước quần thể hiệu dụng

## Bốn lực và thang thời gian của chúng

Chọn lọc, trôi dạt, đột biến, di nhập gen. Đột biến tạo biến dị nhưng tốc độ rất chậm ($10^{-8}$-$10^{-6}$ mỗi locus mỗi thế hệ); di nhập gen làm đồng nhất hoá nhanh — chỉ **một cá thể di cư mỗi thế hệ** cũng đủ ngăn hai quần thể phân hoá hoàn toàn.

## Chọn lọc chống alen lặn: bài toán lợi tức giảm dần

Với alen lặn có hại tần số $q$, thay đổi mỗi thế hệ xấp xỉ

$$\Delta q \approx -\frac{s q^2 (1-q)}{1-sq^2}$$

Khi $q$ nhỏ, $\Delta q \propto q^2$ — giảm cực nhanh. Lí do sinh học rất trực quan: khi $q = 0{,}01$ thì trong 10000 cá thể chỉ có $q^2\times10^4 = 1$ cá thể đồng hợp lặn để chọn lọc "nhìn thấy" (mang 2 alen lặn lộ ra), trong khi có $2pq\times10^4 \approx 198$ cá thể dị hợp mang 198 alen lặn **ẩn** và hoàn toàn miễn nhiễm với chọn lọc — tỉ số ẩn trên lộ là $2q/(2q^2) = 1/q = 100$.

Hệ quả xã hội quan trọng: chương trình loại bỏ người bệnh không thể xoá được alen lặn hiếm khỏi quần thể — con số cho thấy phải hàng nghìn thế hệ để giảm được một bậc.

## Cân bằng đột biến - chọn lọc

Alen có hại vẫn tồn tại ở tần số cân bằng: với alen lặn $\hat q = \sqrt{\mu/s}$, với alen trội $\hat q = \mu/s$. Đây là lời giải cho câu hỏi vì sao bệnh di truyền không biến mất.

## Ưu thế dị hợp

Khi dị hợp thích nghi nhất, chọn lọc **duy trì** cả hai alen ở tần số cân bằng $\hat q = s_1/(s_1+s_2)$. Alen hồng cầu hình liềm ở vùng sốt rét là ví dụ kinh điển: đồng hợp $HbS$ chết sớm, nhưng dị hợp kháng sốt rét nên alen được giữ ở tần số cao tới 0,1-0,15.

## Trôi dạt và $N_e$

Trôi dạt là biến động ngẫu nhiên do lấy mẫu giao tử hữu hạn; cường độ tỉ lệ $1/(2N_e)$. Quy tắc so sánh then chốt:

- Nếu $|s| \gg 1/(2N_e)$: chọn lọc chi phối.
- Nếu $|s| \ll 1/(2N_e)$: alen coi như trung tính, số phận do trôi dạt định.

Vì vậy cùng một alen có $s = 0{,}001$ sẽ được chọn lọc hiệu quả trong quần thể vi khuẩn $N_e = 10^8$ nhưng hoàn toàn trung tính trong quần thể động vật có vú $N_e = 100$. **Trung tính không phải tính chất của alen, mà là quan hệ giữa alen và quần thể.**

$N_e$ luôn nhỏ hơn số cá thể đếm được, bị kéo xuống bởi tỉ lệ giới tính lệch, biến động kích thước qua các thế hệ (trung bình điều hoà bị chi phối bởi giá trị nhỏ nhất) và chênh lệch số con.

**Lỗi thường gặp:**
- Cho rằng loại bỏ người mắc bệnh lặn sẽ nhanh chóng xoá alen bệnh khỏi quần thể. Khi $q$ nhỏ, tỉ số alen ẩn trong dị hợp tử trên alen lộ ra bằng $1/q$; với $q = 0{,}01$ có tới 99% alen bệnh nằm ngoài tầm chọn lọc.
- Coi "trung tính" là một tính chất cố hữu của đột biến. Một đột biến có $s = 0{,}001$ là trung tính trong quần thể $N_e = 100$ nhưng chịu chọn lọc mạnh khi $N_e = 10^6$; ranh giới là so sánh $|s|$ với $1/(2N_e)$.
- Lấy trung bình cộng khi tính $N_e$ của quần thể có kích thước biến động. Phải dùng trung bình điều hoà, vốn bị chi phối bởi thế hệ có kích thước nhỏ nhất; một lần thắt cổ chai kéo $N_e$ xuống rất lâu sau khi số lượng đã hồi phục.
- Nghĩ chọn lọc luôn làm giảm đa dạng di truyền. Ưu thế dị hợp và chọn lọc phụ thuộc tần số duy trì đa hình ở trạng thái cân bằng ổn định — alen hồng cầu hình liềm tồn tại ở tần số cao chính nhờ cơ chế này.

<sub>`lesson.biology.di-truyen-hoc.chon-loc-troi-dat-va-tien-hoa`</sub>

---

### 7. Genomics, nghiên cứu liên kết toàn hệ gen và tư vấn di truyền
*Genomics, GWAS and genetic counselling* · Đại học · intl-undergrad · 50 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao GWAS phát hiện được tín hiệu ở các SNP không phải là biến thể gây bệnh
- Vận dụng được hiệu chỉnh đa kiểm định để đặt ngưỡng ý nghĩa toàn hệ gen
- Vận dụng được định lí Bayes để tính nguy cơ trong bài toán phả hệ

## GWAS đo cái gì

GWAS so sánh tần số alen tại hàng triệu SNP giữa nhóm bệnh và nhóm chứng. Điểm cốt lõi thường bị hiểu sai: SNP cho tín hiệu **hầu như không bao giờ là biến thể gây bệnh**. Nó chỉ nằm trong cùng khối mất cân bằng liên kết với biến thể thật. Vì vậy sau GWAS luôn phải có bước tinh chỉnh bản đồ và nghiên cứu chức năng.

## Vấn đề đa kiểm định

Với một triệu SNP và ngưỡng $\alpha = 0{,}05$, ta kì vọng 50000 kết quả dương tính giả. Hiệu chỉnh Bonferroni cho ngưỡng $0{,}05/10^{6} = 5\times10^{-8}$ — đây chính là nguồn gốc của con số quen thuộc trong mọi bài báo GWAS.

Bonferroni là bảo thủ vì các SNP không độc lập (chúng liên kết với nhau). Với dữ liệu biểu hiện gen, kiểm soát tỉ lệ phát hiện sai FDR theo Benjamini - Hochberg thường phù hợp hơn: nó chấp nhận một tỉ lệ dương tính giả xác định trong số các phát hiện, đổi lấy độ mạnh cao hơn nhiều.

## Vì sao GWAS giải thích được ít

Phần lớn biến thể tìm được có tỉ số chênh 1,1-1,3 và tổng cộng chỉ giải thích một phần nhỏ độ di truyền ước lượng từ phả hệ. Ba lời giải thích chính: biến thể hiếm không có trên chip SNP, hiệu ứng rất nhỏ nằm dưới ngưỡng phát hiện, và tương tác gen - gen, gen - môi trường. Điểm phương pháp luận: một biến thể có ý nghĩa thống kê ở cỡ mẫu $10^5$ vẫn có thể **vô dụng về mặt tiên lượng cá thể**.

## Từ quần thể tới cá nhân

Tư vấn di truyền không dùng thống kê quần thể trực tiếp mà cập nhật xác suất theo Bayes. Cấu trúc bài toán luôn gồm ba phần: xác suất tiên nghiệm từ phả hệ, khả năng quan sát được dữ liệu (số con khoẻ, kết quả xét nghiệm) dưới mỗi giả thuyết, và chuẩn hoá để ra hậu nghiệm.

## Nguyên tắc đạo đức

Ba nguyên tắc chi phối tư vấn: không định hướng (đưa thông tin, không khuyên quyết định sinh sản), bảo mật (kết quả của một người là thông tin của cả gia đình — mâu thuẫn thực sự chưa có lời giải chung), và quyền không biết (bệnh nhân có quyền từ chối biết nguy cơ, đặc biệt với bệnh chưa có điều trị như Huntington).

**Lỗi thường gặp:**
- Cho rằng SNP đạt ý nghĩa trong GWAS chính là biến thể gây bệnh. Trong đại đa số trường hợp nó chỉ là marker nằm cùng khối mất cân bằng liên kết với biến thể thật, và biến thể thật thường nằm ở vùng điều hoà chứ không ở vùng mã hoá.
- Dùng ngưỡng $p < 0{,}05$ cho từng SNP trong GWAS. Với một triệu kiểm định, ngưỡng đó cho khoảng 50000 kết quả dương tính giả; ngưỡng đúng sau hiệu chỉnh Bonferroni là $5\times10^{-8}$.
- Quên điều kiện hoá trên thông tin đã biết khi tính xác suất tiên nghiệm trong phả hệ. Người tư vấn đã được biết là không mắc bệnh, nên phải loại kiểu gen bệnh khỏi không gian mẫu; dùng tỉ lệ 1:2:1 thay vì 1:2 sẽ cho kết quả sai ngay từ bước đầu.
- Diễn giải ý nghĩa thống kê thành ý nghĩa lâm sàng. Một biến thể có $p = 10^{-20}$ với tỉ số chênh 1,15 gần như vô dụng để dự báo cho một cá nhân; cỡ mẫu lớn làm giá trị $p$ nhỏ mà không làm hiệu ứng lớn thêm.

<sub>`lesson.biology.di-truyen-hoc.genomics-gwas-va-tu-van-di-truyen`</sub>

---

## Unit 6: Sinh lí học

### 1. Điện thế màng lúc nghỉ: phương trình Nernst và Goldman
*Resting membrane potential: the Nernst and Goldman equations* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Tính được điện thế cân bằng của một ion bằng phương trình Nernst
- Vận dụng được phương trình Goldman - Hodgkin - Katz để giải thích điện thế nghỉ thực tế
- Phân tích được vai trò trực tiếp và gián tiếp của bơm natri - kali đối với điện thế màng

## Một gradient chưa đủ để có điện thế

Màng phải vừa có gradient nồng độ vừa **thấm chọn lọc**. Nếu màng không thấm ion nào, dù gradient lớn tới đâu cũng không có điện thế; nếu màng thấm mọi ion như nhau, các gradient triệt tiêu nhau.

## Nernst: trường hợp một ion

$$E_{ion} = \frac{RT}{zF}\ln\frac{[\text{ion}]_{ngoài}}{[\text{ion}]_{trong}} \approx \frac{61}{z}\log_{10}\frac{[\text{ion}]_{ngoài}}{[\text{ion}]_{trong}}\ \mathrm{(mV\ ở\ 37^\circ C)}$$

Với nồng độ điển hình của neuron: $E_K \approx -90$ mV, $E_{Na} \approx +60$ mV, $E_{Cl} \approx -70$ mV, $E_{Ca} \approx +120$ mV.

Cách đọc quan trọng: $E_{ion}$ là **đích** mà ion đó kéo điện thế màng về.

## Goldman: nhiều ion cùng lúc

$$V_m = 61\log_{10}\frac{P_K[K^+]_o + P_{Na}[Na^+]_o + P_{Cl}[Cl^-]_i}{P_K[K^+]_i + P_{Na}[Na^+]_i + P_{Cl}[Cl^-]_o}$$

Chú ý $Cl^-$ đảo vị trí tử số - mẫu số vì mang điện âm. Điện thế nghỉ là **trung bình có trọng số** của các $E_{ion}$, trọng số là tính thấm. Ở neuron nghỉ, $P_K : P_{Na} \approx 100:1$ nên $V_m = -70$ mV, nằm gần $E_K$ nhưng dương hơn một chút — đúng bằng phần "kéo" của dòng $Na^+$ rò vào.

## Vai trò thật của bơm $Na^+/K^+$

Hai vai trò, và vai trò lớn hơn là gián tiếp:
- **Trực tiếp**: bơm sinh điện, đóng góp khoảng $-5$ mV.
- **Gián tiếp và quyết định**: duy trì gradient nồng độ. Nếu ngừng bơm, điện thế không sập ngay (vì gradient còn) nhưng suy giảm dần trong vài chục phút khi gradient tan.

Đây là điểm phân biệt hiểu sâu và hiểu thuộc lòng: bơm không "tạo ra" điện thế nghỉ, nó nạp lại pin mà kênh rò đang xả.

## Ứng dụng lâm sàng trực tiếp

Tăng kali máu làm $[K^+]_o$ tăng, $E_K$ dương hơn, màng khử cực dai dẳng. Kênh $Na^+$ bị bất hoạt kéo dài nên tế bào **mất khả năng phát xung** — nghịch lí biểu kiến: khử cực nhưng lại giảm kích thích, và đây là cơ chế gây ngừng tim khi kali máu cao.

**Lỗi thường gặp:**
- Cho rằng điện thế nghỉ do bơm $Na^+/K^+$ trực tiếp tạo ra. Bơm chỉ đóng góp khoảng $-5$ mV trực tiếp; phần lớn điện thế đến từ dòng $K^+$ đi ra qua kênh rò, còn bơm có vai trò duy trì gradient để dòng đó tồn tại lâu dài.
- Đảo ngược tỉ số nồng độ trong phương trình Nernst hoặc quên đảo vị trí của $Cl^-$ trong Goldman. Ion âm có $z = -1$, nên trong dạng Goldman nồng độ trong của $Cl^-$ nằm ở tử số; sai chỗ này làm đổi dấu kết quả.
- Nghĩ tăng kali máu làm tế bào dễ kích thích hơn vì màng gần ngưỡng hơn. Khử cực **kéo dài** đưa kênh natri vào trạng thái bất hoạt, mà kênh bất hoạt chỉ hồi phục khi màng tái phân cực; kết quả thực tế là giảm kích thích và có thể ngừng tim.
- Áp dụng Nernst cho toàn màng khi có nhiều ion thấm. Nernst chỉ mô tả trạng thái cân bằng của một ion duy nhất; điện thế nghỉ thực tế là trạng thái ổn định có dòng ròng khác không của từng ion, nên phải dùng Goldman.

<sub>`lesson.biology.sinh-li-hoc.dien-the-mang-nghi`</sub>

---

### 2. Điện thế hoạt động và dẫn truyền xung thần kinh
*The action potential and nerve conduction* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được cơ chế phản hồi dương của kênh natri và vì sao điện thế hoạt động có tính tất cả hoặc không
- Phân biệt được trạng thái đóng, mở và bất hoạt của kênh natri và liên hệ với thời kì trơ
- Phân tích được ảnh hưởng của đường kính sợi và bao myelin lên tốc độ dẫn truyền

## Phản hồi dương và tính tất cả hoặc không

Khử cực mở kênh $Na^+$ → $Na^+$ vào → khử cực thêm → mở thêm kênh. Vòng lặp này không có điểm dừng ở giữa: một khi vượt ngưỡng, điện thế bắt buộc chạy tới đỉnh. Đó là lí do điện thế hoạt động **không có biên độ trung gian** — nó là tín hiệu số, không phải tín hiệu tương tự.

Hệ quả tất yếu: thông tin về cường độ kích thích không thể mã hoá bằng biên độ, mà phải mã hoá bằng **tần số** xung.

## Vì sao phải có hai cổng

Kênh $Na^+$ có cổng hoạt hoá nhanh và cổng bất hoạt chậm. Nếu chỉ có một cổng, phản hồi dương sẽ khoá màng ở trạng thái khử cực vĩnh viễn. Cổng bất hoạt đóng sau khoảng 1 ms, cắt dòng $Na^+$; đồng thời kênh $K^+$ mở chậm đưa màng về nghỉ.

Ba trạng thái kênh — đóng sẵn sàng, mở, bất hoạt — giải thích trực tiếp hai thời kì trơ. **Trơ tuyệt đối**: mọi kênh đang bất hoạt, không kích thích nào gây được xung. **Trơ tương đối**: một phần kênh đã hồi phục, cần kích thích mạnh hơn. Ý nghĩa: thời kì trơ vừa đặt giới hạn trên cho tần số phát xung, vừa buộc xung chỉ lan **một chiều** vì vùng vừa đi qua đang trơ.

## Tốc độ dẫn truyền phụ thuộc gì

Hai cách tăng tốc:
1. **Tăng đường kính**: điện trở dọc sợi giảm theo bình phương bán kính, hằng số không gian tăng theo $\sqrt{d}$. Mực ống dùng cách này với sợi khổng lồ đường kính 1 mm.
2. **Myelin hoá**: tăng điện trở màng và giảm điện dung, làm hằng số không gian dài ra và hằng số thời gian ngắn lại. Sợi có myelin đường kính 20 µm dẫn 120 m/s, nhanh hơn sợi mực khổng lồ dày gấp 50 lần.

Myelin hiệu quả hơn nhiều về mặt không gian và năng lượng — đó là lí do động vật có xương sống chọn giải pháp này.

## Khi myelin hỏng

Trong xơ cứng rải rác, mảng mất myelin làm dòng điện rò ra qua vùng màng trần vốn có rất ít kênh $Na^+$. Tín hiệu suy giảm dưới ngưỡng trước khi tới eo Ranvier tiếp theo và dẫn truyền bị **chặn hoàn toàn** chứ không chỉ chậm lại — cơ sở của mất chức năng đột ngột theo từng đợt.

**Lỗi thường gặp:**
- Cho rằng cường độ kích thích mạnh làm điện thế hoạt động có biên độ lớn hơn. Do phản hồi dương, biên độ luôn như nhau; cường độ được mã hoá bằng tần số xung và bằng số sợi được huy động.
- Giải thích thời kì trơ bằng việc bơm $Na^+/K^+$ chưa kịp phục hồi gradient. Một điện thế hoạt động chỉ trao đổi khoảng một phần triệu lượng ion nội bào; thời kì trơ hoàn toàn do kênh $Na^+$ đang ở trạng thái bất hoạt.
- Nghĩ myelin giúp dẫn truyền vì nó "dẫn điện tốt". Ngược lại, myelin là chất **cách điện**: nó tăng điện trở màng và giảm điện dung, khiến dòng điện chạy dọc trong bào tương thay vì rò ra ngoài.
- Coi mất myelin chỉ làm dẫn truyền chậm đi. Khi hằng số không gian giảm đủ nhiều, tín hiệu tới eo Ranvier kế tiếp đã dưới ngưỡng và dẫn truyền bị chặn hẳn — đó là lí do triệu chứng xuất hiện đột ngột chứ không tăng dần.

<sub>`lesson.biology.sinh-li-hoc.dien-the-hoat-dong-va-dan-truyen`</sub>

---

### 3. Dẫn truyền synapse và tích hợp tín hiệu ở neuron
*Synaptic transmission and neuronal integration* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Mô tả được chuỗi sự kiện từ điện thế hoạt động tới giải phóng chất dẫn truyền thần kinh
- Phân biệt được điện thế sau synapse hưng phấn và ức chế theo cơ sở ion học
- Giải thích được cộng gộp không gian, cộng gộp thời gian và vai trò của gò sợi trục

## Chuỗi sự kiện

Điện thế hoạt động tới cúc tận cùng → kênh $Ca^{2+}$ phụ thuộc điện thế mở → $Ca^{2+}$ vào → synaptotagmin cảm nhận $Ca^{2+}$ và kích hoạt phức hợp SNARE → túi dung hợp và giải phóng chất dẫn truyền → chất dẫn truyền khuếch tán qua khe 20 nm → gắn thụ thể sau synapse.

Điểm cần nhấn: **$Ca^{2+}$ là mắt xích bắt buộc**. Bỏ $Ca^{2+}$ khỏi dịch ngoại bào thì điện thế hoạt động vẫn tới cúc tận cùng nhưng không có giải phóng nào cả. Đây cũng là lí do quan hệ giữa $[Ca^{2+}]$ và lượng giải phóng có bậc rất cao (mũ 3-4), tức là hệ có tính hợp tác mạnh.

## Vì sao EPSP đảo cực ở 0 mV

Thụ thể nicotinic và AMPA là kênh cation không chọn lọc, cho cả $Na^+$ vào lẫn $K^+$ ra. Điện thế đảo là trung bình của $E_{Na}$ ($+60$) và $E_K$ ($-90$), rơi vào khoảng $0$ mV. Vì $0$ mV luôn dương hơn điện thế nghỉ, dòng này **luôn** khử cực.

Ngược lại, GABA$_A$ và glycine mở kênh $Cl^-$ với $E_{Cl} \approx -70$ mV, xấp xỉ điện thế nghỉ. Do đó ức chế nhiều khi không làm màng âm thêm mà chỉ **giữ chặt** màng ở gần $E_{Cl}$ và làm tăng độ dẫn — ức chế phân dòng. Hiệu quả ức chế nằm ở chỗ nó làm dòng hưng phấn bị rò mất chứ không ở chỗ nó hạ điện thế.

## Tích hợp: neuron là bộ cộng có ngưỡng

Một EPSP đơn lẻ chỉ khoảng 0,5-1 mV, trong khi cần khoảng 15-20 mV để đạt ngưỡng. Vậy neuron phải cộng:
- **Cộng gộp thời gian**: nhiều xung liên tiếp từ cùng một synapse, hiệu quả khi khoảng cách nhỏ hơn hằng số thời gian màng.
- **Cộng gộp không gian**: nhiều synapse cùng hoạt động, hiệu quả khi chúng nằm trong khoảng hằng số không gian.

Quyết định cuối cùng diễn ra tại gò sợi trục, nơi mật độ kênh $Na^+$ cao nhất. Vị trí của synapse do đó rất quan trọng: synapse trên thân tế bào có ảnh hưởng lớn hơn nhiều so với synapse ở đầu xa của tua gai, và synapse ức chế đặt ngay tại gốc tua gai có thể vô hiệu toàn bộ nhánh đó.

## Tính mềm dẻo

Kích thích tần số cao gây tăng cường dài hạn (LTP) qua thụ thể NMDA — thụ thể này là **bộ phát hiện trùng hợp** vì cần đồng thời glutamate gắn và màng đã khử cực để đẩy $Mg^{2+}$ ra khỏi kênh. Đó là cơ sở phân tử của quy tắc Hebb: các neuron cùng hoạt động thì liên kết mạnh lên.

**Lỗi thường gặp:**
- Cho rằng ức chế luôn làm màng âm hơn điện thế nghỉ. Vì $E_{Cl}$ xấp xỉ điện thế nghỉ, nhiều synapse ức chế gần như không đổi điện thế; tác dụng của chúng là tăng độ dẫn màng làm rò mất dòng hưng phấn (ức chế phân dòng).
- Nghĩ điện thế hoạt động phát sinh ngay tại nơi synapse hoạt động mạnh nhất. Nơi khởi phát luôn là gò sợi trục vì mật độ kênh natri ở đó cao nhất; EPSP phải lan thụ động tới đó và bị suy giảm trên đường đi.
- Bỏ qua vai trò của $Ca^{2+}$ và cho rằng khử cực đủ để giải phóng chất dẫn truyền. Trong dung dịch không có $Ca^{2+}$, điện thế hoạt động vẫn tới cúc tận cùng nhưng không có túi nào dung hợp; $Ca^{2+}$ là tín hiệu kích hoạt trực tiếp qua synaptotagmin.
- Cộng các EPSP liên tiếp bằng phép nhân đơn thuần với số xung. Mỗi EPSP đã suy giảm theo hàm mũ trước khi cái sau tới, nên tổng là cấp số nhân có giới hạn hữu hạn, thường thấp hơn ngưỡng rất nhiều.

<sub>`lesson.biology.sinh-li-hoc.dan-truyen-synapse`</sub>

---

### 4. Sinh lí cơ: cơ chế trượt sợi và quan hệ lực - chiều dài
*Muscle physiology: the sliding filament mechanism and length-tension relationship* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Mô tả được chu kì cầu ngang và vai trò của ATP ở từng bước
- Giải thích được quan hệ lực - chiều dài dựa trên mức chồng lấn của sợi actin và myosin
- Phân biệt được cơ vân, cơ tim và cơ trơn về cơ chế ghép kích thích - co cơ

## Cơ chế trượt sợi

Sarcomere ngắn lại **không** phải vì sợi actin hay myosin co lại — chiều dài mỗi loại sợi không đổi. Chúng trượt lên nhau. Bằng chứng quyết định: dưới kính hiển vi, băng A (chiều dài sợi dày) giữ nguyên trong khi băng I và vùng H hẹp lại.

## ATP làm gì trong chu kì cầu ngang

Đây là chỗ trực giác thường sai. Trình tự đúng:
1. ATP gắn vào đầu myosin → myosin **nhả** actin.
2. Thuỷ phân ATP → đầu myosin dựng lên, tích năng lượng (trạng thái nạp).
3. Gắn actin → nhả $P_i$ → **cú đập lực** kéo sợi mảnh.
4. Nhả ADP → trạng thái cứng, chờ ATP mới.

Vậy ATP cần cho việc **tách rời**, không phải cho việc kéo. Bằng chứng lâm sàng: khi chết, ATP cạn nên myosin không nhả được actin — đó chính là cứng xác. Suy luận này chỉ đúng nếu hiểu đúng vai trò ATP.

## Quan hệ lực - chiều dài

Lực tỉ lệ với số cầu ngang tạo được, tức tỉ lệ với mức chồng lấn:
- Sarcomere quá dài ($>3{,}6$ µm): không chồng lấn, lực bằng 0.
- Vùng tối ưu (2,0-2,2 µm): mọi đầu myosin đều có actin đối diện, lực cực đại.
- Quá ngắn ($<2{,}0$ µm): sợi mảnh từ hai đầu chồng lên nhau gây cản, sợi dày chạm đĩa Z, lực giảm.

Cơ thể giữ chiều dài cơ nghỉ ở gần vùng tối ưu. Ở tim, đường cong này chính là **định luật Frank - Starling**: tim nhận nhiều máu về thì sợi cơ dài ra về phía tối ưu và co mạnh hơn.

## Ba loại cơ, ba cách ghép

- **Cơ vân**: ghép cơ học trực tiếp, $Ca^{2+}$ hoàn toàn từ lưới cơ tương; không cần $Ca^{2+}$ ngoại bào. Điều hoà ở sợi mảnh qua troponin - tropomyosin.
- **Cơ tim**: cần $Ca^{2+}$ ngoại bào để kích hoạt giải phóng $Ca^{2+}$ từ lưới cơ tương. Vì vậy thuốc chẹn kênh calci ảnh hưởng tim mà không làm liệt cơ vân.
- **Cơ trơn**: điều hoà ở sợi dày, qua phosphoryl hoá chuỗi nhẹ myosin nhờ kinase phụ thuộc $Ca^{2+}$-calmodulin; co chậm nhưng duy trì lực với chi phí ATP rất thấp — phù hợp với vai trò giữ trương lực mạch máu suốt đời.

**Lỗi thường gặp:**
- Nói ATP cung cấp năng lượng cho cú đập lực ngay tại thời điểm kéo. Năng lượng thuỷ phân được dùng để **nạp** lại đầu myosin ở bước trước; việc gắn ATP mới có tác dụng tách myosin khỏi actin, và chính vì thiếu ATP mà xác cứng lại.
- Cho rằng sợi actin và myosin ngắn lại khi cơ co. Chiều dài mỗi sợi không đổi; quan sát băng A giữ nguyên trong khi băng I hẹp lại là bằng chứng trực tiếp cho cơ chế trượt.
- Giải thích lực giảm ở sarcomere quá ngắn bằng việc thiếu chồng lấn. Ở chiều dài ngắn, chồng lấn thậm chí nhiều hơn; lực giảm vì sợi mảnh từ hai phía cản nhau và sợi dày bị đĩa Z ép, tức là do trở ngại cơ học chứ không do thiếu cầu ngang tiềm năng.
- Áp dụng cơ chế của cơ vân cho cơ tim. Cơ tim bắt buộc cần $Ca^{2+}$ ngoại bào để khởi động giải phóng $Ca^{2+}$ từ lưới cơ tương, nên chẹn kênh calci làm giảm co bóp tim trong khi cơ vân hầu như không bị ảnh hưởng.

<sub>`lesson.biology.sinh-li-hoc.sinh-li-co`</sub>

---

### 5. Chu kì tim, cung lượng tim và định luật Frank - Starling
*The cardiac cycle, cardiac output and the Frank-Starling law* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân tích được bốn pha của chu kì tim theo quan hệ áp suất - thể tích
- Tính được cung lượng tim, phân suất tống máu và chỉ số tim từ số liệu lâm sàng
- Phân biệt được ảnh hưởng của tiền gánh, hậu gánh và sức co bóp lên thể tích tống máu

## Bốn pha đọc trên vòng áp suất - thể tích

1. **Đổ đầy tâm trương**: van hai lá mở, thể tích tăng, áp suất tăng rất ít (tâm thất giãn tốt).
2. **Co đẳng tích**: cả hai van đóng, áp suất tăng vọt, thể tích không đổi.
3. **Tống máu**: van động mạch chủ mở, thể tích giảm.
4. **Giãn đẳng tích**: cả hai van đóng, áp suất giảm nhanh.

Diện tích bên trong vòng chính là **công cơ học** của tâm thất trong một nhịp. Đây là lí do vòng P-V là công cụ mạnh hơn nhiều so với việc học thuộc các mốc thời gian.

## Cung lượng tim

$$CO = SV\times HR, \qquad SV = EDV - ESV, \qquad EF = \frac{SV}{EDV}$$

Chỉ số tim chuẩn hoá theo diện tích bề mặt cơ thể để so sánh giữa các cá thể khác kích thước. Giá trị bình thường: $CO \approx 5$ L/phút, $EF \ge 0{,}55$, chỉ số tim 2,5-4,0 L·phút⁻¹·m⁻².

## Frank - Starling: tim tự điều chỉnh

Tăng thể tích cuối tâm trương → sarcomere kéo dài về vùng tối ưu → lực co mạnh hơn → thể tích tống máu tăng. Ý nghĩa hệ thống: **tim tự động bơm ra đúng lượng máu nó nhận về**, không cần bất kì tín hiệu thần kinh nào. Nếu không có cơ chế này, chỉ cần chênh lệch nhỏ giữa hai tâm thất là máu sẽ dồn ứ ở một bên trong vài phút.

Cơ chế phân tử không chỉ là chồng lấn: kéo dài sarcomere còn làm tăng **độ nhạy của troponin C với $Ca^{2+}$**, nên tim khai thác quan hệ lực - chiều dài hiệu quả hơn cơ vân.

## Ba biến độc lập

- Tăng **tiền gánh** (truyền dịch): $SV$ tăng, di chuyển **dọc theo** cùng một đường cong Starling.
- Tăng **hậu gánh** (tăng huyết áp): $SV$ giảm, $ESV$ tăng.
- Tăng **sức co bóp** (adrenaline, digoxin): **đổi sang đường cong khác** — cùng một tiền gánh cho $SV$ lớn hơn.

Phân biệt ba biến này là chìa khoá của điều trị suy tim: lợi tiểu giảm tiền gánh, thuốc giãn mạch giảm hậu gánh, thuốc tăng co bóp đổi đường cong.

## Nhu cầu oxygen của tim

Tim tiêu oxygen chủ yếu theo **áp suất** phải sinh ra, không theo thể tích tống. Vì vậy hẹp van động mạch chủ (hậu gánh cao) gây thiếu máu cơ tim nặng hơn nhiều so với hở van cùng mức độ nặng — một hệ quả trực tiếp và có thể kiểm chứng của phân tích vòng P-V.

**Lỗi thường gặp:**
- Tính phân suất tống máu bằng $SV/ESV$. Định nghĩa là $SV/EDV$ — tỉ lệ máu được tống trên tổng lượng máu có trong thất cuối tâm trương; nhầm mẫu số cho giá trị lớn hơn 100% ở người bình thường.
- Cho rằng tăng nhịp tim luôn làm tăng cung lượng tim. Ở nhịp rất nhanh, thời gian tâm trương ngắn lại nên thất không kịp đổ đầy, $EDV$ và $SV$ giảm; cung lượng đạt cực đại rồi giảm khi nhịp vượt khoảng 180 lần/phút.
- Nhầm tăng sức co bóp với tăng tiền gánh vì cả hai đều làm tăng thể tích tống máu. Tiền gánh dịch chuyển điểm làm việc **dọc theo** một đường cong Starling, còn sức co bóp **đổi sang đường cong khác**; hai can thiệp điều trị hoàn toàn khác nhau.
- Nghĩ nhu cầu oxygen của cơ tim tỉ lệ với lượng máu bơm ra. Nó tỉ lệ chủ yếu với áp suất mà thất phải sinh và với nhịp tim; đó là lí do hậu gánh cao gây thiếu máu cơ tim nặng hơn tăng thể tích cùng mức.

<sub>`lesson.biology.sinh-li-hoc.sinh-li-tim-va-cung-luong`</sub>

---

### 6. Huyết động học: sức cản, định luật Poiseuille và trao đổi mao mạch
*Haemodynamics: resistance, Poiseuille's law and capillary exchange* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được định luật Poiseuille để giải thích vai trò then chốt của bán kính mạch
- Tính được huyết áp động mạch trung bình và sức cản mạch hệ thống
- Phân tích được cân bằng lực Starling quyết định chiều dòng dịch qua thành mao mạch

## Bán kính là tất cả

Định luật Hagen - Poiseuille cho dòng chảy tầng:

$$Q = \frac{\pi \Delta P r^{4}}{8\eta L} \quad \Longrightarrow \quad R = \frac{8\eta L}{\pi r^{4}}$$

Sức cản tỉ lệ nghịch với **luỹ thừa bốn** của bán kính. Giảm bán kính 20% làm sức cản tăng $1/0{,}8^4 = 2{,}44$ lần. Đây là lí do tiểu động mạch — không phải mao mạch — là nơi điều hoà: chỉ cần co nhẹ cơ trơn là thay đổi được dòng máu tới cả một cơ quan.

## Vì sao mao mạch có sức cản thấp dù rất hẹp

Mỗi mao mạch có sức cản khổng lồ, nhưng chúng mắc **song song** với số lượng khoảng $10^{10}$. Với mạch song song, $1/R_{tổng} = \sum 1/R_i$, nên tổng sức cản rất nhỏ. Cùng lí do đó, tổng tiết diện ngang của giường mao mạch lớn gấp khoảng 700 lần động mạch chủ, khiến vận tốc máu ở mao mạch chậm nhất — đúng điều cần cho trao đổi chất.

## Huyết áp trung bình

$$MAP \approx DBP + \frac{1}{3}(SBP-DBP)$$

Hệ số $1/3$ chứ không phải $1/2$ vì tim ở tâm trương lâu hơn tâm thu. Với hệ tuần hoàn coi như mạch điện:

$$MAP = CO \times SVR$$

Đây là phương trình trung tâm của mọi phân tích sốc: huyết áp tụt thì hoặc do cung lượng giảm (sốc tim, sốc giảm thể tích) hoặc do sức cản giảm (sốc nhiễm khuẩn, sốc phản vệ) — và hai nhóm cần điều trị ngược nhau.

## Định luật Laplace và hệ quả

Với mạch máu, sức căng thành $T = P\times r$. Ở phình động mạch chủ, bán kính lớn làm sức căng thành tăng theo, càng phình càng dễ vỡ — một vòng phản hồi dương giải thích vì sao phình lớn có nguy cơ vỡ tăng vọt chứ không tuyến tính.

## Trao đổi mao mạch

$$J_v = K_f[(P_c - P_i) - \sigma(\pi_c - \pi_i)]$$

Ở đầu tiểu động mạch, áp suất thuỷ tĩnh $P_c \approx 35$ mmHg vượt áp suất keo $\pi_c \approx 25$ mmHg → lọc ra. Ở đầu tiểu tĩnh mạch, $P_c$ giảm còn khoảng 15 mmHg → tái hấp thu vào. Khoảng 10% dịch lọc không quay lại và được hệ bạch huyết dẫn về.

Phù xuất hiện khi bất kì số hạng nào lệch: suy tim làm $P_c$ tăng, xơ gan hay hội chứng thận hư làm $\pi_c$ giảm, viêm làm $K_f$ và tính thấm protein tăng, tắc bạch huyết làm mất đường thoát. Bốn cơ chế, một công thức.

**Lỗi thường gặp:**
- Lấy trung bình cộng của huyết áp tâm thu và tâm trương để tính $MAP$. Thời gian tâm trương dài gấp khoảng hai lần tâm thu ở nhịp bình thường, nên phải dùng trung bình có trọng số với hệ số $1/3$ cho hiệu áp.
- Cho rằng mao mạch là nơi có sức cản lớn nhất vì chúng hẹp nhất. Sức cản của từng mao mạch rất lớn nhưng chúng mắc song song với số lượng khổng lồ; nơi đóng góp sức cản chính là tiểu động mạch, nơi cơ trơn điều khiển bán kính.
- Bỏ qua luỹ thừa bốn khi ước lượng ảnh hưởng của co giãn mạch. Thay đổi bán kính 20% làm sức cản đổi gần 2,5 lần chứ không phải 20%; đây là sai lầm dẫn tới đánh giá sai hoàn toàn tác dụng của thuốc vận mạch.
- Giải thích mọi trường hợp phù bằng ứ dịch. Công thức Starling có bốn số hạng: phù có thể do tăng áp suất thuỷ tĩnh, giảm áp suất keo huyết tương, tăng tính thấm thành mạch, hoặc tắc dẫn lưu bạch huyết — điều trị của bốn nhóm này khác nhau.

<sub>`lesson.biology.sinh-li-hoc.huyet-dong-hoc`</sub>

---

### 7. Cơ học thông khí: áp suất màng phổi, độ giãn nở và khoảng chết
*Mechanics of ventilation: pleural pressure, compliance and dead space* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được vai trò của áp suất màng phổi âm và của chất hoạt diện phế nang
- Phân biệt được thông khí phút và thông khí phế nang, tính được khoảng chết
- Phân tích được rối loạn thông khí tắc nghẽn và hạn chế qua các chỉ số hô hấp kí

## Vì sao phổi không xẹp

Phổi luôn có xu hướng co lại (do sợi đàn hồi và sức căng bề mặt), lồng ngực có xu hướng nở ra. Hai lực ngược chiều tạo áp suất màng phổi **âm** khoảng $-5$ cmH₂O lúc cuối thở ra. Chọc thủng khoang màng phổi làm áp suất về 0, phổi xẹp và lồng ngực bật ra — tràn khí màng phổi là thí nghiệm tự nhiên chứng minh cơ chế này.

## Định luật Laplace và nghịch lí phế nang

Với bóng cầu, $P = 2T/r$. Nếu sức căng $T$ như nhau, phế nang **nhỏ** có áp suất cao hơn và sẽ xả khí vào phế nang lớn — mọi phế nang nhỏ phải xẹp hết. Thực tế không xảy ra vì chất hoạt diện có tính chất đặc biệt: khi phế nang nhỏ lại, phân tử hoạt diện dồn đặc hơn nên $T$ giảm nhiều hơn, bù đúng phần $r$ giảm.

Đây là lí do trẻ sinh non thiếu chất hoạt diện mắc hội chứng suy hô hấp: phổi vừa cứng vừa có xu hướng xẹp từng vùng.

## Thông khí phút không phải thông khí hữu ích

$$\dot V_E = V_T\times f, \qquad \dot V_A = (V_T - V_D)\times f$$

Vì khoảng chết bị trừ **mỗi nhịp**, thở nông nhanh kém hiệu quả hơn thở sâu chậm dù thông khí phút bằng nhau. Đây là một trong những kết luận có giá trị thực hành cao nhất của sinh lí hô hấp, và nó suy trực tiếp từ cấu trúc công thức.

## Đo khoảng chết

Phương trình Bohr dùng nguyên lí bảo toàn $CO_2$: toàn bộ $CO_2$ thở ra chỉ đến từ phần phế nang có trao đổi.

$$\frac{V_D}{V_T} = \frac{P_aCO_2 - P_ECO_2}{P_aCO_2}$$

Bình thường tỉ số này khoảng 0,3; tăng cao trong thuyên tắc phổi vì có vùng phổi được thông khí nhưng mất tưới máu.

## Đọc hô hấp kí

- **Tắc nghẽn** (hen, COPD): $FEV_1/FVC$ giảm dưới 0,7; khó thở ra nên khí bị bẫy lại, thể tích cặn tăng.
- **Hạn chế** (xơ phổi, gù vẹo cột sống): mọi thể tích giảm nhưng tỉ số $FEV_1/FVC$ **bình thường hoặc tăng**, vì cả tử số và mẫu số cùng giảm.

Quy tắc đọc: nhìn tỉ số trước để phân nhóm, rồi mới nhìn các thể tích tuyệt đối để đánh giá mức nặng.

**Lỗi thường gặp:**
- Đánh giá hiệu quả hô hấp bằng thông khí phút. Chỉ thông khí phế nang mới quyết định $P_aCO_2$; hai kiểu thở có cùng thông khí phút có thể chênh nhau gần hai lần về thông khí hữu ích.
- Cho rằng chất hoạt diện chỉ có tác dụng làm giảm sức căng bề mặt. Điều quyết định là nó giảm sức căng **mạnh hơn ở phế nang nhỏ**; nếu chỉ giảm đều thì nghịch lí Laplace vẫn khiến phế nang nhỏ xẹp vào phế nang lớn.
- Kết luận rối loạn hạn chế khi thấy $FEV_1$ giảm. $FEV_1$ giảm trong cả hai nhóm bệnh; tiêu chí phân biệt là tỉ số $FEV_1/FVC$ — giảm trong tắc nghẽn, bình thường hoặc tăng trong hạn chế.
- Nghĩ áp suất màng phổi âm là do cơ hoành chủ động hút. Áp suất âm tồn tại ngay cả khi mọi cơ hô hấp nghỉ, vì nó là kết quả của hai lực đàn hồi ngược chiều giữa phổi và thành ngực.

<sub>`lesson.biology.sinh-li-hoc.co-hoc-thong-khi`</sub>

---

### 8. Trao đổi khí ở phổi và vận chuyển oxygen, carbon dioxide trong máu
*Pulmonary gas exchange and transport of oxygen and carbon dioxide* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Vận dụng được phương trình khí phế nang để tính $P_AO_2$ và chênh lệch A-a
- Giải thích được hình dạng sigmoid của đường cong phân li oxyhemoglobin và ý nghĩa của các yếu tố làm dịch chuyển nó
- Tính được dung lượng oxygen của máu và phân tích các dạng thiếu oxy mô

## Khí phế nang không giống khí trời

$$P_AO_2 = F_iO_2(P_{atm}-P_{H_2O}) - \frac{P_aCO_2}{R}$$

Hai hiệu chỉnh bắt buộc: khí hít vào được làm ẩm hoàn toàn (trừ 47 mmHg hơi nước ở 37 °C) và $CO_2$ thải ra chiếm chỗ trong phế nang. Với khí trời ở mực nước biển, $P_AO_2 \approx 100$ mmHg chứ không phải 159 mmHg.

Chênh lệch A-a bình thường dưới 15 mmHg ở người trẻ. Giá trị này là công cụ chẩn đoán mạnh: giảm oxy máu **kèm** A-a bình thường chỉ ra giảm thông khí hoặc độ cao; giảm oxy máu **kèm** A-a tăng chỉ ra bệnh tại phổi.

## Vì sao đường cong oxyhemoglobin có dạng sigmoid

Hemoglobin có bốn tiểu đơn vị hợp tác dương (đã học ở bài dị lập thể). Hình dạng này có hai vùng chức năng rõ rệt:
- **Phần bằng phẳng** ($pO_2 > 60$ mmHg): bảo hiểm khi nạp. $pO_2$ giảm từ 100 xuống 60 mmHg chỉ làm bão hoà giảm từ 97% xuống 90%.
- **Phần dốc** ($pO_2$ 20-40 mmHg): ở mô, chỉ cần $pO_2$ giảm ít là nhả rất nhiều oxygen.

## Bốn yếu tố dịch phải

Tăng $CO_2$, giảm pH, tăng nhiệt độ, tăng 2,3-BPG. Điểm chung: tất cả đều là dấu hiệu của **mô đang hoạt động mạnh**. Nghĩa là chính mô cần oxygen nhất lại tự tạo điều kiện để hemoglobin nhả nhiều hơn — một cơ chế điều hoà cục bộ hoàn toàn tự động, không cần tín hiệu thần kinh.

Hemoglobin thai nhi (HbF) thiếu chuỗi $\beta$ nên gắn 2,3-BPG yếu, đường cong dịch **trái**, cho phép lấy oxygen từ máu mẹ qua nhau thai.

## Vận chuyển $CO_2$

Ba dạng: hoà tan (7%), carbamino gắn với hemoglobin (23%), và bicarbonat (70%). Dạng bicarbonat hình thành trong hồng cầu nhờ carbonic anhydrase, $HCO_3^-$ ra huyết tương đổi lấy $Cl^-$ (dịch chuyển chloride). Hiệu ứng Haldane bổ sung: hemoglobin đã nhả oxygen thì gắn $CO_2$ tốt hơn — nạp oxygen và thải $CO_2$ hỗ trợ lẫn nhau ở cả hai đầu tuần hoàn.

## Bốn kiểu thiếu oxy mô

Giảm oxy máu ($P_aO_2$ thấp), thiếu máu (Hb thấp, $P_aO_2$ bình thường), ứ trệ (dòng máu thấp), và nhiễm độc (mô không dùng được oxygen, như ngộ độc cyanide). Hai kiểu giữa có $P_aO_2$ và $SpO_2$ **hoàn toàn bình thường** — đây là lí do máy đo bão hoà không phát hiện được thiếu máu nặng hay ngộ độc CO.

**Lỗi thường gặp:**
- Dùng 159 mmHg làm $P_AO_2$ khi thở khí trời. Phải trừ 47 mmHg hơi nước và trừ phần chỗ $CO_2$ chiếm trong phế nang; bỏ hai hiệu chỉnh này làm chênh lệch A-a bị thổi phồng và dẫn tới chẩn đoán sai.
- Cho rằng $SpO_2$ bình thường loại trừ được thiếu oxy mô. Trong thiếu máu và ngộ độc CO hay cyanide, bão hoà đo được vẫn bình thường trong khi lượng oxygen thực tới mô rất thấp; máy đo bão hoà đo tỉ lệ, không đo lượng.
- Nghĩ tăng $P_aO_2$ bằng thở oxygen luôn cải thiện đáng kể dung lượng oxygen. Phần hoà tan chỉ $0{,}003\times P_aO_2$, tức tăng $P_aO_2$ thêm 100 mmHg chỉ thêm 0,3 mL/dL; muốn tăng nhiều phải tăng hemoglobin hoặc tăng bão hoà khi bão hoà đang thấp.
- Coi hiệu ứng Bohr là bất lợi vì làm hemoglobin gắn oxygen kém đi. Đó chính là điều mong muốn tại mô: vùng có $CO_2$ cao và pH thấp là vùng đang hoạt động mạnh, và ở đó hemoglobin cần nhả nhiều oxygen hơn.

<sub>`lesson.biology.sinh-li-hoc.trao-doi-va-van-chuyen-khi`</sub>

---

### 9. Sinh lí thận: lọc cầu thận, tái hấp thu và độ thanh thải
*Renal physiology: glomerular filtration, reabsorption and clearance* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Tính được áp suất lọc hữu hiệu và giải thích các yếu tố ảnh hưởng tới mức lọc cầu thận
- Vận dụng được khái niệm độ thanh thải để suy ra cơ chế xử lí của thận với một chất
- Giải thích được cơ chế nhân nồng độ ngược dòng tạo gradient tuỷ thận

## Ba quá trình, một phương trình

$$\text{Bài xuất} = \text{Lọc} - \text{Tái hấp thu} + \text{Bài tiết}$$

Độ thanh thải cho phép suy ngược cơ chế mà không cần đo trực tiếp. So với inulin (chỉ lọc, không tái hấp thu, không bài tiết):
- $C_x < GFR$: chất bị tái hấp thu ròng (glucose có $C \approx 0$).
- $C_x = GFR$: chỉ lọc (inulin, xấp xỉ creatinin).
- $C_x > GFR$: có bài tiết ròng (PAH có $C \approx$ lưu lượng huyết tương thận).

## Lọc cầu thận

$$NFP = P_{GC} - P_{BS} - \pi_{GC}$$

Điển hình: $60 - 15 - 29 = 16$ mmHg. Chú ý một điểm khác với mao mạch thường: dọc theo mao mạch cầu thận, nước bị lọc ra làm protein cô đặc lại nên $\pi_{GC}$ **tăng dần**, và lọc gần như dừng ở đầu ra.

Hai tiểu động mạch điều khiển độc lập cho hai hiệu ứng trái ngược:
- Co tiểu động mạch **đến**: giảm cả dòng máu thận lẫn GFR.
- Co tiểu động mạch **đi**: giảm dòng máu thận nhưng **tăng** GFR (giữ áp suất trong cầu thận).

Đây là cơ sở của tác dụng và tác dụng phụ của thuốc ức chế men chuyển: angiotensin II co tiểu động mạch đi để bảo vệ GFR khi tưới máu thận giảm; chặn nó giúp bảo vệ thận lâu dài nhưng có thể làm tụt GFR cấp ở bệnh nhân hẹp động mạch thận.

## Tái hấp thu bão hoà

Glucose được SGLT2 tái hấp thu hoàn toàn tới ngưỡng khoảng 10-11 mmol/L; trên ngưỡng, chất mang bão hoà và glucose niệu xuất hiện. Chính cơ chế này là đích của nhóm thuốc ức chế SGLT2 điều trị đái tháo đường — ép ngưỡng xuống để thải bớt glucose.

## Cơ chế cô đặc nước tiểu

Quai Henle tạo gradient dọc trục tuỷ thận nhờ hiệu ứng đơn nhỏ (200 mOsm) được dòng ngược chiều nhân lên. Urea tái tuần hoàn ở ống góp tuỷ đóng góp gần một nửa gradient. ADH mở kênh aquaporin-2 ở ống góp, cho nước ra theo gradient. Mạch thẳng vasa recta chạy ngược chiều nên **trao đổi** thụ động, lấy oxygen mà không rửa trôi gradient.

Điểm cần nhớ: quai Henle **tạo** gradient, ống góp **dùng** gradient, vasa recta **bảo tồn** gradient. Ba vai trò khác nhau, thường bị gộp lẫn.

**Lỗi thường gặp:**
- Cho rằng co tiểu động mạch nào cũng làm giảm mức lọc cầu thận. Co tiểu động mạch **đi** giữ áp suất trong cầu thận nên làm **tăng** GFR dù dòng máu thận giảm; đây là cơ chế bảo vệ GFR của angiotensin II.
- Dùng độ thanh thải creatinin như thước đo chính xác của GFR. Creatinin được bài tiết thêm một phần ở ống lượn gần nên độ thanh thải của nó cao hơn GFR thật khoảng 10-20%, và sai lệch này tăng lên khi chức năng thận giảm.
- Nghĩ quai Henle trực tiếp cô đặc nước tiểu. Quai Henle chỉ **tạo** gradient thẩm thấu ở tuỷ thận; việc cô đặc thực sự xảy ra ở ống góp và chỉ khi có ADH mở kênh aquaporin-2.
- Kì vọng glucose niệu chỉ xuất hiện khi tải lọc vượt đúng $T_m$. Do các nephron không đồng nhất, một số bão hoà sớm hơn, nên ngưỡng thận quan sát được luôn thấp hơn giá trị tính từ $T_m$ trung bình.

<sub>`lesson.biology.sinh-li-hoc.sinh-li-than-loc-va-tai-hap-thu`</sub>

---

### 10. Cân bằng nước - điện giải và cân bằng acid - base
*Water, electrolyte and acid-base balance* · Đại học · intl-undergrad · 55 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được điều hoà thể tích và điều hoà độ thẩm thấu về cảm biến và tín hiệu đáp ứng
- Phân tích được bốn rối loạn acid - base nguyên phát và mức bù trừ kì vọng
- Vận dụng được khoảng trống anion để thu hẹp chẩn đoán nguyên nhân nhiễm toan chuyển hoá

## Hai hệ điều hoà độc lập, hai đầu ra khác nhau

Đây là điểm dễ lẫn nhất trong sinh lí dịch thể:

| | Điều hoà độ thẩm thấu | Điều hoà thể tích |
|---|---|---|
| Cảm biến | Thụ thể thẩm thấu vùng dưới đồi | Thụ thể áp lực, bộ máy cạnh cầu thận |
| Đầu ra | ADH, cảm giác khát | Hệ renin - angiotensin - aldosterone, ANP |
| Điều chỉnh | **Nước** | **Natri** |

Quy tắc rút gọn: **nồng độ natri máu phản ánh cân bằng nước, không phản ánh lượng natri trong cơ thể.** Bệnh nhân suy tim phù to có thể hạ natri máu — thừa natri toàn cơ thể nhưng thừa nước còn nhiều hơn.

Khi hai hệ mâu thuẫn, **thể tích thắng**: mất máu nặng làm ADH tiết dù độ thẩm thấu thấp, vì duy trì tưới máu quan trọng hơn giữ nồng độ.

## Bốn rối loạn acid - base

Quy trình đọc gồm bốn bước, theo đúng thứ tự:
1. Xem pH: dưới 7,35 là toan, trên 7,45 là kiềm.
2. Xem $pCO_2$ và $HCO_3^-$: cái nào **cùng chiều** với rối loạn pH là nguyên phát.
3. Kiểm tra bù trừ có đúng mức kì vọng không. Với nhiễm toan chuyển hoá, công thức Winter: $pCO_2$ kì vọng $= 1{,}5[HCO_3^-] + 8 \pm 2$.
4. Nếu là nhiễm toan chuyển hoá, tính khoảng trống anion.

## Vì sao khoảng trống anion hữu ích

Mọi dung dịch phải trung hoà điện. Khi acid lactic hay ceto-acid được thêm vào, $H^+$ tiêu $HCO_3^-$ còn anion đi kèm (lactate, ceton) ở lại nhưng không được đo trong bộ xét nghiệm thường quy — nên khoảng trống tăng. Ngược lại, tiêu chảy làm mất $HCO_3^-$ và thận giữ $Cl^-$ bù lại, khoảng trống **không đổi**.

Hai nhóm nguyên nhân do đó tách bạch: khoảng trống tăng (nhiễm toan ceton, toan lactic, suy thận, ngộ độc methanol/ethylene glycol/salicylate) và khoảng trống bình thường (tiêu chảy, toan ống thận).

## Giới hạn của bù trừ

Bù trừ hô hấp nhanh (vài phút tới vài giờ) nhưng có giới hạn: $pCO_2$ hiếm khi xuống dưới 10-12 mmHg. Bù trừ thận chậm (2-5 ngày) nhưng mạnh hơn. Quan trọng nhất: bù trừ **không bao giờ điều chỉnh quá mức**. Nếu pH đã vượt sang phía đối diện, chắc chắn có hai rối loạn cùng tồn tại.

**Lỗi thường gặp:**
- Suy ra tổng lượng natri trong cơ thể từ nồng độ natri máu. Nồng độ là tỉ số natri trên nước; hạ natri máu thường gặp nhất ở bệnh nhân **thừa** natri toàn cơ thể như suy tim và xơ gan, vì họ thừa nước nhiều hơn.
- Coi $pCO_2$ giảm trong nhiễm toan chuyển hoá là một rối loạn hô hấp thứ hai. Đó là bù trừ sinh lí bình thường; chỉ khi giá trị đo nằm ngoài khoảng kì vọng theo công thức Winter mới kết luận có rối loạn hô hấp kèm theo.
- Bỏ qua khoảng trống anion khi đã xác định được nhiễm toan chuyển hoá. Khoảng trống chia nguyên nhân thành hai nhóm hoàn toàn khác nhau về xử trí, và delta gap còn phát hiện được rối loạn chuyển hoá thứ hai bị che khuất.
- Kì vọng bù trừ đưa pH về đúng 7,40. Bù trừ luôn không hoàn toàn và không bao giờ vượt qua mức bình thường; nếu pH đã sang phía đối diện thì chắc chắn có hai rối loạn nguyên phát cùng tồn tại.

<sub>`lesson.biology.sinh-li-hoc.can-bang-nuoc-dien-giai-va-acid-base`</sub>

---

### 11. Nội tiết học: trục điều hoà, phản hồi âm và cơ chế tác động hormone
*Endocrinology: regulatory axes, negative feedback and hormone action* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được cơ chế tác động của hormone tan trong nước và hormone tan trong lipid
- Phân tích được cấu trúc trục dưới đồi - tuyến yên - tuyến đích và ý nghĩa của phản hồi âm nhiều tầng
- Định khu được vị trí tổn thương nội tiết dựa trên tổ hợp nồng độ hormone đo được

## Hai cơ chế, hai thang thời gian

- **Tan trong nước** (peptide, catecholamine): không qua màng, gắn thụ thể bề mặt, dùng chất truyền tin thứ hai. Tác dụng trong giây tới phút, thường là biến đổi hoạt tính enzyme sẵn có.
- **Tan trong lipid** (steroid, hormone giáp): qua màng, gắn thụ thể nội bào, thay đổi phiên mã. Tác dụng sau hàng giờ tới ngày.

Hệ quả thực hành: insulin (peptide) phải tiêm vì bị tiêu hoá nếu uống; hormone giáp và steroid uống được. Và trong cấp cứu, corticoid tiêm tĩnh mạch **cũng không** có tác dụng tức thì — vì cơ chế của nó là qua phiên mã.

## Cấu trúc trục và cách định khu tổn thương

Vùng dưới đồi tiết hormone giải phóng → tuyến yên tiết hormone kích thích → tuyến đích tiết hormone cuối → hormone cuối ức chế ngược cả hai tầng trên.

Cấu trúc này cho một công cụ chẩn đoán mạnh: **đọc cặp hormone tầng trên và tầng dưới**.

- Hormone đích thấp + hormone kích thích **cao** → tổn thương tại tuyến đích (nguyên phát).
- Hormone đích thấp + hormone kích thích **thấp hoặc bình thường không phù hợp** → tổn thương tuyến yên hoặc dưới đồi (thứ phát).

Ví dụ: suy giáp nguyên phát có $T_4$ thấp, TSH rất cao; suy giáp do tuyến yên có $T_4$ thấp mà TSH lại thấp — TSH "bình thường" trong bối cảnh $T_4$ thấp đã là bất thường.

## Chỉ hormone tự do mới có tác dụng

Hơn 99% $T_4$ và cortisol tuần hoàn gắn protein. Thai kì và thuốc tránh thai làm tăng globulin gắn, nên hormone **toàn phần** tăng trong khi hormone tự do vẫn bình thường và bệnh nhân hoàn toàn không có triệu chứng. Đây là lí do xét nghiệm hiện đại đo $FT_4$ chứ không đo $T_4$ toàn phần.

## Khi phản hồi âm bị lợi dụng hoặc bị phá

Dùng corticoid ngoại sinh kéo dài ức chế trục, làm tuyến thượng thận teo. Ngừng thuốc đột ngột gây suy thượng thận cấp vì trục cần nhiều tuần tới nhiều tháng để hồi phục — do đó phải giảm liều từ từ.

Một số hệ dùng **phản hồi dương**: đỉnh LH trước rụng trứng, oxytocin trong chuyển dạ. Phản hồi dương luôn cần một sự kiện kết thúc để dừng vòng lặp — ở đây là rụng trứng và sổ thai.

**Lỗi thường gặp:**
- Đọc TSH đơn độc để kết luận chức năng tuyến giáp. TSH "bình thường" khi $FT_4$ thấp là bất thường, vì phản hồi âm lẽ ra phải đẩy TSH lên cao; luôn phải diễn giải cặp giá trị.
- Dùng nồng độ hormone toàn phần để đánh giá chức năng nội tiết. Chỉ phần tự do có hoạt tính; thai kì hay thuốc tránh thai làm tăng protein gắn nên hormone toàn phần tăng mà bệnh nhân bình giáp hoàn toàn.
- Kì vọng corticoid tiêm tĩnh mạch có tác dụng ngay lập tức. Steroid tác động qua thụ thể nội bào và thay đổi phiên mã, nên tác dụng chống viêm xuất hiện sau hàng giờ; trong sốc phản vệ thuốc cứu mạng là adrenaline chứ không phải corticoid.
- Ngừng đột ngột corticoid dùng kéo dài. Phản hồi âm đã ức chế trục và làm vỏ thượng thận teo; ngừng ngay gây suy thượng thận cấp, nên bắt buộc giảm liều dần trong nhiều tuần.

<sub>`lesson.biology.sinh-li-hoc.noi-tiet-va-dieu-hoa`</sub>

---

### 12. Tiêu hoá, chuyển hoá năng lượng toàn cơ thể và điều nhiệt
*Digestion, whole-body energetics and thermoregulation* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Tính được chuyển hoá cơ bản và tổng năng lượng tiêu hao từ số liệu nhân trắc
- Vận dụng được thương số hô hấp để suy ra loại cơ chất đang bị oxi hoá
- Phân tích được bốn con đường trao đổi nhiệt và cơ chế điều nhiệt của cơ thể

## Tiêu hoá là bài toán bề mặt và enzyme

Ruột non đạt diện tích hấp thu khoảng 200 m² nhờ ba tầng gấp nếp: nếp vòng, nhung mao, vi nhung mao. Enzyme tuỵ thuỷ phân cả ba nhóm chất; muối mật không phải enzyme mà là chất nhũ hoá — chúng làm tăng **diện tích bề mặt** của giọt mỡ để lipase làm việc, một cơ chế vật lí chứ không hoá học. Vì vậy tắc mật gây kém hấp thu mỡ dù lipase hoàn toàn bình thường.

## Ba thành phần của năng lượng tiêu hao

$$TDEE = BMR + TEF + \text{hoạt động thể lực}$$

BMR chiếm 60-75%, hiệu ứng nhiệt của thức ăn khoảng 10%, phần còn lại là hoạt động. BMR gần như tỉ lệ với **khối nạc**, không tỉ lệ với khối lượng toàn phần — đó là lí do hai người cùng cân nặng nhưng khác thành phần cơ thể có BMR chênh nhau đáng kể.

Ở mức liên loài, định luật Kleiber cho $BMR \propto M^{0{,}75}$: chuột tiêu năng lượng trên mỗi gam cao hơn voi hàng chục lần. Số mũ 3/4 chứ không phải 2/3 vẫn là chủ đề tranh luận, nhưng dữ liệu thực nghiệm qua nhiều bậc độ lớn ủng hộ nó.

## Thương số hô hấp cho biết đang đốt gì

Oxi hoá glucose: $C_6H_{12}O_6 + 6O_2 \to 6CO_2 + 6H_2O$, nên $RQ = 6/6 = 1{,}0$. Acid béo có tỉ lệ hydrogen trên oxygen cao hơn nên cần nhiều $O_2$ hơn cho mỗi $CO_2$, cho $RQ \approx 0{,}7$.

Ứng dụng trong hồi sức: bệnh nhân thở máy được nuôi quá nhiều carbohydrate sẽ có $RQ$ tiến tới và vượt 1,0, sinh nhiều $CO_2$ hơn, làm khó cai máy thở.

## Bốn con đường mất nhiệt

Bức xạ (khoảng 60% lúc nghỉ), dẫn truyền, đối lưu, bay hơi. Điểm then chốt: ba con đường đầu phụ thuộc **chênh lệch nhiệt độ** nên ngừng hoạt động khi môi trường nóng bằng hoặc hơn cơ thể. Khi đó bay hơi là con đường **duy nhất** — và bay hơi lại bị độ ẩm cao chặn. Đó là lí do nóng ẩm nguy hiểm hơn nóng khô rất nhiều, và là cơ sở của chỉ số nhiệt.

## Sốt khác tăng thân nhiệt

Sốt: cytokine gây viêm làm tăng $PGE_2$ ở vùng dưới đồi, **nâng điểm đặt**. Cơ thể thấy mình đang lạnh so với điểm đặt mới nên run cơ và co mạch — bệnh nhân sốt cảm thấy rét run dù thân nhiệt đang tăng. Thuốc hạ sốt hoạt động bằng cách ức chế tổng hợp prostaglandin, tức hạ điểm đặt trở lại.

Tăng thân nhiệt do say nắng thì hoàn toàn khác: điểm đặt bình thường nhưng cơ chế thải nhiệt bị quá tải. Vì vậy thuốc hạ sốt **vô tác dụng** với say nắng; phải làm mát vật lí.

**Lỗi thường gặp:**
- Coi chuyển hoá cơ bản tỉ lệ với khối lượng cơ thể. BMR gần như tỉ lệ với khối nạc; mô mỡ có hoạt động chuyển hoá thấp, nên hai người cùng cân nhưng khác tỉ lệ mỡ có BMR khác nhau rõ rệt.
- Dùng thuốc hạ sốt để xử trí say nắng. Trong say nắng điểm đặt vùng dưới đồi hoàn toàn bình thường và vấn đề là thải nhiệt quá tải; thuốc hạ sốt tác động lên điểm đặt nên vô tác dụng, xử trí đúng là làm mát vật lí.
- Nghĩ mật chứa enzyme tiêu hoá mỡ. Muối mật chỉ nhũ hoá, tức tăng diện tích bề mặt cho lipase tuỵ hoạt động; đây là tác dụng vật lí, và tắc mật gây kém hấp thu mỡ dù enzyme bình thường.
- Cho rằng ở môi trường nóng, quạt và tăng thông gió luôn giúp hạ nhiệt. Khi nhiệt độ môi trường vượt nhiệt độ da, đối lưu **đưa nhiệt vào** cơ thể; lúc đó chỉ còn bay hơi có tác dụng, và nếu độ ẩm cao thì cả đường này cũng bị chặn.

<sub>`lesson.biology.sinh-li-hoc.chuyen-hoa-nang-luong-va-dieu-nhiet`</sub>

---

### 13. Miễn dịch học: miễn dịch bẩm sinh, thích ứng và trí nhớ miễn dịch
*Immunology: innate and adaptive immunity and immunological memory* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- So sánh được miễn dịch bẩm sinh và thích ứng về tốc độ, tính đặc hiệu và trí nhớ
- Giải thích được nguồn gốc của tính đa dạng khổng lồ của thụ thể kháng nguyên
- Vận dụng được các chỉ số độ nhạy, độ đặc hiệu và giá trị tiên đoán cho xét nghiệm miễn dịch

## Hai hệ thống bổ sung nhau

**Bẩm sinh**: đáp ứng trong vài phút, nhận diện các mẫu phân tử chung của mầm bệnh (PAMP) qua thụ thể mã hoá sẵn trong hệ gen như TLR. Không có trí nhớ theo nghĩa cổ điển.

**Thích ứng**: mất 5-7 ngày lần đầu, nhận diện kháng nguyên rất đặc hiệu, có trí nhớ. Lần gặp lại chỉ mất 1-3 ngày với hiệu giá cao hơn và lớp kháng thể đã chuyển sang IgG.

Điểm liên kết quan trọng: hệ bẩm sinh **quyết định** hệ thích ứng đáp ứng ra sao. Tế bào tua nhận tín hiệu nguy hiểm rồi trình diện kháng nguyên kèm tín hiệu đồng kích thích; không có tín hiệu thứ hai này, tế bào T gặp kháng nguyên sẽ trở nên vô cảm thay vì hoạt hoá. Đây chính là lí do vaccine cần tá dược.

## Nghịch lí đa dạng và lời giải

Hệ gen người có khoảng 20000 gen, nhưng cơ thể tạo được hơn $10^{11}$ thụ thể kháng nguyên khác nhau. Lời giải là tổ hợp: chọn ngẫu nhiên một đoạn V, một D, một J từ các nhóm đoạn có sẵn; thêm hoặc bớt nucleotide ngẫu nhiên tại mối nối (đa dạng nối); rồi ghép ngẫu nhiên chuỗi nặng với chuỗi nhẹ.

Cái giá phải trả: nhiều thụ thể tạo ra sẽ nhận diện chính cơ thể. Vì thế phải có chọn lọc âm ở tuyến ức và tuỷ xương, cộng thêm dung nạp ngoại vi với tế bào T điều hoà. Bệnh tự miễn là hậu quả khi các tầng kiểm soát này rò rỉ — nói cách khác, tự miễn là **cái giá cấu trúc** của khả năng nhận diện mọi thứ.

## Vì sao MHC chia hai lớp

MHC lớp I có ở mọi tế bào có nhân và trình diện peptide **nội sinh** — cách duy nhất để tế bào T CD8 biết bên trong một tế bào có virus. MHC lớp II chỉ có ở tế bào trình diện chuyên nghiệp và trình diện peptide **ngoại sinh** cho tế bào T CD4. Hai lớp giải quyết hai bài toán khác nhau: phát hiện nhiễm nội bào và phối hợp đáp ứng với mầm bệnh ngoại bào.

## Trí nhớ và vaccine

Đáp ứng thứ phát nhanh và mạnh hơn nhờ ba yếu tố: số tế bào nhớ đặc hiệu nhiều hơn dòng ngây thơ hàng nghìn lần, kháng thể đã chuyển lớp, và ái lực đã chín muồi qua siêu đột biến soma.

Miễn dịch cộng đồng đạt được khi tỉ lệ tiêm chủng vượt ngưỡng $1 - 1/R_0$. Với sởi có $R_0 \approx 15$, ngưỡng lên tới 93% — con số cao này giải thích vì sao sởi luôn là bệnh bùng phát trở lại đầu tiên khi tỉ lệ tiêm chủng giảm.

**Lỗi thường gặp:**
- Cho rằng xét nghiệm có độ nhạy và độ đặc hiệu cao thì kết quả dương tính đáng tin trong mọi hoàn cảnh. Giá trị tiên đoán dương phụ thuộc mạnh vào tỉ lệ hiện mắc; khi bệnh hiếm, số dương tính giả có thể vượt xa số dương tính thật.
- Nghĩ tính đa dạng của kháng thể được mã hoá sẵn bằng hàng tỉ gen. Hệ gen chỉ chứa vài trăm đoạn gen; đa dạng sinh ra từ tái tổ hợp tổ hợp V(D)J, đa dạng tại mối nối và ghép ngẫu nhiên hai chuỗi.
- Coi bệnh tự miễn là lỗi hiếm gặp của hệ miễn dịch. Do thụ thể được tạo ngẫu nhiên, việc sinh ra thụ thể tự phản ứng là **tất yếu**; điều hệ miễn dịch làm là loại chúng bằng nhiều tầng dung nạp, và tự miễn là hậu quả khi các tầng đó rò rỉ.
- Cho rằng chỉ cần kháng nguyên là đủ để hoạt hoá tế bào T. Thiếu tín hiệu đồng kích thích từ tế bào trình diện đã được hoạt hoá bởi tín hiệu nguy hiểm, tế bào T sẽ trở nên vô cảm; đây chính là lí do vaccine bất hoạt cần tá dược.

<sub>`lesson.biology.sinh-li-hoc.mien-dich-hoc`</sub>

---

## Unit 7: Sinh thái và tiến hoá định lượng

### 1. Mô hình tăng trưởng quần thể: hàm mũ, logistic và các mô hình rời rạc
*Population growth models: exponential, logistic and discrete models* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được điều kiện áp dụng của mô hình tăng trưởng hàm mũ và logistic
- Tính được tốc độ tăng trưởng nội tại, thời gian nhân đôi và sản lượng bền vững tối đa
- Giải thích được vì sao mô hình rời rạc có thể cho dao động và hỗn loạn còn mô hình liên tục thì không

## Hai mô hình, hai giả thiết

$$\frac{dN}{dt} = rN \quad\Longrightarrow\quad N(t) = N_0 e^{rt}$$

$$\frac{dN}{dt} = rN\left(1-\frac{N}{K}\right) \quad\Longrightarrow\quad N(t)=\frac{K}{1+\left(\frac{K-N_0}{N_0}\right)e^{-rt}}$$

Mô hình hàm mũ giả định tài nguyên vô hạn; nó **không sai** mà chỉ có phạm vi hẹp — đúng cho quần thể mới xâm nhập, cho vi khuẩn pha log, cho giai đoạn đầu của dịch bệnh.

Mô hình logistic thêm số hạng $(1-N/K)$ biểu diễn phần tài nguyên còn lại. Điểm cần hiểu: số hạng này giả định phản hồi **tức thời** và **tuyến tính** — cả hai giả định đều thô so với thực tế.

## Đọc đường cong logistic

Điểm uốn nằm tại $N = K/2$, nơi $dN/dt$ đạt cực đại $rK/4$. Đây chính là cơ sở của MSY trong quản lí nghề cá: khai thác giữ quần thể quanh $K/2$ cho sản lượng lớn nhất.

Nhưng MSY là điểm quản lí **rủi ro cao**: nó nằm đúng trên đỉnh đường cong nên bất kì sai số ước lượng nào cũng đẩy quần thể xuống dốc bên kia, nơi khai thác vượt khả năng tái tạo và quần thể sụp đổ. Sự sụp đổ của nghề cá tuyết Bắc Đại Tây Dương là ví dụ lịch sử.

## Mô hình rời rạc và hỗn loạn

Với loài sinh sản theo mùa, thời gian là rời rạc. Mô hình Ricker $N_{t+1} = N_t e^{r(1-N_t/K)}$ và Beverton - Holt $N_{t+1} = \dfrac{R_0 N_t}{1+N_t/M}$ là hai dạng phổ biến.

Điểm khác biệt cốt lõi: mô hình rời rạc có **độ trễ nội tại một thế hệ**. Với $r$ nhỏ, quần thể tiến êm tới $K$; khi $r$ tăng, xuất hiện dao động hai chu kì, rồi bốn, rồi hỗn loạn tất định ở $r > 2{,}69$ với Ricker. Beverton - Holt thì luôn ổn định vì bù trừ của nó không quá mức.

Kết luận quan trọng: **dao động không đều của một quần thể không nhất thiết do môi trường biến động** — nó có thể sinh ra từ chính động học nội tại của một mô hình hoàn toàn tất định.

## Chọn mô hình nào

Sinh sản liên tục, thế hệ chồng lấn → mô hình vi phân. Sinh sản theo mùa, thế hệ tách biệt → mô hình rời rạc. Chọn sai loại mô hình sẽ bỏ sót toàn bộ khả năng dao động.

**Lỗi thường gặp:**
- Cho rằng khai thác ở mức thấp hơn MSY luôn an toàn. Nếu quần thể đang ở nhánh trái đường cong ($N < K/2$), tốc độ tái tạo thấp hơn MSY, và khai thác vượt tái tạo sẽ đẩy quần thể vào vòng suy giảm tự gia tốc.
- Nhầm tốc độ tăng trưởng riêng với tốc độ tăng trưởng tuyệt đối. Tốc độ riêng $(1/N)(dN/dt)$ giảm đơn điệu theo $N$ trong mô hình logistic, còn tốc độ tuyệt đối $dN/dt$ có cực đại tại $K/2$ — hai đại lượng có hình dạng hoàn toàn khác nhau.
- Giải thích mọi dao động số lượng quần thể bằng biến động môi trường. Mô hình rời rạc hoàn toàn tất định như Ricker đã sinh ra chu kì và hỗn loạn khi $r$ đủ lớn, chỉ nhờ độ trễ một thế hệ.
- Dùng mô hình logistic liên tục cho loài sinh sản theo mùa. Mô hình liên tục không có độ trễ nên luôn tiến êm tới $K$; nó sẽ bỏ sót hoàn toàn khả năng quần thể vọt lố và dao động, vốn là hành vi thực tế của nhiều loài côn trùng.

<sub>`lesson.biology.sinh-thai-dinh-luong.mo-hinh-tang-truong-quan-the`</sub>

---

### 2. Bảng sống, chiến lược sống và ma trận Leslie
*Life tables, life-history strategies and the Leslie matrix* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Lập và đọc được bảng sống với các cột $l_x$, $m_x$ và tính $R_0$, $T$, $r$
- Vận dụng được ma trận Leslie để dự báo cấu trúc tuổi và tốc độ tăng trưởng tiệm cận
- Ước lượng được kích thước quần thể bằng phương pháp bắt - đánh dấu - bắt lại

## Bảng sống là gì

Cột $l_x$ là xác suất sống tới tuổi $x$ tính từ lúc sinh; cột $m_x$ là số con cái trung bình sinh ra ở tuổi $x$. Từ hai cột này rút ra ba đại lượng:

$$R_0=\sum l_x m_x, \qquad T=\frac{\sum x\,l_x m_x}{R_0}, \qquad r\approx\frac{\ln R_0}{T}$$

Công thức $r \approx \ln R_0 / T$ là **gần đúng**; giá trị chính xác phải giải phương trình Euler - Lotka $\sum e^{-rx}l_x m_x = 1$. Sai lệch tăng khi $R_0$ khác xa 1.

## Ba kiểu đường cong sống sót

- **Kiểu I** (người, voi): tử vong dồn về cuối đời; ít con, chăm sóc nhiều.
- **Kiểu II** (nhiều loài chim, thuỷ tức): tỉ lệ tử vong không đổi theo tuổi, đường thẳng trên thang log.
- **Kiểu III** (cá, hàu, cây gỗ): tử vong khổng lồ ở giai đoạn non; rất nhiều con, không chăm sóc.

Đây không phải ba nhóm rời rạc mà là ba điểm trên một phổ liên tục của sự đánh đổi giữa số lượng và đầu tư cho mỗi cá thể con.

## Ma trận Leslie: từ mô tả sang dự báo

Bảng sống cho ảnh tĩnh; ma trận Leslie cho phép chiếu về tương lai:

$$\mathbf{n}(t+1) = \mathbf{L}\,\mathbf{n}(t)$$

Sau đủ nhiều bước, cấu trúc tuổi hội tụ về vectơ riêng ứng với trị riêng trội $\lambda$, và toàn quần thể tăng với hệ số $\lambda$ mỗi bước ($\lambda = e^{r}$).

Giá trị lớn nhất của phương pháp này nằm ở **phân tích độ nhạy**: đạo hàm của $\lambda$ theo từng phần tử ma trận cho biết can thiệp vào nhóm tuổi nào hiệu quả nhất. Với rùa biển, phân tích này đã chỉ ra rằng bảo vệ rùa non trên bãi đẻ kém hiệu quả hơn nhiều so với giảm tử vong của rùa trưởng thành trong lưới đánh cá — và kết luận đó đã làm thay đổi hoàn toàn chiến lược bảo tồn.

## Ước lượng kích thước quần thể

Phương pháp Lincoln - Petersen: $\hat N = \dfrac{n_1 n_2}{m_2}$. Bốn giả thiết bắt buộc: quần thể đóng, dấu không mất, đánh dấu không ảnh hưởng khả năng bị bắt lại, và mọi cá thể có xác suất bắt như nhau. Giả thiết cuối hay bị vi phạm nhất vì có hiện tượng "khôn bẫy" hoặc "nghiện bẫy". Với mẫu nhỏ, phải dùng hiệu chỉnh Chapman để tránh sai lệch hệ thống.

**Lỗi thường gặp:**
- Nhầm $l_x$ (xác suất sống tới tuổi $x$ tính từ lúc sinh) với $p_x$ (xác suất sống thêm một tuổi từ tuổi $x$). Hai đại lượng liên hệ qua $l_{x+1} = l_x p_x$; dùng nhầm làm $R_0$ sai lệch hàng lần.
- Coi $R_0 > 1$ là quần thể tăng nhanh. $R_0$ đo tăng trưởng trên mỗi **thế hệ**, còn tốc độ theo thời gian phụ thuộc cả thời gian thế hệ; hai loài cùng $R_0$ nhưng $T$ chênh 10 lần có $r$ chênh 10 lần.
- Dùng $r = \ln R_0 / T$ như công thức chính xác. Đó là xấp xỉ chỉ tốt khi $R_0$ gần 1; giá trị đúng là nghiệm của phương trình Euler - Lotka và phải giải bằng phương pháp số.
- Áp dụng Lincoln - Petersen mà không kiểm tra giả thiết quần thể đóng. Nếu có sinh, tử, di cư giữa hai lần bắt, ước lượng sẽ lệch; ngoài ra với số cá thể bắt lại nhỏ phải dùng hiệu chỉnh Chapman vì công thức gốc bị lệch lên trên.

<sub>`lesson.biology.sinh-thai-dinh-luong.bang-song-va-ma-tran-leslie`</sub>

---

### 3. Cạnh tranh và quan hệ vật ăn thịt - con mồi theo mô hình Lotka - Volterra
*Competition and predator-prey dynamics: the Lotka-Volterra models* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Dựng được đường đẳng không và xác định điều kiện cùng tồn tại trong mô hình cạnh tranh
- Giải thích được vì sao mô hình vật ăn thịt - con mồi cổ điển cho dao động lệch pha một phần tư chu kì
- Phân tích được ảnh hưởng của phản ứng chức năng Holling lên tính ổn định của hệ

## Cạnh tranh: điều kiện cùng tồn tại

$$\frac{dN_1}{dt}=r_1N_1\frac{K_1-N_1-\alpha_{12}N_2}{K_1}, \qquad \frac{dN_2}{dt}=r_2N_2\frac{K_2-N_2-\alpha_{21}N_1}{K_2}$$

Phân tích đồ thị cho bốn kết cục. Điều kiện cùng tồn tại ổn định:

$$\alpha_{12} < \frac{K_1}{K_2} \quad \text{và} \quad \alpha_{21} < \frac{K_2}{K_1}$$

Diễn đạt bằng lời: **mỗi loài phải tự kìm hãm mình mạnh hơn kìm hãm loài kia**. Đây là điều kiện chung của mọi lí thuyết cùng tồn tại hiện đại, và nó chỉ xảy ra khi hai loài dùng tài nguyên đủ khác nhau — tức là có phân hoá ổ sinh thái.

Nếu $\alpha_{12}$ và $\alpha_{21}$ đều lớn, kết cục phụ thuộc điều kiện ban đầu: loài nào đông trước sẽ thắng. Đây là cân bằng không ổn định, và giải thích hiện tượng ưu tiên thứ tự trong diễn thế.

## Vật ăn thịt - con mồi

$$\frac{dN}{dt}=rN-aNP, \qquad \frac{dP}{dt}=faNP-qP$$

Điểm cân bằng: $N^*=q/(fa)$ và $P^*=r/a$. Kết quả phản trực giác nhưng rất đáng nhớ: mật độ **con mồi** ở cân bằng chỉ phụ thuộc các tham số của **vật ăn thịt**, và ngược lại. Lí do: mỗi loài là yếu tố điều chỉnh loài kia.

Hệ cho dao động trung tính, trong đó vật ăn thịt trễ pha con mồi một phần tư chu kì. Trễ pha này là hệ quả tất yếu của cấu trúc: vật ăn thịt chỉ tăng **sau khi** con mồi đã nhiều, và đạt đỉnh khi con mồi đã bắt đầu giảm.

## Vì sao mô hình cổ điển không thực tế

Dao động trung tính nghĩa là biên độ hoàn toàn do điều kiện ban đầu quyết định và không có xu hướng trở lại — một nhiễu loạn nhỏ sẽ đổi biên độ vĩnh viễn. Hệ thực không hành xử như vậy. Ba bổ sung thường dùng:

1. Cho con mồi tăng trưởng logistic thay vì hàm mũ → cân bằng trở nên ổn định.
2. Dùng phản ứng chức năng kiểu II thay vì tuyến tính → **gây mất ổn định**, vì vật ăn thịt bão hoà nên không kìm được con mồi ở mật độ cao (nghịch lí làm giàu).
3. Dùng kiểu III → ổn định ở mật độ con mồi thấp, tạo nơi trú ẩn cho con mồi.

## Bài học phương pháp luận

Lotka - Volterra không dùng để dự báo số lượng. Giá trị của nó là chỉ ra **cơ chế nào sinh ra hành vi nào**: trễ pha từ đâu, cùng tồn tại cần điều kiện gì, và vì sao làm giàu môi trường lại có thể gây dao động dữ dội dẫn tới tuyệt chủng cục bộ.

**Lỗi thường gặp:**
- Cho rằng loài có sức chứa lớn hơn luôn thắng trong cạnh tranh. Kết cục do các hệ số $\alpha$ so với tỉ số sức chứa quyết định; ở ví dụ trên loài có $K = 800$ vẫn bị loại bởi loài có $K = 500$.
- Kì vọng dao động của mô hình vật ăn thịt - con mồi cổ điển có biên độ ổn định. Đó là dao động trung tính: biên độ hoàn toàn do điều kiện ban đầu quyết định và mọi nhiễu loạn đều làm đổi biên độ vĩnh viễn, nên mô hình gốc không mô tả được hệ thực.
- Nghĩ tăng tài nguyên cho con mồi luôn giúp hệ ổn định hơn. Với phản ứng chức năng kiểu II, làm giàu môi trường lại làm biên độ dao động tăng tới mức một trong hai loài tuyệt chủng cục bộ — đó là nghịch lí làm giàu.
- Diễn giải mật độ cân bằng của con mồi bằng các tham số của chính con mồi. Trong mô hình cổ điển, $N^* = q/(fa)$ chỉ chứa tham số của vật ăn thịt; tăng tốc độ sinh của con mồi làm tăng số **vật ăn thịt** chứ không tăng số con mồi ở cân bằng.

<sub>`lesson.biology.sinh-thai-dinh-luong.tuong-tac-lotka-volterra`</sub>

---

### 4. Cấu trúc quần xã và các chỉ số đa dạng sinh học
*Community structure and biodiversity indices* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được độ giàu loài, độ đồng đều và độ đa dạng
- Tính và so sánh được các chỉ số Shannon, Simpson và số loài hiệu dụng Hill
- Đánh giá được ảnh hưởng của công sức lấy mẫu lên ước lượng đa dạng

## Ba khái niệm không được lẫn

- **Độ giàu loài** $S$: chỉ đếm số loài.
- **Độ đồng đều**: các loài phân bố cá thể đều hay lệch.
- **Độ đa dạng**: kết hợp cả hai.

Hai quần xã cùng có 10 loài, một quần xã mỗi loài 100 cá thể, quần xã kia có một loài 991 cá thể và chín loài mỗi loài 1 cá thể — chúng khác nhau hoàn toàn về mặt sinh thái dù cùng $S$.

## Hai chỉ số phổ biến

$$H' = -\sum_{i} p_i \ln p_i, \qquad D = \sum_i p_i^{2}$$

Shannon xuất phát từ lí thuyết thông tin: nó đo độ bất định khi đoán loài của một cá thể bắt ngẫu nhiên. Simpson đo xác suất hai cá thể bắt ngẫu nhiên thuộc cùng một loài, nên **$D$ càng lớn thì đa dạng càng thấp** — vì vậy thường báo cáo $1-D$ hoặc $1/D$.

Điểm khác biệt cần nhớ: Shannon nhạy với các loài **hiếm**, Simpson nhạy với các loài **ưu thế**. Chọn chỉ số nào phụ thuộc câu hỏi sinh thái, và báo cáo cả hai thường tốt hơn báo cáo một.

## Vì sao nên dùng số Hill

Chỉ số Shannon 2,0 lớn hơn 1,0 bao nhiêu lần về mặt sinh học? Câu hỏi này không có câu trả lời tự nhiên vì $H'$ ở thang logarit. Số Hill giải quyết bằng cách quy về đơn vị "số loài tương đương":

$$^{0}D = S, \qquad ^{1}D = e^{H'}, \qquad ^{2}D = 1/\sum p_i^2$$

Bậc $q$ càng cao thì càng coi nhẹ loài hiếm. Với số Hill, câu "quần xã A đa dạng gấp đôi B" mới có nghĩa xác định.

## Vấn đề lấy mẫu

Độ giàu loài quan sát được luôn **thấp hơn** thực tế và tăng theo công sức lấy mẫu — đường cong tích luỹ loài hiếm khi bão hoà hoàn toàn. Vì vậy so sánh $S$ giữa hai địa điểm lấy mẫu khác công sức là vô nghĩa.

Hai cách xử lí: chuẩn hoá bằng đường cong pha loãng (rarefaction) về cùng cỡ mẫu, hoặc ước lượng độ giàu thực bằng Chao1 dựa trên số loài chỉ gặp một lần và hai lần. Trực giác của Chao1: nếu còn nhiều loài chỉ xuất hiện một lần thì chắc chắn còn nhiều loài chưa được gặp lần nào.

## Quan hệ loài - diện tích

$$S = cA^{z}$$

với $z$ thường 0,15-0,35. Hệ quả cho bảo tồn rất mạnh: giảm 90% diện tích môi trường sống ($A$ còn 0,1) làm mất khoảng $1 - 0{,}1^{0{,}25} \approx 44\%$ số loài. Đây là công cụ cơ bản để dự báo tuyệt chủng do mất môi trường sống.

**Lỗi thường gặp:**
- Đọc chỉ số Simpson $D$ như thước đo đa dạng theo chiều thuận. $D$ là xác suất hai cá thể cùng loài, nên $D$ lớn nghĩa là đa dạng **thấp**; phải báo cáo rõ đang dùng $D$, $1-D$ hay $1/D$, nếu không kết luận đảo ngược hoàn toàn.
- So sánh độ giàu loài giữa hai địa điểm có công sức lấy mẫu khác nhau. Số loài quan sát tăng đơn điệu theo cỡ mẫu; phải chuẩn hoá bằng rarefaction hoặc ước lượng độ giàu thực bằng Chao1 trước khi so sánh.
- Diễn giải chênh lệch chỉ số Shannon như chênh lệch bội số về đa dạng. $H'$ ở thang logarit nên hiệu của nó không có nghĩa nhân; muốn nói "gấp đôi" phải chuyển sang số Hill $e^{H'}$.
- Coi độ giàu loài cao là quần xã khoẻ mạnh. Một quần xã bị một loài xâm lấn chiếm ưu thế có thể giữ nguyên số loài trong khi độ đồng đều sụp đổ; chính độ đồng đều mới báo động sớm về suy thoái chức năng.

<sub>`lesson.biology.sinh-thai-dinh-luong.cau-truc-quan-xa-va-chi-so-da-dang`</sub>

---

### 5. Năng suất hệ sinh thái, dòng năng lượng và chu trình dinh dưỡng
*Ecosystem productivity, energy flow and nutrient cycling* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được năng suất sơ cấp thô và tinh, tính được hiệu suất sinh thái giữa các bậc
- Giải thích được vì sao chuỗi thức ăn hiếm khi vượt quá bốn hoặc năm bậc dinh dưỡng
- So sánh được đặc điểm của chu trình carbon, nitrogen và phosphorus

## Năng lượng đi một chiều, vật chất quay vòng

Đây là phát biểu nền tảng của sinh thái hệ sinh thái. Năng lượng vào dưới dạng ánh sáng, ra dưới dạng nhiệt, và **không tái sử dụng được** vì nhiệt độ thấp không sinh công. Vật chất thì quay vòng vì nguyên tử không bị tiêu hao.

## GPP, NPP và hiệu suất quang hợp

$$NPP = GPP - R_{\text{tự dưỡng}}$$

Thực vật hô hấp hết khoảng một nửa lượng carbon cố định được. Trên phạm vi toàn cầu, chỉ khoảng 1% năng lượng bức xạ tới bề mặt được chuyển thành NPP — con số thấp này do phần lớn bước sóng không dùng được cho quang hợp, do phản xạ, và do các giới hạn sinh hoá của Rubisco.

Yếu tố giới hạn khác nhau theo hệ: trên cạn là nước và nhiệt độ; ở đại dương là dinh dưỡng, đặc biệt nitrogen, và sắt ở các vùng "nhiều dinh dưỡng, ít diệp lục".

## Vì sao chuỗi thức ăn ngắn

Với hiệu suất 10% mỗi bậc, từ 10000 kJ ở sinh vật sản xuất chỉ còn 1 kJ ở bậc thứ năm. Năng lượng còn lại quá nhỏ để nuôi một quần thể có kích thước tối thiểu tồn tại được. Ba nguồn thất thoát: phần không được ăn, phần không tiêu hoá được, và hô hấp của chính bậc đó — hô hấp chiếm phần lớn nhất.

Hệ quả tính được: hệ sinh thái có NPP cao (rừng nhiệt đới, cửa sông) nuôi được chuỗi dài hơn hệ có NPP thấp (sa mạc, biển sâu).

Cùng lập luận này giải thích tháp sinh khối **ngược** ở đại dương: thực vật phù du có sinh khối nhỏ hơn động vật phù du ăn chúng, nhưng chúng thay thế lứa cực nhanh nên **năng suất** vẫn lớn hơn. Tháp năng lượng thì không bao giờ ngược được — đó là hệ quả trực tiếp của nguyên lí thứ hai nhiệt động lực học.

## Ba chu trình, ba đặc tính

- **Carbon**: bể khí quyển lớn, luân chuyển nhanh. Đốt nhiên liệu hoá thạch chuyển carbon từ bể địa chất (thời gian cư trú hàng triệu năm) vào bể khí quyển trong vài thế kỉ — mất cân bằng về **tốc độ**, không phải về tổng lượng.
- **Nitrogen**: khí quyển chứa 78% $N_2$ nhưng liên kết ba làm nó trơ; chỉ vi khuẩn cố định đạm và quá trình Haber - Bosch phá được. Con người hiện cố định nhiều nitrogen hơn toàn bộ các quá trình tự nhiên trên cạn cộng lại.
- **Phosphorus**: không có pha khí đáng kể, chỉ đi qua đá và trầm tích. Vì vậy nó thường là yếu tố giới hạn ở nước ngọt, và không thể được bổ sung nhanh từ khí quyển như nitrogen.

Đây là lí do phú dưỡng ở hồ thường được kiểm soát bằng cắt nguồn phosphorus, còn ở cửa sông ven biển lại phải cắt nitrogen.

**Lỗi thường gặp:**
- Dùng GPP làm cơ sở tính năng lượng chuyển lên bậc trên. Sinh vật sản xuất hô hấp mất khoảng một nửa lượng carbon cố định; chỉ NPP mới là phần khả dụng cho sinh vật tiêu thụ.
- Cho rằng tháp sinh khối luôn có đáy rộng. Ở đại dương, thực vật phù du có sinh khối tức thời nhỏ hơn động vật phù du vì chúng thay lứa trong vài ngày; tháp **năng lượng** thì không bao giờ ngược, do nguyên lí thứ hai nhiệt động lực học.
- Giải thích chuỗi thức ăn ngắn bằng việc thiếu loài thích hợp. Nguyên nhân là năng lượng: với hiệu suất khoảng 10% mỗi bậc, sau bốn bậc năng lượng còn lại không đủ nuôi một quần thể có kích thước tối thiểu tồn tại được.
- Coi vấn đề carbon là do tổng lượng carbon trên Trái Đất tăng. Tổng lượng không đổi; vấn đề là **tốc độ** chuyển carbon từ bể địa chất có thời gian cư trú hàng triệu năm sang bể khí quyển chỉ trong vài thế kỉ.

<sub>`lesson.biology.sinh-thai-dinh-luong.nang-suat-he-sinh-thai-va-chu-trinh-dinh-duong`</sub>

---

### 6. Sinh thái cảnh quan, siêu quần thể và sinh học bảo tồn
*Landscape ecology, metapopulations and conservation biology* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được mô hình siêu quần thể Levins để đánh giá ngưỡng tồn tại của loài trong cảnh quan phân mảnh
- Phân tích được ảnh hưởng của phân mảnh môi trường sống qua hiệu ứng biên và cách li
- Đánh giá được nguy cơ di truyền của quần thể nhỏ qua kích thước quần thể hiệu dụng

## Cảnh quan không đồng nhất

Sinh thái cảnh quan xét sự phân bố không gian của các mảnh và ảnh hưởng của nó tới quá trình sinh thái. Ba biến chính: diện tích mảnh, mức cách li, và chất lượng vùng đệm giữa các mảnh.

## Mô hình Levins

$$\frac{dp}{dt} = cp(1-p) - ep$$

trong đó $p$ là tỉ lệ mảnh đang có loài chiếm giữ. Điểm cân bằng:

$$\hat p = 1-\frac{e}{c}$$

Hai kết luận có giá trị thực hành cao:

1. Loài tồn tại được chỉ khi $c > e$. Đây là **ngưỡng**, không phải quan hệ tuyến tính.
2. Ngay ở cân bằng, luôn có một tỉ lệ mảnh **trống**. Vì vậy quan sát thấy mảnh môi trường sống tốt mà không có loài không có nghĩa mảnh đó không phù hợp.

Hệ quả cho bảo tồn: phá huỷ một phần mảnh làm giảm $c$ hiệu dụng; khi vượt ngưỡng, loài sụp đổ trên **toàn** cảnh quan chứ không chỉ mất ở phần bị phá. Đây là hiện tượng "nợ tuyệt chủng" — loài còn tồn tại một thời gian sau khi ngưỡng đã bị vượt qua, tạo cảm giác an toàn giả.

## Phân mảnh không chỉ là mất diện tích

Một mảnh rừng vuông 1 km² với vùng biên sâu 100 m chỉ còn lõi $0{,}8\times0{,}8 = 0{,}64$ km², tức mất 36% diện tích lõi. Chia cùng diện tích đó thành bốn mảnh 0,25 km² thì lõi mỗi mảnh chỉ còn $0{,}3\times0{,}3 = 0{,}09$ km², tổng 0,36 km² — mất 64%. **Cùng tổng diện tích, khác hoàn toàn về giá trị bảo tồn.**

Đây là nội dung định lượng đằng sau nguyên tắc thiết kế khu bảo tồn: ưu tiên mảnh lớn, tròn, có hành lang nối.

## Nguy cơ di truyền của quần thể nhỏ

Ba quá trình cộng dồn: mất biến dị do trôi dạt với tốc độ $1/(2N_e)$ mỗi thế hệ, tăng hệ số nội phối gây suy thoái cận huyết, và tích luỹ đột biến có hại nhẹ vốn lẽ ra bị chọn lọc loại bỏ ở quần thể lớn.

Quy tắc kinh nghiệm 50/500: cần $N_e \ge 50$ để tránh suy thoái cận huyết ngắn hạn, và $N_e \ge 500$ để duy trì tiềm năng thích nghi lâu dài. Cần nhớ $N_e$ thường chỉ bằng 10-30% số cá thể đếm được, nên ngưỡng 500 tương ứng vài nghìn cá thể thực.

## Giải cứu di truyền

Đưa một vài cá thể từ quần thể khác vào có thể phục hồi sức sống rất nhanh — trường hợp báo Florida được bổ sung tám con cái từ Texas năm 1995 là ví dụ được ghi nhận đầy đủ nhất. Rủi ro cần cân nhắc là suy thoái do lai xa nếu hai quần thể đã thích nghi khác biệt.

**Lỗi thường gặp:**
- Kết luận một mảnh môi trường sống không phù hợp vì không thấy loài ở đó. Trong siêu quần thể ở cân bằng luôn có một tỉ lệ mảnh trống do tuyệt chủng địa phương ngẫu nhiên; vắng mặt là trạng thái bình thường của hệ động.
- Đánh giá tác động của phá huỷ môi trường sống theo tỉ lệ tuyến tính với diện tích mất đi. Mô hình Levins và quan hệ loài - diện tích đều cho phản ứng phi tuyến có ngưỡng: mất 40% mảnh có thể xoá sổ loài trên toàn cảnh quan.
- Coi kích thước quần thể đếm được là kích thước quần thể hiệu dụng. $N_e$ thường chỉ bằng 10-30% số cá thể do tỉ lệ giới tính lệch, chênh lệch số con và biến động kích thước, nên ngưỡng 500 tương ứng vài nghìn cá thể thực.
- Cho rằng bảo tồn cùng một tổng diện tích thì chia nhỏ hay để nguyên đều như nhau. Hiệu ứng biên làm diện tích lõi giảm rất nhanh khi chia nhỏ; bốn mảnh 0,25 km² có tổng lõi chỉ bằng khoảng nửa lõi của một mảnh 1 km².

<sub>`lesson.biology.sinh-thai-dinh-luong.sinh-thai-canh-quan-va-bao-ton`</sub>

---

### 7. Mô hình dịch tễ SIR và số sinh sản cơ bản
*The SIR epidemic model and the basic reproduction number* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Xây dựng và diễn giải được hệ phương trình của mô hình SIR
- Tính được $R_0$, ngưỡng miễn dịch cộng đồng và quy mô cuối cùng của dịch
- Phân biệt được $R_0$ với số sinh sản hiệu dụng và giải thích ý nghĩa của điều kiện $R_t = 1$

## Ba khoang và ba giả thiết

$$\frac{dS}{dt}=-\beta SI, \qquad \frac{dI}{dt}=\beta SI-\gamma I, \qquad \frac{dR}{dt}=\gamma I$$

Số hạng $\beta SI$ giả định **trộn đều**: mọi cá thể có xác suất tiếp xúc như nhau. Đây là giả thiết mạnh nhất và cũng là giả thiết sai nhất trong thực tế, nhưng nó cho phép rút ra các kết luận định tính đúng.

$$R_0 = \frac{\beta}{\gamma}$$

Diễn giải: $\beta$ là tốc độ lây mỗi đơn vị thời gian, $1/\gamma$ là thời gian còn lây nhiễm. Tích của chúng là số người bị lây từ một ca.

## Điều kiện bùng phát là một bất đẳng thức

Từ $dI/dt = I(\beta S - \gamma)$, dịch chỉ tăng khi $\beta S > \gamma$, tức

$$R_t = R_0 s > 1$$

Hai hệ quả quan trọng:

1. Dịch **không cần** hết người cảm nhiễm mới dừng. Nó bắt đầu suy giảm ngay khi $s$ xuống dưới $1/R_0$. Đỉnh dịch xảy ra đúng tại thời điểm đó.
2. Ngưỡng miễn dịch cộng đồng là $1 - 1/R_0$. Với $R_0 = 15$ (sởi), cần 93%; với $R_0 = 2{,}5$, chỉ cần 60%.

## Vượt đích

Tại đỉnh dịch vẫn còn rất nhiều người đang nhiễm, và họ tiếp tục lây trong thời gian $1/\gamma$ nữa. Vì vậy **quy mô cuối cùng luôn vượt ngưỡng miễn dịch cộng đồng**. Với $R_0 = 2{,}5$: ngưỡng là 60% nhưng nếu để dịch chạy tự do thì tổng cộng khoảng 89% dân số sẽ nhiễm.

Đây là lập luận định lượng quan trọng nhất ủng hộ việc đạt miễn dịch bằng tiêm chủng thay vì bằng lây nhiễm tự nhiên: tiêm chủng dừng ở đúng ngưỡng, còn dịch tự nhiên luôn vượt xa.

## Làm phẳng đường cong

Giảm $\beta$ (giãn cách, khẩu trang) làm đỉnh thấp hơn và muộn hơn, đồng thời **giảm** cả quy mô cuối cùng vì hiện tượng vượt đích nhẹ đi. Đây là kết quả tính được từ mô hình, không phải khẩu hiệu.

## Giới hạn của mô hình

SIR bỏ qua tính không đồng nhất về tiếp xúc, cấu trúc tuổi, thời gian ủ bệnh (cần thêm khoang E), và khả năng miễn dịch suy giảm (cần mô hình SIRS). Tính không đồng nhất đặc biệt quan trọng: khi một số ít cá thể có tiếp xúc rất nhiều, dịch lan nhanh hơn ở giai đoạn đầu nhưng ngưỡng miễn dịch cộng đồng thực tế lại **thấp hơn** dự đoán của mô hình trộn đều, vì những người tiếp xúc nhiều bị nhiễm sớm và tự loại khỏi mạng lây.

**Lỗi thường gặp:**
- Coi $R_0$ là hằng số cố hữu của mầm bệnh. $R_0$ phụ thuộc cả mầm bệnh lẫn hành vi tiếp xúc và mật độ dân số của quần thể; cùng một virus có $R_0$ khác nhau ở thành thị và nông thôn.
- Cho rằng dịch chỉ dừng khi hết người cảm nhiễm. Số ca bắt đầu giảm ngay khi $s$ xuống dưới $1/R_0$; đỉnh dịch xảy ra đúng tại thời điểm đó chứ không phải khi mọi người đã nhiễm.
- Đồng nhất quy mô cuối cùng của dịch với ngưỡng miễn dịch cộng đồng. Do hiện tượng vượt đích, dịch tự nhiên luôn nhiễm nhiều hơn ngưỡng — với $R_0 = 2{,}5$ thì ngưỡng là 60% nhưng tổng nhiễm đạt khoảng 89%.
- Quên chia cho hiệu quả vaccine khi tính độ phủ tiêm chủng cần thiết. Nếu vaccine chỉ bảo vệ 80% số người tiêm, độ phủ phải là $p_c/0{,}8$; bỏ bước này khiến chương trình tiêm chủng không bao giờ đạt ngưỡng thật.

<sub>`lesson.biology.sinh-thai-dinh-luong.mo-hinh-dich-te-sir`</sub>

---

## Unit 8: Tin sinh học và thống kê sinh học

### 1. Căn chỉnh trình tự và các ma trận điểm thay thế
*Sequence alignment and substitution scoring matrices* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được căn chỉnh toàn cục và cục bộ về thuật toán và về tình huống sử dụng
- Giải thích được ý nghĩa log tỉ số khả dĩ của các ma trận PAM và BLOSUM
- Vận dụng được mô hình phạt khoảng trống affine và giải thích lí do sinh học của nó

## Hai bài toán, hai thuật toán

- **Needleman - Wunsch** (toàn cục): buộc căn chỉnh toàn bộ hai trình tự từ đầu tới cuối. Dùng khi hai trình tự cùng chiều dài và cùng nguồn gốc, ví dụ hai bản gen orthologue.
- **Smith - Waterman** (cục bộ): cho phép bắt đầu và kết thúc ở bất kì đâu, mọi ô âm được đặt về 0. Dùng khi tìm miền chung trong hai protein có kiến trúc khác nhau.

Cả hai đều là quy hoạch động và đều **bảo đảm** tìm được căn chỉnh tối ưu; giá phải trả là độ phức tạp $O(mn)$, quá chậm để quét cả cơ sở dữ liệu.

Chọn sai loại là lỗi hay gặp: dùng căn chỉnh toàn cục cho hai protein đa miền sẽ ép các miền không liên quan phải khớp nhau, làm che khuất miền thực sự tương đồng.

## Ma trận điểm mã hoá điều gì

Điểm của cặp $(a,b)$ là

$$s(a,b) = \frac{1}{\lambda}\ln\frac{q_{ab}}{p_a p_b}$$

trong đó $q_{ab}$ là tần suất cặp trong các căn chỉnh đã được xác thực, $p_a p_b$ là tần suất kì vọng nếu ghép ngẫu nhiên. Điểm dương nghĩa là cặp đó xuất hiện **nhiều hơn ngẫu nhiên** — tức được chọn lọc giữ lại.

Vì vậy thay thế Leu ↔ Ile được điểm dương (cùng kị nước, cùng kích thước) còn Leu ↔ Asp bị điểm âm mạnh. Ma trận không phải bảng "độ giống nhau hoá học" mà là **bảng thống kê tiến hoá**.

## PAM và BLOSUM khác nhau ở đâu

- **PAM$n$**: xây từ các trình tự rất giống nhau rồi ngoại suy bằng luỹ thừa ma trận. Số càng **lớn** thì khoảng cách tiến hoá càng xa.
- **BLOSUM$n$**: xây trực tiếp từ các khối căn chỉnh có độ đồng nhất tối đa $n\%$. Số càng **nhỏ** thì dùng cho trình tự càng xa nhau.

Hai thang **ngược chiều nhau** — đây là nguồn nhầm lẫn kinh điển. BLOSUM62 là mặc định của BLAST; về khoảng cách tiến hoá áp dụng, nó thường được quy đổi tương đương khoảng PAM160-250 tuỳ cách quy đổi, nên con số quy đổi chỉ nên coi là ước lượng thô.

## Vì sao phạt khoảng trống phải affine

Một sự kiện chèn hoặc mất thường xoá cả một đoạn. Nếu phạt tuyến tính, một khoảng trống 6 vị trí bị phạt bằng sáu khoảng trống 1 vị trí — trong khi về mặt tiến hoá, một sự kiện dài dễ xảy ra hơn nhiều so với sáu sự kiện độc lập. Phạt affine $W = g + e(L-1)$ với $g \gg e$ phản ánh đúng điều đó, và cho căn chỉnh sinh học hợp lí hơn hẳn.

## Đọc kết quả cho đúng

Với protein, đồng nhất trên 30% trên đoạn đủ dài gần như chắc chắn là đồng nguồn. Dưới 20% là "vùng chạng vạng", nơi các trình tự không liên quan cũng có thể đạt mức đó do ngẫu nhiên — khi đó phải dựa vào cấu trúc hoặc vào tìm kiếm theo hồ sơ chứ không dựa vào điểm căn chỉnh cặp đôi.

**Lỗi thường gặp:**
- Nhầm chiều của thang PAM và BLOSUM. PAM số lớn dùng cho trình tự xa nhau, còn BLOSUM số nhỏ mới dùng cho trình tự xa nhau; chọn nhầm làm bỏ sót các đồng nguồn xa hoặc tạo ra khớp giả.
- Dùng căn chỉnh toàn cục cho hai protein đa miền. Needleman - Wunsch buộc mọi phần phải khớp, nên nó sẽ trải đều khoảng trống và làm nhoè đi miền thực sự tương đồng; trường hợp này phải dùng Smith - Waterman.
- Coi ma trận điểm là bảng độ tương tự hoá học. Điểm là log tỉ số khả dĩ tính từ dữ liệu tiến hoá quan sát được; hai amino acid giống nhau về hoá học nhưng ít khi thay thế cho nhau trong thực tế vẫn nhận điểm thấp.
- Kết luận đồng nguồn từ mức đồng nhất 15-20%. Đây là vùng chạng vạng, nơi các trình tự ngẫu nhiên cũng đạt được mức đó; kết luận cần dựa vào giá trị E, vào tìm kiếm theo hồ sơ hoặc vào bằng chứng cấu trúc.

<sub>`lesson.biology.tin-sinh-hoc.can-chinh-trinh-tu-va-ma-tran-diem`</sub>

---

### 2. BLAST: thuật toán tìm kiếm và ý nghĩa thống kê của giá trị E
*BLAST: the search heuristic and the statistical meaning of the E-value* · Đại học · intl-undergrad · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao BLAST nhanh hơn Smith - Waterman và cái giá phải trả
- Diễn giải chính xác được giá trị E và phân biệt nó với xác suất và với phần trăm đồng nhất
- Chọn được chương trình BLAST và tham số phù hợp với từng loại câu hỏi sinh học

## Đánh đổi giữa tốc độ và bảo đảm

Smith - Waterman bảo đảm tối ưu nhưng có độ phức tạp $O(mn)$ — quét toàn bộ GenBank sẽ mất hàng ngày. BLAST đổi bảo đảm lấy tốc độ bằng chiến lược ba bước: tách truy vấn thành các từ ngắn, tìm nhanh các vị trí khớp từ trong cơ sở dữ liệu đã lập chỉ mục, rồi chỉ mở rộng căn chỉnh **quanh những vị trí đó**.

Cái giá: nếu hai trình tự đồng nguồn nhưng không chia sẻ một từ hạt giống nào đủ điểm, BLAST **bỏ sót hoàn toàn**. Đây là lí do các đồng nguồn rất xa cần PSI-BLAST hoặc HMM hồ sơ.

## Giá trị E nghĩa là gì

$$E = Kmn\,e^{-\lambda S}$$

Trong đó $m$ là chiều dài truy vấn, $n$ là tổng kích thước cơ sở dữ liệu. Ba điểm cần hiểu chính xác:

1. $E$ là **số lần kì vọng**, không phải xác suất. $E = 5$ nghĩa là kì vọng 5 kết quả ngẫu nhiên tốt bằng thế, hoàn toàn hợp lệ dù lớn hơn 1.
2. $E$ tỉ lệ thuận với kích thước cơ sở dữ liệu. Cùng một căn chỉnh cho $E$ lớn hơn khi tìm trong cơ sở dữ liệu lớn hơn — chính là hiệu chỉnh đa kiểm định, được xây sẵn vào công thức.
3. $E$ giảm theo **hàm mũ** của điểm. Chênh nhau vài bit làm $E$ đổi hàng bậc độ lớn.

Bit score thì ngược lại: không phụ thuộc kích thước cơ sở dữ liệu, nên nó mới là đại lượng so sánh được giữa các lần tìm kiếm ở thời điểm khác nhau.

## Chọn chương trình

- **blastn**: ADN với ADN. Kém nhạy với đồng nguồn xa vì mã di truyền thoái hoá làm nucleotide phân kì nhanh hơn amino acid nhiều.
- **blastp**: protein với protein.
- **blastx**: dịch truy vấn ADN theo sáu khung, so với protein. Dùng để chú giải trình tự mới.
- **tblastn**: protein truy vấn, so với cơ sở dữ liệu ADN đã dịch. Dùng để tìm gen chưa được chú giải.

Quy tắc thực hành: khi tìm đồng nguồn xa, **luôn** so ở mức protein nếu có thể.

## Bẫy thường gặp

Vùng có độ phức tạp thấp (giàu một loại gốc, ví dụ đoạn poly-Gln) cho điểm cao giả với vô số trình tự không liên quan. Bộ lọc mặc định che chúng đi; tắt lọc mà không hiểu sẽ tạo ra danh sách kết quả đầy nhiễu.

Cuối cùng: điểm cao chứng minh **tương đồng trình tự**, không chứng minh **cùng chức năng**. Nhiều enzyme cùng họ chỉ khác vài gốc ở tâm hoạt động lại xúc tác phản ứng khác hẳn.

**Lỗi thường gặp:**
- Diễn giải giá trị E như một xác suất. $E$ là **số lần kì vọng** nên có thể lớn hơn 1; chỉ khi $E$ rất nhỏ thì nó mới xấp xỉ xác suất gặp ít nhất một kết quả ngẫu nhiên tốt bằng thế.
- So sánh giá trị E của hai lần tìm kiếm ở hai thời điểm khác nhau. $E$ tỉ lệ với kích thước cơ sở dữ liệu, vốn tăng liên tục; muốn so sánh phải dùng bit score, vốn đã được chuẩn hoá.
- Dùng phần trăm đồng nhất làm tiêu chí chính. Đồng nhất 90% trên đoạn 15 gốc là chuyện ngẫu nhiên bình thường, trong khi đồng nhất 28% trên 400 gốc là bằng chứng đồng nguồn rất mạnh; giá trị E tích hợp cả độ dài lẫn mức khớp nên đáng tin hơn.
- Kết luận cùng chức năng từ điểm BLAST cao. Tương đồng trình tự chỉ gợi ý cùng nguồn gốc tiến hoá; các thành viên cùng họ enzyme có thể xúc tác phản ứng khác nhau do chỉ vài gốc ở tâm hoạt động khác biệt.

<sub>`lesson.biology.tin-sinh-hoc.blast-va-y-nghia-e-value`</sub>

---

### 3. Xây dựng cây phát sinh chủng loại và đồng hồ phân tử
*Phylogenetic tree construction and the molecular clock* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao phải hiệu chỉnh khoảng cách quan sát thành khoảng cách tiến hoá
- So sánh được UPGMA và Neighbor-Joining về giả thiết và về độ tin cậy
- Diễn giải được giá trị bootstrap và tỉ lệ dN/dS

## Vì sao khoảng cách quan sát không phải khoảng cách thật

Khoảng cách $p$ là tỉ lệ vị trí khác nhau. Vấn đề: khi hai trình tự đã phân kì lâu, một vị trí có thể đột biến A → G → A và trở về trạng thái ban đầu. Ta chỉ thấy "giống nhau" trong khi thực tế đã có hai thay thế.

Hệ quả: $p$ bão hoà ở khoảng 0,75 với ADN (vì bốn base đồng xác suất cho 3/4 vị trí khác nhau khi hoàn toàn ngẫu nhiên), dù thời gian phân kì vẫn tăng. Mô hình Jukes - Cantor hiệu chỉnh:

$$d = -\frac{3}{4}\ln\left(1-\frac{4}{3}p\right)$$

Kimura hai tham số tinh tế hơn vì phân biệt chuyển tiếp (A↔G, C↔T) với chuyển đảo — chuyển tiếp xảy ra thường xuyên hơn nhiều do hình học cặp base tương tự nhau.

## Hai phương pháp dựa trên khoảng cách

- **UPGMA**: gộp dần cặp gần nhất, cho cây **có gốc** và **siêu đo được** (mọi lá cách gốc bằng nhau). Điều này chỉ đúng nếu đồng hồ phân tử chạy đều ở mọi nhánh — một giả thiết rất mạnh và thường bị vi phạm.
- **Neighbor-Joining**: không giả định đồng hồ đều, cho cây **không gốc** với chiều dài nhánh khác nhau. Vì vậy NJ được ưa dùng hơn hẳn.

Muốn có gốc, phải dùng **nhóm ngoài** — một đơn vị phân loại chắc chắn tách ra trước tất cả các nhóm đang xét.

## Bootstrap đo cái gì

Lấy lại các cột của căn chỉnh có hoàn lại, dựng cây, lặp 1000 lần, rồi đếm tỉ lệ cây chứa mỗi nhánh. Giá trị trên 70% thường coi là ủng hộ tốt.

Điều bootstrap **không** cho biết: nhánh đó có đúng không. Nếu căn chỉnh sai hoặc mô hình tiến hoá chọn sai, mọi lần lấy mẫu lại đều mắc cùng lỗi và bootstrap có thể đạt 100% cho một nhánh sai. Bootstrap đo tính nhất quán, không đo tính đúng.

## Đồng hồ phân tử

Ý tưởng: nếu thay thế trung tính tích luỹ với tốc độ gần đều, số khác biệt tỉ lệ với thời gian phân kì. Cần hiệu chuẩn bằng hoá thạch hay sự kiện địa chất.

Giới hạn: tốc độ khác nhau giữa các dòng và giữa các gen, nên phương pháp hiện đại dùng đồng hồ thả lỏng cho phép tốc độ biến thiên theo nhánh.

## dN/dS phát hiện chọn lọc

Thay thế đồng nghĩa gần như trung tính nên phản ánh tốc độ đột biến nền. So sánh với thay thế làm đổi amino acid:

- $dN/dS < 1$: chọn lọc thanh lọc — phổ biến nhất, vì phần lớn thay đổi protein là có hại.
- $dN/dS \approx 1$: tiến hoá trung tính.
- $dN/dS > 1$: chọn lọc dương — hiếm, thấy ở gen miễn dịch, protein bề mặt virus và các gen liên quan đến cuộc chạy đua vũ trang tiến hoá.

Lưu ý: tính $dN/dS$ trên toàn gen thường che khuất tín hiệu, vì chọn lọc dương hay chỉ tác động lên vài codon; phải dùng phương pháp theo từng vị trí.

**Lỗi thường gặp:**
- Dùng khoảng cách $p$ trực tiếp cho các trình tự đã phân kì nhiều. Do thay thế nhiều lần tại cùng vị trí, $p$ bão hoà quanh 0,75 với ADN và đánh giá thấp khoảng cách thật; sai lệch tăng phi tuyến theo mức phân kì.
- Quên rằng cả hai dòng cùng tích luỹ thay thế kể từ tổ tiên chung. Thời gian phân kì phải chia cho **hai lần** tốc độ mỗi dòng; bỏ sót hệ số 2 làm kết quả sai đúng gấp đôi.
- Coi giá trị bootstrap cao là bằng chứng nhánh đó đúng. Bootstrap chỉ đo độ ổn định trước biến động lấy mẫu cột; nếu căn chỉnh sai hoặc mô hình tiến hoá không phù hợp thì mọi lần lấy mẫu đều lặp lại cùng sai lầm.
- Dùng UPGMA cho dữ liệu có tốc độ tiến hoá khác nhau giữa các nhánh. UPGMA áp đặt cây siêu đo được, tức giả định đồng hồ phân tử chạy đều tuyệt đối; khi giả thiết này sai, nó nhóm sai các dòng tiến hoá nhanh lại với nhau.

<sub>`lesson.biology.tin-sinh-hoc.cay-phat-sinh-chung-loai`</sub>

---

### 4. Phân tích biểu hiện gen RNA-seq và hiệu chỉnh đa kiểm định
*RNA-seq expression analysis and multiple testing correction* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao dữ liệu RNA-seq cần chuẩn hoá trước khi so sánh giữa mẫu
- Phân biệt được hiệu chỉnh Bonferroni và kiểm soát tỉ lệ phát hiện sai theo Benjamini - Hochberg
- Diễn giải đúng được giá trị $p$ hiệu chỉnh và phân biệt ý nghĩa thống kê với ý nghĩa sinh học

## Ba tầng chuẩn hoá

Số đọc thô của một gen phụ thuộc ba yếu tố ngoài mức biểu hiện: độ sâu giải trình tự của mẫu, chiều dài gen, và thành phần transcriptome.

- **Trong một mẫu**, so sánh giữa các gen cần chia cho chiều dài (TPM).
- **Giữa các mẫu**, so sánh cùng một gen chỉ cần chuẩn hoá độ sâu — và đây mới là mục tiêu của phân tích biểu hiện khác biệt.

Điểm tinh tế thứ ba: nếu một vài gen chiếm tỉ lệ đọc rất lớn ở một mẫu, chúng "nén" số đọc của mọi gen khác. Phương pháp trung vị tỉ số của DESeq2 và TMM của edgeR xử lí đúng vấn đề này, còn chia đơn thuần cho tổng số đọc thì không.

## Vì sao không dùng Poisson

Nếu chỉ có nhiễu lấy mẫu kĩ thuật, số đọc theo Poisson với phương sai bằng trung bình. Nhưng các mẫu lặp sinh học khác nhau thật sự, nên phương sai lớn hơn nhiều. Mô hình nhị thức âm thêm một tham số phân tán để bắt phần biến thiên đó.

Hệ quả thực tế: dùng Poisson sẽ cho hàng nghìn gen "có ý nghĩa" toàn dương tính giả. Và không có mô hình nào cứu được thí nghiệm **không có mẫu lặp sinh học** — mẫu lặp kĩ thuật không thay thế được, vì chúng không chứa thông tin về biến thiên giữa các cá thể.

## Bài toán đa kiểm định

Với 20000 gen và $\alpha = 0{,}05$, ta kì vọng 1000 gen dương tính giả ngay cả khi **không gen nào** thực sự khác biệt.

Hai chiến lược khác nhau về mục tiêu:

- **Bonferroni**: dùng ngưỡng $\alpha/m$, kiểm soát xác suất mắc **dù chỉ một** sai lầm. Rất nghiêm ngặt, phù hợp khi một kết quả sai gây hậu quả lớn (GWAS xác nhận, thử nghiệm lâm sàng).
- **Benjamini - Hochberg**: kiểm soát **tỉ lệ** sai trong số các phát hiện. Sắp các giá trị $p$ tăng dần, tìm chỉ số $k$ lớn nhất thoả $p_{(k)} \le \dfrac{k}{m}\alpha$, rồi tuyên bố $k$ gen đầu là có ý nghĩa.

Với nghiên cứu khám phá, chấp nhận 5% trong danh sách là sai để đổi lấy độ mạnh cao hơn nhiều là đánh đổi hợp lí — vì các gen tìm được sẽ còn được kiểm chứng riêng bằng qPCR hoặc western blot.

## Diễn giải cho đúng

"FDR = 0,05" nghĩa là kì vọng 5% **trong danh sách gen được chọn** là dương tính giả, không phải 5% xác suất cho từng gen.

Và quan trọng nhất: giá trị $p$ nhỏ không đồng nghĩa hiệu ứng lớn. Một gen biểu hiện cao có thể đạt $p$ rất nhỏ với thay đổi chỉ 1,05 lần. Vì vậy nên lọc đồng thời theo cả FDR và ngưỡng bội số thay đổi, và cách trình bày chuẩn là biểu đồ núi lửa với hai trục đó.

**Lỗi thường gặp:**
- Diễn giải FDR = 0,05 là mỗi gen trong danh sách có 5% khả năng sai. FDR là tỉ lệ kì vọng trên **toàn danh sách**; một gen ở đầu danh sách có xác suất sai thấp hơn nhiều so với gen ở cuối.
- Chạy RNA-seq không có mẫu lặp sinh học rồi hiệu chỉnh bằng mô hình thống kê. Không mô hình nào ước lượng được biến thiên sinh học nếu dữ liệu không chứa nó; mẫu lặp kĩ thuật chỉ đo nhiễu của máy giải trình tự.
- Áp dụng quy tắc Benjamini - Hochberg bằng cách dừng ở giá trị $p$ đầu tiên không thoả điều kiện. Quy tắc đúng là tìm chỉ số $k$ **lớn nhất** thoả mãn rồi lấy toàn bộ các hạng từ 1 tới $k$, kể cả những hạng ở giữa không thoả riêng lẻ.
- Xếp hạng gen quan trọng theo giá trị $p$. Gen biểu hiện rất cao đạt $p$ nhỏ với thay đổi không đáng kể về sinh học; phải lọc đồng thời theo cả FDR và bội số thay đổi, và trình bày bằng biểu đồ núi lửa.

<sub>`lesson.biology.tin-sinh-hoc.phan-tich-bieu-hien-gen-va-da-kiem-dinh`</sub>

---

### 5. Thống kê sinh học ứng dụng: thiết kế thí nghiệm và suy luận
*Applied biostatistics: experimental design and inference* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Chọn được kiểm định thống kê phù hợp với loại dữ liệu và thiết kế thí nghiệm
- Phân biệt được độ lệch chuẩn với sai số chuẩn và diễn giải đúng khoảng tin cậy
- Phân biệt được ý nghĩa thống kê với độ lớn hiệu ứng và giải thích vai trò của cỡ mẫu

## Chọn kiểm định theo ba câu hỏi

1. **Biến kết cục thuộc loại nào?** Liên tục → t-test, ANOVA, hồi quy. Đếm hoặc phân loại → chi bình phương, hồi quy logistic.
2. **Các nhóm độc lập hay ghép cặp?** Ghép cặp (đo trước - sau trên cùng cá thể) phải dùng t-test ghép cặp, vì nó loại được biến thiên giữa cá thể và do đó mạnh hơn hẳn.
3. **Bao nhiêu nhóm?** Nhiều hơn hai nhóm thì dùng ANOVA rồi mới so sánh hậu kiểm; so từng cặp bằng nhiều t-test làm tăng sai lầm loại I.

## SD và SEM không thay thế nhau

$$SEM = \frac{s}{\sqrt{n}}$$

SD mô tả **độ phân tán của quần thể** — dùng khi muốn nói các cá thể khác nhau bao nhiêu. SEM mô tả **độ chính xác của ước lượng trung bình** — dùng khi so sánh các nhóm.

SEM luôn nhỏ hơn SD và nhỏ đi khi tăng $n$, nên vẽ thanh sai số bằng SEM làm biểu đồ trông "đẹp" hơn. Đó chính là lí do nhiều bài báo lạm dụng SEM, và là lí do người đọc phải luôn kiểm tra chú thích hình xem đó là SD hay SEM.

## Khoảng tin cậy nói gì

$$CI_{95\%} = \bar x \pm t_{0{,}025,\,n-1}\frac{s}{\sqrt n}$$

Diễn giải đúng: nếu lặp lại thí nghiệm nhiều lần, 95% các khoảng dựng theo cách này sẽ chứa giá trị thật. **Không** phải "có 95% xác suất giá trị thật nằm trong khoảng này" — giá trị thật là hằng số, khoảng mới là biến ngẫu nhiên.

Khoảng tin cậy thông tin hơn giá trị $p$ vì nó cho biết cả hướng, độ lớn và độ chính xác cùng lúc.

## Ba sai lầm thiết kế phổ biến

- **Mẫu lặp giả**: đo 30 tế bào trong một đĩa và báo $n = 30$. Đơn vị thí nghiệm thật là đĩa, nên $n = 1$. Đây là lỗi phổ biến nhất trong sinh học tế bào.
- **Thiếu ngẫu nhiên hoá và làm mù**: nếu người đo biết mẫu thuộc nhóm nào, kết quả bị lệch một cách hệ thống, đặc biệt với các đo lường cần đánh giá chủ quan.
- **Kiểm định lặp cho tới khi có kết quả**: bổ sung mẫu rồi kiểm định lại nhiều lần làm sai lầm loại I tăng vọt so với mức danh nghĩa.

## Ý nghĩa thống kê không phải ý nghĩa sinh học

Với $n$ đủ lớn, mọi khác biệt dù nhỏ tới đâu đều đạt $p < 0{,}05$. Ngược lại, một hiệu ứng lớn có thể không đạt ý nghĩa nếu $n$ nhỏ — và khi đó kết luận đúng là "chưa đủ bằng chứng", **không phải** "không có khác biệt".

Vì vậy cách báo cáo chuẩn luôn gồm ba thành phần: độ lớn hiệu ứng, khoảng tin cậy của nó, và cỡ mẫu. Giá trị $p$ đứng một mình là báo cáo không đầy đủ.

**Lỗi thường gặp:**
- Kết luận "không có khác biệt" khi $p > 0{,}05$. Không bác bỏ giả thuyết không chỉ nghĩa là chưa đủ bằng chứng; khoảng tin cậy rộng cho thấy nhiều giá trị hiệu ứng lớn vẫn tương thích với dữ liệu.
- Dùng SEM thay cho SD khi muốn mô tả độ biến thiên của quần thể. SEM nhỏ đi khi tăng cỡ mẫu nên nó nói về độ chính xác của trung bình, không nói gì về mức khác biệt giữa các cá thể.
- Coi các phép đo trên cùng một đơn vị thí nghiệm là mẫu lặp độc lập. Đo 30 tế bào trong một đĩa cho $n = 1$ chứ không phải $n = 30$; mẫu lặp giả làm giá trị $p$ nhỏ giả tạo và là nguyên nhân lớn của khủng hoảng tái lập.
- So sánh nhiều nhóm bằng cách chạy t-test cho từng cặp. Với 4 nhóm có 6 cặp, xác suất mắc ít nhất một sai lầm loại I lên tới khoảng 26%; phải dùng ANOVA rồi hậu kiểm có hiệu chỉnh.
- Diễn giải khoảng tin cậy 95% là "xác suất 95% giá trị thật nằm trong khoảng". Giá trị thật là hằng số cố định; chính khoảng mới là biến ngẫu nhiên, và 95% là tỉ lệ các khoảng dựng theo cách này sẽ chứa giá trị thật khi lặp lại thí nghiệm.

<sub>`lesson.biology.tin-sinh-hoc.thong-ke-sinh-hoc-ung-dung`</sub>

---
