# Generated by Django 3.2.23 on 2024-01-19 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20240118_1224'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.AlterField(
            model_name='eventbooking',
            name='lesson_time',
            field=models.TimeField(default=datetime.time(8, 0)),
        ),
    ]
