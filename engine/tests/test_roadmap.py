"""Dựng lộ trình học.

Bất biến quan trọng nhất: **tiên quyết luôn đứng trước**. Một lộ trình vi phạm
nó thì người học vấp ngay bài đầu tiên, mà nhìn bảng thì vẫn thấy hợp lí — đúng
loại hỏng không tự lộ ra.
"""

from __future__ import annotations

import sqlite3

import pytest

from aistem import roadmap
from aistem.models import RoadmapRequest

GOALS = [
    "lesson.math.ap-calculus.quy-tac-lhospital",
    "định luật Ohm",
    "di truyền Mendel",
    "exam.ap-calculus-bc",
]


def _positions(path) -> dict[str, int]:
    return {m.lesson.id: i for i, m in enumerate(path.milestones)}


class TestPrerequisiteOrder:
    @pytest.mark.parametrize("goal", GOALS)
    def test_prerequisites_always_come_first(self, conn: sqlite3.Connection, goal: str) -> None:
        graph = roadmap.prerequisite_graph(conn)
        path = roadmap.build(conn, RoadmapRequest(goal=goal, max_lessons=60))
        assert path.milestones, goal
        pos = _positions(path)
        for lesson_id, index in pos.items():
            for prerequisite in graph.get(lesson_id, ()):
                if prerequisite in pos:
                    assert pos[prerequisite] < index, (
                        f"{lesson_id} đứng trước tiên quyết {prerequisite}"
                    )

    def test_graph_is_acyclic(self, conn: sqlite3.Connection) -> None:
        """Có chu trình thì không tồn tại thứ tự học nào hợp lệ."""
        graph = roadmap.prerequisite_graph(conn)
        colour: dict[str, int] = {}
        cycles: list[list[str]] = []

        def visit(node: str, stack: list[str]) -> None:
            colour[node] = 1
            stack.append(node)
            for parent in graph.get(node, ()):
                if colour.get(parent) == 1:
                    cycles.append([*stack[stack.index(parent):], parent])
                elif colour.get(parent, 0) == 0:
                    visit(parent, stack)
            stack.pop()
            colour[node] = 2

        for node in list(graph):
            if colour.get(node, 0) == 0:
                visit(node, [])
        assert cycles == []


class TestGoalResolution:
    def test_lesson_id_is_used_directly(self, conn: sqlite3.Connection) -> None:
        goal = "lesson.math.ap-calculus.quy-tac-lhospital"
        targets, _ = roadmap.resolve_goal(conn, RoadmapRequest(goal=goal))
        assert targets == [goal]

    def test_exam_id_resolves_through_required_formulas(self, conn: sqlite3.Connection) -> None:
        targets, notes = roadmap.resolve_goal(conn, RoadmapRequest(goal="exam.ap-calculus-bc"))
        assert targets and all(t.startswith("lesson.") for t in targets)
        assert any("kỳ thi" in n for n in notes)

    @pytest.mark.parametrize("goal", ["qwerty asdf zxcv", "xyzzy plugh", ""])
    def test_nonsense_goal_is_refused_not_guessed(
        self, conn: sqlite3.Connection, goal: str
    ) -> None:
        """BM25 luôn trả về *cái gì đó*; một lộ trình sai chủ đề trông rất thuyết phục.

        Từ chối bằng hai đường: hoặc không tìm thấy gì, hoặc tìm thấy nhưng
        không chia sẻ từ nào với mục tiêu. Cả hai đều phải cho lộ trình rỗng.
        """
        targets, notes = roadmap.resolve_goal(conn, RoadmapRequest(goal=goal))
        assert targets == []
        assert notes

    def test_refused_goal_yields_an_empty_path_not_a_wrong_one(
        self, conn: sqlite3.Connection
    ) -> None:
        path = roadmap.build(conn, RoadmapRequest(goal="qwerty asdf zxcv"))
        assert path.milestones == []
        assert path.total_minutes == 0
        assert "Chưa dựng được" in path.summary

    def test_chosen_targets_are_reported_back(self, conn: sqlite3.Connection) -> None:
        path = roadmap.build(conn, RoadmapRequest(goal="định luật Ohm"))
        assert any("Hiểu mục tiêu" in w for w in path.warnings)


class TestPersonalisation:
    def test_known_lessons_prune_their_whole_branch(self, conn: sqlite3.Connection) -> None:
        goal = "lesson.math.ap-calculus.quy-tac-lhospital"
        full = roadmap.build(conn, RoadmapRequest(goal=goal))
        assert full.lesson_count > 2

        known = [m.lesson.id for m in full.milestones[:3]]
        pruned = roadmap.build(conn, RoadmapRequest(goal=goal, known_lessons=known))
        assert pruned.lesson_count < full.lesson_count
        assert not (set(known) & {m.lesson.id for m in pruned.milestones})

    def test_knowing_the_goal_itself_empties_the_path(self, conn: sqlite3.Connection) -> None:
        goal = "lesson.math.ap-calculus.quy-tac-lhospital"
        path = roadmap.build(conn, RoadmapRequest(goal=goal, known_lessons=[goal]))
        assert path.lesson_count == 0


class TestShape:
    def test_practice_follows_each_lesson(self, conn: sqlite3.Connection) -> None:
        path = roadmap.build(
            conn, RoadmapRequest(goal=GOALS[0], practice_per_lesson=2)
        )
        assert any(m.practice for m in path.milestones)
        for milestone in path.milestones:
            assert len(milestone.practice) <= 2
            assert all(p.kind == "problem" for p in milestone.practice)

    def test_no_problem_is_repeated(self, conn: sqlite3.Connection) -> None:
        path = roadmap.build(conn, RoadmapRequest(goal="tích phân", max_lessons=30))
        seen = [p.id for m in path.milestones for p in m.practice]
        assert len(seen) == len(set(seen))

    def test_sessions_respect_the_time_budget(self, conn: sqlite3.Connection) -> None:
        path = roadmap.build(conn, RoadmapRequest(goal=GOALS[0], minutes_per_session=60))
        assert path.sessions
        for session_ in path.sessions:
            # Một buổi được vượt hạn mức vì việc cuối, nhưng phần trước phải vừa.
            if len(session_.items) > 1:
                before_last = session_.minutes - session_.items[-1].minutes
                assert before_last <= 60

    def test_totals_add_up(self, conn: sqlite3.Connection) -> None:
        path = roadmap.build(conn, RoadmapRequest(goal=GOALS[0]))
        from_milestones = sum(m.minutes for m in path.milestones)
        assert abs(from_milestones - path.total_minutes) < 0.5
        assert abs(sum(s.minutes for s in path.sessions) - path.total_minutes) < 1.0

    def test_truncation_is_announced(self, conn: sqlite3.Connection) -> None:
        path = roadmap.build(conn, RoadmapRequest(goal="tích phân", max_lessons=3))
        assert path.lesson_count <= 3
        if path.truncated:
            assert any("đã cắt" in w for w in path.warnings)
