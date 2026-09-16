#!/usr/bin/env python3
"""Rà soát toàn diện kho dữ liệu AISTEM — tìm chỗ thiếu, chỗ lệch, chỗ chưa nối.

Chạy:  python3 tools/audit.py

Không sinh dữ liệu, không sửa gì — chỉ đọc và báo cáo. Sáu nhóm phát hiện:
  1. Ma trận độ phủ (môn × cấp × chương trình) từng kho — ô nào mỏng/trống.
  2. Công thức chưa có bài học và chưa có bài tập nào dùng tới.
  3. Chủ đề (topic) có công thức nhưng không có bài học tương ứng.
  4. Bài học / bài tập không tham chiếu công thức nào (có thể thiếu liên kết).
  5. Lệch phân bố độ khó của bài tập theo môn.
  6. Công thức/kỳ thi tham chiếu treo, và các điểm cần rà theo cảnh báo.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

SUBJECTS = ["math", "physics", "chemistry", "biology"]
SUBJ_VI = {"math": "Toán", "physics": "Lí", "chemistry": "Hoá", "biology": "Sinh"}
LEVELS = ["tieu-hoc", "thcs", "thpt", "dai-hoc"]
LV_VI = {"tieu-hoc": "TH", "thcs": "THCS", "thpt": "THPT", "dai-hoc": "ĐH"}
CURR = ["vn-gdpt-2018", "ap", "ib", "a-level", "intl-undergrad", "olympiad", "ru-east-eu"]


def load(kind: str, key: str) -> list[dict]:
    out = []
    d = DATA / kind
    if not d.exists():
        return out
    for p in sorted(d.rglob("*.json")):
        if p.name in {"schema.json", "index.json", "usage.json"}:
            continue
        try:
            out.extend(json.loads(p.read_text(encoding="utf-8")).get(key, []))
        except (json.JSONDecodeError, KeyError):
            pass
    return out


def bar(n: int, mx: int, w: int = 20) -> str:
    if mx == 0:
        return ""
    return "█" * max(1, round(n / mx * w)) if n else ""


def h(title: str) -> None:
    print(f"\n{'=' * 66}\n{title}\n{'=' * 66}")


def main() -> None:
    formulas = load("formulas", "formulas")
    lessons = load("lessons", "lessons")
    problems = load("problems", "problems")
    exams = load("exams", "exams")
    fids = {f["id"] for f in formulas}

    print(f"Kho: {len(formulas)} công thức · {len(lessons)} bài học · "
          f"{len(problems)} bài tập · {len(exams)} hồ sơ đề thi")

    # ---------- 1. Ma trận độ phủ ----------
    h("1. ĐỘ PHỦ công thức theo môn × cấp (ô trống = chưa có gì)")
    grid = defaultdict(int)
    for f in formulas:
        grid[(f["subject"], f["level"])] += 1
    print(f"{'':6}" + "".join(f"{LV_VI[l]:>8}" for l in LEVELS) + "     Tổng")
    for s in SUBJECTS:
        row = [grid[(s, l)] for l in LEVELS]
        cells = "".join(f"{v:>8}" if v else f"{'·':>8}" for v in row)
        print(f"{SUBJ_VI[s]:6}{cells}{sum(row):>10}")

    h("1b. ĐỘ PHỦ theo chương trình × môn (số công thức)")
    cg = defaultdict(int)
    for f in formulas:
        for c in f.get("curriculum", []):
            cg[(c, f["subject"])] += 1
    print(f"{'':16}" + "".join(f"{SUBJ_VI[s]:>8}" for s in SUBJECTS) + "     Tổng")
    for c in CURR:
        row = [cg[(c, s)] for s in SUBJECTS]
        print(f"{c:16}" + "".join(f"{v:>8}" if v else f"{'·':>8}" for v in row) + f"{sum(row):>10}")

    # ---------- 2. Công thức chưa có nội dung ----------
    usage_path = DATA / "formulas" / "usage.json"
    usage = json.loads(usage_path.read_text(encoding="utf-8"))["usage"] if usage_path.exists() else {}
    no_lesson = [f for f in formulas if not usage.get(f["id"], {}).get("lessons")]
    no_problem = [f for f in formulas if not usage.get(f["id"], {}).get("problems")]
    orphan = [f for f in formulas if f["id"] not in usage]

    h("2. CÔNG THỨC chưa được nội dung nào dùng tới")
    print(f"Chưa có BÀI HỌC nào giảng : {len(no_lesson)}/{len(formulas)} ({len(no_lesson)*100//len(formulas)}%)")
    print(f"Chưa có BÀI TẬP nào dùng  : {len(no_problem)}/{len(formulas)} ({len(no_problem)*100//len(formulas)}%)")
    print(f"Chưa gắn với gì cả        : {len(orphan)}/{len(formulas)} ({len(orphan)*100//len(formulas)}%)")
    ob = defaultdict(int)
    for f in orphan:
        ob[(f["subject"], f["level"])] += 1
    print("\nCông thức chưa gắn nội dung, theo môn × cấp:")
    for s in SUBJECTS:
        cells = [(l, ob[(s, l)]) for l in LEVELS if ob[(s, l)]]
        if cells:
            print(f"  {SUBJ_VI[s]:5} " + " · ".join(f"{LV_VI[l]} {n}" for l, n in cells))

    # ---------- 3. Chủ đề có công thức nhưng không có bài học ----------
    h("3. CHỦ ĐỀ có công thức nhưng CHƯA có bài học (theo môn × cấp)")
    ftopics = defaultdict(set)
    for f in formulas:
        ftopics[(f["subject"], f["level"])].add(f["topic"])
    ltopics = defaultdict(set)
    for l in lessons:
        # bài học đối chiếu qua công thức nó dùng
        for fid in l.get("formulas", []):
            ff = next((x for x in formulas if x["id"] == fid), None)
            if ff:
                ltopics[(ff["subject"], ff["level"])].add(ff["topic"])
    shown = 0
    for s in SUBJECTS:
        for l in ["thpt", "dai-hoc"]:  # bài học chỉ phủ 2 cấp này
            miss = sorted(ftopics[(s, l)] - ltopics[(s, l)])
            if miss:
                print(f"\n  {SUBJ_VI[s]} · {LV_VI[l]} — {len(miss)} chủ đề chưa có bài học:")
                for t in miss[:12]:
                    print(f"    · {t}")
                if len(miss) > 12:
                    print(f"    … và {len(miss) - 12} chủ đề nữa")
                shown += 1
    if not shown:
        print("  (không có — mọi chủ đề THPT/ĐH đều đã có bài học chạm tới)")

    # ---------- 4. Nội dung không nối công thức ----------
    h("4. NỘI DUNG chưa nối công thức nào (có thể thiếu liên kết)")
    l_no = [l for l in lessons if not l.get("formulas")]
    p_no = [p for p in problems if not p.get("formulas_used")]
    print(f"Bài học không có formulas[]      : {len(l_no)}/{len(lessons)}")
    for l in l_no[:8]:
        print(f"    · {l['id']}")
    if len(l_no) > 8:
        print(f"    … và {len(l_no) - 8} bài nữa")
    print(f"Bài tập không có formulas_used[] : {len(p_no)}/{len(problems)}")
    pnb = defaultdict(int)
    for p in p_no:
        pnb[p["subject"]] += 1
    if pnb:
        print("    theo môn: " + ", ".join(f"{SUBJ_VI[s]} {pnb[s]}" for s in SUBJECTS if pnb[s]))

    # ---------- 5. Phân bố độ khó bài tập ----------
    h("5. PHÂN BỐ ĐỘ KHÓ bài tập theo môn (mục tiêu ~20% dễ / 50% vừa / 30% khó)")
    for s in SUBJECTS:
        ps = [p for p in problems if p["subject"] == s]
        if not ps:
            continue
        d = defaultdict(int)
        for p in ps:
            d[p.get("difficulty", 0)] += 1
        easy = d[1] + d[2]
        mid = d[3]
        hard = d[4] + d[5]
        tot = len(ps)
        print(f"  {SUBJ_VI[s]:5} n={tot:3}  dễ {easy*100//tot:2}%  vừa {mid*100//tot:2}%  "
              f"khó {hard*100//tot:2}%   [{d[1]}·{d[2]}·{d[3]}·{d[4]}·{d[5]}]")
    # dạng bài
    print("\n  Phân bố dạng bài tập:")
    dt = defaultdict(int)
    for p in problems:
        dt[p.get("type", "?")] += 1
    for t, n in sorted(dt.items(), key=lambda kv: -kv[1]):
        print(f"    {t:14} {n:4}  {bar(n, len(problems))}")

    # ---------- 6. Tham chiếu treo ----------
    h("6. THAM CHIẾU TREO và điểm cần rà")
    dangling = 0
    for l in lessons:
        for fid in l.get("formulas", []):
            if fid not in fids:
                print(f"  bài học {l['id']} -> công thức không tồn tại: {fid}")
                dangling += 1
    for p in problems:
        for fid in p.get("formulas_used", []):
            if fid not in fids:
                print(f"  bài tập {p['id']} -> công thức không tồn tại: {fid}")
                dangling += 1
    for e in exams:
        for fid in e.get("formulas_must_memorize", []):
            if fid not in fids:
                print(f"  đề thi {e['id']} -> công thức không tồn tại: {fid}")
                dangling += 1
    # related treo trong công thức
    rel_dangle = 0
    for f in formulas:
        for r in f.get("related", []):
            if r not in fids:
                rel_dangle += 1
    print(f"  Tham chiếu công thức treo (bài học/bài tập/đề thi): {dangling}")
    print(f"  related treo trong kho công thức: {rel_dangle}")
    tagged = [p for p in problems if "ngoai-pham-vi-ap-2026" in p.get("tags", [])]
    print(f"  Bài tập gắn cờ 'ngoai-pham-vi-ap-2026' (đã đổi nhãn, cần rà lại khi thi 2027): {len(tagged)}")

    h("TÓM TẮT — nơi nên đầu tư tiếp")
    gaps = []
    if no_lesson:
        gaps.append(f"{len(no_lesson)} công thức chưa có bài giảng")
    if no_problem:
        gaps.append(f"{len(no_problem)} công thức chưa có bài luyện")
    thcs_thpt_lessons = sum(1 for l in lessons if l["level"] in ("thcs", "tieu-hoc"))
    if thcs_thpt_lessons == 0:
        gaps.append("bài học & bài tập CHƯA phủ bậc TH/THCS (chỉ mới cấp 3 + ĐH)")
    for g in gaps:
        print(f"  ▸ {g}")


if __name__ == "__main__":
    main()
