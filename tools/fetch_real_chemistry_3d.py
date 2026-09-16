#!/usr/bin/env python3
"""Script tải dữ liệu phân tử 3D thực nghiệm từ NCI/CADD Chemical Identifier Resolver (NIH).

Tải cấu trúc tọa độ 3D thực nghiệm (MMFF94 / Quantum Mechanics 3D coordinates).
"""

import os
import sys
import json
import time
import urllib.request
import urllib.parse
from pathlib import Path

DATA_DIR = Path("/Volumes/SecondaryDisk/aistemx/data/real_assets/chemistry_3d")
DATA_DIR.mkdir(parents=True, exist_ok=True)

COMPOUNDS = [
    {"slug": "water", "name": "water", "name_vi": "Nước", "formula": "H2O"},
    {"slug": "methane", "name": "methane", "name_vi": "Metan", "formula": "CH4"},
    {"slug": "ethene", "name": "ethene", "name_vi": "Etilen", "formula": "C2H4"},
    {"slug": "ethyne", "name": "ethyne", "name_vi": "Axetilen", "formula": "C2H2"},
    {"slug": "benzene", "name": "benzene", "name_vi": "Benzen", "formula": "C6H6"},
    {"slug": "ethanol", "name": "ethanol", "name_vi": "Rượu Etylic", "formula": "C2H5OH"},
    {"slug": "acetic_acid", "name": "acetic acid", "name_vi": "Axit Axetic", "formula": "CH3COOH"},
    {"slug": "glucose", "name": "glucose", "name_vi": "Glucozơ", "formula": "C6H12O6"},
    {"slug": "alanine", "name": "alanine", "name_vi": "Alanin", "formula": "C3H7NO2"},
    {"slug": "caffeine", "name": "caffeine", "name_vi": "Cafein", "formula": "C8H10N4O2"},
    {"slug": "aspirin", "name": "aspirin", "name_vi": "Aspirin", "formula": "C9H8O4"},
    {"slug": "sulfuric_acid", "name": "sulfuric acid", "name_vi": "Axit Sunfuric", "formula": "H2SO4"},
]


def download_compound_3d(item: dict):
    slug = item["slug"]
    name = item["name"]
    sdf_path = DATA_DIR / f"{slug}.sdf"

    encoded = urllib.parse.quote(name)
    url = f"https://cactus.nci.nih.gov/chemical/structure/{encoded}/sdf?get3d=true"

    print(f"⬇ Đang tải tọa độ 3D thực nghiệm cho {item['name_vi']} ({name})...")
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "AISTEM-Scientific-Pipeline/1.0 (Educational Academic Project)"},
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            content = resp.read().decode("utf-8")
            if "V2000" in content or "M  END" in content:
                sdf_path.write_text(content, encoding="utf-8")
                print(f"  ✓ Đã lưu thành công: {slug}.sdf")
            else:
                print(f"  ⚠ Phản hồi không phải định dạng SDF hợp lệ: {content[:100]}")
    except Exception as e:
        print(f"  ❌ Lỗi tải {name}: {e}")
    time.sleep(0.4)


def main():
    print("=== TẢI TỌA ĐỘ 3D CHUẨN KHOA HỌC CHO PHÂN TỬ HOÁ HỌC (NIH / NCI) ===")
    for c in COMPOUNDS:
        download_compound_3d(c)
    print("\n✓ Hoàn tất thu thập dữ liệu tọa độ 3D hóa học thực nghiệm.")


if __name__ == "__main__":
    main()
