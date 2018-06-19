# _*_ coding:utf-8 _*_
from django.contrib import admin
from users.models import UserProfile

# Register your models here.

'''
    用来进行注册后台管理系统的
'''


class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
