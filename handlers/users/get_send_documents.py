import logging
from io import BytesIO

from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentTypes.AUDIO)
async def get_audio(message: types.Message):
    file_id = message.audio.file_id
    logging.info('Get audio id')

    await message.answer(f'ID аудиозаписи: {file_id}')


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def convert_photo_to_document(message: types.Message):
    save_to_io = BytesIO()
    await message.photo[-1].download(destination=save_to_io)
    await message.answer_document(types.InputFile(save_to_io, filename='photo_from_io.jpg'))


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def convert_document_to_photo(message: types.Message):
    save_to_io = BytesIO()
    await message.document.download(destination=save_to_io)
    await message.answer_photo(types.InputFile(save_to_io))
