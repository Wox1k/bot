from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardBuilder

from handlers.tracking import button_count
from database import people_orders

async def orders_keyboard_build(tg_id: int, start_orders: int):
    orders = people_orders(tg_id)
    orders_counter = len(orders)

    kb = InlineKeyboardBuilder()
    two_buttons_flag = 0

    if start_orders >= button_count:
        kb.add(InlineKeyboardButton(text = "<< Назад", callback_data = f"back_list:{start_orders}"))
        two_buttons_flag += 1
    if start_orders + button_count < orders_counter:
        kb.add(InlineKeyboardButton(text = "Вперед >>", callback_data = f"forward_list:{start_orders}"))
        two_buttons_flag += 1

    end = min(start_orders + button_count, orders_counter)

    for ind in range(start_orders, end):    
        order = orders[ind]

        order_id = order["id"]

        kb.button(text = f" Заказ №{order_id}", 
                        callback_data = f"order:{order_id}:{start_orders}")

    kb.add(InlineKeyboardButton(text = "Меню ⫶", callback_data = f"menu"))
           
    if two_buttons_flag == 2:
        kb.adjust(2,1)
    else:
        kb.adjust(1)

    return kb

async def orders_back_keyboard_build(start_orders: int):
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text = "Назад ↩", callback_data = f"start:{start_orders}"))

    return kb

main_true_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Профиль", callback_data="profile"),
            InlineKeyboardButton(text="Мои заказы", callback_data="my_orders")
        ],
        [
            InlineKeyboardButton(text="Найти товар 🔎  ", callback_data="search_product"), 
            InlineKeyboardButton(text="Курс юаня 💸 ", callback_data="exchange_rate")
        ],
        [
            InlineKeyboardButton(text="Рассчитать стоимость заказа 💰", callback_data="calc_order")
        ],
        [
            InlineKeyboardButton(text="Рассчитать стоимость доставки 🚚", callback_data="calc_delivery")
        ],
        [
            InlineKeyboardButton(text="Рефералка 🙋‍♂️", callback_data="referal"),
            InlineKeyboardButton(text="Акции 🎁", url="https://t.me/c/2748083111/27")
        ],
        [
            InlineKeyboardButton(text="FAQ ❓ ", url="https://t.me/c/2748083111/1/29"),
            InlineKeyboardButton(text="Отзывы ⭐ ", callback_data="rate", url="https://t.me/c/2748083111/2")
        ],
        [
            InlineKeyboardButton(text="Связать с администратором ℹ️", callback_data="support")
        ],
        [
            InlineKeyboardButton(text="Уведомления включены ✅", callback_data="notification_false")
        ]
    ]
)

main_false_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Профиль", callback_data="profile"),
            InlineKeyboardButton(text="Мои заказы", callback_data="my_orders")
        ],
        [
            InlineKeyboardButton(text="Найти товар 🔎  ", callback_data="search_product"), 
            InlineKeyboardButton(text="Курс юаня 💸 ", callback_data="exchange_rate")
        ],
        [
            InlineKeyboardButton(text="Рассчитать стоимость заказа 💰", callback_data="calc_order")
        ],
        [
            InlineKeyboardButton(text="Рассчитать стоимость доставки 🚚", callback_data="calc_delivery")
        ],
        [
            InlineKeyboardButton(text="Рефералка 🙋‍♂️", callback_data="referal"),
            InlineKeyboardButton(text="Акции 🎁", url="https://t.me/c/2748083111/27")
        ],
        [
            InlineKeyboardButton(text="FAQ ❓ ", url="https://t.me/c/2748083111/1/29"),
            InlineKeyboardButton(text="Отзывы ⭐ ", callback_data="rate", url="https://t.me/c/2748083111/2")
        ],
        [
            InlineKeyboardButton(text="Связать с администратором ℹ️", callback_data="support")
        ],
        [
            InlineKeyboardButton(text="Уведомления выключены ❌", callback_data="notification_true")
        ]
    ]
)

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

