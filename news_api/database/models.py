from typing import Any

from sqlalchemy import BigInteger, Column, Date, DateTime, String
from sqlalchemy.sql import func

from . import Base


class News(Base):
    __tablename__ = 'news'
    id = Column(BigInteger, primary_key=True)
    title = Column(String)
    picture_url = Column(String, nullable=True)
    publication_date = Column(Date)
    parsing_date = Column(DateTime, server_default=func.now())

    def __eq__(self, other: Any) -> bool:
        return all(
            (self.title == other.title, self.picture_url == other.picture_url,
             self.publication_date == other.publication_date)
        )

    def __hash__(self):
        return hash(('title', self.title,
                    'publication_date', self.publication_date))
