"""Tiến độ học và lịch ôn giãn cách.

Trước module này vòng lặp học bị hở: hệ thống chẩn đoán được lỗ hổng, dựng được
lộ trình, chấm được bài — nhưng không nhớ gì cả. Mỗi lần mở lên là một lần bắt
đầu lại, và người học phải tự khai "tôi đã học bài nào" thì lộ trình mới cá
nhân hoá được. Ở đây ta ghi lại và dùng chính lịch sử ấy.

Hai loại tiến độ, cố ý tách riêng:

* **đã đọc bài giảng** (`lesson_progress`) — mới là đã tiếp xúc.
* **làm đúng bài tập** (`attempts`) — mới là bằng chứng đã hiểu.

Ôn giãn cách tính theo **kỹ năng**, không theo từng bài tập: người học cần nhớ
*cách làm*, không cần nhớ một đề cụ thể. Thuật toán theo lối SM-2: làm đúng thì
giãn khoảng ôn ra theo hệ số dễ, làm sai thì kéo về ôn lại ngay và hạ hệ số dễ.
"""

from __future__ import annotations

import math
import sqlite3
from collections import defaultdict
from datetime import datetime, timedelta
from typing import Any

from . import skills as skills_module
from .models import Hit, RecordKind
from .textnorm import fold

#: Khoảng ôn cho hai lần đầu, tính bằng ngày. Từ lần thứ ba trở đi khoảng cách
#: nhân với hệ số dễ, đúng lối SM-2.
_FIRST_INTERVALS = (1.0, 3.0)
_MIN_EASE = 1.3
_MAX_INTERVAL_DAYS = 180.0

#: Mức thạo dưới ngưỡng này thì coi là còn yếu và được lộ trình ưu tiên luyện.
_WEAK_THRESHOLD = 0.6

#: Kết quả cũ nói ít hơn kết quả mới. Nửa đời 30 ngày: một lần làm đúng cách đây
#: một tháng chỉ còn nặng bằng nửa một lần làm đúng hôm nay.
_RECENCY_HALF_LIFE_DAYS = 30.0


def _now(now: datetime | None = None) -> datetime:
    return now or datetime.now()


def _stamp(value: datetime) -> str:
    return value.strftime("%Y-%m-%d %H:%M:%S")


def _parse(value: str) -> datetime:
    for pattern in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, pattern)
        except (ValueError, TypeError):
            continue
    return datetime.min


# --------------------------------------------------------------------------- #
# Ghi tiến độ
# --------------------------------------------------------------------------- #


def complete_lesson(
    conn: sqlite3.Connection,
    lesson_id: str,
    *,
    learner: str = "local",
    status: str = "done",
    now: datetime | None = None,
) -> None:
    """Đánh dấu đã học xong một bài giảng."""
    conn.execute(
        "INSERT INTO lesson_progress (learner, lesson_id, status, completed_at)"
        " VALUES (?,?,?,?)"
        " ON CONFLICT(learner, lesson_id) DO UPDATE SET"
        " status = excluded.status, completed_at = excluded.completed_at",
        (learner, lesson_id, status, _stamp(_now(now))),
    )
    conn.commit()


def completed_lessons(conn: sqlite3.Connection, learner: str = "local") -> set[str]:
    return {
        row["lesson_id"]
        for row in conn.execute(
            "SELECT lesson_id FROM lesson_progress WHERE learner = ? AND status = 'done'",
            (learner,),
        )
    }


# --------------------------------------------------------------------------- #
# Ôn giãn cách
# --------------------------------------------------------------------------- #


def _schedule(
    repetitions: int, ease: float, correct: bool, quality: float
) -> tuple[int, float, float]:
    """Bước lên lịch kiểu SM-2. Trả (số lần lặp, hệ số dễ, khoảng ôn tính bằng ngày).

    `quality` trong khoảng 0-1: chấm nửa điểm (gần đúng, đúng một phần) cho ra
    khoảng ôn ngắn hơn hẳn làm đúng hoàn toàn — vì "gần đúng" nghĩa là chưa chắc.
    """
    if not correct:
        # Sai thì về ôn lại ngay hôm sau và hạ hệ số dễ. Không đưa về 0 hẳn:
        # quên một lần không xoá sạch những lần nhớ trước đó.
        return 0, max(_MIN_EASE, ease - 0.2), _FIRST_INTERVALS[0]

    ease = max(_MIN_EASE, ease + 0.1 - (1 - quality) * 0.6)
    repetitions += 1
    if repetitions <= len(_FIRST_INTERVALS):
        interval = _FIRST_INTERVALS[repetitions - 1]
    else:
        interval = _FIRST_INTERVALS[-1] * (ease ** (repetitions - len(_FIRST_INTERVALS)))
    return repetitions, ease, min(interval, _MAX_INTERVAL_DAYS)


