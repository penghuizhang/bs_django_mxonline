# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-06 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usernotecomment',
            name='wxopenid',
            field=models.CharField(default='', max_length=40, verbose_name='用户openid'),
        ),
    ]
