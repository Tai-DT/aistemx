"""Dựng lộ trình học từ đồ thị tiên quyết của kho bài giảng.

Kho có sẵn thứ cần thiết: 858 bài học, mỗi bài khai báo `prerequisites[]`, và
đồ thị ấy **không có chu trình** (đã kiểm) nên sắp thứ tự tô-pô được. Cộng thêm
`duration_minutes` trên từng bài và `estimated_minutes` trên từng bài tập, ta
ước lượng được thời gian thật chứ không phải đoán.

Bốn việc, theo đúng thứ tự:

1. **Phân giải mục tiêu** — người học nói "tích phân" hoặc "thi AP Calculus BC",
   không nói id. Phải dịch sang tập bài học đích.
2. **Bao đóng tiên quyết** — muốn học bài đích thì phải học những gì trước đó.
3. **Sắp thứ tự** — tô-pô, nhưng có hàng trăm thứ tự hợp lệ; chọn thứ tự **sư
   phạm** bằng cách phá hoà theo cấp học, lớp, rồi `unit`/`order` của kho.
4. **Xen bài luyện và chia buổi** — học xong lí thuyết phải làm bài ngay, và
   lịch phải vừa quỹ thời gian người học có.
"""

from __future__ import annotations

import heapq
import json
import re
import sqlite3
from collections import defaultdict
from typing import Any

from .models import (
    SUBJECT_VI,
    LearningPath,
    Milestone,
    PathItem,
    RoadmapRequest,
    StudySession,
)
from .skills import SkillMatcher
from .skills import tokens as skill_tokens
from .store.search import Filters, search
from .textnorm import fold

#: Thứ tự cấp học, dùng phá hoà khi sắp tô-pô.
_LEVEL_RANK = {"tieu-hoc": 0, "thcs": 1, "thpt": 2, "dai-hoc": 3}

_TOKEN_RE = re.compile(r"[a-z0-9]+")

#: Hai kho dùng hai thang độ khó khác nhau: bài tập ghi số 1-5, bài học ghi
#: chữ. Quy về một thang để hiển thị và sắp xếp được cùng nhau.
_LESSON_DIFFICULTY = {"co-ban": 1, "trung-binh": 2, "nang-cao": 4, "chuyen-sau": 5}


def _level_rank(level: str) -> int:
    return _LEVEL_RANK.get(level, 2)


def _difficulty(value: Any) -> int | None:
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        return _LESSON_DIFFICULTY.get(value.strip().lower())
    return None


# --------------------------------------------------------------------------- #
# 1. Phân giải mục tiêu
# --------------------------------------------------------------------------- #


def resolve_goal(
    conn: sqlite3.Connection, request: RoadmapRequest, limit: int = 6
) -> tuple[list[str], list[str]]:
    """Dịch mục tiêu của người học thành tập id bài học đích.

    Nhận bốn kiểu mục tiêu, thử theo thứ tự cụ thể dần tới mơ hồ dần:
    id bài học → id kỳ thi → từ khoá chủ đề.
    """
    goal = (request.goal or "").strip()
    notes: list[str] = []
    if not goal:
        return [], ["mục tiêu rỗng"]

    # id bài học: dùng thẳng.
    if _exists(conn, "lesson", goal):
        return [goal], notes

    # id kỳ thi: đích là các bài dạy công thức kỳ thi bắt buộc thuộc.
    if _exists(conn, "exam", goal):
        lessons = _lessons_for_exam(conn, goal, limit)
        if lessons:
            notes.append(f"Mục tiêu là kỳ thi {goal}: lấy các bài dạy công thức bắt buộc thuộc.")
            return lessons, notes
        notes.append(f"Kỳ thi {goal} chưa nối được sang bài học nào.")

    # từ khoá: tìm bài học khớp nhất.
    hits = search(
        conn,
        goal,
        filters=Filters(
            kinds=["lesson"],
            subject=request.subject,
            level=request.level,
            curriculum=request.curriculum,
        ),
        limit=limit,
    )
    if not hits:
        return [], [f"Không tìm thấy bài học nào khớp mục tiêu {goal!r}."]

    # BM25 luôn trả về *cái gì đó*, kể cả khi truy vấn là chuỗi vô nghĩa. Không
    # chặn thì người học gõ nhầm một chữ và nhận về lộ trình 40 giờ hoàn toàn
    # sai chủ đề — mà lộ trình thì trông rất thuyết phục, không ai nghi ngờ.
    relevant = [hit for hit in hits if _shares_a_word(goal, hit.title, hit.topic)]
    if not relevant:
        return [], [
            f"Mục tiêu {goal!r} không khớp rõ bài học nào trong kho. "
            "Thử nêu tên chủ đề cụ thể hơn, hoặc dùng thẳng id bài học / id kỳ thi."
        ]
    if len(relevant) < len(hits):
        notes.append(f"Bỏ {len(hits) - len(relevant)} kết quả chỉ khớp lỏng lẻo.")
    # Nói rõ đã hiểu mục tiêu thành gì. Một lộ trình 40 giờ trông rất thuyết
    # phục kể cả khi nó nhắm sai chủ đề, nên người học phải nhìn thấy ngay hệ
    # thống chọn bài đích nào để bác lại nếu sai.
    chosen = "; ".join(f"“{hit.title[:52]}”" for hit in relevant[:3])
    notes.append(
        f"Hiểu mục tiêu {goal!r} thành {len(relevant)} bài đích: {chosen}"
        + (" …" if len(relevant) > 3 else "")
    )
    return [hit.id for hit in relevant], notes


