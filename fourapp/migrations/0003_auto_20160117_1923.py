# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 19:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourapp', '0002_zakaz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zakaz',
            name='summa',
        ),
        migrations.RemoveField(
            model_name='zakaz',
            name='zakaz',
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='last_deal',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 17, 19, 23, 43, 523586), verbose_name='Дата заказа'),
        ),
    ]
