from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

branch_position_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Лавозим ва Филиал ўзгартириш'),
        ],
        [
            KeyboardButton(text='Таклиф ва шикоятлар'),

        ],
    ],
    resize_keyboard=True
)
branch_position_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Смена должности и отделения'),
        ],
        [
            KeyboardButton(text='Предложения и жалобы'),

        ],
    ],
    resize_keyboard=True
)