# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-12 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20161105_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='score',
            field=models.FloatField(default=1.1),
        ),
        migrations.AlterField(
            model_name='article',
            name='createtime',
            field=models.DateField(auto_now=True),
        ),
    ]
