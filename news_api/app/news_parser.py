from datetime import datetime
from typing import List, Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from database.models import News
from loguru import logger


class NewsParser:
    URL = 'https://mosday.ru/news/tags.php?metro'

    def get_news(self) -> Optional[str]:
        response = requests.get(self.URL)
        if response.status_code == 200:
            logger.info('Data recieved')
            return response.text
        else:
            logger.error(f'Response code {response.status_code}')
            return None

    def parse_data(self, text: str) -> Optional[List[News]]:
        objs = []
        try:
            soup = BeautifulSoup(text, 'html.parser')
            items = soup.find_all('table', {
                'style': 'font-family:Arial;font-size:15px',
                'width': '95%',
                'cellpadding': '0'
            })
            items = [i.find_all('tr') for i in items]
            items = [
                k for i in items for k in i if k.find('td', {'valign': 'top'})
            ]
            for i in items:
                data = [k.text for k in i.find_all('b')]
                title = data[-1]
                publication_date = datetime.strptime(
                    data[0], '%d.%m.%Y').date()
                if i.find('img'):
                    picture_url = urljoin(self.URL, i.find('img').get('src'))
                else:
                    picture_url = None
                obj = News(
                    title=title,
                    picture_url=picture_url,
                    publication_date=publication_date
                )
                objs.append(obj)
            logger.info('Data parsed')
            return objs
        except Exception as e:
            logger.error(e)
