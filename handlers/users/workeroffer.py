from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile, ContentType
from loader import dp
from states.offerData import OfferData
from keyboards.default.contact import contact_key
from keyboards.default.back import back_key
from keyboards.default.menu import menu
from aiogram.types import Message, CallbackQuery
from keyboards.default.offer_complaint import offer_complaint_key
from data.config import ADMINS, CHANNELS
from keyboards.inline.confirm import confirmation_keyboard, post_callback

@dp.message_handler(text="Таклиф ва шикоятлар")
async def worker(message: Message):
    await message.answer('Қуйидагилардан бирини танланг', reply_markup=offer_complaint_key)



@dp.message_handler(text='Таклиф', state=None)
async def enter_name(message: types.Message):
    await message.answer("🙎‍♂️ Исм, Фамилия ва Шарифингизни киритинг!", reply_markup=back_key)
    await OfferData.name.set()

@dp.message_handler(state=OfferData.name)
async def worker_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    await message.answer("📝 Илтимос таклифингизни ёзинг!", reply_markup=back_key)
    await OfferData.next()

@dp.message_handler(state=OfferData.offer)
async def worker_name(message: types.Message, state: FSMContext):
    offer = message.text

    await state.update_data(
        {"offer": offer}
    )

    await message.answer('<b>📝 Маълумотлар барчаси тўгрилигига эътибот қилинг</b>', reply_markup=menu)
    await OfferData.next()



    data = await state.get_data()
    name = data.get("name")
    offer = data.get('offer')

    msg = "<b>Қуйидаги маълумотлар қабул қилинди:</b>\n"
    msg += f"<b>🙎‍♂️Ф.И.Ш:</b> -<code> {name}</code>\n"
    msg += f"<b>📝 Таклиф мазмуни:</b> -<code> {offer}</code>\n"

    await message.answer(msg, reply_markup=confirmation_keyboard)
    await OfferData.next()
    

