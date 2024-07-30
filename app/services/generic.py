from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Optional, List

from pydantic import BaseModel

from app.repositories.generic import GenericRepository

R = TypeVar('R', bound=GenericRepository)
BM = TypeVar('BM', bound=BaseModel)
BRM = TypeVar('BRM', bound=BaseModel)  # base response model


class GenericService(Generic[BRM], ABC):

    @abstractmethod
    async def create(self, schema: BM) -> BRM:
        raise NotImplementedError()

    @abstractmethod
    async def get(self, schema: BM) -> Optional[BRM]:
        raise NotImplementedError()

    @abstractmethod
    async def list(self, schema: BM) -> List[BRM]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, schema: BM) -> BRM:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, schema: BM) -> None:
        raise NotImplementedError()
