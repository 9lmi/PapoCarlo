# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 23:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourapp', '0008_auto_20160118_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zakaz',
            name='zakaz1',
        ),
        migrations.AlterField(
            model_name='zakaz',
            name='list_deal',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 18, 23, 47, 40, 838493), verbose_name='Дата заказа'),
        ),
    ]
