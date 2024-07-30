from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Extra


class BaseSentimentResultSchema(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime


class SentimentResultSchema(BaseSentimentResultSchema):
    prompt: str
    answer: int


class CreateSentimentResultSchema(BaseModel, extra=Extra.allow):
    prompt: str
