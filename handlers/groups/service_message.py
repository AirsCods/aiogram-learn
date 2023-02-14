from aiogram import types

from loader import dp


# В группу добавился новый пользователь
@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):

    # Собираем в строку новых пользователей
    members = ', '.join([member.get_mention(as_html=True) for member in message.new_chat_members])
    await message.reply(f'Привет, {members}.')


# Пользователь вышел или удален из группы
@dp.message_handler(content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def last_member(message: types.Message):

    # Пользователь вышел сам
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f'{message.left_chat_member.get_mention(as_html=True)} вышел из чата.')

    # Пользователя удалил бот
    elif message.from_user.id == (await dp.bot.me).id:
        await message.answer(f'{message.left_chat_member.full_name} был удален ботом.')

    # Пользователя удалил другой пользователь
    else:
        await message.answer(f'{message.left_chat_member.full_name} был удален из чата '
                             f'пользователем {message.from_user.full_name}.')