def record_practice(
    conn: sqlite3.Connection,
    problem_skills: list[str],
    *,
    correct: bool,
    score: float = 1.0,
    learner: str = "local",
    now: datetime | None = None,
) -> list[str]:
    """Cập nhật lịch ôn cho mọi kỹ năng mà bài vừa làm chạm tới."""
    moment = _now(now)
    touched: list[str] = []
    for skill in problem_skills:
        key = skills_module.canonical(skill) or fold(skill)
        if not key:
            continue
        row = conn.execute(
            "SELECT repetitions, ease, lapses FROM skill_reviews"
            " WHERE learner = ? AND skill_key = ?",
            (learner, key),
        ).fetchone()
        repetitions = row["repetitions"] if row else 0
        ease = row["ease"] if row else 2.5
        lapses = row["lapses"] if row else 0

        repetitions, ease, interval = _schedule(repetitions, ease, correct, score)
        if not correct:
            lapses += 1
        due = moment + timedelta(days=interval)
        conn.execute(
            "INSERT INTO skill_reviews (learner, skill_key, skill_label, repetitions, ease,"
            " interval_days, due_at, last_seen_at, lapses) VALUES (?,?,?,?,?,?,?,?,?)"
            " ON CONFLICT(learner, skill_key) DO UPDATE SET"
            " skill_label = excluded.skill_label, repetitions = excluded.repetitions,"
            " ease = excluded.ease, interval_days = excluded.interval_days,"
            " due_at = excluded.due_at, last_seen_at = excluded.last_seen_at,"
            " lapses = excluded.lapses",
            (learner, key, skill, repetitions, ease, interval,
             _stamp(due), _stamp(moment), lapses),
        )
        touched.append(key)
    conn.commit()
    return touched


def due_skills(
    conn: sqlite3.Connection,
    *,
    learner: str = "local",
    limit: int = 20,
    now: datetime | None = None,
) -> list[dict[str, Any]]:
    """Kỹ năng đã tới hạn ôn, quá hạn lâu nhất xếp trước."""
    rows = conn.execute(
        "SELECT * FROM skill_reviews WHERE learner = ? AND due_at <= ?"
        " ORDER BY due_at ASC LIMIT ?",
        (learner, _stamp(_now(now)), limit),
    ).fetchall()
    moment = _now(now)
    return [
        {
            "skill": row["skill_label"] or row["skill_key"],
            "skill_key": row["skill_key"],
            "due_at": row["due_at"],
            "overdue_days": round((moment - _parse(row["due_at"])).total_seconds() / 86400, 1),
            "repetitions": row["repetitions"],
            "lapses": row["lapses"],
            "ease": round(row["ease"], 2),
        }
        for row in rows
    ]


# --------------------------------------------------------------------------- #
# Mức thạo
# --------------------------------------------------------------------------- #


def skill_mastery(
    conn: sqlite3.Connection, *, learner: str = "local", now: datetime | None = None
) -> dict[str, dict[str, Any]]:
    """Mức thạo từng kỹ năng, suy từ lịch sử làm bài có **giảm trọng theo thời gian**.

    Không dùng tỉ lệ đúng thô: làm đúng ba lần hồi tháng trước rồi sai hôm nay
    thì mức thạo phải xuống, mà tỉ lệ thô lại vẫn 75%. Mỗi kết quả được nhân
    với hệ số suy giảm theo nửa đời 30 ngày.
    """
    rows = conn.execute(
        "SELECT a.problem_id, a.correct, a.created_at, ps.skill, ps.skill_key"
        " FROM attempts a JOIN problem_skills ps ON ps.problem_id = a.problem_id"
        " WHERE a.learner = ?",
        (learner,),
    ).fetchall()
    if not rows:
        return {}

    moment = _now(now)
    earned: dict[str, float] = defaultdict(float)
    possible: dict[str, float] = defaultdict(float)
    labels: dict[str, list[str]] = defaultdict(list)
    counts: dict[str, int] = defaultdict(int)

    for row in rows:
        key = row["skill_key"] or fold(row["skill"])
        age_days = max(0.0, (moment - _parse(row["created_at"])).total_seconds() / 86400)
        weight = 0.5 ** (age_days / _RECENCY_HALF_LIFE_DAYS)
        earned[key] += weight * (1.0 if row["correct"] else 0.0)
        possible[key] += weight
        labels[key].append(row["skill"])
        counts[key] += 1

    out: dict[str, dict[str, Any]] = {}
    for key, total in possible.items():
        mastery = earned[key] / total if total else 0.0
        out[key] = {
            "skill": skills_module.display_name(labels[key]),
            "mastery": round(mastery, 3),
            "attempts": counts[key],
            "weak": mastery < _WEAK_THRESHOLD,
        }
    return out


