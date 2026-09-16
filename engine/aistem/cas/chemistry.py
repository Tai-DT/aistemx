"""Kiểm chứng hoá học: cân bằng nguyên tử và khối lượng mol.

Đây là một **trục kiểm chứng khác hẳn** phần còn lại của lớp CAS. SymPy so hai
biểu thức bằng cách rút gọn hiệu; ở đây không có biểu thức nào cả — chỉ có phép
đếm nguyên tử hai bên mũi tên. Đổi lại, kết luận chắc tay hơn nhiều: một phương
trình không cân bằng là sai theo định luật bảo toàn khối lượng, không có ngữ
cảnh nào cứu được nó.

Chính vì kết luận chắc nên **hàng rào nhận dạng phải rất chặt**. Rủi ro lớn nhất
của module này không phải đếm sai nguyên tử — phép đếm là số học thuần — mà là
nhận nhầm một bước Toán thành phương trình hoá học. `\\lim_{x \\to 3}` và
`X \\rightarrow Y` (di chuyển nước giữa hai tế bào, môn Sinh) đều có mũi tên;
đọc bừa chúng rồi báo "không cân bằng" là kiểu báo oan tệ nhất mà hệ thống này
có thể mắc. Nguyên tắc xuyên suốt: **mọi ký tự phải được nhận ra**. Còn sót một
mẩu không hiểu ở bất kỳ đâu trong phương trình thì trả `unknown`, không đoán.
"""

from __future__ import annotations

import re
from collections import Counter
from fractions import Fraction
from typing import Literal

ChemVerdict = Literal["balanced", "unbalanced", "unknown"]

# --------------------------------------------------------------------------- #
# Bảng nguyên tử khối
# --------------------------------------------------------------------------- #

#: Khối lượng nguyên tử trung bình theo IUPAC (u). Đủ 92 nguyên tố đầu — kho
#: giáo dục không đụng tới nguyên tố siêu urani.
ATOMIC_MASS: dict[str, float] = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.011,
    "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180, "Na": 22.990,
    "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06,
    "Cl": 35.45, "Ar": 39.948, "K": 39.098, "Ca": 40.078, "Sc": 44.956,
    "Ti": 47.867, "V": 50.942, "Cr": 51.996, "Mn": 54.938, "Fe": 55.845,
    "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38, "Ga": 69.723,
    "Ge": 72.630, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798,
    "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906,
    "Mo": 95.95, "Tc": 98.0, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42,
    "Ag": 107.87, "Cd": 112.41, "In": 114.82, "Sn": 118.71, "Sb": 121.76,
    "Te": 127.60, "I": 126.90, "Xe": 131.29, "Cs": 132.91, "Ba": 137.33,
    "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24, "Pm": 145.0,
    "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.50,
    "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.05, "Lu": 174.97,
    "Hf": 178.49, "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23,
    "Ir": 192.22, "Pt": 195.08, "Au": 196.97, "Hg": 200.59, "Tl": 204.38,
    "Pb": 207.2, "Bi": 208.98, "Po": 209.0, "At": 210.0, "Rn": 222.0,
    "Fr": 223.0, "Ra": 226.0, "Ac": 227.0, "Th": 232.04, "Pa": 231.04,
    "U": 238.03,
}

