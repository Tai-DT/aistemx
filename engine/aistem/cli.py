"""Giao diện dòng lệnh.

    aistem db build            dựng lại cơ sở dữ liệu từ kho JSON
    aistem search "dao ham"    tra cứu xuyên bốn kho
    aistem classify "..."      phân loại đề (không cần khoá API)
    aistem solve "..."         giải một bài toán, kiểm chứng bằng CAS
    aistem grade <id> "6"      chấm một câu trả lời
    aistem verify <id>         kiểm chứng lại lời giải có sẵn trong kho
    aistem serve               chạy REST API
"""

from __future__ import annotations

import json as json_module
from pathlib import Path
from typing import Annotated, Optional

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from . import __version__, grading, llm
from .cas import verify_answer
from .config import settings
from .models import DiagnosisRequest, GradeRequest, Problem, SolveRequest
from .pipeline import classify_by_retrieval, describe, encode_image
from .pipeline import solve as run_solve
from .store.build import build_database, ensure_built
from .store.db import connect, load_record, stats
from .store.search import Filters
from .store.search import search as run_search

app = typer.Typer(
    help="Hệ thống xử lí bài toán trên kho dữ liệu AISTEM.",
    add_completion=False,
)
db_app = typer.Typer(help="Quản lí cơ sở dữ liệu.", no_args_is_help=True)
app.add_typer(db_app, name="db")
console = Console()

_STATUS_STYLE = {
    "verified": "green",
    "refuted": "red",
    "inconclusive": "yellow",
    "unparsed": "dim",
    "skipped": "dim",
    "unchecked": "yellow",
    "cao": "green",
    "trung-binh": "yellow",
    "thap": "red",
}


def _style(value: str) -> str:
    return f"[{_STATUS_STYLE.get(value, 'white')}]{value}[/]"


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: Annotated[bool, typer.Option("--version", help="In phiên bản rồi thoát.")] = False,
) -> None:
    if version:
        console.print(f"aistem-engine {__version__}")
        raise typer.Exit()
    if ctx.invoked_subcommand is None:
        console.print(ctx.get_help())
        raise typer.Exit()


# --------------------------------------------------------------------------- #
# db
# --------------------------------------------------------------------------- #


@db_app.command("build")
def db_build(
    corpus: Annotated[Optional[Path], typer.Option(help="Thư mục gốc kho AISTEM.")] = None,
    out: Annotated[Optional[Path], typer.Option(help="Đường dẫn file .db muốn ghi.")] = None,
    verbose: Annotated[bool, typer.Option("-v", "--verbose")] = False,
) -> None:
    """Nạp bốn kho JSON vào SQLite và dựng chỉ mục toàn văn."""
    with console.status("Đang nạp kho..."):
        report = build_database(corpus_root=corpus, db_path=out, verbose=verbose)

    table = Table(title="Đã dựng cơ sở dữ liệu", show_header=True)
    table.add_column("Kho")
    table.add_column("Bản ghi", justify="right")
    for kind, count in report.counts.items():
        table.add_row(kind, f"{count:,}")
    table.add_row("[bold]tổng[/]", f"[bold]{sum(report.counts.values()):,}[/]")
    console.print(table)
    console.print(
        f"Cạnh liên kết: {report.edges:,} · kỹ năng: {report.skills:,} · "
        f"{report.files} file · {report.elapsed_s:.1f}s"
    )
    if report.dangling_edges:
        console.print(
            f"[yellow]{len(report.dangling_edges)} liên kết trỏ tới id không tồn tại[/]"
        )


@db_app.command("stats")
def db_stats() -> None:
    """In thống kê cơ sở dữ liệu."""
    conn = connect(readonly=True)
    try:
        data = stats(conn)
    finally:
        conn.close()
    console.print_json(json_module.dumps(data, ensure_ascii=False))


