"""Kiểm thử tương tác dữ liệu với PostgreSQL trên Docker (psycopg 3, JSONB, Full-Text Search)."""
from __future__ import annotations

import pytest
from psycopg.rows import dict_row

from aistem.config import settings
from aistem.store.postgres import get_postgres_connection, get_postgres_summary


@pytest.fixture
def pg_conn():
    with get_postgres_connection() as conn:
        yield conn


def test_postgres_connection_and_stats(pg_conn):
    stats = get_postgres_summary(pg_conn)
    assert stats["total_records"] >= 10650
    assert stats["formula"] == 5272
    assert stats["lesson"] >= 990
    assert stats["problem"] == 4351
    assert stats["exam"] == 41
    assert stats["edges"] >= 22286
    assert stats["scholarships"] >= 24



def test_postgres_scholarships_query(pg_conn):
    with pg_conn.cursor(row_factory=dict_row) as cur:
        # Lấy học bổng Full-Ride
        cur.execute("SELECT id, name, country, financial_value_usd, coverage FROM scholarships WHERE coverage = 'full-ride' ORDER BY financial_value_usd DESC LIMIT 5")
        rows = cur.fetchall()
        assert len(rows) == 5
        assert all(r["coverage"] == "full-ride" for r in rows)
        assert rows[0]["financial_value_usd"] >= 80000

        # Lấy học bổng theo tags JSONB
        cur.execute("SELECT id, name FROM scholarships WHERE tags ? 'ivy-league'")
        ivy_rows = cur.fetchall()
        assert len(ivy_rows) >= 2


def test_postgres_records_jsonb_query(pg_conn):
    with pg_conn.cursor(row_factory=dict_row) as cur:
        # Truy vấn trực tiếp vào trường JSONB payload
        cur.execute("SELECT rid, kind, title, payload->>'latex' AS latex FROM records WHERE kind = 'formula' AND subject = 'math' LIMIT 3")
        rows = cur.fetchall()
        assert len(rows) == 3
        for r in rows:
            assert r["kind"] == "formula"
            assert r["latex"] is not None


def test_postgres_text_search(pg_conn):
    with pg_conn.cursor(row_factory=dict_row) as cur:
        # Tìm kiếm toàn văn bằng tsvector và unaccent
        cur.execute("""
            SELECT rid, title, kind, subject
            FROM records
            WHERE search_tsv @@ to_tsquery('simple', 'newton | bernoulli')
            LIMIT 5
        """)
        rows = cur.fetchall()
        assert len(rows) > 0
