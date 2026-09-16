"""Truy xuất lai: BM25 (FTS5) trên hai kênh có dấu / không dấu, tuỳ chọn thêm
kênh vector, rồi hợp nhất bằng RRF (Reciprocal Rank Fusion).

Vì sao RRF chứ không cộng điểm thô: BM25 và cosine không cùng thang đo, cộng
thẳng thì kênh nào có phương sai lớn hơn sẽ nuốt kênh kia. RRF chỉ dùng thứ
hạng nên miễn nhiễm với chuyện đó và không cần hiệu chỉnh tham số.
"""

from __future__ import annotations

import json
import re
import sqlite3
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from itertools import pairwise
from typing import Any

from ..config import settings
from ..models import Hit, RecordKind
from ..skills import SkillMatcher
from ..skills import tokens as skill_tokens
from ..textnorm import fold

# BM25 trong FTS5 trả điểm ÂM, càng nhỏ càng khớp. Trọng số cột: tiêu đề và chủ
# đề đáng tin hơn thân bài.
_BM25_WEIGHTS = "8.0, 4.0, 1.0, 1.0"

_TOKEN_RE = re.compile(r"[0-9\w]+", re.UNICODE)

# Hư từ tiếng Việt và động từ ra đề. Chúng có mặt trong gần như mọi bản ghi nên
# BM25 chấm điểm gần bằng nhau cho tất cả — giữ lại chỉ làm loãng tín hiệu.
_STOPWORDS = {
    "la", "cua", "va", "voi", "mot", "cac", "co", "cho", "trong", "khi", "nao", "bao",
    "nhieu", "hay", "tim", "tinh", "biet", "duoc", "tai", "den", "tu", "theo", "sau",
    "day", "nay", "do", "thi", "ma", "nen", "se", "da", "cung", "hon", "nhu", "vao", "ra",
    "len", "xuong", "ve", "bang", "neu", "hoac", "khong", "phai", "dung", "sai", "gia",
    "tri", "ket", "qua", "bai", "toan", "cau", "hoi", "tren", "duoi", "moi", "tat", "ca",
    "the", "nhat", "hai", "ba", "bon", "nam", "dat", "goi", "xet", "sao", "vi",
}


def _is_useful(token: str) -> bool:
    """Token có mang thông tin tra cứu không?

    Số liệu trong đề (`2 kg`, `500 mL`, `x^2 - 9`) là dữ kiện của riêng bài đó,
    không giúp tìm công thức — mà lại rất nhiều, nên nếu để nguyên thì BM25 đi
    tìm các bản ghi tình cờ chứa cùng con số.
    """
    if len(token) < 2:
        return False
    if token.isdigit() and len(token) < 4:
        return False
    return token not in _STOPWORDS


def _useful_tokens(source: str) -> list[str]:
    return [t for t in _TOKEN_RE.findall(source) if _is_useful(t)]


def _adjacent_bigrams(source: str) -> list[str]:
    """Cụm hai từ **thật sự đứng cạnh nhau** trong câu gốc.

    Không được ghép qua đầu một từ đã lọc bỏ: "đạo hàm của hàm số" mà bỏ "của"
    rồi ghép thẳng sẽ đẻ ra cụm "hàm hàm" chưa từng tồn tại, và tệ hơn là
    những cụm sai nghĩa kéo hẳn kết quả đi chỗ khác.
    """
    tokens = _TOKEN_RE.findall(source)
    pairs: list[str] = []
    for first, second in pairwise(tokens):
        if _is_useful(first) and _is_useful(second):
            pairs.append(f"{first} {second}")
    return pairs


def _fts_query(text: str, *, folded: bool = False, phrases: bool = False) -> str:
    """Biến truy vấn tự do thành cú pháp FTS5 an toàn.

    Mọi ký tự đặc biệt của FTS5 (`"`, `*`, `:`, `^`, `NEAR`…) đều bị vô hiệu vì
    từng token được bọc trong dấu nháy kép.

    `phrases=True` dựng truy vấn theo **cụm hai từ liền nhau** thay vì từng từ
    rời. Tiếng Việt là ngôn ngữ đơn âm: "đạo hàm", "động năng", "nồng độ" chỉ
    mang nghĩa khi đi cạnh nhau, còn tách ra thì "hàm", "năng", "độ" khớp với
    gần như mọi bản ghi. Kênh cụm từ là thứ kéo đúng công thức lên đầu.
    """
    raw = fold(text) if folded else text
    tokens = _useful_tokens(fold(text)) if folded else _useful_tokens_preserving(text)
    if not tokens:
        tokens = _TOKEN_RE.findall(raw)[:8]  # truy vấn toàn hư từ: thà tìm còn hơn không
    if not tokens:
        return ""
    if phrases:
        bigrams = _adjacent_bigrams(fold(text) if folded else text)[:24]
        if not bigrams:
            return ""
        return " OR ".join(f'"{b}"' for b in bigrams)
    return " OR ".join(f'"{t}"' for t in tokens[:32])


