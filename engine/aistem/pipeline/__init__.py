"""Pipeline xử lí bài toán: đọc đề → phân loại → truy xuất → giải → kiểm chứng."""

from .classify import classify, classify_by_retrieval, describe
from .ingest import ReadResult, encode_image, read
from .retrieve import as_prompt_context, formula_records, gather
from .solve import solve

__all__ = [
    "ReadResult",
    "as_prompt_context",
    "classify",
    "classify_by_retrieval",
    "describe",
    "encode_image",
    "formula_records",
    "gather",
    "read",
    "solve",
]
