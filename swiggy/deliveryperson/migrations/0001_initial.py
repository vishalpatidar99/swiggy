# Generated by Django 4.1 on 2022-08-30 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DeliveryPerson",
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
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                ("vehicle_number", models.CharField(blank=True, max_length=100)),
                ("driving_licence_number", models.CharField(blank=True, max_length=15)),
                ("id_proof", models.FileField(blank=True, upload_to="media")),
                (
                    "vehicle_document_photo",
                    models.FileField(blank=True, upload_to="media"),
                ),
                (
                    "driving_licence_photo",
                    models.FileField(blank=True, upload_to="media"),
                ),
                ("verify", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
