"""Kiểm thứ nguyên — ba trạng thái, mặc định là "chưa kiểm được".

Vì sao có module riêng thay vì dùng thẳng `check_unit`: hai chỗ gọi có **ngữ
cảnh đạo đức khác hẳn nhau**.

* `check_unit` chấm bài **học sinh**. Ở đó "đáp án thiếu đơn vị" là một nhận xét
  chính đáng — người học quên ghi đơn vị thật, và nói ra là đúng việc.
* Module này kiểm lời giải **của kho / của mô hình**. Ở đó hai đầu vào đều do
  chính hệ thống công bố, nên "chuỗi đáp án không kèm đơn vị" chỉ là lối viết,
  không phải bằng chứng sai thứ nguyên. Kết tội ở đây là báo oan.

Gộp hai ngữ cảnh vào một hàm hai trạng thái chính là nguồn gốc của 231/524 lần
báo "sai đơn vị" mà `aistem verify` đang in ra — đo trên toàn kho, xem NOTES.md.

Nguyên tắc: chỉ nói "không đồng nhất" khi **cả hai** vế đọc được trọn vẹn và
thứ nguyên thực sự khác nhau. Mọi trường hợp còn lại trả "unknown". Pint không
biết `cM`, `bp`, `nat`, `đvC`; coi "không hiểu" là "sai" đúng là cái bẫy đã một
lần làm bộ chấm nói sai với người trả lời đúng.
"""

from __future__ import annotations

import re
from typing import Literal

from .units import extract_unit, is_dimensionless, parse_unit

DimensionStatus = Literal["consistent", "inconsistent", "unknown"]

#: Đáp án là khoá trắc nghiệm. Pint đọc `A` thành ampe, `B` thành bel, `C` thành
#: coulomb — cùng một cái bẫy chữ-cái-bị-chiếm-chỗ mà `F = ma` đã dính ở tầng
#: SymPy. Đây là nhóm báo oan lớn nhất đo được, phải chặn trước mọi thứ khác.
_CHOICE_KEY_RE = re.compile(r"^\s*[A-E]\s*$")

#: Nhiều đại lượng trên một chuỗi: `E_K ≈ -89,0 mV; E_Na ≈ +60,6 mV`. Kho khai
#: đúng một `answer_unit` cho cả cụm, nên không biết nó nói về đại lượng nào.
#: Đoán là kết tội bừa; ở đây chỉ cần nhận ra là không đủ dữ kiện.
_MULTI_QUANTITY_RE = re.compile(r";|\bvà\b|\|")

#: Ký pháp khoa học kho hay viết mà bộ tách đơn vị chung chưa nuốt: `1,81 x 10^-3`
#: và mũ Unicode `2,68 × 10³`. Không gỡ thì phần "x 10^-3" dính vào chuỗi đơn vị,
#: Pint chịu thua, và ta mất một phép kiểm đáng lẽ làm được. Chỉ nới theo chiều
#: **kiểm được thêm**, không theo chiều kết tội thêm.
_SCI_TAIL_RE = re.compile(r"^\s*[xX×·]\s*10\s*[\^]?\s*\{?-?[\d⁰-⁹]+\}?\s*")

#: Mũ viết bằng ký tự Unicode: `μmol·phút⁻¹`. Pint không đọc được chúng.
_SUPERSCRIPT_DIGITS = "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻"
_SUPERSCRIPT_RE = re.compile(f"[{_SUPERSCRIPT_DIGITS}]+")
_SUPERSCRIPT_MAP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻", "0123456789+-")

