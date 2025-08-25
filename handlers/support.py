import os

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb

router_support = Router()

@router_support.callback_query(F.data == "support")
async def exchange_rate(callback: CallbackQuery, state: FSMContext):
    admin_username = os.getenv("admin_username")
    await callback.message.edit_text(text=f"Ссылка для связи с администратором: {admin_username}",
                                     reply_markup=kb.menu_keyboard)
    
    await state.clear()