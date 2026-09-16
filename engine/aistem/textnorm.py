"""Chuẩn hoá văn bản tiếng Việt và LaTeX.

Hai việc tách bạch:

* `fold()` — bỏ dấu tiếng Việt, hạ chữ thường. Dùng cho cột tìm kiếm không dấu,
  để gõ "dao ham" vẫn ra "đạo hàm".
* `clean_latex()` — gọt LaTeX về dạng SymPy nuốt được. Kho AISTEM lưu LaTeX
  thuần (không bọc `$`), nhưng vẫn có `\\dfrac`, `\\vec`, `\\text{...}`,
  `\\left(`, `\\,` … là những thứ parser hay vấp.
"""

from __future__ import annotations

import hashlib
import math
import re
import unicodedata

# Đ/đ không tách được bằng NFD nên phải thay tay trước.
_D_MAP = str.maketrans({"Đ": "D", "đ": "d"})


def strip_diacritics(text: str) -> str:
    """Bỏ toàn bộ dấu tiếng Việt, giữ nguyên chữ và khoảng trắng."""
    if not text:
        return ""
    text = text.translate(_D_MAP)
    decomposed = unicodedata.normalize("NFD", text)
    return "".join(ch for ch in decomposed if unicodedata.category(ch) != "Mn")


def fold(text: str) -> str:
    """Dạng chuẩn để so khớp: không dấu, chữ thường, gộp khoảng trắng."""
    return re.sub(r"\s+", " ", strip_diacritics(text or "").lower()).strip()


def search_blob(*parts: object) -> str:
    """Ghép nhiều mẩu thành một chuỗi tìm kiếm: bản có dấu + bản không dấu.

    Giữ cả hai để BM25 khớp được cả truy vấn gõ dấu lẫn gõ không dấu.
    """
    chunks: list[str] = []
    for part in parts:
        if part is None:
            continue
        if isinstance(part, (list, tuple, set)):
            chunks.extend(str(x) for x in part if x)
        elif isinstance(part, dict):
            chunks.extend(f"{k} {v}" for k, v in part.items())
        else:
            chunks.append(str(part))
    joined = " ".join(c.strip() for c in chunks if str(c).strip())
    folded = fold(joined)
    return f"{joined} {folded}" if folded and folded != joined.lower() else joined


# --------------------------------------------------------------------------- #
# LaTeX
# --------------------------------------------------------------------------- #

_WRAPPERS = [
    (re.compile(r"^\s*\$\$(.*)\$\$\s*$", re.S), r"\1"),
    (re.compile(r"^\s*\$(.*)\$\s*$", re.S), r"\1"),
    (re.compile(r"^\s*\\\[(.*)\\\]\s*$", re.S), r"\1"),
    (re.compile(r"^\s*\\\((.*)\\\)\s*$", re.S), r"\1"),
]

# Lệnh chỉ mang nghĩa trình bày — bỏ tên lệnh, giữ nội dung trong ngoặc.
#
# `bar`, `hat`, `tilde` KHÔNG nằm ở đây: chúng đổi nghĩa của ký hiệu chứ không
# chỉ đổi cách vẽ. Xem `_DECORATION_RE` bên dưới.
_UNWRAP_CMDS = (
    "vec", "overrightarrow", "mathbf", "mathrm",
    "textbf", "textit", "operatorname", "displaystyle", "boldsymbol", "mathit",
)
_UNWRAP_RE = re.compile(r"\\(?:{})\s*\{{([^{{}}]*)\}}".format("|".join(_UNWRAP_CMDS)))

