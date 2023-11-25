from aiogram.types import Message
from keyboards.default.elon_berish import aboutbuy
from aiogram.types.callback_query import CallbackQuery
from states.newpost import AboutPhone
from aiogram.dispatcher import FSMContext
from keyboards.default.phone_color import aboutphone,phonecolor,phonedocument,phonebatereya
from keyboards.inline.yana import anythinkelse
from keyboards.inline.yana import post_add
from keyboards.default.phone_color import back
from data.config import ADMINS, CHANNELS
from keyboards.inline.manage_post import post_callback
from keyboards.inline.manage_post import confirmation_keyboard
from keyboards.default.main_menu import mainmenu

from loader import dp,bot

class Variable:
    global_ls = []
    allTxt = ""

def cancel(txt):
    return txt != "Bekor qilish ❌"
    

@dp.message_handler(text_contains="E'lon berish ✍️")
async def elon_berish(msg: Message):
    
    Variable.global_ls=[]
    Variable.allTxt = ""
    await msg.answer('Tanlang',reply_markup=aboutbuy)

@dp.message_handler(text_contains="Sotaman")
async def elon_berish(msg: Message):
    txt = """
📱 Telefoningizning modelini bexato va to'liq bilan kiriting!👇

Namuna:
iPhone 15 Pro Max
Samsung Galaxy S24 Ultra 5G
Xiaomi Redmi Note 13 Pro Plus
Huawei Honor X9a
Vivo V27 Pro
Oppo Find N2 Flip
Realme 10 Pro Plus va h.k...
"""
    await msg.answer(text=txt)
    await AboutPhone.About.set()


@dp.message_handler(state=AboutPhone.About)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
    
    if cancel(text):
        Variable.global_ls.append(text)
        await message.answer("Xotirasini kiriting\n"
                             "64/4")
        await AboutPhone.next()
    else:
        Variable.global_ls = []
        await message.answer("Siz bosh menudasiz !!!",reply_markup=mainmenu)
        await state.finish()

    
@dp.message_handler(state=AboutPhone.AboutTwo)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
    if cancel(text):
        Variable.global_ls.append(text)
        await message.answer("Telefoningiz holatini tanlang",reply_markup=aboutphone)
        await AboutPhone.next()
    else:
        Variable.global_ls = []
        await message.answer("Siz bosh menudasiz !!!",reply_markup=mainmenu)
        await state.finish()
    
@dp.message_handler(state=AboutPhone.AboutThree)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
    if cancel(text):
       
        await message.answer("Telefoningiz rangini tanlang",reply_markup=phonecolor)
        await AboutPhone.next()
    else:
        Variable.global_ls = []
        await state.finish()
        await message.answer("Siz bosh menudasiz !!!",reply_markup=mainmenu)

@dp.message_handler(state=AboutPhone.AboutColor)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
    
    txt = """
📦 & 📑 Kor-Dok bormi yoki yo‘q?

Eslatma: full deb, agarda yangiligida korobkasini ichidan chiqqan jihozlari (zaryadchik, chehol, quloqchin va h.k..) haligacha ham mavjud bo‘lsagina yozing!

Knopkadan tanlang!👇
"""
    if cancel(text):
        Variable.global_ls.append(text)
        await AboutPhone.next()
        await message.answer(txt,reply_markup=phonedocument)
    else:
        Variable.global_ls = []
        await state.finish()
        await message.answer("Siz bosh menudasiz !!!",reply_markup=mainmenu)


@dp.message_handler(state=AboutPhone.AboutPass)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
    if cancel(text):
        Variable.global_ls.append(text)
        await message.answer("♻️ Almashtirish/Obmen/Barter bormi yoki yo'q?"+
                             "Agar birortasini yozadigan bolsangiz aniq qilib yozing"+
                             " Yo'q bo'lsa yo'q deb yozing",reply_markup=back)
        await AboutPhone.next()
    else:
        Variable.global_ls = []
        await message.answer("Siz bosh menudasiz !!!",reply_markup=mainmenu)
        await state.finish()

