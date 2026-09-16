"""Sinh đề thi thử theo đúng bản thiết kế của kỳ thi thật.

36 hồ sơ trong `data/exams/` không phải mô tả suông: mỗi hồ sơ có `sections`
(số câu, thời lượng, có được dùng máy tính không), `topic_weights` là phần trăm
từng chủ đề cộng lại đúng 100, và `scoring` mô tả cách quy điểm. Đó là một bản
thiết kế đủ chi tiết để bốc bài từ ngân hàng 1 258 bài cho ra một đề **cùng tỉ
trọng** với đề thật.

Nguyên tắc xuyên suốt: **thiếu thì nói thiếu**. Kho không phủ đều mọi chủ đề,
nên có phần đề sẽ không đủ bài. Lấy bừa bài chủ đề khác cho đủ số câu là cách
chắc chắn nhất để người học tưởng mình đã ôn kín trong khi có mảng chưa đụng
tới. Ở đây phần thiếu được ghi thẳng vào `coverage` và `warnings`.
"""

from __future__ import annotations

import json
import random
import re
import sqlite3
from typing import Any

from .grading import grade
from .models import (
    ExamQuestion,
    GradeRequest,
    MockExam,
    MockExamRequest,
    MockExamResult,
    MockExamSubmission,
    Problem,
    TopicCoverage,
    TopicScore,
)
from .store.db import load_record
from .store.search import Filters, search

#: `Unit 3: Differentiation …` trong trọng số kỳ thi ứng với tag `unit-3` trên
#: bài tập. Đây là mối nối chắc nhất giữa hai kho.
_UNIT_RE = re.compile(r"^\s*(?:unit|chủ đề|chuyên đề|phần)\s*(\d+)", re.IGNORECASE)


def load_exam(conn: sqlite3.Connection, exam_id: str) -> dict[str, Any]:
    row = conn.execute(
        "SELECT payload FROM records WHERE kind = 'exam' AND rid = ?", (exam_id,)
    ).fetchone()
    if row is None:
        raise KeyError(f"Không có hồ sơ kỳ thi {exam_id!r} trong kho.")
    return json.loads(row["payload"])


def blueprint_counts(weights: dict[str, float], total: int) -> dict[str, int]:
    """Chia số câu theo trọng số, giữ đúng tổng.

    Chia rồi làm tròn từng phần thì tổng lệch; ở đây phần dư được phát lại cho
    các chủ đề có phần thập phân lớn nhất, đúng lối chia ghế Hamilton.
    """
    if not weights or total <= 0:
        return {}
    scale = sum(weights.values()) or 1.0
    exact = {topic: weight / scale * total for topic, weight in weights.items()}
    counts = {topic: int(value) for topic, value in exact.items()}
    leftover = total - sum(counts.values())
    for topic, _ in sorted(exact.items(), key=lambda kv: -(kv[1] - int(kv[1])))[:leftover]:
        counts[topic] += 1
    return counts


def _candidates(
    conn: sqlite3.Connection,
    exam: dict[str, Any],
    topic: str,
    *,
    difficulty_max: int | None,
) -> list[dict[str, Any]]:
    """Bài tập ứng với một chủ đề trong bản thiết kế.

    Thử tag `unit-N` trước vì đó là mối nối chính xác; không có thì mới tìm
    theo tên chủ đề.
    """
    subject = exam.get("subject") or None
    curriculum = exam.get("curriculum")
    curriculum = curriculum[0] if isinstance(curriculum, list) and curriculum else None

    unit = _UNIT_RE.match(topic)
    if unit:
        tag = f"unit-{unit.group(1)}"
        sql = (
            "SELECT payload FROM records WHERE kind = 'problem'"
            " AND EXISTS (SELECT 1 FROM json_each(tags) t WHERE t.value = ?)"
        )
        params: list[Any] = [tag]
        if subject:
            sql += " AND subject = ?"
            params.append(subject)
        if curriculum:
            sql += " AND curriculum LIKE ?"
            params.append(f'%"{curriculum}"%')
        if difficulty_max is not None:
            sql += " AND COALESCE(difficulty, 3) <= ?"
            params.append(difficulty_max)
        rows = conn.execute(sql, params).fetchall()
        if rows:
            return [json.loads(row["payload"]) for row in rows]

    # Không có tag thì tìm theo tên chủ đề, bỏ phần "Unit N:" ở đầu.
    query = _UNIT_RE.sub("", topic).lstrip(" :-—")
    hits = search(
        conn,
        query or topic,
        filters=Filters(
            kinds=["problem"],
            subject=subject,
            curriculum=curriculum,
            difficulty_max=difficulty_max,
        ),
        limit=40,
        include_record=True,
    )
    return [hit.record for hit in hits if hit.record]


def _question(order: int, record: dict[str, Any], topic: str, keep_solution: bool) -> ExamQuestion:
    problem = Problem.model_validate(record)
    return ExamQuestion(
        order=order,
        problem_id=problem.id,
        topic=topic,
        statement=problem.statement_vi or problem.statement_en,
        type=problem.type,
        choices=[choice.model_dump() for choice in problem.choices],
        difficulty=problem.difficulty,
        minutes=problem.estimated_minutes,
        answer=problem.answer if keep_solution else "",
        solution_steps=(
            [step.model_dump(exclude_none=True) for step in problem.solution_steps]
            if keep_solution
            else []
        ),
    )


