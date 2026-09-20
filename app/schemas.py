from pydantic import BaseModel, Field
from decimal import Decimal
from typing import Optional

# ==================== СХЕМЫ КАТЕГОРИЙ ====================
class CategoryBase(BaseModel):
    title: str = Field(..., max_length=100)

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

# ==================== СХЕМЫ КНИГ ====================
class BookBase(BaseModel):
    title: str = Field(..., max_length=255)
    description: Optional[str] = None
    price: Decimal = Field(..., max_digits=10, decimal_places=2)
    url: Optional[str] = None
    category_id: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    price: Optional[Decimal] = Field(None, max_digits=10, decimal_places=2)
    url: Optional[str] = None
    category_id: Optional[int] = None

class Book(BookBase):
    id: int

    class Config:
        from_attributes = True
