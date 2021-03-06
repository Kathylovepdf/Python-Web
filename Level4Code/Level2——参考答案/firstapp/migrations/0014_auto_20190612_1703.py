# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-06-12 09:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_auto_20170803_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('normal', 'normal')], max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('boy', '男'), ('girl', '女')], max_length=10),
        ),
    ]
