from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env", env_file_encoding="utf-8", extra="ignore"
    )

    app_name: str = "Quản lý sản phẩm"
    database_url: str = "sqlite:///" + (PROJECT_ROOT / "data" / "products.db").as_posix()
