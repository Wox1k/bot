from aiogram import Bot, F
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.states import CreateProfile
from aiogram import Router
from database import change_user_info, check_profile
from utils.states import CreateProfile

import utils.keyboards as kb
    
router_edit_profile = Router()

@router_edit_profile.callback_query(F.data == 'change_name')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Введи свое имя:',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_name)

@router_edit_profile.message(CreateProfile.set_name)
async def set_name(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'name', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]["name"]
    last_name = record[0]["last_name"]
    phone = record[0]["phone"]
    city = record[0]["city"]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()


@router_edit_profile.callback_query(F.data == 'change_last_name')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Введи свою фамилию:',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_last_name)

@router_edit_profile.message(CreateProfile.set_last_name)
async def set_last_name(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'last_name', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]["name"]
    last_name = record[0]["last_name"]
    phone = record[0]["phone"]
    city = record[0]["city"]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()

@router_edit_profile.callback_query(F.data == 'change_username')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Укажи в профиле новый username.\n'
                                     'После этого жми на кнопку снизу',
                                     reply_markup=kb.change_username_keyboard)
    await state.set_state(CreateProfile.set_username)

@router_edit_profile.callback_query(F.data == "change_username_from_profile")
async def username_from_profile(callback: CallbackQuery, state: FSMContext):
    username = callback.from_user.username
    if not username:
        await callback.message.answer('Кажется у тебя не указан username.\n'
                                      'Укажи его в профиле и повторно нажми на кнопку снизу\n',
                         reply_markup=kb.change_username_keyboard)
        await state.set_state(CreateProfile.set_username)

    else:
        record = check_profile(callback.from_user.id)
        name = record[0]["name"]
        last_name = record[0]["last_name"]
        phone = record[0]["phone"]
        city = record[0]["city"]

        if record[0]["username"] != username:   
            change_user_info(callback.from_user.id, 'username', username)

        await callback.message.edit_text(text='Изменение прошло успешно!\n\n'
                                      f'Имя: {name} {last_name}\n'
                                      f'Номер телефона: {phone}\n'
                                      f'Город: {city}\n\n'
                                      'При необходимости можешь изменить данные, используя кнопки снизу',
                                      reply_markup=kb.change_keyboard)
        
        await state.clear()

@router_edit_profile.callback_query(F.data == 'change_phone')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Введи свой номер телефона (начиная с +7):',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_phone)

@router_edit_profile.message(CreateProfile.set_phone)
async def set_about_self(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'phone', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]["name"]
    last_name = record[0]["last_name"]
    phone = record[0]["phone"]
    city = record[0]["city"]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()


@router_edit_profile.callback_query(F.data == 'change_city')
async def change_name(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text='Напиши свой город:',
                                     reply_markup=kb.cancel_keyboard)
    await state.set_state(CreateProfile.set_city)

@router_edit_profile.message(CreateProfile.set_city)
async def set_about_self(message: Message, state: FSMContext, bot: Bot):
    change_user_info(message.from_user.id, 'city', str(message.text))

    record = check_profile(message.from_user.id)
    name = record[0]["name"]
    last_name = record[0]["last_name"]
    phone = record[0]["phone"]
    city = record[0]["city"]

    await bot.send_message(message.from_user.id, 
                           'Изменение прошло успешно!\n\n'
                           f'Имя: {name} {last_name}\n'
                           f'Номер телефона: {phone}\n'
                           f'Город: {city}\n\n'
                           'При необходимости можешь изменить данные, используя кнопки снизу',
                           reply_markup=kb.change_keyboard)
    await state.clear()