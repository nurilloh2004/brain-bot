from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile, ContentType
from loader import dp
from states.complaintData import ComplaintData
from keyboards.default.contact import contact_key
from keyboards.default.back import back_key
from keyboards.default.menu import menu
from aiogram.types import Message, CallbackQuery
from keyboards.default.offer_complaint import offer_complaint_key
from data.config import ADMINS, CHANNELS
from keyboards.inline.confirm import confirmation_keyboard, post_callback


@dp.message_handler(text="Таклиф ва шикоятлар")
async def worker(message: Message):
    await message.answer('👇 Қуйидагилардан бирини танланг', reply_markup=offer_complaint_key)


@dp.message_handler(text='Шикоят', state=None)
async def enter_name(message: types.Message):
    await message.answer("🙎‍♂️ Исм, Фамилия ва Шарифингизни киритинг!", reply_markup=back_key)
    await ComplaintData.name.set()


@dp.message_handler(state=ComplaintData.name)
async def worker_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    await message.answer("📝 Илтимос шикоятингизни аниқ равишда ёзинг!", reply_markup=back_key)
    await ComplaintData.next()


@dp.message_handler(state=ComplaintData.complaint)
async def worker_name(message: types.Message, state: FSMContext):
    complaint = message.text

    await state.update_data(
        {"complaint": complaint}
    )

    await message.answer('<b>📝Маълумотлар барчаси тўгрилигига эътибот қилинг</b>', reply_markup=menu)
    await ComplaintData.next()

    data = await state.get_data()
    name = data.get("name")
    complaint = data.get('complaint')

    msg = "<b>Қуйидаги маълумотлар қабул қилинди:</b>\n"
    msg += f"<b>👤 Ф.И.Ш:</b> -<code> {name}</code>\n"
    msg += f"<b>📝 Шикоят мазмуни:</b> -<code> {complaint}</code>\n"

    await message.answer(msg, reply_markup=confirmation_keyboard)
    await ComplaintData.next()


