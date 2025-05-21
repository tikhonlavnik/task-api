from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from core.database import get_db
from core.exceptions import AppError, NotFoundError

# from src.api.exceptions.task_exceptions import TaskNotFoundError
from src.dto.task import BaseTaskSchema, ResponseTaskSchema, ResponseListTaskSchema
from src.infrastructure.repositories.task_repo import TaskRepository
from src.infrastructure.services.task import TaskService

task_router = APIRouter(prefix="/tasks")


def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    repo = TaskRepository(db)
    return TaskService(repo)


@task_router.post(
    "",
    responses={
        HTTP_400_BAD_REQUEST: {
            "description": "Invalid data",
            "application/json": {
                "example": {
                    "error": "Client error while creating task",
                    "type": "AppError",
                }
            },
        }
    },
)
def create_task(
    body: BaseTaskSchema, service: TaskService = Depends(get_task_service)
) -> ResponseTaskSchema:
    try:
        return service.create_task(body)
    except AppError:
        raise AppError(detail="Client error while creating task")


@task_router.get(
    "/{task_id}",
    responses={
        HTTP_404_NOT_FOUND: {
            "description": "Not found",
            "content": {
                "application/json": {
                    "example": {"error": "Task not found", "type": "TaskNotFoundError"}
                }
            },
        }
    },
)
def get_task_by_id(
    task_id: int, service: TaskService = Depends(get_task_service)
) -> ResponseTaskSchema:
    try:
        return service.get_task(task_id)
    except NotFoundError as e:
        raise e


@task_router.get("")
def get_task_list(
    service: TaskService = Depends(get_task_service),
) -> ResponseListTaskSchema:
    try:
        return service.get_tasks_list()
    except NotFoundError as e:
        raise e
