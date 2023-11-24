from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

post_add = CallbackData("add_write", "add")

anythinkelse = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ha',callback_data=post_add.new(add='yes')),
            InlineKeyboardButton(text='O\'tkazib yuborish',callback_data=post_add.new(add='no'))
        ],
    ],
    
)