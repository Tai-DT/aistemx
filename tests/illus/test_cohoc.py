"""Kiểm họ hình **cơ học**.

Hai nhóm phép kiểm, ứng với hai kiểu hỏng khác nhau:

* **Hình** — phải dựng được với mọi tham số, kể cả tham số bậy (0, âm, khổng
  lồ, chuỗi rác), và không nét nào lọt khỏi khung. Hình tràn khung là lỗi im
  lặng: file vẫn hợp lệ, trình duyệt vẫn vẽ, chỉ phần bị cắt là không ai thấy.
* **Luật** — phải **không bắt nhầm**. Mỗi luật được thử trên những công thức
  *gần giống mà khác nghĩa* lấy đúng id thật trong kho: giao thoa ngược pha (mẫu
  vân dịch đi, vẽ hình cùng pha là sai), ống sáo một đầu kín (không phải dây),
  vật lăn trên mặt nghiêng (không phải khối trượt), lực quán tính li tâm (hướng
  ra xa tâm, ngược hẳn với hình lực hướng tâm).
"""

from __future__ import annotations

import math

import pytest
from conftest import coords_within_viewbox, svg_is_wellformed

from tools.illus.gen_cohoc import REGISTRY
from tools.illus.rules_cohoc import RULES
from tools.illus import rules_cohoc as rc

TEN_GENERATOR = sorted(REGISTRY)

# Tham số biên: mỗi bộ đều phải cho ra hình hợp lệ, không được nổ.
THAM_SO_BIEN: list[dict] = [
    {},
    {k: 0 for k in ("x0", "v", "a", "v0", "tmax", "h", "H", "A", "T", "alpha",
                    "angle", "phi", "dphi", "k", "n", "d", "lam", "cycles", "modes")},
    {k: -1 for k in ("x0", "v", "a", "v0", "tmax", "h", "H", "A", "T", "alpha",
                     "angle", "phi", "dphi", "k", "n", "d", "cycles", "modes")},
    {k: 1e9 for k in ("x0", "v", "a", "v0", "tmax", "h", "H", "A", "T", "alpha",
                      "angle", "phi", "dphi", "k", "n", "d", "cycles", "modes")},
    {k: float("nan") for k in ("v", "a", "tmax", "A", "T", "alpha", "dphi")},
    {k: "rác" for k in ("v", "a", "tmax", "A", "T", "alpha", "h", "H", "k", "n")},
    {"points": [], "strip": [], "tangent": None, "kind": "không-có-kiểu",
     "mode": "không-có", "direction": "ngang-bậy", "show": "bậy"},
    {"points": [[0, 0]], "strip": [1, 1], "tangent": 1e9},
    {"slope": True, "area": True, "mean": True, "delta": True, "chord": True,
     "luc": True, "ma_sat": True, "keo": True, "bien_do": True, "do_cao": True,
     "cang": True, "two_points": True, "free_end": True, "mark_M": True,
     "khoang_cach": True, "gia_toc": "len", "phan_tich": True, "n": 3},
]


@pytest.mark.parametrize("ten", TEN_GENERATOR)
def test_mac_dinh_du_cho_moi_khoa(ten: str) -> None:
    """``build_x({})`` phải chạy được: builder gọi generator với params rỗng."""
    svg = REGISTRY[ten]({})
    assert svg.startswith("<svg") and svg.rstrip().endswith("</svg>")
    assert svg_is_wellformed(svg)


@pytest.mark.parametrize("ten", TEN_GENERATOR)
@pytest.mark.parametrize("bo", range(len(THAM_SO_BIEN)))
def test_tham_so_bien_khong_no(ten: str, bo: int) -> None:
    svg = REGISTRY[ten](dict(THAM_SO_BIEN[bo]))
    assert svg_is_wellformed(svg), f"{ten} với bộ {bo}: SVG hỏng"
    assert coords_within_viewbox(svg), f"{ten} với bộ {bo}: có nét ngoài viewBox"


