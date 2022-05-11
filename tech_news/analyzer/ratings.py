from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    news = get_collection().aggregate([
        {"$project": {
            "_id": 0,
            "title": 1,
            "url": 1,
            "rank_5": {"$sum": ["shares_count", "comments_count"]},
        }},
        {"$sort": {"rank_5": -1, "title": 1}},
        {"$limit": 5},
    ])
    top_5_news = [
        (top_news["title"], top_news["url"]) for top_news in news
    ]
    return top_5_news


# Requisito 11
def top_5_categories():
    categories = get_collection().aggregate([
        {"$unwind": "$categories"},
        {"$sort": {"categories": 1}},
        {"$limit": 5},
    ])
    top_5_categories = [
        top_categories["categories"] for top_categories in categories
    ]
    return top_5_categories
