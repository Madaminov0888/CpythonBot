import config
from backend.models import *
from aiogram import types, Bot
from html import escape
from button import calc, problems_calc
from states import *
import datetime
from checker import *



async def checkUser(access: bool, user, message: types.Message):
    if access:
        user.username = message.from_user.username
        user.fullname = message.from_user.full_name
        user.save()
        ProblemContestUser.objects.create(user=BotUser.objects.get(chat_id=message.chat.id))
        Variable.objects.create(user=BotUser.objects.get(chat_id=message.chat.id))
        await message.answer(Template.objects.get(title="choose_language").get(user.language),
                             reply_markup=calc("choosing_language", user.language))
    else:
        await message.answer(Template.objects.get(title="menu").get(user.language),
                             reply_markup=calc("main", user.language))
        
        
async def change_language(message: types.CallbackQuery, language):
    user = BotUser.objects.get(chat_id=message.message.chat.id)
    user.language = Button.objects.get(title2=message.data).title2
    user.save()
    await message.message.edit_text(Template.objects.get(title="menu").get(user.language),
                                    reply_markup=calc("main", user.language))
    await message.answer(Template.objects.get(title="language_chose").get(user.language),
                         show_alert=True)
    
    
async def my_profile(message: types.CallbackQuery, language):
    usr = ProblemContestUser.objects.get(user__chat_id=message.message.chat.id)
    await message.message.edit_text(
    f"""
    ➤   KepCoin: {BotUser.objects.get(chat_id=message.message.chat.id).kepcoin}ㅤㅤㅤㅤㅤㅤㅤㅤ
➤   {Template.objects.get(title="my_rating").get(language)}: {usr.rating}
➤   {Template.objects.get(title="max_rating").get(language)}: {usr.big_rating}
➤   {Template.objects.get(title="contests").get(language)}: {usr.contests}
    """,
    reply_markup=calc("profile", language, add_back_button=True)
    )
    
    
async def back_to_menu(message: types.CallbackQuery, language):
    user = Variable.objects.get(user__chat_id=message.message.chat.id)
    user.page = 1
    user.save()
    await message.message.edit_text(Template.objects.get(title="menu").get(language),
                                    reply_markup=calc("main", language))
    

async def show_solved_problems(message: types.CallbackQuery, language):
    user = ProblemContestUser.objects.get(user__chat_id=message.message.chat.id)
    await message.message.edit_text(
        f"""
    ➤   {Template.objects.get(title="beginner").get(language)}: {user.beginner}ㅤㅤㅤㅤㅤㅤㅤ
➤   {Template.objects.get(title="basic").get(language)}: {user.basic}
➤   {Template.objects.get(title="normal").get(language)}: {user.normal}
➤   {Template.objects.get(title="medium").get(language)}: {user.medium}
➤   {Template.objects.get(title="advanced").get(language)}: {user.advanced}
➤   {Template.objects.get(title="hard").get(language)}: {user.hard}

☑   {Template.objects.get(title="total").get(language)}: {user.beginner+user.basic+user.normal+user.medium+user.advanced+user.hard}
        """,
        reply_markup=calc("profile", language, add_back_button=True, get_by_title2=True)
    )
    
    
def get_available_page(page, total_problems, problem):
    per_page = 10
    problems = problem
    total_pages = (total_problems + per_page - 1) // per_page

    # Проверяем, есть ли хотя бы одна попытка
    if total_problems == 0:
        return [[], total_pages]

    if page == total_pages:
        available_problems = total_problems - (total_pages - 1) * per_page
        problems = problems[per_page * (page - 1):per_page * (page - 1) + available_problems]
    else:
        problems = problems[per_page * (page - 1):per_page * page]
    return [problems, total_pages]



async def checkProblem(problem, number="", text="", message: types.CallbackQuery=""):
    
    true = f"✅ {number}{'.' if number != '' else ''} {text}"
    false = f"❌ {number}{'.' if number != '' else ''} {text}"
    
    if type(problem) == UserAttempt and problem.solved:
        return true
        
    else:
        try:
            SolvedProblem.objects.get(user=BotUser.objects.get(chat_id=message.message.chat.id),
                                        attempt=problem)
            return true
        except:
            return false
    
    
        
    
async def get_problems(message: types.CallbackQuery, language, answer=False):
    if answer:
        chat_id = message.chat.id
    else:
        chat_id = message.message.chat.id
    page = Variable.objects.get(user__chat_id=chat_id).page
     # [10*page-10:10*page]
    
    total_problems = Problem.objects.count()

    response = get_available_page(page, total_problems, Problem.objects.all())
    problems = response[0]
    result = ""
    for i in range(len(problems)):
        result += await checkProblem(problems[i], problems[i].pk, problems[i].get(language, 'title'), message)
        result += f" {problems[i].difficulty}\n"
    if answer:
        await message.answer(result, reply_markup=problems_calc(problems, language, page, response[1]))
    else:
        await message.message.edit_text(result, reply_markup=problems_calc(problems, language, page, response[1]))
    
    
