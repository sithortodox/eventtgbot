import os

# Bot token from the BotFather
API_TOKEN = os.environ.get("API_TOKEN") or "6088000209:AAFweaeNJtsCMD08gtuiHoi6-fPy_u8_qxM"

# Log chat ID for sending bot status updates (optional)
LOG_CHAT_ID = os.environ.get("LOG_CHAT_ID") or None

# Available cities and their public calendar URLs
AVAILABLE_CITIES = {
    "Москва": "https://calendar.google.com/calendar/ical/d3b3494781229f1d4e2d2c72d0b0e263bca713c503e13fa8cfc37e84913d26fe%40group.calendar.google.com/private-336915723ded14871c86079c7dafb7fe/basic.ics",
    
}

# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL") or "sqlite:///events_bot.db"
