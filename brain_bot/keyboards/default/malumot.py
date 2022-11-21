from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

malumot_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Олий'),
            KeyboardButton(text='Магистратура'),
        ],
        [
            KeyboardButton(text='Талаба'),
            KeyboardButton(text='Ўрта махсус'),
        ],
        [
            KeyboardButton(text='Ўрта')
        ],
        [
            # KeyboardButton(text='Orqaga ↩️'),
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ],
    resize_keyboard=True
)

malumot_keyboard_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Oбразование'),
            KeyboardButton(text='Магистра'),
        ],
        [
            KeyboardButton(text='Cтудент'),
            KeyboardButton(text='Cреднее специальнoe'),
        ],
        [
            KeyboardButton(text='Середина')
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]
    ],
    resize_keyboard=True
)