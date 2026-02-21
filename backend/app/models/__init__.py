# Импортируем все модели здесь, чтобы Alembic видел их при генерации миграций
from app.db.base import Base  # noqa: F401
from app.models.user import User  # noqa: F401
