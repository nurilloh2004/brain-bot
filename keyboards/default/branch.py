from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

branch_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Фарғона'),
            KeyboardButton(text='Қўқон'),
            KeyboardButton(text='Тошкент'),
        ],
        [
            # KeyboardButton(text='Orqaga ↩️'),
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ],
    resize_keyboard=True
)

branch_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Фергана'),
            KeyboardButton(text='Коканд'),
            KeyboardButton(text='Тошкент'),
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]
    ],
    resize_keyboard=True
)