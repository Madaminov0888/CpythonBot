# Generated by Django 4.1 on 2023-04-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0003_contest_problem"),
    ]

    operations = [
        migrations.AddField(
            model_name="contest",
            name="ending_date",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="contest",
            name="starting_date",
            field=models.CharField(default="", max_length=255),
        ),
    ]
