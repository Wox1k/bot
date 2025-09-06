import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers.admin_panel import router_admin
from handlers.calculations import router_calculations
from handlers.course import router_course
from handlers.edit_profile import router_edit_profile
from handlers.menu import router_menu
from handlers.profile import router_profile
from handlers.referal import router_referal
from handlers.register import router_register
from handlers.search import router_search
from handlers.start import router_start
from handlers.support import router_support
from handlers.tracking import router_tracking

from database import clear, clear_order

async def main():
    load_dotenv()

    debug = os.getenv("DEBUG")

    if not debug:
        token = os.getenv("BOT_TOKEN")
        logging.basicConfig(level=logging.INFO)
    else:
        token = os.getenv("BOT_TOKEN_TEST")
        logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_routers(
        router_admin,
        router_calculations,
        router_course,
        router_edit_profile,
        router_menu,
        router_profile,
        router_referal,
        router_register,
        router_search,
        router_start,
        router_support,
        router_tracking
    )
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")