from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import channel_link

def channels_btn():
    markup = InlineKeyboardMarkup()
    i = 1
    for x in channel_link:
        markup.add(InlineKeyboardButton(text=f'{i}-Kanal', url=x))
    markup.add(InlineKeyboardButton("✅Tekseriw "))
    return markup
