"""Integration tests cho API Trợ lý Gia sư AI STEM (/api/ai/chat)."""
from unittest.mock import patch
import pytest
from fastapi.testclient import TestClient

try:
    from server import app
except ImportError:
    from engine.server import app


@pytest.fixture
def client():
    return TestClient(app)


def test_api_ai_chat_empty_message_rejected(client):
    """Kiểm tra từ chối tin nhắn rỗng."""
    res = client.post(
        "/api/ai/chat",
        json={"message": "   ", "model": "llama-3.3"},
        headers={"User-Agent": "aistem-internal-audit"},
    )
    assert res.status_code == 400


def test_api_ai_chat_rag_and_response(client):
    """Kiểm tra RAG tra cứu công thức và trả lời từ mô hình."""
    mock_reply = {
        "reply": "Định luật Ohm phát biểu rằng $I = \\dfrac{U}{R}$.",
        "thinking": "Phân tích định luật Ohm...",
        "model": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
        "success": True,
    }

    with patch("engine.aistem.llm.cloudflare_chat", return_value=mock_reply):
        res = client.post(
            "/api/ai/chat",
            json={
                "message": "Định luật Ohm phát biểu như thế nào?",
                "model": "llama-3.3",
            },
            headers={"User-Agent": "aistem-internal-audit"},
        )
        assert res.status_code == 200
        data = res.json()
        assert data["success"] is True
        assert "Định luật Ohm" in data["reply"]
        assert data["thinking"] == "Phân tích định luật Ohm..."
        # Kiểm tra RAG tra cứu được công thức liên quan
        assert len(data["grounding_formulas"]) > 0
        assert any("ôm" in f["name_vi"].lower() or "ohm" in f["name_vi"].lower() for f in data["grounding_formulas"])
