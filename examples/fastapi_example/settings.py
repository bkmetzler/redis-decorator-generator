from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=False)  # This is a personal preference

    redis_url: str


@lru_cache
def get_settings() -> Settings:
    return Settings()
