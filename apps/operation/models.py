# _*_ coding:utf-8 _*_

from datetime import datetime
from django.db import models

from users.models import StudentProfile
from courses.models import Course

# Create your models here.


class UserAsk(models.Model):
    """
    用户进行学习申请form申请
    """
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.CharField(max_length=11, verbose_name=u"手机")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 用户评论
class CourseComments(models.Model):
    """课程评,需要两个表，就需要将定义的两个表导入进来"""
    user = models.ForeignKey(StudentProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程名")
    comment = models.CharField(max_length=200, verbose_name=u"评论")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户收藏课程
class UserFavorite(models.Model):
    """用户收藏，将会使用user表和课程表，同时有"""
    user = models.ForeignKey(StudentProfile, verbose_name=u"用户名")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "教师")), verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程消息
class UserMessage(models.Model):
    openId = models.ForeignKey(StudentProfile, verbose_name=u"用户id")
    user = models.IntegerField(default=0, verbose_name=u"接收消息用户")
    message = models.CharField(max_length=500, verbose_name=u"消息内容")
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户参加那些课程?这里主要是参加实战课程进行记录
class UserCourse(models.Model):
    user = models.ForeignKey(StudentProfile, verbose_name=u"用户", default="")
    wxopenid = models.CharField(verbose_name="微信openid", default="", max_length=50)
    course = models.ForeignKey(Course, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户笔记
class UserNoteComment(models.Model):
    course = models.CharField(verbose_name=u"所属课程", default="", max_length=5)
    note_message = models.CharField(verbose_name=u"评论信息", max_length=500, default="")
    add_time = models.DateField(default=datetime.now, verbose_name=u"添加时间")
    user = models.ForeignKey(StudentProfile, verbose_name=u"用户", default="")
    wxopenid = models.CharField(verbose_name=u"用户openid", default="", max_length=40)

    class Meta:
        verbose_name = u"用户笔记"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.note_message

