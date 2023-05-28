import sqlite3

import pandas as pd

conn: sqlite3.Connection = sqlite3.connect("./src/techcrunch/db/techcrunch.db")

query: str = (
    "SELECT * FROM articles JOIN authors ON articles.author_id = authors.author_id"
)
df: pd.DataFrame = pd.read_sql(query, conn, parse_dates="date_published")

print(df.head())
print(df.info())

conn.close()
