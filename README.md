# 🌿 Plant Tracker

Production-ready веб-приложение для отслеживания растений.  
Три поддомена, одна база, единая система пользователей.

---

## Архитектура

```
Internet
    │
    ▼
 Nginx (80/443)  ← единая точка входа, SSL termination
    │
    ├─► plant-tracker.ru       → frontend-main  (Next.js  :3000)
    ├─► admin.plant-tracker.ru → frontend-admin (Vite SPA :80)
    ├─► tg.plant-tracker.ru    → frontend-tg    (Vite SPA :80)
    └─► */api/*                → backend        (FastAPI  :8000)
                                      │
                          ┌───────────┴───────────┐
                          ▼                       ▼
                    PostgreSQL 17            Redis 7
                   (единая БД)        (кэш / сессии / очереди)
```

### Почему такой стек?

| Выбор | Обоснование |
|---|---|
| **FastAPI** | async-нативный, автодокументация, Pydantic v2, легко тестировать |
| **Next.js** для main | SSR + SEO (каталог растений должен индексироваться) |
| **Vite + React** для admin/tg | SPA без SSR — быстрее билдится, легче деплоится |
| **PostgreSQL** | JSONB, полнотекстовый поиск, надёжные транзакции |
| **Redis** | Кэш, JWT-blacklist, rate-limiting, фоновые задачи |
| **Alembic** | Версионирование схемы, autogenerate из моделей |
| **Nginx** | Reverse proxy, SSL termination, gzip |
| **Docker** | Воспроизводимость, изоляция, CI/CD-friendly |

---

## Быстрый старт (локально)

```bash
cp .env.example .env   # заполнить секреты
make dev               # docker compose dev с hot reload
make migrate           # применить Alembic миграции
make seed              # создать superadmin
```

Адреса после запуска:
- API + Swagger: http://localhost:8000/api/v1/docs
- Frontend main: http://localhost:3000
- Frontend admin: http://localhost:3001
- Frontend tg:   http://localhost:3002

---

## Production деплой

```bash
cp .env.example .env && vim .env
make ssl    # Certbot (webroot)
make prod
make logs
```

---

## API

| Метод | Путь | Описание | Auth |
|---|---|---|---|
| GET | `/api/v1/health` | Healthcheck | — |
| POST | `/api/v1/auth/register` | Регистрация | — |
| POST | `/api/v1/auth/login` | JWT | — |
| POST | `/api/v1/auth/refresh` | Refresh token | — |
| GET | `/api/v1/auth/me` | Текущий пользователь | Bearer |
| GET | `/api/v1/users` | Список (admin only) | Admin |
| PATCH | `/api/v1/users/me` | Обновить профиль | Bearer |

---

## Роли: `user` · `admin` · `superadmin`

Superadmin создаётся автоматически через `make seed`.

---

## Roadmap

- [ ] Celery / ARQ — напоминания о поливе
- [ ] S3 — хранение фото растений
- [ ] Telegram Bot (aiogram)
- [ ] Rate limiting (slowapi + Redis)
- [ ] CI/CD: GitHub Actions → Docker Hub
- [ ] Observability: Prometheus + Grafana + Loki
