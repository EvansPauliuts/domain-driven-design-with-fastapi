import os
from functools import lru_cache

from pydantic import AnyHttpUrl, BaseSettings


@lru_cache
def get_env() -> str:
    run_env = os.getenv('ENV')
    return f'.env.{run_env}' if run_env else '.env'


class Settings(BaseSettings):
    API_VERSION: str = '1.0.0'
    API_V1_STR: str = '/api/v1'

    PROJECT_NAME: str

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        'http://localhost',
        'http://localhost:8000',
    ]

    # DATABASE
    POSTGRES_NAME: str = os.getenv('POSTGRES_NAME')
    POSTGRES_PORT: str = os.getenv('POSTGRES_PORT')
    POSTGRES_DB: str = os.getenv('POSTGRES_DB')
    POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    DATABASE_CONN_STRING: str = (
        f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}' f'@{POSTGRES_DB}:{POSTGRES_PORT}/{POSTGRES_NAME}'
    )

    class Config:
        env_file = get_env()
        env_file_encoding = 'utf-8'


@lru_cache
def env_settings() -> Settings:
    return Settings()
