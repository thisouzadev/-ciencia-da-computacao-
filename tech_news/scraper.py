import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url, timeout=1):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


html = fetch("https://www.tecmundo.com.br/novidades")
# print(html)


# Requisito 2
# https://www.tecmundo.com.br/novidades
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    url = selector.css(".tec--card .tec--card__info h3 a::attr(href)").getall()
    return url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next = selector.css("div.tec--list a.tec--btn::attr(href)").get()
    if next:
        return next
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    news = {
        'url': '',
        'title': '',
        'timestamp': '',
        'writer': None,
        'shares_count': '',
        'comments_count': '',
        'summary': '',
        'sources': [],
        'categories': []
    }

    selector = Selector(text=html_content)
    news["url"] = selector.css(
        "head link[rel='canonical']::attr(href)"
    ).get()

    news['title'] = selector.css(
        "main h1#js-article-title::text"
    ).get()

    news['timestamp'] = selector.css(
        "div.tec--timestamp time::attr(datetime)"
    ).get()

    writer = selector.css(
        ".z--font-bold *::text"
    ).get()

    if(writer is not None and writer != ''):
        formated_writer = writer
        if writer[0] == " " and writer[-1] == " ":
            formated_writer = writer[1:-1]
        news['writer'] = formated_writer

    shares = selector.css(
        "nav.tec--toolbar div.tec--toolbar__item::text"
    ).get()
    if(shares):
        news['shares_count'] = int(shares.strip("Compartilharam"))
    else:
        news['shares_count'] = 0

    comments = selector.css(
        "#js-comments-btn::attr(data-count)"
    ).get()
    if(comments):
        news['comments_count'] = int(comments.strip())
    else:
        news['comments_count'] = 0

    news['summary'] = "".join(selector.css(
        "div.tec--article__body > p:first-child *::text"
    ).getall())

    news['sources'] = [
        source.strip()
        for source
        in selector.css(
            "div.z--mb-16 div a::text"
        ).getall()
    ]
    news['categories'] = [
        category.strip()
        for category
        in selector.css(
            "#js-categories a::text"
        ).getall()
    ]
    return news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
