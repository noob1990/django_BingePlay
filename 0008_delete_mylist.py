# Generated by Django 5.1.1 on 2024-11-29 05:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "recommendations",
            "0007_alter_rating_unique_together_remove_rating_movie_and_more",
        ),
    ]

    operations = [
        migrations.DeleteModel(
            name="MyList",
        ),
    ]
