from tech_news.database import search_news
from datetime import datetime


# Miguel Dantas me explicou um jeito mais simples de fazer
def regex(text):
    return {"$regex": text, "$options": "i"}


def extract_attr(notice):
    return (notice["title"], notice["url"])


# Requisito 6
def search_by_title(title):
    news = search_news({"title": regex(title)})
    results = map(extract_attr, news)

    return list(results)


# Requisito 7
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        news = search_news({"timestamp": regex(date)})
        results = map(extract_attr, news)

        return list(results)

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_source(source):
    news = search_news({"sources": regex(source)})
    results = map(extract_attr, news)

    return list(results)


# Requisito 9
def search_by_category(category):
    news = search_news({"categories": regex(category)})
    results = map(extract_attr, news)

    return list(results)
