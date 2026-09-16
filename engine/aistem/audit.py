"""Đo chất lượng hệ thống bằng cách chạy nó ngược lại trên chính kho.

Đây là cách tìm lỗi hiệu quả nhất ở dự án này, hơn hẳn test viết tay. Lí do:
test viết tay chỉ kiểm những trường hợp người viết **nghĩ ra được**, còn kho
7 424 bản ghi chứa đủ mọi cách viết mà không ai ngồi đoán hết nổi — dấu phẩy
thập phân Việt Nam, phân số, mũ Unicode, đơn vị chuyên ngành, nhãn dính số.

Ba phép đo, mỗi phép dựa trên một **bất biến** phải đúng nếu hệ thống lành:

1. *chấm bài* — nộp đúng đáp án mà kho công bố thì phải được chấm đúng.
   Lần đo đầu: 436/1258 bài trượt (35%).
2. *kiểm chứng CAS* — lời giải trong kho đã qua kiểm định, nên số bước bị bác
   bỏ phải rất nhỏ. Lần đo đầu: 294 bước, gần hết là báo oan.
3. *gợi ý luyện tập* — mỗi kỹ năng phải gợi được vài bài để luyện.
   Lần đo đầu: 95% kỹ năng gợi được không quá một bài.

Chạy lại sau mỗi lần kho mở rộng: `aistem audit`.
"""

from __future__ import annotations

import json
import random
import re
import sqlite3
import time
from collections import Counter
from dataclasses import dataclass, field
from typing import Any

from . import quantities, roadmap
from .cas import verify_answer
from .cas.parse import abandoned_count
from .config import settings
from .grading import grade_problem
from .models import Problem, RoadmapRequest
from .store.search import problems_by_skill
from .textnorm import fold


@dataclass
class Finding:
    """Một bản ghi làm hệ thống tự mâu thuẫn — tức là một lỗi cần xem."""

    check: str
    record_id: str
    detail: str


@dataclass
class AuditReport:
    checks: dict[str, dict[str, Any]] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)
    elapsed_s: float = 0.0

    @property
    def healthy(self) -> bool:
        """Mọi phép đo có nằm trong ngưỡng chấp nhận được không?"""
        return all(check.get("ok", True) for check in self.checks.values())

    def as_dict(self) -> dict[str, Any]:
        return {
            "healthy": self.healthy,
            "checks": self.checks,
            "findings": [f.__dict__ for f in self.findings[:40]],
            "findings_total": len(self.findings),
            "elapsed_s": round(self.elapsed_s, 1),
        }


def _load_problems(conn: sqlite3.Connection, limit: int | None, seed: int) -> list[Problem]:
    rows = conn.execute("SELECT payload FROM records WHERE kind = 'problem'").fetchall()
    problems = [Problem.model_validate(json.loads(row["payload"])) for row in rows]
    if limit and limit < len(problems):
        random.Random(seed).shuffle(problems)
        return problems[:limit]
    return problems


def check_grading(problems: list[Problem], report: AuditReport) -> None:
    """Bất biến: nộp đúng đáp án kho công bố thì phải được chấm đúng."""
    correct = uncheckable = 0
    wrong: list[Problem] = []
    methods: Counter = Counter()

    for problem in problems:
        result = grade_problem(problem, problem.answer)
        methods[result.method] += 1
        if result.verdict == "khong-cham-duoc":
            uncheckable += 1
        elif result.correct:
            correct += 1
        else:
            wrong.append(problem)
            report.findings.append(
                Finding("cham-bai", problem.id, f"{result.verdict}: {result.detail[:110]}")
            )

    total = len(problems) or 1
    report.checks["cham-bai"] = {
        "mô tả": "nộp đúng đáp án của kho thì phải được chấm đúng",
        "tổng": len(problems),
        "chấm đúng": correct,
        "không chấm được": uncheckable,
        "chấm oan": len(wrong),
        "tỉ lệ chấm oan": round(len(wrong) / total, 4),
        "phương pháp": dict(methods),
        # Ngưỡng 1%: dưới mức này thì phần còn lại là ký pháp cá biệt, không
        # phải lỗi hệ thống.
        "ok": len(wrong) / total <= 0.01,
    }


