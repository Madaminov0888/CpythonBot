import config
from aiogram import types
from backend.models import Button, Template

def calc(location, lang, add_back_button=False):
    texts = Button.objects.filter(title=location)
    key = types.InlineKeyboardMarkup(row_width=2)
    btns = [types.InlineKeyboardButton(text=i.get(lang), callback_data=i.get(lang)) for i in texts]
    key.add(*btns)
    if add_back_button:
        t = Button.objects.get(title2='back').get(lang)
        key.add(types.InlineKeyboardButton(text=t, callback_data=t))
    return key