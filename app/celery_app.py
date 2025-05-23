from celery import Celery

from config import settings

celery_app = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

celery_app.autodiscover_tasks(["bg_tasks.progress_task"], force=True)

celery_app.conf.task_track_started = True
celery_app.conf.result_extended = True
