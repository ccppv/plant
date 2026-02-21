.PHONY: help dev prod build test migrate seed lint

# ───────────────────────────────────────────────
help:  ## Показать список команд
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ───────────────────────────────────────────────
dev:  ## Запустить локальное окружение
	docker compose -f docker-compose.dev.yml up --build

dev-down:  ## Остановить локальное окружение
	docker compose -f docker-compose.dev.yml down -v

# ───────────────────────────────────────────────
prod:  ## Запустить production окружение
	docker compose up -d --build

prod-down:  ## Остановить production окружение
	docker compose down

logs:  ## Показать логи всех сервисов
	docker compose logs -f

logs-backend:  ## Логи только backend
	docker compose logs -f backend

# ───────────────────────────────────────────────
migrate:  ## Применить миграции Alembic
	docker compose -f docker-compose.dev.yml exec backend alembic upgrade head

migrate-create:  ## Создать новую миграцию (MSG=...)
	docker compose -f docker-compose.dev.yml exec backend alembic revision --autogenerate -m "$(MSG)"

migrate-down:  ## Откатить последнюю миграцию
	docker compose -f docker-compose.dev.yml exec backend alembic downgrade -1

seed:  ## Запустить seed-скрипт
	docker compose -f docker-compose.dev.yml exec backend python scripts/seed.py

# ───────────────────────────────────────────────
test:  ## Запустить тесты backend
	docker compose -f docker-compose.dev.yml exec backend pytest -v

# ───────────────────────────────────────────────
ssl:  ## Получить SSL-сертификаты (запускать на сервере!)
	docker compose --profile ssl run --rm certbot

# ───────────────────────────────────────────────
install-main:  ## Установить зависимости main frontend
	cd frontend/main && npm install

install-admin:  ## Установить зависимости admin frontend
	cd frontend/admin && npm install

install-tg:  ## Установить зависимости tg frontend
	cd frontend/tg && npm install

install-all: install-main install-admin install-tg  ## Установить все npm зависимости
