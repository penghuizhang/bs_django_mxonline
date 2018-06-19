#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/8 12:15
# @Author  : 张鹏辉
# @File    : adminx.py

import xadmin

from .models import EmailVerifyRecord, Banner, StudentProfile
from xadmin import views


'''网站名称和主题修改'''


class BaseSetting(object):
    enable_themes = True
    use_bootswatch  = True


"""页头页脚"""


class GlobalSetting(object):
    site_title = "后台管理"
    site_footer = "kylin"
    menu_style = "accordion"
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title', 'images', 'url', 'index', 'add_time']
    list_filter = ['title', 'images', 'url', 'index', 'add_time']
    search_fields = ['title', 'images', 'url', 'index']
xadmin.site.register(Banner, BannerAdmin)


class StudentAdmin(object):
    list_display = ["nick_name", 'gender', 'province', 'city']
    list_filter = ["nick_name", 'gender', 'province', 'city']
    search_fields = ["nick_name", 'gender', 'province', 'city']
    model_icon = 'fa fa-address-book'

    # 限制用户权限，只能看到自己编辑的文章
    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
xadmin.site.register(StudentProfile, StudentAdmin)







