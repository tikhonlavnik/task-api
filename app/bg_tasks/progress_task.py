import time

from celery_app import celery_app


@celery_app.task(bind=True)
def long_task(self):
    for i in range(100):
        time.sleep(1)
        self.update_state(state="PROGRESS", meta={"progress": i})
    return {"progress": 100, "status": "Completed"}
