#!/usr/bin/env python3
"""
AISTEM X — Bộ công cụ biên dịch tài liệu dự thi sang HTML & PDF chuẩn in ấn A4.
Hỗ trợ KaTeX, Mermaid.js, trang bìa trang trọng và định dạng báo cáo khoa học kỹ thuật.
"""

import os
import re
import subprocess
from pathlib import Path
from markdown_it import MarkdownIt

ROOT_DIR = Path("/Volumes/SecondaryDisk/aistemx")
SUBMISSION_DIR = ROOT_DIR / "docs" / "submission"
CHROME_BIN = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

md_parser = MarkdownIt("commonmark", {"html": True, "typographer": True}).enable("table")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>{{title}}</title>
  <!-- Google Fonts: Inter & Merriweather & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Merriweather:ital,wght@0,300;0,400;0,700;1,300&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  
  <!-- KaTeX -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <!-- Mermaid.js -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({
      startOnLoad: false,
      theme: 'neutral',
      flowchart: { curve: 'basis' },
      themeVariables: {
        fontFamily: 'Inter, sans-serif',
        primaryColor: '#eff6ff',
        primaryBorderColor: '#3b82f6',
        lineColor: '#1d4ed8',
        secondaryColor: '#f8fafc',
        tertiaryColor: '#ffffff'
      }
    });
  </script>

  <style>
    @page {
      size: A4;
      margin: 20mm 18mm 20mm 18mm;
      @bottom-right {
        content: counter(page);
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        color: #64748b;
      }
      @bottom-left {
        content: "AISTEM X (aistemx.com) — Hồ Sơ KHKT";
        font-family: 'Inter', sans-serif;
        font-size: 9pt;
        color: #94a3b8;
      }
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 11pt;
      line-height: 1.65;
      color: #0f172a;
      background-color: #ffffff;
      margin: 0;
      padding: 0;
    }

    .cover-page {
      page-break-after: always;
      min-height: 90vh;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 3px double #1d4ed8;
      padding: 35px 30px;
      margin-bottom: 20px;
      text-align: center;
      background: linear-gradient(180deg, #f8fafc 0%, #ffffff 70%, #eff6ff 100%);
      border-radius: 8px;
    }

    .cover-header {
      font-size: 11pt;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #334155;
      line-height: 1.8;
      border-bottom: 1.5px solid #cbd5e1;
      padding-bottom: 18px;
    }

    .cover-body {
      margin: auto 0;
      padding: 20px 0;
    }

    .cover-badge {
      display: inline-block;
      background: #dbeafe;
      color: #1e40af;
      padding: 6px 18px;
      border-radius: 9999px;
      font-size: 10pt;
      font-weight: 700;
      letter-spacing: 1px;
      margin-bottom: 20px;
      border: 1px solid #bfdbfe;
    }

    .cover-title {
      font-size: 26pt;
      font-weight: 800;
      color: #1e3a8a;
      line-height: 1.3;
      margin: 0 0 15px 0;
    }

    .cover-subtitle {
      font-size: 14pt;
      font-weight: 500;
      color: #475569;
      line-height: 1.5;
      max-width: 85%;
      margin: 0 auto;
    }

    .cover-meta {
      border-top: 1.5px solid #cbd5e1;
      padding-top: 20px;
      font-size: 11pt;
      color: #334155;
      text-align: left;
      display: grid;
      grid-template-columns: 180px 1fr;
      row-gap: 8px;
      width: 85%;
      margin: 0 auto;
    }

    .cover-meta-label {
      font-weight: 700;
      color: #1e293b;
    }

    h1, h2, h3, h4, h5, h6 {
      color: #0f172a;
      font-weight: 700;
      line-height: 1.3;
      margin-top: 24pt;
      margin-bottom: 8pt;
      page-break-after: avoid;
    }

    h1 {
      font-size: 20pt;
      color: #1e3a8a;
      border-bottom: 2px solid #3b82f6;
      padding-bottom: 6px;
    }

    h2 {
      font-size: 15pt;
      color: #1d4ed8;
      border-bottom: 1px solid #e2e8f0;
      padding-bottom: 4px;
    }

    h3 {
      font-size: 12.5pt;
      color: #0369a1;
    }

    p {
      margin-top: 0;
      margin-bottom: 10pt;
      text-align: justify;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 16pt 0;
      font-size: 9.5pt;
      page-break-inside: avoid;
    }

    table th, table td {
      border: 1px solid #cbd5e1;
      padding: 8pt 10pt;
      text-align: left;
    }

    table th {
      background-color: #f1f5f9;
      font-weight: 700;
      color: #1e293b;
    }

    table tr:nth-child(even) {
      background-color: #f8fafc;
    }

    blockquote {
      margin: 12pt 0;
      padding: 10pt 16pt;
      background: #eff6ff;
      border-left: 4px solid #3b82f6;
      color: #1e3a8a;
      font-style: normal;
      border-radius: 0 8px 8px 0;
      page-break-inside: avoid;
    }

    code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 9pt;
      background-color: #f1f5f9;
      padding: 2px 5px;
      border-radius: 4px;
      color: #0f766e;
    }

    pre {
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 12pt;
      overflow-x: auto;
      font-size: 8.5pt;
      page-break-inside: avoid;
    }

    pre code {
      background: none;
      padding: 0;
      color: #1e293b;
    }

    .mermaid {
      margin: 18pt auto;
      text-align: center;
      background: #ffffff;
      padding: 15pt;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      page-break-inside: avoid;
    }

    hr {
      border: 0;
      height: 1px;
      background: #e2e8f0;
      margin: 20pt 0;
    }

    .page-break {
      page-break-before: always;
    }
  </style>
