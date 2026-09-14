from app.db.db import engine, Base, SessionLocal
from app.db import crud

def init():
    # Создаем таблицы в БД, если они еще не созданы
    print("Создание таблиц...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        print("Заполнение базы данных первичными данными...")
        
        # 1. Добавляем две категории
        cat_programming = crud.create_category(db, title="Программирование")
        cat_fiction = crud.create_category(db, title="Художественная литература")
        
        # 2. Добавляем книги к первой категории (Программирование)
        crud.create_book(db, title="Изучаем Python", price=1200.0, category_id=cat_programming.id, description="Классический учебник Марка Лутца")
        crud.create_book(db, title="Чистый код", price=950.0, category_id=cat_programming.id, description="Руководство Роберта Мартина по созданию хорошего кода")
        crud.create_book(db, title="Грокаем алгоритмы", price=800.0, category_id=cat_programming.id, description="Иллюстрированное пособие для программистов")
        
        # 3. Добавляем книги ко второй категории (Художественная литература)
        crud.create_book(db, title="1984", price=450.0, category_id=cat_fiction.id, description="Антиутопия Джорджа Оруэлла")
        crud.create_book(db, title="Преступление и наказание", price=550.0, category_id=cat_fiction.id, description="Классический роман Ф. М. Достоевского")
        crud.create_book(db, title="Мастер и Маргарита", price=600.0, category_id=cat_fiction.id, description="Роман Михаила Булгакова")
        
        print("База данных успешно заполнена книгами и категориями!")
        
    except Exception as e:
        print(f"Ошибка при инициализации БД: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    init()
