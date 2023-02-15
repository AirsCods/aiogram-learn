from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import admins, channels
from keyboards.inline import confirmation_keyboard
from keyboards.inline.manage_post import post_callback
from loader import dp
from states import NewPost


@dp.message_handler(Command('create_post'))
async def create_post(message: types.Message):
    await message.answer('Отправьте мне текст на публикацию')
    await NewPost.EnterMessage.set()


@dp.message_handler(state=NewPost.EnterMessage)
async def enter_message(message: types.Message, state: FSMContext):
    await state.update_data(
        text=message.html_text,
        mention=message.from_user.get_mention(as_html=True)
    )
    await message.answer(
        text='Вы собираетесь отправить пост на проверку?',
        reply_markup=confirmation_keyboard)
    await NewPost.Confirm.set()


@dp.callback_query_handler(post_callback.filter(action='post'), state=NewPost.Confirm)
async def confirm_post(call: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        text = data.get('text')
        mention = data.get('mention')
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Вы отправили пост на проверку')

    await dp.bot.send_message(chat_id=admins[0], text=f'Пользователь {mention} хочет сделать пост:')
    await dp.bot.send_message(chat_id=admins[0], text=text, parse_mode='HTML', reply_markup=confirmation_keyboard)


@dp.callback_query_handler(post_callback.filter(action='cancel'), state=NewPost.Confirm)
async def cancel_post(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Вы отменили отправку поста')


@dp.message_handler(state=NewPost.Confirm)
async def post_unknown(message: types.Message):
    await message.answer('Выберите опубликовать или отложить пост')


@dp.callback_query_handler(post_callback.filter(action='post'), user_id=admins)
async def approve_post(call: types.CallbackQuery):
    await call.answer('Вы одобрили этот пост.', show_alert=True)
    target_channel = channels[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action='cancel'), user_id=admins)
async def decline_post(call: types.CallbackQuery):
    await call.answer('Вы отклонили этот пост.', show_alert=True)
    await call.message.edit_reply_markup()
