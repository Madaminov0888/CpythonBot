# Generated by Django 4.1 on 2023-04-29 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0028_problem_acceptible_languages"),
    ]

    operations = [
        migrations.AddField(
            model_name="problem",
            name="checker",
            field=models.BooleanField(default=False),
        ),
    ]
