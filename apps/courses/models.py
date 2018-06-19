# _*_ coding:utf-8 _*_

from django.db import models
from datetime import datetime
from organization.models import CourseOrg
from category.models import courseCategory
from users.models import UserProfile


# Create your models here.
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
    name = models.CharField(max_length=30, verbose_name=u"课程名")
    course_category = models.ForeignKey(courseCategory, verbose_name=u"课程归类", null=True, blank=True)
    description = models.CharField(max_length=30, verbose_name=u"课程描述")
    details = models.TextField(verbose_name=u"课程详情")
    degree = models.CharField(verbose_name=u"难度", choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")), max_length=3)
    learn_time = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
    students = models.IntegerField(default=0, verbose_name=u"学习课程人人数")
    favorite_student = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"课程封面图")
    click_numbers = models.IntegerField(default=0, verbose_name=u"点击数量")
    category = models.CharField(max_length=30, verbose_name=u"类别", default="后端开发")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    tag = models.CharField(max_length=100, verbose_name=u"标签", default="")
    lunBo = models.CharField(verbose_name=u"是否放到首页轮播", choices=(("1", u"是"), ("2", u"否")), max_length=2)
    user_list = models.TextField(verbose_name=u"学生学习自动加入该列表", default="", null=True, blank=True)

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zjs_number(self):
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_list_queryset(self, request):
        qs = super(Course, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(user=request.user.id)
        return qs.filter(user=request.user.id)


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名")
    desc = models.CharField(max_length=200, verbose_name=u"章节描述", default="", null=True, blank=True)
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
    name = models.CharField(verbose_name=u"视频", max_length=30)
    video_url = models.FileField(verbose_name=u"视频", upload_to="video/course/%Y/%m")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class LessonRecord(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u"播放章节")
    name = models.CharField(verbose_name=u"视频", max_length=30)
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    video_url = models.FileField(verbose_name=u"视频", upload_to="video/course/%Y/%m")
    add_time = models.DateTimeField(default="", verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户播放记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.lesson.name
