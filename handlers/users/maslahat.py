from aiogram.types import Message
from data.texts import maslahat
from loader import dp


@dp.message_handler(text='Muhim eslatma va qoidalar 🗞')
async def malahat(msg: Message):
    await msg.answer(maslahat)