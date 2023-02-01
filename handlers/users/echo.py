from aiogram import types

from loader import dp, bot


@dp.message_handler()
async def bot_echo(message: types.Message):
    bot.send_message(
        chat_id=message.chat.id,
        text=message.text,
    )
    # await message.reply()
