import logging

from loader import db
from utils.db_api import db_gino


async def on_startup(dispatcher):
    import middlewares
    import filters
    middlewares.setup(dispatcher)
    filters.setup(dispatcher)

    # logging.info('Создаем подключение к базе данных')
    # await db.create()
    #
    # await db.drop_table_users()
    #
    # logging.info('Создаем таблицу пользователей')
    # await db.create_table_users()
    #
    logging.info('Подключаем БД')
    await db_gino.on_startup(dp)
    logging.info('Готово')

    logging.info('Чистим базу')
    await db.gino.drop_all()
    logging.info('Готово')

    logging.info('Создаем таблицы')
    await db.gino.create_all()
    logging.info('Готово')

    from utils.notify_admins import on_startup_notify
    from utils.set_bot_commands import set_default_commands

    await on_startup_notify(dispatcher)
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