async def show_problem(message: types.CallbackQuery, language, problem_id=0, attempt=False):
    user = Variable.objects.get(user__chat_id=message.message.chat.id)
    user.attempt_page = 1
    if attempt:
        problem_id = user.problem_to_solve
    problem = Problem.objects.get(pk=problem_id)
    user.problem_to_solve = problem_id
    user.save()

    await message.message.edit_text(
    f"""
    <b>{problem_id}. {escape(problem.get(language, "title"))}</b>

<strong>{Template.objects.get(title="difficulty").get(language)}: {Problem.difficulties(language).get(problem.difficulty)}</strong>
<strong>{Template.objects.get(title="acceptable_languages").get(language)}: {problem.acceptible_languages}</strong>

{escape(problem.get(language, "condition"))}

<b>{escape(Template.objects.get(title="input_data").get(language))+":" if problem.get(language, "incoming_data") != "" else ""}</b>
{escape(problem.get(language, "incoming_data"))}

<b>{escape(Template.objects.get(title="output_data").get(language))}:</b>
{problem.get(language, "outgoing_data")}

<b>{escape(Template.objects.get(title="example").get(language))+":" if problem.example != "" else ""}</b>
{escape(problem.example)}
""",
    reply_markup=calc("problem", language),
    parse_mode="html"
    )
    
    
async def back_to_problems(message: types.CallbackQuery, language):
    await get_problems(message, language)
    
    
async def settings(message: types.CallbackQuery, language):
    await message.message.edit_text(Template.objects.get(title="choose").get(language),
                                    reply_markup=calc("settings", language, add_back_button=True))
    
    
async def choose_language(message: types.CallbackQuery, language):
    await message.message.edit_text(Template.objects.get(title="choose_language").get(language),
                                    reply_markup=calc("choosing_language", language))
    
    
async def get_solution(message: types.CallbackQuery, language):
    await user_solution.solution.set()
    await message.message.edit_text(Template.objects.get(title="send_solution").get(language),
                                    reply_markup=calc("back_to_problem", language, get_by_title2=True))
    
    
async def check_checker_answer(message: types.Message, language, bot: Bot, message_id, problem: Problem, attempt: UserAttempt, answer=False, no_checker=False, botuser=""):
    if no_checker:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message_id,
                                    text=Template.objects.get(title="no_checker").get(language))
        await show_problem(message, language, problem.pk)
        
        attempt.answer = Template.objects.get(title="no_checker").get(language)
        
        attempt.save()
    
    elif answer:
        SolvedProblem.objects.get_or_create(user=botuser, attempt=problem)
        attempt.answer = Template.objects.get(title="accepted").get(language)
        attempt.solved = True
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message_id,
                                    text=Template.objects.get(title="accepted").get(language))
        await get_problems(message, language, answer=True)
        
        attempt.save()
        
        
    else:
        await bot.edit_message_text(chat_id=message.chat.id,
                                    message_id=message_id,
                                    text=Template.objects.get(title="wrong_answer").get(language))
        await get_problems(message, language, answer=True)
        
        attempt.answer = Template.objects.get(title="wrong_answer").get(language)
    
        attempt.save()
    
async def userSolution(message: types.Message, bot: Bot):
    botuser = BotUser.objects.get(chat_id=message.chat.id)
    problem_id = Variable.objects.get(user__chat_id=message.chat.id)
    problem = Problem.objects.get(pk=problem_id.problem_to_solve)
    user = UserAttempt.objects.create(user=botuser,
                                      problem=problem)
    user.solution = message.text
    date = str(datetime.datetime.now())
    user.date = date.split()[0]
    user.time = date.split()[1].split(".")[0]
    user.status = "checking"
    user.save()
    
    msg = await message.answer(Template.objects.get(title="checking").get(botuser.language))
    for pk, func in return_problem().items():
        if pk == problem_id.problem_to_solve:
            await check_checker_answer(message,
                                       botuser.language,
                                       bot,
                                       msg.message_id,
                                       problem,
                                       attempt=user,
                                       answer=func(message.text),
                                       botuser=botuser
            )
            break
    else:
        await check_checker_answer(message, botuser.language, bot, msg.message_id, no_checker=True)        
        
    

    

async def tests(message: types.CallbackQuery, language):
    categories = TestCategory.objects.all()
    keyboard = types.InlineKeyboardMarkup()
    back = Button.objects.get(title2="back_to_menu")
    for i in categories:
        keyboard.add(types.InlineKeyboardButton(text=i.get("name", language), callback_data=i.title))
    keyboard.add(types.InlineKeyboardButton(text=back.get(language), callback_data=back.title2))
    await message.message.edit_text(Template.objects.get(title="choose").get(language),
                                    reply_markup=keyboard)


