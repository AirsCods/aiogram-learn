import logging

from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.inline import choice, pear_keyboard
from keyboards.inline.callback_datas import buy_callback
from loader import dp


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(
        text='На продажу у нас есть 2 товара: 5 Яблок и 1 Груша. \n'
             'Если вам ничего не нужно - жмите отмену.',
        reply_markup=choice
    )


@dp.callback_query_handler(buy_callback.filter(item_name='pear'))
async def buy_pear(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback data = {call.data}')
    logging.info(f'callback data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали купить груши. Груши всего {quantity}. Спасибо!',
                              reply_markup=pear_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='apple'))
async def buy_pear(call: types.CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f'callback data = {call.data}')
    logging.info(f'callback data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали купить яблоки. Яблок всего {quantity}. Спасибо!')


@dp.callback_query_handler(text='cancel')
async def cancel_buying(call: types.CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer('Вы отменили эту покупку!', show_alert=True)

    # Отправляем пустую клваиатуру изменяя сообщение, для того чтобы ее убрать из сообщения:
    await call.message.edit_reply_markup(reply_markup=None)
