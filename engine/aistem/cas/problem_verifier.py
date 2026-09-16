"""Hệ thống Kiểm chứng Khoa học Tự động (CAS Problem Verification Pipeline) cho AISTEM.

Sử dụng SymPy và hệ thống CAS độc lập để đối chiếu tính toán:
1. Giải toán số học và kiểm định kết quả (Numeric Dien-So).
2. Phân giải đáp án Trắc nghiệm (Multiple Choice / Trac-Nghiem) khớp với lời giải và định luật.
3. Rà soát từng bước biến đổi đại số / phương trình hoá học (Solution Steps).
4. Cập nhật kết quả kiểm chứng (cas_verified, cas_status, cas_details) trực tiếp vào PostgreSQL.
"""
from __future__ import annotations

import concurrent.futures
import json
import time
from typing import Any, Callable, Dict, List, Optional, Tuple

import psycopg
from psycopg.rows import dict_row

from ..textnorm import extract_number
from .verify import verify_answer


def verify_problem_data(
    problem: Dict[str, Any],
    budget: float = 0.8
) -> Tuple[bool, str, Dict[str, Any]]:
    """Kiểm chứng một bài toán độc lập qua SymPy CAS.

    Trả về:
    - cas_verified (bool): True nếu đáp số hoặc các bước được SymPy xác thực độc lập
    - cas_status (str): 'verified' | 'refuted' | 'inconclusive' | 'unchecked' | 'error'
    - cas_details (dict): Chi tiết đầy đủ về kết quả tính toán CAS
    """
    try:
        ptype = problem.get("type") or "trac-nghiem"
        ans_str = str(problem.get("answer") or "")
        ans_num = problem.get("answer_numeric")
        steps = problem.get("solution_steps") or []
        tolerance = problem.get("tolerance")
        unit = problem.get("answer_unit")
        choices = problem.get("choices") or []

        # Nếu là trắc nghiệm và answer là nhãn A, B, C, D: phân giải nội dung phương án
        if ptype == "trac-nghiem" and ans_str.strip().upper() in ("A", "B", "C", "D"):
            target_key = ans_str.strip().upper()
            for c in choices:
                if isinstance(c, dict) and str(c.get("key", "")).strip().upper() == target_key:
                    choice_text = str(c.get("text") or "")
                    ans_str = choice_text
                    if ans_num is None:
                        ans_num = extract_number(choice_text)
                    break

        v = verify_answer(
            answer=ans_str,
            answer_numeric=ans_num,
            steps=steps,
            tolerance=tolerance,
            expected_unit=unit,
            budget=budget,
        )

        is_verified = (v.answer_status == "verified") or (
            v.trustworthy and v.steps_verified > 0 and v.steps_refuted == 0
        )
        status = v.answer_status
        if status == "unchecked" and is_verified:
            status = "verified"

        details = {
            "answer_status": v.answer_status,
            "answer_detail": v.answer_detail,
            "answer_mismatch": v.answer_mismatch,
            "cas_value": v.cas_value,
            "cas_expression": v.cas_expression,
            "unit_status": v.unit_status,
            "steps_total": v.steps_total,
            "steps_verified": v.steps_verified,
            "steps_refuted": v.steps_refuted,
            "steps_inconclusive": v.steps_inconclusive,
            "trustworthy": v.trustworthy,
        }
        return is_verified, status, details

    except Exception as exc:
        details = {
            "error": str(exc),
            "answer_status": "error",
            "trustworthy": False,
        }
        return False, "error", details


