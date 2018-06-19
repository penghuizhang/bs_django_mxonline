#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 16:41
# @Author  : 张鹏辉
# @File    : email_send.py
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from bs.settings import EMAIL_FROM


def random_srt(randomlength=8):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_srt(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ""
    if send_type == "register":
        email_title = "激活链接"
        email_body = "请点击下面连接进行激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == "forget":
        email_title = "重置链接"

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
