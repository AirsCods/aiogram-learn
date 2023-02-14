import asyncio
import datetime
import re

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from filters import IsGroup, AdminFilter
from loader import dp


@dp.message_handler(IsGroup(), Command('ro', prefixes='!/'), AdminFilter())
async def read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user

    command_parse = re.compile(r'(!ro|/ro) ?(\d+)? ?([a-zA-Z ]+)?')
    parsed = command_parse.match(message.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    else:
        time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    read_only_permissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_media_messages=False,
        can_send_polls=False,
        can_send_other_messages=False,
        can_add_web_page_previews=False,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )
    try:
        await message.chat.restrict(user_id=member.id, permissions=read_only_permissions, until_date=until_date)
        await message.reply(f'Ползавателю {member.full_name} запрещено писать на {time} минут. Потому что: {comment}')

    except BadRequest:
        await message.answer('Пользователь является администратором!')

    service_message = await message.reply('Сообщение самоуничтожиться через 5 секунд.')
    await asyncio.sleep(5)
    await message.delete()
    await service_message.delete()


@dp.message_handler(IsGroup(), Command('un_ro', prefixes='!/'), AdminFilter())
async def undo_read_only_mode(message: types.Message):
    member = message.reply_to_message.from_user

    user_allowed = types.ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
        can_change_info=False,
        can_pin_messages=False,
    )

    await message.chat.restrict(user_id=member.id, permissions=user_allowed, until_date=0)
    await message.reply(f'Пользователь {member.full_name} был размьючен!')


@dp.message_handler(IsGroup(), Command('ban', prefixes='!/'), AdminFilter())
async def ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    await message.chat.kick(user_id=member.id)
    await message.reply(f'Пользователь {member.full_name} был забанен!')


@dp.message_handler(IsGroup(), Command('un_ban', prefixes='!/'), AdminFilter())
async def undo_ban_user(message: types.Message):
    member = message.reply_to_message.from_user
    await message.chat.unban(user_id=member.id)
    await message.reply(f'Пользователь {member.full_name} был разбанен!')
