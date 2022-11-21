from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

nothing_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ҳеч қаерда ишламаганман'),

        ],
        [

            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ],
    resize_keyboard=True
)

nothing_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я нигде не работал'),

        ],
        [

            KeyboardButton(text='Отмена 🚫'),
        ]
    ],
    resize_keyboard=True
)