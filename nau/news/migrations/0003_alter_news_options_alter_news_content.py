# Generated by Django 5.1.2 on 2025-05-11 23:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_news_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name": "News"},
        ),
        migrations.AlterField(
            model_name="news",
            name="content",
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
