# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-16 06:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('milk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodcnt', models.IntegerField(verbose_name='数量')),
                ('foodmoney', models.FloatField(verbose_name='金额')),
                ('foodtime', models.DateTimeField(verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodname', models.CharField(max_length=100, verbose_name='物品名称')),
            ],
        ),
        migrations.AddField(
            model_name='foodrecord',
            name='foodtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='milk.FoodType'),
        ),
    ]
