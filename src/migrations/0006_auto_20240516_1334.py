# Generated by Django 3.1.2 on 2024-05-16 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20220408_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='in_time',
            field=models.TimeField(default=datetime.datetime(2024, 5, 16, 19, 4, 35, 936388)),
        ),
    ]
