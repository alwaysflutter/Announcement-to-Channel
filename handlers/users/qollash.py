from aiogram.types import Message
from data.config import ADMINS
from data.texts import qollash
from states.send_message_admin import Send_account
from aiogram.dispatcher import FSMContext

from loader import bot,dp


@dp.message_handler(text="Qo'llab quvvatlash ✊🏻")
async def malahat(msg: Message):
    await msg.answer(qollash)
    await Send_account.send_account.set()

@dp.message_handler(state=Send_account.send_account)
async def send_username(msg: Message,state: FSMContext):
    await state.update_data(text=msg.html_text, mention=msg.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
        mention = date.get('mention')

    await state.finish()
    await bot.send_message(ADMINS[0], f"Foydalanuvching {mention} o'zing taklifi" + 
                           " yoki shikoyati borligi sababli sizga o'z username qoldirdi ⤵️")
    await bot.send_message(ADMINS[0],text,)
