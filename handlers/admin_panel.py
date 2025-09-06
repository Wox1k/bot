from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb
from utils.states import Admin
from database import check_profile, new_order, check_order_track_num, change_order_info, check_customers_id

router_admin = Router()

@router_admin.message(Command("admin"))
async def admin(message:Message, state:FSMContext):
    record = check_profile(message.chat.id)
    if record and record[0]["role"] == "admin":
        await message.answer("Запущен режим администрирования.\n"
                             "Выбери нужную команду:", 
                             reply_markup=kb.admin_keyboard)
        
    else:
        await message.answer("Хей, похоже кое-кто пытается написать команду, которую "
                             "ему нельзя писать. На этот раз прощаю, но будь аккуратней",
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
    track_num = message.text
    await state.update_data(track_num=track_num)
    reg_data = await state.get_data()
    tg_id = reg_data.get("order_id")

    record = check_order_track_num(track_num)
    if record:
        status = record[0]["status"]
    else:
        status = "в ожидании"

    await message.answer(text="Отлично, теперь проверь введенные данные. \n"
                         "Когда убедишься в их правильности, жми кнопку 'Сохранить':\n\n"
                         f"telegram_id: {tg_id}\n"
                         f"Трек-номер: {track_num}\n"
                         f"Статус: {status}\n\n"
                         "При необходимости можешь изменить данные, используя кнопки снизу",
                         reply_markup=kb.change_order_keyboard)
    

@router_admin.callback_query(F.data == "admin_back")
async def admin_back(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text("Выбери нужную команду:", 
                                     reply_markup=kb.admin_keyboard)

    await state.clear()

@router_admin.callback_query(F.data == "change_order")
async def change_order(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="Введи трек-номер заказа для изменения:\n",
                                     reply_markup=kb.admin_back_keyboard)
    
    await state.set_state(Admin.change_order_track_num)

@router_admin.message(Admin.change_order_track_num)
async def change_order_track_num(message: Message, state: FSMContext):
    record = check_order_track_num(message.text)
    
    if record:
        await state.update_data(change_order_track_num=message.text)
        track_num = message.text
        status = record[0]["status"]

        await message.answer(text="Выбранный заказ для редактирования:\n\n"
                             f"Трек-номер: {track_num}\n"
                             f"Статус: {status}\n\n"
                             "Выбери, что хочешь изменить:",
                             reply_markup=kb.change_track_num_keyboard)
        
    else:
        await message.answer(text="Кажется, ты ошибся в трек-номере. Такого заказа не существует. Введи трек-номер еще раз",
                             reply_markup=kb.admin_back_keyboard)
        
@router_admin.callback_query(F.data == "change_tg_id")
async def change_tg_id_button(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="Введи новый telegram_id:",
                                     reply_markup=kb.admin_back_keyboard)
    
    await state.set_state(Admin.change_tg_id)

@router_admin.message(Admin.change_tg_id)
async def change_tg_id(message: Message, state:FSMContext):
    tg_id = message.text
    if tg_id.isdigit():
        await state.update_data(order_id=int(message.text))

        reg_data = await state.get_data()
        tg_id = reg_data.get("order_id")
        track_num = reg_data.get("track_num")
        status = reg_data.get("order_status")

        await message.answer("Отлично, telegram_id успешно изменен:\n"
                             f"telegram_id: {tg_id}\n"
                             f"Трек-номер: {track_num}\n"
                             f"Статус: {status}\n\n"
                             "При необходимости можешь изменить данные, используя кнопки снизу",
                             reply_markup=kb.change_order_keyboard)
    
    else:
        await message.answer("Кажется, ты неправильно ввел telegram_id.\n"
                             "Проверь корректность и отправь мне telegram_id еще раз",
                             reply_markup=kb.admin_back_keyboard)
        
@router_admin.callback_query(F.data == "change_track_num")
async def change_track_num(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="Введи новый трек-номер:",
                                     reply_markup=kb.admin_back_keyboard)
    
    await state.set_state(Admin.change_track_num)

@router_admin.message(Admin.change_track_num)
async def change_tg_id(message: Message, state:FSMContext):
    track_num = message.text
    await state.update_data(track_num=track_num)

    reg_data = await state.get_data()
    tg_id = reg_data.get("order_id")

    record = check_order_track_num(track_num)
    if record:
        status = record[0]["status"]
    else:
        status = "в ожидании"

    await state.update_data(order_status=status)
    await message.answer("Отлично, трек-номер успешно изменен:\n"
                            f"telegram_id: {tg_id}\n"
                            f"Трек-номер: {track_num}\n"
                            f"Статус: {status}\n\n"
                            "При необходимости можешь изменить данные, используя кнопки снизу",
                            reply_markup=kb.change_order_keyboard)
    
@router_admin.callback_query(F.data == "change_status")
async def change_status(callback: CallbackQuery):
    await callback.message.edit_text(text="Выбери нужный статус:",
                                     reply_markup=kb.admin_back_keyboard)

@router_admin.callback_query(F.data == "save_order")
async def change_status(callback: CallbackQuery, state:FSMContext, bot:Bot):
    reg_data = await state.get_data()
    tg_id = reg_data.get("order_id")
    track_num = reg_data.get("track_num")
    
    record = check_order_track_num(track_num)
    if record:
        status = record[0]["status"]
    else:
        status = "в ожидании"
    
    new_order(tg_id, track_num, status)
    record = check_order_track_num(track_num)
    customer = check_profile(tg_id)
    if customer:
        if customer[0]["notification"] == "true":
            await bot.send_message(chat_id=tg_id,
                                   text="❗Оформлен новый заказ❗\n\n"
                                   f"ID заказа: {record[0]["id"]}\n"
                                   f"Статус заказа: {status}",
                                   reply_markup=kb.menu_keyboard)
    
    await callback.message.edit_text(text="Заказ успешно сохранен ✅",
                                     reply_markup=kb.admin_back_keyboard)
    await state.clear()

@router_admin.callback_query(F.data == "change_order_track_num")
async def new_order_track_num(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="Введи новый трек-номер:",
                                     reply_markup=kb.admin_back_keyboard)
    
    await state.set_state(Admin.new_order_track_num)

@router_admin.message(Admin.new_order_track_num)
async def new_order_track_num(message: Message, state:FSMContext):
    track_num = message.text
    reg_data = await state.get_data()
    old_track_num = reg_data.get("change_order_track_num")
    await state.update_data(track_num=track_num)
    await state.update_data(change_order_track_num=track_num)
    
    record = check_order_track_num(old_track_num)
    if record:
        status = record[0]["status"]
    else:
        status = "в ожидании"

    change_order_info(old_track_num, "track_num", track_num)

    await message.answer(text="Выбранный заказ для редактирования:\n\n"
                            f"Трек-номер: {track_num}\n"
                            f"Статус: {status}\n\n"
                            "Выбери, что хочешь изменить:",
                            reply_markup=kb.change_track_num_keyboard)

@router_admin.callback_query(F.data == "change_order_status")
async def change_tg_id_button(callback: CallbackQuery):
    await callback.message.edit_text(text="Выбери новый статус:",
                                     reply_markup=kb.status_keyboard)

@router_admin.callback_query(lambda c: c.data.startswith("status"))
async def status(callback: CallbackQuery, state:FSMContext, bot:Bot):
    status = str(callback.data).split(":")[1]
    reg_data = await state.get_data()
    track_num = reg_data.get("change_order_track_num")

    change_order_info(track_num, "status", status)

    customers = check_customers_id(track_num)
    for customer in customers:
        t_id = customer["telegram_id"]
        record = check_profile(t_id)
        if record:
            if record[0]["notification"] == "false":
                continue

            await bot.send_message(chat_id=t_id,
                                   text=f"Статус заказа {customer["id"]} изменен.\n"
                                   f"Новый статус: {status}",
                                   reply_markup=kb.menu_keyboard)


    await callback.message.edit_text(text="Заказ успешно изменен ✅\n"
                                     f"Трек-номер: {track_num}\n"
                                     f"Статус: {status}\n\n"
                                     "Выбери, что хочешь изменить:",
                                     reply_markup=kb.change_track_num_keyboard)
    
    await state.clear()