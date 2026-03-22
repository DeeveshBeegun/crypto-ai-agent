import json 
import re 
import html

def _extract_json(raw_text: str) -> dict:
    if not raw_text or not raw_text.strip(): 
        raise ValueError("Empty JSON response")
    text = raw_text.strip()

    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.DOTALL)
    if fenced: 
        text = fenced.group(1).strip()
    else: 
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1 and end > start: 
            text = text[start:end + 1]
    try: 
        data, _ = json.JSONDecoder().raw_decode(text)
    except json.JSONDecodeError as exc: 
        raise ValueError(f"Could not parse sentiment JSON: {exc}")
    return data

def generate_signal(sentiment_json: str) -> dict:
    data = _extract_json(sentiment_json)

    coin = str(data.get("coin", "UNKNOWN")).upper()
    sentiment = str(data.get("sentiment", "neutral")).lower().strip()
    confidence_raw = data.get("confidence_score", 0)

    try: 
        confidence = int(float(confidence_raw))
    except (TypeError, ValueError):
        confidence = 0

    confidence_score = max(0, min(100, confidence))

    if sentiment == "bullish":
        if confidence_score >= 80:
            action = "STRONG_BUY"
        elif confidence_score >= 60: 
            action = "BUY"
        else: 
            action = "HOLD"
    elif sentiment == "bearish":
        if confidence_score >= 80: 
            action = "STRONG_SELL"
        elif confidence_score >= 60: 
            action = "SELL"
        else: 
            action = "HOLD"

    return {
        "coin": coin, 
        "sentiment": sentiment, 
        "confidence_score": confidence_score, 
        "signal": action, 
        "reason": data.get("reason", "")
    }
