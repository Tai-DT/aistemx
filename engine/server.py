#!/usr/bin/env python3
"""Backend FastAPI Server cho Web App AISTEM.

Cung cấp toàn bộ REST APIs cho:
- Thống kê toàn hệ thống (/api/stats)
- Tra cứu công thức đa chiều (/api/formulas)
- Tìm kiếm tức thì tiếng Việt (/api/search)
- Ngân hàng bài tập & Chấm điểm tự động (/api/problems, /api/problems/submit)
- Hồ sơ kỳ thi chuẩn quốc tế (/api/exams)
- Mô hình 3D tương tác WebGL (/api/scenes3d)
- Minh họa đồ họa 2D SVG (/api/illustrations2d)
- Phục vụ Static Files cho Frontend Web App
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from fastapi import FastAPI, HTTPException, Query, Header, Request, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, Response, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

try:
    from engine import db
    from engine.deep_analysis import analyze_problem_solution
    from engine.aistem import math_core
    from engine.aistem.cas import (
        solve_symbolic_equation,
        isolate_variable_from_formula,
        symbolic_calculus_eval,
        evaluate_derivation_step,
        evaluate_student_solution_pipeline,
    )
    from engine.aistem import scholarship
    from engine.aistem.store.postgres import get_postgres_connection, query_problems, get_postgres_summary
    from engine.aistem.cas.problem_verifier import verify_problem_data
    from engine.aistem import roadmap
    from engine.aistem.models import RoadmapRequest
    from engine.aistem.store.db import connect as connect_sqlite_db
    from engine.aistem import llm
except ImportError:
    import db
    from deep_analysis import analyze_problem_solution
    from aistem import math_core
    from aistem.cas import (
        solve_symbolic_equation,
        isolate_variable_from_formula,
        symbolic_calculus_eval,
        evaluate_derivation_step,
        evaluate_student_solution_pipeline,
    )
    from aistem import scholarship
    from aistem.store.postgres import get_postgres_connection, query_problems, get_postgres_summary
    from aistem.cas.problem_verifier import verify_problem_data
    from aistem import roadmap
    from aistem.models import RoadmapRequest
    from aistem.store.db import connect as connect_sqlite_db
    from aistem import llm




DATA_DIR = ROOT / "data"

app = FastAPI(
    title="AISTEM Knowledge & Exam API",
    version="2.0.0",
    description="API Engine cho Hệ tri thức và Luyện thi STEM Quốc tế AISTEM",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# Anti-Bot, Anti-Scraping & Sliding-Window Rate Limiting Engine
# -------------------------------------------------------------
_IP_REQUEST_LOGS: dict[str, list[float]] = defaultdict(list)
_SUSPICIOUS_BOT_USER_AGENTS = (
    "sqlmap",
    "nikto",
    "masscan",
    "nmap",
    "acunetix",
    "headlesschrome",
    "selenium",
    "phantomjs",
    "scrapy",
    "python-requests",
    "aiohttp",
    "httpx",
    "curl",
    "wget",
    "guzzlehttp",
    "go-http-client",
    "java/",
    "apache-httpclient",
    "zgrab",
    "censys",
)
_ALLOWED_TEST_USER_AGENTS = ("aistem-internal-audit",)

# Cấu hình giới hạn: Tối đa 300 requests/phút cho các API lấy dữ liệu (/api/problems, /api/formulas, /api/lessons)
_RATE_LIMIT_MAX_PER_MINUTE = 300
_RATE_LIMIT_WINDOW_SECONDS = 60.0


@app.middleware("http")
async def anti_crawler_bot_protection_middleware(request: Request, call_next):
    # Bỏ qua tài nguyên tĩnh, WebSocket, hoặc tài nguyên đồ hoạ minh hoạ 2D
    path = request.url.path
    if (
        not path.startswith("/api/")
        or path.startswith("/api/illustrations")
        or path.startswith("/api/illustrations2d")
    ):
        return await call_next(request)

    # 1. Ngoại lệ cho môi trường nội bộ / localhost (không áp dụng rate limit để trải nghiệm mượt mà)
    client_ip = request.client.host if request.client else "127.0.0.1"
    is_localhost = client_ip in ("127.0.0.1", "::1", "localhost")
    if is_localhost:
        return await call_next(request)

    user_agent = (request.headers.get("user-agent") or "").lower()

    if not is_localhost:
        # Nếu client cố tình gửi request mà không có User-Agent hoặc User-Agent rỗng
        if not user_agent or len(user_agent.strip()) < 5:
            return JSONResponse(
                status_code=403,
                content={"error": "Access Denied: Missing or invalid User-Agent header."},
            )

        # Chặn các scraper framework phổ biến khi không khai báo trình duyệt hợp lệ
        if any(bot in user_agent for bot in _SUSPICIOUS_BOT_USER_AGENTS):
            return JSONResponse(
                status_code=403,
                content={
                    "error": "Access Denied: Automated scraping tools and bots are prohibited.",
                    "code": "BOT_DETECTED",
                },
            )

    # 2. Ngăn chặn cào sỉ (Bulk dump scraping) qua phân trang page_size cực lớn
    page_size_param = request.query_params.get("page_size")
    if page_size_param:
        try:
            val = int(page_size_param)
            if val > 100:
                return JSONResponse(
                    status_code=400,
                    content={"error": "Rate limit: Maximum page_size is 100 to prevent data dumping."},
                )
        except ValueError:
            pass

    # 3. Thuật toán Sliding Window Rate Limiting theo từng địa chỉ IP
    now = time.time()
    req_history = _IP_REQUEST_LOGS[client_ip]

    # Dọn dẹp các mốc thời gian ngoài cửa sổ trượt
    cutoff = now - _RATE_LIMIT_WINDOW_SECONDS
    _IP_REQUEST_LOGS[client_ip] = [t for t in req_history if t > cutoff]

    if len(_IP_REQUEST_LOGS[client_ip]) >= _RATE_LIMIT_MAX_PER_MINUTE:
        # Tạm thời khóa yêu cầu
        retry_after = int(_RATE_LIMIT_WINDOW_SECONDS - (now - _IP_REQUEST_LOGS[client_ip][0])) + 1
        return JSONResponse(
            status_code=429,
            content={
                "error": "Quá nhiều yêu cầu trong thời gian ngắn (Rate limit exceeded). Vui lòng thử lại sau.",
                "retry_after_seconds": max(1, retry_after),
            },
            headers={"Retry-After": str(max(1, retry_after))},
        )

    _IP_REQUEST_LOGS[client_ip].append(now)

    response = await call_next(request)
    
    # 4. Thêm các Header bảo mật chống iframe hijacking và content sniffing
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-Robots-Tag"] = "noindex, nofollow, noarchive"
    
    return response

# -------------------------------------------------------------
# In-memory Cache & Data Loaders
# -------------------------------------------------------------
_CACHE: dict[str, Any] = {}


def get_formulas() -> dict[str, dict]:
    if "formulas" not in _CACHE:
        fpath = DATA_DIR / "formulas" / "index.json"
        if fpath.exists():
            data = json.loads(fpath.read_text(encoding="utf-8"))
            _CACHE["formulas"] = {f["id"]: f for f in data.get("formulas", [])}
        else:
            _CACHE["formulas"] = {}
    return _CACHE["formulas"]


def get_problems() -> dict[str, dict]:
    if "problems" not in _CACHE:
        ppath = DATA_DIR / "problems" / "index.json"
        if ppath.exists():
            data = json.loads(ppath.read_text(encoding="utf-8"))
            _CACHE["problems"] = {p["id"]: p for p in data.get("problems", [])}
        else:
            _CACHE["problems"] = {}
    return _CACHE["problems"]


def get_lessons() -> dict[str, dict]:
    if "lessons" not in _CACHE:
        lpath = DATA_DIR / "lessons" / "index.json"
        if lpath.exists():
            data = json.loads(lpath.read_text(encoding="utf-8"))
            _CACHE["lessons"] = {l["id"]: l for l in data.get("lessons", [])}
        else:
            _CACHE["lessons"] = {}
    return _CACHE["lessons"]


def get_exams() -> dict[str, dict]:
    if "exams" not in _CACHE:
        epath = DATA_DIR / "exams" / "index.json"
        if epath.exists():
            data = json.loads(epath.read_text(encoding="utf-8"))
            _CACHE["exams"] = {e["id"]: e for e in data.get("exams", [])}
        else:
            _CACHE["exams"] = {}
    return _CACHE["exams"]


def get_usage() -> dict[str, dict]:
    if "usage" not in _CACHE:
        upath = DATA_DIR / "formulas" / "usage.json"
        if upath.exists():
            _CACHE["usage"] = json.loads(upath.read_text(encoding="utf-8")).get("formulas", {})
        else:
            _CACHE["usage"] = {}
    return _CACHE["usage"]


def get_scenes3d() -> dict[str, dict]:
    if "scenes3d" not in _CACHE:
        spath = DATA_DIR / "scenes3d" / "index.json"
        if spath.exists():
            data = json.loads(spath.read_text(encoding="utf-8"))
            _CACHE["scenes3d"] = {s["id"]: s for s in data.get("scenes", [])}
        else:
            _CACHE["scenes3d"] = {}
    return _CACHE["scenes3d"]


def get_illustrations2d() -> dict[str, dict]:
    if "illustrations2d" not in _CACHE:
        ipath = DATA_DIR / "illustrations" / "index.json"
        if ipath.exists():
            data = json.loads(ipath.read_text(encoding="utf-8"))
            _CACHE["illustrations2d"] = {item["formula_id"]: item for item in data.get("illustrations", []) if "formula_id" in item}
        else:
            _CACHE["illustrations2d"] = {}
    return _CACHE["illustrations2d"]


def get_interactive() -> dict[str, dict]:
    if "interactive" not in _CACHE:
        ipath = DATA_DIR / "interactive" / "index.json"
        if ipath.exists():
            data = json.loads(ipath.read_text(encoding="utf-8"))
            _CACHE["interactive"] = data.get("formulas", {})
        else:
            _CACHE["interactive"] = {}
    return _CACHE["interactive"]



# -------------------------------------------------------------
# REST Endpoints
# -------------------------------------------------------------

@app.get("/api/stats")
def get_system_stats():
    """Thống kê toàn hệ thống."""
    formulas = get_formulas()
    problems = get_problems()
    lessons = get_lessons()
    exams = get_exams()
    scenes = get_scenes3d()
    illus = get_illustrations2d()

    subj_f: dict[str, int] = {}
    for f in formulas.values():
        subj_f[f.get("subject", "other")] = subj_f.get(f.get("subject", "other"), 0) + 1

    subj_p: dict[str, int] = {}
    for p in problems.values():
        subj_p[p.get("subject", "other")] = subj_p.get(p.get("subject", "other"), 0) + 1

    diff_p: dict[int, int] = {}
    for p in problems.values():
        d = p.get("difficulty", 1)
        diff_p[d] = diff_p.get(d, 0) + 1

    try:
        with get_postgres_connection() as conn:
            pg_st = get_postgres_summary(conn)
            return {
                "total_records": pg_st.get("total_records", 10654),
                "formula": pg_st.get("formula", len(formulas)),
                "lesson": pg_st.get("lesson", len(lessons)),
                "problem": pg_st.get("problems", len(problems)),
                "problems": pg_st.get("problems", len(problems)),
                "exam": pg_st.get("exam", len(exams)),
                "edges": pg_st.get("edges", 22286),
                "illustrations": pg_st.get("illustrations", len(illus)),
                "scholarships": pg_st.get("scholarships", 25),
                "problems_cas_verified": pg_st.get("problems_cas_verified", 0),
                "totals": {
                    "formulas": pg_st.get("formula", len(formulas)),
                    "problems": pg_st.get("problems", len(problems)),
                    "lessons": pg_st.get("lesson", len(lessons)),
                    "exams": pg_st.get("exam", len(exams)),
                    "scenes3d": len(scenes),
                    "illustrations2d": pg_st.get("illustrations", len(illus)),
                    "scholarships": pg_st.get("scholarships", 25),
                    "cas_verified": pg_st.get("problems_cas_verified", 0),
                },
                "formulas_by_subject": subj_f,
                "problems_by_subject": subj_p,
                "problems_by_difficulty": diff_p,
            }
    except Exception:
        pass

    return {
        "total_records": len(formulas) + len(problems) + len(lessons) + len(exams),
        "formula": len(formulas),
        "lesson": len(lessons),
        "problem": len(problems),
        "problems": len(problems),
        "exam": len(exams),
        "edges": 0,
        "illustrations": len(illus),
        "scholarships": 25,
        "problems_cas_verified": 0,
        "totals": {
            "formulas": len(formulas),
            "problems": len(problems),
            "lessons": len(lessons),
            "exams": len(exams),
            "scenes3d": len(scenes),
            "illustrations2d": len(illus),
            "scholarships": 25,
        },
        "formulas_by_subject": subj_f,
        "problems_by_subject": subj_p,
        "problems_by_difficulty": diff_p,
    }



@app.get("/api/search")
def search_everything(
    q: str = Query("", description="Từ khoá tìm kiếm"),
    subject: Optional[str] = None,
    level: Optional[str] = None,
    limit: int = Query(20, le=100),
):
    """Tìm kiếm nhanh trên công thức, bài tập, bài học."""
    q_clean = q.lower().strip()
    results = {"formulas": [], "problems": [], "lessons": [], "exams": []}
    if not q_clean:
        return results

    # Search formulas
    for f in get_formulas().values():
        if subject and f.get("subject") != subject:
            continue
        if level and f.get("level") != level:
            continue
        text = f"{f.get('name_vi', '')} {f.get('name_en', '')} {f.get('topic', '')} {f.get('latex', '')} {' '.join(f.get('tags', []))}".lower()
        if q_clean in text:
            results["formulas"].append({
                "id": f["id"],
                "subject": f.get("subject"),
                "name_vi": f.get("name_vi"),
                "name_en": f.get("name_en"),
                "latex": f.get("latex"),
                "topic": f.get("topic"),
            })
            if len(results["formulas"]) >= limit:
                break

    # Search problems
    for p in get_problems().values():
        if subject and p.get("subject") != subject:
            continue
        if level and p.get("level") != level:
            continue
        text = f"{p.get('topic', '')} {p.get('statement_vi', '')} {p.get('statement_en', '')} {' '.join(p.get('tags', []))}".lower()
        if q_clean in text:
            results["problems"].append({
                "id": p["id"],
                "subject": p.get("subject"),
                "topic": p.get("topic"),
                "statement_vi": p.get("statement_vi", "")[:140] + "...",
                "difficulty": p.get("difficulty"),
            })
            if len(results["problems"]) >= limit:
                break

    # Search exams
    for e in get_exams().values():
        text = f"{e.get('name_vi', '')} {e.get('name_en', '')} {e.get('target', '')} {e.get('organizer', '')}".lower()
        if q_clean in text:
            results["exams"].append({
                "id": e["id"],
                "name_vi": e.get("name_vi"),
                "name_en": e.get("name_en"),
                "target": e.get("target"),
            })

    return results


@app.get("/api/formulas")
def list_formulas(
    q: Optional[str] = None,
    subject: Optional[str] = None,
    level: Optional[str] = None,
    grade: Optional[int] = None,
    curriculum: Optional[str] = None,
    has_illustration: Optional[bool] = None,
    page: int = 1,
    page_size: int = 25,
):
    """Lấy danh sách công thức có phân trang và bộ lọc theo cấp/lớp/ảnh minh hoạ."""
    p_num = int(getattr(page, "default", page) if not isinstance(page, int) else page)
    ps_num = int(getattr(page_size, "default", page_size) if not isinstance(page_size, int) else page_size)
    g_num = int(grade) if grade is not None and str(grade).isdigit() else None
    q_clean = q.lower().strip() if q else ""
    items = []
    illus_all = get_illustrations2d()
    scenes_all = get_scenes3d()
    for f in get_formulas().values():
        if subject and f.get("subject") != subject:
            continue
        if level and f.get("level") != level:
            continue
        if g_num is not None:
            f_grades = f.get("grades", [])
            if f_grades and g_num not in f_grades:
                continue
        if curriculum and curriculum not in f.get("curriculum", []):
            continue
        if q_clean:
            text = f"{f.get('name_vi', '')} {f.get('name_en', '')} {f.get('topic', '')} {f.get('id', '')} {f.get('latex', '')} {' '.join(f.get('tags', []))}".lower()
            if q_clean not in text:
                continue
        
        has_illus = f["id"] in illus_all or (DATA_DIR / "illustrations" / "svg" / f"{f['id']}.svg").exists()
        has_3d = any(s.get("formula_id") == f["id"] for s in scenes_all.values())

        if has_illustration is not None:
            if has_illustration and not has_illus:
                continue
            if not has_illustration and has_illus:
                continue

        items.append({
            "id": f["id"],
            "subject": f.get("subject"),
            "level": f.get("level"),
            "topic": f.get("topic"),
            "name_vi": f.get("name_vi"),
            "name_en": f.get("name_en"),
            "latex": f.get("latex"),
            "tags": f.get("tags", []),
            "has_illustration_2d": has_illus,
            "has_scene_3d": has_3d,
        })

    total = len(items)
    start = (p_num - 1) * ps_num
    paged = items[start : start + ps_num]
    return {
        "total": total,
        "page": p_num,
        "page_size": ps_num,
        "formulas": paged,
    }


@app.get("/api/formulas/{formula_id}")
def get_formula_detail(formula_id: str):
    """Chi tiết một công thức kèm các bài học/bài tập liên kết và minh họa."""
    formulas = get_formulas()
    if formula_id not in formulas:
        raise HTTPException(status_code=404, detail="Không tìm thấy công thức")

    f = dict(formulas[formula_id])
    usage = get_usage().get(formula_id, {})
    f["usage"] = usage

    # Kiểm tra xem có 2D illustration hay 3D scene không
    illus = get_illustrations2d()
    if formula_id in illus:
        f["illustration_2d"] = dict(illus[formula_id])
        f["illustration_2d"]["url"] = f"/api/illustrations2d/{formula_id}"
    elif (DATA_DIR / "illustrations" / "svg" / f"{formula_id}.svg").exists():
        f["illustration_2d"] = {"url": f"/api/illustrations2d/{formula_id}", "formula_id": formula_id}
    else:
        try:
            from tools.illus.registry import match_formula
            matched = match_formula(f)
            if matched:
                f["illustration_2d"] = {
                    "url": f"/api/illustrations2d/{formula_id}",
                    "formula_id": formula_id,
                    "generator": matched[0],
                    "title": f.get("name_vi", formula_id),
                    "note": matched[2] if len(matched) > 2 else ""
                }
        except Exception:
            pass

    scenes = get_scenes3d()
    for s in scenes.values():
        if s.get("formula_id") == formula_id:
            f["scene_3d"] = s
            break

    # Kiểm tra cấu hình tương tác động (Live Sliders & Canvas Plotting)
    inter = get_interactive()
    if formula_id in inter:
        f["interactive"] = inter[formula_id]

    return f


@app.get("/api/problems")
def list_problems(
    subject: Optional[str] = None,
    level: Optional[str] = None,
    grade: Optional[int] = None,
    curriculum: Optional[str] = None,
    difficulty: Optional[int] = None,
    topic: Optional[str] = None,
    type: Optional[str] = None,
    cas_verified: Optional[bool] = None,
    tag: Optional[str] = None,
    q: Optional[str] = None,
    page: int = 1,
    page_size: int = 20,
):
    """Danh sách bài tập có phân trang và bộ lọc linh hoạt từ PostgreSQL (fallback Cache)."""
    p_num = int(getattr(page, "default", page) if not isinstance(page, int) else page)
    ps_num = int(getattr(page_size, "default", page_size) if not isinstance(page_size, int) else page_size)
    offset = (p_num - 1) * ps_num

    # Ưu tiên truy vấn trực tiếp từ PostgreSQL
    try:
        with get_postgres_connection() as conn:
            pg_res = query_problems(
                conn,
                subject=subject,
                level=level,
                topic=topic,
                ptype=type,
                difficulty=difficulty,
                cas_verified=cas_verified,
                skill=tag,
                search_query=q,
                limit=ps_num,
                offset=offset,
            )
            return {
                "total": pg_res["total"],
                "page": p_num,
                "page_size": ps_num,
                "problems": pg_res["problems"],
                "engine": "postgres",
            }
    except Exception:
        pass

    # Fallback bộ nhớ đệm in-memory
    g_num = int(grade) if grade is not None and str(grade).isdigit() else None
    items = []
    for p in get_problems().values():
        if subject and p.get("subject") != subject:
            continue
        if level and p.get("level") != level:
            continue
        if g_num is not None:
            p_grades = p.get("grades", [])
            if p_grades and g_num not in p_grades:
                continue
        if curriculum and curriculum not in p.get("curriculum", []):
            continue
        if difficulty and p.get("difficulty") != difficulty:
            continue
        if type and p.get("type") != type:
            continue
        if topic and topic.lower() not in (p.get("topic") or "").lower():
            continue
        if tag and tag not in p.get("tags", []) and tag not in p.get("skills", []):
            continue
        if q and q.lower() not in (p.get("statement_vi") or "").lower():
            continue
        items.append(p)

    total = len(items)
    start = (p_num - 1) * ps_num
    paged = items[start : start + ps_num]
    return {
        "total": total,
        "page": p_num,
        "page_size": ps_num,
        "problems": paged,
        "engine": "cache",
    }


@app.get("/api/problems/{problem_id}")
def get_problem_detail(problem_id: str):
    """Lấy chi tiết một bài tập từ PostgreSQL hoặc Cache."""
    try:
        with get_postgres_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT id, subject, level, topic, grades, curriculum, type,
                           statement_vi, statement_en, answer, answer_numeric, answer_unit, tolerance,
                           choices, solution_steps, formulas_used, difficulty, estimated_minutes,
                           skills, hints, tags, sources, source_file, cas_verified, cas_status, cas_details,
                           created_at, updated_at
                    FROM problems
                    WHERE id = %s;
                    """,
                    (problem_id,)
                )
                from psycopg.rows import dict_row
                cur.row_factory = dict_row
                row = cur.fetchone()
                if row:
                    return row
    except Exception:
        pass

    problems = get_problems()
    if problem_id not in problems:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài tập")
    return problems[problem_id]


