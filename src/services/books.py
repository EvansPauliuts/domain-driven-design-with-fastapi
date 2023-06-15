from typing import Type

from fastapi import Depends

from src.models.books import Book
from src.repositories.books import BookRepository
from src.schemas.books import BookSchema


class BookService:
    book_repository: BookRepository

    def __init__(self, book_repo: BookRepository = Depends()) -> None:
        self.book_repository = book_repo

    def list(
        self,
        name: str | None = None,
        page_size: int | None = 100,
        start_index: int | None = 0,
    ) -> list[Type[Book]]:
        return self.book_repository.list(
            name,
            page_size,
            start_index,
        )

    def create(
        self,
        book: BookSchema,
    ) -> Book:
        return self.book_repository.create(Book(name=book.name))

    def get(self, book_id: int) -> Type[Book] | None:
        return self.book_repository.get(Book(id=book_id))

    def update(self, book_id: int, book: BookSchema) -> Book:
        return self.book_repository.update(
            book_id,
            Book(name=book.name),
        )

    def delete(self, book_id: int) -> None:
        return self.book_repository.delete(Book(id=book_id))
