# EventHub — Django + Telegram Bot

Portfolio project by **Stefan Golubev**. Event platform with Django, PostgreSQL and an asynchronous Telegram bot.

## Stack
Python 3.12, Django 5, Django ORM, PostgreSQL, aiogram 3, asyncio/aiohttp, HTML/CSS, Docker, pytest.

## Run
```bash
cp .env.example .env
docker compose up --build
```

Create admin: `docker compose exec web python manage.py createsuperuser`.

Bot commands: `/start`, `/events`.
