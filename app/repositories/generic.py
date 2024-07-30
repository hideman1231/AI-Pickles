from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Optional, List, Any

from pydantic import BaseModel

from app.models import Base

B = TypeVar('B', bound=Base)
BM = TypeVar('BM', bound=BaseModel)


class GenericRepository(Generic[B], ABC):

    @abstractmethod
    async def create(self, schema: BM) -> B:
        raise NotImplementedError()

    @abstractmethod
    async def get(self, **filters: Any) -> Optional[B]:
        raise NotImplementedError()

    @abstractmethod
    async def list(self, **filters: Any) -> List[B]:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, record: B, schema: BM) -> B:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, record: B) -> None:
        raise NotImplementedError()
