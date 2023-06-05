from loader import dp
from data.config import admins_id
from aiogram import types
from utils.inline_btn import create_markup
from static.text import users
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from utils.db_api import db_task


class UserState(StatesGroup):
    new_task = State()


MAIN_MARKUP = None


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    global MAIN_MARKUP
    if not MAIN_MARKUP:
        MAIN_MARKUP = await create_markup('reply', 2, ['Подивитися список'], ['Додати новий'], ['Очистити список'])

    await message.answer(users.text_start.format(message.chat.first_name), reply_markup=MAIN_MARKUP)
