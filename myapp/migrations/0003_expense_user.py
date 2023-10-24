# Generated by Django 4.2.6 on 2023-10-07 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("myapp", "0002_alter_expense_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="user",
            field=models.ForeignKey(
                default="Rohan223",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
