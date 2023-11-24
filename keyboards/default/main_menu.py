from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

mainmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Muhim eslatma va qoidalar 🗞'),
        ],
        [
            KeyboardButton(text="E'lon berish ✍️"),
            KeyboardButton(text='E\'lon holati 👀'),
        ],
        [
            KeyboardButton(text='Shaxsiy kabinet 💳')
        ],
        [
            KeyboardButton(text='Qo\'llab quvvatlash ✊🏻'),
            KeyboardButton(text='Lohilarimiz 🫂')
        ],
    ],
    resize_keyboard=True
)
