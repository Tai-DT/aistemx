"""Bước tiếp nhận đề bài.

Đề vào hệ thống theo ba đường: văn bản gõ tay, LaTeX, hoặc ảnh chụp trang sách
/ vở. Ảnh đi qua Claude vision để ra văn bản kèm LaTeX — không cần dịch vụ OCR
công thức riêng, và đọc được cả chữ viết tay.
"""

from __future__ import annotations

import base64
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .. import llm
from ..textnorm import clean_latex

READ_SCHEMA: dict[str, Any] = {
    "type": "object",
    "required": ["statement_vi", "has_problem"],
    "properties": {
        "has_problem": {
            "type": "boolean",
            "description": "Ảnh/văn bản có chứa một bài toán thật sự hay không",
        },
        "statement_vi": {
            "type": "string",
            "description": (
                "Đề bài chép lại đầy đủ bằng tiếng Việt. Công thức viết bằng LaTeX thuần, "
                "không bọc dấu $. Giữ nguyên mọi số liệu và đơn vị, không làm tròn, "
                "không thêm bớt dữ kiện."
            ),
        },
        "statement_latex": {
            "type": "string",
            "description": "Biểu thức chính của đề, nếu đề quy về một biểu thức duy nhất",
        },
        "choices": {
            "type": "array",
            "description": "Các phương án nếu đây là câu trắc nghiệm",
            "items": {
                "type": "object",
                "required": ["key", "text"],
                "properties": {
                    "key": {"type": "string"},
                    "text": {"type": "string"},
                },
            },
        },
        "given_values": {
            "type": "array",
            "description": "Các dữ kiện đã cho, dạng 'ký hiệu = giá trị đơn vị'",
            "items": {"type": "string"},
        },
        "asked_for": {"type": "string", "description": "Đề hỏi tìm cái gì"},
        "notes": {"type": "string", "description": "Chỗ mờ, thiếu dữ kiện, hoặc đọc không chắc"},
    },
}

READ_SYSTEM = """Bạn đọc đề bài Toán - Lí - Hoá - Sinh từ ảnh chụp hoặc văn bản thô,
chép lại thành văn bản máy đọc được. Tuyệt đối không giải bài, không gợi ý,
không sửa đề kể cả khi thấy đề có vẻ sai.
Công thức viết bằng LaTeX thuần, không bọc $ hay \\[ \\].
Số liệu giữ nguyên như trong đề, kể cả dấu phẩy thập phân kiểu Việt Nam.
Chỗ nào ảnh mờ không đọc chắc thì ghi vào trường notes chứ đừng đoán."""


@dataclass
class ReadResult:
    """Đề bài sau khi đã đưa về dạng chuẩn."""

    statement: str
    statement_latex: str | None = None
    choices: list[dict[str, str]] = field(default_factory=list)
    given: list[str] = field(default_factory=list)
    asked: str = ""
    notes: str = ""
    source: str = "text"


_LATEX_HINT_RE = re.compile(r"\\[a-zA-Z]{2,}|\^\{|_\{|\\frac|\\int|\\sum")


def encode_image(path: str | Path) -> tuple[str, str]:
    """Đọc file ảnh thành (base64, media_type) để gửi cho mô hình."""
    file_path = Path(path)
    data = file_path.read_bytes()
    suffix = file_path.suffix.lower()
    media_type = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }.get(suffix)
    if media_type is None:
        raise ValueError(
            f"Định dạng ảnh {suffix or '(không rõ)'} không được hỗ trợ. "
            "Dùng PNG, JPEG, GIF hoặc WebP."
        )
    if len(data) > 5 * 1024 * 1024:
        raise ValueError("Ảnh lớn hơn 5 MB — hãy giảm kích thước trước khi gửi.")
    return base64.standard_b64encode(data).decode("ascii"), media_type


def read(
    statement: str = "",
    *,
    image_base64: str | None = None,
    image_media_type: str = "image/png",
    model: str | None = None,
) -> ReadResult:
    """Đưa đề bài về dạng chuẩn.

    Không có ảnh và không cần bóc tách gì thêm thì trả thẳng văn bản — không
    gọi mô hình, không tốn tiền, không thêm độ trễ.
    """
    if not image_base64:
        text = (statement or "").strip()
        if not text:
            raise ValueError("Đề bài rỗng: cần truyền văn bản hoặc ảnh.")
        latex = clean_latex(text) if _LATEX_HINT_RE.search(text) else None
        return ReadResult(statement=text, statement_latex=latex, source="text")

    result = llm.structured(
        system=READ_SYSTEM,
        prompt=(
            "Chép lại đề bài trong ảnh."
            + (f"\n\nGợi ý kèm theo từ người dùng: {statement}" if statement else "")
        ),
        schema=READ_SCHEMA,
        tool_name="doc_de_bai",
        tool_description="Trả về đề bài đã chép lại.",
        model=model,
        max_tokens=3000,
        image_base64=image_base64,
        image_media_type=image_media_type,
    )
    data = result.data
    if not data.get("has_problem"):
        raise ValueError(
            "Không tìm thấy bài toán nào trong ảnh."
            + (f" Ghi chú của mô hình: {data.get('notes')}" if data.get("notes") else "")
        )
    return ReadResult(
        statement=data.get("statement_vi", "").strip(),
        statement_latex=data.get("statement_latex") or None,
        choices=data.get("choices") or [],
        given=data.get("given_values") or [],
        asked=data.get("asked_for", ""),
        notes=data.get("notes", ""),
        source="image",
    )
