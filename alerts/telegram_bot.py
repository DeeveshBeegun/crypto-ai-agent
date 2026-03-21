from config.settings import TELEGRAM_BOT
from config.settings import TELEGRAM_CHATID
import requests

def send_signal(signal: str):

  url_requests = f"https://api.telegram.org/bot{TELEGRAM_BOT}/getUpdates"

  print(requests.get(url_requests))

  url = f"https://api.telegram.org/bot{TELEGRAM_BOT}/sendMessage"

  payload = {
      "chat_id": TELEGRAM_CHATID, 
      "text": signal
  }

  requests.post(url, json=payload)



