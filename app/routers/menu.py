
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.callback_query(lambda c: c.data=="open_menu")
async def menu(c: types.CallbackQuery):
    kb=InlineKeyboardBuilder()
    kb.button(text="🌐 API Checker", callback_data="api_menu")
    kb.button(text="🛡 Proxy Checker", callback_data="proxy_menu")
    kb.button(text="📡 IP Lookup", callback_data="ip_menu")
    kb.button(text="📧 Email Validator", callback_data="email_menu")
    kb.button(text="🔐 SSL Checker", callback_data="ssl_menu")
    kb.button(text="👤 Username Checker", callback_data="user_menu")
    await c.message.edit_text("🔥 <b>Select a Tool</b>", reply_markup=kb.as_markup())
