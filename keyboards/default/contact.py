from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact_key = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text="📱 Рақам юбориш",request_contact=True)
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ]
)

contact_key_ru = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(
                text="📱 Отправить номер",request_contact=True)
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]
    ]
)