def _shares_a_word(goal: str, *texts: str) -> bool:
    """Mục tiêu và bài học có chung ít nhất một từ mang nghĩa không?"""
    wanted = {t for t in _TOKEN_RE.findall(fold(goal)) if len(t) >= 3}
    if not wanted:
        return False
    found: set[str] = set()
    for text in texts:
        found.update(_TOKEN_RE.findall(fold(text or "")))
    return bool(wanted & found)


def _exists(conn: sqlite3.Connection, kind: str, rid: str) -> bool:
    return (
        conn.execute(
            "SELECT 1 FROM records WHERE kind = ? AND rid = ? LIMIT 1", (kind, rid)
        ).fetchone()
        is not None
    )


def _lessons_for_exam(conn: sqlite3.Connection, exam_id: str, limit: int) -> list[str]:
    """Bài học dạy nhiều công thức mà kỳ thi này bắt buộc thuộc nhất."""
    rows = conn.execute(
        "SELECT e2.src_id AS lesson_id, COUNT(*) AS n"
        " FROM edges e1"
        " JOIN edges e2 ON e2.dst_id = e1.dst_id AND e2.rel = 'uses_formula'"
        "               AND e2.src_kind = 'lesson'"
        " WHERE e1.src_id = ? AND e1.rel = 'must_memorize'"
        " GROUP BY e2.src_id ORDER BY n DESC LIMIT ?",
        (exam_id, limit),
    ).fetchall()
    return [row["lesson_id"] for row in rows]


# --------------------------------------------------------------------------- #
# 2. Bao đóng tiên quyết
# --------------------------------------------------------------------------- #


def prerequisite_graph(conn: sqlite3.Connection) -> dict[str, list[str]]:
    """`bài học -> danh sách bài phải học trước`."""
    graph: dict[str, list[str]] = defaultdict(list)
    for row in conn.execute(
        "SELECT src_id, dst_id FROM edges WHERE rel = 'prerequisite'"
    ):
        graph[row["src_id"]].append(row["dst_id"])
    return graph


def required_lessons(
    graph: dict[str, list[str]], targets: list[str], known: set[str]
) -> tuple[set[str], int]:
    """Mọi bài phải học để tới được đích, trừ những bài đã nắm.

    Bài đã nắm bị cắt **cùng toàn bộ nhánh tiên quyết của nó**: đã hiểu đạo hàm
    hàm hợp thì không cần quay lại định nghĩa đạo hàm. Đây là chỗ lộ trình cá
    nhân hoá khác hẳn một mục lục sách.
    """
    needed: set[str] = set()
    skipped = 0
    stack = [t for t in targets if t not in known]
    skipped += len(targets) - len(stack)

    while stack:
        node = stack.pop()
        if node in needed:
            continue
        needed.add(node)
        for parent in graph.get(node, ()):
            if parent in known:
                skipped += 1
                continue
            if parent not in needed:
                stack.append(parent)
    return needed, skipped


