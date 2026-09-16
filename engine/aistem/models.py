"""Kiểu dữ liệu dùng chung — bám sát `schema.json` của bốn kho, cộng thêm các
kiểu vào/ra của pipeline xử lí bài toán."""

from __future__ import annotations

from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field

Subject = Literal["math", "physics", "chemistry", "biology"]
Level = Literal["tieu-hoc", "thcs", "thpt", "dai-hoc"]
Curriculum = Literal[
    "vn-gdpt-2018", "ap", "ib", "a-level", "intl-undergrad", "olympiad", "ru-east-eu"
]
ProblemType = Literal["trac-nghiem", "tu-luan", "dien-so", "dung-sai", "ghep-doi"]

SUBJECT_VI = {
    "math": "Toán học",
    "physics": "Vật lí",
    "chemistry": "Hoá học",
    "biology": "Sinh học",
}
LEVEL_VI = {
    "tieu-hoc": "Tiểu học",
    "thcs": "THCS",
    "thpt": "THPT",
    "dai-hoc": "Đại học",
}
DIFFICULTY_VI = {
    1: "nhận biết",
    2: "thông hiểu",
    3: "vận dụng",
    4: "vận dụng cao",
    5: "olympiad",
}


class RecordKind(str, Enum):
    FORMULA = "formula"
    LESSON = "lesson"
    PROBLEM = "problem"
    EXAM = "exam"


# --------------------------------------------------------------------------- #
# Bản ghi trong kho
# --------------------------------------------------------------------------- #


