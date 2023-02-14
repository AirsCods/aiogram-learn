import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import AdminFilter, IsGroup
from loader import dp


@dp.message_handler(IsGroup(), Command('set_photo', prefixes='!/'), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    if not source_message:
        return await message.reply("Использовать эту команду можно только ответом на сообщение!")

    photo = source_message.photo[-1]

    # Сохраняю фото в оперативной памяти в байтах при помощи download(destination=io.BytesIO())
    photo = await photo.download(destination=io.BytesIO())

    # Создаю файл для вставки, буре его содержимое из оперативной памяти в виде байт
    input_file = types.InputFile(path_or_bytesio=photo)

    # Задаю фото для чата
    # await dp.bot.set_chat_photo(chat_id=message.chat.id, photo=input_file)
    await message.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command('set_title', prefixes='!/'), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    if not source_message:
        return await message.reply("Использовать эту команду можно только ответом на сообщение!")
    title = source_message.text
    await message.chat.set_title(title=title)


@dp.message_handler(IsGroup(), Command('set_description', prefixes='!/'), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    if not source_message:
        return await message.reply("Использовать эту команду можно только ответом на сообщение!")
    description = source_message.text
    await message.chat.set_description(description=description)
