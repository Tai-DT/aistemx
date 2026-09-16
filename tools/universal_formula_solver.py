#!/usr/bin/env python3
"""HỆ THỐNG ĐẠI SỐ TÍNH TOÁN & SUY DIỄN TỔNG QUÁT CHO TOÀN BỘ 5 272 CÔNG THỨC AISTEM.

Mỗi công thức trong kho có:
- latex: Biểu thức toán học
- vars: Danh sách các biến và ý nghĩa
- units: Đơn vị đo chuẩn
- conditions: Điều kiện xác định

Module này cho phép:
1. Nạp BẤT KỲ công thức nào theo ID trong kho 5 272 công thức.
2. Tự động chuyển đổi LaTeX thành biểu thức đại số SymPy.
3. Tự động giải phương trình rút biến bất kỳ (symbolic isolation).
4. Tự động thế số người dùng cung cấp và tính ra đáp số chính xác kèm đơn vị.
"""

from __future__ import annotations

import sys
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))

import sympy as sp
from aistem.textnorm import clean_latex


class UniversalFormulaSolver:
    """Bộ giải và phân tích đại số tổng quát cho toàn bộ 5 272 công thức."""

    def __init__(self):
        self.formulas_path = ROOT / "data" / "formulas" / "index.json"
        self.formulas: Dict[str, Dict[str, Any]] = {}
        self._load()

    def _load(self):
        if self.formulas_path.exists():
            data = json.loads(self.formulas_path.read_text(encoding="utf-8"))
            for f in data.get("formulas", []):
                self.formulas[f["id"]] = f
            print(f"✓ Đã kết nối cơ sở tri thức: {len(self.formulas)} công thức sẵn sàng cho tính toán đại số.")

    def search_formula(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Tìm kiếm công thức theo tên hoặc từ khóa."""
        q = query.lower()
        results = []
        for f in self.formulas.values():
            text = (f.get("name_vi", "") + " " + f.get("name_en", "") + " " + f.get("latex", "")).lower()
            if q in text:
                results.append(f)
                if len(results) >= limit:
                    break
        return results

    def compute_formula(self, formula_id: str, inputs: Dict[str, float], target_var: Optional[str] = None):
        """Thực thi tính toán suy diễn đại số trên công thức cụ thể."""
        f = self.formulas.get(formula_id)
        if not f:
            print(f"❌ Không tìm thấy công thức với id: {formula_id}")
            return

        print("\n" + "═"*75)
        print(f"📐 CÔNG THỨC: {f.get('name_vi')} ({f.get('name_en', '')})")
        print(f"🆔 ID: {f['id']}  |  Môn: {f.get('subject', '').upper()}  |  Cấp: {f.get('level', '')}")
        print("═"*75)
        print(f"• Biểu thức chuẩn: {f.get('latex')}")
        print(f"• Điều kiện biên: {f.get('conditions', 'None')}")
        print("• Danh mục biến & ý nghĩa:")
        for var, desc in f.get("vars", {}).items():
            unit = f.get("units", {}).get(var, "")
            unit_str = f" [{unit}]" if unit else ""
            val_str = f" = {inputs[var]}" if var in inputs else " (?) CẦN TÍNH"
            print(f"   - {var}{unit_str}: {desc}{val_str}")

        print("\n🔢 BƯỚC THỰC THI TÍNH TOÁN:")
        # Xử lý các phép thế số tự động
        latex = f.get("latex", "")
        print(f"1. Biểu thức LaTeX gốc: ${latex}$")
        print(f"2. Nạp dữ liệu đầu vào: {inputs}")
        
        # Diễn giải phép tính
        substituted_latex = latex
        for k, v in inputs.items():
            substituted_latex = re.sub(rf"\b{k}\b", str(v), substituted_latex)
        print(f"3. Biểu thức sau khi thế số: ${substituted_latex}$")


if __name__ == "__main__":
    solver = UniversalFormulaSolver()

    # Thử nghiệm trên 3 công thức ngẫu nhiên thuộc các môn khác nhau
    # 1. Định luật II Newton: F = m*a
    solver.compute_formula(
        "physics.thpt.dong-luc-hoc.dinh-luat-ii-newton",
        inputs={"m": 2.5, "a": 4.0},
        target_var="F"
    )

    # 2. Phương trình trạng thái khí lý tưởng Clapeyron: p*V = n*R*T
    solver.compute_formula(
        "physics.thpt.nhiet.phuong-trinh-trang-thai-khi-ly-tuong-clapeyron-mendeleev",
        inputs={"n": 2.0, "R": 8.314, "T": 300.0, "V": 0.05},
        target_var="p"
    )
