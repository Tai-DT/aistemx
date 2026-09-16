"""Nhúng vector — hoàn toàn tuỳ chọn.

Không cấu hình `AISTEM_EMBED_PROVIDER` thì mọi hàm ở đây trả `None` và tìm kiếm
chạy thuần BM25. Với 6 931 bản ghi, cosine brute-force bằng numpy chỉ mất vài
mili-giây, nên không cần sqlite-vec hay vector DB riêng.
"""

from __future__ import annotations

import sqlite3
from collections.abc import Sequence
from dataclasses import dataclass
from functools import lru_cache

import httpx
import numpy as np

from .config import settings

_ENDPOINTS = {
    "voyage": ("https://api.voyageai.com/v1/embeddings", "Authorization", "Bearer {key}"),
    "openai": ("https://api.openai.com/v1/embeddings", "Authorization", "Bearer {key}"),
    "gemini": (
        "https://generativelanguage.googleapis.com/v1beta/models/{model}:embedContent",
        "x-goog-api-key",
        "{key}",
    ),
}


def enabled() -> bool:
    return settings.embed_provider != "none" and bool(settings.embed_api_key)


def embed_texts(texts: Sequence[str], *, input_type: str = "document") -> np.ndarray | None:
    """Nhúng một lô văn bản. Trả ma trận đã chuẩn hoá L2, hoặc None nếu tắt."""
    if not enabled() or not texts:
        return None
    provider = settings.embed_provider
    url, header, template = _ENDPOINTS[provider]
    headers = {
        header: template.format(key=settings.embed_api_key),
        "content-type": "application/json",
    }

    vectors: list[list[float]] = []
    with httpx.Client(timeout=120.0) as client:
        for start in range(0, len(texts), settings.embed_batch):
            batch = list(texts[start : start + settings.embed_batch])
            if provider == "gemini":
                for text in batch:
                    resp = client.post(
                        url.format(model=settings.embed_model),
                        headers=headers,
                        json={"content": {"parts": [{"text": text}]}},
                    )
                    resp.raise_for_status()
                    vectors.append(resp.json()["embedding"]["values"])
                continue
            body: dict = {"model": settings.embed_model, "input": batch}
            if provider == "voyage":
                body["input_type"] = "query" if input_type == "query" else "document"
            resp = client.post(url, headers=headers, json=body)
            resp.raise_for_status()
            data = sorted(resp.json()["data"], key=lambda d: d.get("index", 0))
            vectors.extend(d["embedding"] for d in data)

    matrix = np.asarray(vectors, dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    return matrix / np.clip(norms, 1e-9, None)


@lru_cache(maxsize=512)
def embed_query(text: str) -> np.ndarray | None:
    matrix = embed_texts([text], input_type="query")
    return None if matrix is None else matrix[0]


@dataclass
class EmbeddingMatrix:
    keys: list[str]
    vectors: np.ndarray  # (n, dim), đã chuẩn hoá L2


_CACHE: dict[int, EmbeddingMatrix | None] = {}


def load_matrix(conn: sqlite3.Connection) -> EmbeddingMatrix | None:
    """Nạp toàn bộ vector vào RAM một lần, giữ trong cache theo kết nối."""
    token = id(conn)
    if token in _CACHE:
        return _CACHE[token]
    try:
        rows = conn.execute("SELECT kind, rid, dim, vector FROM embeddings").fetchall()
    except sqlite3.Error:
        rows = []
    if not rows:
        _CACHE[token] = None
        return None
    dim = rows[0]["dim"]
    keys = [f"{r['kind']}:{r['rid']}" for r in rows]
    vectors = np.frombuffer(b"".join(r["vector"] for r in rows), dtype=np.float32)
    matrix = EmbeddingMatrix(keys=keys, vectors=vectors.reshape(len(rows), dim))
    _CACHE[token] = matrix
    return matrix


def store_embeddings(
    conn: sqlite3.Connection, items: Sequence[tuple[str, str, np.ndarray]]
) -> int:
    """Ghi (kind, rid, vector) vào bảng embeddings."""
    rows = [
        (kind, rid, settings.embed_model, int(vec.shape[0]), vec.astype(np.float32).tobytes())
        for kind, rid, vec in items
    ]
    conn.executemany(
        "INSERT INTO embeddings (kind, rid, model, dim, vector) VALUES (?,?,?,?,?)"
        " ON CONFLICT(kind, rid) DO UPDATE SET"
        " model = excluded.model, dim = excluded.dim, vector = excluded.vector",
        rows,
    )
    _CACHE.clear()
    return len(rows)
