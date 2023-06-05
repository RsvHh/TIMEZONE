from static.text import users
from utils.db_api import db_task
from loader import bot


async def check_task():
    tasks = await db_task.return_all()
    if tasks:
        for task in tasks:
            if await db_task.check_time(task.id):
                await bot.send_message(task.user_id, users.text_task_example.format(task.name))
