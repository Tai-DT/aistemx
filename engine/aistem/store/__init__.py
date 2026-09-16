"""Tầng lưu trữ: SQLite + FTS5 + đồ thị liên kết bốn kho."""

from . import illustrations
from .build import BuildReport, build_database, database_stats, ensure_built
from .db import connect, get_meta, init_schema, load_record, load_records, session, set_meta, stats
from .search import (
    Filters,
    formulas_of,
    lessons_for_formulas,
    problems_by_skill,
    rrf_fuse,
    search,
    uses_formula,
)

__all__ = [
    "BuildReport",
    "Filters",
    "build_database",
    "connect",
    "database_stats",
    "ensure_built",
    "formulas_of",
    "get_meta",
    "illustrations",
    "init_schema",
    "lessons_for_formulas",
    "load_record",
    "load_records",
    "problems_by_skill",
    "rrf_fuse",
    "search",
    "session",
    "set_meta",
    "stats",
    "uses_formula",
]
