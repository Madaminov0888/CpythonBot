# Generated by Django 4.1 on 2023-05-16 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0042_alter_solvedproblem_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="solvedproblem",
            name="problem_number",
        ),
    ]