# --------------------------------------------------------------------------- #
# 3. Sắp thứ tự
# --------------------------------------------------------------------------- #


def _lesson_rows(conn: sqlite3.Connection, ids: set[str]) -> dict[str, dict[str, Any]]:
    if not ids:
        return {}
    out: dict[str, dict[str, Any]] = {}
    ids_list = list(ids)
    for start in range(0, len(ids_list), 400):
        chunk = ids_list[start : start + 400]
        placeholders = ",".join("?" * len(chunk))
        for row in conn.execute(
            f"SELECT rid, payload FROM records WHERE kind = 'lesson' AND rid IN ({placeholders})",
            chunk,
        ):
            out[row["rid"]] = json.loads(row["payload"])
    return out


def _sort_key(record: dict[str, Any]) -> tuple:
    """Khoá phá hoà khi nhiều bài cùng sẵn sàng học.

    Cấp học trước, rồi lớp nhỏ trước, rồi theo `unit`/`order` mà kho đã đánh —
    tức là theo đúng trình tự sách giáo khoa, không phải theo id.
    """
    grades = record.get("grades") or [13]
    return (
        _level_rank(record.get("level", "")),
        min(grades) if grades else 13,
        record.get("unit") or "",
        record.get("order") if record.get("order") is not None else 999,
        record.get("id", ""),
    )


def topological_order(
    graph: dict[str, list[str]], ids: set[str], records: dict[str, dict[str, Any]]
) -> list[str]:
    """Sắp thứ tự học: tiên quyết luôn đứng trước, phá hoà theo trình tự sách.

    Dùng hàng đợi ưu tiên chứ không phải hàng đợi thường: sắp tô-pô có rất
    nhiều thứ tự hợp lệ, và thứ tự "hợp lệ" bất kỳ thì nhảy cóc giữa các môn và
    các cấp — đúng về mặt logic nhưng không ai học nổi.
    """
    remaining = {node: [p for p in graph.get(node, ()) if p in ids] for node in ids}
    dependents: dict[str, list[str]] = defaultdict(list)
    for node, parents in remaining.items():
        for parent in parents:
            dependents[parent].append(node)

    counts = {node: len(parents) for node, parents in remaining.items()}
    heap = [
        (*_sort_key(records.get(node, {"id": node})), node)
        for node, count in counts.items()
        if count == 0
    ]
    heapq.heapify(heap)

    order: list[str] = []
    while heap:
        node = heapq.heappop(heap)[-1]
        order.append(node)
        for child in dependents.get(node, ()):
            counts[child] -= 1
            if counts[child] == 0:
                heapq.heappush(heap, (*_sort_key(records.get(child, {"id": child})), child))

    # Còn sót nghĩa là có chu trình. Kho hiện tại sạch, nhưng dữ liệu thì thay
    # đổi, và im lặng bỏ rơi vài bài thì lộ trình thiếu mà không ai biết.
    leftover = [node for node in ids if node not in set(order)]
    order.extend(sorted(leftover, key=lambda n: _sort_key(records.get(n, {"id": n}))))
    return order


# --------------------------------------------------------------------------- #
# 4. Bài luyện và chia buổi
# --------------------------------------------------------------------------- #


