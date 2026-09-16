from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    # Ограничили длину до 100 символов и сделали название уникальным
    title = Column(String(100), nullable=False, unique=True)

    # Пункт 4: Согласовали каскадное удаление на уровне ORM (cascade="all, delete-orphan")
    books = relationship("Book", back_populates="category", cascade="all, delete-orphan")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    # Пункт 2: Заменили Float на Numeric(10, 2) — максимум 10 знаков, 2 знака после запятой
    price = Column(Numeric(10, 2), nullable=False)
    url = Column(String, nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)

    # Связь с категорией
    category = relationship("Category", back_populates="books")
