# Das ist ein Zwischenschritt von 'find elements' zu 'find elements 2'
# NICHT MEHR DARAN RUMFUSCHEN !!

import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")

from bs4 import BeautifulSoup

doc = BeautifulSoup(r.text, "html.parser")


class CrawledArticle():
    def __init__(self, emoji, title, content, image):
        self.emoji = emoji
        self.title = title
        self.content = content
        self.image = image


articles = []

for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text
    title_spans = card.select(".card-title span")
    title = title_spans[1].text
    image = card.select_one("img").attrs["src"]

    crawled = CrawledArticle(emoji, title, content, image)
    articles.append(crawled)

print(articles)

    # Wenn ich diese for loop laufen lasse, werden ale Titel in der Console ausgegeben. "for articel in articles:
#                                                                                        print(article.title)"


