# Generated by Django 5.1.2 on 2024-12-05 19:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