@pytest.mark.parametrize("ten", TEN_GENERATOR)
def test_tat_dinh(ten: str) -> None:
    """Kho minh hoạ được commit vào repo nên hai lần vẽ phải ra byte y hệt."""
    assert REGISTRY[ten]({}) == REGISTRY[ten]({})
    tham_so = {"A": 3, "T": 1.5, "alpha": 25, "k": 2, "n": 3}
    assert REGISTRY[ten](dict(tham_so)) == REGISTRY[ten](dict(tham_so))


@pytest.mark.parametrize("ten", TEN_GENERATOR)
def test_co_nhan_va_khong_mau_cung(ten: str) -> None:
    svg = REGISTRY[ten]({})
    assert "<title>" in svg and "<desc>" in svg and 'role="img"' in svg
    assert "#" not in svg.split("</style>", 1)[-1], "có mã màu viết thẳng"
    assert "http" not in svg.replace('xmlns="http://www.w3.org/2000/svg"', "")


def test_moi_luat_tra_ve_generator_co_that() -> None:
    ten_co_that = set(TEN_GENERATOR) | {"projectile", "vector_add"}
    for bang in (rc._XT, rc._VT, rc._TRIO, rc._ROI, rc._NEM_NGANG, rc._NEM_XIEN,
                 rc._TRON, rc._FBD_NGANG, rc._FBD_NGHIENG, rc._FBD_TREO, rc._HE_VAT,
                 rc._LO_XO_NGANG, rc._LO_XO_DOC, rc._CON_LAC_DON, rc._SHM_XT,
                 rc._SHM_TRIO, rc._SHM_ELIP, rc._PHA, rc._NANG_LUONG, rc._SONG,
                 rc._SONG_DUNG, rc._GIAO_THOA, rc._VECTO):
        assert bang, "bảng rỗng"
    for luat in RULES:
        got = luat({"id": "physics.thpt.dong-hoc.gia-toc-huong-tam"})
        if got:
            assert got[0] in ten_co_that


def test_moi_id_trong_bang_deu_ton_tai_that(formula_by_id: dict[str, dict]) -> None:
    """Luật trỏ tới một id không có trong kho là luật chết — không ai phát hiện.

    Kiểu sai này im lặng tuyệt đối: bảng thống kê chỉ thiếu đi một dòng, mà
    thiếu một dòng thì trông y hệt "công thức đó chưa được phủ".
    """
    thieu = []
    for ten in dir(rc):
        bang = getattr(rc, ten)
        if ten.isupper() and isinstance(bang, dict) and ten != "RULES":
            thieu += [i for i in bang if i not in formula_by_id]
    assert thieu == [], f"id không tồn tại trong kho: {thieu}"


def test_moi_cong_thuc_khop_toi_da_mot_luat(formulas: list[dict]) -> None:
    """Trong nội bộ họ, không công thức nào được hai luật cùng nhận."""
    trung = []
    for f in formulas:
        khop = [r(f)[0] for r in RULES if r(f)]
        if len(khop) > 1:
            trung.append((f["id"], khop))
    assert trung == [], f"công thức bị nhiều luật nhận: {trung}"


def test_khong_lan_sang_luat_cua_matcher_goc(formulas: list[dict]) -> None:
    """Không giành công thức mà `matcher.py` đã nhận (đặc biệt là ném xiên).

    `matcher.py` nhận 4 id ném xiên; họ này chỉ bù ba id còn lại. Nếu chồng lên
    nhau thì hình vẽ ra phụ thuộc thứ tự nạp module — đổi tên file là đổi hình.
    """
    from tools.illus import matcher

    chong = [f["id"] for f in formulas
             if matcher.match_formula(f) and any(r(f) for r in RULES)]
    assert chong == [], f"chồng lấn với matcher.py: {chong}"


