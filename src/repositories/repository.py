from abc import abstractmethod
from typing import Generic, TypeVar

M = TypeVar('M')
K = TypeVar('K')


class AbstractRepository(Generic[M, K]):
    @abstractmethod
    def create(self, instance: M) -> M:
        pass

    @abstractmethod
    def list(self, name: str, limit: int, start: int) -> list[M]:
        pass

    @abstractmethod
    def get(self, id_s: K) -> M:
        pass

    @abstractmethod
    def update(self, id_s: K, instance: M) -> M:
        pass

    @abstractmethod
    def delete(self, id_s: K) -> None:
        pass
