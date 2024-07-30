from fastapi import FastAPI

from app.api.v1.sentiment import router as sentiment_router
from app.db import engine
from app.models import Base
from app.settings import settings

app = FastAPI(
    debug=settings.debug,
    title=settings.title,
)

if settings.db.init_tables:
    @app.on_event("startup")
    async def init_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


app.include_router(sentiment_router)
