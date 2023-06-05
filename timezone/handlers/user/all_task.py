from loader import dp
from data.config import admins_id
from aiogram import types
from utils.inline_btn import create_markup
from static.text import users
from aiogram.dispatcher import FSMContext
from utils.db_api import db_task
from handlers.user.start import UserState


@dp.message_handler(commands=['list'])
async def all_task_command(message: types.Message):
    await all_task_message(message)


@dp.message_handler(regexp='Подивитися список')
async def all_task_message(message: types.Message):
    data = await db_task.deanon(message.chat.id)
    if data:
        tasks = '\n'.join([users.text_all_task_example.format(i+1, t.name, t.time) for i, t in enumerate(data)])
        await message.answer(users.text_all_task + tasks)
    else:
        await message.answer(users.text_all_task_no)
