
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN=os.getenv("BOT_TOKEN")
WEBHOOK_URL=os.getenv("WEBHOOK_URL")
OWNER_ID=int(os.getenv("OWNER_ID"))
SPONSOR_CHANNEL=os.getenv("SPONSOR_CHANNEL")
MAIN_CHANNEL=os.getenv("MAIN_CHANNEL")
