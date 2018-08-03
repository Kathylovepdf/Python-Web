# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-02 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('views', models.IntegerField(blank=True, null=True)),
                ('favs', models.IntegerField(blank=True, null=True)),
                ('createtime', models.DateField(auto_now=True)),
            ],
        ),
    ]