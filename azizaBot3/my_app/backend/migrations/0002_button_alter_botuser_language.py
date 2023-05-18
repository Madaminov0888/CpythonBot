# Generated by Django 4.1 on 2023-04-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Button",
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
                ("title2", models.CharField(max_length=255)),
                ("body_uz", models.CharField(max_length=255)),
                ("body_ru", models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name="botuser",
            name="language",
            field=models.CharField(default="uz", max_length=10),
        ),
    ]
