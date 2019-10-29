import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin


url = "http://python.beispiel.programmierenlernen.io/index.php"
join_url = urljoin(url, "./img/2.jpg")
print(join_url)

class CrawledArticle():
    def __init__(self, emoji, title, content, image):
        self.emoji = emoji
        self.title = title
        self.content = content
        self.image = image

class ArticleFetcher():
     def fetch(self) -> object:
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")

        articles = []

        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title_spans = card.select(".card-title span")
            title = title_spans[1].text
            image = urljoin (url, card.select_one("img").attrs["src"])
            print(image)

            crawled = CrawledArticle(emoji, title, content, image)
            articles.append(crawled)

        return articles

fetcher = ArticleFetcher()
fetcher.fetch()

