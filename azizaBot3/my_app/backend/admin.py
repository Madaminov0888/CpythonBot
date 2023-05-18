from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ["chat_id", "fullname", "username", "kepcoin", "language", "status"]
    list_display_links = ["chat_id", "fullname", "username", "kepcoin", "language", "status"]
    search_fields = ["chat_id", "fullname", "username", "kepcoin", "language", "status"]
    
    
@admin.register(SolvedProblem)
class SolvedProblemAdmin(admin.ModelAdmin):
    list_display = ["user", "attempt"]
    list_display_links = ["user", "attempt"]
    search_fields = ["user", "attempt"]
    
    
@admin.register(ProblemContestUser)
class ProblemContestUserAdmin(admin.ModelAdmin):
    list_display = ["user", "rating", "language", "big_rating", "contests", "beginner", "basic", "normal", "medium", "advanced", "hard"]
    list_display_links = ["user", "rating", "language", "big_rating", "contests", "beginner", "basic", "normal", "medium", "advanced", "hard"]
    search_fields = ["user", "rating", "language", "big_rating", "contests", "beginner", "basic", "normal", "medium", "advanced", "hard"]
    

@admin.register(Template)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ["title", "body_uz", "body_ru"]
    list_display_links = ["title", "body_uz", "body_ru"]
    search_fields = ["title", "body_uz", "body_ru"]
    
    
@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_display = ["user", "page", "attempt_page", "problem_to_solve", "test_category", "test_theme"]
    list_display_links = ["user", "page", "attempt_page", "problem_to_solve", "test_category", "test_theme"]
    search_fields = ["user", "page", "attempt_page", "problem_to_solve", "test_category", "test_theme"]
    
    
@admin.register(Button)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ["title", "title2", "body_uz", "body_ru"]
    list_display_links = ["title", "title2", "body_uz", "body_ru"]
    search_fields = ["title", "title2", "body_uz", "body_ru"]
    

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ["title_uz", "difficulty", "acceptible_languages", "rating", "time_limit", "memory_limit", "checker"]
    list_display_links = ["title_uz", "difficulty", "acceptible_languages", "rating", "time_limit", "memory_limit"]
    search_fields = ["title_uz", "difficulty", "acceptible_languages", "rating", "time_limit", "memory_limit", "condition_uz", "incoming_data_uz", "outgoing_data_uz", "example"]


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "starting_date", "starting_time", "ending_date", "ending_time", "contestType", "number_of_participants"]
    list_display_links = ["title", "status", "starting_time", "ending_time", "contestType", "number_of_participants"]
    search_fields = ["title", "status", "starting_time", "ending_time", "contestType", "number_of_participants"]


@admin.register(UserAttempt)
class UserAttemptAdmin(admin.ModelAdmin):
    list_display = ["user", "problem", "time", "date", "status", "answer", "solved"]
    list_display_links = ["user", "problem", "time", "date", "status", "answer", "solved"]
    search_fields = ["user", "problem", "time", "date", "status", "answer", "solved"]


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ["theme", "question_uz", "answer_uz", "option1_uz", "option2_uz", "option3_uz"]
    list_display_links = ["theme", "question_uz", "answer_uz", "option1_uz", "option2_uz", "option3_uz"]
    search_fields = ["theme", "question_uz", "answer_uz", "option1_uz", "option2_uz", "option3_uz"]
    
    
@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "name_uz", ]
    list_display_links = ["title", "name_uz"]
    search_fields = ["title", "name_uz"]


@admin.register(TestTheme)
class TestThemeAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "name_uz", "number_of_questions", "best_result", "difficulty", "passed"]
    list_display_links = ["title", "category", "name_uz", "number_of_questions", "best_result", "difficulty", "passed"]
    search_fields = ["title", "category", "name_uz", "number_of_questions", "best_result", "difficulty", "passed"]

