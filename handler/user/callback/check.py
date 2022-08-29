from aiogram import types
from filters.join_check import  IsMember
from filters.not_join import IsNoMember
from loader import dp

@dp.callback_query_handler(IsNoMember(), text="check")
async def no_member(call: types.CallbackQuery):
    await call.answer("Siz kanallarǵa aǵza bolmaǵansız!", True)

@dp.callback_query_handler(IsMember(), text="check")
async def is_member(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Assalawma áleykum. Xosh keldińiz. Usı bot arqalı Siz sorawlarǵa juwap berseńiz boladı.")
