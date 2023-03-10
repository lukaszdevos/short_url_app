# Generated by Django 4.1.7 on 2023-03-05 13:50

import django.core.validators
from django.db import migrations, models

import url_shortener.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Shortener",
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
                (
                    "long_url",
                    models.TextField(
                        unique=True, validators=[django.core.validators.URLValidator()]
                    ),
                ),
                (
                    "short_url",
                    models.CharField(
                        db_index=True,
                        default=url_shortener.models.generate_short_url,
                        max_length=10,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
