# Generated by Django 5.0 on 2023-12-13 13:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=200)),
                ("phone", models.CharField(max_length=15)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Cliente",
                "verbose_name_plural": "Clientes",
            },
        ),
        migrations.CreateModel(
            name="RealEstate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("code", models.CharField(max_length=100)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("APARTAMENTO", "APARTAMENTO"),
                            ("KITNET", "KITNET"),
                            ("CASA", "CASA"),
                        ],
                        max_length=100,
                    ),
                ),
                ("address", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_rented", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "Imóvel",
                "verbose_name_plural": "Imóveis",
            },
        ),
    ]
