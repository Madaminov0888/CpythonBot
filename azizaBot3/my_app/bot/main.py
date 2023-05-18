from aiogram import types, executor, Dispatcher, Bot
import config
from backend.models import BotUser, Template
from function import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from states import *
from aiogram.dispatcher.storage import FSMContext
from contextlib import suppress
import importlib


storage = MemoryStorage()
bot = Bot(token=config.TOKEN, parse_mode="HTML")
dp = Dispatcher(bot=bot, storage=storage)


def check_request_to_side(req: types.CallbackQuery):
    r = req.data.split()
    if len(r) > 1:
        if r[1] == "a":
            return True
    return False

def check_request_to_number(req: types.CallbackQuery):
    r = req.data.split()
    if len(r) > 1:
        if r[1] == "n":
            return True
    return False


@dp.callback_query_handler(lambda c: c.data == 'back_to_problem', state=user_solution.solution)
async def callback_finish(query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await show_problem(query,
                       language=BotUser.objects.get(chat_id=query.message.chat.id).language,
                       problem_id=Variable.objects.get(user__chat_id=query.message.chat.id).problem_to_solve)
    


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    user, access = BotUser.objects.get_or_create(chat_id=message.chat.id)
    await checkUser(access, user, message)
    

@dp.message_handler(state=user_solution.solution)
async def solution(message: types.Message, state: FSMContext):
    await userSolution(message, bot=bot)
    await state.finish()
    
    
@dp.callback_query_handler(lambda query: query.data.startswith('category_'))
async def get_theme(message: types.CallbackQuery):
    await get_themes(message)
    
    
@dp.callback_query_handler(lambda query: query.data.startswith('theme_'))
async def get_theme_about(message: types.CallbackQuery):
    await give_info_about_theme(message)
    
    
@dp.callback_query_handler(lambda query: check_request_to_side(query))
async def left_to_right(message: types.CallbackQuery):
    await left_and_right(message, BotUser.objects.get(chat_id=message.message.chat.id).language, attempts=True)
    
    
@dp.callback_query_handler(lambda query: check_request_to_number(query))
async def attempt_numbers(message: types.CallbackQuery):
    await get_user_attempt(message, BotUser.objects.get(chat_id=message.message.chat.id).language)
    
    
@dp.callback_query_handler(lambda query: True)
async def callback(message: types.CallbackQuery, state: FSMContext):
    user = BotUser.objects.get(chat_id=message.message.chat.id)
    try:
        problem_id = int(message.data)
        await show_problem(message, user.language, problem_id)
    except Exception as ex:
        buttons = Button.objects.all()
        
        for i in buttons:
            if  i.fucntion is None:
                continue
            elif i.title2 == message.data:
                func = getattr(importlib.import_module("function") ,i.fucntion)
                if i.title2 == "back_to_problem":
                    await func(message, user.language, attempt=True)
                else:
                    await func(message, user.language)
                    
        
      











executor.start_polling(skip_updates=True, dispatcher=dp)