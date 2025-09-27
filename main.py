## Newsapi.org API key 3586a06025c9449fbd48d8c78c2a9dad
import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass

url = ("https://newsapi.org/v2/everything?"
       "qInTitle=meditation&"
       "from=2025-09-25&"
       "to=2025-09-27&"
       "language=en&"
       "apiKey=3586a06025c9449fbd48d8c78c2a9dad")

response = requests.get(url)
content = response.text
pprint(content)