def _useful_tokens_preserving(text: str) -> list[str]:
    """Như `_useful_tokens` nhưng giữ nguyên dấu tiếng Việt của token gốc."""
    original = _TOKEN_RE.findall(text)
    keep = set(_useful_tokens(fold(text)))
    return [t for t in original if fold(t) in keep]


@dataclass
class Filters:
    kinds: Sequence[str] | None = None
    subject: str | None = None
    subjects: Sequence[str] | None = None
    level: str | None = None
    curriculum: str | None = None
    grade: int | None = None
    topic: str | None = None
    difficulty_min: int | None = None
    difficulty_max: int | None = None
    exclude_ids: Sequence[str] = ()

    def where(self) -> tuple[str, list[Any]]:
        clauses: list[str] = []
        params: list[Any] = []
        if self.kinds:
            clauses.append(f"r.kind IN ({','.join('?' * len(self.kinds))})")
            params.extend(self.kinds)
        subjects = list(self.subjects or ([self.subject] if self.subject else []))
        if subjects:
            clauses.append(f"r.subject IN ({','.join('?' * len(subjects))})")
            params.extend(subjects)
        if self.level:
            clauses.append("r.level = ?")
            params.append(self.level)
        if self.curriculum:
            clauses.append("r.curriculum LIKE ?")
            params.append(f'%"{self.curriculum}"%')
        if self.grade is not None:
            # grades lưu dạng JSON '[11, 12]' — so khớp theo phần tử.
            clauses.append(
                "EXISTS (SELECT 1 FROM json_each(r.grades) g WHERE g.value = ?)"
            )
            params.append(self.grade)
        if self.topic:
            clauses.append("r.topic LIKE ?")
            params.append(f"%{self.topic}%")
        if self.difficulty_min is not None:
            clauses.append("COALESCE(r.difficulty, 3) >= ?")
            params.append(self.difficulty_min)
        if self.difficulty_max is not None:
            clauses.append("COALESCE(r.difficulty, 3) <= ?")
            params.append(self.difficulty_max)
        if self.exclude_ids:
            ids = list(self.exclude_ids)
            clauses.append(f"r.rid NOT IN ({','.join('?' * len(ids))})")
            params.extend(ids)
        return (" AND ".join(clauses) if clauses else "1=1"), params


def _bm25_channel(
    conn: sqlite3.Connection,
    query: str,
    filters: Filters,
    limit: int,
    *,
    folded: bool,
    phrases: bool = False,
) -> list[str]:
    """Trả về danh sách khoá `kind:rid` xếp theo độ khớp giảm dần."""
    match = _fts_query(query, folded=folded, phrases=phrases)
    if not match:
        return []
    column = "folded" if folded else "records_fts"
    where, params = filters.where()
    sql = f"""
        SELECT r.kind || ':' || r.rid AS key
        FROM records_fts f
        JOIN records r ON r.rowid = f.rowid
        WHERE {column} MATCH ? AND {where}
        ORDER BY bm25(records_fts, {_BM25_WEIGHTS})
        LIMIT ?
    """
    try:
        rows = conn.execute(sql, (match, *params, limit)).fetchall()
    except sqlite3.OperationalError:
        return []
    return [row["key"] for row in rows]


def _vector_channel(
    conn: sqlite3.Connection, query: str, filters: Filters, limit: int
) -> list[str]:
    """Kênh vector — chỉ chạy khi bảng `embeddings` có dữ liệu và có bộ nhúng."""
    from ..embed import embed_query, load_matrix  # nhập trễ: tránh kéo numpy khi không dùng

    matrix = load_matrix(conn)
    if matrix is None:
        return []
    vector = embed_query(query)
    if vector is None:
        return []
    import numpy as np

    scores = matrix.vectors @ vector
    order = np.argsort(-scores)[: limit * 4]
    allowed = _allowed_keys(conn, filters)
    keys: list[str] = []
    for idx in order:
        key = matrix.keys[int(idx)]
        if allowed is None or key in allowed:
            keys.append(key)
            if len(keys) >= limit:
                break
    return keys


