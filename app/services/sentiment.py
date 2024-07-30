from typing import Union

from app.repositories.sentiment import SentimentRepository
from app.schemas.sentiment import CreateSentimentResultSchema, SentimentResultSchema
from app.services.base import BaseService
from app.utils import get_sentiment_answer


class SentimentResultService(BaseService[SentimentResultSchema]):

    response_schema = SentimentResultSchema
    repository = SentimentRepository

    async def create(self, schema: CreateSentimentResultSchema) -> SentimentResultSchema:
        schema.answer = get_sentiment_answer(schema.prompt)
        return await super().create(schema)

    async def get(self, schema: CreateSentimentResultSchema) -> Union[SentimentResultSchema]:
        record = await self.repository.get(**dict(schema))

        if not record:
            return await self.create(schema)

        return self.response_schema(**record.__dict__)
