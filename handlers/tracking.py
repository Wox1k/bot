from aiogram import Router, F
from aiogram.types import CallbackQuery
import utils.keyboards as kb

from database import check_order_id

router_tracking = Router()

button_count = 5

@router_tracking.callback_query(F.data == "my_orders")
async def my_orders(callback: CallbackQuery, start = 0):
    reply_markup = await kb.orders_keyboard_build(callback.from_user.id, start)
    await callback.message.edit_text("Выбери нужную команду:", 
                                     reply_markup=reply_markup.as_markup())
    
@router_tracking.callback_query(lambda c: c.data.startswith("forward_list"))
async def forward_list(callback: CallbackQuery):
    start = int(str(callback.data).split(":")[1])
    global button_count
    start += button_count
    await my_orders(callback, start)

@router_tracking.callback_query(lambda c: c.data.startswith("back_list"))
async def back_list(callback: CallbackQuery):
    start = int(str(callback.data).split(":")[1])
    global button_count
    start -= button_count
    await my_orders(callback, start)

@router_tracking.callback_query(lambda c: c.data.startswith("order"))
async def callback_scroll_forward(callback: CallbackQuery):
    order_id = int(str(callback.data).split(":")[1])
    order = check_order_id(order_id)

    status = order[0]["status"]
    start = int(str(callback.data).split(":")[2])

    reply_markup = await kb.orders_back_keyboard_build(start)
    await callback.message.edit_text(text=f"Заказ №{order_id}:\n\n"
                                     f"Статус заказа: '{status}'",
                                     reply_markup=reply_markup.as_markup())

@router_tracking.callback_query(lambda c: c.data.startswith("start"))
async def start_orders(callback: CallbackQuery):
    start = int(str(callback.data).split(":")[1])
    await my_orders(callback, start)