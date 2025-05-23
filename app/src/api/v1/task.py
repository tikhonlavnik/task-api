from fastapi import APIRouter, Depends
from starlette import status

from core.exceptions import AppError
from src.api.dependencies import get_task_service
from src.dto.task import (BaseTaskSchema, ResponseDeleteTaskSchema,
                          ResponseListTaskSchema, ResponseTaskSchema)
from src.infrastructure.services.task import TaskService

task_router = APIRouter(prefix="/tasks")


@task_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    body: BaseTaskSchema, service: TaskService = Depends(get_task_service)
) -> ResponseTaskSchema:
    try:
        return service.create_task(body)
    except AppError as e:
        raise e


@task_router.get(
    "/{task_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {
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
    except AppError as e:
        raise e


@task_router.get(
    "",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Not found",
            "content": {
                "application/json": {
                    "example": {
                        "error": "Tasks list not found",
                        "type": "TaskNotFoundError",
                    }
                }
            },
        }
    },
)
def get_task_list(
    service: TaskService = Depends(get_task_service),
) -> ResponseListTaskSchema:
    try:
        return service.get_tasks_list()
    except AppError as e:
        raise e


@task_router.put(
    "/{task_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Not found",
            "content": {
                "application/json": {
                    "example": {"error": "Task not found", "type": "TaskNotFoundError"}
                }
            },
        }
    },
)
def update_task(
    task_id: int, body: BaseTaskSchema, service: TaskService = Depends(get_task_service)
) -> ResponseTaskSchema:
    try:
        return service.update_task(task_id, body)
    except AppError as e:
        raise e


@task_router.delete(
    "/{task_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "Not found",
            "content": {
                "application/json": {
                    "example": {"error": "Task not found", "type": "TaskNotFoundError"}
                }
            },
        }
    },
)
def delete_task(
    task_id: int, service: TaskService = Depends(get_task_service)
) -> ResponseDeleteTaskSchema:
    try:
        return service.delete_task(task_id)
    except AppError as e:
        raise e
