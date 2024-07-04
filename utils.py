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
import google.generativeai as genai

def generate_gmini_story(prompt, user_id, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    
    # 确保返回的故事内容不含多余的文字
    story_text = response.get('story', '')
    story_text = story_text.replace('感謝您的訊息', '').strip()
    
    return {'story': story_text}