</head>
<body>
  {{cover_html}}
  <main>
    {{content_html}}
  </main>

  <script>
    document.addEventListener("DOMContentLoaded", function() {
      renderMathInElement(document.body, {
        delimiters: [
          {left: '$$', right: '$$', display: true},
          {left: '$', right: '$', display: false}
        ],
        throwOnError: false
      });
      mermaid.run({
        querySelector: '.mermaid'
      });
    });
  </script>
</body>
</html>
"""

def generate_cover_page(title: str, subtitle: str, doc_type: str) -> str:
    return f"""
    <div class="cover-page">
      <div class="cover-header">
        BỘ GIÁO DỤC VÀ ĐÀO TẠO — HỘI ĐỒNG KHOA HỌC & CÔNG NGHỆ<br>
        CUỘC THI KHOA HỌC KỸ THUẬT & KHỞI NGHIỆP ĐỔI MỚI SÁNG TẠO
      </div>
      <div class="cover-body">
        <div class="cover-badge">{doc_type}</div>
        <h1 class="cover-title">{title}</h1>
        <p class="cover-subtitle">{subtitle}</p>
      </div>
      <div class="cover-meta">
        <span class="cover-meta-label">Lĩnh vực dự thi:</span>
        <span>Hệ thống phần mềm & Trí tuệ Nhân tạo (Systems Software & AI)</span>
        <span class="cover-meta-label">Dự án / Tên miền:</span>
        <span><strong>AISTEM X</strong> — <a href="https://aistemx.com" style="color:#1d4ed8; text-decoration:none;">https://aistemx.com</a></span>
        <span class="cover-meta-label">Độ sẵn sàng:</span>
        <span>Sản phẩm thương mại hoàn thiện 100% (Production Ready)</span>
        <span class="cover-meta-label">Quy mô tri thức:</span>
        <span>10,682 bản ghi — 5,272 công thức — 4,351 bài toán CAS</span>
        <span class="cover-meta-label">Năm thực hiện:</span>
        <span>2026</span>
      </div>
    </div>
    """

def convert_md_to_html(md_path: Path, output_html: Path, title: str, subtitle: str, doc_type: str):
    print(f"🔄 Đang xử lý: {md_path.name}...")
    with open(md_path, "r", encoding="utf-8") as f:
        raw_md = f.read()

    # Chuyển đổi khối mermaid code block ```mermaid sang <pre class="mermaid">
    def repl_mermaid(match):
        return f'<pre class="mermaid">\n{match.group(1)}\n</pre>'
    
    processed_md = re.sub(r"```mermaid\n([\s\S]*?)```", repl_mermaid, raw_md)

    content_html = md_parser.render(processed_md)
    cover_html = generate_cover_page(title, subtitle, doc_type)

    full_html = (
        HTML_TEMPLATE
        .replace("{{title}}", title)
        .replace("{{cover_html}}", cover_html)
        .replace("{{content_html}}", content_html)
    )

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"✅ Đã tạo HTML: {output_html.name}")

def export_html_to_pdf(html_path: Path, pdf_path: Path):
    print(f"🖨️ Đang in PDF chất lượng cao: {pdf_path.name}...")
    cmd = [
        CHROME_BIN,
        "--headless=new",
        "--disable-gpu",
        "--virtual-time-budget=4000",
        "--no-pdf-header-footer",
        f"--print-to-pdf={str(pdf_path)}",
        str(html_path),
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and pdf_path.exists():
        size_kb = pdf_path.stat().st_size / 1024
        print(f"🎉 Xuất PDF thành công: {pdf_path.name} ({size_kb:.1f} KB)")
    else:
        print(f"❌ Lỗi xuất PDF: {res.stderr}")

def main():
    SUBMISSION_DIR.mkdir(parents=True, exist_ok=True)
    
    docs = [
        {
            "md": SUBMISSION_DIR / "PROJECT_DOSSIER_THUYET_MINH.md",
            "html": SUBMISSION_DIR / "AISTEMX_BAN_THUYET_MINH_DU_THI.html",
            "pdf": SUBMISSION_DIR / "AISTEMX_BAN_THUYET_MINH_DU_THI.pdf",
            "title": "AISTEM X — BÁO CÁO THUYẾT MINH ĐỀ TÀI DỰ THI",
            "subtitle": "Nền tảng Siêu Tri Thức Khoa Học Liên Môn & Gia Sư AI STEM Chuẩn Quốc Tế",
            "type": "BÁO CÁO KHOA HỌC KỸ THUẬT CHÍNH THỨC"
        },
        {
            "md": SUBMISSION_DIR / "SYSTEM_FLOWS_AND_ARCHITECTURE.md",
            "html": SUBMISSION_DIR / "AISTEMX_SO_DO_LUONG_HE_THONG.html",
            "pdf": SUBMISSION_DIR / "AISTEMX_SO_DO_LUONG_HE_THONG.pdf",
            "title": "AISTEM X — HỆ THỐNG SƠ ĐỒ LUỒNG & KIẾN TRÚC KỸ THUẬT",
            "subtitle": "Bộ 6 Sơ Đồ Kiến Trúc Mạng Biên, Dữ Liệu Đồ Thị & Trình Khử Ảo Giác CAS",
            "type": "HỒ SƠ THIẾT KẾ KỸ THUẬT & FLOWCHARTS"
        },
        {
            "md": SUBMISSION_DIR / "PITCH_DECK_AND_DEMO_SCRIPT.md",
            "html": SUBMISSION_DIR / "AISTEMX_KICH_BAN_THUYET_TRINH_VA_PHAN_BIEN.html",
            "pdf": SUBMISSION_DIR / "AISTEMX_KICH_BAN_THUYET_TRINH_VA_PHAN_BIEN.pdf",
            "title": "AISTEM X — KỊCH BẢN THUYẾT TRÌNH & PHẢN BIỆN GIÁM KHẢO",
            "subtitle": "Hướng Dẫn Pitching 3-5 Phút, Thị Phạm Live Demo & Bộ Phản Biện Chuyên Sâu",
            "type": "CẨM NANG BẢO VỆ ĐỀ TÀI & PHẢN BIỆN"
        }
    ]

    for item in docs:
        if item["md"].exists():
            convert_md_to_html(item["md"], item["html"], item["title"], item["subtitle"], item["type"])
            export_html_to_pdf(item["html"], item["pdf"])

    # Tạo Master Full Dossier (gộp cả 3 tài liệu thành 1 tập sách A4 hoàn chỉnh)
    master_html = SUBMISSION_DIR / "AISTEMX_HO_SO_DU_THI_TOAN_DIEN_A4.html"
    master_pdf = SUBMISSION_DIR / "AISTEMX_HO_SO_DU_THI_TOAN_DIEN_A4.pdf"
    
    print("📚 Đang tạo Hồ sơ tổng hợp toàn diện (Master Dossier)...")
    with open(docs[0]["md"], "r", encoding="utf-8") as f1, \
         open(docs[1]["md"], "r", encoding="utf-8") as f2, \
         open(docs[2]["md"], "r", encoding="utf-8") as f3:
        combined_md = f"""
