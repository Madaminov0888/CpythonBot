# Generated by Django 4.1 on 2023-04-30 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0034_remove_testcategory_name_testcategory_name_ru_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testcategory",
            name="best_result",
        ),
        migrations.RemoveField(
            model_name="testcategory",
            name="difficulty",
        ),
        migrations.RemoveField(
            model_name="testcategory",
            name="number_of_questions",
        ),
        migrations.RemoveField(
            model_name="testcategory",
            name="passed",
        ),
        migrations.CreateModel(
            name="TestTheme",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("name_uz", models.CharField(max_length=255)),
                ("name_ru", models.CharField(max_length=255)),
                ("number_of_questions", models.IntegerField()),
                ("best_result", models.IntegerField(default=0)),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("🟢", "beginner"),
                            ("🟡", "normal"),
                            ("🟠", "medium"),
                            ("🔴", "hard"),
                        ],
                        max_length=255,
                    ),
                ),
                ("passed", models.IntegerField(default=0)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.testcategory",
                    ),
                ),
            ],
        ),
    ]
