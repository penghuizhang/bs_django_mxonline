# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-29 23:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='CourseName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='TeacherName',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='click_numbers',
            field=models.IntegerField(default=0, verbose_name='点击量'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='course_number',
            field=models.IntegerField(default=0, verbose_name='发布课程数'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='favorite_numbers',
            field=models.IntegerField(default=0, verbose_name='收藏数量'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y%m', verbose_name='教师头像'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_authenticate',
            field=models.CharField(choices=[('rz', '已认证'), ('wrz', '未认证')], default=False, max_length=5, verbose_name='是否认证'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name='教师姓名'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.CharField(default=1, max_length=50, verbose_name='教学特点'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_company',
            field=models.CharField(default=12, max_length=50, verbose_name='就职公司'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_position',
            field=models.CharField(default=1, max_length=40, verbose_name='公司职位'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='work_year',
            field=models.IntegerField(default=0, verbose_name='工作年限'),
        ),
    ]
