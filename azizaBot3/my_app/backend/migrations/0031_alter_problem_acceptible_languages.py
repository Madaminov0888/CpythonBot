# Generated by Django 4.1 on 2023-04-29 12:40

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0030_problemcontestuser_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="acceptible_languages",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("java", "Java 20"),
                    ("python", "Python 3.10"),
                    ("cpp", "C++ 20"),
                ],
                default="",
                max_length=255,
            ),
        ),
    ]
