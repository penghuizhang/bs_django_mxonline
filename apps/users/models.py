# _*_ coding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    name = models.CharField(max_length=50, verbose_name=u"教师姓名")
    work_year = models.IntegerField(default=0, verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
    work_position = models.CharField(max_length=40, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    click_numbers = models.IntegerField(default=0, verbose_name=u"点击量")
    favorite_numbers = models.IntegerField(default=0, verbose_name=u"收藏数量")
    course_number = models.IntegerField(default=0, verbose_name=u"发布课程数")
    is_authenticate = models.CharField(verbose_name=u"是否认证", default=False, max_length=5,
                                       choices=(("rz", "已认证"), ("wrz", "未认证")))
    add_time = models.DateTimeField(default=datetime.now)
    image = models.ImageField(default='', upload_to="teacher/%Y%m", verbose_name=u"教师头像")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=30, verbose_name=u"邮箱")
    send_type = models.CharField(verbose_name=u"验证码类型", choices=(("register", u"注册"), ("forget", u"找回密码")), max_length=10)
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=30, verbose_name=u"轮播图标题")
    images = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图")
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


#学生模型
class StudentProfile(models.Model):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    gender = models.CharField(max_length=20, verbose_name=u"性别", default="")
    city = models.CharField(max_length=20, verbose_name=u"城市", default="")
    province = models.CharField(max_length=20, verbose_name=u"省份", default="")
    country = models.CharField(max_length=20, verbose_name=u"国家", default="")
    image_url = models.CharField(verbose_name=u"微信获取头像", default="", max_length=150)
    userAccount = models.CharField(verbose_name=u"用户账号", default="", max_length=50)
    email = models.CharField(verbose_name=u"邮箱账号", max_length=30, default="")
    study_course = models.CharField(verbose_name=u"学习课程编号", max_length=150,default="")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
