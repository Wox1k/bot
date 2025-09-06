from aiogram import Router, F
from aiogram.types import CallbackQuery
import utils.keyboards as kb

from database import check_profile

router_referal = Router()

@router_referal.callback_query(F.data == "referal")
async def change_name(callback: CallbackQuery):
    record = check_profile(callback.from_user.id)

    if not record:
        await callback.message.edit_text(text="У тебя еще нет профиля, но не переживай,\n"
                                         "ты можешь зарегистрироваться, нажав на кнопку снизу",
                                         reply_markup=kb.register_keyboard)
        
    else:
        discount = record[0]["discount"]

        await callback.message.edit_text(text=f"Текущая скидка: {discount}%",
                                         reply_markup=kb.referal_keyboard)