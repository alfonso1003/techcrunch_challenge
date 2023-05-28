import sqlite3


def main():
    conn = sqlite3.connect("./src/techcrunch/db/techcrunch.db")
    cursor = conn.cursor()

    drop_articles_if_exists = "DROP TABLE IF EXISTS articles"
    create_articles = """CREATE TABLE articles (
                            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            techcrunch_id   INTEGER,
                            author_id  TEXT,
                            date_published  DATE,
                            title   TEXT,
                            url TEXT,
                            text    TEXT);"""

    drop_authors_if_exists = "DROP TABLE IF EXISTS authors"
    create_authors = """CREATE TABLE authors (
                            id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,
                            name TEXT, 
                            url TEXT,
                            author_id INTEGER NOT NULL,
                            FOREIGN KEY (author_id) REFERENCES articles (id));"""

    cursor.execute(drop_articles_if_exists)
    cursor.execute(create_articles)

    cursor.execute(drop_authors_if_exists)
    cursor.execute(create_authors)
    conn.commit()


if __name__ == "__main__":
    main()
