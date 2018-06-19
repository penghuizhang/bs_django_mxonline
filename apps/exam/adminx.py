#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : on 2018/5/8.
# @Author  : kylin
import xadmin
from .models import examUnit


class examUnitAdmin(object):
    list_display = ['courseName', 'choise_type', 'add_time']
    list_filter = ['courseName', 'choise_type', 'add_time']
    search_fields = ['courseName', 'choise_type', 'add_time']
    exclude = ['answer_a', 'answer_b', 'studentId', 'choise_type']
    model_icon = 'fa  fa-rocket'
xadmin.site.register(examUnit, examUnitAdmin)

