from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardBuilder, InlineKeyboardBuilder

main_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Профиль", callback_data="profile"),
        ],
        [
            InlineKeyboardButton(text="Найти товар🔎", callback_data="search_product"), 
            InlineKeyboardButton(text="Курс юаня💸", callback_data="exchange_rate")
        ],
        [
            InlineKeyboardButton(text="FAQ❓", callback_data="support"),
            InlineKeyboardButton(text="Отзывы⭐", callback_data="rate"),
        ]
    ]
)

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu"),
        ]
    ]
)

register_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Зарегистрироваться✏️", callback_data="register"),
        ],
        [
            InlineKeyboardButton(text="Меню ⫶", callback_data="menu"),
        ],
    ]
)

change_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Вернуться в меню ⫶", callback_data="menu"),
        ],
        [
            InlineKeyboardButton(text="Изменить имя", callback_data="change_name"),
            InlineKeyboardButton(text="Изменить фамилию", callback_data="change_last_name")
        ],
        [
            InlineKeyboardButton(text="Изменить номер телефона", callback_data="change_phone")
        ],
        [
            InlineKeyboardButton(text="Изменить Город", callback_data="change_city")
        ]
    ]
)

cancel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад ↩", callback_data="profile"),
        ]
    ]
)