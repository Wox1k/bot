from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from bs4 import BeautifulSoup
import aiohttp

import utils.keyboards as kb

router_course = Router()

async def yuan():
    link = "https://www.banki.ru/products/currency/cb/"

    async with aiohttp.ClientSession() as session:
            async with session.get(link) as response:
                response.raise_for_status()
                soup = BeautifulSoup(await response.text(), "html.parser")

                # Ищем элемент с нужным data-id
                currency_element = soup.find("div", {"data-id": 156})

                if currency_element:
                    rate_element = currency_element.find("div", {"data-test": "text", "class": "Text__sc-vycpdy-0 gJTmbP"})

                    if rate_element:
                        rate_text = rate_element.get_text(strip=True).split("₽")[0]
                        return rate_text
                    else:
                        return "Не удалось найти курс в полученном HTML."

@router_course.callback_query(F.data == "exchange_rate")
async def exchange_rate(callback: CallbackQuery, state: FSMContext):
    rate = await yuan()

    await callback.message.edit_text(text="💱 Курс юаня (CNY):\n"
                                     f"🇨🇳 1 ¥ = {rate} ₽ 🇷🇺\n\n"
                                     "📊 Данные актуальны на текущее время.",
                         parse_mode="Markdown",
                         reply_markup=kb.menu_keyboard)