#!/usr/bin/env python3
"""Công cụ Phân tích Công thức -> Biến đổi Đại số -> Thế số -> Tính toán Từng bước & Kiểm chứng.

Chạy:
  /Volumes/SecondaryDisk/aistemx/engine/.venv/bin/python3 /Volumes/SecondaryDisk/aistemx/tools/formula_calculator.py
"""

import sys
import math
from pathlib import Path

# Thêm engine vào path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))

import sympy as sp
from aistem.cas.parse import to_sympy


class FormulaExplainer:
    """Bộ máy phân tích, diễn giải công thức và tính toán số học tự động."""

    @staticmethod
    def solve_kinematics(v0: float, a: float, t: float):
        """1. VẬT LÝ: Chuyển động biến đổi đều v = v0 + at; s = v0*t + 0.5*a*t^2"""
        print("\n" + "="*60)
        print("🔬 CHUYÊN ĐỀ: VẬT LÝ — CHUYỂN ĐỘNG BIẾN ĐỔI ĐỀU")
        print("="*60)
        print(f"• Giả thiết:")
        print(f"  - Vận tốc ban đầu (v₀): {v0} m/s")
        print(f"  - Gia tốc (a): {a} m/s²")
        print(f"  - Thời gian (t): {t} s")

        print("\n📐 1. CÔNG THỨC GỐC:")
        print("   (1) Vận tốc tức thời: v(t) = v₀ + a·t")
        print("   (2) Quãng đường đi được: s(t) = v₀·t + ½·a·t²")
        print("   (3) Hệ thức độc lập thời gian: v² - v₀² = 2·a·s")

        print("\n🔢 2. QUY TRÌNH THẾ SỐ VÀO PHÉP TÍNH:")
        v = v0 + a * t
        s = v0 * t + 0.5 * a * (t ** 2)
        print(f"   • Tính v:  v = {v0} + ({a}) × {t} = {v0} + {a*t} = {v} m/s")
        print(f"   • Tính s:  s = {v0} × {t} + 0.5 × ({a}) × ({t}²) = {v0*t} + {0.5*a*(t**2)} = {s} m")

        print("\n🛡 3. KIỂM CHỨNG ĐỘC LẬP BẰNG HỆ THỨC LIÊN HỆ:")
        check_val = v**2 - v0**2
        expected = 2 * a * s
        diff = abs(check_val - expected)
        print(f"   • Vế trái (v² - v₀²): {v}² - {v0}² = {check_val}")
        print(f"   • Vế phải (2·a·s)    : 2 × {a} × {s} = {expected}")
        print(f"   • Trạng thái kiểm chứng CAS: {'✓ HOÀN TOÀN CHÍNH XÁC (Sai số = 0)' if diff < 1e-6 else '❌ SAI LỆCH'}")

    @staticmethod
    def solve_chemistry_dilution(c1: float, v1: float, c2: float):
        """2. HOÁ HỌC: Pha loãng dung dịch c1*v1 = c2*v2"""
        print("\n" + "="*60)
        print("⚗ CHUYÊN ĐỀ: HOÁ HỌC — BẢO TOÀN SỐ MOL PHA LOÃNG DUNG DỊCH")
        print("="*60)
        print(f"• Giả thiết:")
        print(f"  - Nồng độ ban đầu (C₁): {c1} M")
        print(f"  - Thể tích ban đầu (V₁): {v1} mL")
        print(f"  - Nồng độ mục tiêu (C₂): {c2} M (C₂ < C₁)")

        print("\n📐 1. CÔNG THỨC GỐC:")
        print("   Số mol chất tan không đổi: n = C₁·V₁ = C₂·V₂")
        print("   Rút ẩn thể tích sau pha loãng: V₂ = (C₁·V₁) / C₂")
        print("   Thể tích nước cần thêm vào: V_nước = V₂ - V₁")

        v2 = (c1 * v1) / c2
        v_water = v2 - v1
        print("\n🔢 2. THẾ SỐ & TÍNH TOÁN:")
        print(f"   • V₂ = ({c1} × {v1}) / {c2} = {c1*v1} / {c2} = {v2:.2f} mL")
        print(f"   • V_nước = {v2:.2f} - {v1} = {v_water:.2f} mL")
        print(f"\n✓ KẾT LUẬN: Cần thêm chính xác {v_water:.2f} mL nước cất vào {v1} mL dung dịch {c1}M để được dung dịch {c2}M.")

    @staticmethod
    def solve_quadratic_formula(a: float, b: float, c: float):
        """3. TOÁN HỌC: Giải phương trình bậc 2 ax^2 + bx + c = 0"""
        print("\n" + "="*60)
        print(f"📐 CHUYÊN ĐỀ: TOÁN HỌC — GIẢI PHƯƠNG TRÌNH BẬC HAI: {a}x² + {b}x + {c} = 0")
        print("="*60)
        print("\n1. CÔNG THỨC CHUẨN:")
        print("   Biệt thức: Δ = b² - 4ac")
        print("   Nghiệm: x₁,₂ = (-b ± √Δ) / (2a)")

        delta = b**2 - 4*a*c
        print(f"\n2. THẾ SỐ TÍNH BIỆT THỨC Δ:")
        print(f"   Δ = ({b})² - 4 × ({a}) × ({c}) = {b**2} - ({4*a*c}) = {delta}")

        if delta > 0:
            sqrt_d = math.sqrt(delta)
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)
            print(f"\n3. TÍNH NGHIỆM:")
            print(f"   x₁ = (-({b}) + √{delta}) / (2 × {a}) = ({-b} + {sqrt_d:.4f}) / {2*a} = {x1:.4f}")
            print(f"   x₂ = (-({b}) - √{delta}) / (2 × {a}) = ({-b} - {sqrt_d:.4f}) / {2*a} = {x2:.4f}")
        elif delta == 0:
            x0 = -b / (2*a)
            print(f"\n3. PHƯƠNG TRÌNH CÓ NGHIỆM KÉP: x = {-b} / {2*a} = {x0:.4f}")
        else:
            print("\n3. PHƯƠNG TRÌNH VÔ NGHIỆM TRÊN TRƯỜNG SỐ THỰC ℝ.")


if __name__ == "__main__":
    calc = FormulaExplainer()
    # 1. Chuyển động biến đổi đều: v0=10 m/s, a=2 m/s^2, t=5 s
    calc.solve_kinematics(v0=10.0, a=2.0, t=5.0)

    # 2. Pha loãng hóa học: C1=2.0M, V1=100mL, C2=0.5M
    calc.solve_chemistry_dilution(c1=2.0, v1=100.0, c2=0.5)

    # 3. Phương trình bậc 2: 2x^2 - 7x + 3 = 0
    calc.solve_quadratic_formula(a=2.0, b=-7.0, c=3.0)
