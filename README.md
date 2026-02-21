# Plant Tracker

Веб-приложение для отслеживания растений.  

---

## Быстрый старт (локально)

```bash
cp .env.example .env   
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
