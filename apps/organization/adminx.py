#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 21:24
# @Author  : 张鹏辉
# @File    : adminx.py

import xadmin

from .models import CityDesc, CourseOrg


class CityDescAdmin(object):
    list_display = ['desc', 'name', 'add_time']
    list_filter = ['desc', 'name', 'add_time']
    search_fields = ['desc', 'name']


class CourseOrgAdmin(object):
    list_filter = ['name', 'description', 'click_numbers', 'favorite_numbers', 'images', 'address', 'city', 'add_time']
    list_display = ['name', 'description', 'click_numbers', 'favorite_numbers', 'images', 'address', 'city', 'add_time']
    search_fields = ['name', 'description', 'click_numbers', 'favorite_numbers', 'images', 'address', 'city']


xadmin.site.register(CityDesc, CityDescAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
