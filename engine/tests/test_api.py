"""REST API."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from aistem.api.main import app


@pytest.fixture(scope="module")
def client(request) -> TestClient:
    return TestClient(app)


def test_health(client: TestClient) -> None:
    body = client.get("/health").json()
    assert body["status"] == "ok"
    assert body["records"] > 6000


def test_stats(client: TestClient) -> None:
    body = client.get("/stats").json()
    assert set(body["counts"]) == {"formula", "lesson", "problem", "exam"}


def test_search(client: TestClient) -> None:
    body = client.get(
        "/search", params={"q": "nong do mol", "kind": ["formula"], "limit": 5}
    ).json()
    assert body["total"] > 0
    assert all(h["kind"] == "formula" for h in body["hits"])


def test_search_rejects_bad_filter_values(client: TestClient) -> None:
    assert client.get("/search", params={"q": "x", "subject": "khong-co-mon"}).status_code == 422
    assert client.get("/search", params={"q": "x", "grade": 99}).status_code == 422


def test_get_record_and_404(client: TestClient) -> None:
    assert client.get("/formulas/chemistry.thcs.dung-dich.nong-do-mol").status_code == 200
    assert client.get("/formulas/khong-ton-tai").status_code == 404


def test_formula_usage(client: TestClient) -> None:
    body = client.get("/formulas/math.thpt.dao-ham.dao-ham-cua-tich/usage").json()
    assert isinstance(body, list) and body


def test_classify(client: TestClient) -> None:
    body = client.post("/classify", json={"statement": "Tính đạo hàm của y = x^2"}).json()
    assert body["subject"] == "math"
    assert client.post("/classify", json={}).status_code == 400


def test_grade(client: TestClient) -> None:
    body = client.post(
        "/grade", json={"problem_id": "prob.math.ap-calculus.0001", "student_answer": "B"}
    ).json()
    assert body["correct"] is False
    assert body["why_wrong"]
    assert client.post(
        "/grade", json={"problem_id": "khong-co", "student_answer": "A"}
    ).status_code == 404


def test_diagnose(client: TestClient) -> None:
    body = client.post(
        "/diagnose", json={"answers": {"prob.math.ap-calculus.0001": "B"}}
    ).json()
    assert body["total"] == 1
    assert client.post("/diagnose", json={"answers": {}}).status_code == 400


def test_practice(client: TestClient) -> None:
    body = client.get("/practice", params={"skill": ["khử nhân tử chung"], "limit": 3}).json()
    assert all(h["kind"] == "problem" for h in body)


def test_solve_without_key_still_returns_context(client: TestClient) -> None:
    body = client.post("/solve", json={"statement": "Tính giới hạn lim x->3 (x^2-9)/(x^2-5x+6)"})
    assert body.status_code == 200
    payload = body.json()
    assert payload["classification"]["subject"] == "math"
    assert payload["context"]["formulas"]


def test_solve_rejects_empty_statement(client: TestClient) -> None:
    assert client.post("/solve", json={"statement": "   "}).status_code == 400


def test_openapi_is_complete(client: TestClient) -> None:
    """Lược đồ OpenAPI là hợp đồng để sinh client cho web/mobile."""
    schema = client.get("/openapi.json").json()
    for path in ("/search", "/solve", "/grade", "/diagnose", "/practice", "/health"):
        assert path in schema["paths"]


def test_lifespan_builds_the_database_on_first_start(tmp_path, monkeypatch) -> None:
    """`docker run` lần đầu chưa có file .db — vòng đời ứng dụng phải tự dựng.

    Đây là đường chỉ chạy khi khởi động thật, nên nếu không test riêng thì lỗi
    ở đây chỉ lộ ra lúc container đã lên.
    """
    from aistem.config import settings

    target = tmp_path / "fresh.db"
    monkeypatch.setattr(settings, "db_path", target)
    assert not target.exists()

    with TestClient(app) as started:          # `with` mới chạy lifespan
        assert started.get("/health").status_code == 200
    assert target.exists()


def test_illustration_endpoints(client: TestClient) -> None:
    formula_id = "math.thcs.he-thuc-luong.dinh-li-pytago"
    body = client.get(f"/formulas/{formula_id}/illustration").json()
    assert body["caption_vi"]
    assert body["svg"].lstrip().startswith("<svg")

    raw = client.get(f"/illustrations/{formula_id}.svg")
    assert raw.status_code == 200
    assert raw.headers["content-type"].startswith("image/svg+xml")
    assert "default-src 'none'" in raw.headers["content-security-policy"]

    assert client.get("/formulas/khong-co-hinh/illustration").status_code == 404
    assert client.get("/illustrations/khong-co.svg").status_code == 404


def test_catch_all_route_does_not_shadow_specific_ones(client: TestClient) -> None:
    """`/{collection}/{record_id}` khớp mọi đường dẫn hai đoạn.

    Khai báo nó trước `/illustrations/<id>.svg` thì route SVG không bao giờ
    chạy tới, và người gọi nhận 422 thay vì tấm ảnh.
    """
    formula_id = "math.thcs.he-thuc-luong.dinh-li-pytago"
    assert client.get(f"/illustrations/{formula_id}.svg").status_code == 200
    assert client.get(f"/formulas/{formula_id}").status_code == 200

