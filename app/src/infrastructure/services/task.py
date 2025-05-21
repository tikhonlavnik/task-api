from core.exceptions import AppError
from src.dto.task import BaseTaskSchema, ResponseTaskSchema, ResponseListTaskSchema
from src.infrastructure.repositories.task_repo import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, body: BaseTaskSchema) -> ResponseTaskSchema:
        task = self.repo.create(body.model_dump())
        return ResponseTaskSchema(**task.to_dict())

    def get_task(self, task_id: int) -> ResponseTaskSchema:
        task = self.repo.get_by_id(task_id)
        return ResponseTaskSchema(**task.to_dict())

    def get_tasks_list(self) -> ResponseListTaskSchema:
        tasks_list, count = self.repo.get_list()
        return ResponseListTaskSchema(tasks_list=tasks_list, count=count)