def _allowed_keys(conn: sqlite3.Connection, filters: Filters) -> set[str] | None:
    where, params = filters.where()
    if where == "1=1":
        return None
    rows = conn.execute(
        f"SELECT r.kind || ':' || r.rid AS key FROM records r WHERE {where}", params
    ).fetchall()
    return {row["key"] for row in rows}


def rrf_fuse(channels: dict[str, list[str]], k: int = 60) -> dict[str, tuple[float, list[str]]]:
    """Hợp nhất nhiều bảng xếp hạng. Trả `key -> (điểm, các kênh đã khớp)`."""
    fused: dict[str, float] = {}
    provenance: dict[str, list[str]] = {}
    for channel_name, keys in channels.items():
        for rank, key in enumerate(keys, start=1):
            fused[key] = fused.get(key, 0.0) + 1.0 / (k + rank)
            provenance.setdefault(key, []).append(channel_name)
    return {key: (score, provenance[key]) for key, score in fused.items()}


def _hydrate(conn: sqlite3.Connection, keys: Iterable[str]) -> dict[str, sqlite3.Row]:
    keys = list(keys)
    if not keys:
        return {}
    out: dict[str, sqlite3.Row] = {}
    for i in range(0, len(keys), 400):
        chunk = keys[i : i + 400]
        placeholders = ",".join("?" * len(chunk))
        rows = conn.execute(
            "SELECT kind, rid, subject, level, topic, title, difficulty, payload,"
            " kind || ':' || rid AS key FROM records"
            f" WHERE kind || ':' || rid IN ({placeholders})",
            chunk,
        ).fetchall()
        out.update({row["key"]: row for row in rows})
    return out


def _snippet(kind: str, payload: dict[str, Any]) -> str:
    if kind == RecordKind.FORMULA.value:
        return payload.get("latex", "")[:220]
    if kind == RecordKind.LESSON.value:
        objectives = payload.get("objectives") or []
        return (objectives[0] if objectives else payload.get("content", ""))[:220]
    if kind == RecordKind.PROBLEM.value:
        return (payload.get("statement_vi") or payload.get("statement_en") or "")[:220]
    return (payload.get("overview") or "")[:220]


def search(
    conn: sqlite3.Connection,
    query: str,
    *,
    filters: Filters | None = None,
    limit: int = 10,
    include_record: bool = False,
    use_vector: bool = True,
) -> list[Hit]:
    """Tìm kiếm lai trên toàn bộ bốn kho."""
    filters = filters or Filters()
    query = (query or "").strip()
    if not query:
        return _browse(conn, filters, limit, include_record)

    pool = max(limit * 5, 40)
    channels = {
        "phrase": _bm25_channel(conn, query, filters, pool, folded=True, phrases=True),
        "bm25": _bm25_channel(conn, query, filters, pool, folded=False),
        "bm25_folded": _bm25_channel(conn, query, filters, pool, folded=True),
    }
    if use_vector:
        try:
            vector_keys = _vector_channel(conn, query, filters, pool)
        except Exception:  # kênh phụ hỏng không được làm sập tìm kiếm
            vector_keys = []
        if vector_keys:
            channels["vector"] = vector_keys

    fused = rrf_fuse(channels, k=settings.rrf_k)
    if not fused:
        return []
    ranked = sorted(fused.items(), key=lambda kv: -kv[1][0])[:limit]
    rows = _hydrate(conn, [key for key, _ in ranked])

    hits: list[Hit] = []
    for key, (score, provenance) in ranked:
        row = rows.get(key)
        if row is None:
            continue
        payload = json.loads(row["payload"])
        hits.append(
            Hit(
                kind=RecordKind(row["kind"]),
                id=row["rid"],
                title=row["title"],
                score=round(score, 6),
                subject=row["subject"] or "",
                level=row["level"] or "",
                topic=row["topic"] or "",
                snippet=_snippet(row["kind"], payload),
                channels=provenance,
                record=payload if include_record else None,
            )
        )
    return hits


