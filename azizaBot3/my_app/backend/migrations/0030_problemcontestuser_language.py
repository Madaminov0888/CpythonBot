# Generated by Django 4.1 on 2023-04-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0029_problem_checker"),
    ]

    operations = [
        migrations.AddField(
            model_name="problemcontestuser",
            name="language",
            field=models.CharField(default="", max_length=255),
        ),
    ]
