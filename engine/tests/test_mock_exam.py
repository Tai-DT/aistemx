"""Sinh và chấm đề thi thử theo bản thiết kế kỳ thi."""

from __future__ import annotations

import sqlite3

import pytest

from aistem import mock_exam
from aistem.models import MockExamRequest, MockExamSubmission

AP = "exam.ap-calculus-bc"


class TestBlueprintCounts:
    def test_counts_add_up_to_the_total(self) -> None:
        """Chia rồi làm tròn từng phần thì tổng lệch; phần dư phải được phát lại."""
        weights = {"a": 7.0, "b": 7.0, "c": 18.0, "d": 17.0, "e": 11.0}
        for total in (5, 10, 20, 33, 45):
            counts = mock_exam.blueprint_counts(weights, total)
            assert sum(counts.values()) == total

    def test_heavier_topics_get_more_questions(self) -> None:
        counts = mock_exam.blueprint_counts({"nhẹ": 5.0, "nặng": 45.0}, 20)
        assert counts["nặng"] > counts["nhẹ"]

    def test_empty_inputs_are_safe(self) -> None:
        assert mock_exam.blueprint_counts({}, 10) == {}
        assert mock_exam.blueprint_counts({"a": 1.0}, 0) == {}


class TestGeneration:
    def test_respects_the_requested_size(self, conn: sqlite3.Connection) -> None:
        exam = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=15))
        assert len(exam.questions) <= 15
        assert exam.coverage

    def test_same_seed_gives_the_same_exam(self, conn: sqlite3.Connection) -> None:
        first = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=12, seed=3))
        second = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=12, seed=3))
        assert [q.problem_id for q in first.questions] == [q.problem_id for q in second.questions]

    def test_different_seeds_give_different_exams(self, conn: sqlite3.Connection) -> None:
        first = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=12, seed=1))
        second = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=12, seed=2))
        assert [q.problem_id for q in first.questions] != [q.problem_id for q in second.questions]

    def test_no_question_appears_twice(self, conn: sqlite3.Connection) -> None:
        exam = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=30))
        ids = [q.problem_id for q in exam.questions]
        assert len(ids) == len(set(ids))

    def test_solutions_are_hidden_unless_asked(self, conn: sqlite3.Connection) -> None:
        """Đề thi thử mà kèm sẵn đáp án thì không còn là thi thử."""
        exam = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=8))
        assert all(not q.answer and not q.solution_steps for q in exam.questions)

        with_answers = mock_exam.generate(
            conn, MockExamRequest(exam_id=AP, question_count=8, include_solutions=True)
        )
        assert any(q.answer for q in with_answers.questions)

    def test_shortfall_is_announced_not_padded(self, conn: sqlite3.Connection) -> None:
        """Lấy bừa bài chủ đề khác cho đủ số câu khiến người học tưởng đã ôn kín."""
        exam = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=100))
        short = [c for c in exam.coverage if not c.complete]
        if short:
            assert any("thiếu" in w for w in exam.warnings)
        # Dù thiếu thì cũng không được bịa thêm câu.
        assert len(exam.questions) == sum(c.got for c in exam.coverage)

    def test_difficulty_ceiling_is_respected(self, conn: sqlite3.Connection) -> None:
        exam = mock_exam.generate(
            conn, MockExamRequest(exam_id=AP, question_count=15, difficulty_max=2)
        )
        assert all(q.difficulty is None or q.difficulty <= 2 for q in exam.questions)

    def test_unknown_exam_raises(self, conn: sqlite3.Connection) -> None:
        with pytest.raises(KeyError):
            mock_exam.generate(conn, MockExamRequest(exam_id="exam.khong-ton-tai"))

    @pytest.mark.parametrize("exam_id", ["exam.ap-calculus-bc", "exam.ib-physics-hl"])
    def test_works_for_more_than_one_blueprint_style(
        self, conn: sqlite3.Connection, exam_id: str
    ) -> None:
        """AP đánh chủ đề bằng `Unit N`, IB bằng chữ cái — cả hai phải chạy."""
        exam = mock_exam.generate(conn, MockExamRequest(exam_id=exam_id, question_count=8))
        assert exam.questions
        assert sum(c.got for c in exam.coverage) == len(exam.questions)


class TestGrading:
    def test_scores_only_what_it_can_grade(self, conn: sqlite3.Connection) -> None:
        """Câu không tự chấm được mà tính thành sai thì hạ điểm oan."""
        exam = mock_exam.generate(
            conn, MockExamRequest(exam_id=AP, question_count=12, include_solutions=True)
        )
        submission = MockExamSubmission(
            exam_id=AP,
            learner="pytest-exam",
            answers={q.problem_id: q.answer for q in exam.questions},
        )
        result = mock_exam.grade_exam(conn, submission)
        graded = result.total - result.uncheckable
        assert result.total == len(exam.questions)
        assert graded >= 0
        if graded:
            # Nộp đúng đáp án của kho thì phần chấm được phải gần như đúng hết.
            assert result.percent >= 80

    def test_breaks_the_score_down_by_blueprint_topic(self, conn: sqlite3.Connection) -> None:
        exam = mock_exam.generate(conn, MockExamRequest(exam_id=AP, question_count=12))
        submission = MockExamSubmission(
            exam_id=AP, learner="pytest-exam",
            answers={q.problem_id: "A" for q in exam.questions},
        )
        result = mock_exam.grade_exam(conn, submission)
        assert result.per_topic
        assert sum(t.total for t in result.per_topic) <= result.total
