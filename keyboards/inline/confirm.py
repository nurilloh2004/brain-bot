from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_callback = CallbackData("create_post", "action")

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Тасдиқлаш", callback_data=post_callback.new(action="post")),
        InlineKeyboardButton(text="❌ Бекор қилиш", callback_data=post_callback.new(action="cancel")),
    ]]
)

confirmation_keyboard_ru = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="🆗 Подтверждение", callback_data=post_callback.new(action="post_ru")),
        InlineKeyboardButton(text="❌ Отмена", callback_data=post_callback.new(action="cancel_ru")),
    ]]
)