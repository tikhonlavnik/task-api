from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND", REDIS_URL)
    SQL_URL: str = os.getenv("SQL_URL")


settings = Settings()
