from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

offer_complaint_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Таклиф'),
            KeyboardButton(text='Шикоят'),
        ],
    ],
    resize_keyboard=True
)

offer_complaint_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Предложение'),
            KeyboardButton(text='Жалоба'),
        ],
    ],
    resize_keyboard=True
)