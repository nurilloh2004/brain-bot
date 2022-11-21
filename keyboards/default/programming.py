from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

programming_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Office Дастурлари'),
            KeyboardButton(text='PhotoShop'),
        ],

        [
            KeyboardButton(text='CorlDraw'),
            KeyboardButton(text='3dMax'),
        ],
        [
            KeyboardButton(text='1C'),
        ],
        [
            KeyboardButton(text='Дастурлаш тиллари'),
        ],
        [
            # KeyboardButton(text='Orqaga ↩️'),
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]

    ],
    resize_keyboard=True
)



programming_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Офисные программы'),
            KeyboardButton(text='PhotoShop'),
        ],
[
            KeyboardButton(text='CorelDraw'),
            KeyboardButton(text='3dMax'),
        ],
        [
            KeyboardButton(text='1C'),
        ],
        [
            KeyboardButton(text='Языки программирования'),
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]

    ],
    resize_keyboard=True
)