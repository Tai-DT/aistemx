"""Tiến độ học và ôn giãn cách.

Trước module này vòng lặp học bị hở: hệ thống chẩn đoán được, dựng được lộ
trình, chấm được bài — nhưng không nhớ gì, nên mỗi lần mở lên là bắt đầu lại.
"""

from __future__ import annotations

import sqlite3
from datetime import datetime, timedelta

import pytest

from aistem import progress, roadmap
from aistem.grading import grade
from aistem.models import GradeRequest, RoadmapRequest
from aistem.store import problems_by_skill

LEARNER = "pytest-learner"
LESSON = "lesson.math.ap-calculus.gioi-han-khai-niem"
NOW = datetime(2026, 8, 15, 9, 0, 0)


@pytest.fixture
def learner(conn: sqlite3.Connection) -> str:
    for table in ("lesson_progress", "skill_reviews", "attempts"):
        conn.execute(f"DELETE FROM {table} WHERE learner = ?", (LEARNER,))
    conn.commit()
    return LEARNER


class TestLessonProgress:
    def test_completed_lessons_are_remembered(self, conn, learner) -> None:
        progress.complete_lesson(conn, LESSON, learner=learner, now=NOW)
        assert progress.completed_lessons(conn, learner) == {LESSON}

    def test_marking_twice_does_not_duplicate(self, conn, learner) -> None:
        progress.complete_lesson(conn, LESSON, learner=learner, now=NOW)
        progress.complete_lesson(conn, LESSON, learner=learner, now=NOW)
        assert len(progress.completed_lessons(conn, learner)) == 1

    def test_study_hours_come_from_real_lesson_durations(self, conn, learner) -> None:
        progress.complete_lesson(conn, LESSON, learner=learner, now=NOW)
        assert progress.overview(conn, learner=learner, now=NOW)["study_hours"] > 0


class TestSpacedRepetition:
    def test_correct_answers_push_the_review_further_out(self, conn, learner) -> None:
        skills = ["đổi đơn vị"]
        progress.record_practice(conn, skills, correct=True, learner=learner, now=NOW)
        first = conn.execute(
            "SELECT interval_days FROM skill_reviews WHERE learner = ?", (learner,)
        ).fetchone()["interval_days"]

        progress.record_practice(
            conn, skills, correct=True, learner=learner, now=NOW + timedelta(days=1)
        )
        second = conn.execute(
            "SELECT interval_days FROM skill_reviews WHERE learner = ?", (learner,)
        ).fetchone()["interval_days"]
        assert second > first

    def test_a_wrong_answer_brings_it_straight_back(self, conn, learner) -> None:
        skills = ["đổi đơn vị"]
        for day in range(4):
            progress.record_practice(
                conn, skills, correct=True, learner=learner, now=NOW + timedelta(days=day)
            )
        grown = conn.execute(
            "SELECT interval_days FROM skill_reviews WHERE learner = ?", (learner,)
        ).fetchone()["interval_days"]
        assert grown > 1

        progress.record_practice(
            conn, skills, correct=False, learner=learner, now=NOW + timedelta(days=10)
        )
        row = conn.execute(
            "SELECT interval_days, lapses FROM skill_reviews WHERE learner = ?", (learner,)
        ).fetchone()
        assert row["interval_days"] == 1.0
        assert row["lapses"] == 1

    def test_nothing_is_due_before_its_time(self, conn, learner) -> None:
        progress.record_practice(conn, ["đổi đơn vị"], correct=True, learner=learner, now=NOW)
        assert progress.due_skills(conn, learner=learner, now=NOW) == []
        assert progress.due_skills(conn, learner=learner, now=NOW + timedelta(days=2))

    def test_two_spellings_share_one_schedule(self, conn, learner) -> None:
        """`đổi đơn vị` và `doi-don-vi` là một kỹ năng, không phải hai."""
        progress.record_practice(conn, ["đổi đơn vị"], correct=True, learner=learner, now=NOW)
        progress.record_practice(conn, ["doi-don-vi"], correct=True, learner=learner, now=NOW)
        count = conn.execute(
            "SELECT COUNT(*) AS n FROM skill_reviews WHERE learner = ?", (learner,)
        ).fetchone()["n"]
        assert count == 1


