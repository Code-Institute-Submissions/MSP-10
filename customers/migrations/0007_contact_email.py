# Generated by Django 4.0 on 2022-02-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]