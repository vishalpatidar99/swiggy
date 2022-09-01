# Generated by Django 4.1 on 2022-09-01 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_alter_restaurant_followers'),
        ('user', '0007_alter_orderdetails_dishesh_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetails',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.RemoveField(
            model_name='orderdetails',
            name='dishesh',
        ),
        migrations.AddField(
            model_name='orderdetails',
            name='dishesh',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.dish'),
            preserve_default=False,
        ),
    ]
