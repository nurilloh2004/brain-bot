from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile
from keyboards.default.menu import menu, about, about_ru
import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

        text = '<b>🇺🇿 Ассалому алайкум.\nБарака савдо марказининг ишга қабул қилиш тизимига хуш келибсиз.</b>\n'
        text += '<b>Берилган саволларга тўлиқ ва аниқ жавоб беришингиз\nсизнинг ишга қабул қилинишингизга асос бўлади.\nТилни танланг!</b>\n\n'
        text += '-------------------------------------------------------------------------------------\n\n'
        text += '<b>🇷🇺 Привет.\nДобро пожаловать в систему набора персонала ТЦ Барака.\nПолные и точные ответы на вопросы</b>\n'
        text += '<b>будет основанием для вашего трудоустройства.\nВыбери язык!</b>\n'

    await message.answer(text, reply_markup=menu)
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)



@dp.message_handler(text='🇺🇿 Ўзбек ✅')
async def uzbek(message:Message):
    text = '<b>Сиз ишга кириш бўйича мурожат қилаётган бўлсангиз <b>Вакант</b> тугмасини босинг!</b>\n\n'
    text += '<b>Бизнинг ташкилотда ҳодим бўлсангиз <b>Ҳодимлар</b> учун тумасини босинг!</b>\n\n'
    await message.answer(text,
                         reply_markup=about
                         )

@dp.message_handler(text='🇷🇺 Рус ✅')
async def uzbek(message:Message):
    text = '<b>Если вы подаете заявление о приеме на работу, нажмите кнопку «На вакансии»!</b>\n\n'
    text += '<b>Если вы являетесь сотрудником нашей организации, нажмите на кнопку « Для сотрудников»!</b>\n\n'
    await message.answer(text,
                         reply_markup=about_ru
                         )

