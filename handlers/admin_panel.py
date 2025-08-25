from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb
from utils.states import Admin
from database import check_profile, new_order

router_admin = Router()

@router_admin.message(Command("admin"))
async def admin(message:Message, state:FSMContext):
    record = check_profile(message.chat.id)
    if record and record[0]["role"] == "admin":
        await message.answer('Запущен режим администрирования.\n'
                             'Выбери нужную команду:', 
                             reply_markup=kb.admin_keyboard)
        
    else:
        await message.answer('Хей, похоже кое-кто пытается написать команду, которую '
                                'ему нельзя писать. На этот раз прощаю, но будь аккуратней',
                                reply_markup=kb.menu_keyboard)
        
    await state.clear()

@router_admin.callback_query(F.data == "new_order")
async def new_order_start(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="Введи telegram_id заказчика:\n",
                                     reply_markup=kb.admin_back_keyboard)
    
    await state.set_state(Admin.order_id)

@router_admin.message(Admin.order_id)
async def new_order_id(message: Message, state: FSMContext):
    tg_id = message.text
    if tg_id.isdigit():
        await state.update_data(order_id=int(message.text))
        await message.answer("Отлично, теперь напиши трек-номер заказа:",
                             reply_markup=kb.admin_back_keyboard)
        await state.set_state(Admin.order_track_num)
    
    else:
        await message.answer("Кажется, ты неправильно ввел telegram_id.\n"
                             "Проверь корректность и отправь мне telegram_id еще раз",
                             reply_markup=kb.admin_back_keyboard)

@router_admin.message(Admin.order_track_num)
async def new_order_track_num(message: Message, state: FSMContext):
    reg_data = await state.get_data()
    tg_id = reg_data.get("order_id")
    track_num = message.text

    new_order(tg_id, track_num)

    await message.answer(text="Отлично, заказ успешно зарегистрирован:\n\n"
                         f'telegram_id: {tg_id}\n'
                         f'Трек-номер: {track_num}\n'
                         f'Статус: "в ожидании"\n\n'
                         'При необходимости можешь изменить данные, используя кнопки снизу',
                         reply_markup=kb.change_order_keyboard)

    await state.clear()

@router_admin.callback_query(F.data == "admin_back")
async def admin_back(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text("Выбери нужную команду:", 
                                     reply_markup=kb.admin_keyboard)

    await state.clear()