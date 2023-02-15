from aiogram import types

from data.config import DOWNLOAD_PATH
from loader import dp


@dp.message_handler()
async def cath_text(message: types.Message):
    await message.answer('Вы прилали текст')


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def cath_document(message: types.Message):
    await message.document.download(destination_dir=DOWNLOAD_PATH)
    await message.answer('Вы прилали документ. Он был скачан.\n'
                         f'<pre>FILE ID = {message.document.file_id}</pre>',
                         parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.AUDIO)
async def cath_audio(message: types.Message):
    await message.audio.download(destination_dir=DOWNLOAD_PATH)
    await message.answer('Вы прилали аудиофайл. Он был скачан.\n'
                         f'<pre>FILE ID = {message.audio.file_id}</pre>',
                         parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def cath_video(message: types.Message):
    await message.video.download(destination_dir=DOWNLOAD_PATH)
    await message.answer('Вы прилали видеофайл. Он был скачан.\n'
                         f'<pre>FILE ID = {message.video.file_id}</pre>',
                         parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def cath_photo(message: types.Message):
    await message.photo[-1].download(destination_dir=DOWNLOAD_PATH)
    await message.answer('Вы прилали фото. Оно был скачан.\n'
                         f'<pre>FILE ID = {message.photo[-1].file_id}</pre>',
                         parse_mode='HTML')


@dp.message_handler(content_types=types.ContentType.ANY)
async def cath_any(message: types.Message):
    await message.answer(f'Вы прислали ... {message.content_type}')
