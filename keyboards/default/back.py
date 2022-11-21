from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back_key = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ],
    resize_keyboard=True
)

back_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [

            KeyboardButton(text='Отмена 🚫'),
        ]
    ],
    resize_keyboard=True
)

