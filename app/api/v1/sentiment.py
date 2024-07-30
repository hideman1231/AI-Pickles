from typing import List

from fastapi import APIRouter, Depends, Form
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependenses import get_session
from app.schemas.sentiment import SentimentResultSchema, CreateSentimentResultSchema
from app.services.sentiment import SentimentResultService
from app.settings import settings

router = APIRouter(
    prefix=settings.api.api_v1,
    tags=['sentiment']
)


templates = Jinja2Templates(directory='app/templates')


# use for API
# @router.post('/sentiment/', status_code=200, response_model=SentimentResultSchema)
# async def get_or_create_sentiment(
#     data: CreateSentimentResultSchema,
#     session: AsyncSession = Depends(get_session),
# ):
#     return await SentimentResultService(session).get(data)


@router.post('/sentiment/', status_code=200)
async def get_or_create_sentiment(
    request: Request,
    prompt: str = Form(...),
    session: AsyncSession = Depends(get_session),
):
    schema = CreateSentimentResultSchema(prompt=prompt)
    data = await SentimentResultService(session).get(schema)
    return templates.TemplateResponse(name='success.html', context={'request': request, 'answer': data.answer})


@router.get('/sentiment/', status_code=200, response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(name='home.html', context={'request': request})
