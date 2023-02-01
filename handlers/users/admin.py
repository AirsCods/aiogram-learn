from aiogram import types
from filters import IsPrivate
from loader import dp


@dp.message_handler(IsPrivate(), text='secret')
@dp.message_handler(IsPrivate(), text='admin')
async def admin_chat_secret(message: types.Message):
    await message.answer('Это скеретное сообщение, вызванное одним из администраторов'
                         'в личной переписке')