# --------------------------------------------------------------------------- #
# `\text{...}` nằm trong CHỈ SỐ DƯỚI là một phần của tên ký hiệu
# --------------------------------------------------------------------------- #
#
# `U_{\text{eff}}`, `n_{\text{dư}}`, `P_{\text{tổng}}` — ở đây `\text` không phải
# chú thích cũng không phải đơn vị, nó là **tên** của đại lượng. Gỡ như chú thích
# để lại `U_{}` và parser chết ngay tại đó; 61 bước trong kho mất trắng vì vậy.
#
# Nhãn được mã hoá thành một chỉ số **bằng số** chứ không giữ nguyên chữ, vì
# parser LaTeX của SymPy đọc chỉ số nhiều chữ cái thành TÍCH của từng chữ:
# `n_{eff}` ra `n_{e*f*f}`. Tích thì có cấu trúc đại số — hai nhãn khác nghĩa mà
# trùng tập chữ cái (`x_{ab}+x_{cd}` với `x_{ad}+x_{cb}`) sẽ so ra "khác nhau"
# và một bước đúng bị kết tội. `X_{412345}` thì SymPy đọc thành **một** ký hiệu
# nguyên khối, không có cấu trúc nào để so nhầm.
_INDEX_GROUP_RE = re.compile(r"(?<=_)\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
_INDEX_TEXT_RE = re.compile(r"\\text(?:rm|bf|it)?\s*\{([^{}]*)\}")

#: Chỉ số dành riêng cho ký pháp Newton, để không đụng dải băm của nhãn chữ.
_DOT_INDEX = {"dot": "900001", "ddot": "900002"}


def _index_token(label: str) -> str:
    """Nhãn chữ trong chỉ số dưới -> một token parser đọc được thành MỘT ký hiệu."""
    slug = re.sub(r"[^A-Za-z0-9]", "", strip_diacritics(label))
    if not slug:
        return ""  # nhãn rỗng: để nguyên cho `_TEXT_RE` xử lí như cũ
    # Số và chữ cái đơn vốn đã là một token nguyên khối, giữ nguyên cho dễ đọc.
    if slug.isdigit() or (len(slug) == 1 and slug.isalpha()):
        return slug
    digest = hashlib.sha1(slug.lower().encode()).hexdigest()
    return str(100000 + int(digest[:8], 16) % 800000)


def _rewrite_index_labels(source: str) -> str:
    """Đổi `X_{\\text{nhãn}}` thành `X_{<số>}`. Chỉ đụng chỉ số DƯỚI.

    Chỉ số TRÊN cố ý không xử lí: `K_M^{\\text{bk}}` là nhãn chứ không phải số mũ,
    mà mọi cách viết lại nó đều là một phỏng đoán — bỏ nhãn đi thì `K_M^{bk}` và
    `K_M` nhập làm một và `\\frac{K_M^{bk}}{K_M} = 3{,}00` thành `1 = 3`, tức là
    kết tội oan. Để nguyên thì parser bó tay và ta trả "chưa kết luận", an toàn hơn.
    """

    def _group(match: re.Match[str]) -> str:
        inner = match.group(1)
        if "\\text" not in inner:
            return match.group(0)

        def _label(hit: re.Match[str]) -> str:
            token = _index_token(hit.group(1))
            return token or hit.group(0)

        return "{" + _INDEX_TEXT_RE.sub(_label, inner) + "}"

    return _INDEX_GROUP_RE.sub(_group, source)


# Ký pháp Newton cho đạo hàm theo thời gian: `\dot{\theta}`, `\ddot{x}`.
# Bắt buộc phải là ký hiệu KHÁC với `\theta`/`x` — nhập làm một thì phương trình
# chuyển động `\ddot{\theta} = -\frac{g}{L}\theta` thành một đẳng thức sai hiển
# nhiên và bước đúng bị bác bỏ.
#: `(?![A-Za-z])` là bắt buộc: không có nó thì `\dots` khớp `\dot` + `s` và dấu
#: chấm lửng biến thành một ký hiệu bịa.
_NEWTON_DOT_RE = re.compile(
    r"\\(d?dot)(?![A-Za-z])\s*(?:\{\s*(\\?[A-Za-z]+)\s*\}|(\\[A-Za-z]+|[A-Za-z]))"
)


def _newton_dot(match: re.Match[str]) -> str:
    return f"{match.group(2) or match.group(3)}_{{{_DOT_INDEX[match.group(1)]}}}"


# --------------------------------------------------------------------------- #
# Ký hiệu có mũ trang trí: `\bar{x}`, `\hat{p}`, `\tilde{\nu}`
# --------------------------------------------------------------------------- #

#: Gạch ngang trên đầu là **trung bình mẫu**, mũ nón là **ước lượng** — chúng là
#: những đại lượng khác hẳn ký hiệu trần cùng tên. Gỡ mũ đi (cách làm cũ) thì
#: `\bar{x}` và `x` nhập làm một, và hỏng theo cả hai chiều trong cùng một bước:
#:
#: * `z = \frac{x - \bar{x}}{s}` thành `z = \frac{x - x}{s}`, tức `z = 0` —
#:   công thức điểm chuẩn hoá bị đọc thành hằng số 0;
#: * `\operatorname{rank} A = \operatorname{rank} \bar{A} = 1` thành
#:   `rank A = rank A`, hai vế trùng khít nên bước được **xác nhận** — hệ thống
#:   tự dựng ra một hằng đẳng thức rồi khen chính nó. Đây là kiểu hỏng tệ nhất:
#:   một lời xác nhận không có nội dung nào.
#:
#: Cách chữa là đổi tên chứ không phải chặn: `\bar{x}` → `x_{bar}` cho ra một
#: ký hiệu riêng biệt, nên bước vẫn kiểm được mà không còn nhập nhằng.
#: Chỉ số dưới đi ngay sau phải nuốt vào cùng (`\bar{p}_{1}` → `p_{bar1}`),
#: vì `p_{bar}_{1}` là cú pháp parser không đọc nổi.
_DECORATION_RE = re.compile(
    r"\\(bar|overline|hat|widehat|tilde)\s*\{([^{}]*)\}"
    r"(?:\s*_\s*(?:\{([^{}]*)\}|(\w)))?"
)


def _decoration_name(match: re.Match) -> str:
    kind = "bar" if match.group(1) in {"bar", "overline"} else (
        "hat" if match.group(1) in {"hat", "widehat"} else "tilde"
    )
    body = match.group(2).strip()
    subscript = (match.group(3) or match.group(4) or "").strip()
    if not body:
        return match.group(0)
    tag = f"{kind}{subscript}".replace(" ", "")
    return f"{body}_{{{tag}}}"


#: Ký pháp độ: `\cos 30^{\circ}`, `\theta = 14{,}48^{\circ}`.
#:
#: Bỏ qua nó không phải là "chưa kiểm" mà là **đọc sai**: `\cos 30^{\circ}` mất
#: mũ tròn thì thành `\cos 30` = cos(30 radian) = 0,154 thay vì 0,866. Không lỗi
#: nào ném ra, chỉ có một con số sai. Vì thế mũ tròn được đổi thẳng sang radian.
#:
#: Ba hàng rào, vì `^\circ` trong kho mang tới bốn nghĩa khác nhau:
#:
#: * **cơ số phải là chữ số.** `\Delta H_{f}^{\circ}`, `E^{\circ}`, `K^{\circ}`
#:   là trạng thái chuẩn trong Hoá — mũ tròn dán vào *tên đại lượng*, không phải
#:   vào một con số. Chặn cả `_` phía trước để `H_2^{\circ}` không lọt.
#: * **không được theo sau bởi C/F/K.** `42{,}5\ ^{\circ}\text{C}` là độ Celsius,
#:   một nhiệt độ chứ không phải một góc; quy sang radian là sai hoàn toàn.
#: * **`\circ` không khớp thì vẫn bị chặn.** Hàm này không đụng tới `\circ` đứng
#:   một mình (phép hợp `f \circ g`) hay mũ tròn trên tên đại lượng; danh sách
#:   `_UNSUPPORTED_RE` bên phía kiểm chứng vẫn bắt được chúng như trước.
_DEGREE_RE = re.compile(
    r"(?<![A-Za-z0-9_])"
    r"(\d+(?:\s*\{\s*,\s*\}\s*\d+|\.\d+)?)"
    r"(?:\\[,;:!]|\\ |\s)*\^\s*(?:\{\s*\\circ\s*\}|\\circ)"
    r"(?!(?:\\[,;:!]|\\ |\s)*"
    r"(?:\\(?:text|mathrm|rm|mbox)\s*\{\s*[CFK]|[CFK](?![A-Za-z])))"
)


#: `3^{\circ} > 2^{\circ} > 1^{\circ}` — chỉ gồm chữ số mang mũ tròn và dấu so.
_DEGREE_RANKING_RE = re.compile(
    r"\s*\d\s*\^\s*(?:\{\s*\\circ\s*\}|\\circ)"
    r"(?:\s*(?:>|<|\\gg|\\ll|\\ge|\\le|\\geq|\\leq|≥|≤|,)\s*"
    r"\d\s*\^\s*(?:\{\s*\\circ\s*\}|\\circ))+\s*"
)


def normalise_degrees(latex: str) -> str:
    """Đổi `<số>^\\circ` sang radian. Giữ nguyên mọi `\\circ` còn lại.

    Kết quả là một số thực chứ không phải `\\frac{30\\pi}{180}`, và đó là chủ ý:
    parser LaTeX của SymPy đọc `\\pi` thành **ký hiệu tự do**, không phải hằng số,
    nên `\\cos 30^{\\circ}` viết theo lối phân số sẽ còn ẩn và không tính ra số nào
    cả. Sửa `\\pi` ở tầm toàn cục thì đụng tới 328 bước ngoài phạm vi đòn bẩy này
    — một việc riêng, cần đo riêng. Sai số của phép đổi nằm ở hàng 1e-16, thấp
    hơn ngưỡng làm tròn của bộ kiểm chứng nhiều bậc.
    """
    if not latex or "\\circ" not in latex:
        return latex or ""
    # Cả dòng chỉ gồm những `<chữ số>^\circ` nối bằng dấu so sánh là một BẢNG
    # XẾP HẠNG, không phải phép tính góc: `3^{\circ} > 2^{\circ} > 1^{\circ}` là
    # bậc carbocation trong Hoá hữu cơ. Quy sang radian rồi "xác nhận" thứ tự
    # 0,0349 > 0,0175 là một lời xác nhận rỗng — nó kiểm đúng cái nó vừa tự bịa.
    if _DEGREE_RANKING_RE.fullmatch(latex.strip()):
        return latex

    def _swap(match: re.Match) -> str:
        number = re.sub(r"\s*\{\s*,\s*\}\s*", ".", match.group(1))
        try:
            return f"({math.radians(float(number))!r})"
        except ValueError:  # pragma: no cover - regex đã chặn dạng lạ
            return match.group(0)

    return _DEGREE_RE.sub(_swap, latex)


# `\text{...}` thường là chú thích hoặc đơn vị trong công thức — bỏ hẳn.
#
# Phải nuốt luôn số mũ đi kèm. `18\ \text{g/m}^3` là "18 gam trên mét khối":
# bỏ mỗi `\text{g/m}` sẽ để lại `18 ^3`, và CAS đọc thành 18³ = 5832. Một con
# số bị nhân lên 324 lần mà không có lỗi nào ném ra — đúng loại hỏng tệ nhất.
#
# Và phải gỡ **cả cụm** khi nhiều mẩu nối nhau: `\text{s}^{2}/\text{m}^{3}` là
# một đơn vị duy nhất. Gỡ từng mẩu để lại dấu `/` lơ lửng ở cuối, và một vế vốn
# đọc được trở thành không đọc được. Ngược lại `1 + 2 + \text{ghi chú}` chỉ có
# một mẩu, nên dấu `+` cụt vẫn còn — đúng như mong muốn, vì ở đó ta thật sự
# không biết cái bị gỡ đi đáng giá bao nhiêu.
_TEXT_ATOM = r"\\text(?:rm|bf|it)?\s*\{[^{}]*\}(?:\s*\^\s*\{?\s*-?\d+\s*\}?)?"
_TEXT_RE = re.compile(rf"{_TEXT_ATOM}(?:\s*(?:\\cdot|·|/|\*)\s*{_TEXT_ATOM})*")

_TRIG_FUNCS = (
    "sinh", "cosh", "tanh", "arcsin", "arccos", "arctan",
    "sin", "cos", "tan", "cot", "sec", "csc", "ln", "log", "exp",
)
_TRIG_ARG_RE = re.compile(
    r"\\({})\s+(\d+\s*\\?[A-Za-z]+(?:_\{{?\w+\}}?)?)".format("|".join(_TRIG_FUNCS))
)

_SPACING_RE = re.compile(r"\\[,;:!>]|\\quad|\\qquad|\\ (?=\S)|~")
_LEFTRIGHT_RE = re.compile(r"\\(?:left|right|bigl|bigr|Bigl|Bigr|big|Big)\s*(?=[([{|.\\\])}])")


def clean_latex(latex: str) -> str:
    """Gọt LaTeX về dạng SymPy dễ nuốt. Không đổi nghĩa toán học."""
    if not latex:
        return ""
    s = latex.strip()

    for pattern, repl in _WRAPPERS:
        s = pattern.sub(repl, s).strip()

    # Hai phép này phải chạy TRƯỚC khi gỡ `\text{...}` và `\mathrm{...}`:
    # dấu hiệu phân biệt độ Celsius với góc nằm đúng trong cái `\text{C}` sắp bị
    # xoá, còn `\bar{x}` thì sắp bị `_UNWRAP_RE` bóc mất mũ.
    s = normalise_degrees(s)
    s = _DECORATION_RE.sub(_decoration_name, s)
    # Cũng phải chạy trước `_TEXT_RE`: nó gỡ `\text{...}` không cần biết đang
    # đứng ở đâu, mà trong chỉ số dưới thì `\text` là tên ký hiệu.
    s = _rewrite_index_labels(s)
    s = _NEWTON_DOT_RE.sub(_newton_dot, s)

    s = _TEXT_RE.sub(" ", s)
    for _ in range(3):  # lồng nhau tối đa vài lớp
        new = _UNWRAP_RE.sub(r"\1", s)
        if new == s:
            break
        s = new

    # Dấu thập phân kiểu Việt Nam. Kho viết `0{,}0241` — `{,}` là quy ước LaTeX
    # để dấu phẩy không bị hiểu là dấu ngắt. 31,5% số bước giải dùng cách này,
    # bỏ qua thì parser đọc `0{,}30125` thành số nguyên và mọi kiểm chứng sai hết.
    # Ngược lại KHÔNG đụng tới dấu phẩy trần: trong kho nó là chỉ số dưới
    # (`t_{1/2,1}`) hoặc phần tử bộ (`(1,1,1)`), không phải thập phân.
    s = re.sub(r"(\d)\s*\{\s*,\s*\}\s*(\d)", r"\1.\2", s)

    # `\cos 6\theta` theo quy ước LaTeX là cos(6θ), nhưng parser đọc thành
    # cos(6)·θ và mọi đồng nhất thức lượng giác sẽ bị báo sai. Bọc ngoặc lại.
    s = _TRIG_ARG_RE.sub(r"\\\1(\2)", s)

    s = s.replace(r"\dfrac", r"\frac").replace(r"\tfrac", r"\frac")
    s = s.replace(r"\cdot", "*").replace(r"\times", "*").replace(r"\div", "/")
    # `\neq` phải thay trước `\ne`, không thì `\neq` biến thành `!=q`.
    s = s.replace(r"\neq", "!=").replace(r"\ne ", "!= ")
    s = s.replace("^{\\prime}", "'").replace("^\\prime", "'")
    s = _LEFTRIGHT_RE.sub("", s)
    s = _SPACING_RE.sub(" ", s)
    s = re.sub(r"\s+", " ", s).strip()

    # Ngoặc trở nên rỗng sau khi gỡ `\text{...}` là **chú thích**, không phải
    # phép nhân: `4\ (\text{vòng thơm}) + 1\ (\text{nhóm C=O}) = 5` là "bốn cái
    # này cộng một cái kia bằng năm". Để lại `4 ( ) + 1` thì parser nuốt mất vế
    # sau và trả về đúng số `4`, rồi CAS kết luận `4 ≠ 5` — bác bỏ một lời giải
    # hoàn toàn đúng, mà không có lỗi nào ném ra.
    for _ in range(3):
        new = re.sub(r"(?<![A-Za-z\\])\(\s*\)", " ", s)
        if new == s:
            break
        s = re.sub(r"\s+", " ", new).strip()

    # Dấu cách phân nhóm hàng nghìn: `12\,000` gọt xong còn `12 000`. Parser
    # ghép hai cụm số dính nhau thành một, nên ở đây nó ra 12000 — đúng ý.
    # Gộp thẳng để cổng an toàn phía sau phân biệt được trường hợp này với
    # `5 \quad 7` (hai mệnh đề rời bị gọt thành `5 7`, ghép lại thành 57).
    for _ in range(4):
        new = re.sub(r"(?<=\d) (\d{3})(?![\d.,])", r"\1", s)
        if new == s:
            break
        s = new

    # Bỏ dấu chấm câu cuối dòng — kho có vài công thức kết thúc bằng "." hoặc ","
    s = re.sub(r"[.,;]+$", "", s).strip()
    # Dấu cách mỏng `\ ` đứng ngay trước phần vừa bị gỡ (thường là đơn vị) nay
    # trơ lại thành dấu gạch chéo cuối chuỗi, làm parser vấp.
    s = re.sub(r"\\+\s*$", "", s).strip()
    return s


# Chú thích điều kiện đi kèm cuối bước giải: "(x \neq 3)", "(với t > 0)", "(đpcm)".
# Chúng là văn bản cho người đọc, đưa vào parser sẽ bị hiểu nhầm thành phép nhân.
_ANNOTATION_RE = re.compile(
    r"\s*\((?=[^()]*(?:!=|<|>|\\neq|\\leq|\\geq|\\le\b|\\ge\b|\\forall|\\in\b|[^\x00-\x7f]))"
    r"[^()]*\)\s*$"
)


# Đơn vị dán ở cuối một kết quả số: `4,01 \times 10^{-3}\ \mathrm{s^{-1}}`.
# Giữ lại thì CAS thấy `mathrm` và `s` là ẩn nên không tính ra số nào cả.
_TRAILING_UNIT_RE = re.compile(
    r"(?:\\[,;:! ]|\s)*\\(?:mathrm|text|rm|operatorname|mathit|mbox)\s*"
    r"\{(?:[^{}]|\{[^{}]*\})*\}\s*$"
)


def strip_trailing_units(latex: str) -> str:
    """Bỏ phần đơn vị bám đuôi để còn lại thuần biểu thức số."""
    s = (latex or "").strip()
    for _ in range(3):
        new = _TRAILING_UNIT_RE.sub("", s).strip()
        if new == s or not new:
            break
        s = new
    return s


def strip_annotations(latex: str) -> str:
    """Bỏ phần chú thích điều kiện ở cuối một biểu thức."""
    s = (latex or "").strip()
    for _ in range(3):
        new = _ANNOTATION_RE.sub("", s).strip()
        if new == s or not new:
            break
        s = new
    return s


def split_equation(latex: str, *, clean: bool = True) -> list[str]:
    """Tách `a = b = c` thành ['a', 'b', 'c'].

    Bỏ qua `=` nằm trong `\\leq`, `\\geq`, `!=` và trong ngoặc nhọn.

    Cố ý chỉ tách theo `=`, dù `split_relations` bên dưới tách được cả `≈` và
    bất đẳng thức: những chỗ gọi hàm này (`sides()`, phần rút giá trị số của
    một bước, `carry` giữa hai bước) hiểu "phần tử cuối" là **vế phải cuối cùng
    của một đẳng thức**. Tách thêm theo `<` thì vế cuối của `n = 12 < 30` thành
    `30`, và đáp số của bài sẽ bị đối chiếu với một cận.

    `clean=False` giữ nguyên chuỗi gốc. Dùng khi cần đọc những thứ mà
    `clean_latex` cố tình gỡ đi — điển hình là đơn vị: `0{,}0252\\ \\mathrm{g} =
    25{,}2\\ \\mathrm{mg}` gọt xong chỉ còn `0.0252 = 25.2`, và nếu không biết
    hai vế viết ở hai đơn vị khác nhau thì đó trông y hệt một lỗi số học.
    """
    s = strip_annotations(clean_latex(latex)) if clean else str(latex or "").strip()
    if not s:
        return []
    parts: list[str] = []
    depth = 0
    buf: list[str] = []
    i = 0
    while i < len(s):
        ch = s[i]
        if ch in "{([":
            depth += 1
        elif ch in "})]":
            depth -= 1
        if ch == "=" and depth == 0:
            prev = s[i - 1] if i else ""
            nxt = s[i + 1] if i + 1 < len(s) else ""
            # `prev and` là bắt buộc: chuỗi rỗng là chuỗi con của mọi chuỗi, nên
            # `"" in "<>!:"` cho True và dấu `=` mở đầu dòng sẽ không bao giờ
            # được tách — đúng lối viết nối tiếp phổ biến nhất trong kho.
            if (prev and prev in "<>!:=") or nxt == "=":
                buf.append(ch)
                i += 1
                continue
            parts.append("".join(buf).strip())
            buf = []
            i += 1
            continue
        buf.append(ch)
        i += 1
    parts.append("".join(buf).strip())
    return [p for p in parts if p]


#: Các quan hệ tách được ở mức ngoài cùng của một chuỗi biến đổi.
#:
#: Thứ tự trong phép hoặc là bắt buộc: `\\leqslant` phải đứng trước `\\leq`,
#: `\\leq` trước `\\le`, `<=` trước `<`. Lối viết dài mà bị `\\le` nuốt mất hai
#: chữ đầu thì phần còn lại (`q`, `qslant`) dính vào vế phải và cả mắt xích hỏng.
#: `(?![A-Za-z])` giữ cho `\\le` không khớp vào `\\left`, `\\ll` không khớp
#: `\\llcorner` — đúng loại hỏng im lặng: chuỗi vẫn tách, chỉ là tách sai chỗ.
_RELATION_RE = re.compile(
    r"\\approxeq|\\approx|\\simeq|\\cong|≈"
    r"|\\leqslant|\\leq|\\le(?![A-Za-z])|<=|≤"
    r"|\\geqslant|\\geq|\\ge(?![A-Za-z])|>=|≥"
    r"|\\ll(?![A-Za-z])|≪|\\gg(?![A-Za-z])|≫"
    r"|!=|\\neq|\\ne(?![A-Za-z])|≠"
    r"|<|>|="
)

#: Mọi cách viết của cùng một quan hệ quy về một ký hiệu, để nơi dùng chỉ phải
#: xét chín trường hợp thay vì hai chục cách gõ LaTeX.
_RELATION_CANON = {
    "\\approx": "≈", "\\approxeq": "≈", "\\simeq": "≈", "\\cong": "≈", "≈": "≈",
    "\\leqslant": "<=", "\\leq": "<=", "\\le": "<=", "<=": "<=", "≤": "<=",
    "\\geqslant": ">=", "\\geq": ">=", "\\ge": ">=", ">=": ">=", "≥": ">=",
    "\\ll": "≪", "≪": "≪", "\\gg": "≫", "≫": "≫",
    "!=": "!=", "\\neq": "!=", "\\ne": "!=", "≠": "!=",
    "<": "<", ">": ">", "=": "=",
}


def starts_with_relation(latex: str) -> bool:
    """Chuỗi **thô** có mở đầu bằng một quan hệ không?

    Phải hỏi trên chuỗi thô, không phải chuỗi đã gọt. `\\text{cận dưới} = 16 +
    5 + 8 = 29` sau khi gỡ `\\text{...}` cũng bắt đầu bằng `=`, nhưng nó không
    phải bước nối tiếp — vế trái của nó là cái nhãn vừa bị gỡ. Nối nó vào vế
    phải của bước trước là dựng ra một đẳng thức không ai viết, đúng kiểu
    `P_1 = 0{,}5 \\qquad P_2 = 0{,}4` bị nối thành `0{,}5 = P_2`.
    """
    return bool(_RELATION_RE.match((latex or "").lstrip()))


def split_relations(latex: str, *, clean: bool = True) -> tuple[list[str], list[str]]:
    """Tách `a = b ≈ c < d` thành (['a','b','c','d'], ['=','≈','<']).

    Một dòng lời giải hiếm khi chỉ có một loại quan hệ:
    `\\left|R\\right| \\le \\frac{1}{1320} \\approx 0.00076 < 0.001` là bốn vế
    nối bằng ba quan hệ **khác nhau**. Gộp cả dòng thành một vế duy nhất thì
    parser chịu thua và không kiểm được gì; tách mà quên quan hệ nào đi với mắt
    xích nào thì lại đem so `0.00076` với `0.001` bằng dấu `=`. Vì vậy trả về
    hai danh sách song song: `len(ops) == len(parts) - 1` luôn đúng.

    Vế đầu (hoặc vế cuối) có thể là chuỗi rỗng — đó chính là lối viết nối tiếp
    `= \\frac{x+3}{x-2}` mở đầu bằng quan hệ. Giữ lại chỗ trống ấy thay vì lọc
    đi, để nơi gọi biết mà nối vào vế phải của bước trước.

    `clean=False` giữ nguyên chuỗi gốc, để đọc được những thứ `clean_latex` cố
    tình gỡ — đơn vị là trường hợp duy nhất đang dùng tới.
    """
    s = strip_annotations(clean_latex(latex)) if clean else str(latex or "").strip()
    if not s:
        return [], []
    parts: list[str] = []
    ops: list[str] = []
    depth = 0
    buf: list[str] = []
    i = 0
    while i < len(s):
        ch = s[i]
        match = _RELATION_RE.match(s, i) if depth == 0 else None
        if match:
            token = match.group(0)
            # `:=` là ký hiệu định nghĩa, `==` là dấu bằng gõ đôi — cả hai không
            # phải hai quan hệ liên tiếp. Cùng lí do với `split_equation`.
            prev = s[i - 1] if i else ""
            if token == "=" and ((prev and prev in ":=") or s[i + 1 : i + 2] == "="):
                buf.append(ch)
                i += 1
                continue
            parts.append("".join(buf).strip())
            ops.append(_RELATION_CANON[token])
            buf = []
            i = match.end()
            continue
        if ch in "{([":
            depth += 1
        elif ch in "})]":
            depth -= 1
        buf.append(ch)
        i += 1
    parts.append("".join(buf).strip())
    return parts, ops


#: Chữ số mũ dạng Unicode: kho viết `10³`, `s⁻¹`, `M⁻¹` chứ không phải `10^3`.
_SUPERSCRIPTS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "0123456789+-")
_SUPERSCRIPT_RE = re.compile(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻]+)")

