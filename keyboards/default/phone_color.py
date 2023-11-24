from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

phonecolor = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='white ⬜️'),
            KeyboardButton(text='black ⬛️')
        ],
        [
            KeyboardButton(text="blue 🟦"),
            KeyboardButton(text='gold 🟨'),
        ],
        [
            KeyboardButton(text='grey🟫/silver'),
            KeyboardButton(text='red 🟥')
        ],
        [
            KeyboardButton(text='Bekor qilish ❌')
        ],
    ],
    resize_keyboard=True
)

aboutphone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Yangi karobkadan ochilamagan'),
        ],
        [
            KeyboardButton(text="Yangidek"),
            KeyboardButton(text='zo\'r'),
        ],
        [
            KeyboardButton(text='yaxshi'),
            KeyboardButton(text='ishlatsa bo\'ladi')
        ],
        [
            KeyboardButton(text='yaroqsiz'),
            KeyboardButton(text='Bekor qilish ❌')
        ],
    ],
    resize_keyboard=True
)

phonedocument = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Yo\'q Pass-Kopiya beriladi'),
        ],
        [
            KeyboardButton(text="Full"),
            KeyboardButton(text='Bor'),
        ],
        [
            KeyboardButton(text='Bekor qilish ❌')
        ],
    ],
    resize_keyboard=True
)

phonebatereya = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Zo'r"),
            KeyboardButton(text='Biroz charchagan'),
        ],
        [
            KeyboardButton(text="Yaxshi"),
            KeyboardButton(text='Almashtirish kerak'),
        ],
        [
            KeyboardButton(text='Bekor qilish ❌')
        ],
    ],
    resize_keyboard=True
)

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Bekor qilish ❌')
        ],
    ]
)