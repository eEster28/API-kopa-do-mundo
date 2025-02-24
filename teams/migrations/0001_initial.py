# Generated by Django 5.0.4 on 2024-04-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=30)),
                ("titles", models.IntegerField(default=0, null=True)),
                ("top_scorer", models.CharField(max_length=50)),
                ("fifa_code", models.CharField(max_length=3, unique=True)),
                ("first_cup", models.DateField(max_length=30, null=True)),
            ],
        ),
    ]
