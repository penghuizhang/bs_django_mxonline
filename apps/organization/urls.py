#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 23:14
# @Author  : 张鹏辉
# @File    : urls.py
from django.conf.urls import url

from organization.views import OrgView, AddUserAskView, OrgHomeView,\
    OrgCourseView, OrgDescView, OrgTeacherView, AddFavView


urlpatterns = [
    # 机构首页
    url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),

    #机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),

]
