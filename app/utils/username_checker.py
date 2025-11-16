import aiohttp
async def check_telegram(username):
    async with aiohttp.ClientSession() as s:
        r = await s.get(f"https://t.me/{username}")
        return r.status!=404