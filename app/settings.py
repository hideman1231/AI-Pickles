from pydantic import BaseSettings, BaseModel


class APISettings(BaseModel):
    api_v1 = '/api/v1'


class PostgreSQLSettings(BaseModel):
    url: str = 'postgresql+asyncpg://postgres:postgres@db/postgres'
    echo: bool = True

    init_tables: bool = True


class Settings(BaseSettings):
    debug: bool = True
    title: str = 'AI Pickles'

    db: PostgreSQLSettings = PostgreSQLSettings()

    api: APISettings = APISettings()


settings = Settings()
