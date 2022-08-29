from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import channel_link

def channels_btn():
    markup = InlineKeyboardMarkup()
    i = 1
    for x in channel_link:
        markup.add(InlineKeyboardButton(text=f'{i}-Kanal', url=x))
        i = i + 1
    markup.add(InlineKeyboardButton("✅Tekseriw", callback_data="check"))
    return markup
