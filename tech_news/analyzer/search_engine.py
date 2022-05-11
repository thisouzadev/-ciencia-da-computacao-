from tech_news.database import find_news, search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news = find_news()
    news_filtered = [
        (element["title"], element["url"])
        for element in news if title.upper() in element["title"].upper()
    ]
    return news_filtered


# Requisito 7
def search_by_date(date):
    try:
        if datetime.strptime(date, "%Y-%m-%d"):
            result = search_news({"timestamp": {"$regex": date}})
            return [
                (element["title"], element["url"]) for element in result
            ]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
