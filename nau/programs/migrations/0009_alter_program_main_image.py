# Generated by Django 5.1.2 on 2025-05-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0008_program_main_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="program",
            name="main_image",
            field=models.ImageField(upload_to=""),
        ),
    ]
