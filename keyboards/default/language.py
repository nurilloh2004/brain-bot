from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ўзбек'),
            KeyboardButton(text='Ўзбек/Рус'),
        ],
        [
            KeyboardButton(text='Ўзбек/Энг')
        ],
        [
            KeyboardButton(text='Ўзбек/Рус/Энг'),
        ],
        [
            # KeyboardButton(text='Orqaga ↩️'),
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]

    ],
    resize_keyboard=True
)


language_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Узбекский'),
            KeyboardButton(text='Узбекский/Pусский'),
        ],
        [
            KeyboardButton(text='Узбекский/Aнглийский')
        ],
        [
            KeyboardButton(text='Узбекский/Aнглийский/Pусский')
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]

    ],
    resize_keyboard=True
)