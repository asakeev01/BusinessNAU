# Generated by Django 5.1.2 on 2024-11-25 16:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0002_link_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="block",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
