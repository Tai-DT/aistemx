# Hướng Dẫn Triển Khai AISTEM X (Production Deployment)

Hệ thống AISTEM X gồm 3 thành phần:
1. **Database**: PostgreSQL 16 (khuyến nghị cho môi trường lớn) hoặc SQLite `engine/aistem.db` (chạy độc lập, không cần setup DB).
2. **Backend Engine**: FastAPI + SymPy CAS + Python 3.13 (phục vụ REST API và kiêm phục vụ Frontend SPA build).
3. **Frontend**: React 19 + TypeScript + Vite (`apps/app`).

---

## Cách 1: Triển khai Monolith trên 1 VPS (Khuyến nghị, đơn giản nhất)

Dùng chính Docker Compose và Caddy (tự động cấp SSL HTTPS miễn phí).

### 1. Cấu hình DNS
Trỏ tên miền (ví dụ `aistemx.com` và `api.aistemx.com`) về IP của VPS.

### 2. Build Frontend trên VPS
```bash
git clone <repo-url> /opt/aistemx
cd /opt/aistemx
npm --prefix apps/app install
npm --prefix apps/app run build
```
*Lưu ý: Thư mục `apps/app/dist` sau khi build sẽ được FastAPI `server.py` tự động mount phục vụ tại `/` và `/assets`.*

### 3. Cài đặt môi trường Python & Khởi chạy Backend
```bash
cd /opt/aistemx/engine
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"

# Đồng bộ PostgreSQL nếu dùng Docker Postgres
docker compose -f ../docker-compose.yml up -d
.venv/bin/python sync_postgres.py

# Chạy với Systemd hoặc PM2 / Gunicorn
.venv/bin/gunicorn server:app -w 4 -k uvicorn.workers.UvicornWorker --bind 127.0.0.1:8000
```

### 4. Reverse Proxy với Caddy (hoặc Nginx)
Tạo file `/etc/caddy/Caddyfile`:
```caddy
aistemx.com {
    reverse_proxy 127.0.0.1:8000
}
```
Khởi động Caddy: `sudo systemctl restart caddy`. Caddy sẽ tự động đăng ký SSL Let's Encrypt.

---

## Cách 2: Triển khai tách biệt (Vercel / Cloudflare Pages + Cloud Backend)

### 1. Frontend (Vercel / Cloudflare Pages)
- **Root Directory**: `apps/app`
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Biến môi trường**: Tạo rewrite hoặc cấu hình `VITE_API_BASE_URL` trỏ tới domain Backend API.

### 2. Backend (Render / Railway / Fly.io / VPS)
- Chạy container từ `engine/Dockerfile` hoặc chạy trực tiếp FastAPI.
- Kết nối tới Managed PostgreSQL qua biến môi trường `AISTEM_POSTGRES_URL`.

---

## Cách 3: Triển khai qua Cloudflare Tunnel (Đang áp dụng cho aistemx.com)
Không cần mở port router hay public IP tĩnh, dùng Cloudflare Zero Trust Tunnel:
1. Cài đặt `cloudflared`:
   ```bash
   brew install cloudflared  # macOS hoặc tải binary Linux
   ```
2. Cấu hình Tunnel (`~/.cloudflared/aistemx.yml`):
   ```yaml
   tunnel: <tunnel-id>
   credentials-file: ~/.cloudflared/<tunnel-id>.json

   ingress:
     - hostname: aistemx.com
       service: http://127.0.0.1:5173
     - hostname: www.aistemx.com
       service: http://127.0.0.1:5173
     - hostname: api.aistemx.com
       service: http://127.0.0.1:8000
     - service: http_status:404
   ```
3. Chạy tunnel:
   ```bash
   cloudflared tunnel --config ~/.cloudflared/aistemx.yml run
   ```

---

## 4. Kiểm tra sức khỏe hệ thống (Health Check)
- **API Status**: `GET http://localhost:8000/api/stats`
- **Interactive Swagger Docs**: `http://localhost:8000/docs`
- **Web App**: `http://localhost:8000/`

