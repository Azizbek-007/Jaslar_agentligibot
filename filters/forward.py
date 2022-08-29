from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import bot

class Forward(BoundFilter):
    async def check(self, message: types.Message):
       return await message.forward_from