
import asyncio
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from app.core.bot import bot
from app.core.dispatcher import dp
from app.core.settings import WEBHOOK_URL
from app.routers.start import router as start_router
from app.routers.menu import router as menu_router
from app.routers.checkers import router as check_router
from app.routers.admin import router as admin_router

dp.include_router(start_router)
dp.include_router(menu_router)
dp.include_router(check_router)
dp.include_router(admin_router)

async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    await bot.delete_webhook()

def main():
    app = web.Application()
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    SimpleRequestHandler(dp, bot).register(app, path="/webhook")
    setup_application(app, dp, bot=bot)

    web.run_app(app, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
