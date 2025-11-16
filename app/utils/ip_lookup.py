import aiohttp
async def ip_lookup(ip):
    async with aiohttp.ClientSession() as s:
        async with s.get(f"http://ip-api.com/json/{ip}") as r:
            return await r.json()