def practice_for_lesson(
    conn: sqlite3.Connection,
    lesson: dict[str, Any],
    count: int,
    *,
    exclude: set[str],
    weak_matcher: SkillMatcher | None = None,
    weak_tokens: set[str] | None = None,
) -> list[dict[str, Any]]:
    """Bài tập luyện ngay sau một bài giảng, độ khó tăng dần.

    Lấy theo **công thức mà bài giảng dạy**, không theo từ khoá: đó là liên kết
    chắc chắn nhất trong kho. Sắp theo độ khó rồi bốc rải đều từ dễ tới khó —
    ba bài cùng mức dễ thì luyện xong vẫn không lên được đâu.
    """
    formulas = [f for f in (lesson.get("formulas") or []) if isinstance(f, str)]
    if not formulas or count <= 0:
        return []

    placeholders = ",".join("?" * len(formulas))
    rows = conn.execute(
        "SELECT r.rid, r.payload, COALESCE(r.difficulty, 3) AS difficulty, COUNT(*) AS shared"
        " FROM edges e JOIN records r ON r.kind = 'problem' AND r.rid = e.src_id"
        f" WHERE e.rel = 'uses_formula' AND e.dst_id IN ({placeholders})"
        " GROUP BY r.rid ORDER BY shared DESC, difficulty ASC",
        formulas,
    ).fetchall()

    candidates = [row for row in rows if row["rid"] not in exclude]
    if not candidates:
        return []

    # Ưu tiên bài chạm đúng kỹ năng đang yếu, nếu người học có khai báo.
    if weak_matcher is not None and weak_tokens:
        def weakness(row: sqlite3.Row) -> float:
            record = json.loads(row["payload"])
            found: set[str] = set()
            for skill in record.get("skills") or []:
                found.update(skill_tokens(skill))
            shared = found & weak_tokens
            return -sum(weak_matcher.weight(t) for t in shared)

        candidates.sort(key=weakness)

    by_difficulty: dict[int, list[sqlite3.Row]] = defaultdict(list)
    for row in candidates:
        by_difficulty[int(row["difficulty"])].append(row)

    picked: list[dict[str, Any]] = []
    # Rải từ dễ tới khó; hết mức nào thì lấy bù ở mức gần nhất.
    for difficulty in sorted(by_difficulty):
        if len(picked) >= count:
            break
        picked.append(json.loads(by_difficulty[difficulty].pop(0)["payload"]))
    for row in candidates:
        if len(picked) >= count:
            break
        record = json.loads(row["payload"])
        if record["id"] not in {p["id"] for p in picked}:
            picked.append(record)
    return picked[:count]


def pace(items: list[PathItem], minutes_per_session: int) -> list[StudySession]:
    """Cắt danh sách việc thành các buổi vừa quỹ thời gian.

    Không cắt đôi một việc: một bài giảng 45 phút thì phải nằm trọn trong một
    buổi. Buổi có thể vượt hạn mức một chút, còn hơn để người học dừng giữa bài.
    """
    sessions: list[StudySession] = []
    current = StudySession(index=1)
    for item in items:
        if current.items and current.minutes + item.minutes > minutes_per_session:
            sessions.append(current)
            current = StudySession(index=len(sessions) + 1)
        current.items.append(item)
        current.minutes = round(current.minutes + item.minutes, 1)
    if current.items:
        sessions.append(current)
    return sessions


# --------------------------------------------------------------------------- #
# Ghép lại
# --------------------------------------------------------------------------- #


def _lesson_item(record: dict[str, Any], reason: str) -> PathItem:
    return PathItem(
        kind="lesson",
        id=record["id"],
        title=record.get("title_vi") or record.get("title_en") or record["id"],
        minutes=float(record.get("duration_minutes") or 45),
        difficulty=_difficulty(record.get("difficulty")),
        subject=record.get("subject", ""),
        level=record.get("level", ""),
        topic=record.get("unit", ""),
        reason=reason,
    )


def _problem_item(record: dict[str, Any], reason: str) -> PathItem:
    return PathItem(
        kind="problem",
        id=record["id"],
        title=(record.get("statement_vi") or record["id"])[:160],
        minutes=float(record.get("estimated_minutes") or 5),
        difficulty=_difficulty(record.get("difficulty")),
        subject=record.get("subject", ""),
        level=record.get("level", ""),
        topic=record.get("topic", ""),
        reason=reason,
    )


