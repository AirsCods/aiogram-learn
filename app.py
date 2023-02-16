import logging

from loader import dp, db


async def on_startup(dispatcher):
    import middlewares
    import filters
    middlewares.setup(dispatcher)
    filters.setup(dispatcher)

    logging.info('Создаем подключение к базе данных')
    await db.create()

    logging.info('Создаем таблицу пользователей')
    await db.create_table_users()

    from utils.notify_admins import on_startup_notify
    from utils.set_bot_commands import set_default_commands

    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, on_startup=on_startup)
