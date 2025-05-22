from src.dto.task import (
    BaseTaskSchema,
    ResponseTaskSchema,
    ResponseListTaskSchema,
    ResponseDeleteTaskSchema,
)
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
        tasks_list = self.repo.get_list()
        tasks_list = [ResponseTaskSchema(**task.to_dict()) for task in tasks_list]
        return ResponseListTaskSchema(data=tasks_list)

    def update_task(self, task_id: int, data: BaseTaskSchema) -> ResponseTaskSchema:
        task = self.repo.update(task_id, data.model_dump())
        return ResponseTaskSchema(**task.to_dict())

    def delete_task(self, task_id: int) -> ResponseDeleteTaskSchema:
        task_id = self.repo.delete(task_id)
        return ResponseDeleteTaskSchema(id=task_id)
