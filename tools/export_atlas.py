#!/usr/bin/env python3
"""Xuất **một file HTML tự chứa** gồm toàn bộ minh hoạ của kho.

    python3 tools/export_atlas.py                      # ra atlas-minh-hoa.html
    python3 tools/export_atlas.py --out /tmp/a.html --level thpt --subject math

Khác gallery ở `viewer/`: gallery tải `index.json` rồi tải tiếp từng file SVG,
nên **phải có server** (mở bằng `file://` là chặn bởi CORS) và mỗi lần mở là vài
trăm lượt tải. File này nhúng thẳng mọi SVG vào HTML: mở bằng cách nhấp đúp, gửi
qua chat cho người khác cũng xem được, và không phụ thuộc gì vào kho nữa.

Đánh đổi có ý thức: file nặng hơn (mỗi SVG vài KB). Vì vậy có sẵn bộ lọc theo
môn/cấp để xuất riêng từng phần thay vì luôn xuất cả kho.
"""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ILL_DIR = ROOT / "data" / "illustrations"
INDEX = ILL_DIR / "index.json"

_PAGE = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{title}</title>
<style>
  :root {{ --bg:#f5f7fa; --card:#fff; --ink:#1f2933; --muted:#6b7280; --border:#e5e7eb;
           --tag:#eef2ff; --tagink:#3730a3; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg:#0f141b; --card:#161d26; --ink:#e5e9f0; --muted:#94a3b8; --border:#2b3644;
             --tag:#1e293b; --tagink:#93c5fd; }}
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--ink);
          font-family:system-ui,"Segoe UI",Roboto,sans-serif; }}
  header {{ position:sticky; top:0; z-index:2; background:var(--bg);
            border-bottom:1px solid var(--border); padding:14px 20px;
            display:flex; align-items:center; gap:12px; flex-wrap:wrap; }}
  header h1 {{ font-size:16px; margin:0; }}
  .stat {{ font-size:13px; color:var(--muted); }}
  input, select {{ font:inherit; font-size:13px; padding:6px 10px; border-radius:8px;
                   border:1px solid var(--border); background:var(--card); color:var(--ink); }}
  input {{ min-width:210px; }}
  main {{ padding:20px; display:grid; grid-template-columns:repeat(auto-fill,minmax(300px,1fr)); gap:16px; }}
  .card {{ background:var(--card); border:1px solid var(--border); border-radius:14px;
           overflow:hidden; display:flex; flex-direction:column; }}
  .fig {{ padding:14px; display:flex; align-items:center; justify-content:center; min-height:190px; }}
  .fig svg {{ max-width:100%; height:auto; }}
  .meta {{ padding:10px 14px 14px; border-top:1px solid var(--border); }}
  .name {{ font-size:13.5px; font-weight:600; line-height:1.35; }}
  .cap {{ font-size:12px; color:var(--muted); line-height:1.45; margin-top:5px; }}
  .tex {{ font-size:11.5px; color:var(--muted); font-family:ui-monospace,monospace;
          margin-top:6px; word-break:break-all; }}
  .id {{ font-size:10.5px; color:var(--muted); font-family:ui-monospace,monospace;
         margin-top:6px; word-break:break-all; }}
  .tags {{ margin-top:8px; display:flex; gap:6px; flex-wrap:wrap; }}
  .tag {{ font-size:10.5px; padding:2px 8px; border-radius:999px;
          background:var(--tag); color:var(--tagink); }}
  .empty {{ color:var(--muted); padding:40px; text-align:center; grid-column:1/-1; }}
</style>
</head>
<body>
<header>
  <h1>{title}</h1>
  <span class="stat" id="stat"></span>
  <input id="q" placeholder="Lọc theo tên · id · chủ đề · công thức…"/>
  <select id="subject"><option value="">— mọi môn —</option>{subject_options}</select>
  <select id="level"><option value="">— mọi cấp —</option>{level_options}</select>
  <select id="gen"><option value="">— mọi generator —</option>{gen_options}</select>
