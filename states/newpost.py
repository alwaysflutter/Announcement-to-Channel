from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
    NewMessage = State()
    Confirm = State()

class AboutPhone(StatesGroup):
    About = State()
    AboutTwo = State()
    AboutThree = State()
    AboutColor = State()
    AboutPass = State()
    AboutAlmash = State()
    AboutBater = State()
    AboutConiform = State()
    Coniform = State()
    AboutCost = State()