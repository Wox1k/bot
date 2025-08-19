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
        name = record[0]
        last_name = record[1]
        phone = record[4]
        city = record[5]

        await callback.message.edit_text(text=f'Имя: {name} {last_name}\n'
                                         f'Номер телефона: {phone}\n'
                                         f'Город: {city}\n\n'
                                         'При необходимости можешь изменить данные, используя кнопки снизу',
                                         reply_markup=kb.change_keyboard)