#: Sách giáo khoa Việt Nam và đề thi phổ thông dùng nguyên tử khối làm tròn
#: (H = 1, C = 12, O = 16, Cl = 35,5, Cu = 64, Fe = 56…) và **cả bài giải được
#: viết theo bộ số ấy**. Nếu chỉ đối chiếu với giá trị IUPAC thì `M_{CuO} = 80`
#: (64 + 16) sẽ bị coi là sai trong khi nó đúng theo đúng quy ước bài đang dùng.
#: Nên bộ kiểm chấp nhận cả hai bảng, và chỉ kết tội khi lệch cả hai.
TEXTBOOK_MASS: dict[str, float] = {
    "H": 1.0, "He": 4.0, "Li": 7.0, "Be": 9.0, "B": 11.0, "C": 12.0, "N": 14.0,
    "O": 16.0, "F": 19.0, "Ne": 20.0, "Na": 23.0, "Mg": 24.0, "Al": 27.0,
    "Si": 28.0, "P": 31.0, "S": 32.0, "Cl": 35.5, "Ar": 40.0, "K": 39.0,
    "Ca": 40.0, "Cr": 52.0, "Mn": 55.0, "Fe": 56.0, "Ni": 59.0, "Cu": 64.0,
    "Zn": 65.0, "Br": 80.0, "Ag": 108.0, "Sn": 119.0, "I": 127.0, "Ba": 137.0,
    "Pb": 207.0, "Hg": 201.0, "Au": 197.0, "Pt": 195.0, "Co": 59.0,
    "Sr": 88.0, "Cd": 112.0, "As": 75.0, "Se": 79.0, "Rb": 85.5, "Cs": 133.0,
}

#: Ký hiệu nguyên tố hai chữ phải thử trước ký hiệu một chữ, nếu không `Cl` bị
#: đọc thành `C` rồi `l` (mà `l` không phải nguyên tố → cả công thức hỏng).
_ELEMENT_RE = re.compile(
    "|".join(sorted(ATOMIC_MASS, key=lambda s: (-len(s), s)))
)

# --------------------------------------------------------------------------- #
# Gọt LaTeX về công thức hoá học trần
# --------------------------------------------------------------------------- #

#: Mũi tên phản ứng. `\to` nằm trong danh sách vì kho Hoá Việt Nam dùng nó thật
#: (`3\mathrm{Cu} + 8\mathrm{HNO_3} \to ...`), nhưng nó cũng là mũi tên giới hạn
#: của môn Toán — 104/211 bước có mũi tên trong kho là bước Toán. Hàng rào không
#: nằm ở đây mà ở chỗ hai vế phải đọc trọn vẹn thành công thức hoá học.
_ARROW_RE = re.compile(
    r"\\xrightarrow\s*(?:\[[^\[\]]*\])?\s*(?:\{(?:[^{}]|\{[^{}]*\})*\})?"
    r"|\\(?:rightarrow|longrightarrow|rightleftharpoons|leftrightarrow|to)\b"
    r"|→|⟶|⇌|↔"
)

#: Nhãn điều kiện trên mũi tên `\xrightarrow{Fe}`, `\xrightarrow[t^\circ]{H_2SO_4}`
#: là **xúc tác / điều kiện**, không tham gia cân bằng nên gỡ bỏ là đúng. Ngoại
#: lệ chết người: trong phổ khối kho viết `72 \xrightarrow{-\mathrm{CH_3}} 57`,
#: nhãn mang dấu `-`/`+` nghĩa là "mất/thêm mảnh này" và nó ĐỔI cân bằng. Gặp
#: nhãn như thế thì bỏ cả bước, không kiểm.
_ARROW_LABEL_RE = re.compile(
    r"\\xrightarrow\s*(?:\[[^\[\]]*\])?\s*\{\s*[-+]"
    r"|\\xrightarrow\s*\[\s*[-+]"
)

#: Trạng thái chất và ghi chú kết tủa / bay hơi — trình bày, không đổi số nguyên tử.
_STATE_RE = re.compile(
    r"\(\s*(?:s|l|g|aq|r|k|dd|gr|graphite|rắn|lỏng|khí)\s*\)"
    r"|\\(?:downarrow|uparrow|bullet|cdot\s*(?=\s|$))"
    r"|↓|↑"
)

