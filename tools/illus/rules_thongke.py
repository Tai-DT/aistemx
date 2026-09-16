"""Luật gán hình cho họ ``thongke``: thống kê, tổ hợp – xác suất, suy diễn thống kê.

Khớp bằng **đuôi id** (``id.endswith("." + tail)``) chứ không bằng chuỗi con: đuôi
là một đoạn slug trọn vẹn nên "thong-ke.mot" không bao giờ nuốt "thong-ke.mot-ghep-nhom",
còn khớp chuỗi con thì có. Họ ``hinhphang`` đã dùng cách này và đạt 0 lần bắt nhầm.

Vì sao nhiều công thức trong vùng này CỐ TÌNH không có hình:

* **Kiểm định/khoảng tin cậy dựa trên Student t, Fisher F, χ²** — bỏ hết. Vùng bác
  bỏ của chúng nhìn *giống* đường cong chuẩn, và đó chính là cái bẫy: hình ở đây
  ghi rõ "N(μ; σ)" trong chú thích, dán nó cho một kiểm định t là nói sai phân
  phối tham chiếu. Chỉ kiểm định z (và kiểm định chính xác nhị thức/Poisson, vốn
  vẽ được bằng biểu đồ cột thật) mới được gán hình.
* **Hoán vị – chỉnh hợp – tổ hợp** (n!, Aⁿₖ, Cⁿₖ, nhị thức Newton, Catalan,
  Stirling…) — bỏ hết. Sơ đồ cây minh hoạ QUY TẮC NHÂN, không minh hoạ n!; gán
  cây cho công thức tổ hợp là để người học tự suy ra một liên hệ không có thật.
* **Đường hồi quy x theo y** — bỏ. Hình vẽ đường y theo x, là một đường KHÁC.

Mỗi rule trả ``(generator, params, ghi_chú)`` hoặc ``None``.
"""

from __future__ import annotations

from typing import Callable, Optional

Match = tuple[str, dict, str]
Rule = Callable[[dict], Optional[Match]]


def _is(f: dict, *tails: str) -> bool:
    """Id có kết thúc bằng đúng một trong các đuôi (tính cả dấu chấm ngăn) không?"""
    fid = f["id"]
    return any(fid.endswith("." + t) for t in tails)


# Mẫu số liệu dùng lại nhiều chỗ: giữ một bộ duy nhất để mọi hình mô tả cùng nói
# về một mẫu, người học đối chiếu được trung bình / trung vị / tứ phân vị với nhau.
_MAU = [12, 15, 16, 18, 19, 20, 21, 22, 24, 25, 27, 44]
_NHOM = {"bounds": [0, 10, 20, 30, 40, 50], "freqs": [4, 9, 15, 10, 6]}
_ROI_RAC = {"values": [1, 2, 3, 4, 5, 6], "freqs": [3, 7, 12, 9, 5, 2]}


# --------------------------------------------------------------------------
# 1. Thống kê mô tả — đo xu thế trung tâm
# --------------------------------------------------------------------------
def r_trung_binh(f: dict) -> Optional[Match]:
    if _is(f, "thong-ke.so-trung-binh-cong", "thong-ke.so-trung-binh-mau",
           "thong-ke-mau.trung-binh-mau"):
        return "data_dots", {"mark": "mean"}, "trung bình trên dải số liệu"
    if _is(f, "thong-ke.so-trung-binh-cong-theo-tan-so", "thong-ke.so-trung-binh-co-tan-so"):
        return "bar_chart", dict(_ROI_RAC, show_mean=True), "trung bình có tần số"
    if _is(f, "thong-ke.so-trung-binh-ghep-nhom", "thong-ke.phuong-sai-ghep-nhom"):
        return "histogram", dict(_NHOM, show_mean=True), "mẫu ghép nhóm, x̄ theo giá trị đại diện"
    return None


def r_mot(f: dict) -> Optional[Match]:
    if _is(f, "thong-ke.mot"):
        return "bar_chart", dict(_ROI_RAC, show_mode=True), "mốt là giá trị có tần số lớn nhất"
    if _is(f, "thong-ke.mot-ghep-nhom"):
        return "histogram", dict(_NHOM, highlight=2, highlight_label="nhóm chứa mốt"), "nhóm chứa mốt"
    return None


