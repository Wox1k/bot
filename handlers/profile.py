from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb
from database import check_profile

router_profile = Router()

@router_profile.callback_query(F.data == "profile")
async def profile(callback: CallbackQuery, state: FSMContext):
    record = check_profile(callback.message.chat.id)
    
    if not record:
        await callback.message.edit_text(text="У тебя еще нет профиля, но не переживай,\n"
                                         "ты можешь зарегистрироваться, нажав на кнопку снизу",
                                         parse_mode="Markdown",
                                         reply_markup=kb.register_keyboard)
        
    else:
        name = record[0]["name"]
        last_name = record[0]["last_name"]
        phone = record[0]["phone"]
        city = record[0]["city"]

        await callback.message.edit_text(text=f"Имя: {name} {last_name}\n"
                                         f"Номер телефона: {phone}\n"
                                         f"Город: {city}\n\n"
                                         "При необходимости можешь изменить данные, нажав кнопку снизу",
                                         reply_markup=kb.profile_keyboard)
    await state.clear()
        
@router_profile.callback_query(F.data == "change_profile")
async def change_profile(callback: CallbackQuery):
    record = check_profile(callback.message.chat.id)

    name = record[0]["name"]
    last_name = record[0]["last_name"]
    phone = record[0]["phone"]
    city = record[0]["city"]

    await callback.message.edit_text(text=f"Имя: {name} {last_name}\n"
                                     f"Номер телефона: {phone}\n"
                                     f"Город: {city}\n\n"
                                     "Выбери, что хочешь изменить",
                                     reply_markup=kb.change_keyboard)
    
@router_profile.callback_query(F.data == "tg_id")
async def profile(callback: CallbackQuery):
    tg_id = callback.from_user.id
    await callback.message.edit_text(text=f"Твой telegram_id: {tg_id}",
                                     reply_markup=kb.cancel_keyboard)