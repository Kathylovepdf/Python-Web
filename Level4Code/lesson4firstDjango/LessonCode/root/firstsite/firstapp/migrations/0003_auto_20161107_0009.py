# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-11-07 00:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_aritcle'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aritcle',
            new_name='Article',
        ),
    ]
