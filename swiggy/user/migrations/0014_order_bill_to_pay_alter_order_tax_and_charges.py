# Generated by Django 4.1 on 2022-09-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_order_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bill_to_pay',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='tax_and_charges',
            field=models.FloatField(default=0),
        ),
    ]
