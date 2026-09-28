# EventHub — Django + Telegram Bot

Portfolio project by **Stefan Golubev**. A small event-management application combining a Django website/admin panel with an asynchronous Telegram bot.

## Tech stack
Python 3.12 · Django 5 · Django ORM · PostgreSQL · aiogram · asyncio/aiohttp · HTML/CSS · Docker · pytest · GitHub Actions

## Implemented
- event and registration relational models;
- Django admin for managing data;
- web page with upcoming events;
- JSON endpoint consumed by the Telegram bot;
- asynchronous Telegram bot commands;
- PostgreSQL in Docker with SQLite fallback for local development;
- Django migrations;
- automated tests and CI.

## Bot commands
- `/start` — introduction;
- `/events` — retrieve events from the Django API.

## Run
```bash
cp .env.example .env
# add your Telegram BOT_TOKEN to .env
docker compose up --build
```

Web: `http://localhost:8000`  
Admin: `http://localhost:8000/admin`

Create an administrator:
```bash
docker compose exec web python manage.py createsuperuser
```

## Tests
```bash
pytest -q
```

## Architecture
```text
Telegram Bot -> Django JSON API -> PostgreSQL
                    |
               Django Admin
```

Real secrets and the local `.env` file are excluded from Git.
