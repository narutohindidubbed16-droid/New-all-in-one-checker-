import aiohttp
async def check_proxy(proxy):
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get("http://httpbin.org/ip",proxy=f"http://{proxy}",timeout=7) as r:
                return r.status==200
    except:
        return False