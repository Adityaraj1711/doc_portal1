# Generated by Django 3.1.2 on 2022-04-08 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20220405_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='or_days',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='patient',
            name='follow_up_days',
            field=models.IntegerField(choices=[(0, 0), (10, 10), (15, 15), (20, 20), (30, 30), (45, 45), (60, 60)], default=10),
        ),
        migrations.AlterField(
            model_name='patient',
            name='in_time',
            field=models.TimeField(default=datetime.datetime(2022, 4, 8, 21, 59, 7, 701094)),
        ),
    ]