#: Ký pháp chắc chắn KHÔNG phải hoá học. Có bất kỳ thứ nào thì bỏ cả bước — thà
#: bỏ sót còn hơn đem một biểu thức Toán đi đếm nguyên tử.
_NOT_CHEMISTRY_RE = re.compile(
    r"\\(?:lim|int|sum|prod|frac|dfrac|partial|infty|sqrt|log|ln|exp"
    r"|sin|cos|tan|cot|sec|csc|sinh|cosh|tanh|lfloor|choose|binom|nabla"
    r"|forall|exists|subset|cup|cap|mapsto|sim|propto|approx|neq|leq|geq"
    r"|le|ge|ll|gg|pm|mp|dots|cdots|ldots|hbar|nu|mu|alpha|beta|gamma"
    r"|delta|theta|lambda|sigma|omega|Delta|Omega|Psi|psi|phi|varphi|pi)\b"
    r"|[=<>≤≥≈≠∈∑∫√%]|\||\bd[A-Za-z]\b"
)

#: Hệ số dạng phân số: `\tfrac{3}{2}\mathrm{H_2}`. Kho Hoá VN viết bán phản ứng
#: kiểu này rất nhiều, bỏ qua thì mất hẳn một nhóm bài.
_FRAC_COEF_RE = re.compile(r"\\[dt]?frac\s*\{\s*(\d+)\s*\}\s*\{\s*(\d+)\s*\}")

#: Gạch nối trong công thức cấu tạo thu gọn (`CH_3\text{-}CH_3`,
#: `(CH_3)_2CBr\!-\!CH_2CH_3`) và nối ba (`HC\equiv CH`) chỉ là **liên kết**,
#: không phải phép trừ. Phân biệt với dấu trừ tách số hạng (`Fe - 2e^{-}`) bằng
#: khoảng trắng: liên kết viết dính, phép trừ viết rời.
_BOND_RE = re.compile(r"\\text\s*\{\s*-\s*\}|\\!-\\!|\\equiv|≡|(?<=[A-Za-z0-9)])-(?=[A-Za-z(])")

