# Hoá học — Bài học AISTEM

Tổng số: **185** bài. Sinh tự động bằng `tools/build_content_index.py`.

## Chủ đề: Dung dịch

### 1. Nồng độ phần trăm của dung dịch
*Percentage concentration of a solution* · THCS · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Tính được nồng độ phần trăm $C\%$ khi biết khối lượng chất tan và khối lượng dung dịch
- Tính được khối lượng chất tan hoặc dung dịch từ nồng độ phần trăm

## Nồng độ phần trăm cho biết điều gì

Khi pha nước muối, ta muốn biết muối "đậm" hay "loãng". **Nồng độ phần trăm** $C\%$ trả lời câu đó: nó là số gam chất tan trong **100 gam dung dịch**.

$$C\% = \frac{m_{ct}}{m_{dd}}\times100\%$$

trong đó khối lượng dung dịch bằng khối lượng chất tan cộng khối lượng dung môi (thường là nước):

$$m_{dd} = m_{ct} + m_{dm}$$

## Cẩn thận với mẫu số

Lỗi hay gặp là chia cho khối lượng **nước** thay vì khối lượng **dung dịch**. Nước là dung môi, còn dung dịch là cả hỗn hợp — luôn nhớ cộng thêm chất tan vào mẫu.

## Tính ngược

Biết $C\%$ và khối lượng dung dịch, tính được chất tan:

$$m_{ct} = \frac{C\%\times m_{dd}}{100}$$

Đây là công cụ để pha một dung dịch có nồng độ mong muốn trong phòng thí nghiệm và trong đời sống (pha nước muối sinh lí, pha thuốc...).

**Lỗi thường gặp:**
- Chia khối lượng chất tan cho khối lượng nước (dung môi) thay vì cho khối lượng dung dịch.
- Quên cộng khối lượng chất tan vào khối lượng dung dịch.
- Nhầm nồng độ phần trăm (theo khối lượng) với nồng độ mol (theo thể tích).

<sub>`lesson.chemistry.thcs-hoa-sinh.nong-do-phan-tram`</sub>

---

### 2. Nồng độ mol của dung dịch
*Molar concentration of a solution* · THCS · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Tính được nồng độ mol $C_M$ khi biết số mol chất tan và thể tích dung dịch
- Tính được số mol chất tan hoặc thể tích dung dịch từ nồng độ mol

## Vì sao có thêm nồng độ mol

Nồng độ phần trăm dùng khối lượng, nhưng phản ứng lại theo số mol. Vì thế trong phòng thí nghiệm người ta hay dùng **nồng độ mol** $C_M$: số mol chất tan trong **1 lít dung dịch**.

$$C_M = \frac{n}{V}$$

với $n$ tính bằng mol, $V$ tính bằng **lít**. Đơn vị của $C_M$ là mol/L, viết tắt M.

## Đừng quên đổi đơn vị

Đề thường cho thể tích bằng mililit. Phải đổi: $500$ mL $= 0{,}5$ lít. Đây là lỗi số 1 khi tính nồng độ mol.

## Ba chiều tính

Từ công thức gốc suy ra hai công thức con:

$$n = C_M\times V \qquad V = \frac{n}{C_M}$$

Biết hai đại lượng bất kì là tìm được đại lượng còn lại. Nếu đề cho khối lượng chất tan, nhớ đổi ra số mol $n=\dfrac{m}{M}$ trước.

**Lỗi thường gặp:**
- Quên đổi mililit ra lít nên nồng độ sai gấp 1000 lần.
- Dùng thẳng khối lượng chất tan làm số mol mà không chia cho khối lượng mol.
- Nhầm nồng độ mol (theo thể tích dung dịch) với nồng độ phần trăm (theo khối lượng dung dịch).

<sub>`lesson.chemistry.thcs-hoa-sinh.nong-do-mol`</sub>

---

### 3. Độ tan và dung dịch bão hoà
*Solubility and saturated solutions* · THCS · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Nêu được ý nghĩa của độ tan và tính được khối lượng chất tan tối đa trong một lượng nước
- Tính được nồng độ phần trăm của dung dịch bão hoà khi biết độ tan

## Nước hoà tan có giới hạn

Cho đường vào cốc nước, khuấy mãi đến lúc đường không tan thêm nữa — dung dịch đã **bão hoà**. Lượng chất tan tối đa ấy phụ thuộc nhiệt độ và được đo bằng **độ tan** $S$: số gam chất tan trong 100 gam nước.

$$S = \frac{m_{ct}}{m_{H_2O}}\times100$$

Độ tan càng lớn, chất càng dễ tan. Đa số chất rắn tan nhiều hơn khi nước nóng lên.

## Từ độ tan sang nồng độ phần trăm

Dung dịch bão hoà có $S$ gam chất tan trong 100 gam nước, tức trong $(100+S)$ gam dung dịch:

$$C\% = \frac{S}{100+S}\times100\%$$

## Vì sao tinh thể tách ra khi nguội

Khi hạ nhiệt độ, độ tan giảm, dung dịch "chứa" không hết chất tan nên phần dư **kết tinh** tách ra. Đây chính là cách làm ra đường phèn, muối kết tinh — một thí nghiệm quan sát rất trực quan.

**Lỗi thường gặp:**
- Nhầm độ tan tính trên 100 g dung dịch thay vì 100 g nước.
- Khi tính $C\%$ dung dịch bão hoà, lấy mẫu số là 100 (chỉ nước) thay vì $100+S$ (cả dung dịch).
- Cho rằng độ tan không đổi theo nhiệt độ nên không giải thích được vì sao tinh thể tách ra khi nguội.

<sub>`lesson.chemistry.thcs-hoa-sinh.do-tan-va-dung-dich-bao-hoa`</sub>

---

## Chủ đề: Liên kết hoá học và kim loại

### 1. Liên kết hoá học cơ bản và quy tắc hoá trị
*Basic chemical bonding and the valence rule* · THCS · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Phân biệt được liên kết ion và liên kết cộng hoá trị qua cách góp hoặc cho - nhận electron
- Vận dụng được quy tắc hoá trị để lập và kiểm tra công thức hoá học hai nguyên tố

## Vì sao nguyên tử "kết bạn"

Nguyên tử bền khi lớp electron ngoài cùng đủ 8 (hoặc 2 với heli). Để đạt điều đó, chúng liên kết theo hai kiểu chính:

- **Liên kết ion**: kim loại **cho** electron, phi kim **nhận** electron. Hai ion trái dấu hút nhau, như trong $NaCl$.
- **Liên kết cộng hoá trị**: hai phi kim **dùng chung** cặp electron, như trong $H_2$, $H_2O$.

## Quy tắc hoá trị

Trong hợp chất hai nguyên tố $A_xB_y$ với hoá trị $a$ của $A$ và $b$ của $B$:

$$x\times a = y\times b$$

"Tích chỉ số nhân hoá trị của hai bên phải bằng nhau." Từ đó rút ra tỉ lệ $\dfrac{x}{y} = \dfrac{b}{a}$ (rút gọn).

## Dùng để làm gì

- **Lập công thức**: biết hoá trị, tìm chỉ số $x, y$.
- **Kiểm tra công thức**: thay vào quy tắc, nếu hai vế bằng nhau là công thức đúng.
- **Tìm hoá trị** của một nguyên tố khi biết công thức và hoá trị nguyên tố kia.

**Lỗi thường gặp:**
- Nhầm chỉ số với hoá trị: chỉ số là con số nhỏ dưới kí hiệu, hoá trị là khả năng liên kết.
- Không rút gọn tỉ lệ nên viết $Al_2O_3$ thành dạng chưa tối giản như $Al_4O_6$.
- Cho rằng liên kết ion và cộng hoá trị giống nhau; thực ra một bên cho - nhận, một bên dùng chung electron.

<sub>`lesson.chemistry.thcs-hoa-sinh.lien-ket-hoa-hoc-va-quy-tac-hoa-tri`</sub>

---

### 2. Dãy hoạt động hoá học của kim loại và điện hoá sơ khởi
*Reactivity series of metals and basic electrochemistry* · THCS · vn-gdpt-2018 · 40 phút · nang-cao

**Mục tiêu:**
- Sắp xếp được một số kim loại theo mức độ hoạt động và dự đoán phản ứng đẩy kim loại
- Giải thích được nguyên tắc hoạt động sơ khởi của pin đơn giản dựa vào chênh lệch hoạt động

## Kim loại có "mạnh yếu"

Không phải kim loại nào cũng phản ứng như nhau. Các nhà hoá học xếp chúng thành **dãy hoạt động hoá học**, mạnh dần từ phải sang trái:

$$K,\ Na,\ Ca,\ Mg,\ Al,\ Zn,\ Fe,\ Pb,\ (H),\ Cu,\ Ag,\ Au$$

Câu thần chú quen thuộc: "Khi Nào Cần May Áo Záp Sắt Phải Hỏi Cúc Bạc Vàng".

## Quy tắc dùng dãy

- Kim loại đứng **trước H** đẩy được hydrogen ra khỏi dung dịch axit (như $Zn$, $Fe$).
- Kim loại đứng **trước** đẩy được kim loại đứng **sau** ra khỏi dung dịch muối. Ví dụ $Fe$ đẩy $Cu$ khỏi $CuSO_4$: đinh sắt nhúng vào dung dịch xanh, dần phủ lớp đồng đỏ.

## Chớm tới điện hoá

Ghép hai kim loại khác nhau (ví dụ $Zn$ và $Cu$) vào dung dịch, kim loại mạnh hơn nhường electron, tạo dòng điện — đó là nguyên tắc của **pin**. Chênh lệch hoạt động giữa hai kim loại càng lớn thì pin cho hiệu điện thế càng cao. Đây là cửa ngõ vào điện hoá học.

**Lỗi thường gặp:**
- Cho rằng mọi kim loại đều đẩy được nhau; thực ra chỉ kim loại đứng trước đẩy kim loại đứng sau.
- Nghĩ vàng, bạc phản ứng với axit loãng như sắt, kẽm; thực ra chúng đứng sau H nên không đẩy được hydrogen.
- Nhầm rằng pin mạnh do kim loại to; thực ra hiệu điện thế phụ thuộc chênh lệch vị trí trong dãy hoạt động.

<sub>`lesson.chemistry.thcs-hoa-sinh.day-hoat-dong-hoa-hoc-va-dien-hoa`</sub>

---

## Chủ đề: Mol và tính toán hoá học

### 1. Mol, khối lượng mol và số hạt vi mô
*The mole, molar mass and number of particles* · THCS · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Tính được số mol của một chất khi biết khối lượng và ngược lại bằng công thức $n=\dfrac{m}{M}$
- Tính được số nguyên tử hoặc phân tử trong một lượng chất bằng số Avogadro
- Đổi qua lại giữa ba đại lượng: số mol, khối lượng và số hạt

## Vì sao cần "mol"

Một giọt nước đã chứa hàng tỉ tỉ phân tử — không thể đếm từng cái. Nhà hoá học dùng **mol** như người bán trứng dùng "tá": 1 tá là 12 quả, còn 1 mol là $6{,}022\times10^{23}$ hạt. Con số khổng lồ này gọi là **số Avogadro** $N_A$.

## Ba đại lượng, hai chiếc cầu

Khi cân một chất ta biết **khối lượng** $m$ (gam), nhưng phản ứng lại xảy ra theo **số hạt**. Mol nối hai thế giới đó lại:

$$n = \frac{m}{M} \qquad m = n\times M$$

trong đó $M$ là **khối lượng mol** (g/mol), lấy đúng bằng nguyên tử khối hay phân tử khối. Ví dụ nước $H_2O$ có $M = 2\times1 + 16 = 18$ g/mol.

Muốn biết có bao nhiêu hạt thì nhân số mol với $N_A$:

$$N = n\times N_A$$

## Sơ đồ dễ nhớ

$$m \;\xrightarrow{\;:M\;}\; n \;\xrightarrow{\;\times N_A\;}\; N$$

Đi ngược lại thì làm phép tính ngược. Nắm chắc sơ đồ này là giải được hầu hết bài tính toán hoá học lớp 8.

**Lỗi thường gặp:**
- Lấy khối lượng nhân $M$ thay vì chia — nhớ sơ đồ: từ $m$ sang $n$ là phép CHIA cho $M$.
- Lẫn lộn nguyên tử khối của nguyên tử với phân tử khối của phân tử: $O$ là 16 nhưng khí oxygen $O_2$ có $M=32$.
- Quên nhân với $N_A$ khi đề hỏi số hạt, chỉ dừng ở số mol.

<sub>`lesson.chemistry.thcs-hoa-sinh.mol-khoi-luong-so-hat`</sub>

---

### 2. Thể tích chất khí và tỉ khối của chất khí
*Gas volume and gas density ratio* · THCS · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Tính được thể tích chất khí ở đktc ($22{,}4$ L/mol) và ở điều kiện chuẩn đkc ($24{,}79$ L/mol)
- Tính được tỉ khối của một khí so với khí khác và so với không khí
- Dựa vào tỉ khối để dự đoán khí nặng hay nhẹ hơn không khí

## Vì sao mọi khí lại chiếm cùng thể tích

**Định luật Avogadro**: ở cùng nhiệt độ và áp suất, những thể tích khí bằng nhau chứa số phân tử bằng nhau. Hệ quả tuyệt vời: 1 mol của *bất kì* chất khí nào cũng chiếm cùng một thể tích, dù phân tử nặng nhẹ khác nhau.

## Hai mốc điều kiện

- **đktc** ($0^{\circ}$C, 1 atm): $V = 22{,}4\,n$
- **đkc** ($25^{\circ}$C, 1 bar, SGK mới): $V = 24{,}79\,n$

Muốn tìm số mol thì làm ngược: $n = \dfrac{V}{22{,}4}$ hoặc $n=\dfrac{V}{24{,}79}$. Nhớ đọc kĩ đề dùng mốc nào.

## Tỉ khối: khí nào nặng hơn

Muốn biết khí $A$ nặng gấp mấy lần khí $B$:

$$d_{A/B} = \frac{M_A}{M_B}$$

So với **không khí** (coi $M = 29$ g/mol):

$$d_{A/kk} = \frac{M_A}{29}$$

Nếu $d_{A/kk} > 1$ khí nặng hơn không khí (như $CO_2$), nên thu bằng cách để ngửa bình; nếu $< 1$ khí nhẹ hơn (như $H_2$), phải úp bình.

**Lỗi thường gặp:**
- Dùng nhầm mốc $22{,}4$ cho đkc hoặc $24{,}79$ cho đktc — phải đọc kĩ đề cho điều kiện nào.
- Lấy khối lượng mol so với 28 (nitrogen) thay vì 29 (không khí) khi tính tỉ khối so với không khí.
- Nhầm tỉ khối $d$ có đơn vị; thực ra tỉ khối là con số không có đơn vị vì là thương hai khối lượng mol.

<sub>`lesson.chemistry.thcs-hoa-sinh.the-tich-khi-ti-khoi`</sub>

---

### 3. Phần trăm khối lượng nguyên tố trong hợp chất
*Percent composition by mass of a compound* · THCS · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Tính được phần trăm khối lượng của mỗi nguyên tố trong một hợp chất
- Lập được công thức hoá học đơn giản khi biết phần trăm khối lượng các nguyên tố

## Ý tưởng: chia phần của mỗi nguyên tố

Hợp chất giống một chiếc bánh, mỗi nguyên tố góp một "miếng" khối lượng. Muốn biết miếng đó chiếm bao nhiêu phần trăm, ta lấy khối lượng nguyên tố chia cho khối lượng cả phân tử rồi nhân 100.

$$\%A = \frac{n_A\times M_A}{M_{\text{hợp chất}}}\times 100\%$$

với $n_A$ là số nguyên tử $A$ trong công thức.

## Các bước

1. Tính phân tử khối của hợp chất.
2. Tính khối lượng phần của từng nguyên tố (số nguyên tử nhân nguyên tử khối).
3. Chia cho phân tử khối, nhân 100%.

Mẹo kiểm tra: cộng phần trăm của tất cả nguyên tố phải bằng $100\%$.

## Chiều ngược lại

Biết phần trăm, ta có thể **lập công thức**: đặt công thức $A_xB_y$, dùng phần trăm để tìm tỉ lệ $x:y$. Đây là cách nhà hoá học suy ra thành phần một chất mới từ kết quả phân tích.

**Lỗi thường gặp:**
- Quên nhân số nguyên tử: trong $NH_4NO_3$ có 2 nguyên tử N nên phải lấy $2\times14$, không phải 14.
- Chia cho nguyên tử khối của nguyên tố thay vì cho phân tử khối của cả hợp chất.
- Không kiểm tra lại tổng phần trăm bằng 100% nên bỏ sót sai sót tính toán.

<sub>`lesson.chemistry.thcs-hoa-sinh.phan-tram-khoi-luong-nguyen-to`</sub>

---

### 4. Tính theo phương trình hoá học và định luật bảo toàn khối lượng
*Stoichiometry and the law of conservation of mass* · THCS · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phát biểu và vận dụng được định luật bảo toàn khối lượng trong phản ứng hoá học
- Tính được lượng chất tham gia hoặc tạo thành dựa vào tỉ lệ số mol trong phương trình

## Định luật bảo toàn khối lượng

Lavoisier phát hiện: trong một phản ứng, nguyên tử không tự sinh ra hay mất đi, chỉ sắp xếp lại. Vì thế **tổng khối lượng không đổi**. Với phản ứng $A + B \rightarrow C + D$:

$$m_A + m_B = m_C + m_D$$

Biết ba khối lượng là suy ngay ra khối lượng còn lại.

## Tính theo phương trình

Hệ số trong phương trình chính là **tỉ lệ số mol**. Ví dụ:

$$Zn + 2HCl \rightarrow ZnCl_2 + H_2$$

cho biết 1 mol $Zn$ sinh ra 1 mol khí $H_2$. Các bước làm:

1. Viết và cân bằng phương trình.
2. Đổi dữ kiện đề (gam, lít) về **số mol**.
3. Dùng tỉ lệ hệ số suy ra số mol chất cần tìm.
4. Đổi số mol đó về khối lượng hoặc thể tích theo yêu cầu.

Đây là "xương sống" của mọi bài toán hoá học: luôn đi qua số mol ở giữa.

**Lỗi thường gặp:**
- Quên cân bằng phương trình nên lấy sai tỉ lệ mol giữa các chất.
- Cộng thẳng khối lượng theo tỉ lệ hệ số mà không đổi ra số mol trước — tỉ lệ hệ số là tỉ lệ MOL, không phải tỉ lệ khối lượng.
- Áp bảo toàn khối lượng nhưng bỏ sót khối lượng chất khí thoát ra hoặc kết tủa tách ra.

<sub>`lesson.chemistry.thcs-hoa-sinh.tinh-theo-phuong-trinh-bao-toan-khoi-luong`</sub>

---

### 5. Hiệu suất phản ứng và độ tinh khiết
*Reaction yield and sample purity* · THCS · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được hiệu suất phản ứng khi biết lượng sản phẩm thực tế và lí thuyết
- Vận dụng hiệu suất để tính lượng sản phẩm thu được trên thực tế

## Vì sao không phải lúc nào cũng thu đủ

Tính theo phương trình cho ta lượng sản phẩm **lí thuyết** — nếu phản ứng xảy ra hoàn toàn. Nhưng thực tế thường thất thoát: phản ứng chưa hết, sản phẩm bám dụng cụ, tạo chất phụ... nên lượng thu được **thực tế** ít hơn.

## Công thức hiệu suất

$$H = \frac{\text{lượng thực tế}}{\text{lượng lí thuyết}}\times 100\%$$

Có thể tính theo khối lượng hoặc theo số mol của cùng một chất. Vì thực tế $\le$ lí thuyết nên $H \le 100\%$.

## Dùng ngược để dự đoán

Biết hiệu suất, ta tính được lượng thực sự thu được:

$$\text{thực tế} = \text{lí thuyết}\times \frac{H}{100}$$

## Các bước giải

1. Tính lượng sản phẩm **lí thuyết** theo phương trình.
2. So với lượng **thực tế** đề cho (hoặc ngược lại).
3. Áp công thức, chú ý cùng một đơn vị và cùng một chất.

**Lỗi thường gặp:**
- Lấy lượng thực tế chia cho lượng chất ban đầu thay vì cho lượng sản phẩm lí thuyết.
- Cho ra hiệu suất lớn hơn 100% mà không nhận ra vô lí (thực tế luôn $\le$ lí thuyết).
- Tính hiệu suất giữa hai chất khác nhau; phải so cùng một chất (cùng sản phẩm hoặc cùng chất tham gia).

<sub>`lesson.chemistry.thcs-hoa-sinh.hieu-suat-phan-ung`</sub>

---

## Chuyên đề: Các dạng bài toán vô cơ giải nhanh

### 1. Bài toán CO2, SO2 tác dụng với dung dịch kiềm
*CO2 and SO2 reacting with alkali solutions* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Xác định muối tạo thành khi cho CO2 (SO2) vào dung dịch kiềm dựa vào tỉ lệ T
- Giải được bài toán ngược có hai nghiệm khi biết lượng kết tủa

## Vì sao phải xét tỉ lệ

Khi sục $\mathrm{CO_2}$ vào dung dịch kiềm, có thể tạo muối trung hoà $\mathrm{CO_3^{2-}}$, muối acid $\mathrm{HCO_3^-}$, hoặc cả hai — tuỳ lượng $\mathrm{OH^-}$ so với $\mathrm{CO_2}$. Đặt:
$$T = \frac{n_{\mathrm{OH^-}}}{n_{\mathrm{CO_2}}}.$$
- $T \le 1$: chỉ tạo $\mathrm{HCO_3^-}$ (CO2 dư hoặc vừa đủ tạo muối acid);
- $1 < T < 2$: tạo **cả hai** muối;
- $T \ge 2$: chỉ tạo $\mathrm{CO_3^{2-}}$ (kiềm dư).

## Tính nhanh khi tạo hai muối

Dùng bảo toàn nguyên tố C và điện tích:
$$n_{\mathrm{CO_3^{2-}}} = n_{\mathrm{OH^-}} - n_{\mathrm{CO_2}}, \qquad n_{\mathrm{HCO_3^-}} = 2n_{\mathrm{CO_2}} - n_{\mathrm{OH^-}}.$$
Hai công thức này suy ra từ: bảo toàn C ($n_{\mathrm{CO_3}}+n_{\mathrm{HCO_3}}=n_{\mathrm{CO_2}}$) và bảo toàn điện tích/OH ($2n_{\mathrm{CO_3}}+n_{\mathrm{HCO_3}}=n_{\mathrm{OH^-}}$).

## Bài toán ngược: cẩn thận hai nghiệm

Sục $\mathrm{CO_2}$ vào $\mathrm{Ca(OH)_2}$ tạo kết tủa $\mathrm{CaCO_3}$. Nếu lượng kết tủa **nhỏ hơn cực đại**, có **hai** khả năng:
- **Thiếu $\mathrm{CO_2}$**: $n_{\mathrm{CO_2}} = n_{\downarrow}$;
- **Dư $\mathrm{CO_2}$** đã hoà tan bớt kết tủa thành $\mathrm{Ca(HCO_3)_2}$: $n_{\mathrm{CO_2}} = 2n_{\mathrm{Ca(OH)_2}} - n_{\downarrow}$.
Đề thường yêu cầu tìm giá trị lớn nhất/nhỏ nhất, hoặc cả hai. Bỏ sót một nghiệm là lỗi kinh điển.

## Khi nào dùng

Gặp "sục khí vào kiềm": tính $T$ để biết muối, rồi áp công thức. Gặp "biết lượng kết tủa": nghĩ ngay tới hai nghiệm.

**Lỗi thường gặp:**
- Mặc định luôn tạo muối trung hoà mà không xét tỉ lệ $T$ — sai vì khi $\mathrm{CO_2}$ dư sẽ tạo muối acid $\mathrm{HCO_3^-}$.
- Bài toán ngược chỉ lấy một nghiệm $n_{\mathrm{CO_2}}=n_{\downarrow}$ — bỏ sót nghiệm CO2 dư hoà tan bớt kết tủa, thiếu một đáp án.
- Quên $\mathrm{Ca(OH)_2}$ cho 2 mol $\mathrm{OH^-}$ mỗi mol khi tính $n_{\mathrm{OH^-}}$ — làm sai tỉ lệ $T$.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.co2-so2-tac-dung-kiem`</sub>

---

### 2. Muối nhôm, kẽm tác dụng với dung dịch kiềm
*Aluminium and zinc salts reacting with alkali* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Giải được bài toán lượng OH- tạo kết tủa Al(OH)3, Zn(OH)2 với hai nghiệm
- Vận dụng tính lưỡng tính của hydroxide để tính lượng kết tủa cực đại và hoà tan

## Đặc điểm quyết định: tính lưỡng tính

Cho từ từ $\mathrm{OH^-}$ vào dung dịch $\mathrm{Al^{3+}}$: đầu tiên tạo kết tủa $\mathrm{Al(OH)_3}$, đạt **cực đại** khi $n_{\mathrm{OH^-}}=3n_{\mathrm{Al^{3+}}}$. Thêm $\mathrm{OH^-}$ nữa, kết tủa **tan** dần thành $\mathrm{AlO_2^-}$ (aluminate) và biến mất hết khi $n_{\mathrm{OH^-}}=4n_{\mathrm{Al^{3+}}}$.

## Hai nghiệm cho một lượng kết tủa

Nếu đề cho lượng kết tủa $n_\downarrow < n_\downarrow^{max}$, có **hai giá trị** $\mathrm{OH^-}$:
- **Kết tủa chưa cực đại** (thiếu OH): $n_{\mathrm{OH^-}} = 3n_\downarrow$;
- **Kết tủa đã bị hoà tan bớt** (dư OH): $n_{\mathrm{OH^-}} = 4n_{\mathrm{Al^{3+}}} - n_\downarrow$.
Đồ thị lượng kết tủa theo $n_{\mathrm{OH^-}}$ có dạng tam giác: tăng tuyến tính đến đỉnh rồi giảm, nên mỗi mức kết tủa (trừ đỉnh) cắt đồ thị hai lần.

## Với kẽm hệ số khác

$\mathrm{Zn^{2+}}$ cũng lưỡng tính nhưng: kết tủa cực đại khi $n_{\mathrm{OH^-}}=2n_{\mathrm{Zn^{2+}}}$, tan hết khi $n_{\mathrm{OH^-}}=4n_{\mathrm{Zn^{2+}}}$. Nghiệm dư: $n_{\mathrm{OH^-}}=4n_{\mathrm{Zn^{2+}}}-2n_\downarrow$.

## Hỗn hợp Na, Al vào nước

Na tác dụng nước tạo NaOH, NaOH lại hoà tan Al. Al chỉ tan hết khi $n_{\mathrm{NaOH}}\ge n_{\mathrm{Al}}$ (tỉ lệ 1:1 tạo $\mathrm{NaAlO_2}$). Khí $\mathrm{H_2}$ gồm phần từ Na và phần từ Al.

## Khi nào dùng

Gặp "nhỏ từ từ kiềm vào muối nhôm/kẽm, thu được x mol kết tủa": nghĩ ngay hai nghiệm, so với cực đại để biết có hoà tan hay chưa.

**Lỗi thường gặp:**
- Chỉ lấy nghiệm $n_{\mathrm{OH^-}}=3n_\downarrow$ mà quên nghiệm kiềm dư hoà tan bớt kết tủa — thiếu một đáp số.
- Dùng hệ số của nhôm (3 và 4) cho kẽm — sai vì $\mathrm{Zn^{2+}}$ có cực đại ở $2n$ và tan hết ở $4n$.
- Cho rằng $\mathrm{Al(OH)_3}$ tan trong kiềm yếu như $\mathrm{NH_3}$ — sai vì $\mathrm{Al(OH)_3}$ chỉ tan trong kiềm mạnh (NaOH, KOH), không tan trong $\mathrm{NH_3}$.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.muoi-nhom-kem-voi-kiem`</sub>

---

### 3. Kim loại tác dụng với HNO3 và H2SO4 đặc
*Metals reacting with nitric acid and hot concentrated sulfuric acid* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · chuyen-sau

**Mục tiêu:**
- Vận dụng bảo toàn electron để tính số mol khí và số mol kim loại phản ứng
- Tính được khối lượng muối và lượng axit phản ứng, kể cả trường hợp tạo NH4NO3

## Axit oxi hoá mạnh: N và S nhận electron

Với $\mathrm{HNO_3}$ và $\mathrm{H_2SO_4}$ đặc, chất oxi hoá không phải $\mathrm{H^+}$ mà là $\mathrm{N^{+5}}$ và $\mathrm{S^{+6}}$. Kim loại bị oxi hoá lên hoá trị cao, N/S bị khử tạo các sản phẩm: $\mathrm{NO_2, NO, N_2O, N_2, NH_4^+}$ (với $\mathrm{HNO_3}$) hoặc $\mathrm{SO_2, S, H_2S}$ (với $\mathrm{H_2SO_4}$ đặc). Vì thế **không có khí $\mathrm{H_2}$**.

## Số electron mỗi sản phẩm khử nhận

$$\begin{array}{ll}\mathrm{NO_2}: 1e & \mathrm{NO}: 3e\\ \mathrm{N_2O}: 8e & \mathrm{N_2}: 10e\\ \mathrm{NH_4^+}: 8e & \mathrm{SO_2}: 2e\end{array}$$
Bảo toàn electron: $\sum n_e(\text{kim loại cho}) = \sum (\text{số } e \times n_{\text{sản phẩm}})$.

## Công thức khối lượng muối

Muối nitrat: $m_{\text{muối}} = m_{\text{kim loại}} + 62\,n_{\mathrm{NO_3^-(muối)}}$, mà $n_{\mathrm{NO_3^-(muối)}} = n_e$ trao đổi. Nếu có $\mathrm{NH_4NO_3}$ thì cộng thêm khối lượng của nó.
Muối sulfat: $m_{\text{muối}} = m_{\text{kim loại}} + 96\,n_{\mathrm{SO_4^{2-}(muối)}}$, với $n_{\mathrm{SO_4^{2-}}} = \tfrac12 n_e$ (vì gốc mang điện $2-$).

## Cảnh giác NH4NO3

Khi kim loại mạnh (Mg, Al, Zn) + $\mathrm{HNO_3}$ rất loãng, có thể tạo $\mathrm{NH_4NO_3}$ không thoát khí. Nếu bài cho "không có khí" hoặc electron cho nhiều hơn electron khí nhận, phần chênh lệch chính là electron tạo $\mathrm{NH_4^+}$: $n_{\mathrm{NH_4NO_3}} = (n_e - n_{e\,khí})/8$.

## Khi nào dùng

Mọi bài kim loại + $\mathrm{HNO_3}$/$\mathrm{H_2SO_4}$ đặc: viết bảo toàn electron trước, rồi mới tính khối lượng muối và axit ($n_{\mathrm{HNO_3}}=n_{\mathrm{NO_3^-(muối)}}+n_{\mathrm{N(khí)}}+n_{\mathrm{N(NH_4)}}$).

**Lỗi thường gặp:**
- Cho rằng kim loại + $\mathrm{HNO_3}$ hay $\mathrm{H_2SO_4}$ đặc sinh khí $\mathrm{H_2}$ — sai vì chất oxi hoá là N/S, sản phẩm khử là $\mathrm{NO_x, SO_2}$..., không phải $\mathrm{H_2}$.
- Bỏ qua khả năng tạo $\mathrm{NH_4NO_3}$ khi kim loại mạnh gặp $\mathrm{HNO_3}$ loãng — làm thiếu electron và sai khối lượng muối.
- Lấy $n_{\mathrm{SO_4^{2-}}}=n_e$ thay vì $n_e/2$ khi tính muối sulfat — sai vì gốc $\mathrm{SO_4^{2-}}$ mang điện tích $2-$.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.kim-loai-hno3-h2so4-dac`</sub>

---

### 4. Kim loại với axit loãng, khử oxit kim loại và nhiệt nhôm
*Metals with dilute acids, reduction of metal oxides and thermite reactions* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Tính khối lượng muối và thể tích H2 khi kim loại tác dụng axit loãng bằng bảo toàn
- Vận dụng bảo toàn nguyên tố và khối lượng cho phản ứng khử oxit và nhiệt nhôm

## Kim loại + axit loãng: chỉ $\mathrm{H^+}$ oxi hoá

Với HCl, $\mathrm{H_2SO_4}$ loãng, chất oxi hoá là $\mathrm{H^+}$, sản phẩm khử là khí $\mathrm{H_2}$. Bảo toàn electron: $n_e = 2n_{\mathrm{H_2}}$. Khối lượng muối:
$$m_{\text{muối}} = m_{\text{kim loại}} + m_{\text{gốc acid}},$$
với HCl: $n_{\mathrm{Cl^-}}=2n_{\mathrm{H_2}}$; với $\mathrm{H_2SO_4}$ loãng: $n_{\mathrm{SO_4^{2-}}}=n_{\mathrm{H_2}}$. (Kim loại đứng sau H như Cu không phản ứng.)

## Khử oxit kim loại bằng CO, H2

$\mathrm{CO}$ hoặc $\mathrm{H_2}$ lấy oxi của oxit kim loại (sau Al) tạo kim loại + $\mathrm{CO_2}$ (hoặc $\mathrm{H_2O}$). Mấu chốt là **bảo toàn nguyên tố oxi**: mỗi mol CO lấy 1 mol O. Khối lượng chất rắn giảm đúng bằng khối lượng oxi bị lấy đi:
$$m_{\text{rắn giảm}} = 16\,n_{\mathrm{O\,bị\,khử}} = 16\,n_{\mathrm{CO}} = 16\,n_{\mathrm{CO_2}}.$$

## Nhiệt nhôm

$\mathrm{2Al + Fe_2O_3 \to Al_2O_3 + 2Fe}$. Vì là phản ứng rắn - rắn, dùng **bảo toàn khối lượng** (khối lượng hỗn hợp không đổi trước và sau) và **bảo toàn nguyên tố** (Al, Fe, O). Hiệu suất tính theo chất phản ứng hết trước. Hỗn hợp sau gồm $\mathrm{Fe, Al_2O_3}$ và có thể còn Al hoặc $\mathrm{Fe_2O_3}$ dư.

## Khi nào dùng

- "Kim loại + HCl/$\mathrm{H_2SO_4}$ loãng, V lít $\mathrm{H_2}$": dùng $m_{\text{muối}}=m_{KL}+m_{\text{gốc}}$.
- "Khử oxit thu m gam kim loại": bảo toàn khối lượng, chú ý khối lượng O mất đi.
- "Nhiệt nhôm hiệu suất H%": bảo toàn khối lượng + nguyên tố.

**Lỗi thường gặp:**
- Cho rằng Cu (đứng sau H) tan trong HCl hay $\mathrm{H_2SO_4}$ loãng — sai vì chỉ kim loại đứng trước H mới khử được $\mathrm{H^+}$ thành $\mathrm{H_2}$.
- Lấy $n_{\mathrm{SO_4^{2-}}}=2n_{\mathrm{H_2}}$ với $\mathrm{H_2SO_4}$ loãng — sai vì mỗi $\mathrm{H_2}$ ứng với 1 gốc $\mathrm{SO_4^{2-}}$ (do $\mathrm{H_2SO_4}$ cho 2 H$^+$).
- Tính khối lượng chất rắn sau khử mà quên trừ khối lượng oxi bị lấy đi — làm sai khối lượng kim loại thu được.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.kim-loai-axit-loang-khu-oxit-nhiet-nhom`</sub>

---

### 5. Điện phân dung dịch, nước cứng và phân bón hoá học
*Solution electrolysis, water hardness and chemical fertilisers* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Xác định sản phẩm và tính lượng chất khi điện phân dung dịch muối
- Tính độ cứng của nước, lượng hoá chất làm mềm nước và độ dinh dưỡng của phân bón

## Điện phân dung dịch: nước cũng tham gia

Khác điện phân nóng chảy, trong dung dịch nước có thể bị điện phân. Thứ tự (điện cực trơ):
- **Catode**: $\mathrm{Ag^+, Cu^{2+}}$... bị khử trước; hết ion kim loại yếu thì nước bị khử: $\mathrm{2H_2O+2e\to H_2+2OH^-}$. Ion $\mathrm{Na^+, K^+, Al^{3+}}$ không bị khử.
- **Anode**: $\mathrm{Cl^-}$ bị oxi hoá tạo $\mathrm{Cl_2}$; hết $\mathrm{Cl^-}$ hoặc với gốc $\mathrm{SO_4^{2-}, NO_3^-}$ thì nước bị oxi hoá: $\mathrm{2H_2O\to O_2+4H^++4e}$.
Dùng bảo toàn electron hai cực ($n_e$ như nhau) và định luật Faraday để tính.

## Nước cứng và cách làm mềm

Nước cứng do $\mathrm{Ca^{2+}, Mg^{2+}}$. Làm mềm = kết tủa hai ion đó. $\mathrm{Na_2CO_3}$ kết tủa cả hai: mỗi mol $\mathrm{CO_3^{2-}}$ loại 1 mol $\mathrm{M^{2+}}$, nên $n_{\mathrm{Na_2CO_3}} = n_{\mathrm{Ca^{2+}}}+n_{\mathrm{Mg^{2+}}}$. Nước cứng tạm thời (chứa $\mathrm{HCO_3^-}$) còn làm mềm được bằng cách đun sôi.

## Độ dinh dưỡng của phân bón

- Phân **đạm** đánh giá qua $\%\mathrm{N}$. Ví dụ urea $(\mathrm{NH_2})_2\mathrm{CO}$ ($M=60$) có $\%\mathrm{N}=\dfrac{28}{60}\times100\%\approx46{,}7\%$ — cao nhất trong các phân đạm.
- Phân **lân** đánh giá qua $\%\mathrm{P_2O_5}$.
- Phân **kali** đánh giá qua $\%\mathrm{K_2O}$.
Quy đổi: từ số mol N (hoặc P, K) trong công thức, suy khối lượng nguyên tố dinh dưỡng rồi chia khối lượng phân.

## Khi nào dùng

Gặp điện phân dung dịch: xác định thứ tự điện cực rồi Faraday. Gặp nước cứng: đếm $\mathrm{Ca^{2+}+Mg^{2+}}$. Gặp phân bón: quy về phần trăm nguyên tố dinh dưỡng.

**Lỗi thường gặp:**
- Cho rằng $\mathrm{Na^+}$ bị khử ở catode khi điện phân dung dịch NaCl — sai vì nước bị khử trước tạo $\mathrm{H_2}$ và $\mathrm{OH^-}$.
- Tính lượng $\mathrm{Na_2CO_3}$ chỉ theo $\mathrm{Ca^{2+}}$ mà bỏ $\mathrm{Mg^{2+}}$ — sai vì cả hai ion đều gây cứng và đều bị kết tủa.
- Đánh giá phân đạm theo khối lượng phân thay vì phần trăm N — sai vì độ dinh dưỡng quy về hàm lượng nguyên tố dinh dưỡng.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.dien-phan-dung-dich-nuoc-cung-phan-bon`</sub>

---

## Chuyên đề: Đại lượng cơ bản và các định luật bảo toàn

### 1. Mol, tỉ khối chất khí và khối lượng mol trung bình
*Mole, gas density ratio and average molar mass* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Chuyển đổi thành thạo giữa khối lượng, số mol, số hạt và thể tích khí
- Tính được tỉ khối chất khí và khối lượng mol trung bình của hỗn hợp khí

## Mol là trung tâm của mọi tính toán

Phản ứng xảy ra theo tỉ lệ số hạt, nhưng ta cân được khối lượng và đo được thể tích. **Mol** nối ba đại lượng đó:

$$n = \frac{m}{M} = \frac{N}{N_A} = \frac{V_{\text{khí}}}{V_m}$$

Theo GDPT 2018, ở điều kiện chuẩn (25$^\circ$C, 1 bar) thể tích mol khí $V_m = 24{,}79$ L/mol.

## Tỉ khối: cân khí bằng khí

Hai khí cùng điều kiện thì tỉ lệ khối lượng bằng tỉ lệ khối lượng mol:

$$d_{A/B} = \frac{M_A}{M_B}, \qquad d_{A/\text{kk}} = \frac{M_A}{29}$$

Biết tỉ khối là biết ngay khối lượng mol, rất tiện để nhận dạng khí.

## Khối lượng mol trung bình của hỗn hợp

Khi trộn nhiều khí, ta coi hỗn hợp như một khí giả định có:

$$\bar M = \frac{m_{hh}}{n_{hh}} = \frac{\sum n_i M_i}{\sum n_i} = \sum x_i M_i$$

với $x_i$ là phần mol. Tính chất quan trọng: $\bar M$ luôn nằm **giữa** $M$ nhỏ nhất và $M$ lớn nhất; nếu tính ra ngoài khoảng đó thì chắc chắn sai.

## Khi nào dùng

Hỗn hợp khí biết tỉ khối so với H$_2$ (hay không khí) $\Rightarrow$ suy $\bar M = 2 d_{hh/H_2}$; kết hợp với tổng mol để lập hệ tìm thành phần.

**Lỗi thường gặp:**
- Tính $\bar M$ bằng trung bình cộng đơn giản của các $M$ mà bỏ số mol — sai vì phải lấy trung bình có trọng số theo số mol (phần mol).
- Dùng $V_m = 22{,}4$ L/mol cho điều kiện chuẩn GDPT 2018 — sai vì ở 25$^\circ$C, 1 bar giá trị đúng là $24{,}79$ L/mol; $22{,}4$ chỉ ứng với $0^\circ$C.
- Chấp nhận $\bar M$ nằm ngoài khoảng $[M_{min}; M_{max}]$ — vô lí vì trung bình có trọng số luôn nằm trong khoảng đó, dấu hiệu tính sai.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.mol-ti-khoi-khoi-luong-mol-trung-binh`</sub>

---

### 2. Nồng độ dung dịch, pha loãng và quy tắc đường chéo
*Solution concentration, dilution and the cross rule* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Chuyển đổi giữa nồng độ mol và nồng độ phần trăm dựa vào khối lượng riêng
- Vận dụng quy tắc đường chéo để tính tỉ lệ pha trộn hai dung dịch cùng chất

## Hai cách đo "đậm đặc"

Nồng độ mô tả lượng chất tan trong dung dịch. Hai đại lượng hay dùng:
$$C_M = \frac{n}{V\,(\text{lít})}, \qquad C\% = \frac{m_{ct}}{m_{dd}}\times100\%.$$
Chúng liên hệ qua khối lượng riêng $D$ (g/mL): $C_M = \dfrac{10\,D\,C\%}{M}$.

## Pha loãng: chất tan không đổi

Thêm dung môi làm loãng nhưng **số mol chất tan giữ nguyên**, nên:
$$C_1 V_1 = C_2 V_2.$$
Đây là chìa khoá mọi bài pha loãng hay cô đặc.

## Quy tắc đường chéo: trộn để đạt nồng độ giữa

Trộn dung dịch nồng độ $C_1$ (đậm) với $C_2$ (loãng) để được $C$ ($C_2 < C < C_1$). Tỉ lệ khối lượng (hoặc thể tích nếu cùng đơn vị nồng độ mol và bỏ qua co thể tích) là:
$$\frac{m_1}{m_2} = \frac{|C - C_2|}{|C_1 - C|}.$$
Cách nhớ: viết $C_1$ và $C_2$ ở hai góc trái, $C$ ở giữa, lấy hiệu chéo. Lượng dung dịch nào lấy nhiều hơn thì nồng độ của nó gần $C$ hơn.

## Đọc kĩ điều kiện áp dụng

Đường chéo cho **tỉ lệ thể tích** chỉ chính xác khi hai dung dịch cùng loại nồng độ (đều $C_M$) và thể tích cộng được. Với nồng độ phần trăm, đường chéo cho **tỉ lệ khối lượng**.

## Khi nào dùng

Bài "trộn hai dung dịch cùng chất để được nồng độ cho trước": dùng ngay đường chéo thay vì lập hệ, nhanh hơn nhiều.

**Lỗi thường gặp:**
- Đặt hiệu chéo nhầm vị trí, lấy $|C_1-C|$ cho dung dịch đậm — sai vì lượng dung dịch đậm tỉ lệ với hiệu ở phía dung dịch loãng $|C-C_2|$.
- Dùng công thức pha loãng $C_1V_1=C_2V_2$ cho phản ứng có chất tan bị tiêu thụ — sai vì công thức này chỉ đúng khi số mol chất tan được bảo toàn (chỉ thêm dung môi).
- Áp dụng đường chéo cho tỉ lệ thể tích với hai dung dịch khác loại nồng độ ($C_M$ và $C\%$) — sai vì phải quy về cùng loại nồng độ trước.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.nong-do-pha-loang-duong-cheo`</sub>

---

### 3. Các định luật bảo toàn: khối lượng, nguyên tố, electron và điện tích
*Conservation laws: mass, element, electron and charge* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng bảo toàn khối lượng và bảo toàn nguyên tố để giải nhanh bài toán hỗn hợp
- Vận dụng bảo toàn electron cho phản ứng oxi hoá - khử và bảo toàn điện tích cho dung dịch

## Vì sao dùng định luật bảo toàn thay vì viết đủ phương trình

Trong thi trắc nghiệm, viết và cân bằng mọi phương trình rất mất thời gian. Các **định luật bảo toàn** cho phép "nhảy thẳng" từ dữ kiện đầu đến đại lượng cần tìm, bỏ qua chi tiết trung gian.

## Bốn công cụ chủ lực

**Bảo toàn khối lượng**: $\sum m_{\text{chất đầu}} = \sum m_{\text{sản phẩm}}$. Rất mạnh với bài "kim loại + axit $\to$ muối + khí": $m_{\text{muối}} = m_{\text{kim loại}} + m_{\text{gốc axit}}$.

**Bảo toàn nguyên tố**: số mol một nguyên tố không đổi qua phản ứng. Ví dụ mọi nguyên tử Na trong NaOH cuối cùng nằm trong muối natri.

**Bảo toàn electron**: $\sum n_e(\text{cho}) = \sum n_e(\text{nhận})$. Cho phép bỏ qua sản phẩm khử trung gian, chỉ cần đếm electron.

**Bảo toàn điện tích** (trong dung dịch):
$$\sum (\text{số mol cation}\times\text{điện tích}) = \sum (\text{số mol anion}\times|\text{điện tích}|).$$
Dùng để tìm số mol một ion còn thiếu hoặc khối lượng muối khan khi cô cạn.

## Chọn định luật nào

- Bài có khí thoát ra, biết khối lượng chất rắn trước - sau: bảo toàn khối lượng.
- Bài oxi hoá - khử, nhiều sản phẩm khử: bảo toàn electron.
- Bài cho danh sách ion trong dung dịch: bảo toàn điện tích.
Thường phải phối hợp hai, ba định luật trong một bài.

## Khi nào dùng

Hễ gặp "hỗn hợp", "cô cạn dung dịch thu m gam muối", hay "tính V khí", hãy nghĩ tới bảo toàn trước khi viết phương trình.

**Lỗi thường gặp:**
- Bỏ sót một ion khi viết bảo toàn điện tích — làm phương trình điện tích không cân, dẫn tới sai số mol ion cần tìm.
- Tính $n_{\mathrm{Cl^-}} = n_{\mathrm{H_2}}$ thay vì $2n_{\mathrm{H_2}}$ — sai vì mỗi phân tử $\mathrm{H_2}$ ứng với 2 nguyên tử H, tức 2 gốc $\mathrm{Cl^-}$ đi vào muối.
- Áp dụng bảo toàn khối lượng mà quên khối lượng khí thoát ra khỏi hệ — sai vì khí $\mathrm{H_2}$ bay đi không còn trong dung dịch.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.cac-dinh-luat-bao-toan`</sub>

---

## Chương 1: Cấu tạo nguyên tử

### 1. Thành phần nguyên tử, số khối, đồng vị và nguyên tử khối trung bình
*Atomic composition, mass number, isotopes and average atomic mass* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Xác định được số proton, neutron, electron của nguyên tử và ion từ kí hiệu nguyên tử
- Phân biệt được số khối với nguyên tử khối và giải thích vì sao đồng vị có cùng số proton
- Tính được nguyên tử khối trung bình và phần trăm mỗi đồng vị

## Vì sao cần phân biệt số khối và nguyên tử khối

Nguyên tử gồm hạt nhân (proton mang điện $+1$, neutron trung hoà) và lớp vỏ electron (điện $-1$). Vì proton và neutron nặng gần bằng nhau và gấp khoảng 1836 lần electron, khối lượng nguyên tử tập trung ở hạt nhân. Ta quy ước **số khối** $A = Z + N$ để đếm số hạt nặng, còn nguyên tử khối là khối lượng thực đo bằng amu.

## Đồng vị sinh ra từ đâu

Nguyên tố được định danh bằng $Z$ (số proton). Nhưng cùng một $Z$ có thể ứng với nhiều giá trị $N$: đó là các **đồng vị**. Ví dụ chlorine có $^{35}\mathrm{Cl}$ và $^{37}\mathrm{Cl}$, cùng 17 proton nhưng 18 và 20 neutron.

## Cầu nối với thí nghiệm: nguyên tử khối trung bình

Phổ khối cho biết phần trăm số nguyên tử mỗi đồng vị. Vì trong tự nhiên các đồng vị trộn lẫn theo tỉ lệ cố định, giá trị ghi trong bảng tuần hoàn là **trung bình có trọng số**:

$$\bar{A} = \frac{a_1 A_1 + a_2 A_2 + \dots}{100}$$

trong đó $a_i$ là phần trăm số nguyên tử của đồng vị $i$. Chính vì thế nguyên tử khối trung bình thường không phải số nguyên, dù mỗi số khối riêng lẻ đều nguyên.

## Khi nào dùng

Gặp bài cho $\bar{A}$ và hai đồng vị, đặt phần trăm một đồng vị là $x$, lập phương trình một ẩn rồi giải.

**Lỗi thường gặp:**
- Lấy nguyên tử khối trung bình làm số khối để tính neutron — sai vì $\bar{A}$ là số thập phân trung bình của nhiều đồng vị, còn $N=A-Z$ phải dùng số khối nguyên của một đồng vị cụ thể.
- Cho rằng ion $\mathrm{X}^{2+}$ có ít hơn 2 proton — sai vì điện tích dương sinh ra do mất electron, số proton (đặc trưng nguyên tố) luôn giữ nguyên.
- Nhầm phần trăm khối lượng với phần trăm số nguyên tử khi tính $\bar{A}$ — công thức trung bình dùng phần trăm số nguyên tử; dùng phần trăm khối lượng sẽ cho kết quả lệch.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.nguyen-tu-thanh-phan-so-khoi-dong-vi`</sub>

---

### 2. Cấu hình electron của nguyên tử và ion
*Electron configuration of atoms and ions* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Viết được cấu hình electron của nguyên tử theo nguyên lí vững bền, quy tắc Hund và nguyên lí Pauli
- Suy ra được cấu hình electron của ion dương và ion âm từ nguyên tử tương ứng
- Xác định được số electron độc thân và tính chất kim loại/phi kim từ cấu hình

## Trật tự lấp đầy các mức năng lượng

Electron không phân bố tuỳ tiện. Theo **nguyên lí vững bền**, chúng chiếm mức năng lượng thấp trước. Trật tự thực nghiệm (quy tắc Klechkovski, sắp theo $n+l$ tăng) là:

$$1s\,2s\,2p\,3s\,3p\,4s\,3d\,4p\,5s\,4d\,5p\,6s\dots$$

Điểm dễ quên: $4s$ điền trước $3d$ vì mức năng lượng $4s$ thấp hơn khi đang lấp.

## Ba nguyên tắc chi phối

- **Nguyên lí Pauli**: mỗi orbital chứa tối đa 2 electron ngược chiều spin.
- **Quy tắc Hund**: trong một phân lớp chưa đầy, electron trải đều ra các orbital trước khi ghép đôi, cho số electron độc thân lớn nhất.
- Phân lớp $s,p,d$ chứa tối đa $2,6,10$ electron.

## Cấu hình của ion — cẩn thận thứ tự bỏ electron

Khi tạo **ion dương**, nguyên tử **mất electron ở lớp ngoài cùng trước** (lớp $n$ lớn nhất), không phải bỏ theo thứ tự điền. Với kim loại chuyển tiếp, bỏ $4s$ trước rồi mới đến $3d$. Ví dụ $\mathrm{Fe}: [\mathrm{Ar}]3d^6 4s^2 \to \mathrm{Fe^{2+}}: [\mathrm{Ar}]3d^6$ (bỏ 2 electron $4s$), $\mathrm{Fe^{3+}}: [\mathrm{Ar}]3d^5$.

Khi tạo **ion âm**, nguyên tử nhận thêm electron vào phân lớp đang dở, ví dụ $\mathrm{Cl}: [\mathrm{Ne}]3s^2 3p^5 \to \mathrm{Cl^-}: [\mathrm{Ne}]3s^2 3p^6$.

## Vì sao quan trọng

Số electron lớp ngoài cùng cho biết nguyên tố là kim loại (1–3e ngoài, dễ nhường), phi kim (5–7e, dễ nhận) hay khí hiếm (8e, bền).

**Lỗi thường gặp:**
- Bỏ electron ở phân lớp $3d$ trước $4s$ khi tạo ion dương — sai vì khi ion hoá, lớp có $n$ lớn nhất ($4s$) bị lấy trước dù nó được điền sau.
- Điền $3d$ trước $4s$ khi viết cấu hình nguyên tử — sai vì lúc lấp đầy, $4s$ có mức năng lượng thấp hơn nên được điền trước.
- Quên quy tắc Hund, ghép đôi electron ngay khi phân lớp chưa đầy — dẫn đến đếm sai số electron độc thân và sai tính chất từ.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.cau-hinh-electron`</sub>

---

### 3. Năng lượng ion hoá và cấu trúc lớp vỏ electron
*Ionisation energy and the electron shell structure* · THPT (lớp 10-12) · vn-gdpt-2018 · 35 phút · trung-binh

**Mục tiêu:**
- Định nghĩa được năng lượng ion hoá thứ nhất và giải thích xu hướng biến đổi của nó
- Vận dụng bước nhảy năng lượng ion hoá liên tiếp để suy ra số electron hoá trị và nhóm của nguyên tố

## Năng lượng ion hoá đo điều gì

**Năng lượng ion hoá thứ nhất** $I_1$ là năng lượng cần để bứt electron liên kết yếu nhất khỏi nguyên tử khí:

$$\mathrm{X}(g) \to \mathrm{X^+}(g) + e^-, \quad \Delta H = I_1 > 0$$

$I_1$ càng lớn thì electron càng bị hạt nhân giữ chặt. Nó phản ánh trực tiếp lực hút hạt nhân lên electron ngoài cùng.

## Xu hướng trong bảng tuần hoàn

Đi từ trái sang phải trong một chu kì, điện tích hạt nhân tăng nhưng electron thêm vào cùng lớp, bán kính giảm nên $I_1$ **tăng**. Đi xuống một nhóm, lớp electron tăng, electron ngoài cùng xa hạt nhân và bị chắn nhiều hơn nên $I_1$ **giảm**. (Có vài bất thường nhỏ như từ nhóm IIA sang IIIA do cấu trúc phân lớp.)

## Chìa khoá suy luận: bước nhảy $I_k$

Dãy $I_1 < I_2 < I_3 < \dots$ luôn tăng vì tách electron khỏi ion dương ngày càng khó. Nhưng khi vừa tách hết electron hoá trị và bắt đầu chạm vào lớp trong (gần hạt nhân, rất bền), năng lượng **nhảy vọt**. Vị trí bước nhảy cho biết số electron lớp ngoài cùng, tức nhóm của nguyên tố.

Ví dụ nếu $I_1, I_2$ gần nhau rồi $I_3$ nhảy vọt, nguyên tố có 2 electron hoá trị $\Rightarrow$ nhóm IIA (kim loại kiềm thổ).

## Khi nào dùng

Đề cho dãy $I_1$ đến $I_n$ và hỏi nhóm/tên nguyên tố: tìm chỗ tỉ số $I_{k+1}/I_k$ lớn bất thường, số electron hoá trị bằng $k$.

**Lỗi thường gặp:**
- Cho rằng năng lượng ion hoá luôn tăng đều nên bỏ qua bước nhảy — sai vì chính bước nhảy đột ngột (khi chạm lớp trong) mới là dấu hiệu xác định số electron hoá trị.
- Kết luận $I_1$ giảm khi sang phải trong chu kì — sai vì sang phải điện tích hạt nhân tăng, bán kính giảm, electron bị giữ chặt hơn nên $I_1$ tăng.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.nang-luong-ion-hoa`</sub>

---

## Chương 2: Bảng tuần hoàn các nguyên tố hoá học và định luật tuần hoàn

### 1. Cấu tạo bảng tuần hoàn và mối liên hệ với cấu hình electron
*Structure of the periodic table and its link to electron configuration* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Xác định được ô, chu kì, nhóm của nguyên tố từ cấu hình electron
- Giải thích được vì sao số thứ tự chu kì bằng số lớp và số thứ tự nhóm A bằng số electron lớp ngoài cùng

## Bảng tuần hoàn là bản đồ của cấu hình electron

Mendeleev sắp nguyên tố theo khối lượng, nhưng bảng hiện đại sắp theo **số hiệu nguyên tử $Z$ tăng dần**. Sức mạnh của bảng nằm ở chỗ vị trí mỗi nguyên tố phản ánh trực tiếp cấu hình electron của nó.

## Ba toạ độ và ba quy tắc

- **Ô**: số thứ tự ô $=Z=$ số proton $=$ số electron của nguyên tử trung hoà.
- **Chu kì**: số thứ tự chu kì $=$ số lớp electron. Ví dụ nguyên tố có lớp ngoài là lớp thứ 3 thì ở chu kì 3.
- **Nhóm A**: số thứ tự nhóm A $=$ số electron lớp ngoài cùng (chỉ áp dụng cho nguyên tố nhóm A, tức khối $s$ và $p$).

## Vì sao các quy tắc này đúng

Electron điền lần lượt vào các lớp; khi bắt đầu một lớp mới ta bắt đầu một chu kì mới, nên số lớp bằng số chu kì là điều hiển nhiên. Tính chất hoá học do electron lớp ngoài cùng quyết định, nên các nguyên tố cùng số electron ngoài (cùng nhóm A) có tính chất tương tự — đó chính là **định luật tuần hoàn**.

## Ví dụ vận dụng

Nguyên tố có cấu hình $1s^2 2s^2 2p^6 3s^2 3p^4$: có $Z=16$ (ô 16), lớp ngoài cùng là lớp 3 (chu kì 3), có $3s^2 3p^4$ tức 6 electron lớp ngoài (nhóm VIA). Đó là sulfur.

## Khối d và ngoại lệ

Nguyên tố nhóm B (khối $d$) xác định nhóm theo số electron hoá trị $(n-1)d + ns$, không dùng quy tắc nhóm A.

**Lỗi thường gặp:**
- Dùng quy tắc số thứ tự nhóm A cho nguyên tố khối $d$ — sai vì nguyên tố nhóm B xác định nhóm theo số electron hoá trị $(n-1)d\,ns$, không phải số electron lớp ngoài cùng.
- Đếm số lớp bằng số phân lớp — sai vì chu kì bằng số **lớp** (số $n$ lớn nhất), không phải số phân lớp $s,p,d$.
- Lấy nguyên tử khối làm số thứ tự ô — sai vì ô nguyên tố bằng $Z$ (số proton), không bằng khối lượng.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.bang-tuan-hoan-cau-tao`</sub>

---

### 2. Quy luật biến đổi tính chất trong chu kì và nhóm
*Periodic trends within periods and groups* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- So sánh được bán kính nguyên tử, độ âm điện, tính kim loại - phi kim theo chu kì và nhóm
- Giải thích được sự biến đổi tính axit - bazơ của oxit và hydroxide theo vị trí nguyên tố

## Một nguyên nhân, nhiều hệ quả

Gần như mọi xu hướng tuần hoàn đều bắt nguồn từ cuộc kéo co giữa **điện tích hạt nhân hiệu dụng $Z_{eff}$** (kéo electron vào) và **hiệu ứng chắn cùng số lớp** (đẩy electron ra).

## Trong một chu kì (trái $\to$ phải)

$Z$ tăng, electron thêm vào cùng lớp nên chắn không tăng mấy $\Rightarrow Z_{eff}$ tăng. Hệ quả:
- Bán kính **giảm**;
- Độ âm điện và năng lượng ion hoá **tăng**;
- Tính kim loại **giảm**, tính phi kim **tăng**.

## Trong một nhóm A (trên $\to$ dưới)

Thêm một lớp electron, electron ngoài xa hạt nhân và bị chắn mạnh $\Rightarrow$ lực hút yếu đi. Hệ quả:
- Bán kính **tăng**;
- Độ âm điện, năng lượng ion hoá **giảm**;
- Tính kim loại **tăng**.

## Hệ quả về oxit và hydroxide

Tính phi kim mạnh đi kèm oxit và hydroxide có tính **axit** mạnh; tính kim loại mạnh đi kèm oxit, hydroxide có tính **bazơ** mạnh. Vì thế trong một chu kì, đi sang phải oxit cao nhất chuyển dần từ bazơ (Na$_2$O) sang lưỡng tính (Al$_2$O$_3$) rồi sang axit (SO$_3$, Cl$_2$O$_7$).

## Khi nào dùng

Gặp câu so sánh bán kính, độ âm điện hay tính axit - bazơ: quy về vị trí trong bảng, rồi áp hai xu hướng trên. Chú ý ion: cùng số electron thì ion nào nhiều proton hơn sẽ nhỏ hơn.

**Lỗi thường gặp:**
- Cho rằng bán kính tăng sang phải trong chu kì — sai vì $Z_{eff}$ tăng làm electron bị kéo vào, bán kính giảm dần sang phải.
- So sánh độ âm điện chỉ theo khối lượng nguyên tử — sai vì độ âm điện phụ thuộc vị trí (chu kì, nhóm) và $Z_{eff}$, không phụ thuộc trực tiếp khối lượng.
- Kết luận oxit của mọi nguyên tố cùng chu kì đều cùng tính axit hay bazơ — sai vì tính axit - bazơ của oxit biến đổi dần theo tính kim loại - phi kim khi đi ngang chu kì.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.quy-luat-bien-doi-tuan-hoan`</sub>

---

## Chương 3: Liên kết hoá học

### 1. Độ âm điện và phân loại liên kết hoá học
*Electronegativity and classification of chemical bonds* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Vận dụng hiệu độ âm điện để phân loại liên kết cộng hoá trị không cực, có cực và liên kết ion
- Giải thích được sự hình thành liên kết theo quy tắc octet

## Liên kết là gì và vì sao hình thành

Nguyên tử liên kết để đạt cấu hình bền của khí hiếm (**quy tắc octet**, 8 electron lớp ngoài, riêng H và Li hướng tới 2). Cách đạt octet quyết định loại liên kết.

## Thang phân loại theo hiệu độ âm điện

Đặt $\Delta\chi = |\chi_A - \chi_B|$ là hiệu độ âm điện hai nguyên tử. Quy ước phổ biến trong sách GDPT:

$$\begin{cases}\Delta\chi < 0{,}4: & \text{cộng hoá trị không cực}\\ 0{,}4 \le \Delta\chi < 1{,}7: & \text{cộng hoá trị có cực}\\ \Delta\chi \ge 1{,}7: & \text{liên kết ion}\end{cases}$$

Ý nghĩa: chênh lệch càng lớn thì cặp electron càng bị kéo lệch hẳn về nguyên tử âm điện hơn; khi lệch đủ mạnh, electron chuyển hẳn tạo ion.

## Đọc kĩ: phân loại chỉ là gần đúng

Ranh giới $1{,}7$ không tuyệt đối. HF có $\Delta\chi \approx 1{,}9$ nhưng vẫn được xem là cộng hoá trị phân cực mạnh (phân tử tồn tại độc lập). Vì thế cần kết hợp thêm bản chất nguyên tố: kim loại điển hình + phi kim điển hình mới cho ion thực sự.

## Cực của liên kết và của phân tử

Liên kết có cực chưa chắc làm phân tử phân cực. $\mathrm{CO_2}$ có hai liên kết C=O phân cực nhưng thẳng hàng, đối xứng nên mô men lưỡng cực triệt tiêu $\Rightarrow$ phân tử không cực. Đây là cầu nối sang bài hình học phân tử.

## Khi nào dùng

Đề cho giá trị độ âm điện và hỏi loại liên kết: tính $\Delta\chi$ rồi tra thang; đồng thời kiểm tra xem có phải kim loại + phi kim điển hình không.

**Lỗi thường gặp:**
- Kết luận cứ $\Delta\chi \ge 1{,}7$ là liên kết ion mà không xét bản chất nguyên tố — sai vì HF có $\Delta\chi\approx1{,}9$ vẫn là cộng hoá trị phân cực; ion thực sự cần kim loại điển hình kết hợp phi kim điển hình.
- Đồng nhất liên kết có cực với phân tử có cực — sai vì hình học đối xứng (như $\mathrm{CO_2}$) có thể triệt tiêu mô men lưỡng cực của các liên kết cực.
- Bỏ qua quy tắc octet khi lí giải liên kết — sai vì chính xu hướng đạt 8 electron lớp ngoài là động lực hình thành cả liên kết ion lẫn cộng hoá trị.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.do-am-dien-va-lien-ket`</sub>

---

### 2. Số oxi hoá và quy tắc xác định
*Oxidation number and rules for assigning it* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Xác định được số oxi hoá của nguyên tố trong phân tử và ion theo quy tắc
- Phân biệt được số oxi hoá với hoá trị và điện tích ion

## Số oxi hoá dùng để làm gì

Số oxi hoá là công cụ **kế toán electron**: nó cho biết một nguyên tử "giữ" nhiều hay ít electron hơn so với trạng thái tự do, nhờ đó nhận diện chất khử, chất oxi hoá và cân bằng phản ứng oxi hoá - khử.

## Bộ quy tắc theo thứ tự ưu tiên

1. Đơn chất: số oxi hoá $=0$ (ví dụ $\mathrm{O_2, Fe, Cl_2}$).
2. Ion đơn nguyên tử: số oxi hoá $=$ điện tích ion ($\mathrm{Na^+}$ là $+1$, $\mathrm{S^{2-}}$ là $-2$).
3. Trong hợp chất, thường: H là $+1$ (trừ hydride kim loại $-1$), O là $-2$ (trừ peroxide $-1$, $\mathrm{OF_2}$ là $+2$), kim loại kiềm $+1$, kiềm thổ $+2$, F luôn $-1$.
4. **Quy tắc chốt**: tổng số oxi hoá trong phân tử trung hoà $=0$; trong ion $=$ điện tích ion.

## Cách tính nhanh

Gán số oxi hoá cho các nguyên tố đã biết (H, O, kim loại...), đặt ẩn cho nguyên tố cần tìm rồi dùng quy tắc chốt để lập phương trình.

## Đừng nhầm ba khái niệm

- **Số oxi hoá** có dấu, tính theo quy ước ion; có thể là số âm, dương hoặc phân số trung bình (như C trong $\mathrm{C_3O_2}$).
- **Hoá trị** (cộng hoá trị) là số liên kết, không mang dấu.
- **Điện tích ion** là điện tích thực của tiểu phân.

Ví dụ trong $\mathrm{H_2O}$: O có số oxi hoá $-2$ nhưng cộng hoá trị là 2 (hai liên kết O-H).

## Khi nào dùng

Trước khi cân bằng phản ứng oxi hoá - khử hoặc gọi tên hợp chất theo hoá trị, luôn xác định số oxi hoá của nguyên tố trung tâm.

**Lỗi thường gặp:**
- Lấy tổng số oxi hoá trong ion bằng 0 — sai vì với ion, tổng phải bằng **điện tích ion**, chỉ phân tử trung hoà mới bằng 0.
- Cho O luôn là $-2$ trong mọi hợp chất — sai vì trong peroxide ($\mathrm{H_2O_2}$) O là $-1$ và trong $\mathrm{OF_2}$ O là $+2$.
- Nhầm số oxi hoá với hoá trị — sai vì số oxi hoá có dấu và tính theo quy ước ion, còn hoá trị (cộng hoá trị) là số liên kết không mang dấu.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.so-oxi-hoa`</sub>

---

### 3. Hình học phân tử: mô hình VSEPR và lai hoá orbital
*Molecular geometry: VSEPR model and orbital hybridisation* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · nang-cao

**Mục tiêu:**
- Dự đoán được dạng hình học của phân tử đơn giản bằng mô hình VSEPR
- Xác định được trạng thái lai hoá của nguyên tử trung tâm và liên hệ với hình học phân tử

## Vì sao phân tử có hình dạng xác định

Các cặp electron hoá trị quanh nguyên tử trung tâm mang điện âm nên **đẩy nhau**. Chúng tự sắp để tổng lực đẩy nhỏ nhất, tức nằm cách xa nhau nhất trong không gian. Đó là ý tưởng của mô hình **VSEPR**.

## Đếm miền electron

Đếm số **miền electron** quanh nguyên tử trung tâm = số nguyên tử liên kết + số cặp electron riêng (một liên kết đôi, ba vẫn tính là **một** miền vì cùng nằm một hướng):

$$\begin{array}{lll}\text{2 miền} & \to sp & \text{thẳng }180^\circ\\ \text{3 miền} & \to sp^2 & \text{tam giác phẳng }120^\circ\\ \text{4 miền} & \to sp^3 & \text{tứ diện }109{,}5^\circ\end{array}$$

## Cặp electron riêng bẻ cong góc

Cặp riêng đẩy mạnh hơn cặp liên kết nên ép các liên kết lại gần nhau. $\mathrm{CH_4}$ (4 cặp liên kết) là tứ diện đều $109{,}5^\circ$; $\mathrm{NH_3}$ (3 liên kết + 1 cặp riêng) là chóp tam giác, góc còn $107^\circ$; $\mathrm{H_2O}$ (2 liên kết + 2 cặp riêng) gấp khúc, góc còn $104{,}5^\circ$. Cả ba đều lai hoá $sp^3$ nhưng hình dạng khác nhau vì số cặp riêng khác nhau.

## Lai hoá giải thích điều VSEPR mô tả

Để tạo các liên kết hướng đúng theo hình học, nguyên tử trung tâm trộn orbital $s$ và $p$ thành orbital lai hoá tương đương. Số orbital lai hoá bằng số miền electron.

## Khi nào dùng

Muốn biết dạng phân tử hay góc liên kết: viết Lewis, đếm miền electron của nguyên tử trung tâm, suy ra lai hoá và hình dạng, cuối cùng chỉnh góc theo số cặp riêng.

**Lỗi thường gặp:**
- Tính mỗi liên kết đôi hay ba là hai, ba miền electron — sai vì các liên kết bội cùng nằm về một hướng nên chỉ tính **một** miền khi xác định hình học.
- Cho rằng $\mathrm{NH_3}$ và $\mathrm{H_2O}$ là tứ diện đều vì đều lai hoá $sp^3$ — sai vì cặp electron riêng chiếm chỗ và đẩy mạnh, làm phân tử thành chóp hoặc gấp khúc với góc nhỏ hơn $109{,}5^\circ$.
- Quên cặp electron riêng khi đếm miền — dẫn đến dự đoán sai lai hoá và góc liên kết.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.vsepr-lai-hoa`</sub>

---

## Chương 4: Phản ứng oxi hoá - khử

### 1. Phản ứng oxi hoá - khử và phương pháp thăng bằng electron
*Redox reactions and the electron-balance method* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được chất oxi hoá, chất khử, quá trình oxi hoá và quá trình khử dựa vào sự thay đổi số oxi hoá
- Cân bằng được phương trình phản ứng oxi hoá - khử bằng phương pháp thăng bằng electron

## Bản chất của phản ứng oxi hoá - khử

Đây là phản ứng có **sự chuyển electron**, biểu hiện qua thay đổi số oxi hoá. Chất **khử** nhường electron (số oxi hoá tăng), chất **oxi hoá** nhận electron (số oxi hoá giảm). Mẹo nhớ: "khử cho, o nhận" — chất khử cho electron, chất oxi hoá nhận.

## Định luật nền tảng: bảo toàn electron

Electron không tự sinh ra hay mất đi, nên:

$$\sum n_{e}\,(\text{cho}) = \sum n_{e}\,(\text{nhận})$$

Đây vừa là nguyên tắc cân bằng, vừa là công cụ giải nhanh mọi bài toán oxi hoá - khử.

## Bốn bước thăng bằng electron

1. Xác định số oxi hoá, tìm nguyên tố thay đổi.
2. Viết quá trình oxi hoá và quá trình khử, ghi số electron trao đổi.
3. Tìm hệ số sao cho electron cho $=$ electron nhận (nhân chéo, lấy bội chung).
4. Đặt hệ số vào phương trình phân tử, cân bằng các nguyên tố còn lại (thường theo thứ tự: kim loại, phi kim, H, kiểm tra O).

## Ví dụ mạch tư duy

Với $\mathrm{Cu + HNO_3 \to Cu(NO_3)_2 + NO + H_2O}$: Cu từ $0 \to +2$ (cho 2e), N từ $+5 \to +2$ (nhận 3e). Bội chung của 2 và 3 là 6 nên $\times3$ cho Cu, $\times2$ cho N: $3\mathrm{Cu} + 8\mathrm{HNO_3} \to 3\mathrm{Cu(NO_3)_2} + 2\mathrm{NO} + 4\mathrm{H_2O}$.

## Khi nào dùng

Bài định lượng kim loại tác dụng axit, điện phân, nhiệt luyện... đều quy về bảo toàn electron mà không cần viết đủ phương trình.

**Lỗi thường gặp:**
- Nhầm chất khử với chất oxi hoá — sai vì chất khử là chất **cho** electron (số oxi hoá tăng), dễ lẫn với tên gọi.
- Chỉ cân bằng số nguyên tử mà quên cân bằng electron cho - nhận — dẫn đến hệ số sai với phản ứng oxi hoá - khử phức tạp.
- Bỏ sót $\mathrm{HNO_3}$ đóng vai trò môi trường (tạo muối nitrat) khi đếm hệ số axit — làm sai số mol axit phản ứng.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.oxi-hoa-khu-thang-bang-electron`</sub>

---

## Chương 5: Năng lượng hoá học

### 1. Biến thiên enthalpy của phản ứng theo nhiệt tạo thành
*Reaction enthalpy from standard enthalpies of formation* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Nêu được ý nghĩa của biến thiên enthalpy chuẩn và dấu của nó với phản ứng thu, toả nhiệt
- Tính được biến thiên enthalpy của phản ứng từ nhiệt tạo thành chuẩn của các chất

## Phản ứng kèm theo trao đổi nhiệt

Mọi phản ứng đều kèm hấp thụ hoặc giải phóng năng lượng. Ở áp suất không đổi, nhiệt đó chính là **biến thiên enthalpy** $\Delta_r H^\circ_{298}$. Quy ước dấu:
- $\Delta_r H < 0$: phản ứng **toả nhiệt** (giải phóng năng lượng);
- $\Delta_r H > 0$: phản ứng **thu nhiệt**.

## Nhiệt tạo thành chuẩn — điểm mốc chung

Để so sánh, ta chọn mốc: **nhiệt tạo thành chuẩn** $\Delta_f H^\circ$ là nhiệt khi tạo 1 mol chất từ các đơn chất ở dạng bền nhất, tại điều kiện chuẩn (298 K, 1 bar). Đơn chất bền (như $\mathrm{O_2, N_2, C\,(graphite)}$) có $\Delta_f H^\circ = 0$.

## Công thức tính enthalpy phản ứng

Vì enthalpy là hàm trạng thái, ta lấy "sản phẩm trừ chất đầu":

$$\Delta_r H^\circ = \sum \Delta_f H^\circ_{\text{sản phẩm}} - \sum \Delta_f H^\circ_{\text{chất đầu}}$$

nhớ nhân với hệ số tỉ lượng của mỗi chất trong phương trình.

## Đọc kĩ trạng thái chất

Phải dùng đúng $\Delta_f H^\circ$ theo **trạng thái** ghi trong phương trình. Nước lỏng và hơi nước có nhiệt tạo thành khác nhau ($-285{,}8$ so với $-241{,}8$ kJ/mol); dùng nhầm sẽ lệch kết quả hàng chục kJ.

## Khi nào dùng

Đề cho bảng $\Delta_f H^\circ$ các chất và yêu cầu tính nhiệt phản ứng: áp thẳng công thức "sản phẩm trừ chất đầu", chú ý hệ số và trạng thái.

**Lỗi thường gặp:**
- Lấy "chất đầu trừ sản phẩm" — sai dấu vì công thức đúng là tổng nhiệt tạo thành sản phẩm trừ tổng của chất đầu.
- Dùng nhiệt tạo thành của nước lỏng khi phương trình ghi hơi nước (hoặc ngược lại) — sai vì $\Delta_f H^\circ$ phụ thuộc trạng thái, chênh nhau khoảng $44$ kJ/mol.
- Quên nhân hệ số tỉ lượng vào nhiệt tạo thành mỗi chất — làm sai tổng năng lượng.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.enthalpy-nhiet-tao-thanh`</sub>

---

### 2. Tính enthalpy theo năng lượng liên kết và định luật Hess
*Reaction enthalpy from bond energies and Hess's law* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được biến thiên enthalpy của phản ứng ở thể khí từ năng lượng liên kết
- Vận dụng định luật Hess để tính enthalpy của phản ứng qua các phản ứng trung gian

## Cách nhìn thứ hai: phá và tạo liên kết

Phản ứng thực chất là **phá liên kết cũ** (tốn năng lượng, thu nhiệt) rồi **tạo liên kết mới** (giải phóng năng lượng, toả nhiệt). Với phản ứng ở thể khí, khi biết năng lượng liên kết $E_b$:

$$\Delta_r H^\circ = \sum E_b(\text{liên kết bị phá}) - \sum E_b(\text{liên kết tạo thành})$$

Hãy nhớ chiều: **phá trừ tạo** (ngược với công thức nhiệt tạo thành là "sản phẩm trừ chất đầu"). Công thức này chỉ dùng cho chất khí vì năng lượng liên kết định nghĩa ở thể khí.

## Định luật Hess: đi vòng vẫn tới đích

Vì enthalpy là hàm trạng thái, ta có thể cộng đại số các phản ứng trung gian để suy ra phản ứng đích. Quy tắc thao tác:
- Đảo chiều một phản ứng $\Rightarrow$ đổi dấu $\Delta H$;
- Nhân một phản ứng với hệ số $k$ $\Rightarrow$ nhân $\Delta H$ với $k$;
- Cộng các phản ứng lại $\Rightarrow$ cộng các $\Delta H$.

## Vì sao Hess hữu ích

Nhiều phản ứng khó đo nhiệt trực tiếp (ví dụ $\mathrm{C + \tfrac12 O_2 \to CO}$ luôn kèm tạo $\mathrm{CO_2}$). Hess cho phép tính gián tiếp qua các phản ứng đo được.

## Khi nào dùng cái nào

- Có bảng $\Delta_f H^\circ$: dùng công thức nhiệt tạo thành.
- Có bảng năng lượng liên kết và mọi chất là khí: dùng công thức năng lượng liên kết.
- Cho vài phản ứng trung gian: ghép Hess.

**Lỗi thường gặp:**
- Dùng công thức "tạo trừ phá" cho năng lượng liên kết — sai vì với năng lượng liên kết là **phá trừ tạo** (ngược chiều so với công thức nhiệt tạo thành).
- Dùng năng lượng liên kết cho phản ứng có chất lỏng hoặc rắn — sai vì năng lượng liên kết chỉ định nghĩa cho liên kết ở thể khí.
- Khi ghép Hess, đảo chiều phản ứng mà quên đổi dấu $\Delta H$ — làm sai toàn bộ tổng đại số.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.enthalpy-nang-luong-lien-ket-hess`</sub>

---

## Chương 6: Kim loại và Hợp chất vô cơ

### 10. Phương pháp xác định công thức chất vô cơ, Oxit kim loại và Muối ngậm nước
*Methods for determining inorganic formulas: Metal oxides and hydrated salts* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Thiết lập công thức oxit kim loại MxOy dựa trên thành phần phần trăm khối lượng và phản ứng khử
- Xác định kim loại chưa biết thông qua khối lượng mol tương đương và hoá trị
- Tìm số phân tử nước kết tinh trong muối ngậm nước qua phương pháp nung

## Xác định kim loại chưa biết

Cho $m$ gam kim loại $M$ hoá trị $n$ tác dụng với axit hoặc phi kim. Số mol kim loại liên hệ với số mol electron trao đổi:

$$n_M = \frac{m}{M_M} = \frac{n_e}{n} \Rightarrow M_M = \frac{m \cdot n}{n_e}$$

Lập bảng biện luận theo hoá trị thông thường $n \in \{1, 2, 3\}$ để tìm kim loại phù hợp.

## Xác định oxit kim loại và muối ngậm nước

- Oxit kim loại $M_xO_y$: Tìm tỉ lệ $x : y = \frac{\%m_M}{M_M} : \frac{\%m_O}{16}$.
- Muối ngậm nước $A \cdot n H_2O$: Khi nung nóng, nước bay hơi hoàn toàn. Số phân tử nước $n = \frac{n_{H_2O}}{n_{muối\ khan}} = \frac{m_{giảm} / 18}{m_{rắn\ sau} / M_{muối\ khan}}$.

**Lỗi thường gặp:**
- Quên biện luận hoá trị n của kim loại chuyển tiếp (ví dụ Fe có thể có hoá trị 2 hoặc 3)
- Lấy khối lượng muối ngậm nước ban đầu chia trực tiếp cho khối lượng mol muối khan

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.xac-dinh-cong-thuc-chat-vo-co`</sub>

---

## Chương 6: Tốc độ phản ứng hoá học

### 1. Tốc độ phản ứng và các yếu tố ảnh hưởng
*Reaction rate and factors affecting it* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Viết được biểu thức tốc độ trung bình theo một chất và giải thích ý nghĩa hệ số tỉ lượng
- Giải thích được ảnh hưởng của nồng độ, nhiệt độ, diện tích bề mặt và chất xúc tác đến tốc độ phản ứng

## Đo tốc độ như thế nào

Tốc độ phản ứng cho biết phản ứng xảy ra **nhanh hay chậm**, đo bằng độ biến thiên nồng độ theo thời gian. Với phản ứng $aA + bB \to cC + dD$, tốc độ trung bình tính theo bất kì chất nào cũng cho cùng một giá trị nếu chia cho hệ số:

$$\bar v = -\frac{1}{a}\frac{\Delta[A]}{\Delta t} = \frac{1}{c}\frac{\Delta[C]}{\Delta t}$$

Dấu trừ cho chất phản ứng vì nồng độ của chúng giảm dần.

## Bốn yếu tố điều khiển

- **Nồng độ** tăng $\Rightarrow$ số va chạm hiệu quả tăng $\Rightarrow$ tốc độ tăng.
- **Nhiệt độ** tăng $\Rightarrow$ nhiều phân tử vượt năng lượng hoạt hoá $\Rightarrow$ tốc độ tăng mạnh. Định luật kinh nghiệm Van't Hoff: tăng $10^\circ\mathrm{C}$, tốc độ tăng $\gamma$ lần.
- **Diện tích bề mặt** chất rắn tăng (nghiền nhỏ) $\Rightarrow$ tăng tiếp xúc $\Rightarrow$ tốc độ tăng.
- **Chất xúc tác** hạ năng lượng hoạt hoá $\Rightarrow$ tăng tốc độ mà không bị tiêu hao.

## Công thức Van't Hoff định lượng

Khi nhiệt độ tăng từ $T_1$ lên $T_2$:

$$\frac{v_2}{v_1} = \gamma^{\frac{T_2 - T_1}{10}}$$

Vì tốc độ tỉ lệ nghịch với thời gian phản ứng, ta cũng có $t_1/t_2 = \gamma^{(T_2-T_1)/10}$.

## Khi nào dùng

Bài cho $\gamma$ và hỏi tốc độ (hoặc thời gian) thay đổi bao nhiêu lần khi đổi nhiệt độ: tính số nấc $10^\circ$ rồi luỹ thừa $\gamma$.

**Lỗi thường gặp:**
- Cộng thay vì luỹ thừa $\gamma$ theo số nấc nhiệt độ — sai vì mỗi nấc $10^\circ$ **nhân** thêm $\gamma$, cho quan hệ luỹ thừa chứ không cộng.
- Quên chia cho hệ số tỉ lượng khi so sánh tốc độ tính theo các chất khác nhau — dẫn đến giá trị tốc độ không thống nhất.
- Cho rằng chất xúc tác làm dịch chuyển cân bằng hoặc bị tiêu hao — sai vì xúc tác chỉ tăng tốc độ đạt cân bằng, không đổi vị trí cân bằng và được hoàn nguyên.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.toc-do-phan-ung`</sub>

---

## Chương: Carbohydrate

### 1. Glucose, fructose và saccharose
*Glucose, fructose and sucrose* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Viết được phản ứng tráng bạc, cộng H2 và phản ứng lên men của glucose
- So sánh được tính chất của glucose (có nhóm –CHO) và fructose, saccharose
- Tính được lượng sản phẩm trong phản ứng lên men rượu và thủy phân saccharose theo hiệu suất

Glucose là carbohydrate quan trọng nhất, mang đồng thời tính chất của polyalcohol (5 nhóm –OH) và của aldehyde (1 nhóm –CHO). Chính nhóm –CHO tạo nên các phản ứng nhận biết đặc trưng.

**Tính chất của nhóm –CHO.** Glucose tráng bạc (cho 2 Ag trên 1 phân tử) và bị khử bởi H2 tạo sorbitol:
$$C_6H_{12}O_6+2AgNO_3+...\rightarrow ...+2Ag\downarrow$$
Fructose không có –CHO nhưng trong môi trường base (NH3) chuyển hóa thành glucose nên **cũng tráng bạc** — một điểm dễ nhầm.

**Lên men rượu.** $C_6H_{12}O_6\xrightarrow{enzyme}2C_2H_5OH+2CO_2$. Mỗi mol glucose cho 2 mol ethanol và 2 mol CO2; nhân hiệu suất H để ra lượng thực tế.

**Saccharose** $C_{12}H_{22}O_{11}$ là disaccharide, không có nhóm –CHO tự do nên **không tráng bạc**. Khi thủy phân tạo glucose và fructose:
$$C_{12}H_{22}O_{11}+H_2O\rightarrow C_6H_{12}O_6(glucose)+C_6H_{12}O_6(fructose)$$

Khi nào dùng gì? Phân biệt saccharose (không tráng bạc) với glucose/fructose (tráng bạc); bài lên men dùng tỉ lệ 1 glucose → 2 ethanol → 2 CO2 kèm hiệu suất.

**Lỗi thường gặp:**
- Cho rằng saccharose tráng bạc được: saccharose không có nhóm –CHO tự do nên không tráng bạc; chỉ sản phẩm thủy phân (glucose, fructose) mới phản ứng.
- Nghĩ fructose không tráng bạc vì là ketone: trong môi trường base của thuốc thử Tollens, fructose chuyển thành glucose nên vẫn cho phản ứng tráng bạc.
- Quên nhân hệ số 2 khi tính ethanol/CO2 từ glucose, hoặc quên nhân hiệu suất — cả hai đều làm sai lượng sản phẩm.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.glucose-saccharose`</sub>

---

### 2. Tinh bột và cellulose (xenlulozơ)
*Starch and cellulose* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- So sánh được cấu tạo và tính chất của tinh bột và cellulose (cùng công thức (C6H10O5)n)
- Tính được số mắt xích và lượng glucose tạo thành khi thủy phân polysaccharide
- Vận dụng phản ứng của cellulose với HNO3 để tính lượng cellulose trinitrate

Tinh bột và cellulose cùng công thức $(C_6H_{10}O_5)_n$ nhưng vai trò sinh học và tính chất khác hẳn nhau — tinh bột là chất dự trữ, cellulose là chất tạo khung thực vật. Điểm chung: đều là polymer của glucose và đều thủy phân được.

**Thủy phân.** Cả hai bị thủy phân (acid hoặc enzyme) đến cùng cho glucose:
$$(C_6H_{10}O_5)_n+nH_2O\rightarrow nC_6H_{12}O_6$$
Mỗi mắt xích $C_6H_{10}O_5$ (M = 162) tạo 1 phân tử glucose (M = 180). Số mắt xích $n=\dfrac{M_{polymer}}{162}$.

**Nhận biết.** Tinh bột tạo màu xanh tím với iodine — phản ứng đặc trưng để nhận biết hồ tinh bột.

**Cellulose và HNO3.** Mỗi mắt xích cellulose có 3 nhóm –OH, ester hóa với HNO3 đặc tạo cellulose trinitrate:
$$[C_6H_7O_2(OH)_3]_n+3nHNO_3\rightarrow [C_6H_7O_2(ONO_2)_3]_n+3nH_2O$$
Mỗi mắt xích trinitrate có M = 297; đây là cơ sở tính lượng cellulose và HNO3.

Khi nào dùng gì? Nhận biết tinh bột bằng iodine; bài thủy phân dùng tỉ lệ 162 → 180 kèm hiệu suất; bài điều chế thuốc súng dùng tỉ lệ 162 (mắt xích) ↔ 297 (trinitrate) ↔ 3 HNO3.

**Lỗi thường gặp:**
- Cho rằng tinh bột và cellulose khác công thức phân tử: cả hai đều là (C6H10O5)n; chúng chỉ khác kiểu liên kết glycoside và cấu trúc mạch.
- Dùng khối lượng mắt xích cellulose là 180 (như glucose): mắt xích trong polymer là C6H10O5 (M = 162), đã mất một phân tử nước khi trùng ngưng.
- Chỉ dùng 1 nhóm –OH của cellulose khi phản ứng HNO3: mỗi mắt xích có 3 nhóm –OH nên tạo trinitrate và cần 3 HNO3 — thiếu sẽ sai tỉ lệ.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.tinh-bot-xenlulozo`</sub>

---

## Chương: Dẫn xuất halogen – Alcohol – Phenol

### 1. Alcohol: phản ứng đặc trưng của nhóm –OH
*Alcohols: characteristic reactions of the hydroxyl group* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Viết được phản ứng của alcohol với Na, phản ứng tách nước tạo alkene và ether, phản ứng oxi hóa bởi CuO
- Xác định được số nhóm –OH qua phản ứng với Na dựa vào tỉ lệ mol H2
- Phân biệt được sản phẩm oxi hóa của alcohol bậc I (aldehyde) và bậc II (ketone)

Nhóm –OH là trung tâm phản ứng của alcohol. Ba phản ứng đặc trưng — với kim loại kiềm, tách nước, và oxi hóa — vừa dùng để định lượng, vừa để phân biệt bậc alcohol.

**Tác dụng với Na.** Nguyên tử H của –OH linh động, bị Na thay thế giải phóng H2:
$$2R(OH)_a+2aNa\rightarrow 2R(ONa)_a+aH_2$$
Suy ra $n_{H_2}=\tfrac{a}{2}n_{alcohol}$ (a là số nhóm –OH). Dùng tỉ lệ $n_{H_2}/n_{alcohol}$ để tìm số nhóm –OH.

**Tách nước.** Xúc tác $H_2SO_4$ đặc: ở $170^\circ C$ tạo alkene ($C_2H_5OH\rightarrow C_2H_4+H_2O$); ở $140^\circ C$ tạo ether ($2C_2H_5OH\rightarrow (C_2H_5)_2O+H_2O$).

**Oxi hóa bởi CuO (hoặc $O_2$/xúc tác).** Alcohol bậc I $\rightarrow$ aldehyde; bậc II $\rightarrow$ ketone; bậc III không bị oxi hóa kiểu này:
$$R\text{-}CH_2OH+CuO\xrightarrow{t^\circ}R\text{-}CHO+Cu+H_2O$$
Khối lượng chất rắn giảm đúng bằng khối lượng oxygen tách ra (CuO → Cu).

Khi nào dùng gì? Xác định số –OH dùng phản ứng Na; phân biệt bậc alcohol dùng oxi hóa CuO rồi thử sản phẩm (aldehyde tráng bạc, ketone thì không).

**Lỗi thường gặp:**
- Cho rằng mỗi mol alcohol luôn cho ½ mol H2 với Na: chỉ đúng cho alcohol đơn chức; alcohol đa chức (glycerol 3 OH) cho nhiều H2 hơn theo số nhóm –OH.
- Cho rằng alcohol bậc III bị oxi hóa bởi CuO thành ketone: alcohol bậc III không có H trên carbon mang –OH nên không bị oxi hóa kiểu này.
- Dùng 22,4 L/mol để tính thể tích khí ở đkc theo GDPT 2018: điều kiện chuẩn hiện hành là 25 °C, 1 bar với thể tích mol 24,79 L/mol.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.alcohol`</sub>

---

### 2. Phenol: tính acid yếu và phản ứng thế vòng thơm
*Phenol: weak acidity and aromatic substitution* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao phenol có tính acid yếu (tác dụng cả Na và NaOH) trong khi alcohol không tác dụng NaOH
- Viết được phản ứng thế bromine vào vòng benzene của phenol tạo kết tủa trắng
- So sánh được ảnh hưởng qua lại giữa nhóm –OH và vòng benzene trong phân tử phenol

Vì sao phenol $C_6H_5OH$ tác dụng được với dung dịch NaOH còn ethanol thì không, dù cả hai đều có nhóm –OH? Câu trả lời nằm ở **ảnh hưởng qua lại** giữa vòng benzene và nhóm –OH.

**Tính acid yếu.** Vòng thơm hút electron làm liên kết O–H phân cực mạnh, H dễ tách ra. Phenol vừa tác dụng Na (như mọi –OH) vừa tác dụng base:
$$C_6H_5OH+NaOH\rightarrow C_6H_5ONa+H_2O$$
Tuy vậy tính acid rất yếu: phenol không làm đổi màu quỳ tím và bị $CO_2$ đẩy ra khỏi muối phenolate ($C_6H_5ONa+CO_2+H_2O\rightarrow C_6H_5OH+NaHCO_3$).

**Thế dễ vào vòng.** Ngược lại, –OH đẩy electron làm vòng benzene của phenol hoạt động hơn benzene: phenol phản ứng ngay với nước bromine tạo kết tủa trắng 2,4,6-tribromophenol:
$$C_6H_5OH+3Br_2\rightarrow C_6H_2Br_3OH\downarrow+3HBr$$
Đây là phản ứng nhận biết phenol (benzene không phản ứng).

Khi nào dùng gì? Phân biệt phenol với alcohol bằng NaOH (phenol tan tạo muối); nhận biết phenol bằng nước bromine cho kết tủa trắng.

**Lỗi thường gặp:**
- Cho rằng alcohol cũng tác dụng với NaOH như phenol: alcohol có tính acid yếu hơn nước, không phản ứng với NaOH; chỉ phenol mới tạo muối phenolate.
- Kết luận phenol có tính acid mạnh vì tác dụng NaOH: tính acid của phenol rất yếu (yếu hơn carbonic acid), không làm đổi màu quỳ và bị CO2 đẩy ra khỏi muối.
- Cho rằng phenol chỉ thế 1 Br như benzene: nhóm –OH hoạt hóa mạnh vòng, phenol thế đồng thời 3 vị trí (2,4,6) tạo kết tủa tribromo — tính thiếu Br làm sai khối lượng.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.phenol`</sub>

---

## Chương: Ester – Lipid

### 1. Ester: thủy phân và xà phòng hóa
*Esters: hydrolysis and saponification* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Viết được phản ứng thủy phân ester trong môi trường acid (thuận nghịch) và base (xà phòng hóa, một chiều)
- Vận dụng bảo toàn khối lượng cho phản ứng ester với NaOH để tính khối lượng muối
- Xác định được công thức ester dựa vào tỉ lệ mol ester và NaOH

Ester là dẫn xuất của acid, có mặt trong hương liệu, chất béo và nhiều vật liệu. Phản ứng quan trọng nhất của ester là thủy phân, và cách nó xảy ra khác nhau rõ rệt giữa môi trường acid và base.

**Thủy phân trong acid.** Thuận nghịch, là phản ứng ngược của ester hóa:
$$R\text{-}COOR'+H_2O\rightleftharpoons R\text{-}COOH+R'OH$$

**Xà phòng hóa (trong base).** Một chiều, hoàn toàn:
$$R\text{-}COOR'+NaOH\rightarrow R\text{-}COONa+R'OH$$
Với ester đơn chức: $n_{NaOH}=n_{ester}$. Đây là mấu chốt giải nhanh: đếm số nhóm chức ester bằng tỉ lệ mol NaOH phản ứng.

**Bảo toàn khối lượng.** Áp dụng cho phản ứng xà phòng hóa:
$$m_{ester}+40n_{NaOH}=m_{muối}+m_{alcohol}$$
Nếu NaOH lấy dư, khi cô cạn phần rắn gồm cả muối và **NaOH dư** — đây là bẫy phổ biến.

Khi nào dùng gì? Cho khối lượng ester và lượng NaOH → dùng bảo toàn khối lượng và tỉ lệ mol để tìm muối/alcohol. Luôn kiểm tra NaOH dư trước khi tính khối lượng chất rắn khan.

**Lỗi thường gặp:**
- Quên NaOH dư khi cô cạn: nếu NaOH lấy dư, chất rắn khan gồm cả muối và NaOH dư; chỉ tính muối sẽ thiếu khối lượng.
- Tính cả ethanol vào chất rắn khan: alcohol dễ bay hơi nên không còn trong phần rắn sau khi cô cạn — cộng nhầm alcohol làm dư khối lượng.
- Coi thủy phân trong acid là một chiều như xà phòng hóa: thủy phân acid là thuận nghịch (hiệu suất < 100%), chỉ phản ứng với kiềm mới hoàn toàn.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.ester`</sub>

---

### 2. Chất béo (lipid) và các chỉ số đặc trưng
*Fats and their characteristic indices* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Trình bày được cấu tạo triglyceride và phản ứng thủy phân, xà phòng hóa, hydrogen hóa chất béo
- Tính được chỉ số acid, chỉ số xà phòng hóa và chỉ số iodine của chất béo
- Giải thích được ý nghĩa của các chỉ số trong đánh giá chất lượng dầu mỡ

Chất béo là trieste của glycerol với acid béo. Trong công nghiệp thực phẩm, người ta đánh giá chất béo qua ba con số: chỉ số acid, chỉ số xà phòng hóa và chỉ số iodine. Hiểu định nghĩa của chúng là hiểu bản chất phản ứng của –COOH, –COO– và C=C.

**Phản ứng.** Thủy phân/xà phòng hóa cho glycerol và acid béo (hoặc muối):
$$(RCOO)_3C_3H_5+3NaOH\rightarrow 3RCOONa+C_3H_5(OH)_3$$
Mỗi mol chất béo cần 3 mol NaOH và tạo 1 mol glycerol. Hydrogen hóa biến chất béo lỏng thành rắn (cộng H2 vào C=C).

**Các chỉ số** (đơn vị mg KOH hoặc g I2 trên mỗi gam/100 gam):
- Chỉ số acid $A=\dfrac{m_{KOH}(mg)}{m_{béo}(g)}$: đo lượng acid béo tự do.
- Chỉ số xà phòng hóa $S$: KOH để trung hòa acid tự do **và** thủy phân ester; $S=A+E$ với $E$ là chỉ số ester.
- Chỉ số iodine $I=\dfrac{254\,n_{I_2}}{m_{béo}}\times100$: đo độ không no.

Khi nào dùng gì? Chất béo càng ôi (nhiều acid tự do) thì chỉ số acid càng cao; chất béo càng lỏng (nhiều nối đôi) thì chỉ số iodine càng lớn. Bài toán thường quy về $n_{KOH}$ hoặc $n_{I_2}$ rồi chia cho khối lượng mẫu.

**Lỗi thường gặp:**
- Nhầm chỉ số acid với chỉ số xà phòng hóa: chỉ số acid chỉ tính KOH trung hòa acid béo tự do, còn chỉ số xà phòng hóa tính cả KOH thủy phân ester.
- Quên đổi khối lượng KOH sang miligam khi tính chỉ số: các chỉ số dùng đơn vị mg KOH trên gam chất béo, để nguyên gam sẽ nhỏ hơn 1000 lần.
- Cho rằng mỗi mol chất béo cần 1 mol NaOH/KOH: triglyceride có 3 nhóm ester nên cần 3 mol kiềm cho mỗi mol chất béo.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.chat-beo`</sub>

---

## Chương: Hydrocarbon

### 1. Alkane: tính chất và phản ứng đặc trưng
*Alkanes: properties and characteristic reactions* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Viết được công thức tổng quát và gọi tên alkane, xác định số đồng phân
- Trình bày được ba phản ứng đặc trưng: thế halogen, cracking, đốt cháy
- Giải được bài toán cracking và đốt cháy alkane bằng bảo toàn khối lượng

Alkane là hydrocarbon no, xương sống của dầu mỏ và khí thiên nhiên. Vì chỉ chứa liên kết đơn bền nên alkane khá trơ; phản ứng của chúng chủ yếu là thế, cắt mạch và oxi hóa.

**Phản ứng thế halogen.** Dưới ánh sáng, alkane thế nguyên tử H bởi halogen theo cơ chế gốc: $CH_4+Cl_2\xrightarrow{as}CH_3Cl+HCl$. Ưu tiên thế ở carbon bậc cao hơn.

**Cracking.** Alkane lớn bị bẻ mạch: $C_4H_{10}\rightarrow CH_4+C_3H_6$ hoặc $C_2H_6+C_2H_4$. Mỗi phân tử bị cracking cho 2 phân tử, nên **số mol khí tăng** nhưng **khối lượng không đổi** (bảo toàn khối lượng). Đây là chìa khóa giải nhanh: $\bar M$ hỗn hợp sau giảm, và $n_{sau}=n_{trước}\cdot(1+\text{độ cracking})$.

**Đốt cháy.** Vì no nên $n_{H_2O}>n_{CO_2}$ và đặc biệt:
$$n_{alkane}=n_{H_2O}-n_{CO_2}$$
$$n_{O_2}=n_{CO_2}+\tfrac{1}{2}n_{H_2O}$$
Khi nào dùng? Bài cracking dùng bảo toàn khối lượng cùng $\bar M$; bài đốt cháy alkane dùng ngay hệ thức $n_{alkane}=n_{H_2O}-n_{CO_2}$ để tìm số mol mà không cần cân bằng phương trình.

**Lỗi thường gặp:**
- Nghĩ cracking làm thay đổi khối lượng hỗn hợp: sai, cracking chỉ bẻ mạch nên tổng khối lượng khí trước và sau bằng nhau — phải dùng bảo toàn khối lượng.
- Quên rằng mỗi phân tử bị cracking sinh ra 2 phân tử nên số mol tăng: nếu giữ nguyên số mol sẽ tính sai khối lượng mol trung bình.
- Áp hệ thức n(alkane) = n(H2O) − n(CO2) cho hydrocarbon không no: sai vì hệ thức này chỉ đúng khi k = 0 (chất no mạch hở).

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.alkane`</sub>

---

### 2. Alkene: phản ứng cộng và trùng hợp
*Alkenes: addition and polymerization* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Viết được phản ứng cộng H2, cộng Br2, cộng HX (quy tắc Markovnikov) của alkene
- Tính được số mol liên kết pi qua phản ứng cộng Br2 hoặc H2
- Giải được bài toán hỗn hợp alkene và H2 dựa vào độ giảm số mol khí

Khác với alkane trơ, alkene có liên kết pi kém bền — đây là trung tâm phản ứng khiến alkene rất hoạt động. Toàn bộ hóa học của alkene xoay quanh phản ứng cộng vào nối đôi.

**Cộng hydrogen và halogen.** Mỗi liên kết pi cộng đúng 1 phân tử: $C_nH_{2n}+H_2\xrightarrow{Ni}C_nH_{2n+2}$ và $C_nH_{2n}+Br_2\rightarrow C_nH_{2n}Br_2$. Phản ứng với dung dịch $Br_2$ làm mất màu nâu đỏ — dấu hiệu nhận biết nối đôi. Suy ra: $n_{\pi}=n_{Br_2}=n_{H_2\,\text{cộng}}$.

**Cộng HX và nước.** Theo quy tắc Markovnikov, H cộng vào carbon đã có nhiều H hơn, X (hoặc OH) vào carbon còn lại, tạo sản phẩm chính.

**Trùng hợp.** $n\,CH_2=CH_2\rightarrow (-CH_2-CH_2-)_n$ tạo polyethylene.

**Giải nhanh hỗn hợp alkene + H2 qua Ni.** Khi cộng, số mol khí giảm đúng bằng số mol H2 phản ứng: $n_{giảm}=n_{H_2\,pư}$. Vì khối lượng bảo toàn, $\bar M$ tăng. Khi nào dùng? Bài cho tỉ khối hỗn hợp trước và sau phản ứng — lập bảo toàn khối lượng để tìm số mol, rồi suy hiệu suất.

**Lỗi thường gặp:**
- Cho rằng cộng Br2 hay H2 làm thay đổi khối lượng hỗn hợp khí theo cách khác bảo toàn: khối lượng luôn được bảo toàn, chỉ số mol khí giảm bằng số mol H2 phản ứng.
- Nhầm 1 mol alkene chỉ cộng 1 mol Br2 với alkyne cộng 2 mol: alkene (1 pi) cộng 1 Br2, alkyne (2 pi) cộng 2 Br2 — dùng sai làm lệch số mol liên kết pi.
- Áp quy tắc Markovnikov ngược: H phải cộng vào carbon nối đôi đã nhiều H hơn; cộng nhầm cho ra sản phẩm phụ thay vì sản phẩm chính.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.alkene`</sub>

---

### 3. Alkyne: phản ứng cộng và phản ứng thế ion kim loại
*Alkynes: addition and terminal-alkyne substitution* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Viết được phản ứng cộng H2, Br2 (theo hai nấc) và phản ứng thế của ank-1-yne với AgNO3/NH3
- Sử dụng phản ứng với AgNO3/NH3 để nhận biết và định lượng ank-1-yne
- Vận dụng bảo toàn liên kết pi cho hỗn hợp hydrocarbon không no cộng H2/Br2

Alkyne có liên kết ba — hai liên kết pi — nên hoạt động hơn cả alkene, cộng được **hai nấc**. Nhưng nét độc đáo nhất của ank-1-yne là phản ứng thế nguyên tử H đầu mạch, dùng để nhận biết.

**Cộng H2, Br2 (hai nấc).** $C_nH_{2n-2}+2H_2\xrightarrow{Ni}C_nH_{2n+2}$; với Br2 tương tự cộng 2 mol. Do đó với alkyne: $n_{\pi}=2n_{alkyne}$.

**Phản ứng thế của ank-1-yne với AgNO3/NH3.** H đầu mạch bị thay bởi Ag tạo kết tủa vàng nhạt:
$$R\text{-}C\equiv CH+AgNO_3+NH_3\rightarrow R\text{-}C\equiv CAg\downarrow+NH_4NO_3$$
Riêng acetylene $HC\equiv CH$ có hai H đầu mạch nên tạo $Ag_2C_2$ (dùng 2 AgNO3). Phản ứng này phân biệt ank-1-yne (có kết tủa) với alkyne trong mạch (không kết tủa) và với alkene/alkane.

**Bảo toàn liên kết pi.** Với hỗn hợp hydrocarbon không no cộng $H_2$ rồi cộng $Br_2$: tổng $n_{\pi}$ ban đầu $=n_{H_2\,pư}+n_{Br_2\,pư}$. Khi nào dùng? Bài hỗn hợp alkene–alkyne cộng lần lượt H2 và Br2, dùng bảo toàn liên kết pi để lập một phương trình gọn thay cho việc theo dõi từng chất.

**Lỗi thường gặp:**
- Cho rằng mọi alkyne đều phản ứng với AgNO3/NH3: chỉ ank-1-yne (có H đầu mạch) mới tạo kết tủa; but-2-yne không phản ứng.
- Dùng 1 AgNO3 cho acetylene: acetylene có hai H đầu mạch nên tạo Ag2C2, dùng 2 AgNO3 — quên điều này làm sai khối lượng kết tủa gấp đôi.
- Tính alkyne chỉ cộng 1 mol Br2 như alkene: alkyne có 2 liên kết pi nên cộng 2 mol Br2 — thiếu một nấc làm sai n(pi).

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.alkyne`</sub>

---

### 4. Arene: benzene và đồng đẳng
*Arenes: benzene and homologues* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Mô tả được cấu tạo vòng benzene và tính thơm (vừa thế vừa khó cộng)
- Viết được phản ứng thế (halogen hóa, nitro hóa) và quy tắc thế trên vòng có sẵn nhóm thế
- Phân biệt phản ứng của benzene với phản ứng ở nhánh alkyl (toluene)

Benzene $C_6H_6$ có độ bất bão hòa $k=4$ nhưng lại không làm mất màu dung dịch bromine như alkene — nghịch lí này được giải thích bằng **tính thơm**: sáu electron pi liên hợp đều trên vòng làm vòng rất bền. Vì thế arene ưu tiên phản ứng thế hơn cộng.

**Phản ứng thế.** Halogen hóa (xúc tác bột Fe) và nitro hóa (HNO3 đặc/H2SO4 đặc) thay H trên vòng: $C_6H_6+Br_2\xrightarrow{Fe}C_6H_5Br+HBr$. Với vòng đã có sẵn nhóm thế, hướng thế tiếp theo tuân theo quy tắc: nhóm đẩy electron (–CH3, –OH) định hướng ortho/para, nhóm hút electron (–NO2, –COOH) định hướng meta.

**Phản ứng ở nhánh.** Toluene $C_6H_5CH_3$ vừa thế được ở vòng, vừa oxi hóa được ở nhánh: $KMnO_4$ nóng biến $-CH_3$ thành $-COOH$ (tạo acid benzoic), trong khi benzene trơ với $KMnO_4$.

**Cộng khắc nghiệt.** Chỉ trong điều kiện mạnh benzene mới cộng: $+3H_2\xrightarrow{Ni,t^\circ}$ cyclohexane; $+3Cl_2\xrightarrow{as}$ hexachlorocyclohexane.

Khi nào dùng dữ kiện nào? Nhận biết benzene vs toluene bằng $KMnO_4$; xác định vị trí nhóm thế bằng quy tắc định hướng ortho/para/meta.

**Lỗi thường gặp:**
- Cho rằng benzene làm mất màu dung dịch bromine như alkene: benzene bền, chỉ thế (cần xúc tác Fe) chứ không cộng Br2 ở điều kiện thường.
- Nhầm khả năng oxi hóa của benzene và toluene với KMnO4: benzene trơ, còn toluene bị oxi hóa nhánh CH3 thành COOH — dùng nhầm để nhận biết sẽ sai.
- Áp sai quy tắc định hướng: nhóm –NO2, –COOH hút electron nên định hướng meta, không phải ortho/para; xác định nhầm vị trí đồng phân.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.arene`</sub>

---

### 5. Bài toán đốt cháy hydrocarbon: phương pháp giải nhanh
*Fast methods for hydrocarbon combustion problems* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Thiết lập được quan hệ giữa n(CO2) và n(H2O) theo từng dãy đồng đẳng khi đốt cháy
- Tính được số nguyên tử carbon trung bình để tìm hai chất đồng đẳng kế tiếp
- Áp dụng bảo toàn nguyên tố oxygen và bảo toàn khối lượng để tính lượng O2 và sản phẩm

Đề đốt cháy hydrocarbon lặp đi lặp lại trong đề thi, và nếu cân bằng từng phương trình sẽ rất mất thời gian. Cả dạng bài này quy về vài hệ thức bảo toàn nhớ sẵn.

**Quan hệ n(CO2) và n(H2O) theo dãy.** Đây là dấu hiệu nhận dạng nhanh:
- Alkane $C_nH_{2n+2}$: $n_{H_2O}>n_{CO_2}$ và $n_{alkane}=n_{H_2O}-n_{CO_2}$.
- Alkene, cycloalkane $C_nH_{2n}$: $n_{CO_2}=n_{H_2O}$.
- Alkyne, alkadiene $C_nH_{2n-2}$: $n_{CO_2}>n_{H_2O}$ và $n_{chất}=n_{CO_2}-n_{H_2O}$.

**Số C trung bình.** Với hỗn hợp: $\bar C=\dfrac{n_{CO_2}}{n_{hh}}$. Nếu $\bar C$ nằm giữa hai số nguyên thì hai chất là đồng đẳng kế tiếp bao quanh giá trị đó.

**Bảo toàn O và khối lượng.**
$$n_{O_2}=n_{CO_2}+\tfrac{1}{2}n_{H_2O}$$
$$m_{hydrocarbon}=12n_{CO_2}+2n_{H_2O}$$
Độ tăng khối lượng bình đựng $H_2SO_4$ (hút $H_2O$) $=m_{H_2O}$; bình đựng $KOH$ (hút $CO_2$) $=m_{CO_2}$.

Khi nào dùng gì? Cho $n_{CO_2},n_{H_2O}$ và hỏi loại chất hoặc số mol: dùng quan hệ theo dãy; cho khối lượng hydrocarbon và hỏi $O_2$: dùng bảo toàn O và khối lượng.

**Lỗi thường gặp:**
- Áp quan hệ n(CO2) = n(H2O) cho alkane: sai, alkane luôn cho n(H2O) > n(CO2); chỉ alkene/cycloalkane mới có n(CO2) = n(H2O).
- Tính n(O2) = n(CO2) + n(H2O): sai hệ số, phải là n(O2) = n(CO2) + ½n(H2O) theo bảo toàn nguyên tố oxygen.
- Lấy độ tăng khối lượng bình KOH làm khối lượng H2O: KOH hấp thụ CO2, còn H2SO4 đặc (hoặc P2O5) mới hấp thụ H2O — gán nhầm bình dẫn tới đảo dữ kiện.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.dot-chay-hidrocacbon`</sub>

---

## Chương: Hợp chất carbonyl – Carboxylic acid

### 1. Aldehyde và ketone: phản ứng của nhóm carbonyl
*Aldehydes and ketones: carbonyl reactions* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được aldehyde và ketone qua phản ứng tráng bạc (chỉ aldehyde phản ứng)
- Viết được phản ứng cộng H2 (khử) và phản ứng oxi hóa aldehyde thành acid
- Tính được khối lượng Ag khi tráng bạc, lưu ý trường hợp đặc biệt của HCHO

Aldehyde và ketone cùng chứa nhóm carbonyl C=O nhưng khác nhau ở vị trí. Sự khác biệt then chốt: aldehyde có nguyên tử H gắn trực tiếp vào carbonyl nên dễ bị oxi hóa, còn ketone thì không — đây là cơ sở phân biệt hai loại.

**Phản ứng tráng bạc (nhận biết aldehyde).**
$$R\text{-}CHO+2AgNO_3+3NH_3+H_2O\rightarrow R\text{-}COONH_4+2Ag\downarrow+2NH_4NO_3$$
Mỗi nhóm –CHO cho **2 mol Ag**. Ngoại lệ quan trọng: formaldehyde $HCHO$ có cấu tạo như có hai nhóm –CHO, cho **4 mol Ag** với 1 mol HCHO. Ketone không cho phản ứng này.

**Phản ứng cộng H2 (khử).** Carbonyl cộng $H_2$ (Ni, t°) tạo alcohol: aldehyde → alcohol bậc I, ketone → alcohol bậc II.

**Oxi hóa aldehyde.** Aldehyde dễ bị oxi hóa (bởi $O_2$, $Br_2$, $KMnO_4$…) thành acid tương ứng: $R\text{-}CHO\rightarrow R\text{-}COOH$.

Khi nào dùng gì? Dùng tráng bạc để nhận biết và định lượng aldehyde; nhớ kiểm tra HCHO (4 Ag) và các chất có nhiều nhóm –CHO. Đề cho khối lượng Ag → suy n(–CHO), lưu ý bẫy HCHO.

**Lỗi thường gặp:**
- Cho rằng ketone cũng tráng bạc: chỉ aldehyde (có H gắn carbonyl) phản ứng, ketone không cho Ag — dùng nhầm để nhận biết là sai.
- Áp tỉ lệ 1 –CHO cho 2 Ag cho cả HCHO: HCHO cho 4 Ag; bỏ qua ngoại lệ này làm sai gấp đôi số mol chất.
- Nhầm aldehyde với alcohol khi cộng H2: aldehyde cộng H2 tạo alcohol bậc I, ketone tạo alcohol bậc II — kết luận nhầm bậc alcohol sản phẩm.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.aldehyde-ketone`</sub>

---

### 2. Carboxylic acid: tính acid và phản ứng ester hóa
*Carboxylic acids: acidity and esterification* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Viết được phản ứng của carboxylic acid với kim loại, base và muối carbonate
- Phân biệt được carboxylic acid với phenol và alcohol dựa vào phản ứng với NaHCO3
- Vận dụng phản ứng ester hóa và khái niệm phản ứng thuận nghịch, hiệu suất

Carboxylic acid mang nhóm –COOH và là acid hữu cơ tiêu biểu. Tính acid của nó tuy yếu nhưng đủ mạnh để thể hiện đầy đủ tính chất acid — và đó chính là cách phân biệt nó với phenol, alcohol.

**Tính acid.** –COOH tác dụng với kim loại trước H, với base và với oxide base:
$$2R\text{-}COOH+2Na\rightarrow 2R\text{-}COONa+H_2$$
$$R\text{-}COOH+NaOH\rightarrow R\text{-}COONa+H_2O$$
Đặc biệt, acid mạnh hơn carbonic acid nên đẩy được $CO_2$ ra khỏi muối carbonate:
$$R\text{-}COOH+NaHCO_3\rightarrow R\text{-}COONa+CO_2\uparrow+H_2O$$
Phenol và alcohol **không** phản ứng với $NaHCO_3$ — đây là cách phân biệt chắc chắn nhất.

**Ester hóa.** Với alcohol, xúc tác $H_2SO_4$ đặc, tạo ester:
$$R\text{-}COOH+R'OH\rightleftharpoons R\text{-}COOR'+H_2O$$
Phản ứng thuận nghịch nên hiệu suất < 100%; muốn tăng hiệu suất phải tách nước hoặc dùng dư một chất.

Khi nào dùng gì? Phân biệt acid / phenol / alcohol: dùng $NaHCO_3$ (chỉ acid sủi bọt khí); định lượng acid bằng phản ứng trung hòa với NaOH ($n_{NaOH}=n_{-COOH}$).

**Lỗi thường gặp:**
- Cho rằng phenol và alcohol cũng phản ứng với NaHCO3 sinh khí: chỉ carboxylic acid mới đủ mạnh đẩy CO2 khỏi muối carbonate — nhầm sẽ mất dấu hiệu phân biệt.
- Coi ester hóa là phản ứng một chiều, hoàn toàn: đây là phản ứng thuận nghịch, hiệu suất luôn nhỏ hơn 100% nên không được lấy lượng ester bằng lượng acid ban đầu.
- Nhầm số nhóm –COOH: acid đa chức (như oxalic HOOC-COOH) cần nhiều NaOH hơn theo số nhóm; giả định luôn đơn chức làm sai khối lượng mol.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.carboxylic-acid`</sub>

---

## Chương: Hợp chất chứa nitrogen

### 1. Amine: tính base và phản ứng với acid
*Amines: basicity and reaction with acids* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được tính base của amine và so sánh lực base của amine với ammonia
- Viết được phản ứng của amine với dung dịch acid tạo muối
- Giải được bài toán đốt cháy amine no đơn chức và xác định công thức

Amine là dẫn xuất của ammonia. Giống ammonia, nguyên tử nitrogen còn cặp electron tự do, khiến amine có **tính base** — đây là tính chất chi phối toàn bộ phản ứng của chúng.

**Tính base và phản ứng với acid.** Amine nhận proton tạo muối:
$$CH_3NH_2+HCl\rightarrow CH_3NH_3Cl$$
Với amine đơn chức: $n_{HCl}=n_{amine}$. Lực base phụ thuộc gốc gắn với N: gốc alkyl đẩy electron làm methylamine, ethylamine mạnh hơn ammonia; ngược lại aniline $C_6H_5NH_2$ có vòng benzene hút electron nên là base rất yếu (không đổi màu quỳ).

**Đốt cháy amine no đơn chức.** Với $C_nH_{2n+3}N$:
$$n_{H_2O}-n_{CO_2}=1{,}5\,n_{amine}$$
(vì mỗi phân tử dư 3 H so với alkene). Từ số mol CO2 suy số C.

**Nhận biết.** Aniline tạo kết tủa trắng với nước bromine (tương tự phenol, do nhóm –NH2 hoạt hóa vòng).

Khi nào dùng gì? Định lượng amine bằng phản ứng với HCl ($n_{HCl}=n_{amine}$ cho đơn chức); tìm công thức amine no đơn chức qua đốt cháy dùng quan hệ $n_{H_2O}-n_{CO_2}=1{,}5n$.

**Lỗi thường gặp:**
- Cho rằng mọi amine đều có lực base mạnh hơn ammonia: aniline (amine thơm) có lực base yếu hơn ammonia do vòng benzene hút cặp electron của N.
- Dùng quan hệ n(H2O) = n(CO2) cho amine no đơn chức: thực tế n(H2O) − n(CO2) = 1,5·n(amine) vì công thức là CnH2n+3N (nhiều H hơn alkene).
- Quên amine đa chức cần nhiều HCl hơn: amine hai chức phản ứng 2 HCl trên mỗi phân tử; giả định luôn đơn chức làm sai tỉ lệ mol.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.amine`</sub>

---

### 2. Amino acid: tính lưỡng tính
*Amino acids: amphoteric character* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được tính lưỡng tính của amino acid (vừa phản ứng acid vừa phản ứng base)
- Tính được lượng HCl và NaOH phản ứng dựa vào số nhóm –NH2 và –COOH
- Giải được bài toán amino acid phản ứng lần lượt với HCl rồi NaOH (hoặc ngược lại)

Amino acid mang cùng lúc nhóm –NH2 có tính base và nhóm –COOH có tính acid, nên chúng vừa phản ứng với acid vừa phản ứng với base — tức là **lưỡng tính**. Đây là điểm mấu chốt của mọi bài toán về amino acid.

**Phản ứng với acid (nhờ –NH2).** $H_2N\text{-}R\text{-}COOH+HCl\rightarrow ClH_3N\text{-}R\text{-}COOH$; $n_{HCl}=(\text{số }NH_2)\cdot n_{aa}$.

**Phản ứng với base (nhờ –COOH).** $H_2N\text{-}R\text{-}COOH+NaOH\rightarrow H_2N\text{-}R\text{-}COONa+H_2O$; $n_{NaOH}=(\text{số }COOH)\cdot n_{aa}$.

**Bài toán hai giai đoạn.** Khi cho amino acid vào HCl (dư) rồi trung hòa dung dịch thu được bằng NaOH: NaOH phải trung hòa **cả HCl dư lẫn nhóm –COOH** của amino acid. Công thức bảo toàn:
$$n_{NaOH}=n_{HCl\,ban\,đầu}+(\text{số }COOH)\cdot n_{aa}$$
Coi toàn bộ hỗn hợp cần trung hòa gồm H+ của HCl và H+ của –COOH.

Khi nào dùng gì? Tìm số nhóm chức: so sánh $n_{HCl}$ và $n_{NaOH}$ với $n_{aa}$. Bài phản ứng nối tiếp acid–base: dùng bảo toàn điện tích/bảo toàn nhóm H+ thay vì theo dõi từng bước.

**Lỗi thường gặp:**
- Chỉ trừ đi phần HCl 'còn dư' rồi cộng nhóm –COOH: cách đúng là NaOH trung hòa cả LƯỢNG HCl ban đầu lẫn nhóm –COOH của amino acid, tức n(NaOH) = n(HCl ban đầu) + số COOH × n(aa).
- Nhầm số nhóm chức: glutamic acid có 2 nhóm –COOH, lysine có 2 nhóm –NH2; giả định luôn 1–1 làm sai tỉ lệ HCl/NaOH.
- Cho rằng amino acid chỉ có tính acid (vì tên gọi 'acid'): amino acid lưỡng tính, phản ứng được với cả HCl và NaOH nhờ hai nhóm chức khác nhau.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.amino-acid`</sub>

---

### 3. Peptide và protein: thủy phân và bảo toàn khối lượng
*Peptides and proteins: hydrolysis and mass conservation* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Xác định được số liên kết peptide và số mắt xích của một peptide
- Tính được khối lượng muối khi thủy phân peptide bằng NaOH nhờ bảo toàn khối lượng
- Đếm được số peptide (đipeptit, tripeptit) tạo thành từ các amino acid cho trước

Peptide được tạo thành khi các amino acid nối với nhau bằng liên kết peptide –CO–NH–, loại đi một phân tử nước mỗi lần nối. Protein là polypeptide phức tạp. Các bài toán peptide tưởng khó nhưng đều quy về đếm mắt xích và bảo toàn khối lượng.

**Số mắt xích và liên kết.** Peptide gồm k gốc amino acid có $k-1$ liên kết peptide. Khối lượng của peptide tạo từ k amino acid $M_i$: $M_{peptide}=\sum M_i-(k-1)\cdot 18$ (mất $k-1$ nước).

**Thủy phân bằng NaOH.** Mỗi gốc có 1 nhóm –COOH (giả sử amino acid đơn giản) nên $n_{NaOH}=k\cdot n_{peptide}$, và toàn bộ peptide chỉ nhận thêm 1 phân tử nước khi thủy phân, cho:
$$m_{muối}=m_{peptide}+40n_{NaOH}-18n_{peptide}$$
Đây là công cụ giải nhanh: không cần biết peptide cụ thể, chỉ cần khối lượng và số mắt xích.

**Đếm số peptide.** Từ n loại amino acid, số đipeptit tối đa (kể cả trùng gốc) $=n^2$; số tripeptit $=n^3$.

Khi nào dùng gì? Cho khối lượng peptide và số mắt xích → dùng bảo toàn khối lượng tìm muối; hỏi số đipeptit/tripeptit → dùng $n^2$, $n^3$; cho sản phẩm thủy phân → đếm gốc để suy số liên kết peptide.

**Lỗi thường gặp:**
- Nhầm số phân tử nước: khi thủy phân bằng NaOH, cả peptide chỉ nhận thêm 1 mol H2O trên mỗi mol peptide (không phải mỗi liên kết), còn NaOH thì bằng số mắt xích.
- Lấy n(NaOH) bằng số liên kết peptide (k − 1) thay vì số mắt xích (k): NaOH phản ứng với tất cả nhóm –COOH của các gốc, nên bằng k.
- Đếm số đipeptit chỉ gồm hai gốc khác nhau: số đipeptit tối đa từ n amino acid là n² (bao gồm cả đipeptit tạo từ hai gốc giống nhau như Gly-Gly).

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.peptide-protein`</sub>

---

## Chương: Phương pháp giải nhanh hóa hữu cơ

### 1. Các phương pháp bảo toàn trong hóa hữu cơ
*Conservation methods in organic chemistry* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · chuyen-sau

**Mục tiêu:**
- Vận dụng bảo toàn khối lượng và bảo toàn nguyên tố để tránh viết phương trình phức tạp
- Sử dụng bảo toàn nguyên tố oxygen trong bài toán đốt cháy hợp chất chứa oxygen
- Kết hợp bảo toàn liên kết pi cho hỗn hợp hydrocarbon không no cộng H2, Br2

Đề trắc nghiệm hóa hữu cơ hiếm khi yêu cầu viết đủ phương trình — thay vào đó, người ta thưởng cho ai biết dùng **các định luật bảo toàn** để đi tắt. Ba công cụ dưới đây giải quyết phần lớn bài toán.

**Bảo toàn khối lượng (BTKL).** $\sum m_{trước}=\sum m_{sau}$. Áp cho xà phòng hóa, thủy phân peptide, cracking: biết mọi chất trừ một, tính chất còn lại ngay.

**Bảo toàn nguyên tố (BTNT).** Số mol mỗi nguyên tố không đổi. Với đốt cháy hợp chất $C_xH_yO_z$:
$$n_{O\,(chất)}+2n_{O_2}=2n_{CO_2}+n_{H_2O}$$
Từ đây tìm số O trong chất hoặc lượng O2 mà không cần cân bằng.

**Bảo toàn liên kết pi.** Với hỗn hợp hydrocarbon không no: tổng số mol liên kết pi ban đầu bằng tổng $n_{H_2}$ và $n_{Br_2}$ đã cộng: $n_{\pi}=n_{H_2\,pư}+n_{Br_2\,pư}$.

Khi nào dùng gì? Bài nhiều chất, nhiều bước phản ứng nhưng hỏi khối lượng tổng: dùng BTKL. Bài đốt cháy tìm số O hoặc lượng O2: dùng BTNT oxygen. Bài cộng H2 rồi Br2: dùng bảo toàn liên kết pi. Chọn đúng đại lượng bảo toàn giúp bỏ qua chi tiết trung gian.

**Lỗi thường gặp:**
- Quên số mol O có sẵn trong hợp chất khi bảo toàn oxygen: với hợp chất chứa O, phải cộng n(O trong chất) vào vế trái, không chỉ tính O2.
- Áp bảo toàn liên kết pi cho hợp chất no: chất no không có liên kết pi, hệ thức n(pi) = n(H2) + n(Br2) chỉ dùng cho hydrocarbon không no.
- Dùng bảo toàn khối lượng nhưng bỏ sót một chất tham gia hoặc sản phẩm (ví dụ nước, glycerol, khí thoát ra): thiếu một số hạng làm phương trình khối lượng sai.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.bao-toan-huu-co`</sub>

---

## Chương: Polymer

### 1. Polymer: hệ số trùng hợp và vật liệu
*Polymers: degree of polymerization and materials* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Tính được hệ số trùng hợp (số mắt xích) từ khối lượng mol của polymer
- Tính được phần trăm khối lượng nguyên tố trong polymer và trong cao su lưu hóa
- Phân biệt được phản ứng trùng hợp và trùng ngưng, tính hiệu suất điều chế polymer

Polymer là những phân tử khổng lồ gồm nhiều mắt xích lặp lại. Toàn bộ tính toán về polymer xoay quanh một ý tưởng: phân tử polymer bằng $n$ lần mắt xích, với $n$ là hệ số trùng hợp.

**Hệ số trùng hợp.** $n=\dfrac{M_{polymer}}{M_{mắt\,xích}}$. Ví dụ polyethylene $(-CH_2-CH_2-)_n$ có mắt xích M = 28.

**Trùng hợp và trùng ngưng.** Trùng hợp: các monomer có nối đôi cộng hợp lại, không tách sản phẩm phụ (PE, PVC, cao su). Trùng ngưng: các monomer có hai nhóm chức nối nhau và **tách ra phân tử nhỏ** như H2O (nylon-6,6, tơ lapsan).

**Phần trăm khối lượng nguyên tố** trong polymer tính như mọi hợp chất, dựa trên công thức mắt xích.

**Cao su lưu hóa.** Lưu huỳnh tạo cầu nối –S–S–; nếu cứ $k$ mắt xích isoprene ($C_5H_8$, M = 68) có một cầu gồm $a$ nguyên tử S:
$$\%S=\dfrac{32a}{68k+32a-2}\times100\%$$
Từ %S suy ra $k$ (số mắt xích trên mỗi cầu nối).

Khi nào dùng gì? Cho M polymer → tính n; cho %S → tìm số mắt xích trên mỗi cầu lưu hóa; bài điều chế có hiệu suất → nhân/chia hiệu suất giữa monomer và polymer.

**Lỗi thường gặp:**
- Nhầm trùng hợp với trùng ngưng: trùng hợp không tách sản phẩm phụ, còn trùng ngưng tách ra phân tử nhỏ (thường H2O) — nhầm sẽ tính sai khối lượng mắt xích.
- Dùng khối lượng monomer thay cho khối lượng mắt xích khi tính hệ số trùng hợp: trong trùng ngưng, mắt xích nhỏ hơn monomer do đã tách H2O.
- Quên phần khối lượng H bị thay khi lưu hóa: công thức %S trừ đi 2 ở mẫu số vì hai H bị S thay thế; bỏ qua làm lệch kết quả.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.polymer`</sub>

---

## Chương: Đại cương về hóa học hữu cơ

### 1. Công thức tổng quát của các dãy đồng đẳng
*General formulas of homologous series* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · co-ban

**Mục tiêu:**
- Viết được công thức tổng quát của các dãy đồng đẳng hydrocarbon và dẫn xuất chứa oxygen, nitrogen thường gặp
- Suy luận được số liên kết pi và vòng (độ bất bão hòa) từ công thức tổng quát
- Vận dụng công thức tổng quát để nhận dạng nhanh loại hợp chất trong bài toán trắc nghiệm

Khi gặp một hợp chất hữu cơ lạ, câu hỏi đầu tiên là: nó thuộc dãy nào? Trả lời được câu này thì đã đoán được tính chất và chọn đúng công thức tính toán. Vì thế, thuộc công thức tổng quát (CTTQ) của các dãy đồng đẳng là nền tảng của toàn bộ hóa hữu cơ.

**Hydrocarbon.** Alkane no, mạch hở: $C_nH_{2n+2}$ $(n\ge 1)$. Mỗi liên kết đôi hoặc một vòng làm mất 2 nguyên tử H: alkene và cycloalkane $C_nH_{2n}$, alkyne và alkadiene $C_nH_{2n-2}$, arene (đồng đẳng benzene) $C_nH_{2n-6}$ $(n\ge 6)$.

**Dẫn xuất chứa oxygen.** Alcohol/ether no, đơn chức, mạch hở: $C_nH_{2n+2}O$. Aldehyde/ketone no, đơn chức, mạch hở: $C_nH_{2n}O$. Acid/ester no, đơn chức, mạch hở: $C_nH_{2n}O_2$.

**Chứa nitrogen.** Amine no, đơn chức, mạch hở: $C_nH_{2n+3}N$. Amino acid no có 1 nhóm $NH_2$ và 1 nhóm $COOH$: $C_nH_{2n+1}O_2N$.

Quy luật vàng: viết CTTQ dạng $C_nH_{2n+2-2k}X$ rồi cộng thêm phần của nhóm chức. Khi nào dùng? Bất cứ khi nào cần thiết lập phương trình theo n để tìm công thức phân tử từ khối lượng mol hoặc từ sản phẩm cháy.

**Lỗi thường gặp:**
- Nhầm cycloalkane với alkane: cả hai đều no nhưng cycloalkane có 1 vòng nên là CnH2n, ít hơn alkane 2 H — quên điều này sẽ đặt sai công thức tổng quát khi lập phương trình.
- Quên điều kiện chặn của n (ví dụ arene cần n ≥ 6, alcohol đơn chức cần n ≥ 1) dẫn tới nghiệm vô lí như số nguyên tử C âm hoặc bằng 0.
- Áp công thức của chất no cho hợp chất có nối đôi/nối ba: sai vì số H không còn khớp, làm lệch toàn bộ bài toán đốt cháy.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.cttq-day-dong-dang`</sub>

---

### 2. Độ bất bão hòa và liên hệ đốt cháy
*Degree of unsaturation and combustion relationship* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Tính được độ bất bão hòa k từ công thức phân tử của hợp chất chứa C, H, O, N
- Giải thích được vì sao hiệu số mol CO2 và H2O khi đốt cháy cho biết loại hợp chất
- Vận dụng liên hệ $n_{CO_2}-n_{H_2O}=(k-1)n_X$ để tính nhanh không cần viết phương trình

Nhiều bài toán hữu cơ cho dữ kiện gián tiếp: đề không nói X là chất gì mà chỉ cho số mol CO2 và H2O. Làm sao biết X thuộc dãy nào để chọn công thức? Chìa khóa là **độ bất bão hòa** $k$.

**Công thức tính.** Với hợp chất $C_xH_yO_zN_t$:
$$k=\dfrac{2x+2+t-y}{2}$$
Nguyên tử oxygen không xuất hiện vì O có hóa trị 2, không làm thay đổi số H bão hòa. Giá trị $k$ phải là số nguyên $\ge 0$; nếu ra số lẻ hoặc âm thì công thức sai.

**Liên hệ với đốt cháy.** Đây là công cụ giải nhanh quan trọng nhất của phần hydrocarbon và hợp chất chứa oxygen mạch hở:
$$n_{CO_2}-n_{H_2O}=(k-1)\,n_X$$
Từ đó:
- $k=0$ (chất no, hở, như alkane, alcohol no): $n_{H_2O}>n_{CO_2}$, và $n_X=n_{H_2O}-n_{CO_2}$.
- $k=1$ (alkene, ester no đơn chức): $n_{CO_2}=n_{H_2O}$.
- $k=2$ (alkyne, alkadiene): $n_{CO_2}-n_{H_2O}=n_X$.

Khi nào dùng? Khi đề cho sẵn số mol sản phẩm cháy và hỏi số mol chất, số C trung bình, hoặc loại dãy đồng đẳng — dùng liên hệ này bỏ qua hoàn toàn việc cân bằng phương trình.

**Lỗi thường gặp:**
- Cộng cả số nguyên tử O vào công thức tính k — sai vì O hóa trị 2 không ảnh hưởng cân bằng H; chỉ C, H, N (và halogen) mới vào công thức.
- Quên rằng k phải nguyên và không âm: nếu tính ra k = 1,5 thì chắc chắn đã sai số nguyên tử H hoặc nhầm công thức, cần soát lại.
- Dùng liên hệ n(CO2) − n(H2O) = (k−1)n cho hỗn hợp nhiều chất có k khác nhau mà không tách riêng — với hỗn hợp phải dùng k trung bình hoặc tổng số mol liên kết pi.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.do-bat-bao-hoa`</sub>

---

### 3. Lập công thức phân tử hợp chất hữu cơ
*Determining molecular formula* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Lập được công thức đơn giản nhất từ phần trăm khối lượng các nguyên tố
- Xác định được số nguyên tử mỗi nguyên tố từ khối lượng sản phẩm cháy (CO2, H2O, N2)
- Suy ra được công thức phân tử khi biết khối lượng mol hoặc tỉ khối hơi

Xác định công thức phân tử là mục tiêu trung tâm của phân tích hữu cơ. Có hai con đường dữ kiện thường gặp, và cả hai đều quy về việc tìm số mol từng nguyên tố.

**Con đường 1 — từ phần trăm khối lượng.** Giả sử có 100 g chất: khối lượng mỗi nguyên tố bằng đúng phần trăm của nó. Chia cho khối lượng mol nguyên tử để được số mol, rồi lập tỉ lệ:
$$x:y:z=\dfrac{\%C}{12}:\dfrac{\%H}{1}:\dfrac{\%O}{16}$$
Tối giản tỉ lệ này được công thức đơn giản nhất $(CH_2O)_m$ chẳng hạn. Sau đó dùng khối lượng mol $M$ để tìm $m$: $M=m\cdot M_{CTĐGN}$.

**Con đường 2 — từ sản phẩm cháy.** Áp dụng bảo toàn nguyên tố:
$$n_C=n_{CO_2},\quad n_H=2n_{H_2O},\quad n_N=2n_{N_2}$$
Khối lượng oxygen trong chất tính bằng hiệu: $m_O=m_X-m_C-m_H-m_N$. Từ số mol các nguyên tố và số mol chất (nếu biết) suy ra số nguyên tử.

Khi nào dùng cách nào? Có phần trăm hoặc khối lượng nguyên tố thì dùng con đường 1; có khối lượng $CO_2$, $H_2O$ thì dùng con đường 2. Luôn kiểm tra bằng độ bất bão hòa: $k$ ra số nguyên không âm mới nhận.

**Lỗi thường gặp:**
- Quên tính phần trăm nguyên tố còn lại (thường là O) bằng cách lấy 100% trừ đi các phần trăm đã cho — bỏ sót O làm sai toàn bộ tỉ lệ.
- Lấy công thức đơn giản nhất làm luôn công thức phân tử mà không nhân hệ số m: sai vì nhiều chất khác nhau có cùng CTĐGN (ví dụ CH2O, C2H4O2, C6H12O6 đều là (CH2O)m).
- Tính m(O) trong chất bằng m(H2O) hoặc m(CO2): sai vì oxygen của sản phẩm cháy còn lấy từ khí O2; phải dùng m(O) = m(chất) − m(C) − m(H).

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.lap-cong-thuc-phan-tu`</sub>

---

### 4. Đếm đồng phân hợp chất hữu cơ
*Counting isomers of organic compounds* · THPT (lớp 10-12) · vn-gdpt-2018 · 50 phút · trung-binh

**Mục tiêu:**
- Phân biệt được đồng phân cấu tạo (mạch carbon, vị trí, nhóm chức) và đồng phân hình học cis–trans
- Đếm được số đồng phân của alkane, alcohol, aldehyde, acid, ester, amine đơn chức thường gặp
- Xác định được điều kiện để một hợp chất có đồng phân hình học

Cùng một công thức phân tử có thể ứng với nhiều chất khác nhau — đó là hiện tượng đồng phân, và bài toán đếm đồng phân xuất hiện dày đặc trong đề trắc nghiệm. Bí quyết là đếm có hệ thống, không bỏ sót không trùng lặp.

**Phân loại.** Đồng phân cấu tạo gồm: đồng phân mạch carbon (thẳng/nhánh), đồng phân vị trí (nhóm chức, nối đôi ở vị trí khác), và đồng phân nhóm chức (ví dụ alcohol và ether cùng $C_nH_{2n+2}O$). Ngoài ra còn đồng phân hình học cis–trans quanh nối đôi.

**Một số kết quả nhớ nhanh** (đơn chức, no, mạch hở):
- Alcohol $C_nH_{2n+2}O$: số đồng phân alcohol $=2^{\,n-2}$ với $2<n<6$ (C3: 2, C4: 4, C5: 8).
- Aldehyde, acid, ester đều có quy luật tương tự; ester $C_nH_{2n}O_2$: $2^{\,n-2}$ với $n<5$ (C3: 2, C4: 4).
- Amine $C_nH_{2n+3}N$: tổng số đồng phân amine $=2^{\,n-1}$ với $n<5$.

**Đồng phân hình học** xuất hiện khi mỗi C của nối đôi mang hai nhóm khác nhau. But-2-ene có cis/trans, còn but-1-ene thì không (một C mang hai H giống nhau).

Khi nào áp công thức mũ, khi nào vẽ tay? Với $n$ nhỏ nên vẽ cấu tạo để chắc chắn; công thức mũ chỉ dùng để đối chiếu kết quả.

**Lỗi thường gặp:**
- Đếm cả đồng phân của gốc acid lẫn gốc ancol nhưng bỏ sót các nhánh (ví dụ quên isopropyl của C3H7) — dẫn tới thiếu đồng phân.
- Cho rằng mọi hợp chất có nối đôi C=C đều có đồng phân hình học: sai, phải kiểm tra mỗi C của nối đôi có hai nhóm khác nhau (propene, but-1-ene không có cis–trans).
- Nhầm đồng phân với đồng đẳng: đồng phân cùng công thức phân tử; đồng đẳng khác nhau một số nhóm CH2 — nhầm hai khái niệm khiến đếm sai đối tượng.

<sub>`lesson.chemistry.vn-thpt-chemistry-huuco.dem-dong-phan`</sub>

---

## Lớp 11 - Chương 1: Cân bằng hoá học

### 1. Cân bằng hoá học, hằng số cân bằng Kc và Kp
*Chemical equilibrium and the equilibrium constants Kc and Kp* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Viết được biểu thức hằng số cân bằng Kc, Kp cho phản ứng thuận nghịch
- Tính được Kc, Kp và độ chuyển hoá từ nồng độ hoặc áp suất lúc cân bằng

## Phản ứng thuận nghịch và trạng thái cân bằng

Nhiều phản ứng không xảy ra hoàn toàn mà **thuận nghịch**: sản phẩm lại tái tạo chất đầu. Khi tốc độ thuận bằng tốc độ nghịch, nồng độ các chất không đổi — đó là **cân bằng hoá học**. Cân bằng là động (phản ứng vẫn xảy ra hai chiều), không phải phản ứng dừng lại.

## Hằng số cân bằng Kc

Với $aA + bB \rightleftharpoons cC + dD$:

$$K_c = \frac{[C]^c [D]^d}{[A]^a [B]^b}$$

dùng nồng độ **lúc cân bằng**. Chất rắn và chất lỏng nguyên chất không xuất hiện trong biểu thức (nồng độ coi như hằng). $K_c$ chỉ phụ thuộc nhiệt độ: $K_c$ lớn nghĩa là cân bằng lệch mạnh về sản phẩm.

## Hằng số Kp cho phản ứng khí

Với phản ứng khí, dùng áp suất riêng phần:
$$K_p = \frac{(p_C)^c (p_D)^d}{(p_A)^a (p_B)^b}, \qquad K_p = K_c (RT)^{\Delta n}$$
với $\Delta n = (c+d)-(a+b)$ là chênh lệch số mol khí. Nếu $\Delta n = 0$ thì $K_p = K_c$.

## Cách lập bảng ICE

Đặt nồng độ ban đầu (Initial), biến đổi (Change) theo ẩn $x$ và hệ số, rồi nồng độ cân bằng (Equilibrium). Thay vào biểu thức $K_c$ để tìm $x$, từ đó suy độ chuyển hoá.

## Khi nào dùng

Đề cho nồng độ (hoặc số mol và thể tích bình) lúc cân bằng: thay thẳng vào $K_c$. Đề cho $K_c$ và nồng độ đầu: lập ICE, giải phương trình tìm $x$.

**Lỗi thường gặp:**
- Đưa nồng độ chất rắn hoặc chất lỏng nguyên chất vào biểu thức $K_c$ — sai vì nồng độ của chúng coi như hằng số, đã gộp vào $K_c$.
- Quên luỹ thừa nồng độ theo hệ số tỉ lượng — ví dụ viết $[\mathrm{HI}]$ thay vì $[\mathrm{HI}]^2$, cho $K_c$ sai hoàn toàn.
- Dùng nồng độ ban đầu thay cho nồng độ lúc cân bằng — sai vì $K_c$ định nghĩa theo trạng thái cân bằng.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.can-bang-hoa-hoc-kc-kp`</sub>

---

### 2. Nguyên lí chuyển dịch cân bằng Le Chatelier
*Le Chatelier's principle of equilibrium shift* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · trung-binh

**Mục tiêu:**
- Dự đoán được chiều chuyển dịch cân bằng khi thay đổi nồng độ, áp suất, nhiệt độ
- Vận dụng nguyên lí Le Chatelier để giải thích điều kiện tối ưu trong sản xuất hoá học

## Cân bằng "chống lại" thay đổi

**Nguyên lí Le Chatelier**: khi tác động vào hệ cân bằng (đổi nồng độ, áp suất, nhiệt độ), cân bằng chuyển dịch theo chiều **làm giảm** tác động đó. Nắm ý tưởng "hệ phản kháng" này là dự đoán được mọi trường hợp.

## Ba loại tác động

**Nồng độ**: tăng nồng độ một chất $\Rightarrow$ cân bằng dịch theo chiều làm giảm chất đó (tức chiều tiêu thụ nó). Lấy bớt sản phẩm $\Rightarrow$ dịch theo chiều thuận.

**Áp suất** (chỉ ảnh hưởng phản ứng có chất khí và $\Delta n_{khí}\ne0$): tăng áp suất $\Rightarrow$ dịch về phía có **ít mol khí hơn**. Nếu số mol khí hai vế bằng nhau, áp suất không làm dịch cân bằng.

**Nhiệt độ**: tăng nhiệt độ $\Rightarrow$ dịch theo chiều **thu nhiệt** ($\Delta H > 0$); giảm nhiệt độ $\Rightarrow$ dịch theo chiều toả nhiệt. Đây là yếu tố **duy nhất làm đổi giá trị $K$**.

## Xúc tác không làm dịch cân bằng

Chất xúc tác tăng tốc cả chiều thuận và nghịch như nhau, chỉ giúp đạt cân bằng nhanh hơn, **không** đổi vị trí cân bằng hay $K$.

## Ứng dụng sản xuất

Tổng hợp ammonia $\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3}$, $\Delta H<0$, $\Delta n_{khí}=-2$: muốn nhiều $\mathrm{NH_3}$ nên dùng **áp suất cao** (dịch về phía ít mol khí) và **nhiệt độ vừa phải** (nhiệt thấp có lợi cân bằng nhưng chậm, nên chọn ~450$^\circ$C và xúc tác).

## Khi nào dùng

Câu hỏi "tăng/giảm yếu tố X thì cân bằng dịch chiều nào": xét từng yếu tố theo ba quy tắc trên, nhớ áp suất chỉ xét khi $\Delta n_{khí}\ne0$.

**Lỗi thường gặp:**
- Xét ảnh hưởng áp suất khi số mol khí hai vế bằng nhau — sai vì lúc đó áp suất không làm chuyển dịch cân bằng.
- Cho rằng chất xúc tác làm cân bằng dịch về phía sản phẩm — sai vì xúc tác chỉ tăng tốc đạt cân bằng, không đổi vị trí cân bằng.
- Kết luận tăng nhiệt độ luôn làm tăng hiệu suất — sai vì với phản ứng toả nhiệt, tăng nhiệt độ đẩy cân bằng theo chiều nghịch, giảm sản phẩm.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.nguyen-li-le-chatelier`</sub>

---

### 3. Sự điện li, chất điện li và pH của dung dịch
*Electrolytic dissociation, electrolytes and solution pH* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · trung-binh

**Mục tiêu:**
- Phân biệt được chất điện li mạnh, chất điện li yếu và viết phương trình điện li
- Tính được pH của dung dịch acid mạnh, base mạnh và nêu ý nghĩa của thang pH

## Vì sao dung dịch dẫn điện

Một số chất khi tan trong nước phân li thành **ion** chuyển động tự do, làm dung dịch dẫn điện. Đó là **sự điện li**, và chất gây ra gọi là chất điện li.

## Mạnh hay yếu

- **Chất điện li mạnh** (acid mạnh HCl, $\mathrm{HNO_3}$, $\mathrm{H_2SO_4}$; base mạnh NaOH, KOH, $\mathrm{Ba(OH)_2}$; muối tan) phân li **hoàn toàn**, dùng mũi tên một chiều: $\mathrm{HCl}\to\mathrm{H^+}+\mathrm{Cl^-}$.
- **Chất điện li yếu** (acid yếu $\mathrm{CH_3COOH}$, base yếu $\mathrm{NH_3}$) chỉ phân li **một phần**, dùng mũi tên thuận nghịch.

## Tích số ion của nước và thang pH

Nước tự phân li rất ít: $[\mathrm{H^+}][\mathrm{OH^-}] = K_w = 10^{-14}$ (ở 25$^\circ$C). Định nghĩa:
$$\mathrm{pH} = -\log[\mathrm{H^+}], \qquad \mathrm{pH} + \mathrm{pOH} = 14.$$
pH < 7 là acid, pH = 7 trung tính, pH > 7 base.

## Tính pH acid mạnh, base mạnh

Vì phân li hoàn toàn, nồng độ ion tính trực tiếp:
- Acid mạnh nồng độ $C_a$ (đơn nấc): $[\mathrm{H^+}]=C_a \Rightarrow \mathrm{pH}=-\log C_a$.
- Base mạnh: tính $[\mathrm{OH^-}]$ rồi $\mathrm{pH}=14+\log[\mathrm{OH^-}]$.
Chú ý acid, base nhiều nấc: $\mathrm{H_2SO_4}\to 2\mathrm{H^+}$, $\mathrm{Ba(OH)_2}\to2\mathrm{OH^-}$, phải nhân đôi.

## Khi nào dùng

Bài cho nồng độ acid/base mạnh: quy về $[\mathrm{H^+}]$ hoặc $[\mathrm{OH^-}]$ rồi lấy log. Với acid/base yếu cần dùng hằng số phân li (bài sau).

**Lỗi thường gặp:**
- Quên nhân đôi khi tính $\mathrm{Ba(OH)_2}$ hoặc $\mathrm{H_2SO_4}$ — sai vì mỗi phân tử tạo 2 ion $\mathrm{OH^-}$ (hoặc 2 $\mathrm{H^+}$).
- Dùng công thức acid mạnh $[\mathrm{H^+}]=C_a$ cho acid yếu — sai vì acid yếu chỉ phân li một phần, $[\mathrm{H^+}]$ nhỏ hơn nhiều so với nồng độ acid.
- Tính pH của base bằng $-\log C$ trực tiếp — sai vì với base phải qua $[\mathrm{OH^-}]$ và pOH rồi mới suy pH.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.su-dien-li-ph`</sub>

---

### 4. Acid - base yếu, hằng số Ka, Kb và dung dịch đệm
*Weak acids and bases, Ka, Kb and buffer solutions* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được pH của dung dịch acid yếu, base yếu từ hằng số phân li
- Giải thích cơ chế và tính được pH của dung dịch đệm

## Acid yếu không phân li hết

Acid yếu $\mathrm{HA}$ chỉ phân li một phần, đặc trưng bởi hằng số:
$$K_a = \frac{[\mathrm{H^+}][\mathrm{A^-}]}{[\mathrm{HA}]}, \qquad \mathrm{p}K_a = -\log K_a.$$
Với acid yếu nồng độ $C$ và độ phân li nhỏ, gần đúng:
$$[\mathrm{H^+}]\approx\sqrt{K_a\,C}, \qquad \mathrm{pH}\approx\tfrac12(\mathrm{p}K_a - \log C).$$
Công thức gần đúng này chỉ đúng khi độ phân li nhỏ (dưới ~5%), tức $C$ không quá loãng.

## Base yếu tương tự

Base yếu có $K_b$; liên hệ với acid liên hợp: $K_a\,K_b = K_w = 10^{-14}$, hay $\mathrm{p}K_a + \mathrm{p}K_b = 14$.

## Dung dịch đệm giữ pH ổn định

Trộn acid yếu $\mathrm{HA}$ với muối chứa base liên hợp $\mathrm{A^-}$ tạo **đệm**. Khi thêm chút acid, $\mathrm{A^-}$ hấp thụ; thêm chút base, $\mathrm{HA}$ trung hoà — nên pH gần như không đổi. Công thức Henderson - Hasselbalch:
$$\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\mathrm{A^-}]}{[\mathrm{HA}]}.$$
Khi $[\mathrm{A^-}]=[\mathrm{HA}]$ thì $\mathrm{pH}=\mathrm{p}K_a$: đệm hiệu quả nhất quanh giá trị này. Máu người là một hệ đệm $\mathrm{HCO_3^-}/\mathrm{H_2CO_3}$ giữ pH ~7,4.

## Khi nào dùng công thức nào

- Chỉ có acid yếu: dùng $[\mathrm{H^+}]=\sqrt{K_a C}$.
- Có cả acid yếu và base liên hợp (đệm): dùng Henderson - Hasselbalch.

**Lỗi thường gặp:**
- Dùng công thức acid mạnh $[\mathrm{H^+}]=C$ cho acid yếu — sai vì acid yếu phân li ít, $[\mathrm{H^+}]$ nhỏ hơn $C$ nhiều lần.
- Áp dụng $[\mathrm{H^+}]=\sqrt{K_aC}$ cho dung dịch đệm — sai vì trong đệm đã có sẵn base liên hợp $\mathrm{A^-}$, phải dùng Henderson - Hasselbalch.
- Nhầm $\mathrm{p}K_a$ với $K_a$ khi tính pH đệm — quên lấy $-\log$ của $K_a$.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.axit-bazo-yeu-ka-kb-dem`</sub>

---

### 5. Tích số tan và điều kiện tạo kết tủa
*Solubility product and conditions for precipitation* · THPT (lớp 10-12) · vn-gdpt-2018 · 40 phút · nang-cao

**Mục tiêu:**
- Viết được biểu thức tích số tan Ksp và tính độ tan từ Ksp
- Dự đoán được sự tạo thành kết tủa bằng cách so sánh thương số ion với Ksp

## Chất ít tan vẫn có cân bằng

Chất "không tan" thực ra tan một lượng cực nhỏ, tạo cân bằng giữa chất rắn và ion trong dung dịch bão hoà. Với $\mathrm{M_aX_b}(r)\rightleftharpoons a\mathrm{M^{n+}}+b\mathrm{X^{m-}}$:
$$K_{sp} = [\mathrm{M^{n+}}]^a[\mathrm{X^{m-}}]^b.$$
Chất rắn không vào biểu thức. $K_{sp}$ càng nhỏ, chất càng khó tan.

## Từ Ksp suy độ tan

Gọi độ tan (mol/L) là $S$. Ví dụ $\mathrm{AgCl}$: $[\mathrm{Ag^+}]=[\mathrm{Cl^-}]=S$ nên $K_{sp}=S^2 \Rightarrow S=\sqrt{K_{sp}}$. Với $\mathrm{Mg(OH)_2}$: $[\mathrm{Mg^{2+}}]=S$, $[\mathrm{OH^-}]=2S$ nên $K_{sp}=S(2S)^2=4S^3 \Rightarrow S=\sqrt[3]{K_{sp}/4}$. Chú ý hệ số 2 trong ion $\mathrm{OH^-}$ được bình phương.

## Dự đoán kết tủa: so Q với Ksp

Trộn hai dung dịch, tính **thương số ion** $Q$ (giống biểu thức $K_{sp}$ nhưng dùng nồng độ tức thời sau khi trộn):
- $Q > K_{sp}$: quá bão hoà $\Rightarrow$ **có kết tủa**;
- $Q = K_{sp}$: bão hoà, bắt đầu kết tủa;
- $Q < K_{sp}$: chưa kết tủa.
Nhớ tính nồng độ **sau khi pha trộn** (thể tích tăng làm loãng).

## Hiệu ứng ion chung

Thêm ion chung (ví dụ thêm $\mathrm{Cl^-}$ vào dung dịch $\mathrm{AgCl}$) làm giảm độ tan, vì cân bằng dịch về phía chất rắn để giữ $K_{sp}$ không đổi.

## Khi nào dùng

Bài hỏi độ tan: lập $S$ theo $K_{sp}$. Bài hỏi có kết tủa hay không: tính $Q$ sau trộn rồi so với $K_{sp}$.

**Lỗi thường gặp:**
- Đưa nồng độ chất rắn vào biểu thức $K_{sp}$ — sai vì chất rắn nguyên chất không xuất hiện trong biểu thức tích số tan.
- Quên bình phương hệ số ion khi lập độ tan (ví dụ $\mathrm{Mg(OH)_2}$ dùng $S^2$ thay vì $4S^3$) — cho độ tan sai.
- So $Q$ với $K_{sp}$ mà dùng nồng độ trước khi pha trộn — sai vì trộn hai dung dịch làm loãng, phải tính nồng độ sau trộn.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.tich-so-tan`</sub>

---

## Lớp 12 - Chương: Pin điện và điện phân

### 1. Thế điện cực chuẩn, sức điện động của pin và phương trình Nernst
*Standard electrode potential, cell emf and the Nernst equation* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Tính được sức điện động chuẩn của pin từ thế điện cực chuẩn và xác định cực âm, cực dương
- Vận dụng phương trình Nernst để tính thế điện cực khi nồng độ khác chuẩn

## Vì sao cặp oxi hoá - khử có "thế"

Mỗi cặp $\mathrm{M^{n+}}/\mathrm{M}$ có xu hướng nhận hay nhường electron khác nhau, đo bằng **thế điện cực chuẩn** $E^\circ$ (so với điện cực hydrogen quy ước $0$ V). $E^\circ$ càng lớn (dương), dạng oxi hoá càng dễ nhận electron (tính oxi hoá mạnh); $E^\circ$ càng âm, kim loại càng dễ bị oxi hoá (tính khử mạnh).

## Ghép hai điện cực thành pin

Trong pin Galvani, cặp có $E^\circ$ lớn hơn làm **cực dương (cathode, khử)**, cặp $E^\circ$ nhỏ hơn làm **cực âm (anode, oxi hoá)**. Sức điện động chuẩn:
$$E^\circ_{pin} = E^\circ_{(+)} - E^\circ_{(-)} > 0.$$
Hiệu này luôn dương với pin tự diễn biến; kim loại mạnh hơn (âm hơn) bị ăn mòn để đẩy electron ra mạch ngoài.

## Khi nồng độ khác chuẩn: phương trình Nernst

Thế thay đổi theo nồng độ. Ở 25$^\circ$C:
$$E = E^\circ - \frac{0{,}0592}{n}\log Q$$
với $n$ là số electron trao đổi, $Q$ là thương số phản ứng (tích nồng độ sản phẩm chia chất đầu, dạng oxi hoá - khử). Tăng nồng độ ion sản phẩm làm $Q$ tăng, $E$ giảm.

## Liên hệ với chiều phản ứng

$E_{pin} > 0$ nghĩa là phản ứng tự xảy ra ($\Delta G = -nFE < 0$). Đây là cầu nối giữa điện hoá và nhiệt động.

## Khi nào dùng

Bài cho bảng $E^\circ$: xác định cực, tính $E^\circ_{pin}$ bằng hiệu. Bài cho nồng độ khác 1 M: hiệu chỉnh bằng Nernst.

**Lỗi thường gặp:**
- Lấy $E^\circ_{pin}=E^\circ_{(-)}-E^\circ_{(+)}$ ra số âm — sai vì công thức là cực dương trừ cực âm, cho sức điện động dương.
- Nhầm anode là cực dương như trong bình điện phân — sai vì trong pin Galvani, anode (nơi oxi hoá) là cực **âm**.
- Quên chia cho số electron $n$ trong phương trình Nernst — làm sai mức hiệu chỉnh thế theo nồng độ.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.the-dien-cuc-pin-nernst`</sub>

---

### 2. Điện phân, định luật Faraday và ăn mòn kim loại
*Electrolysis, Faraday's law and metallic corrosion* · THPT (lớp 10-12) · vn-gdpt-2018 · 45 phút · nang-cao

**Mục tiêu:**
- Vận dụng định luật Faraday để tính khối lượng chất và thời gian trong điện phân
- Xác định thứ tự điện phân ở các điện cực và giải thích cơ chế ăn mòn điện hoá

## Điện phân: dùng điện để ép phản ứng

Điện phân dùng dòng điện một chiều buộc phản ứng oxi hoá - khử **không tự xảy ra** phải xảy ra. Tại **catode (cực âm)** xảy ra khử (nhận electron), tại **anode (cực dương)** xảy ra oxi hoá. Lưu ý dấu cực ngược với pin Galvani.

## Định luật Faraday định lượng

Số mol electron trao đổi liên hệ với điện lượng:
$$n_e = \frac{I\,t}{F}, \qquad m = \frac{A\,I\,t}{n\,F}$$
với $I$ (A), $t$ (giây), $A$ khối lượng mol, $n$ số electron trao đổi tạo 1 nguyên tử/phân tử chất, $F=96500$ C/mol. Đây là công cụ tính khối lượng kim loại bám catode, thể tích khí ở anode, hoặc thời gian điện phân.

## Thứ tự điện phân

- **Catode**: ion kim loại có tính oxi hoá mạnh (đứng sau trong dãy điện hoá, như $\mathrm{Cu^{2+}, Ag^+}$) bị khử trước; ion kim loại mạnh ($\mathrm{Na^+, K^+, Al^{3+}}$) không bị khử trong dung dịch, thay vào đó nước bị khử tạo $\mathrm{H_2}$.
- **Anode** (trơ): $\mathrm{Cl^-}$ bị oxi hoá trước, các gốc $\mathrm{SO_4^{2-}, NO_3^-}$ không bị oxi hoá nên nước bị oxi hoá tạo $\mathrm{O_2}$.

## Ăn mòn điện hoá

Khi hai kim loại khác nhau tiếp xúc trong dung dịch điện li, chúng tạo thành pin: kim loại hoạt động hơn (âm hơn) làm anode và **bị ăn mòn**, kim loại kém hoạt động được bảo vệ. Nguyên tắc này dùng để bảo vệ vỏ tàu bằng "anode hi sinh" (gắn Zn để bảo vệ Fe).

## Khi nào dùng

Bài điện phân cho $I, t$: dùng $n_e=It/F$ rồi phân bổ electron cho các ion theo thứ tự. Bài ăn mòn: xác định kim loại nào là anode để biết kim loại nào bị phá huỷ.

**Lỗi thường gặp:**
- Quên chia số mol electron cho số electron $n$ của phản ứng điện cực — ví dụ tính $n_{\mathrm{Cu}}=n_e$ thay vì $n_e/2$, cho khối lượng gấp đôi.
- Cho rằng $\mathrm{Na^+}$ hay $\mathrm{Al^{3+}}$ bị khử ở catode trong dung dịch nước — sai vì nước bị khử trước, tạo $\mathrm{H_2}$.
- Nhầm kim loại kém hoạt động bị ăn mòn — sai vì trong pin ăn mòn, kim loại **hoạt động hơn** (đóng vai anode) mới bị phá huỷ.

<sub>`lesson.chemistry.vn-thpt-chemistry-daicuong-voco.dien-phan-faraday-an-mon`</sub>

---

## Unit 10: Spectroscopy and Structure Determination

### 1. Phổ khối lượng trong xác định cấu trúc hữu cơ
*Mass spectrometry in organic structure determination* · THPT (lớp 10-12) · ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Xác định được phân tử khối từ pic ion phân tử và đếm số carbon từ pic M+1
- Nhận biết được chlorine và bromine qua tỉ lệ pic M và M+2
- Suy luận được cấu trúc từ các mảnh phân mảnh đặc trưng

## Ba tầng thông tin trên một phổ đồ

**Tầng 1 — pic ion phân tử** cho phân tử khối. Quy tắc nitrogen: nếu $M$ là số **lẻ** thì phân tử chứa số lẻ nguyên tử N; nếu $M$ chẵn thì không có N hoặc có số chẵn.

**Tầng 2 — cụm pic đồng vị** cho biết nguyên tố có mặt:

$$\text{số C} \approx \frac{\text{chiều cao } (M{+}1)}{\text{chiều cao } M}\times \frac{100}{1{,}1}$$

vì $\mathrm{^{13}C}$ chiếm 1,1% carbon tự nhiên. Với M+2:

- $M : M{+}2 \approx 3 : 1$ ⇒ có **một** Cl.
- $M : M{+}2 \approx 1 : 1$ ⇒ có **một** Br.
- $M : M{+}2 : M{+}4 \approx 9 : 6 : 1$ ⇒ có **hai** Cl.

**Tầng 3 — các mảnh** cho biết bộ khung. Chỉ mảnh **cation** xuất hiện; mảnh trung hoà vô hình nhưng suy được từ hiệu $M - m/z$.

## Các hiệu số cần thuộc

| Hiệu | Mảnh mất | Gợi ý cấu trúc |
|---|---|---|
| 15 | $\mathrm{CH_3}$ | có nhóm methyl |
| 17 | $\mathrm{OH}$ | acid hoặc alcohol |
| 18 | $\mathrm{H_2O}$ | alcohol (dễ tách nước) |
| 28 | $\mathrm{CO}$ hoặc $\mathrm{C_2H_4}$ | carbonyl hoặc mạch dài |
| 29 | $\mathrm{CHO}$ hoặc $\mathrm{C_2H_5}$ | aldehyde hoặc ethyl |
| 45 | $\mathrm{COOH}$ | acid carboxylic |

## Nguyên tắc bền của cation

Mảnh nào cho **cation bền hơn** thì pic đó cao hơn. Thứ tự bền: bậc ba > bậc hai > bậc một; cation acyl $\mathrm{RCO^+}$ rất bền nhờ cộng hưởng; cation benzyl $\mathrm{C_6H_5CH_2^+}$ ($m/z = 91$) cực bền nhờ giải toả vào vòng thơm — pic 91 gần như là chữ kí của hợp chất chứa nhóm benzyl.

## Giới hạn

Một số phân tử phân mảnh mạnh tới mức **không thấy pic ion phân tử**, khiến không xác định được $M$. Khi đó phải dùng kĩ thuật ion hoá mềm hơn, hoặc kết hợp với IR và NMR.

**Lỗi thường gặp:**
- Coi pic cao nhất trên phổ là pic ion phân tử — sai vì pic cao nhất là pic cơ sở, ứng với mảnh bền nhất; pic ion phân tử là pic có m/z lớn nhất (không kể pic đồng vị) và có thể rất thấp.
- Nhìn thấy pic M+2 rồi kết luận ngay có chlorine — sai vì brom cũng cho M+2; phải đọc tỉ lệ chiều cao, 3:1 cho một Cl còn khoảng 1:1 cho một Br.
- Kì vọng thấy pic của mảnh trung hoà bị tách ra — sai vì phổ kế chỉ tách và ghi nhận hạt mang điện; mảnh trung hoà chỉ suy ra gián tiếp qua hiệu khối lượng.
- Dùng pic M+1 để đếm carbon mà quên rằng hydrogen cũng có đồng vị — thực tế đóng góp của ²H rất nhỏ (0,015%) nên bỏ qua được, nhưng với hợp chất chứa nhiều N hoặc S thì công thức đếm carbon đơn giản sẽ cho kết quả sai lệch.

<sub>`lesson.chemistry.intl-spectroscopy.pho-khoi-huu-co`</sub>

---

### 2. Phổ hồng ngoại IR và phổ NMR proton
*Infrared spectroscopy and proton NMR* · THPT (lớp 10-12) · ib, a-level · 55 phút · chuyen-sau

**Mục tiêu:**
- Nhận diện được nhóm chức từ các dải hấp thụ đặc trưng trên phổ IR
- Đọc được bốn thông tin của phổ NMR proton: số tín hiệu, độ dịch chuyển, tích phân và sự tách
- Kết hợp được dữ liệu IR, NMR và phổ khối để xác định cấu trúc một hợp chất chưa biết

## IR: nhận nhóm chức trong vài giây

Phân tử hấp thụ IR ở tần số cộng hưởng với dao động của liên kết. Điều kiện: dao động phải làm **thay đổi momen lưỡng cực** — đó là lí do $\mathrm{N_2}$ và $\mathrm{O_2}$ không hấp thụ IR và không phải khí nhà kính.

Các dải bắt buộc thuộc:

| Số sóng (cm⁻¹) | Liên kết | Đặc điểm |
|---|---|---|
| 3200-3600 | O-H alcohol | rộng, tù |
| 2500-3300 | O-H acid | rất rộng, chồng lên C-H |
| 3300-3500 | N-H amine | trung bình, có thể tách đôi |
| 2850-3100 | C-H | hầu như luôn có |
| 1670-1750 | C=O | mạnh, nhọn — dấu hiệu rõ nhất |
| 1600-1680 | C=C | yếu tới trung bình |

Chiến thuật đọc: tìm C=O trước (nhọn, mạnh, khó nhầm), rồi tìm O-H, rồi N-H.

## NMR proton: bốn câu hỏi

1. **Bao nhiêu tín hiệu?** = bao nhiêu môi trường proton khác nhau. Proton tương đương về đối xứng cho một tín hiệu chung.
2. **Ở đâu?** ($\delta$) = môi trường điện tử. $\mathrm{CH_3}$ alkane ~0,9; kề C=O ~2,1; kề O ~3,5; thơm 6,5-8; $\mathrm{CHO}$ ~9,5; $\mathrm{COOH}$ 10-12.
3. **Cao bao nhiêu?** (tích phân) = **tỉ lệ** số proton, không phải số tuyệt đối. Tỉ lệ 3:2:1 có thể là 3H:2H:1H hoặc 6H:4H:2H.
4. **Tách mấy vạch?** = quy tắc $n+1$. Singlet ⇒ không có láng giềng; triplet + quartet ⇒ nhóm ethyl $\mathrm{CH_3CH_2}$.

## Proton của OH và NH

Cho tín hiệu **rộng, không tách** vì trao đổi nhanh với dung môi. Kiểm chứng bằng cách lắc mẫu với $\mathrm{D_2O}$: tín hiệu **biến mất** do H bị thay bằng D. Đây là thí nghiệm chuẩn để khẳng định có nhóm OH hay NH.

## Quy trình phối hợp ba phổ

Phổ khối cho công thức phân tử và độ bất bão hoà. IR cho nhóm chức. NMR cho bộ khung carbon và cách ghép các mảnh lại. Ba nguồn dữ liệu phải **nhất quán** — nếu mâu thuẫn, giả thiết cấu trúc sai.

**Lỗi thường gặp:**
- Đọc chiều cao tích phân NMR là số proton tuyệt đối — sai vì tích phân chỉ cho tỉ lệ; tỉ lệ 2:3 có thể ứng với 2H:3H hoặc 4H:6H, phải đối chiếu với công thức phân tử từ phổ khối.
- Dùng vùng vân tay dưới 1500 cm⁻¹ để suy nhóm chức — sai vì vùng này quá phức tạp và chồng chéo; nó chỉ dùng để so khớp toàn bộ phổ với phổ chuẩn nhằm nhận diện chất cụ thể.
- Áp quy tắc n+1 cho proton của nhóm OH — sai vì proton OH trao đổi rất nhanh với dung môi nên không ghép spin với láng giềng, cho tín hiệu rộng không tách.
- Kết luận không có nhóm OH chỉ vì không thấy dải ở 3200-3600 cm⁻¹ — sai vì acid carboxylic cho dải O-H rất rộng trải từ 2500 tới 3300 cm⁻¹, dễ bị nhầm với nền C-H nếu không quan sát kĩ độ rộng.

<sub>`lesson.chemistry.intl-spectroscopy.pho-ir-va-nmr`</sub>

---

## Unit 11: Organic Mechanisms and Stereochemistry

### 1. Cơ chế thế nucleophin SN1 và SN2
*Nucleophilic substitution: SN1 and SN2 mechanisms* · THPT (lớp 10-12) · ib, a-level · 55 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được hai cơ chế SN1 và SN2 theo động học, lập thể và ảnh hưởng của bậc carbon
- Dự đoán được cơ chế ưu thế từ cấu trúc dẫn xuất halogen, nucleophile và dung môi
- Giải thích được sự nghịch chuyển cấu hình trong SN2 và sự racemic hoá trong SN1

## Cùng một sản phẩm, hai con đường

$$\mathrm{R{-}X + Nu^- \to R{-}Nu + X^-}$$

Phản ứng viết ra thì giống nhau, nhưng cơ chế khác hẳn và cho hệ quả lập thể trái ngược.

## SN2 — một bước, đồng bộ

Nucleophile tấn công từ phía **đối diện** nhóm đi ra (tấn công lưng, 180°). Liên kết mới hình thành đồng thời với liên kết cũ đứt.

- Động học: $v = k[\mathrm{RX}][\mathrm{Nu^-}]$, **bậc 2**.
- Lập thể: **nghịch chuyển hoàn toàn** cấu hình. Nếu chất đầu là $R$ thì sản phẩm là $S$ (khi thứ tự ưu tiên không đổi).
- Thứ tự tốc độ: $\mathrm{CH_3X} >$ **bậc một** > bậc hai $\gg$ bậc ba.

Lí do thứ tự này là **cản trở không gian**: càng nhiều nhóm alkyl quanh carbon thì nucleophile càng khó tiếp cận từ phía sau.

## SN1 — hai bước, qua carbocation

Bước chậm là sự tách $\mathrm{X^-}$ tạo carbocation phẳng; bước nhanh là nucleophile tấn công.

- Động học: $v = k[\mathrm{RX}]$, **bậc 1** — nucleophile không có trong biểu thức tốc độ vì nó tham gia sau bước chậm.
- Lập thể: carbocation phẳng bị tấn công **từ cả hai phía như nhau** ⇒ hỗn hợp **racemic**.
- Thứ tự tốc độ: bậc ba > bậc hai $\gg$ bậc một, đúng theo thứ tự bền của carbocation (hiệu ứng đẩy electron $+I$ và siêu liên hợp của nhóm alkyl).

## Bảng quyết định

| Yếu tố | Ưu tiên SN2 | Ưu tiên SN1 |
|---|---|---|
| Bậc carbon | bậc một | bậc ba |
| Nucleophile | mạnh ($\mathrm{OH^-, CN^-}$) | yếu ($\mathrm{H_2O}$, ROH) |
| Dung môi | phân cực **không** proton (aceton, DMSO) | phân cực **có** proton (nước, ethanol) |
| Nhóm đi ra | tốt với cả hai ($\mathrm{I^- > Br^- > Cl^-}$) | |

Dung môi có proton solvat hoá và làm "cùn" nucleophile mạnh, đồng thời ổn định carbocation — nên nó đẩy phản ứng về phía SN1.

## Ảnh hưởng của nhóm đi ra

Tốc độ thuỷ phân tăng theo $\mathrm{C{-}I > C{-}Br > C{-}Cl}$. Đây là chỗ **năng lượng liên kết thắng độ phân cực**: C-Cl phân cực hơn nhưng bền hơn nhiều (338 so với 238 kJ/mol của C-I), mà bước quyết định là bẻ liên kết.

**Lỗi thường gặp:**
- Cho rằng nucleophile luôn xuất hiện trong biểu thức tốc độ — sai vì trong SN1 nucleophile tham gia ở bước nhanh sau bước quyết định tốc độ, nên nồng độ của nó không ảnh hưởng tốc độ tổng thể.
- Dự đoán SN2 xảy ra dễ với dẫn xuất bậc ba vì carbocation bậc ba bền — sai vì lập luận độ bền carbocation chỉ áp cho SN1; SN2 không đi qua carbocation mà bị chặn bởi cản trở không gian của ba nhóm alkyl.
- Kết luận SN1 luôn cho sản phẩm racemic hoàn toàn — sai vì nhóm đi ra vẫn còn che một phía trong khoảnh khắc đầu (cặp ion), nên thực nghiệm thường thấy dư nhẹ sản phẩm nghịch chuyển chứ không phải tỉ lệ 50:50 chính xác.
- Sắp thứ tự tốc độ thuỷ phân theo độ phân cực liên kết C-X nên đặt C-Cl nhanh nhất — sai vì bước quyết định là bẻ liên kết, mà C-I có năng lượng liên kết thấp nhất nên iodoalkane phản ứng nhanh nhất.

<sub>`lesson.chemistry.intl-organic-mechanisms.sn1-va-sn2`</sub>

---

### 2. Cơ chế tách E1, E2 và cạnh tranh giữa thế với tách
*Elimination E1, E2 and the substitution-elimination competition* · THPT (lớp 10-12) · ib, a-level · 50 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được cơ chế E1 và E2 theo động học và yêu cầu hình học
- Vận dụng được quy tắc Zaitsev để xác định sản phẩm tách chính
- Dự đoán được tỉ lệ sản phẩm thế và tách theo bản chất base, dung môi và nhiệt độ

## Tách là đối thủ của thế

Cùng một chất đầu $\mathrm{R{-}X}$ và cùng một tác nhân $\mathrm{OH^-}$ có thể cho hai sản phẩm khác nhau:

- Vai trò **nucleophile** ⇒ tấn công carbon ⇒ **thế**, cho alcohol.
- Vai trò **base** ⇒ lấy proton beta ⇒ **tách**, cho alkene.

Cùng một tiểu phân, hai vai trò. Điều kiện phản ứng quyết định vai trò nào trội.

## E2 — một bước, có yêu cầu hình học

$$v = k[\mathrm{RX}][\mathrm{base}]$$

Base lấy $\mathrm{H}$ ở carbon **beta** trong khi $\mathrm{X}$ rời khỏi carbon **alpha**, đồng bộ. Yêu cầu quan trọng: H và X phải nằm **anti-periplanar** (cùng mặt phẳng, góc nhị diện 180°), vì chỉ khi đó orbital của liên kết C-H mới xen phủ tốt với orbital phản liên kết C-X để tạo liên kết pi.

Yêu cầu hình học này giải thích vì sao một số dẫn xuất vòng cyclohexane tách rất chậm: nhóm đi ra phải ở vị trí trục (axial).

## E1 — hai bước, qua carbocation

$$v = k[\mathrm{RX}]$$

Cùng carbocation trung gian với SN1, nên **E1 và SN1 luôn cạnh tranh nhau** và thường cho hỗn hợp. Không có yêu cầu hình học vì carbocation phẳng, liên kết C-H nào cạnh đó cũng xen phủ được.

## Điều khiển tỉ lệ thế/tách

| Yếu tố | Ưu tiên thế | Ưu tiên tách |
|---|---|---|
| Tác nhân | nucleophile mạnh, base **yếu** ($\mathrm{CN^-}$, $\mathrm{I^-}$) | base **mạnh** ($\mathrm{OH^-}$ trong ethanol, $\mathrm{RO^-}$) |
| Dung môi | nước | ethanol khan |
| Nhiệt độ | thấp | **cao** |
| Bậc carbon | bậc một | bậc ba |

Quy tắc thực hành của A-Level: $\mathrm{NaOH}$ **trong nước, đun nhẹ** ⇒ thế cho alcohol; $\mathrm{KOH}$ **trong ethanol, đun hồi lưu** ⇒ tách cho alkene. Nhiệt độ cao ưu tiên tách vì tách làm tăng số phân tử nên $\Delta S$ dương lớn, mà số hạng $-T\Delta S$ càng có lợi khi $T$ tăng.

## Zaitsev và ngoại lệ Hofmann

Base thường cho sản phẩm **Zaitsev** (alkene nhiều nhóm thế, bền hơn). Nhưng base **cồng kềnh** như $\mathrm{(CH_3)_3CO^-}$ không chen vào được vị trí trong, buộc phải lấy proton ở nhóm methyl biên, cho sản phẩm **Hofmann** ít thế hơn.

**Lỗi thường gặp:**
- Cho rằng OH⁻ chỉ có một vai trò cố định — sai vì cùng một ion vừa là nucleophile vừa là base; dung môi và nhiệt độ quyết định vai trò nào trội, nên cùng chất đầu cho hai sản phẩm khác nhau.
- Áp quy tắc Zaitsev cho mọi base — sai vì base cồng kềnh như tert-butoxide bị cản trở không gian nên lấy proton ở vị trí biên, cho sản phẩm Hofmann ít thế hơn.
- Bỏ qua yêu cầu anti-periplanar của E2 — sai vì nếu H beta và nhóm đi ra không thể xếp thành góc nhị diện 180° thì orbital không xen phủ được và phản ứng E2 không xảy ra, dù mọi yếu tố khác đều thuận lợi.
- Quên rằng but-2-ene có đồng phân hình học — sai vì mỗi carbon nối đôi mang hai nhóm thế khác nhau, điều kiện đủ để có cis và trans; báo một sản phẩm duy nhất là chưa đầy đủ.

<sub>`lesson.chemistry.intl-organic-mechanisms.e1-e2-va-canh-tranh`</sub>

---

### 3. Thế gốc tự do và cộng electrophin vào alkene
*Free radical substitution and electrophilic addition to alkenes* · THPT (lớp 10-12) · ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Mô tả được ba giai đoạn của cơ chế thế gốc tự do và giải thích vì sao sản phẩm là hỗn hợp
- Trình bày được cơ chế cộng electrophin và vai trò của carbocation trung gian
- Vận dụng được quy tắc Markovnikov và giải thích bằng độ bền carbocation

## Hai kiểu đứt liên kết

**Đồng li**: mỗi nguyên tử giữ một electron ⇒ hai gốc tự do. Cần ánh sáng UV hoặc nhiệt độ cao.

**Dị li**: một nguyên tử giữ cả cặp ⇒ một cation và một anion. Xảy ra trong dung môi phân cực.

Hai kiểu này dẫn tới hai họ cơ chế hoàn toàn khác nhau.

## Thế gốc tự do — halogen hoá alkane

Ba giai đoạn:

1. **Khơi mào**: $\mathrm{Cl_2 \xrightarrow{UV} 2Cl\cdot}$ (đồng li).
2. **Phát triển mạch** (hai bước lặp lại):
   $$\mathrm{Cl\cdot + CH_4 \to HCl + \cdot CH_3}$$
   $$\mathrm{\cdot CH_3 + Cl_2 \to CH_3Cl + Cl\cdot}$$
   Gốc $\mathrm{Cl\cdot}$ được tái tạo nên một photon có thể gây ra hàng nghìn lượt phản ứng.
3. **Tắt mạch**: hai gốc gặp nhau, ví dụ $\mathrm{\cdot CH_3 + \cdot CH_3 \to C_2H_6}$.

**Hệ quả quan trọng**: phương pháp này cho **hỗn hợp** $\mathrm{CH_3Cl}$, $\mathrm{CH_2Cl_2}$, $\mathrm{CHCl_3}$, $\mathrm{CCl_4}$ và cả sản phẩm tắt mạch. Vì thế nó gần như vô dụng trong tổng hợp chọn lọc — một điểm mà đề thi rất hay hỏi.

## Cộng electrophin — đặc trưng của alkene

Nối đôi C=C là vùng giàu electron pi lộ ra ngoài, nên nó **hút** tác nhân thiếu electron.

Cơ chế cộng HBr vào ethene:

1. Electron pi tấn công $\mathrm{H}$ của HBr, liên kết H-Br đứt dị li ⇒ carbocation + $\mathrm{Br^-}$.
2. $\mathrm{Br^-}$ tấn công carbocation ⇒ sản phẩm.

Với $\mathrm{Br_2}$ (phân tử không phân cực), nối đôi **cảm ứng** lưỡng cực khi phân tử tới gần — đây là lí do alkene làm mất màu nước brom ngay cả khi không có xúc tác.

## Markovnikov giải thích bằng carbocation

Cộng HBr vào propene có hai lối:

- H vào C1 ⇒ carbocation **bậc hai** $\mathrm{CH_3\overset{+}{C}HCH_3}$.
- H vào C2 ⇒ carbocation **bậc một** $\mathrm{CH_3CH_2\overset{+}{C}H_2}$.

Carbocation bậc hai bền hơn (nhóm alkyl đẩy electron và siêu liên hợp), năng lượng hoạt hoá thấp hơn nên đường đó chiếm ưu thế. Sản phẩm chính là **2-bromopropane**.

Vậy quy tắc Markovnikov không phải một quy tắc rời rạc phải học thuộc — nó là hệ quả trực tiếp của thứ tự bền carbocation.

**Lỗi thường gặp:**
- Học thuộc Markovnikov như một quy tắc rời rạc mà không nối với độ bền carbocation — sai về bản chất, và sẽ thất bại khi gặp trường hợp có nhóm hút electron làm đảo thứ tự bền của carbocation.
- Cho rằng halogen hoá alkane bằng gốc tự do là phương pháp tổng hợp tốt — sai vì gốc tái tạo liên tục làm phản ứng thế nhiều lần, cho hỗn hợp mono, di, tri và tetra halide cùng sản phẩm tắt mạch, rất khó tách.
- Vẽ mũi tên cong xuất phát từ nguyên tử thay vì từ cặp electron hoặc liên kết pi — sai vì mũi tên cong biểu diễn dòng chuyển của cặp electron; vẽ sai gốc mũi tên là lỗi bị trừ điểm trực tiếp trong đề A-Level.
- Cho rằng nước brom mất màu với mọi hydrocarbon — sai vì alkane không có mật độ electron pi để cảm ứng lưỡng cực trong phân tử Br₂; đây chính là cơ sở của phép thử phân biệt alkane với alkene.

<sub>`lesson.chemistry.intl-organic-mechanisms.cong-electrophin-va-goc-tu-do`</sub>

---

### 4. Thế electrophin vào vòng thơm và quy tắc định hướng
*Electrophilic aromatic substitution and directing effects* · THPT (lớp 10-12) · ib, a-level · 50 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao benzene tham gia phản ứng thế chứ không phải phản ứng cộng
- Mô tả được ba giai đoạn của cơ chế thế electrophin vào vòng thơm
- Dự đoán được vị trí thế thứ hai từ bản chất nhóm thế đã có trên vòng

## Vì sao benzene thế chứ không cộng

Alkene cộng dễ dàng vì phá một liên kết pi định xứ là rẻ. Benzene có hệ pi **phi định xứ** với năng lượng cộng hưởng khoảng 150 kJ/mol. Cộng sẽ phá vĩnh viễn tính thơm; **thế** thì phá tạm rồi khôi phục lại.

Bằng chứng thực nghiệm: nhiệt hydro hoá benzene chỉ là $-208$ kJ/mol thay vì $3\times(-120) = -360$ kJ/mol như dự đoán cho ba nối đôi độc lập. Chênh lệch 152 kJ/mol chính là độ bền thêm do cộng hưởng.

Hệ quả thực tế: benzene **không làm mất màu nước brom** ở điều kiện thường, khác hẳn alkene.

## Cơ chế ba giai đoạn

1. **Tạo electrophile mạnh** — luôn cần xúc tác:
   - Nitro hoá: $\mathrm{HNO_3 + H_2SO_4 \to NO_2^+ + HSO_4^- + H_2O}$.
   - Halogen hoá: $\mathrm{Br_2 + FeBr_3 \to Br^+ + FeBr_4^-}$.
   - Friedel-Crafts: $\mathrm{RCl + AlCl_3 \to R^+ + AlCl_4^-}$.
2. **Tấn công**: electron pi tấn công electrophile, tạo phức sigma — bước **chậm**, vì phải hi sinh tính thơm.
3. **Tách proton**: base lấy $\mathrm{H^+}$ ở carbon đó, **khôi phục tính thơm** — bước nhanh và là động lực của toàn bộ quá trình.

## Định hướng cho lần thế thứ hai

Nhóm thế đã có làm thay đổi mật độ electron trên vòng một cách **không đều**.

**Đẩy electron ⇒ hoạt hoá ⇒ ortho, para**: $\mathrm{-NH_2}$, $\mathrm{-OH}$, $\mathrm{-OR}$, $\mathrm{-R}$ (alkyl). Cặp electron tự do hoặc hiệu ứng $+I$ đẩy mật độ vào vòng, tập trung ở vị trí ortho và para.

**Hút electron ⇒ phản hoạt hoá ⇒ meta**: $\mathrm{-NO_2}$, $\mathrm{-CN}$, $\mathrm{-COOH}$, $\mathrm{-CHO}$. Chúng rút mật độ khỏi ortho và para mạnh hơn khỏi meta, nên meta trở thành vị trí ít nghèo nhất.

**Ngoại lệ quan trọng**: halogen $\mathrm{-Cl}$, $\mathrm{-Br}$ vừa **phản hoạt hoá** (hiệu ứng $-I$ mạnh do độ âm điện) vừa **định hướng ortho-para** (cặp electron tự do liên hợp vào vòng). Hai hiệu ứng ngược nhau tác động lên hai đại lượng khác nhau — đó là lí do halogen luôn được nêu riêng.

## Ứng dụng vào tổng hợp

Thứ tự đưa nhóm vào quyết định sản phẩm. Muốn được 3-nitrobenzoic acid phải oxi hoá toluene thành acid **trước** rồi mới nitro hoá (nhóm $\mathrm{-COOH}$ định hướng meta). Làm ngược lại sẽ được 4-nitrobenzoic acid.

**Lỗi thường gặp:**
- Cho rằng benzene làm mất màu nước brom như alkene — sai vì hệ pi phi định xứ của benzene có năng lượng cộng hưởng khoảng 150 kJ/mol, đủ bền để không cộng brom nếu không có xúc tác halogen carrier.
- Áp quy tắc định hướng theo nhóm có trong sản phẩm cuối thay vì nhóm đang có trên vòng — sai vì hiệu ứng điện tử chỉ phát huy khi nhóm đã gắn trên vòng tại thời điểm electrophile tấn công.
- Xếp halogen vào nhóm định hướng meta vì nó phản hoạt hoá — sai vì phản hoạt hoá và định hướng là hai hiệu ứng khác nhau; halogen phản hoạt hoá do -I nhưng vẫn định hướng ortho-para nhờ cặp electron tự do liên hợp vào vòng.
- Bỏ qua xúc tác khi viết phương trình halogen hoá hay Friedel-Crafts — sai vì Br₂ và RCl không đủ mạnh để phá tính thơm; phải có acid Lewis như FeBr₃ hoặc AlCl₃ tạo electrophile mạnh trước.

<sub>`lesson.chemistry.intl-organic-mechanisms.the-electrophin-vong-thom`</sub>

---

### 5. Đồng phân lập thể và hoạt tính quang học
*Stereoisomerism and optical activity* · THPT (lớp 10-12) · ib, a-level · 50 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được đồng phân hình học và đồng phân quang học theo nguyên nhân sinh ra chúng
- Gán được cấu hình R/S bằng quy tắc Cahn - Ingold - Prelog và cấu hình E/Z cho nối đôi
- Tính được số đồng phân lập thể tối đa và nhận diện hợp chất meso

## Hai nguồn gốc của đồng phân lập thể

**Đồng phân hình học (cis/trans, E/Z)** sinh ra từ sự **hạn chế quay**: liên kết pi hoặc vòng ngăn hai nhóm hoán đổi vị trí. Điều kiện: mỗi carbon nối đôi phải mang **hai nhóm khác nhau**.

**Đồng phân quang học** sinh ra từ **tính không đối xứng gương**. Điều kiện thường gặp: có carbon gắn bốn nhóm khác nhau.

Hai loại này khác nhau về tính chất: đồng phân hình học có nhiệt độ sôi, nhiệt độ nóng chảy và momen lưỡng cực **khác nhau** nên tách được bằng chưng cất; đồng phân đối quang có mọi tính chất vật lí **giống hệt** nên rất khó tách.

## Quy tắc CIP để gán R/S

1. Xếp hạng bốn nhóm thế theo **số hiệu nguyên tử** của nguyên tử gắn trực tiếp, lớn nhất là ưu tiên $a$.
2. Nếu bằng nhau, so tiếp lớp nguyên tử kế bên, lần lượt cho tới khi phân định.
3. Liên kết đôi tính như **hai** liên kết đơn tới cùng nguyên tử đó.
4. Quay phân tử sao cho nhóm ưu tiên **thấp nhất** ($d$) hướng ra xa người quan sát.
5. Đi từ $a \to b \to c$: cùng chiều kim đồng hồ là **R**, ngược chiều là **S**.

Cùng bộ quy tắc xếp hạng đó áp cho hai carbon nối đôi cho danh pháp E/Z: hai nhóm ưu tiên cùng phía là **Z**, khác phía là **E**. Danh pháp E/Z chính xác hơn cis/trans vì áp dụng được cả khi bốn nhóm thế đều khác nhau.

## Đếm đồng phân

Với $n$ tâm lập thể **không tương đương**, số đồng phân lập thể tối đa là $2^n$. Nhưng nếu phân tử có **đối xứng nội** thì con số thực nhỏ hơn.

Acid tartaric có 2 tâm lập thể nên dự đoán $2^2 = 4$; thực tế chỉ có **3** dạng: một cặp đối quang $(R,R)$ và $(S,S)$, cộng dạng **meso** $(R,S)$ — dạng này có mặt phẳng gương nội phân tử nên trùng ảnh gương của chính nó và **không quay** ánh sáng phân cực.

## Vì sao điều này quan trọng

Thụ thể sinh học tự nó bất đối xứng, nên nó "cầm" hai đối quang khác nhau như tay phải và tay trái. Hệ quả có thể nghiêm trọng: một đối quang của thalidomide có tác dụng an thần, đối quang kia gây quái thai. Đó là lí do dược phẩm hiện đại phải kiểm soát cấu hình tuyệt đối.

**Lỗi thường gặp:**
- Luôn dùng công thức 2ⁿ mà không kiểm tra đối xứng nội phân tử — sai vì khi phân tử có mặt phẳng gương nội, một số cấu hình trùng nhau và số đồng phân thực tế nhỏ hơn; acid tartaric có 3 chứ không phải 4.
- Đồng nhất hợp chất meso với hỗn hợp racemic vì cả hai đều không quay ánh sáng — sai vì meso là một chất tinh khiết có bù trừ nội phân tử, còn racemic là hỗn hợp hai chất và về nguyên tắc có thể tách bằng phương pháp bất đối xứng.
- Quên đưa nhóm ưu tiên thấp nhất ra xa trước khi đọc chiều quay R/S — sai vì nếu nhóm d hướng về phía người quan sát thì chiều đọc được sẽ ngược, cho kết quả trái hoàn toàn với cấu hình thật.
- Cho rằng cứ có nối đôi C=C là có đồng phân hình học — sai vì nếu một carbon nối đôi mang hai nhóm thế giống nhau, ví dụ trong 1,1-dicloroethene, thì hoán đổi không tạo cấu trúc mới.

<sub>`lesson.chemistry.intl-organic-mechanisms.dong-phan-lap-the`</sub>

---

### 6. Tổng hợp hữu cơ nhiều bước và phân tích ngược
*Multi-step organic synthesis and retrosynthetic analysis* · THPT (lớp 10-12) · ib, a-level · 55 phút · chuyen-sau

**Mục tiêu:**
- Xây dựng được lộ trình tổng hợp nhiều bước bằng phương pháp phân tích ngược
- Lựa chọn được thuốc thử và điều kiện phù hợp cho mỗi phép chuyển hoá nhóm chức
- Đánh giá được hiệu suất tổng và tính kinh tế nguyên tử của một lộ trình

## Nghĩ ngược để làm xuôi

Đi xuôi từ chất đầu dễ lạc vào vô số ngã rẽ. Đi ngược từ **phân tử đích** thì mỗi bước chỉ có vài lựa chọn hợp lí.

Câu hỏi ở mỗi bước ngược: "Chất nào chỉ cần **một** phản ứng đã biết là thành chất này?"

## Bản đồ chuyển hoá tối thiểu cần thuộc

| Từ | Sang | Thuốc thử và điều kiện |
|---|---|---|
| haloalkane | alcohol | NaOH loãng, nước, đun |
| haloalkane | alkene | KOH, ethanol, đun hồi lưu |
| haloalkane | nitrile (**+1 C**) | KCN, ethanol, đun |
| haloalkane | amine | $\mathrm{NH_3}$ đặc dư, ethanol, ống hàn kín |
| alkene | alcohol | $\mathrm{H_2O}$, $\mathrm{H_3PO_4}$, hơi nước, 300 °C |
| alcohol bậc 1 | aldehyde | $\mathrm{K_2Cr_2O_7}$/$\mathrm{H_2SO_4}$, **chưng cất ngay** |
| alcohol bậc 1 | acid | $\mathrm{K_2Cr_2O_7}$/$\mathrm{H_2SO_4}$, **đun hồi lưu** |
| alcohol bậc 2 | ketone | $\mathrm{K_2Cr_2O_7}$/$\mathrm{H_2SO_4}$ |
| nitrile | acid | HCl loãng, đun hồi lưu |
| nitrile | amine (**+1 C**) | $\mathrm{LiAlH_4}$ hoặc $\mathrm{H_2}$/Ni |
| carbonyl | alcohol (**+1 C**) | HCN/KCN rồi thuỷ phân |

Chú ý cặp đối lập **chưng cất ngay** với **đun hồi lưu** — cùng thuốc thử nhưng cho hai sản phẩm khác nhau. Chưng cất tách aldehyde ra khỏi hỗn hợp trước khi nó bị oxi hoá tiếp; hồi lưu giữ nó lại trong bình để oxi hoá tới cùng.

## Ba nguyên tắc thiết kế

1. **Đếm carbon trước tiên**. Nếu số carbon tăng, phải có bước KCN hoặc Grignard. Đây là điều kiện lọc mạnh nhất.
2. **Càng ít bước càng tốt**: 5 bước với hiệu suất 80% mỗi bước cho tổng chỉ $0{,}8^5 = 33\%$.
3. **Chú ý tính chọn lọc**: nếu phân tử có hai nhóm chức, phải bảo vệ một nhóm hoặc chọn thuốc thử chỉ tác dụng với nhóm kia.

## Với hợp chất thơm

Thứ tự đưa nhóm vào quyết định vị trí (xem bài về định hướng). Luôn hỏi: "Nhóm nào cần vào trước để định hướng đúng cho nhóm sau?"

**Lỗi thường gặp:**
- Thiết kế lộ trình mà không đếm số carbon của chất đầu và chất đích — sai vì nếu số carbon thay đổi thì bắt buộc phải có bước kéo dài mạch bằng KCN hoặc Grignard; bỏ qua bước này làm cả lộ trình không thể dẫn tới đích.
- Dùng đun hồi lưu khi muốn dừng lại ở aldehyde — sai vì hồi lưu giữ aldehyde trong bình và nó bị oxi hoá tiếp thành acid; muốn thu aldehyde phải chưng cất ngay để tách nó ra khỏi tác nhân oxi hoá.
- Cộng hiệu suất các bước thay vì nhân — sai vì mỗi bước chỉ chuyển hoá được một phần lượng chất từ bước trước, nên hiệu suất tổng là tích chứ không phải trung bình cộng.
- Bỏ qua thứ tự khi tổng hợp hợp chất thơm hai nhóm thế — sai vì quy tắc định hướng chỉ áp cho nhóm đã có trên vòng; đảo thứ tự các bước sẽ cho đồng phân vị trí khác.

<sub>`lesson.chemistry.intl-organic-mechanisms.tong-hop-nhieu-buoc`</sub>

---

## Unit 12: Lattice Energetics and Transition Metals

### 1. Chu trình Born - Haber và enthalpy mạng lưới
*The Born-Haber cycle and lattice enthalpy* · THPT (lớp 10-12) · ib, a-level · 55 phút · chuyen-sau

**Mục tiêu:**
- Xây dựng được chu trình Born - Haber đầy đủ cho hợp chất ion đơn giản
- Tính được enthalpy mạng lưới từ các đại lượng đo được bằng thực nghiệm
- Giải thích được sự phụ thuộc của enthalpy mạng lưới vào điện tích và bán kính ion

## Vấn đề không đo được

Không thí nghiệm nào tách được tinh thể NaCl thành các ion khí riêng lẻ và đo nhiệt. Chu trình Born - Haber giải quyết bằng cách đi vòng qua những đại lượng **đo được**, rồi dùng định luật Hess.

## Các chặng của chu trình cho NaCl

Đi từ đơn chất tới tinh thể theo hai đường:

Đường trực tiếp: $\Delta H_f^\circ(\mathrm{NaCl}) = -411$ kJ/mol.

Đường vòng gồm năm chặng:

1. Nguyên tử hoá Na: $+107$
2. Ion hoá thứ nhất Na: $+496$
3. Nguyên tử hoá $\tfrac{1}{2}\mathrm{Cl_2}$: $+122$
4. Ái lực electron của Cl: $-349$
5. Enthalpy mạng lưới: $\Delta H_{\text{lat}}$ (cần tìm)

Áp định luật Hess:

$$\Delta H_f = \Delta H_{at}(\mathrm{Na}) + IE_1 + \Delta H_{at}(\mathrm{Cl}) + EA_1 + \Delta H_{\text{lat}}$$

## Hai quy ước dấu — nguồn nhầm lẫn lớn nhất

- **Quy ước tạo thành** (formation): ion khí → tinh thể, giá trị **âm**.
- **Quy ước phân li** (dissociation): tinh thể → ion khí, giá trị **dương**.

AP và nhiều sách Mỹ dùng quy ước phân li; Cambridge dùng quy ước tạo thành. Luôn đọc kĩ đề nói "lattice formation" hay "lattice dissociation" trước khi đặt dấu.

## Enthalpy mạng lưới phụ thuộc gì

Từ định luật Coulomb:

$$|\Delta H_{\text{lat}}| \propto \frac{|z_+ z_-|}{r_+ + r_-}$$

- **Điện tích** tác động mạnh hơn vì nó vào dưới dạng tích: MgO ($2\times2$) có mạng lưới khoảng $-3800$, gấp hơn bốn lần NaCl ($-787$).
- **Bán kính** nhỏ ⇒ ion gần nhau ⇒ mạng lưới lớn hơn. Đó là lí do LiF có mạng lưới lớn hơn CsI rất nhiều.

## Kiểm tra tính ion bằng chu trình

So giá trị Born - Haber (thực nghiệm) với giá trị tính lí thuyết theo mô hình ion điểm. Chênh lệch càng lớn thì hợp chất càng mang **tính cộng hoá trị**, do cation phân cực hoá anion (quy tắc Fajans). Với AgI chênh lệch rất lớn; với NaCl gần như trùng khớp.

**Lỗi thường gặp:**
- Quên nhân đôi enthalpy nguyên tử hoá và ái lực electron của halogen trong hợp chất MX₂ — sai vì chu trình phải tạo đủ hai mol ion X⁻ khí; bỏ sót hệ số làm kết quả lệch vài trăm kJ.
- Dùng ái lực electron thứ hai với dấu âm — sai vì thêm electron vào ion đã tích điện âm phải thắng lực đẩy tĩnh điện, nên EA₂ luôn dương (ví dụ EA₂ của O là +844 kJ/mol).
- Lẫn lộn hai quy ước dấu của enthalpy mạng lưới — sai vì quy ước tạo thành cho giá trị âm còn quy ước phân li cho giá trị dương; dùng nhầm sẽ đảo dấu toàn bộ và cho kết luận vô lí về độ bền tinh thể.
- Cho rằng enthalpy mạng lưới chỉ phụ thuộc bán kính ion — sai vì điện tích vào công thức dưới dạng tích z₊z₋ nên tác động mạnh hơn; MgO và NaF có kích thước ion tương tự nhưng mạng lưới chênh nhau khoảng bốn lần.

<sub>`lesson.chemistry.intl-energetics-transition.chu-trinh-born-haber`</sub>

---

### 2. Enthalpy hidrat hoá và enthalpy hoà tan
*Enthalpies of hydration and of solution* · THPT (lớp 10-12) · ib, a-level · 50 phút · chuyen-sau

**Mục tiêu:**
- Xây dựng được chu trình năng lượng liên hệ enthalpy hoà tan với mạng lưới và hidrat hoá
- Giải thích được xu hướng của enthalpy hidrat hoá theo bán kính và điện tích ion
- Phân tích được vì sao một số muối tan dù quá trình thu nhiệt

## Hoà tan là cuộc đấu giữa hai đại lượng lớn

Để hoà tan một tinh thể ion, phải:

1. **Phá mạng lưới**: tốn năng lượng, độ lớn hàng nghìn kJ/mol (thu nhiệt).
2. **Hidrat hoá các ion**: giải phóng năng lượng, cũng hàng nghìn kJ/mol (toả nhiệt).

$$\Delta H_{\text{hoà tan}} = -\Delta H_{\text{lat(tạo thành)}} + \sum \Delta H_{\text{hidrat}}$$

Hai số lớn gần bằng nhau, hiệu số nhỏ. Đó là lí do $\Delta H_{\text{hoà tan}}$ có thể dương hoặc âm với biên độ chỉ vài chục kJ/mol, và tại sao phép tính này rất nhạy với sai số làm tròn.

## Enthalpy hidrat hoá phụ thuộc gì

Cùng một logic Coulomb như mạng lưới, nhưng lần này là tương tác **ion - lưỡng cực** với nước:

$$|\Delta H_{\text{hidrat}}| \propto \frac{|z|}{r}$$

Do đó:

- Đi xuống nhóm 1: $\mathrm{Li^+}$ ($-519$) → $\mathrm{Cs^+}$ ($-276$), độ lớn giảm vì bán kính tăng.
- Cùng bán kính, điện tích lớn hơn cho hidrat hoá mạnh hơn nhiều: $\mathrm{Mg^{2+}}$ ($-1921$) so với $\mathrm{Na^+}$ ($-406$).

Ít ai ngờ: $\mathrm{Li^+}$ nhỏ nhất nhưng **ion hidrat hoá của nó lớn nhất**, vì nó kéo nhiều lớp nước quanh mình. Đây là lí do $\mathrm{Li^+}$ di chuyển chậm nhất trong dung dịch dù bản thân nhỏ nhất.

## Vì sao muối thu nhiệt vẫn tan

$\mathrm{NH_4NO_3}$ có $\Delta H_{\text{hoà tan}} = +25$ kJ/mol nhưng tan rất tốt. Lí do nằm ở **entropy**: mạng tinh thể trật tự cao chuyển thành các ion phân tán trong dung dịch, $\Delta S$ dương lớn. Số hạng $-T\Delta S$ đủ âm để $\Delta G$ âm.

Nhưng có giới hạn: nếu $\Delta H_{\text{hoà tan}}$ quá dương (như với $\mathrm{BaSO_4}$, nơi cả hai ion đều mang hai điện tích nên mạng lưới rất lớn), entropy không bù nổi và muối không tan.

## Xu hướng độ tan trong nhóm 2

Sulfate nhóm 2 **giảm** độ tan khi đi xuống nhóm ($\mathrm{MgSO_4}$ tan, $\mathrm{BaSO_4}$ không tan). Hydroxide thì ngược lại, **tăng** độ tan.

Giải thích: $\mathrm{SO_4^{2-}}$ rất lớn nên enthalpy mạng lưới thay đổi ít khi cation to dần, trong khi enthalpy hidrat hoá của cation giảm mạnh. Với $\mathrm{OH^-}$ nhỏ thì ngược lại, mạng lưới nhạy hơn. Nguyên tắc chung: **đại lượng nào nhạy hơn với sự thay đổi bán kính cation thì đại lượng đó quyết định xu hướng.**

**Lỗi thường gặp:**
- Cộng thẳng enthalpy mạng lưới tạo thành (số âm) vào tổng hidrat hoá — sai vì chu trình đòi hỏi đi ngược chiều mạng lưới tạo thành, tức phải đổi dấu; giữ nguyên dấu sẽ ra khoảng −1571 kJ/mol, vô lí với một muối gần như không toả nhiệt khi tan.
- Cho rằng muối có ΔH(hoà tan) dương thì không tan — sai vì tiêu chuẩn tan là ΔG âm; entropy tăng khi mạng tinh thể phân rã thành ion thường đủ để bù, như trường hợp NH₄NO₃.
- Kết luận Li⁺ di chuyển nhanh nhất trong dung dịch vì nó nhỏ nhất — sai vì mật độ điện tích cao khiến nó kéo theo nhiều lớp nước hidrat, làm ion hidrat hoá của Li⁺ lớn nhất trong nhóm 1 và di chuyển chậm nhất.
- Giải thích xu hướng độ tan của sulfate và hydroxide nhóm 2 bằng cùng một lập luận — sai vì hai anion có kích thước rất khác nhau, nên đại lượng nhạy hơn với bán kính cation là khác nhau và hai xu hướng đi ngược chiều.

<sub>`lesson.chemistry.intl-energetics-transition.enthalpy-hidrat-hoa-va-hoa-tan`</sub>

---

### 3. Kim loại chuyển tiếp và phức chất
*Transition metals and complex ions* · THPT (lớp 10-12) · ib, a-level · 55 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được bốn tính chất đặc trưng của kim loại chuyển tiếp từ cấu hình d chưa bão hoà
- Giải thích được nguồn gốc màu sắc của phức chất bằng sự tách mức d
- Vận dụng được hằng số bền để dự đoán chiều của phản ứng thay thế phối tử

## Bốn tính chất và một nguyên nhân chung

Mọi đặc trưng của kim loại chuyển tiếp đều bắt nguồn từ **phân lớp d chưa bão hoà, với mức năng lượng gần mức s**:

1. **Nhiều số oxi hoá**: electron $4s$ và $3d$ năng lượng sát nhau nên có thể mất số lượng khác nhau. Mn từ $+2$ tới $+7$.
2. **Tạo phức**: orbital $d$ trống nhận cặp electron của phối tử.
3. **Có màu**: xem dưới.
4. **Xúc tác**: nhờ khả năng đổi số oxi hoá thuận nghịch (xúc tác đồng thể) hoặc hấp phụ trên bề mặt (dị thể).

**Ngoại lệ cần nhớ**: $\mathrm{Sc^{3+}}$ ($3d^0$) và $\mathrm{Zn^{2+}}$ ($3d^{10}$) đều **không màu** và không có tính chất chuyển tiếp, vì không có sự chuyển electron d-d.

## Nguồn gốc màu sắc

Trong ion tự do, năm orbital $d$ suy biến. Khi phối tử tiến lại (thường theo bát diện), chúng đẩy các orbital hướng thẳng vào mình lên cao hơn:

$$d_{z^2},\ d_{x^2-y^2} \;(\text{cao}) \qquad d_{xy},\ d_{xz},\ d_{yz} \;(\text{thấp})$$

Electron hấp thụ photon để nhảy lên mức cao; **màu quan sát được là màu bù** của màu bị hấp thụ. $\mathrm{[Cu(H_2O)_6]^{2+}}$ hấp thụ vùng đỏ - cam nên trông xanh lam.

Ba yếu tố đổi $\Delta$ ⇒ đổi màu: **bản chất phối tử** (dãy quang phổ hoá: $\mathrm{I^- < Br^- < Cl^- < F^- < H_2O < NH_3 < CN^- < CO}$), **số oxi hoá** của kim loại, và **số phối trí**.

## Spin cao hay spin thấp

So $\Delta$ với năng lượng ghép đôi $P$:

- $\Delta < P$ (trường yếu): electron thà lên mức cao còn hơn ghép đôi ⇒ **spin cao**, nhiều electron độc thân, thuận từ mạnh.
- $\Delta > P$ (trường mạnh, như $\mathrm{CN^-}$, CO): ghép đôi ở mức thấp ⇒ **spin thấp**.

Đo momen từ cho biết số electron độc thân: $\mu = \sqrt{n(n+2)}$ magneton Bohr.

## Thay thế phối tử và hiệu ứng chelat

Phản ứng thay phối tử là cân bằng với hằng số bền $K_{\text{stab}}$. Phối tử ở cuối dãy quang phổ hoá thường đẩy được phối tử đầu dãy.

Phối tử **đa càng** (EDTA sáu càng, ethylenediamine hai càng) cho phức bền hơn hẳn — chủ yếu vì một phân tử EDTA thay thế sáu phân tử nước, làm **tăng số tiểu phân tự do** nên $\Delta S$ dương lớn. Đây là hiệu ứng nhiệt động chứ không phải do liên kết mạnh hơn.

**Lỗi thường gặp:**
- Xếp Zn vào kim loại chuyển tiếp vì nó nằm trong khối d — sai vì Zn²⁺ có cấu hình 3d¹⁰ đầy đủ nên không có chuyển electron d-d, hợp chất của nó không màu và nó chỉ có một số oxi hoá bền.
- Nói màu quan sát được chính là màu bị hấp thụ — sai vì mắt nhìn thấy phần ánh sáng còn lại sau khi phức đã hấp thụ; màu quan sát là màu bù của màu bị hấp thụ trên vòng tròn màu.
- Giải thích hiệu ứng chelat bằng 'liên kết phối trí mạnh hơn' — sai vì enthalpy của liên kết kim loại - nitrogen trong ethylenediamine gần bằng trong ammonia; nguồn gốc chính là entropy, vì một phối tử đa càng giải phóng nhiều phân tử nước.
- Cho rằng mọi phức bát diện của Fe³⁺ đều spin cao — sai vì phụ thuộc phối tử: với H₂O trường yếu thì Δ < P cho spin cao (5 electron độc thân), nhưng với CN⁻ trường mạnh thì Δ > P cho spin thấp (1 electron độc thân).

<sub>`lesson.chemistry.intl-energetics-transition.kim-loai-chuyen-tiep-va-phuc-chat`</sub>

---

## Unit 1: Atomic Structure and Properties

### 1. Mol, hằng số Avogadro và tính toán định lượng
*The mole, Avogadro constant and stoichiometric calculations* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Giải thích được vì sao hoá học cần một đơn vị đếm hạt riêng và mol được định nghĩa như thế nào sau cải cách SI 2019
- Vận dụng được sơ đồ khối lượng - mol - số hạt để chuyển đổi giữa các đại lượng trong một bài toán tỉ lượng
- Xác định được chất giới hạn và tính được hiệu suất phần trăm của phản ứng

## Vì sao hoá học cần một đơn vị đếm riêng

Phản ứng xảy ra giữa từng hạt: một nguyên tử Mg nhường hai electron cho một nguyên tử O. Nhưng trong phòng thí nghiệm ta không đếm được hạt, ta chỉ cân được khối lượng. Mol là chiếc cầu nối hai thế giới đó.

## Định nghĩa hiện hành

Trước 2019, mol được neo vào 12 g carbon-12. Từ tháng 5 năm 2019, SI đảo ngược: hằng số Avogadro được **ấn định** bằng $N_A = 6{,}02214076\times10^{23}\ \mathrm{mol^{-1}}$, và mol là lượng chất chứa đúng bấy nhiêu thực thể. Hệ quả tinh tế: hằng số khối lượng mol $M_u$ không còn đúng bằng $1\ \mathrm{g\,mol^{-1}}$ một cách tuyệt đối, nhưng sai khác nhỏ hơn $10^{-9}$ nên mọi tính toán phổ thông vẫn dùng $M(\mathrm{^{12}C}) = 12\ \mathrm{g\,mol^{-1}}$.

## Ba con đường vào mol

$$n = \frac{m}{M} = \frac{N}{N_A} = \frac{V_{\text{khí}}}{V_m}$$

Điểm dễ sai nhất là $V_m$. AP dùng phương trình khí lí tưởng chứ hiếm khi dùng thể tích mol cố định; A-Level dùng $24{,}0\ \mathrm{dm^3\,mol^{-1}}$ ở r.t.p. (25 °C, 1 atm); IUPAC hiện định nghĩa STP là 0 °C và 1 bar, cho $22{,}7\ \mathrm{dm^3\,mol^{-1}}$ chứ không phải 22,4. Con số 22,4 thuộc về quy ước cũ 1 atm.

## Quy trình giải một bài tỉ lượng

1. Viết và cân bằng phương trình — không có bước này mọi tỉ lệ đều vô nghĩa.
2. Đổi mọi dữ kiện về mol.
3. So sánh $n_i/\nu_i$ để tìm chất giới hạn.
4. Dùng tỉ lệ hệ số để sang mol sản phẩm.
5. Đổi ngược về đại lượng đề hỏi, rồi nhân hiệu suất nếu có.

## Khi nào cách này không đủ

Sơ đồ trên giả định phản ứng xảy ra hoàn toàn theo đúng một phương trình. Nếu hệ đạt cân bằng (Unit 7) hoặc có phản ứng phụ, lượng sản phẩm phải tính bằng hằng số cân bằng chứ không phải bằng tỉ lượng.

**Lỗi thường gặp:**
- So sánh trực tiếp số mol hai chất phản ứng để tìm chất giới hạn mà quên chia cho hệ số tỉ lượng — sai vì phương trình cho biết tỉ lệ tiêu thụ chứ không phải lượng tuyệt đối; một chất có nhiều mol hơn vẫn có thể hết trước nếu nó bị tiêu thụ nhanh gấp đôi.
- Dùng 22,4 dm³/mol cho mọi bài khí — sai vì con số này chỉ đúng ở 0 °C và 1 atm; theo định nghĩa STP hiện hành của IUPAC (1 bar) giá trị là 22,7 dm³/mol, còn ở điều kiện phòng của A-Level là 24,0 dm³/mol.
- Nhân hiệu suất vào lượng chất phản ứng thay vì vào lượng sản phẩm lí thuyết — sai vì hiệu suất mô tả phần sản phẩm thực sự thu hồi được, không mô tả lượng chất ban đầu đem dùng.

<sub>`lesson.chemistry.ap-atomic-structure.mol-va-tinh-toan-ti-luong`</sub>

---

### 2. Phổ khối lượng, đồng vị và nguyên tử khối trung bình
*Mass spectrometry, isotopes and relative atomic mass* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được nguyên lí hoạt động của phổ kế khối lượng và ý nghĩa trục hoành m/z
- Tính được nguyên tử khối trung bình từ phổ đồ và ngược lại tìm phần trăm đồng vị
- Phân tích được cụm pic đồng vị để nhận biết nguyên tố có mặt trong hợp chất

## Bài toán mở đầu

Bảng tuần hoàn ghi Cl = 35,45. Không có nguyên tử clo nào nặng 35,45 u cả. Con số đó là trung bình của một hỗn hợp — và phổ kế khối lượng là dụng cụ cho ta nhìn thấy hỗn hợp ấy.

## Bốn bước trong phổ kế

1. **Ion hoá**: mẫu bị bắn electron hoặc phun điện tử, tạo ion dương.
2. **Gia tốc**: điện trường truyền cho mọi ion cùng động năng.
3. **Làm lệch**: từ trường bẻ cong quỹ đạo; ion nhẹ lệch nhiều hơn ion nặng.
4. **Ghi nhận**: detector đếm số ion ở mỗi giá trị m/z.

Vì hầu hết ion tạo thành mang điện tích $+1$, trục hoành đọc thẳng ra khối lượng. Đây là lí do đề bài thường viết tắt "pic ở m/z = 35" nghĩa là ion $\mathrm{^{35}Cl^+}$.

## Từ phổ đồ ra nguyên tử khối

$$\bar{A} = \frac{\sum a_i A_i}{\sum a_i}$$

với $a_i$ là chiều cao pic (phần trăm số nguyên tử, không phải phần trăm khối lượng). Với clo, nếu dùng số khối nguyên: $\bar{A} = 0{,}7577\times35 + 0{,}2423\times37 = 35{,}48$. Giá trị bảng 35,45 chỉ thu được khi thay bằng khối lượng đồng vị chính xác ($34{,}969$ và $36{,}966$ u), vì khối lượng thực của hạt nhân luôn nhỏ hơn số khối do độ hụt khối. Với đề thi phổ thông sai khác này thường bỏ qua được, nhưng phải biết nó tồn tại. Khi chỉ có hai đồng vị, đặt $x$ là phần trăm đồng vị nhẹ ta được phương trình bậc nhất, giải trực tiếp.

## Dấu vân tay đồng vị trong hợp chất

Cụm pic ở vùng ion phân tử kể chuyện về nguyên tố có mặt:

- $\mathrm{^{35}Cl}$ và $\mathrm{^{37}Cl}$ theo tỉ lệ xấp xỉ 3 : 1 ⇒ pic M và M+2 cao 3 : 1.
- $\mathrm{^{79}Br}$ và $\mathrm{^{81}Br}$ gần 1 : 1 ⇒ M và M+2 cao gần bằng nhau.
- $\mathrm{^{13}C}$ chiếm 1,1% ⇒ pic M+1 nhỏ, chiều cao tỉ lệ với số nguyên tử carbon.

## Giới hạn

Phổ khối cho khối lượng chứ không cho cấu trúc. Hai đồng phân có cùng công thức phân tử cho cùng pic ion phân tử; muốn phân biệt phải đọc kiểu phân mảnh hoặc dùng IR và NMR.

**Lỗi thường gặp:**
- Dùng phần trăm khối lượng thay cho phần trăm số nguyên tử khi tính trung bình — sai vì chiều cao pic phổ khối đếm số ion, mà mỗi ion tương ứng một nguyên tử, nên trọng số phải là số nguyên tử.
- Coi pic M+2 luôn là dấu hiệu của clo — sai vì brom cũng cho M+2, chỉ khác ở tỉ lệ chiều cao (3:1 cho clo, gần 1:1 cho brom); phải đọc tỉ lệ chứ không chỉ đọc sự tồn tại của pic.
- Nhầm nguyên tử khối trung bình với số khối của đồng vị phổ biến nhất — sai vì trung bình là giá trị nội suy giữa các đồng vị, hầu như không bao giờ là số nguyên.

<sub>`lesson.chemistry.ap-atomic-structure.pho-khoi-va-dong-vi`</sub>

---

### 3. Cấu hình electron: nguyên lí, quy tắc và các ngoại lệ
*Electron configuration: principles, rules and exceptions* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Viết được cấu hình electron đầy đủ và dạng rút gọn khí hiếm cho nguyên tử và ion
- Giải thích được vì sao chromium và copper có cấu hình bất thường
- Xác định được thứ tự mất electron khi kim loại chuyển tiếp tạo ion

## Vấn đề

Biết số proton, ta muốn dự đoán nguyên tố phản ứng thế nào. Chìa khoá là electron ngoài cùng — nhưng phải biết chúng nằm ở đâu.

## Ba quy tắc và một trật tự

Thứ tự điền tuân theo quy tắc Klechkovski: xếp theo $n+l$ tăng dần, khi $n+l$ bằng nhau thì $n$ nhỏ điền trước. Kết quả là dãy quen thuộc $1s\,2s\,2p\,3s\,3p\,4s\,3d\,4p\,5s\,4d\,5p\,6s\,4f\,5d\,6p$. Số electron tối đa của phân lớp là $2(2l+1)$, của lớp thứ $n$ là $2n^2$.

Cùng lúc phải tuân Pauli (mỗi orbital tối đa 2 electron ngược spin) và Hund (điền đơn lẻ trước).

## Hai ngoại lệ bắt buộc nhớ

$$\mathrm{Cr}:\ [\mathrm{Ar}]3d^5 4s^1 \quad\text{chứ không phải } 3d^4 4s^2$$
$$\mathrm{Cu}:\ [\mathrm{Ar}]3d^{10} 4s^1 \quad\text{chứ không phải } 3d^9 4s^2$$

Lí do không phải "nửa bão hoà đẹp" như cách nói tắt, mà là: mức $3d$ và $4s$ rất sát nhau nên năng lượng trao đổi thu được khi có 5 (hoặc 10) electron $d$ song song đủ bù cho việc chuyển một electron từ $4s$ sang $3d$.

## Cấu hình của ion — chỗ hay sai nhất

Với kim loại chuyển tiếp, **electron $4s$ mất trước electron $3d$**. Vì sao nghịch với thứ tự điền? Vì sau khi $3d$ đã có electron, lực chắn thay đổi và $3d$ tụt xuống dưới $4s$; trong ion, $4s$ trở thành mức ngoài cùng và cao hơn. Do đó $\mathrm{Fe^{2+}}$ là $[\mathrm{Ar}]3d^6$, không phải $[\mathrm{Ar}]3d^4 4s^2$.

Với phi kim tạo anion thì đơn giản hơn: thêm electron vào phân lớp đang dở.

## Giới hạn của mô hình

Aufbau là quy tắc kinh nghiệm cho nguyên tử ở trạng thái cơ bản, cô lập. Nó không mô tả trạng thái kích thích, không áp dụng thẳng cho nguyên tử trong phân tử, và với các nguyên tố nặng (Z lớn) hiệu ứng tương đối tính làm sai lệch thứ tự.

**Lỗi thường gặp:**
- Bỏ electron 3d trước 4s khi viết cấu hình ion kim loại chuyển tiếp — sai vì thứ tự điền và thứ tự mất không đồng nhất; sau khi 3d có electron thì 3d hạ xuống dưới 4s nên 4s là mức ngoài cùng và mất trước.
- Ghép đôi electron trong một orbital p khi vẫn còn orbital p trống — sai vì hai electron cùng orbital đẩy nhau mạnh hơn (năng lượng ghép đôi dương), quy tắc Hund yêu cầu điền đơn lẻ trước.
- Giải thích ngoại lệ của Cr và Cu chỉ bằng câu 'phân lớp nửa bão hoà bền' mà không nói tới mức 3d và 4s gần nhau — sai vì nếu khoảng cách năng lượng lớn thì lợi ích trao đổi không đủ bù, và thực tế các nguyên tố như W không theo mẫu này.

<sub>`lesson.chemistry.ap-atomic-structure.cau-hinh-electron`</sub>

---

### 4. Phổ hấp thụ - phát xạ và bằng chứng lượng tử hoá
*Absorption and emission spectra, evidence for quantised energy* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao phổ nguyên tử là phổ vạch chứ không phải phổ liên tục
- Vận dụng được hệ thức Planck để chuyển đổi giữa bước sóng, tần số và hiệu năng lượng hai mức
- Tính được năng lượng ion hoá của hydrogen từ giới hạn hội tụ của dãy Lyman

## Câu hỏi thực nghiệm

Đốt nóng khí hydrogen ở áp suất thấp, ánh sáng phát ra khi qua lăng kính không cho dải màu liên tục mà cho vài vạch sắc nét. Vì sao?

## Lượng tử hoá

Nếu electron có thể mang năng lượng bất kì, mọi hiệu năng lượng đều khả dĩ và ta sẽ thấy phổ liên tục. Thực tế chỉ thấy vạch, nên tập năng lượng khả dĩ phải rời rạc. Mỗi vạch là một photon phát ra khi electron rơi từ mức cao xuống mức thấp:

$$\Delta E = h\nu = \frac{hc}{\lambda}$$

với $h = 6{,}626\times10^{-34}\ \mathrm{J\,s}$, $c = 3{,}00\times10^8\ \mathrm{m\,s^{-1}}$.

## Đọc một phổ đồ

Các vạch trong cùng một dãy **hội tụ** khi đi về phía tần số cao: khoảng cách giữa các mức năng lượng thu hẹp dần khi $n$ tăng. Nơi các vạch chụm lại thành một điểm là giới hạn hội tụ, ứng với chuyển từ $n = \infty$. Với dãy Lyman ($n_2 \to 1$), năng lượng của giới hạn hội tụ chính là **năng lượng ion hoá thứ nhất** của hydrogen:

$$E_i = h\nu_{\infty}\times N_A$$

Nhân $N_A$ để đổi từ một nguyên tử sang một mol — đây là bước học sinh hay quên.

## Hấp thụ hay phát xạ

Cùng một nguyên tử, cùng các mức năng lượng, nên vạch hấp thụ và vạch phát xạ nằm ở đúng những bước sóng như nhau. Khác biệt chỉ ở chiều: phổ hấp thụ là các vạch tối trên nền sáng (ánh sáng trắng đi qua hơi nguyên tử), phổ phát xạ là các vạch sáng trên nền tối.

## Ranh giới áp dụng

Công thức Rydberg dạng $1/\lambda = R(1/n_1^2 - 1/n_2^2)$ chỉ đúng cho hệ **một electron** (H, He⁺, Li²⁺). Với nguyên tử nhiều electron, tương tác đẩy electron - electron làm phổ phức tạp hơn nhiều và phải xử lí bằng cơ học lượng tử gần đúng.

**Lỗi thường gặp:**
- Quên nhân với hằng số Avogadro khi báo kết quả theo kJ/mol — sai vì hc/λ cho năng lượng của một photon ứng với một nguyên tử, còn năng lượng ion hoá theo quy ước hoá học luôn tính cho một mol nguyên tử.
- Dùng giới hạn hội tụ của dãy Balmer để tính năng lượng ion hoá — sai vì dãy Balmer hội tụ về n = 2 nên chỉ cho năng lượng ion hoá từ trạng thái kích thích thứ nhất, nhỏ hơn giá trị thật.
- Nói rằng các vạch trong một dãy cách đều nhau — sai vì mức năng lượng theo 1/n² nên khoảng cách giữa các mức thu hẹp rất nhanh khi n tăng, tạo ra hiện tượng hội tụ.

<sub>`lesson.chemistry.ap-atomic-structure.pho-hap-thu-phat-xa`</sub>

---

### 5. Năng lượng ion hoá liên tiếp, phổ PES và bằng chứng cho lớp electron
*Successive ionisation energies, PES and evidence for shells* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phân tích được đồ thị năng lượng ion hoá liên tiếp để xác định nhóm của nguyên tố
- Giải thích được ý nghĩa vị trí và chiều cao của mỗi pic trên phổ quang electron
- Chứng minh được sự tồn tại của lớp và phân lớp electron từ số liệu thực nghiệm

## Làm sao biết electron xếp thành lớp

Mô hình lớp không phải là quy ước tuỳ tiện. Có hai bộ số liệu thực nghiệm buộc ta chấp nhận nó.

## Bằng chứng thứ nhất: ion hoá liên tiếp

Tách lần lượt từng electron của một nguyên tử, ta thu được dãy $I_1 < I_2 < I_3 < \dots$ Dãy luôn tăng (mỗi lần tách, ion còn lại dương hơn nên giữ electron chặt hơn), nhưng tăng **không đều**: có những chỗ nhảy vọt gấp 3-5 lần.

Với nhôm ($1s^2 2s^2 2p^6 3s^2 3p^1$), $I_1 = 578$, $I_2 = 1817$, $I_3 = 2745$, rồi $I_4 = 11577$ kJ/mol. Bước nhảy sau electron thứ ba nói rằng nhôm chỉ có 3 electron ở lớp ngoài cùng — tức là nhóm 13. **Quy tắc đọc: số electron trước bước nhảy lớn đầu tiên bằng số thứ tự nhóm A.**

## Bằng chứng thứ hai: phổ PES

PES cho ảnh chụp cả nguyên tử một lúc. Mỗi pic là một phân lớp. Đọc phổ theo hai trục:

- **Vị trí** (năng lượng liên kết): pic càng xa bên trái, năng lượng càng lớn, electron càng gần hạt nhân. Với AP, trục thường vẽ ngược nên phải đọc nhãn cẩn thận.
- **Chiều cao** (cường độ): tỉ lệ với số electron trong phân lớp. Tỉ lệ 2 : 2 : 6 nhận ra ngay $1s^2 2s^2 2p^6$.

Ví dụ phổ của Na có bốn pic tỉ lệ chiều cao 2 : 2 : 6 : 1 — chính là $1s^2 2s^2 2p^6 3s^1$.

## Vì sao 2s và 2p tách thành hai pic

Nếu chỉ có lớp thì $n = 2$ phải cho một pic duy nhất cao 8 đơn vị. Thực tế có hai pic (2 và 6) ở hai năng lượng khác nhau, chứng minh lớp còn chia thành phân lớp. Electron $2s$ có xác suất xuất hiện gần hạt nhân lớn hơn ($s$ xuyên qua vùng chắn tốt hơn $p$) nên bị giữ chặt hơn.

## Giới hạn

PES đo được electron của mọi phân lớp nhưng không phân biệt được orbital riêng lẻ trong cùng phân lớp, và không cho biết trực tiếp cấu trúc phân tử.

**Lỗi thường gặp:**
- Đếm số electron sau bước nhảy thay vì trước bước nhảy để suy ra nhóm — sai vì các electron dễ tách (nằm trước bước nhảy) mới là electron hoá trị ở lớp ngoài cùng, còn sau bước nhảy là lớp bên trong.
- Cho rằng chiều cao pic PES tỉ lệ với năng lượng của electron — sai vì chiều cao chỉ đếm số electron trong phân lớp, còn năng lượng nằm ở trục hoành; nhầm hai trục dẫn tới đọc sai hoàn toàn cấu hình.
- Kì vọng năng lượng ion hoá luôn tăng đều — sai vì trong cùng một phân lớp mức tăng nhỏ, chỉ khi chuyển sang lớp mới mới nhảy vọt; đúng đặc điểm này mới là cơ sở để nhận biết cấu trúc lớp.

<sub>`lesson.chemistry.ap-atomic-structure.nang-luong-ion-hoa-lien-tiep`</sub>

---

### 6. Xu hướng tuần hoàn và điện tích hạt nhân hiệu dụng
*Periodic trends and effective nuclear charge* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được mọi xu hướng tuần hoàn bằng hai biến số điện tích hạt nhân hiệu dụng và khoảng cách
- So sánh được bán kính nguyên tử, bán kính ion, năng lượng ion hoá và ái lực electron của các nguyên tố
- Phân tích được các bất thường trong dãy năng lượng ion hoá chu kì 3

## Một nguyên lí, mọi xu hướng

Toàn bộ bảng tuần hoàn có thể đọc bằng định luật Coulomb dạng tỉ lệ:

$$F \propto \frac{Z_{\text{eff}}\cdot q}{r^2}$$

Mọi câu hỏi "vì sao đại lượng này tăng hay giảm" quy về việc hai biến $Z_{\text{eff}}$ và $r$ thay đổi thế nào.

## Đi ngang một chu kì

Thêm proton nhưng electron mới điền vào **cùng lớp**, mà electron cùng lớp chắn cho nhau rất kém. Vậy $Z_{\text{eff}}$ tăng đều trong khi $r$ gần như không đổi (thậm chí giảm vì lực hút mạnh hơn). Hệ quả:

- Bán kính nguyên tử **giảm**.
- Năng lượng ion hoá **tăng**.
- Độ âm điện **tăng**.
- Ái lực electron trở nên **âm hơn**.

## Đi xuống một nhóm

Thêm hẳn một lớp mới: $r$ tăng vọt, đồng thời electron lớp trong chắn rất hiệu quả nên $Z_{\text{eff}}$ gần như không đổi. Khoảng cách thắng thế: bán kính tăng, năng lượng ion hoá giảm.

## Ba bất thường phải giải thích được

1. **Al thấp hơn Mg**: electron bị tách của Al nằm ở $3p$, có năng lượng cao hơn và bị $3s$ chắn, nên dễ tách hơn dự đoán.
2. **S thấp hơn P**: ở S, phân lớp $3p$ đã bắt đầu ghép đôi ($3p^4$), lực đẩy giữa hai electron cùng orbital làm electron đó dễ bị tách.
3. **Ái lực electron của F nhỏ hơn Cl**: nguyên tử F quá nhỏ, electron thêm vào chịu lực đẩy lớn từ các electron đã có trong lớp $2p$ chật chội.

## Bán kính ion

Cation luôn nhỏ hơn nguyên tử mẹ (mất cả một lớp, hoặc ít electron hơn mà cùng số proton). Anion luôn lớn hơn. Trong dãy đẳng electron như $\mathrm{N^{3-}, O^{2-}, F^-, Na^+, Mg^{2+}}$, cùng 10 electron nên bán kính giảm khi $Z$ tăng.

## Giới hạn

Các quy luật này mô tả nguyên tố nhóm A rõ ràng; với dãy chuyển tiếp, việc điền vào lớp $(n-1)d$ bên trong làm bán kính thay đổi rất ít qua cả dãy.

**Lỗi thường gặp:**
- Nói bán kính giảm khi đi ngang chu kì 'vì thêm electron nên nguyên tử phải to ra' rồi kết luận ngược — sai vì electron thêm vào cùng lớp không tạo lớp mới, trong khi proton thêm vào làm Zeff tăng nên tác dụng co lại thắng thế.
- Cho rằng ái lực electron luôn tăng đều theo chu kì và nhóm — sai vì F có ái lực nhỏ hơn Cl do bán kính quá nhỏ gây lực đẩy giữa các electron trong lớp 2p, một ngoại lệ mà đề A-Level rất hay hỏi.
- Giải thích bất thường Al < Mg bằng 'Mg có phân lớp 3s bão hoà' mà không nói electron của Al ở phân lớp 3p cao hơn — sai ở chỗ lập luận, vì bão hoà 3s chỉ là cách nói khác của cùng hiện tượng, còn nguyên nhân vật lí là chênh lệch năng lượng giữa 3s và 3p.

<sub>`lesson.chemistry.ap-atomic-structure.xu-huong-tuan-hoan`</sub>

---

## Unit 2: Compound Structure and Properties

### 1. Liên kết ion, cộng hoá trị, kim loại và tam giác van Arkel - Ketelaar
*Ionic, covalent and metallic bonding; the van Arkel-Ketelaar triangle* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được ba kiểu liên kết theo cơ chế phân bố electron hoá trị
- Vận dụng được tam giác van Arkel - Ketelaar để định vị một chất trên phổ liên kết liên tục
- Giải thích được tính chất vật lí đặc trưng của mỗi kiểu liên kết từ bản chất tương tác

## Ba loại hay một phổ liên tục

Sách phổ thông chia liên kết thành ba loại rời rạc. Sự thật là chúng nằm trên một miền liên tục, và tam giác van Arkel - Ketelaar là cách nhìn thấy điều đó.

## Cơ chế của từng loại

| Loại | Cấu tử | Cơ chế | Đặc trưng |
|---|---|---|---|
| Ion | kim loại + phi kim | chuyển hẳn electron | mạng cứng, giòn, dẫn điện khi nóng chảy |
| Cộng hoá trị | phi kim + phi kim | dùng chung cặp electron | phân tử rời hoặc mạng lưới, thường không dẫn điện |
| Kim loại | kim loại + kim loại | biển electron phi định xứ | dẻo, dẫn điện và dẫn nhiệt tốt |

## Hai toạ độ của tam giác

- Trục ngang: **độ âm điện trung bình** $\bar{\chi} = (\chi_A + \chi_B)/2$. Giá trị nhỏ nghĩa là cả hai nguyên tố đều giữ electron yếu — hướng về kim loại.
- Trục dọc: **hiệu độ âm điện** $\Delta\chi = |\chi_A - \chi_B|$. Giá trị lớn nghĩa là một bên kéo electron mạnh hơn hẳn — hướng về ion.

NaCl có $\Delta\chi = 2{,}1$: nằm cao, rõ ràng ion. $\mathrm{Cl_2}$ có $\Delta\chi = 0$ và $\bar{\chi} = 3{,}0$: góc cộng hoá trị. Na kim loại có $\Delta\chi = 0$ và $\bar{\chi} = 0{,}9$: góc kim loại. Còn $\mathrm{AlCl_3}$ với $\Delta\chi = 1{,}5$ rơi vào vùng giữa — và thực tế nó thăng hoa ở 180 °C như một chất cộng hoá trị chứ không như muối.

## Vì sao tính chất vật lí khác nhau

Điểm mấu chốt: **cái gì bị phá vỡ khi nóng chảy**. Với NaCl phải phá lực hút tĩnh điện toàn mạng nên cần 801 °C. Với $\mathrm{I_2}$ chỉ cần thắng lực London giữa các phân tử (liên kết I-I bên trong vẫn nguyên) nên 114 °C là đủ. Đây là lí do so sánh nhiệt độ nóng chảy phải hỏi "lực nào bị phá" trước.

## Giới hạn

Tam giác dùng thang Pauling, vốn là thang kinh nghiệm; ranh giới $\Delta\chi = 1{,}7$ hay dùng chỉ là quy ước gần đúng, không phải một ngưỡng vật lí.

**Lỗi thường gặp:**
- Kết luận 'kim loại + phi kim thì luôn là hợp chất ion' — sai vì AlCl₃, BeCl₂ có hiệu độ âm điện chưa đủ lớn và cation nhỏ điện tích cao phân cực hoá mạnh anion, khiến liên kết mang nhiều tính cộng hoá trị.
- So sánh nhiệt độ nóng chảy của hợp chất cộng hoá trị bằng độ mạnh liên kết trong phân tử — sai vì nóng chảy chỉ phá lực liên phân tử, không phá liên kết cộng hoá trị bên trong; nhầm hai loại lực này dẫn tới dự đoán ngược hoàn toàn.
- Cho rằng chất ion luôn dẫn điện — sai vì ở thể rắn các ion bị khoá cứng trong mạng, chỉ khi nóng chảy hoặc hoà tan các ion mới chuyển động được và dẫn điện.

<sub>`lesson.chemistry.ap-compound-structure.ba-loai-lien-ket`</sub>

---

### 2. Công thức Lewis, điện tích hình thức và cấu trúc cộng hưởng
*Lewis structures, formal charge and resonance* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Vẽ được công thức Lewis cho phân tử và ion đa nguyên tử theo quy trình đếm electron
- Tính được điện tích hình thức và dùng nó để chọn cấu trúc hợp lí nhất
- Giải thích được ý nghĩa của cộng hưởng và tính được bậc liên kết trung bình

## Quy trình vẽ Lewis

1. Đếm tổng electron hoá trị; **ion âm cộng thêm, ion dương trừ đi** số electron bằng điện tích.
2. Chọn nguyên tử trung tâm là nguyên tử có độ âm điện nhỏ nhất (không bao giờ là H hay F).
3. Nối liên kết đơn, rồi điền cặp electron tự do cho các nguyên tử biên đủ octet.
4. Electron còn dư đặt lên nguyên tử trung tâm.
5. Nếu trung tâm thiếu octet, kéo cặp tự do từ nguyên tử biên vào tạo liên kết đôi hoặc ba.

## Điện tích hình thức: công cụ chọn cấu trúc

$$FC = (\text{số e hoá trị}) - (\text{số e tự do}) - \tfrac{1}{2}(\text{số e dùng chung})$$

Quy tắc chọn: cấu trúc tốt nhất có (a) trị tuyệt đối các $FC$ nhỏ nhất, (b) điện tích âm nằm trên nguyên tử âm điện hơn, (c) tránh hai điện tích cùng dấu cạnh nhau. Tổng $FC$ luôn bằng điện tích của tiểu phân — dùng điều này để tự kiểm tra.

## Ba nhóm ngoại lệ octet

- **Thiếu electron**: $\mathrm{BF_3}$ (6 e quanh B), $\mathrm{BeCl_2}$ (4 e).
- **Số electron lẻ**: $\mathrm{NO}$, $\mathrm{NO_2}$ — gốc tự do, không thể có octet cho mọi nguyên tử.
- **Mở rộng octet**: $\mathrm{PCl_5}$, $\mathrm{SF_6}$ — chỉ xảy ra với nguyên tử trung tâm từ chu kì 3 trở đi, vì cần orbital $d$ trống (cách giải thích hiện đại thiên về liên kết ba tâm bốn electron).

## Cộng hưởng không phải là dao động

Với $\mathrm{NO_3^-}$ ta vẽ ba cấu trúc, mỗi cấu trúc có một liên kết đôi. Ion thật **không** chuyển qua lại giữa ba dạng đó. Nó là một dạng duy nhất, trung bình của ba, với electron pi trải đều. Bằng chứng thực nghiệm: cả ba liên kết N-O dài bằng nhau (124 pm), nằm giữa độ dài đơn (136 pm) và đôi (115 pm).

$$\text{Bậc liên kết} = \frac{\text{tổng số cặp liên kết}}{\text{số cấu trúc}} = \frac{4}{3} \approx 1{,}33$$

Cộng hưởng luôn làm hệ **bền hơn** so với bất kì cấu trúc đơn lẻ nào; phần chênh lệch gọi là năng lượng cộng hưởng (rõ nhất ở benzene, khoảng 150 kJ/mol).

**Lỗi thường gặp:**
- Quên cộng hoặc trừ electron theo điện tích của ion khi đếm tổng electron hoá trị — sai vì công thức Lewis phải mô tả đúng số electron thực có; thiếu hai electron sẽ dẫn tới cấu trúc hoàn toàn khác.
- Hiểu cộng hưởng là phân tử dao động luân phiên giữa các cấu trúc — sai vì thực nghiệm cho thấy mọi liên kết tương đương và có độ dài trung gian tại mọi thời điểm; cộng hưởng là hạn chế của kí hiệu Lewis chứ không phải hiện tượng vật lí.
- Mở rộng octet cho nguyên tử chu kì 2 như N hay O (ví dụ vẽ N với 5 liên kết trong HNO₃) — sai vì lớp 2 chỉ có orbital 2s và 2p, tối đa 8 electron; không có orbital 2d để chứa thêm.

<sub>`lesson.chemistry.ap-compound-structure.lewis-va-cong-huong`</sub>

---

### 3. Thuyết VSEPR, hình học phân tử và lai hoá orbital
*VSEPR theory, molecular geometry and orbital hybridisation* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Xác định được dạng hình học electron và hình học phân tử từ kí hiệu AXmEn
- Giải thích được định lượng sự thu hẹp góc liên kết do cặp electron tự do
- Liên hệ được trạng thái lai hoá với số vùng electron và số liên kết sigma, pi

## Nguyên lí duy nhất của VSEPR

Các vùng mật độ electron quanh nguyên tử trung tâm đẩy nhau, nên tự sắp xếp sao cho **xa nhau nhất có thể**. Chỉ có vậy.

## Quy trình ba bước

1. Vẽ Lewis, **đếm số vùng** quanh nguyên tử trung tâm (liên kết đôi tính là một vùng).
2. Số vùng ⇒ hình học electron: 2 thẳng, 3 tam giác phẳng, 4 tứ diện, 5 lưỡng chóp tam giác, 6 bát diện.
3. Bỏ cặp tự do đi ⇒ hình học phân tử.

Kí hiệu $\mathrm{AX}_m\mathrm{E}_n$: $m$ nguyên tử biên, $n$ cặp tự do. $\mathrm{H_2O}$ là $\mathrm{AX_2E_2}$: hình học electron tứ diện, hình học phân tử **gấp khúc**.

## Góc liên kết thu hẹp bao nhiêu

Cặp tự do chỉ bị một hạt nhân giữ nên phình ra rộng hơn cặp liên kết, đẩy mạnh hơn. Quy tắc kinh nghiệm: **mỗi cặp tự do làm góc giảm khoảng 2,5°**.

$$\mathrm{CH_4}\ 109{,}5^\circ \;\to\; \mathrm{NH_3}\ 107^\circ \;\to\; \mathrm{H_2O}\ 104{,}5^\circ$$

Thứ tự lực đẩy: cặp tự do - cặp tự do > cặp tự do - cặp liên kết > cặp liên kết - cặp liên kết.

## Vị trí ưu tiên trong lưỡng chóp tam giác

Với 5 vùng, hai vị trí không tương đương: trục (axial, 2 vị trí) và xích đạo (equatorial, 3 vị trí). Cặp tự do **luôn chọn vị trí xích đạo**, vì ở đó nó chỉ có 2 láng giềng ở 90° thay vì 3. Nhờ quy tắc này ta biết $\mathrm{SF_4}$ có dạng bập bênh, $\mathrm{ClF_3}$ có dạng chữ T và $\mathrm{XeF_2}$ thẳng.

## Lai hoá: đọc thẳng từ số vùng

| Số vùng | Lai hoá | Góc lí tưởng |
|---|---|---|
| 2 | $sp$ | 180° |
| 3 | $sp^2$ | 120° |
| 4 | $sp^3$ | 109,5° |

Liên kết đơn là một sigma. Liên kết đôi là một sigma + một pi; liên kết ba là một sigma + hai pi. Orbital pi hình thành từ orbital $p$ **chưa lai hoá** xen phủ bên — đó là lí do liên kết đôi không quay tự do được và sinh ra đồng phân hình học.

## Giới hạn của VSEPR

VSEPR dự đoán hình học rất tốt cho hợp chất nhóm A nhưng thất bại với nhiều phức chất kim loại chuyển tiếp, nơi trường phối tử và cấu hình $d$ mới là yếu tố quyết định.

**Lỗi thường gặp:**
- Đếm liên kết đôi là hai vùng electron — sai vì hai cặp electron của liên kết đôi cùng nằm giữa một cặp nguyên tử nên chỉ chiếm một hướng trong không gian; đếm sai làm CO₂ ra hình gấp khúc thay vì thẳng.
- Trả lời hình học electron khi đề hỏi hình học phân tử — sai vì hình học phân tử chỉ mô tả vị trí nguyên tử; NH₃ có hình học electron tứ diện nhưng hình học phân tử là chóp tam giác.
- Đặt cặp electron tự do ở vị trí trục trong hệ 5 vùng — sai vì ở vị trí trục cặp tự do có ba láng giềng ở 90°, còn ở vị trí xích đạo chỉ có hai, nên năng lượng đẩy lớn hơn và cấu hình đó không bền.

<sub>`lesson.chemistry.ap-compound-structure.vsepr-va-lai-hoa`</sub>

---

### 4. Độ phân cực phân tử và lực liên phân tử
*Molecular polarity and intermolecular forces* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được phân tử có phân cực hay không bằng tổng vectơ momen lưỡng cực
- Sắp xếp được các lực liên phân tử theo độ mạnh và giải thích cơ sở vật lí
- Dự đoán được nhiệt độ sôi, độ tan và độ nhớt từ kiểu lực liên phân tử

## Phân tử có liên kết phân cực chưa chắc đã phân cực

$\mathrm{CO_2}$ có hai liên kết C=O rất phân cực, nhưng phân tử thẳng nên hai vectơ momen ngược chiều triệt tiêu: $\vec{\mu}_{\text{tổng}} = \vec{0}$. Phân tử không phân cực. Ngược lại $\mathrm{H_2O}$ gấp khúc nên hai vectơ cộng lại cho $\mu = 1{,}85$ D.

**Quy trình**: (1) xác định hình học, (2) vẽ vectơ trên từng liên kết theo chiều tăng độ âm điện, (3) cộng vectơ, có kể vectơ của cặp electron tự do. Đối xứng cao mà mọi nguyên tử biên giống nhau ⇒ triệt tiêu.

## Thang lực liên phân tử

$$\text{ion-lưỡng cực} > \text{liên kết hydrogen} > \text{lưỡng cực-lưỡng cực} > \text{London}$$

Nhưng thang này chỉ đúng khi **so cùng kích thước phân tử**. Lực London tăng theo số electron và diện tích tiếp xúc, nên $\mathrm{I_2}$ (chỉ có London) sôi ở 184 °C, cao hơn $\mathrm{HCl}$ (có lưỡng cực) sôi ở −85 °C. Đây là chỗ học sinh sai nhiều nhất.

## Ba hệ quả thực nghiệm

- **Nhiệt độ sôi**: bất thường của $\mathrm{H_2O}$, $\mathrm{NH_3}$, $\mathrm{HF}$ so với các hydride cùng nhóm là bằng chứng trực tiếp cho liên kết hydrogen.
- **Độ tan**: "giống tan trong giống" thực chất là câu hỏi năng lượng — chất tan chỉ tan nếu tương tác mới (chất tan - dung môi) bù được tương tác cũ bị phá vỡ.
- **Đồng phân mạch nhánh**: pentane sôi 36 °C còn neopentane chỉ 9,5 °C, vì phân tử cầu gọn có diện tích tiếp xúc nhỏ hơn nên lực London yếu hơn dù cùng số electron.

## Một điểm hay bị nói sai

Khi nước sôi, **liên kết O-H không bị phá**. Chỉ liên kết hydrogen giữa các phân tử bị phá. Đó là lí do 100 °C đủ để nước sôi trong khi phá liên kết O-H cần khoảng 460 kJ/mol.

**Lỗi thường gặp:**
- Kết luận phân tử có liên kết phân cực thì phân tử phân cực — sai vì momen lưỡng cực là đại lượng vectơ; trong CCl₄, BF₃, CO₂ các vectơ triệt tiêu do đối xứng nên phân tử không phân cực.
- Xếp lực lưỡng cực luôn mạnh hơn lực London — sai vì lực London tăng rất nhanh theo số electron; I₂ chỉ có London nhưng sôi cao hơn HCl có lưỡng cực rất nhiều.
- Nói khi đun sôi nước thì liên kết O-H bị phá — sai vì nếu vậy nước sẽ phân huỷ thành H₂ và O₂; sôi chỉ tách các phân tử ra xa nhau, tức phá liên kết hydrogen liên phân tử.
- Cho rằng mọi phân tử chứa H và O đều tạo liên kết hydrogen — sai vì H phải liên kết trực tiếp với N, O hoặc F; trong CH₃OCH₃ nguyên tử H chỉ gắn với C nên chất này không tự tạo liên kết hydrogen với nhau.

<sub>`lesson.chemistry.ap-compound-structure.phan-cuc-va-luc-lien-phan-tu`</sub>

---

## Unit 2: IChO Theoretical Chemistry

### 1. IChO Hoá lượng tử: Mô hình electron tự do FEMO và Phân bố Boltzmann
*Quantum chemistry in IChO: Free-electron model (FEMO) and Boltzmann distribution* · THPT (lớp 10-12) · olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Áp dụng mô hình giếng thế 1 chiều FEMO tính bước sóng hấp thụ quang học của phân tử polyen liên hợp
- Tính năng lượng chuyển dời điện tử giữa mức HOMO và LUMO
- Vận dụng phân bố Boltzmann có kể đến độ suy biến mức năng lượng

## Mô hình electron tự do FEMO cho mạch liên hợp

Xét mạch polyen liên hợp chứa $k$ liên kết đôi, tức có $N = 2k$ electron $\pi$. Chiều dài giếng thế một chiều được ước tính bởi $L = (2k + 1) d_{CC}$. Năng lượng mức thứ $n$ trong giếng thế vô hạn:

$$E_n = \frac{n^2 h^2}{8 m_e L^2}$$

Mỗi orbital chứa 2 electron. Mức bị chiếm cao nhất (HOMO) có $n_1 = k$, mức trống thấp nhất (LUMO) có $n_2 = k + 1$. Năng lượng kích thích quang học:

$$\Delta E = E_{k+1} - E_k = \frac{(2k + 1) h^2}{8 m_e L^2} = \frac{h c}{\lambda}$$

## Phân bố Boltzmann với độ suy biến

Số phân tử ở trạng thái năng lượng $E_2$ (độ suy biến $g_2$) so với trạng thái $E_1$ (độ suy biến $g_1$) ở cân bằng nhiệt độ $T$:

$$\frac{N_2}{N_1} = \frac{g_2}{g_1} e^{-\frac{E_2 - E_1}{k_B T}}$$

**Lỗi thường gặp:**
- Quên nhân độ suy biến g_2/g_1 trong biểu thức tỉ số quần tụ Boltzmann
- Tính sai chỉ số mức HOMO: mạch có 2k electron pi thì mức HOMO là n = k, LUMO là n = k + 1

<sub>`lesson.chemistry.icho.hoa-luong-tu-femo-va-nhiet-dong-thong-ke`</sub>

---

## Unit 3: Intermolecular Forces and Properties

### 1. Trạng thái vật chất, khí lí tưởng và sai lệch của khí thực
*States of matter, the ideal gas law and deviations of real gases* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Vận dụng được phương trình trạng thái khí lí tưởng và dạng hai trạng thái để giải bài toán khí
- Giải thích được hai giả định của mô hình khí lí tưởng và vì sao chúng thất bại
- Phân tích được đồ thị hệ số nén Z theo áp suất để nhận diện kiểu sai lệch

## Một phương trình cho ba định luật cũ

$$pV = nRT$$

gói gọn Boyle ($pV$ hằng khi $T$, $n$ cố định), Charles ($V/T$ hằng) và Avogadro ($V \propto n$). Với $R = 8{,}314\ \mathrm{J\,K^{-1}mol^{-1}}$, bắt buộc dùng $p$ theo Pa, $V$ theo m³, $T$ theo K. Đây là nguồn sai số phổ biến nhất: quên đổi cm³ sang m³ (chia $10^6$) hoặc quên đổi °C sang K.

Khi một lượng khí xác định chuyển trạng thái, $n$ và $R$ triệt tiêu:

$$\frac{p_1V_1}{T_1} = \frac{p_2V_2}{T_2}$$

## Hai giả định và khi nào chúng gãy

Mô hình lí tưởng giả định (a) phân tử không có thể tích riêng, (b) không có lực hút giữa các phân tử. Cả hai đều là xấp xỉ tốt khi **áp suất thấp và nhiệt độ cao** — lúc đó phân tử ở xa nhau, thể tích riêng không đáng kể so với thể tích bình, và động năng lớn hơn nhiều thế năng hút.

## Đọc đồ thị Z theo p

$$Z = \frac{pV_m}{RT}$$

- **Áp suất trung bình, $Z < 1$**: lực hút liên phân tử kéo các phân tử lại, va chạm vào thành yếu hơn nên áp suất đo được nhỏ hơn lí tưởng. Sai lệch này rõ nhất với khí phân cực hoặc dễ hoá lỏng như $\mathrm{NH_3}$, $\mathrm{CO_2}$.
- **Áp suất rất cao, $Z > 1$**: phân tử bị ép sát, thể tích riêng của chúng trở nên đáng kể, khí khó nén hơn dự đoán.

He và $\mathrm{H_2}$ gần lí tưởng nhất vì phân tử nhỏ, ít electron, lực London rất yếu.

## Hệ quả cần nhớ

Sai lệch càng lớn khi lực liên phân tử càng mạnh. Vì thế câu hỏi "khí nào lệch khỏi lí tưởng nhiều nhất" thực chất là câu hỏi "khí nào có lực liên phân tử mạnh nhất" — quay lại đúng nội dung Unit 2.

**Lỗi thường gặp:**
- Thay nhiệt độ theo độ Celsius vào pV = nRT — sai vì phương trình xuất phát từ động năng trung bình tỉ lệ với nhiệt độ tuyệt đối; dùng °C sẽ cho kết quả vô nghĩa khi nhiệt độ âm.
- Giải thích Z < 1 bằng thể tích riêng của phân tử — sai vì thể tích riêng luôn làm Z tăng; chỉ lực hút liên phân tử mới kéo Z xuống dưới 1, và hai hiệu ứng này chiếm ưu thế ở hai vùng áp suất khác nhau.
- Cho rằng mọi khí đều lệch khỏi lí tưởng như nhau — sai vì mức lệch phụ thuộc lực liên phân tử; He gần lí tưởng còn NH₃ lệch mạnh dù cùng điều kiện p, T.

<sub>`lesson.chemistry.ap-imf-properties.khi-li-tuong-va-khi-thuc`</sub>

---

### 2. Áp suất riêng phần, phân mol và định luật Graham
*Partial pressure, mole fraction and Graham's law* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Tính được áp suất riêng phần của từng khí trong hỗn hợp bằng phân mol
- Vận dụng được định luật Dalton để xử lí bài toán thu khí trên nước
- So sánh được tốc độ khuếch tán và thoát khí của hai khí bằng định luật Graham

## Vì sao mỗi khí "không biết" có khí khác

Trong mô hình lí tưởng, phân tử không tương tác. Vậy áp suất mà khí A gây ra chỉ phụ thuộc số phân tử A, thể tích và nhiệt độ — hoàn toàn độc lập với sự có mặt của B. Đó là nội dung định luật Dalton:

$$p_{\text{tổng}} = p_A + p_B + \dots \qquad p_A = x_A\, p_{\text{tổng}}$$

với $x_A = n_A/n_{\text{tổng}}$.

## Hệ quả quan trọng

Vì $p_A \propto n_A$ ở cùng $V$, $T$, nên với khí lí tưởng **phần trăm áp suất = phần trăm số mol = phần trăm thể tích**. Ba con số này bằng nhau, và điều đó chỉ đúng cho chất khí — với dung dịch thì không.

## Thu khí trên nước

Khi thu khí qua nước, hỗn hợp trong ống luôn có hơi nước bão hoà. Áp suất khí cần đo là:

$$p_{\text{khí}} = p_{\text{khí quyển}} - p_{\mathrm{H_2O}}$$

Áp suất hơi nước tra bảng theo nhiệt độ (ví dụ 3,17 kPa ở 25 °C). Bỏ qua bước trừ này là lỗi kinh điển, làm kết quả cao hơn thực tế vài phần trăm.

## Định luật Graham

$$\frac{r_1}{r_2} = \sqrt{\frac{M_2}{M_1}}$$

Nguồn gốc: ở cùng nhiệt độ, mọi khí có cùng động năng trung bình $\tfrac{3}{2}k_BT$. Từ $\tfrac{1}{2}mv^2$ bằng nhau suy ra $v \propto 1/\sqrt{m}$. Phân tử nhẹ chạy nhanh hơn nên thoát nhanh hơn — nhưng chỉ theo căn bậc hai, nên $\mathrm{H_2}$ (M = 2) chỉ nhanh gấp 4 lần $\mathrm{O_2}$ (M = 32) chứ không phải 16 lần.

## Ranh giới áp dụng

Graham mô tả **thoát khí** qua lỗ nhỏ rất chính xác. Với **khuếch tán** trong không khí, va chạm liên tục làm quá trình chậm hơn nhiều và công thức chỉ còn là ước lượng định tính về thứ tự nhanh chậm.

**Lỗi thường gặp:**
- Chia áp suất theo tỉ lệ khối lượng các khí — sai vì áp suất do va chạm của từng phân tử gây ra, tỉ lệ với số hạt tức số mol; 2 g H₂ có nhiều phân tử hơn 8 g O₂ rất nhiều.
- Quên trừ áp suất hơi nước khi thu khí trên nước — sai vì ống nghiệm chứa hỗn hợp khí sản phẩm và hơi nước bão hoà, áp suất đọc trên áp kế là áp suất tổng của cả hai.
- Dùng tỉ số khối lượng mol thay vì căn bậc hai trong định luật Graham — sai vì động năng bằng nhau cho v² tỉ lệ nghịch với m, nên tốc độ chỉ tỉ lệ nghịch với căn bậc hai của khối lượng mol.

<sub>`lesson.chemistry.ap-imf-properties.ap-suat-rieng-phan`</sub>

---

### 3. Dung dịch, độ tan và tính chất tập hợp
*Solutions, solubility and colligative properties* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Chuyển đổi được giữa nồng độ mol, nồng độ molan, phân mol và nồng độ phần trăm
- Giải thích được quá trình hoà tan bằng cân bằng năng lượng giữa các tương tác bị phá và được tạo
- Tính được độ tăng điểm sôi, độ hạ điểm đông đặc và áp suất thẩm thấu, có kể hệ số van't Hoff

## Hoà tan là một bài toán năng lượng

Để chất tan hoà tan, phải (1) phá tương tác chất tan - chất tan, (2) phá tương tác dung môi - dung môi, rồi (3) tạo tương tác chất tan - dung môi. Bước 1 và 2 thu nhiệt, bước 3 toả nhiệt. Chất tan tan tốt khi bước 3 bù đủ, tức khi hai bên có **cùng kiểu lực liên phân tử**. Đó chính là nội dung định lượng của câu "giống tan trong giống".

Với khí, độ tan còn tuân định luật Henry: $C = k_H p$ — nồng độ khí tan tỉ lệ áp suất riêng phần của nó. Đây là lí do nước ngọt có ga sủi bọt khi mở nắp.

## Chọn đúng loại nồng độ

- $C_M = n/V_{\text{dd}}$ (mol/L) — tiện cho chuẩn độ, nhưng **thay đổi theo nhiệt độ** vì thể tích giãn nở.
- $b = n/m_{\text{dung môi}}$ (mol/kg) — dùng cho tính chất tập hợp, độc lập nhiệt độ.
- $x_i$ phân mol — dùng cho định luật Raoult.

## Bốn tính chất tập hợp

$$\Delta p = x_{\text{tan}}\, p^\circ \qquad \Delta T_b = i\,K_b\,b \qquad \Delta T_f = i\,K_f\,b \qquad \Pi = i\,cRT$$

Cơ chế chung: hạt chất tan làm giảm phân mol dung môi, do đó giảm áp suất hơi. Đường cong áp suất hơi hạ xuống kéo theo điểm sôi tăng và điểm đông đặc giảm.

## Vì sao phải nhân $i$

NaCl 0,10 mol/kg tạo 0,20 mol hạt/kg vì phân li hoàn toàn thành $\mathrm{Na^+}$ và $\mathrm{Cl^-}$. Với $\mathrm{CaCl_2}$, $i = 3$. Trong thực tế $i$ đo được thường nhỏ hơn giá trị lí thuyết một chút do các ion trái dấu hút nhau tạo cặp ion, hiệu ứng này rõ hơn khi nồng độ tăng.

## Giới hạn

Mọi công thức trên chỉ đúng cho **dung dịch loãng, chất tan không bay hơi**. Khi nồng độ lớn, tương tác ion - ion khiến phải thay nồng độ bằng hoạt độ.

## Lưu ý về phạm vi chương trình

Phần độ tan và định luật Henry nằm trong AP Unit 3. Nhưng **bốn tính chất tập hợp cùng định luật Raoult là nội dung MỞ RỘNG**: College Board đã loại chúng khỏi AP Chemistry CED (có exclusion statement rõ ràng), và chúng cũng không thuộc IB Chemistry hay Cambridge 9701. Học phần này để hiểu sâu bản chất dung dịch và để chuẩn bị cho đại học hoặc olympiad, không phải để luyện thi ba chương trình trên.

**Lỗi thường gặp:**
- Dùng nồng độ mol/L thay cho nồng độ molan trong công thức ΔT = K·b — sai vì K_b và K_f được định nghĩa theo khối lượng dung môi; hai loại nồng độ chỉ gần bằng nhau ở dung dịch rất loãng của dung môi có khối lượng riêng 1 g/mL.
- Bỏ quên hệ số van't Hoff với chất điện li — sai vì tính chất tập hợp đếm số hạt chứ không đếm số đơn vị công thức; một mol CaCl₂ tạo ba mol hạt nên gây hiệu ứng gấp ba lần glucose cùng nồng độ.
- Cho rằng chất tan làm hạ điểm đông đặc bằng cách 'hoà tan tinh thể đá' — sai vì cơ chế thật là hạt chất tan làm giảm thế hoá học của dung môi lỏng, khiến cân bằng lỏng - rắn dịch về nhiệt độ thấp hơn.

<sub>`lesson.chemistry.ap-imf-properties.dung-dich-va-tinh-chat-tap-hop`</sub>

---

### 4. Sắc kí, chưng cất và định luật Beer - Lambert
*Chromatography, distillation and the Beer-Lambert law* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được nguyên lí tách của sắc kí dựa trên sự phân bố giữa pha động và pha tĩnh
- Tính được hệ số lưu giữ Rf và dùng nó để nhận diện chất
- Vận dụng được định luật Beer - Lambert để xác định nồng độ từ độ hấp thụ

## Tách chất bằng sự khác biệt về lực liên phân tử

Sắc kí giấy hay lớp mỏng đặt hai lực cạnh tranh nhau: pha tĩnh (giấy tẩm nước, silica gel) giữ chất lại, pha động (dung môi) kéo chất đi. Chất nào tương tác mạnh hơn với dung môi thì đi xa hơn.

$$R_f = \frac{\text{quãng đường chất}}{\text{quãng đường dung môi}}$$

$R_f$ đặc trưng cho một chất **trong một hệ dung môi và pha tĩnh cụ thể**. Đổi dung môi thì $R_f$ đổi, nên không bao giờ tra $R_f$ từ hệ này để kết luận cho hệ khác. Cách dùng đúng: chạy đồng thời mẫu và chất chuẩn trên cùng bản mỏng.

## Chưng cất phân đoạn

Dựa trên khác biệt nhiệt độ sôi, tức khác biệt lực liên phân tử. Cột phân đoạn tạo nhiều chu trình bay hơi - ngưng tụ liên tiếp; mỗi chu trình làm pha hơi giàu thêm cấu tử dễ bay hơi. Cột càng cao, tách càng tốt. Phương pháp thất bại với **hỗn hợp đẳng phí** (ví dụ ethanol - nước 95,6%) vì tại đó pha hơi có cùng thành phần với pha lỏng.

## Định luật Beer - Lambert

$$A = \varepsilon\,c\,l$$

với $\varepsilon$ là hệ số hấp thụ mol (đặc trưng cho chất và bước sóng), $l$ chiều dày cuvette (thường 1,00 cm), $c$ nồng độ.

Quan hệ với độ truyền qua: $A = -\log T = \log(I_0/I)$. Vì là logarit, $A = 1$ nghĩa là chỉ còn 10% ánh sáng đi qua, $A = 2$ còn 1%.

## Quy trình đường chuẩn

1. Chọn bước sóng ở **cực đại hấp thụ** $\lambda_{\max}$ — ở đó độ nhạy cao nhất và sai số bước sóng ảnh hưởng ít nhất.
2. Đo $A$ của loạt dung dịch chuẩn, vẽ $A$ theo $c$.
3. Nội suy nồng độ mẫu từ đường thẳng qua gốc toạ độ.

## Khi định luật gãy

Tuyến tính chỉ giữ được khi $A \lesssim 1$. Ở nồng độ cao, các phân tử chất tan tương tác với nhau, $\varepsilon$ thay đổi và đồ thị cong xuống. Vì thế mẫu quá đậm phải pha loãng rồi nhân lại hệ số pha loãng, chứ không được ngoại suy.

**Lỗi thường gặp:**
- So sánh Rf đo được với giá trị tra ở tài liệu khác để kết luận chất — sai vì Rf phụ thuộc dung môi, pha tĩnh, nhiệt độ và độ bão hoà buồng chạy; chỉ so sánh được khi chạy song song với chất chuẩn trên cùng bản.
- Coi độ hấp thụ tỉ lệ nghịch tuyến tính với độ truyền qua — sai vì quan hệ là A = −log T, tức phi tuyến; giảm T từ 100% xuống 10% làm A tăng từ 0 lên 1, nhưng từ 10% xuống 1% cũng chỉ tăng thêm 1 đơn vị.
- Ngoại suy đường chuẩn cho mẫu có A lớn hơn 1,5 — sai vì ở nồng độ cao tương tác giữa các phân tử chất tan làm ε thay đổi, đồ thị cong và giá trị nội suy sẽ thấp hơn thực tế.
- Nhúng bản sắc kí ngập vạch xuất phát vào dung môi — sai vì chất sẽ tan thẳng vào bình dung môi thay vì di chuyển theo pha động, khiến không thu được vệt nào.

<sub>`lesson.chemistry.ap-imf-properties.sac-ki-va-beer-lambert`</sub>

---

## Unit 4: Chemical Reactions

### 1. Phân loại phản ứng và phương trình ion thu gọn
*Classifying reactions and net ionic equations* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân loại được phản ứng thành kết tủa, acid - base và oxi hoá khử theo dấu hiệu nhận biết
- Viết được phương trình ion thu gọn bằng cách loại bỏ ion khán giả
- Vận dụng được định luật bảo toàn điện tích để kiểm tra thành phần ion trong dung dịch

## Ba câu hỏi để phân loại một phản ứng

1. Có số oxi hoá nào thay đổi không? Nếu có ⇒ **oxi hoá khử**.
2. Có sự chuyển proton $\mathrm{H^+}$ không? Nếu có ⇒ **acid - base**.
3. Có sản phẩm rời khỏi dung dịch (kết tủa, khí, chất điện li yếu) không? Nếu có ⇒ **trao đổi ion**.

Hỏi theo thứ tự này tránh được nhầm lẫn: phản ứng $\mathrm{Zn + CuSO_4}$ trông như trao đổi nhưng số oxi hoá đổi nên là oxi hoá khử.

## Vì sao viết phương trình ion thu gọn

Phương trình phân tử $\mathrm{AgNO_3 + NaCl \to AgCl + NaNO_3}$ che giấu sự thật: trong dung dịch không tồn tại "phân tử $\mathrm{AgNO_3}$". Chỉ có ion rời rạc. Điều thực sự xảy ra là:

$$\mathrm{Ag^+_{(aq)} + Cl^-_{(aq)} \to AgCl_{(s)}}$$

Phương trình này giải thích vì sao mọi muối bạc tan đều cho cùng kết tủa với mọi muối chloride tan — bản chất chỉ có một.

## Quy trình ba bước

1. Viết phương trình phân tử đã cân bằng, ghi rõ trạng thái.
2. Tách thành ion mọi **chất điện li mạnh tan** (acid mạnh, base mạnh, muối tan). Giữ nguyên dạng phân tử: chất rắn, khí, chất lỏng, acid yếu, base yếu.
3. Gạch ion giống nhau hai vế, viết lại phần còn lại và kiểm tra cân bằng cả nguyên tố lẫn điện tích.

## Bảng tan tối thiểu cần thuộc

- Luôn tan: muối của nhóm 1, $\mathrm{NH_4^+}$, $\mathrm{NO_3^-}$, hầu hết acetate.
- Halide tan trừ $\mathrm{Ag^+, Pb^{2+}, Hg_2^{2+}}$.
- Sulfate tan trừ $\mathrm{Ba^{2+}, Sr^{2+}, Pb^{2+}}$ (rất ít tan) và $\mathrm{Ca^{2+}}$ (ít tan) — độ tan giảm dần khi đi xuống nhóm 2.
- Carbonate, phosphate, sulfide, hydroxide **không tan** trừ nhóm 1 và $\mathrm{NH_4^+}$.

## Bảo toàn điện tích như công cụ giải nhanh

Trong một dung dịch, $\sum n_+ \cdot |z_+| = \sum n_- \cdot |z_-|$. Hệ thức này cho phép tìm nồng độ một ion còn thiếu mà không cần biết ion đó đến từ muối nào — rất mạnh trong bài toán hỗn hợp.

**Lỗi thường gặp:**
- Tách acid yếu như CH₃COOH thành ion trong phương trình ion — sai vì acid yếu chỉ điện li một phần, phần lớn tồn tại dạng phân tử; viết tách sẽ làm phương trình ion thu gọn mất luôn chất tham gia chính.
- Gạch ion khán giả mà quên kiểm tra lại cân bằng điện tích hai vế — sai vì phương trình ion đúng phải cân bằng cả số nguyên tử lẫn tổng điện tích; bỏ sót một điện tích là dấu hiệu đã gạch nhầm.
- Cân bằng bảo toàn điện tích theo số mol ion mà quên nhân với độ lớn điện tích — sai vì một mol Mg²⁺ mang hai mol điện tích dương, gấp đôi một mol Na⁺.

<sub>`lesson.chemistry.ap-chemical-reactions.phuong-trinh-ion-thu-gon`</sub>

---

### 2. Hoá học phân tích định lượng: chuẩn độ và chuẩn độ ngược
*Quantitative analysis: titration and back titration* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Thực hiện được tính toán chuẩn độ theo hệ thức tỉ lượng tổng quát
- Giải thích được khi nào phải dùng chuẩn độ ngược thay vì chuẩn độ trực tiếp
- Đánh giá được sai số phần trăm và nguồn sai số hệ thống trong phép chuẩn độ

## Hệ thức trung tâm

$$\frac{n_A}{a} = \frac{n_B}{b} \quad\Longleftrightarrow\quad \frac{C_A V_A}{a} = \frac{C_B V_B}{b}$$

với $a$, $b$ là hệ số trong phương trình. Bỏ qua hệ số là lỗi phổ biến nhất: chuẩn độ $\mathrm{H_2SO_4}$ bằng NaOH cần $b/a = 2$, nên $C\!V$ của NaOH gấp đôi $C\!V$ của acid tại điểm tương đương.

## Quy trình chuẩn: ba lần đồng nhất

Phép chuẩn độ đáng tin đòi hỏi ít nhất ba kết quả đồng nhất (chênh nhau dưới 0,10 cm³). Lần đầu là lần "thô" để ước lượng, không đưa vào trung bình. Chỉ lấy trung bình các giá trị đồng nhất.

## Khi nào phải chuẩn độ ngược

Ba tình huống buộc dùng kĩ thuật này:

- Chất phân tích là **chất rắn không tan** hoặc tan chậm (ví dụ $\mathrm{CaCO_3}$ trong vỏ trứng).
- Phản ứng trực tiếp **quá chậm**, điểm cuối không sắc nét.
- **Không có chỉ thị phù hợp** cho phản ứng trực tiếp.

Sơ đồ tính: $n_{\text{phản ứng với mẫu}} = n_{\text{thêm vào}} - n_{\text{dư chuẩn độ được}}$. Mọi sai lầm ở bài chuẩn độ ngược đều bắt nguồn từ việc quên phép trừ này.

## Sai số và cách kiểm soát

$$\text{sai số \%} = \frac{|\text{giá trị đo} - \text{giá trị lí thuyết}|}{\text{giá trị lí thuyết}}\times 100\%$$

Sai số dụng cụ: buret đọc được tới $\pm 0{,}05$ cm³ mỗi lần đọc, mà mỗi phép đo thể tích cần hai lần đọc nên sai số tuyệt đối là $\pm 0{,}10$ cm³. Vì thế **dùng thể tích chuẩn độ lớn hơn 20 cm³** sẽ giảm sai số tương đối xuống dưới 0,5%.

Sai số hệ thống hay gặp: buret chưa tráng bằng dung dịch chuẩn (làm loãng, thể tích đo tăng), pipet còn giọt cuối (không được thổi ra), bình nón được tráng bằng dung dịch chuẩn thay vì nước cất (thêm chất, thể tích đo tăng).

**Lỗi thường gặp:**
- Dùng trực tiếp số mol chất chuẩn làm số mol chất phân tích mà không nhân tỉ lệ hệ số — sai vì phương trình mới cho biết tỉ lệ phản ứng; với H₂SO₄ và NaOH tỉ lệ là 1:2 nên bỏ qua sẽ sai đúng hai lần.
- Trong chuẩn độ ngược, lấy luôn số mol chuẩn độ được làm số mol phản ứng với mẫu — sai vì phần chuẩn độ được là phần thuốc thử còn dư, phải lấy tổng ban đầu trừ đi phần dư.
- Tráng bình nón bằng dung dịch chất phân tích trước khi chuẩn độ — sai vì làm thế thêm một lượng chất phân tích không xác định vào bình, khiến thể tích chất chuẩn tiêu tốn lớn hơn thực tế và kết quả bị thổi phồng.
- Đưa cả kết quả chuẩn độ thô vào giá trị trung bình — sai vì lần thô thường vượt quá điểm cuối do chưa biết khoảng, làm trung bình lệch lên.

<sub>`lesson.chemistry.ap-chemical-reactions.chuan-do-dinh-luong`</sub>

---

### 3. Phản ứng oxi hoá khử và cân bằng bằng nửa phản ứng
*Redox reactions and balancing by half-equations* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Xác định được số oxi hoá của nguyên tố trong phân tử và ion đa nguyên tử
- Cân bằng được phương trình oxi hoá khử bằng phương pháp nửa phản ứng trong môi trường acid và base
- Vận dụng được bảo toàn electron để giải bài toán định lượng oxi hoá khử

## Quy tắc số oxi hoá

Áp theo thứ tự ưu tiên, gặp mâu thuẫn thì quy tắc đứng trước thắng:

1. Đơn chất: 0. Ion đơn nguyên tử: bằng điện tích.
2. F luôn $-1$. Kim loại nhóm 1: $+1$; nhóm 2: $+2$.
3. H là $+1$ (trừ hydride kim loại: $-1$).
4. O là $-2$ (trừ peroxide: $-1$; superoxide: $-1/2$; $\mathrm{OF_2}$: $+2$).
5. Tổng số oxi hoá bằng 0 trong phân tử, bằng điện tích trong ion.

Số oxi hoá **có thể là phân số** — trong $\mathrm{Fe_3O_4}$ sắt có số oxi hoá trung bình $+8/3$, phản ánh hỗn hợp Fe(II) và Fe(III).

## Cân bằng nửa phản ứng trong môi trường acid

Quy trình "O-H-e":

1. Cân bằng nguyên tố chính (không phải O, H).
2. Cân bằng O bằng cách thêm $\mathrm{H_2O}$.
3. Cân bằng H bằng cách thêm $\mathrm{H^+}$.
4. Cân bằng điện tích bằng cách thêm $e^-$ vào vế cần thiết.
5. Nhân hai nửa phản ứng để số electron bằng nhau, rồi cộng.

Ví dụ: $\mathrm{MnO_4^- + 8H^+ + 5e^- \to Mn^{2+} + 4H_2O}$.

## Chuyển sang môi trường base

Không cân bằng lại từ đầu. Làm như môi trường acid, rồi thêm vào **cả hai vế** số $\mathrm{OH^-}$ bằng số $\mathrm{H^+}$, ghép $\mathrm{H^+ + OH^- \to H_2O}$ và rút gọn nước. Lí do: $\mathrm{H^+}$ không tồn tại đáng kể trong môi trường base, nhưng phép biến đổi này bảo toàn cả nguyên tố lẫn điện tích nên hợp lệ.

## Bảo toàn electron: lối tắt định lượng

$$\sum n_{\text{chất khử}}\cdot(\text{số e nhường}) = \sum n_{\text{chất oxi hoá}}\cdot(\text{số e nhận})$$

Hệ thức này cho phép giải bài toán hỗn hợp nhiều kim loại tác dụng với nhiều chất oxi hoá mà không cần viết đủ mọi phương trình — chỉ cần biết trạng thái đầu và cuối của mỗi nguyên tố.

**Lỗi thường gặp:**
- Dùng H⁺ trong phương trình cân bằng cuối cùng ở môi trường base — sai vì trong dung dịch base nồng độ H⁺ cực nhỏ, phương trình phải mô tả tiểu phân thực sự có mặt là OH⁻ và H₂O.
- Quên nhân hai nửa phản ứng để số electron bằng nhau trước khi cộng — sai vì electron không được sinh ra hay mất đi; nếu số electron hai vế không triệt tiêu hết thì phương trình vẫn còn electron tự do, điều không tồn tại trong dung dịch.
- Coi số oxi hoá luôn là số nguyên — sai vì trong hợp chất như Fe₃O₄ hay S₄O₆²⁻ giá trị trung bình là phân số, phản ánh việc các nguyên tử cùng nguyên tố ở trạng thái khác nhau.
- Cân bằng oxygen bằng cách thêm O₂ — sai vì O₂ là một chất tham gia phản ứng thật, thêm vào sẽ thay đổi bản chất hoá học; oxygen phải cân bằng bằng H₂O trong dung dịch.

<sub>`lesson.chemistry.ap-chemical-reactions.oxi-hoa-khu-va-nua-phan-ung`</sub>

---

## Unit 5: Kinetics

### 1. Tốc độ phản ứng và các phương pháp đo
*Reaction rate and methods of measurement* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Định nghĩa được tốc độ phản ứng theo một chất và theo phương trình tổng quát
- Lựa chọn được phương pháp đo tốc độ phù hợp với từng loại phản ứng
- Xác định được tốc độ tức thời từ hệ số góc tiếp tuyến của đồ thị nồng độ theo thời gian

## Định nghĩa cho một con số duy nhất

Với $\mathrm{2N_2O_5 \to 4NO_2 + O_2}$, nồng độ $\mathrm{NO_2}$ tăng nhanh gấp 4 lần $\mathrm{O_2}$. Nếu mỗi người báo tốc độ theo một chất khác nhau sẽ ra bốn con số. Để thống nhất, ta chia cho hệ số:

$$v = -\frac{1}{a}\frac{\Delta[A]}{\Delta t} = \frac{1}{c}\frac{\Delta[C]}{\Delta t}$$

Dấu trừ đứng trước chất phản ứng vì nồng độ chúng giảm, mà tốc độ luôn là số dương.

## Chọn phương pháp đo theo dấu hiệu quan sát được

Nguyên tắc: tìm một đại lượng vật lí thay đổi tỉ lệ với mức độ phản ứng.

- **Có khí thoát ra**: đo thể tích khí bằng ống đong úp nước hoặc syringe; hoặc đặt bình trên cân điện tử và theo dõi khối lượng giảm.
- **Có màu thay đổi**: đo độ hấp thụ bằng máy quang phổ (dùng định luật Beer - Lambert để đổi ra nồng độ).
- **Có ion sinh ra hoặc mất đi**: đo độ dẫn điện.
- **Có thay đổi pH**: dùng pH kế và ghi dữ liệu liên tục.
- **Phương pháp lấy mẫu và làm ngưng phản ứng**: hút mẫu theo thời gian, làm lạnh đột ngột hoặc pha loãng để "đóng băng" phản ứng rồi chuẩn độ.
- **Phương pháp đồng hồ** (clock reaction): đo thời gian $t$ tới khi xuất hiện dấu hiệu cố định; khi đó $v \propto 1/t$.

## Đồ thị nồng độ - thời gian

Đường cong luôn dốc nhất ở đầu rồi thoải dần, vì nồng độ chất phản ứng giảm nên tần suất va chạm hiệu quả giảm. Muốn có tốc độ tại thời điểm $t$, vẽ tiếp tuyến tại điểm đó và lấy độ dốc. Đây là kĩ năng thực hành bị chấm điểm trong cả IB IA lẫn A-Level Paper 3.

## Vì sao ưu tiên tốc độ đầu

Tại $t = 0$ ta biết chính xác nồng độ mọi chất, chưa có sản phẩm nên chưa có phản ứng nghịch, và chưa có sản phẩm nào có thể xúc tác hay ức chế. Đó là lí do phương pháp xác định bậc phản ứng chuẩn mực dựa trên tốc độ đầu chứ không dựa trên tốc độ ở giữa quá trình.

**Lỗi thường gặp:**
- Báo tốc độ phản ứng bằng tốc độ biến thiên của một chất bất kì mà không chia hệ số — sai vì mỗi chất biến đổi với tốc độ riêng tỉ lệ với hệ số của nó, chỉ sau khi chia hệ số mới thu được một giá trị chung cho cả phản ứng.
- Dùng tốc độ trung bình trên một khoảng dài để thay cho tốc độ tức thời — sai vì đồ thị nồng độ - thời gian là đường cong; trung bình trên khoảng rộng luôn nhỏ hơn tốc độ đầu và lớn hơn tốc độ cuối khoảng.
- Bỏ dấu trừ trong định nghĩa theo chất phản ứng rồi báo tốc độ âm — sai vì tốc độ theo quy ước là đại lượng dương mô tả mức độ tiến triển; dấu trừ chỉ để bù cho việc Δ[A] âm.

<sub>`lesson.chemistry.ap-kinetics.toc-do-phan-ung-va-cach-do`</sub>

---

### 2. Biểu thức tốc độ, bậc phản ứng và phương pháp tốc độ đầu
*Rate law, reaction order and the initial rates method* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Xác định được bậc riêng phần của từng chất từ bảng số liệu tốc độ đầu
- Giải thích được vì sao bậc phản ứng phải xác định bằng thực nghiệm chứ không suy từ phương trình
- Suy ra được đơn vị của hằng số tốc độ từ bậc chung của phản ứng

## Điều bất ngờ đầu tiên của động học

Phương trình $\mathrm{2NO_2 + F_2 \to 2NO_2F}$ có hệ số 2 trước $\mathrm{NO_2}$, nhưng biểu thức tốc độ thực nghiệm lại là $v = k[\mathrm{NO_2}][\mathrm{F_2}]$ — bậc 1 theo $\mathrm{NO_2}$.

**Không suy được bậc từ hệ số tỉ lượng.** Phương trình tổng thể mô tả cân bằng vật chất giữa đầu và cuối; tốc độ lại do bước chậm nhất trong cơ chế quyết định. Đây là ranh giới quan trọng nhất của Unit 5.

## Phương pháp tốc độ đầu

Thiết kế thí nghiệm: giữ mọi nồng độ cố định, chỉ đổi một chất. Khi đó

$$\frac{v_2}{v_1} = \left(\frac{[A]_2}{[A]_1}\right)^m \;\Rightarrow\; m = \frac{\ln(v_2/v_1)}{\ln([A]_2/[A]_1)}$$

Trong đề thi, tỉ số nồng độ thường là 2 hoặc 3 nên đọc trực tiếp: gấp đôi nồng độ mà tốc độ không đổi ⇒ bậc 0; tốc độ gấp đôi ⇒ bậc 1; gấp bốn ⇒ bậc 2; gấp tám ⇒ bậc 3.

## Ý nghĩa của bậc 0

Bậc 0 theo một chất **không** có nghĩa chất đó không cần thiết. Nó có nghĩa chất đó không xuất hiện trong bước quyết định tốc độ (hoặc trước bước đó), ví dụ vì bề mặt xúc tác đã bão hoà.

## Đơn vị của k tự nói lên bậc

Từ $v = k\,[\;]^{n}$ với $v$ đơn vị $\mathrm{mol\,L^{-1}s^{-1}}$:

$$[k] = \mathrm{mol^{1-n}\,L^{n-1}\,s^{-1}}$$

- Bậc 0: $\mathrm{mol\,L^{-1}s^{-1}}$
- Bậc 1: $\mathrm{s^{-1}}$
- Bậc 2: $\mathrm{L\,mol^{-1}s^{-1}}$

Mẹo kiểm tra bài làm: nếu đơn vị $k$ tính ra không khớp với bậc chung vừa tìm, chắc chắn có sai sót ở đâu đó.

## Giới hạn

Biểu thức tốc độ chỉ mô tả **giai đoạn đầu** của phản ứng thuận nghịch. Khi sản phẩm tích tụ, phản ứng nghịch trở nên đáng kể và tốc độ quan sát được không còn tuân biểu thức đơn giản này.

**Lỗi thường gặp:**
- Lấy hệ số tỉ lượng trong phương trình làm bậc riêng phần — sai vì phương trình tổng thể chỉ mô tả cân bằng vật chất, còn tốc độ do bước chậm quyết định; chỉ với phản ứng cơ bản một bước hai đại lượng này mới trùng nhau.
- So sánh hai thí nghiệm mà cả hai nồng độ đều thay đổi rồi gán toàn bộ thay đổi tốc độ cho một chất — sai vì không tách được đóng góp của từng chất, phải chọn cặp thí nghiệm khống chế biến.
- Bỏ đơn vị của k hoặc dùng chung một đơn vị cho mọi bậc — sai vì đơn vị của k phụ thuộc bậc chung; báo k bằng s⁻¹ cho phản ứng bậc 2 là mâu thuẫn thứ nguyên và làm mọi tính toán tiếp theo sai.

<sub>`lesson.chemistry.ap-kinetics.bieu-thuc-toc-do-va-bac`</sub>

---

### 3. Phương trình động học tích phân và đồ thị tuyến tính hoá
*Integrated rate laws and linearised plots* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Viết được dạng tích phân của phương trình động học bậc 0, bậc 1 và bậc 2
- Xác định được bậc phản ứng bằng cách tìm đồ thị nào cho đường thẳng
- Vận dụng được đặc điểm chu kì bán huỷ để nhận diện phản ứng bậc 1

## Từ vi phân sang tích phân

Biểu thức tốc độ cho biết tốc độ **tại một thời điểm**. Muốn dự đoán nồng độ **sau thời gian t**, phải tích phân.

| Bậc | Dạng tích phân | Đồ thị thẳng | Độ dốc | $t_{1/2}$ |
|---|---|---|---|---|
| 0 | $[A] = [A]_0 - kt$ | $[A]$ theo $t$ | $-k$ | $[A]_0/2k$ |
| 1 | $\ln[A] = \ln[A]_0 - kt$ | $\ln[A]$ theo $t$ | $-k$ | $\ln 2/k$ |
| 2 | $\dfrac{1}{[A]} = \dfrac{1}{[A]_0} + kt$ | $1/[A]$ theo $t$ | $+k$ | $1/(k[A]_0)$ |

Lưu ý dấu: chỉ bậc 2 có độ dốc dương, vì $1/[A]$ tăng khi $[A]$ giảm.

## Chiến lược xác định bậc từ số liệu

Vẽ cả ba đồ thị (hoặc tính hệ số tương quan cho cả ba). Đồ thị nào cho đường thẳng đẹp nhất thì bậc tương ứng là đáp án. Đây là cách duy nhất khi chỉ có **một** thí nghiệm theo dõi theo thời gian, không có bộ số liệu tốc độ đầu.

## Dấu hiệu nhận biết nhanh bậc 1

Với bậc 1, $t_{1/2} = \ln 2 / k$ **không phụ thuộc nồng độ đầu**. Hệ quả: đo các chu kì bán huỷ liên tiếp trên cùng một đường cong, nếu chúng bằng nhau thì chắc chắn bậc 1.

So sánh: bậc 0 có $t_{1/2}$ giảm dần (mỗi chu kì sau ngắn hơn); bậc 2 có $t_{1/2}$ tăng dần (mỗi chu kì sau dài gấp đôi chu kì trước). Ba hành vi này phân biệt được bằng mắt.

## Ứng dụng

Phân rã phóng xạ, thải trừ thuốc khỏi huyết tương và phân huỷ nhiều chất hữu cơ đều là bậc 1. Đó là lí do liều thuốc được kê theo chu kì cố định: sau mỗi $t_{1/2}$ nồng độ giảm nửa, bất kể liều ban đầu là bao nhiêu.

## Điều kiện áp dụng

Các công thức trên viết cho phản ứng chỉ phụ thuộc **một** chất. Với phản ứng nhiều chất, phải dùng kĩ thuật cô lập: cho các chất khác dư rất nhiều để nồng độ chúng coi như không đổi, khi đó phản ứng trở thành "bậc giả" theo chất còn lại.

**Lỗi thường gặp:**
- Cho rằng mọi phản ứng đều có chu kì bán huỷ không đổi — sai vì tính chất này là đặc trưng riêng của bậc 1; với bậc 2 chu kì bán huỷ tỉ lệ nghịch với nồng độ nên tăng dần theo thời gian.
- Vẽ đồ thị 1/[A] theo t rồi lấy độ dốc là −k — sai dấu, vì với bậc 2 nghịch đảo nồng độ tăng theo thời gian nên độ dốc dương và bằng đúng +k.
- Dùng công thức tích phân bậc 1 cho phản ứng hai chất mà không cô lập — sai vì công thức được suy ra từ giả thiết tốc độ chỉ phụ thuộc một nồng độ; muốn dùng phải cho các chất khác dư để nồng độ chúng gần như không đổi.
- Nhầm ln với log thập phân khi tính k từ độ dốc — sai vì phương trình tích phân bậc 1 dùng logarit tự nhiên; nếu vẽ log[A] theo t thì độ dốc là −k/2,303 chứ không phải −k.

<sub>`lesson.chemistry.ap-kinetics.phuong-trinh-tich-phan`</sub>

---

### 4. Cơ chế phản ứng, bước quyết định tốc độ và xấp xỉ tiền cân bằng
*Reaction mechanisms, rate-determining step and pre-equilibrium approximation* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Kiểm tra được một cơ chế đề xuất có phù hợp với biểu thức tốc độ thực nghiệm hay không
- Phân biệt được chất trung gian và chất xúc tác trong dãy các bước cơ bản
- Vận dụng được xấp xỉ tiền cân bằng khi bước chậm không phải bước đầu tiên

## Cơ chế là giả thuyết, không phải sự thật

Ta không quan sát trực tiếp được từng va chạm. Cơ chế là một mô hình được **đề xuất** rồi kiểm tra bằng hai tiêu chuẩn bắt buộc:

1. Tổng các bước cơ bản phải cho đúng phương trình tổng thể (mọi chất trung gian triệt tiêu).
2. Biểu thức tốc độ suy từ cơ chế phải trùng biểu thức thực nghiệm.

Thoả cả hai không chứng minh cơ chế đúng — chỉ nghĩa là chưa bị bác bỏ.

## Trường hợp đơn giản: bước chậm là bước đầu

Khi đó biểu thức tốc độ đọc thẳng từ bước chậm, và với bước cơ bản thì bậc **bằng** hệ số. Ví dụ cơ chế:

$$\mathrm{NO_2 + NO_2 \to NO_3 + NO} \quad (\text{chậm})$$
$$\mathrm{NO_3 + CO \to NO_2 + CO_2} \quad (\text{nhanh})$$

cho $v = k[\mathrm{NO_2}]^2$, giải thích tại sao CO không xuất hiện trong biểu thức tốc độ dù có mặt trong phương trình tổng.

## Trường hợp khó: bước chậm là bước thứ hai

Nếu bước 1 nhanh và thuận nghịch, bước 2 chậm, thì biểu thức tốc độ từ bước 2 sẽ chứa **chất trung gian** — điều không chấp nhận được, vì nồng độ chất trung gian không đo được.

Cách xử lí là **xấp xỉ tiền cân bằng**: bước 1 đạt cân bằng nhanh nên

$$K_1 = \frac{[\text{trung gian}]}{[A][B]} \;\Rightarrow\; [\text{trung gian}] = K_1[A][B]$$

Thay vào biểu thức của bước chậm, ta khử được chất trung gian và thu biểu thức chỉ chứa các chất đo được. Hằng số quan sát được là tích $k_{\text{qs}} = k_2 K_1$.

## Phân biệt trung gian và xúc tác

- **Trung gian**: xuất hiện lần đầu ở **vế phải** một bước, rồi biến mất ở vế trái bước sau.
- **Xúc tác**: xuất hiện lần đầu ở **vế trái** một bước, được tái tạo ở vế phải bước sau.

Cả hai đều triệt tiêu khi cộng các bước, nên phải nhìn thứ tự xuất hiện chứ không chỉ nhìn kết quả cộng.

## Giới hạn

Phân tử số của một bước cơ bản hầu như không vượt quá 2, vì xác suất ba tiểu phân va chạm đồng thời đúng hướng là cực nhỏ. Một "bước cơ bản" ba phân tử trong đề bài thường là dấu hiệu cơ chế đó không thực tế.

**Lỗi thường gặp:**
- Viết biểu thức tốc độ tổng thể còn chứa chất trung gian — sai vì nồng độ chất trung gian rất nhỏ và không đo được; biểu thức tốc độ phải chỉ chứa các chất có thể pha chế và đo nồng độ.
- Dùng hệ số tỉ lượng của phương trình tổng thể làm bậc — sai vì chỉ bước cơ bản mới có bậc bằng hệ số; phương trình tổng thể là tổng nhiều bước nên không mang thông tin động học.
- Nhầm chất xúc tác với chất trung gian vì cả hai đều không có trong phương trình tổng — sai vì phải nhìn thứ tự: xúc tác bị tiêu thụ trước rồi tái tạo sau, còn trung gian được tạo trước rồi tiêu thụ sau.
- Đề xuất bước cơ bản có ba phân tử va chạm đồng thời — sai vì xác suất ba tiểu phân gặp nhau cùng lúc với đúng định hướng là cực nhỏ, nên cơ chế như vậy không có ý nghĩa vật lí.

<sub>`lesson.chemistry.ap-kinetics.co-che-phan-ung`</sub>

---

### 5. Năng lượng hoạt hoá, phương trình Arrhenius và xúc tác
*Activation energy, the Arrhenius equation and catalysis* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao tăng nhiệt độ làm tốc độ tăng nhanh hơn nhiều so với mức tăng động năng trung bình
- Xác định được năng lượng hoạt hoá từ đồ thị Arrhenius
- Phân tích được cách xúc tác làm tăng tốc độ mà không bị tiêu hao

## Câu hỏi mấu chốt

Tăng nhiệt độ từ 300 K lên 310 K chỉ làm động năng trung bình tăng 3%. Vậy vì sao tốc độ phản ứng thường **tăng gấp đôi**?

## Câu trả lời nằm ở đuôi phân bố

Phản ứng chỉ xảy ra với những phân tử ở **đuôi phải** của phân bố Maxwell - Boltzmann, tức là có $E \ge E_a$. Tỉ lệ này cho bởi thừa số Boltzmann:

$$f = e^{-E_a/RT}$$

Hàm mũ rất nhạy. Với $E_a = 50$ kJ/mol, tăng $T$ từ 300 lên 310 K làm $f$ tăng khoảng 1,9 lần — đúng bằng quan sát thực nghiệm. Điểm cần hiểu: nhiệt độ không làm cả đường phân bố dịch đều, nó làm **đuôi phải phình lên rất mạnh** trong khi đỉnh hạ xuống và dịch phải.

## Phương trình Arrhenius

$$k = A\,e^{-E_a/RT} \qquad\Longleftrightarrow\qquad \ln k = \ln A - \frac{E_a}{R}\cdot\frac{1}{T}$$

Dạng logarit là dạng dùng để xử lí số liệu: vẽ $\ln k$ theo $1/T$ được đường thẳng có độ dốc $-E_a/R$ và tung độ gốc $\ln A$. Từ độ dốc: $E_a = -R\times(\text{độ dốc})$, luôn dương vì độ dốc âm.

Thừa số $A$ (thừa số tần số) gộp tần suất va chạm và yếu tố định hướng — hai phân tử có thể đủ năng lượng nhưng va chạm sai hướng thì vẫn không phản ứng.

## Xúc tác làm gì và không làm gì

**Làm**: mở một đường phản ứng khác có $E_a$ thấp hơn, khiến phần diện tích dưới đường Maxwell - Boltzmann vượt ngưỡng tăng vọt. Tăng tốc **cả chiều thuận lẫn chiều nghịch** như nhau.

**Không làm**: không thay đổi $\Delta H$, không thay đổi hằng số cân bằng $K$, không dịch chuyển vị trí cân bằng, không làm phản ứng không tự diễn biến trở nên tự diễn biến.

Xúc tác dị thể (rắn, phản ứng khí hoặc lỏng) hoạt động qua hấp phụ - phản ứng - giải hấp; xúc tác đồng thể tham gia tạo chất trung gian rồi được tái tạo. Enzyme là xúc tác sinh học có tính chọn lọc cực cao và bị biến tính khi vượt nhiệt độ tối ưu — đó là lí do đồ thị tốc độ - nhiệt độ của enzyme có cực đại, khác hẳn dạng tăng đơn điệu của Arrhenius.

**Lỗi thường gặp:**
- Giải thích tốc độ tăng theo nhiệt độ chỉ bằng 'phân tử chuyển động nhanh hơn nên va chạm nhiều hơn' — sai vì tần suất va chạm chỉ tăng vài phần trăm khi tăng 10 K, không đủ giải thích việc tốc độ gấp đôi; nguyên nhân chính là tỉ lệ phân tử vượt Ea tăng theo hàm mũ.
- Nói xúc tác làm tăng hiệu suất hay dịch chuyển cân bằng về phía sản phẩm — sai vì xúc tác giảm Ea của cả chiều thuận và chiều nghịch một lượng như nhau, nên K không đổi; nó chỉ giúp đạt cân bằng nhanh hơn.
- Lấy độ dốc đồ thị ln k theo 1/T làm luôn Ea — sai vì độ dốc bằng −Ea/R, phải nhân với −R mới ra Ea; quên bước này làm kết quả nhỏ đi khoảng 8000 lần và mang dấu âm.
- Vẽ đường Maxwell - Boltzmann ở nhiệt độ cao hơn với đỉnh cao hơn — sai vì diện tích dưới đường luôn bằng tổng số phân tử; khi T tăng đường phải thấp hơn và tù hơn, đồng thời trải rộng về phía năng lượng cao.

<sub>`lesson.chemistry.ap-kinetics.arrhenius-va-xuc-tac`</sub>

---

## Unit 6: Thermodynamics I - Thermochemistry

### 1. Nội năng, enthalpy và quy ước dấu
*Internal energy, enthalpy and sign conventions* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · co-ban

**Mục tiêu:**
- Phân biệt được nhiệt, công và nội năng trong nguyên lí thứ nhất nhiệt động lực học
- Giải thích được vì sao enthalpy là đại lượng thuận tiện cho quá trình ở áp suất không đổi
- Xác định được dấu của biến thiên enthalpy từ mô tả thí nghiệm

## Nguyên lí thứ nhất

$$\Delta U = q + w$$

Năng lượng không tự sinh ra hay mất đi, chỉ chuyển giữa hệ và môi trường dưới hai hình thức: nhiệt $q$ và công $w$. Quy ước lấy **hệ làm gốc**: cái gì đi vào hệ mang dấu dương.

## Vì sao cần enthalpy

Hầu hết phản ứng trong ống nghiệm xảy ra ở áp suất khí quyển không đổi, và nếu có khí sinh ra thì hệ phải đẩy không khí ra xa, tức thực hiện công $w = -p\Delta V$. Khi đó nhiệt đo được không bằng $\Delta U$.

Định nghĩa $H = U + pV$ giải quyết gọn vấn đề: ở $p$ không đổi,

$$\Delta H = \Delta U + p\Delta V = q_p$$

Nghĩa là **nhiệt lượng đo được ở áp suất không đổi chính là ΔH**. Đó là toàn bộ lí do enthalpy tồn tại.

## Đọc dấu từ hiện tượng

- $\Delta H < 0$ — **toả nhiệt**: hệ nhả năng lượng, nhiệt độ môi trường (dung dịch, nhiệt kế) **tăng**. Sản phẩm có enthalpy thấp hơn chất phản ứng.
- $\Delta H > 0$ — **thu nhiệt**: hệ hút năng lượng, nhiệt độ đo được **giảm**.

Chỗ hay lẫn: nhiệt kế đo môi trường, không đo hệ. Dung dịch nóng lên nghĩa là phản ứng **toả** nhiệt, tức $\Delta H$ **âm**.

## Điều kiện chuẩn và trạng thái chuẩn

Kí hiệu $\Delta H^\circ$ đòi hỏi áp suất 100 kPa, mọi dung dịch 1 mol/dm³, và mỗi chất ở dạng bền nhất. Từ đó:

$$\Delta H_f^\circ(\text{đơn chất bền nhất}) = 0$$

Ví dụ $\Delta H_f^\circ(\mathrm{O_2, g}) = 0$ nhưng $\Delta H_f^\circ(\mathrm{O_3, g}) = +142$ kJ/mol, vì ozone không phải dạng bền nhất của oxygen.

## Giới hạn

Dấu của $\Delta H$ **không** quyết định phản ứng có xảy ra hay không. Nhiều phản ứng thu nhiệt vẫn tự diễn biến (như hoà tan $\mathrm{NH_4NO_3}$). Yếu tố quyết định là năng lượng Gibbs — nội dung Unit 9.

**Lỗi thường gặp:**
- Kết luận ΔH dương khi thấy nhiệt độ dung dịch tăng — sai vì nhiệt kế đo môi trường; môi trường nóng lên nghĩa là hệ đã nhả năng lượng ra, tức phản ứng toả nhiệt và ΔH âm.
- Gán ΔHf° = 0 cho mọi dạng thù hình của một nguyên tố — sai vì chỉ dạng bền nhất ở điều kiện chuẩn mới có giá trị 0; kim cương có ΔHf° = +1,9 kJ/mol vì graphite mới là dạng chuẩn của carbon.
- Cho rằng phản ứng thu nhiệt thì không thể tự xảy ra — sai vì tính tự diễn biến do ΔG quyết định; khi ΔS dương đủ lớn thì số hạng −TΔS thắng ΔH dương và phản ứng vẫn xảy ra.
- Dùng nhiệt lượng đo được ở thể tích không đổi làm ΔH — sai vì ở thể tích không đổi hệ không thực hiện công giãn nở, nên nhiệt đo được là ΔU chứ không phải ΔH; hai giá trị chênh nhau một lượng Δn(khí)·RT.

<sub>`lesson.chemistry.ap-thermochemistry.noi-nang-va-enthalpy`</sub>

---

### 2. Nhiệt lượng kế: đo enthalpy bằng thực nghiệm
*Calorimetry: measuring enthalpy experimentally* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Tính được biến thiên enthalpy từ số liệu nhiệt lượng kế cốc xốp và bom nhiệt lượng
- Vận dụng được phép ngoại suy đồ thị để hiệu chỉnh mất nhiệt
- Đánh giá được các giả thiết và nguồn sai số của phép đo nhiệt lượng

## Nguyên lí

Ta không đo được enthalpy của hệ. Ta chỉ đo được nhiệt độ của **môi trường** quanh nó rồi suy ngược:

$$q = m\,c\,\Delta T \qquad \Delta H = -\frac{q_{\text{môi trường}}}{n}$$

Dấu trừ và phép chia cho số mol chất **giới hạn** là hai chỗ sai kinh điển.

## Nhiệt lượng kế cốc xốp

Dùng cho phản ứng trong dung dịch ở áp suất không đổi, cho $\Delta H$ trực tiếp. Ba giả thiết ngầm:

1. Khối lượng dung dịch ≈ khối lượng nước.
2. Nhiệt dung riêng dung dịch ≈ $4{,}18\ \mathrm{J\,g^{-1}K^{-1}}$.
3. Cốc và nhiệt kế không hấp thụ nhiệt đáng kể.

Mỗi giả thiết là một nguồn sai số cần nêu khi đánh giá thí nghiệm.

## Hiệu chỉnh bằng ngoại suy

Với phản ứng chậm, nhiệt thoát ra môi trường trong lúc phản ứng còn đang xảy ra, nên $T_{\max}$ đọc được luôn **thấp hơn** giá trị lí thuyết. Cách xử lí chuẩn:

1. Ghi nhiệt độ 2-3 phút trước khi trộn (đường nền).
2. Trộn, ghi tiếp tới khi nhiệt độ bắt đầu giảm đều.
3. Vẽ đường thẳng qua đoạn nguội, **kéo ngược về thời điểm trộn**.
4. Đọc $T$ tại giao điểm — đó là nhiệt độ cực đại nếu phản ứng xảy ra tức thời và không mất nhiệt.

Không làm bước này thì $|\Delta H|$ đo được luôn nhỏ hơn giá trị thật.

## Bom nhiệt lượng

Thể tích cố định nên $w = 0$ và $q_V = \Delta U$. Toàn bộ thiết bị hấp thụ nhiệt, nên phải chuẩn hoá trước bằng chất chuẩn (thường acid benzoic) để tìm $C_{\text{cal}}$:

$$q = C_{\text{cal}}\,\Delta T$$

Chuyển sang enthalpy: $\Delta H = \Delta U + \Delta n_{\text{khí}}RT$. Với phản ứng đốt cháy hydrocarbon, $\Delta n$ thường nhỏ nên chênh lệch chỉ vài kJ/mol — nhưng vẫn phải nêu khi so sánh với giá trị bảng.

**Lỗi thường gặp:**
- Dùng khối lượng chỉ của một trong hai dung dịch khi tính q — sai vì sau khi trộn cả hai dung dịch đều được làm nóng lên cùng một ΔT, nên khối lượng phải là tổng.
- Chia nhiệt lượng cho số mol của chất dư thay vì chất giới hạn — sai vì chỉ phần chất phản ứng hết mới sinh ra toàn bộ nhiệt lượng đo được; chia sai làm ΔH nhỏ đi tuỳ ý.
- Đọc trực tiếp nhiệt độ cực đại trên nhiệt kế mà không ngoại suy — sai vì trong lúc phản ứng đang diễn ra hệ đã mất nhiệt ra không khí, nên giá trị đọc được luôn thấp hơn giá trị lí thuyết và |ΔH| bị đánh giá thấp.
- Dùng số liệu bom nhiệt lượng làm ΔH mà không hiệu chỉnh — sai vì bom hoạt động ở thể tích không đổi nên cho ΔU; muốn có ΔH phải cộng Δn(khí)RT.

<sub>`lesson.chemistry.ap-thermochemistry.nhiet-luong-ke`</sub>

---

### 3. Enthalpy liên kết và enthalpy tạo thành
*Bond enthalpies and enthalpies of formation* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Tính được biến thiên enthalpy của phản ứng theo năng lượng liên kết và theo nhiệt tạo thành
- Giải thích được vì sao hai phương pháp cho kết quả khác nhau và phương pháp nào chính xác hơn
- Xác định được chiều của phép trừ trong mỗi công thức bằng lập luận chu trình

## Hai công thức, hai chiều trừ ngược nhau

$$\Delta H = \sum E(\text{liên kết bị phá}) - \sum E(\text{liên kết được tạo})$$
$$\Delta H = \sum \Delta H_f(\text{sản phẩm}) - \sum \Delta H_f(\text{chất phản ứng})$$

Chiều trừ ngược nhau và đây là nguồn nhầm lẫn số một. Đừng học thuộc — hãy suy từ chu trình.

**Với năng lượng liên kết**: phá liên kết luôn **thu** nhiệt (dương), tạo liên kết luôn **toả** (âm). Đi từ chất phản ứng lên nguyên tử tự do rồi xuống sản phẩm, ta cộng phần đi lên và trừ phần đi xuống ⇒ phá trừ tạo.

**Với nhiệt tạo thành**: mũi tên hình thành đều đi **từ đơn chất vào**, nên đi từ chất phản ứng phải đi ngược (trừ) rồi đi xuôi vào sản phẩm (cộng) ⇒ sản phẩm trừ chất phản ứng.

## Vì sao hai cách cho kết quả khác nhau

Enthalpy liên kết là giá trị **trung bình**. Năng lượng phân li liên kết C-H **thứ nhất** của methane là 439 kJ/mol, ba liên kết còn lại có giá trị khác hẳn (trung bình của cả bốn chỉ là 416); sang ethanol hay chloroform con số lại khác nữa, nhưng bảng chỉ ghi một giá trị trung bình duy nhất là 413. Vì thế phương pháp năng lượng liên kết chỉ cho kết quả **gần đúng**.

Thêm hai hạn chế: nó chỉ áp dụng cho chất ở **thể khí** (không kể enthalpy hoá hơi), và không mô tả được năng lượng cộng hưởng — đó là lí do giá trị tính cho benzene lệch khoảng 150 kJ/mol so với thực nghiệm.

Phương pháp nhiệt tạo thành dùng giá trị đo riêng cho **từng chất cụ thể**, kể cả trạng thái vật lí, nên **chính xác hơn**. Khi đề cho cả hai bộ dữ liệu, hãy chọn nhiệt tạo thành.

## Enthalpy đốt cháy

Dùng khi không có nhiệt tạo thành (nhiều hợp chất hữu cơ không tổng hợp trực tiếp được từ đơn chất). Chú ý chiều trừ **đảo lại**:

$$\Delta H = \sum \Delta H_c(\text{chất phản ứng}) - \sum \Delta H_c(\text{sản phẩm})$$

vì mũi tên đốt cháy đi **ra khỏi** chất, ngược với mũi tên tạo thành.

**Lỗi thường gặp:**
- Áp chiều trừ 'sản phẩm trừ chất phản ứng' cho công thức năng lượng liên kết — sai vì hai công thức có chiều mũi tên ngược nhau trong chu trình; với liên kết phải là 'phá trừ tạo', áp nhầm sẽ đảo dấu ΔH.
- Đếm số liên kết không nhân với hệ số phân tử — sai vì 2NH₃ chứa 6 liên kết N-H chứ không phải 3; đếm thiếu làm kết quả sai hàng trăm kJ.
- Dùng năng lượng liên kết cho phản ứng có chất lỏng hoặc rắn — sai vì bảng năng lượng liên kết định nghĩa cho quá trình phá liên kết ở thể khí, không kể enthalpy hoá hơi hay enthalpy mạng lưới.
- Cho rằng năng lượng liên kết cho kết quả chính xác hơn nhiệt tạo thành vì 'gần với bản chất liên kết hơn' — sai vì giá trị liên kết là trung bình trên nhiều hợp chất, trong khi nhiệt tạo thành đo riêng cho từng chất cụ thể ở đúng trạng thái vật lí.

<sub>`lesson.chemistry.ap-thermochemistry.enthalpy-lien-ket-va-tao-thanh`</sub>

---

### 4. Định luật Hess và chu trình năng lượng
*Hess's law and energy cycles* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · trung-binh

**Mục tiêu:**
- Phát biểu và chứng minh được định luật Hess từ tính chất hàm trạng thái của enthalpy
- Xây dựng được chu trình năng lượng để tính enthalpy không đo trực tiếp được
- Xử lí được phép nhân hệ số và phép đảo chiều phương trình khi tổ hợp

## Vì sao định luật Hess đúng

Enthalpy là hàm trạng thái. Đi từ A tới B bằng đường nào cũng vậy, $\Delta H = H_B - H_A$. Nếu không đúng, ta có thể đi vòng theo đường tốn ít năng lượng rồi quay về theo đường sinh nhiều năng lượng, tạo ra năng lượng từ hư không — mâu thuẫn nguyên lí thứ nhất.

Đây là lí do định luật Hess không phải một quy tắc thực nghiệm riêng lẻ mà là hệ quả logic bắt buộc.

## Vì sao cần định luật Hess

Nhiều $\Delta H$ không đo trực tiếp được:

- $\mathrm{C(s) + \tfrac{1}{2}O_2 \to CO(g)}$: không thể ngăn một phần thành $\mathrm{CO_2}$.
- Enthalpy mạng lưới của NaCl: không thể tách rời từng ion mà quan sát.
- Enthalpy tạo thành của nhiều chất hữu cơ: không tổng hợp trực tiếp từ đơn chất được.

Giải pháp là vòng qua các phản ứng **đo được** (thường là phản ứng đốt cháy) rồi tổ hợp.

## Ba phép biến đổi hợp lệ

1. **Đảo chiều** phương trình ⇒ đổi dấu $\Delta H$.
2. **Nhân hệ số** $n$ ⇒ nhân $\Delta H$ với $n$ (enthalpy là đại lượng khuếch độ, tỉ lệ với lượng chất).
3. **Cộng** các phương trình ⇒ cộng các $\Delta H$.

## Kĩ thuật vẽ chu trình

Đặt chất phản ứng và sản phẩm ở hàng trên, các chất trung gian chung (đơn chất, hoặc sản phẩm cháy $\mathrm{CO_2}$ và $\mathrm{H_2O}$) ở hàng dưới. Vẽ mũi tên theo chiều của định nghĩa từng loại enthalpy. Sau đó **đi theo mũi tên thì cộng, đi ngược mũi tên thì trừ**.

Quy tắc này tự động sinh ra hai công thức của bài trước: mũi tên tạo thành hướng lên (từ đơn chất) nên công thức là sản phẩm trừ chất phản ứng; mũi tên đốt cháy hướng xuống nên công thức đảo lại.

## Một cảnh báo

Định luật Hess chỉ nói về **enthalpy**, không nói gì về tốc độ hay khả năng xảy ra. Một chu trình cho $\Delta H$ rất âm không bảo đảm phản ứng sẽ xảy ra — kim cương chuyển thành graphite có $\Delta H$ âm nhưng mất hàng tỉ năm vì rào năng lượng hoạt hoá quá cao.

**Lỗi thường gặp:**
- Đổi chiều phương trình mà quên đổi dấu ΔH — sai vì enthalpy của quá trình nghịch bằng đúng số đối của quá trình thuận; giữ nguyên dấu tương đương với việc khẳng định năng lượng tự sinh ra.
- Nhân hệ số phương trình mà không nhân ΔH — sai vì enthalpy là đại lượng khuếch độ tỉ lệ với số mol; đốt hai mol carbon toả gấp đôi nhiệt so với một mol.
- Dùng công thức 'sản phẩm trừ chất phản ứng' cho dữ kiện nhiệt đốt cháy — sai vì mũi tên đốt cháy đi ra khỏi chất chứ không đi vào như mũi tên tạo thành, nên chiều trừ phải đảo lại.
- Kết luận phản ứng sẽ xảy ra vì chu trình Hess cho ΔH rất âm — sai vì định luật Hess chỉ nói về chênh lệch enthalpy giữa hai trạng thái, hoàn toàn không đề cập rào năng lượng hoạt hoá hay yếu tố entropy.

<sub>`lesson.chemistry.ap-thermochemistry.dinh-luat-hess`</sub>

---

## Unit 7: Equilibrium

### 1. Cân bằng động, hằng số Kc và Kp
*Dynamic equilibrium, Kc and Kp* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Giải thích được bản chất động của trạng thái cân bằng hoá học
- Viết được biểu thức Kc và Kp đúng quy ước về trạng thái tập hợp
- Chuyển đổi được giữa Kp và Kc bằng hệ thức chứa Δn khí

## Cân bằng không phải là đứng yên

Dấu hiệu vĩ mô của cân bằng là nồng độ không đổi. Nhưng ở cấp phân tử, phản ứng thuận và nghịch vẫn diễn ra liên tục — chỉ là **cùng tốc độ**. Bằng chứng: dùng đồng vị đánh dấu, sau khi hệ đạt cân bằng nguyên tử đánh dấu vẫn phân tán vào cả hai phía.

Hai điều kiện bắt buộc: hệ phải **kín** (không mất chất) và nhiệt độ phải **không đổi**.

## Viết biểu thức K

$$\mathrm{aA + bB \rightleftharpoons cC + dD} \qquad K_c = \frac{[\mathrm{C}]^c[\mathrm{D}]^d}{[\mathrm{A}]^a[\mathrm{B}]^b}$$

Quy ước loại trừ: **chất rắn nguyên chất và chất lỏng nguyên chất không xuất hiện** trong biểu thức. Lí do: hoạt độ của chúng bằng 1 vì "nồng độ" của một chất rắn nguyên chất là hằng số không phụ thuộc lượng có mặt. Hệ quả thực tế quan trọng: thêm bớt $\mathrm{CaCO_3}$ rắn không làm dịch chuyển cân bằng nung vôi.

Nước cũng bị loại **khi là dung môi**, nhưng phải giữ lại khi tham gia ở thể khí.

## Kp và quan hệ với Kc

Với phản ứng khí, tiện hơn khi dùng áp suất riêng phần:

$$K_p = K_c(RT)^{\Delta n}, \qquad \Delta n = \sum \nu_{\text{khí, sp}} - \sum \nu_{\text{khí, pư}}$$

Khi $\Delta n = 0$ (số mol khí hai vế bằng nhau) thì $K_p = K_c$. Đó là trường hợp của $\mathrm{H_2 + I_2 \rightleftharpoons 2HI}$.

## Đọc ý nghĩa của giá trị K

- $K \gg 1$: cân bằng lệch mạnh về sản phẩm.
- $K \approx 1$: lượng đáng kể cả hai phía.
- $K \ll 1$: hầu như không phản ứng.

K **chỉ phụ thuộc nhiệt độ**. Thay đổi nồng độ, áp suất hay thêm xúc tác đều **không** làm K đổi — chúng chỉ làm hệ tạm rời cân bằng rồi trở về đúng giá trị K cũ.

## Ba biến đổi hay gặp

Đảo chiều phản ứng: $K' = 1/K$. Nhân phương trình với $n$: $K' = K^n$. Cộng hai phương trình: $K = K_1 K_2$.

**Lỗi thường gặp:**
- Đưa chất rắn hoặc chất lỏng nguyên chất vào biểu thức K — sai vì hoạt độ của chúng bằng 1; hệ quả là thêm bớt lượng chất rắn không dịch chuyển cân bằng, điều mà biểu thức sai sẽ dự đoán ngược lại.
- Cho rằng thêm xúc tác làm tăng K — sai vì xúc tác giảm năng lượng hoạt hoá cả hai chiều một lượng như nhau, tỉ số k(thuận)/k(nghịch) không đổi nên K giữ nguyên; xúc tác chỉ rút ngắn thời gian đạt cân bằng.
- Dùng R = 8,314 khi muốn Kp theo atm — sai vì giá trị R phải tương thích đơn vị áp suất; dùng nhầm sẽ cho kết quả lệch khoảng 10⁵ lần.
- Nhầm 'nồng độ không đổi' với 'nồng độ các chất bằng nhau' — sai vì tại cân bằng các nồng độ thường rất khác nhau, chỉ có điều chúng không còn thay đổi theo thời gian.

<sub>`lesson.chemistry.ap-equilibrium.can-bang-dong-kc-kp`</sub>

---

### 2. Thương số phản ứng Q và kĩ thuật bảng ICE
*Reaction quotient Q and the ICE table method* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- So sánh được Q với K để dự đoán chiều diễn biến của hệ chưa cân bằng
- Lập được bảng ICE để tính nồng độ cân bằng từ nồng độ ban đầu
- Áp dụng và kiểm tra được phép xấp xỉ bỏ qua x theo quy tắc 5%

## Q trả lời câu hỏi "hệ sẽ đi về đâu"

K cho biết đích đến; Q cho biết ta đang ở đâu. So sánh hai giá trị:

- $Q < K$: thiếu sản phẩm ⇒ phản ứng đi **thuận** (sang phải).
- $Q > K$: thừa sản phẩm ⇒ phản ứng đi **nghịch**.
- $Q = K$: đã cân bằng, không có biến đổi ròng.

Cách nhớ bản chất: hệ luôn tìm cách đưa Q về bằng K.

## Bảng ICE

| | I (ban đầu) | C (biến thiên) | E (cân bằng) |
|---|---|---|---|
| A | $[A]_0$ | $-ax$ | $[A]_0 - ax$ |
| C | 0 | $+cx$ | $cx$ |

Ba quy tắc bắt buộc:

1. Dòng C phải theo **tỉ lệ hệ số**: nếu A mất $2x$ thì C được $3x$ khi tỉ lệ là 2:3.
2. Mọi giá trị phải là **nồng độ** (mol/L), không phải số mol — nếu đề cho mol thì chia thể tích trước.
3. Chiều biến đổi xác định bằng Q so với K, không đoán bừa.

Sau đó thay dòng E vào biểu thức K và giải phương trình theo $x$.

## Phép xấp xỉ và điều kiện dùng

Khi $K$ rất nhỏ, phản ứng xảy ra không đáng kể nên $x \ll [A]_0$ và ta viết $[A]_0 - x \approx [A]_0$. Điều này biến phương trình bậc hai thành phương trình bậc nhất, tiết kiệm rất nhiều công.

**Nhưng phải kiểm tra**: tính $x$ rồi so $x/[A]_0$. Nếu vượt 5%, phép xấp xỉ không hợp lệ và phải giải lại bằng phương trình bậc hai đầy đủ. Kinh nghiệm: xấp xỉ thường an toàn khi $[A]_0/K > 400$.

## Loại nghiệm vô lí

Phương trình bậc hai cho hai nghiệm. Loại nghiệm nào làm một nồng độ trở nên **âm** — đó không phải nghiệm hoá học dù đúng về đại số. Đây là bước bắt buộc trong lời giải hoàn chỉnh.

**Lỗi thường gặp:**
- Quên nhân hệ số tỉ lượng vào dòng Change của bảng ICE — sai vì tỉ lệ biến thiên các chất bị phương trình ràng buộc; với N₂O₄ ⇌ 2NO₂ mà viết +x thay vì +2x thì kết quả sai gấp bội.
- Dùng phép xấp xỉ bỏ qua x mà không kiểm tra quy tắc 5% — sai vì khi K không đủ nhỏ so với nồng độ đầu, x chiếm phần đáng kể và bỏ qua nó làm sai số vượt xa dung sai thí nghiệm.
- Đưa số mol thay vì nồng độ vào bảng ICE khi thể tích khác 1 L — sai vì Kc được định nghĩa theo nồng độ; chỉ khi V = 1,00 L hai giá trị mới trùng nhau về số.
- Nhận cả hai nghiệm của phương trình bậc hai — sai vì nghiệm cho nồng độ âm không có ý nghĩa vật lí, phải loại và nêu rõ lí do loại.

<sub>`lesson.chemistry.ap-equilibrium.thuong-so-q-va-bang-ice`</sub>

---

### 3. Nguyên lí Le Chatelier và ảnh hưởng của điều kiện lên cân bằng
*Le Chatelier's principle and effects of changing conditions* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Dự đoán được chiều dịch chuyển cân bằng khi thay đổi nồng độ, áp suất hoặc nhiệt độ
- Phân biệt được yếu tố làm dịch chuyển cân bằng với yếu tố làm thay đổi hằng số K
- Vận dụng được nguyên lí vào điều kiện công nghiệp của quá trình Haber và Contact

## Cách hiểu đúng nguyên lí

Le Chatelier là quy tắc định tính, hệ quả của việc hệ luôn kéo Q trở lại bằng K. Muốn kiểm chứng bất kì dự đoán nào, hãy tính lại Q và so với K.

## Bốn tác động

**Thay đổi nồng độ**: thêm chất ⇒ hệ dịch chuyển theo chiều tiêu thụ chất đó. Lấy bớt sản phẩm liên tục là kĩ thuật công nghiệp then chốt để "kéo" phản ứng chạy mãi. K **không đổi**.

**Thay đổi áp suất bằng cách nén** (chỉ ảnh hưởng hệ có khí): hệ dịch về phía **ít mol khí hơn** để giảm áp suất. Nếu số mol khí hai vế bằng nhau thì không có dịch chuyển. K **không đổi**.

**Thêm khí trơ ở thể tích không đổi**: áp suất tổng tăng nhưng áp suất riêng phần từng chất không đổi, nên Q không đổi ⇒ **không dịch chuyển**. Đây là câu hỏi bẫy kinh điển.

**Thay đổi nhiệt độ**: đây là yếu tố duy nhất làm **K thay đổi**. Coi nhiệt như một chất:

- Toả nhiệt ($\Delta H < 0$): nhiệt ở vế sản phẩm. Tăng $T$ ⇒ dịch nghịch ⇒ $K$ **giảm**.
- Thu nhiệt ($\Delta H > 0$): tăng $T$ ⇒ dịch thuận ⇒ $K$ **tăng**.

## Xúc tác

Không dịch chuyển cân bằng, không đổi K. Nó tăng tốc độ cả hai chiều như nhau nên chỉ giúp **đạt cân bằng sớm hơn**. Trong công nghiệp đây lại là giá trị lớn nhất: sản lượng theo giờ tăng dù hiệu suất cân bằng giữ nguyên.

## Vì sao Haber chạy ở 450 °C

$$\mathrm{N_2 + 3H_2 \rightleftharpoons 2NH_3} \qquad \Delta H = -92\ \mathrm{kJ/mol}$$

Toả nhiệt nên nhiệt độ **thấp** cho hiệu suất cao — nhưng ở nhiệt độ thấp tốc độ quá chậm, phải chờ hàng tháng. Chọn 450 °C là **thoả hiệp**: hiệu suất khoảng 15% nhưng đạt nhanh, và ammonia được hoá lỏng tách ra liên tục còn khí chưa phản ứng được tuần hoàn nên hiệu suất tổng thể tiến tới trên 97%.

Áp suất 200 atm: vế phải ít mol khí hơn (2 so với 4) nên nén giúp tăng hiệu suất; giới hạn là chi phí và độ bền thiết bị.

**Lỗi thường gặp:**
- Cho rằng thêm khí trơ ở thể tích không đổi làm dịch chuyển cân bằng vì áp suất tổng tăng — sai vì Q chỉ phụ thuộc áp suất riêng phần của các chất tham gia, mà những giá trị này không đổi khi thể tích và số mol chúng không đổi.
- Nói rằng tăng nhiệt độ luôn làm hiệu suất tăng vì phản ứng nhanh hơn — sai vì tốc độ và hiệu suất là hai khái niệm khác nhau; với phản ứng toả nhiệt, tăng nhiệt độ làm K giảm nên hiệu suất cân bằng giảm dù đạt nhanh hơn.
- Cho rằng xúc tác làm tăng hiệu suất — sai vì xúc tác không đổi K; nó chỉ rút ngắn thời gian đạt tới cùng một trạng thái cân bằng.
- Áp dụng ảnh hưởng của áp suất cho cân bằng chỉ gồm chất lỏng và rắn — sai vì chất ngưng tụ gần như không nén được, thay đổi áp suất không làm đổi nồng độ của chúng đáng kể.

<sub>`lesson.chemistry.ap-equilibrium.le-chatelier`</sub>

---

### 4. Tích số tan Ksp, độ tan và hiệu ứng ion chung
*Solubility product, molar solubility and the common ion effect* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Liên hệ được tích số tan với độ tan mol của chất điện li ít tan
- Dự đoán được sự tạo thành kết tủa bằng cách so sánh Q với Ksp
- Giải thích được vì sao ion chung, pH và sự tạo phức làm thay đổi độ tan

## Ksp chỉ là K của một cân bằng đặc biệt

$$\mathrm{Ca(OH)_2(s) \rightleftharpoons Ca^{2+}(aq) + 2OH^-(aq)} \qquad K_{sp} = [\mathrm{Ca^{2+}}][\mathrm{OH^-}]^2$$

Chất rắn không xuất hiện theo đúng quy ước hoạt độ. Vì thế **thêm bao nhiêu chất rắn cũng không làm tăng nồng độ ion** trong dung dịch đã bão hoà.

## Từ Ksp ra độ tan và ngược lại

Với $\mathrm{M_aX_b}$, đặt độ tan mol là $s$: $[\mathrm{M}] = as$, $[\mathrm{X}] = bs$, nên

$$K_{sp} = (as)^a (bs)^b = a^a b^b\, s^{a+b}$$

Hệ quả quan trọng: **không so sánh trực tiếp Ksp của hai muối có công thức khác kiểu**. $\mathrm{AgCl}$ có $K_{sp} = 1{,}8\times10^{-10}$ còn $\mathrm{Ag_2CrO_4}$ có $K_{sp} = 1{,}1\times10^{-12}$ nhỏ hơn, nhưng độ tan của $\mathrm{Ag_2CrO_4}$ ($6{,}5\times10^{-5}$ M) lại **lớn hơn** của AgCl ($1{,}3\times10^{-5}$ M), vì số mũ khác nhau.

## Dự đoán kết tủa

Tính $Q_{sp}$ với nồng độ **sau khi trộn** (nhớ pha loãng!):

- $Q < K_{sp}$: chưa bão hoà, không kết tủa.
- $Q = K_{sp}$: vừa bão hoà.
- $Q > K_{sp}$: quá bão hoà, có kết tủa cho tới khi $Q$ về bằng $K_{sp}$.

## Ba cách làm đổi độ tan

**Ion chung** — giảm độ tan. Thêm $\mathrm{NaCl}$ vào dung dịch bão hoà AgCl làm $[\mathrm{Cl^-}]$ tăng, hệ dịch về phía kết tủa. Đây là cơ sở của kĩ thuật rửa kết tủa bằng dung dịch loãng chứa ion chung thay vì nước cất.

**pH** — tăng độ tan nếu anion là base yếu. $\mathrm{CaCO_3}$ tan trong acid vì $\mathrm{CO_3^{2-}}$ bị $\mathrm{H^+}$ lấy đi, kéo cân bằng hoà tan sang phải. Đây là hoá học của hang động đá vôi và của mưa acid ăn mòn công trình.

**Tạo phức** — tăng độ tan. AgCl không tan trong nước nhưng tan trong dung dịch $\mathrm{NH_3}$ vì tạo $\mathrm{[Ag(NH_3)_2]^+}$, làm $[\mathrm{Ag^+}]$ tự do giảm mạnh.

## Giới hạn

Ksp mô tả tốt các muối rất ít tan. Với muối tan vừa phải, lực ion cao khiến phải dùng hoạt độ thay nồng độ, và giá trị tính theo Ksp sẽ lệch đáng kể so với thực nghiệm.

**Lỗi thường gặp:**
- So sánh trực tiếp giá trị Ksp của các muối có tỉ lệ ion khác nhau để kết luận muối nào tan hơn — sai vì quan hệ giữa Ksp và độ tan chứa số mũ phụ thuộc công thức; phải quy về độ tan mol rồi mới so sánh.
- Quên hệ số 2 khi viết [F⁻] = 2s trong bảng ICE — sai vì mỗi đơn vị CaF₂ tan ra cho hai ion F⁻; bỏ sót làm kết quả sai hàng chục lần do số mũ bậc ba.
- Cho rằng thêm chất rắn ít tan vào dung dịch bão hoà sẽ làm tăng nồng độ ion — sai vì hoạt độ chất rắn nguyên chất bằng 1 và không xuất hiện trong Ksp; phần rắn thêm vào chỉ nằm lại ở đáy.
- Không pha loãng nồng độ khi trộn hai dung dịch trước khi tính Q — sai vì thể tích tổng lớn hơn thể tích từng phần, nồng độ mỗi ion đều giảm; bỏ qua bước này thường cho kết luận có kết tủa trong khi thực tế chưa bão hoà.

<sub>`lesson.chemistry.ap-equilibrium.ksp-va-ion-chung`</sub>

---

## Unit 7: IChO - Chiến lược bài toán và vòng thực hành

### 1. Chiến lược bài toán cân bằng nhiều nấc
*Strategy for multi-equilibrium problems* · THPT (lớp 10-12) · olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Lập được hệ phương trình đầy đủ gồm cân bằng, bảo toàn khối lượng và cân bằng điện tích
- Viết được điều kiện proton để rút gọn hệ phương trình
- Vận dụng được phân số nồng độ alpha để tính nhanh thành phần dung dịch theo pH

## Vì sao bài cân bằng IChO khó

Dung dịch thực có nhiều cân bằng xảy ra **đồng thời**: phân li acid nhiều nấc, tự phân li của nước, tạo phức, kết tủa. Bài thi không cho biết cân bằng nào chi phối; đó chính là phần phải suy luận.

## Bộ phương trình đầy đủ

Với $n$ dạng tồn tại, luôn viết được đủ $n$ phương trình:

1. **Các hằng số cân bằng**: mỗi cân bằng một biểu thức $K$.
2. **Bảo toàn khối lượng**: tổng nồng độ các dạng của một nguyên tố bằng nồng độ ban đầu.
3. **Trung hoà điện tích**: tổng điện tích dương bằng tổng điện tích âm.
4. **Tích số ion của nước**: $K_w=[H^+][OH^-]$.

Hệ này **luôn giải được** nhưng thường là phương trình bậc cao. Nghệ thuật là biết bỏ số hạng nào.

## Điều kiện proton: rút gọn nhanh

Chọn mức tham chiếu (thường là các chất được thêm vào), rồi viết: tổng nồng độ các dạng đã **nhận** proton bằng tổng các dạng đã **cho** proton. Ví dụ dung dịch $NaHA$:

$$[H^+]+[H_2A]=[A^{2-}]+[OH^-].$$

Một phương trình này thay cho việc kết hợp bảo toàn khối lượng và điện tích, ít sai sót hơn nhiều.

## Phân số alpha: công cụ tính nhanh

Với acid $n$ nấc, gọi $h=[H^+]$:

$$\alpha_j=\frac{h^{\,n-j}\prod_{i\le j}K_i}{\sum_{k=0}^{n}h^{\,n-k}\prod_{i\le k}K_i}.$$

Biết pH là biết ngay toàn bộ thành phần. Đây là cách chuẩn để trả lời "ở pH = 7, dạng nào chiếm ưu thế?" mà không cần giải hệ.

## Trình tự làm bài

1. Liệt kê **mọi** dạng tồn tại và mọi cân bằng có thể.
2. So sánh các hằng số: nếu $K_1/K_2>10^4$ thì hai nấc tách nhau, xử lí riêng từng nấc.
3. Ước lượng pH sơ bộ để biết dạng nào chiếm ưu thế.
4. Viết phương trình rút gọn, giải, rồi **kiểm tra lại** mọi giả thiết bỏ qua.

**Lỗi thường gặp:**
- Coi $NaHCO_3$ chỉ là base (hoặc chỉ là acid) rồi dùng công thức một chiều — sai vì ion lưỡng tính tham gia đồng thời hai cân bằng ngược chiều; bỏ một chiều làm pH lệch cả đơn vị.
- Bỏ qua tự phân li của nước trong dung dịch rất loãng — sai vì khi $C$ nhỏ tới cỡ $10^{-6}$ M, đóng góp $K_w$ trở nên đáng kể và nồng độ $H^+$ không thể nhỏ hơn $10^{-7}$ M.
- Dùng nồng độ ban đầu thay cho nồng độ cân bằng trong biểu thức $K$ mà không kiểm tra — sai vì phép gần đúng đó chỉ hợp lệ khi độ phân li nhỏ hơn khoảng 5%; với acid tương đối mạnh nó sai lệch lớn.

<sub>`lesson.chemistry.icho.can-bang-nhieu-nac`</sub>

---

### 2. Khi nào được dùng gần đúng và sai số kèm theo
*When approximations are valid and how large the error is* · THPT (lớp 10-12) · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Kiểm tra được tiêu chuẩn 5 phần trăm trước và sau khi dùng phép gần đúng
- Phân tích được sai số tương đối do bỏ qua một số hạng trong biểu thức cân bằng
- Xác định được khi nào bắt buộc phải giải phương trình bậc cao đầy đủ

## Gần đúng không phải là cẩu thả

Ở IChO, phép gần đúng **được khuyến khích** — nhưng phải kèm hai thứ: điều kiện áp dụng và ước lượng sai số. Một lời giải chính xác đến 6 chữ số mà mất 40 phút thua một lời giải gần đúng 3 chữ số kèm câu "sai số dưới 1%" trong 8 phút.

## Ba phép gần đúng hay dùng nhất

**1. Bỏ qua $x$ so với $C$.** Trong $K_a=\dfrac{x^2}{C-x}$, nếu $x\ll C$ thì $x\approx\sqrt{K_aC}$. Điều kiện: $\sqrt{K_a/C}<0{,}05$, tức $C>400K_a$. Sai số tương đối của $x$ xấp xỉ $\dfrac{x}{2C}$.

**2. Bỏ qua tự phân li của nước.** Hợp lệ khi $[H^+]$ tính được lớn hơn $10^{-6}$ M. Với acid rất yếu hoặc rất loãng thì không được.

**3. Xấp xỉ nồng độ ổn định (Bodenstein).** Trong động học, đặt $\dfrac{d[\text{trung gian}]}{dt}\approx0$. Điều kiện: chất trung gian phải **rất hoạt động**, tức tốc độ tiêu thụ nó lớn hơn nhiều tốc độ sinh ra; nồng độ nó luôn nhỏ.

## Quy trình bắt buộc

1. Giả sử phép gần đúng đúng, tính kết quả.
2. **Kiểm tra ngược** điều kiện với kết quả vừa tính.
3. Nếu không thoả, dùng **lặp liên tiếp**: thay giá trị vừa tính vào biểu thức chính xác, tính lại. Thường 2-3 vòng là hội tụ tới 3 chữ số — nhanh hơn giải phương trình bậc ba.
4. Ghi rõ trong bài: "Kiểm tra: $x/C=0{,}03<0{,}05$, phép gần đúng chấp nhận được".

## Khi bắt buộc giải đầy đủ

- Acid trung bình mạnh với nồng độ nhỏ ($K_a$ và $C$ cùng bậc).
- Hỗn hợp hai acid có $K_a$ chênh nhau dưới $10^{4}$.
- Bài yêu cầu độ chính xác cao (ví dụ tính sai số chuẩn độ).

Trong các trường hợp đó, phương trình bậc ba theo $[H^+]$ là bắt buộc; hãy giải bằng lặp hoặc bằng chức năng SOLVE của máy tính.

**Lỗi thường gặp:**
- Dùng phép gần đúng mà không kiểm tra ngược — sai vì điều kiện áp dụng phụ thuộc chính kết quả cần tìm; không kiểm tra thì không biết mình đang sai 1% hay 100%.
- Áp xấp xỉ nồng độ ổn định cho chất trung gian bền — sai vì điều kiện của Bodenstein là chất trung gian bị tiêu thụ rất nhanh; với chất trung gian tích luỹ được thì đạo hàm của nó không nhỏ.
- Kết luận nghiệm âm của phương trình bậc hai cũng là đáp án — sai vì nồng độ phải dương; nghiệm âm là nghiệm toán học không có ý nghĩa hoá học và phải loại tường minh.

<sub>`lesson.chemistry.icho.khi-nao-duoc-dung-gan-dung`</sub>

---

### 4. Suy luận cấu trúc từ dữ liệu phổ: quy trình đọc MS, IR và NMR
*Structure elucidation from MS, IR and NMR data* · THPT (lớp 10-12) · olympiad · 50 phút · nang-cao

**Mục tiêu:**
- Xác định được công thức phân tử và độ bất bão hoà từ phổ khối lượng
- Xác định được nhóm chức từ các vùng hấp thụ đặc trưng của phổ hồng ngoại
- Suy ra được khung carbon từ số tín hiệu, tích phân và độ bội của phổ NMR proton

## Trình tự đọc chuẩn: MS trước, IR sau, NMR cuối

Đây không phải sở thích mà là chiến thuật: mỗi phổ thu hẹp không gian tìm kiếm cho phổ tiếp theo.

**Bước 1 - Phổ khối (MS).**
- Pic ion phân tử $M^+$ cho phân tử khối.
- **Quy tắc nitơ**: $M$ lẻ $\Rightarrow$ số nguyên tử N lẻ.
- Pic $M+1$: $\dfrac{I_{M+1}}{I_M}\approx1{,}1\%\times n_C$ cho số nguyên tử carbon.
- Pic $M+2$ cao bằng $M$ $\Rightarrow$ có Br; cao bằng $\frac13 M$ $\Rightarrow$ có Cl.
- Mảnh mất: $-15$ (CH$_3$), $-17$ (OH), $-18$ (H$_2$O), $-29$ (CHO hoặc C$_2$H$_5$), $-45$ (COOH).
- Từ công thức phân tử, tính ngay **độ bất bão hoà**.

**Bước 2 - Phổ hồng ngoại (IR): nhận nhóm chức.**
- $3200$-$3600$ rộng: O-H (alcohol/acid).
- $\approx3300$ nhọn: N-H hoặc C-H alkyne.
- $1700\pm40$ mạnh: C=O (ester $\approx1735$, aldehyde/ketone $\approx1715$, acid $\approx1710$, amide $\approx1650$).
- $1600$ và $1500$: vòng thơm.
- $2250$: C$\equiv$N hoặc C$\equiv$C.

**Bước 3 - NMR proton: dựng khung.**
- **Số tín hiệu** = số loại proton không tương đương.
- **Tích phân** = tỉ lệ số proton mỗi loại.
- **Độ dịch chuyển**: $0{,}9$ (CH$_3$ alkyl), $2{,}1$ (cạnh C=O), $3{,}5$ (cạnh O), $5$-$6$ (alkene), $7$-$8$ (thơm), $9$-$10$ (CHO), $10$-$12$ (COOH).
- **Độ bội**: $n+1$ vạch với $n$ proton kề.

## Cách ghép thông tin

Viết ra các **mảnh** đã chắc chắn, đếm nguyên tử còn dư, rồi ghép sao cho khớp cả độ bất bão hoà lẫn mô hình tách vạch. Cuối cùng **kiểm tra ngược**: dự đoán lại phổ từ cấu trúc đề xuất và đối chiếu từng dữ kiện.

## Bẫy hay gặp

Proton của OH và NH thường **không tách vạch** (do trao đổi nhanh) và có độ dịch chuyển thay đổi theo dung môi. Đừng dùng chúng để đếm proton lân cận.

**Lỗi thường gặp:**
- Dùng độ bội của tín hiệu OH để đếm proton lân cận — sai vì proton của OH trao đổi nhanh với dung môi nên thường xuất hiện dạng singlet rộng, không phản ánh số proton kề.
- Bỏ qua độ bất bão hoà khi đề xuất cấu trúc — sai vì cấu trúc phải khớp CHÍNH XÁC số vòng cộng liên kết pi tính từ công thức phân tử; lệch một đơn vị là cấu trúc sai.
- Nhầm đỉnh C=O của ester với của ketone — sai vì hai nhóm cách nhau khoảng 25 cm$^{-1}$ ($1735$ so với $1715$); dùng thêm sự có mặt của tín hiệu $CH_2$ ở $\delta$ khoảng 4 để phân biệt chắc chắn.

<sub>`lesson.chemistry.icho.suy-luan-cau-truc-tu-pho`</sub>

---

### 7. Chiến thuật vòng thực hành IChO: chuẩn độ, tổng hợp và phân tích
*IChO practical round strategy* · THPT (lớp 10-12) · olympiad · 50 phút · nang-cao

**Mục tiêu:**
- Lập được kế hoạch thời gian cho một buổi thực hành nhiều nhiệm vụ song song
- Vận dụng được kỹ thuật chuẩn độ chính xác và tính sai số chuẩn độ
- Trình bày được số liệu thô và kết quả với số chữ số có nghĩa phù hợp

## Vòng thực hành chiếm 40% tổng điểm

Điểm thực hành IChO không chỉ chấm **kết quả** mà chấm cả **quy trình** và **cách ghi số liệu**. Nhiều thí sinh có kết quả chính xác nhưng mất điểm vì không ghi số liệu thô hoặc sai chữ số có nghĩa.

## Kế hoạch 5 phút đầu

1. Đọc **toàn bộ** đề, không chạm dụng cụ.
2. Đánh dấu các bước có **thời gian chờ** (kết tủa già hoá, làm khô, đun hồi lưu). Khởi động chúng **trước tiên**, làm việc khác trong lúc chờ.
3. Ước lượng thể tích chuẩn độ dự kiến để chọn nồng độ và cỡ buret.
4. Ghi ngay bảng số liệu trống lên phiếu trả lời.

## Kỹ thuật chuẩn độ đúng chuẩn

- **Lần 1 thô**: chuẩn nhanh để biết khoảng thể tích.
- **Lần 2, 3 chính xác**: nhỏ từng giọt khi còn cách $1$ mL, cuối cùng nhỏ nửa giọt và tráng thành bình.
- Lấy trung bình các lần **đồng nhất trong $0{,}05$ mL**; loại giá trị lệch xa và ghi rõ lí do loại.
- Đọc buret ở **đáy mặt khum**, mắt ngang mức chất lỏng, đọc tới $0{,}01$-$0{,}02$ mL.

## Nguồn sai số hệ thống hay bị bỏ sót

1. Không tráng buret bằng dung dịch chuẩn (pha loãng dung dịch chuẩn bởi nước còn sót).
2. Bọt khí ở đầu buret — xả trước khi đọc mức 0.
3. Chỉ thị chọn sai khoảng pH: khoảng đổi màu phải nằm trong bước nhảy pH của đường chuẩn độ. Với acid yếu chuẩn bằng base mạnh, điểm tương đương ở pH $>7$ nên phải dùng phenolphthalein, không dùng methyl da cam.
4. Nhiệt độ dung dịch khác nhiệt độ hiệu chuẩn dụng cụ.

## Ghi chép và trình bày

- Ghi **số liệu thô** (thể tích đầu, thể tích cuối) chứ không chỉ hiệu số.
- Số chữ số có nghĩa của kết quả không vượt quá số chữ số của dữ liệu kém chính xác nhất.
- Nếu làm hỏng một phép đo, **gạch một đường** và ghi lại, không tẩy xoá — giám khảo cần thấy quá trình.

## Khi hết thời gian

Ưu tiên: hoàn thành **một** nhiệm vụ trọn vẹn hơn là làm dở ba nhiệm vụ. Nếu chưa kịp tính toán, hãy ghi đủ số liệu thô — nhiều phần điểm nằm ở đó.

**Lỗi thường gặp:**
- Lấy trung bình cả giá trị lệch xa mà không loại — sai vì một lỗi thao tác kéo trung bình lệch hệ thống; phép trung bình chỉ có nghĩa với các phép đo lặp lại trong dung sai của dụng cụ.
- Dùng methyl da cam khi chuẩn độ acid yếu bằng base mạnh — sai vì điểm tương đương nằm ở pH kiềm; chỉ thị đổi màu ở vùng acid sẽ báo điểm cuối trước điểm tương đương rất xa.
- Ghi kết quả với nhiều chữ số hơn dữ liệu gốc — sai vì độ chính xác không thể tăng lên qua phép tính; số chữ số có nghĩa bị giới hạn bởi phép đo kém chính xác nhất.

<sub>`lesson.chemistry.icho.chien-thuat-vong-thuc-hanh`</sub>

---

## Unit 8: Acids and Bases

### 1. Định nghĩa Brønsted - Lowry, Lewis và cặp acid - base liên hợp
*Brønsted-Lowry and Lewis definitions, conjugate acid-base pairs* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Xác định được cặp acid - base liên hợp trong một phương trình chuyển proton
- Phân biệt được ba định nghĩa Arrhenius, Brønsted - Lowry và Lewis theo phạm vi áp dụng
- Chứng minh được hệ thức Ka·Kb = Kw cho một cặp liên hợp

## Ba định nghĩa mở rộng dần

**Arrhenius** (hẹp nhất): acid tạo $\mathrm{H^+}$, base tạo $\mathrm{OH^-}$ trong nước. Không giải thích được vì sao $\mathrm{NH_3}$ có tính base dù không chứa nhóm OH.

**Brønsted - Lowry**: acid **cho** proton, base **nhận** proton. Không cần dung môi là nước. Giải thích được $\mathrm{NH_3 + HCl \to NH_4Cl}$ ở thể khí.

**Lewis** (rộng nhất): acid **nhận cặp electron**, base **cho cặp electron**. Bao trùm cả những phản ứng không có proton nào tham gia: $\mathrm{BF_3 + NH_3 \to F_3B{-}NH_3}$, hoặc $\mathrm{Ag^+ + 2NH_3 \to [Ag(NH_3)_2]^+}$.

Mọi base Brønsted đều là base Lewis (cặp electron chính là thứ đón proton), nhưng chiều ngược lại không đúng.

## Cặp liên hợp

$$\mathrm{CH_3COOH + H_2O \rightleftharpoons CH_3COO^- + H_3O^+}$$

Cặp 1: $\mathrm{CH_3COOH}$ / $\mathrm{CH_3COO^-}$. Cặp 2: $\mathrm{H_2O}$ / $\mathrm{H_3O^+}$. Nhận diện bằng cách tìm hai tiểu phân **chỉ khác một H⁺**, một ở mỗi vế.

## Chất lưỡng tính

Nước vừa cho vừa nhận proton tuỳ đối tác. $\mathrm{HCO_3^-}$, $\mathrm{HSO_4^-}$, $\mathrm{H_2PO_4^-}$ và các amino acid cũng vậy. Với ion lưỡng tính, tính acid hay base trội hơn được quyết định bằng cách so $K_a$ của chính nó với $K_b$ của nó.

## Quan hệ Ka - Kb

Với cặp liên hợp $\mathrm{HA}$ / $\mathrm{A^-}$, nhân hai cân bằng lại thì $\mathrm{HA}$ và $\mathrm{A^-}$ triệt tiêu, chỉ còn tự ion hoá của nước:

$$K_a \cdot K_b = K_w = 1{,}0\times10^{-14}\ (25\ ^\circ\mathrm{C}) \qquad \mathrm{p}K_a + \mathrm{p}K_b = 14$$

Hệ thức này định lượng hoá câu nói "acid càng mạnh thì base liên hợp càng yếu". Nó cũng là công cụ tính nhanh: biết $K_a$ của $\mathrm{CH_3COOH}$ là $1{,}8\times10^{-5}$ thì ngay lập tức $K_b$ của acetate là $5{,}6\times10^{-10}$.

## Cảnh báo

$\mathrm{Cl^-}$ là base liên hợp của acid mạnh HCl, nên nó **rất yếu tới mức không có tính base đáng kể** trong nước. Đó là lí do NaCl cho dung dịch trung tính.

**Lỗi thường gặp:**
- Cho rằng base liên hợp của acid mạnh cũng là base mạnh — sai vì quan hệ là nghịch đảo qua Kw; HCl phân li hoàn toàn nên Cl⁻ hầu như không nhận lại proton và không có tính base đáng kể trong nước.
- Chọn cặp liên hợp gồm hai chất ở cùng một vế phương trình — sai vì cặp liên hợp phải nằm ở hai vế và khác nhau đúng một proton; ví dụ H₂O và H₃O⁺ mới là một cặp, còn H₂O và CH₃COO⁻ thì không.
- Coi mọi acid Lewis đều là acid Brønsted — sai vì BF₃ và Al³⁺ nhận cặp electron nhưng không hề có proton để cho; định nghĩa Lewis rộng hơn hẳn.
- Áp dụng pKa + pKb = 14 ở mọi nhiệt độ — sai vì Kw phụ thuộc nhiệt độ; ở 50 °C giá trị Kw lớn hơn nên tổng hai pK nhỏ hơn 14.

<sub>`lesson.chemistry.ap-acids-bases.bronsted-lowry-va-lewis`</sub>

---

### 2. pH, pOH và tích số ion của nước
*pH, pOH and the ionic product of water* · THPT (lớp 10-12) · ap, ib, a-level · 45 phút · trung-binh

**Mục tiêu:**
- Tính được pH và pOH từ nồng độ ion và ngược lại
- Giải thích được vì sao pH trung tính không phải luôn bằng 7
- Xác định được số chữ số có nghĩa đúng khi báo kết quả pH

## Nước không hoàn toàn trơ

$$\mathrm{2H_2O \rightleftharpoons H_3O^+ + OH^-} \qquad K_w = [\mathrm{H_3O^+}][\mathrm{OH^-}]$$

Ở 25 °C, $K_w = 1{,}0\times10^{-14}$, nghĩa là trong nước tinh khiết $[\mathrm{H_3O^+}] = [\mathrm{OH^-}] = 10^{-7}$ M. Chỉ khoảng hai phân tử trong một tỉ bị ion hoá — nhưng chính lượng nhỏ này định nghĩa thang pH.

## Thang logarit và ý nghĩa

$$\mathrm{pH} = -\log[\mathrm{H_3O^+}] \qquad \mathrm{pOH} = -\log[\mathrm{OH^-}] \qquad \mathrm{pH + pOH} = 14\ (25\ ^\circ\mathrm{C})$$

Mỗi đơn vị pH là **một bậc mười**. Dung dịch pH 3 có nồng độ $\mathrm{H_3O^+}$ gấp 1000 lần dung dịch pH 6, không phải gấp đôi.

## Nước trung tính ở 50 °C có pH 6,63

Tự ion hoá của nước là quá trình **thu nhiệt** ($\Delta H = +57$ kJ/mol, vì phải phá liên kết O-H). Theo Le Chatelier, tăng nhiệt độ đẩy cân bằng sang phải nên $K_w$ tăng: ở 50 °C, $K_w = 5{,}5\times10^{-14}$.

Khi đó $[\mathrm{H_3O^+}] = \sqrt{5{,}5\times10^{-14}} = 2{,}34\times10^{-7}$, cho pH = 6,63. **Nước vẫn trung tính** vì $[\mathrm{H_3O^+}] = [\mathrm{OH^-}]$; chỉ là con số 7 không còn là mốc trung tính nữa. Đây là câu hỏi phân loại điển hình của A-Level.

## Chữ số có nghĩa trong pH

Quy tắc: **chỉ phần thập phân của pH mới mang chữ số có nghĩa**, phần nguyên chỉ ghi bậc mười. Với $[\mathrm{H^+}] = 2{,}5\times10^{-3}$ (2 chữ số có nghĩa), pH = 2,60 — hai chữ số sau dấu phẩy, không phải "2,6" hay "2,602".

## Ranh giới áp dụng

Công thức $\mathrm{pH} = -\log C$ cho acid mạnh chỉ đúng khi $C \gtrsim 10^{-6}$ M. Với dung dịch loãng hơn, lượng $\mathrm{H_3O^+}$ do nước tự sinh ra trở nên đáng kể, và HCl $10^{-8}$ M **không** có pH 8 (không thể có acid mà pH kiềm) mà có pH khoảng 6,98.

**Lỗi thường gặp:**
- Kết luận dung dịch có pH nhỏ hơn 7 thì luôn có tính acid — sai vì mốc trung tính phụ thuộc nhiệt độ; ở 60 °C nước tinh khiết có pH 6,51 mà vẫn trung tính vì hai nồng độ ion bằng nhau.
- Dùng pH + pOH = 14 ở nhiệt độ khác 25 °C — sai vì tổng này bằng pKw, mà Kw tăng theo nhiệt độ nên pKw giảm; ở 60 °C tổng chỉ còn khoảng 13,02.
- Tính pH của HCl 10⁻⁸ M ra 8 — sai vì acid không thể cho dung dịch kiềm; ở nồng độ này phải kể cả H₃O⁺ do nước tự ion hoá sinh ra, kết quả đúng là khoảng 6,98.
- Đếm cả phần nguyên của pH là chữ số có nghĩa — sai vì phần nguyên chỉ mã hoá bậc mười của nồng độ, không mang thông tin về độ chính xác của phép đo; chỉ phần thập phân mới đếm.

<sub>`lesson.chemistry.ap-acids-bases.ph-poh-va-kw`</sub>

---

### 3. Acid - base mạnh yếu, Ka, Kb và phần trăm điện li
*Strong and weak acids and bases, Ka, Kb and percentage dissociation* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Phân biệt được độ mạnh và nồng độ của một acid, hai khái niệm hoàn toàn độc lập
- Tính được pH của dung dịch acid yếu và base yếu bằng phép xấp xỉ có kiểm tra
- Giải thích được vì sao pha loãng làm tăng phần trăm điện li nhưng vẫn làm pH tăng

## Mạnh khác đậm

Hai câu hoàn toàn khác nhau:

- **Mạnh/yếu** = mức độ phân li, đặc trưng bởi $K_a$. Không đổi khi pha loãng.
- **Đậm/loãng** = nồng độ, đặc trưng bởi $C$.

Một dung dịch $\mathrm{CH_3COOH}$ 5 M là acid **yếu nhưng đậm đặc**; HCl $10^{-4}$ M là acid **mạnh nhưng rất loãng** và có pH cao hơn.

## Tính pH acid mạnh

Phân li hoàn toàn nên $[\mathrm{H_3O^+}] = C$ (với acid đơn chức), cho $\mathrm{pH} = -\log C$.

## Tính pH acid yếu

Lập ICE cho $\mathrm{HA \rightleftharpoons H^+ + A^-}$:

$$K_a = \frac{x^2}{C - x} \;\xrightarrow{\ x \ll C\ }\; x \approx \sqrt{K_a C} \qquad \mathrm{pH} = \tfrac{1}{2}(\mathrm{p}K_a - \log C)$$

Phép xấp xỉ hợp lệ khi $C/K_a > 400$ (tương đương $x$ dưới 5% của $C$). Với acid không quá yếu hoặc dung dịch rất loãng, phải giải phương trình bậc hai.

## Nghịch lí pha loãng

Pha loãng làm **phần trăm điện li tăng** — hệ dịch về phía nhiều hạt hơn theo Le Chatelier. Nhưng pH vẫn **tăng** (dung dịch bớt acid). Không mâu thuẫn: tỉ lệ phân li tăng nhưng tổng lượng acid trong một lít giảm nhanh hơn, nên $[\mathrm{H_3O^+}]$ tuyệt đối vẫn giảm.

Quy tắc thực hành: pha loãng acid yếu 100 lần làm pH tăng khoảng **1 đơn vị** (vì $x \propto \sqrt{C}$), trong khi pha loãng acid mạnh 100 lần làm pH tăng đúng **2 đơn vị**. Đây là cách phân biệt acid mạnh với acid yếu bằng thực nghiệm.

## Cách nhận biết acid mạnh hay yếu trong phòng thí nghiệm

So cùng nồng độ: acid yếu có pH cao hơn, độ dẫn điện thấp hơn, phản ứng với Mg chậm hơn — nhưng **thể tích khí H₂ cuối cùng bằng nhau**, vì tổng số mol acid như nhau. Ý cuối là điểm phân biệt then chốt giữa "độ mạnh" (ảnh hưởng tốc độ) và "nồng độ" (ảnh hưởng lượng sản phẩm).

**Lỗi thường gặp:**
- Dùng công thức pH = −logC cho acid yếu — sai vì acid yếu chỉ phân li một phần nên [H₃O⁺] nhỏ hơn nhiều so với C; áp dụng nhầm sẽ cho pH thấp hơn thực tế cả đơn vị.
- Đồng nhất 'acid mạnh' với 'acid đậm đặc' — sai vì độ mạnh đo bằng Ka và không đổi khi pha loãng, còn nồng độ là lượng chất trong một thể tích; CH₃COOH đặc vẫn là acid yếu.
- Kết luận pha loãng làm dung dịch acid mạnh hơn vì phần trăm điện li tăng — sai vì tính acid của dung dịch được đánh giá bằng [H₃O⁺] tuyệt đối, mà đại lượng này giảm khi pha loãng dù tỉ lệ phân li tăng.
- Cho rằng acid yếu phản ứng với kim loại sinh ít khí hơn acid mạnh cùng nồng độ và thể tích — sai vì tổng số mol proton có thể cho là như nhau; acid yếu chỉ phản ứng chậm hơn chứ thể tích khí cuối cùng bằng nhau.

<sub>`lesson.chemistry.ap-acids-bases.acid-base-manh-yeu`</sub>

---

### 4. Thuỷ phân muối, dung dịch đệm và phương trình Henderson - Hasselbalch
*Salt hydrolysis, buffer solutions and the Henderson-Hasselbalch equation* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Dự đoán được tính acid, base hay trung tính của dung dịch muối từ nguồn gốc ion
- Giải thích được cơ chế đệm bằng cặp acid - base liên hợp có mặt đồng thời
- Tính được pH của đệm trước và sau khi thêm một lượng nhỏ acid hoặc base mạnh

## Bốn loại muối, bốn kết quả

Xét nguồn gốc từng ion:

| Cation từ | Anion từ | pH dung dịch |
|---|---|---|
| base mạnh | acid mạnh | trung tính (NaCl) |
| base mạnh | acid yếu | **base** (CH₃COONa) |
| base yếu | acid mạnh | **acid** (NH₄Cl) |
| base yếu | acid yếu | so $K_a$ với $K_b$ (CH₃COONH₄) |

Cơ chế: $\mathrm{CH_3COO^- + H_2O \rightleftharpoons CH_3COOH + OH^-}$ sinh $\mathrm{OH^-}$; còn $\mathrm{NH_4^+ + H_2O \rightleftharpoons NH_3 + H_3O^+}$ sinh $\mathrm{H_3O^+}$.

Ion từ acid mạnh hoặc base mạnh **không thuỷ phân**, vì base liên hợp của acid mạnh quá yếu.

## Đệm hoạt động thế nào

Đệm chứa cả $\mathrm{HA}$ (kho hấp thụ $\mathrm{OH^-}$) lẫn $\mathrm{A^-}$ (kho hấp thụ $\mathrm{H_3O^+}$):

$$\mathrm{HA + OH^- \to A^- + H_2O} \qquad \mathrm{A^- + H_3O^+ \to HA + H_2O}$$

Lượng acid hay base thêm vào bị chuyển hoá thành cấu tử kia thay vì tồn tại tự do, nên pH gần như không đổi.

## Henderson - Hasselbalch

$$\mathrm{pH} = \mathrm{p}K_a + \log\frac{[\mathrm{A^-}]}{[\mathrm{HA}]}$$

Ba hệ quả:

- Khi $[\mathrm{A^-}] = [\mathrm{HA}]$ thì $\mathrm{pH} = \mathrm{p}K_a$ — điểm đệm hiệu quả nhất.
- Khoảng đệm dùng được là $\mathrm{p}K_a \pm 1$, tương ứng tỉ lệ từ 1:10 tới 10:1.
- Vì là **tỉ số** nên pha loãng đệm gần như không đổi pH, chỉ giảm dung lượng.

Mẹo tính nhanh: có thể thay nồng độ bằng **số mol** trong công thức, vì hai chất ở cùng thể tích nên thể tích triệt tiêu.

## Ứng dụng

Máu người được đệm bằng hệ $\mathrm{H_2CO_3/HCO_3^-}$ giữ pH 7,35-7,45. Lệch ra ngoài khoảng này chỉ vài phần mười đơn vị đã gây nhiễm acid hoặc nhiễm kiềm nguy hiểm — minh hoạ rằng dung lượng đệm là hữu hạn.

**Lỗi thường gặp:**
- Thay trực tiếp nồng độ ban đầu vào Henderson - Hasselbalch sau khi thêm acid mà bỏ qua bước tỉ lượng — sai vì acid mạnh thêm vào đã chuyển một phần A⁻ thành HA, phải cập nhật số mol hai cấu tử trước khi tính lại.
- Cho rằng pha loãng đệm làm pH thay đổi nhiều — sai vì công thức chỉ chứa tỉ số [A⁻]/[HA], mà pha loãng làm cả hai nồng độ giảm cùng tỉ lệ nên tỉ số không đổi; chỉ dung lượng đệm giảm.
- Cho rằng dung dịch NaCl có tính base vì có Na⁺ của base mạnh — sai vì cả Na⁺ lẫn Cl⁻ đều là ion liên hợp của base mạnh và acid mạnh nên không thuỷ phân, dung dịch trung tính.
- Trộn acid mạnh với base mạnh rồi gọi đó là đệm — sai vì đệm cần một acid yếu và base liên hợp của nó cùng tồn tại; acid mạnh và base mạnh trung hoà hết nhau, không còn cặp liên hợp nào để hấp thụ tác động.

<sub>`lesson.chemistry.ap-acids-bases.thuy-phan-muoi-va-dem`</sub>

---

### 5. Đường cong chuẩn độ, acid đa nấc và chỉ thị
*Titration curves, polyprotic acids and indicators* · THPT (lớp 10-12) · ap, ib, a-level · 55 phút · chuyen-sau

**Mục tiêu:**
- Phân tích được bốn mốc đặc trưng trên đường cong chuẩn độ acid yếu bằng base mạnh
- Chọn được chỉ thị phù hợp dựa trên pH tại điểm tương đương
- Giải thích được vì sao acid đa nấc cho nhiều bước nhảy và điều kiện tách được các bước

## Bốn mốc trên đường cong acid yếu - base mạnh

1. **Trước khi thêm base**: dung dịch acid yếu thuần, $\mathrm{pH} = \tfrac{1}{2}(\mathrm{p}K_a - \log C)$.
2. **Vùng đệm** (0 < V < V_tđ): tồn tại cả HA và A⁻, dùng Henderson - Hasselbalch. Tại **nửa tương đương**, $\mathrm{pH} = \mathrm{p}K_a$ — đây là cách đọc $K_a$ trực tiếp từ đồ thị.
3. **Điểm tương đương**: chỉ còn A⁻, một base yếu, nên $\mathrm{pH > 7}$. Tính bằng $K_b = K_w/K_a$.
4. **Sau điểm tương đương**: base mạnh dư quyết định pH, tính trực tiếp từ nồng độ $\mathrm{OH^-}$ dư.

## Bốn kiểu đường cong

| Acid | Base | pH tại điểm tương đương | Chỉ thị |
|---|---|---|---|
| mạnh | mạnh | 7 | phenolphtalein hoặc metyl da cam |
| yếu | mạnh | > 7 | **phenolphtalein** (8,3-10,0) |
| mạnh | yếu | < 7 | **metyl da cam** (3,1-4,4) |
| yếu | yếu | ~7 | không có bước nhảy rõ ⇒ dùng pH kế |

## Nguyên tắc chọn chỉ thị

Khoảng đổi màu của chỉ thị phải **nằm trọn trong bước nhảy pH**. Không cần trùng với pH điểm tương đương — chỉ cần nằm trong đoạn dốc đứng, vì ở đó một giọt duy nhất đủ đưa pH vượt qua cả khoảng đổi màu.

Dùng metyl da cam cho chuẩn độ acid yếu bằng base mạnh là **sai**: nó đổi màu ở pH 3-4, tức khi mới thêm được một phần nhỏ base, gây sai số lớn.

## Acid đa nấc

$\mathrm{H_3PO_4}$ có $\mathrm{p}K_{a1} = 2{,}1$, $\mathrm{p}K_{a2} = 7{,}2$, $\mathrm{p}K_{a3} = 12{,}3$. Mỗi nấc cho một bước nhảy riêng, cách nhau đúng bằng lượng base tương đương như nhau.

Điều kiện **tách được** hai bước nhảy: $K_{a1}/K_{a2} \gtrsim 10^4$, tức $\Delta\mathrm{p}K_a \ge 4$. Với $\mathrm{H_2CO_3}$ ($\mathrm{p}K_{a1} = 6{,}4$; $\mathrm{p}K_{a2} = 10{,}3$) chênh 3,9 nên hai bước hơi chồng lấn; với $\mathrm{H_2SO_4}$ nấc một là acid mạnh nên chỉ thấy một bước nhảy.

Giữa hai điểm tương đương liên tiếp là một **vùng đệm**, và pH tại nửa đường của vùng đó bằng $\mathrm{p}K_a$ của nấc tương ứng.

**Lỗi thường gặp:**
- Cho rằng điểm tương đương của mọi phép chuẩn độ đều ở pH 7 — sai vì chỉ đúng với acid mạnh và base mạnh; với acid yếu, muối tạo thành chứa base liên hợp thuỷ phân nên pH lớn hơn 7.
- Quên pha loãng khi tính nồng độ tại điểm tương đương — sai vì thể tích dung dịch đã tăng do thêm chất chuẩn; dùng thể tích ban đầu làm nồng độ bị thổi phồng và pH tính ra sai.
- Chọn chỉ thị chỉ dựa trên tên phản ứng mà không xét pH tại điểm tương đương — sai vì tiêu chuẩn duy nhất là khoảng đổi màu phải nằm trong bước nhảy pH của đường cong cụ thể đó.
- Kì vọng H₂SO₄ cho hai bước nhảy rõ rệt như H₃PO₄ — sai vì nấc phân li thứ nhất của H₂SO₄ là acid mạnh, chênh lệch pKa giữa hai nấc không đủ lớn nên hai bước nhảy chồng lên nhau thành một.

<sub>`lesson.chemistry.ap-acids-bases.duong-cong-chuan-do-va-chi-thi`</sub>

---

## Unit 9: Thermodynamics II and Electrochemistry

### 1. Entropy và nguyên lí thứ hai nhiệt động lực học
*Entropy and the second law of thermodynamics* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Dự đoán được dấu của biến thiên entropy từ thay đổi trạng thái và số mol khí
- Tính được entropy chuẩn của phản ứng và entropy của môi trường
- Giải thích được vì sao tiêu chuẩn tự diễn biến thật sự là entropy tổng của vũ trụ

## Vì sao enthalpy không đủ

Nhiều quá trình thu nhiệt vẫn tự xảy ra: nước đá tan ở 25 °C, $\mathrm{NH_4NO_3}$ tan làm dung dịch lạnh đi, và $\mathrm{N_2O_4}$ phân li ở nhiệt độ cao. Vậy phải có một động lực thứ hai ngoài việc "hạ năng lượng".

## Entropy là gì thật sự

Entropy đếm **số cách phân bố năng lượng và vị trí**. Trạng thái nào có nhiều cách sắp xếp hơn thì xác suất quan sát được lớn hơn. Đó là lí do khí tự khuếch tán đầy bình mà không bao giờ tự co lại một góc — không phải vì bị cấm về năng lượng, mà vì xác suất quá nhỏ.

## Dự đoán dấu của ΔS

Xếp theo mức độ ảnh hưởng giảm dần:

1. **Số mol khí thay đổi** — yếu tố áp đảo. $\Delta n_{\text{khí}} > 0 \Rightarrow \Delta S > 0$.
2. **Chuyển pha**: rắn → lỏng → khí đều làm $S$ tăng, bước hoá hơi tăng mạnh nhất.
3. **Hoà tan chất rắn** thường làm tăng (mạng trật tự tan thành ion phân tán), nhưng hoà tan khí vào lỏng làm **giảm**.
4. **Số phân tử tăng** hoặc phân tử phức tạp hơn ⇒ $S$ tăng.
5. **Nhiệt độ tăng** ⇒ $S$ tăng.

## Ba công thức

$$\Delta S^\circ_{\text{hệ}} = \sum \nu S^\circ(\text{sp}) - \sum \nu S^\circ(\text{pư})$$
$$\Delta S_{\text{môi trường}} = -\frac{\Delta H_{\text{hệ}}}{T}$$
$$\Delta S_{\text{tổng}} = \Delta S_{\text{hệ}} + \Delta S_{\text{môi trường}} > 0 \;\text{ nếu tự diễn biến}$$

Khác biệt quan trọng so với enthalpy: **$S^\circ$ của đơn chất KHÔNG bằng 0**. Nguyên lí thứ ba chỉ nói entropy của tinh thể hoàn hảo ở 0 K bằng 0, nên ở 298 K mọi chất đều có $S^\circ$ dương.

## Vì sao phản ứng toả nhiệt thường tự diễn biến

Vì $\Delta H < 0$ làm $\Delta S_{\text{môi trường}} = -\Delta H/T > 0$: nhiệt toả ra làm tăng chuyển động hỗn loạn của môi trường. Ngay cả khi $\Delta S_{\text{hệ}}$ âm, phần đóng góp của môi trường vẫn có thể thắng — đó chính là cách nhiệt động học giải thích quy tắc kinh nghiệm cũ.

## Cảnh báo

Entropy tăng là điều kiện của **vũ trụ**, không phải của riêng hệ. Sự sống tạo ra cấu trúc trật tự cao (ΔS hệ âm) nhưng luôn kèm theo việc thải nhiệt làm entropy môi trường tăng nhiều hơn.

**Lỗi thường gặp:**
- Gán S° = 0 cho đơn chất như với ΔHf° — sai vì nguyên lí thứ ba chỉ cho entropy bằng 0 với tinh thể hoàn hảo ở 0 K; ở 298 K mọi chất kể cả O₂ đều có S° dương và phải tra bảng.
- Cộng ΔS(hệ) theo J/K với ΔS(môi trường) tính từ ΔH theo kJ — sai về thứ nguyên vì lệch 1000 lần, dẫn tới kết luận ngược hoàn toàn về tính tự diễn biến.
- Kết luận phản ứng không tự diễn biến vì ΔS(hệ) âm — sai vì tiêu chuẩn là entropy tổng của vũ trụ; phản ứng toả nhiệt làm entropy môi trường tăng và phần này có thể lớn hơn phần giảm của hệ.
- Cho rằng entropy chỉ là 'độ hỗn loạn' rồi dự đoán ΔS của mọi phản ứng có nhiều phân tử hơn đều dương — sai vì yếu tố quyết định là số mol khí; phản ứng sinh nhiều phân tử trong dung dịch có thể vẫn cho ΔS âm nếu ion bị hidrat hoá làm trật tự hoá các phân tử nước.

<sub>`lesson.chemistry.ap-thermo-electrochem.entropy-va-nguyen-li-hai`</sub>

---

### 2. Năng lượng Gibbs và tính tự diễn biến
*Gibbs free energy and spontaneity* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Tính được biến thiên năng lượng Gibbs chuẩn từ ΔH và ΔS
- Phân tích được bốn trường hợp dấu của ΔH và ΔS để xác định miền nhiệt độ tự diễn biến
- Phân biệt được tính tự diễn biến về nhiệt động với khả năng xảy ra thực tế về động học

## Gộp hai tiêu chuẩn thành một

Tiêu chuẩn thật là $\Delta S_{\text{tổng}} > 0$. Nhân hai vế của $\Delta S_{\text{tổng}} = \Delta S_{\text{hệ}} - \Delta H/T$ với $-T$ (số âm, đảo chiều bất đẳng thức):

$$-T\Delta S_{\text{tổng}} = \Delta H - T\Delta S \equiv \Delta G$$

Vậy $\Delta S_{\text{tổng}} > 0$ **tương đương** $\Delta G < 0$. Ưu điểm của $\Delta G$: chỉ cần dữ liệu về **hệ**, không phải tính riêng môi trường.

## Bốn trường hợp

| $\Delta H$ | $\Delta S$ | Kết quả |
|---|---|---|
| $<0$ | $>0$ | tự diễn biến ở **mọi** nhiệt độ |
| $>0$ | $<0$ | **không bao giờ** tự diễn biến |
| $<0$ | $<0$ | tự diễn biến ở nhiệt độ **thấp** |
| $>0$ | $>0$ | tự diễn biến ở nhiệt độ **cao** |

Hai trường hợp cuối có nhiệt độ chuyển tiếp $T = \Delta H/\Delta S$, tại đó $\Delta G = 0$ và hệ ở **cân bằng**. Đó chính là nhiệt độ nóng chảy hay nhiệt độ sôi khi áp cho chuyển pha.

## Đồ thị ΔG theo T

Viết lại $\Delta G = -\Delta S\cdot T + \Delta H$: đây là **đường thẳng** với độ dốc $-\Delta S$ và tung độ gốc $\Delta H$. Đọc đồ thị: giao điểm với trục hoành là nhiệt độ chuyển tiếp; độ dốc âm nghĩa là $\Delta S$ dương.

## Ba cảnh báo

1. **Đơn vị**: $\Delta H$ thường theo kJ/mol còn $\Delta S$ theo J·K⁻¹·mol⁻¹. Phải đổi trước khi trừ.
2. **Tự diễn biến ≠ nhanh**. Kim cương chuyển thành graphite có $\Delta G = -2{,}9$ kJ/mol nhưng cần rào hoạt hoá khổng lồ nên không quan sát được. Nhiệt động cho biết "có được phép", động học cho biết "có kịp không".
3. $\Delta G^\circ$ chỉ nói về **điều kiện chuẩn**. Ở điều kiện khác dùng $\Delta G = \Delta G^\circ + RT\ln Q$.

## Ghép cặp phản ứng

Phản ứng không tự diễn biến vẫn thực hiện được nếu ghép với một phản ứng có $\Delta G$ âm lớn hơn về độ lớn, miễn hai quá trình chia sẻ một chất trung gian chung. Đây là nguyên lí của luyện kim ($\mathrm{Fe_2O_3}$ khử bằng CO) và của toàn bộ trao đổi chất trong tế bào (ghép với thuỷ phân ATP).

**Lỗi thường gặp:**
- Trừ trực tiếp TΔS theo J/K khỏi ΔH theo kJ mà không đổi đơn vị — sai vì hai số lệch nhau 1000 lần, làm số hạng entropy bị phóng đại và cho kết luận hoàn toàn sai về nhiệt độ ngưỡng.
- Kết luận phản ứng có ΔG âm thì chắc chắn quan sát được — sai vì nhiệt động chỉ nói về chiều có lợi về năng lượng, không nói gì về rào hoạt hoá; kim cương và hỗn hợp H₂ với O₂ đều có ΔG âm mà vẫn bền ở nhiệt độ phòng.
- Dùng ΔG° để dự đoán chiều phản ứng ở điều kiện không chuẩn — sai vì ΔG° chỉ ứng với mọi chất ở trạng thái chuẩn; ở điều kiện thực phải dùng ΔG = ΔG° + RT·lnQ, và dấu của hai đại lượng này có thể ngược nhau.
- Cho rằng phản ứng có ΔH dương thì không bao giờ tự diễn biến — sai vì nếu ΔS đủ dương thì ở nhiệt độ cao số hạng −TΔS thắng, đúng như trường hợp nung vôi.

<sub>`lesson.chemistry.ap-thermo-electrochem.gibbs-va-tu-dien-bien`</sub>

---

### 3. Quan hệ giữa năng lượng Gibbs và hằng số cân bằng
*The relationship between Gibbs energy and the equilibrium constant* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · chuyen-sau

**Mục tiêu:**
- Vận dụng được hệ thức ΔG° = −RT·lnK để chuyển đổi giữa nhiệt động và cân bằng
- Giải thích được vì sao ΔG bằng 0 tại cân bằng trong khi ΔG° thường khác 0
- Dự đoán được sự thay đổi của K theo nhiệt độ từ dấu của ΔH

## Cầu nối hai chương

Unit 7 nói về $K$, Unit 9 nói về $\Delta G$. Chúng là hai cách diễn đạt cùng một sự thật:

$$\Delta G^\circ = -RT\ln K \qquad\Longleftrightarrow\qquad K = e^{-\Delta G^\circ/RT}$$

| $\Delta G^\circ$ | $K$ | Cân bằng lệch về |
|---|---|---|
| âm lớn | $\gg 1$ | sản phẩm |
| $\approx 0$ | $\approx 1$ | cân bằng giữa |
| dương lớn | $\ll 1$ | chất phản ứng |

Vì là hàm mũ, $\Delta G^\circ$ chỉ cần khoảng $-30$ kJ/mol đã cho $K \approx 2\times10^5$.

## Phân biệt ΔG và ΔG° — điểm hay nhầm nhất

$$\Delta G = \Delta G^\circ + RT\ln Q$$

- $\Delta G^\circ$ là **hằng số** ở một nhiệt độ, ứng với mọi chất ở trạng thái chuẩn.
- $\Delta G$ **thay đổi liên tục** khi phản ứng tiến triển vì $Q$ thay đổi.

Tại cân bằng $Q = K$ và $\Delta G = 0$ — nhưng $\Delta G^\circ$ vẫn khác 0. Nói "$\Delta G^\circ = 0$ tại cân bằng" là sai; điều đúng là $\Delta G = 0$.

Diễn giải hình học: $G$ của hệ là một đường cong theo mức độ phản ứng, có **cực tiểu** tại vị trí cân bằng. $\Delta G$ là độ dốc của đường cong đó, nên bằng 0 tại đáy.

## K thay đổi theo nhiệt độ

Thay $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$ vào:

$$\ln K = -\frac{\Delta H^\circ}{R}\cdot\frac{1}{T} + \frac{\Delta S^\circ}{R}$$

Đây là dạng van't Hoff. Vẽ $\ln K$ theo $1/T$ cho đường thẳng độ dốc $-\Delta H^\circ/R$. Với phản ứng toả nhiệt ($\Delta H^\circ < 0$), độ dốc dương nên $K$ **giảm** khi $T$ tăng — đúng dự đoán Le Chatelier, nhưng bây giờ là định lượng.

## Ứng dụng

Biết $\Delta G_f^\circ$ của các chất, ta tính được $K$ của bất kì phản ứng nào mà không cần làm thí nghiệm cân bằng. Ngược lại, đo $K$ ở vài nhiệt độ cho phép suy ra $\Delta H^\circ$ và $\Delta S^\circ$ mà không cần nhiệt lượng kế.

**Lỗi thường gặp:**
- Nói ΔG° = 0 tại cân bằng — sai vì ΔG° là hằng số ứng với trạng thái chuẩn của mọi chất; đại lượng bằng 0 tại cân bằng là ΔG, còn ΔG° liên hệ với K qua −RT·lnK và chỉ bằng 0 khi K đúng bằng 1.
- Dùng dấu của ΔG° để dự đoán chiều phản ứng ở nồng độ tuỳ ý — sai vì phải kể tới số hạng RT·lnQ; một phản ứng có ΔG° dương vẫn đi chiều thuận nếu Q nhỏ hơn K đáng kể.
- Quên đổi ΔG° từ kJ sang J trước khi chia cho RT với R = 8,314 J·K⁻¹·mol⁻¹ — sai về thứ nguyên, làm lnK sai 1000 lần và K trở nên vô nghĩa.
- Cho rằng K thay đổi khi thêm chất hoặc đổi áp suất — sai vì từ ΔG° = −RT·lnK thấy rõ K chỉ phụ thuộc ΔG°, mà ΔG° chỉ phụ thuộc bản chất phản ứng và nhiệt độ.

<sub>`lesson.chemistry.ap-thermo-electrochem.gibbs-va-hang-so-can-bang`</sub>

---

### 4. Pin điện hoá, thế điện cực chuẩn và phương trình Nernst
*Galvanic cells, standard electrode potentials and the Nernst equation* · THPT (lớp 10-12) · ap, ib, a-level · 55 phút · chuyen-sau

**Mục tiêu:**
- Xây dựng được sơ đồ pin theo quy ước IUPAC và tính được sức điện động chuẩn
- Liên hệ được sức điện động với năng lượng Gibbs và hằng số cân bằng
- Vận dụng được phương trình Nernst để tính thế ở điều kiện không chuẩn

## Ý tưởng: tách hai nửa phản ứng ra xa

Nhúng Zn vào dung dịch $\mathrm{Cu^{2+}}$ thì electron chuyển trực tiếp và toả nhiệt vô ích. Nếu tách hai nửa ra hai cốc, nối bằng dây dẫn và cầu muối, electron buộc phải đi qua dây — ta thu được **công điện** thay vì nhiệt.

## Quy ước và cách nhớ

- **Anode**: nơi **oxi hoá** (mất electron). Trong pin Galvani anode mang dấu **âm**.
- **Cathode**: nơi **khử**. Trong pin Galvani cathode mang dấu **dương**.

Cách nhớ: "AN OX, RED CAT" — anode oxidation, reduction cathode. Lưu ý dấu điện cực **đảo ngược** trong bình điện phân, dù vai trò oxi hoá/khử vẫn giữ nguyên.

Sơ đồ IUPAC viết anode bên trái, cathode bên phải:

$$\mathrm{Zn(s)\,|\,Zn^{2+}(aq)\,\|\,Cu^{2+}(aq)\,|\,Cu(s)}$$

$$E^\circ_{\text{pin}} = E^\circ_{\text{cathode}} - E^\circ_{\text{anode}} = +0{,}34 - (-0{,}76) = +1{,}10\ \mathrm{V}$$

**Không nhân $E^\circ$ với hệ số** khi cân bằng electron — thế là đại lượng cường độ (intensive), không phụ thuộc lượng chất, khác hẳn enthalpy.

## Cầu nối với nhiệt động

$$\Delta G^\circ = -nFE^\circ, \qquad F = 96\,485\ \mathrm{C\,mol^{-1}}$$

$E^\circ > 0 \Leftrightarrow \Delta G^\circ < 0 \Leftrightarrow K > 1$. Ba cách nói về cùng một điều. Ghép với $\Delta G^\circ = -RT\ln K$ ta được $\ln K = nFE^\circ/RT$.

## Phương trình Nernst

$$E = E^\circ - \frac{RT}{nF}\ln Q \;\xrightarrow{\ 298\ \mathrm{K}\ }\; E = E^\circ - \frac{0{,}0592}{n}\log Q$$

Ý nghĩa: khi pin phóng điện, sản phẩm tích tụ nên $Q$ tăng, $E$ giảm dần. Pin "hết" đúng lúc $Q = K$ và $E = 0$ — pin đã đạt cân bằng.

**Pin nồng độ** là trường hợp đặc biệt: hai nửa cùng cặp oxi hoá khử nên $E^\circ = 0$, toàn bộ thế sinh ra từ chênh lệch nồng độ. Chiều tự diễn biến luôn là chiều làm hai nồng độ tiến về bằng nhau.

## Lưu ý về phạm vi chương trình

Phương trình Nernst ở dạng **định lượng** thuộc Cambridge 9701 mục 24.2 (syllabus cho sẵn dạng $E = E^\circ + \frac{0{,}059}{z}\log\frac{[\text{dạng oxi hoá}]}{[\text{dạng khử}]}$, tương đương dạng viết theo $Q$ ở trên). AP Chemistry chỉ yêu cầu lập luận **định tính**: biết $Q$ tăng thì $E$ giảm, và $E = 0$ khi $Q = K$. IB dừng ở thế điện cực chuẩn và hệ thức $\Delta G^\circ = -nFE^\circ$. Vì vậy học sinh AP và IB nên nắm phần lập luận, còn phần thay số vào công thức là dành cho A-Level.

**Lỗi thường gặp:**
- Nhân thế điện cực với hệ số khi cân bằng số electron — sai vì E° là đại lượng cường độ, không phụ thuộc lượng chất; chỉ ΔG° mới là đại lượng khuếch độ và mới nhân với n.
- Giữ nguyên quy ước dấu điện cực khi chuyển từ pin Galvani sang bình điện phân — sai vì trong bình điện phân nguồn ngoài áp đặt dấu, anode trở thành cực dương dù vẫn là nơi xảy ra oxi hoá.
- Viết Q trong phương trình Nernst theo chiều ngược với phương trình phản ứng đã dùng để tính E° — sai vì đảo Q làm đổi dấu số hạng hiệu chỉnh, cho kết quả lệch tới hai lần giá trị hiệu chỉnh.
- Cho rằng pin nồng độ có E° khác 0 — sai vì hai nửa pin dùng cùng một cặp oxi hoá khử nên thế chuẩn triệt tiêu; toàn bộ sức điện động sinh ra từ số hạng lnQ do chênh lệch nồng độ.

<sub>`lesson.chemistry.ap-thermo-electrochem.pin-dien-hoa-va-nernst`</sub>

---

### 5. Điện phân và định luật Faraday
*Electrolysis and Faraday's laws* · THPT (lớp 10-12) · ap, ib, a-level · 50 phút · nang-cao

**Mục tiêu:**
- Dự đoán được sản phẩm ở catot và anot khi điện phân dung dịch
- Tính được khối lượng chất thoát ra bằng định luật Faraday
- Giải thích được vì sao điện phân dung dịch cho sản phẩm khác điện phân nóng chảy

## Điện phân là pin chạy ngược

Pin Galvani biến năng lượng hoá học thành điện năng ($\Delta G < 0$). Điện phân làm ngược lại: dùng điện năng ép phản ứng có $\Delta G > 0$ phải xảy ra. Vai trò điện cực không đổi (anode vẫn oxi hoá) nhưng **dấu điện cực đảo**: anode nối cực dương của nguồn.

## Thứ tự phóng điện trong dung dịch

Đây là điểm khác biệt lớn nhất so với điện phân nóng chảy: **nước tham gia cạnh tranh**.

**Tại catot** (khử), cạnh tranh giữa cation kim loại và nước:

- Cation từ $\mathrm{Cu^{2+}}$ trở về sau trong dãy điện hoá ⇒ **kim loại** thoát ra.
- Cation của kim loại mạnh ($\mathrm{Na^+, K^+, Ca^{2+}, Al^{3+}}$) ⇒ **nước bị khử**: $\mathrm{2H_2O + 2e^- \to H_2 + 2OH^-}$.

Đó là lí do không thể điều chế Na bằng điện phân dung dịch NaCl, mà phải điện phân NaCl **nóng chảy**.

**Tại anot** (oxi hoá):

- Halide ($\mathrm{Cl^-, Br^-, I^-}$) ⇒ halogen thoát ra.
- Anion chứa oxygen ($\mathrm{SO_4^{2-}, NO_3^-}$) rất bền ⇒ **nước bị oxi hoá**: $\mathrm{2H_2O \to O_2 + 4H^+ + 4e^-}$.
- Điện cực tan (Cu, Ag) ⇒ chính kim loại điện cực bị oxi hoá — nguyên lí tinh luyện đồng và mạ điện.

## Định luật Faraday

$$Q = It, \qquad n_e = \frac{Q}{F} = \frac{It}{96485}, \qquad m = \frac{M\,I\,t}{n\,F}$$

với $n$ là số electron trao đổi cho một đơn vị chất. Quy trình an toàn: (1) tính $Q = It$, (2) chia $F$ ra mol electron, (3) dùng nửa phản ứng để đổi sang mol chất, (4) nhân $M$.

Hệ quả: mắc nối tiếp nhiều bình thì cùng $Q$ đi qua, nên số mol **electron** bằng nhau — nhưng số mol kim loại khác nhau tuỳ điện tích ion.

## Vì sao lí thuyết và thực tế lệch nhau

Thế nhiệt động chỉ là ngưỡng tối thiểu. Thực tế phải cấp thêm **quá thế**, đặc biệt lớn với khí $\mathrm{O_2}$ trên nhiều vật liệu điện cực. Chính quá thế của oxygen là lí do điện phân dung dịch NaCl đậm đặc cho $\mathrm{Cl_2}$ chứ không cho $\mathrm{O_2}$ như dự đoán thuần nhiệt động.

**Lỗi thường gặp:**
- Cho rằng điện phân dung dịch NaCl thu được Na ở catot — sai vì Na⁺ có thế khử rất âm, nước dễ bị khử hơn nhiều nên sản phẩm thực tế là H₂ và NaOH; muốn có Na phải điện phân NaCl nóng chảy.
- Bỏ qua số electron n trong công thức Faraday — sai vì mỗi ion cần số electron khác nhau; dùng chung n = 1 cho Cu²⁺ sẽ cho khối lượng gấp đôi giá trị đúng.
- Cho rằng mắc nối tiếp hai bình thì khối lượng kim loại thoát ra ở hai bình bằng nhau — sai vì đại lượng bằng nhau là số mol electron, còn số mol kim loại còn phải chia cho điện tích ion tương ứng.
- Dự đoán anot luôn cho O₂ vì nước dễ bị oxi hoá nhất về nhiệt động — sai vì quá thế của oxygen trên nhiều điện cực rất lớn, nên với dung dịch chloride đậm đặc thì Cl₂ mới là sản phẩm thực tế.

<sub>`lesson.chemistry.ap-thermo-electrochem.dien-phan-va-faraday`</sub>

---

## Unit 1: Nhiệt động hoá học

### 1. Hệ nhiệt động, hàm trạng thái và các quá trình cơ bản
*Thermodynamic systems, state functions and basic processes* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Phân biệt được hệ cô lập, hệ kín và hệ mở theo khả năng trao đổi chất và năng lượng
- Giải thích được vì sao nội năng là hàm trạng thái còn nhiệt và công thì không
- Tính được công dãn nở trong quá trình thuận nghịch và bất thuận nghịch, rồi so sánh hai giá trị

## Trước khi tính, phải khoanh vùng

Câu hỏi "phản ứng này toả bao nhiêu nhiệt" chỉ có nghĩa khi ta đã nói rõ **hệ** là gì và ranh giới nằm ở đâu. Cùng một bình phản ứng, nếu coi hệ là dung dịch thì nước là môi trường; nếu coi hệ là cả bình thì lượng nhiệt đo được đổi dấu và đổi giá trị. Nhiệt động hoá học vì thế bắt đầu bằng ba loại hệ: **cô lập** (không trao đổi gì), **kín** (trao đổi năng lượng, không trao đổi chất), **mở** (trao đổi cả hai).

## Hàm trạng thái và đại lượng đường đi

Trạng thái của một hệ đồng thể được xác định bởi vài biến như $p$, $V$, $T$, $n$. Đại lượng nào tính được từ bộ biến đó là **hàm trạng thái**: $U$, $H$, $S$, $G$. Với chúng, vi phân là vi phân toàn phần và

$$\oint dU = 0$$

Ngược lại, nhiệt $q$ và công $w$ **không** là hàm trạng thái: hai đường khác nhau nối cùng một cặp trạng thái cho $q$, $w$ khác nhau, chỉ tổng $q+w$ là bất biến. Vì vậy phải viết $\delta q$, $\delta w$ chứ không viết $dq$, $dw$.

## Công dãn nở: thuận nghịch cho giá trị lớn nhất

Với dãn nở chống áp suất ngoài không đổi, $w=-p_{\text{ng}}\Delta V$. Với dãn nở đẳng nhiệt thuận nghịch của khí lí tưởng, ở mỗi thời điểm $p_{\text{ng}}=p_{\text{hệ}}=nRT/V$, nên

$$w_{\text{tn}}=-\int_{V_1}^{V_2} \frac{nRT}{V}\,dV=-nRT\ln\frac{V_2}{V_1}$$

Trị tuyệt đối của $w_{\text{tn}}$ luôn lớn nhất trong mọi cách dãn nở giữa hai trạng thái đó. Đây là mầm mống của nguyên lí II: quá trình bất thuận nghịch luôn "phí" một phần khả năng sinh công.

## Giới hạn áp dụng

Công thức $w_{\text{tn}}=-nRT\ln(V_2/V_1)$ chỉ đúng cho **khí lí tưởng, đẳng nhiệt, thuận nghịch**. Khí thực ở áp suất cao phải dùng phương trình trạng thái tương ứng; quá trình có ma sát hay dãn nở vào chân không thì không thuận nghịch, và với dãn nở vào chân không $p_{\text{ng}}=0$ nên $w=0$.

**Lỗi thường gặp:**
- Viết $\Delta q$ hoặc $dq$ cho nhiệt — sai vì $q$ không phải hàm trạng thái, không có 'giá trị của $q$ tại một trạng thái' để lấy hiệu; chỉ tồn tại lượng nhiệt trao đổi dọc một đường đi cụ thể.
- Dùng $w=-nRT\ln(V_2/V_1)$ cho dãn nở vào chân không — sai vì công thức đó giả thiết áp suất ngoài luôn bằng áp suất hệ; khi dãn vào chân không $p_{\text{ng}}=0$ nên $w=0$ dù thể tích vẫn tăng gấp đôi.
- Nhầm 'thuận nghịch' với 'quay lại được' — một quá trình bất thuận nghịch vẫn có thể đưa hệ về trạng thái đầu, nhưng khi đó môi trường đã thay đổi vĩnh viễn; thuận nghịch đòi hỏi cả hệ và môi trường cùng trở về nguyên trạng.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.he-va-qua-trinh`</sub>

---

### 2. Nguyên lí thứ nhất, enthalpy và nhiệt phản ứng
*First law, enthalpy and reaction heat* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Phát biểu được nguyên lí I dưới dạng vi phân và dạng tích phân cho hệ kín
- Giải thích được vì sao nhiệt đẳng áp bằng biến thiên enthalpy còn nhiệt đẳng tích bằng biến thiên nội năng
- Vận dụng được định luật Hess và nhiệt tạo thành chuẩn để tính nhiệt phản ứng

## Bảo toàn năng lượng viết cho hệ hoá học

Nguyên lí I khẳng định nội năng của hệ kín chỉ đổi khi hệ trao đổi nhiệt hoặc công:

$$dU=\delta q+\delta w,\qquad \Delta U=q+w$$

Quy ước dấu hiện đại: mọi thứ đi **vào** hệ mang dấu dương. Với hệ cô lập $\Delta U=0$ — đó là lí do không tồn tại động cơ vĩnh cửu loại một.

## Vì sao phải phát minh ra enthalpy

Phòng thí nghiệm hoá học làm việc trong cốc hở, tức đẳng áp, và ở đó khí sinh ra phải đẩy khí quyển ra, tiêu tốn công $-p\Delta V$. Nhiệt đo được không bằng $\Delta U$. Đặt

$$H=U+pV \;\Rightarrow\; dH=dU+p\,dV+V\,dp$$

Ở $p$ không đổi và chỉ có công thể tích, $dU=\delta q_p-p\,dV$, nên $dH=\delta q_p$, tức $\Delta H = q_p$. Trong khi đó bom nhiệt lượng kế giữ $V$ không đổi cho $\Delta U=q_V$. Hai đại lượng liên hệ với nhau qua số mol khí biến đổi:

$$\Delta H=\Delta U+\Delta n_{\text{khí}}RT$$

## Định luật Hess và bảng nhiệt tạo thành

Vì $H$ là hàm trạng thái, nhiệt phản ứng không phụ thuộc cách đi từ chất đầu tới sản phẩm. Đó là **định luật Hess**, và hệ quả thực dụng của nó là ta chỉ cần một bảng $\Delta_f H^\circ$ duy nhất:

$$\Delta_r H^\circ=\sum \nu_i \Delta_f H^\circ(\text{sp})-\sum \nu_j \Delta_f H^\circ(\text{cđ})$$

## Khi nào dùng được

Các hệ thức trên giả thiết hệ **kín**, chỉ có công thể tích. Nếu hệ sinh công điện (pin) hay công bề mặt thì $\Delta H\ne q_p$ nữa. Ngoài ra $\Delta_f H^\circ$ của đơn chất bền bằng 0 chỉ theo quy ước, và quy ước đó gắn với một dạng thù hình cụ thể: graphite chứ không phải kim cương.

**Lỗi thường gặp:**
- Đếm cả chất lỏng và chất rắn vào $\Delta n$ khi dùng $\Delta H=\Delta U+\Delta nRT$ — sai vì hệ thức này xuất phát từ $pV=nRT$ chỉ áp dụng cho pha khí; thể tích mol của pha ngưng tụ nhỏ hơn khoảng ba bậc nên đóng góp $p\Delta V$ của chúng bỏ qua được.
- Lấy $\Delta_f H^\circ$ của O$_2$(l) hay C(kim cương) bằng 0 — sai vì quy ước bằng 0 chỉ dành cho dạng bền nhất ở trạng thái chuẩn, tức O$_2$(g) và C(graphite); dùng dạng khác sẽ bỏ sót nhiệt chuyển pha hoặc nhiệt chuyển thù hình.
- Cho rằng $\Delta H<0$ thì phản ứng chắc chắn tự xảy ra — sai vì chiều tự diễn biến do $\Delta G$ quyết định; nhiều phản ứng thu nhiệt vẫn tự xảy ra nhờ số hạng entropy, ví dụ sự hoà tan NH$_4$NO$_3$ trong nước.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.nguyen-li-i-va-enthalpy`</sub>

---

### 3. Nhiệt dung và sự phụ thuộc nhiệt độ của nhiệt phản ứng
*Heat capacities and the Kirchhoff equation* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Định nghĩa được nhiệt dung đẳng áp và đẳng tích qua đạo hàm của hàm trạng thái tương ứng
- Chứng minh được hệ thức Mayer cho khí lí tưởng
- Vận dụng được phương trình Kirchhoff để quy đổi nhiệt phản ứng sang nhiệt độ khác

## Hai nhiệt dung, hai điều kiện

Đun nóng một hệ ở thể tích không đổi thì toàn bộ nhiệt đi vào nội năng; ở áp suất không đổi thì một phần nhiệt bị "rút" ra làm công đẩy môi trường. Vì thế phải phân biệt

$$C_V=\left(\frac{\partial U}{\partial T}\right)_V,\qquad C_p=\left(\frac{\partial H}{\partial T}\right)_p$$

Với khí lí tưởng, $H=U+nRT$ nên lấy đạo hàm theo $T$ ta được ngay **hệ thức Mayer** $C_{p,m}-C_{V,m}=R$. Con số $R\approx 8{,}31$ J/(mol·K) chính là công dãn nở trên mỗi mol, mỗi kelvin.

## Vì sao nhiệt phản ứng lại phụ thuộc nhiệt độ

Bảng nhiệt hoá học cho $\Delta_r H^\circ$ ở 298 K, nhưng lò công nghiệp chạy ở 700 K. Chất đầu và sản phẩm có nhiệt dung khác nhau, nên khi nâng nhiệt độ, enthalpy của hai vế tăng không bằng nhau. Lấy đạo hàm hiệu enthalpy:

$$\left(\frac{\partial \Delta_r H}{\partial T}\right)_p=\Delta_r C_p=\sum \nu_i C_{p,i}(\text{sp})-\sum \nu_j C_{p,j}(\text{cđ})$$

Tích phân từ $T_1$ tới $T_2$ cho dạng dùng được:

$$\Delta_r H(T_2)=\Delta_r H(T_1)+\int_{T_1}^{T_2}\Delta_r C_p\,dT$$

Nếu $\Delta_r C_p$ coi như hằng số trong khoảng đó thì tích phân thành $\Delta_r C_p (T_2-T_1)$.

## Khi nào dạng đơn giản hỏng

Dạng $\Delta_r C_p$ = const chỉ chấp nhận được trên khoảng vài chục kelvin. Trên khoảng rộng phải dùng $C_p=a+bT+c/T^2$ rồi tích phân từng số hạng. Quan trọng hơn: nếu trong khoảng $[T_1,T_2]$ có chất **chuyển pha** thì phải chia tích phân tại điểm chuyển pha và cộng thêm enthalpy chuyển pha, vì $C_p$ phân kì tại đó.

**Lỗi thường gặp:**
- Lấy $\Delta_r C_p$ bằng tổng nhiệt dung các chất thay vì hiệu sản phẩm trừ chất đầu — sai vì Kirchhoff sinh ra từ đạo hàm của một **hiệu** enthalpy, nên hệ số hợp thức phải mang dấu như trong $\Delta_r H$.
- Áp dụng Kirchhoff xuyên qua nhiệt độ sôi hoặc nhiệt độ nóng chảy của một chất — sai vì tại điểm chuyển pha enthalpy nhảy bậc, $C_p$ không hữu hạn; phải tách tích phân và cộng $\Delta_{\text{cp}}H$.
- Dùng $C_{p,m}-C_{V,m}=R$ cho chất lỏng hay chất rắn — sai vì hệ thức Mayer dựa trên $pV=nRT$; với pha ngưng tụ hiệu này rất nhỏ và phải tính qua $\alpha$, $\kappa_T$.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.nhiet-dung-va-kirchhoff`</sub>

---

### 4. Nguyên lí thứ hai và entropy
*The second law and entropy* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Phát biểu được nguyên lí II theo Clausius và theo bất đẳng thức entropy của hệ cô lập
- Chứng minh được hiệu suất cực đại của máy nhiệt bằng hiệu suất chu trình Carnot
- Tính được biến thiên entropy cho quá trình đun nóng, dãn nở đẳng nhiệt và chuyển pha

## Nguyên lí I không đủ

Nguyên lí I không cấm nhiệt tự truyền từ vật lạnh sang vật nóng, cũng không cấm một cốc nước tự sôi lên trong khi phòng nguội đi — cả hai đều bảo toàn năng lượng. Thực tế lại chỉ cho một chiều. Nguyên lí II là phát biểu định lượng của chiều đó.

## Từ máy nhiệt tới hàm trạng thái mới

Carnot chỉ ra rằng máy nhiệt thuận nghịch chạy giữa hai nguồn $T_n$ và $T_l$ có hiệu suất

$$\eta_{\max}=1-\frac{T_l}{T_n}$$

và không máy nào vượt được. Tính tổng $q/T$ quanh chu trình Carnot ta được $\sum q_{\text{tn}}/T=0$: đại lượng $\delta q_{\text{tn}}/T$ có tích phân theo chu trình bằng 0, tức nó là vi phân của một **hàm trạng thái**. Clausius gọi đó là entropy:

$$dS=\frac{\delta q_{\text{tn}}}{T}$$

Với quá trình bất kì, $dS\ge \delta q/T$; áp dụng cho hệ cô lập ($\delta q=0$) ta được tiêu chuẩn quen thuộc $\Delta S_{\text{cô lập}}\ge 0$.

## Ba phép tính hay dùng

- Đun nóng đẳng áp: $\Delta S=\int_{T_1}^{T_2} \dfrac{C_p}{T}dT = C_p\ln\dfrac{T_2}{T_1}$ khi $C_p$ không đổi.
- Dãn nở đẳng nhiệt khí lí tưởng: $\Delta S=nR\ln\dfrac{V_2}{V_1}$.
- Chuyển pha ở nhiệt độ chuyển pha: $\Delta S=\dfrac{\Delta H_{\text{cp}}}{T_{\text{cp}}}$.

## Bẫy lớn nhất

$S$ là hàm trạng thái, nên để tính $\Delta S$ của một quá trình **bất thuận nghịch** ta vẫn dùng ba công thức trên — nhưng phải hiểu chúng như tính dọc một đường **thuận nghịch giả định** nối cùng hai đầu. Ví dụ khí dãn vào chân không: $q=0$ nhưng $\Delta S=nR\ln 2>0$, vì đường thuận nghịch tương đương phải nhận nhiệt. Và đừng quên: chỉ $\Delta S_{\text{hệ}}+\Delta S_{\text{môi trường}}$ mới bắt buộc không âm.

**Lỗi thường gặp:**
- Kết luận 'phản ứng có $\Delta S_{\text{hệ}}<0$ thì không tự xảy ra' — sai vì nguyên lí II chỉ cấm $\Delta S_{\text{vũ trụ}}<0$; phản ứng toả nhiệt làm entropy môi trường tăng và có thể bù thừa, ví dụ sự đóng băng của nước dưới 273 K.
- Dùng $\Delta S=q/T$ với $q$ đo được trong quá trình bất thuận nghịch — sai vì định nghĩa entropy đòi hỏi nhiệt **thuận nghịch**; dùng $q$ thực luôn cho giá trị nhỏ hơn giá trị đúng.
- Nhầm entropy với 'độ lộn xộn' theo nghĩa hình ảnh — cách nói này khiến nhiều người kết luận sai với các quá trình hoà tan hay tạo phức, nơi entropy của dung môi (giải phóng hoặc bị cấu trúc hoá) mới là số hạng quyết định.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.nguyen-li-ii-va-entropy`</sub>

---

### 5. Nguyên lí thứ ba và entropy tuyệt đối
*The third law and absolute entropies* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Phát biểu được nguyên lí III và nêu điều kiện về tinh thể hoàn hảo
- Giải thích được vì sao hoá học có bảng entropy tuyệt đối nhưng không có bảng enthalpy tuyệt đối
- Tính được entropy dư của tinh thể có bất trật tự dư bằng công thức Boltzmann

## Một mốc chung cho entropy

Nguyên lí I và II chỉ cho ta **biến thiên**. Với entropy, nguyên lí III cấp thêm một mốc tuyệt đối: tinh thể hoàn hảo của chất nguyên chất có $S\to 0$ khi $T\to 0$. Lí do vi mô nằm ở công thức Boltzmann

$$S=k_B\ln W$$

Tinh thể hoàn hảo ở 0 K chỉ có **một** vi trạng thái ($W=1$), nên $S=0$.

## Hệ quả thực dụng: bảng $S^\circ$

Nhờ mốc đó, entropy tuyệt đối đo được bằng nhiệt lượng kế:

$$S^\circ(T)=\int_0^{T_{nc}}\frac{C_p^{(r)}}{T}dT+\frac{\Delta_{nc}H}{T_{nc}}+\int_{T_{nc}}^{T_s}\frac{C_p^{(l)}}{T}dT+\frac{\Delta_{h}H}{T_{s}}+\int_{T_s}^{T}\frac{C_p^{(k)}}{T}dT$$

Vì thế bảng nhiệt hoá học ghi $\Delta_f H^\circ$ (biến thiên) nhưng ghi $S^\circ$ (giá trị tuyệt đối). Entropy phản ứng tính trực tiếp:

$$\Delta_r S^\circ=\sum \nu_i S_i^\circ(\text{sp})-\sum \nu_j S_j^\circ(\text{cđ})$$

Chú ý $S^\circ$ của đơn chất **không** bằng 0 ở 298 K.

## Khi tinh thể không hoàn hảo

CO, N$_2$O, nước đá có mômen lưỡng cực nhỏ hoặc ràng buộc hình học, nên khi làm lạnh chúng "đóng băng" ở trạng thái bất trật tự. Với CO, mỗi phân tử có 2 hướng gần như đẳng năng, $W=2^{N_A}$ cho một mol, nên

$$S_{\text{dư}}=R\ln 2\approx 5{,}8\ \mathrm{J\,mol^{-1}K^{-1}}$$

đúng bằng chênh lệch giữa $S^\circ$ đo bằng nhiệt lượng kế và $S^\circ$ tính bằng nhiệt động thống kê. Sự khớp này là bằng chứng mạnh cho cả nguyên lí III lẫn công thức Boltzmann.

**Lỗi thường gặp:**
- Cho rằng $S^\circ$ của đơn chất bền bằng 0 giống như $\Delta_f H^\circ$ — sai vì nguyên lí III đặt mốc 0 tại **0 K**, còn bảng $S^\circ$ lập ở 298 K, nơi mọi chất đều đã tích luỹ entropy nhiệt.
- Tích phân $C_p/T$ từ 0 K mà dùng $C_p$ hằng số — sai vì $C_p\to 0$ khi $T\to 0$ (định luật $T^3$ của Debye); nếu giữ $C_p$ hằng số thì tích phân phân kì logarit và cho entropy vô hạn.
- Kết luận entropy dư nghĩa là nguyên lí III bị vi phạm — sai vì nguyên lí III phát biểu cho **tinh thể hoàn hảo**; CO và nước đá không đạt trạng thái cân bằng cấu hình khi làm lạnh nên chỉ là hệ bị đóng băng động học.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.nguyen-li-iii-va-entropy-tuyet-doi`</sub>

---

### 6. Năng lượng Gibbs, Helmholtz và tiêu chuẩn tự diễn biến
*Gibbs and Helmholtz energies and criteria of spontaneity* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Xây dựng được năng lượng Gibbs và Helmholtz từ bất đẳng thức Clausius
- Vận dụng được tiêu chuẩn $\Delta G<0$ để xét chiều tự diễn biến ở $T$, $p$ không đổi
- Liên hệ được $\Delta_r G^\circ$ với hằng số cân bằng và với sự phụ thuộc nhiệt độ của nó

## Chuyển tiêu chuẩn từ vũ trụ về hệ

Tiêu chuẩn $\Delta S_{\text{vũ trụ}}\ge 0$ đúng nhưng bất tiện: nhà hoá học chỉ đo được đại lượng của hệ. Ở $T$, $p$ không đổi, môi trường nhận nhiệt $-\Delta H$ một cách thuận nghịch nên $\Delta S_{\text{mt}}=-\Delta H/T$. Thay vào:

$$\Delta S_{\text{vũ trụ}}=\Delta S-\frac{\Delta H}{T}\ge 0 \;\Longleftrightarrow\; \Delta H-T\Delta S\le 0$$

Vế trái là $\Delta G$ với $G\equiv H-TS$. Vậy $\Delta G<0$ chỉ là nguyên lí II viết lại **hoàn toàn bằng đại lượng của hệ**. Tương tự, ở $T$, $V$ không đổi ta được $A=U-TS$.

## Ý nghĩa công

Từ $dG=Vdp-SdT+\delta w_{\text{phi thể tích}}$ ta thấy ở $T$, $p$ cố định $\Delta G = w_{\text{phi thể tích, max}}$. Đây là cầu nối tới điện hoá: $\Delta_r G=-nFE$.

## Phụ thuộc áp suất và nhiệt độ

$$\left(\frac{\partial G}{\partial p}\right)_T=V,\qquad \left(\frac{\partial G}{\partial T}\right)_p=-S$$

Với khí lí tưởng, tích phân số hạng đầu cho $G(p_2)=G(p_1)+nRT\ln(p_2/p_1)$. Số hạng thứ hai dẫn tới phương trình **Gibbs–Helmholtz**:

$$\left(\frac{\partial (G/T)}{\partial T}\right)_p=-\frac{H}{T^2}$$

## Nối với cân bằng

Đặt $\Delta_r G=\Delta_r G^\circ+RT\ln Q$ (đẳng nhiệt Van't Hoff). Tại cân bằng $\Delta_r G=0$ và $Q=K$, nên

$$\Delta_r G^\circ=-RT\ln K$$

Lưu ý: $\Delta_r G^\circ$ là hằng số ở mỗi nhiệt độ, còn $\Delta_r G$ thay đổi liên tục khi phản ứng tiến triển. Nói "phản ứng có $\Delta G^\circ>0$ nên không xảy ra" là sai — nó vẫn xảy ra tới một mức chuyển hoá nhỏ.

**Lỗi thường gặp:**
- Dùng $\Delta_r G^\circ$ để kết luận phản ứng 'không xảy ra' — sai vì $\Delta_r G^\circ$ ứng với điều kiện mọi chất ở trạng thái chuẩn; chiều thực tế do $\Delta_r G=\Delta_r G^\circ+RT\ln Q$ quyết định và luôn có một mức chuyển hoá khác 0.
- Cộng $\Delta_r H^\circ$ (kJ) với $T\Delta_r S^\circ$ (J) mà quên đổi đơn vị — sai về mặt thứ nguyên và sai số lên tới 1000 lần; đây là lỗi số học phổ biến nhất trong bài toán Gibbs.
- Cho rằng $\Delta G<0$ nghĩa là phản ứng xảy ra nhanh — sai vì nhiệt động chỉ nói về chiều và mức độ cân bằng; tốc độ do rào hoạt hoá quyết định, ví dụ hỗn hợp H$_2$ và O$_2$ có $\Delta G$ rất âm nhưng bền vô hạn ở nhiệt độ phòng.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.nang-luong-gibbs-va-helmholtz`</sub>

---

### 7. Bốn phương trình cơ bản và các hệ thức Maxwell
*The fundamental equations and Maxwell relations* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Viết được bốn phương trình cơ bản của nhiệt động lực học cho hệ kín
- Chứng minh được các hệ thức Maxwell từ điều kiện vi phân toàn phần
- Vận dụng được hệ thức Maxwell để thay đại lượng khó đo bằng đại lượng đo được

## Hợp nhất hai nguyên lí

Với hệ kín, quá trình thuận nghịch, chỉ công thể tích: $\delta q_{\text{tn}}=T\,dS$ và $\delta w=-p\,dV$, nên

$$dU=T\,dS-p\,dV$$

Vì cả hai vế chỉ chứa hàm trạng thái, đẳng thức này đúng cho **mọi** quá trình, kể cả bất thuận nghịch. Từ định nghĩa $H=U+pV$, $A=U-TS$, $G=H-TS$ suy ra ba bạn đồng hành:

$$dH=T\,dS+V\,dp,\quad dA=-S\,dT-p\,dV,\quad dG=-S\,dT+V\,dp$$

## Cỗ máy sinh hệ thức

Nếu $dz=M\,dx+N\,dy$ là vi phân toàn phần thì $(\partial M/\partial y)_x=(\partial N/\partial x)_y$. Áp dụng lần lượt cho bốn phương trình trên:

$$\left(\frac{\partial T}{\partial V}\right)_S=-\left(\frac{\partial p}{\partial S}\right)_V,\qquad \left(\frac{\partial T}{\partial p}\right)_S=\left(\frac{\partial V}{\partial S}\right)_p$$

$$\left(\frac{\partial S}{\partial V}\right)_T=\left(\frac{\partial p}{\partial T}\right)_V,\qquad \left(\frac{\partial S}{\partial p}\right)_T=-\left(\frac{\partial V}{\partial T}\right)_p$$

## Vì sao chúng có giá trị thực

Hai hệ thức cuối đắt giá nhất, vì vế trái chứa entropy — không đo trực tiếp được — còn vế phải chỉ cần dữ liệu $p$–$V$–$T$. Nhờ đó ta tính được **áp suất nội**:

$$\left(\frac{\partial U}{\partial V}\right)_T=T\left(\frac{\partial p}{\partial T}\right)_V-p$$

Với khí lí tưởng $p=nRT/V$ cho $T(\partial p/\partial T)_V=p$, nên vế phải bằng 0: nội năng khí lí tưởng không phụ thuộc thể tích — kết quả Joule đo bằng thực nghiệm nay suy ra được bằng vài dòng toán.

## Điều kiện áp dụng

Các hệ thức đòi hỏi hệ **kín, thành phần không đổi**, chỉ có công thể tích. Hệ có phản ứng hoá học hay trao đổi chất phải bổ sung số hạng $\sum \mu_i\,dn_i$, và khi đó số hệ thức Maxwell tăng lên tương ứng.

**Lỗi thường gặp:**
- Ghi nhớ máy móc dấu của bốn hệ thức Maxwell — dễ sai; nên suy lại từ phương trình cơ bản tương ứng, vì dấu trừ chỉ xuất hiện khi biến đi kèm mang dấu trừ trong vi phân ($-S\,dT$ hoặc $-p\,dV$).
- Dùng $(\partial U/\partial V)_T=0$ cho khí thực — sai vì kết quả đó chỉ suy ra được khi $p$ tỉ lệ thuận với $T$ ở $V$ cố định; khí thực có lực hút nên nội năng tăng khi dãn đẳng nhiệt.
- Áp dụng $dG=-S\,dT+V\,dp$ cho hệ đang xảy ra phản ứng — sai vì phương trình này viết cho thành phần cố định; khi $n_i$ thay đổi phải thêm $\sum\mu_i\,dn_i$, nếu bỏ qua sẽ mất chính số hạng quyết định cân bằng hoá học.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.he-thuc-maxwell`</sub>

---

### 8. Thế hoá học và đại lượng mol riêng phần
*Chemical potential and partial molar quantities* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Định nghĩa được đại lượng mol riêng phần và giải thích vì sao nó khác đại lượng mol của chất nguyên chất
- Xác định được thế hoá học là năng lượng Gibbs mol riêng phần và dùng nó làm tiêu chuẩn cân bằng vật chất
- Vận dụng được phương trình Gibbs - Duhem để ràng buộc các đại lượng mol riêng phần trong hỗn hợp

## Một mol nước không phải lúc nào cũng là 18 cm³

Thêm 1 mol nước vào nước nguyên chất, thể tích tăng 18,0 cm³. Thêm 1 mol nước vào một lượng lớn ethanol, thể tích chỉ tăng 14,0 cm³, vì phân tử nước lọt vào hốc trong mạng liên kết hydro của ethanol. Đại lượng đúng để mô tả là **thể tích mol riêng phần**

$$V_i=\left(\frac{\partial V}{\partial n_i}\right)_{T,p,n_{j\ne i}},\qquad V=\sum_i n_i V_i$$

Nó phụ thuộc thành phần, và có thể **âm** (MgSO$_4$ trong nước loãng) khi ion co cụm được lớp hydrat hoá.

## Thế hoá học: đại lượng mol riêng phần quan trọng nhất

Áp dụng ý tưởng đó cho $G$ ta được thế hoá học $\mu_i$. Phương trình cơ bản mở rộng thành

$$dG=-S\,dT+V\,dp+\sum_i \mu_i\,dn_i$$

Ở $T$, $p$ không đổi, $dG=\sum_i \mu_i\,dn_i$. Từ đây:

- **Cân bằng pha**: cấu tử $i$ có cùng $\mu_i$ trong mọi pha cùng tồn tại, nếu không nó sẽ chảy từ pha có $\mu$ cao sang pha có $\mu$ thấp.
- **Cân bằng hoá học**: $\sum_i \nu_i\mu_i=0$, chính là $\Delta_r G=0$.

Với khí lí tưởng, $\mu=\mu^\circ+RT\ln(p/p^\circ)$; với cấu tử trong dung dịch lí tưởng, $\mu_i=\mu_i^*+RT\ln x_i$.

## Ràng buộc Gibbs - Duhem

Lấy vi phân $G=\sum n_i\mu_i$ rồi so với phương trình cơ bản, ở $T$, $p$ cố định ta được

$$\sum_i n_i\,d\mu_i=0$$

Trong hệ hai cấu tử, $x_1 d\mu_1 = -x_2 d\mu_2$: nếu thế hoá học của dung môi giảm thì của chất tan phải tăng. Hệ quả rất thực dụng — đo hoạt độ của **một** cấu tử là đủ để tính hoạt độ cấu tử kia bằng tích phân.

**Lỗi thường gặp:**
- Cộng thể tích các chất nguyên chất để tính thể tích dung dịch — sai vì tương tác giữa các cấu tử khác với tương tác trong chất nguyên chất; chỉ dung dịch lí tưởng mới có $\Delta_{\text{trộn}}V=0$.
- Cho rằng thế hoá học chỉ liên quan đến phản ứng hoá học — sai vì $\mu$ điều khiển mọi quá trình trao đổi vật chất: bay hơi, hoà tan, thẩm thấu, khuếch tán đều được xét bằng chênh lệch $\mu$.
- Coi các $\mu_i$ trong một pha là độc lập nhau — sai vì Gibbs - Duhem ràng buộc chúng; bỏ qua ràng buộc này sẽ dẫn tới mô hình hoạt độ mâu thuẫn nhiệt động, ví dụ đặt hệ số hoạt độ của chất tan tuỳ ý mà vẫn giữ dung môi lí tưởng.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.the-hoa-hoc-va-mol-rieng-phan`</sub>

---

### 9. Cân bằng pha, quy tắc pha và phương trình Clapeyron
*Phase equilibria, the phase rule and the Clapeyron equation* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Xác định được số bậc tự do của một hệ bằng quy tắc pha Gibbs
- Chứng minh được phương trình Clapeyron từ điều kiện cân bằng thế hoá học
- Vận dụng được phương trình Clausius - Clapeyron để tính enthalpy hoá hơi từ dữ liệu áp suất hơi

## Điều kiện cân bằng pha

Hai pha $\alpha$, $\beta$ cùng tồn tại khi mỗi cấu tử có cùng thế hoá học trong cả hai:

$$\mu_i^{\alpha}(T,p)=\mu_i^{\beta}(T,p)$$

Đếm số phương trình và số ẩn cho ngay **quy tắc pha Gibbs**

$$f=c-p+2$$

Với chất nguyên chất ($c=1$): một pha thì $f=2$ (một miền trên giản đồ), hai pha thì $f=1$ (một đường), ba pha thì $f=0$ (một điểm — điểm ba, không thể chọn tuỳ ý cả $T$ lẫn $p$).

## Từ cân bằng ra độ dốc của đường cong

Đi dọc đường hai pha, $d\mu^{\alpha}=d\mu^{\beta}$. Dùng $d\mu=-S_m dT+V_m dp$ cho mỗi pha rồi sắp xếp lại:

$$\frac{dp}{dT}=\frac{\Delta_{\text{cp}}S_m}{\Delta_{\text{cp}}V_m}=\frac{\Delta_{\text{cp}}H_m}{T\,\Delta_{\text{cp}}V_m}$$

Đó là **phương trình Clapeyron**, đúng cho mọi chuyển pha bậc một. Nó giải thích ngay vì sao đường nóng chảy của nước nghiêng sang trái: $\Delta_{nc}V_m<0$ nên $dp/dT<0$.

## Trường hợp có hơi: Clausius - Clapeyron

Khi một pha là hơi, $\Delta V_m\approx V_m(\text{hơi})=RT/p$, dẫn tới

$$\frac{d\ln p}{dT}=\frac{\Delta_{h}H_m}{RT^2}\;\Longrightarrow\; \ln\frac{p_2}{p_1}=-\frac{\Delta_{h}H_m}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right)$$

Đồ thị $\ln p$ theo $1/T$ là đường thẳng có hệ số góc $-\Delta_h H_m/R$ — cách chuẩn để đo enthalpy hoá hơi.

## Ba giả thiết cần kiểm tra

Dạng tích phân giả thiết: hơi là khí lí tưởng, thể tích pha ngưng tụ bỏ qua được, và $\Delta_h H_m$ không đổi trong khoảng nhiệt độ xét. Gần **điểm tới hạn** cả ba đều hỏng, và ở đó $\Delta_h H_m\to 0$.

**Lỗi thường gặp:**
- Dùng nhiệt độ Celsius trong Clausius - Clapeyron — sai vì công thức chứa $1/T$ với $T$ tuyệt đối; dùng độ C làm mẫu số đổi hoàn toàn giá trị và có thể chia cho 0.
- Áp dụng Clausius - Clapeyron cho cân bằng rắn - lỏng — sai vì phép rút gọn $\Delta V\approx V_{\text{hơi}}=RT/p$ chỉ đúng khi có pha khí; với nóng chảy phải dùng phương trình Clapeyron đầy đủ.
- Đếm số cấu tử $c$ bằng số chất có mặt — sai vì $c$ là số cấu tử **độc lập**: mỗi phản ứng cân bằng và mỗi ràng buộc hợp thức đều làm giảm $c$ đi một đơn vị, ví dụ hệ CaCO$_3$/CaO/CO$_2$ có 3 chất nhưng $c=2$.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.can-bang-pha-va-quy-tac-pha`</sub>

---

### 10. Giản đồ pha hai cấu tử và quy tắc đòn bẩy
*Two-component phase diagrams and the lever rule* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Đọc được giản đồ nhiệt độ - thành phần của hệ lỏng - hơi và hệ rắn - lỏng
- Vận dụng được quy tắc đòn bẩy để tính lượng tương đối của hai pha cân bằng
- Giải thích được hiện tượng azeotrope và điểm eutectic bằng nhiệt động của dung dịch

## Vì sao cần trục thành phần

Với hệ hai cấu tử, quy tắc pha cho $f=4-p$. Cố định áp suất còn $f'=3-p$, nên với hai pha $f'=1$: chọn nhiệt độ là thành phần cả hai pha bị ấn định. Đó là lí do giản đồ $T$–$x$ ở $p$ cố định mô tả trọn vẹn hệ.

## Đọc giản đồ lỏng - hơi

Hệ lí tưởng tuân theo định luật Raoult, $p_i=x_i p_i^*$, và tổng áp suất là hàm bậc nhất của $x$. Vẽ theo nhiệt độ ta được hai đường: đường dưới cho thành phần **lỏng**, đường trên cho thành phần **hơi**. Điểm biểu diễn hệ nằm giữa hai đường thì hệ tách thành hai pha, thành phần mỗi pha đọc ở hai đầu đường nối ngang.

Lượng tương đối của hai pha suy ra từ bảo toàn vật chất — **quy tắc đòn bẩy**:

$$n_{\alpha}\,\ell_{\alpha}=n_{\beta}\,\ell_{\beta}$$

với $\ell$ là khoảng cách từ điểm hệ tới đầu mút tương ứng. Điểm hệ càng gần một đường thì pha đó càng nhiều.

## Khi dung dịch không lí tưởng

Sai lệch dương mạnh (ethanol - nước) làm đường sôi có **cực tiểu**; sai lệch âm mạnh (HNO$_3$ - nước) cho **cực đại**. Tại cực trị, đường lỏng và đường hơi tiếp xúc nhau: pha hơi có cùng thành phần với pha lỏng, tức **azeotrope**. Chưng cất phân đoạn ethanol - nước vì thế dừng ở 95,6 % khối lượng, muốn vượt qua phải đổi áp suất hoặc dùng chất kéo theo.

## Hệ rắn - lỏng

Hai chất không tan lẫn ở trạng thái rắn cho giản đồ hình chữ V với **điểm eutectic** ở đáy: cả hai nhánh đều là đường hạ điểm đông đặc của một cấu tử bởi cấu tử kia. Tại eutectic $f'=0$, nên hỗn hợp nóng chảy ở nhiệt độ xác định như một chất nguyên chất — cơ sở của hợp kim hàn và của muối rải đường băng.

**Lỗi thường gặp:**
- Áp dụng quy tắc đòn bẩy với đoạn cùng phía — sai vì tỉ lệ là **nghịch**: pha ở gần điểm hệ hơn thì có số mol lớn hơn, nên $n_\alpha/n_\beta = \ell_\beta/\ell_\alpha$.
- Cho rằng chưng cất phân đoạn luôn tách được hai chất lỏng tinh khiết — sai khi hệ có azeotrope, vì tại đó pha hơi trùng thành phần pha lỏng nên mỗi lần ngưng - bay hơi không làm giàu thêm được nữa.
- Dùng định luật Raoult cho chất tan loãng thay vì định luật Henry — sai vì cấu tử ở nồng độ rất nhỏ nằm trong môi trường toàn phân tử khác loại; áp suất riêng phần của nó tỉ lệ với $x$ nhưng hằng số tỉ lệ là $K_H$ chứ không phải $p^*$.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.gian-do-pha-hai-cau-tu`</sub>

---

### 11. Dung dịch thực, hoạt độ và hệ số hoạt độ
*Real solutions, activity and activity coefficients* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao phải thay nồng độ bằng hoạt độ trong biểu thức thế hoá học
- Phân biệt được hai quy ước định nghĩa hoạt độ theo Raoult và theo Henry
- Tính được hệ số hoạt độ trung bình ion bằng định luật giới hạn Debye - Hückel

## Vì sao lí tưởng không đủ

Với dung dịch lí tưởng, $\mu_i=\mu_i^*+RT\ln x_i$. Dung dịch thực lệch khỏi Raoult vì tương tác A–B khác trung bình của A–A và B–B. Thay vì vứt bỏ công thức đẹp, Lewis giữ nguyên dạng và **định nghĩa lại biến**:

$$\mu_i=\mu_i^{\circ}+RT\ln a_i,\qquad a_i=\gamma_i x_i$$

Toàn bộ sai lệch bị dồn vào $\gamma_i$, một đại lượng đo được.

## Hai quy ước, đừng trộn lẫn

- **Quy ước Raoult** (dùng cho dung môi): trạng thái chuẩn là chất nguyên chất, $\gamma_i\to 1$ khi $x_i\to 1$; đo qua $a_i=p_i/p_i^*$.
- **Quy ước Henry** (dùng cho chất tan): trạng thái chuẩn là trạng thái giả định ngoại suy từ dung dịch loãng, $\gamma_i\to 1$ khi $x_i\to 0$; đo qua $a_i=p_i/K_{H,i}$.

Cùng một dung dịch có hai bộ $\gamma$ khác nhau vì hai mốc khác nhau — số liệu phải đi kèm quy ước.

## Dung dịch điện li: sai lệch xuất hiện ngay ở nồng độ rất nhỏ

Ion tương tác Coulomb tầm xa, nên ngay ở $10^{-3}$ mol/L đã lệch rõ. Mỗi ion bị bao bởi một "khí quyển ion" tích điện trái dấu, làm hạ năng lượng Gibbs của nó. Debye và Hückel tính được, ở giới hạn loãng:

$$\log \gamma_{\pm}=-A|z_+z_-|\sqrt{I},\qquad A=0{,}509\ (\text{nước},\,25\ ^\circ\mathrm{C})$$

với lực ion $I=\tfrac12\sum_i z_i^2 (c_i/c^\circ)$.

## Ranh giới áp dụng

Định luật **giới hạn** chỉ tin được tới $I\lesssim 0{,}01$. Trên mức đó dùng dạng mở rộng $\log\gamma_\pm=-A|z_+z_-|\sqrt I/(1+B a\sqrt I)$ hoặc phương trình Davies (tới $I\approx 0{,}5$). Ở nồng độ cao $\gamma_\pm$ có thể **vượt quá 1** do hiệu ứng hydrat hoá làm giảm lượng nước tự do — điều mà mô hình Debye - Hückel không mô tả được vì nó coi dung môi là môi trường liên tục.

**Lỗi thường gặp:**
- Lấy lực ion bằng nồng độ mol của muối — sai vì mỗi ion đóng góp theo $z^2$ và theo số ion sinh ra; với CaCl$_2$ lực ion gấp 3 lần nồng độ, với MgSO$_4$ gấp 4 lần.
- Dùng định luật giới hạn Debye - Hückel cho nước biển hay dịch sinh lí ($I\approx 0{,}1$–0,7) — sai vì mô hình chỉ giữ số hạng bậc $\sqrt I$ đầu tiên; ở đó phải dùng phương trình Davies hoặc mô hình Pitzer.
- Trộn lẫn hai quy ước hoạt độ trong cùng một phép tính — sai vì $\gamma$ theo Raoult và theo Henry quy chiếu về hai trạng thái chuẩn khác nhau, nên $\mu^\circ$ đi kèm cũng khác; ghép chúng lại sẽ sai một hằng số cộng trong $\mu$.

<sub>`lesson.chemistry.nhiet-dong-hoa-hoc.dung-dich-thuc-va-hoat-do`</sub>

---

## Unit 2: Động hoá học

### 1. Định luật tốc độ thực nghiệm và cách xác định bậc phản ứng
*Empirical rate laws and determination of reaction order* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Định nghĩa được tốc độ phản ứng theo độ chuyển hoá để không phụ thuộc chất được theo dõi
- Phân biệt được bậc phản ứng với hệ số hợp thức và với phân tử số
- Vận dụng được phương pháp tốc độ đầu, phương pháp cô lập và phương pháp tích phân để tìm bậc

## Định nghĩa tốc độ cho đúng

Với phản ứng $2\mathrm{A}\to 3\mathrm{B}$, nếu định nghĩa tốc độ theo A ta được một số, theo B ta được số khác gấp 1,5 lần. Cách sửa là chia cho hệ số hợp thức có dấu:

$$v=\frac{1}{\nu_i}\frac{d[i]}{dt}$$

với $\nu_i<0$ cho chất đầu. Khi đó chỉ có **một** tốc độ cho cả phản ứng.

## Định luật tốc độ là dữ liệu, không phải suy luận

Không thể đọc bậc phản ứng từ phương trình hoá học. Phản ứng $\mathrm{H_2+Br_2\to 2HBr}$ có định luật tốc độ

$$v=\frac{k[\mathrm{H_2}][\mathrm{Br_2}]^{1/2}}{1+k'[\mathrm{HBr}]/[\mathrm{Br_2}]}$$

không hề có bậc xác định. Định luật tốc độ phải **đo**; nó là dữ kiện dùng để loại bỏ cơ chế sai.

## Ba phương pháp tìm bậc

1. **Tốc độ đầu**: đo $v_0$ ở nhiều $[\mathrm{A}]_0$ khác nhau; $\ln v_0 = \ln k + a\ln[\mathrm{A}]_0$ cho hệ số góc là bậc riêng $a$. Ưu điểm: tránh nhiễu do sản phẩm.
2. **Cô lập Ostwald**: giữ mọi chất khác ở nồng độ dư lớn để chúng coi như không đổi, phản ứng trở thành **giả bậc** theo một chất.
3. **Tích phân**: giả thiết một bậc rồi kiểm tra tuyến tính. Bậc 1 cho $\ln[\mathrm{A}]$ tuyến tính theo $t$; bậc 2 cho $1/[\mathrm{A}]$ tuyến tính; bậc 0 cho chính $[\mathrm{A}]$ tuyến tính.

## Dấu hiệu nhanh: thời gian bán huỷ

$$t_{1/2}=\frac{\ln 2}{k}\ (\text{bậc 1}),\qquad t_{1/2}=\frac{1}{k[\mathrm{A}]_0}\ (\text{bậc 2}),\qquad t_{1/2}=\frac{[\mathrm{A}]_0}{2k}\ (\text{bậc 0})$$

Chỉ bậc 1 có $t_{1/2}$ **không phụ thuộc nồng độ đầu**. Vì thế chỉ cần kiểm tra xem thời gian giảm một nửa có lặp lại đều đặn hay không là đã đoán được bậc.

## Cảnh báo về đơn vị

Thứ nguyên của $k$ là (nồng độ)$^{1-n}$(thời gian)$^{-1}$. Nếu đơn vị của $k$ tính ra không khớp với bậc giả định thì chắc chắn có lỗi ở đâu đó — đây là phép kiểm tra rẻ nhất trong động hoá học.

**Lỗi thường gặp:**
- Suy bậc phản ứng từ hệ số hợp thức — sai vì hệ số hợp thức chỉ mô tả cân bằng vật chất tổng, còn tốc độ do bước chậm nhất trong cơ chế quyết định; chỉ với bước **sơ cấp** hai đại lượng mới trùng nhau.
- Nói 'phản ứng bậc 2' khi thấy $1/[\mathrm{A}]$ tuyến tính mà không kiểm tra khoảng chuyển hoá — sai vì ở mức chuyển hoá thấp mọi mô hình đều cho đường gần thẳng; phải theo dõi ít nhất tới 2–3 lần bán huỷ mới phân biệt được.
- Dùng $t_{1/2}=\ln 2/k$ cho mọi phản ứng — sai vì công thức đó riêng cho bậc 1; với bậc 2 thời gian bán huỷ tăng gấp đôi sau mỗi lần bán huỷ, dùng nhầm sẽ ước lượng sai hằng loạt về độ bền của chất.

<sub>`lesson.chemistry.dong-hoa-hoc.dinh-luat-toc-do-thuc-nghiem`</sub>

---

### 2. Cơ chế phản ứng, nồng độ ổn định và tiền cân bằng
*Reaction mechanisms, steady state and pre-equilibrium* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Xây dựng được định luật tốc độ từ một cơ chế giả định bằng nguyên lí nồng độ ổn định
- Phân biệt được điều kiện áp dụng xấp xỉ nồng độ ổn định và xấp xỉ tiền cân bằng
- Phân tích được động học của phản ứng nối tiếp, song song và thuận nghịch bậc một

## Cơ chế là giả thuyết, định luật tốc độ là bằng chứng

Không ai "nhìn thấy" cơ chế. Ta đề xuất một chuỗi bước sơ cấp, suy ra định luật tốc độ, rồi so với thực nghiệm. Cơ chế nào cho định luật sai thì bị loại; cơ chế nào cho định luật đúng thì **chưa** được chứng minh, mới chỉ chưa bị bác bỏ.

## Nồng độ ổn định

Với cơ chế $\mathrm{A}\xrightarrow{k_1}\mathrm{I}\xrightarrow{k_2}\mathrm{P}$, nếu $k_2\gg k_1$ thì I sinh ra bao nhiêu tiêu thụ gần hết bấy nhiêu, nồng độ của nó nhỏ và gần như không đổi. Đặt

$$\frac{d[\mathrm{I}]}{dt}\approx 0 \;\Rightarrow\; [\mathrm{I}]_{ss}=\frac{k_1[\mathrm{A}]}{k_2}$$

rồi thay vào biểu thức tốc độ tạo sản phẩm. Kĩ thuật này biến hệ phương trình vi phân thành hệ đại số.

## Tiền cân bằng

Nếu cơ chế là $\mathrm{A}+\mathrm{B}\underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}}\mathrm{I}\xrightarrow{k_2}\mathrm{P}$ với $k_{-1}\gg k_2$, bước đầu kịp đạt cân bằng:

$$[\mathrm{I}]=K[\mathrm{A}][\mathrm{B}],\quad K=\frac{k_1}{k_{-1}} \;\Rightarrow\; v=k_2K[\mathrm{A}][\mathrm{B}]$$

Đây thực chất là **trường hợp riêng** của nồng độ ổn định: dạng tổng quát $v=\dfrac{k_1k_2[\mathrm{A}][\mathrm{B}]}{k_{-1}+k_2}$ rút về tiền cân bằng khi $k_{-1}\gg k_2$, và rút về "bước 1 quyết định" khi $k_2\gg k_{-1}$.

## Ba sơ đồ chuẩn

- **Nối tiếp** $\mathrm{A}\to\mathrm{I}\to\mathrm{P}$: $[\mathrm{I}]$ đi qua cực đại tại $t_{\max}=\dfrac{\ln(k_2/k_1)}{k_2-k_1}$.
- **Song song** $\mathrm{A}\to\mathrm{P_1}$, $\mathrm{A}\to\mathrm{P_2}$: A mất theo bậc 1 với hằng số $k_1+k_2$, và tỉ lệ sản phẩm luôn bằng $k_1/k_2$ ở mọi thời điểm — cơ sở của khống chế động học.
- **Thuận nghịch bậc 1**: hệ tiến về cân bằng theo hàm mũ với hằng số $k_1+k_{-1}$, còn vị trí cân bằng cho $K=k_1/k_{-1}$.

## Khi xấp xỉ hỏng

Nồng độ ổn định sai trong **giai đoạn cảm ứng** đầu tiên và sai khi chất trung gian tích luỹ đáng kể (khi $k_1 \gtrsim k_2$). Với phản ứng nổ hay dao động, nồng độ trung gian biến thiên mạnh nên không được dùng.

**Lỗi thường gặp:**
- Đặt $d[\mathrm{I}]/dt=0$ cho một chất trung gian **bền** tích luỹ được — sai vì nồng độ ổn định đòi hỏi chất trung gian có tốc độ tiêu thụ lớn hơn nhiều tốc độ sinh ra; với chất trung gian bền phải giải hệ vi phân đầy đủ.
- Coi $[\mathrm{I}]_{ss}$ là hằng số theo thời gian — sai vì 'ổn định' chỉ có nghĩa $d[\mathrm{I}]/dt$ nhỏ so với các tốc độ khác; $[\mathrm{I}]_{ss}$ vẫn giảm dần vì tỉ lệ với $[\mathrm{A}]$ đang giảm.
- Cho rằng bước quyết định tốc độ luôn là bước chậm nhất trong danh sách — sai vì cái quyết định là **rào năng lượng cao nhất tính từ trạng thái bền phía trước**; một bước có hằng số tốc độ nhỏ nhưng đi sau một tiền cân bằng bất lợi vẫn có thể không phải bước khống chế.

<sub>`lesson.chemistry.dong-hoa-hoc.co-che-va-nong-do-on-dinh`</sub>

---

### 3. Thuyết va chạm và ý nghĩa của phương trình Arrhenius
*Collision theory and the meaning of the Arrhenius equation* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Giải thích được nguồn gốc của thừa số mũ và thừa số trước mũ trong phương trình Arrhenius
- Tính được tần số va chạm và hằng số tốc độ theo thuyết va chạm cho phản ứng pha khí
- Đánh giá được vì sao thuyết va chạm cần thừa số định hướng và khi nào nó thất bại

## Vì sao tốc độ tăng vọt theo nhiệt độ

Tăng nhiệt độ từ 300 K lên 310 K chỉ làm tốc độ trung bình của phân tử tăng khoảng 1,6 %, nhưng tốc độ phản ứng thường tăng gấp đôi. Vậy yếu tố quyết định không phải tốc độ trung bình mà là **phần đuôi** phân bố Maxwell - Boltzmann — số phân tử có năng lượng vượt ngưỡng. Phần đó tỉ lệ với $e^{-E_a/RT}$, và đây là gốc của

$$k=A\,e^{-E_a/RT},\qquad \ln k=\ln A-\frac{E_a}{R}\cdot\frac{1}{T}$$

Đồ thị $\ln k$ theo $1/T$ (đồ thị Arrhenius) cho hệ số góc $-E_a/R$.

## Ghép ba yếu tố

Thuyết va chạm viết tốc độ như tích của ba thừa số:

$$k = \underbrace{\sigma \langle v_{\text{rel}}\rangle N_A}_{\text{tần số va chạm}}\times \underbrace{e^{-E_a/RT}}_{\text{đủ năng lượng}}\times \underbrace{P}_{\text{đúng hướng}}$$

với $\langle v_{\text{rel}}\rangle=\sqrt{8k_BT/\pi\mu}$ và $\mu$ là khối lượng rút gọn. Với tiết diện va chạm điển hình $\sigma\sim 0{,}5$ nm$^2$ và $\langle v_{\text{rel}}\rangle\sim 500$ m/s, thừa số tần số va chạm trong khí ở điều kiện thường vào cỡ $10^{11}$ L mol$^{-1}$s$^{-1}$ — nếu mọi va chạm đều phản ứng thì mọi phản ứng khí đều tức thời.

## Thừa số định hướng nói lên điều gì

Với $\mathrm{K}+\mathrm{Br_2}$, $P\approx 4{,}8$ (lớn hơn 1!) vì electron "nhảy" sang Br$_2$ ở khoảng cách xa, tiết diện hiệu dụng lớn hơn tiết diện hình học. Với phản ứng giữa hai phân tử hữu cơ cồng kềnh, $P$ có thể xuống $10^{-5}$: chỉ một hướng tiếp cận rất hẹp mới dẫn tới phản ứng. Chính sự tuỳ tiện của $P$ là điểm yếu của thuyết va chạm — nó mô tả chứ không tiên đoán.

## Ranh giới áp dụng

Mô hình coi phân tử là quả cầu cứng không cấu trúc, nên chỉ khá tốt cho phản ứng nguyên tử - phân tử đơn giản trong pha khí. Nó bỏ qua bậc tự do quay và dao động, bỏ qua hiệu ứng đường hầm, và không dùng được cho phản ứng trong dung dịch, nơi chuyển động là khuếch tán chứ không phải bay tự do.

**Lỗi thường gặp:**
- Coi $E_a$ là 'năng lượng của phản ứng' và so sánh với $\Delta_r H$ — sai vì $E_a$ đo rào chắn giữa chất đầu và trạng thái chuyển tiếp, không liên quan trực tiếp tới hiệu enthalpy giữa chất đầu và sản phẩm; phản ứng toả nhiệt mạnh vẫn có thể có $E_a$ rất lớn.
- Kết luận $A$ luôn nhỏ hơn tần số va chạm — sai trong các phản ứng 'harpoon' như K + Br$_2$, nơi chuyển electron ở khoảng cách xa làm tiết diện hiệu dụng lớn hơn tiết diện hình học nên $P>1$.
- Vẽ đồ thị $\ln k$ theo $T$ thay vì theo $1/T$ — sai vì Arrhenius là tuyến tính theo nghịch đảo nhiệt độ; vẽ theo $T$ cho đường cong và hệ số góc không có ý nghĩa vật lí.

<sub>`lesson.chemistry.dong-hoa-hoc.thuyet-va-cham`</sub>

---

### 4. Thuyết trạng thái chuyển tiếp và phương trình Eyring
*Transition state theory and the Eyring equation* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Trình bày được các giả thiết nền tảng của thuyết trạng thái chuyển tiếp
- Vận dụng được phương trình Eyring để tách enthalpy và entropy hoạt hoá từ dữ liệu nhiệt độ
- Giải thích được dấu của entropy hoạt hoá theo phân tử tính của bước quyết định tốc độ

## Thay quả cầu cứng bằng mặt thế năng

Thuyết va chạm không tiên đoán được $P$ vì nó bỏ qua cấu trúc phân tử. Eyring đổi cách nhìn: phản ứng là chuyển động của điểm biểu diễn hệ trên **mặt thế năng**, và mọi hệ muốn thành sản phẩm đều phải đi qua điểm yên ngựa — trạng thái chuyển tiếp $\mathrm{X}^{\ddagger}$.

Giả thiết cốt lõi: $\mathrm{A}+\mathrm{B}\rightleftharpoons \mathrm{X}^{\ddagger}$ ở cân bằng giả, và $\mathrm{X}^{\ddagger}$ tan rã với tần số phổ quát $k_BT/h$. Kết quả:

$$k=\kappa\,\frac{k_BT}{h}\,K^{\ddagger}=\kappa\,\frac{k_BT}{h}\exp\!\left(-\frac{\Delta^{\ddagger}G^{\circ}}{RT}\right)$$

## Dạng dùng được cho thực nghiệm

Tách $\Delta^{\ddagger}G^\circ=\Delta^{\ddagger}H^\circ-T\Delta^{\ddagger}S^\circ$:

$$\ln\frac{k}{T}=-\frac{\Delta^{\ddagger}H^{\circ}}{R}\cdot\frac{1}{T}+\ln\frac{k_B}{h}+\frac{\Delta^{\ddagger}S^{\circ}}{R}$$

Đồ thị **Eyring** ($\ln(k/T)$ theo $1/T$) cho hệ số góc $-\Delta^{\ddagger}H^\circ/R$ và tung độ gốc chứa $\Delta^{\ddagger}S^\circ$. So với Arrhenius, ta thu thêm một thông tin quý: entropy hoạt hoá.

Với phản ứng trong dung dịch hoặc phản ứng lưỡng phân tử pha khí, $E_a=\Delta^{\ddagger}H^\circ+RT$ (pha khí lưỡng phân tử: $E_a=\Delta^{\ddagger}H^\circ+2RT$).

## Đọc dấu của $\Delta^{\ddagger}S^\circ$

- Rất âm ($-100$ tới $-200$ J/(mol·K)): hai tiểu phân phải gặp và định hướng chặt — cơ chế **kết hợp** (S$_N$2, Diels - Alder).
- Gần 0 hoặc dương: liên kết bị kéo dãn, hệ trở nên tự do hơn — cơ chế **phân li** (S$_N$1, phân huỷ đơn phân tử).

Chính $\Delta^{\ddagger}S^\circ$ là bản dịch nhiệt động của thừa số định hướng $P$ trong thuyết va chạm.

## Giới hạn

Giả thiết cân bằng giả và $\kappa=1$ bỏ qua hiện tượng **vượt rồi quay lại**. Ở nhiệt độ thấp, phản ứng chuyển proton hay chuyển hydride có **hiệu ứng đường hầm** đáng kể, khiến $k$ lớn hơn dự đoán và đồ thị Arrhenius bị cong.

**Lỗi thường gặp:**
- Đồng nhất $E_a$ với $\Delta^{\ddagger}H^\circ$ — sai vì $E_a$ định nghĩa qua đạo hàm của $\ln k$, còn Eyring có thêm thừa số $T$ trước hàm mũ; chênh lệch là $RT$ hoặc $2RT$ tuỳ pha và phân tử số, cỡ 2,5–5 kJ/mol ở nhiệt độ phòng.
- Vẽ $\ln k$ theo $1/T$ rồi gọi tung độ gốc là $\Delta^{\ddagger}S^\circ/R$ — sai vì entropy hoạt hoá chỉ tách được từ đồ thị $\ln(k/T)$; bỏ quên thừa số $T$ làm sai $\Delta^{\ddagger}S^\circ$ một lượng phụ thuộc khoảng nhiệt độ.
- Coi trạng thái chuyển tiếp là một chất trung gian có thể phân lập — sai vì nó nằm ở **cực đại** theo toạ độ phản ứng, tức không có cực tiểu năng lượng để tồn tại; chất trung gian phân lập được nằm ở hõm giữa hai rào.

<sub>`lesson.chemistry.dong-hoa-hoc.trang-thai-chuyen-tiep-eyring`</sub>

---

### 5. Phản ứng trong dung dịch: khuếch tán, hiệu ứng lồng và hiệu ứng dung môi
*Reactions in solution: diffusion control, cage effect and solvent effects* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được phản ứng khống chế bởi khuếch tán và phản ứng khống chế bởi hoạt hoá
- Vận dụng được quan hệ Stokes - Einstein để tính hằng số tốc độ giới hạn khuếch tán
- Phân tích được ảnh hưởng của độ phân cực dung môi và của lực ion lên tốc độ phản ứng

## Dung dịch không phải pha khí loãng

Trong pha khí, hai phân tử gặp nhau rồi tách ngay. Trong dung dịch, chúng bị "nhốt" trong một **lồng dung môi** và va chạm hàng trăm lần trước khi khuếch tán ra. Vì thế số lần gặp mỗi giây nhỏ hơn nhiều, nhưng mỗi lần gặp lại kéo dài hơn nhiều — hai hiệu ứng bù trừ, và với phản ứng có $E_a$ đáng kể, tốc độ trong dung dịch không khác pha khí bao nhiêu.

## Trần tốc độ do khuếch tán

Nếu rào hoạt hoá gần bằng 0, mọi lần gặp đều thành công, và tốc độ chỉ còn bị chặn bởi khuếch tán:

$$k_d=4\pi (r_A+r_B)(D_A+D_B)N_A,\qquad D=\frac{k_BT}{6\pi\eta r}$$

Ghép hai công thức cho ước lượng đơn giản $k_d\approx \dfrac{8RT}{3\eta}$. Trong nước ở 25 °C, $k_d\sim 7\times10^{9}$ L mol$^{-1}$s$^{-1}$. Không phản ứng lưỡng phân tử trung hoà nào trong nước vượt được con số này — đó là **giới hạn hoàn hảo xúc tác** mà một số enzyme đạt tới.

Dấu hiệu nhận biết: $E_a$ đo được chỉ khoảng 15–20 kJ/mol, đúng bằng năng lượng hoạt hoá của **độ nhớt**, chứ không phải của phản ứng.

## Dung môi làm gì

Quy tắc **Hughes - Ingold**: dung môi phân cực ổn định trạng thái nào có mật độ điện tích tập trung hơn.
- Nếu phức hoạt động phân cực **hơn** chất đầu (ví dụ S$_N$1 tạo carbocation), tăng độ phân cực làm giảm $\Delta^{\ddagger}G$ và **tăng** tốc độ.
- Nếu điện tích bị **phân tán** trong phức hoạt động (ví dụ anion + phân tử trung hoà trong S$_N$2), tăng độ phân cực làm **giảm** tốc độ.

## Lực ion

Với hai ion điện tích $z_A$, $z_B$, phương trình Brønsted - Bjerrum cho

$$\log\frac{k}{k_0}=2A z_Az_B\sqrt{I}$$

Cùng dấu điện tích thì tăng lực ion làm tăng tốc độ; trái dấu thì làm giảm. Dấu của hệ số góc trong đồ thị $\log k$ theo $\sqrt I$ vì thế là **bằng chứng trực tiếp** về điện tích của hai tiểu phân trong bước quyết định tốc độ.

**Lỗi thường gặp:**
- Cho rằng phản ứng trong dung dịch luôn chậm hơn trong pha khí vì 'phân tử khó gặp nhau' — sai vì hiệu ứng lồng bù lại: số lần gặp ít hơn nhưng mỗi lần gặp gồm rất nhiều va chạm, nên tổng số va chạm mỗi giây gần như không đổi.
- Dùng phương trình Brønsted - Bjerrum cho phản ứng có một chất trung hoà — sai vì khi $z_A$ hoặc $z_B$ bằng 0 thì tích bằng 0 và mô hình dự đoán không có hiệu ứng muối sơ cấp; hiệu ứng quan sát được khi đó thuộc loại thứ cấp (thay đổi nồng độ ion phản ứng).
- Kết luận dung môi phân cực luôn làm tăng tốc độ phản ứng ion — sai vì nếu điện tích bị phân tán trong phức hoạt động thì dung môi phân cực ổn định chất đầu nhiều hơn, làm rào tăng và tốc độ giảm.

<sub>`lesson.chemistry.dong-hoa-hoc.phan-ung-trong-dung-dich`</sub>

---

### 6. Xúc tác đồng thể, dị thể và enzyme
*Homogeneous, heterogeneous and enzyme catalysis* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao xúc tác làm tăng tốc độ mà không dịch chuyển cân bằng
- Phân tích được động học xúc tác dị thể theo cơ chế Langmuir - Hinshelwood và Eley - Rideal
- Vận dụng được phương trình Michaelis - Menten và đồ thị Lineweaver - Burk để xác định $K_M$ và $v_{\max}$

## Xúc tác chỉ đổi đường, không đổi đích

Xúc tác hạ $\Delta^{\ddagger}G$ nên tăng $k$ theo hàm mũ:

$$\frac{k_{xt}}{k_0}=\exp\!\left(\frac{\Delta^{\ddagger}G_0-\Delta^{\ddagger}G_{xt}}{RT}\right)$$

Nhưng nó hạ rào theo **cả hai chiều** như nhau, nên $K=k_{thuận}/k_{nghịch}$ không đổi. Xúc tác không thể làm phản ứng có $\Delta_r G>0$ trở nên tự xảy ra.

## Xúc tác đồng thể

Xúc tác axit - bazơ là điển hình. Xúc tác axit đặc hiệu do $\mathrm{H_3O^+}$ gây ra; xúc tác axit tổng quát do mọi axit Brønsted trong dung dịch gây ra, và hằng số của chúng tuân theo hệ thức **Brønsted** $k_{HA}=G_A K_a^{\alpha}$ — một quan hệ tuyến tính giữa năng lượng tự do hoạt hoá và năng lượng tự do cân bằng.

## Xúc tác dị thể

Phản ứng xảy ra trên bề mặt, nên trước hết phải mô tả hấp phụ. Đẳng nhiệt **Langmuir** cho độ che phủ $\theta=\dfrac{Kp}{1+Kp}$.

- **Langmuir - Hinshelwood**: cả A và B đều hấp phụ, $v=k\theta_A\theta_B$. Hệ quả đặc trưng: tốc độ đi qua **cực đại** theo áp suất một chất, vì chất đó dư sẽ chiếm hết chỗ và đẩy chất kia khỏi bề mặt.
- **Eley - Rideal**: chỉ A hấp phụ, B tấn công từ pha khí, $v=k\theta_A p_B$; tốc độ tăng đơn điệu theo $p_B$.

Dạng phụ thuộc áp suất vì thế phân biệt được hai cơ chế bằng thực nghiệm.

## Enzyme

Với $\mathrm{E}+\mathrm{S}\rightleftharpoons \mathrm{ES}\to \mathrm{E}+\mathrm{P}$, áp dụng nồng độ ổn định cho ES:

$$v=\frac{v_{\max}[\mathrm{S}]}{K_M+[\mathrm{S}]},\qquad v_{\max}=k_{cat}[\mathrm{E}]_0$$

Ở $[\mathrm{S}]\ll K_M$ động học là bậc một với hằng số $(k_{cat}/K_M)[\mathrm{E}]_0$; ở $[\mathrm{S}]\gg K_M$ enzyme bão hoà và động học là **bậc không**. Nghịch đảo hai vế cho đường thẳng Lineweaver - Burk

$$\frac{1}{v}=\frac{K_M}{v_{\max}}\cdot\frac{1}{[\mathrm{S}]}+\frac{1}{v_{\max}}$$

Chất ức chế cạnh tranh làm $K_M$ biểu kiến tăng nhưng $v_{\max}$ không đổi — vì có thể đẩy lùi bằng cách tăng $[\mathrm{S}]$.

**Lỗi thường gặp:**
- Nói xúc tác 'làm cân bằng dịch về phía sản phẩm' — sai vì xúc tác hạ rào cho cả chiều thuận và chiều nghịch bằng đúng một lượng, nên $K$ giữ nguyên; nó chỉ rút ngắn thời gian đạt cân bằng.
- Đồng nhất $K_M$ với hằng số phân li của phức ES — sai vì $K_M=(k_{-1}+k_2)/k_1$ còn $K_S=k_{-1}/k_1$; hai đại lượng chỉ trùng nhau khi bước xúc tác chậm hơn nhiều bước tách ($k_2\ll k_{-1}$).
- Kết luận enzyme mạnh hơn khi $K_M$ nhỏ hơn — sai vì $K_M$ chỉ đo ái lực; hiệu quả xúc tác thực sự do $k_{cat}/K_M$ quyết định, và một enzyme ái lực rất mạnh nhưng $k_{cat}$ bé vẫn chậm.
- Dùng cơ chế Eley - Rideal khi thấy tốc độ giảm ở áp suất cao — sai vì cực đại rồi giảm theo áp suất là dấu hiệu đặc trưng của Langmuir - Hinshelwood, do cạnh tranh chỗ hấp phụ trên bề mặt.

<sub>`lesson.chemistry.dong-hoa-hoc.xuc-tac-dong-the-di-the-enzyme`</sub>

---

### 7. Quang hoá học: hiệu suất lượng tử và các quá trình khử kích thích
*Photochemistry: quantum yields and deactivation processes* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Phát biểu được hai định luật quang hoá học cơ bản và định nghĩa hiệu suất lượng tử
- Phân tích được giản đồ Jablonski để phân loại các quá trình bức xạ và không bức xạ
- Vận dụng được phương trình Stern - Volmer để xác định hằng số dập tắt và thời gian sống

## Ánh sáng như một chất phản ứng

Photon cung cấp năng lượng theo từng gói: ở 400 nm mỗi mol photon mang khoảng 300 kJ, đủ để bẻ nhiều liên kết. Quan trọng hơn, hấp thụ tạo ra một **trạng thái điện tử mới** với phân bố electron khác hẳn — nên quy tắc phản ứng ở trạng thái kích thích không giống trạng thái cơ bản.

Hai định luật nền: chỉ ánh sáng **bị hấp thụ** mới gây phản ứng (Grotthuss - Draper); và mỗi photon hấp thụ kích thích đúng một phân tử (Stark - Einstein).

## Hiệu suất lượng tử

$$\Phi=\frac{\text{số biến cố}}{\text{số photon hấp thụ}}$$

$\Phi$ của một quá trình sơ cấp không vượt 1. Nhưng hiệu suất lượng tử của **sản phẩm** có thể tới $10^6$ nếu photon khơi mào một dây chuyền, ví dụ phản ứng H$_2$ + Cl$_2$.

## Số phận của trạng thái kích thích

Sau hấp thụ, phân tử ở S$_1$ có nhiều lối thoát cạnh tranh nhau, mỗi lối là một hằng số tốc độ:

- **Huỳnh quang** ($k_f$): phát xạ S$_1\to$ S$_0$, cho phép về spin, thời gian sống ns.
- **Chuyển nội bộ** ($k_{ic}$): S$_1\to$ S$_0$ không bức xạ.
- **Chuyển hệ** ($k_{isc}$): S$_1\to$ T$_1$; sau đó **lân quang** T$_1\to$ S$_0$ bị cấm spin nên chậm ($\mu$s tới s).
- **Phản ứng** ($k_r$) và **dập tắt** ($k_q[\mathrm{Q}]$).

Thời gian sống quan sát $\tau=1/\sum k_i$ và $\Phi_f=k_f\tau$. Vì dịch chuyển Stokes, phổ phát xạ luôn ở bước sóng dài hơn phổ hấp thụ.

## Stern - Volmer: đo bằng tỉ số

Thêm chất dập tắt Q, áp dụng nồng độ ổn định cho S$_1$:

$$\frac{\Phi_{f,0}}{\Phi_f}=\frac{I_0}{I}=1+k_q\tau_0[\mathrm{Q}]$$

Đồ thị $I_0/I$ theo $[\mathrm{Q}]$ là đường thẳng có hệ số góc $K_{SV}=k_q\tau_0$. Đo riêng $\tau_0$ ta tách được $k_q$; nếu $k_q$ đạt cỡ $10^{10}$ M$^{-1}$s$^{-1}$ thì dập tắt bị khống chế bởi khuếch tán, tức mỗi lần gặp đều dập tắt.

**Lưu ý**: đồ thị Stern - Volmer cong lên là dấu hiệu có đồng thời dập tắt động (va chạm) và dập tắt tĩnh (tạo phức không phát xạ) — khi đó không được rút $k_q$ từ hệ số góc đơn giản.

**Lỗi thường gặp:**
- Cho rằng hiệu suất lượng tử không bao giờ vượt 1 — sai vì giới hạn đó chỉ áp dụng cho **quá trình sơ cấp**; phản ứng dây chuyền quang hoá có thể cho $\Phi$ hàng triệu vì một photon khơi mào rất nhiều chu kì lan truyền.
- Coi lân quang chỉ là 'huỳnh quang chậm' — sai vì lân quang xuất phát từ trạng thái triplet và bị cấm spin, nên vừa có thời gian sống dài hơn nhiều bậc vừa xuất hiện ở bước sóng dài hơn huỳnh quang của cùng chất.
- Rút $k_q$ từ hệ số góc Stern - Volmer khi đồ thị bị cong — sai vì độ cong báo hiệu hai cơ chế dập tắt cùng hoạt động; phương trình tuyến tính chỉ đúng cho dập tắt động thuần tuý.

<sub>`lesson.chemistry.dong-hoa-hoc.quang-hoa-hoc`</sub>

---

### 8. Phản ứng dây chuyền, độ dài mạch và giới hạn nổ
*Chain reactions, chain length and explosion limits* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Phân loại được các bước khơi mào, lan truyền, phân nhánh và ngắt mạch trong cơ chế dây chuyền
- Tính được độ dài mạch và giải thích ý nghĩa của nó
- Giải thích được sự tồn tại của ba giới hạn nổ trong phản ứng H$_2$ - O$_2$

## Bốn loại bước

Cơ chế dây chuyền luôn gồm:
1. **Khơi mào**: sinh gốc từ phân tử bền (nhiệt phân, quang phân, chất khơi mào).
2. **Lan truyền**: gốc phản ứng với phân tử bền, sinh sản phẩm **và** một gốc mới. Số gốc không đổi.
3. **Phân nhánh** (không phải lúc nào cũng có): một gốc sinh hai hoặc ba gốc.
4. **Ngắt mạch**: hai gốc kết hợp, hoặc gốc bị thành bình hấp phụ.

Đặc trưng động học: định luật tốc độ thường có **bậc phân số** (1/2, 3/2), vì nồng độ gốc ở trạng thái ổn định tỉ lệ với căn bậc hai của tốc độ khơi mào.

## Độ dài mạch

$$\ell=\frac{v_{\text{lan truyền}}}{v_{\text{khơi mào}}}=\frac{v_{\text{lan truyền}}}{v_{\text{ngắt mạch}}}$$

Với polymer hoá gốc tự do, $\ell$ chính là độ trùng hợp trung bình. Muốn chuỗi dài thì phải khơi mào **ít** — nghịch lí thực dụng: tăng nồng độ chất khơi mào làm phản ứng nhanh hơn nhưng polymer ngắn hơn.

## Vì sao nổ

Nếu chỉ có lan truyền, nồng độ gốc giữ ở mức ổn định thấp. Khi có phân nhánh, phương trình cho nồng độ gốc thành

$$\frac{d[\mathrm{R}]}{dt}=v_i+(f_{br}-f_{term})[\mathrm{R}]$$

Nếu tốc độ phân nhánh vượt tốc độ ngắt mạch, $[\mathrm{R}]$ tăng theo hàm mũ và hệ **nổ nhánh** — khác hẳn nổ nhiệt (do nhiệt toả ra làm tăng $k$).

## Ba giới hạn của H$_2$ + O$_2$

Cơ chế phân nhánh chính là $\mathrm{H\cdot+O_2\to OH\cdot+O:}$ và $\mathrm{O:+H_2\to OH\cdot+H\cdot}$.

- **Giới hạn thứ nhất** (áp suất rất thấp): gốc khuếch tán tới **thành bình** và bị huỷ trước khi phân nhánh. Tăng áp suất làm khuếch tán chậm lại, ngắt mạch trên thành yếu đi → nổ.
- **Giới hạn thứ hai**: áp suất cao hơn, ngắt mạch pha khí ba thể $\mathrm{H\cdot+O_2+M\to HO_2\cdot+M}$ thắng phân nhánh → tắt.
- **Giới hạn thứ ba**: áp suất rất cao, HO$_2$· lại trở nên phản ứng và toả nhiệt mạnh → nổ nhiệt.

Hình dạng "bán đảo nổ" trên giản đồ $p$–$T$ là bằng chứng đẹp nhất cho thấy cơ chế dây chuyền không phải suy đoán mà kiểm chứng được.

**Lỗi thường gặp:**
- Cho rằng bậc phân số nghĩa là dữ liệu sai — sai vì bậc 1/2 hoặc 3/2 là **hệ quả tất yếu** của ngắt mạch lưỡng phân tử: nồng độ gốc ổn định tỉ lệ với căn bậc hai tốc độ khơi mào.
- Đồng nhất mọi vụ nổ với nổ nhiệt — sai vì nổ nhánh xảy ra ngay cả khi nhiệt được tản hoàn toàn, do số gốc tăng theo hàm mũ; giới hạn nổ thứ nhất và thứ hai của H$_2$ - O$_2$ chỉ giải thích được bằng cơ chế nhánh.
- Nghĩ rằng tăng nồng độ chất khơi mào luôn có lợi trong trùng hợp gốc — sai vì độ dài mạch tỉ lệ nghịch với căn bậc hai tốc độ khơi mào, nên polymer thu được sẽ có khối lượng phân tử thấp hơn.

<sub>`lesson.chemistry.dong-hoa-hoc.phan-ung-day-chuyen`</sub>

---

## Unit 3: Chemical Thermodynamics and Equilibrium

### 1. Cân bằng hoá học nhiệt động: Hằng số Kp, Kx, Kn và Ảnh hưởng của khí trơ
*Chemical equilibrium thermodynamics: Kp, Kx, Kn relations and inert gas effects* · Đại học · intl-undergrad, vn-gdpt-2018 · 50 phút · nang-cao

**Mục tiêu:**
- Xác định thương số phản ứng Q và liên hệ giữa năng lượng tự do Gibbs với hằng số cân bằng
- Chuyển đổi linh hoạt giữa các hằng số cân bằng Kp, Kc, Kx và Kn
- Phân tích ảnh hưởng của việc thêm khí trơ ở điều kiện đẳng áp và đẳng tích lên độ chuyển hoá

## Các dạng hằng số cân bằng

Đối với phản ứng giữa các khí lý tưởng $\sum \nu_i A_i = 0$, hằng số cân bằng có thể biểu diễn qua áp suất riêng phần ($K_p$), nồng độ ($K_c$), phần mol ($K_x$) và số mol ($K_n$):

$$K_p = K_c (RT)^{\Delta n} = K_x P^{\Delta n} = K_n \left(\frac{P}{\sum n}\right)^{\Delta n}$$

Trong đó $\Delta n = \sum \nu_{khí\ sp} - \sum \nu_{khí\ cđ}$.

## Ảnh hưởng của khí trơ

- **Thêm khí trơ ở thể tích không đổi ($V = \text{const}$)**: Áp suất riêng phần của các chất phản ứng không đổi, cân bằng **không bị dịch chuyển**.
- **Thêm khí trơ ở áp suất không đổi ($P = \text{const}$)**: Tổng số mol khí tăng làm áp suất riêng phần từng chất giảm. Cân bằng sẽ dịch chuyển theo chiều làm tăng số mol khí (nếu $\Delta n > 0$, độ chuyển hoá tăng).

**Lỗi thường gặp:**
- Nghĩ rằng thêm khí trơ luôn làm dịch chuyển cân bằng (ở V không đổi cân bằng không đổi)
- Nhầm lẫn chiều chuyển dịch khi Delta n = 0 (khi Delta n = 0 áp suất và khí trơ không ảnh hưởng)

<sub>`lesson.chemistry.undergrad-chemistry.can-bang-hoa-hoc-nhiet-dong-va-hoat-do`</sub>

---

## Unit 3: Điện hoá học

### 1. Dung dịch điện li và lí thuyết Debye - Hückel
*Electrolyte solutions and Debye - Hückel theory* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Giải thích được vì sao dung dịch điện li lệch khỏi lí tưởng ngay ở nồng độ rất thấp
- Tính được lực ion và hệ số hoạt độ trung bình ion cho dung dịch nhiều chất điện li
- Xác định được độ dài Debye và giải thích ý nghĩa vật lí của khí quyển ion

## Vì sao muối "khó tính" hơn đường

Dung dịch glucose 0,01 M gần như lí tưởng. Dung dịch NaCl 0,01 M thì không: $\gamma_\pm\approx 0{,}90$. Khác biệt nằm ở **tầm** của tương tác. Lực giữa các phân tử trung hoà giảm theo $r^{-6}$; lực Coulomb giữa ion giảm theo $r^{-2}$, nên một ion "cảm nhận" được rất nhiều ion khác dù dung dịch loãng.

## Mô hình khí quyển ion

Debye và Hückel giả thiết: ion là điện tích điểm, dung môi là môi trường liên tục có hằng số điện môi $\varepsilon$, và phân bố ion quanh một ion trung tâm tuân theo Boltzmann. Giải phương trình Poisson - Boltzmann tuyến tính hoá cho thế bị **chắn**:

$$\phi(r)=\frac{z_ie}{4\pi\varepsilon r}e^{-r/r_D},\qquad r_D=\left(\frac{\varepsilon RT}{2F^2 I c^{\circ}}\right)^{1/2}$$

Trong nước 25 °C, $r_D\approx 0{,}304/\sqrt{I}$ nm: ở $I=0{,}001$ khí quyển dày khoảng 10 nm, ở $I=0{,}1$ chỉ còn 1 nm.

## Kết quả then chốt

Công thực hiện để "tạo" khí quyển ion làm hạ năng lượng Gibbs của ion, dẫn tới **định luật giới hạn**:

$$\log\gamma_{\pm}=-A|z_+z_-|\sqrt I,\qquad I=\tfrac12\sum_i z_i^2\frac{c_i}{c^{\circ}}$$

Hai điểm đáng chú ý: phụ thuộc $\sqrt I$ (không phải $I$) và phụ thuộc $z^2$. Vì thế MgSO$_4$ lệch mạnh hơn NaCl rất nhiều ở cùng nồng độ.

## Vì sao chỉ đo được $\gamma_\pm$

Không thể pha dung dịch chỉ chứa Na$^+$: điều kiện trung hoà điện buộc cation và anion đi cùng nhau. Do đó đại lượng đo được là trung bình nhân

$$\gamma_{\pm}=(\gamma_+^{p}\gamma_-^{q})^{1/(p+q)}$$

## Nơi mô hình hỏng

Coi ion là điểm khiến $\gamma_\pm\to 0$ khi $I$ lớn — trái thực nghiệm. Dạng mở rộng thêm bán kính ion $a$ vào mẫu số; phương trình Davies dùng được tới $I\approx 0{,}5$. Ở nồng độ rất cao, $\gamma_\pm$ **tăng vượt 1** do hydrat hoá làm giảm lượng dung môi tự do — hiệu ứng nằm ngoài khuôn khổ mô hình môi trường liên tục.

**Lỗi thường gặp:**
- Bỏ qua chất điện li trơ khi tính lực ion — sai vì mọi ion trong dung dịch đều góp vào khí quyển ion; đây là lỗi khiến các phép tính độ tan và pH trong dung dịch có nền muối lệch đáng kể.
- Tính hệ số hoạt độ riêng cho từng ion rồi báo cáo như đại lượng đo được — sai vì điều kiện trung hoà điện khiến $\gamma_+$ và $\gamma_-$ riêng lẻ không đo được bằng nhiệt động thuần tuý; chỉ $\gamma_\pm$ có ý nghĩa thực nghiệm.
- Cho rằng $\gamma_\pm$ luôn nhỏ hơn 1 — sai ở nồng độ cao, nơi hiệu ứng hydrat hoá làm hoạt độ nước giảm mạnh và $\gamma_\pm$ của nhiều muối vượt 1 (ví dụ HCl đặc).

<sub>`lesson.chemistry.dien-hoa-hoc.dung-dich-dien-li-debye-huckel`</sub>

---

### 2. Độ dẫn điện của dung dịch điện li
*Conductivity of electrolyte solutions* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Phân biệt được độ dẫn điện riêng, độ dẫn điện mol và độ dẫn điện mol giới hạn
- Vận dụng được định luật Kohlrausch để xác định độ dẫn giới hạn của chất điện li yếu
- Liên hệ được linh độ ion với số vận chuyển và với hệ số khuếch tán

## Từ điện trở tới đại lượng của chất

Đo điện trở $R$ của dung dịch trong bình có hằng số bình $C$ (xác định bằng KCl chuẩn) cho **độ dẫn điện riêng**

$$\kappa=\frac{C}{R}\quad [\mathrm{S\,m^{-1}}]$$

$\kappa$ phụ thuộc nồng độ, nên để so sánh các chất ta chia cho nồng độ:

$$\Lambda_m=\frac{\kappa}{c}$$

Nếu ion chuyển động hoàn toàn độc lập thì $\Lambda_m$ sẽ không đổi theo $c$. Thực tế nó luôn giảm khi $c$ tăng — và **kiểu** giảm hé lộ bản chất chất điện li.

## Hai hành vi, hai loại chất điện li

- **Chất điện li mạnh**: $\Lambda_m$ giảm chậm và tuyến tính theo $\sqrt c$:
$$\Lambda_m=\Lambda_m^{\circ}-K\sqrt c$$
Nguyên nhân là hiệu ứng bất đối xứng và hiệu ứng điện di của khí quyển ion, được lí thuyết Debye - Hückel - Onsager tính ra từ đầu.

- **Chất điện li yếu**: $\Lambda_m$ giảm rất mạnh ở nồng độ thấp, vì nguyên nhân không phải tương tác mà là **độ điện li** thay đổi. Ta đặt $\alpha=\Lambda_m/\Lambda_m^{\circ}$ và suy ra
$$K_a=\frac{c\alpha^2}{1-\alpha}$$
Không thể ngoại suy $\Lambda_m$ về $c\to 0$ cho chất điện li yếu; phải lấy $\Lambda_m^\circ$ gián tiếp qua **định luật Kohlrausch về chuyển động độc lập**, ví dụ
$$\Lambda_m^{\circ}(\mathrm{CH_3COOH})=\Lambda_m^{\circ}(\mathrm{CH_3COONa})+\Lambda_m^{\circ}(\mathrm{HCl})-\Lambda_m^{\circ}(\mathrm{NaCl})$$

## Ion nào chạy nhanh

$\lambda^\circ$ của H$^+$ (349,6 S cm² mol⁻¹) và OH$^-$ (199,1) lớn bất thường so với Na$^+$ (50,1). Lí do là **cơ chế Grotthuss**: proton không bơi qua dung dịch mà "nhảy" dọc mạng liên kết hydro. Đây cũng là lí do chuẩn độ dẫn điện có bước nhảy rất rõ tại điểm tương đương axit - bazơ.

## Nối với khuếch tán

Linh độ và hệ số khuếch tán liên hệ qua **Nernst - Einstein**:

$$D=\frac{RT}{z^2F^2}\lambda$$

Nhờ đó một phép đo độ dẫn điện đơn giản cho ngay hệ số khuếch tán của ion — đại lượng cần cho mọi bài toán động học điện cực.

**Lỗi thường gặp:**
- Ngoại suy $\Lambda_m$ theo $\sqrt c$ về $c=0$ cho chất điện li yếu — sai vì với chất điện li yếu độ dốc phân kì gần gốc (do $\alpha$ thay đổi), nên phải dùng định luật Kohlrausch về chuyển động độc lập.
- Kết luận độ dẫn điện riêng luôn tăng theo nồng độ — sai vì ở nồng độ cao $\kappa$ đi qua cực đại rồi giảm, do tương tác ion và độ nhớt tăng làm linh độ giảm nhanh hơn mức tăng số hạt tải.
- Giải thích linh độ lớn bất thường của H$^+$ bằng 'ion nhỏ nên chạy nhanh' — sai vì H$^+$ trong nước tồn tại dưới dạng hydrat lớn; nguyên nhân thật là cơ chế Grotthuss, tức chuyển proton dọc mạng liên kết hydro chứ không phải sự di chuyển của khối lượng.

<sub>`lesson.chemistry.dien-hoa-hoc.do-dan-dien-dung-dich`</sub>

---

### 3. Pin điện hoá, thế điện cực và phương trình Nernst
*Galvanic cells, electrode potentials and the Nernst equation* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Viết được sơ đồ pin theo quy ước IUPAC và xác định đúng dấu của sức điện động
- Vận dụng được phương trình Nernst cho pin và cho từng nửa phản ứng
- Phân loại được các kiểu điện cực và chọn được điện cực phù hợp cho phép đo

## Quy ước trước, tính toán sau

Sơ đồ pin viết **cực âm bên trái, cực dương bên phải**, ranh giới pha là $|$, cầu muối là $\|$. Phản ứng pin quy ước là: khử ở điện cực phải, oxi hoá ở điện cực trái. Khi đó

$$E=E_{\text{phải}}-E_{\text{trái}}$$

Nếu tính ra $E>0$ thì phản ứng viết theo quy ước là chiều tự xảy ra; nếu $E<0$ thì chiều thực tế ngược lại. Cách này tránh hoàn toàn việc "đoán" cực nào là anode.

## Nernst từ nhiệt động

Công điện tối đa ở $T$, $p$ không đổi bằng $\Delta_r G$:

$$\Delta_r G=-nFE$$

Thay $\Delta_r G=\Delta_r G^\circ+RT\ln Q$ và chia cho $-nF$:

$$E=E^{\circ}-\frac{RT}{nF}\ln Q \;\xrightarrow{\ 25\,^\circ\mathrm{C}\ }\; E=E^{\circ}-\frac{0{,}05916}{n}\log Q$$

Phương trình Nernst là **cầu nối** giữa một phép đo điện thế (rất chính xác, dễ thực hiện) và các đại lượng hoá học như hoạt độ, hằng số cân bằng, tích số tan.

## Thang thế chuẩn

Không đo được thế tuyệt đối của một điện cực, chỉ đo được hiệu. Vì thế người ta quy ước $E^\circ(\mathrm{SHE})=0$ và mọi $E^\circ$ trong bảng là sức điện động của pin ghép nửa đó với SHE, viết dưới dạng **quá trình khử**.

## Các kiểu điện cực

- **Loại 1** — $\mathrm{Zn}\,|\,\mathrm{Zn^{2+}}$: thế phụ thuộc $a(\mathrm{Zn^{2+}})$.
- **Loại 2** — $\mathrm{Ag}\,|\,\mathrm{AgCl}\,|\,\mathrm{Cl^-}$: thế phụ thuộc $a(\mathrm{Cl^-})$.
- **Điện cực khí** — $\mathrm{Pt}\,|\,\mathrm{H_2}\,|\,\mathrm{H^+}$: phụ thuộc $a(\mathrm{H^+})$ và $p(\mathrm{H_2})$.
- **Oxi hoá - khử** — $\mathrm{Pt}\,|\,\mathrm{Fe^{3+}},\mathrm{Fe^{2+}}$: phụ thuộc tỉ số hai hoạt độ.

Điện cực loại hai (Ag/AgCl, calomel) ổn định và dễ chế tạo nên được dùng làm **điện cực so sánh**; điện cực thuỷ tinh dùng đo pH nhờ màng thuỷ tinh chọn lọc H$^+$.

## Cảnh báo

$E^\circ$ nói về nhiệt động, không nói về tốc độ: cặp có $E^\circ$ thuận lợi vẫn có thể phản ứng cực chậm nếu quá thế lớn. Ngoài ra $Q$ phải viết bằng **hoạt độ**; dùng nồng độ là xấp xỉ chỉ chấp nhận được ở dung dịch loãng.

**Lỗi thường gặp:**
- Xác định anode/cathode bằng cách 'nhìn chất nào mạnh hơn' rồi mới viết sơ đồ — dễ sai dấu; cách an toàn là viết sơ đồ trước, luôn giả thiết khử ở bên phải, rồi để dấu của $E$ tự nói lên chiều thực.
- Dùng $n$ bằng số electron của một nửa phản ứng chưa cân bằng — sai vì $n$ trong Nernst là số electron trao đổi trong **phản ứng pin đã cân bằng**; nhân nhầm hệ số làm sai số hạng logarit theo tỉ lệ.
- Cho rằng nhân đôi hệ số phản ứng sẽ nhân đôi $E$ — sai vì $E$ là đại lượng **cường độ**: khi nhân đôi phương trình thì cả $\Delta_r G^\circ$ lẫn $n$ đều nhân đôi nên $E^\circ=-\Delta_r G^\circ/nF$ không đổi.
- Bỏ qua thế nối lỏng khi ghép hai dung dịch khác nhau — sai trong phép đo chính xác; cầu muối KCl bão hoà được dùng chính là để giảm thế nối lỏng xuống mức vài mV vì K$^+$ và Cl$^-$ có linh độ gần bằng nhau.

<sub>`lesson.chemistry.dien-hoa-hoc.pin-va-the-dien-cuc`</sub>

---

### 4. Nhiệt động học của pin: suy ra ΔG, ΔH, ΔS và K từ phép đo sức điện động
*Cell thermodynamics: obtaining Delta G, Delta H, Delta S and K from potential measurements* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Liên hệ được sức điện động với năng lượng Gibbs của phản ứng pin
- Xác định được $\Delta_r S$ và $\Delta_r H$ từ hệ số nhiệt độ của sức điện động
- Tính được hằng số cân bằng, tích số tan và hệ số hoạt độ từ dữ liệu điện hoá

## Vì sao vôn kế lại là dụng cụ nhiệt động

Đo $E$ ở dòng bằng 0 nghĩa là phản ứng chạy thuận nghịch, nên công điện đạt cực đại và bằng $\Delta_r G$:

$$\Delta_r G=-nFE,\qquad \Delta_r G^{\circ}=-nFE^{\circ}$$

Sai số của phép đo thế hiện đại cỡ $10^{-5}$ V, tương đương vài J/mol — độ chính xác mà nhiệt lượng kế không sánh được. Đó là lí do rất nhiều dữ liệu nhiệt động trong bảng có nguồn gốc điện hoá.

## Lấy đạo hàm theo nhiệt độ

Từ $(\partial G/\partial T)_p=-S$ suy ra ngay

$$\Delta_r S=nF\left(\frac{\partial E}{\partial T}\right)_p$$

và ghép hai kết quả:

$$\Delta_r H=\Delta_r G+T\Delta_r S=-nF\left[E-T\left(\frac{\partial E}{\partial T}\right)_p\right]$$

Nghĩa là chỉ cần đo $E$ ở vài nhiệt độ là có trọn bộ ba $\Delta G$, $\Delta S$, $\Delta H$ của phản ứng.

Hệ quả thực tế: nếu $(\partial E/\partial T)_p>0$ thì $\Delta_r S>0$, pin **hấp thụ** nhiệt khi hoạt động thuận nghịch và tự làm lạnh; nếu âm thì pin toả nhiệt ngoài phần nhiệt Joule.

## Ba ứng dụng chuẩn

1. **Hằng số cân bằng**: $\ln K = \dfrac{nFE^{\circ}}{RT}$. Một $E^\circ$ chỉ 0,3 V với $n=2$ đã cho $K\sim 10^{10}$.
2. **Tích số tan**: ghép pin có nửa Ag|AgCl|Cl⁻ với nửa Ag|Ag⁺; $E^\circ$ của pin cho ngay $K_{sp}(\mathrm{AgCl})$.
3. **Hệ số hoạt độ**: pin không có thế nối lỏng như Pt|H₂|HCl($m$)|AgCl|Ag cho
$$E=E^{\circ}-\frac{2RT}{F}\ln(m\gamma_{\pm}/m^{\circ})$$
Ngoại suy $E+\dfrac{2RT}{F}\ln m$ theo $\sqrt m$ về 0 cho $E^\circ$, và từ đó $\gamma_\pm$ ở mọi nồng độ. Đây là **cách chuẩn mực nhất** để có bảng $\gamma_\pm$.

## Điều kiện

Mọi hệ thức trên đòi hỏi pin **thuận nghịch**: không có phản ứng phụ, không có thế nối lỏng đáng kể, và phép đo ở dòng bằng 0. Pin có dòng chạy qua sẽ có sụt thế do quá thế và điện trở nội, khi đó $-nFE$ nhỏ hơn $|\Delta_r G|$ và phần chênh lệch biến thành nhiệt.

**Lỗi thường gặp:**
- Cho rằng toàn bộ $\Delta_r H$ của phản ứng pin chuyển thành điện năng — sai vì phần $T\Delta_r S$ bắt buộc trao đổi dưới dạng nhiệt ngay cả khi pin chạy thuận nghịch; chỉ $\Delta_r G$ mới là công điện tối đa.
- Dùng $(\partial E/\partial T)$ đo ở dòng lớn — sai vì khi có dòng, $E$ đo được bị trừ đi quá thế và sụt thế Ohm, cả hai đều phụ thuộc nhiệt độ, nên đạo hàm thu được không phải đại lượng nhiệt động.
- Quên rằng dấu của $\Delta_r S$ suy từ hệ số nhiệt độ chứ không từ dấu của $E$ — hai đại lượng độc lập; một pin có $E>0$ vẫn có thể có $\Delta_r S<0$, như chính ví dụ Ag/AgCl ở trên.

<sub>`lesson.chemistry.dien-hoa-hoc.nhiet-dong-cua-pin`</sub>

---

### 5. Động học điện cực: mật độ dòng trao đổi, Butler - Volmer và Tafel
*Electrode kinetics: exchange current density, Butler - Volmer and Tafel* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao quá thế là lực điều khiển của động học điện cực
- Vận dụng được phương trình Butler - Volmer và hai dạng giới hạn của nó
- Xác định được mật độ dòng trao đổi và hệ số chuyển từ đồ thị Tafel

## Cân bằng động ở bề mặt điện cực

Tại thế cân bằng, phản ứng điện cực **không** dừng: dòng anode và dòng cathode bằng nhau về độ lớn nên dòng thuần bằng 0. Giá trị chung đó là **mật độ dòng trao đổi** $j_0$. Nó trải rộng hơn 10 bậc: $j_0(\mathrm{H^+/H_2})$ trên Pt cỡ $10^{-3}$ A/cm², trên Hg chỉ $10^{-13}$ A/cm². Chính con số này, chứ không phải $E^\circ$, quyết định điện cực nào "chạy được".

## Quá thế đổi rào theo hàm mũ

Đặt quá thế $\eta$ làm hạ rào của một chiều và nâng rào của chiều kia, mỗi chiều nhận một phần $\alpha$ hay $(1-\alpha)$ của $F\eta$. Ghép lại được **phương trình Butler - Volmer**:

$$j=j_0\left[e^{(1-\alpha)F\eta/RT}-e^{-\alpha F\eta/RT}\right]$$

## Hai giới hạn cần nhớ

- **Quá thế nhỏ** ($|\eta|\ll RT/F\approx 25$ mV): khai triển hai hàm mũ tới bậc nhất,
$$j\approx \frac{j_0F}{RT}\eta$$
Điện cực xử sự như một **điện trở** — đó là điện trở chuyển điện tích $R_{ct}=RT/(j_0F)$.

- **Quá thế lớn** ($\eta \gg 25$ mV): một hàm mũ áp đảo, cho quan hệ **Tafel**
$$\eta = a + b\log|j|,\qquad b=\frac{2{,}303RT}{(1-\alpha)F}$$
Vẽ $\log|j|$ theo $\eta$ cho đường thẳng; tung độ gốc ngoại suy về $\eta=0$ cho $\log j_0$, hệ số góc cho $\alpha$.

## Vì sao điều này quan trọng

- **Điện phân**: điện thế phân huỷ thực tế = thế nhiệt động + quá thế anode + quá thế cathode + $IR$. Quá thế lớn của H$_2$ trên Hg là lí do điện phân nước muối trên catot thuỷ ngân cho Na chứ không cho H$_2$.
- **Ăn mòn**: tốc độ ăn mòn do $j_0$ và hệ số Tafel của cả hai phản ứng liên hợp quyết định.
- **Pin nhiên liệu**: tổn hao lớn nhất nằm ở quá thế khử oxi, vì $j_0$ của O$_2$ rất nhỏ.

## Điều kiện áp dụng

Butler - Volmer mô tả bước **chuyển điện tích**. Ở dòng lớn, tốc độ có thể bị chặn bởi **khuếch tán** chất phản ứng tới bề mặt: khi đó $j$ tiến tới dòng giới hạn và đồ thị Tafel bị cong. Ngoài ra $\alpha$ được coi là hằng số — giả thiết chỉ đúng trong khoảng quá thế không quá rộng.

**Lỗi thường gặp:**
- Dùng phương trình Tafel ở quá thế nhỏ — sai vì khi $|\eta|\lesssim 25$ mV hai số hạng mũ trong Butler - Volmer còn so sánh được, quan hệ là tuyến tính chứ không logarit; ép dữ liệu vào Tafel cho $j_0$ sai hàng bậc.
- Coi quá thế lớn thì dòng tăng vô hạn theo hàm mũ — sai vì khi dòng đủ lớn, chất phản ứng cạn kiệt ở bề mặt và tốc độ chuyển sang bị khống chế bởi khuếch tán; dòng bão hoà ở giá trị giới hạn.
- Nhầm mật độ dòng trao đổi với dòng đo được — sai vì $j_0$ là dòng của **mỗi chiều** tại cân bằng, nơi dòng thuần bằng 0; nó không đo trực tiếp được mà chỉ suy ra bằng ngoại suy Tafel.

<sub>`lesson.chemistry.dien-hoa-hoc.dong-hoc-dien-cuc-butler-volmer`</sub>

---

### 6. Ăn mòn điện hoá và các phương pháp bảo vệ
*Electrochemical corrosion and protection methods* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Giải thích được cơ chế pin ăn mòn cục bộ trên bề mặt kim loại
- Xác định được thế ăn mòn và dòng ăn mòn từ giao điểm của hai đường Tafel
- So sánh được cơ sở điện hoá của bảo vệ catot, bảo vệ anot và lớp phủ thụ động

## Ăn mòn là một pin ngắn mạch

Trên một mẩu sắt ẩm luôn có vùng hoạt động mạnh hơn (biên hạt, chỗ biến dạng, chỗ thiếu oxi) đóng vai anode:

$$\mathrm{Fe\to Fe^{2+}+2e^-}$$

và vùng khác đóng vai cathode, tiêu thụ electron:

$$\mathrm{O_2+2H_2O+4e^-\to 4OH^-}\quad(\text{môi trường trung tính, có oxi})$$
$$\mathrm{2H^+ + 2e^-\to H_2}\quad(\text{môi trường axit})$$

Hai vùng nối với nhau qua chính kim loại (mạch electron) và qua màng nước (mạch ion). Đó là một pin **ngắn mạch**: toàn bộ năng lượng biến thành nhiệt và thành sản phẩm ăn mòn.

## Thế hỗn hợp và dòng ăn mòn

Bề mặt không thể có hai thế cùng lúc, nên nó ổn định ở $E_{corr}$ — nơi

$$|j_a|=|j_c|\equiv j_{corr}$$

Vẽ hai đường Tafel (anode của Fe, cathode của O$_2$ hoặc H$^+$) trên cùng đồ thị $\log|j|$–$E$, **giao điểm** cho ngay $E_{corr}$ và $j_{corr}$. Từ $j_{corr}$, định luật Faraday cho tốc độ ăn mòn:

$$\text{tốc độ}=\frac{j_{corr}M}{nF\rho}$$

## Ba cách can thiệp, ba cơ chế khác nhau

1. **Bảo vệ catot bằng anode hi sinh**: nối Fe với Zn hoặc Mg có $E^\circ$ âm hơn. Kim loại hi sinh trở thành anode duy nhất, Fe bị đẩy về thế âm hơn $E_{corr}$ nên dòng anode của nó gần như tắt.
2. **Bảo vệ catot bằng dòng ngoài**: bơm electron vào công trình từ nguồn một chiều — dùng cho đường ống, tàu biển.
3. **Bảo vệ anot / thụ động hoá**: nâng thế lên **vùng thụ động**, nơi oxit bảo vệ hình thành. Đây là nguyên lí của thép không gỉ (lớp Cr$_2$O$_3$) và của nhôm (Al$_2$O$_3$). Nghịch lí: nhôm hoạt động hơn sắt về nhiệt động nhưng bền hơn nhiều nhờ oxit sít chặt, trong khi gỉ sắt xốp nên không bảo vệ.

## Khi biện pháp phản tác dụng

Nâng thế vào vùng thụ động chỉ an toàn nếu duy trì được; mất kiểm soát sẽ rơi vào **vùng quá thụ động** nơi oxit tan lại. Ion Cl$^-$ phá cục bộ màng thụ động gây **ăn mòn lỗ** — dòng tổng nhỏ nhưng tập trung vào diện tích bé nên thủng rất nhanh. Cuối cùng, mạ kẽm bảo vệ sắt ngay cả khi lớp mạ bị xước, còn mạ thiếc thì làm ăn mòn nhanh hơn khi xước, vì thiếc dương hơn sắt.

**Lỗi thường gặp:**
- Dự đoán khả năng ăn mòn chỉ bằng $E^\circ$ — sai vì tốc độ do động học quyết định; nhôm có $E^\circ$ rất âm nhưng bền trong không khí nhờ màng oxit thụ động làm $j_{corr}$ giảm nhiều bậc.
- Cho rằng $E_{corr}$ là thế cân bằng của cặp Fe$^{2+}$/Fe — sai vì đó là **thế hỗn hợp**, nằm giữa hai thế cân bằng của hai cặp liên hợp và được xác định bởi điều kiện cân bằng **dòng**, không phải cân bằng hoá học của một cặp.
- Nghĩ mạ thiếc và mạ kẽm bảo vệ sắt theo cùng một cơ chế — sai vì kẽm âm hơn sắt nên hi sinh bảo vệ ngay cả khi lớp mạ bị xước, còn thiếc dương hơn sắt nên khi xước sẽ biến sắt thành anode diện tích nhỏ và ăn mòn cục bộ mạnh hơn.

<sub>`lesson.chemistry.dien-hoa-hoc.an-mon-va-bao-ve`</sub>

---

### 7. Pin nhiên liệu: hiệu suất nhiệt động và các nguồn tổn hao
*Fuel cells: thermodynamic efficiency and sources of loss* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Tính được sức điện động lí thuyết và hiệu suất nhiệt động của pin nhiên liệu
- Phân tích được ba vùng tổn hao trên đường đặc trưng thế - dòng
- So sánh được các loại pin nhiên liệu theo chất điện li và nhiệt độ làm việc

## Vì sao không bị Carnot chặn

Động cơ nhiệt đốt hydro chuyển hoá năng thành nhiệt rồi mới thành công, nên bị chặn bởi $\eta_{Carnot}=1-T_l/T_n$. Pin nhiên liệu chuyển thẳng năng lượng Gibbs thành công điện, nên trần hiệu suất là

$$\eta_{td}=\frac{\Delta_r G}{\Delta_r H}$$

Với $\mathrm{H_2+\tfrac12 O_2\to H_2O(l)}$ ở 298 K: $\Delta_r H^\circ=-285{,}8$ kJ/mol, $\Delta_r G^\circ=-237{,}1$ kJ/mol, cho $\eta_{td}=83\,\%$ — cao hơn hẳn động cơ đốt trong. Sức điện động lí thuyết:

$$E^{\circ}=-\frac{\Delta_r G^{\circ}}{nF}=\frac{237\,100}{2\times96485}=1{,}23\ \mathrm{V}$$

**Chú ý nghịch lí**: vì $\Delta_r S<0$, $\eta_{td}$ **giảm** khi tăng nhiệt độ, ngược với động cơ nhiệt.

## Ba nguồn tổn hao thực

Điện áp thực luôn thấp hơn 1,23 V:

$$E = E_{eq} - \underbrace{|\eta_{act}|}_{\text{Tafel}} - \underbrace{jR_{\Omega}}_{\text{Ohm}} - \underbrace{|\eta_{conc}|}_{\text{vận chuyển}}$$

1. **Hoạt hoá**: chủ yếu ở cathode, vì $j_0$ của khử O$_2$ chỉ cỡ $10^{-9}$ A/cm² — nhỏ hơn oxi hoá H$_2$ tới sáu bậc. Đây là lí do phải dùng Pt và là điểm nghẽn công nghệ lớn nhất.
2. **Ohm**: điện trở màng dẫn proton và điện trở tiếp xúc; tuyến tính theo dòng.
3. **Vận chuyển chất**: ở dòng cao, oxi không khuếch tán kịp qua lớp khuếch tán khí, hoặc nước sinh ra làm ngập lỗ xốp.

Ngay ở mạch hở, điện áp thực chỉ khoảng 1,0 V do dòng rò và phản ứng phụ.

## Các họ pin nhiên liệu

- **PEMFC** (màng polymer, 60–80 °C): khởi động nhanh, dùng cho xe; cần H$_2$ rất sạch vì CO đầu độc Pt.
- **SOFC** (oxit rắn, 700–1000 °C): dùng được nhiên liệu hydrocarbon nhờ reforming nội bộ, không cần kim loại quý, nhưng khởi động chậm và vật liệu khắt khe.
- **AFC**, **PAFC**, **MCFC**: các trung gian về nhiệt độ và chất điện li.

## Đánh giá trung thực

Hiệu suất "83 %" là trần **nhiệt động** ở dòng bằng 0. Ở điểm công suất cực đại, điện áp thường chỉ 0,6–0,7 V, tức hiệu suất thực khoảng 45–55 %. Ngoài ra, nếu hydro được sản xuất bằng reforming khí thiên nhiên thì hiệu suất và phát thải phải tính trên toàn chuỗi, chứ không chỉ tính ở pin.

**Lỗi thường gặp:**
- Nói pin nhiên liệu 'không bị giới hạn nào' về hiệu suất — sai vì trần vẫn là $\Delta_r G/\Delta_r H$; chỉ khi $\Delta_r S \ge 0$ thì hiệu suất mới có thể đạt hoặc vượt 100 %, còn phản ứng H$_2$/O$_2$ có $\Delta_r S<0$ nên trần là 83 %.
- Cho rằng tăng nhiệt độ luôn cải thiện hiệu suất — sai với pin nhiên liệu H$_2$/O$_2$: vì $\Delta_r S<0$ nên $\Delta_r G$ bớt âm khi $T$ tăng, hiệu suất nhiệt động giảm; lợi ích của nhiệt độ cao nằm ở động học và ở khả năng tận dụng nhiệt thải, không ở trần nhiệt động.
- Dùng $\Delta_r H$ của nước ở thể hơi rồi so với sức điện động tính từ nước lỏng — sai vì hai trạng thái sản phẩm khác nhau một lượng enthalpy hoá hơi; phải thống nhất 'nhiệt trị cao' hay 'nhiệt trị thấp' trong suốt phép tính hiệu suất.

<sub>`lesson.chemistry.dien-hoa-hoc.pin-nhien-lieu`</sub>

---

## Unit 4: Hoá lượng tử

### 1. Nền tảng cơ học lượng tử cho hoá học
*Foundations of quantum mechanics for chemistry* · Đại học · intl-undergrad · 75 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được ý nghĩa của hàm sóng và điều kiện chuẩn hoá, đơn trị, liên tục
- Vận dụng được phương trình Schrödinger dừng như bài toán trị riêng của toán tử Hamilton
- Đánh giá được vai trò của nguyên lí biến phân và xấp xỉ Born - Oppenheimer trong hoá lượng tử

## Vì sao hoá học cần cơ học lượng tử

Vật lí cổ điển không giải thích nổi ba sự kiện cốt lõi của hoá học: nguyên tử bền, phổ vạch rời rạc, và liên kết cộng hoá trị. Cả ba đều bắt nguồn từ tính **lượng tử hoá** — hệ quả của việc buộc hàm sóng phải thoả điều kiện biên.

## Hàm sóng và phương trình trị riêng

Trạng thái được mô tả bởi $\psi$; ý nghĩa vật lí nằm ở $|\psi|^2$ (diễn giải Born). Điều kiện bắt buộc: đơn trị, liên tục, đạo hàm liên tục (trừ nơi thế phân kì), và bình phương khả tích để chuẩn hoá được:

$$\int |\psi|^2\,d\tau = 1$$

Trạng thái dừng thoả

$$\hat H\psi = E\psi,\qquad \hat H=-\frac{\hbar^2}{2m}\nabla^2+V$$

Chính việc đòi hỏi $\psi$ hữu hạn và triệt tiêu ở biên đã loại bỏ hầu hết giá trị $E$: **lượng tử hoá không phải giả thiết thêm vào, nó là hệ quả toán học**.

## Ba nguyên lí công cụ

- **Bất định**: $\Delta x\,\Delta p \ge \hbar/2$. Đây là lí do electron không rơi vào hạt nhân — thu hẹp $\Delta x$ làm động năng tăng vô hạn.
- **Biến phân**: mọi hàm thử cho $\langle E\rangle \ge E_0$. Toàn bộ hoá lượng tử tính toán (Hartree - Fock, CI, DFT) dựa trên việc tối ưu tham số để hạ $\langle E\rangle$.
- **Born - Oppenheimer**: cố định hạt nhân, giải cho electron ở từng cấu hình hạt nhân, thu được $E_{el}(R)$ — **mặt thế năng**. Không có xấp xỉ này thì các khái niệm "độ dài liên kết", "cấu dạng", "trạng thái chuyển tiếp" đều mất nghĩa.

## Khi các xấp xỉ hỏng

Born - Oppenheimer thất bại ở nơi hai mặt thế năng tiếp cận nhau — **giao cắt hình nón** — nơi chuyển động electron và hạt nhân bị ghép chặt. Đó chính là cơ chế các quá trình quang hoá siêu nhanh như sự nhìn của mắt (đồng phân hoá retinal) và cơ chế tự bảo vệ của DNA khỏi tia tử ngoại.

**Lỗi thường gặp:**
- Coi $\psi$ là 'mật độ electron' — sai vì $\psi$ là hàm phức, có thể âm và có nút; đại lượng có ý nghĩa xác suất là $|\psi|^2$, còn dấu của $\psi$ mới là thứ tạo ra giao thoa xây dựng hay phá huỷ trong liên kết hoá học.
- Nghĩ nguyên lí biến phân cho phép năng lượng tính được thấp hơn giá trị thật nếu hàm thử 'tốt' — sai vì bất đẳng thức là một chiều: mọi hàm thử đều cho giá trị **không nhỏ hơn** $E_0$; năng lượng tính ra thấp hơn thực nghiệm là dấu hiệu có lỗi (thường là sai chuẩn hoá hoặc thiếu số hạng trong Hamilton).
- Cho rằng xấp xỉ Born - Oppenheimer luôn dùng được vì hạt nhân nặng — sai ở vùng giao cắt hình nón, nơi hai mặt thế năng suy biến và ghép vibronic trở nên chi phối; các quá trình quang hoá nhanh nhất đều xảy ra chính tại đó.

<sub>`lesson.chemistry.hoa-luong-tu.nen-tang-co-hoc-luong-tu`</sub>

---

### 2. Hạt trong hộp thế và ứng dụng cho hệ liên hợp
*Particle in a box and applications to conjugated systems* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Giải được bài toán hạt trong hộp một chiều và giải thích nguồn gốc của lượng tử hoá
- Vận dụng được mô hình electron tự do để dự đoán bước sóng hấp thụ của polyene liên hợp
- Đánh giá được giới hạn của mô hình khi áp dụng cho phân tử thật

## Bài toán đơn giản nhất, bài học sâu nhất

Trong hộp, $V=0$ nên $\hat H\psi = -\frac{\hbar^2}{2m}\psi''=E\psi$, nghiệm tổng quát là $A\sin kx + B\cos kx$. Điều kiện biên $\psi(0)=0$ loại cosin; $\psi(L)=0$ buộc $kL=n\pi$. Kết quả:

$$\psi_n=\sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L},\qquad E_n=\frac{n^2h^2}{8mL^2},\ n=1,2,3,\dots$$

Ba bài học tổng quát rút ra ngay:
- **Lượng tử hoá đến từ điều kiện biên**, không phải từ giả thiết thêm.
- **$n=0$ bị cấm** vì cho $\psi\equiv 0$; do đó tồn tại năng lượng điểm không $E_1>0$.
- **Khoảng cách mức** $\Delta E = (2n+1)h^2/(8mL^2)$ tỉ lệ nghịch $L^2$: nhốt càng chặt thì mức càng thưa. Đây là nguyên lí của **chấm lượng tử** — cùng một chất, hạt nhỏ phát ánh sáng xanh, hạt lớn phát đỏ.

## Áp dụng cho polyene

Với polyene liên hợp có $N$ electron $\pi$, coi chúng chạy tự do dọc mạch dài $L$. Nguyên lí Pauli cho mỗi mức chứa 2 electron, nên HOMO là mức $n=N/2$ và LUMO là $n=N/2+1$:

$$\Delta E = \frac{h^2}{8m_eL^2}\left[(N/2+1)^2-(N/2)^2\right]=\frac{h^2(N+1)}{8m_eL^2}$$

Vì $L$ tỉ lệ với $N$, ta có $\Delta E \propto 1/N$: **mạch liên hợp càng dài, hấp thụ càng dịch về phía đỏ**. Đây là lí do $\beta$-carotene (11 nối đôi liên hợp) có màu cam, còn ethylene thì không màu.

## Hộp nhiều chiều và suy biến

Trong hộp ba chiều, $E=\dfrac{h^2}{8m}\left(\dfrac{n_x^2}{L_x^2}+\dfrac{n_y^2}{L_y^2}+\dfrac{n_z^2}{L_z^2}\right)$. Với hộp lập phương, các trạng thái (2,1,1), (1,2,1), (1,1,2) suy biến bậc 3. Hạ đối xứng (kéo dài một cạnh) làm tách mức — đó chính là mầm mống của hiệu ứng Jahn - Teller trong phức chất.

## Đừng kì vọng quá nhiều

Mô hình bỏ qua: thế tuần hoàn do hạt nhân, tương tác electron - electron, và sự rò hàm sóng ra ngoài đầu mạch. Nó cho xu hướng đúng và bậc độ lớn hợp lí, nhưng sai số bước sóng có thể tới vài chục nanomet. Muốn định lượng phải dùng Hückel hoặc phương pháp tự hợp.

**Lỗi thường gặp:**
- Cho $n=0$ là trạng thái cơ bản — sai vì $n=0$ cho $\psi\equiv 0$, tức không có hạt; trạng thái thấp nhất là $n=1$ và năng lượng điểm không khác 0 là hệ quả bắt buộc của nguyên lí bất định.
- Dùng $\Delta E = h^2/(8mL^2)$ cho mọi chuyển dời — sai vì khoảng cách hai mức kề nhau phụ thuộc $n$: $\Delta E=(2n+1)h^2/(8mL^2)$, nên mức càng cao thì khoảng cách càng lớn.
- Đếm số electron $\pi$ bằng số nguyên tử carbon trong mạch — sai với hệ mang điện tích hoặc dị nguyên tử; ví dụ cation allyl có 3 carbon nhưng chỉ 2 electron $\pi$, nên HOMO nằm ở $n=1$ chứ không phải $n=2$.

<sub>`lesson.chemistry.hoa-luong-tu.hat-trong-hop-va-he-lien-hop`</sub>

---

### 3. Dao động tử điều hoà và quay tử cứng
*The harmonic oscillator and the rigid rotor* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Viết được phổ năng lượng của dao động tử điều hoà và giải thích năng lượng điểm không
- Tính được tần số dao động từ hằng số lực và khối lượng rút gọn
- Xác định được mức năng lượng quay và độ suy biến của quay tử cứng thẳng

## Vì sao hai mô hình này là xương sống của phổ học

Mọi cực tiểu của đường thế năng đều xấp xỉ parabol nếu ta ở đủ gần đáy, và mọi phân tử hai nguyên tử đều quay được. Hai bài toán này vì thế mô tả trực tiếp phổ hồng ngoại và phổ vi sóng.

## Dao động tử điều hoà

Với $V=\tfrac12 kx^2$, nghiệm chính xác cho

$$E_v=\left(v+\tfrac12\right)\hbar\omega,\qquad \omega=\sqrt{\frac{k}{\mu}},\ v=0,1,2,\dots$$

Ba đặc điểm:
- **Cách đều**: mọi khoảng cách mức bằng $\hbar\omega$ — nên phổ hồng ngoại lí tưởng chỉ có một vạch.
- **Năng lượng điểm không** $\tfrac12\hbar\omega \neq 0$: liên kết không bao giờ "đứng yên", ngay cả ở 0 K.
- **Tần số phụ thuộc $\mu$**: thay H bằng D làm $\mu$ tăng gần gấp đôi, nên $\tilde\nu$ giảm theo hệ số $1/\sqrt2$. Đây là cơ sở của hiệu ứng đồng vị trong phổ và trong động học.

Chú ý phân biệt: $k$ đo **độ cứng**, còn năng lượng phân li đo **độ bền**. Hai đại lượng thường tương quan nhưng không đồng nhất.

## Quay tử cứng

$$E_J = \frac{\hbar^2}{2I}J(J+1)=hcBJ(J+1),\qquad I=\mu R^2$$

Mỗi mức $J$ suy biến $2J+1$ lần (các giá trị $M_J$). Khoảng cách hai mức kề nhau là $2B(J+1)$ — **tăng dần**, nên phổ quay là dãy vạch cách đều $2B$ khi áp quy tắc lọc lựa $\Delta J=\pm 1$.

Vì $B\propto 1/(\mu R^2)$, đo một dãy vạch phổ vi sóng cho độ dài liên kết với độ chính xác cỡ $10^{-4}$ Å — chính xác hơn hầu hết phương pháp khác.

## Dân số các mức

Ở nhiệt độ phòng, $\hbar\omega/k_BT \gg 1$ cho dao động (hầu hết phân tử ở $v=0$) nhưng $hcB/k_BT \ll 1$ cho quay (nhiều mức $J$ được chiếm). Kể cả suy biến $2J+1$, dân số cực đại nằm ở

$$J_{\max}\approx\sqrt{\frac{k_BT}{2hcB}}-\tfrac12$$

Đó là lí do phổ quay và nhánh P, R của phổ dao động - quay có **bao hình** đặc trưng chứ không giảm đơn điệu.

## Giới hạn

Thế thật không phải parabol: ở $v$ cao mức xích lại gần nhau và phân tử phân li — phải dùng thế Morse. Quay tử cũng không cứng: quay nhanh làm liên kết dãn ra, sinh hiệu chỉnh biến dạng li tâm $-D_JJ^2(J+1)^2$.

**Lỗi thường gặp:**
- Dùng khối lượng của một nguyên tử thay vì khối lượng rút gọn — sai vì cả hai hạt nhân đều chuyển động quanh khối tâm; với H–Cl thì $\mu$ gần bằng khối lượng H nên sai số nhỏ, nhưng với O–O hay C–C thì sai gần hai lần.
- Cho rằng thay đồng vị làm đổi hằng số lực — sai vì trong xấp xỉ Born - Oppenheimer, mặt thế năng chỉ do electron và điện tích hạt nhân quyết định; $k$ giữ nguyên, chỉ $\mu$ và do đó tần số thay đổi.
- Đồng nhất hằng số lực với năng lượng liên kết — sai vì $k$ là độ cong của thế tại đáy giếng, còn $D_e$ là độ sâu giếng; một liên kết có thể rất cứng ở đáy nhưng phân li ở năng lượng không quá lớn.

<sub>`lesson.chemistry.hoa-luong-tu.dao-dong-tu-va-quay-tu`</sub>

---

### 4. Nguyên tử nhiều electron và phương pháp trường tự hợp
*Many-electron atoms and the self-consistent field method* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao bài toán nhiều electron không giải chính xác được và cần xấp xỉ obitan
- Trình bày được ý tưởng của định thức Slater và của vòng lặp trường tự hợp
- Vận dụng được định lí Koopmans và khái niệm năng lượng tương quan để đánh giá kết quả

## Rào chắn: số hạng $1/r_{12}$

Hamilton của He đã chứa $\dfrac{e^2}{4\pi\varepsilon_0 r_{12}}$ khiến biến không tách được. Không có nghiệm giải tích cho bất kì nguyên tử nào từ He trở đi. Hoá lượng tử vì thế là nghệ thuật xấp xỉ có kiểm soát.

## Xấp xỉ obitan và phản đối xứng

Bước một: giả thiết mỗi electron có obitan riêng, hàm sóng là tích các spin-obitan. Nhưng tích đơn thuần vi phạm nguyên lí Pauli. Bước hai: viết dưới dạng **định thức Slater**

$$\Psi=\frac{1}{\sqrt{N!}}\det\left|\chi_1(1)\ \chi_2(2)\ \cdots\ \chi_N(N)\right|$$

Định thức đổi dấu khi hoán vị hai hàng (hai electron) và triệt tiêu nếu hai cột trùng nhau — nguyên lí loại trừ Pauli trở thành **tính chất toán học**, không cần phát biểu thêm.

## Vòng lặp tự hợp

Thay $1/r_{12}$ bằng thế trung bình do mật độ các electron khác tạo ra, ta được phương trình Hartree - Fock $\hat f\chi_i=\varepsilon_i\chi_i$. Nhưng $\hat f$ lại phụ thuộc chính các $\chi$ chưa biết. Cách giải: đoán bộ obitan → dựng $\hat f$ → giải → thu bộ obitan mới → lặp cho tới khi hội tụ.

Toán tử Fock chứa cả tích phân **Coulomb** $J$ (đẩy cổ điển) và tích phân **trao đổi** $K$ (thuần lượng tử, chỉ giữa electron cùng spin). Chính $K$ giải thích quy tắc Hund thứ nhất: electron cùng spin tránh nhau nên đẩy nhau yếu hơn.

Lưu ý quan trọng: $E_{HF}\ne \sum\varepsilon_i$, vì cộng như vậy sẽ đếm hai lần tương tác electron - electron.

## Đọc kết quả

- **Koopmans**: $I_1\approx -\varepsilon_{HOMO}$. Xấp xỉ này gặp may nhờ hai sai số triệt tiêu nhau (bỏ qua tái tổ chức obitan làm ước lượng cao, bỏ qua tương quan làm ước lượng thấp).
- **Năng lượng tương quan**: $E_{corr}=E_{exact}-E_{HF}$, luôn âm, cỡ 1 % năng lượng toàn phần — nhưng con số đó có thể lớn hơn cả năng lượng liên kết! Đó là lí do Hartree - Fock thuần tuý dự đoán năng lượng phân li rất tệ, và vì sao cần các phương pháp hậu Hartree - Fock (MP2, CI, coupled cluster) hoặc DFT.

## Che chắn và quy tắc Slater

Ở mức định tính, hiệu ứng nhiều electron được gói vào điện tích hạt nhân hiệu dụng $Z_{eff}=Z-\sigma$, với $\sigma$ tính bằng quy tắc Slater. Mô hình thô này vẫn giải thích đúng xu hướng bán kính nguyên tử và năng lượng ion hoá trong bảng tuần hoàn.

**Lỗi thường gặp:**
- Coi năng lượng toàn phần Hartree - Fock bằng tổng các năng lượng obitan — sai vì mỗi $\varepsilon_i$ đã chứa tương tác của electron $i$ với mọi electron khác, nên cộng tất cả sẽ **đếm hai lần** phần đẩy electron - electron; phải trừ đi tổng $J-K$ tương ứng.
- Nghĩ năng lượng tương quan nhỏ nên bỏ qua được — sai vì tuy chỉ chiếm khoảng 1 % năng lượng toàn phần, giá trị tuyệt đối của nó thường vượt cả năng lượng liên kết; đó là lí do Hartree - Fock dự đoán sai nghiêm trọng năng lượng phân li.
- Dùng định lí Koopmans cho ái lực electron với cùng độ tin cậy như cho năng lượng ion hoá — sai vì với ái lực electron hai sai số (tái tổ chức và tương quan) **cộng dồn** thay vì triệt tiêu, nên sai số lớn hơn nhiều.

<sub>`lesson.chemistry.hoa-luong-tu.nguyen-tu-nhieu-electron-hartree-fock`</sub>

---

### 5. Số hạng nguyên tử và ghép momen động lượng
*Atomic term symbols and angular momentum coupling* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Xây dựng được kí hiệu số hạng $^{2S+1}L_J$ cho một cấu hình electron
- Vận dụng được ba quy tắc Hund để xác định số hạng cơ bản
- Giải thích được nguồn gốc và độ lớn của tách spin - obitan

## Vì sao cấu hình electron chưa đủ

Cấu hình $2p^2$ của carbon không xác định một trạng thái duy nhất: có 15 vi trạng thái, phân thành ba số hạng $^3P$, $^1D$, $^1S$ với năng lượng chênh nhau vài eV. Muốn nói về phổ nguyên tử, về từ tính, về quy tắc lọc lựa, ta phải làm việc với **số hạng**, không phải cấu hình.

## Đếm vi trạng thái

Với $n$ electron trên phân lớp có $g$ spin-obitan:

$$W=\binom{g}{n}$$

Với $2p^2$: $g=6$, $n=2$, $W=15$. Lớp đầy có $W=1$ và luôn cho $^1S_0$ — nên **chỉ cần xét các phân lớp chưa đầy**.

## Xây dựng số hạng

$L$ lấy các giá trị $|\ell_1-\ell_2|,\dots,\ell_1+\ell_2$ và kí hiệu bằng chữ S, P, D, F, G ứng với $L=0,1,2,3,4$. $S$ lấy $|s_1-s_2|,\dots$; độ bội là $2S+1$. Cuối cùng $J$ chạy từ $|L-S|$ tới $L+S$.

Với electron **tương đương** (cùng $n$, cùng $\ell$), nguyên lí Pauli loại bớt tổ hợp: $p^2$ chỉ cho $^3P$, $^1D$, $^1S$ (tổng $9+5+1=15$ vi trạng thái, khớp).

## Ba quy tắc Hund

1. Số hạng có **$S$ lớn nhất** nằm thấp nhất (electron cùng spin tránh nhau nhờ tương tác trao đổi).
2. Trong cùng $S$, số hạng có **$L$ lớn nhất** nằm thấp nhất.
3. Nếu phân lớp **chưa đầy một nửa**, mức có $J$ **nhỏ nhất** thấp nhất (đa tuyến thường); nếu **quá nửa**, mức có $J$ **lớn nhất** thấp nhất (đa tuyến nghịch).

Với C ($2p^2$, chưa nửa): $^3P_0$. Với O ($2p^4$, quá nửa): $^3P_2$.

**Cảnh báo**: quy tắc Hund chỉ đáng tin cho **số hạng cơ bản**, không dùng để sắp thứ tự các số hạng kích thích.

## Tách spin - obitan

$$E_{so}=\frac{A}{2}\left[J(J+1)-L(L+1)-S(S+1)\right]$$

Hằng số $A$ tăng rất nhanh theo $Z$ (gần như $Z^4$): với C tách chỉ vài chục cm$^{-1}$, với Pb tới hàng nghìn cm$^{-1}$. Khi $A$ trở nên lớn hơn tương tác đẩy electron, sơ đồ Russell - Saunders sụp đổ và phải dùng ghép $jj$ — đó là tình huống của các nguyên tố nặng, và là một lí do khiến hoá học của Pb, Tl khác biệt so với đồng nhóm nhẹ hơn.

**Lỗi thường gặp:**
- Ghép tự do $L$ và $S$ cho electron tương đương — sai vì nguyên lí Pauli cấm nhiều tổ hợp; với $p^2$ cách làm tự do cho cả $^3D$ và $^1P$ vốn không tồn tại, và tổng vi trạng thái sẽ vượt quá 15.
- Dùng quy tắc Hund để sắp thứ tự mọi số hạng kích thích — sai vì ba quy tắc chỉ được kiểm chứng cho số hạng **cơ bản**; thứ tự các mức kích thích phải lấy từ tính toán hoặc từ phổ.
- Áp dụng ghép Russell - Saunders cho nguyên tố nặng — sai vì khi tương tác spin - obitan (tăng gần như $Z^4$) vượt tương tác đẩy electron, $L$ và $S$ không còn là số lượng tử tốt; phải dùng ghép $jj$.
- Quên rằng phân lớp đầy luôn cho $^1S_0$ — dẫn tới việc mất công liệt kê số hạng cho lõi kín; chỉ cần xét phân lớp chưa đầy là đủ.

<sub>`lesson.chemistry.hoa-luong-tu.so-hang-nguyen-tu`</sub>

---

### 6. Liên kết hoá học theo thuyết VB và thuyết MO
*Chemical bonding: valence bond and molecular orbital theories* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- So sánh được cách xây dựng hàm sóng liên kết theo thuyết VB và theo thuyết MO
- Xác định được giản đồ MO của phân tử hai nguyên tử đồng hạch và bậc liên kết tương ứng
- Giải thích được ưu, nhược điểm của mỗi thuyết qua các ví dụ then chốt như O$_2$ và H$_2$ ở khoảng cách lớn

## Hai lối vào cùng một hiện tượng

Với H$_2$, thuyết **VB** viết hàm sóng như hai electron ghép đôi trên hai nguyên tử:

$$\Psi_{VB}\propto \phi_A(1)\phi_B(2)+\phi_A(2)\phi_B(1)$$

còn thuyết **MO** đưa mỗi electron vào một obitan trải khắp phân tử:

$$\psi_{\pm}=N(\phi_A\pm\phi_B),\qquad \Psi_{MO}=\psi_+(1)\psi_+(2)$$

Khai triển $\Psi_{MO}$ cho thấy nó chứa cả số hạng cộng hoá trị lẫn số hạng **ion** ($\mathrm{H^+H^-}$) với trọng số bằng nhau — quá nhiều tính ion. Đó là lí do MO đơn giản dự đoán H$_2$ ở khoảng cách lớn phân li thành ion, sai về mặt vật lí. Ngược lại, VB thiếu tính ion. Cả hai hội tụ về cùng đáp số khi bổ sung: VB thêm cấu trúc ion, MO thêm tương tác cấu hình.

## Dựng giản đồ MO

Giải bài toán biến phân với hai obitan cho **định thức thế kỉ**

$$\begin{vmatrix}\alpha-E & \beta-ES\\ \beta-ES & \alpha-E\end{vmatrix}=0 \;\Rightarrow\; E_{\pm}=\frac{\alpha\pm\beta}{1\pm S}$$

Vì $S>0$, mức phản liên kết bị đẩy lên **nhiều hơn** mức liên kết bị hạ xuống — hệ quả then chốt: He$_2$ không tồn tại dù có số electron liên kết bằng số phản liên kết.

Với chu kì 2, thứ tự MO là $\sigma_{2s}<\sigma^*_{2s}<\pi_{2p}<\sigma_{2p}<\pi^*_{2p}<\sigma^*_{2p}$ đối với B$_2$ đến N$_2$ (do trộn $s$–$p$), nhưng $\sigma_{2p}$ tụt xuống dưới $\pi_{2p}$ ở O$_2$ và F$_2$.

## Bài kiểm tra quyết định: O$_2$

Cấu hình MO của O$_2$ là $\dots(\pi^*_{2p})^2$ với hai electron **độc thân song song** trên hai obitan $\pi^*$ suy biến. O$_2$ do đó **thuận từ** — điều mà công thức Lewis O=O không hề gợi ý và thuyết VB sơ cấp không giải thích được. Đây là thắng lợi kinh điển của thuyết MO.

Bậc liên kết: $\tfrac12(8-4)=2$, phù hợp với $d(\mathrm{O-O})=121$ pm. Với O$_2^+$ bậc lên 2,5 và liên kết ngắn lại; với O$_2^{2-}$ bậc còn 1 và dài ra — xu hướng dự đoán chính xác.

## Chọn thuyết nào

VB gần với ngôn ngữ hoá học (liên kết định cư, lai hoá, cộng hưởng) nên tiện cho lập luận cơ chế. MO xử lí tốt hệ giải toả, trạng thái kích thích, tính từ, và là nền của mọi phần mềm tính toán. Người làm hoá học thành thạo dùng **cả hai**, tuỳ câu hỏi.

**Lỗi thường gặp:**
- Dùng thứ tự MO của N$_2$ cho O$_2$ và F$_2$ — sai vì hiệu ứng trộn $s$–$p$ giảm khi $Z$ tăng, nên từ O trở đi $\sigma_{2p}$ nằm dưới $\pi_{2p}$; dùng nhầm sẽ dự đoán sai tính từ của các phân tử này.
- Cho rằng obitan phản liên kết chỉ 'huỷ' đúng một obitan liên kết — sai vì do tích phân xen phủ $S>0$, mức phản liên kết bị đẩy lên nhiều hơn mức liên kết bị hạ xuống; đó là lí do He$_2$ không bền dù bậc liên kết bằng 0 chứ không âm.
- Kết luận thuyết VB sai vì không giải thích được tính thuận từ của O$_2$ — nói quá; VB sơ cấp thất bại, nhưng VB hiện đại có cộng hưởng và cấu hình mở vẫn mô tả đúng, và VB lại vượt trội MO đơn giản ở giới hạn phân li của H$_2$.

<sub>`lesson.chemistry.hoa-luong-tu.lien-ket-vb-va-mo`</sub>

---

### 7. Phương pháp Hückel cho hệ pi liên hợp
*Huckel molecular orbital method for pi systems* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Trình bày được các giả thiết của thuyết Hückel và lập được định thức thế kỉ
- Tính được mức năng lượng, mật độ electron pi và bậc liên kết pi cho hệ mạch hở và hệ vòng
- Vận dụng được giản đồ Frost và quy tắc $4n+2$ để đánh giá tính thơm

## Đơn giản hoá triệt để để đổi lấy hiểu biết

Hückel giữ lại đúng một điều: **topo của mạng liên hợp**. Mọi carbon giống nhau ($\alpha$), chỉ nguyên tử kề nhau tương tác ($\beta$), xen phủ bỏ qua ($S=0$). Bài toán MO thành bài toán trị riêng của **ma trận kề** của đồ thị phân tử. Kết quả tuy thô nhưng chứa những kết luận mà tính toán tinh vi cũng khẳng định.

## Mạch hở

Với polyene mạch hở $N$ carbon, nghiệm giải tích:

$$E_k=\alpha+2\beta\cos\frac{k\pi}{N+1},\qquad k=1,\dots,N$$

Với butadiene ($N=4$): $E=\alpha+1{,}618\beta$, $\alpha+0{,}618\beta$, $\alpha-0{,}618\beta$, $\alpha-1{,}618\beta$. Bốn electron $\pi$ vào hai mức thấp cho $E_\pi=4\alpha+4{,}472\beta$. So với hai liên kết đôi cô lập ($4\alpha+4\beta$), **năng lượng giải toả** là $0{,}472\beta$ — dương về độ bền, giải thích vì sao dien liên hợp bền hơn dien cô lập.

## Hệ vòng và giản đồ Frost

Với vòng $N$ carbon:

$$E_k=\alpha+2\beta\cos\frac{2k\pi}{N},\qquad k=0,\pm1,\dots$$

Cách dựng hình: vẽ đa giác đều $N$ cạnh nội tiếp đường tròn bán kính $2|\beta|$, **một đỉnh chạm đáy**; chiều cao mỗi đỉnh là một mức năng lượng. Ngay lập tức thấy: mức thấp nhất luôn không suy biến, các mức trên suy biến từng cặp.

Hệ quả: lấp đầy trọn vẹn các mức liên kết cần $2+4n$ electron — chính là **quy tắc $4n+2$**. Benzene ($6\pi$) có vỏ đóng, năng lượng giải toả $2\beta$; cyclobutadiene ($4\pi$) có hai electron độc thân trên cặp mức không liên kết, **phản thơm**, và thực tế bị biến dạng thành hình chữ nhật để thoát khỏi suy biến.

## Đại lượng rút ra được

- **Mật độ electron $\pi$** trên nguyên tử $r$: $q_r=\sum_i n_i c_{ir}^2$; điện tích $\pi$ là $1-q_r$, dùng dự đoán vị trí bị tấn công ái điện tử hay ái nhân.
- **Bậc liên kết $\pi$**: $p_{rs}=\sum_i n_i c_{ir}c_{is}$, tương quan tốt với độ dài liên kết đo bằng nhiễu xạ.
- **Khe HOMO - LUMO** cho ước lượng bước sóng hấp thụ và cho biết hệ dễ bị oxi hoá hay khử tới đâu.

## Biết rõ nó không làm được gì

Hückel không có tương tác electron - electron tường minh, nên không phân biệt được trạng thái singlet và triplet, không cho năng lượng tuyệt đối, và không xử lí được hệ không phẳng. Với dị nguyên tử phải đưa vào tham số $\alpha_X=\alpha+h_X\beta$ mang tính kinh nghiệm. Giá trị thật của nó nằm ở việc cho **quy luật đối xứng và topo** — điều tồn tại bền vững qua mọi mức lí thuyết.

**Lỗi thường gặp:**
- Quên rằng $\beta$ là số **âm** nên xếp mức năng lượng ngược — dẫn tới điền electron vào obitan phản liên kết; luôn kiểm tra: mức thấp nhất phải là $\alpha+2\beta$ vì $\beta<0$ làm nó nằm dưới $\alpha$.
- Lấy mốc so sánh là các nguyên tử carbon cô lập khi tính năng lượng giải toả — sai vì định nghĩa đòi hỏi mốc là hệ có cùng số liên kết đôi nhưng **định cư**; đổi mốc sẽ cho con số vô nghĩa để so sánh giữa các phân tử.
- Áp dụng quy tắc $4n+2$ cho hệ không phẳng hoặc không liên hợp toàn vòng — sai vì quy tắc giả thiết mọi obitan $p$ song song và xen phủ liên tục; cyclooctatetraene có $8\pi$ nhưng không phản thơm vì nó gấp thành hình 'bồn tắm' và mất tính liên hợp vòng.
- Dùng Hückel để so sánh năng lượng tuyệt đối giữa hai phân tử khác nhau — sai vì $\alpha$ và $\beta$ là tham số kinh nghiệm không có giá trị tuyệt đối; chỉ các hiệu năng lượng trong cùng một họ hệ liên hợp mới có ý nghĩa.

<sub>`lesson.chemistry.hoa-luong-tu.phuong-phap-huckel`</sub>

---

### 8. Lí thuyết phiếm hàm mật độ ở mức khái niệm
*Density functional theory at the conceptual level* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Phát biểu được hai định lí Hohenberg - Kohn và ý nghĩa của việc dùng mật độ thay cho hàm sóng
- Giải thích được vai trò của hệ Kohn - Sham và của phiếm hàm trao đổi - tương quan
- Đánh giá được điểm mạnh và các thất bại có hệ thống của DFT trong thực hành hoá học

## Đổi biến để thoát khỏi bùng nổ chiều

Hàm sóng của $N$ electron phụ thuộc $3N$ biến không gian: với một phân tử nhỏ đã là hàng chục biến, không thể lưu trữ nổi. Mật độ electron $\rho(\mathbf r)$ chỉ phụ thuộc **ba** biến. Hohenberg và Kohn chứng minh rằng chừng đó là đủ: mật độ trạng thái cơ bản xác định duy nhất thế ngoài, do đó xác định Hamilton, do đó xác định mọi thứ.

Định lí thứ hai cho công cụ tính: năng lượng là phiếm hàm $E[\rho]$ và cực tiểu của nó ứng với mật độ đúng — tức có một nguyên lí biến phân viết bằng $\rho$.

## Vấn đề: động năng

Viết $E[\rho]$ tường minh thất bại ở số hạng động năng (các mô hình Thomas - Fermi cho sai số lớn tới mức không dự đoán được liên kết hoá học). Kohn và Sham giải bằng một mẹo: xét một hệ **electron không tương tác** có cùng mật độ. Với hệ đó, động năng tính chính xác từ các obitan. Phần sai khác bị dồn vào một số hạng duy nhất:

$$E[\rho]=T_s[\rho]+E_{ne}[\rho]+J[\rho]+E_{xc}[\rho]$$

Phương trình Kohn - Sham có dạng giống Hartree - Fock và cũng giải bằng vòng lặp tự hợp.

## Điểm mấu chốt: $E_{xc}$ không biết chính xác

Toàn bộ nghệ thuật của DFT nằm ở việc xấp xỉ $E_{xc}$:
- **LDA**: lấy mật độ tại mỗi điểm như khí electron đồng nhất.
- **GGA** (PBE, BLYP): thêm gradient của mật độ.
- **Lai** (B3LYP, PBE0): trộn một phần trao đổi Hartree - Fock chính xác.
- **Có hiệu chỉnh phân tán** (D3, D4): bù tương tác van der Waals.

Vì $E_{xc}$ là xấp xỉ, DFT **không có tính biến phân theo bậc thang**: không đảm bảo phiếm hàm phức tạp hơn luôn cho kết quả tốt hơn, và năng lượng tính được có thể thấp hơn giá trị thật.

## Vì sao DFT thống trị hoá học tính toán

Chi phí tính toán tăng theo $N^3$–$N^4$, so với $N^7$ của coupled cluster, trong khi độ chính xác cho năng lượng phản ứng và hình học thường đủ dùng. Đó là lí do hầu hết bài báo hoá học hiện nay có một mục tính toán DFT.

## Bốn thất bại có hệ thống cần biết

1. **Sai số tự tương tác**: electron tự đẩy chính nó, làm rào phản ứng bị hạ và trạng thái chuyển điện tích bị mô tả sai.
2. **Tương tác phân tán** không có trong LDA/GGA thuần — bắt buộc thêm hiệu chỉnh cho hệ có xếp chồng $\pi$, protein, tinh thể phân tử.
3. **Khe HOMO - LUMO Kohn - Sham** không phải khe quang phổ; phải dùng TD-DFT và cả nó cũng sai cho trạng thái chuyển điện tích.
4. **Hệ tương quan mạnh** (kim loại chuyển tiếp nhiều cấu hình, phá vỡ liên kết) nằm ngoài tầm của DFT một định thức.

Quy tắc thực hành: luôn nêu rõ phiếm hàm và bộ hàm cơ sở, và đối chiếu với ít nhất một phiếm hàm khác.

**Lỗi thường gặp:**
- Coi obitan Kohn - Sham và trị riêng của chúng như obitan thật với ý nghĩa vật lí đầy đủ — sai vì chúng thuộc hệ **giả định không tương tác** dựng ra chỉ để tái tạo mật độ; riêng $\varepsilon_{HOMO}$ có ý nghĩa (bằng trị đối của năng lượng ion hoá với phiếm hàm chính xác), còn khe HOMO - LUMO Kohn - Sham không phải khe quang phổ.
- Cho rằng DFT là phương pháp biến phân nên năng lượng tính được luôn là chặn trên — sai vì nguyên lí biến phân chỉ đúng với phiếm hàm $E_{xc}$ **chính xác**; với phiếm hàm xấp xỉ, năng lượng có thể nằm dưới giá trị thật.
- Dùng GGA thuần cho hệ có xếp chồng $\pi$ hoặc hấp phụ vật lí mà không thêm hiệu chỉnh phân tán — sai vì tương tác London là hiệu ứng tương quan tầm xa, hoàn toàn vắng mặt trong các phiếm hàm dựa trên mật độ cục bộ.
- Chọn phiếm hàm chỉ vì nó phổ biến (B3LYP) mà không kiểm tra loại bài toán — sai vì mỗi phiếm hàm được tham số hoá cho những tập dữ liệu khác nhau; rào phản ứng, năng lượng liên kết kim loại chuyển tiếp và phổ kích thích đòi hỏi những lựa chọn khác nhau.

<sub>`lesson.chemistry.hoa-luong-tu.li-thuyet-phiem-ham-mat-do`</sub>

---

## Unit 5: Phổ học phân tử

### 1. Tương tác bức xạ - vật chất và quy tắc lọc lựa
*Radiation-matter interaction and selection rules* · Đại học · intl-undergrad · 60 phút · nang-cao

**Mục tiêu:**
- Vận dụng được các hệ thức chuyển đổi giữa năng lượng, tần số, bước sóng và số sóng
- Giải thích được nguồn gốc của quy tắc lọc lựa qua momen chuyển dời lưỡng cực
- Đánh giá được ảnh hưởng của phân bố Boltzmann và của thời gian sống tới cường độ và độ rộng vạch phổ

## Một thang, nhiều đơn vị

Phổ học dùng song song bốn đại lượng liên hệ với nhau:

$$E=h\nu=\frac{hc}{\lambda}=hc\tilde\nu$$

Số sóng $\tilde\nu=1/\lambda$ (cm$^{-1}$) được ưa dùng vì nó tỉ lệ thuận với năng lượng. Vài mốc cần thuộc: 1 eV $\approx$ 8065 cm$^{-1}$ $\approx$ 96,5 kJ/mol; $k_BT$ ở 298 K $\approx$ 207 cm$^{-1}$.

Mốc cuối rất hữu ích: nó cho biết ngay mức nào bị chiếm đáng kể ở nhiệt độ phòng. Chuyển động **quay** có khoảng cách mức vài cm$^{-1}$ nên nhiều mức được chiếm; **dao động** cỡ 1000–3000 cm$^{-1}$ nên hầu hết phân tử ở $v=0$; **điện tử** cỡ 20 000–50 000 cm$^{-1}$ nên chỉ trạng thái cơ bản được chiếm.

## Vì sao có chuyển dời bị cấm

Xác suất chuyển dời do momen chuyển dời quyết định:

$$\boldsymbol\mu_{fi}=\int \psi_f^*\,\hat{\boldsymbol\mu}\,\psi_i\,d\tau$$

Tích phân này bằng 0 vì lí do **đối xứng** nếu tích $\psi_f^*\,\hat\mu\,\psi_i$ là hàm lẻ. Từ đó sinh ra mọi quy tắc lọc lựa cụ thể:
- Phổ quay: phân tử phải có momen lưỡng cực vĩnh cửu; $\Delta J=\pm 1$.
- Phổ dao động: momen lưỡng cực phải **biến thiên** theo toạ độ dao động; $\Delta v=\pm 1$.
- Phổ điện tử: quy tắc spin $\Delta S=0$ và quy tắc Laporte (chuyển dời $g\leftrightarrow g$ bị cấm ở phân tử có tâm đối xứng).

"Cấm" ở đây nghĩa là **cường độ rất yếu**, không phải bằng 0 tuyệt đối: dao động phá vỡ đối xứng, ghép spin - obitan trộn các trạng thái, nên các vạch cấm vẫn xuất hiện mờ nhạt. Chính điều đó cho ta lân quang và phổ d–d của phức bát diện.

## Cường độ và độ rộng

Cường độ hấp thụ đo bằng $\varepsilon$ hoặc bằng hệ số hấp thụ mol tích phân, và tương quan với **lực dao động tử** — đại lượng không thứ nguyên so sánh chuyển dời thật với một dao động tử điện tử cổ điển lí tưởng.

Độ rộng vạch có ba nguồn: **tự nhiên** (thời gian sống), **Doppler** (chuyển động nhiệt, chi phối trong pha khí loãng), và **va chạm** (áp suất cao, pha ngưng tụ). Với trạng thái sống rất ngắn, $\delta\tilde\nu\ \mathrm{(cm^{-1})}\approx \dfrac{5{,}31}{\tau\ \mathrm{(ps)}}$ — vì thế phổ của trạng thái phân li nhanh chỉ là một dải rộng, không có cấu trúc vạch.

**Lỗi thường gặp:**
- Hiểu 'chuyển dời bị cấm' là hoàn toàn không xảy ra — sai vì quy tắc lọc lựa suy ra từ mô hình lí tưởng; ghép vibronic và ghép spin - obitan làm các chuyển dời cấm xuất hiện yếu, và chính chúng tạo ra lân quang cũng như màu của nhiều phức chất.
- Cho rằng phân tử không phân cực thì không có phổ dao động — sai vì điều kiện là momen lưỡng cực **biến thiên** trong quá trình dao động; CO$_2$ không phân cực nhưng dao động bất đối xứng và dao động biến dạng của nó vẫn hoạt động hồng ngoại, và đó chính là cơ chế hiệu ứng nhà kính.
- Cải tiến máy phổ để phân giải vạch có độ rộng tự nhiên lớn — vô ích vì độ rộng đó là hệ quả của thời gian sống hữu hạn; chỉ có thể thu hẹp bằng cách kéo dài thời gian sống của trạng thái, ví dụ làm lạnh hoặc pha loãng trong nền trơ.

<sub>`lesson.chemistry.pho-hoc.tuong-tac-buc-xa-vat-chat`</sub>

---

### 2. Phổ quay thuần tuý và xác định cấu trúc phân tử
*Pure rotational spectroscopy and molecular structure determination* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Xác định được vị trí các vạch trong phổ quay của phân tử thẳng
- Tính được độ dài liên kết từ hằng số quay đo được
- Giải thích được bao hình cường độ và hiệu chỉnh biến dạng li tâm

## Phổ đơn giản nhất, thông tin sắc nét nhất

Với quay tử cứng thẳng, $\tilde F(J)=BJ(J+1)$, và quy tắc lọc lựa $\Delta J=+1$ cho các vạch hấp thụ tại

$$\tilde\nu_{J\to J+1}=2B(J+1),\qquad J=0,1,2,\dots$$

Nghĩa là phổ quay là một dãy vạch **cách đều nhau đúng $2B$**. Không có phổ nào đơn giản hơn, và cũng ít phổ nào cho thông tin cấu trúc chính xác bằng.

Điều kiện: phân tử phải có **momen lưỡng cực vĩnh cửu**. Vì thế HCl, CO, H$_2$O có phổ quay vi sóng; H$_2$, N$_2$, CO$_2$, CH$_4$ thì không.

## Từ $B$ ra độ dài liên kết

$$B=\frac{h}{8\pi^2cI},\qquad I=\mu R^2$$

Vì $B$ đo được với sai số cỡ $10^{-4}$ cm$^{-1}$, độ dài liên kết suy ra chính xác tới $10^{-4}$ Å. Với phân tử ba nguyên tử trở lên, đo phổ của nhiều **đồng vị** (thay $\mu$ mà giữ nguyên hình học) cho đủ phương trình để giải ra toàn bộ bộ độ dài và góc liên kết. Đây là phương pháp chuẩn xác định cấu trúc pha khí.

## Cường độ: hai xu hướng đối nghịch

Dân số mức $J$ tỉ lệ với

$$N_J\propto (2J+1)\,e^{-hcBJ(J+1)/k_BT}$$

Thừa số suy biến $2J+1$ **tăng** theo $J$, thừa số Boltzmann **giảm**. Tích của chúng cực đại tại

$$J_{\max}\approx\sqrt{\frac{k_BT}{2hcB}}-\frac12$$

Với CO ở 300 K ($B=1{,}93$ cm$^{-1}$), $J_{\max}\approx 7$. Đó là lí do phổ quay có hình "quả chuông" chứ không giảm đơn điệu — và cũng là lí do đo bao hình cho phép **xác định nhiệt độ** của chất khí ở xa, kĩ thuật dùng trong thiên văn và trong chẩn đoán ngọn lửa.

## Hiệu chỉnh và giới hạn

Quay nhanh làm liên kết dãn:

$$\tilde F(J)=BJ(J+1)-D_JJ^2(J+1)^2,\qquad \tilde\nu_{J\to J+1}=2B(J+1)-4D_J(J+1)^3$$

$D_J$ nhỏ (cỡ $10^{-6}B$) nên chỉ lộ ra ở $J$ lớn, nhưng chính nó liên hệ với hằng số lực: $D_J\approx 4B^3/\tilde\nu_{dđ}^2$. Ngoài ra $B$ phụ thuộc trạng thái dao động ($B_v=B_e-\alpha_e(v+\tfrac12)$), nên phân tích chính xác phải tách $B_e$ từ nhiều mức $v$.

**Lỗi thường gặp:**
- Cho rằng mọi phân tử đều có phổ quay vi sóng — sai vì cần momen lưỡng cực vĩnh cửu để có momen chuyển dời khác 0; N$_2$, O$_2$, CO$_2$, CH$_4$ không có phổ quay hấp thụ (nhưng vẫn có phổ quay Raman).
- Lấy khoảng cách vạch bằng $B$ thay vì $2B$ — sai vì với $\Delta J=+1$, vạch $J\to J+1$ nằm tại $2B(J+1)$; nhầm hệ số 2 làm độ dài liên kết sai $\sqrt2$ lần.
- Bỏ qua biến dạng li tâm khi phân tích vạch có $J$ lớn — sai vì số hạng $-4D_J(J+1)^3$ tăng theo luỹ thừa ba; ở $J\sim 40$ nó đã đủ lớn để làm sai lệch rõ giá trị $B$ nếu khớp bằng đường thẳng.
- Dùng khối lượng nguyên tử trung bình của nguyên tố thay vì khối lượng của đồng vị cụ thể — sai vì phổ ứng với từng loại đồng vị; dùng 12,011 cho carbon thay vì 12,000 làm sai $\mu$ và do đó sai độ dài liên kết.

<sub>`lesson.chemistry.pho-hoc.pho-quay`</sub>

---

### 3. Phổ dao động hồng ngoại và hiệu ứng phi điều hoà
*Infrared vibrational spectroscopy and anharmonicity* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Áp dụng được quy tắc lọc lựa hồng ngoại và đếm được số dao động chuẩn của phân tử
- Phân tích được cấu trúc nhánh P, Q, R của phổ dao động - quay
- Vận dụng được thế Morse và ngoại suy Birge - Sponer để xác định năng lượng phân li

## Điều kiện để hoạt động hồng ngoại

Dao động chỉ hấp thụ hồng ngoại nếu momen lưỡng cực **biến thiên** dọc toạ độ dao động: $(\partial\mu/\partial Q)_0\ne 0$. Vì thế N$_2$ và O$_2$ trong suốt với hồng ngoại — may mắn cho khí quyển Trái Đất — trong khi CO$_2$ tuy không phân cực vẫn hấp thụ mạnh qua dao động bất đối xứng (2349 cm$^{-1}$) và dao động biến dạng (667 cm$^{-1}$).

Số dao động chuẩn: $3N-6$ (phi tuyến) hoặc $3N-5$ (thẳng). H$_2$O có 3, CO$_2$ có 4 (trong đó hai dao động biến dạng suy biến).

## Phi điều hoà: nơi mô hình lí tưởng nhường chỗ

Thế thật không phải parabol. Với thế Morse:

$$\tilde G(v)=\tilde\nu_e\left(v+\tfrac12\right)-\tilde\nu_ex_e\left(v+\tfrac12\right)^2$$

Hệ quả đo được:
- Khoảng cách các mức **giảm dần** khi $v$ tăng, và về 0 tại giới hạn phân li.
- Xuất hiện **hoạ ba** ($\Delta v=2,3,\dots$) tuy yếu — điều bị cấm hoàn toàn trong mô hình điều hoà.
- Phân biệt $D_e$ (độ sâu giếng) với $D_0$ (năng lượng phân li thực tế), khác nhau đúng năng lượng điểm không: $D_0=D_e-\tfrac12\tilde\nu_e+\tfrac14\tilde\nu_ex_e$.

**Ngoại suy Birge - Sponer**: vẽ $\Delta\tilde G_{v+1/2}=\tilde G(v+1)-\tilde G(v)$ theo $v$; đường thẳng cắt trục hoành ở $v_{\max}$, và diện tích dưới đường cho $D_0$. Phép này thường **ước lượng cao** $D_0$ vì đường thực cong xuống ở $v$ lớn.

## Cấu trúc quay chồng lên dao động

Ở pha khí, mỗi dao động kèm chuyển dời quay, cho ba nhánh:
- **Nhánh R** ($\Delta J=+1$): $\tilde\nu_0+2B(J+1)$, nằm phía số sóng cao.
- **Nhánh P** ($\Delta J=-1$): $\tilde\nu_0-2BJ$, phía số sóng thấp.
- **Nhánh Q** ($\Delta J=0$): đúng tại $\tilde\nu_0$, chỉ xuất hiện với dao động biến dạng của phân tử thẳng hoặc phân tử có momen động lượng electron. HCl **không có** nhánh Q, nên phổ của nó có một "khe" ở giữa.

Vì $B_1<B_0$ (liên kết dài hơn ở trạng thái dao động cao), khoảng cách vạch trong nhánh R thu hẹp dần và cuối cùng nhánh R "quay đầu" — hiện tượng band head.

## Dùng phổ IR trong thực hành

Vùng nhóm chức (4000–1500 cm$^{-1}$) cho biết có nhóm nào: O–H rộng 3300, C=O nhọn 1700, C$\equiv$N 2250. Vùng vân tay (dưới 1500 cm$^{-1}$) phức tạp nhưng đặc trưng cho từng chất — dùng để **đối chiếu nhận danh**, không dùng để suy luận cấu trúc từng mảnh.

**Lỗi thường gặp:**
- Đồng nhất số sóng vạch cơ bản với $\tilde\nu_e$ — sai vì vạch quan sát là $\tilde\nu_e-2\tilde\nu_ex_e$; với HCl chênh lệch hơn 100 cm$^{-1}$, đủ để làm sai hằng số lực vài phần trăm.
- Cho rằng hoạ ba nằm đúng ở bội số nguyên của vạch cơ bản — sai vì phi điều hoà làm các mức xích lại gần nhau; hoạ ba luôn thấp hơn bội số nguyên, và độ lệch chính là thước đo $\tilde\nu_ex_e$.
- Lẫn lộn $D_e$ và $D_0$ — sai vì $D_0$ tính từ mức $v=0$ (đã có năng lượng điểm không) nên luôn nhỏ hơn $D_e$; so sánh giá trị tính toán lượng tử ($D_e$) với thực nghiệm nhiệt hoá học ($D_0$) mà không hiệu chỉnh là lỗi phổ biến.
- Trông đợi nhánh Q ở mọi phổ dao động - quay — sai vì $\Delta J=0$ chỉ được phép khi có momen động lượng khác 0 quanh trục phân tử; phổ dao động dãn của HCl không có nhánh Q.

<sub>`lesson.chemistry.pho-hoc.pho-dao-dong-va-phi-dieu-hoa`</sub>

---

### 4. Phổ điện tử và nguyên lí Franck - Condon
*Electronic spectroscopy and the Franck - Condon principle* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Áp dụng được quy tắc lọc lựa spin và quy tắc Laporte cho chuyển dời điện tử
- Giải thích được phân bố cường độ trong dải vibronic bằng nguyên lí Franck - Condon
- Liên hệ được cấu trúc phân tử với vị trí và cường độ dải hấp thụ tử ngoại - khả kiến

## Chuyển dời điện tử: nhanh tới mức hạt nhân không kịp phản ứng

Electron chuyển trạng thái trong khoảng $10^{-15}$ s, còn một chu kì dao động là $10^{-13}$ s. Trong thời gian chuyển dời, hạt nhân **đứng yên**. Trên giản đồ hai đường thế năng, chuyển dời vì thế là một mũi tên **thẳng đứng** — đó là nội dung của nguyên lí Franck - Condon.

## Hệ quả cho hình dạng dải phổ

Trạng thái kích thích thường có liên kết yếu hơn nên độ dài cân bằng $R_e'$ lớn hơn $R_e''$. Mũi tên thẳng đứng từ đáy giếng dưới sẽ chạm giếng trên ở một mức dao động $v'$ **cao**, nơi hàm sóng dao động có biên độ lớn tại điểm quay đầu. Do đó:

$$I \propto \left|\int \psi_{v'}^*\psi_{v''}\,dR\right|^2$$

- $R_e'\approx R_e''$: vạch $0\to0$ mạnh nhất, dải hẹp.
- $R_e'$ lệch nhiều: cường độ cực đại rơi vào $v'$ cao, dải rộng và có cấu trúc vibronic dài.
- $R_e'$ lệch rất nhiều: chuyển dời chạm vào **vùng liên tục** phía trên giới hạn phân li, phổ là dải trơn — phân tử phân li ngay sau khi hấp thụ (quang phân li).

Đo cấu trúc vibronic vì thế cho biết trực tiếp **hình học của trạng thái kích thích** — thông tin rất khó có bằng cách khác.

## Quy tắc lọc lựa

- **Spin**: $\Delta S=0$. Singlet $\to$ triplet bị cấm, nên hấp thụ trực tiếp vào triplet rất yếu. Ghép spin - obitan (mạnh ở nguyên tử nặng) nới lỏng quy tắc này — "hiệu ứng nguyên tử nặng".
- **Laporte**: $g\leftrightarrow u$ cho hệ có tâm đối xứng. Chuyển dời d–d của phức bát diện bị cấm nên $\varepsilon$ chỉ 1–100, trong khi chuyển điện tích cho phép có $\varepsilon$ tới $10^4$–$10^5$. Đó là lí do KMnO$_4$ (chuyển điện tích) màu tím đậm còn [Ni(H$_2$O)$_6$]$^{2+}$ (d–d) chỉ xanh nhạt.

## Đọc phổ UV-Vis trong hoá hữu cơ

Liên hợp càng dài, khe HOMO - LUMO càng nhỏ, $\lambda_{\max}$ càng lớn (dịch chuyển bathochromic). Quy tắc **Woodward - Fieser** cho phép tính $\lambda_{\max}$ của dien và enone liên hợp bằng cách cộng số gia cho từng nhóm thế — công cụ kinh nghiệm nhưng chính xác tới vài nanomet.

Phân biệt các loại chuyển dời theo $\varepsilon$: $n\to\pi^*$ yếu ($\varepsilon\sim 10$–100, bị cấm đối xứng), $\pi\to\pi^*$ mạnh ($\varepsilon\sim 10^4$). Dung môi phân cực làm dải $n\to\pi^*$ dịch xanh và dải $\pi\to\pi^*$ dịch đỏ — một phép thử đơn giản để phân loại dải phổ.

**Lỗi thường gặp:**
- Vẽ chuyển dời điện tử là mũi tên nghiêng trên giản đồ thế năng — sai vì hạt nhân không kịp chuyển động trong thời gian chuyển dời; mũi tên phải thẳng đứng, và chính điều đó quyết định phân bố cường độ vibronic.
- Cho rằng vạch $0\to0$ luôn mạnh nhất — sai khi hình học trạng thái kích thích khác nhiều so với trạng thái cơ bản; khi đó xen phủ của $\psi_{0}''$ với $\psi_{0}'$ rất nhỏ và cường độ dồn về các $v'$ cao.
- Kết luận chuyển dời d–d bị cấm nên phức không có màu — sai vì dao động bất đối xứng phá vỡ tâm đối xứng tức thời (ghép vibronic), làm chuyển dời trở nên yếu chứ không tắt; đó chính là màu nhạt đặc trưng của nhiều phức kim loại chuyển tiếp.
- Dùng quy tắc Woodward - Fieser cho hệ không liên hợp hoặc hệ vòng bị xoắn — sai vì các số gia được rút ra từ tập chất liên hợp phẳng; mất tính phẳng làm liên hợp giảm và $\lambda_{\max}$ lệch hàng chục nanomet.

<sub>`lesson.chemistry.pho-hoc.pho-dien-tu-franck-condon`</sub>

---

### 5. Phổ Raman và quy tắc loại trừ lẫn nhau
*Raman spectroscopy and the mutual exclusion rule* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Giải thích được cơ chế tán xạ Raman và sự khác biệt với hấp thụ hồng ngoại
- Áp dụng được quy tắc lọc lựa dựa trên độ phân cực và quy tắc loại trừ lẫn nhau
- Tính được tỉ số cường độ vạch anti-Stokes trên Stokes và dùng nó để xác định nhiệt độ

## Một cơ chế khác hẳn

Hồng ngoại là **hấp thụ**: photon có năng lượng đúng bằng khe mức dao động bị nuốt. Raman là **tán xạ**: photon năng lượng bất kì (thường laser khả kiến) đưa phân tử lên một trạng thái ảo, rồi phân tử phát ra photon khác.

- Về đúng mức cũ: tán xạ Rayleigh (đàn hồi, mạnh nhất).
- Về mức dao động cao hơn: vạch **Stokes**, $\tilde\nu_{tán xạ}=\tilde\nu_{tới}-\tilde\nu_{dđ}$.
- Về mức thấp hơn (xuất phát từ $v=1$): vạch **anti-Stokes**, $\tilde\nu_{tới}+\tilde\nu_{dđ}$.

Điểm quan trọng: **độ dịch chuyển Raman không phụ thuộc bước sóng laser**, nên đổi laser vẫn thu được cùng một phổ dao động.

## Quy tắc lọc lựa dựa trên độ phân cực

Dao động hoạt động Raman khi $(\partial\alpha/\partial Q)_0\ne 0$. Điều này bổ sung chứ không trùng với điều kiện hồng ngoại ($\partial\mu/\partial Q\ne 0$).

Hệ quả nổi bật: H$_2$, N$_2$, O$_2$ **không** hoạt động hồng ngoại nhưng **có** phổ Raman, vì kéo dãn liên kết làm đám mây electron dễ bị phân cực hơn. Nhờ đó Raman theo dõi được N$_2$ và O$_2$ trong không khí — điều IR không làm được.

Với CO$_2$ (có tâm đối xứng): dao động đối xứng chỉ hoạt động Raman, dao động bất đối xứng và biến dạng chỉ hoạt động IR. Đây là minh hoạ của **quy tắc loại trừ lẫn nhau**, và cũng là cách xác định thực nghiệm rằng CO$_2$ **thẳng** chứ không gấp khúc.

## Tỉ số cường độ và nhiệt kế quang học

Vạch anti-Stokes chỉ sinh ra từ phân tử đã ở $v=1$, nên cường độ tỉ lệ với dân số mức đó:

$$\frac{I_{anti-S}}{I_{S}}=\left(\frac{\tilde\nu_0+\tilde\nu_{dđ}}{\tilde\nu_0-\tilde\nu_{dđ}}\right)^4 e^{-hc\tilde\nu_{dđ}/k_BT}$$

Ở nhiệt độ phòng với $\tilde\nu_{dđ}=1000$ cm$^{-1}$, thừa số Boltzmann chỉ khoảng 0,008 — nên vạch anti-Stokes rất yếu, và thực tế người ta luôn đo phía Stokes. Đảo ngược công thức cho một **nhiệt kế không tiếp xúc**, dùng đo nhiệt độ ngọn lửa và vi mạch.

## Phổ quay Raman

Với $\Delta J=\pm 2$ (khác IR), phổ quay Raman của phân tử thẳng cho các vạch cách đều $4B$, và tồn tại cả với phân tử không phân cực — cách duy nhất đo hằng số quay của N$_2$ hay O$_2$.

## Hạn chế thực tế

Tiết diện Raman rất nhỏ (khoảng $10^{-6}$ photon tán xạ Raman trên mỗi photon Rayleigh), nên tín hiệu yếu và dễ bị **huỳnh quang** của tạp chất che lấp. Giải pháp: laser hồng ngoại gần (1064 nm) để tránh kích thích huỳnh quang, hoặc dùng tăng cường bề mặt (SERS) để tăng tín hiệu tới $10^6$ lần.

**Lỗi thường gặp:**
- Nghĩ Raman là hấp thụ nên cần laser có năng lượng bằng khe dao động — sai vì Raman là tán xạ qua trạng thái ảo; bất kì bước sóng nào cũng dùng được, và độ dịch chuyển Raman không đổi khi đổi laser.
- Cho rằng dao động hoạt động IR thì cũng hoạt động Raman — sai với phân tử có tâm đối xứng, nơi quy tắc loại trừ lẫn nhau cấm điều đó; chính sự loại trừ này là bằng chứng thực nghiệm cho tâm đối xứng.
- Bỏ qua thừa số $(\tilde\nu)^4$ khi tính tỉ số anti-Stokes/Stokes — sai vì cường độ tán xạ tỉ lệ bậc bốn với số sóng phát ra; bỏ qua nó làm sai tỉ số khoảng hai lần với dao động tần số cao.
- Giải thích vạch anti-Stokes yếu bằng 'xác suất tán xạ thấp hơn' — sai vì nguyên nhân là dân số: mức $v=1$ hầu như trống ở nhiệt độ phòng; nung nóng mẫu làm anti-Stokes mạnh lên rõ rệt.

<sub>`lesson.chemistry.pho-hoc.pho-raman`</sub>

---

### 6. Huỳnh quang, lân quang và giản đồ Jablonski
*Fluorescence, phosphorescence and the Jablonski diagram* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Phân biệt được huỳnh quang và lân quang theo tính chất spin và thời gian sống
- Tính được hiệu suất lượng tử và thời gian sống từ các hằng số tốc độ cạnh tranh
- Vận dụng được nguyên lí FRET để đo khoảng cách trong hệ sinh học

## Đường đi của một photon đã bị hấp thụ

Sau hấp thụ, phân tử ở mức dao động cao của S$_1$ (hoặc S$_2$). Hồi phục dao động trong dung dịch mất khoảng $10^{-12}$ s — nhanh hơn phát xạ ($10^{-9}$ s) ba bậc. Đó là nội dung của **quy tắc Kasha**: phát xạ luôn từ mức thấp nhất của S$_1$, bất kể ta kích thích ở bước sóng nào. Hệ quả kiểm chứng được: **phổ phát xạ không phụ thuộc bước sóng kích thích**.

Vì một phần năng lượng đã mất vào hồi phục dao động và vào tái tổ chức dung môi, phổ phát xạ luôn nằm ở bước sóng dài hơn — **dịch chuyển Stokes**. Phổ hấp thụ và phổ huỳnh quang thường gần đối xứng gương nhau, vì cấu trúc dao động của hai trạng thái tương tự.

## Huỳnh quang so với lân quang

| | Huỳnh quang | Lân quang |
|---|---|---|
| Chuyển dời | S$_1\to$S$_0$ | T$_1\to$S$_0$ |
| Spin | cho phép | bị cấm |
| Thời gian sống | ns | $\mu$s đến s |
| Bước sóng | ngắn hơn | dài hơn |

Đường vào T$_1$ là **chuyển hệ** S$_1\to$T$_1$, một quá trình bị cấm spin nhưng được mở nhờ ghép spin - obitan. Vì thế nguyên tử nặng (Br, I, kim loại) làm tăng mạnh hiệu suất lân quang — "hiệu ứng nguyên tử nặng", cơ sở của các chất phát quang OLED dùng phức Ir và Pt.

## Định lượng bằng các hằng số tốc độ cạnh tranh

$$\tau=\frac{1}{k_f+k_{ic}+k_{isc}+k_r},\qquad \Phi_f=\frac{k_f}{k_f+k_{ic}+k_{isc}+k_r}=k_f\tau$$

Hai hệ thức này cho phép tách $k_f$ (bản chất của chuyển dời) khỏi các kênh mất mát: đo $\Phi_f$ và $\tau$ là đủ.

## FRET: cái thước phân tử

Khi phổ phát xạ của chất cho chồng lấp phổ hấp thụ của chất nhận và hai chất ở gần nhau, năng lượng truyền không bức xạ với hiệu suất

$$E=\frac{R_0^6}{R_0^6+r^6}$$

Phụ thuộc $r^{-6}$ rất dốc: quanh $r=R_0$ (thường 2–6 nm), thay đổi 10 % khoảng cách làm hiệu suất đổi rõ rệt. Nhờ đó FRET đo được sự gấp cuộn protein, sự bắt cặp DNA và tương tác protein - protein **trong tế bào sống**, ở thang khoảng cách mà kính hiển vi quang học không phân giải nổi.

Lưu ý: $R_0$ phụ thuộc chỉ số khúc xạ, độ chồng lấp phổ và **hệ số định hướng** $\kappa^2$ — đại lượng thường phải giả thiết bằng 2/3 (định hướng ngẫu nhiên), và đó là nguồn sai số hệ thống lớn nhất của phương pháp.

**Lỗi thường gặp:**
- Cho rằng kích thích ở bước sóng khác sẽ cho phổ phát xạ khác — sai theo quy tắc Kasha: hồi phục dao động và chuyển nội bộ nhanh hơn phát xạ nhiều bậc, nên phát xạ luôn từ mức thấp nhất của S$_1$; phổ phát xạ độc lập với bước sóng kích thích.
- Coi lân quang là huỳnh quang có thời gian sống dài — sai vì bản chất là chuyển dời **bị cấm spin** T$_1\to$S$_0$; do đó lân quang có năng lượng thấp hơn huỳnh quang của cùng chất và nhạy với oxi (chất dập tắt triplet hiệu quả).
- Dùng FRET để đo khoảng cách lớn hơn $2R_0$ — sai vì hiệu suất khi đó dưới 2 % và chìm trong nhiễu; FRET chỉ nhạy trong khoảng $0{,}5R_0$ đến $1{,}5R_0$.
- Bỏ qua hệ số định hướng $\kappa^2$ khi tính $R_0$ — sai vì giá trị 2/3 chỉ đúng khi cả hai lưỡng cực quay tự do nhanh so với thời gian sống; với nhãn bị cố định cứng, $\kappa^2$ có thể từ 0 đến 4, gây sai số khoảng cách tới 35 %.

<sub>`lesson.chemistry.pho-hoc.huynh-quang-va-lan-quang`</sub>

---

### 7. Phổ NMR: độ dịch chuyển hoá học và ghép spin - spin
*NMR spectroscopy: chemical shift and spin-spin coupling* · Đại học · intl-undergrad · 90 phút · nang-cao

**Mục tiêu:**
- Giải thích được nguồn gốc của độ dịch chuyển hoá học và vì sao dùng thang ppm
- Vận dụng được quy tắc $n+1$ và quy tắc bội tổng quát để xác định số vạch và cường độ tương đối
- Vận dụng được phương trình Karplus để suy ra thông tin về góc nhị diện

## Vì sao mỗi proton có một tần số riêng

Đặt trong từ trường $B_0$, hạt nhân spin 1/2 tách thành hai mức, cộng hưởng ở tần số Larmor $\nu=\gamma B_0/2\pi$. Nhưng electron quanh hạt nhân sinh dòng cảm ứng chống lại $B_0$, nên trường thực tại hạt nhân là $B_0(1-\sigma)$. Hạt nhân trong môi trường electron khác nhau có $\sigma$ khác nhau — đó là **độ dịch chuyển hoá học**.

Vì hiệu tần số tỉ lệ với $B_0$, người ta chuẩn hoá:

$$\delta=\frac{\nu-\nu_{ref}}{\nu_{máy}}\times 10^{6}\ \mathrm{(ppm)}$$

Nhờ đó $\delta$ của một proton là như nhau trên máy 300 MHz hay 600 MHz. Ngược lại, để đổi $\delta$ ra Hz phải nhân với tần số máy: $\Delta\nu = \delta\times\nu_{máy}$.

Vài mốc $^1$H: TMS 0; alkane 0,9–1,5; cạnh C=O hay O 2–4; alkene 5–6; thơm 7–8; aldehyde 9–10; COOH 10–13.

## Ghép spin - spin: thông tin về hàng xóm

Spin của hạt nhân lân cận làm tách vạch. Với $n$ proton tương đương lân cận (tất cả cùng $J$), tín hiệu tách thành $n+1$ vạch, cường độ theo tam giác Pascal. Nếu có hai nhóm lân cận khác nhau với $J_1\ne J_2$, số vạch là $(n_1+1)(n_2+1)$ — bội của bội, ví dụ "dd" (doublet của doublet).

Ba đặc điểm phải nhớ:
- $J$ đo bằng **Hz**, không đổi khi tăng từ trường; đó là cách phân biệt ghép thật với hai tín hiệu chồng lấp.
- Ghép có **tính đối ứng**: hai nhóm ghép với nhau có cùng $J$ — dùng để nối các mảnh khi giải cấu trúc.
- Hạt nhân **tương đương** không ghép nhau quan sát được.

## Karplus: từ $J$ ra hình học

$$^3J_{HH}=A\cos^2\phi+B\cos\phi+C$$

$^3J$ lớn khi $\phi\approx 0°$ hoặc $180°$, nhỏ khi $\phi\approx 90°$. Ứng dụng: proton trans-diaxial trên cyclohexane ($\phi\approx 180°$) có $J\approx 10$–13 Hz, còn axial - equatorial hoặc equatorial - equatorial ($\phi\approx 60°$) chỉ 2–5 Hz. Trong alkene, $J_{trans}$ (15–17 Hz) lớn hơn hẳn $J_{cis}$ (7–11 Hz) — cách gán hình học nhanh và chắc chắn.

## Đừng quên tích phân và trao đổi

Diện tích tín hiệu tỉ lệ **số proton**, nên tích phân cho công thức tỉ lệ. Proton của OH, NH thường cho tín hiệu tù, không ghép và biến mất khi lắc với D$_2$O, vì chúng trao đổi nhanh — hiện tượng này là một công cụ chẩn đoán chứ không phải phiền toái.

**Lỗi thường gặp:**
- Cho rằng hằng số ghép $J$ tăng khi dùng máy từ trường mạnh hơn — sai vì $J$ truyền qua electron liên kết, không liên quan đến $B_0$; chỉ khoảng cách tính bằng Hz giữa các **tín hiệu khác nhau** mới tăng theo $B_0$.
- Áp dụng quy tắc $n+1$ khi các hàng xóm không tương đương — sai vì khi $J_1\ne J_2$ phải nhân các bội với nhau, cho $(n_1+1)(n_2+1)$ vạch; ép vào $n+1$ sẽ đếm nhầm số proton lân cận.
- Đếm số vạch của một bội rồi chia khoảng cách hai vạch ngoài cùng cho số vạch — sai vì số **khoảng cách** ít hơn số vạch một đơn vị; với sextet phải chia cho 5 chứ không phải 6.
- Kết luận không có nhóm OH vì thiếu tín hiệu ghép — sai vì proton OH thường trao đổi nhanh nên cho vạch đơn tù, vị trí phụ thuộc nồng độ và dung môi; phép thử D$_2$O mới là cách xác nhận.

<sub>`lesson.chemistry.pho-hoc.nmr-dich-chuyen-va-ghep-spin`</sub>

---

### 8. NMR carbon-13 và các kĩ thuật hai chiều
*Carbon-13 NMR and two-dimensional techniques* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được vì sao phổ $^{13}$C có độ nhạy thấp và thường được ghi ở chế độ khử ghép proton
- Đọc được thông tin từ phổ DEPT để phân loại carbon theo số hydro gắn vào
- Trình bày được nguyên lí và cách đọc bản đồ COSY, HSQC, HMBC ở mức khái niệm

## Vấn đề độ nhạy

$^{13}$C chỉ chiếm 1,1 % carbon tự nhiên, và $\gamma(^{13}\mathrm{C})$ chỉ bằng 1/4 của $^1$H. Vì tín hiệu tỉ lệ với $\gamma^3$ và với độ phổ biến, $^{13}$C kém nhạy hơn $^1$H khoảng 5700 lần. Hệ quả thực tế: phải cộng dồn hàng nghìn lần quét, và **tích phân phổ $^{13}$C thường không tin cậy** vì thời gian hồi phục của các carbon rất khác nhau và có hiệu ứng NOE không đồng đều.

Bù lại có hai lợi thế lớn: thang $\delta$ rộng (0–220 ppm so với 0–12 ppm của proton) nên hầu như không chồng lấp; và xác suất hai $^{13}$C nằm cạnh nhau chỉ $(0{,}011)^2\approx10^{-4}$ nên không thấy ghép C–C.

## Đọc phổ carbon

Ở chế độ khử ghép proton, **mỗi carbon không tương đương cho đúng một vạch**. Chỉ riêng việc đếm vạch đã cho biết tính đối xứng của phân tử: toluene có 7 carbon nhưng chỉ 5 vạch, vì hai cặp carbon vòng tương đương nhau.

Mốc $\delta(^{13}$C): alkane 0–50; cạnh O hoặc N 50–90; alkyne 70–90; alkene và thơm 110–160; nitrile 115–125; ester và amide 165–180; ketone và aldehyde 190–220.

**DEPT-135** bổ sung phần thông tin bị mất khi khử ghép: CH và CH$_3$ hướng lên, CH$_2$ hướng xuống, carbon bậc bốn vắng mặt. So phổ khử ghép với DEPT là cách nhanh nhất để tìm carbon bậc bốn.

## Vì sao cần chiều thứ hai

Phổ một chiều cho danh sách các mảnh; câu hỏi khó là **nối chúng lại**. Phổ hai chiều trải tín hiệu lên một mặt phẳng, đỉnh chéo cho biết hai hạt nhân có liên hệ.

- **COSY** ($^1$H–$^1$H): đỉnh chéo nối các proton ghép nhau. Đi theo chuỗi đỉnh chéo là dựng được mạch carbon có hydro.
- **HSQC** ($^1$H–$^{13}$C qua một liên kết): gán mỗi proton với carbon mang nó. Đây là bước "phiên dịch" giữa hai phổ một chiều.
- **HMBC** ($^1$H–$^{13}$C qua 2–3 liên kết): công cụ mạnh nhất, vì nó **vượt qua** được carbon bậc bốn và dị nguyên tử — chính những chỗ mà COSY im lặng.
- **NOESY** (không gian, không qua liên kết): cho biết hai hạt nhân gần nhau trong không gian dưới ~5 Å; dùng xác định lập thể và cấu dạng.

## Chiến lược thực hành

Quy trình chuẩn: phổ khối cho công thức phân tử $\to$ IR cho nhóm chức $\to$ $^1$H và $^{13}$C cho các mảnh $\to$ HSQC gán proton - carbon $\to$ COSY nối mạch $\to$ HMBC ghép các mảnh qua carbon bậc bốn $\to$ NOESY xác định lập thể. Mỗi bước phải **nhất quán** với các bước trước; một mâu thuẫn nhỏ thường có nghĩa là giả thiết cấu trúc sai chứ không phải dữ liệu sai.

**Lỗi thường gặp:**
- Dùng tích phân phổ $^{13}$C để đếm số carbon — sai vì thời gian hồi phục dọc và hiệu ứng NOE khác nhau giữa các carbon, đặc biệt carbon bậc bốn có tín hiệu yếu bất thường; muốn định lượng phải dùng chuỗi xung chuyên biệt với thời gian chờ dài và tắt NOE.
- Kết luận số vạch $^{13}$C bằng số carbon — sai khi phân tử có đối xứng; ngược lại, số vạch **ít hơn** số carbon chính là thông tin quý về đối xứng, như trường hợp vòng benzene thế một lần cho 4 vạch từ 6 carbon.
- Coi đỉnh chéo COSY là bằng chứng hai carbon nối trực tiếp — sai vì COSY chỉ nói hai **proton** ghép nhau, thường qua 3 liên kết; muốn khẳng định nối carbon - carbon qua nguyên tử không mang hydro phải dùng HMBC.
- Nhầm NOESY với COSY — sai vì NOESY phản ánh khoảng cách **không gian** (qua không gian, không qua liên kết); hai proton cách nhau nhiều liên kết vẫn cho NOE nếu chúng gần nhau về hình học, và đó chính là giá trị của nó trong xác định lập thể.

<sub>`lesson.chemistry.pho-hoc.nmr-carbon-va-hai-chieu`</sub>

---

### 9. Phổ khối lượng và cách đọc các mảnh
*Mass spectrometry and fragment interpretation* · Đại học · intl-undergrad · 90 phút · nang-cao

**Mục tiêu:**
- Giải thích được nguyên lí tách theo tỉ số $m/z$ và ý nghĩa của độ phân giải
- Vận dụng được quy tắc nitơ và cụm pic đồng vị để suy ra công thức phân tử
- Phân tích được các kiểu phân mảnh đặc trưng để suy ra khung cấu trúc

## Đo cái gì và đo thế nào

Phổ khối ion hoá mẫu rồi tách các ion theo tỉ số **khối lượng trên điện tích** $m/z$. Với ion đơn điện tích, $m/z$ chính là khối lượng ion. Ion hoá va chạm electron (EI, 70 eV) truyền dư năng lượng nên phân mảnh mạnh — cho "vân tay" cấu trúc; ion hoá mềm (ESI, MALDI) giữ ion phân tử nguyên vẹn — thích hợp cho protein và chất kém bền.

**Độ phân giải** quyết định loại thông tin thu được. Ở $R\approx 10^3$, ta chỉ có khối lượng nguyên. Ở $R>10^4$ (phổ khối phân giải cao), ta đo khối lượng chính xác tới 4 chữ số thập phân và **suy ra công thức phân tử duy nhất**: N$_2$ (28,0062) tách được khỏi CO (27,9949) và C$_2$H$_4$ (28,0313).

## Ba đầu mối đọc nhanh

1. **Quy tắc nitơ**: $M$ chẵn $\Rightarrow$ số N chẵn (kể cả 0); $M$ lẻ $\Rightarrow$ số N lẻ. Một pic phân tử ở 121 lập tức nói rằng phân tử có số lẻ nguyên tử nitơ.

2. **Cụm pic đồng vị**: tỉ số $M{+}2$ so với $M$ là dấu hiệu nhận dạng halogen và lưu huỳnh.
 - Cl: $M{:}M{+}2 \approx 3{:}1$
 - Br: $M{:}M{+}2 \approx 1{:}1$
 - S: $M{+}2$ khoảng 4,4 %
 Còn $M{+}1$ cho số carbon: mỗi carbon đóng góp 1,1 %, nên $M{+}1$ bằng 6,6 % của $M$ nghĩa là khoảng 6 carbon.

3. **Mảnh mất đi** thường dễ đọc hơn mảnh còn lại: mất 15 (CH$_3$), 18 (H$_2$O), 28 (CO hoặc C$_2$H$_4$), 29 (CHO hoặc C$_2$H$_5$), 31 (OCH$_3$), 45 (COOH).

## Quy luật phân mảnh

Ion bền hơn thì pic mạnh hơn. Vì thế:
- **Cắt alpha** cạnh dị nguyên tử tạo ion oxocarbenium hoặc iminium bền: đây là mảnh chủ đạo của alcohol, ether, amine.
- **Cắt benzylic** cho ion tropylium $m/z$ 91 — pic đặc trưng gần như chắc chắn của nhóm benzyl.
- **Chuyển vị McLafferty** cho ion khối lượng **chẵn** từ phân tử không chứa N; thấy pic chẵn giữa các pic lẻ là dấu hiệu mạnh của chuyển vị này ở hợp chất carbonyl.
- Alcohol thường **mất pic ion phân tử** vì dễ tách nước; không thấy $M$ không có nghĩa là mẫu sai.

## Đọc có kỉ luật

Phổ khối cho công thức và khung; nó **không** phân biệt được đồng phân lập thể và thường không phân biệt được đồng phân vị trí. Kết luận cấu trúc phải luôn được kiểm chứng chéo bằng NMR và IR.

**Lỗi thường gặp:**
- Cho rằng pic có $m/z$ lớn nhất luôn là ion phân tử — sai vì cụm đồng vị làm xuất hiện pic ở $M{+}1$, $M{+}2$; ngược lại nhiều chất (alcohol, một số amine) mất hẳn pic ion phân tử do phân mảnh quá nhanh.
- Dùng tỉ lệ $M{+}2$ để đếm carbon — sai vì $M{+}2$ chủ yếu phản ánh halogen, lưu huỳnh và oxi; số carbon phải đọc từ $M{+}1$ với hệ số 1,1 % cho mỗi carbon.
- Kết luận cấu trúc lập thể từ phổ khối — sai vì các đồng phân đối quang và hầu hết đồng phân hình học cho phổ khối giống hệt nhau; phổ khối chỉ nói về thành phần và khung liên kết.
- Quên rằng ion mảnh **chẵn** từ hợp chất không chứa N là bất thường — bỏ qua dấu hiệu này làm mất manh mối quan trọng về chuyển vị McLafferty ở hợp chất carbonyl.

<sub>`lesson.chemistry.pho-hoc.pho-khoi-va-doc-manh`</sub>

---

### 10. Phân tích cấu trúc tổng hợp từ nhiều loại phổ
*Integrated structure determination from combined spectra* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Xây dựng được quy trình phối hợp phổ khối, IR, NMR để xác định cấu trúc chưa biết
- Tính được độ bất bão hoà và dùng nó để giới hạn các khung cấu trúc có thể
- Đánh giá được giả thiết cấu trúc bằng kiểm chứng chéo và loại bỏ phương án mâu thuẫn

## Mỗi phổ trả lời một câu hỏi khác nhau

Không có phổ nào một mình giải được cấu trúc. Sức mạnh nằm ở sự **phối hợp**, vì mỗi kĩ thuật nhìn phân tử từ một góc:

- **Phổ khối** $\to$ công thức phân tử, sự có mặt của halogen/S, khung qua các mảnh.
- **IR** $\to$ nhóm chức: có carbonyl không? là acid, ester hay ketone? có OH, NH, C$\equiv$N không?
- **$^1$H NMR** $\to$ số proton mỗi loại, số hàng xóm, môi trường electron, hình học qua $J$.
- **$^{13}$C và DEPT** $\to$ số carbon không tương đương, phân loại theo số hydro, phát hiện carbon bậc bốn.
- **2D NMR** $\to$ nối các mảnh lại với nhau.

## Quy trình chuẩn

1. **Công thức phân tử** từ phổ khối phân giải cao (hoặc từ $M$, $M{+}1$, $M{+}2$).
2. **Độ bất bão hoà**:
$$\mathrm{DoU}=\frac{2n_C+2+n_N-n_H-n_X}{2}$$
Ghi nhớ: mỗi vòng hoặc mỗi liên kết đôi là 1; mỗi liên kết ba là 2; vòng benzene là **4**.
3. **Nhóm chức từ IR**: một băng mạnh 1700–1750 cm$^{-1}$ dùng hết 1 DoU; băng rộng 3200–3600 báo OH.
4. **Đếm và phân loại carbon** từ $^{13}$C + DEPT; so với số carbon trong công thức để phát hiện **đối xứng**.
5. **Dựng mảnh** từ $^1$H NMR: tích phân cho số H, độ bội cho hàng xóm, $\delta$ cho môi trường.
6. **Ráp mảnh**: cộng nguyên tử các mảnh, phần còn thiếu chính là phần nối chúng.
7. **Kiểm chứng chéo** với mọi dữ liệu, kể cả những dữ liệu chưa dùng.

## Nguyên tắc kỉ luật

Đừng dừng lại ở cấu trúc **đầu tiên** khớp được vài dữ kiện. Hãy liệt kê các đồng phân hợp lí rồi tìm dữ kiện **phân biệt** chúng. Ví dụ, để phân biệt ester CH$_3$COOCH$_2$CH$_3$ với CH$_3$CH$_2$COOCH$_3$, cả hai đều có $M=88$ và một băng C=O; nhưng $\delta$ của nhóm gắn với oxi (khoảng 4,1 ppm) so với nhóm gắn với carbonyl (khoảng 2,3 ppm) phân biệt chúng ngay.

Và luôn kiểm tra: cấu trúc đề xuất có giải thích **mọi** tín hiệu không, hay còn tín hiệu nào bị bỏ mặc? Tín hiệu không giải thích được là dấu hiệu cấu trúc sai hoặc mẫu không tinh khiết.

**Lỗi thường gặp:**
- Chốt cấu trúc ngay khi tìm được phương án khớp vài dữ kiện — sai vì nhiều đồng phân cùng khớp một phần; phải chủ động tìm dữ kiện **phân biệt** rồi mới kết luận.
- Bỏ qua tín hiệu không giải thích được — sai vì mọi vạch trong phổ đều có nguồn gốc; tín hiệu thừa hoặc là bằng chứng cấu trúc sai, hoặc là bằng chứng mẫu không tinh khiết, cả hai đều quan trọng.
- Tính độ bất bão hoà mà quên halogen hoặc nitơ — sai vì halogen phải trừ như hydro còn nitơ phải cộng thêm; sai DoU dẫn tới bỏ sót hoặc thêm thừa một vòng hay một liên kết đôi.
- Coi tích phân $^1$H NMR là số proton tuyệt đối — sai vì nó chỉ cho **tỉ lệ**; phải kết hợp với công thức phân tử từ phổ khối mới quy ra số proton thực.

<sub>`lesson.chemistry.pho-hoc.phan-tich-cau-truc-tong-hop`</sub>

---

## Unit 6: Hoá hữu cơ nâng cao

### 1. Hiệu ứng điện tử và phân tích cấu dạng
*Electronic effects and conformational analysis* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Phân biệt được hiệu ứng cảm ứng, hiệu ứng liên hợp và hiệu ứng siêu liên hợp
- Phân tích được cân bằng cấu dạng của hệ mạch hở và của cyclohexane thế
- Tính được tỉ lệ cấu dạng ở cân bằng bằng phân bố Boltzmann

## Ba cách electron dịch chuyển

Toàn bộ lập luận định tính trong hoá hữu cơ đều quy về việc mật độ electron được đẩy đi đâu.

- **Cảm ứng ($I$)**: truyền qua khung $\sigma$, do chênh lệch độ âm điện. Suy giảm mạnh theo khoảng cách — $\mathrm{p}K_a$ của acid butanoic đổi rõ khi gắn Cl ở C2, gần như không đổi khi gắn ở C4.
- **Liên hợp ($M$)**: truyền qua hệ $\pi$, đòi hỏi các obitan $p$ **song song**. Vì thế mất tính phẳng là mất hiệu ứng liên hợp — nguyên nhân khiến amide bị xoắn phản ứng khác hẳn amide phẳng.
- **Siêu liên hợp**: xen phủ giữa $\sigma_{\mathrm{C-H}}$ với obitan trống hoặc $\sigma^*$ kề bên. Đây là lí do carbocation bậc ba bền hơn bậc hai, và cũng là lí do alkene có nhiều nhóm thế bền hơn.

Cẩn thận: hai hiệu ứng có thể **ngược chiều** trên cùng một nhóm. Halogen rút electron theo cảm ứng nhưng cho electron theo liên hợp; kết quả là chúng làm giảm hoạt tính vòng benzene nhưng vẫn định hướng ortho/para.

## Cấu dạng mạch hở

Butane có ba cực tiểu: **anti** (0 kJ/mol), hai **gauche** ($+3{,}8$ kJ/mol). Rào quay qua cấu dạng che khuất syn cao khoảng 19 kJ/mol — đủ thấp để quay tự do ở nhiệt độ phòng, nhưng phân bố vẫn lệch rõ về anti.

Ở cân bằng, tỉ lệ tuân theo Boltzmann:

$$\frac{N_2}{N_1}=g\,e^{-\Delta E/RT}$$

với $g$ là số cấu dạng tương đương (butane có **hai** cấu dạng gauche, nên $g=2$).

## Cyclohexane: ghế và giá trị A

Cyclohexane tồn tại chủ yếu ở dạng ghế; sự lật ghế biến mọi vị trí axial thành equatorial. Nhóm thế ưu tiên equatorial vì ở axial nó chịu **tương tác 1,3-diaxial** với hai hydro axial cùng phía.

Giá trị A đo mức ưu tiên đó: CH$_3$ 7,3; iPr 9,3; **t-Bu 21** kJ/mol (khoá cứng vòng); OH chỉ 2,2–4,2 tuỳ dung môi; halogen 1–2 (nhỏ vì liên kết C–X dài, ít va chạm).

Với nhiều nhóm thế, các giá trị A **cộng gần đúng** — nguyên tắc thực dụng để dự đoán cấu dạng chiếm ưu thế.

## Vì sao cấu dạng lại quyết định phản ứng

Nhiều phản ứng có yêu cầu lập thể chặt: tách E2 đòi hỏi H và nhóm rời **anti-periplanar**, tức cả hai phải ở vị trí axial trên cyclohexane. Vì thế menthyl chloride và neomenthyl chloride tách với tốc độ chênh nhau hàng trăm lần và cho sản phẩm khác nhau, dù chỉ khác nhau ở cấu hình một tâm.

**Lỗi thường gặp:**
- Cộng thẳng các giá trị A cho nhóm thế cis-1,2 mà không xét tương tác gauche giữa chúng — sai vì giá trị A đo tương tác 1,3-diaxial của một nhóm đơn lẻ; khi hai nhóm ở cạnh nhau còn có tương tác trực tiếp mà phép cộng bỏ sót.
- Quên thừa số suy biến trong Boltzmann khi so anti với gauche của butane — sai vì có **hai** cấu dạng gauche tương đương nhưng chỉ một cấu dạng anti; bỏ qua hệ số 2 làm sai tỉ lệ hai lần.
- Cho rằng nhóm càng cồng kềnh về khối lượng thì giá trị A càng lớn — sai vì điều quyết định là khoảng cách C–X và hình dạng; iodine nặng hơn methyl nhiều nhưng có $A$ nhỏ hơn vì liên kết C–I dài, đẩy nguyên tử ra xa các hydro 1,3-diaxial.
- Dùng hiệu ứng liên hợp cho hệ không phẳng — sai vì liên hợp đòi hỏi các obitan $p$ song song; khi vòng bị xoắn hoặc nhóm thế bị cản trở không gian, hiệu ứng liên hợp giảm mạnh và chỉ còn hiệu ứng cảm ứng.

<sub>`lesson.chemistry.huu-co-nang-cao.hieu-ung-dien-tu-va-cau-dang`</sub>

---

### 2. Phân tích cơ chế bằng động học và đánh dấu đồng vị
*Mechanistic analysis by kinetics and isotopic labelling* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Thiết kế được thí nghiệm động học để phân biệt các cơ chế cạnh tranh
- Giải thích được nguồn gốc của hiệu ứng đồng vị động học sơ cấp và thứ cấp
- Vận dụng được tiên đề Hammond và nguyên lí Curtin - Hammett để dự đoán sản phẩm

## Cơ chế là giả thuyết bị kiểm tra, không phải câu chuyện

Bốn loại bằng chứng thường dùng, xếp theo sức thuyết phục tăng dần: sản phẩm — lập thể — động học — đánh dấu đồng vị.

## Động học phân biệt cơ chế thế nào

S$_N$1 cho $v=k[\mathrm{RX}]$ (bậc nhất, không phụ thuộc nucleophile), racemic hoá, ưu tiên chất nền bậc ba. S$_N$2 cho $v=k[\mathrm{RX}][\mathrm{Nu}]$, **nghịch đảo cấu hình Walden**, ưu tiên chất nền bậc nhất. Bậc phản ứng theo nucleophile vì thế là phép thử đơn giản mà quyết định.

Một cảnh báo: chất nền bậc ba trong dung môi phân cực có thể cho bậc nhất theo cả hai cơ chế nếu nucleophile là dung môi (solvolysis). Khi đó phải dùng thêm lập thể và hiệu ứng muối để phân biệt.

## Đánh dấu đồng vị: hai kiểu thông tin

**Vị trí nguyên tử.** Thuỷ phân ester được đánh dấu $^{18}$O cho biết liên kết nào bị cắt: acyl–O hay alkyl–O. Đây là bằng chứng trực tiếp về đường đi của nguyên tử, không thể suy được từ động học.

**Hiệu ứng đồng vị động học (KIE).** Liên kết C–H có năng lượng điểm không cao hơn C–D (vì $\tilde\nu\propto 1/\sqrt\mu$). Ở trạng thái chuyển tiếp mà liên kết đó đang bị bẻ, năng lượng điểm không gần như biến mất cho cả hai, nên C–D phải leo rào cao hơn:

$$\frac{k_H}{k_D}=\exp\left[\frac{hc(\tilde\nu_H-\tilde\nu_D)}{2k_BT}\right]$$

Ước lượng cho C–H (3000 cm$^{-1}$) và C–D (2200 cm$^{-1}$) cho $k_H/k_D\approx 6{,}9$ ở 298 K. **Đọc kết quả**: $k_H/k_D>2$ nghĩa là liên kết C–H bị bẻ trong bước quyết định tốc độ; $k_H/k_D\approx 1$ nghĩa là không. Giá trị vượt 8–10 là dấu hiệu có **đường hầm lượng tử**.

Hiệu ứng thứ cấp nhỏ hơn nhiều nhưng cũng nói được nhiều: chuyển $sp^3\to sp^2$ (như trong S$_N$1) làm dao động biến dạng lỏng ra, cho $k_H/k_D\approx 1{,}15$ (hiệu ứng bình thường); chuyển $sp^3\to sp^3$ chật hơn ở trạng thái chuyển tiếp S$_N$2 có thể cho hiệu ứng **nghịch** ($<1$).

## Hai nguyên lí định tính then chốt

**Hammond**: bước tạo carbocation là thu nhiệt nên trạng thái chuyển tiếp giống carbocation — vì thế yếu tố nào làm bền carbocation cũng làm tăng tốc độ. Đây là cầu nối giữa nhiệt động và động học.

**Curtin - Hammett**: nếu hai cấu dạng cân bằng nhanh, đừng suy tỉ lệ sản phẩm từ tỉ lệ cấu dạng. Cấu dạng chỉ chiếm 1 % vẫn có thể cho 99 % sản phẩm nếu rào của nó thấp hơn 10 kJ/mol. Chỉ khi cân bằng cấu dạng **chậm** hơn phản ứng thì tỉ lệ cấu dạng mới quyết định.

**Lỗi thường gặp:**
- Kết luận cơ chế chỉ từ sản phẩm — sai vì nhiều cơ chế khác nhau cho cùng sản phẩm; sản phẩm là bằng chứng yếu nhất, phải bổ sung bằng động học và lập thể.
- Cho rằng $k_H/k_D \approx 1$ nghĩa là liên kết C–H không tham gia phản ứng — sai vì nó chỉ nói liên kết đó không bị bẻ trong **bước quyết định tốc độ**; nó vẫn có thể bị bẻ ở một bước nhanh trước hoặc sau đó.
- Dự đoán tỉ lệ sản phẩm từ tỉ lệ cấu dạng ở cân bằng — sai theo Curtin - Hammett khi cân bằng cấu dạng nhanh hơn phản ứng; quyết định thuộc về hiệu năng lượng của hai **trạng thái chuyển tiếp**, không phải của hai cấu dạng.
- Coi $k_H/k_D = 12$ là bằng chứng cơ chế khác lạ — thực ra giá trị vượt giới hạn bán cổ điển (khoảng 7–8) là dấu hiệu của **đường hầm lượng tử** trong chuyển proton hoặc chuyển hydride, hiện tượng đã được ghi nhận rộng rãi trong xúc tác enzyme.

<sub>`lesson.chemistry.huu-co-nang-cao.phan-tich-co-che-dong-hoc-dong-vi`</sub>

---

### 3. Phương trình Hammett và quan hệ năng lượng tự do tuyến tính
*The Hammett equation and linear free energy relationships* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được ý nghĩa của hằng số nhóm thế $\sigma$ và hằng số phản ứng $\rho$
- Vận dụng được đồ thị Hammett để suy ra sự tích luỹ điện tích ở trạng thái chuyển tiếp
- Phân tích được ý nghĩa cơ chế của đồ thị Hammett bị gãy hoặc cong

## Ý tưởng: mượn một thang đo

Hammett nhận thấy ảnh hưởng của nhóm thế lên nhiều phản ứng khác nhau đều **tỉ lệ** với ảnh hưởng của nó lên một phản ứng chuẩn. Ông chọn sự ion hoá của acid benzoic thế làm chuẩn và định nghĩa

$$\sigma_X=\log\frac{K_X}{K_H}$$

$\sigma>0$ cho nhóm rút electron (NO$_2$: 0,78 para; CN: 0,66), $\sigma<0$ cho nhóm cho electron (NH$_2$: $-0{,}66$; OCH$_3$: $-0{,}27$ para). Với bất kì phản ứng nào khác:

$$\log\frac{k_X}{k_H}=\rho\,\sigma_X$$

## Đọc $\rho$: cỗ máy suy cơ chế

$\rho$ nói lên **điện tích tích luỹ ở trạng thái chuyển tiếp so với chất đầu**:

- $\rho>0$: trạng thái chuyển tiếp có mật độ electron **tăng** (điện tích âm phát triển), nên nhóm rút electron làm tăng tốc. Ví dụ: thuỷ phân ester trong base ($\rho\approx +2{,}5$).
- $\rho<0$: điện tích **dương** phát triển, nhóm cho electron làm tăng tốc. Ví dụ: solvolysis benzyl chloride ($\rho\approx -4$ đến $-5$).
- $|\rho|$ nhỏ (dưới 0,5): trung tâm phản ứng ít thay đổi điện tích, hoặc ở xa vòng.

Bản thân định nghĩa cho $\rho=1$ với phản ứng chuẩn (ion hoá acid benzoic ở 25 °C trong nước).

## Khi thang gốc không đủ

Nếu nhóm thế **liên hợp trực tiếp** với tâm phản ứng, hiệu ứng lớn hơn dự đoán và điểm lệch khỏi đường thẳng. Khi đó dùng:
- $\sigma^+$ cho trung tâm **thiếu electron** (carbocation): p-OCH$_3$ có $\sigma^+=-0{,}78$ so với $\sigma=-0{,}27$.
- $\sigma^-$ cho trung tâm **giàu electron** (phenolate, carbanion): p-NO$_2$ có $\sigma^-=1{,}27$ so với $\sigma=0{,}78$.

Việc dữ liệu khớp tốt hơn với $\sigma^+$ chính là **bằng chứng** rằng trạng thái chuyển tiếp mang điện tích dương được ổn định bằng liên hợp trực tiếp — một suy luận cơ chế rút ra từ dạng đồ thị.

## Đồ thị bất thường nói gì

- **Gãy khúc** (hai đoạn thẳng, $\rho$ đổi dấu hoặc đổi độ lớn): cơ chế **thay đổi** giữa hai vùng nhóm thế, ví dụ chuyển từ S$_N$1 sang S$_N$2.
- **Cong xuống liên tục**: bước quyết định tốc độ dịch dần khi nhóm thế thay đổi, phù hợp Hammond.
- **Tản mát không có xu hướng**: có thể hiệu ứng không gian chi phối — khi đó phải dùng phương trình **Taft**, vốn tách riêng số hạng cảm ứng $\sigma^*$ và số hạng không gian $E_s$.

Lưu ý về phạm vi: thang Hammett chỉ dùng cho nhóm thế **meta và para**; nhóm ortho gây cản trở không gian và ảnh hưởng trực tiếp lên tâm phản ứng nên nằm ngoài mô hình.

**Lỗi thường gặp:**
- Dùng thang Hammett cho nhóm thế ortho — sai vì mô hình chỉ tách hiệu ứng điện tử, còn nhóm ortho gây thêm cản trở không gian và có thể tương tác trực tiếp với tâm phản ứng; trường hợp này phải dùng phương trình Taft.
- Hiểu $\rho$ như 'độ nhanh của phản ứng' — sai vì $\rho$ chỉ đo **độ nhạy** với nhóm thế; một phản ứng rất nhanh vẫn có thể có $\rho$ gần 0 nếu trạng thái chuyển tiếp không thay đổi điện tích.
- Coi đồ thị Hammett gãy khúc là dữ liệu tồi — sai vì điểm gãy thường là thông tin quý nhất: nó báo hiệu **đổi cơ chế** hoặc đổi bước quyết định tốc độ khi bản chất điện tử của nhóm thế thay đổi.
- Tính $\rho$ bằng cách chia từng điểm cho $\sigma$ của nó — không đáng tin vì với $\sigma$ nhỏ, sai số thực nghiệm bị khuếch đại; phải hồi quy toàn bộ tập dữ liệu và báo cáo hệ số tương quan.

<sub>`lesson.chemistry.huu-co-nang-cao.phuong-trinh-hammett`</sub>

---

### 4. Hoá học lập thể và tổng hợp bất đối xứng
*Stereochemistry and asymmetric synthesis* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được các quan hệ lập thể và các khái niệm đồng phân đối quang, xuyên lập thể, meso
- Tính được độ dư đối quang từ độ quay cực và liên hệ nó với chênh lệch năng lượng hoạt hoá
- Phân tích được nguyên tắc của xúc tác bất đối xứng và của sự khuếch đại chọn lọc

## Vì sao lập thể là vấn đề sống còn

Hai đồng phân đối quang có mọi tính chất vật lí giống hệt nhau trong môi trường không bất đối, nhưng trong cơ thể — vốn hoàn toàn bất đối — chúng có thể khác nhau một trời một vực. Thalidomide là bài học đắt giá; ngày nay phần lớn dược phẩm mới được phát triển ở dạng một đối quang duy nhất.

## Đo mức độ bất đối

$$ee=\frac{|[R]-[S]|}{[R]+[S]}\times 100\,\%,\qquad ee \approx \frac{[\alpha]_{\text{quan sát}}}{[\alpha]_{\text{tinh khiết}}}\times100\,\%$$

Quan hệ với tỉ lệ đối quang: $er = (100+ee):(100-ee)$. Một $ee$ 90 % ứng với $er = 95{:}5$, tức vẫn còn 5 % đồng phân không mong muốn.

**Cảnh báo**: đo $ee$ bằng độ quay cực có nhiều bẫy (tạp chất quang hoạt, hiệu ứng nồng độ, giá trị chuẩn không chắc); nên dùng HPLC pha tĩnh bất đối hoặc NMR với tác nhân dịch chuyển.

## Chọn lọc là bài toán về hiệu năng lượng

Hai trạng thái chuyển tiếp dẫn tới hai đối quang là **xuyên lập thể** với nhau, nên khác năng lượng. Tỉ lệ sản phẩm:

$$\frac{k_{\text{chính}}}{k_{\text{phụ}}}=e^{\Delta\Delta G^{\ddagger}/RT},\qquad \Delta\Delta G^{\ddagger}=\Delta G^{\ddagger}_{\text{phụ}}-\Delta G^{\ddagger}_{\text{chính}}>0$$

Con số cần thuộc ở 25 °C: $\Delta\Delta G^{\ddagger}$ chỉ **5,7 kJ/mol** đã cho $ee = 82\,\%$; **11 kJ/mol** cho $ee\approx 98\,\%$. Nghĩa là chọn lọc xuất sắc chỉ đòi hỏi một khác biệt năng lượng nhỏ hơn một liên kết hydro — nhưng phải kiểm soát nó chính xác.

Hệ quả thực hành: **hạ nhiệt độ làm tăng $ee$** (vì $RT$ giảm), miễn là phản ứng vẫn chạy — mẹo đầu tiên khi tối ưu một phản ứng bất đối.

## Bốn chiến lược tạo bất đối

1. **Chất nền bất đối** (substrate control): tâm bất đối sẵn có định hướng phản ứng.
2. **Chất phụ trợ bất đối** (auxiliary): gắn tạm nhóm bất đối (oxazolidinone Evans), phản ứng, rồi tách ra.
3. **Tác nhân bất đối** (reagent): dùng lượng hợp thức, ví dụ CBS reduction.
4. **Xúc tác bất đối** (catalysis): hiệu quả nhất về nguyên tử — một lượng nhỏ xúc tác tạo lượng lớn sản phẩm. Sharpless epoxidation, Noyori hydrogenation, xúc tác hữu cơ bằng proline; ba giải Nobel đã trao cho hướng này.

## Curtin - Hammett lại xuất hiện

Trong nhiều phản ứng xúc tác, chất nền tạo hai phức xúc tác cân bằng nhanh với nhau. Phức **chiếm ưu thế** thường không phải phức phản ứng nhanh; theo Curtin - Hammett, chính phức **thiểu số nhưng hoạt động** quyết định sản phẩm. Đây là cơ chế Halpern nổi tiếng của hydro hoá Noyori — và là lí do việc "quan sát thấy phức nào nhiều nhất" không đủ để giải thích chọn lọc.

**Lỗi thường gặp:**
- Đồng nhất $ee$ với phần trăm đồng phân chính — sai vì $ee = 90\,\%$ nghĩa là hỗn hợp gồm 95 % đồng phân chính và 5 % đồng phân phụ, không phải 90 % và 10 %.
- Kết luận mẫu là racemic khi độ quay cực bằng 0 — sai vì hợp chất meso cũng không quay mặt phẳng ánh sáng phân cực dù là chất tinh khiết duy nhất; ngoài ra một số hỗn hợp không racemic vẫn có độ quay rất nhỏ ở bước sóng nhất định.
- Suy chọn lọc từ phức xúc tác quan sát được nhiều nhất — sai theo Curtin - Hammett; phức chiếm ưu thế thường là phức trơ, còn phức thiểu số phản ứng nhanh mới quyết định sản phẩm, như trong cơ chế Halpern.
- Cho rằng hạ nhiệt độ luôn cải thiện $ee$ — sai khi $\Delta\Delta S^{\ddagger}$ và $\Delta\Delta H^{\ddagger}$ trái dấu; khi đó tồn tại 'nhiệt độ đảo' mà bên dưới nó chọn lọc **giảm**, thậm chí đổi chiều.

<sub>`lesson.chemistry.huu-co-nang-cao.hoa-hoc-lap-the-va-tong-hop-bat-doi-xung`</sub>

---

### 5. Phản ứng vòng hoá và quy tắc Woodward - Hoffmann
*Pericyclic reactions and the Woodward - Hoffmann rules* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Phân loại được các phản ứng pericyclic theo kiểu chuyển vị electron
- Vận dụng được quy tắc Woodward - Hoffmann cho phản ứng electrocyclic, cộng vòng và chuyển vị sigmatropic
- Giải thích được sự đảo ngược lập thể khi chuyển từ điều kiện nhiệt sang điều kiện quang hoá

## Một lớp phản ứng có luật riêng

Phản ứng pericyclic không có chất trung gian, không nhạy với dung môi hay xúc tác, nhưng lại **cực kì đặc thù về lập thể** và đảo hoàn toàn lập thể khi chuyển từ đun nóng sang chiếu sáng. Sự đảo đó không giải thích được bằng ngôn ngữ cơ chế thông thường; nó là hệ quả của **đối xứng obitan**.

## Ba họ chính

- **Electrocyclic**: mở/đóng vòng của polyene.
- **Cộng vòng (cycloaddition)**: hai hệ $\pi$ ghép lại, ví dụ Diels - Alder [4+2].
- **Chuyển vị sigmatropic**: một liên kết $\sigma$ di chuyển dọc hệ $\pi$, ví dụ chuyển vị Cope [3,3] và Claisen [3,3].

## Cách suy nhanh: nhìn HOMO

Với phản ứng electrocyclic, chỉ cần xét đối xứng của **HOMO** ở hai đầu mạch. Hai thuỳ cùng dấu ở cùng phía thì đóng vòng disrotatory; khác dấu thì conrotatory.

Kết quả tổng quát cho hệ $4n$ và $4n+2$ electron $\pi$:

- $4n$ electron: **nhiệt — conrotatory**; quang — disrotatory.
- $4n{+}2$ electron: **nhiệt — disrotatory**; quang — conrotatory.

Ví dụ kiểm chứng: (2E,4Z,6E)-octatriene (6 electron $\pi$) đóng vòng nhiệt theo disrotatory cho cis-5,6-dimethylcyclohexadiene; chiếu sáng cho đồng phân trans. Không có phản ứng nào khác trong hoá hữu cơ cho sự đảo ngược sạch sẽ như vậy.

## Cộng vòng và chuyển vị

- **Cộng vòng**: $[4+2]$ (tổng 6 electron, tức $4n+2$) được phép nhiệt theo kiểu suprafacial - suprafacial — đó chính là Diels - Alder, phản ứng tạo vòng quan trọng nhất trong tổng hợp hữu cơ. $[2+2]$ (4 electron) bị cấm nhiệt nhưng được phép quang hoá; vì thế dime hoá alkene chỉ xảy ra dưới ánh sáng.
- **Sigmatropic $[i,j]$**: đếm tổng số electron tham gia ($i+j-1$ cặp... thực dụng hơn là đếm số electron trong trạng thái chuyển tiếp vòng). $[3,3]$ có 6 electron nên được phép nhiệt, suprafacial trên cả hai mảnh — giải thích trạng thái chuyển tiếp ghế của Cope và Claisen. $[1,5]$ chuyển hydro (6 electron) được phép nhiệt suprafacial; $[1,3]$ (4 electron) thì không, phải antarafacial hoặc quang hoá.

## Quy tắc tổng quát

Một cách phát biểu gọn cho mọi trường hợp: phản ứng **được phép nhiệt** khi tổng số thành phần $(4q+2)_s$ cộng $(4r)_a$ là **lẻ**. Với đường quang hoá, điều kiện là chẵn.

## Ranh giới

"Cấm" nghĩa là **cấm theo đối xứng đồng bộ**, không phải không xảy ra. Phản ứng bị cấm vẫn có thể đi vòng qua cơ chế từng bước (gốc tự do hoặc lưỡng cực), chỉ là chậm hơn nhiều và **mất tính đặc thù lập thể**. Chính sự mất đặc thù đó là dấu hiệu thực nghiệm cho biết phản ứng không còn là pericyclic thực sự.

**Lỗi thường gặp:**
- Đếm tổng số electron $\pi$ của cả phân tử thay vì số electron **tham gia** trạng thái chuyển tiếp vòng — sai vì chỉ hệ liên hợp trực tiếp tham gia mới được tính; một liên kết đôi biệt lập ở xa không đổi kết quả.
- Cho rằng phản ứng 'bị cấm' thì không xảy ra được — sai vì cấm chỉ áp dụng cho đường **đồng bộ có đối xứng**; phản ứng vẫn có thể đi từng bước qua gốc tự do hoặc lưỡng cực, nhưng khi đó mất tính đặc thù lập thể.
- Dùng cùng một quy tắc cho phản ứng nhiệt và phản ứng quang hoá — sai vì kích thích đưa electron lên obitan có đối xứng ngược, làm đảo hoàn toàn kết luận; đây chính là điểm mấu chốt của lí thuyết Woodward - Hoffmann.
- Nhầm suprafacial/antarafacial với con quay/đối xứng gương — sai vì cặp thuật ngữ đầu mô tả phía nào của hệ $\pi$ được sử dụng trong cộng vòng và chuyển vị, còn cặp sau riêng cho chiều quay của hai đầu mạch trong phản ứng electrocyclic.

<sub>`lesson.chemistry.huu-co-nang-cao.phan-ung-vong-hoa-woodward-hoffmann`</sub>

---

### 6. Hoá học kim loại chuyển tiếp trong tổng hợp: phản ứng ghép chéo
*Transition metals in synthesis: cross-coupling reactions* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Nhận diện được các bước cơ bản trong chu trình xúc tác cơ kim
- Trình bày được chu trình xúc tác của các phản ứng ghép chéo dùng palladium
- Đánh giá được vai trò của phối tử phosphine qua góc nón và tham số điện tử Tolman

## Vì sao kim loại chuyển tiếp thay đổi tổng hợp hữu cơ

Ghép hai carbon lai hoá $sp^2$ với nhau bằng phương pháp cổ điển rất khó. Palladium làm được điều đó ở điều kiện êm dịu, dung nạp nhiều nhóm chức, và với lượng xúc tác dưới 1 %. Ba giải Nobel 2010 (Heck, Negishi, Suzuki) ghi nhận tầm ảnh hưởng của hướng này lên tổng hợp dược phẩm và vật liệu.

## Các bước cơ bản, dùng lại cho mọi chu trình

Đọc bất kì chu trình xúc tác cơ kim nào cũng chỉ cần vài bước sau, mỗi bước có "chữ kí" riêng về số electron, số oxi hoá và số phối trí:

- **Cộng oxi hoá**: số oxi hoá $+2$, số phối trí $+2$, số electron $+2$.
- **Chuyển kim loại**: số oxi hoá không đổi, số phối trí không đổi, số electron không đổi.
- **Chèn di trú** (1,2-insertion): số oxi hoá không đổi, số phối trí $-1$, số electron $-2$.
- **Tách $\beta$-hydride**: ngược lại với chèn.
- **Khử tách**: số oxi hoá $-2$, số phối trí $-2$, số electron $-2$.

Quy tắc 18 electron giúp kiểm tra tính hợp lí của từng trung gian.

## Chu trình ghép chéo chuẩn

$$\mathrm{L_nPd(0)} \xrightarrow{\ \mathrm{R-X}\ } \mathrm{L_nPd(II)(R)(X)} \xrightarrow{\ \mathrm{R'-M}\ } \mathrm{L_nPd(II)(R)(R')} \xrightarrow{\ \ } \mathrm{R-R'} + \mathrm{L_nPd(0)}$$

Chỉ đổi nguồn $\mathrm{R'-M}$ là ra các phản ứng mang tên khác nhau: **Suzuki** (boronic acid, cần base để tạo boronate), **Stille** (organostannane, độc), **Negishi** (organozinc, hoạt tính cao), **Sonogashira** (alkyne đầu mạch, đồng xúc tác Cu), **Kumada** (Grignard, kém dung nạp nhóm chức), **Buchwald - Hartwig** (amine, tạo liên kết C–N).

**Heck** thì khác: không có chuyển kim loại; sau cộng oxi hoá là **chèn di trú** alkene rồi **tách $\beta$-hydride**, nên sản phẩm là alkene thế chứ không phải ghép trực tiếp.

## Phối tử quyết định thành bại

Phối tử phosphine được mô tả bằng hai tham số Tolman:
- **Góc nón** $\theta$: cồng kềnh lớn (P(t-Bu)$_3$: 182°) đẩy nhanh **khử tách** và giữ Pd ở dạng phối trí thấp, hoạt động hơn cho **cộng oxi hoá** của aryl chloride vốn trơ.
- **Tham số điện tử** $\nu$ (từ $\tilde\nu_{\mathrm{CO}}$ của Ni(CO)$_3$L): phosphine giàu electron làm Pd(0) giàu electron hơn, thúc đẩy cộng oxi hoá.

Đây là lí do các phối tử Buchwald (SPhos, XPhos) — vừa cồng kềnh vừa giàu electron — mở rộng được phạm vi phản ứng sang aryl chloride rẻ tiền.

## Chẩn đoán khi thất bại

Chất nền alkyl có hydro ở vị trí $\beta$ dễ bị **tách $\beta$-hydride** cạnh tranh, phá chu trình — đó là lí do ghép chéo alkyl khó hơn aryl nhiều.

**Lỗi thường gặp:**
- Bắt đầu chu trình từ phức 18 electron bão hoà — sai vì phức bão hoà không còn chỗ trống để cộng oxi hoá; luôn phải có bước phân li phối tử tạo tiểu phân không bão hoà trước.
- Nghĩ chuyển kim loại làm thay đổi số oxi hoá của Pd — sai vì cả nhóm rời và nhóm đến đều là phối tử anion X; số oxi hoá, số phối trí và số electron đều giữ nguyên, đó chính là chữ kí nhận dạng bước này.
- Coi base trong phản ứng Suzuki chỉ để trung hoà acid sinh ra — sai vì vai trò chính của nó là hoạt hoá boron thành boronate mang điện âm; không có base thì chuyển kim loại quá chậm và phản ứng không chạy dù không có acid nào cần trung hoà.
- Cho rằng phối tử càng cồng kềnh thì càng tốt — sai vì cồng kềnh quá mức cản trở chính bước chuyển kim loại và làm phức kém bền; thiết kế phối tử là sự cân bằng giữa góc nón và tính cho electron, và tối ưu phụ thuộc bước nào đang là bước chậm.

<sub>`lesson.chemistry.huu-co-nang-cao.kim-loai-chuyen-tiep-ghep-cheo`</sub>

---

### 7. Phân tích retrosynthesis và thiết kế lộ trình tổng hợp
*Retrosynthetic analysis and synthetic route design* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Vận dụng được phép cắt mạch và khái niệm synthon, tác nhân tương đương
- Nhận diện được các quan hệ nhóm chức để chọn phép cắt phù hợp
- Đánh giá được một lộ trình tổng hợp theo số bước, hiệu suất tổng và tính hội tụ

## Tư duy ngược

Corey đặt nền cho phương pháp: thay vì mò mẫm từ nguyên liệu, ta bắt đầu từ **phân tử đích** và cắt ngược về các mảnh đơn giản hơn, cho tới khi chạm tới hoá chất thương mại. Mỗi phép cắt (kí hiệu $\Longrightarrow$) phải tương ứng với một phản ứng thuận **đã biết và đáng tin cậy**.

## Ba câu hỏi cho mỗi phép cắt

1. **Cắt ở đâu?** Ưu tiên cắt liên kết C–C ở vị trí có nhóm chức gần đó, cắt tại điểm phân nhánh, và cắt sao cho hai mảnh **gần bằng nhau** về kích thước.
2. **Synthon nào?** Cắt liên kết C–X dị li cho một mảnh dương và một mảnh âm; chọn cách phân cực **phù hợp với tính chất tự nhiên** của nhóm chức.
3. **Tác nhân tương đương là gì?** Synthon là ý tưởng; phải quy về hoá chất thật.

## Bảng quan hệ nhóm chức

Khoảng cách giữa hai nhóm chức quyết định phép cắt hợp lí:

- **1,3-dioxygenated** (aldol): cắt liên kết $\mathrm{C}\alpha$–$\mathrm{C}\beta$, lùi về hai hợp chất carbonyl.
- **1,5-dicarbonyl**: cắt kiểu Michael, lùi về enolate và enone.
- **1,2-dioxygenated**: dihydroxyl hoá alkene, hoặc mở epoxide.
- **1,4-dicarbonyl** và **1,6-dicarbonyl**: không khớp phân cực tự nhiên, cần **umpolung** (dithiane, chemistry của acyl anion) hoặc cắt vòng oxi hoá.

Nhận ra quan hệ 1,4 hoặc 1,6 là dấu hiệu phải đổi chiến lược — đây là kĩ năng phân biệt người mới với người có kinh nghiệm.

## Nhóm bảo vệ và thứ tự

Nhóm bảo vệ không tạo liên kết nào nhưng chiếm hai bước (bảo vệ và gỡ). Nguyên tắc: chỉ dùng khi không tìm được thứ tự phản ứng nào tránh được xung đột. Trước khi thêm nhóm bảo vệ, hãy thử **đổi thứ tự các bước**.

## Đánh giá một lộ trình

Hiệu suất tổng của $n$ bước tuyến tính là tích các hiệu suất: 10 bước với 80 % mỗi bước chỉ cho $0{,}8^{10}=10{,}7\,\%$. Vì thế:

- **Số bước tuyến tính dài nhất** quan trọng hơn tổng số bước.
- **Tổng hợp hội tụ** (ghép hai mảnh ở cuối) luôn thắng tổng hợp tuyến tính cùng số bước: hai nhánh 5 bước ghép lại cho hiệu suất cao hơn hẳn một chuỗi 10 bước.
- Các tiêu chí khác: tính sẵn có và giá của nguyên liệu, độ an toàn, khả năng nâng quy mô, và **hiệu quả nguyên tử**.

## Kiểm tra lại chiều thuận

Sau khi vẽ xong sơ đồ ngược, luôn viết lại theo chiều thuận và kiểm tra từng bước: có phản ứng phụ nào cạnh tranh không? có nhóm chức nào không sống sót qua điều kiện đó không? có tâm bất đối nào bị racemic hoá không? Một lộ trình đẹp trên giấy mà bỏ qua các câu hỏi này thường thất bại ngay ở bước đầu tiên trong phòng thí nghiệm.

**Lỗi thường gặp:**
- Vẽ phép cắt mà không có phản ứng thuận tương ứng — sai vì retrosynthesis không phải trò chơi cắt hình; mỗi mũi tên ngược phải là một phản ứng đã được kiểm chứng, nếu không lộ trình chỉ tồn tại trên giấy.
- Cắt liên kết ở xa mọi nhóm chức — sai vì hoá học tạo liên kết C–C hầu như luôn cần một nhóm chức để hoạt hoá; cắt ở giữa một chuỗi alkane trơ để lại hai mảnh không phản ứng được với nhau.
- Cố ghép quan hệ 1,4-dicarbonyl bằng phân cực thông thường — sai vì phân cực tự nhiên của hai nhóm carbonyl xung đột nhau ở khoảng cách đó; phải dùng umpolung (dithiane) hoặc cắt vòng oxi hoá.
- Đánh giá lộ trình bằng tổng số bước thay vì số bước **tuyến tính dài nhất** — sai vì tổng hợp hội tụ có thể có nhiều bước hơn mà hiệu suất tổng cao hơn hẳn, do các nhánh được thực hiện song song.

<sub>`lesson.chemistry.huu-co-nang-cao.phan-tich-retrosynthesis`</sub>

---

## Unit 7: Hoá vô cơ nâng cao

### 1. Đối xứng phân tử và nhóm điểm
*Molecular symmetry and point groups* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Nhận diện được các yếu tố đối xứng và phép đối xứng của một phân tử
- Gán được nhóm điểm cho phân tử bằng sơ đồ quyết định
- Vận dụng được đối xứng để dự đoán tính phân cực, tính bất đối và số vạch phổ hoạt động

## Đối xứng: ngôn ngữ chung của phổ học và liên kết

Nhiều kết luận trong hoá học vô cơ — phức nào có màu, phân tử nào phân cực, dao động nào hoạt động IR — không cần tính toán, chỉ cần **đối xứng**. Học nhóm điểm là học cách đọc những kết luận đó trực tiếp từ hình dạng phân tử.

## Năm loại phép đối xứng

- $E$: phép đồng nhất (luôn có).
- $C_n$: quay $360°/n$ quanh một trục. Trục có $n$ lớn nhất là **trục chính**.
- $\sigma$: phản chiếu qua mặt phẳng. Phân loại: $\sigma_h$ (vuông góc trục chính), $\sigma_v$ (chứa trục chính), $\sigma_d$ (chứa trục chính và chia đôi góc giữa hai trục $C_2$).
- $i$: nghịch đảo qua tâm.
- $S_n$: quay rồi phản chiếu.

## Gán nhóm điểm

Đi theo sơ đồ quyết định:
1. Phân tử thẳng? Có $i$ thì $D_{\infty h}$, không thì $C_{\infty v}$.
2. Có nhiều trục $C_n$ bậc cao ($n>2$)? Nhóm khối: $T_d$, $O_h$, $I_h$.
3. Tìm trục chính $C_n$. Có $n$ trục $C_2$ vuông góc với nó? Nếu có thì họ $D$; nếu không thì họ $C$.
4. Có $\sigma_h$? $\Rightarrow D_{nh}$ hoặc $C_{nh}$. Có $n$ mặt $\sigma_v/\sigma_d$? $\Rightarrow D_{nd}$ hoặc $C_{nv}$. Không có mặt nào? $\Rightarrow D_n$ hoặc $C_n$.

Ví dụ: H$_2$O là $C_{2v}$; NH$_3$ là $C_{3v}$; BF$_3$ là $D_{3h}$; CH$_4$ là $T_d$; SF$_6$ là $O_h$; benzene là $D_{6h}$; ferrocene xen kẽ là $D_{5d}$.

## Ba kết luận đọc ngay từ nhóm điểm

**Phân cực**: phân tử chỉ có momen lưỡng cực vĩnh cửu nếu nó thuộc $C_1$, $C_s$, $C_n$ hoặc $C_{nv}$. Mọi nhóm có $i$, có $\sigma_h$ hoặc thuộc họ $D$ đều **không phân cực**. Vì thế CO$_2$ ($D_{\infty h}$) không phân cực còn H$_2$O ($C_{2v}$) thì có.

**Bất đối**: phân tử bất đối (có đối quang) khi và chỉ khi nó **không** có $S_n$ nào, kể cả $\sigma$ ($=S_1$) và $i$ ($=S_2$). Đây là tiêu chuẩn chặt chẽ hơn nhiều so với "có carbon bất đối".

**Phổ**: dao động hoạt động IR khi biến đổi theo cùng biểu diễn với $x$, $y$ hoặc $z$; hoạt động Raman khi biến đổi như một tích bậc hai ($x^2$, $xy$, ...). Với nhóm có tâm đối xứng, hai tập này rời nhau hoàn toàn — **quy tắc loại trừ lẫn nhau**.

## Vì sao điều này quan trọng cho phức chất

Đối xứng bát diện $O_h$ có tâm đối xứng, nên chuyển dời d–d bị cấm Laporte và phức chỉ có màu nhạt. Phức tứ diện $T_d$ **không** có tâm đối xứng, nên chuyển dời d–d được phép hơn và phức tứ diện luôn có màu đậm hơn phức bát diện cùng kim loại. Chỉ một chi tiết đối xứng đã giải thích được quan sát định lượng đó.

**Lỗi thường gặp:**
- Kết luận phân tử bất đối chỉ dựa vào việc có 'carbon bất đối' — sai vì tiêu chuẩn đúng là **không có trục $S_n$ nào**; hợp chất meso có $\sigma$ nên không bất đối dù có hai tâm bất đối, còn nhiều phân tử không có tâm bất đối nào vẫn bất đối (allene, biphenyl bị cản quay).
- Quên rằng $\sigma = S_1$ và $i = S_2$ — dẫn tới bỏ sót khi kiểm tra tính bất đối; chỉ cần một mặt phẳng gương là đủ để phân tử trùng với ảnh gương của nó.
- Cho rằng mọi phân tử có phối tử khác nhau đều phân cực — sai vì sự sắp xếp đối xứng có thể triệt tiêu các vectơ momen; trans-$[\mathrm{Pt(NH_3)_2Cl_2}]$ có bốn liên kết phân cực nhưng tổng vectơ bằng 0.
- Xác định trục chính là trục 'trông có vẻ dài nhất' — sai vì trục chính là trục $C_n$ có $n$ **lớn nhất**, xác định bằng bậc quay chứ không bằng hình dạng trực quan.

<sub>`lesson.chemistry.vo-co-nang-cao.doi-xung-phan-tu-va-nhom-diem`</sub>

---

### 2. Thuyết trường tinh thể và thuyết trường phối tử
*Crystal field and ligand field theories* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được sự tách mức d trong trường bát diện và trường tứ diện
- Tính được năng lượng bền hoá trường tinh thể và dự đoán cấu hình spin cao hay spin thấp
- Phân tích được vai trò của phối tử pi-cho và pi-nhận trong dãy quang phổ hoá

## Từ tĩnh điện tới obitan

Thuyết trường tinh thể coi phối tử là điện tích âm điểm. Trong trường bát diện, hai obitan trỏ **thẳng vào** phối tử ($d_{z^2}$, $d_{x^2-y^2}$, tập $e_g$) bị đẩy lên; ba obitan trỏ **vào giữa** ($d_{xy}$, $d_{yz}$, $d_{xz}$, tập $t_{2g}$) hạ xuống. Bảo toàn trọng tâm cho

$$E(e_g)=+0{,}6\Delta_o,\qquad E(t_{2g})=-0{,}4\Delta_o$$

Trường tứ diện đảo thứ tự và tách yếu hơn nhiều: $\Delta_t\approx\tfrac49\Delta_o$ — vì chỉ có 4 phối tử và không obitan nào trỏ thẳng vào chúng. Hệ quả: **hầu như mọi phức tứ diện đều spin cao**.

## Spin cao hay spin thấp

So $\Delta_o$ với năng lượng ghép đôi $P$:
- $\Delta_o < P$: electron thà lên $e_g$ còn hơn ghép đôi $\Rightarrow$ **spin cao**.
- $\Delta_o > P$: **spin thấp**.

Chỉ cấu hình $d^4$ đến $d^7$ mới có hai khả năng; $d^1$–$d^3$ và $d^8$–$d^{10}$ chỉ có một cách điền.

Ba yếu tố làm $\Delta_o$ lớn: kim loại ở **chu kì 4d, 5d** (tăng khoảng 30–50 % mỗi chu kì, nên phức 4d/5d gần như luôn spin thấp); **số oxi hoá cao**; và phối tử mạnh.

## Dãy quang phổ hoá và lí do của nó

$$\mathrm{I^-<Br^-<Cl^-<F^-<OH^-<H_2O<NH_3<en<bpy<CN^-<CO}$$

Thuyết tĩnh điện thuần tuý **không giải thích nổi** dãy này: tại sao CO trung hoà lại mạnh hơn F$^-$ mang điện? Câu trả lời cần thuyết **trường phối tử**, tức MO:

- **Phối tử pi-cho** (halide, OH$^-$, O$^{2-}$): obitan p đầy tương tác với $t_{2g}$, **đẩy $t_{2g}$ lên**, làm $\Delta_o$ **giảm**.
- **Phối tử pi-nhận** (CO, CN$^-$, bpy, phosphine): obitan $\pi^*$ trống nhận electron từ $t_{2g}$, **hạ $t_{2g}$ xuống**, làm $\Delta_o$ **tăng mạnh**.

Đây cũng là lí do CO ổn định kim loại ở số oxi hoá thấp: nó rút bớt mật độ electron dư qua liên kết ngược (back-bonding), điều thấy được qua $\tilde\nu_{\mathrm{CO}}$ giảm từ 2143 cm$^{-1}$ (CO tự do) xuống 1900–2000 cm$^{-1}$ trong phức.

## Jahn - Teller

Trạng thái điện tử suy biến của phân tử không thẳng **không bền**; phân tử biến dạng để hạ đối xứng và tách suy biến. Hiệu ứng mạnh khi suy biến nằm ở $e_g$ (trỏ thẳng vào phối tử): cấu hình $d^9$ (Cu$^{2+}$) và $d^4$ spin cao (Mn$^{3+}$) cho biến dạng kéo dài trục rõ rệt — đó là lí do hầu hết phức Cu(II) có bốn liên kết ngắn và hai liên kết dài.

**Lỗi thường gặp:**
- Quên cộng phần năng lượng ghép đôi phụ trội khi tính CFSE của phức spin thấp — sai vì spin thấp phải trả giá bằng việc ép thêm các cặp electron; bỏ qua $nP$ làm phóng đại độ bền của phức spin thấp.
- Dự đoán phức tứ diện spin thấp — gần như luôn sai vì $\Delta_t\approx\tfrac49\Delta_o$, hầu như không bao giờ vượt năng lượng ghép đôi; các trường hợp ngoại lệ cực hiếm và đều liên quan phối tử pi-nhận rất mạnh.
- Giải thích dãy quang phổ hoá bằng điện tích phối tử — sai vì CO trung hoà lại mạnh hơn F$^-$ mang điện; nguyên nhân thật là liên kết $\pi$, đòi hỏi thuyết trường phối tử chứ không phải mô hình tĩnh điện.
- Áp dụng Jahn - Teller cho mọi cấu hình có suy biến — về nguyên tắc đúng nhưng biến dạng chỉ **đáng kể** khi suy biến nằm ở $e_g$ (obitan trỏ thẳng vào phối tử); suy biến ở $t_{2g}$ cho biến dạng rất nhỏ, thường không quan sát được.

<sub>`lesson.chemistry.vo-co-nang-cao.truong-tinh-the-va-truong-phoi-tu`</sub>

---

### 3. Phổ điện tử của phức chất và giản đồ Tanabe - Sugano
*Electronic spectra of complexes and Tanabe - Sugano diagrams* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Phân loại được các dải hấp thụ d–d và dải chuyển điện tích theo cường độ
- Sử dụng được giản đồ Tanabe - Sugano để xác định $\Delta_o$ và tham số Racah $B$
- Giải thích được hiệu ứng nephelauxetic và ý nghĩa của nó về độ cộng hoá trị

## Đọc cường độ trước, đọc vị trí sau

Cường độ phân loại ngay bản chất dải hấp thụ:

- $\varepsilon < 1$: chuyển dời d–d **cấm cả spin lẫn Laporte** (ví dụ $[\mathrm{Mn(H_2O)_6}]^{2+}$, $d^5$ spin cao — nên dung dịch Mn(II) gần như không màu).
- $\varepsilon \approx 1$–100: d–d cấm Laporte nhưng cho phép spin, được mở nhờ ghép vibronic. Đây là màu nhạt của đa số phức bát diện.
- $\varepsilon \approx 100$–1000: d–d trong phức **tứ diện** (không có tâm đối xứng nên Laporte không áp dụng).
- $\varepsilon > 10^3$: **chuyển điện tích**. MnO$_4^-$ ($\varepsilon\approx 2\times10^3$) và các phức Fe(III)-phenolate màu đậm đều thuộc loại này.

Vì thế màu đậm rực rỡ hầu như luôn là chuyển điện tích, không phải d–d.

## Tại sao cần Tanabe - Sugano

Với $d^1$, chỉ có một dải và $\Delta_o$ đọc trực tiếp. Từ $d^2$ trở đi, **lực đẩy electron - electron** làm nhiều số hạng cùng tồn tại, và vị trí các dải phụ thuộc **hai** tham số: $\Delta_o$ và $B$. Giản đồ Tanabe - Sugano vẽ $E/B$ theo $\Delta_o/B$, cho phép rút cả hai từ tỉ số của hai dải quan sát được.

Cách dùng: đo tỉ số $\tilde\nu_2/\tilde\nu_1$, tra trên giản đồ để tìm $\Delta_o/B$ tương ứng, đọc $E_1/B$ tại đó, rồi tính $B=\tilde\nu_1/(E_1/B)$ và $\Delta_o = (\Delta_o/B)\times B$.

Đặc điểm cần lưu ý: giản đồ của $d^4$–$d^7$ có **đường thẳng đứng** đánh dấu điểm chuyển spin cao sang spin thấp; bên trái là spin cao, bên phải là spin thấp, và số hạng cơ bản đổi hẳn tại đó.

## Nephelauxetic: thước đo độ cộng hoá trị

Ion kim loại tự do có $B_0$ xác định; trong phức, $B < B_0$. Tỉ số

$$\beta=\frac{B_{\text{phức}}}{B_{\text{tự do}}}$$

giảm theo dãy $\mathrm{F^->H_2O>NH_3>Cl^->CN^->Br^->I^-}$. Ý nghĩa vật lí: electron d giải toả ra phối tử nên "đám mây nở ra" (nephelauxetic nghĩa là "làm nở đám mây"), làm chúng đẩy nhau yếu đi. $\beta$ nhỏ $\Rightarrow$ liên kết **cộng hoá trị nhiều hơn**.

Chú ý dãy nephelauxetic **khác** dãy quang phổ hoá: hai dãy đo hai thứ khác nhau ($\Delta_o$ đo tách trường, $\beta$ đo độ cộng hoá trị), nên I$^-$ đứng cuối cả hai nhưng vì lí do khác nhau.

## Cảnh báo khi phân tích

Dải d–d thường rộng và có thể chồng lấp; dải chuyển điện tích mạnh có thể che khuất hoàn toàn dải d–d yếu. Ngoài ra biến dạng Jahn - Teller làm dải bị tách hoặc có vai — nếu ép khớp một dải bất đối xứng bằng một đường Gauss duy nhất thì $\Delta_o$ thu được sẽ sai lệch.

**Lỗi thường gặp:**
- Đọc $\Delta_o$ trực tiếp từ dải hấp thụ thấp nhất cho mọi cấu hình $d^n$ — sai vì chỉ $d^1$, $d^4$ spin cao, $d^6$ spin cao, $d^9$ và $d^8$ mới có quan hệ đơn giản; với $d^2$, $d^3$, $d^7$ thì lực đẩy electron làm dịch các số hạng và bắt buộc phải dùng giản đồ Tanabe - Sugano.
- Kết luận phức không màu thì không có electron d — sai vì $d^5$ spin cao (Mn$^{2+}$) có 5 electron d nhưng mọi chuyển dời d–d đều bị cấm cả spin lẫn Laporte, nên $\varepsilon$ dưới 1 và dung dịch gần như không màu.
- Nhầm dãy nephelauxetic với dãy quang phổ hoá — sai vì hai dãy đo hai đại lượng khác nhau; ví dụ CN$^-$ đứng gần cuối dãy quang phổ hoá theo nghĩa $\Delta_o$ lớn nhất, nhưng vị trí của nó trong dãy nephelauxetic phản ánh độ cộng hoá trị chứ không phải độ mạnh trường.
- Gán mọi dải mạnh trong phổ phức là d–d — sai vì $\varepsilon > 10^3$ hầu như chắc chắn là chuyển điện tích; dùng dải đó để tính $\Delta_o$ sẽ cho giá trị vô nghĩa.

<sub>`lesson.chemistry.vo-co-nang-cao.pho-dien-tu-cua-phuc`</sub>

---

### 4. Từ tính của phức chất kim loại chuyển tiếp
*Magnetic properties of transition metal complexes* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Phân biệt được nghịch từ, thuận từ, sắt từ và phản sắt từ ở mức phân tử và mức chất rắn
- Tính được momen từ hiệu dụng theo công thức spin thuần tuý và so với thực nghiệm
- Xác định được số electron độc thân từ độ cảm từ đo bằng định luật Curie

## Đo từ tính để đếm electron độc thân

Chất **nghịch từ** (mọi electron ghép đôi) bị đẩy nhẹ ra khỏi từ trường; chất **thuận từ** (có electron độc thân) bị hút vào. Vì mỗi electron độc thân đóng góp một lượng xác định, phép đo từ tính là cách đếm trực tiếp — và nhờ đó xác định cấu hình spin cao hay spin thấp mà không cần phổ.

## Công thức spin thuần tuý

$$\mu_{so}=\sqrt{n(n+2)}\ \mu_B$$

Bảng cần thuộc: $n=1\to1{,}73$; $2\to2{,}83$; $3\to3{,}87$; $4\to4{,}90$; $5\to5{,}92\ \mu_B$.

Từ thực nghiệm, độ cảm từ mol theo định luật Curie cho

$$\mu_{eff}=2{,}828\sqrt{\chi_M T}\ \ \mu_B$$

với $\chi_M$ tính bằng cm³/mol. So $\mu_{eff}$ với bảng trên là ra ngay $n$.

## Vì sao "spin thuần tuý" lại đủ tốt

Về nguyên tắc momen từ có cả đóng góp obitan. Nhưng trong trường phối tử bát diện, đóng góp obitan bị **dập tắt** với hầu hết cấu hình: momen obitan chỉ tồn tại khi có thể quay một obitan bị chiếm thành một obitan trống **tương đương**, điều bị trường phối tử ngăn cản.

Ngoại lệ đáng chú ý: cấu hình có $t_{2g}$ chiếm không đối xứng như $d^1$, $d^2$, $d^6$ và $d^7$ spin cao giữ lại một phần đóng góp obitan, nên $\mu_{eff}$ **cao hơn** giá trị spin thuần tuý (Co$^{2+}$ octahedral: đo 4,7–5,2 so với 3,87 tính được). Với ion **lanthanide** thì công thức spin thuần tuý sai hoàn toàn: 4f nằm sâu bên trong, không bị trường phối tử ảnh hưởng, nên phải dùng $\mu = g_J\sqrt{J(J+1)}$.

## Từ tính tập thể trong chất rắn

Trong chất rắn, các momen có thể ghép với nhau:
- **Sắt từ**: momen song song, từ hoá tự phát dưới nhiệt độ Curie.
- **Phản sắt từ**: momen đối song, triệt tiêu; $\chi$ đi qua cực đại ở nhiệt độ Néel.
- **Ferri từ**: momen đối song nhưng không bằng nhau nên còn dư — magnetite Fe$_3$O$_4$ là ví dụ.

Dấu hiệu phân biệt: chất thuận từ đơn thuần tuân theo Curie ($\chi \propto 1/T$) trên toàn dải; ghép tập thể làm đồ thị $1/\chi$ theo $T$ cắt trục nhiệt độ ở giá trị khác 0 (định luật Curie - Weiss).

## Chuyển spin: nơi $\Delta_o \approx P$

Khi hai trạng thái spin gần nhau về năng lượng, nhiệt độ quyết định. Nhiều phức Fe(II) với phối tử nitơ chuyển từ spin thấp (nghịch từ, ở nhiệt độ thấp) sang spin cao (thuận từ, ở nhiệt độ cao). Hiện tượng này thuận nghịch, đôi khi có trễ, và đang được nghiên cứu cho vật liệu chuyển mạch và lưu trữ dữ liệu phân tử.

**Lỗi thường gặp:**
- Dùng công thức spin thuần tuý cho ion lanthanide — sai vì obitan 4f nằm sâu, được che chắn khỏi trường phối tử nên momen obitan **không** bị dập tắt; phải dùng $\mu = g_J\sqrt{J(J+1)}$ với $J$ từ quy tắc Hund.
- Kết luận cấu hình sai khi $\mu_{eff}$ đo được lớn hơn giá trị spin thuần tuý — sai vì các cấu hình $t_{2g}$ chiếm không đối xứng ($d^1$, $d^2$, $d^6$, $d^7$ spin cao) vốn dĩ cho giá trị cao hơn; phải so với **khoảng** thực nghiệm điển hình chứ không so với một con số duy nhất.
- Cho rằng chất có electron độc thân thì bị nam châm hút mạnh như sắt — sai vì thuận từ yếu hơn sắt từ hàng nghìn lần; sắt từ đòi hỏi các momen ghép song song theo miền, một hiện tượng tập thể của chất rắn chứ không phải tính chất của phân tử đơn lẻ.
- Bỏ qua hiệu chỉnh nghịch từ của lõi và của phối tử khi tính $\chi_M$ — sai vì mọi electron ghép đôi đều đóng góp nghịch từ; với phức có phối tử hữu cơ lớn, bỏ qua hiệu chỉnh Pascal làm $\mu_{eff}$ thấp đi vài phần trăm.

<sub>`lesson.chemistry.vo-co-nang-cao.tu-tinh-cua-phuc`</sub>

---

### 5. Hoá học organometallic và quy tắc 18 electron
*Organometallic chemistry and the 18-electron rule* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Xác định được số electron hoá trị của phức cơ kim bằng cả phương pháp ion và phương pháp trung hoà
- Giải thích được cơ sở và các ngoại lệ của quy tắc 18 electron
- Vận dụng được quy tắc Wade và khái niệm tương tự isolobal để phân tích cluster

## Vì sao lại là 18

Kim loại chuyển tiếp có chín obitan hoá trị: năm $d$, một $s$, ba $p$. Lấp đầy cả chín cần 18 electron — cấu hình khí hiếm của chu kì đó. Quy tắc 18 electron vì thế là phiên bản kim loại chuyển tiếp của quy tắc bát tử.

## Hai cách đếm, một kết quả

**Phương pháp trung hoà** (donor pair): coi mọi phối tử trung hoà, đếm electron mà nó cho.
- 2 electron: CO, PR$_3$, NH$_3$, alkene ($\eta^2$) — phối tử kiểu L, cho nguyên một cặp electron.
- 1 electron: H, halogen, alkyl, $\eta^1$-allyl — phối tử kiểu X, vì ở dạng trung hoà mỗi phối tử này chỉ mang một electron độc thân.
- 3 electron: $\eta^3$-allyl, NO thẳng.
- 5 electron: $\eta^5$-Cp.
- 6 electron: $\eta^6$-arene.
Điện tích tổng của phức được cộng/trừ vào cuối.

**Phương pháp ion**: coi các phối tử X là anion; kim loại mang số oxi hoá tương ứng, đếm electron d của ion đó rồi cộng 2 electron cho mỗi cặp phối tử cho.

Hai cách luôn cho cùng tổng. Ví dụ ferrocene $\mathrm{Fe(\eta^5\text{-}C_5H_5)_2}$: trung hoà cho $8 + 2\times5 = 18$; ion cho $\mathrm{Fe^{2+}}$ ($d^6$) $+ 2\times6 = 18$.

## Khi 18 không đúng

Quy tắc mạnh nhất với kim loại **giữa dãy chuyển tiếp, số oxi hoá thấp, phối tử pi-nhận mạnh** — tức đúng chỗ obitan $d$, $s$, $p$ gần nhau về năng lượng.

Ba nhóm ngoại lệ có hệ thống:
- **Phức vuông phẳng $d^8$** (Rh(I), Ir(I), Pd(II), Pt(II), Au(III)): bền ở **16 electron**, vì obitan $p_z$ nằm quá cao nên không được dùng. Chính chỗ trống đó cho phép cộng oxi hoá — nền tảng của xúc tác đồng thể.
- **Kim loại đầu dãy** (Ti, Zr, Ta) thường dưới 18 do cản trở không gian: không đủ chỗ gắn phối tử.
- **Kim loại cuối dãy và phức với phối tử cho thuần** (không có pi-nhận) có thể vượt 18 vì các electron d dư nằm trên obitan gần như phi liên kết.

## Cluster: quy tắc Wade

Với cluster borane và cluster cơ kim, đếm **cặp electron khung** $b$ so với số đỉnh $n$:
- $b = n+1$: **closo** (đa diện kín).
- $b = n+2$: **nido** (mất một đỉnh).
- $b = n+3$: **arachno** (mất hai đỉnh).

Ví dụ $\mathrm{B_6H_6^{2-}}$: 7 cặp khung, 6 đỉnh $\Rightarrow$ closo bát diện.

## Isolobal: cầu nối hai thế giới

Fragment $\mathrm{Mn(CO)_5}$ (17 electron) có một obitan biên chứa một electron — giống hệt $\mathrm{CH_3}$. Vì thế $\mathrm{Mn_2(CO)_{10}}$ tồn tại như ethane, và $\mathrm{CH_3Mn(CO)_5}$ cũng vậy. Tương tự $\mathrm{Fe(CO)_4}\leftrightarrow \mathrm{CH_2}$ và $\mathrm{Co(CO)_3}\leftrightarrow \mathrm{CH}$. Hoffmann dùng ý tưởng này để **dự đoán** các cluster hỗn hợp trước khi chúng được tổng hợp.

**Lỗi thường gặp:**
- Trộn lẫn phương pháp ion và phương pháp trung hoà trong cùng một phép đếm — sai vì mỗi phương pháp có quy ước riêng về việc gán electron cho phối tử X; trộn lẫn thường làm sai lệch 1–2 electron cho mỗi phối tử anion.
- Coi mọi phức không đạt 18 electron là không bền — sai vì phức vuông phẳng $d^8$ bền ở 16 electron do obitan $p_z$ không tham gia; chính chỗ trống đó là nền tảng của hoá học xúc tác đồng thể.
- Đếm $\eta^5$-Cp là 6 electron vì có 5 carbon và 1 điện tích âm — sai nếu đang dùng phương pháp trung hoà, nơi Cp cho 5 electron; giá trị 6 chỉ đúng khi coi nó là anion $\mathrm{Cp^-}$ trong phương pháp ion, và khi đó kim loại phải mang số oxi hoá tương ứng.
- Quên trừ số cặp electron liên kết ngoài khung khi áp dụng quy tắc Wade — sai vì chỉ **cặp electron khung** mới quyết định kiểu cấu trúc; mỗi đỉnh B–H đã dùng một cặp cho liên kết ngoài, phải loại trước khi so với $n+1$, $n+2$, $n+3$.

<sub>`lesson.chemistry.vo-co-nang-cao.organometallic-va-quy-tac-18-electron`</sub>

---

### 6. Hoá học chất rắn và cấu trúc tinh thể
*Solid state chemistry and crystal structures* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Mô tả được các kiểu xếp chặt và tính được độ đặc khít cùng số phối trí
- Vận dụng được định luật Bragg để xác định thông số mạng từ dữ liệu nhiễu xạ
- Tính được năng lượng mạng lưới bằng chu trình Born - Haber và bằng phương trình Born - Landé

## Xếp chặt và các hốc

Xếp chặt cầu cứng cho hai kiểu chính, cả hai đều có độ đặc khít **74,05 %** và số phối trí 12: lập phương tâm mặt (fcc, xếp ABC) và lục phương xếp chặt (hcp, xếp ABAB). Lập phương tâm khối (bcc) kém khít hơn (68,02 %, số phối trí 8), còn lập phương đơn giản chỉ 52,36 %.

Trong mạng xếp chặt có hai loại hốc: **tứ diện** (2 hốc mỗi cầu) và **bát diện** (1 hốc mỗi cầu). Cấu trúc của hầu hết hợp chất ion đọc được theo sơ đồ "anion xếp chặt, cation chiếm hốc":
- NaCl: anion fcc, cation chiếm **toàn bộ** hốc bát diện.
- ZnS (blende): anion fcc, cation chiếm **một nửa** hốc tứ diện.
- CaF$_2$ (fluorite): cation fcc, anion chiếm toàn bộ hốc tứ diện.

**Tỉ số bán kính** $r_+/r_-$ dự đoán số phối trí: dưới 0,225 là 4 (tứ diện), 0,225–0,414 là 4, 0,414–0,732 là 6 (bát diện), trên 0,732 là 8 (lập phương). Quy tắc này chỉ là hướng dẫn thô — nó thất bại với nhiều hợp chất có tính cộng hoá trị đáng kể.

## Nhiễu xạ: nhìn thấy mạng

$$n\lambda=2d\sin\theta$$

Với mạng lập phương, $d_{hkl}=\dfrac{a}{\sqrt{h^2+k^2+l^2}}$. Kết hợp hai công thức cho phép gán chỉ số Miller cho từng vạch nhiễu xạ và rút hằng số mạng $a$.

Điều kiện tắt hệ thống là công cụ nhận dạng kiểu mạng: fcc chỉ cho phản xạ khi $h$, $k$, $l$ **cùng chẵn hoặc cùng lẻ**; bcc chỉ khi $h+k+l$ **chẵn**. Nhìn dãy các vạch đầu tiên là biết ngay kiểu mạng.

Từ $a$ và số đơn vị cấu trúc $Z$ trong ô mạng, khối lượng riêng tính được:

$$\rho=\frac{ZM}{N_Aa^3}$$

So $\rho$ tính với $\rho$ đo là phép kiểm tra hữu ích — chênh lệch báo hiệu có khuyết tật hoặc lỗ trống trong mạng.

## Năng lượng mạng lưới: hai đường tiếp cận

**Thực nghiệm (Born - Haber)**: dùng định luật Hess ghép enthalpy tạo thành, thăng hoa, phân li, ion hoá và ái lực electron để suy ra $U$.

**Lí thuyết (Born - Landé)**:

$$U=-\frac{N_AAz_+z_-e^2}{4\pi\varepsilon_0 r_0}\left(1-\frac{1}{n}\right)$$

với $A$ là hằng số Madelung (NaCl: 1,748; CsCl: 1,763; blende: 1,638) và $n$ là số mũ Born. Phương trình **Kapustinskii** cho ước lượng nhanh khi không biết kiểu cấu trúc.

Chênh lệch giữa hai giá trị rất có ý nghĩa: với halide kim loại kiềm, hai giá trị khớp trong vài phần trăm — mô hình ion đúng. Với AgI, giá trị Born - Haber lớn hơn nhiều — dấu hiệu **tính cộng hoá trị đáng kể**, đúng như dự đoán của nguyên lí HSAB cho cặp ion mềm - mềm.

**Lỗi thường gặp:**
- Nhầm $\theta$ với $2\theta$ khi đọc giản đồ nhiễu xạ — sai vì máy ghi góc giữa tia tới và tia nhiễu xạ ($2\theta$) còn định luật Bragg dùng góc tới mặt mạng ($\theta$); nhầm lẫn làm khoảng cách mạng sai gần hai lần.
- Đếm số nguyên tử trong ô mạng mà không chia sẻ theo vị trí — sai vì nguyên tử ở đỉnh thuộc về 8 ô, ở mặt thuộc 2 ô, ở cạnh thuộc 4 ô; đếm nguyên vẹn cho $Z$ lớn gấp nhiều lần và khối lượng riêng vô lí.
- Dùng tỉ số bán kính để dự đoán cấu trúc cho mọi hợp chất — sai vì quy tắc này giả thiết liên kết ion thuần tuý và ion là cầu cứng; nó thất bại rõ với các hợp chất có tính cộng hoá trị như AgI hay các oxit kim loại chuyển tiếp.
- Coi năng lượng mạng lưới đo được trực tiếp bằng thực nghiệm — sai vì không có phép đo nào tách được nó; giá trị 'thực nghiệm' thực chất là kết quả của chu trình Born - Haber, tức tổ hợp của nhiều đại lượng đo khác.

<sub>`lesson.chemistry.vo-co-nang-cao.hoa-hoc-chat-ran-va-cau-truc-tinh-the`</sub>

---

### 7. Hoá sinh vô cơ: kim loại trong hệ sinh học
*Bioinorganic chemistry: metals in biological systems* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Giải thích được nguyên lí HSAB và dãy Irving - Williams trong việc chọn lọc kim loại sinh học
- Phân tích được cơ sở nhiệt động của hiệu ứng chelat
- Mô tả được vai trò của các trung tâm kim loại trong vận chuyển oxi và trong xúc tác enzyme

## Vì sao sự sống chọn đúng những kim loại đó

Khoảng một phần ba số protein chứa kim loại. Việc chọn kim loại nào không ngẫu nhiên mà tuân theo hoá học phối trí.

**HSAB**: acid cứng (Mg$^{2+}$, Ca$^{2+}$, Fe$^{3+}$, Zn$^{2+}$ ở mức trung gian) ưu tiên base cứng — carboxylate, phosphate, oxi của nước. Acid mềm (Cu$^+$, Cd$^{2+}$, Hg$^{2+}$) ưu tiên base mềm — nhóm thiol của cysteine. Vì thế trung tâm kẽm cấu trúc dùng cysteine và histidine, còn Ca$^{2+}$ trong calmodulin dùng aspartate và glutamate. Đây cũng là cơ sở của độc tính: Hg$^{2+}$ và Cd$^{2+}$ tấn công nhóm thiol, phá cấu trúc và hoạt tính enzyme.

**Irving - Williams**: độ bền phức M(II) tăng theo Mn < Fe < Co < Ni < Cu, đạt cực đại ở Cu rồi giảm ở Zn — hệ quả của bán kính ion giảm cộng với CFSE tăng, và biến dạng Jahn - Teller làm Cu(II) đặc biệt bền. Hệ quả sinh học: tế bào phải kiểm soát cực nghiêm ngặt nồng độ Cu tự do (thực tế gần bằng 0, mọi ion Cu đều được protein chaperone chuyển giao), nếu không Cu sẽ chiếm chỗ mọi kim loại khác trong protein.

## Hiệu ứng chelat: entropy làm chủ

So $[\mathrm{Ni(NH_3)_6}]^{2+}$ với $[\mathrm{Ni(en)_3}]^{2+}$: cùng sáu nguyên tử N cho, nhưng phức chelate bền hơn nhiều bậc. $\Delta H$ gần như bằng nhau, khác biệt nằm ở $\Delta S$: phản ứng

$$[\mathrm{Ni(H_2O)_6}]^{2+}+3\,\mathrm{en}\to[\mathrm{Ni(en)_3}]^{2+}+6\,\mathrm{H_2O}$$

đi từ 4 tiểu phân lên 7 tiểu phân — **số tiểu phân tăng** nên $\Delta S>0$. Với NH$_3$ đơn càng, số tiểu phân không đổi.

Hệ quả thiết kế: vòng chelate 5 cạnh bền nhất; phối tử **macrocyclic** như porphyrin còn bền hơn nữa vì đã bị khoá sẵn hình dạng.

## Ba hệ kinh điển

**Hemoglobin và myoglobin**: Fe(II) trong porphyrin, phối trí thứ năm là histidine gần, vị trí thứ sáu gắn O$_2$. Fe(II) spin cao (bán kính lớn) nằm lệch khỏi mặt phẳng porphyrin; khi gắn O$_2$ nó chuyển sang **spin thấp**, bán kính co lại và trượt vào mặt phẳng, kéo theo histidine và toàn bộ chuỗi polypeptide. Chính chuyển động vài chục picomet đó truyền tín hiệu sang các tiểu đơn vị khác — cơ sở phân tử của **cộng tác** và của đường cong sigmoid.

**Cytochrome**: cũng là Fe-porphyrin nhưng vị trí thứ sáu bị chặn, nên chỉ chuyển electron qua cặp Fe(II)/Fe(III).

**Carbonic anhydrase**: Zn$^{2+}$ phối trí bởi ba histidine, hoạt hoá phân tử nước thành OH$^-$ ngay ở pH sinh lí (hạ $\mathrm{p}K_a$ của nước từ 15,7 xuống khoảng 7). Zn được chọn vì là acid Lewis mạnh nhưng **không có hoạt tính oxi hoá - khử**.

**Lỗi thường gặp:**
- Giải thích hiệu ứng chelat bằng 'liên kết chelate mạnh hơn' — sai vì $\Delta H$ của hai hệ gần như nhau khi nguyên tử cho giống nhau; động lực chính là entropy do số tiểu phân trong dung dịch tăng.
- So sánh trực tiếp $\beta_6$ với $\beta_3$ để kết luận phức nào bền hơn — sai vì hai hằng số ứng với hai phản ứng có số phối tử khác nhau nên thứ nguyên khác nhau; phải viết phản ứng thay thế và lấy tỉ số.
- Cho rằng kim loại đứng cao trong dãy Irving - Williams luôn là lựa chọn sinh học tốt nhất — sai vì chính vì Cu(II) tạo phức bền nhất mà tế bào phải giữ nồng độ Cu tự do gần bằng 0; nếu không nó sẽ chiếm chỗ Zn và Fe trong các protein khác.
- Cho rằng sắt trong hemoglobin bị oxi hoá khi gắn oxi — sai vì hemoglobin gắn O$_2$ thuận nghịch mà sắt vẫn là Fe(II) (dù có sự chuyển một phần mật độ electron); dạng bị oxi hoá thật sự là methemoglobin với Fe(III), và nó **không** vận chuyển được oxi.

<sub>`lesson.chemistry.vo-co-nang-cao.hoa-sinh-vo-co`</sub>

---

## Unit 7: IChO - Chiến lược bài toán và vòng thực hành

### 3. Bài toán động học phức tạp: cơ chế nhiều bước và phương trình tốc độ
*Complex kinetics: multi-step mechanisms and rate laws* · Đại học · olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Suy ra được phương trình tốc độ từ cơ chế bằng xấp xỉ nồng độ ổn định hoặc tiền cân bằng
- Xác định được bậc phản ứng từ dữ liệu thực nghiệm bằng tuyến tính hoá hoặc thời gian bán huỷ
- Phân tích được động học phản ứng nối tiếp và phản ứng song song

## Ba câu hỏi động học IChO hay hỏi

1. Từ **cơ chế** suy ra phương trình tốc độ.
2. Từ **dữ liệu** suy ra bậc và hằng số tốc độ.
3. Từ **phương trình tốc độ** dự đoán diễn biến nồng độ theo thời gian.

## Từ cơ chế sang phương trình tốc độ

Hai công cụ, chọn theo tình huống:

- **Tiền cân bằng**: khi bước ngược của phản ứng đầu nhanh hơn nhiều bước tiếp theo ($k_{-1}\gg k_2$). Cho $[I]=\dfrac{k_1}{k_{-1}}[A][B]$.
- **Nồng độ ổn định**: dùng được rộng hơn, không cần giả thiết về tỉ lệ tốc độ. Đặt $\dfrac{d[I]}{dt}=k_1[A]-k_{-1}[I]-k_2[I]=0$ cho $[I]=\dfrac{k_1[A]}{k_{-1}+k_2}$.

Cơ chế Lindemann-Hinshelwood cho ví dụ đẹp: $k_{\text{hiệu dụng}}=\dfrac{k_1k_2[M]}{k_{-1}[M]+k_2}$, chuyển từ bậc **hai** ở áp suất thấp sang bậc **một** ở áp suất cao — hai giới hạn của cùng một công thức.

## Từ dữ liệu sang bậc

| Vẽ tuyến tính | Bậc |
|---|---|
| $[A]$ theo $t$ | 0 |
| $\ln[A]$ theo $t$ | 1 |
| $1/[A]$ theo $t$ | 2 |

Hoặc dùng **thời gian bán huỷ liên tiếp**: bằng nhau $\to$ bậc 1; tăng gấp đôi mỗi lần $\to$ bậc 2; giảm một nửa mỗi lần $\to$ bậc 0. Hoặc **phương pháp tốc độ đầu** với nồng độ ban đầu khác nhau.

## Phản ứng nối tiếp và song song

**Nối tiếp** $A\to B\to C$: nồng độ $B$ đạt cực đại tại $t_{\max}=\dfrac{\ln(k_2/k_1)}{k_2-k_1}$. Nếu bài hỏi "khi nào nên dừng phản ứng để thu nhiều sản phẩm trung gian nhất", đây là công thức cần dùng.

**Song song** $A\to B$ và $A\to C$: tỉ lệ sản phẩm bằng đúng tỉ lệ hằng số tốc độ, $\dfrac{[B]}{[C]}=\dfrac{k_1}{k_2}$, **không đổi theo thời gian**. Đây là cơ sở của khái niệm kiểm soát động học.

## Cảnh báo

Bậc phản ứng là đại lượng **thực nghiệm**, không suy được từ hệ số tỉ lượng. Viết "phản ứng $2A+B\to C$ nên bậc 3" là sai cơ bản, trừ khi đề nói rõ đó là phản ứng sơ cấp.

**Lỗi thường gặp:**
- Suy bậc phản ứng từ hệ số tỉ lượng của phương trình tổng — sai vì bậc là đại lượng thực nghiệm phản ánh cơ chế; chỉ với phản ứng sơ cấp bậc mới trùng hệ số.
- Để chất trung gian còn lại trong phương trình tốc độ cuối cùng — sai vì phương trình tốc độ phải viết theo nồng độ các chất đo được; chất trung gian bắt buộc phải bị khử đi.
- Dùng tiền cân bằng khi bước chậm cũng nhanh cỡ bước ngược — sai vì giả thiết cân bằng đòi hỏi $k_{-1}\gg k_2$; khi hai tốc độ tương đương, chỉ nồng độ ổn định cho kết quả đúng.

<sub>`lesson.chemistry.icho.dong-hoc-phuc-tap`</sub>

---

### 5. Bài toán tinh thể học: từ ô mạng tới khối lượng riêng và bán kính ion
*Crystallography problems: unit cells, density and ionic radii* · Đại học · olympiad · 45 phút · nang-cao

**Mục tiêu:**
- Đếm được số đơn vị cấu trúc Z trong một ô mạng cơ sở
- Tính được khối lượng riêng tinh thể từ hằng số mạng và ngược lại
- Vận dụng được định luật Bragg để suy hằng số mạng từ dữ liệu nhiễu xạ

## Ba đại lượng và ba cầu nối

Bài tinh thể học IChO gần như luôn liên hệ ba đại lượng: **hằng số mạng $a$**, **khối lượng riêng $\rho$**, và **bán kính nguyên tử/ion $r$**. Ba cầu nối:

$$\rho=\frac{Z\,M}{N_A\,a^3},\qquad n\lambda=2d\sin\theta,\qquad d_{hkl}=\frac{a}{\sqrt{h^2+k^2+l^2}}.$$

Biết hai trong ba, tính được cái thứ ba.

## Đếm Z cho đúng

Quy tắc chia sẻ: tiểu phân ở **đỉnh** thuộc 8 ô nên đóng góp $\frac18$; ở **cạnh** thuộc 4 ô nên $\frac14$; ở **mặt** thuộc 2 ô nên $\frac12$; ở **trong** thì $1$.

- Lập phương đơn giản: $8\times\frac18=1$.
- Lập phương tâm khối (bcc): $8\times\frac18+1=2$.
- Lập phương tâm mặt (fcc): $8\times\frac18+6\times\frac12=4$.
- NaCl (fcc của cả hai ion): $Z=4$ đơn vị NaCl.

## Quan hệ $a$ và $r$

| Kiểu mạng | Hướng tiếp xúc | Hệ thức |
|---|---|---|
| Lập phương đơn giản | cạnh | $a=2r$ |
| bcc | đường chéo khối | $\sqrt3\,a=4r$ |
| fcc | đường chéo mặt | $\sqrt2\,a=4r$ |
| NaCl | cạnh | $a=2(r_++r_-)$ |

## Hốc và tỉ số bán kính

Trong mạng đặc khít, hốc **bát diện** chứa được ion bán kính tới $0{,}414R$, hốc **tứ diện** tới $0{,}225R$. Tỉ số $r_+/r_-$ quyết định số phối trí: $<0{,}225$ cho phối trí 3, $0{,}225$-$0{,}414$ cho 4 (kiểu ZnS), $0{,}414$-$0{,}732$ cho 6 (kiểu NaCl), $>0{,}732$ cho 8 (kiểu CsCl). Đây là cách dự đoán kiểu cấu trúc mà không cần dữ liệu thực nghiệm.

## Bẫy thường gặp

1. Đơn vị: $a$ thường cho bằng pm hoặc Å; $\rho$ tính ra g/cm$^3$ nên phải đổi $a$ về cm ($1$ pm $=10^{-10}$ cm).
2. $M$ là khối lượng mol của **một đơn vị công thức**, không phải của một nguyên tử.
3. Trong Bragg, $\theta$ là góc giữa tia tới và **mặt phẳng mạng**, không phải pháp tuyến — khác quy ước quang hình.

**Lỗi thường gặp:**
- Dùng $a=2r$ cho mạng fcc — sai vì trong fcc các nguyên tử tiếp xúc dọc đường chéo mặt chứ không dọc cạnh; hệ thức đúng là $4r=a\sqrt2$.
- Quên đổi hằng số mạng từ pm sang cm khi tính khối lượng riêng — sai vì $\rho$ theo g/cm$^3$ đòi hỏi thể tích tính bằng cm$^3$; sai đơn vị ở đây làm kết quả lệch tới 30 bậc độ lớn.
- Đo góc Bragg từ pháp tuyến của mặt mạng — sai vì trong định luật Bragg, $\theta$ được đo từ chính MẶT PHẲNG mạng; nhầm với quy ước quang hình làm $\sin\theta$ thành $\cos\theta$.

<sub>`lesson.chemistry.icho.bai-toan-tinh-the-hoc`</sub>

---

### 6. Bài toán nhiệt động kết hợp cân bằng: từ delta G tới hằng số K
*Coupling thermodynamics with equilibrium* · Đại học · olympiad · 50 phút · chuyen-sau

**Mục tiêu:**
- Liên hệ được năng lượng Gibbs chuẩn với hằng số cân bằng và với thế điện cực
- Vận dụng được phương trình Van't Hoff để tính K ở nhiệt độ khác
- Phân tích được ảnh hưởng của enthalpy và entropy tới chiều phản ứng theo nhiệt độ

## Sơ đồ liên kết các đại lượng

Mọi bài nhiệt động - cân bằng của IChO đều chạy trên một sơ đồ:

$$\Delta H^\circ,\ \Delta S^\circ\ \xrightarrow{\ \Delta G^\circ=\Delta H^\circ-T\Delta S^\circ\ }\ \Delta G^\circ\ \xrightarrow{\ \Delta G^\circ=-RT\ln K\ }\ K\ \xrightarrow{\ \ }\ \text{nồng độ cân bằng}$$

và nhánh điện hoá $\Delta G^\circ=-nFE^\circ$. Nhận ra mình đang ở mắt xích nào của sơ đồ là bước đầu tiên.

## Bốn công thức phải viết chuẩn

$$\Delta G^\circ=-RT\ln K,\qquad \Delta G=\Delta G^\circ+RT\ln Q,$$
$$\Delta G^\circ=-nFE^\circ,\qquad \ln\frac{K_2}{K_1}=-\frac{\Delta H^\circ}{R}\left(\frac1{T_2}-\frac1{T_1}\right).$$

## Đọc dấu để dự đoán

| $\Delta H^\circ$ | $\Delta S^\circ$ | Kết luận |
|---|---|---|
| $<0$ | $>0$ | tự diễn biến ở mọi $T$ |
| $>0$ | $<0$ | không tự diễn biến ở mọi $T$ |
| $<0$ | $<0$ | tự diễn biến ở $T$ **thấp**, $T_{\text{giới hạn}}=\Delta H^\circ/\Delta S^\circ$ |
| $>0$ | $>0$ | tự diễn biến ở $T$ **cao** |

Đồ thị $\Delta G^\circ$ theo $T$ là đường thẳng hệ số góc $-\Delta S^\circ$, tung độ gốc $\Delta H^\circ$. Đồ thị $\ln K$ theo $1/T$ là đường thẳng hệ số góc $-\Delta H^\circ/R$ — dạng chuẩn để lấy $\Delta H^\circ$ từ số liệu thực nghiệm.

## Ba cạm bẫy

1. **Trạng thái chuẩn.** $K$ là đại lượng **không thứ nguyên**, tính theo hoạt độ tương đối với trạng thái chuẩn ($1$ M cho chất tan, $1$ bar cho khí). Trộn $K_p$ và $K_c$ mà không đổi qua $K_p=K_c(RT/p^\circ)^{\Delta n}$ là lỗi phổ biến.
2. **$\Delta H^\circ$ coi là hằng số** trong Van't Hoff tích phân chỉ đúng khi khoảng nhiệt độ hẹp; nếu rộng phải dùng Kirchhoff để hiệu chỉnh theo $\Delta C_p$.
3. **$\Delta G^\circ$ khác $\Delta G$.** $\Delta G^\circ$ chỉ nói về trạng thái chuẩn; chiều thực tế của phản ứng do dấu của $\Delta G$ quyết định, tức phụ thuộc $Q$ hiện thời.

**Lỗi thường gặp:**
- Thay $K_c$ vào $\Delta G^\circ=-RT\ln K$ cho phản ứng khí mà đề cho $K_p$ — sai vì hai hằng số khác nhau bởi hệ số $(RT/p^\circ)^{\Delta n}$ khi $\Delta n\ne0$; giá trị $\Delta G^\circ$ thu được sẽ ứng với trạng thái chuẩn khác.
- Dùng $\Delta G^\circ$ để kết luận chiều phản ứng ở điều kiện bất kì — sai vì chiều thực tế do dấu của $\Delta G=\Delta G^\circ+RT\ln Q$ quyết định; phản ứng có $\Delta G^\circ>0$ vẫn tự diễn biến khi $Q$ đủ nhỏ.
- Dùng Van't Hoff tích phân trên khoảng nhiệt độ rộng hàng trăm kelvin — sai vì $\Delta H^\circ$ phụ thuộc nhiệt độ qua $\Delta C_p$; bỏ qua hiệu chỉnh Kirchhoff làm sai lệch đáng kể.

<sub>`lesson.chemistry.icho.nhiet-dong-ket-hop-can-bang`</sub>

---

## Unit 8: Hoá phân tích

### 1. Thống kê trong phân tích và đánh giá độ tin cậy
*Statistics in analysis and evaluation of reliability* · Đại học · intl-undergrad · 75 phút · nang-cao

**Mục tiêu:**
- Phân biệt được độ đúng và độ chụm, sai số hệ thống và sai số ngẫu nhiên
- Tính được khoảng tin cậy của giá trị trung bình từ một tập số liệu nhỏ
- Vận dụng được kiểm định t và kiểm định Q để kết luận về sai số hệ thống và số liệu nghi ngờ

## Một con số không có sai số thì vô nghĩa

Báo cáo "hàm lượng sắt 12,4 %" là chưa hoàn chỉnh. Câu hỏi luôn phải trả lời là: con số đó tin được tới đâu, và tin được vì lí do gì.

Phân biệt hai loại sai số vì cách xử lí chúng hoàn toàn khác nhau:
- **Sai số hệ thống** (determinate): luôn lệch về một phía; do dụng cụ chưa hiệu chuẩn, phương pháp có sai lệch, hoặc người thao tác. Đo lặp lại nhiều lần **không** làm nó nhỏ đi. Chỉ phát hiện được bằng mẫu chuẩn hoặc phương pháp đối chứng.
- **Sai số ngẫu nhiên** (indeterminate): dao động hai phía; giảm theo $1/\sqrt n$ khi tăng số lần đo.

Hệ quả: một phép đo có thể rất **chụm** mà hoàn toàn **sai** — đó là tình huống nguy hiểm nhất, vì độ chụm cao tạo cảm giác tin cậy giả.

## Khoảng tin cậy cho mẫu nhỏ

$$\bar x=\frac{1}{n}\sum x_i,\qquad s=\sqrt{\frac{\sum(x_i-\bar x)^2}{n-1}}$$

$$\mu = \bar x \pm \frac{t s}{\sqrt n}$$

Chú ý mẫu số $n-1$ (bậc tự do) và việc dùng **$t$** thay cho $z$: với $n$ nhỏ, $s$ chỉ là ước lượng của $\sigma$ nên khoảng phải rộng hơn. Với $n=3$ và 95 %, $t=4{,}30$; với $n=5$, $t=2{,}78$; với $n=10$, $t=2{,}26$. Tăng số lần đo có lợi kép: $t$ giảm và $\sqrt n$ tăng.

## Hai phép kiểm định thường dùng

**Kiểm định t** (so với giá trị đã biết, ví dụ mẫu chuẩn):

$$t_{tính}=\frac{|\bar x-\mu|\sqrt n}{s}$$

Nếu $t_{tính}>t_{bảng}$ ở mức 95 % thì chênh lệch **có ý nghĩa** — kết luận có sai số hệ thống.

**Kiểm định Q** (loại số liệu nghi ngờ):

$$Q=\frac{|x_{\text{nghi ngờ}}-x_{\text{gần nhất}}|}{x_{\max}-x_{\min}}$$

Loại bỏ nếu $Q>Q_{bảng}$. Nguyên tắc đạo đức: chỉ loại **một** giá trị, và phải báo cáo việc đã loại.

## Lan truyền sai số

- Cộng, trừ: cộng bình phương **sai số tuyệt đối**.
- Nhân, chia: cộng bình phương **sai số tương đối**.

Quy tắc thực dụng quan trọng nhất rút ra từ đây: khâu nào có sai số tương đối lớn nhất sẽ **chi phối** kết quả; cải thiện các khâu khác gần như vô ích. Trong chuẩn độ, đó thường là việc đọc thể tích tại điểm cuối chứ không phải phép cân.

**Lỗi thường gặp:**
- Loại bỏ số liệu chỉ vì 'trông lạc' — sai vì việc loại phải dựa trên tiêu chí thống kê; loại tuỳ tiện làm giảm giả tạo độ lệch chuẩn và tạo ra độ tin cậy không có thật.
- Dùng $n$ thay vì $n-1$ ở mẫu số của độ lệch chuẩn — sai vì $\bar x$ đã được ước lượng từ chính tập số liệu, làm mất một bậc tự do; dùng $n$ cho $s$ nhỏ hơn thực và khoảng tin cậy hẹp giả tạo.
- Dùng hệ số $z = 1{,}96$ cho mẫu nhỏ — sai vì với $n$ nhỏ thì $s$ chỉ là ước lượng thô của $\sigma$; phải dùng $t$ tra theo bậc tự do, và với $n=3$ thì $t=4{,}30$, gấp hơn hai lần 1,96.
- Cho rằng đo nhiều lần sẽ khắc phục sai số hệ thống — sai vì sai số hệ thống lệch cùng một phía ở mọi lần đo nên trung bình không cải thiện; chỉ mẫu chuẩn hoặc phương pháp độc lập mới phát hiện được nó.

<sub>`lesson.chemistry.hoa-phan-tich.thong-ke-va-do-tin-cay`</sub>

---

### 2. Cân bằng trong phân tích: acid - base, kết tủa và tạo phức
*Equilibria in analysis: acid-base, precipitation and complexation* · Đại học · intl-undergrad · 90 phút · nang-cao

**Mục tiêu:**
- Tính được pH của các hệ acid - base và của dung dịch đệm
- Phân tích được ảnh hưởng của ion chung, pH và sự tạo phức lên độ tan
- Vận dụng được hằng số bền điều kiện để mô tả cân bằng tạo phức trong môi trường thực

## Vì sao cân bằng là nền của phân tích

Mọi phương pháp phân tích ướt đều dựa trên một cân bằng chuyển dịch mạnh về một phía. Muốn biết phép chuẩn độ có khả thi không, có chọn lọc không, và điểm cuối sắc tới đâu — đều phải quay về hằng số cân bằng.

## Acid - base: từ công thức tới hệ đầy đủ

Các trường hợp thường dùng:
- Acid yếu $C$, $K_a$: $[\mathrm{H^+}]\approx\sqrt{K_aC}$, hợp lệ khi $\alpha<5\,\%$ và $K_aC\gg K_w$.
- Đệm: $\mathrm{pH}=\mathrm{p}K_a+\lg\dfrac{[\mathrm{A^-}]}{[\mathrm{HA}]}$ (Henderson - Hasselbalch).
- Muối acid lưỡng tính: $\mathrm{pH}\approx\tfrac12(\mathrm{p}K_{a1}+\mathrm{p}K_{a2})$, gần như **không phụ thuộc nồng độ**.

Với hệ đa acid, cách nhìn tổng quát nhất là **phân số nồng độ**: mỗi dạng $\mathrm{H}_n\mathrm{A}$ có $\alpha_i$ là hàm của pH. Vẽ $\alpha$ theo pH cho ngay biết ở pH nào dạng nào chiếm ưu thế — công cụ nền cho mọi lập luận về chọn lọc.

**Dung lượng đệm** cực đại tại $\mathrm{pH}=\mathrm{p}K_a$ và tỉ lệ với nồng độ tổng. Khoảng đệm hữu ích là $\mathrm{p}K_a\pm1$; ngoài khoảng đó dung lượng sụt nhanh. Vì thế chọn đệm là chọn chất có $\mathrm{p}K_a$ gần pH mong muốn, không phải chất "quen dùng".

## Độ tan và ba yếu tố tác động

Từ $K_{sp}$, độ tan của $\mathrm{M}_m\mathrm{X}_n$ là $s=\left(\dfrac{K_{sp}}{m^mn^n}\right)^{1/(m+n)}$.

- **Ion chung**: giảm độ tan, tuân định luật tác dụng khối lượng.
- **pH**: nếu anion là base (CO$_3^{2-}$, S$^{2-}$, F$^-$), hạ pH proton hoá nó và **tăng** độ tan. Đây là lí do CaCO$_3$ tan trong acid còn AgCl thì không.
- **Tạo phức**: thêm phối tử tạo phức với cation làm **tăng** độ tan — AgCl tan trong NH$_3$ dư. Nhưng chú ý hiệu ứng phi tuyến: thêm Cl$^-$ ban đầu giảm độ tan AgCl (ion chung), rồi lại **tăng** ở nồng độ cao do tạo $[\mathrm{AgCl_2}]^-$.

Ngoài ra, thêm chất điện li trơ làm **tăng** độ tan (hiệu ứng muối), vì hệ số hoạt độ giảm.

## Hằng số bền điều kiện: cầu nối lí thuyết và thực tế

EDTA chỉ tạo phức ở dạng $\mathrm{Y^{4-}}$, mà tỉ lệ dạng này phụ thuộc mạnh vào pH: $\alpha_{Y^{4-}}$ bằng $3{,}5\times10^{-7}$ ở pH 5, $0{,}30$ ở pH 10 và $0{,}81$ ở pH 11. Vì thế đại lượng dùng được là

$$K'_f=\alpha_{Y^{4-}}K_f$$

Quy tắc thực hành: cần $K'_f \gtrsim 10^{8}$ để chuẩn độ cho bước nhảy đủ sắc. Điều này giải thích vì sao Ca$^{2+}$ ($K_f=10^{10{,}7}$) phải chuẩn ở pH 10, còn Fe$^{3+}$ ($K_f=10^{25{,}1}$) chuẩn được ngay ở pH 2 — và chính sự khác biệt đó cho phép **chuẩn độ chọn lọc** Fe$^{3+}$ khi có mặt Ca$^{2+}$.

**Lỗi thường gặp:**
- Dùng $K_f$ trong bảng để đánh giá khả năng chuẩn độ — sai vì bảng ứng với dạng $\mathrm{Y^{4-}}$ tinh khiết; trong dung dịch thực chỉ một phần EDTA ở dạng đó, nên phải nhân với $\alpha_{Y^{4-}}$ để có hằng số bền điều kiện.
- Cho rằng thêm ion chung luôn làm giảm độ tan — sai vì ở nồng độ cao ion chung có thể tạo phức tan; thêm Cl$^-$ dư làm AgCl tan trở lại dưới dạng $[\mathrm{AgCl_2}]^-$, nên đường độ tan theo $[\mathrm{Cl^-}]$ có cực tiểu.
- Chọn đệm chỉ theo tên quen thuộc mà không xét $\mathrm{p}K_a$ — sai vì dung lượng đệm cực đại tại $\mathrm{pH}=\mathrm{p}K_a$ và sụt nhanh ngoài khoảng $\mathrm{p}K_a\pm1$; đệm chọn sai gần như không có tác dụng.
- Dùng $\mathrm{pH}\approx\tfrac12(\mathrm{p}K_{a1}+\mathrm{p}K_{a2})$ cho dung dịch muối acid rất loãng — sai vì công thức rút gọn đó giả thiết nồng độ đủ lớn so với $K_{a1}$ và $K_w$; ở nồng độ thấp phải dùng biểu thức đầy đủ.

<sub>`lesson.chemistry.hoa-phan-tich.can-bang-trong-phan-tich`</sub>

---

### 3. Các phương pháp chuẩn độ và đường cong chuẩn độ
*Titration methods and titration curves* · Đại học · intl-undergrad · 90 phút · nang-cao

**Mục tiêu:**
- Dựng và giải thích được đường cong chuẩn độ acid - base, kết tủa và oxi hoá - khử
- Chọn được chỉ thị phù hợp dựa trên pH hoặc thế tại điểm tương đương
- Phân biệt được điểm tương đương với điểm cuối và ước lượng được sai số chuẩn độ

## Hình dạng đường cong quyết định chất lượng phép chuẩn độ

Bước nhảy càng dốc và càng dài thì điểm cuối càng dễ nhận và sai số càng nhỏ. Ba yếu tố làm bước nhảy dốc: hằng số cân bằng lớn, nồng độ cao, và ít cản trở từ nền mẫu.

## Acid - base

- **Acid mạnh + base mạnh**: điểm tương đương ở pH 7, bước nhảy dài (khoảng pH 4–10) nên chỉ thị nào cũng dùng được.
- **Acid yếu + base mạnh**: điểm tương đương ở pH **kiềm** (do base liên hợp thuỷ phân), bước nhảy ngắn hơn. Chọn phenolphtalein ($\mathrm{p}K_{In}\approx 9{,}4$), không dùng methyl da cam.
- Tại nửa điểm tương đương, $\mathrm{pH}=\mathrm{p}K_a$ — cách xác định $K_a$ nhanh và chính xác.
- Acid quá yếu ($K_a<10^{-8}$) không chuẩn độ được trong nước: bước nhảy chìm trong hiệu ứng san bằng của dung môi.

**Quy tắc chọn chỉ thị**: khoảng đổi màu $\mathrm{p}K_{In}\pm1$ phải nằm **trọn trong** bước nhảy.

## Kết tủa

Phương pháp bạc là kinh điển:
- **Mohr**: chỉ thị $\mathrm{CrO_4^{2-}}$, tạo Ag$_2$CrO$_4$ đỏ gạch; chỉ dùng ở pH 7–10 vì cromat bị proton hoá ở pH thấp và Ag$_2$O kết tủa ở pH cao.
- **Volhard**: chuẩn ngược bằng SCN$^-$ với chỉ thị Fe$^{3+}$; làm trong môi trường acid nên tránh được nhược điểm của Mohr.
- **Fajans**: chỉ thị hấp phụ trên bề mặt kết tủa, đổi màu khi bề mặt đổi dấu điện tích ngay sau điểm tương đương.

## Oxi hoá - khử

Trước điểm tương đương, thế được tính từ cặp của chất phân tích; sau điểm tương đương, từ cặp của chất chuẩn. Tại điểm tương đương:

$$E_{tđ}=\frac{n_1E_1^{\circ\prime}+n_2E_2^{\circ\prime}}{n_1+n_2}$$

(khi không có H$^+$ trong nửa phản ứng). Bước nhảy càng lớn khi $\Delta E^\circ$ giữa hai cặp càng lớn; cần khoảng $\Delta E^{\circ}>0{,}2$ V mới đủ dùng chỉ thị.

## Điểm cuối không phải điểm tương đương

Sai số chuẩn độ là hệ quả trực tiếp của chênh lệch này. Cách xử lí đúng:
1. Chạy **mẫu trắng** để trừ đi lượng chất chuẩn tiêu tốn cho chính chỉ thị.
2. Dùng phương pháp **đo điện thế** hoặc đo độ dẫn để xác định điểm cuối khách quan, tránh phụ thuộc mắt người.
3. Với đường cong đo điện thế, điểm uốn xác định bằng cực đại của đạo hàm bậc nhất hoặc điểm cắt 0 của đạo hàm bậc hai — chính xác hơn nhiều so với ước lượng bằng mắt trên đồ thị gốc.

**Lỗi thường gặp:**
- Cho rằng điểm tương đương của mọi phép chuẩn độ acid - base đều ở pH 7 — sai vì chỉ đúng khi cả acid và base đều mạnh; với acid yếu, base liên hợp sinh ra thuỷ phân làm điểm tương đương nằm ở vùng kiềm.
- Chọn chỉ thị theo thói quen thay vì theo bước nhảy — sai vì dùng methyl da cam cho chuẩn độ acid yếu làm điểm cuối xuất hiện quá sớm; sai số có thể tới hàng chục phần trăm chứ không phải vài phần trăm.
- Quên hiệu chỉnh thể tích pha loãng khi tính nồng độ tại điểm tương đương — sai vì thể tích tổng đã tăng gấp đôi trong ví dụ trên; bỏ qua làm nồng độ base liên hợp sai hai lần và pH sai khoảng 0,15 đơn vị.
- Đồng nhất điểm cuối với điểm tương đương — sai vì chỉ thị luôn cần một lượng chất chuẩn dư nhất định để đổi màu; phải chạy mẫu trắng hoặc dùng phương pháp đo điện thế để giảm sai số này.

<sub>`lesson.chemistry.hoa-phan-tich.cac-phuong-phap-chuan-do`</sub>

---

### 4. Phương pháp quang phổ định lượng
*Quantitative spectroscopic methods* · Đại học · intl-undergrad · 90 phút · nang-cao

**Mục tiêu:**
- Vận dụng được định luật Lambert - Beer và nêu rõ các điều kiện làm nó sai lệch
- Xây dựng và đánh giá được đường chuẩn bằng hồi quy tuyến tính
- Tính được giới hạn phát hiện và giới hạn định lượng của một phương pháp

## Định luật nền và vùng làm việc

$$A=\varepsilon\, b\, c$$

Với $\varepsilon$ là hệ số hấp thụ mol (L mol$^{-1}$cm$^{-1}$), $b$ bề dày cuvet, $c$ nồng độ.

Có một **vùng độ hấp thụ tối ưu** là 0,2–0,8. Lí do là sai số tương đối của nồng độ, xuất phát từ sai số đọc độ truyền qua, đạt cực tiểu quanh $A\approx 0{,}43$. Ở $A$ quá nhỏ tín hiệu chìm trong nhiễu; ở $A$ quá lớn ($>1{,}5$), $I$ nhỏ tới mức sai số tương đối bùng nổ. Mẫu quá đặc phải **pha loãng**, không được đo trực tiếp rồi ngoại suy.

## Vì sao Lambert - Beer bị lệch

Ba nhóm nguyên nhân, cần phân biệt để xử lí đúng:

- **Thật (hoá học)**: ở nồng độ cao, chất tan tương tác hoặc thay đổi cân bằng (dimer hoá, phân li, tạo phức); hệ số hoạt độ thay đổi. Cách xử lí: pha loãng, hoặc cố định lực ion và pH.
- **Do thiết bị**: ánh sáng không đơn sắc (dải bước sóng rộng làm đường cong uốn xuống), ánh sáng lạc. Cách xử lí: đo tại **cực đại hấp thụ** nơi $\varepsilon$ ít đổi theo $\lambda$, và dùng khe hẹp.
- **Do mẫu**: huyền phù gây tán xạ, huỳnh quang của mẫu. Cách xử lí: lọc mẫu, đo mẫu trắng nền.

## Đường chuẩn làm cho đúng

Hồi quy $y = mx + b$ với ít nhất 5 điểm chuẩn phủ trọn khoảng nồng độ mẫu. Đánh giá:
- $R^2$ **không đủ** để kết luận tuyến tính — luôn phải xem **đồ thị phần dư**; phần dư có xu hướng cong nghĩa là mô hình tuyến tính sai dù $R^2 = 0{,}999$.
- Không ngoại suy ra ngoài khoảng chuẩn.
- Nồng độ mẫu tính bằng $c = (y-b)/m$, và sai số của nó phải tính từ sai số của cả $m$, $b$ và $y$.

$$\mathrm{LOD}=\frac{3s_{b}}{m},\qquad \mathrm{LOQ}=\frac{10s_{b}}{m}$$

## Khi nền mẫu gây rắc rối

Đường chuẩn thông thường giả thiết nền của mẫu chuẩn giống nền của mẫu thật. Khi điều đó không đúng (nước biển, huyết thanh, dịch chiết đất), dùng **thêm chuẩn**: thêm các lượng chất chuẩn tăng dần vào chính mẫu, vẽ tín hiệu theo lượng thêm, và ngoại suy đường thẳng cắt trục hoành — giao điểm cho lượng chất có sẵn trong mẫu.

Phương pháp thứ hai là **nội chuẩn**: thêm một chất tương tự với lượng cố định vào mọi mẫu và mọi chuẩn, rồi dùng **tỉ số** tín hiệu. Cách này bù được cả dao động thể tích tiêm lẫn dao động độ nhạy thiết bị, nên là chuẩn mực trong sắc kí và phổ khối.

**Lỗi thường gặp:**
- Đo mẫu có độ hấp thụ trên 1,5 rồi dùng thẳng đường chuẩn — sai vì ở đó cường độ truyền qua rất nhỏ, sai số tương đối bùng nổ và Lambert - Beer thường đã lệch; phải pha loãng về vùng $A = 0{,}2$–$0{,}8$.
- Dùng $R^2$ gần 1 làm bằng chứng duy nhất cho tính tuyến tính — sai vì $R^2$ rất kém nhạy với độ cong nhẹ; phải xem đồ thị **phần dư**, nơi xu hướng có hệ thống lộ ra rõ ràng.
- Ngoại suy đường chuẩn ra ngoài khoảng nồng độ đã chuẩn — sai vì không có bằng chứng nào về hành vi của hệ ở đó; sai lệch khỏi Lambert - Beer thường bắt đầu ngay bên ngoài khoảng đã kiểm chứng.
- Dùng đường chuẩn thông thường cho mẫu có nền phức tạp — sai khi nền làm thay đổi độ nhạy; phải dùng phương pháp thêm chuẩn hoặc nội chuẩn, nếu không kết quả sẽ lệch có hệ thống mà đường chuẩn vẫn trông rất đẹp.

<sub>`lesson.chemistry.hoa-phan-tich.quang-pho-dinh-luong`</sub>

---

### 5. Phương pháp tách sắc kí: lí thuyết đĩa và độ phân giải
*Chromatographic separations: plate theory and resolution* · Đại học · intl-undergrad · 90 phút · nang-cao

**Mục tiêu:**
- Định nghĩa được hệ số lưu giữ, hệ số chọn lọc và số đĩa lí thuyết
- Vận dụng được phương trình độ phân giải để tối ưu phép tách
- Giải thích được phương trình Van Deemter và ý nghĩa của tốc độ pha động tối ưu

## Ba đại lượng, ba nút điều khiển

Chất lượng phép tách của hai pic kề nhau tóm gọn trong một phương trình:

$$R_s=\frac{\sqrt N}{4}\cdot\underbrace{\frac{\alpha-1}{\alpha}}_{\text{chọn lọc}}\cdot\underbrace{\frac{k_2}{1+k_2}}_{\text{lưu giữ}}$$

Ba thừa số ứng với ba cách can thiệp hoàn toàn khác nhau:

- **$N$ (hiệu lực)**: tăng bằng cột dài hơn hoặc hạt nhồi nhỏ hơn. Nhưng $R_s\propto\sqrt N$, nên **gấp bốn lần chiều dài cột chỉ tăng gấp đôi độ phân giải** — và thời gian phân tích tăng gấp bốn. Đây là cách kém hiệu quả nhất.
- **$\alpha$ (chọn lọc)**: đổi pha động, pha tĩnh, pH hoặc nhiệt độ. Vì $\alpha$ nằm trong thừa số $(\alpha-1)/\alpha$ vốn rất nhạy khi $\alpha$ gần 1, đây là **nút điều khiển mạnh nhất**: đưa $\alpha$ từ 1,05 lên 1,10 gần như nhân đôi $R_s$.
- **$k$ (lưu giữ)**: thừa số $k/(1+k)$ tăng nhanh từ 0 tới khoảng $k=5$ rồi bão hoà. Tăng $k$ quá 10 chỉ làm kéo dài phân tích mà gần như không cải thiện tách.

Mục tiêu thực hành: $R_s\ge 1{,}5$ là tách hoàn toàn (đường nền tách rời).

## Van Deemter: vì sao có tốc độ tối ưu

$$H=A+\frac{B}{u}+Cu$$

- $A$ — **khuếch tán xoáy**: đường đi khác nhau giữa các hạt nhồi. Không phụ thuộc $u$; giảm bằng hạt nhỏ, đều, nhồi tốt. Bằng 0 với cột mao quản hở.
- $B/u$ — **khuếch tán dọc**: chi phối ở tốc độ thấp. Lớn trong sắc kí khí (khuếch tán trong khí nhanh), nhỏ trong HPLC.
- $Cu$ — **cản trở chuyển khối**: chi phối ở tốc độ cao; giảm bằng lớp phim pha tĩnh mỏng và hạt nhỏ.

Cực tiểu của $H$ cho tốc độ tối ưu $u_{opt}=\sqrt{B/C}$. Ý nghĩa thực hành: chạy nhanh hơn **không** luôn tệ hơn — nhưng chạy chậm hơn $u_{opt}$ thì vừa chậm vừa kém. Với hạt dưới 2 $\mu$m (UHPLC), số hạng $C$ nhỏ tới mức đường Van Deemter gần như phẳng ở tốc độ cao, cho phép phân tích nhanh mà không mất hiệu lực.

## Chọn kĩ thuật

- **GC**: chất bay hơi, bền nhiệt; hiệu lực rất cao ($N$ tới $10^5$).
- **HPLC pha đảo**: chất phân cực tới trung bình, không bay hơi; nút điều khiển chính là thành phần dung môi và pH.
- **Trao đổi ion**: ion, protein; điều khiển bằng lực ion và pH.
- **Loại trừ kích thước**: tách theo kích thước phân tử, dùng cho polymer và protein.

Ghép với detector chọn lọc (MS) cho thêm một chiều phân giải: hai chất đồng rửa giải vẫn tách được nếu khác $m/z$.

**Lỗi thường gặp:**
- Cải thiện độ phân giải bằng cách kéo dài cột như phản xạ đầu tiên — kém hiệu quả vì $R_s\propto\sqrt L$: muốn gấp đôi độ phân giải phải gấp bốn chiều dài, kéo theo gấp bốn thời gian và áp suất.
- Tăng hệ số lưu giữ $k$ lên rất cao để tách tốt hơn — sai vì thừa số $k/(1+k)$ bão hoà quanh $k\approx 5$; vượt quá 10 chỉ kéo dài phân tích và làm pic tù hơn mà độ phân giải gần như không đổi.
- Chạy pha động càng chậm càng tốt để tăng hiệu lực — sai vì phương trình Van Deemter có cực tiểu; dưới $u_{opt}$, khuếch tán dọc ($B/u$) làm pic rộng ra, nên vừa chậm vừa kém hiệu lực.
- Dùng $N$ tính từ một pic để mô tả toàn bộ sắc đồ — sai vì $N$ phụ thuộc chất và thời gian lưu; báo cáo hiệu lực cột phải nêu rõ tính trên pic nào và ở điều kiện nào.

<sub>`lesson.chemistry.hoa-phan-tich.phuong-phap-tach-sac-ki`</sub>

---

### 6. Phương pháp điện hoá trong phân tích
*Electroanalytical methods* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Phân biệt được các nhóm phương pháp điện hoá theo đại lượng đo và điều kiện dòng
- Giải thích được nguyên lí và các nguồn sai số của phép đo pH bằng điện cực thuỷ tinh
- Trình bày được nguyên lí của các kĩ thuật von-ampe và ứng dụng phân tích vết

## Phân loại theo đại lượng đo

- **Đo điện thế**: đo $E$ ở $I\approx 0$. Tín hiệu tỉ lệ với $\lg a$, nên khoảng động rộng nhiều bậc nhưng độ chính xác tương đối kém.
- **Đo độ dẫn**: đo tổng nồng độ ion; không chọn lọc, hữu ích cho chuẩn độ và cho theo dõi độ tinh khiết của nước.
- **Đo điện lượng (coulometry)**: đo điện lượng, tính lượng chất bằng Faraday. Là phương pháp **tuyệt đối** — không cần đường chuẩn.
- **Von-ampe**: đo dòng theo thế áp đặt; dòng tỉ lệ **tuyến tính** với nồng độ, và có thể làm giàu trước để đạt độ nhạy rất cao.

## Điện cực thuỷ tinh: mạnh nhưng có bẫy

Màng thuỷ tinh phát triển một thế màng phụ thuộc hoạt độ H$^+$:

$$E=k-0{,}05916\,\mathrm{pH}\ \ (25\ ^\circ\mathrm{C})$$

Bốn nguồn sai số phải kiểm soát:
1. **Sai số kiềm** ở pH $>12$: Na$^+$ cạnh tranh, pH đọc **thấp** hơn thực.
2. **Sai số acid** ở pH $<0{,}5$: pH đọc cao hơn thực.
3. **Thế bất đối xứng** trôi theo thời gian — bắt buộc hiệu chuẩn bằng ít nhất **hai** dung dịch đệm kẹp lấy pH mẫu.
4. **Nhiệt độ**: hệ số Nernst thay đổi theo $T$; máy phải bù nhiệt độ.

Quan trọng về nguyên tắc: điện cực đo **hoạt độ**, không đo nồng độ. Với dung dịch có lực ion cao, hai đại lượng chênh nhau đáng kể — khi cần nồng độ, phải cố định lực ion cho cả mẫu và chuẩn bằng dung dịch điều chỉnh lực ion tổng.

## Điện cực chọn lọc ion

Nguyên lí giống điện cực thuỷ tinh nhưng màng khác: màng tinh thể (F$^-$ với LaF$_3$), màng lỏng (Ca$^{2+}$), màng khí (NH$_3$, CO$_2$).

Không có điện cực nào chọn lọc tuyệt đối. Phương trình Nikolsky - Eisenman đưa vào hệ số chọn lọc $K_{ij}$, và giá trị này quyết định ion nào gây nhiễu. Ví dụ điện cực F$^-$ bị nhiễu bởi OH$^-$, nên phải đệm mẫu về pH 5–6.

## Von-ampe và phân tích vết

Trong von-ampe xung vi phân, việc lấy mẫu dòng vào cuối xung loại được phần lớn dòng tụ điện, đưa giới hạn phát hiện xuống cỡ $10^{-8}$ M.

**Von-ampe hoà tan anot** còn thêm một bước làm giàu: giữ điện cực ở thế khử vài phút để kết tủa kim loại lên bề mặt, rồi quét thế về phía dương để hoà tan lại. Vì chất được cô đặc từ hàng chục mL vào một lớp cực mỏng, độ nhạy tăng hàng trăm lần, đạt tới $10^{-10}$–$10^{-11}$ M. Đây là một trong số ít phương pháp cho phép đo Pb, Cd, Cu, Zn ở mức ppt ngay tại hiện trường, với thiết bị rẻ hơn nhiều so với ICP-MS.

Hạn chế: phụ thuộc mạnh vào nền mẫu (chất hoạt động bề mặt, chất hữu cơ hấp phụ lên điện cực), nên hầu như luôn phải dùng **thêm chuẩn** thay vì đường chuẩn ngoài.

**Lỗi thường gặp:**
- Hiệu chuẩn máy đo pH bằng một dung dịch đệm duy nhất — sai vì cần ít nhất hai điểm để xác định cả thế bất đối xứng lẫn độ dốc; một điểm chỉ chỉnh được offset và bỏ sót sự suy giảm độ dốc của điện cực cũ.
- Coi điện cực đo nồng độ — sai vì nó đáp ứng theo **hoạt độ**; trong dung dịch có lực ion cao, chênh lệch giữa hai đại lượng có thể tới hàng chục phần trăm, nên phải cố định lực ion cho cả mẫu và chuẩn.
- Dùng điện cực thuỷ tinh ở pH trên 12 mà không hiệu chỉnh — sai vì sai số kiềm khiến pH đọc thấp hơn thực; ở môi trường rất kiềm phải dùng điện cực thuỷ tinh lithi chuyên dụng.
- Áp dụng đường chuẩn ngoài cho von-ampe hoà tan trên mẫu môi trường — sai vì hiệu suất làm giàu phụ thuộc mạnh vào nền mẫu; phương pháp thêm chuẩn là bắt buộc trong hầu hết ứng dụng thực tế.

<sub>`lesson.chemistry.hoa-phan-tich.phuong-phap-dien-hoa-phan-tich`</sub>

---

### 7. Kiểm soát chất lượng và thẩm định phương pháp phân tích
*Quality control and analytical method validation* · Đại học · intl-undergrad · 90 phút · chuyen-sau

**Mục tiêu:**
- Trình bày được các tiêu chí thẩm định một phương pháp phân tích
- Đọc và diễn giải được biểu đồ kiểm soát theo các quy tắc Westgard
- Thiết kế được kế hoạch kiểm soát chất lượng cho một quy trình phân tích thường quy

## Một kết quả chỉ có giá trị khi truy nguyên được

Phòng thí nghiệm hiện đại không chỉ đo, mà phải **chứng minh** kết quả đúng. Ba trụ cột: thẩm định phương pháp trước khi dùng, kiểm soát chất lượng liên tục khi dùng, và ước lượng độ không đảm bảo đo khi báo cáo.

## Bộ tiêu chí thẩm định

- **Độ chọn lọc**: phương pháp đo đúng chất cần đo khi có mặt tạp chất, chất chuyển hoá và nền mẫu.
- **Khoảng tuyến tính** và **khoảng làm việc**.
- **Độ đúng**: đánh giá bằng mẫu chuẩn được chứng nhận, bằng độ thu hồi (thêm chuẩn), hoặc bằng đối chiếu với phương pháp chuẩn.
- **Độ chụm**: tách thành **độ lặp lại** (cùng người, cùng ngày, cùng thiết bị) và **độ tái lặp trong phòng** (khác ngày, khác người) — hai con số này thường chênh nhau đáng kể và phải báo cáo riêng.
- **LOD, LOQ**.
- **Độ vững**: chủ động thay đổi nhỏ các thông số để tìm điểm nhạy cảm trước khi chúng gây sự cố ngoài ý muốn.

## Biểu đồ kiểm soát và quy tắc Westgard

Chạy mẫu kiểm soát cùng mỗi lô mẫu thật và vẽ kết quả theo thời gian. Các quy tắc thường dùng:

- **$1_{3s}$**: một điểm vượt $\pm 3s$ $\Rightarrow$ **loại lô**, tìm nguyên nhân.
- **$2_{2s}$**: hai điểm liên tiếp cùng phía vượt $2s$ $\Rightarrow$ loại lô (sai số hệ thống).
- **$R_{4s}$**: hai điểm liên tiếp chênh nhau quá $4s$ $\Rightarrow$ loại lô (sai số ngẫu nhiên tăng).
- **$4_{1s}$** và **$10_{\bar x}$**: bốn điểm cùng phía vượt $1s$, hoặc mười điểm liên tiếp cùng phía trung tâm $\Rightarrow$ cảnh báo về **xu hướng trôi** (điện cực già, đèn yếu, chuẩn phân huỷ).

Điểm quan trọng về diễn giải: một điểm vượt $2s$ **không** tự động là lỗi — xác suất ngẫu nhiên của việc đó là 5 %. Chính vì thế mới cần bộ quy tắc kết hợp, cân bằng giữa phát hiện lỗi thật và báo động giả.

## Độ không đảm bảo đo

Khác với "sai số" (một giá trị cụ thể, thường không biết), độ không đảm bảo là một **khoảng** ước lượng được. Quy trình: liệt kê mọi nguồn (cân, dụng cụ định mức, đường chuẩn, độ lặp lại, độ tinh khiết chất chuẩn), quy về độ lệch chuẩn, tổ hợp theo quy tắc lan truyền, rồi nhân với hệ số phủ $k=2$ cho mức tin cậy khoảng 95 %.

Kết quả báo cáo có dạng: "$c = 12{,}4 \pm 0{,}6$ mg/L ($k=2$)". Giá trị trần trụi không kèm độ không đảm bảo là kết quả **chưa hoàn chỉnh**.

## Thử nghiệm thành thạo liên phòng

Nhiều phòng cùng phân tích một mẫu đồng nhất; kết quả đánh giá bằng điểm $z$, đạt khi $|z|\le 2$. Đây là cách duy nhất phát hiện sai số hệ thống mà kiểm soát nội bộ không thể thấy, vì nó nhất quán ở mọi lần đo của chính phòng đó.

**Lỗi thường gặp:**
- Chỉ theo dõi quy tắc $1_{3s}$ — sai vì nó chỉ bắt được sự cố lớn đã xảy ra; các quy tắc nhiều điểm như $4_{1s}$ và $10_{\bar x}$ phát hiện xu hướng trôi từ nhiều ngày trước, khi còn kịp ngăn chặn.
- Loại bỏ lô ngay khi một điểm vượt $2s$ — sai vì xác suất ngẫu nhiên của sự kiện đó là khoảng 5 %; loại lô mỗi lần như vậy tạo quá nhiều báo động giả và làm mất niềm tin vào chính hệ thống kiểm soát.
- Báo cáo kết quả không kèm độ không đảm bảo đo — sai vì người dùng kết quả không có cách nào đánh giá liệu hai giá trị có khác nhau thật hay không; một con số trần trụi là kết quả chưa hoàn chỉnh.
- Cho rằng kiểm soát nội bộ tốt là đủ — sai vì sai số hệ thống của chính phòng thí nghiệm (chuẩn gốc sai, phương pháp có độ chệch) nhất quán ở mọi lần đo nên biểu đồ kiểm soát vẫn đẹp; chỉ thử nghiệm thành thạo liên phòng mới phát hiện được.

<sub>`lesson.chemistry.hoa-phan-tich.kiem-soat-chat-luong`</sub>

---
