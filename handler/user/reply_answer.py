from aiogram import types
from filters.forward import Forward
from loader import dp, bot

@dp.message_handler(Forward(), is_reply=True)
async def reply_answer(message: types.Message):
    try:
        forward_user_id = await message.forward_from.id
        await bot.send_message(forward_user_id, message.text)
    except:
        await message.answer("User anonim sebepli jiberilmedi 2-usildan paydalanin'")