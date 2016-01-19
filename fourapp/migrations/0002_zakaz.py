# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 05:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fourapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя заказчика')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон заказчика')),
                ('zakaz', models.CharField(max_length=255, verbose_name='Что заказал')),
                ('summa', models.IntegerField(default=0, verbose_name='Сумма заказа')),
                ('last_deal', models.DateTimeField(default=datetime.datetime(2016, 1, 10, 5, 56, 1, 935782), verbose_name='Дата заказа')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]