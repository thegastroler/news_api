from datetime import date, timedelta
from typing import List, Optional

from loguru import logger

from database import Session

from .models import News


class NewsStorage:
    def __init__(self, session: Session):
        self.session = session

    def add_news(self, data: List[Optional[News]]):
        try:
            with self.session() as session:
                obj = session.query(News).order_by(News.id.desc()).first()
                if obj:
                    objs = []
                    for i in data:
                        if i != obj:
                            objs.append(i)
                        else:
                            break
                    data = objs
                if data:
                    session.add_all(data[::-1])
                    session.commit()
                    session.expire_all()
                    logger.info(f'Inserted {len(data)} rows')
                else:
                    logger.info('No new data')
        except Exception as e:
            logger.error(e)

    def get_news(self, day: int) -> Optional[List[News]]:
        date_delta = date.today() - timedelta(days=day-1)
        try:
            with self.session() as session:
                objs = session.query(News).where(
                    News.publication_date >= date_delta).all()
                return objs
        except Exception as e:
            logger.error(e)