#: Phần định trị: số thập phân, chấp nhận cả dấu phẩy Việt Nam và `{,}` của LaTeX.
#: Số phải KHÔNG đứng ngay sau một chữ cái — nếu không thì `Q10`, `H2`, `Vmax`
#: bị đọc thành số và đáp án `Q10 ≈ 2,31` cho ra 10 thay vì 2,31.
_MANTISSA = r"(?<![A-Za-zÀ-ỹ])[-+]?(?:\d+(?:\s*\{\s*,\s*\}\s*|[.,])?\d*|\.\d+)"
#: Phần mũ: `× 10^{-4}`, `x 10^-4`, `e-4`, `·10⁻⁴`.
#: Dấu nhân trước `10^n`. Kho VN còn dùng cả dấu chấm — `8,64.10^-3` nghĩa là
#: 8,64 × 10⁻³, một quy ước rất phổ biến trong sách giáo khoa Việt Nam.
_EXPONENT = r"(?:\s*(?:\\times|\\cdot|[×·xX*eE.])\s*10\s*\^?\s*\{?\s*([-+]?\d+)\s*\}?)"
_NUM_RE = re.compile(f"({_MANTISSA})({_EXPONENT})?")

#: Phân số hai số nguyên: `27/64`, `3/64`. Sau nó không được là chữ cái, để
#: `m/s` hay `mol/L` không bị hiểu là phân số.
_FRACTION_RE = re.compile(
    r"(?<![A-Za-zÀ-ỹ\d])(-?\d+)\s*/\s*(\d+)(?![\d]*\s*[A-Za-zÀ-ỹ])"
)

