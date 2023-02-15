from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import allowed_users
from loader import dp


@dp.inline_handler(text='')
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id='unknown',
                title='Введите какой то запрос',
                input_message_content=types.InputTextMessageContent(
                    message_text='Сначала введи, а потом уже жми, понятненько.',
                )
            )
        ],
        cache_time=5
    )


@dp.inline_handler()
async def some_query(query: types.InlineQuery):
    user = query.from_user.id
    if user not in allowed_users:
        await query.answer(
            results=[],
            switch_pm_text='Бот недоступен. Подключить бота.',
            switch_pm_parameter='connect_user',
            cache_time=5
        )
        return

    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id='1',
                title='Название, которое отображается в инлайн режиме!',
                input_message_content=types.InputTextMessageContent(
                    message_text='Какой то текст которые будет отправлени при нажатии на кнопку'
                ),
                url='https://core.telegram.org/bots/api#inlinequeryresult',
                thumb_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fimagekit.io%2Fblog%2Fwhat-is-image-cdn-guide%2F&psig=AOvVaw1-1LfVBsxrCgW0UFvmiEyu&ust=1676551073907000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCIC_msvFl_0CFQAAAAAdAAAAABAI',
                description='Описание, в инлайн режиме'
            ),
            types.InlineQueryResultVideo(
                id='4',
                video_url='https://pixabay.com/en/videos/download/video-10737_medium.mp4',
                caption='Подпись к видео',
                title='Название видео',
                description='Описание видео',
                thumb_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fimagekit.io%2Fblog%2Fwhat-is-image-cdn-guide%2F&psig=AOvVaw1-1LfVBsxrCgW0UFvmiEyu&ust=1676551073907000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCIC_msvFl_0CFQAAAAAdAAAAABAI',
                mime_type='video/mp4'
            )
        ]
    )


@dp.message_handler(CommandStart(deep_link='connect_user'))
async def connect_user(message: types.Message):
    allowed_users.append(message.from_user.id)
    await message.answer('Вы подключены.',
                         reply_markup=InlineKeyboardMarkup(
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(text='Войти в инлайн режим',
                                                          switch_inline_query_current_chat='Запрос')
                                 ]
                             ]
                         ))
