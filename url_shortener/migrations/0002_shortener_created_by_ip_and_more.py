# Generated by Django 4.1.7 on 2023-03-05 16:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("url_shortener", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shortener",
            name="created_by_ip",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="shortener",
            name="created_by_user_agent",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="shortener",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
    ]