# Generated by Django 5.1.2 on 2025-05-18 04:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("flyer", models.ImageField(upload_to="")),
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("date", models.DateTimeField()),
                ("place", models.CharField(max_length=255)),
                ("speaker", models.CharField(max_length=255)),
                ("speaker_link", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="EventsPageConfig",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("header_image", models.ImageField(upload_to="")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EventType",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="EventImage",
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
                ("image", models.ImageField(upload_to="")),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="event_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="events.eventtype"
            ),
        ),
        migrations.CreateModel(
            name="EventVideo",
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
                ("video", models.FileField(upload_to="")),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
            ],
        ),
    ]