#: Kho viết đơn vị bằng tiếng Việt (`5,4 L/phút`, `≈ 9,93 năm`). Pint chỉ biết
#: tên tiếng Anh, nên không dịch thì 77 bài mất phép kiểm hoàn toàn.
#:
#: Bảng này cố ý đặt ở đây chứ KHÔNG thêm vào `_ALIASES` của `units.py`: bảng
#: bên ấy nằm trên đường chấm bài học sinh, đụng vào là đổi kết quả chấm của
#: hàng trăm bài. Ở đây phạm vi hẹp và hậu quả xấu nhất chỉ là một dòng hiển thị.
#:
#: KHÔNG có `độ` (vừa là góc vừa là nhiệt độ) và KHÔNG có danh từ đếm được
#: (`lần`, `cá thể`, `phân tử`, `nucleotide`, `ATP`): ép Pint hiểu chúng là mở
#: đường cho đúng loại báo oan mà module này sinh ra để chặn.
_VIETNAMESE_UNITS = {
    "giây": "second",
    "phút": "minute",
    "giờ": "hour",
    "ngày": "day",
    "tuần": "week",
    "năm": "year",
    "lít": "liter",
    "gam": "gram",
    "mét": "meter",
}
_VI_RE = re.compile(
    r"(?<![A-Za-zÀ-ỹ])(" + "|".join(sorted(_VIETNAMESE_UNITS, key=len, reverse=True)) + r")"
    r"(?![A-Za-zÀ-ỹ])"
)


def _normalize(text: str) -> str:
    """Đưa cách viết đơn vị của kho về thứ Pint đọc được."""
    s = _SUPERSCRIPT_RE.sub(lambda m: "^" + m.group(0).translate(_SUPERSCRIPT_MAP), text)
    return _VI_RE.sub(lambda m: _VIETNAMESE_UNITS[m.group(1)], s)


def _unit_of(text: str):
    """Chuỗi đơn vị -> đối tượng Pint, có qua bước chuẩn hoá tiếng Việt."""
    return parse_unit(_normalize(text))


def _answer_unit_text(answer: str) -> str:
    """Đơn vị đọc từ đáp án — chỉ trả về khi MỌI mẩu của đáp án cùng nói một thứ nguyên.

    Một chuỗi đáp án có thể mang nhiều dấu `=`/`≈`, và hai hình dạng ấy đòi hai
    cách xử lí ngược nhau:

    * **chuỗi quy đổi** — `Wq = 0,4 giờ = 24 phút`. Các mẩu cùng thứ nguyên,
      đọc mẩu nào cũng được. Cắt theo dấu `=` đầu tiên thì còn `giờ = 24 phút`,
      Pint nhân hai đơn vị ra thời gian **bậc hai** rồi báo sai một đáp án đúng.
    * **nhiều đại lượng** — `Gamma ≈ 1,91e12 s^-1, tương ứng tau ≈ 5,24e-13 s`.
      Các mẩu khác thứ nguyên, và kho chỉ khai đúng một `answer_unit`, nên không
      thể biết nó nói về đại lượng nào. Chọn bừa mẩu cuối là kết tội bừa.

    Phân biệt hai hình dạng bằng chính dữ liệu thay vì đoán theo dấu câu: đọc
    đơn vị của **tất cả** các mẩu, và chỉ kết luận khi chúng đồng thuận.
    """
    text = (answer or "").strip()
    segments = re.split(r"[=≈]", text)
    if len(segments) > 1:
        segments = segments[1:]  # mẩu đầu là nhãn (`Wq`, `Gamma`), không phải giá trị

    units: list[str] = []
    for segment in segments:
        unit = extract_unit(segment.strip())
        unit = _SCI_TAIL_RE.sub("", unit).strip(" .,;")
        # Còn sót dấu so sánh nghĩa là cắt chưa sạch — thà không kiểm còn hơn đoán.
        if not unit or re.search(r"[=≈<>]", unit):
            return ""
        units.append(unit)

    if not units:
        return ""
    dimensions = {(_unit_of(u).dimensionality if _unit_of(u) is not None else None) for u in units}
    if None in dimensions or len(dimensions) > 1:
        return ""
    return units[-1]


