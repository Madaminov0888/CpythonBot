# Generated by Django 4.1 on 2023-04-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0033_rename_answer_test_answer_uz_remove_test_option1_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testcategory",
            name="name",
        ),
        migrations.AddField(
            model_name="testcategory",
            name="name_ru",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="testcategory",
            name="name_uz",
            field=models.CharField(default="", max_length=255),
        ),
    ]