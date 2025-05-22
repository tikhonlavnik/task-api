from fastapi import Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import JSONResponse

from core.database import get_db
from core.exceptions import AppError
from src.infrastructure.repositories.task_repo import TaskRepository
from src.infrastructure.services.task import TaskService


async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "type": exc.__class__.__name__},
    )


err_handlers = {
    AppError: app_error_handler,
    # other errs
}


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    repo = TaskRepository(db)
    return TaskService(repo)
