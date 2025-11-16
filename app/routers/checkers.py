
from aiogram import Router, types
from app.utils.api_checker import check_api
from app.utils.proxy_checker import check_proxy
from app.utils.ip_lookup import ip_lookup
from app.utils.email_validator import validate_email
from app.utils.ssl_checker import get_ssl_info
from app.utils.username_checker import check_telegram

router = Router()

@router.message(commands=["api"])
async def api_cmd(msg: types.Message):
    try: url = msg.text.split(" ",1)[1]
    except: return await msg.reply("❌ URL missing")
    data = await check_api(url)
    await msg.reply(f"<b>API CHECK</b>\nStatus: {data}")

@router.message(commands=["proxy"])
async def proxy_cmd(msg: types.Message):
    try: proxy = msg.text.split(" ",1)[1]
    except: return await msg.reply("❌ Proxy missing")
    ok = await check_proxy(proxy)
    await msg.reply("Live ✅" if ok else "Dead ❌")