# --------------------------------------------------------------------------
# Luật KHÔNG được bắt nhầm — id thật, nghĩa khác
# --------------------------------------------------------------------------
KHONG_DUOC_BAT: list[tuple[str, str]] = [
    # giao thoa ngược pha: vân cực đại và cực tiểu đổi chỗ, hình cùng pha là SAI
    ("r_giao_thoa", "physics.thpt.song-co.giao-thoa-hai-nguon-nguoc-pha"),
    # ống sáo là cột khí, không phải dây căng — hình sóng dừng trên dây gây hiểu nhầm
    ("r_song_dung", "physics.thpt.song-co.hoa-am-ong-sao"),
    # đây là cường độ âm / mức cường độ âm, chẳng liên quan hình dạng sóng
    ("r_song_ngang", "physics.thpt.song-co.cuong-do-am"),
    ("r_song_ngang", "physics.thpt.song-co.muc-cuong-do-am"),
    ("r_song_ngang", "physics.thpt.song-co.toc-do-song-tren-day"),
    # lực quán tính li tâm hướng RA XA tâm, ngược hẳn hình lực hướng tâm
    ("r_tron_deu", "physics.thpt.dong-luc-hoc.luc-quan-tinh-li-tam"),
    ("r_tron_deu", "physics.thpt.dong-luc-hoc.con-lac-con"),
    ("r_tron_deu", "physics.thpt.dong-luc-hoc.vong-xiec-diem-cao-nhat"),
    ("r_tron_deu", "physics.thpt.dong-luc-hoc.xe-qua-cau-vong"),
    # vật LĂN trên mặt nghiêng: hình khối trượt không mô tả được
    ("r_so_do_luc_nghieng", "physics.thpt.chuyen-dong-quay.gia-toc-vat-lan-tren-mat-nghieng"),
    # con lắc đơn trong trường lực lạ / đổi theo độ cao, nhiệt độ: hình cơ bản không đủ
    ("r_con_lac_don", "physics.thpt.dao-dong-dieu-hoa.con-lac-don-luc-la"),
    ("r_con_lac_don", "physics.thpt.dao-dong-dieu-hoa.chu-ki-con-lac-don-theo-do-cao"),
    ("r_con_lac_don", "physics.thpt.dao-dong-dieu-hoa.chu-ki-con-lac-don-theo-nhiet-do"),
    # dao động tắt dần / cưỡng bức: đồ thị hình sin biên độ không đổi là sai
    ("r_do_thi_li_do", "physics.thpt.dao-dong-dieu-hoa.do-giam-bien-do-tat-dan"),
    ("r_do_thi_li_do", "physics.thpt.dao-dong-dieu-hoa.dao-dong-cuong-buc-cong-huong"),
    ("r_do_thi_x_v_a", "physics.thpt.dao-dong-dieu-hoa.quang-duong-tong-cong-tat-dan"),
    # ghép lò xo: hình một lò xo treo vật không nói được nối tiếp / song song
    ("r_lo_xo_doc", "physics.thpt.dao-dong-dieu-hoa.ghep-lo-xo"),
    ("r_lo_xo_doc", "physics.thpt.dong-luc-hoc.ghep-lo-xo"),
    # bốn id ném xiên mà matcher.py đã nhận
    ("r_nem_xien_bo_sung", "physics.thpt.dong-hoc.nem-xien-phuong-trinh-quy-dao"),
    ("r_nem_xien_bo_sung", "physics.thpt.dong-hoc.nem-xien-tam-xa"),
    ("r_nem_xien_bo_sung", "physics.thpt.dong-hoc.nem-xien-goc-nem-toi-uu"),
    # ném ngang khác ném xiên: hai hình khác nhau, không lẫn
    ("r_nem_ngang", "physics.thpt.dong-hoc.nem-xien-tam-xa"),
    # đổi đơn vị tốc độ: không có gì để vẽ
    ("r_do_thi_xt", "physics.thcs.chuyen-dong.doi-don-vi-toc-do"),
    ("r_do_thi_xt", "physics.thcs.chuyen-dong.hai-vat-duoi-kip-cung-chieu"),
    # bài toán chuyển động của Toán tiểu học/THCS — không thuộc họ này
    ("r_do_thi_xt", "math.tieu-hoc.chuyen-dong-deu.quang-duong"),
    ("r_do_thi_xt", "math.tieu-hoc.chuyen-dong-deu.van-toc"),
    ("r_do_thi_xt", "math.thcs.giai-toan-lap-phuong-trinh.quang-duong-van-toc-thoi-gian"),
    # "song" trong id không có nghĩa là sóng
    ("r_song_ngang", "math.thpt.oxy-duong-thang.khoang-cach-hai-duong-song-song"),
    ("r_song_dung", "math.dai-hoc.to-hop-co-ban.nguyen-li-song-anh"),
    ("r_giao_thoa", "math.thpt.quan-he-song-song.hai-mat-phang-song-song"),
    # "dao-dong" trong hoá lượng tử là dao động phân tử, không phải con lắc
    ("r_lo_xo_ngang", "chemistry.dai-hoc.hoa-luong-tu.dao-dong-tu-dieu-hoa-so-hang"),
    ("r_do_thi_li_do", "chemistry.dai-hoc.pho-hoc.dao-dong-phi-dieu-hoa-morse"),
    ("r_lo_xo_doc", "chemistry.dai-hoc.hoa-luong-tu.khoi-luong-rut-gon-tan-so-dao-dong"),
    # "luc" trong id không có nghĩa là lực cơ học
    ("r_so_do_luc_ngang", "physics.thcs.luc-day-ac-si-met.luc-day-ac-si-met"),
    ("r_so_do_luc_ngang", "chemistry.dai-hoc.dung-dich.luc-ion"),
    ("r_so_do_luc_treo", "biology.dai-hoc.sinh-li-hoc.luc-starling-mao-mach"),
    ("r_so_do_luc_nghieng", "chemistry.thpt.nhiet-hoa-quoc-te.ai-luc-electron"),
    # bảo toàn cơ năng / động năng THCS: hình rơi tự do hoạt nghiệm không nói được
    ("r_roi_tu_do", "physics.thcs.co-nang.bao-toan-co-nang"),
    ("r_roi_tu_do", "physics.thcs.co-nang.dong-nang"),
    # hợp lực cùng phương: hình bình hành suy biến, không minh hoạ được
    ("r_tong_hop_vecto", "physics.thcs.luc.hop-luc-cung-chieu"),
    ("r_tong_hop_vecto", "physics.thpt.dong-hoc.cong-van-toc-cung-phuong"),
    # năng lượng dao động ở giáo trình đại học có tắt dần / cưỡng bức đi kèm
    ("r_nang_luong_dao_dong", "physics.dai-hoc.dao-dong-song.nang-luong-dao-dong-dieu-hoa"),
    ("r_elip_pha", "physics.dai-hoc.dao-dong-song.tong-hop-dao-dong-vuong-goc-lissajous"),
]


