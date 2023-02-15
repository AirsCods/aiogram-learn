import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

from keyboards.default import contact_buttons
from loader import dp


@dp.message_handler(Command('callback'))
async def share_number(message: types.Message):
    await message.answer(
        f'Здравствуйте, {message.from_user.full_name}.\n'
        f'Для того, чтобы мы вам звонили, дай нам свой номер телефона нажав на кнопку нижу!',
        reply_markup=contact_buttons.keyboard,
    )
    logging.info('Запросили номерок')


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def share_number(message: types.Message):
    contact = message.contact
    await message.answer(
        f'Спасибо, {contact.full_name}\n'
        f'Ваш номер {contact.phone_number} был получен и передан куда надо. Ожидайте!',
        reply_markup=ReplyKeyboardRemove()
    )
