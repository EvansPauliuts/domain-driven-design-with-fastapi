from pydantic import BaseModel


class BookPostSchema(BaseModel):
    name: str


class BookSchema(BookPostSchema):
    id: int
