from collectors.news_collector import fetch_news
from ai.sentiment_analyser import analyse_news
from signals.signal_generator import generate_signal

def main(): 
    print("Fetching News...")
    news = fetch_news()

    sentiment_json = analyse_news(news)
    print("SENTIMENT_JSON:", sentiment_json)

    signal = generate_signal(sentiment_json)
    print("Generated Signal:", signal)
    
if __name__ == "__main__":
    main()