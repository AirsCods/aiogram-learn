from aiogram import types

from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    await dp.bot.send_message(
        chat_id=message.chat.id,
        text=message.text,
    )
    # await message.reply()
