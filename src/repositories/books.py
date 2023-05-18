from typing import Type

from fastapi import Depends
from sqlalchemy.orm import Session

from src.core.db import get_db_conn
from src.models.books import Book
from src.repositories.repository import AbstractRepository


class BookRepository(AbstractRepository):
    db: Session

    def __init__(self, db: Session = Depends(get_db_conn)) -> None:
        self.db = db

    def list(
        self,
        name: str | None,
        limit: int | None,
        start: int | None,
    ) -> list[Type[Book]]:
        query = self.db.query(Book)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all()

    def get(self, book: Book) -> Type[Book] | None:
        return self.db.get(Book, book.id)

    def create(self, book: Book) -> Book:
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    def update(self, id_s: int, book: Book) -> Book:
        book.id = id_s
        self.db.merge(book)
        self.db.commit()
        return book

    def delete(self, book: Book) -> None:
        self.db.delete(book)
        self.db.commit()
        self.db.flush()