def check_strictness(problems: list[Problem], report: AuditReport) -> None:
    """Bất biến ngược: nới cho đúng thì dễ nới quá tay, phải kiểm cả chiều này."""
    checkable = [p for p in problems if p.answer_numeric not in (None, 0)]
    caught = 0
    for problem in checkable:
        wrong_answer = str(problem.answer_numeric * 1.6)
        if not grade_problem(problem, wrong_answer).correct:
            caught += 1
    total = len(checkable) or 1
    report.checks["do-nghiem"] = {
        "mô tả": "nộp đáp án lệch 60% thì phải bị bắt",
        "số bài kiểm được": len(checkable),
        "bắt được": caught,
        "tỉ lệ bắt": round(caught / total, 4),
        "ok": caught / total >= 0.9,
    }


#: Ngân sách kiểm chứng khi chạy hàng loạt. Mặc định của `verify_answer` là 20
#: giây — hợp lí cho một request đơn lẻ, nhưng quét cả kho thì chỉ cần vài chục
#: bài chạm trần là lượt đo kéo dài hàng chục phút. Ở đây ta chấp nhận bỏ sót
#: vài bước khó đổi lấy một phép đo chạy xong trong vài phút.
_BATCH_VERIFY_BUDGET = 1.5


def check_verification(
    problems: list[Problem], report: AuditReport, budget: float = _BATCH_VERIFY_BUDGET
) -> None:
    """Bất biến: lời giải trong kho đã kiểm định, nên bước bị bác bỏ phải hiếm."""
    steps: Counter = Counter()
    answers: Counter = Counter()
    refuted_answers = 0

    for problem in problems:
        result = verify_answer(
            answer=problem.answer,
            answer_numeric=problem.answer_numeric,
            steps=[s.model_dump() for s in problem.solution_steps],
            tolerance=quantities.relative_tolerance(
                problem.tolerance, problem.answer_numeric, settings.default_tolerance
            ),
            budget=budget,
        )
        answers[result.answer_status] += 1
        if result.answer_status == "refuted":
            refuted_answers += 1
            report.findings.append(
                Finding("kiem-chung", problem.id, f"đáp số: {result.answer_detail[:110]}")
            )
        for check in result.steps:
            steps[check.status] += 1
            if check.status == "refuted":
                report.findings.append(
                    Finding(
                        "kiem-chung",
                        problem.id,
                        f"bước {check.index + 1}: {check.detail[:90]}",
                    )
                )

    total_steps = sum(steps.values()) or 1
    report.checks["kiem-chung"] = {
        "mô tả": "CAS bác bỏ bước hoặc đáp số của lời giải đã kiểm định",
        "đáp số": dict(answers),
        "bước": dict(steps),
        "tỉ lệ bước bị bác bỏ": round(steps["refuted"] / total_steps, 4),
        "đáp số bị bác bỏ": refuted_answers,
        # Mỗi luồng bỏ dở là một phép tính SymPy vẫn đang chạy và vẫn ăn CPU.
        # Con số này lớn nghĩa là kho có cụm bài mà CAS xử lí rất nặng.
        "luồng CAS bỏ dở": abandoned_count(),
        "ok": steps["refuted"] / total_steps <= 0.03 and refuted_answers <= len(problems) * 0.01,
    }


#: Con số "tự do" trong một biểu thức. Loại trừ số trong chỉ số dưới (`x_2`),
#: số mũ (`^{2}`) và số dính ngay sau chữ cái (`H2O`): sửa chúng là đổi tên đại
#: lượng chứ không phải làm sai một phép tính.
_FREE_NUMBER_RE = re.compile(r"(?<![A-Za-z_^{\\])(?<!\d)(\d+(?:\{,\}\d+|[.,]\d+)?)(?!\d)")


def _corrupt(latex: str, limit: int = 3) -> list[str]:
    """Vài phiên bản của một bước, mỗi bản làm hỏng đúng một con số."""
    out: list[str] = []
    for match in list(_FREE_NUMBER_RE.finditer(latex))[:limit]:
        text = match.group(1)
        digits = re.sub(r"[^\d]", "", text)
        if not digits or len(digits) > 12:
            continue
        # Đổi chữ số đầu để chắc chắn lệch xa hơn mọi dung sai làm tròn.
        broken = text.replace(digits[0], "9" if digits[0] != "9" else "2", 1)
        if broken != text:
            out.append(latex[: match.start(1)] + broken + latex[match.end(1) :])
    return out


