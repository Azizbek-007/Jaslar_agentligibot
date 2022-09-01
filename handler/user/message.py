from aiogram import types
from filters.join_check import  IsMember
from loader import dp, bot
from datetime import datetime
from pytz import timezone
from data.config import chat_id

@dp.message_handler(IsMember(), content_types=['text'], chat_type=types.ChatType.PRIVATE)
async def send_answer(message: types.Message):
    tz = timezone("Asia/Tashkent")
    dt_format = "%Y-%m-%d %H:%M:%S"
    moscowZone = datetime.now(tz)
    time = moscowZone.strftime(dt_format)
    a = await message.forward(chat_id)
    await a.reply(f"👆⏳{time}\n\n```{message.from_user.id}```", parse_mode='markdown')
    await message.reply("Sizdiń juwabıńız qabıllandı ✔️")
 
