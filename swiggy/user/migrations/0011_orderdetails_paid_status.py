# Generated by Django 4.1 on 2022-09-01 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='paid_status',
            field=models.BooleanField(default=False),
        ),
    ]
