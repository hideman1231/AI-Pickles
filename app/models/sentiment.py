import uuid

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

from app.models.date_mixin import DateMixinBase


class SentimentResult(DateMixinBase):
    __tablename__ = 'sentiment_results'

    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prompt = sa.Column(sa.String)
    answer = sa.Column(sa.Integer)

    def __str__(self):
        return self.prompt


