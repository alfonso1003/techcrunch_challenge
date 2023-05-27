from .techcrunch import ArticleTransformer, AuthorTransformer, DataExtractor, DataLoader


def main() -> None:
    # extract articles
    print("... Extracting articles from techcrunch.com ...")
    url = "https://techcrunch.com/wp-json/wp/v2/posts?per_page=100"
    article_extractor = DataExtractor(url)
    article_json = article_extractor.extract_data()

    # transform articles
    print("... Transforming articles to match db schema ...")
    article_transformer = ArticleTransformer(article_json)
    article_df = article_transformer.transform_data()

    # extract authors
    print("... Extracting authors from techcrunch.com ...")
    url_base = "https://techcrunch.com/wp-json/tc/v1/users?per_page=100&include="
    author_id_list = article_transformer.get_distinct_data_vals("author_id")
    author_id_string = ",".join([str(author_id) for author_id in author_id_list])
    url = url_base + author_id_string
    author_extractor = DataExtractor(url)
    author_json = author_extractor.extract_data()

    # transform authors
    print("... Transforming authors to match db schema ...")
    author_transformer = AuthorTransformer(author_json)
    author_df = author_transformer.transform_data()

    # load authors
    print("... Loading authors to database ...")
    db = "./db/techcrunch.db"
    authors_table = "authors"
    author_loader = DataLoader(author_df, database=db, table=authors_table)
    author_loader.load_data()

    # load articles
    print("... Loading articles to database ...")
    db = "./db/techcrunch.db"
    articles_table = "articles"
    article_loader = DataLoader(article_df, database=db, table=articles_table)
    article_loader.load_data()


if __name__ == "__main__":
    main()
