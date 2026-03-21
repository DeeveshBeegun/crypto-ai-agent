from pydantic import BaseModel
import requests 

from config.settings import OLLAMA_BASE_URL, OLLAMA_MODEL
from config.settings import OPENAI_BASE_URL, OPENAI_MODEL
from config.settings import AI_PROVIDER

class SentimentResult(BaseModel):
    coin: str
    sentiment: str
    confidence: int
    reason: str

def _build_prompt(text: str) -> str: 
    return f"""
you are a crypto market analyst. 

Analyse the following news and return the fields below as JSON. 
Give analysis for only one coin per JSON
Return strict JSON only

Fields: 
coin
sentiment as bullish, bearish or neutral
confidence score in percentage
reason

News: 
{text}
""".strip()


def analyse_news(text: str) -> str:
    prompt = _build_prompt(text)
    if AI_PROVIDER == "openAi":
        return call_openAI_model(prompt)
    return call_ollama_model(prompt)

def call_ollama_model(prompt: str) -> str: 
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL.rstrip('/')}/api/chat",
            json={
                "model": OLLAMA_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
            },
            timeout=60,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        raise RuntimeError(
            f"Failed to reach Ollama at {OLLAMA_BASE_URL}. Make sure Ollama is running and the model '{OLLAMA_MODEL}' is pulled."
        ) from exc

    payload = response.json()
    message = payload.get("message", {})
    content = message.get("content", "")

    if not content:
        raise RuntimeError("Ollama returned an empty response")

    return content

def call_openAI_model(prompt:str) -> str: 
    try: 
        response = requests.post(
            f"{OPENAI_BASE_URL.rstrip('/')}/api/chat", 
            json={
                "model": OPENAI_MODEL, 
                "messages": [{"role": "user", "content": prompt}], 
                "temperature": 0.2, 
            }, 
            timeout=60,
        )
        response.raise_for_status()
    except requests.RequestException as exc: 
        raise RuntimeError(
            f"Failed to reach openai at {OPENAI_BASE_URL}"
        ) from exc
    
    payload = response.json()
    message = payload.get("message", {})
    content = message.get("content", "")

    if not content: 
        raise RuntimeError("Openai returned an empty response")
    
    return content