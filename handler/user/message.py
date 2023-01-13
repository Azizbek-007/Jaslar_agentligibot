from aiogram import types
from filters.join_check import  IsMember
from loader import dp
from datetime import datetime
from pytz import timezone
from data.config import chat_id

@dp.message_handler(IsMember(), content_types=['text'], chat_type=types.ChatType.PRIVATE)
async def send_answer(message: types.Message):
    time_zone = timezone("Asia/Tashkent")
    date_time_format = "%Y-%m-%d %H:%M:%S"
    Zone = datetime.now(time_zone)
    time = Zone.strftime(date_time_format)
    user_message = await message.forward(chat_id)
    await user_message.reply(f"👆⏳{time}\n\n```{message.from_user.id}```", parse_mode='markdown')
    await message.reply("Sizdiń juwabıńız qabıllandı ✔️")
 
