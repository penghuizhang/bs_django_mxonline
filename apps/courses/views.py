# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Course
# Create your views here.


class CourseListView(View):
    # //java  @RequestMapping
    def get(self, request):
        all_course = Course.objects.all().order_by("-add_time")

        # 热度排序
        sorts = request.GET.get('sort', "")

        #热度课程
        hot_course = Course.objects.all().order_by("-click_numbers")[:3]

        if sorts:
            if sorts == "hot":
                all_course = all_course.order_by("-students")
            elif sorts == "students":
                all_course = all_course.order_by("-click_numbers")

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_course, 3, request=request)
        course = p.page(page)

        return render(request, 'course-list.html', {
            'all_course': course,
            'sort': sorts,
            'hot_course': hot_course
        })


class CourseDetailView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        #增加课程点击数
        course.click_numbers += 1

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        course.save()
        return render(request, 'course-detail.html', {
            'course': course,
            "relate_courses" : relate_courses
        })



