"""Стартовый скрипт: ждёт БД + Redis, запускает миграции, seed и сервер."""
import asyncio
import subprocess
import sys
import time

import asyncpg
import redis.asyncio as aioredis

from app.core.config import settings


async def wait_for_postgres(retries: int = 20, delay: float = 2.0) -> None:
    for attempt in range(retries):
        try:
            conn = await asyncpg.connect(settings.DATABASE_URL.replace("+asyncpg", ""))
            await conn.close()
            print("[prestart] PostgreSQL — ready")
            return
        except Exception:
            print(f"[prestart] Waiting for PostgreSQL ({attempt + 1}/{retries})...")
            await asyncio.sleep(delay)
    sys.exit("[prestart] PostgreSQL not available — aborting")


async def wait_for_redis(retries: int = 20, delay: float = 1.0) -> None:
    client = aioredis.from_url(settings.REDIS_URL)
    for attempt in range(retries):
        try:
            await client.ping()
            await client.aclose()
            print("[prestart] Redis — ready")
            return
        except Exception:
            print(f"[prestart] Waiting for Redis ({attempt + 1}/{retries})...")
            await asyncio.sleep(delay)
    sys.exit("[prestart] Redis not available — aborting")


async def main() -> None:
    await asyncio.gather(wait_for_postgres(), wait_for_redis())
    subprocess.run(["alembic", "upgrade", "head"], check=True)
    subprocess.run(["python", "scripts/seed.py"], check=True)


if __name__ == "__main__":
    asyncio.run(main())
