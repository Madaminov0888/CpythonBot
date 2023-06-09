# Generated by Django 4.1 on 2023-05-17 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0045_alter_solvedproblem_attempt"),
    ]

    operations = [
        migrations.AddField(
            model_name="userattempt",
            name="solved",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="solvedproblem",
            name="attempt",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="backend.problem"
            ),
        ),
    ]
