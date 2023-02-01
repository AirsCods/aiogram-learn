from utils.set_bot_commands import set_default_commands
from aiogram import Dispatcher, executor
from handlers import dp
from utils.notify_admins import on_startup_notify


async def on_startup(dispathcer: Dispatcher):
    # import filters
    # import middlewares
    # filters.setup(dp)
    # middlewares.setup(dp)

    await on_startup_notify(dp)
    # await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
