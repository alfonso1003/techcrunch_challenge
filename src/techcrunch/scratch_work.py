"""
I am leaving this file to demonstrate that the code can fit on one file and be written procedurally.
"""

import sqlite3

import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get(
    "https://techcrunch.com/wp-json/wp/v2/posts?per_page=100", timeout=5
)
article_json = response.json()

articles = []
for a_j in article_json:
    techcrunch_id = a_j.get("id")
    date_published = pd.to_datetime(a_j.get("date_gmt"))
    title = requests.utils.unquote(a_j.get("title").get("rendered"))
    url = a_j.get("link")
    raw_html_text = a_j.get("content").get("rendered")
    text = BeautifulSoup(raw_html_text, "lxml").text
    articles.append([techcrunch_id, date_published, title, url, text])


df = pd.DataFrame(
    articles, columns=["techcrunch_id", "date_published", "title", "url", "text"]
)
df.index += 1


conn = sqlite3.connect("./db/techcrunch.db")
df.to_sql("articles", conn, if_exists="replace", index_label="id")
conn.close()