def r_trung_vi(f: dict) -> Optional[Match]:
    if _is(f, "thong-ke.trung-vi"):
        return "data_dots", {"mark": "median"}, "trung vị chia đôi mẫu"
    if _is(f, "thong-ke.trung-vi-ghep-nhom"):
        return "cumulative_curve", dict(_NHOM, fractions=[0.5], fraction_labels=["Mₑ"]), \
            "đọc trung vị ghép nhóm trên đường tích luỹ"
    if _is(f, "thong-ke.tu-phan-vi-ghep-nhom"):
        return "cumulative_curve", dict(_NHOM, fractions=[0.25, 0.5, 0.75],
                                        fraction_labels=["Q₁", "Q₂", "Q₃"]), \
            "đọc tứ phân vị ghép nhóm trên đường tích luỹ"
    return None


# --------------------------------------------------------------------------
# 2. Thống kê mô tả — đo độ phân tán
# --------------------------------------------------------------------------
def r_tu_phan_vi(f: dict) -> Optional[Match]:
    if _is(f, "thong-ke.tu-phan-vi"):
        return "box_plot", {"data": _MAU, "show_fence": False}, "tứ phân vị trên biểu đồ hộp"
    if _is(f, "thong-ke.khoang-tu-phan-vi"):
        return "box_plot", {"data": _MAU, "show_iqr": True, "show_fence": False}, "khoảng tứ phân vị ΔQ"
    if _is(f, "thong-ke.gia-tri-ngoai-le"):
        return "box_plot", {"data": _MAU, "show_fence": True}, "hàng rào Q₁ − 1,5ΔQ và Q₃ + 1,5ΔQ"
    return None


def r_bien_thien(f: dict) -> Optional[Match]:
    if _is(f, "thong-ke.khoang-bien-thien"):
        return "data_dots", {"mark": "range"}, "khoảng biến thiên R = max − min"
    return None


def r_do_lech(f: dict) -> Optional[Match]:
    """Phương sai / độ lệch chuẩn: hình chỉ ra ĐỘ LỆCH xᵢ − x̄ — thứ được bình phương."""
    if _is(f, "thong-ke.phuong-sai-mau", "thong-ke.do-lech-chuan",
           "thong-ke.do-lech-tuyet-doi-trung-binh",
           "thong-ke-mau.phuong-sai-mau-hieu-chinh",
           "thong-ke-mau.phuong-sai-mau-chua-hieu-chinh",
           "thong-ke-mau.do-lech-chuan-mau",
           "thong-ke-sinh-hoc.trung-binh-va-do-lech-chuan"):
        return "data_dots", {"mark": "deviation"}, "mỗi đoạn là một độ lệch xᵢ − x̄"
    return None


# --------------------------------------------------------------------------
# 3. Biểu đồ
# --------------------------------------------------------------------------
def r_bieu_do(f: dict) -> Optional[Match]:
    if _is(f, "thong-ke.goc-o-tam-bieu-do-hinh-quat"):
        return "pie_chart", {}, "góc ở tâm của biểu đồ hình quạt"
    if _is(f, "thong-ke.tan-so-tuong-doi", "xac-suat.xac-suat-thuc-nghiem"):
        return "bar_chart", dict(_ROI_RAC, show_percent=True), "tần số tương đối"
    return None


# --------------------------------------------------------------------------
# 4. Tổ hợp – xác suất: quy tắc đếm và sơ đồ cây
# --------------------------------------------------------------------------
def r_quy_tac_nhan(f: dict) -> Optional[Match]:
    if _is(f, "to-hop-xac-suat.quy-tac-nhan", "to-hop-co-ban.nguyen-li-nhan",
           "xac-suat.so-ket-qua-hai-hanh-dong"):
        return "prob_tree", {"mode": "count", "m": 3, "n": 4}, "quy tắc nhân đếm số nhánh"
    if _is(f, "to-hop-xac-suat.so-do-hinh-cay"):
        return "prob_tree", {}, "sơ đồ hình cây hai giai đoạn"
    return None


def r_nhan_xac_suat(f: dict) -> Optional[Match]:
    if _is(f, "to-hop-xac-suat.cong-thuc-nhan-xac-suat-tong-quat",
           "to-hop-xac-suat.quy-tac-nhan-xac-suat-doc-lap",
           "xac-suat-co-ban.cong-thuc-nhan", "xac-suat-co-ban.cong-thuc-nhan-tong-quat"):
        return "prob_tree", {}, "xác suất một nhánh là tích dọc theo nhánh"
    if _is(f, "to-hop-xac-suat.cong-thuc-xac-suat-toan-phan",
           "xac-suat-co-ban.cong-thuc-xac-suat-day-du",
           "to-hop-xac-suat.cong-thuc-bayes", "xac-suat-co-ban.cong-thuc-bayes",
           "xac-suat.dinh-li-bayes-phan-hoach"):
        # tô hai nhánh cùng dẫn tới B: tổng của chúng chính là P(B) — mẫu số của Bayes
        return "prob_tree", {"highlight": [[0, 0], [1, 0]]}, "các nhánh dẫn tới cùng một biến cố"
    return None


