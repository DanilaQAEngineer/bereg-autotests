# Этот файл/класс нужен для URL, таймаутов, браузера


from pathlib import Path
from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# Загружаем .env из корня проекта
ROOT_DIR = Path(__file__).parent.parent
load_dotenv(ROOT_DIR / ".env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        populate_by_name=True,
        env_file=ROOT_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    base_url: str = Field(default="https://pfbereg.ru", alias="BASE_URL")
    browser: str = Field(default="chrome", alias="BROWSER")
    headless: bool = Field(default=True, alias="HEADLESS")
    timeout: int = Field(default=10, alias="DEFAULT_TIMEOUT")

    # пути
    logs_dir: Path = ROOT_DIR / "logs"
    screenshots_dir: Path = ROOT_DIR / "screenshots"


settings = Settings()
