import logging
from abc import ABC
from typing import List

from sqlalchemy import delete, select
from sqlalchemy.orm import Session

from core.exceptions import NotFoundError
from src.domain.models.task import Task
from src.domain.repositories.base_task_repo import ITaskRepository

logger = logging.Logger(__name__)


class TaskRepository(ITaskRepository, ABC):
    def __init__(self, db: Session):
        self._db = db
        self.model = Task

    def get_by_id(self, task_id: int) -> Task:
        with self._db as session:
            task = session.get(self.model, task_id)

            if not task:
                logger.error(f"Ошибка при получении задачи с {task_id=}")
                raise NotFoundError("Task")
            return task

    def get_list(self, params: dict = None) -> List[Task]:
        with self._db as session:
            query = select(self.model)

            if params:
                query = query.filter_by(**params)

            tasks_list = session.scalars(query).all()

            if not tasks_list:
                logger.error("Ошибка при получении списка задач")
                raise NotFoundError("Tasks list")

            return tasks_list

    def create(self, data: dict) -> Task:
        with self._db as session:
            new_task = self.model(**data)
            session.add(new_task)
            session.commit()
            session.refresh(new_task)
            return new_task

    def update(self, task_id: int, data: dict) -> Task:
        with self._db as session:
            task = session.get(self.model, task_id)
            if not task:
                raise NotFoundError("Task while updating")

            for key, value in data.items():
                setattr(task, key, value)

            session.commit()
            session.refresh(task)
            return task

    def delete(self, task_id: int) -> int:
        with self._db as session:
            if not session.get(self.model, task_id):
                raise NotFoundError("Task while deleting")

            session.execute(
                delete(Task).filter_by(id=task_id).returning(Task)
            ).scalar_one()
            session.commit()
            return task_id
