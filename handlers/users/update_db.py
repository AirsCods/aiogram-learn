from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hcode

from loader import dp, db


@dp.message_handler(Command('update_username'))
async def update_username(message: types.Message, state: FSMContext):
    await message.answer('Пришли свой новый username')
    await state.set_state('username')


@dp.message_handler(state='username')
async def enter_username(message: types.Message, state: FSMContext):
    await db.update_user_name(username=message.text, telegram_id=message.from_user.id)
    user = await db.select_user(telegram_id=message.from_user.id)
    user = dict(user)
    await message.answer('Данная запись в базе данных\n' + hcode(f'{user=}'))
