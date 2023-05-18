# Generated by Django 4.1 on 2023-04-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0002_button_alter_botuser_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("status", models.CharField(max_length=255)),
                ("starting_time", models.CharField(max_length=255)),
                ("ending_time", models.CharField(max_length=255)),
                ("contestType", models.CharField(max_length=255)),
                ("number_of_participants", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Problem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=1000)),
                ("difficulty", models.CharField(max_length=255)),
                ("rating", models.CharField(max_length=255)),
                ("time_limit", models.IntegerField(default=1000)),
                ("memory_limit", models.IntegerField(default=250)),
                ("condition", models.TextField()),
                ("incoming_data", models.TextField()),
                ("outgoing_data", models.TextField()),
                ("example", models.TextField()),
            ],
        ),
    ]