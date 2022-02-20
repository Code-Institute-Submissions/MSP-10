# Generated by Django 4.0 on 2022-02-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('subscription', models.CharField(blank=True, max_length=50, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
