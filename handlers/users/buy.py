from aiogram.types import Message

from loader import dp

@dp.message_handler(text='Sotib olaman')
async def buy(msg: Message):
    await msg.answer(text='🏃 TEZ KUNDA....')

@dp.message_handler(text='Faqat Obmen')
async def obmen(msg: Message):
    await msg.answer(text='🏃 TEZ KUNDA....')

@dp.message_handler(text='Shaxsiy kabinet 💳')
async def obmen(msg: Message):
    await msg.answer(text='🏃 TEZ KUNDA....')
