from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.settings import settings

engine = create_async_engine(
    settings.db.url,
    future=True,
    echo=settings.db.echo,
)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=True,
    class_=AsyncSession,
)
