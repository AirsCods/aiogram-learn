from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Купить грушу',
                callback_data=buy_callback.new(
                    item_name="pear",
                    quantity=1
                ),
            ),
            InlineKeyboardButton(
                text='Купить яблоки',
                callback_data=buy_callback.new(
                    item_name="apple",
                    quantity=5
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ]
    ]
)

# Второй вариант создания кнопок
pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = 'https://ru.wikipedia.org/wiki/%D0%93%D1%80%D1%83%D1%88%D0%B0'

pear_link = InlineKeyboardButton(text='Купи тут', url=PEAR_LINK)

pear_keyboard.insert(pear_link)
