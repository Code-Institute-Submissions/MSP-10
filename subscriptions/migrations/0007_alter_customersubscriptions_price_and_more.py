# Generated by Django 4.0 on 2022-02-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_alter_customersubscriptions_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customersubscriptions',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
