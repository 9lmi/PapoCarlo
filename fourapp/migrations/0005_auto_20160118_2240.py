# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 22:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourapp', '0004_auto_20160118_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakaz',
            name='last_deal',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 22, 40, 40, 59517), verbose_name='Дата заказа'),
        ),
    ]