from aiogram.dispatcher.filters.state import State,StatesGroup

class Lang(StatesGroup):
    lang= State()

class Update(StatesGroup):
    lang = State()