"""Tầng lưu trữ và truy xuất."""

from __future__ import annotations

import sqlite3

import pytest

from aistem.store import Filters, load_record, search, stats, uses_formula
from aistem.store.search import _fts_query, problems_by_skill, rrf_fuse


def test_all_four_collections_loaded(conn: sqlite3.Connection) -> None:
    counts = stats(conn)["counts"]
    assert counts["formula"] > 5000
    assert counts["lesson"] > 600
    assert counts["problem"] > 900
    assert counts["exam"] >= 30


def test_diacritic_insensitive_search(conn: sqlite3.Connection) -> None:
    """Gõ không dấu vẫn phải ra kết quả có dấu — đây là cách người Việt gõ nhanh."""
    with_marks = search(conn, "đạo hàm của tích", filters=Filters(kinds=["formula"]), limit=5)
    without = search(conn, "dao ham cua tich", filters=Filters(kinds=["formula"]), limit=5)
    assert {h.id for h in without} & {h.id for h in with_marks}
    assert any("dao-ham-cua-tich" in h.id for h in without)


def test_filters_are_applied(conn: sqlite3.Connection) -> None:
    hits = search(
        conn, "năng lượng", filters=Filters(kinds=["formula"], subject="physics"), limit=10
    )
    assert hits and all(h.subject == "physics" for h in hits)


def test_grade_filter_matches_json_array(conn: sqlite3.Connection) -> None:
    hits = search(conn, "", filters=Filters(kinds=["formula"], grade=12), limit=5)
    assert hits and all(12 in (h.record or {}).get("grades", [12]) for h in hits if h.record)


def test_fts_query_neutralises_special_characters(conn: sqlite3.Connection) -> None:
    """Ký tự cú pháp FTS5 phải bị vô hiệu, không được làm sập truy vấn."""
    for hostile in ('a" OR "b', "NEAR(x y)", "col:value", "*", '"""', "^abc", "x AND"):
        search(conn, hostile, limit=3)  # không được ném lỗi
    assert _fts_query('a" OR "b').count('"') % 2 == 0


def test_reverse_graph(conn: sqlite3.Connection) -> None:
    hits = uses_formula(conn, "math.thpt.dao-ham.dao-ham-cua-tich", limit=10)
    assert hits
    assert all(h.kind.value in {"lesson", "problem", "exam"} for h in hits)


def test_problems_by_skill(conn: sqlite3.Connection) -> None:
    hits = problems_by_skill(conn, ["phân tích đa thức thành nhân tử"], limit=5)
    assert hits and all(h.kind.value == "problem" for h in hits)


def test_rrf_rewards_agreement_between_channels() -> None:
    fused = rrf_fuse({"a": ["x", "y"], "b": ["y", "x"]}, k=60)
    assert fused["x"][0] == pytest.approx(fused["y"][0])
    fused = rrf_fuse({"a": ["x", "y"], "b": ["x", "z"]}, k=60)
    assert fused["x"][0] > fused["y"][0]


def test_load_record_returns_none_for_unknown(conn: sqlite3.Connection) -> None:
    assert load_record(conn, "formula", "khong-ton-tai") is None


def test_empty_query_browses(conn: sqlite3.Connection) -> None:
    hits = search(conn, "", filters=Filters(kinds=["exam"]), limit=5)
    assert len(hits) == 5
