# Generated by Django 5.1.1 on 2024-12-03 06:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("recommendations", "0009_delete_movie"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Watchlist",
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
                ("tmdb_id", models.IntegerField()),
                ("title", models.CharField(max_length=200)),
                ("poster_path", models.CharField(max_length=200)),
                ("overview", models.TextField(blank=True, null=True)),
                ("added_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="watchlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