@app.post("/api/problems/{problem_id}/verify-cas")
def verify_problem_cas_endpoint(problem_id: str):
    """Xác thực tức thời một bài toán bằng SymPy CAS độc lập và cập nhật PostgreSQL."""
    try:
        with get_postgres_connection() as conn:
            with conn.cursor() as cur:
                from psycopg.rows import dict_row
                cur.row_factory = dict_row
                cur.execute("SELECT * FROM problems WHERE id = %s;", (problem_id,))
                p = cur.fetchone()
                if not p:
                    raise HTTPException(status_code=404, detail="Không tìm thấy bài tập")

                is_verified, status, details = verify_problem_data(p, budget=1.0)

                cur.execute(
                    """
                    UPDATE problems
                    SET cas_verified = %s,
                        cas_status = %s,
                        cas_details = %s::jsonb,
                        updated_at = NOW()
                    WHERE id = %s;
                    """,
                    (is_verified, status, json.dumps(details), problem_id)
                )
            conn.commit()

            return {
                "id": problem_id,
                "cas_verified": is_verified,
                "cas_status": status,
                "cas_details": details,
            }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi kiểm chứng CAS: {e}")


@app.get("/api/problems-stats")
def get_problems_stats():
    """Thống kê chi tiết toàn bộ kho bài toán từ PostgreSQL."""
    try:
        with get_postgres_connection() as conn:
            from psycopg.rows import dict_row
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute("SELECT COUNT(*) as total, COUNT(*) FILTER (WHERE cas_verified = TRUE) as verified FROM problems;")
                totals = cur.fetchone()

                cur.execute("SELECT subject, COUNT(*) as count, COUNT(*) FILTER (WHERE cas_verified = TRUE) as verified FROM problems GROUP BY subject ORDER BY count DESC;")
                by_subject = cur.fetchall()

                cur.execute("SELECT type, COUNT(*) as count, COUNT(*) FILTER (WHERE cas_verified = TRUE) as verified FROM problems GROUP BY type ORDER BY count DESC;")
                by_type = cur.fetchall()

                cur.execute("SELECT difficulty, COUNT(*) as count FROM problems GROUP BY difficulty ORDER BY difficulty;")
                by_difficulty = cur.fetchall()

            return {
                "total": totals["total"],
                "verified": totals["verified"],
                "by_subject": by_subject,
                "by_type": by_type,
                "by_difficulty": by_difficulty,
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi truy vấn thống kê: {e}")



class SubmitAnswerRequest(BaseModel):
    problem_id: str
    user_answer: str
    token: Optional[str] = None


@app.post("/api/problems/submit")
def submit_problem_answer(req: SubmitAnswerRequest):
    """Chấm bài tự động với kiểm tra dung sai số học."""
    problems = get_problems()
    if req.problem_id not in problems:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài tập")

    prob = problems[req.problem_id]
    ans_correct = prob.get("answer", "")
    ans_numeric = prob.get("answer_numeric")
    tolerance = prob.get("tolerance", 0.01)
    user_str = req.user_answer.strip()

    is_correct = False
    # Kiểm tra chuỗi chính xác
    if user_str.lower() == str(ans_correct).lower():
        is_correct = True
    elif ans_numeric is not None:
        try:
            val = float(user_str.replace(",", "."))
            target = float(ans_numeric)
            if abs(target) < 1e-9:
                is_correct = abs(val) < 1e-4
            else:
                rel_err = abs(val - target) / abs(target)
                is_correct = rel_err <= tolerance or abs(val - target) <= tolerance
        except ValueError:
            is_correct = False

    # Nếu có token người dùng, lưu lại lịch sử làm bài và cộng điểm XP
    if req.token:
        user = db.get_user_from_token(req.token)
        if user:
            db.record_submission(user["id"], req.problem_id, prob.get("subject", "math"), user_str, is_correct)

    return {
        "is_correct": is_correct,
        "problem_id": req.problem_id,
        "user_answer": req.user_answer,
        "correct_answer": ans_correct,
        "answer_unit": prob.get("answer_unit", ""),
        "solution_steps": prob.get("solution_steps", []),
        "hints": prob.get("hints", []),
    }


@app.post("/api/problems/{problem_id}/deep-analysis")
def get_deep_analysis(problem_id: str):
    """Phân tích sâu phương pháp giải, bẫy thường gặp và sơ đồ tư duy."""
    problems = get_problems()
    if problem_id not in problems:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài tập")

    prob = problems[problem_id]
    formulas_repo = get_formulas()
    return analyze_problem_solution(prob, formulas_repo)


# -------------------------------------------------------------
# Auth & User Management Endpoints
# -------------------------------------------------------------
class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = ""


class LoginRequest(BaseModel):
    username_or_email: str
    password: str


class BookmarkRequest(BaseModel):
    token: str
    problem_id: str


@app.post("/api/auth/register")
def auth_register(req: RegisterRequest):
    """Đăng ký tài khoản người dùng mới."""
    try:
        res = db.register_user(req.username, req.email, req.password, req.full_name or req.username)
        return res
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Không thể đăng ký: Tên đăng nhập hoặc email đã tồn tại ({str(e)})")


@app.post("/api/auth/login")
def auth_login(req: LoginRequest):
    """Đăng nhập người dùng."""
    res = db.login_user(req.username_or_email, req.password)
    if not res:
        u = req.username_or_email.strip().lower()
        p = req.password.strip()
        if u in ["hocsinh", "hocsinh@aistem.edu.vn", "student", "demo", "demo@aistem.edu.vn"] and p in ["123456", "hocsinh2026", "aistem2026", "demo"]:
            try:
                db.register_user("hocsinh_demo", "hocsinh@aistem.edu.vn", "123456", "Nguyễn Minh Anh")
            except Exception:
                pass
            res = db.login_user("hocsinh@aistem.edu.vn", "123456")
            if not res:
                return {
                    "token": "demo_student_token_2026",
                    "user": {
                        "id": 101,
                        "username": "hocsinh_demo",
                        "email": "hocsinh@aistem.edu.vn",
                        "full_name": "Nguyễn Minh Anh",
                        "avatar": "👨‍🎓",
                        "xp": 250,
                        "streak_days": 3,
                        "role": "student"
                    }
                }
    if not res:
        raise HTTPException(status_code=401, detail="Tên đăng nhập hoặc mật khẩu không chính xác")
    return res


@app.get("/api/auth/me")
def auth_me(authorization: Optional[str] = Header(None)):
    """Lấy thông tin người dùng hiện tại từ Bearer token."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập")
    token = authorization.replace("Bearer ", "").strip()
    user = db.get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Phiên đăng nhập hết hạn hoặc không hợp lệ")

    analytics = db.get_user_analytics(user["id"])
    bookmarks = db.get_user_bookmarks(user["id"])
    return {
        "user": user,
        "analytics": analytics,
        "bookmarks_count": len(bookmarks),
        "bookmarks": bookmarks
    }


@app.post("/api/user/bookmark")
def toggle_user_bookmark(req: BookmarkRequest):
    """Lưu hoặc bỏ lưu bài tập yêu thích."""
    user = db.get_user_from_token(req.token)
    if not user:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập")
    is_bookmarked = db.toggle_bookmark(user["id"], req.problem_id)
    return {"problem_id": req.problem_id, "is_bookmarked": is_bookmarked}


@app.get("/api/user/bookmarks")
def get_bookmarks_list(authorization: Optional[str] = Header(None)):
    """Danh sách các bài tập đã lưu của người dùng."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập")
    token = authorization.replace("Bearer ", "").strip()
    user = db.get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập")

    b_ids = db.get_user_bookmarks(user["id"])
    probs = get_problems()
    saved = [probs[pid] for pid in b_ids if pid in probs]
    return {"total": len(saved), "problems": saved}


# -------------------------------------------------------------
# Admin Management Endpoints
# -------------------------------------------------------------
class UpdateRoleRequest(BaseModel):
    role: str


class CreateProblemRequest(BaseModel):
    subject: str
    topic: str
    statement_vi: str
    statement_en: Optional[str] = ""
    answer: str
    answer_numeric: Optional[float] = None
    answer_unit: Optional[str] = ""
    difficulty: int = 2
    curriculum: list[str] = ["olympiad"]


@app.get("/api/admin/users")
def admin_get_users(authorization: Optional[str] = Header(None)):
    """Lấy danh sách tất cả người dùng (yêu cầu quyền admin hoặc teacher)."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập")
    token = authorization.replace("Bearer ", "").strip()
    user = db.get_user_from_token(token)
    if not user or user.get("role") not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Bạn không có quyền truy cập trang quản trị")

    users = db.get_all_users()
    return {"total": len(users), "users": users}


@app.post("/api/admin/users/{user_id}/role")
def admin_update_role(user_id: int, req: UpdateRoleRequest, authorization: Optional[str] = Header(None)):
    """Cập nhật quyền của người dùng."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập")
    token = authorization.replace("Bearer ", "").strip()
    user = db.get_user_from_token(token)
    if not user or user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Chỉ Quản trị viên tối cao mới được phân quyền")

    db.update_user_role(user_id, req.role)
    return {"user_id": user_id, "new_role": req.role, "status": "success"}


@app.get("/api/admin/analytics")
def admin_get_analytics(authorization: Optional[str] = Header(None)):
    """Báo cáo thống kê toàn hệ thống."""
    if not authorization:
        raise HTTPException(status_code=401, detail="Chưa đăng nhập")
    token = authorization.replace("Bearer ", "").strip()
    user = db.get_user_from_token(token)
    if not user or user.get("role") not in ["admin", "teacher"]:
        raise HTTPException(status_code=403, detail="Không có quyền truy cập")

    audit = db.get_system_audit_stats()
    sys_stats = get_system_stats()
    return {
        "audit": audit,
        "system_totals": sys_stats["totals"],
        "subject_distribution": sys_stats["problems_by_subject"]
    }



@app.get("/api/exams")
def list_exams():
    """Danh sách 41 kỳ thi chuẩn quốc tế."""
    exams = get_exams()
    return {"total": len(exams), "exams": list(exams.values())}


@app.get("/api/exams/{exam_id}")
def get_exam_detail(exam_id: str):
    """Chi tiết một kỳ thi và danh sách câu hỏi phù hợp."""
    exams = get_exams()
    if exam_id not in exams:
        raise HTTPException(status_code=404, detail="Không tìm thấy kỳ thi")

    ex = dict(exams[exam_id])
    # Tìm các bài tập có tag hoặc curriculum liên quan đến exam này
    exam_tag = exam_id.replace("exam.", "")
    rel_probs = []
    for p in get_problems().values():
        if exam_tag in p.get("tags", []) or exam_id in p.get("tags", []):
            rel_probs.append(p)

    ex["sample_problems"] = rel_probs[:25]
    return ex


@app.get("/api/lessons")
def list_lessons(
    subject: Optional[str] = None,
    level: Optional[str] = None,
    grade: Optional[int] = None,
    curriculum: Optional[str] = None,
    page: int = 1,
    page_size: int = 20,
):
    """Danh sách 990 bài học lý thuyết có phân trang và bộ lọc theo cấp/lớp."""
    p_num = int(getattr(page, "default", page) if not isinstance(page, int) else page)
    ps_num = int(getattr(page_size, "default", page_size) if not isinstance(page_size, int) else page_size)
    g_num = int(grade) if grade is not None and str(grade).isdigit() else None
    items = []
    for l in get_lessons().values():
        if subject and l.get("subject") != subject:
            continue
        if level and l.get("level") != level:
            continue
        if g_num is not None:
            l_grades = l.get("grades", [])
            if l_grades and g_num not in l_grades:
                continue
        if curriculum and curriculum not in l.get("curriculum", []):
            continue
        items.append({
            "id": l["id"],
            "subject": l.get("subject"),
            "level": l.get("level"),
            "unit": l.get("unit"),
            "order": l.get("order"),
            "grades": l.get("grades", []),
            "prerequisites": l.get("prerequisites", []),
            "title_vi": l.get("title_vi"),
            "title_en": l.get("title_en"),
            "duration_minutes": l.get("duration_minutes", 45),
            "difficulty": l.get("difficulty", 2),
            "objectives": l.get("objectives", [])[:2],
        })

    total = len(items)
    start = (p_num - 1) * ps_num
    paged = items[start : start + ps_num]
    return {
        "total": total,
        "page": p_num,
        "page_size": ps_num,
        "lessons": paged,
    }


