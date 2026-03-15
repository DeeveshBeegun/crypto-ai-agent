from config.settings import TELEGRAM_BOT
from config.settings import TELEGRAM_CHATID
import requests

def send_signal():

  url_requests = f"https://api.telegram.org/bot{TELEGRAM_BOT}/getUpdates"

  print(requests.get(url_requests))

  url = f"https://api.telegram.org/bot{TELEGRAM_BOT}/sendMessage"

  payload = {
      "chat_id": TELEGRAM_CHATID, 
      "text": "Test message from crypto ai bot"
  }

  requests.post(url, json=payload)