@db_app.command("pg-sync")
def db_pg_sync(
    url: Annotated[Optional[str], typer.Option("--url", help="Chuỗi kết nối PostgreSQL")] = None,
) -> None:
    """Đồng bộ toàn bộ cơ sở dữ liệu SQLite, học bổng và 4,351 bài toán sang PostgreSQL trên Docker."""
    from .store.postgres import (
        get_postgres_connection,
        init_postgres_schema,
        migrate_sqlite_to_postgres,
        migrate_scholarships_to_postgres,
        migrate_problems_to_postgres,
        get_postgres_summary,
    )
    from .config import settings

    target_url = url or settings.postgres_url
    sqlite_db = settings.database
    scholarships_file = settings.corpus_root / "data" / "scholarships" / "scholarships.json"
    problems_dir = settings.corpus_root / "data" / "problems"

    with console.status(f"[bold cyan]Đang kết nối PostgreSQL ({target_url})...[/]"):
        with get_postgres_connection(target_url) as conn:
            init_postgres_schema(conn)
            report = migrate_sqlite_to_postgres(sqlite_db, conn)
            sch_count = migrate_scholarships_to_postgres(scholarships_file, conn)
            prob_count = migrate_problems_to_postgres(problems_dir, conn)
            st = get_postgres_summary(conn)

    table = Table(title=f"Đồng bộ PostgreSQL Thành Công ({report['elapsed_seconds']}s)")
    table.add_column("Bảng / Thực thể", style="bold cyan")
    table.add_column("Số bản ghi", justify="right", style="green")
    table.add_row("Formulas (Công thức)", f"{st.get('formula', 0):,}")
    table.add_row("Lessons (Bài giảng)", f"{st.get('lesson', 0):,}")
    table.add_row("Problems (Bài tập)", f"{st.get('problem', 0):,}")
    table.add_row("Exams (Kỳ thi)", f"{st.get('exam', 0):,}")
    table.add_row("TỔNG RECORDS", f"{st.get('total_records', 0):,}")
    table.add_row("Edges (Đồ thị cạnh)", f"{st.get('edges', 0):,}")
    table.add_row("Problem Skills", f"{st.get('problem_skills', 0):,}")
    table.add_row("Illustrations (Minh họa)", f"{st.get('illustrations', 0):,}")
    table.add_row("Scholarships (Học bổng)", f"{st.get('scholarships', 0):,}")
    table.add_row("BẢNG PROBLEMS CHUYÊN SÂU", f"{st.get('problems', 0):,}")
    table.add_row("CAS Verified", f"{st.get('problems_cas_verified', 0):,}")
    console.print(table)


@db_app.command("pg-sync-problems")
def db_pg_sync_problems(
    url: Annotated[Optional[str], typer.Option("--url", help="Chuỗi kết nối PostgreSQL")] = None,
) -> None:
    """Nạp hoặc đồng bộ lại bảng problems từ các file JSON trong data/problems/."""
    from .store.postgres import get_postgres_connection, init_postgres_schema, migrate_problems_to_postgres, get_postgres_summary
    from .config import settings

    target_url = url or settings.postgres_url
    problems_dir = settings.corpus_root / "data" / "problems"

    with console.status(f"[bold cyan]Đang nạp bài toán vào PostgreSQL...[/]"):
        with get_postgres_connection(target_url) as conn:
            init_postgres_schema(conn)
            count = migrate_problems_to_postgres(problems_dir, conn)
            st = get_postgres_summary(conn)

    console.print(f"[bold green]✓ Đã đồng bộ thành công {count:,} bài toán vào bảng problems![/]")
    console.print(f"Tổng số bài toán trong DB: {st.get('problems', 0):,} (Đã xác minh CAS: {st.get('problems_cas_verified', 0):,})")


@db_app.command("verify-problems")
def db_verify_problems(
    subject: Annotated[Optional[str], typer.Option("--subject", "-s", help="Lọc theo môn (math, physics, chemistry, biology)")] = None,
    ptype: Annotated[Optional[str], typer.Option("--type", "-t", help="Lọc theo dạng (dien-so, trac-nghiem, tu-luan)")] = None,
    source_file: Annotated[Optional[str], typer.Option("--source", help="Lọc theo tệp (vd: vn-physics-diendtu.json)")] = None,
    limit: Annotated[Optional[int], typer.Option("--limit", "-n", help="Giới hạn số lượng bài kiểm tra")] = None,
    workers: Annotated[int, typer.Option("--workers", "-w", help="Số tiến trình kiểm tra song song")] = 4,
    recheck: Annotated[bool, typer.Option("--recheck", help="Kiểm tra lại cả bài đã xác thực")] = False,
    url: Annotated[Optional[str], typer.Option("--url", help="Chuỗi kết nối PostgreSQL")] = None,
) -> None:
    """Chạy pipeline kiểm định CAS tự động cho các bài toán trên PostgreSQL."""
    from .store.postgres import get_postgres_connection
    from .cas.problem_verifier import verify_problems_pipeline
    from .config import settings

    target_url = url or settings.postgres_url
    with get_postgres_connection(target_url) as conn:
        with console.status("[bold cyan]Đang chạy SymPy CAS kiểm định bài toán...[/]"):
            report = verify_problems_pipeline(
                conn,
                subject=subject,
                ptype=ptype,
                source_file=source_file,
                limit=limit,
                max_workers=workers,
                recheck=recheck,
            )

    table = Table(title=f"Báo Cáo Kiểm Định CAS Bài Toán ({report['elapsed_seconds']}s)")
    table.add_column("Chỉ tiêu", style="bold cyan")
    table.add_column("Số lượng / Giá trị", justify="right", style="green")
    table.add_row("Tổng số bài đã quét", f"{report['total']:,}")
    table.add_row("Xác thực thành công (Verified)", f"[bold green]{report['verified']:,}[/]")
    table.add_row("Bác bỏ / Lệch đáp án (Refuted)", f"[bold red]{report['refuted']:,}[/]")
    table.add_row("Chưa kết luận (Inconclusive)", f"{report['inconclusive']:,}")
    table.add_row("Chưa có cơ sở tính (Unchecked)", f"{report['unchecked']:,}")
    table.add_row("Lỗi kiểm tra (Error)", f"{report['error']:,}")
    table.add_row("Tốc độ xử lý", f"{report['throughput']} bài/giây")
    console.print(table)


