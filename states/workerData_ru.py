from aiogram.dispatcher.filters.state import StatesGroup, State


class WorkerData_ru(StatesGroup):
    name = State()
    birth_date = State()
    phonenum = State()
    branch_name = State()
    position = State()
    new_branch = State()
    new_position = State()
    cause = State()
    news = State()
    confirm = State()






