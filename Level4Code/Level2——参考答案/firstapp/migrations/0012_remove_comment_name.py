# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0011_auto_20170802_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