class TestMastery:
    def test_recent_results_outweigh_old_ones(self, conn, learner) -> None:
        """Đúng ba lần tháng trước rồi sai hôm nay thì mức thạo phải xuống.

        Tỉ lệ đúng thô vẫn cho 75% và che mất chỗ hổng.
        """
        old = NOW - timedelta(days=90)
        for _ in range(3):
            conn.execute(
                "INSERT INTO attempts (learner, problem_id, correct, created_at)"
                " VALUES (?,?,?,?)",
                (learner, "prob.math.ap-calculus.0001", 1, old.strftime("%Y-%m-%d %H:%M:%S")),
            )
        conn.execute(
            "INSERT INTO attempts (learner, problem_id, correct, created_at) VALUES (?,?,?,?)",
            (learner, "prob.math.ap-calculus.0001", 0, NOW.strftime("%Y-%m-%d %H:%M:%S")),
        )
        conn.commit()
        mastery = progress.skill_mastery(conn, learner=learner, now=NOW)
        assert mastery
        assert all(entry["mastery"] < 0.5 for entry in mastery.values())

    def test_weak_skills_are_reported(self, conn, learner) -> None:
        grade(conn, GradeRequest(
            problem_id="prob.math.ap-calculus.0001", student_answer="B", learner=learner
        ))
        assert progress.weak_skills(conn, learner=learner)

    def test_geometric_mean_exposes_the_gap_an_average_hides(self) -> None:
        """Thạo 5 kỹ năng ở mức 0,9 và một kỹ năng ở mức 0,1: bài thi sẽ gãy
        đúng ở kỹ năng kia, nên con số tổng hợp phải phản ánh điều đó."""
        uneven = [0.9, 0.9, 0.9, 0.9, 0.9, 0.1]
        average = sum(uneven) / len(uneven)
        assert progress.mastery_curve(uneven) < average - 0.1

        # Đều tay thì hai cách tính gần như trùng nhau.
        even = [0.7] * 6
        assert abs(progress.mastery_curve(even) - 0.7) < 0.01


class TestGradingFeedsProgress:
    def test_grading_records_the_attempt_and_the_review(self, conn, learner) -> None:
        grade(conn, GradeRequest(
            problem_id="prob.math.ap-calculus.0001", student_answer="A", learner=learner
        ))
        attempts = conn.execute(
            "SELECT COUNT(*) AS n FROM attempts WHERE learner = ?", (learner,)
        ).fetchone()["n"]
        reviews = conn.execute(
            "SELECT COUNT(*) AS n FROM skill_reviews WHERE learner = ?", (learner,)
        ).fetchone()["n"]
        assert attempts == 1
        assert reviews > 0

    def test_correct_answers_are_recorded_as_correct(self, conn, learner) -> None:
        grade(conn, GradeRequest(
            problem_id="prob.math.ap-calculus.0001", student_answer="A", learner=learner
        ))
        row = conn.execute(
            "SELECT correct FROM attempts WHERE learner = ?", (learner,)
        ).fetchone()
        assert row["correct"] == 1


class TestRoadmapUsesProgress:
    def test_completed_lessons_shorten_the_path(self, conn, learner) -> None:
        goal = "lesson.math.ap-calculus.quy-tac-lhospital"
        before = roadmap.build(conn, RoadmapRequest(goal=goal))
        for milestone in before.milestones[:3]:
            progress.complete_lesson(conn, milestone.lesson.id, learner=learner, now=NOW)

        after = roadmap.build(conn, RoadmapRequest(goal=goal, learner=learner))
        assert after.lesson_count < before.lesson_count
        assert any("tiến độ" in w for w in after.warnings)


class TestMultiSkillMatching:
    def test_many_skills_still_return_problems(self, conn) -> None:
        """Hỏi "bài nào luyện MỘT TRONG các kỹ năng này", không phải "phủ được CẢ".

        Gộp token của mọi kỹ năng rồi đo độ phủ khiến không bài nào qua ngưỡng,
        và gợi ý biến mất đúng lúc người học có nhiều lỗ hổng nhất.
        """
        many = [
            "giới hạn lượng giác cơ bản",
            "kỹ thuật nhân chia thêm đối số",
            "phân biệt giá trị hàm và giới hạn",
            "phân loại gián đoạn",
            "khai triển Maclaurin",
            "tính giới hạn bằng chuỗi",
        ]
        for count in (1, 2, 3, 6):
            assert len(problems_by_skill(conn, many[:count], limit=10)) >= 5, count

    def test_unrelated_skill_still_matches_nothing(self, conn) -> None:
        assert problems_by_skill(conn, ["nuôi cấy mô tế bào thực vật in vitro"], limit=10) == []