# --------------------------------------------------------------------------
# 5. Tổ hợp – xác suất: sơ đồ Venn
# --------------------------------------------------------------------------
def r_quy_tac_cong(f: dict) -> Optional[Match]:
    if _is(f, "to-hop-xac-suat.quy-tac-cong", "to-hop-co-ban.nguyen-li-cong",
           "to-hop-xac-suat.quy-tac-cong-xac-suat-xung-khac"):
        return "venn2", {"mode": "disjoint"}, "cộng được vì hai biến cố rời nhau"
    if _is(f, "to-hop-xac-suat.quy-tac-cong-xac-suat",
           "xac-suat-co-ban.cong-thuc-cong-hai-bien-co"):
        return "venn2", {"mode": "union"}, "phần giao bị đếm hai lần nên phải trừ đi"
    if _is(f, "xac-suat-co-ban.cong-thuc-cong-ba-bien-co",
           "to-hop-co-ban.nguyen-li-bao-ham-loai-tru"):
        return "venn3", {}, "bao hàm – loại trừ ba tập"
    return None


def r_bien_co_doi(f: dict) -> Optional[Match]:
    if _is(f, "to-hop-xac-suat.bien-co-doi", "xac-suat-co-ban.xac-suat-bien-co-doi",
           "to-hop-co-ban.nguyen-li-bu"):
        return "venn2", {"mode": "complement"}, "biến cố đối là phần còn lại của Ω"
    return None


def r_xac_suat_co_dien(f: dict) -> Optional[Match]:
    if _is(f, "to-hop-xac-suat.xac-suat-co-dien", "xac-suat-co-ban.dinh-nghia-co-dien",
           "xac-suat.xac-suat-bien-co-dong-kha-nang"):
        return "venn2", {"mode": "classical", "n_omega": 12, "n_a": 5}, "P(A) = n(A)/n(Ω)"
    return None


def r_co_dieu_kien(f: dict) -> Optional[Match]:
    if _is(f, "to-hop-xac-suat.xac-suat-co-dieu-kien", "xac-suat-co-ban.xac-suat-co-dieu-kien"):
        return "venn2", {"mode": "conditional"}, "B trở thành không gian mẫu mới"
    return None


def r_tap_hop(f: dict) -> Optional[Match]:
    if _is(f, "menh-de-tap-hop.giao-hai-tap-hop"):
        return "venn2", {"mode": "intersection"}, "giao của hai tập hợp: phần thuộc cả A và B"
    if _is(f, "menh-de-tap-hop.hop-hai-tap-hop"):
        return "venn2", {"mode": "union"}, "hợp của hai tập hợp: phần thuộc A hoặc thuộc B"
    if _is(f, "menh-de-tap-hop.hieu-hai-tap-hop"):
        return "venn2", {"mode": "difference"}, "hiệu của hai tập hợp A \\ B: thuộc A nhưng không thuộc B"
    if _is(f, "menh-de-tap-hop.phan-bu-cua-tap-hop"):
        return "venn2", {"mode": "complement"}, "phần bù của tập con: C_E A là phần thuộc E không thuộc A"
    if _is(f, "menh-de-tap-hop.so-phan-tu-hop-hai-tap-hop"):
        return "venn2", {"mode": "union"}, "n(A ∪ B) = n(A) + n(B) − n(A ∩ B)"
    if _is(f, "menh-de-tap-hop.so-phan-tu-hop-ba-tap-hop"):
        return "venn3", {}, "công thức bao hàm – loại trừ ba tập hợp"
    return None


# --------------------------------------------------------------------------
# 6. Biến ngẫu nhiên rời rạc và các phân phối rời rạc
# --------------------------------------------------------------------------
_BANG = {"values": [0, 1, 2, 3], "freqs": [0.1, 0.3, 0.4, 0.2],
         "xlabel": "xᵢ", "ylabel": "pᵢ"}


