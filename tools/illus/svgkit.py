"""Tiện ích dựng SVG cho minh hoạ 2D.

Mọi màu đi qua biến CSS (``var(--ill-*, fallback)``) để ứng dụng đổi theme sáng/tối
mà không phải sinh lại ảnh. SVG không tham chiếu tài nguyên ngoài, nhúng thẳng được.
"""

from __future__ import annotations

import html
import math
from typing import Iterable, Sequence

# Bảng màu mực/nền/nhấn. Fallback hợp nền sáng; khối @media tự lật màu mực/trục/lưới
# khi nền tối để SVG đọc được cả hai theme mà KHÔNG cần app set biến. App vẫn có thể
# ghi đè bằng cách set --ill-* với độ ưu tiên cao hơn.
PALETTE_STYLE = """
@media (prefers-color-scheme: dark){
  :root{--ill-ink:#e5e9f0;--ill-axis:#9aa5b4;--ill-grid:#3a4656;--ill-muted:#9aa5b4}
}
.ill-bg{fill:var(--ill-bg,transparent)}
.ink{stroke:var(--ill-ink,#1f2933);fill:none;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.ink-thin{stroke:var(--ill-ink,#1f2933);fill:none;stroke-width:1;opacity:.55}
.axis{stroke:var(--ill-axis,#6b7280);fill:none;stroke-width:1.5}
.grid{stroke:var(--ill-grid,#d1d5db);fill:none;stroke-width:1;opacity:.5}
.accent-a{stroke:var(--ill-a,#2563eb);fill:var(--ill-a,#2563eb)}
.accent-b{stroke:var(--ill-b,#dc2626);fill:var(--ill-b,#dc2626)}
.accent-c{stroke:var(--ill-c,#16a34a);fill:var(--ill-c,#16a34a)}
.accent-d{stroke:var(--ill-d,#d97706);fill:var(--ill-d,#d97706)}
.fill-a{fill:var(--ill-a,#2563eb);stroke:none;opacity:.2}
.fill-b{fill:var(--ill-b,#dc2626);stroke:none;opacity:.2}
.fill-c{fill:var(--ill-c,#16a34a);stroke:none;opacity:.2}
.curve{stroke:var(--ill-a,#2563eb);fill:none;stroke-width:2.5}
.lbl{fill:var(--ill-ink,#1f2933);font-family:'Cambria Math','STIX Two Math',Georgia,serif;font-size:15px;font-style:italic}
.lbl-sm{fill:var(--ill-muted,#6b7280);font-family:system-ui,Segoe UI,Roboto,sans-serif;font-size:12px;font-style:normal}
""".strip()


def _n(v: float) -> str:
    """Số gọn: bỏ đuôi 0 để SVG deterministic và nhẹ."""
    if v == int(v):
        return str(int(v))
    return f"{v:.3f}".rstrip("0").rstrip(".")


def esc(text: str) -> str:
    return html.escape(str(text), quote=True)


class Canvas:
    """Bộ tích luỹ phần tử SVG với vài helper hình học thường dùng."""

    def __init__(self, width: float, height: float, title: str = "", desc: str = ""):
        self.w = width
        self.h = height
        self.title = title
        self.desc = desc
        self._parts: list[str] = []
        self._defs: list[str] = []

    # -- primitives --------------------------------------------------------
    def raw(self, markup: str) -> None:
        self._parts.append(markup)

    def line(self, x1, y1, x2, y2, cls="ink", extra=""):
        self._parts.append(
            f'<line x1="{_n(x1)}" y1="{_n(y1)}" x2="{_n(x2)}" y2="{_n(y2)}" class="{cls}"{extra}/>'
        )

    def polyline(self, pts: Iterable[Sequence[float]], cls="curve", extra=""):
        d = " ".join(f"{_n(x)},{_n(y)}" for x, y in pts)
        self._parts.append(f'<polyline points="{d}" class="{cls}" fill="none"{extra}/>')

    def polygon(self, pts: Iterable[Sequence[float]], cls="fill-a", extra=""):
        d = " ".join(f"{_n(x)},{_n(y)}" for x, y in pts)
        self._parts.append(f'<polygon points="{d}" class="{cls}"{extra}/>')

    def circle(self, cx, cy, r, cls="ink", extra=""):
        self._parts.append(
            f'<circle cx="{_n(cx)}" cy="{_n(cy)}" r="{_n(r)}" class="{cls}"{extra}/>'
        )

    def dot(self, cx, cy, r=3.2, cls="accent-a"):
        self._parts.append(f'<circle cx="{_n(cx)}" cy="{_n(cy)}" r="{_n(r)}" class="{cls}"/>')

    def rect(self, x, y, w, h, cls="ink", extra=""):
        self._parts.append(
            f'<rect x="{_n(x)}" y="{_n(y)}" width="{_n(w)}" height="{_n(h)}" class="{cls}"{extra}/>'
        )

    def path(self, d: str, cls="ink", extra=""):
        self._parts.append(f'<path d="{d}" class="{cls}"{extra}/>')

    def text(self, x, y, s, cls="lbl", anchor="start", extra=""):
        self._parts.append(
            f'<text x="{_n(x)}" y="{_n(y)}" text-anchor="{anchor}" class="{cls}"{extra}>{esc(s)}</text>'
        )

    # -- composite helpers -------------------------------------------------
    def arrow(self, x1, y1, x2, y2, cls="accent-a", head=9.0, extra=""):
        """Mũi tên đặc (vectơ). ``cls`` áp cho cả thân lẫn đầu mũi."""
        self.line(x1, y1, x2, y2, cls=cls, extra=' stroke-width="2.5"' + extra)
        ang = math.atan2(y2 - y1, x2 - x1)
        a1 = ang + math.radians(150)
        a2 = ang - math.radians(150)
        p = [
            (x2, y2),
            (x2 + head * math.cos(a1), y2 + head * math.sin(a1)),
            (x2 + head * math.cos(a2), y2 + head * math.sin(a2)),
        ]
        self.polygon(p, cls=cls, extra=' stroke="none" fill-opacity="1"')

    def right_angle(self, vx, vy, ux, uy, wx, wy, size=12.0):
        """Ký hiệu góc vuông tại đỉnh (vx,vy) giữa hai tia tới (ux,uy) và (wx,wy)."""
        def unit(ax, ay, bx, by):
            dx, dy = bx - ax, by - ay
            d = math.hypot(dx, dy) or 1.0
            return dx / d, dy / d
        u = unit(vx, vy, ux, uy)
        w = unit(vx, vy, wx, wy)
        p1 = (vx + u[0] * size, vy + u[1] * size)
        p3 = (vx + w[0] * size, vy + w[1] * size)
        p2 = (vx + (u[0] + w[0]) * size, vy + (u[1] + w[1]) * size)
        self.polyline([p1, p2, p3], cls="ink-thin")

    def render(self) -> str:
        defs = f"<defs>{''.join(self._defs)}</defs>" if self._defs else ""
        title = f"<title>{esc(self.title)}</title>" if self.title else ""
        desc = f"<desc>{esc(self.desc)}</desc>" if self.desc else ""
        body = "".join(self._parts)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {_n(self.w)} {_n(self.h)}" '
            f'role="img" aria-label="{esc(self.title)}">'
            f"{title}{desc}<style>{PALETTE_STYLE}</style>{defs}"
            f'<rect class="ill-bg" x="0" y="0" width="{_n(self.w)}" height="{_n(self.h)}"/>'
            f"{body}</svg>"
        )
