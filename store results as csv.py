import csv


with open("challenge crawler_output.csv", "w", newline="") as csvfile:
    articlewriter = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for article in fetch():
        articlewriter.writerow([article.emoji, article.title, article.content, article.image])
