from aiogram import Router, F, Bot
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.states import CreateProfile
import utils.keyboards as kb
from database import new_user

router_register = Router()

@router_register.callback_query(F.data == "register")
async def start_register(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text("Для начала, напиши своё имя:")
    await state.set_state(CreateProfile.name)
    
@router_register.message(CreateProfile.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(f"Приятно познакомиться, {message.text} 👀\n"
                         "Теперь напиши свою фамилию:")
    await state.set_state(CreateProfile.last_name)

@router_register.message(CreateProfile.last_name)
async def register_last_name(message: Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(CreateProfile.username)

    await message.answer("Пожалуйста, убедись, что у тебя в профиле указан username.\n"
                         "Как все проверишь, жми кнопку снизу",
                         reply_markup=kb.username_keyboard)

@router_register.callback_query(F.data == "username_from_profile")
async def username_from_profile(callback: CallbackQuery, state: FSMContext):
    username = callback.from_user.username
    if not username:
        await callback.message.answer("Кажется у тебя все еще не указан username.\n"
                                      "Укажи его в профиле и повторно нажми на кнопку снизу\n",
                         reply_markup=kb.username_keyboard)
        await state.set_state(CreateProfile.username)

    else:
        await state.update_data(username=username)
        await callback.message.edit_text("Теперь напиши свой номер телефона (начиная с +7):") 
        await state.set_state(CreateProfile.phone)


@router_register.message(CreateProfile.phone)
async def register_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Отлично, теперь напиши свой город:")
    await state.set_state(CreateProfile.city)
                         
@router_register.message(CreateProfile.city)
async def register_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text)

    reg_data = await state.get_data()
    name = reg_data.get("name")
    last_name = reg_data.get("last_name")
    tg_id = message.chat.id
    username = reg_data.get("username")
    phone = reg_data.get("phone")
    city = reg_data.get("city")

    new_user(name, last_name, tg_id, username, phone, city)

    await message.answer("Поздравляю, ты успешно зарегистировался:\n\n"
                                  f"Имя: {name} {last_name}\n"
                                  f"Номер телефона: {phone}\n"
                                  f"Город: {city}\n\n"
                                  "Если вдруг ошибся с данными, то можешь изменить их, используя кнопки снизу",
                                  reply_markup=kb.profile_keyboard)