import asyncio

from data import config
from utils.db_api import quick_commands as commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URL)
    print(config.POSTGRES_URL)
    await db.gino.drop_all()
    await db.gino.create_all()

    print('Добавляем пользователей')
    await commands.add_user(1, 'One', 'email')
    await commands.add_user(2, 'Vasya', 'gmail.com')
    await commands.add_user(3, '3', 'mail')
    await commands.add_user(4, '4', '4mail')
    await commands.add_user(5, 'John', 'johm@gmail.com')
    print('Готово')

    users = await commands.select_all_users()
    print(f'Все пользователи: {users}')

    count_users = await commands.count_users()
    print(f'Всего пользователей: {count_users}')

    user = await commands.select_user(id=5)
    print(f'Полученный пользователь: {user}')


loop = asyncio.get_event_loop()
loop.run_until_complete(test())