@db_app.command("pg-stats")
def db_pg_stats(
    url: Annotated[Optional[str], typer.Option("--url", help="Chuỗi kết nối PostgreSQL")] = None,
) -> None:
    """In thống kê các bảng hiện có trên PostgreSQL."""
    from .store.postgres import get_postgres_connection, get_postgres_summary
    from .config import settings

    target_url = url or settings.postgres_url
    with get_postgres_connection(target_url) as conn:
        st = get_postgres_summary(conn)
    console.print_json(json_module.dumps(st, ensure_ascii=False))



# --------------------------------------------------------------------------- #
# tra cứu
# --------------------------------------------------------------------------- #


@app.command()
def search(
    query: Annotated[str, typer.Argument(help="Từ khoá; gõ không dấu vẫn ra kết quả.")],
    kind: Annotated[Optional[str], typer.Option(help="formula | lesson | problem | exam")] = None,
    subject: Annotated[Optional[str], typer.Option(help="math|physics|chemistry|biology")] = None,
    level: Annotated[Optional[str], typer.Option()] = None,
    grade: Annotated[Optional[int], typer.Option(help="Lớp 1-13, 13 là đại học.")] = None,
    curriculum: Annotated[Optional[str], typer.Option()] = None,
    limit: Annotated[int, typer.Option("-n", "--limit")] = 10,
    json: Annotated[bool, typer.Option("--json", help="In JSON thay vì bảng.")] = False,
) -> None:
    """Tra cứu xuyên bốn kho."""
    conn = connect(readonly=True)
    try:
        hits = run_search(
            conn,
            query,
            filters=Filters(
                kinds=[kind] if kind else None,
                subject=subject,
                level=level,
                grade=grade,
                curriculum=curriculum,
            ),
            limit=limit,
        )
    finally:
        conn.close()

    if json:
        console.print_json(
            json_module.dumps([h.model_dump(mode="json") for h in hits], ensure_ascii=False)
        )
        return
    if not hits:
        console.print("[yellow]Không tìm thấy gì.[/]")
        return

    table = Table(show_header=True, header_style="bold")
    table.add_column("kho", width=8)
    table.add_column("id", overflow="fold")
    table.add_column("tên", overflow="fold")
    table.add_column("chủ đề", overflow="fold")
    for hit in hits:
        table.add_row(hit.kind.value, hit.id, hit.title[:70], hit.topic[:34])
    console.print(table)


