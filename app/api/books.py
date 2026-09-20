from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db import crud, models
from app import schemas

router = APIRouter(prefix="/books", tags=["Books"])

@router.get("", response_model=List[schemas.Book])
def read_books(category_id: Optional[int] = None, db: Session = Depends(get_db)):
    if category_id:
        return db.query(models.Book).filter(models.Book.category_id == category_id).all()
    return crud.get_books(db)

@router.post("", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    if not crud.get_category_by_id(db, book.category_id):
        raise HTTPException(status_code=400, detail="Category not found")
    return crud.create_book(db, title=book.title, price=book.price, category_id=book.category_id, description=book.description, url=book.url)

@router.put("/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book_data: schemas.BookUpdate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, title=book_data.title, price=book_data.price, description=book_data.description)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    if not crud.delete_book(db, book_id):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
