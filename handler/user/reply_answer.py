from aiogram import types
from loader import dp, bot

@dp.message_handler(is_reply=True)
async def reply_answer(message: types.Message):
    try:
        user_id = message.reply_to_message.text.split('\n')[2]
        await bot.send_message(user_id, message.text)
        await message.reply("Jiberildi")
    except:
        await message.answer("Jiberimedi")