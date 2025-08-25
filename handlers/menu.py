from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb
from database import check_profile, change_user_info

router_menu = Router()

@router_menu.callback_query(F.data == "menu")
async def menu(callback: CallbackQuery, state: FSMContext):
    reply_markup = kb.main_false_keyboard

    tg_id = callback.from_user.id
    record = check_profile(tg_id)

    if record and record[0]["notification"] == "true":
        reply_markup = kb.main_true_keyboard

    await callback.message.edit_text(text="Выбери нужную функцию:\n",
                                     reply_markup=reply_markup)
    
    await state.clear()

@router_menu.callback_query(F.data == "notification_false")
async def notification_true(callback: CallbackQuery):
    tg_id = callback.from_user.id
    record = check_profile(tg_id)

    if record:
        if record[0]["notification"] == "true":
            change_user_info(tg_id, "notification", "false")
            await callback.message.edit_text(text="Выбери нужную функцию:\n",
                                             reply_markup=kb.main_false_keyboard)
    else:
        await callback.message.edit_text(text="Прежде, чем нажимать на эту кнопку, тебе нужно зарегистрироваться 🥺\n"
                                         "Ты можешь это сделать, нажав на кнопку снизу",
                                         reply_markup=kb.notification_keyboard)
        
@router_menu.callback_query(F.data == "notification_true")
async def notification_true(callback: CallbackQuery):
    tg_id = callback.from_user.id
    record = check_profile(tg_id)

    if record:
        if record[0]["notification"] == "false":
            change_user_info(tg_id, "notification", "true")
            await callback.message.edit_text(text="Выбери нужную функцию:\n",
                                             reply_markup=kb.main_true_keyboard)
    else:
        await callback.message.edit_text(text="Прежде, чем нажимать на эту кнопку, тебе нужно зарегистрироваться 🥺\n"
                                         "Ты можешь это сделать, нажав на кнопку снизу",
                                         reply_markup=kb.notification_keyboard)