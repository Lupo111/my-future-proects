# Wenn ich den code jetzt sehe, ist er total logisch. Mit der while loop haette ich auch begonnen. Nur so waere ich
# nie drauf gekommen. If & else haette ich auch benutzt, aber wohl niemals auf diese Art. Ich muss noch viel lernen.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
import csv


class CrawledArticle():
    def __init__(self, emoji, title, content, image):
        self.emoji = emoji
        self.title = title
        self.content = content
        self.image = image


class ArticleFetcher():
    @property
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        r = requests.get(url)
        doc = BeautifulSoup(r.text, "html.parser")

        articles = []

        while url != "":
            print(url)
            time.sleep(1)
            r = requests.get(url)
            doc = BeautifulSoup(r.text, "html.parser")

            for card in doc.select(".card"):
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs["src"])

                crawled = CrawledArticle(emoji, title, content, image)
                articles.append(crawled)

            next_button = doc.select_one(".navigation .btn")
            if next_button:
                next_href = next_button.attrs["href"]
                next_href = urljoin(url, next_href)
                url = next_href
                print(url)
            else:
                url = ""

        return articles


fetcher = ArticleFetcher()
article: CrawledArticle
for article in fetcher.fetch:
    print(article.emoji + " : " + article.title)

with open("challenge crawler_output.csv", "w", newline="") as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';',
                             quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for article in fetcher.fetch:
        articlewriter.writerow([article.emoji, article.title, article.content, article.image])



