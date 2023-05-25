from fastapi import APIRouter, Depends, status

from src.schemas.books import BookPostSchema, BookSchema
from src.services.books import BookService

router = APIRouter(
    prefix='/books',
    tags=['book'],
)


@router.get('/', response_model=list[BookSchema], status_code=status.HTTP_200_OK)
def list_book(
    name: str | None = None,
    page_size: int | None = 100,
    start_index: int | None = 0,
    book_service: BookService = Depends(),
):
    return [book.normalize() for book in book_service.list(name, page_size, start_index)]


@router.post('/', response_model=BookSchema, status_code=status.HTTP_201_CREATED)
def create(
    book: BookPostSchema,
    book_service: BookService = Depends(),
):
    return book_service.create(book=book).normalize()


@router.get('/{book_id}')
def retrieve_book(book_id: int, book_service: BookService = Depends()):
    return book_service.get(book_id=book_id)


@router.patch('/{book_id}', response_model=BookSchema)
def retrieve_update_book(
    book_id: int,
    book: BookPostSchema,
    book_service: BookService = Depends(),
):
    return book_service.update(book_id=book_id, book=book).normalize()


@router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int,
    book_service: BookService = Depends(),
):
    return book_service.delete(book_id=book_id)
