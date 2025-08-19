import os
import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers.start import router_start
from handlers.course import router_course
from handlers.menu import router_menu
from handlers.profile import router_profile
from handlers.register import router_register
from handlers.edit_profile import router_edit

from database import clear

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
        router_start,
        router_course,
        router_menu,
        router_profile,
        router_register,
        router_edit
    )
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')