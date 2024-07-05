# utils.py
import requests

import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=API_KEY')
response = requests.get(url)
print response.json()
