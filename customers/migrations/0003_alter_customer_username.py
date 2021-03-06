# Generated by Django 4.0 on 2022-01-03 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('customers', '0002_customer_password_alter_customer_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.OneToOneField(max_length=30, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user'),
        ),
    ]
