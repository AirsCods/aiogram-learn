from aiogram import types

from loader import dp


@dp.channel_post_handler(content_types=types.ContentType.ANY)
async def new_post(message: types.Message):
    print(f'Опубликовано новое сообщение в канале {message.chat.title}\n'
          f'{message.text}')
