from aiogram import types, executor, Dispatcher, Bot
import config
from backend.models import BotUser, Template
from function import *

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user, access = BotUser.objects.get_or_create(chat_id=message.chat.id)
    await checkUser(access, user, message)
    
    
@dp.callback_query_handler(lambda query: True)
async def callback(message: types.CallbackQuery):
    user = BotUser.objects.get(chat_id=message.message.chat.id)
    for text, func in processingCalbacks(user.language).items():
        if text == message.data:
            await func(message, user.language)
            break











executor.start_polling(skip_updates=True, dispatcher=dp)