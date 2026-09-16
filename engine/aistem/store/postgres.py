"""Mô-đun quản lý PostgreSQL & Đồng bộ Dữ liệu Toàn diện cho AISTEM trên Docker.

Hỗ trợ:
- Lược đồ cơ sở dữ liệu quan hệ chuẩn PostgreSQL 16
- Hỗ trợ kiểu dữ liệu JSONB, chỉ mục GIN, tìm kiếm toàn văn Full-Text Search và Trigram
- Đồng bộ tự động toàn bộ kho dữ liệu (Formulas, Lessons, Problems, Exams, Edges, Skills, Scholarships)
"""
from __future__ import annotations

import json
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterator, List, Optional

import psycopg
from psycopg.rows import dict_row

from ..config import settings


POSTGRES_SCHEMA = """
-- Kích hoạt extension hỗ trợ tìm kiếm không dấu và độ tương đồng chuỗi
CREATE EXTENSION IF NOT EXISTS "unaccent";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Bảng records lưu trữ toàn bộ 4 kho (Formulas, Lessons, Problems, Exams)
CREATE TABLE IF NOT EXISTS records (
    id          BIGSERIAL PRIMARY KEY,
    kind        VARCHAR(32) NOT NULL,          -- formula | lesson | problem | exam
    rid         VARCHAR(128) NOT NULL,         -- id gốc trong kho (vd: prob.math.001)
    subject     VARCHAR(64) NOT NULL DEFAULT '',
    level       VARCHAR(64) NOT NULL DEFAULT '',
    topic       VARCHAR(128) NOT NULL DEFAULT '',
    title       TEXT NOT NULL DEFAULT '',
    grades      JSONB NOT NULL DEFAULT '[]'::jsonb,
    curriculum  JSONB NOT NULL DEFAULT '[]'::jsonb,
    tags        JSONB NOT NULL DEFAULT '[]'::jsonb,
    difficulty  INTEGER,
    ptype       VARCHAR(64) NOT NULL DEFAULT '',
    source_file TEXT NOT NULL DEFAULT '',
    payload     JSONB NOT NULL,
    search_tsv  TSVECTOR,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    CONSTRAINT uq_records_kind_rid UNIQUE (kind, rid)
);

CREATE INDEX IF NOT EXISTS idx_records_kind_subject ON records (kind, subject);
CREATE INDEX IF NOT EXISTS idx_records_level        ON records (level);
CREATE INDEX IF NOT EXISTS idx_records_topic        ON records (topic);
CREATE INDEX IF NOT EXISTS idx_records_rid          ON records (rid);
CREATE INDEX IF NOT EXISTS idx_records_payload_gin  ON records USING GIN (payload);
CREATE INDEX IF NOT EXISTS idx_records_tags_gin     ON records USING GIN (tags);
CREATE INDEX IF NOT EXISTS idx_records_title_trgm   ON records USING GIN (title gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_records_search_tsv   ON records USING GIN (search_tsv);

-- Đồ thị liên kết quan hệ tri thức
CREATE TABLE IF NOT EXISTS edges (
    src_kind VARCHAR(32) NOT NULL,
    src_id   VARCHAR(128) NOT NULL,
    rel      VARCHAR(64) NOT NULL,
    dst_kind VARCHAR(32) NOT NULL,
    dst_id   VARCHAR(128) NOT NULL,
    PRIMARY KEY (src_kind, src_id, rel, dst_id)
);

CREATE INDEX IF NOT EXISTS idx_edges_dst ON edges (dst_kind, dst_id, rel);

-- Kỹ năng từng bài tập phục vụ chẩn đoán lỗ hổng kiến thức
CREATE TABLE IF NOT EXISTS problem_skills (
    problem_id VARCHAR(128) NOT NULL,
    skill      TEXT NOT NULL,
    skill_fold TEXT NOT NULL,
    skill_key  TEXT NOT NULL DEFAULT '',
    PRIMARY KEY (problem_id, skill)
);

CREATE INDEX IF NOT EXISTS idx_problem_skills_fold ON problem_skills (skill_fold);
CREATE INDEX IF NOT EXISTS idx_problem_skills_key  ON problem_skills (skill_key);

-- Chỉ mục ngược token kỹ năng
CREATE TABLE IF NOT EXISTS skill_tokens (
    token      VARCHAR(128) NOT NULL,
    problem_id VARCHAR(128) NOT NULL,
    PRIMARY KEY (token, problem_id)
);

CREATE INDEX IF NOT EXISTS idx_skill_tokens_prob ON skill_tokens (problem_id);

-- Minh họa khoa học 2D SVG / 3D
CREATE TABLE IF NOT EXISTS illustrations (
    formula_id  VARCHAR(128) PRIMARY KEY,
    kind        VARCHAR(32) NOT NULL DEFAULT '2d-svg',
    source      TEXT NOT NULL DEFAULT '',
    generator   TEXT NOT NULL DEFAULT '',
    caption_vi  TEXT NOT NULL DEFAULT '',
    subject     VARCHAR(64) NOT NULL DEFAULT '',
    level       VARCHAR(64) NOT NULL DEFAULT '',
    topic       VARCHAR(128) NOT NULL DEFAULT '',
    title       TEXT NOT NULL DEFAULT '',
    svg_path    TEXT,
    raster_path TEXT,
    width       INTEGER,
    height      INTEGER,
    status      VARCHAR(32) NOT NULL DEFAULT '',
    payload     JSONB NOT NULL DEFAULT '{}'::jsonb,
    updated_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_illus_kind ON illustrations (kind);
CREATE INDEX IF NOT EXISTS idx_illus_subj_lvl ON illustrations (subject, level);

-- Cơ sở dữ liệu Học bổng Toàn phần & Tinh hoa Toàn cầu
CREATE TABLE IF NOT EXISTS scholarships (
    id                  VARCHAR(128) PRIMARY KEY,
    name                TEXT NOT NULL,
    country             VARCHAR(128) NOT NULL,
    provider            TEXT NOT NULL,
    type                VARCHAR(64) NOT NULL,
    coverage            VARCHAR(64) NOT NULL,
    financial_value_usd NUMERIC(12, 2) NOT NULL DEFAULT 0,
    gpa_min             NUMERIC(4, 2) NOT NULL DEFAULT 0,
    sat_min             INTEGER NOT NULL DEFAULT 0,
    ielts_min           NUMERIC(3, 1) NOT NULL DEFAULT 0,
    ap_recommended      INTEGER NOT NULL DEFAULT 0,
    target_majors       JSONB NOT NULL DEFAULT '[]'::jsonb,
    overview            TEXT NOT NULL,
    selection_criteria  JSONB NOT NULL DEFAULT '[]'::jsonb,
    requirements        JSONB NOT NULL DEFAULT '{}'::jsonb,
    deadlines           JSONB NOT NULL DEFAULT '{}'::jsonb,
    official_url        TEXT NOT NULL,
    tags                JSONB NOT NULL DEFAULT '[]'::jsonb,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_scholarships_country ON scholarships (country);
CREATE INDEX IF NOT EXISTS idx_scholarships_coverage ON scholarships (coverage);
CREATE INDEX IF NOT EXISTS idx_scholarships_type ON scholarships (type);
CREATE INDEX IF NOT EXISTS idx_scholarships_tags_gin ON scholarships USING GIN (tags);

-- Cơ sở dữ liệu Chuyên sâu 4,351 Bài toán STEM
CREATE TABLE IF NOT EXISTS problems (
    id                  VARCHAR(128) PRIMARY KEY,
    subject             VARCHAR(64) NOT NULL DEFAULT '',
    level               VARCHAR(64) NOT NULL DEFAULT '',
    topic               VARCHAR(128) NOT NULL DEFAULT '',
    grades              JSONB NOT NULL DEFAULT '[]'::jsonb,
    curriculum          JSONB NOT NULL DEFAULT '[]'::jsonb,
    type                VARCHAR(32) NOT NULL DEFAULT 'trac-nghiem',
    statement_vi        TEXT NOT NULL DEFAULT '',
    statement_en        TEXT NOT NULL DEFAULT '',
    answer              TEXT NOT NULL DEFAULT '',
    answer_numeric      DOUBLE PRECISION,
    answer_unit         VARCHAR(64) NOT NULL DEFAULT '',
    tolerance           DOUBLE PRECISION NOT NULL DEFAULT 0.0,
    choices             JSONB NOT NULL DEFAULT '[]'::jsonb,
    solution_steps      JSONB NOT NULL DEFAULT '[]'::jsonb,
    formulas_used       JSONB NOT NULL DEFAULT '[]'::jsonb,
    difficulty          INTEGER NOT NULL DEFAULT 2,
    estimated_minutes   DOUBLE PRECISION NOT NULL DEFAULT 5,
    skills              JSONB NOT NULL DEFAULT '[]'::jsonb,
    hints               JSONB NOT NULL DEFAULT '[]'::jsonb,
    tags                JSONB NOT NULL DEFAULT '[]'::jsonb,
    sources             JSONB NOT NULL DEFAULT '[]'::jsonb,
    source_file         TEXT NOT NULL DEFAULT '',
    cas_verified        BOOLEAN NOT NULL DEFAULT FALSE,
    cas_status          VARCHAR(32) NOT NULL DEFAULT 'unchecked',
    cas_details         JSONB NOT NULL DEFAULT '{}'::jsonb,
    search_tsv          TSVECTOR,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_problems_subject_level ON problems (subject, level);
CREATE INDEX IF NOT EXISTS idx_problems_topic         ON problems (topic);
CREATE INDEX IF NOT EXISTS idx_problems_type          ON problems (type);
CREATE INDEX IF NOT EXISTS idx_problems_difficulty    ON problems (difficulty);
CREATE INDEX IF NOT EXISTS idx_problems_cas_verified  ON problems (cas_verified);
CREATE INDEX IF NOT EXISTS idx_problems_cas_status    ON problems (cas_status);
CREATE INDEX IF NOT EXISTS idx_problems_choices_gin   ON problems USING GIN (choices);
CREATE INDEX IF NOT EXISTS idx_problems_steps_gin     ON problems USING GIN (solution_steps);
CREATE INDEX IF NOT EXISTS idx_problems_formulas_gin  ON problems USING GIN (formulas_used);
CREATE INDEX IF NOT EXISTS idx_problems_skills_gin    ON problems USING GIN (skills);
CREATE INDEX IF NOT EXISTS idx_problems_tags_gin      ON problems USING GIN (tags);
CREATE INDEX IF NOT EXISTS idx_problems_search_tsv    ON problems USING GIN (search_tsv);


-- Lịch sử làm bài tập
CREATE TABLE IF NOT EXISTS attempts (
    id          BIGSERIAL PRIMARY KEY,
    learner     VARCHAR(64) NOT NULL DEFAULT 'local',
    problem_id  VARCHAR(128) NOT NULL,
    answer      TEXT NOT NULL DEFAULT '',
    correct     BOOLEAN NOT NULL DEFAULT FALSE,
    verdict     TEXT NOT NULL DEFAULT '',
    created_at  TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_attempts_learner ON attempts (learner, created_at DESC);

-- Tiến độ bài học
CREATE TABLE IF NOT EXISTS lesson_progress (
    learner      VARCHAR(64) NOT NULL DEFAULT 'local',
    lesson_id    VARCHAR(128) NOT NULL,
    status       VARCHAR(32) NOT NULL DEFAULT 'done',
    completed_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (learner, lesson_id)
);

-- Thống kê ôn tập kỹ năng theo thuật toán FSRS / SM-2
CREATE TABLE IF NOT EXISTS skill_reviews (
    learner       VARCHAR(64) NOT NULL DEFAULT 'local',
    skill_key     TEXT NOT NULL,
    skill_label   TEXT NOT NULL DEFAULT '',
    repetitions   INTEGER NOT NULL DEFAULT 0,
    ease          REAL NOT NULL DEFAULT 2.5,
    interval_days REAL NOT NULL DEFAULT 0,
    due_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    last_seen_at  TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    lapses        INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (learner, skill_key)
);

-- Bảng metadata hệ thống
CREATE TABLE IF NOT EXISTS meta (
    key   VARCHAR(128) PRIMARY KEY,
    value TEXT NOT NULL
);

-- Bảng công thức tương tác và tham số hoá tính toán thời gian thực
CREATE TABLE IF NOT EXISTS formula_interactive (
    formula_id        VARCHAR(128) PRIMARY KEY,
    name_vi           TEXT NOT NULL,
    subject           TEXT NOT NULL,
    interactive_type  TEXT NOT NULL,
    is_computable     BOOLEAN NOT NULL DEFAULT FALSE,
    output_symbol     TEXT,
    output_name       TEXT,
    output_unit       TEXT,
    expression_js     TEXT,
    expression_py     TEXT,
    inputs            JSONB NOT NULL DEFAULT '[]'::jsonb,
    config            JSONB NOT NULL,
    created_at        TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at        TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_interactive_subject ON formula_interactive (subject);
CREATE INDEX IF NOT EXISTS idx_interactive_type ON formula_interactive (interactive_type);
CREATE INDEX IF NOT EXISTS idx_interactive_computable ON formula_interactive (is_computable);

-- Quản lý tài khoản học viên & người dùng
CREATE TABLE IF NOT EXISTS learners (
    id           VARCHAR(64) PRIMARY KEY,
    name         TEXT NOT NULL,
    email        TEXT NOT NULL UNIQUE,
    school       TEXT NOT NULL DEFAULT '',
    grade        INTEGER NOT NULL DEFAULT 12,
    target_major TEXT NOT NULL DEFAULT 'Computer Science / STEM',
    role         VARCHAR(32) NOT NULL DEFAULT 'student',
    created_at   TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Lịch sử đánh giá hồ sơ săn học bổng quốc tế
CREATE TABLE IF NOT EXISTS scholarship_evaluations (
    id              BIGSERIAL PRIMARY KEY,
    learner         VARCHAR(64) NOT NULL,
    gpa             REAL NOT NULL,
    sat             INTEGER DEFAULT 0,
    ielts           REAL DEFAULT 0,
    stem_awards     JSONB NOT NULL DEFAULT '[]'::jsonb,
    spike_projects  JSONB NOT NULL DEFAULT '[]'::jsonb,
    research_papers INTEGER DEFAULT 0,
    tier            VARCHAR(32) NOT NULL,
    tier_name       TEXT NOT NULL,
    total_score     REAL NOT NULL,
    gap_analysis    JSONB NOT NULL DEFAULT '[]'::jsonb,
    evaluated_at    TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
CREATE INDEX IF NOT EXISTS idx_evaluations_learner ON scholarship_evaluations (learner, evaluated_at DESC);
"""


