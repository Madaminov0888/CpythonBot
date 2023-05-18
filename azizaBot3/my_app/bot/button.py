import config
from aiogram import types
from backend.models import Button, Template

def calc(location, lang, add_back_button=False, get_by_title2=False, row_width=1):
    if not get_by_title2:
        texts = Button.objects.filter(title=location)
    else:
        texts = Button.objects.filter(title2=location)
    key = types.InlineKeyboardMarkup(row_width=row_width)
    btns = [types.InlineKeyboardButton(text=i.get(lang), callback_data=i.title2) for i in texts]
    key.add(*btns)
    if add_back_button:
        t = Button.objects.get(title2='back_to_menu')
        key.add(types.InlineKeyboardButton(text=t.get(lang), callback_data=t.title2))
    return key


def problems_calc(problems, language, page, total_pages, id=0, attempts=False, editing=False, ):
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    if attempts:
        space = Template.objects.get(title="space").get(language)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        buttons = [types.InlineKeyboardButton(text=(lambda text: text+" ✅" if editing and i.pk == id else text)(f"{space}{n+1}. {i.date}  {i.time}{space}"), callback_data=f"{i.pk} n") for n, i in enumerate(problems)]
    else:
        buttons = [types.InlineKeyboardButton(text=i.pk, callback_data=i.pk) for i in problems]
    keyboard.add(*buttons)
    left = Template.objects.get(title="left")
    right = Template.objects.get(title="right")
    
    left_button = types.InlineKeyboardButton(text=left.get(language), callback_data=left.title)
    right_button = types.InlineKeyboardButton(text=right.get(language), callback_data=right.title)
    if attempts:
        left_button = types.InlineKeyboardButton(text=left.get(language), callback_data=f"{left.title} a")
        right_button = types.InlineKeyboardButton(text=right.get(language), callback_data=f"{right.title} a")
        
    if (len(problems) == 0 or total_pages == 1):
        pass
    elif (page == 1 and total_pages > 1):
        keyboard.add(right_button)
    elif (page == total_pages and total_pages > 1):
        keyboard.add(left_button)
    else:
        keyboard.row(left_button,
                     right_button)
    t = Button.objects.get(title2='back_to_menu')
    if attempts:
        t = Button.objects.get(title2='back_to_problem')
    keyboard.add(types.InlineKeyboardButton(text=t.get(language), callback_data=t.title2))
    return keyboard


