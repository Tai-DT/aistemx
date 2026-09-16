"""Kiểm đơn vị bằng Pint.

Kho AISTEM ghi đơn vị dạng ASCII SI (`m/s^2`, `J/(mol.K)`, `mol/L`) trong
trường `units` của công thức. Lớp này dịch sang Pint để trả lời hai câu hỏi:
đáp số học sinh có đúng thứ nguyên không, và các đại lượng trong một công thức
có nhất quán thứ nguyên không.
"""

from __future__ import annotations

import re
from functools import lru_cache

from ..textnorm import extract_number


@lru_cache(maxsize=1)
def _registry():
    import pint

    ureg = pint.UnitRegistry(autoconvert_offset_to_baseunit=True)
    ureg.default_format = "~P"
    return ureg


# Cách viết hay gặp trong kho, Pint không hiểu thẳng.
_ALIASES = {
    "đvC": "dalton",
    "u": "dalton",
    "amu": "dalton",
    "M": "mol/L",
    "N": "newton",
    "kmh": "km/hour",
    "km/h": "km/hour",
    "atm": "atmosphere",
    "cal": "calorie",
    "eV": "electron_volt",
    "°C": "degC",
    "°K": "kelvin",
    "độ C": "degC",
}


def normalize_unit(text: str) -> str:
    """Chuẩn hoá chuỗi đơn vị ASCII của kho về cú pháp Pint."""
    s = (text or "").strip()
    if not s:
        return ""
    if s in _ALIASES:
        return _ALIASES[s]
    s = s.replace("·", "*").replace("×", "*").replace("−", "-")
    # `J/(mol.K)` -> `J/(mol*K)`: dấu chấm giữa hai ký hiệu là phép nhân.
    s = re.sub(r"(?<=[A-Za-zΩ°\)])\.(?=[A-Za-zΩ°\(])", "*", s)
    s = s.replace("^", "**")
    for alias, replacement in _ALIASES.items():
        if len(alias) > 1:
            s = re.sub(rf"(?<![A-Za-z]){re.escape(alias)}(?![A-Za-z])", replacement, s)
    return s.strip()


def parse_unit(text: str):
    """Chuỗi đơn vị -> đối tượng Pint. Trả None nếu không hiểu được."""
    normalized = normalize_unit(text)
    if not normalized:
        return None
    try:
        return _registry().Unit(normalized)
    except Exception:
        try:
            return _registry().parse_expression(normalized).units
        except Exception:
            return None


def extract_unit(answer: str) -> str:
    """Tách phần đơn vị khỏi một đáp án kiểu `9,8 m/s^2`."""
    s = (answer or "").strip()
    if not s:
        return ""
    # Đáp án hay có nhãn ở đầu: `a = 361 pm`, `V = 300 mL`. Không cắt nhãn đi
    # thì cả chuỗi bị coi là đơn vị, Pint chịu thua, và bộ chấm báo sai đơn vị
    # cho một câu trả lời hoàn toàn đúng.
    labelled = re.match(r"^.{0,40}?[=≈]\s*(.+)$", s, re.S)
    if labelled:
        s = labelled.group(1).strip()
    s = re.sub(r"^[≈~]\s*", "", s)
    # Bỏ phần số (kể cả ký hiệu khoa học) ở đầu, phần còn lại coi là đơn vị.
    s = re.sub(
        r"^[-+]?(?:\d+(?:[.,]\d+)?|\.\d+)"
        r"(?:\s*(?:\\times|\\cdot|×|·|[eE.])\s*10\s*\^?\s*\{?-?\d+\}?)?\s*",
        "",
        s,
    )
    s = s.replace("$", "").replace("\\,", " ").replace("\\ ", " ")
    s = re.sub(r"^\\(?:mathrm|text|rm)\s*\{([^{}]*)\}", r"\1", s.strip())
    # Chú thích trong ngoặc ở cuối không phải đơn vị: `1800 g (1,8 kg)` có đơn
    # vị là `g`. Giữ lại thì Pint đọc cả cụm và báo sai thứ nguyên.
    s = re.sub(r"\s*\([^()]*\)\s*$", "", s).strip()
    return s.strip(" .,;")


