import os

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb
from utils.states import SearchProduct

router_search = Router()

@router_search.callback_query(F.data == "search_product")
async def search_product(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Пришли мне фотографию товара и его описание (все одним сообщением)",
                                     reply_markup=kb.menu_keyboard)
    
    await state.set_state(SearchProduct.product)

@router_search.message(SearchProduct.product)
async def info_about_product(message: Message, bot:Bot, state: FSMContext):
    await message.answer(text="Спасибо за обращение. Я дам знать, когда мы найдем нужный тебе товар",
                         reply_markup=kb.menu_keyboard)

    admin_id = os.getenv("admin_id")
    caption = "🚨🚨🚨НОВЫЙ ЗАКАЗ🚨🚨🚨\n\nusername: @" + str(message.from_user.username) + "\ntelegram_id: " + str(message.from_user.id) + "\n\n"

    if message.photo:
        caption += str(message.caption)
        await bot.send_photo(chat_id=admin_id,
                             photo=message.photo[0].file_id,
                             caption=caption)
    else:
        caption += str(message.text)
        await bot.send_message(chat_id=admin_id,
                               text=caption)
    
    await state.clear()