</header>
<main id="grid"></main>
<script id="data" type="application/json">{payload}</script>
<script>
const ITEMS = JSON.parse(document.getElementById('data').textContent);
const grid = document.getElementById('grid');
const boxes = {{
  q: document.getElementById('q'),
  subject: document.getElementById('subject'),
  level: document.getElementById('level'),
  gen: document.getElementById('gen'),
}};
function render() {{
  const q = boxes.q.value.trim().toLowerCase();
  const shown = ITEMS.filter(it =>
    (!boxes.subject.value || it.subject === boxes.subject.value) &&
    (!boxes.level.value   || it.level   === boxes.level.value) &&
    (!boxes.gen.value     || it.generator === boxes.gen.value) &&
    (!q || (it.formula_id + ' ' + it.title + ' ' + it.topic + ' ' + it.caption + ' ' +
            it.latex + ' ' + it.generator).toLowerCase().includes(q)));
  document.getElementById('stat').textContent = shown.length + '/' + ITEMS.length + ' hình';
  if (!shown.length) {{ grid.innerHTML = '<div class="empty">Không có hình khớp bộ lọc.</div>'; return; }}
  grid.innerHTML = shown.map(it => `
    <div class="card">
      <div class="fig">${{it.svg}}</div>
      <div class="meta">
        <div class="name">${{it.title || it.formula_id.split('.').pop().replace(/-/g,' ')}}</div>
        ${{it.caption ? `<div class="cap">${{it.caption}}</div>` : ''}}
        ${{it.latex ? `<div class="tex">${{it.latex}}</div>` : ''}}
        <div class="id">${{it.formula_id}}</div>
        <div class="tags">${{[it.subject, it.level, it.topic, it.generator]
          .filter(Boolean).map(t => `<span class="tag">${{t}}</span>`).join('')}}</div>
      </div>
    </div>`).join('');
}}
Object.values(boxes).forEach(el => {{ el.oninput = render; el.onchange = render; }});
render();
</script>
</body>
</html>
"""


def _options(values: list[str]) -> str:
    return "".join(f'<option value="{html.escape(v)}">{html.escape(v)}</option>' for v in values)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "atlas-minh-hoa.html"))
    ap.add_argument("--subject", help="lọc theo môn trước khi xuất")
    ap.add_argument("--level", help="lọc theo cấp trước khi xuất")
    ap.add_argument("--title", default="AISTEM · Atlas minh hoạ")
    args = ap.parse_args()

    if not INDEX.exists():
        print("chưa có index.json — chạy python3 tools/build_illustrations.py trước")
        return 1
    index = json.loads(INDEX.read_text(encoding="utf-8"))

    items = []
    for record in index["illustrations"]:
        if args.subject and record.get("subject") != args.subject:
            continue
        if args.level and record.get("level") != args.level:
            continue
        svg_path = record.get("svg_path")
        if not svg_path:
            continue  # bản ghi chỉ-raster: không nhúng được vào file tự chứa
        svg_file = ILL_DIR / svg_path
        if not svg_file.exists():
            continue
        items.append({
            "formula_id": record["formula_id"],
            "title": record.get("title", ""),
            "topic": record.get("topic", ""),
            "subject": record.get("subject", ""),
            "level": record.get("level", ""),
            "generator": record.get("generator", ""),
            "caption": record.get("caption_vi", ""),
            "latex": record.get("latex", ""),
            "svg": svg_file.read_text(encoding="utf-8"),
        })

    if not items:
        print("không có hình nào khớp bộ lọc")
        return 1

    def uniq(key: str) -> list[str]:
        return sorted({i[key] for i in items if i[key]})

    page = _PAGE.format(
        title=html.escape(args.title),
        payload=json.dumps(items, ensure_ascii=False),
        subject_options=_options(uniq("subject")),
        level_options=_options(uniq("level")),
        gen_options=_options(uniq("generator")),
    )
    out = Path(args.out)
    out.write_text(page, encoding="utf-8")
    print(f"đã xuất {len(items)} hình -> {out}  ({out.stat().st_size / 1024:.0f} KB)")
    print("mở bằng cách nhấp đúp; không cần server, không cần kho.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
