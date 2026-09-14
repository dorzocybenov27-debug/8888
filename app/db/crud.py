from sqlalchemy.orm import Session
from app.db import models

# ==================== CRUD ДЛЯ КАТЕГОРИЙ ====================

def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    return db.query(models.Category).all()

def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def update_category(db: Session, category_id: int, new_title: str):
    db_category = get_category_by_id(db, category_id)
    if db_category:
        db_category.title = new_title
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = get_category_by_id(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False


# ==================== CRUD ДЛЯ КНИГ ====================

def create_book(db: Session, title: str, price: float, category_id: int, description: str = None, url: str = None):
    db_book = models.Book(
        title=title, 
        price=price, 
        category_id=category_id, 
        description=description, 
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, title: str = None, price: float = None, description: str = None):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        if title: db_book.title = title
        if price is not None: db_book.price = price
        if description: db_book.description = description
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False
