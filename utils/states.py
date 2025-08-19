from aiogram.fsm.state import StatesGroup, State

# Создание анкеты пользователя
class CreateProfile(StatesGroup):
    name = State()
    last_name = State()
    telegram_user_id = State()
    telegram_username = State()
    phone = State()
    city = State()

    set_name = State()
    set_last_name = State()
    set_phone = State()
    set_city = State()