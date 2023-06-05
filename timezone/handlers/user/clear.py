from loader import dp
from data.config import admins_id
from aiogram import types
from utils.inline_btn import create_markup
from static.text import users
from aiogram.dispatcher import FSMContext
from utils.db_api import db_task
from handlers.user.start import UserState


@dp.message_handler(commands=['clear'])
async def clear_command(message: types.Message):
    await clear_message(message)


@dp.message_handler(regexp='Очистити список')
async def clear_message(message: types.Message):
    await db_task.delete_all(message.chat.id)
    await message.answer(users.text_clear)
