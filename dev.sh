#!/usr/bin/env bash
# Khởi động toàn diện AISTEM X App: Backend API Engine (Port 8000) & Vite React App (Port 5173)
set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

echo "================================================================="
echo "⚡ KHỞI ĐỘNG HỆ THỐNG AISTEM X APP & BACKEND ENGINE (POSTGRESQL)"
echo "================================================================="

# 1. Kiểm tra Docker PostgreSQL
if docker ps --format '{{.Names}}' | grep -q "aistem-postgres"; then
    echo "✅ Docker PostgreSQL đang chạy trên cổng 5434."
else
    echo "⚠️ Khởi động container PostgreSQL..."
    docker-compose up -d
fi

# 2. Khởi động Backend API Server (Background)
echo "🚀 Khởi động Backend FastAPI Server trên http://127.0.0.1:8000..."
cd "$ROOT_DIR/engine"
.venv/bin/uvicorn server:app --host 127.0.0.1 --port 8000 &
BACKEND_PID=$!

# Trap để tắt backend khi tắt script
trap "echo 'Đang dừng server...'; kill $BACKEND_PID 2>/dev/null || true; exit 0" SIGINT SIGTERM EXIT

# 3. Khởi động Frontend App
echo "✨ Khởi động Frontend Vite App trên http://localhost:5173..."
cd "$ROOT_DIR/apps/app"
npm run dev
