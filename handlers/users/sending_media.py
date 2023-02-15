import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo_id(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_photo_id(message: types.Message):
    await message.reply(message.video.file_id)


# Send photo
@dp.message_handler(Command('get_cat'))
async def send_cat(message: types.Message):
    logging.info('Command /get_cat')
    await dp.bot.send_photo(chat_id=message.from_user.id,
                            photo='AgACAgIAAxkBAAIB0GPslwFX_1zmMVjIkrxUXWtrRkKBAAKIxjEbAAHKaEsin2jJPAVQRwEAAwIAA3gAAy4E',
                            caption='Вот тебе фото кота /more_cats')


# Send albums
@dp.message_handler(Command('more_cats'))
async def more_cats(message: types.Message):
    logging.info('Command /more_cats')
    album = types.MediaGroup()
    photo_file_id = 'AgACAgIAAxkBAAIB1GPslxvJpa3cmqW9udA-F5X6hnLiAAKJxjEbAAHKaEtkEPyLTB2p2wEAAwIAA3kAAy4E'
    # photo_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FCat&psig=AOvVaw2VmnU-B3jHVec6JtC0Z3Je&ust=1676534670247000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCOiH3cyIl_0CFQAAAAAdAAAAABAD'
    photo_bytes = InputFile(path_or_bytesio='src/photo/alian.jpg')
    video_file_id = 'BAACAgIAAxkBAAIB0mPslxBz3MdVKTsPX9tW0SZj70A0AAJfJAADymhLntswZEUoNMouBA'
    album.attach_photo(photo_file_id)
    album.attach_photo(photo_bytes)
    # album.attach_photo(photo_url)
    album.attach_video(video_file_id, caption='Ееее видос!')

    # await dp.bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)
