import aiohttp, time
async def check_api(url):
    try:
        start=time.time()
        async with aiohttp.ClientSession() as s:
            async with s.get(url,timeout=10) as r:
                return {"status":r.status,"time":round(time.time()-start,3),"content_type":r.headers.get("Content-Type")}
    except Exception as e:
        return {"error":str(e)}