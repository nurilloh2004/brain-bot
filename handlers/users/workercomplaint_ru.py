from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile, ContentType
from loader import dp
from states.complaintData_ru import ComplaintData_ru
from keyboards.default.contact import contact_key
from keyboards.default.back import back_key_ru
from keyboards.default.menu import menu
from aiogram.types import Message, CallbackQuery
from keyboards.default.offer_complaint import offer_complaint_key_ru
from data.config import ADMINS, CHANNELS
from keyboards.inline.confirm import confirmation_keyboard_ru, post_callback


@dp.message_handler(text='Жалоба', state=None)
async def enter_name(message: types.Message):
    await message.answer("🙎‍♂️ Введите свое имя, фамилию и фамилию:!", reply_markup=back_key_ru)
    await ComplaintData_ru.name.set()


@dp.message_handler(state=ComplaintData_ru.name)
async def worker_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    await message.answer("📝 Пишите свои жалобы четко!!", reply_markup=back_key_ru)
    await ComplaintData_ru.next()


@dp.message_handler(state=ComplaintData_ru.complaint)
async def worker_name(message: types.Message, state: FSMContext):
    complaint = message.text

    await state.update_data(
        {"complaint": complaint}
    )

    await message.answer('<b>📝 Убедитесь, что вся информация верна</b>', reply_markup=menu)
    await ComplaintData_ru.next()

    data = await state.get_data()
    name = data.get("name")
    complaint = data.get('complaint')

    msg = "<b>Была получена следующая информация:</b>\n"
    msg += f"<b>👤 Ф.И.O:</b> -<code> {name}</code>\n"
    msg += f"<b>📝 Жалобы:</b> -<code> {complaint}</code>\n"

    await message.answer(msg, reply_markup=confirmation_keyboard_ru)
    await ComplaintData_ru.next()



