# Generated by Django 4.1 on 2023-04-30 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0036_remove_test_category_test_theme"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="test",
            name="user",
        ),
    ]
