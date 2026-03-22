from config.settings import TELEGRAM_BOT
from config.settings import TELEGRAM_CHATID
import requests
import html
from collections.abc import Mapping
from typing import Any

def _format_label(value:str) -> str: 
  return value.replace("_", " ").title()

def _format_signal_message(signal: Mapping[str, Any]) -> str: 
  coin = html.escape(str(signal.get("coin", "UNKNOWN")).upper())
  action_raw = str(signal.get("signal", "HOLD"))
  sentiment_raw = str(signal.get("sentiment", "neutral"))

  action = html.escape(_format_label(action_raw))
  sentiment = html.escape(_format_label(sentiment_raw))

  confidence_raw = signal.get("confidence_score", 0)
  try:
     confidence = max(0, min(100, int(float(confidence_raw))))
  except (TypeError, ValueError):
     confidence = 0

  reason = str(signal.get("reason", "")).strip()
  reason_text = html.escape(reason) if reason else "No supporting rationale provided."

  if action_raw == "STRONG_BUY":
     header = "🟢🟢 <b>STRONG BUY SIGNAL</b>"
  elif action_raw == "BUY":
     header = "🟢 <b>BUY SIGNAL</b>"
  elif action_raw == "STRONG_SELL":
     header = "🔴🔴 <b>STRONG SELL SIGNAL</b>"
  elif action_raw == "SELL":
     header = "🔴 <b>SELL SIGNAL</b>"
  else:
     header = "🟡 <b>HOLD SIGNAL</b>"

  return (
        f"{header}\n"
        f"━━━━━━━━━━\n"
        f"🪙 <b>{coin}</b>\n"
        f"📊 {sentiment}\n"
        f"⚡ <b>{action}</b>\n"
        f"🎯 Confidence: <b>{confidence}%</b>\n\n"
        f"📝 <b>Reason</b>\n"
        f"{reason_text}"
    )

def send_signal(signal: Mapping[str, Any] | str):

  url_requests = f"https://api.telegram.org/bot{TELEGRAM_BOT}/getUpdates"

  if isinstance(signal, Mapping): 
    message = _format_signal_message(signal)
  else: 
    message = html.escape(str(signal))

  print(requests.get(url_requests))

  url = f"https://api.telegram.org/bot{TELEGRAM_BOT}/sendMessage"

  payload = {
      "chat_id": TELEGRAM_CHATID, 
      "text": message, 
      "parse_mode": "HTML", 
      "disable_web_page_preview": True, 
  }

  requests.post(url, json=payload)



