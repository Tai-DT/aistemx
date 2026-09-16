"""Chấm đáp án nhiều phần, và cách đọc trường `tolerance` của kho.

Hai chuyện tách bạch nhưng cùng lộ ra trong một lượt đo:

* 155/1258 bài (12,3%) bị trả về "không chấm được" chỉ vì đáp án có một câu
  diễn giải bám đuôi. Người học hỏi thì không nhận được gì.
* 119 bài khai `tolerance` theo quy ước **tuyệt đối** (`50000` cho đáp án
  `7{,}5\\times10^{6}`) trong khi bộ chấm đọc mọi giá trị như **tương đối**. Cửa
  sổ chấp nhận rộng tới năm triệu phần trăm, và người học sai gấp đôi vẫn được
  khen đúng.
"""

from __future__ import annotations

import pytest

from aistem.grading import _truth_table, grade_problem
from aistem.models import Problem
from aistem.quantities import countable_quantities, relative_tolerance


def _problem(answer: str, **kwargs: object) -> Problem:
    payload = {
        "id": "prob.test.0001", "subject": "physics", "level": "thpt", "grades": [12],
        "curriculum": ["vn"], "topic": "thử", "type": "tu-luan",
        "statement_vi": "đề thử", "statement_en": "", "answer": answer,
        "difficulty": 3, "estimated_minutes": 5.0,
    }
    payload.update(kwargs)
    return Problem.model_validate(payload)


class TestDungSaiTungY:
    """Dạng "câu trắc nghiệm đúng - sai" của đề thi Việt Nam: chấm tất định."""

    def test_dung_ca_bon_y(self) -> None:
        problem = _problem("(a) Đúng; (b) Sai; (c) Đúng; (d) Sai")
        assert grade_problem(problem, "a) Đúng; b) Sai; c) Đúng; d) Sai").correct

    def test_tra_loi_nguoc_thi_bi_bat(self) -> None:
        problem = _problem("(a) Đúng; (b) Sai; (c) Đúng; (d) Sai")
        result = grade_problem(problem, "(a) Sai; (b) Đúng; (c) Sai; (d) Đúng")
        assert not result.correct and result.verdict == "sai"

    def test_sai_mot_y_thi_bao_dung_ba_tren_bon(self) -> None:
        problem = _problem("(a) Đúng; (b) Sai; (c) Đúng; (d) Sai")
        result = grade_problem(problem, "(a) Đúng; (b) Sai; (c) Đúng; (d) Đúng")
        assert result.verdict == "dung-mot-phan"
        assert [p.label for p in result.parts if not p.correct] == ["d"]

    def test_thieu_mot_y_la_thieu_chu_khong_phai_sai_nguoc(self) -> None:
        problem = _problem("(a) Đúng; (b) Sai; (c) Đúng")
        result = grade_problem(problem, "(a) Đúng; (b) Sai")
        missing = [p for p in result.parts if p.label == "c"]
        assert missing and "thiếu" in missing[0].detail

    def test_khong_nham_voi_dap_an_thuong(self) -> None:
        assert _truth_table("9,8 m/s^2") == {}
        assert _truth_table("Đúng") == {}


class TestPhanDienGiaiChuaChamDuoc:
    """Phần bằng lời không được xếp vào ô "sai" — nó chưa được chấm."""

    def test_chi_chấm_phan_chấm_duoc(self) -> None:
        problem = _problem("theta = 0,20; LOD ≈ 3,35 nên kết luận có liên kết")
        result = grade_problem(problem, problem.answer)
        assert result.correct and result.verdict == "dung"

    def test_dien_giai_khac_di_thi_noi_la_chua_cham_duoc(self) -> None:
        problem = _problem("Ức chế cạnh tranh; K_i = 0,25 mM")
        result = grade_problem(problem, "Ức chế phi cạnh tranh; K_i = 0,25 mM")
        # Con số đúng, phần lời khác — KHÔNG được nói người học sai.
        assert not any(p.status == "sai" for p in result.parts)
        assert any(p.status == "chua-cham-duoc" for p in result.parts)
        assert "chưa chấm" in result.detail

    def test_so_sai_thi_van_bi_bat(self) -> None:
        problem = _problem("Ức chế cạnh tranh; K_i = 0,25 mM")
        result = grade_problem(problem, "Ức chế cạnh tranh; K_i = 2,5 mM")
        assert not result.correct
        assert any(p.status == "sai" for p in result.parts)

    def test_dap_an_mot_dai_luong_khong_di_qua_duong_nhieu_phan(self) -> None:
        assert countable_quantities("9,8 m/s^2") < 2


class TestDocDungTruongTolerance:
    """`tolerance` trong kho lẫn lộn hai quy ước, và đọc nhầm thì mở toang cửa."""

    @pytest.mark.parametrize(
        ("declared", "expected", "want"),
        [
            (0.01, 300, 0.01),          # tương đối, đúng như hệ thống vẫn hiểu
            (0.05, 7, 0.05),
            (0.2, 4, 0.2),              # ngưỡng: vẫn còn là tương đối
            (50000.0, 7.5e6, 1 / 150),  # tuyệt đối ±50000 trên 7,5·10⁶
            (1.0, 200000, 5e-6),
            (0.5, 10800, 0.5 / 10800),
        ],
    )
    def test_quy_doi_ve_sai_so_tuong_doi(
        self, declared: float, expected: float, want: float
    ) -> None:
        assert relative_tolerance(declared, expected, 0.01) == pytest.approx(want)

    def test_khong_co_moc_thi_lay_mac_dinh_chu_khong_dung_so_dang_ngo(self) -> None:
        assert relative_tolerance(50000.0, None, 0.01) == 0.01
        assert relative_tolerance(None, 5, 0.01) == 0.01

    def test_dap_an_sai_gap_doi_khong_con_duoc_khen_dung(self) -> None:
        problem = _problem(
            "k_cat = 300 s^-1", answer_numeric=300.0, tolerance=50000.0, type="dien-so"
        )
        assert grade_problem(problem, "300").correct
        assert not grade_problem(problem, "600").correct
