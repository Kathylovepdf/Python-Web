# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-14 10:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20190614_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='belong_to',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]