def weak_skills(
    conn: sqlite3.Connection, *, learner: str = "local", limit: int = 10,
    now: datetime | None = None,
) -> list[str]:
    """Tên các kỹ năng đang yếu nhất, để lộ trình ưu tiên luyện."""
    mastery = skill_mastery(conn, learner=learner, now=now)
    weak = [entry for entry in mastery.values() if entry["weak"]]
    weak.sort(key=lambda e: (e["mastery"], -e["attempts"]))
    return [entry["skill"] for entry in weak[:limit]]


# --------------------------------------------------------------------------- #
# Tổng hợp
# --------------------------------------------------------------------------- #


def overview(
    conn: sqlite3.Connection, *, learner: str = "local", now: datetime | None = None
) -> dict[str, Any]:
    """Bức tranh tiến độ của một người học."""
    done = completed_lessons(conn, learner)
    attempts = conn.execute(
        "SELECT COUNT(*) AS n, SUM(correct) AS ok FROM attempts WHERE learner = ?",
        (learner,),
    ).fetchone()
    total_attempts = attempts["n"] or 0
    correct = attempts["ok"] or 0
    mastery = skill_mastery(conn, learner=learner, now=now)
    weak = [entry for entry in mastery.values() if entry["weak"]]

    minutes = conn.execute(
        "SELECT COALESCE(SUM(json_extract(r.payload, '$.duration_minutes')), 0) AS m"
        " FROM lesson_progress p JOIN records r ON r.kind = 'lesson' AND r.rid = p.lesson_id"
        " WHERE p.learner = ? AND p.status = 'done'",
        (learner,),
    ).fetchone()["m"]

    return {
        "learner": learner,
        "lessons_done": len(done),
        "study_hours": round((minutes or 0) / 60, 1),
        "attempts": total_attempts,
        "correct": correct,
        "accuracy": round(correct / total_attempts, 3) if total_attempts else 0.0,
        "skills_tracked": len(mastery),
        "skills_weak": len(weak),
        "reviews_due": len(due_skills(conn, learner=learner, limit=1000, now=now)),
    }


def review_problems(
    conn: sqlite3.Connection,
    *,
    learner: str = "local",
    limit: int = 10,
    now: datetime | None = None,
) -> list[Hit]:
    """Bài tập cụ thể để ôn các kỹ năng đã tới hạn.

    Ưu tiên bài **chưa từng làm**: ôn tập mà gặp lại đúng đề cũ thì người học
    nhớ đáp án chứ chưa chắc nhớ cách làm.
    """
    from .store.search import problems_by_skill

    due = due_skills(conn, learner=learner, limit=limit, now=now)
    if not due:
        return []
    seen = {
        row["problem_id"]
        for row in conn.execute("SELECT DISTINCT problem_id FROM attempts WHERE learner = ?",
                                (learner,))
    }
    hits = problems_by_skill(
        conn, [entry["skill"] for entry in due], limit=limit * 3, exclude=sorted(seen)
    )
    if len(hits) < limit:
        hits += [
            hit
            for hit in problems_by_skill(conn, [e["skill"] for e in due], limit=limit * 3)
            if hit.id not in {h.id for h in hits}
        ]
    return [hit for hit in hits if hit.kind is RecordKind.PROBLEM][:limit]


def mastery_curve(values: list[float]) -> float:
    """Gộp nhiều mức thạo thành một con số, thiên về mức thấp nhất.

    Trung bình cộng che mất chỗ hổng: thạo 5 kỹ năng ở mức 0,9 và một kỹ năng ở
    mức 0,1 thì trung bình vẫn 0,77, trong khi bài thi sẽ gãy đúng ở kỹ năng kia.
    """
    if not values:
        return 0.0
    return round(math.prod(v + 1e-6 for v in values) ** (1 / len(values)), 3)
