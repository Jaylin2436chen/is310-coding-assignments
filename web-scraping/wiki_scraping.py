import requests
from bs4 import BeautifulSoup
import csv
import time

HEADERS = {"User-Agent": "is310-course-scraper/1.0 (student project; Jaylinc2@illinois.edu)"}
pages = [
    ("series", "Harry Potter film series",
     "https://en.wikipedia.org/wiki/Harry_Potter_(film_series)"),
    ("film", "Philosopher's Stone",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Philosopher%27s_Stone_(film)"),
    ("film", "Chamber of Secrets",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Chamber_of_Secrets_(film)"),
    ("film", "Prisoner of Azkaban",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Prisoner_of_Azkaban_(film)"),
    ("film", "Goblet of Fire",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Goblet_of_Fire_(film)"),
    ("film", "Order of the Phoenix",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Order_of_the_Phoenix_(film)"),
    ("film", "Half-Blood Prince",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Half-Blood_Prince_(film)"),
    ("film", "Deathly Hallows Part 1",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1"),
    ("film", "Deathly Hallows Part 2",
     "https://en.wikipedia.org/wiki/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2")
]

rows = []

for page_type, name, url in pages:
    response = requests.get(url, headers=HEADERS, timeout=10)
    time.sleep(1)

    if response.status_code != 200:
        print("Skipping:", name, response.status_code)
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find(id = "mw-content-text")

    if content is None:
        print("Can't find article for:", name)
        continue

    article_text = content.get_text(" ", strip=True)
    word_count = len(article_text.split())

    link_count = 0
    for link in content.find_all("a", href=True):
        href = link["href"]
        if (href.startswith("/wiki/") or href.startswith("https://en.wikipedia.org/wiki/")
    ) and "#" not in href:
            link_count += 1

    rows.append([page_type, name, url, word_count, link_count])
    print("Collected:", name)

with open("harry_potter_films.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["page_type", "name", "url", "word_count", "internal_link_count"])
    writer.writerows(rows)
print("Saved", len(rows), "pages to harry_potter_films.csv")
