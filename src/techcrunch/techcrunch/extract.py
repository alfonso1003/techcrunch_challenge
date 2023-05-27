import requests


class DataExtractor:
    def __init__(self, url: str):
        self.url = url

    def extract_data(self) -> dict:
        response = requests.get(self.url, timeout=5)
        response_json = response.json()
        return response_json
