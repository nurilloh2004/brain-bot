from aiogram.dispatcher.filters.state import StatesGroup, State


class OfferData_ru(StatesGroup):
    name = State()
    offer = State()
    Confirm = State()