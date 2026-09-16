"""Bước phân loại đề: môn, cấp, chủ đề, dạng, độ khó, kỹ năng.

Chạy hai tầng. Tầng một thuần truy xuất — lấy các bài tập giống nhất trong kho
rồi bỏ phiếu theo trọng số độ khớp. Tầng này không cần khoá API, không tốn
tiền, và với đề nằm trong vùng kho đã phủ thì đã đủ chính xác. Tầng hai gọi
Claude để tinh chỉnh và đặt tên chủ đề, chỉ chạy khi có khoá và khi tầng một
chưa đủ tự tin.
"""

from __future__ import annotations

import sqlite3
from collections import Counter
from typing import Any

from .. import llm
from ..models import SUBJECT_VI, Classification
from ..store.search import Filters, search
from ..textnorm import fold

CLASSIFY_SCHEMA: dict[str, Any] = {
    "type": "object",
    "required": ["subject", "level", "topic", "type", "difficulty", "skills", "confidence"],
    "properties": {
        "subject": {
            "type": "string",
            "enum": ["math", "physics", "chemistry", "biology"],
            "description": "Môn của bài toán",
        },
        "level": {
            "type": "string",
            "enum": ["tieu-hoc", "thcs", "thpt", "dai-hoc"],
            "description": "Cấp học mà đề này thuộc về",
        },
        "grades": {
            "type": "array",
            "items": {"type": "integer", "minimum": 1, "maximum": 13},
            "description": "Các lớp áp dụng; 13 nghĩa là bậc đại học",
        },
        "curriculum": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": ["vn-gdpt-2018", "ap", "ib", "a-level", "intl-undergrad",
                         "olympiad", "ru-east-eu"],
            },
        },
        "topic": {"type": "string", "description": "Tên chủ đề bằng tiếng Việt, ngắn gọn"},
        "type": {
            "type": "string",
            "enum": ["trac-nghiem", "tu-luan", "dien-so", "dung-sai", "ghep-doi"],
            "description": "dien-so khi đáp án là một con số, tu-luan khi cần trình bày",
        },
        "difficulty": {
            "type": "integer",
            "minimum": 1,
            "maximum": 5,
            "description": "1 nhận biết, 2 thông hiểu, 3 vận dụng, 4 vận dụng cao, 5 olympiad",
        },
        "skills": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Kỹ năng bài này kiểm tra, viết bằng tiếng Việt, 2-5 mục",
        },
        "tags": {"type": "array", "items": {"type": "string"}},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "rationale": {"type": "string", "description": "Một câu giải thích căn cứ phân loại"},
    },
}

CLASSIFY_SYSTEM = """Bạn phân loại bài tập Toán - Lí - Hoá - Sinh cho hệ thống AISTEM.
Chỉ phân loại, tuyệt đối không giải bài.
Bốn trục phân loại phải khớp với quy ước của kho:
- subject: math | physics | chemistry | biology
- level: tieu-hoc (lớp 1-5) | thcs (6-9) | thpt (10-12) | dai-hoc
- grades: mảng số lớp, 13 nghĩa là bậc đại học
- curriculum: vn-gdpt-2018 | ap | ib | a-level | intl-undergrad | olympiad | ru-east-eu
Đặt confidence thấp khi đề mơ hồ hoặc thiếu dữ kiện, đừng đoán bừa cho có."""

#: Từ khoá đặc trưng từng môn — dùng khi kho không trả về bài nào đủ giống.
_SUBJECT_HINTS = {
    "math": ("dao ham", "tich phan", "gioi han", "phuong trinh", "ham so", "vecto",
             "xac suat", "ma tran", "so phuc", "day so", "hinh hoc", "tam giac", "logarit",
             # Hình học phổ thông cơ bản: kho bài tập gần như không phủ tiểu học
             # và THCS, nên đây là chỗ duy nhất bắt được các bài này.
             "chu vi", "dien tich", "the tich", "hinh chu nhat", "hinh vuong",
             "hinh tron", "hinh thang", "hinh binh hanh", "canh huyen", "duong cheo",
             "phan so", "ti le", "trung binh cong", "boi chung", "uoc chung"),
    "physics": ("van toc", "gia toc", "luc", "dong nang", "the nang", "dien truong",
                "tu truong", "song", "dao dong", "quang", "hat nhan", "nhiet do", "ap suat"),
    "chemistry": ("mol", "dung dich", "nong do", "phan ung", "axit", "bazo", "muoi",
                  "oxi hoa", "khu", "can bang", "ph", "este", "ancol", "kim loai", "electron"),
    "biology": ("te bao", "adn", "arn", "gen", "protein", "quang hop", "ho hap",
                "di truyen", "nhiem sac the", "quan the", "enzym", "sinh thai", "tien hoa"),
}


#: Trọng số giảm theo cấp số nhân theo thứ hạng. Điểm RRF thô chênh nhau quá ít
#: (1/61 so với 1/62) nên nếu bỏ phiếu bằng nó thì bài khớp nhất và bài thứ tám
#: gần như ngang phiếu, và chủ đề bầu ra thường là của một bài chỉ trùng vài từ.
_RANK_DECAY = 0.55


def _vote(hits: list, attribute: str) -> tuple[Any, float]:
    """Bỏ phiếu theo thứ hạng. Trả (giá trị thắng, tỉ lệ phiếu)."""
    tally: Counter = Counter()
    for rank, hit in enumerate(hits):
        record = hit.record or {}
        value = record.get(attribute) or getattr(hit, attribute, None)
        if isinstance(value, list):
            value = value[0] if value else None
        if value:
            tally[value] += _RANK_DECAY**rank
    if not tally:
        return None, 0.0
    winner, weight = tally.most_common(1)[0]
    return winner, weight / sum(tally.values())