def check_dimension(answer: str, expected_unit: str | None) -> tuple[DimensionStatus, str]:
    """Đáp án có cùng thứ nguyên với đơn vị kho khai không?

    Trả `unknown` bất cứ khi nào thiếu dữ kiện — đó là mặc định, không phải
    trường hợp ngoại lệ. `inconsistent` chỉ dành cho lúc đã đọc trọn vẹn cả hai
    vế và chúng khác thứ nguyên thật.
    """
    unit = (expected_unit or "").strip()
    if not unit:
        return "unknown", "kho không khai đơn vị cho đáp án"

    # Ba hàng rào về hình dạng ĐÁP ÁN phải chạy trước mọi phép đọc đơn vị: nếu
    # chuỗi vốn không phải một đại lượng đơn thì mọi thứ rút ra từ nó đều vô
    # nghĩa, kể cả khi Pint tình cờ đọc trôi.
    text = (answer or "").strip()
    if not text:
        return "unknown", "đáp án rỗng"
    if _CHOICE_KEY_RE.match(text):
        return "unknown", "đáp án là khoá trắc nghiệm, không phải một đại lượng có đơn vị"
    if _MULTI_QUANTITY_RE.search(text):
        return "unknown", "đáp án gồm nhiều đại lượng, không biết đơn vị kho khai cho đại lượng nào"

    # Tỉ lệ, đơn vị đếm, đơn vị chuyên ngành (`%`, `bp`, `cM`, `nat`, `lần`).
    # Xác nhận thì vẫn rộng tay — số thuần hoặc một đơn vị cũng không thứ nguyên
    # là khớp. Nhưng KHÔNG BAO GIỜ kết tội ở nhánh này: kho hay khai `%` cho một
    # đáp án nhiều phần mà phần cuối lại có đơn vị thật, và đó là cách ghi nhãn
    # của kho chứ không phải lỗi thứ nguyên.
    if is_dimensionless(unit):
        got_text = _answer_unit_text(text)
        if not got_text:
            # `_answer_unit_text` trả rỗng vì BỐN lí do khác hẳn nhau, và chỉ
            # một trong bốn là "đáp án đúng là số thuần". Ba lí do còn lại —
            # các mẩu không đồng thuận thứ nguyên, cắt chưa sạch, `extract_unit`
            # chịu thua — đều là "chưa đọc được", và đóng dấu `consistent` ở đó
            # là xác nhận một thứ chưa hề kiểm. Hỏi thẳng `extract_unit` xem đáp
            # án có ghi đơn vị nào không, rồi mới dám nói "số thuần".
            if extract_unit(text).strip():
                return "unknown", "không đọc chắc được đơn vị trong đáp án, chưa kiểm được"
            return "consistent", f"đáp án là số thuần, khớp với đại lượng không thứ nguyên {unit}"
        got = _unit_of(got_text)
        # Dùng `.dimensionless` chứ không phải `str(.dimensionality)`: với đại
        # lượng không thứ nguyên Pint trả về chuỗi "dimensionless" — chuỗi ấy
        # KHÁC RỖNG, nên kiểm bằng độ dài chuỗi sẽ luôn cho kết quả ngược.
        if got is not None and got.dimensionless:
            return "consistent", f"đơn vị {got_text} không mang thứ nguyên, khớp với {unit}"
        return "unknown", f"đơn vị {unit!r} không mang thứ nguyên, không có gì để đối chiếu"

    expected = _unit_of(unit)
    if expected is None:
        return "unknown", f"Pint không hiểu đơn vị {unit!r} của kho, chưa kiểm được thứ nguyên"

    got_text = _answer_unit_text(text)
    if not got_text:
        return "unknown", "chuỗi đáp án không kèm đơn vị — là lối viết, không phải lỗi thứ nguyên"

    got = _unit_of(got_text)
    if got is None:
        return "unknown", f"Pint không hiểu đơn vị {got_text!r} trong đáp án, chưa kiểm được"

    if got.dimensionality == expected.dimensionality:
        same = str(got) == str(expected)
        return "consistent", (
            f"đơn vị {got_text} đúng thứ nguyên"
            + ("" if same else f" (khác bội số với {unit}, vẫn hợp lệ)")
        )

    # Tới đây cả hai vế đều đọc được trọn vẹn và thứ nguyên khác nhau thật.
    return "inconsistent", (
        f"sai thứ nguyên: đáp án ghi {got_text} có [{got.dimensionality}], "
        f"kho khai {unit} tức [{expected.dimensionality}]"
    )
