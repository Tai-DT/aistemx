"""Chuẩn hoá và so khớp kỹ năng.

Trường `skills` của mỗi bài tập là văn bản tự do, và mỗi lát cắt trong kho được
soạn độc lập nên cùng một kỹ năng được viết theo nhiều kiểu:

    "phân tích đa thức thành nhân tử"      (kho quốc tế, viết bằng chữ)
    "phan-tich-da-thuc-thanh-nhan-tu"      (kho VN, viết dạng slug)
    "phân tích nhân tử"                    (viết tắt)

So khớp bằng chuỗi nguyên thì ba cái trên là ba kỹ năng khác nhau. Hậu quả đo
được trên kho hiện tại: **94% kỹ năng chỉ xuất hiện ở đúng một bài**, nên tính
năng "luyện thêm kỹ năng đang yếu" gần như không trả về gì.

Cách sửa dựa trên một quan sát đơn giản: sau khi bỏ dấu, slug và dạng chữ chỉ
khác nhau ở dấu gạch nối thay cho dấu cách. Tách thành token thì chúng **trùng
khít**. Từ đó:

* `canonical()` — khoá chuẩn để gộp thống kê, không phụ thuộc cách viết.
* `tokens()` — để so khớp một phần khi hai cách viết không trùng hẳn.
* trọng số IDF — "áp dụng công thức" xuất hiện ở khắp nơi nên gần như không
  mang thông tin, còn "nhiễu xạ" thì mang rất nhiều. Không cân theo độ hiếm thì
  mọi bài đều "liên quan" tới mọi kỹ năng.
"""

from __future__ import annotations

import math
import re
from collections.abc import Iterable, Sequence

from .textnorm import fold

_TOKEN_RE = re.compile(r"[a-z0-9]+")

#: Hư từ và từ đệm hay gặp trong tên kỹ năng. Bỏ đi thì "vận dụng công thức
#: Nernst" và "công thức Nernst" quy về cùng một chỗ.
_SKILL_STOPWORDS = frozenset(
    """
    va voi cua cho trong khi tu theo den ra vao len tren duoi mot cac
    su viec cach dang loai co the
    bai toan cau hoi van de
    """.split()
)

#: Động từ mở đầu tên kỹ năng. Chúng nói *mức độ tư duy* chứ không nói *nội
#: dung*, nên giữ lại chỉ khiến mọi kỹ năng trông giống nhau.
_SKILL_VERBS = frozenset(
    """
    ap dung van tinh toan xac dinh tim giai lap viet neu trinh bay
    nhan biet nhan dien hieu phan tich tong danh gia so sanh
    chung minh suy luan bien doi thuc hien su dung doc lap ve
    """.split()
)


def tokens(skill: str) -> list[str]:
    """Các token mang nội dung của một tên kỹ năng, đã bỏ dấu."""
    raw = _TOKEN_RE.findall(fold(skill))
    kept = [t for t in raw if len(t) > 1 and t not in _SKILL_STOPWORDS]
    content = [t for t in kept if t not in _SKILL_VERBS]
    # Kỹ năng chỉ gồm toàn động từ ("vận dụng cao", "áp dụng công thức") thì giữ
    # nguyên, vì bỏ hết sẽ thành rỗng và không so khớp được gì.
    return content or kept


def canonical(skill: str) -> str:
    """Khoá gộp: token nội dung, sắp xếp, nối bằng dấu cách.

    `"phân tích đa thức thành nhân tử"` và `"phan-tich-da-thuc-thanh-nhan-tu"`
    cho ra cùng một khoá.
    """
    return " ".join(sorted(set(tokens(skill))))


def display_name(variants: Iterable[str]) -> str:
    """Chọn cách viết dễ đọc nhất trong các biến thể của cùng một kỹ năng.

    Ưu tiên bản có dấu tiếng Việt và có khoảng trắng — tức dạng chữ, không phải
    dạng slug — vì đó là thứ sẽ hiện ra cho người học.
    """
    best = ""
    best_score = (-1, -1, 0)
    for variant in variants:
        has_diacritics = any(ord(ch) > 127 for ch in variant)
        has_spaces = " " in variant
        score = (int(has_diacritics), int(has_spaces), len(variant))
        if score > best_score:
            best, best_score = variant, score
    return best


class SkillMatcher:
    """Chấm điểm mức giống nhau giữa hai tên kỹ năng, có cân theo độ hiếm.

    `document_frequency` là số bài tập chứa mỗi token, dùng để tính IDF. Không
    có thì mọi token cân bằng nhau.
    """

    def __init__(self, document_frequency: dict[str, int] | None = None, total: int = 0) -> None:
        self.document_frequency = document_frequency or {}
        self.total = max(total, 1)

    def weight(self, token: str) -> float:
        frequency = self.document_frequency.get(token, 1)
        return math.log(1 + self.total / max(frequency, 1))

    def similarity(self, a: str, b: str) -> float:
        """Độ giống trong khoảng 0-1, theo tỉ lệ trọng số token dùng chung."""
        ta, tb = set(tokens(a)), set(tokens(b))
        if not ta or not tb:
            return 0.0
        shared = ta & tb
        if not shared:
            return 0.0
        shared_weight = sum(self.weight(t) for t in shared)
        union_weight = sum(self.weight(t) for t in ta | tb)
        return shared_weight / union_weight if union_weight else 0.0

    def matches(self, a: str, b: str, threshold: float = 0.34) -> bool:
        return self.similarity(a, b) >= threshold


def group(skills: Sequence[str]) -> dict[str, list[str]]:
    """Gộp danh sách tên kỹ năng theo khoá chuẩn."""
    grouped: dict[str, list[str]] = {}
    for skill in skills:
        grouped.setdefault(canonical(skill), []).append(skill)
    return grouped
