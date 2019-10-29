import requests
r = requests.get("http://python.beispiel.programmierenlernen.io/index.php")

from bs4 import BeautifulSoup

doc = BeautifulSoup(r.text, "html.parser")

for card in doc.select(".card"):
    emoji = card.select_one(".emoji").text
    content = card.select_one(".card-text").text
    title_spans = card.select(".card-title span")
    title = title_spans[1].text
    image = card.select_one("img").attrs["src"]

    print(emoji + " " + title)


