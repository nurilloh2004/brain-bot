from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🇺🇿 Ўзбек ✅'),
            KeyboardButton(text='🇷🇺 Рус ✅'),
        ],
    ],
    resize_keyboard=True
)
about = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👨‍🎓 Вакантлар учун'),
            KeyboardButton(text='🤵‍♂️ Ҳодимлар учун')
        ]
    ], resize_keyboard=True
)

about_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👨‍🎓 На вакансии'),
            KeyboardButton(text='🤵‍♂️ Для сотрудников')
        ]
    ], resize_keyboard=True
)