@contextmanager
def get_postgres_connection(connection_url: Optional[str] = None) -> Iterator[psycopg.Connection]:
    """Tạo kết nối PostgreSQL dạng context manager."""
    url = connection_url or settings.postgres_url
    conn = psycopg.connect(url, autocommit=False)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_postgres_schema(conn: psycopg.Connection) -> None:
    """Khởi tạo toàn bộ cấu trúc bảng và chỉ mục trên PostgreSQL."""
    with conn.cursor() as cur:
        cur.execute(POSTGRES_SCHEMA)
    conn.commit()


def _normalize_difficulty(val: Any) -> Optional[int]:
    if val is None:
        return None
    if isinstance(val, int):
        return val
    s = str(val).lower().strip()
    if s.isdigit():
        return int(s)
    mapping = {
        "co-ban": 1,
        "trung-binh": 2,
        "nang-cao": 3,
        "chuyen-sau": 4,
        "olympic": 5,
    }
    return mapping.get(s, 3)


def migrate_sqlite_to_postgres(
    sqlite_db_path: Path | str,
    pg_conn: psycopg.Connection,
    batch_size: int = 1000
) -> Dict[str, Any]:
    """Chuyển đổi toàn bộ dữ liệu từ SQLite (aistem.db) sang PostgreSQL."""
    t0 = time.perf_counter()
    sq_conn = sqlite3.connect(str(sqlite_db_path))
    sq_conn.row_factory = sqlite3.Row

    init_postgres_schema(pg_conn)
    report: Dict[str, int] = {}

    with pg_conn.cursor() as cur:
        # 1. Bảng records
        sq_cur = sq_conn.execute("SELECT * FROM records ORDER BY rowid")
        records_batch: List[tuple] = []
        total_records = 0

        insert_record_sql = """
            INSERT INTO records (
                kind, rid, subject, level, topic, title, grades, curriculum,
                tags, difficulty, ptype, source_file, payload, search_tsv
            ) VALUES (
                %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb,
                %s::jsonb, %s, %s, %s, %s::jsonb,
                to_tsvector('simple', %s)
            )
            ON CONFLICT (kind, rid) DO UPDATE SET
                subject = EXCLUDED.subject,
                level = EXCLUDED.level,
                topic = EXCLUDED.topic,
                title = EXCLUDED.title,
                grades = EXCLUDED.grades,
                curriculum = EXCLUDED.curriculum,
                tags = EXCLUDED.tags,
                difficulty = EXCLUDED.difficulty,
                ptype = EXCLUDED.ptype,
                source_file = EXCLUDED.source_file,
                payload = EXCLUDED.payload,
                search_tsv = EXCLUDED.search_tsv,
                updated_at = NOW();
        """

        while True:
            rows = sq_cur.fetchmany(batch_size)
            if not rows:
                break
            for r in rows:
                search_text = f"{r['title']} {r['topic']}"
                diff_norm = _normalize_difficulty(r["difficulty"])
                records_batch.append((
                    r["kind"],
                    r["rid"],
                    r["subject"] or "",
                    r["level"] or "",
                    r["topic"] or "",
                    r["title"] or "",
                    r["grades"] or "[]",
                    r["curriculum"] or "[]",
                    r["tags"] or "[]",
                    diff_norm,
                    r["ptype"] or "",
                    r["source_file"] or "",
                    r["payload"],
                    search_text
                ))

            cur.executemany(insert_record_sql, records_batch)
            total_records += len(records_batch)
            records_batch.clear()

        report["records"] = total_records

        # 2. Bảng edges
        cur.execute("DELETE FROM edges;")
        sq_edges = sq_conn.execute("SELECT src_kind, src_id, rel, dst_kind, dst_id FROM edges").fetchall()
        edges_data = [tuple(e) for e in sq_edges]
        if edges_data:
            cur.executemany(
                "INSERT INTO edges (src_kind, src_id, rel, dst_kind, dst_id) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;",
                edges_data
            )
        report["edges"] = len(edges_data)

        # 3. Bảng problem_skills
        cur.execute("DELETE FROM problem_skills;")
        sq_skills = sq_conn.execute("SELECT problem_id, skill, skill_fold, skill_key FROM problem_skills").fetchall()
        skills_data = [tuple(s) for s in sq_skills]
        if skills_data:
            cur.executemany(
                "INSERT INTO problem_skills (problem_id, skill, skill_fold, skill_key) VALUES (%s, %s, %s, %s) ON CONFLICT DO NOTHING;",
                skills_data
            )
        report["problem_skills"] = len(skills_data)

        # 4. Bảng skill_tokens
        cur.execute("DELETE FROM skill_tokens;")
        sq_tokens = sq_conn.execute("SELECT token, problem_id FROM skill_tokens").fetchall()
        tokens_data = [tuple(t) for t in sq_tokens]
        if tokens_data:
            cur.executemany(
                "INSERT INTO skill_tokens (token, problem_id) VALUES (%s, %s) ON CONFLICT DO NOTHING;",
                tokens_data
            )
        report["skill_tokens"] = len(tokens_data)

        # 5. Bảng illustrations
        sq_illus = sq_conn.execute("SELECT * FROM illustrations").fetchall()
        illus_batch: List[tuple] = []
        for il in sq_illus:
            illus_batch.append((
                il["formula_id"],
                il["kind"] or "2d-svg",
                il["source"] or "",
                il["generator"] or "",
                il["caption_vi"] or "",
                il["subject"] or "",
                il["level"] or "",
                il["topic"] or "",
                il["title"] or "",
                il["svg_path"],
                il["raster_path"],
                il["width"],
                il["height"],
                il["status"] or "",
                il["payload"] or "{}"
            ))

        if illus_batch:
            cur.executemany(
                """
                INSERT INTO illustrations (
                    formula_id, kind, source, generator, caption_vi, subject, level, topic,
                    title, svg_path, raster_path, width, height, status, payload
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb)
                ON CONFLICT (formula_id) DO UPDATE SET
                    caption_vi = EXCLUDED.caption_vi,
                    svg_path = EXCLUDED.svg_path,
                    payload = EXCLUDED.payload,
                    updated_at = NOW();
                """,
                illus_batch
            )
        report["illustrations"] = len(illus_batch)

        # 6. Bảng meta
        sq_meta = sq_conn.execute("SELECT key, value FROM meta").fetchall()
        for m in sq_meta:
            cur.execute(
                "INSERT INTO meta (key, value) VALUES (%s, %s) ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value;",
                (m["key"], m["value"])
            )
        report["meta"] = len(sq_meta)

    pg_conn.commit()
    sq_conn.close()

    elapsed = time.perf_counter() - t0
    report["elapsed_seconds"] = round(elapsed, 2)
    return report


