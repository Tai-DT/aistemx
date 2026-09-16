"""Lệnh đo chất lượng.

Bản thân `audit` cũng cần test: nó là thứ ta dựa vào để biết hệ thống có lành
hay không, nên nó hỏng thầm thì mọi phép đo sau đó đều vô nghĩa.
"""

from __future__ import annotations

import sqlite3

from aistem import audit


def test_audit_runs_and_reports_every_check(conn: sqlite3.Connection) -> None:
    report = audit.run(conn, limit=40, skill_sample=25)
    assert set(report.checks) == {
        "lien-ket", "lo-trinh", "cham-bai", "do-nghiem", "kiem-chung",
        "do-nghiem-kiem-chung", "goi-y-luyen-tap",
    }
    for check in report.checks.values():
        assert "mô tả" in check and "ok" in check


def test_corpus_links_are_intact(conn: sqlite3.Connection) -> None:
    report = audit.run(conn, limit=5, skill_sample=5)
    links = report.checks["lien-ket"]
    assert links["cạnh treo"] == 0
    assert links["minh hoạ mồ côi"] == 0


def test_grading_invariant_holds_on_a_sample(conn: sqlite3.Connection) -> None:
    """Nộp đúng đáp án kho công bố thì phải được chấm đúng."""
    report = audit.run(conn, limit=200, skill_sample=10)
    assert report.checks["cham-bai"]["ok"], report.checks["cham-bai"]


def test_grader_is_still_strict(conn: sqlite3.Connection) -> None:
    """Nới cho đúng dễ nới quá tay — phép đo này canh chiều ngược lại."""
    report = audit.run(conn, limit=200, skill_sample=10)
    assert report.checks["do-nghiem"]["tỉ lệ bắt"] >= 0.9


def test_practice_recommendations_are_usable(conn: sqlite3.Connection) -> None:
    report = audit.run(conn, limit=5, skill_sample=120)
    coverage = report.checks["goi-y-luyen-tap"]
    assert coverage["trung bình bài gợi được"] >= 3
    assert coverage["tỉ lệ vô dụng"] <= 0.15


def test_report_is_serialisable(conn: sqlite3.Connection) -> None:
    import json

    report = audit.run(conn, limit=20, skill_sample=10)
    json.dumps(report.as_dict(), ensure_ascii=False)


def test_roadmap_invariants_hold(conn: sqlite3.Connection) -> None:
    """Đồ thị tiên quyết phải phi chu trình; có chu trình thì không tồn tại
    thứ tự học nào hợp lệ và bộ sắp xếp âm thầm bỏ rơi vài bài."""
    report = audit.run(conn, limit=5, skill_sample=80)
    check = report.checks["lo-trinh"]
    assert check["chu trình"] == 0
    assert check["vi phạm thứ tự"] == 0
    assert check["không dựng được"] == 0
