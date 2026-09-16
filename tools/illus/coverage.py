"""Đo độ phủ minh hoạ: luật nào bắt được bao nhiêu công thức, và bỏ sót ở đâu.

    python3 tools/illus/coverage.py                 # toàn kho
    python3 tools/illus/coverage.py --level thpt    # lọc theo cấp
    python3 tools/illus/coverage.py --miss "Lượng giác"   # liệt kê công thức CHƯA có hình

Một hình sai còn tệ hơn không có hình: người học tin vào cái mình nhìn thấy, và
một hình vẽ sai thì không có cách nào để họ phát hiện ra. Vì vậy phép đo ở đây
luôn in ra **cả hai** con số — bắt được bao nhiêu, và bỏ sót bao nhiêu — chứ
không chỉ khoe phần bắt được. Luật nào bắt bừa để nâng số phủ là đi ngược lại
mục đích của cả tầng này.
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from tools.illus.registry import LOAD_ERRORS, match_formula  # noqa: E402

FORMULA_INDEX = ROOT / "data" / "formulas" / "index.json"
BINDINGS = ROOT / "data" / "illustrations" / "bindings.json"


def load_formulas() -> list[dict]:
    data = json.loads(FORMULA_INDEX.read_text(encoding="utf-8"))
    return data["formulas"]


def load_bound_ids() -> set[str]:
    if not BINDINGS.exists():
        return set()
    data = json.loads(BINDINGS.read_text(encoding="utf-8"))
    items = data if isinstance(data, list) else data.get("bindings", [])
    return {b["formula_id"] for b in items}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", help="lọc theo cấp: tieu-hoc, thcs, thpt, dai-hoc")
    ap.add_argument("--subject", help="lọc theo môn")
    ap.add_argument("--miss", help="in công thức CHƯA có hình của một chủ đề")
    ap.add_argument("--limit", type=int, default=30)
    args = ap.parse_args()

    formulas = load_formulas()
    if args.level:
        formulas = [f for f in formulas if f.get("level") == args.level]
    if args.subject:
        formulas = [f for f in formulas if f.get("subject") == args.subject]

    bound = load_bound_ids()
    by_generator: collections.Counter = collections.Counter()
    covered: list[dict] = []
    missing: list[dict] = []

    for formula in formulas:
        hit = match_formula(formula)
        if hit is not None:
            by_generator[hit[0]] += 1
            covered.append(formula)
        elif formula["id"] in bound:
            by_generator["<bindings.json>"] += 1
            covered.append(formula)
        else:
            missing.append(formula)

    # In SAU vòng khớp: việc dò các họ chỉ xảy ra ở lần gọi `match_formula`
    # đầu tiên, nên trước đó danh sách lỗi luôn rỗng.
    for name, error in LOAD_ERRORS:
        print(f"  [cảnh báo] không nạp được họ {name}: {error}", file=sys.stderr)

    total = len(formulas) or 1
    print(f"phủ {len(covered)}/{len(formulas)} công thức ({len(covered) / total:.1%})")
    print(f"chưa có hình: {len(missing)}")
    print("\ntheo generator:")
    for name, count in by_generator.most_common():
        print(f"  {count:5d}  {name}")

    if args.miss:
        wanted = [f for f in missing if args.miss.lower() in (f.get("topic") or "").lower()]
        print(f"\n{len(wanted)} công thức chưa có hình trong chủ đề {args.miss!r}:")
        for formula in wanted[: args.limit]:
            print(f"  {formula['id']}")
            print(f"      {formula.get('latex', '')[:88]}")
    else:
        print("\n12 chủ đề còn thiếu nhiều nhất:")
        gaps: collections.Counter = collections.Counter(
            (f.get("subject"), f.get("topic")) for f in missing
        )
        for (subject, topic), count in gaps.most_common(12):
            print(f"  {count:5d}  {subject:10s} {topic}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
