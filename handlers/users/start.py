import logging

import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Command

from loader import dp, db


@dp.message_handler(Command('start'))
async def bot_start(message: types.Message):
    try:
        logging.info(f'Добавляю пользователя в базу данных.')
        user = await db.add_user(
            full_name=message.from_user.full_name,
            username=message.from_user.username,
            telegram_id=message.from_user.id
        )
    except asyncpg.exceptions.UniqueViolationError as err:
        logging.exception(f'Пользователь уже существует в базе!\n{err}')
        user = await db.select_user(telegram_id=message.from_user.id)

    count_users = await db.count_users()
    logging.info(count_users)
    user_data = list(user)
    user_data_dict = dict(user)

    username = user.get('username')
    full_name = user.get('full_name')
    logging.info('Отправляю пользователю сообщение в тг')

    await message.answer(
        '\n'.join(
            [
                f'Привет, {message.from_user.full_name}',
                f'Ты был записан в базу',
                f'В базе <b>{count_users}</b> пользователей',
                '',
                '',
                f'<code>User: {username} - {full_name}',
                f'{user_data=}',
                f'{user_data_dict=}</code>'
            ]
        )
    )