def build(conn: sqlite3.Connection, request: RoadmapRequest) -> LearningPath:
    """Dựng lộ trình học hoàn chỉnh cho một mục tiêu."""
    targets, notes = resolve_goal(conn, request)
    path = LearningPath(goal=request.goal, goal_lessons=targets, warnings=list(notes))
    if not targets:
        path.summary = "Chưa dựng được lộ trình: không phân giải được mục tiêu."
        return path

    graph = prerequisite_graph(conn)
    known = set(request.known_lessons)
    weak = list(request.weak_skills)

    # Có tiến độ thật thì dùng tiến độ thật. Bắt người học tự khai "tôi đã học
    # bài nào" là cách chắc chắn nhất để tính năng cá nhân hoá không ai dùng.
    if request.learner:
        from . import progress

        tracked = progress.completed_lessons(conn, request.learner)
        if tracked:
            known |= tracked
            path.warnings.append(
                f"Lấy {len(tracked)} bài đã học từ tiến độ của {request.learner!r}."
            )
        if not weak:
            weak = progress.weak_skills(conn, learner=request.learner)
            if weak:
                path.warnings.append(
                    "Ưu tiên luyện các kỹ năng đang yếu: " + ", ".join(weak[:4])
                )

    needed, skipped = required_lessons(graph, targets, known)
    path.skipped_known = skipped

    records = _lesson_rows(conn, needed)
    order = topological_order(graph, needed, records)

    if len(order) > request.max_lessons:
        # Cắt từ đầu: phần đầu là nền, bỏ phần đuôi thì lộ trình vẫn liền mạch,
        # còn bỏ phần đầu thì người học vấp ngay bài thứ nhất.
        path.truncated = True
        path.warnings.append(
            f"Lộ trình cần {len(order)} bài, đã cắt còn {request.max_lessons} bài đầu. "
            "Tăng max_lessons nếu muốn xem trọn."
        )
        order = order[: request.max_lessons]

    weak_tokens: set[str] = set()
    for skill in weak:
        weak_tokens.update(skill_tokens(skill))
    matcher = SkillMatcher() if weak_tokens else None

    used_problems: set[str] = set()
    items: list[PathItem] = []
    target_set = set(targets)

    for index, lesson_id in enumerate(order, start=1):
        record = records.get(lesson_id)
        if record is None:
            continue
        reason = (
            "bài đích của mục tiêu"
            if lesson_id in target_set
            else "cần trước để học được bài sau"
        )
        lesson_item = _lesson_item(record, reason)
        milestone = Milestone(
            order=index,
            lesson=lesson_item,
            unit=record.get("unit", ""),
            prerequisites_met=[p for p in graph.get(lesson_id, ()) if p in needed],
        )
        items.append(lesson_item)

        for problem in practice_for_lesson(
            conn,
            record,
            request.practice_per_lesson,
            exclude=used_problems,
            weak_matcher=matcher,
            weak_tokens=weak_tokens,
        ):
            used_problems.add(problem["id"])
            item = _problem_item(problem, f"luyện công thức của bài {lesson_item.title[:40]}")
            milestone.practice.append(item)
            items.append(item)

        path.milestones.append(milestone)

    path.lesson_count = len(path.milestones)
    path.practice_count = len(used_problems)
    path.total_minutes = round(sum(item.minutes for item in items), 1)
    path.sessions = pace(items, request.minutes_per_session)
    path.subjects = sorted({m.lesson.subject for m in path.milestones if m.lesson.subject})
    path.summary = _summarize(path, request)
    return path


def _summarize(path: LearningPath, request: RoadmapRequest) -> str:
    if not path.milestones:
        return "Lộ trình rỗng."
    subjects = ", ".join(SUBJECT_VI.get(s, s) for s in path.subjects)
    lines = [
        f"{path.lesson_count} bài học và {path.practice_count} bài luyện, "
        f"tổng {path.total_hours} giờ, chia {len(path.sessions)} buổi "
        f"({request.minutes_per_session} phút mỗi buổi)."
    ]
    if subjects:
        lines.append(f"Môn: {subjects}.")
    first, last = path.milestones[0].lesson, path.milestones[-1].lesson
    lines.append(f"Bắt đầu từ “{first.title[:60]}”, kết thúc ở “{last.title[:60]}”.")
    if path.skipped_known:
        lines.append(f"Đã bỏ qua {path.skipped_known} bài bạn khai là đã nắm.")
    return " ".join(lines)