def _browse(
    conn: sqlite3.Connection, filters: Filters, limit: int, include_record: bool
) -> list[Hit]:
    """Không có từ khoá thì duyệt theo bộ lọc."""
    where, params = filters.where()
    rows = conn.execute(
        "SELECT kind, rid, subject, level, topic, title, payload FROM records r"
        f" WHERE {where} ORDER BY r.kind, r.rid LIMIT ?",
        (*params, limit),
    ).fetchall()
    hits = []
    for row in rows:
        payload = json.loads(row["payload"])
        hits.append(
            Hit(
                kind=RecordKind(row["kind"]),
                id=row["rid"],
                title=row["title"],
                score=0.0,
                subject=row["subject"] or "",
                level=row["level"] or "",
                topic=row["topic"] or "",
                snippet=_snippet(row["kind"], payload),
                channels=["browse"],
                record=payload if include_record else None,
            )
        )
    return hits


# --------------------------------------------------------------------------- #
# Đi theo đồ thị
# --------------------------------------------------------------------------- #


def uses_formula(
    conn: sqlite3.Connection,
    formula_id: str,
    *,
    kinds: Sequence[str] | None = None,
    limit: int = 20,
) -> list[Hit]:
    """Đồ thị ngược: bài học và bài tập nào dùng công thức này.

    Đây chính là thứ `data/formulas/usage.json` mô tả, nhưng dựng lại từ cạnh
    trong DB nên luôn khớp với dữ liệu vừa nạp.
    """
    sql = (
        "SELECT r.kind, r.rid, r.title, r.subject, r.level, r.topic, r.payload"
        " FROM edges e JOIN records r ON r.kind = e.src_kind AND r.rid = e.src_id"
        " WHERE e.dst_id = ? AND e.rel IN ('uses_formula', 'must_memorize')"
    )
    params: list[Any] = [formula_id]
    if kinds:
        sql += f" AND r.kind IN ({','.join('?' * len(kinds))})"
        params.extend(kinds)
    sql += " ORDER BY r.kind, r.rid LIMIT ?"
    params.append(limit)
    rows = conn.execute(sql, params).fetchall()
    return [
        Hit(
            kind=RecordKind(row["kind"]),
            id=row["rid"],
            title=row["title"],
            score=1.0,
            subject=row["subject"] or "",
            level=row["level"] or "",
            topic=row["topic"] or "",
            snippet=_snippet(row["kind"], json.loads(row["payload"])),
            channels=["graph:uses_formula"],
        )
        for row in rows
    ]


def formulas_of(conn: sqlite3.Connection, kind: str, rid: str) -> list[str]:
    rows = conn.execute(
        "SELECT dst_id FROM edges WHERE src_kind = ? AND src_id = ? AND rel = 'uses_formula'",
        (kind, rid),
    ).fetchall()
    return [row["dst_id"] for row in rows]


def _token_document_frequency(
    conn: sqlite3.Connection, tokens: Sequence[str]
) -> tuple[dict[str, int], int]:
    """Số bài tập chứa mỗi token, và tổng số bài — để tính IDF."""
    if not tokens:
        return {}, 0
    placeholders = ",".join("?" * len(tokens))
    rows = conn.execute(
        f"SELECT token, COUNT(*) AS n FROM skill_tokens WHERE token IN ({placeholders})"
        " GROUP BY token",
        list(tokens),
    ).fetchall()
    total = conn.execute(
        "SELECT COUNT(*) AS n FROM records WHERE kind = 'problem'"
    ).fetchone()["n"]
    return {row["token"]: row["n"] for row in rows}, total


