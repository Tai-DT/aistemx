#!/usr/bin/env python3
"""Crawl catalog digitallearning.vn qua RSC payload trong HTML.

Public:    python3 fetch_library.py
Sau login: python3 fetch_library.py --cookies cookies.txt   (Netscape cookie file,
           lấy từ trình duyệt đã đăng nhập; route /app/library trả thêm resources
           isPublic=false)
"""
import csv
import json
import os
import re
import subprocess
import sys
import time

BASE = "https://digitallearning.vn"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36"
OUT = os.path.dirname(os.path.abspath(__file__))


def fetch(url, cookies=None):
    cmd = ["curl", "-sL", "--max-time", "40", "-A", UA]
    if cookies:
        cmd += ["-b", cookies]
    cmd.append(url)
    return subprocess.run(cmd, capture_output=True).stdout.decode("utf-8", "replace")


def rsc_text(html):
    """Nối toàn bộ self.__next_f.push([1,\"...\"]) chunks thành text."""
    out = []
    for c in re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html):
        try:
            out.append(json.loads('"' + c + '"'))
        except Exception:
            out.append(c.encode().decode("unicode_escape", "replace"))
    return "".join(out)


def crawl(list_path, cookies=None):
    items = {}
    for page in range(1, 40):
        url = f"{BASE}{list_path}?pageSize=20&page={page}"
        m = re.search(r'"resources":(\[\{.*?\}\]),"total":(\d+)', rsc_text(fetch(url, cookies)), re.S)
        if not m:
            break
        arr = json.loads(m.group(1))
        for it in arr:
            items[it["slug"]] = it
        print(f"page {page}: {len(arr)} (total {m.group(2)})")
        if len(items) >= int(m.group(2)):
            break
        time.sleep(0.35)
    return list(items.values())


def write_csv(items, path):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["slug", "id", "title", "title_en", "subject", "resource_types",
                    "renderer", "source_type", "is_public", "education_levels",
                    "suggested_grades", "duration_min", "tags", "embed_url",
                    "module_key", "source_url", "public_route", "status",
                    "published_at", "updated_at", "thumbnail"])
        for it in items:
            rc = it.get("rendererConfig") or {}
            prov = it.get("provenance") or {}
            w.writerow([
                it["slug"], it["id"], it["title"], it.get("titleEn"), it.get("subject"),
                "|".join(it.get("resourceTypes") or []), it.get("rendererType"),
                it.get("sourceType"), it.get("isPublic"),
                "|".join(it.get("educationLevels") or []),
                "|".join(map(str, it.get("suggestedGrades") or [])),
                it.get("estimatedDurationMinutes"), "|".join(it.get("tags") or []),
                rc.get("tourUrl") or rc.get("embedUrl") or "",
                it.get("moduleKey") or "", prov.get("sourceUrl") or "",
                it.get("publicRoute"), it.get("status"), it.get("publishedAt"),
                it.get("updatedAt"), it.get("thumbnail"),
            ])


def main():
    cookies = None
    if "--cookies" in sys.argv:
        cookies = sys.argv[sys.argv.index("--cookies") + 1]
    if cookies:
        items = crawl("/app/library", cookies)
        json.dump(items, open(f"{OUT}/app_library_items.json", "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        write_csv(items, f"{OUT}/app_library_catalog.csv")
    else:
        items = crawl("/library")
        json.dump(items, open(f"{OUT}/library_items.json", "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        write_csv(items, f"{OUT}/library_catalog.csv")
    print("DONE:", len(items), "items")


if __name__ == "__main__":
    main()
