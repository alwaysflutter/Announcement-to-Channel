from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

aboutbuy = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Sotaman'),
            KeyboardButton(text="Sotib olaman")
        ],
        [
            KeyboardButton(text='Faqat Obmen'),
        ],
        [
            KeyboardButton(text='Bekor qilish ❌')
        ],
    ],
    resize_keyboard=True
)