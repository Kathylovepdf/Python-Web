# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20170731_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('like', 'like'), ('normal', 'normal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(upload_to='profile_image'),
        ),
    ]
