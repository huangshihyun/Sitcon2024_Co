# utils.py
import requests

def fetch_news_data(query, api_key, num_articles=5):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'zh',
        'sortBy': 'publishedAt',
        'pageSize': num_articles  # 限制返回的文章数量
    }
    response = requests.get(url, params=params)
    return response.json()
