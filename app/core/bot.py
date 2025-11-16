
from aiogram import Bot
from aiogram.enums import ParseMode
from app.core.settings import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
