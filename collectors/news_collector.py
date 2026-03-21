import requests

from config.settings import CRYPTOPANIC_API_KEY


def fetch_news():
    if not CRYPTOPANIC_API_KEY:
        raise ValueError("Missing CRYPTOPANIC_API_KEY in config/settings.py or environment")

    url = f'https://cryptopanic.com/api/developer/v2/posts/?auth_token={CRYPTOPANIC_API_KEY}&public=true'

    response = requests.get(url)
    if response.status_code == 200: 
        news_data = response.json() 
        collected_posts = []
        for post in news_data['results']: 
            collected_posts.append(
                f"Title: {post['title']}\nDescription: {post['description']}"
            )
        return "\n\n".join(collected_posts)
    else: 
        raise RuntimeError('Failed to fetch news')