_MATHRM_RE = re.compile(r"\\(?:mathrm|mathbf|text|textrm|mbox|rm)\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
_SPACING_RE = re.compile(r"\\[,;:!>]|\\quad|\\qquad|\\ |~|\\left|\\right|\\,")


def _strip_latex(source: str) -> str:
    """Gỡ lớp trình bày LaTeX, giữ nguyên mọi ký tự mang nghĩa hoá học."""
    s = source
    for _ in range(4):  # `\mathrm{Ca(OH)_2}` lồng một lớp, `\mathrm{[Ag(NH_3)_2]}` hai lớp
        new = _MATHRM_RE.sub(r"\1", s)
        if new == s:
            break
        s = new
    s = _FRAC_COEF_RE.sub(lambda m: f"{m.group(1)}/{m.group(2)} ", s)
    s = _STATE_RE.sub(" ", s)
    s = _BOND_RE.sub("", s)
    s = _SPACING_RE.sub(" ", s)
    s = s.replace("\\overset{+}{", "{+}{").replace("\\overset{\\bullet}{", "{}{")
    return re.sub(r"\s+", " ", s).strip()


# --------------------------------------------------------------------------- #
# Đọc một công thức phân tử
# --------------------------------------------------------------------------- #

#: `2+`, `+`, `3-`, `-`, `+5` (số oxi hoá) — đều ở mũ.
_CHARGE_RE = re.compile(r"^\s*(?:(\d*)\s*([+-])|([+-])\s*(\d+))\s*$")


def _read_charge(token: str) -> int | None:
    """Đọc phần mũ thành điện tích. `2+` → +2, `-` → −1, `+5` → +5."""
    m = _CHARGE_RE.match(token)
    if not m:
        return None
    if m.group(2):
        return int(m.group(1) or 1) * (1 if m.group(2) == "+" else -1)
    return int(m.group(4)) * (1 if m.group(3) == "+" else -1)


class _Cursor:
    """Con trỏ đọc công thức. Tách ra thành lớp chỉ để `_read_group` gọi đệ quy."""

    def __init__(self, text: str) -> None:
        self.s = text
        self.i = 0

    def eof(self) -> bool:
        return self.i >= len(self.s)

    def peek(self) -> str:
        return self.s[self.i] if self.i < len(self.s) else ""


def _read_subscript(cur: _Cursor) -> int | None:
    """Chỉ số dưới sau một nguyên tố hay một nhóm ngoặc. Không có thì là 1."""
    s, i = cur.s, cur.i
    if i < len(s) and s[i] == "_":
        i += 1
        if i < len(s) and s[i] == "{":
            end = s.find("}", i)
            if end < 0:
                return None
            body = s[i + 1 : end]
            if not body.isdigit():
                return None  # chỉ số chữ (`(-CH_2-)_n`) → không kiểm được
            cur.i = end + 1
            return int(body)
        j = i
        while j < len(s) and s[j].isdigit():
            j += 1
        if j == i:
            return None
        cur.i = j
        return int(s[i:j])
    # Chỉ số viết trần, không có `_`: `H2SO4`. Kho dùng cả hai lối.
    j = i
    while j < len(s) and s[j].isdigit():
        j += 1
    if j > i:
        cur.i = j
        return int(s[i:j])
    return 1


def _read_superscript(cur: _Cursor) -> str | None:
    """Phần mũ thô (chưa diễn giải). Trả `""` khi không có mũ."""
    s, i = cur.s, cur.i
    if i >= len(s) or s[i] != "^":
        return ""
    i += 1
    if i < len(s) and s[i] == "{":
        end = s.find("}", i)
        if end < 0:
            return None
        cur.i = end + 1
        return s[i + 1 : end]
    j = i
    while j < len(s) and (s[j].isdigit() or s[j] in "+-"):
        j += 1
    if j == i:
        return None
    cur.i = j
    return s[i:j]


def _read_group(cur: _Cursor, depth: int = 0) -> tuple[Counter, int] | None:
    """Đọc một dãy nguyên tố / nhóm ngoặc. Trả (số nguyên tử, tổng điện tích)."""
    if depth > 6:
        return None
    atoms: Counter = Counter()
    charge = 0
    while not cur.eof():
        ch = cur.peek()
        if ch in ")]}":
            break
        if ch in "([":
            close = {"(": ")", "[": "]"}[ch]
            cur.i += 1
            inner = _read_group(cur, depth + 1)
            if inner is None or cur.peek() != close:
                return None
            cur.i += 1
            count = _read_subscript(cur)
            if count is None:
                return None
            raw = _read_superscript(cur)
            if raw is None:
                return None
            inner_atoms, inner_charge = inner
            for element, n in inner_atoms.items():
                atoms[element] += n * count
            charge += inner_charge * count
            if raw:
                q = _read_charge(raw)
                if q is None:
                    return None
                charge += q
            continue
        match = _ELEMENT_RE.match(cur.s, cur.i)
        if not match:
            return None
        cur.i = match.end()
        count = _read_subscript(cur)
        if count is None:
            return None
        raw = _read_superscript(cur)
        if raw is None:
            return None
        atoms[match.group(0)] += count
        if raw:
            q = _read_charge(raw)
            if q is None:
                return None
            charge += q
    return atoms, charge


def parse_formula(formula: str) -> tuple[Counter, int] | None:
    """`Ca(OH)_2` → ({Ca: 1, O: 2, H: 2}, 0). Không đọc được thì `None`.

    Trả cả điện tích để kiểm được phương trình ion. Không đọc được nghĩa là còn
    ký tự nào đó module này không hiểu — khi ấy phải im lặng, vì đoán một nguyên
    tố sai là đủ để kết tội oan một phản ứng đúng.
    """
    text = _strip_latex(formula)
    if not text:
        return None
    # KHÔNG được xoá khoảng trắng còn sót rồi nối hai mẩu lại. `\cdot` trong
    # muối ngậm nước bị `_strip_latex` gỡ đi, nên `CuSO_4 \cdot 5H_2O` còn lại
    # `CuSO_4 5H_2O`; nối liền thành `CuSO_45H_2O` thì chỉ số đọc ra **45** và
    # công thức sai lệch cả chục lần mà không lỗi nào ném ra.
    if " " in text.strip():
        return None
    text = text.strip()
    cur = _Cursor(text)
    result = _read_group(cur)
    if result is None or not cur.eof():
        return None
    atoms, charge = result
    return (atoms, charge) if atoms else None


def molar_mass(formula: str, *, table: dict[str, float] | None = None) -> float | None:
    """Khối lượng mol (g/mol) của một công thức phân tử."""
    parsed = parse_formula(formula)
    if parsed is None:
        return None
    masses = ATOMIC_MASS if table is None else table
    total = 0.0
    for element, count in parsed[0].items():
        mass = masses.get(element)
        if mass is None:
            return None
        total += mass * count
    return total


# --------------------------------------------------------------------------- #
# Đọc một vế của phương trình
# --------------------------------------------------------------------------- #

#: Electron viết đủ kiểu: `e^-`, `e^{-}`, `2e`, `e`. Đứng riêng thành một số
#: hạng nên bắt ở mức số hạng chứ không ở mức công thức.
_ELECTRON_RE = re.compile(r"^\s*e\s*(?:\^\s*\{?\s*-?\s*\}?)?\s*$")

#: Hệ số đứng trước công thức: `2`, `1/2`, `2\,`. Hệ số chữ (`n\,CH_2=CH_2`,
#: `x\mathrm{Fe}`) là ẩn chưa biết — không kiểm được, phải trả unknown.
_COEF_RE = re.compile(r"^\s*(\d+(?:\.\d+)?(?:/\d+)?)\s*(?:\\times|\\cdot|\*)?\s*")


def _split_terms(side: str) -> list[tuple[int, str]] | None:
    """Tách một vế thành các số hạng có dấu. `Fe - 2e^{-}` → [(+1,'Fe'), (-1,'2e^{-}')].

    Dấu `-` ở đây là phép trừ số hạng (lối viết bán phản ứng của kho Việt Nam:
    `Fe - 2e = Fe^{2+}`). Gạch nối liên kết trong công thức cấu tạo đã bị
    `_strip_latex` gỡ trước đó, nên tới đây `-` chỉ còn một nghĩa.
    """
    terms: list[tuple[int, str]] = []
    sign = 1
    buf: list[str] = []
    depth = 0
    for ch in side:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if depth == 0 and ch in "+-" and buf and "".join(buf).strip():
            # `Fe^{2+}` — dấu nằm trong mũ, không phải dấu tách số hạng.
            tail = "".join(buf).rstrip()
            if tail.endswith("^") or tail.endswith("{"):
                buf.append(ch)
                continue
            terms.append((sign, "".join(buf).strip()))
            sign = 1 if ch == "+" else -1
            buf = []
            continue
        if depth == 0 and ch in "+-" and not "".join(buf).strip():
            sign = sign * (1 if ch == "+" else -1)
            buf = []
            continue
        buf.append(ch)
    if depth != 0:
        return None
    if "".join(buf).strip():
        terms.append((sign, "".join(buf).strip()))
    return terms or None


def parse_side(side: str) -> tuple[Counter, Fraction] | None:
    """Đọc một vế thành (số nguyên tử có hệ số, tổng điện tích).

    Số nguyên tử là `Counter` giá trị `Fraction` để chịu được hệ số phân số
    (`\\tfrac{1}{2}\\mathrm{O_2}`, rất phổ biến trong bán phản ứng).
    """
    text = _strip_latex(side)
    if not text.strip():
        return None
    terms = _split_terms(text)
    if terms is None:
        return None

    atoms: Counter = Counter()
    charge = Fraction(0)
    for sign, raw in terms:
        match = _COEF_RE.match(raw)
        coefficient = Fraction(1)
        body = raw
        if match:
            token = match.group(1)
            coefficient = (
                Fraction(*(int(x) for x in token.split("/")))
                if "/" in token
                else Fraction(token)
            )
            body = raw[match.end() :]
        body = body.strip()
        if not body:
            return None
        if _ELECTRON_RE.match(body):
            # Electron không phải nguyên tử: chỉ mang điện tích.
            charge += sign * coefficient * -1
            continue
        parsed = parse_formula(body)
        if parsed is None:
            return None
        formula_atoms, formula_charge = parsed
        for element, count in formula_atoms.items():
            atoms[element] += sign * coefficient * count
        charge += sign * coefficient * formula_charge
    return (atoms, charge) if atoms else None


# --------------------------------------------------------------------------- #
# Kiểm cân bằng
# --------------------------------------------------------------------------- #

#: Chữ tiếng Việt / tiếng Anh lẫn trong bước ("không phản ứng", "chậm", tên
#: chất viết bằng chữ thường như `malate`, `alkene`, `nylon`). Công thức hoá học
#: chỉ gồm ký hiệu nguyên tố, chữ số và ngoặc — thấy chữ lạ là dừng.
_PROSE_RE = re.compile(r"[^\x00-\x7f]")

#: Bằng chứng tối thiểu để tin đây là hoá học thật.
#:
#: Chỉ đòi "đọc trọn vẹn thành nguyên tố" là chưa đủ, và kho có sẵn phản ví dụ:
#: `UUU \rightarrow UUC` là **đột biến codon** của môn Sinh, nhưng U là urani và
#: C là cacbon nên nó đọc trót lọt thành hai chất rồi bị báo "không cân bằng
#: nguyên tử" — đúng kiểu báo oan tệ nhất mà module này có thể gây ra.
#:
#: Quan sát để bịt: một công thức hoá học thật, trong kho này, luôn để lộ ít
#: nhất một trong bốn dấu vết dưới đây. Chuỗi codon và ẩn số toán học thì không
#: có dấu vết nào cả.
_TWO_LETTER_RE = re.compile(
    r"(?<![A-Za-z])(?:" + "|".join(e for e in ATOMIC_MASS if len(e) == 2) + r")(?![a-z])"
)
_SUBSCRIPT_RE = re.compile(r"_\s*\{?\s*\d|(?<=[A-Za-z])\d")   # H_2, H_{2}, H2SO4
_CHARGE_MARK_RE = re.compile(r"\^\s*\{?\s*\d*\s*[+-]")        # Fe^{2+}, OH^-
_ELECTRON_MARK_RE = re.compile(r"(?<![A-Za-z])\d*\s*e\s*\^?\s*\{?\s*-")


def _looks_chemical(text: str) -> bool:
    stripped = _strip_latex(text)
    return bool(
        _TWO_LETTER_RE.search(stripped)
        or _SUBSCRIPT_RE.search(stripped)
        or _CHARGE_MARK_RE.search(stripped)
        or _ELECTRON_MARK_RE.search(stripped)
    )


def check_equation(latex: str) -> tuple[ChemVerdict, str]:
    """Phương trình hoá học này có cân bằng nguyên tử không?

    Trả `unknown` ở mọi chỗ còn nghi ngờ. Danh sách các cửa phải qua, theo thứ
    tự, mỗi cửa là một kiểu báo oan đã thấy thật trong kho:

    1. đúng **một** mũi tên — `NO_3^- → NO_2^- → NO → N_2` là chuỗi chuyển hoá
       trong chu trình nitơ, không phải một phương trình để cân;
    2. không có ký pháp toán (`\\lim`, `\\frac`, `=`, `\\approx`…);
    3. nhãn trên mũi tên không mang dấu `±` (phổ khối: `\\xrightarrow{-CH_3}`);
    4. không có chữ ngoài bảng ASCII (chú thích tiếng Việt);
    5. có dấu vết hoá học thật — chỉ số, điện tích, electron, hoặc ký hiệu
       nguyên tố hai chữ (xem `_looks_chemical`);
    6. **cả hai vế đọc trọn vẹn** thành công thức hoá học, không sót ký tự nào.
    """
    text = (latex or "").strip()
    if not text:
        return "unknown", ""

    arrows = _ARROW_RE.findall(text)
    if len(arrows) != 1:
        return "unknown", ""
    if _ARROW_LABEL_RE.search(text):
        return "unknown", "nhãn trên mũi tên mang dấu ± — là mảnh mất/thêm, không kiểm cân bằng"

    left_raw, right_raw = _ARROW_RE.split(text, maxsplit=1)
    if _NOT_CHEMISTRY_RE.search(left_raw) or _NOT_CHEMISTRY_RE.search(right_raw):
        return "unknown", ""
    if _PROSE_RE.search(left_raw) or _PROSE_RE.search(right_raw):
        return "unknown", ""

    if not _looks_chemical(text):
        return "unknown", ""
    left = parse_side(left_raw)
    right = parse_side(right_raw)
    if left is None or right is None:
        return "unknown", ""

    left_atoms, left_charge = left
    right_atoms, right_charge = right
    off = [
        element
        for element in set(left_atoms) | set(right_atoms)
        if left_atoms.get(element, 0) != right_atoms.get(element, 0)
    ]
    if off:
        # Công thức cấu tạo hữu cơ (`CH_3\text{-}C\equiv CH`) là ngoại lệ, và là
        # ngoại lệ bắt buộc: sách giáo khoa viết phản ứng hữu cơ theo lối **bộ
        # khung**, lược cả sản phẩm phụ và cả chất xúc tác —
        # `CH_3\text{-}C\equiv CH + AgNO_3 \rightarrow CH_3\text{-}C\equiv CAg`
        # bỏ mất HNO_3 ở vế phải. Đếm nguyên tử ở đó luôn lệch, mà lời giải thì
        # hoàn toàn đúng. Đo trên kho: 4/4 bước có nối ba đều bị kết tội oan.
        # Vẫn xác nhận được nếu tình cờ cân — chỉ chặn đường kết tội.
        if _BOND_RE.search(text):
            return "unknown", (
                "công thức cấu tạo hữu cơ viết theo lối bộ khung — sản phẩm phụ"
                " thường được lược, không đếm nguyên tử để kết luận được"
            )
        detail = "; ".join(
            f"{e}: trái {_fmt(left_atoms.get(e, 0))} ≠ phải {_fmt(right_atoms.get(e, 0))}"
            for e in sorted(off)
        )
        return "unbalanced", f"phương trình không cân bằng nguyên tử — {detail}"

    if left_charge != right_charge:
        # Điện tích lệch trong khi nguyên tử khớp thì gần như luôn là do lối
        # viết chứ không phải lỗi: kho ghi số oxi hoá ở mũ (`Mn^{+7}`) hệt như
        # ghi điện tích ion, và bán phản ứng hay lược electron. Không đủ căn cứ
        # kết tội, mà cũng không được nhận là đã kiểm xong.
        return "unknown", (
            f"nguyên tử cân nhưng điện tích lệch ({_fmt(left_charge)} ≠ {_fmt(right_charge)})"
            " — có thể là số oxi hoá, chưa kiểm được"
        )

    formula = ", ".join(f"{e}: {_fmt(n)}" for e, n in sorted(left_atoms.items()))
    return "balanced", f"phương trình cân bằng nguyên tử và điện tích ({formula})"


def _fmt(value: object) -> str:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value.numerator}/{value.denominator}"
    return str(value)


