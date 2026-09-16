"""Duyệt kho minh hoạ từ engine: API và tầng lưu trữ.

Trước đây kho hình chỉ tra được **từ công thức sang hình** — hợp lí khi mới có
31 hình. Thư viện lớn lên thì câu hỏi đổi chiều ("môn Lí bậc THPT đã có những
hình gì"), và đường cũ không trả lời được.
"""

from __future__ import annotations

import sqlite3

import pytest
from fastapi.testclient import TestClient

from aistem.api.main import app
from aistem.store import illustrations


@pytest.fixture(scope="module")
def client() -> TestClient:
    return TestClient(app)


class TestDuyetKho:
    def test_khong_loc_thi_tra_ve_toan_bo(self, conn: sqlite3.Connection) -> None:
        assert illustrations.browse(conn, limit=500)

    def test_loc_theo_mon(self, conn: sqlite3.Connection) -> None:
        rows = illustrations.browse(conn, subject="math", limit=500)
        assert rows
        assert all((r.model_extra or {}).get("subject") == "math" for r in rows)

    def test_loc_theo_cap(self, conn: sqlite3.Connection) -> None:
        rows = illustrations.browse(conn, level="thcs", limit=500)
        assert rows
        assert all((r.model_extra or {}).get("level") == "thcs" for r in rows)

    def test_hai_bo_loc_giao_nhau(self, conn: sqlite3.Connection) -> None:
        both = illustrations.browse(conn, subject="math", level="thcs", limit=500)
        only_subject = illustrations.browse(conn, subject="math", limit=500)
        assert len(both) <= len(only_subject)

    def test_loc_khong_khop_thi_tra_rong_chu_khong_no(
        self, conn: sqlite3.Connection
    ) -> None:
        assert illustrations.browse(conn, subject="khong-co-mon-nay") == []

    def test_tim_theo_tu_khoa(self, conn: sqlite3.Connection) -> None:
        rows = illustrations.browse(conn, query="tam-giac", limit=50)
        assert any("tam-giac" in r.formula_id for r in rows)

    def test_bo_qua_cho_danh_san(self, conn: sqlite3.Connection) -> None:
        """Hình `placeholder` không được lọt vào danh sách duyệt.

        Hiện một ô trống cho người học còn tệ hơn không hiện gì — cùng nguyên
        tắc mà `for_formulas` đang giữ.
        """
        rows = illustrations.browse(conn, limit=500)
        assert all(r.status != "placeholder" for r in rows)

    def test_facets_dem_dung(self, conn: sqlite3.Connection) -> None:
        facets = illustrations.facets(conn)
        assert set(facets) == {"subject", "level", "generator"}
        by_subject = facets["subject"]
        assert by_subject
        for subject, count in by_subject.items():
            assert len(illustrations.browse(conn, subject=subject, limit=999)) == count


class TestQuaAPI:
    def test_duyet(self, client: TestClient) -> None:
        body = client.get("/illustrations", params={"limit": 5}).json()
        assert isinstance(body, list) and body
        assert "formula_id" in body[0]

    def test_duyet_co_loc(self, client: TestClient) -> None:
        body = client.get("/illustrations", params={"subject": "math", "limit": 99}).json()
        assert body and all(item["subject"] == "math" for item in body)

    def test_facets(self, client: TestClient) -> None:
        body = client.get("/illustrations/facets").json()
        assert body["subject"] and body["generator"]

    def test_duong_svg_khong_bi_route_duyet_nuot(self, client: TestClient) -> None:
        """`/illustrations/{id}.svg` phải vẫn trả SVG, không rơi vào route duyệt.

        README ghi sẵn cái bẫy này ở một lần trước: một route khai quá rộng đã
        từng nuốt đúng đường dẫn ấy và trả 422.
        """
        listing = client.get("/illustrations", params={"limit": 1}).json()
        formula_id = listing[0]["formula_id"]
        response = client.get(f"/illustrations/{formula_id}.svg")
        assert response.status_code == 200
        assert response.headers["content-type"].startswith("image/svg+xml")
        assert response.text.startswith("<svg")

    def test_svg_khong_co_thi_bao_404(self, client: TestClient) -> None:
        assert client.get("/illustrations/khong.co.that.svg").status_code == 404