async def back_to_category(message: types.CallbackQuery, language):
    await tests(message, language)
    
    
async def get_themes(message: types.CallbackQuery):
    user = BotUser.objects.get(chat_id = message.message.chat.id)
    variable = Variable.objects.get(user=user)
    if message.data.startswith("category_"):
        variable.test_category = message.data
        variable.save()
    themes = TestTheme.objects.filter(category=TestCategory.objects.get(title=variable.test_category))
    keyboard = types.InlineKeyboardMarkup()
    back = Button.objects.get(title2="back_to_category")
    for i in themes:
        keyboard.add(types.InlineKeyboardButton(text=i.get("name", user.language), callback_data=i.title))
    keyboard.add(types.InlineKeyboardButton(text=back.get(user.language), callback_data=back.title2))
    await message.message.edit_text(Template.objects.get(title="choose").get(user.language),
                                    reply_markup=keyboard)


async def give_info_about_theme(message: types.CallbackQuery):
    user = BotUser.objects.get(chat_id = message.message.chat.id)
    variable = Variable.objects.get(user=user)
    theme = TestTheme.objects.get(title=message.data)
    variable.test_theme = message.data
    variable.save()
    keyboard = types.InlineKeyboardMarkup()
    back = Button.objects.get(title2="back_to_themes")
    start = Button.objects.get(title2="start_test")
    keyboard.add(types.InlineKeyboardButton(text=start.get(user.language), callback_data=start.title2))
    keyboard.add(types.InlineKeyboardButton(text=back.get(user.language), callback_data=back.title2))
    await message.message.edit_text(
    f"""
    {Template.objects.get(title="category").get(user.language)}: {theme.category}
{Template.objects.get(title="theme").get(user.language)}: {theme.get("name", user.language)}
━━━━━━━━━━━━━━━━━
{Template.objects.get(title="difficulty").get(user.language)}: {Problem.difficulties(user.language)[theme.difficulty]}
━━━━━━━━━━━━━━━━━
{Template.objects.get(title="best_result").get(user.language)}: {theme.best_result}/{theme.number_of_questions}
━━━━━━━━━━━━━━━━━
{Template.objects.get(title="test_number").get(user.language)}: {theme.number_of_questions}
━━━━━━━━━━━━━━━━━
{Template.objects.get(title="passed_number").get(user.language)}: {theme.passed}
    """,
    reply_markup=keyboard
    )
    
    
def make_problem_calc(message: types.CallbackQuery, language, id=0, editing=False):
    variable = Variable.objects.get(user__chat_id=message.message.chat.id)
    problem = Problem.objects.get(pk=variable.problem_to_solve)
    problems = UserAttempt.objects.filter(user__chat_id=message.message.chat.id,
                                          problem=problem)
    
    response = get_available_page(variable.attempt_page, problems.count(), problems)
    
    return problems_calc(response[0], 
                         language, 
                         variable.attempt_page,
                         response[1],
                         attempts=True,
                         editing=editing,
                         id=id
                         )
    
    
async def get_attempts(message: types.CallbackQuery, language):
    variable = Variable.objects.get(user__chat_id=message.message.chat.id)
    problem = Problem.objects.get(pk=variable.problem_to_solve)
    problems = UserAttempt.objects.filter(user__chat_id=message.message.chat.id,
                                          problem=problem)

    result = f"{problem.get(language, 'title')}\n\n"
        
    response = get_available_page(variable.attempt_page, problems.count(), problems)
    #result += await checkProblem(problems[i], problems[i].pk, problems[i].get(language, 'title'), message)
    for n, i in enumerate(response[0]):
        print(i)
        result += f"{await checkProblem(problem=i, message=message)} {n+1}. | {i.date} | {i.time} | ({i.pk})\n"
    await message.message.edit_text(result,
                                    reply_markup=make_problem_calc(message, language))


async def left_and_right(message: types.CallbackQuery, language, attempts=False):
    user = Variable.objects.get(user__chat_id=message.message.chat.id)
    if message.data.split()[0] == Template.objects.get(title="left").title:
        if attempts:
            user.attempt_page -= 1
        else:
            user.page -= 1
    else:
        if attempts:
            user.attempt_page += 1
        else:
            user.page += 1
    user.save()
    if not attempts:
        await get_problems(message, language)
    else:
        await get_attempts(message, language)
    
    print
async def get_user_attempt(message: types.CallbackQuery, language):
    id = int(message.data.split()[0])
    attempt = UserAttempt.objects.filter(user__chat_id=message.message.chat.id, pk=id)
    text = f"""
    {Template.objects.get(title="result").get(language)}: {attempt[0].answer}
{Template.objects.get(title="attempt").get(language)}: {attempt[0].pk}

{attempt[0].solution}
    """
    await message.message.edit_text(text, reply_markup=make_problem_calc(message, language, id, editing=True))
    
    
async def back_to_themes(message: types.CallbackQuery, language):
    await get_themes(message)


    