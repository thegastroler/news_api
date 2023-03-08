# **NEWS API**
API сервис для получения новостей с сайта http://mosday.ru/news/tags.php?metro. Проект написан на python 3.9.

Стек: FastApi, PostgreSQL, docker-compose, SQLAlchemy, beautifulsoup4, poetry

### **API методы**:
- Метод показа новостей, опубликованных за период {n} дней (включительно)
(GET запрос на http://localhost:8000/metro/news/?day={n}).

*Пример ответа*:
```
[
    {
        "parsing_date": "2023-03-08T00:03:48.588652",
        "title": "На станциях БКЛ появились стикеры для потерявшихся детей",
        "picture_url": "https://mosday.ru/news/preview/415/4157645.jpg",
        "publication_date": "2023-03-07",
        "id": 27
    },
    {
        "parsing_date": "2023-03-08T00:03:48.588652",
        "title": "Экономим время. Открытие БКЛ сокращает путь в разы",
        "picture_url": "https://mosday.ru/news/preview/415/4157712.jpg",
        "publication_date": "2023-03-07",
        "id": 26
    }
]
```


### **Загрузка новостей**.
Новости загружаются в базу данных при помощи парсера, который автоматически парсит каждые 10 минут новости с сайта http://mosday.ru/news/tags.php?metro.

_Встроенная документация FastAPI_: http://localhost:8000/docs#/


## **Запуск проекта**.
Склонировать проект:
```
git pull https://github.com/thegastroler/news_api
```
В корневой папке проекта:
```
docker-compose up -d --build
```
Проект готов к работе.

Для просмотра БД переходим в админ-панель pgAdmin 
http://localhost:5050/
```
login: admin@admin.com
password: admin
```

Далее подключаемся к БД:
```
Object -> Register -> Server...
name: news_api
```
Во вкладке **Connection**:
```
Host name: db
Port: 5432
Maintenance database: postgres
Username: postgres
Password: postgres
```
Просмотр таблицы по пути:
```
news_api -> Databases -> postgres -> Schemas -> public -> Tables
```

