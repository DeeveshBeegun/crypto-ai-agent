from collectors.news_collector import fetch_news
from ai.sentiment_analyser import analyse_news
from signals.signal_generator import generate_signal
from config.settings import TELEGRAM_BOT
from alerts.telegram_bot import send_signal
import requests
import asyncio
from database.db import updateDatabase
from database.db import read_sql

def main(): 
    # sentiment_json_array = []

    # print("Fetching News...")
    # news = fetch_news()

    # sentiment_json = analyse_news(news)
    # print("SENTIMENT_JSON:", sentiment_json)
    # sentiment_json_array.append(sentiment_json)
    # print(sentiment_json_array)

    # for signal in sentiment_json_array: 
    #     signal = "Generated Signal:", generate_signal(signal)
    #     send_signal(signal)

    # signal = generate_signal(sentiment_json)
    # print("Generated Signal:", signal)

    # send_signal(signal)
    # asyncio.run(updateDatabase())
    df = read_sql()
    print(df.tail())
    

if __name__ == "__main__":
    main()