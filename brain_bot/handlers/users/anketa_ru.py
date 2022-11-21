from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile, ContentType
from keyboards.default.malumot import malumot_keyboard_ru
from keyboards.default.marriage import married_ru
from keyboards.default.region import region_key_ru
from keyboards.default.branch import branch_key_ru
from keyboards.default.position import position_key_ru
from keyboards.default.language import language_key_ru
from keyboards.default.programming import programming_key_ru
from keyboards.default.back import back_key_ru
from keyboards.default.nothing import nothing_key_ru
from keyboards.default.car import car_key_ru
from keyboards.default.next import next_key_ru
from keyboards.default.menu import menu
from keyboards.default.contact import contact_key_ru
from loader import dp, bot
from states.personalData_ru import PersonalData_ru
from aiogram.types import Message, CallbackQuery

from aiogram.dispatcher.filters import Text
import logging
logging.basicConfig(level=logging.INFO)

from data.config import ADMINS, CHANNELS
from keyboards.inline.confirm import confirmation_keyboard_ru, post_callback



# /anketa komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
@dp.message_handler(text='👨‍🎓 На вакансии', state=None)
async def enter_test(message: types.Message):
    await message.answer("🙎‍♂️ Введите свое имя, фамилию и фамилию:!", reply_markup=ReplyKeyboardRemove())
    await PersonalData_ru.name.set()


