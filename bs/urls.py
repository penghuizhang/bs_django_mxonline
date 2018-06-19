#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""bs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.views.static import serve
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ModifyPwdView, ResetUserView, LogoutView
from organization.views import OrgView
from bs.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^captcha/', include('captcha.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="active"),
    url(r'^forgetpwd/$', ForgetPwdView.as_view(), name="forgetpwd"),
    url(r'^reset/(?P<active_code>.*)/$', ResetUserView.as_view(), name="reset"),
    url(r'^modify/$', ModifyPwdView.as_view(), name="modifypwd"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    #课程机构地址配置
    url(r'^org/', include('organization.urls', namespace="org")),

    # 课程相关地址配置
    url(r'^course/', include('courses.urls', namespace="course")),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}, name="media"),


]