def generate(conn: sqlite3.Connection, request: MockExamRequest) -> MockExam:
    """Bốc một đề thi thử theo bản thiết kế của kỳ thi."""
    exam = load_exam(conn, request.exam_id)
    weights = exam.get("topic_weights") or {}
    weights = {k: float(v) for k, v in weights.items() if isinstance(v, (int, float))}

    sections = exam.get("sections") or []
    blueprint_total = 0
    for section in sections:
        try:
            blueprint_total += int(str(section.get("question_count", "0")).split("-")[0])
        except (TypeError, ValueError):
            continue
    total = request.question_count or min(blueprint_total or 20, 40)

    result = MockExam(
        exam_id=request.exam_id,
        name=exam.get("name", request.exam_id),
        subject=exam.get("subject", ""),
        blueprint_questions=blueprint_total,
        requested_questions=total,
        sections=[
            {
                "name": section.get("name", ""),
                "question_count": section.get("question_count"),
                "duration_minutes": section.get("duration_minutes"),
                "calculator": section.get("calculator"),
                "weight_percent": section.get("weight_percent"),
            }
            for section in sections
        ],
    )
    if not weights:
        result.warnings.append(
            f"Hồ sơ {request.exam_id} không có topic_weights nên không bốc đề theo tỉ trọng được."
        )
        return result

    targets = blueprint_counts(weights, total)
    rng = random.Random(request.seed)
    used: set[str] = set()
    order = 0

    for topic, wanted in sorted(targets.items(), key=lambda kv: -kv[1]):
        if wanted <= 0:
            continue
        pool = [
            record
            for record in _candidates(conn, exam, topic, difficulty_max=request.difficulty_max)
            if record.get("id") not in used
        ]
        rng.shuffle(pool)
        picked = pool[:wanted]
        for record in picked:
            used.add(record["id"])
            order += 1
            result.questions.append(
                _question(order, record, topic, request.include_solutions)
            )
        result.coverage.append(
            TopicCoverage(
                topic=topic,
                weight_percent=round(weights[topic], 2),
                wanted=wanted,
                got=len(picked),
                available=len(pool),
            )
        )

    short = [c for c in result.coverage if c.got < c.wanted]
    if short:
        missing = sum(c.wanted - c.got for c in short)
        result.warnings.append(
            f"Kho thiếu {missing} câu so với bản thiết kế, ở {len(short)} chủ đề: "
            + ", ".join(f"{c.topic[:38]} ({c.got}/{c.wanted})" for c in short[:4])
            + ". Đề vẫn dùng được nhưng chưa phủ đúng tỉ trọng đề thật."
        )

    result.questions.sort(key=lambda q: q.order)
    result.total_minutes = round(sum(q.minutes for q in result.questions), 1)
    result.summary = (
        f"{len(result.questions)} câu, ước tính {result.total_minutes:.0f} phút, "
        f"phủ {len([c for c in result.coverage if c.got])}/{len(result.coverage)} chủ đề "
        f"của bản thiết kế."
    )
    return result


# --------------------------------------------------------------------------- #
# Chấm đề thi thử
# --------------------------------------------------------------------------- #


def grade_exam(
    conn: sqlite3.Connection, submission: MockExamSubmission
) -> MockExamResult:
    """Chấm một bài thi thử, kèm phân tích theo chủ đề của bản thiết kế.

    Điểm phần trăm tính trên **số câu chấm được**, không trên tổng số câu: kho
    có những câu hệ thống thành thật nói là không tự chấm được, và tính chúng
    thành sai sẽ hạ điểm oan.
    """
    exam = load_exam(conn, submission.exam_id)
    weights = exam.get("topic_weights") or {}

    result = MockExamResult(exam_id=submission.exam_id, total=len(submission.answers), correct=0)
    per_topic: dict[str, list[bool]] = {}

    for problem_id, answer in submission.answers.items():
        try:
            outcome = grade(
                conn,
                GradeRequest(
                    problem_id=problem_id, student_answer=answer, learner=submission.learner
                ),
            )
        except KeyError:
            continue
        result.per_question.append(outcome)
        if outcome.verdict == "khong-cham-duoc":
            result.uncheckable += 1
            continue
        if outcome.correct:
            result.correct += 1
        result.raw_score += outcome.score

        record = load_record(conn, "problem", problem_id) or {}
        topic = _blueprint_topic(record, weights)
        per_topic.setdefault(topic, []).append(outcome.correct)

    graded = result.total - result.uncheckable
    result.percent = round(result.correct / graded * 100, 1) if graded else 0.0
    result.per_topic = [
        TopicScore(
            topic=topic,
            correct=sum(values),
            total=len(values),
            weight_percent=round(float(weights.get(topic, 0)), 2),
        )
        for topic, values in sorted(per_topic.items())
    ]
    result.weakest_topics = [
        score.topic
        for score in sorted(result.per_topic, key=lambda s: s.accuracy)
        if score.accuracy < 0.5
    ][:5]

    scoring = exam.get("scoring")
    if isinstance(scoring, dict) and scoring.get("description"):
        result.scoring_note = str(scoring["description"])[:300]

    lines = [f"Đúng {result.correct}/{graded} câu chấm được ({result.percent:.0f}%)."]
    if result.uncheckable:
        lines.append(f"{result.uncheckable} câu cần người chấm, không tính vào điểm.")
    if result.weakest_topics:
        lines.append("Yếu nhất ở: " + ", ".join(t[:44] for t in result.weakest_topics[:3]) + ".")
    result.summary = " ".join(lines)
    return result


def _blueprint_topic(record: dict[str, Any], weights: dict[str, Any]) -> str:
    """Bài này thuộc chủ đề nào của bản thiết kế."""
    tags = {str(t) for t in record.get("tags") or []}
    for topic in weights:
        unit = _UNIT_RE.match(topic)
        if unit and f"unit-{unit.group(1)}" in tags:
            return topic
    return record.get("topic") or "(chưa xếp chủ đề)"
