import { useMemo, type FC } from 'react';
import katex from 'katex';

interface MathViewProps {
  content?: string;
  latex?: string;
  block?: boolean;
  className?: string;
}

const KATEX_OPTIONS = {
  throwOnError: false,
  strict: false,
  trust: true,
  output: 'htmlAndMathml' as const,
  macros: {
    '\\degree': '^\\circ',
    '\\textdegree': '^\\circ',
    '\\celsius': '^\\circ\\text{C}',
    '\\angstrom': '\\text{\\AA}',
    '\\ohm': '\\Omega',
    '\\micro': '\\mu',
    '\\implies': '\\Longrightarrow',
    '\\iff': '\\Longleftrightarrow',
    '\\to': '\\rightarrow',
  },
};

/**
 * Chuẩn hóa các ký hiệu toán học unicode thành lệnh LaTeX tương thích cao
 */
function sanitizeLatex(input: string): string {
  if (!input) return '';
  return input
    .trim()
    .replace(/^(\$\$|\$|\\\[|\\\()/, '')
    .replace(/(\$\$|\$|\\\]|\\\))$/, '')
    .replace(/→/g, '\\rightarrow ')
    .replace(/⇒/g, '\\Rightarrow ')
    .replace(/×/g, '\\times ')
    .replace(/•/g, '\\cdot ')
    .replace(/±/g, '\\pm ')
    .replace(/≤/g, '\\le ')
    .replace(/≥/g, '\\ge ')
    .replace(/≠/g, '\\ne ')
    .replace(/≈/g, '\\approx ')
    .replace(/∞/g, '\\infty ')
    .replace(/°C/g, '^\\circ\\text{C}')
    .replace(/°/g, '^\\circ');
}

function renderKaTeX(raw: string, isBlock: boolean): string {
  const clean = sanitizeLatex(raw);
  if (!clean) return '';
  try {
    return katex.renderToString(clean, {
      ...KATEX_OPTIONS,
      displayMode: isBlock,
    });
  } catch {
    return `<span class="katex-fallback">${clean}</span>`;
  }
}

