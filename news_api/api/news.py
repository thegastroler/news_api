from datetime import date
from typing import Optional

from database import Session
from database.news_storage import NewsStorage
from fastapi import APIRouter, Query
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter(prefix="/metro")


class News(BaseModel):
    id: int
    title: str
    picture_url: Optional[str]
    publication_date: date


@router.get('/news/')
def get_news(day: int = Query(gt=0)) -> JSONResponse:
    data = NewsStorage(Session).get_news(day)
    json_data = jsonable_encoder(data)
    return JSONResponse(content=json_data)
