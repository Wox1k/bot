import math

from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from handlers.course import yuan
from utils.states import Calculations
import utils.keyboards as kb

router_calculations = Router()

@router_calculations.callback_query(F.data == 'calc_order')
async def calc_order(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="📝 Укажи общую сумму заказа в ¥ (например, 97.90)",
                                     reply_markup=kb.menu_keyboard)

    await state.set_state(Calculations.price)

@router_calculations.message(Calculations.price)
async def calculations_order(message: Message, state: FSMContext, bot: Bot):
    rate = await yuan()
    rate = float(rate.replace(",", "."))

    price = round(float(message.text) * rate, 1)
    potencial_commision = math.floor(price / 10)
    commission = potencial_commision if potencial_commision >= 400 else 400
    result = price + commission

    await bot.send_message(message.from_user.id, 
                           text="✅ Предварительный расчет:\n"
                           f"• Стоимость товара: {message.text} ¥\n"
                           f"• Текущий курс: 1 ¥ = {rate} ₽\n"
                           f"• Стоимость в рублях: {price} ₽\n"
                           f"• Наша комиссия 10%: {commission} ₽\n"
                           f"• Итого к оплате за выкуп: {result} ₽\n\n"
                           "💡 Обрати внимание:\n"
                           "• Это стоимость только ВЫКУПА товара. Доставка из Китая оплачивается отдельно.\n"
                           "• Курс валют может незначительно меняться.",
                           reply_markup=kb.order_keyboard)
    
    await state.set_state(Calculations.price)

@router_calculations.callback_query(F.data == 'calc_delivery')
async def calc_delivery(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="💎 Хочешь заранее прикинуть бюджет?\n"
                                     "Мы можем ориентировочно рассчитать стоимость доставки из Китая, если ты знаешь ориентировочный вес товара.\n\n"
                                     "‼️ Помни: итоговый расчет — только после взвешивания товара на нашем складе в Китае.",
                                     reply_markup=kb.delivery_keyboard)
    
    await state.clear()

@router_calculations.callback_query(F.data == 'calc_faq')
async def calc_faq_delivery(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="🤷‍♂️ Почему нельзя назвать точную стоимость сразу?\n\n"
                                     "К сожалению, на итоговый вес влияет много факторов, которые мы не контролируем:\n"
                                     "• Упаковка продавца: иногда она очень тяжелая.\n"
                                     "• Упаковка транспортной компании в Китае для безопасной перевозки.\n"
                                     "• Погрешность веса, указанного на сайте.\n\n"
                                     "Мы не хотим называть тебе одну сумму заранее, а потом брать другую. Поэтому расчет доставки — после взвешивания по факту.\n\n"
                                     "Это честно✅",
                                     reply_markup=kb.delivery_faq_keyboard)
    
    await state.clear()
    
@router_calculations.callback_query(F.data == 'calc_ru')
async def calc_ru(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="📦 Для точного расчета доставки от нашего склада до твоего города воспользуйся официальными калькуляторами:\n\n"
                                     "• Калькулятор СДЭК: https://www.cdek.ru/ru/calculate\n"
                                     "• Калькулятор Почта России https://www.pochta.ru/shipment?type=PARCEL&weight=200\n\n"
                                     "Не забудь указать:\n"
                                     "- Город назначения: Ваш город\n"
                                     "- Город отправления: Ростов-на-дону\n"
                                     "- Вес: Твой ориентировочный вес\n"
                                     "- Габариты: Можно указать ориентировочно",
                                     reply_markup=kb.delivery_ru_keyboard)
    
    await state.clear()
    
@router_calculations.callback_query(F.data == 'calc_cn')
async def calc_cn(callback: CallbackQuery, state:FSMContext):
    await callback.message.edit_text(text="✏️ Введи ориентировочный вес товара в килограммах (например: 1.5):",
                                     reply_markup=kb.menu_keyboard)
    
    await state.set_state(Calculations.weight)

@router_calculations.message(Calculations.weight)
async def calculations_order(message: Message, state: FSMContext, bot: Bot):
    weight = float(message.text.replace(",", "."))
    tariff = 400
    result = round(weight * tariff, 1)

    await bot.send_message(message.from_user.id, 
                           text="✅ Ориентировочная стоимость доставки Китай -> Москва:\n\n"
                           f"• Предполагаемый вес: {weight}\n"
                           f"• Усредненный тариф: {tariff} ₽/кг\n"
                           f"• Итого: {result} ₽",
                           reply_markup=kb.delivery_cn_keyboard)