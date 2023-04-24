from backend.models import BotUser, Template, Button, ProblemContestUser
from aiogram import types
from button import calc

async def checkUser(access: bool, user, message: types.Message):
    if access:
        user.username = message.from_user.username
        user.fullname = message.from_user.full_name
        user.save()
        ProblemContestUser.objects.create(chat_id=message.chat.id)
        await message.answer(Template.objects.get(title="choose_language").get(user.language),
                             reply_markup=calc("choosing_language", user.language))
    else:
        await message.answer(Template.objects.get(title="menu").get(user.language),
                             reply_markup=calc("main", user.language))
        
        
async def change_language(message: types.CallbackQuery, language):
    user = BotUser.objects.get(chat_id=message.message.chat.id)
    user.language = Button.objects.get(body_uz=message.data).title2
    user.save()
    await message.message.edit_text(Template.objects.get(title="menu").get(user.language),
                                    reply_markup=calc("main", user.language))
    await message.answer(Template.objects.get(title="language_chose").get(user.language),
                         show_alert=True)
    
    
async def my_profile(message: types.CallbackQuery, language):
    user = ProblemContestUser.objects.get(chat_id=message.message.chat.id)
    await message.message.edit_text(
    f"""
        KepCoin: {BotUser.objects.get(chat_id=message.message.chat.id).kepcoin}
    {Template.objects.get(title="my_rating").get(language)}: {user.rating}
    {Template.objects.get(title="max_rating").get(language)}: {user.big_rating}
    {Template.objects.get(title="contests").get(language)}: {user.contests}
    """,
    reply_markup=calc("profile", language, add_back_button=True)
    )







def processingCalbacks(language):
    dt = {
        Button.objects.get(title2="uz").get(language): change_language,
        Button.objects.get(title2="ru").get(language): change_language,
        Button.objects.get(title2="profile").get(language): my_profile,
    }
    return dt
    