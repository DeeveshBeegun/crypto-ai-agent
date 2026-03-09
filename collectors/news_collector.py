import requests

API_KEY = ""


def fetch_news():
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={API_KEY}&public=true"

    response = requests.get(url)

    print(response)

    data = response.json()

    news = []

    print(data)

    # for post in data["results"]:
    #     news.append({
    #         "title": post["title"], 
    #         "url": post["url"], 
    #         "source": post["source"]["title"], 
    #         "published": post["published_at"]
    #     })
    return data

def print_helloWorld(): 
    print("Hello World")