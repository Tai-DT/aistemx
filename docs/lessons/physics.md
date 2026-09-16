# Vật lí — Bài học AISTEM

Tổng số: **261** bài. Sinh tự động bằng `tools/build_content_index.py`.

## Chủ đề: Công và công suất, máy cơ đơn giản

### 1. Công cơ học
*Mechanical work* · THCS · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nêu được điều kiện để có công cơ học
- Vận dụng được công thức $A = F \cdot s$ để tính công
- Tính được công nâng một vật lên độ cao $h$

## Khi nào có 'công'?

Trong vật lí, **công cơ học** chỉ sinh ra khi có **lực** làm vật **dịch chuyển theo phương của lực**:

$$A = F \cdot s$$

với $F$ là lực (N), $s$ là quãng đường dịch chuyển theo phương của lực (m), $A$ là công (J).

## Hai điều kiện

Phải có **cả hai**: có lực và có dịch chuyển. Ví dụ:

- Đẩy tường mà tường không nhúc nhích: có lực nhưng $s = 0$ nên $A = 0$.
- Xách vali đi ngang: trọng lực hướng xuống, dịch chuyển nằm ngang, lực không cùng phương dịch chuyển nên trọng lực **không sinh công**.

## Công nâng vật lên cao

Để nâng vật khối lượng $m$ lên độ cao $h$ đều đặn, lực nâng bằng trọng lượng $P = 10m$, quãng đường là $h$:

$$A = P \cdot h = 10m \cdot h$$

Đây là công có ích thường gặp khi kéo vật lên, và bằng đúng thế năng mà vật nhận được.

## Đơn vị

$1$ J $= 1$ N$\cdot$m: công của lực 1 N làm vật dịch chuyển 1 m theo phương của lực.

**Lỗi thường gặp:**
- Cho rằng cứ có lực là có công. Nếu vật đứng yên ($s=0$) thì công bằng không.
- Tính công của trọng lực khi vật dịch chuyển ngang. Trọng lực vuông góc với dịch chuyển nên không sinh công.

<sub>`lesson.physics.thcs-vatli.cong-co-hoc`</sub>

---

### 2. Công suất
*Power* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được ý nghĩa của công suất là tốc độ sinh công
- Vận dụng được công thức $P = \dfrac{A}{t}$ để tính công suất
- So sánh được khả năng làm việc của các máy qua công suất

## Ai làm việc 'khỏe' hơn?

Hai máy cùng nâng một khối bê tông lên cao 10 m, một máy mất 20 giây, máy kia mất 5 giây. Cả hai sinh **cùng một công** nhưng máy nhanh hơn thì **mạnh** hơn. Đại lượng đo điều này là **công suất**:

$$P = \dfrac{A}{t}$$

tức là công sinh ra trong mỗi giây. Đơn vị là oát (W): $1$ W $= 1$ J/s.

## Công suất theo lực và vận tốc

Khi vật chuyển động đều với vận tốc $v$ nhờ lực $F$ thì trong thời gian $t$ vật đi được $s = v t$, công $A = F s = F v t$, nên:

$$P = \dfrac{A}{t} = F \cdot v$$

Công thức này tiện khi biết lực kéo và tốc độ của xe, băng chuyền, thang máy.

## Ý nghĩa các con số

Bóng đèn 60 W tiêu thụ 60 J mỗi giây. Động cơ 1000 W (1 kW) mạnh gấp nhiều lần. Người leo cầu thang nhanh có công suất tức thời vài trăm oát. So sánh công suất giúp chọn thiết bị phù hợp.

**Lỗi thường gặp:**
- Nhầm công suất với công. Công suất còn phụ thuộc thời gian: cùng công, mất ít thời gian hơn thì công suất lớn hơn.
- Quên đổi đơn vị thời gian ra giây khi tính công suất ra oát.

<sub>`lesson.physics.thcs-vatli.cong-suat`</sub>

---

### 3. Máy cơ đơn giản và định luật về công
*Simple machines and the law of work* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Kể được các máy cơ đơn giản: đòn bẩy, ròng rọc, mặt phẳng nghiêng
- Phát biểu và vận dụng được định luật về công
- Tính được hiệu suất của máy cơ đơn giản có ma sát

## Máy cơ đơn giản giúp gì?

Các **máy cơ đơn giản** - đòn bẩy, ròng rọc, mặt phẳng nghiêng - giúp ta **đổi hướng** hoặc **giảm lực** cần dùng. Ví dụ mặt phẳng nghiêng cho phép đẩy vật lên cao bằng lực nhỏ hơn trọng lượng.

## Định luật về công

Tuy vậy, **không máy nào cho lợi về công**:

> Được lợi bao nhiêu lần về lực thì thiệt bấy nhiêu lần về đường đi.

Dùng mặt phẳng nghiêng dài gấp đôi độ cao thì lực chỉ còn một nửa, nhưng phải kéo quãng đường gấp đôi. Công $A = F \cdot s$ không đổi.

## Hiệu suất

Thực tế luôn có ma sát nên phải tốn thêm công. **Công toàn phần** $A_{tp}$ ta bỏ ra lớn hơn **công có ích** $A_{ích}$ (công nâng vật). Ta đánh giá bằng **hiệu suất**:

$$H = \dfrac{A_{ích}}{A_{tp}} \cdot 100\%$$

Hiệu suất luôn nhỏ hơn 100%. Máy càng ít ma sát, hiệu suất càng cao. Với mặt phẳng nghiêng, $A_{ích} = P \cdot h$ và $A_{tp} = F \cdot l$ (lực kéo nhân chiều dài mặt phẳng).

**Lỗi thường gặp:**
- Nghĩ máy cơ đơn giản giúp lợi cả về công. Nó chỉ lợi về lực, thiệt về đường đi.
- Tính hiệu suất lớn hơn 100% do lẫn lộn công có ích với công toàn phần ở tử và mẫu.

<sub>`lesson.physics.thcs-vatli.may-co-don-gian-dinh-luat-ve-cong`</sub>

---

## Chủ đề: Cơ năng

### 1. Động năng và thế năng
*Kinetic and potential energy* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được vật có động năng khi chuyển động và thế năng khi ở độ cao
- Biết các yếu tố ảnh hưởng đến độ lớn động năng và thế năng
- Tính được thế năng trọng trường của vật

## Năng lượng của chuyển động và của độ cao

Một vật có thể mang **cơ năng** dưới hai dạng:

- **Động năng** $W_đ$: do vật đang **chuyển động**. Vật càng nặng, càng nhanh thì động năng càng lớn:

$$W_đ = \dfrac{1}{2}mv^2$$

Vì $v$ được bình phương nên khi vận tốc tăng gấp đôi, động năng tăng gấp bốn.

- **Thế năng trọng trường** $W_t$: do vật ở **trên cao** so với mốc chọn. Vật càng nặng, càng cao thì thế năng càng lớn:

$$W_t = P \cdot h = 10mh$$

## Vì sao phải chọn mốc?

Thế năng luôn tính so với một **mốc** (thường là mặt đất hoặc mặt bàn). Chọn mốc khác thì giá trị thế năng khác, nhưng độ chênh thế năng giữa hai vị trí thì không đổi.

## Ví dụ đời sống

Búa máy nâng cao có thế năng lớn; khi rơi, thế năng chuyển thành động năng đóng cọc. Nước trên đập cao mang thế năng, chảy xuống quay tua-bin thủy điện. Xe chạy nhanh có động năng lớn nên phanh gấp rất nguy hiểm.

**Lỗi thường gặp:**
- Quên rằng động năng phụ thuộc bình phương vận tốc; nghĩ vận tốc gấp đôi thì động năng gấp đôi (đúng ra gấp bốn).
- Tính thế năng mà không nói rõ mốc, hoặc lấy sai độ cao $h$ so với mốc đã chọn.

<sub>`lesson.physics.thcs-vatli.dong-nang-the-nang`</sub>

---

### 2. Định luật bảo toàn cơ năng
*Conservation of mechanical energy* · THCS · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Phát biểu được sự chuyển hóa giữa động năng và thế năng
- Vận dụng được định luật bảo toàn cơ năng cho vật rơi hoặc con lắc
- Tính được vận tốc của vật rơi từ độ cao $h$

## Động năng và thế năng đổi vai cho nhau

Thả một quả bóng từ trên cao: lúc đầu nó đứng yên nên chỉ có **thế năng**. Khi rơi, độ cao giảm (thế năng giảm) nhưng vận tốc tăng (động năng tăng). Nếu **bỏ qua ma sát**, tổng của chúng - **cơ năng** - luôn không đổi:

$$W = W_đ + W_t = \text{hằng số}$$

Đó là **định luật bảo toàn cơ năng**.

## Vận tốc vật rơi

Vật thả rơi từ độ cao $h$ (vận tốc đầu bằng 0): tại mặt đất, toàn bộ thế năng biến thành động năng:

$$10mh = \dfrac{1}{2}mv^2 \;\Rightarrow\; v = \sqrt{2gh}$$

Khối lượng bị triệt tiêu, nên mọi vật rơi từ cùng độ cao đều đạt cùng vận tốc (khi bỏ qua sức cản không khí).

## Con lắc và tàu lượn

Con lắc ở vị trí cao nhất có thế năng lớn nhất, động năng bằng 0; ở vị trí thấp nhất thì ngược lại. Tàu lượn siêu tốc lên đỉnh chậm (tích thế năng) rồi lao xuống rất nhanh (biến thành động năng). Có ma sát thì một phần cơ năng chuyển thành nhiệt, cơ năng giảm dần.

**Lỗi thường gặp:**
- Nghĩ vật nặng rơi nhanh hơn vật nhẹ. Khi bỏ qua sức cản, cùng độ cao thì cùng vận tốc.
- Áp dụng bảo toàn cơ năng khi có ma sát đáng kể. Lúc đó cơ năng giảm, không được coi là bảo toàn.

<sub>`lesson.physics.thcs-vatli.bao-toan-co-nang`</sub>

---

## Chủ đề: Lực

### 1. Lực đàn hồi của lò xo
*Elastic force of a spring* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được đặc điểm của lực đàn hồi xuất hiện khi lò xo bị biến dạng
- Vận dụng được hệ thức $F = k \cdot \Delta l$ (định luật Hooke) để tính lực hoặc độ cứng
- Tính được chiều dài lò xo khi treo vật

## Lò xo 'chống lại' khi bị kéo

Khi treo vật vào lò xo, lò xo dãn ra và xuất hiện **lực đàn hồi** kéo vật lại. Độ dãn càng lớn thì lực đàn hồi càng mạnh. Trong giới hạn đàn hồi, lực tỉ lệ thuận với độ biến dạng:

$$F = k \cdot \Delta l$$

Trong đó $\Delta l = l - l_0$ là **độ dãn** (chiều dài lúc sau trừ chiều dài tự nhiên), $k$ là **độ cứng** của lò xo.

## Khi vật treo đứng yên

Vật đứng yên nghĩa là lực đàn hồi cân bằng với trọng lượng:

$$F_{đh} = P = 10m$$

Từ đó tính được độ dãn $\Delta l = \dfrac{P}{k}$ và chiều dài lò xo $l = l_0 + \Delta l$.

## Ứng dụng: lực kế

Lực kế chính là một lò xo có gắn thang chia độ. Vì độ dãn tỉ lệ với lực nên ta đọc được lực trực tiếp. Càng kéo mạnh, kim chỉ càng lớn - đó là định luật Hooke đang làm việc.

**Lỗi thường gặp:**
- Dùng cả chiều dài $l$ thay vì độ dãn $\Delta l$ trong công thức $F = k\Delta l$.
- Quên đổi khối lượng gam ra kg khi tính $P = 10m$.

<sub>`lesson.physics.thcs-vatli.luc-dan-hoi-lo-xo`</sub>

---

### 2. Lực ma sát
*Friction force* · THCS · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nhận biết được ba loại lực ma sát: trượt, lăn, nghỉ
- Nêu được lực ma sát có thể có lợi hoặc có hại và cách làm tăng, giảm ma sát
- Tính được lực ma sát trượt trong trường hợp đơn giản

## Vì sao dừng đạp xe thì xe chậm lại?

Vì có **lực ma sát** cản trở chuyển động ở chỗ tiếp xúc. Có ba loại:

- **Ma sát trượt**: khi vật trượt trên mặt khác (kéo lê thùng hàng).
- **Ma sát lăn**: khi vật lăn (bánh xe lăn trên đường) - nhỏ hơn ma sát trượt nhiều.
- **Ma sát nghỉ**: giữ vật đứng yên dù bị đẩy (quyển sách trên bàn nghiêng chưa trượt).

## Lực ma sát trượt tính thế nào?

$$F_{ms} = \mu \cdot N$$

với $N$ là áp lực ép vuông góc lên mặt (thường bằng trọng lượng khi vật nằm ngang), $\mu$ là hệ số ma sát tùy mặt tiếp xúc.

## Có lợi hay có hại?

Ma sát **có lợi** khi giúp ta đi lại không trượt, phanh xe, cầm nắm đồ vật. Ma sát **có hại** khi làm mòn máy móc, tốn năng lượng. Muốn **giảm** ma sát ta bôi trơn, dùng ổ bi; muốn **tăng** ma sát ta làm nhám bề mặt (rãnh lốp xe, đế giày).

## Khi vật chuyển động đều

Nếu kéo vật trượt đều (tốc độ không đổi) thì lực kéo cân bằng với lực ma sát, nên $F_{kéo} = F_{ms}$. Đây là cách đo lực ma sát bằng lực kế.

**Lỗi thường gặp:**
- Cho rằng lực ma sát cùng chiều chuyển động. Thực ra nó luôn ngược chiều chuyển động (cản trở).
- Nghĩ ma sát luôn có hại. Nếu không có ma sát ta không đi, không cầm, không phanh được.

<sub>`lesson.physics.thcs-vatli.luc-ma-sat`</sub>

---

### 3. Hai lực cân bằng và quán tính
*Balanced forces and inertia* · THCS · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Nêu được đặc điểm của hai lực cân bằng và tác dụng của chúng lên vật
- Giải thích được quán tính là gì và cho ví dụ thực tế
- Vận dụng quán tính để giải thích các hiện tượng thường gặp

## Vì sao vật đứng yên vẫn 'chịu lực'?

Quyển sách nằm trên bàn chịu trọng lực kéo xuống và lực nâng của bàn đẩy lên. Hai lực này **cân bằng**: cùng phương thẳng đứng, ngược chiều, độ lớn bằng nhau. Vì thế sách đứng yên.

**Hai lực cân bằng không làm thay đổi vận tốc của vật.** Vật đang đứng yên thì tiếp tục đứng yên; vật đang chuyển động thẳng đều thì tiếp tục như thế.

## Quán tính

Mọi vật đều có xu hướng **giữ nguyên vận tốc** của mình - đó là **quán tính**. Vật nặng có quán tính lớn, khó thay đổi vận tốc hơn vật nhẹ.

## Giải thích bằng quán tính

- Xe phanh gấp, người **ngả về trước** vì thân trên còn muốn giữ vận tốc cũ.
- Đang chạy vấp phải đá, người **ngã chúi về trước** vì chân dừng nhưng thân trên còn tiến.
- Giũ mạnh chiếc khăn, bụi **rơi ra** vì khăn dừng đột ngột còn bụi vẫn muốn chuyển động.

## Vì sao thắt dây an toàn?

Khi ô tô va chạm dừng đột ngột, quán tính làm người lao về trước rất mạnh. Dây an toàn tạo lực giữ người lại, tránh chấn thương.

**Lỗi thường gặp:**
- Nghĩ 'không có lực thì vật đứng yên'. Vật có thể đang chuyển động thẳng đều mà hợp lực vẫn bằng không.
- Cho rằng hai lực cân bằng thì vật phải đứng yên. Thực ra vật vẫn có thể chuyển động thẳng đều.

<sub>`lesson.physics.thcs-vatli.hai-luc-can-bang-quan-tinh`</sub>

---

## Chủ đề: Lực đẩy Ác-si-mét và sự nổi

### 1. Lực đẩy Ác-si-mét
*Archimedes' buoyant force* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được đặc điểm và phương chiều của lực đẩy Ác-si-mét
- Vận dụng được công thức $F_A = d \cdot V$ để tính lực đẩy
- Xác định được số chỉ lực kế khi nhúng vật trong chất lỏng

## Vì sao dưới nước ta thấy nhẹ hơn?

Mọi vật nhúng trong chất lỏng đều bị chất lỏng **đẩy lên** một lực gọi là **lực đẩy Ác-si-mét**:

$$F_A = d \cdot V$$

trong đó $d$ là trọng lượng riêng của **chất lỏng**, $V$ là thể tích phần chất lỏng bị vật chiếm chỗ (phần chìm). Lực này hướng thẳng đứng **từ dưới lên**.

## Vì sao có lực đẩy?

Chất lỏng gây áp suất tăng theo độ sâu, nên mặt dưới của vật chịu áp suất lớn hơn mặt trên. Chênh lệch áp suất tạo ra lực đẩy tổng hợp hướng lên - chính là lực Ác-si-mét.

## Số chỉ lực kế

Treo vật vào lực kế trong không khí, kim chỉ trọng lượng $P$. Nhúng vật ngập trong nước, kim chỉ nhỏ hơn:

$$P' = P - F_A$$

Độ giảm số chỉ chính bằng lực đẩy Ác-si-mét. Đây là cách đo $F_A$ và cũng là cách xác định thể tích vật.

## Nhớ đúng $d$ và $V$

$d$ là của chất lỏng (nước, dầu...), **không phải** của vật. $V$ là thể tích **phần chìm**. Hai nhầm lẫn này khiến rất nhiều bài sai.

**Lỗi thường gặp:**
- Dùng trọng lượng riêng của vật thay cho của chất lỏng trong công thức $F_A = d\cdot V$.
- Quên đổi thể tích cm³ ra m³ (chia $10^6$), làm lực đẩy sai rất nhiều lần.

<sub>`lesson.physics.thcs-vatli.luc-day-ac-si-met`</sub>

---

### 2. Điều kiện vật nổi, chìm, lơ lửng
*Conditions for floating, sinking and neutral buoyancy* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- So sánh được lực đẩy Ác-si-mét với trọng lượng để dự đoán vật nổi, chìm hay lơ lửng
- Vận dụng được điều kiện nổi theo trọng lượng riêng $d_{vật}$ và $d_{lỏng}$
- Tính được tỉ lệ phần chìm của vật nổi

## Vì sao thép chìm mà tàu thép nổi?

Tất cả phụ thuộc cuộc 'đọ sức' giữa **trọng lượng** $P$ (kéo xuống) và **lực đẩy Ác-si-mét** $F_A$ (đẩy lên) khi vật **ngập hoàn toàn**:

- $P > F_A$: vật **chìm** xuống.
- $P < F_A$: vật **nổi** lên.
- $P = F_A$: vật **lơ lửng** (cân bằng ở mọi độ sâu).

## So sánh trọng lượng riêng

Với vật đặc, có thể so sánh nhanh trọng lượng riêng:

- $d_{vật} > d_{lỏng}$: chìm.
- $d_{vật} < d_{lỏng}$: nổi.
- $d_{vật} = d_{lỏng}$: lơ lửng.

Tàu thép nổi được vì phần rỗng chứa không khí làm **trọng lượng riêng trung bình** của cả con tàu nhỏ hơn của nước.

## Vật nổi chìm bao nhiêu?

Khi vật nổi cân bằng, phần chìm chiếm tỉ lệ:

$$\dfrac{V_{chìm}}{V} = \dfrac{d_{vật}}{d_{lỏng}}$$

Băng trôi có $D \approx 900$ kg/m³ nổi trên nước biển: chỉ khoảng 90% chìm, còn 10% nhô lên - phần 'nổi của tảng băng chìm'.

**Lỗi thường gặp:**
- So sánh nhầm chiều: nghĩ $d_{vật} > d_{lỏng}$ thì nổi. Ngược lại mới đúng - nặng riêng hơn thì chìm.
- Dùng toàn bộ thể tích vật cho $F_A$ khi vật đang nổi. Chỉ phần chìm mới chiếm chỗ chất lỏng.

<sub>`lesson.physics.thcs-vatli.dieu-kien-noi-chim-lo-lung`</sub>

---

## Chủ đề: Nhiệt học

### 1. Nhiệt lượng và nhiệt dung riêng
*Heat and specific heat capacity* · THCS · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nêu được nhiệt lượng là phần nhiệt năng vật thu vào hay tỏa ra khi đổi nhiệt độ
- Vận dụng được công thức $Q = mc\Delta t$
- Giải thích được ý nghĩa của nhiệt dung riêng

## Đun nước tốn nhiệt bao nhiêu?

Muốn làm một vật nóng lên, phải truyền cho nó **nhiệt lượng**:

$$Q = m \cdot c \cdot \Delta t$$

trong đó $m$ là khối lượng (kg), $\Delta t = t_2 - t_1$ là độ tăng nhiệt độ (°C), và $c$ là **nhiệt dung riêng** của chất.

## Nhiệt dung riêng nói lên điều gì?

$c$ là nhiệt lượng cần để **1 kg** chất tăng thêm **1°C**. Nước có $c = 4200$ J/(kg·K) - rất lớn, nên đun nước tốn nhiều nhiệt và nước nguội chậm. Nhờ vậy nước dùng làm chất tải nhiệt (nước làm mát động cơ) và biển điều hòa khí hậu.

Kim loại có $c$ nhỏ (đồng 380, nhôm 880) nên nóng lên và nguội đi rất nhanh.

## Thu vào hay tỏa ra?

Nếu nhiệt độ **tăng** ($\Delta t > 0$): vật **thu** nhiệt. Nếu nhiệt độ **giảm**: vật **tỏa** nhiệt, cùng công thức nhưng $\Delta t$ lấy trị tuyệt đối. Công thức này là nền tảng cho phương trình cân bằng nhiệt ở bài sau.

## Nhớ đơn vị

$m$ bằng kg, $\Delta t$ bằng °C (hay K, độ chênh bằng nhau), $c$ bằng J/(kg·K), thì $Q$ ra jun.

**Lỗi thường gặp:**
- Dùng nhiệt độ cuối $t_2$ thay cho độ tăng $\Delta t = t_2 - t_1$ trong công thức.
- Quên đổi khối lượng ra kg (để nguyên gam), làm nhiệt lượng sai 1000 lần.

<sub>`lesson.physics.thcs-vatli.nhiet-luong-nhiet-dung-rieng`</sub>

---

### 2. Phương trình cân bằng nhiệt
*Heat balance equation* · THCS · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Phát biểu được nguyên lí truyền nhiệt giữa các vật
- Vận dụng được phương trình cân bằng nhiệt $Q_{tỏa} = Q_{thu}$
- Tính được nhiệt độ khi trộn hai lượng nước

## Trộn nước nóng với nước lạnh

Khi cho hai vật có nhiệt độ khác nhau tiếp xúc, **nhiệt truyền từ vật nóng sang vật lạnh** cho đến khi cả hai cùng một nhiệt độ - gọi là **nhiệt độ cân bằng** $t$. Theo định luật bảo toàn năng lượng:

$$Q_{tỏa} = Q_{thu}$$

Vật nóng tỏa ra bao nhiêu nhiệt thì vật lạnh thu vào bấy nhiêu (nếu không mất nhiệt ra ngoài).

## Viết đầy đủ

Gọi vật nóng ($m_1, c_1, t_1$) và vật lạnh ($m_2, c_2, t_2$), nhiệt độ cân bằng $t$:

$$m_1 c_1 (t_1 - t) = m_2 c_2 (t - t_2)$$

Vế trái là nhiệt tỏa ra (nhiệt độ giảm từ $t_1$ về $t$), vế phải là nhiệt thu vào (tăng từ $t_2$ lên $t$).

## Mẹo tránh sai dấu

Luôn viết mỗi hiệu nhiệt độ sao cho **dương**: vật nóng lấy (nhiệt độ đầu − nhiệt độ cân bằng), vật lạnh lấy (nhiệt độ cân bằng − nhiệt độ đầu). Khi trộn cùng một chất (nước với nước), các $c$ triệt tiêu, giúp tính nhanh nhiệt độ cân bằng bằng trung bình có trọng số theo khối lượng.

**Lỗi thường gặp:**
- Viết hiệu nhiệt độ bị âm (ví dụ $t - t_1$ cho vật nóng), dẫn tới phương trình sai dấu.
- Cho rằng nhiệt độ cân bằng bằng trung bình cộng ngay cả khi khối lượng hai phần khác nhau.

<sub>`lesson.physics.thcs-vatli.phuong-trinh-can-bang-nhiet`</sub>

---

### 3. Nhiệt nóng chảy, hóa hơi và năng suất tỏa nhiệt của nhiên liệu
*Melting, vaporization heat and fuel heating value* · THCS · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Vận dụng được công thức nhiệt nóng chảy $Q = \lambda m$ và nhiệt hóa hơi $Q = Lm$
- Tính được nhiệt lượng tỏa ra khi đốt cháy nhiên liệu $Q = qm$
- Tính được hiệu suất của bếp đun

## Nóng chảy và hóa hơi 'ngốn' nhiệt mà không tăng nhiệt độ

Khi nước đá đang tan hay nước đang sôi, ta vẫn cấp nhiệt nhưng **nhiệt độ không đổi**. Nhiệt đó dùng để **phá vỡ liên kết**, đổi trạng thái:

- Nóng chảy (rắn → lỏng): $Q = \lambda m$, với $\lambda$ là nhiệt nóng chảy riêng.
- Hóa hơi (lỏng → hơi): $Q = L m$, với $L$ là nhiệt hóa hơi riêng.

Nước có $\lambda = 3{,}4\cdot10^5$ J/kg và $L = 2{,}3\cdot10^6$ J/kg - hóa hơi tốn nhiều nhiệt hơn nóng chảy rất nhiều.

## Đốt nhiên liệu tỏa nhiệt

Đốt cháy hoàn toàn nhiên liệu tỏa ra nhiệt lượng:

$$Q = q \cdot m$$

với $q$ là **năng suất tỏa nhiệt** (J/kg). Củi khô khoảng $10^7$, than đá $27\cdot10^6$, dầu hỏa $44\cdot10^6$ J/kg.

## Hiệu suất bếp đun

Không phải nhiệt nào đốt ra cũng dùng được: một phần thất thoát. Hiệu suất bếp:

$$H = \dfrac{Q_{ích}}{Q_{tỏa}} \cdot 100\%$$

trong đó $Q_{ích}$ là nhiệt làm nóng nước, $Q_{tỏa} = qm$ là nhiệt do nhiên liệu cháy sinh ra.

**Lỗi thường gặp:**
- Nghĩ trong lúc nóng chảy/sôi nhiệt độ vẫn tăng. Thực ra nhiệt độ không đổi cho tới khi đổi trạng thái xong.
- Nhầm nhiệt nóng chảy riêng $\lambda$ với nhiệt dung riêng $c$; hai đại lượng khác hẳn về ý nghĩa và đơn vị.

<sub>`lesson.physics.thcs-vatli.nhiet-nong-chay-hoa-hoi-nhien-lieu`</sub>

---

## Chủ đề: Quang học

### 1. Phản xạ và khúc xạ ánh sáng
*Reflection and refraction of light* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu và vận dụng được định luật phản xạ ánh sáng
- Nêu được hiện tượng khúc xạ khi ánh sáng truyền qua mặt phân cách hai môi trường
- So sánh được góc tới và góc khúc xạ khi ánh sáng đi vào môi trường chiết quang hơn

## Ánh sáng gặp gương thì dội lại

Khi chiếu tia sáng tới một gương phẳng, nó bị **phản xạ**. Định luật phản xạ:

- Tia phản xạ nằm trong mặt phẳng chứa tia tới và pháp tuyến.
- **Góc phản xạ bằng góc tới**: $i' = i$.

Các góc luôn đo từ **pháp tuyến** (đường vuông góc với gương), không đo từ mặt gương. Nếu tia tới hợp với gương 30° thì góc tới là $90° - 30° = 60°$.

## Ánh sáng gặp mặt nước thì gãy khúc

Khi truyền **xiên** từ môi trường này sang môi trường trong suốt khác (không khí sang nước, thủy tinh...), tia sáng bị đổi hướng - gọi là **khúc xạ**. Đó là lí do cái ống hút trong cốc nước trông như bị gãy, đáy hồ trông nông hơn thực tế.

## So sánh góc

- Đi từ không khí **vào** nước (môi trường chiết quang hơn): góc khúc xạ **nhỏ hơn** góc tới, tia sáng gãy lại gần pháp tuyến.
- Đi từ nước **ra** không khí: góc khúc xạ **lớn hơn** góc tới.

Khi tia tới vuông góc mặt phân cách (góc tới 0°) thì truyền thẳng, không đổi hướng.

**Lỗi thường gặp:**
- Đo góc tới từ mặt gương thay vì từ pháp tuyến, dẫn tới góc sai.
- Cho rằng góc khúc xạ luôn nhỏ hơn góc tới. Điều này chỉ đúng khi đi vào môi trường chiết quang hơn.

<sub>`lesson.physics.thcs-vatli.phan-xa-khuc-xa-anh-sang`</sub>

---

### 2. Thấu kính và ảnh qua thấu kính
*Lenses and image formation* · THCS · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được thấu kính hội tụ và thấu kính phân kì
- Vận dụng được công thức thấu kính và số phóng đại
- Tính được độ tụ của thấu kính và số bội giác của kính lúp

## Hai loại thấu kính

**Thấu kính hội tụ** (rìa mỏng, giữa dày) làm chùm tia song song hội tụ tại tiêu điểm - dùng làm kính lúp, vật kính máy ảnh. **Thấu kính phân kì** (rìa dày) làm chùm tia loe ra - dùng chữa cận thị.

## Công thức thấu kính

Liên hệ giữa tiêu cự $f$, khoảng cách từ vật $d$ và từ ảnh $d'$ đến thấu kính:

$$\dfrac{1}{f} = \dfrac{1}{d} + \dfrac{1}{d'}$$

**Số phóng đại** cho biết ảnh lớn hơn hay nhỏ hơn vật:

$$k = \dfrac{d'}{d} = \dfrac{h'}{h}$$

$k > 1$ là ảnh lớn hơn vật. Với thấu kính hội tụ, vật ngoài tiêu cự cho **ảnh thật, ngược chiều**; vật trong tiêu cự cho **ảnh ảo, cùng chiều, lớn hơn** (đó là cách kính lúp hoạt động).

## Độ tụ

Độ 'khỏe' của thấu kính đo bằng **độ tụ**:

$$D = \dfrac{1}{f} \quad (f \text{ tính bằng mét, } D \text{ tính bằng điốp})$$

Tiêu cự càng ngắn thì độ tụ càng lớn, khả năng hội tụ càng mạnh. Kính lúp có tiêu cự ngắn để phóng to vật nhỏ.

**Lỗi thường gặp:**
- Đổi đơn vị $f$ ra mét khi tính độ tụ mà lại quên, cho ra độ tụ sai 100 lần.
- Nhầm thấu kính hội tụ luôn cho ảnh nhỏ hơn. Vật trong tiêu cự cho ảnh ảo lớn hơn vật (kính lúp).

<sub>`lesson.physics.thcs-vatli.thau-kinh`</sub>

---

## Chủ đề: Truyền tải điện năng và máy biến áp

### 1. Truyền tải điện năng đi xa và máy biến áp
*Power transmission and transformers* · THCS · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao có hao phí điện năng khi truyền tải đi xa
- Nêu được cách giảm hao phí bằng cách tăng hiệu điện thế
- Vận dụng được công thức máy biến áp $\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$

## Vì sao tải điện lại hao phí?

Dây tải điện có điện trở $R$, nên khi có dòng điện chạy qua sẽ tỏa nhiệt theo Jun - Len-xơ. Phần điện năng biến thành nhiệt vô ích này gọi là **hao phí**. Với công suất truyền tải $P$ ở hiệu điện thế $U$:

$$P_{hp} = \dfrac{P^2 \cdot R}{U^2}$$

## Cách giảm hao phí

Nhìn công thức, có thể giảm hao phí bằng cách giảm $R$ (dùng dây to, tốn kém) hoặc **tăng hiệu điện thế** $U$. Vì $U$ nằm ở mẫu và được **bình phương**, chỉ cần tăng $U$ lên 10 lần thì hao phí giảm **100 lần**. Đây là cách hiệu quả nhất, nên đường dây cao thế truyền ở hàng trăm nghìn vôn.

## Máy biến áp

Để tăng rồi lại giảm hiệu điện thế, người ta dùng **máy biến áp**. Tỉ số hiệu điện thế bằng tỉ số số vòng dây hai cuộn:

$$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2}$$

Cuộn nhiều vòng hơn ứng với hiệu điện thế lớn hơn. Ở nhà máy dùng máy **tăng áp** trước khi truyền đi; đến khu dân cư dùng máy **hạ áp** đưa về 220 V an toàn để sử dụng.

**Lỗi thường gặp:**
- Nghĩ tăng hiệu điện thế lên 10 lần thì hao phí giảm 10 lần. Thực ra giảm 100 lần vì $U$ được bình phương.
- Lắp tỉ số vòng dây ngược, cho ra hiệu điện thế lớn hơn trong khi thực tế là máy hạ áp.

<sub>`lesson.physics.thcs-vatli.truyen-tai-dien-nang-may-bien-ap`</sub>

---

## Chủ đề: Tốc độ và chuyển động

### 1. Tốc độ, quãng đường và thời gian
*Speed, distance and time* · THCS · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nêu được ý nghĩa của tốc độ và viết được công thức $v = \dfrac{s}{t}$
- Tính được quãng đường hoặc thời gian khi biết tốc độ
- Đổi được đơn vị tốc độ giữa km/h và m/s

## Nhanh hay chậm đo bằng gì?

Để so sánh xe nào chạy nhanh hơn, ta dùng **tốc độ** - quãng đường đi được trong mỗi đơn vị thời gian:

$$v = \dfrac{s}{t}$$

Một xe đi 90 km trong 2 giờ có tốc độ $v = \dfrac{90}{2} = 45$ km/h, nghĩa là mỗi giờ đi được 45 km.

## Ba công thức 'anh em'

$$s = v \cdot t, \qquad t = \dfrac{s}{v}$$

Biết hai đại lượng là tìm được cái thứ ba, giống như bài khối lượng riêng.

## Đổi đơn vị tốc độ

Tốc độ hay dùng hai đơn vị: km/h (đi đường) và m/s (trong phòng thí nghiệm). Quy tắc:

$$1 \text{ m/s} = 3{,}6 \text{ km/h}$$

Ví dụ $36$ km/h $= \dfrac{36}{3{,}6} = 10$ m/s. Khi giải bài **phải đưa mọi đại lượng về cùng hệ đơn vị** trước khi thay số, nếu không kết quả sẽ sai.

## Mẹo nhớ

Nhân 3,6 khi đi từ m/s (số nhỏ, đơn vị 'nhỏ') lên km/h. Chia 3,6 khi đi ngược lại. Cứ nhớ 'số km/h luôn lớn hơn số m/s'.

**Lỗi thường gặp:**
- Quên đổi phút ra giờ (hoặc giây), ví dụ thay thẳng số 30 vào công thức.
- Đổi đơn vị nhầm chiều: lấy km/h nhân 3,6 để ra m/s. Đúng ra phải chia cho 3,6.

<sub>`lesson.physics.thcs-vatli.toc-do-quang-duong-thoi-gian`</sub>

---

### 2. Tốc độ trung bình của chuyển động không đều
*Average speed of non-uniform motion* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được chuyển động đều và chuyển động không đều
- Tính được tốc độ trung bình bằng tổng quãng đường chia tổng thời gian
- Giải thích được vì sao không lấy trung bình cộng các tốc độ

## Xe thật không chạy đều

Trên đường thật, xe lúc nhanh lúc chậm, dừng đèn đỏ rồi lại chạy - đó là **chuyển động không đều**. Để mô tả chung cả hành trình, ta dùng **tốc độ trung bình**:

$$v_{tb} = \dfrac{s}{t} = \dfrac{s_1 + s_2 + \dots}{t_1 + t_2 + \dots}$$

tức là **tổng quãng đường** chia cho **tổng thời gian**.

## Cạm bẫy hay gặp

Nhiều bạn lấy trung bình cộng hai tốc độ. Điều này chỉ đúng khi vật đi hai đoạn trong **thời gian bằng nhau**. Nếu hai đoạn có **quãng đường bằng nhau** thì phải tính riêng thời gian từng đoạn rồi cộng lại.

Ví dụ đi nửa đường đầu 40 km/h, nửa sau 60 km/h: đoạn chậm tốn nhiều thời gian hơn nên tốc độ trung bình 48 km/h, **nhỏ hơn** 50 km/h (trung bình cộng).

## Cách làm chắc chắn đúng

Luôn quay về định nghĩa: tính tổng quãng đường, tính tổng thời gian, rồi chia. Cách này không bao giờ sai, dù đề cho kiểu gì.

**Lỗi thường gặp:**
- Lấy trung bình cộng của các tốc độ. Chỉ đúng khi thời gian mỗi đoạn bằng nhau.
- Tính tốc độ trung bình riêng từng đoạn rồi cộng lại - hoàn toàn sai về ý nghĩa.

<sub>`lesson.physics.thcs-vatli.toc-do-trung-binh`</sub>

---

## Chủ đề: Áp suất

### 1. Áp suất của chất rắn
*Pressure of solids* · THCS · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nêu được áp suất là độ lớn của áp lực trên một đơn vị diện tích bị ép
- Vận dụng được công thức $p = \dfrac{F}{S}$ để tính áp suất, áp lực hoặc diện tích
- Giải thích được cách làm tăng, giảm áp suất trong thực tế

## Vì sao dao sắc thì cắt dễ?

Cùng một lực ấn, nhưng lưỡi dao mỏng có diện tích tiếp xúc rất nhỏ nên **áp suất** rất lớn, cắt vật dễ dàng. Áp suất đo độ 'tập trung' của lực trên diện tích:

$$p = \dfrac{F}{S}$$

với $F$ là **áp lực** (vuông góc với mặt), $S$ là **diện tích bị ép**. Đơn vị áp suất là paxcan: $1$ Pa $= 1$ N/m².

## Ba công thức 'anh em'

$$F = p \cdot S, \qquad S = \dfrac{F}{p}$$

## Tăng hay giảm áp suất

- **Tăng** áp suất: tăng áp lực hoặc giảm diện tích (mài dao mỏng, đóng đinh nhọn).
- **Giảm** áp suất: giảm áp lực hoặc tăng diện tích (xe tăng dùng bản xích rộng, móng nhà làm to để không lún).

## Chú ý đơn vị diện tích

Rất hay sai ở bước đổi diện tích: $1$ cm² $= 0{,}0001$ m² $= 10^{-4}$ m². Nếu để diện tích bằng cm² mà lực bằng N thì áp suất ra sai. Luôn đổi diện tích về m² để áp suất ra Pa.

**Lỗi thường gặp:**
- Không đổi diện tích ra m² (để nguyên cm²), làm áp suất sai hàng vạn lần.
- Nhầm áp lực với áp suất. Áp lực là lực (N), áp suất là lực trên diện tích (Pa).

<sub>`lesson.physics.thcs-vatli.ap-suat-chat-ran`</sub>

---

### 2. Áp suất chất lỏng và bình thông nhau
*Liquid pressure and communicating vessels* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được công thức $p = d \cdot h$ để tính áp suất trong lòng chất lỏng
- Giải thích được áp suất chất lỏng phụ thuộc độ sâu chứ không phụ thuộc hình dạng bình
- Nêu được đặc điểm mặt thoáng của chất lỏng trong bình thông nhau

## Càng lặn sâu càng tức ngực

Vì áp suất chất lỏng **tăng theo độ sâu**:

$$p = d \cdot h$$

với $d$ là trọng lượng riêng của chất lỏng, $h$ là độ sâu tính từ mặt thoáng đến điểm ta xét. Càng xuống sâu, cột chất lỏng phía trên càng nặng, áp suất càng lớn.

Điều bất ngờ: áp suất **không phụ thuộc hình dạng bình** hay lượng nước, chỉ phụ thuộc độ sâu và loại chất lỏng. Ở cùng độ sâu trong cùng một chất lỏng, áp suất bằng nhau theo mọi phương.

## Bình thông nhau

Trong bình thông nhau chứa **cùng một chất lỏng** đứng yên, mặt thoáng ở mọi nhánh luôn **ngang bằng** nhau, dù các nhánh to nhỏ khác nhau. Lí do: nếu lệch nhau thì áp suất ở đáy hai bên khác nhau, chất lỏng sẽ chảy cho đến khi cân bằng.

## Ứng dụng

Nguyên tắc bình thông nhau được dùng trong ấm nước (vòi và thân ngang mức), đài phun nước, và ống thủy đo mực nước trong bể kín. Máy nén thủy lực ở bài sau cũng dựa trên áp suất chất lỏng.

**Lỗi thường gặp:**
- Nghĩ bình to chứa nhiều nước thì áp suất đáy lớn hơn. Áp suất chỉ phụ thuộc độ sâu, không phụ thuộc lượng nước.
- Dùng khối lượng riêng $D$ thay cho trọng lượng riêng $d$ trong công thức $p = d\cdot h$.

<sub>`lesson.physics.thcs-vatli.ap-suat-chat-long-binh-thong-nhau`</sub>

---

### 3. Máy nén thủy lực và áp suất khí quyển
*Hydraulic press and atmospheric pressure* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu được nguyên lí truyền áp suất trong chất lỏng (định luật Pascal)
- Vận dụng được hệ thức $\dfrac{F_2}{F_1} = \dfrac{S_2}{S_1}$ cho máy nén thủy lực
- Nêu được sự tồn tại và độ lớn của áp suất khí quyển

## Vì sao kích thủy lực nâng được ô tô?

Áp suất tác dụng lên chất lỏng được truyền **nguyên vẹn** theo mọi phương (định luật Pascal). Trong máy nén thủy lực, hai pit-tông có diện tích $S_1$ nhỏ và $S_2$ lớn. Áp suất hai bên bằng nhau nên:

$$\dfrac{F_2}{F_1} = \dfrac{S_2}{S_1}$$

Pit-tông lớn gấp bao nhiêu lần thì lực nâng lớn gấp bấy nhiêu lần. Nhờ đó, một lực nhỏ ở pit-tông nhỏ tạo được lực rất lớn ở pit-tông lớn để nâng ô tô. Đổi lại, pit-tông nhỏ phải đi một đoạn dài hơn.

## Áp suất khí quyển

Không khí cũng có trọng lượng nên gây **áp suất khí quyển** lên mọi vật, khoảng $101300$ Pa ở gần mặt biển. Thí nghiệm Tô-ri-xe-li cho thấy nó nâng được cột thủy ngân cao khoảng 76 cm.

Áp suất khí quyển **giảm khi lên cao** vì cột không khí phía trên mỏng đi. Nó giải thích vì sao hút được nước bằng ống hút, giác mút bám tường, và tai ù khi máy bay lên cao.

**Lỗi thường gặp:**
- Lấy tỉ số diện tích ngược ($S_1/S_2$), làm lực nâng nhỏ đi thay vì lớn lên.
- Nghĩ máy thủy lực 'sinh' thêm năng lượng. Thực ra pit-tông nhỏ phải đi đoạn dài hơn, công không đổi.

<sub>`lesson.physics.thcs-vatli.may-nen-thuy-luc-ap-suat-khi-quyen`</sub>

---

## Chủ đề: Âm học

### 1. Âm học: tần số, chu kì và tiếng vang
*Acoustics: frequency, period and echo* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được mối liên hệ giữa tần số, chu kì và độ cao của âm
- Tính được tần số và chu kì dao động của nguồn âm
- Vận dụng được điều kiện nghe tiếng vang và cách đo khoảng cách bằng âm phản xạ

## Âm cao, âm thấp do đâu?

Nguồn âm phát ra âm nhờ **dao động**. Số dao động trong một giây gọi là **tần số** $f$, đơn vị héc (Hz):

$$f = \dfrac{n}{t}, \qquad T = \dfrac{1}{f}$$

với $n$ là số dao động trong thời gian $t$, còn $T$ là **chu kì** (thời gian một dao động). Tần số **càng lớn thì âm càng cao** (bổng); tần số nhỏ thì âm trầm. Tai người nghe được âm từ 20 Hz đến 20000 Hz.

## Âm phản xạ và tiếng vang

Âm gặp vật cản thì bị **phản xạ**. Nếu âm phản xạ đến tai chậm hơn âm trực tiếp ít nhất $\dfrac{1}{15}$ giây, ta nghe được **tiếng vang** tách biệt.

## Đo khoảng cách bằng âm

Âm đi từ nguồn đến vật cản rồi dội về, tổng quãng đường là $s = v \cdot t$. Vì âm đi **hai lượt** (đi và về), khoảng cách tới vật cản là:

$$d = \dfrac{v \cdot t}{2}$$

Nguyên lí này dùng trong **sonar** đo độ sâu đáy biển và siêu âm trong y học. Tốc độ âm trong không khí khoảng 340 m/s, trong nước khoảng 1500 m/s.

**Lỗi thường gặp:**
- Quên chia đôi khi tính khoảng cách bằng âm phản xạ (âm đi cả đi lẫn về).
- Nhầm tần số với chu kì. Tần số là số dao động mỗi giây (Hz), chu kì là thời gian một dao động (s), chúng nghịch đảo nhau.

<sub>`lesson.physics.thcs-vatli.am-hoc-tan-so-tieng-vang`</sub>

---

## Chủ đề: Điện học

### 1. Cường độ dòng điện và định luật Ôm
*Current and Ohm's law* · THCS · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nêu được cường độ dòng điện đặc trưng cho độ mạnh của dòng điện: $I = \dfrac{q}{t}$
- Phát biểu và vận dụng được định luật Ôm $I = \dfrac{U}{R}$
- Tính được một trong ba đại lượng $U$, $I$, $R$ khi biết hai đại lượng còn lại

## Dòng điện mạnh yếu đo bằng gì?

**Cường độ dòng điện** $I$ cho biết dòng điện mạnh hay yếu, bằng lượng điện tích chuyển qua tiết diện dây trong mỗi giây:

$$I = \dfrac{q}{t}$$

Đơn vị là ampe (A). Đo bằng ampe kế mắc **nối tiếp** vào mạch.

## Định luật Ôm

Hiệu điện thế $U$ (đo bằng vôn) là 'lực đẩy' tạo ra dòng điện, còn **điện trở** $R$ (đo bằng ôm) là sự cản trở. Định luật Ôm liên hệ ba đại lượng:

$$I = \dfrac{U}{R}$$

Dòng điện **tỉ lệ thuận** với hiệu điện thế và **tỉ lệ nghịch** với điện trở. Đặt cùng một hiệu điện thế, dây có điện trở lớn thì dòng nhỏ.

## Ba công thức 'anh em'

$$U = I \cdot R, \qquad R = \dfrac{U}{I}$$

Biết hai đại lượng là suy ra cái thứ ba. Chú ý $R = \dfrac{U}{I}$ chỉ để **tính** điện trở, chứ điện trở của một dây là không đổi, không phụ thuộc $U$ hay $I$.

**Lỗi thường gặp:**
- Nghĩ điện trở phụ thuộc vào $U$ và $I$ vì công thức $R = U/I$. Điện trở là tính chất của dây, không đổi.
- Nhầm chiều tỉ lệ: cho rằng điện trở lớn thì dòng điện lớn. Ngược lại, điện trở lớn thì dòng nhỏ.

<sub>`lesson.physics.thcs-vatli.cuong-do-dong-dien-dinh-luat-om`</sub>

---

### 2. Điện trở của dây dẫn
*Resistance of a conductor* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được điện trở của dây dẫn phụ thuộc chiều dài, tiết diện và vật liệu
- Vận dụng được công thức $R = \rho \dfrac{l}{S}$
- Giải thích được vai trò của biến trở

## Dây nào cản dòng nhiều hơn?

Điện trở của một dây dẫn phụ thuộc **ba yếu tố**: chiều dài, tiết diện (độ to nhỏ) và vật liệu:

$$R = \rho \dfrac{l}{S}$$

- **Dài hơn** ($l$ lớn) thì điện trở lớn hơn - electron phải đi xa hơn, va chạm nhiều hơn.
- **To hơn** ($S$ lớn) thì điện trở nhỏ hơn - lối đi rộng, dòng qua dễ.
- **Vật liệu**: đặc trưng bởi **điện trở suất** $\rho$. Đồng, nhôm có $\rho$ nhỏ nên dẫn điện tốt; nikelin, constantan có $\rho$ lớn dùng làm dây điện trở.

## Chú ý đơn vị tiết diện

$S$ phải đổi ra m². Nhớ $1$ mm² $= 10^{-6}$ m². Đây là chỗ hay sai nhất trong dạng bài này.

## Biến trở

**Biến trở** là điện trở thay đổi được, thường là cuộn dây có con chạy. Dịch con chạy làm thay đổi chiều dài dây tham gia mạch, từ đó thay đổi $R$ và điều chỉnh được cường độ dòng điện - ví dụ chỉnh độ sáng đèn, âm lượng.

**Lỗi thường gặp:**
- Không đổi tiết diện mm² ra m² (thiếu nhân $10^{-6}$), làm điện trở sai một triệu lần.
- Nghĩ dây to (tiết diện lớn) thì điện trở lớn. Ngược lại, tiết diện lớn thì điện trở nhỏ.

<sub>`lesson.physics.thcs-vatli.dien-tro-day-dan`</sub>

---

### 3. Đoạn mạch nối tiếp và song song
*Series and parallel circuits* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được các hệ thức của đoạn mạch nối tiếp
- Vận dụng được các hệ thức của đoạn mạch song song
- Tính được điện trở tương đương, cường độ dòng và hiệu điện thế của mạch

## Hai cách mắc điện trở

**Nối tiếp** (mắc liên tiếp thành một hàng): dòng điện chỉ có một đường đi nên **cường độ như nhau** ở mọi điểm; hiệu điện thế và điện trở cộng lại:

$$I = I_1 = I_2, \quad U = U_1 + U_2, \quad R_{tđ} = R_1 + R_2$$

**Song song** (mắc chung hai đầu): dòng điện rẽ nhánh, **hiệu điện thế như nhau** trên mỗi nhánh; cường độ cộng lại, còn nghịch đảo điện trở cộng lại:

$$U = U_1 = U_2, \quad I = I_1 + I_2, \quad \dfrac{1}{R_{tđ}} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$$

Với hai điện trở song song, có thể dùng công thức gọn: $R_{tđ} = \dfrac{R_1 R_2}{R_1 + R_2}$.

## Nhận biết nhanh

- Nối tiếp: điện trở tương đương **lớn hơn** mỗi điện trở thành phần.
- Song song: điện trở tương đương **nhỏ hơn** mỗi điện trở thành phần.

## Vì sao đèn nhà mắc song song?

Để mỗi đèn nhận đủ hiệu điện thế 220 V và bật tắt độc lập. Nếu mắc nối tiếp, một đèn hỏng là cả dãy tắt (như đèn nháy cây thông cũ).

**Lỗi thường gặp:**
- Cộng thẳng điện trở khi mắc song song. Song song phải cộng nghịch đảo, kết quả nhỏ hơn mỗi điện trở.
- Nhầm: nối tiếp thì hiệu điện thế như nhau, song song thì cường độ như nhau. Thực ra ngược lại.

<sub>`lesson.physics.thcs-vatli.doan-mach-noi-tiep-song-song`</sub>

---

### 4. Công, công suất điện và định luật Jun - Len-xơ
*Electrical work, power and Joule's law* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được công thức công suất điện $P = UI$ và điện năng $A = UIt$
- Tính được điện năng tiêu thụ (số đếm công tơ) và tiền điện
- Vận dụng được định luật Jun - Len-xơ $Q = I^2 R t$

## Đồ điện 'ăn' bao nhiêu điện?

**Công suất điện** cho biết mỗi giây thiết bị tiêu thụ bao nhiêu năng lượng:

$$P = U \cdot I$$

Còn có hai dạng khác nhờ định luật Ôm: $P = I^2 R = \dfrac{U^2}{R}$. Số ghi '220V - 100W' trên bóng đèn chính là hiệu điện thế và công suất định mức.

## Điện năng tiêu thụ và tiền điện

**Điện năng** (công của dòng điện) là công suất nhân thời gian:

$$A = P \cdot t = U I t$$

Công tơ điện đo điện năng theo đơn vị **kilôoát giờ** (kWh, còn gọi 'số điện'): $1$ kWh $= 1000$ W $\times 1$ h. Tiền điện = số kWh × giá mỗi kWh.

## Định luật Jun - Len-xơ

Khi dòng điện chạy qua vật dẫn có điện trở, một phần điện năng biến thành **nhiệt**:

$$Q = I^2 R t$$

Đây là nguyên lí của bếp điện, bàn là, ấm siêu tốc (biến điện thành nhiệt có ích) và cũng là lí do dây dẫn nóng lên, cầu chì đứt khi quá tải (bảo vệ mạch).

**Lỗi thường gặp:**
- Đổi kWh sai: quên $1$ kWh $= 1000$ Wh, hoặc để công suất bằng W mà thời gian bằng giây khi tính ra kWh.
- Nhầm công suất (W) với điện năng (kWh hay J). Điện năng còn nhân thêm thời gian.

<sub>`lesson.physics.thcs-vatli.cong-cong-suat-dien-jun-len-xo`</sub>

---

## Chủ đề: Điện từ

### 1. Quy tắc nắm tay phải và bàn tay trái
*Right-hand and left-hand rules* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được chiều đường sức từ của dòng điện bằng quy tắc nắm tay phải
- Xác định được chiều lực điện từ bằng quy tắc bàn tay trái
- Nêu được điều kiện xuất hiện dòng điện cảm ứng

## Dòng điện sinh ra từ trường

Xung quanh dây có dòng điện luôn có **từ trường**. Với ống dây (cuộn dây), dùng **quy tắc nắm tay phải** để tìm chiều đường sức từ:

> Nắm bàn tay phải, **bốn ngón** khum theo chiều **dòng điện** chạy trong các vòng dây, thì **ngón cái** choãi ra chỉ chiều **đường sức từ** trong lòng ống - đầu đó là cực Bắc.

Nhờ vậy ống dây có dòng điện trở thành **nam châm điện**.

## Từ trường tác dụng lực lên dòng điện

Khi đặt dây có dòng điện trong từ trường, dây chịu **lực điện từ**. Chiều lực xác định bằng **quy tắc bàn tay trái**:

> Đặt bàn tay trái sao cho các **đường sức từ** hướng vào lòng bàn tay, **bốn ngón** chỉ chiều **dòng điện**, thì **ngón cái** choãi 90° chỉ chiều **lực điện từ**.

Đây là nguyên lí hoạt động của **động cơ điện**: lực điện từ làm khung dây quay.

## Dòng điện cảm ứng

Ngược lại, khi **số đường sức từ** xuyên qua một cuộn dây kín **biến thiên** (nam châm lại gần hay ra xa), trong cuộn dây xuất hiện **dòng điện cảm ứng**. Đây là nguyên lí của máy phát điện và đàn ghi ta điện.

**Lỗi thường gặp:**
- Dùng nhầm tay: lấy tay trái cho ống dây hoặc tay phải cho lực điện từ. Nhớ: nắm tay PHẢI cho từ trường, bàn tay TRÁI cho lực.
- Nghĩ chỉ cần có từ trường và dòng điện là đủ sinh dòng cảm ứng. Phải có sự BIẾN THIÊN số đường sức từ mới có dòng cảm ứng.

<sub>`lesson.physics.thcs-vatli.quy-tac-nam-tay-phai-ban-tay-trai`</sub>

---

## Chủ đề: Đo lường và khối lượng riêng

### 1. Khối lượng riêng và cách xác định
*Density and how to determine it* · THCS · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Phát biểu được khối lượng riêng là khối lượng của một đơn vị thể tích của chất
- Tính được một trong ba đại lượng $D$, $m$, $V$ khi biết hai đại lượng còn lại
- Xác định được khối lượng riêng của vật rắn không thấm nước bằng cân và bình chia độ

## Vì sao 1 kg bông lại 'to' hơn 1 kg sắt?

Hai vật cùng khối lượng nhưng chiếm thể tích rất khác nhau vì chúng có **khối lượng riêng** khác nhau. Khối lượng riêng cho biết trong mỗi đơn vị thể tích (1 m³ hay 1 cm³) chứa bao nhiêu khối lượng chất:

$$D = \dfrac{m}{V}$$

Sắt có $D = 7800$ kg/m³, nghĩa là mỗi mét khối sắt nặng 7800 kg. Nước có $D = 1000$ kg/m³, còn bông chỉ vài chục kg/m³ nên cùng 1 kg thì bông phồng to hơn nhiều.

## Ba dạng của một công thức

Từ $D = \dfrac{m}{V}$ ta suy ra hai công thức 'anh em':

$$m = D \cdot V, \qquad V = \dfrac{m}{D}$$

Biết hai đại lượng bất kì là tìm được đại lượng thứ ba.

## Đo khối lượng riêng của một hòn đá

1. Dùng **cân** để đo khối lượng $m$ của hòn đá.
2. Đổ nước vào bình chia độ, đọc thể tích $V_1$. Thả hòn đá ngập nước, đọc thể tích $V_2$. Thể tích hòn đá là $V = V_2 - V_1$.
3. Tính $D = \dfrac{m}{V}$.

Chú ý luôn dùng **cùng một hệ đơn vị**: nếu $m$ tính bằng gam và $V$ bằng cm³ thì $D$ ra g/cm³.

**Lỗi thường gặp:**
- Nhầm 'khối lượng riêng' với 'khối lượng'. Khối lượng riêng gắn với một đơn vị thể tích, có đơn vị kg/m³, không phải kg.
- Quên đổi đơn vị cho đồng bộ: dùng $m$ bằng gam nhưng $V$ bằng m³, làm kết quả sai hàng nghìn lần.

<sub>`lesson.physics.thcs-vatli.khoi-luong-rieng`</sub>

---

### 2. Trọng lượng, trọng lượng riêng và liên hệ với khối lượng riêng
*Weight, specific weight and their link to density* · THCS · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Tính được trọng lượng của vật theo công thức $P = 10m$
- Phân biệt được khối lượng riêng $D$ và trọng lượng riêng $d$
- Vận dụng được hệ thức $d = 10D$ để chuyển đổi giữa hai đại lượng

## Khối lượng và trọng lượng khác nhau thế nào?

**Khối lượng** $m$ (đơn vị kg) đo lượng chất, không đổi dù ở đâu. **Trọng lượng** $P$ (đơn vị N) là lực hút của Trái Đất lên vật:

$$P = 10m$$

Một bạn nặng 40 kg thì trọng lượng là $P = 10 \cdot 40 = 400$ N. Lên Mặt Trăng khối lượng vẫn 40 kg nhưng trọng lượng nhỏ hơn vì lực hút yếu hơn.

## Trọng lượng riêng

Giống như khối lượng riêng, **trọng lượng riêng** cho biết mỗi mét khối chất nặng bao nhiêu niutơn:

$$d = \dfrac{P}{V}$$

Vì $P = 10m$ nên chia cả hai vế cho $V$ ta được mối liên hệ rất gọn:

$$d = 10D$$

Nước có $D = 1000$ kg/m³ nên $d = 10000$ N/m³. Nhớ hệ thức này giúp đổi qua lại nhanh mà không cần tính lại từ đầu.

## Dùng để làm gì?

Trọng lượng riêng $d$ rất tiện khi tính lực đẩy Ác-si-mét và áp suất chất lỏng ở các bài sau, vì các công thức đó dùng trực tiếp $d$ chứ không dùng $D$.

**Lỗi thường gặp:**
- Nhầm $P = 10m$ thành $m = 10P$. Trọng lượng luôn lớn gấp khoảng 10 lần số kg khối lượng.
- Lẫn lộn $D$ (kg/m³) với $d$ (N/m³). Chúng khác nhau đúng 10 lần và khác đơn vị.

<sub>`lesson.physics.thcs-vatli.trong-luong-trong-luong-rieng`</sub>

---

## Chương I: Điện tích - Điện trường

### 1. Điện tích và định luật Coulomb
*Electric charge and Coulomb's law* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Trình bày được ba cách làm nhiễm điện một vật và chỉ ra điện tích luôn bảo toàn trong mỗi cách
- Vận dụng được định luật Coulomb để tính lực tương tác giữa hai điện tích điểm trong chân không và trong điện môi
- Vận dụng được nguyên lí chồng chất để tìm hợp lực điện lên một điện tích trong hệ nhiều điện tích

## Vì sao cần hai loại điện tích

Cọ xát thanh thuỷ tinh vào lụa rồi đưa lại gần nhau, hai thanh đẩy nhau; nhưng thanh thuỷ tinh lại hút thanh nhựa đã cọ vào len. Không thể giải thích bằng một loại điện tích, nên ta quy ước có **hai loại**: dương và âm. Nhờ gán dấu đại số, việc cộng lực trở thành cộng vectơ có dấu.

Nhiễm điện xảy ra theo ba cách: cọ xát, tiếp xúc và hưởng ứng. Điểm mấu chốt: cọ xát **không sinh ra** điện tích, electron chỉ chuyển từ vật này sang vật kia. Vì thế tổng đại số điện tích của một hệ cô lập không đổi:

$$\sum q_i = \text{const}$$

## Định luật Coulomb

Bằng cân xoắn, Coulomb đo được lực giữa hai điện tích điểm đứng yên:

$$F = k\dfrac{|q_1 q_2|}{\varepsilon r^2}, \qquad k = 9\cdot10^{9}\ \text{N·m}^2/\text{C}^2$$

Lực hướng dọc đường nối hai điện tích: **đẩy** nhau nếu cùng dấu, **hút** nhau nếu trái dấu. Trong điện môi đồng chất, lực giảm $\varepsilon$ lần so với chân không ($\varepsilon \ge 1$).

## Khi có nhiều điện tích

Lực điện tuân theo **nguyên lí chồng chất**: hợp lực lên một điện tích bằng tổng vectơ các lực do từng điện tích còn lại gây ra, $\vec{F} = \sum \vec{F}_i$. Ta tính độ lớn từng lực rồi cộng vectơ (theo quy tắc hình bình hành hoặc chiếu lên trục).

**Lỗi thường gặp:**
- Quên bình phương khoảng cách hoặc quên đổi cm sang m, dẫn tới sai số 10^4 lần; công thức có r ở mẫu và được bình phương.
- Cộng thẳng độ lớn các lực khi có nhiều điện tích, quên rằng lực là đại lượng vectơ nên phải cộng theo phương chiều.
- Nhầm dấu điện tích với chiều lực: dấu chỉ cho biết hút hay đẩy, còn độ lớn luôn dùng trị tuyệt đối $|q_1 q_2|$.

<sub>`lesson.physics.vn-thpt-physics-diendtu.dien-tich-dinh-luat-coulomb`</sub>

---

### 2. Điện trường và cường độ điện trường
*Electric field and field strength* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Nêu được khái niệm điện trường là môi trường truyền tương tác điện
- Tính được cường độ điện trường do một điện tích điểm gây ra và vận dụng nguyên lí chồng chất điện trường
- Xác định được lực điện tác dụng lên một điện tích đặt trong điện trường đã biết

## Từ tác dụng xa đến điện trường

Định luật Coulomb mô tả lực giữa hai điện tích nhưng không nói tương tác truyền đi thế nào. Faraday đề xuất: mỗi điện tích tạo quanh nó một **điện trường**, và chính điện trường mới tác dụng lực lên điện tích khác. Điện trường tồn tại khách quan, kể cả khi chưa có điện tích thử.

## Cường độ điện trường

Đặt điện tích thử $q$ (đủ nhỏ) tại một điểm, nó chịu lực $\vec{F}$. Tỉ số

$$\vec{E} = \dfrac{\vec{F}}{q}$$

không phụ thuộc $q$ mà chỉ phụ thuộc điện trường tại điểm đó, nên đặc trưng cho điện trường. Từ đó, lực lên một điện tích bất kì là $\vec{F} = q\vec{E}$: nếu $q>0$ thì $\vec{F}$ cùng chiều $\vec{E}$, nếu $q<0$ thì ngược chiều.

Với một điện tích điểm $Q$ gây ra tại điểm cách nó $r$:

$$E = k\dfrac{|Q|}{\varepsilon r^2}$$

Vectơ $\vec{E}$ hướng ra xa nếu $Q>0$, hướng vào nếu $Q<0$.

## Chồng chất điện trường

Điện trường do nhiều điện tích bằng tổng vectơ các điện trường thành phần: $\vec{E} = \sum \vec{E}_i$. Đây là cơ sở để tính trường tại một điểm trong hệ nhiều điện tích, cũng bằng quy tắc hình bình hành như với lực.

**Lỗi thường gặp:**
- Lẫn lộn E và F: cường độ điện trường không phụ thuộc điện tích thử, còn lực thì tỉ lệ với điện tích đặt vào.
- Cộng độ lớn hai vectơ E cùng điểm mà quên chúng khác phương; phải cộng vectơ, nhất là khi các điện tích không thẳng hàng.
- Nhầm chiều E của điện tích âm: E luôn hướng về phía điện tích âm, ngược với trường của điện tích dương.

<sub>`lesson.physics.vn-thpt-physics-diendtu.dien-truong-cuong-do-dien-truong`</sub>

---

### 3. Điện thế, hiệu điện thế và công của lực điện
*Potential, voltage and work of electric force* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Tính được công của lực điện khi điện tích dịch chuyển trong điện trường đều
- Phân biệt và tính được điện thế, hiệu điện thế và liên hệ giữa chúng với thế năng
- Vận dụng được liên hệ $E = U/d$ trong điện trường đều

## Lực điện là lực thế

Trong điện trường đều, khi điện tích $q$ đi từ M đến N, công của lực điện chỉ phụ thuộc hình chiếu $d$ của độ dời theo phương đường sức:

$$A_{MN} = qEd$$

Công không phụ thuộc dạng đường đi, nên **lực điện là lực thế** và ta định nghĩa được thế năng điện $W = A_{M\infty}$ (công dịch tới vô cực).

## Điện thế và hiệu điện thế

Chia thế năng cho điện tích ta được đại lượng chỉ phụ thuộc điện trường: **điện thế** $V = W/q$. Hiệu hai điện thế cho **hiệu điện thế**:

$$U_{MN} = V_M - V_N = \dfrac{A_{MN}}{q}$$

Hiệu điện thế đo được trực tiếp bằng vôn kế và là đại lượng dùng trong mọi mạch điện. Đơn vị là vôn (V).

## Liên hệ E và U trong điện trường đều

Từ $A = qEd$ và $A = qU$ suy ra quan hệ rất hay dùng:

$$U = Ed \quad\Rightarrow\quad E = \dfrac{U}{d}$$

Nhờ hệ thức này, biết hiệu điện thế giữa hai bản tụ phẳng cách nhau $d$ ta tính ngay được cường độ trường đều giữa chúng. Đây cũng là lí do đơn vị của $E$ là V/m.

**Lỗi thường gặp:**
- Nhầm d là quãng đường thực đi thay vì hình chiếu theo phương đường sức; nếu điện tích đi vuông góc đường sức thì d = 0 và công bằng 0.
- Quên rằng công có dấu: điện tích dương đi theo chiều điện trường thì lực điện sinh công dương, ngược chiều thì công âm.
- Lẫn điện thế (một điểm) với hiệu điện thế (giữa hai điểm); vôn kế đo hiệu điện thế chứ không đo điện thế tuyệt đối.

<sub>`lesson.physics.vn-thpt-physics-diendtu.dien-the-hieu-dien-the-cong-luc-dien`</sub>

---

### 4. Tụ điện, ghép tụ và năng lượng điện trường
*Capacitors, combinations and field energy* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được cấu tạo, định nghĩa điện dung và ý nghĩa đơn vị fara của tụ điện
- Tính được điện dung tương đương của bộ tụ ghép nối tiếp và ghép song song
- Tính được năng lượng và điện tích tích trữ trong tụ điện

## Tụ điện dùng để làm gì

Tụ điện là hệ hai vật dẫn (hai bản) đặt gần nhau, ngăn bởi điện môi, dùng để **tích và phóng điện**. Khi nối vào nguồn, hai bản tích điện trái dấu bằng nhau về độ lớn. Khả năng tích điện được đo bằng **điện dung**:

$$C = \dfrac{Q}{U}$$

Với tụ phẳng, điện dung phụ thuộc kích thước và điện môi: $C = \dfrac{\varepsilon S}{4\pi k d}$. Nghĩa là bản càng rộng, khoảng cách càng nhỏ thì điện dung càng lớn.

## Ghép tụ

Khi ghép **nối tiếp**, điện tích trên mọi tụ bằng nhau còn hiệu điện thế cộng lại, dẫn tới nghịch đảo điện dung cộng: $\dfrac{1}{C_b} = \dfrac{1}{C_1}+\dfrac{1}{C_2}+\dots$ Khi ghép **song song**, hiệu điện thế chung nên điện dung cộng trực tiếp: $C_b = C_1 + C_2 + \dots$ Ghi nhớ đối lập này giúp không nhầm với ghép điện trở.

## Năng lượng tích trữ

Tụ đã tích điện dự trữ năng lượng dưới dạng năng lượng điện trường:

$$W = \dfrac{1}{2}CU^2 = \dfrac{Q^2}{2C} = \dfrac{1}{2}QU$$

Chọn dạng nào tuỳ vào đại lượng đề cho. Đây là cơ sở của đèn flash máy ảnh: tụ tích năng lượng chậm rồi phóng ra rất nhanh.

**Lỗi thường gặp:**
- Áp dụng nhầm công thức ghép: nối tiếp tụ giống song song điện trở (cộng nghịch đảo), rất dễ lẫn nếu học vẹt.
- Cho rằng ghép nối tiếp thì hiệu điện thế mỗi tụ bằng nhau; thực ra điện tích bằng nhau còn hiệu điện thế chia theo tỉ lệ nghịch điện dung.
- Dùng sai công thức năng lượng khi đề cho Q thay vì U; nên chọn dạng $W = Q^2/(2C)$ để khỏi phải tính U trung gian.

<sub>`lesson.physics.vn-thpt-physics-diendtu.tu-dien-ghep-tu-nang-luong`</sub>

---

## Chương I: Động học

### 1. Độ dịch chuyển, quãng đường, tốc độ và vận tốc
*Displacement, distance, speed and velocity* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được quãng đường (đại lượng vô hướng) với độ dịch chuyển (đại lượng vectơ)
- Tính được tốc độ trung bình và vận tốc trung bình của một chuyển động
- Viết được phương trình chuyển động thẳng đều và đọc được đồ thị độ dịch chuyển - thời gian

## Vì sao phải tách quãng đường khỏi độ dịch chuyển?

Một người đi 3 m sang phải rồi 3 m sang trái quay về chỗ cũ: **quãng đường** đi được là $s = 6$ m nhưng **độ dịch chuyển** bằng $0$ vì vị trí đầu trùng vị trí cuối. Quãng đường luôn dương và cộng dồn; độ dịch chuyển là vectơ, có thể âm, dương hay bằng không tùy chiều dương đã chọn.

## Tốc độ và vận tốc

Tốc độ trung bình đo *độ nhanh*: $v = \dfrac{s}{t}$, luôn dương. Vận tốc trung bình đo *độ nhanh kèm hướng dịch chuyển*: $v_{tb} = \dfrac{d}{t}$. Vì thế người chạy một vòng sân trở về đích có tốc độ trung bình khác không nhưng vận tốc trung bình bằng không.

## Chuyển động thẳng đều

Khi vận tốc không đổi, tọa độ biến thiên theo hàm bậc nhất của thời gian:

$$x = x_0 + v\,t$$

Đồ thị $x$-$t$ là một đường thẳng, **độ dốc của nó chính bằng vận tốc** $v$. Đồ thị càng dốc thì vật đi càng nhanh; độ dốc âm nghĩa là vật chuyển động theo chiều âm. Trên đồ thị $v$-$t$, đường nằm ngang và **diện tích hình chữ nhật dưới đường đó bằng độ dịch chuyển**.

## Khi nào dùng?

Dùng mô hình thẳng đều cho các đoạn đường mà tốc độ gần như không đổi (xe chạy ổn định trên cao tốc, băng chuyền). Khi cần cộng nhiều đoạn có tốc độ khác nhau, hãy tính tốc độ trung bình bằng *tổng quãng đường chia tổng thời gian*, tuyệt đối không lấy trung bình cộng các tốc độ.

**Lỗi thường gặp:**
- Lấy trung bình cộng hai tốc độ $(40+60)/2 = 50$ km/h. Sai vì trung bình phải lấy tổng quãng đường chia tổng thời gian; hai đoạn tốn thời gian khác nhau nên không thể lấy trung bình cộng đơn giản.
- Đồng nhất quãng đường với độ dịch chuyển. Với vật đổi chiều hoặc đi vòng, quãng đường luôn lớn hơn độ lớn độ dịch chuyển, nên tốc độ trung bình lớn hơn độ lớn vận tốc trung bình.

<sub>`lesson.physics.vn-thpt-physics-conhiet.do-dich-chuyen-van-toc-thang-deu`</sub>

---

### 2. Chuyển động thẳng biến đổi đều
*Uniformly accelerated straight-line motion* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Định nghĩa được gia tốc và nêu ý nghĩa dấu của gia tốc so với dấu vận tốc
- Vận dụng được bốn công thức của chuyển động thẳng biến đổi đều để giải bài toán
- Sử dụng được hệ thức độc lập thời gian khi bài toán không cho thời gian

## Từ vận tốc đổi đều đến gia tốc

Khi vận tốc thay đổi *đều đặn* theo thời gian, tỉ số $\dfrac{\Delta v}{\Delta t}$ là hằng số và được gọi là **gia tốc** $a$. Gia tốc dương hay âm không quyết định vật nhanh hay chậm dần; điều quyết định là **dấu của tích $a\cdot v$**: cùng dấu thì nhanh dần, trái dấu thì chậm dần.

## Bốn công thức lõi

Chọn mốc thời gian lúc $t=0$ với vận tốc đầu $v_0$:

$$v = v_0 + a t, \qquad d = v_0 t + \tfrac{1}{2} a t^2,$$
$$v^2 - v_0^2 = 2 a d, \qquad x = x_0 + v_0 t + \tfrac{1}{2} a t^2.$$

Hệ thức thứ ba đặc biệt hữu ích vì **không chứa thời gian**: khi đề cho vận tốc đầu, vận tốc cuối và quãng đường mà không cho $t$, đây là công thức cần chọn ngay.

## Đồ thị kể chuyện chuyển động

Trên đồ thị $v$-$t$, chuyển động biến đổi đều cho một đường thẳng xiên: **độ dốc bằng gia tốc**, còn **diện tích phần giới hạn giữa đồ thị và trục thời gian bằng độ dịch chuyển**. Phần diện tích nằm dưới trục hoành mang dấu âm — đó là lúc vật đi theo chiều âm.

## Mẹo chọn công thức

Liệt kê các đại lượng đã biết và đại lượng cần tìm, rồi chọn công thức chứa đúng bốn đại lượng đó. Quy tắc quãng đường trong giây thứ $n$ là $\Delta s_n = v_0 + a\left(n - \tfrac12\right)$ giúp giải nhanh nhiều câu trắc nghiệm.

**Lỗi thường gặp:**
- Cho rằng gia tốc âm luôn là chuyển động chậm dần. Sai; phải xét dấu tích $a\cdot v$: nếu vận tốc cũng âm thì vật vẫn nhanh dần.
- Quên đổi dấu gia tốc khi hãm phanh, dẫn tới nghiệm quãng đường âm hoặc vô lí. Phải gán $a$ ngược dấu $v_0$ khi vật chậm dần.

<sub>`lesson.physics.vn-thpt-physics-conhiet.chuyen-dong-thang-bien-doi-deu`</sub>

---

### 3. Sự rơi tự do
*Free fall* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nêu được đặc điểm của sự rơi tự do và điều kiện để một vật rơi tự do
- Vận dụng được các công thức rơi tự do để tính thời gian rơi, vận tốc và quãng đường
- Giải thích được vì sao trong chân không mọi vật rơi như nhau bất kể khối lượng

## Vì sao lông chim và viên bi rơi khác nhau?

Trong không khí, lông chim rơi chậm hơn viên bi vì lực cản. Nhưng trong ống đã hút chân không, cả hai **rơi như nhau** và chạm đáy cùng lúc. Điều đó cho thấy: khi chỉ còn trọng lực, mọi vật rơi với cùng một gia tốc $g$, độc lập với khối lượng. Đó là bản chất của rơi tự do.

## Các công thức

Rơi tự do là chuyển động nhanh dần đều với $v_0 = 0$, $a = g$, chiều dương hướng xuống:

$$v = g t, \qquad h = \tfrac{1}{2} g t^2, \qquad v^2 = 2 g h.$$

Từ $h = \tfrac12 g t^2$ suy ra thời gian rơi từ độ cao $h$: $t = \sqrt{\dfrac{2h}{g}}$. Vận tốc ngay trước khi chạm đất: $v = \sqrt{2gh}$.

## Một dấu hiệu nhận biết rơi tự do

Vì $h \propto t^2$, quãng đường rơi trong các giây liên tiếp tỉ lệ với dãy số lẻ $1 : 3 : 5 : 7\ldots$. Quãng đường rơi trong giây thứ $n$ là $\Delta h_n = g\left(n - \tfrac12\right)$. Đây là mẹo kiểm tra nhanh và cũng là cách nhận ra một chuyển động có phải nhanh dần đều hay không.

## Khi nào áp dụng được?

Mô hình rơi tự do chỉ đúng khi lực cản không khí không đáng kể — vật nặng, nhỏ, rơi từ độ cao vừa phải. Với vật nhẹ, xốp hoặc rơi rất lâu, phải kể đến lực cản và vật sẽ đạt tốc độ giới hạn.

**Lỗi thường gặp:**
- Cho rằng vật nặng rơi nhanh hơn vật nhẹ. Sai trong rơi tự do: khi bỏ qua lực cản, mọi vật có cùng gia tốc $g$ nên rơi như nhau.
- Tính quãng đường giây cuối bằng $\tfrac12 g \cdot 1^2 = 5$ m. Sai vì đó là quãng đường của giây ĐẦU; giây cuối phải lấy hiệu quãng đường giữa hai mốc thời gian liên tiếp.

<sub>`lesson.physics.vn-thpt-physics-conhiet.su-roi-tu-do`</sub>

---

### 4. Chuyển động ném ngang và ném xiên
*Projectile motion: horizontal and oblique launch* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Phân tích được chuyển động ném thành hai thành phần độc lập theo phương ngang và phương thẳng đứng
- Tính được thời gian bay, tầm xa, tầm cao của vật ném ngang và ném xiên
- Chứng minh được góc ném 45 độ cho tầm xa lớn nhất khi hai điểm ném và rơi cùng độ cao

## Bí quyết: tách một bài khó thành hai bài dễ

Một vật ném đi trong trọng trường có quỹ đạo cong, nhưng ta không cần giải cả đường cong đó. Chìa khóa là **phân tích thành hai chuyển động độc lập**: theo phương ngang không có lực nên vật chuyển động thẳng đều $v_x = v_0\cos\alpha$; theo phương thẳng đứng chỉ chịu trọng lực nên là chuyển động biến đổi đều với gia tốc $g$. Hai chuyển động dùng chung một đồng hồ $t$.

## Ném ngang

Ném ngang là trường hợp $\alpha = 0$: $x = v_0 t$, $y = \tfrac12 g t^2$. Thời gian rơi **chỉ phụ thuộc độ cao**, giống hệt rơi tự do: $t = \sqrt{2h/g}$. Vì thế một viên bi ném ngang và một viên bi thả rơi từ cùng độ cao sẽ chạm đất *cùng lúc*. Tầm xa $L = v_0\sqrt{2h/g}$.

## Ném xiên

Với góc ném $\alpha$ và cùng độ cao điểm ném - điểm rơi:

$$t_{bay} = \dfrac{2v_0\sin\alpha}{g}, \quad H = \dfrac{v_0^2\sin^2\alpha}{2g}, \quad L = \dfrac{v_0^2\sin 2\alpha}{g}.$$

Vì $\sin 2\alpha$ đạt cực đại tại $2\alpha = 90^\circ$, **góc ném 45 độ cho tầm xa lớn nhất**. Hai góc phụ nhau (ví dụ 30 độ và 60 độ) cho cùng tầm xa vì $\sin 2\alpha$ bằng nhau.

## Lưu ý

Mô hình bỏ qua sức cản không khí. Tại điểm cao nhất, vận tốc theo phương đứng bằng 0 nhưng vận tốc ngang vẫn còn, nên vật *không* dừng lại.

**Lỗi thường gặp:**
- Cho rằng ném ngang càng nhanh thì thời gian rơi càng lâu. Sai; thời gian rơi chỉ phụ thuộc độ cao vì chuyển động thẳng đứng độc lập với chuyển động ngang.
- Nghĩ tại điểm cao nhất của ném xiên vật đứng yên. Sai; chỉ thành phần vận tốc thẳng đứng bằng 0, thành phần ngang $v_0\cos\alpha$ vẫn được bảo toàn.

<sub>`lesson.physics.vn-thpt-physics-conhiet.chuyen-dong-nem`</sub>

---

### 5. Tính tương đối của chuyển động và công thức cộng vận tốc
*Relativity of motion and velocity addition* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được hệ quy chiếu đứng yên và hệ quy chiếu chuyển động
- Vận dụng được công thức cộng vận tốc cho các trường hợp cùng phương và vuông góc
- Giải được bài toán thuyền qua sông và bài toán vận tốc tương đối giữa hai xe

## Chuyển động là tương đối

Người ngồi trên tàu thấy hành khách bên cạnh đứng yên, nhưng người đứng ở sân ga lại thấy hành khách đó chuyển động. Không ai sai cả: **vận tốc phụ thuộc hệ quy chiếu**. Muốn nói vận tốc của một vật, bắt buộc phải nói rõ *đối với hệ nào*.

## Quy ước chỉ số và công thức cộng vận tốc

Dùng ba chỉ số: 1 là vật khảo sát, 2 là hệ chuyển động (ví dụ dòng nước, con tàu), 3 là hệ đứng yên (bờ, mặt đất). Khi đó:

$$\vec{v}_{13} = \vec{v}_{12} + \vec{v}_{23},$$

trong đó $\vec{v}_{13}$ là vận tốc tuyệt đối (so với đất), $\vec{v}_{12}$ là vận tốc tương đối, $\vec{v}_{23}$ là vận tốc kéo theo. Đây là **phép cộng vectơ**, không phải cộng số học.

## Hai trường hợp hay gặp

Nếu hai vận tốc **cùng phương**: cùng chiều thì cộng độ lớn, ngược chiều thì trừ. Nếu hai vận tốc **vuông góc** (thuyền hướng mũi vuông góc dòng nước): dùng định lí Pythagore $v_{13} = \sqrt{v_{12}^2 + v_{23}^2}$.

## Ứng dụng điển hình

Bài toán thuyền qua sông, máy bay gặp gió, hai xe gặp nhau hay đuổi nhau đều quy về cộng vận tốc. Chọn đúng ba chỉ số và vẽ đúng tam giác vectơ là giải xong.

**Lỗi thường gặp:**
- Cộng số học hai vận tốc vuông góc thành $3 + 4 = 7$ m/s. Sai vì cộng vận tốc là phép cộng vectơ; hai vectơ vuông góc phải dùng Pythagore.
- Nhầm vai trò ba chỉ số, lấy vận tốc nước so với thuyền thay cho thuyền so với nước, dẫn đến sai hướng và sai kết quả. Cần đặt chỉ số nhất quán $\vec{v}_{13}=\vec{v}_{12}+\vec{v}_{23}$.

<sub>`lesson.physics.vn-thpt-physics-conhiet.tinh-tuong-doi-cong-van-toc`</sub>

---

### 6. Chuyển động tròn đều
*Uniform circular motion* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Định nghĩa được tốc độ góc, chu kì, tần số và nêu mối liên hệ giữa chúng
- Thiết lập được liên hệ giữa tốc độ dài và tốc độ góc
- Giải thích được vì sao chuyển động tròn đều luôn có gia tốc dù tốc độ không đổi

## Tốc độ không đổi nhưng vận tốc thì đổi

Một điểm trên vành bánh xe quay đều đi được những cung bằng nhau trong những khoảng thời gian bằng nhau: **tốc độ dài không đổi**. Nhưng *hướng* của vận tốc luôn thay đổi (luôn tiếp tuyến quỹ đạo), nên vận tốc — vốn là vectơ — vẫn biến thiên. Vì có sự biến thiên vận tốc nên **luôn có gia tốc**.

## Các đại lượng đặc trưng

Góc quét trên đơn vị thời gian là tốc độ góc $\omega$. Đi hết một vòng ($2\pi$ rad) mất chu kì $T$, nên:

$$\omega = \dfrac{2\pi}{T} = 2\pi f, \qquad v = \omega r.$$

Công thức $v = \omega r$ giải thích vì sao điểm ở mép ngoài đĩa quay nhanh hơn điểm gần trục: cùng $\omega$ nhưng $r$ lớn hơn.

## Gia tốc hướng tâm

Gia tốc trong chuyển động tròn đều **hướng vào tâm** và có độ lớn:

$$a_{ht} = \dfrac{v^2}{r} = \omega^2 r.$$

Nó không làm thay đổi tốc độ (không có thành phần tiếp tuyến) mà chỉ *bẻ cong* quỹ đạo, giữ vật đi vòng.

## Khi nào cần?

Mọi bài toán vệ tinh, xe vào cua, đồng hồ, đĩa quay đều bắt đầu từ các đại lượng này. Ở bài sau, ta gắn gia tốc hướng tâm với lực để hiểu lực hướng tâm.

**Lỗi thường gặp:**
- Cho rằng chuyển động tròn đều không có gia tốc vì tốc độ không đổi. Sai; vận tốc đổi hướng liên tục nên luôn có gia tốc hướng tâm.
- Quên đổi vòng/phút sang rad/s trước khi tính, hoặc nhầm $\omega$ với $f$. Phải nhân với $2\pi$ vì mỗi vòng ứng với $2\pi$ rad.

<sub>`lesson.physics.vn-thpt-physics-conhiet.chuyen-dong-tron-deu`</sub>

---

## Chương II: Dòng điện không đổi

### 1. Định luật Ohm cho toàn mạch và ghép nguồn điện
*Ohm's law for the whole circuit and combining sources* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu và vận dụng được định luật Ohm cho toàn mạch có điện trở trong
- Tính được cường độ dòng điện và hiệu điện thế mạch ngoài trong mạch kín
- Xác định được suất điện động và điện trở trong của bộ nguồn ghép nối tiếp, song song và hỗn hợp đối xứng

## Nguồn điện không lí tưởng

Pin thực không giữ nguyên hiệu điện thế khi nối tải: càng lấy dòng lớn, hiệu điện thế hai cực càng tụt. Nguyên nhân là **điện trở trong** $r$. Áp dụng định luật bảo toàn năng lượng cho mạch kín gồm nguồn ($\xi, r$) và mạch ngoài $R_N$:

$$I = \dfrac{\xi}{R_N + r}$$

Hiệu điện thế mạch ngoài (cũng là hiệu điện thế hai cực nguồn): $U_N = \xi - I r = I R_N$. Khi mạch hở $I=0$ thì $U_N = \xi$; khi đoản mạch $R_N = 0$ thì $I$ cực đại bằng $\xi/r$.

## Ghép nguồn thành bộ

Khi một pin không đủ, ta ghép nhiều pin. **Nối tiếp** $n$ nguồn giống nhau: suất điện động và điện trở trong đều cộng, $\xi_b = n\xi,\ r_b = nr$ - dùng khi cần hiệu điện thế lớn. **Song song** $m$ nguồn giống nhau: $\xi_b = \xi,\ r_b = r/m$ - dùng khi cần dòng lớn. Bộ **hỗn hợp đối xứng** gồm $m$ dãy song song, mỗi dãy $n$ nguồn nối tiếp: $\xi_b = n\xi,\ r_b = \dfrac{nr}{m}$.

## Khi nào dùng

Nhận dạng nhanh: đề cho mạch một nguồn thì dùng ngay công thức Ohm toàn mạch; đề cho nhiều pin thì trước hết quy về bộ nguồn tương đương rồi mới áp dụng.

**Lỗi thường gặp:**
- Quên điện trở trong r ở mẫu, tính I chỉ bằng ξ/R nên ra dòng lớn hơn thực tế.
- Ghép nguồn song song vẫn cộng suất điện động; thực ra suất điện động bộ song song bằng suất điện động một nguồn, chỉ điện trở trong giảm.
- Nhầm U hai cực nguồn với suất điện động ξ; hai đại lượng chỉ bằng nhau khi mạch hở (không có dòng).

<sub>`lesson.physics.vn-thpt-physics-diendtu.dinh-luat-om-toan-mach-ghep-nguon`</sub>

---

### 2. Công suất điện, định luật Jun - Len-xơ và điện phân Faraday
*Electric power, Joule's law and Faraday electrolysis* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được công và công suất của dòng điện, của nguồn điện và của toàn mạch
- Vận dụng được định luật Jun - Len-xơ để tính nhiệt lượng toả ra trên vật dẫn
- Vận dụng được định luật Faraday để tính khối lượng chất giải phóng khi điện phân

## Dòng điện sinh công như thế nào

Khi dòng chạy qua đoạn mạch có hiệu điện thế $U$, điện trường sinh công dịch chuyển các điện tích. Công và công suất điện:

$$A = UIt, \qquad P = UI$$

Với vật dẫn thuần trở, thay $U = IR$ được $P = I^2 R = \dfrac{U^2}{R}$. Toàn bộ công này biến thành nhiệt - đó là **định luật Jun - Len-xơ**:

$$Q = I^2 R t$$

Với nguồn, công suất nguồn sinh ra là $P_{ng} = \xi I$, một phần hao trên điện trở trong ($I^2 r$), phần còn lại cấp cho mạch ngoài.

## Điện phân và định luật Faraday

Nếu mạch ngoài là bình điện phân, dòng điện gây phản ứng hoá học ở điện cực. Khối lượng chất bám vào catôt tỉ lệ với điện lượng $q = It$:

$$m = \dfrac{1}{F}\cdot\dfrac{A}{n}\,It$$

trong đó $A$ là khối lượng mol nguyên tử, $n$ là hoá trị, $F = 96500$ C/mol là hằng số Faraday. Công thức cho phép mạ điện, tinh luyện kim loại với lượng tính toán chính xác.

## Khi nào dùng

Bài hỏi nhiệt lượng, tiền điện thì dùng công suất và Jun - Len-xơ; bài có bình điện phân, mạ kim loại thì dùng Faraday, nhớ đổi thời gian ra giây.

**Lỗi thường gặp:**
- Quên đổi phút ra giây khi tính điện lượng; công thức Faraday và Jun - Len-xơ đều cần t tính bằng giây.
- Nhầm hoá trị n với số nguyên tử trong công thức hoá học; n là số electron trao đổi của ion kim loại.
- Dùng công suất P = U²/R cho cả đoạn có nguồn hay động cơ; công thức này chỉ đúng cho vật dẫn thuần trở.

<sub>`lesson.physics.vn-thpt-physics-diendtu.cong-suat-dien-jun-lenxo-dien-phan`</sub>

---

## Chương II: Động lực học

### 1. Ba định luật Newton
*Newton's three laws of motion* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu được ba định luật Newton và nêu ý nghĩa của mỗi định luật
- Vận dụng được định luật II Newton để tính gia tốc, lực hoặc khối lượng
- Phân biệt được cặp lực - phản lực với cặp lực cân bằng

## Định luật I: quán tính

Nếu hợp lực tác dụng lên vật bằng 0, vật đang đứng yên sẽ đứng yên mãi, vật đang chuyển động sẽ chuyển động thẳng đều. Vật *không tự nhiên* dừng lại — nó dừng vì có ma sát. Đây là bước ngoặt so với quan niệm cổ đại rằng phải có lực mới duy trì chuyển động.

## Định luật II: liên hệ lực và gia tốc

Hợp lực gây ra gia tốc, không phải vận tốc:

$$\vec{F}_{hl} = m\vec{a}.$$

Gia tốc luôn cùng hướng hợp lực. Đây là công cụ trung tâm của động lực học: muốn tìm gia tốc, hãy tổng hợp mọi lực rồi chia cho khối lượng. Khối lượng đóng vai trò *mức cản trở* thay đổi vận tốc.

## Định luật III: tương tác luôn có hai chiều

Khi vật A đẩy vật B thì B đẩy lại A một lực bằng độ lớn, ngược chiều:

$$\vec{F}_{AB} = -\vec{F}_{BA}.$$

Điểm cốt lõi: hai lực này **đặt vào hai vật khác nhau** nên không bao giờ cân bằng lẫn nhau. Đừng nhầm với hai lực cân bằng cùng đặt lên một vật.

## Cách giải một bài động lực học

Bốn bước: (1) chọn vật khảo sát; (2) vẽ mọi lực tác dụng lên nó; (3) chọn hệ trục và chiếu định luật II lên các trục; (4) giải hệ phương trình. Sơ đồ lực vẽ đúng là nửa lời giải.

**Lỗi thường gặp:**
- Cho rằng lực và phản lực triệt tiêu nhau nên vật không chuyển động. Sai; chúng đặt vào hai vật khác nhau nên không cân bằng trên cùng một vật.
- Nghĩ có lực thì có vận tốc. Sai; lực gây ra gia tốc chứ không phải vận tốc, vật có thể đang chuyển động nhanh mà hợp lực vẫn bằng 0.

<sub>`lesson.physics.vn-thpt-physics-conhiet.ba-dinh-luat-newton`</sub>

---

### 2. Lực hấp dẫn và trọng lực
*Gravitation and weight* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu và vận dụng được định luật vạn vật hấp dẫn của Newton
- Thiết lập được biểu thức gia tốc trọng trường tại mặt đất và ở độ cao h
- Phân biệt được trọng lực với trọng lượng và giải thích hiện tượng tăng - giảm trọng lượng

## Một lực điều khiển cả vũ trụ

Newton nhận ra rằng lực làm quả táo rơi và lực giữ Mặt Trăng quay quanh Trái Đất là *cùng một lực*. Mọi vật có khối lượng đều hút nhau:

$$F = G\dfrac{m_1 m_2}{r^2}.$$

Lực này rất yếu giữa các vật thường (nên ta không cảm nhận) nhưng khổng lồ khi một trong hai vật là hành tinh.

## Trọng lực và gia tốc trọng trường

Áp định luật hấp dẫn cho vật khối lượng $m$ ở gần mặt đất, coi Trái Đất là quả cầu khối lượng $M$, bán kính $R$:

$$P = G\dfrac{Mm}{R^2} = mg \Rightarrow g = \dfrac{GM}{R^2}.$$

Vì $g$ không phụ thuộc $m$, mọi vật rơi tự do như nhau — đúng như đã học. Lên cao $h$ thì khoảng cách tăng, $g$ giảm: $g_h = \dfrac{GM}{(R+h)^2}$.

## Trọng lực khác trọng lượng

Trọng lực là lực hút của Trái Đất, gần như không đổi. Trọng lượng là *độ lớn lực mà vật ép lên giá đỡ hay lực căng dây treo* — nó thay đổi khi hệ có gia tốc. Trong thang máy đi lên nhanh dần, ta thấy nặng hơn; khi rơi tự do, trọng lượng biểu kiến bằng 0 (trạng thái không trọng lượng). Chính hiệu ứng này giúp giải thích cảm giác của phi hành gia trên trạm quỹ đạo.

**Lỗi thường gặp:**
- Cho rằng lên cao thì $g$ tỉ lệ nghịch với khoảng cách. Sai; $g$ tỉ lệ nghịch với BÌNH PHƯƠNG khoảng cách tới tâm Trái Đất.
- Lấy khoảng cách bằng $h$ thay vì $R + h$. Sai; công thức tính từ tâm Trái Đất nên phải cộng bán kính $R$.

<sub>`lesson.physics.vn-thpt-physics-conhiet.luc-hap-dan-trong-luc`</sub>

---

### 3. Lực đàn hồi và định luật Hooke
*Elastic force and Hooke's law* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · co-ban

**Mục tiêu:**
- Nêu được đặc điểm và điều kiện xuất hiện của lực đàn hồi
- Vận dụng được định luật Hooke để tính lực đàn hồi và độ cứng lò xo
- Tính được độ cứng của hệ lò xo ghép nối tiếp và ghép song song

## Vì sao lò xo kéo lại?

Khi kéo hoặc nén một lò xo, các nguyên tử bị dịch khỏi vị trí cân bằng và sinh ra **lực đàn hồi** chống lại biến dạng, luôn hướng về trạng thái tự nhiên. Lực này chỉ tồn tại khi còn biến dạng và biến mất khi lò xo trở lại chiều dài ban đầu.

## Định luật Hooke

Robert Hooke phát hiện: trong giới hạn đàn hồi, lực đàn hồi tỉ lệ thuận với độ biến dạng:

$$F_{dh} = k|\Delta l| = k|l - l_0|.$$

Đồ thị $F$ theo $\Delta l$ là đường thẳng qua gốc, độ dốc chính là độ cứng $k$. Vượt quá giới hạn đàn hồi, lò xo biến dạng dẻo và định luật không còn đúng.

## Lò xo treo thẳng đứng

Treo vật $m$ vào lò xo, ở vị trí cân bằng lực đàn hồi cân bằng trọng lực:

$$k\,\Delta l = mg \Rightarrow \Delta l = \dfrac{mg}{k}.$$

Đo độ dãn ở cân bằng là cách xác định $k$ trong thí nghiệm.

## Ghép lò xo

Ghép **nối tiếp** thì lò xo mềm đi: $\dfrac{1}{k} = \dfrac{1}{k_1} + \dfrac{1}{k_2}$. Ghép **song song** thì cứng lên: $k = k_1 + k_2$. Nhớ mẹo: nối tiếp giống điện trở song song, song song giống điện trở nối tiếp — vì độ cứng đo *độ khó dãn*.

**Lỗi thường gặp:**
- Nhầm công thức ghép: cộng thẳng độ cứng khi nối tiếp. Sai; nối tiếp phải cộng nghịch đảo vì tổng độ dãn tăng, hệ mềm đi.
- Quên rằng cắt ngắn lò xo làm độ cứng tăng. Độ cứng tỉ lệ nghịch với chiều dài tự nhiên nên cắt đôi thì mỗi nửa cứng gấp đôi.

<sub>`lesson.physics.vn-thpt-physics-conhiet.luc-dan-hoi-dinh-luat-hooke`</sub>

---

### 4. Lực ma sát
*Friction forces* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được ma sát nghỉ, ma sát trượt và ma sát lăn
- Vận dụng được công thức lực ma sát trượt để giải bài toán chuyển động
- Giải thích được vai trò hai mặt của ma sát trong đời sống và kĩ thuật

## Ba loại ma sát

Ma sát xuất hiện ở mặt tiếp xúc giữa hai vật. **Ma sát nghỉ** giữ cho vật chưa trượt: nó tự tăng theo ngoại lực đến một giá trị cực đại rồi vật bắt đầu trượt. **Ma sát trượt** cản lại chuyển động trượt. **Ma sát lăn** rất nhỏ, xuất hiện khi vật lăn — đó là lí do người ta dùng bánh xe, ổ bi.

## Công thức ma sát trượt

Độ lớn lực ma sát trượt tỉ lệ với áp lực (phản lực pháp tuyến) $N$:

$$F_{mst} = \mu_t N,$$

trong đó $\mu_t$ là hệ số ma sát trượt, không thứ nguyên, phụ thuộc bản chất và độ nhám hai mặt. Đáng chú ý: lực ma sát trượt **gần như không phụ thuộc diện tích tiếp xúc và tốc độ**.

## Chú ý về áp lực N

Sai lầm phổ biến là lấy $N = mg$ trong mọi trường hợp. Thực ra $N$ là phản lực pháp tuyến, phải tìm từ phương trình theo phương vuông góc mặt. Trên mặt phẳng ngang có lực kéo xiên góc $\alpha$ lên trên thì $N = mg - F\sin\alpha$; trên mặt nghiêng thì $N = mg\cos\theta$.

## Hai mặt của ma sát

Ma sát vừa có hại (làm nóng, mòn máy, tiêu hao năng lượng) vừa có lợi (giúp đi lại, phanh xe, cầm nắm). Kĩ thuật tìm cách giảm ma sát chỗ cần (bôi trơn, ổ bi) và tăng ma sát chỗ khác (rãnh lốp, phanh).

**Lỗi thường gặp:**
- Lấy $N = mg$ ngay cả khi có lực kéo xiên hoặc trên mặt nghiêng. Sai; phải tìm $N$ từ phương trình chiếu theo phương pháp tuyến.
- Cho rằng lực ma sát trượt tăng theo tốc độ hoặc theo diện tích tiếp xúc. Thực nghiệm cho thấy nó gần như chỉ phụ thuộc áp lực và hệ số ma sát.

<sub>`lesson.physics.vn-thpt-physics-conhiet.luc-ma-sat`</sub>

---

### 5. Chuyển động trên mặt phẳng nghiêng
*Motion on an inclined plane* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Phân tích được trọng lực thành hai thành phần trên mặt phẳng nghiêng
- Tính được gia tốc của vật trượt trên mặt nghiêng có và không có ma sát
- Xác định được điều kiện để vật nằm yên hoặc bắt đầu trượt trên mặt nghiêng

## Chọn hệ trục thông minh

Trên mặt phẳng nghiêng, thay vì dùng trục ngang - đứng, ta chọn **một trục dọc theo mặt nghiêng, một trục vuông góc mặt nghiêng**. Khi đó chỉ trọng lực bị phân tích, còn phản lực và ma sát đã nằm sẵn trên trục. Trọng lực tách thành:

$$P_x = mg\sin\theta \ (\text{kéo vật xuống dốc}), \qquad P_y = mg\cos\theta \ (\text{ép vào mặt}).$$

## Mặt nghiêng nhẵn

Không ma sát, chỉ $P_x$ gây gia tốc dọc mặt:

$$a = g\sin\theta.$$

Gia tốc **không phụ thuộc khối lượng** — mọi vật trượt như nhau, giống rơi tự do bị 'pha loãng' theo $\sin\theta$.

## Mặt nghiêng có ma sát

Khi vật trượt xuống, ma sát hướng lên dốc, độ lớn $\mu N = \mu mg\cos\theta$:

$$a = g(\sin\theta - \mu\cos\theta).$$

## Điều kiện nằm yên

Vật đứng yên khi thành phần kéo xuống chưa vượt ma sát nghỉ cực đại: $mg\sin\theta \le \mu_n mg\cos\theta$, tức $\tan\theta \le \mu_n$. Góc mà vật bắt đầu trượt thỏa $\tan\theta = \mu_n$ — đây là cách đo hệ số ma sát nghỉ chỉ bằng một tấm ván nghiêng.

**Lỗi thường gặp:**
- Lấy $N = mg$ trên mặt nghiêng. Sai; áp lực chỉ bằng thành phần vuông góc $N = mg\cos\theta$, nhỏ hơn trọng lực.
- Quên rằng chiều lực ma sát phụ thuộc chiều chuyển động; khi vật đi lên thì ma sát hướng xuống, dấu trong công thức gia tốc đổi.

<sub>`lesson.physics.vn-thpt-physics-conhiet.chuyen-dong-tren-mat-phang-nghieng`</sub>

---

### 6. Lực hướng tâm
*Centripetal force* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Nêu được bản chất của lực hướng tâm và chỉ ra lực đóng vai trò hướng tâm trong mỗi tình huống
- Vận dụng được công thức lực hướng tâm để giải bài toán xe qua cầu, vòng xiếc
- Xác định được tốc độ giới hạn để vật không văng ra hoặc không rời quỹ đạo tròn

## Lực hướng tâm không phải lực mới

Mọi vật chuyển động tròn đều có gia tốc hướng tâm, nên theo định luật II Newton phải có một **hợp lực hướng vào tâm**. Nhưng đó không phải một loại lực riêng: trong từng tình huống, chính lực căng dây, lực hấp dẫn, lực ma sát hay phản lực *đóng vai trò* lực hướng tâm. Câu hỏi luôn phải trả lời là: 'Lực nào ở đây hướng vào tâm?'

$$F_{ht} = m\dfrac{v^2}{r} = m\omega^2 r.$$

## Xe qua cầu

Qua cầu vồng lên, phản lực và trọng lực cho hợp lực hướng xuống (vào tâm): $mg - N = \dfrac{mv^2}{r}$, nên $N < mg$ — xe *nhẹ* hơn. Qua cầu võng xuống thì ngược lại, $N > mg$ — xe *nặng* hơn, dễ hỏng cầu hơn.

## Vòng xiếc thẳng đứng

Tại đỉnh vòng, cả trọng lực và phản lực đều hướng xuống tâm: $mg + N = \dfrac{mv^2}{r}$. Vật chỉ giữ được quỹ đạo khi $N \ge 0$, tức

$$v_{dinh} \ge \sqrt{gr}.$$

Dưới tốc độ này vật rời quỹ đạo và rơi. Đây là lí do xe đạp lộn vòng phải đủ nhanh.

## Lưu ý về lực li tâm

'Lực li tâm' chỉ là cảm giác quán tính trong hệ quy chiếu quay, không phải lực thực trong hệ đứng yên; đừng thêm nó vào sơ đồ lực khi phân tích ở mặt đất.

**Lỗi thường gặp:**
- Coi lực hướng tâm là một lực độc lập cần vẽ thêm vào sơ đồ. Sai; nó là hợp lực của các lực thực đã có, không được cộng thêm.
- Ở đỉnh cầu vồng lấy $N = mg$. Sai; phải trừ đi phần dành cho gia tốc hướng tâm nên $N = mg - \dfrac{mv^2}{r} < mg$.

<sub>`lesson.physics.vn-thpt-physics-conhiet.luc-huong-tam`</sub>

---

### 7. Hệ vật nối dây và ròng rọc
*Connected bodies and pulley systems* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Áp dụng được định luật II Newton cho từng vật trong hệ nối dây
- Tính được gia tốc chung và lực căng dây của hệ vật qua ròng rọc
- Giải được bài toán máy Atwood và hệ vật trên bàn nối với vật treo

## Nguyên tắc: mỗi vật một phương trình

Với hệ nhiều vật nối dây, ta **tách từng vật** và viết định luật II Newton riêng cho mỗi vật. Dây không dãn buộc mọi vật có **cùng độ lớn gia tốc** $a$; dây và ròng rọc lí tưởng cho **lực căng bằng nhau** ở hai đầu. Giải hệ phương trình này ra $a$ và $T$.

## Máy Atwood

Hai vật $m_1 > m_2$ treo hai đầu dây qua ròng rọc. Chọn chiều dương theo chiều chuyển động (vật nặng đi xuống):

$$m_1 g - T = m_1 a, \qquad T - m_2 g = m_2 a.$$

Cộng hai phương trình khử $T$:

$$a = \dfrac{(m_1 - m_2)g}{m_1 + m_2}, \qquad T = \dfrac{2 m_1 m_2 g}{m_1 + m_2}.$$

Mẹo nhanh: gia tốc bằng *hợp lực phát động chia tổng khối lượng*.

## Vật trên bàn nối vật treo

Vật $m_1$ trên bàn ngang (có thể có ma sát) nối qua ròng rọc mép bàn với vật treo $m_2$. Lực phát động là $m_2 g$, lực cản là ma sát $\mu m_1 g$:

$$a = \dfrac{m_2 g - \mu m_1 g}{m_1 + m_2}.$$

## Kinh nghiệm

Luôn chọn *một* chiều dương thống nhất cho cả hệ theo chiều chuyển động dự đoán, rồi giữ nhất quán khi chiếu lực. Nếu ra $a < 0$ thì chiều chuyển động ngược với dự đoán.

**Lỗi thường gặp:**
- Cho rằng lực căng dây bằng trọng lượng vật treo. Sai; khi hệ có gia tốc, lực căng khác $mg$; chỉ bằng $mg$ khi hệ đứng yên hoặc chuyển động đều.
- Dùng chiều dương khác nhau cho hai vật rồi cộng nhầm dấu. Phải chọn một chiều dương thống nhất theo chiều chuyển động cho toàn hệ.

<sub>`lesson.physics.vn-thpt-physics-conhiet.he-vat-noi-day-rong-roc`</sub>

---

## Chương III: Cân bằng và chuyển động quay của vật rắn

### 1. Mômen lực, quy tắc mômen và cân bằng vật rắn
*Torque, the moment rule and rigid-body equilibrium* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Định nghĩa được mômen lực và nêu tác dụng làm quay của lực
- Phát biểu và vận dụng được quy tắc mômen lực cho vật có trục quay cố định
- Nêu được đặc điểm của ngẫu lực và điều kiện cân bằng tổng quát của vật rắn

## Không chỉ độ lớn lực, mà cả điểm đặt

Mở cửa: đẩy ở mép xa bản lề thì dễ, đẩy sát bản lề thì khó dù cùng lực. Vậy tác dụng làm quay phụ thuộc cả **cánh tay đòn** $d$ — khoảng cách từ trục quay đến giá của lực:

$$M = F\,d.$$

Đơn vị N·m. Lực có giá đi qua trục ($d=0$) không gây quay.

## Quy tắc mômen

Vật có trục quay cố định đứng cân bằng khi tổng mômen làm quay hai chiều bằng nhau:

$$\sum M_{thuan} = \sum M_{nghich}.$$

Đây là nguyên lí của đòn bẩy, cân đòn, cần cẩu. Muốn nâng vật nặng bằng lực nhỏ, hãy bố trí cánh tay đòn của lực nhỏ dài hơn.

## Ngẫu lực

Hai lực song song, ngược chiều, cùng độ lớn nhưng khác giá tạo thành **ngẫu lực**. Ngẫu lực không làm vật tịnh tiến mà chỉ làm quay, với mômen $M = F\,d$ ($d$ là khoảng cách giữa hai giá). Đặc biệt mômen ngẫu lực *không phụ thuộc vị trí trục quay*. Vặn vô lăng, mở nắp chai là các ngẫu lực.

## Cân bằng tổng quát

Vật rắn cân bằng khi thỏa đồng thời hai điều kiện: hợp lực bằng 0 (không tịnh tiến) và tổng mômen quanh một trục bất kì bằng 0 (không quay). Đây là công cụ để giải bài thanh, dầm, giá đỡ.

**Lỗi thường gặp:**
- Lấy khoảng cách từ trục đến điểm đặt lực làm cánh tay đòn ngay cả khi lực xiên. Cánh tay đòn là khoảng cách vuông góc từ trục đến GIÁ của lực, phải nhân thêm $\sin$ góc nếu lực xiên.
- Quên trọng lượng thanh khi thanh không nhẹ. Với thanh đồng chất, trọng lực đặt tại trung điểm và phải tính mômen của nó.

<sub>`lesson.physics.vn-thpt-physics-conhiet.momen-luc-can-bang-vat-ran`</sub>

---

### 2. Động lực học vật rắn quay: mômen quán tính, mômen động lượng và động năng quay
*Rotational dynamics: moment of inertia, angular momentum and rotational energy* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · chuyen-sau

**Mục tiêu:**
- Nêu được ý nghĩa của mômen quán tính như số đo mức quán tính quay
- Vận dụng được phương trình động lực học vật rắn quay quanh trục cố định
- Áp dụng được định luật bảo toàn mômen động lượng và tính động năng quay

## Đại lượng tương ứng của khối lượng trong chuyển động quay

Trong chuyển động thẳng, khối lượng đo mức quán tính. Trong chuyển động quay, vai trò đó thuộc về **mômen quán tính** $I$. Điều mới là $I$ phụ thuộc *cách phân bố khối lượng*: khối lượng càng xa trục thì $I$ càng lớn. Với chất điểm $I = mr^2$; với vật đồng chất có công thức riêng (đĩa đặc $\tfrac12 mR^2$, vành tròn $mR^2$, cầu đặc $\tfrac25 mR^2$).

## Phương trình động lực học quay

Định luật II Newton cho chuyển động quay thay lực bằng mômen lực, gia tốc bằng gia tốc góc:

$$M = I\gamma,$$

trong đó $\gamma$ là gia tốc góc. Mômen lực càng lớn, $I$ càng nhỏ thì quay càng nhanh dần.

## Mômen động lượng và bảo toàn

Đại lượng $L = I\omega$ gọi là mômen động lượng. Khi tổng mômen ngoại lực bằng 0:

$$L = I\omega = \text{hằng số}.$$

Đây là lí do vận động viên trượt băng thu tay lại (giảm $I$) thì quay nhanh hơn (tăng $\omega$), vì tích $I\omega$ không đổi.

## Động năng quay

Vật quay tích trữ năng lượng: $W_d = \tfrac12 I\omega^2$. Vật vừa lăn vừa tịnh tiến (không trượt) có động năng toàn phần bằng tổng động năng tịnh tiến và động năng quay — điều này giải thích vì sao vật đặc lăn nhanh hơn vật rỗng khi cùng lăn xuống dốc.

**Lỗi thường gặp:**
- Cho rằng mômen quán tính chỉ phụ thuộc khối lượng. Sai; nó còn phụ thuộc mạnh vào cách phân bố khối lượng so với trục, nên cùng khối lượng nhưng hình dạng khác cho $I$ khác.
- Dùng $M = I\omega$ thay cho $M = I\gamma$. Sai; mômen lực liên hệ với gia tốc GÓC $\gamma$, còn $I\omega$ là mômen động lượng.

<sub>`lesson.physics.vn-thpt-physics-conhiet.dong-luc-hoc-vat-ran-quay`</sub>

---

## Chương III: Từ trường

### 1. Cảm ứng từ và lực từ
*Magnetic flux density and magnetic force* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được khái niệm cảm ứng từ và viết được công thức cảm ứng từ của các dòng điện đặc biệt
- Vận dụng được công thức lực từ tác dụng lên đoạn dây dẫn mang dòng điện
- Xác định được chiều của lực từ bằng quy tắc bàn tay trái

## Từ trường và cảm ứng từ

Xung quanh nam châm hay dòng điện tồn tại **từ trường**. Đại lượng đặc trưng cho nó về mặt tác dụng lực là **cảm ứng từ** $\vec{B}$: phương tiếp tuyến đường sức, độ lớn đo bằng tesla. Một số dòng điện đặc biệt có công thức riêng:

- Dây thẳng dài: $B = 2\cdot10^{-7}\dfrac{I}{r}$
- Tâm vòng tròn bán kính $R$: $B = 2\pi\cdot10^{-7}\dfrac{I}{R}$
- Lòng ống dây dài: $B = 4\pi\cdot10^{-7} nI$ với $n$ là số vòng trên mét.

Khi có nhiều dòng, từ trường tổng bằng tổng vectơ (nguyên lí chồng chất từ trường).

## Lực từ tác dụng lên dây dẫn

Đặt đoạn dây dài $l$ mang dòng $I$ trong từ trường, nó chịu lực từ:

$$F = BIl\sin\alpha$$

với $\alpha$ là góc giữa dây và $\vec{B}$. Lực lớn nhất khi dây vuông góc $\vec{B}$, bằng 0 khi dây song song $\vec{B}$. Chiều lực xác định bằng **quy tắc bàn tay trái**.

## Ứng dụng

Lực từ giữa dây dẫn với từ trường là nguyên lí của động cơ điện và loa. Hai dây song song mang dòng cùng chiều thì hút nhau, ngược chiều thì đẩy nhau, với lực trên mỗi mét $F/l = 2\cdot10^{-7}\dfrac{I_1 I_2}{r}$.

**Lỗi thường gặp:**
- Quên nhân sinα, coi mọi trường hợp như dây vuông góc; khi dây song song B thì lực bằng 0.
- Nhầm công thức từ trường dây thẳng với vòng tròn: dây thẳng chia cho r, vòng tròn có thêm hệ số π.
- Dùng quy tắc bàn tay phải (dành cho chiều B của dòng) để tìm chiều lực từ; chiều lực từ dùng bàn tay trái.

<sub>`lesson.physics.vn-thpt-physics-diendtu.cam-ung-tu-va-luc-tu`</sub>

---

### 2. Lực Lorentz và chuyển động của điện tích trong từ trường
*Lorentz force and charged-particle motion* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Vận dụng được công thức lực Lorentz tác dụng lên điện tích chuyển động
- Giải thích được vì sao điện tích chuyển động vuông góc từ trường đều đi theo quỹ đạo tròn
- Tính được bán kính và chu kì của quỹ đạo tròn trong từ trường đều

## Lực lên một điện tích đang bay

Đoạn dây mang dòng chịu lực từ, mà dòng là dòng các điện tích chuyển động, nên mỗi điện tích cũng chịu lực. Đó là **lực Lorentz**:

$$f = |q|vB\sin\alpha$$

với $\alpha$ là góc giữa $\vec{v}$ và $\vec{B}$. Điểm đặc biệt: lực Lorentz **luôn vuông góc với vận tốc**, nên nó không sinh công, chỉ làm đổi hướng chứ không đổi độ lớn vận tốc.

## Quỹ đạo tròn

Khi $\vec{v}\perp\vec{B}$, lực Lorentz đóng vai trò lực hướng tâm với độ lớn không đổi $|q|vB$, nên điện tích chuyển động **tròn đều**. Cho lực Lorentz bằng lực hướng tâm $\dfrac{mv^2}{R}$:

$$R = \dfrac{mv}{|q|B}, \qquad T = \dfrac{2\pi m}{|q|B}$$

Đáng chú ý, chu kì $T$ không phụ thuộc vận tốc: hạt nhanh đi vòng lớn, hạt chậm đi vòng nhỏ, nhưng thời gian một vòng như nhau. Đây là nguyên lí của máy cyclotron.

## Trường hợp tổng quát

Nếu $\vec{v}$ hợp với $\vec{B}$ một góc bất kì, ta tách vận tốc thành thành phần song song (chuyển động thẳng đều) và vuông góc (chuyển động tròn), tổng hợp cho **quỹ đạo xoắn ốc**.

**Lỗi thường gặp:**
- Cho rằng lực Lorentz sinh công làm điện tích tăng tốc; thực ra lực luôn vuông góc vận tốc nên độ lớn vận tốc không đổi.
- Quên nhân sinα khi v không vuông góc B, hoặc dùng luôn công thức tròn cho quỹ đạo xoắn ốc.
- Cho rằng chu kì phụ thuộc vận tốc; T = 2πm/(qB) chỉ phụ thuộc tỉ số điện tích trên khối lượng và từ trường.

<sub>`lesson.physics.vn-thpt-physics-diendtu.luc-lorentz-chuyen-dong-dien-tich`</sub>

---

## Chương IV: Cảm ứng điện từ

### 1. Từ thông, định luật Faraday và định luật Lenz
*Magnetic flux, Faraday's and Lenz's laws* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được từ thông qua một khung dây phẳng đặt trong từ trường đều
- Vận dụng được định luật Faraday để tính suất điện động cảm ứng
- Xác định được chiều dòng điện cảm ứng bằng định luật Lenz

## Từ thông đo cái gì

Muốn nói tới sự biến thiên của từ trường qua một mạch, ta cần một đại lượng gộp cả $B$, diện tích và hướng đặt khung: đó là **từ thông**

$$\Phi = NBS\cos\alpha$$

với $N$ số vòng, $\alpha$ là góc giữa vectơ pháp tuyến khung và $\vec{B}$. Từ thông cực đại khi khung vuông góc đường sức ($\alpha = 0$), bằng 0 khi mặt khung song song đường sức.

## Định luật Faraday

Faraday phát hiện: chỉ khi từ thông **biến thiên** mới xuất hiện dòng điện trong mạch kín. Độ lớn suất điện động cảm ứng bằng tốc độ biến thiên từ thông:

$$e_c = -\dfrac{\Delta\Phi}{\Delta t}$$

Dấu trừ mang ý nghĩa của định luật Lenz. Từ thông có thể đổi do $B$ đổi, do diện tích đổi (thanh trượt) hay do khung quay (đổi $\alpha$) - máy phát điện dùng chính cách cuối.

## Định luật Lenz

**Dòng cảm ứng có chiều chống lại nguyên nhân sinh ra nó.** Nếu từ thông tăng, dòng cảm ứng tạo từ trường ngược để cản lại; nếu giảm, dòng cảm ứng tạo từ trường cùng chiều để duy trì. Đây là biểu hiện của bảo toàn năng lượng: muốn duy trì biến thiên phải tốn công.

**Lỗi thường gặp:**
- Quên số vòng N khi tính từ thông và suất điện động của cuộn nhiều vòng.
- Nhầm góc α: α là góc giữa pháp tuyến và B chứ không phải giữa mặt phẳng khung và B; hai góc phụ nhau.
- Cho rằng cứ có từ trường mạnh là có dòng cảm ứng; dòng cảm ứng chỉ xuất hiện khi từ thông biến thiên theo thời gian.

<sub>`lesson.physics.vn-thpt-physics-diendtu.tu-thong-dinh-luat-faraday-lenz`</sub>

---

### 2. Hiện tượng tự cảm và năng lượng từ trường
*Self-induction and magnetic energy* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được hiện tượng tự cảm và viết công thức suất điện động tự cảm
- Tính được độ tự cảm của ống dây và năng lượng từ trường tích trữ trong nó
- Vận dụng công thức tính năng lượng và mật độ năng lượng từ trường

## Mạch tự cảm ứng chính nó

Dòng điện chạy qua cuộn dây tạo từ thông riêng $\Phi = Li$ xuyên qua chính nó. Khi dòng biến thiên, từ thông riêng biến thiên và sinh suất điện động cảm ứng ngay trong mạch đó - gọi là **hiện tượng tự cảm**:

$$e_{tc} = -L\dfrac{\Delta i}{\Delta t}$$

Hệ số $L$ là **độ tự cảm**, chỉ phụ thuộc cấu tạo cuộn dây. Với ống dây dài $l$, tiết diện $S$, tổng $N$ vòng: $L = 4\pi\cdot10^{-7}\dfrac{N^2}{l}S$.

Hiện tượng này giải thích tia lửa khi ngắt mạch có cuộn cảm: dòng giảm đột ngột làm $\Delta i/\Delta t$ rất lớn, sinh suất điện động tự cảm cao.

## Năng lượng từ trường

Muốn thiết lập dòng $i$ trong cuộn cảm, nguồn phải thắng suất điện động tự cảm, tốn công tích thành **năng lượng từ trường**:

$$W = \dfrac{1}{2}Li^2$$

Năng lượng này thực chất chứa trong từ trường lấp đầy ống dây, với mật độ $w = \dfrac{B^2}{8\pi k}$ (dạng SI $w = B^2/2\mu_0$). So sánh với tụ điện tích $W = \tfrac12 CU^2$ thấy cuộn cảm là "kho" từ, tụ điện là "kho" điện.

**Lỗi thường gặp:**
- Nhầm năng lượng W = ½Li² với công thức tụ; cuộn cảm dùng dòng i, tụ dùng hiệu điện thế U.
- Cho rằng suất điện động tự cảm phụ thuộc độ lớn dòng; thực ra nó phụ thuộc tốc độ biến thiên Δi/Δt.
- Quên bình phương số vòng N khi tính độ tự cảm của ống dây (L tỉ lệ với N²).

<sub>`lesson.physics.vn-thpt-physics-diendtu.tu-cam-nang-luong-tu-truong`</sub>

---

## Chương IV: Năng lượng, công và công suất

### 1. Công, công suất và hiệu suất
*Work, power and efficiency* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được công của một lực không đổi theo góc giữa lực và độ dịch chuyển
- Phân biệt được công phát động với công cản và tính công suất trung bình, tức thời
- Tính được hiệu suất của một máy hoặc quá trình

## Khi nào lực sinh công?

Một người bê vật đứng yên thấy 'mệt' nhưng theo vật lí *không sinh công cơ học* vì vật không dịch chuyển. Công chỉ xuất hiện khi điểm đặt lực dịch chuyển, và phụ thuộc góc giữa lực với độ dịch chuyển:

$$A = F\,s\cos\alpha.$$

Khi $\alpha < 90^\circ$: công dương (phát động). Khi $\alpha = 90^\circ$: công bằng 0 (lực hướng tâm, trọng lực với vật đi ngang không sinh công). Khi $\alpha > 90^\circ$: công âm (công cản, như ma sát).

## Công suất — nhanh hay chậm

Hai cần cẩu cùng nâng một vật lên cùng độ cao sinh công như nhau, nhưng cái làm nhanh hơn có công suất lớn hơn:

$$P = \dfrac{A}{t} = F v\cos\alpha.$$

Công thức $P = Fv$ rất tiện: xe chạy đều trên đường, lực kéo bằng lực cản, biết công suất động cơ thì suy ra tốc độ tối đa.

## Hiệu suất

Không máy nào biến đổi năng lượng mà không hao phí (ma sát, tỏa nhiệt). Hiệu suất đo phần năng lượng thực sự có ích:

$$H = \dfrac{A_{ci}}{A_{tp}}\cdot 100\% = \dfrac{P_{ci}}{P_{tp}}\cdot 100\%.$$

Hiệu suất luôn nhỏ hơn 100%; phần còn lại chuyển thành nhiệt và các dạng hao phí.

**Lỗi thường gặp:**
- Cho rằng cứ có lực và vật di chuyển là có công. Sai; lực vuông góc với độ dịch chuyển (như lực hướng tâm) không sinh công vì $\cos 90^\circ = 0$.
- Nhầm công với công suất. Công là năng lượng (J), công suất là năng lượng trên thời gian (W); hai cần cẩu sinh công như nhau vẫn có thể khác công suất.

<sub>`lesson.physics.vn-thpt-physics-conhiet.cong-cong-suat-hieu-suat`</sub>

---

### 2. Động năng và định lí biến thiên động năng
*Kinetic energy and the work-energy theorem* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Định nghĩa được động năng và nêu tính chất vô hướng, không âm của nó
- Vận dụng được định lí biến thiên động năng để giải bài toán không cần gia tốc
- Liên hệ được động năng với động lượng

## Năng lượng của chuyển động

Một vật khối lượng $m$ chuyển động với tốc độ $v$ mang **động năng**:

$$W_d = \tfrac12 m v^2.$$

Động năng là đại lượng vô hướng, luôn dương hoặc bằng 0, và tỉ lệ với *bình phương* tốc độ — nên tốc độ tăng gấp đôi thì động năng tăng gấp bốn. Đây là lí do va chạm ở tốc độ cao nguy hiểm hơn nhiều.

## Định lí biến thiên động năng — 'phím tắt' của động lực học

Thay vì đi qua gia tốc và thời gian, ta liên hệ trực tiếp công của hợp lực với thay đổi động năng:

$$A_{hl} = W_{d2} - W_{d1} = \tfrac12 m v_2^2 - \tfrac12 m v_1^2.$$

Công phát động làm động năng tăng, công cản (ma sát) làm động năng giảm. Định lí này *cực mạnh* khi bài toán không cho thời gian, không cần gia tốc: chỉ cần liệt kê công của mọi lực.

## Liên hệ với động lượng

Động năng và động lượng liên hệ qua:

$$W_d = \dfrac{p^2}{2m}.$$

Công thức này hay dùng trong va chạm và bài toán hạt.

## Khi nào chọn định lí này?

Khi biết lực và quãng đường, cần tìm tốc độ (hoặc ngược lại), mà không quan tâm thời gian. Ví dụ: quãng đường hãm phanh, tốc độ vật sau khi trượt một đoạn có ma sát.

**Lỗi thường gặp:**
- Quên rằng công của lực cản mang dấu âm nên ra quãng đường âm. Lực hãm ngược chiều chuyển động nên $\cos 180^\circ = -1$, công âm.
- Cho rằng động năng tỉ lệ thuận với tốc độ. Sai; nó tỉ lệ với bình phương tốc độ, nên tăng tốc độ gấp đôi thì động năng gấp bốn.

<sub>`lesson.physics.vn-thpt-physics-conhiet.dong-nang-dinh-li-bien-thien-dong-nang`</sub>

---

### 3. Thế năng và định luật bảo toàn cơ năng
*Potential energy and conservation of mechanical energy* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được thế năng trọng trường và thế năng đàn hồi, nêu ý nghĩa mốc thế năng
- Phát biểu và vận dụng được định luật bảo toàn cơ năng cho vật chỉ chịu lực thế
- Giải thích được sự giảm cơ năng khi có lực ma sát và tính độ biến thiên cơ năng

## Năng lượng của vị trí

Một vật ở trên cao có khả năng sinh công khi rơi — đó là **thế năng trọng trường** $W_t = mgz$. Giá trị của nó phụ thuộc **mốc thế năng** ta chọn (thường là mặt đất); nhưng *độ biến thiên* thế năng thì không phụ thuộc mốc, và đó mới là đại lượng có ý nghĩa vật lí. Lò xo biến dạng tích trữ thế năng đàn hồi $W_t = \tfrac12 k(\Delta l)^2$.

## Bảo toàn cơ năng

Khi vật chỉ chịu **lực thế** (trọng lực, lực đàn hồi), tổng động năng và thế năng không đổi:

$$W = W_d + W_t = \tfrac12 m v^2 + mgz = \text{hằng số}.$$

Động năng và thế năng chuyển hóa qua lại: vật rơi thì thế năng giảm, động năng tăng; con lắc lên cao thì ngược lại. Định luật này cho phép tính tốc độ tại mọi vị trí *mà không cần biết quỹ đạo hay lực chi tiết* — chỉ cần độ cao.

## Khi có ma sát

Ma sát là lực không thế; nó 'ăn' bớt cơ năng, chuyển thành nhiệt. Khi đó độ giảm cơ năng bằng công của lực ma sát:

$$W_2 - W_1 = A_{ms} = -F_{ms}\,s.$$

Đây là dạng tổng quát hơn của bảo toàn năng lượng: cơ năng không mất đi mà chuyển sang dạng khác.

## Mẹo giải

Chọn hai vị trí, viết cơ năng tại mỗi vị trí, cho bằng nhau (nếu không ma sát) hoặc lấy hiệu bằng công ma sát. Thường không cần biết gia tốc.

**Lỗi thường gặp:**
- Áp dụng bảo toàn cơ năng khi vẫn có ma sát. Sai; ma sát là lực không thế, làm cơ năng giảm, phải dùng độ biến thiên cơ năng bằng công ma sát.
- Cho rằng phải biết khối lượng mới tính được tốc độ. Trong bài chỉ có trọng lực, $m$ triệt tiêu nên tốc độ không phụ thuộc khối lượng.

<sub>`lesson.physics.vn-thpt-physics-conhiet.the-nang-bao-toan-co-nang`</sub>

---

## Chương IX: Sóng ánh sáng

### 1. Tán sắc ánh sáng và giao thoa ánh sáng (Y-âng)
*Dispersion and Young's double-slit interference* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được hiện tượng tán sắc ánh sáng qua lăng kính
- Vận dụng được công thức khoảng vân và vị trí vân sáng, vân tối trong thí nghiệm Y-âng
- Tính được bước sóng ánh sáng từ hệ vân giao thoa

## Tán sắc: ánh sáng trắng là hỗn hợp

Chiếu chùm ánh sáng trắng qua lăng kính, ta thu được dải màu từ đỏ đến tím. Newton giải thích: ánh sáng trắng là hỗn hợp nhiều ánh sáng đơn sắc, mà **chiết suất của lăng kính phụ thuộc bước sóng** (lớn nhất với tia tím, nhỏ nhất với tia đỏ), nên các màu bị lệch khác nhau. Đó là **tán sắc**, giải thích cả cầu vồng.

## Thí nghiệm Y-âng

Chiếu ánh sáng đơn sắc qua hai khe hẹp $S_1, S_2$ cách nhau $a$, trên màn cách hai khe khoảng $D$ xuất hiện các **vân sáng - vân tối** xen kẽ. Đây là bằng chứng ánh sáng có tính chất sóng. Tại điểm cách vân trung tâm đoạn $x$, hiệu đường đi $\Delta d = \dfrac{ax}{D}$ quyết định sáng hay tối:

$$\text{Vân sáng}: \ x = k\dfrac{\lambda D}{a}; \qquad \text{Vân tối}: \ x = \left(k+\dfrac12\right)\dfrac{\lambda D}{a}$$

## Khoảng vân

Khoảng cách giữa hai vân sáng liên tiếp là **khoảng vân**:

$$i = \dfrac{\lambda D}{a}$$

Đo $i$ ta suy ra bước sóng $\lambda = \dfrac{ia}{D}$. Ánh sáng bước sóng lớn (đỏ) cho vân thưa, bước sóng nhỏ (tím) cho vân dày. Với ánh sáng trắng, vân trung tâm màu trắng, hai bên là các dải màu do các bức xạ có khoảng vân khác nhau.

**Lỗi thường gặp:**
- Quên đổi đơn vị (μm, mm, m) đồng nhất khi tính khoảng vân, sai vài bậc mười.
- Nhầm công thức vân tối với vân sáng: vân tối ứng với (k + 0,5), vân sáng ứng với k nguyên.
- Cho rằng tán sắc là do lăng kính nhuộm màu ánh sáng; thực ra lăng kính chỉ tách các màu đã có sẵn trong ánh sáng trắng.

<sub>`lesson.physics.vn-thpt-physics-diendtu.tan-sac-giao-thoa-anh-sang`</sub>

---

## Chương V: Dao động điều hoà

### 1. Dao động điều hoà và các đại lượng đặc trưng
*Simple harmonic motion and its quantities* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Viết được phương trình li độ, vận tốc, gia tốc của dao động điều hoà và nêu quan hệ pha giữa chúng
- Vận dụng được các hệ thức độc lập với thời gian giữa li độ, vận tốc, gia tốc
- Tính được chu kì, tần số, tần số góc và lực kéo về

## Phương trình dao động

Vật dao động điều hoà có li độ biến thiên theo quy luật cosin:

$$x = A\cos(\omega t + \varphi)$$

Đạo hàm liên tiếp cho vận tốc và gia tốc:

$$v = -A\omega\sin(\omega t+\varphi), \qquad a = -\omega^2 x$$

Nhận xét then chốt về pha: $v$ **sớm pha** $\pi/2$ so với $x$, còn $a$ **ngược pha** với $x$. Do đó khi vật qua vị trí cân bằng ($x=0$) thì tốc độ cực đại $v_{max}=\omega A$; khi ở biên ($|x|=A$) thì $v=0$ nhưng gia tốc cực đại $a_{max}=\omega^2 A$.

## Hệ thức độc lập với thời gian

Vì $v$ và $x$ vuông pha, khử $t$ ta được các hệ thức rất mạnh, dùng khi đề không cho thời gian:

$$A^2 = x^2 + \dfrac{v^2}{\omega^2}, \qquad \dfrac{a^2}{\omega^4} + \dfrac{v^2}{\omega^2} = A^2$$

## Chu kì, tần số và lực kéo về

Chu kì $T = \dfrac{2\pi}{\omega}$, tần số $f = \dfrac{1}{T} = \dfrac{\omega}{2\pi}$. Gia tốc $a=-\omega^2 x$ nên **lực kéo về** $F = ma = -m\omega^2 x$: luôn hướng về vị trí cân bằng, đó là dấu hiệu nhận biết dao động điều hoà.

**Lỗi thường gặp:**
- Cho rằng vận tốc cực đại ở biên; thực ra ở biên vật đổi chiều nên v = 0, tốc độ cực đại ở vị trí cân bằng.
- Nhầm quan hệ pha: gia tốc ngược pha li độ (không phải vuông pha), còn vận tốc mới vuông pha với li độ.
- Quên đồng nhất đơn vị khi dùng hệ thức độc lập (x và A cùng cm thì v ra cm/s).

<sub>`lesson.physics.vn-thpt-physics-diendtu.dao-dong-dieu-hoa-dai-luong-dac-trung`</sub>

---

### 2. Con lắc lò xo
*Spring pendulum* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Viết và vận dụng được công thức chu kì con lắc lò xo
- Tính được lực đàn hồi, lực kéo về và chiều dài lò xo trong quá trình dao động
- Xác định được chu kì khi ghép lò xo nối tiếp và song song

## Chu kì con lắc lò xo

Vật khối lượng $m$ gắn lò xo độ cứng $k$ dao động điều hoà với

$$T = 2\pi\sqrt{\dfrac{m}{k}}$$

Điểm quan trọng: chu kì **không phụ thuộc biên độ** và không phụ thuộc cách treo (ngang hay đứng). Với con lắc thẳng đứng, lò xo giãn thêm $\Delta l_0 = mg/k$ ở vị trí cân bằng, cho $T = 2\pi\sqrt{\Delta l_0/g}$.

## Lực kéo về khác lực đàn hồi

Đây là chỗ dễ nhầm nhất. **Lực kéo về** luôn tính theo li độ so với vị trí cân bằng: $F_{kv} = -kx$. **Lực đàn hồi** tính theo độ biến dạng thực của lò xo: $F_{dh} = k|\Delta l_0 + x|$ (con lắc đứng). Với con lắc nằm ngang $\Delta l_0 = 0$ nên hai lực trùng nhau.

Chiều dài lò xo khi dao động: $l = l_0 + \Delta l_0 + x$, biến thiên từ $l_{min}$ đến $l_{max}$.

## Ghép lò xo

Ghép **nối tiếp** thì độ cứng giảm: $\dfrac{1}{k} = \dfrac{1}{k_1}+\dfrac{1}{k_2}$ (chu kì tăng). Ghép **song song** thì độ cứng tăng: $k = k_1 + k_2$ (chu kì giảm). Lưu ý quy tắc ngược với ghép tụ điện.

**Lỗi thường gặp:**
- Cho rằng chu kì phụ thuộc biên độ hay gia tốc trọng trường; với con lắc lò xo T chỉ phụ thuộc m và k.
- Đồng nhất lực kéo về với lực đàn hồi ở con lắc thẳng đứng; hai lực chỉ trùng khi lò xo nằm ngang.
- Áp dụng nhầm quy tắc ghép: nối tiếp lò xo làm mềm đi (k giảm), ngược với cảm nhận trực giác.

<sub>`lesson.physics.vn-thpt-physics-diendtu.con-lac-lo-xo`</sub>

---

### 3. Con lắc đơn
*Simple pendulum* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Viết và vận dụng được công thức chu kì con lắc đơn dao động nhỏ
- Tính được vận tốc và lực căng dây tại một vị trí bất kì bằng bảo toàn năng lượng
- Giải thích được sự thay đổi chu kì theo nhiệt độ và độ cao

## Chu kì con lắc đơn

Con lắc đơn gồm vật nhỏ khối lượng $m$ treo vào dây dài $l$. Khi dao động với biên độ góc nhỏ, thành phần trọng lực đóng vai trò lực kéo về và con lắc dao động điều hoà với

$$T = 2\pi\sqrt{\dfrac{l}{g}}$$

Điểm đáng chú ý: chu kì **không phụ thuộc khối lượng** và không phụ thuộc biên độ (khi biên độ nhỏ), chỉ phụ thuộc chiều dài dây và gia tốc trọng trường. Đây là lí do con lắc từng dùng làm đồng hồ.

## Vận tốc và lực căng dây

Con lắc đơn dao động thì cả độ cao lẫn tốc độ đổi, nên dùng **bảo toàn cơ năng** tính vận tốc tại li độ góc $\alpha$:

$$v = \sqrt{2gl(\cos\alpha - \cos\alpha_0)}$$

và lực căng dây $\tau = mg(3\cos\alpha - 2\cos\alpha_0)$. Lực căng lớn nhất ở vị trí cân bằng (dây chịu cả trọng lực và lực hướng tâm), nhỏ nhất ở biên.

## Ảnh hưởng nhiệt độ và độ cao

Nhiệt độ tăng làm dây dài ra ($l$ tăng) nên chu kì tăng, đồng hồ chạy chậm. Lên cao thì $g$ giảm nên chu kì cũng tăng. Các bài toán đồng hồ chạy nhanh/chậm dựa trên hai hiệu ứng này.

**Lỗi thường gặp:**
- Cho rằng chu kì con lắc đơn phụ thuộc khối lượng vật nặng; công thức chỉ chứa l và g.
- Dùng công thức T = 2π√(l/g) cho biên độ lớn; khi biên độ lớn dao động không còn điều hoà.
- Tính vận tốc bằng công thức dao động điều hoà v = ω√(A²-x²) với li độ dài; nên dùng bảo toàn năng lượng để tránh sai số biên độ lớn.

<sub>`lesson.physics.vn-thpt-physics-diendtu.con-lac-don`</sub>

---

### 4. Năng lượng trong dao động điều hoà
*Energy in simple harmonic motion* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Viết được biểu thức động năng, thế năng và cơ năng của dao động điều hoà
- Chứng minh được cơ năng bảo toàn và tỉ lệ với bình phương biên độ
- Xác định được vị trí tại đó động năng bằng n lần thế năng

## Hai kho năng lượng đổi chỗ nhau

Trong dao động điều hoà, **động năng** $W_d = \tfrac12 mv^2$ và **thế năng** $W_t = \tfrac12 kx^2$ liên tục chuyển hoá. Khi vật ở biên, toàn bộ là thế năng; khi qua vị trí cân bằng, toàn bộ là động năng. Tổng của chúng - **cơ năng** - luôn không đổi (nếu không ma sát):

$$W = W_d + W_t = \dfrac{1}{2}kA^2 = \dfrac{1}{2}m\omega^2 A^2$$

Cơ năng **tỉ lệ với bình phương biên độ**: tăng biên độ gấp đôi thì năng lượng gấp bốn. Đây là hệ quả rất hay dùng trong bài toán.

## Tần số biến đổi năng lượng

Vì $W_t = \tfrac12 kA^2\cos^2(\omega t+\varphi)$ chứa $\cos^2$, nó biến thiên với tần số **gấp đôi** dao động, tức chu kì $T/2$. Động năng cũng vậy. Nhiều bạn quên điều này khi tính khoảng thời gian giữa hai lần động năng bằng thế năng.

## Vị trí phân chia năng lượng

Cho $W_d = nW_t$ và dùng $W = W_d + W_t$ suy ra:

$$x = \pm\dfrac{A}{\sqrt{n+1}}$$

Ví dụ $W_d = W_t$ (n = 1) tại $x = \pm A/\sqrt2$. Công thức này giúp giải nhanh nhiều câu trắc nghiệm.

**Lỗi thường gặp:**
- Quên rằng động năng và thế năng biến thiên với chu kì T/2 (tần số gấp đôi), nên tính sai thời gian.
- Cho rằng cơ năng tỉ lệ với biên độ; thực ra cơ năng tỉ lệ với bình phương biên độ.
- Lẫn thế năng đàn hồi (theo độ biến dạng lò xo) với thế năng dao động (theo li độ) ở con lắc thẳng đứng.

<sub>`lesson.physics.vn-thpt-physics-diendtu.nang-luong-dao-dong-dieu-hoa`</sub>

---

### 5. Dao động tắt dần, dao động cưỡng bức và cộng hưởng
*Damped, forced oscillation and resonance* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Phân biệt được dao động tắt dần, duy trì, cưỡng bức và dao động riêng
- Tính được độ giảm biên độ và quãng đường vật đi được cho tới khi dừng trong dao động tắt dần do ma sát
- Nêu được điều kiện và ứng dụng của hiện tượng cộng hưởng

## Vì sao dao động thực tắt dần

Dao động điều hoà lí tưởng giữ nguyên biên độ mãi mãi, nhưng thực tế luôn có lực cản (ma sát, không khí). Lực cản tiêu hao cơ năng nên biên độ **giảm dần** - đó là **dao động tắt dần**. Với con lắc lò xo trên mặt phẳng ngang có ma sát hệ số $\mu$, sau mỗi nửa chu kì biên độ giảm một lượng không đổi:

$$\Delta A = \dfrac{2\mu mg}{k}$$

Vật dừng lại khi cơ năng còn lại không thắng nổi ma sát nghỉ. Tổng quãng đường đi được đến khi dừng tính từ bảo toàn năng lượng: $S = \dfrac{kA^2}{2\mu mg}$.

## Duy trì, cưỡng bức và cộng hưởng

Muốn dao động không tắt, ta bù năng lượng. Nếu bù đúng phần mất mà không đổi tần số riêng, ta có **dao động duy trì** (như đồng hồ quả lắc). Nếu tác dụng ngoại lực tuần hoàn tần số $f$, hệ dao động **cưỡng bức** với chính tần số $f$ đó.

**Cộng hưởng** xảy ra khi $f = f_0$ (tần số riêng): biên độ đạt cực đại. Cộng hưởng có lợi (đàn, hộp cộng hưởng) nhưng cũng có hại (cầu rung sập, máy móc rung mạnh), nên kĩ thuật thường tránh cho tần số cưỡng bức trùng tần số riêng.

**Lỗi thường gặp:**
- Cho rằng chu kì dao động tắt dần thay đổi nhiều; thực ra chu kì gần như không đổi, chỉ biên độ giảm.
- Nhầm cộng hưởng xảy ra khi ngoại lực mạnh nhất; cộng hưởng xảy ra khi tần số ngoại lực bằng tần số riêng, không phụ thuộc độ lớn lực.
- Quên đổi biên độ ra mét khi tính quãng đường, hoặc dùng ½kA² với A tính bằng cm.

<sub>`lesson.physics.vn-thpt-physics-diendtu.dao-dong-tat-dan-cuong-buc-cong-huong`</sub>

---

### 6. Tổng hợp hai dao động điều hoà cùng phương, cùng tần số
*Superposition of two harmonic oscillations* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Vận dụng được phương pháp giản đồ vectơ (Fre-nen) để tổng hợp hai dao động cùng phương cùng tần số
- Tính được biên độ và pha ban đầu của dao động tổng hợp
- Biện luận được biên độ tổng hợp cực đại, cực tiểu theo độ lệch pha

## Vì sao dùng giản đồ vectơ

Cộng hai hàm cosin cùng tần số $x_1 = A_1\cos(\omega t+\varphi_1)$ và $x_2 = A_2\cos(\omega t+\varphi_2)$ bằng lượng giác rất dài. Fre-nen nhận ra mỗi dao động ứng với một **vectơ quay** có độ dài bằng biên độ và góc bằng pha ban đầu. Vì hai vectơ quay cùng tốc độ $\omega$, tổng của chúng cũng quay với $\omega$, tức dao động tổng hợp cũng điều hoà cùng tần số.

## Công thức tổng hợp

Biên độ tổng hợp theo định lí hàm cosin:

$$A^2 = A_1^2 + A_2^2 + 2A_1 A_2\cos\Delta\varphi$$

và pha ban đầu:

$$\tan\varphi = \dfrac{A_1\sin\varphi_1 + A_2\sin\varphi_2}{A_1\cos\varphi_1 + A_2\cos\varphi_2}$$

## Biện luận biên độ

Từ công thức thấy ngay:
- **Cùng pha** ($\Delta\varphi = 0$): $A = A_1 + A_2$ - cực đại.
- **Ngược pha** ($\Delta\varphi = \pi$): $A = |A_1 - A_2|$ - cực tiểu.
- **Vuông pha** ($\Delta\varphi = \pi/2$): $A = \sqrt{A_1^2 + A_2^2}$.

Nói chung $|A_1 - A_2| \le A \le A_1 + A_2$. Kết quả này rất hay dùng để tìm biên độ lớn nhất, nhỏ nhất khi cho một biên độ thay đổi.

**Lỗi thường gặp:**
- Cộng thẳng hai biên độ A = A1 + A2 bất kể độ lệch pha; chỉ đúng khi hai dao động cùng pha.
- Nhầm dấu độ lệch pha khi tính, dẫn tới lẫn cực đại với cực tiểu của biên độ.
- Quên rằng biên độ tổng hợp luôn nằm trong đoạn [|A1−A2|, A1+A2], nên chọn đáp án nằm ngoài khoảng này.

<sub>`lesson.physics.vn-thpt-physics-diendtu.tong-hop-hai-dao-dong-dieu-hoa`</sub>

---

## Chương V: Động lượng

### 1. Động lượng, định luật bảo toàn động lượng và va chạm
*Momentum, its conservation and collisions* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Định nghĩa được động lượng và phát biểu định lí biến thiên động lượng
- Phát biểu và vận dụng được định luật bảo toàn động lượng cho hệ kín
- Phân biệt và giải được va chạm mềm với va chạm đàn hồi trực diện

## Vì sao cần một đại lượng ngoài động năng?

Động năng vô hướng, không giữ được thông tin về hướng và thường không bảo toàn trong va chạm. Ta cần một đại lượng *vectơ* và *bảo toàn* mạnh hơn: **động lượng** $\vec{p} = m\vec{v}$.

## Định lí biến thiên động lượng

Xung lượng của lực (tích lực với thời gian tác dụng) bằng độ biến thiên động lượng:

$$\vec{F}\,\Delta t = \Delta \vec{p} = m\vec{v}_2 - m\vec{v}_1.$$

Đây là lí do túi khí, đệm rơi kéo dài thời gian va chạm để giảm lực.

## Định luật bảo toàn động lượng

Với hệ kín, tổng động lượng trước bằng tổng động lượng sau:

$$m_1\vec{v}_1 + m_2\vec{v}_2 = m_1\vec{v}_1' + m_2\vec{v}_2'.$$

Đây là **phương trình vectơ** — với va chạm thẳng, chiếu lên trục và cẩn thận dấu. Áp dụng cho va chạm, đạn nổ, súng giật, tên lửa phản lực.

## Hai loại va chạm

**Va chạm mềm**: hai vật dính nhau, $v = \dfrac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$; động lượng bảo toàn nhưng động năng giảm. **Va chạm đàn hồi trực diện**: bảo toàn cả động lượng lẫn động năng, cho công thức

$$v_1' = \dfrac{(m_1-m_2)v_1 + 2m_2 v_2}{m_1+m_2}.$$

Dấu hiệu nhận biết nhanh: hai vật cùng khối lượng va chạm đàn hồi thì *trao đổi vận tốc* cho nhau.

**Lỗi thường gặp:**
- Áp dụng bảo toàn động năng cho va chạm mềm. Sai; va chạm mềm chỉ bảo toàn động lượng, động năng luôn giảm vì có biến dạng và tỏa nhiệt.
- Cộng động lượng như đại lượng vô hướng khi hai vật chuyển động ngược chiều. Động lượng là vectơ; phải gán dấu theo chiều dương đã chọn trước khi cộng.

<sub>`lesson.physics.vn-thpt-physics-conhiet.dong-luong-bao-toan-va-cham`</sub>

---

## Chương VI: Sóng cơ

### 1. Sóng cơ và phương trình sóng
*Mechanical waves and the wave equation* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được khái niệm sóng cơ, phân biệt sóng dọc và sóng ngang
- Vận dụng được công thức liên hệ bước sóng, tốc độ và chu kì
- Viết được phương trình sóng và tính độ lệch pha giữa hai điểm trên phương truyền

## Sóng truyền cái gì

Khi một phần tử môi trường dao động, nó kéo phần tử bên cạnh dao động theo, tạo thành **sóng cơ** lan truyền. Điều quan trọng: sóng **truyền pha dao động và năng lượng**, còn các phần tử vật chất chỉ dao động quanh vị trí cân bằng, không bị cuốn đi. Nếu phần tử dao động vuông góc phương truyền là **sóng ngang**, dao động dọc theo phương truyền là **sóng dọc**.

## Bước sóng và các đại lượng

Trong một chu kì $T$, sóng đi được một **bước sóng**:

$$\lambda = vT = \dfrac{v}{f}$$

Bước sóng cũng là khoảng cách giữa hai điểm gần nhất dao động **cùng pha**. Tốc độ $v$ phụ thuộc môi trường (không phụ thuộc nguồn), còn tần số $f$ do nguồn quyết định.

## Phương trình sóng và độ lệch pha

Nếu nguồn O dao động $u_O = A\cos\omega t$ thì điểm M cách O đoạn $d$ dao động **trễ** hơn:

$$u_M = A\cos\!\left(\omega t - \dfrac{2\pi d}{\lambda}\right)$$

Hai điểm cách nhau $d$ lệch pha $\Delta\varphi = \dfrac{2\pi d}{\lambda}$: cùng pha khi $d = k\lambda$, ngược pha khi $d = (k+0{,}5)\lambda$, vuông pha khi $d = (2k+1)\lambda/4$.

**Lỗi thường gặp:**
- Cho rằng các phần tử môi trường bị sóng cuốn đi; thực ra chúng chỉ dao động tại chỗ.
- Nhầm bước sóng với biên độ hoặc với quãng đường sóng đi trong một giây; bước sóng là quãng đường trong một chu kì.
- Quên đổi đơn vị đồng nhất giữa d và λ khi tính độ lệch pha.

<sub>`lesson.physics.vn-thpt-physics-diendtu.song-co-phuong-trinh-song`</sub>

---

### 2. Giao thoa sóng cơ
*Interference of mechanical waves* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Nêu được điều kiện giao thoa và khái niệm hai nguồn kết hợp
- Xác định được vị trí cực đại, cực tiểu giao thoa theo hiệu đường đi
- Tính được số điểm cực đại, cực tiểu trên đoạn nối hai nguồn

## Khi hai sóng gặp nhau

Cho hai nguồn **kết hợp** (cùng tần số, hiệu pha không đổi) truyền sóng gặp nhau, tại mỗi điểm hai sóng chồng chất. Kết quả là những vùng dao động rất mạnh xen kẽ vùng đứng yên, ổn định theo thời gian - đó là **giao thoa**. Biên độ tại một điểm phụ thuộc hiệu đường đi $\Delta d = d_2 - d_1$.

## Điều kiện cực đại, cực tiểu

Với hai nguồn **cùng pha**:

$$\text{Cực đại}: \ d_2 - d_1 = k\lambda; \qquad \text{Cực tiểu}: \ d_2 - d_1 = \left(k+\dfrac12\right)\lambda$$

Tại cực đại hai sóng cùng pha nên biên độ $2A$; tại cực tiểu ngược pha nên triệt tiêu. Nếu hai nguồn **ngược pha** thì điều kiện đảo lại.

## Đếm số cực đại, cực tiểu

Trên đoạn nối hai nguồn cách nhau $S_1S_2 = L$, số cực đại là số giá trị nguyên $k$ thoả

$$-\dfrac{L}{\lambda} < k < \dfrac{L}{\lambda}$$

(với hai nguồn cùng pha). Số cực tiểu là số nửa nguyên trong cùng khoảng. Đây là dạng bài đếm điểm rất thường gặp; nhớ vẽ trục và xét dấu bất đẳng thức cẩn thận.

**Lỗi thường gặp:**
- Lấy hai nguồn bất kì làm nguồn kết hợp; chỉ hai nguồn cùng tần số và hiệu pha không đổi mới giao thoa ổn định.
- Nhầm điều kiện cực đại và cực tiểu khi hai nguồn ngược pha; lúc đó công thức đảo lại.
- Dùng dấu ≤ thay vì dấu < khi đếm điểm trên đoạn thẳng nối hai nguồn, làm đếm dư hai điểm ở đầu mút.

<sub>`lesson.physics.vn-thpt-physics-diendtu.giao-thoa-song-co`</sub>

---

### 3. Sóng dừng
*Standing waves* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được sự hình thành sóng dừng do giao thoa sóng tới và sóng phản xạ
- Vận dụng được điều kiện sóng dừng trên dây hai đầu cố định và một đầu tự do
- Xác định được vị trí, khoảng cách nút và bụng sóng

## Sóng dừng hình thành thế nào

Khi sóng truyền trên dây gặp đầu cố định, nó phản xạ ngược lại. Sóng tới và sóng phản xạ cùng tần số, truyền ngược chiều, giao thoa với nhau tạo ra **sóng dừng**: có những điểm luôn đứng yên (**nút**) xen kẽ điểm dao động mạnh nhất (**bụng**), và các vị trí này **cố định** theo thời gian.

Khoảng cách giữa hai nút liền kề (hoặc hai bụng liền kề) bằng $\lambda/2$; khoảng cách nút tới bụng gần nhất bằng $\lambda/4$.

## Điều kiện sóng dừng

Sóng dừng chỉ hình thành khi chiều dài dây ăn khớp với bước sóng.

- **Hai đầu cố định** (hai đầu là nút): $l = k\dfrac{\lambda}{2}$, số bụng bằng $k$, số nút bằng $k+1$.
- **Một đầu cố định, một đầu tự do** (đầu tự do là bụng): $l = (2k+1)\dfrac{\lambda}{4}$.

## Ứng dụng

Sóng dừng là cơ sở của nhạc cụ dây và ống sáo. Tần số nhỏ nhất tạo sóng dừng gọi là **hoạ âm cơ bản**; các tần số bội của nó là **hoạ âm** bậc cao, quyết định âm sắc. Dây đàn hai đầu cố định cho họa âm $f_k = k\dfrac{v}{2l}$; ống sáo một đầu kín cho $f = (2k+1)\dfrac{v}{4l}$.

**Lỗi thường gặp:**
- Cho rằng khoảng cách hai nút liền kề bằng bước sóng; thực ra bằng nửa bước sóng.
- Áp dụng nhầm điều kiện hai đầu cố định cho dây một đầu tự do; đầu tự do là bụng nên công thức khác.
- Đếm nhầm số nút và số bụng: hai đầu cố định có số nút nhiều hơn số bụng đúng một.

<sub>`lesson.physics.vn-thpt-physics-diendtu.song-dung`</sub>

---

### 4. Sóng âm và mức cường độ âm
*Sound waves and sound intensity level* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Nêu được các đặc trưng vật lí và sinh lí của âm
- Vận dụng được công thức cường độ âm và mức cường độ âm
- Giải được bài toán so sánh mức cường độ âm tại các điểm khác nhau

## Âm là sóng cơ

Âm là sóng cơ lan truyền trong các môi trường rắn, lỏng, khí (không truyền trong chân không). Tai người nghe được âm tần số 16 Hz đến 20000 Hz. Âm có ba đặc trưng **vật lí** (tần số, cường độ, đồ thị dao động) gắn với ba đặc trưng **sinh lí** (độ cao, độ to, âm sắc).

## Cường độ âm và định luật giảm theo khoảng cách

**Cường độ âm** $I$ là công suất âm qua một đơn vị diện tích. Với nguồn điểm phát đều ra mọi hướng, năng lượng trải trên mặt cầu bán kính $r$:

$$I = \dfrac{P}{4\pi r^2}$$

nên cường độ giảm theo bình phương khoảng cách. Đây là chìa khoá của các bài so sánh hai điểm: $\dfrac{I_1}{I_2} = \dfrac{r_2^2}{r_1^2}$.

## Mức cường độ âm

Tai người cảm nhận theo thang loga, nên ta dùng **mức cường độ âm**:

$$L = 10\lg\dfrac{I}{I_0}\ (\text{dB}), \qquad I_0 = 10^{-12}\ \text{W/m}^2$$

Hệ quả hay dùng: hiệu mức cường độ âm giữa hai điểm $L_1 - L_2 = 10\lg\dfrac{I_1}{I_2} = 20\lg\dfrac{r_2}{r_1}$. Nhờ thang loga, cường độ tăng 10 lần thì mức chỉ tăng 10 dB.

**Lỗi thường gặp:**
- Cho rằng cường độ âm giảm tỉ lệ nghịch với khoảng cách; thực ra giảm theo bình phương khoảng cách.
- Nhầm cường độ âm với mức cường độ âm; cường độ đo bằng W/m², mức đo bằng dB theo thang loga.
- Cộng trực tiếp mức cường độ âm (dB) khi có nhiều nguồn; phải cộng cường độ I rồi mới lấy loga.

<sub>`lesson.physics.vn-thpt-physics-diendtu.song-am-muc-cuong-do-am`</sub>

---

## Chương VI: Vật lí nhiệt và nhiệt động lực học

### 1. Nội năng và định luật I nhiệt động lực học
*Internal energy and the first law of thermodynamics* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Nêu được khái niệm nội năng và hai cách làm biến đổi nội năng
- Phát biểu và vận dụng được định luật I nhiệt động lực học với quy ước dấu
- Áp dụng được định luật I cho các quá trình đẳng tích, đẳng áp, đẳng nhiệt

## Nội năng là gì?

Mỗi phân tử luôn chuyển động hỗn loạn và tương tác với nhau. Tổng động năng chuyển động nhiệt và thế năng tương tác của tất cả phân tử gọi là **nội năng** $U$. Với khí lí tưởng, bỏ qua tương tác nên nội năng chỉ là tổng động năng phân tử, và **chỉ phụ thuộc nhiệt độ**: nhiệt độ tăng thì nội năng tăng.

## Hai cách đổi nội năng

Có thể thay đổi nội năng bằng **thực hiện công** (cọ xát, nén khí) hoặc **truyền nhiệt** (đun nóng, tiếp xúc vật nóng). Hai cách khác nhau về bản chất nhưng cùng dẫn tới một kết quả — nội năng thay đổi.

## Định luật I nhiệt động lực học

Đây là định luật bảo toàn năng lượng cho hệ nhiệt:

$$\Delta U = Q + A,$$

với quy ước: hệ **nhận nhiệt** thì $Q>0$, **tỏa nhiệt** thì $Q<0$; hệ **nhận công** (bị nén) thì $A>0$, **sinh công** (dãn) thì $A<0$. Nắm chắc dấu là chìa khóa của mọi bài nhiệt động lực học.

## Áp dụng cho các quá trình

- **Đẳng tích** ($V$ không đổi): khí không sinh công, $A=0$ nên $\Delta U = Q$ — mọi nhiệt lượng thành nội năng.
- **Đẳng nhiệt** ($T$ không đổi): với khí lí tưởng $\Delta U = 0$ nên $Q = -A$ — nhiệt nhận vào bằng công khí sinh ra.
- **Đẳng áp** ($p$ không đổi): khí sinh công $A = -p\Delta V$, đồng thời nội năng đổi; nhiệt lượng chia cho cả hai phần.

**Lỗi thường gặp:**
- Nhầm dấu công: lấy $A = +120$ J khi khí sinh công. Theo quy ước $\Delta U = Q + A$, khí sinh công thì $A$ mang dấu âm.
- Cho rằng đun nóng khí thì toàn bộ nhiệt thành nội năng. Chỉ đúng khi đẳng tích; nếu khí dãn nở, một phần nhiệt chuyển thành công.

<sub>`lesson.physics.vn-thpt-physics-conhiet.noi-nang-dinh-luat-i-nhiet-dong-luc-hoc`</sub>

---

### 2. Nhiệt lượng, phương trình cân bằng nhiệt và sự chuyển thể
*Heat, thermal equilibrium and phase changes* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được nhiệt lượng thu vào hay tỏa ra khi vật thay đổi nhiệt độ
- Vận dụng được phương trình cân bằng nhiệt để tìm nhiệt độ cân bằng
- Tính được nhiệt lượng trong quá trình nóng chảy và hóa hơi

## Nhiệt lượng làm đổi nhiệt độ

Để một vật khối lượng $m$ tăng nhiệt độ thêm $\Delta t$, cần cung cấp nhiệt lượng:

$$Q = mc\Delta t,$$

với $c$ là nhiệt dung riêng — đặc trưng cho từng chất. Nước có $c$ rất lớn ($4200$ J/(kg·K)) nên khó nóng, khó nguội, giúp điều hòa khí hậu.

## Phương trình cân bằng nhiệt

Khi các vật trao đổi nhiệt trong bình cách nhiệt, chúng tiến tới cùng một nhiệt độ. Bảo toàn năng lượng cho:

$$Q_{toa} = Q_{thu}.$$

Vật nóng tỏa nhiệt (giảm nhiệt độ), vật lạnh thu nhiệt (tăng nhiệt độ), gặp nhau ở nhiệt độ cân bằng $t$. Đây là nguyên lí của nhiệt lượng kế.

## Chuyển thể — nhiệt 'ẩn'

Khi chất **nóng chảy** hay **hóa hơi**, nhiệt độ *không đổi* dù vẫn nhận nhiệt; nhiệt lượng dùng để phá vỡ liên kết phân tử:

$$Q = \lambda m \ (\text{nóng chảy}), \qquad Q = L m \ (\text{hóa hơi}).$$

Với nước: nhiệt nóng chảy $\lambda = 3{,}4\cdot 10^5$ J/kg, nhiệt hóa hơi $L = 2{,}3\cdot 10^6$ J/kg. Hóa hơi tốn nhiều năng lượng hơn hẳn — vì thế mồ hôi bay hơi làm mát cơ thể rất hiệu quả.

## Bài toán tổng hợp

Làm tan một tảng nước đá rồi đun sôi cần cộng nhiều giai đoạn: hâm nóng đá, nóng chảy, hâm nóng nước, hóa hơi — mỗi giai đoạn một công thức riêng.

**Lỗi thường gặp:**
- Quên nhiệt nóng chảy, chỉ tính nhiệt hâm nóng nước đá. Sai; đá phải nhận nhiệt nóng chảy $\lambda m$ để tan trước khi nhiệt độ tăng.
- Cho rằng trong quá trình nóng chảy nhiệt độ vẫn tăng. Sai; khi chất đang chuyển thể, nhiệt độ giữ nguyên tại điểm chuyển thể.

<sub>`lesson.physics.vn-thpt-physics-conhiet.nhiet-luong-can-bang-nhiet-chuyen-the`</sub>

---

### 3. Hiệu suất của động cơ nhiệt
*Efficiency of heat engines* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Nêu được nguyên tắc hoạt động và sơ đồ năng lượng của động cơ nhiệt
- Tính được hiệu suất của động cơ nhiệt theo nhiệt lượng nhận và tỏa
- Vận dụng được giới hạn hiệu suất Carnot và nêu ý nghĩa nguyên lí II

## Biến nhiệt thành công — nhưng không trọn vẹn

Động cơ nhiệt (máy hơi nước, động cơ ô tô) nhận nhiệt $Q_1$ từ **nguồn nóng**, biến một phần thành công $A$, và buộc phải **thải nhiệt thừa** $Q_2$ ra nguồn lạnh. Định luật bảo toàn năng lượng cho:

$$A = Q_1 - Q_2.$$

## Hiệu suất

Hiệu suất đo phần nhiệt biến thành công có ích:

$$H = \dfrac{A}{Q_1} = \dfrac{Q_1 - Q_2}{Q_1} = 1 - \dfrac{Q_2}{Q_1}.$$

Vì luôn có nhiệt thải ($Q_2 > 0$), hiệu suất luôn nhỏ hơn 100% — đây không phải do máy chưa hoàn thiện mà là *giới hạn nguyên lí*.

## Giới hạn Carnot và nguyên lí II

**Nguyên lí II nhiệt động lực học** khẳng định: không thể chế tạo động cơ biến hoàn toàn nhiệt thành công. Sadi Carnot chứng minh hiệu suất cực đại chỉ phụ thuộc nhiệt độ hai nguồn:

$$H_{max} = 1 - \dfrac{T_2}{T_1},$$

với $T_1, T_2$ tính bằng Kelvin. Muốn hiệu suất cao, cần nguồn nóng thật nóng và nguồn lạnh thật lạnh. Mọi động cơ thực có hiệu suất *nhỏ hơn* $H_{max}$.

## Ý nghĩa thực tiễn

Động cơ ô tô thực đạt khoảng 25–40%. Phần lớn nhiên liệu thành nhiệt thải — đó là lí do cần bộ tản nhiệt và ống xả. Hiểu giới hạn này giúp đánh giá đúng các tuyên bố về 'động cơ hiệu suất 100%'.

**Lỗi thường gặp:**
- Cho rằng có thể chế tạo động cơ hiệu suất 100%. Nguyên lí II bác bỏ điều này; luôn phải thải nhiệt $Q_2 > 0$ ra nguồn lạnh.
- Dùng nhiệt độ Celsius trong công thức Carnot. Sai; $H_{max} = 1 - T_2/T_1$ đòi hỏi nhiệt độ tuyệt đối (Kelvin).

<sub>`lesson.physics.vn-thpt-physics-conhiet.hieu-suat-dong-co-nhiet`</sub>

---

## Chương VII: Dòng điện xoay chiều

### 1. Đại cương về dòng điện xoay chiều và giá trị hiệu dụng
*Alternating current fundamentals and RMS values* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được nguyên tắc tạo ra dòng điện xoay chiều bằng khung dây quay trong từ trường
- Phân biệt và tính được giá trị cực đại, giá trị hiệu dụng của điện áp và dòng điện
- Nêu được quan hệ pha giữa u và i trên từng phần tử R, L, C và tính cảm kháng, dung kháng

## Tạo ra dòng xoay chiều

Cho khung dây quay đều trong từ trường, từ thông qua khung biến thiên điều hoà nên xuất hiện suất điện động cảm ứng xoay chiều:

$$e = E_0\cos(\omega t + \varphi), \qquad E_0 = NBS\omega$$

Đây là nguyên tắc của máy phát điện. Nối khung với mạch ngoài ta được dòng điện xoay chiều.

## Giá trị hiệu dụng

Dòng xoay chiều đổi chiều liên tục nên giá trị trung bình bằng 0; ta đặc trưng nó bằng **giá trị hiệu dụng**, định nghĩa từ nhiệt lượng toả ra:

$$I = \dfrac{I_0}{\sqrt2}, \qquad U = \dfrac{U_0}{\sqrt2}$$

Ampe kế và vôn kế xoay chiều đều chỉ giá trị hiệu dụng. Khi nói "điện 220 V" là nói giá trị hiệu dụng, còn điện áp cực đại là $220\sqrt2 \approx 311$ V.

## Quan hệ pha trên R, L, C

- Điện trở R: $u$ **cùng pha** $i$.
- Cuộn cảm L: $u$ **sớm pha** $\pi/2$ so với $i$, cản trở bằng cảm kháng $Z_L = \omega L$.
- Tụ điện C: $u$ **trễ pha** $\pi/2$ so với $i$, cản trở bằng dung kháng $Z_C = 1/(\omega C)$.

Nhớ câu "L sớm, C trễ" giúp không nhầm dấu độ lệch pha khi ghép mạch.

**Lỗi thường gặp:**
- Dùng giá trị cực đại thay cho giá trị hiệu dụng khi tính công suất hay khi nói điện áp định mức.
- Nhầm quan hệ pha: cho rằng u trễ pha so với i trên cuộn cảm; thực ra trên L thì u sớm pha, trên C thì u trễ pha.
- Lẫn cảm kháng với dung kháng: Z_L tỉ lệ thuận với tần số, còn Z_C tỉ lệ nghịch với tần số.

<sub>`lesson.physics.vn-thpt-physics-diendtu.dai-cuong-dong-dien-xoay-chieu`</sub>

---

### 2. Mạch RLC nối tiếp: tổng trở và độ lệch pha
*Series RLC circuit: impedance and phase* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Vận dụng được công thức tổng trở và định luật Ohm cho mạch RLC nối tiếp
- Tính được độ lệch pha giữa điện áp và dòng điện
- Sử dụng được giản đồ vectơ để tổng hợp điện áp trong mạch

## Cộng điện áp bằng giản đồ vectơ

Trong mạch RLC nối tiếp, dòng $i$ chung cho cả ba phần tử, còn điện áp trên mỗi phần tử lệch pha khác nhau so với $i$. Vì thế điện áp tổng **không** bằng tổng đại số $U_R + U_L + U_C$ mà phải cộng vectơ. Chọn trục theo $i$: $U_R$ cùng phương $i$, $U_L$ vuông góc hướng lên, $U_C$ vuông góc hướng xuống. Cộng vectơ cho

$$U = \sqrt{U_R^2 + (U_L - U_C)^2}$$

## Tổng trở

Chia cho $I$, và vì $U_R = IR,\ U_L = IZ_L,\ U_C = IZ_C$, ta được **tổng trở**:

$$Z = \sqrt{R^2 + (Z_L - Z_C)^2}, \qquad I = \dfrac{U}{Z}$$

## Độ lệch pha

Góc lệch pha giữa $u$ và $i$ xác định bởi:

$$\tan\varphi = \dfrac{Z_L - Z_C}{R} = \dfrac{U_L - U_C}{U_R}$$

Nếu $Z_L > Z_C$ mạch có **tính cảm kháng**, $u$ sớm pha hơn $i$ ($\varphi > 0$). Nếu $Z_L < Z_C$ mạch có **tính dung kháng**, $u$ trễ pha hơn $i$. Đây là bước bắt buộc trước khi viết biểu thức tức thời của $u$ hay $i$.

**Lỗi thường gặp:**
- Cộng đại số U_R + U_L + U_C để ra điện áp toàn mạch; phải cộng vectơ vì chúng lệch pha.
- Lấy hiệu Z_C − Z_L trong công thức tổng trở; thứ tự không ảnh hưởng vì bình phương, nhưng dấu của (Z_L − Z_C) quyết định tính cảm hay dung của mạch.
- Quên rằng mọi giá trị trong định luật Ohm xoay chiều là giá trị hiệu dụng, không phải cực đại.

<sub>`lesson.physics.vn-thpt-physics-diendtu.mach-rlc-noi-tiep-tong-tro`</sub>

---

### 3. Công suất, hệ số công suất, cộng hưởng và bài toán cực trị
*Power, power factor, resonance and extrema* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · chuyen-sau

**Mục tiêu:**
- Tính được công suất tiêu thụ và hệ số công suất của mạch RLC
- Nêu được điều kiện và đặc điểm của hiện tượng cộng hưởng điện
- Giải được bài toán cực trị khi R, L, C hoặc tần số thay đổi

## Công suất do đâu mà có

Trong mạch RLC, cuộn cảm và tụ chỉ tích - phóng năng lượng chứ không tiêu thụ; **chỉ điện trở** biến điện năng thành nhiệt. Công suất tiêu thụ:

$$P = UI\cos\varphi = I^2 R, \qquad \cos\varphi = \dfrac{R}{Z}$$

Đại lượng $\cos\varphi$ là **hệ số công suất**. Trong truyền tải, hệ số công suất thấp buộc dòng lớn hơn để tải cùng công suất, làm hao phí tăng, nên các nhà máy luôn nâng $\cos\varphi$.

## Cộng hưởng điện

Khi thay đổi $L$, $C$ hoặc tần số sao cho

$$Z_L = Z_C \quad\Leftrightarrow\quad \omega = \dfrac{1}{\sqrt{LC}}$$

thì tổng trở nhỏ nhất $Z = R$, dòng điện và công suất **cực đại**, $u$ cùng pha $i$, $\cos\varphi = 1$. Đó là **cộng hưởng điện**, được dùng trong mạch chọn sóng radio.

## Bài toán cực trị

Khi một đại lượng thay đổi, dùng các kết quả nhanh:
- $R$ thay đổi để $P_{max}$: $R = |Z_L - Z_C|$, khi đó $P_{max} = \dfrac{U^2}{2R}$.
- Hai giá trị $R_1, R_2$ cho cùng $P$: $R_1 R_2 = (Z_L - Z_C)^2$.
- $C$ thay đổi để $U_C$ cực đại, $L$ thay đổi để $U_L$ cực đại: có công thức riêng dựa trên giản đồ.

**Lỗi thường gặp:**
- Cho rằng cuộn cảm và tụ điện tiêu thụ công suất; chỉ điện trở R tiêu thụ, P = I²R.
- Nhầm cộng hưởng là khi Z_L = Z_C = 0; thực ra cộng hưởng khi Z_L = Z_C (chúng bằng nhau và khác 0), lúc đó chúng triệt tiêu nhau.
- Dùng cosφ = R/Z nhưng quên rằng khi cộng hưởng Z = R nên cosφ = 1, dễ tính nhầm còn dư số hạng.

<sub>`lesson.physics.vn-thpt-physics-diendtu.cong-suat-he-so-cong-suat-cong-huong`</sub>

---

### 4. Máy biến áp và truyền tải điện năng
*Transformers and power transmission* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được công thức máy biến áp lí tưởng liên hệ điện áp và số vòng dây
- Giải thích được vì sao phải tăng điện áp khi truyền tải điện năng đi xa
- Tính được công suất hao phí và hiệu suất truyền tải

## Máy biến áp

Máy biến áp gồm hai cuộn dây quấn trên lõi sắt. Dòng xoay chiều ở cuộn sơ cấp tạo từ thông biến thiên, cảm ứng sang cuộn thứ cấp. Với máy lí tưởng:

$$\dfrac{U_1}{U_2} = \dfrac{N_1}{N_2} = \dfrac{I_2}{I_1}$$

Cuộn nào nhiều vòng hơn có điện áp lớn hơn. Nếu $N_2 > N_1$ là máy tăng áp, ngược lại là máy hạ áp. Do bảo toàn công suất ($U_1 I_1 = U_2 I_2$), tăng áp thì dòng giảm và ngược lại.

## Vì sao phải tăng áp khi truyền tải

Truyền công suất $P$ trên đường dây điện trở $R$ với điện áp $U$, dòng $I = \dfrac{P}{U\cos\varphi}$ gây hao phí:

$$\Delta P = I^2 R = \dfrac{P^2 R}{U^2\cos^2\varphi}$$

Hao phí tỉ lệ **nghịch với bình phương điện áp**. Vì thế tăng điện áp truyền tải lên $n$ lần thì hao phí giảm $n^2$ lần. Đó là lí do dùng đường dây cao thế (hàng trăm kV) rồi hạ áp bằng máy biến áp trước khi đưa vào nhà.

## Hiệu suất

Hiệu suất truyền tải:

$$H = \dfrac{P - \Delta P}{P} = 1 - \dfrac{\Delta P}{P}$$

Bài toán thường cho H và hỏi phải tăng áp bao nhiêu lần, hoặc ngược lại.

**Lỗi thường gặp:**
- Cho rằng tăng điện áp truyền tải thì hao phí giảm tỉ lệ nghịch với U; thực ra giảm theo bình phương U.
- Nhầm chiều tăng/giảm áp với số vòng: cuộn nhiều vòng có điện áp lớn hơn, không phụ thuộc cuộn nào là sơ cấp.
- Quên rằng máy biến áp chỉ hoạt động với dòng xoay chiều, không dùng được cho dòng một chiều không đổi.

<sub>`lesson.physics.vn-thpt-physics-diendtu.may-bien-ap-truyen-tai-dien-nang`</sub>

---

## Chương VII: Khí lí tưởng

### 1. Thuyết động học phân tử và mô hình khí lí tưởng
*Kinetic molecular theory and the ideal gas model* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Nêu được các nội dung cơ bản của thuyết động học phân tử chất khí
- Giải thích được áp suất chất khí bằng va chạm phân tử lên thành bình
- Liên hệ được nhiệt độ tuyệt đối với động năng tịnh tiến trung bình của phân tử

## Chất khí nhìn từ phân tử

Thuyết động học phân tử coi chất khí gồm vô số phân tử: kích thước rất nhỏ so với khoảng cách giữa chúng, luôn **chuyển động hỗn loạn không ngừng** theo mọi hướng, và **va chạm đàn hồi** với nhau và với thành bình. Giữa các va chạm, phân tử chuyển động thẳng đều vì bỏ qua tương tác — đó là mô hình **khí lí tưởng**.

## Áp suất sinh ra thế nào?

Mỗi phân tử đập vào thành bình truyền cho thành một xung lượng. Vô số va chạm mỗi giây tạo nên một lực trung bình đều đặn — chính là **áp suất**. Thuyết động học cho:

$$p = \tfrac{1}{3} n m_0 \overline{v^2},$$

với $n$ là số phân tử trên đơn vị thể tích, $m_0$ khối lượng một phân tử, $\overline{v^2}$ tốc độ bình phương trung bình. Khí càng đặc, phân tử càng nhanh thì áp suất càng lớn.

## Nhiệt độ chính là 'độ nhanh' của phân tử

So sánh với phương trình khí lí tưởng dẫn tới kết quả sâu sắc: động năng tịnh tiến trung bình của phân tử tỉ lệ thuận với **nhiệt độ tuyệt đối**:

$$\overline{W_d} = \tfrac{3}{2} k T.$$

Vậy nhiệt độ là *thước đo động năng chuyển động nhiệt*. Ở 0 K lí thuyết, chuyển động nhiệt dừng lại. Tốc độ căn quân phương $v = \sqrt{\overline{v^2}} = \sqrt{\dfrac{3kT}{m_0}}$ cho thấy phân tử nhẹ chuyển động nhanh hơn ở cùng nhiệt độ.

**Lỗi thường gặp:**
- Dùng nhiệt độ Celsius trong $\overline{W_d} = \tfrac32 kT$. Sai; công thức đòi hỏi nhiệt độ tuyệt đối, phải đổi sang Kelvin.
- Cho rằng khí nặng có động năng phân tử trung bình lớn hơn ở cùng nhiệt độ. Sai; động năng trung bình chỉ phụ thuộc nhiệt độ, khí nặng chỉ chuyển động chậm hơn.

<sub>`lesson.physics.vn-thpt-physics-conhiet.thuyet-dong-hoc-phan-tu-khi-li-tuong`</sub>

---

### 2. Các định luật chất khí: Boyle, Charles và Gay-Lussac
*Gas laws: Boyle, Charles and Gay-Lussac* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu và vận dụng được định luật Boyle cho quá trình đẳng nhiệt
- Phát biểu và vận dụng được định luật Charles và Gay-Lussac cho quá trình đẳng áp, đẳng tích
- Nhận dạng và vẽ được các đường đẳng nhiệt, đẳng áp, đẳng tích

## Ba quá trình, ba định luật

Giữ cố định một trong ba đại lượng $p, V, T$, ta thu được ba định luật thực nghiệm về chất khí.

## Đẳng nhiệt — định luật Boyle

Giữ $T$ không đổi, nén khí thì áp suất tăng: áp suất tỉ lệ nghịch thể tích:

$$p_1 V_1 = p_2 V_2.$$

Trên hệ trục $(p, V)$, đường đẳng nhiệt là một nhánh hypebol. Đây là nguyên lí của bơm, xi lanh.

## Đẳng áp — định luật Charles

Giữ $p$ không đổi, đun nóng thì khí nở: thể tích tỉ lệ thuận nhiệt độ *tuyệt đối*:

$$\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}.$$

## Đẳng tích — định luật Gay-Lussac

Giữ $V$ không đổi, đun nóng thì áp suất tăng:

$$\dfrac{p_1}{T_1} = \dfrac{p_2}{T_2}.$$

Đó là lí do bình gas, lốp xe để ngoài nắng dễ nổ.

## Điều tối quan trọng: dùng Kelvin

Mọi tỉ lệ với nhiệt độ chỉ đúng khi $T$ tính bằng **Kelvin** ($T = t + 273$). Dùng độ Celsius sẽ sai hoàn toàn vì thang Celsius có gốc tùy tiện. Nhớ quy tắc: chuyển nhanh trắc nghiệm bằng cách lập tỉ số hai trạng thái, đại lượng nào không đổi thì để nguyên.

**Lỗi thường gặp:**
- Dùng nhiệt độ Celsius trong định luật Charles và Gay-Lussac. Sai; các định luật này chỉ đúng với nhiệt độ tuyệt đối (Kelvin).
- Cho rằng nén khí đẳng nhiệt làm nhiệt độ tăng. Trong quá trình đẳng nhiệt, theo định nghĩa nhiệt độ không đổi; nhiệt sinh ra được truyền ra ngoài.

<sub>`lesson.physics.vn-thpt-physics-conhiet.cac-dinh-luat-chat-khi`</sub>

---

### 3. Phương trình trạng thái và phương trình Clapeyron-Mendeleev
*The gas state equation and the ideal gas law* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Thiết lập được phương trình trạng thái của khí lí tưởng từ ba định luật chất khí
- Vận dụng được phương trình Clapeyron-Mendeleev để tính các đại lượng của khối khí
- Tính được khối lượng, số mol và khối lượng riêng của chất khí

## Gộp ba định luật thành một

Kết hợp Boyle, Charles và Gay-Lussac cho **phương trình trạng thái** của một lượng khí xác định:

$$\dfrac{pV}{T} = \text{hằng số} \quad\Rightarrow\quad \dfrac{p_1 V_1}{T_1} = \dfrac{p_2 V_2}{T_2}.$$

Dùng công thức này khi khối khí *không đổi* nhưng cả ba đại lượng cùng thay đổi giữa hai trạng thái.

## Phương trình Clapeyron-Mendeleev

Khi cần liên hệ với *lượng chất*, ta dùng dạng đầy đủ:

$$pV = nRT = \dfrac{m}{M} RT,$$

với $n$ là số mol, $R = 8{,}31$ J/(mol·K), $M$ là khối lượng mol. Phương trình này cho phép tính khối lượng khí, số mol, hoặc khối lượng riêng $\rho = \dfrac{m}{V} = \dfrac{pM}{RT}$ chỉ từ trạng thái hiện tại — không cần trạng thái thứ hai.

## Chọn công thức nào?

- Bài cho *hai trạng thái* của cùng một khối khí (nén, đun, dãn): dùng phương trình trạng thái, lập tỉ số.
- Bài hỏi *khối lượng, số mol, khối lượng riêng* hay có đổi lượng khí: dùng Clapeyron-Mendeleev.

## Lưu ý đơn vị

Trong $pV = nRT$ với $R = 8{,}31$, phải dùng $p$ theo Pa, $V$ theo m$^3$, $T$ theo K. Nếu dùng atm và lít thì đổi $R$ tương ứng. Sai đơn vị là lỗi phổ biến nhất ở dạng bài này.

**Lỗi thường gặp:**
- Áp dụng phương trình trạng thái $\dfrac{p_1V_1}{T_1}=\dfrac{p_2V_2}{T_2}$ khi lượng khí thay đổi (nạp thêm hoặc rò rỉ). Công thức này chỉ đúng khi khối lượng khí không đổi.
- Quên đổi lít sang m$^3$ hoặc Celsius sang Kelvin khi dùng $R = 8{,}31$. Sai đơn vị làm kết quả lệch hàng nghìn lần hoặc sai dấu.

<sub>`lesson.physics.vn-thpt-physics-conhiet.phuong-trinh-trang-thai-clapeyron-mendeleev`</sub>

---

## Chương VIII: Chất rắn và chất lỏng

### 1. Biến dạng của vật rắn và sự nở vì nhiệt
*Deformation of solids and thermal expansion* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được biến dạng đàn hồi của vật rắn và vận dụng định luật Hooke cho biến dạng kéo, nén
- Tính được ứng suất và độ biến dạng tỉ đối của thanh rắn
- Vận dụng được công thức nở dài và nở khối của vật rắn

## Vật rắn cũng 'đàn hồi'

Dưới lực kéo hoặc nén vừa phải, vật rắn biến dạng rồi trở lại hình dạng cũ khi bỏ lực — đó là **biến dạng đàn hồi**. Đại lượng đo mức tác dụng lực trên tiết diện là **ứng suất** $\sigma = \dfrac{F}{S}$. Định luật Hooke cho biến dạng phát biểu: độ biến dạng tỉ đối tỉ lệ với ứng suất:

$$\dfrac{\Delta l}{l_0} = \dfrac{\sigma}{E} = \dfrac{F}{ES},$$

trong đó $E$ (suất Young) đặc trưng cho vật liệu — thép có $E$ rất lớn nên khó biến dạng. Vượt quá giới hạn bền, vật đứt gãy.

## Sự nở vì nhiệt

Đun nóng, các nguyên tử dao động mạnh hơn và khoảng cách trung bình tăng, làm vật **nở ra**. Nở dài:

$$\Delta l = \alpha l_0 \Delta t,$$

với $\alpha$ là hệ số nở dài (đơn vị K$^{-1}$). Nở khối có hệ số $\beta \approx 3\alpha$: $\Delta V = \beta V_0 \Delta t$.

## Vì sao phải quan tâm?

Đường ray, cầu thép phải chừa khe hở giãn nở; nếu không, ngày nóng thanh ray sẽ cong vênh. Bê tông cốt thép bền vì thép và bê tông có hệ số nở gần bằng nhau. Nhiệt kế, rơ-le lưỡng kim đều dựa trên nở vì nhiệt.

## Kết nối

Khi một thanh bị *giữ chặt hai đầu* rồi đun nóng, nó không nở được nên sinh ứng suất nhiệt rất lớn — kết hợp cả hai công thức trên để tính lực nén.

**Lỗi thường gặp:**
- Nhầm hệ số nở khối bằng hệ số nở dài. Với vật đẳng hướng, hệ số nở khối $\beta \approx 3\alpha$, không bằng $\alpha$.
- Cho rằng thanh bị giữ chặt hai đầu vẫn nở dài bình thường. Sai; khi bị cản, thanh không giãn được mà sinh ứng suất nhiệt lớn.

<sub>`lesson.physics.vn-thpt-physics-conhiet.bien-dang-vat-ran-su-no-vi-nhiet`</sub>

---

### 2. Chất lỏng: lực căng bề mặt, mao dẫn và độ ẩm không khí
*Liquids: surface tension, capillarity and air humidity* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Nêu được nguyên nhân và biểu thức của lực căng bề mặt chất lỏng
- Giải thích được hiện tượng mao dẫn và tính độ dâng của chất lỏng trong ống
- Phân biệt được độ ẩm tuyệt đối, độ ẩm cực đại và độ ẩm tỉ đối của không khí

## Vì sao giọt nước co tròn?

Các phân tử ở mặt thoáng bị phân tử bên trong hút vào, tạo nên **lực căng bề mặt** khiến mặt thoáng có xu hướng co nhỏ nhất — đó là lí do giọt nước, bong bóng xà phòng có dạng cầu. Lực căng tác dụng lên đường giới hạn dài $l$:

$$f = \sigma l,$$

với $\sigma$ là hệ số căng bề mặt. Nhờ nó, côn trùng đi được trên mặt nước, kim khâu nổi được.

## Mao dẫn

Trong ống rất nhỏ, chất lỏng dính ướt (như nước trong ống thủy tinh) **dâng lên**, chất không dính ướt (như thủy ngân) **hạ xuống**:

$$h = \dfrac{4\sigma}{\rho g d}.$$

Ống càng nhỏ, nước dâng càng cao. Mao dẫn giúp nước thấm lên thân cây, dầu thấm lên bấc đèn, nước ngấm qua giấy.

## Độ ẩm không khí

Không khí chứa hơi nước. **Độ ẩm tuyệt đối** $a$ là khối lượng hơi nước trong 1 m$^3$ không khí. **Độ ẩm cực đại** $A$ là giá trị $a$ khi hơi nước bão hòa ở nhiệt độ đó. **Độ ẩm tỉ đối**:

$$f = \dfrac{a}{A}\cdot 100\%.$$

Độ ẩm tỉ đối càng cao, mồ hôi càng khó bay hơi nên ta thấy oi bức. Khi không khí lạnh đi tới điểm sương, hơi nước ngưng tụ thành sương, mây, mưa.

**Lỗi thường gặp:**
- Nhầm độ ẩm cực đại với độ ẩm tuyệt đối. Độ ẩm cực đại là giá trị bão hòa; độ ẩm tuyệt đối mới là lượng hơi nước thực có, thường nhỏ hơn.
- Cho rằng lực căng bề mặt phụ thuộc diện tích mặt thoáng. Sai; nó tỉ lệ với độ dài đường giới hạn $l$ chứ không phải diện tích.

<sub>`lesson.physics.vn-thpt-physics-conhiet.chat-long-cang-be-mat-do-am`</sub>

---

## Chương VIII: Dao động và sóng điện từ

### 1. Mạch dao động LC và sóng điện từ
*LC oscillator and electromagnetic waves* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Viết được biểu thức điện tích, dòng điện trong mạch dao động LC và công thức chu kì Thomson
- Vận dụng được định luật bảo toàn năng lượng điện từ trong mạch LC
- Tính được bước sóng điện từ mà mạch thu, phát

## Dao động điện từ tự do

Nối tụ đã tích điện với cuộn cảm, tụ phóng điện qua cuộn cảm rồi cuộn cảm lại nạp ngược tụ, tạo dao động điện từ. Điện tích trên tụ biến thiên điều hoà:

$$q = Q_0\cos(\omega t + \varphi), \qquad \omega = \dfrac{1}{\sqrt{LC}}$$

nên chu kì riêng (công thức **Thomson**) là $T = 2\pi\sqrt{LC}$. Dòng điện $i = q'$ sớm pha $\pi/2$ so với $q$, với $I_0 = \omega Q_0$.

## Tương tự cơ - điện

Mạch LC giống hệt con lắc lò xo: $q$ ứng với li độ $x$, $i$ ứng với vận tốc $v$, $\dfrac{1}{C}$ ứng với $k$, $L$ ứng với $m$. Năng lượng chuyển hoá giữa **điện trường** trong tụ $W_C = \dfrac{q^2}{2C}$ và **từ trường** trong cuộn cảm $W_L = \dfrac{1}{2}Li^2$, tổng bảo toàn:

$$W = \dfrac{Q_0^2}{2C} = \dfrac{1}{2}LI_0^2$$

## Sóng điện từ

Mạch LC hở (ăng-ten) phát ra sóng điện từ lan truyền với tốc độ ánh sáng $c = 3\cdot10^8$ m/s. Bước sóng mạch thu, phát:

$$\lambda = cT = 2\pi c\sqrt{LC}$$

Thay đổi C (tụ xoay) làm đổi bước sóng - đó là cách chọn sóng của radio. Thang sóng điện từ từ sóng vô tuyến, hồng ngoại, ánh sáng nhìn thấy, tử ngoại, tia X đến tia gamma, sắp xếp theo bước sóng giảm dần.

**Lỗi thường gặp:**
- Nhầm dòng i cùng pha với điện tích q; thực ra i sớm pha π/2 so với q (như v với x).
- Quên căn bậc hai trong công thức Thomson, tính T tỉ lệ với LC thay vì với căn của LC.
- Lẫn năng lượng điện trường với năng lượng từ trường: khi q cực đại thì i = 0 và ngược lại.

<sub>`lesson.physics.vn-thpt-physics-diendtu.mach-dao-dong-lc-song-dien-tu`</sub>

---

## Chương X: Lượng tử ánh sáng

### 1. Hiện tượng quang điện và phương trình Einstein
*Photoelectric effect and Einstein's equation* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Nêu được nội dung thuyết lượng tử ánh sáng và khái niệm photon
- Phát biểu và vận dụng được phương trình Einstein về hiện tượng quang điện
- Tính được giới hạn quang điện, động năng ban đầu cực đại và hiệu điện thế hãm

## Vì sao cần thuyết photon

Hiện tượng quang điện: chiếu ánh sáng thích hợp vào kim loại thì electron bị bứt ra. Thí nghiệm cho thấy có **giới hạn quang điện** - ánh sáng bước sóng dài (dù rất mạnh) cũng không bứt được electron, còn ánh sáng bước sóng ngắn (dù rất yếu) lại bứt được ngay. Sóng cổ điển không giải thích nổi điều này.

Einstein đề xuất: ánh sáng gồm các hạt **photon**, mỗi photon mang năng lượng

$$\varepsilon = hf = \dfrac{hc}{\lambda}$$

Mỗi electron hấp thụ trọn một photon. Nếu năng lượng photon nhỏ hơn công thoát $A$ thì không bứt được, bất kể cường độ.

## Phương trình Einstein

Năng lượng photon dùng để thắng công thoát và cấp động năng ban đầu cho electron:

$$hf = A + \dfrac{1}{2}mv_{0\max}^2$$

Giới hạn quang điện: $\lambda_0 = \dfrac{hc}{A}$. Điều kiện xảy ra quang điện là $\lambda \le \lambda_0$.

## Hiệu điện thế hãm

Để đo động năng ban đầu cực đại, ta đặt hiệu điện thế hãm $U_h$ chặn dòng quang điện:

$$eU_h = \dfrac{1}{2}mv_{0\max}^2$$

Cường độ sáng chỉ quyết định **số** electron bứt ra (dòng bão hoà), còn động năng của chúng chỉ phụ thuộc tần số ánh sáng.

**Lỗi thường gặp:**
- Cho rằng tăng cường độ ánh sáng thì electron bứt ra có động năng lớn hơn; cường độ chỉ tăng số electron, động năng phụ thuộc tần số.
- Dùng ánh sáng bước sóng lớn hơn giới hạn quang điện vẫn tính ra quang điện; điều kiện là λ ≤ λ₀.
- Nhầm công thoát A với năng lượng photon; A là ngưỡng của kim loại, ε là năng lượng một hạt ánh sáng.

<sub>`lesson.physics.vn-thpt-physics-diendtu.hien-tuong-quang-dien-einstein`</sub>

---

### 2. Mẫu nguyên tử Bohr và quang phổ hiđrô
*Bohr model and hydrogen spectrum* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Phát biểu được hai tiên đề Bohr về trạng thái dừng và bức xạ, hấp thụ
- Tính được bán kính quỹ đạo và năng lượng các mức trong nguyên tử hiđrô
- Xác định được bước sóng các vạch trong quang phổ hiđrô

## Hai tiên đề Bohr

Nguyên tử hiđrô phát quang phổ **vạch** rời rạc chứ không liên tục, điều mà mô hình cổ điển không giải thích được. Bohr đưa ra hai tiên đề:

1. **Trạng thái dừng**: nguyên tử chỉ tồn tại trong những trạng thái có năng lượng xác định $E_n$, ở đó electron chuyển động trên quỹ đạo dừng mà **không bức xạ**. Bán kính quỹ đạo $r_n = n^2 r_0$ với $r_0 = 5{,}3\cdot10^{-11}$ m.
2. **Bức xạ - hấp thụ**: khi chuyển từ mức cao $E_m$ về mức thấp $E_n$, nguyên tử phát một photon:

$$hf = E_m - E_n$$

ngược lại hấp thụ photon để nhảy lên mức cao.

## Mức năng lượng hiđrô

Năng lượng các mức của hiđrô lượng tử hoá:

$$E_n = -\dfrac{13{,}6}{n^2}\ \text{(eV)}$$

Mức $n=1$ là cơ bản (bền nhất), $n\to\infty$ là ion hoá ($E=0$).

## Quang phổ vạch

Các vạch phát xạ xếp thành dãy: Lyman (về $n=1$, tử ngoại), Balmer (về $n=2$, có vạch nhìn thấy), Paschen (về $n=3$, hồng ngoại). Bước sóng mỗi vạch tính từ $\dfrac{hc}{\lambda} = E_m - E_n$. Số vạch tối đa khi electron từ mức $n$ về thấp hơn là $\dfrac{n(n-1)}{2}$.

**Lỗi thường gặp:**
- Quên dấu âm của mức năng lượng, tính hiệu năng lượng ra âm rồi lấy bước sóng âm.
- Nhầm bán kính quỹ đạo r_n tỉ lệ với n; thực ra r_n tỉ lệ với n².
- Cho rằng electron ở trạng thái dừng vẫn bức xạ liên tục; theo tiên đề Bohr, ở trạng thái dừng nguyên tử không bức xạ.

<sub>`lesson.physics.vn-thpt-physics-diendtu.mau-nguyen-tu-bohr-quang-pho-hidro`</sub>

---

## Chương XI: Hạt nhân nguyên tử

### 1. Cấu tạo hạt nhân, độ hụt khối và năng lượng liên kết
*Nuclear structure, mass defect and binding energy* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Nêu được cấu tạo hạt nhân và kí hiệu hạt nhân
- Tính được độ hụt khối và năng lượng liên kết của hạt nhân
- So sánh được độ bền vững của các hạt nhân qua năng lượng liên kết riêng

## Hạt nhân được cấu tạo thế nào

Hạt nhân gồm các **nuclôn**: $Z$ proton (mang điện dương) và $N = A - Z$ neutron (trung hoà), kí hiệu $^{A}_{Z}X$ với $A$ là số khối. Bán kính hạt nhân $R = 1{,}2\cdot10^{-15}A^{1/3}$ m rất nhỏ, nên khối lượng riêng hạt nhân cực lớn.

## Độ hụt khối - điều kì lạ

Đo chính xác thấy khối lượng hạt nhân **nhỏ hơn** tổng khối lượng các nuclôn tạo thành nó. Phần thiếu gọi là **độ hụt khối**:

$$\Delta m = Zm_p + (A-Z)m_n - m_{hn}$$

## Năng lượng liên kết

Theo hệ thức Einstein $E = mc^2$, phần khối lượng hụt đi đã biến thành **năng lượng liên kết** giữ các nuclôn lại với nhau:

$$W_{lk} = \Delta m\, c^2$$

Đây cũng là năng lượng cần cung cấp để phá vỡ hạt nhân thành các nuclôn riêng lẻ. Để so sánh độ bền giữa các hạt nhân khác nhau, ta dùng **năng lượng liên kết riêng** $W_{lk}/A$: hạt nhân có $W_{lk}/A$ càng lớn càng bền. Các hạt nhân số khối trung bình (quanh sắt) bền nhất, giải thích vì sao cả phân hạch (hạt nặng tách ra) lẫn nhiệt hạch (hạt nhẹ kết hợp) đều toả năng lượng.

**Lỗi thường gặp:**
- Cho rằng khối lượng hạt nhân bằng tổng khối lượng các nuclôn; thực ra nhỏ hơn một lượng là độ hụt khối.
- Dùng năng lượng liên kết (tổng) để so sánh độ bền; phải dùng năng lượng liên kết riêng W_lk/A.
- Quên đổi đơn vị u sang MeV/c² (nhân 931,5) khi tính năng lượng.

<sub>`lesson.physics.vn-thpt-physics-diendtu.cau-tao-hat-nhan-nang-luong-lien-ket`</sub>

---

### 2. Phóng xạ, phản ứng hạt nhân, phân hạch và nhiệt hạch
*Radioactivity, nuclear reactions, fission and fusion* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · chuyen-sau

**Mục tiêu:**
- Phát biểu và vận dụng được định luật phóng xạ để tính số hạt và độ phóng xạ còn lại
- Viết được phương trình phản ứng hạt nhân dựa trên các định luật bảo toàn
- Tính được năng lượng toả ra hoặc thu vào của phản ứng, phân biệt phân hạch và nhiệt hạch

## Định luật phóng xạ

Hạt nhân không bền tự phân rã một cách ngẫu nhiên, nhưng số lượng lớn tuân theo quy luật thống kê. Sau mỗi **chu kì bán rã** $T$, số hạt nhân còn lại giảm một nửa:

$$N = N_0\, 2^{-t/T} = N_0 e^{-\lambda t}, \qquad \lambda = \dfrac{\ln 2}{T}$$

**Độ phóng xạ** $H = \lambda N$ (số phân rã mỗi giây, đơn vị Bq) cũng giảm theo cùng quy luật. Nhờ đó, đo độ phóng xạ còn lại (ví dụ $^{14}C$) cho phép xác định tuổi cổ vật.

## Phản ứng hạt nhân và các định luật bảo toàn

Phản ứng $A + B \to C + D$ tuân theo **bảo toàn điện tích** (tổng Z) và **bảo toàn số khối** (tổng A), cùng bảo toàn động lượng và năng lượng toàn phần. Nhờ đó viết được phương trình và tìm hạt chưa biết. Các loại phóng xạ: $\alpha$ (phát $^4_2He$), $\beta^-$ (phát electron), $\beta^+$ (phát pôzitron), $\gamma$ (phát photon năng lượng cao).

## Năng lượng, phân hạch và nhiệt hạch

Năng lượng phản ứng: $Q = (m_{truoc} - m_{sau})c^2$. Nếu $Q>0$ phản ứng **toả** năng lượng.

- **Phân hạch**: hạt nhân nặng (U-235) hấp thụ neutron rồi vỡ thành hai mảnh, toả năng lượng và phát thêm neutron gây phản ứng dây chuyền - cơ sở của nhà máy điện hạt nhân.
- **Nhiệt hạch**: các hạt nhân nhẹ (như hiđrô) kết hợp thành hạt nặng hơn, toả năng lượng lớn hơn nhiều trên mỗi nuclôn - nguồn năng lượng của Mặt Trời.

**Lỗi thường gặp:**
- Cho rằng sau hai chu kì bán rã thì chất phóng xạ hết; mỗi chu kì chỉ giảm một nửa, không bao giờ về đúng 0.
- Nhầm số hạt đã phân rã với số hạt còn lại; số đã phân rã là N₀ − N = N₀(1 − 2^(−t/T)).
- Không kiểm tra bảo toàn số khối A và điện tích Z khi viết phương trình phản ứng, dẫn tới xác định sai hạt tạo thành.

<sub>`lesson.physics.vn-thpt-physics-diendtu.phong-xa-phan-ung-hat-nhan`</sub>

---

## Chương XII: Thuyết tương đối hẹp

### 1. Thuyết tương đối hẹp
*Special relativity* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · chuyen-sau

**Mục tiêu:**
- Phát biểu được hai tiên đề của thuyết tương đối hẹp Einstein
- Vận dụng được công thức co độ dài và giãn thời gian
- Tính được năng lượng nghỉ, năng lượng toàn phần theo hệ thức Einstein

## Hai tiên đề

Vật lí cổ điển giả định thời gian và không gian tuyệt đối, nhưng điều đó mâu thuẫn với việc tốc độ ánh sáng đo được luôn bằng $c$. Einstein đề ra hai tiên đề:

1. Các định luật vật lí như nhau trong mọi hệ quy chiếu quán tính.
2. Tốc độ ánh sáng trong chân không bằng $c$ với **mọi** quan sát viên, không phụ thuộc chuyển động của nguồn hay người quan sát.

## Co độ dài và giãn thời gian

Từ hai tiên đề suy ra các hệ quả kì lạ với hệ số Lorentz $\gamma = \dfrac{1}{\sqrt{1 - v^2/c^2}} \ge 1$:

$$\Delta t = \gamma\Delta t_0 \quad(\text{thời gian giãn}), \qquad l = \dfrac{l_0}{\gamma} \quad(\text{độ dài co})$$

Đồng hồ chuyển động chạy chậm hơn, thước chuyển động ngắn lại theo phương chuyển động. Các hiệu ứng chỉ đáng kể khi $v$ gần $c$; với vận tốc thường ngày $\gamma \approx 1$ nên trở về cơ học Newton.

## Khối lượng - năng lượng

Hệ thức nổi tiếng nhất:

$$E = mc^2 = \gamma m_0 c^2$$

Ngay cả khi đứng yên, vật đã có **năng lượng nghỉ** $E_0 = m_0 c^2$. Động năng tương đối tính $W_d = (\gamma - 1)m_0 c^2$. Chính hệ thức này giải thích năng lượng khổng lồ toả ra trong phản ứng hạt nhân: một lượng khối lượng rất nhỏ biến thành năng lượng rất lớn.

**Lỗi thường gặp:**
- Áp dụng công thức cộng vận tốc Galilê khi vận tốc gần c; phải dùng công thức cộng vận tốc tương đối tính.
- Cho rằng năng lượng nghỉ bằng 0 khi vật đứng yên; thực ra E₀ = m₀c² khác 0.
- Nhầm chiều của hiệu ứng: đồng hồ chuyển động chạy chậm và thước chuyển động ngắn lại, không phải ngược lại.

<sub>`lesson.physics.vn-thpt-physics-diendtu.thuyet-tuong-doi-hep`</sub>

---

## Unit 0: Kĩ năng thực nghiệm và xử lí dữ liệu (AP/IB/A-Level Practical Skills)

### 1. Đại lượng vật lí, hệ đơn vị SI và phân tích thứ nguyên
*Physical quantities, SI units and dimensional analysis* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Xác định được thứ nguyên của một đại lượng vật lí theo bảy đại lượng cơ bản SI
- Vận dụng được phân tích thứ nguyên để kiểm tra tính đúng đắn của một công thức
- Giải thích được vì sao phân tích thứ nguyên không xác định được hằng số không thứ nguyên

## Một con số trần trụi thì không nói lên điều gì

Câu "khối lượng bằng 5" không có nội dung vật lí: 5 gam hay 5 tấn là hai thế giới khác nhau. Mọi đại lượng vật lí đều gồm **giá trị số** nhân với **đơn vị**. Hệ SI chọn bảy đại lượng cơ bản và quy tất cả đại lượng còn lại về chúng.

## Thứ nguyên: bộ xương của công thức

Ký hiệu thứ nguyên bằng ngoặc vuông. Với vận tốc: $[v] = \mathsf{L}\,\mathsf{T}^{-1}$; với lực, từ $F = ma$ suy ra $[F] = \mathsf{M}\,\mathsf{L}\,\mathsf{T}^{-2}$; với năng lượng $[E] = \mathsf{M}\,\mathsf{L}^{2}\,\mathsf{T}^{-2}$.

Hai nguyên tắc dùng suốt đời:

1. **Chỉ cộng được các đại lượng cùng thứ nguyên.** Viết $v = v_0 + at^2$ là sai ngay lập tức vì $\mathsf{L}\mathsf{T}^{-1} \neq \mathsf{L}\mathsf{T}^{0}$.
2. **Hai vế của một phương trình phải cùng thứ nguyên.**

## Đoán được cả dạng công thức

Giả sử chu kì con lắc đơn phụ thuộc $l$, $g$, $m$: $T = k\, l^{a} g^{b} m^{c}$. Cân bằng thứ nguyên cho $a = 1/2$, $b = -1/2$, $c = 0$, tức

$$T = k\sqrt{\dfrac{l}{g}}$$

Phương pháp trả lời được cả câu hỏi thú vị: chu kì **không phụ thuộc khối lượng**. Đó chính là tinh thần của định lí Buckingham Pi.

## Ranh giới của phương pháp

Phân tích thứ nguyên **không** cho biết hằng số $k$ (ở đây $k = 2\pi$), vì hằng số không thứ nguyên tàng hình trước phép cân bằng. Nó cũng bó tay khi bài toán có nhiều hơn một tổ hợp không thứ nguyên. Vì vậy hãy dùng nó như một bộ lọc sai, chứ không phải một máy sinh công thức.

**Lỗi thường gặp:**
- Coi "đơn vị đúng" là "công thức đúng". Thứ nguyên chỉ loại được công thức sai, không chứng minh được công thức đúng, vì mọi hằng số không thứ nguyên như $2\pi$ hay $1/2$ đều lọt qua phép kiểm tra.
- Đặt đại lượng có thứ nguyên vào trong hàm sin, log, exp. Khai triển chuỗi $e^{x} = 1 + x + x^{2}/2 + \dots$ đòi hỏi cộng $x$ với $x^{2}$, chỉ hợp lệ khi $x$ không thứ nguyên.
- Nhầm thứ nguyên với đơn vị: đổi từ km/h sang m/s là đổi đơn vị, thứ nguyên vẫn là $\mathsf{L}\mathsf{T}^{-1}$ và không hề thay đổi.

<sub>`lesson.physics.intl-phuong-phap.dai-luong-don-vi-si-thu-nguyen`</sub>

---

### 2. Chữ số có nghĩa, sai số và độ không đảm bảo đo
*Significant figures, errors and measurement uncertainty* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được sai số hệ thống và sai số ngẫu nhiên qua biểu hiện trên dữ liệu
- Tính được độ không đảm bảo tương đối và lan truyền sai số qua tích, thương, lũy thừa
- Trình bày được kết quả đo với số chữ số có nghĩa phù hợp với độ không đảm bảo

## Không có phép đo nào cho một con số duy nhất

Kết quả đo phải viết dạng $x = (\bar{x} \pm \Delta x)$ kèm đơn vị. Con số $\Delta x$ không phải "lỗi của người làm", nó là **khoảng tin cậy** của phép đo.

## Hai loại sai lệch có bản chất khác hẳn nhau

- **Hệ thống**: cân chưa chỉnh về 0, thước bị co, luôn đọc lệch một phía. Trên đồ thị, sai số hệ thống làm đường thẳng **dịch song song** (sai hệ số chặn) hoặc **đổi độ dốc**, nhưng các điểm vẫn thẳng hàng đẹp.
- **Ngẫu nhiên**: bấm đồng hồ sớm muộn. Trên đồ thị, các điểm **tản mát hai phía** đường chuẩn.

Dấu hiệu này là câu hỏi ruột của A-Level và IB: dữ liệu rất tuyến tính nhưng lệch gốc nghĩa là chính xác cao (precise) mà kém đúng (accurate).

## Lan truyền sai số

Quy tắc thực dụng dùng ở AP, IB, A-Level:

- Cộng, trừ: **cộng độ không đảm bảo tuyệt đối**, $\Delta(a\pm b) = \Delta a + \Delta b$.
- Nhân, chia: **cộng độ không đảm bảo tương đối**, $\dfrac{\Delta y}{y} = \dfrac{\Delta a}{a} + \dfrac{\Delta b}{b}$.
- Lũy thừa $y = a^{n}$: $\dfrac{\Delta y}{y} = |n|\dfrac{\Delta a}{a}$.

Hệ quả quan trọng: đại lượng nào bị nâng lên lũy thừa cao thì phải đo cẩn thận nhất. Trong $g = 4\pi^{2}l/T^{2}$, sai 1% ở $T$ gây 2% ở $g$.

## Viết kết quả cho đúng

Làm tròn $\Delta x$ về **một chữ số có nghĩa** (đôi khi hai), rồi làm tròn $\bar{x}$ tới cùng hàng thập phân. Viết $g = 9{,}81 \pm 0{,}3\ \mathrm{m/s^{2}}$ là mâu thuẫn nội tại: đã không chắc ở hàng phần mười thì ghi hàng phần trăm để làm gì.

**Lỗi thường gặp:**
- Nghĩ rằng đo lại nhiều lần sẽ khử được mọi sai số. Trung bình chỉ triệt tiêu phần ngẫu nhiên; sai số hệ thống lặp lại y hệt ở mọi lần đo nên trung bình vẫn lệch đúng bằng chừng ấy.
- Cộng độ không đảm bảo tuyệt đối khi nhân chia. Nếu $y=ab$ thì $\Delta y$ phụ thuộc cả $a$ lẫn $b$ theo $\Delta y = a\Delta b + b\Delta a$; chỉ khi chia hai vế cho $y=ab$ mới có quy tắc cộng phần trăm gọn gàng.
- Giữ nguyên toàn bộ chữ số máy tính hiện ra, ví dụ $g = 9{,}8617283$. Số chữ số có nghĩa của kết quả không được vượt quá số chữ số có nghĩa của dữ liệu thô kém chính xác nhất.

<sub>`lesson.physics.intl-phuong-phap.chu-so-co-nghia-va-sai-so`</sub>

---

### 3. Vẽ đồ thị và tuyến tính hoá dữ liệu thực nghiệm
*Graphing and linearisation of experimental data* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Biến đổi được một quan hệ phi tuyến về dạng đường thẳng $y = mx + c$
- Xác định được đại lượng vật lí từ độ dốc và hệ số chặn của đồ thị
- Phân tích được ý nghĩa của hệ số chặn khác 0 ngoài dự đoán lí thuyết

## Vì sao luôn cố kéo về đường thẳng

Mắt người phát hiện được một điểm lệch khỏi **đường thẳng** rất nhạy, nhưng gần như bất lực trước một đường cong. Vì vậy AP, IB và A-Level đều yêu cầu học sinh biến quan hệ lí thuyết về dạng $y = mx + c$ trước khi vẽ.

## Công thức làm việc

Giả sử lí thuyết cho $T = 2\pi\sqrt{l/g}$. Bình phương hai vế:

$$T^{2} = \frac{4\pi^{2}}{g}\, l$$

Vẽ $T^{2}$ theo $l$ thì đây là đường thẳng qua gốc với độ dốc $m = 4\pi^{2}/g$, suy ra $g = 4\pi^{2}/m$. So với việc đo một cặp $(l,T)$ rồi thay số, cách này dùng toàn bộ dữ liệu và tự động lộ ra sai số hệ thống.

Bảng chuyển đổi hay dùng:

| Quan hệ lí thuyết | Vẽ trục tung | Vẽ trục hoành |
|---|---|---|
| $v^{2} = v_0^{2} + 2as$ | $v^{2}$ | $s$ |
| $y = kx^{n}$ (chưa biết $n$) | $\ln y$ | $\ln x$ |
| $I = I_0 e^{-\mu x}$ | $\ln I$ | $x$ |
| $F = Gm_1m_2/r^{2}$ | $F$ | $1/r^{2}$ |

Với đồ thị log-log, độ dốc chính là số mũ $n$ — đó là cách duy nhất ở bậc phổ thông để **đo** một số mũ chưa biết.

## Hệ số chặn nói điều gì

Nếu lí thuyết bảo đường thẳng qua gốc mà thực nghiệm cho $c \neq 0$ rõ rệt, đừng ép nó qua gốc. Hệ số chặn khác 0 thường là dấu vân tay của một **sai số hệ thống**: thước đo chiều dài con lắc bỏ sót bán kính quả nặng, cân chưa trừ bì, nhiệt kế lệch không. Đọc được thông tin đó mới là mục đích thật của việc vẽ đồ thị.

**Lỗi thường gặp:**
- Lấy độ dốc bằng cách chia tọa độ của một điểm dữ liệu, ví dụ $m = y_1/x_1$. Cách đó chỉ đúng khi đường thẳng chắc chắn qua gốc; nếu có hệ số chặn thì kết quả sai và ta mất luôn thông tin về sai số hệ thống.
- Quên đơn vị của độ dốc. Độ dốc của đồ thị $T^{2}$ theo $l$ có đơn vị $\mathrm{s^{2}/m}$, nếu ghi nhầm là s/m thì mọi phép suy ra $g$ đều lệch thứ nguyên.
- Nối các điểm dữ liệu thành đường gấp khúc. Mỗi điểm đều mang sai số ngẫu nhiên, nối chúng lại là tin vào nhiễu; phải vẽ một đường thẳng (hoặc đường trơn) khớp tốt nhất qua đám điểm.

<sub>`lesson.physics.intl-phuong-phap.do-thi-va-tuyen-tinh-hoa`</sub>

---

## Unit 10: Thermal Physics (AP Physics 2 Unit 9 / IB B.1-B.4 / CIE 9702 Topics 14-16)

### 1. Nhiệt độ, cân bằng nhiệt và thang nhiệt độ tuyệt đối
*Temperature, thermal equilibrium and the absolute scale* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được nhiệt độ, nhiệt lượng và nội năng về mặt khái niệm
- Giải thích được ý nghĩa vật lí của độ không tuyệt đối và thang Kelvin
- Vận dụng được phương trình cân bằng nhiệt cho hệ cô lập nhiều vật

## Ba khái niệm luôn bị trộn lẫn

- **Nhiệt độ** là đại lượng cường tính, đo mức độ chuyển động nhiệt trung bình của **một** phân tử. Nó quyết định **chiều** truyền nhiệt.
- **Nội năng** là đại lượng quảng tính, tổng động năng và thế năng của **tất cả** phân tử trong vật.
- **Nhiệt lượng** là năng lượng **đang được truyền** do chênh lệch nhiệt độ; nói "vật chứa nhiệt lượng" là sai, vật chứa nội năng.

Một cốc nước sôi có nhiệt độ cao hơn một bể bơi ấm, nhưng bể bơi có nội năng lớn hơn nhiều lần.

## Cân bằng nhiệt và nguyên lí thứ không

Hai vật tiếp xúc nhiệt trao đổi năng lượng cho tới khi cùng nhiệt độ. Nguyên lí thứ không nói: nếu $A$ cân bằng nhiệt với $C$ và $B$ cũng cân bằng nhiệt với $C$, thì $A$ cân bằng nhiệt với $B$. Nghe hiển nhiên, nhưng chính nó cho phép tồn tại **nhiệt kế**: vật $C$ đóng vai trò thiết bị so sánh chung.

## Vì sao cần thang Kelvin

Đồ thị áp suất theo nhiệt độ của mọi khí loãng, khi ngoại suy về $P = 0$, đều cắt trục nhiệt độ tại đúng $-273{,}15$ độ C bất kể loại khí. Điểm hội tụ đó không thể là ngẫu nhiên: nó là điểm không tự nhiên của thang nhiệt độ.

$$T(\mathrm{K}) = t(^{\circ}\mathrm{C}) + 273{,}15$$

Độ chia hai thang bằng nhau nên $\Delta T = \Delta t$. Nhưng mọi công thức có **tỉ số** nhiệt độ (khí lí tưởng, hiệu suất Carnot, tốc độ căn quân phương) bắt buộc dùng Kelvin: nói "$40$ độ C nóng gấp đôi $20$ độ C" là vô nghĩa, còn $313$ K so với $293$ K chỉ hơn nhau 7 phần trăm.

## Phương trình cân bằng nhiệt

Trong hệ cô lập, $\sum Q = 0$, tức tổng nhiệt lượng thu vào bằng tổng nhiệt lượng toả ra:

$$Q_{\text{thu}} = Q_{\text{toả}}$$

Quy ước dấu: viết $Q = mc(t_{\text{sau}} - t_{\text{trước}})$ cho mọi vật rồi cho tổng bằng 0, cách này tự động xử lí dấu và tránh phải đoán vật nào nóng lên.

**Lỗi thường gặp:**
- Nói "vật chứa nhiều nhiệt lượng". Nhiệt lượng là năng lượng đang truyền qua ranh giới do chênh lệch nhiệt độ, không phải thứ tích trữ trong vật; cái vật chứa là nội năng.
- Dùng độ C trong công thức khí lí tưởng hoặc hiệu suất Carnot. Những công thức đó chứa tỉ số nhiệt độ nên phải dùng thang tuyệt đối; dùng độ C có thể cho cả kết quả âm vô nghĩa.
- Quên nhiệt lượng kế hoặc bình chứa trong phương trình cân bằng nhiệt. Bình cũng thay đổi nhiệt độ nên cũng trao đổi nhiệt; bỏ qua nó khiến nhiệt độ cân bằng tính ra cao hơn thực tế.

<sub>`lesson.physics.nhiet-hoc-intl.nhiet-do-va-can-bang-nhiet`</sub>

---

### 2. Nhiệt dung riêng, nhiệt ẩn và quá trình chuyển thể
*Specific heat capacity, latent heat and phase changes* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Tính được nhiệt lượng trong quá trình có và không có chuyển thể
- Giải thích được vì sao nhiệt độ không đổi trong suốt quá trình chuyển thể
- Phân tích được đồ thị nhiệt độ - thời gian khi đun một chất qua nhiều pha

## Hai loại nhiệt lượng, hai công thức

$$Q = mc\Delta T \quad(\text{đổi nhiệt độ}), \qquad Q = mL \quad(\text{đổi pha})$$

Công thức thứ nhất không có mặt khi vật đang chuyển thể; công thức thứ hai không có $\Delta T$ vì nhiệt độ đứng yên.

## Vì sao nhiệt độ đứng yên khi đang sôi

Nhiệt độ đo động năng trung bình. Trong quá trình chuyển thể, năng lượng cấp vào được dùng để **phá vỡ liên kết** giữa các phân tử, tức làm tăng thế năng chứ không tăng động năng. Vì thế nhiệt kế đứng yên trong khi năng lượng vẫn ào ạt đi vào.

Con số ấn tượng: nhiệt hoá hơi của nước là $2{,}26\times10^{6}$ J/kg, lớn gấp hơn 5 lần nhiệt lượng cần để đun cùng khối lượng nước từ 0 lên 100 độ C ($4{,}2\times10^{5}$ J/kg). Đây là lí do nồi cạn nước rất lâu, và cũng là lí do đổ mồ hôi làm mát cơ thể hiệu quả đến vậy.

Nhiệt hoá hơi luôn lớn hơn nhiệt nóng chảy đối với cùng một chất, vì khi hoá hơi phải tách hẳn phân tử ra xa, còn khi nóng chảy chúng vẫn kề nhau.

## Đọc đồ thị nhiệt độ - thời gian

Đun đá từ $-20$ độ C với công suất không đổi, đồ thị gồm năm đoạn:

1. Đá nóng lên: dốc, độ dốc $= P/(mc_{\text{đá}})$.
2. Đá tan ở 0 độ C: **nằm ngang**, dài $= mL_f/P$.
3. Nước nóng lên: dốc thoải hơn vì $c_{\text{nước}} > c_{\text{đá}}$.
4. Nước sôi ở 100 độ C: nằm ngang và rất dài.
5. Hơi nóng lên: dốc trở lại.

Từ đồ thị này đọc được cả $c$ (qua độ dốc) lẫn $L$ (qua chiều dài đoạn ngang) — dạng câu hỏi ruột của IB và A-Level.

## Vì sao nước là chất đặc biệt

Nước có $c = 4200$ J/(kg.K), cao bất thường. Hệ quả: đại dương điều hoà khí hậu, vùng ven biển có biên độ nhiệt ngày đêm nhỏ, và nước là chất tải nhiệt lí tưởng cho động cơ và lò phản ứng.

**Lỗi thường gặp:**
- Dùng $Q = mc\Delta T$ trong giai đoạn chuyển thể. Nhiệt độ không đổi nên $\Delta T = 0$ và công thức cho $Q = 0$, trong khi thực tế đây là giai đoạn tiêu tốn năng lượng nhiều nhất.
- Cho rằng nhiệt độ tăng liên tục khi đun đều một khối đá. Đồ thị có hai đoạn nằm ngang ứng với hai lần chuyển thể; năng lượng lúc đó dùng để phá vỡ liên kết chứ không làm phân tử chuyển động nhanh hơn.
- Nhầm nhiệt dung riêng với nhiệt dung. Nhiệt dung riêng $c$ tính cho 1 kg chất và là đặc trưng của chất; nhiệt dung $C = mc$ phụ thuộc khối lượng cụ thể của vật.

<sub>`lesson.physics.nhiet-hoc-intl.nhiet-dung-rieng-va-nhiet-an`</sub>

---

### 3. Thuyết động học phân tử và phương trình khí lí tưởng
*Kinetic theory of gases and the ideal gas equation* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu được các giả thiết của mô hình khí lí tưởng và nêu khi nào chúng bị vi phạm
- Vận dụng được phương trình trạng thái ở cả dạng mol và dạng phân tử
- Giải thích được ý nghĩa vi mô của áp suất và nhiệt độ theo thuyết động học

## Ba định luật thực nghiệm gộp thành một

Boyle: $PV = $ hằng số khi $T$ không đổi. Charles: $V/T = $ hằng số khi $P$ không đổi. Gay-Lussac: $P/T = $ hằng số khi $V$ không đổi. Gộp lại:

$$\frac{PV}{T} = \text{hằng số} \Rightarrow PV = nRT = Nk_BT$$

Dạng mol dùng $R = 8{,}31$ J/(mol.K); dạng phân tử dùng $k_B = 1{,}38\times10^{-23}$ J/K. Hai dạng hoàn toàn tương đương vì $R = N_Ak_B$.

## Giải thích vi mô của áp suất

Phân tử đập vào thành bình rồi bật lại, mỗi lần truyền cho thành một xung lượng. Cộng hàng tỉ va chạm mỗi giây cho ra một lực gần như đều đặn. Tính toán chi tiết cho

$$P = \tfrac13 \rho \overline{v^{2}} = \tfrac13 \frac{Nm}{V}\overline{v^{2}}$$

Đây là công thức trung tâm của thuyết động học, có mặt trong syllabus A-Level dưới tên $pV = \tfrac13 Nm\overline{c^{2}}$.

## Nhiệt độ là gì ở mức phân tử

So sánh $PV = \tfrac13 Nm\overline{v^{2}}$ với $PV = Nk_BT$:

$$\bar{E}_k = \tfrac12 m\overline{v^{2}} = \tfrac32 k_B T$$

**Nhiệt độ tuyệt đối tỉ lệ thuận với động năng tịnh tiến trung bình của một phân tử.** Đây là câu trả lời sâu sắc nhất cho câu hỏi "nhiệt độ là gì", và nó giải thích luôn vì sao có độ không tuyệt đối: động năng không thể âm.

Hệ quả: ở cùng nhiệt độ, mọi khí có cùng động năng trung bình, nhưng phân tử nhẹ chạy nhanh hơn vì $v_{rms} \propto 1/\sqrt{M}$. Hydro ở 300 K có $v_{rms} \approx 1930$ m/s, oxy chỉ khoảng 480 m/s. Đó là lí do khí quyển Trái Đất giữ được oxy nhưng để hydro thoát dần vào vũ trụ.

## Khi nào mô hình sụp đổ

Khí thực lệch khỏi mô hình khi **áp suất rất cao** (thể tích riêng của phân tử không còn bỏ qua được) hoặc **nhiệt độ rất thấp** (lực hút giữa các phân tử trở nên đáng kể, khí sắp hoá lỏng). Phương trình Van der Waals hiệu chỉnh đúng hai điểm này.

**Lỗi thường gặp:**
- Dùng nhiệt độ Celsius trong $PV = nRT$. Phương trình được xây trên thang tuyệt đối; ở 0 độ C, dùng $T = 0$ sẽ cho $PV = 0$, tức khí biến mất.
- Nhầm tốc độ căn quân phương với tốc độ trung bình. $v_{rms}$ là căn của trung bình bình phương, luôn lớn hơn tốc độ trung bình số học khoảng 8 phần trăm; các công thức động năng đều dùng $v_{rms}$.
- Cho rằng ở cùng nhiệt độ mọi phân tử đều chạy như nhau. Chúng có cùng **động năng** trung bình, nên phân tử nặng chạy chậm hơn theo tỉ lệ $1/\sqrt{M}$; đây là nguyên lí của phương pháp khuếch tán tách đồng vị.

<sub>`lesson.physics.nhiet-hoc-intl.thuyet-dong-hoc-va-khi-li-tuong`</sub>

---

### 4. Nội năng và nguyên lí I nhiệt động lực học với quy ước dấu quốc tế
*Internal energy and the first law of thermodynamics with sign conventions* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Tính được nội năng của khí lí tưởng đơn nguyên tử và lưỡng nguyên tử theo bậc tự do
- Vận dụng được nguyên lí I với quy ước dấu của AP và của IB một cách nhất quán
- Phân tích được vì sao nội năng là hàm trạng thái còn nhiệt lượng và công thì không

## Nội năng của khí lí tưởng chỉ phụ thuộc nhiệt độ

Vì mô hình khí lí tưởng bỏ qua lực hút giữa các phân tử, thế năng tương tác bằng 0 và

$$U = N\bar{E}_k = \tfrac32 Nk_BT = \tfrac32 nRT \quad(\text{đơn nguyên tử})$$

Với khí lưỡng nguyên tử ở nhiệt độ thường, hai bậc tự do quay được kích hoạt nên $U = \tfrac52 nRT$.

Hệ quả cực kỳ tiện dụng: **quá trình đẳng nhiệt của khí lí tưởng có $\Delta U = 0$**, bất kể áp suất và thể tích thay đổi thế nào.

## Nguyên lí I: bảo toàn năng lượng có kể tới nhiệt

Hai cách truyền năng lượng vào hệ: truyền nhiệt và thực hiện công. Nguyên lí I nói rằng tổng của chúng làm thay đổi nội năng.

**Quy ước AP (và cả CT Việt Nam):**
$$\Delta U = Q + W, \qquad W = -P\Delta V$$
với $W$ là công thực hiện **lên** khí. Nén khí thì $W > 0$ và khí nóng lên — kiểm tra trực giác này để nhớ dấu.

**Quy ước IB (và nhiều giáo trình Anh):**
$$Q = \Delta U + W, \qquad W = +P\Delta V$$
với $W$ là công do khí **sinh ra**. Giãn khí thì $W > 0$.

Hai cách viết mô tả cùng một vật lí, chỉ khác chỗ đặt dấu. **Sai một dấu là sai toàn bài**, nên hãy tuyên bố rõ quy ước ngay dòng đầu lời giải và giữ nguyên đến hết.

## Vì sao $U$ đặc biệt

Đưa hệ từ trạng thái A tới B bằng hai đường khác nhau: $Q$ và $W$ của hai đường **khác nhau**, nhưng tổng $Q + W$ thì **giống hệt**. Đó chính là bằng chứng thực nghiệm cho thấy $U$ là hàm trạng thái. Vì thế ta viết $\Delta U$ nhưng không bao giờ viết $\Delta Q$ hay $\Delta W$: hệ không "chứa" nhiệt lượng hay công, nó chỉ chứa nội năng.

## Bốn quá trình nhìn qua nguyên lí I

| Quá trình | Đặc điểm | Nguyên lí I (quy ước AP) |
|---|---|---|
| Đẳng tích | $\Delta V = 0$ | $\Delta U = Q$ |
| Đẳng áp | $P$ không đổi | $\Delta U = Q - P\Delta V$ |
| Đẳng nhiệt | $\Delta U = 0$ | $Q = -W$ |
| Đoạn nhiệt | $Q = 0$ | $\Delta U = W$ |

**Lỗi thường gặp:**
- Trộn lẫn hai quy ước dấu trong cùng một bài, ví dụ dùng $\Delta U = Q + W$ của AP nhưng lấy $W = +P\Delta V$ của IB. Kết quả sai đúng hai lần giá trị công; luôn chọn một quy ước và ghi rõ ngay từ đầu.
- Viết $\Delta Q$ hoặc $\Delta W$. Nhiệt lượng và công là năng lượng truyền qua ranh giới trong một quá trình, không phải thuộc tính của trạng thái; hệ không chứa sẵn chúng để mà biến thiên.
- Cho rằng cấp nhiệt thì nhiệt độ luôn tăng. Trong quá trình đẳng nhiệt, toàn bộ nhiệt lượng nhận được chuyển thành công giãn nở và nhiệt độ đứng yên; thậm chí khí có thể nhận nhiệt mà vẫn lạnh đi nếu nó sinh công nhiều hơn.

<sub>`lesson.physics.nhiet-hoc-intl.noi-nang-va-nguyen-li-i`</sub>

---

### 5. Các quá trình nhiệt động và đồ thị pV
*Thermodynamic processes and pV diagrams* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Đọc được công của khí từ diện tích dưới đường quá trình trên giản đồ pV
- Phân biệt được đường đẳng nhiệt và đường đoạn nhiệt về độ dốc và về ý nghĩa vật lí
- Tính được công và nhiệt lượng của một chu trình kín trên giản đồ pV

## Diện tích trên giản đồ pV chính là công

$$W_{\text{khí sinh ra}} = \int_{V_1}^{V_2} P\,dV$$

Quy tắc đọc: đi sang **phải** (giãn nở) thì khí sinh công dương; đi sang **trái** (nén) thì công âm. Đường thẳng đứng (đẳng tích) có diện tích bằng 0, nên khí không sinh công.

## Bốn quá trình trên giản đồ

| Quá trình | Hình dạng | Công của khí | Nguyên lí I |
|---|---|---|---|
| Đẳng tích | Đoạn thẳng đứng | $0$ | $\Delta U = Q$ |
| Đẳng áp | Đoạn nằm ngang | $P\Delta V$ | $Q = \Delta U + P\Delta V$ |
| Đẳng nhiệt | Hypebol $PV = $ hằng | $nRT\ln\dfrac{V_2}{V_1}$ | $Q = W$ |
| Đoạn nhiệt | Đường dốc hơn hypebol | $\dfrac{P_1V_1 - P_2V_2}{\gamma - 1}$ | $\Delta U = -W$ |

## Vì sao đường đoạn nhiệt dốc hơn đường đẳng nhiệt

Khi giãn đẳng nhiệt, khí nhận nhiệt từ ngoài để giữ $T$ nên áp suất giảm chậm. Khi giãn đoạn nhiệt, khí không nhận nhiệt nên phải lấy năng lượng từ chính nội năng của mình, nhiệt độ **tụt xuống**, và áp suất giảm nhanh hơn. Vì thế $PV^{\gamma} = $ hằng số với $\gamma > 1$ cho đường dốc hơn $PV = $ hằng số.

Hai ví dụ đời thường: bơm xe đạp nóng lên (nén đoạn nhiệt); bình gas lạnh đi khi xả nhanh (giãn đoạn nhiệt). Mây hình thành cũng theo cơ chế này khi khối không khí bốc lên và giãn nở đoạn nhiệt.

## Chu trình kín

Quay về đúng trạng thái ban đầu thì $\Delta U = 0$ (vì $U$ là hàm trạng thái), do đó

$$Q_{\text{tổng}} = W_{\text{tổng}} = \text{diện tích bên trong chu trình}$$

Chu trình chạy **theo chiều kim đồng hồ** cho công dương: đó là động cơ nhiệt. Chạy **ngược chiều kim đồng hồ** cho công âm: đó là máy lạnh hoặc bơm nhiệt.

Chú ý: công phụ thuộc **đường đi**, nên hai quá trình nối cùng hai trạng thái nhưng qua đường khác nhau cho công khác nhau, dù $\Delta U$ như nhau.

**Lỗi thường gặp:**
- Dùng $W = P\Delta V$ cho quá trình đẳng nhiệt. Áp suất thay đổi liên tục trong quá trình đó nên phải lấy tích phân, cho $W = nRT\ln(V_2/V_1)$; dùng $P\Delta V$ với $P$ nào đó là sai về nguyên tắc.
- Nghĩ đường đoạn nhiệt và đường đẳng nhiệt có độ dốc như nhau. Đoạn nhiệt dốc hơn đúng hệ số $\gamma$ vì nhiệt độ khí giảm khi giãn, làm áp suất tụt nhanh hơn.
- Cho rằng khí trở về trạng thái ban đầu thì nhiệt lượng trao đổi cũng bằng 0. Chỉ nội năng trở về giá trị cũ; nhiệt lượng và công phụ thuộc đường đi và tổng của chúng bằng diện tích chu trình, khác 0.

<sub>`lesson.physics.nhiet-hoc-intl.cac-qua-trinh-va-do-thi-pv`</sub>

---

### 6. Nguyên lí II nhiệt động lực học và entropy
*The second law of thermodynamics and entropy* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu được nguyên lí II theo Clausius, theo Kelvin - Planck và theo entropy
- Tính được độ biến thiên entropy trong quá trình truyền nhiệt đơn giản
- Giải thích được ý nghĩa thống kê của entropy qua số vi trạng thái

## Nguyên lí I không đủ

Một cốc nước tự nguội đi rồi truyền nhiệt cho phòng ấm hơn — điều này **không vi phạm** bảo toàn năng lượng, nhưng không bao giờ xảy ra. Nguyên lí I cho biết cái gì được phép về năng lượng; nguyên lí II cho biết cái gì thực sự xảy ra. Nó quy định **chiều** của mọi quá trình tự nhiên.

## Ba phát biểu tương đương

- **Clausius**: nhiệt không thể tự truyền từ vật lạnh sang vật nóng hơn mà không có tác động bên ngoài.
- **Kelvin - Planck**: không thể chế tạo động cơ chỉ nhận nhiệt từ một nguồn duy nhất và biến toàn bộ thành công. Nói cách khác, **mọi động cơ nhiệt bắt buộc phải có nguồn lạnh**.
- **Entropy**: entropy của một hệ cô lập không bao giờ giảm, $\Delta S_{\text{toàn phần}} \ge 0$; dấu bằng chỉ xảy ra với quá trình thuận nghịch lí tưởng.

## Tính entropy

$$\Delta S = \frac{Q}{T} \quad(\text{quá trình thuận nghịch, } T \text{ không đổi})$$

Vật nhận nhiệt thì $\Delta S > 0$, vật toả nhiệt thì $\Delta S < 0$. Cùng một lượng nhiệt $Q$ gây biến thiên entropy **lớn hơn** khi truyền ở nhiệt độ thấp — vì với hệ lạnh, $Q$ đó là một xáo trộn tương đối lớn hơn.

Đó chính là lí do truyền nhiệt từ nóng sang lạnh luôn làm tổng entropy tăng: vật nóng mất $Q/T_H$ nhưng vật lạnh được $Q/T_C$ với $T_C < T_H$, nên tổng dương.

## Ý nghĩa thống kê

$$S = k_B\ln\Omega$$

Trạng thái vĩ mô nào ứng với nhiều cách sắp xếp vi mô hơn thì có entropy cao hơn, và hệ tự tìm đến đó đơn giản vì nó **nhiều khả năng hơn**. Thả một giọt mực vào nước, số cách phân tán đều lớn hơn số cách tụ lại một chỗ theo tỉ lệ thiên văn.

Điều này cũng cho thấy nguyên lí II mang tính **thống kê**, không tuyệt đối như nguyên lí I: về nguyên tắc mực có thể tụ lại, chỉ là xác suất nhỏ tới mức chờ cả tuổi vũ trụ cũng không thấy.

## Hiểu cho đúng

Entropy của một hệ **có thể giảm** (tủ lạnh làm lạnh thức ăn, cơ thể sinh vật tự tổ chức). Nhưng khi đó môi trường xung quanh tăng entropy nhiều hơn, nên tổng vẫn tăng.

**Lỗi thường gặp:**
- Cho rằng entropy của mọi hệ luôn phải tăng. Chỉ entropy của hệ **cô lập** (hoặc tổng hệ cộng môi trường) mới không giảm; một hệ hở như tủ lạnh hoặc cơ thể sống hoàn toàn có thể giảm entropy.
- Nghĩ nguyên lí II bị vi phạm bởi sự hình thành sinh vật có tổ chức cao. Sinh vật hạ entropy cục bộ nhờ tiêu thụ năng lượng có chất lượng cao từ Mặt Trời và thải nhiệt ra môi trường, làm tổng entropy vẫn tăng.
- Dùng công thức $\Delta S = Q/T$ cho quá trình không thuận nghịch mà không đi vòng qua một đường thuận nghịch tương đương. Vì $S$ là hàm trạng thái, phải tính $\Delta S$ dọc một đường thuận nghịch nối cùng hai trạng thái đó.

<sub>`lesson.physics.nhiet-hoc-intl.nguyen-li-ii-va-entropy`</sub>

---

### 7. Động cơ nhiệt, máy lạnh và giới hạn hiệu suất Carnot
*Heat engines, refrigerators and the Carnot limit* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Tính được hiệu suất của động cơ nhiệt và hiệu năng của máy lạnh, bơm nhiệt
- Vận dụng được công thức hiệu suất Carnot để đánh giá một động cơ thực
- Giải thích được vì sao không thể có động cơ nhiệt đạt hiệu suất 100 phần trăm

## Sơ đồ chung của mọi động cơ nhiệt

Nhận $Q_H$ từ nguồn nóng, sinh công $W$, **bắt buộc** thải $Q_C$ ra nguồn lạnh. Vì chu trình kín nên $\Delta U = 0$ và $W = Q_H - Q_C$, do đó

$$\eta = \frac{W}{Q_H} = 1 - \frac{Q_C}{Q_H}$$

Muốn $\eta = 1$ thì $Q_C = 0$, tức không cần nguồn lạnh — điều bị phát biểu Kelvin - Planck cấm tuyệt đối.

## Vì sao phải có nguồn lạnh

Lập luận bằng entropy: nguồn nóng mất entropy $Q_H/T_H$. Để tổng entropy không giảm, phải có nơi nhận entropy, mà công cơ học thì không mang entropy. Vậy buộc phải thải nhiệt vào một nguồn lạnh sao cho $Q_C/T_C \ge Q_H/T_H$. Sắp xếp lại bất đẳng thức này cho ngay

$$\eta \le 1 - \frac{T_C}{T_H}$$

Đây là **hiệu suất Carnot**, giới hạn không thể vượt qua dù chế tạo hoàn hảo đến đâu, dù không có chút ma sát nào.

## Đọc công thức Carnot

Muốn hiệu suất cao phải tăng $T_H$ hoặc giảm $T_C$. Thực tế $T_C$ bị chặn bởi nhiệt độ môi trường (khoảng 300 K), nên cả ngành nhiệt điện chạy đua nâng $T_H$ bằng vật liệu chịu nhiệt tốt hơn. Nhà máy nhiệt điện hiện đại có $T_H \approx 850$ K, cho $\eta_{Carnot} \approx 65$ phần trăm, còn hiệu suất thực khoảng 40 phần trăm.

## Máy lạnh và bơm nhiệt: động cơ chạy ngược

Tốn công $W$ để lấy $Q_C$ từ chỗ lạnh và đẩy $Q_H = Q_C + W$ ra chỗ nóng.

$$\mathrm{COP}_{\text{máy lạnh}} = \frac{Q_C}{W} \le \frac{T_C}{T_H - T_C}, \qquad \mathrm{COP}_{\text{bơm nhiệt}} = \frac{Q_H}{W} \le \frac{T_H}{T_H - T_C}$$

COP thường lớn hơn 1 và điều đó **không vi phạm** bảo toàn năng lượng: máy không tạo ra năng lượng mà chỉ **bơm** nhiệt từ nơi này sang nơi khác. Bơm nhiệt sưởi ấm nhà với COP bằng 4 cung cấp 4 kWh nhiệt cho mỗi 1 kWh điện, hiệu quả gấp bốn lần lò sưởi điện trở.

Lưu ý: hai nguồn càng gần nhau về nhiệt độ thì COP càng cao; đó là lí do điều hoà chạy tốn điện hơn hẳn vào ngày cực nóng.

**Lỗi thường gặp:**
- Dùng nhiệt độ Celsius trong công thức hiệu suất Carnot. Công thức chứa tỉ số $T_C/T_H$ nên bắt buộc dùng Kelvin; với 27 và 327 độ C, dùng Celsius cho 0,92 trong khi giá trị đúng là 0,50.
- Cho rằng COP lớn hơn 1 là vi phạm bảo toàn năng lượng. COP không phải hiệu suất mà là tỉ số nhiệt lượng vận chuyển trên công tiêu tốn; máy chỉ di dời nhiệt sẵn có chứ không sinh ra năng lượng.
- Nghĩ có thể đạt hiệu suất 100 phần trăm nếu loại bỏ hết ma sát. Ngay cả động cơ hoàn hảo không ma sát vẫn bị chặn bởi $1 - T_C/T_H$, vì nguyên lí II buộc phải thải nhiệt để entropy toàn phần không giảm.

<sub>`lesson.physics.nhiet-hoc-intl.dong-co-nhiet-va-hieu-suat-carnot`</sub>

---

### 8. Truyền nhiệt: dẫn nhiệt, đối lưu và bức xạ
*Heat transfer: conduction, convection and radiation* · THPT (lớp 10-12) · ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được ba cơ chế truyền nhiệt qua điều kiện xảy ra và môi trường cần thiết
- Tính được tốc độ dẫn nhiệt qua một tấm phẳng và công suất bức xạ của vật
- Vận dụng được định luật Stefan - Boltzmann và định luật Wien cho bài toán cân bằng bức xạ

## Ba con đường, ba điều kiện khác nhau

| Cơ chế | Cần môi trường | Có chuyển dời vật chất | Chủ yếu trong |
|---|---|---|---|
| Dẫn nhiệt | Có | Không | Chất rắn, nhất là kim loại |
| Đối lưu | Có (chất lưu) | Có | Chất lỏng, chất khí |
| Bức xạ | Không | Không | Mọi vật, kể cả trong chân không |

Chỉ **bức xạ** truyền được qua chân không — đó là lí do năng lượng Mặt Trời tới được Trái Đất.

## Dẫn nhiệt

$$\frac{Q}{t} = kA\frac{\Delta T}{d}$$

Tốc độ dẫn nhiệt tỉ lệ với diện tích và chênh lệch nhiệt độ, tỉ lệ nghịch với bề dày. Hệ số $k$ của đồng khoảng 400 W/(m.K), của không khí tĩnh chỉ 0,024. Chính vì thế mọi vật liệu cách nhiệt (len, xốp, áo lông) đều hoạt động theo một nguyên lí: **giam giữ không khí tĩnh** trong các túi nhỏ để nó không đối lưu được.

## Đối lưu

Đun nước từ đáy, lớp nước nóng nở ra, khối lượng riêng giảm, nổi lên; nước lạnh chìm xuống thay chỗ và tạo dòng đối lưu. Cơ chế này giải thích gió biển, dòng hải lưu, chuyển động của mảng kiến tạo và cả lí do tủ lạnh đặt ngăn đá ở phía trên.

## Bức xạ và luỹ thừa bốn

$$P = e\sigma A T^{4}$$

Số mũ 4 khiến bức xạ cực kỳ nhạy với nhiệt độ: tăng $T$ gấp đôi thì công suất tăng **16 lần**. Vật vừa phát vừa hấp thụ, nên công suất thực là $P = e\sigma A(T^{4} - T_{mt}^{4})$.

Định luật dịch chuyển Wien cho bước sóng ứng với đỉnh phổ:

$$\lambda_{max}T = 2{,}90\times10^{-3}\ \mathrm{m\,K}$$

Vật ở nhiệt độ phòng phát chủ yếu hồng ngoại (khoảng 10 micromet, mắt không thấy); sắt nung tới 1000 K bắt đầu phát ánh đỏ; Mặt Trời ở 5800 K có đỉnh ở vùng ánh sáng nhìn thấy — và không ngẫu nhiên mà mắt người nhạy nhất đúng ở đó.

## Ứng dụng: cân bằng bức xạ của hành tinh

Hành tinh hấp thụ bức xạ Mặt Trời và phát lại theo Stefan - Boltzmann. Đặt hai công suất bằng nhau, có kể tới albedo, ta ước lượng được nhiệt độ cân bằng. Với Trái Đất, phép tính này cho khoảng 255 K, thấp hơn thực tế 288 K — chênh lệch 33 K chính là hiệu ứng nhà kính tự nhiên.

**Lỗi thường gặp:**
- Cho rằng kim loại "lạnh hơn" gỗ khi sờ vào ở cùng nhiệt độ phòng. Cả hai cùng nhiệt độ; kim loại dẫn nhiệt tốt nên rút nhiệt khỏi da nhanh hơn, tạo cảm giác lạnh, đó là phản ứng của da chứ không phải phép đo nhiệt độ.
- Nghĩ đối lưu xảy ra được trong chất rắn hoặc trong chân không. Đối lưu đòi hỏi khối chất lưu di chuyển được; chất rắn không chảy còn chân không thì không có gì để chảy.
- Quên số mũ 4 trong định luật Stefan - Boltzmann và coi bức xạ tỉ lệ thuận với nhiệt độ. Vì $P \propto T^{4}$, tăng nhiệt độ tuyệt đối 20 phần trăm đã làm công suất bức xạ tăng hơn gấp đôi.

<sub>`lesson.physics.nhiet-hoc-intl.truyen-nhiet-dan-doi-luu-buc-xa`</sub>

---

## Unit 10: Thuyết tương đối hẹp - Special Relativity

### 1. Hai tiên đề Einstein và tính tương đối của sự đồng thời
*Einstein's two postulates and the relativity of simultaneity* · THPT (lớp 10-12) · ap, ib · 45 phút · nang-cao

**Mục tiêu:**
- Phát biểu được hai tiên đề của thuyết tương đối hẹp và nêu được bối cảnh thực nghiệm dẫn tới chúng
- Giải thích được vì sao hai biến cố đồng thời trong hệ này lại không đồng thời trong hệ kia
- Phân tích được thí nghiệm tưởng tượng con tàu và sân ga của Einstein

## Mâu thuẫn buộc phải giải quyết

Cuối thế kỉ XIX, vật lí có hai trụ cột dường như xung khắc. Cơ học Newton nói vận tốc cộng được: ngồi trên tàu chạy 20 m/s ném bóng 10 m/s về trước thì người trên sân ga thấy bóng bay 30 m/s. Nhưng phương trình Maxwell lại cho tốc độ sóng điện từ $c = 1/\sqrt{\varepsilon_0\mu_0}$ — một con số cố định, không tham chiếu tới bất kì hệ quy chiếu nào.

Giả thuyết ê-te (môi trường tuyệt đối mà ánh sáng truyền trong đó) là lối thoát tự nhiên, và thí nghiệm Michelson - Morley năm 1887 được thiết kế để phát hiện chuyển động của Trái Đất so với ê-te. Kết quả: **không đo được gì cả**, dù độ nhạy thừa sức phát hiện.

## Hai tiên đề

Năm 1905, Einstein chọn con đường triệt để: chấp nhận kết quả thực nghiệm và sửa lại khái niệm không gian - thời gian.

**Tiên đề 1 (nguyên lí tương đối).** Mọi định luật vật lí có dạng như nhau trong mọi hệ quy chiếu quán tính. Không tồn tại hệ quy chiếu "đứng yên tuyệt đối", và không thí nghiệm nào phát hiện được chuyển động thẳng đều của phòng thí nghiệm.

**Tiên đề 2.** Tốc độ ánh sáng trong chân không bằng $c$ trong mọi hệ quy chiếu quán tính, không phụ thuộc chuyển động của nguồn hay của người quan sát.

Tiên đề 2 là điều phản trực giác nhất trong toàn bộ vật lí: dù bạn chạy đuổi theo tia sáng với tốc độ 0,99c, bạn vẫn đo được nó vượt bạn với đúng $c$.

## Cái giá phải trả: sự đồng thời sụp đổ

Thí nghiệm tưởng tượng của Einstein. Một toa tàu chạy đều; đúng giữa toa có đèn chớp sáng.

**Người trên tàu:** ánh sáng đi hai phía quãng đường bằng nhau, tốc độ bằng nhau, nên tới hai đầu toa **cùng lúc**.

**Người trên sân ga:** ánh sáng vẫn đi với tốc độ $c$ về cả hai phía (tiên đề 2, không được cộng vận tốc tàu). Nhưng trong lúc đó, đầu sau của toa chạy **lại gần** chỗ đèn chớp còn đầu trước chạy **ra xa**. Vậy ánh sáng tới đầu sau **trước**.

Hai người đều đúng. Kết luận không thể tránh: **sự đồng thời không tuyệt đối**, nó phụ thuộc hệ quy chiếu.

Điều bị hi sinh là khái niệm "thời gian phổ quát" mà Newton coi là hiển nhiên. Từ tính tương đối của đồng thời, mọi hệ quả khác — giãn thời gian, co độ dài — đều suy ra được. Cần nhấn mạnh: các hiệu ứng này **không phải ảo giác quang học**; đồng hồ thật sự chạy chậm, và điều đó đã được kiểm chứng bằng đồng hồ nguyên tử đặt trên máy bay.

**Lỗi thường gặp:**
- Cộng vận tốc theo Galileo ở tốc độ lớn — sai vì phép cộng đó là xấp xỉ chỉ đúng khi $v \ll c$; dùng nó với tốc độ tương đối tính sẽ cho kết quả vượt $c$, mâu thuẫn với mọi thực nghiệm.
- Cho rằng các hiệu ứng tương đối tính chỉ là ảo giác do trễ tín hiệu ánh sáng — sai vì chúng vẫn tồn tại sau khi đã hiệu chỉnh mọi thời gian truyền tín hiệu; đồng hồ nguyên tử bay vòng quanh Trái Đất thực sự lệch so với đồng hồ ở mặt đất.
- Nghĩ có một hệ quy chiếu 'thật sự đứng yên' để so sánh — sai vì tiên đề 1 khẳng định mọi hệ quán tính hoàn toàn tương đương, và thí nghiệm Michelson - Morley đã loại bỏ giả thuyết ê-te.

<sub>`lesson.physics.tuong-doi.hai-tien-de-va-dong-thoi-tuong-doi`</sub>

---

### 2. Sự giãn thời gian và sự co độ dài
*Time dilation and length contraction* · THPT (lớp 10-12) · ap, ib · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được công thức giãn thời gian và co độ dài với hệ số Lorentz
- Xác định được đúng đại lượng nào là thời gian riêng và độ dài riêng trong từng bài toán
- Giải thích được nghịch lí muy-ôn khí quyển bằng hai cách nhìn tương đương

## Đồng hồ ánh sáng

Hình dung một đồng hồ gồm hai gương song song cách nhau $d$, một xung sáng nảy qua lại; một "tích tắc" là một lần đi và về.

**Trong hệ của đồng hồ:** xung đi thẳng đứng, $\Delta t_0 = 2d/c$.

**Trong hệ thấy đồng hồ chuyển động với $v$:** xung phải đi theo đường zigzag, dài hơn. Nhưng theo tiên đề 2, tốc độ của nó vẫn là $c$ chứ không tăng lên. Quãng đường dài hơn với cùng tốc độ nghĩa là **thời gian lâu hơn**. Dùng định lí Pythagore ta thu được:

$$\Delta t = \gamma\,\Delta t_0, \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$$

Đồng hồ chuyển động chạy chậm hơn. Điều này không liên quan tới cơ cấu đồng hồ — mọi quá trình, kể cả nhịp tim và tốc độ phân rã hạt nhân, đều chậm đi như nhau, vì chính **thời gian** trong hệ đó trôi chậm.

## Co độ dài

Hệ quả kèm theo, chỉ theo phương chuyển động:

$$L = \frac{L_0}{\gamma}$$

Kích thước theo phương vuông góc **không đổi**.

## Quy tắc nhận diện, chống nhầm lẫn

Sai lầm phổ biến nhất là đặt nhầm $\Delta t_0$ và $L_0$. Hai câu hỏi giúp xác định:

- **Thời gian riêng:** "Hai biến cố có xảy ra tại CÙNG MỘT ĐIỂM trong hệ này không?" Nếu có, thời gian đo trong hệ đó là thời gian riêng, và nó **nhỏ nhất**.
- **Độ dài riêng:** "Vật có ĐỨNG YÊN trong hệ này không?" Nếu có, chiều dài đo được là độ dài riêng, và nó **lớn nhất**.

Mẹo kiểm tra cuối cùng: vì $\gamma \ge 1$, thời gian luôn **giãn** ra và độ dài luôn **co** lại so với giá trị riêng. Nếu kết quả ngược lại thì chắc chắn đã nhân thay vì chia.

## Muy-ôn: bằng chứng hằng ngày

Tia vũ trụ tạo muy-ôn ở độ cao khoảng 10 km, chúng bay với 0,998c và có thời gian sống riêng chỉ 2,2 μs. Tính cổ điển: quãng đường tối đa $\approx 660$ m — không muy-ôn nào tới được mặt đất. Thực tế, máy đo ghi nhận rất nhiều.

Hai cách giải thích, hoàn toàn tương đương:

- **Nhìn từ Trái Đất:** đồng hồ của muy-ôn chạy chậm, $\gamma \approx 15{,}8$, nên thời gian sống trong hệ Trái Đất là 35 μs, đủ để đi khoảng 10 km.
- **Nhìn từ muy-ôn:** thời gian sống vẫn là 2,2 μs, nhưng bầu khí quyển co lại còn $10/15{,}8 \approx 0{,}63$ km — quãng đường ngắn đủ để đi hết.

Hai mô tả khác nhau về hình thức nhưng cho cùng kết luận quan sát được. Đó chính là nội dung của tiên đề 1: các hệ quy chiếu quán tính bình đẳng, chỉ cách kể chuyện là khác.

**Lỗi thường gặp:**
- Nhân thay vì chia khi tính co độ dài — sai vì $\gamma \ge 1$ nên nhân sẽ cho độ dài lớn hơn độ dài riêng, trong khi độ dài riêng theo định nghĩa đã là giá trị lớn nhất.
- Cho rằng thời gian riêng là thời gian đo trong hệ Trái Đất vì đó là hệ 'của chúng ta' — sai vì thời gian riêng gắn với việc hai biến cố có xảy ra cùng một chỗ hay không, không liên quan tới việc ai là người quan sát.
- Áp dụng co độ dài cho kích thước theo phương vuông góc với chuyển động — sai vì phép biến đổi Lorentz chỉ tác động lên toạ độ dọc phương chuyển động; bề ngang của vật hoàn toàn không đổi.

<sub>`lesson.physics.tuong-doi.gian-thoi-gian-va-co-do-dai`</sub>

---

### 3. Động lượng và năng lượng tương đối tính
*Relativistic momentum and energy* · THPT (lớp 10-12) · ap, ib · 50 phút · chuyen-sau

**Mục tiêu:**
- Vận dụng được biểu thức động lượng và năng lượng tương đối tính
- Giải thích được vì sao không vật có khối lượng nào đạt được tốc độ ánh sáng
- Vận dụng được hệ thức $E^2 = (pc)^2 + (mc^2)^2$ cho cả hạt có khối lượng và photon

## Vì sao phải sửa động lượng

Định luật bảo toàn động lượng là trụ cột của vật lí, nhưng dạng $p = mv$ không còn bảo toàn khi chuyển hệ quy chiếu bằng phép biến đổi Lorentz. Muốn giữ định luật bảo toàn, phải sửa định nghĩa:

$$\vec{p} = \gamma m\vec{v} = \frac{m\vec{v}}{\sqrt{1-v^2/c^2}}$$

Ở đây $m$ là **khối lượng nghỉ**, một đại lượng bất biến gắn liền với hạt. Cách nói "khối lượng tăng theo tốc độ" từng phổ biến nhưng nay bị tránh dùng, vì nó gợi ý sai rằng vật trở nên đặc hơn; điều thực sự tăng là $\gamma$.

Khi $v \to c$ thì $\gamma \to \infty$, nên động lượng tăng vô hạn. Muốn tăng tốc thêm cần lực và năng lượng vô hạn: đây là lí do vật lí sâu xa khiến **không vật có khối lượng nào đạt được $c$**. Đó không phải giới hạn kĩ thuật mà là ràng buộc nguyên tắc.

## Năng lượng

$$E = \gamma mc^2, \qquad E_0 = mc^2, \qquad W_đ = (\gamma - 1)mc^2$$

Hệ thức $E_0 = mc^2$ là kết quả sâu sắc nhất: khối lượng **chính là** một dạng năng lượng. Một vật đứng yên vẫn chứa năng lượng khổng lồ — 1 gam bất kì chất nào tương đương $9\times10^{13}$ J, bằng năng lượng của khoảng 20 nghìn tấn thuốc nổ TNT.

Đây là lời giải thích cuối cùng cho năng lượng hạt nhân: độ hụt khối trong phân hạch và nhiệt hạch chính là phần khối lượng đã chuyển thành năng lượng.

Kiểm tra tính nhất quán với cơ học Newton: khai triển $\gamma$ cho $v \ll c$ được $\gamma \approx 1 + \frac{v^2}{2c^2}$, nên

$$W_đ \approx \left(\frac{v^2}{2c^2}\right)mc^2 = \frac{1}{2}mv^2$$

Công thức quen thuộc xuất hiện trở lại như một xấp xỉ — đúng như mọi lí thuyết mới phải làm được.

## Hệ thức năng lượng - động lượng

$$E^2 = (pc)^2 + (mc^2)^2$$

Đây là dạng hữu dụng nhất trong vật lí hạt vì nó không chứa $v$ và $\gamma$. Hai trường hợp giới hạn:

- **Hạt đứng yên** ($p=0$): $E = mc^2$.
- **Photon** ($m=0$): $E = pc$, nên $p = E/c = hf/c = h/\lambda$ — đúng hệ thức de Broglie. Photon không có khối lượng nghỉ nhưng vẫn có động lượng, và đó là lí do áp suất bức xạ tồn tại, cho phép cánh buồm mặt trời đẩy tàu vũ trụ.

Quy ước đơn vị của vật lí hạt: khối lượng đo bằng MeV/c², động lượng bằng MeV/c. Khi đó hệ thức trên trở thành phép cộng Pythagore đơn giản giữa ba con số cùng đơn vị MeV — một tiện lợi lớn khi tính toán phản ứng hạt.

**Lỗi thường gặp:**
- Dùng $W_đ = \frac{1}{2}mv^2$ cho hạt có động năng cùng cỡ hoặc lớn hơn năng lượng nghỉ — sai vì công thức đó chỉ là số hạng đầu của khai triển; ở tốc độ cao nó cho kết quả vượt tốc độ ánh sáng.
- Cho rằng $E = mc^2$ là năng lượng toàn phần của mọi vật — sai vì đó chỉ là năng lượng NGHỈ; vật chuyển động có $E = \gamma mc^2$, lớn hơn phần chênh lệch chính là động năng.
- Kết luận photon không có động lượng vì khối lượng nghỉ bằng 0 — sai vì hệ thức $E^2 = (pc)^2 + (mc^2)^2$ với $m=0$ cho $p = E/c \ne 0$; áp suất bức xạ là bằng chứng thực nghiệm trực tiếp.

<sub>`lesson.physics.tuong-doi.dong-luong-va-nang-luong-tuong-doi-tinh`</sub>

---

## Unit 11: Thiên văn - Astrophysics (IB Option D)

### 1. Thang khoảng cách thiên văn và phép đo thị sai
*The cosmic distance ladder and stellar parallax* · THPT (lớp 10-12) · ib · 45 phút · trung-binh

**Mục tiêu:**
- Sử dụng được các đơn vị đo khoảng cách thiên văn: AU, năm ánh sáng và parsec
- Vận dụng được phương pháp thị sai lượng giác để tính khoảng cách tới sao gần
- Giải thích được vai trò của nến chuẩn trong việc mở rộng thang khoảng cách

## Vì sao đo khoảng cách vũ trụ là bài toán khó

Không thể căng thước tới một ngôi sao. Toàn bộ thiên văn học định lượng dựa trên một chuỗi phương pháp gián tiếp, mỗi phương pháp hiệu chuẩn cho phương pháp tiếp theo — gọi là **thang khoảng cách vũ trụ**. Mỗi bậc thang có tầm hoạt động riêng, và sai số tích luỹ dần khi leo lên cao.

## Bậc 1: đơn vị thiên văn

Khoảng cách Trái Đất - Mặt Trời, $1\ \text{AU} \approx 1{,}50\times10^{11}$ m, được xác định trực tiếp bằng radar phản xạ từ các hành tinh. Đây là bậc thang duy nhất đo được theo nghĩa thực sự.

## Bậc 2: thị sai lượng giác

Quan sát một sao gần cách nhau sáu tháng, khi Trái Đất ở hai đầu đường kính quỹ đạo. Sao gần sẽ dịch chuyển biểu kiến so với nền sao xa. Nửa góc dịch chuyển gọi là góc thị sai $p$.

Định nghĩa parsec được xây dựng để công thức trở nên đơn giản nhất có thể:

$$d\ (\text{pc}) = \frac{1}{p\ (\text{giây cung})}$$

Sao càng xa, góc thị sai càng nhỏ. Ngôi sao gần nhất, Proxima Centauri, có $p = 0{,}77''$ — nhỏ hơn góc trông một đồng xu ở cách 5 km. Đó là lí do phải mất tới năm 1838 con người mới đo được thị sai sao đầu tiên, dù ý tưởng đã có từ thời Hy Lạp cổ.

Giới hạn: từ mặt đất chỉ đo được tới khoảng 100 pc; vệ tinh Gaia mở rộng ra hàng chục nghìn pc nhưng vẫn chỉ bao phủ một phần Ngân Hà.

## Bậc 3: nến chuẩn

Với khoảng cách lớn hơn, ta dùng nguyên tắc: nếu biết **độ trưng thật** $L$ của một thiên thể và đo được **độ rọi** $b$ mà nó gây ra ở Trái Đất, thì khoảng cách suy ra từ định luật nghịch đảo bình phương:

$$b = \frac{L}{4\pi d^2}$$

Hai loại nến chuẩn quan trọng:

- **Sao Cepheid:** chu kì biến quang liên hệ chặt chẽ với độ trưng (Henrietta Leavitt, 1912). Đo chu kì là biết $L$. Dùng được tới khoảng 30 Mpc.
- **Siêu tân tinh loại Ia:** nổ khi sao lùn trắng vượt giới hạn Chandrasekhar 1,44 khối lượng Mặt Trời, nên độ sáng cực đại gần như đồng nhất. Rất sáng, dùng được tới hàng nghìn Mpc.

Chính siêu tân tinh Ia đã dẫn tới phát hiện năm 1998 rằng vũ trụ giãn nở **có gia tốc** — bằng chứng đầu tiên cho năng lượng tối.

Cần nhớ giới hạn phương pháp: nến chuẩn giả định độ trưng thật đồng nhất và ánh sáng không bị bụi hấp thụ trên đường đi. Việc hiệu chỉnh hai giả định này là nguồn sai số chính của toàn bộ thang đo.

**Lỗi thường gặp:**
- Dùng toàn bộ góc dịch chuyển sau sáu tháng làm góc thị sai — sai vì thị sai được định nghĩa là NỬA góc đó, ứng với đáy tam giác bằng 1 AU chứ không phải 2 AU; nhầm lẫn làm khoảng cách sai một nửa.
- Nhầm độ trưng với độ rọi — sai vì độ trưng là công suất thật của sao, còn độ rọi là công suất nhận được trên mỗi mét vuông tại Trái Đất; hai đại lượng chỉ liên hệ với nhau qua khoảng cách.
- Áp dụng phương pháp thị sai cho thiên hà xa — sai vì góc thị sai giảm theo khoảng cách và nhanh chóng xuống dưới ngưỡng phân giải của mọi kính thiên văn; ở tầm đó phải chuyển sang nến chuẩn.

<sub>`lesson.physics.thien-van.thang-khoang-cach-va-thi-sai`</sub>

---

### 2. Độ trưng, cấp sao và định luật Stefan-Boltzmann
*Luminosity, stellar magnitudes and the Stefan-Boltzmann law* · THPT (lớp 10-12) · ib · 50 phút · nang-cao

**Mục tiêu:**
- Phân tích được sự khác nhau giữa cấp sao biểu kiến và cấp sao tuyệt đối, vận dụng được mô đun khoảng cách
- Vận dụng được định luật Stefan-Boltzmann và định luật Wien để xác định bán kính và nhiệt độ sao
- Giải thích được vì sao thang cấp sao là thang logarit ngược

## Một thang đo có từ thời cổ đại

Hipparchus xếp các sao thành 6 cấp: cấp 1 là sáng nhất, cấp 6 là mờ nhất mà mắt thường còn thấy. Khi đo được định lượng, người ta phát hiện mắt người phản ứng theo **logarit** với độ sáng, và cấp 1 sáng hơn cấp 6 khoảng 100 lần. Thang hiện đại giữ nguyên truyền thống ấy bằng định nghĩa:

$$m_1 - m_2 = -2{,}5\lg\frac{b_1}{b_2}$$

Hai đặc điểm dễ gây nhầm, cần ghi nhớ:

- Thang **ngược**: số nhỏ hơn nghĩa là sáng hơn. Mặt Trời có $m = -26{,}7$; Sirius có $m = -1{,}46$.
- Thang **logarit**: chênh 5 cấp là tỉ số 100 lần, nên chênh 1 cấp là tỉ số $100^{1/5} \approx 2{,}512$ lần.

## Cấp biểu kiến không nói gì về ngôi sao

Một ngôi sao trông mờ có thể vì nó thật sự yếu, hoặc vì nó rất xa. Để so sánh bản chất các sao, ta quy tất cả về cùng khoảng cách chuẩn 10 pc, thu được cấp sao tuyệt đối $M$. Liên hệ qua **mô đun khoảng cách**:

$$m - M = 5\lg\frac{d}{10\ \text{pc}}$$

Công thức này rất mạnh vì nó dùng được theo cả hai chiều: biết $d$ thì suy ra $M$; ngược lại, nếu biết $M$ từ nến chuẩn thì đo $m$ sẽ cho $d$. Đây chính là cơ chế toán học đằng sau thang khoảng cách vũ trụ.

## Ngôi sao như một vật đen

Phổ của sao rất gần phổ vật đen, nên hai định luật của bức xạ nhiệt áp dụng trực tiếp:

**Wien** cho nhiệt độ bề mặt từ màu sắc:
$$\lambda_{\max}T = 2{,}90\times10^{-3}\ \text{m·K}$$

**Stefan-Boltzmann** cho độ trưng từ nhiệt độ và kích thước:
$$L = 4\pi R^2\sigma T^4$$

Ghép hai định luật lại, ta có một quy trình đo được **bán kính của một ngôi sao cách xa hàng nghìn tỉ kilômét** chỉ bằng cách phân tích ánh sáng của nó:

1. Đo phổ → tìm $\lambda_{\max}$ → suy ra $T$ (Wien).
2. Đo $m$ và biết $d$ → tính $L$.
3. Thay vào Stefan-Boltzmann → giải ra $R$.

Đây là một trong những thành tựu đẹp nhất của vật lí ứng dụng: ba phép đo trên Trái Đất cho biết kích thước và nhiệt độ của một vật thể ta sẽ không bao giờ chạm tới.

Lưu ý về độ nhạy: $L$ phụ thuộc $T^4$ nên sai số 5% ở nhiệt độ gây sai số hơn 20% ở độ trưng, và tiếp tục lan sang bán kính. Ước lượng sai số vì thế là phần bắt buộc của mọi bài toán thiên văn thực tế.

**Lỗi thường gặp:**
- Cho rằng cấp sao lớn hơn nghĩa là sáng hơn — sai vì thang cấp sao là thang ngược kế thừa từ Hipparchus; sao càng sáng thì cấp càng nhỏ, và các thiên thể rất sáng có cấp âm.
- Kết luận sao lạnh thì luôn mờ — sai vì độ trưng phụ thuộc cả bán kính lẫn nhiệt độ; sao siêu kềnh đỏ có nhiệt độ thấp nhưng diện tích bề mặt khổng lồ nên độ trưng vẫn rất lớn.
- Dùng cấp sao biểu kiến để so sánh độ sáng thật của hai sao — sai vì cấp biểu kiến phụ thuộc khoảng cách; muốn so sánh bản chất phải quy về cấp sao tuyệt đối qua mô đun khoảng cách.

<sub>`lesson.physics.thien-van.do-trung-va-cap-sao`</sub>

---

### 3. Giản đồ Hertzsprung-Russell và tiến hoá sao
*The Hertzsprung-Russell diagram and stellar evolution* · THPT (lớp 10-12) · ib · 50 phút · nang-cao

**Mục tiêu:**
- Đọc và giải thích được các vùng chính trên giản đồ Hertzsprung-Russell
- Vận dụng được quan hệ khối lượng - độ trưng để ước lượng thời gian sống trên dãy chính
- Mô tả được con đường tiến hoá của sao khối lượng nhỏ và sao khối lượng lớn

## Một biểu đồ tổ chức lại toàn bộ thiên văn học

Đầu thế kỉ XX, Hertzsprung và Russell vẽ độ trưng theo nhiệt độ bề mặt cho hàng nghìn sao. Nếu các sao là ngẫu nhiên, các điểm sẽ rải đều. Thực tế chúng tụ lại thành vài vùng rõ rệt — dấu hiệu chắc chắn rằng có quy luật vật lí phía sau.

Lưu ý quy ước vẽ: trục nhiệt độ **giảm dần từ trái sang phải** (kế thừa từ cách xếp lớp phổ OBAFGKM), còn trục độ trưng theo thang logarit.

**Bốn vùng chính:**

- **Dãy chính** — dải chéo từ trên trái (nóng, sáng, xanh) xuống dưới phải (lạnh, mờ, đỏ). Mặt Trời nằm giữa dải này.
- **Sao kềnh đỏ và siêu kềnh đỏ** — góc trên phải: lạnh nhưng cực sáng, nên phải rất lớn.
- **Sao lùn trắng** — góc dưới trái: nóng nhưng rất mờ, nên phải rất nhỏ (cỡ Trái Đất).
- Các đường chéo đồng bán kính chạy chéo qua giản đồ, giúp đọc kích thước ngay từ vị trí điểm.

## Vì sao có dãy chính

Sao trên dãy chính đang ở trạng thái **cân bằng thuỷ tĩnh**: áp suất bức xạ và áp suất khí từ phản ứng nhiệt hạch trong lõi đẩy ra, cân bằng đúng với lực hấp dẫn nén vào. Trạng thái này rất ổn định và chiếm phần lớn đời sao.

Vị trí trên dãy chính do **duy nhất khối lượng** quyết định, theo quan hệ thực nghiệm:

$$L \propto M^{3{,}5}$$

Từ đó suy ra thời gian sống:

$$t \propto \frac{M}{L} \propto M^{-2{,}5}$$

Kết luận phản trực giác nhưng cực kì quan trọng: **sao càng nặng càng chết sớm**. Sao 10 khối lượng Mặt Trời có nhiều nhiên liệu gấp 10 lần nhưng đốt nhanh gấp hơn 3000 lần, nên chỉ sống khoảng 30 triệu năm so với 10 tỉ năm của Mặt Trời.

## Hai con đường tiến hoá

**Sao khối lượng nhỏ và trung bình (dưới 8 $M_\odot$):** hết hiđrô ở lõi → phồng thành kềnh đỏ, đốt heli → đẩy lớp vỏ ra thành tinh vân hành tinh → lõi trơ còn lại thành **sao lùn trắng**, nguội dần mãi mãi. Sao lùn trắng được chống đỡ bởi áp suất suy biến electron, một hiệu ứng thuần lượng tử từ nguyên lí loại trừ Pauli, và chỉ tồn tại được nếu khối lượng dưới giới hạn Chandrasekhar 1,44 $M_\odot$.

**Sao khối lượng lớn (trên 8 $M_\odot$):** đốt lần lượt các nguyên tố nặng dần thành các lớp vỏ như củ hành, cho tới khi lõi hoá **sắt**. Vì sắt nằm ở đỉnh đồ thị năng lượng liên kết riêng, mọi phản ứng tiếp theo đều **thu** năng lượng chứ không toả. Lõi mất chỗ dựa, sụp đổ trong chưa tới một giây và bật lại thành **siêu tân tinh**. Tàn dư là sao nơtron (nếu lõi dưới khoảng 3 $M_\odot$) hoặc **lỗ đen**.

Mọi nguyên tố nặng hơn sắt trong vũ trụ đều được tổng hợp trong những giây cuối cùng của các vụ nổ ấy.

**Lỗi thường gặp:**
- Cho rằng sao khối lượng lớn sống lâu hơn vì có nhiều nhiên liệu — sai vì độ trưng tăng theo $M^{3{,}5}$, nhanh hơn nhiều so với mức tăng nhiên liệu tỉ lệ với $M$, nên tốc độ tiêu thụ lấn át hoàn toàn.
- Đọc trục nhiệt độ của giản đồ HR theo chiều tăng từ trái sang phải — sai vì quy ước thiên văn xếp nhiệt độ GIẢM dần sang phải; đọc ngược sẽ đặt sao lùn trắng và kềnh đỏ vào sai vị trí.
- Áp giới hạn Chandrasekhar cho khối lượng ban đầu của sao — sai vì giới hạn này áp cho khối lượng LÕI còn lại sau khi sao đã thổi bay phần lớn vỏ ngoài; một sao ban đầu 5 khối lượng Mặt Trời vẫn kết thúc thành sao lùn trắng.

<sub>`lesson.physics.thien-van.gian-do-hr-va-tien-hoa-sao`</sub>

---

### 4. Định luật Hubble và sự giãn nở của vũ trụ
*Hubble's law and the expanding universe* · THPT (lớp 10-12) · ib · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được dịch chuyển đỏ vũ trụ và phân biệt nó với hiệu ứng Doppler thông thường
- Vận dụng được định luật Hubble để tính khoảng cách tới thiên hà và ước lượng tuổi vũ trụ
- Phân tích được các bằng chứng ủng hộ mô hình Vụ Nổ Lớn

## Phát hiện làm thay đổi vũ trụ quan

Những năm 1920, Hubble đo phổ của nhiều thiên hà và thấy các vạch quang phổ đều dịch về phía đỏ. Áp dụng cho tốc độ, kết quả là hầu hết thiên hà đang **lùi xa** chúng ta. Đáng chú ý hơn, tốc độ lùi xa tỉ lệ thuận với khoảng cách:

$$v = H_0d$$

Đây là bằng chứng đầu tiên rằng vũ trụ không tĩnh tại.

## Hiểu cho đúng: không gian giãn nở

Cách hiểu sai phổ biến: các thiên hà bay ra xa trong một không gian cố định, và ta ở tâm vụ nổ.

Cách hiểu đúng: **chính không gian giữa các thiên hà đang giãn ra**. Ánh sáng bị kéo dài bước sóng trong lúc đang đi, chứ không phải do nguồn chuyển động — vì thế gọi là dịch chuyển đỏ vũ trụ chứ không phải Doppler.

Hai hệ quả quan trọng của cách hiểu này:

- **Không có tâm.** Hình dung các chấm mực trên quả bóng đang được thổi phồng: mọi chấm đều thấy các chấm khác lùi xa mình, và chấm càng xa thì lùi càng nhanh. Không chấm nào đặc biệt. Vũ trụ cũng vậy.
- **Vũ trụ không giãn nở "vào" đâu cả.** Câu hỏi "bên ngoài vũ trụ là gì" không có nghĩa trong mô hình này, vì không gian không nằm bên trong một không gian lớn hơn.

## Tuổi vũ trụ

Cho ánh xạ ngược thời gian: nếu tốc độ giãn nở không đổi, thời gian để mọi thứ chụm về một điểm là

$$t = \frac{1}{H_0}$$

Với $H_0 = 70$ km/s/Mpc, đổi đơn vị cho $t \approx 14$ tỉ năm — rất gần giá trị chính xác 13,8 tỉ năm từ dữ liệu vi sóng nền. Sự trùng khớp này đáng nể vì phép tính đã giả định tốc độ giãn nở không đổi, điều không hoàn toàn đúng.

## Ba bằng chứng cho Vụ Nổ Lớn

1. **Định luật Hubble** — vũ trụ đang giãn, nên trong quá khứ nó nhỏ và đặc hơn.
2. **Bức xạ nền vi sóng vũ trụ (CMB)** — phổ vật đen gần như hoàn hảo ở 2,7 K, phủ đều toàn bầu trời. Đây là ánh sáng phát ra khi vũ trụ mới 380 000 tuổi và vừa đủ nguội để nguyên tử hình thành, nay đã bị kéo dài bước sóng vào vùng vi sóng.
3. **Tỉ lệ nguyên tố nhẹ** — mô hình dự đoán khoảng 75% hiđrô và 25% heli theo khối lượng được tạo trong ba phút đầu tiên; quan sát khớp chính xác.

## Câu hỏi còn mở

Cuối những năm 1990, quan sát siêu tân tinh loại Ia ở rất xa cho thấy chúng mờ hơn dự đoán, nghĩa là vũ trụ giãn nở **có gia tốc**. Nguyên nhân được gọi là năng lượng tối, chiếm khoảng 68% mật độ năng lượng vũ trụ, và bản chất của nó vẫn hoàn toàn chưa được biết. So sánh mật độ thực với **mật độ tới hạn** cho biết vũ trụ sẽ giãn mãi hay co lại; số liệu hiện nay nghiêng hẳn về kịch bản giãn nở vĩnh viễn và tăng tốc.

**Lỗi thường gặp:**
- Kết luận Trái Đất nằm ở tâm vũ trụ vì mọi thiên hà đều lùi xa ta — sai vì trong không gian đang giãn nở đồng đều, người quan sát ở BẤT KÌ thiên hà nào cũng thấy điều tương tự; không tồn tại vị trí đặc biệt.
- Giải thích dịch chuyển đỏ vũ trụ hoàn toàn bằng hiệu ứng Doppler — sai vì thiên hà không chuyển động xuyên qua không gian, mà chính không gian giữa chúng giãn ra và kéo dài bước sóng ánh sáng đang truyền.
- Quên đổi megaparsec sang mét khi tính tuổi vũ trụ từ $H_0$ — sai vì đơn vị km/s/Mpc trộn hai hệ đo khoảng cách; bỏ qua bước này làm kết quả sai nhiều bậc độ lớn.

<sub>`lesson.physics.thien-van.dinh-luat-hubble-va-gian-no-vu-tru`</sub>

---

## Unit 1: Kinematics (AP Physics 1 Unit 1 / IB A.1 / CIE 9702 Topic 2)

### 1. Hệ quy chiếu, độ dịch chuyển, vận tốc và tốc độ
*Frames of reference, displacement, velocity and speed* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được quãng đường với độ dịch chuyển, tốc độ với vận tốc bằng ví dụ cụ thể
- Xác định được vận tốc trung bình và vận tốc tức thời từ dữ liệu vị trí - thời gian
- Giải thích được vì sao mọi mô tả chuyển động chỉ có nghĩa khi gắn với một hệ quy chiếu

## Chuyển động so với cái gì

Một hành khách ngồi yên trên tàu: đứng yên so với toa, chạy 80 km/h so với đường ray, và quay quanh trục Trái Đất với vài trăm mét mỗi giây so với tâm Trái Đất. Cả ba mô tả đều đúng. Bài toán vật lí chỉ bắt đầu có nghĩa khi ta tuyên bố **hệ quy chiếu**: vật mốc, trục tọa độ có chiều dương, và mốc thời gian.

## Bốn đại lượng dễ lẫn

| Vô hướng | Vectơ |
|---|---|
| Quãng đường $s$ (luôn tăng) | Độ dịch chuyển $\vec{d}$ (có thể giảm, có thể bằng 0) |
| Tốc độ trung bình $= s/\Delta t$ | Vận tốc trung bình $\vec{v}_{tb} = \vec{d}/\Delta t$ |

Vận động viên chạy hết một vòng sân 400 m trong 50 s có tốc độ trung bình 8 m/s nhưng vận tốc trung bình **bằng 0**, vì điểm đầu trùng điểm cuối. Đây là câu hỏi khởi động kinh điển của AP Physics 1.

## Từ trung bình sang tức thời

Vận tốc trung bình trên đoạn $\Delta t$:

$$\vec{v}_{tb} = \frac{\Delta \vec{r}}{\Delta t}$$

Thu nhỏ $\Delta t$ dần, cát tuyến trên đồ thị $x$-$t$ tiến về tiếp tuyến, và ta được vận tốc tức thời

$$\vec{v} = \lim_{\Delta t \to 0}\frac{\Delta \vec{r}}{\Delta t} = \frac{d\vec{r}}{dt}$$

AP Physics 1 dừng ở mức đồ thị và tỉ số; AP Physics C dùng thẳng đạo hàm. Ý tưởng vật lí thì như nhau.

## Khi nào dùng được

Mọi công thức trên đúng với mọi chuyển động, kể cả gia tốc thay đổi. Chỉ khi chuyển động **thẳng và không đổi chiều** thì quãng đường mới bằng độ lớn độ dịch chuyển, và tốc độ trung bình mới bằng độ lớn vận tốc trung bình.

**Lỗi thường gặp:**
- Lấy trung bình cộng hai tốc độ của hai chặng. Tốc độ trung bình là tổng quãng đường chia tổng thời gian; trung bình cộng chỉ đúng khi hai chặng có **thời gian** bằng nhau, không phải khi quãng đường bằng nhau.
- Cộng độ dịch chuyển như cộng số. Độ dịch chuyển là vectơ, đi 3 km đông rồi 4 km bắc cho 5 km chứ không phải 7 km.
- Bỏ qua việc chọn chiều dương rồi lúng túng với dấu. Khi vật đổi chiều, tọa độ giảm và vận tốc mang dấu âm; dấu âm ở đây mang thông tin về hướng chứ không có nghĩa là "chậm".

<sub>`lesson.physics.dong-hoc-intl.he-quy-chieu-va-do-dich-chuyen`</sub>

---

### 2. Đồ thị chuyển động: ý nghĩa của độ dốc và diện tích
*Motion graphs: meaning of gradient and area* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được vận tốc từ độ dốc đồ thị vị trí - thời gian và gia tốc từ độ dốc đồ thị vận tốc - thời gian
- Tính được độ dịch chuyển từ diện tích dưới đồ thị vận tốc - thời gian, kể cả phần diện tích âm
- Chuyển đổi được qua lại giữa ba loại đồ thị $x$-$t$, $v$-$t$, $a$-$t$ của cùng một chuyển động

## Hai thao tác, ba đồ thị

Toàn bộ động học đồ thị nằm gọn trong hai câu:

- **Đi xuống một bậc thì lấy độ dốc**: $x \xrightarrow{\text{độ dốc}} v \xrightarrow{\text{độ dốc}} a$.
- **Đi lên một bậc thì lấy diện tích**: $a \xrightarrow{\text{diện tích}} \Delta v \xrightarrow{\text{diện tích}} \Delta x$.

## Đọc hình dạng

Trên đồ thị $x$-$t$: đường nằm ngang là đứng yên; đường thẳng dốc là vận tốc không đổi; đường cong lõm lên là gia tốc dương. **Điểm cực trị** của $x$-$t$ là lúc vật đổi chiều, ở đó $v = 0$ nhưng $a$ thường khác 0 — đây là chỗ nhiều học sinh sập bẫy.

Trên đồ thị $v$-$t$: giao điểm với trục hoành là lúc đổi chiều; hai vùng diện tích trái dấu triệt tiêu nhau nghĩa là vật quay lại vị trí cũ.

## Vì sao diện tích lại là độ dịch chuyển

Chia trục thời gian thành nhiều dải hẹp $\Delta t$. Trong mỗi dải, $v$ gần như không đổi nên $\Delta x \approx v\,\Delta t$, đúng bằng diện tích cột. Cộng mọi cột và cho $\Delta t \to 0$:

$$\Delta x = \int_{t_1}^{t_2} v\,dt$$

Đây chính là lí do vì sao với chuyển động biến đổi đều, diện tích hình thang cho $\Delta x = \frac{1}{2}(v_0 + v)t$.

## Giới hạn cần nhớ

Đồ thị $v$-$t$ cho **độ dịch chuyển** qua diện tích đại số. Muốn quãng đường thì phải lấy tổng **trị tuyệt đối** từng vùng. Ngoài ra đồ thị chỉ mô tả chuyển động theo một trục; chuyển động hai chiều cần hai bộ đồ thị riêng cho $x$ và $y$.

**Lỗi thường gặp:**
- Cho rằng $v = 0$ thì $a = 0$. Tại điểm cao nhất của vật ném lên, vận tốc bằng 0 nhưng gia tốc vẫn là $g$ hướng xuống; nếu $a$ cũng bằng 0 thì vật sẽ đứng lơ lửng mãi mãi.
- Nhầm đồ thị $x$-$t$ với hình dạng quỹ đạo. Đồ thị $x$-$t$ hình parabol không có nghĩa vật bay theo đường parabol; nó chỉ nói tọa độ biến thiên bậc hai theo thời gian trên một đường thẳng.
- Lấy tổng diện tích không dấu khi được hỏi độ dịch chuyển. Phần dưới trục hoành ứng với chuyển động ngược chiều dương, phải trừ đi, nếu không kết quả sẽ là quãng đường chứ không phải độ dịch chuyển.

<sub>`lesson.physics.dong-hoc-intl.do-thi-chuyen-dong`</sub>

---

### 3. Chuyển động thẳng biến đổi đều và bộ phương trình SUVAT
*Uniformly accelerated motion and the SUVAT equations* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Chứng minh được bốn phương trình SUVAT từ định nghĩa gia tốc và đồ thị vận tốc - thời gian
- Vận dụng được phương trình phù hợp bằng cách nhận diện đại lượng thiếu trong bài toán
- Phân tích được điều kiện áp dụng và những tình huống mà bộ SUVAT không dùng được

## Trường hợp đặc biệt nhưng phổ biến nhất

Khi lực tổng hợp không đổi thì gia tốc không đổi, và đó là tình huống của rơi tự do, vật trượt trên mặt phẳng nghiêng, xe phanh gấp. Với gia tốc không đổi, ta có bộ công thức đóng kín.

## Dẫn ra từ đồ thị

Đồ thị $v$-$t$ là đường thẳng từ $u$ tới $v$ trong thời gian $t$.

1. Độ dốc là gia tốc: $v = u + at$.
2. Diện tích hình thang là độ dịch chuyển: $s = \dfrac{u+v}{2}t$.
3. Thay (1) vào (2): $s = ut + \tfrac12 at^{2}$.
4. Khử $t$ giữa (1) và (2): $v^{2} = u^{2} + 2as$.

AP viết bộ này theo trục $x$: $v_x = v_{x0} + a_x t$ và $x = x_0 + v_{x0}t + \tfrac12 a_x t^{2}$; IB và A-Level dùng ký hiệu SUVAT. Nội dung hoàn toàn như nhau.

## Chiến thuật chọn phương trình

Liệt kê năm ký hiệu, đánh dấu ba đại lượng đã biết và một đại lượng cần tìm. Đại lượng còn lại là đại lượng **không xuất hiện**, hãy chọn phương trình vắng nó. Cách này tránh được việc giải hệ vòng vo.

## Khi nào tuyệt đối không dùng

Bộ SUVAT sụp đổ nếu gia tốc thay đổi: lò xo dao động ($a = -\omega^{2}x$), rơi có lực cản, chuyển động tròn đều (gia tốc đổi hướng liên tục dù không đổi độ lớn). Trong những trường hợp đó phải quay về $a = dv/dt$ và tích phân, hoặc dùng năng lượng. Đọc kỹ đề: chữ "biến đổi đều", "gia tốc không đổi", "bỏ qua lực cản" chính là giấy phép sử dụng.

**Lỗi thường gặp:**
- Dùng SUVAT cho chuyển động có gia tốc thay đổi. Cả bốn hệ thức đều được dẫn ra với giả thiết đồ thị $v$-$t$ là đường thẳng; áp dụng cho dao động điều hòa hay rơi có lực cản sẽ cho kết quả vô nghĩa.
- Đặt $a = -g$ rồi lại thay $g = -9{,}8$. Dấu đã nằm trong việc chọn chiều dương; ghi dấu hai lần làm gia tốc thành hướng lên, vật ném lên sẽ bay mãi.
- Thay $s$ bằng quãng đường khi vật đổi chiều. Trong SUVAT, $s$ là **độ dịch chuyển**; với vật ném lên rồi rơi về chỗ cũ thì $s = 0$ chứ không phải hai lần độ cao cực đại.

<sub>`lesson.physics.dong-hoc-intl.chuyen-dong-bien-doi-deu-suvat`</sub>

---

### 4. Rơi tự do và chuyển động thẳng đứng dưới trọng lực
*Free fall and vertical motion under gravity* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao mọi vật rơi tự do đều có cùng gia tốc, không phụ thuộc khối lượng
- Vận dụng được bộ SUVAT cho chuyển động thẳng đứng với quy ước dấu nhất quán
- Phân tích được sự đối xứng của quỹ đạo ném thẳng đứng khi bỏ qua lực cản

## Vì sao búa và lông chim rơi như nhau

Định luật II Newton cho $a = F/m$. Với trọng lực $F = mg$ thì $a = mg/m = g$: khối lượng bị triệt tiêu. Vật nặng chịu lực lớn hơn nhưng cũng "ì" hơn đúng theo cùng tỉ lệ. Thí nghiệm của phi hành gia David Scott trên Mặt Trăng năm 1971 cho búa và lông chim chạm đất cùng lúc chính là minh chứng trực tiếp.

Trong không khí, lông chim rơi chậm không phải vì nhẹ mà vì tỉ số lực cản trên trọng lượng của nó rất lớn.

## Áp dụng SUVAT theo phương thẳng đứng

Chọn chiều dương hướng lên, khi đó $a = -g$ trong suốt chuyển động, kể cả lúc đi lên, lúc ở đỉnh và lúc rơi xuống. Bốn hệ thức trở thành

$$v = u - gt,\qquad y = ut - \tfrac12 gt^{2},\qquad v^{2} = u^{2} - 2gy$$

Mốc thời gian và mốc tọa độ đặt ở điểm ném.

## Ba hệ quả đối xứng

1. Tại độ cao cực đại $v = 0$, suy ra $t_{\text{lên}} = u/g$ và $h_{\max} = u^{2}/(2g)$.
2. Thời gian rơi trở lại điểm ném bằng đúng $t_{\text{lên}}$, nên tổng thời gian bay là $2u/g$.
3. Vật trở về điểm ném với **tốc độ bằng tốc độ ném**, chỉ ngược chiều.

Cả ba hệ quả chỉ đúng khi bỏ qua lực cản. Có lực cản, thời gian rơi xuống **dài hơn** thời gian đi lên và tốc độ khi về nhỏ hơn tốc độ ném, vì lực cản luôn lấy đi năng lượng ở cả hai chặng.

## Bẫy quen thuộc

Vật ném lên từ đỉnh tòa nhà rồi rơi xuống chân tòa nhà: nếu chọn chiều dương lên và gốc ở điểm ném thì $y$ lúc chạm đất là **số âm**. Giải phương trình bậc hai sẽ ra hai nghiệm $t$; nghiệm âm bị loại vì ứng với quá khứ trước lúc ném.

**Lỗi thường gặp:**
- Cho rằng ở điểm cao nhất gia tốc bằng 0 vì vận tốc bằng 0. Gia tốc do trọng lực gây ra, mà trọng lực không hề biến mất khi vật dừng lại trong khoảnh khắc; nếu $a = 0$ vật sẽ treo lơ lửng.
- Dùng công thức $h = \tfrac12 gt^{2}$ cho vật ném lên. Công thức đó chỉ đúng khi vận tốc ban đầu bằng 0; với $u \neq 0$ phải dùng $y = ut - \tfrac12 gt^{2}$.
- Nghĩ vật nặng rơi nhanh hơn trong chân không. Kết luận của Aristotle bị phản bác vì $a = mg/m$ không chứa $m$; sự khác biệt quan sát trong không khí là do lực cản chứ không do trọng lực.

<sub>`lesson.physics.dong-hoc-intl.roi-tu-do`</sub>

---

### 5. Chuyển động ném và tính độc lập của hai phương
*Projectile motion and independence of perpendicular components* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được tính độc lập giữa chuyển động theo phương ngang và phương thẳng đứng
- Vận dụng được phương pháp tách thành phần để tính tầm xa, tầm cao và thời gian bay
- Chứng minh được góc ném 45 độ cho tầm xa lớn nhất khi hai đầu cùng độ cao

## Thí nghiệm quyết định

Thả một viên bi rơi thẳng đứng, đồng thời bắn một viên bi khác theo phương ngang từ cùng độ cao. Hai viên **chạm đất cùng lúc**. Lí do: trọng lực chỉ có thành phần thẳng đứng nên không hề ảnh hưởng đến chuyển động ngang, và chuyển động ngang cũng không làm thay đổi tốc độ rơi.

Đây là ý tưởng trung tâm của cả chủ đề: **tách một bài toán hai chiều thành hai bài toán một chiều đã biết cách giải**.

## Bộ công thức

Với vận tốc ném $v_0$ hợp góc $\theta$ so với phương ngang, gốc tại điểm ném:

$$x = v_0\cos\theta \cdot t, \qquad y = v_0\sin\theta \cdot t - \tfrac12 g t^{2}$$

$$v_x = v_0\cos\theta = \text{const}, \qquad v_y = v_0\sin\theta - gt$$

Khử $t$ được phương trình quỹ đạo là parabol:

$$y = x\tan\theta - \frac{g x^{2}}{2v_0^{2}\cos^{2}\theta}$$

## Ba kết quả hay dùng (khi ném và rơi cùng độ cao)

- Thời gian bay: $t = \dfrac{2v_0\sin\theta}{g}$
- Tầm cao: $H = \dfrac{v_0^{2}\sin^{2}\theta}{2g}$
- Tầm xa: $R = \dfrac{v_0^{2}\sin 2\theta}{g}$

Vì $\sin 2\theta \le 1$ nên $R$ cực đại tại $2\theta = 90^{\circ}$, tức $\theta = 45^{\circ}$. Hai góc bù nhau như $30^{\circ}$ và $60^{\circ}$ cho cùng tầm xa nhưng thời gian bay khác nhau.

## Cảnh báo phạm vi

Ba công thức trên **chỉ đúng khi điểm ném và điểm rơi cùng độ cao**. Bắn từ vách đá hoặc ném bóng rổ vào rổ cao hơn tay thì phải quay lại giải trực tiếp phương trình $y(t)$. Ngoài ra mọi kết quả đều giả thiết bỏ qua lực cản; với quả bóng thật, quỹ đạo không còn đối xứng và góc tối ưu nhỏ hơn $45^{\circ}$.

**Lỗi thường gặp:**
- Cho rằng thành phần vận tốc ngang giảm dần theo thời gian. Không có lực nào theo phương ngang (đã bỏ qua lực cản), nên theo định luật I Newton $v_x$ giữ nguyên suốt quỹ đạo.
- Dùng công thức tầm xa $R = v_0^{2}\sin 2\theta/g$ cho bài ném từ vách đá. Công thức này được dẫn ra với điều kiện điểm rơi cùng độ cao điểm ném; ném từ độ cao khác phải giải phương trình bậc hai theo $t$.
- Lấy $v_0$ trực tiếp vào phương trình phương đứng mà quên nhân $\sin\theta$. Chỉ có hình chiếu của vận tốc lên phương đứng mới tham gia chuyển động theo phương đó.

<sub>`lesson.physics.dong-hoc-intl.chuyen-dong-nem`</sub>

---

### 6. Chuyển động tương đối và công thức cộng vận tốc
*Relative motion and velocity addition* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Vận dụng được công thức cộng vận tốc với ký hiệu chỉ số kép theo quy ước quốc tế
- Giải được bài toán qua sông và bài toán vượt xe bằng giản đồ vectơ
- Giải thích được vì sao gia tốc là như nhau trong mọi hệ quy chiếu quán tính

## Vận tốc luôn là vận tốc "so với"

Khi nói ô tô chạy 60 km/h, ta ngầm hiểu là so với mặt đường. Ký hiệu quốc tế viết rõ điều đó: $\vec{v}_{AB}$ là vận tốc của $A$ **đối với** $B$.

## Quy tắc ghép chỉ số

$$\vec{v}_{AC} = \vec{v}_{AB} + \vec{v}_{BC}$$

Chỉ số $B$ ở giữa "khử" đi. Kèm theo là $\vec{v}_{AB} = -\vec{v}_{BA}$. Với ký hiệu Việt Nam quen thuộc, đây chính là $\vec{v}_{13} = \vec{v}_{12} + \vec{v}_{23}$ (vật 1 so với đất 3, qua trung gian là hệ 2).

Khi hai vận tốc cùng phương thì cộng đại số; khi hợp góc $\alpha$ thì dùng định lí hàm cos:

$$v_{13} = \sqrt{v_{12}^{2} + v_{23}^{2} + 2v_{12}v_{23}\cos\alpha}$$

## Hai bài toán mẫu

**Qua sông.** Thuyền có vận tốc $\vec{v}_{TN}$ so với nước, nước chảy $\vec{v}_{ND}$ so với bờ. Muốn **sang bờ nhanh nhất**, hướng mũi thuyền vuông góc bờ: thời gian $t = d/v_{TN}$ là nhỏ nhất, nhưng thuyền bị trôi xuôi. Muốn **cập đúng điểm đối diện**, phải hướng mũi thuyền chếch ngược dòng sao cho thành phần ngang triệt tiêu dòng chảy; khi đó $v_{\text{ngang}} = \sqrt{v_{TN}^{2} - v_{ND}^{2}}$ và bài toán chỉ có nghiệm nếu $v_{TN} > v_{ND}$.

**Vượt xe.** Trên đường cao tốc, xe 100 km/h vượt xe 90 km/h: trong hệ quy chiếu của xe chậm, xe nhanh chỉ đi 10 km/h. Chuyển sang hệ quy chiếu của một trong hai vật biến bài toán hai vật chuyển động thành bài toán một vật.

## Điều bất biến

Lấy đạo hàm hệ thức cộng vận tốc theo thời gian, nếu $\vec{v}_{BC}$ không đổi thì $\vec{a}_{AC} = \vec{a}_{AB}$. **Gia tốc như nhau trong mọi hệ quy chiếu quán tính** — chính điều này khiến định luật II Newton dùng được ở mọi hệ quán tính.

**Lỗi thường gặp:**
- Cộng độ lớn hai vận tốc mà không vẽ giản đồ vectơ. Chỉ khi hai vectơ cùng phương mới cộng trừ số học được; hợp góc bất kì phải dùng định lí hàm cos hoặc tách thành phần.
- Nhầm chiều chỉ số, viết $\vec{v}_{AC} = \vec{v}_{BA} + \vec{v}_{BC}$. Quy tắc chỉ khử được chỉ số khi chúng đứng kề nhau và cùng ký hiệu; viết sai thứ tự tương đương với việc đổi dấu một vectơ.
- Cho rằng hệ quy chiếu gắn với vật đang có gia tốc vẫn dùng được định luật Newton như bình thường. Hệ đó không quán tính, muốn dùng phải bổ sung lực quán tính.

<sub>`lesson.physics.dong-hoc-intl.chuyen-dong-tuong-doi`</sub>

---

## Unit 1: Tĩnh điện - Electrostatics

### 1. Điện tích, bảo toàn điện tích và định luật Coulomb
*Electric charge, charge conservation and Coulomb's law* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được ba cách làm nhiễm điện một vật và chỉ ra điện tích được bảo toàn trong mỗi cách
- Vận dụng được định luật Coulomb để tính lực tương tác giữa hai điện tích điểm trong chân không và trong điện môi
- Vận dụng được nguyên lí chồng chất để tìm lực điện tổng hợp lên một điện tích trong hệ nhiều điện tích

## Vì sao điện tích lại có hai loại

Cọ xát thanh thuỷ tinh vào lụa, thanh nhựa vào len: hai thanh thuỷ tinh đẩy nhau, thanh thuỷ tinh lại hút thanh nhựa. Không cách nào giải thích bộ thí nghiệm này bằng một loại điện tích duy nhất, nên Franklin quy ước có hai loại và gán dấu đại số cho chúng. Quy ước đó không phải tuỳ tiện: nó biến phép cộng lực thành phép cộng đại số.

Điều then chốt là cọ xát **không sinh ra** điện tích. Electron chỉ chuyển từ vật này sang vật kia, nên tổng đại số điện tích của hệ cô lập không đổi:

$$\sum q_i = \text{const}$$

Đây là định luật bảo toàn điện tích, đúng cả trong phản ứng hạt nhân lẫn trong va chạm hạt cơ bản.

## Định luật Coulomb

Dùng cân xoắn, Coulomb (1785) đo được lực giữa hai quả cầu nhỏ tích điện:

$$F = k\dfrac{|q_1 q_2|}{r^2}, \qquad k = \dfrac{1}{4\pi\varepsilon_0} \approx 9{,}0\times10^{9}\ \text{N·m}^2/\text{C}^2$$

Lực hướng dọc đường nối hai điện tích, đẩy nhau nếu cùng dấu, hút nhau nếu trái dấu. Trong điện môi đồng nhất, lực giảm $\varepsilon_r$ lần: $F = k|q_1q_2|/(\varepsilon_r r^2)$.

## Khi nào dùng được và khi nào không

Công thức trên chỉ đúng cho **điện tích điểm** hoặc quả cầu tích điện đều (khi đó có thể coi điện tích tập trung ở tâm). Với hai quả cầu dẫn đặt gần nhau, điện tích phân bố lại do hưởng ứng, khoảng cách hiệu dụng khác $r$ tâm - tâm nên công thức chỉ còn gần đúng.

Với nhiều điện tích, lực tuân theo **nguyên lí chồng chất**: lực tổng hợp lên $q_0$ là tổng vectơ các lực do từng điện tích gây ra, tính độc lập như thể các điện tích khác không có mặt. Chính tính tuyến tính này khiến toàn bộ tĩnh điện học trở nên giải được.

**Lỗi thường gặp:**
- Thay cả dấu âm của điện tích vào công thức rồi kết luận lực âm — sai vì công thức Coulomb tính ĐỘ LỚN, dấu chỉ dùng để quyết định hút hay đẩy; nhét dấu vào rồi lại vẽ vectơ theo dấu sẽ tính hai lần một thông tin.
- Cộng độ lớn các lực thành phần khi có nhiều hơn hai điện tích — sai vì lực là đại lượng vectơ, chỉ khi các lực cùng phương cùng chiều thì tổng độ lớn mới bằng độ lớn tổng.
- Quên đổi đơn vị khoảng cách từ cm sang m — sai vì hằng số $k$ được cho trong hệ SI, dùng cm làm kết quả sai $10^4$ lần do $r$ bị bình phương.

<sub>`lesson.physics.tinh-dien.dien-tich-va-dinh-luat-coulomb`</sub>

---

### 2. Điện trường và đường sức điện
*Electric field and field lines* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được cường độ điện trường do một hoặc nhiều điện tích điểm gây ra tại một điểm
- Giải thích được ý nghĩa vật lí của đường sức điện và đọc được thông tin về độ lớn, hướng của trường từ hình vẽ đường sức
- Phân tích được điện trường của lưỡng cực điện và của hệ hai điện tích cùng dấu

## Từ lực sang trường

Định luật Coulomb mô tả tương tác trực tiếp giữa hai điện tích, nhưng nó im lặng về câu hỏi: nếu ta dịch chuyển $q_1$, thì $q_2$ biết ngay lập tức hay chậm hơn? Faraday đề nghị đổi cách nhìn: điện tích $Q$ làm biến đổi không gian quanh nó, tạo ra một **trường**; điện tích $q$ đặt vào đó chịu lực do trường tại chỗ nó đứng, không cần biết $Q$ ở đâu.

Định nghĩa toán học tách hẳn trường khỏi vật thử:

$$\vec{E} = \frac{\vec{F}}{q_0}\quad (\text{V/m hoặc N/C})$$

Điện tích thử $q_0$ phải đủ nhỏ để không làm xáo trộn phân bố điện tích nguồn — đây là điều kiện thường bị bỏ quên.

## Trường của điện tích điểm và nguyên lí chồng chất

Ghép định nghĩa với định luật Coulomb:

$$E = k\frac{|Q|}{r^2}$$

hướng ra xa $Q$ nếu $Q>0$, hướng về $Q$ nếu $Q<0$. Với hệ nhiều điện tích, $\vec{E} = \sum \vec{E}_i$ — cộng **vectơ**, không cộng số.

## Đường sức nói gì

Quy ước vẽ đường sức chứa hai thông tin: hướng của tiếp tuyến cho hướng $\vec{E}$, còn **mật độ** đường sức tỉ lệ với độ lớn $E$. Vì vậy vùng đường sức mau là vùng trường mạnh. Đường sức xuất phát từ điện tích dương, kết thúc ở điện tích âm hoặc đi ra vô cùng.

Ba hệ quả nên nhớ vì chúng thường bị vi phạm khi học sinh vẽ hình:

- Hai đường sức **không bao giờ cắt nhau**, vì tại giao điểm sẽ có hai hướng $\vec{E}$ khác nhau, vô lí.
- Đường sức **không khép kín** trong tĩnh điện (khác hẳn đường cảm ứng từ), phản ánh việc trường tĩnh điện là trường thế.
- Đường sức luôn **vuông góc với mặt vật dẫn** ở trạng thái cân bằng tĩnh điện, vì thành phần tiếp tuyến sẽ làm electron tự do chuyển động, mâu thuẫn với giả thiết cân bằng.

Giữa hai bản phẳng song song rộng tích điện trái dấu, trường coi là đều — mô hình nền cho tụ điện và cho bài toán chuyển động của hạt mang điện.

**Lỗi thường gặp:**
- Nghĩ rằng $\vec{E}$ phụ thuộc vào điện tích thử $q_0$ — sai vì khi $q_0$ tăng thì $F$ tăng đúng cùng tỉ lệ, thương số không đổi; $\vec{E}$ chỉ do điện tích nguồn và vị trí quyết định.
- Vẽ đường sức cắt nhau ở vùng giữa hai điện tích — sai vì tại điểm cắt vectơ $\vec{E}$ sẽ có hai hướng, trong khi trường tổng hợp tại mỗi điểm là duy nhất.
- Cộng $E_1 + E_2$ theo số học khi hai vectơ không cùng phương — sai vì bỏ mất phép chiếu, kết quả luôn lớn hơn giá trị thật.

<sub>`lesson.physics.tinh-dien.dien-truong-va-duong-suc`</sub>

---

### 3. Thông lượng điện và định luật Gauss
*Electric flux and Gauss's law* · THPT (lớp 10-12) · ap · 50 phút · nang-cao

**Mục tiêu:**
- Tính được thông lượng điện qua một mặt phẳng đặt trong điện trường đều
- Phát biểu và giải thích được ý nghĩa của định luật Gauss dạng tích phân
- Phân tích được vì sao điện trường bên trong vật dẫn cân bằng tĩnh điện bằng không

## Ý tưởng: đếm đường sức thay vì cộng vectơ

Tính $\vec{E}$ của một dây tích điện dài bằng cách chia nhỏ rồi cộng vectơ là một tích phân khó chịu. Gauss nhận ra rằng nếu hệ có đối xứng, ta có thể **đếm** tổng số đường sức đi ra khỏi một mặt kín, và con số đó chỉ phụ thuộc điện tích bên trong.

Đại lượng đếm ấy là thông lượng điện. Với trường đều qua mặt phẳng:

$$\Phi_E = EA\cos\theta$$

Góc $\theta$ đo giữa $\vec{E}$ và **pháp tuyến** của mặt, không phải giữa $\vec{E}$ và mặt phẳng. Khi mặt song song với đường sức, $\theta = 90^\circ$ và $\Phi_E = 0$: không đường sức nào xuyên qua.

## Định luật Gauss

$$\oint_S \vec{E}\cdot d\vec{A} = \frac{Q_{\text{trong}}}{\varepsilon_0}$$

Phát biểu: thông lượng điện qua một mặt kín bất kì bằng tổng đại số điện tích nằm **bên trong** mặt đó chia cho $\varepsilon_0$.

Hai chi tiết quyết định khi vận dụng:

- Điện tích **ngoài** mặt Gauss vẫn đóng góp vào $\vec{E}$ tại từng điểm trên mặt, nhưng đóng góp **0** vào thông lượng tổng, vì đường sức của nó vào rồi lại ra.
- Định luật luôn đúng, nhưng chỉ **giải được ra $E$** khi ta chọn được mặt Gauss mà trên đó $E$ không đổi và $\vec{E}$ song song hoặc vuông góc với mặt. Không có đối xứng thì định luật vẫn đúng mà vô dụng về mặt tính toán.

## Hệ quả: vật dẫn cân bằng tĩnh điện

Giả sử bên trong khối kim loại có $\vec{E}\neq 0$; electron tự do sẽ chuyển động, mâu thuẫn với trạng thái cân bằng. Vậy $\vec{E}_{\text{trong}} = 0$. Lấy mặt Gauss nằm hoàn toàn trong khối kim loại: thông lượng bằng 0 nên $Q_{\text{trong}} = 0$ — **mọi điện tích dư phải nằm trên bề mặt**. Ngay sát mặt ngoài, $E = \sigma/\varepsilon_0$ và luôn vuông góc với mặt. Đây chính là nguyên lí của lồng Faraday và lí do ngồi trong ô tô kim loại là an toàn khi sét đánh.

**Lỗi thường gặp:**
- Dùng góc giữa $\vec{E}$ và mặt phẳng thay vì góc với pháp tuyến — sai vì làm hoán đổi $\sin$ và $\cos$, dẫn tới thông lượng cực đại lại bị tính thành 0.
- Kết luận $\vec{E} = 0$ tại mọi điểm trên mặt Gauss khi $Q_{\text{trong}} = 0$ — sai vì Gauss chỉ nói TỔNG thông lượng bằng 0; trường tại từng điểm vẫn có thể khác 0 do điện tích bên ngoài.
- Cho rằng điện tích đặt ngoài mặt Gauss làm thay đổi thông lượng — sai vì mọi đường sức của nó đi vào mặt kín rồi đi ra, đóng góp hai phần bằng nhau trái dấu.

<sub>`lesson.physics.tinh-dien.thong-luong-dien-va-dinh-luat-gauss`</sub>

---

### 4. Vận dụng định luật Gauss: đối xứng cầu, trụ và phẳng
*Applying Gauss's law: spherical, cylindrical and planar symmetry* · THPT (lớp 10-12) · ap · 50 phút · nang-cao

**Mục tiêu:**
- Chọn được mặt Gauss phù hợp với từng loại đối xứng của phân bố điện tích
- Chứng minh được biểu thức điện trường trong và ngoài quả cầu dẫn, quả cầu tích điện đều theo thể tích, dây dài vô hạn và mặt phẳng vô hạn
- So sánh được quy luật phụ thuộc khoảng cách $1/r^2$, $1/r$ và hằng số của ba loại đối xứng

## Quy trình bốn bước

Định luật Gauss chỉ hữu ích nếu ta chọn mặt Gauss khéo. Quy trình chuẩn:

1. Nhận diện đối xứng để đoán hướng của $\vec{E}$.
2. Chọn mặt Gauss sao cho trên đó $E$ = const và $\vec{E}\parallel d\vec{A}$ (hoặc $\perp$, khi đó phần ấy đóng góp 0).
3. Viết $\oint\vec{E}\cdot d\vec{A} = E\cdot A_{\text{hiệu dụng}}$.
4. Tính $Q_{\text{trong}}$ rồi giải ra $E$.

## Đối xứng cầu

Quả cầu **dẫn** bán kính $R$ mang điện tích $Q$: điện tích nằm hết trên mặt.

$$r<R:\ E = 0; \qquad r\ge R:\ E = k\frac{Q}{r^2}$$

Bên ngoài, quả cầu "giả dạng" một điện tích điểm ở tâm.

Quả cầu **cách điện** tích điện đều theo thể tích với mật độ $\rho$: bên trong chỉ phần điện tích trong bán kính $r$ đóng góp, $Q_{\text{trong}} = Q r^3/R^3$, nên

$$r<R:\ E = \frac{kQr}{R^3}\ (\text{tỉ lệ thuận } r); \qquad r\ge R:\ E = \frac{kQ}{r^2}$$

Điện trường đạt cực đại đúng tại mặt cầu.

## Đối xứng trụ

Dây thẳng dài vô hạn, mật độ $\lambda$. Mặt Gauss là hình trụ đồng trục bán kính $r$, dài $\ell$. Hai đáy có $\vec{E}\perp$ pháp tuyến nên không đóng góp; mặt bên có diện tích $2\pi r\ell$:

$$E\cdot 2\pi r\ell = \frac{\lambda \ell}{\varepsilon_0} \;\Rightarrow\; E = \frac{\lambda}{2\pi\varepsilon_0 r}$$

Giảm theo $1/r$ chứ không phải $1/r^2$ — vì nguồn trải theo một chiều.

## Đối xứng phẳng

Mặt phẳng vô hạn mật độ $\sigma$: $E = \dfrac{\sigma}{2\varepsilon_0}$, **không phụ thuộc khoảng cách**. Với hai bản song song tích điện trái dấu, trường ở giữa cộng lại thành $E = \sigma/\varepsilon_0$ còn bên ngoài triệt tiêu — đây là cơ sở của tụ điện phẳng.

Quy luật chung dễ nhớ: nguồn điểm ($1/r^2$), nguồn dài ($1/r$), nguồn phẳng (hằng số). Số chiều mà nguồn trải ra càng lớn, trường càng giảm chậm.

**Lỗi thường gặp:**
- Dùng toàn bộ $Q$ khi tính trường bên trong quả cầu tích điện đều — sai vì phần vỏ cầu nằm ngoài bán kính $r$ tạo trường bằng 0 tại mọi điểm bên trong nó, chỉ lõi trong đóng góp.
- Áp dụng $E = kQ/r^2$ cho dây dài vô hạn — sai vì công thức đó chỉ đúng với đối xứng cầu; nguồn trải theo chiều dài cho $E \propto 1/r$.
- Quên rằng với hai bản song song, trường giữa hai bản là $\sigma/\varepsilon_0$ chứ không phải $\sigma/2\varepsilon_0$ — sai vì đã bỏ mất đóng góp của bản thứ hai, hai bản trái dấu cho trường cùng chiều ở khoảng giữa.

<sub>`lesson.physics.tinh-dien.van-dung-gauss-ba-hinh-doi-xung`</sub>

---

### 5. Thế năng điện, điện thế và hiệu điện thế
*Electric potential energy, potential and potential difference* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Chứng minh được công của lực điện không phụ thuộc dạng đường đi và suy ra sự tồn tại của thế năng điện
- Phân tích được sự khác nhau giữa thế năng điện, đại lượng của hệ điện tích, với điện thế, đại lượng của riêng trường
- Vận dụng được nguyên lí chồng chất điện thế để tính điện thế do hệ điện tích điểm gây ra

## Vì sao điện trường tĩnh có thế năng

Lực Coulomb là lực xuyên tâm và phụ thuộc khoảng cách, giống hệt lực hấp dẫn. Khi tính công dịch chuyển điện tích từ M tới N theo hai đường khác nhau, kết quả bằng nhau: công chỉ phụ thuộc vị trí đầu và cuối. Lực có tính chất đó gọi là **lực thế**, và ta được phép định nghĩa thế năng $W$ sao cho $A_{MN} = W_M - W_N$.

Đây không phải chuyện hình thức. Nó cho phép giải bài toán chuyển động của hạt mang điện bằng bảo toàn năng lượng, tránh hẳn việc tích phân lực theo quỹ đạo cong.

## Từ thế năng sang điện thế

Thế năng $W = qV$ phụ thuộc cả điện tích thử. Chia đi phần "của vật thử", ta được đại lượng thuần tuý của trường:

$$V = \frac{W}{q}, \qquad V_{\text{điểm}} = k\frac{Q}{r}$$

Chú ý dấu: điện thế do điện tích âm gây ra là **âm**, không lấy trị tuyệt đối như khi tính $E$. Vì $V$ là vô hướng, chồng chất trở nên rất dễ:

$$V = \sum_i k\frac{Q_i}{r_i}$$

cộng đại số, không cần phân tích vectơ. Đây là lí do bài toán nào tính được bằng $V$ thì nên tính bằng $V$.

## Công của lực điện

$$A_{MN} = q(V_M - V_N) = qU_{MN}$$

Trong điện trường đều, $A = qEd$ với $d$ là **hình chiếu** của độ dời lên phương đường sức. Nếu điện tích chạy vòng rồi về chỗ cũ, $A = 0$ — hệ quả trực tiếp của tính thế.

## Ba cạm bẫy khái niệm

- $V$ có thể khác 0 nơi $E = 0$ (ví dụ bên trong quả cầu dẫn: $E=0$ nhưng $V = kQ/R$ không đổi và khác 0).
- $E$ có thể khác 0 nơi $V = 0$ (điểm giữa hai điện tích trái dấu bằng nhau).
- Chỉ **hiệu** điện thế có ý nghĩa vật lí; gốc thế thường chọn ở vô cùng hoặc ở đất, nhưng đó là quy ước.

Với các bài hạt vi mô, dùng đơn vị eV giúp tránh luỹ thừa âm rất lớn: electron tăng tốc qua 1000 V thu động năng đúng 1000 eV.

**Lỗi thường gặp:**
- Lấy trị tuyệt đối của $Q$ khi tính $V = kQ/r$ — sai vì điện thế là đại lượng đại số, dấu của nó mang thông tin vật lí; bỏ dấu sẽ khiến điện thế của lưỡng cực không bao giờ triệt tiêu.
- Kết luận $E = 0$ ở nơi $V = 0$ — sai vì $E$ liên hệ với ĐỘ DỐC của $V$ theo không gian chứ không phải giá trị của $V$; hàm số có thể bằng 0 tại một điểm mà đạo hàm vẫn khác 0.
- Dùng $A = qEd$ với $d$ là quãng đường thực tế đi được — sai vì chỉ hình chiếu của độ dời lên phương đường sức mới sinh công, thành phần vuông góc cho công bằng 0.

<sub>`lesson.physics.tinh-dien.the-nang-dien-va-dien-the`</sub>

---

### 6. Mặt đẳng thế và liên hệ giữa điện trường với điện thế
*Equipotential surfaces and the field-potential relationship* · THPT (lớp 10-12) · ap, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao đường sức luôn vuông góc với mặt đẳng thế
- Vận dụng được hệ thức $E = -\,dV/dx$ và $E = U/d$ trong điện trường đều
- Phân tích được đồ thị $V(r)$ để suy ra hướng và độ lớn của điện trường

## Vì sao đường sức vuông góc với mặt đẳng thế

Giả sử $\vec{E}$ có một thành phần nằm dọc theo mặt đẳng thế. Khi đó dịch chuyển điện tích một đoạn nhỏ dọc mặt sẽ sinh công khác 0, kéo theo $\Delta V \neq 0$ — mâu thuẫn với định nghĩa mặt đẳng thế. Vậy thành phần tiếp tuyến phải bằng 0, tức $\vec{E}\perp$ mặt đẳng thế tại mọi điểm.

Đây là lí do hình học: bề mặt vật dẫn cân bằng tĩnh điện là một mặt đẳng thế, nên đường sức luôn đâm vuông góc vào kim loại.

## Hệ thức định lượng

Dọc một hướng bất kì:

$$E_x = -\frac{dV}{dx}$$

Dấu trừ mang ý nghĩa vật lí rõ ràng: điện trường hướng về phía điện thế **giảm**, giống như vật rơi về phía thế năng thấp. Điện tích dương thả tự do sẽ trôi xuôi theo $\vec{E}$, tức là đi tới nơi $V$ nhỏ hơn; điện tích âm thì ngược lại.

Trong điện trường đều giữa hai bản song song cách nhau $d$:

$$E = \frac{U}{d}$$

Công thức này lí giải vì sao đơn vị của $E$ vừa là N/C vừa là V/m — hai cách nhìn cùng một đại lượng.

## Đọc bản đồ đẳng thế

Vẽ các mặt đẳng thế cách nhau những bước $\Delta V$ bằng nhau, ta được một "bản đồ đường đồng mức":

- Nơi các mặt đẳng thế **sít nhau** là nơi $|dV/dx|$ lớn, tức $E$ mạnh.
- Nơi chúng thưa là nơi trường yếu.
- Quanh điện tích điểm, mặt đẳng thế là các mặt cầu đồng tâm, càng vào gần càng dày đặc, đúng với $E\propto 1/r^2$.

Với quả cầu dẫn tích điện: bên trong $E = 0$ nên $V$ = const $= kQ/R$; bên ngoài $V = kQ/r$. Đồ thị $V(r)$ là một đoạn nằm ngang rồi tiếp nối một nhánh hypebol — chỗ nối tại $r=R$ có độ dốc gãy, phản ánh $E$ nhảy từ 0 lên $kQ/R^2$.

## Cạm bẫy

Mặt đẳng thế **không** phải nơi $E$ không đổi. Ví dụ mặt phẳng trung trực của lưỡng cực có $V=0$ ở mọi điểm nhưng $E$ giảm dần khi ra xa. Hai khái niệm "đẳng thế" và "đều" hoàn toàn khác nhau.

**Lỗi thường gặp:**
- Bỏ dấu trừ trong $E = -dV/dx$ — sai vì khi đó điện trường sẽ được vẽ hướng về phía điện thế tăng, mâu thuẫn với việc điện tích dương tự do luôn chạy về nơi thế năng thấp.
- Dùng $E = U/d$ cho trường không đều — sai vì công thức này là hệ quả của việc $E$ không đổi trên đoạn $d$; với trường của điện tích điểm phải dùng dạng vi phân hoặc tích phân.
- Đồng nhất mặt đẳng thế với vùng có trường đều — sai vì đẳng thế chỉ ràng buộc giá trị $V$ như nhau, còn độ lớn $E$ (tức độ dốc theo phương pháp tuyến) hoàn toàn có thể thay đổi dọc theo mặt.

<sub>`lesson.physics.tinh-dien.mat-dang-the-va-lien-he-e-v`</sub>

---

### 7. Chuyển động của điện tích trong điện trường đều
*Motion of charged particles in a uniform electric field* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được định luật II Newton để lập phương trình chuyển động của hạt mang điện trong điện trường đều
- Chứng minh được quỹ đạo của hạt bay vuông góc vào điện trường đều là một parabol
- Giải thích được nguyên lí thí nghiệm giọt dầu Millikan và phép đo tỉ số $e/m$

## Vì sao bài toán này giống ném ngang

Trong điện trường đều, lực điện $\vec{F} = q\vec{E}$ có độ lớn và hướng không đổi, hệt như trọng lực gần mặt đất. Do đó toàn bộ bộ công cụ của chuyển động ném xiên dùng lại được, chỉ thay $g$ bằng

$$a = \frac{qE}{m} = \frac{qU}{md}$$

Một lưu ý về độ lớn: với electron trong trường $10^4$ V/m, $a \approx 1{,}8\times10^{15}$ m/s². So với con số đó, $g = 9{,}8$ m/s² là hoàn toàn bỏ qua được — đây chính là lí do các bài toán hạt cơ bản thường không nhắc tới trọng lực. Ngược lại, với giọt dầu Millikan khối lượng lớn hơn hàng chục bậc, trọng lực lại là nhân vật chính.

## Hai tình huống chuẩn

**Tăng tốc dọc đường sức.** Dùng định lí động năng: $qU = \frac{1}{2}mv^2 \Rightarrow v = \sqrt{2qU/m}$. Cách này nhanh hơn hẳn dùng động học vì không cần biết thời gian hay quãng đường.

**Bay vuông góc vào trường** (bài toán bản lái tia trong dao động kí). Chọn Ox theo $\vec{v}_0$, Oy theo lực điện:

$$x = v_0 t,\qquad y = \frac{1}{2}\frac{qE}{m}t^2 \;\Rightarrow\; y = \frac{qE}{2mv_0^2}x^2$$

Quỹ đạo là **parabol**. Khi rời khỏi hai bản dài $\ell$, độ lệch $y = \dfrac{qU\ell^2}{2mdv_0^2}$ và $\tan\alpha = \dfrac{qU\ell}{mdv_0^2}$.

## Millikan và điện tích nguyên tố

Millikan cho giọt dầu tích điện rơi giữa hai bản. Khi giọt **lơ lửng**, lực điện cân bằng trọng lực:

$$qE = mg \;\Rightarrow\; q = \frac{mgd}{U}$$

Đo hàng nghìn giọt, ông thấy mọi giá trị $q$ đều là bội số nguyên của một lượng duy nhất $e \approx 1{,}6\times10^{-19}$ C. Kết luận không phải là "điện tích nhỏ" mà là **điện tích bị lượng tử hoá** — một trong những bằng chứng thực nghiệm đẹp nhất của vật lí đầu thế kỉ XX.

Phép đo $e/m$ của Thomson dùng ý tưởng đối ngẫu: cho chùm electron chịu đồng thời điện trường và từ trường vuông góc, chỉnh sao cho tia đi thẳng rồi tắt từ trường để đo độ lệch.

**Lỗi thường gặp:**
- Cộng thêm trọng lực vào bài toán electron — sai vì gia tốc do lực điện lớn hơn $g$ tới khoảng 14 bậc độ lớn, việc giữ lại $g$ không cải thiện độ chính xác mà chỉ gây rối; ngược lại với giọt dầu Millikan thì bắt buộc phải giữ.
- Dùng $v = v_0 + at$ cho tốc độ theo phương ban đầu — sai vì lực điện vuông góc với $\vec{v}_0$ nên thành phần $v_x$ giữ nguyên; chỉ thành phần vuông góc mới biến thiên.
- Cho rằng hạt luôn ra khỏi hai bản mà không kiểm tra $y \le d/2$ — sai vì nếu độ lệch vượt nửa khoảng cách bản, hạt đập vào bản và bài toán dừng ở đó.

<sub>`lesson.physics.tinh-dien.chuyen-dong-dien-tich-trong-dien-truong-deu`</sub>

---

## Unit 2: Advanced Electrodynamics

### 1. Phương pháp ảnh điện và Chuyển động của hạt trong điện từ trường chéo nhau
*Method of image charges and charged particle motion in crossed fields* · THPT (lớp 10-12) · ru-east-eu, olympiad · 55 phút · nang-cao

**Mục tiêu:**
- Vận dụng phương pháp ảnh điện để tìm thế và cường độ điện trường gần mặt phẳng dẫn nối đất
- Tính lực tương tác và năng lượng thế giữa điện tích điểm và mặt phẳng dẫn
- Phân tích quỹ đạo chuyển động cycloid và vận tốc trôi của hạt mang điện trong trường E vuông góc B

## Phương pháp ảnh điện đối với mặt phẳng dẫn nối đất

Xét điện tích điểm $q$ đặt cách mặt phẳng dẫn nối đất vô hạn ($V = 0$) một khoảng $d$. Theo định lý tính duy nhất nghiệm của phương trình Poisson, trường điện trong nửa không gian thực giống hệt trường tạo bởi $q$ và một điện tích ảnh $q' = -q$ đặt đối xứng ở khoảng cách $d$ phía sau mặt phẳng.

Lực hút tĩnh điện giữa điện tích và mặt phẳng:

$$F = \frac{1}{4\pi\varepsilon_0} \frac{q^2}{(2d)^2} = \frac{q^2}{16\pi\varepsilon_0 d^2}$$

Năng lượng tương tác toàn phần bằng một nửa năng lượng tương tác giữa hai điện tích điểm cô lập: $W = -\frac{q^2}{16\pi\varepsilon_0 d}$.

## Hạt trong trường điện từ chéo nhau

Khi $\vec{E} \perp \vec{B}$, chuyển động của hạt là sự kết hợp giữa chuyển động tròn cyclotron và chuyển động trôi tịnh tiến với vận tốc trôi $v_{drift} = \frac{E}{B}$. Quỹ đạo chuyển động là đường cycloid.

**Lỗi thường gặp:**
- Tính lực ảnh điện bằng k*q^2 / d^2 thay vì chia cho (2d)^2 = 4d^2
- Quên thừa số 1/2 khi tính năng lượng tĩnh điện của điện tích ảnh so với hệ hai điện tích điểm thực

<sub>`lesson.physics.em-modern.phuong-phap-anh-dien-va-dien-tu-truong-cheo`</sub>

---

## Unit 2: Dynamics - Newton's Laws (AP Physics 1 Unit 2 / IB A.2 / CIE 9702 Topic 3-4)

### 1. Ba định luật Newton và giản đồ vật tự do
*Newton's three laws and free-body diagrams* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu được ba định luật Newton và nêu đúng phạm vi áp dụng của mỗi định luật
- Vẽ được giản đồ vật tự do cho một vật trong hệ nhiều vật
- Vận dụng được định luật II Newton dạng chiếu theo hai trục vuông góc

## Câu hỏi Newton trả lời

Trước Newton, người ta tin rằng muốn vật chuyển động phải liên tục đẩy nó. Newton đảo ngược câu hỏi: lực không duy trì chuyển động, lực làm **thay đổi** chuyển động.

- **Định luật I**: nếu $\sum\vec{F} = 0$ thì $\vec{v}$ không đổi. Đây đồng thời là định nghĩa hệ quy chiếu quán tính.
- **Định luật II**: $\sum\vec{F} = m\vec{a}$, hay tổng quát hơn $\sum\vec{F} = d\vec{p}/dt$. Gia tốc **cùng hướng với hợp lực**, không cùng hướng với vận tốc.
- **Định luật III**: $\vec{F}_{AB} = -\vec{F}_{BA}$.

## Giản đồ vật tự do - kỹ năng số một

Quy trình bốn bước dùng cho mọi bài động lực học:

1. Chọn **một** vật để khảo sát, tách khỏi mọi vật khác.
2. Vẽ mọi lực **tác dụng lên nó**: trọng lực, phản lực pháp tuyến, lực căng, ma sát, lực đẩy. Không vẽ lực mà nó tác dụng lên vật khác, cũng không vẽ "lực do chuyển động".
3. Chọn hệ trục sao cho gia tốc nằm dọc một trục.
4. Viết $\sum F_x = ma_x$ và $\sum F_y = ma_y$.

## Cái bẫy lớn nhất của định luật III

Quyển sách nằm trên bàn chịu trọng lực $\vec{P}$ và phản lực $\vec{N}$. Hai lực này **không** phải cặp lực - phản lực dù bằng nhau về độ lớn: chúng cùng đặt lên quyển sách và khác bản chất. Phản lực của $\vec{P}$ là lực sách hút Trái Đất; phản lực của $\vec{N}$ là lực sách nén mặt bàn. Kiểm tra nhanh: cặp lực - phản lực **luôn đặt lên hai vật khác nhau**.

## Phạm vi

Ba định luật đúng trong hệ quy chiếu quán tính, với tốc độ nhỏ so với tốc độ ánh sáng và vật ở thang vĩ mô. Trong hệ phi quán tính (thang máy đang tăng tốc, xe vào cua), muốn giữ dạng $\sum\vec{F} = m\vec{a}$ ta phải thêm lực quán tính.

**Lỗi thường gặp:**
- Vẽ thêm một "lực chuyển động" theo hướng vận tốc. Vận tốc không sinh ra lực; sau khi ném quả bóng, tay không còn tác dụng lực nào lên nó nữa, chỉ còn trọng lực.
- Coi trọng lực và phản lực pháp tuyến là cặp lực - phản lực. Chúng cùng đặt lên một vật, còn cặp lực - phản lực theo định luật III bắt buộc đặt lên hai vật khác nhau; nếu $N$ đúng là phản lực của $P$ thì chúng luôn bằng nhau, trong khi thực tế $N$ thay đổi khi thang máy tăng tốc.
- Mặc định $N = mg$ trong mọi tình huống. $N$ là ẩn số phải tìm từ phương trình chiếu theo phương thẳng đứng; nó thay đổi khi có lực chếch, khi mặt phẳng nghiêng, hoặc khi hệ có gia tốc thẳng đứng.

<sub>`lesson.physics.dong-luc-hoc-intl.ba-dinh-luat-newton-va-fbd`</sub>

---

### 2. Các loại lực cơ học và bản chất của chúng
*Types of mechanical forces and their nature* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân loại được các lực cơ học theo bản chất tiếp xúc hay tương tác từ xa
- Vận dụng được định luật Hooke cho lò xo và hệ lò xo ghép
- Giải thích được sự khác nhau giữa trọng lượng thật và trọng lượng biểu kiến

## Bốn tương tác, vài chục cái tên

Ở thang vĩ mô, mọi lực cơ học đều quy về hai nguồn gốc: **hấp dẫn** (trọng lực) và **điện từ** (mọi lực tiếp xúc). Lực căng dây, phản lực, ma sát, lực đàn hồi đều là biểu hiện vĩ mô của lực điện từ giữa các nguyên tử.

## Bảng nhận diện

| Lực | Hướng | Độ lớn |
|---|---|---|
| Trọng lực $\vec{P}$ | Thẳng đứng xuống | $mg$ |
| Pháp tuyến $\vec{N}$ | Vuông góc bề mặt, đẩy ra | Ẩn số, tìm từ phương trình |
| Lực căng $\vec{T}$ | Dọc dây, kéo về phía dây | Ẩn số; dây nhẹ vắt qua ròng rọc nhẹ nhẵn thì $T$ như nhau hai bên |
| Đàn hồi $\vec{F}_{dh}$ | Ngược chiều biến dạng | $k|\Delta l|$ |
| Ma sát $\vec{f}$ | Dọc bề mặt, cản trượt tương đối | Xem bài riêng |

## Định luật Hooke và giới hạn của nó

$$F = k\,|\Delta l|$$

Chỉ đúng trong **giới hạn đàn hồi**. Vượt quá, lò xo biến dạng dẻo và không trở lại chiều dài cũ. Ghép nối tiếp cho lò xo mềm hơn ($1/k = 1/k_1 + 1/k_2$), ghép song song cho cứng hơn ($k = k_1 + k_2$) — hãy nhớ bằng trực giác: nối tiếp thì tổng độ dãn cộng lại, song song thì tổng lực cộng lại.

## Cân chỉ cái gì

Cân lò xo trong thang máy chỉ **trọng lượng biểu kiến** $N$, không phải $mg$. Chiếu định luật II theo phương đứng:

$$N = m(g + a)$$

với $a$ dương khi gia tốc hướng lên. Thang máy đi lên nhanh dần: cân chỉ nhiều hơn. Cáp đứt, $a = -g$: cân chỉ 0 — đó chính là **trạng thái không trọng lượng**, xảy ra không phải vì hết trọng lực mà vì vật và giá đỡ rơi cùng gia tốc.

**Lỗi thường gặp:**
- Cho rằng khối lượng và trọng lượng là một. Khối lượng là đại lượng vô hướng đo bằng kg và không đổi khi mang lên Mặt Trăng; trọng lượng là lực đo bằng N và giảm khoảng 6 lần trên Mặt Trăng.
- Áp dụng $F = k\Delta l$ khi lò xo bị kéo quá giới hạn đàn hồi. Ngoài vùng đàn hồi, đồ thị $F$ theo $\Delta l$ cong đi và lò xo không trở lại chiều dài ban đầu, mọi tính toán dựa trên $k$ đều sai.
- Nghĩ phi hành gia trên trạm ISS không có trọng lực. Ở độ cao 400 km, $g$ vẫn còn khoảng 89 phần trăm giá trị mặt đất; họ không trọng lượng vì trạm và người cùng rơi tự do quanh Trái Đất, nên phản lực bằng 0.

<sub>`lesson.physics.dong-luc-hoc-intl.cac-loai-luc-co-hoc`</sub>

---

### 3. Ma sát nghỉ và ma sát trượt
*Static and kinetic friction* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được ma sát nghỉ với ma sát trượt qua điều kiện xuất hiện và cách tính độ lớn
- Vận dụng được bất đẳng thức ma sát nghỉ để xét điều kiện vật bắt đầu trượt
- Giải thích được vì sao độ lớn lực ma sát không phụ thuộc diện tích tiếp xúc biểu kiến

## Một lực biết tự điều chỉnh

Đẩy nhẹ chiếc tủ, nó không nhúc nhích: ma sát nghỉ đã cân bằng đúng bằng lực đẩy. Đẩy mạnh hơn, ma sát nghỉ tăng theo. Đến một ngưỡng, tủ bỗng trượt và lực cản **giảm xuống** — vì $\mu_k < \mu_s$. Đó là lí do vật lí của cảm giác "đẩy được rồi thì đẩy nhẹ hơn".

Biểu thức đúng phải viết dạng bất đẳng thức:

$$f_s \le \mu_s N \qquad\text{(chưa trượt)}$$
$$f_k = \mu_k N \qquad\text{(đang trượt)}$$

Dấu bằng ở dòng đầu **chỉ dùng đúng tại ngưỡng sắp trượt**. Đây là điểm mà đề AP và A-Level kiểm tra thường xuyên nhất.

## Vì sao không phụ thuộc diện tích

Bề mặt nhìn phẳng nhưng ở thang micro chỉ chạm nhau tại vài đỉnh nhấp nhô. Diện tích **tiếp xúc thực** tỉ lệ với áp lực $N$ chứ không tỉ lệ với diện tích biểu kiến: ép mạnh hơn thì các đỉnh bẹp ra và chạm nhiều hơn. Trải một viên gạch nằm hay dựng đứng đều cho cùng lực ma sát vì $N$ như nhau.

## Hệ số ma sát nói lên điều gì

$\mu$ không thứ nguyên, phụ thuộc **cặp vật liệu** chứ không phải một vật liệu. Thép trên thép khô cho $\mu_s \approx 0{,}7$; thép trên thép có dầu chỉ còn $0{,}05$. Với lốp cao su trên nhựa đường khô, $\mu_s$ có thể vượt 1, nên bất đẳng thức $\mu \le 1$ mà nhiều học sinh tưởng là quy luật thực ra không tồn tại.

## Ma sát không phải lúc nào cũng cản

Khi ta đi bộ, chân đạp về sau, ma sát nghỉ của mặt đất đẩy ta **về trước**: đây là lực phát động. Bánh xe lăn không trượt cũng vậy. Vì điểm tiếp xúc không trượt nên ma sát nghỉ **không sinh công**, khác hẳn ma sát trượt luôn tiêu tán năng lượng thành nhiệt.

**Lỗi thường gặp:**
- Luôn tính ma sát nghỉ bằng $\mu_s N$. Công thức đó chỉ cho giá trị **cực đại**; khi vật còn đứng yên, ma sát nghỉ bằng đúng thành phần ngoại lực song song mặt tiếp xúc, có thể nhỏ hơn nhiều.
- Cho rằng đặt vật nằm xuống thì ma sát lớn hơn vì diện tích lớn hơn. Lực ma sát chỉ phụ thuộc $\mu$ và $N$; diện tích tiếp xúc thực ở thang vi mô tỉ lệ với $N$ nên diện tích biểu kiến bị triệt tiêu khỏi công thức.
- Luôn coi ma sát là lực cản chuyển động. Ma sát nghỉ giữa bàn chân và mặt đất, hay giữa lốp và đường khi xe tăng tốc, chính là lực phát động đẩy vật về phía trước.

<sub>`lesson.physics.dong-luc-hoc-intl.ma-sat-tinh-va-ma-sat-dong`</sub>

---

### 4. Hệ nhiều vật nối bằng dây và ròng rọc
*Connected bodies, strings and pulleys* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được phương pháp hệ và phương pháp tách vật để giải bài toán nhiều vật
- Xác định được điều kiện ràng buộc về gia tốc của các vật nối bằng dây không dãn
- Giải thích được vì sao lực căng hai bên ròng rọc bằng nhau chỉ khi ròng rọc nhẹ và nhẵn

## Hai công cụ, dùng phối hợp

Bài toán hệ vật luôn giải theo hai bước bổ trợ nhau:

1. **Phương pháp hệ** để tìm gia tốc chung: gộp mọi vật thành một, nội lực (lực căng, lực tương tác giữa các vật) tự triệt tiêu theo định luật III.
2. **Phương pháp tách vật** để tìm lực căng: viết định luật II riêng cho một vật, thay $a$ vừa tìm được.

Gộp trước để tìm $a$ nhanh, tách sau để tìm $T$ — thứ tự này tiết kiệm rất nhiều công.

## Điều kiện ràng buộc

Dây **không dãn** buộc các vật có cùng độ lớn gia tốc. Nếu dây vắt qua ròng rọc, hai vật chuyển động ngược chiều nhau nhưng cùng độ lớn $a$. Nếu hệ có ròng rọc động, ràng buộc phức tạp hơn: vật treo ở ròng rọc động có gia tốc chỉ bằng nửa gia tốc của đầu dây tự do.

## Máy Atwood

Hai vật $m_1 > m_2$ treo hai đầu dây qua ròng rọc cố định. Phương pháp hệ: ngoại lực gây chuyển động là hiệu trọng lượng.

$$a = \frac{(m_1 - m_2)g}{m_1 + m_2}, \qquad T = \frac{2m_1m_2}{m_1+m_2}g$$

Kiểm tra bằng trực giác: khi $m_1 = m_2$ thì $a = 0$ và $T = mg$; khi $m_2 \to 0$ thì $a \to g$ (rơi tự do) và $T \to 0$. Chú ý $T$ luôn nằm **giữa** $m_2 g$ và $m_1 g$ — không bao giờ bằng $m_1 g$, vì nếu bằng thì $m_1$ đứng yên.

## Khi nào giả thiết sụp đổ

"Lực căng như nhau ở hai bên" chỉ đúng nếu ròng rọc **khối lượng không đáng kể và quay không ma sát**. Ròng rọc có mômen quán tính $I$ cần chênh lệch lực căng để tạo mômen quay nó: $(T_1 - T_2)R = I\alpha$. Đây là bài toán chuẩn của AP Physics C, sẽ gặp lại ở phần chuyển động quay.

**Lỗi thường gặp:**
- Cho rằng lực căng dây bằng trọng lượng vật treo. Nếu $T = m_2 g$ thì vật treo có hợp lực bằng 0 và đứng yên; hệ đang có gia tốc nên $T$ bắt buộc phải nhỏ hơn $m_2 g$ khi vật đi xuống.
- Đưa lực căng vào phương trình của phương pháp hệ. Lực căng là cặp nội lực trực đối theo định luật III, chúng triệt tiêu khi gộp hệ; giữ lại là tính trùng.
- Quên kiểm tra hệ có chuyển động hay không trước khi áp dụng công thức ma sát trượt. Nếu trọng lượng vật treo nhỏ hơn ma sát nghỉ cực đại thì cả hệ đứng yên và mọi công thức gia tốc trở nên vô nghĩa.

<sub>`lesson.physics.dong-luc-hoc-intl.he-vat-day-va-rong-roc`</sub>

---

### 5. Bài toán mặt phẳng nghiêng
*The inclined plane* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân tích được trọng lực thành hai thành phần song song và vuông góc mặt nghiêng
- Tính được gia tốc của vật trượt trên mặt nghiêng có và không có ma sát
- Xác định được góc nghiêng tới hạn để vật bắt đầu trượt

## Chọn trục là nửa lời giải

Sai lầm chí mạng của bài mặt phẳng nghiêng là dùng trục ngang - đứng thông thường. Vật trượt **dọc mặt nghiêng**, nên hãy quay hệ trục: $Ox$ dọc mặt nghiêng, $Oy$ vuông góc mặt nghiêng. Khi đó $a_y = 0$ và bài toán chỉ còn một chiều.

Trọng lực khi ấy phải tách:

$$P_x = mg\sin\theta \quad(\text{gây trượt}), \qquad P_y = mg\cos\theta \quad(\text{ép vào mặt})$$

Mẹo nhớ dấu: khi $\theta \to 0$ (mặt nằm ngang) thì $P_x \to 0$ và $P_y \to mg$ — đúng trực giác. Nếu ai đó viết ngược lại ($\cos$ cho thành phần trượt), phép thử này lộ ra ngay.

## Bốn tình huống

Quy ước cho bảng dưới đây: mỗi dòng lấy chiều dương là chiều chuyển động của vật, nên dấu âm nghĩa là gia tốc cản lại chuyển động.

| Trường hợp | Kết quả |
|---|---|
| Nhẵn | $a = g\sin\theta$, không phụ thuộc $m$ |
| Trượt xuống có ma sát | $a = g(\sin\theta - \mu_k\cos\theta)$ |
| Trượt lên (đã có vận tốc lên) | $a = -g(\sin\theta + \mu_k\cos\theta)$ |
| Đứng yên | $mg\sin\theta \le \mu_s mg\cos\theta$ |

Bất đẳng thức cuối rút gọn thành $\tan\theta \le \mu_s$, tức **điều kiện không trượt không phụ thuộc khối lượng**. Đổ thêm cát lên khối gỗ cũng không giúp nó bám tốt hơn, vì cả lực gây trượt lẫn ma sát đều tăng theo cùng tỉ lệ.

## Ứng dụng đo hệ số ma sát

Đặt vật lên ván, nâng dần đầu ván tới khi vật bắt đầu trượt, đo góc $\theta_c$. Khi đó $\mu_s = \tan\theta_c$. Bài thực hành này có mặt trong cả IB internal assessment lẫn Cambridge 9702 Paper 3, và ưu điểm của nó là không cần lực kế.

## Chú ý về vận tốc và gia tốc

Vật đi lên chậm dần rồi đi xuống nhanh dần: hai chặng có **độ lớn gia tốc khác nhau** vì ma sát đổi chiều còn trọng lực thì không. Đây là lí do vật quay về chân dốc với tốc độ nhỏ hơn tốc độ ban đầu.

**Lỗi thường gặp:**
- Viết $N = mg$ trên mặt nghiêng. Chỉ thành phần $mg\cos\theta$ ép vào mặt phẳng; lấy $N = mg$ làm lực ma sát tính ra lớn hơn thực tế và gia tốc bị nhỏ đi.
- Đổi chỗ sin và cos. Kiểm tra bằng trường hợp giới hạn: mặt phẳng nằm ngang ($\theta = 0$) phải cho thành phần gây trượt bằng 0, mà $\sin 0 = 0$ nên thành phần trượt phải đi với sin.
- Dùng cùng một công thức gia tốc cho cả chặng đi lên và chặng đi xuống. Lực ma sát luôn ngược chiều vận tốc, nên khi đi lên nó cộng vào với thành phần trọng lực, khi đi xuống nó trừ đi.

<sub>`lesson.physics.dong-luc-hoc-intl.mat-phang-nghieng`</sub>

---

### 6. Lực cản của chất lưu và tốc độ giới hạn
*Fluid resistance and terminal velocity* · THPT (lớp 10-12) · ap, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Phân biệt được hai chế độ lực cản tỉ lệ bậc nhất và tỉ lệ bình phương tốc độ
- Chứng minh được sự tồn tại của tốc độ giới hạn từ phương trình định luật II Newton
- Phân tích được dạng đồ thị vận tốc - thời gian của vật rơi trong không khí

## Vì sao hạt mưa không giết người

Rơi tự do từ 2 km sẽ cho tốc độ chạm đất khoảng 200 m/s. Thực tế hạt mưa chạm đất chỉ khoảng 9 m/s. Nguyên nhân: **lực cản của không khí tăng theo tốc độ**, đến một lúc nó cân bằng với trọng lực.

## Hai chế độ

- Vật nhỏ, tốc độ thấp (giọt sương, viên bi trong dầu): $F_{c} = bv$, chảy tầng. Với hình cầu, định luật Stokes cho $b = 6\pi\eta r$.
- Vật lớn, tốc độ cao (người nhảy dù, ô tô): $F_{c} = kv^{2}$, chảy rối.

Số Reynolds quyết định chế độ nào chiếm ưu thế. Lưu ý phạm vi: AP Physics C Mechanics chỉ yêu cầu dạng $F_c = -bv$ hoặc $-cv^{2}$, còn CIE 9702 chỉ yêu cầu mô tả định tính tốc độ giới hạn; định luật Stokes và số Reynolds ở đây là **nội dung mở rộng**.

## Cơ chế tiến tới tốc độ giới hạn

Viết định luật II theo chiều rơi:

$$m\frac{dv}{dt} = mg - bv$$

Lúc $t = 0$, $v = 0$ nên $a = g$: vật rơi như rơi tự do. Khi $v$ tăng, lực cản tăng, $a$ **giảm dần**. Khi $a = 0$:

$$v_{T} = \frac{mg}{b} \qquad\text{hoặc}\qquad v_{T} = \sqrt{\frac{mg}{k}}\ \text{(chế độ bình phương)}$$

Nghiệm của phương trình vi phân là $v(t) = v_T\left(1 - e^{-t/\tau}\right)$ với $\tau = m/b$. Đồ thị $v$-$t$ có dạng cong tiệm cận: dốc đứng lúc đầu (độ dốc bằng $g$), rồi thoải dần và **tiệm cận** đường nằm ngang $v = v_T$ mà không bao giờ cắt nó.

## Đọc được gì từ công thức

Vì $v_T \propto m$ (chế độ tuyến tính) hoặc $v_T \propto \sqrt{m/A}$ (chế độ bình phương), vật nặng và gọn có tốc độ giới hạn lớn. Người nhảy dù bung dù làm $A$ tăng vài chục lần, $v_T$ giảm từ khoảng 55 m/s xuống khoảng 5 m/s. Đó là toàn bộ nguyên lí của chiếc dù.

Lưu ý: **bộ SUVAT hoàn toàn không dùng được ở đây** vì gia tốc thay đổi liên tục.

**Lỗi thường gặp:**
- Áp dụng công thức SUVAT cho vật rơi có lực cản. Gia tốc giảm dần từ $g$ về 0 nên đồ thị $v$-$t$ là đường cong, mọi hệ thức dẫn từ giả thiết gia tốc không đổi đều sai.
- Cho rằng khi đạt tốc độ giới hạn thì không còn lực nào tác dụng. Trọng lực và lực cản vẫn tồn tại và đều lớn; chỉ có **hợp lực** bằng 0, đúng theo định luật I Newton.
- Quên lực đẩy Archimedes khi vật rơi trong chất lỏng. Trong không khí lực này nhỏ nên bỏ qua được, nhưng trong dầu hay nước nó chiếm phần đáng kể của trọng lực và làm tốc độ giới hạn giảm rõ rệt.

<sub>`lesson.physics.dong-luc-hoc-intl.luc-can-va-toc-do-gioi-han`</sub>

---

## Unit 2: Tụ điện và điện môi - Capacitance and Dielectrics

### 1. Điện dung và tụ điện phẳng
*Capacitance and the parallel-plate capacitor* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu được định nghĩa điện dung và giải thích vì sao điện dung không phụ thuộc điện tích đã tích
- Vận dụng được công thức điện dung của tụ phẳng để phân tích ảnh hưởng của diện tích bản và khoảng cách
- Xác định được hiệu điện thế giới hạn của tụ dựa trên cường độ điện trường đánh thủng

## Điện dung là gì và không phải là gì

Đặt hai bản kim loại đối diện, nối vào nguồn: bản này tích $+Q$, bản kia $-Q$, giữa chúng có hiệu điện thế $U$. Thực nghiệm cho thấy $Q$ luôn tỉ lệ thuận với $U$, nên tỉ số

$$C = \frac{Q}{U}$$

là một hằng số của riêng hệ vật dẫn đó. Đây là điểm hay bị hiểu nhầm: công thức có $Q$ và $U$ nhưng $C$ **không phụ thuộc** vào chúng, giống như $R = U/I$ không phụ thuộc $U$ với vật dẫn ohm. $C$ chỉ do hình học và điện môi quyết định.

## Tụ điện phẳng

Với hai bản diện tích $S$, cách nhau $d$ (nhỏ so với kích thước bản, để bỏ qua hiệu ứng mép):

$$C = \frac{\varepsilon_0\varepsilon_r S}{d}$$

Có thể dẫn ra kết quả này chỉ bằng những gì đã học: từ Gauss, $E = \sigma/\varepsilon_0 = Q/(\varepsilon_0 S)$; trường đều nên $U = Ed = Qd/(\varepsilon_0 S)$; chia ra được $C$. Việc dẫn được công thức quan trọng hơn việc nhớ nó, vì nó cho thấy ba cách tăng điện dung: tăng $S$, giảm $d$, hoặc chèn điện môi.

## Vì sao không thể giảm $d$ mãi

Giảm $d$ làm $C$ tăng, nhưng ở cùng $U$ thì $E = U/d$ cũng tăng. Khi $E$ vượt cường độ đánh thủng $E_{\max}$ của lớp điện môi (không khí khoảng $3\times10^{6}$ V/m), chất cách điện bị ion hoá, tia lửa phóng qua và tụ hỏng. Vậy

$$U_{\max} = E_{\max} d$$

Đây là ràng buộc kĩ thuật thật sự: mọi tụ thương mại đều ghi kèm điện áp làm việc, và vượt quá nó thì trị số điện dung ghi trên vỏ trở nên vô nghĩa.

## Quả cầu cô lập cũng là một tụ

Một quả cầu dẫn bán kính $R$ đứng riêng cũng có điện dung $C = 4\pi\varepsilon_0 R$, với "bản thứ hai" là vô cùng. Con số cho thấy fara là đơn vị khổng lồ: muốn $C = 1$ F thì $R$ phải cỡ $9\times10^{9}$ m, lớn hơn Mặt Trời. Vì thế tụ thực tế đo bằng μF, nF, pF.

**Lỗi thường gặp:**
- Nghĩ rằng nạp thêm điện tích sẽ làm điện dung tăng — sai vì $Q$ và $U$ tăng cùng tỉ lệ, tỉ số không đổi; $C$ chỉ đổi khi thay đổi hình học hoặc điện môi.
- Áp dụng $C = \varepsilon_0 S/d$ cho hai bản đặt xa nhau — sai vì khi $d$ so sánh được với kích thước bản, đường sức phình ra ở mép, trường không còn đều và công thức mất hiệu lực.
- Lấy $U_{\max}$ từ trị số điện dung — sai vì điện dung không chứa thông tin về độ bền điện môi; giới hạn điện áp được quyết định bởi $E_{\max}$ và $d$.

<sub>`lesson.physics.tu-dien.dien-dung-va-tu-dien-phang`</sub>

---

### 2. Ghép tụ điện và năng lượng điện trường
*Capacitor combinations and stored energy* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Chứng minh được công thức điện dung tương đương của bộ tụ ghép nối tiếp và song song
- Tính được năng lượng tích trữ trong tụ điện bằng ba dạng biểu thức tương đương
- Giải thích được ý nghĩa của mật độ năng lượng điện trường

## Ghép tụ: đảo ngược trực giác về điện trở

**Song song.** Hai bản dương nối chung, hai bản âm nối chung nên mọi tụ có cùng $U$. Điện tích cộng lại: $Q = Q_1 + Q_2$, chia cho $U$:

$$C_{ss} = C_1 + C_2 + \dots$$

Hiểu bản chất: ghép song song tương đương với việc tăng tổng diện tích bản.

**Nối tiếp.** Phần giữa bị cô lập nên chỉ có thể phân bố lại điện tích, tổng vẫn bằng 0; hệ quả là mọi tụ mang **cùng điện tích** $Q$. Hiệu điện thế cộng lại:

$$\frac{1}{C_{nt}} = \frac{1}{C_1} + \frac{1}{C_2} + \dots$$

Ghép nối tiếp tương đương với việc tăng khoảng cách $d$, nên $C_{nt}$ luôn **nhỏ hơn** tụ nhỏ nhất trong bộ. Đây là điểm ngược với điện trở, và là mẹo kiểm tra kết quả nhanh nhất.

## Năng lượng tích trữ

Nạp tụ không phải chuyển ngay $Q$ ở điện áp $U$: điện tích đầu tiên đi qua khi $u\approx 0$, điện tích cuối cùng mới phải vượt $U$. Cộng dồn công từng phần $dW = u\,dq = (q/C)dq$ cho

$$W = \frac{Q^2}{2C} = \frac{1}{2}CU^2 = \frac{1}{2}QU$$

Hệ số $1/2$ chính là dấu vết của quá trình nạp dần này, không phải một hằng số tuỳ tiện.

## Năng lượng nằm ở đâu

Thay $C = \varepsilon_0 S/d$ và $U = Ed$ vào $W = \frac{1}{2}CU^2$:

$$W = \frac{1}{2}\varepsilon_0 E^2 \cdot (Sd) \;\Rightarrow\; u = \frac{W}{V} = \frac{1}{2}\varepsilon_0 E^2$$

Kết quả nói rằng năng lượng phân bố trong **không gian có trường**, không phải "nằm trên bản tụ". Cách nhìn này về sau tổng quát cho mọi điện trường và là bước chuẩn bị cho ý tưởng sóng điện từ mang năng lượng.

## Khi nạp tụ qua điện trở

Nguồn cung cấp $W_{ng} = QU = CU^2$, tụ chỉ giữ được $\frac{1}{2}CU^2$. Đúng một nửa biến thành nhiệt trên điện trở, **bất kể $R$ lớn hay nhỏ**. Đây là kết quả đáng nhớ vì nó cho thấy giới hạn hiệu suất của việc nạp tụ bằng nguồn điện áp không đổi.

**Lỗi thường gặp:**
- Dùng công thức cộng trực tiếp cho tụ nối tiếp vì quen với điện trở — sai vì tụ nối tiếp có cùng điện tích còn điện áp cộng lại, dẫn tới nghịch đảo cộng nghịch đảo; kết quả đúng phải nhỏ hơn tụ bé nhất.
- Áp dụng $U$ của cả bộ cho từng tụ trong nhánh nối tiếp — sai vì điện áp phân chia tỉ lệ nghịch với điện dung, tụ nhỏ lại gánh điện áp lớn hơn.
- Quên hệ số $1/2$ trong $W = \frac{1}{2}CU^2$ — sai vì trong quá trình nạp, hiệu điện thế tăng dần từ 0 tới $U$, công trung bình chỉ bằng nửa $QU$.

<sub>`lesson.physics.tu-dien.ghep-tu-va-nang-luong`</sub>

---

### 3. Điện môi trong tụ điện
*Dielectrics in capacitors* · THPT (lớp 10-12) · ap, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được cơ chế phân cực điện môi và vì sao nó làm giảm điện trường trong tụ
- Phân tích được hai trường hợp đưa điện môi vào tụ: tụ cô lập và tụ vẫn nối nguồn
- So sánh được sự thay đổi của $Q$, $U$, $E$ và $W$ trong hai trường hợp đó

## Cơ chế vi mô

Điện môi không có electron tự do, nhưng phân tử của nó vẫn phản ứng với điện trường: phân tử phân cực (như nước) quay theo trường, phân tử không phân cực bị kéo giãn thành lưỡng cực cảm ứng. Kết quả là bên trong khối chất, các lưỡng cực bù nhau, chỉ còn lại lớp điện tích liên kết ở hai mặt — trái dấu với bản tụ kề nó.

Lớp điện tích liên kết ấy tạo ra một điện trường **ngược chiều** với trường ngoài. Trường tổng hợp giảm đi $\kappa$ lần:

$$E = \frac{E_0}{\kappa}$$

Giảm $E$ với cùng $Q$ nghĩa là giảm $U$, tức tăng $C$:

$$C = \kappa C_0 = \frac{\kappa\varepsilon_0 S}{d}$$

Điện môi còn phục vụ hai mục đích thực tế nữa: giữ hai bản cách nhau đúng khoảng cách rất nhỏ, và nâng cường độ đánh thủng lên trên mức của không khí.

## Hai kịch bản phải phân biệt rạch ròi

Câu hỏi quyết định luôn là: **đại lượng nào bị giữ cố định?**

**Kịch bản 1 - tụ đã ngắt khỏi nguồn (cô lập).** Điện tích không đi đâu được nên $Q$ = const.

$$C\uparrow \kappa \text{ lần},\quad U = \frac{Q}{C}\downarrow \kappa,\quad E\downarrow \kappa,\quad W = \frac{Q^2}{2C}\downarrow \kappa$$

Năng lượng giảm — phần thiếu chuyển thành công: khối điện môi bị **hút vào** giữa hai bản.

**Kịch bản 2 - tụ vẫn nối nguồn.** Nguồn ghim $U$ = const.

$$C\uparrow \kappa,\quad Q = CU\uparrow \kappa,\quad E = \frac{U}{d} \text{ không đổi},\quad W = \frac{1}{2}CU^2\uparrow \kappa$$

Năng lượng tăng vì nguồn bơm thêm điện tích vào tụ.

## Vì sao hay nhầm

Hai kịch bản cho kết luận **ngược nhau** về $U$, $E$ và $W$. Học sinh thường học thuộc một bộ kết quả rồi áp cho cả hai. Cách chữa duy nhất là mỗi lần đều tự hỏi "tụ còn nối nguồn không?" trước khi viết bất kì công thức nào, rồi bám vào đại lượng bất biến để suy ra phần còn lại qua $Q = CU$.

**Lỗi thường gặp:**
- Cho rằng đưa điện môi vào luôn làm giảm hiệu điện thế — sai vì kết luận này chỉ đúng khi tụ đã ngắt nguồn; nếu còn nối nguồn thì nguồn giữ $U$ cố định và chính điện tích mới là đại lượng thay đổi.
- Nghĩ điện môi làm giảm điện trường trong mọi trường hợp — sai vì khi $U$ và $d$ đều cố định thì $E = U/d$ không đổi, điện môi chỉ khiến bản tụ tích thêm điện tích tự do để bù phần điện tích liên kết.
- Coi điện tích liên kết trên mặt điện môi là điện tích tự do có thể chạy trong mạch — sai vì chúng gắn với phân tử, chỉ dịch chuyển ở cỡ kích thước phân tử và không tạo thành dòng điện dẫn.

<sub>`lesson.physics.tu-dien.dien-moi-trong-tu-dien`</sub>

---

### 4. Mạch RC: quá trình nạp và phóng điện
*RC circuits: charging and discharging* · THPT (lớp 10-12) · ap, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Thiết lập được phương trình vi phân của mạch RC nối tiếp từ định luật Kirchhoff
- Vận dụng được nghiệm hàm mũ để tính điện tích, dòng điện và hiệu điện thế theo thời gian
- Giải thích được ý nghĩa vật lí của hằng số thời gian $\tau = RC$ và thời gian bán phóng

## Vì sao dòng điện không đổi không giải quyết được bài toán này

Khi đóng khoá nối nguồn $\mathcal{E}$ với $R$ và $C$ nối tiếp, tụ chưa tích điện nên không cản trở gì: dòng ban đầu bằng $\mathcal{E}/R$, đúng như không có tụ. Nhưng điện tích tích lại tạo ra điện áp ngược, làm dòng giảm dần, làm điện tích tăng chậm hơn... Nói cách khác, tốc độ biến thiên phụ thuộc chính giá trị hiện tại — dấu hiệu của một phương trình vi phân.

Áp dụng định luật vòng Kirchhoff với $i = dq/dt$:

$$\mathcal{E} = iR + \frac{q}{C} \;\Longrightarrow\; R\frac{dq}{dt} + \frac{q}{C} = \mathcal{E}$$

## Nghiệm và cách đọc

**Nạp** (tụ ban đầu rỗng):

$$q(t) = Q_0\left(1 - e^{-t/RC}\right),\qquad i(t) = \frac{\mathcal{E}}{R}e^{-t/RC}$$

với $Q_0 = C\mathcal{E}$. Điện áp trên tụ đi lên theo hàm mũ bão hoà, còn dòng đi xuống theo hàm mũ.

**Phóng** (nối tụ đã nạp qua $R$):

$$q(t) = Q_0 e^{-t/RC},\qquad i(t) = \frac{Q_0}{RC}e^{-t/RC}$$

## Hằng số thời gian nói gì

$\tau = RC$ đo bằng giây (ôm × fara = giây). Nó là thước đo "độ ì" của mạch:

| Thời gian | Tỉ lệ còn lại (phóng) |
|---|---|
| $\tau$ | 37% |
| $2\tau$ | 14% |
| $3\tau$ | 5% |
| $5\tau$ | dưới 1% |

Quy ước kĩ thuật: sau $5\tau$ coi như quá trình đã kết thúc. Đồ thị hàm mũ không bao giờ chạm trục hoành về mặt toán học, nhưng về mặt vật lí thì điện tích còn lại nhỏ hơn cả điện tích nguyên tố.

Một mẹo thực nghiệm quan trọng: vẽ $\ln q$ theo $t$ ta được đường thẳng có hệ số góc $-1/RC$. Đây là cách đo $\tau$ chính xác nhất trong phòng thí nghiệm, vì nó dùng toàn bộ số liệu chứ không chỉ một điểm.

## Ở trạng thái ổn định

Sau thời gian dài trong mạch một chiều, $i = 0$ qua nhánh có tụ: **tụ chặn dòng một chiều**. Khi giải mạch phức tạp ở chế độ dừng, thay mọi tụ bằng chỗ hở mạch rồi tính, sau đó lấy hiệu điện thế hai đầu chỗ hở để suy ra điện tích trên tụ.

**Lỗi thường gặp:**
- Cho rằng sau thời gian $\tau$ tụ phóng hết — sai vì hàm mũ chỉ giảm còn 37%; phải tới khoảng $5\tau$ mới coi như hết theo tiêu chuẩn kĩ thuật.
- Dùng cùng hằng số thời gian cho điện tích và cho năng lượng — sai vì năng lượng tỉ lệ với bình phương điện tích nên số mũ nhân đôi, năng lượng suy giảm nhanh gấp đôi.
- Áp dụng $I = \mathcal{E}/R$ cho mọi thời điểm trong quá trình nạp — sai vì khi tụ đã tích điện, điện áp trên tụ trừ bớt vào điện áp đặt lên điện trở, dòng giảm dần về 0.

<sub>`lesson.physics.tu-dien.mach-rc-nap-va-phong`</sub>

---

## Unit 3: Circular Motion (AP Physics 1 Unit 2 / IB A.2 / CIE 9702 Topic 12)

### 1. Động học chuyển động tròn đều và gia tốc hướng tâm
*Kinematics of uniform circular motion and centripetal acceleration* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được mối liên hệ giữa tốc độ dài, tốc độ góc, chu kì và tần số
- Chứng minh được công thức gia tốc hướng tâm bằng phương pháp giản đồ vectơ vận tốc
- Giải thích được vì sao chuyển động tròn đều vẫn là chuyển động có gia tốc

## Đều mà vẫn có gia tốc

Chuyển động tròn đều có **tốc độ** không đổi nhưng **vận tốc** thì đổi liên tục vì hướng thay đổi từng khoảnh khắc. Gia tốc là tốc độ biến thiên của vectơ vận tốc, nên nó khác 0. Đây là chỗ mà ngôn ngữ đời thường ("đều" = "không đổi") đánh lừa trực giác.

## Bộ liên hệ cơ bản

$$\omega = \frac{2\pi}{T} = 2\pi f, \qquad v = \omega r$$

Từ đó

$$a_c = \frac{v^{2}}{r} = \omega^{2} r = \frac{4\pi^{2} r}{T^{2}}$$

Ba dạng của $a_c$ đều có mặt trên bảng công thức IB; chọn dạng nào tuỳ vào đề cho $v$, $\omega$ hay $T$.

## Vì sao gia tốc hướng vào tâm

Vẽ hai vectơ vận tốc tại hai thời điểm cách nhau $\Delta t$ nhỏ. Chúng có cùng độ lớn $v$ nhưng lệch nhau góc $\Delta\theta$. Hiệu $\Delta\vec{v}$ là cạnh đáy của tam giác cân, có độ lớn $v\Delta\theta$ và **hướng vào tâm** khi $\Delta\theta$ rất nhỏ. Vậy

$$a = \frac{|\Delta\vec{v}|}{\Delta t} = v\frac{\Delta\theta}{\Delta t} = v\omega = \frac{v^{2}}{r}$$

Cách chứng minh này không cần giải tích, nên dùng được cả ở AP Physics 1 lẫn IB SL.

## Khi tốc độ cũng thay đổi

Nếu vật vừa quay vừa tăng tốc (ô tô vào cua có đạp ga), gia tốc có hai thành phần vuông góc:

$$\vec{a} = \vec{a}_t + \vec{a}_n, \qquad a = \sqrt{a_t^{2} + a_c^{2}}$$

Thành phần hướng tâm bẻ hướng, thành phần tiếp tuyến đổi tốc độ. Chỉ khi $a_t = 0$ mới có chuyển động tròn đều.

**Lỗi thường gặp:**
- Cho rằng chuyển động tròn đều không có gia tốc vì tốc độ không đổi. Gia tốc đo sự biến thiên của **vectơ** vận tốc; hướng đổi liên tục nên gia tốc khác 0 mọi lúc.
- Dùng độ thay vì radian khi tính $v = \omega r$. Hệ thức này chỉ đúng khi góc đo bằng radian, vì độ dài cung $s = r\theta$ được định nghĩa với radian.
- Nhầm gia tốc hướng tâm là một loại lực riêng. Hướng tâm là **tên gọi vai trò** của hợp lực đã có sẵn (trọng lực, lực căng, ma sát), không phải một lực mới cần thêm vào giản đồ vật tự do.

<sub>`lesson.physics.chuyen-dong-tron-intl.dong-hoc-chuyen-dong-tron-deu`</sub>

---

### 2. Lực hướng tâm: vòng xiếc, cầu vồng lên và đường cong nghiêng
*Centripetal force: vertical loops, humpback bridges and banked curves* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Xác định được lực nào đóng vai trò lực hướng tâm trong từng tình huống cụ thể
- Tính được tốc độ tối thiểu để vật qua được điểm cao nhất của vòng xiếc
- Vận dụng được điều kiện vào cua an toàn trên đường cong nghiêng có và không có ma sát

## Quy trình ba bước, đúng cho mọi bài

1. Vẽ giản đồ vật tự do với **các lực thực**: trọng lực, phản lực, lực căng, ma sát.
2. Chọn trục hướng vào tâm là chiều dương.
3. Viết $\sum F_{\text{hướng tâm}} = \dfrac{mv^{2}}{r}$.

Tuyệt đối không vẽ thêm mũi tên "lực hướng tâm" vào giản đồ — đó là kết quả, không phải nguyên nhân.

## Vòng xiếc thẳng đứng

Tại **điểm cao nhất**, cả trọng lực lẫn phản lực đều hướng xuống, tức đều hướng vào tâm:

$$mg + N = \frac{mv^{2}}{r}$$

Vật vẫn bám mặt trong khi $N \ge 0$, tức $v \ge \sqrt{gr}$. Tại tốc độ tối thiểu này, người ngồi trong tàu lượn cảm thấy "không trọng lượng" vì ghế không đẩy vào lưng nữa.

Tại **điểm thấp nhất**, phản lực hướng lên còn trọng lực hướng xuống, tâm ở trên:

$$N - mg = \frac{mv^{2}}{r} \Rightarrow N = mg + \frac{mv^{2}}{r} > mg$$

Đó là cảm giác bị ép xuống ghế ở đáy vòng.

## Cầu vồng lên và cầu võng xuống

Cầu vồng lên: tâm ở dưới, $N = mg - mv^{2}/r < mg$. Xe chạy đủ nhanh có thể làm $N = 0$ và bay khỏi mặt cầu tại $v = \sqrt{gr}$.
Cầu võng xuống: tâm ở trên, $N = mg + mv^{2}/r > mg$, cầu chịu tải nặng hơn.

## Đường cong nghiêng

Trên mặt nghiêng nhẵn góc $\theta$, chiếu phản lực $N$: thành phần đứng $N\cos\theta = mg$, thành phần ngang $N\sin\theta = mv^{2}/r$. Chia hai vế:

$$\tan\theta = \frac{v^{2}}{gr} \Rightarrow v = \sqrt{gr\tan\theta}$$

Tốc độ thiết kế **không phụ thuộc khối lượng**, nên đường cong nghiêng phục vụ được cả xe máy lẫn xe tải. Có thêm ma sát, tốc độ an toàn nằm trong một khoảng chứ không phải một giá trị.

**Lỗi thường gặp:**
- Thêm "lực hướng tâm" vào giản đồ vật tự do bên cạnh các lực thực. Làm vậy là tính hai lần cùng một thứ; lực hướng tâm chính là tổng hình chiếu của các lực thực lên phương bán kính.
- Vẽ "lực li tâm" hướng ra ngoài trong hệ quy chiếu mặt đất. Lực li tâm chỉ tồn tại trong hệ quy chiếu quay (phi quán tính); trong hệ quán tính, cảm giác bị văng ra là do quán tính chứ không do lực nào.
- Dùng cùng một phương trình cho điểm cao nhất và điểm thấp nhất. Hướng vào tâm đảo ngược giữa hai vị trí, nên dấu của trọng lực trong phương trình cũng phải đảo theo.

<sub>`lesson.physics.chuyen-dong-tron-intl.luc-huong-tam-va-ung-dung`</sub>

---

## Unit 3: Dòng điện và mạch điện - Current and Circuits

### 1. Mô hình dòng electron, mật độ dòng và điện trở suất
*Drift model of current, current density and resistivity* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được sự khác nhau giữa tốc độ trôi của electron và tốc độ lan truyền tín hiệu điện
- Vận dụng được công thức $I = nAve$ để tính tốc độ trôi trong dây dẫn kim loại
- Phân tích được sự phụ thuộc của điện trở suất vào nhiệt độ ở kim loại và ở chất bán dẫn

## Một nghịch lí mở đầu

Bật công tắc, đèn sáng gần như tức thì. Nhưng tính toán cho thấy electron trong dây đồng chỉ trôi với tốc độ cỡ **0,1 mm/s** — mất hơn hai giờ để đi hết một mét dây. Vậy tín hiệu truyền bằng cách nào?

Câu trả lời: cái lan truyền nhanh (gần tốc độ ánh sáng) là **điện trường** dọc dây, chứ không phải bản thân electron. Điện trường lập tức tác động lên electron ở mọi vị trí, kể cả electron sẵn có trong dây tóc bóng đèn. Ví von quen thuộc: đẩy một đầu ống nước đã đầy thì nước chảy ra ở đầu kia ngay, dù phân tử nước ở đầu này chưa đi tới đâu cả.

## Mô hình định lượng

Trong đoạn dây tiết diện $A$, mật độ hạt tải $n$, mỗi hạt mang điện $q$ và trôi với $v_d$:

$$I = nAqv_d, \qquad J = \frac{I}{A} = nqv_d$$

Với đồng, $n \approx 8{,}5\times10^{28}$ electron/m³ — con số khổng lồ này chính là lí do $v_d$ nhỏ đến vậy dù dòng điện đáng kể.

Giữa hai va chạm với ion mạng, electron được điện trường gia tốc; sau va chạm nó mất phương hướng. Kết quả trung bình là một vận tốc có hướng không đổi tỉ lệ với $E$ — chính đây là gốc vi mô của định luật Ohm.

## Điện trở suất và nhiệt độ

$$R = \rho\frac{\ell}{A}, \qquad \rho = \rho_0\left[1 + \alpha(t - t_0)\right]$$

Cần phân biệt: $R$ phụ thuộc hình dạng, $\rho$ thì không. Kéo dài dây gấp đôi (thể tích không đổi nên tiết diện giảm một nửa) làm $R$ tăng **4 lần**, còn $\rho$ giữ nguyên.

Hai xu hướng ngược nhau theo nhiệt độ, và lí do vật lí khác hẳn nhau:

- **Kim loại:** $n$ gần như không đổi; nhiệt độ tăng làm ion dao động mạnh hơn, electron va chạm nhiều hơn nên $\rho$ **tăng** ($\alpha > 0$).
- **Bán dẫn và nhiệt điện trở NTC:** nhiệt độ tăng giải phóng thêm hạt tải, $n$ tăng theo hàm mũ, lấn át hiệu ứng va chạm nên $\rho$ **giảm** mạnh.

Ở nhiệt độ rất thấp, một số vật liệu có $\rho$ đột ngột về 0 — hiện tượng siêu dẫn, không giải thích được bằng mô hình cổ điển này.

**Lỗi thường gặp:**
- Cho rằng electron chạy từ nguồn tới bóng đèn với tốc độ ánh sáng — sai vì cái lan truyền nhanh là điện trường và tín hiệu, còn hạt tải chỉ trôi cỡ phần mười milimét mỗi giây.
- Kết luận điện trở suất tăng theo nhiệt độ với mọi vật liệu — sai vì ở bán dẫn, số hạt tải tăng theo hàm mũ với nhiệt độ và lấn át hiệu ứng tán xạ, làm điện trở suất giảm.
- Nhầm điện trở với điện trở suất khi so sánh hai dây khác kích thước — sai vì $R$ phụ thuộc chiều dài và tiết diện, hai dây cùng chất liệu vẫn có $R$ khác nhau trong khi $\rho$ hoàn toàn như nhau.

<sub>`lesson.physics.mach-dien.mo-hinh-dong-electron-va-dien-tro-suat`</sub>

---

### 2. Định luật Ohm và các vật liệu không tuân theo Ohm
*Ohm's law and non-ohmic materials* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu được chính xác định luật Ohm cùng điều kiện áp dụng của nó
- Phân tích được đặc tuyến vôn-ampe của điện trở, bóng đèn dây tóc, điốt bán dẫn và nhiệt điện trở
- Xác định được điện trở tại một điểm làm việc từ đồ thị $I(U)$

## Phát biểu cho đúng

Định luật Ohm thường bị rút gọn thành "$U = IR$", nhưng đó chỉ là **định nghĩa điện trở**, luôn đúng với mọi linh kiện. Nội dung thực sự của định luật Ohm là một khẳng định **thực nghiệm**:

> Với một vật dẫn kim loại ở nhiệt độ không đổi, cường độ dòng điện tỉ lệ thuận với hiệu điện thế; tức là $R$ là hằng số.

Cụm "ở nhiệt độ không đổi" mới là linh hồn của phát biểu. Bỏ nó đi thì không có gì để mà đúng hay sai.

## Bốn đặc tuyến cần đọc được

**Điện trở kim loại (ở nhiệt độ ổn định):** đường thẳng qua gốc. Hệ số góc bằng $1/R$.

**Bóng đèn dây tóc:** đường cong **cong xuống**. Dòng lớn làm dây tóc nóng lên tới hơn 2000 °C, $\rho$ tăng, nên $R$ tăng. Đây là lí do dòng khởi động của bóng đèn lớn hơn dòng làm việc nhiều lần.

**Điốt bán dẫn:** dòng gần như bằng 0 cho tới điện áp ngưỡng (khoảng 0,6 V với silic) rồi tăng vọt; theo chiều ngược thì hầu như không dẫn. Điốt có tính **một chiều**, thứ mà điện trở thuần không có.

**Nhiệt điện trở NTC:** $R$ giảm mạnh khi nhiệt độ tăng, dùng làm cảm biến nhiệt.

## Đọc điện trở từ đồ thị

Đây là kĩ năng thi hay hỏi và hay bị làm sai. Với linh kiện phi tuyến:

- Điện trở tại điểm làm việc là $R = U/I$ — tức **nghịch đảo hệ số góc của đường thẳng nối điểm đó với gốc toạ độ**.
- Không được lấy hệ số góc của **tiếp tuyến** rồi gọi đó là $R$; tiếp tuyến cho điện trở vi phân $r = dU/dI$, một đại lượng khác dùng cho tín hiệu nhỏ.

Với bóng đèn, hai giá trị này khác nhau rõ rệt, và câu hỏi "điện trở tăng hay giảm khi $U$ tăng?" phải trả lời bằng tỉ số $U/I$ chứ không bằng hình dạng cong.

## Vì sao vẫn dùng định luật Ohm

Dù nhiều linh kiện phi tuyến, mô hình ohm vẫn là nền tảng vì trong dải làm việc hẹp, mọi đường cong đều xấp xỉ thẳng. Kĩ thuật viên gọi đó là "tuyến tính hoá quanh điểm làm việc" — cách tiếp cận xuất hiện lại ở khắp nơi trong vật lí.

**Lỗi thường gặp:**
- Coi $U = IR$ là nội dung định luật Ohm — sai vì hệ thức này chỉ định nghĩa điện trở và luôn viết được cho mọi linh kiện; điều mà định luật Ohm khẳng định là $R$ giữ nguyên khi $U$ thay đổi ở nhiệt độ không đổi.
- Lấy hệ số góc tiếp tuyến của đặc tuyến cong để tính $R$ tại một điểm — sai vì tiếp tuyến cho điện trở vi phân $dU/dI$, còn điện trở thông thường phải lấy tỉ số $U/I$ của chính điểm đó.
- Cho rằng điốt có điện trở âm ở đoạn dốc đứng — sai vì đồ thị dốc chỉ nghĩa là $R$ nhỏ; điện trở âm đòi hỏi $U$ và $I$ biến thiên ngược chiều, điều không xảy ra ở điốt thường.

<sub>`lesson.physics.mach-dien.dinh-luat-ohm-va-vat-lieu-phi-tuyen`</sub>

---

### 3. Định luật Kirchhoff và giải mạch nhiều vòng
*Kirchhoff's laws and multiloop circuits* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Chứng minh được định luật nút xuất phát từ bảo toàn điện tích và định luật vòng từ bảo toàn năng lượng
- Vận dụng được hệ hai định luật để lập và giải hệ phương trình cho mạch hai vòng
- Xác định được số phương trình độc lập cần thiết cho một mạch bất kì

## Hai định luật, hai định luật bảo toàn

Kirchhoff không phát minh ra quy luật mới; ông chỉ dịch hai định luật bảo toàn sang ngôn ngữ mạch điện.

**Định luật nút = bảo toàn điện tích.** Điện tích không tích tụ tại một mối nối, nên bao nhiêu vào phải bấy nhiêu ra:

$$\sum I_{\text{vào}} = \sum I_{\text{ra}}$$

**Định luật vòng = bảo toàn năng lượng.** Một đơn vị điện tích đi hết một vòng kín trở về chỗ cũ thì thế năng của nó không đổi, nên năng lượng nhận từ các nguồn phải bằng năng lượng nhả ra ở các điện trở:

$$\sum \mathcal{E} = \sum IR$$

Hiểu được nguồn gốc này giúp nhớ dấu: đi qua nguồn từ cực âm sang cực dương thì $+\mathcal{E}$; đi qua điện trở cùng chiều dòng giả định thì $-IR$ (thế giảm).

## Quy trình giải chuẩn

1. **Giả định chiều dòng** trong mỗi nhánh, tuỳ ý. Nếu đoán sai, nghiệm sẽ ra âm — điều đó tự động sửa lỗi cho ta, nên không cần lo lắng khi chọn.
2. **Đếm ẩn:** số nhánh chưa biết dòng.
3. Viết $(n-1)$ phương trình nút với $n$ là số nút, rồi bổ sung phương trình vòng cho đủ số ẩn. Viết phương trình nút thứ $n$ là vô ích vì nó là tổ hợp của các phương trình trước.
4. Chọn vòng sao cho mỗi vòng mới chứa ít nhất một nhánh chưa dùng, để bảo đảm phương trình độc lập.
5. Giải hệ và **kiểm tra bằng công suất**: tổng công suất các nguồn phải bằng tổng công suất toả trên các điện trở.

## Trường hợp đặc biệt hay gặp

Mạch **cầu Wheatstone**: khi $R_1/R_2 = R_3/R_4$ thì hai điểm giữa cùng điện thế, dòng qua nhánh chéo bằng 0, và ta có thể tháo bỏ nhánh đó. Phép đo điện trở bằng cầu chính xác hơn dùng vôn kế - ampe kế vì nó là phép **so sánh về không**: chỉ cần phát hiện dòng bằng 0, không cần đọc giá trị tuyệt đối của bất kì đồng hồ nào, nên sai số của đồng hồ không đi vào kết quả.

Với mạch có nhiều nguồn giống nhau ghép nối tiếp hoặc song song, gộp thành nguồn tương đương trước khi dùng Kirchhoff sẽ rút ngắn hệ phương trình đáng kể.

**Lỗi thường gặp:**
- Viết đủ $n$ phương trình nút cho mạch có $n$ nút rồi không giải được — sai vì phương trình cuối cùng là tổ hợp tuyến tính của các phương trình trước, không mang thông tin mới, chỉ có $n-1$ phương trình độc lập.
- Đổi chiều dòng giữa chừng khi thấy kết quả âm — sai vì dấu âm đã tự nó chứa thông tin về chiều thực; sửa lại chiều rồi giữ nguyên các phương trình cũ sẽ tạo mâu thuẫn dấu.
- Bỏ qua điện trở trong khi tính vòng có nguồn — sai vì độ giảm thế $Ir$ bên trong nguồn cũng là một số hạng của định luật vòng; bỏ nó đi làm phương trình không còn bảo toàn năng lượng.

<sub>`lesson.physics.mach-dien.dinh-luat-kirchhoff`</sub>

---

### 4. Nguồn điện thực, điện trở trong và truyền công suất
*Real sources, internal resistance and power transfer* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phân tích được sự khác nhau giữa suất điện động và hiệu điện thế ở hai cực của nguồn đang phát điện
- Vận dụng được định luật Ohm cho toàn mạch để tính dòng và hiệu suất của nguồn
- Chứng minh được điều kiện $R = r$ cho công suất mạch ngoài cực đại và giải thích vì sao đó không phải điều kiện hiệu suất cao nhất

## Vì sao pin mới và pin cũ khác nhau

Đo pin AA bằng vôn kế (gần như không rút dòng) luôn thấy khoảng 1,5 V, kể cả pin sắp hết. Nhưng lắp vào đèn pin thì pin cũ sáng yếu hẳn. Nguyên nhân không nằm ở suất điện động mà ở **điện trở trong** đã tăng lên theo thời gian sử dụng.

Mô hình nguồn thực: một nguồn lí tưởng $\mathcal{E}$ nối tiếp với điện trở $r$. Khi mạch kín:

$$I = \frac{\mathcal{E}}{R + r}, \qquad U = \mathcal{E} - Ir$$

Hai hệ quả giới hạn đáng nhớ:

- **Hở mạch** ($I=0$): $U = \mathcal{E}$. Đây là lí do vôn kế tốt đo được gần đúng suất điện động.
- **Đoản mạch** ($R=0$): $I_{\max} = \mathcal{E}/r$. Với ắc quy ô tô ($r \approx 0{,}01$ Ω) dòng này lên tới hàng trăm ampe, đủ nung chảy dây — lí do vật lí của cầu chì.

## Truyền công suất: hai bài toán khác nhau

Công suất mạch ngoài:

$$P = I^2R = \frac{\mathcal{E}^2 R}{(R+r)^2}$$

Chia cả tử và mẫu cho $R$ để đưa mẫu về dạng tổng hai số hạng có tích không đổi:

$$P = \frac{\mathcal{E}^2}{\left(\sqrt{R} + r/\sqrt{R}\right)^2}$$

Theo bất đẳng thức Cauchy, mẫu nhỏ nhất khi $\sqrt{R} = r/\sqrt{R}$, tức $R = r$, cho $P_{\max} = \mathcal{E}^2/(4r)$.

Nhưng ở điều kiện đó, hiệu suất chỉ là

$$H = \frac{R}{R+r} = 50\%$$

Một nửa năng lượng đốt nóng chính cái pin. Vì thế **hoà hợp trở kháng** ($R=r$) chỉ dùng khi ta muốn lấy được nhiều công suất nhất từ nguồn yếu (mạch thu tín hiệu, loa, ăng-ten), còn hệ thống truyền tải điện quốc gia làm điều ngược lại: giữ $R \gg r$ để hiệu suất tiến tới 100%, chấp nhận công suất mỗi lần lấy ra không phải cực đại.

Sự phân biệt giữa "cực đại công suất" và "cực đại hiệu suất" là một trong những điểm tinh tế nhất của phần điện học phổ thông.

**Lỗi thường gặp:**
- Đồng nhất suất điện động với hiệu điện thế hai cực — sai vì chỉ khi dòng bằng 0 hai giá trị mới trùng nhau; khi nguồn phát dòng luôn có độ giảm thế $Ir$ bên trong.
- Cho rằng $R = r$ là chế độ làm việc tối ưu của mọi hệ thống điện — sai vì ở đó hiệu suất chỉ 50%; lưới điện và bộ sạc đều thiết kế để $R \gg r$ nhằm tối đa hoá hiệu suất chứ không phải công suất.
- Dùng $P = \mathcal{E}I$ để tính công suất tiêu thụ ở mạch ngoài — sai vì $\mathcal{E}I$ là công suất TỔNG do nguồn sản ra, phần dành cho mạch ngoài chỉ là $UI = \mathcal{E}I - I^2r$.

<sub>`lesson.physics.mach-dien.nguon-thuc-va-truyen-cong-suat`</sub>

---

### 5. Dụng cụ đo điện và ảnh hưởng của chúng lên mạch
*Measuring instruments and their loading effects* · THPT (lớp 10-12) · ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao ampe kế phải có điện trở rất nhỏ còn vôn kế phải có điện trở rất lớn
- Tính được điện trở sun và điện trở phụ để mở rộng thang đo
- Phân tích được sai số hệ thống do dụng cụ đo gây ra và cách khắc phục bằng phương pháp so sánh

## Nguyên tắc chung: đo mà không làm nhiễu

Mọi dụng cụ đo đều lấy một chút năng lượng từ mạch, và vì thế đều làm thay đổi cái nó đang đo. Thiết kế tốt là thiết kế giảm ảnh hưởng đó xuống mức bỏ qua được.

**Ampe kế** mắc **nối tiếp**, dòng cần đo chạy qua nó. Muốn không làm giảm dòng, điện trở của nó phải rất nhỏ so với điện trở mạch: lí tưởng $R_A \to 0$. Hệ quả quan trọng: **không bao giờ mắc ampe kế trực tiếp vào hai cực nguồn**, vì đó là đoản mạch.

**Vôn kế** mắc **song song** với đoạn cần đo. Muốn không rẽ bớt dòng, điện trở của nó phải rất lớn: lí tưởng $R_V \to \infty$.

## Chiều của sai số

Sai số do dụng cụ đo là **hệ thống**, luôn lệch về một phía, nên có thể dự đoán và hiệu chỉnh:

- Vôn kế thực mắc song song $R$ làm điện trở đoạn đó giảm xuống $\dfrac{RR_V}{R+R_V} < R$, nên số đo điện áp **thấp hơn** giá trị khi chưa mắc.
- Ampe kế thực làm tổng điện trở mạch tăng, nên dòng đo được **nhỏ hơn** dòng thật.

Sai số tương đối của phép đo vôn kế cỡ $R/R_V$. Với $R = 10$ kΩ và vôn kế $R_V = 100$ kΩ, sai số tới 10% — không hề nhỏ. Đây là lí do đồng hồ số hiện đại có $R_V$ cỡ 10 MΩ.

## Mở rộng thang đo

Một điện kế có dòng cực đại $I_g$ và điện trở $R_g$:

- Thành **ampe kế** đo tới $I$: mắc sun $R_s = \dfrac{I_gR_g}{I - I_g}$ (phần dòng thừa đi vòng qua sun).
- Thành **vôn kế** đo tới $U$: mắc nối tiếp $R_p = \dfrac{U}{I_g} - R_g$.

## Cách né tránh triệt để

Cầu Wheatstone và potentiometer (dây điện thế) né vấn đề bằng **phương pháp so sánh về không**: điều chỉnh cho tới khi điện kế chỉ 0, rồi đọc kết quả từ tỉ số chiều dài hoặc tỉ số điện trở. Vì lúc cân bằng không có dòng chạy qua nhánh đo, dụng cụ không rút năng lượng của mạch, và độ chính xác của điện kế không ảnh hưởng đến kết quả — nó chỉ cần nhạy, không cần chuẩn. Potentiometer nhờ đó đo được suất điện động **thật** của pin, điều mà vôn kế không bao giờ làm được chính xác.

**Lỗi thường gặp:**
- Mắc ampe kế song song với linh kiện cần đo dòng — sai vì điện trở ampe kế rất nhỏ, mắc song song sẽ tạo đường tắt gần như đoản mạch và có thể làm hỏng cả dụng cụ lẫn nguồn.
- Cho rằng vôn kế lí tưởng vì đọc số đẹp — sai vì vôn kế thực luôn rẽ bớt dòng, làm điện áp đo được thấp hơn giá trị thật; mức sai lệch phụ thuộc tỉ số giữa điện trở mạch và điện trở vôn kế.
- Nghĩ potentiometer chính xác hơn nhờ điện kế tốt — sai vì ưu thế của nó nằm ở chỗ đo tại trạng thái dòng bằng không, khi đó độ chuẩn của điện kế hoàn toàn không đi vào kết quả.

<sub>`lesson.physics.mach-dien.dung-cu-do-va-anh-huong`</sub>

---

## Unit 4: Thermal Physics and Molecular Properties

### 2. Hiện tượng bề mặt, Sức căng mặt ngoài và Hiện tượng mao dẫn
*Surface phenomena: Surface tension, Laplace pressure, and capillarity* · THPT (lớp 10-12) · ru-east-eu, olympiad · 45 phút · trung-binh

**Mục tiêu:**
- Xác định năng lượng mặt ngoài và công cần thiết để làm tăng diện tích bề mặt chất lỏng
- Tính áp suất phụ Laplace trong bọt xà phòng và giọt chất lỏng hình cầu
- Thiết lập công thức độ dâng mao dẫn Jurin giữa hai bản phẳng song song

## Sức căng mặt ngoài và Năng lượng bề mặt

Các phân tử trên lớp bề mặt chịu lực hút không cân bằng từ lòng chất lỏng, tạo nên năng lượng tự do bề mặt: $E_s = \sigma S$. Công cần thiết để tăng diện tích mặt ngoài: $A = \sigma \Delta S$.

## Áp suất phụ Laplace và Độ dâng mao dẫn

Tại mặt phân cách cong có bán kính $R$, lực căng mặt ngoài tạo áp suất phụ nén vào phía lõm:

- Giọt chất lỏng (1 mặt thoáng): $\Delta p = \frac{2\sigma}{R}$
- Bọt xà phòng trong không khí (2 mặt thoáng): $\Delta p = \frac{4\sigma}{R}$

Độ dâng mao dẫn giữa hai bản phẳng song song cách nhau khoảng $d$ khi thấm ướt hoàn toàn: $h = \frac{2\sigma}{\rho g d}$.

**Lỗi thường gặp:**
- Quên nhân đôi bán kính màng đối với bọt xà phòng (có cả mặt trong và mặt ngoài)
- Nhầm lẫn công thức mao dẫn trong ống tròn h = 2*sigma/(rho*g*r) với mao dẫn giữa hai bản song song h = 2*sigma/(rho*g*d)

<sub>`lesson.physics.mechanics-heat.hien-tuong-be-mat-suc-cang-va-mao-dan`</sub>

---

## Unit 4: Từ trường - Magnetic Fields

### 1. Từ trường, cảm ứng từ và lực Lorentz
*Magnetic field, magnetic flux density and the Lorentz force* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được nguồn gốc của từ trường là dòng điện và chuyển động của điện tích
- Vận dụng được quy tắc bàn tay trái và tích có hướng để xác định hướng của lực từ
- Phân tích được vì sao lực từ không sinh công lên hạt mang điện

## Từ trường sinh ra từ đâu

Năm 1820 Oersted tình cờ thấy kim la bàn lệch khi đặt cạnh dây có dòng điện. Phát hiện đó phá vỡ ranh giới giữa "điện" và "từ": **mọi từ trường đều do điện tích chuyển động sinh ra**. Nam châm vĩnh cửu không ngoại lệ — từ tính của nó đến từ chuyển động và spin của electron trong nguyên tử.

Điều này giải thích một khác biệt căn bản với tĩnh điện: không tồn tại "từ tích" đơn cực. Cắt đôi thanh nam châm, ta được hai nam châm đủ hai cực chứ không tách được cực bắc riêng. Hệ quả toán học là định luật Gauss cho từ trường:

$$\oint \vec{B}\cdot d\vec{A} = 0$$

Đường cảm ứng từ luôn **khép kín**, khác hẳn đường sức điện tĩnh.

## Lực Lorentz

$$\vec{F} = q\vec{v}\times\vec{B}, \qquad F = |q|vB\sin\alpha$$

Ba đặc điểm khiến lực này khác mọi lực đã học:

1. **Chỉ tác dụng lên điện tích đang chuyển động.** Hạt đứng yên trong từ trường không chịu lực nào.
2. **Phụ thuộc hướng của vận tốc.** Nếu $\vec{v}\parallel\vec{B}$ thì $\sin\alpha = 0$ và lực bằng 0; lực cực đại khi $\vec{v}\perp\vec{B}$.
3. **Luôn vuông góc với $\vec{v}$.**

Đặc điểm thứ ba dẫn tới kết luận quan trọng nhất: vì $\vec{F}\perp\vec{v}$ nên công của lực từ luôn bằng 0, do đó **lực từ không làm thay đổi động năng** của hạt. Nó chỉ bẻ hướng chuyển động, không tăng tốc cũng không hãm. Máy gia tốc dùng từ trường để lái hạt vòng quanh, nhưng phải dùng điện trường để tăng năng lượng — không có cách nào khác.

## Xác định hướng

Quy tắc bàn tay trái, phát biểu cho điện tích **dương**: đặt bàn tay trái sao cho $\vec{B}$ hướng vuông góc **vào lòng bàn tay**, chiều từ cổ tay tới các ngón chỉ chiều $\vec{v}$; khi đó ngón cái choãi ra $90^\circ$ chỉ chiều $\vec{F}$. Với điện tích âm thì đảo chiều kết quả. Tương đương và tổng quát hơn là quy tắc bàn tay phải cho tích có hướng $\vec{v}\times\vec{B}$, rồi nhân với dấu của $q$.

Từ trường mạnh trong phòng thí nghiệm cỡ vài tesla; từ trường Trái Đất chỉ khoảng $5\times10^{-5}$ T, nên tesla là đơn vị rất lớn.

**Lỗi thường gặp:**
- Cho rằng từ trường làm hạt mang điện tăng tốc — sai vì lực từ luôn vuông góc với vận tốc nên công bằng 0, tốc độ và động năng giữ nguyên, chỉ hướng chuyển động bị đổi.
- Áp dụng lực Lorentz cho điện tích đứng yên — sai vì biểu thức chứa thừa số $v$; hạt không chuyển động thì không có dòng, không có tương tác từ.
- Dùng $\cos\alpha$ trong công thức lực từ vì quen với công của lực — sai vì lực từ cực đại khi $\vec{v}\perp\vec{B}$ và triệt tiêu khi $\vec{v}\parallel\vec{B}$, đúng quy luật của hàm sin.

<sub>`lesson.physics.tu-truong.tu-truong-va-luc-lorentz`</sub>

---

### 2. Lực từ lên dây dẫn, mômen ngẫu lực và động cơ điện
*Force on a current-carrying conductor, torque and the electric motor* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được công thức $F = BI\ell\sin\theta$ cho đoạn dây dẫn mang dòng trong từ trường
- Tính được mômen ngẫu lực từ tác dụng lên khung dây và giải thích nguyên lí động cơ điện một chiều
- Giải thích được cơ chế tương tác giữa hai dây dẫn song song và định nghĩa ampe

## Từ hạt sang dòng

Một đoạn dây mang dòng chỉ là tập hợp rất nhiều hạt tải điện cùng trôi. Cộng lực Lorentz của tất cả hạt trong đoạn dây dài $\ell$:

$$F = BI\ell\sin\theta \qquad \text{hay} \qquad \vec{F} = I\vec{\ell}\times\vec{B}$$

với $\theta$ là góc giữa dây và $\vec{B}$. Công thức này là cầu nối giữa vi mô (hạt) và vĩ mô (thiết bị), và chính là cơ sở của mọi động cơ điện, loa, rơ le.

## Vì sao khung dây quay

Đặt khung chữ nhật mang dòng vào từ trường đều. Hai cạnh song song với $\vec{B}$ chịu lực bằng 0 hoặc dọc trục; hai cạnh vuông góc chịu hai lực **bằng nhau, ngược chiều, không cùng giá** — đúng định nghĩa của ngẫu lực. Ngẫu lực không làm khung tịnh tiến mà làm nó quay:

$$M = NBIS\sin\alpha = mB\sin\alpha$$

trong đó $\alpha$ là góc giữa **pháp tuyến** khung và $\vec{B}$. Mômen cực đại khi mặt phẳng khung chứa $\vec{B}$ ($\alpha = 90^\circ$), và bằng 0 khi pháp tuyến trùng $\vec{B}$ — vị trí cân bằng bền.

## Bài toán của động cơ và lời giải bằng cổ góp

Nếu để tự nhiên, khung sẽ quay tới vị trí cân bằng rồi dao động quanh đó và dừng lại. Muốn quay liên tục, phải đảo chiều dòng đúng lúc khung đi qua vị trí cân bằng — nhiệm vụ của **cổ góp**. Nhờ đó mômen luôn cùng chiều quay, và ta có động cơ điện một chiều.

Đây là ví dụ đẹp về việc một chi tiết cơ khí đơn giản giải quyết trọn vẹn một hạn chế vật lí.

## Hai dây song song và định nghĩa ampe

Dây 1 tạo ra từ trường tại vị trí dây 2; dây 2 mang dòng nên chịu lực. Kết quả:

$$\frac{F}{\ell} = \frac{\mu_0 I_1I_2}{2\pi d}$$

Hai dòng **cùng chiều thì hút nhau**, ngược chiều thì đẩy nhau — trái ngược trực giác từ tĩnh điện, nơi "cùng thì đẩy". Chính hệ thức này từng được dùng để định nghĩa đơn vị ampe trong hệ SI cũ, và nó cũng giải thích vì sao dây cáp mang dòng lớn phải được kẹp chặt: lực từ giữa các dây có thể đủ mạnh để làm bung hệ thống.

**Lỗi thường gặp:**
- Dùng góc giữa mặt phẳng khung và $\vec{B}$ thay cho góc giữa pháp tuyến và $\vec{B}$ — sai vì hai góc phụ nhau, việc hoán đổi làm mômen cực đại bị tính thành 0 và ngược lại.
- Cho rằng hai dây mang dòng cùng chiều đẩy nhau theo kiểu 'cùng dấu thì đẩy' — sai vì quy luật này thuộc về tĩnh điện; áp dụng quy tắc bàn tay trái cho từ trường của dây kia sẽ thấy lực hướng vào nhau.
- Quên nhân số vòng $N$ khi tính mômen của khung nhiều vòng — sai vì mỗi vòng đều chịu ngẫu lực riêng và các mômen này cùng chiều nên cộng dồn.

<sub>`lesson.physics.tu-truong.luc-tu-len-day-dan-va-dong-co`</sub>

---

### 3. Chuyển động tròn và xoắn ốc của hạt mang điện trong từ trường
*Circular and helical motion of charges in a magnetic field* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Chứng minh được bán kính quỹ đạo $r = mv/(qB)$ từ điều kiện lực hướng tâm
- Giải thích được vì sao chu kì chuyển động tròn không phụ thuộc tốc độ và bán kính
- Phân tích được chuyển động xoắn ốc và ứng dụng trong máy gia tốc cyclotron

## Vì sao quỹ đạo là đường tròn

Khi $\vec{v}\perp\vec{B}$, lực Lorentz có độ lớn không đổi $F = qvB$ (vì $v$ không đổi do lực không sinh công) và luôn vuông góc với vận tốc. Một lực như thế đúng là **lực hướng tâm**. Cân bằng:

$$qvB = \frac{mv^2}{r} \;\Longrightarrow\; r = \frac{mv}{qB} = \frac{p}{qB}$$

Bán kính tỉ lệ với **động lượng**, điều này khiến buồng bọt và detector hạt hiện đại đo được động lượng chỉ bằng cách đo độ cong vết hạt.

## Kết quả bất ngờ: chu kì độc lập với tốc độ

$$T = \frac{2\pi r}{v} = \frac{2\pi m}{qB}, \qquad f = \frac{qB}{2\pi m}$$

Hai đại lượng $v$ triệt tiêu nhau. Hạt nhanh chạy quỹ đạo lớn, hạt chậm chạy quỹ đạo nhỏ, nhưng cả hai mất **cùng một thời gian** để đi hết một vòng.

Đây không phải một trùng hợp toán học vô nghĩa — chính tính chất này làm cho máy gia tốc cyclotron khả thi. Điện áp xoay chiều đặt giữa hai hộp D chỉ cần có tần số cố định $f$ đúng bằng tần số cyclotron; mỗi lần hạt băng qua khe, nó được tăng tốc thêm, bán kính lớn dần thành hình xoắn ốc phẳng, nhưng nhịp độ vẫn khớp. Động năng cực đại khi ra khỏi máy:

$$W_{\max} = \frac{q^2B^2R^2}{2m}$$

với $R$ là bán kính hộp D. Ở tốc độ gần ánh sáng, khối lượng tương đối tính tăng làm $T$ tăng, hạt lệch nhịp — đó là lí do máy hiện đại phải dùng synchrotron với tần số biến thiên.

## Trường hợp tổng quát: xoắn ốc

Nếu $\vec{v}$ hợp góc $\alpha$ với $\vec{B}$, tách vận tốc thành hai thành phần:

- $v_\parallel = v\cos\alpha$: không chịu lực, chuyển động thẳng đều dọc $\vec{B}$.
- $v_\perp = v\sin\alpha$: quay tròn với bán kính $r = mv\sin\alpha/(qB)$.

Tổng hợp cho **đường xoắn ốc** có bước $h = v_\parallel T$. Đây chính là cách hạt mang điện từ Mặt Trời bị từ trường Trái Đất dẫn dắt về hai cực, va chạm với khí quyển và tạo ra cực quang. Nguyên lí đó cũng được dùng để giam plasma trong lò phản ứng nhiệt hạch tokamak.

**Lỗi thường gặp:**
- Nghĩ hạt nhanh hơn thì quay nhanh hơn nên chu kì nhỏ hơn — sai vì tốc độ lớn đi kèm bán kính lớn theo đúng tỉ lệ, quãng đường và tốc độ cùng tăng nên thời gian một vòng không đổi.
- Dùng toàn bộ $v$ để tính bán kính khi hạt bay xiên góc với $\vec{B}$ — sai vì chỉ thành phần vuông góc mới tham gia chuyển động tròn, phải lấy $v\sin\alpha$.
- Áp dụng công thức cyclotron cho hạt có tốc độ gần bằng tốc độ ánh sáng — sai vì khối lượng tương đối tính tăng theo hệ số Lorentz, làm chu kì tăng dần và hạt mất đồng bộ với điện áp gia tốc.

<sub>`lesson.physics.tu-truong.chuyen-dong-tron-trong-tu-truong`</sub>

---

### 4. Định luật Biot-Savart và từ trường của các cấu hình cơ bản
*The Biot-Savart law and fields of standard configurations* · THPT (lớp 10-12) · ap · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu được định luật Biot-Savart và giải thích ý nghĩa từng thừa số trong biểu thức
- Vận dụng được định luật để tìm cảm ứng từ của dây thẳng dài, vòng dây tròn và trên trục vòng dây
- Vận dụng được nguyên lí chồng chất từ trường cho hệ nhiều dòng điện

## Ý tưởng: chia nhỏ rồi cộng lại

Định luật Coulomb cho phép tính điện trường của phân bố bất kì bằng cách chia thành điện tích điểm rồi cộng. Biot và Savart làm điều tương tự cho từ trường: chia dây thành các **phần tử dòng** $I\,d\vec{\ell}$, mỗi phần tử đóng góp

$$d\vec{B} = \frac{\mu_0}{4\pi}\frac{I\,d\vec{\ell}\times\hat{r}}{r^2}$$

Đọc kĩ ba đặc điểm:

- Vẫn là quy luật **nghịch đảo bình phương** như Coulomb.
- Có **tích có hướng**, nên $d\vec{B}$ vuông góc với cả $d\vec{\ell}$ lẫn bán kính — đây là điểm khác căn bản với điện trường, và là lí do đường cảm ứng từ bao quanh dây thay vì toả ra.
- Phần tử dòng nằm **thẳng hàng** với điểm khảo sát ($d\vec{\ell}\parallel\hat r$) đóng góp bằng 0.

## Ba kết quả cần thuộc

**Dây thẳng dài vô hạn**, cách dây khoảng $r$:

$$B = \frac{\mu_0 I}{2\pi r} = 2\times10^{-7}\frac{I}{r}$$

Đường cảm ứng từ là những vòng tròn đồng tâm quanh dây; chiều xác định bằng quy tắc nắm tay phải.

**Tâm vòng dây tròn** bán kính $R$, $N$ vòng:

$$B = \frac{\mu_0 NI}{2R}$$

**Trên trục vòng dây**, cách tâm khoảng $x$:

$$B = \frac{\mu_0 I R^2}{2(R^2+x^2)^{3/2}}$$

Đặt $x=0$ ta thu lại công thức tâm vòng — một phép kiểm tra giới hạn nên làm mỗi khi nhớ công thức phức tạp. Khi $x \gg R$, biểu thức trở thành $B \approx \mu_0 m/(2\pi x^3)$ với $m = I\pi R^2$: vòng dây ở xa trông như một lưỡng cực từ, giảm theo $1/x^3$.

## Chồng chất

Với nhiều dòng, $\vec{B} = \sum\vec{B}_i$ — cộng **vectơ**. Bài toán điển hình là hai dây song song: giữa hai dây cùng chiều, hai từ trường ngược nhau nên có điểm triệt tiêu; hai dây ngược chiều thì trường ở giữa cộng dồn.

Biot-Savart luôn áp dụng được, kể cả khi không có đối xứng, nhưng cái giá là phải tính tích phân. Khi hệ có đối xứng cao, định luật Ampère sẽ nhanh hơn nhiều.

**Lỗi thường gặp:**
- Bỏ tích có hướng và cộng độ lớn các $dB$ khi tích phân — sai vì các $d\vec{B}$ do những phần tử khác nhau gây ra thường không cùng hướng; phải chiếu lên trục rồi mới cộng.
- Áp dụng $B = \mu_0 I/(2\pi r)$ cho dây có chiều dài hữu hạn ở gần đầu dây — sai vì công thức là kết quả của tích phân từ $-\infty$ tới $+\infty$, gần đầu dây giá trị thật nhỏ hơn đáng kể.
- Tìm điểm triệt tiêu của hai dòng cùng chiều ở phía ngoài đoạn nối — sai vì ngoài đoạn nối hai vectơ cảm ứng từ cùng chiều nên tổng không bao giờ bằng 0.

<sub>`lesson.physics.tu-truong.dinh-luat-biot-savart`</sub>

---

### 5. Định luật Ampère và từ trường của ống dây, cuộn xuyến
*Ampère's law: solenoid and toroid fields* · THPT (lớp 10-12) · ap · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu được định luật Ampère về lưu số và so sánh vai trò của nó với định luật Gauss
- Chọn được đường lấy tích phân phù hợp để suy ra từ trường của ống dây dài và cuộn xuyến
- Phân tích được vì sao từ trường bên trong ống dây dài là đều và bên ngoài gần như bằng không

## Định luật Ampère là gì

$$\oint_C \vec{B}\cdot d\vec{\ell} = \mu_0 I_{\text{xuyên qua}}$$

Phát biểu: lưu số của cảm ứng từ dọc một đường cong kín bất kì bằng $\mu_0$ nhân tổng đại số các dòng điện xuyên qua mặt giới hạn bởi đường đó.

Đối chiếu với Gauss cho điện trường giúp nhớ cả hai:

| | Gauss (điện) | Ampère (từ) |
|---|---|---|
| Đối tượng tích phân | mặt kín | đường cong kín |
| Nguồn | điện tích bên trong | dòng điện xuyên qua |
| Điều kiện dùng được | đối xứng cầu/trụ/phẳng | đối xứng trụ/ống dây/xuyến |

Giống Gauss, định luật Ampère **luôn đúng** nhưng chỉ **giải được** khi $B$ không đổi dọc đường lấy tích phân.

## Kiểm chứng với dây thẳng

Chọn đường tròn bán kính $r$ đồng tâm với dây. Do đối xứng, $B$ không đổi trên đường đó và $\vec{B}\parallel d\vec{\ell}$:

$$B\cdot 2\pi r = \mu_0 I \;\Rightarrow\; B = \frac{\mu_0 I}{2\pi r}$$

Một dòng ba, thay vì cả một tích phân Biot-Savart dài.

## Ống dây dài

Chọn đường chữ nhật có một cạnh dài $L$ nằm **trong** ống (song song trục), cạnh đối diện nằm **ngoài** ống ở rất xa. Lập luận từng cạnh:

- Cạnh trong: đóng góp $BL$.
- Hai cạnh vuông góc với trục: $\vec{B}\perp d\vec{\ell}$ nên đóng góp 0.
- Cạnh ngoài: từ trường bên ngoài ống dây dài xấp xỉ 0 nên đóng góp 0.

Dòng xuyên qua khung là $nLI$ với $n$ vòng/mét. Vậy $BL = \mu_0 nLI$:

$$B = \mu_0 n I$$

Kết quả **không chứa vị trí**: từ trường trong lòng ống dây dài là đều, kể cả gần thành ống. Đây là cách tạo từ trường đều đáng tin cậy nhất trong phòng thí nghiệm.

## Cuộn xuyến

Với cuộn dây quấn quanh lõi hình xuyến $N$ vòng, chọn đường tròn bán kính $r$ trong lòng xuyến:

$$B = \frac{\mu_0 NI}{2\pi r}$$

Từ trường bị **giam hoàn toàn** bên trong xuyến, bên ngoài bằng 0 — lí do máy biến áp và cuộn cảm công suất lớn thường dùng lõi xuyến: chúng không phát nhiễu ra môi trường xung quanh.

**Lỗi thường gặp:**
- Thay tổng số vòng $N$ vào công thức $B = \mu_0 nI$ — sai vì $n$ là số vòng trên MỖI MÉT; nhầm lẫn này cho kết quả sai theo đúng tỉ lệ chiều dài ống.
- Cho rằng định luật Ampère chỉ đúng khi đường lấy tích phân là đường tròn — sai vì định luật đúng với mọi đường cong kín; đường tròn chỉ được chọn vì nó khai thác đối xứng để tính được tích phân.
- Tính cả dòng điện nằm ngoài đường Ampère vào vế phải — sai vì chỉ dòng XUYÊN QUA mặt giới hạn mới đóng góp; dòng bên ngoài vẫn ảnh hưởng tới $\vec{B}$ từng điểm nhưng lưu số của nó dọc đường kín bằng 0.

<sub>`lesson.physics.tu-truong.dinh-luat-ampere`</sub>

---

### 6. Bộ chọn lọc vận tốc, phổ khối kế và hiệu ứng Hall
*Velocity selector, mass spectrometer and the Hall effect* · THPT (lớp 10-12) · ap, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được nguyên lí bộ chọn lọc vận tốc từ điều kiện cân bằng lực điện và lực từ
- Vận dụng được nguyên lí phổ khối kế để xác định khối lượng đồng vị
- Giải thích được hiệu ứng Hall và cách dùng nó để xác định dấu của hạt tải điện

## Ghép hai loại lực để lọc tốc độ

Chùm ion phát ra từ nguồn luôn có tốc độ rất khác nhau — không thể phân tích khối lượng nếu chưa chuẩn hoá tốc độ. Giải pháp: cho chùm đi qua vùng có $\vec{E}$ và $\vec{B}$ **vuông góc với nhau và cùng vuông góc với $\vec{v}$**, bố trí sao cho lực điện và lực từ ngược chiều:

$$qE = qvB \;\Longrightarrow\; v = \frac{E}{B}$$

Hai điều đáng chú ý: điều kiện này **không chứa $q$ và $m$** — mọi hạt bất kể điện tích hay khối lượng, chỉ cần đúng tốc độ $E/B$, đều đi thẳng. Hạt nhanh hơn bị lực từ thắng thế và lệch một bên, hạt chậm hơn bị lực điện kéo về bên kia; khe chắn ở cuối chỉ cho khe hẹp đi qua.

## Phổ khối kế

Sau khi ra khỏi bộ lọc với tốc độ đã biết, ion đi vào vùng chỉ có từ trường $B'$ và chạy cung tròn bán kính:

$$r = \frac{mv}{qB'} = \frac{mE}{qBB'}$$

Đo $r$ trên tấm cảm biến, biết $q$, ta suy ra $m$. Vì $r \propto m$, các đồng vị của cùng nguyên tố (cùng $q$, khác $m$ vài phần trăm) rơi vào những vị trí tách bạch. Đây là cách xác định tỉ lệ đồng vị trong khảo cổ, địa chất và kiểm tra doping thể thao.

## Hiệu ứng Hall: đọc được dấu của hạt tải

Cho dòng chạy dọc một bản dẫn mỏng đặt trong từ trường vuông góc. Lực Lorentz đẩy hạt tải dồn về một mặt bên, tạo ra điện trường ngang. Khi lực điện ngang cân bằng lực từ, quá trình dừng lại và ta đo được:

$$U_H = \frac{IB}{nqt}$$

Ý nghĩa lịch sử rất lớn: **dấu của $U_H$ cho biết dấu của hạt tải**. Lí do là nếu hạt tải dương chạy theo chiều dòng, hay hạt tải âm chạy ngược chiều dòng, thì lực Lorentz đẩy chúng về **cùng một bên**, nhưng điện tích tích tụ trái dấu nên hiệu điện thế đảo dấu. Thí nghiệm Hall (1879) nhờ đó chứng minh trong kim loại thường hạt tải là electron âm, còn trong một số bán dẫn loại p, hạt tải hiệu dụng lại mang dấu dương — kết quả mà nếu chỉ đo dòng và điện áp thì không bao giờ phát hiện được.

Ứng dụng ngày nay: đầu dò Hall đo từ trường, cảm biến vị trí trong động cơ không chổi than, đo tốc độ vòng quay.

**Lỗi thường gặp:**
- Cho rằng bộ chọn lọc vận tốc lọc theo khối lượng — sai vì điều kiện $v = E/B$ hoàn toàn không chứa $m$ và $q$; việc phân tách khối lượng chỉ xảy ra ở vùng từ trường phía sau.
- Dùng cùng một giá trị $B$ cho cả bộ lọc lẫn vùng phân tách — sai vì đó là hai từ trường độc lập trong thiết kế; nhầm lẫn làm bán kính tính ra lệch theo tỉ số hai từ trường.
- Kết luận hiệu ứng Hall chỉ cho biết độ lớn từ trường — sai vì thông tin quý nhất của nó là DẤU của hiệu điện thế Hall, thứ tiết lộ hạt tải điện trong vật liệu mang dấu gì.

<sub>`lesson.physics.tu-truong.chon-loc-van-toc-pho-khoi-va-hall`</sub>

---

## Unit 4: Work and Energy (AP Physics 1 Unit 3 / IB A.3 / CIE 9702 Topic 5)

### 1. Công của lực không đổi và công của lực biến thiên
*Work done by constant and variable forces* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Tính được công của lực không đổi theo tích vô hướng của lực và độ dịch chuyển
- Xác định được công của lực biến thiên bằng diện tích dưới đồ thị lực - độ dời
- Giải thích được vì sao lực vuông góc với chuyển động không sinh công

## Công không phải là "sự cố gắng"

Giữ nguyên một chiếc vali nặng đứng yên suốt mười phút thì mỏi tay, nhưng công cơ học bằng **0**: không có độ dịch chuyển. Xách vali đi ngang trên sàn phẳng cũng có $W = 0$ với lực nâng, vì lực thẳng đứng vuông góc với chuyển động ngang.

$$W = \vec{F}\cdot\vec{d} = Fd\cos\theta$$

Ba trường hợp cần thuộc:

- $\theta < 90^{\circ}$: công dương, lực tiếp năng lượng cho vật.
- $\theta = 90^{\circ}$: công bằng 0. Đây là lí do **lực hướng tâm không bao giờ sinh công**, và lực từ tác dụng lên hạt mang điện cũng vậy.
- $\theta > 90^{\circ}$: công âm, lực rút năng lượng, điển hình là ma sát trượt với $W = -f_k s$.

## Lực biến thiên: chuyển sang diện tích

Công thức $W = Fd\cos\theta$ giả thiết $F$ không đổi. Khi $F$ thay đổi (kéo lò xo, lực đẩy tên lửa), chia quãng đường thành các đoạn nhỏ mà trong đó $F$ coi như hằng, rồi cộng lại:

$$W = \int_{x_1}^{x_2} F(x)\,dx$$

Về mặt hình học, đó chính là **diện tích dưới đồ thị $F$-$x$**, tính có dấu. AP Physics 1 và IB đọc diện tích bằng hình học; AP Physics C dùng tích phân.

Ví dụ quan trọng nhất là lò xo: $F = kx$ cho đồ thị là đường thẳng qua gốc, diện tích tam giác cho

$$W = \tfrac12 k x^{2}$$

Hệ số $\tfrac12$ xuất hiện chính vì lực tăng tuyến tính từ 0 chứ không phải vì một quy ước nào.

## Công của trọng lực

$W_{P} = -mg\Delta h$ khi lấy chiều dương hướng lên; công này **không phụ thuộc đường đi**, chỉ phụ thuộc độ chênh cao. Tính chất đó biến trọng lực thành lực thế, mở đường cho khái niệm thế năng ở bài sau.

**Lỗi thường gặp:**
- Dùng $W = Fs$ mà quên $\cos\theta$. Chỉ hình chiếu của lực lên phương chuyển động mới sinh công; bỏ cos làm công bị thổi phồng và vi phạm bảo toàn năng lượng.
- Cho rằng lực căng dây trong chuyển động tròn sinh công. Lực căng luôn vuông góc với vận tốc trong quỹ đạo tròn nên $\cos 90^{\circ} = 0$, đó là lí do tốc độ không đổi trong chuyển động tròn đều.
- Áp dụng $W = Fd$ cho lò xo với $F$ lấy ở giá trị cuối. Lực lò xo tăng dần từ 0, nên công là diện tích tam giác $\tfrac12 kx^{2}$ chứ không phải diện tích chữ nhật $kx^{2}$ — sai đúng gấp đôi.

<sub>`lesson.physics.nang-luong-intl.cong-cua-luc-hang-va-luc-bien-thien`</sub>

---

### 2. Động năng và định lí công - động năng
*Kinetic energy and the work-energy theorem* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Chứng minh được định lí công - động năng từ định luật II Newton và hệ thức động học
- Vận dụng được định lí để giải bài toán mà phương pháp động lực học phải qua nhiều bước
- Phân tích được vì sao quãng đường phanh tỉ lệ với bình phương tốc độ

## Chứng minh trong ba dòng

Với lực không đổi trên đường thẳng, định luật II cho $F = ma$, và hệ thức động học độc lập thời gian cho $v_f^{2} = v_i^{2} + 2as$. Nhân hai vế với $m/2$ và thay $ma = F$:

$$Fs = \tfrac12 mv_f^{2} - \tfrac12 mv_i^{2}$$

Vế trái là công, vế phải là độ biến thiên động năng. Kết quả này còn đúng cho lực biến thiên và đường cong, khi ta thay $Fs$ bằng tích phân đường.

## Vì sao nó tiện hơn động lực học

Định lí nối **trạng thái đầu với trạng thái cuối**, bỏ qua toàn bộ chi tiết của quá trình. Nếu bài toán không hỏi thời gian và không hỏi gia tốc từng thời điểm, đây gần như luôn là con đường ngắn nhất. Một viên bi trượt trên máng cong lồi lõm phức tạp: dùng định lí này chỉ cần biết công của trọng lực và của ma sát.

## Chú ý chữ "hợp lực"

$$W_{\text{hợp lực}} = \sum W_i = \Delta E_k$$

Phải cộng công của **mọi** lực, kể cả công âm của ma sát. Nếu chỉ lấy công của lực kéo, kết quả sẽ vượt quá động năng thật.

## Hai hệ quả đáng nhớ

1. **Quãng đường phanh**: $\tfrac12 mv^{2} = f_k s \Rightarrow s = \dfrac{v^{2}}{2\mu_k g}$. Tăng tốc độ gấp đôi thì quãng đường phanh gấp bốn, và điều này **không phụ thuộc khối lượng** — xe tải và xe con phanh hết cùng một quãng đường nếu cùng hệ số ma sát.
2. **Liên hệ với động lượng**: $E_k = \dfrac{p^{2}}{2m}$. Hai vật cùng động lượng thì vật nhẹ có động năng lớn hơn; hai vật cùng động năng thì vật nặng có động lượng lớn hơn.

## Ranh giới

Định lí đúng cho **chất điểm** hoặc cho khối tâm của vật rắn. Với vật vừa quay vừa tịnh tiến, phải bổ sung động năng quay, sẽ gặp ở phần chuyển động quay.

**Lỗi thường gặp:**
- Chỉ lấy công của lực phát động mà bỏ công âm của ma sát. Định lí nói về công của **hợp lực**; bỏ sót công âm sẽ cho vận tốc cuối lớn hơn thực tế.
- Cho rằng động năng là đại lượng vectơ vì chứa $v$. Động năng là vô hướng, luôn dương; hai vật chạy ngược chiều nhau vẫn có động năng cộng lại chứ không trừ nhau như động lượng.
- Nghĩ xe nặng cần quãng đường phanh dài hơn. Từ $s = v^{2}/(2\mu_k g)$ thấy khối lượng triệt tiêu; xe tải phanh dài hơn trong thực tế là vì hệ thống phanh nóng lên và lốp biến dạng, không phải vì khối lượng trong công thức này.

<sub>`lesson.physics.nang-luong-intl.dinh-li-cong-dong-nang`</sub>

---

### 3. Lực thế, thế năng và bảo toàn cơ năng
*Conservative forces, potential energy and conservation of mechanical energy* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được lực thế và lực không thế qua tính chất công theo đường đi
- Vận dụng được định luật bảo toàn cơ năng cho hệ chỉ có lực thế
- Tính được độ biến thiên cơ năng khi hệ có lực ma sát hoặc lực cản

## Vì sao chỉ một số lực mới có thế năng

Đưa vật lên độ cao $h$ theo cầu thang xoắn hay theo phương thẳng đứng, công của trọng lực đều bằng $-mgh$. Ngược lại, kéo thùng đi vòng vèo rồi về chỗ cũ thì công của ma sát khác 0 và càng đi vòng càng âm. Sự khác biệt này chia lực thành hai loại, và **chỉ lực thế mới định nghĩa được thế năng**.

$$\Delta E_p = -W_{\text{lực thế}}$$

Dấu trừ có ý nghĩa vật lí rõ ràng: trọng lực sinh công dương khi vật rơi, và thế năng giảm đúng bằng chừng ấy.

## Ba biểu thức thế năng

$$E_p = mgh \ \ (\text{gần mặt đất}), \qquad E_p = \tfrac12 kx^{2} \ \ (\text{lò xo}), \qquad E_p = -\frac{GMm}{r} \ \ (\text{hấp dẫn tổng quát})$$

Mốc thế năng chọn tuỳ ý: mặt đất, mặt bàn, hay vô cực. Chọn khác nhau cho $E_p$ khác nhau nhưng $\Delta E_p$ và mọi kết luận vật lí vẫn như cũ.

## Bảo toàn và không bảo toàn

Nếu **chỉ** lực thế sinh công:

$$E_{k1} + E_{p1} = E_{k2} + E_{p2}$$

Nếu có thêm lực không thế (ma sát, lực cản, lực đẩy động cơ):

$$\Delta E = E_2 - E_1 = W_{\text{lực không thế}}$$

Với ma sát, $W = -f_k s$ (dùng **quãng đường**, không phải độ dịch chuyển) và phần năng lượng mất đi chuyển thành nhiệt. Năng lượng toàn phần vẫn bảo toàn, chỉ cơ năng thì không.

## Sức mạnh của phương pháp

Một viên bi trượt không ma sát trong lòng máng cong bất kỳ: tốc độ tại độ cao $h$ chỉ phụ thuộc $h$, hoàn toàn không phụ thuộc hình dạng máng, vì $v = \sqrt{2g(h_0 - h)}$. Giải bằng động lực học sẽ phải biết hàm số của máng; giải bằng năng lượng chỉ mất một dòng.

**Lỗi thường gặp:**
- Định nghĩa thế năng cho lực ma sát. Công của ma sát phụ thuộc đường đi (đi vòng xa thì mất nhiều hơn), nên không tồn tại hàm thế năng nào của riêng vị trí ứng với nó.
- Dùng độ dịch chuyển thay vì quãng đường khi tính công ma sát. Ma sát luôn ngược chiều chuyển động tức thời, nên vật đi rồi quay lại vẫn mất năng lượng ở cả hai chặng; dùng độ dịch chuyển sẽ cho kết quả bằng 0 một cách vô lí.
- Cho rằng cơ năng không bảo toàn thì năng lượng biến mất. Năng lượng toàn phần luôn bảo toàn; phần cơ năng hao hụt chuyển thành nội năng làm hai bề mặt nóng lên.

<sub>`lesson.physics.nang-luong-intl.the-nang-va-bao-toan-co-nang`</sub>

---

### 4. Đồ thị thế năng, lực thế và các loại điểm cân bằng
*Potential energy graphs, force from potential and equilibrium points* · THPT (lớp 10-12) · ap, a-level, olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Xác định được lực từ đồ thị thế năng bằng quan hệ $F = -dE_p/dx$
- Phân loại được cân bằng bền, không bền và phiếm định dựa vào dạng đồ thị thế năng
- Xác định được vùng chuyển động cho phép và điểm quay đầu từ mức cơ năng cho trước

## Đọc cả một chuyển động chỉ từ một đường cong

Vẽ $E_p(x)$ rồi kẻ một đường nằm ngang ở mức cơ năng $E$. Từ hình vẽ đó đọc được gần như mọi thứ:

- **Khoảng cách theo phương đứng** giữa đường $E$ và đường cong là động năng: $E_k = E - E_p(x)$.
- **Vùng cho phép** là nơi $E \ge E_p$. Vùng $E_p > E$ là vùng cấm vì động năng không thể âm.
- **Giao điểm** của đường $E$ với đường cong là điểm quay đầu.
- **Độ dốc** cho lực: $F = -dE_p/dx$. Dốc lên thì lực hướng sang trái, dốc xuống thì lực hướng sang phải.

Hình dung một viên bi lăn trên chính đường cong đó dưới tác dụng trọng lực — trực giác gần như luôn đúng.

## Ba loại điểm cân bằng

Cân bằng ứng với $dE_p/dx = 0$:

| Loại | Dấu hiệu | Hành vi khi lệch nhỏ |
|---|---|---|
| Bền | Cực tiểu, $d^{2}E_p/dx^{2} > 0$ | Lực kéo về, vật dao động |
| Không bền | Cực đại, $d^{2}E_p/dx^{2} < 0$ | Lực đẩy đi xa, vật rời khỏi |
| Phiếm định | $E_p$ hằng số | Không có lực, vật đứng yên ở vị trí mới |

## Dao động nhỏ quanh cực tiểu

Khai triển Taylor thế năng quanh cực tiểu $x_0$:

$$E_p(x) \approx E_p(x_0) + \tfrac12 E_p''(x_0)(x - x_0)^{2}$$

Số hạng bậc nhất triệt tiêu vì đó là cực tiểu. Dạng này giống hệt thế năng lò xo với $k_{\text{hiệu dụng}} = E_p''(x_0)$, nên mọi hệ đều dao động điều hòa quanh vị trí cân bằng bền với

$$\omega = \sqrt{\frac{E_p''(x_0)}{m}}$$

Đây là lí do sâu xa vì sao dao động điều hòa xuất hiện ở khắp nơi trong tự nhiên, từ phân tử tới cầu treo.

## Ví dụ chuẩn

Thế năng Lennard-Jones giữa hai nguyên tử có một cực tiểu ở khoảng cách cân bằng: đó chính là độ dài liên kết. Muốn tách hai nguyên tử ra vô cực phải cấp năng lượng bằng độ sâu của hố thế — đó là năng lượng liên kết.

**Lỗi thường gặp:**
- Quên dấu trừ trong $F = -dE_p/dx$, dẫn tới kết luận ngược hoàn toàn về chiều lực. Dấu trừ phản ánh sự thật vật lí là hệ luôn có xu hướng chuyển về nơi thế năng thấp.
- Coi mọi điểm có $dE_p/dx = 0$ là cân bằng bền. Cực đại cũng thoả điều kiện đạo hàm bậc nhất bằng 0 nhưng là cân bằng không bền; phải xét đạo hàm bậc hai mới phân loại được.
- Cho rằng vật có thể đi vào vùng $E_p > E$ nếu chạy đủ nhanh. Ở đó động năng phải âm, điều không thể trong cơ học cổ điển; đây chính là ranh giới mà hiệu ứng đường hầm lượng tử phá vỡ.

<sub>`lesson.physics.nang-luong-intl.do-thi-the-nang-va-can-bang`</sub>

---

### 5. Công suất và hiệu suất
*Power and efficiency* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Tính được công suất trung bình và công suất tức thời theo hai cách tương đương
- Vận dụng được hệ thức $P = Fv$ để giải bài toán tốc độ cực đại của phương tiện
- Đánh giá được hiệu suất của máy và giải thích vì sao hiệu suất luôn nhỏ hơn 100 phần trăm

## Cùng một công, khác nhau ở tốc độ

Một người và một cần cẩu cùng nâng 1000 kg lên 10 m thì công đều là $10^{5}$ J. Khác biệt nằm ở **thời gian**: cần cẩu làm trong 10 s, người dùng ròng rọc mất cả buổi. Công suất là đại lượng đo tốc độ đó.

$$P_{tb} = \frac{W}{\Delta t}, \qquad P = \frac{dW}{dt} = \vec{F}\cdot\vec{v}$$

Dạng thứ hai rất mạnh: nó cho biết ở mỗi khoảnh khắc, động cơ đang tiêu thụ bao nhiêu.

## Hệ quả: tốc độ cực đại của xe

Động cơ có công suất định mức $P$. Khi xe đạt tốc độ cực đại thì gia tốc bằng 0, tức lực kéo cân bằng lực cản:

$$P = F_{\text{kéo}} v_{\max} = F_{\text{cản}} v_{\max} \Rightarrow v_{\max} = \frac{P}{F_{\text{cản}}}$$

Vì lực cản không khí tăng theo $v^{2}$, ta có $P \propto v^{3}$: muốn xe chạy nhanh gấp đôi phải có động cơ mạnh gấp **tám** lần. Đây là lí do vật lí khiến xe đua tiêu thụ nhiên liệu khủng khiếp và vì sao đạp xe ngược gió mệt đến vậy.

Hệ quả thứ hai: ở tốc độ thấp, cùng công suất cho lực kéo lớn (số 1 của xe máy leo dốc); ở tốc độ cao, lực kéo nhỏ đi.

## Hiệu suất

$$\eta = \frac{W_{\text{có ích}}}{W_{\text{toàn phần}}} \times 100\%$$

Phần chênh lệch không biến mất mà chuyển thành nhiệt do ma sát, nhiệt Joule, âm thanh. Với động cơ nhiệt còn có giới hạn nghiêm ngặt hơn do nguyên lí II nhiệt động lực học, sẽ học ở phần nhiệt học.

Con số thực tế đáng nhớ: động cơ xăng khoảng 25 đến 30 phần trăm, động cơ điện trên 90 phần trăm, bóng đèn sợi đốt chỉ 5 phần trăm cho ánh sáng.

## Đơn vị hay bị lẫn

Oát là đơn vị công suất, kilôoát giờ (kWh) là đơn vị **năng lượng**: $1\ \mathrm{kWh} = 3{,}6\times10^{6}$ J. Hóa đơn điện tính bằng kWh vì người ta bán năng lượng chứ không bán công suất.

**Lỗi thường gặp:**
- Dùng $P = Fv$ với $F$ là lực kéo của động cơ khi xe đang tăng tốc rồi kết luận tốc độ cực đại. Công thức $v_{\max} = P/F_{\text{cản}}$ chỉ áp dụng khi gia tốc bằng 0, tức lực kéo đã bằng lực cản.
- Nhầm kWh với kW. kW là công suất (tốc độ tiêu thụ năng lượng), kWh là năng lượng (công suất nhân thời gian); nhầm hai đại lượng này làm sai thứ nguyên toàn bài.
- Cho rằng máy có hiệu suất 100 phần trăm là khả thi nếu chế tạo đủ tinh vi. Mọi máy thực đều có ma sát và toả nhiệt; riêng động cơ nhiệt còn bị nguyên lí II chặn trên bởi hiệu suất Carnot dù không hề có ma sát.

<sub>`lesson.physics.nang-luong-intl.cong-suat-va-hieu-suat`</sub>

---

## Unit 5: Cảm ứng điện từ - Electromagnetic Induction

### 1. Từ thông và định luật Faraday về cảm ứng điện từ
*Magnetic flux and Faraday's law of induction* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được từ thông qua một khung dây và ba cách làm từ thông biến thiên
- Vận dụng được định luật Faraday để tính suất điện động cảm ứng
- Phân tích được đồ thị $\Phi(t)$ để suy ra đồ thị suất điện động cảm ứng

## Câu hỏi ngược của Faraday

Oersted đã chỉ ra dòng điện tạo ra từ trường. Faraday dành mười năm hỏi câu ngược lại: từ trường có tạo ra dòng điện không? Ông thất bại nhiều lần vì luôn dùng **nam châm đứng yên**. Bước ngoặt đến khi ông nhận ra điều quyết định không phải từ trường mà là **sự biến thiên** của nó.

Để phát biểu chính xác "biến thiên cái gì", cần đại lượng từ thông:

$$\Phi = BS\cos\alpha$$

Góc $\alpha$ đo giữa $\vec{B}$ và **pháp tuyến** mặt phẳng khung. Từ thông cực đại khi $\vec{B}$ vuông góc mặt khung, bằng 0 khi $\vec{B}$ nằm trong mặt phẳng khung.

## Định luật Faraday

$$e = -\frac{d\Phi}{dt}, \qquad |e| = N\left|\frac{\Delta\Phi}{\Delta t}\right|$$

Điều bị hiểu nhầm nhiều nhất: suất điện động **không** tỉ lệ với $\Phi$, mà tỉ lệ với **tốc độ biến thiên** của $\Phi$. Một khung nằm trong từ trường cực mạnh nhưng không đổi thì không sinh ra suất điện động nào. Về mặt toán học, $e$ là đạo hàm của $\Phi$, nên:

- $\Phi$ tăng đều theo thời gian → $e$ là hằng số.
- $\Phi$ đạt cực đại (đỉnh đồ thị) → $e = 0$ tại đúng thời điểm đó.
- $\Phi$ biến thiên hình sin → $e$ biến thiên hình sin lệch pha $\pi/2$.

Kĩ năng đọc cặp đồ thị $\Phi(t)$ và $e(t)$ là dạng bài trọng tâm của IB và A Level.

## Ba cách làm biến thiên từ thông

Từ $\Phi = BS\cos\alpha$, có đúng ba cách:

1. **Đổi $B$** — đưa nam châm lại gần, thay đổi dòng trong cuộn sơ cấp.
2. **Đổi $S$** — kéo dãn khung, hoặc để thanh trượt trên ray làm diện tích mạch thay đổi.
3. **Đổi $\alpha$** — quay khung trong từ trường, chính là nguyên lí máy phát điện.

Mọi bài toán cảm ứng đều quy về việc nhận ra đang dùng cách nào trong ba cách này.

Một hệ quả sâu xa: suất điện động cảm ứng tồn tại ngay cả khi mạch hở (khi đó không có dòng nhưng vẫn có hiệu điện thế ở hai đầu). Nghĩa là từ trường biến thiên sinh ra một **điện trường xoáy** thực sự trong không gian, không cần dây dẫn — ý tưởng dẫn thẳng tới phương trình Maxwell và sóng điện từ.

**Lỗi thường gặp:**
- Cho rằng từ thông lớn thì suất điện động lớn — sai vì định luật Faraday chứa ĐẠO HÀM của từ thông; khung đặt trong từ trường rất mạnh nhưng không đổi cho suất điện động bằng 0.
- Dùng góc giữa $\vec{B}$ và mặt phẳng khung trong công thức $\Phi = BS\cos\alpha$ — sai vì $\alpha$ phải là góc với pháp tuyến; nhầm lẫn này hoán đổi $\sin$ và $\cos$, cho từ thông cực đại ở đúng vị trí mà thực tế nó bằng 0.
- Quên nhân số vòng $N$ — sai vì các vòng mắc nối tiếp nhau nên suất điện động của từng vòng cộng dồn; bỏ $N$ làm kết quả nhỏ đi đúng $N$ lần.

<sub>`lesson.physics.cam-ung.tu-thong-va-dinh-luat-faraday`</sub>

---

### 2. Định luật Lenz và suất điện động chuyển động
*Lenz's law and motional emf* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được định luật Lenz để xác định chiều dòng điện cảm ứng trong các tình huống cụ thể
- Chứng minh được định luật Lenz là hệ quả của định luật bảo toàn năng lượng
- Thiết lập được biểu thức suất điện động chuyển động $e = B\ell v$ bằng hai con đường độc lập

## Dấu trừ của Faraday chính là Lenz

Dấu trừ trong $e = -d\Phi/dt$ không phải quy ước hình thức. Nó phát biểu rằng dòng cảm ứng luôn **chống lại** nguyên nhân sinh ra nó.

Giả sử ngược lại: dòng cảm ứng hỗ trợ sự biến thiên. Khi đó đẩy nam châm lại gần cuộn dây sẽ sinh ra lực hút, nam châm tự tăng tốc, từ thông biến thiên nhanh hơn, dòng lớn hơn, lực hút mạnh hơn... Ta có một cỗ máy tự sinh năng lượng vô hạn. **Định luật Lenz chính là định luật bảo toàn năng lượng viết cho hiện tượng cảm ứng** — hiểu như vậy sẽ không bao giờ nhớ nhầm chiều.

Hệ quả thực nghiệm nổi tiếng: thả nam châm rơi qua ống đồng, nó rơi chậm hẳn lại dù đồng không nhiễm từ. Dòng cảm ứng trong thành ống tạo lực cản; công cơ học ta bỏ ra để thắng lực cản đó chính là nguồn của nhiệt Joule sinh trong ống.

## Suất điện động chuyển động

Thanh dẫn dài $\ell$ trượt với vận tốc $v$ trên hai ray, vuông góc với $\vec{B}$. Hai cách dẫn ra kết quả, và nên biết cả hai:

**Cách 1 - qua từ thông.** Trong thời gian $dt$, diện tích mạch tăng $dS = \ell v\,dt$, nên

$$|e| = \frac{d\Phi}{dt} = B\ell v$$

**Cách 2 - qua lực Lorentz.** Electron trong thanh chuyển động cùng thanh nên chịu lực $F = evB$ dồn về một đầu, tạo điện trường trong thanh. Cân bằng khi $eE = evB$, tức $E = vB$, và hiệu điện thế hai đầu $U = E\ell = B\ell v$.

Hai cách cho cùng đáp số nhưng cách 2 giải thích được cả trường hợp không có mạch kín — thanh dẫn bay tự do trong từ trường vẫn tích điện hai đầu.

## Cân bằng năng lượng của thanh trượt

Khi mạch kín có điện trở $R$:

$$I = \frac{B\ell v}{R}, \qquad F_{\text{cản}} = BI\ell = \frac{B^2\ell^2v}{R}$$

Lực cản tỉ lệ với $v$: thanh càng nhanh càng bị hãm mạnh. Nếu kéo thanh với lực không đổi, nó tiến tới **tốc độ giới hạn** khi lực kéo cân bằng lực cản. Công suất cơ mà ta cung cấp, $P = F v$, đúng bằng công suất điện $I^2R$ toả trên điện trở — không mất mát, không dư thừa. Đây là kiểm chứng định lượng đẹp nhất cho khẳng định "Lenz = bảo toàn năng lượng".

**Lỗi thường gặp:**
- Xác định chiều dòng cảm ứng bằng cách nhìn chiều của $\vec{B}$ thay vì chiều BIẾN THIÊN của từ thông — sai vì cùng một từ trường, việc nó đang tăng hay đang giảm cho hai chiều dòng ngược nhau.
- Nghĩ dòng cảm ứng luôn ngược chiều dòng gây ra nó — sai vì Lenz nói dòng cảm ứng chống lại SỰ BIẾN THIÊN; khi từ thông giảm, dòng cảm ứng lại có chiều duy trì từ thông, tức cùng chiều với dòng ban đầu.
- Bỏ qua lực cản từ khi tính chuyển động của thanh — sai vì chính lực này là cơ chế chuyển hoá năng lượng; bỏ nó đi thì thanh sẽ tăng tốc mãi mà vẫn sinh ra điện, vi phạm bảo toàn năng lượng.

<sub>`lesson.physics.cam-ung.dinh-luat-lenz-va-sdd-chuyen-dong`</sub>

---

### 3. Dòng Foucault: tác hại và ứng dụng
*Eddy currents: drawbacks and applications* · THPT (lớp 10-12) · ib, a-level · 40 phút · trung-binh

**Mục tiêu:**
- Giải thích được cơ chế hình thành dòng Foucault trong khối kim loại đặt trong từ trường biến thiên
- Phân tích được nguyên lí hãm điện từ và bếp từ dựa trên dòng Foucault
- Giải thích được vì sao lõi máy biến áp phải ghép từ các lá thép mỏng cách điện

## Khi vật dẫn không phải là dây

Định luật Faraday nói về từ thông qua **mạch**, nhưng bản chất của nó là điện trường xoáy sinh ra trong không gian. Khi từ thông biến thiên xuyên qua một **khối** kim loại đặc, không cần dây dẫn nào cả: electron tự do trong khối lập tức chảy thành những vòng xoáy khép kín. Đó là dòng Foucault.

Theo Lenz, những vòng xoáy này tạo từ trường chống lại sự biến thiên, nên chúng luôn kèm theo hai hệ quả:

1. **Lực cản** lên chuyển động tương đối giữa khối kim loại và từ trường.
2. **Nhiệt Joule** toả ra trong khối, do điện trở của chính kim loại.

Tuỳ hoàn cảnh, mỗi hệ quả là ưu điểm hay nhược điểm.

## Khi là ưu điểm

**Hãm điện từ.** Tàu cao tốc và xe tải hạng nặng dùng đĩa kim loại quay giữa hai cực nam châm điện. Lực cản tỉ lệ với tốc độ nên phanh rất êm, và vì không có bố phanh cọ xát nên không mòn, không quá nhiệt cục bộ. Điểm hạn chế cần biết: lực cản tỉ lệ với $v$ nên khi tốc độ tiến về 0 thì lực cũng về 0 — phanh điện từ không thể giữ xe đứng yên, luôn phải kết hợp phanh cơ.

**Bếp từ.** Cuộn dây dưới mặt bếp mang dòng cao tần tạo từ trường biến thiên nhanh, sinh dòng Foucault ngay trong đáy nồi. Nồi tự nóng lên còn mặt kính thì không, vì kính không dẫn điện. Đây cũng là lí do bếp từ chỉ dùng được nồi sắt từ.

**Máy dò kim loại, lò nung cảm ứng, đồng hồ đo điện kiểu đĩa quay** đều dựa trên cùng nguyên lí.

## Khi là nhược điểm và cách chữa

Trong lõi máy biến áp và động cơ, từ thông biến thiên liên tục nên dòng Foucault đốt nóng lõi, gây tổn hao năng lượng và làm hỏng cách điện. Không thể triệt tiêu hiện tượng, nhưng có thể **cắt đường đi** của nó: ghép lõi từ nhiều lá thép mỏng, mỗi lá phủ lớp oxit hoặc sơn cách điện, đặt song song với mặt phẳng chứa từ thông.

Vì sao cách này hiệu quả: tổn hao Foucault tỉ lệ với **bình phương** bề dày lá thép. Chia lõi thành 10 lá làm tổn hao giảm khoảng 100 lần. Ngoài ra người ta còn dùng thép silic có điện trở suất cao, hoặc lõi ferit ở tần số cao.

**Lỗi thường gặp:**
- Cho rằng ghép lõi thép thành lá mỏng nhằm giảm từ thông — sai vì mục đích ngược lại: các lá được đặt song song với từ thông để không cản trở nó, chỉ nhằm cắt đứt đường đi của dòng xoáy trong mặt phẳng vuông góc.
- Nghĩ phanh điện từ có thể giữ xe đứng yên hoàn toàn — sai vì lực hãm tỉ lệ với tốc độ tương đối, khi tốc độ về 0 thì từ thông ngừng biến thiên và lực hãm cũng biến mất.
- Cho rằng bếp từ đun nóng được mọi loại nồi — sai vì cần vật liệu vừa dẫn điện vừa nhiễm từ để tập trung từ thông; nồi thuỷ tinh hay nhôm mỏng không sinh đủ dòng Foucault để làm nóng.

<sub>`lesson.physics.cam-ung.dong-foucault`</sub>

---

### 4. Hiện tượng tự cảm, mạch RL và năng lượng từ trường
*Self-inductance, RL circuits and magnetic energy* · THPT (lớp 10-12) · ap, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được hiện tượng tự cảm và ý nghĩa của độ tự cảm $L$
- Vận dụng được nghiệm hàm mũ của mạch RL để mô tả quá trình đóng và ngắt mạch
- Tính được năng lượng tích trữ trong cuộn cảm và mật độ năng lượng từ trường

## Mạch tự chống lại chính mình

Khi dòng qua cuộn dây thay đổi, từ thông riêng do chính nó tạo ra cũng thay đổi, sinh suất điện động cảm ứng ngay trong nó. Theo Lenz, suất điện động ấy chống lại sự thay đổi của dòng:

$$e_{tc} = -L\frac{di}{dt}, \qquad \Phi_{\text{riêng}} = Li$$

Cuộn cảm vì thế đóng vai trò "quán tính điện": nó không cho dòng tăng đột ngột cũng không cho dòng tắt đột ngột. Với ống dây dài:

$$L = \mu_0\mu_r n^2 V = \frac{\mu_0\mu_r N^2 S}{\ell}$$

Chú ý $L \propto N^2$: tăng số vòng gấp đôi làm độ tự cảm tăng gấp bốn, vì vừa tăng từ thông vừa tăng số vòng móc vòng.

## Mạch RL

**Đóng khoá:** $i(t) = \dfrac{\mathcal{E}}{R}\left(1 - e^{-t/\tau}\right)$ với $\tau = L/R$.

**Ngắt nguồn (có đường khép mạch):** $i(t) = I_0e^{-t/\tau}$.

So sánh với mạch RC giúp thấy tính đối ngẫu: tụ điện chống lại sự thay đổi **điện áp**, cuộn cảm chống lại sự thay đổi **dòng điện**. Ngay sau khi đóng khoá, cuộn cảm hành xử như chỗ hở mạch ($i = 0$); sau thời gian dài nó hành xử như dây dẫn thường ($e_{tc} = 0$). Đúng ngược với tụ điện.

## Vì sao tia lửa xuất hiện khi ngắt mạch

Nếu ngắt cuộn cảm mà không có đường cho dòng chảy tiếp, $di/dt$ có độ lớn khổng lồ, và $e_{tc} = -L\,di/dt$ có thể lên tới hàng nghìn vôn — đủ đánh thủng không khí ở khe công tắc. Đây là nguyên lí của bô-bin đánh lửa ô tô, nhưng cũng là mối nguy cho linh kiện bán dẫn. Giải pháp kĩ thuật là mắc **điốt dập** song song với cuộn dây để dòng có lối tắt dần an toàn.

## Năng lượng nằm trong từ trường

Công mà nguồn phải thực hiện để đưa dòng từ 0 lên $I$ được tích trữ dưới dạng năng lượng từ trường:

$$W = \frac{1}{2}LI^2, \qquad u = \frac{B^2}{2\mu_0}$$

Cặp công thức này song song hoàn hảo với $W = \frac{1}{2}CU^2$ và $u = \frac{1}{2}\varepsilon_0E^2$ của tụ điện. Sự đối xứng ấy không ngẫu nhiên — nó là dấu hiệu sớm rằng điện trường và từ trường là hai mặt của cùng một thực thể, điều mà Maxwell sẽ chứng minh trọn vẹn.

**Lỗi thường gặp:**
- Cho rằng dòng đạt ngay giá trị $\mathcal{E}/R$ khi đóng khoá — sai vì suất điện động tự cảm chống lại sự tăng của dòng, ngay sau khi đóng khoá dòng bằng 0 và tăng dần theo hàm mũ.
- Nhầm vai trò của cuộn cảm với tụ điện ở chế độ ổn định — sai vì ở chế độ dừng cuộn cảm là dây dẫn (điện áp trên nó bằng 0), còn tụ điện là chỗ hở (dòng qua nó bằng 0), hai hành vi hoàn toàn ngược nhau.
- Dùng $L \propto N$ khi tính độ tự cảm của ống dây — sai vì độ tự cảm tỉ lệ với BÌNH PHƯƠNG số vòng: mỗi vòng vừa góp phần tạo từ thông vừa là nơi từ thông móc vòng qua.

<sub>`lesson.physics.cam-ung.tu-cam-va-mach-rl`</sub>

---

### 5. Máy phát điện xoay chiều và máy biến áp
*AC generators and transformers* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Thiết lập được biểu thức suất điện động của khung dây quay đều trong từ trường đều
- Vận dụng được công thức máy biến áp lí tưởng và phân tích các nguồn tổn hao thực tế
- Giải thích được vì sao truyền tải điện năng phải dùng điện áp cao

## Máy phát điện: đổi $\alpha$ thay vì đổi $B$

Cho khung $N$ vòng, diện tích $S$, quay đều với tốc độ góc $\omega$ trong từ trường đều $B$. Góc giữa pháp tuyến và $\vec{B}$ biến thiên theo $\alpha = \omega t$, nên

$$\Phi = NBS\cos\omega t \;\Longrightarrow\; e = -\frac{d\Phi}{dt} = NBS\omega\sin\omega t$$

Ba kết luận đọc được ngay từ biểu thức:

- Suất điện động **hình sin**, biên độ $E_0 = NBS\omega$.
- $e$ lệch pha $\pi/2$ so với $\Phi$: khi khung ở vị trí từ thông cực đại (mặt khung vuông góc $\vec{B}$) thì $e = 0$, và ngược lại. Nghịch lí biểu kiến này biến mất khi nhớ rằng $e$ là đạo hàm.
- Tăng tốc độ quay làm tăng cả biên độ lẫn tần số.

## Máy biến áp

Dòng xoay chiều ở cuộn sơ cấp tạo từ thông biến thiên, lõi thép dẫn từ thông ấy sang cuộn thứ cấp. Mỗi vòng dây ở cả hai cuộn đều có cùng $d\Phi/dt$, nên

$$\frac{U_2}{U_1} = \frac{N_2}{N_1}$$

Với máy lí tưởng, công suất bảo toàn: $U_1I_1 = U_2I_2$, do đó **tăng áp thì giảm dòng** đúng theo tỉ lệ.

Điểm cốt lõi hay bị bỏ qua: máy biến áp **không hoạt động với dòng một chiều**. Dòng không đổi cho $d\Phi/dt = 0$, cuộn thứ cấp không sinh suất điện động nào, còn cuộn sơ cấp có điện trở nhỏ nên bị đoản mạch và cháy.

## Vì sao phải truyền tải ở điện áp cao

Công suất hao phí trên đường dây:

$$\Delta P = I^2R_{\text{dây}} = \frac{P^2R_{\text{dây}}}{U^2\cos^2\varphi}$$

Hao phí tỉ lệ **nghịch với bình phương điện áp truyền tải**. Nâng điện áp từ 22 kV lên 220 kV (gấp 10) làm hao phí giảm 100 lần. Đây là lí do duy nhất và đầy đủ cho hệ thống lưới điện cao thế: không phải để "đẩy điện đi xa", mà để giảm dòng nhằm giảm nhiệt Joule trên dây.

Hiệu suất truyền tải $H = 1 - \Delta P/P$. Đến nơi tiêu thụ, máy hạ áp đưa điện áp về mức an toàn.

## Tổn hao thực tế của máy biến áp

Bốn nguồn chính: điện trở cuộn dây (tổn hao đồng), dòng Foucault trong lõi (khắc phục bằng lá thép mỏng), từ trễ của vật liệu lõi (chọn thép silic), và rò từ thông ra ngoài lõi. Máy biến áp lớn hiện đại đạt hiệu suất trên 99%, thuộc loại máy hiệu quả nhất mà con người chế tạo được — chính vì nó không có bộ phận chuyển động nào.

**Lỗi thường gặp:**
- Dùng công thức $\Delta P = U^2/R$ cho hao phí đường dây — sai vì $U$ trong đó phải là độ giảm thế TRÊN DÂY chứ không phải điện áp truyền tải; công thức an toàn luôn là $\Delta P = I^2R$.
- Cho rằng máy biến áp làm việc được với nguồn một chiều — sai vì cần từ thông biến thiên mới sinh suất điện động ở cuộn thứ cấp; với dòng không đổi thì $d\Phi/dt = 0$ và cuộn sơ cấp còn có nguy cơ cháy.
- Nghĩ suất điện động cực đại khi từ thông cực đại — sai vì $e$ tỉ lệ với tốc độ biến thiên của từ thông; tại đỉnh đồ thị từ thông, đạo hàm bằng 0 nên suất điện động cũng bằng 0.

<sub>`lesson.physics.cam-ung.may-phat-dien-va-may-bien-ap`</sub>

---

## Unit 5: Momentum and Impulse (AP Physics 1 Unit 4 / IB A.2 / CIE 9702 Topic 3)

### 1. Động lượng, xung lượng và đồ thị lực - thời gian
*Momentum, impulse and force-time graphs* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Tính được xung lượng của lực từ diện tích dưới đồ thị lực - thời gian
- Vận dụng được định lí xung lượng - động lượng để giải thích nguyên lí giảm chấn
- Phát biểu được định luật II Newton dưới dạng tổng quát theo động lượng

## Dạng gốc của định luật II Newton

Newton không viết $F = ma$; ông viết lực bằng tốc độ biến thiên của "lượng chuyển động":

$$\sum\vec{F} = \frac{d\vec{p}}{dt}$$

Khi $m$ không đổi, dạng này rút về $\sum\vec{F} = m\vec{a}$. Nhưng với **hệ có khối lượng thay đổi** (tên lửa phụt khí, băng tải đổ cát), chỉ dạng động lượng mới còn đúng. Đó là lí do AP Physics C và A-Level nhấn mạnh dạng này.

Nhân hai vế với $dt$ và lấy tích phân:

$$\vec{J} = \int_{t_1}^{t_2}\vec{F}\,dt = \Delta\vec{p}$$

## Đọc đồ thị lực - thời gian

Trong va chạm thật, lực không hề là hằng số: nó tăng vọt rồi giảm về 0 trong vài mili giây. Đồ thị $F$-$t$ có dạng đỉnh nhọn, và **diện tích dưới đồ thị chính là xung lượng**. Lực trung bình được định nghĩa sao cho hình chữ nhật cùng diện tích: $\bar{F} = \Delta p/\Delta t$.

## Nguyên lí của mọi thiết bị an toàn

Khi va chạm, $\Delta p$ do trạng thái đầu và cuối quyết định, ta **không thay đổi được**. Nhưng

$$\bar{F} = \frac{\Delta p}{\Delta t}$$

cho thấy kéo dài thời gian va chạm sẽ giảm lực. Túi khí, mũ bảo hiểm, đệm nhảy cao, vùng biến dạng của ô tô, động tác gập gối khi tiếp đất — tất cả đều làm tăng $\Delta t$ để giảm $\bar{F}$ trong khi $\Delta p$ giữ nguyên.

## So sánh với năng lượng

Động lượng là **vectơ** và bảo toàn trong mọi va chạm của hệ kín; động năng là **vô hướng** và chỉ bảo toàn trong va chạm đàn hồi. Hai công cụ bổ trợ nhau: dùng động lượng khi có va chạm hay nổ, dùng năng lượng khi có độ cao hay biến dạng.

**Lỗi thường gặp:**
- Tính $\Delta p = m(v_f - v_i)$ bằng cách trừ hai tốc độ mà quên dấu. Với bóng bật ngược lại, $\Delta p = m(12 - 15)$ cho 0,6 kg.m/s thay vì 5,4 kg.m/s — sai gần chín lần vì bỏ qua tính vectơ.
- Nhầm xung lượng với động lượng. Động lượng là trạng thái của vật tại một thời điểm; xung lượng là tác động của lực trong một khoảng thời gian, hai đại lượng chỉ trùng đơn vị chứ không cùng ý nghĩa.
- Cho rằng túi khí làm giảm độ biến thiên động lượng. $\Delta p$ được quyết định bởi tốc độ trước và sau va chạm; túi khí chỉ kéo dài $\Delta t$ nên hạ lực trung bình xuống, hoàn toàn không đụng tới $\Delta p$.

<sub>`lesson.physics.dong-luong-intl.xung-luong-va-dong-luong`</sub>

---

### 2. Định luật bảo toàn động lượng và chuyển động bằng phản lực
*Conservation of momentum and rocket propulsion* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Chứng minh được định luật bảo toàn động lượng từ định luật III Newton
- Xác định được khi nào một hệ được coi là kín để áp dụng định luật
- Vận dụng được bảo toàn động lượng theo từng thành phần trong bài toán hai chiều

## Từ định luật III tới định luật bảo toàn

Xét hai vật tương tác. Theo định luật III, $\vec{F}_{12} = -\vec{F}_{21}$ tại mọi thời điểm. Nhân với $\Delta t$ chung:

$$\Delta\vec{p}_1 = -\Delta\vec{p}_2 \Rightarrow \Delta(\vec{p}_1 + \vec{p}_2) = 0$$

Vậy bảo toàn động lượng **không phải một định luật mới**, nó là hệ quả trực tiếp của định luật III cộng với việc không có ngoại lực.

$$\sum \vec{p}_{\text{trước}} = \sum \vec{p}_{\text{sau}}$$

## Hệ kín tới mức nào là đủ

Trong thực tế hiếm có hệ kín tuyệt đối. Nhưng va chạm hoặc nổ diễn ra trong thời gian rất ngắn, nên xung lượng của ngoại lực (trọng lực, ma sát) là $F\Delta t$ với $\Delta t$ cực nhỏ, không đáng kể so với xung lượng nội lực. Vì thế ta vẫn áp dụng định luật cho hai viên bi va nhau trên bàn có ma sát, miễn là chỉ so sánh ngay trước và ngay sau va chạm.

Một mẹo hữu ích: nếu ngoại lực chỉ có theo phương đứng (trọng lực), thì **thành phần nằm ngang** của động lượng vẫn bảo toàn ngay cả khi tổng động lượng không bảo toàn.

## Súng giật và tên lửa

Súng khối lượng $M$ bắn đạn $m$ với vận tốc $v$: ban đầu tổng động lượng bằng 0 nên

$$MV + mv = 0 \Rightarrow V = -\frac{m}{M}v$$

Súng giật ngược lại, tốc độ nhỏ hơn nhiều lần vì $M \gg m$.

Tên lửa hoạt động cùng nguyên lí, và **không cần môi trường để đẩy vào** — đây là điểm mà trực giác đời thường hay sai. Trong chân không tên lửa vẫn bay được vì nó đẩy chính khối khí của mình. Lực đẩy: $F = v_{\text{khí}}\dfrac{dm}{dt}$.

## Va chạm hai chiều

Viết riêng hai phương trình cho $x$ và $y$. Với hai quả bi-a, chọn trục $Ox$ dọc theo hướng bi tới sẽ làm một trong hai phương trình có vế trái đơn giản nhất.

**Lỗi thường gặp:**
- Áp dụng bảo toàn động lượng cho hệ có ngoại lực đáng kể trong thời gian dài. Xe phanh trên đường mất dần động lượng vì ma sát là ngoại lực; chỉ trong khoảng thời gian va chạm cực ngắn ta mới bỏ qua được ngoại lực.
- Cộng động lượng như cộng số vô hướng trong bài hai chiều. Phải chiếu lên hai trục rồi giải hai phương trình độc lập; cộng độ lớn sẽ vi phạm bảo toàn theo từng phương.
- Cho rằng tên lửa bay được nhờ đẩy vào không khí phía sau. Nếu vậy tên lửa sẽ vô dụng trong vũ trụ; thực tế nó đẩy vào chính khối khí phụt ra, và không khí bên ngoài chỉ gây thêm lực cản.

<sub>`lesson.physics.dong-luong-intl.bao-toan-dong-luong`</sub>

---

### 3. Va chạm đàn hồi, va chạm mềm và hệ số phục hồi
*Elastic collisions, inelastic collisions and the coefficient of restitution* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phân loại được va chạm dựa trên sự bảo toàn hay không bảo toàn động năng
- Giải được bài toán va chạm đàn hồi trực diện bằng hệ hai phương trình bảo toàn
- Vận dụng được hệ số phục hồi để mô tả va chạm trung gian giữa hai trường hợp giới hạn

## Một định luật luôn đúng, một định luật có điều kiện

Trong **mọi** va chạm của hệ kín, động lượng bảo toàn. Động năng thì tuỳ:

| Loại va chạm | Động lượng | Động năng | $e$ |
|---|---|---|---|
| Đàn hồi | Bảo toàn | Bảo toàn | 1 |
| Không đàn hồi một phần | Bảo toàn | Giảm | $0 < e < 1$ |
| Hoàn toàn không đàn hồi (mềm) | Bảo toàn | Giảm nhiều nhất | 0 |

Phần động năng mất đi chuyển thành nội năng, âm thanh và biến dạng dẻo — không hề "biến mất".

## Va chạm đàn hồi trực diện

Giải hệ hai phương trình bảo toàn cho kết quả gọn đáng nhớ:

$$v_1' = \frac{(m_1-m_2)v_1 + 2m_2v_2}{m_1+m_2}, \qquad v_2' = \frac{(m_2-m_1)v_2 + 2m_1v_1}{m_1+m_2}$$

Ba trường hợp đặc biệt nên thuộc:

- $m_1 = m_2$: hai vật **hoán đổi vận tốc**. Đây là nguyên lí của con lắc Newton.
- $m_1 \ll m_2$ (bóng đập tường): vật nhẹ bật ngược lại gần như cùng tốc độ.
- $m_1 \gg m_2$: vật nặng đi tiếp gần như không đổi, vật nhẹ bị bắn đi với tốc độ gần $2v_1$.

## Mẹo tính nhanh

Thay vì giải hệ bậc hai, dùng cặp phương trình tuyến tính: bảo toàn động lượng cộng với hệ thức phục hồi

$$v_2' - v_1' = -e(v_2 - v_1)$$

Với $e=1$, đây chính là "tốc độ tách xa bằng tốc độ tiến lại gần", hệ quả tương đương với bảo toàn động năng nhưng dễ giải hơn nhiều.

## Bóng nảy

Thả bóng từ độ cao $h$, nảy lên $h'$. Vì $v \propto \sqrt{h}$ nên $e = \sqrt{h'/h}$, và sau $n$ lần nảy độ cao còn $h_n = e^{2n}h$. Đây là bài thực nghiệm chuẩn để đo $e$ trong IB internal assessment.

**Lỗi thường gặp:**
- Dùng bảo toàn cơ năng cho giai đoạn đạn cắm vào gỗ. Đó là va chạm mềm, phần lớn động năng chuyển thành nhiệt; chỉ động lượng mới bảo toàn ở giai đoạn này.
- Cho rằng động lượng cũng bảo toàn ở giai đoạn con lắc đi lên. Lúc đó dây và trọng lực là ngoại lực tác dụng trong thời gian dài, động lượng thay đổi rõ rệt; ngược lại cơ năng thì bảo toàn.
- Nghĩ va chạm mềm là va chạm mất toàn bộ động năng. Nếu mất hết thì hệ đứng yên, vi phạm bảo toàn động lượng; động năng còn lại đúng bằng động năng của khối tâm, chỉ phần động năng chuyển động tương đối mới mất đi.

<sub>`lesson.physics.dong-luong-intl.va-cham-va-he-so-phuc-hoi`</sub>

---

### 4. Khối tâm và chuyển động của khối tâm
*Centre of mass and motion of the centre of mass* · THPT (lớp 10-12) · ap, a-level, olympiad · 50 phút · nang-cao

**Mục tiêu:**
- Xác định được vị trí khối tâm của hệ chất điểm và của vật đồng chất đối xứng
- Chứng minh được định luật II Newton áp dụng cho khối tâm của hệ
- Giải thích được vì sao quỹ đạo khối tâm không đổi khi hệ nổ hoặc va chạm

## Một điểm đại diện cho cả hệ

Ném một chiếc cờ-lê xoay tít trong không trung: mọi điểm của nó vẽ những đường loằng ngoằng, **trừ một điểm** vẽ đúng một parabol đẹp. Điểm đó là khối tâm.

$$\vec{r}_C = \frac{\sum m_i \vec{r}_i}{\sum m_i}, \qquad \vec{v}_C = \frac{\sum m_i\vec{v}_i}{M} = \frac{\vec{p}_{\text{hệ}}}{M}$$

## Định lí then chốt

Cộng định luật II cho mọi hạt trong hệ. Theo định luật III, nội lực triệt tiêu từng cặp, chỉ còn ngoại lực:

$$\sum\vec{F}_{\text{ngoại}} = M\vec{a}_C$$

Hệ quả mạnh mẽ: **nội lực dù dữ dội đến đâu cũng không làm đổi chuyển động của khối tâm**. Quả pháo hoa nổ tung giữa không trung, các mảnh bay tứ tán, nhưng khối tâm của toàn bộ mảnh vẫn tiếp tục đúng parabol cũ cho tới khi mảnh đầu tiên chạm đất.

Nếu $\sum\vec{F}_{\text{ngoại}} = 0$ thì $\vec{v}_C$ không đổi — đây chính là bảo toàn động lượng viết theo ngôn ngữ khối tâm.

## Cách tìm khối tâm

- Vật đồng chất có tâm đối xứng: khối tâm ở tâm đối xứng.
- Vật ghép từ nhiều phần: coi mỗi phần là một chất điểm đặt tại khối tâm riêng, rồi lấy trung bình có trọng số.
- Vật có lỗ khoét: dùng "khối lượng âm" cho phần bị khoét — mẹo tiết kiệm rất nhiều công.
- Vật liên tục: $\vec{r}_C = \dfrac{1}{M}\int \vec{r}\,dm$.

Lưu ý khối tâm có thể nằm **ngoài** vật, ví dụ tâm của chiếc nhẫn hay của boomerang.

## Trọng tâm có phải khối tâm không

Trong trường trọng lực đều, hai điểm trùng nhau. Với vật rất lớn (một ngọn núi, một hành tinh) mà $g$ thay đổi theo vị trí, trọng tâm lệch nhẹ về phía có $g$ lớn hơn. Ở bậc phổ thông ta luôn coi chúng trùng nhau.

**Lỗi thường gặp:**
- Cho rằng khối tâm luôn nằm trên vật. Với chiếc nhẫn, chữ V hay boomerang, khối tâm nằm trong khoảng trống; đó vẫn là điểm hợp lệ vì nó chỉ là trung bình có trọng số của các vị trí.
- Nghĩ nội lực có thể làm khối tâm chuyển động. Nội lực xuất hiện thành cặp trực đối nên triệt tiêu trong tổng; không ai tự nhấc mình lên bằng cách kéo dây giày của chính mình.
- Lấy trung bình cộng vị trí mà quên trọng số khối lượng. Hai vật cách nhau 3 m với khối lượng 1 kg và 2 kg có khối tâm cách vật nặng 1 m chứ không phải ở trung điểm.

<sub>`lesson.physics.dong-luong-intl.khoi-tam-va-chuyen-dong-khoi-tam`</sub>

---

## Unit 6: IPhO - Phương pháp giải và vòng thực hành

### 1. Phân tích thứ nguyên và định lí Buckingham Pi
*Dimensional analysis and the Buckingham Pi theorem* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được thứ nguyên của một đại lượng theo hệ cơ sở MLT
- Vận dụng được định lí Buckingham Pi để đếm số tham số không thứ nguyên độc lập
- Giải thích được vì sao phân tích thứ nguyên không xác định được hệ số không thứ nguyên

## Vì sao thứ nguyên là bước đầu tiên

Trước khi giải, hãy hỏi: **đáp số phải có thứ nguyên gì, và ta có những đại lượng nào?** Nhiều bài IPhO chỉ cần đúng bước này là ra công thức đúng tới một hệ số không thứ nguyên. Ngay cả khi không giải trọn, một công thức đúng thứ nguyên đã ăn phần điểm đáng kể.

## Quy trình Buckingham Pi

1. Liệt kê $n$ đại lượng liên quan.
2. Viết thứ nguyên mỗi đại lượng theo hệ cơ sở (thường $\mathrm{M,L,T}$, thêm $\Theta$ cho nhiệt độ, $\mathrm{I}$ cho dòng điện).
3. Xác định $k$ = hạng của ma trận thứ nguyên.
4. Lập $n-k$ tổ hợp không thứ nguyên $\Pi_1,\dots,\Pi_{n-k}$.
5. Quan hệ vật lí có dạng $f(\Pi_1,\dots,\Pi_{n-k})=0$.

Trường hợp đẹp nhất là $n-k=1$: khi đó $\Pi_1$ phải bằng hằng số, và ta có công thức tới một hệ số.

## Ví dụ mẫu

Chu kì con lắc đơn phụ thuộc $\ell$, $g$, $m$, biên độ góc $\theta_0$. Có $n=4$ đại lượng có thứ nguyên (bỏ $\theta_0$ vì đã không thứ nguyên), $k=3$ ($\mathrm{M,L,T}$). Vậy $n-k=1$ tổ hợp: $\Pi=T\sqrt{g/\ell}$. Kết luận $T=F(\theta_0)\sqrt{\ell/g}$ — khối lượng **không** ảnh hưởng, và toàn bộ phụ thuộc biên độ nằm trong hàm $F$ chưa xác định. Giá trị $F(0)=2\pi$ phải lấy từ lời giải động lực học.

## Ước lượng bậc độ lớn

Sau khi có công thức, hãy thay số bằng **luỹ thừa của 10** để kiểm tra tính hợp lí. Nếu ra khối lượng Mặt Trời $10^{50}$ kg thì chắc chắn có lỗi. Rèn thói quen ước lượng bằng cách nhớ vài mốc: $g\approx10$, $c\approx3\times10^8$, $R_{\text{Trái Đất}}\approx6\times10^6$ m, mật độ nước $10^3$ kg/m$^3$.

## Giới hạn cần nói rõ

Phân tích thứ nguyên **không** cho hệ số không thứ nguyên ($2\pi$, $\frac12$, $\sqrt3$), và **thất bại** khi có nhiều hơn một tổ hợp $\Pi$ độc lập hoặc khi bài chứa sẵn tỉ số không thứ nguyên (góc, chiết suất, hệ số ma sát). Khi ấy phải bổ sung lập luận vật lí.

**Lỗi thường gặp:**
- Bỏ sót một đại lượng chi phối khi lập danh sách — sai vì khi đó số tổ hợp $\Pi$ tính ra ít hơn thực tế, cho một công thức đơn nhất trong khi đáp án thật còn phụ thuộc một tham số không thứ nguyên.
- Thêm quá nhiều đại lượng không liên quan — sai vì mỗi đại lượng thừa làm tăng số tổ hợp $\Pi$, kết luận trở nên vô nghĩa dạng 'hàm chưa biết của nhiều biến'.
- Kết luận công thức đầy đủ kể cả hệ số — sai vì phân tích thứ nguyên chỉ xác định các số mũ; hệ số như $2\pi$ hay $\frac{1}{2}$ nằm ngoài tầm của phương pháp.

<sub>`lesson.physics.ipho.thu-nguyen-va-buckingham-pi`</sub>

---

### 2. Chọn hệ quy chiếu khôn ngoan: hệ khối tâm và hệ quay
*Choosing a smart reference frame* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Vận dụng được hệ quy chiếu khối tâm để đơn giản hoá bài toán va chạm và hai vật
- Xác định được các lực quán tính xuất hiện trong hệ phi quán tính
- Phân tích được khi nào chuyển hệ quy chiếu làm bài toán khó lên

## Nguyên tắc: chọn hệ làm biến mất một đại lượng

Bài toán không đổi, nhưng độ khó thì đổi theo hệ quy chiếu. Chọn hệ sao cho một đại lượng phiền phức triệt tiêu.

## Hệ khối tâm (hệ C)

Trong hệ C, tổng động lượng bằng 0. Hệ quả:

- Va chạm hai vật: hai động lượng luôn **ngược chiều và bằng độ lớn**, nên va chạm đàn hồi chỉ **quay** vectơ động lượng mà không đổi độ lớn. Bài toán ba chiều rút về một góc quay.
- Định lí König: $E_{\text{đ}}=\frac12Mv_C^2+E_{\text{đ,riêng}}$. Phần $\frac12Mv_C^2$ không bao giờ chuyển hoá được, nên **năng lượng khả dụng** cho phản ứng chính là $E_{\text{đ,riêng}}$.
- Bài hai vật với lực xuyên tâm rút về **bài một vật** khối lượng rút gọn $\mu=\frac{m_1m_2}{m_1+m_2}$ trong trường thế.

## Hệ tịnh tiến có gia tốc

Bổ sung lực quán tính $-m\vec a_0$ đều cho mọi vật; nó **có thế** nên vẫn bảo toàn được "cơ năng" mở rộng. Ứng dụng kinh điển: con lắc trong toa tàu tăng tốc — đổi sang hệ toa tàu, trọng lực hiệu dụng $\vec g_{\text{hd}}=\vec g-\vec a_0$, bài trở thành con lắc thường với $g$ mới và phương thẳng đứng mới.

## Hệ quay

Bổ sung hai lực: li tâm $m\omega^2\vec r_\perp$ (có thế, thế năng $-\frac12m\omega^2r_\perp^2$) và Coriolis $-2m\vec\omega\times\vec v'$. Điểm mấu chốt: **lực Coriolis không sinh công** vì luôn vuông góc vận tốc, nên định luật bảo toàn năng lượng trong hệ quay vẫn dùng được với thế năng li tâm.

## Khi nào KHÔNG nên đổi hệ

- Khi bài hỏi đại lượng đo trong hệ phòng thí nghiệm và việc chuyển đổi ngược phức tạp hơn lời giải trực tiếp.
- Khi có nhiều vật với gia tốc khác nhau — không có một hệ nào làm mọi thứ đơn giản.
- Trong bài tương đối tính, phép cộng vận tốc Galilei sai; phải dùng biến đổi Lorentz và bất biến $E^2-p^2c^2$.

Hãy viết rõ trong bài: "Xét trong hệ quy chiếu ..., trong đó xuất hiện thêm lực quán tính ...". Không ghi câu đó là mất điểm trình bày.

**Lỗi thường gặp:**
- Dùng bảo toàn năng lượng trong hệ phi quán tính mà quên thế năng của lực li tâm — sai vì lực li tâm sinh công; bỏ nó ra khỏi bảng năng lượng làm phương trình mất cân bằng.
- Thêm lực Coriolis vào phương trình năng lượng — sai vì lực Coriolis luôn vuông góc với vận tốc trong hệ quay nên công của nó bằng 0; đưa vào là đếm thừa.
- Cộng vận tốc theo Galilei trong bài hạt chuyển động gần tốc độ ánh sáng — sai vì phép cộng đó chỉ đúng khi $v\ll c$; với hạt tương đối tính phải dùng biến đổi Lorentz.

<sub>`lesson.physics.ipho.chon-he-quy-chieu`</sub>

---

### 3. Khai thác tính đối xứng và các định luật bảo toàn
*Exploiting symmetry and conservation laws* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được đại lượng bảo toàn tương ứng với mỗi phép đối xứng của hệ
- Vận dụng được đối xứng để giảm số biến trước khi viết phương trình động lực học
- Phân tích được điều kiện để một định luật bảo toàn còn áp dụng được

## Bảng đối xứng - bảo toàn

| Hệ bất biến dưới | Đại lượng bảo toàn |
|---|---|
| Tịnh tiến thời gian (không có lực phụ thuộc $t$) | Năng lượng |
| Tịnh tiến theo phương $x$ | $p_x$ |
| Quay quanh trục $z$ | $L_z$ |
| Đối xứng cầu (trường xuyên tâm) | cả vectơ $\vec L$ |
| Đối xứng Coulomb/Kepler | thêm vectơ Laplace-Runge-Lenz |

Quy tắc thực hành: **nhìn vào thế năng**. Nếu $U$ không phụ thuộc $x$ thì $p_x$ bảo toàn; nếu $U$ chỉ phụ thuộc $r$ thì $\vec L$ bảo toàn và quỹ đạo nằm trong một mặt phẳng.

## Đối xứng giúp giảm biến trước khi tính

Một bài ba chiều với trường xuyên tâm: bảo toàn $\vec L$ ép quỹ đạo phẳng (giảm từ 3 xuống 2 chiều), bảo toàn $|\vec L|$ cho $r^2\dot\varphi=$ const (khử $\varphi$), bảo toàn năng lượng cho phương trình một biến $r$. Ba chiều thành một chiều **trước khi** viết một dòng tích phân nào.

## Đối xứng hình học trong tĩnh điện và từ

Đối xứng cầu, trụ, phẳng quyết định dạng của $\vec E$ và $\vec B$, cho phép dùng định lí Gauss và định lí Ampère. Trước khi lấy tích phân, hãy nói rõ: "do đối xứng trụ, $\vec E$ hướng xuyên tâm và độ lớn chỉ phụ thuộc $r$". Không có câu này thì việc rút $E$ ra khỏi tích phân là không hợp lệ.

## Khi nào định luật bảo toàn KHÔNG dùng được

- **Năng lượng**: khi có ma sát, va chạm mềm, hoặc ràng buộc phụ thuộc thời gian (ví dụ dây bị kéo ngắn dần) — khi đó ngoại lực sinh công.
- **Động lượng**: khi có ngoại lực theo phương đó; nhưng thường vẫn bảo toàn theo **một phương** riêng (ví dụ phương ngang khi chỉ có trọng lực).
- **Mômen động lượng**: khi có mômen ngoại lực đối với điểm/trục đang xét. Chú ý mômen động lượng có thể bảo toàn đối với điểm này mà không đối với điểm khác.

Luôn ghi rõ **đối với điểm nào** và **trong khoảng thời gian nào** khi viết bảo toàn mômen động lượng.

**Lỗi thường gặp:**
- Dùng bảo toàn cơ năng khi có ngoại lực sinh công (kéo dây, ma sát) — sai vì cơ năng chỉ bảo toàn khi mọi lực sinh công đều là lực thế; ở đây tay người bơm năng lượng vào hệ.
- Viết bảo toàn mômen động lượng mà không nói đối với điểm nào — sai vì mômen động lượng phụ thuộc gốc quy chiếu; nó có thể bảo toàn với gốc này và không bảo toàn với gốc khác.
- Rút $E$ ra khỏi tích phân Gauss khi hệ không đủ đối xứng — sai vì bước đó chỉ hợp lệ khi độ lớn trường là hằng số trên mặt Gauss, điều chỉ bảo đảm bởi đối xứng cầu, trụ hoặc phẳng.

<sub>`lesson.physics.ipho.doi-xung-va-bao-toan`</sub>

---

### 4. Xấp xỉ và khai triển bậc nhất: nghệ thuật giữ đúng số hạng
*Approximations and first-order expansions* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Vận dụng được khai triển nhị thức và Taylor bậc nhất cho các biểu thức vật lí
- Xác định được tham số nhỏ và bậc cần giữ trong từng bài toán
- Phân tích được sai số bỏ qua khi cắt cụt khai triển

## Vì sao xấp xỉ là kỹ năng cốt lõi của IPhO

Rất nhiều bài IPhO không có nghiệm giải tích chính xác, hoặc nghiệm chính xác vô dụng. Đề thường hỏi thẳng "tính tới bậc nhất theo $x/R$". Người biết xấp xỉ đúng bậc làm trong 10 phút; người cố tính chính xác hết giờ.

## Bộ khai triển phải thuộc lòng

$$(1+\varepsilon)^n\approx1+n\varepsilon+\frac{n(n-1)}{2}\varepsilon^2,\qquad \frac{1}{1\pm\varepsilon}\approx1\mp\varepsilon+\varepsilon^2,$$
$$\sin\varepsilon\approx\varepsilon-\frac{\varepsilon^3}{6},\quad \cos\varepsilon\approx1-\frac{\varepsilon^2}{2},\quad \tan\varepsilon\approx\varepsilon+\frac{\varepsilon^3}{3},$$
$$e^\varepsilon\approx1+\varepsilon+\frac{\varepsilon^2}{2},\qquad \ln(1+\varepsilon)\approx\varepsilon-\frac{\varepsilon^2}{2}.$$

## Quy tắc chọn bậc

Giữ tới bậc **thấp nhất khác không** của đại lượng cần tính. Nguyên tắc vàng: nếu số hạng bậc nhất **triệt tiêu** (thường do đối xứng), phải giữ tới bậc hai. Ví dụ kinh điển: lực thuỷ triều là hiệu hai lực hấp dẫn gần bằng nhau, bậc nhất triệt tiêu, kết quả tỉ lệ $1/r^3$ chứ không phải $1/r^2$.

## Ba bước làm chuẩn

1. **Xác định tham số nhỏ không thứ nguyên** $\varepsilon$. Phải không thứ nguyên, nếu không thì "nhỏ" vô nghĩa.
2. Viết đại lượng cần tính dưới dạng hàm của $\varepsilon$, đưa về dạng $(1+\varepsilon)^n$ hoặc dạng chuẩn.
3. Khai triển, giữ đúng bậc, và **nói rõ số hạng bỏ đi là bậc mấy**.

## Cạm bẫy hiệu hai số gần bằng nhau

Khi trừ hai đại lượng gần bằng nhau, sai số tương đối bùng nổ. Phải khai triển **trước khi** trừ, không phải sau. Ví dụ: tính $\sqrt{R^2+h^2}-R$ với $h\ll R$ bằng cách viết $R\left(\sqrt{1+h^2/R^2}-1\right)\approx\frac{h^2}{2R}$, chứ không bấm máy hai căn rồi trừ.

## Kiểm tra kết quả

Sau khi xấp xỉ, luôn kiểm tra hai giới hạn: $\varepsilon\to0$ phải cho kết quả đã biết, và thứ nguyên phải đúng. Nếu công thức xấp xỉ có $\varepsilon$ ở mẫu mà không có ở tử, gần như chắc chắn đã sai dấu hoặc sai bậc.

**Lỗi thường gặp:**
- Khai triển theo một đại lượng CÓ thứ nguyên — sai vì 'nhỏ' chỉ có nghĩa khi so với một đại lượng cùng thứ nguyên; phải lập tỉ số không thứ nguyên trước khi nói nó nhỏ.
- Trừ hai số gần bằng nhau bằng máy tính rồi mới xấp xỉ — sai vì hiện tượng mất chữ số có nghĩa: hai số giống nhau tới 6 chữ số cho hiệu chỉ còn vài chữ số đáng tin.
- Dừng ở bậc nhất khi bậc nhất triệt tiêu — sai vì kết quả sẽ ra 0, che mất hiệu ứng thật nằm ở bậc hai; phải kiểm tra số hạng giữ lại có khác 0 hay không.

<sub>`lesson.physics.ipho.xap-xi-bac-nhat`</sub>

---

### 5. Dao động nhỏ quanh vị trí cân bằng: quy trình bốn bước
*Small oscillations about equilibrium* · THPT (lớp 10-12) · olympiad · 45 phút · chuyen-sau

**Mục tiêu:**
- Xác định được vị trí cân bằng bền từ điều kiện cực tiểu của thế năng
- Tính được tần số dao động nhỏ từ đạo hàm cấp hai của thế năng hiệu dụng
- Vận dụng được khối lượng hiệu dụng khi hệ có ràng buộc

## Vì sao mọi hệ đều dao động điều hoà quanh cân bằng bền

Gần cực tiểu của thế năng, khai triển Taylor cho

$$U(q)\approx U(q_0)+\underbrace{U'(q_0)}_{=0}(q-q_0)+\frac12U''(q_0)(q-q_0)^2.$$

Số hạng bậc nhất triệt tiêu vì $q_0$ là điểm dừng. Còn lại đúng dạng thế năng lò xo với $k_{\text{hd}}=U''(q_0)$. Đó là lí do dao động điều hoà xuất hiện ở mọi nơi trong vật lí.

## Quy trình bốn bước

1. **Chọn một toạ độ suy rộng $q$** mô tả trọn vẹn cấu hình hệ.
2. **Viết động năng** dưới dạng $E_{\text{đ}}=\frac12m_{\text{hd}}(q)\dot q^2$ và **thế năng** $U(q)$. Nếu có định luật bảo toàn (mômen động lượng chẳng hạn), dùng nó để khử biến và thu $U_{\text{hd}}$.
3. **Tìm $q_0$** từ $U_{\text{hd}}'(q_0)=0$, kiểm tra $U_{\text{hd}}''(q_0)>0$ để bảo đảm cân bằng **bền**.
4. **Tần số**: $\omega=\sqrt{\dfrac{U_{\text{hd}}''(q_0)}{m_{\text{hd}}(q_0)}}$.

## Vì sao khối lượng hiệu dụng quan trọng

Với hệ có ràng buộc, động năng không phải $\frac12m\dot q^2$. Ví dụ quả cầu đặc lăn không trượt: $E_{\text{đ}}=\frac12mv^2+\frac12I\omega^2=\frac12\left(m+\frac{I}{R^2}\right)v^2=\frac{7}{10}mv^2$, tức $m_{\text{hd}}=\frac75m$. Quên phần quay là lỗi kinh điển làm tần số sai hệ số $\sqrt{7/5}$.

## Hệ nhiều bậc tự do

Với $n$ toạ độ, khai triển bậc hai cho hai ma trận: ma trận độ cứng $K_{ij}=\partial^2U/\partial q_i\partial q_j$ và ma trận khối lượng $M_{ij}$. Tần số riêng là nghiệm của $\det(K-\omega^2M)=0$; các vectơ riêng là **mode chuẩn**. Mẹo phòng thi: dùng đối xứng để đoán mode (đối xứng và phản đối xứng) trước khi giải định thức.

## Cảnh báo

- Nếu $U''(q_0)=0$, dao động **không** điều hoà; chu kì phụ thuộc biên độ, phải khai triển tới bậc bốn.
- Trong hệ quay, phải dùng $U_{\text{hd}}$ bao gồm thế năng li tâm, nếu không sẽ tìm sai vị trí cân bằng.

**Lỗi thường gặp:**
- Tính tần số bằng $\sqrt{U''/m}$ với $m$ là khối lượng thật trong hệ có ràng buộc quay hoặc lăn — sai vì động năng chứa thêm phần quay, khối lượng hiệu dụng lớn hơn nên tần số nhỏ hơn.
- Tìm vị trí cân bằng từ $U$ thay vì $U_{\text{hd}}$ khi hệ quay hoặc có mômen động lượng bảo toàn — sai vì bỏ qua rào li tâm, kết quả cho một điểm không phải cân bằng thật.
- Kết luận dao động điều hoà khi $U''(q_0)=0$ — sai vì khi đó thế năng gần cực tiểu là bậc bốn, chu kì phụ thuộc biên độ và không có tần số riêng cố định.

<sub>`lesson.physics.ipho.dao-dong-nho-quanh-can-bang`</sub>

---

### 7. Phương pháp tương tự: mượn lời giải từ bài toán khác
*Reasoning by analogy across physical systems* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được hai hệ vật lí có cùng phương trình mô tả dù bản chất khác nhau
- Vận dụng được phương pháp ảnh điện và phương pháp đường tải
- Phân tích được giới hạn của mỗi phép tương tự

## Vì sao tương tự là công cụ thật, không phải mẹo

Định lí duy nhất nghiệm nói: nếu hai bài toán có cùng phương trình và cùng điều kiện biên thì nghiệm giống nhau. Do đó khi nhận ra một bài đã được giải ở lĩnh vực khác, ta có quyền dùng lại kết quả.

## Bảng tương tự cần thuộc

| Cơ học | Điện | Nhiệt |
|---|---|---|
| $m$ | $L$ | nhiệt dung |
| $k$ | $1/C$ | - |
| $b$ (cản) | $R$ | $1/$độ dẫn nhiệt |
| $x$ | $q$ | nhiệt lượng |
| $\dot x$ | $I$ | dòng nhiệt |

Phương trình $m\ddot x+b\dot x+kx=F$ và $L\ddot q+R\dot q+q/C=\mathcal{E}$ **giống hệt nhau**; mọi kết quả về cộng hưởng, hệ số phẩm chất, tắt dần chuyển thẳng qua lại.

## Tương tự tĩnh điện - hấp dẫn - dẫn nhiệt

Cả ba đều là phương trình Laplace/Poisson. Kết quả về điện trường của quả cầu tích điện đều dịch ngay sang trường hấp dẫn của quả cầu đặc; bài dẫn nhiệt dừng qua vỏ cầu có cùng dạng với điện trở của vỏ cầu dẫn điện.

## Phương pháp ảnh điện

Điện tích $q$ cách mặt phẳng dẫn nối đất một đoạn $d$: thay mặt phẳng bằng điện tích $-q$ ở vị trí đối xứng. Trường trong nửa không gian chứa $q$ giống hệt trường của cặp lưỡng cực. Với quả cầu dẫn bán kính $R$ và điện tích $q$ ở cách tâm $d$: ảnh là $q'=-\dfrac{R}{d}q$ đặt cách tâm $\dfrac{R^2}{d}$.

**Bắt buộc kiểm tra**: ảnh phải nằm **ngoài** miền ta quan tâm, và điều kiện biên phải được tái tạo chính xác. Nếu không, phép thay thế vô hiệu.

## Phương pháp đường tải cho phần tử phi tuyến

Mạch có một phần tử phi tuyến (điốt, bóng đèn, quang trở) không giải được bằng đại số. Cách làm: vẽ đặc tuyến $I(U)$ của phần tử và **đường tải** $I=\dfrac{\mathcal E-U}{R}$ trên cùng hệ trục; giao điểm là điểm làm việc. Đây là phương pháp đồ thị chính thức, được chấm điểm đầy đủ ở IPhO.

## Giới hạn

Tương tự chỉ đúng khi **cả phương trình lẫn điều kiện biên** trùng khớp. Ví dụ tương tự cơ - điện hỏng khi hệ cơ có ma sát khô (lực không tỉ lệ vận tốc). Phải kiểm tra trước khi mượn kết quả.

**Lỗi thường gặp:**
- Tính năng lượng bằng thế năng của cặp điện tích thật và ảnh — sai vì điện tích ảnh không có thật; nó dịch chuyển khi điện tích thật dịch, nên phải lấy tích phân lực thay vì dùng công thức thế năng tĩnh.
- Đặt điện tích ảnh trong miền đang quan tâm — sai vì khi đó phương trình Poisson trong miền bị thay đổi (thêm một nguồn không có thật), nghiệm không còn tương ứng bài gốc.
- Áp tương tự cơ - điện cho hệ có ma sát khô — sai vì ma sát khô cho lực hằng số ngược chiều chuyển động, không tuyến tính theo vận tốc, nên phương trình không cùng dạng với mạch RLC.

<sub>`lesson.physics.ipho.phuong-phap-tuong-tu`</sub>

---

### 8. Vòng thực hành IPhO: xử lí số liệu, tuyến tính hoá và sai số
*IPhO experimental round: data handling, linearization and uncertainty* · THPT (lớp 10-12) · olympiad · 50 phút · nang-cao

**Mục tiêu:**
- Tuyến tính hoá được một quan hệ phi tuyến để vẽ đồ thị và lấy hệ số góc
- Tính được sai số lan truyền qua các phép toán và qua hàm nhiều biến
- Trình bày được kết quả với số chữ số có nghĩa đúng và sai số kèm theo

## Nguyên tắc số một: luôn tuyến tính hoá

Mắt người và phương pháp bình phương tối thiểu đều làm việc tốt nhất với **đường thẳng**. Trước khi vẽ, hãy biến đổi:

| Quan hệ giả định | Vẽ trục | Lấy gì từ đồ thị |
|---|---|---|
| $y=Ax^n$ | $\ln y$ theo $\ln x$ | hệ số góc $=n$, tung độ gốc $=\ln A$ |
| $y=Ae^{kx}$ | $\ln y$ theo $x$ | hệ số góc $=k$ |
| $T=2\pi\sqrt{\ell/g}$ | $T^2$ theo $\ell$ | hệ số góc $=4\pi^2/g$ |
| $\frac1v+\frac1u=\frac1f$ | $\frac1v$ theo $\frac1u$ | tung độ gốc $=1/f$ |

Mẹo: khi chưa biết dạng quan hệ, **luôn thử log-log trước** — nó phát hiện mọi quan hệ luỹ thừa.

## Sai số: ba quy tắc thực dụng

1. **Cộng trừ** $\to$ cộng sai số **tuyệt đối**: $\Delta(x\pm y)=\Delta x+\Delta y$.
2. **Nhân chia** $\to$ cộng sai số **tương đối**: $\delta(xy)=\delta x+\delta y$.
3. **Luỹ thừa** $\to$ nhân sai số tương đối với số mũ: $\delta(x^n)=|n|\,\delta x$.

Với hàm phức tạp, dùng $\Delta f\approx\sum\left|\frac{\partial f}{\partial x_i}\right|\Delta x_i$.

## Sai số của hệ số góc

Không ước lượng bằng mắt. Hai cách được chấp nhận:

- **Đường dốc nhất và thoải nhất**: vẽ hai đường còn đi qua hầu hết thanh sai số, lấy $\Delta a=\frac{a_{\max}-a_{\min}}{2}$.
- **Bình phương tối thiểu**: dùng công thức sai số chuẩn của hệ số góc; máy tính cầm tay thường có sẵn.

## Kỷ luật trình bày

- Sai số làm tròn về **một chữ số có nghĩa** (đôi khi hai nếu chữ số đầu là 1).
- Giá trị làm tròn tới cùng hàng thập phân với sai số: viết $g=(9{,}81\pm0{,}05)$ m/s$^2$, không viết $9{,}8123\pm0{,}05$.
- Luôn ghi **đơn vị** trên trục đồ thị và trong bảng số liệu.
- Vẽ **thanh sai số** cho mọi điểm.

## Chiến thuật thời gian vòng thực hành

1. Đọc hết đề trước khi chạm dụng cụ (10 phút) — nhiều phần độc lập, chọn phần dễ làm trước.
2. Đo **nhanh và thô** toàn dải trước để biết dạng đồ thị, rồi mới đo kỹ ở vùng quan trọng.
3. Vẽ đồ thị **ngay khi có dữ liệu**, không đợi tới cuối: điểm lạc sẽ lộ ra khi còn kịp đo lại.
4. Ghi số liệu thô vào bảng ngay, không tính nhẩm rồi ghi kết quả — giám khảo chấm cả bảng thô.

**Lỗi thường gặp:**
- Cộng sai số tuyệt đối cho phép nhân chia — sai vì với tích, sai số TƯƠNG ĐỐI mới cộng; cộng tuyệt đối cho kết quả sai cả về độ lớn lẫn thứ nguyên.
- Ghi kết quả với quá nhiều chữ số so với sai số — sai vì các chữ số nằm sau vị trí của sai số không mang thông tin; giám khảo trừ điểm trình bày định lượng.
- Vẽ đồ thị quan hệ phi tuyến rồi ước lượng tham số bằng mắt — sai vì mắt người không đánh giá được độ cong; phải tuyến tính hoá để tham số nằm ở hệ số góc của một đường thẳng.

<sub>`lesson.physics.ipho.xu-li-so-lieu-thuc-hanh`</sub>

---

## Unit 6: Rotational Motion (AP Physics 1 Unit 5-6 / AP Physics C Mechanics / IB A.4 HL)

### 1. Động học chuyển động quay của vật rắn
*Rotational kinematics of a rigid body* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được các đại lượng góc và mối liên hệ với các đại lượng dài tương ứng
- Vận dụng được bộ phương trình động học góc cho chuyển động quay biến đổi đều
- Phân tích được gia tốc toàn phần của một điểm trên vật rắn quay

## Một bộ công thức, hai ngôn ngữ

Mọi điểm trên một vật rắn quay có tốc độ dài khác nhau (điểm ngoài rìa đi nhanh hơn), nhưng **tốc độ góc thì như nhau**. Đó là lí do ta mô tả chuyển động quay bằng các đại lượng góc: một con số cho cả vật.

| Chuyển động thẳng | Chuyển động quay |
|---|---|
| $x$ | $\theta$ |
| $v = dx/dt$ | $\omega = d\theta/dt$ |
| $a = dv/dt$ | $\alpha = d\omega/dt$ |
| $v = v_0 + at$ | $\omega = \omega_0 + \alpha t$ |
| $x = x_0 + v_0t + \tfrac12 at^{2}$ | $\theta = \theta_0 + \omega_0 t + \tfrac12\alpha t^{2}$ |
| $v^{2} = v_0^{2} + 2a\Delta x$ | $\omega^{2} = \omega_0^{2} + 2\alpha\Delta\theta$ |

Sự tương ứng này không phải trùng hợp: cả hai đều là hệ quả của định nghĩa đạo hàm với đại lượng biến thiên đều. Vì vậy mọi kỹ năng đã có ở phần động học thẳng dùng lại được nguyên vẹn.

## Cầu nối giữa hai thế giới

$$s = r\theta, \qquad v = r\omega, \qquad a_t = r\alpha$$

**Bắt buộc dùng radian**. Nếu thay $\theta$ bằng độ, hệ thức $s = r\theta$ sai ngay, vì radian được định nghĩa chính là tỉ số cung trên bán kính.

## Gia tốc của một điểm có hai phần

Một điểm trên vành bánh xe đang tăng tốc có:

- $a_t = r\alpha$: dọc tiếp tuyến, làm đổi độ lớn vận tốc.
- $a_n = r\omega^{2} = v^{2}/r$: hướng vào trục, làm đổi hướng vận tốc.

Hai thành phần vuông góc nhau nên $a = \sqrt{a_t^{2} + a_n^{2}}$. Khi quay đều, $\alpha = 0$ nên chỉ còn thành phần hướng tâm — trở về đúng bài chuyển động tròn đều.

## Lưu ý phạm vi

Bộ phương trình góc trên chỉ dùng cho **gia tốc góc không đổi**, hệt như bộ SUVAT. Với mômen lực thay đổi (con lắc vật lí dao động), $\alpha$ biến thiên và phải quay lại phương trình vi phân.

**Lỗi thường gặp:**
- Dùng vòng/phút hoặc độ/giây trực tiếp trong công thức $v = r\omega$. Các hệ thức nối đại lượng dài và góc chỉ đúng với radian, vì định nghĩa radian là tỉ số độ dài cung trên bán kính.
- Cho rằng mọi điểm trên vật rắn quay có cùng gia tốc. Chúng có cùng $\omega$ và $\alpha$, nhưng $v = r\omega$ và $a_n = r\omega^{2}$ phụ thuộc khoảng cách tới trục nên khác nhau ở từng điểm.
- Bỏ qua thành phần hướng tâm khi tính gia tốc của một điểm đang quay nhanh dần. Ở tốc độ góc lớn, $a_n = r\omega^{2}$ thường lớn hơn $a_t$ hàng trăm lần và chi phối hoàn toàn gia tốc toàn phần.

<sub>`lesson.physics.chuyen-dong-quay-intl.dong-hoc-quay`</sub>

---

### 2. Mômen lực, ngẫu lực và cân bằng vật rắn
*Torque, couples and equilibrium of rigid bodies* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Tính được mômen lực đối với một trục quay theo cánh tay đòn và theo tích có hướng
- Vận dụng được hai điều kiện cân bằng của vật rắn để giải bài toán tĩnh học
- Giải thích được vì sao có thể chọn tùy ý điểm lấy mômen khi vật ở trạng thái cân bằng

## Vì sao tay nắm cửa đặt xa bản lề

Cùng một lực đẩy, đặt sát bản lề thì cửa gần như không nhúc nhích, đặt ở mép ngoài thì mở dễ dàng. Tác dụng làm quay phụ thuộc **cả độ lớn lực lẫn khoảng cách vuông góc từ trục tới giá của lực**:

$$\tau = F d_{\perp} = F r\sin\theta$$

Hai cách tính tương đương: hoặc lấy toàn bộ lực nhân cánh tay đòn, hoặc lấy thành phần vuông góc của lực nhân $r$. Dạng vectơ tổng quát là $\vec{\tau} = \vec{r}\times\vec{F}$.

Hệ quả tức thì: lực có giá **đi qua trục quay** cho $\tau = 0$, dù lực rất lớn. Đẩy vào bản lề thì cửa không quay.

## Hai điều kiện, không phải một

Một vật rắn cân bằng khi:

$$\sum F_x = 0, \qquad \sum F_y = 0, \qquad \sum \tau = 0$$

Chỉ có $\sum\vec{F} = 0$ là chưa đủ: ngẫu lực có hợp lực bằng 0 mà vẫn quay vật (vô lăng ô tô, mở nắp chai). Ngược lại, chỉ có $\sum\tau = 0$ cũng chưa đủ vì vật vẫn có thể trượt đi.

## Mẹo chọn trục

Khi vật cân bằng, $\sum\tau = 0$ đối với **mọi** điểm, kể cả điểm nằm ngoài vật. Hãy khai thác điều này: chọn trục đi qua điểm đặt của ẩn số mà ta chưa quan tâm, mômen của lực đó triệt tiêu và phương trình chỉ còn một ẩn. Với bài dầm hai gối đỡ, chọn lần lượt từng gối để tìm từng phản lực mà không cần giải hệ.

## Cân bằng của vật có mặt chân đế

Vật không đổ khi đường thẳng đứng qua trọng tâm còn cắt mặt chân đế. Mức vững vàng tăng khi trọng tâm thấp và chân đế rộng — nguyên lí của xe đua gầm thấp, của tháp nghiêng Pisa và của tư thế đứng tấn.

**Lỗi thường gặp:**
- Dùng khoảng cách từ trục tới điểm đặt lực thay vì cánh tay đòn vuông góc. Khi lực xiên góc $\theta$, chỉ thành phần vuông góc mới gây quay, nên $\tau = Fr\sin\theta$ chứ không phải $Fr$.
- Cho rằng $\sum\vec{F} = 0$ là đủ để vật rắn cân bằng. Ngẫu lực có hợp lực bằng 0 nhưng vẫn làm vật quay nhanh dần; phải kiểm tra thêm điều kiện mômen.
- Quên trọng lượng của chính thanh hoặc đặt nó sai vị trí. Với thanh đồng chất, trọng lực coi như đặt tại trung điểm; với thanh không đồng chất phải xác định trọng tâm trước khi lấy mômen.

<sub>`lesson.physics.chuyen-dong-quay-intl.momen-luc-va-can-bang-vat-ran`</sub>

---

### 3. Mômen quán tính và định lí trục song song
*Moment of inertia and the parallel-axis theorem* · THPT (lớp 10-12) · ap, a-level, olympiad · 50 phút · nang-cao

**Mục tiêu:**
- Tính được mômen quán tính của hệ chất điểm và của vật rắn đồng chất đơn giản
- Vận dụng được định lí trục song song để chuyển mômen quán tính giữa hai trục
- Giải thích được vì sao mômen quán tính phụ thuộc cách phân bố khối lượng chứ không chỉ khối lượng

## Khối lượng của chuyển động quay

Trong chuyển động thẳng, quán tính chỉ phụ thuộc khối lượng. Trong chuyển động quay, **vị trí của khối lượng cũng quan trọng**. Cùng một khối lượng, dồn ra xa trục thì rất khó quay:

$$I = \sum m_i r_i^{2}, \qquad I = \int r^{2}\,dm$$

Số mũ 2 khiến $I$ nhạy khủng khiếp với khoảng cách: dời khối lượng ra xa gấp đôi thì $I$ tăng gấp bốn. Đó là lí do vận động viên trượt băng co tay vào để quay nhanh, và vì sao bánh đà công nghiệp được thiết kế với vành nặng ở ngoài.

## Bảng cần thuộc

| Vật (khối lượng $M$) | Trục | $I$ |
|---|---|---|
| Vành tròn / trụ rỗng thành mỏng, bán kính $R$ | Trục đối xứng | $MR^{2}$ |
| Đĩa tròn / trụ đặc | Trục đối xứng | $\tfrac12 MR^{2}$ |
| Quả cầu đặc | Đường kính | $\tfrac25 MR^{2}$ |
| Vỏ cầu mỏng | Đường kính | $\tfrac23 MR^{2}$ |
| Thanh dài $L$ | Qua tâm, vuông góc thanh | $\tfrac{1}{12}ML^{2}$ |
| Thanh dài $L$ | Qua một đầu | $\tfrac13 ML^{2}$ |

Hai dòng cuối minh hoạ định lí trục song song: $\tfrac{1}{12}ML^{2} + M(L/2)^{2} = \tfrac13 ML^{2}$.

## Định lí trục song song

$$I = I_C + Md^{2}$$

Ý nghĩa sâu: **trục qua khối tâm luôn cho mômen quán tính nhỏ nhất** trong các trục song song, vì $Md^{2} \ge 0$. Vật rắn tự do luôn ưu tiên quay quanh khối tâm.

## Tính cộng được

$I$ của vật ghép bằng tổng $I$ của các phần đối với **cùng một trục**. Với vật khoét lỗ, dùng mẹo khối lượng âm: $I = I_{\text{đặc}} - I_{\text{lỗ}}$, nhớ áp dụng định lí trục song song cho phần lỗ nếu nó lệch tâm.

Lưu ý: không có "mômen quán tính của một vật" nói chung; luôn phải nói rõ **đối với trục nào**.

**Lỗi thường gặp:**
- Nói "mômen quán tính của quả cầu là $\tfrac25 MR^{2}$" mà không nêu trục. Cùng một vật có vô số giá trị $I$ ứng với các trục khác nhau; bỏ qua trục là bỏ qua một nửa thông tin.
- Áp dụng định lí trục song song giữa hai trục mà không trục nào qua khối tâm. Công thức $I = I_C + Md^{2}$ đòi hỏi $I_C$ phải là mômen quán tính đối với trục qua khối tâm; muốn nối hai trục lệch bất kì phải đi vòng qua trục khối tâm.
- Cho rằng vật nặng hơn luôn khó quay hơn. Một vành mỏng 1 kg bán kính 1 m có $I = 1\ \mathrm{kg\,m^{2}}$, lớn hơn quả cầu đặc 2 kg bán kính 0,3 m với $I = 0{,}072\ \mathrm{kg\,m^{2}}$; phân bố khối lượng quyết định chứ không phải khối lượng.

<sub>`lesson.physics.chuyen-dong-quay-intl.momen-quan-tinh-va-truc-song-song`</sub>

---

### 4. Định luật II Newton cho chuyển động quay và bài toán lăn không trượt
*Newton's second law for rotation and rolling without slipping* · THPT (lớp 10-12) · ap, a-level, olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Vận dụng được phương trình động lực học vật rắn quay quanh trục cố định
- Viết được điều kiện lăn không trượt và động năng toàn phần của vật lăn
- So sánh được gia tốc của các vật có hình dạng khác nhau khi lăn trên mặt phẳng nghiêng

## Một phương trình quen thuộc trong bộ áo mới

$$\sum\tau = I\alpha$$

Mọi kỹ thuật của động lực học thẳng chuyển sang nguyên vẹn: vẽ giản đồ vật tự do, chọn chiều quay dương, viết phương trình. Với hệ vừa quay vừa tịnh tiến (ròng rọc có khối lượng, vật lăn), phải viết **cả hai** phương trình:

$$\sum F = Ma_C \qquad\text{và}\qquad \sum\tau = I_C\alpha$$

rồi nối chúng bằng điều kiện ràng buộc.

## Lăn không trượt: điều kiện then chốt

Điểm tiếp xúc **đứng yên tức thời** so với mặt. Từ đó

$$v_C = \omega R, \qquad a_C = \alpha R$$

Đây là mối nối bắt buộc giữa hai phương trình. Chú ý: ma sát ở điểm tiếp xúc là **ma sát nghỉ**, nên nó không tiêu tán năng lượng — cơ năng vẫn bảo toàn khi vật lăn không trượt.

Động năng gồm hai phần theo định lí Koenig:

$$E_k = \tfrac12 Mv_C^{2} + \tfrac12 I_C\omega^{2} = \tfrac12(1+\beta)Mv_C^{2}$$

## Cuộc đua trên mặt phẳng nghiêng

Dùng bảo toàn cơ năng cho vật lăn từ độ cao $h$:

$$Mgh = \tfrac12(1+\beta)Mv_C^{2} \Rightarrow v_C = \sqrt{\frac{2gh}{1+\beta}}, \qquad a_C = \frac{g\sin\theta}{1+\beta}$$

Kết quả **không phụ thuộc khối lượng và bán kính**, chỉ phụ thuộc hình dạng qua $\beta$:

- Quả cầu đặc: $\beta = 2/5$, nhanh nhất.
- Trụ đặc: $\beta = 1/2$.
- Trụ rỗng thành mỏng: $\beta = 1$, chậm nhất.

Lí do: vật có khối lượng dồn ra xa trục phải dành nhiều thế năng hơn cho động năng quay, còn lại ít cho động năng tịnh tiến. Đây là thí nghiệm biểu diễn kinh điển và cũng là câu hỏi tủ của AP Physics 1.

## Điều kiện để không trượt

Ma sát nghỉ phải đủ lớn: $\tan\theta \le \mu_s(1 + 1/\beta)$. Dốc quá đứng thì vật vừa lăn vừa trượt, và khi ấy cơ năng không còn bảo toàn.

**Lỗi thường gặp:**
- Quên động năng quay khi dùng bảo toàn cơ năng cho vật lăn. Kết quả sẽ ra $v = \sqrt{2gh}$ cho mọi vật, mâu thuẫn với thí nghiệm cho thấy quả cầu luôn thắng vành.
- Cho rằng ma sát trong lăn không trượt làm mất cơ năng. Điểm tiếp xúc có vận tốc bằng 0 nên ma sát nghỉ không sinh công; chỉ khi vật trượt thì cơ năng mới hao hụt.
- Nghĩ vật nặng hơn hoặc lớn hơn sẽ lăn nhanh hơn. Từ $v_C = \sqrt{2gh/(1+\beta)}$ thấy $M$ và $R$ triệt tiêu; chỉ hình dạng, thể hiện qua $\beta$, mới quyết định kết quả cuộc đua.

<sub>`lesson.physics.chuyen-dong-quay-intl.dinh-luat-ii-quay-va-lan-khong-truot`</sub>

---

### 5. Mômen động lượng và định luật bảo toàn mômen động lượng
*Angular momentum and its conservation* · THPT (lớp 10-12) · ap, a-level, olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Tính được mômen động lượng của chất điểm và của vật rắn quay quanh trục cố định
- Vận dụng được định luật bảo toàn mômen động lượng cho hệ có mômen quán tính thay đổi
- Giải thích được các hiện tượng thực tế bằng bảo toàn mômen động lượng

## Đại lượng bảo toàn thứ ba

Cơ học có ba định luật bảo toàn lớn: năng lượng, động lượng, và mômen động lượng. Cái thứ ba chi phối mọi thứ quay, từ electron tới thiên hà.

$$\vec{L} = \vec{r}\times\vec{p}, \qquad L = I\omega, \qquad \sum\vec{\tau} = \frac{d\vec{L}}{dt}$$

Nếu $\sum\tau = 0$ thì $L$ không đổi. Chú ý điều kiện là **mômen ngoại lực** bằng 0, chứ không phải lực bằng 0: trọng lực tác dụng lên vận động viên trượt băng nhưng có giá đi qua trục quay nên không tạo mômen.

## Hệ quả ngoạn mục: đổi $I$ để đổi $\omega$

$$I_1\omega_1 = I_2\omega_2$$

- **Vận động viên trượt băng** co tay: $I$ giảm vài lần, $\omega$ tăng đúng chừng ấy lần. Động năng quay $E = L^{2}/(2I)$ **tăng lên** — năng lượng đó do cơ bắp thực hiện công kéo tay vào chống lực quán tính li tâm.
- **Sao neutron**: một ngôi sao bán kính $10^{6}$ km co lại còn 10 km, $I$ giảm cỡ $10^{10}$ lần, nên chu kì từ vài chục ngày rút xuống vài mili giây. Đó là pulsar.
- **Mèo rơi tự do** vẫn tiếp đất bằng bốn chân dù $L = 0$ suốt quá trình, bằng cách xoay phần thân trước và thân sau ngược nhau.

## Vì sao bánh xe đạp không đổ

Bánh xe quay có $\vec{L}$ lớn dọc trục. Muốn làm đổ xe phải đổi hướng $\vec{L}$, mà điều đó đòi hỏi mômen lực đáng kể. Với mômen nhỏ, phản ứng là **tuế sai**: trục quay từ từ vẽ nón thay vì đổ xuống. Đây là nguyên lí của con quay hồi chuyển trong thiết bị dẫn đường.

## Bảng đối chiếu ba đại lượng bảo toàn

| Đại lượng | Bảo toàn khi | Va chạm mềm |
|---|---|---|
| Động lượng $\vec{p}$ | $\sum\vec{F}_{\text{ngoại}} = 0$ | Bảo toàn |
| Mômen động lượng $\vec{L}$ | $\sum\vec{\tau}_{\text{ngoại}} = 0$ | Bảo toàn |
| Cơ năng | Chỉ có lực thế | Không bảo toàn |

**Lỗi thường gặp:**
- Áp dụng bảo toàn động năng quay cùng lúc với bảo toàn mômen động lượng. Khi $I$ thay đổi do nội lực, $E = L^{2}/(2I)$ thay đổi theo; chỉ một trong hai đại lượng bảo toàn, không phải cả hai.
- Cho rằng cần lực bằng 0 để mômen động lượng bảo toàn. Điều kiện đúng là **mômen** ngoại lực bằng 0; lực có giá đi qua trục quay cho mômen bằng 0 dù lực rất lớn.
- Quên rằng mômen động lượng luôn được tính đối với một trục hay một điểm cụ thể. Cùng một chuyển động cho $L$ khác nhau với các trục khác nhau, và có thể bảo toàn với trục này mà không bảo toàn với trục kia.

<sub>`lesson.physics.chuyen-dong-quay-intl.momen-dong-luong-va-bao-toan`</sub>

---

## Unit 6: Sóng và âm - Waves and Sound

### 1. Mô tả sóng và phương trình sóng
*Describing waves and the wave equation* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Phân tích được sự khác nhau giữa sóng ngang và sóng dọc, nêu được ví dụ của mỗi loại
- Vận dụng được hệ thức $v = \lambda f$ và giải thích đại lượng nào không đổi khi sóng đổi môi trường
- Viết và giải thích được phương trình sóng $u = A\cos(\omega t - kx)$

## Sóng chuyển cái gì đi

Thả một chiếc lá lên mặt nước có sóng: lá nhấp nhô tại chỗ chứ không trôi theo sóng. Đây là điểm mấu chốt: sóng truyền **pha dao động và năng lượng**, không truyền vật chất. Mỗi phần tử môi trường chỉ dao động quanh vị trí cân bằng của nó rồi kéo phần tử kế bên dao động theo, chậm hơn một chút.

Phân loại theo phương dao động:

- **Sóng ngang:** phần tử dao động vuông góc phương truyền (sóng dây, sóng điện từ). Sóng ngang cơ học chỉ truyền được trên bề mặt chất lỏng và trong chất rắn, vì cần lực đàn hồi trượt.
- **Sóng dọc:** phần tử dao động dọc phương truyền, tạo vùng nén và vùng dãn (sóng âm trong không khí, sóng P của động đất). Sóng dọc truyền được trong cả ba trạng thái vật chất.

Chính sự khác biệt này giúp các nhà địa chấn kết luận lõi ngoài Trái Đất ở thể lỏng: sóng ngang S không xuyên qua được vùng đó.

## Hệ thức nền tảng

$$v = \lambda f$$

Câu hỏi quan trọng hơn công thức: **đại lượng nào do nguồn quyết định, đại lượng nào do môi trường quyết định?**

- **Tần số $f$** do nguồn phát quyết định và **không đổi** khi sóng sang môi trường khác. Số dao động đi vào mỗi giây phải bằng số đi ra, nếu không phần tử biên sẽ tích luỹ vô hạn.
- **Tốc độ $v$** do môi trường quyết định (với dây căng, $v = \sqrt{F/\mu}$).
- **Bước sóng $\lambda = v/f$** vì thế thay đổi theo môi trường.

Đây là chìa khoá giải thích khúc xạ: ánh sáng vào nước chậm lại, tần số giữ nguyên nên bước sóng ngắn lại, và mặt sóng bị bẻ hướng.

## Phương trình sóng

Sóng truyền theo chiều dương Ox:

$$u(x,t) = A\cos\left(\omega t - \frac{2\pi x}{\lambda}\right) = A\cos(\omega t - kx)$$

Đọc từng phần: $\omega t$ là pha dao động của nguồn; $kx$ là **độ trễ pha** do sóng cần thời gian mới tới được điểm $x$. Dấu trừ nghĩa là điểm xa nguồn dao động **chậm pha** hơn. Nếu sóng truyền theo chiều âm, dấu đổi thành cộng.

Độ lệch pha giữa hai điểm cách nhau $d$:

$$\Delta\varphi = \frac{2\pi d}{\lambda}$$

Hai điểm cùng pha khi $d = k\lambda$, ngược pha khi $d = (k+0{,}5)\lambda$. Toàn bộ phần giao thoa sẽ xây trên đúng hai điều kiện này.

**Lỗi thường gặp:**
- Cho rằng tần số thay đổi khi sóng sang môi trường khác — sai vì tần số do nguồn áp đặt; nếu tần số ở hai bên mặt phân cách khác nhau thì phần tử tại biên sẽ phải dao động với hai nhịp cùng lúc, điều không thể xảy ra.
- Nghĩ phần tử môi trường di chuyển theo sóng — sai vì mỗi phần tử chỉ dao động quanh vị trí cân bằng; cái lan truyền là trạng thái dao động và năng lượng, không phải vật chất.
- Đổi dấu sai giữa $\omega t - kx$ và $\omega t + kx$ — sai vì dấu trừ ứng với sóng truyền theo chiều dương và điểm xa trễ pha; đổi dấu tuỳ tiện làm đảo ngược chiều truyền của sóng.

<sub>`lesson.physics.song.mo-ta-song-va-phuong-trinh-song`</sub>

---

### 2. Chồng chất, giao thoa và thí nghiệm hai khe Young
*Superposition, interference and Young's double-slit experiment* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu được nguyên lí chồng chất và điều kiện để hai nguồn giao thoa được với nhau
- Vận dụng được điều kiện hiệu đường đi để xác định vị trí vân sáng và vân tối
- Giải thích được ý nghĩa lịch sử của thí nghiệm Young đối với bản chất sóng của ánh sáng

## Nguyên lí chồng chất

Khi hai sóng gặp nhau, li độ tại mỗi điểm bằng **tổng đại số** li độ do từng sóng gây ra. Sau khi đi qua nhau, mỗi sóng tiếp tục truyền như chưa hề có cuộc gặp — sóng không va chạm như hạt.

Hệ quả: tại nơi hai sóng cùng pha, biên độ cộng lại (giao thoa **tăng cường**); tại nơi ngược pha, biên độ trừ nhau (giao thoa **triệt tiêu**). Nếu hai biên độ bằng nhau, triệt tiêu là hoàn toàn.

## Điều kiện để thấy được vân

Hai nguồn phải **kết hợp**: cùng tần số và độ lệch pha không đổi. Đây là lí do không thể tạo vân giao thoa bằng hai bóng đèn: nguyên tử phát sáng độc lập, pha đổi ngẫu nhiên cỡ $10^{-8}$ s, hình ảnh vân xáo trộn quá nhanh để mắt kịp thấy. Young giải bài toán ấy bằng cách tách **một** chùm sáng thành hai qua hai khe — chúng cùng gốc nên tự động kết hợp.

## Điều kiện giao thoa

Với hai nguồn cùng pha:

$$\delta = d_2 - d_1 = k\lambda \ (\text{cực đại}), \qquad \delta = \left(k+\tfrac{1}{2}\right)\lambda \ (\text{cực tiểu})$$

Nếu hai nguồn **ngược pha**, hai điều kiện đổi chỗ cho nhau — đây là chỗ cần tỉnh táo, không được học vẹt.

## Thí nghiệm Young và khoảng vân

Hai khe cách nhau $a$, màn cách khe $D \gg a$. Với góc nhỏ, $\delta \approx ax/D$, nên:

$$x_{\text{sáng}} = k\frac{\lambda D}{a}, \qquad x_{\text{tối}} = \left(k+\tfrac{1}{2}\right)\frac{\lambda D}{a}, \qquad i = \frac{\lambda D}{a}$$

Hai điều đọc được từ công thức khoảng vân: muốn vân rộng dễ quan sát thì phải cho hai khe **thật gần nhau** và màn **thật xa**; và vì $i \propto \lambda$, ánh sáng đỏ cho vân rộng hơn ánh sáng tím.

Với ánh sáng trắng, vân trung tâm ($k=0$) là màu trắng vì mọi bước sóng đều có $\delta = 0$ tại đó, còn các vân bậc cao bị tán thành quang phổ với tím ở trong, đỏ ở ngoài.

## Vì sao thí nghiệm này quan trọng

Năm 1801, mô hình hạt của Newton đang thống trị. Giao thoa là hiện tượng mà mô hình hạt không giải thích nổi: hai chùm sáng chồng lên nhau lại cho **bóng tối**. Chỉ sóng mới triệt tiêu được nhau. Thí nghiệm Young vì thế là bằng chứng quyết định cho bản chất sóng của ánh sáng — và một thế kỉ sau, khi lặp lại với từng electron một, nó lại trở thành thí nghiệm nền tảng của cơ học lượng tử.

**Lỗi thường gặp:**
- Dùng điều kiện cực đại $\delta = k\lambda$ cho hai nguồn ngược pha — sai vì khi hai nguồn đã lệch pha $\pi$ sẵn, hiệu đường đi bằng bội nguyên bước sóng lại cho hai sóng tới nơi ngược pha, tạo cực tiểu.
- Cho rằng nhúng thí nghiệm vào nước làm đổi màu ánh sáng quan sát được — sai vì màu do tần số quyết định mà tần số không đổi; chỉ bước sóng và do đó khoảng vân bị co lại.
- Nghĩ hai bóng đèn giống hệt nhau sẽ tạo được vân giao thoa — sai vì các nguyên tử phát sáng độc lập, độ lệch pha giữa hai nguồn biến đổi ngẫu nhiên rất nhanh nên hệ vân không đứng yên đủ lâu để quan sát.

<sub>`lesson.physics.song.giao-thoa-va-hai-khe-young`</sub>

---

### 3. Nhiễu xạ qua một khe hẹp và cách tử nhiễu xạ
*Single-slit diffraction and the diffraction grating* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được sự hình thành cực tiểu nhiễu xạ một khe bằng phương pháp chia đôi mặt sóng
- Vận dụng được công thức cách tử $d\sin\theta = k\lambda$ và giải thích ưu thế của cách tử so với hai khe
- Vận dụng được tiêu chuẩn Rayleigh để đánh giá khả năng phân giải của dụng cụ quang

## Vì sao khe hẹp lại cho vân tối

Nghịch lí biểu kiến: mở rộng nguồn sáng ra cả một khe mà lại xuất hiện chỗ tối. Lời giải nằm ở nguyên lí Huygens - mỗi điểm trên khe là một nguồn thứ cấp, và các nguồn ấy giao thoa với nhau.

Mẹo chia đôi mặt sóng: chia khe rộng $b$ thành hai nửa. Mỗi tia ở nửa trên có một tia "bạn" ở nửa dưới cách nó $b/2$. Nếu hai tia bạn này lệch nhau nửa bước sóng, chúng triệt tiêu **từng cặp một**, và cả khe cho kết quả bằng 0:

$$\frac{b}{2}\sin\theta = \frac{\lambda}{2} \;\Longrightarrow\; b\sin\theta = \lambda$$

Tổng quát, cực tiểu tại $b\sin\theta = k\lambda$ với $k = \pm1, \pm2,\dots$ (chú ý $k \ne 0$).

Bề rộng cực đại trung tâm: $L = 2\lambda D/b$ — **gấp đôi** các cực đại phụ, và tỉ lệ nghịch với bề rộng khe. Thu hẹp khe làm ảnh loe rộng ra chứ không sắc nét hơn: đây là giới hạn cơ bản của mọi dụng cụ quang.

## Cách tử: nhiều khe thì tốt hơn hai khe

$$d\sin\theta = k\lambda$$

Công thức giống hai khe, nhưng hình ảnh khác hẳn về chất. Với $N$ khe, một cực đại chỉ xuất hiện khi **tất cả** $N$ sóng cùng pha; chỉ cần lệch góc rất nhỏ là chúng bắt đầu triệt tiêu lẫn nhau. Kết quả: cực đại **hẹp hơn và sáng hơn** nhiều lần, độ sắc tăng theo $N$.

Đó là lí do cách tử là dụng cụ tiêu chuẩn để đo bước sóng và phân tích quang phổ, thay vì hai khe. Số bậc quan sát được bị chặn bởi $\sin\theta \le 1$, tức $k_{\max} = \lfloor d/\lambda \rfloor$.

## Giới hạn phân giải

Mọi thấu kính và gương đều có khẩu độ hữu hạn, nên ảnh của một điểm sáng không bao giờ là một điểm mà là đĩa nhiễu xạ Airy. Hai ngôi sao quá gần nhau sẽ cho hai đĩa chồng lấn không tách được. Tiêu chuẩn Rayleigh:

$$\theta_{\min} \approx 1{,}22\frac{\lambda}{D}$$

Muốn nhìn rõ chi tiết nhỏ hơn, chỉ có hai cách: tăng đường kính $D$ (vì sao kính thiên văn ngày càng to) hoặc giảm bước sóng (vì sao kính hiển vi điện tử dùng chùm electron có $\lambda$ cỡ picômét thay vì ánh sáng nhìn thấy).

**Lỗi thường gặp:**
- Dùng $k = 0$ trong công thức cực tiểu nhiễu xạ một khe — sai vì tại $\theta = 0$ mọi tia đều đồng pha, đó là cực đại trung tâm sáng nhất chứ không phải cực tiểu.
- Cho rằng thu hẹp khe làm ảnh sắc nét hơn — sai vì bề rộng cực đại trung tâm tỉ lệ nghịch với bề rộng khe; khe càng hẹp thì ánh sáng càng loe rộng, ảnh càng nhoè.
- Lấy chu kì cách tử bằng số vạch trên milimét — sai vì $d$ là khoảng cách giữa hai vạch, tức nghịch đảo mật độ vạch; nhầm lẫn này làm sai kết quả tới hàng triệu lần.

<sub>`lesson.physics.song.nhieu-xa-mot-khe-va-cach-tu`</sub>

---

### 4. Giao thoa màng mỏng và hiện tượng đảo pha khi phản xạ
*Thin-film interference and phase inversion on reflection* · THPT (lớp 10-12) · ap · 50 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được điều kiện xảy ra đảo pha $\pi$ khi sóng phản xạ trên mặt phân cách
- Vận dụng được điều kiện giao thoa màng mỏng cho các trường hợp có một lần hoặc hai lần đảo pha
- Tính được bề dày lớp phủ chống phản xạ cho một bước sóng cho trước

## Vì sao váng dầu có màu

Một lớp dầu mỏng trên mặt nước, một bong bóng xà phòng, lớp phủ trên mắt kính — tất cả đều lấp lánh nhiều màu dù bản thân chất đó trong suốt không màu. Nguyên nhân: ánh sáng phản xạ ở mặt trên và mặt dưới của màng giao thoa với nhau. Mỗi bước sóng có điều kiện tăng cường riêng, nên mỗi bề dày cho một màu khác nhau.

## Hai yếu tố quyết định

**Yếu tố 1 - hiệu quang lộ hình học.** Tia phản xạ ở mặt dưới đi thêm quãng đường $2t$ trong màng chiết suất $n$, tương đương quang lộ $2nt$ (chiếu vuông góc).

**Yếu tố 2 - đảo pha khi phản xạ.** Đây là phần quyết định và hay bị bỏ sót. Quy tắc:

- Phản xạ trên môi trường **chiết quang hơn** (đi từ $n$ nhỏ sang $n$ lớn): đảo pha $\pi$, tương đương thêm $\lambda/2$ vào quang lộ.
- Phản xạ trên môi trường **kém chiết quang hơn**: không đảo pha.

Đây chính là hiện tượng tương tự sóng trên dây phản xạ ở đầu cố định (đảo chiều) so với đầu tự do (không đảo).

## Hai trường hợp và hai bộ điều kiện

**Trường hợp A - có đúng MỘT lần đảo pha** (ví dụ màng xà phòng trong không khí: $n_{kk} < n_{xp} > n_{kk}$; chỉ mặt trên đảo pha):

$$2nt = \left(k+\tfrac{1}{2}\right)\lambda \ (\text{sáng}), \qquad 2nt = k\lambda \ (\text{tối})$$

**Trường hợp B - có HAI lần hoặc KHÔNG lần đảo pha** (ví dụ lớp phủ $n$ trung gian giữa không khí và thuỷ tinh):

$$2nt = k\lambda \ (\text{sáng}), \qquad 2nt = \left(k+\tfrac{1}{2}\right)\lambda \ (\text{tối})$$

Hai bộ điều kiện **đổi chỗ cho nhau**. Không thể học thuộc một bộ rồi dùng chung; phải kiểm tra số lần đảo pha trước mỗi bài.

Một kiểm tra định tính hữu ích: màng cực mỏng ($t \to 0$) trong trường hợp A cho vệt **tối**, đúng như quan sát ở mép trên của màng xà phòng đang chảy mỏng dần ngay trước khi vỡ. Nếu công thức của bạn cho vệt sáng ở đó thì đã chọn nhầm trường hợp.

## Lớp phủ chống phản xạ

Chọn $n_{\text{phủ}}$ nằm giữa $n_{kk}$ và $n_{\text{thuỷ tinh}}$ (cả hai mặt đều đảo pha, thuộc trường hợp B) rồi làm cho tia phản xạ **triệt tiêu**:

$$t_{\min} = \frac{\lambda}{4n}$$

Ánh sáng không phản xạ được thì buộc phải truyền qua, nên ống kính máy ảnh phủ lớp này cho ảnh sáng hơn và ít loá hơn. Vì chỉ tối ưu cho một bước sóng (thường chọn màu lục ở giữa dải nhìn thấy), phần đỏ và tím phản xạ còn sót lại làm ống kính có ánh tím đặc trưng.

**Lỗi thường gặp:**
- Bỏ qua sự đảo pha khi phản xạ — sai vì mỗi lần đảo pha tương đương thêm nửa bước sóng vào quang lộ, đủ để biến điều kiện sáng thành tối và ngược lại.
- Dùng quãng đường hình học $2t$ thay cho quang lộ $2nt$ — sai vì bước sóng trong màng ngắn hơn $n$ lần, nên cùng một bề dày chứa nhiều bước sóng hơn so với trong chân không.
- Áp dụng chung một bộ công thức cho mọi màng mỏng — sai vì điều kiện sáng và tối hoán đổi tuỳ theo số lần đảo pha là lẻ hay chẵn; phải xét chiết suất ba môi trường trước khi viết công thức.

<sub>`lesson.physics.song.giao-thoa-mang-mong`</sub>

---

### 5. Sóng dừng trên dây và trong ống khí
*Standing waves on strings and in air columns* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được sự hình thành sóng dừng từ sự chồng chất của sóng tới và sóng phản xạ
- Xác định được điều kiện chiều dài và tần số hoạ âm cho dây hai đầu cố định, ống hở hai đầu và ống một đầu kín
- Vận dụng được sóng dừng để đo tốc độ truyền sóng trong thực nghiệm

## Sóng dừng hình thành thế nào

Sóng chạy tới đầu dây rồi phản xạ ngược lại, chồng lên sóng tới. Ở một số điểm hai sóng **luôn** ngược pha nên đứng yên vĩnh viễn (nút); ở một số điểm khác chúng **luôn** cùng pha nên dao động cực mạnh (bụng). Vị trí nút và bụng không di chuyển — vì thế gọi là sóng "dừng", dù nó vẫn là kết quả của hai sóng chạy.

Hai đặc điểm hình học cần thuộc:

- Khoảng cách hai nút liên tiếp (hoặc hai bụng liên tiếp) $= \lambda/2$.
- Khoảng cách nút tới bụng gần nhất $= \lambda/4$.

Đây là công cụ đo bước sóng chính xác nhất trong phòng thí nghiệm phổ thông: đo khoảng cách giữa nhiều nút rồi chia, thay vì đo một bước sóng dễ sai số.

## Ba cấu hình chuẩn

**Dây hai đầu cố định** (đàn ghi ta, violin). Hai đầu bắt buộc là nút:

$$\ell = k\frac{\lambda}{2} \;\Rightarrow\; f_k = k\frac{v}{2\ell}, \quad k = 1,2,3,\dots$$

Đủ mọi hoạ âm. Kết hợp với $v = \sqrt{F/\mu}$, ta hiểu ba cách chỉnh cao độ đàn: bấm phím (đổi $\ell$), lên dây (đổi $F$), và chọn dây to nhỏ (đổi $\mu$).

**Ống hở hai đầu** (sáo). Hai đầu là bụng, điều kiện hình học giống hệt dây:

$$f_k = k\frac{v}{2\ell}$$

**Ống một đầu kín** (ống nghiệm, kèn clarinet). Đầu kín là nút, đầu hở là bụng, nên chiều dài chứa số lẻ lần $\lambda/4$:

$$\ell = (2k-1)\frac{\lambda}{4} \;\Rightarrow\; f = (2k-1)\frac{v}{4\ell}$$

Hai kết luận: tần số cơ bản chỉ bằng **một nửa** so với ống hở cùng chiều dài, và chỉ tồn tại hoạ âm **lẻ**. Chính sự thiếu vắng hoạ âm chẵn tạo ra âm sắc trầm, rỗng đặc trưng của clarinet so với sáo.

## Vì sao dùng để đo tốc độ

Cho âm thoa tần số $f$ đã biết dao động trên miệng ống nước điều chỉnh được. Hạ mực nước cho tới khi nghe cộng hưởng lần đầu ($\ell_1$) và lần hai ($\ell_2$). Vì hai vị trí cách nhau đúng $\lambda/2$:

$$v = 2f(\ell_2 - \ell_1)$$

Cách này khéo ở chỗ nó **loại trừ được sai số đầu ống** — bụng sóng thực ra nằm nhô ra ngoài miệng ống một đoạn nhỏ, nhưng hiệu số hai chiều dài triệt tiêu hoàn toàn phần dôi ấy.

**Lỗi thường gặp:**
- Cho rằng khoảng cách hai nút liên tiếp bằng một bước sóng — sai vì trong một bước sóng có hai nút; khoảng cách đúng là $\lambda/2$, và nhầm lẫn này làm tốc độ tính ra sai gấp đôi.
- Áp dụng công thức ống hở cho ống một đầu kín — sai vì điều kiện biên khác nhau: đầu kín bắt buộc là nút nên chiều dài phải chứa số lẻ lần một phần tư bước sóng, dẫn tới chỉ có hoạ âm lẻ.
- Nghĩ mọi điểm trên sóng dừng đều dao động cùng biên độ — sai vì biên độ biến thiên theo vị trí từ 0 ở nút tới cực đại ở bụng; chỉ có pha là giống nhau trong từng bó sóng.

<sub>`lesson.physics.song.song-dung-tren-day-va-trong-ong`</sub>

---

### 6. Hiện tượng phách và hiệu ứng Doppler
*Beats and the Doppler effect* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được sự hình thành phách và tính được tần số phách của hai nguồn âm gần nhau
- Vận dụng được công thức Doppler cho trường hợp nguồn chuyển động và máy thu chuyển động
- Phân tích được vì sao hai trường hợp đó không đối xứng nhau về mặt vật lí

## Phách: giao thoa theo thời gian

Giao thoa hai khe cho các cực đại phân bố theo **không gian**. Khi hai âm có tần số hơi khác nhau chồng lên nhau tại **một điểm**, hiện tượng tương tự xảy ra theo **thời gian**: có lúc hai sóng cùng pha (âm to), có lúc ngược pha (âm nhỏ), lặp lại đều đặn.

$$f_{\text{phách}} = |f_1 - f_2|$$

Tai người nghe được phách khi hiệu tần số nhỏ hơn khoảng 10 Hz; lớn hơn thì ta nghe thành hai âm riêng biệt. Đây là công cụ lên dây đàn chính xác nhất mà không cần máy: chỉnh cho tới khi phách biến mất, tức hai tần số trùng khít. Phương pháp "đo về không" này chính xác hơn nhiều so với cố nghe xem hai nốt có giống nhau không.

## Doppler: hai cơ chế khác nhau

**Nguồn chuyển động, máy thu đứng yên.** Nguồn chạy theo sóng nó vừa phát, làm các mặt sóng bị **dồn lại** phía trước và **giãn ra** phía sau. Bước sóng thực sự thay đổi trong không gian:

$$f' = f\frac{v}{v \mp v_s}$$

(dấu trừ khi nguồn lại gần).

**Máy thu chuyển động, nguồn đứng yên.** Bước sóng trong không khí **không đổi**; chỉ là máy thu chạy đón đầu nên gặp nhiều mặt sóng hơn trong mỗi giây:

$$f' = f\frac{v \pm v_o}{v}$$

(dấu cộng khi máy thu lại gần).

Hai công thức cho kết quả **hơi khác nhau** ở cùng tốc độ tương đối — bằng chứng rằng môi trường truyền âm là một hệ quy chiếu ưu tiên. Với sóng âm, việc "ai đang chuyển động" thực sự có ý nghĩa vật lí. Điều này khác hẳn ánh sáng, nơi chỉ vận tốc tương đối mới có nghĩa, và đó chính là manh mối dẫn tới thuyết tương đối hẹp.

Công thức tổng quát:

$$f' = f\frac{v \pm v_o}{v \mp v_s}$$

Mẹo nhớ dấu không cần học thuộc: **lại gần thì tần số phải tăng, ra xa thì giảm**. Sau khi tính, kiểm tra kết quả có đúng chiều đó không; nếu ngược thì chọn nhầm dấu.

## Ứng dụng

Súng bắn tốc độ và radar thời tiết dùng Doppler với sóng phản xạ (hiệu ứng xảy ra hai lần nên độ nhạy gấp đôi). Siêu âm Doppler đo tốc độ dòng máu. Trong thiên văn, dịch chuyển đỏ của vạch quang phổ cho biết thiên hà đang lùi xa — dữ liệu nền tảng của định luật Hubble.

**Lỗi thường gặp:**
- Dùng chung một công thức Doppler cho cả nguồn và máy thu chuyển động — sai vì hai cơ chế khác nhau: nguồn chuyển động làm thay đổi bước sóng trong không gian, còn máy thu chuyển động chỉ thay đổi số mặt sóng gặp mỗi giây.
- Chọn dấu bằng cách học thuộc mà không kiểm tra — sai vì rất dễ nhớ nhầm; cách an toàn là tính xong rồi đối chiếu với nguyên tắc lại gần thì tần số tăng, ra xa thì giảm.
- Cho rằng phách là hiện tượng chỉ xảy ra với âm thanh — sai vì phách là hệ quả của chồng chất hai dao động lệch tần số, xuất hiện với mọi loại sóng, kể cả sóng vô tuyến trong mạch trộn tần.

<sub>`lesson.physics.song.phach-va-hieu-ung-doppler`</sub>

---

### 7. Cường độ âm, mức cường độ âm và thang decibel
*Sound intensity, sound level and the decibel scale* · THPT (lớp 10-12) · ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được định luật nghịch đảo bình phương cho cường độ âm của nguồn điểm
- Tính được mức cường độ âm theo thang decibel và giải thích vì sao thang này là thang logarit
- Phân tích được mối liên hệ giữa độ tăng decibel và tỉ số cường độ âm

## Vì sao cường độ giảm theo $1/r^2$

Nguồn điểm phát công suất $P$ toả đều ra mọi hướng. Ở khoảng cách $r$, năng lượng đó trải trên mặt cầu diện tích $4\pi r^2$:

$$I = \frac{P}{4\pi r^2}$$

Đây thuần tuý là hệ quả hình học của bảo toàn năng lượng, không liên quan gì tới bản chất âm — nên cùng quy luật ấy áp dụng cho ánh sáng, bức xạ, và mọi thứ phát ra từ nguồn điểm. Đi xa gấp đôi, cường độ chỉ còn một phần tư.

Cường độ cũng tỉ lệ với **bình phương biên độ**: $I \propto A^2$. Vì thế muốn cường độ tăng 4 lần, biên độ dao động phải tăng 2 lần.

## Vì sao phải dùng thang logarit

Tai người nghe được từ ngưỡng $10^{-12}$ W/m² tới ngưỡng đau $1$ W/m² — dải rộng **mười hai bậc độ lớn**. Vẽ trên trục tuyến tính là bất khả thi. Hơn nữa, cảm giác to nhỏ của tai gần đúng tỉ lệ với **logarit** của cường độ chứ không phải với chính cường độ (định luật Weber-Fechner). Cả hai lí do đều dẫn tới thang decibel:

$$L = 10\lg\frac{I}{I_0}, \qquad I_0 = 10^{-12}\ \text{W/m}^2$$

## Đọc thang decibel cho đúng

Vì là thang logarit, decibel **cộng** ứng với cường độ **nhân**:

| Thay đổi mức | Tỉ số cường độ |
|---|---|
| $+3$ dB | gấp 2 |
| $+10$ dB | gấp 10 |
| $+20$ dB | gấp 100 |
| $+60$ dB | gấp $10^6$ |

Hai hệ quả hay bị hiểu sai:

- **80 dB không phải to gấp đôi 40 dB.** Nó mạnh hơn $10^4$ lần về cường độ.
- **Hai nguồn giống nhau cùng phát không cho gấp đôi decibel**, mà chỉ thêm 3 dB, vì cường độ mới gấp đôi cường độ cũ.

Hiệu mức giữa hai điểm không cần biết $I_0$:

$$L_2 - L_1 = 10\lg\frac{I_2}{I_1} = 20\lg\frac{r_1}{r_2}$$

Dạng thứ hai rất tiện: đi ra xa gấp đôi làm mức âm giảm đúng $20\lg 2 = 6$ dB, bất kể công suất nguồn là bao nhiêu.

## Vài mốc thực tế

0 dB ngưỡng nghe, 30 dB thư viện yên tĩnh, 60 dB trò chuyện, 90 dB máy cắt cỏ, 120 dB ngưỡng đau. Tiếp xúc kéo dài trên 85 dB gây tổn thương thính giác không hồi phục — con số này là cơ sở của mọi quy định an toàn lao động về tiếng ồn.

**Lỗi thường gặp:**
- Cộng hoặc nhân trực tiếp các giá trị decibel của nhiều nguồn — sai vì decibel là thang logarit; phải quy về cường độ, cộng cường độ rồi mới chuyển ngược lại thành decibel.
- Cho rằng 100 dB to gấp đôi 50 dB — sai vì chênh 50 dB tương ứng tỉ số cường độ $10^5$ lần; quan hệ giữa số decibel và cường độ là hàm mũ chứ không phải tỉ lệ thuận.
- Dùng $I \propto 1/r$ cho nguồn điểm — sai vì năng lượng trải trên mặt cầu có diện tích tỉ lệ $r^2$, nên cường độ giảm theo bình phương khoảng cách.

<sub>`lesson.physics.song.cuong-do-am-va-thang-decibel`</sub>

---

### 8. Phân cực ánh sáng và định luật Malus
*Polarisation of light and Malus's law* · THPT (lớp 10-12) · ap, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao chỉ sóng ngang mới phân cực được và ý nghĩa của điều đó với bản chất ánh sáng
- Vận dụng được định luật Malus để tính cường độ ánh sáng qua hệ nhiều kính phân cực
- Giải thích được sự phân cực do phản xạ và ý nghĩa của góc Brewster

## Một thí nghiệm quyết định về bản chất ánh sáng

Sóng dọc như sóng âm không thể phân cực: phương dao động đã trùng phương truyền, không còn tự do nào để chọn. Chỉ sóng **ngang** mới có vô số phương dao động vuông góc với phương truyền để lọc lựa.

Vì thế, việc ánh sáng phân cực được là bằng chứng trực tiếp rằng ánh sáng là **sóng ngang** — thông tin mà giao thoa và nhiễu xạ không cung cấp được (chúng chỉ chứng minh ánh sáng là sóng, không nói loại nào).

Ánh sáng từ đèn hay Mặt Trời là **ánh sáng tự nhiên**: vectơ $\vec{E}$ dao động theo mọi phương ngang với xác suất như nhau, vì mỗi nguyên tử phát độc lập.

## Kính phân cực và định luật Malus

**Kính thứ nhất** biến ánh sáng tự nhiên thành phân cực thẳng, cường độ còn **một nửa**:

$$I_1 = \frac{I_0}{2}$$

Hệ số $1/2$ đến từ việc lấy trung bình $\cos^2\theta$ trên mọi góc, không phải từ định luật Malus.

**Kính thứ hai** (kính phân tích) đặt lệch góc $\theta$: chỉ thành phần $E\cos\theta$ đi qua, và vì $I \propto E^2$:

$$I_2 = I_1\cos^2\theta$$

Khi hai kính vuông góc ($\theta = 90^\circ$), ánh sáng bị chặn hoàn toàn.

**Kết quả phản trực giác đáng nhớ:** hai kính vuông góc cho tối hoàn toàn, nhưng **chèn thêm** một kính thứ ba ở giữa lệch $45^\circ$ lại cho ánh sáng đi qua ($I = I_1\cos^2 45^\circ\cos^2 45^\circ = I_1/4$). Thêm vật cản mà lại sáng lên — lời giải thích là mỗi kính không chỉ lọc mà còn **định hướng lại** phương phân cực của ánh sáng đi qua nó.

## Phân cực do phản xạ

Ánh sáng phản xạ trên mặt nước, kính, đường nhựa bị phân cực một phần, với phương dao động ưu tiên **song song mặt phản xạ** (tức nằm ngang khi phản xạ trên mặt ngang). Ở góc Brewster $\tan\theta_B = n_2/n_1$, tia phản xạ phân cực **hoàn toàn**.

Đây là cơ sở của kính râm phân cực: trục của kính đặt **thẳng đứng** để chặn thành phần nằm ngang, loại bỏ phần lớn ánh loá từ mặt đường và mặt nước trong khi ánh sáng cảnh vật thông thường vẫn qua được. Nhiếp ảnh gia dùng kính lọc phân cực xoay được để làm bầu trời xanh đậm hơn và khử phản chiếu trên kính, nước.

Màn hình LCD cũng phát ánh sáng đã phân cực — nghiêng đầu đeo kính râm phân cực mà nhìn màn hình, ta sẽ thấy nó tối đi hoặc tắt hẳn.

**Lỗi thường gặp:**
- Áp dụng $I = I_0\cos^2\theta$ cho kính phân cực đầu tiên gặp ánh sáng tự nhiên — sai vì ánh sáng tự nhiên không có phương phân cực xác định để đo góc; kết quả đúng là một nửa cường độ, đến từ trung bình của $\cos^2$ trên mọi hướng.
- Đo góc của mỗi kính so với kính đầu tiên thay vì so với phương phân cực của ánh sáng tới nó — sai vì mỗi kính đều xoay lại phương phân cực, nên chuỗi góc phải tính liên tiếp từng cặp.
- Cho rằng kính râm phân cực nào cũng như nhau nếu xoay 90 độ — sai vì ánh loá phản xạ trên mặt ngang phân cực theo phương ngang, nên chỉ kính có trục thẳng đứng mới chặn được; xoay kính đi 90 độ sẽ để ánh loá lọt qua trọn vẹn.

<sub>`lesson.physics.song.phan-cuc-va-dinh-luat-malus`</sub>

---

## Unit 7: Quang hình - Geometric Optics

### 1. Phản xạ, khúc xạ, phản xạ toàn phần và sợi quang
*Reflection, refraction, total internal reflection and optical fibres* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được định luật khúc xạ Snell dưới cả dạng chiết suất và dạng tốc độ sóng
- Xác định được góc giới hạn và điều kiện xảy ra phản xạ toàn phần
- Giải thích được nguyên lí truyền tín hiệu trong sợi quang và ưu điểm của nó

## Vì sao ánh sáng bị bẻ cong

Ánh sáng đi từ không khí vào nước bị lệch vì tốc độ của nó giảm. Hình dung một mặt sóng đi xiên tới mặt nước: mép sóng chạm nước trước sẽ chậm lại trước, trong khi mép còn lại vẫn đi nhanh, khiến cả mặt sóng xoay hướng — hệt như hàng người diễu hành bước từ đường nhựa sang bãi cát xiên góc.

Điều đó cho ngay dạng tổng quát của định luật khúc xạ:

$$\frac{\sin i}{\sin r} = \frac{v_1}{v_2} = \frac{n_2}{n_1} \;\Longleftrightarrow\; n_1\sin i = n_2\sin r$$

Dạng theo tốc độ đúng cho **mọi loại sóng**, kể cả sóng âm và sóng nước; dạng theo chiết suất là trường hợp riêng cho ánh sáng.

Quy tắc định tính đáng nhớ: đi vào môi trường chiết quang hơn thì tia **gãy về gần pháp tuyến**, đi ra thì gãy xa pháp tuyến.

## Phản xạ toàn phần

Khi ánh sáng đi từ môi trường chiết quang hơn sang kém chiết quang hơn ($n_1 > n_2$), góc khúc xạ lớn hơn góc tới. Tăng góc tới dần, có lúc góc khúc xạ chạm $90^\circ$:

$$\sin i_{gh} = \frac{n_2}{n_1}$$

Vượt qua $i_{gh}$, phương trình Snell đòi hỏi $\sin r > 1$ — vô nghiệm. Vật lí trả lời: không còn tia khúc xạ nào, **toàn bộ** ánh sáng bị phản xạ. Đây là loại phản xạ duy nhất không mất năng lượng, hơn hẳn gương tráng bạc vốn hấp thụ vài phần trăm mỗi lần.

Hai điều kiện bắt buộc, thiếu một là không xảy ra:

1. Ánh sáng đi từ môi trường chiết quang **hơn** sang môi trường chiết quang **kém**.
2. Góc tới **lớn hơn** góc giới hạn.

## Sợi quang

Sợi quang gồm lõi chiết suất $n_1$ bọc bởi vỏ $n_2$ hơi nhỏ hơn. Tia sáng đi vào với góc thích hợp sẽ liên tục phản xạ toàn phần ở mặt phân cách lõi - vỏ, bị "giam" trong lõi suốt hàng chục kilômét.

Ưu điểm so với cáp đồng: băng thông rất lớn (vì tần số ánh sáng cao), suy hao nhỏ, không bị nhiễu điện từ, không dẫn điện nên an toàn. Hạn chế kĩ thuật chính là **tán sắc**: các tia đi theo đường khác nhau hoặc các bước sóng khác nhau tới đích lệch thời điểm, làm xung tín hiệu nhoè ra. Sợi đơn mode có lõi rất mảnh (cỡ 9 μm) chỉ cho một đường truyền duy nhất, khắc phục được vấn đề này.

Ứng dụng y học: nội soi dùng một bó sợi để đưa ánh sáng vào và một bó khác để dẫn ảnh ra, cho phép quan sát bên trong cơ thể mà không cần phẫu thuật lớn.

**Lỗi thường gặp:**
- Cho rằng phản xạ toàn phần xảy ra khi ánh sáng đi từ môi trường loãng sang môi trường đặc — sai vì khi đó tia gãy về gần pháp tuyến và luôn tồn tại tia khúc xạ với mọi góc tới, không bao giờ đạt điều kiện giới hạn.
- Đo góc tới so với mặt phân cách thay vì so với pháp tuyến — sai vì định luật Snell được phát biểu với pháp tuyến; nhầm lẫn này hoán đổi sin và cosin và làm kết quả sai hoàn toàn.
- Nghĩ ánh sáng trong sợi quang đi thẳng theo trục — sai vì phần lớn tia đi zigzag nhờ liên tiếp phản xạ toàn phần; chính sự khác biệt quãng đường giữa các tia gây ra tán sắc mode làm nhoè tín hiệu.

<sub>`lesson.physics.quang-hinh.khuc-xa-va-phan-xa-toan-phan`</sub>

---

### 2. Gương cầu và thấu kính mỏng theo quy ước dấu quốc tế
*Spherical mirrors and thin lenses with international sign conventions* · THPT (lớp 10-12) · ap, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Vận dụng được công thức gương cầu và thấu kính mỏng với quy ước dấu nhất quán
- Xác định được tính chất ảnh (thật hay ảo, cùng chiều hay ngược chiều, lớn hơn hay nhỏ hơn) từ dấu của kết quả
- Vẽ được ảnh bằng phương pháp ba tia đặc biệt và đối chiếu với kết quả tính toán

## Vì sao phải nói rõ quy ước dấu

Cùng một công thức thấu kính có thể xuất hiện dưới hai dạng:

$$\frac{1}{f} = \frac{1}{d} + \frac{1}{d'} \qquad \text{(real-is-positive)}$$
$$\frac{1}{f} = \frac{1}{v} - \frac{1}{u} \qquad \text{(Cartesian)}$$

Hai dạng không mâu thuẫn nhau — chúng dùng hai hệ quy ước dấu khác nhau. Sai lầm nghiêm trọng nhất trong phần quang hình là **trộn lẫn** hai hệ. Quy tắc làm việc: chọn một hệ ngay từ đầu bài và bám nó tới cuối.

Dưới đây dùng quy ước **real-is-positive** phổ biến ở IB và A Level.

## Bảng quy ước

| Đại lượng | Dương khi | Âm khi |
|---|---|---|
| $d$ (vật) | vật thật | vật ảo |
| $d'$ (ảnh) | ảnh thật | ảnh ảo |
| $f$ | hội tụ / gương lõm | phân kì / gương lồi |
| $k = -d'/d$ | ảnh cùng chiều | ảnh ngược chiều |

Công thức chung cho cả gương cầu và thấu kính mỏng, chỉ khác cách xác định $f$: gương cầu có $f = R/2$, còn thấu kính dùng công thức nhà chế tạo kính.

## Đọc kết quả

Sau khi tính, **dấu của $d'$ và $k$ chứa toàn bộ thông tin về ảnh**, không cần nhớ bảng phân loại dài dòng:

- $d' > 0$: ảnh thật, ở phía bên kia thấu kính, hứng được trên màn, luôn ngược chiều vật.
- $d' < 0$: ảnh ảo, cùng phía với vật, không hứng được, luôn cùng chiều vật.
- $|k| > 1$: ảnh lớn hơn vật; $|k| < 1$: nhỏ hơn.

Thấu kính phân kì và gương lồi luôn cho ảnh ảo, cùng chiều, nhỏ hơn vật với **mọi** vị trí vật — đây là lí do gương chiếu hậu lồi cho tầm nhìn rộng, kèm cảnh báo "vật thể ở gần hơn vẻ ngoài".

## Ba tia đặc biệt để vẽ

1. Tia song song trục chính → khúc xạ đi qua tiêu điểm ảnh.
2. Tia qua quang tâm → truyền thẳng, không đổi hướng.
3. Tia qua tiêu điểm vật → khúc xạ song song trục chính.

Chỉ cần hai tia là đủ xác định ảnh; tia thứ ba dùng để kiểm tra. Hình vẽ và phép tính phải cho cùng kết luận — nếu lệch nhau thì chắc chắn có lỗi dấu, và hình vẽ thường đúng hơn.

Ghép sát hai thấu kính: $D = D_1 + D_2$, tức $1/f = 1/f_1 + 1/f_2$. Với hệ hai thấu kính đặt cách nhau, phải giải tuần tự: ảnh của thấu kính thứ nhất trở thành vật của thấu kính thứ hai.

**Lỗi thường gặp:**
- Trộn lẫn quy ước Cartesian và real-is-positive trong cùng một bài — sai vì hai hệ gán dấu ngược nhau cho khoảng cách vật; kết quả sẽ mâu thuẫn với hình vẽ dù từng phép biến đổi đều đúng.
- Kết luận ảnh ảo là ảnh không tồn tại — sai vì ảnh ảo hoàn toàn nhìn thấy được bằng mắt (kính lúp, gương phẳng đều cho ảnh ảo); nó chỉ khác ở chỗ không hứng được lên màn vì tia sáng thật không đi qua vị trí đó.
- Quên dấu trừ trong $k = -d'/d$ — sai vì dấu này mã hoá chiều của ảnh; bỏ nó đi thì mọi ảnh đều thành cùng chiều, mâu thuẫn với thực nghiệm về ảnh thật của thấu kính hội tụ.

<sub>`lesson.physics.quang-hinh.guong-cau-va-thau-kinh`</sub>

---

### 3. Mắt và các dụng cụ quang học
*The eye and optical instruments* · THPT (lớp 10-12) · a-level, ib · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được cơ chế điều tiết của mắt và nguyên nhân của tật cận thị, viễn thị
- Xác định được loại và độ tụ của kính cần đeo để chữa từng tật
- Vận dụng được công thức độ bội giác cho kính lúp, kính hiển vi và kính thiên văn

## Mắt: thấu kính có tiêu cự thay đổi

Khác với máy ảnh (đổi khoảng cách thấu kính - phim), mắt giữ nguyên khoảng cách tới võng mạc và thay đổi **tiêu cự** bằng cách bóp hoặc dãn cơ vòng quanh thể thuỷ tinh. Đó là sự điều tiết.

Mắt bình thường nhìn rõ từ điểm cực cận $OC_c \approx 25$ cm tới điểm cực viễn ở vô cực. Khi nhìn xa, cơ hoàn toàn thả lỏng — đây là lí do sinh lí của lời khuyên nhìn ra xa sau mỗi giờ học.

## Hai tật và cách chữa

**Cận thị:** trục nhãn cầu quá dài hoặc thể thuỷ tinh quá cong, ảnh của vật ở xa hội tụ **trước** võng mạc. Điểm cực viễn không ở vô cực mà ở khoảng cách $OC_v$ hữu hạn. Cần **thấu kính phân kì** để đẩy ảnh của vật ở vô cực về đúng $C_v$:

$$f = -OC_v \quad (\text{kính đeo sát mắt})$$

**Viễn thị và mắt lão:** ảnh hội tụ **sau** võng mạc, điểm cực cận xa hơn 25 cm. Cần **thấu kính hội tụ** để đưa ảnh của vật ở 25 cm về đúng cực cận thật của mắt.

Cách suy luận không cần học thuộc: xác định vật ở đâu và ảnh cần rơi vào đâu, rồi giải công thức thấu kính. Ảnh trung gian do kính tạo ra phải nằm đúng trong khoảng nhìn rõ của mắt và luôn là **ảnh ảo**.

## Ba dụng cụ, một nguyên lí

Mọi dụng cụ quang đều nhằm **tăng góc trông**, vì kích thước ảnh trên võng mạc phụ thuộc góc trông chứ không phụ thuộc kích thước thật của vật.

**Kính lúp** (một thấu kính hội tụ tiêu cự ngắn): đặt vật trong khoảng tiêu cự để có ảnh ảo lớn hơn. Ngắm chừng ở vô cực cho

$$G_\infty = \frac{\text{Đ}}{f} \quad (\text{Đ} = 25\ \text{cm})$$

**Kính hiển vi** (hai thấu kính): vật kính tiêu cự rất ngắn tạo ảnh thật phóng đại, thị kính dùng như kính lúp để phóng đại tiếp:

$$G_\infty = |k_1|\cdot G_2 = \frac{\delta\,\text{Đ}}{f_1f_2}$$

với $\delta$ là độ dài quang học (khoảng cách giữa hai tiêu điểm trong).

**Kính thiên văn** (hai thấu kính): vật ở vô cực nên vật kính có tiêu cự **rất dài**, tạo ảnh tại tiêu diện; thị kính ngắm ảnh đó:

$$G_\infty = \frac{f_1}{f_2}$$

Điểm cần nhớ: kính hiển vi cần **cả hai** tiêu cự ngắn, còn kính thiên văn cần vật kính **dài** và thị kính ngắn. Ngoài ra, với kính thiên văn thì đường kính vật kính quan trọng không kém độ bội giác, vì nó quyết định lượng ánh sáng thu được và giới hạn phân giải theo tiêu chuẩn Rayleigh.

**Lỗi thường gặp:**
- Cho rằng mắt điều tiết bằng cách thay đổi khoảng cách từ thể thuỷ tinh tới võng mạc — sai vì khoảng cách đó cố định; mắt thay đổi độ cong của thể thuỷ tinh, tức thay đổi tiêu cự.
- Dùng thấu kính hội tụ để chữa cận thị — sai vì mắt cận đã hội tụ ảnh quá sớm, thêm kính hội tụ càng làm ảnh rơi xa võng mạc hơn; cần kính phân kì để dời ảnh về phía sau.
- Đồng nhất độ bội giác với độ phóng đại dài — sai vì độ bội giác so sánh GÓC TRÔNG chứ không so sánh kích thước; một ảnh ảo rất lớn ở rất xa vẫn có thể cho góc trông nhỏ.

<sub>`lesson.physics.quang-hinh.mat-va-dung-cu-quang`</sub>

---

## Unit 7: Simple Harmonic Motion (AP Physics 1 Unit 7 / IB C.1 / CIE 9702 Topic 17)

### 1. Điều kiện dao động điều hòa và con lắc lò xo
*Conditions for simple harmonic motion and the mass-spring oscillator* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu được điều kiện định nghĩa của dao động điều hòa dưới dạng phương trình gia tốc
- Chứng minh được con lắc lò xo dao động điều hòa và tính được chu kì của nó
- Vận dụng được hệ thức độc lập thời gian giữa li độ và vận tốc

## Định nghĩa bằng phương trình, không bằng hình dáng

Một chuyển động là điều hòa khi và chỉ khi

$$a = -\omega^{2}x \qquad\text{tương đương}\qquad F_{\text{hợp}} = -kx$$

Hai đặc điểm phải có: độ lớn **tỉ lệ** với li độ, và chiều **luôn hướng về** vị trí cân bằng (dấu trừ). Nếu chỉ có lực kéo về mà không tỉ lệ, dao động vẫn tuần hoàn nhưng không điều hòa.

Nghiệm của phương trình vi phân $\ddot{x} + \omega^{2}x = 0$ là

$$x = A\cos(\omega t + \varphi), \quad v = -A\omega\sin(\omega t + \varphi), \quad a = -A\omega^{2}\cos(\omega t + \varphi)$$

IB quy ước dùng hàm sin, AP thường dùng cosin; chỉ khác nhau ở pha ban đầu.

## Đọc quan hệ pha

$v$ sớm pha $\pi/2$ so với $x$; $a$ ngược pha với $x$. Hệ quả trực quan:

- Tại **biên**: $|x|$ cực đại, $v = 0$, $|a|$ cực đại.
- Tại **cân bằng**: $x = 0$, $|v| = A\omega$ cực đại, $a = 0$.

## Con lắc lò xo

Tại li độ $x$, hợp lực là $F = -kx$, nên $a = -(k/m)x$. So sánh với định nghĩa:

$$\omega = \sqrt{\frac{k}{m}}, \qquad T = 2\pi\sqrt{\frac{m}{k}}$$

Điều đáng kinh ngạc: **chu kì không phụ thuộc biên độ**. Kéo lò xo ra xa gấp đôi thì lực kéo về cũng gấp đôi, gia tốc gấp đôi, vật đi quãng đường gấp đôi trong đúng khoảng thời gian ấy. Tính chất này gọi là tính đẳng thời và là cơ sở của mọi đồng hồ cơ.

Với lò xo treo thẳng đứng, kết quả vẫn y nguyên: trọng lực chỉ dời vị trí cân bằng xuống đoạn $\Delta l_0 = mg/k$ mà không đổi $\omega$. Từ đó có công thức tiện dụng $T = 2\pi\sqrt{\Delta l_0/g}$.

## Hệ thức độc lập thời gian

$$A^{2} = x^{2} + \frac{v^{2}}{\omega^{2}}$$

Dùng khi đề cho $x$ và $v$ tại cùng một thời điểm mà không cho pha.

**Lỗi thường gặp:**
- Cho rằng chu kì phụ thuộc biên độ. Từ $T = 2\pi\sqrt{m/k}$ thấy biên độ không xuất hiện; kéo mạnh hơn chỉ làm vật đi nhanh hơn trên quãng đường dài hơn, hai hiệu ứng bù trừ chính xác.
- Nhầm vị trí có gia tốc cực đại với vị trí có vận tốc cực đại. Vì $a = -\omega^{2}x$, gia tốc cực đại ở biên nơi vận tốc bằng 0, còn vận tốc cực đại ở cân bằng nơi gia tốc bằng 0.
- Áp dụng công thức dao động điều hòa cho con lắc lò xo bị kéo quá giới hạn đàn hồi. Khi đó $F$ không còn tỉ lệ với $x$ nên điều kiện định nghĩa $a = -\omega^{2}x$ bị phá vỡ.

<sub>`lesson.physics.dao-dong-intl.dieu-kien-shm-va-con-lac-lo-xo`</sub>

---

### 2. Con lắc đơn và năng lượng trong dao động điều hòa
*The simple pendulum and energy in SHM* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Chứng minh được con lắc đơn dao động điều hòa trong điều kiện góc lệch nhỏ
- Tính được động năng, thế năng và cơ năng của vật dao động điều hòa tại mọi li độ
- Giải thích được vì sao động năng và thế năng biến thiên với tần số gấp đôi tần số dao động

## Con lắc đơn: điều hòa có điều kiện

Thành phần trọng lực dọc theo cung là $F = -mg\sin\theta$. Đây **không** phải dạng $-kx$ vì $\sin\theta$ không tỉ lệ với $\theta$. Nhưng khi góc nhỏ, $\sin\theta \approx \theta = s/l$, nên

$$F \approx -\frac{mg}{l}s \Rightarrow \omega = \sqrt{\frac{g}{l}}, \qquad T = 2\pi\sqrt{\frac{l}{g}}$$

Chu kì **không phụ thuộc khối lượng** (vì $m$ triệt tiêu giữa lực và quán tính) và **không phụ thuộc biên độ** (chỉ trong xấp xỉ góc nhỏ). Với biên độ lớn, chu kì thực tăng dần: ở $30$ độ đã sai khoảng 1,7 phần trăm.

Ứng dụng quan trọng: đo $g$ chính xác đến bốn chữ số bằng dụng cụ đơn giản, chỉ cần đo $l$ và $T$.

## Năng lượng: cuộc chuyển hoá tuần hoàn

$$E_p = \tfrac12 kx^{2}, \qquad E_k = \tfrac12 mv^{2} = \tfrac12 k(A^{2} - x^{2}), \qquad E = \tfrac12 kA^{2}$$

Hai đường cong $E_p(x)$ và $E_k(x)$ là hai parabol ngược nhau, tổng luôn là đường nằm ngang. Vì $E \propto A^{2}$, tăng biên độ gấp đôi thì cơ năng gấp **bốn**.

## Tần số gấp đôi

Thay $x = A\cos\omega t$ vào $E_p = \tfrac12 kx^{2}$ và dùng $\cos^{2}u = \tfrac12(1 + \cos 2u)$:

$$E_p = \tfrac14 kA^{2}\left(1 + \cos 2\omega t\right)$$

Vậy năng lượng dao động với tần số góc $2\omega$, tức chu kì $T/2$. Lí do trực quan: trong một chu kì, vật qua vị trí cân bằng **hai lần** và tới biên **hai lần**, nên mỗi chu kì năng lượng hoàn thành hai vòng chuyển hoá. Giá trị trung bình của cả $E_p$ và $E_k$ đều bằng $E/2$.

## Con lắc vật lí

Với vật rắn treo tại điểm cách khối tâm $d$: $\tau = -mgd\sin\theta \approx -mgd\,\theta$, kết hợp $\tau = I\alpha$ cho

$$T = 2\pi\sqrt{\frac{I}{mgd}}$$

Con lắc đơn là trường hợp riêng với $I = ml^{2}$ và $d = l$.

**Lỗi thường gặp:**
- Dùng công thức $T = 2\pi\sqrt{l/g}$ cho biên độ góc lớn. Xấp xỉ $\sin\theta \approx \theta$ chỉ tốt dưới khoảng 15 độ; ở biên độ 60 độ chu kì thực lớn hơn công thức tới 7 phần trăm.
- Cho rằng động năng và thế năng biến thiên với cùng chu kì $T$ như li độ. Vì chúng tỉ lệ với bình phương của các hàm điều hòa, chu kì biến thiên của chúng chỉ là $T/2$.
- Nghĩ con lắc nặng hơn dao động chậm hơn. Khối lượng triệt tiêu trong $T = 2\pi\sqrt{l/g}$ vì trọng lực gây dao động và quán tính cản dao động đều tỉ lệ với $m$.

<sub>`lesson.physics.dao-dong-intl.con-lac-don-va-nang-luong-dao-dong`</sub>

---

### 3. Dao động tắt dần, dao động cưỡng bức và cộng hưởng
*Damped oscillations, forced oscillations and resonance* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Phân biệt được ba chế độ tắt dần thiếu, tới hạn và quá tắt dần qua dạng đồ thị li độ
- Xác định được điều kiện cộng hưởng và ảnh hưởng của lực cản lên đường cong cộng hưởng
- Phân tích được ví dụ thực tế trong đó cộng hưởng có lợi hoặc gây hại

## Thực tế: mọi dao động đều tắt

Có lực cản, cơ năng giảm dần. Với cản nhỏ (tắt dần thiếu), vật vẫn dao động qua lại nhưng biên độ giảm theo hàm mũ, còn chu kì gần như không đổi. Ba chế độ:

| Chế độ | Hành vi | Ứng dụng |
|---|---|---|
| Tắt dần thiếu (light) | Dao động nhiều lần, biên độ giảm dần | Dây đàn, con lắc trong không khí |
| Tới hạn (critical) | Về cân bằng nhanh nhất, không vượt quá | Giảm xóc ô tô, kim đồng hồ đo |
| Quá tắt dần (heavy) | Về cân bằng chậm, không dao động | Cửa tự đóng, giảm chấn nặng |

Điểm dễ nhầm: quá tắt dần **chậm hơn** tới hạn, dù cản mạnh hơn.

## Dao động cưỡng bức

Tác dụng ngoại lực tuần hoàn tần số $f$. Sau giai đoạn chuyển tiếp, hệ dao động **ổn định với đúng tần số $f$ của ngoại lực**, không phải tần số riêng $f_0$. Biên độ phụ thuộc vào việc $f$ gần $f_0$ đến đâu.

## Cộng hưởng

Khi $f \approx f_0$, mỗi chu kì ngoại lực đẩy đúng lúc và cùng chiều chuyển động, năng lượng được bơm vào liên tục và biên độ vọt lên. Vai trò của lực cản:

- Cản nhỏ: đỉnh cộng hưởng **cao và nhọn**, tần số cộng hưởng gần $f_0$.
- Cản lớn: đỉnh **thấp và tù**, và đỉnh còn dịch về phía tần số thấp hơn $f_0$.

Độ nhọn được đo bằng hệ số phẩm chất $Q$: $Q$ càng lớn thì đỉnh càng nhọn và hệ càng chọn lọc tần số.

## Cộng hưởng có ích và có hại

**Có ích**: mạch LC chọn đài phát thanh; lò vi sóng kích thích dao động phân tử nước; máy MRI cộng hưởng từ hạt nhân; nhạc cụ dùng hộp cộng hưởng để khuếch đại âm.

**Có hại**: cầu Tacoma Narrows sụp năm 1940 (chính xác hơn, đây là dao động tự kích flutter khí động - đàn hồi chứ không phải cộng hưởng với một tần số cưỡng bức có sẵn); binh lính phải phá bước đều khi qua cầu; máy giặt rung dữ dội ở một tốc độ vắt nhất định rồi lại êm khi vượt qua. Kỹ sư chống lại bằng cách hoặc dời $f_0$ ra xa tần số kích thích, hoặc tăng cản để hạ đỉnh cộng hưởng.

**Lỗi thường gặp:**
- Cho rằng hệ dao động cưỡng bức sẽ dao động với tần số riêng của nó. Ở trạng thái ổn định, hệ dao động đúng tần số của ngoại lực; tần số riêng chỉ quyết định biên độ lớn hay nhỏ.
- Nghĩ cản càng mạnh thì hệ càng nhanh trở về cân bằng. Vượt quá mức tới hạn, hệ chuyển sang quá tắt dần và bò về vị trí cân bằng chậm hơn hẳn; tới hạn mới là mức nhanh nhất.
- Cho rằng cộng hưởng luôn xảy ra đúng tại $f_0$. Khi có lực cản đáng kể, đỉnh biên độ dịch về tần số thấp hơn $f_0$ một chút và thấp đi rõ rệt; chỉ khi cản rất nhỏ đỉnh mới trùng $f_0$.

<sub>`lesson.physics.dao-dong-intl.tat-dan-cuong-buc-va-cong-huong`</sub>

---

## Unit 8: Gravitation (AP Physics 1 Unit 2 và 6 / IB D.1 / CIE 9702 Topic 13)

### 1. Định luật vạn vật hấp dẫn và trường hấp dẫn
*Newton's law of universal gravitation and gravitational fields* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được định luật vạn vật hấp dẫn cho hai chất điểm và cho vật đối xứng cầu
- Phân biệt được cường độ trường hấp dẫn với gia tốc rơi tự do về mặt khái niệm
- Phân tích được sự phụ thuộc của $g$ theo độ cao và theo độ sâu trong lòng Trái Đất

## Táo rơi và Mặt Trăng quay: cùng một lực

Bước nhảy vọt của Newton là nhận ra lực giữ Mặt Trăng trên quỹ đạo và lực làm quả táo rơi có cùng bản chất:

$$F = G\frac{m_1m_2}{r^{2}}$$

Bốn điều cần nhớ về công thức này: lực luôn **hút**, luôn dọc đường nối hai vật, tuân theo định luật III (hai lực bằng nhau dù khối lượng rất khác nhau), và $r$ là khoảng cách giữa **hai tâm** chứ không phải khoảng cách bề mặt.

## Vì sao dùng được cho quả cầu

Định lí vỏ cầu cho phép thay Trái Đất bằng một chất điểm ở tâm khi tính lực lên vật bên ngoài. Không có định lí này, công thức chỉ áp dụng được cho chất điểm và toàn bộ bài toán thiên văn sụp đổ. Newton đã phải phát minh phép tính vi tích phân để chứng minh nó.

## Trường hấp dẫn

$$g = \frac{F}{m} = \frac{GM}{r^{2}}$$

Đây là **cường độ trường**, đo bằng N/kg. Về số trị nó trùng gia tốc rơi tự do đo bằng $\mathrm{m/s^{2}}$, nhưng khác nhau về khái niệm: trường tồn tại ngay cả khi không có vật nào để rơi. IB và A-Level phân biệt rất rõ hai cách diễn đạt này.

## $g$ thay đổi thế nào

- **Ngoài Trái Đất**, cách tâm $r > R$: $g = GM/r^{2}$, giảm theo bình phương. Ở độ cao 400 km, $g$ còn khoảng $8{,}7\ \mathrm{m/s^{2}}$.
- **Trong lòng Trái Đất** (coi đồng chất), chỉ phần khối lượng nằm trong bán kính $r$ mới tác dụng lực, phần vỏ ngoài không tác dụng gì. Vì $M_{\text{trong}} \propto r^{3}$ nên $g \propto r$: giảm **tuyến tính** về 0 tại tâm.

Đồ thị $g$ theo $r$ vì thế tăng tuyến tính từ tâm tới mặt đất rồi giảm theo $1/r^{2}$ ra ngoài — một dạng đồ thị hay được hỏi ở đề A-Level.

Trên thực tế $g$ còn thay đổi theo vĩ độ (do Trái Đất dẹt và do lực quán tính li tâm) và theo địa chất địa phương.

**Lỗi thường gặp:**
- Dùng độ cao $h$ thay cho khoảng cách tới tâm $r = R + h$. Định luật vạn vật hấp dẫn đo khoảng cách giữa hai tâm; với vệ tinh ở 400 km thì $r$ là 6770 km chứ không phải 400 km, sai số lên tới vài trăm lần.
- Cho rằng vật càng xuống sâu thì $g$ càng lớn vì gần tâm hơn. Phần vỏ cầu bên ngoài không tác dụng lực nào, nên khối lượng hiệu dụng giảm theo $r^{3}$ nhanh hơn $r^{2}$ ở mẫu số, kết quả là $g$ giảm tuyến tính về 0 tại tâm.
- Nhầm hằng số $G$ với gia tốc $g$. $G$ là hằng số vũ trụ bằng $6{,}67\times10^{-11}$ với đơn vị $\mathrm{N\,m^{2}\,kg^{-2}}$, còn $g$ phụ thuộc thiên thể và vị trí, đơn vị N/kg.

<sub>`lesson.physics.hap-dan-intl.dinh-luat-van-vat-hap-dan-va-truong`</sub>

---

### 2. Thế năng hấp dẫn, thế hấp dẫn và tốc độ thoát
*Gravitational potential energy, potential and escape speed* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao thế năng hấp dẫn tổng quát mang dấu âm
- Phân biệt được thế năng hấp dẫn của hệ với thế hấp dẫn tại một điểm
- Tính được tốc độ thoát và cơ năng toàn phần của vệ tinh trên quỹ đạo tròn

## Vì sao thế năng lại âm

Chọn mốc $E_p = 0$ tại vô cực là quy ước tự nhiên nhất, vì ở đó hai vật hoàn toàn không tương tác. Kéo hai vật lại gần nhau, lực hấp dẫn sinh công dương nên thế năng phải **giảm** — tức trở thành âm:

$$E_p = -\frac{GMm}{r}$$

Dấu âm mang thông tin quan trọng: hệ **bị liên kết**. Muốn tách hai vật ra vô cực phải cấp năng lượng đúng bằng $GMm/r$.

Công thức quen thuộc $E_p = mgh$ chỉ là **trường hợp riêng** khi $h \ll R$: khi đó $\Delta E_p = GMm\left(\frac{1}{R} - \frac{1}{R+h}\right) \approx \frac{GMm}{R^{2}}h = mgh$.

## Thế và thế năng: đừng lẫn

$$V = -\frac{GM}{r}\ (\mathrm{J/kg}) \qquad\text{và}\qquad E_p = mV\ (\mathrm{J})$$

Thế $V$ là thuộc tính của **điểm trong không gian**; thế năng là thuộc tính của **hệ** gồm điểm đó và vật thử. Quan hệ với cường độ trường: $g = -dV/dr$.

## Tốc độ thoát

Điều kiện thoát: cơ năng toàn phần không âm, vì chỉ khi đó vật mới tới được vô cực.

$$\tfrac12 mv^{2} - \frac{GMm}{R} \ge 0 \Rightarrow v_{th} = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$$

Với Trái Đất, $v_{th} = 11{,}2$ km/s. Con số này **không phụ thuộc khối lượng vật phóng** và cũng không phụ thuộc hướng phóng (khi bỏ qua khí quyển và sự quay của Trái Đất).

Mặt Trăng có $v_{th} = 2{,}4$ km/s, quá nhỏ để giữ khí quyển vì phân tử khí ở nhiệt độ ban ngày có tốc độ đủ lớn để thoát dần. Đó là lời giải thích vật lí cho việc Mặt Trăng trơ trụi.

## Cơ năng của vệ tinh

Với quỹ đạo tròn bán kính $r$: $E_k = \frac{GMm}{2r}$ và $E_p = -\frac{GMm}{r}$, nên

$$E = E_k + E_p = -\frac{GMm}{2r} = -E_k$$

Hệ quả nghịch lí: vệ tinh ở quỹ đạo **thấp** hơn có cơ năng nhỏ hơn nhưng tốc độ **lớn** hơn. Ma sát khí quyển làm vệ tinh mất năng lượng và... bay nhanh hơn trong khi tụt dần xuống.

**Lỗi thường gặp:**
- Cho rằng thế năng âm là vô nghĩa hoặc là dấu hiệu tính sai. Dấu âm chỉ phản ánh việc chọn mốc tại vô cực; điều có ý nghĩa vật lí là **độ biến thiên** thế năng, luôn dương khi đưa vật ra xa.
- Dùng $E_p = mgh$ cho vệ tinh ở độ cao hàng trăm km. Công thức đó giả thiết $g$ không đổi, chỉ đúng khi $h \ll R$; ở 300 km, $g$ đã giảm gần 9 phần trăm và sai số tích luỹ rất lớn.
- Nghĩ tốc độ thoát phụ thuộc khối lượng tàu vũ trụ. Khối lượng $m$ triệt tiêu ở cả hai vế của phương trình năng lượng, nên viên đạn và con tàu đều cần đúng 11,2 km/s.

<sub>`lesson.physics.hap-dan-intl.the-hap-dan-va-toc-do-thoat`</sub>

---

### 3. Ba định luật Kepler, chuyển động vệ tinh và trạng thái không trọng lượng
*Kepler's three laws, satellite motion and weightlessness* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu được ba định luật Kepler và dẫn ra định luật III từ định luật vạn vật hấp dẫn
- Tính được bán kính và chu kì của quỹ đạo địa tĩnh
- Giải thích được bản chất của trạng thái không trọng lượng trên trạm vũ trụ

## Ba định luật của Kepler

Kepler rút ra chúng từ dữ liệu quan sát của Tycho Brahe, trước Newton nửa thế kỷ. Newton sau đó chứng minh cả ba là hệ quả của định luật vạn vật hấp dẫn.

1. **Quỹ đạo elip**, Mặt Trời ở một tiêu điểm.
2. **Diện tích quét bằng nhau trong thời gian bằng nhau**. Hệ quả: hành tinh chạy nhanh nhất ở cận điểm, chậm nhất ở viễn điểm. Đây là bảo toàn mômen động lượng $L = mr^{2}\dot{\theta}$ viết bằng ngôn ngữ hình học.
3. $$\frac{T^{2}}{a^{3}} = \frac{4\pi^{2}}{GM} = \text{hằng số cho mọi vật quay quanh cùng thiên thể}$$

## Dẫn ra định luật III cho quỹ đạo tròn

Lực hấp dẫn đóng vai trò lực hướng tâm:

$$\frac{GMm}{r^{2}} = \frac{mv^{2}}{r} = m\omega^{2}r = m\frac{4\pi^{2}}{T^{2}}r$$

Rút gọn $m$ rồi sắp xếp lại cho ngay $T^{2} = \dfrac{4\pi^{2}}{GM}r^{3}$. Khối lượng vệ tinh triệt tiêu, nên **mọi vật ở cùng bán kính quỹ đạo đều có cùng chu kì**, dù là hòn sỏi hay trạm vũ trụ.

Từ đó cũng có: $v = \sqrt{GM/r}$ — quỹ đạo càng cao thì tốc độ càng chậm.

## Quỹ đạo địa tĩnh

Đặt $T = 86164$ s (một ngày sao) vào định luật III với $M$ của Trái Đất, ta được $r = 4{,}22\times10^{7}$ m, tức độ cao khoảng 35 800 km. Vệ tinh viễn thông và vệ tinh thời tiết đều nằm ở vành đai này; đó là lí do ăng-ten chảo cố định hướng được về một điểm trên trời.

Ba điều kiện bắt buộc: đúng bán kính đó, nằm trong mặt phẳng xích đạo, và quay cùng chiều Trái Đất.

## Không trọng lượng, giải thích cho đúng

Ở độ cao trạm ISS (400 km), $g$ vẫn bằng 89 phần trăm giá trị mặt đất. Phi hành gia lơ lửng **không phải vì hết trọng lực**, mà vì trạm và người cùng rơi tự do quanh Trái Đất với cùng gia tốc, nên sàn không đẩy vào chân họ: phản lực $N = 0$. Trạng thái này giống hệt người trong thang máy đứt cáp, chỉ khác là quỹ đạo cong khép kín nên họ "rơi mãi mà không chạm đất".

**Lỗi thường gặp:**
- Cho rằng phi hành gia không trọng lượng vì ở ngoài vùng ảnh hưởng của trọng lực. Ở độ cao 400 km, $g$ vẫn còn 8,7 N/kg; họ lơ lửng vì cùng rơi tự do với trạm nên phản lực bằng 0.
- Áp dụng định luật III Kepler cho các vật quay quanh những thiên thể khác nhau. Hằng số $4\pi^{2}/(GM)$ phụ thuộc khối lượng thiên thể trung tâm, nên không so sánh trực tiếp được vệ tinh Trái Đất với hành tinh quanh Mặt Trời.
- Nghĩ vệ tinh ở quỹ đạo cao hơn phải bay nhanh hơn. Từ $v = \sqrt{GM/r}$, tốc độ giảm khi $r$ tăng; vệ tinh địa tĩnh chỉ bay khoảng 3,1 km/s trong khi vệ tinh quỹ đạo thấp bay 7,9 km/s.

<sub>`lesson.physics.hap-dan-intl.kepler-va-chuyen-dong-ve-tinh`</sub>

---

## Unit 8: Vật lí lượng tử - Quantum Physics

### 1. Bức xạ vật đen và thảm hoạ tử ngoại
*Blackbody radiation and the ultraviolet catastrophe* · THPT (lớp 10-12) · ap, ib · 45 phút · nang-cao

**Mục tiêu:**
- Mô tả được đặc điểm phổ bức xạ của vật đen và vận dụng định luật dịch chuyển Wien
- Giải thích được vì sao vật lí cổ điển thất bại khi mô tả bức xạ vật đen ở bước sóng ngắn
- Trình bày được giả thuyết lượng tử của Planck và ý nghĩa cách mạng của nó

## Bài toán tưởng chừng đơn giản

Mọi vật nóng đều phát bức xạ. Nung thanh sắt: nó đỏ lên, rồi cam, rồi trắng. Đường cong cường độ theo bước sóng có ba đặc điểm thực nghiệm rõ ràng:

1. Mỗi nhiệt độ cho một **đỉnh** ở bước sóng xác định, thoả định luật Wien:
$$\lambda_{\max}T = 2{,}90\times10^{-3}\ \text{m·K}$$
2. Tổng công suất bức xạ tăng rất nhanh theo nhiệt độ (Stefan-Boltzmann): $P = \sigma AT^4$.
3. Cường độ **giảm về 0** khi bước sóng tiến về 0.

Đặc điểm thứ ba tưởng tầm thường, nhưng nó phá huỷ toàn bộ vật lí cổ điển.

## Thảm hoạ tử ngoại

Rayleigh và Jeans áp dụng đúng quy trình cổ điển: đếm số mode sóng đứng trong hốc, gán cho mỗi mode năng lượng trung bình $k_BT$ theo định lí phân bố đều. Kết quả:

$$u(\lambda) \propto \frac{k_BT}{\lambda^4}$$

Công thức này khớp rất tốt ở bước sóng dài, nhưng khi $\lambda \to 0$ nó **phân kì ra vô cùng**. Nghĩa là: mở cửa lò nướng ở nhiệt độ phòng thì ta phải bị thiêu cháy bởi tia tử ngoại và tia X. Đây là "thảm hoạ tử ngoại" — không phải một sai sót tính toán mà là hệ quả logic không thể tránh của vật lí cổ điển.

## Giải pháp táo bạo của Planck

Năm 1900, Planck giả thiết rằng dao động tử trong thành hốc **không** trao đổi năng lượng liên tục, mà chỉ theo từng gói rời rạc $\varepsilon = hf$.

Hệ quả tự nhiên và tinh tế: mode tần số cao đòi hỏi gói năng lượng lớn. Ở nhiệt độ $T$, năng lượng nhiệt trung bình sẵn có chỉ cỡ $k_BT$; nếu $hf \gg k_BT$ thì hầu như không mode nào đủ "tiền" để mua nổi dù chỉ một gói. Các mode tần số cao vì thế bị **đóng băng**, và cường độ tự động triệt tiêu ở bước sóng ngắn.

Công thức Planck khớp hoàn hảo với thực nghiệm trên toàn dải, và cho lại Rayleigh-Jeans ở giới hạn bước sóng dài.

## Vì sao đây là bước ngoặt

Bản thân Planck xem $h$ chỉ là một thủ thuật toán học và mất nhiều năm cố loại bỏ nó. Nhưng năm 1905 Einstein dùng chính ý tưởng ấy giải thích hiệu ứng quang điện, và hằng số $h$ trở thành hằng số nền tảng thứ ba của tự nhiên bên cạnh $c$ và $G$. Ngày 14 tháng 12 năm 1900 vì thế thường được coi là ngày khai sinh của vật lí lượng tử.

Ứng dụng: đo $\lambda_{\max}$ của một ngôi sao cho ngay nhiệt độ bề mặt của nó mà không cần tới đó — nền tảng của toàn bộ thiên văn vật lí.

**Lỗi thường gặp:**
- Dùng nhiệt độ Celsius trong định luật Wien và Stefan-Boltzmann — sai vì cả hai định luật xuất phát từ nhiệt động lực học nên bắt buộc dùng thang Kelvin; dùng Celsius có thể cho cả kết quả âm, vô nghĩa vật lí.
- Nghĩ vật nóng chỉ phát bức xạ ở bước sóng đỉnh — sai vì phổ vật đen liên tục trải trên mọi bước sóng; $\lambda_{\max}$ chỉ là nơi cường độ lớn nhất, không phải bức xạ duy nhất.
- Cho rằng thảm hoạ tử ngoại là do tính toán sai của Rayleigh và Jeans — sai vì phép tính của họ hoàn toàn đúng theo vật lí cổ điển; chính các tiên đề cổ điển mới là cái sai, và đó là lí do phải đưa vào giả thuyết lượng tử.

<sub>`lesson.physics.luong-tu.buc-xa-vat-den`</sub>

---

### 2. Hiệu ứng quang điện và bằng chứng hạt của ánh sáng
*The photoelectric effect and the particle evidence for light* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Nêu được bốn đặc điểm thực nghiệm mà lí thuyết sóng không giải thích được
- Vận dụng được phương trình Einstein về hiệu ứng quang điện và khái niệm công thoát
- Xác định được hằng số Planck từ đồ thị hiệu điện thế hãm theo tần số

## Bốn sự thật mà mô hình sóng không nuốt trôi

Chiếu ánh sáng vào tấm kim loại, electron bật ra. Bốn quan sát thực nghiệm:

1. **Có ngưỡng tần số $f_0$.** Ánh sáng dưới ngưỡng, dù cường độ cực mạnh, không bứt được electron nào.
2. **Không có độ trễ.** Electron bật ra trong khoảng $10^{-9}$ s kể cả với ánh sáng cực yếu.
3. **Động năng cực đại phụ thuộc tần số, không phụ thuộc cường độ.**
4. **Cường độ chỉ ảnh hưởng số lượng electron**, tức dòng bão hoà.

Mô hình sóng dự đoán ngược lại toàn bộ: theo nó, năng lượng sóng trải đều nên electron cần thời gian tích luỹ (mâu thuẫn 2), và cường độ mạnh thì electron nhận nhiều năng lượng hơn (mâu thuẫn 3, 4). Về ngưỡng tần số, mô hình sóng không có lí do nào để tồn tại một ngưỡng như vậy.

## Lời giải của Einstein

Ánh sáng không chỉ trao đổi năng lượng theo gói (như Planck nói), mà **bản thân nó là các gói** — photon, mỗi photon mang $\varepsilon = hf$. Một electron hấp thụ **trọn vẹn một photon** trong một lần va chạm, không tích luỹ dần:

$$hf = A + W_{đ\max} = A + \frac{1}{2}mv_{\max}^2$$

Bốn quan sát được giải thích ngay lập tức:

- $hf < A$: photon không đủ trả "phí vào cửa", electron không thoát dù có bao nhiêu photon đi nữa. Đó là ngưỡng $f_0 = A/h$.
- Va chạm là tức thời nên không có độ trễ.
- $W_{đ\max} = hf - A$ chỉ phụ thuộc tần số.
- Tăng cường độ = tăng **số photon** = tăng số electron bật ra, không tăng năng lượng mỗi electron.

## Đo hằng số Planck

Viết lại phương trình theo hiệu điện thế hãm:

$$U_h = \frac{h}{e}f - \frac{A}{e}$$

Đây là **hàm bậc nhất** của $f$. Vẽ đồ thị $U_h$ theo $f$ cho đường thẳng với:

- Hệ số góc $= h/e$ → xác định được $h$.
- Giao trục hoành $= f_0$ → xác định ngưỡng.
- Giao trục tung $= -A/e$ → xác định công thoát.

Điều đẹp đẽ: thay đổi kim loại chỉ **tịnh tiến** đường thẳng chứ không đổi hệ số góc, vì $h$ là hằng số phổ quát còn $A$ đặc trưng cho vật liệu. Millikan làm thí nghiệm này suốt mười năm với ý định bác bỏ Einstein, và cuối cùng lại xác nhận ông chính xác đến từng phần trăm.

## Kết luận về bản chất ánh sáng

Giao thoa và nhiễu xạ chứng minh ánh sáng là sóng; quang điện chứng minh nó là hạt. Cả hai đều là thực nghiệm không thể chối cãi. Ánh sáng vì thế không phải sóng cũng không phải hạt theo nghĩa cổ điển, mà là một thực thể lượng tử bộc lộ mặt này hay mặt kia tuỳ cách ta hỏi nó.

**Lỗi thường gặp:**
- Cho rằng chiếu ánh sáng đủ mạnh thì kim loại nào cũng bật electron — sai vì mỗi electron chỉ hấp thụ một photon; nếu năng lượng một photon nhỏ hơn công thoát thì số lượng photon nhiều đến đâu cũng vô ích.
- Nghĩ hiệu điện thế hãm phụ thuộc cường độ ánh sáng — sai vì nó đo động năng cực đại của electron, mà động năng ấy chỉ do hiệu $hf - A$ quyết định; cường độ chỉ ảnh hưởng số electron.
- So sánh bước sóng ngược chiều với năng lượng — sai vì bước sóng LỚN ứng với năng lượng NHỎ; điều kiện xảy ra hiệu ứng là $\lambda \le \lambda_0$ chứ không phải $\lambda \ge \lambda_0$.

<sub>`lesson.physics.luong-tu.hieu-ung-quang-dien`</sub>

---

### 3. Quang phổ vạch và mẫu nguyên tử Bohr
*Line spectra and the Bohr model of the atom* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được sự hình thành quang phổ vạch phát xạ và quang phổ vạch hấp thụ
- Vận dụng được hai tiên đề Bohr để tính bước sóng các vạch của nguyên tử hiđrô
- Đánh giá được thành công và hạn chế của mẫu Bohr

## Vấn đề mà mẫu Rutherford để lại

Rutherford chứng minh nguyên tử có hạt nhân nhỏ và electron quay quanh. Nhưng theo điện động lực học cổ điển, điện tích chuyển động có gia tốc phải bức xạ; electron sẽ mất năng lượng và rơi vào hạt nhân trong khoảng $10^{-11}$ s. Nguyên tử lẽ ra không tồn tại nổi một phần tỉ giây.

Thêm nữa, khí loãng bị kích thích chỉ phát ra những **vạch rời rạc** rất sắc nét chứ không phải dải liên tục. Mỗi nguyên tố có bộ vạch riêng như dấu vân tay. Vật lí cổ điển không lí giải nổi cả hai sự thật này.

## Hai tiên đề Bohr

**Tiên đề 1 - trạng thái dừng.** Nguyên tử chỉ tồn tại ở những trạng thái có năng lượng xác định $E_n$; khi ở đó, nó **không bức xạ**. Đây là một khẳng định thẳng thừng rằng điện động lực học cổ điển không áp dụng được ở cấp nguyên tử.

**Tiên đề 2 - bức xạ và hấp thụ.** Nguyên tử phát hoặc thu photon khi chuyển giữa hai trạng thái dừng:

$$hf = E_{\text{cao}} - E_{\text{thấp}}$$

Đây chính là nguồn gốc của quang phổ vạch: vì $E_n$ rời rạc nên hiệu của chúng cũng rời rạc, và chỉ những tần số nhất định được phát ra.

## Với nguyên tử hiđrô

Thêm điều kiện lượng tử hoá mômen động lượng $L = n\hbar$, Bohr thu được:

$$r_n = n^2r_0\ (r_0 = 0{,}53\ \text{Å}), \qquad E_n = -\frac{13{,}6}{n^2}\ \text{eV}$$

Cách đọc dấu âm: năng lượng bằng 0 ứng với electron ở vô cùng, tự do. Trạng thái liên kết có năng lượng âm, và cần cung cấp đúng 13,6 eV để ion hoá hiđrô từ trạng thái cơ bản.

Bước sóng phát ra khi chuyển từ $n$ về $m$:

$$\frac{1}{\lambda} = R_H\left(\frac{1}{m^2} - \frac{1}{n^2}\right)$$

Dãy Lyman ($m=1$, tử ngoại), Balmer ($m=2$, nhìn thấy), Paschen ($m=3$, hồng ngoại). Từ mức $n$ có thể có tối đa $C_n^2 = n(n-1)/2$ vạch.

## Hấp thụ: cùng một bộ vạch

Chiếu ánh sáng trắng qua khí hiđrô nguội: khí hấp thụ đúng những photon có năng lượng bằng hiệu hai mức, để lại các vạch tối ở đúng vị trí các vạch sáng phát xạ. Đây là cách xác định thành phần hoá học của khí quyển các ngôi sao — chỉ bằng cách phân tích ánh sáng của chúng.

## Hạn chế

Mẫu Bohr chính xác đến kinh ngạc cho hiđrô và các ion một electron, nhưng thất bại với heli trở đi, không giải thích được cường độ tương đối của các vạch, và bản thân giả thiết "quỹ đạo tròn xác định" mâu thuẫn với nguyên lí bất định. Nó là một mô hình **chuyển tiếp** — đúng về ý tưởng lượng tử hoá năng lượng, sai về hình ảnh quỹ đạo, và được thay bằng cơ học lượng tử của Schrödinger năm 1926.

**Lỗi thường gặp:**
- Bỏ dấu âm của mức năng lượng khi tính hiệu — sai vì các mức đều âm và càng lên cao càng gần 0; lấy trị tuyệt đối rồi trừ sẽ cho hiệu ngược dấu và bước sóng sai.
- Cho rằng nguyên tử ở mức $n = 4$ chỉ phát ra một vạch khi về mức cơ bản — sai vì electron có thể xuống theo nhiều chặng trung gian, và trong một chùm khí thì mọi lộ trình đều xảy ra, cho đủ 6 vạch.
- Nghĩ mẫu Bohr mô tả đúng nguyên tử nhiều electron — sai vì công thức $E_n = -13{,}6/n^2$ chỉ đúng cho hệ một electron; với heli trở đi, tương tác giữa các electron làm mô hình sụp đổ.

<sub>`lesson.physics.luong-tu.quang-pho-vach-va-mau-bohr`</sub>

---

### 4. Lưỡng tính sóng hạt, de Broglie và thí nghiệm hai khe với electron
*Wave-particle duality, de Broglie and the electron double-slit experiment* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được hệ thức de Broglie để tính bước sóng của hạt vật chất
- Giải thích được vì sao tính chất sóng của vật vĩ mô không quan sát được
- Phân tích được ý nghĩa của thí nghiệm hai khe thực hiện với từng electron một

## Một câu hỏi đối xứng

Einstein đã chứng minh sóng ánh sáng có mặt hạt. Năm 1924, de Broglie đặt câu hỏi ngược đầy táo bạo trong luận án tiến sĩ: nếu sóng có mặt hạt, thì hạt có mặt sóng không?

Ông đảo ngược hệ thức của photon $p = h/\lambda$ và áp cho **mọi** hạt:

$$\lambda = \frac{h}{p} = \frac{h}{mv}$$

Giả thuyết này táo bạo tới mức hội đồng chấm luận án phải hỏi ý kiến Einstein trước khi thông qua.

## Vì sao ta không thấy bàn ghế nhiễu xạ

Hằng số $h \approx 6{,}6\times10^{-34}$ J·s cực nhỏ, nên bước sóng de Broglie của vật vĩ mô nhỏ đến vô nghĩa. Quả bóng 0,1 kg bay 10 m/s có $\lambda \approx 6{,}6\times10^{-34}$ m — nhỏ hơn bán kính hạt nhân nguyên tử (cỡ $10^{-15}$ m) khoảng $10^{18}$ lần. Muốn thấy nhiễu xạ, khe phải hẹp cỡ bước sóng, điều bất khả thi.

Ngược lại, electron tăng tốc qua 100 V có $\lambda \approx 0{,}12$ nm — đúng cỡ khoảng cách giữa các nguyên tử trong tinh thể. Tinh thể vì thế đóng vai trò cách tử nhiễu xạ tự nhiên cho electron. Davisson và Germer (1927) chiếu chùm electron vào tinh thể niken và thu được **đúng hình ảnh nhiễu xạ** như tia X — xác nhận de Broglie bằng thực nghiệm.

Ứng dụng trực tiếp: kính hiển vi điện tử. Vì giới hạn phân giải tỉ lệ với bước sóng, dùng electron ($\lambda$ cỡ picômét) thay ánh sáng ($\lambda$ cỡ 500 nm) cho độ phân giải tốt hơn hàng nghìn lần.

## Thí nghiệm hai khe với từng electron một

Đây là thí nghiệm được bình chọn là "đẹp nhất trong vật lí". Bắn electron qua hai khe, **mỗi lần một hạt**, cách nhau đủ lâu để chúng không thể tương tác với nhau.

Quan sát:

- Mỗi electron để lại **một chấm** trên màn — hành xử như hạt.
- Sau hàng vạn electron, các chấm xếp thành **vân giao thoa** — hành xử như sóng.
- Mỗi electron dường như "đi qua cả hai khe" và giao thoa với chính nó.
- Nếu đặt máy dò để biết electron qua khe nào, **vân giao thoa biến mất** ngay lập tức, chỉ còn hai vệt sáng như bắn đạn.

Điểm cuối cùng là điều gây tranh cãi nhất trong vật lí thế kỉ XX: hành vi của hệ phụ thuộc vào việc ta có đo hay không. Cách hiểu thông dụng (Copenhagen) nói rằng trước khi đo, electron không có "vị trí" xác định; hàm sóng chỉ cho **xác suất** tìm thấy nó, và cường độ vân tỉ lệ với bình phương biên độ hàm sóng.

Bài học rút ra không phải là "electron lúc là sóng lúc là hạt", mà là: electron không phải sóng cũng không phải hạt theo nghĩa cổ điển. Hai khái niệm ấy là công cụ mô tả của thế giới vĩ mô, và chúng đơn giản không đủ dùng ở cấp lượng tử.

**Lỗi thường gặp:**
- Dùng $\lambda = h/(mv)$ với vận tốc gần bằng tốc độ ánh sáng — sai vì khi đó phải dùng động lượng tương đối tính $p = \gamma m v$; công thức cổ điển cho bước sóng lớn hơn giá trị thật.
- Cho rằng vật vĩ mô không có bước sóng de Broglie — sai vì mọi vật có động lượng đều có bước sóng; chỉ là giá trị đó nhỏ tới mức không có thiết bị nào phát hiện được hiệu ứng sóng.
- Giải thích vân giao thoa electron bằng việc các electron va chạm với nhau — sai vì thí nghiệm được thực hiện với từng electron riêng lẻ cách nhau rất xa về thời gian, mà vân vẫn hình thành.

<sub>`lesson.physics.luong-tu.luong-tinh-song-hat-de-broglie`</sub>

---

### 5. Nguyên lí bất định Heisenberg
*The Heisenberg uncertainty principle* · THPT (lớp 10-12) · ap, ib · 45 phút · chuyen-sau

**Mục tiêu:**
- Phát biểu được nguyên lí bất định cho cặp vị trí - động lượng và cặp năng lượng - thời gian
- Giải thích được vì sao bất định là tính chất nội tại chứ không phải hạn chế của dụng cụ đo
- Vận dụng được nguyên lí bất định để ước lượng năng lượng tối thiểu của hạt bị giam

## Không phải lỗi của dụng cụ

Nguyên lí bất định thường bị diễn giải sai thành: "đo vị trí thì làm nhiễu động lượng, nên ta không biết chính xác được". Cách hiểu ấy gợi ý rằng hạt **thực sự có** vị trí và động lượng xác định, chỉ là ta vụng về.

Cách hiểu đúng: bất định là **tính chất nội tại**. Một sóng có bước sóng hoàn toàn xác định phải trải vô hạn trong không gian; muốn định xứ nó vào một vùng hẹp thì phải chồng chất nhiều bước sóng khác nhau, tức động lượng không còn xác định. Vị trí và động lượng đơn giản **không cùng tồn tại** ở dạng xác định — đây là đặc điểm của mọi sóng, kể cả sóng âm, chứ không riêng gì thế giới lượng tử.

$$\Delta x\,\Delta p_x \ge \frac{\hbar}{2}, \qquad \hbar = \frac{h}{2\pi}$$

## Ba hệ quả có thể kiểm chứng

**Electron không thể ở trong hạt nhân.** Giam electron vào $\Delta x \approx 10^{-15}$ m đòi hỏi $\Delta p \ge \hbar/(2\Delta x)$, cho động năng cỡ hàng chục MeV — lớn hơn nhiều so với năng lượng liên kết hạt nhân. Vậy electron trong phóng xạ beta không nằm sẵn trong hạt nhân mà được sinh ra lúc phân rã.

**Năng lượng điểm không.** Hạt bị giam trong hố thế không thể đứng yên, vì $v = 0$ chính xác nghĩa là $\Delta p = 0$, kéo theo $\Delta x$ vô hạn — mâu thuẫn với việc nó bị giam. Mọi hạt bị giam đều có động năng tối thiểu khác 0. Đây là lí do heli lỏng không đông đặc ở áp suất thường dù nhiệt độ về 0 K.

**Bề rộng vạch quang phổ.** Trạng thái kích thích sống trong thời gian $\Delta t$ hữu hạn, nên năng lượng của nó bất định $\Delta E \ge \hbar/(2\Delta t)$. Vạch phổ vì thế không bao giờ mảnh tuyệt đối. Trạng thái càng ngắn hạn, vạch càng rộng — quan hệ này được đo trực tiếp trong vật lí hạt để suy ra thời gian sống của các hạt cộng hưởng.

## Liên hệ với thí nghiệm hai khe

Nguyên lí bất định giải thích luôn vì sao đo được "electron qua khe nào" thì vân giao thoa biến mất: xác định vị trí electron ở mức khe (thu hẹp $\Delta x$) buộc $\Delta p$ phải tăng, và độ bất định động lượng ngang ấy đủ lớn để xoá nhoè hệ vân. Hai điều mà thí nghiệm cho thấy — thông tin đường đi và hình ảnh giao thoa — là hai mặt loại trừ nhau, đúng như Bohr gọi là **tính bổ sung**.

## Ranh giới cổ điển

Vì $\hbar \approx 1{,}05\times10^{-34}$ J·s cực nhỏ, với vật vĩ mô các độ bất định nằm dưới mọi ngưỡng đo được. Bi-a lăn trên bàn có $\Delta x$ và $\Delta p$ đồng thời nhỏ tuỳ ý về mặt thực tiễn. Cơ học Newton vì thế vẫn đúng trong phạm vi của nó — mọi lí thuyết mới đều phải tái tạo được lí thuyết cũ ở miền nó đã kiểm chứng.

**Lỗi thường gặp:**
- Giải thích bất định là do dụng cụ đo làm nhiễu hệ — sai vì bất định vẫn tồn tại với mọi dụng cụ hoàn hảo; nó phản ánh việc vị trí và động lượng không đồng thời có giá trị xác định, giống như một xung sóng ngắn không có tần số duy nhất.
- Áp dụng nguyên lí bất định cho cặp đại lượng bất kì, ví dụ vị trí theo phương x và động lượng theo phương y — sai vì hệ thức chỉ ràng buộc các cặp liên hợp cùng phương; $\Delta x$ và $\Delta p_y$ có thể nhỏ đồng thời.
- Kết luận hạt bị giam có thể đứng yên hoàn toàn ở nhiệt độ 0 K — sai vì $v = 0$ chính xác đòi hỏi $\Delta p = 0$ và kéo theo $\Delta x$ vô hạn, mâu thuẫn với việc hạt bị giam; luôn tồn tại năng lượng điểm không.

<sub>`lesson.physics.luong-tu.nguyen-li-bat-dinh`</sub>

---

## Unit 9: Fluids (AP Physics 1 Unit 8 theo CED 2024 / CIE 9702 Topic 4 / IB Option B.3 chương trình cũ)

### 1. Áp suất chất lưu, áp suất theo độ sâu và nguyên lí Pascal
*Fluid pressure, pressure with depth and Pascal's principle* · THPT (lớp 10-12) · ap, a-level · 45 phút · co-ban

**Mục tiêu:**
- Tính được áp suất tuyệt đối và áp suất dư tại một điểm trong lòng chất lỏng
- Giải thích được vì sao áp suất chỉ phụ thuộc độ sâu mà không phụ thuộc hình dạng bình
- Vận dụng được nguyên lí Pascal cho máy nén thuỷ lực

## Áp suất chỉ phụ thuộc độ sâu

Xét một cột chất lỏng tiết diện $A$, cao $h$. Trọng lượng cột là $\rho A h g$, chia cho diện tích đáy:

$$P = P_0 + \rho g h$$

Điều đáng ngạc nhiên: $A$ triệt tiêu. Áp suất ở đáy một hồ bơi rộng và ở đáy một ống nghiệm hẹp là **như nhau** nếu cùng độ sâu. Đây gọi là nghịch lí thuỷ tĩnh, và nó có nghĩa là hình dạng bình không hề ảnh hưởng — chỉ chiều cao cột chất lỏng mới quan trọng.

Hệ quả thực tế: hai bình thông nhau có mực chất lỏng ngang nhau; đập nước phải xây dày ở chân chứ không phải vì hồ rộng mà vì hồ sâu.

## Áp suất là vô hướng

Tại một điểm trong chất lưu đứng yên, áp suất tác dụng như nhau theo mọi hướng. Đó là lí do thợ lặn bị ép đều từ mọi phía, và vì sao ta viết $P$ không có mũi tên. Chỉ **lực** do áp suất gây ra mới là vectơ, và nó luôn vuông góc bề mặt.

## Nguyên lí Pascal và máy thuỷ lực

Ép pit-tông nhỏ diện tích $A_1$ bằng lực $F_1$ tạo áp suất $P = F_1/A_1$. Áp suất này truyền nguyên vẹn tới pit-tông lớn:

$$\frac{F_1}{A_1} = \frac{F_2}{A_2} \Rightarrow F_2 = F_1\frac{A_2}{A_1}$$

Diện tích lớn gấp 100 lần cho lực lớn gấp 100 lần. Nhưng **không có bữa trưa miễn phí**: chất lỏng không nén được nên thể tích dịch chuyển bằng nhau, $A_1d_1 = A_2d_2$, tức pit-tông lớn chỉ đi được quãng đường bằng 1 phần 100. Công vào bằng công ra, đúng như định luật bảo toàn năng lượng đòi hỏi.

## Đơn vị hay gặp

$1\ \mathrm{atm} = 1{,}013\times10^{5}$ Pa $= 760$ mmHg. Cứ xuống sâu 10 m trong nước, áp suất tăng thêm khoảng 1 atm — con số đáng nhớ cho mọi bài về lặn.

**Lỗi thường gặp:**
- Cho rằng bình rộng hơn thì áp suất đáy lớn hơn. Diện tích triệt tiêu trong phép chia trọng lượng cho diện tích; chỉ chiều cao cột chất lỏng và khối lượng riêng mới quyết định áp suất.
- Nhầm áp suất dư với áp suất tuyệt đối trong bài toán khí. Phương trình khí lí tưởng đòi hỏi áp suất tuyệt đối $P_0 + \rho gh$; dùng áp suất dư sẽ cho kết quả sai lệch cả một atmosphere.
- Nghĩ máy thuỷ lực tạo ra năng lượng vì lực ra lớn hơn lực vào. Quãng đường dịch chuyển giảm đúng theo tỉ lệ ngược lại nên công vào bằng công ra; máy chỉ đổi lực lấy quãng đường.

<sub>`lesson.physics.chat-luu-intl.ap-suat-do-sau-va-nguyen-li-pascal`</sub>

---

### 2. Lực đẩy Archimedes và điều kiện nổi
*Archimedes' principle and flotation* · THPT (lớp 10-12) · ap, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Chứng minh được lực đẩy Archimedes từ sự chênh lệch áp suất theo độ sâu
- Xác định được điều kiện nổi, lơ lửng và chìm dựa vào khối lượng riêng
- Tính được trọng lượng biểu kiến của vật nhúng trong chất lưu

## Lực đẩy đến từ đâu

Xét một khối hộp nhúng trong chất lỏng, mặt trên ở độ sâu $h_1$, mặt dưới ở $h_2 > h_1$. Áp suất tăng theo độ sâu nên lực đẩy lên mặt dưới **lớn hơn** lực ép xuống mặt trên:

$$F_A = (P_2 - P_1)A = \rho g(h_2 - h_1)A = \rho g V$$

Vậy lực đẩy Archimedes không phải một lực bí ẩn; nó chỉ là hệ quả trực tiếp của việc áp suất tăng theo độ sâu. Các lực bên hông triệt tiêu nhau nên không đóng góp.

$$F_A = \rho_{\text{lưu}}\, V_{\text{chìm}}\, g$$

Chú ý ba điểm: dùng khối lượng riêng của **chất lưu** chứ không phải của vật; dùng thể tích **phần chìm** chứ không phải toàn bộ vật; lực này không phụ thuộc độ sâu (miễn vật ngập hoàn toàn) và không phụ thuộc chất liệu vật.

## Ba trạng thái

So sánh $\rho_{\text{vật}}$ với $\rho_{\text{lưu}}$ khi vật ngập hoàn toàn:

| Quan hệ | Kết quả |
|---|---|
| $\rho_{v} > \rho_{l}$ | Chìm xuống đáy |
| $\rho_{v} = \rho_{l}$ | Lơ lửng ở mọi độ sâu |
| $\rho_{v} < \rho_{l}$ | Nổi lên, cân bằng khi chìm một phần |

Với vật nổi: $\dfrac{V_{\text{chìm}}}{V} = \dfrac{\rho_v}{\rho_l}$. Nước đá có $\rho = 917\ \mathrm{kg/m^{3}}$ trong nước biển $1025\ \mathrm{kg/m^{3}}$ nên chỉ nhô lên khoảng 11 phần trăm — phần chìm của tảng băng trôi.

## Vì sao tàu thép nổi

Thép có $\rho = 7800\ \mathrm{kg/m^{3}}$, nặng hơn nước gần tám lần. Nhưng con tàu là **thép cộng với khoang rỗng chứa không khí**, nên khối lượng riêng trung bình của cả con tàu nhỏ hơn nước. Thủng khoang, nước tràn vào thay chỗ không khí, khối lượng riêng trung bình vượt ngưỡng, tàu chìm.

## Đo khối lượng riêng bằng cân thuỷ tĩnh

Cân vật trong không khí được $W$, cân trong nước được $W'$. Khi đó $F_A = W - W'$ và

$$\rho_{\text{vật}} = \frac{W}{W - W'}\rho_{\text{nước}}$$

Truyền thuyết kể Archimedes dùng đúng ý tưởng này để phát hiện vương miện pha bạc.

**Lỗi thường gặp:**
- Dùng khối lượng riêng của vật trong công thức $F_A = \rho V g$. Lực đẩy bằng trọng lượng chất lưu bị chiếm chỗ, nên phải dùng $\rho$ của chất lưu; nhầm lẫn này khiến mọi vật đều lơ lửng.
- Lấy toàn bộ thể tích vật khi vật chỉ chìm một phần. Chỉ phần ngập trong chất lưu mới chiếm chỗ; với tảng băng nổi, dùng cả thể tích sẽ cho lực đẩy lớn hơn trọng lượng và kết luận sai rằng băng bay lên.
- Cho rằng lực đẩy Archimedes tăng theo độ sâu vì áp suất tăng theo độ sâu. Áp suất ở cả mặt trên lẫn mặt dưới đều tăng cùng một lượng, nên **hiệu** áp suất giữ nguyên và lực đẩy không đổi khi vật đã ngập hoàn toàn.

<sub>`lesson.physics.chat-luu-intl.luc-day-archimedes-va-su-noi`</sub>

---

### 3. Phương trình liên tục, phương trình Bernoulli và ứng dụng
*The continuity equation, Bernoulli's equation and applications* · THPT (lớp 10-12) · ap · 50 phút · nang-cao

**Mục tiêu:**
- Vận dụng được phương trình liên tục để liên hệ tốc độ dòng với tiết diện ống
- Giải thích được phương trình Bernoulli như một dạng của định luật bảo toàn năng lượng
- Phân tích được các ứng dụng thực tế như ống Venturi, lực nâng cánh máy bay và định luật Torricelli

## Bảo toàn khối lượng: bịt vòi thì nước bắn xa

Chất lưu không nén được chảy trong ống: lượng đi vào bằng lượng đi ra.

$$A_1v_1 = A_2v_2$$

Bóp đầu vòi làm $A$ giảm nên $v$ tăng — nguyên lí này ai cũng từng dùng khi tưới cây.

## Bảo toàn năng lượng: phương trình Bernoulli

Áp dụng định lí công - động năng cho một khối chất lưu di chuyển dọc ống, ta được

$$P + \tfrac12\rho v^{2} + \rho g y = \text{hằng số}$$

Ba số hạng lần lượt là áp suất tĩnh, "áp suất động" (mật độ động năng) và mật độ thế năng. Toàn bộ phương trình chỉ là bảo toàn năng lượng tính trên một đơn vị thể tích.

## Bốn ứng dụng kinh điển

1. **Ống Venturi**: chỗ thắt có $v$ lớn nên $P$ nhỏ; đo chênh lệch áp suất suy ra lưu lượng.
2. **Định luật Torricelli**: lỗ thủng ở độ sâu $h$ dưới mặt thoáng cho $v = \sqrt{2gh}$ — đúng bằng tốc độ vật rơi tự do từ độ cao $h$, vì cả hai đều là chuyển hoá thế năng thành động năng.
3. **Cánh máy bay**: dòng khí phía trên đi nhanh hơn nên áp suất nhỏ hơn, tạo lực nâng. (Giải thích đầy đủ còn cần đến sự lệch dòng khí xuống dưới theo định luật III Newton.)
4. **Mái tôn bị tốc trong bão**: gió thổi nhanh phía trên mái làm áp suất giảm, không khí tĩnh bên trong nhà đẩy mái bật lên.

## Giới hạn nghiêm ngặt

Bernoulli đòi hỏi chất lưu **lí tưởng**: không nhớt, không nén được, chảy ổn định (chảy tầng), và áp dụng **dọc theo một đường dòng**. Với dầu nhớt trong ống dài, phải dùng định luật Hagen - Poiseuille; với dòng chảy rối (số Reynolds lớn), phương trình mất hiệu lực hoàn toàn. Đây là lí do không thể dùng Bernoulli tính lưu lượng nước máy qua hàng trăm mét ống mà bỏ qua tổn thất áp suất.

## Phạm vi chương trình

Phương trình liên tục và Bernoulli nằm trong AP Physics 1 Unit 8 (CED 2024; trước đó là AP Physics 2) và trong IB Option B.3 của chương trình cũ. Syllabus CIE 9702 và IB 2023 hiện hành **không** yêu cầu phần này, nên với hai chương trình đó hãy coi đây là nội dung mở rộng.

**Lỗi thường gặp:**
- Nghĩ chỗ ống hẹp có áp suất lớn hơn vì chất lưu bị ép lại. Bernoulli cho kết quả ngược: tốc độ tăng thì áp suất tĩnh giảm, vì tổng năng lượng trên đơn vị thể tích không đổi.
- Áp dụng Bernoulli cho chất lưu nhớt trong ống dài hoặc cho dòng chảy rối. Phương trình được dẫn ra với giả thiết không có tiêu tán năng lượng; ống dẫn dầu hay đường ống dài phải dùng công thức Poiseuille có kể tới độ nhớt.
- Quên số hạng $\rho gy$ khi ống không nằm ngang. Với vòi nước ở tầng cao hay bể chứa trên mái, chênh lệch độ cao đóng góp đáng kể và bỏ nó đi làm sai hoàn toàn áp suất tính được.

<sub>`lesson.physics.chat-luu-intl.phuong-trinh-lien-tuc-va-bernoulli`</sub>

---

## Unit 9: Vật lí hạt nhân - Nuclear Physics

### 1. Cấu trúc hạt nhân và lực hạt nhân mạnh
*Nuclear structure and the strong nuclear force* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được số proton, nơtron và kí hiệu hạt nhân từ dữ kiện cho trước
- Giải thích được vì sao cần một lực mới ngoài lực điện và lực hấp dẫn để hạt nhân tồn tại
- Phân tích được các đặc điểm của lực hạt nhân mạnh và ý nghĩa của tỉ lệ nơtron trên proton

## Kí hiệu và những con số nền

Hạt nhân kí hiệu $^A_ZX$ với $Z$ là số proton (quyết định nguyên tố), $A$ là số khối, và $N = A - Z$ là số nơtron. Proton và nơtron gọi chung là **nucleon**.

Bán kính hạt nhân gần đúng:

$$R = R_0 A^{1/3}, \qquad R_0 \approx 1{,}2\ \text{fm}$$

Công thức này chứa một thông tin quan trọng: vì $R^3 \propto A$ nên **mật độ hạt nhân là hằng số** với mọi nguyên tố, cỡ $2{,}3\times10^{17}$ kg/m³. Nucleon xếp sát nhau như những viên bi trong túi chứ không nén lại được. Một thìa cà phê vật chất hạt nhân nặng khoảng một tỉ tấn — chính là mật độ của sao nơtron.

So sánh kích thước: hạt nhân nhỏ hơn nguyên tử khoảng $10^{5}$ lần. Nếu phóng to nguyên tử bằng một sân vận động, hạt nhân chỉ là hạt đậu ở giữa sân.

## Vì sao phải có lực thứ ba

Trong hạt nhân heli, hai proton cách nhau khoảng 2 fm đẩy nhau bằng lực Coulomb cỡ 58 N — khổng lồ ở thang hạt. Lực hấp dẫn giữa chúng nhỏ hơn lực điện khoảng $10^{36}$ lần, hoàn toàn vô nghĩa. Vậy nếu chỉ có hai lực đã biết, mọi hạt nhân phải nổ tung tức thì.

Tồn tại của hạt nhân buộc phải có một lực hút mới. Đặc điểm của **lực hạt nhân mạnh**:

- **Rất mạnh:** khoảng 100 lần lực điện ở cùng khoảng cách.
- **Tầm tác dụng cực ngắn:** chỉ hiệu quả trong vài fm, gần như biến mất ngoài khoảng đó. Đây là điểm khác biệt căn bản với lực điện và lực hấp dẫn vốn có tầm vô hạn.
- **Không phụ thuộc điện tích:** lực giữa p-p, p-n, n-n như nhau.
- **Bão hoà:** mỗi nucleon chỉ tương tác với các nucleon lân cận, không phải với tất cả.

## Đường bền vững

Tầm ngắn của lực mạnh giải thích hình dạng của đồ thị $N$ theo $Z$:

- Hạt nhân nhẹ ($Z < 20$) bền khi $N \approx Z$.
- Hạt nhân nặng cần **thừa nơtron** ($N/Z$ tới khoảng 1,5). Lí do: lực đẩy Coulomb tác dụng giữa **mọi cặp** proton dù xa hay gần, nên nó tăng theo $Z^2$; còn lực hút mạnh chỉ tác dụng với hàng xóm nên tăng gần như tuyến tính theo $A$. Cần thêm nơtron để bổ sung lực hút mà không thêm lực đẩy.
- Vượt $Z = 83$ (bitmut), không hạt nhân nào bền tuyệt đối: lực đẩy Coulomb thắng hẳn, và mọi nguyên tố nặng hơn đều phóng xạ.

Đây là toàn bộ lí do vật lí khiến bảng tuần hoàn có điểm dừng.

**Lỗi thường gặp:**
- Cho rằng hạt nhân nặng có mật độ lớn hơn hạt nhân nhẹ — sai vì thể tích tỉ lệ với $A$ đúng như khối lượng, nên mật độ hạt nhân như nhau ở mọi nguyên tố.
- Nghĩ lực hạt nhân mạnh giữ được hạt nhân lớn tuỳ ý — sai vì lực này có tầm rất ngắn nên chỉ tác dụng với nucleon lân cận, trong khi lực đẩy Coulomb cộng dồn giữa mọi cặp proton và cuối cùng thắng thế ở $Z > 83$.
- Nhầm số khối $A$ với số proton $Z$ khi viết phương trình phản ứng — sai vì $A$ đếm tổng số nucleon còn $Z$ đếm điện tích; nhầm lẫn làm sai cả hai định luật bảo toàn dùng để cân bằng phản ứng.

<sub>`lesson.physics.hat-nhan.cau-truc-hat-nhan-va-luc-manh`</sub>

---

### 2. Độ hụt khối và năng lượng liên kết riêng
*Mass defect and binding energy per nucleon* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Tính được độ hụt khối và năng lượng liên kết của một hạt nhân
- Giải thích được vì sao năng lượng liên kết riêng mới là thước đo độ bền vững
- Đọc được đồ thị năng lượng liên kết riêng theo số khối để dự đoán phản ứng toả năng lượng

## Một sự thật gây sốc

Cân khối lượng hạt nhân heli-4 và so với tổng khối lượng 2 proton + 2 nơtron riêng lẻ: hạt nhân **nhẹ hơn**. Phần chênh lệch $\Delta m$ gọi là độ hụt khối, và nó không hề nhỏ theo thang hạt nhân.

Khối lượng biến đi đâu? Theo Einstein, khối lượng và năng lượng là hai mặt của cùng một đại lượng:

$$W_{lk} = \Delta m\,c^2$$

Để tách hạt nhân thành các nucleon riêng, ta phải cung cấp đúng $W_{lk}$; ngược lại khi các nucleon kết hợp, đúng lượng năng lượng đó được giải phóng và khối lượng hệ giảm tương ứng.

Đơn vị làm việc thuận tiện: $1u = 931{,}5$ MeV/c². Nhờ hằng số này, chỉ cần lấy độ hụt khối theo u rồi nhân 931,5 là ra năng lượng theo MeV, không phải động tới $c^2$.

## Vì sao phải chia cho A

Urani có $W_{lk} \approx 1800$ MeV, sắt chỉ khoảng 492 MeV. Nếu so bằng năng lượng liên kết tổng thì urani "bền hơn" — kết luận sai hoàn toàn.

Đại lượng đúng là **năng lượng liên kết riêng**:

$$\frac{W_{lk}}{A}$$

Nó đo mức năng lượng cần để bứt **một** nucleon ra, tức độ chặt của liên kết trung bình. Với urani, giá trị này là 7,6 MeV/nucleon; với sắt là 8,8 MeV/nucleon. Sắt bền hơn nhiều.

## Đọc đồ thị $W_{lk}/A$ theo $A$

Đây là một trong những đồ thị quan trọng nhất của vật lí:

- Tăng nhanh từ $A = 1$ tới khoảng $A = 20$.
- Đạt **cực đại khoảng 8,8 MeV/nucleon quanh $^{56}$Fe** và $^{62}$Ni.
- Giảm dần và đều về khoảng 7,6 MeV/nucleon ở $A = 238$.

Hình dạng "đỉnh núi" này quyết định toàn bộ năng lượng học hạt nhân. Mọi quá trình đi **lên phía đỉnh** đều toả năng lượng:

- **Nhiệt hạch** — hạt nhân nhẹ hợp lại, leo dốc bên trái. Đây là nguồn năng lượng của các ngôi sao.
- **Phân hạch** — hạt nhân nặng vỡ ra, trượt xuống từ bên phải về phía đỉnh. Đây là nguồn năng lượng của nhà máy điện hạt nhân.

Hai quá trình có vẻ trái ngược nhau nhưng cùng tuân theo một nguyên tắc duy nhất: hệ tiến về trạng thái có năng lượng liên kết riêng lớn hơn.

Hệ quả thiên văn sâu sắc: sắt là **điểm cuối** của phản ứng nhiệt hạch trong sao. Khi lõi sao khối lượng lớn đã hoá thành sắt, không phản ứng nào còn toả năng lượng nữa, áp suất bức xạ sụp đổ, và ngôi sao nổ thành siêu tân tinh. Mọi nguyên tố nặng hơn sắt trong cơ thể chúng ta đều được tạo ra trong những vụ nổ ấy.

**Lỗi thường gặp:**
- So sánh độ bền vững bằng năng lượng liên kết tổng thay vì năng lượng liên kết riêng — sai vì hạt nhân càng nhiều nucleon thì tổng càng lớn một cách hiển nhiên; chỉ giá trị trung bình trên mỗi nucleon mới đo được độ chặt của liên kết.
- Dùng khối lượng nguyên tử thay cho khối lượng hạt nhân mà không trừ khối lượng electron — sai vì với hạt nhân nặng, khối lượng của hàng chục electron đủ làm sai lệch đáng kể độ hụt khối.
- Cho rằng độ hụt khối là do phép đo thiếu chính xác — sai vì đó là hiệu ứng vật lí thật: một phần khối lượng đã chuyển thành năng lượng liên kết được giải phóng khi hạt nhân hình thành.

<sub>`lesson.physics.hat-nhan.do-hut-khoi-va-nang-luong-lien-ket`</sub>

---

### 3. Phóng xạ và định luật phân rã
*Radioactivity and the decay law* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Viết được phương trình các loại phân rã alpha, beta trừ, beta cộng và gamma
- Vận dụng được định luật phóng xạ để tính số hạt còn lại, độ phóng xạ và tuổi mẫu vật
- Giải thích được tính ngẫu nhiên và tính tự phát của hiện tượng phóng xạ

## Ba loại tia và ba cơ chế

**Alpha** ($^4_2$He): hạt nhân quá nặng đẩy ra một cụm 4 nucleon rất bền. $Z$ giảm 2, $A$ giảm 4. Tia alpha ion hoá rất mạnh nhưng chỉ đi được vài cm trong không khí, một tờ giấy chặn được.

**Beta trừ** ($^0_{-1}e$): một nơtron biến thành proton kèm electron và phản nơtrinô. $Z$ tăng 1, $A$ không đổi. Xảy ra với hạt nhân **thừa nơtron**.

**Beta cộng** ($^0_{+1}e$): một proton biến thành nơtron kèm pozitron và nơtrinô. $Z$ giảm 1, $A$ không đổi. Xảy ra với hạt nhân **thừa proton**.

**Gamma:** hạt nhân con sinh ra ở trạng thái kích thích, trở về mức cơ bản bằng cách phát photon năng lượng cao. Không đổi $Z$ lẫn $A$, nên gamma luôn **đi kèm** phân rã khác chứ không đứng riêng.

Mọi phương trình phân rã đều phải bảo toàn số khối $A$ và điện tích $Z$ — hai định luật này đủ để cân bằng bất kì phản ứng nào.

## Định luật phân rã

Điều then chốt: không thể dự đoán **hạt nhân nào** sẽ phân rã và **khi nào**. Mỗi hạt nhân có cùng một xác suất phân rã trong mỗi giây, độc lập với tuổi của nó — hạt nhân không "già đi". Từ giả thiết thống kê ấy:

$$\frac{dN}{dt} = -\lambda N \;\Longrightarrow\; N = N_0e^{-\lambda t} = N_0 2^{-t/T}$$

với $T = \ln 2/\lambda$. Độ phóng xạ $H = \lambda N$ suy giảm theo đúng quy luật đó.

Dạng $2^{-t/T}$ tiện cho tính nhẩm: sau $n$ chu kì bán rã còn $1/2^n$. Sau 10 chu kì còn chưa tới 0,1%.

Một đặc điểm khiến phóng xạ trở thành đồng hồ tin cậy: $T$ **không phụ thuộc** nhiệt độ, áp suất, trạng thái hoá học — vì đó là quá trình của hạt nhân, hoàn toàn cách li với lớp vỏ electron nơi mọi tác động bên ngoài dừng lại.

## Định tuổi

**Cacbon-14** ($T = 5730$ năm): sinh vật sống liên tục trao đổi cacbon với môi trường nên giữ tỉ lệ $^{14}$C/$^{12}$C không đổi. Khi chết, quá trình trao đổi dừng và $^{14}$C bắt đầu giảm. Đo tỉ lệ còn lại cho tuổi mẫu vật, dùng được tới khoảng 50 000 năm (sau đó lượng còn lại quá nhỏ để đo chính xác).

**Urani-chì** ($T = 4{,}5$ tỉ năm): dùng cho đá và khoáng vật, cho tuổi Trái Đất khoảng 4,54 tỉ năm.

Nguyên tắc chung khi chọn đồng vị định tuổi: chu kì bán rã phải **cùng cỡ** với khoảng thời gian cần đo. Quá ngắn thì không còn gì để đo, quá dài thì lượng giảm không đáng kể so với sai số.

**Lỗi thường gặp:**
- Cho rằng sau hai chu kì bán rã thì mẫu phân rã hết — sai vì mỗi chu kì chỉ làm giảm một nửa lượng CÒN LẠI, nên sau hai chu kì vẫn còn 25%; hàm mũ không bao giờ chạm 0.
- Nghĩ có thể tăng tốc phân rã bằng cách nung nóng hoặc nén mẫu — sai vì phân rã là quá trình của hạt nhân, cách li hoàn toàn với năng lượng nhiệt và hoá học vốn chỉ tác động tới lớp vỏ electron.
- Viết phương trình phân rã beta trừ với $A$ thay đổi — sai vì nơtron chuyển thành proton nên tổng số nucleon giữ nguyên; chỉ điện tích $Z$ tăng thêm một đơn vị.

<sub>`lesson.physics.hat-nhan.phong-xa-va-dinh-luat-phan-ra`</sub>

---

### 4. Phân hạch, nhiệt hạch và an toàn bức xạ
*Fission, fusion and radiation safety* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Tính được năng lượng toả ra của phản ứng phân hạch và nhiệt hạch từ độ hụt khối
- Giải thích được điều kiện duy trì phản ứng dây chuyền và vai trò của chất làm chậm, thanh điều khiển
- Phân tích được vì sao nhiệt hạch có kiểm soát khó thực hiện và các nguyên tắc an toàn bức xạ

## Phân hạch

Hạt nhân $^{235}$U hấp thụ một nơtron chậm, trở nên không bền và vỡ thành hai mảnh trung bình kèm 2-3 nơtron:

$$^{235}\text{U} + n \to ^{95}\text{Y} + ^{138}\text{I} + 3n + \sim200\ \text{MeV}$$

Con số 200 MeV cho mỗi phân hạch cần được đặt trong so sánh: đốt một phân tử cacbon giải phóng khoảng 4 eV. Vậy 1 kg urani cho năng lượng bằng khoảng 3 triệu kg than.

Những nơtron sinh ra có thể gây phân hạch tiếp, tạo **phản ứng dây chuyền**. Hai điều kiện kiểm soát:

- **Khối lượng tới hạn:** khối nhiên liệu phải đủ lớn để nơtron không thoát ra ngoài trước khi kịp gặp hạt nhân khác.
- **Hệ số nhân $k$:** lò phản ứng vận hành ở $k = 1$ chính xác, gọi là trạng thái tới hạn.

Hai bộ phận điều khiển điều đó: **chất làm chậm** (nước, graphit) hãm nơtron nhanh xuống tốc độ nhiệt vì $^{235}$U hấp thụ nơtron chậm hiệu quả hơn nhiều; và **thanh điều khiển** (bo, cadimi) hút bớt nơtron thừa, đẩy vào sâu thì $k$ giảm.

Nhược điểm lớn nhất là chất thải phóng xạ: các mảnh phân hạch thừa nơtron nên phóng xạ beta mạnh, một số đồng vị có chu kì bán rã hàng nghìn năm.

## Nhiệt hạch

$$^2_1\text{H} + ^3_1\text{H} \to ^4_2\text{He} + n + 17{,}6\ \text{MeV}$$

Tính trên mỗi nucleon, nhiệt hạch toả 3,5 MeV còn phân hạch chỉ 0,85 MeV, tức **lớn hơn khoảng bốn lần**, nhiên liệu (đơteri trong nước biển) gần như vô tận, và sản phẩm heli không phóng xạ.

Vậy vì sao chưa có nhà máy nhiệt hạch? Rào cản là **hàng rào Coulomb**: hai hạt nhân đều tích điện dương, phải lại gần nhau tới cỡ 1 fm mới cảm nhận được lực hút mạnh. Điều đó đòi hỏi nhiệt độ trên 100 triệu độ, ở đó vật chất là plasma và không vật liệu nào chứa nổi. Hai hướng giải quyết: giam bằng từ trường (tokamak, dự án ITER) và giam bằng quán tính (nén viên nhiên liệu bằng laser).

Mặt Trời làm được ở nhiệt độ "chỉ" 15 triệu độ nhờ hai lợi thế mà ta không có: áp suất khổng lồ do khối lượng bản thân, và hiệu ứng đường ngầm lượng tử cho phép một tỉ lệ nhỏ hạt vượt rào dù thiếu năng lượng.

## An toàn bức xạ

Ba nguyên tắc thực hành, xếp theo hiệu quả:

1. **Thời gian** — giảm thời gian tiếp xúc, liều tỉ lệ thuận với nó.
2. **Khoảng cách** — liều giảm theo $1/r^2$, nên lùi ra xa gấp đôi đã giảm bốn lần.
3. **Che chắn** — giấy chặn alpha, nhôm vài milimét chặn beta, chì hoặc bê tông dày mới chặn được gamma và nơtron.

Nguy hiểm phụ thuộc đường nhiễm: alpha vô hại từ bên ngoài (da chặn được) nhưng cực nguy hiểm khi hít hoặc nuốt phải, vì toàn bộ năng lượng ion hoá được nhả ra trong một thể tích mô rất nhỏ.

**Lỗi thường gặp:**
- Cho rằng lò phản ứng hạt nhân có thể nổ như bom nguyên tử — sai vì nhiên liệu lò chỉ làm giàu vài phần trăm $^{235}$U trong khi bom cần trên 90%; ở nồng độ thấp không thể đạt được hệ số nhân đủ lớn để phản ứng bùng nổ.
- Nghĩ nhiệt hạch dễ thực hiện hơn phân hạch vì dùng hạt nhân nhẹ — sai vì phân hạch khởi động bằng nơtron trung hoà không gặp rào Coulomb, còn nhiệt hạch phải đưa hai hạt nhân tích điện dương lại gần nhau, đòi hỏi nhiệt độ trên trăm triệu độ.
- Coi tia alpha là ít nguy hiểm nhất trong mọi hoàn cảnh — sai vì khả năng đâm xuyên yếu chỉ có nghĩa khi nguồn ở ngoài cơ thể; nuốt hoặc hít phải chất phát alpha thì toàn bộ năng lượng ion hoá tập trung vào một vùng mô rất nhỏ.

<sub>`lesson.physics.hat-nhan.phan-hach-nhiet-hach-va-an-toan`</sub>

---

## Unit 1: Cơ học giải tích

### 1. Nguyên lí tác dụng dừng và hàm Lagrange
*Stationary action principle and the Lagrangian* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Phát biểu được nguyên lí Hamilton dưới dạng biến phân của tác dụng
- Chứng minh được phương trình Euler - Lagrange từ điều kiện tác dụng dừng
- Vận dụng được hình thức Lagrange để lập phương trình chuyển động cho hệ có ràng buộc đơn giản

## Vì sao cần một nguyên lí thay cho lực

Với hệ có ràng buộc — hạt trượt trên mặt cong, con lắc kép, vật lăn không trượt — viết $\vec F = m\vec a$ buộc ta đưa vào các phản lực ràng buộc chưa biết rồi lại phải khử chúng. Cơ học giải tích đổi hướng: mô tả toàn bộ hệ bằng **một hàm vô hướng** duy nhất, không cần vẽ lực.

## Hàm Lagrange và tác dụng

Với hệ holonom và lực thế, đặt $L(q,\dot q,t)=T-U$. Tác dụng của một quỹ đạo thử $q(t)$ nối hai cấu hình cố định là

$$S[q]=\int_{t_1}^{t_2} L(q,\dot q,t)\,dt$$

**Nguyên lí Hamilton**: quỹ đạo thực làm $S$ *dừng*, tức $\delta S=0$ với mọi biến phân triệt tiêu ở hai đầu mút.

## Từ $\delta S = 0$ ra phương trình chuyển động

Biến phân $S$, tích phân từng phần số hạng chứa $\delta\dot q$ và dùng $\delta q(t_1)=\delta q(t_2)=0$:

$$\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q_k}-\frac{d}{dt}\frac{\partial L}{\partial\dot q_k}\right)\delta q_k\,dt=0$$

Vì các $\delta q_k$ độc lập và tùy ý, mỗi ngoặc phải triệt tiêu:

$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_k}-\frac{\partial L}{\partial q_k}=0,\qquad k=1,\dots,n$$

## Khi nào dùng được, khi nào không

Dạng $L=T-U$ đòi hỏi lực rút ra được từ thế, kể cả thế phụ thuộc vận tốc như lực Lorentz. Ma sát nhớt và lực cản không có thế: khi đó phải bổ sung lực suy rộng hoặc hàm tiêu tán Rayleigh. Cũng lưu ý nguyên lí là **dừng**, không phải "cực tiểu": trên khoảng thời gian dài quỹ đạo thực có thể chỉ là điểm yên ngựa của $S$.

**Lỗi thường gặp:**
- Viết $L=T+U$. Sai vì phép biến phân chỉ tái tạo được $m\ddot q=-\partial U/\partial q$ khi thế năng vào với dấu trừ; lấy dấu cộng sẽ cho lực cùng chiều gradient thế, tức mô tả một hệ vật lí khác hẳn.
- Tính động năng trong hệ đang quay hoặc đang tịnh tiến có gia tốc mà quên phần vận tốc kéo theo. Động năng trong $L$ phải đo trong hệ quán tính, nếu không phương trình thu được thiếu hẳn các lực quán tính.
- Hiểu nguyên lí là "tác dụng cực tiểu". Với khoảng thời gian vượt quá điểm liên hợp, quỹ đạo thực chỉ là điểm dừng dạng yên ngựa, nên mọi lập luận dựa vào tính cực tiểu đều có thể dẫn tới kết luận sai.

<sub>`lesson.physics.co-hoc-giai-tich.nguyen-li-tac-dung-va-ham-lagrange`</sub>

---

### 2. Tọa độ suy rộng, ràng buộc và nhân tử Lagrange
*Generalized coordinates, constraints and Lagrange multipliers* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Phân biệt được ràng buộc holonom và không holonom
- Xác định được số bậc tự do của một hệ cơ học cụ thể
- Vận dụng được phương pháp nhân tử Lagrange để tính lực ràng buộc

## Ràng buộc: hai loại rất khác nhau

Ràng buộc **holonom** viết được thành $f(\vec r_1,\dots,\vec r_N,t)=0$: hạt trên mặt cầu, dây không dãn, thanh cứng. Mỗi phương trình như vậy cắt đi một bậc tự do, nên $n = 3N - m$.

Ràng buộc **không holonom** chỉ viết được ở dạng vi phân không tích phân được, ví dụ điều kiện lăn không trượt của đĩa trên mặt phẳng. Nó hạn chế *vận tốc* nhưng không hạn chế miền cấu hình đạt tới được, do đó **không** làm giảm số tọa độ cần dùng.

## Tọa độ suy rộng

Chọn $n$ đại lượng $q_1,\dots,q_n$ đủ để xác định cấu hình. Chúng không nhất thiết có thứ nguyên độ dài: góc, diện tích, thậm chí tổ hợp phi tuyến đều được. Khi đó $\vec r_i=\vec r_i(q,t)$ và toàn bộ ràng buộc holonom đã tự động thoả mãn — đó chính là cái lợi lớn nhất.

## Khi cần biết lực ràng buộc

Chọn tọa độ độc lập thì lực ràng buộc biến mất, nhưng đôi khi ta lại **cần** nó (ví dụ để biết khi nào vật rời mặt cong). Khi đó giữ nguyên tọa độ dư thừa và ràng buộc $f(q,t)=0$, viết

$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_k}-\frac{\partial L}{\partial q_k}=\lambda\,\frac{\partial f}{\partial q_k}$$

Vế phải chính là lực ràng buộc suy rộng; $\lambda$ và các $q_k$ được giải đồng thời cùng $f=0$.

## Lực không thế

Nếu có lực không rút ra từ thế (ma sát, lực cưỡng bức ngoài), thêm lực suy rộng $Q_k$ vào vế phải. Riêng lực cản tỉ lệ vận tốc mô tả gọn bằng hàm tiêu tán Rayleigh $\mathcal F$, khi đó vế phải là $-\partial\mathcal F/\partial\dot q_k$.

**Lỗi thường gặp:**
- Trừ bậc tự do cho ràng buộc lăn không trượt của đĩa trong mặt phẳng. Sai vì đó là ràng buộc không holonom: nó ràng buộc vận tốc chứ không thu hẹp tập cấu hình, đĩa vẫn tới được mọi vị trí và mọi hướng.
- Cho rằng nhân tử $\lambda$ luôn có thứ nguyên lực. Thứ nguyên của $\lambda$ phụ thuộc cách viết hàm ràng buộc $f$; chỉ tích $\lambda\,\partial f/\partial q_k$ mới chắc chắn là lực suy rộng.
- Thêm lực ma sát vào thế năng để "tiện". Sai vì công của ma sát phụ thuộc đường đi nên không tồn tại hàm thế; phải đưa vào qua lực suy rộng hoặc hàm tiêu tán Rayleigh.

<sub>`lesson.physics.co-hoc-giai-tich.toa-do-suy-rong-va-rang-buoc`</sub>

---

### 3. Định lí Noether và các định luật bảo toàn
*Noether's theorem and conservation laws* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Giải thích được liên hệ giữa đối xứng liên tục của hàm Lagrange và đại lượng bảo toàn
- Xác định được tọa độ cyclic và động lượng suy rộng bảo toàn tương ứng
- Chứng minh được sự bảo toàn hàm năng lượng khi Lagrange không phụ thuộc tường minh thời gian

## Câu hỏi trung tâm

Vì sao động lượng, mômen động lượng và năng lượng lại được bảo toàn? Newton coi đó là các định lí riêng lẻ. Noether cho thấy cả ba đều là **cùng một sự thật**: chúng đến từ tính đối xứng của quy luật, không phải từ chi tiết của lực.

## Trường hợp dễ thấy: tọa độ cyclic

Nếu $q_k$ không xuất hiện tường minh trong $L$ thì $\partial L/\partial q_k=0$, và phương trình Euler - Lagrange rút gọn ngay thành

$$\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q_k}\right)=0\ \Longrightarrow\ p_k=\frac{\partial L}{\partial\dot q_k}=\text{const}$$

Nếu $q_k$ là một toạ độ tịnh tiến, $p_k$ là động lượng thẳng; nếu là một góc quay, $p_k$ là mômen động lượng quanh trục đó.

## Dạng tổng quát

Cho họ biến đổi $q_k\to q_k+\varepsilon\,K_k(q)$ mà $L$ bất biến tới bậc nhất theo $\varepsilon$. Khi đó đại lượng

$$I=\sum_k \frac{\partial L}{\partial\dot q_k}K_k(q)$$

không đổi theo thời gian. Chứng minh chỉ gồm hai bước: khai triển điều kiện bất biến $\delta L=0$ rồi thay $\partial L/\partial q_k$ bằng $\dot p_k$.

## Đối xứng thời gian

Nếu $\partial L/\partial t=0$ thì hàm năng lượng $h=\sum_k p_k\dot q_k-L$ bảo toàn. Chú ý: $h$ **chỉ** bằng $T+U$ khi các phương trình liên hệ $\vec r_i(q)$ không chứa $t$ tường minh và $T$ là dạng toàn phương thuần nhất của $\dot q$. Trong hệ quy chiếu quay, $h$ bảo toàn nhưng khác cơ năng — đó là tích phân Jacobi.

**Lỗi thường gặp:**
- Đồng nhất động lượng suy rộng với $m\dot q$. Sai vì $p_k=\partial L/\partial\dot q_k$ phụ thuộc dạng của $L$: với hạt tích điện trong từ trường $p_x=m\dot x+qA_x$, khác hẳn động lượng cơ học.
- Kết luận "năng lượng bảo toàn" chỉ vì $\partial L/\partial t=0$ rồi lấy luôn $E=T+U$. Đại lượng bảo toàn là $h=\sum p_k\dot q_k-L$; khi hệ tọa độ phụ thuộc thời gian (ví dụ hạt trên vòng đang quay cưỡng bức) thì $h\neq T+U$.
- Tìm đại lượng bảo toàn từ đối xứng rời rạc như phép phản xạ. Định lí Noether đòi hỏi nhóm biến đổi **liên tục** một tham số; đối xứng rời rạc cho quy tắc lọc lựa chứ không cho tích phân chuyển động.

<sub>`lesson.physics.co-hoc-giai-tich.dinh-li-noether-va-cac-bao-toan`</sub>

---

### 4. Hàm Hamilton và hệ phương trình chính tắc
*The Hamiltonian and canonical equations* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Xây dựng được hàm Hamilton bằng biến đổi Legendre từ hàm Lagrange
- Viết được hệ phương trình chính tắc Hamilton cho một hệ cụ thể
- Giải thích được ý nghĩa của không gian pha và ưu điểm của hình thức Hamilton

## Đổi biến, không đổi vật lí

Lagrange cho $n$ phương trình bậc hai theo $(q,\dot q)$. Hamilton đổi sang $2n$ phương trình bậc **nhất** theo $(q,p)$. Số phương trình tăng gấp đôi nhưng cấu trúc đẹp hơn hẳn: mỗi biến tiến hoá độc lập, và toàn bộ động lực được mã hoá trong một hàm duy nhất.

## Biến đổi Legendre

Định nghĩa $p_k=\partial L/\partial\dot q_k$, rồi **giải ngược** để có $\dot q_k=\dot q_k(q,p,t)$ (bước này đòi hỏi ma trận Hess $\partial^2 L/\partial\dot q_i\partial\dot q_j$ khả nghịch). Đặt

$$H(q,p,t)=\sum_k p_k\dot q_k-L(q,\dot q,t)$$

trong đó mọi $\dot q$ phải được thay hết bằng $p$ — đây là điểm dễ sai nhất.

## Hệ phương trình chính tắc

Lấy vi phân toàn phần của $H$ và so sánh hệ số:

$$\dot q_k=\frac{\partial H}{\partial p_k},\qquad \dot p_k=-\frac{\partial H}{\partial q_k},\qquad \frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}$$

Hệ quả tức thì: nếu $H$ không phụ thuộc $t$ tường minh thì $dH/dt=0$.

## Vì sao hình thức này quan trọng

Với hệ bảo toàn quen thuộc $H=T+U=E$. Nhưng giá trị thật của hình thức Hamilton không nằm ở chỗ giải bài toán nhanh hơn — thường nó còn dài hơn — mà ở cấu trúc: dòng trong không gian pha bảo toàn thể tích, cho phép định nghĩa ngoặc Poisson, mở đường sang cơ học thống kê (tổng thống kê lấy trên không gian pha) và sang cơ học lượng tử (thay $\{\,,\,\}$ bằng $\tfrac{1}{i\hbar}[\,,\,]$).

**Lỗi thường gặp:**
- Viết $H$ mà vẫn còn chứa $\dot q$. Hamilton là hàm của $(q,p,t)$; nếu còn $\dot q$ thì đạo hàm $\partial H/\partial p$ không có nghĩa và hệ chính tắc thu được sẽ sai.
- Mặc định $H=E$. Đẳng thức này chỉ đúng khi phép đổi tọa độ không phụ thuộc thời gian tường minh; với hệ chịu ràng buộc chuyển động cưỡng bức, $H$ vẫn bảo toàn nhưng không phải cơ năng.
- Quên dấu trừ trong $\dot p_k=-\partial H/\partial q_k$. Dấu này chính là cấu trúc symplectic của bài toán; đảo dấu sẽ cho nghiệm đảo chiều thời gian, ví dụ dao động tử trở thành hệ tăng trưởng theo hàm mũ.

<sub>`lesson.physics.co-hoc-giai-tich.ham-hamilton-va-phuong-trinh-chinh-tac`</sub>

---

### 5. Ngoặc Poisson, biến đổi chính tắc và định lí Liouville
*Poisson brackets, canonical transformations and Liouville's theorem* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Tính được ngoặc Poisson của các đại lượng động lực cơ bản
- Vận dụng được ngoặc Poisson để kiểm tra một đại lượng có bảo toàn hay không
- Giải thích được nội dung và hệ quả của định lí Liouville về thể tích pha

## Một công thức gói trọn động lực học

Với hàm bất kì $f(q,p,t)$, quy tắc dây chuyền cùng hệ chính tắc cho

$$\frac{df}{dt}=\{f,H\}+\frac{\partial f}{\partial t}$$

Vậy chỉ cần một phép toán — ngoặc Poisson — là biết mọi đại lượng tiến hoá thế nào. Đặc biệt, $f$ không phụ thuộc $t$ tường minh là **tích phân chuyển động** khi và chỉ khi $\{f,H\}=0$. Đây là cách kiểm tra bảo toàn nhanh hơn nhiều so với tìm đối xứng bằng mắt.

## Các ngoặc cơ bản

$$\{q_i,q_j\}=0,\qquad \{p_i,p_j\}=0,\qquad \{q_i,p_j\}=\delta_{ij}$$

Ngoặc Poisson phản đối xứng, tuyến tính, thoả quy tắc Leibniz và đồng nhất thức Jacobi. Chính bộ tính chất này được sao chép nguyên vẹn sang giao hoán tử lượng tử qua tương ứng $\{f,g\}\to\frac{1}{i\hbar}[\hat f,\hat g]$.

## Biến đổi chính tắc

Một phép đổi biến $(q,p)\to(Q,P)$ là chính tắc khi $\{Q_i,P_j\}=\delta_{ij}$ theo biến cũ. Sinh ra chúng bằng hàm sinh, ví dụ loại hai $F_2(q,P)$ với $p=\partial F_2/\partial q$, $Q=\partial F_2/\partial P$. Mục tiêu thực dụng: chọn biến mới sao cho càng nhiều tọa độ trở thành cyclic càng tốt — đẩy tới cùng chính là phương trình Hamilton - Jacobi và biến tác dụng - góc.

## Định lí Liouville

Dòng Hamilton có divergence bằng không trong không gian pha, do đó mật độ điểm pha $\rho$ thoả $d\rho/dt=0$: một "giọt" trạng thái ban đầu có thể bị kéo dài và xoắn rối nhưng **thể tích không đổi**. Đây là nền tảng để định nghĩa tổng thống kê trong vật lí thống kê cổ điển.

**Lỗi thường gặp:**
- Quên dấu và thứ tự trong định nghĩa, viết $\{f,g\}=\sum(\partial_p f\,\partial_q g-\partial_q f\,\partial_p g)$. Đảo dấu làm mọi tích phân chuyển động vẫn đúng nhưng phương trình tiến hoá $df/dt=\{f,H\}$ chạy ngược thời gian.
- Hiểu định lí Liouville là "hình dạng miền pha không đổi". Chỉ **thể tích** được bảo toàn; hình dạng thường bị kéo thành sợi mảnh vô cùng, và chính điều này giải thích vì sao hệ tất định vẫn tiến tới trạng thái trông như cân bằng thống kê.
- Coi mọi phép đổi biến "trông tự nhiên" đều là chính tắc. Ví dụ $Q=q^2$, $P=p$ không chính tắc vì $\{Q,P\}=2q\neq 1$, và nếu cứ áp dụng hệ phương trình Hamilton cho biến mới sẽ ra động lực học sai.

<sub>`lesson.physics.co-hoc-giai-tich.ngoac-poisson-va-dinh-li-liouville`</sub>

---

### 6. Bài toán hai vật, khối lượng rút gọn và thế hiệu dụng
*Two-body problem, reduced mass and effective potential* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Tách được bài toán hai vật thành chuyển động khối tâm và chuyển động tương đối
- Xây dựng được thế hiệu dụng và phân tích được dạng quỹ đạo theo năng lượng
- Chứng minh được quỹ đạo conic trong trường hấp dẫn Newton

## Tách bài toán

Với hai vật tương tác qua thế chỉ phụ thuộc khoảng cách, đổi sang tọa độ khối tâm $\vec R$ và tọa độ tương đối $\vec r=\vec r_1-\vec r_2$:

$$L=\tfrac12 M\dot{\vec R}^2+\tfrac12\mu\dot{\vec r}^2-U(r),\qquad \mu=\frac{m_1m_2}{m_1+m_2}$$

Hai phần tách hẳn nhau. $\vec R$ là tọa độ cyclic nên khối tâm chuyển động thẳng đều; bài toán còn lại là **một** hạt khối lượng $\mu$ trong trường xuyên tâm.

## Rút về một chiều

Lực xuyên tâm nên $\vec\ell$ bảo toàn, chuyển động nằm trong một mặt phẳng, và $\ell=\mu r^2\dot\varphi$. Thay $\dot\varphi=\ell/(\mu r^2)$ vào cơ năng:

$$E=\tfrac12\mu\dot r^2+\underbrace{U(r)+\frac{\ell^2}{2\mu r^2}}_{U_{\text{eff}}(r)}$$

Bài toán hai chiều đã thành bài toán một chiều. Đọc đồ thị $U_{\text{eff}}$ là biết ngay loại quỹ đạo: cực tiểu ứng với quỹ đạo tròn bền; $E<0$ cho chuyển động bị chặn giữa $r_{\min}$ và $r_{\max}$; $E\ge 0$ cho quỹ đạo mở.

## Trường Kepler

Với $U=-k/r$, đổi biến $u=1/r$ đưa phương trình quỹ đạo về dạng dao động tử (phương trình Binet):

$$\frac{d^2u}{d\varphi^2}+u=\frac{\mu k}{\ell^2}$$

Nghiệm là conic $r=\dfrac{p}{1+e\cos\varphi}$ với $p=\ell^2/(\mu k)$ và $e=\sqrt{1+\dfrac{2E\ell^2}{\mu k^2}}$. Dấu của $E$ quyết định loại conic: elip ($E<0$), parabol ($E=0$), hyperbol ($E>0$).

## Giới hạn áp dụng

Kết quả conic đóng kín chỉ đúng riêng cho thế $1/r$ và thế đàn hồi $r^2$ (định lí Bertrand). Mọi nhiễu loạn nhỏ — vật thứ ba, độ dẹt của thiên thể, hiệu ứng tương đối tính — đều làm quỹ đạo tiến động.

**Lỗi thường gặp:**
- Dùng khối lượng $m_1$ thay cho $\mu$ khi hai khối lượng so sánh được. Chỉ khi $m_2\gg m_1$ mới có $\mu\approx m_1$; với hệ sao đôi, sai số này làm lệch cả chu kì lẫn năng lượng liên kết.
- Coi rào li tâm $\ell^2/(2\mu r^2)$ là một thế năng thật. Nó là hệ quả của việc đã dùng bảo toàn mômen động lượng để khử $\dot\varphi$; nếu vẫn giữ $\dot\varphi$ trong Lagrange rồi lại thêm rào li tâm là tính hai lần.
- Kết luận mọi lực hút xuyên tâm đều cho quỹ đạo elip đóng kín. Chỉ $1/r$ và $r^2$ có tính chất đó; các thế khác cho quỹ đạo hình hoa thị vì tỉ số $\omega_r/\omega_\varphi$ không phải số hữu tỉ.

<sub>`lesson.physics.co-hoc-giai-tich.bai-toan-hai-vat-va-the-hieu-dung`</sub>

---

### 7. Tán xạ trong trường xuyên tâm và công thức Rutherford
*Scattering in a central field and the Rutherford formula* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Định nghĩa được tham số va chạm và tiết diện tán xạ vi phân
- Thiết lập được liên hệ giữa tham số va chạm và góc tán xạ trong trường Coulomb
- Phân tích được ý nghĩa thí nghiệm của công thức Rutherford

## Bài toán ngược của quỹ đạo

Với quỹ đạo hyperbol ta biết đường đi. Trong thí nghiệm tán xạ thì ngược lại: chỉ đo được **có bao nhiêu hạt bay ra theo mỗi hướng**, từ đó suy ngược ra dạng của lực. Cầu nối giữa hai thứ là tiết diện.

## Từ quỹ đạo tới tiết diện

Chùm hạt tới đồng nhất, mỗi hạt có tham số va chạm $b$ xác định. Vì $b$ càng nhỏ thì hạt tới càng gần tâm và bị lệch càng mạnh, nên $\theta$ là hàm đơn điệu giảm của $b$. Các hạt đi qua vành $b\to b+db$ đúng bằng các hạt bay ra trong vành góc $\theta\to\theta+d\theta$:

$$\frac{d\sigma}{d\Omega}=\frac{b}{\sin\theta}\left|\frac{db}{d\theta}\right|$$

Trị tuyệt đối là bắt buộc vì $db/d\theta<0$ trong khi tiết diện phải dương.

## Trường Coulomb

Giải quỹ đạo hyperbol cho thế $U=\dfrac{q_1q_2}{4\pi\varepsilon_0 r}$ ta được

$$b=\frac{q_1q_2}{8\pi\varepsilon_0 E}\cot\frac{\theta}{2}$$

Thay vào công thức trên:

$$\frac{d\sigma}{d\Omega}=\left(\frac{q_1q_2}{16\pi\varepsilon_0 E}\right)^{2}\frac{1}{\sin^{4}(\theta/2)}$$

## Vì sao kết quả này đổi cả vật lí

Phân bố $\sin^{-4}(\theta/2)$ tiên đoán một số ít hạt alpha bị bật ngược lại — điều không thể xảy ra nếu điện tích dương trải đều trong nguyên tử. Thí nghiệm Geiger - Marsden khớp với công thức này ở mọi góc, buộc phải thừa nhận hạt nhân nhỏ và đặc. Đáng chú ý: công thức cổ điển này trùng khít kết quả lượng tử trong xấp xỉ Born, một sự trùng hợp riêng của thế $1/r$.

## Giới hạn

Tiết diện toàn phần $\int (d\sigma/d\Omega)\,d\Omega$ phân kì vì thế Coulomb tầm xa vô hạn; trong thực tế hiệu ứng che chắn của electron cắt đuôi này ở góc rất nhỏ.

**Lỗi thường gặp:**
- Nhầm góc tán xạ trong hệ phòng thí nghiệm với góc trong hệ khối tâm. Công thức Rutherford viết cho hệ khối tâm; khi khối lượng bia không lớn hơn hẳn khối lượng đạn thì hai góc khác nhau đáng kể.
- Bỏ trị tuyệt đối trong $|db/d\theta|$ rồi thu được tiết diện âm. Tiết diện là một diện tích hiệu dụng nên luôn dương; dấu âm chỉ phản ánh việc $b$ giảm khi $\theta$ tăng.
- Kết luận công thức sai vì tiết diện toàn phần phân kì. Phân kì là ở $\theta\to 0$, tức các hạt gần như không lệch, phản ánh tầm tác dụng vô hạn của lực Coulomb chứ không phải lỗi tính toán.

<sub>`lesson.physics.co-hoc-giai-tich.tan-xa-rutherford`</sub>

---

### 8. Hệ quy chiếu quay, lực li tâm và lực Coriolis
*Rotating frames, centrifugal and Coriolis forces* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Thiết lập được liên hệ giữa đạo hàm trong hệ đứng yên và trong hệ quay
- Viết được phương trình Newton đầy đủ trong hệ quy chiếu quay
- Giải thích được các hiện tượng địa vật lí gây bởi lực Coriolis

## Vì sao phải làm việc trong hệ quay

Trái Đất quay, và mọi phép đo trong phòng thí nghiệm đều thực hiện trong một hệ quay. Ta có hai lựa chọn: mô tả trong hệ quán tính rồi đổi tọa độ (rất rối), hoặc viết định luật Newton ngay trong hệ quay với giá cho phải trả là xuất hiện các **lực quán tính**.

## Chìa khoá: đạo hàm vectơ

Với mọi vectơ $\vec A$,

$$\left(\frac{d\vec A}{dt}\right)_{\text{qt}}=\left(\frac{d\vec A}{dt}\right)_{\text{quay}}+\vec\omega\times\vec A$$

Áp dụng hai lần cho vectơ vị trí rồi nhân $m$:

$$m\vec a\,'=\vec F-m\vec\omega\times(\vec\omega\times\vec r)-2m\,\vec\omega\times\vec v\,'-m\dot{\vec\omega}\times\vec r$$

Ba số hạng thêm lần lượt là lực li tâm, lực Coriolis và lực Euler (bằng 0 khi $\omega$ không đổi).

## Đọc từng số hạng

**Li tâm** chỉ phụ thuộc vị trí, có thể gộp vào một thế hiệu dụng; trên Trái Đất nó làm $g$ hiệu dụng giảm khoảng $0{,}3\%$ ở xích đạo và lệch khỏi phương bán kính.

**Coriolis** chỉ tác dụng lên vật đang chuyển động trong hệ quay và luôn vuông góc $\vec v\,'$, nên **không sinh công** — nó bẻ hướng chứ không đổi tốc độ. Ở bắc bán cầu nó làm mọi chuyển động ngang lệch sang phải, nên dòng khí hội tụ vào một vùng áp thấp bị bẻ thành chuyển động **ngược chiều kim đồng hồ** — đó là xoáy thuận (cyclone); vùng áp cao cho xoáy nghịch quay theo chiều ngược lại. Cũng chính lực này làm mặt phẳng dao động của con lắc Foucault quay chậm với chu kì $T=24\ \text{h}/\sin\lambda$.

## Cảnh báo

Lực quán tính không có phản lực và không phải là tương tác: chúng biến mất ngay khi ta quay lại hệ quán tính. Chúng cũng không đủ để giải thích các hiệu ứng cỡ nhỏ như chiều xoáy nước bồn rửa — ở quy mô đó lực Coriolis nhỏ hơn nhiều so với nhiễu động ban đầu.

**Lỗi thường gặp:**
- Cho rằng lực Coriolis làm vật chuyển động nhanh lên hoặc chậm đi. Vì nó luôn vuông góc với $\vec v\,'$ nên công bằng 0; nó chỉ đổi hướng chuyển động.
- Dùng lực li tâm cho một vật đứng yên trong hệ quán tính khi đang mô tả trong hệ đó. Các lực quán tính chỉ xuất hiện khi phương trình được viết trong hệ phi quán tính; đưa chúng vào hệ quán tính là đếm lực hai lần.
- Lẫn lộn lực hướng tâm với lực li tâm. Lực hướng tâm là hợp lực thật hướng vào trục trong hệ quán tính; lực li tâm là lực quán tính hướng ra ngoài, chỉ tồn tại trong hệ quay và không có vật nào gây ra nó.

<sub>`lesson.physics.co-hoc-giai-tich.he-quy-chieu-quay-va-luc-coriolis`</sub>

---

### 9. Dao động nhỏ ghép và mode chuẩn
*Coupled small oscillations and normal modes* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Khai triển được hàm Lagrange tới bậc hai quanh vị trí cân bằng bền
- Giải được bài toán trị riêng suy rộng để tìm tần số riêng
- Xác định được tọa độ chuẩn và giải thích được ý nghĩa vật lí của mode chuẩn

## Ý tưởng: mọi hệ đều là dao động tử ở gần cân bằng

Quanh vị trí cân bằng bền, khai triển thế năng tới bậc hai (bậc nhất triệt tiêu theo định nghĩa cân bằng) và động năng tới bậc thấp nhất:

$$U\approx\tfrac12 V_{ij}\,\eta_i\eta_j,\qquad T\approx\tfrac12 T_{ij}\,\dot\eta_i\dot\eta_j$$

với $\eta_i$ là độ lệch khỏi cân bằng. Cả $V$ và $T$ là ma trận đối xứng, $T$ xác định dương.

## Bài toán trị riêng suy rộng

Thử nghiệm $\eta_i=a_i e^{-i\omega t}$ đưa phương trình Lagrange về $(V-\omega^2 T)\vec a=0$. Có nghiệm không tầm thường khi

$$\det(V-\omega^2 T)=0$$

Đây là phương trình đặc trưng; $n$ nghiệm $\omega_k^2$ là bình phương các tần số riêng. Vì $V,T$ đối xứng và $T>0$ nên mọi $\omega_k^2$ đều thực; cân bằng bền tương đương mọi $\omega_k^2>0$.

## Tọa độ chuẩn

Các vectơ riêng $\vec a^{(k)}$ trực giao theo tích vô hướng có trọng số $T$. Đặt $\eta_i=\sum_k a_i^{(k)}\xi_k$ thì

$$L=\tfrac12\sum_k\left(\dot\xi_k^2-\omega_k^2\xi_k^2\right)$$

Hệ ghép đã tách thành $n$ dao động tử **độc lập**. Đây chính là lí do khái niệm mode chuẩn quan trọng: mọi chuyển động nhỏ đều là chồng chất của các mode, mỗi mode tiến hoá riêng.

## Ở đâu dùng lại

Cùng bộ công cụ này tái xuất khi lượng tử hoá dao động mạng tinh thể (phonon), khi phân tích dao động phân tử trong quang phổ hồng ngoại, và khi nghiên cứu độ bền kết cấu. Điều kiện áp dụng là biên độ đủ nhỏ để bỏ được số hạng bậc ba trở lên — nếu không, các mode ghép trở lại với nhau và sinh phi tuyến.

**Lỗi thường gặp:**
- Giải $\det(V-\omega^2\mathbf 1)=0$ khi ma trận động năng không tỉ lệ đơn vị. Với các khối lượng khác nhau hoặc tọa độ góc, phải dùng $\det(V-\omega^2T)=0$; bỏ qua $T$ cho tần số sai hoàn toàn.
- Cho rằng vectơ riêng trực giao theo nghĩa thông thường. Chúng trực giao theo tích có trọng số $T$: $\vec a^{(k)T}T\vec a^{(l)}=0$; dùng trực giao Euclid sẽ tách tọa độ chuẩn sai.
- Bỏ qua các nghiệm $\omega^2=0$. Chúng không phải lỗi tính toán mà ứng với mode tịnh tiến hoặc quay tổng thể — chuyển động không bị lực hồi phục, cần xử lí riêng.

<sub>`lesson.physics.co-hoc-giai-tich.dao-dong-ghep-va-mode-chuan`</sub>

---

### 10. Động lực học vật rắn: tenxơ quán tính và phương trình Euler
*Rigid-body dynamics: inertia tensor and Euler equations* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Tính được các thành phần của tenxơ quán tính cho vật rắn đơn giản
- Giải thích được vì sao mômen động lượng nói chung không cùng phương với vận tốc góc
- Vận dụng được phương trình Euler để phân tích chuyển động tự do của con quay đối xứng

## Vì sao cần tenxơ, không phải một số

Ở phổ thông, $L=I\omega$ với $I$ là một số — nhưng điều đó chỉ đúng khi trục quay cố định và là trục đối xứng. Trong trường hợp tổng quát,

$$\vec L=\mathbf I\,\vec\omega,\qquad I_{ij}=\int\rho\,(r^2\delta_{ij}-x_ix_j)\,dV$$

và $\vec L$ **không** cùng phương $\vec\omega$. Đây chính là nguyên nhân vật lí của hiện tượng rung khi bánh xe chưa cân bằng động: trục phải liên tục tác dụng mômen để giữ $\vec L$ quay theo.

## Trục chính

$\mathbf I$ đối xứng thực nên luôn chéo hoá được: tồn tại ba trục vuông góc với các mômen quán tính chính $I_1,I_2,I_3$. Trong hệ trục đó

$$T_{\text{quay}}=\tfrac12\left(I_1\omega_1^2+I_2\omega_2^2+I_3\omega_3^2\right)$$

Mọi trục đối xứng của vật đều là trục chính, nên với vật đối xứng ta khỏi phải chéo hoá.

## Phương trình Euler

Viết $d\vec L/dt=\vec\tau$ trong hệ **gắn với vật** (nơi $\mathbf I$ không đổi) và dùng quan hệ đạo hàm hệ quay:

$$I_1\dot\omega_1+(I_3-I_2)\omega_2\omega_3=\tau_1$$

cùng hai phương trình hoán vị vòng quanh. Số hạng phi tuyến này là nguồn gốc của mọi hiện tượng "lạ" của con quay.

## Hai hệ quả kinh điển

Với con quay đối xứng tự do ($I_1=I_2$, $\vec\tau=0$), $\omega_3$ không đổi còn $\vec\omega$ tiến động quanh trục vật với tốc độ $\Omega=\dfrac{I_3-I_1}{I_1}\omega_3$.

Với con quay không đối xứng ($I_1<I_2<I_3$), quay quanh trục có mômen quán tính **trung gian** là không bền: nhiễu loạn nhỏ tăng theo hàm mũ. Đó là hiệu ứng vợt tennis, kiểm chứng được bằng cách tung một cuốn sách.

**Lỗi thường gặp:**
- Dùng $\vec L=I\vec\omega$ với $I$ vô hướng trong trường hợp tổng quát. Chỉ khi $\vec\omega$ trùng một trục chính thì $\vec L$ mới cùng phương $\vec\omega$; ngoài ra $\vec L$ lệch và tạo mômen lên ổ trục.
- Áp dụng định lí trục song song cho một trục bất kì không qua khối tâm mà không song song. Định lí Steiner chỉ đúng cho trục **song song** với trục qua khối tâm; trường hợp tổng quát phải dùng công thức dịch chuyển đầy đủ của tenxơ.
- Viết phương trình Euler trong hệ phòng thí nghiệm. Chúng chỉ đúng trong hệ gắn với vật theo các trục chính, nơi các $I_k$ là hằng số; trong hệ cố định $\mathbf I$ biến thiên theo thời gian và phương trình có dạng khác.

<sub>`lesson.physics.co-hoc-giai-tich.dong-luc-hoc-vat-ran-va-tenxo-quan-tinh`</sub>

---

## Unit 2: Rigid Body Dynamics and Analytical Mechanics

### 1. Mômen quán tính và Động lực học vật rắn quay quanh trục cố định
*Rotational dynamics of rigid bodies and moment of inertia* · Đại học · intl-undergrad, vn-gdpt-2018 · 55 phút · trung-binh

**Mục tiêu:**
- Tính mômen quán tính của các vật rắn đồng chất hình học cơ bản bằng tích phân
- Áp dụng định lý trục song song Steiner - Huygens và định lý trục vuông góc
- Thiết lập phương trình động lực học chuyển động quay và bảo toàn mômen động lượng

## Định nghĩa và Phương pháp tích phân

Mômen quán tính của vật rắn liên tục đối với trục $\Delta$ được xác định bởi tích phân khối lượng:

$$I = \int r_{\perp}^2\,dm = \int \rho(\vec{r}) r_{\perp}^2\,dV$$

Với các vật đồng chất: đĩa tròn $I = \frac{1}{2} M R^2$, khối cầu đặc $I = \frac{2}{5} M R^2$, thanh mảnh qua tâm $I = \frac{1}{12} M L^2$.

## Định lý Steiner - Huygens và Định lý Trục vuông góc

Nếu biết mômen quán tính đối với trục đi qua khối tâm $I_{cm}$, mômen quán tính đối với trục $\Delta$ song song cách một đoạn $d$ là:

$$I_{\Delta} = I_{cm} + M d^2$$

Phương trình động lực học quay cơ bản: $M = I \gamma = I \frac{d\omega}{dt}$.

**Lỗi thường gặp:**
- Áp dụng định lý Steiner giữa hai trục bất kì mà không có trục nào đi qua khối tâm
- Nhầm lẫn hệ số mômen quán tính giữa khối cầu đặc (2/5) và khối cầu rỗng (2/3)

<sub>`lesson.physics.undergrad-physics.tensor-quan-tinh-va-dong-luc-hoc-vat-ran`</sub>

---

### 2. Động năng lăn không trượt và Hiện tượng tiến động của con quay
*Rolling without slipping, kinetic energy and gyroscopic precession* · Đại học · intl-undergrad, vn-gdpt-2018 · 55 phút · nang-cao

**Mục tiêu:**
- Phân tích động năng của vật rắn lăn không trượt thành chuyển động tịnh tiến và tự quay
- Tính gia tốc của khối cầu hoặc khối trụ lăn trên mặt phẳng nghiêng
- Giải thích cơ chế tiến động của con quay dưới tác dụng của mômen trọng lực

## Động năng lăn không trượt

Theo định lý König, động năng toàn phần của vật rắn lăn không trượt bằng tổng động năng tịnh tiến của khối tâm và động năng quay quanh khối tâm:

$$K = \frac{1}{2} M v_{cm}^2 + \frac{1}{2} I_{cm} \omega^2$$

Vì $v_{cm} = R \omega$, ta có $K = \frac{1}{2} M v_{cm}^2 \left(1 + \frac{I_{cm}}{M R^2}\right)$. Hệ số $\beta = \frac{I_{cm}}{M R^2}$ quyết định gia tốc lăn của vật trên mặt nghiêng góc $\alpha$:

$$a = \frac{g \sin \alpha}{1 + \beta}$$

## Hiện tượng tiến động của con quay

Khi con quay quay với vận tốc góc lớn $\omega$, trọng lực tạo mômen $\vec{M} = \vec{r} \times \vec{P}$ vuông góc với trục quay, làm biến thiên mômen động lượng $d\vec{L} = \vec{M} dt$, khiến trục quay chuyển động tiến động với tốc độ góc:

$$\Omega_p = \frac{M g d}{I \omega}$$

**Lỗi thường gặp:**
- Bỏ qua công của ma sát nghỉ: ma sát nghỉ không làm tiêu hao cơ năng trong chuyển động lăn không trượt
- Nghĩ rằng vật nặng hơn sẽ lăn nhanh hơn (gia tốc chỉ phụ thuộc vào phân bố hình học beta, độc lập với khối lượng M)

<sub>`lesson.physics.undergrad-physics.dong-nang-lan-khong-truot-va-tien-dong`</sub>

---

## Unit 2: Điện động lực học

### 1. Tĩnh điện: định lí Gauss và phương trình Poisson - Laplace
*Electrostatics: Gauss's law and the Poisson-Laplace equation* · Đại học · intl-undergrad · 55 phút · trung-binh

**Mục tiêu:**
- Chuyển được định lí Gauss từ dạng tích phân sang dạng vi phân
- Thiết lập được phương trình Poisson và Laplace cho điện thế
- Phân tích được vai trò của điều kiện biên trong tính duy nhất của nghiệm

## Từ Coulomb tới phương trình vi phân

Định luật Coulomb cho ngay lời giải dưới dạng tích phân chồng chất, nhưng tích phân đó chỉ tính được khi biết trước **toàn bộ** phân bố điện tích. Trong thực tế ta thường chỉ biết điện thế trên các vật dẫn, còn điện tích cảm ứng phân bố ra sao lại là ẩn số. Cách xử lí đúng là chuyển sang bài toán biên.

## Dạng vi phân

Lấy divergence hai vế của $\vec E$ do một điện tích điểm gây ra, dùng $\nabla\!\cdot\!\dfrac{\hat r}{r^2}=4\pi\delta^3(\vec r)$:

$$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0},\qquad \nabla\times\vec E=0$$

Vì trường tĩnh điện không xoáy nên tồn tại $V$ với $\vec E=-\nabla V$. Thay vào:

$$\nabla^2V=-\frac{\rho}{\varepsilon_0}$$

Trong miền trống điện tích, $\nabla^2V=0$.

## Ý nghĩa của tính điều hòa

Hàm điều hòa có tính chất giá trị trung bình: $V$ tại một điểm bằng trung bình $V$ trên mọi mặt cầu bao quanh nó. Hệ quả trực tiếp là **định lí Earnshaw**: $V$ không thể có cực đại hay cực tiểu địa phương trong vùng trống, nên không thể giữ một điện tích ở trạng thái cân bằng bền chỉ bằng trường tĩnh điện. Đây là lí do bẫy ion phải dùng trường biến thiên theo thời gian.

## Điều kiện biên và tính duy nhất

Phương trình Laplace một mình không xác định nghiệm; cần thêm điều kiện biên. Nếu biết $V$ trên toàn biên (Dirichlet) hoặc $\partial V/\partial n$ trên toàn biên (Neumann, sai khác một hằng số), nghiệm là duy nhất. Chính định lí này cho phép ta dùng bất kì mẹo nào — đoán, đối xứng, ảnh điện — miễn là nghiệm tìm được thoả phương trình và biên: nó chắc chắn là nghiệm duy nhất.

**Lỗi thường gặp:**
- Dùng định lí Gauss để tính $\vec E$ khi phân bố điện tích không có đối xứng cầu, trụ hay phẳng. Định lí luôn đúng, nhưng nó chỉ cho **một** phương trình vô hướng trong khi $\vec E$ có ba thành phần chưa biết; chỉ khi đối xứng bảo đảm $E$ không đổi trên mặt Gauss ta mới rút được $E$ ra ngoài tích phân. Thiếu đối xứng thì bài toán thiếu dữ kiện chứ không phải định lí sai — khi đó phải giải phương trình Poisson.
- Cho rằng $E=0$ tại một điểm thì $V=0$ tại đó. $V$ và $E$ liên hệ qua đạo hàm, nên $V$ có thể lớn tuỳ ý ở nơi $E=0$; ví dụ bên trong một vật dẫn tích điện.
- Tìm được một nghiệm thoả phương trình Laplace rồi lo rằng còn nghiệm khác. Định lí duy nhất bảo đảm chỉ có một nghiệm ứng với điều kiện biên đã cho, nên mọi cách đoán hợp lệ đều dẫn tới cùng đáp số.

<sub>`lesson.physics.dien-dong-luc-hoc.tinh-dien-va-phuong-trinh-poisson-laplace`</sub>

---

### 2. Phương pháp ảnh điện và khai triển đa cực
*Method of images and multipole expansion* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Vận dụng được phương pháp ảnh điện cho mặt phẳng dẫn và quả cầu dẫn
- Khai triển được điện thế của một phân bố điện tích theo các số hạng đa cực
- Giải thích được vì sao mômen lưỡng cực phụ thuộc gốc tọa độ khi điện tích tổng khác không

## Ảnh điện: mượn định lí duy nhất

Bài toán "điện tích $q$ cách mặt phẳng dẫn nối đất một đoạn $d$" khó vì điện tích cảm ứng phân bố chưa biết. Mẹo: trong nửa không gian chứa $q$, ta chỉ cần **một** hàm $V$ thoả $\nabla^2V=-\rho/\varepsilon_0$ và $V=0$ trên mặt phẳng. Cấu hình gồm $q$ tại $+d$ và $-q$ tại $-d$ làm được đúng điều đó. Theo định lí duy nhất, nó chính là nghiệm — dù điện tích ảnh không hề tồn tại.

Với quả cầu dẫn bán kính $R$ nối đất và điện tích $q$ ở khoảng cách $a>R$, ảnh là $q'=-\dfrac{R}{a}q$ đặt cách tâm $b=\dfrac{R^2}{a}$. Lực hút suy ra ngay từ định luật Coulomb giữa $q$ và $q'$.

Điều kiện dùng được: hình học phải đủ đơn giản để tồn tại điện tích ảnh, và **chỉ được** dùng kết quả trong miền không chứa ảnh — năng lượng cũng phải tính lại vì trường ở nửa kia là khác.

## Khai triển đa cực

Ở xa một phân bố điện tích cỡ $a$, dùng $\dfrac{1}{|\vec r-\vec r\,'|}=\sum_n \dfrac{r'^n}{r^{n+1}}P_n(\cos\alpha)$:

$$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\left[\frac{Q}{r}+\frac{\vec p\cdot\hat r}{r^2}+\frac{1}{2}\frac{Q_{ij}\hat r_i\hat r_j}{r^3}+\dots\right]$$

Số hạng đầu tiên khác không là số hạng chi phối. Nếu $Q\neq 0$ thì $\vec p$ **phụ thuộc gốc tọa độ**; chỉ khi $Q=0$ thì $\vec p$ mới là đại lượng nội tại của hệ. Quy tắc này lặp lại ở mọi bậc.

## Ứng dụng

Phân tử trung hoà nhưng phân cực (nước) tương tác chủ yếu qua lưỡng cực; hạt nhân biến dạng có mômen tứ cực đo được bằng cộng hưởng từ; ăng-ten và bức xạ cũng được phân loại theo cùng ngôn ngữ đa cực.

**Lỗi thường gặp:**
- Dùng lời giải ảnh điện cho vùng nằm phía sau vật dẫn. Ở đó trường thực bằng không, còn cấu hình ảnh lại cho trường khác không, nên kết quả hoàn toàn sai.
- Tính năng lượng bằng công thức năng lượng tương tác của hệ hai điện tích thật. Vì trường chỉ chiếm nửa không gian, năng lượng đúng chỉ bằng một nửa; sai lầm này cho kết quả gấp đôi.
- Cho rằng mômen lưỡng cực luôn xác định duy nhất. Khi tổng điện tích khác không, dịch gốc tọa độ một đoạn $\vec a$ làm $\vec p\to\vec p-Q\vec a$; muốn nói về "mômen lưỡng cực của ion" phải nêu rõ gốc quy chiếu.

<sub>`lesson.physics.dien-dong-luc-hoc.phuong-phap-anh-dien-va-khai-trien-da-cuc`</sub>

---

### 3. Điện môi, vectơ phân cực và vectơ cảm ứng điện
*Dielectrics, polarization and the electric displacement* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Phân biệt được điện tích tự do và điện tích liên kết
- Thiết lập được định lí Gauss cho vectơ cảm ứng điện D
- Vận dụng được điều kiện biên của E và D tại mặt phân cách hai điện môi

## Vấn đề: điện tích ta không kiểm soát được

Đặt điện môi vào trường ngoài, các phân tử bị phân cực và xuất hiện điện tích **liên kết**. Chúng có thật, sinh trường thật, nhưng ta không rót chúng vào từ nguồn được. Cần một cách kế toán tách riêng phần "điện tích ta bơm vào" khỏi phần "vật liệu phản ứng lại".

## Phân cực và điện tích liên kết

Định nghĩa $\vec P$ là mômen lưỡng cực trên đơn vị thể tích. Tính điện thế của toàn khối bằng cách cộng đóng góp của các lưỡng cực rồi tích phân từng phần, kết quả tương đương với hai loại điện tích:

$$\rho_b=-\nabla\cdot\vec P,\qquad \sigma_b=\vec P\cdot\hat n$$

Ý nghĩa hình học rất trực quan: ở nơi $\vec P$ hội tụ, điện tích dồn lại; ở bề mặt, các đầu lưỡng cực không bị bù trừ.

## Vectơ D

Viết $\nabla\cdot\vec E=(\rho_f+\rho_b)/\varepsilon_0$ rồi chuyển $\rho_b$ sang vế trái:

$$\nabla\cdot\vec D=\rho_f,\qquad \vec D=\varepsilon_0\vec E+\vec P$$

Với điện môi tuyến tính đẳng hướng $\vec P=\varepsilon_0\chi_e\vec E$ nên $\vec D=\varepsilon_0\varepsilon_r\vec E$ với $\varepsilon_r=1+\chi_e$.

## Điều kiện biên và cạm bẫy

Tại mặt phân cách không có điện tích tự do: $E_{\parallel}$ liên tục (vì $\nabla\times\vec E=0$) còn $D_{\perp}$ liên tục (vì $\nabla\cdot\vec D=\rho_f$). Chú ý $\vec D$ **không** đóng vai trò như $\vec E$: nói chung $\nabla\times\vec D=\nabla\times\vec P\neq 0$, nên không tồn tại "thế của D" và không có định luật Coulomb cho $\vec D$. $\vec D$ chỉ là công cụ kế toán; lực tác dụng lên điện tích vẫn do $\vec E$ quyết định.

**Lỗi thường gặp:**
- Coi $\vec D$ có tính chất như $\vec E$, ví dụ viết $\vec D$ của một điện tích điểm theo Coulomb trong mọi cấu hình. Vì $\nabla\times\vec D$ nói chung khác không, $\vec D$ không có thế và định lí Gauss cho $\vec D$ chỉ giải được khi có đối xứng.
- Bỏ qua điện tích liên kết khi tính lực lên một điện tích thử đặt trong điện môi. Lực do trường $\vec E$ toàn phần gây ra, mà $\vec E$ đã bị điện tích liên kết làm yếu đi $\varepsilon_r$ lần.
- Áp dụng $\vec D=\varepsilon_0\varepsilon_r\vec E$ cho mọi vật liệu. Hệ thức này chỉ đúng với điện môi tuyến tính, đẳng hướng và không có phân cực dư; với chất sắt điện hay tinh thể dị hướng phải dùng tenxơ hoặc đường trễ.

<sub>`lesson.physics.dien-dong-luc-hoc.dien-moi-va-vecto-phan-cuc`</sub>

---

### 4. Tĩnh từ, thế vectơ và vật liệu từ
*Magnetostatics, the vector potential and magnetic materials* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Thiết lập được dạng vi phân của định luật Ampère và định lí Gauss cho từ trường
- Giải thích được ý nghĩa của thế vectơ và tính tự do chuẩn
- Phân biệt được nghịch từ, thuận từ và sắt từ theo cơ chế vi mô

## Hai phương trình nền

Thực nghiệm cho $\nabla\cdot\vec B=0$ (không có đơn cực từ) và, với dòng dừng, $\nabla\times\vec B=\mu_0\vec J$. Cặp này là song ánh của cặp tĩnh điện nhưng **đảo vai trò**: điện trường tĩnh không xoáy nhưng có nguồn, từ trường tĩnh có xoáy nhưng không nguồn.

## Thế vectơ

Vì $\nabla\cdot\vec B=0$ nên luôn viết được $\vec B=\nabla\times\vec A$. Nhưng $\vec A$ không duy nhất: $\vec A\to\vec A+\nabla\lambda$ cho cùng $\vec B$. Ta khai thác tự do này bằng cách chọn chuẩn Coulomb $\nabla\cdot\vec A=0$, khi đó định luật Ampère thành

$$\nabla^2\vec A=-\mu_0\vec J$$

tức ba phương trình Poisson độc lập — toàn bộ kĩ thuật tĩnh điện dùng lại được ngay.

## Vật liệu từ

Từ hóa $\vec M$ tương đương với dòng liên kết $\vec J_b=\nabla\times\vec M$ và dòng mặt $\vec K_b=\vec M\times\hat n$. Đặt $\vec H=\dfrac{\vec B}{\mu_0}-\vec M$ thì $\nabla\times\vec H=\vec J_f$, và với vật liệu tuyến tính $\vec B=\mu_0\mu_r\vec H$.

Ba lớp vật liệu, ba cơ chế khác hẳn nhau:

- **Nghịch từ** ($\chi_m<0$, rất nhỏ): trường ngoài làm biến đổi chuyển động quỹ đạo electron, mômen cảm ứng chống lại trường theo định luật Lenz. Mọi chất đều có, chỉ bị lấn át khi có cơ chế mạnh hơn.
- **Thuận từ** ($\chi_m>0$, nhỏ): các mômen từ nguyên tử có sẵn được định hướng một phần, cạnh tranh với nhiễu loạn nhiệt nên $\chi_m\propto 1/T$ (định luật Curie).
- **Sắt từ**: tương tác trao đổi lượng tử làm các spin lân cận song song trong từng đômen; quan hệ $\vec B(\vec H)$ phi tuyến và có trễ, mất trật tự trên nhiệt độ Curie.

## Cạm bẫy

$\vec H$ cũng chỉ là công cụ kế toán như $\vec D$: nói chung $\nabla\cdot\vec H=-\nabla\cdot\vec M\neq 0$, nên $\vec H$ không thoả một định lí Gauss tầm thường và lực Lorentz vẫn tính theo $\vec B$.

**Lỗi thường gặp:**
- Cho rằng $\vec H$ luôn bằng $\vec B/\mu_0$ nhân một hằng số. Với sắt từ, quan hệ $B(H)$ phi tuyến và có trễ nên $\mu_r$ không phải hằng số mà phụ thuộc cả lịch sử từ hóa.
- Quên rằng thế vectơ chỉ xác định sai khác một gradient, rồi gán ý nghĩa vật lí trực tiếp cho từng giá trị của $\vec A$. Chỉ các đại lượng bất biến chuẩn — $\vec B$ và tích phân $\oint\vec A\cdot d\vec l$ — mới đo được.
- Dùng định luật Ampère dạng tĩnh $\nabla\times\vec B=\mu_0\vec J$ cho dòng biến thiên. Khi $\partial\vec E/\partial t\neq 0$, phương trình này mâu thuẫn với bảo toàn điện tích và phải bổ sung dòng điện dịch.

<sub>`lesson.physics.dien-dong-luc-hoc.tinh-tu-the-vecto-va-vat-lieu-tu`</sub>

---

### 5. Dòng điện dịch và hệ phương trình Maxwell đầy đủ
*Displacement current and the complete Maxwell equations* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Chứng minh được sự cần thiết của dòng điện dịch từ phương trình liên tục
- Viết được hệ phương trình Maxwell ở dạng vi phân và tích phân
- Suy ra được phương trình sóng cho E và B trong chân không

## Một mâu thuẫn buộc phải sửa lí thuyết

Lấy divergence hai vế của $\nabla\times\vec B=\mu_0\vec J$ cho $0=\mu_0\nabla\cdot\vec J$. Nhưng bảo toàn điện tích đòi hỏi $\nabla\cdot\vec J=-\partial\rho/\partial t$, nói chung khác không — hãy nghĩ tới tụ điện đang nạp: dòng chạy vào bản tụ nhưng không đi qua khe. Vậy định luật Ampère chỉ đúng cho dòng dừng.

## Sửa như thế nào

Thay $\rho$ bằng $\varepsilon_0\nabla\cdot\vec E$:

$$\nabla\cdot\vec J+\frac{\partial}{\partial t}\left(\varepsilon_0\nabla\cdot\vec E\right)=\nabla\cdot\left(\vec J+\varepsilon_0\frac{\partial\vec E}{\partial t}\right)=0$$

Tổ hợp trong ngoặc mới là thứ có divergence bằng 0. Vậy phải viết

$$\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}$$

Với tụ đang nạp, dòng điện dịch trong khe đúng bằng dòng dẫn trong dây, nên định luật Ampère cho cùng một kết quả bất kể chọn mặt nào tựa lên vòng kín.

## Hệ đầy đủ

$$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0},\quad \nabla\cdot\vec B=0,\quad \nabla\times\vec E=-\frac{\partial\vec B}{\partial t},\quad \nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}$$

## Hệ quả tức thì: sóng

Trong chân không ($\rho=0,\vec J=0$), lấy curl phương trình Faraday và dùng $\nabla\times(\nabla\times\vec E)=\nabla(\nabla\cdot\vec E)-\nabla^2\vec E$:

$$\nabla^2\vec E=\mu_0\varepsilon_0\frac{\partial^2\vec E}{\partial t^2}$$

Đó là phương trình sóng với $c=1/\sqrt{\mu_0\varepsilon_0}$. Giá trị số trùng vận tốc ánh sáng đo được — kết luận rằng ánh sáng là sóng điện từ đến từ đây, không cần giả thiết thêm.

**Lỗi thường gặp:**
- Gọi dòng điện dịch là "dòng điện tích chạy trong chân không". Không có hạt mang điện nào chuyển động; đó là số hạng do điện trường biến thiên, chỉ giống dòng thật ở chỗ sinh ra từ trường.
- Cho rằng dòng điện dịch chỉ tồn tại trong tụ điện. Bất kì nơi nào $\partial\vec E/\partial t\neq 0$ — kể cả trong sóng điện từ truyền trong chân không — đều có nó; thực ra trong sóng thì đó là số hạng duy nhất.
- Dùng $\nabla\times\vec E=0$ trong bài toán có từ trường biến thiên rồi định nghĩa điện thế như tĩnh điện. Khi $\partial\vec B/\partial t\neq0$, điện trường có xoáy nên tích phân $\oint\vec E\cdot d\vec l$ khác không và khái niệm hiệu điện thế mất tính đơn trị.

<sub>`lesson.physics.dien-dong-luc-hoc.dong-dien-dich-va-he-maxwell`</sub>

---

### 6. Định lí Poynting, năng lượng và động lượng của trường
*Poynting's theorem, field energy and momentum* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Chứng minh được định lí Poynting từ hệ phương trình Maxwell
- Giải thích được ý nghĩa vật lí của vectơ Poynting và mật độ năng lượng trường
- Tính được áp suất bức xạ từ mật độ động lượng của trường điện từ

## Trường có mang năng lượng hay không

Nếu năng lượng chỉ thuộc về các hạt thì trong khoảng thời gian một tín hiệu rời ăng-ten mà chưa tới máy thu, năng lượng ở đâu? Định lí Poynting trả lời: nó nằm trong trường, và trường vận chuyển nó.

## Dẫn ra định lí

Công suất mà trường thực hiện lên các hạt là $\int\vec J\cdot\vec E\,dV$. Thay $\vec J$ từ phương trình Ampère - Maxwell rồi dùng đồng nhất thức $\nabla\cdot(\vec E\times\vec B)=\vec B\cdot(\nabla\times\vec E)-\vec E\cdot(\nabla\times\vec B)$:

$$-\frac{\partial u}{\partial t}=\nabla\cdot\vec S+\vec J\cdot\vec E,\qquad u=\frac{\varepsilon_0E^2}{2}+\frac{B^2}{2\mu_0},\quad \vec S=\frac{\vec E\times\vec B}{\mu_0}$$

Đọc như một phương trình liên tục: năng lượng trường giảm đi hoặc là do chảy ra ngoài qua mặt biên ($\nabla\cdot\vec S$), hoặc là do chuyển sang cho hạt ($\vec J\cdot\vec E$).

## Kiểm chứng trực quan

Với dây dẫn có điện trở mang dòng $I$: $\vec E$ dọc dây, $\vec B$ vòng quanh, nên $\vec S$ hướng **vào trong** dây từ mọi phía. Tích phân $\vec S$ trên mặt trụ cho đúng $I^2R$. Năng lượng Joule không chạy dọc trong dây mà đi qua không gian xung quanh rồi mới rót vào — đây là bức tranh vật lí đúng.

## Động lượng và áp suất bức xạ

Trường mang cả động lượng, với mật độ $\vec g=\varepsilon_0\,\vec E\times\vec B=\vec S/c^2$. Sóng phẳng đập vuông góc lên mặt hấp thụ hoàn toàn gây áp suất $p=\dfrac{\langle S\rangle}{c}=\dfrac{I}{c}$; nếu phản xạ toàn phần thì gấp đôi. Chỉ khi cộng cả động lượng của trường thì định luật bảo toàn động lượng mới đúng cho hệ hạt + trường.

## Lưu ý

$u$ và $\vec S$ chỉ xác định tới một trường có divergence hoặc curl bằng 0; cách phân bố năng lượng "địa phương" không đo trực tiếp được. Điều đo được là tổng năng lượng và thông lượng qua mặt kín.

**Lỗi thường gặp:**
- Cho rằng năng lượng điện trong mạch chạy bên trong dây dẫn. Vectơ Poynting chỉ ra dòng năng lượng đi trong không gian quanh dây rồi mới thấm vào; điều này quan trọng khi phân tích đường truyền và cáp đồng trục ở tần số cao.
- Dùng $\vec S=\vec E\times\vec B/\mu_0$ trong môi trường vật chất. Trong môi trường phải dùng $\vec S=\vec E\times\vec H$, nếu không phần năng lượng dự trữ trong phân cực và từ hóa bị tính sai.
- Nhân trực tiếp giá trị tức thời $E_0B_0/\mu_0$ để lấy cường độ sóng. Cường độ là trung bình theo thời gian, với sóng điều hòa phải thêm hệ số $1/2$ do $\langle\cos^2\rangle=1/2$.

<sub>`lesson.physics.dien-dong-luc-hoc.dinh-li-poynting-va-dong-luong-truong`</sub>

---

### 7. Sóng điện từ trong chân không và trong môi trường
*Electromagnetic waves in vacuum and in matter* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Chứng minh được tính ngang và quan hệ pha giữa E và B trong sóng phẳng
- Phân tích được sự truyền sóng trong môi trường tán sắc qua chiết suất phức
- Tính được độ thấm sâu của sóng trong vật dẫn tốt

## Cấu trúc của sóng phẳng trong chân không

Thay $\vec E=\vec E_0e^{i(\vec k\cdot\vec r-\omega t)}$ vào hệ Maxwell. Hai phương trình divergence cho $\vec k\cdot\vec E_0=0$ và $\vec k\cdot\vec B_0=0$: sóng là **ngang**. Phương trình Faraday cho

$$\vec B_0=\frac{\vec k\times\vec E_0}{\omega}\ \Longrightarrow\ B_0=\frac{E_0}{c}$$

nghĩa là $\vec E$, $\vec B$, $\vec k$ tạo thành tam diện thuận và hai trường **cùng pha**. Mật độ năng lượng chia đều cho hai phần điện và từ.

## Trong điện môi tuyến tính

Đổi $\varepsilon_0\to\varepsilon_0\varepsilon_r$, $\mu_0\to\mu_0\mu_r$: vận tốc pha $v=c/n$ với $n=\sqrt{\varepsilon_r\mu_r}$. Trở kháng sóng $Z=\sqrt{\mu/\varepsilon}$ (chân không: $377\ \Omega$) quyết định tỉ số $E/H$ và sẽ chi phối bài toán phản xạ.

## Tán sắc và hấp thụ

Ở tần số quang học, $\varepsilon_r$ phụ thuộc $\omega$ vì electron liên kết phản ứng như dao động tử cưỡng bức có tắt dần. Khi đó $\tilde n=n+i\kappa$ là số phức, và

$$\vec E\propto e^{-\kappa\omega z/c}\,e^{i(n\omega z/c-\omega t)}$$

Phần thực gây chậm pha (khúc xạ), phần ảo gây suy giảm; cường độ giảm theo $e^{-\alpha z}$ với $\alpha=2\kappa\omega/c$ — đó là định luật Beer. Vì $n$ phụ thuộc $\omega$ nên vận tốc pha khác vận tốc nhóm $v_g=d\omega/dk$; tín hiệu và năng lượng đi với $v_g$, và chỉ $v_g$ mới bị chặn bởi $c$.

## Trong vật dẫn

Thêm $\vec J=\sigma\vec E$ vào phương trình Ampère - Maxwell. Với vật dẫn tốt ($\sigma\gg\varepsilon\omega$), số sóng gần như $k\approx(1+i)/\delta$ với

$$\delta=\sqrt{\frac{2}{\mu\sigma\omega}}$$

Sóng tắt trong vài $\delta$; ở $50$ Hz đồng có $\delta\approx 9$ mm còn ở $1$ GHz chỉ $2\ \mu$m. Đây là cơ sở của hiệu ứng bề mặt và của việc kim loại phản xạ tốt ánh sáng. Ngoài ra $\vec E$ và $\vec B$ trong vật dẫn **lệch pha** $45^\circ$, khác hẳn chân không.

## Plasma

Với khí electron tự do không tắt dần, $\varepsilon(\omega)=1-\omega_p^2/\omega^2$: sóng có $\omega<\omega_p$ bị phản xạ toàn phần. Đó là lí do sóng vô tuyến AM dội lại từ tầng điện li còn sóng FM thì xuyên qua.

**Lỗi thường gặp:**
- Kết luận vận tốc pha lớn hơn $c$ là vi phạm thuyết tương đối. Vận tốc pha không truyền thông tin; ràng buộc tương đối tính áp lên vận tốc nhóm và vận tốc tín hiệu.
- Dùng $B_0=E_0/c$ trong mọi môi trường. Quan hệ đúng là $B_0=E_0/v=nE_0/c$; trong vật dẫn còn thêm lệch pha nên hai trường thậm chí không đạt cực đại cùng lúc.
- Cho rằng độ thấm sâu chỉ quan trọng ở tần số cao. Ngay ở 50 Hz, đồng chỉ có $\delta\approx9$ mm, nên trong một thanh dẫn tiết diện lớn phần lõi hầu như không mang dòng; đó là lí do dây tải điện cỡ lớn được bện từ nhiều sợi hoặc làm rỗng ruột.

<sub>`lesson.physics.dien-dong-luc-hoc.song-dien-tu-trong-chan-khong-va-moi-truong`</sub>

---

### 8. Phản xạ, khúc xạ và hệ số Fresnel
*Reflection, refraction and the Fresnel coefficients* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Suy ra được định luật Snell từ điều kiện biên của trường điện từ
- Tính được hệ số phản xạ và truyền qua cho phân cực s và p
- Giải thích được góc Brewster và phản xạ toàn phần bằng hệ số Fresnel

## Mọi thứ đến từ điều kiện biên

Ở mặt phân cách, thành phần tiếp tuyến của $\vec E$ và $\vec H$ phải liên tục **tại mọi điểm và mọi thời điểm**. Yêu cầu này chỉ thoả được nếu ba sóng (tới, phản xạ, khúc xạ) có cùng $\omega$ và cùng thành phần tiếp tuyến của $\vec k$. Từ đó suy ra ngay:

$$\theta_r=\theta_i,\qquad n_1\sin\theta_i=n_2\sin\theta_t$$

Định luật phản xạ và Snell không phải tiên đề riêng — chúng là hệ quả động học của điều kiện biên.

## Biên độ: công thức Fresnel

Áp phần **động lực** của điều kiện biên cho từng phân cực (với $\mu\approx\mu_0$):

$$r_s=\frac{n_1\cos\theta_i-n_2\cos\theta_t}{n_1\cos\theta_i+n_2\cos\theta_t},\qquad r_p=\frac{n_2\cos\theta_i-n_1\cos\theta_t}{n_2\cos\theta_i+n_1\cos\theta_t}$$

Độ phản xạ theo năng lượng là $R=|r|^2$; độ truyền qua $T=1-R$ chứ **không** phải $|t|^2$, vì tiết diện chùm và vận tốc thay đổi khi qua mặt phân cách.

## Hai hiện tượng đặc biệt

**Brewster**: $r_p=0$ khi $\theta_i+\theta_t=90^\circ$, tức $\tan\theta_B=n_2/n_1$. Lí do vật lí: các lưỡng cực trong môi trường 2 dao động dọc theo hướng lẽ ra là hướng phản xạ, mà lưỡng cực không bức xạ dọc trục của nó. Ánh sáng phản xạ khi đó phân cực s hoàn toàn — nguyên lí của kính phân cực chống loá.

**Phản xạ toàn phần**: khi $n_1>n_2$ và $\theta_i>\theta_c=\arcsin(n_2/n_1)$, $\cos\theta_t$ trở thành thuần ảo, $|r|=1$. Sóng trong môi trường 2 là sóng **evanescent**, tắt theo hàm mũ và không mang năng lượng đi trung bình, nhưng vẫn tồn tại — cơ sở của cảm biến trường gần và của hiệu ứng "đường ngầm quang học".

## Ở tới vuông góc

$R=\left(\dfrac{n_1-n_2}{n_1+n_2}\right)^2$; với không khí - thuỷ tinh cho $R\approx 4\%$ mỗi mặt, lí do các ống kính nhiều thấu kính phải phủ lớp chống phản xạ.

**Lỗi thường gặp:**
- Viết $T=|t|^2$. Truyền qua theo năng lượng phải tính theo thông lượng: $T=\dfrac{n_2\cos\theta_t}{n_1\cos\theta_i}|t|^2$; dùng $|t|^2$ trực tiếp sẽ vi phạm bảo toàn năng lượng.
- Cho rằng trong phản xạ toàn phần không có trường ở môi trường thứ hai. Sóng evanescent tồn tại và thấm sâu cỡ bước sóng; đưa một môi trường chiết quang khác lại gần sẽ hút được năng lượng qua khe, đúng như hiệu ứng đường ngầm.
- Áp dụng góc Brewster cho phân cực s. Chỉ $r_p$ mới triệt tiêu; $r_s$ đơn điệu tăng theo góc tới và không bao giờ bằng không với hai điện môi thông thường.

<sub>`lesson.physics.dien-dong-luc-hoc.phan-xa-khuc-xa-va-he-so-fresnel`</sub>

---

### 9. Ống dẫn sóng, mode TE-TM và tần số cắt
*Waveguides, TE/TM modes and cut-off frequency* · Đại học · intl-undergrad · 55 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao ống dẫn sóng kim loại không truyền được mode TEM
- Tính được tần số cắt của các mode TE trong ống chữ nhật
- Phân biệt được vận tốc pha và vận tốc nhóm trong ống dẫn sóng

## Vì sao ống kim loại rỗng không dẫn được sóng TEM

Trong ống dẫn kim loại lí tưởng, $E_\parallel=0$ trên thành. Nếu giả sử mode TEM ($E_z=B_z=0$) thì bài toán mặt cắt ngang trở thành bài toán tĩnh điện hai chiều với biên đẳng thế duy nhất, mà nghiệm duy nhất là $\vec E=0$. Kết luận: ống rỗng đơn liên **không** truyền được TEM; cần hai vật dẫn tách biệt (cáp đồng trục) mới có TEM. Ống rỗng chỉ truyền được TE hoặc TM.

## Bài toán mặt cắt ngang

Viết trường dạng $e^{i(k_zz-\omega t)}$ và tách thành phần dọc. Với mode TE trong ống chữ nhật $a\times b$, $B_z$ thoả phương trình Helmholtz hai chiều với điều kiện $\partial B_z/\partial n=0$ trên thành:

$$B_z\propto\cos\frac{m\pi x}{a}\cos\frac{n\pi y}{b},\qquad k_z^2=\frac{\omega^2}{c^2}-\left(\frac{m\pi}{a}\right)^2-\left(\frac{n\pi}{b}\right)^2$$

## Tần số cắt

$k_z$ thực chỉ khi

$$\omega>\omega_{mn}=c\pi\sqrt{\left(\frac{m}{a}\right)^2+\left(\frac{n}{b}\right)^2}$$

Dưới ngưỡng, $k_z$ thuần ảo và trường tắt dần — ống hoạt động như bộ lọc thông cao. Mode có tần số cắt thấp nhất (mode chủ) là TE$_{10}$ với $\omega_{10}=\pi c/a$, tương ứng $\lambda_c=2a$: bước sóng không được dài hơn hai lần cạnh lớn.

## Tán sắc

Từ hệ thức tán sắc, $v_p=\dfrac{\omega}{k_z}=\dfrac{c}{\sqrt{1-\omega_{mn}^2/\omega^2}}>c$ còn $v_g=\dfrac{d\omega}{dk_z}=c\sqrt{1-\omega_{mn}^2/\omega^2}<c$, và $v_pv_g=c^2$. Vận tốc pha vượt $c$ không mâu thuẫn gì: năng lượng đi với $v_g$. Bức tranh trực quan là sóng phẳng nảy zigzag giữa hai thành, đường đi thực dài hơn nên tiến dọc trục chậm hơn $c$.

## Hệ quả kĩ thuật

Vì $v_g$ phụ thuộc $\omega$, xung bị giãn khi truyền — giới hạn băng thông. Ống dẫn sóng thường được thiết kế làm việc trong dải chỉ có mode chủ, để tránh nhiều mode chạy với vận tốc khác nhau làm méo tín hiệu.

**Lỗi thường gặp:**
- Cho rằng ống dẫn sóng truyền được mọi tần số như cáp đồng trục. Ống rỗng có tần số cắt vì không tồn tại mode TEM; cáp đồng trục có hai vật dẫn nên truyền được xuống tận một chiều.
- Kết luận $v_p>c$ vi phạm thuyết tương đối. Vận tốc pha chỉ mô tả tốc độ dịch chuyển của mặt đồng pha, không mang thông tin; tín hiệu đi với $v_g<c$.
- Xem tần số cắt chỉ phụ thuộc cạnh lớn. Điều đó chỉ đúng cho TE$_{10}$; với mode tổng quát cả hai kích thước đều vào công thức, và thiết kế dải đơn mode đòi hỏi so sánh tần số cắt của tất cả các mode thấp.

<sub>`lesson.physics.dien-dong-luc-hoc.ong-dan-song`</sub>

---

### 10. Thế trễ và bức xạ lưỡng cực
*Retarded potentials and dipole radiation* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Viết được nghiệm thế trễ của phương trình sóng không thuần nhất
- Thiết lập được công suất bức xạ của lưỡng cực điện dao động
- Giải thích được phụ thuộc bậc bốn vào tần số và ứng dụng vào màu trời

## Từ Maxwell tới phương trình sóng cho thế

Viết $\vec B=\nabla\times\vec A$, $\vec E=-\nabla V-\partial\vec A/\partial t$ rồi chọn chuẩn Lorenz. Hai phương trình còn lại thành

$$\Box V=-\frac{\rho}{\varepsilon_0},\qquad \Box\vec A=-\mu_0\vec J,\qquad \Box\equiv\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}$$

Nghiệm là thế tĩnh quen thuộc nhưng **lấy nguồn ở thời điểm trễ**:

$$V(\vec r,t)=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vec r\,',t_r)}{|\vec r-\vec r\,'|}dV',\qquad t_r=t-\frac{|\vec r-\vec r\,'|}{c}$$

Ý nghĩa: thông tin về nguồn lan với tốc độ $c$. Nghiệm "tiến" (advanced) cũng thoả phương trình nhưng bị loại vì vi phạm nhân quả.

## Lưỡng cực dao động

Với $\vec p(t)=p_0\cos\omega t\,\hat z$ và ở vùng xa ($r\gg\lambda$), giữ lại các số hạng giảm như $1/r$ — chỉ chúng mới mang năng lượng ra vô cùng, vì $S\sim E^2\sim1/r^2$ vừa đủ bù diện tích mặt cầu $4\pi r^2$. Kết quả:

$$\langle P\rangle=\frac{\mu_0 p_0^2\omega^4}{12\pi c},\qquad \frac{d\langle P\rangle}{d\Omega}\propto\sin^2\theta$$

Đọc hai điều: không có bức xạ dọc trục lưỡng cực ($\theta=0$), và công suất tỉ lệ $\omega^4$.

## Hệ quả của luật $\omega^4$

Ánh sáng xanh (bước sóng ngắn) bị phân tử khí quyển tán xạ mạnh hơn ánh sáng đỏ khoảng $(700/450)^4\approx 6$ lần — bầu trời xanh, hoàng hôn đỏ. Cùng công thức giải thích vì sao ăng-ten ngắn kém hiệu quả ở tần số thấp.

## Điện tích gia tốc

Với một hạt điểm, thế Liénard - Wiechert cho công thức Larmor $P=\dfrac{q^2a^2}{6\pi\varepsilon_0c^3}$, mở rộng tương đối tính thành công thức Liénard. Chính bức xạ này làm nguyên tử cổ điển không thể bền: electron quay quanh hạt nhân sẽ rơi vào trong khoảng $10^{-11}$ s — một trong những lí do buộc phải có cơ học lượng tử.

**Lỗi thường gặp:**
- Dùng thế tĩnh điện Coulomb cho nguồn biến thiên nhanh. Bỏ qua thời gian trễ chỉ hợp lệ khi kích thước hệ nhỏ hơn nhiều bước sóng; ngược lại toàn bộ hiệu ứng bức xạ biến mất khỏi kết quả.
- Giữ lại các số hạng $1/r^2$ khi tính công suất bức xạ. Chúng thuộc vùng gần, đóng góp $S\sim1/r^4$ nên tích phân trên mặt cầu tiến tới 0; chỉ số hạng $1/r$ mới mang năng lượng ra vô cùng.
- Cho rằng điện tích chuyển động đều cũng bức xạ. Trường của điện tích chuyển động thẳng đều mang theo nó và không có phần $1/r$; chỉ gia tốc mới sinh bức xạ.

<sub>`lesson.physics.dien-dong-luc-hoc.the-tre-va-buc-xa-luong-cuc`</sub>

---

### 11. Điện động lực học tương đối tính: tenxơ trường và biến đổi
*Relativistic electrodynamics: field tensor and transformations* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Viết được hệ phương trình Maxwell ở dạng hiệp biến qua tenxơ trường
- Vận dụng được công thức biến đổi E và B giữa hai hệ quy chiếu quán tính
- Giải thích được vì sao điện trường và từ trường là hai mặt của một thực thể duy nhất

## Vì sao điện học và từ học phải hợp nhất

Xét một điện tích đứng yên trong hệ $K$: chỉ có điện trường. Trong hệ $K'$ chuyển động, điện tích đó là một dòng điện, và ta đo được cả từ trường. Vậy việc "có từ trường hay không" phụ thuộc hệ quy chiếu — hai trường không thể là hai thực thể độc lập.

## Dạng hiệp biến

Gộp $A^\mu=(V/c,\vec A)$ và $J^\mu=(c\rho,\vec J)$. Đặt

$$F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$$

thì, với metric $(+,-,-,-)$, $F^{0i}=-E_i/c$ (tức $F^{i0}=+E_i/c$) và $F^{ij}=-\epsilon_{ijk}B_k$. Dấu này bị ràng buộc bởi chính hai phương trình dưới đây; sách dùng metric ngược dấu sẽ đảo dấu cả ma trận, nên luôn phải kiểm tra quy ước trước khi so công thức. Toàn bộ hệ Maxwell rút gọn thành hai phương trình:

$$\partial_\mu F^{\mu\nu}=\mu_0J^\nu,\qquad \partial^\lambda F^{\mu\nu}+\partial^\mu F^{\nu\lambda}+\partial^\nu F^{\lambda\mu}=0$$

Phương trình thứ nhất chứa Gauss và Ampère - Maxwell; phương trình thứ hai (đồng nhất thức Bianchi) chứa $\nabla\cdot\vec B=0$ và Faraday. Bảo toàn điện tích $\partial_\mu J^\mu=0$ là hệ quả tự động của tính phản đối xứng.

## Biến đổi trường

Với hệ $K'$ chuyển động vận tốc $v$ dọc $x$:

$$E'_x=E_x,\quad E'_y=\gamma(E_y-vB_z),\quad E'_z=\gamma(E_z+vB_y)$$
$$B'_x=B_x,\quad B'_y=\gamma\!\left(B_y+\frac{v}{c^2}E_z\right),\quad B'_z=\gamma\!\left(B_z-\frac{v}{c^2}E_y\right)$$

Thành phần dọc phương chuyển động không đổi; thành phần ngang trộn lẫn.

## Hai bất biến và điều chúng cấm

$$E^2-c^2B^2=\text{const},\qquad \vec E\cdot\vec B=\text{const}$$

Hệ quả rất mạnh: nếu trong một hệ $\vec E\perp\vec B$ và $E=cB$ (sóng phẳng) thì điều đó đúng trong **mọi** hệ — không thể "đứng yên cùng" sóng ánh sáng. Nếu $E>cB$ ở đâu đó thì không hệ nào làm $\vec E$ triệt tiêu được.

## Lực Lorentz hiệp biến

$$\frac{dp^\mu}{d\tau}=qF^{\mu\nu}u_\nu$$

Từ đây thấy rõ lực Lorentz không phải hai định luật ghép lại mà là một công thức duy nhất.

**Lỗi thường gặp:**
- Cho rằng có thể tìm hệ quy chiếu mà sóng điện từ đứng yên. Bất biến $E^2-c^2B^2=0$ và $\vec E\cdot\vec B=0$ của sóng phẳng giữ nguyên trong mọi hệ, nên không hệ nào làm trường triệt tiêu.
- Biến đổi $\vec E$ và $\vec B$ như hai vectơ ba chiều độc lập. Chúng là các thành phần của một tenxơ hạng hai; chỉ khi biến đổi đồng thời theo đúng công thức mới thu được kết quả nhất quán.
- Nghĩ rằng cần vận tốc gần $c$ thì hiệu ứng tương đối tính mới xuất hiện trong điện từ học. Vận tốc trôi của electron trong dây chỉ cỡ mm/s, vậy mà toàn bộ từ trường của dòng điện chính là hiệu ứng tương đối tính — nó không nhỏ vì lực Coulomb vốn cực mạnh.

<sub>`lesson.physics.dien-dong-luc-hoc.dien-dong-luc-tuong-doi-tinh`</sub>

---

## Unit 3: Cơ học lượng tử

### 1. Nguồn gốc thực nghiệm của cơ học lượng tử
*Experimental origins of quantum mechanics* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được vì sao vật lí cổ điển thất bại trước bức xạ vật đen và hiệu ứng quang điện
- Phân tích được ý nghĩa lượng tử của hiệu ứng Compton và giả thuyết de Broglie
- Vận dụng được các hệ thức lượng tử cơ bản để tính năng lượng và động lượng photon

## Bốn thí nghiệm phá vỡ vật lí cổ điển

**Bức xạ vật đen.** Áp dụng định lí phân bố đều năng lượng cho vô số mode sóng dừng trong hốc, Rayleigh - Jeans thu được $u_\nu\propto\nu^2T$, phân kì khi $\nu\to\infty$ — "khủng hoảng tử ngoại". Planck sửa được bằng cách giả thiết mỗi dao động tử chỉ trao đổi năng lượng theo bội của $h\nu$, cho

$$u_\nu=\frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT}-1}$$

Cơ chế: các mode tần số cao cần một gói năng lượng $h\nu\gg k_BT$ nên hầu như bị "đóng băng".

**Hiệu ứng quang điện.** Cổ điển tiên đoán động năng electron tăng theo cường độ và có độ trễ. Thực nghiệm cho $K_{\max}=h\nu-A$: động năng chỉ phụ thuộc **tần số**, dưới ngưỡng thì không có electron dù chiếu sáng bao lâu. Ánh sáng trao đổi năng lượng theo từng gói.

**Hiệu ứng Compton.** Tia X tán xạ trên electron tự do đổi bước sóng: $\Delta\lambda=\dfrac{h}{m_ec}(1-\cos\theta)$. Kết quả này suy ra được từ bảo toàn năng lượng - động lượng khi coi photon là hạt có $p=h/\lambda$. Đây là bằng chứng photon mang **động lượng**, mạnh hơn cả quang điện.

**Sóng vật chất.** De Broglie đề xuất $\lambda=h/p$ cho mọi hạt; Davisson - Germer thấy electron nhiễu xạ trên tinh thể niken đúng theo định luật Bragg.

## Bài học chung

Không phải "ánh sáng là hạt" hay "electron là sóng", mà là: mọi đối tượng lượng tử có cả hai mặt, và cái quyết định biểu hiện nào xuất hiện chính là **cách bố trí thí nghiệm**. Điều kiện để hiệu ứng lượng tử rõ rệt: bước sóng de Broglie so sánh được với kích thước đặc trưng của hệ. Với hạt bụi ở nhiệt độ phòng, $\lambda$ nhỏ hơn kích thước nguyên tử nhiều bậc độ lớn, nên vật lí cổ điển vẫn đúng.

**Lỗi thường gặp:**
- Cho rằng tăng cường độ ánh sáng sẽ giúp bứt electron ngay cả dưới tần số ngưỡng. Mỗi electron hấp thụ một photon; tăng cường độ chỉ tăng số photon chứ không tăng năng lượng từng gói.
- Dùng $\Delta\lambda$ Compton cho electron liên kết chặt trong nguyên tử nặng. Công thức giả thiết electron tự do và đứng yên; với electron liên kết mạnh, photon tán xạ trên cả nguyên tử nên độ dịch nhỏ hơn hàng nghìn lần.
- Áp dụng $\lambda=h/p$ với $p=mv$ cho hạt chuyển động gần tốc độ ánh sáng. Phải dùng động lượng tương đối tính $p=\gamma mv$, nếu không bước sóng tính ra lớn hơn thực tế đáng kể.

<sub>`lesson.physics.co-hoc-luong-tu.nguon-goc-thuc-nghiem-cua-luong-tu`</sub>

---

### 2. Hàm sóng, diễn giải xác suất và chuẩn hóa
*The wave function, probability interpretation and normalization* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Giải thích được ý nghĩa xác suất của bình phương môđun hàm sóng
- Áp dụng được điều kiện chuẩn hóa và điều kiện liên tục cho hàm sóng
- Chứng minh được phương trình liên tục cho mật độ xác suất

## Hàm sóng nói lên điều gì

Born đề xuất: $|\Psi(\vec r,t)|^2\,d^3r$ là xác suất tìm thấy hạt trong thể tích $d^3r$. Đây là bước ngoặt khái niệm — lí thuyết không cho biết hạt *ở đâu*, chỉ cho biết xác suất. Bản thân $\Psi$ là số phức và không đo được; pha toàn cục $e^{i\alpha}$ không mang thông tin, nhưng **hiệu pha** giữa các thành phần chồng chất lại quyết định giao thoa.

## Điều kiện chuẩn hóa

Vì hạt phải ở đâu đó:

$$\int|\Psi|^2\,d^3r=1$$

Điều này đòi hỏi $\Psi$ khả bình phương, tự động loại các nghiệm phân kì. Đáng chú ý: phương trình Schrödinger bảo toàn chuẩn hóa theo thời gian, nên chỉ cần chuẩn hóa một lần.

## Điều kiện chính quy

$\Psi$ phải liên tục ở mọi nơi; $\partial\Psi/\partial x$ liên tục trừ nơi thế có kì dị vô hạn. Hai điều kiện này chính là thứ tạo ra sự **lượng tử hóa**: chỉ với các giá trị năng lượng rời rạc thì nghiệm mới ghép trơn được ở các biên.

## Phương trình liên tục

Từ phương trình Schrödinger và liên hợp phức của nó:

$$\frac{\partial|\Psi|^2}{\partial t}+\nabla\cdot\vec j=0,\qquad \vec j=\frac{\hbar}{2mi}\left(\Psi^*\nabla\Psi-\Psi\nabla\Psi^*\right)$$

Xác suất không tự sinh hay mất, chỉ chảy — đúng như điện tích trong điện động lực học. Chú ý $\vec j=0$ với mọi hàm sóng thực, nên trạng thái liên kết mô tả bởi hàm thực không có dòng xác suất.

## Trị trung bình

$$\langle x\rangle=\int\Psi^*x\Psi\,d^3r,\qquad \langle p\rangle=\int\Psi^*\left(-i\hbar\nabla\right)\Psi\,d^3r$$

Đây **không** phải trung bình theo thời gian của một hạt, mà là trung bình trên nhiều lần đo lặp lại trên các hệ chuẩn bị giống hệt nhau.

**Lỗi thường gặp:**
- Coi $|\Psi|^2$ là mật độ khối lượng hay điện tích trải ra trong không gian. Mỗi phép đo luôn tìm thấy hạt trọn vẹn ở một điểm; $|\Psi|^2$ mô tả thống kê của nhiều lần đo chứ không phải một vật thể bị trải mỏng.
- Cộng xác suất thay vì cộng biên độ cho các đường đi khả dĩ. Nếu không phân biệt được đường nào thì phải cộng $\Psi$ rồi mới bình phương; cộng $|\Psi_i|^2$ làm mất hẳn số hạng giao thoa.
- Bỏ qua điều kiện liên tục của đạo hàm khi ghép nghiệm ở biên. Chính điều kiện này chọn ra tập năng lượng rời rạc; bỏ nó đi thì mọi năng lượng đều có vẻ hợp lệ và phổ không còn lượng tử hóa.

<sub>`lesson.physics.co-hoc-luong-tu.ham-song-va-dien-giai-xac-suat`</sub>

---

### 3. Phương trình Schrödinger, toán tử và bài toán trị riêng
*The Schrödinger equation, operators and eigenvalue problems* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Viết được phương trình Schrödinger phụ thuộc và không phụ thuộc thời gian
- Giải thích được vì sao đại lượng quan sát được biểu diễn bằng toán tử Hermite
- Khai triển được trạng thái bất kì theo hệ trạng thái riêng và tính xác suất kết quả đo

## Phương trình động lực

$$i\hbar\frac{\partial\Psi}{\partial t}=\hat H\Psi,\qquad \hat H=-\frac{\hbar^2}{2m}\nabla^2+V(\vec r,t)$$

Phương trình bậc nhất theo thời gian: biết $\Psi$ ở một thời điểm là biết mọi thời điểm sau — lí thuyết vẫn tất định, chỉ có kết quả **đo** mới ngẫu nhiên.

## Tách biến và trạng thái dừng

Khi $V$ không phụ thuộc $t$, thử $\Psi=\psi(\vec r)f(t)$ dẫn tới

$$\hat H\psi=E\psi,\qquad f(t)=e^{-iEt/\hbar}$$

Nghiệm riêng gọi là trạng thái dừng vì $|\Psi|^2=|\psi|^2$ không đổi theo thời gian. Nghiệm tổng quát là chồng chất

$$\Psi(\vec r,t)=\sum_n c_n\psi_n(\vec r)e^{-iE_nt/\hbar}$$

Chú ý các số hạng có pha quay với tốc độ khác nhau, nên $|\Psi|^2$ của một chồng chất **có** phụ thuộc thời gian — đó là nguồn gốc của mọi chuyển động lượng tử.

## Toán tử và phép đo

Mỗi đại lượng quan sát được ứng với một toán tử Hermite: $\hat x=x$, $\hat p=-i\hbar\nabla$, $\hat H$ như trên. Tính Hermite bảo đảm hai điều thiết yếu: trị riêng **thực** (kết quả đo là số thực) và hệ hàm riêng **đầy đủ, trực giao** (mọi trạng thái khai triển được).

Đo $\hat A$ chỉ có thể cho một trong các trị riêng $a_n$, với xác suất $|c_n|^2=|\langle\psi_n|\Psi\rangle|^2$; sau phép đo trạng thái sập về $\psi_n$. Trị trung bình $\langle A\rangle=\langle\Psi|\hat A|\Psi\rangle$.

## Giao hoán tử

$[\hat x,\hat p]=i\hbar$. Hai toán tử giao hoán mới có hệ hàm riêng chung, tức mới đo đồng thời chính xác được. Định lí Ehrenfest cho thấy $\dfrac{d\langle\vec p\rangle}{dt}=-\langle\nabla V\rangle$: trị trung bình tuân theo dạng của định luật Newton, giải thích vì sao giới hạn cổ điển xuất hiện.

**Lỗi thường gặp:**
- Cho rằng mọi hàm sóng đều tiến hóa với một thừa số pha $e^{-iEt/\hbar}$. Chỉ trạng thái **dừng** mới như vậy; chồng chất có nhiều tần số khác nhau nên mật độ xác suất biến thiên.
- Đồng nhất $\langle A\rangle$ với kết quả một phép đo. Trị trung bình có thể là giá trị mà phép đo không bao giờ cho được, ví dụ $\langle E\rangle=(E_1+E_2)/2$ trong ví dụ trên không nằm trong phổ.
- Coi $\hat p=-i\hbar\partial/\partial x$ luôn có hàm riêng chuẩn hóa được. Hàm riêng $e^{ikx}$ không khả bình phương; phổ liên tục cần chuẩn hóa theo delta Dirac và các trạng thái vật lí phải là bó sóng.

<sub>`lesson.physics.co-hoc-luong-tu.phuong-trinh-schrodinger-va-toan-tu`</sub>

---

### 4. Hệ thức bất định Heisenberg
*The Heisenberg uncertainty relations* · Đại học · intl-undergrad · 50 phút · nang-cao

**Mục tiêu:**
- Phát biểu chính xác được hệ thức bất định vị trí - động lượng
- Chứng minh được hệ thức bất định tổng quát Robertson từ giao hoán tử
- Vận dụng được hệ thức bất định để ước lượng năng lượng trạng thái cơ bản

## Không phải sai số của dụng cụ

Hệ thức bất định **không** nói về sự vụng về của phép đo. Nó nói: không tồn tại trạng thái lượng tử nào mà cả $x$ lẫn $p$ đều có phân bố hẹp tuỳ ý. Đó là tính chất của trạng thái, không phải của máy đo.

## Dẫn ra hệ thức tổng quát

Với hai toán tử Hermite bất kì, dùng bất đẳng thức Schwarz cho hai vectơ $(\hat A-\langle A\rangle)|\Psi\rangle$ và $(\hat B-\langle B\rangle)|\Psi\rangle$, rồi tách phần thực - ảo:

$$\sigma_A\sigma_B\ge\frac{1}{2}\left|\langle[\hat A,\hat B]\rangle\right|$$

Áp dụng cho $[\hat x,\hat p]=i\hbar$:

$$\sigma_x\sigma_p\ge\frac{\hbar}{2}$$

Nguồn gốc toán học rất rõ: đây chính là quan hệ giữa độ rộng của một hàm và độ rộng biến đổi Fourier của nó. Trạng thái đạt dấu bằng là bó sóng Gauss.

## Hệ quả định lượng

Ước lượng năng lượng cơ bản: hạt bị nhốt trong miền $a$ có $p\sim\hbar/a$, nên $E\sim\dfrac{\hbar^2}{2ma^2}+V(a)$. Cực tiểu hoá theo $a$ cho ngay bậc độ lớn đúng — với nguyên tử hydro ta thu được cả bán kính Bohr lẫn $-13{,}6$ eV. Đây cũng là lời giải thích vật lí cho việc **nguyên tử bền**: nén electron lại gần hạt nhân làm động năng tăng nhanh hơn thế năng giảm.

## Bất định năng lượng - thời gian

$\Delta E\,\Delta t\ge\hbar/2$ có nghĩa khác hẳn, vì $t$ không phải toán tử: $\Delta t$ là thời gian đặc trưng để hệ thay đổi đáng kể. Hệ quả đo được là độ rộng tự nhiên của vạch phổ: trạng thái sống ngắn có mức năng lượng nhoè rộng.

## Điều cần nhớ

Chỉ các cặp **không giao hoán** mới bị ràng buộc. $\hat x$ và $\hat p_y$ giao hoán nên đo đồng thời được chính xác; ba thành phần mômen động lượng thì không.

**Lỗi thường gặp:**
- Hiểu hệ thức bất định là "đo vị trí làm nhiễu động lượng". Nhiễu loạn do phép đo là có thật nhưng là chuyện khác; hệ thức Robertson nói về độ tán của phân bố trong một trạng thái đã cho, ngay cả khi chưa đo gì.
- Áp dụng $\Delta E\Delta t\ge\hbar/2$ như một hệ thức Robertson thông thường. Không có toán tử thời gian trong cơ học lượng tử; hệ thức này phải được diễn giải qua tốc độ biến thiên của một đại lượng quan sát được.
- Kết luận mọi cặp đại lượng đều bất định. Nếu $[\hat A,\hat B]=0$ thì tồn tại trạng thái mà cả hai đều xác định chính xác; ví dụ năng lượng và mômen động lượng trong thế xuyên tâm.

<sub>`lesson.physics.co-hoc-luong-tu.he-thuc-bat-dinh`</sub>

---

### 5. Giếng thế một chiều: phổ rời rạc và trạng thái liên kết
*One-dimensional wells: discrete spectra and bound states* · Đại học · intl-undergrad · 55 phút · trung-binh

**Mục tiêu:**
- Giải được phương trình Schrödinger cho giếng thế vuông góc vô hạn
- Phân tích được bài toán giếng thế hữu hạn và phương trình siêu việt cho mức liên kết
- Giải thích được vì sao sự lượng tử hóa xuất phát từ điều kiện biên

## Giếng vô hạn: bài toán mẫu

Với $V=0$ trong $0<x<a$ và $V=\infty$ ngoài, hàm sóng phải triệt tiêu ở hai thành. Nghiệm $\psi=A\sin kx$ thoả $\psi(0)=0$; điều kiện $\psi(a)=0$ buộc $ka=n\pi$. Đây chính là **cơ chế của lượng tử hóa**: không phải một tiên đề riêng mà là hệ quả của việc buộc nghiệm khớp điều kiện biên, hệt như sóng dừng trên dây.

$$\psi_n=\sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a},\qquad E_n=\frac{n^2\pi^2\hbar^2}{2ma^2}$$

Ba đặc điểm cần đọc ra: $E_1\neq0$ (bất định không cho phép hạt "nằm yên"), khoảng cách mức tăng theo $n$, và $E\propto1/a^2$ nên hộp càng nhỏ hiệu ứng lượng tử càng rõ.

## Giếng hữu hạn: chỉ một số hữu hạn mức

Với $V=-V_0$ trong $|x|<a$ và $V=0$ ngoài, nghiệm bên trong dao động ($k=\sqrt{2m(E+V_0)}/\hbar$), bên ngoài tắt mũ ($\kappa=\sqrt{-2mE}/\hbar$). Ghép trơn $\psi$ và $\psi'$ tại $x=a$ cho phương trình siêu việt

$$k\tan(ka)=\kappa\quad(\text{nghiệm chẵn}),\qquad -k\cot(ka)=\kappa\quad(\text{nghiệm lẻ})$$

Chỉ giải được bằng đồ thị hoặc số. Kết luận vật lí quan trọng: số mức liên kết là **hữu hạn**, xấp xỉ $N\approx1+\left[\dfrac{2a\sqrt{2mV_0}}{\pi\hbar}\right]$. Tuy nhiên trong một chiều, giếng dù nông tới đâu cũng luôn có ít nhất một trạng thái liên kết — điều không còn đúng trong ba chiều.

## Điều tổng quát

Hàm sóng "rò" vào vùng cấm cổ điển với độ sâu $1/\kappa$; nó không dừng đột ngột ở điểm quay. Mức càng cao thì rò càng sâu, nên năng lượng thấp hơn giá trị của giếng vô hạn tương ứng.

**Lỗi thường gặp:**
- Cho rằng hạt trong giếng có thể có $E=0$. Trạng thái $n=0$ cho $\psi\equiv0$, tức không có hạt; hơn nữa hệ thức bất định cấm động lượng xác định bằng 0 khi vị trí bị giới hạn.
- Áp dụng công thức $E_n\propto n^2$ cho giếng hữu hạn. Ở giếng hữu hạn hàm sóng rò ra ngoài nên bước sóng hiệu dụng dài hơn, các mức thấp hơn công thức vô hạn và số mức bị chặn.
- Đòi hỏi $\psi'$ liên tục ở thành giếng vô hạn. Ở đó thế nhảy vô hạn nên chỉ $\psi$ phải liên tục; ép thêm điều kiện cho $\psi'$ sẽ dẫn tới kết luận không có nghiệm nào tồn tại.

<sub>`lesson.physics.co-hoc-luong-tu.gieng-the-mot-chieu`</sub>

---

### 6. Dao động tử điều hòa và phương pháp toán tử sinh - hủy
*Harmonic oscillator and the ladder-operator method* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Xây dựng được toán tử sinh và toán tử hủy từ x và p
- Suy ra được phổ năng lượng của dao động tử điều hòa bằng phương pháp đại số
- Vận dụng được biểu diễn x, p qua a và a† để tính phần tử ma trận

## Vì sao dao động tử quan trọng đến thế

Mọi thế năng gần cực tiểu đều xấp xỉ parabol. Vì vậy dao động tử mô tả được dao động phân tử, dao động mạng tinh thể (phonon), và cả từng mode của trường điện từ (photon). Giải được nó một lần là dùng lại ở khắp nơi.

## Mẹo đại số

Thay vì giải phương trình vi phân với đa thức Hermite, hãy "khai căn" Hamiltonian. Đặt

$$a=\frac{1}{\sqrt{2m\hbar\omega}}\left(m\omega \hat x+i\hat p\right),\qquad a^\dagger=\frac{1}{\sqrt{2m\hbar\omega}}\left(m\omega \hat x-i\hat p\right)$$

Từ $[\hat x,\hat p]=i\hbar$ suy ra $[a,a^\dagger]=1$ và

$$\hat H=\hbar\omega\left(a^\dagger a+\tfrac12\right)$$

## Thang trạng thái

Từ $[\hat H,a^\dagger]=\hbar\omega a^\dagger$ và $[\hat H,a]=-\hbar\omega a$: nếu $|n\rangle$ có năng lượng $E$ thì $a^\dagger|n\rangle$ có $E+\hbar\omega$ và $a|n\rangle$ có $E-\hbar\omega$. Vì $\langle n|a^\dagger a|n\rangle=\|a|n\rangle\|^2\ge0$, thang không thể đi xuống mãi: phải tồn tại $|0\rangle$ với $a|0\rangle=0$. Điều đó cho ngay

$$E_n=\hbar\omega\left(n+\tfrac12\right),\qquad a|n\rangle=\sqrt n\,|n-1\rangle,\qquad a^\dagger|n\rangle=\sqrt{n+1}\,|n+1\rangle$$

Toàn bộ phổ thu được mà không giải một phương trình vi phân nào — đó là sức mạnh của phương pháp đại số.

## Tính toán trở nên dễ

$$\hat x=\sqrt{\frac{\hbar}{2m\omega}}(a+a^\dagger),\qquad \hat p=i\sqrt{\frac{m\hbar\omega}{2}}(a^\dagger-a)$$

Mọi phần tử ma trận quy về đếm chỉ số. Ví dụ $\langle n|\hat x|m\rangle$ chỉ khác 0 khi $m=n\pm1$ — đó chính là **quy tắc lọc lựa** $\Delta n=\pm1$ cho chuyển mức lưỡng cực, giải thích vì sao phổ dao động phân tử có các vạch cách đều.

## Điều kiện áp dụng

Xấp xỉ điều hòa hỏng khi biên độ lớn: thế thật (ví dụ thế Morse) bất đối xứng và có giới hạn phân li, làm các mức cao xích lại gần nhau thay vì cách đều.

**Lỗi thường gặp:**
- Cho rằng $a$ và $a^\dagger$ là các đại lượng quan sát được. Chúng không Hermite ($a^\dagger\neq a$) nên trị riêng phức và không ứng với phép đo nào; chỉ các tổ hợp Hermite như $N=a^\dagger a$ mới đo được.
- Bỏ qua $\hbar\omega/2$ vì "chỉ là hằng số cộng". Năng lượng điểm không có hệ quả đo được thật: lực Casimir, sự tồn tại của heli lỏng ở 0 K, và độ dịch mức trong quang phổ.
- Dùng $\langle n|\hat x|n\rangle=0$ để kết luận hạt luôn ở gốc tọa độ. Trung bình bằng 0 do đối xứng, nhưng độ tán $\langle x^2\rangle$ khác 0 và tăng theo $n$; hạt trải rộng chứ không đứng yên.

<sub>`lesson.physics.co-hoc-luong-tu.dao-dong-tu-va-toan-tu-sinh-huy`</sub>

---

### 7. Hàng rào thế và hiệu ứng đường ngầm
*Potential barriers and quantum tunnelling* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Tính được hệ số truyền qua của hàng rào thế chữ nhật
- Vận dụng được xấp xỉ WKB cho hàng rào có hình dạng bất kì
- Giải thích được các hiện tượng vật lí dựa trên hiệu ứng đường ngầm

## Điều cổ điển cấm

Với $E<V_0$, cơ học cổ điển nói hạt bị phản xạ hoàn toàn. Trong cơ học lượng tử, phương trình Schrödinger trong vùng cấm có nghiệm tắt mũ $\psi\propto e^{-\kappa x}$ với $\kappa=\sqrt{2m(V_0-E)}/\hbar$ — hàm sóng nhỏ đi nhưng **không** bằng 0. Nếu hàng rào có bề rộng hữu hạn, biên độ còn lại ở đầu kia khác không, nên có dòng truyền qua.

## Hàng rào chữ nhật

Ghép $\psi$ và $\psi'$ ở hai biên cho

$$T=\left[1+\frac{V_0^2\sinh^2(\kappa a)}{4E(V_0-E)}\right]^{-1}\xrightarrow{\ \kappa a\gg1\ }16\frac{E}{V_0}\left(1-\frac{E}{V_0}\right)e^{-2\kappa a}$$

Điều quan trọng nhất nằm ở số mũ: $T$ **giảm theo hàm mũ** theo bề rộng và theo $\sqrt{m}$. Vì thế đường ngầm là hiệu ứng của hạt nhẹ (electron, proton) qua hàng rào mỏng; với vật vĩ mô $T$ nhỏ tới mức vô nghĩa.

## Hàng rào bất kì: WKB

Chia hàng rào thành nhiều lát mỏng, mỗi lát đóng góp một thừa số tắt:

$$T\approx\exp\left[-\frac{2}{\hbar}\int_{x_1}^{x_2}\sqrt{2m\left(V(x)-E\right)}\,dx\right]$$

Điều kiện áp dụng: thế biến thiên chậm trên một bước sóng de Broglie, và công thức kém chính xác ngay tại các điểm quay.

## Ba ứng dụng quyết định

**Phân rã alpha.** Hạt alpha bị nhốt trong giếng hạt nhân, phải chui qua rào Coulomb. WKB cho ngay quy luật Geiger - Nuttall: chu kì bán rã phụ thuộc năng lượng alpha theo hàm mũ, trải dài hơn 20 bậc độ lớn.

**Kính hiển vi quét đường ngầm.** Dòng đường ngầm giữa mũi dò và mẫu phụ thuộc khoảng cách theo $e^{-2\kappa d}$; thay đổi $d$ cỡ $0{,}1$ nm đã làm dòng đổi một bậc, cho độ phân giải nguyên tử.

**Phản ứng nhiệt hạch trong sao.** Nhiệt độ lõi Mặt Trời chỉ cho động năng cỡ keV, thấp hơn nhiều rào Coulomb MeV; không có đường ngầm thì các ngôi sao không thể cháy.

**Lỗi thường gặp:**
- Cho rằng hạt "mượn" năng lượng để vượt rào rồi trả lại. Không có sự vi phạm bảo toàn năng lượng nào: hạt đo được ở phía bên kia vẫn có đúng năng lượng $E$ ban đầu; điều xảy ra là hàm sóng có đuôi tắt mũ trong vùng cấm.
- Dùng $T\approx e^{-2\kappa a}$ khi hàng rào mỏng hoặc $E$ gần $V_0$. Công thức đơn giản này chỉ là giới hạn $\kappa a\gg1$; ngoài vùng đó phải dùng biểu thức $\sinh^2$ đầy đủ, và tại $E>V_0$ còn xuất hiện cộng hưởng truyền qua với $T=1$.
- Bỏ qua khối lượng khi so sánh các hạt. Vì $\kappa\propto\sqrt m$ nằm trong số mũ, proton chui qua cùng hàng rào với xác suất nhỏ hơn electron nhiều bậc độ lớn — điều này chi phối cả hiệu ứng đồng vị trong xúc tác.

<sub>`lesson.physics.co-hoc-luong-tu.hang-rao-the-va-hieu-ung-duong-ngam`</sub>

---

### 8. Mômen động lượng và spin
*Angular momentum and spin* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Suy ra được phổ trị riêng của mômen động lượng từ đại số giao hoán tử
- Phân biệt được mômen động lượng quỹ đạo và spin về nguồn gốc và trị riêng
- Vận dụng được ma trận Pauli để mô tả hệ spin 1/2

## Đại số quyết định tất cả

Chỉ cần một giả thiết: $[J_x,J_y]=i\hbar J_z$ cùng hoán vị vòng quanh. Từ đó $[\vec J^2,J_z]=0$, nên có hệ trạng thái riêng chung $|j,m\rangle$. Dùng $J_\pm=J_x\pm iJ_y$ và lập luận thang bị chặn (vì $\langle J_x^2+J_y^2\rangle\ge0$):

$$\vec J^2|j,m\rangle=\hbar^2j(j+1)|j,m\rangle,\qquad J_z|j,m\rangle=\hbar m|j,m\rangle$$

với $m=-j,-j+1,\dots,j$ và $j$ nhận **cả giá trị nguyên lẫn bán nguyên**. Đây là kết quả thuần đại số, không cần biết dạng hàm sóng.

## Quỹ đạo: chỉ nguyên

Với $\vec L=\vec r\times\vec p$, hàm riêng là hàm cầu $Y_{\ell m}(\theta,\varphi)$. Điều kiện đơn trị khi $\varphi\to\varphi+2\pi$ loại hết các giá trị bán nguyên, nên $\ell=0,1,2,\dots$ Chú ý $|\vec L|=\hbar\sqrt{\ell(\ell+1)}>\hbar\ell$: vectơ mômen động lượng không bao giờ nằm hoàn toàn dọc trục $z$, đúng như bất định đòi hỏi vì $L_x,L_y$ không đo đồng thời được với $L_z$.

## Spin: bán nguyên được phép

Thí nghiệm Stern - Gerlach tách chùm bạc thành **hai** vệt, tức $2s+1=2$ nên $s=1/2$ — giá trị bán nguyên không thể là mômen quỹ đạo. Spin là bậc tự do nội tại, không có tương ứng cổ điển; hình ảnh "electron tự quay" sai vì bề mặt sẽ phải chuyển động nhanh hơn ánh sáng.

Với $s=1/2$, không gian trạng thái là $\mathbb{C}^2$ và

$$\vec S=\frac{\hbar}{2}\vec\sigma,\qquad \sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\ \sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\ \sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$$

với $\sigma_i^2=\mathbf 1$ và $\sigma_i\sigma_j=i\epsilon_{ijk}\sigma_k$ khi $i\neq j$.

## Hệ quả đo được

Mômen từ $\vec\mu=g\dfrac{q}{2m}\vec S$ với $g\approx2$ cho electron (tiên đoán bởi phương trình Dirac). Ghép $\vec L$ và $\vec S$ theo quy tắc cộng mômen động lượng cho $j=\ell\pm\tfrac12$, sinh ra cấu trúc tinh tế của vạch phổ và hiệu ứng Zeeman dị thường qua thừa số Landé.

**Lỗi thường gặp:**
- Cho rằng $|\vec L|=\hbar\ell$. Độ lớn đúng là $\hbar\sqrt{\ell(\ell+1)}$, luôn lớn hơn hình chiếu cực đại $\hbar\ell$; nếu bằng nhau thì $L_x=L_y=0$ đồng thời, vi phạm hệ thức bất định.
- Hình dung spin như electron tự quay quanh trục. Với bán kính cổ điển của electron, tốc độ bề mặt cần thiết vượt xa $c$; hơn nữa giá trị bán nguyên không thể có ở bất kì chuyển động quay không gian nào.
- Cộng mômen động lượng bằng cách cộng số lượng tử: $j=\ell+s$ luôn. Quy tắc đúng cho dải $|\ell-s|\le j\le\ell+s$, và mỗi $j$ ứng với một tổ hợp cụ thể của các trạng thái tích qua hệ số Clebsch - Gordan.

<sub>`lesson.physics.co-hoc-luong-tu.momen-dong-luong-va-spin`</sub>

---

### 9. Nguyên tử hydro: lời giải chính xác và cấu trúc phổ
*The hydrogen atom: exact solution and spectral structure* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Tách được phương trình Schrödinger trong thế Coulomb thành phần bán kính và phần góc
- Giải thích được nguồn gốc các số lượng tử n, l, m và sự suy biến
- Tính được bước sóng các vạch quang phổ hydro từ mức năng lượng

## Tách biến

Thế Coulomb xuyên tâm nên đặt $\psi=R_{n\ell}(r)Y_{\ell m}(\theta,\varphi)$. Phần góc đã giải xong ở bài mômen động lượng. Phần bán kính, với $u=rR$:

$$-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2}+\left[-\frac{e^2}{4\pi\varepsilon_0 r}+\frac{\hbar^2\ell(\ell+1)}{2mr^2}\right]u=Eu$$

Ngoặc vuông chính là **thế hiệu dụng** quen thuộc từ cơ học cổ điển: thế Coulomb cộng rào li tâm.

## Phổ năng lượng

Đòi hỏi $u$ hữu hạn ở gốc và tắt ở vô cùng cắt bỏ hầu hết nghiệm, chỉ còn

$$E_n=-\frac{m e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}=-\frac{13{,}6\ \text{eV}}{n^2},\qquad n=1,2,\dots$$

với $\ell=0,\dots,n-1$ và $m=-\ell,\dots,\ell$. Mức $n$ có $n^2$ trạng thái (chưa kể spin), tức $2n^2$ khi tính spin.

## Hai loại suy biến, hai nguồn gốc

Suy biến theo $m$ có ở **mọi** thế xuyên tâm, do đối xứng quay. Suy biến theo $\ell$ thì đặc biệt của thế $1/r$: nó đến từ một đối xứng ẩn (bảo toàn vectơ Laplace - Runge - Lenz, tương ứng quỹ đạo elip đóng kín trong cơ học cổ điển). Vì thế mọi nhiễu loạn phá vỡ dạng $1/r$ — che chắn trong nguyên tử nhiều electron — lập tức tách các mức theo $\ell$.

## Từ mức tới vạch phổ

$$\frac{1}{\lambda}=R_\infty\left(\frac{1}{n_f^2}-\frac{1}{n_i^2}\right),\qquad R_\infty=1{,}097\cdot10^7\ \text{m}^{-1}$$

Dãy Lyman ($n_f=1$) trong tử ngoại, Balmer ($n_f=2$) trong khả kiến, Paschen ($n_f=3$) hồng ngoại. Không phải mọi cặp mức đều cho vạch: quy tắc lọc lựa $\Delta\ell=\pm1$ (do toán tử $\vec r$ là tenxơ bậc 1) cấm nhiều chuyển mức, ví dụ $2s\to1s$ — đó là lí do trạng thái $2s$ giả bền với thời gian sống $0{,}12$ s.

## Hiệu chỉnh

Kết quả trên còn thô: cấu trúc tinh tế (bậc $\alpha^2$) do hiệu ứng tương đối tính và tương tác spin - quỹ đạo, dịch chuyển Lamb do điện động lực học lượng tử, và cấu trúc siêu tinh tế do spin hạt nhân.

**Lỗi thường gặp:**
- Cho rằng số lượng tử $\ell$ có thể bằng $n$. Điều kiện tồn tại nghiệm bán kính chính quy buộc $\ell\le n-1$; trạng thái $2d$ hay $3f$ không tồn tại.
- Đồng nhất bán kính Bohr với bán kính quỹ đạo xác định. Trạng thái $1s$ có phân bố xác suất trải rộng, $a_0$ chỉ là bán kính có mật độ xác suất bán kính lớn nhất; $\langle r\rangle=1{,}5a_0$.
- Áp dụng công thức $E_n=-13{,}6\ \text{eV}/n^2$ cho mọi nguyên tử. Nó chỉ đúng cho hệ một electron; với ion tương tự hydro phải nhân $Z^2$, còn nguyên tử nhiều electron có che chắn nên năng lượng phụ thuộc cả $\ell$.

<sub>`lesson.physics.co-hoc-luong-tu.nguyen-tu-hidro`</sub>

---

### 10. Hạt đồng nhất, nguyên lí Pauli và định thức Slater
*Identical particles, the Pauli principle and Slater determinants* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Phân biệt được boson và fermion theo tính đối xứng của hàm sóng
- Giải thích được nguyên lí loại trừ Pauli như hệ quả của tính phản đối xứng
- Viết được hàm sóng nhiều fermion dưới dạng định thức Slater

## Không phân biệt được nghĩa là gì

Hai electron không có "nhãn". Hoán vị chúng phải cho cùng trạng thái vật lí, tức $|\Psi|^2$ không đổi, nên $\hat P\Psi=\pm\Psi$. Tự nhiên chỉ dùng hai khả năng đó, và định lí spin - thống kê (chứng minh trong lí thuyết trường lượng tử tương đối tính) gắn chúng với spin:

- spin nguyên $\to$ **boson**, hàm sóng đối xứng;
- spin bán nguyên $\to$ **fermion**, hàm sóng phản đối xứng.

## Hệ quả tức thì: nguyên lí Pauli

Với hai fermion cùng trạng thái một hạt $\psi_a$:

$$\Psi=\frac{1}{\sqrt2}\left[\psi_a(1)\psi_a(2)-\psi_a(2)\psi_a(1)\right]=0$$

Không có trạng thái nào tồn tại. Nguyên lí loại trừ **không phải tiên đề riêng** mà là hệ quả trực tiếp của tính phản đối xứng. Với $N$ fermion, viết gọn:

$$\Psi=\frac{1}{\sqrt{N!}}\det\left[\psi_i(\vec r_j)\right]$$

Định thức tự động triệt tiêu khi hai hàng trùng nhau — chính là Pauli.

## Lực trao đổi

Tính $\langle(x_1-x_2)^2\rangle$ cho hai hạt ở hai trạng thái khác nhau. So với trường hợp hạt phân biệt được, kết quả có thêm số hạng $-2|\langle x\rangle_{ab}|^2$ với boson và $+2|\langle x\rangle_{ab}|^2$ với fermion: boson có xu hướng **tụ lại**, fermion **tránh nhau**. Đây không phải lực thật mà là hệ quả thống kê của tính đối xứng — nhưng hệ quả thì rất thật.

## Ở đâu thấy được

Cấu hình electron và toàn bộ bảng tuần hoàn dựa trên việc mỗi trạng thái $(n,\ell,m_\ell,m_s)$ chứa nhiều nhất một electron. Áp suất suy biến của khí electron giữ sao lùn trắng khỏi sụp đổ. Ngược lại, boson tụ lại cho ngưng tụ Bose - Einstein, laser và siêu chảy. Với electron, phần spin và phần không gian phải có tính đối xứng ngược nhau: trạng thái singlet (spin phản đối xứng) đi với hàm không gian đối xứng, và chính ràng buộc này tạo ra liên kết hóa học cùng tương tác trao đổi trong sắt từ.

**Lỗi thường gặp:**
- Áp dụng nguyên lí Pauli cho boson. Photon, phonon và nguyên tử heli-4 có thể chiếm cùng một trạng thái với số lượng tùy ý; đó chính là điều kiện cho laser và ngưng tụ Bose - Einstein.
- Coi "lực trao đổi" là một tương tác cơ bản mới. Không có trường lực nào; hiệu ứng đến hoàn toàn từ ràng buộc đối xứng lên hàm sóng, nhưng lại đủ mạnh để giải thích liên kết cộng hóa trị và sắt từ.
- Viết hàm sóng hai electron là tích đơn giản $\psi_a(1)\psi_b(2)$. Cách viết này giả định phân biệt được hai hạt; nó cho tiên đoán sai về tương quan vị trí và không thể hiện được nguyên lí Pauli.

<sub>`lesson.physics.co-hoc-luong-tu.hat-dong-nhat-va-nguyen-li-pauli`</sub>

---

### 11. Lí thuyết nhiễu loạn dừng và phương pháp biến phân
*Time-independent perturbation theory and the variational method* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Tính được hiệu chỉnh năng lượng bậc một và bậc hai của lí thuyết nhiễu loạn
- Xử lí được trường hợp mức suy biến bằng cách chéo hóa trong không gian con
- Vận dụng được nguyên lí biến phân để chặn trên năng lượng trạng thái cơ bản

## Vì sao cần phương pháp gần đúng

Số bài toán giải chính xác được đếm trên đầu ngón tay. Mọi hệ thực tế — nguyên tử heli, phân tử, nguyên tử trong điện trường — đều cần gần đúng. Hai công cụ chủ lực bổ sung cho nhau: nhiễu loạn khi phần thêm vào nhỏ, biến phân khi không có tham số nhỏ nào.

## Nhiễu loạn không suy biến

Đặt $\hat H=\hat H_0+\lambda\hat H'$ và khai triển cả $E_n$ lẫn $|\psi_n\rangle$ theo $\lambda$. So sánh từng bậc:

$$E_n^{(1)}=\langle\psi_n^{(0)}|\hat H'|\psi_n^{(0)}\rangle,\qquad E_n^{(2)}=\sum_{m\neq n}\frac{\left|\langle\psi_m^{(0)}|\hat H'|\psi_n^{(0)}\rangle\right|^2}{E_n^{(0)}-E_m^{(0)}}$$

Đọc ngay hai điều: bậc một chỉ là trị trung bình của nhiễu loạn; bậc hai với trạng thái cơ bản **luôn âm** vì mọi mẫu số đều âm — mức cơ bản luôn bị đẩy xuống. Điều kiện hội tụ: $|\langle m|H'|n\rangle|\ll|E_n^{(0)}-E_m^{(0)}|$, nên phương pháp hỏng khi có mức gần suy biến.

## Suy biến: phải chéo hóa trước

Khi mức $E_n^{(0)}$ suy biến, mẫu số triệt tiêu và công thức trên vô nghĩa. Cách xử lí: lập ma trận $\langle a|\hat H'|b\rangle$ trong không gian con suy biến rồi **chéo hóa** nó. Trị riêng là các hiệu chỉnh bậc một, vectơ riêng là "tổ hợp đúng" để tiếp tục khai triển. Đây là cơ chế của hiệu ứng Stark tuyến tính trong hydro và của mọi hiện tượng tách mức.

## Biến phân

Vì mọi hàm thử khai triển được theo hệ riêng, $\langle H\rangle=\sum|c_n|^2E_n\ge E_0\sum|c_n|^2=E_0$. Chiến lược: chọn họ hàm thử có tham số, tính $\langle H\rangle$ rồi cực tiểu hoá. Kết quả luôn là **chặn trên**, và thường rất tốt cho năng lượng ngay cả khi hàm thử tầm thường — vì sai số năng lượng là bậc hai theo sai số hàm sóng.

Điểm yếu: biến phân không cho biết mình sai bao nhiêu, và tính tốt cho năng lượng không có nghĩa hàm sóng đúng. Với heli, hàm thử hydro có điện tích hiệu dụng $Z_{\text{eff}}$ cho $-77{,}5$ eV so với thực nghiệm $-79{,}0$ eV.

**Lỗi thường gặp:**
- Dùng công thức không suy biến cho mức suy biến. Mẫu số $E_n^{(0)}-E_m^{(0)}$ triệt tiêu, cho kết quả vô hạn; phải chéo hóa nhiễu loạn trong không gian con trước.
- Cho rằng hiệu chỉnh bậc một bằng 0 nghĩa là nhiễu loạn không ảnh hưởng. Bậc một thường triệt tiêu do đối xứng (ví dụ $\langle x\rangle=0$); khi đó hiệu ứng nằm ở bậc hai và vẫn đo được, như hiệu ứng Stark bậc hai.
- Coi kết quả biến phân là chặn dưới hoặc là giá trị chính xác. Nó luôn là chặn **trên** của $E_0$; hàm thử càng linh hoạt thì càng gần, nhưng không bao giờ xuống dưới giá trị thật.

<sub>`lesson.physics.co-hoc-luong-tu.nhieu-loan-dung-va-phuong-phap-bien-phan`</sub>

---

### 12. Nhiễu loạn phụ thuộc thời gian và quy tắc vàng Fermi
*Time-dependent perturbation theory and Fermi's golden rule* · Đại học · intl-undergrad · 55 phút · chuyen-sau

**Mục tiêu:**
- Tính được biên độ chuyển mức bậc một dưới tác dụng của nhiễu loạn phụ thuộc thời gian
- Thiết lập được quy tắc vàng Fermi cho tốc độ chuyển mức
- Vận dụng được quy tắc lọc lựa lưỡng cực để giải thích cường độ vạch phổ

## Bài toán

Hệ đang ở trạng thái riêng $|i\rangle$ của $\hat H_0$. Bật một nhiễu loạn $\hat H'(t)$ — chẳng hạn sóng điện từ. Hỏi sau thời gian $t$, xác suất tìm thấy hệ ở $|f\rangle$ là bao nhiêu?

## Bậc một

Khai triển $|\Psi(t)\rangle=\sum_n c_n(t)e^{-iE_nt/\hbar}|n\rangle$ và thay vào phương trình Schrödinger. Ở bậc một (giả sử $c_i\approx1$):

$$c_f(t)=-\frac{i}{\hbar}\int_0^t\langle f|\hat H'(t')|i\rangle\,e^{i\omega_{fi}t'}\,dt',\qquad \omega_{fi}=\frac{E_f-E_i}{\hbar}$$

Đọc ngay: xác suất chuyển mức phụ thuộc **biến đổi Fourier của nhiễu loạn tại tần số cộng hưởng** $\omega_{fi}$. Nhiễu loạn biến thiên chậm hầu như không gây chuyển mức (định lí đoạn nhiệt); nhiễu loạn đột ngột thì kích thích rộng phổ.

## Nhiễu loạn điều hòa và quy tắc vàng

Với $\hat H'=V\cos\omega t$, tích phân cho $|c_f|^2\propto\dfrac{\sin^2\left[(\omega_{fi}-\omega)t/2\right]}{(\omega_{fi}-\omega)^2}$: một đỉnh nhọn quanh cộng hưởng, rộng cỡ $2\pi/t$ và cao tỉ lệ $t^2$. Khi trạng thái cuối là phổ **liên tục**, tích phân đỉnh này trên $E_f$ cho một xác suất tỉ lệ tuyến tính với $t$, tức tốc độ không đổi:

$$W_{i\to f}=\frac{2\pi}{\hbar}\left|\langle f|\hat H'|i\rangle\right|^2\rho(E_f)$$

Đây là quy tắc vàng Fermi. Hai thừa số có vai trò khác nhau: phần tử ma trận quyết định "được phép hay không", mật độ trạng thái quyết định "có bao nhiêu chỗ để đi".

## Quy tắc lọc lựa

Với bức xạ lưỡng cực điện $\hat H'=-q\vec E\cdot\vec r$, phần tử ma trận là $\langle f|\vec r|i\rangle$. Tính chẵn lẻ và tính tenxơ bậc 1 của $\vec r$ cho $\Delta\ell=\pm1$, $\Delta m=0,\pm1$, $\Delta s=0$. Chuyển mức vi phạm bị **cấm lưỡng cực**; chúng vẫn xảy ra qua tứ cực hay lưỡng cực từ nhưng chậm hơn nhiều bậc — đó là nguồn gốc các vạch giả bền trong tinh vân.

## Phạm vi hiệu lực

Kết quả chỉ đúng khi $|c_f|^2\ll1$: nếu nhiễu loạn mạnh hoặc thời gian dài, hệ dao động Rabi qua lại giữa hai mức và lí thuyết bậc một sụp đổ.

**Lỗi thường gặp:**
- Hiểu "cấm" là tuyệt đối không xảy ra. Quy tắc lọc lựa chỉ nói phần tử ma trận **lưỡng cực điện** bằng 0; các cơ chế bậc cao vẫn cho chuyển mức, chỉ chậm hơn nhiều bậc độ lớn.
- Áp dụng quy tắc vàng cho chuyển mức giữa hai trạng thái rời rạc. Công thức đòi hỏi mật độ trạng thái cuối liên tục; với hai mức cô lập, hệ dao động Rabi tuần hoàn chứ không phân rã theo hàm mũ.
- Dùng lí thuyết bậc một khi xác suất chuyển mức tính ra gần 1. Điều đó vi phạm giả thiết $c_i\approx1$; kết quả có thể vượt quá 1, dấu hiệu rõ ràng rằng phải dùng phương pháp không nhiễu loạn.

<sub>`lesson.physics.co-hoc-luong-tu.nhieu-loan-phu-thuoc-thoi-gian-va-quy-tac-vang-fermi`</sub>

---

### 13. Rối lượng tử và bất đẳng thức Bell
*Quantum entanglement and Bell's inequality* · Đại học · intl-undergrad · 55 phút · chuyen-sau

**Mục tiêu:**
- Định nghĩa được trạng thái rối và phân biệt được với trạng thái tích
- Phát biểu được bất đẳng thức Bell dạng CHSH và điều kiện vi phạm
- Giải thích được ý nghĩa của các thí nghiệm Aspect đối với tính thực tại địa phương

## Trạng thái không tách được

Xét cặp spin ở trạng thái singlet

$$|\Psi^-\rangle=\frac{1}{\sqrt2}\left(|{\uparrow}\rangle_A|{\downarrow}\rangle_B-|{\downarrow}\rangle_A|{\uparrow}\rangle_B\right)$$

Không có cách nào viết nó thành $|\phi\rangle_A\otimes|\chi\rangle_B$. Hệ quả: từng hạt riêng lẻ **không có** trạng thái xác định (ma trận mật độ rút gọn là hỗn hợp hoàn toàn), chỉ cặp mới có. Đo spin của A theo bất kì trục nào cho kết quả ngẫu nhiên 50-50, nhưng B luôn cho kết quả ngược lại theo cùng trục đó.

## EPR và câu hỏi của Einstein

Nếu kết quả tương quan hoàn hảo, phải chăng mỗi hạt đã mang sẵn "chỉ dẫn" từ lúc sinh ra? Đó là giả thuyết **biến ẩn địa phương**: thực tại có sẵn, không cần truyền tin xa.

## Bell biến triết học thành thí nghiệm

Đo spin của A theo hướng $\vec a$ hoặc $\vec a'$, của B theo $\vec b$ hoặc $\vec b'$. Đặt $E(\vec a,\vec b)$ là tương quan trung bình. Mọi lí thuyết biến ẩn địa phương buộc

$$S=\left|E(\vec a,\vec b)-E(\vec a,\vec b')+E(\vec a',\vec b)+E(\vec a',\vec b')\right|\le2$$

Cơ học lượng tử cho $E(\vec a,\vec b)=-\cos\theta_{ab}$; chọn bốn hướng cách nhau $45^\circ$ được $S=2\sqrt2\approx2{,}83>2$.

## Thí nghiệm phán quyết

Aspect (1982) rồi các thí nghiệm "không kẽ hở" (2015) đo được $S>2$ với độ tin cậy rất cao. Kết luận: **không có** lí thuyết biến ẩn địa phương nào mô tả đúng tự nhiên. Giải Nobel Vật lí 2022 trao cho Aspect, Clauser và Zeilinger vì công trình này.

## Điều rối lượng tử **không** cho phép

Rối không truyền tin nhanh hơn ánh sáng: kết quả của A luôn ngẫu nhiên, và chỉ khi so sánh hai bảng kết quả qua kênh cổ điển mới thấy tương quan. Định lí không truyền tin bảo đảm điều này. Tuy vậy rối là tài nguyên thực sự cho phân phối khóa lượng tử, viễn tải trạng thái và tính toán lượng tử.

**Lỗi thường gặp:**
- Cho rằng rối lượng tử cho phép truyền tin tức thời. Kết quả đo ở mỗi phía là ngẫu nhiên hoàn toàn và không phụ thuộc lựa chọn của phía kia; chỉ khi ghép hai bảng dữ liệu qua kênh cổ điển mới lộ ra tương quan.
- Hiểu vi phạm Bell là bằng chứng có tín hiệu siêu quang. Điều bị bác bỏ là **tổ hợp** của tính địa phương và tính thực tại có sẵn; cơ học lượng tử vẫn hoàn toàn tương thích với thuyết tương đối.
- Nghĩ rằng mọi trạng thái hai hạt đều rối. Trạng thái tích như $|{\uparrow}\rangle_A|{\downarrow}\rangle_B$ hoàn toàn không rối; đo A không cho biết gì thêm về B, và ma trận mật độ rút gọn của nó là trạng thái thuần.

<sub>`lesson.physics.co-hoc-luong-tu.roi-luong-tu-va-bat-dang-thuc-bell`</sub>

---

## Unit 3: IPhO Advanced Electrodynamics

### 1. IPhO Điện từ nâng cao: Bức xạ Larmor, Khai triển đa cực và Tiến động spin
*Advanced electrodynamics: Larmor radiation formula, multipole expansion, and precession* · Đại học · olympiad · 60 phút · chuyen-sau

**Mục tiêu:**
- Phát biểu và áp dụng công thức Larmor về công suất bức xạ của điện tích có gia tốc
- Thực hiện khai triển đa cực của điện thế đến số hạng lưỡng cực và tứ cực
- Tính tần số tiến động Larmor của mômen từ trong từ trường ngoài

## Công thức bức xạ Larmor

Khi một điện tích điểm $q$ chuyển động với gia tốc $\vec{a}$ phi tương đối tính ($v \ll c$), nó bức xạ sóng điện từ ra không gian với tổng công suất:

$$P = \frac{q^2 a^2}{6\pi\varepsilon_0 c^3}$$

Đây là nguyên nhân electron trong nguyên tử theo cơ học cổ điển sẽ mất dần năng lượng và rơi vào hạt nhân.

## Khai triển đa cực và Tiến động Larmor

Điện thế của phân bố điện tích ở khoảng cách lớn $r \gg d$ được khai triển theo các luỹ thừa của $1/r$:

$$V(\vec{r}) = \frac{1}{4\pi\varepsilon_0} \left[ \frac{Q}{r} + \frac{\vec{p} \cdot \hat{r}}{r^2} + \sum_{i,j} \frac{Q_{ij} \hat{r}_i \hat{r}_j}{2r^3} + \dots \right]$$

Mômen từ $\vec{\mu} = \gamma \vec{L}$ đặt trong từ trường $\vec{B}$ chịu mômen lực $\vec{\tau} = \vec{\mu} \times \vec{B}$, tạo ra chuyển động tiến động Larmor với tần số $\omega_L = \frac{q B}{2m}$.

**Lỗi thường gặp:**
- Áp dụng công thức Larmor phi tương đối tính cho các chùm hạt chuyển động với tốc độ gần bằng ánh sáng
- Nhầm lẫn giữa tần số cyclotron omega_c = qB/m và tần số tiến động Larmor omega_L = qB/(2m)

<sub>`lesson.physics.ipho.dien-tu-nang-cao-buc-xa-larmor-da-cuc`</sub>

---

## Unit 3: Oscillations and Waves in Continuous Media

### 1. Dao động điều hoà, Dao động tắt dần và Hiện tượng cộng hưởng
*Harmonic, damped and forced oscillations and mechanical resonance* · Đại học · intl-undergrad, vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Giải phương trình vi phân dao động tắt dần dưới tác dụng của lực cản nhớt
- Tính lượng giảm logarit và hệ số phẩm chất Q của hệ dao động
- Xác định biên độ và tần số góc cộng hưởng của dao động cưỡng bức

## Phương trình dao động tắt dần

Xét chất điểm khối lượng $m$ chịu lực kéo về $F_{kv} = -kx$ và lực cản nhớt $F_c = -r v$:

$$\ddot{x} + 2\beta \dot{x} + \omega_0^2 x = 0, \quad \beta = \frac{r}{2m},\ \omega_0 = \sqrt{\frac{k}{m}}$$

Khi cản yếu ($\beta < \omega_0$), nghiệm có dạng $x(t) = A_0 e^{-\beta t} \cos(\omega t + \varphi)$ với tần số $\omega = \sqrt{\omega_0^2 - \beta^2}$.

## Dao động cưỡng bức và Cộng hưởng

Khi có ngoại lực điều hoà $F_0 \cos(\Omega t)$, ở trạng thái xác lập biên độ dao động là:

$$A = \frac{F_0/m}{\sqrt{(\omega_0^2 - \Omega^2)^2 + 4\beta^2 \Omega^2}}$$

Hiện tượng cộng hưởng biên độ xuất hiện tại tần số góc $\Omega_{ch} = \sqrt{\omega_0^2 - 2\beta^2}$.

**Lỗi thường gặp:**
- Nhầm tần số cộng hưởng Omega_ch với tần số riêng omega_0 (chỉ trùng nhau khi beta = 0)
- Quên thừa số 2 trước beta trong phương trình vi phân dạng chuẩn

<sub>`lesson.physics.undergrad-physics.dao-dong-dieu-hoa-tat-dan-va-cuong-buc`</sub>

---

### 2. Sóng cơ học, Sóng âm và Hiệu ứng Doppler
*Mechanical waves, acoustic intensity and the Doppler effect* · Đại học · intl-undergrad, vn-gdpt-2018 · 55 phút · trung-binh

**Mục tiêu:**
- Thiết lập phương trình truyền sóng phẳng và tính cường độ sóng âm theo mức dB
- Vận dụng nguyên lý chồng chất sóng tạo hình Lissajous và sóng dừng
- Áp dụng công thức Doppler tổng quát cho nguồn và máy thu chuyển động bất kì

## Phương trình sóng phẳng và Cường độ sóng

Phương trình sóng hình sin lan truyền dọc trục $x$ với vận tốc $v$:

$$u(x, t) = A \cos\left(\omega t - \frac{2\pi}{\lambda} x + \varphi\right)$$

Cường độ sóng $I$ là năng lượng truyền qua một đơn vị diện tích trong một đơn vị thời gian: $I = \frac{1}{2} \rho v \omega^2 A^2$. Mức cường độ âm theo thang decibel: $L = 10 \lg \frac{I}{I_0}$.

## Hiệu ứng Doppler âm thanh

Khi máy thu chuyển động với vận tốc $v_M$ và nguồn phát chuyển động với vận tốc $v_N$ trên cùng đường thẳng (quy ước chiều dương hướng từ nguồn tới máy thu):

$$f' = f \frac{v - v_M}{v - v_N}$$

**Lỗi thường gặp:**
- Nhầm lẫn dấu cộng trừ trong công thức hiệu ứng Doppler khi nguồn hay máy thu tiến lại gần/ra xa
- Quên lấy logarit cơ số 10 trong công thức tính mức decibel

<sub>`lesson.physics.undergrad-physics.song-co-hoc-am-hoc-va-hieu-ung-doppler`</sub>

---

## Unit 4: Fluid Mechanics and Transport Phenomena

### 1. Cơ học chất lưu thực: Phương trình Bernoulli, Poiseuille và Navier-Stokes
*Fluid dynamics: Bernoulli equation, Poiseuille flow, and Reynolds number* · Đại học · intl-undergrad, vn-gdpt-2018 · 55 phút · nang-cao

**Mục tiêu:**
- Vận dụng phương trình liên tục và phương trình Bernoulli cho dòng chảy ổn định
- Tính lưu lượng chất lưu nhớt chảy trong ống hình trụ theo định luật Poiseuille
- Xác định chế độ chảy tầng và chảy rối qua số Reynolds

## Phương trình Bernoulli cho chất lưu lý tưởng

Đối với chất lưu không chịu nén, không nhớt, chảy dừng dọc một đường dòng:

$$p + \frac{1}{2} \rho v^2 + \rho g h = \text{hằng số}$$

Công thức Torricelli tính tốc độ xả đáy từ bể chứa: $v = \sqrt{2gh}$.

## Chất lưu thực: Định luật Poiseuille và Số Reynolds

Khi xét tới độ nhớt $\eta$, lưu lượng dòng chảy tầng qua ống tròn bán kính $R$, chiều dài $L$ dưới chênh áp $\Delta p$ tuân theo định luật Hagen - Poiseuille:

$$Q = \frac{\pi R^4 \Delta p}{8 \eta L}$$

Số Reynolds $Re = \frac{\rho v D}{\eta}$ quyết định tính ổn định của dòng chảy: nếu $Re < 2300$ dòng chảy là chảy tầng (laminar), nếu $Re > 4000$ chuyển thành chảy rối (turbulent).

**Lỗi thường gặp:**
- Áp dụng định luật Poiseuille cho dòng chảy rối (Poiseuille chỉ nghiệm đúng cho dòng chảy tầng)
- Quên luỹ thừa bậc 4 của bán kính R trong công thức tính lưu lượng Poiseuille

<sub>`lesson.physics.undergrad-physics.co-hoc-chat-luu-navier-stokes-va-reynolds`</sub>

---

## Unit 4: Nhiệt động lực học và vật lí thống kê

### 1. Các nguyên lí nhiệt động lực học và các thế nhiệt động
*Laws of thermodynamics and thermodynamic potentials* · Đại học · intl-undergrad · 55 phút · trung-binh

**Mục tiêu:**
- Phát biểu được ba nguyên lí nhiệt động lực học ở dạng vi phân
- Xây dựng được các thế nhiệt động bằng biến đổi Legendre
- Xác định được thế nào là đại lượng cần cực tiểu hóa trong từng điều kiện ràng buộc

## Ba nguyên lí, gọn lại

**Nguyên lí thứ nhất** là bảo toàn năng lượng có kể nhiệt: $dU=\delta Q+\delta W$. Chú ý $U$ là hàm trạng thái còn $Q,W$ thì không — không tồn tại "lượng nhiệt chứa trong vật".

**Nguyên lí thứ hai** đưa vào entropy: $dS\ge\delta Q/T$, dấu bằng khi thuận nghịch. Với hệ cô lập, $S$ chỉ tăng.

**Nguyên lí thứ ba**: $S\to0$ (hoặc hằng số) khi $T\to0$, kéo theo mọi nhiệt dung phải triệt tiêu ở $0$ K và không thể đạt tới $0$ K bằng hữu hạn bước.

Gộp lại cho **hệ thức cơ bản**

$$dU=T\,dS-p\,dV+\mu\,dN$$

## Vì sao cần nhiều thế

$U(S,V,N)$ là hàm tự nhiên nhưng $S$ không đo trực tiếp được. Thí nghiệm thường kiểm soát $T$ và $p$. Biến đổi Legendre đổi biến độc lập mà không mất thông tin:

$$H=U+pV,\qquad F=U-TS,\qquad G=U-TS+pV$$

với các vi phân

$$dH=TdS+Vdp,\qquad dF=-SdT-pdV,\qquad dG=-SdT+Vdp$$

## Nguyên lí cực trị: dùng thế nào khi nào

Từ nguyên lí thứ hai áp cho hệ + môi trường suy ra:

| Ràng buộc | Đại lượng cực tiểu |
|---|---|
| $U,V$ cố định | $S$ cực **đại** |
| $T,V$ cố định | $F$ |
| $T,p$ cố định | $G$ |
| $S,p$ cố định | $H$ |

Chọn sai thế là lỗi khái niệm nghiêm trọng: nước không đóng băng vì entropy nước đá lớn hơn (nó nhỏ hơn), mà vì ở $T<0^\circ$C thì $G$ của pha rắn thấp hơn — entropy giảm của nước được bù thừa bởi entropy tăng của môi trường nhận nhiệt kết tinh.

## Ý nghĩa của F

$-\Delta F$ là công cực đại lấy được từ quá trình đẳng nhiệt; $-\Delta G$ là công phi thể tích cực đại, chính là đại lượng chi phối pin điện hóa và trao đổi chất trong tế bào.

**Lỗi thường gặp:**
- Viết $\Delta Q$ hoặc $\Delta W$ như biến thiên của một hàm trạng thái. Nhiệt và công phụ thuộc đường đi, chỉ có $\delta Q$ và $\delta W$ (vi phân không toàn phần) là hợp lệ; nói "nhiệt lượng của một trạng thái" là vô nghĩa.
- Dùng $\Delta S=Q/T$ cho quá trình bất thuận nghịch. Công thức chỉ đúng cho đường thuận nghịch; với quá trình thực phải tìm một đường thuận nghịch bất kì nối cùng hai trạng thái, vì $S$ là hàm trạng thái.
- Kết luận entropy của hệ không bao giờ giảm. Nguyên lí thứ hai áp cho hệ **cô lập**; hệ mở có thể giảm entropy miễn là entropy môi trường tăng nhiều hơn — đó chính là cách sinh vật sống tồn tại.

<sub>`lesson.physics.nhiet-dong-thong-ke.cac-nguyen-li-va-the-nhiet-dong`</sub>

---

### 2. Các hệ thức Maxwell và ứng dụng
*Maxwell relations and their applications* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Suy ra được bốn hệ thức Maxwell từ tính đối xứng của đạo hàm bậc hai
- Vận dụng được hệ thức Maxwell để tính đại lượng khó đo qua đại lượng dễ đo
- Chứng minh được biểu thức tổng quát của hiệu nhiệt dung Cp − Cv

## Mẹo toán học, hệ quả vật lí

Mỗi thế nhiệt động là hàm trạng thái, nên vi phân của nó toàn phần và đạo hàm bậc hai chéo bằng nhau. Áp dụng cho bốn thế $U,H,F,G$:

$$\left(\frac{\partial T}{\partial V}\right)_S=-\left(\frac{\partial p}{\partial S}\right)_V,\qquad \left(\frac{\partial T}{\partial p}\right)_S=\left(\frac{\partial V}{\partial S}\right)_p$$
$$\left(\frac{\partial S}{\partial V}\right)_T=\left(\frac{\partial p}{\partial T}\right)_V,\qquad \left(\frac{\partial S}{\partial p}\right)_T=-\left(\frac{\partial V}{\partial T}\right)_p$$

## Vì sao chúng hữu ích

Entropy không đo trực tiếp được, nhưng $p,V,T$ thì đo dễ. Hai hệ thức cuối biến mọi đạo hàm của $S$ theo $V$ hoặc $p$ thành đại lượng đo được từ phương trình trạng thái. Đó là toàn bộ giá trị thực dụng của chúng.

Ví dụ, năng lượng nội tại phụ thuộc thể tích thế nào?

$$\left(\frac{\partial U}{\partial V}\right)_T=T\left(\frac{\partial p}{\partial T}\right)_V-p$$

Với khí lí tưởng $p=nRT/V$ nên vế phải bằng 0: $U$ chỉ phụ thuộc $T$ — kết quả này **suy ra được** chứ không cần giả thiết. Với khí Van der Waals, vế phải bằng $a n^2/V^2>0$, giải thích vì sao khí thực lạnh đi khi dãn tự do.

## Hiệu nhiệt dung tổng quát

$$C_p-C_V=\frac{TV\alpha^2}{\kappa_T}$$

Ba nhận xét: hiệu này **luôn không âm** (vì $\kappa_T>0$ với hệ bền); nó triệt tiêu ở $T=0$ và ở điểm mà $\alpha=0$ — chính là nước ở $4^\circ$C; và với khí lí tưởng nó rút về $nR$, tức hệ thức Mayer.

## Kĩ thuật làm việc

Ba công cụ đi kèm: quy tắc dây chuyền, quan hệ nghịch đảo $(\partial x/\partial y)_z=1/(\partial y/\partial x)_z$, và quy tắc vòng $(\partial x/\partial y)_z(\partial y/\partial z)_x(\partial z/\partial x)_y=-1$. Dấu trừ trong quy tắc vòng là chỗ sai phổ biến nhất.

**Lỗi thường gặp:**
- Quên dấu trừ trong quy tắc vòng. Ba đạo hàm riêng nhân nhau cho $-1$ chứ không phải $+1$; sai dấu này lan sang mọi kết quả suy ra sau đó.
- Bỏ qua chỉ số biến giữ cố định. $(\partial S/\partial T)_p$ và $(\partial S/\partial T)_V$ khác nhau và cho $C_p$ hay $C_V$ tương ứng; viết trần $\partial S/\partial T$ là vô nghĩa trong nhiệt động lực học.
- Cho rằng $C_p>C_V$ luôn đúng với mọi vật. Bất đẳng thức đúng nhờ $\alpha^2\ge0$, nhưng dấu bằng xảy ra khi $\alpha=0$; nước ở $4^\circ$C có $C_p=C_V$ vì đúng ở đó thể tích cực tiểu.

<sub>`lesson.physics.nhiet-dong-thong-ke.he-thuc-maxwell-nhiet-dong`</sub>

---

### 3. Chuyển pha và phương trình Clausius - Clapeyron
*Phase transitions and the Clausius-Clapeyron equation* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Phân loại được chuyển pha bậc một và bậc hai theo tính liên tục của đạo hàm thế Gibbs
- Thiết lập được phương trình Clausius - Clapeyron từ điều kiện cân bằng pha
- Giải thích được các đặc điểm bất thường của giản đồ pha nước

## Điều kiện cân bằng

Hai pha cùng tồn tại khi $T$, $p$ và **thế hóa học** bằng nhau: $\mu_1(T,p)=\mu_2(T,p)$. Đẳng thức này định nghĩa một đường cong trong mặt phẳng $(p,T)$ — đường cân bằng pha.

## Dẫn ra Clausius - Clapeyron

Đi dọc đường cân bằng, $d\mu_1=d\mu_2$. Với một hạt, $d\mu=-s\,dT+v\,dp$, nên

$$\frac{dp}{dT}=\frac{s_2-s_1}{v_2-v_1}=\frac{L}{T\,\Delta v}$$

với $L=T\Delta s$ là ẩn nhiệt riêng. Công thức tuy đơn giản nhưng cực kì hữu ích: nó nối độ dốc đường cân bằng với hai đại lượng đo được.

## Đọc giản đồ pha

**Hoá hơi**: $\Delta v>0$ lớn, $L>0$, nên $dp/dT>0$ và dốc thoải. Xấp xỉ $v_{\text{hơi}}\gg v_{\text{lỏng}}$ và dùng khí lí tưởng cho $\dfrac{d\ln p}{dT}=\dfrac{L}{RT^2}$, tích phân được quy luật $p\propto e^{-L/RT}$ — đó là lí do nước sôi ở $\sim70^\circ$C trên đỉnh Everest.

**Nóng chảy của nước**: đặc biệt vì $v_{\text{đá}}>v_{\text{nước}}$, tức $\Delta v<0$, nên $dp/dT<0$ — đường nóng chảy **nghiêng trái**. Tăng áp suất làm nước đá tan; đó là lí do băng trôi nổi và là một phần cơ chế trượt trên băng.

## Phân loại chuyển pha

Bậc một: đạo hàm bậc nhất của $G$ (là $S$ và $V$) nhảy bậc, có ẩn nhiệt, hai pha cùng tồn tại. Bậc hai (liên tục): $S$ và $V$ liên tục nhưng $C_p$, $\kappa_T$ phân kì; không có ẩn nhiệt và không có sự cùng tồn tại. Ví dụ điển hình là điểm Curie sắt từ, chuyển pha siêu dẫn ở từ trường bằng 0, và điểm $\lambda$ của heli.

## Điểm tới hạn

Đi dọc đường lỏng - hơi, hiệu mật độ hai pha giảm dần và triệt tiêu tại điểm tới hạn ($374^\circ$C, $22{,}1$ MPa với nước). Vượt qua đó không còn phân biệt lỏng và hơi. Gần điểm này các đại lượng tuân theo luật lũy thừa với các số mũ tới hạn phổ quát — chung cho những hệ trông rất khác nhau.

**Lỗi thường gặp:**
- Cho rằng mọi chất đều có đường nóng chảy nghiêng phải. Độ dốc chỉ dương khi pha lỏng có thể tích riêng lớn hơn pha rắn ($\Delta v>0$), tức pha rắn đặc hơn — đúng với đa số chất. Nước, bismut và gali là ngoại lệ: pha rắn nở ra nên $\Delta v<0$ và đường nóng chảy nghiêng trái.
- Áp dụng xấp xỉ $\Delta v\approx v_{\text{hơi}}$ cho chuyển pha rắn - lỏng. Xấp xỉ này chỉ hợp lệ khi một pha là khí loãng; với rắn - lỏng hai thể tích so sánh được và hiệu của chúng mới là đại lượng quyết định.
- Nghĩ chuyển pha bậc hai cũng có ẩn nhiệt. Theo định nghĩa $S$ liên tục nên $L=T\Delta s=0$; cái nhảy bậc nằm ở nhiệt dung, và đó là dấu hiệu thực nghiệm để phân loại.

<sub>`lesson.physics.nhiet-dong-thong-ke.chuyen-pha-va-clausius-clapeyron`</sub>

---

### 4. Tổng thống kê chính tắc và cầu nối với nhiệt động lực học
*The canonical partition function and the bridge to thermodynamics* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Thiết lập được phân bố chính tắc từ lập luận về hệ tiếp xúc với bể nhiệt
- Rút ra được mọi đại lượng nhiệt động từ tổng thống kê Z
- Vận dụng được Z cho hệ hạt độc lập và giải thích được nghịch lí Gibbs

## Vì sao có thừa số Boltzmann

Hệ nhỏ tiếp xúc với bể nhiệt lớn ở nhiệt độ $T$. Xác suất hệ ở vi trạng thái $s$ tỉ lệ với số vi trạng thái của **bể**, tức $e^{S_{\text{bể}}/k_B}$. Khai triển $S_{\text{bể}}(E_{\text{tổng}}-E_s)$ tới bậc nhất và dùng $\partial S/\partial E=1/T$:

$$P_s=\frac{e^{-E_s/k_BT}}{Z},\qquad Z=\sum_s e^{-\beta E_s},\quad \beta=\frac{1}{k_BT}$$

Cạnh tranh giữa hai xu hướng nằm ngay trong công thức: hệ "muốn" ở trạng thái năng lượng thấp, nhưng số trạng thái ở năng lượng cao lại nhiều hơn.

## Z là hàm sinh

Mọi thứ rút ra bằng cách lấy đạo hàm:

$$\langle E\rangle=-\frac{\partial\ln Z}{\partial\beta},\qquad F=-k_BT\ln Z,\qquad S=-\left(\frac{\partial F}{\partial T}\right)_V,\qquad p=-\left(\frac{\partial F}{\partial V}\right)_T$$

Đây là **cầu nối** giữa vi mô và vĩ mô: biết phổ năng lượng là biết toàn bộ nhiệt động lực học. Đạo hàm bậc hai cho thăng giáng: $\sigma_E^2=k_BT^2C_V$, nên độ thăng giáng tương đối cỡ $1/\sqrt N$ — với $N\sim10^{23}$ nó nhỏ tới mức các tổng thể khác nhau cho cùng kết quả.

## Hệ hạt độc lập

Nếu năng lượng cộng tính, $Z_N=z^N$ với $z$ là tổng thống kê một hạt. Nhưng với hạt **đồng nhất** trong giới hạn cổ điển phải viết

$$Z_N=\frac{z^N}{N!}$$

Bỏ $N!$ dẫn tới entropy không cộng tính (trộn hai bình cùng khí lại làm entropy tăng) — đó là nghịch lí Gibbs. Thừa số $N!$ sửa được vì các hoán vị của hạt đồng nhất không cho vi trạng thái mới; công thức Sackur - Tetrode thu được từ đó khớp thực nghiệm.

## Điều kiện áp dụng

Cách viết $Z_N=z^N/N!$ chỉ đúng khi số trạng thái khả dĩ lớn hơn nhiều số hạt, tức khi khả năng hai hạt cùng một trạng thái là không đáng kể. Điều kiện định lượng là $n\lambda_T^3\ll1$ với $\lambda_T$ là bước sóng nhiệt de Broglie; ngược lại phải dùng thống kê lượng tử.

**Lỗi thường gặp:**
- Chia $N!$ cho hệ các hạt định xứ. Nguyên tử trên các nút mạng tinh thể phân biệt được bằng vị trí, nên tổng thống kê là $z^N$; chia thêm $N!$ sẽ cho entropy sai.
- Coi $Z$ chỉ là một hằng số chuẩn hóa. $Z$ chứa toàn bộ thông tin nhiệt động qua $F=-k_BT\ln Z$; bỏ qua phụ thuộc của nó vào $V$ hay $T$ làm mất áp suất và entropy.
- Tính tổng trên các **mức năng lượng** mà quên bội suy biến. Tổng phải chạy trên vi trạng thái; nếu gộp theo mức thì mỗi số hạng phải nhân với độ suy biến $g_i$.

<sub>`lesson.physics.nhiet-dong-thong-ke.tong-thong-ke-chinh-tac`</sub>

---

### 5. Thống kê Maxwell - Boltzmann và định lí phân bố đều
*Maxwell-Boltzmann statistics and the equipartition theorem* · Đại học · intl-undergrad · 55 phút · trung-binh

**Mục tiêu:**
- Rút ra được phân bố Maxwell theo tốc độ từ phân bố Boltzmann
- Tính được các tốc độ đặc trưng của phân tử khí
- Phát biểu và vận dụng được định lí phân bố đều năng lượng cùng giới hạn của nó

## Từ Boltzmann tới Maxwell

Trong khí lí tưởng, năng lượng chỉ là động năng nên xác suất một phân tử có vận tốc $\vec v$ tỉ lệ $e^{-mv^2/2k_BT}$. Muốn phân bố theo **độ lớn** $v$, phải nhân thêm thể tích lớp vỏ cầu $4\pi v^2dv$ trong không gian vận tốc:

$$f(v)=4\pi\left(\frac{m}{2\pi k_BT}\right)^{3/2}v^2e^{-mv^2/2k_BT}$$

Chính thừa số $v^2$ này làm $f(0)=0$ và tạo ra cực đại — một chi tiết hay bị bỏ sót.

## Ba tốc độ đặc trưng

$$v_p=\sqrt{\frac{2k_BT}{m}}<\bar v=\sqrt{\frac{8k_BT}{\pi m}}<v_{rms}=\sqrt{\frac{3k_BT}{m}}$$

Thứ tự này luôn đúng vì phân bố lệch phải: đuôi tốc độ cao kéo trung bình lên. Tỉ lệ $1:1{,}128:1{,}225$ không phụ thuộc chất khí hay nhiệt độ.

## Phân bố đều năng lượng

Nếu năng lượng chứa số hạng bậc hai $ax^2$ với $x$ là một biến liên tục, thì tích phân Gauss cho $\langle ax^2\rangle=\tfrac12 k_BT$ — bất kể $a$ bằng bao nhiêu. Hệ quả:

- khí đơn nguyên tử: 3 bậc tịnh tiến, $U=\tfrac32Nk_BT$, $C_V=\tfrac32Nk_B$;
- khí hai nguyên tử ở nhiệt độ phòng: thêm 2 bậc quay, $C_V=\tfrac52Nk_B$;
- chất rắn: 3 động năng + 3 thế năng cho mỗi nguyên tử, $C=3Nk_B$ (định luật Dulong - Petit).

## Nơi lí thuyết cổ điển hỏng

Định lí phân bố đều giả thiết phổ năng lượng liên tục. Thực tế các mức lượng tử cách nhau $\Delta E$; khi $k_BT\ll\Delta E$ bậc tự do bị **đóng băng** và biến mất khỏi nhiệt dung. Vì thế $C_V$ của $H_2$ tăng theo bậc thang: $\tfrac32 R$ dưới $\sim80$ K (chỉ tịnh tiến), $\tfrac52 R$ ở nhiệt độ phòng (thêm quay), $\tfrac72 R$ trên $\sim1000$ K (thêm dao động). Cùng cơ chế đó giải thích vì sao nhiệt dung chất rắn giảm về 0 khi $T\to0$ thay vì giữ giá trị Dulong - Petit, và vì sao Rayleigh - Jeans thất bại với bức xạ vật đen.

**Lỗi thường gặp:**
- Nhầm phân bố theo vectơ vận tốc với phân bố theo độ lớn. Hàm theo $\vec v$ đạt cực đại tại $\vec v=0$, còn hàm theo $v$ triệt tiêu ở $v=0$ vì thừa số thể tích $4\pi v^2$.
- Áp dụng phân bố đều cho mọi bậc tự do ở mọi nhiệt độ. Bậc tự do dao động của phân tử hai nguyên tử bị đóng băng ở nhiệt độ phòng; dùng $C_V=\tfrac72R$ cho không khí sẽ sai khoảng 40%.
- Cho rằng $v_{rms}=\bar v$. Ba tốc độ đặc trưng khác nhau; dùng nhầm $v_{rms}$ khi tính số va chạm hay quãng đường tự do trung bình cho sai số hệ thống vài phần trăm tới hàng chục phần trăm.

<sub>`lesson.physics.nhiet-dong-thong-ke.thong-ke-maxwell-boltzmann`</sub>

---

### 6. Tổng thống kê lớn, thống kê Bose - Einstein và Fermi - Dirac
*Grand partition function, Bose-Einstein and Fermi-Dirac statistics* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Xây dựng được tổng thống kê lớn cho hệ trao đổi được hạt với bể
- Suy ra được số chiếm trung bình của boson và fermion từ tổng thống kê lớn
- Xác định được điều kiện chuyển sang giới hạn cổ điển Maxwell - Boltzmann

## Vì sao cần tổng thể lớn

Đếm trạng thái của $N$ boson hoặc fermion trong tổng thể chính tắc rất khó, vì ràng buộc "tổng số hạt bằng $N$" làm các trạng thái một hạt không độc lập. Mẹo: thả lỏng ràng buộc đó, cho hệ trao đổi hạt với bể, và bù lại bằng thế hóa học $\mu$.

$$\Xi=\sum_s e^{-\beta(E_s-\mu N_s)},\qquad \Omega=-k_BT\ln\Xi=-pV$$

Bây giờ mỗi trạng thái một hạt tiến hoá độc lập và $\Xi$ tách thành tích.

## Số chiếm của từng trạng thái

Với một trạng thái một hạt năng lượng $\varepsilon$:

- **Fermion**: chỉ $n=0$ hoặc $1$, nên $\xi=1+e^{-\beta(\varepsilon-\mu)}$;
- **Boson**: $n=0,1,2,\dots$, chuỗi hình học cho $\xi=\dfrac{1}{1-e^{-\beta(\varepsilon-\mu)}}$ (hội tụ khi $\varepsilon>\mu$).

Lấy $\bar n=k_BT\,\partial\ln\xi/\partial\mu$:

$$\bar n(\varepsilon)=\frac{1}{e^{(\varepsilon-\mu)/k_BT}\pm1}\qquad(+:\text{Fermi - Dirac},\ -:\text{Bose - Einstein})$$

Dấu duy nhất này tạo ra hai thế giới hoàn toàn khác nhau.

## Đọc hai phân bố

Fermi - Dirac không bao giờ vượt 1 — đúng như Pauli đòi hỏi. Ở $T=0$ nó là hàm bậc thang: mọi trạng thái dưới $\mu=E_F$ đầy, trên đó trống.

Bose - Einstein có thể lớn tùy ý, và phân kì khi $\varepsilon\to\mu$. Điều này buộc $\mu\le\varepsilon_{\min}$ với boson, và khi $\mu$ tiến sát mức thấp nhất thì xảy ra ngưng tụ.

## Giới hạn cổ điển

Khi $e^{(\varepsilon-\mu)/k_BT}\gg1$, số $\pm1$ ở mẫu không còn quan trọng và cả hai rút về $\bar n\approx e^{-(\varepsilon-\mu)/k_BT}$ — phân bố Maxwell - Boltzmann. Điều kiện tương đương: $n\lambda_T^3\ll1$ với $\lambda_T=\dfrac{h}{\sqrt{2\pi mk_BT}}$, nghĩa là các bó sóng không chồng lấn. Không khí ở điều kiện thường có $n\lambda_T^3\sim10^{-7}$ nên hoàn toàn cổ điển; electron dẫn trong kim loại có $n\lambda_T^3\sim10^{3}$ nên hoàn toàn suy biến.

**Lỗi thường gặp:**
- Cho rằng thế hóa học luôn âm. Với khí lí tưởng loãng thì $\mu<0$, nhưng với khí Fermi suy biến $\mu\approx E_F>0$; dấu của $\mu$ phụ thuộc chế độ chứ không cố định.
- Dùng phân bố Bose - Einstein với $\mu$ lớn hơn mức năng lượng thấp nhất. Khi đó $\bar n$ âm — vô nghĩa; ràng buộc $\mu\le\varepsilon_0$ là bắt buộc và chính nó dẫn tới ngưng tụ Bose - Einstein.
- Kết luận vì nhiệt độ phòng "cao" nên mọi hệ đều cổ điển. Tiêu chuẩn không phải nhiệt độ tuyệt đối mà là $n\lambda_T^3$; mật độ cao hoặc khối lượng nhỏ đều đẩy hệ vào chế độ lượng tử.

<sub>`lesson.physics.nhiet-dong-thong-ke.tong-thong-ke-lon-va-thong-ke-luong-tu`</sub>

---

### 7. Khí Fermi suy biến và năng lượng Fermi
*The degenerate Fermi gas and the Fermi energy* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Tính được năng lượng Fermi từ mật độ hạt
- Giải thích được vì sao nhiệt dung electron tuyến tính theo nhiệt độ
- Vận dụng được áp suất suy biến để phân tích sự bền của sao lùn trắng

## Ở $T=0$: biển Fermi

Fermion không được chồng lên nhau, nên ở nhiệt độ không chúng lấp đầy các trạng thái từ thấp lên cho tới mức $E_F$. Trong không gian động lượng, vùng bị chiếm là một quả cầu bán kính $p_F$. Đếm trạng thái (kể spin 2) cho

$$E_F=\frac{\hbar^2}{2m}\left(3\pi^2n\right)^{2/3},\qquad g(\varepsilon)\propto\sqrt\varepsilon$$

Năng lượng trung bình mỗi electron là $\tfrac35E_F$, **không** phải 0 — đây là năng lượng thuần lượng tử, không liên quan gì tới nhiệt.

## Nhiệt độ Fermi và ý nghĩa của "suy biến"

$T_F=E_F/k_B$ với kim loại điển hình cỡ $5\cdot10^4$ K. Vì $T\ll T_F$ ở mọi điều kiện thực tế, chỉ một phần nhỏ $\sim T/T_F$ electron gần mặt Fermi mới bị kích thích nhiệt; phần còn lại bị "khoá" vì mọi trạng thái lân cận đã đầy.

## Hệ quả: nhiệt dung tuyến tính

Số electron hoạt động $\sim N\dfrac{T}{T_F}$, mỗi electron mang thêm $\sim k_BT$, nên $U\sim Nk_B\dfrac{T^2}{T_F}$ và

$$C_e=\frac{\pi^2}{2}Nk_B\frac{T}{T_F}$$

(hệ số chính xác từ khai triển Sommerfeld). Điều này giải quyết một nghịch lí lớn của lí thuyết cổ điển: nếu mỗi electron đóng góp $\tfrac32k_B$ như phân bố đều đòi hỏi, nhiệt dung kim loại phải lớn hơn đo được cả trăm lần. Ở nhiệt độ thấp, $C=\gamma T+AT^3$ — số hạng đầu của electron, số hạng sau của phonon.

## Áp suất suy biến

$$p=\frac{2}{5}nE_F\propto n^{5/3}$$

Áp suất này tồn tại ở $T=0$ và không giảm khi làm lạnh. Nó là thứ giữ cho sao lùn trắng khỏi sụp đổ: khi khối lượng tăng, mật độ tăng, áp suất suy biến tăng theo $n^{5/3}$ nhưng hấp dẫn tăng nhanh hơn khi electron trở nên tương đối tính ($p\propto n^{4/3}$). Cân bằng mất khi vượt **giới hạn Chandrasekhar** $\approx1{,}4M_\odot$, sau đó sao sụp thành sao neutron hoặc lỗ đen.

**Lỗi thường gặp:**
- Cho rằng ở $T=0$ mọi electron đều có năng lượng bằng 0. Nguyên lí Pauli buộc chúng xếp chồng lên tới $E_F$; năng lượng trung bình $\tfrac35E_F$ vẫn rất lớn.
- Dùng định lí phân bố đều cho electron dẫn. Chỉ phần $T/T_F$ electron gần mặt Fermi được kích thích nhiệt, nên đóng góp thực tế nhỏ hơn giá trị cổ điển gần hai bậc.
- Áp dụng $p\propto n^{5/3}$ cho mọi mật độ khi tính giới hạn Chandrasekhar. Ở mật độ cực cao electron trở nên tương đối tính và $p\propto n^{4/3}$; chính sự đổi số mũ này tạo ra khối lượng tới hạn.

<sub>`lesson.physics.nhiet-dong-thong-ke.khi-fermi-suy-bien`</sub>

---

### 8. Ngưng tụ Bose - Einstein
*Bose-Einstein condensation* · Đại học · intl-undergrad · 55 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được cơ chế dẫn tới ngưng tụ khi thế hóa học tiến tới mức cơ bản
- Tính được nhiệt độ tới hạn của ngưng tụ Bose - Einstein
- Phân tích được dáng điệu của phần ngưng tụ và nhiệt dung dưới nhiệt độ tới hạn

## Một sự cố tính toán hoá ra là vật lí

Với boson, tổng số hạt là $N=\sum_\varepsilon\dfrac{1}{e^{(\varepsilon-\mu)/k_BT}-1}$. Thay tổng bằng tích phân với $g(\varepsilon)\propto\sqrt\varepsilon$, ta thấy khi hạ $T$ ở $N$ cố định, $\mu$ phải tăng dần lên tới mức cơ bản $\varepsilon_0$. Nhưng $\mu$ **không được vượt** $\varepsilon_0$, và ở $\mu=\varepsilon_0$ tích phân cho một số hữu hạn:

$$N_{\text{kích thích}}^{\max}=2{,}612\,\frac{V}{\lambda_T^3}$$

Nếu $N$ lớn hơn con số đó, phần dư phải đi đâu? Câu trả lời: chúng dồn hết vào trạng thái cơ bản — thứ mà phép thay tổng bằng tích phân đã vô tình bỏ sót vì $g(0)=0$.

## Nhiệt độ tới hạn

Đặt $n\lambda_T^3=2{,}612$:

$$T_c=\frac{2\pi\hbar^2}{mk_B}\left(\frac{n}{2{,}612}\right)^{2/3}$$

Dưới $T_c$, phần hạt ở trạng thái cơ bản là

$$\frac{N_0}{N}=1-\left(\frac{T}{T_c}\right)^{3/2}$$

## Điều làm BEC đặc biệt

Đây là chuyển pha **không cần tương tác**: nó xảy ra ngay cả với khí lí tưởng, thuần tuý do thống kê Bose. Chuyển pha xảy ra trong không gian động lượng chứ không phải không gian thực.

Nhiệt dung tăng theo $T^{3/2}$ dưới $T_c$, đạt cực đại tại $T_c$ rồi giảm về giá trị cổ điển $\tfrac32Nk_B$ — có điểm gãy tại $T_c$, dấu hiệu của chuyển pha.

## Thực nghiệm

Cornell, Wieman và Ketterle (1995, Nobel 2001) tạo BEC từ hơi rubidi và natri ở cỡ $100$ nK, dùng làm lạnh laser rồi làm lạnh bay hơi. Với $n\sim10^{19}$ m⁻³, công thức trên cho $T_c$ đúng cỡ đó. Heli-4 siêu chảy dưới $2{,}17$ K liên quan chặt tới BEC nhưng tương tác mạnh làm chỉ khoảng $10\%$ nguyên tử thực sự ở trạng thái ngưng tụ.

## Giới hạn của mô hình

Khí lí tưởng cho $T_c$ đúng bậc độ lớn nhưng không giải thích được siêu chảy: dòng không nhớt đòi hỏi phổ kích thích kiểu phonon, tức là hệ quả của **tương tác** giữa các hạt (lí thuyết Bogoliubov, tiêu chuẩn Landau).

**Lỗi thường gặp:**
- Cho rằng ngưng tụ Bose - Einstein là hiện tượng hoá lỏng thông thường. Nó xảy ra trong không gian **động lượng**: các nguyên tử vẫn phân tán trong không gian thực nhưng cùng chiếm một trạng thái lượng tử.
- Áp dụng phép thay tổng bằng tích phân mà không tách riêng trạng thái cơ bản. Vì $g(\varepsilon)\propto\sqrt\varepsilon$ triệt tiêu tại 0, tích phân bỏ sót đúng số hạng chứa toàn bộ hiện tượng.
- Đồng nhất BEC với siêu chảy. BEC xảy ra ở khí lí tưởng nhưng khí lí tưởng ngưng tụ **không** siêu chảy; tính siêu chảy đòi hỏi tương tác để phổ kích thích ở vùng $k$ nhỏ là tuyến tính.

<sub>`lesson.physics.nhiet-dong-thong-ke.ngung-tu-bose-einstein`</sub>

---

### 9. Khí photon và bức xạ vật đen từ thống kê Bose
*The photon gas and blackbody radiation from Bose statistics* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao thế hóa học của photon bằng không
- Rút ra được công thức Planck từ phân bố Bose - Einstein và mật độ mode
- Suy ra được định luật Stefan - Boltzmann và định luật dịch chuyển Wien

## Vì sao $\mu=0$

Photon bị thành hốc hấp thụ và phát ra tự do — số photon **không bảo toàn**. Ở cân bằng, hệ tự chọn số photon làm cực tiểu thế Helmholtz, tức $\left(\partial F/\partial N\right)_{T,V}=\mu=0$. Đây là điểm khác biệt then chốt so với khí nguyên tử, và nó giải thích vì sao khí photon không bao giờ ngưng tụ: hạ nhiệt độ chỉ làm photon biến mất chứ không dồn xuống mức thấp nhất.

## Ghép hai mảnh

Số chiếm trung bình mỗi mode: $\bar n=\dfrac{1}{e^{h\nu/k_BT}-1}$. Số mode trên đơn vị thể tích và đơn vị tần số: $\dfrac{8\pi\nu^2}{c^3}$. Nhân với năng lượng mỗi photon $h\nu$:

$$u(\nu,T)=\frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT}-1}$$

Đây chính là công thức Planck, nhưng lần này **không** phải giả thiết mà là hệ quả của thống kê Bose. Ở $h\nu\ll k_BT$ khai triển mẫu số cho Rayleigh - Jeans; ở $h\nu\gg k_BT$ thừa số mũ cắt phổ, dập tắt khủng hoảng tử ngoại.

## Ba hệ quả

Tích phân trên mọi tần số dùng $\int_0^\infty\dfrac{x^3dx}{e^x-1}=\dfrac{\pi^4}{15}$:

$$u=aT^4,\qquad j^*=\sigma T^4,\qquad \sigma=\frac{2\pi^5k_B^4}{15h^3c^2}=5{,}67\cdot10^{-8}\ \frac{\text{W}}{\text{m}^2\text{K}^4}$$

Đạo hàm phổ theo $\lambda$ và cho bằng 0 cho **định luật Wien** $\lambda_{\max}T=2{,}898\cdot10^{-3}$ m·K.

Nhiệt động lực học của khí photon cũng đặc biệt: $p=u/3$ (khác $2u/3$ của khí phi tương đối tính) và $S\propto VT^3$, nên số photon tỉ lệ $VT^3$.

## Ứng dụng

Nhiệt độ bề mặt sao đọc được từ $\lambda_{\max}$; bức xạ nền vi sóng vũ trụ là phổ Planck hoàn hảo nhất từng đo với $T=2{,}725$ K; cân bằng bức xạ quyết định nhiệt độ hành tinh và hiệu ứng nhà kính.

**Lỗi thường gặp:**
- Gán thế hóa học khác không cho photon. Vì số photon không bảo toàn, cân bằng nhiệt buộc $\mu=0$; giữ $\mu\neq0$ sẽ cho phổ sai và tiên đoán sai về ngưng tụ.
- Nhầm hai dạng phổ: cực đại của $u(\nu)$ và cực đại của $u(\lambda)$ **không** ứng với cùng một photon. Vì $d\nu=-\dfrac{c}{\lambda^2}d\lambda$, hai định luật Wien có hằng số khác nhau; dùng lẫn cho sai số khoảng $70\%$.
- Áp dụng $p=\tfrac23 u$ cho khí photon. Photon tương đối tính với $\varepsilon=pc$ nên áp suất bức xạ là $u/3$; dùng công thức khí phi tương đối tính sẽ sai cả trong cấu trúc sao lẫn trong áp suất bức xạ.

<sub>`lesson.physics.nhiet-dong-thong-ke.khi-photon-va-buc-xa-vat-den`</sub>

---

### 10. Nhiệt dung chất rắn: mô hình Einstein và Debye
*Heat capacity of solids: the Einstein and Debye models* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao định luật Dulong - Petit thất bại ở nhiệt độ thấp
- So sánh được giả thiết và tiên đoán của mô hình Einstein và mô hình Debye
- Vận dụng được định luật T³ của Debye để phân tích số liệu thực nghiệm

## Bài toán

Định luật Dulong - Petit ($C=3Nk_B$) đúng ở nhiệt độ phòng nhưng thực nghiệm cho $C\to0$ khi $T\to0$. Vật lí cổ điển không giải thích nổi, vì phân bố đều không có tham số nào phụ thuộc nhiệt độ.

## Einstein (1907): lượng tử hóa dao động

Coi mỗi nguyên tử là ba dao động tử độc lập cùng tần số $\omega_E$. Từ tổng thống kê một dao động tử:

$$C=3Nk_B\left(\frac{\Theta_E}{T}\right)^2\frac{e^{\Theta_E/T}}{\left(e^{\Theta_E/T}-1\right)^2}$$

Ở $T\gg\Theta_E$ cho Dulong - Petit; ở $T\to0$ cho $C\to0$. Đây là lần đầu tiên ý tưởng lượng tử được dùng ngoài bức xạ, và nó **giải thích đúng về mặt định tính**.

Nhưng Einstein tiên đoán $C\propto e^{-\Theta_E/T}$ ở nhiệt độ thấp, trong khi thực nghiệm cho $C\propto T^3$ — giảm chậm hơn nhiều. Nguyên nhân: giả thiết mọi dao động tử cùng tần số là sai; các mode sóng dài có tần số rất thấp và vẫn được kích thích ở nhiệt độ thấp.

## Debye (1912): sóng đàn hồi tập thể

Thay dao động độc lập bằng các mode sóng âm với $\omega=vk$ — chính xác cùng bài toán như khí photon, chỉ khác hai điểm: vận tốc là vận tốc âm và có **ba** phân cực (một dọc, hai ngang). Thêm một điểm mấu chốt: số mode hữu hạn, đúng bằng $3N$, nên phổ bị cắt ở $\omega_D$.

$$C=9Nk_B\left(\frac{T}{\Theta_D}\right)^3\int_0^{\Theta_D/T}\frac{x^4e^x}{(e^x-1)^2}dx$$

Ở $T\ll\Theta_D$, cận trên tiến ra vô cùng và tích phân thành hằng số:

$$C=\frac{12\pi^4}{5}Nk_B\left(\frac{T}{\Theta_D}\right)^3$$

## Kiểm chứng

Vẽ $C/T$ theo $T^2$ với kim loại ở nhiệt độ thấp cho đường thẳng: tung độ gốc là $\gamma$ (electron), độ dốc là số hạng Debye. Đây là cách chuẩn để tách hai đóng góp và đo $\Theta_D$ ($428$ K cho nhôm, $2230$ K cho kim cương — vật liệu càng cứng, nguyên tử càng nhẹ thì $\Theta_D$ càng cao).

Mô hình Debye vẫn là gần đúng: phổ phonon thật không tuyến tính ở vùng biên vùng Brillouin, nên $\Theta_D$ suy từ thực nghiệm hơi phụ thuộc nhiệt độ.

**Lỗi thường gặp:**
- Dùng định luật $T^3$ ở nhiệt độ so sánh được với $\Theta_D$. Dạng tiệm cận chỉ đúng khi $T\ll\Theta_D$; ở nhiệt độ cao nó cho giá trị vượt xa Dulong - Petit, điều vô lí.
- Bỏ qua đóng góp electron khi phân tích kim loại ở nhiệt độ rất thấp. Vì $C_e\propto T$ giảm chậm hơn $T^3$, dưới vài kelvin electron lại chiếm ưu thế.
- Coi mô hình Einstein là hoàn toàn sai. Nó vẫn mô tả tốt các mode quang học (gần như cùng tần số) trong tinh thể nhiều nguyên tử; thực tế người ta thường dùng Debye cho mode âm và Einstein cho mode quang.

<sub>`lesson.physics.nhiet-dong-thong-ke.nhiet-dung-chat-ran-einstein-debye`</sub>

---

### 11. Mô hình Ising và xấp xỉ trường trung bình
*The Ising model and the mean-field approximation* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Viết được Hamiltonian của mô hình Ising và giải thích ý nghĩa từng số hạng
- Thiết lập được phương trình tự hợp của xấp xỉ trường trung bình
- Phân tích được sự xuất hiện của từ hóa tự phát dưới nhiệt độ Curie

## Mô hình tối giản của chuyển pha

$$\hat H=-J\sum_{\langle ij\rangle}s_is_j-h\sum_i s_i,\qquad s_i=\pm1$$

$J>0$ ưu ái spin lân cận song song (sắt từ). Cuộc chiến rất rõ: năng lượng muốn trật tự, entropy muốn hỗn loạn. Nhiệt độ quyết định bên nào thắng.

Mô hình này đơn giản tới mức tưởng như tầm thường, nhưng chỉ giải chính xác được trong một chiều (Ising, không có chuyển pha) và hai chiều không từ trường (Onsager 1944, có chuyển pha với $k_BT_c/J=2/\ln(1+\sqrt2)\approx2{,}269$). Ba chiều đến nay vẫn chưa có lời giải chính xác.

## Trường trung bình

Viết $s_j=m+\delta s_j$ với $m=\langle s\rangle$, rồi **bỏ** tích các thăng giáng $\delta s_i\delta s_j$. Mỗi spin khi đó chỉ thấy một trường hiệu dụng $h_{\text{eff}}=zJm+h$ với $z$ là số lân cận. Bài toán nhiều hạt tương tác đã thành bài toán một spin trong trường ngoài, giải ngay được:

$$m=\tanh\left(\frac{zJm+h}{k_BT}\right)$$

Đây là phương trình **tự hợp**: $m$ xuất hiện cả hai vế.

## Đọc nghiệm

Với $h=0$, so sánh độ dốc của $\tanh(zJm/k_BT)$ tại gốc với đường thẳng $y=m$:

- nếu $zJ/k_BT<1$: chỉ có nghiệm $m=0$ — pha thuận từ;
- nếu $zJ/k_BT>1$: xuất hiện thêm hai nghiệm $\pm m\neq0$ — **từ hóa tự phát**.

Ngưỡng cho nhiệt độ Curie $k_BT_c=zJ$. Gần $T_c$, khai triển $\tanh$ tới bậc ba cho $m\propto(T_c-T)^{1/2}$, tức số mũ tới hạn $\beta=1/2$. Trên $T_c$, độ cảm phân kì theo định luật Curie - Weiss $\chi\propto(T-T_c)^{-1}$.

## Trường trung bình sai ở đâu

Nó bỏ qua thăng giáng, nên: tiên đoán có chuyển pha ngay cả trong một chiều (sai); cho $T_c$ cao hơn thực tế; và cho số mũ tới hạn sai ($\beta=1/2$ so với $1/8$ ở 2D, $\approx0{,}326$ ở 3D). Xấp xỉ càng tốt khi $z$ càng lớn, tức số chiều càng cao — trên bốn chiều nó trở thành chính xác. Bù lại, nó rất dễ tính và nắm được điều cốt lõi: **phá vỡ đối xứng tự phát**. Cùng cấu trúc toán học tái xuất ở lí thuyết BCS về siêu dẫn và ở khai triển Landau.

**Lỗi thường gặp:**
- Cho rằng mô hình Ising một chiều có chuyển pha vì trường trung bình nói vậy. Lời giải chính xác cho thấy trong một chiều thăng giáng phá hủy trật tự ở mọi $T>0$; đây là dấu hiệu rõ nhất về giới hạn của xấp xỉ.
- Coi $m$ trong phương trình tự hợp là dữ liệu đầu vào. Nó là ẩn số phải giải, và chính tính tự hợp mới sinh ra chuyển pha; thay một giá trị $m$ cố định làm mất hoàn toàn hiện tượng.
- Kết luận số mũ tới hạn phụ thuộc chi tiết vật liệu. Chúng chỉ phụ thuộc số chiều và tính đối xứng của tham số trật tự — tính phổ quát này là kết quả sâu sắc nhất của lí thuyết hiện tượng tới hạn.

<sub>`lesson.physics.nhiet-dong-thong-ke.mo-hinh-ising-va-truong-trung-binh`</sub>

---

## Unit 5: Electrodynamics and AC Circuits

### 1. Mạch RLC, Phương pháp trở kháng phức và Định luật Ohm vi phân
*AC circuits: Complex impedance, resonance, and differential Ohm's law* · Đại học · intl-undergrad, vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Thiết lập phương trình vi phân cho mạch dao động LC và RLC nối tiếp
- Vận dụng phương pháp số phức và trở kháng phức để giải mạch điện xoay chiều
- Phân tích công suất biểu kiến, hệ số công suất và định luật Ohm dạng vi phân

## Phương trình vi phân mạch RLC

Áp dụng định luật Kirchhoff cho mạch RLC nối tiếp:

$$L \frac{d^2 q}{dt^2} + R \frac{dq}{dt} + \frac{1}{C} q = u(t)$$

Khi $R = 0$ và $u(t) = 0$, ta có dao động tự do với công thức Thomson cho chu kì riêng: $T_0 = 2\pi \sqrt{LC}$.

## Phương pháp Trở kháng phức

Chuyển sang miền biến đổi phức $u(t) = U_0 e^{i\omega t}$, dòng điện là $i(t) = I_0 e^{i(\omega t - \varphi)}$ với $\dot{I} = \frac{\dot{U}}{Z}$. Trở kháng phức:

$$Z = R + i \left(\omega L - \frac{1}{\omega C}\right)$$

Cộng hưởng xảy ra khi phần ảo triệt tiêu: $\omega_{ch} = \frac{1}{\sqrt{LC}}$.

**Lỗi thường gặp:**
- Quên dấu trừ khi biểu diễn dung kháng dưới dạng phức: Z_C = 1/(i*omega*C) = -i/(omega*C)
- Nhầm lẫn giữa công suất tác dụng P = U*I*cos(phi) và công suất toàn phần S = U*I

<sub>`lesson.physics.undergrad-physics.mach-rlc-tro-khang-phuc-va-cong-huong`</sub>

---

## Unit 5: Vật lí chất rắn, hạt nhân và hạt cơ bản

### 1. Cấu trúc tinh thể và nhiễu xạ tia X
*Crystal structure and X-ray diffraction* · Đại học · intl-undergrad · 50 phút · trung-binh

**Mục tiêu:**
- Mô tả được mạng Bravais, ô cơ sở và bazơ nguyên tử
- Vận dụng được định luật Bragg để xác định hằng số mạng
- Tính được hệ số lấp đầy và mật độ khối lượng của các cấu trúc lập phương

## Tinh thể = mạng + bazơ

Cấu trúc tinh thể được mô tả bằng hai thành phần độc lập: một **mạng Bravais** (tập điểm tuần hoàn) và một **bazơ** (nhóm nguyên tử gắn tại mỗi điểm mạng). Kim cương chẳng hạn là mạng lập phương tâm mặt với bazơ gồm hai nguyên tử cacbon.

Trong không gian ba chiều có đúng 14 mạng Bravais và 230 nhóm không gian — kết quả của lí thuyết nhóm, không phải liệt kê thô.

## Ba cấu trúc lập phương

| Cấu trúc | Số nguyên tử/ô | Số lân cận | Hệ số lấp đầy |
|---|---|---|---|
| Lập phương đơn giản | 1 | 6 | $0{,}52$ |
| Lập phương tâm khối | 2 | 8 | $0{,}68$ |
| Lập phương tâm mặt | 4 | 12 | $0{,}74$ |

Hệ số $0{,}74$ của tâm mặt là mật độ xếp cầu lớn nhất có thể (giả thuyết Kepler, đã được chứng minh). Các kim loại thường chọn cấu trúc xếp chặt vì liên kết kim loại không định hướng.

## Nhiễu xạ: nhìn thấy mạng

Muốn "nhìn" khoảng cách cỡ $10^{-10}$ m cần bức xạ có bước sóng cùng cỡ, tức tia X, hoặc neutron nhiệt, hoặc electron vài chục keV. Điều kiện giao thoa tăng cường từ các mặt cách nhau $d$:

$$2d\sin\theta=n\lambda$$

Với mạng lập phương, $d_{hkl}=\dfrac{a}{\sqrt{h^2+k^2+l^2}}$, nên đo tập các góc $\theta$ là suy ra được cả $a$ lẫn kiểu mạng.

## Vì sao một số vạch biến mất

Không phải mọi $(hkl)$ đều cho vạch. Thừa số cấu trúc $F_{hkl}=\sum_j f_je^{2\pi i(hx_j+ky_j+lz_j)}$ có thể triệt tiêu do giao thoa **trong** ô cơ sở: mạng tâm khối chỉ cho vạch khi $h+k+l$ chẵn, mạng tâm mặt chỉ khi $h,k,l$ cùng chẵn hoặc cùng lẻ. Chính các "vạch tắt" này là dấu vân tay để phân biệt kiểu mạng.

## Ứng dụng

Từ nhiễu xạ tia X mà Watson - Crick - Franklin xác định cấu trúc xoắn kép của ADN; ngày nay tinh thể học protein và nhiễu xạ neutron (nhạy với nguyên tử nhẹ và với spin) là công cụ tiêu chuẩn.

**Lỗi thường gặp:**
- Cho rằng góc trong định luật Bragg đo từ pháp tuyến của mặt phẳng. Góc $\theta$ đo từ **mặt phẳng**, khác quy ước quang hình học; nhầm lẫn này làm sai hẳn kết quả.
- Kì vọng mọi họ mặt $(hkl)$ đều cho vạch nhiễu xạ. Thừa số cấu trúc triệt tiêu nhiều vạch; chính tập vạch tắt mới cho biết kiểu mạng Bravais.
- Đếm nguyên tử trong ô cơ sở mà quên chia sẻ với ô lân cận. Nguyên tử ở đỉnh thuộc 8 ô nên chỉ tính $1/8$, ở mặt thuộc 2 ô nên tính $1/2$; bỏ qua điều này làm mật độ tính ra sai vài lần.

<sub>`lesson.physics.chat-ran-hat-nhan.cau-truc-tinh-the-va-nhieu-xa`</sub>

---

### 2. Mạng đảo, vùng Brillouin và định lí Bloch
*The reciprocal lattice, Brillouin zones and Bloch's theorem* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Xây dựng được vectơ cơ sở của mạng đảo từ mạng thực
- Giải thích được điều kiện nhiễu xạ Laue và liên hệ với biên vùng Brillouin
- Phát biểu được định lí Bloch và ý nghĩa của vectơ sóng tinh thể

## Vì sao cần một mạng thứ hai

Mọi đại lượng vật lí trong tinh thể đều tuần hoàn theo mạng, nên khai triển Fourier là công cụ tự nhiên. Các vectơ sóng xuất hiện trong khai triển đó lập thành **mạng đảo**:

$$\vec b_1=2\pi\frac{\vec a_2\times\vec a_3}{\vec a_1\cdot(\vec a_2\times\vec a_3)}$$

cùng hoán vị vòng quanh, thoả $\vec b_i\cdot\vec a_j=2\pi\delta_{ij}$. Mạng thực lập phương tâm mặt có mạng đảo lập phương tâm khối và ngược lại.

## Nhiễu xạ nhìn lại

Điều kiện Laue: nhiễu xạ xảy ra khi $\Delta\vec k=\vec G$ với $\vec G$ là vectơ mạng đảo. Kết hợp với tán xạ đàn hồi $|\vec k'|=|\vec k|$ suy ra $\vec k\cdot\hat G=|G|/2$ — nghĩa là mũi vectơ $\vec k$ nằm trên **mặt phẳng trung trực** của $\vec G$. Các mặt phẳng đó chính là biên vùng Brillouin. Bragg và Laue chỉ là hai cách phát biểu của cùng một điều kiện.

## Định lí Bloch

Thế tuần hoàn $V(\vec r+\vec R)=V(\vec r)$ giao hoán với phép tịnh tiến mạng, nên hàm riêng có thể chọn đồng thời là hàm riêng của phép tịnh tiến:

$$\psi_{\vec k}(\vec r)=e^{i\vec k\cdot\vec r}u_{\vec k}(\vec r),\qquad u_{\vec k}(\vec r+\vec R)=u_{\vec k}(\vec r)$$

Hệ quả trọng đại: electron trong tinh thể **hoàn hảo** không bị tán xạ. Điện trở không đến từ các ion đứng yên mà từ sai lệch khỏi tính tuần hoàn — dao động nhiệt (phonon), tạp chất, khuyết tật. Điều này giải thích vì sao điện trở kim loại giảm khi hạ nhiệt độ.

## Vectơ sóng tinh thể

$\hbar\vec k$ **không** phải động lượng thật của electron mà là động lượng tinh thể: nó chỉ bảo toàn theo modulo $\hbar\vec G$, vì mạng có thể nhận một lượng động lượng $\hbar\vec G$. Vì $\vec k$ và $\vec k+\vec G$ mô tả cùng một trạng thái, mọi thông tin đều nằm gọn trong vùng Brillouin thứ nhất — đó là lí do mọi giản đồ dải năng lượng và phổ phonon đều vẽ trong vùng này.

**Lỗi thường gặp:**
- Coi $\hbar\vec k$ của electron Bloch là động lượng thật. Nó là động lượng tinh thể, chỉ bảo toàn tới một vectơ mạng đảo; dùng như động lượng thật cho kết luận sai về quá trình umklapp và tán xạ phonon.
- Cho rằng mạng đảo có cùng kiểu với mạng thực. Lập phương tâm mặt có mạng đảo tâm khối và ngược lại; nhầm lẫn này làm vẽ sai hình dạng vùng Brillouin.
- Nghĩ rằng các trạng thái ngoài vùng Brillouin thứ nhất là trạng thái mới. Vì $\psi_{\vec k+\vec G}$ mô tả cùng trạng thái vật lí như $\psi_{\vec k}$, đếm chúng riêng sẽ nhân đôi số trạng thái.

<sub>`lesson.physics.chat-ran-hat-nhan.mang-dao-va-vung-brillouin`</sub>

---

### 3. Dao động mạng và phonon
*Lattice vibrations and phonons* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Thiết lập được hệ thức tán sắc của chuỗi nguyên tử một chiều
- Phân biệt được nhánh âm và nhánh quang trong tinh thể có bazơ hai nguyên tử
- Giải thích được vai trò của phonon trong nhiệt dung và dẫn nhiệt

## Chuỗi một nguyên tử

Cho $N$ nguyên tử khối lượng $M$ nối bằng lò xo $C$, khoảng cách $a$. Phương trình chuyển động của nguyên tử thứ $n$ và nghiệm dạng sóng $u_n\propto e^{i(kna-\omega t)}$ cho

$$\omega(k)=2\sqrt{\frac{C}{M}}\left|\sin\frac{ka}{2}\right|$$

Ba điều đọc ra ngay. Ở $k$ nhỏ, $\omega\approx a\sqrt{C/M}\,k$: tuyến tính, chính là sóng âm với vận tốc $v=a\sqrt{C/M}$. Ở biên vùng $k=\pi/a$, $d\omega/dk=0$: sóng dừng, không truyền năng lượng. Và $\omega(k)$ tuần hoàn theo mạng đảo, xác nhận mọi thông tin nằm trong vùng Brillouin thứ nhất.

## Bazơ hai nguyên tử: xuất hiện nhánh quang

Với hai khối lượng $M_1,M_2$ xen kẽ, bài toán trị riêng $2\times2$ cho hai nghiệm. Nhánh dưới (âm) có $\omega\to0$ khi $k\to0$ — hai nguyên tử dao động cùng pha, tức toàn ô tịnh tiến. Nhánh trên (quang) có $\omega(0)=\sqrt{2C\left(\frac{1}{M_1}+\frac{1}{M_2}\right)}\neq0$ — hai nguyên tử dao động ngược pha, khối tâm đứng yên.

Nếu hai nguyên tử mang điện trái dấu (NaCl, GaAs), dao động ngược pha tạo lưỡng cực dao động, ghép mạnh với ánh sáng hồng ngoại — đó là nguồn gốc tên gọi "quang" và là cơ sở của phổ hấp thụ hồng ngoại chất rắn.

Với $p$ nguyên tử trong ô cơ sở và $d$ chiều: có $d$ nhánh âm và $d(p-1)$ nhánh quang.

## Lượng tử hóa

Mỗi mode chuẩn là một dao động tử điều hòa, nên năng lượng của nó là $\left(n+\tfrac12\right)\hbar\omega$. Ta gọi $n$ là số **phonon**. Vì số phonon không bảo toàn, chúng có $\mu=0$ và tuân theo phân bố Bose - Einstein $\bar n=\dfrac{1}{e^{\hbar\omega/k_BT}-1}$ — hệt như photon. Mô hình Debye chính là áp dụng bức tranh này với phổ tuyến tính bị cắt.

## Phonon làm gì

Chúng chở phần lớn nhiệt trong chất cách điện; dẫn nhiệt bị giới hạn bởi tán xạ phonon - phonon quá trình umklapp (chỉ có nhờ mạng nhận được $\hbar\vec G$). Chúng tán xạ electron, gây điện trở phụ thuộc nhiệt độ. Và tương tác electron - phonon là cơ chế ghép cặp Cooper trong siêu dẫn thường.

**Lỗi thường gặp:**
- Coi phonon là hạt thật có động lượng $\hbar k$. Phonon là quasihạt tồn tại nhờ môi trường; động lượng tinh thể của chúng chỉ bảo toàn tới một vectơ mạng đảo, và quá trình umklapp khai thác đúng điều đó.
- Cho rằng mọi tinh thể đều có nhánh quang. Tinh thể có một nguyên tử trong ô cơ sở (nhiều kim loại đơn chất) chỉ có nhánh âm; nhánh quang đòi hỏi bazơ có ít nhất hai nguyên tử.
- Dùng hệ thức tán sắc tuyến tính $\omega=vk$ trên toàn vùng Brillouin. Nó chỉ đúng ở $k$ nhỏ; gần biên vùng $\omega$ bão hòa và vận tốc nhóm tiến về 0, làm mô hình Debye kém chính xác ở nhiệt độ trung gian.

<sub>`lesson.physics.chat-ran-hat-nhan.dao-dong-mang-va-phonon`</sub>

---

### 4. Khí electron tự do và lí thuyết dải năng lượng
*Free-electron gas and band theory* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Trình bày được thành công và hạn chế của mô hình electron tự do
- Giải thích được sự hình thành vùng cấm tại biên vùng Brillouin
- Phân loại được kim loại, bán dẫn và điện môi theo cách lấp đầy dải

## Mô hình Drude - Sommerfeld: được và mất

Coi electron dẫn là khí Fermi tự do trong hộp. Mô hình này giải thích đúng nhiệt dung tuyến tính, định luật Wiedemann - Franz $\kappa/(\sigma T)=L_0$ với $L_0$ phổ quát, và bậc độ lớn của độ dẫn.

Nhưng nó **không** trả lời được câu hỏi cơ bản nhất: vì sao có chất dẫn điện và có chất cách điện, dù cả hai đều có rất nhiều electron? Và vì sao hệ số Hall của một số kim loại lại dương, như thể hạt tải mang điện tích dương?

## Thế tuần hoàn mở vùng cấm

Bật một thế tuần hoàn yếu $V(x)=2V_G\cos(Gx)$. Ở hầu hết $k$, nhiễu loạn bậc hai chỉ dịch mức chút ít. Nhưng tại $k=\pm G/2$ (biên vùng Brillouin), hai trạng thái $|k\rangle$ và $|k-G\rangle$ **suy biến**: phải chéo hóa ma trận $2\times2$, cho hai mức tách nhau $2|V_G|$.

Ý nghĩa vật lí: tại biên vùng, sóng tới và sóng phản xạ Bragg chồng chất thành sóng dừng. Một sóng dừng tập trung mật độ electron ở vị trí ion (năng lượng thấp), sóng kia tập trung ở giữa (năng lượng cao) — chênh lệch đó chính là vùng cấm.

## Phân loại vật rắn

Mỗi dải chứa $2N$ trạng thái ($N$ ô cơ sở, spin 2). Do đó:

- dải cao nhất **lấp một phần** $\to$ kim loại: có trạng thái trống ngay sát mức Fermi nên điện trường nhỏ cũng gây dòng;
- dải lấp đầy, vùng cấm rộng ($>3$ eV) $\to$ điện môi;
- dải lấp đầy, vùng cấm hẹp ($\sim1$ eV) $\to$ bán dẫn: kích thích nhiệt hoặc quang tạo hạt tải.

Đây là một trong những thành công đẹp nhất của cơ học lượng tử: một tính chất trải hơn 20 bậc độ lớn của điện trở được giải thích chỉ bằng cách đếm trạng thái.

## Khối lượng hiệu dụng và lỗ trống

Phương trình chuyển động bán cổ điển: $\vec v=\dfrac{1}{\hbar}\nabla_kE$ và $\hbar\dfrac{d\vec k}{dt}=-e(\vec E+\vec v\times\vec B)$. Gần đỉnh dải, $d^2E/dk^2<0$ nên $m^*<0$; thay vì nói "electron khối lượng âm", tiện hơn là mô tả bằng **lỗ trống** mang điện dương với khối lượng dương. Đó là lời giải cho hệ số Hall dương.

**Lỗi thường gặp:**
- Cho rằng số electron hóa trị chẵn thì chất luôn là điện môi. Quy tắc này chỉ đúng khi các dải không chồng lấn; magiê, canxi và nhiều kim loại kiềm thổ là phản ví dụ.
- Hiểu khối lượng hiệu dụng là khối lượng thật của electron bị thay đổi. Nó chỉ là cách gói tác dụng của thế mạng vào một tham số; $m^*$ có thể nhỏ hơn $m_e$ hàng chục lần, âm, hoặc là một tenxơ với tinh thể dị hướng.
- Nghĩ rằng vùng cấm xuất hiện ở mọi giá trị $k$. Nó mở ra tại biên vùng Brillouin, nơi điều kiện Bragg được thoả và hai trạng thái phẳng suy biến; ở các $k$ khác thế tuần hoàn chỉ gây dịch mức nhỏ.

<sub>`lesson.physics.chat-ran-hat-nhan.khi-electron-tu-do-va-li-thuyet-dai`</sub>

---

### 5. Bán dẫn và chuyển tiếp p-n
*Semiconductors and the p-n junction* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Tính được nồng độ hạt tải trong bán dẫn thuần và bán dẫn pha tạp
- Giải thích được sự hình thành vùng nghèo và hiệu điện thế tiếp xúc
- Vận dụng được phương trình Shockley để phân tích đặc tuyến điốt

## Hạt tải trong bán dẫn

Kích thích nhiệt đưa electron qua vùng cấm, để lại lỗ trống. Với $E_g\gg k_BT$, tích phân phân bố Fermi cho

$$np=n_i^2=N_cN_v\,e^{-E_g/k_BT}$$

Phụ thuộc hàm mũ vào $E_g/k_BT$ là điều quan trọng nhất: silic ($E_g=1{,}12$ eV) có $n_i\approx10^{10}$ cm⁻³ ở $300$ K, nhỏ hơn mật độ nguyên tử $13$ bậc — nhưng tăng nhiệt độ $10^\circ$C đã làm $n_i$ tăng gấp đôi.

## Pha tạp: điều khiển được hạt tải

Thay một nguyên tử Si bằng P (5 electron hóa trị) tạo mức donor ngay dưới đáy dải dẫn, ion hóa gần hết ở nhiệt độ phòng: $n\approx N_D$. Thay bằng B (3 electron) tạo mức acceptor, cho $p\approx N_A$. Với $N_D=10^{16}$ cm⁻³, mật độ hạt tải tăng $10^6$ lần so với thuần — và định luật tác dụng khối lượng buộc $p=n_i^2/n$ giảm đúng bằng ấy lần.

## Chuyển tiếp p-n

Ghép hai miền lại, chênh lệch nồng độ làm electron khuếch tán sang p và lỗ trống sang n. Chúng để lại các ion tạp chất **cố định**, tạo điện trường nội tại chống lại khuếch tán tiếp. Cân bằng đạt khi mức Fermi bằng nhau hai phía, với hiệu điện thế tiếp xúc

$$V_{bi}=\frac{k_BT}{e}\ln\frac{N_AN_D}{n_i^2}$$

Phân cực thuận hạ rào thế, dòng khuếch tán tăng theo hàm mũ; phân cực ngược nâng rào, chỉ còn dòng bão hòa nhỏ do hạt tải thiểu số. Kết quả là

$$I=I_S\left(e^{eV/k_BT}-1\right)$$

## Vì sao chuyển tiếp p-n quan trọng đến vậy

Tính bất đối xứng này là nền tảng của điốt chỉnh lưu, của transistor (hai chuyển tiếp ghép), của pin mặt trời (điện trường vùng nghèo tách cặp electron - lỗ trống do photon tạo ra) và của LED (tái hợp phát photon với $h\nu\approx E_g$, nên màu do vùng cấm quyết định).

**Lưu ý về giới hạn**: phương trình Shockley bỏ qua tái hợp trong vùng nghèo, hiệu ứng điện trở nối tiếp và đánh thủng; đặc tuyến thực lệch khỏi nó ở cả dòng rất nhỏ lẫn dòng lớn.

**Lỗi thường gặp:**
- Cho rằng pha tạp làm bán dẫn tích điện. Nguyên tử tạp chất trung hòa; khi ion hóa nó để lại ion cố định cân bằng đúng với hạt tải sinh ra, nên vật liệu vẫn trung hòa về điện.
- Dùng $n=N_D$ ở mọi nhiệt độ. Ở nhiệt độ rất thấp donor chưa ion hóa hết (đóng băng hạt tải), còn ở nhiệt độ cao $n_i$ vượt $N_D$ và bán dẫn trở lại chế độ thuần — đó là giới hạn nhiệt độ làm việc của linh kiện.
- Hiểu điốt là "vật dẫn một chiều lí tưởng". Dòng ngược không bằng 0 mà bằng $I_S$, và $I_S$ tăng nhanh theo nhiệt độ; ở điện áp ngược đủ lớn còn xảy ra đánh thủng Zener hoặc thác lũ.

<sub>`lesson.physics.chat-ran-hat-nhan.ban-dan-va-chuyen-tiep-pn`</sub>

---

### 6. Siêu dẫn: hiện tượng luận và lí thuyết BCS
*Superconductivity: phenomenology and BCS theory* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được siêu dẫn với vật dẫn lí tưởng qua hiệu ứng Meissner
- Giải thích được cơ chế ghép cặp Cooper qua tương tác electron - phonon
- Vận dụng được các hệ thức BCS về khe năng lượng và nhiệt độ tới hạn

## Hai hiện tượng, không phải một

Điện trở bằng 0 (Onnes 1911) đã kì lạ, nhưng điều quyết định là **hiệu ứng Meissner** (1933): vật siêu dẫn đẩy từ trường ra khỏi lòng nó ngay cả khi trường được đặt **trước** lúc làm lạnh. Một vật dẫn lí tưởng chỉ giữ nguyên từ thông đang có; siêu dẫn thì chủ động trục xuất nó. Vậy siêu dẫn là một **pha nhiệt động** riêng, không phải giới hạn của tính dẫn tốt.

Phương trình London mô tả điều này: từ trường tắt trong lòng theo $e^{-x/\lambda_L}$ với độ thấm sâu $\lambda_L=\sqrt{m/(\mu_0 n_se^2)}$ cỡ vài chục nm.

## Vì sao electron lại hút nhau

Electron thứ nhất chuyển động kéo các ion dương lại gần; ion nặng nên "nhớ" biến dạng đó lâu hơn thời gian electron đi qua. Vùng dư điện tích dương còn lại hút electron thứ hai. Kết quả là một **tương tác hút hiệu dụng** qua phonon, thắng được đẩy Coulomb đã bị màn chắn.

Cooper chứng minh: dù tương tác hút yếu tới đâu, khí Fermi cũng bất ổn định — luôn tồn tại trạng thái liên kết của cặp $(\vec k\uparrow,-\vec k\downarrow)$.

## Kết quả BCS

Toàn hệ ngưng tụ thành trạng thái cặp kết hợp, với khe năng lượng

$$\Delta(0)=1{,}764\,k_BT_c,\qquad k_BT_c=1{,}13\,\hbar\omega_D\,e^{-1/(N(0)V)}$$

Tỉ số $2\Delta/k_BT_c=3{,}53$ là **phổ quát** cho siêu dẫn ghép yếu, không phụ thuộc vật liệu — một tiên đoán mạnh và đã được xác nhận. Khe năng lượng giải thích điện trở bằng 0: không có trạng thái kích thích nào ở năng lượng thấp hơn $\Delta$, nên tán xạ yếu không phá được dòng.

Hệ quả kiểm chứng khác: hiệu ứng đồng vị $T_c\propto M^{-1/2}$, xác nhận vai trò của phonon.

## Lượng tử hóa từ thông và SQUID

Hàm sóng vĩ mô đơn trị buộc từ thông qua vòng siêu dẫn phải là bội của $\Phi_0=\dfrac{h}{2e}=2{,}07\cdot10^{-15}$ Wb. Chữ $2e$ là bằng chứng trực tiếp rằng hạt tải là **cặp**. Ứng dụng: SQUID đo được từ trường cỡ $10^{-15}$ T.

## Ngoài BCS

Siêu dẫn nhiệt độ cao (cuprate, $T_c$ tới $135$ K) không giải thích được bằng BCS phonon chuẩn; cơ chế ghép cặp vẫn là bài toán mở sau gần bốn thập kỉ.

**Lỗi thường gặp:**
- Coi siêu dẫn là vật dẫn lí tưởng có $\rho=0$. Vật dẫn lí tưởng chỉ bảo toàn từ thông sẵn có; hiệu ứng Meissner trục xuất từ trường ngay cả khi trường đã tồn tại trước, chứng tỏ đây là một pha nhiệt động riêng.
- Nghĩ rằng cặp Cooper là hai electron gần nhau về không gian. Kích thước cặp (độ dài kết hợp) cỡ hàng trăm nm, lớn hơn khoảng cách giữa các electron hàng nghìn lần; các cặp chồng chéo lên nhau mạnh mẽ.
- Dùng lượng tử từ thông $h/e$. Giá trị đúng là $h/2e$; sai số hệ số hai này không phải chi tiết kĩ thuật mà là bằng chứng thực nghiệm trực tiếp cho việc hạt tải mang điện tích $2e$.

<sub>`lesson.physics.chat-ran-hat-nhan.sieu-dan`</sub>

---

### 7. Cấu trúc hạt nhân và các mô hình
*Nuclear structure and nuclear models* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Phân tích được đường cong năng lượng liên kết riêng và ý nghĩa của nó
- Giải thích được từng số hạng trong công thức bán thực nghiệm Weizsäcker
- So sánh được mẫu giọt chất lỏng với mẫu lớp và ý nghĩa của các số magic

## Kích thước và mật độ

Thực nghiệm tán xạ electron cho $R\approx R_0A^{1/3}$ với $R_0=1{,}2$ fm. Vì $V\propto A$, mật độ nuclôn **không đổi** với mọi hạt nhân — đúng như một chất lỏng không nén được. Đây là gợi ý đầu tiên cho mẫu giọt.

## Đường cong năng lượng liên kết riêng

$B/A$ tăng nhanh với $A$ nhỏ, đạt cực đại $\approx8{,}8$ MeV quanh $^{56}$Fe, rồi giảm chậm. Toàn bộ năng lượng hạt nhân đến từ hình dạng này: **hợp hạch** các hạt nhân nhẹ và **phân hạch** các hạt nhân nặng đều đi về phía cực đại, đều tỏa năng lượng.

## Công thức Weizsäcker

$$B=a_VA-a_SA^{2/3}-a_C\frac{Z(Z-1)}{A^{1/3}}-a_A\frac{(A-2Z)^2}{A}+\delta$$

Đọc từng số hạng như đọc vật lí:

- $a_VA$: mỗi nuclôn liên kết với số lân cận cố định — lực hạt nhân **bão hòa** và tầm ngắn;
- $-a_SA^{2/3}$: nuclôn ở bề mặt thiếu lân cận, giống sức căng mặt ngoài; quan trọng nhất với hạt nhân nhẹ;
- $-a_C$: đẩy Coulomb giữa các proton, tầm xa nên tăng như $Z^2$; chi phối ở hạt nhân nặng;
- $-a_A$: số hạng bất đối xứng, hệ quả của nguyên lí Pauli — thừa neutron buộc chúng chiếm mức cao hơn;
- $\delta$: số hạng ghép cặp, ưu ái số proton và neutron chẵn.

Công thức này tiên đoán tốt khối lượng, giải thích vì sao dải bền cong về phía $N>Z$, và cho ngưỡng phân hạch tự phát khi $Z^2/A\gtrsim48$.

## Nơi mẫu giọt hỏng

Nó không giải thích được các đỉnh bền bất thường tại **số magic**. Mẫu lớp sửa điều này: nuclôn chuyển động trong thế trung bình do các nuclôn khác tạo ra, lấp đầy các lớp như electron trong nguyên tử. Chỉ khi thêm tương tác **spin - quỹ đạo mạnh** (Goeppert-Mayer và Jensen, Nobel 1963) thì thứ tự mức mới cho đúng dãy 2, 8, 20, 28, 50, 82, 126.

Hạt nhân "kép magic" như $^{4}$He, $^{16}$O, $^{208}$Pb bền vượt trội. Hai mẫu bổ sung nhau: giọt cho tính chất trung bình, lớp cho spin, chẵn lẻ và cấu trúc mức kích thích.

**Lỗi thường gặp:**
- Cho rằng hạt nhân càng nặng thì năng lượng liên kết riêng càng lớn. $B/A$ đạt cực đại ở sắt rồi **giảm** vì đẩy Coulomb tăng như $Z^2$; chính điều này cho phép phân hạch tỏa năng lượng.
- Dùng $Z^2$ thay vì $Z(Z-1)$ trong số hạng Coulomb. Proton không tự đẩy chính nó; với hạt nhân nhẹ sự khác biệt này đáng kể, ví dụ với $Z=2$ thì sai số là gấp đôi.
- Nghĩ rằng số magic là hệ quả của mẫu giọt. Mẫu giọt cho đường cong trơn không có đỉnh; số magic chỉ giải thích được bằng cấu trúc lớp cộng với tương tác spin - quỹ đạo mạnh.

<sub>`lesson.physics.chat-ran-hat-nhan.cau-truc-hat-nhan-va-cac-mau`</sub>

---

### 8. Phân rã phóng xạ và tiết diện phản ứng
*Radioactive decay and reaction cross-sections* · Đại học · intl-undergrad · 55 phút · nang-cao

**Mục tiêu:**
- Vận dụng được định luật phân rã phóng xạ và khái niệm chu kì bán rã
- Phân biệt được cơ chế của phân rã alpha, beta và gamma cùng các định luật bảo toàn
- Tính được tốc độ phản ứng từ tiết diện và thông lượng hạt tới

## Định luật phân rã

Phân rã là quá trình ngẫu nhiên không nhớ: mỗi hạt nhân có xác suất $\lambda\,dt$ phân rã trong $dt$, độc lập với việc nó đã tồn tại bao lâu. Từ đó

$$N(t)=N_0e^{-\lambda t},\qquad T_{1/2}=\frac{\ln2}{\lambda},\qquad A=\lambda N$$

Chú ý phân biệt số hạt nhân $N$ với **hoạt độ** $A$ (Bq = phân rã/s). Với chuỗi phóng xạ, khi hạt nhân mẹ có $T_1\gg T_2$ thì sau đủ lâu đạt **cân bằng thế kỉ**: $\lambda_1N_1=\lambda_2N_2$, tức mọi thành viên trong chuỗi có cùng hoạt độ.

## Ba loại phân rã

**Alpha**: hạt nhân nặng phát $^4$He. Cơ chế là đường ngầm qua rào Coulomb, nên chu kì bán rã phụ thuộc cực nhạy vào năng lượng $Q$ — quy luật Geiger - Nuttall trải hơn 20 bậc độ lớn từ cùng một công thức WKB.

**Beta**: $n\to p+e^-+\bar\nu_e$ (hoặc $\beta^+$, hoặc bắt electron), do tương tác yếu. Phổ năng lượng electron **liên tục** — chính điều này buộc Pauli tiên đoán neutrino để cứu bảo toàn năng lượng và mômen động lượng.

**Gamma**: hạt nhân chuyển từ trạng thái kích thích về mức thấp hơn, $Z$ và $A$ không đổi. Đi kèm quy tắc lọc lựa theo spin và chẵn lẻ, giống hệt quang phổ nguyên tử nhưng ở thang MeV.

Mọi phân rã đều tuân thủ bảo toàn năng lượng - động lượng, điện tích, số nuclôn, số lepton và mômen động lượng.

## Tiết diện

Tốc độ phản ứng $R=\sigma\,\Phi\,N_{\text{bia}}$, với $\sigma$ đo bằng barn ($10^{-28}$ m²) — cỡ tiết diện hình học của hạt nhân, nhưng có thể lớn hơn hàng nghìn lần tại **cộng hưởng** (dạng Breit - Wigner) hoặc nhỏ hơn nhiều nếu bị rào Coulomb chặn.

Chùm tia đi qua vật liệu suy giảm theo $I=I_0e^{-n\sigma x}$; với photon thường viết $I=I_0e^{-\mu x}$ và lớp hấp thụ nửa $d_{1/2}=\ln2/\mu$.

## An toàn bức xạ

Liều hấp thụ đo bằng gray (J/kg); liều tương đương (sievert) nhân thêm hệ số trọng số bức xạ, vì hạt alpha gây tổn thương sinh học lớn hơn nhiều so với gamma cùng năng lượng do mật độ ion hóa dọc đường đi cao hơn.

**Lỗi thường gặp:**
- Cho rằng hạt nhân "già" dễ phân rã hơn. Phân rã không có trí nhớ: xác suất phân rã trong giây tới là như nhau với mọi hạt nhân cùng loại, bất kể chúng đã tồn tại bao lâu.
- Nhầm số hạt nhân với hoạt độ. Hai mẫu có cùng số hạt nhân nhưng khác đồng vị sẽ có hoạt độ khác nhau rất xa, vì $A=\lambda N$ và $\lambda$ trải qua nhiều bậc độ lớn.
- Coi tiết diện là tiết diện hình học của hạt nhân. Tại cộng hưởng, tiết diện bắt neutron có thể vượt tiết diện hình học hàng nghìn lần; ngược lại phản ứng bị rào Coulomb chặn có tiết diện nhỏ hơn nhiều bậc.

<sub>`lesson.physics.chat-ran-hat-nhan.phan-ra-phong-xa-va-tiet-dien`</sub>

---

### 9. Hạt cơ bản, Mô hình chuẩn và các định luật bảo toàn
*Elementary particles, the Standard Model and conservation laws* · Đại học · intl-undergrad · 60 phút · chuyen-sau

**Mục tiêu:**
- Phân loại được các hạt cơ bản theo thế hệ và theo tương tác mà chúng tham gia
- Vận dụng được các định luật bảo toàn để xét một phản ứng có xảy ra được hay không
- Tính được khối lượng bất biến và năng lượng khối tâm trong va chạm hạt

## Bảng kiểm kê

Vật chất gồm 12 fermion spin $1/2$ xếp thành ba thế hệ:

| | Quark | Lepton |
|---|---|---|
| Thế hệ 1 | u, d | e, $\nu_e$ |
| Thế hệ 2 | c, s | $\mu$, $\nu_\mu$ |
| Thế hệ 3 | t, b | $\tau$, $\nu_\tau$ |

Vật chất thường chỉ dùng thế hệ đầu: proton = uud, neutron = udd. Các thế hệ nặng hơn phân rã nhanh về thế hệ nhẹ.

Tương tác truyền bởi các boson chuẩn spin 1, cộng boson Higgs spin 0 sinh khối lượng (phát hiện tại LHC năm 2012).

## Ba tương tác, ba tính chất

**Mạnh**: gluon mang tích màu nên tự tương tác, làm lực **không giảm** theo khoảng cách. Hệ quả là **cầm tù màu**: không quan sát được quark tự do; tách chúng ra chỉ tạo thêm cặp quark - phản quark. Ở khoảng cách rất nhỏ thì ngược lại — tự do tiệm cận.

**Yếu**: duy nhất đổi được hương quark (qua ma trận CKM) và vi phạm chẵn lẻ. Boson W, Z rất nặng ($80$ và $91$ GeV) nên tương tác có tầm cực ngắn và tốc độ chậm.

**Điện từ**: photon không khối lượng, tầm vô hạn.

## Định luật bảo toàn — công cụ làm việc

Luôn bảo toàn: năng lượng - động lượng, điện tích, số baryon, ba số lepton theo từng thế hệ (sai khác bởi dao động neutrino), mômen động lượng. Bảo toàn **chỉ** với tương tác mạnh và điện từ: số lạ, chẵn lẻ P, liên hợp điện tích C.

Quy trình xét một phản ứng: kiểm tra lần lượt điện tích, số baryon, số lepton, rồi năng lượng ngưỡng. Nếu bảo toàn "yếu" bị vi phạm thì phản ứng vẫn xảy ra nhưng chỉ qua tương tác yếu, tức chậm hơn nhiều bậc.

## Động học tương đối tính

$$s=\left(\sum E\right)^2-\left(\sum \vec pc\right)^2$$

là bất biến. Với máy va chạm đối đầu năng lượng $E$ mỗi chùm, $\sqrt s=2E$; với bia cố định, $\sqrt s\approx\sqrt{2E m_{\text{bia}}c^2}$ — chỉ tăng như căn bậc hai. Chính bất lợi này là lí do mọi máy gia tốc năng lượng cao hiện đại đều là máy va chạm.

## Điều Mô hình chuẩn chưa trả lời

Không chứa hấp dẫn, không giải thích vật chất tối và năng lượng tối, không nói vì sao có đúng ba thế hệ, và cơ chế sinh khối lượng neutrino vẫn còn để ngỏ.

**Lỗi thường gặp:**
- Cho rằng quark có thể tách rời và quan sát riêng lẻ. Sự cầm tù màu làm năng lượng tăng tuyến tính theo khoảng cách; tách quark ra chỉ tạo thêm cặp quark - phản quark, cho các hadron mới.
- Áp dụng bảo toàn số lạ hoặc bảo toàn chẵn lẻ cho phân rã yếu. Tương tác yếu vi phạm cả hai; đó chính là dấu hiệu để nhận ra một quá trình xảy ra qua tương tác yếu và do đó rất chậm.
- Cộng năng lượng của hai chùm bia cố định như với máy va chạm đối đầu. Với bia cố định $\sqrt s$ chỉ tăng như $\sqrt{E}$; muốn tăng gấp đôi năng lượng khối tâm phải tăng năng lượng chùm gấp bốn.

<sub>`lesson.physics.chat-ran-hat-nhan.hat-co-ban-va-mo-hinh-chuan`</sub>

---

## Unit 6: IPhO - Phương pháp giải và vòng thực hành

### 6. Phương pháp nhiễu loạn và bất biến đoạn nhiệt
*Perturbation methods and adiabatic invariants* · Đại học · olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Vận dụng được sơ đồ nhiễu loạn: nghiệm bậc 0 rồi hiệu chỉnh bậc nhất
- Xác định được bất biến đoạn nhiệt của một hệ dao động khi tham số biến đổi chậm
- Phân tích được điều kiện chậm để bất biến đoạn nhiệt còn đúng

## Nhiễu loạn: dùng nghiệm biết để tìm nghiệm chưa biết

Sơ đồ chung:

1. Viết bài toán dưới dạng "bài đã giải được + $\varepsilon\times$ phần nhỏ".
2. Lấy nghiệm bậc 0 (bỏ qua nhiễu loạn).
3. **Thay nghiệm bậc 0 vào phần nhiễu loạn** để tính hiệu chỉnh bậc nhất.
4. Nếu cần, lặp lại.

Điểm quan trọng nhất là bước 3: ta tính công của lực nhiễu loạn, hoặc tích phân của nhiễu loạn, **trên quỹ đạo chưa nhiễu**. Sai số của cách làm này là bậc $\varepsilon^2$.

## Ví dụ mẫu: tiến động quỹ đạo

Thế năng $U=-\frac{\alpha}{r}+\frac{\beta}{r^2}$ với $\beta$ nhỏ. Bài bậc 0 là Kepler (elip đóng). Số hạng $\beta/r^2$ cộng vào rào li tâm, làm đổi tần số bán kính một lượng nhỏ trong khi tần số quay giữ nguyên, gây **tiến động** với tốc độ tỉ lệ $\beta$. Đây là mẫu chung: nhiễu loạn phá vỡ sự cộng hưởng giữa hai tần số.

## Bất biến đoạn nhiệt

Nếu tham số của một hệ dao động (chiều dài con lắc, độ cứng lò xo, từ trường) thay đổi **chậm** — nghĩa là thay đổi ít trong một chu kì — thì

$$I=\oint p\,dq \approx \text{const},\qquad\text{với dao động điều hoà } I=\frac{2\pi E}{\omega}.$$

Do đó $\dfrac{E}{\omega}$ bảo toàn: rút ngắn dây con lắc làm $\omega$ tăng nên $E$ tăng theo cùng tỉ lệ. Với hạt tích điện trong từ trường biến đổi chậm, bất biến là mômen từ $\mu=\frac{mv_\perp^2}{2B}$ — nền tảng của bẫy từ.

## Điều kiện chậm phải kiểm tra

$$\left|\frac{1}{\omega}\frac{d\omega}{dt}\right|\ll\omega,\qquad\text{tức}\qquad \frac{\Delta\omega}{\omega}\ll1 \text{ trong một chu kì}.$$

Nếu tham số đổi nhanh (đột ngột), dùng **xấp xỉ đột biến**: toạ độ và vận tốc không kịp đổi, năng lượng nhảy bậc. Hai giới hạn chậm và nhanh cho kết quả khác hẳn nhau, nên phải nói rõ đang ở chế độ nào.

**Lỗi thường gặp:**
- Dùng bảo toàn năng lượng khi kéo dây con lắc — sai vì lực căng có thành phần dọc theo chuyển động của điểm treo, sinh công; đúng đại lượng bảo toàn là $E/\omega$.
- Áp bất biến đoạn nhiệt cho quá trình thay đổi nhanh — sai vì điều kiện của bất biến là tham số đổi ít trong một chu kì; với thay đổi đột ngột phải dùng xấp xỉ đột biến, cho kết quả hoàn toàn khác.
- Tính hiệu chỉnh nhiễu loạn trên quỹ đạo ĐÃ nhiễu — sai về mặt nhất quán bậc: dùng nghiệm bậc nhất để tính hiệu chỉnh bậc nhất là trộn lẫn các bậc, kết quả không chính xác hơn mà chỉ rối hơn.

<sub>`lesson.physics.ipho.nhieu-loan-va-bat-bien-doan-nhiet`</sub>

---

## Unit 6: Optics and Optical Instruments

### 1. Quang hình học: Ma trận truyền tia ABCD, Khúc xạ qua mặt cầu và Quang hệ
*Geometrical optics: ABCD ray matrices, spherical refraction, and optical systems* · Đại học · intl-undergrad, vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Áp dụng định luật khúc xạ qua lưỡng diện cầu và công thức thợ làm kính
- Thiết lập ma trận truyền tia ABCD cho sự truyền trong môi trường và khúc xạ qua thấu kính
- Tính độ bội giác của kính hiển vi và kính thiên văn khúc xạ

## Khúc xạ qua mặt cầu và Công thức thợ làm kính

Xét chùm tia cận trục đi từ môi trường chiết suất $n_1$ vào môi trường chiết suất $n_2$ qua mặt cầu bán kính cong $R$:

$$\frac{n_1}{d} + \frac{n_2}{d'} = \frac{n_2 - n_1}{R}$$

Với thấu kính mỏng trong không khí ($n_{mt} = 1$), công thức tạo ảnh liên hệ tiêu cự $f$ qua bán kính cong hai mặt:

$$\frac{1}{f} = (n - 1) \left( \frac{1}{R_1} - \frac{1}{R_2} \right)$$

## Dụng cụ quang học: Kính hiển vi và Kính thiên văn

Độ bội giác của kính hiển vi khi ngắm chừng ở vô cực: $G_{\infty} = \frac{\delta \cdot Đ}{f_1 f_2}$, với $\delta$ là độ dài quang học và $Đ = 25\text{ cm}$. Đối với kính thiên văn: $G_{\infty} = \frac{f_1}{f_2}$.

**Lỗi thường gặp:**
- Quy ước sai dấu bán kính cong R: mặt lồi R > 0, mặt lõm R < 0 theo chiều truyền tia sáng
- Nhầm lẫn công thức độ bội giác giữa kính hiển vi (tỉ lệ nghịch với f1*f2) và kính thiên văn (f1/f2)

<sub>`lesson.physics.undergrad-physics.quang-hinh-ma-tran-abcd-va-quang-sai`</sub>

---