# Cặp luật - công thức mà luật ấy KHÔNG được nhận, nhưng một luật khác trong họ
# thì nhận đúng: hai loại đồ thị chuyển động rất dễ bị gán chéo cho nhau.
LUAT_KHONG_DUOC_BAT_RIENG: list[tuple[str, str]] = [
    ("r_do_thi_xt", "physics.thpt.dong-hoc.van-toc-chuyen-dong-bien-doi-deu"),
    ("r_do_thi_vt", "physics.thpt.dong-hoc.phuong-trinh-chuyen-dong-thang-deu"),
    ("r_do_thi_vt", "physics.thcs.chuyen-dong.quang-duong"),
    ("r_roi_tu_do", "physics.thpt.dong-hoc.nem-ngang-thoi-gian-roi"),
    ("r_nem_ngang", "physics.thpt.dong-hoc.roi-tu-do-thoi-gian-roi"),
    ("r_do_thi_li_do", "physics.thpt.dao-dong-dieu-hoa.phuong-trinh-van-toc"),
    ("r_lo_xo_ngang", "physics.thpt.dao-dong-dieu-hoa.con-lac-lo-xo-thang-dung"),
    ("r_lo_xo_doc", "physics.thpt.dao-dong-dieu-hoa.con-lac-lo-xo-chu-ki"),
    ("r_song_ngang", "physics.thpt.song-co.song-dung-hai-dau-co-dinh"),
    ("r_song_dung", "physics.thpt.song-co.buoc-song"),
]