@dp.message_handler(state=AboutPhone.AboutAlmash)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
    
    txt = """
🔋 Telefoningiz quvvati/akkumulyatorining holati qanday?

❗Namuna:
1) zo'r
2) yaxshi
3) bir oz charchagan
4) almashtirish kerak

🔋 iPhone foydalanuvchilari faqat % ni kiriting! Namuna:

80%
95% (usilenniy)

Yoki quyidagilardan birini tanlang!👇
"""

    if cancel(text):
        Variable.global_ls.append(text)
        await message.answer(txt,reply_markup=phonebatereya)
        await AboutPhone.next()
    else:
        Variable.global_ls = []
        await message.answer("Siz bosh menudasiz !!!",reply_markup=mainmenu)
        await state.finish()

@dp.message_handler(state=AboutPhone.AboutBater)
async def enter_message(message: Message, state: FSMContext):
    await state.update_data(text=message.html_text, mention=message.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')
  
    if cancel(text):
        Variable.global_ls.append(text)
        await message.answer("Yana biror narsa qo'shishni hohlaysizmi",reply_markup=anythinkelse)
        await AboutPhone.next()
    else:
        Variable.global_ls = []
        await message.answer("Siz bosh menudasiz !!!",reply_markup=mainmenu)
        await state.finish()

@dp.callback_query_handler(post_add.filter(add='no'),state=AboutPhone.Add)
async def post_noedit(call: CallbackQuery):
    print(Variable.global_ls,Variable.allTxt)
    for i in Variable.global_ls:
        Variable.allTxt += i
        Variable.allTxt += '\n'
    await AboutPhone.next()


@dp.callback_query_handler(post_add.filter(add='yes'),state= AboutPhone.Add)
async def post_edit(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Qo'shish uchun matnni imlo hatolarsiz yuboring !!!")
    
    for i in Variable.global_ls:
        Variable.allTxt += i
        Variable.allTxt += '\n'

    await AboutPhone.next()


@dp.message_handler(state=AboutPhone.AboutConiform)
async def enter_message(msg: Message,state: FSMContext):
    await state.update_data(text=msg.html_text, mention=msg.from_user.get_mention())
    async with state.proxy() as date:
        text = date.get('text')

    await msg.answer("Postni tekshirish uchun yuboraymi?",reply_markup=confirmation_keyboard)
    await AboutPhone.next()
    

@dp.callback_query_handler(post_callback.filter(action="post"), state=AboutPhone.Coniform)
async def confirm_post(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        mention = data.get("mention")
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post Adminga yuborildi")
    await bot.send_message(ADMINS[0], f"Foydalanuvchi {mention} quyidagi postni chop etmoqchi:")
    await bot.send_message(ADMINS[0], Variable.allTxt, parse_mode="HTML", reply_markup=confirmation_keyboard)

    print(Variable.allTxt,Variable.global_ls)

@dp.callback_query_handler(post_callback.filter(action="cancel"), state=AboutPhone.Coniform)
async def cancel_post(call: CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer("Post rad etildi.")


@dp.message_handler(state=AboutPhone.Coniform)
async def post_unknown(message: Message):
    await message.answer("Chop etish yoki rad etishni tanlang")


@dp.callback_query_handler(post_callback.filter(action="post"), user_id=ADMINS)
async def approve_post(call: CallbackQuery):
    await call.answer("Chop etishga ruhsat berdingiz.", show_alert=True)
    target_channel = CHANNELS[0]
    message = await call.message.edit_reply_markup()
    await message.send_copy(chat_id=target_channel)


@dp.callback_query_handler(post_callback.filter(action="cancel"), user_id=ADMINS)
async def decline_post(call: CallbackQuery):
    Variable.allTxt=""
    Variable.global_ls=""
    await call.answer("Post rad etildi.", show_alert=True)
    await call.message.edit_reply_markup()
