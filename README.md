# Bookstore REST API (octagon-example)

Проект представляет собой REST API для управления книжным магазином (книги и категории) с использованием FastAPI, SQLAlchemy и PostgreSQL.

## Переменные окружения (.env)
Для работы проекта создайте в корневой директории файл `.env` и укажите в нём настройки подключения к PostgreSQL:
```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345
```

## Как развернуть проект локально

1. Склонируйте репозиторий и перейдите в папку проекта.
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Установите необходимые зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Задайте переменную путей Python:
   ```bash
   export PYTHONPATH=.
   ```
5. Заполните базу данных первичными данными (опционально):
   ```bash
   python app/init_db.py
   ```
6. Запустите веб-сервер API:
   ```bash
   uvicorn app.main:app --reload
   ```

После запуска интерактивная документация со всеми CRUD-методами доступна по адресу: http://127.0.0
