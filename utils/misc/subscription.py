import logging
from typing import Union

from aiogram import Bot


async def check(user_id, channel_id: Union[int, str]):
    bot = Bot.get_current()
    member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)

    status = member.is_chat_member()
    logging.info(status)
    return status
