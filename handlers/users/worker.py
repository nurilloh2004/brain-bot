from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, InputFile, ContentType
from loader import dp
from states.workerData import WorkerData
from keyboards.default.branch import branch_key
from keyboards.default.position import position_key
from keyboards.default.contact import contact_key
from keyboards.default.branch_position import branch_position_key
from keyboards.default.back import back_key
from keyboards.default.menu import menu
from aiogram.types import Message, CallbackQuery

from data.config import ADMINS, CHANNELS
from keyboards.inline.confirm import confirmation_keyboard, post_callback

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(text="🤵‍♂️ Ҳодимлар учун", state=None)
async def worker_menu(message: Message):
    await message.answer('Қуйидагилардан бирини танланг', reply_markup=branch_position_key)


@dp.message_handler(text='Лавозим ва Филиал ўзгартириш', state=None)
async def enter_name(message: types.Message):
    await message.answer("🙎‍♂️ Исм, Фамилия ва Шарифингизни киритинг:", reply_markup=back_key)
    await WorkerData.name.set()

@dp.message_handler(state=WorkerData.name)
async def worker_name(message: types.Message, state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    await message.answer("📅 Туғилган санангиз :КК.ОО.ЙЙЙЙ(13.12.1997) форматида:", reply_markup=back_key)
    await WorkerData.next()

@dp.message_handler(state=WorkerData.birth_date)
async def worker_birth(message: Message, state: FSMContext):
    birth_date = message.text
    await state.update_data(
        {
            "birth_date": birth_date
        }
    )
    await message.answer('📞 Телефон рақамингиз +998ххххххххх форматида:', reply_markup=contact_key)
    await WorkerData.next()


@dp.message_handler(lambda message: not message.text.isdigit(), state=WorkerData.phonenum)
async def process_phone_invalid(message: types.Message):
    return await message.reply("Қулайлик учун қуйидаги тугмани босинг!")

@dp.message_handler(state=WorkerData.phonenum, content_types='contact')
async def answer_phonenum(message: types.Message, state: FSMContext):
    phonenum = message.contact.phone_number
    async with state.proxy() as data:
        data["phonenum"] = phonenum
        # data["phonenum2"] += 1
    await message.answer("🏫 Айни вақтда сиз қайси филиалда ишлайсиз?", reply_markup=branch_key)
    await WorkerData.next()

@dp.message_handler(state=WorkerData.branch_name)
async def worker_branch(message: Message, state: FSMContext):
    branch_name = message.text
    await state.update_data(
        {"branch_name": branch_name}
    )
    await message.answer("👨🏻‍💼 Қайси лавозимда ишлайсиз?", reply_markup=position_key)
    await WorkerData.next()

@dp.message_handler(state=WorkerData.position)
async def worker_position(message: Message, state: FSMContext):
    position = message.text
    await state.update_data(
        {"position": position}
    )

    await message.answer("🏫 Сиз қайси филиалда ишлашни хоҳлайсиз?", reply_markup=branch_key)
    await WorkerData.next()


@dp.message_handler(state=WorkerData.new_branch)
async def worker_newbranch(message: Message, state: FSMContext):
    new_branch = message.text
    await state.update_data(
        {"new_branch": new_branch}
    )

    await message.answer("👨🏻‍💼 Қайси лавозимда ишлашни хоҳлайсиз?", reply_markup=position_key)
    await WorkerData.next()

@dp.message_handler(state=WorkerData.new_position)
async def worker_newposition(message: Message, state: FSMContext):
    new_position = message.text
    await state.update_data(
        {"new_position": new_position}
    )
    await message.answer("⁉️ Нима сабабдан филиал ёки лавозимингизни ўзрагтирмоқчисиз?", reply_markup=ReplyKeyboardRemove())
    await WorkerData.next()

@dp.message_handler(state=WorkerData.cause)
async def worker_cause(message: Message, state: FSMContext):
    cause = message.text
    await state.update_data(
        {'cause': cause}
    )
    await message.answer('✅ Янги лавозим ёки филиалга ўтсангиз нима янгиликлар қиласиз?')
    await WorkerData.next()

@dp.message_handler(state=WorkerData.news)
async def worker_news(message: Message, state: FSMContext):
    news = message.text
    await state.update_data(
        {"news": news}
    )
    await message.answer("<b>🧾 Маълумотлар барчаси тўгрилигига эътибот қилинг</b>", reply_markup=menu)
    await WorkerData.next()



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

    msg = "<b>Қуйидаги маълумотлар қабул қилинди:</b>\n"
    msg += f"<b>👤 Ф.И.Ш:</b> -<code> {name}</code>\n"
    msg += f"<b>📆 Туғилган вақти:</b> -<code> {birth_date}</code>\n"
    msg += f"<b>📞 Телефон:</b> -<code> {phonenum}</code>\n"
    msg += f"<b>🏫 Филиал номи:</b> -<code> {branch_name}</code>\n"
    msg += f"<b>🧰 Лавозим:</b> -<code> {position}</code>\n"
    msg += f"<b>🏫 Янги филиал:</b> -<code> {new_branch}</code>\n"
    msg += f"<b>🧰 Янги лавозим:</b> -<code>{new_position}</code>\n"
    msg += f"<b>⁉️ Сабаб:</b> -<code>{cause}</code>\n"
    msg += f"<b>✅ Янгилик:</b> -<code>{news}</code>\n"

    await message.answer(msg, reply_markup=confirmation_keyboard)
    await WorkerData.next()

@dp.callback_query_handler(post_callback.filter(action="post"))
async def approve_post(call: CallbackQuery):
    await call.answer("Чоп этишга руҳсат бердингиз.", show_alert=True)
    message = await call.message.edit_reply_markup()
    target_channel = CHANNELS[0]
    await message.send_copy(target_channel)



@dp.callback_query_handler(post_callback.filter(action="cancel"))
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await call.answer("Аризангизни рад қилдингиз!")
    await call.message.edit_reply_markup()
    await call.message.answer("Ариза рад этилди.")


@dp.message_handler(state=WorkerData.confirm)
async def post_unknown(message: Message):
    await message.answer("Юбориш ёки бекор қилшни танланг")