class Formula(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    subject: str
    level: str
    grades: list[int] = Field(default_factory=list)
    curriculum: list[str] = Field(default_factory=list)
    topic: str = ""
    subtopic: str | None = None
    name_vi: str = ""
    name_en: str = ""
    latex: str = ""
    vars: dict[str, str] = Field(default_factory=dict)
    units: dict[str, str] = Field(default_factory=dict)
    conditions: str | None = None
    note: str | None = None
    tags: list[str] = Field(default_factory=list)
    related: list[str] = Field(default_factory=list)

    def as_prompt_block(self) -> str:
        """Rút gọn cho prompt — chỉ giữ phần LLM cần để giải đúng."""
        lines = [f"[{self.id}] {self.name_vi}"]
        if self.name_en and self.name_en != self.name_vi:
            lines[0] += f" ({self.name_en})"
        if self.latex:
            lines.append(f"  LaTeX: {self.latex}")
        if self.vars:
            lines.append("  Biến: " + "; ".join(f"{k} = {v}" for k, v in self.vars.items()))
        if self.units:
            lines.append("  Đơn vị: " + "; ".join(f"{k}: {v}" for k, v in self.units.items()))
        if self.conditions:
            lines.append(f"  Điều kiện: {self.conditions}")
        return "\n".join(lines)


class Choice(BaseModel):
    model_config = ConfigDict(extra="allow")
    key: str
    text: str
    why_wrong: str = ""


class SolutionStep(BaseModel):
    model_config = ConfigDict(extra="allow")
    explain: str
    latex: str | None = None


class Problem(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    subject: str
    level: str
    grades: list[int] = Field(default_factory=list)
    curriculum: list[str] = Field(default_factory=list)
    topic: str = ""
    type: str = "tu-luan"
    statement_vi: str = ""
    statement_en: str = ""
    choices: list[Choice] = Field(default_factory=list)
    answer: str = ""
    answer_numeric: float | None = None
    answer_unit: str | None = None
    tolerance: float | None = None
    solution_steps: list[SolutionStep] = Field(default_factory=list)
    formulas_used: list[str] = Field(default_factory=list)
    difficulty: int = 3
    estimated_minutes: float = 5
    skills: list[str] = Field(default_factory=list)
    hints: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    sources: list[str] = Field(default_factory=list)


class Illustration(BaseModel):
    """Hình minh hoạ gắn với một công thức.

    Không phải một kho ngang hàng với bốn kho kia mà là **phần đính kèm** của
    công thức: khoá chính là `formula_id`, và mọi truy vấn đều đi từ công thức
    sang hình chứ không ngược lại.
    """

    model_config = ConfigDict(extra="allow")

    formula_id: str
    kind: str = "2d-svg"
    source: str = ""
    generator: str = ""
    caption_vi: str = ""
    svg_path: str | None = None
    raster_path: str | None = None
    #: Nội dung SVG nội tuyến — nhỏ (vài KB) nên trả thẳng, phía hiển thị khỏi
    #: phải gọi thêm một vòng nữa.
    svg: str | None = None
    width: int | None = None
    height: int | None = None
    status: str = ""

    @property
    def ready(self) -> bool:
        """Hình đã dùng được chưa, hay mới chỉ là chỗ dành sẵn."""
        return self.status != "placeholder" and bool(self.svg_path or self.raster_path)


class Lesson(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    subject: str
    level: str
    grades: list[int] = Field(default_factory=list)
    curriculum: list[str] = Field(default_factory=list)
    unit: str = ""
    order: int | None = None
    title_vi: str = ""
    title_en: str = ""
    objectives: list[str] = Field(default_factory=list)
    prerequisites: list[str] = Field(default_factory=list)
    key_concepts: list[dict[str, Any]] = Field(default_factory=list)
    content: str = ""
    formulas: list[str] = Field(default_factory=list)
    worked_examples: list[dict[str, Any]] = Field(default_factory=list)
    common_mistakes: list[Any] = Field(default_factory=list)
    duration_minutes: int | None = None
    difficulty: int | None = None
    tags: list[str] = Field(default_factory=list)


class Exam(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    name: str = ""
    provider: str = ""
    subject: str = ""
    curriculum: list[str] | str = Field(default_factory=list)
    level: str = ""
    overview: str = ""
    sections: list[dict[str, Any]] = Field(default_factory=list)
    topic_weights: Any = None
    question_types: list[Any] = Field(default_factory=list)
    formula_sheet_provided: Any = None
    formulas_must_memorize: list[str] = Field(default_factory=list)
    scoring: Any = None
    strategies: list[Any] = Field(default_factory=list)
    common_traps: list[Any] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)


# --------------------------------------------------------------------------- #
# Truy xuất
# --------------------------------------------------------------------------- #


class Hit(BaseModel):
    """Một kết quả tìm kiếm, đã hợp nhất điểm từ nhiều kênh."""

    kind: RecordKind
    id: str
    title: str
    score: float
    subject: str = ""
    level: str = ""
    topic: str = ""
    snippet: str = ""
    channels: list[str] = Field(default_factory=list)
    record: dict[str, Any] | None = None


class SearchResponse(BaseModel):
    query: str
    total: int
    hits: list[Hit]


# --------------------------------------------------------------------------- #
# Pipeline xử lí bài toán
# --------------------------------------------------------------------------- #


class Classification(BaseModel):
    """Kết quả bước phân loại đề."""

    subject: str
    level: str = "thpt"
    grades: list[int] = Field(default_factory=list)
    curriculum: list[str] = Field(default_factory=list)
    topic: str = ""
    type: str = "tu-luan"
    difficulty: int = 3
    skills: list[str] = Field(default_factory=list)
    tags: list[str] = Field(default_factory=list)
    confidence: float = 0.0
    rationale: str = ""
    source: Literal["llm", "retrieval", "heuristic"] = "heuristic"


class StepCheck(BaseModel):
    """Kiểm chứng một bước biến đổi bằng CAS.

    Năm trạng thái, cố ý tách `unparsed` khỏi `inconclusive`: cái đầu là CAS
    không đọc nổi biểu thức, cái sau là đọc được nhưng bước ấy là phép thế số
    nên không có gì để đối chiếu. Gộp hai thứ lại sẽ che mất chỗ cần cải thiện.
    """

    index: int
    latex: str | None = None
    status: Literal["verified", "refuted", "skipped", "unparsed", "inconclusive"] = "skipped"
    detail: str = ""


class Verification(BaseModel):
    """Toàn bộ kết quả kiểm chứng độc lập bằng SymPy/Pint."""

    answer_status: Literal["verified", "refuted", "unchecked"] = "unchecked"
    answer_detail: str = ""
    #: Giá trị cuối CAS đọc được lệch với đáp án công bố, nhưng chưa đủ căn cứ
    #: để kết luận sai — thường vì lời giải kết thúc bằng một đại lượng phụ.
    #: Đáng nêu ra như một điểm cần rà, không đáng gạch sai.
    answer_mismatch: bool = False
    cas_value: float | None = None
    cas_expression: str | None = None
    unit_status: Literal["consistent", "inconsistent", "unchecked"] = "unchecked"
    unit_detail: str = ""
    steps: list[StepCheck] = Field(default_factory=list)
    steps_verified: int = 0
    steps_refuted: int = 0
    steps_inconclusive: int = 0
    steps_total: int = 0

    @property
    def trustworthy(self) -> bool:
        return (
            self.answer_status != "refuted"
            and self.steps_refuted == 0
            and not self.answer_mismatch
        )


class RetrievedContext(BaseModel):
    formulas: list[Hit] = Field(default_factory=list)
    lessons: list[Hit] = Field(default_factory=list)
    similar_problems: list[Hit] = Field(default_factory=list)
    exams: list[Hit] = Field(default_factory=list)
    illustrations: list[Illustration] = Field(default_factory=list)


class SolveRequest(BaseModel):
    statement: str = Field(..., description="Đề bài dạng văn bản hoặc LaTeX thuần")
    image_base64: str | None = Field(None, description="Ảnh đề bài, base64 không kèm tiền tố")
    image_media_type: str = "image/png"
    subject: str | None = Field(None, description="Ép môn, bỏ trống để hệ thống tự phân loại")
    level: str | None = None
    curriculum: str | None = None
    language: Literal["vi", "en"] = "vi"
    show_steps: bool = True
    verify: bool = True
    heavy: bool = Field(False, description="Dùng model mạnh hơn cho bài khó")


class SolveResponse(BaseModel):
    statement: str
    statement_latex: str | None = None
    classification: Classification
    answer: str = ""
    answer_numeric: float | None = None
    answer_unit: str | None = None
    solution_steps: list[SolutionStep] = Field(default_factory=list)
    formulas_used: list[str] = Field(default_factory=list)
    verification: Verification = Field(default_factory=Verification)
    context: RetrievedContext = Field(default_factory=RetrievedContext)
    recommendations: list[Hit] = Field(default_factory=list)
    confidence: Literal["cao", "trung-binh", "thap"] = "trung-binh"
    warnings: list[str] = Field(default_factory=list)
    elapsed_ms: int = 0
    model: str = ""

    def as_problem_record(self, problem_id: str) -> dict[str, Any]:
        """Xuất ra đúng định dạng bản ghi kho `data/problems/` để nạp ngược vào kho."""
        return {
            "id": problem_id,
            "subject": self.classification.subject,
            "level": self.classification.level,
            "grades": self.classification.grades or [12],
            "curriculum": self.classification.curriculum or ["vn-gdpt-2018"],
            "topic": self.classification.topic or "Chưa phân loại",
            "type": self.classification.type,
            "statement_vi": self.statement,
            "statement_en": "",
            "answer": self.answer,
            **({"answer_numeric": self.answer_numeric} if self.answer_numeric is not None else {}),
            **({"answer_unit": self.answer_unit} if self.answer_unit else {}),
            "tolerance": 0.01,
            "solution_steps": [s.model_dump(exclude_none=True) for s in self.solution_steps],
            "formulas_used": self.formulas_used,
            "difficulty": self.classification.difficulty,
            "estimated_minutes": 5,
            "skills": self.classification.skills or ["chưa gắn kỹ năng"],
            "tags": self.classification.tags or ["sinh-tu-dong"],
        }


# --------------------------------------------------------------------------- #
# Chấm bài
# --------------------------------------------------------------------------- #


class GradeRequest(BaseModel):
    problem_id: str | None = Field(None, description="Chấm theo bài có sẵn trong kho")
    learner: str = Field("local", description="Ai đang làm bài, để ghi tiến độ")
    student_answer: str
    expected_answer: str | None = Field(None, description="Dùng khi chấm bài ngoài kho")
    expected_numeric: float | None = None
    tolerance: float | None = None
    problem_type: str | None = None


class PartResult(BaseModel):
    """Kết quả chấm một đại lượng trong đáp án nhiều phần.

    Ba trạng thái chứ không phải hai, cùng lí do với lớp kiểm chứng CAS: một
    đáp án nhiều ý thường trộn đại lượng số với diễn giải bằng lời, và câu chữ
    thì máy không đọc được. Ép phần lời vào ô "sai" là nói với người học rằng
    họ làm sai một thứ chưa ai chấm.
    """

    label: str
    correct: bool
    status: Literal["dung", "sai", "chua-cham-duoc"] = "sai"
    expected: str = ""
    received: str = ""
    detail: str = ""


class GradeResult(BaseModel):
    correct: bool
    verdict: Literal[
        "dung", "sai", "gan-dung", "sai-don-vi", "khong-cham-duoc", "dung-mot-phan"
    ] = "khong-cham-duoc"
    method: Literal["numeric", "choice", "symbolic", "text", "multi", "none"] = "none"
    #: Chi tiết từng phần khi đáp án gồm nhiều đại lượng — để người học biết
    #: mình hỏng ở đâu chứ không chỉ biết là sai.
    parts: list[PartResult] = Field(default_factory=list)
    score: float = 0.0
    expected: str = ""
    received: str = ""
    detail: str = ""
    relative_error: float | None = None
    why_wrong: str = ""
    hints: list[str] = Field(default_factory=list)
    weak_skills: list[str] = Field(default_factory=list)
    next_steps: list[Hit] = Field(default_factory=list)


# --------------------------------------------------------------------------- #
# Lộ trình học
# --------------------------------------------------------------------------- #


class PathItem(BaseModel):
    """Một việc phải làm trong lộ trình: đọc một bài, hoặc làm một bài tập."""

    kind: Literal["lesson", "problem"]
    id: str
    title: str
    minutes: float = 0
    difficulty: int | None = None
    subject: str = ""
    level: str = ""
    topic: str = ""
    #: Vì sao việc này có mặt ở đây — để người học biết mình đang học cái gì
    #: cho mục đích gì, chứ không chỉ nhận một danh sách.
    reason: str = ""


class Milestone(BaseModel):
    """Một chặng: một bài học cộng phần luyện tập ngay sau nó."""

    order: int
    lesson: PathItem
    practice: list[PathItem] = Field(default_factory=list)
    unit: str = ""
    prerequisites_met: list[str] = Field(default_factory=list)

    @property
    def minutes(self) -> float:
        return self.lesson.minutes + sum(p.minutes for p in self.practice)


class StudySession(BaseModel):
    """Một buổi học, cắt theo quỹ thời gian người học có."""

    index: int
    items: list[PathItem] = Field(default_factory=list)
    minutes: float = 0


class RoadmapRequest(BaseModel):
    goal: str = Field(
        ...,
        description=(
            "Mục tiêu: id bài học, id kỳ thi, hoặc từ khoá chủ đề "
            "(ví dụ 'quy tắc L'Hospital', 'exam.ap-calculus-bc', 'tích phân')"
        ),
    )
    subject: str | None = None
    level: str | None = None
    curriculum: str | None = None
    learner: str | None = Field(
        None,
        description=(
            "Lấy bài đã học và kỹ năng yếu từ tiến độ thật của người này, "
            "khỏi phải khai tay"
        ),
    )
    known_lessons: list[str] = Field(
        default_factory=list, description="Bài học đã nắm, sẽ bị loại khỏi lộ trình"
    )
    weak_skills: list[str] = Field(
        default_factory=list, description="Kỹ năng đang yếu, sẽ được luyện thêm"
    )
    practice_per_lesson: int = Field(2, ge=0, le=6)
    minutes_per_session: int = Field(60, ge=15, le=300)
    max_lessons: int = Field(40, ge=1, le=200)


class LearningPath(BaseModel):
    goal: str
    goal_lessons: list[str] = Field(default_factory=list)
    milestones: list[Milestone] = Field(default_factory=list)
    sessions: list[StudySession] = Field(default_factory=list)
    total_minutes: float = 0
    lesson_count: int = 0
    practice_count: int = 0
    skipped_known: int = 0
    truncated: bool = False
    subjects: list[str] = Field(default_factory=list)
    summary: str = ""
    warnings: list[str] = Field(default_factory=list)

    @property
    def total_hours(self) -> float:
        return round(self.total_minutes / 60, 1)


# --------------------------------------------------------------------------- #
# Đề thi thử
# --------------------------------------------------------------------------- #


class ExamQuestion(BaseModel):
    order: int
    problem_id: str
    topic: str = ""
    statement: str = ""
    type: str = "tu-luan"
    choices: list[dict[str, Any]] = Field(default_factory=list)
    difficulty: int | None = None
    minutes: float = 5
    #: Chỉ có khi người dùng xin kèm lời giải — mặc định giấu đi để còn thi thử.
    answer: str = ""
    solution_steps: list[dict[str, Any]] = Field(default_factory=list)


class TopicCoverage(BaseModel):
    """Bản thiết kế đòi bao nhiêu câu ở chủ đề này, và kho đáp ứng được bao nhiêu."""

    topic: str
    weight_percent: float
    wanted: int
    got: int
    available: int

    @property
    def complete(self) -> bool:
        return self.got >= self.wanted


class MockExamRequest(BaseModel):
    exam_id: str = Field(..., description="id hồ sơ kỳ thi, ví dụ exam.ap-calculus-bc")
    question_count: int | None = Field(
        None, ge=1, le=120, description="Bỏ trống để theo đúng số câu của đề thật"
    )
    difficulty_max: int | None = Field(None, ge=1, le=5)
    include_solutions: bool = Field(False, description="Kèm đáp án và lời giải")
    seed: int = Field(0, description="Cùng seed cho ra cùng một đề, để so sánh được")


class MockExam(BaseModel):
    exam_id: str
    name: str = ""
    subject: str = ""
    blueprint_questions: int = 0
    requested_questions: int = 0
    sections: list[dict[str, Any]] = Field(default_factory=list)
    questions: list[ExamQuestion] = Field(default_factory=list)
    coverage: list[TopicCoverage] = Field(default_factory=list)
    total_minutes: float = 0
    summary: str = ""
    warnings: list[str] = Field(default_factory=list)


class MockExamSubmission(BaseModel):
    exam_id: str
    answers: dict[str, str] = Field(..., description="{problem_id: câu trả lời}")
    learner: str = "local"


class TopicScore(BaseModel):
    topic: str
    correct: int
    total: int
    weight_percent: float = 0

    @property
    def accuracy(self) -> float:
        return self.correct / self.total if self.total else 0.0


class MockExamResult(BaseModel):
    exam_id: str
    total: int
    correct: int
    uncheckable: int = 0
    raw_score: float = 0
    percent: float = 0
    per_question: list[GradeResult] = Field(default_factory=list)
    per_topic: list[TopicScore] = Field(default_factory=list)
    weakest_topics: list[str] = Field(default_factory=list)
    summary: str = ""
    scoring_note: str = ""


class DiagnosisRequest(BaseModel):
    """Nộp một loạt câu trả lời để chẩn đoán lỗ hổng kiến thức."""

    answers: dict[str, str] = Field(..., description="{problem_id: câu trả lời của học sinh}")
    max_recommendations: int = 8


class SkillStat(BaseModel):
    skill: str
    attempted: int
    correct: int

    @property
    def accuracy(self) -> float:
        return self.correct / self.attempted if self.attempted else 0.0


class DiagnosisResult(BaseModel):
    total: int
    correct: int
    accuracy: float
    per_problem: list[GradeResult] = Field(default_factory=list)
    weak_skills: list[SkillStat] = Field(default_factory=list)
    weak_topics: list[str] = Field(default_factory=list)
    recommended_lessons: list[Hit] = Field(default_factory=list)
    recommended_problems: list[Hit] = Field(default_factory=list)
    summary: str = ""
