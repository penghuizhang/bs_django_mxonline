from django.db import models

from datetime import datetime

# Create your models here.


class courseCategory(models.Model):
    name = models.CharField(verbose_name=u"课程类别", max_length=30)
    nick = models.CharField(verbose_name=u"id", max_length=30)
    desc = models.CharField(verbose_name=u"描述", max_length=50)
    image = models.ImageField(verbose_name=u"分类", max_length=200, upload_to="fengmian/")
    add_time = models.DateTimeField(verbose_name=u"添加时间", default=datetime.now)

    class Meta:
        verbose_name = u"课程分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name