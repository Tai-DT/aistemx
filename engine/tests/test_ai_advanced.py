"""Integration tests cho các phân hệ AI nâng cao AISTEM X:
- Gợi ý Socratic trực tiếp trong bài toán (/api/ai/hint)
- 3 Chế độ sư phạm trong Chat (/api/ai/chat)
- Cầu nối SymPy CAS Tool-Calling (/api/ai/cas-eval)
- Lưu thẻ ghi nhớ FSRS (/api/ai/save-flashcard)
- AI Thị giác nhận diện đề bài (/api/ai/vision-solve)
"""
from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient

try:
    import server
    from server import app
except ImportError:
    from engine import server
    from engine.server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_api_ai_chat_pedagogical_modes(client):
    """Kiểm tra phản hồi của 3 chế độ sư phạm: Socratic, Deep-Dive, Scholarship."""
    mock_reply = {
        "reply": "Theo định luật bảo toàn năng lượng, $E = mc^2$.",
        "thinking": "Phân tích chế độ sư phạm...",
        "model": "llama-3.3",
        "success": True,
    }

    with patch.object(server.llm, "cloudflare_chat", return_value=mock_reply):
        # 1. Chế độ Socratic
        res_soc = client.post(
            "/api/ai/chat",
            json={
                "message": "Năng lượng nghỉ của hạt tính thế nào?",
                "pedagogical_mode": "socratic",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res_soc.status_code == 200
        data_soc = res_soc.json()
        assert data_soc["pedagogical_mode"] == "socratic"
        assert data_soc["success"] is True

        # 2. Chế độ Deep-Dive
        res_deep = client.post(
            "/api/ai/chat",
            json={
                "message": "Chứng minh phương trình sóng?",
                "pedagogical_mode": "deep_dive",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res_deep.status_code == 200
        assert res_deep.json()["pedagogical_mode"] == "deep_dive"

        # 3. Chế độ Scholarship
        res_sch = client.post(
            "/api/ai/chat",
            json={
                "message": "Ứng dụng hạt nano trong y học?",
                "pedagogical_mode": "scholarship",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res_sch.status_code == 200
        assert res_sch.json()["pedagogical_mode"] == "scholarship"


def test_api_ai_hint_endpoint(client):
    """Kiểm tra sinh gợi ý Socratic cho một bài toán cụ thể."""
    mock_hint = {
        "reply": "Hãy nhớ rằng gia tốc liên hệ với vận tốc qua đạo hàm: $a(t) = v'(t)$. Em hãy thử tính đạo hàm của phương trình vận tốc.",
        "thinking": "Gợi ý bước 1...",
        "model": "llama-3.3",
        "success": True,
    }

    with patch.object(server.llm, "cloudflare_chat", return_value=mock_hint):
        # Lấy thử một bài toán bất kỳ
        res_prob = client.get("/api/problems?page_size=1", headers={"User-Agent": "aistem-internal-audit"})
        assert res_prob.status_code == 200
        prob_id = res_prob.json()["problems"][0]["id"]

        res = client.post(
            "/api/ai/hint",
            json={
                "problem_id": prob_id,
                "step_index": 1,
                "student_answer": "A",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res.status_code == 200
        data = res.json()
        assert data["success"] is True
        assert "hint" in data
        assert data["problem_id"] == prob_id
        assert data["step"] == 1


def test_api_ai_cas_eval_endpoint(client):
    """Kiểm tra cầu nối tính toán biểu tượng SymPy CAS."""
    # 1. Giải phương trình x^2 - 4 = 0
    res_solve = client.post(
        "/api/ai/cas-eval",
        json={
            "expression": "x**2 - 4 = 0",
            "operation": "solve",
            "variable": "x",
        },
        headers={"User-Agent": "aistem-internal-audit"},
    )
    assert res_solve.status_code == 200
    data_solve = res_solve.json()
    assert data_solve["success"] is True
    assert "-2" in str(data_solve["solutions"]) and "2" in str(data_solve["solutions"])

    # 2. Đạo hàm x^3 + 2*x
    res_diff = client.post(
        "/api/ai/cas-eval",
        json={
            "expression": "x**3 + 2*x",
            "operation": "derivative",
            "variable": "x",
        },
        headers={"User-Agent": "aistem-internal-audit"},
    )
    assert res_diff.status_code == 200
    data_diff = res_diff.json()
    assert data_diff["success"] is True
    assert "3*x**2 + 2" in data_diff["result"]


def test_api_ai_save_flashcard_endpoint(client):
    """Kiểm tra lưu thẻ ghi nhớ thông minh từ câu trả lời AI."""
    res = client.post(
        "/api/ai/save-flashcard",
        json={
            "front": "Định luật II Newton phát biểu như thế nào?",
            "back": "Gia tốc của một vật tỉ lệ thuận với lực tác dụng và tỉ lệ nghịch với khối lượng: F = m*a.",
            "latex": "F = m\\cdot a",
            "subject": "physics",
            "topic": "Động Lực Học",
        },
        headers={"User-Agent": "aistem-internal-audit"},
    )
    assert res.status_code == 200
    data = res.json()
    assert data["success"] is True
    assert data["card"]["front"] == "Định luật II Newton phát biểu như thế nào?"
    assert data["card"]["subject"] == "physics"

    # Kiểm tra lấy danh sách thẻ ghi nhớ
    res_list = client.get("/api/ai/flashcards", headers={"User-Agent": "aistem-internal-audit"})
    assert res_list.status_code == 200
    assert res_list.json()["total"] >= 1


def test_api_ai_vision_solve_endpoint(client):
    """Kiểm tra API nhận diện đề bài qua ảnh chụp bằng mô hình thị giác."""
    mock_vision_reply = {
        "reply": "Đề bài trong ảnh: Một vật có khối lượng $m = 2\\text{ kg}$ dao động điều hoà với tần số $f = 5\\text{ Hz}$.",
        "model": "llama-3.2-vision",
        "success": True,
    }

    with patch.object(server.llm, "cloudflare_vision", return_value=mock_vision_reply):
        res = client.post(
            "/api/ai/vision-solve",
            json={
                "image_base64": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII=",
                "prompt": "Trích xuất đề bài",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res.status_code == 200
        data = res.json()
        assert data["success"] is True
        assert data["model"] == "llama-3.2-vision"
        assert "dao động điều hoà" in data["reply"]


def test_api_ai_chat_with_automatic_cas_verification(client):
    """Kiểm tra AI Chat tự động phát hiện toán học và kiểm chứng bằng SymPy CAS."""
    mock_reply = {
        "reply": "Nghiệm của phương trình $x^2 - 5x + 6 = 0$ là $x = 2$ và $x = 3$.",
        "thinking": "Phân tích phương trình bậc 2...",
        "model": "llama-3.3",
        "success": True,
    }

    with patch.object(server.llm, "cloudflare_chat", return_value=mock_reply):
        res = client.post(
            "/api/ai/chat",
            json={
                "message": "Giải phương trình 2*x^2 - 5*x + 2 = 0",
                "pedagogical_mode": "deep_dive",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res.status_code == 200
        data = res.json()
        assert data["success"] is True
        assert data["cas_verification"] is not None
        assert data["cas_verification"]["success"] is True
        assert "1/2" in data["cas_verification"]["solutions"] or "2" in data["cas_verification"]["solutions"]


def test_api_ai_chat_stream_endpoint(client):
    """Kiểm tra phản hồi Streaming SSE qua /api/ai/chat-stream."""
    def mock_stream_gen(*args, **kwargs):
        yield "Định "
        yield "luật "
        yield "Ohm: "
        yield "I = U/R."

    with patch.object(server.llm, "cloudflare_chat_stream", side_effect=mock_stream_gen):
        res = client.post(
            "/api/ai/chat-stream",
            json={
                "message": "Phát biểu định luật Ohm",
                "pedagogical_mode": "socratic",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res.status_code == 200
        assert "text/event-stream" in res.headers.get("content-type", "")
        text = res.text
        assert "type" in text
        assert "metadata" in text
        assert "Định " in text
        assert "[DONE]" in text


def test_api_ai_feedback_and_training_export(client):
    """Kiểm tra lưu phản hồi Gold Dataset và trích xuất định dạng Alpaca phục vụ Fine-tuning."""
    res_fb = client.post(
        "/api/ai/feedback",
        json={
            "instruction": "Tính thể tích mol của khí lý tưởng ở đktc",
            "response": "Ở điều kiện chuẩn, 1 mol khí bất kỳ chiếm thể tích 22.4 lít.",
            "subject": "chemistry",
            "pedagogical_mode": "socratic",
            "rating": 1,
            "cas_verified": True,
        },
        headers={"User-Agent": "aistem-internal-audit"},
    )
    assert res_fb.status_code == 200
    data_fb = res_fb.json()
    assert data_fb["success"] is True
    assert "sample_id" in data_fb

    res_exp = client.get("/api/ai/training-data/export?format=alpaca", headers={"User-Agent": "aistem-internal-audit"})
    assert res_exp.status_code == 200
    data_exp = res_exp.json()
    assert data_exp["format"] == "alpaca"
    assert data_exp["total"] >= 1
    assert any("22.4 lít" in item["output"] for item in data_exp["data"])



