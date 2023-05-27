import unittest

from .techcrunch import DataExtractor


class TechCrunchTests(unittest.TestCase):
    def test_data_extractor_returns_50_articles(self):
        url = "https://techcrunch.com/wp-json/wp/v2/posts?per_page=50"
        data_extractor = DataExtractor(url)
        article_json = data_extractor.extract_data()
        self.assertEqual(len(article_json), 50)


if __name__ == "__main__":
    unittest.main()
