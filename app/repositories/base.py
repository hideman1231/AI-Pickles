from abc import ABC
from typing import Type, List, Optional, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.generic import GenericRepository, B, BM


class BaseRepository(GenericRepository[B], ABC):

    model: Optional[Type[B]] = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, schema: BM) -> B:
        record = self.model(**dict(schema))
        self.session.add(record)
        await self.session.commit()
        await self.session.refresh(record)

        return record

    async def get(self, **filters: Any) -> Optional[B]:
        query = await self.session.execute(select(self.model).filter_by(**filters))
        return query.scalar_one_or_none()

    async def list(self, **filters: Any) -> List[B]:
        query = await self.session.execute(select(self.model).filter_by(**filters))
        return query.scalars().all()

    async def update(self, record: B, schema: BM) -> B:
        for key, value in dict(schema).items():
            setattr(record, key, value)

        await self.session.commit()
        await self.session.refresh(record)

        return record

    async def delete(self, record: B) -> None:
        await self.session.delete(record)
        await self.session.flush()
