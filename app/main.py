from fastapi import FastAPI
from app.db.db import engine, Base
from app.api import categories, books

# Создаем таблицы в БД автоматически при запуске сервера
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Bookstore REST API", version="1.0.0")

# Подключаем роутеры модулей
app.include_router(categories.router)
app.include_router(books.router)

# Шаг 8: Эндпоинт проверки работоспособности
@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "database": "connected"}