# PHẦN I: BÁO CÁO THUYẾT MINH ĐỀ TÀI KHOA HỌC KỸ THUẬT
{f1.read()}

<div class="page-break"></div>

# PHẦN II: HỆ THỐNG SƠ ĐỒ LUỒNG VÀ KIẾN TRÚC KỸ THUẬT
{f2.read()}

<div class="page-break"></div>

# PHẦN III: KỊCH BẢN THUYẾT TRÌNH, DEMO VÀ PHẢN BIỆN BAN GIÁM KHẢO
{f3.read()}
"""
    def repl_mermaid(match):
        return f'<pre class="mermaid">\n{match.group(1)}\n</pre>'
    processed_master_md = re.sub(r"```mermaid\n([\s\S]*?)```", repl_mermaid, combined_md)
    master_content = md_parser.render(processed_master_md)
    master_cover = generate_cover_page(
        "AISTEM X — TẬP HỒ SƠ DỰ THI TOÀN DIỆN",
        "Nền Tảng Siêu Tri Thức Khoa Học Liên Môn & Trợ Lý Gia Sư AI STEM Chuẩn Quốc Tế",
        "TẬP HỒ SƠ TOÀN DIỆN (FULL DOSSIER)"
    )
    master_full_html = (
        HTML_TEMPLATE
        .replace("{{title}}", "AISTEM X — TẬP HỒ SƠ DỰ THI TOÀN DIỆN")
        .replace("{{cover_html}}", master_cover)
        .replace("{{content_html}}", master_content)
    )
    with open(master_html, "w", encoding="utf-8") as f:
        f.write(master_full_html)
    export_html_to_pdf(master_html, master_pdf)
    print("✨ Hoàn tất toàn bộ quy trình biên dịch hồ sơ dự thi!")

if __name__ == "__main__":
    main()
