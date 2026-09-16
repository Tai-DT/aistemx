"""Test cho 3 họ minh hoạ mới: Oxyz, Mômen lực / Cân bằng vật rắn, và Hấp dẫn / Kepler."""

from __future__ import annotations

import pytest
from tools.illus import registry


def test_khop_oxyz_toa_do_va_mat_phang() -> None:
    hit = registry.match_formula({"id": "math.thpt.oxyz-toa-do.toa-do-diem"})
    assert hit is not None
    assert hit[0] == "oxyz_coords"

    hit = registry.match_formula({"id": "math.thpt.oxyz-toa-do.tich-co-huong"})
    assert hit is not None
    assert hit[0] == "oxyz_vectors"

    hit = registry.match_formula({"id": "math.thpt.oxyz-mat-phang.pt-tong-quat"})
    assert hit is not None
    assert hit[0] == "oxyz_plane"

    hit = registry.match_formula({"id": "math.thpt.oxyz-mat-phang.khoang-cach-diem-mat-phang"})
    assert hit is not None
    assert hit[0] == "oxyz_plane"
    assert hit[1].get("mode") == "distance"

    hit = registry.match_formula({"id": "math.thpt.oxyz-duong-thang.goc-duong-mat"})
    assert hit is not None
    assert hit[0] == "oxyz_line"
    assert hit[1].get("mode") == "line_plane_angle"


def test_khop_momen_luc_va_can_bang() -> None:
    hit = registry.match_formula({"id": "physics.thpt.can-bang-vat-ran.momen-luc"})
    assert hit is not None
    assert hit[0] == "torque_moment"

    hit = registry.match_formula({"id": "physics.thpt.can-bang-vat-ran.don-bay"})
    assert hit is not None
    assert hit[0] == "lever_balance"

    hit = registry.match_formula({"id": "physics.thpt.can-bang-vat-ran.can-bang-ba-luc-khong-song-song"})
    assert hit is not None
    assert hit[0] == "equilibrium_3forces"


def test_khop_kepler_va_van_vat_hap_dan() -> None:
    hit = registry.match_formula({"id": "physics.thpt.intl-hap-dan.kepler-dinh-luat-i"})
    assert hit is not None
    assert hit[0] == "kepler_orbit"
    assert hit[1].get("mode") == "kepler1"

    hit = registry.match_formula({"id": "physics.thpt.intl-hap-dan.kepler-dinh-luat-ii"})
    assert hit is not None
    assert hit[0] == "kepler_orbit"
    assert hit[1].get("mode") == "kepler2"

    hit = registry.match_formula({"id": "physics.thpt.dong-luc-hoc.dinh-luat-van-vat-hap-dan"})
    assert hit is not None
    assert hit[0] == "gravitational_field"
    assert hit[1].get("mode") == "newton_law"

    hit = registry.match_formula({"id": "physics.thpt.intl-hap-dan.toc-do-quy-dao-ib"})
    assert hit is not None
    assert hit[0] == "gravitational_field"
    assert hit[1].get("mode") == "satellite"