def migrate_scholarships_to_postgres(
    scholarships_file: Path | str,
    pg_conn: psycopg.Connection
) -> int:
    """Nạp danh sách học bổng toàn cầu từ file JSON vào bảng scholarships trên PostgreSQL."""
    path = Path(scholarships_file)
    if not path.exists():
        return 0

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        items = data.get("scholarships", [])

    insert_sch_sql = """
        INSERT INTO scholarships (
            id, name, country, provider, type, coverage, financial_value_usd,
            gpa_min, sat_min, ielts_min, ap_recommended, target_majors,
            overview, selection_criteria, requirements, deadlines, official_url, tags
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s::jsonb,
            %s, %s::jsonb, %s::jsonb, %s::jsonb, %s, %s::jsonb
        )
        ON CONFLICT (id) DO UPDATE SET
            name = EXCLUDED.name,
            country = EXCLUDED.country,
            provider = EXCLUDED.provider,
            type = EXCLUDED.type,
            coverage = EXCLUDED.coverage,
            financial_value_usd = EXCLUDED.financial_value_usd,
            gpa_min = EXCLUDED.gpa_min,
            sat_min = EXCLUDED.sat_min,
            ielts_min = EXCLUDED.ielts_min,
            ap_recommended = EXCLUDED.ap_recommended,
            target_majors = EXCLUDED.target_majors,
            overview = EXCLUDED.overview,
            selection_criteria = EXCLUDED.selection_criteria,
            requirements = EXCLUDED.requirements,
            deadlines = EXCLUDED.deadlines,
            official_url = EXCLUDED.official_url,
            tags = EXCLUDED.tags,
            updated_at = NOW();
    """

    batch: List[tuple] = []
    for s in items:
        batch.append((
            s["id"],
            s["name"],
            s["country"],
            s["provider"],
            s["type"],
            s["coverage"],
            float(s.get("financial_value_usd", 0)),
            float(s.get("gpa_min", 0.0)),
            int(s.get("sat_min", 0)),
            float(s.get("ielts_min", 0.0)),
            int(s.get("ap_recommended", 0)),
            json.dumps(s.get("target_majors", [])),
            s["overview"],
            json.dumps(s.get("selection_criteria", [])),
            json.dumps(s.get("requirements", {})),
            json.dumps(s.get("deadlines", {})),
            s["official_url"],
            json.dumps(s.get("tags", []))
        ))

    with pg_conn.cursor() as cur:
        cur.executemany(insert_sch_sql, batch)
    pg_conn.commit()
    return len(batch)


