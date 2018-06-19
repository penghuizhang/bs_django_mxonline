#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 20:52
# @Author  : 张鹏辉
# @File    : adminx.py

import xadmin


from .models import Course, Lesson, Video


class CourseAdmin(object):
    list_display = ['name', 'description', 'course_category', 'details', 'degree', 'learn_time', 'students', 'favorite_student', 'click_numbers', 'add_time']
    list_filter = ['name', 'description', 'course_category', 'details', 'degree', 'learn_time', 'students', 'favorite_student', 'image', 'click_numbers', 'add_time']
    search_fields = ['name', 'description', 'course_category', 'details', 'degree', 'students', 'favorite_student', 'image', 'click_numbers']
    model_icon = 'fa fa-futbol-o'
    relfield_style = 'fk_ajax'

'''对LessonAdmin模型进行注册'''


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    model_icon = 'fa fa-folder-open'
    relfield_style = 'fk_ajax'

'''对video模型进行注册'''


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson', 'name', 'add_time']
    search_fields = ['course', 'name']
    model_icon = 'fa fa-file-video-o'
    relfield_style = 'fk_ajax'


class LessonRecordAdmin(object):
    list_display = ['lesson', 'user', 'add_time']
    list_filter = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']

# class CourseResourseAdmin(object):
#     list_display = ['course', 'name', 'add_time']
#     list_filter = ['course', 'name', 'add_time']
#     search_fields = ['course', 'name', 'download']


"""对上面的模型进行注册"""
# xadmin.site.register(CourseResourse, CourseResourseAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Course, CourseAdmin)
