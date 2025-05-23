from celery.result import AsyncResult
from fastapi import APIRouter

from bg_tasks.progress_task import long_task

from celery_app import celery_app

progress_router = APIRouter(prefix="/progress")


@progress_router.post("/start")
async def start_task():
    task = long_task.apply_async()
    return {"task_id": task.id}


@progress_router.get("/status/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery_app)
    if task_result.state == "STARTED":
        return {"state": task_result.state, "progress": 0}
    elif task_result.state == "PROGRESS":
        return {
            "state": task_result.state,
            "progress": task_result.info.get("progress", 0),
        }
    elif task_result.state == "SUCCESS":
        return {"state": task_result.state, "result": task_result.result}
    else:
        return {"state": task_result.state, "error": str(task_result.info)}
