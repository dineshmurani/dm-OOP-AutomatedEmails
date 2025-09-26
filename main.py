## Newsapi.org API key 3586a06025c9449fbd48d8c78c2a9dad
import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2025-08-26&sortBy=publishedAt&apiKey=3586a06025c9449fbd48d8c78c2a9dad")
content = response.text
pprint(content)