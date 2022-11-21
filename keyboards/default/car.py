from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

car_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Бор'),
            KeyboardButton(text='Йўқ')
        ],
        [

            KeyboardButton(text='Бекор қилиш 🚫')
        ]
    ],
    resize_keyboard=True
)

car_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Да'),
            KeyboardButton(text='Нет')
        ],
        [

            KeyboardButton(text='Отмена 🚫')
        ]
    ],
    resize_keyboard=True
)
