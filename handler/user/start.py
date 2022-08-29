from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.join_check import  IsMember
from filters.not_join import IsNoMember
from loader import dp
from keyboard.inline import channels

@dp.message_handler(IsNoMember(), CommandStart())
async def nomember(message: types.Message):
    await message.answer("Siz juwap jazıw ushın tómendegi kanallarǵa aǵza bolıwıńız kerek:",
    reply_markup=channels())

@dp.message_handler(IsMember(), CommandStart())
async def start(message: types.Message):
    await message.answer("hello", 'html')

