from apscheduler.schedulers.asyncio import AsyncIOScheduler
from utils.schedy import check_task


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_task, 'interval', minutes=1)
    scheduler.start()

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)