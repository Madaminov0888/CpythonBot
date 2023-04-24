from django.contrib import admin
from .models import BotUser, Template, Button, Problem, Contest, ProblemContestUser
# Register your models here.

@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ["chat_id", "fullname", "username", "kepcoin", "language", "status"]
    list_display_links = ["chat_id", "fullname", "username", "kepcoin", "language", "status"]
    search_fields = ["chat_id", "fullname", "username", "kepcoin", "language", "status"]
    
    
@admin.register(ProblemContestUser)
class ProblemContestUserAdmin(admin.ModelAdmin):
    list_display = ["chat_id", "rating", "big_rating", "contests", "beginner", "basic", "normal", "medium", "advanced", "hard"]
    list_display_links = ["chat_id", "rating", "big_rating", "contests", "beginner", "basic", "normal", "medium", "advanced", "hard"]
    search_fields = ["chat_id", "rating", "big_rating", "contests", "beginner", "basic", "normal", "medium", "advanced", "hard"]
    

@admin.register(Template)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ["title", "body_uz", "body_ru"]
    list_display_links = ["title", "body_uz", "body_ru"]
    search_fields = ["title", "body_uz", "body_ru"]
    
    
@admin.register(Button)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ["title", "title2", "body_uz", "body_ru"]
    list_display_links = ["title", "title2", "body_uz", "body_ru"]
    search_fields = ["title", "title2", "body_uz", "body_ru"]
    

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ["title", "difficulty", "rating", "time_limit", "memory_limit", "condition", "incoming_data", "outgoing_data", "example"]
    list_display_links = ["title", "difficulty", "rating", "time_limit", "memory_limit", "condition", "incoming_data", "outgoing_data", "example"]
    search_fields = ["title", "difficulty", "rating", "time_limit", "memory_limit", "condition", "incoming_data", "outgoing_data", "example"]


@admin.register(Contest)
class ContestAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "starting_date", "starting_time", "ending_date", "ending_time", "contestType", "number_of_participants"]
    list_display_links = ["title", "status", "starting_time", "ending_time", "contestType", "number_of_participants"]
    search_fields = ["title", "status", "starting_time", "ending_time", "contestType", "number_of_participants"]









