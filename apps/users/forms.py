#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/11 22:04
# @Author  : 张鹏辉
# @File    : forms.py
from django import forms
# import captcha.fields


class LoginForms(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForms(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ForgetForms(forms.Form):
    email = forms.EmailField(required=True)
    # captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ResetPwdForms(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
