from sqlalchemy import Column, Integer, String

from src.models.base import EntityMeta

# from sqlalchemy.orm import relationship


class Book(EntityMeta):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)

    # PrimaryKeyConstraint(str(id))

    def normalize(self) -> dict[str, str]:
        return {
            'id': self.id.__str__(),
            'name': self.name.__str__(),
        }
