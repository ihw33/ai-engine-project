"""Basic configuration placeholders for the AI Engine project."""

from typing import Optional


class Settings:
    app_name: str = "AI Engine"
    debug: bool = False
    environment: str = "local"
    database_url: Optional[str] = None


settings = Settings()