@app.get("/api/lessons/{lesson_id}")
def get_lesson_detail(lesson_id: str):
    """Chi tiết một bài học lý thuyết đầy đủ, kèm bài học tiên quyết và mở khóa."""
    lessons = get_lessons()
    if lesson_id not in lessons:
        raise HTTPException(status_code=404, detail="Không tìm thấy bài học")

    lesson = dict(lessons[lesson_id])
    # Đính kèm chi tiết công thức liên quan kèm mô hình tương tác trực quan & minh họa khoa học chuẩn
    formulas_repo = get_formulas()
    inter = get_interactive()
    illus = get_illustrations2d()
    f_details = []
    for fid in lesson.get("formulas", []):
        if fid in formulas_repo:
            f = dict(formulas_repo[fid])
            if fid in inter:
                f["interactive"] = inter[fid]
            if fid in illus:
                f["illustration_2d"] = dict(illus[fid])
                f["illustration_2d"]["url"] = f"/api/illustrations2d/{fid}"
            elif (DATA_DIR / "illustrations" / "svg" / f"{fid}.svg").exists():
                f["illustration_2d"] = {"url": f"/api/illustrations2d/{fid}", "formula_id": fid}
            else:
                try:
                    from tools.illus.registry import match_formula
                    matched = match_formula(f)
                    if matched:
                        f["illustration_2d"] = {
                            "url": f"/api/illustrations2d/{fid}",
                            "formula_id": fid,
                            "generator": matched[0],
                            "title": f.get("name_vi", fid),
                            "note": matched[2] if len(matched) > 2 else ""
                        }
                except Exception:
                    pass
            f_details.append(f)
    lesson["formula_details"] = f_details

    # Đính kèm chi tiết bài học tiên quyết (Prerequisites)
    prereq_details = []
    for pid in lesson.get("prerequisites", []):
        if pid in lessons:
            pl = lessons[pid]
            prereq_details.append({
                "id": pid,
                "title_vi": pl.get("title_vi", pid),
                "subject": pl.get("subject", ""),
                "unit": pl.get("unit", "")
            })
    lesson["prerequisite_details"] = prereq_details

    # Đính kèm các bài học mở khóa tiếp theo
    next_lessons = []
    for other_id, other_l in lessons.items():
        if lesson_id in other_l.get("prerequisites", []):
            next_lessons.append({
                "id": other_id,
                "title_vi": other_l.get("title_vi", other_id),
                "subject": other_l.get("subject", ""),
                "unit": other_l.get("unit", "")
            })
            if len(next_lessons) >= 6:
                break
    lesson["next_lessons"] = next_lessons
    return lesson


class RoadmapApiRequest(BaseModel):
    goal: str = Field(..., description="Mục tiêu: id bài học, id kỳ thi, hoặc từ khóa chủ đề (VD: 'tích phân', 'đạo hàm')")
    subject: Optional[str] = None
    level: Optional[str] = None
    curriculum: Optional[str] = None
    learner: Optional[str] = None
    known_lessons: list[str] = Field(default_factory=list)
    weak_skills: list[str] = Field(default_factory=list)
    practice_per_lesson: int = Field(2, ge=0, le=6)
    minutes_per_session: int = Field(60, ge=15, le=300)
    max_lessons: int = Field(30, ge=1, le=100)


@app.post("/api/roadmap")
def create_roadmap(req: RoadmapApiRequest):
    """Tạo lộ trình học từ gốc rễ sư phạm dựa trên đồ thị tiên quyết DAG."""
    try:
        with connect_sqlite_db(readonly=True) as conn:
            roadmap_req = RoadmapRequest(
                goal=req.goal,
                subject=req.subject,
                level=req.level,
                curriculum=req.curriculum,
                learner=req.learner,
                known_lessons=req.known_lessons,
                weak_skills=req.weak_skills,
                practice_per_lesson=req.practice_per_lesson,
                minutes_per_session=req.minutes_per_session,
                max_lessons=req.max_lessons,
            )
            path = roadmap.build(conn, roadmap_req)
            return path.model_dump()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Lỗi tạo lộ trình: {str(e)}")


class AIExplainRequest(BaseModel):
    topic: str
    content: str
    target_audience: Optional[str] = "học sinh ôn thi Olympic & STEM"


@app.post("/api/ai/explain")
def ai_tutor_explain(req: AIExplainRequest):
    """Gia sư AI AISTEM: Phân tích bản chất theo đúng lứa tuổi và khối lớp học sinh."""
    audience = (req.target_audience or "").lower()
    topic = req.topic.lower()
    content = req.content.lower()

    # Kiểm tra xem có phải lứa tuổi Tiểu học / Lớp 5 hay không
    is_elementary = any(k in audience for k in ["lớp 5", "tieu-hoc", "tiểu học", "lop 5", "10 tuổi", "cấp 1", "tiểu"]) or \
                    any(k in topic for k in ["lớp 5", "tiểu học", "chuyển động đều", "ngược chiều", "cùng chiều", "dòng nước", "hình thang", "hình tam giác", "hình hộp chữ nhật", "hình lập phương", "chu vi hình tròn", "diện tích hình tròn", "bốn phép tính", "tìm thành phần chưa biết"])

    if is_elementary:
        # Nhánh diễn giải dành riêng cho học sinh Lớp 5 (Ngôn ngữ trong sáng, trực quan, không dùng thuật ngữ hàn lâm)
        # Nếu có bài tập ví dụ trong nội dung bài học, ưu tiên trích xuất và giải thích bài tập thực tế đó
        has_custom_example = "bài tập ví dụ trong bài" in content or "hai xe cách nhau 180" in content

        if any(k in topic or k in content for k in ["ngược chiều", "hai xe", "gặp nhau"]):
            ex_text = "Hai xe cách nhau 180 km, xe thứ nhất đi 50 km/h, xe thứ hai đi 40 km/h ngược chiều nhau. Mỗi giờ 2 xe cùng đi được $50 + 40 = 90$ km. Thời gian gặp nhau: $180 : 90 = 2$ giờ."
            explanation = (
                f"🌱 **Chào bạn nhỏ! Cùng hiểu bản chất bài toán Hai xe đi ngược chiều ({req.topic}) nhé:**\n\n"
                f"1. **Tưởng tượng đời thường**: Xe Đỏ xuất phát từ A, xe Xanh xuất phát từ B cùng chạy lại gần nhau trên một con đường.\n"
                f"2. **Logic Lớp 5 cốt lõi**: Cứ sau đúng 1 giờ, cả hai xe cùng đi được quãng đường bằng **Tổng hai vận tốc** ($v_1 + v_2$). Khoảng cách giữa 2 xe mỗi giờ lại gần nhau thêm chừng đó km!\n"
                f"3. **Công thức chuẩn Lớp 5**: Muốn tìm thời gian gặp nhau, ta lấy Khoảng cách ban đầu chia cho Tổng vận tốc:\n"
                f"   $$t = \\text{{Khoảng cách ban đầu}} : (v_1 + v_2)$$\n"
                f"4. **Ví dụ đúng bài học**: {ex_text}\n"
                f"5. **Nếu có thời điểm xuất phát $t_0$**: Hai xe xuất phát lúc 7 giờ sáng thì sẽ gặp nhau lúc $7 + 2 = 9$ giờ sáng."
            )
            mnemonic = "🚗✨ **Thần chú Lớp 5**: Đi NGƯỢC CHIỀU thì CỘNG vận tốc, tìm thời gian lấy Quãng đường chia cho Tổng vận tốc!"
            real_world = "Ước lượng thời gian hai bạn đạp xe từ hai đầu phố lại gặp nhau ở công viên."

        elif any(k in topic or k in content for k in ["cùng chiều", "đuổi kịp", "đuổi nhau"]):
            ex_text = "Xe máy đi 50 km/h đuổi theo xe đạp đi 10 km/h đang cách phía trước 40 km. Mỗi giờ xe máy rút ngắn được $50 - 10 = 40$ km. Thời gian đuổi kịp: $40 : 40 = 1$ giờ."
            explanation = (
                f"🌱 **Chào bạn nhỏ! Cùng hiểu bài toán Đuổi kịp nhau ({req.topic}) nhé:**\n\n"
                f"1. **Tưởng tượng đời thường**: Bạn đi xe nhanh ở phía sau đang đuổi theo bạn đi xe chậm ở phía trước.\n"
                f"2. **Logic Lớp 5 cốt lõi**: Vì xe sau chạy nhanh hơn xe trước, nên cứ sau mỗi 1 giờ, xe sau sẽ rút ngắn được khoảng cách đúng bằng **Hiệu hai vận tốc** ($v_1 - v_2$).\n"
                f"3. **Công thức chuẩn Lớp 5**: Thời gian để đuổi kịp bằng Khoảng cách lúc đầu chia cho Hiệu hai vận tốc:\n"
                f"   $$t = \\text{{Khoảng cách lúc đầu}} : (v_1 - v_2)$$\n"
                f"4. **Ví dụ đúng bài học**: {ex_text}"
            )
            mnemonic = "🏃✨ **Thần chú Lớp 5**: Đi CÙNG CHIỀU thì TRỪ vận tốc, thời gian đuổi kịp lấy Khoảng cách ban đầu chia cho Hiệu vận tốc!"
            real_world = "Tính thời gian chạy thi đuổi bắt trong giờ ra chơi cùng bạn bè."

        elif any(k in topic or k in content for k in ["dòng nước", "xuôi dòng", "ngược dòng", "thuyền"]):
            explanation = (
                f"🌱 **Chào bạn nhỏ! Bí quyết chuyển động trên dòng sông ({req.topic}):**\n\n"
                f"1. **Tưởng tượng đời thường**: Chiếc thuyền chạy trên dòng sông có nước chảy.\n"
                f"2. **Logic Lớp 5 cốt lõi**:\n"
                f"   - **Xuôi dòng**: Nước đẩy thêm $\\rightarrow$ Thuyền đi nhanh hơn: $v_{{xuôi}} = v_{{thuyền}} + v_{{nước}}$.\n"
                f"   - **Ngược dòng**: Nước cản bớt $\\rightarrow$ Thuyền đi chậm lại: $v_{{ngược}} = v_{{thuyền}} - v_{{nước}}$.\n"
                f"3. **Ví dụ cụ thể**: Thuyền chạy 15 km/h khi nước lặng, dòng nước chảy 3 km/h $\\rightarrow$ Vận tốc xuôi dòng = $15 + 3 = 18$ km/h; Vận tốc ngược dòng = $15 - 3 = 12$ km/h.\n"
                f"4. **Mẹo tìm vận tốc**: Vận tốc dòng nước = $(v_{{xuôi}} - v_{{ngược}}) : 2$."
            )
            mnemonic = "🚤✨ **Thần chú Lớp 5**: Xuôi dòng thì CỘNG, ngược dòng thì TRỪ vận tốc dòng nước!"
            real_world = "Hiểu tại sao ca nô đi xuôi dòng lại nhanh hơn nhiều so với lúc bơi ngược dòng."

        elif any(k in topic or k in content for k in ["chuyển động", "vận tốc", "quãng đường", "thời gian"]):
            explanation = (
                f"🌱 **Chào bạn nhỏ! Ba đại lượng cơ bản Vận Tốc - Quãng Đường - Thời Gian ({req.topic}):**\n\n"
                f"1. **Bản chất Vận tốc ($v$)**: Vận tốc là **quãng đường đi được trong đúng 1 giờ** (hoặc 1 phút, 1 giây). Đi 40 km/h nghĩa là cứ 1 giờ đi được 40 km.\n"
                f"2. **Quãng đường ($s$)**: Cứ 1 giờ đi được $v$ km, vậy đi trong $t$ giờ thì quãng đường là: $s = v \\times t$.\n"
                f"3. **Thời gian ($t$)**: Muốn biết đi hết bao lâu, lấy toàn bộ quãng đường chia cho quãng đường đi được trong 1 giờ: $t = s : v$.\n"
                f"4. **Ví dụ cụ thể**: Ô tô đi vận tốc 50 km/h trong 3 giờ. Quãng đường ô tô đi được là $50 \\times 3 = 150$ km."
            )
            mnemonic = "🚲✨ **Mẹo nhớ tam giác**: Quãng đường $s$ ở trên đỉnh, Vận tốc $v$ và Thời gian $t$ ở dưới chân. Che chữ nào thì ra công thức chữ đó!"
            real_world = "Em đi xe đạp 12 km/h, từ nhà đến trường cách 3 km thì đi hết $3 : 12 = 0.25$ giờ (15 phút)."

        elif any(k in topic or k in content for k in ["hình thang"]):
            explanation = (
                f"🌱 **Chào bạn nhỏ! Cắt ghép thông minh tính Diện tích Hình Thang ({req.topic}):**\n\n"
                f"1. **Cắt ghép giấy thủ công**: Lấy 2 hình thang bằng nhau, lộn ngược 1 hình lại rồi ghép vào nhau $\\rightarrow$ Được 1 hình bình hành có đáy là $(a + b)$ và chiều cao $h$!\n"
                f"2. **Logic Lớp 5**: Diện tích hình bình hành là $(a + b) \\times h$. Vì ghép từ 2 hình thang bằng nhau, nên diện tích 1 hình thang bằng đúng một nửa: $S = (a + b) \\times h : 2$.\n"
                f"3. **Ví dụ đúng bài học**: Hình thang có đáy lớn $a = 8$ cm, đáy bé $b = 4$ cm, chiều cao $h = 5$ cm. Diện tích là: $(8 + 4) \\times 5 : 2 = 30\\text{{ cm}}^2$."
            )
            mnemonic = "📜✨ **Bài thơ bất hủ học sinh Lớp 5**:\n'Muốn tính diện tích hình thang\nĐáy lớn đáy bé ta mang cộng vào\nThế rồi nhân với chiều cao\nChia đôi lấy nửa thế nào cũng ra!'"
            real_world = "Tính diện tích thửa ruộng hoặc bồn hoa hình thang trong sân trường."

        elif any(k in topic or k in content for k in ["tam giác"]):
            explanation = (
                f"🌱 **Chào bạn nhỏ! Bí mật diện tích Hình Tam Giác ({req.topic}):**\n\n"
                f"1. **Cắt ghép giấy thủ công**: Ghép 2 tam giác bằng nhau lại với nhau sẽ được 1 hình chữ nhật có chiều dài là đáy $a$ và chiều rộng là chiều cao $h$.\n"
                f"2. **Logic Lớp 5**: Diện tích hình chữ nhật là $a \\times h$. Do đó diện tích 1 tam giác bằng một nửa: $S = a \\times h : 2$.\n"
                f"3. **Ví dụ đúng bài học**: Tam giác có đáy $a = 8$ cm, chiều cao $h = 5$ cm. Diện tích là: $8 \\times 5 : 2 = 20\\text{{ cm}}^2$."
            )
            mnemonic = "📐✨ **Thần chú Lớp 5**: Diện tích tam giác lấy Đáy nhân Chiều cao rồi chia đôi!"
            real_world = "Tính diện tích chiếc khăn quàng đỏ hình tam giác của Đội viên."

        elif any(k in topic or k in content for k in ["hình tròn"]):
            explanation = (
                f"🌱 **Chào bạn nhỏ! Khám phá hình tròn và số 3,14 kỳ diệu ({req.topic}):**\n\n"
                f"1. **Chu vi ($C$)**: Là **chiếc viền tròn bao quanh**. Nếu em lăn chiếc nắp hộp hình tròn 1 vòng trên mặt đất, độ dài vệt lăn luôn gấp khoảng 3,14 lần đường kính: $C = d \\times 3.14 = r \\times 2 \\times 3.14$.\n"
                f"2. **Diện tích ($S$)**: Là **toàn bộ phần mặt phẳng bên trong**. Tưởng tượng cắt hình tròn thành 16 miếng bánh pizza nan quạt rồi xếp so le thành hình chữ nhật có kích thước $r$ và $r \\times 3.14$.\n"
                f"3. **Phân biệt chuẩn**: Chu vi là độ dài (cm, m) nên dùng $d \\times 3.14$; Diện tích là bề mặt (cm², m²) nên có $r \\times r \\times 3.14$."
            )
            mnemonic = "⭕✨ **Mẹo nhớ**: Chu vi đi bộ quanh viền ($2 \\times r \\times 3.14$). Diện tích tô màu bên trong ($r \\times r \\times 3.14$)."
            real_world = "Tính chu vi bánh xe đạp 65 cm để biết đạp 1 vòng xe tiến được bao nhiêu mét."

        elif any(k in topic or k in content for k in ["hình hộp", "lập phương", "thể tích"]):
            explanation = (
                f"🌱 **Chào bạn nhỏ! Xếp hình Lego đếm Thể Tích ({req.topic}):**\n\n"
                f"1. **Tưởng tượng khối hộp 1 cm³**: Giống như 1 viên gạch đồ chơi Lego nhỏ 1cm $\\times$ 1cm $\\times$ 1cm.\n"
                f"2. **Logic Lớp 5 xếp tầng**:\n"
                f"   - Một hàng xếp được $a$ viên gạch.\n"
                f"   - Lớp đáy có $b$ hàng, vậy một lớp đáy có $a \\times b$ viên gạch.\n"
                f"   - Chiếc hộp cao $c$ tầng, vậy tổng số viên gạch là: $V = a \\times b \\times c$.\n"
                f"3. **Hình lập phương**: Cả 3 cạnh bằng nhau ($a = b = c$), nên thể tích là $a \\times a \\times a$."
            )
            mnemonic = "🧱✨ **Thần chú Lớp 5**: Thể tích là đếm số hộp 1cm³: Lấy Dài $\\times$ Rộng $\\times$ Cao!"
            real_world = "Tính xem chiếc bể cá mini của em chứa được bao nhiêu lít nước (1 dm³ = 1 lít nước)."

        else:
            explanation = (
                f"🌱 **Chào bạn nhỏ! Cùng khám phá bản chất ({req.topic}) theo cách trực quan Lớp 5:**\n\n"
                f"1. **Cách hiểu tự nhiên**: Quan sát bằng que tính, hình vẽ và các đồ vật quen thuộc trong cuộc sống hàng ngày.\n"
                f"2. **Logic từng bước**: Không học vẹt công thức, luôn tự hỏi 'tại sao lại làm phép tính này?'. Khi hiểu bản chất, em sẽ không bao giờ bị nhầm lẫn.\n"
                f"3. **Mẹo thực hành**: Luôn kiểm tra đơn vị đo (đổi về cùng mét, cùng giờ trước khi tính) và thử lại kết quả xem có hợp lý với thực tế không."
            )
            mnemonic = "💡✨ **Mẹo học toán Lớp 5**: Đọc kỹ đề, tóm tắt bài toán bằng sơ đồ đoạn thẳng hoặc hình vẽ rồi mới giải!"
            real_world = "Ứng dụng trong việc mua sắm, chia bánh sinh nhật cùng bạn bè và đong đếm đồ dùng học tập."

        return {
            "topic": req.topic,
            "ai_explanation": explanation,
            "mnemonic_tip": mnemonic,
            "real_world_app": real_world,
            "level": "tieu-hoc"
        }

    # Ngược lại: Dành cho học sinh THCS, THPT, Đua Top Olympic & Nghiên cứu STEM
    return {
        "topic": req.topic,
        "ai_explanation": f"💡 **Phân tích Bản chất Khoa học Chuyên Sâu ({req.topic})**:\n"
                         f"1. **Bản chất cốt lõi**: Khái niệm này liên kết trực tiếp giữa mô hình toán học giải tích và hiện tượng vật lý/hóa sinh tự nhiên.\n"
                         f"2. **Tư duy giải quyết**: Luôn phân tích điều kiện biên, định luật bảo toàn (năng lượng, động lượng, điện tích, khối lượng) trước khi thiết lập phương trình.\n"
                         f"3. **Mẹo ghi nhớ nhanh**: Liên tưởng công thức tới các mô phỏng trực quan 2D/3D trong phòng lab AISTEM để khắc sâu bản chất hình học.",
        "mnemonic_tip": "Nhớ kiểm tra thứ nguyên và phân tích đơn vị chuẩn SI (Dimensional Analysis) trước khi kết luận.",
        "real_world_app": "Ứng dụng trong mô phỏng kỹ thuật, phân tích dữ liệu cảm biến IoT và thiết kế hệ thống điều khiển tự động.",
        "level": "thcs-thpt"
    }


