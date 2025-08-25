from aiogram.fsm.state import StatesGroup, State

# Создание анкеты пользователя
class CreateProfile(StatesGroup):
    name = State()
    last_name = State()
    username = State()
    phone = State()
    city = State()

    set_name = State()
    set_last_name = State()
    set_username = State()
    set_phone = State()
    set_city = State()

# Поиск товара
class SearchProduct(StatesGroup):
    product = State()

# Рассчет стоимости
class Calculations(StatesGroup):
    price = State()
    weight = State()

# Панель админа
class Admin(StatesGroup):
    order_id = State()
    order_track_num = State()