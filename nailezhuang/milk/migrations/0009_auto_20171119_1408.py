# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-19 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0008_auto_20171119_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vipinfo',
            name='vipname',
            field=models.CharField(max_length=30, verbose_name='用户名'),
        ),
    ]
