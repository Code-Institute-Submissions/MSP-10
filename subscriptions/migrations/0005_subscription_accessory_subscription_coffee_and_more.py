# Generated by Django 4.0 on 2022-02-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_subscription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='accessory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subscription',
            name='coffee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subscription',
            name='treats',
            field=models.IntegerField(default=0),
        ),
    ]
