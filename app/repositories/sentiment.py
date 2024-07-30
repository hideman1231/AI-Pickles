from app.models.sentiment import SentimentResult
from app.repositories.base import BaseRepository


class SentimentRepository(BaseRepository[SentimentResult]):

    model = SentimentResult
