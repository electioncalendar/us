from secrets import token_urlsafe
from typing import Any, Dict, Optional

from pydantic import BaseSettings, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    PROJECT_NAME: str = "electioncal"
    API_V1_STR: str = "/v1"
    SECRET_KEY: str = token_urlsafe(32)
    BASE_URL: str

    SENTRY_DSN: Optional[HttpUrl] = None

    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any],) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOST"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    TWILIO_SID: Optional[str]
    TWILIO_AUTH_TOKEN: Optional[str]
    TWILIO_SECRET: Optional[str]

    SUPERUSER_EMAIL: str
    SUPERUSER_PASSWORD: str


settings = Settings()

__all__ = (settings,)
