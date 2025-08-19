from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb

router_menu = Router()

@router_menu.callback_query(F.data == "menu")
async def exchange_rate(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Выбери нужную функцию:\n",
                         reply_markup=kb.main_keyboard)