def migrate_problems_to_postgres(
    problems_dir: Path | str,
    pg_conn: psycopg.Connection,
    batch_size: int = 500
) -> int:
    """Nạp toàn bộ 4,351 bài toán từ các tệp JSON trong thư mục problems vào bảng problems trên PostgreSQL."""
    p_dir = Path(problems_dir)
    if not p_dir.exists():
        return 0

    json_files = sorted(p for p in p_dir.rglob("*.json") if p.name not in {"index.json", "schema.json"})
    insert_sql = """
        INSERT INTO problems (
            id, subject, level, topic, grades, curriculum, type,
            statement_vi, statement_en, answer, answer_numeric, answer_unit, tolerance,
            choices, solution_steps, formulas_used, difficulty, estimated_minutes,
            skills, hints, tags, sources, source_file, search_tsv
        ) VALUES (
            %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s,
            %s, %s, %s, %s, %s, %s,
            %s::jsonb, %s::jsonb, %s::jsonb, %s, %s,
            %s::jsonb, %s::jsonb, %s::jsonb, %s::jsonb, %s,
            to_tsvector('simple', unaccent(%s))
        )
        ON CONFLICT (id) DO UPDATE SET
            subject = EXCLUDED.subject,
            level = EXCLUDED.level,
            topic = EXCLUDED.topic,
            grades = EXCLUDED.grades,
            curriculum = EXCLUDED.curriculum,
            type = EXCLUDED.type,
            statement_vi = EXCLUDED.statement_vi,
            statement_en = EXCLUDED.statement_en,
            answer = EXCLUDED.answer,
            answer_numeric = EXCLUDED.answer_numeric,
            answer_unit = EXCLUDED.answer_unit,
            tolerance = EXCLUDED.tolerance,
            choices = EXCLUDED.choices,
            solution_steps = EXCLUDED.solution_steps,
            formulas_used = EXCLUDED.formulas_used,
            difficulty = EXCLUDED.difficulty,
            estimated_minutes = EXCLUDED.estimated_minutes,
            skills = EXCLUDED.skills,
            hints = EXCLUDED.hints,
            tags = EXCLUDED.tags,
            sources = EXCLUDED.sources,
            source_file = EXCLUDED.source_file,
            search_tsv = EXCLUDED.search_tsv,
            updated_at = NOW();
    """

    total_inserted = 0
    batch: List[tuple] = []

    with pg_conn.cursor() as cur:
        for fpath in json_files:
            rel_path = str(fpath.name)
            try:
                content = fpath.read_text(encoding="utf-8")
                doc = json.loads(content)
                items = doc.get("problems", []) if isinstance(doc, dict) else (doc if isinstance(doc, list) else [])
            except Exception as e:
                print(f"Lỗi đọc {fpath}: {e}")
                continue

            for p in items:
                if not isinstance(p, dict) or not p.get("id"):
                    continue

                pid = str(p["id"])
                subj = str(p.get("subject") or "math")
                lvl = str(p.get("level") or "thpt")
                top = str(p.get("topic") or "")

                raw_grades = p.get("grades", [])
                grades = raw_grades if isinstance(raw_grades, list) else [raw_grades]

                raw_curr = p.get("curriculum", [])
                curriculum = raw_curr if isinstance(raw_curr, list) else [raw_curr]

                ptype = str(p.get("type") or "trac-nghiem")
                stmt_vi = str(p.get("statement_vi") or "")
                stmt_en = str(p.get("statement_en") or "")
                answer = str(p.get("answer") or "")

                ans_num = None
                if p.get("answer_numeric") is not None:
                    try:
                        ans_num = float(p["answer_numeric"])
                    except (ValueError, TypeError):
                        ans_num = None

                ans_unit = str(p.get("answer_unit") or "")
                try:
                    tol = float(p.get("tolerance", 0.0) or 0.0)
                except (ValueError, TypeError):
                    tol = 0.0

                choices = p.get("choices", [])
                solution_steps = p.get("solution_steps", [])
                formulas_used = p.get("formulas_used", [])

                diff = _normalize_difficulty(p.get("difficulty")) or 2
                try:
                    est_min = float(p.get("estimated_minutes", 5.0) or 5.0)
                except (ValueError, TypeError):
                    est_min = 5.0

                skills = p.get("skills", [])
                hints = p.get("hints", [])
                tags = p.get("tags", [])
                sources = p.get("sources", [])

                search_text = f"{stmt_vi} {top} {subj} {' '.join(tags if isinstance(tags, list) else [])}"

                batch.append((
                    pid, subj, lvl, top,
                    json.dumps(grades), json.dumps(curriculum), ptype,
                    stmt_vi, stmt_en, answer, ans_num, ans_unit, tol,
                    json.dumps(choices), json.dumps(solution_steps), json.dumps(formulas_used),
                    diff, est_min,
                    json.dumps(skills), json.dumps(hints), json.dumps(tags), json.dumps(sources),
                    rel_path, search_text
                ))

                if len(batch) >= batch_size:
                    cur.executemany(insert_sql, batch)
                    total_inserted += len(batch)
                    batch.clear()

        if batch:
            cur.executemany(insert_sql, batch)
            total_inserted += len(batch)
            batch.clear()

    pg_conn.commit()
    return total_inserted


