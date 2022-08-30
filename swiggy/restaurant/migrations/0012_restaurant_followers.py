# Generated by Django 4.1 on 2022-08-30 07:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restaurant", "0011_alter_price_price_of_dish"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="followers",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="follow",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
