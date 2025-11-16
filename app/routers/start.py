
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.core.settings import SPONSOR_CHANNEL, MAIN_CHANNEL
from app.core.settings import OWNER_ID

router = Router()

async def check_join(user_id, bot):
    chats=[SPONSOR_CHANNEL, MAIN_CHANNEL]
    for ch in chats:
        try:
            m=await bot.get_chat_member(ch, user_id)
            if m.status=="left":
                return False
        except:
            return False
    return True

@router.message(commands=["start"])
async def start(msg: types.Message, bot):
    if not await check_join(msg.from_user.id, bot):
        kb=InlineKeyboardBuilder()
        kb.button(text="Join Sponsor 🔥", url=f"https://t.me/{SPONSOR_CHANNEL.replace('@','')}")
        kb.button(text="Join Main ⭐", url=f"https://t.me/{MAIN_CHANNEL.replace('@','')}")
        kb.button(text="I Joined ✔", callback_data="check_join")
        return await msg.answer("⚠️ <b>You must join channels to use bot!</b>", reply_markup=kb.as_markup())

    kb=InlineKeyboardBuilder()
    kb.button(text="🔥 Open Main Menu", callback_data="open_menu")
    await msg.answer("<b>Welcome to PRO Checker Bot!</b>", reply_markup=kb.as_markup())
