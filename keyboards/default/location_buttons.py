from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Send Location',
                request_location=True
            )
        ]
    ],
    resize_keyboard=True
)
