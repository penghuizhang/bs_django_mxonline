#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 21:40
# @Author  : 张鹏辉
# @File    : adminx.py
import xadmin

from .models import UserAsk, CourseComments, \
    UserFavorite, UserMessage, UserCourse, UserNoteComment


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    list_filter = ['user', 'course', 'comment', 'add_time']
    search_fields = ['user', 'course', 'comment']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']


class UserMessageAdmin(object):
    list_filter = ['user', 'has_read', 'message', 'add_time']
    list_display = ['user', 'has_read', 'message', 'add_time']
    search_fields = ['user', 'has_read', 'message']


class UserCourseAdmin(object):
    list_filter = ['user', 'course', 'add_time']
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']


class UserNoteCommentAdmin(object):
    list_filter = ['course', 'note_message', 'add_time']
    list_display = ['course', 'note_message', 'add_time']
    search_fields = ['course', 'note_message']

xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserNoteComment, UserNoteCommentAdmin)