def problems_by_skill(
    conn: sqlite3.Connection,
    skills: Sequence[str],
    *,
    limit: int = 10,
    exclude: Sequence[str] = (),
    difficulty_max: int | None = None,
    threshold: float = 0.3,
) -> list[Hit]:
    """Bài tập luyện đúng các kỹ năng đang yếu.

    So khớp theo **token có trọng số IDF**, không theo chuỗi nguyên. Kho được
    soạn theo nhiều lát cắt độc lập nên cùng một kỹ năng có cả dạng chữ
    ("phân tích đa thức thành nhân tử") lẫn dạng slug
    ("phan-tich-da-thuc-thanh-nhan-tu"); so nguyên chuỗi thì hai nửa kho không
    bao giờ gợi ý được cho nhau.

    IDF là phần không thể bỏ: "áp dụng công thức" có mặt ở khắp nơi nên gần như
    không mang thông tin, còn "nhiễu xạ" thì rất đặc trưng. Không cân theo độ
    hiếm thì mọi bài đều "liên quan" tới mọi kỹ năng.
    """
    # Mỗi kỹ năng giữ tập token riêng. Gộp hết vào một tập rồi tính độ phủ là
    # sai về ngữ nghĩa: hỏi "bài nào luyện MỘT TRONG sáu kỹ năng này" mà lại đi
    # đo "bài nào phủ được CẢ SÁU". Không bài nào phủ nổi, và hàm âm thầm trả
    # về rỗng — đúng lúc người học có nhiều lỗ hổng nhất thì gợi ý biến mất.
    per_skill = [(skill, set(skill_tokens(skill))) for skill in skills]
    per_skill = [(skill, toks) for skill, toks in per_skill if toks]
    if not per_skill:
        return []

    query_tokens: set[str] = set()
    for _, toks in per_skill:
        query_tokens |= toks

    frequency, total = _token_document_frequency(conn, sorted(query_tokens))
    matcher = SkillMatcher(frequency, total)
    skill_weights = [
        (toks, sum(matcher.weight(t) for t in toks)) for _, toks in per_skill
    ]
    skill_weights = [(toks, weight) for toks, weight in skill_weights if weight > 0]
    if not skill_weights:
        return []

    placeholders = ",".join("?" * len(query_tokens))
    sql = (
        "SELECT r.kind, r.rid, r.title, r.subject, r.level, r.topic, r.payload,"
        "       r.difficulty, GROUP_CONCAT(DISTINCT st.token) AS hit_tokens"
        " FROM skill_tokens st"
        " JOIN records r ON r.kind = 'problem' AND r.rid = st.problem_id"
        f" WHERE st.token IN ({placeholders})"
    )
    params: list[Any] = sorted(query_tokens)
    if exclude:
        sql += f" AND r.rid NOT IN ({','.join('?' * len(exclude))})"
        params.extend(exclude)
    if difficulty_max is not None:
        sql += " AND COALESCE(r.difficulty, 3) <= ?"
        params.append(difficulty_max)
    # Lấy dư rồi mới chấm điểm: xếp hạng cuối phụ thuộc trọng số IDF, không
    # phải số token trùng, nên không cắt sớm ở tầng SQL được.
    sql += " GROUP BY r.rid LIMIT ?"
    params.append(max(limit * 20, 200))

    scored: list[tuple[float, sqlite3.Row]] = []
    for row in conn.execute(sql, params):
        matched = set((row["hit_tokens"] or "").split(","))
        # Độ phủ **tốt nhất trên một kỹ năng bất kỳ**, không phải trên tất cả.
        coverage = max(
            sum(matcher.weight(t) for t in matched & toks) / weight
            for toks, weight in skill_weights
        )
        if coverage >= threshold:
            scored.append((coverage, row))

    scored.sort(key=lambda pair: (-pair[0], pair[1]["difficulty"] or 3, pair[1]["rid"]))
    return [
        Hit(
            kind=RecordKind.PROBLEM,
            id=row["rid"],
            title=row["title"],
            score=round(coverage, 4),
            subject=row["subject"] or "",
            level=row["level"] or "",
            topic=row["topic"] or "",
            snippet=_snippet("problem", json.loads(row["payload"])),
            channels=["skill"],
        )
        for coverage, row in scored[:limit]
    ]


def lessons_for_formulas(
    conn: sqlite3.Connection, formula_ids: Sequence[str], *, limit: int = 5
) -> list[Hit]:
    """Bài giảng dạy các công thức này — dùng để vá lỗ hổng sau khi làm sai."""
    if not formula_ids:
        return []
    ids = list(formula_ids)
    placeholders = ",".join("?" * len(ids))
    rows = conn.execute(
        "SELECT r.kind, r.rid, r.title, r.subject, r.level, r.topic, r.payload,"
        "       COUNT(*) AS matched"
        " FROM edges e JOIN records r ON r.kind = 'lesson' AND r.rid = e.src_id"
        f" WHERE e.rel = 'uses_formula' AND e.dst_id IN ({placeholders})"
        " GROUP BY r.rid ORDER BY matched DESC LIMIT ?",
        (*ids, limit),
    ).fetchall()
    return [
        Hit(
            kind=RecordKind.LESSON,
            id=row["rid"],
            title=row["title"],
            score=float(row["matched"]),
            subject=row["subject"] or "",
            level=row["level"] or "",
            topic=row["topic"] or "",
            snippet=_snippet("lesson", json.loads(row["payload"])),
            channels=["graph:lesson_for_formula"],
        )
        for row in rows
    ]
