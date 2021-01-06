from functools import lru_cache

from pydantic import BaseModel
from pydantic import BaseSettings


class AbstractSettings(BaseModel):
    """Abstract settings."""

    title: str = 'ORION'
    debug: bool = False


class Settings(AbstractSettings, BaseSettings):
    """Settings."""

    class Config:
        env_file = '.env'
        env_prefix = 'ori_'


@lru_cache()
def get_settings() -> Settings:
    """Get settings."""
    return Settings()
