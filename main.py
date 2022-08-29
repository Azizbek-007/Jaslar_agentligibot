import logging

from utils.commonds import  set_default_commands

logging.basicConfig(level=logging.INFO)

async def on_startup(dp):
    from handler.user import start
    await set_default_commands(dp)

if __name__ == '__main__':
    from aiogram import executor
    from loader import dp
    executor.start_polling(dp, on_startup=on_startup)