function formatInlineText(text: string): string {
  return text
    .replace(/\*\*(.*?)\*\*/g, '<strong style="font-weight: 700; color: #0f172a;">$1</strong>')
    .replace(/\*(.*?)\*/g, '<em style="font-style: italic;">$1</em>')
    .replace(/`([^`]+)`/g, '<code style="background: #f1f5f9; padding: 2px 5px; border-radius: 4px; font-size: 0.88em; color: #0369a1;">$1</code>');
}

export const MathView: FC<MathViewProps> = ({ content, latex, block = false, className = '' }) => {
  const renderedHtml = useMemo(() => {
    // Trường hợp 1: Truyền trực tiếp prop latex
    if (latex) {
      return renderKaTeX(latex, block);
    }

    if (!content) return '';

    // Step 1: Thay thế math blocks & inline math bằng token an toàn
    // Hỗ trợ: $$, \[, \(, $, và các môi trường \begin{cases/aligned/matrix}
    const mathTokens: string[] = [];
    const MATH_REGEX = /(\$\$[\s\S]*?\$\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$[^$\n]+?\$|\\begin\{(?:cases|aligned|matrix|pmatrix|bmatrix)\}[\s\S]*?\\end\{(?:cases|aligned|matrix|pmatrix|bmatrix)\})/g;

    const textWithTokens = content.replace(MATH_REGEX, (match) => {
      const isBlock =
        match.startsWith('$$') ||
        match.startsWith('\\[') ||
        match.startsWith('\\begin{');
      const rendered = renderKaTeX(match, isBlock);
      const token = `@@@MATH_TOKEN_${mathTokens.length}@@@`;
      mathTokens.push(rendered);
      return token;
    });

    // Step 2: Xử lý định dạng markdown cấu trúc bài học & bảng Punnett / dữ liệu
    const lines = textWithTokens.split(/\r?\n/);
    const htmlLines: string[] = [];
    let inList = false;
    let inTable = false;
    let tableRows: string[][] = [];

    const flushTable = () => {
      if (tableRows.length > 0) {
        let tableHtml = '<div style="overflow-x: auto; margin: 14px 0;"><table style="width: 100%; border-collapse: collapse; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.92rem;">';
        // Hàng đầu tiên làm thead nếu có separator |---|
        const hasHeader = tableRows.length > 1;
        if (hasHeader) {
          tableHtml += '<thead style="background: #f8fafc; border-bottom: 2px solid #cbd5e1;"><tr>';
          tableRows[0].forEach((col) => {
            tableHtml += `<th style="padding: 8px 14px; text-align: left; font-weight: 700; color: #0f172a; border: 1px solid #e2e8f0;">${formatInlineText(col)}</th>`;
          });
          tableHtml += '</tr></thead><tbody>';
          for (let r = 1; r < tableRows.length; r++) {
            tableHtml += '<tr>';
            tableRows[r].forEach((col) => {
              tableHtml += `<td style="padding: 8px 14px; border: 1px solid #e2e8f0; color: #1e293b;">${formatInlineText(col)}</td>`;
            });
            tableHtml += '</tr>';
          }
          tableHtml += '</tbody>';
        } else {
          tableHtml += '<tbody>';
          tableRows.forEach((row) => {
            tableHtml += '<tr>';
            row.forEach((col) => {
              tableHtml += `<td style="padding: 8px 14px; border: 1px solid #e2e8f0;">${formatInlineText(col)}</td>`;
            });
            tableHtml += '</tr>';
          });
          tableHtml += '</tbody>';
        }
        tableHtml += '</table></div>';
        htmlLines.push(tableHtml);
        tableRows = [];
        inTable = false;
      }
    };

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];

      // Bảng Markdown: dòng bắt đầu và kết thúc bằng |
      if (line.trim().startsWith('|') && line.trim().endsWith('|')) {
        // Bỏ qua dòng separator ví dụ |---|---|---|
        if (line.trim().match(/^\|(?:\s*:?-+:?\s*\|)+$/)) {
          continue;
        }
        const cols = line
          .trim()
          .slice(1, -1)
          .split('|')
          .map((c) => c.trim());
        inTable = true;
        tableRows.push(cols);
        continue;
      } else if (inTable) {
        flushTable();
      }

      // Danh sách gạch đầu dòng
      const listMatch = line.match(/^(\s*)[-*+]\s+(.*)$/);
      if (listMatch) {
        if (!inList) {
          htmlLines.push('<ul class="math-list" style="margin: 8px 0; padding-left: 22px; list-style-type: disc;">');
          inList = true;
        }
        const itemContent = formatInlineText(listMatch[2]);
        htmlLines.push(`<li style="margin-bottom: 4px; line-height: 1.6;">${itemContent}</li>`);
        continue;
      } else if (inList) {
        htmlLines.push('</ul>');
        inList = false;
      }

      // Tiêu đề cấp 3 (###)
      const h3Match = line.match(/^###\s+(.*)$/);
      if (h3Match) {
        htmlLines.push(`<h4 style="font-size: 1.05rem; font-weight: 700; color: #0369a1; margin: 18px 0 8px 0;">${formatInlineText(h3Match[1])}</h4>`);
        continue;
      }

      // Tiêu đề cấp 2 (##)
      const h2Match = line.match(/^##\s+(.*)$/);
      if (h2Match) {
        htmlLines.push(`<h3 style="font-size: 1.18rem; font-weight: 800; color: #0f172a; margin: 24px 0 10px 0; padding-bottom: 5px; border-bottom: 1px solid #e2e8f0;">${formatInlineText(h2Match[1])}</h3>`);
        continue;
      }

      // Tiêu đề cấp 1 (#)
      const h1Match = line.match(/^#\s+(.*)$/);
      if (h1Match) {
        htmlLines.push(`<h2 style="font-size: 1.28rem; font-weight: 800; color: #0f172a; margin: 26px 0 12px 0;">${formatInlineText(h1Match[1])}</h2>`);
        continue;
      }

      // Trích dẫn ghi chú (> )
      const quoteMatch = line.match(/^>\s+(.*)$/);
      if (quoteMatch) {
        htmlLines.push(`<blockquote style="border-left: 3px solid #f59e0b; background: #fffbeb; padding: 8px 14px; margin: 10px 0; border-radius: 0 6px 6px 0; color: #78350f;">${formatInlineText(quoteMatch[1])}</blockquote>`);
        continue;
      }

      // Dòng trống hoặc đoạn văn thường
      if (line.trim() === '') {
        htmlLines.push('<div style="height: 10px;"></div>');
      } else {
        htmlLines.push(`<div style="line-height: 1.7; margin-bottom: 8px;">${formatInlineText(line)}</div>`);
      }
    }

    if (inTable) flushTable();
    if (inList) htmlLines.push('</ul>');

    let resultHtml = htmlLines.join('');

    // Step 3: Phục hồi lại các khối công thức KaTeX
    mathTokens.forEach((rendered, idx) => {
      const token = `@@@MATH_TOKEN_${idx}@@@`;
      resultHtml = resultHtml.replace(token, rendered);
    });

    return resultHtml;
  }, [content, latex, block]);

  return (
    <div
      className={`math-view ${className}`}
      dangerouslySetInnerHTML={{ __html: renderedHtml }}
      style={{ display: block ? 'block' : 'inline' }}
    />
  );
};
