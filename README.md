# FastAPI + Celery + Redis CRUD Task Manager

### Простое приложение на FastAPI, предоставляющее CRUD API для To-Do List и асинхронную обработку с помощью Celery и Redis.

## Функционал

- REST API для создания, получения и управления задачами
- Асинхронная длительная задача через Celery
- Отслеживание прогресса выполнения задачи
- Использование SQLite для хранения данных
- Redis как брокер сообщений и backend для результатов Celery

## Технологии

- FastAPI
- Celery
- Redis
- SQLAlchemy
- Docker + Docker Compose]

## Установка и запуск

### 1. Через Docker Compose

Запуск всего приложения одной командой:

```bash
docker-compose up --build
```

### 2. Локальный запуск

```bash
docker run --name redis -p 6379:6379 redis:latest
pip install -r requirements.txt
cd /app
python main.py
celery -A celery_app.celery_app worker --loglevel=info
```


## Функционал

### Swagger-документация после запуска доступна по адресу:
### http://localhost:5000/docs
