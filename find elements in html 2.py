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

class ArticleFetcher():
    def fetch(self):
        r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")
        doc = BeautifulSoup(r.text, "html.parser")

        articles = []

        for card in doc.select(".card"):
            emoji = card.select_one(".emoji").text
            content = card.select_one(".card-text").text
            title = card.select(".card-title span")[1].text
            image = card.select_one("img").attrs["src"]
            crawled = CrawledArticle(emoji, title, content, image)
            articles.append(crawled)

        return articles


fetcher = ArticleFetcher()
fetcher.fetch()
