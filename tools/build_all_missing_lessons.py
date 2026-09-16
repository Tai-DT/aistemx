#!/usr/bin/env python3
"""Lắp ráp toàn bộ 28 bài học mới, liên kết 975+ công thức vào các bài học và tái đồng bộ hệ thống."""
from __future__ import annotations

import json
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

def main():
    # 1. Load all new lessons from parts 1-4
    all_new = []
    for part in ["lessons_part1.json", "lessons_part2.json", "lessons_part3.json", "lessons_part4.json"]:
        p = ROOT / "tools" / part
        if p.exists():
            all_new.extend(json.loads(p.read_text(encoding="utf-8")))

    print(f"Loaded {len(all_new)} new lessons.")

    # Group new lessons by target file
    new_by_file = defaultdict(list)
    for item in all_new:
        new_by_file[item["file"]].append(item["lesson"])

    # 2. Insert new lessons into lesson files
    modified_files = set()
    for fname, new_lessons in new_by_file.items():
        fpath = DATA / "lessons" / fname
        doc = json.loads(fpath.read_text(encoding="utf-8"))
        existing_ids = {l["id"] for l in doc.get("lessons", [])}
        for nl in new_lessons:
            if nl["id"] not in existing_ids:
                doc["lessons"].append(nl)
                existing_ids.add(nl["id"])
        doc["meta"]["count"] = len(doc["lessons"])
        fpath.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        modified_files.add(fname)
        print(f"  + Added {len(new_lessons)} lessons to {fname} (total now: {len(doc['lessons'])})")

    # 3. Explicit specific mappings
    specific_maps = {
        "chemistry.thpt.oxit-axit.oxit-tac-dung-hcl": ("vn-chemistry-daicuong-voco.json", "lesson.chemistry.vn-thpt-chemistry-daicuong-voco.kim-loai-axit-loang-khu-oxit-nhiet-nhom"),
        "chemistry.thpt.oxit-axit.oxit-tac-dung-h2so4": ("vn-chemistry-daicuong-voco.json", "lesson.chemistry.vn-thpt-chemistry-daicuong-voco.kim-loai-axit-loang-khu-oxit-nhiet-nhom"),
        "chemistry.thpt.sat.fe-tac-dung-hno3": ("vn-chemistry-daicuong-voco.json", "lesson.chemistry.vn-thpt-chemistry-daicuong-voco.kim-loai-hno3-h2so4-dac"),
        "chemistry.thpt.kim-loai-muoi.tang-giam-khoi-luong": ("vn-chemistry-daicuong-voco.json", "lesson.chemistry.vn-thpt-chemistry-daicuong-voco.kim-loai-axit-loang-khu-oxit-nhiet-nhom"),
        "chemistry.thpt.kim-loai-nuoc.kiem-kiem-tho-tac-dung-nuoc": ("vn-chemistry-daicuong-voco.json", "lesson.chemistry.vn-thpt-chemistry-daicuong-voco.kim-loai-axit-loang-khu-oxit-nhiet-nhom"),
        "physics.thcs.nang-luong.dinh-luat-bao-toan-nang-luong": ("vn-thcs-vatli.json", "lesson.physics.thcs-vatli.may-co-don-gian-dinh-luat-ve-cong"),
    }

    for fid, (fname, lid) in specific_maps.items():
        fpath = DATA / "lessons" / fname
        doc = json.loads(fpath.read_text(encoding="utf-8"))
        for l in doc["lessons"]:
            if l["id"] == lid and fid not in l["formulas"]:
                l["formulas"].append(fid)
        fpath.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        modified_files.add(fname)

    # 4. Load all formulas and all lessons currently in memory
    formulas = []
    for p in sorted((DATA / "formulas").rglob("*.json")):
        if p.name in {"schema.json", "index.json", "usage.json"}:
            continue
        doc = json.loads(p.read_text(encoding="utf-8"))
        formulas.extend(doc.get("formulas", []))

    formula_by_id = {f["id"]: f for f in formulas}

    lesson_docs = {}
    for p in sorted((DATA / "lessons").rglob("*.json")):
        if p.name in {"schema.json", "index.json"}:
            continue
        lesson_docs[p.name] = json.loads(p.read_text(encoding="utf-8"))

    # Map current formula usage
    used_fids = set()
    topic_to_lessons = defaultdict(list)
    for fname, doc in lesson_docs.items():
        for l in doc.get("lessons", []):
            for fid in l.get("formulas", []):
                used_fids.add(fid)
                if fid in formula_by_id:
                    f = formula_by_id[fid]
                    key = (f["subject"], f["level"], f["topic"])
                    if (fname, l["id"]) not in topic_to_lessons[key]:
                        topic_to_lessons[key].append((fname, l["id"]))

    unlinked_formulas = [f for f in formulas if f["id"] not in used_fids]
    print(f"Unlinked formulas before topic mapping: {len(unlinked_formulas)}")

    # 5. Link unlinked formulas by matching (subject, level, topic)
    linked_count = 0
    still_unlinked = []
    for f in unlinked_formulas:
        key = (f["subject"], f["level"], f["topic"])
        cands = topic_to_lessons.get(key, [])
        if cands:
            # Score candidate lessons by subtopic or title match
            subt = f.get("subtopic", "").lower()
            fname_term = f.get("name_vi", "").lower()
            best_cand = cands[0]
            best_score = -1
            for cand_fname, cand_lid in cands:
                cand_lesson = next(l for l in lesson_docs[cand_fname]["lessons"] if l["id"] == cand_lid)
                score = 0
                if subt and subt in cand_lesson["title_vi"].lower():
                    score += 5
                if subt and any(subt in t.lower() for t in cand_lesson.get("tags", [])):
                    score += 3
                if any(w in cand_lesson["title_vi"].lower() for w in fname_term.split() if len(w) > 3):
                    score += 1
                # Prefer lesson with fewer formulas to distribute evenly
                score -= len(cand_lesson.get("formulas", [])) * 0.1
                if score > best_score:
                    best_score = score
                    best_cand = (cand_fname, cand_lid)

            target_fname, target_lid = best_cand
            cand_lesson = next(l for l in lesson_docs[target_fname]["lessons"] if l["id"] == target_lid)
            if f["id"] not in cand_lesson["formulas"]:
                cand_lesson["formulas"].append(f["id"])
                modified_files.add(target_fname)
                linked_count += 1
        else:
            still_unlinked.append(f)

    print(f"Successfully mapped and linked: {linked_count} formulas.")
    print(f"Remaining unlinked formulas: {len(still_unlinked)}")
    if still_unlinked:
        for f in still_unlinked:
            print(f"  - {f['id']}: {f['subject']} | {f['level']} | {f['topic']} | {f['name_vi']}")

    # 6. Save all modified lesson files
    for fname in modified_files:
        doc = lesson_docs[fname]
        doc["meta"]["count"] = len(doc["lessons"])
        fpath = DATA / "lessons" / fname
        fpath.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("Saved all updated files.")

if __name__ == "__main__":
    main()
