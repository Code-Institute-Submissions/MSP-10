# Generated by Django 4.0 on 2022-02-20 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0008_alter_customersubscriptions_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customersubscriptions',
            name='membership',
        ),
        migrations.RemoveField(
            model_name='customersubscriptions',
            name='price',
        ),
    ]
