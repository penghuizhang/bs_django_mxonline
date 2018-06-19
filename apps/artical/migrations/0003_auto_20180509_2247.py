# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-09 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artical', '0002_auto_20180509_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='pinglunNum',
            field=models.ImageField(default=0, max_length=5, upload_to='', verbose_name='评论人数'),
        ),
        migrations.AlterField(
            model_name='artical',
            name='readNum',
            field=models.ImageField(default=0, max_length=5, upload_to='', verbose_name='阅读人数'),
        ),
        migrations.AlterField(
            model_name='artical',
            name='shareNum',
            field=models.ImageField(default=0, max_length=5, upload_to='', verbose_name='分享人数'),
        ),
    ]
