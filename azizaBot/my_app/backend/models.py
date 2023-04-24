from django.db import models

# Create your models here.
class BotUser(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    language = models.CharField(max_length=10, default="uz")
    status = models.CharField(max_length=255, default="user")
    kepcoin = models.IntegerField(default=0)
    new_user = models.BooleanField(default=True)
    
    
class ProblemContestUser(models.Model):
    chat_id = models.IntegerField()
    rating = models.IntegerField(default=0)
    big_rating = models.IntegerField(default=0)
    contests = models.IntegerField(default=0)
    beginner = models.IntegerField(default=0)
    basic = models.IntegerField(default=0)
    normal = models.IntegerField(default=0)
    medium = models.IntegerField(default=0)
    advanced = models.IntegerField(default=0)
    hard = models.IntegerField(default=0)
    
    
    
class Template(models.Model):
    title = models.CharField(max_length=255)
    body_uz = models.TextField()
    body_ru = models.TextField()

    def get(self, lang):
        return getattr(self, f"body_{lang}")
    
    
class Button(models.Model):
    title = models.CharField(max_length=255)
    title2 = models.CharField(max_length=255)
    body_uz = models.CharField(max_length=255)
    body_ru = models.CharField(max_length=255)

    def get(self, lang):
        return getattr(self, f"body_{lang}")
    
    
class Problem(models.Model):
    title = models.CharField(max_length=1000)
    difficulty = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    time_limit = models.IntegerField(default=1000)
    memory_limit = models.IntegerField(default=250)
    condition = models.TextField()
    incoming_data = models.TextField()
    outgoing_data = models.TextField()
    example = models.TextField()


class Contest(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    starting_date = models.CharField(max_length=255, default="")
    starting_time = models.CharField(max_length=255)
    ending_date = models.CharField(max_length=255, default="")
    ending_time = models.CharField(max_length=255)
    contestType = models.CharField(max_length=255)
    number_of_participants = models.IntegerField(default=0)
    
    
    


"""
class Test(models.Model):
    pass
"""

