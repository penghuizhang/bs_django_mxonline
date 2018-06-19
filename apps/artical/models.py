from django.db import models
from datetime import datetime


# Create your models here.
class Artical(models.Model):
    title = models.CharField(verbose_name=u"文章标题", max_length=50)
    author = models.CharField(verbose_name=u"作者", max_length=10)
    readNum = models.ImageField(verbose_name=u"阅读人数", max_length=5, default=0)
    pinglunNum = models.ImageField(verbose_name=u"评论人数", max_length=5, default=0)
    shareNum = models.ImageField(verbose_name=u"分享人数", max_length=5, default=0)
    content = models.TextField(verbose_name='课程详情', max_length=500)
    addTime = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"文章手记"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title