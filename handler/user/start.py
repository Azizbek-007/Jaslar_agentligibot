from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.join_check import  IsMember
from filters.not_join import IsNoMember
from loader import dp
from keyboard.inline.channels import channels_btn

@dp.message_handler(IsNoMember(), content_types=['text'], chat_type=types.ChatType.PRIVATE)
async def nomember(message: types.Message):
    await message.answer("Siz juwap jazıw ushın tómendegi kanallarǵa aǵza bolıwıńız kerek:",
    reply_markup=channels_btn())

@dp.message_handler(IsMember(), CommandStart(), chat_type=types.ChatType.PRIVATE)
async def start(message: types.Message):
    await message.answer("Assalawma áleykum. Xosh keldińiz. Usı bot arqalı Siz sorawlarǵa juwap berseńiz boladı.")


