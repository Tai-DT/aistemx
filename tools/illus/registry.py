"""Gom generator và luật khớp từ mọi họ hình thành một sổ đăng ký duy nhất.

Mỗi họ hình sống trong một cặp file riêng — `gen_<họ>.py` khai `REGISTRY`,
`rules_<họ>.py` khai `RULES` — thay vì cùng sửa một file chung. Lí do rất thực
tế: các họ được dựng song song, và một file chung thì mỗi lần thêm hình là một
lần tranh chấp. Tách file ra thì thêm một họ mới chỉ là thêm hai file, không
phải sửa gì ở giữa.

Nạp **chịu lỗi**: một họ hỏng (đang viết dở, thiếu thư viện) thì bị bỏ qua và
ghi vào `LOAD_ERRORS`, chứ không kéo sập cả tầng minh hoạ. Không có nó thì một
file dở dang làm hỏng luôn cả `coverage.py` lẫn builder, và người đang sửa file
ấy mất luôn công cụ để biết mình sửa tới đâu.
"""

from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path
from typing import Any, Callable

_PACKAGE = "tools.illus"
_HERE = Path(__file__).resolve().parent

#: (tên module, lỗi) của những họ nạp không được — in ra để người dựng biết.
LOAD_ERRORS: list[tuple[str, str]] = []


def _discover(prefix: str) -> list[Any]:
    """Nạp mọi module `tools/illus/<prefix>*.py` theo thứ tự tên."""
    found = []
    for info in sorted(pkgutil.iter_modules([str(_HERE)]), key=lambda m: m.name):
        if not info.name.startswith(prefix):
            continue
        try:
            found.append(importlib.import_module(f"{_PACKAGE}.{info.name}"))
        except Exception as error:  # noqa: BLE001 — một họ hỏng không được kéo sập cả tầng
            LOAD_ERRORS.append((info.name, f"{type(error).__name__}: {error}"))
    return found


def all_generators() -> dict[str, Callable[[dict], str]]:
    """Mọi generator SVG, gộp từ `generators2d` và các họ `gen_*`.

    Trùng tên thì họ nạp sau đè lên — và đó là lỗi cần biết, nên ghi vào
    `LOAD_ERRORS` thay vì im lặng: hai hình khác nhau mang cùng một tên nghĩa là
    có bản ghi trong `index.json` đang trỏ tới một hình không phải hình nó muốn.
    """
    from tools.illus import generators2d

    registry: dict[str, Callable[[dict], str]] = dict(generators2d.REGISTRY)
    for module in _discover("gen_"):
        for name, build in getattr(module, "REGISTRY", {}).items():
            if name in registry:
                LOAD_ERRORS.append((module.__name__, f"generator trùng tên: {name!r}"))
            registry[name] = build
    return registry


def all_rules() -> list[Callable[[dict], Any]]:
    """Mọi luật khớp, gộp từ `matcher` và các họ `rules_*`.

    Luật của `matcher.py` đứng TRƯỚC: đó là những luật đã qua kiểm định lâu nhất,
    và vài luật trong đó cố tình rất hẹp để né nhau (rule Pytago né định lí
    cosin). Cho họ mới chen lên trước thì cái né ấy mất tác dụng.
    """
    from tools.illus import matcher

    rules = list(matcher.RULES)
    for module in _discover("rules_"):
        rules.extend(getattr(module, "RULES", []))
    return rules


def render(generator: str, params: dict | None = None) -> str:
    """Vẽ một hình bất kỳ, bất kể nó nằm ở họ nào."""
    registry = all_generators()
    if generator not in registry:
        raise KeyError(f"generator không tồn tại: {generator}")
    return registry[generator](params or {})


def match_formula(formula: dict) -> Any:
    """Luật đầu tiên trúng thì thắng — giống hệt `matcher.match_formula`."""
    for rule in all_rules():
        hit = rule(formula)
        if hit:
            return hit
    return None
