"""Tách một đáp án nhiều đại lượng thành từng đại lượng riêng.

Kho có hàng trăm bài mà đáp án gồm nhiều con số cùng lúc:

    "Vmax = 50 μmol·phút⁻¹; Km = 4,0 mM"
    "198 phút (3,3 giờ); chỉ số phân bào = 15 %"
    "d(A-B) = 12,8 cM; d(B-D) = 8,0 cM; hệ số trùng hợp = 0,781"

Ép cả chuỗi về một con số rồi so là chắc chắn chấm sai. Nhưng bỏ qua hẳn thì
mất luôn 104 bài điền số — và mất cả khả năng cho **điểm từng phần**, vốn là
thứ người học cần nhất ở dạng bài này: biết mình đúng phần nào, hỏng phần nào.

Module này chỉ làm một việc: cắt chuỗi thành các mẩu `nhãn = giá trị đơn vị`.
Việc so sánh để ở tầng chấm bài.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .cas.units import extract_unit
from .textnorm import extract_number, fold

#: Dấu ngăn giữa các đại lượng. Dấu chấm phẩy là tin cậy nhất; dấu phẩy thì
#: không dùng được vì nó còn là dấu thập phân tiếng Việt.
_SEPARATOR_RE = re.compile(r"\s*;\s*|\s*\|\s*|\s+và\s+(?=[^,]{0,30}[=≈])")

#: Nhãn của một mục trong đáp án nhiều phần: "a)", "(b)", "1.".
_ITEM_LABEL_RE = re.compile(r"^\s*[(\[]?\s*([a-hà-ỹ1-9])\s*[)\].]\s*")

#: `Vmax = 50 μmol·phút⁻¹` -> nhãn "Vmax", phần còn lại là giá trị.
#: Nhãn lấy tới dấu `=` **đầu tiên**, giá trị lấy từ dấu `=` **cuối cùng**:
#: `quang hợp gộp = 4,0 + 2,0 = 6,0` có nhãn ở đầu và kết quả ở cuối.
_LABEL_RE = re.compile(r"^\s*(.{1,40}?)\s*[=≈]", re.S)
_VALUE_RE = re.compile(r"^.*[=≈]\s*(.+)$", re.S)

#: Sau khi bỏ nhãn, một đại lượng thật chỉ còn con số và đơn vị. Còn lại nhiều
#: chữ nghĩa là đoạn ấy là câu văn có kèm số — cần người chấm, không phải máy.
_MAX_VALUE_LENGTH = 28

#: Dấu hiệu phần giá trị không phải một đại lượng đơn: còn phép so sánh, còn
#: một dấu bằng nữa, hoặc còn liên từ nối hai mệnh đề.
_MESSY_VALUE_RE = re.compile(
    r"[<>≤≥]|[=≈].*[=≈]|\b(?:với|tại|tức|ứng với|nên|do|vì|khi)\b", re.IGNORECASE
)


@dataclass
class Quantity:
    """Một đại lượng đọc được từ đáp án."""

    label: str
    value: float | None
    unit: str
    raw: str
    body: str = ""

    @property
    def key(self) -> str:
        """Khoá so khớp nhãn, không phân biệt dấu và hoa thường."""
        return fold(self.label)

    @property
    def numeric(self) -> bool:
        return self.value is not None

    @property
    def looks_like_a_quantity(self) -> bool:
        """Phần giá trị có gọn như một đại lượng không, hay là cả một câu?

        `Km = 4,0 mM` thì có. `t ≈ 2,851 với df = 22 > 2,074` thì không: nó có
        số, nhưng là hai mệnh đề nối nhau kèm một phép so sánh. Chấm máy những
        mẩu như thế sẽ ra kết quả vô nghĩa, mà "vô nghĩa" thì hiện ra thành
        "sai" trước mặt người học.
        """
        body = self.body or self.raw
        if not self.numeric or len(body) > _MAX_VALUE_LENGTH:
            return False
        return not _MESSY_VALUE_RE.search(body)


def _split(text: str) -> list[str]:
    parts = [p.strip() for p in _SEPARATOR_RE.split(text or "")]
    return [p for p in parts if p]


def parse_quantities(text: str) -> list[Quantity]:
    """Tách đáp án thành danh sách đại lượng, theo thứ tự xuất hiện."""
    out: list[Quantity] = []
    for index, piece in enumerate(_split(text)):
        item = _ITEM_LABEL_RE.sub("", piece).strip()
        label_match, value_match = _LABEL_RE.match(item), _VALUE_RE.match(item)
        if label_match and value_match:
            label, body = label_match.group(1).strip(), value_match.group(1).strip()
        else:
            label, body = "", item

        # Bỏ phần chú thích trong ngoặc ở cuối: "198 phút (3,3 giờ)".
        body_main = re.sub(r"\s*\([^()]*\)\s*$", "", body).strip() or body

        out.append(
            Quantity(
                label=label or f"#{index + 1}",
                value=extract_number(body_main),
                unit=extract_unit(body_main),
                raw=piece,
                body=body_main,
            )
        )
    return out


def is_multi_numeric(text: str) -> bool:
    """Đáp án có phải gồm **nhiều đại lượng số**, và chỉ có thế, không?

    Dùng cho những chỗ cần chắc chắn cả chuỗi là số — `cas.verify` hỏi câu này
    để biết có được đem đáp án ra đối chiếu với một giá trị duy nhất không.
    """
    quantities = parse_quantities(text)
    return len(quantities) >= 2 and all(q.looks_like_a_quantity for q in quantities)


#: Trên ngưỡng này thì con số trong trường `tolerance` không thể là sai số
#: **tương đối**: không đề thi nào chấp nhận lệch quá 20%.
_MAX_SENSIBLE_RELATIVE = 0.2


def relative_tolerance(declared: float | None, expected: float | None, default: float) -> float:
    """Đọc trường `tolerance` của kho, phân biệt sai số tương đối với tuyệt đối.

    Kho ghi trường này theo **hai quy ước lẫn lộn nhau**, và cả hệ thống đang
    đọc mọi giá trị như sai số tương đối:

    * `0{,}01` — nghĩa là ±1%, đúng như hệ thống hiểu;
    * `50000` cho đáp án `k_cat/K_M = 7{,}5\\times10^{6}` — đây là ±50000 **tuyệt
      đối**, tức 0,67%. Đọc thành tương đối thì cửa sổ chấp nhận rộng năm triệu
      phần trăm, và bộ chấm nói "đúng" với gần như mọi con số.

    119 bài trong kho (9,5%) khai `tolerance ≥ 0{,}5`. Đó là lớp **xác nhận
    khống** lớn nhất còn lại của bộ chấm, và nó im lặng: người học trả lời sai
    gấp đôi vẫn được khen đúng.

    Phân biệt bằng chính con số: sai số tương đối lớn hơn 20% thì không còn là
    một quy ước chấm bài nào cả, nên giá trị ấy chắc chắn là tuyệt đối.
    """
    if declared is None:
        return default
    declared = abs(declared)
    if declared <= _MAX_SENSIBLE_RELATIVE:
        return declared
    if not expected:
        # Không có mốc để quy đổi. Lấy mặc định chứ không dùng con số đáng ngờ:
        # thà chặt tay còn hơn mở toang cửa sổ chấp nhận.
        return default
    converted = declared / abs(expected)
    # Quy đổi xong mà vẫn quá rộng thì con số ấy không phải dung sai của đại
    # lượng này — thường là dung sai kho khai cho một đại lượng khác trong cùng
    # đáp án nhiều phần (`50000` viết cho `7{,}5\\times10^{6}`, đem áp lên `300`
    # thành ±16 000%). Không có cách đọc nào làm nó hợp lí, nên bỏ hẳn.
    return converted if converted <= _MAX_SENSIBLE_RELATIVE else default


def countable_quantities(text: str) -> int:
    """Có bao nhiêu mẩu trong đáp án này chấm máy được?

    Tách khỏi `is_multi_numeric` vì hai câu hỏi khác nhau. Đòi **mọi** mẩu đều
    là đại lượng thì một câu diễn giải bám đuôi (`LOD ≈ 3,35 > 3 nên kết luận
    có liên kết`) làm hỏng cả đáp án, và hệ thống trả "không chấm được" cho
    12,3% số bài của kho — người học hỏi thì không nhận được gì. Chấm phần chấm
    được, rồi nói thẳng phần nào chưa chấm, vẫn hơn hẳn im lặng.
    """
    return sum(1 for q in parse_quantities(text) if q.looks_like_a_quantity)


def align(
    expected: list[Quantity], received: list[Quantity]
) -> list[tuple[Quantity, Quantity | None]]:
    """Ghép đại lượng của học sinh với đại lượng của đáp án.

    Ghép theo nhãn trước — người học có thể trả lời không đúng thứ tự đề hỏi,
    và phạt vì chuyện đó thì vô lí. Nhãn không khớp thì mới ghép theo vị trí.
    """
    remaining = list(received)
    pairs: list[tuple[Quantity, Quantity | None]] = []

    by_key: dict[str, Quantity] = {}
    for quantity in remaining:
        by_key.setdefault(quantity.key, quantity)

    for want in expected:
        match = by_key.get(want.key) if want.key and not want.key.startswith("#") else None
        if match is not None and match in remaining:
            remaining.remove(match)
            pairs.append((want, match))
        else:
            pairs.append((want, None))

    # Những đại lượng chưa ghép được thì lấp theo thứ tự còn lại.
    for index, (want, got) in enumerate(pairs):
        if got is None and remaining:
            pairs[index] = (want, remaining.pop(0))
    return pairs
