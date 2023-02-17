from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hcode

from loader import dp
from utils.db_api import quick_commands as commands


# @dp.message_handler(Command('update_username'))
# async def update_username(message: types.Message, state: FSMContext):
#     await message.answer('Пришли свой новый username')
#     await state.set_state('username')
#
#
# @dp.message_handler(state='username')
# async def enter_username(message: types.Message, state: FSMContext):
#     await db.update_user_name(username=message.text, telegram_id=message.from_user.id)
#     user = await db.select_user(telegram_id=message.from_user.id)
#     user = dict(user)
#     await message.answer('Данная запись в базе данных\n' + hcode(f'{user=}'))

@dp.message_handler(Command('update_email'))
async def update_username(message: types.Message, state: FSMContext):
    await message.answer('Пришли свой новый email')
    await state.set_state('email')


@dp.message_handler(state='email')
async def enter_username(message: types.Message, state: FSMContext):
    email = message.text
    await commands.update_user_email(email=email, id=message.from_user.id)
    user = await commands.select_user(id=message.from_user.id)
    await message.answer('Данные обновлены. Запись в БД: \n' +
                         hcode(f'id={user.id}\n'
                               f'name={user.name}\n'
                               f'email={user.email}'))
    await state.finish()