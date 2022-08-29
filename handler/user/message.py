from aiogram import types
from filters.join_check import  IsMember
from loader import dp, bot
import datetime
import pytz
from data.config import chat_id

@dp.message_handler(IsMember(), content_types=['text'], chat_type=types.ChatType.PRIVATE)
async def send_answer(message: types.Message):
    tz = pytz.timezone("Asia/Tashkent")
    now = tz.localize(datetime.datetime.now())
    time = now.strftime('%Y-%m-%d %H:%M:%S')
    await message.forward(chat_id)
    await bot.send_message(chat_id, text=f"👆⏳{time}")
    await message.reply("Sizdiń juwabıńız qabıllandı ✔️")
