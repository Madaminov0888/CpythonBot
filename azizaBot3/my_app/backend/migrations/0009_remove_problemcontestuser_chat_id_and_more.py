# Generated by Django 4.1 on 2023-04-24 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0008_remove_botuser_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="problemcontestuser",
            name="chat_id",
        ),
        migrations.AddField(
            model_name="problemcontestuser",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="backend.botuser",
            ),
        ),
    ]