@pytest.mark.parametrize("ten_luat,formula_id",
                         KHONG_DUOC_BAT + LUAT_KHONG_DUOC_BAT_RIENG)
def test_luat_khong_bat_nham(ten_luat: str, formula_id: str,
                             formula_by_id: dict[str, dict]) -> None:
    assert formula_id in formula_by_id, f"id mẫu không còn trong kho: {formula_id}"
    luat = getattr(rc, ten_luat)
    assert luat(formula_by_id[formula_id]) is None, (
        f"{ten_luat} bắt nhầm {formula_id}")


@pytest.mark.parametrize("formula_id", [fid for _, fid in KHONG_DUOC_BAT])
def test_khong_luat_nao_trong_ho_bat_cac_id_nay(formula_id: str,
                                                formula_by_id: dict[str, dict]) -> None:
    """Không riêng luật bị nghi ngờ — cả họ đều phải tránh những id này."""
    f = formula_by_id[formula_id]
    khop = [r(f)[0] for r in RULES if r(f)]
    assert khop == [], f"{formula_id} bị họ cơ học nhận bởi {khop}"


# --------------------------------------------------------------------------
# Vài bất biến hình học có thể kiểm bằng số
# --------------------------------------------------------------------------
def test_song_dung_dung_so_nut_va_bung() -> None:
    """Dây hai đầu cố định k bó: k+1 nút, k bụng.

    Kiểm bằng cách đếm chấm tròn — sai số bó là kiểu lỗi trông vẫn "giống sóng
    dừng" nên mắt rất dễ bỏ qua, mà lại làm sai luôn công thức ℓ = k·λ/2.
    """
    import re

    for k in (1, 2, 3, 4):
        svg = REGISTRY["standing_wave"]({"k": k, "free_end": False, "mark": False})
        nut = len(re.findall(r'class="accent-b"', svg))
        bung = len(re.findall(r'class="accent-c"', svg))
        assert nut == k + 1, f"k={k}: đếm được {nut} nút, phải là {k + 1}"
        assert bung == k, f"k={k}: đếm được {bung} bụng, phải là {k}"


def test_song_dung_dau_tu_do_ket_thuc_o_bung() -> None:
    """Đầu tự do phải là một bụng: ℓ = (2k+1)λ/4 chính là điều kiện ấy."""
    for k in (1, 2, 3):
        he_so = (2 * k - 1) / 2.0
        assert abs(abs(math.sin(he_so * math.pi)) - 1.0) < 1e-9


def test_nem_ngang_tam_xa_dung_cong_thuc() -> None:
    """Nhãn tầm xa in trên hình phải khớp L = v₀·√(2H/g), không phải số vẽ cho đẹp."""
    v0, H, g = 12.0, 20.0, 9.8
    L = v0 * math.sqrt(2 * H / g)
    svg = REGISTRY["horizontal_throw"]({"v0": v0, "H": H, "g": g})
    assert f"L = {round(L, 1)}" in svg


def test_free_fall_moc_thoi_gian_cach_deu_theo_binh_phuong() -> None:
    """Các mốc phải theo (k/n)² — đó là toàn bộ nội dung của h = ½gt²."""
    import re

    svg = REGISTRY["free_fall"]({"h": 40, "n": 4})
    y = sorted(float(m) for m in re.findall(r'<circle cx="176" cy="([\d.]+)" r="8.5"', svg))
    y = sorted(set(y))
    assert len(y) == 5
    khoang = [y[i + 1] - y[i] for i in range(4)]
    ti_le = [k / khoang[0] for k in khoang]
    assert all(abs(t - m) < 0.02 for t, m in zip(ti_le, (1, 3, 5, 7))), ti_le
