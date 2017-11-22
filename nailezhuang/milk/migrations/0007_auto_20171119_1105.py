# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0006_auto_20171116_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtype',
            name='foodprice',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='物品售价'),
        ),
        migrations.AlterField(
            model_name='foodrecord',
            name='foodcnt',
            field=models.PositiveIntegerField(default=1, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='foodtype',
            name='foodname',
            field=models.CharField(max_length=100, unique=True, verbose_name='物品名称'),
        ),
    ]
