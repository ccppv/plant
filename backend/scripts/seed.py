"""Первоначальное наполнение БД: создание superadmin."""
import asyncio

from sqlalchemy import select

from app.core.config import settings
from app.core.security import get_password_hash
from app.db.session import AsyncSessionLocal
from app.models.user import User, UserRole


async def seed() -> None:
    async with AsyncSessionLocal() as db:
        result = await db.execute(
            select(User).where(User.email == settings.FIRST_SUPERUSER_EMAIL)
        )
        superuser = result.scalar_one_or_none()
        if not superuser:
            superuser = User(
                email=settings.FIRST_SUPERUSER_EMAIL,
                hashed_password=get_password_hash(settings.FIRST_SUPERUSER_PASSWORD),
                full_name="Super Admin",
                role=UserRole.SUPERADMIN,
                is_active=True,
                is_verified=True,
            )
            db.add(superuser)
            await db.commit()
            print(f"[seed] Superuser created: {settings.FIRST_SUPERUSER_EMAIL}")
        else:
            print(f"[seed] Superuser already exists: {settings.FIRST_SUPERUSER_EMAIL}")


if __name__ == "__main__":
    asyncio.run(seed())
