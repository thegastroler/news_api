from fastapi import APIRouter, FastAPI
from fastapi_utils.tasks import repeat_every
from loguru import logger

from api import router
from app.news_parser import NewsParser
from database import Session, engine, models
from database.news_storage import NewsStorage

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

main_router = APIRouter()
main_router.include_router(router)
app.include_router(main_router)


@app.on_event('startup')
@repeat_every(seconds=10*60)
def parse_news():
    logger.info('Event started')
    data = None
    parser = NewsParser()
    text = parser.get_news()
    if text:
        data = parser.parse_data(text)
        NewsStorage(Session).add_news(data)
    logger.info('Event finished')
