from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher):
    await dp.bot.set_my_commands([
        # types.BotCommand('channels', 'Список каналов на подписку.'),
        # types.BotCommand('create_post', 'Предложить пост в канале.'),
        types.BotCommand('get_cat', 'Прислать кота.'),
        types.BotCommand('more_cats', 'Прислать больше.'),
        types.BotCommand('show_on_map', 'Локация'),
        types.BotCommand('callback', 'Номерок'),
        types.BotCommand('update_email', 'Обновка'),
    ])