#: Đáp án hay viết dạng "nhãn = giá trị" hoặc "nhãn ≈ giá trị":
#: `d(X/H2) = 18,125`, `Q10 ≈ 2,31`. Giá trị nằm ở vế phải.
_LABELLED_RE = re.compile(r"^.{0,40}?[=≈]\s*(.+)$", re.S)


#: Dấu cách phân nhóm hàng nghìn: `12 000`, `660 000`. Rất phổ biến trong văn
#: bản tiếng Việt. Chỉ gộp khi nhóm sau đúng ba chữ số và không có chữ số nào
#: nữa theo sau — `2 000` là hai nghìn, còn `2 00` thì không phải cách viết nào.
_THOUSANDS_RE = re.compile(r"(?<=\d)[\u00a0\u202f ](\d{3})(?![\d.,])")


def _normalise_numeric_text(text: str) -> str:
    source = str(text).strip()
    source = re.sub(r"(\d)\s*\{\s*,\s*\}\s*(\d)", r"\1.\2", source)
    source = re.sub(r"\\(?:approx|simeq|sim|cong)\b", "≈", source)
    for _ in range(3):  # `1 234 567` cần gộp nhiều lượt
        collapsed = _THOUSANDS_RE.sub(r"\1", source)
        if collapsed == source:
            break
        source = collapsed
    # `10³` -> `10^3`, `s⁻¹` -> `s^-1`
    return _SUPERSCRIPT_RE.sub(lambda m: "^" + m.group(1).translate(_SUPERSCRIPTS), source)


