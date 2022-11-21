from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile, ContentType
from keyboards.default.malumot import malumot_keyboard
from keyboards.default.marriage import married
from keyboards.default.region import region_key
from keyboards.default.branch import branch_key
from keyboards.default.position import position_key
from keyboards.default.language import language_key
from keyboards.default.programming import programming_key
from keyboards.default.back import back_key
from keyboards.default.menu import menu
from keyboards.default.next import next_key
from keyboards.default.contact import contact_key
from loader import dp, bot
from keyboards.default.car import car_key
from states.personalData import PersonalData
from aiogram.types import Message, CallbackQuery
from keyboards.default.nothing import nothing_key
from aiogram.dispatcher.filters import Text
import logging
logging.basicConfig(level=logging.INFO)

from data.config import ADMINS, CHANNELS
from keyboards.inline.confirm import confirmation_keyboard, post_callback



# /anketa komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text='👨‍🎓 Вакантлар учун', state=None)
async def enter_test(message: types.Message):
    await message.answer("🙎‍♂️ Исм, Фамилия ва Шарифингизни киритинг !", reply_markup=ReplyKeyboardRemove())
    await PersonalData.name.set()


@dp.message_handler(state='*', text='Бекор қилиш 🚫')
@dp.message_handler(Text(equals='Бекор қилиш 🚫', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Сиз буйруқларни бекор қилдингиз !', reply_markup=menu)


@dp.message_handler(state=PersonalData.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    await message.answer("📅 Туғилган санангиз :\nКК.ОО.ЙЙЙЙ(13.12.1997) форматида:", reply_markup=back_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.birth_date)
async def answer_birth(message: types.Message, state: FSMContext):
    birth_date = message.text

    await state.update_data(
        {"birth_date": birth_date}
    )
    await message.answer("💼 Маълумотингизни танланг:",reply_markup=malumot_keyboard)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.malumoti)
async def answer_malumot(message: types.Message, state: FSMContext):
    malumot = message.text
    await state.update_data(
        {"malumot": malumot}
    )
    await message.answer("👨‍👩‍👧‍👦 Оилавий аҳволингиз:", reply_markup=married)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.merriage)
async def answer_merriage(message: types.Message, state: FSMContext):
    merriage = message.text
    await state.update_data(
        {"merriage": merriage}
    )
    await message.answer("🌐 Яшаш манзилингиз: туман ёки шаҳар(хозирги турар жойингиз):", reply_markup=region_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.address)
async def answer_address(message: types.Message, state: FSMContext):
    address = message.text
    await state.update_data(
        {"address": address}
    )
    await message.answer("🏘 Тўлиқ манзилингизни киритинг(МФЙ ва кўчангиз):",reply_markup=back_key)
    await PersonalData.next()

@dp.message_handler(state=PersonalData.comunity,)
async def answer_comunity(message: types.Message, state: FSMContext):
    comunity = message.text
    await state.update_data(
        {'comunity': comunity}
    )

    await message.answer("📞 Қуйидаги тугмани босиш орқали юборинг:",reply_markup=contact_key)
    await PersonalData.next()

@dp.message_handler(lambda message: not message.text.isdigit(), state=PersonalData.phonenum)
async def process_phone_invalid(message: types.Message):
    return await message.reply("Қулайлик учун қуйидаги тугмани босинг!")

@dp.message_handler(state=PersonalData.phonenum, content_types='contact')
async def answer_phonenum(message: types.Message, state: FSMContext):
    phonenum = message.contact.phone_number
    async with state.proxy() as data:
        data["phonenum"] = phonenum
    await message.answer("🏫 Сиз қайси худудда ишлашни хоҳлайсиз?", reply_markup=branch_key)
    await PersonalData.next()

@dp.message_handler(state=PersonalData.branch_name)
async def answer_branch(message: types.Message, state: FSMContext):
    branch_name = message.text
    await state.update_data(
        {"branch_name": branch_name}
    )
    await message.answer("👨🏻‍💼 Қайси лавозимда ишлашни хоҳлайсиз?",reply_markup=position_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.position)
async def answer_lavozim(message: types.Message, state: FSMContext):
    lavozim = message.text
    await state.update_data(
        {'lavozim': lavozim}
    )
    await message.answer("🚗 Автомобилингиз борми?", reply_markup=car_key)
    await PersonalData.next()

@dp.message_handler(state=PersonalData.car)
async def answer_car(message: Message, state: FSMContext):
    car = message.text
    await state.update_data(
        {'car': car}
    )
    await message.answer("🇷🇺 🇺🇸 Ҳозирда қайси тилларни биласиз?",reply_markup=language_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.language)
async def answer_lang(messsage: types.Message, state: FSMContext):
    language = messsage.text
    await state.update_data(
        {'language': language}
    )
    await messsage.answer("👨‍💻 Қайси дастурлардан фойдалана оласиз?", reply_markup=programming_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.programming)
async def answer_programming(message: types.Message, state: FSMContext):
    programming = message.text
    await state.update_data(
        {'programming': programming}
    )
    text = "🏦 Ишлаган жойингиз ва вақтлари\n"
    text += "Мисол учун:\n"
    text += "..., Дастурчи, Дастур тузиш - 11.2020 - 03.2021:\n"
    await message.answer(text, reply_markup=nothing_key)
    await PersonalData.next()

@dp.message_handler(state=PersonalData.old_work)
async def answer_oldwork(message: types.Message, state: FSMContext):
    old_work = message.text
    await state.update_data(
        {"old_work": old_work}
    )
    await message.answer("💰 Қанча маош олишни хоҳлайсиз?(фақат рақамларда киритинг):", reply_markup=back_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.money)
async def answer_money(message: types.Message, state: FSMContext):
    money = message.text
    await state.update_data(
        {'money': money}
    )
    await message.answer("Бошланишига Қанча маош ҳоҳлайсиз ? ", reply_markup=back_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.want_get_money)
async def answer_want_get_money(message: types.Message, state: FSMContext):
    want_get_money = message.text
    await state.update_data(
        {'want_get_money': want_get_money}
    )
    await message.answer("📝 Қўшимча маълумотлар (📞 Рақам ёки ўзингиз ҳақингизда)", reply_markup=next_key)
    await PersonalData.next()


@dp.message_handler(state=PersonalData.qoshimcha)
async def answer_qoshimcha(message: types.Message, state: FSMContext):
    qoshimcha = message.text
    await state.update_data(
        {'qoshimcha': qoshimcha}
    )

    await message.answer('<b>Маълумотлар барчаси тўгрилигига эътибот қилинг ва тасдикланг</b>', reply_markup=menu)
    await PersonalData.next()


    data = await state.get_data()
    name = data.get("name")
    birth_date = data.get('birth_date')
    malumot = data.get('malumot')
    address = data.get('address')
    comunity = data.get('comunity')
    merriage = data.get('merriage')
    phonenum = data.get('phonenum')
    branch_name = data.get('branch_name')
    lavozim = data.get('lavozim')
    car = data.get('car')
    language = data.get('language')
    programming = data.get('programming')
    old_work = data.get('old_work')
    money = data.get('money')
    want_get_money = data.get('want_get_money')
    qoshimcha = data.get('qoshimcha')

    msg = "<b>🧾 Қуйидаги маълумотлар қабул қилинди:</b>\n"
    msg += f"<b>👤 ФИШ:</b> -<code> {name}</code>\n"
    msg += f"<b>📆 Туғилган вақти:</b> -<code> {birth_date}</code>\n"
    msg += f"<b>🎓 Маълумоти:</b> - <code>{malumot}</code>\n"
    msg += f"<b>🔍📍 Шахар(Туман):</b> -<code> {address}</code>\n"
    msg += f"<b>🏫 Манзил:</b> -<code> {comunity}</code>\n"
    msg += f"<b>📞 Телефон:</b> -<code> {phonenum}</code>\n"
    msg += f"<b>🏫 Ҳудуд:</b> -<code> {branch_name}</code>\n"
    msg += f"<b>👨‍👩‍👧‍👦 Оилавий шароити:</b> -<code> {merriage}</code>\n"
    msg += f"<b>🧰 Лавозим:</b> -<code> {lavozim}</code>\n"
    msg += f"<b>🚗 Автомобиль:</b> -<code> {car}</code>\n"
    msg += f"<b>🇷🇺🇺🇿🇺🇸 Тил:</b> -<code> {language}</code>\n"
    msg += f"<b>🧑‍💻 Дастурлар:</b> -<code>{programming}</code>\n"
    msg += f"<b>🧳 Эски иш жойи:</b> -<code> {old_work}</code>\n"
    msg += f"<b>💰 Иш ҳаққи:</b> -<code>{money}</code>\n"
    msg += f"<b>💰 Бошланишига Иш ҳаққи</b> -<code>{want_get_money}</code>\n"
    msg += f"<b>✳️ Қўшимча:</b> -<code>{qoshimcha}</code>\n"

    await message.answer(msg, reply_markup=confirmation_keyboard)
    await PersonalData.next()

@dp.callback_query_handler(post_callback.filter(action="post"))
async def approve_post(call: CallbackQuery):
    await call.answer("Аризангиз юборилди раҳмат!", show_alert=True)
    message = await call.message.edit_reply_markup()
    target_channel = CHANNELS[0]
    await message.send_copy(target_channel)



@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.answer("Аризангизни рад этдингиз!", show_alert=True)
    await call.message.edit_reply_markup()
    await call.message.answer("Ариза рад этилди!")


@dp.message_handler(state=PersonalData.confirm)
async def post_unknown(message: Message):
    await message.answer("Чоп этиш ёки рад этишни танланг")

