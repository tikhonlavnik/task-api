import enum
from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from core.database import Base


class TaskStatus(enum.Enum):
    CREATED: str = "CREATED"
    IN_PROGRESS: str = "IN_PROGRESS"
    CLOSED: str = "CLOSED"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column()
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.CREATED)
    user_id: Mapped[int] = mapped_column(nullable=False)

    # for test app without users table
    # user_id: Mapped[int] = mapped_column(
    #     ForeignKey("users.id"), nullable=False, index=True
    # )
    # user: Mapped["Users"] = relationship(back_populates="tasks")

    # sqlite doesnt support func.now()
    # created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    # updated_at: Mapped[datetime] = mapped_column(
    #     DateTime, server_default=func.now(), onupdate=func.now()
    # )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )

    def __repr__(self) -> str:
        return f"Task(id={self.id}, name={self.name}, status={self.status}, user_id={self.user_id})"

    def to_dict(self):
        return dict((col, getattr(self, col)) for col in self.__table__.columns.keys())
