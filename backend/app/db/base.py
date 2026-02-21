from sqlalchemy.orm import DeclarativeBase, MappedColumn, mapped_column
from sqlalchemy import DateTime, func
from datetime import datetime


class Base(DeclarativeBase):
    """Базовый класс для всех моделей.

    Все модели наследуются от этого класса, что позволяет Alembic
    автоматически обнаруживать изменения схемы.
    """
    pass


class TimestampMixin:
    """Миксин с полями created_at / updated_at — добавлять ко всем сущностям."""

    created_at: MappedColumn[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: MappedColumn[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