@app.command()
def classify(
    statement: Annotated[str, typer.Argument(help="Đề bài.")],
    json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Phân loại đề bài chỉ bằng kho, không gọi mô hình."""
    conn = connect(readonly=True)
    try:
        result = classify_by_retrieval(conn, statement)
    finally:
        conn.close()
    if json:
        console.print_json(result.model_dump_json())
        return
    console.print(Panel(describe(result), title="Phân loại", border_style="cyan"))
    console.print(f"Kỹ năng: {', '.join(result.skills) or '(chưa xác định)'}")
    console.print(f"Độ tin cậy: {result.confidence} · căn cứ: {result.rationale}")


# --------------------------------------------------------------------------- #
# xử lí bài toán
# --------------------------------------------------------------------------- #


@app.command()
def solve(
    statement: Annotated[str, typer.Argument(help="Đề bài. Để trống nếu dùng --image.")] = "",
    image: Annotated[Optional[Path], typer.Option(help="Ảnh chụp đề bài.")] = None,
    subject: Annotated[Optional[str], typer.Option(help="Ép môn.")] = None,
    level: Annotated[Optional[str], typer.Option(help="Ép cấp học.")] = None,
    curriculum: Annotated[Optional[str], typer.Option()] = None,
    heavy: Annotated[bool, typer.Option("--heavy", help="Dùng model mạnh hơn.")] = False,
    no_verify: Annotated[bool, typer.Option("--no-verify", help="Bỏ bước kiểm chứng CAS.")] = False,
    json: Annotated[bool, typer.Option("--json")] = False,
    save: Annotated[
        Optional[Path], typer.Option(help="Ghi kết quả ra file JSON đúng lược đồ kho problems.")
    ] = None,
) -> None:
    """Giải một bài toán rồi kiểm chứng lại bằng CAS."""
    image_b64 = media_type = None
    if image is not None:
        image_b64, media_type = encode_image(image)

    request = SolveRequest(
        statement=statement,
        image_base64=image_b64,
        image_media_type=media_type or "image/png",
        subject=subject,
        level=level,
        curriculum=curriculum,
        heavy=heavy,
        verify=not no_verify,
    )

    conn = connect()
    try:
        with console.status("Đang xử lí..."):
            response = run_solve(conn, request)
    finally:
        conn.close()

    if json:
        console.print_json(response.model_dump_json())
    else:
        _print_solution(response)

    if save is not None:
        record = response.as_problem_record(f"prob.{response.classification.subject}.moi.0001")
        save.write_text(
            json_module.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        console.print(f"[green]Đã ghi bản ghi đúng lược đồ kho vào {save}[/]")


def _print_solution(response) -> None:
    console.print(Panel(response.statement, title="Đề bài", border_style="blue"))
    console.print(f"[bold]Phân loại:[/] {describe(response.classification)}")

    if response.solution_steps:
        console.print("\n[bold]Lời giải[/]")
        checks = {c.index: c for c in response.verification.steps}
        for index, step in enumerate(response.solution_steps):
            check = checks.get(index)
            mark = _style(check.status) if check else ""
            console.print(f"  [cyan]{index + 1}.[/] {step.explain}")
            if step.latex:
                console.print(f"     [dim]{step.latex}[/]  {mark}")

    if response.answer:
        console.print(f"\n[bold green]Đáp án:[/] {response.answer}")

    verification = response.verification
    console.print(
        f"\n[bold]Kiểm chứng CAS:[/] đáp số {_style(verification.answer_status)}"
        f" — {verification.answer_detail}"
    )
    if verification.steps_total:
        console.print(
            f"  bước: {verification.steps_verified} xác nhận ·"
            f" {verification.steps_refuted} bác bỏ ·"
            f" {verification.steps_inconclusive} chưa kết luận /"
            f" {verification.steps_total}"
        )
    if verification.unit_status != "unchecked":
        console.print(f"  đơn vị: {_style(verification.unit_status)} — {verification.unit_detail}")

    console.print(f"\n[bold]Mức tin cậy:[/] {_style(response.confidence)}")
    if response.formulas_used:
        console.print("[bold]Công thức đã dùng:[/] " + ", ".join(response.formulas_used))
    for warning in response.warnings:
        console.print(f"[yellow]![/] {warning}")
    if response.context.illustrations:
        console.print("\n[bold]Hình minh hoạ[/]")
        for picture in response.context.illustrations:
            where = picture.svg_path or picture.raster_path or ""
            console.print(f"  {picture.caption_vi[:74]}")
            console.print(f"     [dim]data/illustrations/{where}[/]")

    if response.recommendations:
        console.print("\n[bold]Học tiếp[/]")
        for hit in response.recommendations:
            console.print(f"  [{hit.kind.value}] {hit.id} — {hit.title[:70]}")
    console.print(f"\n[dim]{response.elapsed_ms} ms · model {response.model or '(không dùng)'}[/]")


@app.command()
def verify(
    problem_id: Annotated[str, typer.Argument(help="id bài tập trong kho.")],
    json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Kiểm chứng lại lời giải có sẵn trong kho bằng CAS. Không cần khoá API."""
    conn = connect(readonly=True)
    try:
        record = load_record(conn, "problem", problem_id)
    finally:
        conn.close()
    if record is None:
        console.print(f"[red]Không có bài tập {problem_id!r}.[/]")
        raise typer.Exit(1)

    problem = Problem.model_validate(record)
    result = verify_answer(
        answer=problem.answer,
        answer_numeric=problem.answer_numeric,
        steps=[s.model_dump() for s in problem.solution_steps],
        tolerance=problem.tolerance,
        expected_unit=problem.answer_unit,
    )
    if json:
        console.print_json(result.model_dump_json())
        return

    console.print(Panel(problem.statement_vi, title=problem_id, border_style="blue"))
    console.print(f"Đáp án kho: [bold]{problem.answer}[/]")
    console.print(f"Đáp số: {_style(result.answer_status)} — {result.answer_detail}\n")
    table = Table(show_header=True, header_style="bold")
    table.add_column("#", width=3)
    table.add_column("trạng thái", width=13)
    table.add_column("biểu thức", overflow="fold")
    table.add_column("ghi chú", overflow="fold")
    for check in result.steps:
        table.add_row(
            str(check.index + 1), _style(check.status), (check.latex or "")[:56], check.detail[:60]
        )
    console.print(table)


# --------------------------------------------------------------------------- #
# chấm bài
# --------------------------------------------------------------------------- #


@app.command()
def grade(
    problem_id: Annotated[str, typer.Argument(help="id bài tập trong kho.")],
    answer: Annotated[str, typer.Argument(help="Câu trả lời của học sinh.")],
    json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Chấm một câu trả lời."""
    conn = connect()
    try:
        try:
            result = grading.grade(
                conn, GradeRequest(problem_id=problem_id, student_answer=answer)
            )
        except KeyError as exc:
            console.print(f"[red]{exc}[/]")
            raise typer.Exit(1) from exc
    finally:
        conn.close()

    if json:
        console.print_json(result.model_dump_json())
        return

    colour = "green" if result.correct else "red"
    console.print(
        Panel(
            f"{result.detail}\n\nĐáp án đúng: {result.expected}\nĐã trả lời: {result.received}",
            title=f"[{colour}]{result.verdict}[/] (điểm {result.score})",
            border_style=colour,
        )
    )
    if result.why_wrong:
        console.print(f"[yellow]Vì sao sai:[/] {result.why_wrong}")
    if result.hints:
        console.print("\n[bold]Gợi ý[/]")
        for i, hint in enumerate(result.hints, 1):
            console.print(f"  {i}. {hint}")
    if result.weak_skills:
        console.print("\n[bold]Kỹ năng cần củng cố:[/] " + ", ".join(result.weak_skills))
    if result.next_steps:
        console.print("\n[bold]Học tiếp[/]")
        for hit in result.next_steps:
            console.print(f"  [{hit.kind.value}] {hit.id} — {hit.title[:70]}")


@app.command()
def diagnose(
    answers_file: Annotated[
        Path, typer.Argument(help='File JSON dạng {"prob.id": "câu trả lời", ...}')
    ],
    json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Chấm cả loạt câu rồi chỉ ra lỗ hổng kiến thức."""
    answers = json_module.loads(answers_file.read_text(encoding="utf-8"))
    conn = connect()
    try:
        result = grading.diagnose(conn, DiagnosisRequest(answers=answers))
    finally:
        conn.close()

    if json:
        console.print_json(result.model_dump_json())
        return
    console.print(Panel(result.summary, title="Chẩn đoán", border_style="cyan"))
    if result.weak_skills:
        table = Table(show_header=True, header_style="bold")
        table.add_column("kỹ năng", overflow="fold")
        table.add_column("đúng/làm", justify="right")
        for skill in result.weak_skills:
            table.add_row(skill.skill, f"{skill.correct}/{skill.attempted}")
        console.print(table)
    for title, hits in (
        ("Bài giảng nên đọc lại", result.recommended_lessons),
        ("Bài tập nên luyện", result.recommended_problems),
    ):
        if hits:
            console.print(f"\n[bold]{title}[/]")
            for hit in hits:
                console.print(f"  {hit.id} — {hit.title[:70]}")


# --------------------------------------------------------------------------- #
# server
# --------------------------------------------------------------------------- #


@app.command()
def illus(
    formula_id: Annotated[
        Optional[str], typer.Argument(help="Id công thức; bỏ trống để duyệt.")
    ] = None,
    subject: Annotated[Optional[str], typer.Option(help="math|physics|chemistry|biology")] = None,
    level: Annotated[Optional[str], typer.Option(help="tieu-hoc|thcs|thpt|dai-hoc")] = None,
    topic: Annotated[Optional[str], typer.Option()] = None,
    generator: Annotated[Optional[str], typer.Option(help="Lọc theo tên generator.")] = None,
    query: Annotated[Optional[str], typer.Option("-q", "--query")] = None,
    limit: Annotated[int, typer.Option("-n", "--limit")] = 40,
    out: Annotated[Optional[str], typer.Option("--out", help="Ghi SVG ra file.")] = None,
    facets: Annotated[bool, typer.Option("--facets", help="Liệt kê các giá trị lọc.")] = False,
) -> None:
    """Duyệt kho minh hoạ, hoặc xuất SVG của một công thức."""
    from .store import illustrations as illus_store

    ensure_built()
    conn = connect(readonly=True)
    try:
        if facets:
            for name, values in illus_store.facets(conn).items():
                console.print(f"[bold]{name}[/]")
                for value, count in values.items():
                    console.print(f"   {count:5d}  {value}")
            return

        if formula_id:
            picture = illus_store.get(conn, formula_id)
            if picture is None:
                console.print(f"[yellow]{formula_id} chưa có hình minh hoạ.[/]")
                raise typer.Exit(1)
            if out:
                if not picture.svg:
                    console.print(f"[yellow]{formula_id} không có SVG để ghi ra file.[/]")
                    raise typer.Exit(1)
                Path(out).write_text(picture.svg, encoding="utf-8")
                console.print(f"[green]đã ghi[/] {out}")
            else:
                console.print(f"[bold]{picture.formula_id}[/]  ({picture.generator})")
                if picture.caption_vi:
                    console.print(f"  {picture.caption_vi}")
                console.print(f"  [dim]data/illustrations/{picture.svg_path}[/]")
            return

        rows = illus_store.browse(
            conn, subject=subject, level=level, topic=topic,
            generator=generator, query=query, limit=limit,
        )
        if not rows:
            console.print("[yellow]Không có hình nào khớp bộ lọc.[/]")
            return
        table = Table(show_header=True, header_style='bold')
        for column in ("công thức", "môn", "cấp", "generator", "chủ đề"):
            table.add_column(column, overflow="fold")
        for picture in rows:
            extra = picture.model_extra or {}
            table.add_row(
                picture.formula_id, extra.get("subject", ""), extra.get("level", ""),
                picture.generator, (extra.get("topic", "") or "")[:34],
            )
        console.print(table)
        console.print(f"[dim]{len(rows)} hình. Xuất cả kho ra một file HTML tự chứa:[/]")
        console.print("[dim]  python3 tools/export_atlas.py[/]")
    finally:
        conn.close()


@app.command()
def serve(
    host: Annotated[str, typer.Option()] = settings.host,
    port: Annotated[int, typer.Option()] = settings.port,
    reload: Annotated[bool, typer.Option("--reload", help="Tự nạp lại khi sửa code.")] = False,
) -> None:
    """Chạy REST API. Tài liệu tương tác ở /docs."""
    import uvicorn

    ensure_built()
    if not llm.available():
        console.print(
            "[yellow]Chưa có khoá API: /solve chỉ trả phân loại và ngữ cảnh, "
            "chưa giải bài. Các endpoint còn lại chạy đầy đủ.[/]"
        )
    console.print(f"[green]http://{host}:{port}/docs[/]")
    uvicorn.run("aistem.api.main:app", host=host, port=port, reload=reload)


if __name__ == "__main__":
    app()


@app.command()
def audit(
    limit: Annotated[
        int, typer.Option("-n", "--limit", help="Số bài tập lấy mẫu; 0 nghĩa là quét cả kho.")
    ] = 400,
    seed: Annotated[int, typer.Option(help="Hạt giống lấy mẫu, để lặp lại được.")] = 11,
    json: Annotated[bool, typer.Option("--json")] = False,
    show: Annotated[int, typer.Option(help="Số bản ghi có vấn đề in ra.")] = 8,
) -> None:
    """Đo chất lượng hệ thống bằng cách chạy nó ngược lại trên chính kho.

    Không cần khoá API. Chạy lại sau mỗi lần kho mở rộng.

    Mẫu 400 bài mặc định chạy khoảng 35 giây và đã đủ đại diện. `-n 0` quét cả
    kho nhưng mất nhiều phút: kho có một cụm bài (chuỗi Fourier, ma trận lớn)
    mà SymPy xử lí rất nặng, và chúng chi phối gần hết thời gian chạy.
    """
    from . import audit as audit_module

    conn = connect(readonly=True)
    try:
        with console.status("Đang đo..."):
            report = audit_module.run(conn, limit=limit or None, seed=seed)
    finally:
        conn.close()

    if json:
        console.print_json(json_module.dumps(report.as_dict(), ensure_ascii=False))
        raise typer.Exit(0 if report.healthy else 1)

    for name, check in report.checks.items():
        mark = "[green]đạt[/]" if check.get("ok", True) else "[red]KHÔNG ĐẠT[/]"
        console.print(f"\n[bold]{name}[/] — {check.get('mô tả', '')}  {mark}")
        for key, value in check.items():
            if key in {"mô tả", "ok"}:
                continue
            console.print(f"    {key}: {value}")

    if report.findings:
        console.print(f"\n[bold]Bản ghi có vấn đề[/] ({len(report.findings)} chỗ)")
        for finding in report.findings[:show]:
            console.print(f"  [{finding.check}] {finding.record_id}\n     {finding.detail[:96]}")

    verdict = "[green]Hệ thống lành[/]" if report.healthy else "[red]Có phép đo không đạt[/]"
    console.print(f"\n{verdict} · {report.elapsed_s:.0f}s")
    raise typer.Exit(0 if report.healthy else 1)


@app.command()
def roadmap(
    goal: Annotated[
        str,
        typer.Argument(help="Mục tiêu: id bài học, id kỳ thi, hoặc từ khoá chủ đề."),
    ],
    subject: Annotated[Optional[str], typer.Option(help="Giới hạn môn.")] = None,
    level: Annotated[Optional[str], typer.Option(help="Giới hạn cấp học.")] = None,
    curriculum: Annotated[Optional[str], typer.Option()] = None,
    known: Annotated[
        Optional[Path], typer.Option(help="File JSON chứa danh sách id bài đã nắm.")
    ] = None,
    practice: Annotated[int, typer.Option(help="Số bài luyện sau mỗi bài học.")] = 2,
    minutes: Annotated[int, typer.Option(help="Số phút mỗi buổi học.")] = 60,
    max_lessons: Annotated[int, typer.Option(help="Trần số bài học.")] = 40,
    sessions: Annotated[bool, typer.Option("--sessions", help="In lịch theo buổi.")] = False,
    json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Dựng lộ trình học tới một mục tiêu. Không cần khoá API."""
    from . import roadmap as roadmap_module
    from .models import RoadmapRequest

    known_ids = json_module.loads(known.read_text(encoding="utf-8")) if known else []
    request = RoadmapRequest(
        goal=goal, subject=subject, level=level, curriculum=curriculum,
        known_lessons=known_ids, practice_per_lesson=practice,
        minutes_per_session=minutes, max_lessons=max_lessons,
    )
    conn = connect(readonly=True)
    try:
        path = roadmap_module.build(conn, request)
    finally:
        conn.close()

    if json:
        console.print_json(path.model_dump_json())
        return

    console.print(Panel(path.summary, title=f"Lộ trình: {goal}", border_style="cyan"))
    for warning in path.warnings:
        console.print(f"[yellow]![/] {warning}")
    if not path.milestones:
        raise typer.Exit(1)

    if sessions:
        for session_ in path.sessions:
            console.print(f"\n[bold]Buổi {session_.index}[/] · {session_.minutes:.0f} phút")
            for item in session_.items:
                mark = "[cyan]bài học[/]" if item.kind == "lesson" else "[dim]luyện  [/]"
                console.print(f"  {mark} {item.title[:66]}")
        return

    table = Table(show_header=True, header_style="bold")
    table.add_column("#", width=3, justify="right")
    table.add_column("cấp", width=8)
    table.add_column("bài học", overflow="fold")
    table.add_column("phút", width=5, justify="right")
    table.add_column("luyện", width=5, justify="right")
    for milestone in path.milestones:
        table.add_row(
            str(milestone.order),
            milestone.lesson.level,
            milestone.lesson.title[:64],
            f"{milestone.lesson.minutes:.0f}",
            str(len(milestone.practice)),
        )
    console.print(table)
    console.print(
        f"[bold]Tổng:[/] {path.total_hours} giờ · {len(path.sessions)} buổi "
        f"{request.minutes_per_session} phút"
    )


progress_app = typer.Typer(help="Theo dõi tiến độ học.", no_args_is_help=True)
app.add_typer(progress_app, name="progress")


@progress_app.command("show")
def progress_show(
    learner: Annotated[str, typer.Option(help="Người học.")] = "local",
    json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Đã học gì, thạo tới đâu, cần ôn gì."""
    from . import progress as progress_module

    conn = connect(readonly=True)
    try:
        data = progress_module.overview(conn, learner=learner)
        mastery = progress_module.skill_mastery(conn, learner=learner)
        due = progress_module.due_skills(conn, learner=learner, limit=8)
    finally:
        conn.close()

    if json:
        console.print_json(json_module.dumps(
            {"overview": data, "due": due}, ensure_ascii=False))
        return

    console.print(Panel(
        f"{data['lessons_done']} bài đã học · {data['study_hours']} giờ · "
        f"{data['correct']}/{data['attempts']} bài tập đúng ({data['accuracy']:.0%})\n"
        f"{data['skills_tracked']} kỹ năng đang theo dõi, {data['skills_weak']} còn yếu · "
        f"{data['reviews_due']} kỹ năng tới hạn ôn",
        title=f"Tiến độ: {learner}", border_style="cyan"))

    weak = sorted((e for e in mastery.values() if e["weak"]), key=lambda e: e["mastery"])
    if weak:
        table = Table(show_header=True, header_style="bold")
        table.add_column("kỹ năng còn yếu", overflow="fold")
        table.add_column("mức thạo", justify="right", width=9)
        table.add_column("đã làm", justify="right", width=7)
        for entry in weak[:10]:
            table.add_row(entry["skill"][:60], f"{entry['mastery']:.0%}", str(entry["attempts"]))
        console.print(table)
    if due:
        console.print("\n[bold]Tới hạn ôn[/]")
        for entry in due:
            console.print(f"  {entry['skill'][:60]} · quá hạn {entry['overdue_days']:.0f} ngày")


@progress_app.command("done")
def progress_done(
    lesson_id: Annotated[str, typer.Argument(help="id bài học đã học xong.")],
    learner: Annotated[str, typer.Option()] = "local",
) -> None:
    """Đánh dấu đã học xong một bài giảng."""
    from . import progress as progress_module

    conn = connect()
    try:
        if load_record(conn, "lesson", lesson_id) is None:
            console.print(f"[red]Không có bài học {lesson_id!r}.[/]")
            raise typer.Exit(1)
        progress_module.complete_lesson(conn, lesson_id, learner=learner)
    finally:
        conn.close()
    console.print(f"[green]Đã ghi:[/] {learner} học xong {lesson_id}")


@progress_app.command("review")
def progress_review(
    learner: Annotated[str, typer.Option()] = "local",
    limit: Annotated[int, typer.Option("-n", "--limit")] = 10,
) -> None:
    """Bài tập nên ôn hôm nay, theo lịch giãn cách."""
    from . import progress as progress_module

    conn = connect(readonly=True)
    try:
        due = progress_module.due_skills(conn, learner=learner, limit=limit)
        problems = progress_module.review_problems(conn, learner=learner, limit=limit)
    finally:
        conn.close()

    if not due:
        console.print("[green]Chưa có kỹ năng nào tới hạn ôn.[/]")
        return
    console.print(f"[bold]{len(due)} kỹ năng tới hạn ôn[/]")
    for entry in due:
        console.print(f"  {entry['skill'][:62]} · quá hạn {entry['overdue_days']:.0f} ngày")
    if problems:
        console.print("\n[bold]Bài tập để ôn[/]")
        for hit in problems:
            console.print(f"  {hit.id} — {hit.title[:64]}")


@app.command("mock-exam")
def mock_exam_command(
    exam_id: Annotated[str, typer.Argument(help="id hồ sơ kỳ thi, ví dụ exam.ap-calculus-bc.")],
    count: Annotated[
        Optional[int], typer.Option("-n", "--count", help="Số câu; bỏ trống thì theo đề thật.")
    ] = None,
    difficulty_max: Annotated[Optional[int], typer.Option(help="Trần độ khó 1-5.")] = None,
    seed: Annotated[int, typer.Option(help="Cùng seed cho cùng một đề.")] = 0,
    solutions: Annotated[bool, typer.Option("--solutions", help="Kèm đáp án.")] = False,
    json: Annotated[bool, typer.Option("--json")] = False,
) -> None:
    """Sinh đề thi thử theo bản thiết kế của kỳ thi. Không cần khoá API."""
    from . import mock_exam as mock_exam_module
    from .models import MockExamRequest

    conn = connect(readonly=True)
    try:
        exam = mock_exam_module.generate(conn, MockExamRequest(
            exam_id=exam_id, question_count=count, difficulty_max=difficulty_max,
            seed=seed, include_solutions=solutions,
        ))
    except KeyError as exc:
        console.print(f"[red]{exc}[/]")
        raise typer.Exit(1) from exc
    finally:
        conn.close()

    if json:
        console.print_json(exam.model_dump_json())
        return

    console.print(Panel(f"{exam.name}\n{exam.summary}", title="Đề thi thử", border_style="cyan"))
    for warning in exam.warnings:
        console.print(f"[yellow]![/] {warning}")

    table = Table(show_header=True, header_style="bold", title="Phủ theo bản thiết kế")
    table.add_column("trọng số", justify="right", width=9)
    table.add_column("cần", justify="right", width=4)
    table.add_column("được", justify="right", width=5)
    table.add_column("chủ đề", overflow="fold")
    for item in exam.coverage:
        mark = "" if item.complete else "[yellow]"
        table.add_row(f"{mark}{item.weight_percent:.0f}%", str(item.wanted),
                      str(item.got), item.topic[:56])
    console.print(table)

    console.print()
    for question in exam.questions:
        console.print(f"[bold]Câu {question.order}.[/] [dim]({question.type})[/] "
                      f"{question.statement[:150]}")
        for choice in question.choices:
            console.print(f"     {choice.get('key')}. {str(choice.get('text'))[:80]}")
        if solutions and question.answer:
            console.print(f"     [green]Đáp án:[/] {question.answer[:70]}")