order_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать другой заказ", callback_data="calc_order")
        ],
        [
            InlineKeyboardButton(text="Рассчитать стоимость доставки 🚚", callback_data="calc_delivery")
        ],
        [
            InlineKeyboardButton(text="Связать с администратором ℹ️", callback_data="support")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

delivery_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать доставку из  🇨🇳 Китая 🇨🇳", callback_data="calc_cn")
        ],
        [
            InlineKeyboardButton(text="Рассчитать доставку по  🇷🇺 России 🇷🇺", callback_data="calc_ru")
        ],
        [
            InlineKeyboardButton(text="❓Почему нет точной суммы❓", callback_data="calc_faq")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

delivery_ru_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать доставку из  🇨🇳 Китая 🇨🇳", callback_data="calc_cn")
        ],
        [
            InlineKeyboardButton(text="Связать с администратором ℹ️", callback_data="support")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

delivery_cn_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Заново рассчитать доставку из  🇨🇳 Китая 🇨🇳", callback_data="calc_cn")
        ],
        [
            InlineKeyboardButton(text="Рассчитать доставку по  🇷🇺 России 🇷🇺", callback_data="calc_ru")
        ],
        [
            InlineKeyboardButton(text="Связать с администратором ℹ️", callback_data="support")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

delivery_faq_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рассчитать доставку из  🇨🇳 Китая 🇨🇳", callback_data="calc_cn")
        ],
        [
            InlineKeyboardButton(text="Рассчитать доставку по  🇷🇺 России 🇷🇺", callback_data="calc_ru")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

register_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Зарегистрироваться✍", callback_data="register")
        ],
        [
            InlineKeyboardButton(text="Узнать свой telegram_id", callback_data="tg_id")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

notification_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Зарегистрироваться✍", callback_data="register")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

profile_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Изменить профиль", callback_data="change_profile")
        ],
        [
            InlineKeyboardButton(text="Узнать свой telegram_id", callback_data="tg_id")
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu")
        ]
    ]
)

change_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Имя", callback_data="change_name"),
            InlineKeyboardButton(text="Фамилию ", callback_data="change_last_name")
        ],
        [
            InlineKeyboardButton(text="Username", callback_data="change_username"),
            InlineKeyboardButton(text="Город", callback_data="change_city")
        ],
        [
            InlineKeyboardButton(text="Номер телефона", callback_data="change_phone")
        ],
        [
            InlineKeyboardButton(text="Назад ↩", callback_data="profile")
        ]
    ]
)

cancel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩", callback_data="profile")
        ]
    ]
)

username_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Взять username из профиля", callback_data="username_from_profile")
        ]
    ]
)

change_username_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Взять username из профиля", callback_data="change_username_from_profile")
        ],
        [
            InlineKeyboardButton(text="Назад ↩", callback_data="profile")
        ]
    ]
)

admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Информация об участнике ⓘ", callback_data = "info_about_user")
        ],
        [
            InlineKeyboardButton(text = "Добавить заказ 📦", callback_data = "new_order")
        ],
        [
            InlineKeyboardButton(text = "Изменить информацию о заказе 🔄📦", callback_data = "change_order")
        ],
        [
            InlineKeyboardButton(text = "Отправить сообщение пользователю ✉️", callback_data = "mail_to_one")
        ],
        [
            InlineKeyboardButton(text = "Рассылка всем участникам 📢", callback_data = "mail_to_all")
        ],
        [
            InlineKeyboardButton(text = "Перейти в меню команд ⋮", callback_data = "menu")
        ]
    ]
)

admin_back_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text = "Вернуться к панели админа 🔑", callback_data = "admin_back")
        ],
    ]
)

change_order_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Изменить tg_id", callback_data="change_tg_id")
        ],
        [
            InlineKeyboardButton(text="Изменить трек-номер", callback_data="change_track_num")
        ],
        [
            InlineKeyboardButton(text="Изменить статус", callback_data="change_status")
        ],
        [
            InlineKeyboardButton(text="Сохранить заказ ✅", callback_data="save_order")
        ],
        [
            InlineKeyboardButton(text = "Вернуться к панели админа 🔑", callback_data = "admin_back")
        ],
    ]
)

change_track_num_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Изменить трек-номер", callback_data="change_order_track_num")
        ],
        [
            InlineKeyboardButton(text="Изменить статус", callback_data="change_order_status")
        ],
        [
            InlineKeyboardButton(text = "Вернуться к панели админа 🔑", callback_data = "admin_back")
        ],
    ]
)

referal_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Пригласить друга", callback_data="friend")
        ],
        [
            InlineKeyboardButton(text="Вернуться в меню ⫶", callback_data="menu")
        ]
    ]
)

status_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Выкуплен у продавца 💵", callback_data="status:Выкуплен у продавца 💵")
        ],
        [
            InlineKeyboardButton(text="На складе в Китае 🇨🇳📦", callback_data="status:На складе в Китае 🇨🇳📦")
        ],
        [
            InlineKeyboardButton(text="Отправлен в Москву 🇷🇺", callback_data="status:Отправлен в Москву 🇷🇺")
        ],
        [
            InlineKeyboardButton(text="На складе в Москве 🇷🇺📦", callback_data="status:На складе в Москве 🇷🇺📦")
        ],
        [
            InlineKeyboardButton(text="Отправлен в Ростов-на-Дону 🚚", callback_data="status:Отправлен в Ростов-на-Дону 🚚")
        ],
        [
            InlineKeyboardButton(text="На складе в Ростове-на-Дону 🏠", callback_data="status:На складе в Ростове-на-Дону 🏠")
        ],
        [
            InlineKeyboardButton(text="Выполнен ✅", callback_data="status:Выполнен ✅")
        ],
        [
            InlineKeyboardButton(text="Вернуться к панели админа 🔑", callback_data="admin_back")
        ]
    ]
)