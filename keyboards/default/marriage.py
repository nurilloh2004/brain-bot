from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

married = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Турмуш қурганман'),
            KeyboardButton(text='Турмуш қурмаганман'),
        ],
        [
            # KeyboardButton(text='Orqaga ↩️'),
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ],
    resize_keyboard=True
)

married_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Женат (замужем)'),
            KeyboardButton(text='Не женат (не замужем)'),
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]
    ],
    resize_keyboard=True
)