# --------------------------------------------------------------------------- #
# Kiểm khối lượng mol
# --------------------------------------------------------------------------- #

#: `M_{\mathrm{H_2SO_4}} = 98`, `M_{Ag_2C_2} = 240`. Ba đòi hỏi, mỗi cái bịt một
#: kiểu đọc nhầm:
#:
#: * **tên chất phải nằm ở chỉ số dưới** — `M = 98` trần thì không biết chất nào;
#: * **vế phải phải là một con số trần** (kèm đơn vị là cùng), không phải một
#:   phép tính. `M_{AlCl_3} = 26,98 + 3 \times 35,45 = 133,33` là chuỗi cộng, và
#:   nếu vơ lấy con số gần nhất thì hoá ra đem 35,45 so với 133,33 rồi kết tội
#:   một bước hoàn toàn đúng. Chuỗi tính như thế đã có lớp CAS thường lo;
#: * **phải chạm biên** sau con số, để `M_{X} = 98x` không bị đọc thành 98.
_MOLAR_CLAIM_RE = re.compile(
    r"(?<![A-Za-z])M\s*_\s*\{((?:[^{}]|\{[^{}]*\})*)\}\s*=\s*"
    r"(\d+(?:\.\d+)?)"
    r"\s*(?:\\,|\\ |\s)*(?:\\(?:mathrm|text|rm)\s*\{[^{}]*\})?"
    r"\s*(?=$|[,;:]|\\quad|\\qquad|\\Rightarrow|\\implies|\\,|\\ )"
)

