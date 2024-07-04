import requests

def fetch_news_data(query, api_key):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'apiKey': api_key,
        'language': 'zh',
        'sortBy': 'publishedAt'
    }
    response = requests.get(url, params=params)
    return response.json()