def r_bang_phan_phoi(f: dict) -> Optional[Match]:
    if _is(f, "bien-ngau-nhien.bang-phan-phoi-xac-suat"):
        return "bar_chart", dict(_BANG), "bảng phân phối xác suất"
    if _is(f, "bien-ngau-nhien.ky-vong-bien-roi-rac", "xac-suat.ky-vong-bien-roi-rac"):
        return "bar_chart", dict(_BANG, show_mean=True), "kì vọng là hoành độ trọng tâm"
    return None


def r_nhi_thuc(f: dict) -> Optional[Match]:
    if _is(f, "phan-phoi-roi-rac.phan-phoi-nhi-thuc", "phan-phoi.dieu-kien-boi-canh-nhi-thuc"):
        return "binomial_bars", {"n": 10, "p": 0.4}, "phân phối nhị thức B(n; p)"
    if _is(f, "phan-phoi-roi-rac.phan-phoi-bernoulli"):
        return "binomial_bars", {"n": 1, "p": 0.4}, "phân phối Bernoulli (nhị thức với n = 1)"
    if _is(f, "phan-phoi.trung-binh-do-lech-chuan-nhi-thuc"):
        return "binomial_bars", {"n": 10, "p": 0.4, "show_mean": True}, "μ và σ của nhị thức"
    if _is(f, "to-hop-xac-suat.cong-thuc-bernoulli", "xac-suat-co-ban.cong-thuc-bernoulli"):
        return "binomial_bars", {"n": 10, "p": 0.4, "shade": "eq", "at": 4}, \
            "công thức Bernoulli cho một giá trị k"
    if _is(f, "xac-suat-co-ban.so-lan-co-kha-nang-nhat"):
        return "binomial_bars", {"n": 10, "p": 0.4, "shade": "eq", "at": 4}, "cột cao nhất là k khả dĩ nhất"
    if _is(f, "phan-phoi.ham-tich-luy-nhi-thuc"):
        return "binomial_bars", {"n": 20, "p": 0.3, "shade": "le", "at": 5}, "hàm tích luỹ P(X ≤ k)"
    if _is(f, "xac-suat-co-ban.xac-suat-it-nhat-mot-lan"):
        return "binomial_bars", {"n": 6, "p": 0.3, "shade": "ge", "at": 1}, "P(X ≥ 1) = 1 − P(X = 0)"
    if _is(f, "phan-phoi.xap-xi-chuan-cho-nhi-thuc", "phan-phoi.hieu-chinh-lien-tuc"):
        return "binomial_bars", {"n": 30, "p": 0.4, "overlay_normal": True}, \
            "đường cong chuẩn phủ lên các cột nhị thức"
    if _is(f, "kiem-dinh.kiem-dinh-nhi-thuc", "kiem-dinh.muc-y-nghia-thuc-te-nhi-thuc"):
        return "binomial_bars", {"n": 20, "p": 0.5, "shade": "ge", "at": 15}, \
            "kiểm định chính xác: đuôi tính thẳng trên phân phối nhị thức"
    return None


def r_poisson(f: dict) -> Optional[Match]:
    if _is(f, "phan-phoi-roi-rac.phan-phoi-poisson", "phan-phoi.poisson-ti-le-theo-khoang"):
        return "poisson_bars", {"lam": 4}, "phân phối Poisson Po(λ)"
    if _is(f, "phan-phoi.xap-xi-chuan-cho-poisson"):
        return "poisson_bars", {"lam": 16, "overlay_normal": True}, "xấp xỉ chuẩn cho Poisson"
    if _is(f, "kiem-dinh.kiem-dinh-poisson"):
        return "poisson_bars", {"lam": 4, "shade": "ge", "at": 9}, "đuôi phải của Poisson"
    return None


def r_hinh_hoc(f: dict) -> Optional[Match]:
    if _is(f, "phan-phoi-roi-rac.phan-phoi-hinh-hoc"):
        return "geometric_bars", {"p": 0.35}, "phân phối hình học"
    if _is(f, "phan-phoi.trung-binh-do-lech-chuan-hinh-hoc"):
        return "geometric_bars", {"p": 0.35, "show_mean": True}, "μ = 1/p của phân phối hình học"
    if _is(f, "phan-phoi.hinh-hoc-xac-suat-vuot-qua"):
        return "geometric_bars", {"p": 0.35, "shade": "ge", "at": 5}, "P(X ≥ k) của phân phối hình học"
    return None


