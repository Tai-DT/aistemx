"""Pipeline xử lí bài toán, chạy với mô hình giả lập.

Nhánh có mô hình được test bằng `fake_llm` chứ không gọi API thật, nên bộ test
chạy được ở mọi máy và mọi lần CI mà không tốn tiền, đồng thời kiểm được cả
những đường lỗi khó dựng bằng API thật: mô hình bịa id công thức, mô hình đưa
đáp số mà CAS bác bỏ.
"""

from __future__ import annotations

import sqlite3

from aistem.models import SolveRequest
from aistem.pipeline import classify_by_retrieval, gather, read
from aistem.pipeline.retrieve import _focus, as_prompt_context
from aistem.pipeline.solve import solve

LIMIT_PROBLEM = "Tính giới hạn lim x->3 của (x^2-9)/(x^2-5x+6)."

GOOD_SOLUTION = {
    "answer": "6",
    "answer_numeric": 6,
    "solution_steps": [
        {"explain": "Thay x = 3 cho dạng 0/0 nên phân tích thành nhân tử.",
         "latex": r"\frac{x^{2}-9}{x^{2}-5x+6} = \frac{(x-3)(x+3)}{(x-3)(x-2)}"},
        {"explain": "Khử nhân tử chung rồi thay giá trị.",
         "latex": r"\lim_{x \to 3} \frac{x+3}{x-2} = 6"},
    ],
    "formulas_used": ["math.thpt.dao-ham.dao-ham-cua-tich", "cong.thuc.bia.dat"],
    "confidence": 0.9,
    "warnings": [],
}

#: Lời giải trôi chảy nhưng sai số học — đúng kiểu hỏng mà mô hình ngôn ngữ hay
#: mắc và người đọc khó bắt.
BAD_SOLUTION = {
    "answer": "9",
    "answer_numeric": 9,
    "solution_steps": [
        {"explain": "Bước này cộng sai.", "latex": "y = 2 + 2 = 5"},
        {"explain": "Bước này cộng đúng.", "latex": "x = 3 + 3 = 6"},
    ],
    "formulas_used": [],
    "confidence": 0.95,
    "warnings": [],
}

#: Mọi bước đúng nhưng giá trị cuối lệch với đáp án công bố.
MISMATCHED_SOLUTION = {
    "answer": "7",
    "answer_numeric": 7,
    "solution_steps": [{"explain": "Cộng hai số.", "latex": "x = 3 + 3 = 6"}],
    "formulas_used": [],
    "confidence": 0.95,
    "warnings": [],
}


class TestIngest:
    def test_plain_text_does_not_call_the_model(self) -> None:
        result = read("Tính 2 + 2")
        assert result.statement == "Tính 2 + 2"
        assert result.source == "text"

    def test_empty_input_is_rejected(self) -> None:
        import pytest

        with pytest.raises(ValueError):
            read("")


class TestClassify:
    def test_subject_is_identified_without_a_model(self, conn: sqlite3.Connection) -> None:
        cases = {
            LIMIT_PROBLEM: "math",
            "Một vật khối lượng 2 kg chuyển động 5 m/s. Tính động năng của vật.": "physics",
            "Hoà tan 5,85 g NaCl thành 500 mL. Tính nồng độ mol của dung dịch.": "chemistry",
            "Cho F1 dị hợp tự thụ phấn, tỉ lệ kiểu hình F2 là bao nhiêu?": "biology",
        }
        for statement, expected in cases.items():
            assert classify_by_retrieval(conn, statement).subject == expected


class TestRetrieve:
    def test_focus_extracts_the_question(self) -> None:
        focus = _focus("Một vật nặng 2 kg đi 5 m/s. Tính động năng của vật.")
        assert focus is not None and "động năng" in focus

    def test_question_clause_drives_formula_retrieval(self, conn: sqlite3.Connection) -> None:
        statement = "Một vật khối lượng 2 kg chuyển động với vận tốc 5 m/s. Tính động năng của vật."
        context = gather(conn, statement, classify_by_retrieval(conn, statement))
        assert any("dong-nang" in hit.id for hit in context.formulas)

    def test_prompt_context_only_cites_real_ids(self, conn: sqlite3.Connection) -> None:
        context = gather(conn, LIMIT_PROBLEM, classify_by_retrieval(conn, LIMIT_PROBLEM))
        block = as_prompt_context(context)
        assert "Công thức có trong kho" in block
        for hit in context.formulas[:3]:
            assert hit.id in block


class TestSolveWithoutKey:
    def test_degrades_gracefully(self, conn: sqlite3.Connection) -> None:
        response = solve(conn, SolveRequest(statement=LIMIT_PROBLEM))
        assert response.answer == ""
        assert response.confidence == "thap"
        assert any("khoá API" in w for w in response.warnings)
        # Phần không cần mô hình vẫn phải dùng được.
        assert response.classification.subject == "math"
        assert response.context.formulas


