# Generated by Django 5.0 on 2023-12-18 12:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0004_alter_client_email_alter_client_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="realestate",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="rentalregister",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
