#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : on 2018/5/9.
# @Author  : kylin
import xadmin
from .models import Artical

class articalAdmin(object):
    list_display = ['title', 'author', 'content']
    list_filter = ['title', 'author', 'content']
    search_fields = ['title', 'author', 'content']
    exclude = ['readNum', 'pinglunNum', 'shareNum', 'addTime']
    style_fields = {"detail": "ueditor"}
    model_icon = 'fa fa-futbol-o'
xadmin.site.register(Artical, articalAdmin)