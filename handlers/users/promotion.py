from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import channels
from filters import IsPrivate, IsForwarded
from keyboards.inline import check_button
from loader import dp, bot
from utils.misc import subscription


@dp.message_handler(IsPrivate(), IsForwarded(), content_types=types.ContentType.ANY)
async def get_channel_info(message: types.Message):
    await message.answer(f'Сообщение было прислано из канала {message.forward_from_chat.title}.\n'
                         f'Username channel: @{message.forward_from_chat.username}\n'
                         f'ID channel: {message.forward_from_chat.id}')


@dp.message_handler(IsPrivate(), Command('channels'))
async def show_channels(message: types.Message):
    channels_format = str()
    for channel_id in channels:
        chat = await dp.bot.get_chat(channel_id)

        invite_link = await chat.export_invite_link()

        channels_format += f'Канал <a href=\'{invite_link}\'>{chat.title}</a>\n\n'

    await message.answer(
        f'Вам необходимо подписаться на следующие каналы:\n{channels_format}',
        reply_markup=check_button,
        disable_web_page_preview=True
    )


@dp.callback_query_handler(text='check_subs')
async def checker(call: types.CallbackQuery):
    await call.answer()
    # await call.message.edit_reply_markup()

    result = str()
    for channel_id in channels:

        status = await subscription.check(
            user_id=call.from_user.id,
            channel_id=channel_id
        )

        channel = await bot.get_chat(channel_id)
        if status:
            result += f'Подписка на канал <b>{channel.title}</b> Оформлена!\n\n'

        else:
            invite_link = await channel.export_invite_link()
            result += f'Подписка на канал <b>{channel.title}</b> Не оформлена! <a href="{invite_link}">Подпишись!</a>\n\n'

    await call.message.answer(text=result, disable_web_page_preview=True)
