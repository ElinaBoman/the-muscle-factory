# Generated by Django 3.2.23 on 2024-01-19 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_auto_20240119_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventbooking',
            name='lesson_time',
            field=models.TimeField(default='08:00'),
        ),
    ]