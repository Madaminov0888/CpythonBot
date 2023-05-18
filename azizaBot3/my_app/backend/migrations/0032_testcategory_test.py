# Generated by Django 4.1 on 2023-04-29 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0031_alter_problem_acceptible_languages"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestCategory",
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
                ("name", models.CharField(max_length=255)),
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
            ],
        ),
        migrations.CreateModel(
            name="Test",
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
                ("question", models.TextField()),
                ("answer", models.CharField(max_length=255)),
                ("option1", models.CharField(max_length=255)),
                ("option2", models.CharField(max_length=255)),
                ("option3", models.CharField(max_length=255)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.testcategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.botuser",
                    ),
                ),
            ],
        ),
    ]