def check_verification_sensitivity(
    problems: list[Problem], report: AuditReport, sample: int = 40, budget: float = 3.0
) -> None:
    """Bất biến ngược cho bộ kiểm chứng: nhãn "đã kiểm" phải có thực chất.

    `do-nghiem` đã canh chiều này cho bộ **chấm bài**, nhưng bộ **kiểm chứng**
    thì chưa có gì canh. Thiếu nó thì "nới cho đỡ báo oan" và "nới tới mức xác
    nhận khống" trông giống hệt nhau trên mọi con số báo cáo — trong khi xác
    nhận khống còn nguy hiểm hơn báo oan: người học được bảo là bước này đã
    kiểm rồi, trong khi chưa có gì được kiểm cả.

    Phép đo: lấy một bước mà CAS đã xác nhận, làm hỏng một con số trong đó, chạy
    lại **cả lời giải** (bước nối tiếp chỉ có nghĩa khi còn vế phải của bước
    trước), rồi đòi cái nhãn "verified" phải biến mất. Không đòi phải chuyển
    thành `refuted`: ở bước có liên từ suy luận hệ thống cố ý không kết tội bao
    giờ, nên đòi như thế là đòi sai.
    """
    from .cas.parse import reset_deadline, set_deadline
    from .cas.verify import check_steps

    caught = hollow = 0
    used = 0

    for problem in problems:
        if used >= sample:
            break
        steps = [s.model_dump() for s in problem.solution_steps]
        if not steps:
            continue
        token = set_deadline(budget)
        try:
            verified = [c for c in check_steps(steps) if c.status == "verified" and c.latex]
        finally:
            reset_deadline(token)
        if not verified:
            continue
        used += 1

        target = verified[0]
        variants = _corrupt(target.latex)
        if not variants:
            continue
        for variant in variants:
            mutated = [dict(step) for step in steps]
            mutated[target.index]["latex"] = variant
            token = set_deadline(budget)
            try:
                after = check_steps(mutated)[target.index]
            finally:
                reset_deadline(token)
            if after.status != "verified":
                caught += 1
                break
        else:
            hollow += 1
            report.findings.append(
                Finding(
                    "do-nghiem-kiem-chung",
                    problem.id,
                    f"bước {target.index + 1} vẫn được xác nhận sau khi làm hỏng một con số:"
                    f" {target.latex[:80]}",
                )
            )

    total = caught + hollow or 1
    report.checks["do-nghiem-kiem-chung"] = {
        "mô tả": "làm hỏng một con số trong bước đã xác nhận thì nhãn 'đã kiểm' phải mất",
        "bước đem thử": caught + hollow,
        "mất xác nhận (đúng)": caught,
        "xác nhận khống": hollow,
        "tỉ lệ xác nhận khống": round(hollow / total, 4),
        # Ngưỡng 15%: một bước gồm nhiều mắt xích được xác nhận khi **một** mắt
        # xích kiểm được, nên làm hỏng số ở mắt xích khác không nhất thiết làm
        # mất nhãn. Phần dư ấy là thiết kế, không phải lỗi.
        "ok": hollow / total <= 0.15,
    }


def check_practice_coverage(
    conn: sqlite3.Connection, report: AuditReport, sample: int, seed: int
) -> None:
    """Bất biến: mỗi kỹ năng phải gợi được vài bài để luyện."""
    skills = [row["skill"] for row in conn.execute("SELECT DISTINCT skill FROM problem_skills")]
    if not skills:
        report.checks["goi-y-luyen-tap"] = {"mô tả": "kho chưa có kỹ năng nào", "ok": True}
        return

    chosen = random.Random(seed).sample(skills, min(sample, len(skills)))
    counts = [len(problems_by_skill(conn, [skill], limit=10)) for skill in chosen]
    useless = sum(1 for c in counts if c <= 1)
    for skill, count in zip(chosen, counts, strict=True):
        if count <= 1:
            report.findings.append(
                Finding("goi-y-luyen-tap", fold(skill), f"chỉ gợi được {count} bài")
            )

    total = len(chosen) or 1
    report.checks["goi-y-luyen-tap"] = {
        "mô tả": "mỗi kỹ năng phải gợi được vài bài luyện",
        "kỹ năng đã thử": len(chosen),
        "trung bình bài gợi được": round(sum(counts) / total, 2),
        "kỹ năng vô dụng (≤1 bài)": useless,
        "tỉ lệ vô dụng": round(useless / total, 4),
        "ok": useless / total <= 0.15,
    }


