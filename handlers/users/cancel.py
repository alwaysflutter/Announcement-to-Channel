from aiogram.types import Message
from keyboards.default.main_menu import mainmenu
from loader import dp

@dp.message_handler(text='Bekor qilish ❌')
async def cancel(message: Message):
    await message.answer('Siz bosh menudasiz',reply_markup=mainmenu)