# Generated by Django 4.0.4 on 2022-05-01 07:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=1000000),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.CharField(max_length=1000000),
        ),
    ]
