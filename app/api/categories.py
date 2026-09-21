from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.db import get_db
from app.db import crud, models
from app import schemas

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("", response_model=List[schemas.Category])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)

@router.post("", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    db_category = db.query(models.Category).filter(models.Category.title == category.title).first()
    if db_category:
        raise HTTPException(status_code=400, detail="Category already exists")
    return crud.create_category(db, title=category.title)

@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    if not crud.delete_category(db, category_id):
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category and its books deleted successfully"}
@router.put("/{category_id}", response_model=schemas.Category)
def update_category(category_id: int, category_data: schemas.CategoryUpdate, db: Session = Depends(get_db)):
    db_category = crud.update_category(db, category_id=category_id, new_title=category_data.title)
    if not db_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
