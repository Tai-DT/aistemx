"""Sổ đăng ký gộp, và những bất biến mọi họ hình đều phải giữ.

Test ở đây không biết trước có những họ nào — nó **dò** mọi generator đang đăng
ký rồi kiểm từng cái. Nhờ vậy thêm một họ mới là tự động được canh, không phải
nhớ sửa file test.
"""

from __future__ import annotations

import pytest
from conftest import coords_within_viewbox, svg_is_wellformed

from tools.illus import registry


def test_khong_ho_nao_nap_hong() -> None:
    """Một họ hỏng bị bỏ qua chứ không kéo sập cả tầng — nhưng phải báo ra."""
    registry.all_generators()
    registry.all_rules()
    assert registry.LOAD_ERRORS == [], f"có họ nạp không được: {registry.LOAD_ERRORS}"


def _generator_names() -> list[str]:
    return sorted(registry.all_generators())


@pytest.mark.parametrize("name", _generator_names())
def test_generator_chay_duoc_voi_tham_so_mac_dinh(name: str) -> None:
    """Gọi `build_x({})` phải ra hình — mặc định thiếu là hỏng lúc dựng kho."""
    svg = registry.render(name, {})
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
    assert svg_is_wellformed(svg), f"{name}: SVG không hợp lệ hoặc có tham chiếu ngoài"


@pytest.mark.parametrize("name", _generator_names())
def test_hinh_khong_tran_ra_ngoai_khung(name: str) -> None:
    assert coords_within_viewbox(registry.render(name, {})), f"{name}: có nét nằm ngoài viewBox"


@pytest.mark.parametrize("name", _generator_names())
def test_hinh_tat_dinh(name: str) -> None:
    """Vẽ hai lần phải ra byte y hệt: kho minh hoạ được commit vào repo."""
    assert registry.render(name, {}) == registry.render(name, {})


@pytest.mark.parametrize("name", _generator_names())
def test_co_nhan_cho_trinh_doc_man_hinh(name: str) -> None:
    svg = registry.render(name, {})
    assert 'role="img"' in svg and "aria-label=" in svg
    assert "<title>" in svg


@pytest.mark.parametrize("name", _generator_names())
def test_khong_hard_code_mau(name: str) -> None:
    """Màu phải đi qua lớp CSS để hình tự lật theo nền sáng/tối.

    Bảng màu trong `svgkit.PALETTE_STYLE` là chỗ duy nhất được viết mã màu.
    """
    svg = registry.render(name, {})
    body = svg.split("</style>", 1)[-1]
    assert "#" not in body, f"{name}: có mã màu viết thẳng ngoài bảng màu"


def test_luat_khop_tra_ve_generator_co_that(formulas: list[dict]) -> None:
    """Luật trỏ tới một generator không tồn tại thì builder sẽ bỏ qua âm thầm."""
    known = set(registry.all_generators())
    for formula in formulas:
        hit = registry.match_formula(formula)
        if hit is None:
            continue
        assert hit[0] in known, f"{formula['id']}: luật trỏ tới generator lạ {hit[0]!r}"


def test_moi_cong_thuc_khop_toi_da_mot_lan(formulas: list[dict]) -> None:
    """Hai họ cùng nhận một công thức là dấu hiệu luật của ai đó quá rộng.

    Không phải lỗi chết người — luật đầu tiên thắng — nhưng nó nghĩa là có một
    họ đang với tay sang phần kho không phải của mình, và lần sau đổi thứ tự
    nạp là hình đổi theo mà không ai đụng vào luật nào.
    """
    from collections import defaultdict

    hits: dict[str, list[str]] = defaultdict(list)
    for formula in formulas:
        for rule in registry.all_rules():
            got = rule(formula)
            if got:
                hits[formula["id"]].append(got[0])
    overlaps = {fid: gens for fid, gens in hits.items() if len(set(gens)) > 1}
    assert not overlaps, f"{len(overlaps)} công thức bị nhiều họ nhận: {list(overlaps)[:5]}"
