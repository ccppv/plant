from fastapi import APIRouter
from sqlalchemy import text

from app.core.config import settings
from app.db.redis import redis_client
from app.db.session import AsyncSessionLocal
from app.schemas.health import HealthCheck

router = APIRouter()


@router.get("", response_model=HealthCheck, summary="Проверка состояния сервисов")
async def health_check() -> HealthCheck:
    # Проверка PostgreSQL
    db_status = "ok"
    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
    except Exception as e:
        db_status = f"error: {e}"

    # Проверка Redis
    redis_status = "ok"
    try:
        await redis_client.ping()
    except Exception as e:
        redis_status = f"error: {e}"

    return HealthCheck(
        status="ok" if db_status == "ok" and redis_status == "ok" else "degraded",
        version=settings.API_VERSION,
        environment=settings.ENVIRONMENT,
        db=db_status,
        redis=redis_status,
    )
