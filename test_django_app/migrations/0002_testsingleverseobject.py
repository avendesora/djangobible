# Generated by Django 3.1.6 on 2021-02-10 23:25

from __future__ import annotations

from django.db import migrations, models

import djangobible.fields


class Migration(migrations.Migration):
    dependencies = [
        ("test_django_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TestSingleVerseObject",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("verse", djangobible.fields.VerseField()),
            ],
        ),
    ]