def check_roadmap(conn: sqlite3.Connection, report: AuditReport, sample: int, seed: int) -> None:
    """Bất biến: đồ thị tiên quyết phải phi chu trình, và lộ trình dựng ra phải
    luôn đặt bài tiên quyết trước bài phụ thuộc.

    Có chu trình thì **không tồn tại** thứ tự học nào hợp lệ, và bộ sắp xếp sẽ
    âm thầm bỏ rơi vài bài. Vi phạm thứ tự thì người học vấp ngay bài đầu mà
    nhìn bảng vẫn thấy hợp lí.
    """
    graph = roadmap.prerequisite_graph(conn)

    colour: dict[str, int] = {}
    cycles: list[list[str]] = []

    def visit(node: str, stack: list[str]) -> None:
        colour[node] = 1
        stack.append(node)
        for parent in graph.get(node, ()):
            if colour.get(parent) == 1:
                cycles.append([*stack[stack.index(parent) :], parent])
            elif colour.get(parent, 0) == 0:
                visit(parent, stack)
        stack.pop()
        colour[node] = 2

    for node in list(graph):
        if colour.get(node, 0) == 0:
            visit(node, [])
    for cycle in cycles[:10]:
        report.findings.append(
            Finding("lo-trinh", cycle[0], "chu trình tiên quyết: " + " -> ".join(cycle))
        )

    lessons = [
        row["rid"] for row in conn.execute("SELECT rid FROM records WHERE kind = 'lesson'")
    ]
    chosen = random.Random(seed).sample(lessons, min(sample, len(lessons)))
    violations = 0
    empty = 0
    for lesson_id in chosen:
        path = roadmap.build(conn, RoadmapRequest(goal=lesson_id, practice_per_lesson=0))
        if not path.milestones:
            empty += 1
            report.findings.append(Finding("lo-trinh", lesson_id, "không dựng được lộ trình"))
            continue
        position = {m.lesson.id: i for i, m in enumerate(path.milestones)}
        for node, index in position.items():
            for parent in graph.get(node, ()):
                if parent in position and position[parent] > index:
                    violations += 1
                    report.findings.append(
                        Finding("lo-trinh", node, f"đứng trước tiên quyết {parent}")
                    )

    report.checks["lo-trinh"] = {
        "mô tả": "đồ thị tiên quyết phi chu trình và lộ trình đặt đúng thứ tự",
        "bài học đã thử": len(chosen),
        "chu trình": len(cycles),
        "vi phạm thứ tự": violations,
        "không dựng được": empty,
        "ok": not cycles and violations == 0 and empty == 0,
    }


def check_links(conn: sqlite3.Connection, report: AuditReport) -> None:
    """Bất biến: mọi liên kết giữa các kho phải trỏ tới bản ghi có thật."""
    dangling = conn.execute(
        "SELECT COUNT(*) AS n FROM edges e"
        " LEFT JOIN records r ON r.kind = e.dst_kind AND r.rid = e.dst_id"
        " WHERE r.rid IS NULL"
    ).fetchone()["n"]
    orphan_illustrations = conn.execute(
        "SELECT COUNT(*) AS n FROM illustrations i"
        " LEFT JOIN records r ON r.kind = 'formula' AND r.rid = i.formula_id"
        " WHERE r.rid IS NULL"
    ).fetchone()["n"]
    report.checks["lien-ket"] = {
        "mô tả": "liên kết giữa các kho phải trỏ tới bản ghi có thật",
        "cạnh treo": dangling,
        "minh hoạ mồ côi": orphan_illustrations,
        "ok": dangling == 0 and orphan_illustrations == 0,
    }


def run(
    conn: sqlite3.Connection,
    *,
    limit: int | None = 400,
    seed: int = 11,
    skill_sample: int = 200,
) -> AuditReport:
    """Chạy toàn bộ phép đo. `limit=None` để quét cả kho."""
    started = time.perf_counter()
    report = AuditReport()
    problems = _load_problems(conn, limit, seed)

    check_links(conn, report)
    check_roadmap(conn, report, max(20, skill_sample // 8), seed)
    check_grading(problems, report)
    check_strictness(problems, report)
    check_verification(problems, report)
    check_verification_sensitivity(problems, report)
    check_practice_coverage(conn, report, skill_sample, seed)

    report.elapsed_s = time.perf_counter() - started
    return report
