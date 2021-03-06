# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-29 23:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CityDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='城市名称')),
                ('desc', models.CharField(max_length=200, verbose_name='城市描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '城市',
                'verbose_name_plural': '城市',
            },
        ),
        migrations.CreateModel(
            name='CourseOrg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='机构名称')),
                ('description', models.TextField(verbose_name='机构描述')),
                ('category', models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=20, verbose_name='机构类别')),
                ('click_numbers', models.IntegerField(default=0, verbose_name='点击数量')),
                ('favorite_numbers', models.IntegerField(default=0, verbose_name='收藏数量')),
                ('images', models.ImageField(upload_to='org/%Y%m', verbose_name='机构封面')),
                ('address', models.CharField(max_length=20, verbose_name='机构地址')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('courses_nums', models.IntegerField(default=0, verbose_name='课程数')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CityDesc', verbose_name='所在城市')),
            ],
            options={
                'verbose_name': '课程机构',
                'verbose_name_plural': '课程机构',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='教师姓名')),
                ('work_year', models.IntegerField(default=0, verbose_name='工作年限')),
                ('work_company', models.CharField(max_length=50, verbose_name='就职公司')),
                ('work_position', models.CharField(max_length=40, verbose_name='公司职位')),
                ('points', models.CharField(max_length=50, verbose_name='教学特点')),
                ('click_numbers', models.IntegerField(default=0, verbose_name='点击量')),
                ('favorite_numbers', models.IntegerField(default=0, verbose_name='收藏数量')),
                ('course_number', models.IntegerField(default=0, verbose_name='发布课程数')),
                ('is_authenticate', models.CharField(choices=[('rz', '已认证'), ('wrz', '未认证')], default=False, max_length=5, verbose_name='是否认证')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('image', models.ImageField(default='', upload_to='teacher/%Y%m', verbose_name='教师头像')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.CourseOrg', verbose_name='所属机构')),
            ],
            options={
                'verbose_name': '教师',
                'verbose_name_plural': '教师',
            },
        ),
    ]
