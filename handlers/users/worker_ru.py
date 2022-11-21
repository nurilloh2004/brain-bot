from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile, ContentType
from loader import dp
from states.workerData_ru import WorkerData_ru
from keyboards.default.branch import branch_key_ru
from keyboards.default.position import position_key_ru
from keyboards.default.menu import about_ru
from keyboards.inline.confirm import confirmation_keyboard_ru
from keyboards.default.contact import contact_key_ru
from keyboards.default.menu import menu
from keyboards.default.back import back_key_ru
from aiogram.dispatcher import filters
from aiogram.types import Message, CallbackQuery
from keyboards.default.branch_position import branch_position_key_ru

from data.config import ADMINS, CHANNELS
from keyboards.inline.confirm import confirmation_keyboard_ru, post_callback

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(text="🤵‍♂️ Для сотрудников")
async def worker_menu(message: Message):
    await message.answer('Выберите один из следующих', reply_markup=branch_position_key_ru)

@dp.message_handler(text='Смена должности и отделения')
async def enter_name(message: types.Message):
    await message.answer("🙎‍♂️ Введите ваше имя !", reply_markup=back_key_ru)
    await WorkerData_ru.name.set()

@dp.message_handler(state=WorkerData_ru.name)
async def worker_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    await message.answer("📅 Дата рождения: КК.ОО.ГГГГ (13.12.1997):", reply_markup=back_key_ru)
    await WorkerData_ru.next()

@dp.message_handler(state=WorkerData_ru.birth_date)
async def worker_birth(message: Message, state: FSMContext):
    birth_date = message.text
    await state.update_data(
        {
            "birth_date": birth_date
        }
    )
    await message.answer('📞 Ваш номер телефона в формате + 998xxxxxxxxx:',reply_markup=contact_key_ru)
    await WorkerData_ru.next()


@dp.message_handler(state=WorkerData_ru.phonenum, content_types='contact')
async def answer_phonenum(message: types.Message, state: FSMContext):
    phonenum = message.contact.phone_number
    async with state.proxy() as data:
        data["phonenum"] = phonenum

    await message.answer("🏫 В каком филиале вы работаете?", reply_markup=branch_key_ru)
    await WorkerData_ru.next()

@dp.message_handler(state=WorkerData_ru.branch_name)
async def worker_branch(message: Message, state: FSMContext):
    branch_name = message.text
    await state.update_data(
        {"branch_name": branch_name}
    )
    await message.answer("👨🏻‍💼 На какой должности ты работаешь?", reply_markup=position_key_ru)
    await WorkerData_ru.next()

@dp.message_handler(state=WorkerData_ru.position)
async def worker_position(message: Message, state: FSMContext):
    position = message.text
    await state.update_data(
        {"position": position}
    )

    await message.answer("🏫 В каком филиале вы хотите работать?", reply_markup=branch_key_ru)
    await WorkerData_ru.next()

@dp.message_handler(state=WorkerData_ru.new_branch)
async def worker_newbranch(message: Message, state: FSMContext):
    new_branch = message.text
    await state.update_data(
        {"new_branch": new_branch}
    )

    await message.answer("👨🏻‍💼 На какой должности ты хочешь работать?", reply_markup=position_key_ru)
    await WorkerData_ru.next()

@dp.message_handler(state=WorkerData_ru.new_position)
async def worker_newposition(message: Message, state: FSMContext):
    new_position = message.text
    await state.update_data(
        {"new_position": new_position}
    )
    await message.answer('⁉️Почему вы хотите сменить ветвь или должность?', reply_markup=back_key_ru)
    await WorkerData_ru.next()

@dp.message_handler(state=WorkerData_ru.cause)
async def worker_cause(message: Message, state: FSMContext):
    cause = message.text
    await state.update_data(
        {"cause": cause}
    )
    await message.answer('✅ Какие новости вы делаете, когда переходите на новую должность или филиал?',reply_markup=back_key_ru)
    await WorkerData_ru.next()
@dp.message_handler(state=WorkerData_ru.news)
async def worker_news(message: Message, state: FSMContext):
    news = message.text
    await state.update_data(
        {"news": news}
    )
    await message.answer('<b>🧾 Убедитесь, что вся информация верна</b>', reply_markup=menu)
    await WorkerData_ru.next()



    data = await state.get_data()
    name = data.get("name")
    birth_date = data.get('birth_date')
    phonenum = data.get('phonenum')
    branch_name = data.get('branch_name')
    position = data.get('position')
    new_branch = data.get('new_branch')
    new_position = data.get('new_position')
    cause = data.get('cause')
    news = data.get('news')

    msg = "<b>Была получена следующая информация:</b>\n"
    msg += f"<b>👤 Ф.И.O:</b> -<code> {name}</code>\n"
    msg += f"<b>📆 Дата рождения:</b> -<code> {birth_date}</code>\n"
    msg += f"<b>📞Телефон:</b> -<code> {phonenum}</code>\n"
    msg += f"<b>🏫 Название отделения:</b> -<code> {branch_name}</code>\n"
    msg += f"<b>🧰 Позиция:</b> -<code> {position}</code>\n"
    msg += f"<b>🏫 Название новой ветки:</b> -<code> {new_branch}</code>\n"
    msg += f"<b>🧰 Новое положение:</b> -<code>{new_position}</code>\n"
    msg += f"<b>⁉️Причина:</b> -<code>{cause}</code>\n"
    msg += f"<b>✅ Новости:</b> -<code>{news}</code>\n"


    await message.answer(msg, reply_markup=confirmation_keyboard_ru)

    await WorkerData_ru.next()

@dp.callback_query_handler(post_callback.filter(action="post"))
async def approve_post(call: CallbackQuery):
    await call.answer("Ваша заявка отправлена!", show_alert=True)
    message = await call.message.edit_reply_markup()
    target_channel = CHANNELS[0]
    await message.send_copy(target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await call.answer("Вы отклонили заявку!", show_alert=True)
    await call.message.edit_reply_markup()
    await call.message.answer("Заявка была отклонена")


@dp.message_handler(state=WorkerData_ru.confirm)
async def post_unknown(message: Message):
    await message.answer("Выберите одну из кнопок ниже!")

