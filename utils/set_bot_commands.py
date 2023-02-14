from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('menu', 'Открыть меню.'),
        # types.BotCommand('help', 'Помощь.'),
        types.BotCommand('set_photo', 'Установить фото в чате.'),
        types.BotCommand('set_title', 'Установить название группы.'),
        types.BotCommand('set_description', 'Установить описание группы.'),
        types.BotCommand('ro', 'Режим Read Only.'),
        types.BotCommand('un_ro', 'Отключить Read Only.'),
        types.BotCommand('ban', 'Забанить.'),
        types.BotCommand('un_ban', 'Разбанить.'),
    ])