def update_problem_cas_batch(
    pg_conn: psycopg.Connection,
    updates: List[Dict[str, Any]]
) -> int:
    """Cập nhật hàng loạt trạng thái kiểm chứng CAS cho các bài toán."""
    if not updates:
        return 0

    update_sql = """
        UPDATE problems
        SET cas_verified = %(cas_verified)s,
            cas_status = %(cas_status)s,
            cas_details = %(cas_details)s::jsonb,
            updated_at = NOW()
        WHERE id = %(id)s;
    """
    with pg_conn.cursor() as cur:
        cur.executemany(update_sql, updates)
    pg_conn.commit()
    return len(updates)


def query_problems(
    pg_conn: psycopg.Connection,
    subject: Optional[str] = None,
    level: Optional[str] = None,
    topic: Optional[str] = None,
    ptype: Optional[str] = None,
    difficulty: Optional[int] = None,
    cas_verified: Optional[bool] = None,
    skill: Optional[str] = None,
    search_query: Optional[str] = None,
    limit: int = 50,
    offset: int = 0
) -> Dict[str, Any]:
    """Truy vấn tìm kiếm bài toán linh hoạt trên PostgreSQL."""
    clauses: List[str] = []
    params: List[Any] = []

    if subject:
        clauses.append("subject = %s")
        params.append(subject)
    if level:
        clauses.append("level = %s")
        params.append(level)
    if topic:
        clauses.append("topic ILIKE %s")
        params.append(f"%{topic}%")
    if ptype:
        clauses.append("type = %s")
        params.append(ptype)
    if difficulty is not None:
        clauses.append("difficulty = %s")
        params.append(difficulty)
    if cas_verified is not None:
        clauses.append("cas_verified = %s")
        params.append(cas_verified)
    if skill:
        clauses.append("skills @> %s::jsonb")
        params.append(json.dumps([skill]))
    if search_query:
        clauses.append("search_tsv @@ plainto_tsquery('simple', unaccent(%s))")
        params.append(search_query)

    where_sql = (" WHERE " + " AND ".join(clauses)) if clauses else ""

    count_sql = f"SELECT COUNT(*) AS total FROM problems{where_sql}"
    select_sql = f"""
        SELECT id, subject, level, topic, grades, curriculum, type,
               statement_vi, statement_en, answer, answer_numeric, answer_unit, tolerance,
               choices, solution_steps, formulas_used, difficulty, estimated_minutes,
               skills, hints, tags, sources, source_file, cas_verified, cas_status, cas_details,
               created_at, updated_at
        FROM problems
        {where_sql}
        ORDER BY id
        LIMIT %s OFFSET %s
    """

    with pg_conn.cursor(row_factory=dict_row) as cur:
        cur.execute(count_sql, params)
        total = cur.fetchone()["total"]

        cur.execute(select_sql, params + [limit, offset])
        rows = cur.fetchall()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "problems": rows
    }


