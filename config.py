import os

# --- Telegram API Details ---
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# --- Bot & Owner Info ---
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
LOG_GROUP = int(os.environ.get("LOG_GROUP", "0")) # Yahan /start karne walo ka log aayega

# --- Assistant Session ---
STRING_SESSION = os.environ.get("STRING_SESSION", "")

# --- Database ---
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "")

# --- External APIs & Cookies ---
GROK_API_KEY = os.environ.get("GROK_API_KEY", "")
# In cookies ko hum aage chal kar yt-dlp ke format me use karenge
IG_COOKIES = os.environ.get("IG_COOKIES", "")
YT_COOKIES = os.environ.get("YT_COOKIES", "")

