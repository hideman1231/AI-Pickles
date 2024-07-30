from typing import Optional, List, Type, Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.base import BaseRepository
from app.services.generic import GenericService, BM, BRM


class BaseService(GenericService[BRM]):

    response_schema: Type[BRM] = None
    repository: Union[Type[BaseRepository], BaseRepository] = None

    def __init__(self, session: AsyncSession) -> None:
        self.repository = self.repository(session)

    async def create(self, schema: BM) -> BRM:
        record = await self.repository.create(schema)
        return self.response_schema(**record.__dict__)

    async def get(self, schema: BM) -> Optional[BRM]:
        record = await self.repository.get(**dict(schema))
        return self.response_schema(**record.__dict__)

    async def list(self, schema: Union[BM] = None) -> List[BRM]:
        schema = schema or {}
        query = await self.repository.list(**dict(schema))
        return [self.response_schema(**record.__dict__) for record in query]

    async def update(self, schema: BM) -> BRM:
        record = await self.repository.get(**dict(schema))
        record = await self.repository.update(record, schema)
        return self.response_schema(**record.__dict__)

    async def delete(self, schema: BM) -> None:
        record = await self.repository.get(**dict(schema))
        return await self.repository.delete(record)
