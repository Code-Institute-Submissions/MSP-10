# Generated by Django 4.0 on 2022-01-02 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
