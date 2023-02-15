from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('my_id'))
async def get_user_id(message: types.Message):
    await message.answer(f'You ID: {message.from_user.id}')
