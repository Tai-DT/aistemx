"""REST API của hệ thống xử lí bài toán AISTEM.

FastAPI tự sinh OpenAPI ở `/openapi.json` và trang thử ở `/docs`, nên khi dựng
app (web hay mobile) chỉ cần sinh client từ lược đồ đó, không phải viết tay
tầng gọi API.
"""

from __future__ import annotations

import base64
import sqlite3
from collections.abc import Iterator
from contextlib import asynccontextmanager
from typing import Annotated, Any, Literal

from fastapi import Depends, FastAPI, File, Form, HTTPException, Query, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from .. import __version__, grading, llm, mock_exam, progress, roadmap
from ..config import settings
from ..models import (
    DiagnosisRequest,
    DiagnosisResult,
    GradeRequest,
    GradeResult,
    Hit,
    Illustration,
    LearningPath,
    MockExam,
    MockExamRequest,
    MockExamResult,
    MockExamSubmission,
    RoadmapRequest,
    SearchResponse,
    SolveRequest,
    SolveResponse,
)
from ..pipeline import classify_by_retrieval, solve
from ..store import illustrations
from ..store.build import ensure_built
from ..store.db import connect, load_record, stats
from ..store.search import Filters, problems_by_skill, search, uses_formula

KIND_TO_PATH = {
    "formula": "formulas",
    "lesson": "lessons",
    "problem": "problems",
    "exam": "exams",
}
PATH_TO_KIND = {v: k for k, v in KIND_TO_PATH.items()}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Không có DB thì dựng luôn, để `docker run` là chạy được ngay.
    ensure_built()
    yield


