#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 11:52
# @Author  : 张鹏辉
# @File    : adminx.py
import xadmin
from .models import courseCategory


# Create your views here.
class courseCategoryAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']


# 对模型进行注册
xadmin.site.register(courseCategory, courseCategoryAdmin)