def extract_number(text: str) -> float | None:
    """Rút giá trị số ra khỏi một đáp án.

    Kho viết đáp án theo rất nhiều kiểu, và mỗi kiểu bỏ sót đều thành một lần
    chấm oan:

    * dấu phẩy thập phân Việt Nam — `9,8`
    * dấu thập phân LaTeX — `2{,}5`
    * ký hiệu khoa học mọi biến thể — `3.2 \\times 10^{-4}`, `2,68 × 10³`
    * phân số — `27/64`
    * có nhãn ở đầu — `Q10 ≈ 2,31`, `d(X/H2) = 18,125`

    Hai quy tắc quan trọng nhất: giá trị nằm ở **vế phải** của dấu `=`/`≈` nếu
    có, và một con số dính ngay sau chữ cái (`Q10`, `H2`) là **một phần của tên
    ký hiệu**, không phải giá trị.
    """
    if text is None:
        return None
    if isinstance(text, (int, float)):
        return float(text)

    source = _normalise_numeric_text(text)

    # Có nhãn thì chỉ đọc vế phải; vế trái là tên đại lượng.
    labelled = _LABELLED_RE.match(source)
    if labelled:
        value = _extract_from(labelled.group(1))
        if value is not None:
            return value
    return _extract_from(source)


def _extract_from(source: str) -> float | None:
    fraction = _FRACTION_RE.search(source)
    if fraction:
        numerator, denominator = int(fraction.group(1)), int(fraction.group(2))
        if denominator:
            return numerator / denominator

    match = _NUM_RE.search(source)
    if not match:
        return None
    try:
        value = float(match.group(1).strip().replace(",", ".").rstrip("."))
    except ValueError:
        return None
    if match.group(3):
        value *= 10 ** int(match.group(3))
    return value


def slugify(text: str) -> str:
    """Chuỗi -> slug không dấu, dùng cho id sinh mới."""
    s = fold(text)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")[:64] or "x"
