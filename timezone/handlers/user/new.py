from loader import dp
from data.config import admins_id
from aiogram import types
from utils.inline_btn import create_markup
from static.text import users
from aiogram.dispatcher import FSMContext
from utils.db_api import db_task
from handlers.user.start import UserState


@dp.message_handler(regexp='Додати новий')
async def all_task_message(message: types.Message):
    await UserState.new_task.set()
    markup = await create_markup('reply', 1, ['Назад'])
    await message.answer(users.text_new_task, reply_markup=markup)


@dp.message_handler(state=UserState.new_task, regexp='Назад')
async def all_task_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    MAIN_MARKUP = await create_markup('reply', 2, ['Подивитися список'], ['Додати новий'], ['Очистити список'])
    await message.answer(users.text_cancel, reply_markup=MAIN_MARKUP)


@dp.message_handler(state=UserState.new_task)
async def all_task(message: types.Message, state: FSMContext):
    try:
        if len(message.text.split(' ')) >= 2:
            data = message.text.split(' ')
            task, time = ' '.join(message.text.split(' ')[:-1]), ':'.join([str(int(x)) for x in
                                                                           message.text.split(' ')[-1].split(':')])
            await db_task.add_task(message.chat.id, time, task)
            MAIN_MARKUP = await create_markup('reply', 2, ['Подивитися список'], ['Додати новий'], ['Очистити список'])
            await message.answer(users.text_new_task_ok, reply_markup=MAIN_MARKUP)
            await state.finish()
        else:
            print(2 // 0)
    except Exception:
        await message.reply(users.text_error)
