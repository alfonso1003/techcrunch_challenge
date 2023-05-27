import pandas as pd
import requests
from bs4 import BeautifulSoup


class ArticleTransformer:
    def __init__(self, article_data: dict):
        self.article_data = article_data
        self.article_df = None

    def transform_data(self) -> pd.DataFrame:
        articles = []
        for a_d in self.article_data:
            techcrunch_id = a_d.get("id")
            author_id = a_d.get("author")
            date_published = pd.to_datetime(a_d.get("date_gmt"))
            title = requests.utils.unquote(a_d.get("title").get("rendered"))
            url = a_d.get("link")
            raw_html_text = a_d.get("content").get("rendered")
            text = BeautifulSoup(raw_html_text, "lxml").text
            articles.append(
                [techcrunch_id, author_id, date_published, title, url, text]
            )

        article_df = pd.DataFrame(
            articles,
            columns=[
                "techcrunch_id",
                "author_id",
                "date_published",
                "title",
                "url",
                "text",
            ],
        )
        article_df.index += 1
        self.article_df = article_df
        return article_df

    def get_distinct_data_vals(self, column_name: str) -> list:
        return list(self.article_df[column_name].unique())


class AuthorTransformer:
    def __init__(self, author_data: dict):
        self.author_data = author_data
        self.author_df = None

    def transform_data(self) -> pd.DataFrame:
        author_details = []
        for a_d in self.author_data:
            author_id = a_d.get("id")
            name = a_d.get("name")
            url = a_d.get("link")
            author_details.append([author_id, name, url])

        author_df = pd.DataFrame(author_details, columns=["author_id", "name", "url"])
        author_df = author_df.drop_duplicates(subset=["author_id"], keep=False)
        author_df.sort_values(by=["author_id"], ascending=True, inplace=True)
        author_df.reset_index(drop=True, inplace=True)
        author_df.index += 1
        self.author_df = author_df
        return author_df
