#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : on 2018/4/29.
# @Author  : kylin
from django.db import models
from datetime import datetime
from courses.models import Course

# Create your models here.
class examUnit(models.Model):
    courseName = models.ForeignKey(Course, verbose_name=u"课程名称")
    studentId = models.CharField(verbose_name=u"学员姓名", max_length=40, null=True, blank=True)
    choise_type = models.CharField(verbose_name=u"选择题类型", max_length=20, default="单选")
    choise_name = models.TextField(verbose_name=u"选择题题目", max_length=30)
    answer_a = models.CharField(verbose_name=u"A", max_length=2, default=u"A")
    answer_b = models.CharField(verbose_name=u"B", max_length=2, default=u"B")
    answer = models.CharField(verbose_name=u"答案是:", choices=(("A", u"正确"), ("B", u"错误")), max_length=6)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"单选题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.courseName.name