"""Lớp gọi Claude.

Mọi lời gọi mô hình đều đi qua đây, vì ba lí do: (1) buộc trả về JSON đúng
lược đồ bằng cơ chế tool-use thay vì bóc chuỗi, (2) có bộ nhớ đệm trên đĩa nên
chạy lại cùng một đề không tốn thêm tiền, (3) khi thiếu khoá API thì hỏng ở một
chỗ duy nhất với thông báo rõ ràng, chứ không rải lỗi khắp pipeline.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .config import settings


class LLMUnavailable(RuntimeError):
    """Chưa cấu hình khoá API, hoặc gọi mô hình thất bại."""


@dataclass
class LLMResult:
    data: Any
    model: str
    input_tokens: int = 0
    output_tokens: int = 0
    cached: bool = False


def available() -> bool:
    return settings.has_llm


def _client():
    if not settings.anthropic_api_key:
        raise LLMUnavailable(
            "Chưa có khoá API. Đặt biến môi trường AISTEM_ANTHROPIC_API_KEY "
            "(hoặc ghi vào engine/.env) để bật phần giải bài bằng mô hình. "
            "Các chức năng tra cứu, chấm bài và kiểm chứng CAS vẫn chạy không cần khoá."
        )
    from anthropic import Anthropic

    return Anthropic(api_key=settings.anthropic_api_key, timeout=settings.llm_timeout)


def _cache_key(*parts: Any) -> str:
    blob = json.dumps(parts, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:32]


def _cache_read(key: str) -> Any | None:
    if not settings.llm_cache:
        return None
    path = settings.cache_dir / f"{key}.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _cache_write(key: str, value: Any) -> None:
    if not settings.llm_cache:
        return
    try:
        (settings.cache_dir / f"{key}.json").write_text(
            json.dumps(value, ensure_ascii=False), encoding="utf-8"
        )
    except OSError:
        pass


def _blocks(prompt: str, image_base64: str | None, image_media_type: str) -> list[dict[str, Any]]:
    blocks: list[dict[str, Any]] = []
    if image_base64:
        blocks.append(
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": image_media_type,
                    "data": image_base64,
                },
            }
        )
    blocks.append({"type": "text", "text": prompt})
    return blocks


def structured(
    *,
    system: str,
    prompt: str,
    schema: dict[str, Any],
    tool_name: str = "tra_ket_qua",
    tool_description: str = "Trả kết quả theo đúng lược đồ.",
    model: str | None = None,
    max_tokens: int | None = None,
    image_base64: str | None = None,
    image_media_type: str = "image/png",
) -> LLMResult:
    """Gọi Claude và buộc trả về một object JSON đúng `schema`.

    Dùng tool-use với `tool_choice` chỉ đích danh: mô hình không có đường nào
    khác ngoài gọi công cụ, nên kết quả luôn là JSON hợp lệ và đúng kiểu —
    không phải bóc tách chuỗi hay chịu cảnh mô hình nói thêm vài câu dẫn nhập.
    """
    chosen_model = model or settings.model
    key = _cache_key("structured", system, prompt, schema, chosen_model, bool(image_base64))
    cached = _cache_read(key)
    if cached is not None:
        return LLMResult(data=cached, model=chosen_model, cached=True)

    client = _client()
    try:
        response = client.messages.create(
            model=chosen_model,
            max_tokens=max_tokens or settings.max_tokens,
            system=system,
            messages=[{"role": "user", "content": _blocks(prompt, image_base64, image_media_type)}],
            tools=[
                {
                    "name": tool_name,
                    "description": tool_description,
                    "input_schema": schema,
                }
            ],
            tool_choice={"type": "tool", "name": tool_name},
        )
    except Exception as exc:  # lỗi mạng, hết hạn mức, khoá sai…
        raise LLMUnavailable(f"Gọi Claude thất bại: {exc}") from exc

    payload = next(
        (block.input for block in response.content if getattr(block, "type", "") == "tool_use"),
        None,
    )
    if payload is None:
        raise LLMUnavailable("Claude không trả về khối tool_use như yêu cầu")

    _cache_write(key, payload)
    return LLMResult(
        data=payload,
        model=chosen_model,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
    )


def text(
    *,
    system: str,
    prompt: str,
    model: str | None = None,
    max_tokens: int | None = None,
    image_base64: str | None = None,
    image_media_type: str = "image/png",
) -> LLMResult:
    """Gọi Claude lấy câu trả lời dạng văn bản thuần."""
    chosen_model = model or settings.model
    key = _cache_key("text", system, prompt, chosen_model, bool(image_base64))
    cached = _cache_read(key)
    if cached is not None:
        return LLMResult(data=cached, model=chosen_model, cached=True)

    client = _client()
    try:
        response = client.messages.create(
            model=chosen_model,
            max_tokens=max_tokens or settings.max_tokens,
            system=system,
            messages=[{"role": "user", "content": _blocks(prompt, image_base64, image_media_type)}],
        )
    except Exception as exc:
        raise LLMUnavailable(f"Gọi Claude thất bại: {exc}") from exc

    answer = "".join(
        block.text for block in response.content if getattr(block, "type", "") == "text"
    )
    _cache_write(key, answer)
    return LLMResult(
        data=answer,
        model=chosen_model,
        input_tokens=response.usage.input_tokens,
        output_tokens=response.usage.output_tokens,
    )


# --------------------------------------------------------------------------
# Cloudflare Workers AI Provider (DeepSeek R1 / Llama 3.3 / Llama 3.1)
# --------------------------------------------------------------------------
def _get_cloudflare_auth(force_refresh: bool = False) -> tuple[str, str]:
    """Lấy Account ID và Bearer Token cho Cloudflare Workers AI với cơ chế tự động gia hạn token."""
    acct = os.environ.get("CF_ACCOUNT_ID")
    token = os.environ.get("CF_API_TOKEN")

    if not acct or not token:
        candidates = [
            Path.home() / "Library/Preferences/.wrangler/config/default.toml",
            Path.home() / ".wrangler/config/default.toml",
        ]

        if force_refresh:
            try:
                import subprocess
                subprocess.run(["npx", "wrangler", "whoami"], capture_output=True, timeout=20)
            except Exception:
                pass

        for cfg in candidates:
            if cfg.exists():
                try:
                    import tomllib
                    from datetime import datetime, timezone

                    with open(cfg, "rb") as f:
                        wdata = tomllib.load(f)
                    
                    # Kiểm tra thời hạn của token nếu có
                    exp_str = wdata.get("expiration_time")
                    is_expired = False
                    if exp_str:
                        try:
                            # 2026-09-15T07:33:02.667Z
                            clean_exp = exp_str.replace("Z", "+00:00")
                            exp_dt = datetime.fromisoformat(clean_exp)
                            if datetime.now(timezone.utc) >= exp_dt:
                                is_expired = True
                        except Exception:
                            pass

                    if is_expired and not force_refresh:
                        try:
                            import subprocess
                            subprocess.run(["npx", "wrangler", "whoami"], capture_output=True, timeout=20)
                            with open(cfg, "rb") as f2:
                                wdata = tomllib.load(f2)
                        except Exception:
                            pass

                    token = token or wdata.get("oauth_token")
                    acct = acct or "538f170a4371858f97066cf05483b585"
                    if token and acct:
                        break
                except Exception:
                    pass

    if not acct or not token:
        raise LLMUnavailable(
            "Chưa cấu hình Cloudflare Workers AI. Hãy đăng nhập Wrangler hoặc đặt CF_ACCOUNT_ID và CF_API_TOKEN."
        )
    return acct, token


CF_MODEL_MAP = {
    "deepseek-r1": "@cf/deepseek-ai/deepseek-r1-distill-qwen-32b",
    "llama-3.3": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
    "llama-3.2-vision": "@cf/meta/llama-3.2-11b-vision-instruct",
    "qwq-32b": "@cf/qwen/qwq-32b",
    "default": "@cf/meta/llama-3.3-70b-instruct-fp8-fast",
}

CF_FALLBACK_CANDIDATES = {
    "deepseek-r1": ["llama-3.3", "qwq-32b"],
    "llama-3.3": ["deepseek-r1", "qwq-32b"],
    "qwq-32b": ["deepseek-r1", "llama-3.3"],
}


def cloudflare_chat(
    prompt: str,
    *,
    system: str = "",
    model: str = "llama-3.3",
    history: list[dict[str, str]] | None = None,
    max_tokens: int = 2048,
    temperature: float = 0.6,
) -> dict[str, Any]:
    """Gửi yêu cầu hội thoại tới Cloudflare Workers AI với cơ chế tự động Failover.

    Hỗ trợ bóc tách tag suy luận `<think>...</think>` (cho DeepSeek R1).
    """
    import httpx

    acct, token = _get_cloudflare_auth()

    # Danh sách thử nghiệm: mô hình ưu tiên và các mô hình dự phòng
    models_to_try = [model]
    for alt in CF_FALLBACK_CANDIDATES.get(model, ["llama-3.3"]):
        if alt not in models_to_try:
            models_to_try.append(alt)

    messages: list[dict[str, str]] = []
    if system:
        messages.append({"role": "system", "content": system})
    if history:
        for item in history:
            role = item.get("role", "user")
            content = item.get("content", "")
            if role in ("user", "assistant", "system") and content:
                messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": prompt})

    body: dict[str, Any] = {
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
    }

    last_error: Exception | None = None
    for current_m in models_to_try:
        target_model = CF_MODEL_MAP.get(current_m, current_m)
        url = f"https://api.cloudflare.com/client/v4/accounts/{acct}/ai/run/{target_model}"
        try:
            with httpx.Client(timeout=60.0) as client:
                resp = client.post(
                    url,
                    headers={"Authorization": f"Bearer {token}"},
                    json=body,
                )
                if resp.status_code == 401:
                    acct, token = _get_cloudflare_auth(force_refresh=True)
                    resp = client.post(
                        url,
                        headers={"Authorization": f"Bearer {token}"},
                        json=body,
                    )
            if resp.status_code == 200:
                data = resp.json()
                result = data.get("result", {})
                raw_text = result.get("response", "")
                if not raw_text and "choices" in result:
                    choices = result.get("choices", [])
                    if choices:
                        raw_text = choices[0].get("message", {}).get("content") or choices[0].get("text", "")

                thinking = ""
                reply = raw_text.strip()
                think_match = re.search(r"<think>(.*?)</think>", reply, flags=re.DOTALL)
                if think_match:
                    thinking = think_match.group(1).strip()
                    reply = re.sub(r"<think>.*?</think>", "", reply, flags=re.DOTALL).strip()

                return {
                    "reply": reply,
                    "thinking": thinking,
                    "model": current_m,
                    "success": True,
                }
            else:
                last_error = LLMUnavailable(f"Mô hình {current_m} trả về {resp.status_code}: {resp.text[:200]}")
        except Exception as exc:
            last_error = exc

    raise LLMUnavailable(f"Gọi Cloudflare AI thất bại trên các mô hình {models_to_try}: {last_error}")


def cloudflare_chat_stream(
    prompt: str,
    *,
    system: str = "",
    model: str = "llama-3.3",
    history: list[dict[str, str]] | None = None,
    max_tokens: int = 2048,
    temperature: float = 0.6,
):
    """Generator phát sinh từng chunk văn bản theo thời gian thực (SSE Stream)."""
    import httpx
    import json

    target_model = CF_MODEL_MAP.get(model, model)
    acct, token = _get_cloudflare_auth()
    url = f"https://api.cloudflare.com/client/v4/accounts/{acct}/ai/run/{target_model}"

    messages: list[dict[str, str]] = []
    if system:
        messages.append({"role": "system", "content": system})
    if history:
        for item in history:
            role = item.get("role", "user")
            content = item.get("content", "")
            if role in ("user", "assistant", "system") and content:
                messages.append({"role": role, "content": content})
    messages.append({"role": "user", "content": prompt})

    body: dict[str, Any] = {
        "messages": messages,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": True,
    }

    try:
        with httpx.Client(timeout=60.0) as client:
            with client.stream("POST", url, headers={"Authorization": f"Bearer {token}"}, json=body) as resp:
                if resp.status_code == 401:
                    acct, token = _get_cloudflare_auth(force_refresh=True)
                    with client.stream("POST", url, headers={"Authorization": f"Bearer {token}"}, json=body) as resp2:
                        for line in resp2.iter_lines():
                            if line and line.startswith("data:"):
                                payload = line[5:].strip()
                                if payload == "[DONE]":
                                    break
                                try:
                                    d = json.loads(payload)
                                    delta = d.get("response") or (d.get("choices") and d["choices"][0].get("delta", {}).get("content", ""))
                                    if delta:
                                        yield delta
                                except Exception:
                                    pass
                        return

                for line in resp.iter_lines():
                    if line and line.startswith("data:"):
                        payload = line[5:].strip()
                        if payload == "[DONE]":
                            break
                        try:
                            d = json.loads(payload)
                            delta = d.get("response") or (d.get("choices") and d["choices"][0].get("delta", {}).get("content", ""))
                            if delta:
                                yield delta
                        except Exception:
                            pass
    except Exception as exc:
        yield f"\n[Lỗi kết nối streaming: {str(exc)}]"


def cloudflare_vision(
    prompt: str,
    image_bytes: bytes | str,
    *,
    max_tokens: int = 2048,
) -> dict[str, Any]:
    """Gửi ảnh chụp bài toán hoặc hình vẽ tới mô hình thị giác Llama 3.2 11B Vision."""
    import base64
    import httpx

    if isinstance(image_bytes, str):
        # Hỗ trợ Data URI base64 (ví dụ: data:image/png;base64,....)
        if "base64," in image_bytes:
            image_bytes = image_bytes.split("base64,")[1]
        image_bytes = base64.b64decode(image_bytes)

    image_ints = list(image_bytes)
    acct, token = _get_cloudflare_auth()
    url = f"https://api.cloudflare.com/client/v4/accounts/{acct}/ai/run/@cf/meta/llama-3.2-11b-vision-instruct"

    body: dict[str, Any] = {
        "prompt": prompt,
        "image": image_ints,
        "max_tokens": max_tokens,
    }

    try:
        with httpx.Client(timeout=60.0) as client:
            resp = client.post(
                url,
                headers={"Authorization": f"Bearer {token}"},
                json=body,
            )
            if resp.status_code == 401:
                acct, token = _get_cloudflare_auth(force_refresh=True)
                resp = client.post(
                    url,
                    headers={"Authorization": f"Bearer {token}"},
                    json=body,
                )
    except Exception as exc:
        raise LLMUnavailable(f"Lỗi kết nối tới Cloudflare Vision AI: {exc}") from exc

    if resp.status_code != 200:
        raise LLMUnavailable(f"Cloudflare Vision AI trả về mã {resp.status_code}: {resp.text[:300]}")

    data = resp.json()
    reply = data.get("result", {}).get("response", "").strip()

    return {
        "reply": reply,
        "model": "llama-3.2-vision",
        "success": True,
    }


def cas_tool_eval(
    expression: str,
    operation: str = "solve",
    variable: str = "x",
) -> dict[str, Any]:
    """Cầu nối tính toán đại số biểu tượng qua SymPy Engine để chống ảo giác số học."""
    try:
        from aistem.cas.solver import solve_symbolic_equation, symbolic_calculus_eval

        if operation == "solve":
            res = solve_symbolic_equation(expression, target_var=variable)
            latex_list = res.get("solutions_latex", [])
            latex_str = ", ".join(f"{variable} = {sol}" for sol in latex_list) if latex_list else ""
            return {
                "success": res.get("success", False),
                "operation": "solve",
                "solutions": res.get("solutions", []),
                "latex": latex_str or ", ".join(res.get("solutions", [])),
                "solutions_latex": latex_list,
                "equation_latex": res.get("equation_latex", ""),
            }
        elif operation in ("diff", "derivative", "integrate", "integral", "limit"):
            op = "diff" if operation in ("diff", "derivative") else ("integrate" if operation in ("integrate", "integral") else "limit")
            res = symbolic_calculus_eval(op, expression, var_str=variable)
            return {
                "success": res.get("success", False),
                "operation": operation,
                "result": res.get("result_str") or str(res.get("result")),
                "latex": res.get("result_latex") or str(res.get("latex")),
            }
        else:
            import sympy as sp
            from aistem.cas.solver import _safe_parse

            expr = _safe_parse(expression)
            simplified = sp.simplify(expr)
            return {
                "success": True,
                "operation": "simplify",
                "result": str(simplified),
                "latex": sp.latex(simplified),
            }
    except Exception as exc:
        return {
            "success": False,
            "error": str(exc),
        }


def detect_math_intent(text: str) -> dict[str, Any] | None:
    """Tự động phát hiện yêu cầu toán học và gọi SymPy CAS để kiểm chứng độ chính xác 100%."""
    t = text.strip().lower()

    # 1. Đạo hàm
    m_diff = re.search(r"(?:tính\s+)?đạo\s+hàm(?:\s+của)?\s*[:\s]?\s*(.+)", t)
    if m_diff:
        expr = m_diff.group(1).strip("? .!$")
        res = cas_tool_eval(expr, operation="diff")
        if res.get("success"):
            return res

    # 2. Tích phân / Nguyên hàm
    m_int = re.search(r"(?:tính\s+)?(?:nguyên\s+hàm|tích\s+phân)(?:\s+của)?\s*[:\s]?\s*(.+)", t)
    if m_int:
        expr = m_int.group(1).strip("? .!$")
        res = cas_tool_eval(expr, operation="integrate")
        if res.get("success"):
            return res

    # 3. Giải phương trình
    m_solve = re.search(r"(?:giải\s+)?phương\s+trình(?:\s+sau)?\s*[:\s]?\s*(.+)", t)
    if m_solve:
        eq = m_solve.group(1).strip("? .!$")
        res = cas_tool_eval(eq, operation="solve")
        if res.get("success"):
            return res

    # 4. Rút gọn
    m_simp = re.search(r"rút\s+gọn(?:\s+biểu\s+thức)?\s*[:\s]?\s*(.+)", t)
    if m_simp:
        expr = m_simp.group(1).strip("? .!$")
        res = cas_tool_eval(expr, operation="simplify")
        if res.get("success"):
            return res

    # 5. Phương trình dạng A = B có biến x, y, z hoặc t
    if "=" in text and any(c in text for c in "xyztab"):
        cleaned = text.strip("? .!$")
        res = cas_tool_eval(cleaned, operation="solve")
        if res.get("success") and res.get("solutions"):
            return res

    # 6. Khối lượng mol / Phân tử khối chất hoá học (bảo toàn chữ hoa/thường)
    m_mol = re.search(r"(?:tính\s+)?(?:khối\s+lượng\s+mol|phân\s+tử\s+khối|nguyên\s+tử\s+khối|m)\s*(?:của)?\s*[:\s]?\s*([A-Za-z0-9_()]+)", text, flags=re.IGNORECASE)
    if m_mol:
        raw_f = m_mol.group(1).strip()
        f_formatted = re.sub(r"([A-Za-z)])(\d+)", r"\1_\2", raw_f)
        try:
            from aistem.cas.chemistry import molar_mass
            mm = molar_mass(f_formatted)
            if mm is not None:
                return {
                    "success": True,
                    "operation": "molar_mass",
                    "result": f"{mm:.3f} g/mol",
                    "latex": f"M_{{{f_formatted}}} = {mm:.3f}\\ \\text{{g/mol}}",
                }
        except Exception:
            pass

    # 7. Kiểm tra cân bằng phản ứng hoá học
    if ("->" in text or "→" in text or "\\rightarrow" in text) and any(el in text for el in ["H", "O", "C", "N", "Fe", "Al", "Cu", "Na", "Cl", "Ba", "S"]):
        try:
            from aistem.cas.chemistry import check_equation
            s = text.replace("→", "->").replace("=>", "->").replace("\\rightarrow", "->")
            if "->" in s:
                lhs, rhs = s.split("->", 1)
                def _wrap_chem(side: str) -> str:
                    parts = [p.strip() for p in side.split("+")]
                    w = []
                    for p in parts:
                        m = re.match(r"^([0-9/.]*)\s*([A-Za-z0-9_()^+-]+)$", p)
                        if m:
                            coef, formula = m.groups()
                            f_latex = re.sub(r"([A-Za-z)])(\d+)", r"\1_\2", formula)
                            w.append(f"{coef}\\mathrm{{{f_latex}}}" if coef else f"\\mathrm{{{f_latex}}}")
                        else:
                            w.append(p)
                    return " + ".join(w)
                latex_eq = f"{_wrap_chem(lhs)} \\rightarrow {_wrap_chem(rhs)}"
                verdict, detail = check_equation(latex_eq)
                if verdict in ("balanced", "unbalanced"):
                    return {
                        "success": True,
                        "operation": "chemical_equation_check",
                        "result": "Phản ứng đã cân bằng đúng" if verdict == "balanced" else f"Phản ứng chưa cân bằng ({detail})",
                        "latex": f"\\text{{{verdict.upper()}}}: {detail}" if detail else "\\text{CÂN BẰNG ĐÚNG}",
                    }
        except Exception:
            pass

    return None