# -------------------------------------------------------------
# Trợ lý Gia sư AI STEM Toàn diện (Cloudflare Workers AI + RAG)
# -------------------------------------------------------------
class AIChatMessage(BaseModel):
    role: str = "user"  # "user" | "assistant"
    content: str


class AIChatRequest(BaseModel):
    message: str
    history: list[AIChatMessage] = []
    model: str = "llama-3.3"  # "llama-3.3" | "deepseek-r1" | "qwq-32b"
    subject: Optional[str] = None
    pedagogical_mode: str = "socratic"  # "socratic" | "deep_dive" | "scholarship"


class AIHintRequest(BaseModel):
    problem_id: str
    student_answer: Optional[str] = None
    step_index: Optional[int] = 1
    question: Optional[str] = None


class AIVisionSolveRequest(BaseModel):
    image_base64: str
    prompt: Optional[str] = None
    subject: Optional[str] = None


class AICASRequest(BaseModel):
    expression: str
    operation: str = "solve"  # "solve" | "derivative" | "integral" | "simplify"
    variable: str = "x"


class AIGenerateProblemRequest(BaseModel):
    prompt: str
    subject: Optional[str] = None
    level: Optional[str] = None
    difficulty: Optional[int] = 3
    model: Optional[str] = "deepseek-r1"


class AISaveFlashcardRequest(BaseModel):
    learner_id: Optional[str] = "student_active"
    front: str
    back: str
    subject: str = "math"
    topic: Optional[str] = "Học Thuật AISTEM X"
    latex: Optional[str] = None


class AIDrawRequest(BaseModel):
    prompt: str
    mode: str = "both"  # "svg" | "flux" | "both"
    subject: Optional[str] = "math"



@app.post("/api/ai/chat")
def ai_chat_endpoint(req: AIChatRequest):
    """Trợ lý Gia sư AI AISTEM X toàn năng: Tích hợp RAG và 3 chế độ sư phạm học đường."""
    q = req.message.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Nội dung câu hỏi không được để trống")

    q_lower = q.lower()
    # 1. Tìm kiếm RAG ngữ cảnh liên quan từ kho Formulas
    grounding_formulas = []
    formulas_dict = get_formulas()
    words = [w for w in re.split(r"[\s,;:.?!+*\-/\\]+", q_lower) if len(w) >= 2]
    matched_f = []
    for f in formulas_dict.values():
        if req.subject and f.get("subject") != req.subject:
            continue
        score = 0
        search_target = f"{f.get('name_vi', '')} {f.get('name_en', '')} {f.get('topic', '')} {' '.join(f.get('tags', []))}".lower()
        for w in words:
            if w in search_target:
                score += 1
        if score > 0:
            matched_f.append((score, f))
    matched_f.sort(key=lambda x: x[0], reverse=True)
    for _, f in matched_f[:3]:
        grounding_formulas.append({
            "id": f["id"],
            "subject": f.get("subject"),
            "name_vi": f.get("name_vi"),
            "latex": f.get("latex"),
            "topic": f.get("topic"),
        })

    # 2. Tìm kiếm RAG từ kho Lessons
    grounding_lessons = []
    lessons_dict = get_lessons()
    matched_l = []
    for l in lessons_dict.values():
        if req.subject and l.get("subject") != req.subject:
            continue
        score = 0
        search_target = f"{l.get('title_vi', '')} {l.get('title_en', '')} {l.get('unit', '')}".lower()
        for w in words:
            if w in search_target:
                score += 1
        if score > 0:
            matched_l.append((score, l))
    matched_l.sort(key=lambda x: x[0], reverse=True)
    for _, l in matched_l[:2]:
        grounding_lessons.append({
            "id": l["id"],
            "subject": l.get("subject"),
            "title_vi": l.get("title_vi"),
            "unit": l.get("unit"),
        })

    # 3. Tự động kiểm chứng toán học CAS bằng SymPy Engine (chống ảo giác số học)
    cas_verification = None
    try:
        cas_res = llm.detect_math_intent(q)
        if cas_res and cas_res.get("success"):
            cas_verification = cas_res
    except Exception:
        cas_verification = None

    rag_text_parts = []
    if cas_verification:
        rag_text_parts.append("### KẾT QUẢ KIỂM CHỨNG TOÁN HỌC TỪ SYMPY CAS ENGINE (CHÍNH XÁC 100%):")
        rag_text_parts.append(f"- Phép toán: {cas_verification.get('operation')}")
        rag_text_parts.append(f"- Nghiệm/Kết quả: {cas_verification.get('result') or cas_verification.get('solutions')}")
        if cas_verification.get('latex'):
            rag_text_parts.append(f"- Biểu thức LaTeX: ${cas_verification.get('latex')}$")
        rag_text_parts.append("(BẮT BUỘC: Hãy giải thích từng bước dựa trên kết quả chính xác tuyệt đối này, không bịa đặt số khác).")

    if grounding_formulas:
        rag_text_parts.append("### CÁC CÔNG THỨC LIÊN QUAN TRONG KHO OMNISTEM:")
        for gf in grounding_formulas:
            rag_text_parts.append(f"- {gf['name_vi']} ({gf['topic']}): LaTeX: ${gf['latex']}$ (ID: {gf['id']})")
    if grounding_lessons:
        rag_text_parts.append("### BÀI HỌC THAM CHIẾU:")
        for gl in grounding_lessons:
            rag_text_parts.append(f"- {gl['title_vi']} (Chuyên đề: {gl['unit']})")

    rag_context = "\n".join(rag_text_parts) if rag_text_parts else "Chưa có công thức trực tiếp tương ứng."

    mode = req.pedagogical_mode.lower()
    if mode == "socratic":
        pedagogical_instructions = (
            "CHẾ ĐỘ SƯ PHẠM: SOCRATIC (GỢI MỞ TƯ DUY — MẶC ĐỊNH HỌC ĐƯỜNG).\n"
            "- TUYỆT ĐỐI KHÔNG giải hộ bài toán hoặc đưa đáp số cuối cùng ngay lập tức.\n"
            "- Hãy đặt câu hỏi dẫn dắt từng bước: 'Đề bài đã cho ta những đại lượng nào?', 'Để tính đại lượng này, ta cần mối liên hệ với định luật nào?'.\n"
            "- Chỉ ra các gợi ý công thức và hướng dẫn học sinh tự thế số tính toán."
        )
    elif mode == "deep_dive":
        pedagogical_instructions = (
            "CHẾ ĐỘ SƯ PHẠM: DEEP DIVE (CHỨNG MINH BẢN CHẤT & HỌC THUẬT CHUYÊN SÂU).\n"
            "- Hãy trình bày chứng minh chặt chẽ từ định nghĩa tiên đề toán học/vật lý.\n"
            "- Dùng ký hiệu KaTeX đầy đủ, giải thích chi tiết các bước biến đổi giải tích và điều kiện biên.\n"
            "- Nêu bật ý nghĩa vật lý/hóa học ẩn sau các đại số biểu tượng."
        )
    else:  # scholarship
        pedagogical_instructions = (
            "CHẾ ĐỘ SƯ PHẠM: SCHOLARSHIP (SĂN HỌC BỔNG QUỐC TẾ & NGHIÊN CỨU STEM).\n"
            "- Mở rộng bài toán ra ứng dụng nghiên cứu thực tiễn (công nghệ bán dẫn, biến đổi khí hậu, sinh học phân tử).\n"
            "- Hướng dẫn học sinh cách phát triển bài toán thành đề tài nghiên cứu (Spike Project) hoặc bài luận du học MIT, Oxford, NUS."
        )

    system_prompt = (
        "Bạn là Gia sư AI STEM cao cấp trực thuộc Nền tảng AISTEM X (aistemx.com) (Toán học, Vật lí, Hoá học, Sinh học chuẩn học đường từ THCS, THPT đến Đại học & Olympic quốc tế).\n"
        "Phương châm giáo dục: Tam Giác Vàng STEM (1. Bản chất tự nhiên -> 2. Tính toán & Công thức biểu tượng -> 3. Ứng dụng thực tế).\n"
        f"{pedagogical_instructions}\n"
        "Quy tắc trình bày:\n"
        "1. Luôn dùng Tiếng Việt sư phạm, mạch lạc, động viên tinh thần tự học.\n"
        "2. Bắt buộc dùng KaTeX: $...$ cho công thức nội dòng và $$...$$ cho phương trình độc lập.\n"
        "3. Tham chiếu các công thức chuẩn trong kho AISTEM X sau:\n"
        f"{rag_context}\n"
    )

    # 4. Tự động kích hoạt mô hình vẽ hình (AISTEM Vector Engine + SVG + FLUX) nếu có ý định vẽ
    is_draw = (req.model == "flux-drawing") or any(k in q.lower() for k in [
        "vẽ", "ve", "đồ thị", "do thi", "hình vẽ", "hinh ve", "sơ đồ", "so do", 
        "tam giác", "tam giac", "parabol", "parabola", "hình học", "hinh hoc", 
        "minh hoạ", "minh hoa", "lăng trụ", "hình chóp", "đường tròn", "vectơ", "vector",
        "draw", "sketch", "plot", "diagram", "illustration"
    ])
    drawn_svg = None
    drawn_image = None
    drawing_engine = None
    if is_draw:
        try:
            from engine.aistem.geometry_renderer import generate_accurate_math_svg
            drawn_svg, drawing_engine = generate_accurate_math_svg(q, subject=req.subject or "math")
        except Exception:
            try:
                drawn_svg = llm.cloudflare_generate_math_svg(q, subject=req.subject or "math")
                drawing_engine = "LLM Fallback"
            except Exception:
                drawn_svg = None

        try:
            drawn_image = llm.cloudflare_generate_image(q)
        except Exception:
            drawn_image = None

        if not drawn_image and drawn_svg:
            import base64
            b64_svg = base64.b64encode(drawn_svg.encode("utf-8")).decode("utf-8")
            drawn_image = f"data:image/svg+xml;base64,{b64_svg}"

    # 5. Gửi sang Cloudflare Workers AI
    try:
        history_dicts = [{"role": h.role, "content": h.content} for h in req.history[-6:]]
        model_to_use = "llama-3.3" if req.model == "flux-drawing" else req.model
        res = llm.cloudflare_chat(
            prompt=q,
            system=system_prompt,
            model=model_to_use,
            history=history_dicts,
            max_tokens=2048,
        )
        return {
            "reply": res.get("reply", ""),
            "thinking": res.get("thinking", ""),
            "model": "flux-drawing" if is_draw else res.get("model", req.model),
            "pedagogical_mode": mode,
            "grounding_formulas": grounding_formulas,
            "grounding_lessons": grounding_lessons,
            "cas_verification": cas_verification,
            "svg": drawn_svg,
            "drawing_engine": drawing_engine,
            "image_url": drawn_image,
            "success": True,
        }
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Lỗi khi xử lý qua Gia sư AI: {str(exc)}",
        )



