# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-17 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180429_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='email',
            field=models.CharField(default='', max_length=30, verbose_name='邮箱账号'),
        ),
    ]
