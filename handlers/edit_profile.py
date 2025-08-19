from aiogram import Bot, F
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.states import CreateProfile
from aiogram import Router
from database import change_user_info, check_profile
from utils.states import CreateProfile

import utils.keyboards as kb
    
router_edit = Router()

@router_edit.callback_query(F.data == 'change_name')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Введи свое имя:',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_name)

@router_edit.message(CreateProfile.set_name)
async def set_name(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'name', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]
    last_name = record[1]
    phone = record[4]
    city = record[5]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()


@router_edit.callback_query(F.data == 'change_last_name')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Введи свою фамилию:',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_last_name)

@router_edit.message(CreateProfile.set_last_name)
async def set_last_name(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'last_name', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]
    last_name = record[1]
    phone = record[4]
    city = record[5]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()

@router_edit.callback_query(F.data == 'change_phone')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Введи свой номер телефона (начиная с +7):',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_phone)

@router_edit.message(CreateProfile.set_phone)
async def set_about_self(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'phone', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]
    last_name = record[1]
    phone = record[4]
    city = record[5]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()


@router_edit.callback_query(F.data == 'change_city')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Напиши свой город:',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_city)

@router_edit.message(CreateProfile.set_city)
async def set_about_self(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'city', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]
    last_name = record[1]
    phone = record[4]
    city = record[5]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()