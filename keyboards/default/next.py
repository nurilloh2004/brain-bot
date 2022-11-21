from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

next_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ўтказиб юбориш'),

        ],
        [

            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ],
    resize_keyboard=True
)

next_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Пропускать'),

        ],
        [

            KeyboardButton(text='Отмена 🚫'),
        ]
    ],
    resize_keyboard=True
)