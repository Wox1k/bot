from aiogram import Bot, F
from aiogram.types import Message, ContentType, CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.states import CreateProfile
from aiogram import Router
from database import change_user_info, check_profile
from utils.states import CreateProfile

import utils.keyboards as kb
    
router_edit_order = Router()