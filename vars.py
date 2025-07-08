#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29141829"))
API_HASH = environ.get("API_HASH", "25020d00fbcfd406fc9979d24d761bff")
BOT_TOKEN = environ.get("BOT_TOKEN"7827908788:AAEwYrm_Z-OSPj-Ex6wZFg-SASU1gpLbbvg")
OWNER = int(environ.get("OWNER", "5323404314"))
CREDIT = environ.get("CREDIT", "TXT 𝘽𝙊𝙏𝙎")
AUTH_USER = os.environ.get('AUTH_USERS', '5323404314','5323404314').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