# --------------------------------------------------------------------------
# 7. Phân phối chuẩn
# --------------------------------------------------------------------------
def r_phan_phoi_chuan(f: dict) -> Optional[Match]:
    if _is(f, "phan-phoi-lien-tuc.quy-tac-ba-sigma",
           "thong-ke-sinh-hoc-intl.quy-tac-68-95-do-lech-chuan"):
        return "normal_curve", {"shade": "sigma"}, "quy tắc 68 – 95 – 99,7"
    if _is(f, "phan-phoi-lien-tuc.phan-phoi-chuan", "phan-phoi-lien-tuc.phan-phoi-chuan-tac",
           "phan-phoi-lien-tuc.chuan-hoa-bien-chuan",
           "phan-phoi-mau.chuan-hoa-trung-binh-mau", "phan-phoi-mau.chuan-hoa-ti-le-mau",
           "phan-phoi-mau.dinh-li-gioi-han-trung-tam-ap",
           "thong-ke-mau.phan-phoi-trung-binh-mau"):
        return "normal_curve", {"shade": "sigma"}, "đường cong chuẩn và các dải ±kσ"
    if _is(f, "phan-phoi.xac-suat-khoang-phan-phoi-chuan", "bien-ngau-nhien.ham-mat-do",
           "bien-ngau-nhien.xac-suat-tren-doan"):
        return "normal_curve", {"shade": "between"}, "xác suất là diện tích dưới đường mật độ"
    if _is(f, "bien-ngau-nhien.ham-phan-phoi-tich-luy", "bien-ngau-nhien.phan-vi",
           "phan-phoi.nguoc-phan-phoi-chuan"):
        return "normal_curve", {"shade": "left", "z": -1.0, "area_label": "F(x) = P(X ≤ x)"}, \
            "hàm phân phối tích luỹ là diện tích đuôi trái"
    if _is(f, "phan-phoi.tinh-chat-doi-xung-phi"):
        return "normal_curve", {"shade": "two_tail", "z": 1.5, "area_label": "đuôi"}, \
            "hai đuôi đối xứng bằng nhau: Φ(−z) = 1 − Φ(z)"
    return None


# --------------------------------------------------------------------------
# 8. Kiểm định giả thuyết (chỉ kiểm định z — xem chú thích đầu tệp)
# --------------------------------------------------------------------------
def r_mien_bac_bo(f: dict) -> Optional[Match]:
    if _is(f, "kiem-dinh.p-value-hai-phia", "kiem-dinh.thong-ke-kiem-dinh-chuan-hoa",
           "kiem-dinh.kiem-dinh-z-trung-binh-biet-sigma", "kiem-dinh.kiem-dinh-z-mot-ti-le",
           "kiem-dinh.kiem-dinh-z-hai-ti-le", "kiem-dinh.quan-he-khoang-tin-cay-va-kiem-dinh",
           "kiem-dinh-gia-thuyet.mien-bac-bo", "kiem-dinh-gia-thuyet.kiem-dinh-z-mot-mau",
           "kiem-dinh-gia-thuyet.kiem-dinh-z-hai-mau",
           "thong-ke-sinh-hoc-intl.muc-y-nghia-p-0-05"):
        return "normal_curve", {"shade": "two_tail", "z": 1.96}, "miền bác bỏ hai phía ở mức α = 0,05"
    if _is(f, "kiem-dinh.p-value-mot-phia", "kiem-dinh.quy-tac-quyet-dinh-p-value",
           "kiem-dinh-gia-thuyet.p-value"):
        return "normal_curve", {"shade": "right", "z": 1.645}, "giá trị p là diện tích đuôi"
    return None


def r_luc_kiem_dinh(f: dict) -> Optional[Match]:
    if _is(f, "kiem-dinh.sai-lam-loai-i", "kiem-dinh.sai-lam-loai-ii",
           "kiem-dinh.luc-kiem-dinh", "kiem-dinh.cac-yeu-to-anh-huong-luc-kiem-dinh",
           "kiem-dinh.gia-thuyet-khong-va-doi", "kiem-dinh.co-hieu-ung-chuan-hoa",
           "kiem-dinh-gia-thuyet.sai-lam-loai-i-loai-ii",
           "thong-ke-sinh-hoc-intl.gia-thuyet-khong-va-doi"):
        return "power_curves", {}, "phân phối dưới H₀ và Hₐ, vùng α và vùng β"
    return None


