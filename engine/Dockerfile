# Ảnh chạy REST API của hệ thống xử lí bài toán AISTEM.
#
# Kho dữ liệu KHÔNG nằm trong ảnh — nó là dữ liệu của người dùng, gắn vào lúc
# chạy bằng volume. Nhờ vậy sửa dữ liệu không phải dựng lại ảnh, và ảnh không
# phình theo kích thước kho.

FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    AISTEM_CORPUS_ROOT=/corpus \
    AISTEM_DB_PATH=/data/aistem.db \
    AISTEM_HOST=0.0.0.0 \
    AISTEM_PORT=8000

WORKDIR /app

# Lớp phụ thuộc tách riêng để cache: sửa mã nguồn không phải cài lại thư viện.
COPY pyproject.toml README.md ./
RUN mkdir -p aistem && touch aistem/__init__.py && pip install --no-cache-dir -e .

COPY aistem ./aistem

# Chạy bằng người dùng thường, không phải root.
RUN useradd --create-home --uid 10001 aistem \
    && mkdir -p /data \
    && chown -R aistem:aistem /app /data
USER aistem

VOLUME ["/corpus", "/data"]
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=90s --retries=3 \
    CMD python -c "import urllib.request,sys; \
sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=4).status == 200 else 1)"

# Lần chạy đầu tự dựng SQLite từ kho gắn ở /corpus (mất khoảng 10 giây).
CMD ["uvicorn", "aistem.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
