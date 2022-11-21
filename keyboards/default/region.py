from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

region_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Тошкент Шахар'),
        ],
        [
            KeyboardButton(text='Бешариқ Шахар'),
            KeyboardButton(text='Боғдод Шахар'),
        ],
        [
            KeyboardButton(text='Бувайда Шахар'),
            KeyboardButton(text='Данғара Шахар'),
        ],
        [
            KeyboardButton(text='Ёзёвой Шахар'),
            KeyboardButton(text='Қува Шахар'),
        ],
        [
            KeyboardButton(text='Қувасой Шахар'),
            KeyboardButton(text='Қўқон Шахар'),
        ],
        [
            KeyboardButton(text='Қўштепа Шахар'),
            KeyboardButton(text='Марғилон Шахар'),
        ],
        [
            KeyboardButton(text='Олтиариқ Шахар'),
            KeyboardButton(text='Риштон Шахар'),
        ],
        [
            KeyboardButton(text='Сўх Шахар'),
            KeyboardButton(text='Тошлоқ Шахар'),
        ],
        [
            KeyboardButton(text='Учкўприк Шахар'),
            KeyboardButton(text='Ўзбекистон Шахар'),
        ],
        [
            KeyboardButton(text='Фарғона Шахар'),
            KeyboardButton(text='Фарғона Шахар'),
        ],
        [
            KeyboardButton(text='Фурқат Шахар'),
        ],
        [
            # KeyboardButton(text='Orqaga ↩️'),
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]
    ],
    resize_keyboard=True
)


region_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Бешарик'),
            KeyboardButton(text='Багдад'),
        ],
        [
            KeyboardButton(text='Бувайда '),
            KeyboardButton(text='Дангара'),
        ],
        [
            KeyboardButton(text='Ёзёвой'),
            KeyboardButton(text='Кува'),
        ],
        [
            KeyboardButton(text='Кувасой'),
            KeyboardButton(text='Коканд'),
        ],
        [
            KeyboardButton(text='Коштепа'),
            KeyboardButton(text='Маргилан'),
        ],
        [
            KeyboardButton(text='Алтыарик'),
            KeyboardButton(text='Риштон'),
        ],
        [
            KeyboardButton(text='Сох'),
            KeyboardButton(text='Тошлок'),
        ],
        [
            KeyboardButton(text='Учкуприк'),
            KeyboardButton(text='Район Узбекистана'),
        ],
        [
            KeyboardButton(text='Ферганский район'),
            KeyboardButton(text='Фергана'),
        ],
        [
            KeyboardButton(text='Фуркатский район'),
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]
    ],
    resize_keyboard=True
)