from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class BotUser(models.Model):
    chat_id = models.IntegerField()
    username = models.CharField(max_length=255)
    fullname = models.CharField(max_length=255)
    language = models.CharField(max_length=10, default="uz")
    status = models.CharField(max_length=255, default="user")
    kepcoin = models.IntegerField(default=0)
    new_user = models.BooleanField(default=True)
    
    def __str__(self):
        return self.fullname
    
    
class ProblemContestUser(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE, null=True)
    rating = models.IntegerField(default=0)
    language = models.CharField(max_length=255, default="")
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
    fucntion = models.CharField(max_length=255, null=True, blank=True)

    def get(self, lang):
        return getattr(self, f"body_{lang}")
    
    def __str__(self):
        return self.title2
    
    
class Problem(models.Model):
    class Difficulties(models.TextChoices):
        beginner = "🟢", "beginner"
        normal = "🟡", "normal"
        medium = "🟠", "medium"
        hard = "🔴", "hard"
    
    def difficulties(language, element = Difficulties.choices):
        DIFFICULTY_CHOICES = {choice[0]: Template.objects.get(title=choice[1]).get(language) for choice in element}
        return DIFFICULTY_CHOICES
    
    MY_CHOICES = (
        ("java", "Java 20"),
        ("python", "Python 3.10"),
        ("cpp", "C++ 20")
    )
        
    title_uz = models.CharField(max_length=1000, default="")
    title_ru = models.CharField(max_length=1000, default="")
    difficulty = models.CharField(max_length=255, choices=Difficulties.choices)
    acceptible_languages = MultiSelectField(choices=MY_CHOICES, max_choices=len(MY_CHOICES), max_length=255, default="")
    rating = models.FloatField(default=0)
    time_limit = models.IntegerField(default=1000)
    memory_limit = models.IntegerField(default=250)
    condition_uz = models.TextField(default="")
    condition_ru = models.TextField(default="")
    incoming_data_uz = models.TextField(null=True, blank=True)
    incoming_data_ru = models.TextField(null=True, blank=True)
    outgoing_data_uz = models.TextField(default="Yagona qatorda masala yechimi")
    outgoing_data_ru = models.TextField(default="Результат вычисления.")
    example = models.TextField(null=True, blank=True)
    checker = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title_uz
    
    def get(self, language, field):
        return getattr(self, f"{field}_{language}")


class Contest(models.Model):
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    starting_date = models.CharField(max_length=255, default="")
    starting_time = models.CharField(max_length=255)
    ending_date = models.CharField(max_length=255, default="")
    ending_time = models.CharField(max_length=255)
    contestType = models.CharField(max_length=255)
    number_of_participants = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    
class Variable(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    page = models.IntegerField(default=1)
    attempt_page = models.IntegerField(default=1)
    problem_to_solve = models.IntegerField(null=True)
    test_category = models.CharField(max_length=255, default="", blank=True)
    test_theme = models.CharField(max_length=255, default="", blank=True)
    
    
class UserAttempt(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    time = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    solution = models.TextField()
    status = models.CharField(default="not_checked", max_length=255)
    answer = models.CharField(max_length=255, default="")
    solved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.problem.title_uz} | {self.date} | {self.time}"
    
    
class SolvedProblem(models.Model):
    user = models.ForeignKey(BotUser, on_delete=models.CASCADE)
    attempt = models.ForeignKey(Problem, on_delete=models.CASCADE)
        

class TestCategory(models.Model):
    title = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255, default="")
    name_ru = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.name_uz
    
    def get(self, name, language):
        return getattr(self, f"{name}_{language}")
    
    
class TestTheme(models.Model):
    title = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE)
    number_of_questions = models.IntegerField()
    best_result = models.IntegerField(default=0)
    difficulty = models.CharField(choices=Problem.Difficulties.choices, max_length=255)
    passed = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name_uz
    
    def get(self, name, language):
        return getattr(self, f"{name}_{language}")


class Test(models.Model):
    theme = models.ForeignKey(TestTheme, on_delete=models.CASCADE, default="")
    question_uz = models.TextField(default="")
    answer_uz = models.CharField(max_length=255)
    option1_uz = models.CharField(max_length=255, default="")
    option2_uz = models.CharField(max_length=255, default="")
    option3_uz = models.CharField(max_length=255, default="")
    question_ru = models.TextField(default="")
    answer_ru = models.CharField(max_length=255, default="")
    option1_ru = models.CharField(max_length=255, default="")
    option2_ru = models.CharField(max_length=255, default="")
    option3_ru = models.CharField(max_length=255, default="")
    
    def get(self, name, language):
        return getattr(self, f"{name}_{language}")
    
    
    

"""
class Test(models.Model):
    pass
"""

