# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-08 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20161112_0442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='avatar',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='comment',
            name='createtime',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
