from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

position_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Шартнома  расмийлаштирувчи'),
            KeyboardButton(text='Ундирувчи'),
        ],
        [
            KeyboardButton(text='Кассир'),
            KeyboardButton(text='Маслахатчи  (сотувчи)'),
        ],
        [
            KeyboardButton(text='Мерчендайзер'),
            KeyboardButton(text='Юрист'),
        ],
        [
            KeyboardButton(text='Ундирув оператори'),
            KeyboardButton(text='Реклама агенти'),
        ],
        [
            KeyboardButton(text='Юк ташувчи'),
            KeyboardButton(text='График дизайнер'),
        ],
        [
            KeyboardButton(text='Юк юкловчи'),
            KeyboardButton(text='Call центр оператори'),
        ],
        [
            KeyboardButton(text='Ошпаз'),
            KeyboardButton(text='Ошпаз ёрдамчиси'),

        ],
        [
            KeyboardButton(text='Сервис ҳодим'),
            KeyboardButton(text='Ресепшен')
        ],
        [
            KeyboardButton(text='Тозаловчи (фаррош)'),
        ],
        [
            KeyboardButton(text='Бекор қилиш 🚫'),
        ]

    ],
    resize_keyboard=True
)

position_key_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Исполнитель контракта'),
            KeyboardButton(text='Pекрутер'),
        ],
[
            KeyboardButton(text='Кассep'),
            KeyboardButton(text='Консультант (продавец)'),
        ],
[
            KeyboardButton(text='Мерчендайзер'),
            KeyboardButton(text='Юрист'),
        ],
        [
            KeyboardButton(text='Принимающий оператор'),
            KeyboardButton(text='Рекламный агент'),
        ],
        [
            KeyboardButton(text='Графический дизайнер'),
            KeyboardButton(text='Грузчик'),
        ],
        [
            KeyboardButton(text='Перевозчик'),
            KeyboardButton(text='Операторы колл-центра'),
        ],
        [
            KeyboardButton(text='Повар'),
            KeyboardButton(text='Помощник повара'),
        ],
        [
            KeyboardButton(text='Сервисный работник'),
            KeyboardButton(text='Ресепшен')
        ],
        [
            KeyboardButton(text='Очиститель'),
        ],
        [
            # KeyboardButton(text='Назад ↩️'),
            KeyboardButton(text='Отмена 🚫'),
        ]

    ],
    resize_keyboard=True
)