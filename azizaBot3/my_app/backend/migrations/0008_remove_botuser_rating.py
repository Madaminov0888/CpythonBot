# Generated by Django 4.1 on 2023-04-23 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0007_problemcontestuser"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="botuser",
            name="rating",
        ),
    ]