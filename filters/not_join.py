from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from loader import bot
from data.config import channel_id

class IsNoMember(BoundFilter):
    async def check(self, message: types.Message):
        statuses = []
        for x in channel_id:
            get_chat = await bot.get_chat_member(x, message.from_user.id)
            statuses.append(get_chat.status)
        if 'left' in statuses: return True