from abc import ABC, abstractmethod
from typing import List, Optional

from src.domain.models.task import Task
from src.dto.task import BaseTaskSchema


class ITaskRepository(ABC):
    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        pass

    @abstractmethod
    def get_list(self, params: dict) -> Optional[List[Task]]:
        pass

    @abstractmethod
    def create(self, data: BaseTaskSchema) -> Optional[Task]:
        pass

    @abstractmethod
    def update(self, task_id: int, data: BaseTaskSchema) -> Optional[Task]:
        pass

    @abstractmethod
    def delete(self, task_id: int) -> Optional[Task]:
        pass