class TestSolveWithModel:
    def test_full_pipeline(self, conn: sqlite3.Connection, fake_llm) -> None:
        fake_llm["payloads"]["giai_bai"] = GOOD_SOLUTION
        response = solve(conn, SolveRequest(statement=LIMIT_PROBLEM))

        assert response.answer == "6"
        assert response.verification.answer_status == "verified"
        assert response.confidence == "cao"
        assert response.solution_steps

    def test_invented_formula_ids_are_dropped(self, conn: sqlite3.Connection, fake_llm) -> None:
        fake_llm["payloads"]["giai_bai"] = GOOD_SOLUTION
        response = solve(conn, SolveRequest(statement=LIMIT_PROBLEM))

        assert "cong.thuc.bia.dat" not in response.formulas_used
        assert "math.thpt.dao-ham.dao-ham-cua-tich" in response.formulas_used
        assert any("không có trong kho" in w for w in response.warnings)

    def test_cas_overrules_a_confident_model(self, conn: sqlite3.Connection, fake_llm) -> None:
        """Mô hình khai confidence 0.95 nhưng tính sai — CAS phải có quyền phủ quyết."""
        fake_llm["payloads"]["giai_bai"] = BAD_SOLUTION
        response = solve(conn, SolveRequest(statement=LIMIT_PROBLEM))

        assert response.verification.answer_status == "refuted"
        assert response.verification.steps_refuted >= 1
        assert response.confidence == "thap"
        assert any("CAS bác bỏ" in w for w in response.warnings)

    def test_mismatch_lowers_confidence_without_condemning(
        self, conn: sqlite3.Connection, fake_llm
    ) -> None:
        fake_llm["payloads"]["giai_bai"] = MISMATCHED_SOLUTION
        response = solve(conn, SolveRequest(statement=LIMIT_PROBLEM))

        assert response.verification.answer_status == "unchecked"
        assert response.verification.answer_mismatch is True
        assert response.confidence == "thap"
        assert any("Cần rà lại đáp số" in w for w in response.warnings)

    def test_export_matches_corpus_schema(self, conn: sqlite3.Connection, fake_llm) -> None:
        fake_llm["payloads"]["giai_bai"] = GOOD_SOLUTION
        response = solve(conn, SolveRequest(statement=LIMIT_PROBLEM))
        record = response.as_problem_record("prob.math.moi.0001")

        required = {
            "id", "subject", "level", "grades", "curriculum", "topic", "type",
            "statement_vi", "statement_en", "answer", "solution_steps",
            "formulas_used", "difficulty", "estimated_minutes", "skills", "tags",
        }
        assert required <= set(record)
        assert record["subject"] in {"math", "physics", "chemistry", "biology"}
        assert 1 <= record["difficulty"] <= 5

    def test_model_failure_does_not_crash_the_request(
        self, conn: sqlite3.Connection, fake_llm
    ) -> None:
        fake_llm["payloads"].pop("giai_bai", None)  # mô hình lỗi
        response = solve(conn, SolveRequest(statement=LIMIT_PROBLEM))
        assert response.confidence == "thap"
        assert response.warnings


class TestClassifyAcrossLevels:
    """Kho bài tập gần như không phủ tiểu học và THCS.

    Nếu chỉ bỏ phiếu từ kho bài tập thì bài chu vi hình chữ nhật lớp 4 bị gán
    THPT, rồi bước truy xuất lọc theo cấp sai và trả về công thức Vật lí. Kho
    công thức mới là kho phủ liền mạch từ lớp 1 tới đại học.
    """

    def test_primary_school_problem_is_not_labelled_upper_secondary(
        self, conn: sqlite3.Connection
    ) -> None:
        result = classify_by_retrieval(
            conn, "Tính chu vi hình chữ nhật có chiều dài 8 cm và chiều rộng 5 cm."
        )
        assert result.subject == "math"
        assert result.level in {"tieu-hoc", "thcs"}

    def test_lower_secondary_geometry(self, conn: sqlite3.Connection) -> None:
        result = classify_by_retrieval(conn, "Tính diện tích hình tròn bán kính 5 cm.")
        assert result.subject == "math"
        assert result.level in {"tieu-hoc", "thcs"}

    def test_upper_secondary_still_upper_secondary(self, conn: sqlite3.Connection) -> None:
        result = classify_by_retrieval(conn, LIMIT_PROBLEM)
        assert result.subject == "math"
        assert result.level in {"thpt", "dai-hoc"}


class TestIllustrations:
    def test_geometry_problem_gets_a_picture(self, conn: sqlite3.Connection) -> None:
        response = solve(
            conn, SolveRequest(statement="Tính diện tích hình tròn bán kính 5 cm.")
        )
        pictures = response.context.illustrations
        assert pictures, "bài hình học phải kèm được hình minh hoạ"
        assert pictures[0].svg and pictures[0].svg.lstrip().startswith("<svg")

    def test_placeholders_are_not_offered(self, conn: sqlite3.Connection) -> None:
        """Hiện một ô trống cho người học còn tệ hơn không hiện gì."""
        from aistem.store import illustrations

        rows = conn.execute(
            "SELECT formula_id FROM illustrations WHERE status = 'placeholder' LIMIT 3"
        ).fetchall()
        if not rows:
            return
        ids = [row["formula_id"] for row in rows]
        assert illustrations.for_formulas(conn, ids) == []

    def test_path_traversal_is_blocked(self) -> None:
        from aistem.store import illustrations

        assert illustrations.read_svg("../../../../etc/passwd") is None
        assert illustrations.read_svg("svg/../../../secrets.svg") is None
