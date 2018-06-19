# _*_ coding:utf-8 _*_

from django.db import models
from datetime import datetime

# Create your models here.


class CityDesc(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"城市名称")
    desc = models.CharField(max_length=200, verbose_name=u"城市描述")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"机构名称")
    description = models.TextField(verbose_name=u"机构描述")
    category = models.CharField(verbose_name=u"机构类别", default="pxjg", max_length=20, choices=(("pxjg", "培训机构"), ("gx", "高校"), ("gr", "个人")))
    click_numbers = models.IntegerField(default=0, verbose_name=u"点击数量")
    favorite_numbers = models.IntegerField(default=0, verbose_name=u"收藏数量")
    images = models.ImageField(upload_to="org/%Y%m", verbose_name=u"机构封面")
    address = models.CharField(max_length=20, verbose_name=u"机构地址")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    courses_nums = models.IntegerField(default=0, verbose_name=u"课程数")
    city = models.ForeignKey(CityDesc, verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        #获取课程机构的教师数量
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name

