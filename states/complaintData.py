from aiogram.dispatcher.filters.state import StatesGroup, State


class ComplaintData(StatesGroup):
    name = State()
    complaint = State()
    Confirm = State()