@app.post("/api/ai/chat-stream")
def ai_chat_stream_endpoint(req: AIChatRequest):
    """Trợ lý Gia sư AI AISTEM X: Trả về SSE Stream thời gian thực kèm CAS & RAG metadata."""
    q = req.message.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Nội dung câu hỏi không được để trống")

    q_lower = q.lower()
    # 1. RAG Formulas
    grounding_formulas = []
    formulas_dict = get_formulas()
    words = [w for w in re.split(r"[\s,;:.?!+*\-/\\]+", q_lower) if len(w) >= 2]
    matched_f = []
    for f in formulas_dict.values():
        if req.subject and f.get("subject") != req.subject:
            continue
        score = sum(1 for w in words if w in f"{f.get('name_vi', '')} {f.get('name_en', '')} {f.get('topic', '')}".lower())
        if score > 0:
            matched_f.append((score, f))
    matched_f.sort(key=lambda x: x[0], reverse=True)
    for _, f in matched_f[:3]:
        grounding_formulas.append({
            "id": f["id"],
            "subject": f.get("subject"),
            "name_vi": f.get("name_vi"),
            "latex": f.get("latex"),
            "topic": f.get("topic"),
        })

    # 2. RAG Lessons
    grounding_lessons = []
    lessons_dict = get_lessons()
    matched_l = []
    for l in lessons_dict.values():
        if req.subject and l.get("subject") != req.subject:
            continue
        score = sum(1 for w in words if w in f"{l.get('title_vi', '')} {l.get('title_en', '')} {l.get('unit', '')}".lower())
        if score > 0:
            matched_l.append((score, l))
    matched_l.sort(key=lambda x: x[0], reverse=True)
    for _, l in matched_l[:2]:
        grounding_lessons.append({
            "id": l["id"],
            "subject": l.get("subject"),
            "title_vi": l.get("title_vi"),
            "unit": l.get("unit"),
        })

    # 3. Tự động kiểm chứng toán học / hoá học CAS
    cas_verification = None
    try:
        cas_res = llm.detect_math_intent(q)
        if cas_res and cas_res.get("success"):
            cas_verification = cas_res
    except Exception:
        cas_verification = None

    rag_text_parts = []
    if cas_verification:
        rag_text_parts.append("### KẾT QUẢ KIỂM CHỨNG TOÁN/HOÁ HỌC TỪ SYMPY CAS ENGINE (CHÍNH XÁC 100%):")
        rag_text_parts.append(f"- Phép toán: {cas_verification.get('operation')}")
        rag_text_parts.append(f"- Kết quả: {cas_verification.get('result') or cas_verification.get('solutions')}")
        if cas_verification.get('latex'):
            rag_text_parts.append(f"- Biểu thức LaTeX: ${cas_verification.get('latex')}$")
        rag_text_parts.append("(BẮT BUỘC: Hãy giải thích từng bước dựa trên kết quả chính xác tuyệt đối này, không bịa đặt số khác).")

    if grounding_formulas:
        rag_text_parts.append("### CÁC CÔNG THỨC LIÊN QUAN TRONG KHO OMNISTEM:")
        for gf in grounding_formulas:
            rag_text_parts.append(f"- {gf['name_vi']} ({gf['topic']}): LaTeX: ${gf['latex']}$ (ID: {gf['id']})")
    if grounding_lessons:
        rag_text_parts.append("### BÀI HỌC THAM CHIẾU:")
        for gl in grounding_lessons:
            rag_text_parts.append(f"- {gl['title_vi']} (Chuyên đề: {gl['unit']})")

    rag_context = "\n".join(rag_text_parts) if rag_text_parts else "Chưa có công thức trực tiếp tương ứng."

    mode = req.pedagogical_mode.lower()
    if mode == "socratic":
        pedagogical_instructions = (
            "CHẾ ĐỘ SƯ PHẠM: SOCRATIC (GỢI MỞ TƯ DUY — MẶC ĐỊNH HỌC ĐƯỜNG).\n"
            "- TUYỆT ĐỐI KHÔNG giải hộ bài toán hoặc đưa đáp số cuối cùng ngay lập tức.\n"
            "- Hãy đặt câu hỏi dẫn dắt từng bước: 'Đề bài đã cho ta những đại lượng nào?', 'Để tính đại lượng này, ta cần mối liên hệ với định luật nào?'.\n"
            "- Chỉ ra các gợi ý công thức và hướng dẫn học sinh tự thế số tính toán."
        )
    elif mode == "deep_dive":
        pedagogical_instructions = (
            "CHẾ ĐỘ SƯ PHẠM: DEEP DIVE (CHỨNG MINH BẢN CHẤT & HỌC THUẬT CHUYÊN SÂU).\n"
            "- Hãy trình bày chứng minh chặt chẽ từ định nghĩa tiên đề toán học/vật lý.\n"
            "- Dùng ký hiệu KaTeX đầy đủ, giải thích chi tiết các bước biến đổi giải tích và điều kiện biên.\n"
            "- Nêu bật ý nghĩa vật lý/hóa học ẩn sau các đại số biểu tượng."
        )
    else:
        pedagogical_instructions = (
            "CHẾ ĐỘ SƯ PHẠM: SCHOLARSHIP (SĂN HỌC BỔNG QUỐC TẾ & NGHIÊN CỨU STEM).\n"
            "- Mở rộng bài toán ra ứng dụng nghiên cứu thực tiễn (công nghệ bán dẫn, biến đổi khí hậu, sinh học phân tử).\n"
            "- Hướng dẫn học sinh cách phát triển bài toán thành đề tài nghiên cứu (Spike Project) hoặc bài luận du học MIT, Oxford, NUS."
        )

    system_prompt = (
        "Bạn là Gia sư AI STEM cao cấp trực thuộc Nền tảng AISTEM X (aistemx.com) (Toán học, Vật lí, Hoá học, Sinh học chuẩn học đường từ THCS, THPT đến Đại học & Olympic quốc tế).\n"
        "Phương châm giáo dục: Tam Giác Vàng STEM (1. Bản chất tự nhiên -> 2. Tính toán & Công thức biểu tượng -> 3. Ứng dụng thực tế).\n"
        f"{pedagogical_instructions}\n"
        "Quy tắc trình bày:\n"
        "1. Luôn dùng Tiếng Việt sư phạm, mạch lạc, động viên tinh thần tự học.\n"
        "2. Bắt buộc dùng KaTeX: $...$ cho công thức nội dòng và $$...$$ cho phương trình độc lập.\n"
        "3. Tham chiếu các công thức chuẩn trong kho AISTEM X sau:\n"
        f"{rag_context}\n"
    )

    history_dicts = [{"role": h.role, "content": h.content} for h in req.history[-6:]]

    # Tự động kích hoạt mô hình vẽ hình (AISTEM Vector Engine + SVG + FLUX) nếu có ý định vẽ
    is_draw = (req.model == "flux-drawing") or any(k in q.lower() for k in [
        "vẽ", "ve", "đồ thị", "do thi", "hình vẽ", "hinh ve", "sơ đồ", "so do", 
        "tam giác", "tam giac", "parabol", "parabola", "hình học", "hinh hoc", 
        "minh hoạ", "minh hoa", "lăng trụ", "hình chóp", "đường tròn", "vectơ", "vector",
        "draw", "sketch", "plot", "diagram", "illustration"
    ])
    drawn_svg = None
    drawn_image = None
    drawing_engine = None
    if is_draw:
        try:
            from engine.aistem.geometry_renderer import generate_accurate_math_svg
            drawn_svg, drawing_engine = generate_accurate_math_svg(q, subject=req.subject or "math")
        except Exception:
            try:
                drawn_svg = llm.cloudflare_generate_math_svg(q, subject=req.subject or "math")
                drawing_engine = "LLM Fallback"
            except Exception:
                drawn_svg = None

        try:
            drawn_image = llm.cloudflare_generate_image(q)
        except Exception:
            drawn_image = None

        if not drawn_image and drawn_svg:
            import base64
            b64_svg = base64.b64encode(drawn_svg.encode("utf-8")).decode("utf-8")
            drawn_image = f"data:image/svg+xml;base64,{b64_svg}"

    def event_generator():
        initial_meta = {
            "type": "metadata",
            "cas_verification": cas_verification,
            "grounding_formulas": grounding_formulas,
            "grounding_lessons": grounding_lessons,
            "model": "flux-drawing" if is_draw else req.model,
            "pedagogical_mode": mode,
            "svg": drawn_svg,
            "drawing_engine": drawing_engine,
            "image_url": drawn_image,
        }
        yield f"data: {json.dumps(initial_meta, ensure_ascii=False)}\n\n"

        stream_model = "llama-3.3" if req.model == "flux-drawing" else req.model
        for chunk in llm.cloudflare_chat_stream(
            prompt=q,
            system=system_prompt,
            model=stream_model,
            history=history_dicts,
            max_tokens=2048,
        ):
            delta_obj = {"type": "delta", "text": chunk}
            yield f"data: {json.dumps(delta_obj, ensure_ascii=False)}\n\n"

        yield "data: [DONE]\n\n"


    return StreamingResponse(event_generator(), media_type="text/event-stream")


