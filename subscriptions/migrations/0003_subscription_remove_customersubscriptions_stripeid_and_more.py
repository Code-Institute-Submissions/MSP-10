# Generated by Django 4.0 on 2022-02-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_customersubscriptions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stripe_subscription_id', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='customersubscriptions',
            name='stripeid',
        ),
        migrations.AddField(
            model_name='customersubscriptions',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