def migrate_interactive_to_postgres(
    interactive_file: Path | str,
    pg_conn: psycopg.Connection
) -> int:
    """Nạp toàn bộ cấu hình tham số tương tác cho 5,272 công thức vào PostgreSQL."""
    path = Path(interactive_file)
    if not path.exists():
        return 0

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        formulas = data.get("formulas", {})

    insert_sql = """
        INSERT INTO formula_interactive (
            formula_id, name_vi, subject, interactive_type, is_computable,
            output_symbol, output_name, output_unit,
            expression_js, expression_py, inputs, config
        ) VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s,
            %s, %s, %s::jsonb, %s::jsonb
        )
        ON CONFLICT (formula_id) DO UPDATE SET
            name_vi = EXCLUDED.name_vi,
            subject = EXCLUDED.subject,
            interactive_type = EXCLUDED.interactive_type,
            is_computable = EXCLUDED.is_computable,
            output_symbol = EXCLUDED.output_symbol,
            output_name = EXCLUDED.output_name,
            output_unit = EXCLUDED.output_unit,
            expression_js = EXCLUDED.expression_js,
            expression_py = EXCLUDED.expression_py,
            inputs = EXCLUDED.inputs,
            config = EXCLUDED.config,
            updated_at = NOW();
    """

    rows = []
    for fid, item in formulas.items():
        out = item.get("output", {})
        rows.append((
            fid,
            item.get("name_vi", ""),
            item.get("subject", ""),
            item.get("interactive_type", ""),
            bool(item.get("is_computable", False)),
            out.get("symbol", ""),
            out.get("name", ""),
            out.get("unit", ""),
            item.get("expression_js", ""),
            item.get("expression_py", ""),
            json.dumps(item.get("inputs", []), ensure_ascii=False),
            json.dumps(item, ensure_ascii=False),
        ))

    with pg_conn.cursor() as cur:
        cur.executemany(insert_sql, rows)
    pg_conn.commit()
    return len(rows)


def get_postgres_summary(pg_conn: psycopg.Connection) -> Dict[str, Any]:
    """Truy vấn tổng hợp số lượng bản ghi của từng thực thể trên PostgreSQL."""
    stats: Dict[str, Any] = {}
    with pg_conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT kind, COUNT(*) AS count FROM records GROUP BY kind ORDER BY kind")
        for row in cur.fetchall():
            stats[row["kind"]] = row["count"]

        cur.execute("SELECT COUNT(*) AS total FROM records")
        stats["total_records"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM edges")
        stats["edges"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM problem_skills")
        stats["problem_skills"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM skill_tokens")
        stats["skill_tokens"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM illustrations")
        stats["illustrations"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM scholarships")
        stats["scholarships"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM problems")
        stats["problems"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM problems WHERE cas_verified = TRUE")
        stats["problems_cas_verified"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM formula_interactive")
        stats["formula_interactive"] = cur.fetchone()["total"]

        cur.execute("SELECT COUNT(*) AS total FROM formula_interactive WHERE is_computable = TRUE")
        stats["interactive_computable"] = cur.fetchone()["total"]

    return stats


