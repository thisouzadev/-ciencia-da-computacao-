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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
