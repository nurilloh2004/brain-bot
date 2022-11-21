from aiogram.dispatcher.filters.state import StatesGroup, State


class OfferData(StatesGroup):
    name = State()
    offer = State()
    Confirm = State()