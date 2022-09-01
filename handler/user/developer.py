from aiogram import types
from loader import dp

@dp.message_handler(commands=['developer'])
async def developer_com(message: types.Message):
    await message.answer("👨‍💻 @Azizbek_Berdimuratov")
 