def _subject_from_keywords(statement: str) -> tuple[str | None, float]:
    folded = fold(statement)
    scores = {
        subject: sum(1 for hint in hints if hint in folded)
        for subject, hints in _SUBJECT_HINTS.items()
    }
    best = max(scores, key=lambda s: scores[s])
    total = sum(scores.values())
    if scores[best] == 0:
        return None, 0.0
    return best, scores[best] / total


def classify_by_retrieval(conn: sqlite3.Connection, statement: str) -> Classification:
    """Phân loại chỉ bằng kho, không gọi mô hình.

    Bỏ phiếu từ **cả hai** kho, vì hai kho phủ hai vùng khác nhau:

    * Kho bài tập tập trung ở THPT và đại học theo chương trình quốc tế. Hỏi nó
      một bài chu vi hình chữ nhật lớp 4 thì nó vẫn trả về bài gần nhất nó có —
      và bài ấy là THPT. Tin theo là gán sai cấp học, rồi bước truy xuất sau đó
      lọc theo cấp sai và trả về công thức chẳng liên quan.
    * Kho công thức phủ liền mạch từ lớp 1 tới đại học ở cả bốn môn, nên nó mới
      là căn cứ đáng tin cho `subject` và `level`.

    Vậy: môn và cấp lấy theo công thức, độ khó / dạng / kỹ năng lấy theo bài tập.
    """
    problems = search(
        conn, statement, filters=Filters(kinds=["problem"]), limit=8, include_record=True
    )
    formulas = search(
        conn, statement, filters=Filters(kinds=["formula"]), limit=8, include_record=True
    )

    subject, subject_share = _vote(formulas, "subject")
    problem_subject, problem_share = _vote(problems, "subject")
    if problem_subject and problem_share > subject_share + 0.2:
        subject, subject_share = problem_subject, problem_share

    guessed, keyword_share = _subject_from_keywords(statement)
    if guessed and (not subject or (keyword_share >= 0.6 and subject_share < 0.6)):
        subject, subject_share = guessed, max(keyword_share, subject_share)

    # Cấp học: chỉ tính phiếu của các bản ghi đúng môn đã chốt, không thì công
    # thức Vật lí lạc vào sẽ kéo cấp lên.
    on_subject = [h for h in formulas if h.subject == subject] or formulas
    level, _ = _vote(on_subject, "level")
    topic, _ = _vote(on_subject, "topic")
    curriculum, _ = _vote(problems, "curriculum")

    difficulties = [
        (h.record or {}).get("difficulty") for h in problems if (h.record or {}).get("difficulty")
    ]
    skills: Counter = Counter()
    for hit in problems[:5]:
        for skill in (hit.record or {}).get("skills", []):
            skills[skill] += 1

    return Classification(
        subject=subject or "math",
        level=level or "thpt",
        grades=[],
        curriculum=[curriculum] if curriculum else [],
        topic=topic or "",
        type="tu-luan",
        difficulty=round(sum(difficulties) / len(difficulties)) if difficulties else 3,
        skills=[s for s, _ in skills.most_common(4)],
        tags=[],
        confidence=round(subject_share, 2),
        rationale=(
            f"Suy từ {len(formulas)} công thức và {len(problems)} bài tập giống nhất"
            if formulas or problems
            else "Kho không có gì đủ giống, phân loại theo từ khoá"
        ),
        source="retrieval",
    )


def classify(
    conn: sqlite3.Connection,
    statement: str,
    *,
    hint_subject: str | None = None,
    hint_level: str | None = None,
    hint_curriculum: str | None = None,
    use_llm: bool = True,
    model: str | None = None,
) -> Classification:
    """Phân loại đề bài. Người dùng ép trục nào thì trục đó thắng tuyệt đối."""
    baseline = classify_by_retrieval(conn, statement)

    if use_llm and llm.available() and baseline.confidence < 0.95:
        neighbours = "\n".join(
            f"- [{h.id}] môn {h.subject}, cấp {h.level}, chủ đề {h.topic}, "
            f"độ khó {(h.record or {}).get('difficulty', '?')}: {h.title[:120]}"
            for h in search(
                conn, statement, filters=Filters(kinds=["problem"]), limit=6, include_record=True
            )
        )
        prompt = (
            f"Phân loại bài tập sau.\n\n### Đề bài\n{statement}\n\n"
            f"### Các bài gần nhất trong kho (tham khảo, có thể sai)\n"
            f"{neighbours or '(không có)'}\n\n"
            "Trả kết quả phân loại."
        )
        try:
            result = llm.structured(
                system=CLASSIFY_SYSTEM,
                prompt=prompt,
                schema=CLASSIFY_SCHEMA,
                tool_name="phan_loai",
                tool_description="Trả về phân loại của bài tập.",
                model=model,
                max_tokens=2000,
            )
            data = dict(result.data)
            data.setdefault("grades", [])
            data.setdefault("curriculum", baseline.curriculum)
            data.setdefault("tags", [])
            data.setdefault("rationale", "")
            baseline = Classification(**data, source="llm")
        except llm.LLMUnavailable:
            pass  # giữ nguyên kết quả truy xuất, hệ thống vẫn chạy được

    if hint_subject:
        baseline.subject = hint_subject
    if hint_level:
        baseline.level = hint_level
    if hint_curriculum:
        baseline.curriculum = [hint_curriculum]
    return baseline


def describe(classification: Classification) -> str:
    """Một dòng mô tả cho người đọc."""
    parts = [SUBJECT_VI.get(classification.subject, classification.subject)]
    if classification.topic:
        parts.append(classification.topic)
    parts.append(f"độ khó {classification.difficulty}/5")
    if classification.curriculum:
        parts.append("/".join(classification.curriculum))
    return " · ".join(parts)
