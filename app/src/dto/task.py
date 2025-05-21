from datetime import datetime
from typing import Optional, List, Type

from pydantic import BaseModel

from src.domain.models.task import TaskStatus


class BaseTaskSchema(BaseModel):
    name: str
    description: Optional[str]
    status: TaskStatus
    user_id: int


class ResponseTaskSchema(BaseTaskSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class ResponseListTaskSchema(BaseModel):
    data: List[Type[ResponseTaskSchema]]
    count: int
