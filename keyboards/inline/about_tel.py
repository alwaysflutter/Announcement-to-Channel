from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

phone_state = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Yangi',callback_data='new'),
            InlineKeyboardButton(text='Ishaltilgan',callback_data='ishlatilgan')
        ],
    ],
    
)