app = FastAPI(
    title="AISTEM — Hệ thống xử lí bài toán",
    version=__version__,
    description=(
        "Đọc đề, phân loại, truy xuất công thức và bài học, giải từng bước, "
        "kiểm chứng lại bằng CAS, chấm bài và chẩn đoán lỗ hổng kiến thức "
        "trên kho dữ liệu AISTEM (Toán · Lí · Hoá · Sinh)."
    ),
    lifespan=lifespan,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_conn() -> Iterator[sqlite3.Connection]:
    """Một kết nối SQLite cho mỗi request.

    SQLite mở kết nối rất rẻ, và cách này tránh hẳn chuyện chia sẻ kết nối giữa
    các luồng của FastAPI.
    """
    conn = connect()
    try:
        yield conn
    finally:
        conn.close()


Conn = Annotated[sqlite3.Connection, Depends(get_conn)]


# --------------------------------------------------------------------------- #
# Trạng thái hệ thống
# --------------------------------------------------------------------------- #


@app.get("/health", tags=["hệ thống"], summary="Kiểm tra hệ thống sống")
def health(conn: Conn) -> dict[str, Any]:
    return {
        "status": "ok",
        "version": __version__,
        "database": str(settings.database),
        "llm_configured": llm.available(),
        "records": stats(conn)["total"],
    }


@app.get("/stats", tags=["hệ thống"], summary="Thống kê kho dữ liệu")
def statistics(conn: Conn) -> dict[str, Any]:
    return stats(conn)


# --------------------------------------------------------------------------- #
# Tra cứu
# --------------------------------------------------------------------------- #


@app.get("/search", response_model=SearchResponse, tags=["tra cứu"],
         summary="Tìm kiếm xuyên bốn kho")
def search_endpoint(
    conn: Conn,
    q: Annotated[str, Query(description="Từ khoá; gõ không dấu vẫn ra kết quả có dấu")] = "",
    kind: Annotated[
        list[Literal["formula", "lesson", "problem", "exam"]] | None,
        Query(description="Giới hạn theo kho"),
    ] = None,
    subject: Annotated[
        Literal["math", "physics", "chemistry", "biology"] | None, Query()
    ] = None,
    level: Annotated[
        Literal["tieu-hoc", "thcs", "thpt", "dai-hoc"] | None, Query()
    ] = None,
    grade: Annotated[int | None, Query(ge=1, le=13, description="13 nghĩa là đại học")] = None,
    curriculum: Annotated[str | None, Query()] = None,
    topic: Annotated[str | None, Query()] = None,
    difficulty_min: Annotated[int | None, Query(ge=1, le=5)] = None,
    difficulty_max: Annotated[int | None, Query(ge=1, le=5)] = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    include_record: Annotated[bool, Query(description="Trả kèm toàn bộ bản ghi")] = False,
) -> SearchResponse:
    hits = search(
        conn,
        q,
        filters=Filters(
            kinds=kind,
            subject=subject,
            level=level,
            grade=grade,
            curriculum=curriculum,
            topic=topic,
            difficulty_min=difficulty_min,
            difficulty_max=difficulty_max,
        ),
        limit=limit,
        include_record=include_record,
    )
    return SearchResponse(query=q, total=len(hits), hits=hits)


@app.get("/formulas/{formula_id}/usage", response_model=list[Hit], tags=["tra cứu"],
         summary="Bài học và bài tập nào dùng công thức này")
def formula_usage(formula_id: str, conn: Conn, limit: int = 20) -> list[Hit]:
    if load_record(conn, "formula", formula_id) is None:
        raise HTTPException(404, f"Không có công thức {formula_id!r}.")
    return uses_formula(conn, formula_id, limit=limit)


@app.get("/formulas/{formula_id}/illustration", response_model=Illustration, tags=["tra cứu"],
         summary="Hình minh hoạ của công thức, kèm SVG nội tuyến")
def formula_illustration(formula_id: str, conn: Conn) -> Illustration:
    picture = illustrations.get(conn, formula_id)
    if picture is None:
        raise HTTPException(404, f"Công thức {formula_id!r} chưa có hình minh hoạ.")
    return picture


@app.get("/illustrations", response_model=list[Illustration], tags=["tra cứu"],
         summary="Duyệt kho minh hoạ theo môn · cấp · chủ đề · generator")
def browse_illustrations(
    conn: Conn,
    subject: str | None = None,
    level: str | None = None,
    topic: str | None = None,
    generator: str | None = None,
    q: str | None = None,
    limit: int = 60,
    with_svg: bool = False,
) -> list[Illustration]:
    """Đi thẳng vào kho hình thay vì đi vòng qua công thức.

    Khi thư viện còn 31 hình thì câu hỏi luôn là "công thức này có hình không".
    Thư viện lớn lên thì câu hỏi đổi chiều — "môn Lí bậc THPT đã có những hình
    gì" — và đường cũ không trả lời được.
    """
    return illustrations.browse(
        conn, subject=subject, level=level, topic=topic, generator=generator,
        query=q, limit=limit, with_svg=with_svg,
    )


@app.get("/illustrations/facets", tags=["tra cứu"],
         summary="Các giá trị lọc đang có và số hình của mỗi giá trị")
def illustration_facets(conn: Conn) -> dict[str, dict[str, int]]:
    return illustrations.facets(conn)


@app.get("/illustrations/{formula_id}.svg", tags=["tra cứu"],
         summary="Lấy thẳng file SVG để nhúng vào thẻ img",
         response_class=Response)
def illustration_svg(formula_id: str, conn: Conn) -> Response:
    picture = illustrations.get(conn, formula_id)
    if picture is None or not picture.svg:
        raise HTTPException(404, f"Không có SVG cho {formula_id!r}.")
    return Response(
        content=picture.svg,
        media_type="image/svg+xml",
        headers={
            "Cache-Control": "public, max-age=86400",
            # SVG do công cụ nội bộ sinh ra và đã được lọc mã chạy được, nhưng
            # trình duyệt vẫn nên bị cấm chạy script từ tài nguyên này.
            "Content-Security-Policy": "default-src 'none'; style-src 'unsafe-inline'",
            "X-Content-Type-Options": "nosniff",
        },
    )


# --------------------------------------------------------------------------- #
# Xử lí bài toán
# --------------------------------------------------------------------------- #


@app.post("/solve", response_model=SolveResponse, tags=["xử lí bài toán"],
          summary="Giải một bài toán và kiểm chứng lại bằng CAS")
def solve_endpoint(request: SolveRequest, conn: Conn) -> SolveResponse:
    try:
        return solve(conn, request)
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/solve/image", response_model=SolveResponse, tags=["xử lí bài toán"],
          summary="Giải bài toán từ ảnh chụp đề")
