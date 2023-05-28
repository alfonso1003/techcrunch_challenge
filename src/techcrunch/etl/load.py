""" not empty"""
import sqlite3

import pandas as pd


class DataLoader:
    def __init__(self, article_df: pd.DataFrame, database: str, table: str):
        self.article_df = article_df
        self.database = database
        self.table = table

    def load_data(self):
        conn = sqlite3.connect(self.database)
        self.article_df.to_sql(self.table, conn, if_exists="replace", index_label="id")
        conn.close()
