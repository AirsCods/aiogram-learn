# from utils.set_bot_commands import set_default_commands
from aiogram import Dispatcher, executor

import filters
import handlers
from loader import dp
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher: Dispatcher):
    # import filters
    # import middlewares
    # filters.setup(dp)
    # middlewares.setup(dp)

    # Уведомляет при запуске
    await on_startup_notify(dispatcher)
    # await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
