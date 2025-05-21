import logging
from abc import ABC
from typing import Optional, List, Type, Union

from sqlalchemy.orm import Session

# from src.api.exceptions.task_exceptions import TaskNotFoundError
from core.exceptions import AppError, NotFoundError
from src.domain.models.task import Task
from src.domain.repositories.base_task_repo import ITaskRepository


logger = logging.Logger(__name__)


class TaskRepository(ITaskRepository, ABC):
    def __init__(self, db: Session):
        self._db = db
        self.model = Task

    def get_by_id(self, task_id: int) -> Type[Task]:
        with self._db as session:
            task = session.query(self.model).filter(self.model.id == task_id).first()
            if not task:
                logger.error(f"Ошибка при получении задачи с {task_id=}")
                raise NotFoundError("Task")
            return task

    def get_list(self, params: dict = None) -> tuple[list[Type[Task]], int]:
        with self._db as session:
            tasks_list = session.query(self.model).all()
            if not params:
                tasks_list = session.query(self.model).filter(**params).all()
            if not tasks_list:
                logger.error(f"Ошибка при получении списка задач")
                raise NotFoundError("Tasks list")
            return tasks_list, 100

    def create(self, data: dict) -> Optional[Task]:
        with self._db as session:
            new_task = self.model(**data)
            session.add(new_task)
            session.commit()
            session.refresh(new_task)
            return new_task

    def update(self, task_id: int, data: dict) -> Optional[Task]:
        pass

    def delete(self, task_id: int) -> Optional[Task]:
        pass