def verify_problems_pipeline(
    pg_conn: psycopg.Connection,
    subject: Optional[str] = None,
    ptype: Optional[str] = None,
    source_file: Optional[str] = None,
    limit: Optional[int] = None,
    batch_size: int = 100,
    max_workers: int = 4,
    recheck: bool = False,
    budget: float = 0.8,
    on_progress: Optional[Callable[[int, int, Dict[str, Any]], None]] = None,
) -> Dict[str, Any]:
    """Chạy toàn bộ pipeline kiểm định CAS trên cơ sở dữ liệu PostgreSQL.

    Hỗ trợ xử lý đa luồng (multi-threading) song song để đạt tốc độ cao.
    """
    t0 = time.perf_counter()

    # Xây dựng câu truy vấn lấy danh sách bài toán cần kiểm chứng
    where_parts = []
    params: List[Any] = []

    if not recheck:
        where_parts.append("cas_verified = FALSE")
    if subject:
        where_parts.append("subject = %s")
        params.append(subject)
    if ptype:
        where_parts.append("type = %s")
        params.append(ptype)
    if source_file:
        where_parts.append("source_file = %s")
        params.append(source_file)


    where_sql = (" WHERE " + " AND ".join(where_parts)) if where_parts else ""
    limit_sql = f" LIMIT {int(limit)}" if limit else ""

    select_sql = f"""
        SELECT id, subject, level, topic, type, answer, answer_numeric, answer_unit,
               tolerance, choices, solution_steps, formulas_used
        FROM problems
        {where_sql}
        ORDER BY id
        {limit_sql}
    """

    with pg_conn.cursor(row_factory=dict_row) as cur:
        cur.execute(select_sql, params)
        rows = cur.fetchall()

    total_candidates = len(rows)
    if total_candidates == 0:
        return {
            "total": 0,
            "verified": 0,
            "refuted": 0,
            "inconclusive": 0,
            "unchecked": 0,
            "error": 0,
            "elapsed_seconds": 0.0,
            "throughput": 0.0,
        }

    verified_count = 0
    refuted_count = 0
    inconclusive_count = 0
    unchecked_count = 0
    error_count = 0

    update_batch: List[Dict[str, Any]] = []
    processed_count = 0

    update_sql = """
        UPDATE problems
        SET cas_verified = %(cas_verified)s,
            cas_status = %(cas_status)s,
            cas_details = %(cas_details)s::jsonb,
            updated_at = NOW()
        WHERE id = %(id)s;
    """

    def _worker(item: Dict[str, Any]) -> Dict[str, Any]:
        is_ver, status, details = verify_problem_data(item, budget=budget)
        return {
            "id": item["id"],
            "cas_verified": is_ver,
            "cas_status": status,
            "cas_details": json.dumps(details),
            "status_raw": status,
            "is_verified": is_ver,
        }

    # Chia các nhóm batch để xử lý và ghi vào DB
    for i in range(0, total_candidates, batch_size):
        chunk = rows[i : i + batch_size]
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(executor.map(_worker, chunk))

        batch_updates = []
        for r in results:
            processed_count += 1
            if r["is_verified"]:
                verified_count += 1
            elif r["status_raw"] == "refuted":
                refuted_count += 1
            elif r["status_raw"] == "inconclusive":
                inconclusive_count += 1
            elif r["status_raw"] == "error":
                error_count += 1
            else:
                unchecked_count += 1

            batch_updates.append({
                "id": r["id"],
                "cas_verified": r["cas_verified"],
                "cas_status": r["cas_status"],
                "cas_details": r["cas_details"],
            })

        with pg_conn.cursor() as cur:
            cur.executemany(update_sql, batch_updates)
        pg_conn.commit()

        if on_progress:
            on_progress(processed_count, total_candidates, {
                "verified": verified_count,
                "refuted": refuted_count,
            })

    elapsed = time.perf_counter() - t0
    throughput = round(processed_count / elapsed, 1) if elapsed > 0 else 0.0

    return {
        "total": processed_count,
        "verified": verified_count,
        "refuted": refuted_count,
        "inconclusive": inconclusive_count,
        "unchecked": unchecked_count,
        "error": error_count,
        "elapsed_seconds": round(elapsed, 2),
        "throughput": throughput,
    }