async def solve_image(
    conn: Conn,
    file: Annotated[UploadFile, File(description="Ảnh PNG/JPEG/WebP, tối đa 5 MB")],
    hint: Annotated[str, Form(description="Ghi chú thêm cho phần đọc đề")] = "",
    subject: Annotated[str | None, Form()] = None,
    level: Annotated[str | None, Form()] = None,
    heavy: Annotated[bool, Form(description="Dùng model mạnh hơn cho bài khó")] = False,
) -> SolveResponse:
    payload = await file.read()
    if len(payload) > 5 * 1024 * 1024:
        raise HTTPException(413, "Ảnh lớn hơn 5 MB.")
    if file.content_type not in {"image/png", "image/jpeg", "image/gif", "image/webp"}:
        raise HTTPException(415, f"Định dạng {file.content_type} không được hỗ trợ.")
    try:
        return solve(
            conn,
            SolveRequest(
                statement=hint,
                image_base64=base64.standard_b64encode(payload).decode("ascii"),
                image_media_type=file.content_type,
                subject=subject,
                level=level,
                heavy=heavy,
            ),
        )
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/classify", tags=["xử lí bài toán"],
          summary="Phân loại đề bài (không cần khoá API)")
def classify_endpoint(payload: dict[str, str], conn: Conn) -> dict[str, Any]:
    statement = (payload.get("statement") or "").strip()
    if not statement:
        raise HTTPException(400, "Thiếu trường `statement`.")
    return classify_by_retrieval(conn, statement).model_dump()


# --------------------------------------------------------------------------- #
# Lộ trình học
# --------------------------------------------------------------------------- #


@app.post("/roadmap", response_model=LearningPath, tags=["lộ trình học"],
          summary="Dựng lộ trình học tới một mục tiêu")
def roadmap_endpoint(request: RoadmapRequest, conn: Conn) -> LearningPath:
    """Mục tiêu nhận id bài học, id kỳ thi, hoặc từ khoá chủ đề.

    Không cần khoá API: lộ trình dựng hoàn toàn từ đồ thị tiên quyết của kho.
    """
    return roadmap.build(conn, request)


@app.get("/lessons/{lesson_id}/prerequisites", response_model=list[str],
         tags=["lộ trình học"], summary="Các bài phải học trước bài này")
def lesson_prerequisites(
    lesson_id: str,
    conn: Conn,
    recursive: Annotated[bool, Query(description="Lấy cả nhánh tiên quyết phía trên")] = False,
) -> list[str]:
    if load_record(conn, "lesson", lesson_id) is None:
        raise HTTPException(404, f"Không có bài học {lesson_id!r}.")
    graph = roadmap.prerequisite_graph(conn)
    if not recursive:
        return list(graph.get(lesson_id, []))
    needed, _ = roadmap.required_lessons(graph, [lesson_id], set())
    return sorted(needed - {lesson_id})


# --------------------------------------------------------------------------- #
# Chấm bài
# --------------------------------------------------------------------------- #


@app.post("/grade", response_model=GradeResult, tags=["chấm bài"],
          summary="Chấm một câu trả lời")
