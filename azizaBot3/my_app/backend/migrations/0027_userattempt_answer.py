# Generated by Django 4.1 on 2023-04-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0026_userattempt_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="userattempt",
            name="answer",
            field=models.CharField(default="", max_length=255),
        ),
    ]