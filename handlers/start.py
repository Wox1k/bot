from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ChatAction
from aiogram.fsm.context import FSMContext

import utils.keyboards as kb

router_start = Router()

@router_start.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.bot.send_chat_action(
        chat_id=message.from_user.id, 
        action=ChatAction.TYPING
    )
    await message.answer(
        text=f"👋 Привет! Добро пожаловать в Domino Express 🎲\n\n"
        "Здесь можно легко заказать товары из Китая 🇨🇳:\n"
        "🔹 Отправь стоимость заказа — получишь цену с комиссией\n"
        "🔹 Загрузи фото — админ поможет найти похожий товар\n"
        "🔹 Есть рефералка 💰 — зови друзей и экономь на доставке\n\n"
        "Если что-то непонятно — пиши админу 😉",
        parse_mode="Markdown",
        reply_markup=kb.menu_keyboard
    )
    await state.clear()