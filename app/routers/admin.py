
from aiogram import Router, types
from app.core.settings import OWNER_ID

router = Router()

@router.message(commands=["admin"])
async def admin(msg: types.Message):
    if msg.from_user.id != OWNER_ID:
        return
    await msg.reply("<b>Admin Panel</b>\n/logs\n/broadcast msg")