def check_unit(answer: str, expected_unit: str) -> tuple[bool, str]:
    """Đáp án có đúng thứ nguyên mong đợi không?

    So theo **thứ nguyên**, không theo cách viết: `9,8 m/s^2` và `980 cm/s^2`
    đều hợp lệ với kỳ vọng `m/s^2`, còn `9,8 N` thì không.
    """
    expected = parse_unit(expected_unit)
    if expected is None:
        return True, f"không hiểu đơn vị kỳ vọng {expected_unit!r}, bỏ qua kiểm tra"

    got_text = extract_unit(answer)
    if not got_text:
        return False, f"đáp án thiếu đơn vị, cần {expected_unit}"

    got = parse_unit(got_text)
    if got is None:
        return False, f"không hiểu đơn vị {got_text!r} trong đáp án"

    if got.dimensionality == expected.dimensionality:
        same = str(got) == str(expected)
        return True, (
            f"đơn vị {got_text} đúng thứ nguyên"
            + ("" if same else f" (khác bội số với {expected_unit}, vẫn hợp lệ)")
        )
    return False, (
        f"sai thứ nguyên: đáp án có [{got.dimensionality}], "
        f"cần [{expected.dimensionality}] tức {expected_unit}"
    )


def convert(value: float, from_unit: str, to_unit: str) -> float | None:
    """Đổi đơn vị. Dùng khi học sinh trả lời đúng nhưng khác bội số."""
    src, dst = parse_unit(from_unit), parse_unit(to_unit)
    if src is None or dst is None:
        return None
    try:
        return float((value * src).to(dst).magnitude)
    except Exception:
        return None


#: Ký hiệu không phải đơn vị vật lí mà là cách viết tỉ lệ hoặc đơn vị đếm riêng
#: của từng ngành. Pint không biết chúng, và ép nó biết thì lợi bất cập hại —
#: chỉ cần nhận ra rằng ở đây không có gì để kiểm về thứ nguyên.
_DIMENSIONLESS = {"%", "‰", "phần trăm", "ppm", "ppb", "bp", "kb", "mb", "nt", "aa", "cm-morgan"}


def is_dimensionless(unit: str) -> bool:
    return normalize_unit(unit).strip().lower() in _DIMENSIONLESS or not unit.strip()


def compare_with_units(
    student: str, expected_value: float, expected_unit: str, tolerance: float = 0.01
) -> tuple[bool, str]:
    """So đáp án học sinh với giá trị chuẩn, tự quy đổi nếu khác bội số.

    Đây là chỗ tách bạch "sai vật lí" với "chỉ khác đơn vị": trả lời `980 cm/s^2`
    khi đáp án là `9,8 m/s^2` là **đúng**, không phải sai.

    Và khi Pint không hiểu đơn vị — `cM` (centiMorgan), `bp` (cặp base), `%` —
    thì **so số thôi chứ không kết luận sai**. Kho có hàng trăm đơn vị chuyên
    ngành như thế; coi "không hiểu" là "sai" thì bộ chấm nói sai với người học
    đúng, mà đó là lỗi tệ nhất một bộ chấm có thể mắc.
    """
    number = extract_number(student)
    if number is None:
        return False, "không tìm thấy giá trị số trong câu trả lời"

    from .verify import numbers_match

    def _compare(value: float, note: str = "") -> tuple[bool, str]:
        ok, error = numbers_match(expected_value, value, tolerance)
        if ok:
            return True, (f"khớp giá trị {expected_value:.10g} {expected_unit}".strip() + note)
        return False, (
            f"lệch {error:.3g} so với {expected_value:.10g} {expected_unit}".strip()
            if error is not None
            else "không khớp giá trị"
        )

    if is_dimensionless(expected_unit):
        return _compare(number)

    student_unit = extract_unit(student)
    if not student_unit:
        return _compare(number, " (đáp án thiếu đơn vị)")

    converted = convert(number, student_unit, expected_unit)
    if converted is not None:
        return _compare(converted)

    # Không quy đổi được: hoặc sai thứ nguyên thật, hoặc Pint không biết đơn vị.
    if parse_unit(student_unit) is None or parse_unit(expected_unit) is None:
        return _compare(number, f" (không kiểm được đơn vị {student_unit!r}, chỉ so giá trị)")
    ok_dim, detail = check_unit(student, expected_unit)
    if not ok_dim:
        return False, detail
    return _compare(number)
