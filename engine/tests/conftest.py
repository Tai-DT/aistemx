"""Đồ dùng chung cho test.

Toàn bộ test chạy được **không cần khoá API**: phần gọi mô hình được thay bằng
bản giả, còn phần lưu trữ / CAS / chấm bài vốn đã không phụ thuộc mô hình.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from aistem.config import settings
from aistem.store.build import build_database
from aistem.store.db import connect


@pytest.fixture(scope="session")
def db_path() -> Path:
    """Dùng lại file DB đã dựng nếu có; chưa có thì dựng một lần cho cả phiên."""
    target = settings.database
    if not target.exists():
        build_database(db_path=target)
    return target


@pytest.fixture
def conn(db_path: Path) -> sqlite3.Connection:
    connection = connect(db_path)
    try:
        yield connection
    finally:
        connection.rollback()
        connection.close()


@pytest.fixture
def fake_llm(monkeypatch):
    """Thay lớp gọi Claude bằng bản giả trả về kịch bản định sẵn.

    Nhờ vậy nhánh có mô hình vẫn được test đầy đủ — kể cả các đường xử lí lỗi
    như mô hình bịa id công thức hay đưa ra đáp số sai — mà không tốn một lời
    gọi API nào.
    """
    from aistem import llm

    state: dict[str, object] = {"payloads": {}, "calls": []}

    def _structured(*, system, prompt, schema, tool_name="tra_ket_qua", **kwargs):
        state["calls"].append(tool_name)
        payload = state["payloads"].get(tool_name)
        if payload is None:
            raise llm.LLMUnavailable(f"Test chưa cài kịch bản cho công cụ {tool_name!r}")
        return llm.LLMResult(data=payload, model="fake-model")

    # Mọi module trong pipeline đều dùng `from .. import llm`, nên chúng chia sẻ
    # đúng một đối tượng module — vá ở đây là vá cho tất cả.
    monkeypatch.setattr(llm, "available", lambda: True)
    monkeypatch.setattr(llm, "structured", _structured)
    return state