@dp.message_handler(state='*', text='Отмена 🚫')
@dp.message_handler(Text(equals='Отмена 🚫', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.reply('Спасибо !!!', reply_markup=menu)


@dp.message_handler(state=PersonalData_ru.name)
async def answer_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    await message.answer("📅 Дата рождения: \ nКК.ОО.ГГГГ (13.12.1997) формат:!", reply_markup=back_key_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.birth_date)
async def answer_birth(message: types.Message, state: FSMContext):
    birth_date = message.text

    await state.update_data(
        {"birth_date": birth_date}
    )
    await message.answer("💼 Выберите уровень вашего образования:",reply_markup=malumot_keyboard_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.malumoti)
async def answer_malumot(message: types.Message, state: FSMContext):
    malumot = message.text
    await state.update_data(
        {"malumot": malumot}
    )
    await message.answer("👨‍👩‍👧‍👦 Семейное положение:", reply_markup=married_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.merriage)
async def answer_merriage(message: types.Message, state: FSMContext):
    merriage = message.text
    await state.update_data(
        {"merriage": merriage}
    )
    await message.answer("🌐 Ваше место жительства: район или город (текущее место жительства):", reply_markup=region_key_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.address)
async def answer_address(message: types.Message, state: FSMContext):
    address = message.text
    await state.update_data(
        {"address": address}
    )
    await message.answer("🏘 Введите свой полный адрес (МФЙ и улица):",reply_markup=back_key_ru)
    await PersonalData_ru.next()

@dp.message_handler(state=PersonalData_ru.comunity,)
async def answer_comunity(message: types.Message, state: FSMContext):
    comunity = message.text
    await state.update_data(
        {'comunity': comunity}
    )
    await message.answer("📞 Отправить номер, нажав кнопку ниже !",reply_markup=contact_key_ru)
    await PersonalData_ru.next()

@dp.message_handler(lambda message: not message.text.isdigit(), state=PersonalData_ru.phonenum)
async def process_phone_invalid(message: types.Message):
    return await message.reply("Для удобства нажмите кнопку ниже!")

@dp.message_handler(state=PersonalData_ru.phonenum, content_types='contact')
async def answer_phonenum(message: types.Message, state: FSMContext):
    phonenum = message.contact.phone_number
    async with state.proxy() as data:
        data["phonenum"] = phonenum
    await message.answer("🏫 В какой регионе вы хотите работать?", reply_markup=branch_key_ru)
    await PersonalData_ru.next()

@dp.message_handler(state=PersonalData_ru.branch_name)
async def answer_branch(message: types.Message, state: FSMContext):
    branch_name = message.text
    await state.update_data(
        {"branch_name": branch_name}
    )
    await message.answer("👨🏻‍💼 В какой должности вы хотите работать?",reply_markup=position_key_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.position)
async def answer_lavozim(message: types.Message, state: FSMContext):
    lavozim = message.text
    await state.update_data(
        {'lavozim': lavozim}
    )
    await message.answer("🚗 У тебя есть машина ?", reply_markup=car_key_ru)
    await PersonalData_ru.next()

@dp.message_handler(state=PersonalData_ru.car)
async def answer_car(message: Message, state: FSMContext):
    car = message.text
    await state.update_data(
        {'car': car}
    )
    await message.answer("🇷🇺 🇺🇸 Какие языки ты знаешь?",reply_markup=language_key_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.language)
async def answer_lang(messsage: types.Message, state: FSMContext):
    language = messsage.text
    await state.update_data(
        {'language': language}
    )
    await messsage.answer("👨‍💻 Какие программы можно использовать?", reply_markup=programming_key_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.programming)
async def answer_programming(message: types.Message, state: FSMContext):
    programming = message.text
    await state.update_data(
        {'programming': programming}
    )
    text = "◀️🏦 Где и когда ты работаешь\n"
    text += "Например:\n"
    text += "..., Программист, Программирование - 11.2020 - 03.2021:\n"
    await message.answer(text, reply_markup=nothing_key_ru)
    await PersonalData_ru.next()

@dp.message_handler(state=PersonalData_ru.old_work)
async def answer_oldwork(message: types.Message, state: FSMContext):
    old_work = message.text
    await state.update_data(
        {"old_work": old_work}
    )
    await message.answer("💰 Сколько вы хотите заработать в месяц? (Вводите только цифрами):", reply_markup=back_key_ru)
    await PersonalData_ru.next()


@dp.message_handler(state=PersonalData_ru.money)
async def answer_want_get_money(message: types.Message, state: FSMContext):
    money = message.text
    await state.update_data(
        {'money': money}
    )
    await message.answer("📝Бошланишига Сколько вы хотите заработать", reply_markup=back_key_ru)
    await PersonalData.next()

@dp.message_handler(state=PersonalData_ru.want_get_money)
async def answer_money(message: types.Message, state: FSMContext):
    want_get_money = message.text
    await state.update_data(
        {'want_get_money': want_get_money}
    )
    await message.answer("📝 Дополнительная информация (📞 Номер или о себе):", reply_markup=next_key_ru)
    await PersonalData_ru.next()



@dp.message_handler(state=PersonalData_ru.qoshimcha)
async def answer_qoshimcha(message: types.Message, state: FSMContext):
    qoshimcha = message.text
    await state.update_data(
        {'qoshimcha': qoshimcha}
    )

    await message.answer('<b>Убедитесь, что вся информация верна</b>', reply_markup=menu)
    await PersonalData_ru.next()


    data = await state.get_data()
    name = data.get("name")
    birth_date = data.get('birth_date')
    malumot = data.get('malumot')
    address = data.get('address')
    comunity = data.get('comunity')
    phonenum = data.get('phonenum')
    merriage = data.get('merriage')
    branch_name = data.get('branch_name')
    lavozim = data.get('lavozim')
    car = data.get('car')
    language = data.get('language')
    programming = data.get('programming')
    old_work = data.get('old_work')
    money = data.get('money')
    want_get_money = data.get('want_get_money')
    qoshimcha = data.get('qoshimcha')

    msg = "<b>🧾 Была получена следующая информация:</b>\n"
    msg += f"<b>👤 Ф.И.O:</b> -<code> {name}</code>\n"
    msg += f"<b>📆 Дата рождения:</b> -<code> {birth_date}</code>\n"
    msg += f"<b>🎓 Информация:</b> - <code>{malumot}</code>\n"
    msg += f"<b>🔍📍Город (район):</b> -<code> {address}</code>\n"
    msg += f"<b>🏫 Адрес:</b> -<code> {comunity}</code>\n"
    msg += f"<b>📞 Телефон:</b> -<code> {phonenum}</code>\n"
    msg += f"<b>🏫 Название отделения:</b> -<code> {branch_name}</code>\n"
    msg += f"<b>👨‍👩‍👧‍👦 Семейные условия:</b> -<code> {merriage}</code>\n"
    msg += f"<b>🧰 Позиция:</b> -<code> {lavozim}</code>\n"
    msg += f"<b>🚗 Автомобиль:</b> -<code> {car}</code>\n"
    msg += f"<b>🇷🇺🇺🇿🇺🇸 Язык:</b> -<code> {language}</code>\n"
    msg += f"<b>🧑‍💻 Программное обеспечение:</b> -<code>{programming}</code>\n"
    msg += f"<b>🧳 Старое рабочее место:</b> -<code> {old_work}</code>\n"
    msg += f"<b>💰 Зарплата:</b> -<code>{money}</code>\n"
    msg += f"<b>💰 Start Зарплата:</b> -<code>{want_get_money}</code>\n"
    msg += f"<b>✳️Дополнительный:</b> -<code>{qoshimcha}</code>\n"

    await message.answer(msg, reply_markup=confirmation_keyboard_ru)
    await PersonalData_ru.next()

@dp.callback_query_handler(post_callback.filter(action="post_ru"))
async def approve_post(call: CallbackQuery):
    await call.answer("Ваша заявка отправлена!", show_alert=True)
    message = await call.message.edit_reply_markup()
    target_channel = CHANNELS[0]
    await message.send_copy(target_channel)



@dp.callback_query_handler(post_callback.filter(action="cancel_ru"))
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await call.answer('Вы отклонили заявку!', show_alert=True)
    await call.message.edit_reply_markup()
    await call.message.answer("Заявка была отклонена.")


@dp.message_handler(state=PersonalData_ru.confirm)
async def post_unknown(message: Message):
    await message.answer("Выберите одну из кнопок ниже!")
