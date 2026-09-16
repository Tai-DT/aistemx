"""Kiểm thử kho bài toán chuyên sâu trên PostgreSQL và REST API."""
from __future__ import annotations

import pytest
from fastapi.testclient import TestClient
from psycopg.rows import dict_row

from aistem.store.postgres import get_postgres_connection, query_problems, get_postgres_summary
from server import app


@pytest.fixture
def pg_conn():
    with get_postgres_connection() as conn:
        yield conn


def test_postgres_problems_count_and_stats(pg_conn):
    stats = get_postgres_summary(pg_conn)
    assert stats["problems"] == 4351
    assert stats["problems_cas_verified"] >= 0


def test_postgres_query_problems_filters(pg_conn):
    # Lọc theo môn và dạng bài
    res = query_problems(pg_conn, subject="physics", ptype="dien-so", limit=5)
    assert res["total"] > 0
    assert len(res["problems"]) == 5
    for p in res["problems"]:
        assert p["subject"] == "physics"
        assert p["type"] == "dien-so"
        assert p["answer_numeric"] is not None


def test_postgres_query_problems_search(pg_conn):
    # Tìm kiếm theo từ khoá tiếng Việt
    res = query_problems(pg_conn, search_query="Coulomb", limit=5)
    assert res["total"] > 0
    assert any("coulomb" in p["statement_vi"].lower() or "coulomb" in p["topic"].lower() for p in res["problems"])


def test_postgres_problems_jsonb_indexing(pg_conn):
    with pg_conn.cursor(row_factory=dict_row) as cur:
        # Kiểm tra JSONB choices trên trắc nghiệm
        cur.execute("""
            SELECT id, type, choices
            FROM problems
            WHERE type = 'trac-nghiem' AND jsonb_array_length(choices) >= 4
            LIMIT 5;
        """)
        rows = cur.fetchall()
        assert len(rows) == 5
        for r in rows:
            assert len(r["choices"]) >= 4
            # Kiểm tra distractors có why_wrong
            distractors = [c for c in r["choices"] if c.get("why_wrong")]
            assert len(distractors) >= 1


def test_api_problems_list_and_detail():
    client = TestClient(app)

    # 1. Danh sách bài tập
    resp = client.get("/api/problems?subject=physics&type=dien-so&page_size=3")
    assert resp.status_code == 200
    data = resp.json()
    assert data["engine"] == "postgres"
    assert data["total"] > 0
    assert len(data["problems"]) == 3

    prob_id = data["problems"][0]["id"]

    # 2. Chi tiết bài tập
    detail_resp = client.get(f"/api/problems/{prob_id}")
    assert detail_resp.status_code == 200
    prob = detail_resp.json()
    assert prob["id"] == prob_id
    assert "solution_steps" in prob
    assert "formulas_used" in prob


def test_api_problems_stats():
    client = TestClient(app)
    resp = client.get("/api/problems-stats")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 4351
    assert len(data["by_subject"]) >= 4
    assert len(data["by_type"]) >= 3
