"""Cấu hình toàn hệ thống. Mọi giá trị đều đặt được qua biến môi trường AISTEM_*."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def _default_corpus_root() -> Path:
    """Kho dữ liệu nằm ở thư mục cha của gói engine."""
    return Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AISTEM_", env_file=".env", extra="ignore", case_sensitive=False
    )

    # ---- Đường dẫn & Database -----------------------------------------------
    corpus_root: Path = Field(default_factory=_default_corpus_root)
    db_path: Path | None = None
    postgres_url: str = "postgresql://aistem_user:aistem_password@localhost:5434/aistem"

    # ---- LLM ----------------------------------------------------------------
    anthropic_api_key: str | None = None
    model: str = "claude-sonnet-5"
    model_heavy: str = "claude-opus-5"
    max_tokens: int = 8000
    llm_timeout: float = 180.0
    llm_cache: bool = True

    # ---- Nhúng vector (tuỳ chọn; không cấu hình thì tìm kiếm chạy thuần từ khoá)
    embed_provider: Literal["none", "voyage", "openai", "gemini"] = "none"
    embed_model: str = "voyage-3.5"
    embed_api_key: str | None = None
    embed_batch: int = 96

    # ---- Truy xuất ----------------------------------------------------------
    retrieve_formulas: int = 12
    retrieve_lessons: int = 4
    retrieve_problems: int = 4
    rrf_k: int = 60

    # ---- Kiểm chứng CAS -----------------------------------------------------
    default_tolerance: float = 0.01
    # Chặn thời gian cho một phép rút gọn. SymPy có thể chạy rất lâu trên biểu
    # thức bệnh lí; quá hạn thì trả "chưa kết luận" chứ không treo cả request.
    cas_timeout: float = 4.0
    # Trần thời gian cho cả một lượt kiểm chứng. Chặn từng phép tính là chưa đủ:
    # một lời giải có hàng chục phép nặng thì tổng vẫn thành hàng phút.
    verify_budget: float = 20.0
    # Cho phép môi trường ký hiệu (ràng buộc gom từ các bước trước) tạo ra kết
    # luận "sai". Mặc định TẮT, và nên để yên như vậy: một ràng buộc lấy từ bước
    # trước có thể đã hết hiệu lực mà không câu chữ nào báo trước — ký hiệu đổi
    # nghĩa giữa hai phần của bài, hoặc đổi đơn vị. Đo trên kho: bật lên thì số
    # bước bị bác bỏ tăng vọt và phần lớn là báo oan.
    env_may_refute: bool = False

    # ---- API ----------------------------------------------------------------
    host: str = "127.0.0.1"
    port: int = 8000
    cors_origins: list[str] = Field(default_factory=lambda: ["*"])

    @field_validator("corpus_root", mode="after")
    @classmethod
    def _check_root(cls, v: Path) -> Path:
        return v.expanduser().resolve()

    @property
    def data_dir(self) -> Path:
        return self.corpus_root / "data"

    @property
    def database(self) -> Path:
        return self.db_path or (self.corpus_root / "engine" / "aistem.db")

    @property
    def cache_dir(self) -> Path:
        d = self.corpus_root / "engine" / ".cache"
        d.mkdir(parents=True, exist_ok=True)
        return d

    @property
    def has_llm(self) -> bool:
        return bool(self.anthropic_api_key)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
