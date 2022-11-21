from aiogram.dispatcher.filters.state import StatesGroup, State


class PersonalData(StatesGroup):
    name = State()
    birth_date = State()
    malumoti = State()
    merriage = State()
    address = State()
    comunity = State()
    phonenum = State()
    branch_name = State()
    position = State()
    car = State()
    language = State()
    programming = State()
    old_work = State()
    money = State()
    want_get_money = State()
    qoshimcha = State()
    confirm = State()



