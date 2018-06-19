#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/18 23:07
# @Author  : 张鹏辉
# @File    : forms.py
from django import forms

from operation.models import UserAsk
import re


class UserAskForm(forms.ModelForm):
    """
    用户咨询models
    """
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

        '''这个方法必须以clean进行开头，可以对mobile进行自定义处置'''
    def clean_mobile(self):
        #其中clean_data方法也是固定的内置方法，可以进行调用获取内置的框架获取的值
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")