#: Dấu thập phân LaTeX kiểu Việt Nam. Phải quy đổi **trước** khi dò mệnh đề,
#: nếu không `58{,}5` không khớp nổi dạng "con số trần" ở trên.
_VN_DECIMAL_RE = re.compile(r"(\d)\s*\{\s*,\s*\}\s*(\d)")

#: Sai số cho phép khi đối chiếu khối lượng mol. Đủ rộng để chứa mọi cách làm
#: tròn nguyên tử khối mà sách giáo khoa dùng (M của phân tử lớn cộng dồn sai số
#: của hàng chục nguyên tử), vẫn đủ chặt để bắt lỗi thật — lỗi khối lượng mol
#: điển hình là quên một nguyên tử hoặc nhân nhầm hệ số, lệch hàng chục phần trăm.
_MOLAR_TOLERANCE = 0.02


def check_molar_mass(latex: str) -> tuple[ChemVerdict, str]:
    """`M_{\\mathrm{H_2SO_4}} = 98` có đúng không?

    Chỉ kết tội khi giá trị công bố lệch quá 2% so với **cả hai** bảng nguyên tử
    khối (IUPAC và bảng làm tròn của sách giáo khoa). Lời giải trong kho được
    viết theo bảng làm tròn, nên đối chiếu một bảng thôi là báo oan hàng loạt.
    """
    match = _MOLAR_CLAIM_RE.search(_VN_DECIMAL_RE.sub(r"\1.\2", latex or ""))
    if not match:
        return "unknown", ""
    name = match.group(1)
    if _PROSE_RE.search(name):
        return "unknown", ""
    # `M_{...}` là ký hiệu dùng chung khắp nơi: mômen lực trong Lí, trung bình
    # trong Thống kê, tên điểm trong Hình học. Chỉ số dưới của chúng thường vẫn
    # đọc trót lọt thành "công thức" một nguyên tố (`M_C`, `M_N`), và tra bảng
    # nguyên tử khối ở đó là kết tội một bước chẳng liên quan gì tới hoá học.
    # Đòi tên chất phải TỰ NÓ mang dấu hiệu hoá học.
    if not _looks_chemical(name):
        return "unknown", ""
    try:
        claimed = float(match.group(2))
    except ValueError:
        return "unknown", ""
    if claimed <= 0:
        return "unknown", ""

    candidates = [
        m for m in (molar_mass(name), molar_mass(name, table=TEXTBOOK_MASS)) if m
    ]
    if not candidates:
        return "unknown", ""
    if any(abs(claimed - m) / m <= _MOLAR_TOLERANCE for m in candidates):
        return "balanced", f"khối lượng mol của {_strip_latex(name)} đúng ({claimed:g} g/mol)"
    return "unbalanced", (
        f"khối lượng mol của {_strip_latex(name)} công bố {claimed:g}"
        f" nhưng tính lại được {candidates[0]:.4g} g/mol"
    )
