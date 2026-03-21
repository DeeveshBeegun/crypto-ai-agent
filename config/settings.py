import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:1b")
CRYPTOPANIC_API_KEY = os.getenv("CRYPTOPANIC_API_KEY", "")
TELEGRAM_BOT = os.getenv("TELEGRAM_BOT", "")
TELEGRAM_CHATID=os.getenv("TELEGRAM_CHATID", "")
OPENAI_MODEL= os.getenv("OPENAI_MODEL", "")
OPENAI_BASE_URL= os.getenv("OPENAI_BASE_URL", "")
AI_PROVIDER=os.getenv("AI_PROVIDER", "")