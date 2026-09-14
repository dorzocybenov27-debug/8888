from app.db.db import SessionLocal
from app.db import crud

def main():
    db = SessionLocal()
    try:
        print("=== ПОЛУЧЕНИЕ ДАННЫХ ИЗ БАЗЫ ДАННЫХ ===\n")
        
        # Читаем все категории
        categories = crud.get_categories(db)
        
        for category in categories:
            print(f"Категория: {category.title} (ID: {category.id})")
            print("-" * 40)
            
            # Фильтруем книги, которые относятся к этой категории
            for book in category.books:
                print(f"  • Книга: \"{book.title}\"")
                print(f"    Цена: {book.price} руб.")
                print(f"    Описание: {book.description}")
                print()
                
    except Exception as e:
        print(f"Ошибка при чтении данных: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()
