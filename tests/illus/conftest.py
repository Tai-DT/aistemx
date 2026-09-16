"""Đồ dùng chung cho test tầng minh hoạ.

Test ở đây chạy bằng venv của engine nhưng lại nhập gói `tools` ở gốc kho:

    cd /Volumes/SecondaryDisk/aistemx
    ./engine/.venv/bin/python -m pytest tests/illus -q

pytest chỉ thêm thư mục chứa file test vào `sys.path`, nên không có đoạn dưới
thì `import tools.illus` hỏng ngay ở dòng đầu mỗi file.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


@pytest.fixture(scope="session")
def formulas() -> list[dict]:
    """Toàn bộ công thức trong kho — để kiểm luật khớp trên dữ liệu thật.

    Luật khớp chỉ có nghĩa khi soi trên kho thật: một luật viết trông rất chặt
    vẫn có thể nuốt nhầm một họ công thức mà người viết không ngờ tới, và chỉ
    chạy trên toàn kho mới lộ ra.
    """
    index = ROOT / "data" / "formulas" / "index.json"
    return json.loads(index.read_text(encoding="utf-8"))["formulas"]


@pytest.fixture(scope="session")
def formula_by_id(formulas: list[dict]) -> dict[str, dict]:
    return {f["id"]: f for f in formulas}


def svg_is_wellformed(svg: str) -> bool:
    """SVG có phải một tài liệu XML hợp lệ, không tham chiếu tài nguyên ngoài?"""
    import xml.etree.ElementTree as ET

    if "http://" in svg.replace('xmlns="http://www.w3.org/2000/svg"', ""):
        return False
    if "https://" in svg:
        return False
    try:
        ET.fromstring(svg)
    except ET.ParseError:
        return False
    return True


def coords_within_viewbox(svg: str, slack: float = 2.0) -> bool:
    """Mọi toạ độ trong hình có nằm gọn trong khung không?

    Hình tràn ra ngoài `viewBox` là lỗi im lặng đúng nghĩa: file vẫn hợp lệ,
    trình duyệt vẫn vẽ, chỉ có phần bị cắt là người xem không bao giờ thấy.
    """
    import re
    import xml.etree.ElementTree as ET

    root = ET.fromstring(svg)
    box = (root.get("viewBox") or "").split()
    if len(box) != 4:
        return False
    _, _, width, height = (float(v) for v in box)

    numbers: list[tuple[float, float]] = []
    for element in root.iter():
        tag = element.tag.rsplit("}", 1)[-1]
        if tag in {"line", "rect", "circle", "text", "polyline", "polygon"}:
            if tag in {"polyline", "polygon"}:
                points = re.findall(r"(-?\d+\.?\d*),(-?\d+\.?\d*)", element.get("points", ""))
                numbers.extend((float(x), float(y)) for x, y in points)
            elif tag == "line":
                numbers.append((float(element.get("x1", 0)), float(element.get("y1", 0))))
                numbers.append((float(element.get("x2", 0)), float(element.get("y2", 0))))
            elif tag == "circle":
                cx, cy = float(element.get("cx", 0)), float(element.get("cy", 0))
                r = float(element.get("r", 0))
                numbers.extend([(cx - r, cy - r), (cx + r, cy + r)])
            else:
                numbers.append((float(element.get("x", 0)), float(element.get("y", 0))))
    return all(
        -slack <= x <= width + slack and -slack <= y <= height + slack for x, y in numbers
    )
