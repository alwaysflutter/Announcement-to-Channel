from aiogram.types import Message
from data.config import CHANNELS

from loader import dp,bot

@dp.message_handler(text= 'Lohilarimiz 🫂')
async def projects(msg: Message):
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
    
    await msg.answer(f'Rasmiy kanalimiz\n{channels_format}')