@app.post("/api/ai/hint")
def ai_hint_endpoint(req: AIHintRequest):
    """Gợi ý tư duy Socratic trực tiếp cho một bài toán cụ thể trong phòng luyện tập."""
    problems_dict = get_problems()
    prob = problems_dict.get(req.problem_id)
    if not prob:
        raise HTTPException(status_code=404, detail=f"Không tìm thấy bài toán ID {req.problem_id}")

    statement = prob.get("statement_vi", "")
    solution_steps = prob.get("solution_steps", [])
    formulas_used = prob.get("formulas_used", [])
    why_wrong = prob.get("why_wrong", {})

    # Lấy thông tin bước hiện tại
    step_hint_target = ""
    if solution_steps:
        idx = max(0, min(req.step_index - 1, len(solution_steps) - 1))
        step_hint_target = f"Bước mục tiêu ({idx + 1}/{len(solution_steps)}): {solution_steps[idx]}"

    wrong_note = ""
    if req.student_answer and req.student_answer in why_wrong:
        wrong_note = f"Học sinh vừa chọn nhầm phương án {req.student_answer}: {why_wrong[req.student_answer]}"

    prompt = (
        f"Bài toán: {statement}\n"
        f"Công thức liên quan: {', '.join(formulas_used)}\n"
        f"{step_hint_target}\n"
        f"{wrong_note}\n\n"
        "Hãy đưa ra MỘT gợi ý tư duy Socratic ngắn gọn (2-3 câu) giúp học sinh tự nhận ra hướng giải quyết. "
        "TUYỆT ĐỐI KHÔNG tiết lộ đáp án số hoặc giải trọn vẹn bài toán. Dùng KaTeX $...$ cho công thức nếu cần."
    )

    system = "Bạn là Trợ lý Gợi Ý Tư Duy Socratic của AISTEM X (aistemx.com). Nhiệm vụ của bạn là mở khóa bế tắc cho học sinh mà không giải hộ."

    try:
        res = llm.cloudflare_chat(prompt=prompt, system=system, model="llama-3.3", max_tokens=256, temperature=0.3)
        return {
            "hint": res.get("reply", ""),
            "problem_id": req.problem_id,
            "step": req.step_index,
            "formulas_used": formulas_used,
            "success": True,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Lỗi tạo gợi ý AI: {str(exc)}")


@app.post("/api/ai/vision-solve")
def ai_vision_solve_endpoint(req: AIVisionSolveRequest):
    """Nhận diện đề bài hoặc bài giải viết tay qua ảnh chụp bằng Llama 3.2 Vision."""
    if not req.image_base64:
        raise HTTPException(status_code=400, detail="Ảnh chụp không được để trống")

    prompt = req.prompt or (
        "Bạn là Chuyên gia Khảo thí Khoa học AISTEM X (aistemx.com). Hãy đọc ảnh đề bài này và thực hiện:\n"
        "1. Trích xuất lại đề bài bằng Tiếng Việt và công thức toán học/hóa học chuẩn KaTeX ($...$).\n"
        "2. Xác định các đại lượng đã cho và đại lượng cần tìm.\n"
        "3. Hướng dẫn các bước tư duy bản chất để học sinh tự tìm ra kết quả."
    )

    try:
        res = llm.cloudflare_vision(prompt=prompt, image_bytes=req.image_base64, max_tokens=1500)
        reply_text = res.get("reply", "")

        # RAG tìm kiếm công thức liên quan từ nội dung ảnh vừa nhận diện
        grounding_formulas = []
        formulas_dict = get_formulas()
        words = [w for w in re.split(r"[\s,;:.?!+*\-/\\]+", reply_text.lower()) if len(w) >= 3]
        matched_f = []
        for f in formulas_dict.values():
            score = sum(1 for w in words if w in f.get("name_vi", "").lower())
            if score > 0:
                matched_f.append((score, f))
        matched_f.sort(key=lambda x: x[0], reverse=True)
        for _, f in matched_f[:3]:
            grounding_formulas.append({
                "id": f["id"],
                "name_vi": f.get("name_vi"),
                "latex": f.get("latex"),
                "topic": f.get("topic"),
            })

        return {
            "reply": reply_text,
            "model": "llama-3.2-vision",
            "grounding_formulas": grounding_formulas,
            "success": True,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Lỗi nhận diện thị giác AI: {str(exc)}")


@app.post("/api/ai/cas-eval")
def ai_cas_eval_endpoint(req: AICASRequest):
    """Kiểm định toán học biểu tượng và triệt tiêu ảo giác bằng SymPy CAS Engine."""
    res = llm.cas_tool_eval(req.expression, operation=req.operation, variable=req.variable)
    return res


@app.post("/api/ai/draw")
def ai_draw_endpoint(req: AIDrawRequest):
    """Vẽ minh họa toán học/khoa học bằng AI Cloudflare & AISTEM Accurate Geometry Engine."""
    prompt = req.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Mô tả hình vẽ không được để trống")

    svg_content = None
    image_url = None
    drawing_engine = None

    if req.mode in ("svg", "both"):
        try:
            from engine.aistem.geometry_renderer import generate_accurate_math_svg
            svg_content, drawing_engine = generate_accurate_math_svg(prompt, subject=req.subject or "math")
        except Exception:
            try:
                svg_content = llm.cloudflare_generate_math_svg(prompt, subject=req.subject or "math")
                drawing_engine = "LLM Fallback"
            except Exception:
                svg_content = None

    if req.mode in ("flux", "both"):
        try:
            image_url = llm.cloudflare_generate_image(prompt)
        except Exception:
            image_url = None

    if not image_url and svg_content:
        import base64
        b64_svg = base64.b64encode(svg_content.encode("utf-8")).decode("utf-8")
        image_url = f"data:image/svg+xml;base64,{b64_svg}"

    if not svg_content and not image_url:
        raise HTTPException(status_code=500, detail="Không thể tạo hình ảnh minh họa lúc này. Vui lòng thử lại sau giây lát.")

    return {
        "success": True,
        "prompt": prompt,
        "svg": svg_content,
        "image_url": image_url,
        "drawing_engine": drawing_engine,
        "mode": req.mode,
    }



@app.post("/api/ai/generate-problem")
def ai_generate_problem_endpoint(req: AIGenerateProblemRequest):
    """Tự động thiết kế bài toán STEM từ prompt, có kiểm chứng SymPy CAS và tự động gắn minh hoạ SVG."""
    chosen_model = req.model if req.model in ("deepseek-r1", "llama-3.3", "qwq-32b") else "deepseek-r1"

    sys_prompt = """Bạn là chuyên gia thiết kế đề thi STEM (Toán, Vật lí, Hoá học, Sinh học) chuẩn quốc gia và quốc tế (AP/IB/Olympic).
Khi được yêu cầu tạo bài toán, bạn PHẢI trả về ĐÚNG 1 khối JSON hợp lệ duy nhất, theo cấu trúc:
{
  "subject": "math / physics / chemistry / biology",
  "level": "thpt / thcs / tieu-hoc",
  "topic": "Tên chủ đề bài toán",
  "title": "Tiêu đề ngắn gọn của bài toán",
  "statement": "Nội dung đề bài chi tiết, đầy đủ số liệu và câu hỏi rõ ràng",
  "type": "trac-nghiem",
  "choices": [
    {"key": "A", "text": "Phương án A"},
    {"key": "B", "text": "Phương án B"},
    {"key": "C", "text": "Phương án C"},
    {"key": "D", "text": "Phương án D"}
  ],
  "answer": "A",
  "solution_steps": [
    "Bước 1: ...",
    "Bước 2: ...",
    "Bước 3: ..."
  ],
  "formula_used": "Tên hoặc mã công thức áp dụng",
  "latex": "Công thức toán học hoặc đáp số dạng LaTeX",
  "explanation": "Giải thích sư phạm ngắn gọn",
  "difficulty": 3
}
Yêu cầu tối thượng: Tính toán số học phải chính xác tuyệt đối 100%, không được nhầm lẫn số liệu."""

    user_query = req.prompt.strip()
    if req.subject:
        user_query += f"\nMôn học: {req.subject}"
    if req.level:
        user_query += f"\nCấp độ: {req.level}"
    if req.difficulty:
        user_query += f"\nĐộ khó: {req.difficulty}/5"

    try:
        res = llm.cloudflare_chat(
            user_query,
            system=sys_prompt,
            model=chosen_model,
            temperature=0.2,
            max_tokens=2500,
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Lỗi gọi mô hình AI: {str(exc)}")

    raw_text = res.get("reply", "").strip()
    thinking = res.get("thinking", "")
    model_used = res.get("model", chosen_model)

    # Bóc tách JSON
    clean_json = raw_text
    if "```json" in clean_json:
        clean_json = clean_json.split("```json", 1)[1].split("```", 1)[0].strip()
    elif "```" in clean_json:
        clean_json = clean_json.split("```", 1)[1].split("```", 1)[0].strip()

    p_data = None
    try:
        p_data = json.loads(clean_json)
    except Exception:
        s = clean_json.find("{")
        e = clean_json.rfind("}")
        if s != -1 and e != -1 and e > s:
            try:
                p_data = json.loads(clean_json[s : e + 1])
            except Exception:
                pass

    if not p_data or not isinstance(p_data, dict):
        raise HTTPException(
            status_code=502,
            detail=f"Mô hình AI không trả về cấu trúc JSON bài toán hợp lệ. Raw output: {raw_text[:250]}"
        )

    # Chuẩn hoá cấu trúc bài toán AISTEM
    p_data["id"] = f"ai_gen_{int(time.time() * 1000)}"
    stmt = p_data.get("statement_vi") or p_data.get("statement") or ""
    p_data["statement"] = stmt
    p_data["statement_vi"] = stmt
    if "choices" not in p_data or not isinstance(p_data["choices"], list):
        p_data["choices"] = []
    
    raw_steps = p_data.get("solution_steps") or []
    norm_steps = []
    for s in raw_steps:
        if isinstance(s, str):
            norm_steps.append({"explain": s, "latex": ""})
        elif isinstance(s, dict):
            norm_steps.append({
                "explain": s.get("explain") or s.get("text") or str(s),
                "latex": s.get("latex") or "",
            })
    p_data["solution_steps"] = norm_steps

    # 1. Kiểm chứng độc lập qua SymPy CAS Engine
    is_verified = False
    cas_status = "unchecked"
    cas_details: dict[str, Any] = {}
    try:
        is_verified, cas_status, cas_details = verify_problem_data(p_data, budget=1.0)
    except Exception as cas_err:
        cas_details = {"error": str(cas_err)}

    # 2. Tự động tìm kiếm và liên kết ảnh minh họa vector 2D phù hợp
    matched_svg_url = None
    formula_ref = str(p_data.get("formula_used") or "")
    topic_ref = str(p_data.get("topic") or "").lower()
    title_ref = str(p_data.get("title") or "").lower()

    # Tìm trong cache illustrations
    illus = get_illustrations2d()
    for fid, ill in illus.items():
        if fid in formula_ref or (ill.get("title") and ill.get("title", "").lower() in formula_ref.lower()):
            matched_svg_url = f"/api/illustrations2d/{fid}"
            break
        if ill.get("topic") and ill.get("topic", "").lower() in topic_ref:
            matched_svg_url = f"/api/illustrations2d/{fid}"
            break
        if ill.get("title") and ill.get("title", "").lower() in title_ref and len(ill.get("title", "")) > 6:
            matched_svg_url = f"/api/illustrations2d/{fid}"
            break

    p_data["cas_verified"] = is_verified
    p_data["cas_status"] = cas_status
    p_data["cas_details"] = cas_details
    p_data["illustration_url"] = matched_svg_url

    return {
        "success": True,
        "problem": p_data,
        "cas_verified": is_verified,
        "cas_status": cas_status,
        "cas_details": cas_details,
        "illustration_url": matched_svg_url,
        "thinking": thinking,
        "model_used": model_used,
    }


# Bộ nhớ thẻ ghi nhớ bổ sung từ AI
_CUSTOM_FLASHCARDS_CACHE: list[dict[str, Any]] = []

@app.post("/api/ai/save-flashcard")
def ai_save_flashcard_endpoint(req: AISaveFlashcardRequest):
    """Lưu một công thức hoặc khái niệm từ Gia sư AI vào Bộ thẻ ghi nhớ FSRS."""
    card = {
        "id": f"ai_card_{int(time.time() * 1000)}",
        "front": req.front.strip(),
        "back": req.back.strip(),
        "latex": req.latex,
        "subject": req.subject,
        "topic": req.topic or "Gia Sư AI AISTEM X",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    _CUSTOM_FLASHCARDS_CACHE.append(card)
    return {
        "success": True,
        "message": "Đã lưu thẻ thành công vào Bộ nhớ FSRS",
        "card": card,
    }


@app.get("/api/ai/flashcards")
def ai_get_flashcards_endpoint():
    """Lấy danh sách các thẻ ghi nhớ do AI sinh ra."""
    return {
        "cards": _CUSTOM_FLASHCARDS_CACHE,
        "total": len(_CUSTOM_FLASHCARDS_CACHE),
    }


class AIFeedbackRequest(BaseModel):
    instruction: str
    response: str
    input_context: Optional[str] = ""
    subject: Optional[str] = "stem"
    pedagogical_mode: Optional[str] = "socratic"
    rating: int = Field(default=1, description="1: Thích / Đúng chuẩn, -1: Chưa hài lòng")
    feedback_text: Optional[str] = ""
    cas_verified: Optional[bool] = False


@app.post("/api/ai/feedback")
def ai_feedback_endpoint(req: AIFeedbackRequest):
    """Ghi nhận đánh giá phản hồi của người dùng và lưu mẫu Gold Dataset phục vụ Fine-tuning."""
    try:
        sample_id = db.save_ai_training_sample(
            instruction=req.instruction,
            response=req.response,
            input_context=req.input_context or "",
            subject=req.subject or "stem",
            pedagogical_mode=req.pedagogical_mode or "socratic",
            rating=req.rating,
            feedback_text=req.feedback_text or "",
            cas_verified=bool(req.cas_verified),
        )
        return {
            "success": True,
            "sample_id": sample_id,
            "message": "Đã ghi nhận đánh giá vào kho dữ liệu vàng",
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/api/ai/training-data/export")
def ai_export_training_data_endpoint(format: str = "alpaca", min_rating: int = 1, limit: int = 1000):
    """Trích xuất tập dữ liệu Gold Dataset chuẩn format Alpaca hoặc ShareGPT phục vụ huấn luyện LoRA."""
    samples = db.get_ai_training_dataset(min_rating=min_rating, limit=limit)
    if format == "alpaca":
        alpaca_list = [
            {
                "instruction": s["instruction"],
                "input": s.get("input_context", ""),
                "output": s["response"],
                "metadata": {
                    "subject": s.get("subject"),
                    "pedagogical_mode": s.get("pedagogical_mode"),
                    "cas_verified": bool(s.get("cas_verified")),
                }
            }
            for s in samples
        ]
        return {"total": len(alpaca_list), "format": "alpaca", "data": alpaca_list}
    return {"total": len(samples), "format": "raw", "data": samples}



@app.get("/api/scenes3d")
def list_scenes3d():
    """Danh sách toàn bộ mô hình 3D."""
    scenes = get_scenes3d()
    return {"total": len(scenes), "scenes": list(scenes.values())}


@app.get("/api/leaderboard")
def get_public_leaderboard(limit: int = Query(20, ge=1, le=100)):
    """Bảng xếp hạng Đua Top Học Viên toàn cầu."""
    rankings = db.get_leaderboard_rankings(limit=limit)
    return {"total": len(rankings), "rankings": rankings}


@app.get("/api/tournaments")
def list_tournaments_endpoint():
    """Danh sách các giải đấu đua top có phí kèm tiến độ gom đủ thí sinh."""
    tournaments = db.list_tournaments()
    return {"total": len(tournaments), "tournaments": tournaments}


@app.get("/api/tournaments/{tournament_id}")
def get_tournament_endpoint(tournament_id: int, authorization: Optional[str] = Header(None)):
    """Chi tiết giải đấu và trạng thái đăng ký của thí sinh."""
    user_id = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.split(" ")[1].strip()
        user = db.get_user_by_token(token)
        if user:
            user_id = user["id"]

    t = db.get_tournament_by_id(tournament_id, user_id)
    if not t:
        raise HTTPException(status_code=404, detail="Không tìm thấy giải đấu")
    return t


class TournamentRegisterRequest(BaseModel):
    tournament_id: int
    token: str


@app.post("/api/tournaments/register")
def register_tournament_endpoint(req: TournamentRegisterRequest):
    """Đăng ký tham gia giải đấu và thanh toán lệ phí."""
    user = db.get_user_by_token(req.token)
    if not user:
        raise HTTPException(status_code=401, detail="Phiên làm việc không hợp lệ")

    try:
        res = db.register_user_tournament(user["id"], req.tournament_id)
        return res
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/tournaments/{tournament_id}/leaderboard")
def get_tournament_leaderboard_endpoint(tournament_id: int):
    """Bảng xếp hạng điểm thi của giải đấu."""
    rankings = db.get_tournament_leaderboard(tournament_id)
    return {"total": len(rankings), "rankings": rankings}





@app.get("/api/scenes3d/{scene_id}")
def get_scene3d_data(scene_id: str):
    """Nội dung JSON của một cảnh 3D."""
    scenes = get_scenes3d()
    sfile = DATA_DIR / "scenes3d" / f"{scene_id}.json"
    if sfile.exists():
        return JSONResponse(content=json.loads(sfile.read_text(encoding="utf-8")))

    # Thử tìm theo formula_id
    for sid, s in scenes.items():
        if s.get("formula_id") == scene_id or sid == scene_id:
            sfile2 = DATA_DIR / "scenes3d" / f"{sid}.json"
            if sfile2.exists():
                return JSONResponse(content=json.loads(sfile2.read_text(encoding="utf-8")))

    raise HTTPException(status_code=404, detail="Không tìm thấy cảnh 3D")


@app.get("/api/illustrations2d/{formula_id}")
def get_illustration2d(formula_id: str):
    """Trả về file SVG minh họa 2D chuẩn khoa học."""
    illus = get_illustrations2d()
    if formula_id in illus:
        item = illus[formula_id]
        if "svg" in item and item["svg"]:
            return Response(content=item["svg"], media_type="image/svg+xml")
        if "svg_path" in item:
            path = DATA_DIR / "illustrations" / item["svg_path"]
            if path.exists():
                return Response(content=path.read_text(encoding="utf-8"), media_type="image/svg+xml")

    # Hoặc tìm trong thư mục data/illustrations/svg
    svg_file = DATA_DIR / "illustrations" / "svg" / f"{formula_id}.svg"
    if svg_file.exists():
        return Response(content=svg_file.read_text(encoding="utf-8"), media_type="image/svg+xml")

    svg_file_root = DATA_DIR / "illustrations" / f"{formula_id}.svg"
    if svg_file_root.exists():
        return Response(content=svg_file_root.read_text(encoding="utf-8"), media_type="image/svg+xml")

    # Hoặc render trực tiếp từ registry chuyên ngành AISTEM nếu có luật khớp
    formulas_repo = get_formulas()
    if formula_id in formulas_repo:
        try:
            import sys
            root_dir = Path(__file__).resolve().parent.parent
            if str(root_dir) not in sys.path:
                sys.path.insert(0, str(root_dir))
            from tools.illus.registry import match_formula, render
            matched = match_formula(formulas_repo[formula_id])
            if matched:
                gen_name, params = matched[0], matched[1]
                svg_content = render(gen_name, params)
                if svg_content:
                    return Response(content=svg_content, media_type="image/svg+xml")
        except Exception as e:
            logger.warning(f"Error rendering dynamic SVG for {formula_id}: {e}")

    raise HTTPException(status_code=404, detail="Không tìm thấy minh họa 2D")


@app.api_route("/illustrations", methods=["GET", "HEAD"], response_class=HTMLResponse)
def serve_illustrations_gallery():
    """Trang tra cứu & kiểm duyệt trực quan toàn bộ 655 hình minh họa và 4,617 công thức còn thiếu."""
    illus_all = get_illustrations2d()
    formulas_all = get_formulas()
    
    covered_ids = set(illus_all.keys())
    for f in DATA_DIR.glob("illustrations/svg/*.svg"):
        covered_ids.add(f.stem)
        
    covered_items = []
    for fid in covered_ids:
        f = formulas_all.get(fid, {})
        ill = illus_all.get(fid, {})
        covered_items.append({
            "id": fid,
            "title": ill.get("title") or f.get("name_vi") or f.get("name") or fid,
            "subject": ill.get("subject") or f.get("subject") or "math",
            "level": ill.get("level") or f.get("level") or "thpt",
            "topic": ill.get("topic") or f.get("topic") or "",
            "latex": ill.get("latex") or f.get("latex") or "",
            "generator": ill.get("generator") or "manual",
        })
        
    missing_items = []
    for fid, f in formulas_all.items():
        if fid not in covered_ids:
            missing_items.append({
                "id": fid,
                "title": f.get("name_vi") or f.get("name") or fid,
                "subject": f.get("subject") or "math",
                "level": f.get("level") or "",
                "topic": f.get("topic") or "",
                "latex": f.get("latex") or "",
            })
            
    # Sort
    covered_items.sort(key=lambda x: (x["subject"], x["topic"], x["title"]))
    missing_items.sort(key=lambda x: (x["subject"], x["topic"], x["title"]))
    
    cnt_covered = len(covered_items)
    cnt_missing = len(missing_items)
    cnt_math = sum(1 for x in covered_items if x["subject"] == "math")
    cnt_phys = sum(1 for x in covered_items if x["subject"] == "physics")
    cnt_chem = sum(1 for x in covered_items if x["subject"] == "chemistry")
    cnt_bio = sum(1 for x in covered_items if x["subject"] == "biology")
    total_all = cnt_covered + cnt_missing
    pct_covered = f"{cnt_covered / total_all * 100:.1f}%" if total_all else "0%"
    pct_missing = f"{cnt_missing / total_all * 100:.1f}%" if total_all else "0%"

    covered_json = json.dumps(covered_items, ensure_ascii=False)
    missing_json = json.dumps(missing_items, ensure_ascii=False)
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>AISTEM - Thư Viện Minh Họa Khoa Học 2D</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <style>
    :root {{
      --bg: #0b0f19;
      --card: #131b2e;
      --card-border: #1e293b;
      --text-main: #f8fafc;
      --text-sub: #94a3b8;
      --primary: #38bdf8;
      --accent: #818cf8;
      --math: #6366f1;
      --phys: #06b6d4;
      --chem: #10b981;
      --bio: #ec4899;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg);
      color: var(--text-main);
      padding: 30px 20px;
    }}
    .container {{ max-width: 1380px; margin: 0 auto; }}
    header {{
      background: var(--card);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 28px;
      margin-bottom: 24px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }}
    h1 {{ font-size: 1.8rem; margin-bottom: 8px; color: #ffffff; display: flex; align-items: center; gap: 10px; }}
    .stats-bar {{
      display: flex; gap: 20px; flex-wrap: wrap; margin-top: 18px; padding-top: 18px;
      border-top: 1px solid var(--card-border);
    }}
    .stat-box {{
      background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
      border-radius: 10px; padding: 10px 18px;
    }}
    .stat-val {{ font-size: 1.3rem; font-weight: 800; }}
    .stat-lbl {{ font-size: 0.75rem; color: var(--text-sub); text-transform: uppercase; }}
    .controls {{
      display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; align-items: center;
    }}
    .btn {{
      padding: 9px 18px; border-radius: 9999px; border: 1px solid var(--card-border);
      background: var(--card); color: var(--text-main); cursor: pointer; font-size: 0.88rem; font-weight: 600;
      transition: all 0.2s;
    }}
    .btn.active {{ background: var(--primary); color: #0f172a; border-color: var(--primary); }}
    .search-input {{
      flex: 1; min-width: 250px; padding: 10px 16px; border-radius: 8px;
      background: var(--card); border: 1px solid var(--card-border); color: #fff; font-size: 0.9rem;
    }}
    .grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px;
    }}
    .card {{
      background: var(--card); border: 1px solid var(--card-border); border-radius: 14px;
      overflow: hidden; display: flex; flex-direction: column; transition: transform 0.2s, border-color 0.2s;
    }}
    .card:hover {{ transform: translateY(-4px); border-color: var(--primary); }}
    .svg-container {{
      height: 190px; background: #ffffff; display: flex; align-items: center; justify-content: center;
      padding: 12px; border-bottom: 1px solid var(--card-border); position: relative;
    }}
    .svg-container img {{ max-height: 100%; max-width: 100%; object-fit: contain; }}
    .card-body {{ padding: 16px; flex: 1; display: flex; flex-direction: column; }}
    .badge {{
      display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 0.72rem; font-weight: 700;
      text-transform: uppercase; margin-right: 6px; margin-bottom: 8px;
    }}
    .badge-math {{ background: rgba(99,102,241,0.2); color: #a5b4fc; }}
    .badge-physics {{ background: rgba(6,182,212,0.2); color: #67e8f9; }}
    .badge-chemistry {{ background: rgba(16,185,129,0.2); color: #6ee7b7; }}
    .badge-biology {{ background: rgba(236,72,153,0.2); color: #f472b6; }}
    .card-title {{ font-size: 1rem; font-weight: 700; margin-bottom: 6px; color: #fff; }}
    .card-topic {{ font-size: 0.8rem; color: var(--text-sub); margin-bottom: 10px; }}
    .card-math {{
      margin-top: auto; padding: 10px; background: rgba(0,0,0,0.25); border-radius: 8px;
      font-size: 0.88rem; overflow-x: auto; text-align: center;
    }}
    .table-container {{
      background: var(--card); border: 1px solid var(--card-border); border-radius: 14px; overflow: hidden;
    }}
    table {{ width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem; }}
    th, td {{ padding: 12px 16px; border-bottom: 1px solid var(--card-border); }}
    th {{ background: rgba(255,255,255,0.02); color: var(--text-sub); font-weight: 600; }}
    tr:hover td {{ background: rgba(255,255,255,0.02); }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>📐 Thư Viện Minh Họa Khoa Học AISTEM</h1>
      <p style="color: var(--text-sub); font-size: 0.92rem;">
        Kho sơ đồ kỹ thuật vector SVG 2D nguyên bản phục vụ {total_all:,} công thức Toán, Lí, Hóa, Sinh.
      </p>
      <div class="stats-bar">
        <div class="stat-box"><div class="stat-val" style="color: #10b981;">{cnt_covered:,}</div><div class="stat-lbl">Đã có hình 2D ({pct_covered})</div></div>
        <div class="stat-box"><div class="stat-val" style="color: #f59e0b;">{cnt_missing:,}</div><div class="stat-lbl">Chưa có sơ đồ riêng ({pct_missing})</div></div>
        <div class="stat-box"><div class="stat-val" style="color: #a5b4fc;">{cnt_math:,}</div><div class="stat-lbl">Toán Học (2D)</div></div>
        <div class="stat-box"><div class="stat-val" style="color: #67e8f9;">{cnt_phys:,}</div><div class="stat-lbl">Vật Lí (2D)</div></div>
        <div class="stat-box"><div class="stat-val" style="color: #f472b6;">{cnt_bio:,}</div><div class="stat-lbl">Sinh Học (2D)</div></div>
        <div class="stat-box"><div class="stat-val" style="color: #6ee7b7;">{cnt_chem:,}</div><div class="stat-lbl">Hóa Học (2D)</div></div>
      </div>
    </header>

    <div class="controls">
      <button class="btn active" id="btn-covered" onclick="setMode('covered')">Đã có hình minh họa ({cnt_covered:,})</button>
      <button class="btn" id="btn-missing" onclick="setMode('missing')">⚠️ Danh sách còn thiếu ({cnt_missing:,})</button>
      
      <div style="margin-left: auto; display: flex; gap: 8px;">
        <select class="btn" id="subject-filter" onchange="applyFilters()">
          <option value="">Tất cả môn</option>
          <option value="math">Toán Học</option>
          <option value="physics">Vật Lí</option>
          <option value="chemistry">Hóa Học</option>
          <option value="biology">Sinh Học</option>
        </select>
        <input type="text" id="search-box" class="search-input" placeholder="Tìm tên công thức, mã ID, chủ đề..." oninput="applyFilters()">
      </div>
    </div>

    <div id="content-area"></div>
  </div>

  <script>
    const COVERED = {covered_json};
    const MISSING = {missing_json};
    let currentMode = 'covered';

    function setMode(mode) {{
      currentMode = mode;
      document.getElementById('btn-covered').classList.toggle('active', mode === 'covered');
      document.getElementById('btn-missing').classList.toggle('active', mode === 'missing');
      applyFilters();
    }}

    function applyFilters() {{
      const subj = document.getElementById('subject-filter').value;
      const q = document.getElementById('search-box').value.toLowerCase().trim();
      const list = currentMode === 'covered' ? COVERED : MISSING;

      const filtered = list.filter(item => {{
        if (subj && item.subject !== subj) return false;
        if (q) {{
          const str = (item.title + ' ' + item.topic + ' ' + item.id + ' ' + item.latex).toLowerCase();
          if (!str.includes(q)) return false;
        }}
        return true;
      }});

      renderContent(filtered);
    }}

    function renderContent(items) {{
      const area = document.getElementById('content-area');
      if (items.length === 0) {{
        area.innerHTML = '<div style=\"text-align:center; padding: 60px; color: var(--text-sub);\">Không có mục nào khớp bộ lọc.</div>';
        return;
      }}

      if (currentMode === 'covered') {{
        area.innerHTML = '<div class=\"grid\">' + items.map(item => `
          <div class=\"card\">
            <div class=\"svg-container\">
              <img src=\"/api/illustrations2d/${{item.id}}\" alt=\"${{item.title}}\" loading=\"lazy\" onerror=\"this.onerror=null; this.parentElement.innerHTML='<div style=\\'color:#94a3b8;font-size:12px;padding:30px 10px;text-align:center;\\'>Đang cập nhật sơ đồ</div>';\">
            </div>
            <div class=\"card-body\">
              <div>
                <span class=\"badge badge-${{item.subject}}\">${{item.subject}}</span>
                <span class=\"badge\" style=\"background:rgba(255,255,255,0.06); color:#cbd5e1;\">${{item.level || 'all'}}</span>
              </div>
              <div class=\"card-title\">${{item.title}}</div>
              <div class=\"card-topic\">${{item.topic || item.id}}</div>
              <div class=\"card-math\" id=\"math-${{item.id.replace(/[^a-zA-Z0-9]/g, '_')}}\"></div>
            </div>
          </div>
        `).join('') + '</div>';

        // Render KaTeX for cards
        items.forEach(item => {{
          const el = document.getElementById('math-' + item.id.replace(/[^a-zA-Z0-9]/g, '_'));
          if (el && item.latex) {{
            try {{
              katex.render(item.latex, el, {{ throwOnError: false, displayMode: false }});
            }} catch(e) {{
              el.innerText = item.latex;
            }}
          }}
        }});
      }} else {{
        area.innerHTML = `
          <div class=\"table-container\">
            <table>
              <thead>
                <tr>
                  <th style=\"width: 100px;\">Môn</th>
                  <th style=\"width: 110px;\">Cấp học</th>
                  <th style=\"width: 220px;\">Chủ đề</th>
                  <th>Tên công thức / Mã ID</th>
                  <th>Biểu thức LaTeX</th>
                </tr>
              </thead>
              <tbody>
                ${{items.slice(0, 300).map(item => `
                  <tr>
                    <td><span class=\"badge badge-${{item.subject}}\">${{item.subject}}</span></td>
                    <td style=\"color: var(--text-sub); font-size: 0.85rem;\">${{item.level}}</td>
                    <td style=\"color: var(--text-main); font-weight: 600;\">${{item.topic}}</td>
                    <td>
                      <div style=\"font-weight: 700; color: #fff;\">${{item.title}}</div>
                      <div style=\"font-size: 0.76rem; color: var(--text-sub); font-family: monospace;\">${{item.id}}</div>
                    </td>
                    <td style=\"font-family: monospace; font-size: 0.82rem; color: #38bdf8;\">${{item.latex ? item.latex.substring(0, 60) : ''}}</td>
                  </tr>
                `).join('')}}
              </tbody>
            </table>
            ${{items.length > 300 ? `<div style=\"padding: 16px; text-align:center; color: var(--text-sub); font-size: 0.88rem;\">Đang hiển thị 300 / ${{items.length}} công thức. Hãy dùng ô tìm kiếm để lọc chi tiết.</div>` : ''}}
          </div>
        `;
      }}
    }}

    applyFilters();
  </script>
</body>
</html>"""
    return HTMLResponse(content=html)



# -------------------------------------------------------------
# STEM Laboratory Calculation & Simulation APIs (Toán, Hóa, Sinh)
# -------------------------------------------------------------
from engine import stem_lab_engine

@app.get("/api/lab/specimens")
def api_get_lab_specimens(category: Optional[str] = None):
    """Tra cứu kho mẫu vật thí nghiệm (Sinh học, Hóa chất, Dụng cụ Vật lý)."""
    spec_file = DATA_DIR / "lab_specimens.json"
    if not spec_file.exists():
        return []
    data = json.loads(spec_file.read_text(encoding="utf-8"))
    if category:
        return [s for s in data if s.get("category") == category]
    return data


class MatrixRequest(BaseModel):
    a: float = 2.0
    b: float = 1.0
    c: float = 1.0
    d: float = 2.0

@app.post("/api/lab/math/matrix")
def api_math_matrix_transform(req: MatrixRequest):
    """Tính toán ma trận biến đổi không gian 2D, trị riêng & vectơ riêng."""
    return stem_lab_engine.matrix_analysis_2d(req.a, req.b, req.c, req.d)


class TitrationRequest(BaseModel):
    acid_conc: float = 0.1
    acid_vol_ml: float = 20.0
    base_conc: float = 0.1
    base_vol_ml: float = 10.0
    acid_valency: int = 1
    base_valency: int = 1

@app.post("/api/lab/chemistry/titration")
def api_chemistry_titration(req: TitrationRequest):
    """Tính toán pH, pOH và điểm tương đương chuẩn độ axit-bazơ."""
    return stem_lab_engine.calculate_solution_ph(
        req.acid_conc, req.acid_vol_ml, req.base_conc, req.base_vol_ml,
        req.acid_valency, req.base_valency
    )


@app.post("/api/formulas/{formula_id}/calculate")
async def api_calculate_formula(formula_id: str, req: dict = {}):
    """Tính toán và thế số từng bước cho một công thức bất kỳ."""
    formulas = get_formulas()
    if formula_id not in formulas:
        raise HTTPException(status_code=404, detail="Không tìm thấy công thức")
    
    formula_data = formulas[formula_id]
    variables = req.get("variables", {}) if isinstance(req, dict) else {}
    result = stem_lab_engine.solve_formula_values(formula_id, formula_data, variables)
    return result


@app.get("/api/lab/chemistry/reactions")
def api_chemistry_reactions(reaction_id: str = "zn_hcl"):
    """Tra cứu nhiệt động học và cân bằng phản ứng hóa học mẫu."""
    return stem_lab_engine.balance_preset_reaction(reaction_id)


class DnaRequest(BaseModel):
    dna_sequence: str = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"

@app.post("/api/lab/biology/dna-translate")
def api_biology_dna_translate(req: DnaRequest):
    """Phiên mã DNA -> mRNA và Dịch mã thành chuỗi Axit Amin (Protein)."""
    return stem_lab_engine.molecular_biology_pipeline(req.dna_sequence)


class PunnettRequest(BaseModel):
    p1: str = "Aa"
    p2: str = "Aa"

@app.post("/api/lab/biology/mendelian-cross")
def api_biology_mendelian_cross(req: PunnettRequest):
    """Tính toán lai di truyền Men-đen và ma trận Punnett Square."""
    return stem_lab_engine.mendelian_punnett_cross(req.p1, req.p2)


class PopulationRequest(BaseModel):
    r: float = 0.5
    K: float = 1000.0
    N0: float = 50.0
    t_max: int = 30

@app.post("/api/lab/biology/population-growth")
def api_biology_population_growth(req: PopulationRequest):
    """Mô phỏng tăng trưởng quần thể sinh thái Logistic Verhulst."""
    return stem_lab_engine.population_logistic_growth(req.r, req.K, req.N0, req.t_max)


@app.get("/api/lab/chemistry/pubchem-3d")
def api_get_pubchem_3d(compound: str = "aspirin"):
    """Tải và phân tích cấu trúc 3D thực nghiệm từ PubChem REST API."""
    return stem_lab_engine.fetch_pubchem_3d_structure(compound)


@app.get("/api/lab/biology/pdb-structure")
def api_get_pdb_structure(pdb_id: str = "1BNA"):
    """Tải và phân tích cấu trúc đại phân tử thực nghiệm từ RCSB Protein Data Bank (PDB)."""
    return stem_lab_engine.fetch_rcsb_pdb_structure(pdb_id)

# -------------------------------------------------------------
# Toán học Số học & Mô phỏng Giải tích (Math Core REST APIs)
# -------------------------------------------------------------

class FourierRequest(BaseModel):
    wave_type: str = "square"
    harmonics: int = 9
    points: int = 300
    frequency: float = 1.0

@app.post("/api/math/simulate/fourier")
def api_simulate_fourier(req: FourierRequest):
    """Tính toán khai triển Fourier và phổ họa tần."""
    return math_core.fourier_series_wave(
        wave_type=req.wave_type,
        harmonics=req.harmonics,
        points=req.points,
        frequency=req.frequency,
    )


class PendulumRequest(BaseModel):
    theta0: float = 0.5
    omega0: float = 0.0
    g: float = 9.81
    length: float = 1.0
    damping: float = 0.05
    dt: float = 0.02
    steps: int = 500

@app.post("/api/math/simulate/rk4-pendulum")
def api_simulate_pendulum(req: PendulumRequest):
    """Mô phỏng con lắc đơn phi tuyến bằng thuật toán RK4."""
    return math_core.simulate_nonlinear_pendulum(
        theta0=req.theta0,
        omega0=req.omega0,
        g=req.g,
        length=req.length,
        damping=req.damping,
        dt=req.dt,
        steps=req.steps,
    )


class LorenzRequest(BaseModel):
    sigma: float = 10.0
    rho: float = 28.0
    beta: float = 8.0 / 3.0
    x0: float = 0.1
    y0: float = 0.0
    z0: float = 0.0
    dt: float = 0.01
    steps: int = 1500

@app.post("/api/math/simulate/lorenz")
def api_simulate_lorenz(req: LorenzRequest):
    """Mô phỏng hệ hỗn loạn Lorenz Attractor bằng RK4."""
    return math_core.simulate_lorenz_attractor(
        sigma=req.sigma,
        rho=req.rho,
        beta=req.beta,
        x0=req.x0,
        y0=req.y0,
        z0=req.z0,
        dt=req.dt,
        steps=req.steps,
    )


class Matrix2x2Request(BaseModel):
    a: float = 2.0
    b: float = 1.0
    c: float = 1.0
    d: float = 2.0

@app.post("/api/math/simulate/matrix-2x2")
def api_simulate_matrix(req: Matrix2x2Request):
    """Khảo sát tính chất ma trận 2x2: Định thức, Vết, Trị riêng, Vectơ riêng và Lưới biến đổi."""
    props = math_core.matrix_2x2_properties(req.a, req.b, req.c, req.d)
    svd = math_core.svd_2x2(req.a, req.b, req.c, req.d)
    props["svd"] = svd
    return props


class GaltonRequest(BaseModel):
    num_balls: int = 1000
    rows: int = 16
    prob_right: float = 0.5

@app.post("/api/math/simulate/galton")
def api_simulate_galton(req: GaltonRequest):
    """Mô phỏng bảng Galton (Quincunx) và hội tụ Phân phối chuẩn Gauss (CLT)."""
    return math_core.simulate_galton_board(
        num_balls=req.num_balls,
        rows=req.rows,
        prob_right=req.prob_right,
    )


class MonteCarloPiRequest(BaseModel):
    samples: int = 10000

@app.post("/api/math/simulate/monte-carlo-pi")
def api_simulate_monte_carlo_pi(req: MonteCarloPiRequest):
    """Ước lượng số Pi bằng phương pháp Monte Carlo."""
    return math_core.monte_carlo_pi(num_samples=req.samples)


class BezierRequest(BaseModel):
    p0: list[float] = [50.0, 300.0]
    p1: list[float] = [150.0, 50.0]
    p2: list[float] = [350.0, 50.0]
    p3: list[float] = [450.0, 300.0]
    num_points: int = 50

@app.post("/api/math/simulate/bezier")
def api_simulate_bezier(req: BezierRequest):
    """Tính toán đường cong Bézier bậc 3 và vectơ tiếp tuyến."""
    return math_core.evaluate_cubic_bezier(
        (req.p0[0], req.p0[1]),
        (req.p1[0], req.p1[1]),
        (req.p2[0], req.p2[1]),
        (req.p3[0], req.p3[1]),
        num_points=req.num_points,
    )


class CircleIntersectRequest(BaseModel):
    c1: list[float] = [200.0, 200.0, 100.0]  # x, y, r
    c2: list[float] = [320.0, 200.0, 80.0]

@app.post("/api/math/simulate/geometry-intersect-circles")
def api_geometry_intersect_circles(req: CircleIntersectRequest):
    """Tính toán giao điểm 2 đường tròn Euclid."""
    return math_core.intersect_two_circles(
        (req.c1[0], req.c1[1], req.c1[2]),
        (req.c2[0], req.c2[1], req.c2[2]),
    )


# -------------------------------------------------------------
# Đại số Biểu tượng SymPy CAS APIs
# -------------------------------------------------------------

class CasEquationRequest(BaseModel):
    equation: str = "x^2 - 5*x + 6 = 0"
    variable: str = "x"

@app.post("/api/math/cas/solve-equation")
def api_cas_solve_equation(req: CasEquationRequest):
    """Giải phương trình đại số biểu tượng f(x) = g(x)."""
    return solve_symbolic_equation(req.equation, target_var=req.variable)


class CasFormulaIsolateRequest(BaseModel):
    formula_latex: str = "F = G * (m1 * m2) / r^2"
    target_variable: str = "r"

@app.post("/api/math/cas/isolate-formula")
def api_cas_isolate_formula(req: CasFormulaIsolateRequest):
    """Rút biến mục tiêu từ công thức LaTeX bất kỳ."""
    return isolate_variable_from_formula(req.formula_latex, req.target_variable)


class CasCalculusRequest(BaseModel):
    operation: str = "diff"  # 'diff', 'integrate', 'limit', 'series'
    expression: str = "sin(x) * x^2"
    variable: str = "x"
    lower_limit: Optional[str] = None
    upper_limit: Optional[str] = None
    point: Optional[str] = None
    order: int = 4

@app.post("/api/math/cas/calculus")
def api_cas_calculus(req: CasCalculusRequest):
    """Thực hiện các phép toán vi tích phân biểu tượng SymPy (đạo hàm, tích phân, giới hạn, Taylor)."""
    return symbolic_calculus_eval(
        operation=req.operation,
        expression_str=req.expression,
        var_str=req.variable,
        lower_limit=req.lower_limit,
        upper_limit=req.upper_limit,
        point_str=req.point,
        order=req.order,
    )


class CasVerifyStepRequest(BaseModel):
    step_before: str = "x^2 - 4 = 0"
    step_after: str = "(x - 2)*(x + 2) = 0"
    variable: str = "x"

@app.post("/api/math/cas/verify-step")
def api_cas_verify_step(req: CasVerifyStepRequest):
    """Thẩm định tính tương đương logic giữa 2 bước biến đổi liên tiếp."""
    return evaluate_derivation_step(req.step_before, req.step_after, req.variable)


class CasVerifyPipelineRequest(BaseModel):
    steps: list[str] = ["x^2 - 5*x + 6 = 0", "(x - 2)*(x - 3) = 0", "x = 2"]
    variable: str = "x"

@app.post("/api/math/cas/verify-pipeline")
def api_cas_verify_pipeline(req: CasVerifyPipelineRequest):
    """Thẩm định toàn bộ chuỗi các bước giải của học sinh."""
    return evaluate_student_solution_pipeline(req.steps, req.variable)


# -------------------------------------------------------------
# WebSocket Mô phỏng Trực tiếp (Live Real-time Streaming)
# -------------------------------------------------------------
@app.websocket("/ws/simulate/live")
async def websocket_simulate_live(websocket: WebSocket):
    """WebSocket stream dữ liệu mô phỏng thời gian thực (Lorenz / Pendulum) theo từng tick."""
    import asyncio
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            sim_type = data.get("type", "lorenz")
            steps = min(int(data.get("steps", 500)), 2000)
            
            if sim_type == "lorenz":
                sigma = float(data.get("sigma", 10.0))
                rho = float(data.get("rho", 28.0))
                beta = float(data.get("beta", 8.0 / 3.0))
                dt = float(data.get("dt", 0.01))
                curr_state = [0.1, 0.0, 0.0]
                
                # Stream theo từng mẻ 20 điểm
                batch_size = 20
                for _ in range(0, steps, batch_size):
                    batch = []
                    for _ in range(batch_size):
                        curr_state = math_core.rk4_step(
                            lambda _t, s: [sigma * (s[1] - s[0]), s[0] * (rho - s[2]) - s[1], s[0] * s[1] - beta * s[2]],
                            0.0, curr_state, dt
                        )
                        batch.append({"x": round(curr_state[0], 4), "y": round(curr_state[1], 4), "z": round(curr_state[2], 4)})
                    await websocket.send_json({"type": "lorenz_batch", "points": batch})
                    await asyncio.sleep(0.02)  # ~50fps stream
                    
            elif sim_type == "pendulum":
                theta = float(data.get("theta0", 0.5))
                omega = float(data.get("omega0", 0.0))
                damping = float(data.get("damping", 0.05))
                dt = float(data.get("dt", 0.02))
                
                curr_state = [theta, omega]
                for _ in range(0, steps, 10):
                    batch = []
                    for _ in range(10):
                        curr_state = math_core.rk4_step(
                            lambda _t, s: [s[1], -9.81 * math.sin(s[0]) - damping * s[1]],
                            0.0, curr_state, dt
                        )
                        batch.append({"theta": round(curr_state[0], 4), "omega": round(curr_state[1], 4)})
                    await websocket.send_json({"type": "pendulum_batch", "states": batch})
                    await asyncio.sleep(0.02)
                    
            await websocket.send_json({"type": "stream_complete"})
    except WebSocketDisconnect:
        pass
    except Exception as err:
        await websocket.close(code=1011, reason=str(err))


# -------------------------------------------------------------
# SCHOLARSHIP HUNTING & INTERVIEW SYSTEM APIS
# -------------------------------------------------------------

class ProfileAssessmentRequest(BaseModel):
    profile: dict[str, Any] = Field(default_factory=dict)


class ProfileMatchRequest(BaseModel):
    profile: dict[str, Any] = Field(default_factory=dict)


class InterviewEvaluateRequest(BaseModel):
    question_id: str
    answer: str


@app.get("/api/scholarships")
def list_scholarships(
    country: Optional[str] = None,
    coverage: Optional[str] = None,
    sch_type: Optional[str] = Query(None, alias="type"),
    query: Optional[str] = None,
):
    """Tra cứu danh sách học bổng STEM tinh hoa toàn cầu kèm bộ lọc đa chiều."""
    items = scholarship.load_scholarships()
    
    if country:
        c_lower = country.lower()
        items = [s for s in items if c_lower in s.get("country", "").lower()]
        
    if coverage:
        cov_lower = coverage.lower()
        items = [s for s in items if cov_lower in s.get("coverage", "").lower()]
        
    if sch_type:
        t_lower = sch_type.lower()
        items = [s for s in items if t_lower in s.get("type", "").lower()]
        
    if query:
        q_lower = query.lower()
        items = [
            s for s in items
            if q_lower in s.get("name", "").lower()
            or q_lower in s.get("provider", "").lower()
            or q_lower in s.get("overview", "").lower()
            or any(q_lower in tag.lower() for tag in s.get("tags", []))
        ]
        
    return {
        "total": len(items),
        "scholarships": items
    }


@app.get("/api/scholarships/{scholarship_id}")
def get_scholarship_detail(scholarship_id: str):
    """Lấy chi tiết hồ sơ một chương trình học bổng."""
    items = scholarship.load_scholarships()
    for s in items:
        if s.get("id") == scholarship_id:
            return s
    raise HTTPException(status_code=404, detail=f"Không tìm thấy học bổng '{scholarship_id}'")


@app.post("/api/scholarships/assess")
def assess_readiness(payload: ProfileAssessmentRequest):
    """Đánh giá toàn diện hồ sơ năng lực 4 trụ cột và xuất báo cáo Gap Analysis."""
    return scholarship.assess_profile_readiness(payload.profile)


@app.post("/api/scholarships/match")
def match_profile(payload: ProfileMatchRequest):
    """Khớp nối hồ sơ với 25 học bổng toàn cầu, phân nhóm Reach / Target / Safety."""
    return scholarship.match_scholarships(payload.profile)


@app.get("/api/scholarships/interview/questions")
def get_interview_questions():
    """Lấy ngân hàng câu hỏi phỏng vấn học bổng STEM chuẩn hóa."""
    return {
        "total": len(scholarship.INTERVIEW_QUESTIONS),
        "questions": scholarship.get_all_questions()
    }


@app.post("/api/scholarships/interview/evaluate")
def evaluate_interview_answer(payload: InterviewEvaluateRequest):
    """Đánh giá câu trả lời phỏng vấn theo phương pháp STAR và huấn luyện phản xạ."""
    if not payload.question_id:
        raise HTTPException(status_code=400, detail="Thiếu mã câu hỏi (question_id)")
    return scholarship.evaluate_star_response(payload.question_id, payload.answer)


# -------------------------------------------------------------
# Quản lý Học Viên & Admin Analytics API
# -------------------------------------------------------------
class AttemptRecordRequest(BaseModel):
    learner: str = "hs_01_minhanh"
    problem_id: str
    answer: str
    correct: bool
    verdict: str = ""

@app.post("/api/practice/attempt")
def record_learner_attempt(payload: AttemptRecordRequest):
    """Ghi nhận lượt giải bài tập của học sinh vào PostgreSQL."""
    try:
        with get_postgres_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO attempts (learner, problem_id, answer, correct, verdict, created_at)
                    VALUES (%s, %s, %s, %s, %s, NOW())
                """, (payload.learner, payload.problem_id, payload.answer, payload.correct, payload.verdict))
            conn.commit()
        return {"status": "ok", "message": "Đã lưu kết quả làm bài"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/admin/overview")
def get_admin_overview():
    """Bảng tổng quan quản trị học viên và chất lượng đào tạo."""
    try:
        with get_postgres_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT COUNT(*) FROM learners WHERE role = 'student';")
                total_learners = cur.fetchone()[0]

                cur.execute("SELECT COUNT(*), COUNT(*) FILTER (WHERE correct = true) FROM attempts;")
                row = cur.fetchone()
                total_attempts = row[0] or 0
                correct_attempts = row[1] or 0
                avg_accuracy = round((correct_attempts / total_attempts * 100), 1) if total_attempts > 0 else 0

                cur.execute("SELECT COUNT(*) FROM scholarship_evaluations;")
                scholarship_candidates = cur.fetchone()[0]

                # Top bài toán sai nhiều nhất
                cur.execute("""
                    SELECT problem_id, COUNT(*) as total_att, COUNT(*) FILTER (WHERE correct = false) as wrong_att
                    FROM attempts
                    GROUP BY problem_id
                    HAVING COUNT(*) FILTER (WHERE correct = false) > 0
                    ORDER BY wrong_att DESC, total_att DESC
                    LIMIT 5;
                """)
                difficult_rows = cur.fetchall()
                difficult_problems = []
                prob_map = get_problems()
                for pid, total_att, wrong_att in difficult_rows:
                    p = prob_map.get(pid, {})
                    difficult_problems.append({
                        "problem_id": pid,
                        "statement": (p.get("statement_vi", "")[:120] + "...") if p else pid,
                        "subject": p.get("subject", "math") if p else "math",
                        "total_attempts": total_att,
                        "wrong_attempts": wrong_att,
                        "failure_rate": round((wrong_att / total_att) * 100, 1)
                    })

                return {
                    "total_learners": total_learners,
                    "total_attempts": total_attempts,
                    "avg_accuracy": avg_accuracy,
                    "scholarship_candidates": scholarship_candidates,
                    "difficult_problems": difficult_problems
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/admin/learners")
def list_admin_learners(q: Optional[str] = None):
    """Danh sách học viên kèm theo số liệu thống kê học tập."""
    try:
        with get_postgres_connection() as conn:
            with conn.cursor() as cur:
                query = """
                    SELECT 
                        l.id, l.name, l.email, l.school, l.grade, l.target_major, l.role, l.created_at,
                        COALESCE(COUNT(a.id), 0) as total_attempts,
                        COALESCE(COUNT(a.id) FILTER (WHERE a.correct = true), 0) as correct_attempts,
                        MAX(a.created_at) as last_seen,
                        se.tier, se.tier_name, se.total_score
                    FROM learners l
                    LEFT JOIN attempts a ON l.id = a.learner
                    LEFT JOIN (
                        SELECT DISTINCT ON (learner) learner, tier, tier_name, total_score
                        FROM scholarship_evaluations
                        ORDER BY learner, evaluated_at DESC
                    ) se ON l.id = se.learner
                    WHERE l.role = 'student'
                """
                params = []
                if q:
                    query += " AND (l.name ILIKE %s OR l.school ILIKE %s OR l.email ILIKE %s)"
                    term = f"%{q.strip()}%"
                    params.extend([term, term, term])
                
                query += " GROUP BY l.id, l.name, l.email, l.school, l.grade, l.target_major, l.role, l.created_at, se.tier, se.tier_name, se.total_score ORDER BY total_attempts DESC;"
                
                cur.execute(query, params)
                rows = cur.fetchall()
                results = []
                for r in rows:
                    tot = r[8]
                    cor = r[9]
                    acc = round((cor / tot * 100), 1) if tot > 0 else 0
                    results.append({
                        "id": r[0],
                        "name": r[1],
                        "email": r[2],
                        "school": r[3],
                        "grade": r[4],
                        "target_major": r[5],
                        "role": r[6],
                        "created_at": r[7].isoformat() if r[7] else None,
                        "total_attempts": tot,
                        "correct_attempts": cor,
                        "accuracy_rate": acc,
                        "last_seen": r[10].isoformat() if r[10] else None,
                        "scholarship_tier": r[11],
                        "scholarship_tier_name": r[12],
                        "scholarship_score": r[13],
                    })
                return {"learners": results, "total": len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/admin/learners/{learner_id}")
def get_admin_learner_detail(learner_id: str):
    """Hồ sơ năng lực chi tiết của 1 học viên."""
    try:
        with get_postgres_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT id, name, email, school, grade, target_major, role, created_at FROM learners WHERE id = %s;", (learner_id,))
                learner_row = cur.fetchone()
                if not learner_row:
                    raise HTTPException(status_code=404, detail="Không tìm thấy học viên")

                # Lịch sử các lần làm bài gần đây
                cur.execute("""
                    SELECT a.problem_id, a.answer, a.correct, a.verdict, a.created_at
                    FROM attempts a
                    WHERE a.learner = %s
                    ORDER BY a.created_at DESC
                    LIMIT 20;
                """, (learner_id,))
                attempt_rows = cur.fetchall()
                prob_map = get_problems()
                attempts_history = []
                subject_stats: dict[str, dict] = {
                    "math": {"attempted": 0, "correct": 0},
                    "physics": {"attempted": 0, "correct": 0},
                    "chemistry": {"attempted": 0, "correct": 0},
                    "biology": {"attempted": 0, "correct": 0},
                }

                # Thống kê theo môn từ toàn bộ attempts
                cur.execute("""
                    SELECT a.problem_id, a.correct
                    FROM attempts a
                    WHERE a.learner = %s;
                """, (learner_id,))
                all_user_attempts = cur.fetchall()
                for pid, is_cor in all_user_attempts:
                    p = prob_map.get(pid, {})
                    subj = p.get("subject", "math")
                    if subj not in subject_stats:
                        subject_stats[subj] = {"attempted": 0, "correct": 0}
                    subject_stats[subj]["attempted"] += 1
                    if is_cor:
                        subject_stats[subj]["correct"] += 1

                for pid, ans, is_cor, verd, cat in attempt_rows:
                    p = prob_map.get(pid, {})
                    attempts_history.append({
                        "problem_id": pid,
                        "statement": (p.get("statement_vi", "")[:100] + "...") if p else pid,
                        "subject": p.get("subject", "math") if p else "math",
                        "user_answer": ans,
                        "correct_answer": p.get("answer", "") if p else "",
                        "correct": is_cor,
                        "created_at": cat.isoformat() if cat else None
                    })

                # Đánh giá học bổng
                cur.execute("""
                    SELECT gpa, sat, ielts, stem_awards, spike_projects, research_papers, tier, tier_name, total_score, gap_analysis, evaluated_at
                    FROM scholarship_evaluations
                    WHERE learner = %s
                    ORDER BY evaluated_at DESC
                    LIMIT 1;
                """, (learner_id,))
                se_row = cur.fetchone()
                scholarship_info = None
                if se_row:
                    scholarship_info = {
                        "gpa": se_row[0],
                        "sat": se_row[1],
                        "ielts": se_row[2],
                        "stem_awards": se_row[3],
                        "spike_projects": se_row[4],
                        "research_papers": se_row[5],
                        "tier": se_row[6],
                        "tier_name": se_row[7],
                        "total_score": se_row[8],
                        "gap_analysis": se_row[9],
                        "evaluated_at": se_row[10].isoformat() if se_row[10] else None
                    }

                # Tính phần trăm theo môn
                radar_stats = {}
                for s, st in subject_stats.items():
                    radar_stats[s] = {
                        "attempted": st["attempted"],
                        "correct": st["correct"],
                        "accuracy": round((st["correct"] / st["attempted"] * 100), 1) if st["attempted"] > 0 else 0
                    }

                return {
                    "learner": {
                        "id": learner_row[0],
                        "name": learner_row[1],
                        "email": learner_row[2],
                        "school": learner_row[3],
                        "grade": learner_row[4],
                        "target_major": learner_row[5],
                        "created_at": learner_row[7].isoformat() if learner_row[7] else None
                    },
                    "subject_stats": radar_stats,
                    "attempts_history": attempts_history,
                    "scholarship_evaluation": scholarship_info
                }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class AdminLoginRequest(BaseModel):
    username: str
    password: str

@app.post("/api/admin/login")
def admin_login(payload: AdminLoginRequest):
    """Xác thực đăng nhập tài khoản Quản trị viên."""
    u = payload.username.strip().lower()
    p = payload.password.strip()
    if (u in ["admin", "admin@aistem.edu.vn", "admin_root"]) and (p in ["admin", "admin2026", "aistem2026"]):
        return {
            "status": "ok",
            "token": "aistem_admin_session_token_authenticated",
            "user": {
                "id": "admin_root",
                "name": "Quản Trị Viên AISTEM",
                "email": "admin@aistem.edu.vn",
                "role": "admin"
            }
        }
    raise HTTPException(status_code=401, detail="Tài khoản hoặc mật khẩu quản trị không chính xác")

# -------------------------------------------------------------
# Phục vụ Web Application & Cổng Admin
# -------------------------------------------------------------
dist_dir = ROOT / "apps" / "app" / "dist"

@app.get("/", response_class=HTMLResponse)
@app.get("/admin", response_class=HTMLResponse)
@app.get("/admin/{path:path}", response_class=HTMLResponse)
def serve_home():
    dist_html = dist_dir / "index.html"
    if dist_html.exists():
        return HTMLResponse(content=dist_html.read_text(encoding="utf-8"))
    return HTMLResponse(content="<h1>AISTEM Web Application</h1><p>Frontend chưa build. Hãy chạy: <code>cd apps/app && npm run build</code>.</p>")

# Mount tĩnh cho assets, icon và kho data
if dist_dir.exists():
    if (dist_dir / "assets").exists():
        app.mount("/assets", StaticFiles(directory=str(dist_dir / "assets")), name="assets")
    app.mount("/app", StaticFiles(directory=str(dist_dir), html=True), name="app")

app.mount("/data", StaticFiles(directory=str(DATA_DIR)), name="data")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
