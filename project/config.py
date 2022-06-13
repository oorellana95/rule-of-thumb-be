"""AppSettings config."""
from functools import lru_cache
from pydantic import BaseSettings


class AppSettings(BaseSettings):
    # General
    APP_NAME: str = "Rules of Thumb API"

    # Cors Origins
    DOMAIN_FRONTEND: str = "http://localhost:8080"

    # Database
    DATABASE_DIALECT: str = "mysql+pymysql"
    DATABASE_HOST: str = "127.0.0.1"
    DATABASE_PORT: int = 3306
    DATABASE_USER: str = "master"
    DATABASE_PASSWORD: str = "master_pass"
    DATABASE_NAME: str = "rule_of_thumb_mysql"

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return AppSettings()