def grade_endpoint(request: GradeRequest, conn: Conn) -> GradeResult:
    try:
        return grading.grade(conn, request)
    except KeyError as exc:
        raise HTTPException(404, str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


@app.post("/diagnose", response_model=DiagnosisResult, tags=["chấm bài"],
          summary="Chấm cả loạt và chẩn đoán lỗ hổng kiến thức")
def diagnose_endpoint(request: DiagnosisRequest, conn: Conn) -> DiagnosisResult:
    if not request.answers:
        raise HTTPException(400, "Trường `answers` rỗng.")
    return grading.diagnose(conn, request)


@app.get("/practice", response_model=list[Hit], tags=["chấm bài"],
         summary="Đề xuất bài luyện theo kỹ năng")
def practice(
    conn: Conn,
    skill: Annotated[list[str], Query(description="Một hoặc nhiều kỹ năng cần luyện")],
    limit: Annotated[int, Query(ge=1, le=50)] = 10,
    difficulty_max: Annotated[int | None, Query(ge=1, le=5)] = None,
) -> list[Hit]:
    return problems_by_skill(conn, skill, limit=limit, difficulty_max=difficulty_max)


@app.get("/learners/{learner}/report", tags=["chấm bài"],
         summary="Báo cáo kỹ năng theo lịch sử làm bài")
def learner_report(learner: str, conn: Conn) -> dict[str, Any]:
    return grading.skill_report(conn, learner)


# --------------------------------------------------------------------------- #
# Đề thi thử
# --------------------------------------------------------------------------- #


@app.post("/exams/mock", response_model=MockExam, tags=["thi thử"],
          summary="Sinh đề thi thử theo bản thiết kế của kỳ thi")
def mock_exam_endpoint(request: MockExamRequest, conn: Conn) -> MockExam:
    """Bốc bài từ ngân hàng theo đúng tỉ trọng chủ đề của đề thật.

    Chủ đề nào kho chưa đủ bài thì báo trong `coverage` và `warnings` chứ không
    lấy bừa cho đủ số câu.
    """
    try:
        return mock_exam.generate(conn, request)
    except KeyError as exc:
        raise HTTPException(404, str(exc)) from exc


@app.post("/exams/mock/grade", response_model=MockExamResult, tags=["thi thử"],
          summary="Chấm bài thi thử, phân tích theo chủ đề")
def mock_exam_grade(submission: MockExamSubmission, conn: Conn) -> MockExamResult:
    try:
        return mock_exam.grade_exam(conn, submission)
    except KeyError as exc:
        raise HTTPException(404, str(exc)) from exc


# --------------------------------------------------------------------------- #
# Tiến độ học
# --------------------------------------------------------------------------- #


@app.get("/learners/{learner}/progress", tags=["tiến độ"],
         summary="Bức tranh tiến độ: đã học gì, thạo tới đâu, cần ôn gì")
def learner_progress(learner: str, conn: Conn) -> dict[str, Any]:
    return progress.overview(conn, learner=learner)


@app.post("/learners/{learner}/lessons/{lesson_id}", tags=["tiến độ"],
          summary="Đánh dấu đã học xong một bài giảng")
def complete_lesson(
    learner: str,
    lesson_id: str,
    conn: Conn,
    status: Annotated[Literal["done", "in-progress", "skipped"], Query()] = "done",
) -> dict[str, Any]:
    if load_record(conn, "lesson", lesson_id) is None:
        raise HTTPException(404, f"Không có bài học {lesson_id!r}.")
    progress.complete_lesson(conn, lesson_id, learner=learner, status=status)
    return {"learner": learner, "lesson_id": lesson_id, "status": status}


@app.get("/learners/{learner}/reviews", tags=["tiến độ"],
         summary="Kỹ năng đã tới hạn ôn, kèm bài tập để ôn")
def learner_reviews(
    learner: str,
    conn: Conn,
    limit: Annotated[int, Query(ge=1, le=50)] = 10,
) -> dict[str, Any]:
    return {
        "learner": learner,
        "due": progress.due_skills(conn, learner=learner, limit=limit),
        "problems": progress.review_problems(conn, learner=learner, limit=limit),
    }


@app.get("/learners/{learner}/mastery", tags=["tiến độ"],
         summary="Mức thạo từng kỹ năng, có giảm trọng theo thời gian")
def learner_mastery(learner: str, conn: Conn) -> dict[str, Any]:
    mastery = progress.skill_mastery(conn, learner=learner)
    ranked = sorted(mastery.values(), key=lambda e: e["mastery"])
    return {"learner": learner, "skills": ranked}


# --------------------------------------------------------------------------- #
# Lấy bản ghi theo id
# --------------------------------------------------------------------------- #
#
# Khai báo CUỐI CÙNG là cố ý. `/{collection}/{record_id}` khớp với mọi đường dẫn
# hai đoạn, nên nếu đặt trước thì nó nuốt luôn `/illustrations/<id>.svg` rồi trả
# 422 vì "illustrations" không nằm trong danh sách kho hợp lệ. FastAPI so khớp
# theo thứ tự khai báo, nên route bắt-tất phải đứng sau các route cụ thể.


@app.get("/{collection}/{record_id}", tags=["tra cứu"], summary="Lấy một bản ghi theo id")
def get_record(
    collection: Literal["formulas", "lessons", "problems", "exams"],
    record_id: str,
    conn: Conn,
) -> dict[str, Any]:
    record = load_record(conn, PATH_TO_KIND[collection], record_id)
    if record is None:
        raise HTTPException(404, f"Không có bản ghi {record_id!r} trong kho {collection}.")
    return record
