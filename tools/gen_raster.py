#!/usr/bin/env python3
"""Sinh ảnh raster cho công thức từ manifest prompts.json, rồi ghi attached.json.

Hai backend:

  --backend cloudflare   Gọi Cloudflare Workers AI (REST). Cần biến môi trường
                         CF_ACCOUNT_ID và CF_API_TOKEN (token của bạn, KHÔNG lưu trong repo).
                         Model mặc định lấy từ manifest (@cf/black-forest-labs/flux-1-schnell).

  --backend placeholder  Vẽ ảnh tạm bằng Pillow (không cần mạng/API) để chạy thử toàn tuyến.
                         Ảnh gắn status="placeholder", thay bằng ảnh thật qua cùng đường attach.

Sau khi sinh (hoặc với --attach-only), quét raster/*.png và ghi
data/illustrations/raster/attached.json (path, kích thước, prompt, model, status) —
đầu vào để tools/build_illustrations.py gộp raster vào index.

Ví dụ:
    export CF_ACCOUNT_ID=xxxx CF_API_TOKEN=yyyy
    python3 tools/gen_raster.py --backend cloudflare
    python3 tools/gen_raster.py --backend placeholder            # thử offline
    python3 tools/gen_raster.py --attach-only                    # chỉ quét lại PNG có sẵn
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

RASTER_DIR = ROOT / "data" / "illustrations" / "raster"
PROMPTS = RASTER_DIR / "prompts.json"
ATTACHED = RASTER_DIR / "attached.json"

_NEG_OK = ("stable-diffusion", "sdxl", "dreamshaper", "lightning")  # model nhận negative_prompt


# --------------------------------------------------------------------------
# backend: Cloudflare Workers AI (REST)
# --------------------------------------------------------------------------
def gen_cloudflare(p: dict) -> bytes:
    import requests  # nhập trong hàm để backend placeholder không cần requests

    acct = os.environ.get("CF_ACCOUNT_ID")
    token = os.environ.get("CF_API_TOKEN")
    if not acct or not token:
        # Tự động nạp từ cấu hình Wrangler của hệ thống nếu có
        wrangler_cfg = Path.home() / "Library/Preferences/.wrangler/config/default.toml"
        if not wrangler_cfg.exists():
            wrangler_cfg = Path.home() / ".wrangler/config/default.toml"
        if wrangler_cfg.exists():
            try:
                import tomllib
                with open(wrangler_cfg, "rb") as f:
                    wdata = tomllib.load(f)
                    token = token or wdata.get("oauth_token")
                    acct = acct or "538f170a4371858f97066cf05483b585"
            except Exception:
                pass

    if not acct or not token:
        raise SystemExit("Thiếu CF_ACCOUNT_ID / CF_API_TOKEN trong môi trường (hoặc chưa đăng nhập Wrangler).")
    model = p["model"]
    url = f"https://api.cloudflare.com/client/v4/accounts/{acct}/ai/run/{model}"
    body: dict = {"prompt": p["prompt"]}
    if "flux" in model:
        body["steps"] = 6
    if any(k in model for k in _NEG_OK) and p.get("negative_prompt"):
        body["negative_prompt"] = p["negative_prompt"]
    r = requests.post(url, headers={"Authorization": f"Bearer {token}"}, json=body, timeout=180)
    r.raise_for_status()
    ctype = r.headers.get("content-type", "")
    if "application/json" in ctype:
        data = r.json()
        if not data.get("success", True):
            raise SystemExit(f"Cloudflare lỗi: {data.get('errors')}")
        img_b64 = data["result"]["image"]           # flux trả base64
        return base64.b64decode(img_b64)
    return r.content                                  # sdxl trả bytes ảnh trực tiếp


# --------------------------------------------------------------------------
# backend: placeholder (Pillow) — ảnh tạm, không cần mạng
# --------------------------------------------------------------------------
_SUBJECT_COLOR = {"math": (37, 99, 235), "physics": (13, 148, 136),
                  "chemistry": (217, 119, 6), "biology": (22, 163, 74)}


def _font(size: int):
    from PIL import ImageFont
    for path in ("/System/Library/Fonts/Supplemental/Arial.ttf",
                 "/System/Library/Fonts/Helvetica.ttc",
                 "/Library/Fonts/Arial.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    from PIL import ImageFont as IF
    return IF.load_default()


def gen_placeholder(p: dict) -> bytes:
    from io import BytesIO
    from PIL import Image, ImageDraw

    W, H = p.get("width", 1024), int(p.get("height", 1024) * 0.75) or 768
    col = _SUBJECT_COLOR.get(p["subject"], (100, 116, 139))
    img = Image.new("RGB", (W, H), (248, 250, 252))
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 96], fill=col)
    d.text((36, 30), p["subject"].upper(), font=_font(34), fill=(255, 255, 255))
    d.text((W - 260, 34), "ẢNH TẠM", font=_font(28), fill=(255, 255, 255, 200))
    d.text((36, 150), "\n".join(textwrap.wrap(p.get("name_vi", p["formula_id"]), 34)),
           font=_font(40), fill=(30, 41, 59))
    d.multiline_text((36, 360), "\n".join(textwrap.wrap(p.get("scene", ""), 60)),
                     font=_font(24), fill=(100, 116, 139), spacing=8)
    d.text((36, H - 60), p["formula_id"], font=_font(20), fill=(148, 163, 184))
    d.rectangle([0, 0, W - 1, H - 1], outline=(226, 232, 240), width=2)
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


BACKENDS = {"cloudflare": gen_cloudflare, "placeholder": gen_placeholder}


# --------------------------------------------------------------------------
def png_size(path: Path) -> tuple[int, int]:
    from PIL import Image
    with Image.open(path) as im:
        return im.width, im.height


def rebuild_attached(prompts: list[dict], run_status: dict[str, str]) -> dict:
    """Quét raster/*.png hiện có, ghép prompt + status thành attached.json."""
    by_id = {p["formula_id"]: p for p in prompts}
    prior = {}
    if ATTACHED.exists():
        prior = {a["formula_id"]: a for a in json.loads(ATTACHED.read_text(encoding="utf-8")).get("attached", [])}
    attached = []
    for png in sorted(RASTER_DIR.glob("*.png")):
        fid = png.stem
        w, h = png_size(png)
        p = by_id.get(fid, {})
        status = run_status.get(fid) or prior.get(fid, {}).get("status") or "ai"
        attached.append({
            "formula_id": fid,
            "path": f"raster/{png.name}",
            "width": w, "height": h,
            "prompt": p.get("prompt", prior.get(fid, {}).get("prompt", "")),
            "model": p.get("model", prior.get(fid, {}).get("model", "")),
            "status": status,
        })
    return {"meta": {"count": len(attached), "generated_by": "tools/gen_raster.py"},
            "attached": attached}


def main() -> int:
    ap = argparse.ArgumentParser(description="Sinh ảnh raster cho công thức.")
    ap.add_argument("--backend", choices=list(BACKENDS), default="placeholder")
    ap.add_argument("--only", help="chỉ sinh cho một formula_id")
    ap.add_argument("--limit", type=int, default=0, help="giới hạn số ảnh sinh (0 = tất cả)")
    ap.add_argument("--force", action="store_true", help="sinh lại kể cả khi PNG đã có")
    ap.add_argument("--attach-only", action="store_true", help="không sinh, chỉ quét lại PNG có sẵn")
    args = ap.parse_args()

    if not PROMPTS.exists():
        raise SystemExit("Chưa có prompts.json. Chạy: python3 tools/build_raster_prompts.py")
    prompts = json.loads(PROMPTS.read_text(encoding="utf-8"))["prompts"]
    RASTER_DIR.mkdir(parents=True, exist_ok=True)

    run_status: dict[str, str] = {}
    if not args.attach_only:
        gen = BACKENDS[args.backend]
        todo = [p for p in prompts if not args.only or p["formula_id"] == args.only]
        made = 0
        for p in todo:
            if args.limit and made >= args.limit:
                break
            out = RASTER_DIR / f"{p['formula_id']}.png"
            if out.exists() and not args.force:
                print(f"  bỏ qua (đã có): {p['formula_id']}")
                continue
            try:
                out.write_bytes(gen(p))
                run_status[p["formula_id"]] = "placeholder" if args.backend == "placeholder" else "ai"
                made += 1
                print(f"  ✓ {args.backend}: {p['formula_id']}")
            except SystemExit:
                raise
            except Exception as exc:  # noqa: BLE001
                print(f"  ✖ lỗi {p['formula_id']}: {exc}")
        print(f"Đã sinh {made} ảnh ({args.backend}).")

    manifest = rebuild_attached(prompts, run_status)
    ATTACHED.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"attached.json: {manifest['meta']['count']} ảnh -> {ATTACHED.relative_to(ROOT)}")
    print("Chạy tiếp: python3 tools/build_illustrations.py  (gộp raster vào index)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
