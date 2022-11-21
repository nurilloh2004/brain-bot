from aiogram.dispatcher.filters.state import StatesGroup, State


class ComplaintData_ru(StatesGroup):
    name = State()
    complaint = State()
    Confirm = State()