# --------------------------------------------------------------------------
# 9. Ước lượng khoảng (chỉ khoảng dựa trên z)
# --------------------------------------------------------------------------
def r_khoang_tin_cay(f: dict) -> Optional[Match]:
    if _is(f, "uoc-luong-khoang.dang-tong-quat", "uoc-luong-khoang.bien-sai-so",
           "uoc-luong-khoang.do-chinh-xac-uoc-luong", "uoc-luong-khoang.dien-giai-do-tin-cay",
           "uoc-luong-khoang.gia-tri-toi-han-z-thong-dung",
           "uoc-luong-khoang.khoang-tin-cay-z-mot-ti-le",
           "uoc-luong-khoang.khoang-tin-cay-z-hai-ti-le",
           "uoc-luong-khoang.khoang-tin-cay-ky-vong-biet-phuong-sai",
           "uoc-luong-khoang.co-mau-uoc-luong-trung-binh",
           "uoc-luong-khoang.co-mau-uoc-luong-ti-le",
           "thong-ke-sinh-hoc.khoang-tin-cay",
           "thong-ke-sinh-hoc-intl.khoang-tin-cay-95-hai-sai-so-chuan"):
        return "normal_curve", {"shade": "center", "z": 1.96}, "khoảng tin cậy 95% và biên sai số"
    return None


# --------------------------------------------------------------------------
# 10. Hồi quy và tương quan
# --------------------------------------------------------------------------
def r_hoi_quy(f: dict) -> Optional[Match]:
    if _is(f, "hoi-quy.phan-du", "hoi-quy.tong-binh-phuong-phan-du-rss",
           "hoi-quy.duong-hoi-quy-binh-phuong-toi-thieu", "hoi-quy.do-lech-chuan-phan-du",
           "hoi-quy-tuong-quan.phan-tich-tong-binh-phuong",
           "hoi-quy-tuong-quan.sai-so-chuan-hoi-quy"):
        return "scatter_regression", {"show_residuals": True}, "phần dư là khoảng cách dọc tới đường hồi quy"
    if _is(f, "hoi-quy.di-qua-diem-trung-binh", "hoi-quy-tuong-quan.hiep-phuong-sai-mau"):
        return "scatter_regression", {"show_mean_point": True}, "đường hồi quy đi qua điểm (x̄; ȳ)"
    if _is(f, "hoi-quy.he-so-goc-theo-sxy", "hoi-quy.he-so-goc-theo-r", "hoi-quy.he-so-chan",
           "hoi-quy.he-so-xac-dinh-r2",
           "hoi-quy-tuong-quan.he-so-goc-hoi-quy", "hoi-quy-tuong-quan.he-so-chan-hoi-quy",
           "hoi-quy-tuong-quan.he-so-xac-dinh", "hoi-quy-tuong-quan.he-so-tuong-quan-pearson",
           "thong-ke-sinh-hoc.hoi-quy-tuyen-tinh",
           "thong-ke-sinh-hoc.he-so-tuong-quan-pearson",
           "thong-ke-sinh-hoc-intl.he-so-tuong-quan-pearson",
           "thong-ke-sinh-hoc-intl.he-so-xac-dinh-r2-do-thi"):
        return "scatter_regression", {}, "tán xạ và đường hồi quy bình phương tối thiểu"
    return None


def r_tuong_quan(f: dict) -> Optional[Match]:
    if _is(f, "hoi-quy.tinh-chat-he-so-tuong-quan", "hoi-quy.he-so-tuong-quan-theo-s",
           "hoi-quy.he-so-tuong-quan-dang-diem-z"):
        return "correlation_panels", {}, "r từ −1 tới 1 nói lên điều gì"
    return None


RULES: list[Rule] = [
    r_trung_binh, r_mot, r_trung_vi,
    r_tu_phan_vi, r_bien_thien, r_do_lech, r_bieu_do,
    r_quy_tac_nhan, r_nhan_xac_suat,
    r_quy_tac_cong, r_bien_co_doi, r_xac_suat_co_dien, r_co_dieu_kien,
    r_tap_hop,
    r_bang_phan_phoi, r_nhi_thuc, r_poisson, r_hinh_hoc,
    r_phan_phoi_chuan, r_mien_bac_bo, r_luc_kiem_dinh, r_khoang_tin_cay,
    r_hoi_quy, r_tuong_quan,
]


def match_formula(f: dict) -> Optional[Match]:
    """Luật đầu tiên trúng thì thắng — cùng quy ước với ``matcher.match_formula``."""
    for rule in RULES:
        m = rule(f)
        if m:
            return m
    return None
